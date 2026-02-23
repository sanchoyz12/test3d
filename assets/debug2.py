txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()
# collisionworker initialization - that's what ready waits on
idx = txt.find('collisionworker')
print(f"collisionworker found at {idx}")
print(txt[idx-100:idx+400])
# Find the hitmesh count
idx2 = txt.find('hitmesh_')
print(f"\nhitmesh_ found at {idx2}")
print(txt[idx2-200:idx2+300])
