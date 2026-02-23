import urllib.request
import os

urls = [
    '/assets/glyphworker-DoaYwstb.js',
    '/assets/bitmapworker-DtCLhbWB.js',
    '/assets/geometryworker-WyEueJn9.js'
]

base_url = "https://messenger.abeto.co"

for url_path in urls:
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    print("Downloading", full_url, "to", local_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        req = urllib.request.Request(
            full_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Accept': '*/*'
            }
        )
        with urllib.request.urlopen(req) as response:
            data = response.read()
            with open(local_path, 'wb') as out_file:
                out_file.write(data)
            print(f"Success: {local_path} ({len(data)} bytes)")
    except Exception as e:
        print("Failed to download", full_url, e)

js_files = ['assets/App3D-BLRWK1h9.js', 'assets/runtime-C2kxzoFi.js', 'assets/webgl-C4v7tvuW.js']
for f in js_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Fix the dracoworker path that I broke
        content = content.replace("`${client$1.absolutePath}/assets/dracoworker-9mmlh0V-.js`", '"/assets/dracoworker-9mmlh0V-.js"')
        content = content.replace("`${client$1.absolutePath}/assets/dracoworker", '"/assets/dracoworker')
        
        # In case the other workers also have messenger.abeto.co hardcoded in them, but my previous patch removed `https://messenger.abeto.co`.
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed {f}")
