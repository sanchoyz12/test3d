import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

replacements = [
    # === Главная кнопка ===
    ('"ENTER "', '"ВОЙТИ "'),
    ('"BEGIN"', '"НАЧАТЬ"'),
    
    # === Название игры ===
    ('"MESSENGER"', '"ДОСТАВЩИК"'),
    
    # === Квест descriptions ===
    ('"Falling off the corporate ladder"', '"Неприятности на работе"'),
    ('"Scientists and mixed-up deliveries"', '"Учёные и перепутанные посылки"'),
    ('"A man who\'s hiding from something"', '"Человек, прячущийся от чего-то"'),
    ('"An offering to the mountain temple"', '"Дар горному храму"'),
    
    # === NPC имена / названия ===
    ('"Walking Man"', '"Прохожий"'),
    ('"Unnamed NPC"', '"Незнакомец"'),
    ('"Boss"', '"Начальник"'),
    ('"Fox"', '"Лис"'),
    ('"Owl"', '"Сова"'),
    
    # === Intro texts — вступительный монолог курьера ===
    ('"Looks like I slept in... I better rush to work!"', '"Кажется, я проспал... Надо бежать на работу!"'),
    
    # === UI buttons ===
    ('"continue"', '"продолжить"'),
    ('"customize"', '"настроить"'),
]

count_total = 0
for old, new in replacements:
    count = txt.count(old)
    if count > 0:
        txt = txt.replace(old, new)
        print(f"Replaced {count}x: {old[:50]} → {new[:50]}")
        count_total += count
    else:
        print(f"NOT FOUND: {old[:50]}")

with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8') as f:
    f.write(txt)
    
print(f"\nTotal: {count_total} replacements made")
