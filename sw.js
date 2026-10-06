/* Capture Ideas — service worker.
 * Strategy:
 *  - App shell (HTML/manifest/icons): cache-first, so the app opens offline.
 *  - Ideas.md: network-first, so the board shows the freshest backlog when online
 *    and falls back to the last cached copy when offline.
 *  - GitHub API calls (api.github.com): never cached — always go to the network
 *    (writes must hit GitHub; reads need to be current). Handled by not matching.
 *
 * Bump CACHE_NAME whenever the shell files change so clients pick up the update.
 */
const CACHE_NAME = "capture-ideas-v1.1.0";

// Stable cache key for the backlog file (the app fetches it with a "?t="
// cache-buster; we normalise to this key so offline lookups still hit).
const IDEAS_KEY = "./Ideas.md";

const SHELL = [
  "./Ideas.html",
  "./Ideas.md",
  "./manifest.webmanifest",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/icon-maskable-512.png"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      // addAll fails if any file 404s; add individually so a missing icon
      // during early setup doesn't block install.
      .then(cache => Promise.allSettled(SHELL.map(url => cache.add(url))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", event => {
  const req = event.request;
  const url = new URL(req.url);

  // Only handle GET; let writes/others pass straight through.
  if (req.method !== "GET") return;

  // Never intercept GitHub API traffic — must always hit the network.
  if (url.hostname === "api.github.com") return;

  // Network-first for the backlog file so it stays fresh. Cache and match
  // under a stable key (IDEAS_KEY) so the "?t=" cache-buster on the request
  // doesn't cause an offline miss.
  if (url.pathname.endsWith("Ideas.md")) {
    event.respondWith(
      fetch(req)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE_NAME).then(c => c.put(IDEAS_KEY, copy)).catch(() => {});
          return res;
        })
        .catch(() => caches.match(IDEAS_KEY))
    );
    return;
  }

  // Cache-first for the shell and other same-origin assets.
  event.respondWith(
    caches.match(req).then(cached => {
      if (cached) return cached;
      return fetch(req).then(res => {
        // Cache successful same-origin GETs opportunistically.
        if (res.ok && url.origin === self.location.origin) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then(c => c.put(req, copy)).catch(() => {});
        }
        return res;
      });
    }).catch(() => caches.match("./Ideas.html"))
  );
});
