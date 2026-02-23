import urllib.request
import os

base_url = "https://messenger.abeto.co"

def download_file(url_path, force=False):
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if not force and os.path.exists(local_path) and os.path.getsize(local_path) > 2000:
        return True
        
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': base_url+'/'})
        data = urllib.request.urlopen(req).read()
        
        if b'<!DOCTYPE html>' in data[:100]:
            print(f"SKIP (HTML fallback): {url_path}")
            return False
            
        with open(local_path, 'wb') as f:
            f.write(data)
        print(f"DOWNLOADED ({len(data)} bytes): {local_path}")
        return True
    except Exception as e:
        print(f"FAILED: {url_path} - {e}")
        return False

# Missing animation files
missing_avatars = [
    '/assets/geometries/avatar/avatar-walk.drc',
    '/assets/geometries/avatar/avatar-afk.drc',
]
for url in missing_avatars:
    download_file(url)

# Fix hitmesh files that got 1701-byte HTML fallback (too small to be valid)
import os
problem_files = []
for i in range(10):
    path = f'assets/geometries/planets/present/hitmesh_{i}.drc'
    if os.path.exists(path) and os.path.getsize(path) <= 2000:
        problem_files.append(path)
        url = '/' + path
        print(f"Re-downloading {path} (too small: {os.path.getsize(path)} bytes)...")
        download_file(url, force=True)

print("Done! Fixed files:", problem_files)
