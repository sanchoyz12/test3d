import re

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Find the default animation files list in the code
# From earlier analysis:
# animationFiles:[\"avatar/avatar-idle\",\"avatar/avatar-walk\",\"avatar/avatar-run\",\"avatar/avatar-air\",\"avatar/avatar-afk\"]
# We need to remove avatar-walk and avatar-afk since they don't exist

# Pattern 1: player character animation files
old1 = '"avatar/avatar-idle","avatar/avatar-walk","avatar/avatar-run","avatar/avatar-air","avatar/avatar-afk"'
new1 = '"avatar/avatar-idle","avatar/avatar-run","avatar/avatar-air"'

# Pattern 2: NPC_FILES animation files 
old2 = '"avatar/avatar-idle","avatar/avatar-run","avatar/avatar-sprint","avatar/avatar-air","avatar/avatar-afk1","avatar/avatar-afk2","avatar/avatar-afk3"'
new2 = '"avatar/avatar-idle","avatar/avatar-run","avatar/avatar-sprint","avatar/avatar-air","avatar/avatar-afk1","avatar/avatar-afk2","avatar/avatar-afk3"'

count1 = txt.count(old1)
count2 = txt.count(old2)
print(f"Found pattern1: {count1} times")
print(f"Found pattern2: {count2} times")

txt = txt.replace(old1, new1)

# Also check what the _loadModels expects - it checks `l.some(p => p.tracks.length === 0)`
# So we need to either: remove walk/afk from the list, OR make geometryLoader.skinAnimation return 
# a placeholder animation with at least 1 track. Let's try removing them.

# Write fixed file
with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8') as f:
    f.write(txt)

print("Patched!")
print(f"Remaining occurrences of avatar-walk: {txt.count('avatar-walk')}")
print(f"Remaining occurrences of avatar-afk\": {txt.count(chr(34) + 'avatar/avatar-afk' + chr(34))}")
