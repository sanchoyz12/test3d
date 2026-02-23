import urllib.request
import os

base_url = "https://messenger.abeto.co"

def download_file(url_path):
    if not url_path.startswith('/'):
        url_path = '/' + url_path
    
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 2000:
        return True
        
    print(f"Downloading {full_url}...")
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read()
            with open(local_path, 'wb') as f:
                f.write(data)
            print(f"Saved {local_path} ({len(data)} bytes)")
            return True
    except Exception as e:
        print(f"Failed {url_path}: {e}")
        return False

urls = [
    '/assets/charactergeoworker-D8pdYVWP.js',
    '/assets/collisionworker-eT5h7hIA.js',
    '/assets/geometries/avatar/avatar-bones.drc',
    '/assets/geometries/avatar/avatar-idle.drc',
    '/assets/geometries/avatar/avatar-run.drc',
    '/assets/geometries/avatar/accessories/base.drc',
    '/assets/geometries/avatar/accessories/hair1.drc',
    '/assets/geometries/avatar/accessories/hair2.drc',
    '/assets/geometries/avatar/accessories/hair3.drc',
    '/assets/geometries/avatar/accessories/top1.drc',
    '/assets/geometries/avatar/accessories/top2.drc',
    '/assets/geometries/avatar/accessories/top3.drc',
    '/assets/geometries/avatar/accessories/bottom1.drc',
    '/assets/geometries/avatar/accessories/bottom2.drc',
    '/assets/geometries/avatar/accessories/bottom3.drc',
    '/assets/geometries/avatar/accessories/shoes1.drc',
    '/assets/geometries/avatar/accessories/shoes2.drc',
    '/assets/geometries/avatar/accessories/shoes3.drc',
    '/assets/images/mainchar-eye-highq.ktx2',
    '/assets/images/controls/circles.avif',
    '/assets/images/trails-noise.ktx2'
]

# Add hitmesh and lod files
for i in range(10):
    urls.append(f'/assets/geometries/planets/present/hitmesh_{i}.drc')
    urls.append(f'/assets/geometries/planets/present/full-lod-1_{i}.drc')

for url in urls:
    download_file(url)

# Patch the new workers
import re
new_workers = ['assets/charactergeoworker-D8pdYVWP.js', 'assets/collisionworker-eT5h7hIA.js']
for w in new_workers:
    if os.path.exists(w):
        with open(w, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Consistent patch for libs path
        pattern = r'(const |let |var )([a-zA-Z_0-9]+)\=\`\$\{[a-zA-Z_0-9]+\.substring\(0,[a-zA-Z_0-9]+\.lastIndexOf\("/"\)\)\}/libs/\`'
        def repl(match):
            return f'{match.group(1)}{match.group(2)}="/assets/libs/"'
        content = re.sub(pattern, repl, content)
        
        # Some workers might use a different style
        content = content.replace('}/libs/`', '}/assets/libs/`')
        
        with open(w, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched worker: {w}")
