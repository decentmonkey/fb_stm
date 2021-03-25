
label gallery_ep22_photoshoot4:
    music Groove2_85
    $ shotsAmount = PS4_shots_amount
    $ shotsTotalAmount = 27

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True


    # переоделась
    img 8840
    m "Алекс, это что?"
    alex_photograph "Миссис Бакфетт, это наряд Розы Надежды!"
    img 8841
    m "Ладно, Алекс. Надеюсь эта роза не уколет меня своим шипом!"
    "Иначе Бифу придется выплатить мне компенсацию за это!"

    music stop
    img 8842
    with fade
    alex_photograph "Мотор!"

    label gallery_ep22_photoshoot4_pose1:

        #кадр
        img 8842
        #up
#        img 8843
        #side
#        img 8844
        #down
#        img 8845


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8846
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump gallery_ep22_photoshoot4_pose2
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8843
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_33
            w
            jump gallery_ep22_photoshoot4_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8844
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_34
            w
            jump gallery_ep22_photoshoot4_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8845
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_35
            w
            jump gallery_ep22_photoshoot4_pose1


        #кадр
#        img 8846
        #up
#        img 8847
        #side
#        img 8848
        #down+
#        img 8849
    label gallery_ep22_photoshoot4_pose2:
        img 8846

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8850
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump gallery_ep22_photoshoot4_pose3
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8847
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_36
            w
            jump gallery_ep22_photoshoot4_pose2
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8848
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_37
            w
            jump gallery_ep22_photoshoot4_pose2
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8849
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot1_corruption_required:
                m "Алекс! Хватит!"
                call corruption_required(PS4_monica_shot1_corruption_required) from _rcall_corruption_required
                jump gallery_ep22_photoshoot4_pose2
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_38
            # $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot1_progress")
            w
            jump gallery_ep22_photoshoot4_pose2


        #кадр
#        img 8850
        #up
#        img 8851
        #side
#        img 8852
        #down
#        img 8853
    label gallery_ep22_photoshoot4_pose3:
        img 8850

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8854
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump gallery_ep22_photoshoot4_pose4
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8851
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_39
            w
            jump gallery_ep22_photoshoot4_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8852
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_40
            w
            jump gallery_ep22_photoshoot4_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8853
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_41
            w
            jump gallery_ep22_photoshoot4_pose3


        #кадр
#        img 8854
        #up
#        img 8855
        #side
#        img 8856
        #down
#        img 8857

    label gallery_ep22_photoshoot4_pose4:
        img 8854

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8858
            with fadelong
            #++
            #кадр+ кладет руку на грудь!!!!!!
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            if corruption < PS4_monica_pose5_corruption_required:
                music Groove2_85
                m "Алекс! Я не собираюсь трогать себя за грудь на камеру!"
                "И это не обсуждается!"
                call corruption_required(PS4_monica_pose5_corruption_required) from _rcall_corruption_required_1
                return
            jump gallery_ep22_photoshoot4_pose5
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8855
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_42
            w
            jump gallery_ep22_photoshoot4_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8856
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_43
            w
            jump gallery_ep22_photoshoot4_pose4
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8857
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_44
            w
            jump gallery_ep22_photoshoot4_pose4


        #кадр+ кладет руку на грудь
#        img 8858
        #up
#        img 8859
        #side
#        img 8860
        #down+
#        img 8861
    label gallery_ep22_photoshoot4_pose5:
        img 8858

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8862
            with fadelong
            #++
            #кадр+ кладет руку на грудь!!!!!!
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump gallery_ep22_photoshoot4_pose6
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8859
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_45
            w
            jump gallery_ep22_photoshoot4_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8860
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_46
            w
            jump gallery_ep22_photoshoot4_pose5
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8861
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot2_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS4_monica_shot2_corruption_required) from _rcall_corruption_required_2
                jump gallery_ep22_photoshoot4_pose5
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_47
            # $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot2_progress")
            w
            jump gallery_ep22_photoshoot4_pose5

        #кадр
#        img 8862
        #up
#        img 8863
        #side
#        img 8864
        #down+
#        img 8865

    label gallery_ep22_photoshoot4_pose6:
        img 8862

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8866
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump gallery_ep22_photoshoot4_pose7
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose6
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8863
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_48
            w
            jump gallery_ep22_photoshoot4_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8864
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_49
            w
            jump gallery_ep22_photoshoot4_pose6
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8865
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot3_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS4_monica_shot3_corruption_required) from _rcall_corruption_required_3
                jump gallery_ep22_photoshoot4_pose6
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_50
            # $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot3_progress")
            w
            jump gallery_ep22_photoshoot4_pose6

        #кадр
#        img 8866
        #up
#        img 8867
        #side
#        img 8868
        #down+
#        img 8869

    label gallery_ep22_photoshoot4_pose7:
        img 8866

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8870
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump gallery_ep22_photoshoot4_pose8
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose7
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8867
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_51
            w
            jump gallery_ep22_photoshoot4_pose7
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8868
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_52
            w
            jump gallery_ep22_photoshoot4_pose7
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8869
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot4_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS4_monica_shot4_corruption_required) from _rcall_corruption_required_4
                jump gallery_ep22_photoshoot4_pose7
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_53
            # $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot4_progress")
            w
            jump gallery_ep22_photoshoot4_pose7

        #кадр
#        img 8870
        #up
#        img 8871
        #side
#        img 8872
        #down+
#        img 8873

    label gallery_ep22_photoshoot4_pose8:
        img 8870

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8874
            with fadelong
            #кадр - жесткая поза
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            if corruption < PS4_monica_pose8_corruption_required:
                m "Алекс! Я не буду вставать в такую развратную позу!"
                "И это не обсуждается!"
                call corruption_required(PS4_monica_pose8_corruption_required) from _rcall_corruption_required_5
                return
            jump gallery_ep22_photoshoot4_pose9
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose8
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8871
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_54
            w
            jump gallery_ep22_photoshoot4_pose8
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8872
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_55
            w
            jump gallery_ep22_photoshoot4_pose8
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8873
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot5_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS4_monica_shot5_corruption_required) from _rcall_corruption_required_6
                jump gallery_ep22_photoshoot4_pose8
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_56
            # $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot5_progress")
            w
            jump gallery_ep22_photoshoot4_pose8



        #кадр - жесткая поза
#        img 8874
        #up
#        img 8876
        #side
#        img 8875
        #down+
#        img 8877
#        img 8878

    label gallery_ep22_photoshoot4_pose9:
        img 8874

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            return
#            jump gallery_ep22_photoshoot4_end
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot4_pose9
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8876
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_57
            w
            jump gallery_ep22_photoshoot4_pose9
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8875
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_58
            w
            jump gallery_ep22_photoshoot4_pose9
        if result == "down":
            #down+
            sound camera_lens1
            img 8877
            with Dissolve(0.2)
            if corruption < PS4_monica_shot6_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS4_monica_shot6_corruption_required) from _rcall_corruption_required_7
                jump gallery_ep22_photoshoot4_pose9
            w
            call photoshop_flash() from _rcall_photoshop_flash_35
            w
            $ photoImage = 8878
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_59
            # $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot6_progress")
            w
            jump gallery_ep22_photoshoot4_pose9

label gallery_ep22_photoshoot4_end:

    hide screen photoshoot_camera_icon
    hide screen photoshoot

    music Stealth_Groover
    img 8879
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 8880
    with fade
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot4_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call gallery_ep23_photoshoot4_casting() from _rcall_gallery_ep23_photoshoot4_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot4_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot4_casting_corruption_required:
            pass

    return

label gallery_ep23_photoshoot4_casting:
    music Groove2_85
    sound highheels_short_walk
    img 9470
    with fadelong
    w
    img 9471
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 9472
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 9473
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 9474
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Роза Надежды..."
            biff "Что Роза Надежды хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 4
            call gallery_8442() from _rcall_gallery_8442
            img 9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 4
            $ chickMode = False
            call gallery_8442() from _rcall_gallery_8442_1
            img 9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return

##########################################################
##########################################################

label gallery_ep26_photoshoot_suit6:
    music Groove2_85
    $ shotsAmount = PS6_shots_amount
    $ shotsTotalAmount = 33

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20001
    with fadelong
    m "Что это, Алекс?"
    # Что это?
    img 20002
    with diss
    m "Это что, называется костюм для съемок?"
    # Это что, называется костюм для съемок?
    img 20003
    with diss
    # А это что такое?
    m "А это что такое?"
    img 20004
    with fade
    # Миссис Бакфетт, это реквизит и тд
    alex_photograph "Миссис Бакфетт, этот костюм называется Алая Жемчужина"
    alex_photograph "А этот реквизит олицетворяет раковину, в которой находится изысканная жемчужина!"
    alex_photograph "Это будет замечательная сцена, Миссис Бакфетт!"
    img 20005
    with diss
    # И что мне делать на этой кушетке?
    m "И что мне делать на этой... раковине?"
    img 20006
    with fade
    # Проходить фотосессию
    alex_photograph "Миссис Бакфетт, Вам надо принимать различные позы."
    alex_photograph "Читателям должно понравиться то, как Вы будете выглядеть!"

    img 20007
    with fade
    # Ладно, Алекс!
    # Только на этот раз без пошлых поз!
    m "Ладно, Алекс."
    m "Только на этот раз без пошлых поз!"

    music Molten_Alloy
    img 20008
    with diss
    alex_photograph "Конечно, Миссис Бакфетт! Все будет очень прилично, как обычно!"
    alex_photograph "Итак, мотор!"
    music stop
    img 20009
    with fadelong

$ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose1"
$ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose2"
label gallery_ep26_photoshoot_suit6_pose1:
    #кадр
    img 20009
    # up
#    img 20011
    # side
#    img 20010
    # down
#    img 20012
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20013
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20011
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_60
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20010
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_61
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20012
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_62
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit6_pose2:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose2"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose3"
    # кадр
    img 20013
    # up
#    img 20014
    # side
#    img 20015
    # down
#    img 20016
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        # кадр+
        img 20017
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        if corruption < PS6_monica_pose3_corruption_required:
            m "Алекс! Я не буду вставать в позу, будто показываю задницу!"
            "И это не обсуждается!"
            call corruption_required(PS6_monica_pose3_corruption_required) from _rcall_corruption_required_8
            return
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot1_progress")
        m "Алекс, мне не нравится это поза!"
        m "Постарайся поменьше фокусировать камеру на месте ниже спины!"
        alex_photograph "Конечно, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20014
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_63
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20015
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_64
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20016
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_65
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit6_pose3:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose3"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose4"
    # кадр +
    img 20017
    # up
#    img 20019
    # side
#    img 20018
    # down
#    img 20020
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20021
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20019
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_66
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20018
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_67
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20020
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_68
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit6_pose4:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose4"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose5"
    # кадр
    img 20021
    # up
#    img 20022
    # side +
#    img 20024
    # down
#    img 20023
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20025
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20022
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_69
        w
        jump expression photoPoseLabel
    if result == "side":
        #side+
        sound camera_lens1
        $ photoImage = 20024
        img photoImage
        with Dissolve(0.2)
        if corruption < PS6_monica_shot1_corruption_required:
            m "Алекс! Забудь про такие ракурсы!"
            call corruption_required(PS6_monica_shot1_corruption_required) from _rcall_corruption_required_9
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_70
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot3_progress")
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20023
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_71
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit6_pose5:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose5"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose6"
    # кадр
    img 20025
    # up
#    img 20026
    # side
#    img 20027
    # down
#    img 20028

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20029
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20026
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_72
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20027
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_73
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20028
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_74
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit6_pose6:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose6"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose7"
    # кадр
    img 20029
    # up
#    img 20030
    # side
#    img 20031
    # down
#    img 20032

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20033
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20030
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_75
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20031
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_76
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20032
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_77
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit6_pose7:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose7"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose8"

    # кадр
    img 20033
    # up
#    img 20034
    # side
#    img 20035
    # down +
#    img 20036
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20037
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20034
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_78
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20035
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_79
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20036
        img photoImage
        with Dissolve(0.2)
        m "Алекс! Зачем ты оттуда фотографируешь?"
        m "Что ты хочешь там увидеть?!"
        if corruption < PS6_monica_shot2_corruption_required:
            call corruption_required(PS6_monica_shot2_corruption_required) from _rcall_corruption_required_10
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я фотографирую Ваши ножки!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_80
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot4_progress")
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit6_pose8:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose8"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose9"
    # кадр
    img 20037
    # up
#    img 20038
    # side
#    img 20039
    # down +
#    img 20040
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20041
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20038
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_81
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20039
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_82
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20040
        img photoImage
        with Dissolve(0.2)
        if corruption < PS6_monica_shot3_corruption_required:
            m "Алекс! Я не буду делать такой кадр!"
            call corruption_required(PS6_monica_shot3_corruption_required) from _rcall_corruption_required_11
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_83
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot5_progress")
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit6_pose9:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose9"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose10"

    # кадр
    img 20041
    # up
#    img 20042
#    img 20043
    # side
#    img 20044
#    img 20045
    # down +
#    img 20046
#    img 20047
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20048
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20042
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_36
        w
        $ photoImage = 20043
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_84
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20044
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_37
        w
        $ photoImage = 20045
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_85
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20046
        with Dissolve(0.2)
        if corruption < PS6_monica_shot4_corruption_required:
            m "Алекс! Забудь про такие ракурсы!"
            call corruption_required(PS6_monica_shot4_corruption_required) from _rcall_corruption_required_12
            jump expression photoPoseLabel
        w
        call photoshop_flash() from _rcall_photoshop_flash_38
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot6_progress")
        w
        $ photoImage = 20047
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_86
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit6_pose10:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose10"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose11"
    # кадр
    img 20048
    # up
#    img 20049
#    img 20050
#    img 20051
    # side
#    img 20052
#    img 20053
#    img 20054
    # down+
#    img 20055
#    img 20056
    #+
#    img 20057
#    img 20058
#    img 20059
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
    # кадр +
        img 20060
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        m "Алекс! Я не буду вставать в такую развратную позу!"
        "И это не обсуждается!"
        if corruption < PS6_monica_pose10_corruption_required:
            call corruption_required(PS6_monica_pose10_corruption_required) from _rcall_corruption_required_13
            return
        alex_photograph "Миссис Бакфетт, это сюжетная поза."
        alex_photograph "Раковина, как-бы раскрывается, обнажая жемчужину!"
        m "Я не собираюсь обнажать никакую... жемчужину!"
        alex_photograph "Миссис Бакфетт, не волнутесь, я буду фотографировать только сбоку!"
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot7_progress")
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20049
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_39
        w
        img 20050
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_40
        w
        $ photoImage = 20051
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_87
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20052
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_41
        w
        img 20053
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_42
        w
        $ photoImage = 20054
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_88
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20055
        with Dissolve(0.2)
        m "Алекс! Я не буду делать такой кадр!"
        m "Что это за поза?"
        if corruption < PS6_monica_shot5_corruption_required:
            call corruption_required(PS6_monica_shot5_corruption_required) from _rcall_corruption_required_14
            jump expression photoPoseLabel
        alex_photograph "Это прекрасная поза, Миссис Бакфетт!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_43
        w
        img 20056
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_44
        w
        img 20057
        with Dissolve(0.2)
        m "Алекс! Хватит!"
        m "Что ты там хочешь сфотографировать?!"
        if corruption < PS6_monica_shot6_corruption_required:
            call corruption_required(PS6_monica_shot6_corruption_required) from _rcall_corruption_required_15
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я хочу сфотографировать Ваш чудесный педикюр!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_45
        w
        img 20058
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_46
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot8_progress")
        w
        $ photoImage = 20059
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_89
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit6_pose11:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit6_pose11"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit6_pose12"
    # кадр +
    img 20060
    # up
#    img 20061
#    img 20062
#    img 20063
    # side
#    img 20064
#    img 20065
#    img 20066
    # down +
#    img 20067
#    img 20068
#    img 20069
    #+
#    img 20070
#    img 20071
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        return
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20061
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_47
        w
        img 20062
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_48
        w
        $ photoImage = 20063
        img photoImage
        with Dissolve(0.2)
        m "Я слежу за тобой, Алекс!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_90
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20064
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_49
        w
        img 20065
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_50
        w
        $ photoImage = 20066
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_91
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20067
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_51
        w
        img 20068
        with Dissolve(0.2)
        m "Алекс, твою мать! Это называется вид сбоку?"
        if corruption < PS6_monica_shot7_corruption_required:
            call corruption_required(PS6_monica_shot7_corruption_required) from _rcall_corruption_required_16
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, это вид снизу!"
        alex_photograph "На нем видны только Ваши пальчики на ногах и больше ничего!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_52
        w
        img 20069
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_53
        w
        img 20070
        with Dissolve(0.2)
        m "Алекс! Это тоже вид снизу?!"
        if corruption < PS6_monica_shot8_corruption_required:
            call corruption_required(PS6_monica_shot8_corruption_required) from _rcall_corruption_required_17
            jump expression photoPoseLabel
        alex_photograph "Да, Миссис Бакфетт!"
        alex_photograph "Но не волнуйтесь, костюм плотно все закрывает!"
        m "Точно?!"
        alex_photograph "Да, Миссис Бакфетт! Всего один кадр!"
        m "Только один! И не ближе!"
        alex_photograph "Конечно!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_54
        w
        $ photoImage = 20071
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_92
        # $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot9_progress")
        w
        jump expression photoPoseLabel
    return

label gallery_ep26_photoshoot_suit6_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot

    music Groove2_85
    img 20072
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 20073
    with fade
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot4_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call gallery_ep26_photoshoot6_casting() from _rcall_gallery_ep26_photoshoot6_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot6_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot6_casting_corruption_required:
            pass
    return

label gallery_ep26_photoshoot6_casting:
    music Groove2_85
    sound highheels_short_walk
    img 20176
    with fadelong
    w
    img 20177
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 20178
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 20179
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 20180
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Алая Жемчужина..."
            biff "Что Алая Жемчужина хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 6
            call gallery_8442() from _rcall_gallery_8442_2

            img 20183 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 20182 #9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 6
            $ chickMode = False
            call gallery_8442() from _rcall_gallery_8442_3
            img 20183 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return

##########################################################
##########################################################

label gallery_ep26_photoshoot_suit7:
    music Groove2_85
    $ shotsAmount = PS7_shots_amount
    $ shotsTotalAmount = 33
#    $ shotsAmount = 33 #debug

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20074
    with fadelong
    m "Алекс! Ты что, сошел с ума?!"
    m "У этого костюма прозрачная грудь!"
    m "Я уже не говорю про трусики, которых почти нет!"
    alex_photograph "Но Мэм..."

    img 20075
    m "Никаких Мэм!"
    m "Я не собираюсь обнажаться на эту чертову камеру!"
    img 20076
    with fade
    alex_photograph "Мэм, этот наряд называется Запретное Желание."
    alex_photograph "И, если Вы хотите, Вы можете закрывать грудь руками..."
    img 20077
    with diss
    m "Да, я буду закрывать грудь руками!"
    m "И только на этом условии я соглашаюсь на съемку!"
    mt "Черт! Куда эти фотосессии меня доведут..."

    music Molten_Alloy
    img 20078
    with fade
    alex_photograph "Мэм, отлично, мы договорились!"
    alex_photograph "Итак, мотор!"

    music stop
    img 20079
    with fadelong


$ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose1"
$ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose2"
label gallery_ep26_photoshoot_suit7_pose1:
    # кадр
    img 20079
    # up
#    img 20080
    # side
#    img 20081
    # down +
#    img 20082

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20083
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20080
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_93
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20081
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_94
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20082
        img photoImage
        with Dissolve(0.2)
        m "Алекс, эти стринги совсем тонкие."
        m "Постарайся не брать ракурсы сзади."
        alex_photograph "Мэм, но Вы и так закрываете грудь."
        alex_photograph "Я ведь должен что-то снимать..."
        m "Снимай мое лицо, болван!"
        if corruption < PS7_monica_shot1_corruption_required:
            call corruption_required(PS7_monica_shot1_corruption_required) from _rcall_corruption_required_18
            jump expression photoPoseLabel
        # если можно
        alex_photograph "Миссис Бакфетт?"
        m "Ладно, только так чтобы было ничего не видно!"
        alex_photograph "Конечно, Миссис Бакфетт! Как скажете!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_95
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot1_progress")
        w
        jump expression photoPoseLabel



label gallery_ep26_photoshoot_suit7_pose2:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose2"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose3"
    # кадр
    img 20083
    # up
#    img 20084
    # side
#    img 20085
    # down
#    m "Алекс, ты снова за свое?!"
#    img 20086

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20087
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music Groove2_85
        m "Алекс, я не хочу вставать в эту позу!"
        m "Трусики слишком тонкие!"
        alex_photograph "Миссис Бакфетт, я буду брать ракурсы так, чтобы ничего не было видно, обещаю!"
        m "Ну, ладно... Но смотри у меня!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20084
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_96
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20085
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_97
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20086
        img photoImage
        with Dissolve(0.2)
        m "Алекс, ты снова за свое?!"
        if corruption < PS7_monica_shot2_corruption_required:
            call corruption_required(PS7_monica_shot2_corruption_required) from _rcall_corruption_required_19
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_98
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot2_progress")
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit7_pose3:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose3"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose4"

    # кадр
    img 20087
    # up
#    img 20088
    # side
#    img 20089
#    img 20090
    # down +
#    img 20091
#    img 20092
#    m "Алекс! Я же попросила!"
#    alex_photograph "Миссис Бакфетт, я только замеряю фокус!"
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20093
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20088
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_99
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20089
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_55
        w
        $ photoImage = 20090
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_100
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20091
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_56
        w
        $ photoImage = 20092
        img photoImage
        with Dissolve(0.2)
        m "Алекс! Я же попросила!"
        if corruption < PS7_monica_shot3_corruption_required:
            call corruption_required(PS7_monica_shot3_corruption_required) from _rcall_corruption_required_20
            jump expression photoPoseLabel
        w
        alex_photograph "Миссис Бакфетт, я только замеряю фокус!"
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_101
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot3_progress")
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit7_pose4:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose4"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose5"

    # кадр
    img 20093
    # up
#    img 20094
    # side
#    img 20095
    # down
#    img 20096
#    m "Алекс, что за дурацкие ракурсы ты берешь?!"
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20097
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20094
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_102
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20095
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_103
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20096
        img photoImage
        with Dissolve(0.2)
        m "Алекс, что за дурацкие ракурсы ты берешь?!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_104
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit7_pose5:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose5"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose6"

    # кадр
    img 20097
    # up +
#    img 20098
#    m "Алекс, убери камеру!"
#    m "У меня видно грудь!"
#    alex_photograph "Миссис Бакфетт, ее не видно, клянусь!"
    # side
#    img 20099
    # down+
#    img 20100
#    m "Алекс, я устала тебя предупреждать!"
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20101
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20098
        img photoImage
        with Dissolve(0.2)
        m "Алекс, убери камеру!"
        m "У меня видно грудь!"
        if corruption < PS7_monica_shot4_corruption_required:
            call corruption_required(PS7_monica_shot4_corruption_required) from _rcall_corruption_required_21
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, ее не видно, клянусь!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_105
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot4_progress")
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20099
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_106
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20100
        img photoImage
        with Dissolve(0.2)
        m "Алекс, я устала тебя предупреждать!"
        if corruption < PS7_monica_shot5_corruption_required:
            call corruption_required(PS7_monica_shot5_corruption_required) from _rcall_corruption_required_22
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_107
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot5_progress")
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit7_pose6:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose6"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose7"

    # кадр
    img 20101
    # up
#    img 20102
    # side
#    img 20103
    # down+
#    img 20104
#    m "Алекс, ты глухой?!"
#    m "Не бери такие ракурсы!"
#    alex_photograph "Миссис Бакфетт, я просто обхожу Вас, чтобы зайти с другой стороны..."

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20105
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        m "Алекс, я не буду вставать в эту позу, даже не надейся!"
        m "У меня грудь почти открыта, прикрыты только соски!"
        if corruption < PS7_monica_pose6_corruption_required:
            call corruption_required(PS7_monica_pose6_corruption_required) from _rcall_corruption_required_23
            return
        # если да
        alex_photograph "Миссис Бакфетт, Ваша грудь обнажена не более, чем в приличном нижнем белье."
        alex_photograph "Не переживайте, ничего не видно."
        m "Точно?"
        alex_photograph "Да, Миссис Бакфетт!"
        m "Ладно, только без дурацких ракурсов!"
        m "Снимай меня прямо и... красиво..."
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20102
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_108
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20103
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_109
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20104
        img photoImage
        with Dissolve(0.2)
        m "Алекс, ты глухой?!"
        m "Не бери такие ракурсы!"
        if corruption < PS7_monica_shot6_corruption_required:
            call corruption_required(PS7_monica_shot6_corruption_required) from _rcall_corruption_required_24
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я просто обхожу Вас, чтобы зайти с другой стороны..."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_110
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot6_progress")
        w
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit7_pose7:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose7"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose8"
    # кадр +
    img 20105
    # up
#    img 20106
    # side
#    img 20107
#    img 20108
#    img 20109
    # down
#    img 20110

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20111
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20106
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_111
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20107
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_57
        w
        img 20108
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_58
        w
        $ photoImage = 20109
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_112
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20110
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_113
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit7_pose8:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose8"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose9"
    # кадр
    img 20111
    # up
#    img 20112
#    m "Алекс!"
#    img 20113
    # side
#    img 20114
    # down +
#    img 20115
#    m "Алекс, перестань фотографировать меня сзади!"
#    # да
#    alex_photograph "Миссис Бакфетт, последний кадр..."
#    img 20116
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20117
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20112
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_59
        w
        $ photoImage = 20113
        img photoImage
        with Dissolve(0.2)
        m "Алекс!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_114
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20114
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_115
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20115
        with Dissolve(0.2)
        m "Алекс, перестань фотографировать меня сзади!"
        if corruption < PS7_monica_shot7_corruption_required:
            call corruption_required(PS7_monica_shot7_corruption_required) from _rcall_corruption_required_25
            jump expression photoPoseLabel
        w
        call photoshop_flash() from _rcall_photoshop_flash_60
        w
        $ photoImage = 20116
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Миссис Бакфетт, последний кадр..."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_116
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot7_progress")
        w
        jump expression photoPoseLabel

label gallery_ep26_photoshoot_suit7_pose9:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose9"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose10"


    # кадр
    img 20117
    # up
#    img 20118
    # side
#    img 20119
    # down +
#    img 20120
#    img 20121

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20123
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20118
        img photoImage
        with Dissolve(0.2)
        m "Алекс!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_117
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20119
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_118
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20120
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_61
        w
        img 20121
        with Dissolve(0.2)
        m "Все, Алекс!"
        m "Хватит с меня твоих грязных кадров!"
        m "Мы закончили!"
        if corruption < PS7_monica_shot8_corruption_required:
            call corruption_required(PS7_monica_shot8_corruption_required) from _rcall_corruption_required_26
            jump expression photoPoseLabel
        # да
        alex_photograph "Миссис Бакфетт, это последний такой кадр, я обещаю!"
        alex_photograph "Осталась еще пара приличных кадров и мы успешно закончим!"
        m "Точно?!"
        alex_photograph "Клянусь!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_62
        w
        $ photoImage = 20122
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_119
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot8_progress")
        w
        m "А это что был за кадр?!"
        m "Ты сказал что тот был последним!"
        alex_photograph "Миссис Бакфетт, это чистка затвора."
        alex_photograph "Я не делал съемку!"
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit7_pose10:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose10"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose11"

    # кадр
    img 20123
    # up
#    img 20124
#    img 20125
    # side
#    img 20126
#    img 20127
    # down +
#    img 20128
#    alex_photograph "Миссис Бакфетт, я не снимаю."
#    alex_photograph "Я просто настраиваю фокус."
    # если нет
#    m "Я прекрасно знаю что ты меня обманываешь, Алекс!"
#    m "Достаточно с меня всего этого!"
    # если да
#    m "Алекс, ты не врешь?"
#    alex_photograph "Миссис Бакфетт, я клянусь!"
#    m "Ладно..."
#    img 20129
#    img 20130
#    img 20131


    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        if shotsAmount == 0:
            return
        jump gallery_ep26_photoshoot_suit7_pose11_pre
#        img 20123
#        with fadelong
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
#        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20124
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_63
        w
        $ photoImage = 20125
        img photoImage
        with Dissolve(0.2)
        m "Алекс!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_120
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20126
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_64
        w
        $ photoImage = 20127
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_121
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20128
        with Dissolve(0.2)
        alex_photograph "Миссис Бакфетт, я не снимаю."
        alex_photograph "Я просто настраиваю фокус."
        if corruption < PS7_monica_shot9_corruption_required:
            m "Я прекрасно знаю что ты меня обманываешь, Алекс!"
            m "Достаточно с меня всего этого!"
            call corruption_required(PS7_monica_shot9_corruption_required) from _rcall_corruption_required_27
            jump expression photoPoseLabel
        m "Алекс, ты не врешь?"
        alex_photograph "Миссис Бакфетт, я клянусь!"
        m "Ладно..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_65
        w
        img 20129
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_66
        w
        img 20130
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_67
        w
        $ photoImage = 20131
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_122
        # $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot9_progress")
        jump expression photoPoseLabel


label gallery_ep26_photoshoot_suit7_pose11_pre:

    # поза
    music Groove2_85
    img 20132
    with fadelong
    w
    m "Алекс, что ты так на меня смотришь?"
    m "Зачем ты попросил меня встать в эту позу?"
    img 20133
    alex_photograph "Миссис Бакфетт, я хочу попросить Вас убрать руки..."
    music Power_Bots_Loop
    img 20134
    with diss
    m "ЧТО?!"
    m "НЕТ!!!"
    m "Даже не надейся!"
    img 20135
    alex_photograph "Миссис Бакфетт, но это не моя прихоть, а распоряжение Мистера Бифа!"
    img 20136
    with diss
    m "Мне плевать!"
    music Groove2_85
    img 20137
    with fade
    alex_photograph "Но Миссис Бакфетт, Ваша грудь закрыта."
    alex_photograph "При таком свете, материал белья не такой уж прозрачный."
    alex_photograph "Он сильно бликует на камере и ничего не видно!"
    img 20138
    m "..."
    img 20139
    alex_photograph "К тому же, будет видно не больше чем на предыдущих кадрах."
    alex_photograph "Все что можно было увидеть, уже есть на пленке."
    alex_photograph "Зато подумайте, фотосессия будет завершена и Мистер Биф будет доволен."
    img 20140
    with diss
    alex_photograph "Я не думаю что он потребует еще больше от Вас, Миссис Бакфетт."
    img 20141
    with fade
    m "Ты так думаешь, Алекс?"
    img 20142
    alex_photograph "Миссис Бакфетт, я в этом уверен!"
    music Hidden_Agenda
    img 20143
    with fade
    mt "Черт возьми!"
    mt "Мне не хочется показывать свою грудь на весь мир, хоть и прикрытую какой-то тряпочкой..."
    img 20144
    mt "С другой стороны, Алекс говорит что материал сильно бликует и ничего не будет видно..."
    mt "И Биф, наконец-то, отстанет от меня."
    mt "Вряд-ли он сможет потребовать больше..."
    mt "Иначе он может перестать давать мне мне деньги..."
    mt "И я даже боюсь представить что тогда будет..."
    img 20145
    with diss
    mt "К тому же, мне нечего стыдиться. У меня самая красивая грудь в этой стране..."
    mt "А может и во всем мире!"
    img 20146
    with fade
    mt "..."
    mt "Итак, что же мне делать?"


    menu:
        "Опустить руки.": #corruption
            pass
        "Прекратить фотосессию":
            music Groove2_85
            img 20147
            with fadelong
            m "Нет, Алекс!"
            m "Я не поддамся на твои уловки!"
            m "С меня хватит!"
            return

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20148
    with fadelong
    m "..."
    img 20149
    alex_photograph "..."

    music stop
    img black_screen
    with diss
    pause 1.0
    music Molten_Alloy
    img 20150
    with fadelong
    w
    alex_photograph "Мотор!"

    music stop
    img 20151
    with fadelong

label gallery_ep26_photoshoot_suit7_pose11:
    $ photoPoseLabel = "gallery_ep26_photoshoot_suit7_pose11"
    $ photoPoseNextLabel = "gallery_ep26_photoshoot_suit7_pose11"

    # кадр
    img 20151
    # up
#    img 20152
#    img 20153
#    img 20154
#    img 20155
#    img 20156
#    img 20157
    # side
#    img 20158
#    img 20159
#    img 20160
    # down
#    img 20161
#    img 20162
#    img 20163
#    img 20164
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        return
#        img 20123
#        with fadelong
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
#        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20152
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_68
        w
        img 20153
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_69
        w
        img 20154
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_70
        w
        img 20155
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_71
        w
        img 20156
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_72
        w
        $ photoImage = 20157
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_123
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20158
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_73
        w
        img 20159
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_74
        w
        $ photoImage = 20160
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_124
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20161
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_75
        w
        img 20162
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_76
        w
        img 20163
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_77
        w
        $ photoImage = 20164
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_125

        w
        music Groove2_85
        alex_photograph "Миссис Бакфетт."
        alex_photograph "Могли бы Вы убрать руки?"
        alex_photograph "Они мешают мне фотографировать нижнюю часть Вашего тела..."
        menu:
            "Делать что просит Алекс. (опционально)": #corruption (very high)
                pass
            "Завершить фотосессию.":
                m "Нет, Алекс."
                m "Я думаю фотосессия завершена и так."
                return
        music I_Feel_You
        m "Да, Алекс..."
        m "Я понимаю..."
        img 20165
        with diss
        w
        m "Надо раздвинуть ноги?"
        alex_photograph "Да, Миссис Бакфетт."
        alex_photograph "Если Вам не трудно."
        m "Я понимаю, Алекс..."
        img 20166
        with diss
        m "Так тебя устроит?"
        img 20167
        with fade
        w
        alex_photograph "Да, Миссис Бакфетт. Вполне."
        call photoshop_flash() from _rcall_photoshop_flash_78
        w
        img 20168
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_79
        w
        img 20169
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_80
        w
        sound Jump1
        img 20170
        with fade
        alex_photograph "Миссис Бакфетт."
        alex_photograph "Можно, пожалуйста, я сниму эти трусики и сделаю пару кадров?"
        alex_photograph "Мистер Биф даст мне солидную премию за это."
        music stop
        img black_screen
        with diss
        pause 1.0
        music Master_Disorder
        img 20171
        with fadelong
        m "Нет, Алекс."
        m "Я закончу с проблемами до того как дойдет до этого..."
        img 20172
        with diss
        m "А сейчас..."
        m "Если ты не уберешь руку, то умрешь..."
        img 20173
        w
        jump expression photoPoseLabel




label gallery_ep26_photoshoot_suit7_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot
    music Groove2_85
    img 20174
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 20175
    with fade
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot7_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call gallery_ep26_photoshoot7_casting() from _rcall_gallery_ep26_photoshoot7_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot7_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot7_casting_corruption_required:
            pass

    return


label gallery_ep26_photoshoot7_casting:
    music Groove2_85
    sound highheels_short_walk
    img 20195 #9470
    with fadelong
    w
    img 20196 #9471
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 20197 #9472
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 20198 #9473
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 20199 #9474
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Запретное Желание..."
            biff "Что Запретное Желание хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 7
            call gallery_8442() from _rcall_gallery_8442_4
            img 20201 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 20200 #9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 7
            $ chickMode = False
            call gallery_8442() from _rcall_gallery_8442_5
            img 20201 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return


##########################################################
##########################################################

label gallery_ep29_photoshoot_melanie1:
    $ shotsAmount = PS_Melanie_1_shots_amount
    $ shotsTotalAmount = 36

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music ZigZag
    img 22593
    with fadelong
    melanie "Алекс, я буду следить за тем, какие ты берешь ракурсы."
    alex_photograph "Да, Мелани. Конечно."

label gallery_ep29_photoshoot_melanie_suit1_pose1:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose1"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose2"
    #кадр
    img 22593

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22597
        with fadelong
        alex_photograph "Отлично! Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22594
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_126
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22595
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_127
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22596
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_128
        w
        jump expression photoPoseLabel


label gallery_ep29_photoshoot_melanie_suit1_pose2:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose2"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose3"
    #кадр
    img 22597

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22601
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
        melanie "Алекс, что ты делаешь?"
        alex_photograph "Мелани, я нашел интересный ракурс."
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22598
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_129
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22599
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, ты помнишь, о чем мы с тобой договаривались?"
        alex_photograph "Конечно, Мелани. Никаких откровенных ракурсов!"
        alex_photograph "Я делаю все, как ты сказала!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_130
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22600
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_131
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose3:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose3"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose4"
    #кадр
    img 22601

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22605
        with fadelong
#        w
#        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22602
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Ты просто божественно прекрасно получишься на снимке."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_132
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22603
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Ничего лишнего не будет видно, Мелани."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_133
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22604
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_134
        w
        jump expression photoPoseLabel


label gallery_ep29_photoshoot_melanie_suit1_pose4:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose4"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose5"
    #кадр
    img 22605

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22609
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22606
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_135
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22607
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Ничего лишнего не будет видно, Мелани."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_136
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22608
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, меня, как Миссис Бакфетт, не проведешь..."
        melanie "Не смей снимать меня с такого ракурса."
        alex_photograph "Мелани, не переживай. На снимке ничего не видно."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_137
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose5:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose5"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose6"
    #кадр
    img 22609

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22613
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22610
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_138
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22611
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс. Не смей делать такие кадры!"
        alex_photograph "Я не фотографирую, Мелани."
        alex_photograph "Я просто пытаюсь подобрать интересный ракурс."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_139
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22612
        img photoImage
        with Dissolve(0.2)
        melanie "Ты меня за кого принимаешь, Алекс?"
        melanie "Я не первый раз участвую в фотосессии."
        melanie "Думаешь, я не понимаю, что ты сейчас сделал?"
        alex_photograph "Мелани, я потом покажу тебе снимки."
        alex_photograph "Ты увидишь, что я делаю вполне приличные кадры."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_140
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose6:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose6"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose7"
    #кадр
    img 22613

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22617
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22614
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_141
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22615
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_142
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22616
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, если ты и дальше будешь продолжать делать такие кадры..."
        melanie "То я откажусь от этой фотоссесии."
        alex_photograph "Мелани, снимки получаются очень приличные."
        alex_photograph "Ты зря так переживаешь. На них совсем ничего не видно."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_143
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose7:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose7"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose8"
    #кадр
    img 22617

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22621
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22618
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_144
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22619
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_145
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22620
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, тебе сколько раз нужно повторить, чтобы ты не брал такие ракурсы?"
        melanie "Ты хочешь, чтобы эта фотосессия стала последней нашей совместной работой?"
        alex_photograph "Мелани, нет конечно! Кадры получаются очень красивые и приличные!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_146
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose8:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose8"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose9"
    #кадр
    img 22621

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22625
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22622
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_147
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22623
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_148
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22624
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс. Не смей делать такие кадры!"
        alex_photograph "Мелани, с этого ракурса ничего не видно. Не переживай."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_149
        w
        jump expression photoPoseLabel


label gallery_ep29_photoshoot_melanie_suit1_pose9:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose9"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose10"
    #кадр
    img 22625

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22629
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22626
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_150
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22627
        img photoImage
        with Dissolve(0.2)
        melanie "А сейчас что ты делашь?"
        alex_photograph "Это будет великолепный кадр, Мелани!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_151
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22628
        img photoImage
        with Dissolve(0.2)
        melanie "Если ты меня обманешь, Алекс, то я не буду больше с тобой работать."
        alex_photograph "Мелани, ты можешь не беспокоиться."
        alex_photograph "Я помню, о чем мы договаривались."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_152
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose10:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose10"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose11"
    #кадр
    img 22629

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22633
        with fadelong
        melanie "Алекс, не вздумай в этой позе делать кадры сзади или крупным планом."
        alex_photograph "Конечно, Мелани. Никаких откровенных ракурсов! Я помню."
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22630
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_153
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22631
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, что ты делаешь?"
        alex_photograph "Мелани, я нашел интересный ракурс."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_154
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22632
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, ты помнишь, о чем мы с тобой договаривались?"
        alex_photograph "Конечно, Мелани. Никаких откровенных ракурсов!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_155
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose11:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose11"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_melanie_suit1_pose12"
    #кадр
    img 22633

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22638
        with fadelong
        melanie "Алекс, я не буду принимать такую позу."
        melanie "Это пошло. Я тебе не порномодель."
        alex_photograph "Мелани, я обещаю, что эти снимки будут настоящим произведением искусства!"
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 22634
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_81
        w
        sound camera_lens1
        $ photoImage = 22635
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс?"
        alex_photograph "Я фотографирую не сзади, а сверху. Потрясающий кадр, Мелани!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_156
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22636
        img photoImage
        with Dissolve(0.2)
        melanie "А сейчас что ты делашь?"
        alex_photograph "Фотографирую сверху. Просто немного сменил ракурс."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_157
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22637
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс! Никаких крупных планов. Ты помнишь об этом?"
        alex_photograph "Конечно, Мелани!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_158
        w
        jump expression photoPoseLabel

label gallery_ep29_photoshoot_melanie_suit1_pose12:
    $ photoPoseLabel = "gallery_ep29_photoshoot_melanie_suit1_pose12"
    $ photoPoseNextLabel = "gallery_ep29_photoshoot_suit1_end"
    #кадр
    img 22638

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 22639
        with Dissolve(0.2)
        alex_photograph "Когда ты их увидишь, то захочешь разместить их, как свои портреты, в гримерке!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_82
        w
        sound camera_lens1
        $ photoImage = 22640
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_159
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22641
        img photoImage
        with Dissolve(0.2)
        melanie "Чтобы я никаких своих интимных мест крупным планом на них не видела, Алекс."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_160
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 22642
        with Dissolve(0.2)
        alex_photograph "Конечно, Мелани!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_83
        w
        sound camera_lens1
        img 22643
        with Dissolve(0.2)
        alex_photograph "Никаких откровенных ракурсов, я помню!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_84
        w
        sound camera_lens1
        $ photoImage = 22644
        img photoImage
        with Dissolve(0.2)
        alex_photograph "И никаких крупных планов!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_161
        w
        jump expression photoPoseLabel


label gallery_ep29_photoshoot_suit1_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot
    music stop
    img black_screen
    with diss
    pause 0.2
    $ melanie_photoshoot1_count += 1
    return
