default monicaShlut1PhillipBlowjob1 = False  # Моника согласилась на блоуджоб Филиппу со шлюхой номер 1
default monicaShlut1PhillipBlowjob2 = False  # Моника делала минет Филиппу со шлюхой номер 1

#call ep211_dialogues7_Phillip_home_1() # разговор со шлюхой номер 1 возле дома Филиппа
#call ep211_dialogues7_Phillip_home_2() # гостиная у Филиппа, меню выбора (тройничок или двойной минет)
#call ep211_dialogues7_Phillip_home_3() # выбран пункт меню 'Двойной минет', сцена
#call ep211_dialogues7_Phillip_home_4() # улица возле дома Филиппа после двойного блоуджоба, разговор со шлюхой 1
#call ep211_dialogues7_Phillip_home_5() # мысли Моники после двойного блоуджоба, шлюха 1 отдала ей 50 баксов и ушла


# если у Филиппа шлюха номер 1 и Моника оказалась на улице
# при выборе пункта 'Мне нужны эти деньги' в диалоге со шлюхой номер 1 (ep210_dialogues2_escort_start_Phillip_13)
# улица возле дома Филиппа
label ep211_dialogues7_Phillip_home_1:
    # Моника разговаривает с субботней шлюхой номер 1
    music Pyro_Flow
    img 17064
    with fade
    mt "Он платит этой шлюхе 200 долларов!"
    mt "А мне - какие-то жалкие 100!"
    mt "Мне! Самой красивой женщине этого города!!!"
    mt "!!!"
    menu:
        "Почему $ 50?!":
            pass
    img 17065
    with diss
    m "А почему только 50 долларов?!"
    m "Если я тебе и буду помогать, то только за $ 100!"
    music Groove2_85
    img 17066
    with fade
    whore_number_1 "Если бы я тебе это не предложила..."
    whore_number_1 "Ты бы вообще сегодня осталась без заработка!"
    whore_number_1 "50 баксов и ни центом больше!"
    music Power_Bots_Loop
    img 23168
    with diss
    mt "Жадная сучка!"
    mt "!!!"
    music Groove2_85
    img 17067
    with fade
    whore_number_1 "Тем более, от тебя ничего сверхъестественного не требуется..."
    whore_number_1 "Поможешь отсосать у него и все."
    img 17068
    with diss
    m "А зачем тебе моя помощь?"
    m "Сама не справляешься?"
    img 17069
    with fade
    whore_number_1 "Я думаю, что ему понравится..."
    whore_number_1 "Это внесет немного разнообразия."
    whore_number_1 "И, возможно, он заплатит мне больше..."
    music Pyro_Flow
    img 17070
    with diss
    mt "Да как эта дешевая шлюха смеет предлагать мне такое?!"
    mt "То что она предлагает сделать - грязно и мерзко..."
    mt "Она что, думает что я соглашусь на подобное?"
    music Groove2_85
    img 17071
    with diss
    mt "..."
    mt "С другой стороны, я заработаю $ 50."
    mt "И, может быть, этот мерзавец Филипп станет платить и мне больше денег тоже..."
    img 23169
    with diss
    whore_number_1 "Ну что? Пойдем?"
    menu:
        "А если об этом кто-то узнает?!":
            pass
    img 17064
    with fade
    mt "Черт!"
    img 23170
    with diss
    m "А об этом никто не узнает?"
    img 23171
    with fade
    whore_number_1 "Не узнает."
    whore_number_1 "Я никому не рассказываю о своей подработке у Филиппа."
    whore_number_1 "Пошли."
    $ monicaShlut1PhillipBlowjob1 = True # Моника согласилась на блоуджоб Филиппу со шлюхой номер 1
    # заходят в дом Филиппа
    return


# Моника зашла в гостиную Филиппа со шлюхой номер 1, согласившись помочь ей удовлетворить его
label ep211_dialogues7_Phillip_home_2:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 17075
    with fadelong
    w
    img 16384
    with fade
    mt "Мне даже думать противно о том, что мне предстоит сейчас сделать..."
    mt "Чтобы заработать какие-то жалкие 50 долларов."
    $ menu_corruption = [0, philipThreesomeCorruptionRequired]
    menu:
        "Двойной минет.":
            return 1
        "Групповой секс." if monicaShlut1PhillipBlowjob2 == True:
            return 2
    return

# если выбран пункт 'Двойной минет'
label ep211_dialogues7_Phillip_home_3:
    call check_skip_scene("ep211_dialogues7_Phillip_home_2") from _rcall_check_skip_scene
    if _return == True:
        return True
    # Филипп сидит на диване перед телеком, Моника и шлюха стоят перед ним
    music Groove2_85
    img 17077
    with fade
    philip "Почему так долго?"
    philip "И что здесь делает субботняя шлюха номер 2?"
    philip "Я велел этой шлюхе приходить ко мне через неделю..."
    philip "А субботняя шлюха номер 1 давно уже должна держать во рту мой член."
    img 16440
    with diss
    mt "Козел!!!"
    mt "!!!"
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            music Pyro_Flow
            img 16386
            with fade
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 17078
            with diss
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            sound highheels_short_walk
            img 16418
            with fade
            # Моника уходит
            return False
        "Промолчать.":
            pass
    # Моника стоит перед ним в нерешительности, шлюха номер 1 ведет себя с Филиппом уверенно
    m "..."
    music Hidden_Agenda
    img 17079
    with fade
    whore_number_1 "Я решила устроить тебе небольшой сюрприз..."
    whore_number_1 "Если ты, конечно, не против."
    music Groove2_85
    img 17080
    with diss
    philip "Не люблю сюрпризы."
    philip "Что ты там придумала?"
    whore_number_1 "Я думаю, тебе понравится..."
    # шлюха номер 1 подходит к Филиппу, садится перед ним на колени, достает его член
    sound highheels_short_walk
    img 17081
    with fade
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 17082
    with fadelong
    philip "А шлюха номер 2 будет стоять и смотреть?"
    philip "Это и есть твой сюрприз, шлюха номер 1?"
    whore_number_1 "Она тоже будет сосать твой член."
    img 17083
    with fade
    philip "Я не собираюсь ей за это платить."
    whore_number_1 "Она сегодня сделает это за бесплатно."
    whore_number_1 "Я попросила ее сделать это."
    img 17084
    with diss
    w
    music Power_Bots_Loop
    img 17085
    with diss
    mt "Фу! Это так мерзко!"
    mt "!!!"
    mt "И как мы будем делать это вдвоем?!"
    # облизывает его член и поворачивается к Монике
    music Loved_Up
    img 17086
    with fade
    w
    img 17087
    with diss
    whore_number_1 "Иди сюда..." # и снова принимается за работу
    mt "..."
    $ menu_corruption = [0, monicaPhilipDoubleBlowjobCorruptionRequired]
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            music Pyro_Flow
            img 17088
            with fade
            mt "Я не могу пойти на это!"
            img 17089
            with diss
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            sound highheels_short_walk
            img 16418
            with fade
            return False
        "Сделать Филппу минет вместе с шлюхой номер 1.":
            $ monicaShlut1PhillipBlowjob2 = True # Моника делала минет Филиппу со шлюхой номер 1
            pass
    $ renpy.free_memory()
    # Моника смотрит на то, как шлюха номер 1 облизывает член
    music Groove2_85
    img 17090
    with fade
    mt "Ненавижу этого мерзавца!"
    mt "!!!"
    # подходит к нему и нерешительно садится рядом со шлюхой
    # тот, откинувшись на диван, самодовольно ухмыляется и смотрит на своих шлюх
    img 17091
    with diss
    philip "Уверен, что идея с сюрпризом принадлежала не шлюхе номер 2..."
    philip "Она вряд ли додумалась бы до такого..."
    philip "Субботняя шлюха номер 1 молодец."
    philip "Она старается сделать мне приятное."
    philip "Шлюха номер 2, чего ты ждешь? Приступай!"
    # Шлюха рукой наклоняет голову Моники
    # Моника начинает тоже его облизывать
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 17110
    with fadelong
    w
    img 17111
    with fade
    w
    img 17112
    with diss
    w
    sound vjuh3
    img 17113
    with diss
    w
    music stop
    music2 Loved_Up

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_1_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

#    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    img 17114
    with diss
    mt "Это так... Грязно..."
    mt "Не могу поверить, что я делаю это."
    # сама продолжает, одна берет член в рот и двигает головой, вторая облизывает мошонку (Моника)
    # Шлюха продолжает рукой направлять Монику

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_1_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17115
    with fade
    philip "Ммммм..."
    img 17116
    with diss
    philip "Как же мои субботние шлюхи стараются..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_1_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_3.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_1_3
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_1_4 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_4.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17117
    with fade
    w
    sound snd_slap1
    img 17118
    with hpunch
    philip "Даааа... Вот так..."

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Blowjob_1_5 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_5.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Blowjob_1_5
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17119
    with fade
    philip "Шлюхи готовы за деньги сделать все..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_1_6 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_6.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_1_6
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_1_7 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_7.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_1_7
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17120
    with diss
    philip "Ммммм..."

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_1_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Blowjob_1_8 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_1_8.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Blowjob_1_8
        with fade
        wclean
    stop music
    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Groove2_85
    img 17121
    with diss
    philip "А теперь мои субботние шлюхи поменяются местами."
    # Моника стоит на коленях, вытирая губы недовольно
    # Шлюха смотрит на Филиппа, на Монику, затем берет и рукой направляет голову Моники Филиппу на член.
    # теперь Моника сосет, а шлюха облизывает его
    # Шлюха рукой заставляет Монику взять член очень глубоко. (Можно даже применить морф горла, в blowjob что-то там, в быстром меню)
    music Pyro_Flow
    img 17122
    with fade
    w
    img 17123
    with diss
    sound highheels_short_walk
    w
    img 17124
    with fade
    w
    img 17125
    with diss
    w
    sound vjuh3
    img 17126
    with diss
    philip "Даааа..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_2_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_2_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17127
    with fade
    philip "Еще... Еще..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_2_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17128
    with diss
    philip "Вот так..."

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Blowjob_2_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_3.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Blowjob_2_3
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17129
    with fade
    philip "Аааа..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_2_4 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_4.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_2_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    music2 Loved_Up2
    img 17130
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_2_5 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_5.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_2_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17131
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Blowjob_2_6 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_6.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Blowjob_2_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17132
    with fade
    w

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Blowjob_2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Blowjob_2_7 = Movie(play="video/v_Monica_WhoreN1_Philip_Blowjob_2_7.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Blowjob_2_7
        with fade
        wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17133
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    philip "Аааааааа..."
    img 17134
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    philip "ААААААА!!!" # кончает им на лица-?
    img 17135
    with diss
    w
    # Моника и шлюха номер 1 отстраняются от него, Моника брезгливо вытирает рот
    $ add_corruption(monicaPhilipVisitDoubleBlowjobCorruption, "monicaPhilipVisitDoubleBlowjobCorruption" + str(day))
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 17137
    with fadelong
    whore_number_1 "Ну как тебе мой сюрприз?" # игриво
    img 17136
    with fade
    philip "Молодец, шлюха номер 1. Хорошая идея..."
    philip "Вот, держи 400 долларов."
    img 17138
    with diss
    mt "400?! Он дал ей 400 долларов?!"

#    mt "Хочу забрать деньги и уйти отсюда."
#    mt "И забыть об этом поскорее!"
#    mt "Ни за что не соглашусь еще раз на подобное извращенство!"
    # Филипп дает деньги шлюхе номер 1
    img 17139
    with fade
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 1 может забрать свои деньги."
    philip "А субботняя шлюха номер 2 недостаточно старалась..."
    img 17140
    with diss
    philip "Тем более, сегодня не ее очередь получать деньги."
    philip "Поэтому она сегодня ничего не заработала."
    music Pyro_Flow
    mt "!!!"
    menu:
        "Почему я ничего не заработала?!":
            img 17141
            with fade
            m "Филипп, я делала тоже самое, что и она!"
            m "Почему я не заработала денег?!"
            m "?!?!?!"
            # смотрит на нее
            music Groove2_85
            img 17142
            with diss
            philip "???"
            philip "Моей субботней шлюхе номер 2 нужны деньги?"
            philip "Приходи через неделю."
            # отворачивается
            music Power_Bots_Loop
            img 17143
            with fade
            mt "Вот мерзавец!!!"
            mt "Жадный ублюдок!!!"
            return True
        "Уйти.":
            pass
    music Groove2_85
    img 17144
    with fade
    philip "Можете идти."
    music Power_Bots_Loop
    img 17143
    with diss
    mt "Сволочь!"
    mt "!!!"
    # шлюха номер 1 забирает деньги и они уходят
    return

# улица возле дома Филиппа после двойного блоуджоба
label ep211_dialogues7_Phillip_home_4:
    # Моника разговаривает с субботней шлюхой номер 1
    music Pyro_Flow
    img 23174
    with fade
    m "Это было мерзко!"
    m "!!!"
    music Groove2_85
    img 17072
    with diss
    whore_number_1 "Зато мы заработали денег."
    whore_number_1 "Вот твои 50 баксов, как и договаривались..."
    $ add_money(50.0)
    # дает ей деньги
    img 17073
    with fade
    m "Это несправедливо! Он дал тебе 400!!!"
    img 17074
    with diss
    whore_number_1 "Ты сама согласилась сделать это за 50 баксов!"
    whore_number_1 "Тебя никто не заставлял!"
    music Pyro_Flow
    img 23168
    with fade
    mt "Сучка!!!"
    mt "!!!"
    music Groove2_85
    whore_number_1 "Все, мне пора."
    whore_number_1 "До встречи."
    # шлюха 1 уходит
    return


# мысли Моники после двойного блоуджоба, шлюха 1 отдала ей 50 баксов и ушла
label ep211_dialogues7_Phillip_home_5:
    # не рендерить!
    mt "Почему этот мерзавец Филипп платит любой другой дешевой шлюхе меньше чем мне?!"
    mt "!!!"
    mt "Я заставлю пожалеть мерзавца Филиппа об этом!"
    mt "Он еще будет умолять меня о прощении!"
    mt "Ненавижу!!!"
    mt "!!!"
    return
