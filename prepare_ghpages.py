import os, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ==============================
# 1. Fix index.html absolute paths
# ==============================
html = open('index.html', encoding='utf-8').read()

# Change /assets/ → ./assets/ for all src/href
html = html.replace('src="/assets/', 'src="./assets/')
html = html.replace('href="/assets/', 'href="./assets/')
html = html.replace('content="/assets/', 'content="./assets/')

open('index.html', 'w', encoding='utf-8').write(html)
print("✓ index.html paths fixed (relative)")

# ==============================
# 2. Fix absolutePath in App3D JS  
# ==============================
# Currently: Ke(this,"absolutePath",window.location.origin)
# Need: Ke(this,"absolutePath", window.location.href.replace(/\/[^\/]*$/, ''))
# This will correctly work both on localhost AND on github.io/reponame/

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='surrogateescape').read()

old = 'Ke(this,"absolutePath",window.location.origin)'
new = 'Ke(this,"absolutePath",window.location.href.replace(/\\/[^\\/]*$/,""))'

count = txt.count(old)
if count:
    txt = txt.replace(old, new)
    print(f"✓ absolutePath patched ({count}x) to use full pathname")
else:
    # Try alternative form
    old2 = '"absolutePath",window.location.origin'
    new2 = '"absolutePath",window.location.href.replace(/\\/[^\\/]*$/,"")'
    count2 = txt.count(old2)
    if count2:
        txt = txt.replace(old2, new2)
        print(f"✓ absolutePath patched (alt form, {count2}x)")
    else:
        print("✗ absolutePath NOT FOUND - searching...")
        idx = txt.find('absolutePath')
        print(txt[idx-50:idx+100])

open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8', errors='surrogateescape').write(txt)

# ==============================
# 3. Create .nojekyll (required by GitHub Pages)
# ==============================
open('.nojekyll', 'w').write('')
print("✓ .nojekyll created")

# ==============================
# 4. Print stats
# ==============================
import glob
total = 0
for f in glob.glob('**/*', recursive=True):
    if os.path.isfile(f) and not f.startswith('.git'):
        total += os.path.getsize(f)

print(f"\nTotal project size: {total / 1024 / 1024:.1f} MB (GitHub Pages limit: 1000 MB)")

# Count asset files
counts = {}
for ext in ['.drc', '.ktx2', '.ogg', '.js', '.png', '.avif']:
    files = glob.glob(f'**/*{ext}', recursive=True)
    counts[ext] = len(files)
    
print("Asset counts:", counts)
