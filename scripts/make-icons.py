#!/usr/bin/env python3
"""Generate Capture Ideas PWA icons using only the Python standard library.

Draws a simple lightbulb glyph on the app's dark/accent palette and writes
three PNGs (192 any, 512 any, 512 maskable). No third-party deps (no Pillow).

Run from the Ideas/ folder:  python scripts/make-icons.py
"""
import os
import zlib
import struct
import math

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "icons")

# Palette (matches the app tokens)
BG_TOP = (22, 32, 58)      # #16203a
BG_BOT = (15, 20, 32)      # #0f1420
ACCENT = (91, 141, 239)    # #5b8def
GREEN = (63, 185, 140)     # #3fb98c
BULB = (245, 248, 255)     # near-white
FILAMENT = (224, 169, 74)  # amber


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def make_canvas(size, maskable):
    """Return a size*size list of (r,g,b) pixels."""
    px = [[(0, 0, 0)] * size for _ in range(size)]
    cx = cy = size / 2.0

    # Rounded-square background with a subtle top-to-bottom gradient.
    # Maskable icons need the art inside the safe zone, so we fill the whole
    # square (no rounded corners) and keep the glyph smaller.
    radius = size * 0.22
    for y in range(size):
        for x in range(size):
            t = y / (size - 1)
            col = lerp(BG_TOP, BG_BOT, t)
            if not maskable:
                # rounded corners -> transparent-ish (paint bg colour anyway;
                # PNG here is opaque, corners just use the darkest bg)
                inside = _rounded_inside(x, y, size, radius)
                if not inside:
                    col = BG_BOT
            px[y][x] = col

    # Accent ring glow behind the bulb.
    scale = 0.62 if maskable else 0.74
    _draw_glow(px, size, cx, cy, size * 0.30 * scale, ACCENT, 0.18)

    # Lightbulb: a circle (glass) + a small base (screw).
    bulb_r = size * 0.20 * scale
    bulb_cy = cy - size * 0.04
    _draw_disc(px, size, cx, bulb_cy, bulb_r, BULB)
    # inner filament hint
    _draw_disc(px, size, cx, bulb_cy, bulb_r * 0.42, FILAMENT)
    _draw_disc(px, size, cx, bulb_cy, bulb_r * 0.20, BULB)

    # Base (rounded rectangle) under the bulb.
    bw = bulb_r * 0.9
    bh = bulb_r * 0.7
    top = bulb_cy + bulb_r * 0.85
    for y in range(size):
        for x in range(size):
            if (cx - bw / 2) <= x <= (cx + bw / 2) and top <= y <= (top + bh):
                px[y][x] = lerp(BG_TOP, GREEN, 0.55)
    return px


def _rounded_inside(x, y, size, radius):
    # corners
    for (ox, oy) in ((radius, radius), (size - radius, radius),
                     (radius, size - radius), (size - radius, size - radius)):
        pass
    # Simpler: distance test on each corner region
    r = radius
    if x < r and y < r:
        return (x - r) ** 2 + (y - r) ** 2 <= r * r
    if x > size - r and y < r:
        return (x - (size - r)) ** 2 + (y - r) ** 2 <= r * r
    if x < r and y > size - r:
        return (x - r) ** 2 + (y - (size - r)) ** 2 <= r * r
    if x > size - r and y > size - r:
        return (x - (size - r)) ** 2 + (y - (size - r)) ** 2 <= r * r
    return True


def _draw_disc(px, size, cx, cy, r, colour):
    r2 = r * r
    y0, y1 = max(0, int(cy - r)), min(size - 1, int(cy + r))
    x0, x1 = max(0, int(cx - r)), min(size - 1, int(cx + r))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r2:
                px[y][x] = colour


def _draw_glow(px, size, cx, cy, r, colour, strength):
    r2 = r * r
    y0, y1 = max(0, int(cy - r)), min(size - 1, int(cy + r))
    x0, x1 = max(0, int(cx - r)), min(size - 1, int(cx + r))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            if d2 <= r2:
                t = (1 - math.sqrt(d2) / r) * strength
                px[y][x] = lerp(px[y][x], colour, t)


def write_png(path, px, size):
    raw = bytearray()
    for y in range(size):
        raw.append(0)  # filter type 0
        for x in range(size):
            raw.extend(px[y][x])
    compressed = zlib.compress(bytes(raw), 9)

    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        crc = zlib.crc32(tag + data) & 0xFFFFFFFF
        return c + struct.pack(">I", crc)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)  # 8-bit RGB
    with open(path, "wb") as f:
        f.write(sig)
        f.write(chunk(b"IHDR", ihdr))
        f.write(chunk(b"IDAT", compressed))
        f.write(chunk(b"IEND", b""))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, size, maskable in (
        ("icon-192.png", 192, False),
        ("icon-512.png", 512, False),
        ("icon-maskable-512.png", 512, True),
    ):
        px = make_canvas(size, maskable)
        out = os.path.join(OUT_DIR, name)
        write_png(out, px, size)
        print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    main()
