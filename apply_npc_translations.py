import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Replace all mixed/broken mixed-language NPC dialogues with clean Russian
replacements = [
    # Office worker #1 (sent letter to boss)
    (
        '"Слава богу, ты\'re here! I sent a letter to my boss earlier, but I need to get it back before he sees it..."',
        '"Слава богу, ты здесь! Я отправил письмо начальнику, но нужно вернуть его, пока он не прочитал..."'
    ),
    (
        '"Он живёт в доме на Светлогорском обрыве. Как думаешь, он\'s read it yet?"',
        '"Он живёт в доме на Светлогорском обрыве. Как думаешь, он уже прочитал?"'
    ),
    # Boss reaction
    (
        '"One of my employees wrote this? I can\'не верится... это... же..."',
        '"Один из сотрудников написал это? Не может быть... это... просто..."'
    ),
    (
        '"...hilarious. Wow, he\'s really roasting me. Maybe he\'s manager material after all..."',
        '"...восхитительно. Он реально меня жжёт. Может, из него выйдет хороший руководитель..."'
    ),
    # Postcard quest
    (
        '"Hey there! Can you please take this postcard to my wife? She sells flowers in the main square."',
        '"Привет! Не мог бы ты отнести эту открытку моей жене? Она продаёт цветы на рыбном рынке."'
    ),
    (
        '"I\'d give it to her myself but I... uh... have a bad knee at the moment..."',
        '"Я бы сам отнёс, но... эм... колено подводит в последнее время..."'
    ),
    (
        '"Oh, a postcard from my husband!"',
        '"О, открытка от мужа!"'
    ),
    (
        '"Слушай, между нами, я знаю, что он\'s living in a cave in the forest... I hope his midlife crisis passes soon..."',
        '"Слушай, между нами, он живёт в пещере в Куршской косе... Надеюсь, кризис среднего возраста скоро пройдёт..."'
    ),
    (
        '"Не мог бы ты отнести ему чистую одежду? Не\'t say they\'от меня. Просто скажи, что он выиграл кило янтаря."',
        '"Не мог бы ты отнести ему чистые вещи? Не говори, что от меня. Скажи, что он выиграл кило янтаря."'
    ),
    (
        '"Как раз вовремя, а то я\'m down to my last pair of underwear."',
        '"Как раз вовремя, а у меня уже последнее исподнее осталось."'
    ),
    # Scientists quest
    (
        '"Hey, can you help me with something? We\'у нас нехватка кадров, и, ну, пара посылок ушла в Польшу по ошибке..."',
        '"Можешь помочь? У нас нехватка кадров, и пара посылок случайно ушла в Польшу по ошибке..."'
    ),
    (
        '"Go find Профессор Иммануил and see if he\'s received any packages lately. He lives at the base of the mountain temple."',
        '"Найди Профессора Иммануила и узнай, не приходили ли ему посылки. Он живёт у подножия горного замка."'
    ),
    (
        '"planet gravity data analysis"',
        '"анализ гравитационных данных планеты"'
    ),
    (
        '"They probably mixed me up with Доктор Фреби (или Кант?) at Дом Советов.."',
        '"Меня, наверное, перепутали с Доктором Фреби (или Кантом?) из Дома Советов..."'
    ),
    (
        '"...wait, does that mean MY ORDER went to Dr Frebi? Oh no!!!"',
        '"...подождите, это значит МОЙ ЗАКАЗ отправили Доктору Фреби? О нет!!!"'
    ),
    (
        '"Я... ээ... всё равно не то заказал... Скажи ей, что я не\'t need it anymore..."',
        '"Я... эм... всё равно всё перепутал... Скажи ей, что мне это больше не нужно..."'
    ),
    (
        '"Oh hey, you work for the delivery company? I\'я собирался с вами поговорить..."',
        '"О, ты из службы доставки? Как раз хотел поговорить с кем-нибудь из вас..."'
    ),
    (
        '"You don\'t know anything about that? Oh well. Thanks for the package."',
        '"Не знаешь ничего об этом? Ну ладно. Спасибо за посылку."'
    ),
    # Temple quest
    (
        '"Excuse me, could you please take this offering up to the mountain temple for me?"',
        '"Простите, не могли бы вы отнести это подношение в горный храм?"'
    ),
    (
        '"Oh, pastries and sake?"',
        '"О, пирожки и саке?"'
    ),
    # Dave letter
    (
        '"В одном из них было письмо. Оно\'s a bit wet, but I can make out the name Dave at the top."',
        '"В одном из них было письмо. Немного намокло, но я разобрал имя Дэйв наверху."'
    ),
    (
        '"Dear Future Dave..."',
        '"Дорогой Будущий Дэйв..."'
    ),
    (
        '"Get plenty of sunshine..."',
        '"Побольше солнца..."'
    ),
    (
        '"Well..."',
        '"Ну..."'
    ),
    (
        '"...two out of three ain\'t bad."',
        '"...двое из трёх — неплохой результат."'
    ),
    # Other NPCs
    (
        '"hello there"',
        '"привет"'
    ),
    (
        '"Извини, я\'m on my lunch break."',
        '"Извини, я на обеде."'
    ),
    (
        '"Звучит неплохо, скажи же\'t you think?"',
        '"Звучит неплохо, правда же?"'
    ),
    (
        '"Have you seen my daughter? I thought she\'d be home by now..."',
        '"Не видел мою дочь? Думала, она уже дома..."'
    ),
    # Scientist NPC
    (
        '"Hello."',
        '"Здравствуйте."'
    ),
    (
        '"Have you heard of a thing called three.js?"',
        '"Слышали о такой вещи, как three.js?"'
    ),
    (
        '"Ну... Полагаю, большинство людей не\'t know about 3D experiences."',
        '"Ну... большинство людей не знает о 3D-опыте."'
    ),
    (
        '"They\'re an art form that combines creativity and technology."',
        '"Это вид искусства, объединяющий творчество и технологии."'
    ),
    (
        '"It\'s like painting, but with code!"',
        '"Это как рисование, только кодом!"'
    ),
    # Misc
    (
        '"I think I\'ve seen you somewhere before..."',
        '"Кажется, я где-то тебя видел..."'
    ),
    (
        '"Let\'посмотрим... Сначала я\'ll need to calculate the radius of the bike tire..."',
        '"Посмотрим... Сначала мне нужно вычислить радиус велосипедного колеса..."'
    ),
    (
        '"Come on... open up..."',
        '"Ну же... открывайся..."'
    ),
    (
        '"Do you hear that sound? Silence..."',
        '"Слышишь этот звук? Тишина..."'
    ),
    (
        '"I mean, there\'s the wind chimes too, but it\'s mostly silence..."',
        '"Ну, ещё колокольчики на ветру, но в основном тишина..."'
    ),
]

count = 0
for old, new in replacements:
    c = txt.count(old)
    if c > 0:
        txt = txt.replace(old, new)
        print(f"✓ ({c}x): {old[:50]}")
        count += c
    else:
        print(f"✗ NOT FOUND: {old[:50]}")

with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8') as f:
    f.write(txt)

print(f"\nTotal: {count} replacements applied")
