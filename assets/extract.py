import re
import sys

def extract_strings(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    matches = set(re.findall(r'["\']([^"\']{5,200})["\']', text))
    
    strings = []
    for m in matches:
        if re.search(r'[A-Za-z]', m) and ' ' in m:
            if not '{' in m and not '/' in m and not '\\' in m:
                strings.append(m)
    
    strings.sort()
    return strings

all_strings = []
all_strings.append("--- webgl-C4v7tvuW.js ---")
all_strings.extend(extract_strings('assets/webgl-C4v7tvuW.js'))
all_strings.append("--- App3D-BLRWK1h9.js ---")
all_strings.extend(extract_strings('assets/App3D-BLRWK1h9.js'))
all_strings.append("--- runtime-C2kxzoFi.js ---")
all_strings.extend(extract_strings('assets/runtime-C2kxzoFi.js'))

with open('strings.txt', 'w', encoding='utf-8') as f:
    for s in all_strings:
        f.write(s + '\n')
