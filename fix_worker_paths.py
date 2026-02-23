import glob

for f in glob.glob('assets/*worker*.js'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to force it to look in /assets/libs/
    original = 'const i=`${e.substring(0,e.lastIndexOf("/"))}/libs/`'
    content = content.replace(original, 'const i="/assets/libs/"')
    
    # Just in case other workers use different local variable names or syntax:
    # Let's also do a regex to replace the libs path logic
    import re
    # Match something like: const i=`${e.substring(0,e.lastIndexOf("/"))}/libs/`
    content = re.sub(r'const [a-zA-Z]=\`\$\{[a-zA-Z]\.substring\(0,[a-zA-Z]\.lastIndexOf\("/"\)\)\}/libs/\`', 'const i="/assets/libs/"', content)

    # Some workers might just say `... = ".../libs/"`
    content = content.replace('}/libs/`', '}/assets/libs/`')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Patched libs path in {f}")
