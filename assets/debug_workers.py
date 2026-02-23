import re
import urllib.request
import os

# Read the charactergeoworker and check for how it resolves files
txt = open('assets/charactergeoworker-D8pdYVWP.js', encoding='utf-8', errors='ignore').read()
# find any URL or path references
matches = re.findall(r'["\']([^"\']+\.(?:drc|js|wasm))["\']', txt)
print("charactergeoworker refs:")
for m in set(matches):
    print(" ", m)

txt2 = open('assets/collisionworker-eT5h7hIA.js', encoding='utf-8', errors='ignore').read()
matches2 = re.findall(r'["\']([^"\']+\.(?:drc|js|wasm))["\']', txt2)
print("\ncollisionworker refs:")
for m in set(matches2):
    print(" ", m)
    
# Also check: does collisionworker use /libs/ somewhere?
idx = txt2.find('/libs/')
print("\ncollisionworker /libs/ found at:", idx)
if idx != -1:
    print(txt2[idx-100:idx+200])

# Check for imports
idx2 = txt2.find('await import')
print("\ncollisionworker import at:", idx2)
if idx2 != -1:
    print(txt2[idx2-10:idx2+200])
