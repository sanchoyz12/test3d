import re
import urllib.request
import os

with open('assets/App3D-BLRWK1h9.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Any string containing an extension
matches = re.findall(r'["\']([^"\']+\.(?:ogg|drc|ktx2|icon|font|png|jpg|mp3|wav|bin|gltf|glb))["\']', text)

# For extensions like .font that are mapped with pathFonts
# Let's also extract those that are just the names like "planet" and ending in .font
matches2 = re.findall(r'["\']([a-zA-Z0-9_\-\.]+\.(?:font|icon|drc|ogg|ktx2))["\']', text)

all_matches = set(matches + matches2)
base_url = "https://messenger.abeto.co"

print(f"Found {len(all_matches)} potential valid assets")

def download_asset(url_path, local_dir_prefix="assets/"):
    # Fix paths
    if url_path.startswith('/'):
        url_path = url_path[1:]
    
    # Let's try to figure out the path if it doesn't have slashes
    if '/' not in url_path:
        # guess based on extension
        if url_path.endswith('.font'):
            url_path = "assets/fonts/" + url_path
        elif url_path.endswith('.icon'):
            url_path = "assets/images/" + url_path
        elif url_path.endswith('.drc'):
            pass # hard to guess, but we might try a few or ignore
    
    if not url_path.startswith(local_dir_prefix) and not url_path.startswith('font'):
         url_path = local_dir_prefix + url_path

    full_url = base_url + '/' + url_path
    local_path = url_path

    if os.path.exists(local_path) and os.path.getsize(local_path) > 1750:
        return True

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
            if len(data) > 1750: # Valid asset, not index.html
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                with open(local_path, 'wb') as out_file:
                    out_file.write(data)
                print(f"Success: {local_path} ({len(data)} bytes)")
                return True
    except Exception as e:
        pass
    return False

for m in all_matches:
    download_asset(m)
