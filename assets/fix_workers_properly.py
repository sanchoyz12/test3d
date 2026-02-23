import urllib.request
import os
import re

base_url = "https://messenger.abeto.co"
workers = [
    'assets/dracoworker-9mmlh0V-.js',
    'assets/glyphworker-DoaYwstb.js',
    'assets/geometryworker-WyEueJn9.js',
    'assets/bitmapworker-DtCLhbWB.js'
]

for w in workers:
    full_url = base_url + '/' + w
    req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
    txt = urllib.request.urlopen(req).read().decode('utf-8')
    
    # 1. Fix the libs logic
    # Find something like:  const s=`${n.substring(0,n.lastIndexOf("/"))}/libs/`
    pattern = r'(const |let |var )([a-zA-Z_0-9]+)\=\`\$\{[a-zA-Z_0-9]+\.substring\(0,[a-zA-Z_0-9]+\.lastIndexOf\("/"\)\)\}/libs/\`'
    
    def repl(match):
        decl = match.group(1)
        var_name = match.group(2)
        # We replace it with an absolute path or relative path
        # Actually it's better to just give it relative: './assets/libs/'
        # Wait, if accessed from localhost:8083/, '/assets/libs/' is correct.
        return f'{decl}{var_name}="/assets/libs/"'
        
    txt = re.sub(pattern, repl, txt)
    
    # Also another pattern: `/libs/`
    # Ensure they point to /assets/libs/
    txt = txt.replace('}/libs/`', '}/assets/libs/`')
    
    # Fix the dracoworker path being requested inside App3D
    # I already fixed it inside App3D, but just in case
    txt = txt.replace('https://messenger.abeto.co/assets', '/assets')
    txt = txt.replace('https://messenger.abeto.co', '')

    with open(w, 'w', encoding='utf-8') as f:
        f.write(txt)
        
    print(f"Redownloaded and correctly patched {w}")

