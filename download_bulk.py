import urllib.request
import os

base_url = "https://messenger.abeto.co"

missing = [
    "/assets/geometries/deliveries/note.drc",
    "/assets/geometries/deliveries/postcard.drc",
    "/assets/geometries/deliveries/clothes.drc",
    "/assets/geometries/deliveries/samplebox.drc",
    "/assets/geometries/deliveries/offering.drc",
    "/assets/geometries/deliveries/letterwet.drc",
    "/assets/geometries/emojis/1.drc",
    "/assets/geometries/emojis/2.drc",
    "/assets/geometries/emojis/3.drc",
    "/assets/geometries/emojis/4.drc",
    "/assets/geometries/emojis/5.drc",
    "/assets/geometries/emojis/6.drc",
    "/assets/geometries/emojis/7.drc",
    "/assets/geometries/emojis/8.drc",
    "/assets/geometries/emojis/9.drc",
    "/assets/geometries/emojis/10.drc",
    "/assets/geometries/planets/present/water.drc",
    "/assets/geometries/planets/present/beachfoam_vfx.drc",
    "/assets/geometries/planets/present/smoke-1.drc",
    "/assets/geometries/planets/present/grass.drc",
    "/assets/geometries/planets/present/butterflies.drc",
    "/assets/geometries/planets/present/tree-leaves_0.drc",
    "/assets/geometries/planets/present/tree-leaves_1.drc",
    "/assets/geometries/planets/present/tree-leaves_2.drc",
    "/assets/geometries/planets/present/tree-leaves_3.drc",
    "/assets/geometries/planets/present/tree-leaves_4.drc",
    "/assets/geometries/birds/2.drc",
    "/assets/geometries/birds/curve-2.drc",
    # NPCs - office-worker
    "/assets/geometries/npcs/present/office-worker/office-worker.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-alt.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-bones.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-idle.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-talk.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-walk.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-walk-alt.drc",
    "/assets/geometries/npcs/present/office-worker/office-worker-idle-talk.drc",
    # NPCs - chef
    "/assets/geometries/npcs/present/chef/chef.drc",
    "/assets/geometries/npcs/present/chef/chef-bones.drc",
    "/assets/geometries/npcs/present/chef/chef-idle.drc",
    # NPCs - tall-man
    "/assets/geometries/npcs/present/tall-man-curve.drc",
    # NPCs - caveman
    "/assets/geometries/npcs/present/caveman/caveman.drc",
    "/assets/geometries/npcs/present/caveman/caveman-bones.drc",
    "/assets/geometries/npcs/present/caveman/caveman-idle.drc",
    # NPCs - boss
    "/assets/geometries/npcs/present/boss/boss.drc",
    "/assets/geometries/npcs/present/boss/boss-bones.drc",
    "/assets/geometries/npcs/present/boss/boss-idle.drc",
    # NPCs - young-lady
    "/assets/geometries/npcs/present/young-lady/young-lady.drc",
    "/assets/geometries/npcs/present/young-lady/young-lady-bones.drc",
    "/assets/geometries/npcs/present/young-lady/young-lady-idle.drc",
    "/assets/geometries/npcs/present/young-lady/young-lady-talk.drc",
    "/assets/geometries/npcs/present/young-lady/young-lady-talk-idle.drc",
    # NPCs - scout
    "/assets/geometries/npcs/present/scout/scout.drc",
    "/assets/geometries/npcs/present/scout/scout-bones.drc",
    "/assets/geometries/npcs/present/scout/scout-idle.drc",
    # NPCs - threekid
    "/assets/geometries/npcs/present/threekid/threekid.drc",
    "/assets/geometries/npcs/present/threekid/threekid-bones.drc",
    "/assets/geometries/npcs/present/threekid/threekid-idle.drc",
    # NPCs - factory-worker-a
    "/assets/geometries/npcs/present/factory-worker-a/factory-worker-a.drc",
    "/assets/geometries/npcs/present/factory-worker-a/factory-worker-a-bones.drc",
    "/assets/geometries/npcs/present/factory-worker-a/factory-worker-a-idle.drc",
    # NPCs - factory-worker-b
    "/assets/geometries/npcs/present/factory-worker-b/factory-worker-b.drc",
    "/assets/geometries/npcs/present/factory-worker-b/factory-worker-b-bones.drc",
    "/assets/geometries/npcs/present/factory-worker-b/factory-worker-b-walk.drc",
    "/assets/geometries/npcs/present/factory-worker-b/factory-worker-b-talk.drc",
    "/assets/geometries/npcs/present/factory-worker-b/curve-1.drc",
    # NPCs - female-scientist
    "/assets/geometries/npcs/present/female-scientist/female-scientist.drc",
    "/assets/geometries/npcs/present/female-scientist/female-scientist-bones.drc",
    "/assets/geometries/npcs/present/female-scientist/female-scientist-idle.drc",
    # NPCs - factory-worker-c
    "/assets/geometries/npcs/present/factory-worker-c/factory-worker-c.drc",
    "/assets/geometries/npcs/present/factory-worker-c/factory-worker-c-bones.drc",
    "/assets/geometries/npcs/present/factory-worker-c/factory-worker-c-idle.drc",
    # NPCs - alien
    "/assets/geometries/npcs/present/alien/alien.drc",
    "/assets/geometries/npcs/present/alien/alien-bones.drc",
    "/assets/geometries/npcs/present/alien/alien-idle.drc",
    # NPCs - male-scientist
    "/assets/geometries/npcs/present/male-scientist/male-scientist.drc",
    "/assets/geometries/npcs/present/male-scientist/male-scientist-bones.drc",
    "/assets/geometries/npcs/present/male-scientist/male-scientist-idle.drc",
    # NPCs - diver
    "/assets/geometries/npcs/present/diver/diver.drc",
    "/assets/geometries/npcs/present/diver/diver-bones.drc",
    "/assets/geometries/npcs/present/diver/diver-idle.drc",
    "/assets/geometries/npcs/present/diver/diver-talk.drc",
    "/assets/geometries/npcs/present/diver/diver-talk-idle.drc",
    # NPCs - mountainman
    "/assets/geometries/npcs/present/mountainman/mountainman.drc",
    "/assets/geometries/npcs/present/mountainman/mountainman-bones.drc",
    "/assets/geometries/npcs/present/mountainman/mountainman-idle.drc",
    # NPCs - oldwoman
    "/assets/geometries/npcs/present/oldwoman/oldwoman.drc",
    "/assets/geometries/npcs/present/oldwoman/oldwoman-bones.drc",
    "/assets/geometries/npcs/present/oldwoman/oldwoman-idle.drc",
    # NPCs - musician
    "/assets/geometries/npcs/present/musician/musician.drc",
    "/assets/geometries/npcs/present/musician/musician-bones.drc",
    "/assets/geometries/npcs/present/musician/musician-idle.drc",
    "/assets/geometries/npcs/present/musician/musician-talk.drc",
    # NPCs - fox
    "/assets/geometries/npcs/present/fox/fox.drc",
    "/assets/geometries/npcs/present/fox/fox-bones.drc",
    "/assets/geometries/npcs/present/fox/fox-idle.drc",
    # NPCs - owl
    "/assets/geometries/npcs/present/owl/owl.drc",
    "/assets/geometries/npcs/present/owl/owl-bones.drc",
    "/assets/geometries/npcs/present/owl/owl-idle.drc",
]

ok = 0
skip = 0
fail = 0

for url_path in missing:
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 500:
        ok += 1
        continue
    
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(full_url, headers={
            'User-Agent': 'Mozilla/5.0',
            'Referer': base_url + '/'
        })
        data = urllib.request.urlopen(req).read()
        if b'<!DOCTYPE html>' in data[:100]:
            print(f"SKIP (no file on server): {url_path}")
            skip += 1
            continue
        with open(local_path, 'wb') as f:
            f.write(data)
        print(f"OK ({len(data)}b): {local_path}")
        ok += 1
    except Exception as e:
        print(f"FAIL: {url_path} - {e}")
        fail += 1

print(f"\nDone: {ok} downloaded, {skip} skipped (not on server), {fail} failed")
