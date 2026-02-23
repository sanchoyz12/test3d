import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Replace the whole introTexts array with proper Russian translation
old_intro = 'introTexts=["Looks like I slept in... I better start today\'s deliveries.","I\'у меня пятеро в списке потерь янтаря.\'re easy to find.","Alright, I better get going."]'
new_intro = 'introTexts=["Опять проспал... Ладно, пора развозить посылки по Калининграду.","Пять адресов — не так уж много. Разберёмся.","Ну, поехали. Янтарный край не ждёт."]'

count = txt.count(old_intro)
if count:
    txt = txt.replace(old_intro, new_intro)
    print(f"Replaced introTexts ({count}x)")
else:
    # Find partial match
    idx = txt.find('introTexts=[')
    print(f"introTexts found at {idx}")
    print(repr(txt[idx:idx+300]))

with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8') as f:
    f.write(txt)
