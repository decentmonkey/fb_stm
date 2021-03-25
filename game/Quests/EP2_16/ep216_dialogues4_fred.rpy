default monicaJuliaFredVisit1 = False # Фред застукал Монику и Юлию у них в квартире
default monicaJuliaFredVisit2 = False # Моника делала ассликинг Юлии в комнате отдыха

default ep216_dialogues4_fred_7_last_day = 0

#call ep216_dialogues4_fred_1() # в квартире Юлии после утреннего секса, приходит Фред
#call ep216_dialogues4_fred_2() # после визита Фреда Моника стоит на улице возле дома Юлии, мысли
#call ep216_dialogues4_fred_3() # квартира Юлии, Моника ушла, разговор Юлии с Фредом
#call ep216_dialogues4_fred_4() # после визита Фреда Моника стоит на улице возле дома Юлии, хочет зайти обратно в квартиру, мысли
#call ep216_dialogues4_fred_5() # при клике на Юлию после визита Фреда
#call ep216_dialogues4_fred_6() # Моника при клике на Фреда после его визита к Юлии в квартиру, мысли
#call ep216_dialogues4_fred_7() # рабочий кабинет Моники, h-сцена с Юлией в офисе


# сразу после сцены утреннего куни Юлии у нее в квартире (ep213_dialogues5_julia_8, при выборе пунктов меню "Продолжить ласкать Юлию")
label ep216_dialogues4_fred_1:
    # Юлия лежит, распластавшись на кровати, прибалдевшая
    # Моника валяется расслабленно раздвинув ноги или как-то
    fadeblack 1.5
    music Groove2_85
    imgfl 32399
    w
    imgf 32400
    julia "Ох, Миссис Бакфетт, это было восхитительно!"
    julia "Мммм... Какое хорошее начало дня!"
    music Stealth_Groover
    imgd 32401
    mt "Еще бы!"
    mt "Какой-то бывшей никчемной гувернантке ее хозяйка и ее Босс делает ТАКОЕ!"
    imgf 32402
    mt "Неужели она не понимает, что мне противны все эти извращенства?!"
    mt "Как можно быть такой дурой?!"
    mt "!!!"
    imgd 32401
    mt "Нужно будет снова поговорить с ней об этом ее родственнике..."
    mt "И об отъезде из страны..."
    mt "Моя свобода уже так близко!"
    mt "Моника, осталось потерпеть эту влюбленную дурочку совсем немного!"
    mt "Потом ты сможешь послать ее ко всем чертям!"
    mt "И начать жизнь с чистого листа!"
    # ее мысли прерывает звук открывающейся двери
    sound snd_door_open1
    img 32403 hpunch
    w
    fadeblack
    sound snd_door_locked1
    pause 1.5
    music Master_Disorder
    # Моника испуганно накрывается одеялом, Юлия тоже, смотрят в сторону входной двери
    imgf 32404
    sound man_steps
    w
    # звук мужских шагов
    imgd 32405
    m "!!!"
    m "Это кто?!"
    m "У кого-то есть ключи от твоей квартиры?!"
    julia "Н-нет..."
    # Моника с кровати
    imgd 32406
    sound Jump1
    w
    # звук пластинка
    music stop
    sound plastinka1b
    img 32407 hpunch
    m "ФРЕД?!"
    music Power_Bots_Loop
    m "!!!"
    m "!!!!!"
    julia "Ой..."
    music Groove2_85
    imgd 32408
    fred "Миссис Бакфетт?"
    fred "Отлично выглядите!" # со своей улыбочкой

    # Моника вскакивает, прикрывается и орет
    music Power_Bots_Loop
    img 32409 vpunch
    m "Какого черта ты тут делаешь, Фред?!"
    m "!!!"
    music Groove2_85
    fred "У меня к Вам, Миссис Бакфетт, тот же вопрос."
    fred "Что Вы тут делаете? Я весьма удивлен!"
    m "Это не твое дело, что Я тут делаю!"
    # Моника смотрит на Юлию
    music Power_Bots_Loop
    imgd 32410
    m "Почему этот никчемный водитель заходит к тебе в квартиру, как к себе домой?!"
    m "Как это понимать?!"
    # Юлия испуганно молчит
    imgd 32411
    w
    music Groove2_85
    imgf 32412
    $ questHelp("julia_51", True)
    fred "Миссис Бакфетт, хочу Вам напомнить, что я профессионал."
    fred "И посчитал своим профессиональным долгом проверить..."
    fred "Все ли хорошо у моей подруги Юлии."
    fred "Кстати, дверь была открыта..."
    # Моника снова смотрит на Юлию в бешенстве
    music Power_Bots_Loop
    imgd 32411
    m "Тебя в твоей провинции не учили закрывать двери на ночь?!"
    m "?!?!?!"
    mt "ДУРА!!!"
    mt "!!!"
    music Groove2_85
    julia "Я... Я не знаю как так получилось..."
    julia "Я забыла..."
    imgf 32413
    fred "Не волнуйтесь, Миссис Бакфетт."
    fred "Я же профессионал."
    fred "Поэтому умею хранить чужие секреты."
    fred "Я никому не скажу о Вашей тайной связи с Вашей помощницей..."
    fred "И Вашей бывшей гувернанткой."
    # Монику бомбит
    music Pyro_Flow
    img 32414 hpunch
    m "НЕТ НИКАКОЙ СВЯЗИ!!!"
    m "И ВООБЩЕ!!!"
    m "ТЕБЯ ЭТО НЕ КАСАЕТСЯ!!!"
    m "ТВОЕ ДЕЛО СЛЕДИТЬ ЗА МАШИНОЙ!!!"
    m "А НЕ СОВАТЬ СВОЙ МЕРЗКИЙ НОС НЕ В СВОИ ДЕЛА!!!"
    m "НИКЧЕМНЫЙ ВОДИТЕЛЬ!!!"
    m "!!!"
    imgd 32415
    m "НЕ СМОТРИ НА МЕНЯ!!!"
    m "ОТВЕРНИСЬ БЫСТРО!!!"
    sound Jump2
    imgd 32416
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    sound highheels_run1
    pause 1.5
    sound snd_door_locked1
    pause 1.5
    # Фред, ехидно улыбаясь, отворачивается
    # затемнение, звук надевания одежды, бег на каблуках, хлопает входная дверь
    $ monicaJuliaFredVisit1 = True # Фред застукал Монику и Юлию у них в квартире
    return

# Моника стоит на улице возле дома Юлии, мысли
label ep216_dialogues4_fred_2:
    # не рендерить!!
    mt "Как ты могла допустить ТАКОЕ, Моника?!"
    mt "Этот гребаный мерзавец Фред теперь все знает!!!"
    mt "!!!"
    mt "А что, если он всем расскажет?!"
    mt "Боже! Какой кошмар!!!"
    mt "У него теперь новый повод для того, чтобы шантажировать МЕНЯ!!!"
    mt "Юлия идиотка!!!"
    mt "Бесполезная, глупая идиотка!!!"
    mt "Никчемная!!!"
    mt "Это все из-за ее тупости!!!"
    mt "ААААА!!!"
    mt "НЕНАВИЖУ!!!"
    mt "!!!"
    call ep216_dialogues4_fred_3() from _rcall_ep216_dialogues4_fred_3
    call refresh_scene_fade() from _rcall_refresh_scene_fade_117
    return

# тем временем, в квартире Юлии
# Юлия также сидит на кровати, Фред стоит посреди комнаты
label ep216_dialogues4_fred_3:
    # Юлия растерянно смотрит на него
    music Groove2_85
    imgfl 32417
    w
    imgf 32418
    julia "Мистер Фред..."
    julia "Вы... Вы что-то хотели?"
    # Фред отвечает с улыбочкой
    imgd 32419
    fred "Я просто хотел проверить, как у тебя дела, Юлия..."
    fred "Не обижает ли тебя Миссис Бакфетт..."
    imgf 32420
    fred "Но теперь я удостоверился, что у тебя все в порядке."
    julia "Д-да..."
    julia "Все хорошо..."
    # Фред подходит к кровати и берет в руку одеяло, которым прикрывается Юлия
    sound vjuh3
    imgd 32421
    w
    imgd 32422
    fred "Юлия..."
    fred "Я также считаю своим профессиональным долгом предложить тебе..."
    # тянет одеяло с Юлии, но та его удерживает
    fred "Свою поддержку, если вдруг у тебя возникнут проблемы с Миссис Бакфетт."
    fred "А такая ситуация весьма вероятна, Юлия..."
    fred "Ты даже не представляешь, на что способна эта женщина ради своей выгоды."
    music Power_Bots_Loop
    imgd 32423
    julia "Неправда!"
    julia "Она любит меня!"
    julia "У нас с ней серьезные отношения!" # сердито выдергивает одеяло из руки Фреда
    sound Jump2
    img 32424 hpunch
    w
    # Фред смеется на это
    music Groove2_85
    imgd 32425
    fred "Просто помни о моем предложении..."
    fred "Ты всегда можешь обратиться ко мне за помощью, Юлия."
    julia "..."
    sound man_steps
    imgf 32426
    w
    # Фред смотрит на нее с улыбочкой, разворачивается и уходит
    # Юлия в растерянности смотрит ему вслед
    imgd 32427
    w
    fadeblack
    sound snd_door_locked1
    pause 1.5
    return

# Моника стоит на улице возле дома Юлии, хочет зайти обратно в квартиру, мысли
label ep216_dialogues4_fred_4:
    # не рендерить!!
    mt "Я не пойду туда!"
    mt "Не хочу видеть этого мерзавца Фреда!"
    return

# офис Моники
# при клике на Юлию после визита Фреда
label ep216_dialogues4_fred_5:
    # использовать имеющиеся диалоговые арты!
    music Groove2_85
    imgfl 16495
    mt "Чертова дура Юлия!"
    mt "Я надеюсь, она не рассказала Фреду о нашей связи!"
    mt "Мне нужно будет спросить у нее..."
    # подходит к Юлии
    sound highheels_short_walk
    imgf 16496
    w
    music Hidden_Agenda
    imgd 16497
    m "Юлия..."
    julia "Миссис Бакфетт, Вы не сердитесь на меня?"
    julia "Я не знаю, как я могла забыть закрыть дверь..."
    m "Конечно, я не сержусь, милая..."
    # Юлия лезет к ней обниматься
    imgf 30604
    julia "О, Миссис Бакфетт!"
    julia "Я так переживала, что Вы расстроитесь из-за того..."
    julia "Что Мистер Фред все о нас узнал..."
    # Моника отстраняется
    music stop
    sound plastinka1b
    img 30601 hpunch
    m "В смысле?!"
    m "Ты ему рассказала о наших отношениях?!"
    m "?!?!?!"
    music Groove2_85
    julia "Да, я ему по-дружески все рассказала."
    julia "Он обещал никому не говорить о нашей маленькой тайне."
    julia "Не переживайте, Миссис Бакфетт."
    julia "Мистеру Фреду можно доверять."
    music Pyro_Flow
    imgd 30600
    mt "Черт!"
    mt "Нашла кому доверять!"
    mt "ДУРА!!!"
    mt "!!!"
    # Моника зло
    sound highheels_short_walk
    imgf 16491
    julia "Миссис Бакфетт, поцелуйте меня. Я так соскучилась!"
    m "Мне некогда, Юлия!"
    m "У меня много важных дел!"
    # Юлия обиженно клянчит
    music Groove2_85
    imgd 30603
    julia "Я так и знала, что Вы не любите меня, Миссис Бакфетт..."
    julia "Если бы Вы меня любили, то любили бы и целовать меня..."
    julia "И постоянно этого хотели бы..."
    imgd 20885
    mt "О Боже!!!"
    mt "Когда же прекратится весь этот цирк?!"
    mt "Так, Моника, помни о том, что ты ее просто используешь."
    mt "Тебе даже на руку, что она такая глупая."
    mt "И не замечает, насколько она тебе противна."
    # Моника обнимает Юлию
    music Hidden_Agenda
    imgf 16487
    m "Ну что ты, милая..."
    m "Конечно, я люблю тебя..."
    m "И поцелую тебя... С удовольствием..."
    # поцелуй
    music Loved_Up
    imgd 32428
    w
    sound kiss2
    imgd 32429
    w
    imgf 30609
    julia "Ммммм..."
    julia "Я обожаю целоваться с Вами, Миссис Бакфетт..."
    julia "И не только целоваться..." # игриво
    mt "Начинается!"
    mt "!!!"
    music Hidden_Agenda
    imgd 30620
    m "Я тоже, милая..."
    m "А теперь мне пора."
    m "Мы продолжим позже."
    julia "Буду ждать с нетерпением, Миссис Бакфетт."
    # Моника отходит от нее
    sound highheels_short_walk
    imgf 16490
    w
    music Pyro_Flow
    imgd 16491
    mt "Дьявол!"
    mt "Зачем эта дура все рассказала Фреду?!"
    mt "У нее что, совсем мозгов нет?!"
    mt "Как же она меня БЕСИТ!"
    mt "!!!"
    imgd 16460
    mt "Что же теперь делать?!"
    mt "Чего ожидать от этого никчемного профессионала?!"
    mt "В любом случае, нужно быть аккуратнее с мерзавцем Фредом!"
    mt "Он обязательно захочет воспользоваться этой информацией против меня!"
    mt "Я должна быть на шаг впереди него!"
    music Stealth_Groover
    imgd 16473
    mt "Ведь я не только самая красивая и богатая женщина в этом городе..."
    mt "Я еще и самая умная!"
    mt "Что бы там этом мерзавец не задумал..."
    mt "У него не хватит мозгов обыграть МЕНЯ, саму Миссис Монику Бакфетт!"
    return

# Моника при клике на Фреда после его визита к Юлии в квартиру, мысли
label ep216_dialogues4_fred_6:
    # не рендерить!!
    mt "Гребаный мерзавец Фред!"
    mt "Ничтожный жалкий человечишко!"
    mt "Не хочу с ним разговаривать!!!"
    return

# при условии, что у Моники отношения с Юлией и у Юлии максимальный уровень (т.е. с ней пройдены все сцены в квартире)
# h-сцена с Юлией в офисе
# рабочий кабинет Моники, день
label ep216_dialogues4_fred_7:
    # Моника на рабочем месте, Юлия за своим столом
    # Моника устало
    music Stealth_Groover
    imgfl 22008
    w
    imgf 32430
    mt "Что-то у меня разболелась голова."
    mt "..."
    mt "Моника, ты совсем себя не жалеешь..."
    mt "Постоянно в заботах и в работе..."
    mt "Совсем не бережешь свои нервы."
    imgd 32431
    mt "Как же непросто быть боссом."
    mt "Я единственный умный человек в этом никчемном отделе."
    mt "Вся работа держится на мне одной!"
    mt "И эти все глупые и бесполезные людишки меня утомляют."
    mt "..."
    mt "Мне нужно прилечь и отдохнуть немного..."
    # Моника встает и идет в комнату отдыха
    # ложится на диван и прикрывает глаза
    fadeblack 1.5
    music Groove2_85
    imgfl 32432
    w
    sound highheels_short_walk
    imgf 32433
    w
    music2 drkanje5
    imgd 32434
    w
    imgd 32435
    w
    music2 stop
    imgf 32436
    mt "Я полежу несколько минут..."
    mt "Отдохну..."
    mt "Как же хорошо..."
    mt "Никого не видеть и ни о чем не думать..."
    imgd 32437
    mt "Расслабься немного, Моника..."
    mt "Ты это заслужила..."
    # некоторое время спустя
    # Моника открывает глаза - перед ней голая попа Юлии
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 32438
    w
    music stop
    sound plastinka1b
    img 32439 hpunch
    w
    # у Моники шок
    music Pyro_Flow
    imgd 32440
    mt "!!!"
    mt "!!!!!"
    mt "Какого черта?!"
    mt "?!?!?!"
    # Юлия смотрит на Монику из-за плеча
    music Groove2_85
    imgf 32441
    julia "Миссис Бакфетт, вы такая соблазнительная..."
    julia "Я не смогла удержаться!"
    julia "И тоже решила немного расслабиться вместе с Вами."
    julia "Тем более..."
    imgd 32443
    julia "Вам ведь так понравилось в прошлый раз целовать мою попу..."
    #
    $ notif(_("Моника лизала попу Юлии в душе."))
    #
    imgd 32442
    m "Мне?!"
    m "!!!"
    julia "Да..."
    julia "Миссис Бакфетт, а почему Вы так смотрите на меня?"
    # Юлия расстроенно, убирает свою попу в сторону и начинает канючить
    sound vjuh3
    imgf 32444
    julia "Разве это неправда?"
    julia "Вам не нравится целовать мою попу?"
    music Power_Bots_Loop
    img 32445 vpunch
    mt "Твою мать!"
    mt "Опять она за свое!!!"
    mt "!!!"
    music Groove2_85
    imgd 32444
    julia "Если это так, то и меня Вам не нравится целовать."
    julia "Значит, я все это время заблуждалась и наши чувства не искренние..."
    music Power_Bots_Loop
    imgd 32445
    mt "АААААА!"
    mt "!!!"
    music Hidden_Agenda
    mt "Так, спокойно!"
    mt "Моника, думай про свою цель: получить свободу и закончить этот кошмар."
    mt "Ты не должна дать ей повод усомниться в своих чувствах."
    imgf 32446
    m "..."
    m "Конечно, мне понравилось целовать твою попу, милая."
    m "Как может быть иначе? Ведь ты мне очень нравишься..."
    m "И не просто нравишься. Я испытываю к тебе глубокие чувства."
    imgd 30692
    mt "Глубокое чувство отвращения!"
    imgf 32447
    julia "Правда, Миссис Бакфетт?!"
    m "Конечно, милая..."
    # Юлия радостная, снова нависает своей голой попой над лицом Моники
    sound Jump2
    imgd 32448
    w
    # Моника смотрит на попу Юлии
    music Pyro_Flow
    imgf 32449
    mt "Она хочет, чтобы я..."
    mt "О, Боже!"
    mt "Как же это омерзительно! Фу!"
    mt "!!!"
    menu:
        "Отказать Юлии!":
            imgd 32450
            mt "Нет!"
            mt "Я не собираюсь заниматься этими извращениями!"
            mt "С чего это она решила, что я должна выполнять ее прихоти?!"
            music Stealth_Groover
            imgf 32451
            m "Юлия! Не сейчас!"
            m "У меня очень много дел!"
            m "И еще..."
            m "Еще у меня жутко болит голова!"
            m "Давай, мы с тобой позже вернемся к этому вопросу!"
            # Юлия обижена, встает и поправляет свое платье
            sound vjuh3
            imgd 32452
            julia "Да, Миссис Бакфетт..."
            julia "Как скажете."
            # Моника садится на диван
            sound highheels_short_walk
            imgf 32453
            w
            imgd 32454
            mt "Никчемная глупая Юлия!!!"
            mt "!!!"
            $ workingOfficeCabinet2MonicaSuffix = 2
            call change_scene("working_office_cabinet2", "Fade_long") from _rcall_change_scene_183
            return False
        "Целовать попу Юлии.":
            $ monicaJuliaFredVisit2 = True # Моника делала ассликинг Юлии в комнате отдыха
            pass
    # Юлия смотрит на Монику и улыбается
    # Моника смотрит на ее попу с отвращением
    $ questHelp("julia_55", True)
    imgd 32450
    mt "Черт!"
    mt "Почему Я, ее Босс, должна выполнять ее прихоти?!"
    mt "Прямо здесь! В своем кабинете?!"
    mt "Не могу поверить, что я собираюсь делать ЭТО!"
    mt "Какое грязное извращенство!!! Фууу!!!"
    mt "!!!"
    music Groove2_85
    imgd 32455
    m "Юлия, а если кто-то из сотрудников зайдет?"
    julia "Мы же в комнате отдыха, Миссис Бакфетт..."
    julia "Я успею встать и поправить платье."
    julia "Никто ничего не успеет увидеть..."
    mt "!!!"
    # Моника приближает лицо к ее попе и начинает лизать
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Loved_Up
    imgfl 32457
    w
    imgf 32458
    w


    imgd 32456
    w
    imgf 32461
    w


    $ localSoundVolume = 1.0
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking2_1 = Movie(play="video/v_Monica_Julia_Licking2_1.mkv", fps=30)
    show videov_Monica_Julia_Licking2_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgd 32460
    julia "Ооооо!!!"
    julia "Как хорошо!!!"
    m "Милая... Нас могут услышать."
    m "Постарайся потише."
    imgf 32459
    julia "Да-да..."


    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking2_2 = Movie(play="video/v_Monica_Julia_Licking2_2.mkv", fps=30)
    show videov_Monica_Julia_Licking2_2
    with fade
    julia "Я постараюсь."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking2_3 = Movie(play="video/v_Monica_Julia_Licking2_3.mkv", fps=30)
    show videov_Monica_Julia_Licking2_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Моника снова принимается за ее попу
    imgd 32462
    w
    imgf 32463
    w
    sound lick3
    imgd 32464
    julia "Мммммм..."
    sound lick3
    imgd 32463
    w
    sound lick3
    imgd 32464
    w
    sound lick3
    imgd 32463
    w
    sound lick3
    imgd 32464
    w
    sound lick3
    imgd 32463
    w
    sound lick3
    imgd 32464
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking2_4 = Movie(play="video/v_Monica_Julia_Licking2_4.mkv", fps=30)
    show videov_Monica_Julia_Licking2_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    sound2 highheels_short_walk
    pause 2.0
    music Power_Bots_Loop
    # звук открывающей двери, шаги
    # Моника резко отстраняется от Юлии
    img 32465 hpunch
    m "Дьявол!"
    m "!!!"
    m "!!!!!"
    # Юлия вскакивает с дивана и поправляет платье
    # Моника садится на диван и в этот момент заходит серая мышка в очках
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    imgfl 32466
    w
    imgf 32467
    w1 "Ой, М-миссис Бакфетт..."
    w1 "Я Вам не помешала?"
    music Stealth_Groover
    if monicaBitch == True:
        # Моника орет на нее
        imgd 32468
        m "ПОМЕШАЛА!!!"
        m "!!!"
        m "И вообще!"
    m "Тебя что, не учили стучаться?!"
    m "!!!"
    imgd 32469
    w1 "Я... Просто... Я..." # испуганно
    w1 "Хотела показать Вам свои отчеты..."
    m "Позже! Мне некогда сейчас!"
    w1 "Д-да конечно..."
    m "ИДИ ОТСЮДА!!!"
    # серая мышка испуганно выбегает
    # Моника злая
    fadeblack
    sound highheels_run1
    sound2 snd_door_close1
    pause 1.5
    music Groove2_85
    imgfl 32470
    m "Юлия!"
    m "Еще немного и она увидела бы нас!"
    julia "Ну чего Вы так расстраиваетесь, Миссис Бакфетт?"
    julia "Она ведь ничего не увидела!"
    julia "К тому же, я бы очень хотела, чтобы однажды мы сделали каминг аут и рассказали всем о наших чувствах!"
    music Pyro_Flow
    imgf 32471
    mt "ЧТО?!"
    mt "Я даже не хочу думать о том, какие сплетни поползли бы по отделу!!!"
    mt "А потом и по всему городу!"
    mt "И в заголовках газет!"
    mt "Моника Бакфетт и ее помощница состоят в интимной связи!"
    imgd 32472
    mt "Моника Бакфетт лижет зад своей подчиненной прямо на рабочем месте!"
    mt "Успешная бизнес леди и девушка с трущоб. Их история любви!"
    mt "Ужас!!!"
    mt "!!!"
    # Юлия тем временем уже задрала платье и села на диван на колени, игриво зовет Монику
    sound Jump2
    img 32473 vpunch
    julia "Миссис Бакфетт, моя попа уже ждет Вашего внимания..."
    julia "Ей так нравится Ваш язычок!#it"
    mt "!!!"
    menu:
        "Целовать попу Юлии.":
            pass
    imgd 32474
    mt "Твою мать!!! Достала!!!"
    mt "!!!"
    mt "Просто нужно быстрее закончить с этим!"
    mt "И тогда она, наконец, отстанет от меня!"
    mt "Как же она меня бесит!!!"
    mt "!!!"
    # Моника натягивает улыбку
    music Hidden_Agenda
    imgd 32475
    m "Да, милая, конечно..."
    # Моника наклоняется к попе Юлии и целует ее
    # начинает лизать
    fadeblack 1.5
    music Loved_Up
    imgfl 32476
    julia "Ааааа..."

    $ localSoundVolume = 1.0
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking3_1 = Movie(play="video/v_Monica_Julia_Licking3_1.mkv", fps=30)
    show videov_Monica_Julia_Licking3_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32477
    julia "Еще!!"
    imgd 32478
    julia "Ооо, даааа!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking3_2 = Movie(play="video/v_Monica_Julia_Licking3_2.mkv", fps=30)
    show videov_Monica_Julia_Licking3_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32479
    julia "Еще чуть-чуть, Миссиииис Бакфеееетт!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking3_3 = Movie(play="video/v_Monica_Julia_Licking3_3.mkv", fps=30)
    show videov_Monica_Julia_Licking3_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Loved_up2
    imgf 32480
    w
    imgd 32481
    w
    sound lick3
    img 32482
    w
    sound lick3
    imgd 32481
    w
    sound lick3
    imgd 32482
    w
    sound lick3
    imgd 32481
    w
    sound lick3
    imgd 32482
    w
    sound lick3
    imgd 32481
    w
    sound lick3
    imgd 32482
    julia "Я сейчас коооончуууу!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking3_4 = Movie(play="video/v_Monica_Julia_Licking3_4.mkv", fps=30)
    show videov_Monica_Julia_Licking3_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.666666666666667) + " loop 0.0>Sounds/v_Monica_Julia_Licking2_1.ogg"
    scene black
    image videov_Monica_Julia_Licking3_5 = Movie(play="video/v_Monica_Julia_Licking3_5.mkv", fps=30)
    show videov_Monica_Julia_Licking3_5
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Юлия прижимает ладонь к губам
    sound lick3
    imgf 32483
    w
    img 32484
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan11
    julia "МММ!"
    julia "МММММ!!!"
    julia "ММММММММ!!!!"
    julia "!!!"
    # кончает
    # затемнение
    # Моника отстраняется и пока Юлия сидит балдеет, вытирает губы недовольно
    fadeblack 2.0
    music Groove2_85
    imgfl 32485
    w
    imgf 32486
    julia "О, Миссис Бакфетт!"
    julia "У Вас с каждым разом получается все лучше и лучше!"
    imgd 32487
    mt "Потрясающе!"
    mt "Поздравляю, Моника."
    mt "Тебе стали делать подобные комплименты!"
    m "Милая, я рада, что тебе понравилось."
    # затемнение, звук каблуков
    # Юлия возвращается на свое рабочее место
    # Моника злая сидит на диване
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Pyro_Flow
    imgfl 22386
    mt "Не могу поверить в это!"
    mt "Эта бывшая гувернантка манипулирует МНОЮ, своим БОССОМ!!!"
    mt "Она делает все для того, чтобы я выполняла ее прихоти!!!"
    mt "!!!"
    imgf 22387
    mt "Я больше не должна допускать подобных глупостей!"
    mt "Все-таки Я здесь начальник!"
    mt "И командую здесь только Я!"
    mt "!!!"
    $ ep216_dialogues4_fred_7_last_day = day
    $ add_char_progress("Julia", 15, "julia_relations_progress_scene6")
    $ workingOfficeCabinet2MonicaSuffix = 2
    call change_scene("working_office_cabinet2", "Fade_long") from _rcall_change_scene_184
    return
