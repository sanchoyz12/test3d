import re

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# The problematic check:
# if a.some(p => p.type === "BoxGeometry") || o.type === "BoxGeometry" || l.some(p => p.tracks.length === 0)
# We want to keep checking model/bones failures, but skip the animation check
# so the game loads even without some animations.

old_check = 'a.some(p=>p.type==="BoxGeometry")||o.type==="BoxGeometry"||l.some(p=>p.tracks.length===0)'
new_check = 'a.some(p=>p.type==="BoxGeometry")||o.type==="BoxGeometry"'

count = txt.count(old_check)
print(f"Found {count} occurrences of old check")

txt = txt.replace(old_check, new_check)

with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8') as f:
    f.write(txt)
    
print("Patched! Empty animation tracks no longer block character loading.")
