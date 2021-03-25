default melanieVictoriaMonicaTable1 = False  # Моника осудила Мелани в гостях у Виктории, воткнула в нее розу
default melanieVictoriaMonicaTable2 = False  # Моника попыталась оправдать Мелани перед Викторией

#call ep216_dialogues5_victoria_1() # офис, кабинет Моники, разговор с Юлией
#call ep216_dialogues5_victoria_2() # Моника возле дома Виктории, перед встречей, глазик
#call ep216_dialogues5_victoria_4() # сцена в апартаментах Виктории
#call ep216_dialogues5_victoria_5() # Моника вышла от Виктории, если она пыталась оправдать Мелани, глазик
#call ep216_dialogues5_victoria_6() # Моника и Мелани вышли от Виктории, если Моника осудила Мелани
#call ep216_dialogues5_victoria_7() # при клике на Мелани после сцены у Виктории дома
#call ep216_dialogues5_victoria_8() # мысли, если Моника пытается войти в офис Дика НЕ в одежде шлюхи

# при условии, что Мелани с Моникой уже были у Дика с телефоном Виктории
# офис, кабинет Моники
label ep216_dialogues5_victoria_1:
    # Моника заходит в свой кабинет, садится за стол
    # к ней подходит Юлия
    fadeblack 2.0
    music Groove2_85
    imgfl 30586
    julia "Миссис Бакфетт..."
    # если у Моники отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях."))
        #
        #music Pyro_Flow
        imgf 30587
        mt "Нет, только не это!"
        mt "Снова этой дурочке от меня что-то нужно!"
        mt "Сколько уже можно?!"
        mt "!!!"
        imgd 30588
        mt "Так, Моника, спокойно."
        mt "Помни о том, что ты с помощью этой никчемной Юлии обретешь свободу!"
        mt "И с каждым днем твоя цель все ближе!"
        music Hidden_Agenda
        imgf 30585
        m "Да, милая. Ты что-то хотела?"
        #
    else:
        # если у Моники нет отношений с Юлией
        music Stealth_Groover
        imgf 20369
        mt "Чего она опять ко мне лезет?!"
        mt "Хочет пожаловаться, что у нее много работы?"
        mt "Никчемной, бесполезной и никому не нужной работы."
        mt "Какая же эта бывшая гувернантка жалкая!"
        #music Groove2_85
        imgd 30585
        m "Что?"
        #
    fadeblack
    sound highheels_run1
    pause 1.5
    music Groove2_85
    imgf 30627
    julia "Звонила Мисс Виктория..."
    julia "Просила передать Вам, что ждет Вас у себя."
    img 40265 vpunch
    m "!!!"
    imgd 40266
    julia "И еще попросила сказать Вам, что Мелани уже у нее..."
    # у Моники шок
    music stop
    sound plastinka1b
    img 40267 vpunch
    m "!!!!!"
    mt "Твою мать!!!"
    # Юлия продолжает стоять рядом со столом Моники и умиляться Виктории
    music Groove2_85
    imgf 40268
    julia "Ой, вам так повезло, Миссис Бакфетт, что Мисс Виктория Ваша подружка!"
    julia "Я когда-нибудь тоже хочу пойти в гости к ней!"
    julia "Она мне так нравится!"
    julia "Такая добрая и милая девушка!"
    # Моника зло смотрит на Юлию
    music Pyro_Flow
    img 40269
    mt "Нашла добрую и милую девушку!"
    mt "Дура!!!"
    mt "!!!"
    # если у Моники отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях."))
        #
        # притворно улыбается
        music Hidden_Agenda
        imgf 40270
        m "Да, милая. Виктория очень..."
        m "Кхм..."
        m "Очень милая девушка."
        m "Я рада, что ты с ней подружилась..."
        # Юлия игриво
    #    music Groove2_85
        imgd 40271
        julia "А Вы возьмете меня с собой в гости к ней, Миссис Бакфетт?"
        m "Сейчас?"
        julia "Да! Ну пожалуйста, Миссис Бакфетт!"
        imgf 30634
        m "Нет, милая. Не сегодня. Как-нибудь в следующий раз..."
        # Юлия радостно
        imgd 40272
        julia "Правда?!"
        julia "Обещаете?!"
        # Моника сквозь зубы
        imgd 40273
        m "Конечно, милая."
        # Юлия довольно чмокает Монику в губы и уходит на свое рабочее место
        fadeblack 1.5
        music Loved_up
        imgfl 40274
        sound kiss2
        w
        imgf 40275
        sound highheels_short_walk
        w
    #    music Pyro_Flow
        imgd 40276
    #    mt "ААААА!!!"
        mt "БЕСИТ!!!"
    #    mt "!!!"
        #
    else:
        # если у Моники нет отношений с Юлией
        # Моника рявкает на нее раздраженно
        music Stealth_Groover
        imgd 40277
        m "Я сейчас поеду к Мисс Виктории."
        m "А ты иди работай!"
        m "Хватит болтать о всяких глупостях!"
        # Юлия испуганно
        imgd 40278
        julia "Д-да, Миссис Бакфетт..."
        imgf 22338
        sound highheels_short_walk
        w
        # Юлия уходит на свое рабочее место
        #
    # Моника в панике
    fadeblack 1.5
    music Master_Disorder
    imgfl 40280
    mt "Эта белобрысая стерва будет мстить за наш разговор с Диком!"
    mt "!!!"
    mt "Что она задумала на этот раз?!"
    mt "?!?!?!"
    imgf 30587
    mt "Может, просто не ехать к ней?"
    mt "Скажу, что дурочка Юлия ничего мне не передавала..."
    mt "..."
    imgd 40279
    mt "Но ведь Мелани уже там!"
    mt "Если я не приеду, сучка Виктория разозлится еще больше!"
    mt "И тогда я даже боюсь представить, какие будут последствия!"
    mt "Дьявол!"
#    $ log1 = _("Поехать к Виктории.")
    return

# Моника возле дома Виктории, глазик
label ep216_dialogues5_victoria_2:
    # не рендерить!!
    mt "Я даже думать боюсь о том, какой девичник приготовила эта белобрысая дрянь!"
    mt "Настанет тот день, Моника, когда ты избавишься от сучки Виктории!"
    mt "Это будет один из самых счастливых дней!"
    mt "Не могу дождаться этого момента!"
    mt "А пока я вынуждена терпеть ее присутствие в своей жизни..."
    mt "Иначе меня ждет кое-что похуже... О чем я боюсь даже думать..."
    return

# Моника в квартире Виктории, мысли, когда осматривается
#label ep216_dialogues5_victoria_3:
#    # не рендерить!!
#    mt "Это что, и есть логово белобрысой дьяволицы?!"
#    mt "Это что, шутка?!"
#    mt "Мягкие игрушки... Детские рисунки... Дик поэтому считает ее невинным ангелом?"
#    mt "Прямо сама невинность!"
#    mt "Меня тошнит от изобилия розового!"
#    mt "Фи! Какая безвкусица!"
#    return

# Моника заходит в квартиру Виктории
label ep216_dialogues5_victoria_4:
    # Виктория встречает Монику в холле, мило улыбается ей
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Минуту спустя...")) from _rcall_textonblack_72
    scene black_screen
    with Dissolve(1)
    pause 2.0
    sound2 snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 40514
    victoria "Ой, подружка Моника пришла!"
    victoria "Я так рада тебя видеть, подружка!"
    imgf 40515
    victoria "Я знаю, тебе очень хотелось попасть ко мне в апартаменты."
    victoria "И ты очень рада, что я тебя, наконец-то, пригласила."
    # Моника сквозь зубы
    music Villainous_Treachery
    imgd 40516
    m "Да... очень..."
    music Groove2_85
    imgf 40517
    victoria "Что подружка делает, чтобы показать, как рада она меня видеть?"
    # Виктория показывает на свою щечку, Моника недовольно на нее смотрит
    m "..."
    menu:
        "Поцеловать Викторию.":
            pass
    # Моника наклоняется и чмокает Викторию в щеку, Виктория довольно хихикает
    fadeblack 1.5
    music Loved_up
    imgfl 40518
    sound kiss1
    w
    imgf 40519
    sound snd_woman_laugh3
    victoria "Ой, подружка, какая же ты милая!"
    victoria "Тебе нравится целовать меня, признайся. Хи-хи!"
    # Моника подозрительно смотрит на Викторию
    music Villainous_Treachery
    imgd 40520
    mt "Лучше не спорить с этой сучкой..."
    mt "Еще не время..."
    mt "И вообще, какая-то она слишком довольная..."
    mt "А где Мелани?"
    mt "???"
    music Groove2_85
    imgf 40521
    m "Да... Мне нравится тебя целовать... Подружка..."
    imgd 40522
    victoria "Я знаю, подружка Моника."
    victoria "Ты ведь хорошая подружка, ты меня не расстраиваешь своим поведением."
    m "..."
    victoria "Ну что же ты стоишь возле двери? Проходи в гостиную!"
    # затемнение, звук каблуков
    # проходят через кухню
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 40523
    victoria "Проходи, подружка Моника."
    imgd 40524
    mt "Неплохо устроилась эта белобрысая сикалявка!"
    mt "Наверное это Дик за все платит!"
    # смена кадра на гостиную
    # Моника заходит в гостиную, не сразу обращает внимание на стол
#    fadeblack
    sound highheels_short_walk
#    pause 2.0
#    music Groove2_85
    imgf 40525
    victoria "Присаживайся за стол, подружка."
    victoria "Я хочу выпить с тобой вина..."
    # Виктория садится за стол, внутри которого голая Мелани
    # Моника обращает внимание на стол, она в шоке
    music stop
    sound plastinka1b
    img 40526 hpunch
    mt "!!!"
    music Villainous_Treachery
    mt "!!!!!"
    img 40527
    mt "О БОГИ!!!"
    mt "Мелани!!!"
    imgd 40528
    mt "Что?! Что этот дьявол в юбке с тобой сделал?!"
    imgd 40703
    mt "Что происходит?!"
    mt "?!?!?!"
    # Виктория самодовольно смотрит на реакцию Моники
    fadeblack 1.5
    music Groove2_85
    imgf 40529
    victoria "Ах да, подружка Моника, я совсем забыла сказать тебе..."
    victoria "Подружка Мелани пришла немного раньше тебя..."
    victoria "И мы с ней поиграли немного без тебя..."
    imgd 40530
    victoria "Надеюсь что ты не расстроишься из-за того, что не смогла поучавствовать?"
    victoria "Я ведь знаю ты так любишь наши маленькие дружеские игры!"
    # Моника в ступоре продолжает смотреть на Мелани
    music Master_Disorder
    #music Pyro_Flow
    img 40531
    mt "Если она так с Мелани..."
    mt "Что?.. Что эта дрянь приготовила для меня?!"
    mt "!!!"
#    music Groove2_85
    imgd 40532
    m "Н-немного?"
    victoria "Да, совсем чуть-чуть. Ты ведь не против?"
    victoria "Подружка Моника, так ты не будешь на меня обижаться, что я не подождала тебя?"
    m "..."
    # Виктория снова смотрит на Монику и протягивает ей бокал с вином
    # Моника берет его в руки
    fadeblack 1.5
    music Master_Disorder
    imgfl 40533
    w
    imgf 40534
    w
    imgd 40535
    mt "Я не хочу ничего пробовать из рук этой твари..."
    mt "Нужно просто сделать вид, что я пью..."
    imgf 40536
    victoria "Я не слышу ответа, подружка..."
    victoria "Скажи мне, я хочу услышать."
    # Моника переводит взгляд на Викторию
    m "..."
    menu:
        "Я не против.":
            pass
    # Моника смотрит на Викторию с отвращением
#    music Pyro_Flow
    imgd 40538
    mt "Я хочу, чтобы она отстала от меня!"
    mt "Я хочу уйти отсюда! Поскорее!"
    imgd 40537
    mt "Мерзкая лицемерная тварь!"
    mt "Извращенка, которая прикидывается невинной девочкой!"
    mt "!!!"
#    music Groove2_85
    fadeblack 1.5
    music Groove2_85
    imgf 40539
    m "Я не обижаюсь... подружка..."
    m "Я не против, что вы... поиграли без меня..."
    # Виктория довольно хихикает, потом указывает на стол
    sound snd_woman_laugh3
    imgd 40540
    victoria "Подружка Моника хорошая."
    victoria "Присаживайся."
    # Моника садится на стул возле столика
    # Виктория садится на диван, смотрит вниз на Мелани, раздвигает ноги
    # Мелани сама, без приказа, начинает ей лизать
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 40541
    w
#    sound Jump1
    imgf 40706
    w
    imgd 40542
    victoria "Смотри, теперь я разрешаю подружке Мелани ласкать меня, не спрашивая разрешения об этом..."
    imgf 40704
    w
    sound Jump1
    imgd 40705
    sound snd_woman_laugh3
    victoria "Хи-хи-хи!"
    imgf 40543
    victoria "Она призналась мне, что ей это очень нравится."
    fadeblack 1.5
    music Loved_up

    $ localSoundVolume = 1.0
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Melanie_Licking1_1 = Movie(play="video/v_VictoriaHome_Melanie_Licking1_1.mkv", fps=25)
    show videov_VictoriaHome_Melanie_Licking1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 40544
    w
    sound lick3
    imgd 40545
    w
    sound lick3
    imgd 40544
    w
    sound lick3
    imgd 40545
    w
    sound lick3
    imgd 40544
    w
    sound lick3
    imgd 40545
    # Моника в шоке смотрит на Мелани
    w
    fadeblack 1.5
    music Villainous_Treachery
    img 40546 vpunch
    mt "Боже! Какой кошмар!"
    mt "Что она с ней делала до моего прихода?!"
    mt "!!!"
    # Моника приближает бокал к губам, но не пьет его, потом просто держит в руке
    music Groove2_85
    imgf 40547
    victoria "Как тебе мои апартаменты, подружка Моника?"
#    music Pyro_Flow
    img 40548
    mt "Отвратительно! Безвкусица!"
    mt "!!!"
    music Hidden_Agenda
    imgf 40549
    m "Здесь очень красиво... Подружка..."
    m "Я бы сказала, уютно..."
    music Groove2_85
    imgd 40550
    victoria "Тебе правда нравится?"
    m "Да..."
    victoria "Ты хотела бы жить здесь?"
    m "Да..."
    imgf 40551
    victoria "Вместо меня?" # Виктория подозрительно
    music stop
    sound plastinka1b
    img 40552 hpunch
    m "Нннннет..."
    music Groove2_85
    imgd 40553
    sound snd_woman_laugh3
    victoria "Хи-хи-хи!"
    victoria "Если знать, как правильно вести себя с Мистером Диком..."
    victoria "То он становится очень внимательным и щедрым."
    victoria "Подружка Моника, ты расстроена, что у тебя с Мистером Диком ничего не получилось?"
    imgd 40554
    m "..."
    imgf 40555
    victoria "Можешь не отвечать. Я знаю, что ты мне по-дружески завидуешь. Хи-хи-хи!"
    victoria "Кстати, о дружбе и о Мистере Дике..."
    music Master_Disorder
    img 40556
    mt "Черт!"
    mt "!!!"
    music Groove2_85
    imgf 40557
    victoria "Я считаю, что подружка Мелани поступила не совсем по-дружески..."
    victoria "Когда попыталась показать Мистеру Дику то видео на моем телефоне..."
    victoria "Но я все-же считаю, что подружка Мелани - хорошая подружка."
    victoria "Она просто ошиблась."
    victoria "Ты согласна со мной, подружка Моника, что Мелани ошиблась?"
    # Моника растерянно молчит
    music Master_Disorder
    imgd 40558
    m "..."
    # Виктория наигранно
    music Groove2_85
    imgf 40559
    sound lick3
    pause 1.0
    sound lick3
    pause 1.0
    sound lick3

    $ localSoundVolume = 0.75
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Melanie_Licking1_2 = Movie(play="video/v_VictoriaHome_Melanie_Licking1_2.mkv", fps=25)
    show videov_VictoriaHome_Melanie_Licking1_2
    with fade
    victoria "Ой, подружка Моника, это так невежливо с моей стороны!"
    victoria "Я забыла тебя спросить, не хочешь ли ты присоединиться к подружке Мелани?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 40560
    m "Присо... Что?!"
    # кадр на Мелани
    music stop
    sound plastinka1b
    img 40561 hpunch
    m "!!!"
    m "О, нет-нет!"
    m "Спасибо, мне тут удобно!"
    # Виктория ехидно улыбается и выжидательно смотрит на Монику
    music Groove2_85
    imgf 40562
    victoria "Ну так что ты скажешь, подружка Моника?"
    victoria "Мелани совершила ошибку? Или ты считаешь иначе?"
    # Моника испуганно смотрит на Мелани
    music Master_Disorder
    imgd 40563
    m "..."
    menu:
        "Сказать, что Мелани совершила ошибку.":
            pass
    music Villainous_Treachery
    imgd 40564
    mt "Дьявол!"
    mt "Ведь я была вместе с Мелани!"
    mt "Какой кошмар!"
    imgd 40565
    mt "Что же теперь ожидает меня?!"
    mt "!!!"
    mt "Лучше будет, если я не буду злить эту мерзкую дрянь Викторию!"
    fadeblack 1.5
    music Master_Disorder
    imgd 40566
    m "Я считаю..."
    m "Я считаю, что Мелани ошиблась..."
    # Виктория самодовольно улыбается, поднимает бокал и протягивает его Монике, чтобы чокнуться
    # Моника тоже тянет бокал
    music Groove2_85
    sound snd_glass_table
    imgf 40567
    victoria "За женскую дружбу, подружка Моника!"
    # чокаются
    victoria "Я уверена, что подружка Мелани осознает свою ошибку..."
    victoria "И больше она не будет огорчать меня..."
    imgd 40568
    m "Д-да..."
    # Виктория опускает взгляд на Мелани, та все продолжает лизать
    imgf 40569
    victoria "Жаль, что она не может к нам присоединиться..."

    $ localSoundVolume = 1.0
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Melanie_Licking1_1 = Movie(play="video/v_VictoriaHome_Melanie_Licking1_1.mkv", fps=25)
    show videov_VictoriaHome_Melanie_Licking1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 40570
    m "..."
    imgf 40571
    victoria "Кстати, подружка Мелани настолько хочет снова стать хорошей..."
    victoria "Что попросила у меня разрешения..."
    victoria "Быть допущенной не только до моей киски, но и до моей попы."
    #
    $ notif(_("Виктория говорила, что Мелани допущена только до ее киски, а Моника допущена только до ее попы."))
    #
    imgd 40572
    victoria "Но ведь моя попа только для тебя, подружка Моника..."
    victoria "И я думаю, что же мне делать."
    victoria "Если я допущу подружку Мелани не только до моей киски, но и до попы..."
    imgf 40573
    victoria "То тебе, подружка Моника, ничего не останется..."
    victoria "А ты так любишь мою попу..."
    victoria "Ведь это так, подружка?"
    imgd 40574
    m "..."
    menu:
        "Да, это так.":
            pass
    imgf 40575
    m "Да..."
    victoria "Что 'да'? Скажи мне. Я хочу это услышать от тебя."
    music Power_Bots_Loop
    img 40576
    mt "Гребаная сучка!"
    mt "Ненавижу!!!"
    mt "!!!"
    music Groove2_85
    imgf 40577
    m "Я... Мне нравится твоя... Твоя попа..."
    # Виктория хихикает довольно
    sound snd_woman_laugh3
    imgd 40578
    victoria "Хи-хи!"
    victoria "Да, я знаю, подружка..."
    victoria "Ты очень любишь мою попу."
    victoria "И ты специально опаздываешь с сертификатами, чтобы почаще вылизывать прощение у меня."
    imgd 40579
    victoria "Но, если я допущу подружку Мелани до моей попы..."
    victoria "Тогда ты не сможешь больше быть моей подружкой."

    $ localSoundVolume = 0.75
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Melanie_Licking1_2 = Movie(play="video/v_VictoriaHome_Melanie_Licking1_2.mkv", fps=25)
    show videov_VictoriaHome_Melanie_Licking1_2
    with fade
    victoria "Тебе ничего не останется, чем подтверждать нашу дружбу."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Моника с непониманием смотрит на нее
    music Villainous_Treachery
    imgd 40580
    mt "Что она хочет этим сказать?!"
    mt "Чего эта дрянь добивается?!"
    music Groove2_85
    imgd 40581
    victoria "Скажи мне, подружка, допустить ли мне подружку Мелани к моей попе?"
    victoria "Или она не настолько хорошая подружка, чтобы заслуживать такую привилегию?"
    # Моника смотрит на нее пристально
    music Villainous_Treachery
    imgd 40582
    mt "Вот черт!"
    mt "Эта белобрысая тварь пытается настроить Мелани против меня!"
    mt "Она хочет сделать так, чтобы мы больше не действовали сообща!"
    mt "Мерзкая, грязная извращенка!"
    mt "!!!"
    music Groove2_85
    imgd 40583
    victoria "Ну, что скажешь, подружка Моника?"
    victoria "Я жду твоего ответа."
    # Моника в растерянности
    imgf 40584
    m "..."
    menu:
        "Сказать, что Мелани не настолько хорошая подружка.":
            pass
    music Pyro_Flow
    imgd 40585
    mt "Если я ей скажу, чтобы она допустила Мелани до своего мерзкого тощего зада..."
    mt "То я рискую стать плохой подружкой."
    mt "А это значит... Дьявол! Не хочу даже представлять последствия!"
    mt "!!!"
    imgd 40586
    mt "Твою мать! Моника, эта мелкая сучка вынуждает сказать это!"
    mt "Думаю, Мелани поймет меня..."
    mt "Нужно будет обязательно поговорить с ней об этом. Позже."
    music Groove2_85
    imgf 40587
    m "Я думаю, что..."
    m "Что подружка Мелани не настолько хорошая."
    m "И что она не может быть допущена до твоей попы... Подружка..."
    # Виктория довольно хихикает и смотрит на Мелани
    sound snd_woman_laugh3
    imgd 40588
    victoria "Хорошо, подружка Моника, я прислушаюсь к твоему совету."
    victoria "Хи-хи-хи!"
    victoria "Кстати, забыла спросить тебя..."
    imgd 40589
    victoria "Тебе нравится, как я украсила стол к твоему приходу?"
    victoria "Я старалась для своей хорошей подружки Моники."
    victoria "Эта роза... Мне настолько понравился ее запах, что я даже решила украсить ею стол. Хи-хи!"
    # Моника смотрит на торчащую попу Мелани с цветком
    imgf 40557
    victoria "Тебе нравится, подружка Моника?"
    imgd 40590
    m "Д-да..."
    victoria "Я вижу, что ты тоже хочешь понюхать эту розу."
    victoria "Я разрешаю хорошей подружке Монике взять ее в руку и понюхать."
    music Master_Disorder
    img 40591
    m "Ч-что?.."
    imgd 40592
    victoria "Возьми розу и понюхай ее, подружка. Ты можешь не стесняться и делать то что хочешь."
    # Моника медлит, в недоумении смотрит на розу
    imgd 40593
    m "..."
    menu:
        "Взять розу из попы Мелани.":
            pass
    imgd 40548
    mt "Я что, должна вытащить розу оттуда?!"
    mt "Это... Это просто отвратительно!"
    mt "!!!"
    music Power_Bots_Loop
    imgd 40576
    mt "Что у нее в голове творится?!"
    mt "Как вообще можно додуматься до ТАКОГО?!"
    mt "И Я вынуждена слушать эту гребаную больную извращенку!!!"
    mt "ААА!!!"
    # Моника протягивает руку и вытаскивает розу, подносит ее к своему лицу
    fadeblack 1.5
    music Groove2_85
    imgfl 40594
    w
    imgf 40595
    w
    sound chpok2
    img 40596 vpunch
    w
    imgf 40597
    w
    imgd 40598
    victoria "Тебе нравится ее аромат, подружка Моника?"
    m "Нравится..."
    victoria "Скажи подружка, ты осуждаешь Мелани за ее ошибку?"
    victoria "Ты считаешь, что такая хорошая подружка, как ты, никогда бы не совершила подобное?"
    imgd 40599
    m "Я..."
    music Master_Disorder
    imgd 40600
    mt "Дьявол! Меня слышит Мелани!"
    mt "Мы были там вместе!"
    mt "Что же мне сказать?"
    mt "???"
    imgf 40601
    victoria "Если подружка осуждает Мелани, то она может вернуть розу на место..."
    victoria "Чтобы снова украсить ею стол..."
    imgd 40602
    m "!???!?"
    menu:
        "Осудить Мелани и воткнуть розу обратно. (in Extra version) (disabled)" if game.extra != True:
            pass
        "Осудить Мелани и воткнуть розу обратно." if game.extra == True: # пункт доступен при высокой бичности
            music Pyro_Flow
            imgf 40603
            mt "Да, мы были там вместе с Мелани, но это была ее идея."
            mt "Это ее провал и я не хочу отвечать за него!"
            mt "!!!"
            imgd 40605
            m "Я считаю, что Мелани поступила неправильно."
            imgd 40606
            m "И осуждаю ее."
            call bitch(20, "ep216_dialogues5_victoria_rose") from _rcall_bitch_18
            imgf 40709
            w
            sound chpok2
            img 40708 vpunch
            w
            sound Jump2
            imgd 40707
            w
            imgf 40607
            w
            # чпок, вставляет розу назад (показать Мелани лицо)
            img 40608 hpunch
            melanie "!!!"
            # Виктория довольно
            music Groove2_85
            imgf 40609
            sound snd_woman_laugh3
            victoria "Хи-хи-хи!"
            victoria "Хорошо, подружка Моника."
            mt "Надеюсь, теперь эта сучка Виктория отстанет от меня!"
            imgd 40610
            victoria "Знаешь, подружка, я все-таки переживаю из-за того..."
            victoria "Что ты не успела поиграть с нашей подружкой Мелани."
            victoria "Я тут подумала..."
            victoria "Ты, наверное, хочешь посидеть немного на моем месте?"
            img 40611
            m "На твоем месте?"
            imgd 40612
            victoria "Да. Уверена, подружка Мелани тоже хочет поиграть с тобой..."
            victoria "Ты ведь хочешь этого, подружка Моника?"
            music Master_Disorder
            imgd 40613
            m "..."
            menu:
                "Да, хочу.":
                    pass
            mt "Черт!"
            mt "Если я сейчас откажусь, эта сикалявка разозлиться."
            mt "Лучше не спорить с ней."
            # Моника смотрит на Мелани
            imgd 40614
            mt "Иначе я могу оказаться на месте Мелани..."
            mt "С розой в моей попе..."
            mt "Чтобы стать украшением стола..."
            mt "Кошмар! Нет, я не позволю так себя унижать!"
            music Groove2_85
            mt "!!!"
            imgd 40615
            mt "И вообще!"
            mt "Я ведь просто стараюсь не злить сучку Викторию!"
            mt "Я это делаю не только ради себя..."
            mt "Но и ради Мелани!"
            imgf 40616
            m "Да, я хочу поиграть с подружкой Мелани..."
            victoria "Хи-хи-хи!"
            victoria "Я знала, что ты не сможешь отказаться, подружка."
            # затемнение

########################
            # Моника садится на место Виктории, Виктория стоит рядом (или садится на стул, где была Моника-?)
            # Моника сидит на диване не в раскоряку, а сдвинув ноги
            fadeblack
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            imgfl 40675
            w
            imgf 40676
            victoria "Подружка Моника, нужно раздвинуть ноги и сесть поближе к нашей подружке."
            victoria "Иначе она не сможет дотянуться до твоей киски, чтобы поиграть с ней."
            #music Power_Bots_Loop
            imgd 40677
            mt "Черт!"
            mt "!!!"
            # Моника смотрит на Мелани, немая пауза
            music Master_Disorder
            img 40679
            melanie "!!!"
            melanie "!!!!!"
            imgd 40678
            mt "..."
            imgf 40680
            victoria "Подружка Моника, не заставляй ждать подружку Мелани."
            victoria "Сделай это. Хи-хи-хи!"
            # Моника раздвигает ноги и подставляет свою киску Мелани
            # Мелани делает ликинг, Моника смотрит на нее
            #sound snd_woman_laugh2
            imgd 40721
            w
            imgd 40722
            w
            imgf 40681
            w
            sound Jump1
            imgd 40682
            w
            imgd 40683
            mt "Даже представлять не хочу, что сейчас чувствует Мелани..."
            mt "Это ужасно!"
            mt "..."

            $ localSoundVolume = 1.0

            # если был обнаженный кастинг перед Мелани и мартышкой
            if monicaMelanieCastingLickedPussies == True:
                music Pyro_Flow
#                imgd 40683
                mt "Но если посмотреть на ситуацию с другой стороны..."
                #
                $ notif(_("Моника проходила кастинг перед Мелани и серой мышью."))
                #
                imgd 40684
                mt "Мелани в тот раз поступила так же!"
                mt "Она не терзалась сомнениями, когда эта грязная серая мышь заставила меня лизать..."

                img black_screen
                with diss
                stop music2
                $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                $ renpy.music.set_volume(0.2, 0.5, channel="music")
                play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Monica_Licking1_1.ogg"
                scene black
                image videov_VictoriaHome_Melanie_Monica_Licking1_4 = Movie(play="video/v_VictoriaHome_Melanie_Monica_Licking1_4.mkv", fps=25)
                show videov_VictoriaHome_Melanie_Monica_Licking1_4
                with fade
                wclean
                mt "Лизать Мелани между ног!"
                mt "Я тогда была в не менее унизительном положении, чем сейчас Мелани!"
                mt "Это было отвратительно!"
                mt "!!!"
                wclean
                stop music2
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                if monicaBitch == True:
                    imgd 40685
                    mt "Поэтому теперь это будет моя маленькая месть Мелани за тот поступок!"
                    mt "Ведь тот гребаный кастинг с мартышкой - это была ее инициатива!"
                    mt "!!!"
                else:
                    imgd 40685
                    mt "Хотя Мелани ответила тогда за этот свой поступок..."
                    mt "Знакомством с Маркусом."
                    mt "Страшно представить, что ей пришлось пережить при этом..."
            else:
                music Groove2_85
                imgd 40686
                mt "Но если посмотреть на ситуацию с другой стороны..."

                img black_screen
                with diss
                stop music2
                $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                $ renpy.music.set_volume(0.2, 0.5, channel="music")
                play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Monica_Licking1_1.ogg"
                scene black
                image videov_VictoriaHome_Melanie_Monica_Licking1_4 = Movie(play="video/v_VictoriaHome_Melanie_Monica_Licking1_4.mkv", fps=25)
                show videov_VictoriaHome_Melanie_Monica_Licking1_4
                with fade
                mt "Ведь я делаю это для того, чтобы сучка Виктория наконец отстала от нас!"
                mt "По крайней мере, на сегодня."
                mt "Возможно, после этого она отпустит меня и Мелани."
                wclean
                stop music2
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                imgd 40684
                mt "Мелани должна понять меня."
                mt "Уверена, будь она на моем месте, она поступила бы также."
            # Виктория с довольным видом
            fadeblack
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            imgfl 40687
            victoria "Ну как, подружка Моника, тебе нравится играть с нашей подружкой Мелани?"
            imgf 40688
            m "Да..."
            fadeblack 1.5
            music Loved_up
            #sound lick1
            imgf 40718
            w
            sound lick3
            imgd 40719
            w
            sound lick3
            imgd 40718
            w
            sound lick3
            imgd 40719
            w
            sound lick3
            imgd 40718
            w
            sound lick3
            imgd 40719
            w

            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Monica_Licking1_1.ogg"
            scene black
            image videov_VictoriaHome_Melanie_Monica_Licking1_1 = Movie(play="video/v_VictoriaHome_Melanie_Monica_Licking1_1.mkv", fps=25)
            show videov_VictoriaHome_Melanie_Monica_Licking1_1
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
            play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Monica_Licking1_1.ogg"
            scene black
            image videov_VictoriaHome_Melanie_Monica_Licking1_2 = Movie(play="video/v_VictoriaHome_Melanie_Monica_Licking1_2.mkv", fps=25)
            show videov_VictoriaHome_Melanie_Monica_Licking1_2
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 40688
            sound snd_woman_laugh2
            victoria "Я уверена, что подружке Мелани тоже очень нравится."
            victoria "Хи-хи-хи!"


            imgd 40689
            m "..."
            #sound lick3
            imgf 40720
            w

            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Monica_Licking1_1.ogg"
            scene black
            image videov_VictoriaHome_Melanie_Monica_Licking1_3 = Movie(play="video/v_VictoriaHome_Melanie_Monica_Licking1_3.mkv", fps=25)
            show videov_VictoriaHome_Melanie_Monica_Licking1_3
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            fadeblack 1.5
            music Groove2_85
            imgfl 40690
            victoria "Я знаю, что вы хотели бы еще немного поиграть..."
            victoria "Но на сегодня достаточно, подружки!"
            # Моника отодвигается от Мелани
            # Виктория подходит к попе Мелани и выдергивает розу
            #fadeblack
            sound highheels_short_walk
            imgf 40691
            victoria "Наш девичник закончен и мои подружки могут идти."
            sound chpok2
            img 40692 vpunch
            w
########################
            music stop
            img black_screen
            with Dissolve(2.0)
            call textonblack(t_("5 минут спустя...")) from _rcall_textonblack_73
            img black_screen
            with Dissolve(2.0)
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            # затемнение
            # смена кадра, холл, Виктория провожает Мелани и Монику
            # Мелани подавлена, молчит
            imgfl 40629
            victoria "Я рада, что моим подружкам понравился мой девичник."
            # смотрит на Мелани
            victoria "Ведь это так, подружка Мелани?"
            # Мелани отвечает безразлично
            imgf 40630
            melanie "Да, подружка."
            victoria "Хи-хи-хи!"
            # смотрит на Монику
            imgd 40631
            victoria "Также я рада, что подружка Моника не обижается на то..."
            victoria "Что я немного поиграла с подружкой Мелани, а с ней - нет."
            victoria "Но ты не расстраивайся, подружка Моника..."
            music Master_Disorder
            imgd 40623
            victoria "Мы с тобой еще поиграем..."
            victoria "Не сегодня, но уже совсем скоро, подружка."
            img 40624 vpunch
            m "!!!"
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Виктория ехидно улыбается, Моника испугано смотрит на нее, Мелани выходит
            # затемнение
            $ melanieVictoriaMonicaTable1 = True # Моника осудила Мелани в гостях у Виктории, воткнула в нее розу
            # дается bitchiness

        "Аккуратно положить розу рядом.":
            imgd 40604
            mt "Мелани все слышит."
            mt "Мы были там вместе и я не могу осудить ее, когда она в таком положении!"
            music Groove2_85
            imgf 40617
            m "Я считаю, что Мелани хорошая подружка."
            m "Думаю, ей можно простить небольшую ошибку..."
            m "..."
            call bitch(-20, "ep216_dialogues5_victoria_rose") from _rcall_bitch_19
            imgd 40618
            m "Эта роза стояла неровно, вот так она выглядит гораздо эстетичнее..."
            # Моника кладет розу рядом с Мелани на стол
            imgd 40619
            victoria "Хорошо, подружка Моника..."
            # подозрительно
            victoria "Я тоже решила дать подружке Мелани еще один шанс..."
            imgd 40620
            m "..."
            imgf 40621
            victoria "Наш девичник закончен и мои подружки могут идти."
            victoria "Только..."
            victoria "Подружка Моника, тебе не кажется, что стол будет выглядеть..."
            music Master_Disorder
            victoria "Не очень красиво без такой чудесной вазы под цветок?"
            imgd 40613
            m "Да, кажется..."  #### арт
            imgf 40612
            victoria "Ты разрешишь мне оставить подружку Мелани еще немного?"
            imgd 40613
            m "..."
            menu:
                "Разрешить Виктории оставить Мелани у себя.":
                    pass
            # Моника смотрит на Мелани
            img 40693
            mt "Черт! Черт! Черт!"
            mt "Мне потом нужно будет обязательно поговорить с Мелани!"
            mt "Она должна понять меня!"
            music Groove2_85
            imgd 40615
            mt "Я ведь просто стараюсь не злить сучку Викторию!"
            mt "Я это делаю не только ради себя..."
            mt "Но и ради нее!"
########################
            imgd 40694
            m "Разрешаю..."
            victoria "Хи-хи-хи!"
            victoria "Я знала, подружка Моника, что ты не сможешь отказать мне."
            # Виктория показывает на свою щечку
            imgd 40695
            victoria "Поцелуешь меня на прощание, подружка?"
            victoria "Хорошие подружки целуются не только при встрече."
            imgd 40696
            m "..."
            menu:
                "Поцеловать Викторию.":
                    pass
            # Моника подходит к Виктории, наклоняется и цедует ее в щечку
            fadeblack
            sound highheels_short_walk
            pause 1.5
            music Loved_up
            imgfl 40697
            w
            imgf 40698
            sound kiss1
            victoria "Хи-хи-хи!"

            $ localSoundVolume = 1.0
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Licking1_1.ogg"
            scene black
            image videov_VictoriaHome_Melanie_Licking1_1 = Movie(play="video/v_VictoriaHome_Melanie_Licking1_1.mkv", fps=25)
            show videov_VictoriaHome_Melanie_Licking1_1
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            fadeblack 1.5
            music Groove2_85
            imgf 40699
            victoria "Не забудь поцеловать и нашу подружку Мелани."
            # Моника смотрит на нее вопросительно
            m "Поцеловать подружку Мелани?"
            victoria "Да... Она ведь тоже твоя подружка. Поцелуй ее."
            # Моника в растерянности смотрит на торчащую из стола попу
            imgd 40700
            m "..."
            menu:
                "Поцеловать Мелани.":
                    pass
            # Моника наклоняется над столиком и чмокает попу Мелани
            imgf 40723
            w
            imgd 40701
            sound kiss1
            w

            $ localSoundVolume = 0.7
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/v_VictoriaHome_Melanie_Licking1_1.ogg"
            scene black
            image videov_VictoriaHome_Melanie_Licking1_2 = Movie(play="video/v_VictoriaHome_Melanie_Licking1_2.mkv", fps=25)
            show videov_VictoriaHome_Melanie_Licking1_2
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 40702
            sound snd_woman_laugh3
            victoria "Хи-хи-хи!"

########################

            # затемнение
            # смена кадра, холл, Виктория провожает Монику
            # Виктория ехидно смотрит на нее
            music stop
            img black_screen
            with Dissolve(2.0)
            call textonblack(t_("5 минут спустя...")) from _rcall_textonblack_74
            img black_screen
            with Dissolve(2.0)
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            imgfl 40622
            victoria "Я рада, что моей хорошей подружке Монике понравился мой девичник."
            victoria "И что она не обижается на то, что я поиграла с подружкой Мелани, а с ней - нет."
            imgf 40623
            victoria "Но ты не расстраивайся, подружка Моника..."
            music Master_Disorder
            victoria "Мы с тобой еще поиграем..."
            victoria "Не сегодня, но уже совсем скоро, подружка."
            img 40624 vpunch
            m "!!!"
            # Виктория ехидно улыбается, Моника испугано смотрит на нее
            # затемнение
            $ melanieVictoriaMonicaTable2 = True # Моника попыталась оправдать Мелани перед Викторией
    # Виктория продолжает ехидничать с Моникой
    music Groove2_85
    imgf 40625
    victoria "Кстати, подружка Моника..."
    victoria "Я забыла тебе сказать, что мне нравится твое платье."
    # Моника смотрит на нее удивленно
    imgd 40626
    m "???"
    imgf 40627
    victoria "Я бы хотела дальше подружку Монику видеть в нем в моих апартаментах."
    victoria "Так как здесь приличный район. Хи-хи!"
    victoria "Но в офис Мистера Дика приходи в той забавной одежде."
    victoria "Я бы не хотела, чтобы Мистер Дик видел тебя какой-то другой."
    # Моника злобно на нее смотрит
    imgd 40628
    m "Хорошо... Подружка..."
    m "!!!"
    fadeblack
    sound snd_lift
    pause 2.0
    return

# Моника вышла от Виктории, на улице, глазик
# если она пыталась оправдать Мелани, стоит на улице одна
label ep216_dialogues5_victoria_5:
    # не рендерить!!
    mt "О Боже!"
    mt "Так неудобно получилось с Мелани, но неизвестно, чем бы это закончилось..."
    mt "В конце концов, это ее ошибка!"
    mt "Эта сучка Виктория настоящая извращенка!"
    mt "Притом больная на всю голову!"
    mt "!!!"
    mt "Она заставила меня сказать, что Мелани совершила ошибку..."
    mt "И что она не хорошая подружка!"
    mt "Но ведь я была у Дика вместе с Мелани!!!"
    mt "Я почти уверена, что эта сикалявка просто так мне это не простит!"
    mt "Чего мне теперь ожидать от нее?!"
    mt "Я не хочу, чтобы она втыкала розу в мою... Мою попу!"
    mt "Это! Это мерзко!"
    mt "Отвратительно!!!"
    mt "Унизительно!!!"
    mt "!!!"
    return

# Моника вышла от Виктории, на улице
# если Моника осудила Мелани, они стоят на улице вдвоем
label ep216_dialogues5_victoria_6:
    music Groove2_85
    imgf 24528
    m "Мелани, что эта сучка Виктория сделала с тобой?!"
    m "Она настоящая извращенка!"
    m "Притом больная на всю голову!"
    m "!!!"
    music Master_Disorder
    melanie "Миссис Бакфетт, давайте обсудим все позже..."
    melanie "Я сейчас не хочу говорить об этом."
    melanie "Мне... Мне нужно скорее идти..."
    fadeblack
    sound highheels_short_walk
    pause 2.0
    return

# при клике на Мелани после сцены у Виктории дома
label ep216_dialogues5_victoria_7:
    # не рендерить!!
    melanie "Миссис Бакфетт, давайте обсудим все позже..."
    melanie "Сейчас я хочу побыть одна..."
    return False

# Моника пытается войти в офис Дика НЕ в одежде шлюхи
label ep216_dialogues5_victoria_8a:
    mt "Эта сучка уже видела мое красивое платье, так что лучше идти к ней красивой и уверенной в себе!"
    return

label ep216_dialogues5_victoria_8:
    # не рендерить!!
    mt "Я не могу пойти к сучке Виктории в таком виде."
    mt "Она мне сказала, чтобы я приходила сюда только в той кошмарной одежде шлюхи!"
    return

label ep216_dialogues5_victoria_9: # смотрит на дом Виктории
    mt "Неплохо устроилась эта сикалявка на деньги Дика!"
    return

label ep216_dialogues5_victoria_10: # пытается зайти в дом Виктории
    mt "Мне надо как-то избавиться от этой сикалявки, но я пока не знаю как..."
    mt "Я даже не представляла насколько она опасна..."
    return

label ep216_dialogues5_victoria_11: # смотрит на здание Дика
    mt "Эта сучка поселилась поближе к Дику, чтобы присматривать за ним..."
    return

label ep216_dialogues5_victoria_12: #
    mt "Мне надо идти к этой сучке Виктории..."
    return False

label ep216_dialogues5_victoria_12b: #
    mt "Мне надо идти к этой сучке Виктории..."
    return
