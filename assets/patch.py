import re
import os

replacements = {
    "It's a small planet, but someone's gotta make the deliveries.": "Небольшая область, но посылки-то кому-то нужно доставлять.",
    "Messenger": "Доставщик КЛД",
    "A letter for me? From under the sea? The one who wrote it... is me!": "Письмо мне? Со дна Балтийского моря? Я же сам его и написал!",
    "A note lost at sea": "Записка, затерянная в море",
    "CONGRATULATIONS! ANOTHER SUCCESSFUL DELIVERY COMPLETED": "ПОЗДРАВЛЯЕМ! ЕЩЁ ОДНА УСПЕШНАЯ ДОСТАВКА В КАЛИНИНГРАДЕ!",
    "Can you take this note back to him? He works in the main square.": "Можешь вернуть ему эту записку? Он работает на Острове Канта.",
    "Capital Corp.": "Дом Советов",
    "Captain Steve": "Капитан Степан",
    "Cave Man": "Янтарщик",
    "Dave the Musician": "Денис Лабух",
    "Doctor Frebi": "Доктор Фреби (или Кант?)",
    "Doctor Frieb": "Профессор Иммануил",
    "Factory Worker": "Рабочий вагонозавода",
    "Flower Lady": "Цветочница",
    "Go find Doctor Frieb and see if he": "Найди профессора Иммануила и узнай, сможет ли он",
    "GO BACK TO THE MAN IN THE CAVE AND DELIVER THE CLOTHES": "ВЕРНИСЬ К ЯНТАРЩИКУ В ПЕЩЕРУ И ОТДАЙ ЕМУ ОДЕЖДУ",
    "Hacker Girl": "Студентка БФУ",
    "He lives at the red cliff house. Do you think he": "Он живёт в доме на Светлогорском обрыве. Как думаешь, он",
    "I am talking to you right now.": "Я прямо сейчас с тобой говорю, братан.",
    "I have trouble making it up the slope by myself these days.": "Мне уже тяжело подниматься на дюну самому.",
    "I think I hear my dad calling...": "Кажется, батя зовёт...",
    "I... uh... ordered the wrong thing anyway... Tell her I don": "Я... ээ... всё равно не то заказал... Скажи ей, что я не",
    "It has a nice ring to it, don": "Звучит неплохо, скажи же",
    "Just in time, too. I": "Как раз вовремя, а то я",
    "Keep practicing every day...": "Тренируйся каждый день...",
    "Look, between you and me, I know he": "Слушай, между нами, я знаю, что он",
    "Lucero Graveyard": "Кладбище старых кораблей",
    "Main Square": "Остров Канта",
    "Maybe I should just call in sick...": "Может, просто взять больничный...",
    "Mountain Guy": "Парень с Куршской",
    "Mountain Temple": "Руины замка Бальга",
    "My favourite.": "Моя любимая строганина.",
    "Office Worker": "Офисный клерк из Кловера",
    "Oh my...": "Ё-моё...",
    "Old Woman": "Бабуля",
    "One of them had a letter inside. It": "В одном из них было письмо. Оно",
    "Pale Man": "Турист из Москвы",
    "Pretty crazy huh? I know a guy called Dave. Do you think it could be the same one?": "Безумие, да? Я знаю одного Дениса. Думаешь, это он?",
    "Red Cliff House": "Домик рыбака",
    "Senior associate executive chief vice director...": "Старший помощник младшего заместителя по янтарю...",
    "Shipments in... shipments out...": "Грузы приходят... санкционка уходит...",
    "Shop Keeper": "Владелец сувенирной лавки",
    "Smelly Falls": "Преголя",
    "Sorry, I": "Извини, я",
    "TAKE THE BOSS": "ОТВЕЗИ МЕНЕДЖЕРУ В ДОМ СОВЕТОВ",
    "TAKE THE CAVE MAN": "ОТВЕЗИ ЯНТАРЩИКУ НА КОСУ",
    "TAKE THE CLEAN CLOTHES TO THE MAN IN THE CAVE": "ОТНЕСИ ЧИСТУЮ ОДЕЖДУ ЯНТАРЩИКУ В ПЕЩЕРЕ",
    "TAKE THE MYSTERY LETTER TO DAVE AT SMELLY FALLS": "ОТНЕСИ ТАЙНОЕ ПИСЬМО ДЕНИСУ НА ПРЕГОЛЮ",
    "TAKE THE OLD WOMAN": "ОТВЕЗИ БАБУШКЕ В ЗЕЛЕНОГРАДСК",
    "Take care of your hair. Let it grow wild and free. Your hair is your soul and the most defining feature of your personality.": "Береги волосы, пусть растут как дюны на Куршской косе.",
    "Thank god you": "Слава богу, ты",
    "Thank you for delivering my offering.": "Спасибо за доставку подношения Хомлинам.",
    "The Forest": "Танцующий лес",
    "The new guy is late again.": "Новенький опять опоздал из-за пробки на двухъярусном.",
    "They probably mixed me up with Doctor Frebi at Capital Corp...": "Наверное, меня перепутали с профессором в Доме Советов...",
    "Tulips can take a while to bloom.": "На побережье цветы распускаются долго.",
    "Well... I suppose most people don": "Ну... Полагаю, большинство людей не",
    "Would you mind bringing him these clean clothes? Don": "Не мог бы ты отнести ему чистую одежду? Не",
    "Wow, another prize?": "Ого, ещё один кусок янтаря?",
    "Wow, who would have known that acting on my lowest instincts would help me advance in the corporate world.": "Ого, кто бы мог подумать, что торговля контрабандой так помогает в жизни.",
    "Young Kid": "Шпана с Балтрайона",
    "Check this out! I was diving for oysters earlier and found these old lock boxes buried in the sand.": "Смотри! Я нырял за янтарем у Светлогорска и нашел эти контейнеры в песке.",
    "Do you know why I received 63 packets of instant noodles? Was that meant to go to the grocery store or something?": "Знаешь, почему я получил 63 упаковки шпрот? Это что, в Викторию должно было идти?",
    "ll need to build here... here... and also here...": "ут надо построить торговый центр... и здесь тоже...",
    "m getting... promoted?": "Меня... повышают?",
    "re from me. Just tell him he won a prize.": "от меня. Просто скажи, что он выиграл кило янтаря.",
    "re short on staff lately and, well, some of our mail went to the wrong address by mistake...": "у нас нехватка кадров, и, ну, пара посылок ушла в Польшу по ошибке...",
    "s on an overseas business trip at the moment, visiting all kinds of exotic places!": "сейчас закупается санкционкой в Польше!",
    "s probably down at smelly falls, if you want to take it to him.": "наверное, у Преголи, если хочешь отнести ему.",
    "s see... First I": "посмотрим... Сначала я",
    "s see what I wrote to myself all those years ago...": "посмотрим, что я себе написал тогда...",
    "t believe it... this... is...": "не верится... это... же...",
    "ve been meaning to talk to you guys...": "я собирался с вами поговорить...",
    "ve got five on the list. Hopefully they": "у меня пятеро в списке потерь янтаря.",
}

files_to_patch = ['index.html', 'assets/webgl-C4v7tvuW.js', 'assets/runtime-C2kxzoFi.js', 'assets/App3D-BLRWK1h9.js']

for file_path in files_to_patch:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        for en, ru in replacements.items():
            content = content.replace(en, ru)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file_path}")
