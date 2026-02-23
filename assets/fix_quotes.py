import os

js_files = ['assets/App3D-BLRWK1h9.js', 'assets/runtime-C2kxzoFi.js', 'assets/webgl-C4v7tvuW.js']
for f in js_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace occurrences of ""/assets with "/assets
        content = content.replace('""/assets', '"/assets')
        content = content.replace('.js""', '.js"')
        content = content.replace('.json""', '.json"')
        content = content.replace('.png""', '.png"')
        content = content.replace('.jpg""', '.jpg"')
        content = content.replace('.ktx2""', '.ktx2"')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed quotes in {f}")
