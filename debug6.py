import re
txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()
idx = txt.find('createSkinAnimation')
print(txt[idx:idx+600])
