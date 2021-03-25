default citizen1BoobsNakesShowedLastDay = 0
default citizen1BoobsNakedDancedLastDay = 0
default citizen1BoobsNakesShowedCount = -1
default citizen1BoobsNakedDancedCount = -1
default citizen1DanceCloth = 0
default citizen1BoobsNakedDancedCount1 = 0
default citizen1BoobsNakesShowedCount1 = 0

label citizen1_dialogue:
    imgl Dial_Monica_Sandwich_0
#    "Можно к Вам обратиться?"
    m "Эй, ребята... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_1_1
    if citizen1_offered_last_day == day:
        imgr Dial_Citizen_1_4
        citizen1 "Эй! Тетя!"
        "Ты уже подходила к нам!"
        "Хватит с нас твоих флаеров!"
        return
    citizen1 "Да, тетя? Что тебе надо?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            $ citizen1_offered_last_day = day
            imgl Dial_Monica_Sandwich_1
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen1_refuse_probability) > 0:
                imgr Dial_Citizen_1_2
                citizen1 "Тетя, не видишь, мы заняты, нам сейчас не до тебя."
                imgr Dial_Citizen_2_3
                citizen2 "Погоди, Том, разве ты не видишь? Она работает."
                imgr Dial_Citizen_1_3
                citizen1 "С такой внешностью тебе бы не флаеры раздавать!"
                imgl Dial_Monica_Sandwich_0
                mt "(Вот козел...)"
                imgr Dial_Citizen_2_2
                imgl Dial_Monica_Sandwich_1
                call reduce_flyers() from _call_reduce_flyers_9
                citizen2 "А я возьму, давай свой флаер."
                # на 3 раз будут они давать какие то задания ей
                imgr Dial_Citizen_1_3
                citizen1 "Тетя! А больше ты ничего мне не можешь дать?"
                menu:
                    "Больше ничего!":
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Больше ничего!"
                        $ kebabWorkHarassmentAmount +=1
                    "А что бы вы хотели?":
                        m "А что бы вы хотели?"
                        imgr Dial_Citizen_1_3
                        citizen1 "А то ты не знаешь, тетя! Конечно тебя!"
                        imgr Dial_Citizen_2_3
                        citizen2 "Мой брат слишком груб, но в целом он прав."
                        imgl Dial_Monica_Sandwich_2
                        menu:
                            "Что?! Да как вы можете просить такое?":
                                m "Что?! Да как вы можете просить такое?"
                                return
                            "Я подумаю, но сейчас я занята..." if fallingPathStarted == True:
                                m "Я подумаю, но сейчас я занята..."
                                mt "В любом случае я не могу ничего поделать в этом жутком наряде..."
                                return

            else:
                imgr Dial_Citizen_1_4
                citizen1 "Нам не нужны твои флаеры, тетя!"
                $ kebabWorkMonicaRefusedAmount += 1

    return
# диалог доступен только когда моника не работает на раздаче флаеров
label citizen1_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_1_1
    m "Эй, парни! Скажите, у вас есть деньги?"
    citizen1 "Смотря для чего, тетя. А тебе зачем?"
    m "Вы помнится хотели на меня посмотреть..."
    imgr Dial_Citizen_1_3
    citizen1 "Да, тетя, и до сих пор хотим!"
    m "Ну, я могу Вам кое-что показать, только нам лучше уйти отсюда."
    citizen1 "Конечно, тетя, без проблем."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_214
    call pylonController(2, 1) from _call_pylonController_149
    with fade
    citizen1 "Ну что, тетя..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False

    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen1_dialogue_pilon_loop1:
    call pylonController(1, 1) from _call_pylonController_150
    if (pylonpart4startsCompleted == True and citizen1BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen1BoobsNakesShowedCount>=0:
        $ questHelp("work_slums_37", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_151 #
            citizen1 "Покажи нам свои классные сиськи!"
            $ questHelp("work_slums_5", True)
            $ questHelp("work_slums_15", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")

            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1

            call pylonController(3, 3) from _call_pylonController_152
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_40
            call pylonController(3, 3) from _call_pylonController_153
            # img показывает сиськи
            citizen1 "Отличные сиськи, но как насчет того, чтобы снять все лишнее?"
            call pylonController(3, 2) from _call_pylonController_154
            m "Ну уж нет."
            call pylonController(3, 1) from _call_pylonController_155
            citizen1 "Ну и так не плохо."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen1_dialogue_pilon_loop1
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_156
            citizen1 "Покажи нам свои красивый зад!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5) from _call_pylonController_157
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4) from _call_showRandomImages_41
            call pylonController(4, 5) from _call_pylonController_158
            citizen1 "Шикарная жопа, тетя!"
            call pylonController(4, 5) from _call_pylonController_159
            citizen1 "Почти как у моей бывшей."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen1_dialogue_pilon_loop1
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_160
            citizen1 "Покрутись на пилоне, тетя."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_161
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_162
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            $ citizen1DanceCloth += 1
            if citizen1DanceCloth >= 3:
                $ questHelp("work_slums_15", True)

            call showRandomImages(pylonClothDanceImages1, 4) from _call_showRandomImages_42
#            call pylonController(4, 5)
            citizen1 "А ты крутишься как профессионал. Мне нравится!"
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_163
            with fade
            mt "Не думаю, что буду это делать часто..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen1_dialogue_pilon_loop1
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen1BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen1BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen1BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen1BoobsNakesShowedCount == -1:
                call cit1_2_naked_boobs_1st() from _call_cit1_2_naked_boobs_1st
                if _return != False:
                    $ citizen1BoobsNakesShowedCount += 1
            else:
                if citizen1BoobsNakesShowedCount%2 == 0:
                    call cit1_2_naked_boobs_variant1() from _call_cit1_2_naked_boobs_variant1
                if citizen1BoobsNakesShowedCount%2 == 1:
                    call cit1_2_naked_boobs_variant2() from _call_cit1_2_naked_boobs_variant2
                $ citizen1BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen1BoobsNakesShowedCount1 = citizen1BoobsNakesShowedCount + 1
                if citizen1BoobsNakesShowedCount1 >= 3:
                    $ questHelp("work_slums_27", True)

                $ citizen1BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen1_dialogue_pilon_loop1


            call pylonController(4, 1) from _call_pylonController_164
            citizen1 "Мы хотим поглядеть на твои классные сиськи еще раз. Снимай все!"
            mt "Грязные панки..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_165
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5) from _call_pylonController_166
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_43
            call pylonController(4, 5) from _call_pylonController_167
            citizen1 "Черт, тетя! Они шикарны! И что же ты их раньше от нас прятала?"
            call pylonController(4, 1) from _call_pylonController_168

            citizen1 "Эй, тетя! Как насчет того, чтобы получить немного больше?"
            m "..."
            citizen1 "У меня идея! Нас как раз двое, как и твоих подружек. Давай обнимемся!"
            m "Даже не надейся!"
            citizen1 "Ладно, не горячись, тетя! Ты же не против заработать чуть больше... Сожми ка свои аппетитные соски!"
            label citizen1_dialogue_pilon_loop1_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothNakedBoobsNippleSquizeCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothNakedBoobsNippleSquizeCorruptionRequired] corruption"
                        jump citizen1_dialogue_pilon_loop1_1
                    m "Ладно."
                    call pylonController(3, 4) from _call_pylonController_169
                    with fade
                    w
                    call showRandomImages(nakedboobssquizenipplesImages, 1) from _call_showRandomImages_44
                    call pylonController(3, 4) from _call_pylonController_170
                    citizen1 "Уф...А ты горячая!"
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_171
                    m "Не собираюсь, и так достаточно."
                    citizen1 "Не ожидал я такого тетя. Думаю, ты скоро передумаешь."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen1_dialogue_pilon_loop1
        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen1BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen1BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen1BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen1BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen1BoobsNakedDancedCount == -1:
                call cit1_2_naked_boobs_dance_1st() from _call_cit1_2_naked_boobs_dance_1st
                if _return != False:
                    $ citizen1BoobsNakedDancedCount += 1
            else:
                if citizen1BoobsNakedDancedCount%2 == 0:
                    call cit1_2_naked_boobs_dance_variant1() from _call_cit1_2_naked_boobs_dance_variant1
                if citizen1BoobsNakedDancedCount%2 == 1:
                    call cit1_2_naked_boobs_dance_variant2() from _call_cit1_2_naked_boobs_dance_variant2
                $ citizen1BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen1BoobsNakedDancedCount1 = citizen1BoobsNakedDancedCount + 1
                if citizen1BoobsNakedDancedCount1 >= 3:
                    $ questHelp("work_slums_37", True)
#                    $ questHelp("work_slums_47", skipIfExists=True)
                $ citizen1BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen1_dialogue_pilon_loop1


        "Достаточно на сегодня.":
            $ earnedMoney = 0
            if showedBoobs == True or showedButt == True or showedDance == True or showedNakedBoobs == True or showedNakedBoobsDance == True:
                if showedBoobs == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedButt == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedDance == True:
                    $ earnedMoney += monicaWhoringClothDanceMoney
                if showedNakedBoobs == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoney
                if showedNakedBoobsDance == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoneyDance
                call pylonController(2, 1) from _call_pylonController_172
                citizen1 "Ну все, тетя, хватит. До следующего раза. Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_173
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_174
            citizen1 "Тетя, и за что тебе платить? Ничего не получишь."
            return False
    return

# первый раз
label cit1_2_naked_boobs_1st:
    img 11745
    with fade
    citizen1 "Тетя, у нас с братом возникла шикарная идея!"
    img 11746
    citizen1 "Мы ведь с тобой не первый раз видимся и уже не чужие люди.."
    img 11747
    m "Ты это к чему?"
    img 11748
    citizen1 "Мда, не умею я говорить намеками..."
    citizen1 "Короче мы хотим посмотреть на твои сиськи, но уже так сказать без всего!"
    img 11749
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11750

            m "Хватит с вас и того, что вы уже видели!"
            return False
    music Groove2_85
    img 11751
    with fade
    m "Ну а мне это зачем?"
    img 11752
    citizen1 "Ну как зачем? А зачем ты нам их в одежде показываешь?"
    citizen1 "Мы заплатим!"
    music Hidden_Agenda
    img 11753
    with diss
    m "Хорошо, смотрите, только руками не трогать!"
    m "И отвернитесь!"

    # отворачиваются
    sound snd_fabric1
    img 11755
    with fade
    w
    img 11754
    citizen1 "О чем речь, тетя! Разве мы когда нибудь тебя обманывали?"
    m "Можете поворачиваться.."
    img 11756
    w
    img 11757
    w
    # поворачиваются, моника показывает сиськи
    music Loved_Up
    img 11758
    with diss
    citizen1 "Ого! Прямо как у моей бывшей!"
    # показывает сиськи еще
    img 11759
    with diss
    w
    img 11760
    with diss
    citizen1 "Вот это класс, тетя! Так они смотрятся гораздо лучше."
    img 11761
    with diss
    w
    img 11762
    with diss
    w
    img 11763
    with diss
    w
    img 11764
    with diss
    # показывает сиськи еще
    w
    music Groove2_85
    img 11765
    with diss
    citizen1 "Да, сегодня день прошел не зря!"
    $ nakedBoobsFirstly_Cit1_2 = True
    return True

# вариант 1
label cit1_2_naked_boobs_variant1:
    music Groove2_85
    img 11766
    with fade
    citizen1 "Тетя, покажи нам свои сиськи!"
    img 11767
    m "Как именно?"
    img 11768
    citizen1 "А ты шутница. Конечно голыми, так интереснее!"
    img 11769
    menu:

        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11770
            m "Хватит с вас и того, что вы уже видели!"
            return False

    #m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    #m "Можете повернуться."
    img 11771
    m "Хорошо. Если заплатите..."
    music Loved_Up
    img 11772
    with fadelong
    w
    img 11773
    with diss
    m "Только руками не трогать!"
    img 11774
    citizen1 "Какие вопросы, тетя!"
    # показывает
    img 11775
    citizen1 "Не могу наглядеться, красота!"
    # смена картинки, под другим углом
    img 11776
    w
    img 11777
    w
    img 11778
    w
    img 11779
    citizen1 "Тетя, а че ты молчишь?"
    img 11780
    m "Мне нечего вам сказать..."
    img 11781
    citizen1 "Ого! Ну ладно, глядя на такие сиськи можно и ничего не говорить!"
    # смена картинки, под другим углом
    img 11782
    w
    img 11783
    w
    img 11784
    w
    img 11785
    citizen1 "Эй, тетя! Как насчет того, чтобы получить немного больше?"
    img 11786
    with diss
    m "..."
    img 11787
    citizen1 "У меня идея! Нас как раз двое, как и твоих подружек. Давай обнимемся!"
    music Groove2_85
    img 11788
    with diss
    m "Даже не надейся!!!"
    img 11789
    citizen1 "Кто-то сегодня не в духе? Ладно, и так все очень хорошо!"
    return True

# вариант 2
label cit1_2_naked_boobs_variant2:
    music Groove2_85
    img 11790
    with fade
    citizen1 "Тетя, покажи нам свои сиськи!"
    img 11791
    m "Как именно?"
    img 11792
    citizen1 "Серьезно?! Давай снимай уже все!"
    img 11793
    menu:
        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11794
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 11795
    with fade
    m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    music Loved_Up
    sound snd_fabric1
    img 11796
    with fade
    w
    img 11797
    with diss
    m "Можете повернуться."
    m "Только руками не трогать!"
    img 11798
    citizen1 "Конечно, тетя!"
    # показывает
    img 11799
    w
    img 11800
    w
    img 11801
    citizen1 "Вау! Как в первый раз!"
    img 11802
    w
    img 11803
    w
    img 11804
    # смена картинки
    music Groove2_85
    img 11805
    citizen1 "Ты же не против заработать чуть больше... Сожми ка свои аппетитные соски!"
    img 11806
    m "Ну...Я не знаю..."
    img 11807
    citizen1 "Давай! И прямо сейчас получишь часть денег!"
    img 11808
    menu:
        "Хорошо.":
            $ add_money(0.5)
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11809
            m "Хватит с вас и того, что вы уже видели!"
            return True

    # смена картинки - моника сжимает соски
    music Loved_Up
    img 12487
    with fade
    w
    img 12488
    w
    img 12489
    citizen1 "Уф...А ты горячая!"
    citizen1 "И так заводит!"
    img 12490
    m "Ай!"
    mt "Это немного больно и даже немного приятно... Странно..."
    # смена картинки - моника сжимает соски
    img 12491
    w
    img 12492
    w
    music Groove2_85
    img 12493
    with fade
    citizen1 "Ух, тетя, снова нас порадовала!"
    # ?? может есть смысл сделать картинку: если было сжатие сосков - моника наклоняется и поднимает монетку
    return True

# первый раз танцы с сиськами
label cit1_2_naked_boobs_dance_1st:
    music Groove2_85
    img 13188
    with fade
    citizen1 "Тетя, нам скучно!"
    citizen1 "Как насчет еще одного танца на пилоне?"
    img 13189
    m "Вы уже видели меня танцующей там.."
    img 13190
    citizen1 "Эм...Ну да..."
    citizen1 "Короче потанцуй для нас без кофты."
    img 13191
    with fade
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 13192
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 13193
    with fade
    mt "Я уже танцевала, мою прекрасную грудь они видели... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет... А мне нужны деньги..."
    img 13194
    m "Сколько вы заплатите?"
    img 13195
    citizen1 "Тетя, тариф стандартный!"
    citizen1 "Но если ты готова станцевать с бутылкой в заднице, это можно обсудить!"
    music Power_Bots_Loop
    img 13196
    m "Что?! Да как ты смеешь такое говорить?!"
    img 13197
    citizen1 "Ой, тетя! Не кипятись, я пошутил..."
    music Groove2_85
    img 13198
    with fade
    m "Только вздумайте еще раз так пошутить! Отвернитесь!"

    # отворачиваются
    img 13199
    with diss
    w
    sound snd_fabric1
    img 13200
    with diss
    citizen1 "Конечно, тетя, не вопрос."
    music Loved_Up
    img 13201
    with fade
    m "Можете поворачиваться..."
    # поворачиваются, моника стоит с голыми сиськами
    img 13202
    citizen1 "Да, они шикарны. Можешь начинать."
    # движение на пилоне
    music Molten_Alloy
    img 13203
    with diss
    w
    img 13204
    with diss
    w
    img 13205
    citizen1 "Отлично, тетя!"
    # движение на пилоне еще
    img 13206
    with diss
    w
    img 13207
    with diss
    citizen1 "Черт, как глупо было просить тебя крутиться в одежде!"
    # движение на пилоне еще
    img 13208
    with diss
    w
    img 13209
    with diss
    w
    img 13210
    with diss
    citizen1 "Вау, тетя! Тебе нужно этим зарабатывать! Хотя стоп, этим ты и занимаешься!"
    citizen1 "Ха-ха-ха!"
    music Groove2_85
    img 13211
    with fade
    mt "Грязные панки..."
    mt "Мерзавцы..."
    $ nakedBoobsDanceFirstly_Cit1_2 = True
    return True

# первый выриант
label cit1_2_naked_boobs_dance_variant1:
    music Groove2_85
    img 13212
    with fade
    citizen1 "Тетя, мы снова хотим ощутить себя в стрип клубе!"
    citizen1 "Как насчет еще одного танца на пилоне?"
    img 13213
    m "В стрип клубе платят больше, да и вход туда бывает платный."
    img 13214
    citizen1 "Но мы ведь не в стрип клубе!"
    citizen1 "Станцуй для нас, и сиськи не забудь оголить."
    img 13215
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 13216
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 13217
    with fade
    m "Сколько вы заплатите?"
    img 13218
    citizen1 "Снова ты за свое!"
    citizen1 "Можно подумать о том, как ты можешь заработать больше, но в другой раз."
    citizen1 "И вообще, ты нас утомляешь своей болтовней, раздевайся уже!"
    img 13219
    with diss
    menu:
        "Хорошо.":
            pass
        "Я передумала.":
            img 13220
            m "Нет, не будет вам танцев!"
            m "Вы и так уже видели достаточно!"
            return False
    img 13221
    with fade
    m "Хорошо. Отвернитесь!"
    # отворачиваются
    img 13222
    citizen1 "Конечно, тетя, не вопрос."
    sound snd_fabric1
    music Loved_Up
    img 13223
    with fade
    w
    img 13224
    with fadelong
    m "Можете поворачиваться.."
    # поворачиваются, моника стоит с голыми сиськами
    img 13225
    citizen1 "Тетя, тебе особое приглашение нужно? Начинай уже!"
    # движение на пилоне
    music Molten_Alloy
    img 13226
    with diss
    w
    img 13227
    with diss
    citizen1 "Отлично, тетя!"
    # движение на пилоне еще
    img 13228
    with diss
    w
    img 13229
    with diss
    citizen1 "Черт, как глупо было просить тебя крутиться в одежде!"
    # движение на пилоне еще
    img 13230
    with diss
    w
    img 13231
    with diss
    citizen1 "И зачем мы ходим в стрип клуб?"
    # моника слезает  спилона, панк достает бутылку
    img 13234
    w
    img 13232
    with fade
    citizen1 "Тетя, ты помнишь про наше предложение насчет бутылки?"
    # моника злая
    music Power_Bots_Loop
    img 13233
    with fade
    m "Еще слово, и я засуну бутылку тебе в зад!"
    img 13235
    citizen1 "Ха-ха-ха! Два раза одна и та же шутка прошла!"
    music Groove2_85
    img 13236
    with fade
    mt "Грязные панки..."
    img 13237
    citizen1 "Ладно, молодец, тетя, нам понравилось!"
    return True

# второй выриант
label cit1_2_naked_boobs_dance_variant2:
    music Groove2_85
    img 13238
    with fade
    citizen1 "Тетя, станцуй! И не забуть снять кофту!"
    img 13239
    with fade
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 13240
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 13241
    with fade
    m "Хорошо. Отвернитесь!"
    # отворачиваются
    music Loved_Up
    img 13242
    with diss
    citizen1 "..."
    sound snd_fabric1
    img 13223
    with fade
    w
    img 13224
    with fadelong
    m "Можете поворачиваться.."
    # поворачиваются, моника стоит с голыми сиськами
    img 13225
    citizen1 "Начинай!"
    img 13243
    mt "Что-то они какие-то молчаливые... Это подозрительно..."
    # движение на пилоне
    music Molten_Alloy
    img 13244
    with diss
    w
    img 13245
    with diss
    citizen1 "Отлично!"
    # движение на пилоне еще
    img 13246
    with diss
    w
    img 13247
    with diss
    citizen1 "Не плохо!"
    img 13248
    with diss
    mt "Что это с ними сегодня? Они ведут себя не как обычно..."
    # движение на пилоне еще
    # когда моника крутится на пилоне спиной к панкам, один из них достает
    # телефон, и фоткает другого на фоне моники когда она не видит
    # звук фотографировния
    # моника слезает с шеста
    img 13249
    with diss
    w
    img 13250
    with diss
    call photoshop_flash() from _call_photoshop_flash_149
    w
    music Groove2_85
    img 13251
    with diss
    m "Что это был за звук?"
    img 13252
    mt "Как будто меня сфотографировали..."
    img 13253
    citizen1 "Какой звук, тетя? Мы ничего не слышали."
    img 13254
    m "Вы меня сфотографировали?"
    img 13255
    citizen1 "Нет, тетя! Да и откуда у нас фотоаппарат?"
    img 13256
    with fade
    mt "И правда, откуда... Хотя... Нет, у них нет фотоаппарата..."
    with diss
    img 13257
    citizen1 "Кстати, отличный танец!"
    return True

#Моника
# Высокомерие
# Считает что все ниже нее
# То положение, в котором она сейчас - это временно
# Все что происходит - НЕ принимает, но делает, потому что нужны и нет особо другого пути
# Любые договоренности с людьми в трущобах для нее ничего не значат
# Перед серьезными действиями - внутренняя борьба

label cit1_2_grooping_first:
    img 14488
    citizen1 "Тетя, мы столько времени на тебя смотрели!"
    citizen1 "Хотим тебя потрогать!"
    img 14489
    menu:
        "Сколько вы заплатите?":
            pass
        "А я не хочу!":
            img 14490
            m "А я не хочу!"
            return False
#    mt "Пожалуй, можно это сделать,
    img 14491
    mt "Я заберу все ваши деньги! И не разденусь!"
    mt "Не собираюсь раздеваться при этих болванах."
    mt "Но мне надо как-то получить от них деньги."
    img 14492
    m "Сколько вы заплатите?"
    m "Я хочу 100 долларов! И не меньше!"
    img 14493
    citizen1 "Тетя, ты нас обижаешь! У нас нет таких денег..."
    citizen1 "Только ради твоей жопы и классных сисек я готов предложить тебе двойной тариф!"
    img 14494
    m "Что еще за тариф?!"
    img 14495
    citizen1 "Тетя, все очень просто!"
    citizen1 "Мы платим тебе доллар, а при двойном тарифе платим два. Понятно?"
    img 14496
    m "Понятно."
    img 14497
    mt "Надо сделать так, чтобы эти идиоты заплатили как можно больше!"
    img 14498
    m "Этого не достаточно!"
    img 14499
    citizen1 "Не достаточно для чего? Да на эти деньги ты здесь купишь много всего! Чего только стоит изумительная шаверма у Мамеда... Или Архимеда... Короче ты его знаешь!"
    img 14500
    m "..." # Зло смотрит
    img 14501
    citizen1 "Ох, ладно, тройной тариф, но мы будем это делать одновременно с братом!"
    img 14502
    m "Что!?" # Ошеломление
    img 14503
    mt "Да кем они себя возомнили? Чтобы меня трогали эти грязные панки?! Да еще и вдвоем?!"
    img 14504
    menu:
        "Четверной тариф!":
            pass
        "Что? Да ни за что!":
            img 14490
            m "Что? Да ни за что!"
            return False
    img 14505
    mt "Думаю, они могут заплатить больше..."
    img 14506
    m "Четверной тариф!"
    # переговариваются
    img 14507
    citizen1 "А ты бизнес вуман, тетя, совсем без денег нас оставляешь! Договорились!"
    citizen1 "Раздевайся!"
    img 14508
    m "Вообще-то, я не сказала, что буду раздеваться!"
    img 14509
    citizen1 "Да как так-то? Четверной тариф!"
    img 14510
    m "Я не буду раздеваться!"
    m "Выбор за вами! Я и так собираюсь позволить вам слишком много!"
    img 14503
    mt "Раньше бы я не позволила вам даже стоять со мной рядом!"
    # не довольны
    img 13188
    citizen1 "Да за кого ты нас принимаешь, тетя? Мы с братом высококультуренные личности!"
    citizen1 "Или культурные... Наш кузен работает в магазине старшим работником!"
    img 13193
    mt "Вот это да! Могу себе представить..."
    img 13195
    citizen1 "Нам надо посоветоваться..."
    img 14511
    # отворачиваются что то говорят
    # Моника со спины, панки стоят вдалеке шушкаются, поглядывая на Монику (один смотрит боком, другой шепчет на ухо)
    img 13218
    citizen1 "Ладно, тетя! Ты умеешь убеждать! Давай начнем уже!"
    # начинают лапать- сиськи
    img 14512
    w
    img 14513
    w
    img 14514
    w
    img 14515
    w
    img 14516
    w
    img 14517
    citizen1 "Ого! Деньги вложены не зря!"
    citizen1 "Как тебе, братец?"
    citizen1 "Эти сиськи шикарны!"
    citizen1 "Но надо бы обратить внимание еще и на ее шикарный зад!"
    # начинают лапать- один сиськи другой зад
    img 14518
    menu:
        "Терпеть.":
            mt "Черт! Надо еще немного потерпеть, иначе мне не удастся получить с них деньги..."
            pass
        "Это уже перебор!":
            mt "До чего противно...Это слишком..."
            m "Я передумала! Это уже слишком!"
            return False
    img 14519
    w
    img 14541
    w
    img 14542
    citizen1 "Огонь! Тетя, ты просто космос!"
    img 14543
    m "Да, я это знаю. Все, с вас хватит."
    img 14544
    citizen1 "Вот умеешь ты обламывать! Ладно, пусть так... Вот твои деньги!"
    return True

label cit1_2_grooping_regular:
    img 14520
    citizen1 "Тетя! Дай потрогать твою попу..."
    img 11769
    mt "Грязные панки...Снова хотят меня трогать своими ручищами..."
    img 11770
    m "Нет! Ни за что!"
    img 14521
    citizen1 "Четверной тариф!" # Подмигивает
    img 13239
    menu:
        "Черт... Мне нужны деньги...":
            pass
        "Не сегодня.":
            img 13240
            m "Не сегодня."
            return False
    img 13263
    mt "Ничтожества..."
    img 13192
    m "Четверной тариф!"
    img 13218
    citizen1 "Тетя, не сделаешь ли скидочку?"
    img 14491
    mt "Какие скидочки? Это же я...И... Я себя продаю... Черт..."
    mt "Нет, это просто временное недоразумение."
    mt "Я забуду об этом сразу как все закончится!"
    img 13191
    menu:
        "Это все необходимо...":
            pass
        "Я передумала.":
            img 13198
            m "Я передумала. Я не собираюсь идти на такие грязные вещи за деньги!"
            img 14503
            mt "Тем более за такие маленькие!"
            mt "Хотя... Моника... Да ни за какие вообще!"
            return False
    img 13265
    mt "Это все временная необходимость..."
    img 13213
    m "Нет!"
    img 13214
    citizen1 "Ну хорошо, но я пытался..."
    citizen1 "Начнем?"
    # лапают все подряд сиськи жопу, одновременно
    img 14547
    w
    img 14548
    w
    img 14549
    w
    img 14545
    w
    img 14546
    w
    img 14550
    citizen1 "Какая жопа, да братик? Хотел бы я взглянуть на нее без этих дурацких шорт."
    citizen1 "А сиськи то! Как у моей бывшей! Только в 4 раза больше! Ха-ха-ха!"
    citizen1 "Какая упругая! Тетя, у тебя слишком шикарное тело для уличной шлюхи!"
    img 14551
    m "Я не шлюха!"
    img 14552
    mt "Вы даже не представляете кто я такая!"
    img 14553
    citizen1 "Конечо, конечно! Можешь называть это как хочешь."
    # разовое событие в рамках этого диалога. открывает спешал событие если выполняется
    img 14522
    citizen1 "Тетя, мы понимаем, что ты корчишь из себя недотрогу, но хотим предложить еще кое-что."
    citizen1 "Только дослушай прежде чем психовать."
    img 14523
    menu:
        "Хватит с меня предложений.":
            img 14524
            m "Хватит с меня предложений."
            m "Вы и так уже меня всю облапали..."
            img 14525
            citizen1 "Ладно, тетя, как хочешь. Мы только лишь предлагаем тебе заработать денег."
            pass
        "Я слушаю.":
            img 14526
            m "Я слушаю."
            img 14527
            mt "Хотя надо ли было их слушать? Разве они могут предложить что-то достойное меня?"
            img 14528
            citizen1 "Сыграй с нами в панк-считалочку!"
            img 14529
            m "Чего?"
            img 14530
            citizen1 "Да, сыграй! Она не большая. Вот послушай!"
            citizen1 "Раз!"
            citizen2 "Два!"
            citizen1 "Три!"
            citizen2 "Четыре!"
            citizen1 "Пять!"
            citizen2 "Скоро будем мы бухать!"
            img 13193
            mt "На большее у вас мозгов и не хватит..."
            img 14531
            m "И в чем смысл?"
            img 14532
            citizen1 "Ну в общем..."
            citizen1 "Мы будем слегка шлепать твою попу и считать... Всего 5 раз, это немного."
            citizen1 "Но учти! Это для нас важно, поэтому мы дадим тебе 10 долларов!"
            mt "10 Долларов... И я вынуждена идти на такое за какие-то 10 долларов?!"
            img 14533
            mt "О Боже!"
            mt "Черт, Моника, до чего ты дошла? Раньше ты зарабатывала 100 долларов в секунду..."
            mt "Стоит ли соглашаться?"
            img 14504
            menu:
                "Ладно.":
                    img 14534
                    m "Ладно."
                    img 14535
                    mt "Черт! Я соглашаюсь на такие вещи."
                    mt "Когда это все закончится, я забуду все как страшный сон."
                    img 14536
                    citizen1 "Ура, тетя согласна!"
                    citizen1 "Давай сделаем это."
                    img 14538
                    w
                    img 14537
                    citizen1 "Вставай вот так..."
                    # нагибают ее (не сильно) (ставят к пилону, держится руками за пилон и попа чуть назад)
                    # панки стоят по бокам и шлепают Монику по очереди
                    img 14539
                    w
                    img 14540
                    citizen1 "Да, вот так и стой!"
                    citizen1 "Ну что, братец, мы готовы?"
                    img 14562
                    citizen1 "Раз!"
                    img 14554
                    citizen2 "Два!"
                    img 145562
                    citizen1 "Три!"
                    img 14554
                    citizen2 "Четыре!"
                    img 14562
                    citizen1 "Пять!"
                    img 14555
                    m "Ай! Больно!"
                    img 14554
                    citizen2 "Скоро будем мы бухать!"
                    img 14556
                    citizen1 "Да! Прекрасный день сегодня!"
                    # все происходит быстро, поэтому моника даже не успевает ниче сказать.
                    img 14557
                    citizen1 "Тетя! Ты выглядишь не совсем довольной..."
                    citizen1 "Ты должна быть рада! Теперь ты знаешь нашу считалочку и сможешь сыграть с нами еще раз!"
                    citizen1 "И у тебя есть 10 долларов!"
                    img 14558
                    mt "Предел мечтаний...Черт, моя попа немного болит..."
                    pass
                "Нет.":
                    img 14524
                    m "Нет!"
                    m "Даже не думайте!"
                    img 14525
                    citizen1 "Ха-ха! Тетя, ты даже не знаешь сколько желающих сыграть с нами."
                    citizen1 "Надеюсь, ты передумаешь."
                    img 14527
                    mt "Не надейся!"
                    pass
            pass
    img 14559
    citizen1 "Да, тетя, ты нас сегодня очень порадовала! Скажу тебе по секрету, у меня не было таких телок, как ты."
    img 14560
    mt "И не будет."
    img 14561
    citizen1 "Вот держи, заработала."
    return True

# итерация 1 - в одежде.
label cit1_2_counting1:
    img 11768
    citizen1 "Сыграем в считалочку! Становись к пилону!"
    img 13239
    menu:
        "Хорошо.":
            img 13240
            m "Хорошо."
            pass
        "Не сегодня.":
            img 13192
            m "Не сегодня."
            return False
    # моника нагибыается
    img 14562
    citizen1 "Раз!"
    img 14554
    citizen2 "Два!"
    img 14562
    citizen1 "Три!"
    img 14555
    m "Ай!"
    img 14554
    citizen2 "Четыре!"
    img 14562
    citizen1 "Пять!"
    img 14554
    citizen2 "Скоро будем мы бухать!"
    img 14563
    citizen1 "О да, брат, это волшебное чувство!"
    citizen1 "Смотри, похоже тете нравится."
    img 14564
    m "Неправда."
    img 14564
    citizen1 "Ха-ха-ха. Я заметил твое выражение лица. Ты явно не страдаешь от этого."
    citizen1 "Хватит себя обманывать!"
    citizen1 "Думаю, скоро ты это признаешь, а пока получай свои 10 долларов."
    img 14558
    mt "Грязные панки..."
    return True


# Панк предлагает запихать бутылку в задницу
# Моника отвечает Вы охренели?!
# Панк говорит что ты же согласилась, когда танцевала.
# Только сказала что сделаешь это в следующий раз

# Моника отвечает что такого не было и не могло быть
# Панки говорят что не парься. Мы сделаем это в одежде

# Моника отвечает что не будет это делать ни в одежде ни без!

# Панки говорят что-то про деньги и что это будет быстро
