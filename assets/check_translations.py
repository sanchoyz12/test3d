import re

txt_bytes = open('assets/App3D-BLRWK1h9.js', 'rb').read() 

# The Russian strings shown as mojibake suggest CP1252 mis-decoded UTF-8
# Let's find all complete UTF-8 Cyrillic sequences in the file
cyrillic_pattern = rb'[\xd0-\xd1][\x80-\xbf]'
positions = [m.start() for m in re.finditer(cyrillic_pattern, txt_bytes)]
print(f"Found {len(positions)} Cyrillic characters at positions")

# Extract strings around first few
for pos in positions[:5]:
    # Find the enclosing string quotes
    start = max(0, pos-80)
    end = min(len(txt_bytes), pos+80)
    context = txt_bytes[start:end]
    try:
        print(context.decode('utf-8', errors='replace'))
    except:
        print(repr(context))
    print()
