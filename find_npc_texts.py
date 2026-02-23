import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Find all NPC texts arrays - texts:[...] patterns with English
texts_pattern = re.findall(r'texts:\[([^\]]{10,500})\]', txt)
print(f"Found {len(texts_pattern)} texts arrays")
for t in texts_pattern[:30]:
    # Only show ones with English letters
    if re.search(r'[A-Za-z]{4,}', t) and '"' in t:
        strings = re.findall(r'"([^"]+)"', t)
        english = [s for s in strings if re.search(r'[A-Za-z]{4,}', s) and not s.startswith('http')]
        if english:
            print()
            for s in english:
                print(f'  "{s}"')
