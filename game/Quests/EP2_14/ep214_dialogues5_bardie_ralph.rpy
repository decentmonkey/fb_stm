default monicaBettyRalphSeduction1 = False  # Моника взяла платье Бетти, пока та на фитнесе
default monicaBettyRalphSeduction2 = False  # Моника сделала Ральфу минет в гостиной
default monicaBettyRalphSeduction3 = False  # Моника проглотила сперму Ральфа (минет в гостиной)
default monicaBettyRalphSeduction4 = False  # Моника сделала Ральфу футджоб в первый раз
default monicaBettyRalphSeduction5 = False  # Моника сделала Ральфу титсджоб в первый раз
default monicaBettyRalphSeduction6 = False  # Моника сделала Ральфу минет в спальне
default monicaBettyRalphSeduction7 = False  # Моника и Ральф занялись сексом
default monicaBettyRalphSeduction8 = False  # Моника сказала Ральфу, что ей нужны деньги
default monicaBettyRalphSeduction9 = False  # Моника сказала Ральфу, что любит его

default monicaBettyScene1CumZone = 0

#call ep214_dialogues5_bardie_ralph_1() # разговор с Барди в подвале
#call ep214_dialogues5_bardie_ralph_2() # раздевалка в фитнес-зале, меню - берет платье Бетти
#call ep214_dialogues5_bardie_ralph_3() # Моника в образе Бетти, мысли (глазик)
#call ep214_dialogues5_bardie_ralph_4() # Моника в образе Бетти, мысли перед встречей с Ральфом
#call ep214_dialogues5_bardie_ralph_5() # в гостиной с Ральфом
#call ep214_dialogues5_bardie_ralph_6() # после встречи с Ральфом в гостиной, мысли
#call ep214_dialogues5_bardie_ralph_6a() # после встречи с Ральфом, мысли, если идет в др. локацию, кроме фитнеса
#call ep214_dialogues5_bardie_ralph_7() # фитнес, возвращает платье Бетти
#call ep214_dialogues5_bardie_ralph_8() # разговор с Барди в его комнате
#call ep214_dialogues5_bardie_ralph_9() # после разговора с Барди, мысли
#call ep214_dialogues5_bardie_ralph_9a() # подходит к Ральфу в гостиной, когда Бетти дома
#call ep214_dialogues5_bardie_ralph_10() # в образе Бетти заходит в гостиную, Ральфа там нет
#call ep214_dialogues5_bardie_ralph_11a() # ищет Ральфа по дому, кухня
#call ep214_dialogues5_bardie_ralph_11b() # ищет Ральфа по дому, клик на подвал
#call ep214_dialogues5_bardie_ralph_11c() # ищет Ральфа по дому, клик на выход из дома
#call ep214_dialogues5_bardie_ralph_11d() # ищет Ральфа по дому, клик на комнату Барди
#call ep214_dialogues5_bardie_ralph_11e() # ищет Ральфа по дому, ванная
#call ep214_dialogues5_bardie_ralph_11f() # ищет Ральфа по дому, гостевая комната
#call ep214_dialogues5_bardie_ralph_12a() # спальня хозяев дома, первая встреча с Ральфом там
#call ep214_dialogues5_bardie_ralph_12() # спальня хозяев дома, интим с Ральфом
#call ep214_dialogues5_bardie_ralph_13() # спальня хозяев дома, после интима, меню выбора у Моники
#call ep214_dialogues5_bardie_ralph_13a() # спальня хозяев дома, после интима, регулярно
#call ep214_dialogues5_bardie_ralph_14() # если сказала Ральфу, что нужны деньги, мысли
#call ep214_dialogues5_bardie_ralph_15() # если сказала Ральфу, что любит его, мысли
#call ep214_dialogues5_bardie_ralph_16() # меню после интима, если сказала Ральфу, что любит его


# дом Моники, возле лестницы на первом этаже
label ep214_dialogues5_bardie_ralph_1:

    return

# фитнес, раздевалка
# Бетти переоделась и пошла в зал к тренеру
# при клике на шкафчик
label ep214_dialogues5_bardie_ralph_2:
    # Моника стоит одна возле шкафчика Бетти
    fadeblack 1.5
    music Groove2_85
    imgfl 31492
    call ep00_dialogues_ralph2()
    return

label ep214_dialogues5_bardie_ralph_2b:
    # "Переодеться в одежду Бетти и идти к Ральфу.":
#    menu:
#        "Взять одежду Бетти и ехать домой.":
#            $ monicaBettyRalphSeduction1 = True # Моника взяла платье Бетти, пока та на фитнесе
#            pass
    # Моника тянет руку к шкафчику Бетти
    # затемнение, звук snd_fabric
    imgf 31493
    w
    sound2 take_iron
    imgf scene_Map
    sound highheels_run1
    pause 3.0
    sound2 snd_fabric1
    fadeblack 1.5
    # смена кадра
    # Моника стоит в платье Бетти, с прической как у Бетти
    # переход на движок, Моника в платье Бетти у себя в подвале
    return

label ep214_dialogues5_bardie_ralph_2b1:
    mt "У меня мало времени!"
    mt "Надо успеть вернуться до того, как Бетти пойдет переодеваться после фитнеса!"
    return False

label ep214_dialogues5_bardie_ralph_2b2:
    mt "Некогда есть."
#    mt "Если я буду терять время, меня может заметить Барди!"
#    mt "Мне нельзя, чтобы он знал, что я продолжаю соблазнять Ральфа!"
    return False

label ep214_dialogues5_bardie_ralph_2b3:
    mt "Мне не стоит идти на улицу."
#    mt "Барди, скорее всего, там!"
#    mt "Мне нельзя, чтобы он знал, что я продолжаю соблазнять Ральфа!"
    return False

label ep214_dialogues5_bardie_ralph_2b4:

    return

label ep214_dialogues5_bardie_ralph_2c:

#    fadeblack
#    sound snd_fabric
#    pause 2.0
    music Stealth_Groover
    mt "Поверить не могу, что я надела платье этой провинциалки!"
    mt "Что только Ральф нашел в этой одежде?! Фи!"
    mt "!!!"
    mt "Так, Моника!"
    mt "Тебе нужно торопиться!"
    return

# при клике на Монику в образе Бетти, мысли (глазик)
label ep214_dialogues5_bardie_ralph_3:
    # не рендерить!!
    mt "Поверить не могу, что я надела платье этой провинциалки!"
    mt "Что только Ральф нашел в этой одежде?! Фи!"
    mt "!!!"
    return

# дом Моники
# она стоит во дворе дома или на первом этаже дома, мысли
label ep214_dialogues5_bardie_ralph_4:
    # не рендерить!!
    mt "Скоро я займу место Бетти в этом доме!"
    mt "Нужно будет сделать так, чтобы Ральф выгнал деревенщину Бетти отсюда."
#    mt "А малявку отправил обратно к его родной матери."
    mt "И я верну себе мой дом!"
    mt "Не могу поверить, что я настолько близко подошла к этой цели!!!"
    mt "!!!"
    return

# гостиная
# Ральф, как обычно, читает книгу
label ep214_dialogues5_bardie_ralph_5:
    # переодетая Моника заходит в гостиную к Ральфу
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 31494
    w
    imgf 31495
    w
    imgd 31496
    w
    imgd 31497
    mt "Ну, старикашка!"
    mt "Посмотрим, то ты сейчас будешь делать!"
    mt "!!!"
    # Ральф поднимает взгляд на Монику
    sound highheels_short_walk
    imgf 31498
    w
    imgd 31499
    w
    sound snd_folder_drop
    img 31500 vpunch
    ralph "Бетти..."
    # на лице шок, растерянность
    music stop
    sound plastinka1b
    img 31501 hpunch
    ralph "Моника?!"
    # Барди прячется у входа в гостиную
    # подсматривает за ними, в руках телефон
#    music Sneaky_Snitch
#    imgf 31502
#    w
#    sound snd_photo_capture
#    imgd 31503
#    w
    # смена кадра - гостиная
    # Моника смотрит на него, как-будто смущаясь
    music Groove2_85
    imgf 31504
    m "Не Моника, Мистер Робертс..."
    m "Мое настоящее имя Бетти."
    imgd 31505
    ralph "Бетти? Тебя зовут Бетти?!"
    m "Да, Мистер Робертс..."
    ralph "Ты сейчас пытаешься обмануть меня?"
    ralph "Чего ты хочешь от меня? Денег?"
    ralph "Если это правда, то почему ты представлялась всегда другим именем?"
    music Hidden_Agenda
    imgf 31506
    m "Дело в том, что я..."
    m "Я понимала, что вашей супруге не понравилось бы подобное сходство со мной."
    m "И она не взяла бы меня на работу в ваш дом."
    mt "Боже! Что за бред я несу?!"
    # Ральф в растерянности
    imgd 31507
    ralph "А п-почему ты решила рассказать мне об этом сейчас... Бетти..."
    m "Вы тогда были правы, Мистер Робертс."
    m "С самого начала, как только я устроилась на работу к вам..."
    m "Вы мне очень понравились."
    m "И я решила, что вы должны знать правду обо мне..."
    # Ральф встает с кресла и подходит к ней ближе
    music Groove2_85
    imgf 31508
    ralph "Бетти..."
    ralph "Тебе нужно было сразу мне все рассказать."
    m "Да, Мистер Робертс. Простите меня..."
    ralph "Тебе не за что извиняться передо мной, Бетти."
    ralph "Тебе так идет это платье..."
    ralph "Ты очень красивая в нем, Бетти..."
    # Ральф приобнимает ее за талию
    sound Jump1
    imgd 31509
    w
    # Барди прячется у входа в гостиную
    # Барди хихикает, подсматривая за ними, делает фотки (звуки камеры)
#    music Sneaky_Snitch
#    imgf 31510
#    sound snd_photo_capture
#    bardie_t "Да! Вот ты и попался, Ральф!"
    # смена кадра - гостиная
    fadeblack 1.5
    music Stealth_Groover
    imgfl 31511
    mt "Это сработало!"
    mt "Сработало!!!"
    mt "!!!"
    mt "Так, что дальше по плану, Моника?"
    imgf 31512
    mt "О Боже!"
    mt "Мне придется заниматься с ним ЭТИМ!"
    mt "Фу! Как противно!"
    mt "!!!"
    imgd 31513
    mt "Возьми себя в руки, Моника!"
    mt "Тебе нужно сделать ЭТО!"
#    mt "Малявка думает, что я делаю то, что хочет он..."
#    mt "Но я Моника Бакфетт! И я играю в свою игру..."
    mt "Я хладнокровно и неумолимо иду к своей цели..."
    mt "Вернуть назад мой дом!"
    # Моника игриво улыбается Ральфу
    music Hidden_Agenda
    imgf 31514
    m "Я вам правда нравлюсь, Мистер Робертс?"
    ralph "Да, Бетти..."
    ralph "Ты даже не представляешь, насколько..."
    # Моника слегка толкает Ральфа и он плюхается в свое кресло
    imgd 31515
    m "В таком случае..."
    sound snd_bodyfall
    img 31516 vpunch
    w
    imgf 31517
    m "Мистер Робертс не откажет мне, если я хочу сделать ему приятно?"
    music Loved_Up
    imgd 31518
    ralph "Как я могу отказать такой красивой девушке, Бетти..."
    # Ральф сидит в кресле, Моника на коленях перед ним
    # она игриво смотрит ему в глаза и ведет руками по его бедрам выше и выше
    imgd 31519
    ralph "Бетти..."
    m "Расслабьтесь, Мистер Робертс."
    m "Сейчас Бетти сделает вам очень-очень приятно."
    # Барди прячется у входа в гостиную
    # Барди хихикает, подсматривая за ними, делает фотки (звуки камеры)
#    music Sneaky_Snitch
#    imgf 31503
#    sound snd_photo_capture
#    bardie_t "Прямо как в фильмах про служанку и хозяина!"
#    bardie_t "Молодец, гувернантка!"
    # смена кадра - гостиная
    # Ральф сидит с приспущенными штанами
    # лицо Моники перед его членом
    sound snd_fabric1
    fadeblack 1.5
    music Groove2_85
    imgd 31520
    w
    imgf 31522
    w
    imgd 31521
    mt "Моника, просто сделай это!"
    mt "Ты почти у цели!"
    mt "Еще немного и ты вернешь себе свой дом!"
    ralph "Бетти, продолжай..."
    # Моника притворно улыбается
    music Hidden_Agenda
    imgd 31523
    m "С удовольствием, Мистер Робертс."
    # затем берет член в рот
    # минет
    fadeblack 1.5
    music2 Loved_Up

    imgf 31524
    w
    imgd 31525
    w
    sound drkanje5
    imgd 31526
    w
    imgd 31525
    w
    sound drkanje5
    imgd 31526
    w
    imgd 31525
    w
    sound drkanje5
    imgd 31526
    w
    imgd 31525
    w
    sound drkanje5
    imgd 31526



    ralph "Оооох, Бетти!"
    imgf 31527
    w
    sound lick3
    imgd 31528
    w
    sound lick3
    imgd 31529
    w
    sound lick3
    imgd 31528
    w
    sound lick3
    imgd 31529
    w
    sound lick3
    imgd 31528
    w
    sound lick3
    imgd 31529
    w
    sound lick3
    imgd 31528
    w
    sound lick3
    imgd 31529
    w

    sound chpok6
    imgd 31530
    ralph "Оооох..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Blowjob1.ogg"
    scene black
    image videov_Monica_Ralph_Blowjob1_1 = Movie(play="video/v_Monica_Ralph_Blowjob1_1.mkv", fps=30)
    show videov_Monica_Ralph_Blowjob1_1
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
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Blowjob1.ogg"
    scene black
    image videov_Monica_Ralph_Blowjob1_2 = Movie(play="video/v_Monica_Ralph_Blowjob1_2.mkv", fps=30)
    show videov_Monica_Ralph_Blowjob1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound lick3
    imgd 31531
    w
    sound lick3
    imgd 31532
    w
    sound lick3
    imgd 31533
    w
    sound lick3
    imgd 31532
    w
    sound lick3
    imgd 31533
    w
    sound lick3
    imgd 31532
    w
    sound lick3
    imgd 31533
    w
    sound lick3
    imgd 31532
    w
    sound lick3
    imgd 31533
    w
    sound chpok6
    imgd 31534
    ralph "Ммммм..."

#    img black_screen
#    with diss
#    stop music
#    $ renpy.music.set_volume(0.5, 0.5, channel="music")
#    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
#    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Blowjob1.ogg"
#    scene black
#    image videov_Monica_Ralph_Blowjob1_3 = Movie(play="video/v_Monica_Ralph_Blowjob1_3.mkv", fps=30)
#    show videov_Monica_Ralph_Blowjob1_3
#    with fade
#    wclean
#    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 31535
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Blowjob1.ogg"
    scene black
    image videov_Monica_Ralph_Blowjob1_4 = Movie(play="video/v_Monica_Ralph_Blowjob1_4.mkv", fps=30)
    show videov_Monica_Ralph_Blowjob1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 31536
    ralph "Беттииии..."
    ralph "Как хорошо у тебя получается делать этооооо..."

    # если Моника работала или работает в эскорте
    #
    if monicaEscortLastDay > 0:
        $ notif(_("Моника работает в ВИП-эскорте."))
        imgf 31537
        mt "Хоть какой-то прок от этой дурацкой работе в эскорте..."
    #
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Blowjob1.ogg"
    scene black
    image videov_Monica_Ralph_Blowjob1_5 = Movie(play="video/v_Monica_Ralph_Blowjob1_5.mkv", fps=30)
    show videov_Monica_Ralph_Blowjob1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 stop
    fadeblack 1.5
    music Loved_up2
    imgd 31538
    ralph "Ммммм, как же хорошооооо..."
    ralph "О, Беттииии..."
    ralph "Я сейчас кончу!"
    $ monicaBettyRalphSeduction2 = True # Моника сделала Ральфу минет в гостиной
    menu:
        "Кончить в рот Моники.":
            img 31539
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            ralph "Бетти!"
            ralph "Ооооо!!"
            img 31540
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            ralph "ООООООООО!!!"
            # Моника смотрит на Ральфа
            # он прибалдевший смотрит на нее
            imgf 31541
            w
            imgd 31542
            mt "..."
            $ monicaBettyScene1CumZone = 1
            $ menu_corruption = [0, monicaRalphBlowjob1SpermCorruptionRequired]
            menu:
                "Выплюнуть!":
                    # Моника выплевывает сперму на пол
                    # не показываем плевок
                    sound chavc26
                    imgf 31543
                    mt "ФУУУУ!"
                    mt "!!!!!"
                    pass
                "Проглотить.":
                    # Моника проглатывает, сидя на коленях
                    sound snd_gulp
                    imgf 31544
                    $ add_corruption(10, "monica_ralph_blowjob1_sperm")
                    mt "ФУУУУ!"
                    mt "Отвратительно!!"
                    mt "Меня сейчас стошнит!!!"
                    mt "!!!!!"
                    # + corruption
                    $ monicaBettyRalphSeduction3 = True # Моника проглотила сперму Ральфа (минет в гостиной)
                    pass
        "Кончить на лицо Моники.":
            img 31545
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            ralph "Бетти!"
            img 31546
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            ralph "Ооооо!!"
            ralph "ООООООООО!!!"
            sound hlup10
            imgf 31547
            w
            # Моника смотрит на Ральфа
            # он прибалдевший смотрит на нее
            imgd 31548
            w
            imgd 31549
            mt "ФУУУ!!!"
            mt "Испачкал мое лицо!!!"
            mt "!!!"
            $ monicaBettyScene1CumZone = 2
            pass
    # Барди прячется у входа в гостиную
    # Барди хихикает, подсматривая за ними, делает фотки (звуки камеры)
#    music Sneaky_Snitch
#    imgf 31550
#    w
#    sound snd_photo_capture
#    imgd 31503
#    bardie_t "Готово!!!"
    # затемнение
    # Ральф и Моника стоят в гостиной
    fadeblack
    sound snd_fabric
    pause 2.0
    $ add_corruption(20, "monica_ralph_blowjob1")
    music Hidden_Agenda
    imgfl 31551
    w
    imgf 31552
    m "Мистер Робертс, вам понравилось?"
    m "Я могу еще прийти к вам?"
    # Ральф стоит довольный
    music Groove2_85
    imgd 31553
    ralph "Да, Бетти."
    ralph "Мне очень понравилось!"
    ralph "Обязательно приходи ко мне еще!"
    ralph "Я буду ждать тебя, Бетти."
    return

# Моника вышла из гостиной после минета, мысли
label ep214_dialogues5_bardie_ralph_6:
    # не рендерить!!
    mt "Ральф попался на крючок!"
    mt "Скоро я снова стану здесь хозяйкой!"
    mt "Этот дом по праву принадлежит мне!"
    mt "!!!"
    mt "Сейчас мне нужно вернуться в фитнес зал и сложить платье Бетти в шкафчик."
    mt "Надеюсь, она не заметила моего отсутствия!"
#    $ log1 = _("Вернуться в фитнес зал.")
    return

# Моника вышла из гостиной после минета
# клик на любую другую локацию, кроме выхода, в т.ч. гостиную
label ep214_dialogues5_bardie_ralph_6a:
    # не рендерить!!
    mt "Сейчас мне нужно вернуться в фитнес зал и сложить платье Бетти в шкафчик."
    mt "Надеюсь, она не заметила моего отсутствия!"
    return False

# фитнес зал, раздевалка
label ep214_dialogues5_bardie_ralph_7:
    # Моника стоит у шкафчиков, уже в своей одежде
    sound snd_fabric1
    fadeblack 2.0
    music Stealth_Groover
    imgfl 31554
    w
    imgf 31555
    mt "Эта провинциалка Бетти ничего не заметила."
    mt "Видимо, слишком занята с фитнес тренером."
    #
    $ notif(_("Бетти изменяет Ральфу с фитнес тренером."))
    #
#    mt "Малявка Барди был прав."
#    imgd 31556
#    mt "Кстати, насчет малявки..."
#    mt "Нужно узнать у него, записал он грехопадение Ральфа со мной или нет."
#    $ log1 = _("Поговорить с Барди.")
    return

# комната Барди, вечер после первого интима с Ральфом
label ep214_dialogues5_bardie_ralph_8:
    # Моника заходит к Барди в комнату
    # Барди валяется на кровати

    return

# Моника вышла из комнаты Барди после разговора с ним, мысли
label ep214_dialogues5_bardie_ralph_9:
    # не рендерить!!
    mt "Хозяйка в этом доме одна. Я!"
#    mt "И скоро я от тебя, малявка, избавлюсь раз и навсегда!"
    mt "Этот никчемный Ральф сказал, что будет ждать меня."
    mt "В следующий раз мне нужно будет снова поехать с Бетти на фитнес."
#    $ log1 = _("Поехать с Бетти на фитнес во вторник или четверг.")
    return

# если в любой другой день подойти к Ральфу в форме гувернантки
label ep214_dialogues5_bardie_ralph_9a:
    # в гостиной, Ральф с книгой
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 31560
    w
    imgf 31561
    m "Мистер Робертс..."
    ralph "Тсс!"
    ralph "Бетти, мы с тобой должны скрывать наши отношения!"
    ralph "Я не хочу, чтобы моя другая Бетти узнала об этом!"
    imgd 31562
    m "Хорошо, Мистер Робертс."
    mt "До сих пор боится эту деревенщину Бетти!"
    mt "Жалкий подкаблучник! Фи!"
    return

# следующий раз, когда Бетти на фитнесе
# Моника в наряде Бетти заходит в гостиную
label ep214_dialogues5_bardie_ralph_10:
    # Ральфа в гостиной нет
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 31563
    w
    imgf 31564
    mt "Хммм..."
    mt "Странно..."
    mt "Куда этот никчемный Ральф мог деться?"
    mt "???"
    mt "Он же сказал, что будет ждать меня..."
    mt "Может быть, он в другой комнате?"
    return

# Моника ищет Ральфа по дому
label ep214_dialogues5_bardie_ralph_11a:
    # кухня
    # не рендерить!!
    mt "Странно, что его нет на кухне."
    mt "Обычно он или здесь или в гостиной со своей дурацкой книгой."
    return False
label ep214_dialogues5_bardie_ralph_11b:
    # клик на подвал
    # не рендерить!!
    mt "Вряд ли он пойдет в подвал..."
    mt "Не вижу смысла его там искать."
    return False
label ep214_dialogues5_bardie_ralph_11c:
    # клик на выход из дома
    # не рендерить!!
    mt "Я еще не во всех комнатах поискала."
    mt "Куда делся этот старикашка?!"
    return False
label ep214_dialogues5_bardie_ralph_11d:
    # клик комнату Барди
    # не рендерить!!
    mt "В этой комнате его точно не будет."
    mt "Он вообще сюда не заходит."
    return False
label ep214_dialogues5_bardie_ralph_11e:
    # ванная комната, душ
    # не рендерить!!
    mt "И здесь его нет."
    mt "Он что, решил избежать встречи со мной?!"
    return False
label ep214_dialogues5_bardie_ralph_11f:
    # гостевая комната
    # не рендерить!!
    mt "Не мог же он забыть о нашей встрече!"
    mt "!!!"
    return

# бывшая спальня Моники (первая встреча в спальне)
label ep214_dialogues5_bardie_ralph_12a:
    # Ральф лежит на кровати
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgf 31565
    w
    imgd 31566
    mt "Ну наконец-то!"
    mt "Устроил тут прятки!"
    mt "!!!"
    return

# бывшая спальня Моники
label ep214_dialogues5_bardie_ralph_12:
    # Ральф самодовольно говорит Монике
    music Hidden_Agenda
    imgf 31567
    ralph "А, плохая гувернантка снова хочет соблазнить хозяина в его доме!"
    ralph "Пока хозяйка не видит!"
    ralph "Признавайся, Бетти!"
    # Моника притворно улыбается
    imgd 31568
    m "Да, Мистер Робертс."
    m "Ваша Бетти соскучилась по вам!"
    ralph "Иди сюда!"

##### отсюда регулярные встречи

    # Моника не спешит идти к нему
    # игриво улыбается и скидывает с себя платье на пол
    imgf 31569
    w
    sound snd_fabric1
    imgd 31570
    w
    imgf 31571
    w
    music Stealth_Groover
    imgd 31572
    mt "Какой же он мерзкий, этот никчемный Ральф!"
    mt "!!!"
    mt "Но я должна это сделать!"
    mt "Я совсем близко к тому, чтобы вернуть себе свой дом!"
    ralph "Какая же ты красивая, Бетти..."
    mt "Да..."
    mt "В отличие от твоей провинциальной жены..."
    mt "Которая завладела моей кроватью и валяется в ней своей жирной задницей!"
    mt "Ненавижу эту деревенщину!"
    # Ральф зовет Монику к себе на кровать
    music Groove2_85
    imgd 31573
    ralph "Иди ко мне скорее!"
    # Моника лезет к нему на кровать
    # Ральф похотливо смотрит на нее
    # поцелуй
    fadeblack 1.5
    music Loved_Up
    imgfl 31574
    w
#    sound kiss1
    imgf 31576
    w
    sound kiss1
    imgd 31577
    w
    imgd 31575
    ralph "Мммм... Бетти..."
    ralph "Я так скучал по тебе..."
    ralph "Так хочу тебя, Бетти."
    ralph "Как мы это сделаем сегодня?"
    # пункты меню открываются постепенно
    menu:
        "Ласкать Ральфа ногами.":
            # Моника игриво
            imgf 31578
            m "Если Мистер Робертс не против, я могу ласкать его своими ножками..."
            m "Уверена, что вам понравится..."
            ralph "Ммм... Плохая гувернантка Бетти все-таки соблазнила хозяина дома..."
            # Моника садится напротив Ральфа (поза как в пабе на привате или как на скринах, где она сидит сзади него)
            # начинает трогать его член ногами
            fadeblack
            sound snd_fabric
            pause 2.0
            music2 Loved_up2
            imgfl 31597
            w
            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
            scene black
            image videov_Monica_Ralph_Footjob1_1 = Movie(play="video/v_Monica_Ralph_Footjob1_1.mkv", fps=25)
            show videov_Monica_Ralph_Footjob1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31598
            ralph "Оооох, Бетти!"
            imgd 31599
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
            scene black
            image videov_Monica_Ralph_Footjob1_2 = Movie(play="video/v_Monica_Ralph_Footjob1_2.mkv", fps=25)
            show videov_Monica_Ralph_Footjob1_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31601
            ralph "Оооох..."
            imgd 31600
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
            scene black
            image videov_Monica_Ralph_Footjob1_3 = Movie(play="video/v_Monica_Ralph_Footjob1_3.mkv", fps=25)
            show videov_Monica_Ralph_Footjob1_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31602
            ralph "Ммммм..."
            # водит ногами вверх-вниз
            imgd 31603
            w
            sound drkanje5
            imgd 31605
            w
            imgd 31603
            w
            sound drkanje5
            imgd 31605
            w
            imgd 31603
            w
            sound drkanje5
            imgd 31605
            w
            imgd 31603
            w
            sound drkanje5
            imgd 31605
            w
            # Ральф балдеет
            # Моника смотрит на него игриво
            imgf 31604
            m "Вам нравится, Мистер Робертс?"
            imgd 31606
            ralph "Ммммм, как же хорошооооо..."
            ralph "Как гувернантка Бетти старается для хозяина..."
            imgf 31603
            w
            imgd 31605
            ralph "Я сейчас кончу!"
            # кончает ей на ступни
            img 31607
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            ralph "Бетти!"
            img 31608
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            ralph "Ооооо!!"
            imgd 31609
            ralph "ООООООООО!!!"
            imgf 31610
            mt "Фу!"
            mt "Этот никчемный подкаблучник испачкал мои ножки!"
            mt "!!!"
            $ add_corruption(monicaRalphScene1Corruption, "monica_ralph_scene1")
            $ monicaBettyRalphSeduction4 = True # Моника сделала Ральфу футджоб в первый раз
            music2 stop
            fadeblack 1.5
            pass
        "Ласкать Ральфа грудями." if monicaBettyRalphSeduction4 == True:
            # Ральф трогает груди Моники
            imgf 31611
            ralph "Если моя гувернантка Бетти сделает приятное хозяину этого дома..."
            ralph "Своими прекрасными грудями..."
            ralph "Пока другая Бетти не здесь..."
            ralph "То это будет здорово."
            # Моника игриво
            imgd 31612
            mt "Это МОЙ ДОМ!!!"
            mt "Никчемный старикашка!!!"
            mt "!!!"
            m "Конечно, Мистер Робертс."
            m "Бетти сделает все для вашего удовольствия."
            # Моника обхватывает грудями член Ральфа
            # начинает водить ими по члену туда-сюда
            fadeblack
            sound snd_fabric
            pause 2.0
            music2 Loved_up
            imgfl 31613
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_Ralph_Titjob1.ogg"
            scene black
            image videov_Monica_Ralph_Titjob1_1 = Movie(play="video/v_Monica_Ralph_Titjob1_1.mkv", fps=30)
            show videov_Monica_Ralph_Titjob1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31614
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_Ralph_Titjob1.ogg"
            scene black
            image videov_Monica_Ralph_Titjob1_2 = Movie(play="video/v_Monica_Ralph_Titjob1_2.mkv", fps=30)
            show videov_Monica_Ralph_Titjob1_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31615
            w
            imgf 31616
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_Ralph_Titjob1.ogg"
            scene black
            image videov_Monica_Ralph_Titjob1_3 = Movie(play="video/v_Monica_Ralph_Titjob1_3.mkv", fps=30)
            show videov_Monica_Ralph_Titjob1_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.5
            music Loved_Up2
            imgd 31617
            ralph "Ммммм, Бетти!"
            imgf 31618
            w
            imgd 31619
            w
            sound drkanje5
            imgd 31620
            w
            imgd 31619
            w
            sound drkanje5
            imgd 31620
            w
            imgd 31619
            w
            sound drkanje5
            imgd 31620
            w
            imgd 31619
            w
            sound drkanje5
            imgd 31620
            ralph "Оооох..."
            # Моника смотрит на него игриво
            imgf 31621
            m "Вам нравится, Мистер Робертс?"
            imgd 31622
            ralph "Даааа..."
            ralph "О, Беттииии..."
            imgd 31623
            ralph "Я сейчас кончу!"
            menu:
                "Кончить в рот Моники.":
                    # Моника наклоняется и берет головку члена в рот
                    imgf 31627
                    w
                    img 31628
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Бетти!"
                    img 31629
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan1
                    ralph "Ооооо!!"
                    ralph "ООООООООО!!!"
                    # Моника смотрит на Ральфа
                    # он прибалдевший смотрит на нее
                    imgf 31630
                    mt "Фу!"
                    mt "Какая гадость!"
                    mt "!!!"
                    pass
                "Кончить на грудь Моники.":
                    img 31624
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Бетти!"
                    img 31625
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan1
                    ralph "Ооооо!!"
                    ralph "ООООООООО!!!"
                    # Моника смотрит на Ральфа
                    # он прибалдевший смотрит на нее
                    imgf 31626
                    mt "Этот старикашка испачкал мою прекрасную грудь!"
                    mt "!!!"
                    pass
            $ add_corruption(monicaRalphScene2Corruption, "monica_ralph_scene2")
            $ monicaBettyRalphSeduction5 = True # Моника сделала Ральфу титсджоб в первый раз
            pass
        "Минет." if monicaBettyRalphSeduction5 == True:
            # Моника игриво
            imgf 31631
            m "Если Мистер Робертс не против, я могу ласкать его своим ротиком..."
            m "Уверена, что вам понравится..."
            ralph "Ммм, плохая гувернантка Бетти мечтала о члене хоязина этого дома?"
            mt "ААА!!! Как же он меня бесит!"
            m "Да, мечтала, Мистер Робертс..."
            ralph "Да, Бетти, мне нравится эта идея!"
            # Ральф лежит на кровати, Моника опускается к его члену
            # начинает ласкать его, потом берет в рот
            fadeblack
            sound snd_fabric
            pause 2.0
            music2 Loved_up

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_Ralph_Masturbation1.ogg"
            scene black
            image videov_Monica_Ralph_Masturbation1_1 = Movie(play="video/v_Monica_Ralph_Masturbation1_1.mkv", fps=30)
            show videov_Monica_Ralph_Masturbation1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgfl 31632
            w
            imgf 31633
            w
            imgd 31634
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_Ralph_Masturbation1.ogg"
            scene black
            image videov_Monica_Ralph_Masturbation1_2 = Movie(play="video/v_Monica_Ralph_Masturbation1_2.mkv", fps=30)
            show videov_Monica_Ralph_Masturbation1_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31635
            ralph "Оооох..."

            imgd 31636
            w
            imgf 31637
            w
            sound drkanje5
            imgd 31638
            w
            imgd 31637
            w
            sound drkanje5
            imgd 31638
            w
            imgd 31637
            w
            sound drkanje5
            imgd 31638
            w
            imgd 31637
            w
            sound drkanje5
            imgd 31638
            w
            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_Ralph_Masturbation1.ogg"
            scene black
            image videov_Monica_Ralph_Masturbation1_3 = Movie(play="video/v_Monica_Ralph_Masturbation1_3.mkv", fps=30)
            show videov_Monica_Ralph_Masturbation1_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31639
            ralph "Ммммм..."


            imgd 31640
            ralph "О, Бетти!!!"
            ralph "Это восхитительно!!!"
            ralph "Давай, я сяду по-другому, чтобы мне было удобнее наслаждаться твоим ротиком..."
            ##
            # здесь нужна фраза Ральфа, что-то типа - "давай немного изменим позу"
            ##
            music2 stop
            fadeblack 1.5
            music Loved_Up2
            imgfl 31641
            w
            imgf 31642
            w
            imgd 31643
            ralph "Беттииии..."
            imgf 31644
            w
            sound drkanje5
            imgd 31645
            w
            imgd 31644
            w
            sound drkanje5
            imgd 31645
            w
            imgd 31644
            w
            sound drkanje5
            imgd 31645
            w
            imgd 31644
            w
            sound drkanje5
            imgd 31645
            ralph "Я сейчас кончу!"
            $ monicaBettyRalphSeduction6 = True # Моника сделала Ральфу минет в спальне
            menu:
                "Кончить в рот Моники.":
                    img 31646
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Бетти!"
                    img 31647
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan1
                    ralph "Ооооо!!"
                    ralph "ООООООООО!!!"
                    # Моника смотрит на Ральфа
                    # он прибалдевший смотрит на нее
                    imgd 31648
                    mt "..."
                    $ menu_corruption = [0, monicaRalphBlowjob2SpermCorruptionRequired]
                    menu:
                        "Выплюнуть!":
                            # Моника выплевывает сперму на пол
                            # не показываем плевок
                            sound chavc26
                            imgf 31649
                            mt "ФУУУУ!"
                            mt "!!!!!"
                            pass
                        "Проглотить.":
                            # Моника проглатывает, сидя на коленях
                            sound snd_gulp
                            imgf 31650
                            mt "ФУУУУ!"
                            mt "Отвратительно!!"
                            mt "Меня сейчас стошнит!!!"
                            mt "!!!!!"
                            $ add_corruption(monicaRalphScene3bCorruption, "monica_ralph_scene3b")
                            pass
                "Кончить на лицо Моники.":
                    img 31646
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Бетти!"
                    img 31651
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Ооооо!!"
                    img 31652
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan1
                    ralph "ООООООООО!!!"
                    # Моника смотрит на Ральфа
                    # он прибалдевший смотрит на нее
                    imgf 31653
                    mt "Испачкал мое лицо!!!"
                    mt "Гадость!!!"
                    mt "!!!"
                    pass
            $ add_corruption(monicaRalphScene3Corruption, "monica_ralph_scene3")
            pass
        "Секс" if monicaBettyRalphSeduction6 == True:
            # Ральф трогает груди Моники
            fadeblack
            sound snd_fabric
            pause 2.0
            music Loved_Up
            imgfl 31654
            w
            imgf 31655
            w
            imgd 31656
            w
            imgf 31657
            ralph "Какая же ты красивая!"
            w
            imgd 31658
            ralph "Гувернантка Бетти хочет почувствовать в себе член хозяина?"
            ralph "Она хочет отдаться хозяину этого дома?"
            # целует губы, потом грудь
            sound kiss1
            imgd 31659
            w
            sound kiss1
            imgf 31660
            ralph "Бетти, я так хочу тебя..."
            # Моника игриво
            imgd 31661
            mt "Моника, соберись!"
            mt "Как бы ни было противно, но тебе надо сказать эти слова!"
            m "Мистер Робертс, я тоже хочу вас!"
            ##
            # Здесь сначала поза "собачки"
            ##
            fadeblack 2.0
            music2 Loved_up2
            imgfl 31662
            w
            imgf 31663
            w
            imgd 31664
            w
            imgf 31665
            w
            sound chpok6
            img 31666 vpunch
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex1_1 = Movie(play="video/v_Monica_Ralph_Sex1_1.mkv", fps=30)
            show videov_Monica_Ralph_Sex1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31667
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex1_2 = Movie(play="video/v_Monica_Ralph_Sex1_2.mkv", fps=30)
            show videov_Monica_Ralph_Sex1_2
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
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex1_3 = Movie(play="video/v_Monica_Ralph_Sex1_3.mkv", fps=30)
            show videov_Monica_Ralph_Sex1_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31668
            w
            imgd 31669
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex1_4 = Movie(play="video/v_Monica_Ralph_Sex1_4.mkv", fps=30)
            show videov_Monica_Ralph_Sex1_4
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
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex1_5 = Movie(play="video/v_Monica_Ralph_Sex1_5.mkv", fps=30)
            show videov_Monica_Ralph_Sex1_5
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31670
            ralph "Садись на меня сверху, Бетти."
            ralph "Это моя любимая поза."
            ralph "Я хочу смотреть на тебя, видеть твое прекрасное личико."
            # Ральф ложится на кровать, Моника садится сверху него
            # секс
            music2 stop
            fadeblack 2.0
            music2 Loved_up2
            imgfl 31677
            w
            imgf 31678
            w
            imgd 31679
            w
            imgf 31680
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex2_1 = Movie(play="video/v_Monica_Ralph_Sex2_1.mkv", fps=30)
            show videov_Monica_Ralph_Sex2_1
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
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex2_2 = Movie(play="video/v_Monica_Ralph_Sex2_2.mkv", fps=30)
            show videov_Monica_Ralph_Sex2_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")


            imgd 31681
            ralph "Оооох, Бетти!"
            imgf 31682
            w


            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex2_5 = Movie(play="video/v_Monica_Ralph_Sex2_5.mkv", fps=30)
            show videov_Monica_Ralph_Sex2_5
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
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex2_3 = Movie(play="video/v_Monica_Ralph_Sex2_3.mkv", fps=30)
            show videov_Monica_Ralph_Sex2_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")


            imgd 31683
            ralph "Оооох..."
            music2 stop
            fadeblack 1.5
            music2 Loved_Up2
            imgf 31671
            w
            imgd 31672
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex2_4 = Movie(play="video/v_Monica_Ralph_Sex2_4.mkv", fps=30)
            show videov_Monica_Ralph_Sex2_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31673
            w

            imgd 31674
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Ralph_Sex1.ogg"
            scene black
            image videov_Monica_Ralph_Sex2_6 = Movie(play="video/v_Monica_Ralph_Sex2_6.mkv", fps=30)
            show videov_Monica_Ralph_Sex2_6
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31675
            w
            sound drkanje5
            imgd 31676
            w
            imgd 31675
            w
            sound drkanje5
            imgd 31676
            w
            imgd 31675
            w
            sound drkanje5
            imgd 31676
            w
            imgd 31675
            w
            sound drkanje5
            imgd 31676
#            ralph "Оооох..."
            ralph "Ммммм..."
            # Моника смотрит на него игриво
            imgf 31684
            m "Вам нравится, Мистер Робертс?"
            ralph "Ммммм, даааа..."
            ralph "О, Беттииии..."
            ralph "Я сейчас кончу!"
            $ menu_corruption = [0, monicaRalphSexCumInsideCorruptionRequired]
            menu:
                "Кончить на киску Моники.":
                    # Моника приподнимается и Ральф кончает на ее киску
                    img 31685
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Бетти!"
                    img 31688
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Ооооо!!"
                    img 31689
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan1
                    ralph "ООООООООО!!!"
                    # Моника смотрит на Ральфа
                    # он прибалдевший смотрит на нее
                    mt "!!!"
                    pass
                "Кончить внутрь Моники.":
                    img 31685
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Бетти!"
                    img 31686
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    ralph "Ооооо!!"
                    img 31687
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan1
                    ralph "ООООООООО!!!"
                    # Моника смотрит на Ральфа
                    # он прибалдевший смотрит на нее
                    $ add_corruption(monicaRalphScene4bCorruption, "monica_ralph_scene4b")
                    mt "!!!"
                    pass
            music2 stop
            fadeblack 1.5
            $ questHelp("house_38", True)
            $ add_corruption(monicaRalphScene4Corruption, "monica_ralph_scene4")
            $ monicaBettyRalphSeduction7 = True # Моника и Ральф занялись сексом
            pass
    # затемнение
    return

# бывшая спальня Моники
label ep214_dialogues5_bardie_ralph_13:
    # Моника и Ральф лежат вместе на кровати после интима
    fadeblack 2.0
    music Groove2_85
    imgfl 31579
    w
    imgf 31580
    ralph "Бетти, это было потрясающе!"
    ralph "Почему ты раньше не говорила мне правду о себе?"
    ralph "Мы столько времени потеряли из-за этого..."
    music Stealth_Groover
    imgd 31581
    mt "Надо спросить у твоего сына, почему он именно сейчас решил шантажировать тебя, старикашка..."
#    mt "У мерзкой малявки Барди получилось придумать идеальный для меня план."
    music Groove2_85
    m "Вы же знаете, Мистер Робертс, что я не могла этого сделать..."
    m "Из-за риска потерять работу."
    imgd 31582
    ralph "Кстати, Бетти..."
    ralph "Я тут подумал..."
    ralph "Ты же не получаешь зарплату."
    ralph "Если тебе нужны деньги, ты скажи мне об этом."
    ralph "Я буду помогать тебе."
    mt "..."
    menu:
        "Да, мне нужны деньги, Мистер Робертс.":
            music Stealth_Groover
            imgf 31583
            mt "Отлично, Моника..."
            mt "Он предлагает тебе помогать деньгами."
            mt "Ты стала его любовницей, так почему бы не брать у него денег?"
            mt "Это хорошая возможность прекратить, наконец, издевательства Бифа!"


            # если работает в экорте
            if monicaEscortLastDay > 0 and ep212_escort_monica_fired != True:
                imgd 31584
                mt "И работу в этом гадком ВИП-эскорте!"

            if monicaPubWashingDishesCount > 0:
                # если работает у пилона в трущобах и, или стриптизершей в баре
                imgd 31584
                mt "И еще тебе больше не нужно будет ходить на работу в трущобы!"
                mt "Боже!"
                mt "Как давно я ждала этого момента, чтобы послать к черту всех этих никчемных людишек!"

            # Моника скромно
            music Hidden_Agenda
            imgf 31585
            m "Мистер Робертс, это так неожиданно..."
            m "Мне очень неудобно говорить об этом..."
            ralph "Не стоит стесняться, Бетти."
            ralph "Я же сам предлагаю тебе помощь."
            m "Мне и правда нужны деньги, Мистер Робертс."
            m "Ведь я совсем ничего не зарабатываю..."
            ralph "Сколько денег тебе нужно, Бетти, дорогая?"
            m "$ 5 000."
            music stop
            sound plastinka1b
            img 31586 hpunch
            ralph "Ого! Ты меня несколько удивила..."
            m "В неделю..."
            ralph "Тебе нужна такая сумма каждую неделю?"
            m "Да, Мистер Робертс."
            music Groove2_85
            ralph "Хмм..."
            ralph "Это, конечно, немаленькая сумма..."
            # Ральф в задумчивости чешет затылок
            imgf 31587
            ralph "Дорогая, я буду тебе давать $ 200."
            ralph "Могу это делать при каждой нашей встрече."
            ralph "Для тебя, Бетти, мне не жалко никаких денег."
            music Pyro_Flow
            imgd 31588
            mt "200 долларов?!"
            mt "Он что, издевается?!"
            mt "Жалкий жадный старикашка!!!"
            mt "!!!"
            music Groove2_85
            imgd 31589
            ralph "Только ты должна пообещать мне, дорогая..."
            ralph "Что будешь приходить ко мне каждый раз, когда Бетти не будет дома."
            ralph "И скрывать от нее нашу с тобой связь."
            music Hidden_Agenda
            m "Конечно, Мистер Робертс."
            m "Я так благодарна вам за вашу помощь."
            mt "Придурок!!!"
            mt "!!!"
            imgf 31590
            sound kiss1
            w
            # поцелуй
            $ monicaBettyRalphSeduction8 = True # Моника сказала Ральфу, что ей нужны деньги
#            $ log1 = _("Подкаблучник Ральф готов платить мне $ 200 за секс с ним по вторникам и четвергам. Жадный старикашка!") #квест-лог
            return 1
        "Я делаю это не из-за денег, Мистер Робертс.":
            music Stealth_Groover
            imgf 31583
            mt "Отлично, Моника..."
            mt "Он предлагает тебе помогать деньгами."
            mt "Но не стоит торопиться сейчас..."
            mt "Твоя цель - вернуть себе место хозяйки этого дома."
            mt "Оно по праву принадлежит тебе!"
            imgd 31591
            mt "Мне нужно сделать так, чтобы этот тюфяк поверил, что я люблю его..."
            mt "И что я буду для него лучшей женой, чем провинциалка Бетти."
            mt "Он забывает, что если женщине ничего не надо, это значит что ей надо все!"
            mt "Так что про деньги я с ним поговорю после того, как избавлюсь от Бетти."

            if monicaEscortLastDay > 0 and ep212_escort_monica_fired != True:
                # если работает в экорте
                imgd 31584
                mt "И тогда смогу бросить работу в этом гадком ВИП-эскорте!"

            if monicaPubWashingDishesCount > 0:
                # если работает у пилона в трущобах и, или стриптизершей в баре
                imgd 31584
                mt "И мне больше не нужно будет ходить на работу в трущобы!"
                mt "Боже!"
                mt "Как давно я ждала этого момента, чтобы послать к черту всех этих никчемных людишек!"
                mt "Моя цель совсем близко!!!"
                mt "!!!"

            # Моника возмущенно
            music Hidden_Agenda
            imgf 31592
            m "Мистер Робертс..."
            ralph "Да, Бетти..."
            m "Неужели вы думаете, что я с вами из-за денег?"
            m "Я мечтала о вас с первого дня работы в этом доме!"
            m "И мне не нужны никакие деньги, лишь бы вы были рядом со мной!"
            m "Потому что я..."
            # скромно
            imgd 31585
            m "Я люблю вас, Мистер Робертс..."
            ralph "О, Бетти!"
            ralph "Какая ты милая и хорошая!"
            ralph "Прости, если я тебя обидел!"
            music Stealth_Groover
            imgd 31593
            mt "Он мне верит..."
            mt "Продолжай в том же духе, Моника."
            m "Все хорошо, Мистер Робертс."
            m "Просто поцелуй меня и большего мне не нужно."
            sound kiss1
            imgf 31590
            w
            # поцелуй
            $ monicaBettyRalphSeduction9 = True # Моника сказала Ральфу, что любит его
            return 2
    return

# бывшая спальня Моники, после интима (регулярно)
label ep214_dialogues5_bardie_ralph_13a:
    # Моника и Ральф лежат вместе на кровати после интима и болтают
    fadeblack 2.0
    music Groove2_85
    imgfl 31579
    w
    imgf 31580
    ralph "Бетти, это было потрясающе!"
    ralph "Ты самая красивая женщина из всех, что у меня были."
    mt "Я вообще самая красивая женщина!"
    mt "Не только в твоей жизни, жалкий подкаблучник!"
    ralph "Мне так нравится проводить время с тобой, Бетти..."
    m "И мне очень с вами хорошо, Мистер Робертс..."
    sound kiss1
    imgd 31590
    w
    if monica_ralph_relationships_type == 1:
        # поцелуй
        # если Моника сказала Ральфу, что ей нужны деньги
        # смена кадра, Моника стоит в комнате одетая
        fadeblack
        sound snd_fabric
        pause 2.0
        music Hidden_Agenda
        imgfl 31594
        w
        imgf 31595
        m "Мистер Робертс, мне нужны деньги..."
        music Groove2_85
        ralph "Да, Бетти."
        ralph "Ты же знаешь, что я рад тебе помогать деньгами."
        $ add_money(200.0)
        ralph "Вот твои $ 200."
        imgd 31596
        m "Спасибо, Мистер Робертс."
        mt "Жалкий, жадный старикашка!"
        mt "Фу!"
    return


# если Моника сказала Ральфу, что ей нужны деньги, мысли
label ep214_dialogues5_bardie_ralph_14:
    # не рендерить!!
    mt "Теперь Ральф у меня на крючке."
    mt "Мне достаточно встречаться с ним по вторникам и четвергам."
    mt "Пока провинциалка Бетти кувыркается со совим тренером в фитнес зале."
    mt "И он будет давать мне $ 200."
    mt "Конечно, это небольшая сумма..."
    mt "Но я смогу его убедить давать мне больше денег."
    mt "Ведь этот никчемный старикашка без ума от меня!"
    mt "!!!"
    return

# если Моника сказала Ральфу, что любит его, мысли
label ep214_dialogues5_bardie_ralph_15:
    # не рендерить!!
    mt "Теперь Ральф у меня на крючке."
    mt "Он предлагает тебе помогать деньгами."
    mt "Но не стоит торопиться сейчас..."
    mt "Мне нужно сделать так, чтобы этот тюфяк поверил, что я люблю его..."
    mt "Сначала я верну себе свое законное место хозяйки этого дома!"
    mt "А про деньги я с ним поговорю после того, как избавлюсь от Бетти."
    return

# если Моника сказала Ральфу, что любит его
label ep214_dialogues5_bardie_ralph_16:
    # после очередного секса возникает меню
    fadeblack 2.0
    music Loved_Up
    imgfl 31579
    ralph "Бетти, это было потрясающе!"
    ralph "Ты самая красивая женщина из всех, что у меня были."
    mt "Я вообще самая красивая женщина!"
    mt "Не только в твоей жизни, жалкий подкаблучник!"
    menu:
        "Предложить Ральфу узаконить наши отношения (в следующем обновлении) (disabled)":
            return True
        "Поцеловать Ральфа.":
            # Моника тянется к Ральфу за поцелуем
            music Loved_Up
            imgf 31580
            m "Мистер Робертс, я так счастлива, что вы со мной рядом."
            m "Мне так хорошо с вами..."
            ralph "Бетти, дорогая..."
            ralph "Мне тоже очень хорошо, когда ты со мной!"
            sound kiss1
            imgd 31590
            w
            # поцелуй
            return False
    return
