import urllib.request
import os

base_url = "https://messenger.abeto.co"

def download_file(url_path):
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 2000:
        print(f"EXISTS ({os.path.getsize(local_path)} bytes): {local_path}")
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

# The terrain class loads these LOD variants:
# full_0...full_N.drc  (LOD0)
# full-lod-1_0...full-lod-1_N.drc  (LOD1)
# full-lod-2_0...full-lod-2_N.drc  (LOD2)
# full-lod-3_0...full-lod-3_N.drc  (LOD3)
# Also low/ variants for low memory devices

terrain = "present"  # scene's terrainOptions.terrain value

for lod in ["full-lod-2", "full-lod-3"]:
    for i in range(10):
        download_file(f'/assets/geometries/planets/{terrain}/{lod}_{i}.drc')

# Also check low/ variants
for lod in ["full", "full-lod-1", "full-lod-3"]:
    for i in range(10):
        download_file(f'/assets/geometries/planets/{terrain}/low/{lod}_{i}.drc')

print("\nDone!")
