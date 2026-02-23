import urllib.request
import os

urls = [
    '/assets/libs/glyph/glyph.js',
    '/assets/libs/glyph/glyph.wasm'
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
