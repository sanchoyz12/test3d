import re
import urllib.request
import os

base_url = "https://messenger.abeto.co"
asset_urls = [
    '/assets/favicon32-BC0QIL61.png',
    '/assets/favicon16-B6JSd80n.png',
    '/assets/images/social.jpg',
    '/assets/style-BgpnrCnL.css',
    '/assets/webgl-C4v7tvuW.js',
    '/assets/runtime-C2kxzoFi.js',
    '/assets/App3D-BLRWK1h9.js'
]

# extract from output.txt
with open('output.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('assets/'):
        asset_urls.append('/' + line)
    elif not line.startswith('/'):
        # Many assets found in JS without "assets/" prefix actually live in /assets/
        asset_urls.append('/assets/' + line)
    else:
        asset_urls.append(line)

# Fetch all unique assets
asset_urls = list(set(asset_urls))

for url_path in asset_urls:
    full_url = base_url + url_path
    
    # local path (remove leading slash)
    local_path = url_path[1:]
    
    # skip if already downloaded and size > 0
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        continue
        
    print("Downloading", full_url, "to", local_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        urllib.request.urlretrieve(full_url, local_path)
        print("Success:", local_path)
    except Exception as e:
        print("Failed to download", full_url, e)

# Also fetch scene / levels if they are json or bin
