import urllib.request
import os

base_url = "https://messenger.abeto.co"
urls = [
    '/assets/audio/music/bgmusic-highq.ogg',
    '/assets/audio/intro/letters.ogg',
    '/assets/audio/intro/button-turn.ogg',
    '/assets/audio/intro/button-out.ogg',
    '/assets/audio/intro/rune1.ogg',
    '/assets/audio/intro/rune2.ogg',
    '/assets/audio/intro/rune3.ogg',
    '/assets/audio/intro/rune4.ogg',
    '/assets/audio/ambiances/base.ogg',
    '/assets/audio/ambiances/forest.ogg',
    '/assets/audio/ambiances/city.ogg',
    '/assets/audio/ambiances/factory.ogg',
    '/assets/audio/ambiances/beach.ogg',
    '/assets/audio/ambiances/waterfalls.ogg',
    '/assets/audio/ambiances/temple.ogg',
    '/assets/audio/character/footsteps4.ogg',
    '/assets/audio/character/footsteps-water.ogg',
    '/assets/audio/character/jump-start.ogg',
    '/assets/audio/character/jump-land.ogg',
    '/assets/audio/character/emoji-starts1.ogg',
    '/assets/audio/character/emoji-starts2.ogg',
    '/assets/audio/character/emoji-starts3.ogg',
    '/assets/audio/character/emoji-ends1.ogg',
    '/assets/audio/character/emoji-ends2.ogg',
    '/assets/audio/character/emoji-ends3.ogg',
    '/assets/audio/character/clothes.ogg',
    '/assets/audio/character/bubble-starts.ogg',
    '/assets/audio/character/bubble-ends.ogg',
    '/assets/audio/camera/zoom-off-5.ogg',
    '/assets/audio/camera/zoom-in-5.ogg',
    '/assets/audio/camera/whoosh2.ogg',
    '/assets/audio/ui/title.ogg',
    '/assets/audio/ui/buttons2.ogg',
    '/assets/audio/ui/hover2.ogg',
    '/assets/audio/ui/click2.ogg',
    '/assets/audio/ui/click3.ogg',
    '/assets/audio/ui/openbox1.ogg',
    '/assets/audio/ui/openbox2.ogg',
    '/assets/audio/ui/openbox-emote.ogg',
    '/assets/audio/ui/openbox-checklist.ogg',
    '/assets/audio/ui/paper1.ogg',
    '/assets/audio/ui/paper4.ogg',
    '/assets/audio/ui/customize.ogg',
    '/assets/audio/ui/quest-complete.ogg',
    '/assets/audio/dialogues/quest.ogg',
    '/assets/audio/dialogues/male1.ogg',
    '/assets/audio/dialogues/male2.ogg',
    '/assets/audio/dialogues/male3.ogg',
    '/assets/audio/dialogues/female1.ogg',
    '/assets/audio/dialogues/female2.ogg',
    '/assets/audio/dialogues/female3.ogg',
    '/assets/audio/dialogues/wtf.ogg',
    '/assets/audio/music/musician.ogg',
    '/assets/images/lut.ktx2',
    '/assets/images/clouds_noise_64.ktx2',
    '/assets/images/clouds_noise_512.ktx2',
    '/assets/images/uv/uvchecker-srgb.ktx2',
    '/assets/images/noises-terrain.ktx2',
    '/assets/images/noise-simplex-layered-pixellated-highq.ktx2',
    '/assets/images/noise-simplex-layered-blur-highq.ktx2',
    '/assets/images/particle_sprites.ktx2',
    '/assets/images/water-noises-highq.ktx2',
    '/assets/images/galaxy.ktx2',
    '/assets/images/ui/sidebuttons/list.icon',
    '/assets/images/ui/sidebuttons/sound.icon',
    '/assets/images/ui/sidebuttons/sound-muted.icon',
    '/assets/images/ui/sidebuttons/t-shirt.icon',
    '/assets/images/ui/sidebuttons/poo.icon',
    '/assets/images/ui/arrow.icon',
    '/assets/images/ui/cross.icon',
    '/assets/images/ui/emojis/0.icon',
    '/assets/images/ui/emojis/1.icon',
    '/assets/images/ui/emojis/2.icon',
    '/assets/images/ui/emojis/3.icon',
    '/assets/images/ui/emojis/4.icon',
    '/assets/images/ui/emojis/5.icon',
    '/assets/images/ui/emojis/6.icon',
    '/assets/images/ui/emojis/7.icon',
    '/assets/images/ui/emojis/8.icon',
    '/assets/images/ui/emojis/9.icon',
    '/assets/geometries/planets/present/intro/planet.drc',
    '/assets/geometries/planets/present/intro/water.drc',
    '/assets/geometries/planets/present/intro/trees.drc',
    '/assets/geometries/planets/present/intro/clouds.drc',
    '/assets/geometries/planets/present/intro/title_vertical.drc',
    '/assets/geometries/planets/present/intro/button.drc',
    '/assets/geometries/planets/present/intro/galaxies.drc',
    '/assets/geometries/birds/1.drc',
    '/assets/geometries/birds/curve-1.drc',
    '/assets/geometries/planets/present/cables-1.drc',
    '/assets/geometries/planets/present/cables-2.drc',
    '/assets/geometries/planets/present/waterfall_vfx.drc',
    '/assets/geometries/planets/present/waterfallsplash_vfx.drc',
    '/assets/geometries/planets/present/waterfall_inlet_vfx.drc',
    '/assets/geometries/planets/intro/points.drc',
    '/assets/fonts/planet.font',
    '/assets/fonts/UglyDave-Alternates-optimized.font',
    '/assets/fonts/heading.font',
    '/assets/dracoworker-9mmlh0V-.js',
    '/assets/fonts/REM-Medium.font',
    '/assets/geometries/planets/present/intro/curve-0.drc',
    '/assets/geometries/planets/present/intro/curve-1.drc',
    '/assets/geometries/planets/present/intro/curve-2.drc',
    '/assets/geometries/planets/present/intro/curve-3.drc',
]

for url_path in urls:
    full_url = base_url + url_path
    local_path = url_path.lstrip('/')
    
    # Check if already downloaded and not empty (greater than 1705 bytes because 1701 bytes is index.html fallback)
    if os.path.exists(local_path) and os.path.getsize(local_path) > 1750:
        continue
    
    print("Downloading", full_url, "to", local_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        # Create a request with User-Agent header
        req = urllib.request.Request(
            full_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': '*/*',
                'Referer': 'https://messenger.abeto.co/'
            }
        )
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            print(f"Success: {local_path} ({len(data)} bytes)")
    except Exception as e:
        print("Failed to download", full_url, e)
