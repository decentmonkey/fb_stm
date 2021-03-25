default photoshoot5_count = 0

label ep22_photoshoot5:
    $ melanieWaitingOpenedOutfits = False
    $ shotsAmount = PS5_shots_amount
    $ shotsTotalAmount = 27

    $ shots = 3
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

#    m "Алекс, я не буду сниматься в таком ракурсе!"

#    m "Алекс, даже не думай делать такой кадр!"


#    m "Алекс, я не собираюсь вставать в эту позу!!!"
#    "Даже не мечтай!"

    music Molten_Alloy
    img 8748
    with fade
    alex_photograph "Итак, пассажиру авиакомпании нужна помощь с багажом..."

        #кадр
#        img 8748
        #up
#        img 8749
        #side
#        img 8750
        #down
#        img 8751

    label ep22_photoshoot5_pose1:
        img 8748

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8752
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Пассажир авиакомпании замечает стюардессу..."
            jump ep22_photoshoot5_pose2
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8749, 8750, 8751], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose1
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8749
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_21
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8750
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_22
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8751
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_23
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose1


        #кадр
#        img 8752
        #up
#        img 8753
        #side
#        img 8754
        #down
#        img 8755
    label ep22_photoshoot5_pose2:
        img 8752

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8756
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Представитель авиакомпании спешит помочь..."
            jump ep22_photoshoot5_pose3
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8753, 8754, 8755], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose2
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8753
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_24
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose2
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8754
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_25
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose2
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8755
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_26
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose2


        #кадр
#        img 8756
        #up
#        img 8757
        #side
#        img 8758
        #down
#        img 8759

    label ep22_photoshoot5_pose3:
        img 8756

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8760
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            img 8761
            with fade
            mt "Какая у Мелани бархатная кожа на ощупь..."
            music Molten_Alloy
            img 8760
            with fade
            jump ep22_photoshoot5_pose4
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8757, 8758, 8759], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose3
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8757
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_27
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8758
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_28
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8759
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_29
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose3

        #кадр
#        img 8760
        #вид кадра с комментарием о попе Мелани
#        img 8761

        #up
#        img 8762
        #side
#        img 8764
        #down
#        img 8763

    label ep22_photoshoot5_pose4:
        img 8760

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8765
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Пассажир не удовлетворен качеством услуг..."
            if corruption < PS5_monica_pose4_corruption_required:
                music Groove2_85
                m "Алекс! Я не собираюсь сидеть на коленях перед Мелани!"
                "И это не обсуждается!"
                call corruption_required(PS5_monica_pose4_corruption_required) from _call_corruption_required_10
                return False
            m "Алекс! Я не собираюсь сидеть на коленях перед Мелани!"
            m "..."
            m "Ну, ладно..."
            mt "Черт, мне надо узнать правду про Дика!"
            $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot1_progress")

            jump ep22_photoshoot5_pose5
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8762, 8764, 8763], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose4
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8762
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_30
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8764
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_31
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose4
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8763
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_32
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose4


        #кадр
#        img 8765
        #up
#        img 8766
        #side
#        img 8767
        #down
#        img 8768

    label ep22_photoshoot5_pose5:
        img 8765

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8769
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Стюардесса просит прощения у пассажира..."
            if corruption < PS5_monica_pose5_corruption_required:
                music Groove2_85
                m "Алекс! Я не собираюсь ползать в ногах у Мелани!"
                "И это не обсуждается!"
                call corruption_required(PS5_monica_pose5_corruption_required) from _call_corruption_required_11
                return False
            $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot2_progress")
            jump ep22_photoshoot5_pose6
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8766, 8767, 8768], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose5
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8766
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_33
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8767
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_34
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose5
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8768
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_35
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose5

        #кадр
#        img 8769
        #up
#        img 8770
        #side
#        img 8771
        #down
#        img 8772

    label ep22_photoshoot5_pose6:
        img 8769

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8773
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            jump ep22_photoshoot5_pose7
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8770, 8771, 8772], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose6
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8770
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_36
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8771
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_37
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose6
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8772
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_38
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose6


        #кадр
#        img 8773
        #up
#        img 8774
        #side
#        img 8775
#        img 8776
#        img 8778
        #down
#        img 8777

    label ep22_photoshoot5_pose7:
        img 8773

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            img 8779
            with fadelong
            alex_photograph "Миссис Бакфетт, пожалуйста, поместите голову Мелани между ног!"
            m "Какого черта, Алекс?!"
            "Может мне еще что-нибудь сделать?!"
            alex_photograph "Авиакомпания показывает насколько важен каждый пассажир!"

            if corruption < PS5_monica_pose7_corruption_required:
                call corruption_required(PS5_monica_pose7_corruption_required) from _call_corruption_required_12
                m "Алекс! Я не собираюсь ползать в ногах у Мелани!"
                "И это не обсуждается!"
                return False
            music Loved_Up
            $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot2_progress")
            jump ep22_photoshoot5_pose8
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8774, 8778, 8777], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose7
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8774
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_39
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose7
        if result == "side":
            #side
            sound camera_lens1
            img 8775
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_26
            w
            img 8776
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_27
            w
            $ photoImage = 8778
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_40
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose7
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8777
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_41
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose7

        #кадр
#        img 8779
        #up
#        img 8780
        #side
#        img 8781
        #down
#        img 8782
#        w

    label ep22_photoshoot5_pose8:
        img 8779

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            jump ep22_photoshoot5_pose9_pre
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8780, 8781, 8782], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose8
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8780
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_42
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose8
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8781
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_43
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose8
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8782
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_44
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose8

    label ep22_photoshoot5_pose9_pre:
        #вступление
        hide screen photoshoot_no_next2
        img 8783
        with fade
        w
        img 8784
        with Dissolve(0.5)
        music Power_Bots_Loop
        alex_photograph "Теперь сделайте вид что Вы касаетесь язычком ее киски!"
        m "ЧТО?!?! АЛЕКС, ТЫ В СВОЕМ УМЕ?!?!"
        m "Я НЕ СОБИРАЮСЬ ЛИЗАТЬ У МЕЛАНИ МЕЖДУ НОГ!!!"
        "ДА ЕЩЕ И НА КАМЕРУ!!!"
        music Groove2_85
        img 8785
        with fade
        alex_photograph "Миссис Бакфетт! Это ведь просто симуляция!"
        "Вам надо просто коснуться язычком и все!"
        img 8786
        with Dissolve(0.5)
        "Тем более это всего-лишь трусики!"
        "Вы не сделаете ничего неприличного, если дотронетесь до белья другой модели!"
        img 8787
        with Dissolve(0.5)
        m "АЛЕКС, НО!!!..."
        alex_photograph "Миссис Бакфетт, это эротическая фотосессия."
        "В ней авиакомпания хочет показать что готова на все, лишь бы ее клиенты остались довольны!"


        img 8788
        with fade
        melanie "Миссис Бакфетт?"
        menu:
            "Прервать фотосессию.":
                return False
            "Сделать что просит Алекс.":
                $ monicaLickedMelaniePussyPantiesPhotoshoot = True
                mt "Похоже у меня нет выхода..."
                "Мне надо любой ценой узнать замешан-ли во всем этом Дик!"
                "И Мелани единственная надежда на это!"
                music Loved_Up2
                img 8791
                with fade
            "Попросить Мелани не делать этого (хорошие отношения с Мелани)" if melanieOffended2 == False and melanieOffended1 == False:
                m "Мелани, пожалуйста!"
                "Скажи Алексу что хватит!"
                melanie "Хорошо, Миссис Бакфетт..."
                img 8789
                with fade
                melanie "Алекс, я думаю этого достаточно!"
                "Я ведь знаю что этот кадр твоя инициатива!"
                # конец фотосессии
                return True
            "Попросить Мелани не делать этого (плохие отношения с Мелани) (disabled)" if melanieOffended2 == True or melanieOffended1 == True:
                pass

        #кадр
#        img 8791
        #up
#        img 8800
#        img 8792
#        img 8793
        #side
#        img 8801
#        img 8790
#        img 8794
#        img 8795
        #down
#        img 8799
#        img 8796
#        img 8797
#        img 8798

    label ep22_photoshoot5_pose9:
        img 8791

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            hide screen photoshoot_no_next2
            $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot3_progress")
            return True
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next2([8793, 8795, 8798], PS5_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot_no_next2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot5_pose9
        #up
        if result == "up":
            sound camera_lens1
            img 8800
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_28
            w
            img 8792
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_29
            w
            $ photoImage = 8793
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_45
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose9
        if result == "side":
            #side
            sound camera_lens1
            img 8801
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_30
            w
            img 8790
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_31
            w
            img 8794
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_32
            w
            $ photoImage = 8795
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_46
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose9
        if result == "down":
            #down
            sound camera_lens1
            img 8799
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_33
            w
            img 8796
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_34
            w
            img 8797
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_35
            w
            $ photoImage = 8798
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_47
            $ PS5_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot5_pose9

    return

label ep22_photoshoot5_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot_no_next2
    hide screen photoshoot

    if questHelpFlag8Melanie == False:
        $ questHelpFlag8Melanie = True
        $ questHelp("melanie_2")
#        $ questHelp("office_18")
        $ questHelp("photoshoot_4", True)
#        $ questHelpDesc("photoshoot_desc4", False)

    music Stealth_Groover
    img 8745
    with fadelong
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot5_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep23_photoshoot5_casting() from _call_ep23_photoshoot5_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot5_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot5_casting_corruption_required:
            pass

    return

label ep23_photoshoot5_casting:
    music Groove2_85
    sound highheels_short_walk
    img 9493
    with fadelong
    w
    img 9494
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 9495
    $ add_char_progress("Biff", PS5_BiffProgressCasting, "PS5_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS5_shoots_array)))
#    $ shotsTotalAmount
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 9496
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 9497
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Стюардесса из Fashion Airlines..."
            $ add_char_progress("Biff", PS5_BiffProgressCastingChick, "PS5_BiffProgressCastingChick_day" + str(day))
            biff "Что Стюардесса хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 5
            call ep22_casting() from _call_ep22_casting_2
            img 9499
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 9498
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 5
            $ chickMode = False
            call ep22_casting() from _call_ep22_casting_3
            img 9499
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
