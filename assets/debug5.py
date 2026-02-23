txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Continue finding terrain init - see ALL the files it loads
idx = txt.find('class terrain')
print(txt[idx:idx+2000])
