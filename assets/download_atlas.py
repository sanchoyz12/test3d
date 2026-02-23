import urllib.request
import os

urls = [
    '/assets/images/atlas.png',
    '/assets/images/uv/uvchecker-srgb.png',
    '/assets/draco_wasm_wrapper.js',
    '/assets/draco_decoder.wasm'
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

# Let's also download the rest of images if they exist
import glob
for f in glob.glob('assets/*.js') + glob.glob('assets/*/*.js'):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    import re
    matches = set(re.findall(r'[\'"]([a-zA-Z0-9_\-\./]+\.(?:png|jpg|jpeg|json|bin|glb))[\'"]', txt))
    for m in matches:
        if not m.startswith('/'):
            m = '/' + m
        url_path = m
        if not url_path.startswith('/assets/'):
            url_path = '/assets' + url_path
            
        local_path = url_path.lstrip('/')
        if not os.path.exists(local_path):
            full_url = base_url + url_path
            try:
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
                data = urllib.request.urlopen(req).read()
                with open(local_path, 'wb') as out_file:
                    out_file.write(data)
                print(f"Auto-downloaded: {local_path} ({len(data)} bytes)")
            except Exception as e:
                # Some might not exist
                pass

