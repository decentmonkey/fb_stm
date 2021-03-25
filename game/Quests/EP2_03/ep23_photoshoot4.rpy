default photoshoot4_count = 0

label ep22_photoshoot4:
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

    label ep22_photoshoot4_pose1:

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
            jump ep22_photoshoot4_pose2
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8843, 8844, 8845], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8843
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_48
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8844
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_49
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8845
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_50
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose1


        #кадр
#        img 8846
        #up
#        img 8847
        #side
#        img 8848
        #down+
#        img 8849
    label ep22_photoshoot4_pose2:
        img 8846

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8850
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot4_pose3
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8847, 8848, 8849], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8847
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_51
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose2
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8848
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_52
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose2
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8849
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot1_corruption_required:
                m "Алекс! Хватит!"
                call corruption_required(PS4_monica_shot1_corruption_required) from _call_corruption_required_13
                jump ep22_photoshoot4_pose2
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_53
            $ PS4_shoots_array.append(photoImage)
            $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot1_progress")
            w
            jump ep22_photoshoot4_pose2


        #кадр
#        img 8850
        #up
#        img 8851
        #side
#        img 8852
        #down
#        img 8853
    label ep22_photoshoot4_pose3:
        img 8850

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8854
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot4_pose4
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8851, 8852, 8853], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8851
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_54
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8852
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_55
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8853
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_56
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose3


        #кадр
#        img 8854
        #up
#        img 8855
        #side
#        img 8856
        #down
#        img 8857

    label ep22_photoshoot4_pose4:
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
                call corruption_required(PS4_monica_pose5_corruption_required) from _call_corruption_required_14
                return
            jump ep22_photoshoot4_pose5
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8855, 8856, 8857], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8855
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_57
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8856
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_58
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose4
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8857
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_59
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose4


        #кадр+ кладет руку на грудь
#        img 8858
        #up
#        img 8859
        #side
#        img 8860
        #down+
#        img 8861
    label ep22_photoshoot4_pose5:
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
            jump ep22_photoshoot4_pose6
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8859, 8860, 8861], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8859
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_60
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8860
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_61
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose5
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8861
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot2_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS4_monica_shot2_corruption_required) from _call_corruption_required_15
                jump ep22_photoshoot4_pose5
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_62
            $ PS4_shoots_array.append(photoImage)
            $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot2_progress")
            w
            jump ep22_photoshoot4_pose5

        #кадр
#        img 8862
        #up
#        img 8863
        #side
#        img 8864
        #down+
#        img 8865

    label ep22_photoshoot4_pose6:
        img 8862

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8866
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot4_pose7
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8863, 8864, 8865], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose6
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8863
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_63
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8864
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_64
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose6
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8865
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot3_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS4_monica_shot3_corruption_required) from _call_corruption_required_16
                jump ep22_photoshoot4_pose6
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_65
            $ PS4_shoots_array.append(photoImage)
            $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot3_progress")
            w
            jump ep22_photoshoot4_pose6

        #кадр
#        img 8866
        #up
#        img 8867
        #side
#        img 8868
        #down+
#        img 8869

    label ep22_photoshoot4_pose7:
        img 8866

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8870
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot4_pose8
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8867, 8868, 8869], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose7
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8867
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_66
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose7
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8868
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_67
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose7
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8869
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot4_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS4_monica_shot4_corruption_required) from _call_corruption_required_17
                jump ep22_photoshoot4_pose7
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_68
            $ PS4_shoots_array.append(photoImage)
            $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot4_progress")
            w
            jump ep22_photoshoot4_pose7

        #кадр
#        img 8870
        #up
#        img 8871
        #side
#        img 8872
        #down+
#        img 8873

    label ep22_photoshoot4_pose8:
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
                call corruption_required(PS4_monica_pose8_corruption_required) from _call_corruption_required_18
                return
            jump ep22_photoshoot4_pose9
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8871, 8872, 8873], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose8
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8871
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_69
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose8
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8872
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_70
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose8
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8873
            img photoImage
            with Dissolve(0.2)
            if corruption < PS4_monica_shot5_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS4_monica_shot5_corruption_required) from _call_corruption_required_19
                jump ep22_photoshoot4_pose8
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_71
            $ PS4_shoots_array.append(photoImage)
            $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot5_progress")
            w
            jump ep22_photoshoot4_pose8



        #кадр - жесткая поза
#        img 8874
        #up
#        img 8876
        #side
#        img 8875
        #down+
#        img 8877
#        img 8878

    label ep22_photoshoot4_pose9:
        img 8874

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            return
#            jump ep22_photoshoot4_end
        show screen photoshoot_camera_icon(PS4_shoots_array)
        show screen photoshoot2([8876, 8875, 8878], PS4_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot4_pose9
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8876
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_72
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose9
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8875
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_73
            $ PS4_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot4_pose9
        if result == "down":
            #down+
            sound camera_lens1
            img 8877
            with Dissolve(0.2)
            if corruption < PS4_monica_shot6_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS4_monica_shot6_corruption_required) from _call_corruption_required_20
                jump ep22_photoshoot4_pose9
            w
            call photoshop_flash() from _call_photoshop_flash_36
            w
            $ photoImage = 8878
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_74
            $ PS4_shoots_array.append(photoImage)
            $ add_char_progress("AlexPhotograph", PS4_AlexProgressEachCorruptionShot, "PS4_monica_shot6_progress")
            w
            jump ep22_photoshoot4_pose9

label ep22_photoshoot4_end:

    hide screen photoshoot_camera_icon
    hide screen photoshoot2

    if questHelpFlag21 == False:
        $ questHelpFlag21 = True
#        $ questHelpDesc("photoshoot_desc3a", "photoshoot_desc10a")
    $ questHelp("photoshoot_3a", True)
    $ questHelp("photoshoot_10a", skipIfExists=True)
    $ shotsAmountCompleted = len(list(set(PS4_shoots_array)))
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_10a", True)

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
            $ biffMonicaLastCastingSkipped = True
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
            call ep23_photoshoot4_casting() from _call_ep23_photoshoot4_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot4_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot4_casting_corruption_required:
            pass

    return

label ep23_photoshoot4_casting:
    music Groove2_85
    sound highheels_short_walk
    img 9470
    with fadelong
    w
    img 9471
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 9472
    $ add_char_progress("Biff", PS4_BiffProgressCasting, "PS4_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS4_shoots_array)))
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
            $ add_char_progress("Biff", PS4_BiffProgressCastingChick, "PS4_BiffProgressCastingChick_day" + str(day))
            biff "Что Роза Надежды хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 4
            call ep22_casting() from _call_ep22_casting_4
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
            call ep22_casting() from _call_ep22_casting_5
            img 9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
