default citizen3BoobsNakesShowedLastDay = 0
default citizen3BoobsNakedDancedLastDay = 0
default citizen3BoobsNakesShowedCount = -1
default citizen3BoobsNakedDancedCount = -1
default citizen3BoobsNakesShowedCount1 = 0
default citizen3BoobsNakedDancedCount1 = 0

default citizen3DanceCloth = 0
default monicaGotJoint = False
label citizen3_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_3_1
    if monicaGotJoint == True:
        imgr Dial_Citizen_3_4
        citizen3 "Тебе нужно к Найджелу..."
        return
    if citizen3_offered_last_day == day:
        imgr Dial_Citizen_3_4
        citizen3 "В другой раз, я занят!"
        return
    citizen3 "Да, конечно, красотка!"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen3_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
#                    if renpy.random.randint(0, 3) =:
            imgr Dial_Citizen_3_4
            citizen3 "Не хочу, мне он не нужен."
            imgl Dial_Monica_Sandwich_0
            menu:
                "Попросить вежливо.":
                    #img Моника спрашивает
                    imgl Dial_Monica_Sandwich_1
                    m "Мистер, пожалуйста, возьмите флаер, Вы меня очень выручите."
                    imgr Dial_Citizen_3_2
                    citizen3 "Хорошо, я помогу тебе в обмен на небольшую услугу."
                    m "Какую еще услугу? Ты всего лишь возьмешь у меня флаер..."
                    citizen3 "Да, и попрошу тебя кое что передать моему другу Найджелу. Он на другой стороне улицы и ты его узнаешь по синему пуховику, в котором он круглый год."
                    imgl Dial_Monica_Sandwich_0
                    m "И что же я должна ему передать?"
                    mt "(Что за ?! )"
                    # citizen3показывает монике косяк
                    imgr Dial_Citizen_3_joint
                    m "Что это? Наркотики?!"
#                            imgr Dial_Citizen_3_3
                    citizen3 "(Шепотом) С каких пор травку слали приравнивать к наркотикам? Она абсолютно легальна. Ну дак что, поможешь мне?"
                    menu:
                        "Ладно.":
                            m "(Всего несколько метров...)Хорошо, я сделаю это."
                            #Моника берет косяк и отдает флаер.
                            $ add_inventory("joint", 1, True)
                            imgr Dial_Citizen_3_2
                            citizen3 "Не забудь сказать, что ты от Джека."
                            m "Хорошо"
                            citizen3 "Да, и самое главное: Ты должна будешь сказать Найджелу наш пароль, чтобы он понял, что все чисто."
                            m "Какой еще пароль?"
                            imgr Dial_Citizen_3_3
                            citizen3 "Потрогай мою сиську."
                            imgl Dial_Monica_Sandwich_2
                            m "(Что за?)"
                            imgl Dial_Monica_Sandwich_0
                            menu:
                                "Черт с ним.":
                                    imgl Dial_Monica_Sandwich_0
                                    m "И у кого хватило ума придумал такой пароль?!"
                                    citizen3 "А ты как думаешь? Конечно Найджел, но не переживай, как только ты произнесешь пароль, он сразу все поймет."
                                    call reduce_flyers() from _call_reduce_flyers_13
                                    m "Ладно, но если ты меня обманываешь..."
                                    #citizen33
                                    imgr Dial_Citizen_3_4
                                    citizen3 "Что ты, детка, зачем мне это?"
                                    $ monicaGotJoint = True
                                    return
                                "Ну уж нет, это слишком.":
                                    imgl Dial_Monica_Sandwich_2
                                    #злая моника
                                    $ remove_inventory("joint", 1, True)
                                    m "Я не буду говорить такие вещи!"
                                    return
                        "Ну уж нет.":
                            imgl Dial_Monica_Sandwich_2
                            m "Ты что, за дуру меня держишь?"
                            # смена арта у ситизена
                            imgr Dial_Citizen_3_4
                            citizen3 "Возвращайся, если передумаешь."
                            $ kebabWorkMonicaRefusedAmount += 1
                            return
                "Попросить настойчиво.":
                    imgl Dial_Monica_Sandwich_1
                    #img Моника спрашивает с недовольным выражением лица.
                    m "Неужели для Вас это так сложно?!."
                    imgr Dial_Citizen_3_4
                    citizen3 "Отвали."
                    imgl Dial_Monica_Sandwich_0
                    mt "(Вот засранец.)"
                    imgr Dial_Citizen_3_2
                    $ kebabWorkMonicaRefusedAmount += 1
#                        call reduce_flyers()
#                        citizen3 "Хорошо."
#                        img Dial_Citizen_3_3
#                        citizen3 "А что на нем? Ваш номер телефона?"
#                        "Вы девочка по вызову?"
#                        label citizen3_loop1:
#                            menu:
#                                "НЕТ!":
#                                    #img Моника злится
#                                    m "НЕТ!"
#                                "В общем нет, но... (disabled)":
#                                    jump citizen3_loop1
#                    else:
#                        img Dial_Citizen_3_3
#                        citizen3 "Я занят! Пожалуйста, не отвлекайте меня!"
#        "Уйти.":
#            pass
    return

# диалог доступен только когда моника не работает на раздаче флаеров
label citizen3_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_3_1
    m "Привет! Ты меня помнишь?"
    citizen3 "Конечно, помню, тебя сложно забыть."
    m "Могу тебе, кое что показать."
    citizen3 "Детка, ты говоришь о том, что я думаю?"
    imgr Dial_Citizen_3_3
    m "Возможно..."
    citizen3 "У меня много дел, но такое я пропустить не могу."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_242
    call pylonController(2, 1) from _call_pylonController_248
    with fade
    citizen3 "Ну что, тетя..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False
    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen3_dialogue_pilon_loop3:
    call pylonController(1, 1) from _call_pylonController_249
    if (pylonpart4startsCompleted == True and citizen3BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen3BoobsNakesShowedCount>=0:
        $ questHelp("work_slums_38", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_250 #(2- камера со спины Моники, чуваки лицом, 3 - эмоция и поза чувака, 1 - Моника стоит спиной скрестив руки)
            citizen3 "Покажи ка свои сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3

            call pylonController(3, 3) from _call_pylonController_251 #(1 - камера со спины чуваков, Моника лицом, 1 - эмоция, 2 - Моника недовольно отвечает, жестикулируя)
            with fade
            m "Я не собираюсь раздеваться, только так."
            $ questHelp("work_slums_7", True)
            $ questHelp("work_slums_17", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")

            # img показывает сиськи
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_56
            call pylonController(3, 3) from _call_pylonController_252 #(2- камера со спины Моники, чуваки лицом, 3 - эмоция и поза чувака, 3 - Моника стоит спиной, показывая грудь в одежде)
            citizen3 "Детка, нет слов! Теперь сними свою курточку."
            call pylonController(3, 2) from _call_pylonController_253 #(1 - камера со спины чуваков, Моника лицом, 1 - эмоция, 2 - Моника недовольно отвечает, жестикулируя)
            m "Ну уж нет."
            call pylonController(3, 1) from _call_pylonController_254 #(2- камера со спины Моники, чуваки лицом, 3 - эмоция и поза чувака, 1 - Моника стоит спиной скрестив руки)
            citizen3 "Надо же с чего-то начинать..."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen3_dialogue_pilon_loop3
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_255
            citizen3 "Детка, повернись ко мне спиной. И покажи свою попку."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3
            call pylonController(4, 5) from _call_pylonController_256
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4) from _call_showRandomImages_57
            call pylonController(4, 5) from _call_pylonController_257
            citizen3 "Детка, ты красотка!"
            call pylonController(4, 5) from _call_pylonController_258
            citizen3 "Какая красота!"
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen3_dialogue_pilon_loop3
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_259
            citizen3 "Потанцуй для меня, не зря же сюда пришли."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_260
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_261
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            $ citizen3DanceCloth += 1
            if citizen3DanceCloth >= 3:
                $ questHelp("work_slums_17", True)


            call showRandomImages(pylonClothDanceImages2, 4) from _call_showRandomImages_58
#            call pylonController(4, 5)
            citizen3 "Прекрасно. Ты никогда не задумывалась этим зарабатывать? Раздача флаеров не очень прибыльное дело."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_262
            with fade
            mt "Ни за что..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen3_dialogue_pilon_loop3
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen3BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen3BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen3BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen3BoobsNakesShowedCount == -1:
                call cit3_naked_boobs_1st() from _call_cit3_naked_boobs_1st
                if _return != False:
                    $ citizen3BoobsNakesShowedCount += 1
            else:
                if citizen3BoobsNakesShowedCount%2 == 0:
                    call cit3_naked_boobs_variant1() from _call_cit3_naked_boobs_variant1
                if citizen3BoobsNakesShowedCount%2 == 1:
                    call cit3_naked_boobs_variant2() from _call_cit3_naked_boobs_variant2
                $ citizen3BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen3BoobsNakesShowedCount1 = citizen3BoobsNakesShowedCount + 1
                if citizen3BoobsNakesShowedCount1 >= 3:
                    $ questHelp("work_slums_28", True)

                $ citizen3BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen3_dialogue_pilon_loop3



            call pylonController(4, 1) from _call_pylonController_263
            citizen3 "Детка, хочу взглянуть еще раз на твои сиськи, только сними курточку."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_264
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3
            call pylonController(4, 5) from _call_pylonController_265
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_59
            call pylonController(4, 5) from _call_pylonController_266
            citizen3 "Очень хорошо. Сиськи как у Сары! Ты знакома с Сарой?"
            "Хотя почему я спрашиваю? Конечно вы знакомы."
            call pylonController(4, 1) from _call_pylonController_267
            citizen3 "Да ладно тебе, поговори со мной! Что думаешь?"
            m "Я не знаю о ком ты говоришь."
            call pylonController(4, 5) from _call_pylonController_268
            citizen3 "Ну как же, Сара! У нее лучшие сиськи на районе!"
            citizen3 "Надо будет как нибудь устроить соревнование. да, это отличная идея!"
            mt "Интересно, о ком это он? Хотя какая разница, у меня нет соперниц."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen3_dialogue_pilon_loop3

        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen3BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen3BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen3BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen3BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen3BoobsNakedDancedCount == -1:
                call cit3_naked_boobs_dance_1st() from _call_cit3_naked_boobs_dance_1st
                if _return != False:
                    $ citizen3BoobsNakedDancedCount += 1
            else:
                if citizen3BoobsNakedDancedCount%2 == 0:
                    call cit3_naked_boobs_dance_variant1() from _call_cit3_naked_boobs_dance_variant1
                if citizen3BoobsNakedDancedCount%2 == 1:
                    call cit3_naked_boobs_dance_variant2() from _call_cit3_naked_boobs_dance_variant2
                $ citizen3BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen3BoobsNakedDancedCount1 = citizen3BoobsNakedDancedCount + 1
                if citizen3BoobsNakedDancedCount1 >= 3:
                    $ questHelp("work_slums_38", True)
                $ citizen3BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen3_dialogue_pilon_loop3

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
                call pylonController(2, 1) from _call_pylonController_269
                citizen3 "Ты сделала мой день, отлично потрудилась."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_270
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_271
            citizen3 "Похоже, я только зря потратил с тобой время..."
            return False
    return

# первый раз
label cit3_naked_boobs_1st:
    music Groove2_85
    img 11810
    with fade
    citizen3 "Ты знаешь, есть одна вещь, которая меня сильно интригует!"
    img 11811
    m "?"
    img 11812
    citizen3 "Уж очень мне интересно, как выглядят твои сиськи без этого чудесного топа!"
    img 11813
    m "Они выглядят отлично! Но тебя это не касается!"
    img 11814
    citizen3 "Покажи их мне!"
    img 11815
    menu:
        "Почему бы и нет. Это возможность заработать деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 11816
            m "Хватит и того, что ты уже видел!"
            return False
    img 11817
    m "Отвернись!"
    # отворачивается, моника переодевается...
    img 11818
    with diss
    w
    sound snd_fabric1
    img 11819
    with diss
    w
    music Loved_Up
    img 11820
    with fade
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    img 11821
    with diss
    w
    img 11822
    with diss
    w
    img 11823
    w
    music Groove2_85
    img 11824
    with fade
    citizen3 "Ха! Я уверен, что где-то уже видел твои сиськи... Или не твои.."
    citizen3 "Не подскажешь, где я мог их видеть?"
    img 11825
    m "Нигде."
    # сиськи еще
    img 11826
    w
    img 11827
    w
    img 11828
    w
    img 11829
    with fade
    citizen3 "Странно, очень странно..."
    # citizen смотрит в сторону задумавшись, моника продолжает показывать
    img 11830
    citizen3 "Ладно, в другой раз вспомню..."
    $ nakedBoobsFirstly_Cit3 = True
    return True

# вариант 1
label cit3_naked_boobs_variant1:
    music Groove2_85
    img 11831
    with fade
    citizen3 "Дорогуша, покажи мне свои красивые сиськи!"
    citizen3 "Не за бесплатно конечно же."
    img 11832
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11833
            m "Хватит и того, что ты уже видел!"
            return False

    # отворачивается, моника переодевается...
    img 11834
    with fade
    m "Хорошо."
    music Loved_Up
    sound snd_fabric1
    img 11835
    with fade
    m "Только руками не трогать!"
    # сиськи
    img 11836
    w
    img 11837
    w
    img 11838
    w
    img 11839
    citizen3 "Да! Я вспомнил!"
    img 11840
    m "?"
    # сиськи еще
    img 11841
    w
    img 11842
    w
    img 11843
    w
    music Groove2_85
    img 11844
    with fade
    citizen3 "Сиськи как у Сары! Ты знакома с Сарой?"
    img 11845
    citizen3 "Хотя почему я спрашиваю? Конечно вы знакомы."
    img 11846
    m "Я не знаю о ком ты говоришь."
    # сиськи еще
    music Loved_Up
    img 11847
    with diss
    w
    img 11848
    w
    img 11849
    w
    music Groove2_85
    img 11850
    with fade
    citizen3 "Ну как же, Сара! У нее лучшие сиськи на районе!"
    citizen3 "Надо будет как нибудь устроить соревнование. Да, это отличная идея!"
    img 11851
    mt "Интересно, о ком это он? Хотя какая разница, у меня нет соперниц."
    return True

# вариант 2
label cit3_naked_boobs_variant2:
    music Groove2_85
    img 11852
    with fade
    citizen3 "Детка, хочу взглянуть еще раз на твои сиськи, только сними курточку."
    img 11853
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11854
            m "Хватит и того, что ты уже видел!"
            return False
    img 11855
    with fade
    m "Отвернись!"
    # отворачивается, моника переодевается...
    img 11856
    w
    sound snd_fabric1
    img 11857
    with fadelong
    w
    img 11858
    with diss
    m "Можешь повернуться."
    img 11859
    m "Только руками не трогать!"
    # сиськи
    music Loved_Up
    img 11861
    with diss
    w
    img 11862
    citizen3 "Ага... Да..."
    # сиськи еще
    img 11863
    w
    img 11864
    citizen3 "Хорошо... Вроде бы..."
    # сиськи еще
    img 11865
    w
    img 11866
    with diss
    w
    img 11867
    mt "Интересно, что это с ним сегодня? Обычно он более разоворчив..."
    img 11868
    citizen3 "А что если?"
    # ситизен внезапно хватает монику за грудь
    sound Jump2
    img 11869
    with diss
    w
    # смена картинки, моника злая
    music Power_Bots_Loop
    img 11870
    with hpunch
    m "Ах ты говнюк! Какого черта?!"
    sound snd_fabric1
    img 11871
    with fadelong
    citizen3 "Что то не так?"
    img 11872
    m "Что то не так! Ты трогал мою грудь!"
    music Groove2_85
    img 11873
    citizen3 "А, ты про это..."
    citizen3 "Это твоя вина! Я никак не мог вспомнить видел ли я где-то твою грудь и был вынужден ее поторгать, чтобы убедиться."
    music Power_Bots_Loop
    img 11874
    with hpunch
    m "Да я тебя сейчас..."
    music Groove2_85
    img 11875
    citizen3 "Все, все, не злись! Я прошу прощения и заверяю тебя, что раньше твою грудь я не видел."
    citizen3 "И даже больше: она просто прекрасна, уж можешь поверить."
    img 11876
    citizen3  "И хоть я и не самый хороший парень, но я виноват, признаю."
    citizen3 "Как насчет компенсации? Знаю, что ты не против..."
    $ add_money(2)
    img 11877
    citizen3 "Наш конфликт улажен?"
    img 11878
    with fade
    mt "Были бы мы не в этих трущебах, я бы тебя прибила..."
    m "...Да."
    return True

# первый раз танцы с сиськами
label cit3_naked_boobs_dance_1st:
    music Groove2_85
    img 13258
    with fade
    citizen3 "Детка, разденься и покрутись ка на шесте!"
    citizen3 "Надо же его использовать по назначению."
    img 13259
    m "Не слишком ли многого ты хочешь!?"
    img 13260
    with diss
    citizen3 "Нет, детка, совсем не многого!"
    citizen3 "Знала бы ты мои фантазии... Я там..."
    # моника перебивает. не знаю, как это может выглядеть в диалогах, возможно никак
    music Power_Bots_Loop
    img 13261
    with vpunch
    m "Мне не интересно!"
    music Groove2_85
    img 13262
    with fade
    citizen3 "Ладно, тогда раздевайся и крутись!"
    img 13263
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13264
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13265
    with fade
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет..."
    img 13266
    m "Ладно. Только отвернись!"
    # отворачиваются
    img 13267
    citizen3 "Да, детка, как скажещь!"
    music Loved_Up
    img 13268
    with fade
    w
    # поворачиваются, моника стоит с голыми сиськами
    sound snd_fabric1
    img 13269
    with fadelong
    citizen3 "Танцуй уже!"
    # движение на пилоне
    music RocknRoll_loop
    img 13270
    with fadelong
    w
    img 13271
    with diss
    w
    img 13272
    with diss
    citizen3 "Да, детка, молодец!"
    # движение на пилоне еще
    img 13273
    with diss
    w
    img 13274
    with diss
    citizen3 "А какие у тебя ножки! Ух!"
    # движение на пилоне еще
    img 13275
    with diss
    citizen3 "Я бы заплатил 7, или нет, 9 долларов если ты дотронешься своей ножкой до моего дружка!"
    citizen3 "Ты же понимаешь о ком я?"
    img 13276
    with diss
    mt "Да заткнись ты уже... Я бы на такое не согласилась и за 7000 долларов..."
    mt "Хотя..."
    img 13277
    with diss
    citizen3 "Детка, почему ты молчишь? Сара за 7 баксов мне бы уже отсасывала!"
    # моника слезает с шеста
    music Groove2_85
    img 13278
    with fade
    m "Все! Плати!"
    img 13279
    citizen3 "Хорошо, детка, но ты так и не ответила на мой вопрос!"
    img 13280
    mt "Извращенец..."
    $ nakedBoobsDanceFirstly_Cit3 = True
    return True

# первый вариант танцы с сиськами
label cit3_naked_boobs_dance_variant1:
    music Groove2_85
    img 13281
    with fade
    citizen3 "Детка, разденься и покрутись ка на шесте!"
    citizen3 "Мне нужно кое-что уточнить."
    img 13282
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13283
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13284
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13285
    citizen3 "Да, детка, как скажещь!"
    music Loved_Up
    sound snd_fabric1
    img 13268
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13286
    with fadelong
    citizen3 "Знаешь, я тут видел Сару и мне интересно, кто из Вас лучше танцует..."
    citizen3 "Так что не задерживай меня и начинай!"
    img 13287
    mt "Сравнивать меня с какой-то уличной шлюхой? Конечно я танцую лучше!"
    # движение на пилоне
    music RocknRoll_loop
    img 13288
    with diss
    w
    img 13289
    with diss
    citizen3 "Вау! Не плохо!"
    # движение на пилоне еще
    img 13290
    with diss
    w
    img 13291
    with diss
    citizen3 "Отлично! Но пока еще не уровень Сары!"
    img 13292
    with diss
    mt "Ах ты паразит! Я докажу тебе..."
    # движение на пилоне extra (моника доказывает, что она танцует лучше)
    music stop
    img black_screen
    with diss
    music Molten_Alloy
    pause 1.0
    img 13293
    with fadelong
    w
    img 13294
    with diss
    citizen3 "Ничего себе! А вот это что-то новое!"
    citizen3 "Да, думаю ты лучше!"
    img 13295
    with diss
    mt "В этом никто и не сомневался!"
    # моника слезает с шеста
    music Groove2_85
    img 13278
    with fade
    m "Все! Плати!"
    img 13279
    with diss
    citizen3 "Вот, заработала. Думаю, ты чуть лучше Сары"
    return True

# второй вариант танцы с сиськами
label cit3_naked_boobs_dance_variant2:
    music Groove2_85
    img 13281
    with fade
    citizen3 "Детка, разденься и покрутись ка на шесте!"
    img 13282
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13283
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13284
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    music Loved_Up
    img 13285
    citizen3 "Да, детка, как скажещь!"
    sound snd_fabric1
    img 13268
    with fadelong
    # поворачиваются, моника стоит с голыми сиськами
    w
    img 13286
    citizen3 "Ну не стой, давай уже полезай на шест!"
    img 13287
    mt "Козел..."
    # движение на пилоне
    music RocknRoll_loop
    img 13296
    with diss
    w
    img 13297
    with diss
    citizen3 "Хорошо."
    # движение на пилоне еще
    img 13298
    with diss
    w
    img 13299
    with diss
    citizen3 "Давай детка, еще!"
    # движение на пилоне еще
    img 13301
    with diss
    w
    img 13300
    with diss
    citizen3 "Ах...Вот это ножки."
    citizen3 "Ты шикарна!"
    # моника слезает с шеста
    music Groove2_85
    img 13302
    with fade
    m "Все! Плати!"
    # ситизен показывает косяк
    img 13303
    citizen3 "Знаешь, детка, сейчас не самое удачное время... У меня не так много налички. Но у меня есть прекрасный товар. Хочешь?"
    img 13304
    with fade
    menu:
        "Мне нужны деньги!":
            pass
    music Power_Bots_Loop
    img 13306
    with vpunch
    m "Мне нужны деньги!"
    img 13305
    with fade
    citizen3 "Ты не знаешь от чего отказываешься, ну ладно, держи..."
    return True
