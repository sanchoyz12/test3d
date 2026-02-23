import urllib.request
import os
import re

base_url = "https://messenger.abeto.co"

def try_download(url_path):
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if os.path.exists(local_path):
        size = os.path.getsize(local_path)
        print(f"EXISTS ({size} bytes): {local_path}")
        return True
        
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': base_url+'/'})
        data = urllib.request.urlopen(req).read()
        
        # Check if it's an HTML fallback (404 page)
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

# Character animations: from the JS source we found these
avatar_files = [
    'avatar-bones',
    'avatar',
    'avatar-idle',
    'avatar-walk',
    'avatar-run',
    'avatar-air',
    'avatar-afk',
    'avatar-afk1',
    'avatar-afk2',
    'avatar-afk3',
    'avatar-sprint',
]

avatar_accessories = [
    'base',
    'hair1', 'hair2', 'hair3',
    'top1', 'top2', 'top3',
    'bottom1', 'bottom2', 'bottom3',
    'shoes1', 'shoes2', 'shoes3',
]

# Try variations with .drc extension
extensions = ['.drc', '.bin', '.glb']

print("=== Downloading avatar character files ===")
for anim in avatar_files:
    for ext in extensions:
        path = f'/assets/geometries/avatar/{anim}{ext}'
        try_download(path)

print("\n=== Downloading avatar accessories ===")
for acc in avatar_accessories:
    for ext in extensions:
        path = f'/assets/geometries/avatar/accessories/{acc}{ext}'
        try_download(path)
        
print("\n=== Downloading sounds that may be missing ===")
for fname in ['footsteps4.ogg', 'footsteps-water.ogg', 'jump-start.ogg', 'jump-land.ogg']:
    try_download(f'/assets/audio/character/{fname}')
    
print("\n=== Checking controls/circles ===")
try_download('/assets/images/controls/circles.avif')
