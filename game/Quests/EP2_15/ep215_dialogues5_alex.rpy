default melanieAlexVictoriaSex1 = False  # Мелани делала ликинг Виктории на глазах у Алекса
default melanieAlexVictoriaSex2 = False  # Мелани дала согласие на то, чтобы Алекс переспал с Викторией
default melanieAlexVictoriaSex3 = False  # Мелани и Моника украли телефон Виктории из гримерки и поехали к Дику

#call ep215_dialogues5_alex_1() # холл возле лифта в офисе, разговор Виктории и Алекса
#call ep215_dialogues5_alex_2() # апартаменты Мелани, приходит Виктория
#call ep215_dialogues5_alex_3() # апартаменты Мелани, приходит Алекс
#call ep215_dialogues5_alex_4() # фотостудия, Моника видит Викторию на фотосессии
#call ep215_dialogues5_alex_5() # гримерка, разговор с Мелани
#call ep215_dialogues5_alex_6() # разговор с Диком в его кабинете
#call ep215_dialogues5_alex_7() # приемная Дика, разговор с Викторией
#call ep215_dialogues5_alex_8() # гримерка в офисе Моники, разговор с Мелани



# при условии, что Алекс уже живет у Мелани
label ep215_dialogues5_alex_1:
    # Виктория снова пришла к Алексу на работу и стоит с ним в холле возле лифтов
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_64
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 19369
    victoria "Алекс, мне моя подружка Мелани сказала, что вы теперь живете вместе!"
    victoria "Я так рада за вас!"
    alex_photograph "Да, Виктория."
    alex_photograph "Я тогда был неправ. Ты действительно рассказала мне правду про Мелани."
    #
    $ notif(_("Виктория говорила Алексу, что у Мелани к нему чувства."))
    #
    # Виктория заискиваще
    imgf 19370
    victoria "Так приятно сознавать, что я способствовала развитию ваших отношений, Алекс!"
    victoria "Мелани хорошая подружка и достойна такого талантливого фотографа как ты!"
    victoria "Я думаю, что теперь ничего не мешает тебе помочь мне..."
    victoria "В продвижении моего аккаунта?"
    # Алекс хмурит брови
    imgd 19371
    alex_photograph "Мне надо подумать, Виктория..."
    # Виктория воодушевленно
    imgf 19372
    victoria "Алекс, я тут подумала, что было бы идеально сделать фотосессию!"
    victoria "Я разместила бы твои работы в своем аккаунте с пометкой на тебя!"
    imgd 19373
    victoria "Тебе нужно будет только сделать несколько кадров со мной и все!"
    victoria "Остальное я сделаю сама!"
    victoria "Ну и поставишь на меня ссылку в своем аккаунте, что я новая модель."
    # Алекс в сомнении
    imgf 17639
    alex_photograph "Это не мой уровень и не мой стиль работы, Виктория..."
    alex_photograph "Я работаю только с топ-моделями."
    # Виктория не отстает от него
    imgd 17634
    victoria "А в каком случае ты бы согласился сделать такую работу, Алекс?"
    # Алекс чешет затылок задумчиво
    imgf 19374
    alex_photograph "Нуу... Не знаю... Я не привык нарушать свои правила..."
    victoria "Ну Алекс..."
    victoria "Но ведь должно быть что-то... Или кто-то..."
    victoria "Ради кого ты мог бы сделать исключение?"
    imgd 19375
    alex_photograph "Нууу... Наверное, ради девушки..."
    victoria "Алекс, а хочешь я буду твоей девушкой?!"
    music stop
    sound plastinka1b
    # он смотрит на нее как на ненормальную
    img 19376 vpunch
    alex_photograph "Но ведь... У меня уже есть Мелани... Твоя подруга."
    # Виктория начинает юлить, флиртовать с ним, строить глазки
    # возможно протягивает руку, чтобы притронуться к его руке или волосам
#    stop music fadeout 1.0
#    music Loved_up
    music Hidden_Agenda
    imgd 19377
    victoria "Алекс... Да ладно тебе!"
    victoria "Мы так давно с тобой знаем друг друга..."
    victoria "И я всегда тебя считала довольно привлекательным мужчиной."
    imgf 19378
    victoria "Если ты очень хочешь, я могла бы провести с тобой вечер."
    victoria "Например, сегодня..."
    victoria "Как ты на это смотришь, Алекс?"
    # Алекс отстраняется от нее
#    music stop
#    sound plastinka1b
    music Groove2_85
    imgd 19379
    alex_photograph "Нет-нет, Виктория!"
    alex_photograph "Меня это не интересует!"
    imgd 19380
    alex_photograph "Извини, мне нужно идти!"
    # затемнение, звук лифта
    fadeblack
    sound snd_lift
    pause 2.0
    music Master_Disorder
    # Алекс уходит (звук лифта)
    # Виктория стоит в холле одна и злым взглядом смотрит на лифт
    imgfl 17642
    victoria "Хммм..."
    victoria "Вот так, значит?"
    # затемнение

#    fadeblack 1.5
#    music Power_Bots_Loop
    mt "Надо быстрее убираться отсюда!!"
    return

# вечером того же дня
# апартаменты Мелани
label ep215_dialogues5_alex_2:
    # затемнение, звук - стук в дверь, каблуки, звук открытия двери
    # показываем апартамениы Мелани
    # она стоит у дверей своих апартаментов, смотрит как на врага народа на только что вошедшую Викторию
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_65
#    call textonblack(t_("Некоторое время спустя..."))
    scene black_screen
    with Dissolve(1)
    sound snd_door_knock
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.5
#    sound Jump1
    music Groove2_85
    imgfl 19381
    victoria "Подружка Мелани, привет."
    melanie "..."
    imgf 19382
    victoria "Я соскучилась по тебе и решила навестить тебя."
    victoria "Я знаю, что ты рада моему визиту."
    victoria "Поэтому хочешь поцеловать меня в щечку, подружка."
    victoria "Я совсем не против и разрешаю тебе сделать это."
    # Мелани смотрит на нее с отвращением
    imgd 19383
    melanie "..."
    # Виктория показывает пальцем на свою щеку
    imgd 19384
    victoria "Подружка Мелани, я жду."
    victoria "Или ты мне не рада?" # угрожающе
    menu:
        "Поцеловать Викторию.":
            pass
    imgf 19385
    melanie "Конечно, я тебе рада... Подружка..." # с каменным лицом
    fadeblack
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    imgfl 19386
    w
    sound snd_kiss2
    imgf 19387
    # чмокает Викторию в щечку
    w
    sound snd_woman_laugh3
    imgd 19388
    victoria "Вот. Совсем другое дело, подружка." # хихикает довольно
    # Виктория проходит и садится на диван, Мелани сдится напротив нее на стул
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    # Виктория поднимает голову и смотрит на портрет Мелани на стене, который разрисован помадой
    # довольно ухмыляется
    # потом смотрит на Мелани
    imgfl 19389
    sound highheels_short_walk
    w
    imgf 19390
    victoria "Подружка, а где твой Алекс?"
    # Мелани сквозь зубы
    imgd 18841
    melanie "Скоро должен прийти..."
    imgf 19391
    victoria "Надеюсь, у подружки с Алексом все хорошо?"
    music Power_Bots_Loop
    imgd 18843
    melanie "..."
    music Groove2_85
    imgd 19392
    victoria "В прошлый раз получилось отличное видео, подружка."
    victoria "Оно мне настолько понравилось, что я его решила сохранить у себя..."
    # Мелани в шоке смотрит на нее
    music stop
    sound plastinka1b
    img 19393 hpunch
    melanie "Что?!"
    melanie "?!?!!"
    music Groove2_85
    imgf 19394
    victoria "Да."
    victoria "И еще. Хорошая подружка подвинет камеру немного правее..."
    victoria "Чтобы мне было лучше все видно."
    victoria "Ваши утренние забавы, которые устраивает Алекс, весьма интересны для меня."
    music Power_Bots_Loop
    imgd 19395
    melanie "..."
    music Groove2_85
    imgf 19396
    victoria "Ты сегодня не очень разговорчива, подружка Мелани..."
    victoria "Впрочем, как всегда."
    victoria "Скажи мне, тебе нравится моя попа?"
#    music Pyro_Flow
    imgd 19397
    melanie "К чему этот вопрос?"
    imgf 17361
    victoria "Я хочу услышать это. Хорошей подружке Мелани нравится моя попа?"
    menu:
        "Да, нравится.":
            pass
    imgd 19398
    melanie "Да..."
    victoria "Что 'да'? Скажи мне это, подружка."
    melanie "Мне нравится... твоя... попа..."
    # Виктория довольно хихикает
    sound snd_woman_laugh3
    imgf 17359
    w
    imgd 19399
    victoria "Да, и кстати..."
    victoria "Я тут подумала..."
    victoria "Мы ведь с тобой подружки, а подруги должны делиться всем друг с другом."
    imgf 19400
    victoria "Я понимаю, что ты уже почти невеста Алекса..."
    victoria "И у вас большие планы на будущее."
    music stop
    sound plastinka1b
    img 19401 hpunch
    melanie "!!!"
    music Groove2_85
    imgf 19402
    victoria "Но я думаю, что ты будешь не против, если я займусь с твоим будущим мужем сексом."
    victoria "Ведь ты хорошая подружка..."
    # Мелани в недоумении
#    music Groove2_85
    imgd 19403
    melanie "Что ты имеешь ввиду?"
    # Виктория хихикает
    sound snd_woman_laugh3
    imgf 19404
    victoria "Подружка, я знаю, что ты хочешь отблагодарить меня за то..."
    victoria "Что я поспособствовала воссоединению вашей счастливой пары."
    imgd 19405
    victoria "И я помогу тебе решить вопрос, каким образом ты меня можешь отблагодарить."
    melanie "Каким?"
    victoria "Алекс."
    melanie "Что Алекс?"
    victoria "Подружка Мелани хочет отблагодарить меня тем, что поделится со мной своим Алексом."
    # у Мелани шок, непонимание
    music Pyro_Flow
    img 19406 vpunch
    melanie "?!"
    melanie "?!?!"
    melanie "!!?!?!?!"
    # Виктория ехидно на нее смотрит
    # берет ее за подбородок
    music Groove2_85
    imgf 19407
    victoria "Ты же вроде всегда была неглупой, подружка Мелани..."
    victoria "Вот что любовь делает с некоторыми из нас."
    victoria "Ладно, так уж и быть... Я подскажу тебе, что надо сделать."
    victoria "Просто скажешь Алексу в нужный момент, что ты не против разнообразить ваши отношения."
    imgd 19408
    victoria "И разрешаешь ему интим со своей подружкой, то есть со мной."
    victoria "Думаю, что ты с этим справишься."
    victoria "Ради нашей дружбы."
    victoria "Ты же хорошая подружка?"
    # Мелани с недоумением
    imgf 19409
    melanie "Да... Я хорошая подружка..."
    # затемнение
    return

# апартаменты Мелани
# приходит Алекс
label ep215_dialogues5_alex_3:
    # надпись "некоторое время спустя", звук шагов, открывается дверь
    # в гостиную, где сидят Виктория и Мелани, заходит Алекс
    # он видит Викторию, удивленно смотрит на нее
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_66
    scene black_screen
    with Dissolve(1)
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.5
    music Groove2_85
    img 19495 vpunch
    w
    imgfl 19496
    victoria "Привет, Алекс!"
    sound man_steps
    imgf 19497
    alex_photograph "Привет."
    # подходит к Мелани, наклоняется к ней и целует ее в щечку
    imgd 19498
    alex_photograph "Милая, привет. Я соскучился по тебе."
    # Мелани ему равнодушно
    sound kiss1
    imgd 19499
    melanie "Привет, Алекс."
    # Виктория игриво ему улыбается
    music Hidden_Agenda
    imgf 19500
    victoria "Алекс, я пришла поболтать со своей подружкой..."
    victoria "И мы вместе кое-что придумали..."
    # Виктория зовет Алекса сесть рядом с собой
    imgd 19501
    victoria "Идем сюда, Алекс."
    victoria "Я тебе все расскажу."
    # он садится рядом с ней на диван
    # Виктория кладет руку на его бедро и игриво улыбается ему
    # он в недоумении смотрит на ее манипуляции, потом вопросительно на Мелани
    fadeblack 1.5
    music Groove2_85
    imgf 19502
    w
    sound Jump1
    imgd 19503
    w
    sound Jump2
    img 19504 hpunch
    alex_photograph "Милая, что происходит?"
    # Мелани равнодушна
    music Groove2_85
    imgd 19505
    melanie "..."
    imgf 19507
    victoria "Тсс... Все хорошо, Алекс."
    victoria "Я договорилась со своей подружкой Мелани и она не против."
    # Алекс в шоке, снова смотрит на Мелани
    # Виктория тем временем кладет ладонь на пах и гладит его
    music Hidden_Agenda
    imgd 19508
    sound Jump2
    victoria "Неужели я тебе совсем не нравлюсь?"
    victoria "Моя фигура? Моя попа?"
    # Виктория - неужели тебе не нравится моя попа?
    imgf 19509
    w
    imgd 19510
    alex_photograph "Мне нравится фигура и попа Мелани. И только Мелани."
    imgd 19511
    victoria "А Мелани нравится моя попа. Да, подружка?"
    menu:
        "Да, нравится.":
            pass
    # Мелани равнодушно подтверждает
    music Groove2_85
    imgf 19512
    melanie "..."
    melanie "Да..."
    melanie "Нравится..."
    # Алекс в шоке, не верит
    imgd 19513
    alex_photograph "Милая, это шутка?"
    melanie "..."
    alex_photograph "Да ну! Не может этого быть!"
    alex_photograph "Вы решили разыграть меня?!"
    # Виктория смотрит на Мелани
    imgf 19514
    victoria "Подружка, давай покажем Алексу, как тебе нравится моя попа."
    imgd 18845
    melanie "В смысле?"
    # Виктория пристально смотрит на Мелани, Алекс в шоке, как и Мелани
#    victoria "Чего ты медлишь, подружка?"
    sound Jump1
    imgf 19532
    victoria "Ты мне об этом говорила буквально перед приходом Алекса."
    imgd 19533
    victoria "А теперь докажи, что это так и есть на самом деле."
    victoria "Что это была не шутка."
    # Виктория встает с дивана, сначала подходит к патефону и включает его
    # потом подходит к стулу, снимает платье,
    # ставит колено на стул, как будто Мелани там нет
    music Power_Bots_Loop
    img 19534 vpunch
    melanie "!!!"
    melanie "!!!!!!"
    imgf 19535
    w
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound metal_slide
    imgd 19536
    w
    sound gramophone
    imgf 19537
    w
    music Loved_up
    # music In_Your_Arms
    imgd 19538
    w
    sound highheels_short_walk
    imgf 19539
    w
    sound snd_fabric1
    imgd 19540
    w
    sound Jump1
    imgf 19541
    w
    sound Jump2
    img 19542 vpunch
    w
    # Мелани вынуждена встать
    # Мелани пристально смотрит на Викторию, потом встает со стула и подходит к ней
    # Виктория самодовольно улыбаясь смотрит на Мелани
    # Виктория встает в позу, в которой будет секс.
    imgf 19543
    victoria "Ну же. Давай, подружка."
    victoria "Уверена, Алексу понравится смотреть на это."
    menu:
        "Сделать так, как говорит Виктория.":
            $ melanieAlexVictoriaSex1 = True # Мелани делала ликинг Виктории на глазах у Алекса
            pass
    # Мелани равнодушно смотрит на Алекса, тот офигевает от происходящего
    imgd 19544
    alex_photograph "Мелани, милая..."
    # Мелани молча переводит взгляд на Викторию, опускается на колени
    # лижет киску, Алекс смотрит удивленно
    fadeblack 1.5
    sound highheels_short_walk
    pause 1.5
    music Master_Disorder
    imgfl 19545
    w
    victoria "Ну же, подружка..."
    victoria "Я жду..."
    imgf 19788
    w
    music stop
    sound hlup25
    music2 Loved_Up2
    img 19546 vpunch
    victoria "Мммм..."
    victoria "Да..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Licking1_1 = Movie(play="video/v_Victoria_Melanie_Licking1_1.mkv", fps=30)
    show videov_Victoria_Melanie_Licking1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19547
    victoria "О, как подружка хорошо работает своим язычком..."


    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Licking1_2 = Movie(play="video/v_Victoria_Melanie_Licking1_2.mkv", fps=30)
    show videov_Victoria_Melanie_Licking1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound lick3
    imgd 19548
    w
    sound lick3
    imgd 19549
    w
    sound lick3
    imgd 19548
    w
    sound lick3
    imgd 19549
    w
    sound lick3
    imgd 19548
    w
    sound lick3
    imgd 19549
    w
    imgf 19550
    victoria "Сразу видно, что ей нравится моя киска..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Licking1_3 = Movie(play="video/v_Victoria_Melanie_Licking1_3.mkv", fps=30)
    show videov_Victoria_Melanie_Licking1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19551
    victoria "Как же подружке нравится лизать мою киску..."
    victoria "Если подружка будет хорошей, возможно я разрешу ей лизать и мою попу тоже..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Licking1_4 = Movie(play="video/v_Victoria_Melanie_Licking1_4.mkv", fps=30)
    show videov_Victoria_Melanie_Licking1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Алекс смотрит и начинает возбуждаться
    imgf 19552
    alex_photograph "Мелани?"
    alex_photograph "Неужели это и правда тебе нравится?"
    # Мелани его игнорит и продолжает лизать
    imgd 19553
    victoria "Конечно, нравится, Алекс."
    victoria "Смотри, с каким удовольствием она лижет мою киску."
    music2 stop
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_up2
    imgfl 19554
    victoria "Как она старается... Мммм..."
    victoria "Моя киска ей очень нравится, Алекс."
    victoria "А у Мелани очень хороший вкус..."
    # Виктория обращается к Мелани
    imgf 19555
    victoria "Подружка Мелани, скажи Алексу, тебе ведь нравится?"
    # Мелани отстраняется, остается сидеть на коленях, перед лицом киска Виктории
    music Groove2_85
    imgd 19556
    melanie "Да..."
    imgd 19557
    alex_photograph "Обалдеть!"
    victoria "Подружка, скажи Алексу, ведь ты не против, чтобы я переспала с ним?"
    victoria "Ведь ты не будешь ревновать?"
    menu:
        "Я не против.":
            $ melanieAlexVictoriaSex2 = True # Мелани дала согласие на то, чтобы Алекс переспал с Викторией
            pass
    # Мелани равнодушно
    imgf 19558
    melanie "Алекс, я не против..."
    melanie "И я не буду ревновать тебя."
    # Алекс сомневается
    fadeblack 1.5
    music Groove2_85
    imgfl 19559
    alex_photograph "Правда не будешь ревновать, милая?"
    imgf 19560
    victoria "Не будет, ведь ей это нравится."
    victoria "Алекс, она даже оближет твой член после секса со мной." # ехидно
    music Power_Bots_Loop
    img 19561 vpunch
    melanie "!!!" # зло
    melanie "!!!!!!"

    music Groove2_85
    imgf 19562
    alex_photograph "Мелани, но я не хочу Викторию! Я хочу тебя!"
    # Виктория злится
    victoria "Алекс, подружка Мелани просит тебя попробовать мою попу!"
    victoria "Правда подружка?"
    imgd 19563
    melanie "!!!"
    melanie "Да, Алекс..."
    melanie "Я прошу тебя попробовать..."
    melanie "Попу моей подружки..."

    # Алекс возбужден и не замечает всех этих взглядов
    imgd 19564
    alex_photograph "Ну раз ты просишь, Мелани..."
    alex_photograph "И раз тебе это нравится..."
    alex_photograph "Я сделаю это для тебя, милая."
    imgf 19565
    alex_photograph "Даже несмотря на то, что мне твоя подруга не нравится."
    alex_photograph "Тем более меня так возбудило, как ты работала сейчас своим язычком..."
    alex_photograph "Ты так эротично это делала, Мелани!"
    imgd 19566
    victoria "Подружка, я хочу, чтобы ты сняла это на мой телефон."
    melanie "???"
    # дает Мелани свой телефон
    # Мелани удивленно берет телефон Виктории в руки, включает камеру и начинает снимать
    # Виктория опирается на кресло, ставит на него одну ногу (https://cdn.discordapp.com/attachments/625678994083414052/738837280223002624/unknown.png)
    # Алекс пристраивается сзади нее, Виктория нарочито преувеличенно изображает страсть, стонет
    # Алекс часто смотрит на Мелани
    # он не торопится входить в Викторию
    imgf 19567
    alex_photograph "Мелани, милая..."
    alex_photograph "Ты точно не против?"
    imgd 19568
    victoria "Мммм... Давай быстрее, Алекс!"
    victoria "Мне не терпится почувствовать внутри себя член такого знаменитого фотографа!"
    alex_photograph "Милая, скажи мне..."
    imgf 19569
    melanie "..."
    melanie "Алекс, я не против..." # равнодушно
    music stop
    pause 1.0
    music2 Loved_Up
    imgd 19570
    alex_photograph "Я делаю это только ради тебя, Мелани..."
    sound chpok3
    img 19571 vpunch
    w
    # вводит в Викторию член
    imgf 19572
    sound ahhh1
    victoria "Ооооо!!!"
    victoria "Да, Алекс!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Alex_Sex1_1 = Movie(play="video/v_Victoria_Alex_Sex1_1.mkv", fps=30)
    show videov_Victoria_Alex_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19573
    victoria "Возьми меня!"
    imgf 19574
    alex_photograph "Мммм..."
    alex_photograph "Ох..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Alex_Sex1_2 = Movie(play="video/v_Victoria_Alex_Sex1_2.mkv", fps=30)
    show videov_Victoria_Alex_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19575
    victoria "О, как же хорошо!"
    imgf 19791
    victoria "Да!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Alex_Sex1_6 = Movie(play="video/v_Victoria_Alex_Sex1_6.mkv", fps=30)
    show videov_Victoria_Alex_Sex1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgd 19576
    victoria "Аааа!"
    victoria "Быстрее, Алекс! Да!"
    imgf 19577
    victoria "О, я сейчас кончу!!!"
    imgd 19578
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Alex_Sex1_3 = Movie(play="video/v_Victoria_Alex_Sex1_3.mkv", fps=30)
    show videov_Victoria_Alex_Sex1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    alex_photograph "Да... Я тоже!"
    victoria "Ааааа!"
    # Виктория либо отстраняется, либо перестает двигаться
    music2 Groove2_85
    img 19579 vpunch
    sound Jump2
    alex_photograph "Эй!"
    victoria "Алекс!"
    victoria "Ты согласен сделать фотосессию со мной?"
    alex_photograph "Что? А, да-да... Иди сюда."
    music2 Loved_up2
    # притягивает ее к себе
    imgd 19570
    w
    sound chpok3
    img 19571 vpunch
    alex_photograph "Давай быстрее, не останавливайся!"
    # она снова его тормозит

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Alex_Sex1_5 = Movie(play="video/v_Victoria_Alex_Sex1_5.mkv", fps=30)
    show videov_Victoria_Alex_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Alex_Sex1_4 = Movie(play="video/v_Victoria_Alex_Sex1_4.mkv", fps=30)
    show videov_Victoria_Alex_Sex1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19580
    victoria "Что 'да'? Так ты согласен на фотосессию, Алекс?"
    alex_photograph "Черт! Да, я сделаю эту фотосессию!"


    # он начинает снова двигаться
    # Виктория отворачивается от него и улыбается
    # и делает вид, что кончает
    sound ahhh1
    imgf 19581
    w
    # sound ahhh1
    img 19582
    victoria "ААА!!!"
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan11
    victoria "ААААА!!!"
    menu:
#        "Кончить внутрь Виктории.":
#            alex_photograph "Я сейчас кончуууу!!!"
#            alex_photograph "Оооо!"
#            alex_photograph "Оооооо!"
#            pass
        "Кончить на киску Виктории.":
            imgf 19583
            alex_photograph "Я сейчас кончуууу!!!"
            img 19584 vpunch
            alex_photograph "Оооо!"
            alex_photograph "Оооооо!"
            img 19585
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            alex_photograph "ААААААААА!!!"
            w
            imgf 19586
            w
            pass
    # Виктория с самодовольной улыбкой смотрит на Мелани, которая все это снимает на камеру
    music2 stop
    fadeblack 1.5
    music Groove2_85
    imgf 19587
    victoria "Подружка Мелани, можешь нажать на стоп."
    victoria "Думаю, видео получилось отличное."
    victoria "С удовольствием буду его пересматривать."
    # Мелани опускает руку с телефоном и с отвращением смотрит на Викторию
    # Виктория распрямляется и стоит, поставив одну ногу на стул, видна ее киска со стекающей спермой Алекса
    imgd 19588
    victoria "А теперь подружка Мелани покажет, как ей нравится член Алекса."
    victoria "И моя киска..." # ехидно
    music stop
    sound plastinka1b
    img 19589 hpunch
    melanie "!!!" # зло
    music Pyro_Flow
    imgf 19590
    victoria "Ну же, подружка..."
    victoria "Докажи нам с Алексом, что тебе это очень нравится."
    melanie "Я думаю, что на сегодня досточно доказательств... Подружка Виктория."
    # Виктория хихикает и говорит Алексу
    # Алекс стоит возле Виктории
    music Groove2_85
    imgd 19591
    sound snd_woman_laugh3
    victoria "Моя подружка Мелани такая застенчивая."
    victoria "Хочет это сделать и стесняется. Хи-хи."
    imgf 19592
    alex_photograph "Мелани, дорогая."
    alex_photograph "Если тебе и правда это так нравится, то тебе нечего стесняться."
    alex_photograph "Я с удовольствием посмотрю на то, как ты работаешь своим язычком."
    alex_photograph "Это так сексуально, милая!"
    imgd 19593
    victoria "Слышала, подружка Мелани? Алекс хочет на это посмотреть."
#    victoria "Начнешь с моей киски, а потом оближешь член Алекса."
    melanie "..."
    victoria "Подружка Мелани, мы с Алексом ждем. Иди сюда."
    victoria "Ты должна следить за гигиеной такого знаменитого фотографа как он!"
    menu:
        "Сделать так, как говорит Виктория.":
            pass
    # Мелани зло смотрит на Алекса, потом на Викторию
    # та на нее смотрит угрожающе
    # Мелани кладет телефон Виктории на стол, подходит к Алексу
    # потом опускается на пол и приближает лицо к его члену
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Loved_up
    imgfl 19594
    alex_photograph "Да, милая. Иди ко мне."
#    alex_photograph "Я так соскучился по тебе."
#    alex_photograph "Ооооох..."
    imgf 19595
    w
    imgd 19597
    w
#    sound lick3
    imgd 19598
    w
    sound lick3
    imgd 19599
    w
    sound lick3
    imgd 19598
    w
    sound lick3
    imgd 19599
    w
    sound lick3
    imgd 19598
    w
    sound lick3
    imgd 19599
    w
    sound lick3
    imgf 19600
    alex_photograph "Как же это приятно, милая..."
    sound lick3
    imgd 19602
    w
    imgf 19601
    alex_photograph "Ммммм..."
    # Виктория смотрит на это и ехидно улыбается
#    victoria "Теперь очередь Алекса."
#    victoria "Покажи, как тебе нравится его член."
    sound snd_woman_laugh3
    imgd 19596
    victoria "А теперь подружка покажет, как ей нравится моя киска."
    victoria "Подружка должна заботиться о ней и следить за ее чистотой..."
    victoria "Иди еко мне, подружка Мелани."
    # Мелани с ненавистью смотрит на Викторию
    # встает от Алекса и наклоняется перед Викторией, начинает лизать ей
    music Pyro_Flow
    imgf 19789
    w
    imgd 19603
    w
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    imgfl 19790
    w
    imgf 19604
    victoria "О, да... Какая же ты хорошая, подружка Мелани..."
    # Алекс пристально смотрит и у него начинает вставать

    sound lick3
    imgd 19606
    w
    imgf 19607
    alex_photograph "Мммм... Мелани, это так эротично..."
    alex_photograph "Какая же ты красивая, милая!"
    alex_photograph "Я снова начинаю возбуждаться..."
    imgd 19608
    victoria "Еще немного... Да, вот так..."
    imgf 19609
    victoria "Алекс?"
    alex_photograph "Мммм..."
    victoria "Алекс!"
    alex_photograph "Ну что?"
    victoria "Тебе понравился наш с тобой секс, Алекс?"
    imgd 19610
    alex_photograph "Я хочу еще..."
    alex_photograph "Только красивую... Мммм... Как Мелани..."
#    sound vjuh2
    imgf 19611
    w
    sound Jump1
    imgd 19612
    alex_photograph "Как же ты меня возбуждаешь, милая... Ооох..."

    imgd 19605
    victoria "Не забудь облизать мою ножку..."
    victoria "А то может капнуть и испачкать твой стул. Хи-хи!"

    imgd black_screen

    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    scene black
    sound v_Victoria_Melanie_Licking2_1
    image videov_Victoria_Melanie_Licking2_1 = Movie(play="video/v_Victoria_Melanie_Licking2_1.mkv", fps=20, loop=False, image="/images/Slides/v_Victoria_Melanie_Licking2_1_end.jpg")
    show videov_Victoria_Melanie_Licking2_1
    wclean
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19613
    victoria "Достаточно, подружка Мелани."
    music Groove2_85
    victoria "Подружка Мелани не будет против." # ехидно
    victoria "Она с радостью отдаст свою попу такому красавчику, как ты, Алекс."
    victoria "Да ведь, подружка?"
    # Мелани отстраняется
    imgd 19614
    melanie "..."
    menu:
        "Да.":
            pass
    # Мелани сквозь зубы, глядя на Алекса
    imgf 19615
    melanie "Да, подружка..."
    sound Jump1
    imgd 19616
    alex_photograph "О, Мелани!"
    alex_photograph "Давай сделаем это прямо сейчас!"
    alex_photograph "Я целый день мечтал о том, как возьму тебя!"
    imgf 19617
    melanie "Ты хочешь это сделать прямо сейчас?"
    melanie "Ты уже это делал утром..."
    melanie "Давай уже... Не сегодня..."
    imgd 19618
    alex_photograph "Да, милая! Я хочу сейчас снва!"
    alex_photograph "Мне не терпится скорее войти в тебя!"
    alex_photograph "Снимай одежду, я хочу видеть твое восхитительное тело!"
    imgf 19619
    melanie "!!!"
    victoria "Ну же, подружка!"
    # Мелани зло смотрит на него
    # потом встает и раздевается, ложится на диван на подлокотник (https://cdn.discordapp.com/attachments/625678994083414052/738836379693482004/unknown.png)
    # Алекс ласкает ее грудь, потом гладит ладонью ягодицы
    fadeblack 1.5
    sound highheels_short_walk
    pause 1.5
    sound snd_fabric1
    pause 1.5
    music2 Loved_Up
    imgfl 19620
    w
    imgf 19621
    alex_photograph "О, милая..."
    imgd 19622
    alex_photograph "Как ты прекрасна..."
    alex_photograph "Я так хочу тебя!"
    imgf 19623
    # Алекс забирается на диван и пристраивается к Мелани сзади
    sound vjuh3
    pause 1.0
    sound kiss1
    imgd 19624
    w
    sound kiss1
    imgd 19625
    w
    sound kiss1
    imgd 19626
    w
    imgf 19627
    alex_photograph "Ты самая красивая женщина на свете, Мелани!"
    alex_photograph "С тобой никто не сравнится!"
    # Мелани бросает злорадный взгляд на Викторию
    music2 Loved_up2
    imgd 19628
    alex_photograph "О, моя Мелани!!"
    sound chpok6
    img 19629 vpunch
    alex_photograph "Оооооо!"
    # Алекс входит в Мелани
    # Виктория в это время спрашивает
#    sound ahhh1
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Alex_Sex1_1 = Movie(play="video/v_Victoria_Melanie_Alex_Sex1_1.mkv", fps=30)
    show videov_Victoria_Melanie_Alex_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19630
    victoria "Алекс, а когда мне приходить на мою фотосессию?"
    # он не обращает на нее внимания
#    sound ahhh1
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Alex_Sex1_2 = Movie(play="video/v_Victoria_Melanie_Alex_Sex1_2.mkv", fps=30)
    show videov_Victoria_Melanie_Alex_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19631
    alex_photograph "Меланиии... Моя богиня..."
    imgd 19632
    victoria "Алекс! Ты меня слышишь?"
    # он не совсем доволен, что она его отвлекает
    music2 Power_Bots_Loop
    img 19633 vpunch
    alex_photograph "Что?!"
    music2 Groove2_85
    imgd 19634
    victoria "Когда мне приходить на фотосессию?"
    # отворачивается от Виктории и снова все внимание на Мелани
    music2 Loved_up2
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Alex_Sex1_3 = Movie(play="video/v_Victoria_Melanie_Alex_Sex1_3.mkv", fps=30)
    show videov_Victoria_Melanie_Alex_Sex1_3
    with fade
    alex_photograph "Я смогу провести ее на днях..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19635
    alex_photograph "Ммммм..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Alex_Sex1_4 = Movie(play="video/v_Victoria_Melanie_Alex_Sex1_4.mkv", fps=30)
    show videov_Victoria_Melanie_Alex_Sex1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Виктория снова говорит Алексу
    #sound ahhh1
    imgd 19636
    victoria "Алекс, я позвоню тебе, чтобы договариться о встрече в фотостудии."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Alex_Sex1_5 = Movie(play="video/v_Victoria_Melanie_Alex_Sex1_5.mkv", fps=30)
    show videov_Victoria_Melanie_Alex_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # забирает со стола свой телефон и направляется к выходу
    sound highheels_short_walk
    imgf 19637
    victoria "Подружка Мелани."
    victoria "Спасибо за такое классное видео."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Alex_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Alex_Sex1_6 = Movie(play="video/v_Victoria_Melanie_Alex_Sex1_6.mkv", fps=30)
    show videov_Victoria_Melanie_Alex_Sex1_6
    with fade
    victoria "Теперь я буду его пересматривать по вечерам, подружка."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 stop
    fadeblack 1.5
    pause 1.5
    # уходит, затемнение
    return

# следующий день, когда Моника приходит в свой кабинет на работу
# Моника при клике на лифт, попадает в фотостудию
label ep215_dialogues5_alex_4:
    # в фотостудии находится Виктория в розовом платье
    # она позирует, Алекс фотографирует ее
    # Виктория стоит в позе, с которой ей не видно, что Моника пришла
#    scene black_screen
#    with Dissolve(1)
#    stop music fadeout 1.0
#    call textonblack(t_("Некоторое время спустя..."))
#    scene black_screen
#    with Dissolve(1)
#    sound snd_lift
#    pause 1.5
#    sound snd_fabric1
    fadeblack 2.0
    sound highheels_short_walk
#    pause 0.5
#    sound camera_lens1
#    pause 0.5
#    sound camera_lens1
    music Pyro_Flow
    imgfl 19520
    sound camera_lens1
    w
    call photoshop_flash() from _rcall_photoshop_flash_215
    w
    mt "Какого черта?!"
    mt "Что эта тварь тут делает?!"
    mt "?!?!?!"
    # пока Моника в шоке смотрит, звук каблуков
    # к Монике подходит Мелани
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music ZigZag
    imgf 19521
    melanie "Миссис Бакфетт..."
    # Моника вздрагивает от неожиданности
    imgd 19522
    m "Мелани?"
    imgf 19523
    m "Мелани! Ты видишь ЭТО?!"
    m "Какого?.."
    # Мелани ее перебивает
    imgd 19524
    melanie "Тсс. Тише, Миссис Бакфетт."
    melanie "У меня к вам срочное дело."
    imgf 19525
    m "Срочное?"
    imgd 19526
    melanie "Да. Очень срочное."
    melanie "Пойдемте в гримерку."
    # затемнение, звук каблуков
    return

# гримерке
label ep215_dialogues5_alex_5:
    # Мелани и Моника стоят в гримерке
    # телефон Виктории лежит на видном месте на столике Мелани, рядом стоит ее сумочка
    fadeblack
    sound highheels_run2
    pause 2.0
    music Stealth_Groover
    imgfl 19410
    w
    imgf 19411
    m "Мелани, что происходит?!"
    m "Кто разрешил проводить фотосессию для этой сучки?!"
    m "?!?!?!"
    # Мелани хватает ее телефон со столика и говорит Монике
    imgd 19412
    melanie "Нам надо торопиться, Миссис Бакфетт!"
    melanie "У нас появился отличный шанс расправиться с этой мелкой дрянью!"
    imgf 19414
    m "Шанс?! Но... Как, Мелани?"
    m "Что ты задумала?"
    # Мелани показывает телефон в своих руках
    imgd 19413
    melanie "На этом телефоне есть видео, компрометирующее Викторию."
    # Моника подозрительно
    imgf 19415
    m "Что это за видео?"
    imgd 19416
    melanie "На нем Алекс и Виктория занимаются сексом."
    music stop
    sound plastinka1b
    img 19417 vpunch
    m "Что?!"
    m "Алекс и Виктория?!"
    music ZigZag
    m "Ты в этом уверена, Мелани?"
    m "Откуда ты это знаешь?"
    # Мелани мнется, но решает не говорить правду
    imgf 19418
    melanie "Это... Это точная информация, Миссис Бакфетт..."
    melanie "Из достоверного источника..."
    melanie "Миссис Бакфетт."
    imgd 19419
    melanie "Эта стерва Виктория просчиталась на этот раз."
    melanie "И мы просто обязаны этим воспользоваться, пока она занята фотосессией!"
    # Моника спрашивает
    music Groove2_85
    imgf 19420
    m "Что ты предлагаешь с этим сделать?"
    melanie "Миссис Бакфетт, вы знаете, кому это показать..."
    # Моника задумчиво
    imgd 19421
    m "Дик..."
    melanie "Да, Миссис Бакфетт."
    imgf 19422
    m "Виктория охраняет Дика, как цепной пес, и обычно к нему в кабинет не пройти..."
    m "Но сейчас..."
    melanie "Сейчас Викторию интересует только фотосессия и мы должны поторопиться!"
    m "Да! Нам надо поспешить!"
    fadeblack
    sound highheels_run2
    pause 1.5
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)    # затемнение, звук каблуков, лифт
    # звук мотора, Мелани с Моникой едут к Дику напряженная музыка
    $ melanieAlexVictoriaSex3 = True # Мелани и Моника украли телефон Виктории из гримерки и поехали к Дику
    return

# кабинет Дика
label ep215_dialogues5_alex_6:
    # Моника и Мелани заходят в кабинет Дика
    # Дик сидит за своим рабочим столом, в руках какие-то документы
    # поднимает взгляд на вошедших Монику и Мелани, документы падают из рук на стол
    # он крайне удивлен, смотрит то на одну, то на другую в растерянности
#    scene black_screen
#    with Dissolve(1)
#    stop music fadeout 1.0
#    call textonblack(t_("Некоторое время спустя..."))
#    scene black_screen
#    with Dissolve(1)
    pause 2.0
    sound highheels_run2
    pause 1.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.5
    music Stealth_Groover
    imgfl 19515
    w
    sound Jump1
    imgd 19516
    w
    sound snd_heavy_papers_drop
    img 19517 hpunch
    w
    imgf 19518
    dick "Моника?"
    dick "М-мелани?"
    # Моника ему уверенно
    imgd 19519
    m "Здравствуй, Дик."
    # затемнение, смена кадра на фотостудию
    # тем временем в фотостудии
    # фотосессия продолжается, Виктория сменяет одну позу на другую, видно, что она крайне довольна собой
    # Алекс недоволен, видно, что ему не нравится с ней общаться

    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_67
    scene black_screen
    with Dissolve(1)
    music Groove2_85
#    sound camera_lens1
    imgfl 19527
    victoria "Алекс, это красивая поза?"
    sound camera_lens1
    w
    call photoshop_flash() from _rcall_photoshop_flash_216
    w
    imgf 19528
    victoria "Может, мне встать вот так?"
    alex_photograph "Да, Виктория. Это хорошая поза."
    sound camera_lens1
    w
    call photoshop_flash() from _rcall_photoshop_flash_217
    w
    imgd 19529
    victoria "Алекс, а может ты возьмешь кадр поближе?"
    victoria "И ниже."
    victoria "Мне кажется, так получится намного сексуальнее."
    sound camera_lens1
    w
    call photoshop_flash() from _rcall_photoshop_flash_218
    w
    imgf 19530
    alex_photograph "Я не уверен, но можно попробовать."
    sound camera_lens1
    w
    call photoshop_flash() from _rcall_photoshop_flash_219
    w
    imgd 19531
    victoria "А если я вот так поставлю ножку, будет лучше?"
    alex_photograph "Да, Виктория. Поставь. Давай посмотрим."
    sound camera_lens1
    w
    call photoshop_flash() from _rcall_photoshop_flash_220
    w
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_68
    scene black_screen
    with Dissolve(1)
    # затемнение, смена кадра на офис Дика
    # тем временем в офисе Дика
    # Моника и Мелани сидят в кабинете Дика, он их внимательно слушает
    fadeblack 2.0
    music Stealth_Groover
    imgf 19446
    w
    imgd 19448
    m "Дик, ты все это время ошибался в своей Виктории!"
    m "Она на самом деле не такая хорошая, какой старается казаться перед тобой!"
    m "Это все маска, Дик! Она обманывает тебя!"
    # Дик с серьезным лицом
    music Groove2_85
    imgf 19449
    dick "Я не верю тебе, Моника."
    dick "Ты уже однажды пыталась оговорить Викторию."
    dick "Теперь ты снова за свое..."
    # в разговор вступает Мелани
    music ZigZag
    imgd 19450
    melanie "Мистер Дик. Вы такой умный и такой хороший человек."
    melanie "Я полностью на вашей стороне и понимаю, что вам трудно в это поверить."
    melanie "Но Миссис Бакфетт говорит правду. Я подтверждаю каждое ее слово."
    imgf 19451
    melanie "И мы пришли к вам сегодня, потому что хорошо к вам относимся."
    melanie "И переживаем из-за того, что эта девочка вас обманывает."
    # Дик слушает Мелани, он в шоке
    music Groove2_85
    imgd 19452
    dick "Мелани, я давно знаю Викторию."
    dick "Она искренняя и добрая девушка."
    dick "Это чистый сосуд искренности и непорочности!"
    dick "Виктория не способна никого обмануть!"
    # Моника психует
    music Pyro_Flow
    imgf 19453
    mt "О, боги! Какой же идиот!"
    mt "!!!"
    imgd 19454
    m "Она не способна на обман?!"
    m "Да она самая лицемерная дрянь, которую я видела в своей жизни!"
    # Дик продолжает сомневаться в словах Моники и Мелани
    imgf 19455
    dick "Моника, не надо говорить так о Виктории!"
    imgd 19456
    m "Эта сучка тобой манипулирует, а ты ей веришь!"
    # Дик начинает злиться
    imgf 19457
    dick "Моника!"
    music ZigZag
    imgd 19458
    melanie "Мистер Дик, у нас есть доказательство того, что Виктория вас обманывает."
    # Дик удивленно и растерянно
    imgf 19459
    dick "Доказательство?"
    melanie "Да. В этом телефоне есть видео... На котором Виктория вам изменяет."
    dick "Что?!"
    imgd 19460
    melanie "Да. Посмотрите его, Мистер Дик."
    melanie "И вы все поймете без лишних слов."
    # Мелани встает со стула, подходит к столу Дика и протягивает ему телефон Виктории, он берет его в руки
    # и в этот момент к нему в кабинет заходит Виктория
    # Мелани спокойна, смотрит убийственным взглядом на Викторию и возвращается на свое место
    # Моника про себя злорадствует
    sound highheels_short_walk
    imgf 19461
    w
    #sound highheels_short_walk
    imgd 19462
    w
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 19463
    w
    imgf 19464
    w
    music Stealth_Groover
    imgd 19465
    mt "Пришла, дрянь!"
    mt "Это последние твои минуты в этом кабинете!"
    mt "Сучка!"
    mt "Наконец-то, этот миг настал!"
    mt "!!!"
    # Виктория спокойна, она самодовольно улыбается и подходит к Дику поближе
    # Дик смотрит на Викторию с обожанием
    music Groove2_85
    imgf 19466
    dick "Виктория, дорогая!"
    dick "Я не могу поверить в то, что я сейчас улышал о тебе!"
    # она делает невинное личико, наклоняется к нему, сложив руки у своего подбородка
    imgd 19467
    victoria "Мистер Дик, эти женщины говорят неправду про меня."
    victoria "Вы же не верите им? Вы же знаете, что я не такая!"
    # Дик возмущенно
    imgd 19468
    dick "Они говорят, что на этом телефоне есть видео, на котором ты якобы изменяешь мне!"
    # Виктория с невинным видом
    victoria "Нет конечно! Это неправда, Мистер Дик!"
    imgf 19469
    dick "Ты готова доказать это?"
    dick "Ты согласна, чтобы я посмотрел видео на твоем телефоне и проверил их слова?"
    imgd 19470
    victoria "Да, можете взять мой телефон и проверить его, Мистер Дик!"
    victoria "Мне нечего скрывать от вас!"
    # Дик смотрит на телефон
    imgf 19471
    dick "Ты мне говоришь, что тебе нечего скрывать, а на телефоне стоит пароль..."
    dick "Я не могу его разблокировать."
    # Виктория невинно
    imgd 19472
    victoria "Мистер Дик, дорогой, вы ведь его знаете..."
    dick "Знаю? И какой же он?"
    victoria "Это ваш день рождения, Мистер Дик."
    victoria "Ведь мне нечего от вас скрывать..."
    # Дик с сомнением смотрит на Монику и Мелани, включает телефон
    imgf 19473
    w
    imgd 19474
    dick "Я вижу здесь только одно видео..."
    # Моника вскакивает со стула
    img 19475 vpunch
    m "Да, это оно!"
    m "Посмотри его и ты узнаешь всю правду!"
    m "!!!"
    # Дик включает видео, а там ролик, где Алекс платит деньги Мелани за минет
    # показываем арты со сцены на телефоне и текст прямо с той сцены
############### текст с той сцены
    imgf 19476
    alex_photograph "Какой у тебя прейскурант, Мелани?"
    melanie "!!!"
    victoria "???"
    # Мелани отвечает
    imgd 19477
    melanie "Как обычно, сделаю минет за 50 долларов, секс стоит 100 долларов."
    # Алек бросает ей 50 баксов
    alex_photograph "Вот твой сегодняшний заработок."
    alex_photograph "Соси!"
    # Мелани медлит
    alex_photograph "Ну? Отрабатывай свои деньги!"
    # делает минет Алексу
    sound hlup19
    pause 0.5
    sound vjuh2
    imgd 19478
    alex_photograph "Ооооо, Меланиииии!!!"
    alex_photograph "Ааааааа!!!"
    alex_photograph "Возьми его глубже!"
    sound ahhh1
    imgd 19479
    alex_photograph "Ещеееее!!!"
    alex_photograph "Быстрее! Быстрее!!!"
    # Алекс кончает
    sound bulk1
    pause 0.5
    sound man_moan18
    imgd 19480
    alex_photograph "Дааа..."
    alex_photograph "Дааа!!!"
    alex_photograph "ДААААААА!!!"
###############

    # кадр на Дика с телефном в руках, звуки минета из телефона
    # Моника с Мелани в ужасе переглядываются

    music Power_Bots_Loop
    img 19482 vpunch
    m "!!!"
    img 19481 vpunch
    melanie "!!!"
    # Дик в шоке смотрит на Мелани
    music Groove2_85
    imgf 19483
    dick "Да, Мелани... Теперь я узнал всю правду!"
    dick "Ты, Мелани, сговорилась с интриганкой Моникой!"
    dick "Для того, чтобы опорочить моего ангела! Эту невинную девушку!"
    dick "Этот образец морали и чистоты!"
    # ввернуть эпитет
    imgd 19484
    m "Но Дик!"
    dick "Тихо! Больше не хочу слышать ни слова!"
    # Дик возмущается на Мелани и Монику
    dick "Вы обе не стоите и мизинца этого непорочного создания!"
    imgf 19485
    dick "Как вы смеете наговаривать на нее эти грязные вещи?!"
    dick "Это клевета!"
    dick "Я подам на вас обеих в суд за клевету!"
    # Виктория его успокаивает
    imgd 19493
    victoria "Мистер Дик, дорогой, я не в обиде на них."
    victoria "Не нужно их наказывать, Мистер Дик."
    imgf 19494
    dick "Виктория, как ты можешь за них заступаться?!"
    dick "Я вообще не хочу с ними иметь ничего общего!"
    dick "Я отказываюсь от дела Моники, которое доставляет мне столько хлопот!"
    # Виктория продолжает его успокаивать
    music Power_Bots_Loop
    img 19486 vpunch
    mt "О НЕТ!!!"
    music Groove2_85
    imgf 19487
    victoria "Все хорошо, Мистер Дик."
    victoria "Они просто ошиблись."
    victoria "Давай будем добрее к ним и простим их за эту нелепую ошибку."
    dick "Ты точно не хочешь наказать их за эту попытку очернить тебя в моих глазах?"
    imgd 19488
    victoria "Нет, Мистер Дик. Я не хочу, чтобы вы их наказывали."
    victoria "Мы просто попросим их покинуть ваш кабинет и больше сюда не возвращаться."
    victoria "Мне кажется, этого будет достаточно, Мистер Дик."
    # Дик смотрит на нее влюбленными глазами, она ему мило улыбается
    imgf 19489
    dick "Виктория, ты настоящий ангел."
    victoria "Спасибо, дорогой."
    # Дик смотрит на Монику и Мелани с негодованием
    imgd 19490
    dick "Этот кабинет только для таких непорочных ангелов, как моя Виктория."
    dick "Миссис Бакфетт, Мисс Мелани, покиньте мой кабинет!"
    # Моника и Мелани в шоке, смотрят друг на друга, потом на Викторию
    music Master_Disorder
    img 19491 vpunch
    m "!!!"
    melanie "!!!"
    # Виктория им мило улыбается
    imgd 19492
    victoria "Подождите меня возле моего рабочего места, девочки..."
    # затемнение
    return

# приемная Дика
label ep215_dialogues5_alex_7:

    # в применой стоят злые Мелани и Моника и довольная Виктория
    # Виктория ехидно смотрит на них
    fadeblack
    sound snd_door_locked1
    pause 1.0
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 19436
    victoria "Ой, подружки, я так рада видеть вас!"
    victoria "Так здорово что вы зашли ко мне!"
    music Power_Bots_Loop
    imgf 19437
    m "!!!"
    melanie "!!!"
    music Groove2_85
    imgd 19438
    victoria "Я тут подумала, что мы давно не устраивали девичники!"
    victoria "Вы же не против будете прийти ко мне домой, подружки?"
    victoria "Ведь этот девичник будет особенным!"
    # Моника и Мелани в шоке переглядываются
    img 19439  vpunch
    m "!!!"
    img 19440  vpunch
    melanie "!!!"
    imgf 19441
    victoria "Мои подружки придут ко мне?"
    victoria "Ты придешь, подружка Мелани?"
    # Мелани зло, сквозь зубы
    imgd 19442
    w
    melanie "Да!"
    melanie "!!!"
    imgf 19443
    victoria "А подружка Моника тоже придет?"
    victoria "Она ведь не откажет мне?"
    # Моника тоже зло
    imgd 19444
    m "Приду!"
    m "!!!"
    imgf 19447
    victoria "Ой, я так рада!"
    victoria "Как же здорово, что мы такие хорошие подружки!"
    victoria "Я скоро вам сообщу о моем мероприятии!"
    imgd 19445
    w
    fadeblack
    sound highheels_run2
    pause 1.5
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    # немая пауза, Моника с Мелани смотрят на нее как на психопатку
    # затемнение
    # звук мотора
    return

# гримерка в офисе
label ep215_dialogues5_alex_8:
    # Мелани и Моника, обе в бешенстве
    music Power_Bots_Loop
    imgfl 19423
    sound anger2
    m "Эта мелкая сучка нас подставила!!!"
    m "Ты видела, как она себя ведет с этим кретином Диком?!"
    melanie "Я не позволю этой сиколявке так обращаться со мной!"
    melanie "Я уничтожу ее!"
    music ZigZag
    imgf 19424
    melanie "Миссис Бакфетт, вы хотели знать, откуда я знаю про видео Алекса и Виктории?!"
    imgd 19425
    m "Да!"
    m "Что это за достоверный источник у тебя?!"
    m "Из-за которого мы попали в такую глупую ситуацию!"
    m "!!!"
    imgf 19426
    melanie "Миссис Бакфетт, я сама лично снимала это видео на ее телефон."
    music stop
    sound plastinka1b
    img 19427 hpunch
    m "Что?!"
    music ZigZag
    imgd 19428
    melanie "Помните, она в вашем кабинете мне сказала, что я должна устроить свидание с Алексом?"
    m "Помню..."
    melanie "Она вынудила меня пригласить Алекса жить со мной..."
    melanie "Теперь Алекс живет у меня."
    img 19429 vpunch
    m "О Боже!"
    m "Мелани..."
    imgf 19430
    melanie "А еще эта мелкая стерва мечтает стать моделью!"
    melanie "Алекс ей отказал в помощи и она решила переспать с ним ради фотосессии."
    melanie "А я все это снимала на ее телефон. По ее приказу."
    music Pyro_Flow
    imgd 19431
    m "Вот дрянь!!!"
    m "!!!"
    m "Она специально заставила тебя снять это видео на ее телефон!"
    m "Она знала, что мы будем действовать именно так!"
    music Master_Disorder
    imgf 19432
    melanie "Да!"
    melanie "И эта лицемерная стерва наменула мне на то..."
    melanie "На то, что Алекс - мой будущий муж!"
    melanie "!!!"
    imgd 19433
    m "!!!"
    m "!!!!!!"
    imgf 19434
    melanie "Эта Виктория - настоящий дьявол!"
    melanie "Мы обязательно расправимся с ней, Миссис Бакфетт!"
    imgd 19435
    m "Я не могу дождаться этого дня!"
    return
