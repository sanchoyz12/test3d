txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Now find terrain class and characters class - where do they wait?
idx = txt.find('characters,this.characterInitialOptions')
print(f"at {idx}")
print(txt[idx-100:idx+600])

# Also find the terrain class to see what terrain awaits
idx2 = txt.find('class terrain')
print(f"\nterrain class at {idx2}")
print(txt[idx2:idx2+600] if idx2 != -1 else 'not found')
