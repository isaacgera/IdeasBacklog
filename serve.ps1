# Serves the Ideas backlog viewer on a local server so Ideas.html can fetch Ideas.md.
# Run from this folder:  ./serve.ps1   then open http://localhost:8090/
$http = [System.Net.HttpListener]::new()
$http.Prefixes.Add("http://localhost:8090/")
$http.Start()
Write-Host "Ideas board running at http://localhost:8090/ - Press Ctrl+C to stop"

$mime = @{ '.html'='text/html'; '.js'='application/javascript'; '.json'='application/json'; '.md'='text/markdown'; '.css'='text/css'; '.png'='image/png' }

while ($http.IsListening) {
    $ctx = $http.GetContext()
    $path = $ctx.Request.Url.LocalPath
    if ($path -eq '/') { $path = '/Ideas.html' }
    $file = Join-Path $PSScriptRoot $path.TrimStart('/')
    if (Test-Path $file) {
        $ext = [System.IO.Path]::GetExtension($file)
        $ctx.Response.ContentType = if ($mime[$ext]) { $mime[$ext] } else { 'application/octet-stream' }
        $bytes = [System.IO.File]::ReadAllBytes($file)
        $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
    } else {
        $ctx.Response.StatusCode = 404
    }
    $ctx.Response.Close()
}
