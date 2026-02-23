import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

TRANSLIT_MAP = {
    'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'Yo',
    'Ж':'Zh','З':'Z','И':'I','Й':'Y','К':'K','Л':'L','М':'M',
    'Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U',
    'Ф':'F','Х':'Kh','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Sch',
    'Ъ':'','Ы':'Y','Ь':'','Э':'E','Ю':'Yu','Я':'Ya',
    'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
    'ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m',
    'н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u',
    'ф':'f','х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'sch',
    'ъ':'','ы':'y','ь':'','э':'e','ю':'yu','я':'ya',
}

def translit(text):
    return ''.join(TRANSLIT_MAP.get(c, c) for c in text)

# Read file as raw bytes, decode with utf-8
txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='surrogateescape').read()

# Count cyrillic before
before = sum(1 for c in txt if '\u0400' <= c <= '\u04FF')
print(f"Cyrillic before: {before}")

# Replace every Cyrillic character
result = []
for ch in txt:
    if '\u0400' <= ch <= '\u04FF':
        result.append(TRANSLIT_MAP.get(ch, ch))
    else:
        result.append(ch)

new_txt = ''.join(result)
after = sum(1 for c in new_txt if '\u0400' <= c <= '\u04FF')
print(f"Cyrillic after: {after}")

with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(new_txt)

print("Done!")
