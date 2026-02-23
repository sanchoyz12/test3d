import urllib.request
import os

base_url = "https://messenger.abeto.co"

missing = [
    "/assets/images/grass-blades-highq.ktx2",
    "/assets/images/butterfly-highq.ktx2",
    "/assets/images/butterfly-front-highq.ktx2",
    "/assets/images/ui/npc-icons/inactive.icon",
    "/assets/images/ui/npc-icons/active.icon",
    "/assets/images/eye-highq.ktx2",
    "/assets/images/mouth-highq.ktx2",
    "/assets/images/tree-leaves.ktx2",
    "/assets/images/tree-leaves-detail.ktx2",
]

for url_path in missing:
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')

    if os.path.exists(local_path) and os.path.getsize(local_path) > 500:
        print(f"EXISTS: {local_path}")
        continue

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': base_url+'/'})
        data = urllib.request.urlopen(req).read()
        if b'<!DOCTYPE html>' in data[:100]:
            print(f"SKIP (server 404): {url_path}")
            continue
        with open(local_path, 'wb') as f:
            f.write(data)
        print(f"OK ({len(data)}b): {local_path}")
    except Exception as e:
        print(f"FAIL: {url_path} - {e}")
