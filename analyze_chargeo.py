import re
import urllib.request

# Download and analyse the charactergeoworker - see what messages it handles
req = urllib.request.Request('https://messenger.abeto.co/assets/charactergeoworker-D8pdYVWP.js', headers={'User-Agent': 'Mozilla/5.0'})
original = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')

print("File size:", len(original))
print("First 500 chars:")
print(original[:500])

print("\nLast 500 chars:")
print(original[-500:])

print("\nAll string literals:")
matches = re.findall(r'["\']([^"\']{5,200})["\']', original)
for m in matches[:50]:
    print(" ", repr(m))
