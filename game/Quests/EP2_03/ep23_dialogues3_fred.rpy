# Если на фитнесе было достаточно посещений (в идеале посмотрены все девочки), то появляется Фред в конце занятия.
# Фред говорит Монике что ей идет эта униформа. Моника злится и спрашивает что Фреду надо от нее.
# Фред говорит что нужен совет в выборе попы. Какой попы?
# Одной из тех что там занимается.
# Какую бы Вы предпочли, Миссис Бакфетт?
# Бетти, Стефани или Ребекку?
label ep23_dialogues3_1:
    music Groove2_85
    img 8618
    with fade
    w
    img 8619
    with fade
    w
    img 8620
    with fade
    fred "..."
    img 8621
    m "Фред!?"
    "Что ты здесь делаешь?! Нерадивый водитель!"
    "Твое место у машины!"
    img 8622
    fred "О! Миссис Бакфетт!"
    "Все забываю сказать что Вам очень идет эта униформа..."
    img 8623
    m "!!!"
    img 8624
    m "Что тебе здесь надо, Фред?!"
    img 8625
    fred "О! Миссис Бакфетт!"
    "Мне нужен Ваш совет..."
    m "Какой еще совет?!"
    fred "Совет в выборе попы..."
    music Pyro_Flow
    img 8626
    m "Какой еще попы?! Что ты несешь?!"
    "Иди на свое рабочее место, немедленно!"
    music Groove2_85
    img 8627
    with fade
    fred "Одной попы из тех, которые там занимаются сейчас."
    img 8628
    fred "Какую попу Вы бы предпочли, Миссис Бакфетт?"
    music Loved_Up
    img 8629
    with fade
    fred "Бетти..."
    img 8630
    with fade
    fred "Стефани..."
    img 8631
    with fade
    fred "или Ребекку?"
    music Groove2_85
    img 8632
    with fade
    mt "Вот мерзавец!!!"
    "Как он смеет разговаривать со мной о таких вещах!"
    mt "..."
    mt "Хотя..."
    # Моника говорит что бери Бетти, эта дура как раз заслуживает такого болвана как ты.
    # Фред говорит что это будет непрофессионально, т.к. он у нее работает.
    # Моника говорит что добраться до других у него шансов есть.
    # Фред говорит что Моника поможет ему в этом. Моника спрашивает с какой стати.
    # Фред отвечает что Моника что-нибудь придумает, потому что иначе ей придется пожертвовать своей попой.
    # Хватает ее за зад.
    img 8633
    m "Бери Бетти, эта дура как раз заслуживает такого болвана как ты!"
    img 8634
    fred "Миссис Бакфетт, это будет непрофесионально, так как я работаю у нее."
    "А Вы знаете, я профессионал!"
    img 8635
    m "В любом случае, добраться до остальных у тебя шансов нет!"
    img 8636
    fred "У меня есть шансы, Мэм..."
    fred  "Ведь Вы поможете мне в этом..."
    music Pyro_Flow
    img 8637
    with fade
    m "С какой стати я тебе будут помогать в твоих похотливых фантазиях, Фред?!"
    m "Тебе мало что ты уже натворил, подлец?!"
    img 8636
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    img 8638
    with fade
    m "Я не собираюсь разговаривать с тобой об этом!"
    music Groove2_85
    img 8639
    with fade
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    img 8640
    fred "Обязательно..."
    img 8641
    fred "В противном случае, Вам придется пожертвовать своей попой для этого..."
    sound Jump2
    img 8642
    with Dissolve(0.5)
    # Хватает ее за зад.
    w
    img 8643
    w
    if monicaBettyPanties == False:
        img 8668
    else:
        if monicaBettyPantiesId == 1:
            img 8669
        if monicaBettyPantiesId == 2:
            img 8670
        if monicaBettyPantiesId == 3:
            #before subd
            img 8671
        if monicaBettyPantiesId == 4:
            img 8672
        if monicaBettyPantiesId == 5:
            img 8673
    with fade
    w
    img 8644
    with fade
    w
    img 8645
    music Power_Bots_Loop
    # Моника поворачивается и, в зависимости от bitchness дает пощечину, либо дает по яйцам ногой.
    menu:
        "Ударить Фреда между ног!" if monicaBitch == True:
            img 8654
            with Dissolve(0.5)
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            "НИЧТОЖЕСТВО!!!"
            sound snd_kick_fred1
            img 8655
            with Dissolve(0.5)
            "ПОЛУЧАЙ!!!"
            img 8656
            with Dissolve(0.5)
            "НА!!!"
            #bodyfall
            #fade
            sound snd_bodyfall
            img 8657
            with fade
            fred "АААААххххх!!!"
            fred "Что Вы сделали, Миссис Бакфетт..."
            fred "Вы применили насилие!"
            img 8658
            "Это же..."
            "Это же... Больно..."
            # Фред падает, если ударили.
            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            img 8659
            with fade
            m "Сейчас я воткну каблук в твой рот, мерзавец!"
            img 8660
            with fade
            w
            img 8661
            "Если ты сейчас же не уберешься отсюда!!!"
            if monicaBettyPanties == False:
                img 8662
            else:
                if monicaBettyPantiesId == 1:
                    img 8663
                if monicaBettyPantiesId == 2:
                    img 8664
                if monicaBettyPantiesId == 3:
                    #before subd
                    img 8665
                if monicaBettyPantiesId == 4:
                    img 8666
                if monicaBettyPantiesId == 5:
                    img 8667
            with fade
            "Ты забыл с кем связался! Ничтожество!"
            $ fredKickedByMonicaToBalls = True
        "Ударить Фреда между ног! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass

        "Дать пощечину Фреду." if monicaBitch == False:
            img 8646
            with Dissolve(0.5)
            sound snd_punch_face1
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            img 8647
            with Dissolve(0.5)
            sound snd_punch_face2
            #звук пощечины
            "НИЧТОЖЕСТВО!!!"
            #fade
            sound snd_bodyfall
            img 8648
            with fade
            fred "Айй!!"
            fred "Мои очки!"
            fred "Вы применили насилие!"

            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            img 8650
            with fade
            w
            img 8649
            m "Следующий удар будет гораздо больнее, мерзавец!"
            img 8651
            "Если ты сейчас же не уберешься отсюда!!!"
            img 8652
            with fade
            "Ты забыл с кем связался! Ничтожество!"
            $ fredKickedByMonicaToFace = True

        "Дать пощечину Фреду. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
            pass
    # Стефани и Ребекки нравятся слова Моники и они разговаривают с ней о том наконец-то увидели прежнюю Монику.
    # А то они уже стали сомневаться по поводу ее слов.
    # Моника говорит чтобы не сомневались.
    # После этого несколько меняется диалог при встрече подруг на фитнесе.

    #Фред убегает
    music stop
    img 8653
    with fade
    sound man_steps
    w
    #fade
    music BossaBossa
    img 8674
    with fade
    stephanie "Вау! Моника!"
    rebecca "Моника! Вот это да!"
    stephanie "Наконец-то мы узнаем нашу Монику!"
    rebecca "Да, Моника, а то мы уже начали сомневаться в тебе!"
    img 8675
    m "Я хочу предупредить Вас, девочки!"
    "Если кто-то будет сомневаться во мне, то последует за тем болваном!"
    img 8676
    stephanie "Нет, Моника! Пожалуйста не надо!"
    rebecca "Мы твои верные подруги, Хи-хи!"
    stephanie "Скорее завершай свое приключение."
    "Нам не терпится все узнать!"
    rebecca "Да, Моника!"
    "Про тебя можно снимать кино!"
    img 8677
    with fade
    mt "Да уж, про меня уже можно снимать кино, это точно..."
    img 8678
    with fade
    stephanie "Пока, Моника!"
    "Чмок!"
    rebecca "Пока, Моника!"
    "Чмок!"
    m "Пока, девочки!"
    return


label ep23_dialogues3_2:
    music Groove2_85
    img 7730
    with fade
    betty "Гуверантка! Где моя сумка с униформой?"
    img 7731
    betty "Быстро неси ее сюда!"

    img 7732
    betty "Что ты там копаешься?!"
    img 7733
    with fade
    m "Вот Ваша сумка, Миссис Робертс."

    # Бетти уходит в спортивном
    img 7734
    with fade
    betty "Можешь посидеть здесь или понаблюдать за мной."
    img 7735
    m "Спасибо, Миссис Робертс... Я посижу здесь..."
    img 7736
    w
    music BossaBossa
    img 7743
    with fade
    stephanie "Привет, Моника!"
    m "Привет, девочки!"
    img 7751
    rebecca "Моника, мы скучаем по тебе!"
    stephanie "Скажи нам сразу как только соберешься на наш девичник!"
    "Мы тебя ждем!"
    m "Хорошо, девочки!"
    return

label ep23_dialogues3_3:
    $ store_music()
    music Groove2_85
    # Фред, если к нему подойти у дома, смотрит на Монику.
    # Моника спрашивает хочет-ли он еще получить?
    # Фред делает вид что боится и что не хочет. Моника говорит чтобы тогда помалкивал.
    if day_time == "day":
        if cloth == "Governess":
            img 8680
        if cloth == "Whore":
            img 8679
    else:
        if cloth == "Governess":
            img 8681
        if cloth == "Whore":
            img 8682
    with fade
    m "Фред, ты на меня все-время смотришь..."
    m "Тебе показалось мало в прошлый раз?"
    "Ты хочешь получить еще?"
    fred "Нет, Мэм!"
    "Никак нет!"
    m "Вот и помалкивай! Болван!"
    $ restore_music()
    return

    # Когда Моника трет пятно, периодически вместо Бетти появляется Фред, который смотрит на нее.
    # Если Моника кликнет на Фреда, то оборачивается и говорит чтобы он проваливал, если не хочет получить еще.
    # Фред говорит что просто гуляет и ищет надо-ли где-то применить его профессионализм.
label ep23_dialogues3_4:
    $ store_music()
    music Groove2_85 high
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10554
        else:
            img 8683
    else:
        if monicaBettyPantiesId == 1:
            img 8684
        if monicaBettyPantiesId == 2:
            img 8685
        if monicaBettyPantiesId == 3:
            img 8686
        if monicaBettyPantiesId == 4:
            img 8687
        if monicaBettyPantiesId == 5:
            img 8688
    with fade
    w
    if monicaUnder == "Nude":
        fred "Вау! Какой вид, Миссис Бакфетт!"

    img 8689
    m "Фред! Что ты шляешься здесь?!"
    "Проваливай отсюда, пока не получил по зубам!"
    fred "Мэм! Я просто прогуливаюсь!"
    "Вы знаете, Я профессионал."
    img 8690
    with fade
    "И ищу вдруг где-то надо применить мой профессионализм!"
    img 8691
    m "Это точно не здесь, Фред!"
    if monicaUnder == "Nude":
        m "И не вздумай приближаться ко мне, мерзавец!"
    $ restore_music()
    return

label ep23_dialogues3_5:
    # В один из дней Бетти находится в спальне. Заходит Фред.
    # Бетти в белье (заранее определяется какое белье, запуск когда в определенном)
    # Бетти зло спрашивает что он тут делает?
    # Фред говорит что его послал Мистер Робертс, чтобы позвать Бетти, потому что он уезжает с Фредом по делам
    # и хочет поцеловать супругу перед отъездом.
    # Бетти спрашивает и что, ради этого он послал прислугу водителя в ее спальню?
    # Фред отвечает что вообще-то нет, просто кое-кто еще хочет ее поцелуя.
    # И снимает штаны.
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_14
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 8536
    with fade
    w
    img 8537
    with fade
    w
    img 8538
    with fade
    w
    img 8539
    betty "Фред?!"
    img 8540
    betty "Фред! Что ты делаешь здесь?! В спальне хозяев!"
    img 8541
    with fade
    fred "Миссис Робертс! Меня послал Мистер Робертс, чтобы я позвал Вас спуститься вниз к нему!"
    fred "Мистер Робертся собирается уезжать по делам, до вечера, и хочет поцеловать супругу перед отъездом!"
    img 8542
    betty "И что, ради этого от прислал прислугу водителя в нашу спальню?"
    img 8543
    fred "Мэм, вообще-то нет..."
    sound snd_zip
    #fade
    img 8544
    with fadelong
    "Просто кое-кто еще хочет Ваш поцелуй..."
    # И снимает штаны.

    # Бетти говорит что он сошел с ума? Здесь ходит Барди, не хватало чтобы он это увидел.
    # И что он вообще себе позволяет в ее спальне?
    # Фред отвечает что закрыл дверь и ведет себя профессионально, так как хозяйка богатого дома хочет поцеловать его член.
    # Бетти смотрит на Фреда, спускается и целует.
    # Фред говорит что хозяйка дома хочет взять член в рот поглубже. Бетти делает минет.
    # Фред кончает и говорит что спасибо, теперь можно идти к Мистеру Робертсу.
    img 8545
    with fade
    w
    img 8546
    with Dissolve(0.5)
    w
    img 8547
    betty "Фред?! Ты сошел с ума?!"
#    "Здесь ходит Барди! Не хватало чтобы он это увидел!"
    img 8548
    with fade
    betty "И что ты вообще себе позволяешь?!"
    sound hlup10
    img 8549
    with fade
    "Прямо в спальне хозяев дома!"
    img 8550
    fred "Мэм, я профессионал и поэтому предусмотрительно закрыл дверь."
    fred "Я веду себя профессионально, так как знаю что хозяйка богатого дома хочет этот член..."
    betty "!!!"
    menu:
        "Посмотреть вниз...":
            pass
        "В другой раз, Фред!":
            betty "В другой раз, Фред!"
            music stop
            img black_screen
            with Dissolve(2.0)
            return
    img 8551
    with fade
    betty "..."
    fred "..."
    img 8552
    betty "..."
    img 8553
    with fade
    w
    music Loved_Up
    img 8554
    with fade
    w
    img 8555
    with Dissolve(0.5)
    w
    img 8556
    with fade
    w
    img 8557
    with Dissolve(0.5)
    fred "Ну-же..."
    img 8558
    with fade
    w
    #dissolve
    img 8559
    with Dissolve(0.5)
    w
    music stop
    sound kiss2
    img 8560
    with Dissolve(0.5)
    w
    music snd_licking1
    img 8561
    w
    img 8562
    w
    img 8563
    w
    img 8564
    w
    img 8565
    with Dissolve(0.5)
    w

    $ bettyFredBedroomHasBlowjob = True
    # Бетти смотрит на Фреда, спускается и целует.
    music Loved_Up
    img 8566
    with fade
    fred "Хозяйка богатого дома хочет взять член в рот поглубже..."
    sound hlup19

    img 8567
    betty "..."
    img 8568
    with fade
    w
    img 8569
    with fade
    w
    #video
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(0.7)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_1 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_1.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_1
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_2 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_2.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_2
    wclean
    stop music
    $ renpy.music.set_volume(0.7)
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_3 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_3.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_4 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_4.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_5 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_5.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_6 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_6.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_6
    wclean
    $ renpy.music.set_volume(1.0)
    music stop
    music Loved_Up
    img 8570
    with fade
    w
    img 8571
    with fade
    w
    img 8572
    with fade
    w
    img 8573
    with fade
    sound bulk1
    fred "ААААаааааххх!"
    #longfade
    music Groove2_85
    img 8574
    with fadelong
    fred "Спасибо, Мэм."
    "Теперь можно идти к Мистеру Робертсу."
    img 8575
    with Dissolve(0.5)
    w
    img 8576
    w

    # Бетти говорит что куда это он собрался, давай быстрее и тд. Повторяется сцена секса (можно взять из прошлой версии)
    # Фред кончает. Бетти говорит что не вздумай снова кончить на лицо, раздается крик Ральфа: Бетти, ты где?
    # Фред снова кончает на лицо, Бетти зло смотрит и вытирает его.

    img 8577
    with fade
    menu:
        "Куда это ты собрался?!":
            pass
        "Пойдем...":
            betty "Пойдем..."
            jump ep23_dialogues3_5a

    $ bettyFredBedroomHasSex = True
    betty "Куда это ты собрался?!"
    sound snd_fabric1
    img 9615
    with fade
    betty "А как же я?!"
    img 8578
    sound snd_bodyfall
    #звук падающих предметов
    w
    music Loved_Up2
    img 8579
    with fade
    betty "Давай быстрее!"
    img 8580
    fred "Как скажете, Мэм!"
    "Вы мой Босс!"
    img 8581
    betty "И не забудь вытереть свой член от спермы, прежде чем начнешь!"
    #fade
    img 8582
    with fade
    fred "Да, Мэм! Конечно!"
    img 8583
    betty "Вовсе необязательно делать это о мою занавеску!"
    #fade
    img 8584
    with fade
    fred "Простите, Мэм!"
    img 8585
    fred "Я приношу свои извинения."
    img 8586
    fred "Как профессионал!"
    #sex
    sound hlup10
    img 8587
    with fade
    w
    img 8588
    w
    img 8589
    w
    music stop
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.8)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_1 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_1.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_1
    with fade
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.8)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_2 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_2.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_2
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_3 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_3.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_3
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_4 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_4.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_4
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_5 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_5.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_5
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_6 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_6.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_6
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_7 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_7.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_7
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.7)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_8 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_8.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_8
    wclean

    music Loved_Up2
    $ renpy.music.set_volume(1.0)
    img 8590
    with fade
    w
    img 8591
    with fade
    w
    img 8592
    with fade
    fred "ААААаааааххх!"
    music Groove2_85
    img 8593
    betty "Фред! Не вздумай кончить в меня!"
    img 8594
    with Dissolve(0.5)
    betty "..."
    #fade
    img 8595
    ralph "Бетти!"
    img 8596
    betty "И не вздумай кончить мне на лицо, как в прошлый раз!"
    img 8597
    with fade
    music stop
    ralph "Бетти! Ты где?"
    sound bulk1
    img 8598
    with fade
    fred "ААААаааааххх!"
    #fade
    music Groove2_85
    img 8599
    with fadelong
    betty "!!!"
    img 8600
    fred "..."
    img 8601
    with fade
    betty "..."
    img 8602
    w
    #fade
    img 8603
    with fade
    w
    ralph "Бетти! Ты где?"
    # Кричит в ответ: Ральф, я иду, хватит орать на весь дом!
    # Они спускаются вниз. Фред говорит Ральфу что дверь в комнату Бетти была закрыта и он ждал, пока она закончит макияж.
    # Бетти спрашивает Ральфа зачем он ее звал.
    # Ральф отвечает что едет на важную встречу и хотел чтобы Бетти поцеловала его (Бетти только что была вся в сперме)
    # Бетти решает целовать его или нет. Если целовать, то в губы или в щеку.
    music Pyro_Flow
    img 8604
    with Dissolve(0.5)
    betty "Ральф, я иду!"
    "Хватит орать на весь дом!"

label ep23_dialogues3_5a:
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Минуту спустя...")) from _call_textonblack_15
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 8605
    with fade
    fred "Мистер Робертс, дверь в комнату Миссис Робертс была закрыта."
    "Поэтому я ждал, пока она закончит наносить макияж."
    img 8606
    betty "Ральф, зачем ты звал меня?"
    img 8607
    ralph "Бетти, я еду на важную встречу и хочу чтобы ты поцеловала меня, любимая!"
    "Мне осталось надеть костюм и я выезжаю!"
    img 8608
    with fade
    betty "..."
    img 8609
    fred "..."
    menu:
        "Не целовать Ральфа.":
            $ bettyNotKissedRalphSperm = True
            music Pyro_Flow
            img 8610
            with fade
            betty "Ральф! Ты не заслужил моего поцелуя!"
            "Ты плохо ведешь себя, кушаешь не вовремя и не помогаешь мне ни в чем!"
            img 8611
            ralph "..."
            betty "Когда ты заслужишь, я поцелую тебя!"
        "Поцеловать Ральфа в щеку.":
            music Loved_Up
            $ bettyKissedRalphSpermCheek = True
            img 8612
            with fade
            betty "Да, любимый, иди я тебя поцелую!"
            img 8613
            with fade
            sound kiss2
            betty "Чмок!"
            img 8614
            ralph "..."
        "Поцеловать Ральфа в губы.":
            music Loved_Up
            $ bettyKissedRalphSpermLips = True
            img 8612
            with fade
            betty "Да, любимый, иди я тебя поцелую!"
            img 8615
            with fade
            sound kiss2
            betty "Чмок!"
            img 8617
            ralph "..."
            img 8616
            sound kiss2
            w

    music stop
    img black_screen
    with Dissolve(2.0)
    return

label ep23_dialogues3:
    return
