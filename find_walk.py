import urllib.request

attempts = [
    'https://messenger.abeto.co/assets/geometries/avatar/avatar-walk.drc',
    'https://messenger.abeto.co/assets/geometries/avatar/walk.drc',
    'https://messenger.abeto.co/assets/geometries/avatar/avatar-walking.drc',
    'https://messenger.abeto.co/assets/geometries/avatar/avatar-afk.drc',
    'https://messenger.abeto.co/assets/geometries/avatar/afk.drc'
]
for url in attempts:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        data = urllib.request.urlopen(req).read()
        is_html = b'<!DOCTYPE' in data[:50]
        print(f'{url}: {len(data)} bytes, is_html={is_html}')
    except Exception as e:
        print(f'{url}: ERROR {e}')
