default citizen5BoobsNakesShowedLastDay = 0
default citizen5BoobsNakedDancedLastDay = 0
default citizen5BoobsNakesShowedCount = -1
default citizen5BoobsNakedDancedCount = -1
default citizen5BoobsNakesShowedCount1 = 0
default citizen5BoobsNakedDancedCount1 = 0

default citizen5DanceCloth = 0
label citizen5_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_5_1
    if citizen5_offered_last_day == day:
        imgr Dial_Citizen_5_4
        citizen5 "Мистер занят! Вы отнимать у Мистера время!"
        return
    citizen5 "Что Вы хотеть от Мистера?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen5_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen5_refuse_probability) > 0:
                imgr Dial_Citizen_5_2
                citizen5 "Да, да, конечно...Я взять этот флаер... Но ты мне должна. Акира сан никогда не делает ничего просто так."
                mt "О чем это он?"
                imgr Dial_Citizen_5_3
                citizen5 "Я думать Вы предлагать место?"
                call reduce_flyers() from _call_reduce_flyers_11
                menu:
                    "Я ничего не предлагаю! Просто возьмите флаер!":
                        $ kebabWorkHarassmentAmount +=1
                        #img Моника злится
                        m "Я ничего не предлагаю! Просто возьмите флаер!"
                    "Место для чего?":
                        m "Место для чего?"
                        citizen5 "Место для развлечения! Я очень любить трогать большие попы!"
                        m "Что вы такое говорите?"
                        mt "Лучше пойду отсюда..."
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."
            else:
                imgr Dial_Citizen_5_4
                citizen5 "У Мистера нет времени вашего места!"
                #img Моника злится
                imgl Dial_Monica_Sandwich_0
                m "Какого еще места?"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen5_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_5_1
    m "Привет! Я могу тебе предложить одну вещь."
    imgr Dial_Citizen_5_3
    citizen5 "Вы предлагать место?"
    m "Ну да, мы можем сходить с вами в одно место."
    citizen5 "Да, да, место для утех. Вы мне показы, я вам американские деньги."
    mt "И откуда он такой?"
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_216
    call pylonController(2, 1) from _call_pylonController_194
    with fadelong
    citizen5 "Очень хорошо! Давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False
    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen5_dialogue_pilon_loop5:
    call pylonController(1, 1) from _call_pylonController_195
    if (pylonpart4startsCompleted == True and citizen5BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen5BoobsNakesShowedCount>=0:
        $ questHelp("work_slums_39", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_196
            citizen5 "Я хотеть смотреть твои груди."
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_197
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(3, 3) from _call_pylonController_198
            with fade
            m "Я не собираюсь раздеваться, только так."

            $ questHelp("work_slums_8", True)
            $ questHelp("work_slums_18", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")


            call showRandomImages(boobsImages, 4) from _call_showRandomImages_48
            call pylonController(3, 3) from _call_pylonController_199
            # img показывает сиськи
            citizen5 "Да, твои обе груди прекрасны!"
            call pylonController(3, 3) from _call_pylonController_200
            citizen5 "Я очень ошеломлен!"
            call pylonController(3, 3) from _call_pylonController_201
            citizen5 "Я почти потерял дар говорить при виде этих великолепных сисек!"
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_202
            citizen5 "Оголи свою попку."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_203
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(4, 5) from _call_pylonController_204
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_49
            call pylonController(4, 5) from _call_pylonController_205
            # img показывает зад
            citizen5 "Твоя попка красивее всех поп в моей стране!"
            call pylonController(4, 5) from _call_pylonController_206
            citizen5 "Готов смотреть на нее все время."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_207
            citizen5 "Я желаю ведеть тебя танцующей."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_208
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_209
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            $ citizen5DanceCloth += 1
            if citizen5DanceCloth >= 3:
                $ questHelp("work_slums_18", True)



            call showRandomImages(pylonClothDanceImages4, 4) from _call_showRandomImages_50
#            call pylonController(4, 5)
            citizen5 "Ооо! Какие красивые изгибания!"
            citizen5 "Они похожи гору Фудзи, только две. Ты быда там?"
            call pylonController(4, 1) from _call_pylonController_210
            m "Нет, и не очень то и хочется."
            citizen5 "Вот и зря! Побывать нужно незамедлительно!"
            call pylonController(4, 5) from _call_pylonController_211
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_212
            with fade
            mt "Как же он странно разговаривает..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen5BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen5BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen5BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen5BoobsNakesShowedCount == -1:
                call cit5_naked_boobs_1st() from _call_cit5_naked_boobs_1st
                if _return != False:
                    $ citizen5BoobsNakesShowedCount += 1
            else:
                if citizen5BoobsNakesShowedCount%2 == 0:
                    call cit5_naked_boobs_variant1() from _call_cit5_naked_boobs_variant1
                if citizen5BoobsNakesShowedCount%2 == 1:
                    call cit5_naked_boobs_variant2() from _call_cit5_naked_boobs_variant2
                $ citizen5BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen5BoobsNakesShowedCount1 = citizen5BoobsNakesShowedCount + 1
                if citizen5BoobsNakesShowedCount1 >= 3:
                    $ questHelp("work_slums_29", True)
                $ citizen5BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen5_dialogue_pilon_loop5



            call pylonController(4, 1) from _call_pylonController_213
            citizen5 "Оголи свои манящие груди."
            mt "Ему бы книги писать..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_214
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(4, 5) from _call_pylonController_215
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_51
            call pylonController(4, 5) from _call_pylonController_216
            citizen5 "Я только что лицезрел гору Фудзи, точнее две!"
            call pylonController(4, 1) from _call_pylonController_217
            w
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen5_dialogue_pilon_loop5


        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen5BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen5BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen5BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen5BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen5BoobsNakedDancedCount == -1:
                call cit5_naked_boobs_dance_1st() from _call_cit5_naked_boobs_dance_1st
                if _return != False:
                    $ citizen5BoobsNakedDancedCount += 1
            else:
                if citizen5BoobsNakedDancedCount%2 == 0:
                    call cit5_naked_boobs_dance_variant1() from _call_cit5_naked_boobs_dance_variant1
                if citizen5BoobsNakedDancedCount%2 == 1:
                    call cit5_naked_boobs_dance_variant2() from _call_cit5_naked_boobs_dance_variant2
                $ citizen5BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen5BoobsNakedDancedCount1 = citizen5BoobsNakedDancedCount + 1
                if citizen5BoobsNakedDancedCount1 >= 3:
                    $ questHelp("work_slums_39", True)
#                    $ questHelp("work_slums_53", skipIfExists=True)
                $ citizen5BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen5_dialogue_pilon_loop5


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
                call pylonController(2, 1) from _call_pylonController_218
                citizen5 "Ты дать мистеру величайшее наслаждение. Мы видеться скоро вновь!"
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_219
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_220
            citizen5 "Мистер разочарован, он ничего не посмотрел."
            return False
    return

# первый раз
label cit5_naked_boobs_1st:
    music Groove2_85
    img 11879
    with fade
    citizen5 "Может быть ты согласна показать мне свои груди?"
    img 11880
    m "Думаю, ты уже их видел."
#    img 11881
    citizen5 "Да, конечно, но было бы прекрасно их оголить. У мистера есть деньги! Много денег!"
    music Hidden_Agenda
    img 11882
    with diss
    mt "Он выглядит не очень умным... Возможно это мой шанс получить несколько сотен, а может быть и тысяч долларов..."
    music Groove2_85
    img 11883
    with diss
    m "И сколько же у мистера денег?!"
    img 11884
    citizen5 "У мистера очень много денег! Тебе нужно верить мистеру!"
    citizen5 "Дак ты оголишь свои груди?"
    img 11885
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 11886
            m "Хватит и того, что ты уже видел!"
            return False
    img 11887
    with fade
    m "Отвернись!"
    img 11888
    citizen5 "Да, конечно, мистер отвернется."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 11889
    with fadelong
    w
    img 11890
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    music Loved_Up
    img 11891
    with diss
    w
    img 11892
    w
    img 11893
    citizen5 "Невероятно! Именно такими я себе их и представлял!"
    citizen5 "Они изумительны!"
    img 11894
    mt "Ну прямо мастер комплиментов..."
    # сиськи еще
#    img 11895
#    w
    img 11896
    w
    img 11897
    citizen5 "Какая красота!"
    # моника продолжает показывать
#    img 11898
#    w
    img 11900
    w
    img 11899
    w
    sound snd_fabric1
    music Groove2_85
    img 11901
    with fade
    m "Ну ладно, хватит с тебя."
    img 11902
    citizen5 "Как? Мистер еще не до конца насладился!"
    img 11903
    m "А где деньги мистера?"
    img 11904
    citizen5 "У меня нет сегодня моих миллионов! Только несколько зеленых бумажек. Но ты их получишь."
    img 11905
    mt "Миллионов? Интересно, это правда? Хотя вряд ли у него столько денег..."
    img 11906
    m "Ну раз миллионов нет, тогда на сегодня все."
    img 11907
    with fade
    citizen5 "Ооо...Ну ничего, скоро ты их увидишь!"
    $ nakedBoobsFirstly_Cit5 = True
    return True

# вариант 1
label cit5_naked_boobs_variant1:
    music Groove2_85
    img 11908
    with fade
    citizen5 "Оголи свои манящие груди."
    img 11909
    mt "Ему бы книги писать..."
    img 11910
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11911
            m "Хватит и того, что ты уже видел!"
            return False

    # отворачивается, моника переодевается...
    img 11912
    with fade
    m "Хорошо."
    sound snd_fabric1
    img 11913
    w
    music Loved_Up
    img 11914
    with diss
    m "Только руками не трогать!"
    # сиськи
    img 11915
    w
    img 11916
    w
    img 11917
    citizen5 "Лучезарно! Кажется, в такие моменты я попадаю в рай!"
    img 11918
    with diss
    mt "Ого... Да он прямо поплыл! Кажется, он говорил о миллионах..."
    # сиськи еще
    img 11919
    w
    img 11920
    w
    img 11921
    with diss
    m "Тебе нравится?"
    img 11922
    citizen5 "О да! Это великолепно!"
    # сиськи еще
    img 11923
    w
    img 11924
    w
    img 11925
    citizen5 "Мне кажется, я видел их во сне! Или я гулял между холмов..."
    img 11926
    m "Кстати, кажется, ты в прошлый раз говорил о миллионах?"
    img 11927
    citizen5 "Да, да! У мистера есть миллионы!"
    # сиськи еще
    img 11928
    w
    img 11929
    w
    img 11930
    with diss
    m "Может быть ты дашь мне несколько?"
    # сиськи еще
    img 11931
    w
    img 11932
    w
    img 11933
    citizen5 "Да, конечно! Мистер даст тебе много миллионов! Но они у мистера дома."
    img 11934
    mt "Что он несет? Неужели у него и правда есть столько денег..."
    img 11935
    m "Чтож, тогда на сегодня все."
    img 11936
    citizen5 "Ох, какая жалость! Мне очень стыдно, но я принесу мои миллионы в следующий раз!"
    img 11937
    with fade
    m "Хорошо, буду ждать."
    return True

# вариант 2
label cit5_naked_boobs_variant2:
    music Groove2_85
    img 11938
    with fade
    citizen5 "Оголи свои манящие груди."
    img 11939
    mt "Ему бы книги писать..."
    img 11940
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11941
            m "Хватит и того, что ты уже видел!"
            return False
    img 11942
    with fade
    m "Отвернись!"
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 11943
    with fade
    w
    img 11944
    with diss
    w
    music Loved_Up
    img 11945
    with diss
    m "Можешь повернуться."
    m "Только руками не трогать!"
    # сиськи
    img 11946
    with diss
    w
    img 11947
    w
    img 11948
    citizen5 "Мистер вспомнил! Он принес деньги! Очень много денег!"
    img 11949
    mt "Серьезно?! Думаю, стоит ему подиграть..."
    img 11950
    m "Мистер обещал дать мне много миллионов!"
    # сиськи еще
    img 11951
    w
    img 11952
    w
    img 11953
    m "Мистеру нравится?"
    img 11954
    citizen5 "Конечно да!"
    # сиськи еще
    img 11955
    w
    img 11956
    w
    img 11957
    with diss
    m "Мистер готов дать мне 400 миллионов?"
    # сиськи еще
    img 11958
    w
    img 11959
    w
    img 11960
    with fade
    citizen5 "Да, да, готов! Но у мистера небольшое условие."
    music Groove2_85
    img 12494
    citizen5 "Мистер хочет увидеть на тебе это."
    # показывает зажим для сосков
    img 12495
    with diss
    citizen5 "Мистер будет очень благодарен когда увидит на тебе это."
    img 12496
    mt "Что это еще такое?! Что делать?"
    img 12497
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            img 12498
            m "Ну уж нет! Мне не нужны твои извращенные штучки!"
            return False
    img 12499
    with fade
    mt "Черт, а что если у него и правда есть много денег..."
    m "Хорошо, но только быстро."
    # моника зажимает соски
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 12500
    with fadelong
    w
    img 12502
    with diss
    w
    img 12501
    citizen5 "Это самое лучшее представление, которое я видел!"
    citizen5 "Подожди, постой так немного!"
    # сиськи - еще поза
    img 12503
    w
    img 12504
    w
    img 12505
    citizen5 "Ох, это нечто!"
    # сиськи еще
    img 12506
    w
    img 12507
    w
    img 12508
    with fade
    citizen5 "Мистер очень доволен, вот твои миллионы!"
    # Дает ей миллионы долларов Зимбабве )
    img 12509
    with diss
    w
    music Groove2_85
    img 12510
    with hpunch
    m "Что это такое?"
    img 12511
    citizen5 "Я даю тебе миллионы долларов!"
    music Power_Bots_Loop
    img 12512
    m "Зимбабве?! Да не них здесь ничего не купить!"
    img 12513
    citizen5 "Мистер не знает, но ты теперь миллионер!!!"
    img 12514
    with fade
    mt "Черт, похоже он очень глуп, даже говорить с ним нет смысла..."
    return True

# первый раз танцы с сиськами
label cit5_naked_boobs_dance_1st:
    music Groove2_85
    img 13307
    with fade
    citizen5 "Мистер желает увидеть совмещение."
    img 13308
    m "Что? Я не понимаю."
    img 13309
    citizen5 "Необходимо совместить манящие груди и танцы на железной палке."
    img 13310
    m "Ты хочешь, чтобы я снанцевала?"
    img 13311
    citizen5 "Да! Но перед этим оголи свои манящие груди!"
    img 13312
    mt "Теперь понятно о чем ты..."
    img 13313
    with fade
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13314
            m "Хватит с тебя того, что ты уже видел!"
            img 13315
            citizen5 "Мистер разочарован!"
            return False
    img 13316
    with fade
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет..."
    img 13317
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13318
    with diss
    m "???"
    sound snd_fabric1
    music Loved_Up
    img 13319
    with diss
    citizen5 "О, конечно!"
    # поворачиваются, моника стоит с голыми сиськами
    img 13320
    with fadelong
    citizen5 "Мистер рад, можно начинать!"
    # движение на пилоне
    music Molten_Alloy
    img 13321
    with fadelong
    w
    img 13322
    with diss
    w
    img 13323
    with diss
    citizen5 "Это очень хорошо! Ты очень молодец!"
    # движение на пилоне еще
    img 13324
    with diss
    w
    img 13325
    with diss
    w
    img 13326
    with diss
    citizen5 "Как ты замечательно двигаешься! Ты профессионал!"
    # движение на пилоне еще
    img 13328
    with diss
    w
    img 13327
    with diss
    citizen5 "Ооо...Ты получишь от мистера много денег!"
    # моника слезает с шеста
    music Groove2_85
    img 13329
    with fadelong
    m "Все! Плати! Мне нужны настоящие деньги!"
    img 13330
    mt "И не нужны твои тугрики..."
    img 13331
    with fade
    citizen5 "Настоящие? Это можно, вот возьми."
    $ nakedBoobsDanceFirstly_Cit5 = True
    return True

# первый вариант танцы с сиськами
label cit5_naked_boobs_dance_variant1:
    music Groove2_85
    img 13307
    with fade
    citizen5 "Мистер желает увидеть совмещение."
    img 13312
    mt "Неужели снова придется раздется и станцевать?"
    img 13313
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13314
            m "Хватит с тебя того, что ты уже видел!"
            img 13315
            citizen5 "Мистер разочарован!"
            return False
    img 13317
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13318
    w
    sound snd_fabric1
    img 13319
    with diss
    citizen5 "О, конечно!"
    # поворачиваются, моника стоит с голыми сиськами
    img 13320
    with fadelong
    citizen5 "У мистера сегодня хорошее настроение!"
    # движение на пилоне
    music Molten_Alloy
    img 13332
    with fadelong
    citizen5 "Крутись! Превосходно!"
    # движение на пилоне еще
    img 13333
    with diss
    w
    img 13334
    with diss
    w
    img 13335
    with diss
    w
    img 13336
    with diss
    citizen5 "Мистеру кажется, что он готов будет написать хайку!"
    # моника слезает с шеста
    music Groove2_85
    img 13337
    with fadelong
    citizen5 "Мистер придумал! Вот послушай!"
    img 13338
    with diss
    citizen5 "Стрекоза летала,"
    citizen5 "На сакуру села."
    citizen5 "Радость мистеру."
    img 13339
    with fade
    citizen5 "Или это не хайку... Мистер запутался от твоих безупречных форм!"
    img 13340
    mt "А у мистера похоже, что не все дома..."
    img 13341
    with diss
    citizen5 "Вот твои настоящие деньги."
    return True

# второй вариант танцы с сиськами
label cit5_naked_boobs_dance_variant2:
    music Groove2_85
    img 13342
    with fade
    citizen5 "Как насчет танца на пилоне?"
    img 13343
    mt "Что? А где же обычный бред, который он все время несет?"
    mt "Он что, где то это услышал?"
    img 13344
    citizen5 "И не забудь оголить свои манящие груди."
    img 13345
    mt "А, нет, все нормально."
    mt "Он все тот же кретин..."
    img 13346
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13347
            m "Хватит с тебя того, что ты уже видел!"
            img 13348
            citizen5 "Мистер разочарован!"
            return False
    img 13349
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13350
    citizen5 "О, конечно!"
    img 13351
    w
    sound snd_fabric1
    img 13352
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13353
    with fadelong
    citizen5 "Мистер думает, что ты не очень любишь это прекрасное занятие и хочет, чтобы ты чувствовала себя по-особенному!"
    img 13354
    mt "Он что-то задумал?"
    img 13355
    with diss
    citizen5 "Можно стартовать!"
    # движение на пилоне: моника танцует, а ситизен кидает доллары зимбабве
    # очень много на эту тему стереотипных фото аля Девушка танцует, мужчина сорит деньгами
    music Molten_Alloy
    img 13356
    with fadelong
    w
    img 13357
    with diss
    w
    img 13358
    with diss
    sound snd_take_paper
    citizen5 "Это тебе!"
    #  моника танцует
    sound snd_take_paper
    img 13359
    with diss
    w
    sound snd_take_paper
    img 13360
    with diss
    citizen5 "Получай!"
    #  моника танцует,
    sound snd_take_paper
    img 13361
    with diss
    w
    sound snd_take_paper
    img 13362
    with diss
    citizen5 "И вот еще!"
    #  моника танцует,
    img 13363
    with diss
    w
    img 13364
    with diss
    citizen5 "Все, у меня закончились деньги!"
    #  моника слезает с шеста
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 13365
    with fadelong
    citizen5 "Тебе понравилось? Удалось ли мне создать атмосферу?"
    img 13366
    m "Какую еще атмосферу?"
    img 13367
    citizen5 "Атмосферу твоего рабочего места!"
    img 13369
    with diss
    mt "Знал бы ты что у меня за атмосфера на рабочем месте..."
    img 13368
    m "Нет.."
    img 13370
    with fade
    citizen5 "Ай-ай, мистер немного разочарован. Но ничего, думаю американские деньги также помогут ее созданию..."
    return True
