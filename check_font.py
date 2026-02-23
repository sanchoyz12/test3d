import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# The font binary format - let's really check what unicode chars are in it
# The format starts with "guls" - let's search for the glyph table
with open('assets/fonts/UglyDave-Alternates-optimized.font', 'rb') as f:
    data = f.read()

# Try to find unicode values systematically
# The format probably stores glyph entries as {codepoint, x, y, w, h, ...}
# Let's search for ASCII codepoints (65=A, 66=B, etc.) to find the table format
# Then we'll check if Cyrillic (1040=А, etc.) is there

# Let's search for 0x0041 (A) as 4-byte LE
letter_A = (0x0041).to_bytes(4, 'little')
positions_A = [i for i in range(len(data)-4) if data[i:i+4] == letter_A]
print(f"Codepoint 'A' (0x41) found at positions: {positions_A[:10]}")

# Check patterns around those positions
if positions_A:
    pos = positions_A[0]
    print(f"\nData around first 'A' position ({pos}):")
    print(data[max(0,pos-20):pos+40].hex())
    
# Now check for Cyrillic А (0x0410)
cyr_A = (0x0410).to_bytes(4, 'little')
positions_cyrA = [i for i in range(len(data)-4) if data[i:i+4] == cyr_A]
print(f"\nCyrillic 'А' (0x0410) found at: {positions_cyrA[:10]}")

# Check lowercase kyr а (0x0430)
cyr_a = (0x0430).to_bytes(4, 'little')
positions_cyra = [i for i in range(len(data)-4) if data[i:i+4] == cyr_a]
print(f"Cyrillic 'а' (0x0430) found at: {positions_cyra[:10]}")

print(f"\nFont file size: {len(data)} bytes")
