txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Find isReady() function - what does it check?
idx = txt.find('isReady()')
print(f"isReady() at {idx}")
print(txt[idx-50:idx+400])

# Find loadHitMesh - what does it wait on
idx2 = txt.find('loadHitMesh')
print(f"\nloadHitMesh at {idx2}")
print(txt[idx2-50:idx2+400])

# Find the scene class beginning
idx3 = txt.find('async loadScene')
print(f"\nloadScene at {idx3}")
print(txt[idx3-50:idx3+600])
