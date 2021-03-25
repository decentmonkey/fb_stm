default worker7Option1Cnt = 0
default worker7Option2Cnt = 0

# китаянка
label worker7_look:
    img 20316
    with fade
    if shopVisitorStage10 >= 3:
        music Groove2_85
        mt "Лучше держаться от нее подальше."
    else:
        mt "Похоже, это какой-то стажер."
        if monicaBitch == True:
            mt "Бесполезный и никчемный..."
    return

label worker7_dialogue_workplace:
    music Groove2_85
    img 20317
    with fade
    mt "Кажется, я ее где-то видела..."
    mt "Может быть она когда-то приходила ко мне на кастинг..."
    mt "Или нет, она работала официанткой в моем любимом ресторане..."
    mt "И где я ее могла видеть?"
    img 20318
    with diss
    if shopVisitorStage10 >= 3:
        music Power_Bots_Loop
        mt "Черт! Она же была покупательницей в этом ужасном магазине, где я работала манекеном!"
        music Groove2_85
        mt "Кошмар, надеюсь она меня не узнает..."
        mt "Хотя... Не думаю что можно связать Монику Бакфетт с какой-то продавщицей в трущобах..."
        mt "В любом случае, надо поменьше общаться с ней. Вдруг она, все-же, узнает меня..."
    else:
        mt "Кажется, я ее видела в трущобах..."
        mt "Но и она меня могла видеть..."
    mt "Лучше держаться от нее подальше."
    return

label worker7_dialogue_office:
    music Sneaky_Snitch
    img 20371
    with fadelong
    w7 "Миссис Бакфетт, можно?"
    if shopVisitorStage10 >= 3:
        music Groove2_85
        img 20372
        with fade
        mt "Она может меня узнать... Лучше не говорить с ней долго."
        mt "Думаю, лучше будет ее вежливо выпроводить."
    img 20373
    with diss
    m "Кажется, тебя зовут Лин?"
    img 20374
    w
    img 20375
    with diss
    w7 "Да, мэм."
    img 20376
    with fade
    m "Лин, я сейчас очень занята. Если ты принесла отчет, положи пожалуйста его мне на стол. Я его обязательно посмотрю."
    img 20377
    with diss
    w7 "Хорошо, Мэм."
    sound snd_folder_drop
    if shopVisitorStage10 >= 3:
        img 20378
        with fade
        w7t "(Меня не покидает мысль, что где то Я видела эту миссис Бакфетт...)"
    return

label takeReportsFlashCard_Worker7:
    music Groove2_85
    img 20786
    with fade
    m "Вот флеш карта, скопируй сюда сделанные тобою отчеты."
    img 20787
    with diss
    if shopVisitorStage10 >= 3:
        mt "Хоть бы она меня не узнала... Она могла видеть меня в трущобах..."
    w7 "Хорошо."
    if shopVisitorStage10 >= 3:
        w7t "Меня не покидает чувство, что я где-то видела Миссис Бакфетт. И определенно не здесь."
        # берет флешку cадится
        img 20788
        with diss
        w7t "Может быть в каком-то журнале..."
        w7t "Возможно..."
        w7t "Хотя нет!"
        img 20789
        with diss
        m "Эй! О чем задумалась? Я жду твои отчеты!"
        w7 "Да, мэм, копируется..."
        w7t "Черт, сбила с мысли..."
    img 20790
    with fadelong
    w7 "Готово."
    m "Хорошо, продолжай работу."
    return
