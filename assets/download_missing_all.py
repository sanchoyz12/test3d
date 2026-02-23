import urllib.request
import os
import re

base_url = "https://messenger.abeto.co"

def download_file(url_path):
    if not url_path.startswith('/'):
        url_path = '/' + url_path
    
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 2000:
        return True # Already exists and not a tiny fallback
        
    print(f"Downloading {full_url}...")
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        req = urllib.request.Request(
            full_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': '*/*',
                'Referer': 'https://messenger.abeto.co/'
            }
        )
        with urllib.request.urlopen(req) as response:
            data = response.read()
            if len(data) < 2000 and b'<!DOCTYPE html>' in data:
                print(f"Skipping {url_path} - looks like HTML fallback")
                return False
            with open(local_path, 'wb') as f:
                f.write(data)
            print(f"Saved {local_path} ({len(data)} bytes)")
            return True
    except Exception as e:
        print(f"Failed to download {url_path}: {e}")
        return False

# 1. Identified 404s
missing_known = [
    '/assets/geometries/planets/present/full_2.drc',
    '/assets/geometries/planets/present/full_4.drc',
    '/assets/geometries/planets/present/full_6.drc',
    '/assets/geometries/planets/present/full_7.drc',
    '/assets/geometries/planets/present/full_8.drc',
    '/assets/geometries/planets/present/full_9.drc',
    '/assets/images/mainchar-eye-highq.ktx2',
    '/assets/images/trails-noise.ktx2',
    '/assets/controls/circles.avif',
    '/assets/images/atlas.png'
]

# Guessing other full_N.drc
for i in range(20):
    missing_known.append(f'/assets/geometries/planets/present/full_{i}.drc')

# 2. Extract from JS
js_files = ['assets/App3D-BLRWK1h9.js', 'assets/runtime-C2kxzoFi.js', 'assets/webgl-C4v7tvuW.js']
extracted_urls = set()

for js_file in js_files:
    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Match assets/ path or similar
            matches = re.findall(r'["\']((?:assets/|/assets/)[a-zA-Z0-9_\-\./\%]+\.(?:drc|ktx2|png|jpg|jpeg|ogg|mp3|wav|font|icon|avif|glb|gltf|bin|json))["\']', content)
            for m in matches:
                extracted_urls.add(m)

for url in missing_known:
    download_file(url)

for url in extracted_urls:
    download_file(url)
