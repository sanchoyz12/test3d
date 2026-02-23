import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Find introTexts array - the opening monologue
idx = txt.find('introTexts')
print(txt[idx:idx+1500])
