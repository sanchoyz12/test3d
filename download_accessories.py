import urllib.request
import os

base_url = "https://messenger.abeto.co"

def try_download(url_path):
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 500:
        return True
        
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': base_url+'/'})
        data = urllib.request.urlopen(req).read()
        
        if b'<!DOCTYPE html>' in data[:100]:
            return False
            
        with open(local_path, 'wb') as f:
            f.write(data)
        print(f"OK ({len(data)}b): {local_path}")
        return True
    except Exception as e:
        return False

categories = ['hair', 'top', 'bottom', 'shoes']
for cat in categories:
    for i in range(20):
        try_download(f'/assets/geometries/avatar/accessories/{cat}{i}.drc')

print("Done checking accessories.")
