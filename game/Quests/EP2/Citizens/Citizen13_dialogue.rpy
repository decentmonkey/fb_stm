default citizen13BoobsNakesShowedLastDay = 0
default citizen13BoobsNakedDancedLastDay = 0
default citizen13BoobsNakesShowedCount = -1
default citizen13BoobsNakedDancedCount = -1
default citizen13BoobsNakedDancedEvent1Count = 0
default citizen13BoobsNakesShowedCount1 = 0
default citizen13BoobsNakedDancedCount1 = 0
default citizen13DanceCloth = 0

label citizen13_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_13_1
    if citizen13_offered_last_day == day:
        imgr Dial_Citizen_13_4
        citizen13 "Милая, давай в другой раз, я занят."
        return
    citizen13 "Ой, привет! Что у тебя, подруга?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen13_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen13_refuse_probability) > 0:
                imgr Dial_Citizen_13_2
                citizen13 "Кебаб? Фу...Ты разве не знаешь, они вредны для фигуры."
                m "Но никто же не заставляет тебя его покупать. Просто возьми флаер."
                citizen13 "А ты смешная. Ладно, я возьму один, только обещай мне, что ты не будешь есть эти противные кебабы."
                "Хотя ты знаешь, у них есть одно достоинство и ты наверное знаешь какое."
                m "?"
                imgr Dial_Citizen_13_3
                citizen13 "Глупенькая, ну конечно форма. На что они похожи?"
                label .loop1:
                    menu:
                        "На кебабы.":
                            imgl Dial_Monica_Sandwich_0
                            m "Не знаю... На кебабы."
                            imgr Dial_Citizen_13_4
                            citizen13 "Нууу...С тобой не интересно"
                            $ kebabWorkMonicaRefusedAmount += 1
                            return
                        "На пенис... (requires 30 corruption)" if corruption < 30:
                            jump .loop1
                        "На пенис..." if corruption >= 30:
                            $ kebabWorkHarassmentAmount +=1
                            imgl Dial_Monica_Sandwich_0
                            mt "Боже, что за извращенец?! Пожалуй, скажу то, что он хочет услышать."
                            m "Ну он немного напоминает пенис."
                            imgr Dial_Citizen_13_3
                            citizen13 "Дааа! Только я думаю, что совсем не немного. Я знал, что мы найдем общий язык."

                            imgr Dial_Citizen_13_2
                            imgl Dial_Monica_Sandwich_1
                            call reduce_flyers() from _call_reduce_flyers_6
                            citizen13 "Приятно было пообщаться."
                            return
            else:
                imgr Dial_Citizen_13_4
                citizen13 "Детка, мне совсем некуда его положить..."
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen13_dialogue_pilon:
    if ep214_quests_citizens_stage2 == True:
        jump ep215_slums1_dialogue_citizen13

    imgl Dial_begin35_17
    imgr Dial_Citizen_13_1
    m "Привет! Ты меня помнишь?"
    imgr Dial_Citizen_13_3
    citizen13 "Кончно помню, подруга! Ты разносишь флаеры с рекламой этих ужасных кебабов."
    m "Ну да, иногда."
    mt "А он выглядит дружелюбно и, похоже, я ему не интересна."
    m "Не будет ли у тебя лишних денег?"
    citizen13 "А тебе зачем, подруга? Если нужна контрацептив, дак у меня есть!"
    mt "Да за кого он меня принимает?"
    m "Нет, мне нужна наличка."
    citizen13 "Ну для тебя у меня есть немного, но ты же знаешь, что ничего не делается просто так."
    m "Ты мог бы мне одолжить."
    citizen13 "Ха-ха-ха. Подруга, я похож на идиота?"
    citizen13 "А вообще знаешь, раз тебе так нужны деньги, у меня есть идея. Пошли."
     # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_200
    call pylonController(2, 1) from _call_pylonController_94
    with fadelong
    citizen13 "Вот мы и пришли. Вечером тут полно народу. А теперь..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False
    $ earnedMoney = 0
    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen13_dialogue_pilon_loop13:
    call pylonController(1, 1) from _call_pylonController_95
    if (pylonpart4startsCompleted == True and citizen13BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen13BoobsNakesShowedCount>=0:
        $ questHelp("work_slums_44", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_96
            citizen13 "Подруга, а что у тебя под футболкой?"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_97
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13

            call pylonController(3, 3) from _call_pylonController_98
            with fade
            m "Я не собираюсь раздеваться, только так."
            $ questHelp("work_slums_13", True)
            $ questHelp("work_slums_22", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")

            # img показывает сиськи
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_17
            call pylonController(3, 3) from _call_pylonController_99
            citizen13 "Прекрасно, я вижу форму!"
            call pylonController(3, 3) from _call_pylonController_100
            citizen13 "Не дурно!"
            call pylonController(3, 1) from _call_pylonController_101
            w
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_102
            citizen13 "А что у тебя сзади? Покажи!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_103
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            call pylonController(4, 5) from _call_pylonController_104
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_18
            call pylonController(4, 5) from _call_pylonController_105
            # img показывает зад
            citizen13 "Оу, шикарная попка! Уж поверь, в этом я понимаю!"
            call pylonController(4, 5) from _call_pylonController_106

            citizen13 "Подруга, а шлепни себя по попке! Меня это заводит!"
            label citizen13_dialogue_pilon_loop13_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothAssSpankCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothAssSpankCorruptionRequired] corruption"
                        jump citizen13_dialogue_pilon_loop13_1
                    m "Ладно."
                    call pylonController(3, 1) from _call_pylonController_107
                    with fade
                    w
                    # добавить звук шлепка
                    sound snd_slap1
                    call showRandomImages(assSpankImages, 1) from _call_showRandomImages_19
                    call pylonController(3, 1) from _call_pylonController_108
                    citizen13 "Ух! Да, подруга, ты прямо огонь!"
                    $ store_citizen_action("AssClothSpank", 1)
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_109
                    m "Не собираюсь, и так достаточно."
                    citizen13 "Нууу...Ну пожалуйста?"
                    m "Нет. Ты и так видел многое."

            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_110
            citizen13 "Дорогая, сделай пару оборотов на пилоне, очень хочется на это посмотреть."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_111
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_112
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            $ citizen13DanceCloth += 1
            if citizen13DanceCloth >= 3:
                $ questHelp("work_slums_22", True)

            call showRandomImages(pylonClothDanceImages1, 4) from _call_showRandomImages_20
#            call pylonController(4, 5)
            citizen13 "Здорово, а ты молодец! Надо будет также попробовать."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_113
            with fade
            mt "Да уж, представляю что получится..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen13_dialogue_pilon_loop13
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen13BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen13BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen13BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen13BoobsNakesShowedCount == -1:
                call cit13_naked_boobs_1st() from _call_cit13_naked_boobs_1st
                if _return != False:
                    $ citizen13BoobsNakesShowedCount += 1
            else:
                if citizen13BoobsNakesShowedCount%2 == 0:
                    call cit13_naked_boobs_variant1() from _call_cit13_naked_boobs_variant1
                if citizen13BoobsNakesShowedCount%2 == 1:
                    call cit13_naked_boobs_variant2() from _call_cit13_naked_boobs_variant2
                $ citizen13BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen13BoobsNakesShowedCount1 = citizen13BoobsNakesShowedCount + 1
                if citizen13BoobsNakesShowedCount1 >= 3:
                    $ questHelp("work_slums_34", True)
                $ citizen13BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen13_dialogue_pilon_loop13



            call pylonController(4, 1) from _call_pylonController_114
            citizen13 "Прошлый раз ты меня обманула: не показала, что у тебя под футболкой. Давай теперь честно, мы же подруги."
            mt "Что он такое говорит? Он вообще нормальный?"
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_115
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5) from _call_pylonController_116
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикаснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_21
            call pylonController(4, 5) from _call_pylonController_117
            citizen13 "А тебе есть что показать! Когда нибудь у меня будут такие же!"
            call pylonController(4, 1) from _call_pylonController_118
            mt "Да не дай бог..."
            citizen13 "Подруга, а где ты такие сделала?"
            m "Что?! Они настоящие!"
            call pylonController(4, 5) from _call_pylonController_119
            citizen13 "Да?! Хорошо сохранилась, подруга!"
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen13_dialogue_pilon_loop13


        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen13BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen13BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen13BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen13BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen13BoobsNakedDancedCount == -1:
                call cit13_naked_boobs_dance_1st() from _call_cit13_naked_boobs_dance_1st
                if _return != False:
                    $ citizen13BoobsNakedDancedCount += 1
            else:
                if citizen13BoobsNakedDancedCount%2 == 0:
                    call cit13_naked_boobs_dance_variant1() from _call_cit13_naked_boobs_dance_variant1
                if citizen13BoobsNakedDancedCount%2 == 1:
                    call cit13_naked_boobs_dance_variant2() from _call_cit13_naked_boobs_dance_variant2
                $ citizen13BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen13BoobsNakedDancedCount1 = citizen13BoobsNakedDancedCount + 1
                if citizen13BoobsNakedDancedCount1 >= 3:
                    $ questHelp("work_slums_44", True)
#                    $ questHelp("work_slums_51", skipIfExists=True)
                $ citizen13BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen13_dialogue_pilon_loop13

        "Достаточно на сегодня.":
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
                call pylonController(2, 1) from _call_pylonController_120
                citizen13 "Славно потрудилась, подруга! Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_121
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_122
            citizen13 "Подруга, в следующий раз не халтурь."
            return False
    return

# первый раз
label cit13_naked_boobs_1st:
    music Groove2_85
    img 12323
    with fade
    citizen13 "Подруга, скажу тебе по секрету, я очень тебе завидую!"
    img 12324
    m "Это почему?"
    img 12325
    citizen13 "Ну как же, у тебя есть две классных подружки!"
    img 12326
    mt "Неужели он про этих куриц, с которые ходят на фитнес?!"
    m "Ты это о ком?"
    img 12327
    citizen13 "Ну как же, о твоих красивых сисечках!"
    img 12328
    mt "И он туда же..."
    img 12329
    citizen13 "Покажи их мне, не стесняйся, а я дам тебе деньжат!"
    img 12330
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 12331
            m "Хватит и того, что ты уже видел!"
            return False
    img 12333
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12332
    citizen13 "Конечно, мы же подруги."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 12334
    with fadelong
    w
    music Loved_Up
    img 12335
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    img 12336
    citizen13 "Не разрешаешь? Ну хорошо..."
    # сиськи
    img 12337
    with diss
    w
    img 12338
    with diss
    w
    img 12339
    citizen13 "Вау! Тебе очень повезло с подружками!"
    # сиськи еще
    img 12340
    w
    img 12341
    w
    img 12342
    citizen13 "Такие большие и сочные!"
    # моника продолжает показывать
    img 12343
    w
    img 12344
    citizen13 "Ух, могу говорить о них хоть до утра!"
    # сиськи еще
    img 12345
    with diss
    w
    img 12346
    with diss
    citizen13 "Ох, подруга, как же я тебе завидую!"

    music Groove2_85
    img 12347
    with fade
    m "Ну ладно, хватит!"
    img 12348
    citizen13 "Ну хорошо, но ты должна обещать, что я увижу их снова!"
    img 12349
    m "Хорошего понемногу."
    $ nakedBoobsFirstly_Cit13 = True
    return True

# вариант 1
label cit13_naked_boobs_variant1:
    music Groove2_85
    img 12350
    with fade
    citizen13 "Дорогая, покажи мне своих подружек, никак не могу забыть нашу первую встречу!"
    img 12351
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12352
            m "Хватит и того, что ты уже видел!"
            return False
    img 12353
    with fade
    m "Хорошо."
    m "Только руками не трогай"
    img 12354
    citizen13 "Конечно, мы же подруги."
    sound snd_fabric1
    music Loved_Up
    img 12355
    with fadelong
    citizen13 "А тебе есть что показать! Когда нибудь у меня будут такие же!"
    img 12356
    with diss
    mt "Да неужели..."
    # сиськи
    img 12357
    with diss
    w
    img 12358
    with diss
    w
    img 12359
    with diss
    w
    img 12360
    citizen13 "Подруга, а где ты такие сделала?"
    music Groove2_85
    img 12361
    with fade
    m "Что?! Они настоящие!"
    img 12362
    citizen13 "Ой, да не обманывай! Ну честно, ты делала их у Джузеппе?"
    img 12363
    m "Я не знаю о ком ты говоришь..."
    img 12364
    citizen13 "А, ну да, конфеденциальность, понимаю..."
    citizen13 "Значит у него! Да, отличная работа!"
    img 12365
    with diss
    m "Они настоящие!"
    img 12366
    citizen13 "Ууу! Ладно, подруга, не злись!"
    citizen13 "Все таки они у тебя классные!"
    # сиськи
    music Loved_Up
    img 12367
    with diss
    w
    img 12368
    with diss
    w
    music Groove2_85
    img 12369
    with fade
    m "Ну ладно, хватит!"
    img 12370
    citizen13 "Ну хорошо, но ты должна обещать, что я увижу их снова!"
    img 12371
    with fade
    mt "Посмотрим..."
    return True

# вариант 2
label cit13_naked_boobs_variant2:
    music Groove2_85
    img 12373
    with fade
    citizen13 "Дорогая, сегодня особенный день и ты просто обязана показать мне свои сисечки!"
    img 12372
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12374
            m "Хватит и того, что ты уже видел!"
            return False
    img 12375
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12376
    citizen13 "Конечно, мы же подруги."
    # отворачивается, моника переодевается
    sound snd_fabric1
    img 12377
    with fadelong
    w
    music Loved_Up
    img 12378
    with diss
    w
    img 12379
    citizen13 "Ох, какие же они у тебя...Просто чудо."
    img 12380
    with diss
    mt "Тут не поспоришь."
    # сиськи
    img 12381
    with diss
    w
    img 12382
    with diss
    w
    img 12383
    with diss
    w
    music Groove2_85
    img 12384
    with fade
    citizen13 "Ты знаешь, где то я уже такие видел..."
    citizen13 "..."
    img 12385
    citizen13 "Точно, вспомнил! Вчера вечером я смотрел один фильм..."
    citizen13 "Дак там 10 мужчин... Хотя что я рассказываю, уверен, ты такое каждый день видишь."
    img 12386
    with diss
    mt "10 мужчин?! О боже..."
    # сиськи
    music Loved_Up
    img 12387
    with diss
    w
    img 12388
    with diss
    w
    img 12389
    citizen13 "Кстати, ты никогда не хотела стать актрисой?"
    img 12390
    m "Нет."
    img 12391
    citizen13 "Ну и зря. Уверен, у тебя бы получилось!"
    citizen13 "Мне бы очень хотелось увидеть тебя в кино."
    # сиськи
    img 12392
    with diss
    w
    img 12393
    with diss
    w
    img 12394
    with fade
    citizen13 "Подожди ка..."
    # Достает телефон и фоткает
    img 12395
    with diss
    w
    music stop
    img 12396
    with Dissolve(0.2)
    w
    call photoshop_flash() from _call_photoshop_flash_148
    w
    music Power_Bots_Loop
    img 12397
    with fade
    m "Эй! Что ты сделал?"
    img 12398
    citizen13 "Подруга, ты злишься? Я тебя сфотографировал!"
    citizen13 "Хочу показать твое фото одному моему знакомому, он снимает фильмы!"
    img 12399
    with diss
    m "Удали это фото немедленно!!!"
    # какая то поза моники или просто берет за шквар нигера...
    img 12401
    with diss
    w
    img 12402
    with diss
    w
    music Groove2_85
    img 12400
    with fade
    citizen13 "Ууу! Ладно, подруга, не злись!"
    citizen13 "Хорошо, хорошо, удаляю..."
    # удаляет
    img 12403
    w
    sound click1
    img 12404
    with diss
    w
    img 12405
    with fade
    citizen13 "Эх, подруга, зря ты так, могла бы стать знаменитой..."
    img 12406
    with diss
    mt "Я и так знаменита, только пока у меня не самая удачная полоса в жизни..."
    m "Ну ладно, хватит!"
    img 12407
    citizen13 "Ну хорошо, но ты должна обещать, что я увижу их снова!"
    img 12408
    with fade
    mt "Посмотрим..."
    return True

# первый раз танцы с сиськами
label cit13_naked_boobs_dance_1st:
    music Groove2_85
    img 13692
    with fade
    citizen13 "Подруга, я часто вспоминаю тебя. Точнее твою красивую грудь и твои движения на пилоне."
    citizen13 "Может быть покажешь мне эти две вещи одновременно?"
    img 13316
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    img 13693
    with diss
    m "Что я получу за это?"
    img 13694
    citizen13 "Вот ты какая... Я думал, что ты сделаешь это ради нашей дружбы..."
    img 13695
    m "Нет, мне нужны деньги."
    img 13696
    with diss
    mt "Какой еще дружбы? Я вообще тебя не знаю..."
    mt "У такой леди как Я не может быть друзей в этих грязных трущобах!"
    mt "Это все какое-то недоразумение... Временное..."
    img 13697
    citizen13 "Хорошо, подруга, я дам тебе немного денег."
    img 13698
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13699
            with fade
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13700
    with fade
    m "Хорошо. Только отвернись!"
    img 13701
    citizen13 "А ты смешная! Зачем? Я же уже видел твою грудь."
    img 13702
    m "Я не привыкла переодеваться, когда на меня смотрит мужчина."
    img 13703
    citizen13 "Но я ведь не мужчина, а твой друг, а ты моя подруга."
    img 13704
    m "Это не важно, отвернись!"
    img 13705
    citizen13 "Скучная ты, ну ладно."
    sound snd_fabric1
    img 12334
    with diss
    w
    # отворачивается
    # поворачиваются, моника стоит с голыми сиськами
    img 13706
    with fadelong
    citizen13 "Привет, близняшки! Готовы потанцевать?"
    img 13707
    with diss
    mt "Господи, лучше бы ты молчал..."
    # движение на пилоне
    music RocknRoll_loop
    img 13708
    with fadelong
    w
    img 13709
    with diss
    citizen13 "Подруга, я же уже говорил, что у тебя талант?"
    # движение на пилоне еще
    img 13710
    with diss
    w
    img 13711
    with diss
    citizen13 "Вот это пластика!"
    # движение на пилоне еще
    img 13712
    with diss
    w
    img 13713
    with diss
    citizen13 "Ты же научишь меня также? По дружбе..."
    # моника слезает с шеста
    music Groove2_85
    img 13714
    with fadelong
    citizen13 "Дак что, научишь?"
    img 13422
    mt "Да ни за что на свете."
    img 13715
    with diss
    m "Нет!"
    img 13716
    with fade
    citizen13 "Жаль, но, возможно скоро ты изменишь свое мнение. Мы бы классно провели время."
    citizen13 "Чуть не забыл... Вот твои деньги."
    $ nakedBoobsDanceFirstly_Cit13 = True
    return True

#  танцы с сиськами 1 вариант
label cit13_naked_boobs_dance_variant1:
    music Groove2_85
    img 13717
    with fade
    citizen13 "Потанцуй еще! И грудь оголи, пожалуйста!"
    citizen13 "Мы же подруги!"
    img 13698
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13699
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13700
    with fade
    m "Хорошо. Только отвернись!"
    img 13701
    citizen13 "Ну, подруга, это уже не смешно..."
    img 13702
    m "Отвернись, иначе ничего не будет."
    img 13703
    citizen13 "Ладно, подруга, как скажешь."
    sound snd_fabric1
    img 12334
    with diss
    w
    # отворачивается
    # поворачиваются, моника стоит с голыми сиськами
    img 13718
    with fadelong
    citizen13 "Начинаем!"
    # движение на пилоне
    music RocknRoll_loop
    img 13719
    with fadelong
    w
    img 13720
    with diss
    citizen13 "Отлично!"
    # движение на пилоне еще
    img 13721
    with diss
    w
    img 13722
    with diss
    citizen13 "Подруга, ты прекрасна!"
    # моника крутится на пилони и у нее растегивается и падает туфля. ситизен поднимает
    img 13723
    with diss
    w
    sound Jump1
    img 13724
    with diss
    w
    sound Jump2
    img 13725
    with diss
    w
    img 13726
    with diss
    citizen13 "Ух ты! Что тут у нас?"
    # моника слезает с шеста
    music Groove2_85
    img 13727
    with fadelong
    m "Отдай мою туфлю!"
    img 13728
    citizen13 "Подруга, как не вежливо! Это Луи Витон? Очень похоже..."
    img 13729
    mt "Господи, откуда ты это услышал проживая в этой дыре..."
    img 13730
    with diss
    m "Нет."
    img 13731
    citizen13 "Очень похоже..."
    img 13732
    m "Наверное, а теперь отдай мне туфлю."
    img 13733
    citizen13 "Погоди, подруга. Мне кажется, только я думаю о нашей дружбе и тебе на нее наплевать."
    img 13734
    mt "У нас нет никакой дружбы и мне на тебя плевать..."
    img 13735
    citizen13 "Знаешь что... Обними меня, как свою лучшую подругу и я отдам тебе туфлю, но если ты откажешься, я выкину ее в помойку."
    img 13729
    with fade
    mt "Было бы очень не приятно потерять туфлю... В одной я далеко не уйду... Что делать?"
    img 13736
    with diss
    menu:
        "Хорошо.":
            mt "Возможно, стоит сделать вид что я обнимаюсь с ним."
            mt "Мне нужна моя туфля назад. Я не смогу его догнать в одной туфле..."
            img 13737
            with fade
            m "Хорошо, давай обнимемся."
            img 13738
            citizen13 "Ура! Я знал, что ты не откажешь!"
            # моника обнимает ситизена, а он ее ситизен лапает монику за зад
            music Loved_Up
            img 13744
            with fadelong
            w
            sound Jump2
            img 13745
            with diss
            w
            img 13746
            with hpunch
            mt "Какого черта? Он лапает мой зад?!"
            img 13743
            with fade
            citizen13 "Вот это я понимаю дружба! Вот, возьми свою туфлю."
            $ citizen13BoobsNakedDancedEvent1Count += 1
            pass
        "Подруги так не поступают!":
            music Power_Bots_Loop
            img 13739
            with fade
            m "Подруги так не поступают!"
            img 13740
            citizen13 "Хм... Да, возможно ты права."
            img 13741
            m "Дружба должна быть на доверии, а после такого я не уверена, что могу тебе доверять."
            m "А теперь, если мы и правда подруги, отдай мне туфлю!"
            music Groove2_85
            img 13742
            with fade
            citizen13 "Конечно мы подруги! Вот, возьми."
            pass
    img 13823
    with diss
    citizen13 "Кстати, чуть не забыл: вот твои деньги."
    return True

#  танцы с сиськами 2 вариант
label cit13_naked_boobs_dance_variant2:
    music Groove2_85
    img 13747
    with fade
    citizen13 "Потанцуй еще! И грудь оголи пожалуйста!"
    citizen13 "Мы же подруги!"
    img 13748
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13749
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13750
    with fade
    m "Хорошо. Только отвернись!"
    img 13751
    citizen13 "Ну, подруга, ну хватит уже..."
    img 13702
    m "Отвернись, иначе ничего не будет."
    img 13703
    citizen13 "Какая же ты скучная..."
    sound snd_fabric1
    img 12334
    with diss
    w
    # отворачивается
    # поворачиваются, моника стоит с голыми сиськами
    img 13752
    with fadelong
    citizen13 "Твоя грудь стала больше? Или мне показалось?"
    citizen13 "Ладно, не важно, танцуй!"
    # движение на пилоне
    music RocknRoll_loop
    img 13753
    with fadelong
    w
    img 13754
    with diss
    citizen13 "Йуху! Какие обороты!"
    # движение на пилоне еще
    img 13755
    with diss
    w
    img 13756
    with diss
    citizen13 "Ты  даже так умеешь?!"
    # моника крутится на пилони
    img 13757
    with diss
    w
    img 13758
    with diss
    citizen13 "Круто! Ой, что это?!"
    # ситизен снимает штаны. у него очень маленький член и он стоит.
    # моника слезает с шеста
    sound Jump1
    img 13759
    with diss
    w
    sound Jump2
    img 13760
    with vpunch
    w
    music Groove2_85
    img 13761
    with fade
    w
    img 13762
    with diss
    m "Какого хрена ты делаешь?"
    img 13763
    with diss
    citizen13 "Подруга, это чудо! Видимо ты понравилась моему дружочку! Это так неожиданно!"
    img 13764
    with fade
    m "Оденься!"
    img 13765
    mt "Его член просто крохотный, Фи!"
    img 13766
    with fade
    citizen13 "Обязательно расскажу об этом всем!"
    # ситизен одевает штаны.
    img 13767
    with diss
    citizen13 "Кстати, подруга, вот тебе лишнй доллар! Уверен, ты рада!"
    $ earnedMoney += 1
    return True

label cit13_groping_1st:
    img 13692
    citizen13 "Как же мне нравится наша дружба!"
    citizen13 "У меня никогда не было такой хорошей подруги, как ты!"
    citizen13 "Обнимемся! В честь нашей дружбы!"
    img 13265
    mt "Это ничтожество хочет обнять меня, Монику Бакфетт! Но, он заплатит..."
    img 12324
    menu:
        "Почему я должна на это согласиться?":
            pass
        "Да ни за что!":
            img 13695
            m "Да ни за что!"
            return False
    img 13700
    m "Почему я должна на это согласиться?"
    img 13701
    citizen13 "Потому, что подруги иногда обнимаются, а ты моя подруга."
    img 14658
    mt "Он не отличается умом. Думаю, его  можно обмануть..."
    img 1226
    m "Подруги ведь также помогают друг другу. Так?"
    img 13751
    citizen13 "Ну, да, наверное..."
    img 14659
    m "Понимаешь, у меня сейчас не самое удачное материальное положение..."
    m "Мне бы пригодились...20 долларов."
    img 14660
    citizen13 "Подруга...У меня у самого сейчас не так много денег. У меня только 5."
    img 13265
    mt "Нищеброд!"
    img 13704
    m "Очень жаль..."
    img 13705
    citizen13 "Подруга, я с удовольствием дам тебе эти 5 долларов! Давай обнимемся!"
    img 14661
    menu:
        "Хорошо.":
            pass
        "Не сегодня.":
            img 12326
            m "Не сегодня."
            img 14662
            mt "Я не хочу, чтобы меня обнимало это ничтожество."
            return False
    img 14663
    mt "5 долларов - очень мало, но мне нужны деньги..."
    img 14664
    m "Хорошо."
    img 14665
    citizen13 "Ура!"
    # подходит, обнимает, трогает за зад. моника его не обнимает
    img 14666
    w
    img 14667
    w
    img 14668
    w
    img 14671
    citizen13 "Какая ты хорошая подруга!"
    img 14670
    mt "Какой же ты глупый, если считаешь, что я твоя подруга..."
    img 14669
    citizen13 "А почему ты меня не обнимаешь? Ты не ценишь нашу дружбу?"
    img 14672
    mt "Черт, похоже, придется это сделать, иначе он не заплатит."
    mt "Просто сомкну руки сзади..."
    #смыкает руки сзади
    img 14673
    w
    img 14674
    citizen13 "Как хорошо!"
    #хватает за зад, лапает
    img 14675
    w
    img 14689
    w
    img 14690
    w
    img 14676
    citizen13 "Какая ты мягкая!"
    img 14677
    mt "Он что, лапает мою попу?"
    mt "Что за мерзость?!"
    img 14678
    menu:
        "Терпеть.":
            img 14679
            mt "Если бы не эти 5 долларов, я бы тебя..."
            pass
        "Какого черта?.":
            # отталкивает
            img 14680
            w
            img 14681
            m "Какого черта? Ты лапал мою попу?!"
            img 1468
            citizen13 "Это дружеские объятия!"
            img 1468
            m "Не нужны мне такие объятия!"
            img 14684
            citizen13 "Плохая подруга! Значит и деньги не нужны!"
            return False
    img 14685
    citizen13 "Теперь я вижу, что ты ценишь нашу дружбу!"
    citizen13 "Держи!" # дает деньги
    img 14686
    mt "Никакой между нами дружбы не существует!"
    return True

label cit13_grooping_regular:
    img 13747
    citizen13 "Говорят, что если люди будут обниматься, они будут жить дольше!"
    img 14658
    mt "Возможно, но уж точно не с такими как ты."
    img 12376
    citizen13 "Давай обнимемся!"
    img 12351
    m "Сколько ты заплатишь?"
    img 14660
    citizen13 "Не заплачу, а как ты там говорила?"
    citizen13 "Помогу материально... Кажется так."
    citizen13 "Но только ради нашей дружбы!"
    img 13509
    mt "Которой не существует..."
    img 13697
    citizen13 "Я дам тебе 5 долларов."
    img 12328
    menu:
        "Хорошо.":
            pass
        "Не сегодня.":
            img 12324
            m "Не сегодня."
            img 14658
            mt "Я не хочу, чтобы меня обнимало это ничтожество."
            return False
    img 13701
    citizen13 "Но у меня есть условие."
    citizen13 "Я немного сомневаюсь в том, что наша дружба взаимна..."
    citizen13 "Я хочу, чтобы наши объятия были крепкими!"
    citizen13 "Как демонстрация дружбы!"
    img 14663
    mt "Он хочет, чтобы я обняла его крепко?! Он-никто и не достоин этого."
    mt "Но мне нужны эти 5 долларов!"
    img 14661
    menu:
        "Хорошо.":
            pass
        "Я на такое не согласна.":
            img 13698
            m "Я на такое не согласна."
            img 12354
            citizen13 "Я так и знал, что наша дружба не крепкая..."
            return False
    img 13749
    m "Хорошо."
    img 13751
    citizen13 "Я знал!"
    # подходит и сразу обнимает за зад
    img 14687
    w
    img 14668
    w
    img 14688
    citizen13 "Подруга, теперь ты! И обними меня крепко!"
    # смыкает руки и смыкает сильнее в отличие от first
    img 14695
    mt "Это ужасно..."
    # лапает попу
    img 14694
    w
    img 14691
    w
    img 14692
    w
    img 14693
    w
    img 14696
    citizen13 "Как приятно!"
    citizen13 "У тебя такая упругая попа!"
    citizen13 "Хотел бы я себе такую же!"
    img 14697
    mt "Он снова меня лапает..."
    img 14698
    menu:
        "Терпеть.":
            img 14699
            mt "Если бы не эти 5 долларов, я бы тебя..."
            pass
        "Какого черта?.":
            # отталкивает
            img 14680
            w
            img 14681
            m "Какого черта? Ты снова меня лапаешь?!"
            img 14684
            citizen13 "Я же говорил, это ради дружбы!"
            img 14683
            m "Мне это надоело!"
            img 14700
            citizen13 "Плохая подруга! Значит и деньги не нужны!"
            return False
    img 14702
    m "Ну все, достаточно."
    img 14703
    citizen13 "Ты куда-то спешишь?"
    img 14701
    mt "Я спешу побыстрее вернуть свою прежнюю жизнь, а также спешу не видеть таких как ты."
    img 14704
    m "Нет, просто мы уже достаточно обнимались."
    img 14685
    citizen13 "Ну ладно, в следующий раз продолжим."
    citizen13 "Вот твои 5 долларов."
    img 14686
    mt "Надеюсь, он будет не скоро..."
    return True

label cit13_lipstick_event:
    img 13703
    citizen13 "Подруга, выручай!"
    citizen13 "Мне нужна твоя помощь!"
    img 13696
    mt "Что опять на уме у этого извращенца?"
    img 13697
    citizen13 "По твоей одежде сразу видно, что ты разбираешься в моде!"
    img 14658
    mt "Это одежда шлюхи, она не может быть модной, но ты прав!"
    img 13751
    citizen13 "И знаешь как делать очень красивый мейкап!"
    citizen13 "Скажи, что знаешь!"
    img 14705
    mt "Ну конечно знаю"
    img 14659
    m "Знаю."
    img 14706
    citizen13 "Я тут недавно прикупил одну важную вещь."
    # показывает помаду. цвет должен быть яркий. скорее всего ярко красный лучше всего подойдет
    img 14708
    w
    img 14707
    citizen13 "Но я не уверен, что знаю как ей правильно пользоваться."
    citizen13 "Ты должна мне помочь! Научи меня!"
    citizen13 "Покрась себе губы, как надо!"
    img 14709
    mt "Чтобы я, Моника Бакфетт, красила свои губы этой ужасной помадой?!"
    mt "Да она стоит не больше доллара! Она очень не качественная."
    img 14710
    citizen13 "Да, забыл сказать! Я помню, что у тебя проблемы с деньгами..."
    citizen13 "За этот урок я дам тебе 10 долларов!"
    img 14711
    mt "Накрасить себе губы этой ужасной помадой и получить 10 долларов..."
    img 14712
    menu:
        "Хорошо.":
            pass
        "Я не собираюсь красить губы этой ужасной помадой.":
            img 13698
            m "Я не собираюсь красить губы этой ужасной помадой."
            img 14660
            citizen13 "Ну как же, подруга?! Она такая красивая..."
            img 13699
            m "Это помада для двадцатидолларовой шлюхи, а не для меня!"
            img 13694
            citizen13 "?!"
            citizen13 "Подруга, но ты ведь..."
            img 14713
            m "Я не шлюха!"
            img 13696
            mt "Хоть и одета как шлюха, но это все временно. Скоро я сожгу этот наряд."
            img 14714
            citizen13 "Странная ты. Ладно, как хочешь."
            return False
    img 14715
    mt "Думаю, ничего страшного не произойдет. Я только накрашу себе губы, а потом быстро все сотру."
    mt "А это ничтожество даст мне 10 долларов."
    img 14716
    m "Хорошо."
    img 14717
    citizen13 "Я знал! Я знал, что ты мне поможешь!"
    citizen13 "Вот, держи." # дает помаду
    # моника красит губы
    img 14718
    m "Нужно сделать так..."
    m "А потом вот так."
    m "И все готово!"
    img 14719
    citizen13 "Вау! Так просто! Дай-ка посмотреть!" # смотрит супер близко на монику
    citizen13 "Отлично! А теперь поцелуй меня!"
    citizen13 "Хочу след от губ на моей щеке."
    citizen13 "И я дам тебе 10 долларов."
    citizen13 "Мы же подруги..."
    img 14720
    mt "Что?! Поцеловать этого трущобного жителя?! Пусть даже в щеку..."
    mt "Скоро это все закончится и я не появлюсь в этих трущебах никогда..."
    mt "Что же делать? Он готов дать мне 10 долларов, а деньги мне очень нужны."
    mt "Он не отличается умом... Может, я смогу его обмануть?"
    img 14721
    menu:
        "Хорошо, я тебя поцелую.":
            img 14722
            mt "Сделаю это очень быстро..."
            img 14723
            m "Хорошо, я тебя поцелую."
            img 14724
            citizen13 "Здорово. Я готов!"
            # подходит, целует
            img 14725
            w
            img 14726
            citizen13 "О да! Как приятно! Это гораздо лучше, чем поцелуй Александра!"
            citizen13 "Точнее Александры! Да! Моей девушки Александры!"
            img 14727
            mt "Да все уже давно с тобой ясно..."
            img 14728
            m "Я поняла..."
            pass
        "Попытаться обмануть.":
            img 14729
            m "Ты знашь, я ведь уже научила тебя красить губы?"
            img 14730
            citizen13 "Да! И я за это благодарен!"
            img 14731
            m "Может быть, ты сможешь накрасить себе губы..."
            m "Поцеловать себя в руку, а затем прислонить ее к щеке!"
            m "Ведь если я тебя поцелую, могут передаться разные бактерии..."
            img 14732
            citizen13 "Ты думаешь?"
            img 14733
            m "Да, я уверена."
            img 14734
            citizen13 "Да, я не хочу заболеть...Спасибо, подруга!"
            img 14727
            mt "Ну ты и идиот..."
            pass
    img 14665
    citizen13 "Спасибо тебе, подруга!"
    citizen13 "Ты мне очень помогла!"
    citizen13 "Теперь я знаю, к кому обращаться в случае подобных сложностей!"
    citizen13 "Спасибо за урок." # дает деньги
    return True
