default citizen15BoobsNakesShowedLastDay = 0
default citizen15BoobsNakedDancedLastDay = 0
default citizen15BoobsNakesShowedCount = -1
default citizen15BoobsNakedDancedCount = -1
default citizen15BoobsNakesShowedCount1 = 0
default citizen15BoobsNakedDancedCount1 = 0
default pylonpart2startsCompleted = False
default pylonpart3startsCompleted = False
default pylonpart4startsCompleted = False
default citizen15DanceCloth = 0

label citizen15_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_15_1
    if citizen15_offered_last_day == day:
        imgr Dial_Citizen_15_4
        citizen15 "Я важная персона! Ты отвлекаешь меня!"
        return
    citizen15 "Йо! Бэби! Что ты хочешь?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen15_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen15_refuse_probability) > 0:
                imgr Dial_Citizen_15_2
                citizen15 "Флаер?..."
                call reduce_flyers() from _call_reduce_flyers_10
                "Давай!"
                imgr Dial_Citizen_15_3
                citizen15 "А что дальше?"
                m "В смысле?"
                citizen15 "Я важная персона! Все девочки тащатся от меня!"
                "Продолжай подкатывать ко мне! Мне нравится!"
                menu:
                    "Я не собираюсь к тебе подкатывать!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Я не собираюсь к тебе подкатывать!"
                    "Я не подкатываю, но все-же...":
                        m "Ну я так то не совсем подкатываю..."
                        citizen15 "Да, ты знаешь толк в парнях, но для начала хотел бы посмотреть на тебя поближе."
                        m "А?"
                        citizen15 "Давай сходим за угол, там нам никто не помешает.. Глядишь и заработаешь что-нибудь."
                        m "Да кем ты себя возомнил?!"
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."

            else:
                imgr Dial_Citizen_15_4
                citizen15 "Я важная персона! У меня нет времени на флаеры!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

label citizen15_dialogue_after_showing_naked_boobs: #Моника думает после показа голых сикек за 50 баксов
    mt "ыыы"
    $ add_money(-50)
    return


label citizen15_dialogue_pilon:
    if ep214_quests_citizens_stage2 == True:
        jump ep215_slums1_dialogue_citizen15

    imgl Dial_begin35_17
    imgr Dial_Citizen_15_1
    m "Привет! Кажется, ты говорил, что я могу заработать денег..."
    imgr Dial_Citizen_15_3
    citizen15 "Да, и сейчас говорю. Только учти: у меня от таких как ты отбоя нет. Ты должна мне показать что-то особенное."
    mt "Самодовольный козел...Да кем он себя возомнил? Черт, мне нужны деньги."
    m "Куда ты хотел пойти?"
    citizen15 "Обычно девочки сами придумывают куда меня вести."
    "Не забывай, у меня нет отбоя от таких как ты."
    mt "!!!"
    m "Знаю"
    citizen15 "Ты же наверняка видела подворотню с пилоном? Вот туда и пойдем."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_215
    call pylonController(2, 1) from _call_pylonController_175
    with fadelong
    citizen15 "Ну что, начинай, только не разочаруй меня."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False
    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen15_dialogue_pilon_loop15:
    call pylonController(1, 1) from _call_pylonController_176
    if (pylonpart4startsCompleted == True and citizen15BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen15BoobsNakesShowedCount>=0:
        $ questHelp("work_slums_45", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_177
            citizen15 "Для начала сиськи, показывай!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_178
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15

            call pylonController(3, 3) from _call_pylonController_179
            with fade
            m "Я не собираюсь раздеваться, только так."
            $ questHelp("work_slums_14", True)
            $ questHelp("work_slums_23", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")

            call showRandomImages(boobsImages, 4) from _call_showRandomImages_45
            call pylonController(5, 3) from _call_pylonController_180
            citizen15 "И это все?"
            call pylonController(2, 3) from _call_pylonController_181
            # img показывает сиськи
            citizen15 "Мда, ну и так сойдет..."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen15_dialogue_pilon_loop15


        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_182
            citizen15 "А теперь повернсь и покажи свой зад!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_183
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5) from _call_pylonController_184
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_46
            call pylonController(4, 5) from _call_pylonController_185
            # img показывает зад
            citizen15 "Зад, 10 долларовой шлюхи, но еще рабочий."
            call pylonController(4, 1) from _call_pylonController_186
            mt "Что за козел. Врезать может ему?"
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen15_dialogue_pilon_loop15
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_187
            citizen15 "Покрутись немного на шесте, который сзади тебя."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_188
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_189
            with fade
            m "Хорошо, только не долго."
            m "Только потому, что ты заплатишь."
            $ citizen15DanceCloth += 1
            if citizen15DanceCloth >= 3:
                $ questHelp("work_slums_23", True)

            call showRandomImages(pylonClothDanceImages2, 4) from _call_showRandomImages_47
#            call pylonController(4, 5)
            citizen15 "Мда, тебе далеко до совершенства..."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_190
            with fade
            mt "Ну и урод..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen15_dialogue_pilon_loop15
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen15BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen15BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen15BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen15BoobsNakesShowedCount == -1:
                call cit15_naked_boobs_1st() from _call_cit15_naked_boobs_1st
                if _return != False:
                    $ citizen15BoobsNakesShowedCount += 1
            else:
                if citizen15BoobsNakesShowedCount%2 == 0:
                    call cit15_naked_boobs_variant1() from _call_cit15_naked_boobs_variant1
                if citizen15BoobsNakesShowedCount%2 == 1:
                    call cit15_naked_boobs_variant2() from _call_cit15_naked_boobs_variant2
                $ citizen15BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen15BoobsNakesShowedCount1 = citizen15BoobsNakesShowedCount + 1
                if citizen15BoobsNakesShowedCount1 >= 3:
                    $ questHelp("work_slums_35", True)

                $ citizen15BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen15_dialogue_pilon_loop15


        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen15BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen15BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen15BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen15BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen15BoobsNakedDancedCount == -1:
                call cit15_naked_boobs_dance_1st() from _call_cit15_naked_boobs_dance_1st
                if _return != False:
                    $ citizen15BoobsNakedDancedCount += 1
            else:
                if citizen15BoobsNakedDancedCount%2 == 0:
                    call cit15_naked_boobs_dance_variant1() from _call_cit15_naked_boobs_dance_variant1
                if citizen15BoobsNakedDancedCount%2 == 1:
                    call cit15_naked_boobs_dance_variant2() from _call_cit15_naked_boobs_dance_variant2
                    if _return == 1:
                        $ showedNakedBoobsDance = True
                        $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
                        $ restore_music()
                        $ autorun_to_object("citizen15_autorun_comment1", scene="hostel_edge_1_a")
                        return False # Заканчиваем евент
                $ citizen15BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen15BoobsNakedDancedCount1 = citizen15BoobsNakedDancedCount + 1
                if citizen15BoobsNakedDancedCount1 >= 3:
                    $ questHelp("work_slums_45", True)
#                    $ questHelp("work_slums_50", skipIfExists=True)
                $ citizen15BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen15_dialogue_pilon_loop15

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
                call pylonController(2, 1) from _call_pylonController_191
                citizen15 "Красивая шлюшка. Уверен, ты можешь больше, а пока так..."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_192
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_193
            citizen15 "Сходи поищи себе кого-нибудь еще."
            return False
    return

# первый раз
label cit15_naked_boobs_1st:
    music Groove2_85
    img 12409
    with fade
    citizen15 "Знаешь, обычно при виде меня девочки сами снимают кофточки!"
    citizen15 "Тебе нужно особое приглашение?"
    img 12410
    m "Я не собираюсь ее снимать."
    img 12411
    citizen15 "Хорошие девочки обычно получают за это деньги. Только не говори, что деньги тебе не нужны."
    img 12412
    mt "Самодовольный козел. Но он прав, деньги мне нужны."
    img 12413
    citizen15 "Ну дак что, голые сиськи в обмен на деньги?"
    img 12414
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 12415
            m "Хватит и того, что ты уже видел!"
            return False
    img 12416
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12417
    citizen15 "А ты че, стесняешься? Не переживай, можешь начинать..."
    img 12418
    m "Отвернись! Иначе ничего не покажу!"
    img 12419
    citizen15 "А ты серьезная, ладно, отвернусь."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 12420
    with fadelong
    w
    music Loved_Up
    img 12421
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    img 12422
    citizen15 "Вот так новость! Ну ничего, скоро сама попросишь меня их поторгать!"
    img 12423
    mt "Никогда!"
    # сиськи
    img 12424
    w
    img 12425
    w
    music Groove2_85
    img 12426
    with fade
    citizen15 "Ну скажу честно, так себе!"
    img 12427
    with diss
    mt "Что?!?!"
    # сиськи еще
    img 12428
    w
    img 12429
    w
    img 12430
    citizen15 "Видал я сиськи и получше..."
    # моника продолжает показывать
    img 12431
    with diss
    w
    img 12432
    with diss
    w
    img 12433
    with fade
    citizen15 "Но вообще сойдет, нормально!"
    citizen15 "На 3 балла из 10!"
    img 12434
    with diss
    m "Почему ты мне такое говоришь?"
    img 12435
    citizen15 "А что не так? На правду не обижаются..."
    img 12436
    m "Ну ладно, хватит!"
    img 12437
    citizen15 "Странная ты... Обычно девочки просят, чтобы я смотрел на них как можно дольше!"
    img 12438
    with fade
    mt "Обещаю, когда нибудь я тебя ударю."
    $ nakedBoobsFirstly_Cit15 = True
    return True

# вариант 1
label cit15_naked_boobs_variant1:
    music Groove2_85
    img 12439
    with fade
    citizen15 "Ну что, показывай свои сиськи, погляжу как они там!"
    img 12440
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12441
            m "Хватит и того, что ты уже видел!"
            return False
    img 12442
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12443
    citizen15 "Ты снова об этом...Ладно."
    # отворачивается, моника переодевается
    sound snd_fabric1
    img 12444
    with diss
    w
    img 12445
    with fadelong
    w
    music Loved_Up
    img 12446
    with diss
    w
    img 12447
    with diss
    m "Можешь поворачиваться!"
    img 12448
    with diss
    citizen15 "Как скажешь, детка."
    # сиськи
    img 12449
    with diss
    w
    img 12450
    with diss
    w
    img 12451
    with fade
    citizen15 "Оу, что за взгляд!"
    img 12452
    with diss
    mt "Да я убить тебя готова! Если бы не эти чертовы деньги..."
    img 12453
    with diss
    citizen15 "Я знаю этот взгляд... Ты меня хочешь!"
    img 12454
    m "Размечтался..."
    # сиськи
    img 12455
    with diss
    w
    img 12456
    with diss
    w
    img 12457
    citizen15 "Ха! Так говорят все девочки, но я то знаю правду."
    citizen15 "Если ты меня хочешь, скажи. Не нужно скрывать."
    music Groove2_85
    img 12458
    with fade
    m "Я тебя не хочу."
    # сиськи
    img 12459
    with diss
    w
    img 12460
    with diss
    w
    img 12461
    citizen15 "Я знаю, что ты врешь! Но даже если бы ты это сказала, я бы подумал, стоит ли тебя трахать."
    music Power_Bots_Loop
    img 12462
    with diss
    mt "Что? Да как ты смеешь такое говорить!? Я Моника Бакфет!! А ты ничтожество, проживающее в помойке!!"
    music Groove2_85
    img 12463
    with fade
    citizen15 "Ну вот, снова этот взгляд!"
    # сиськи
    img 12464
    with diss
    w
    img 12465
    with diss
    w
    img 12466
    with fade
    m "Ну ладно, хватит!"
    img 12467
    citizen15 "Что, не можешь с собой справиться? Ха-ха... Ну не знаю, может когда нибудь я тебя и трахну, если хорошо попросишь."
    img 12468
    mt "Да ни за что на свете!"
    return True

# вариант 2
label cit15_naked_boobs_variant2:
    music Groove2_85
    img 12469
    with fade
    citizen15 "Время голых сисек! Давай, расчехляй!"
    music Power_Bots_Loop
    img 12470
    mt "Я вырву твой вонючий язык..."
    img 12471
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 12472
            with fade
            m "Хватит и того, что ты уже видел!"
            return False
    music Groove2_85
    img 12473
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12474
    citizen15 "Конечно, детка!"
    # отворачивается, моника переодевается ситизен резко поворачивается и ее пугает
    sound snd_fabric1
    img 12475
    with fadelong
    w
    sound Jump1
    img 12476
    with hpunch
    w
    img 12477
    with diss
    w
    sound Jump2
    img 12478
    with diss
    citizen15 "Бу!!!"
    img 12479
    with diss
    m "Ой! Какого?"
    img 12480
    with diss
    citizen15 "Ха-ха-ха. Девочки всегда так смешно пугаются."
    citizen15 "И после такого они уже в моей власти!"
    img 12481
    with fade
    m "Что? О чем вообще ты?"
    img 12482
    citizen15 "Ну как же, разве ты не чувствуешь мое превосходство?"
    img 12483
    m "..."
    img 12484
    citizen15 "Разве не готова мне отдаться прямо здесь?"
    img 12485
    with fade
    m "Знаешь что... Я не покажу тебе свою грудь..."
    img 12486
    with diss
    citizen15 "Корчишь недотрогу? Такие девочки мне нравятся..."
    return False
#

# первый раз танцы с сиськами
label cit15_naked_boobs_dance_1st:
    music Groove2_85
    img 13768
    with fade
    citizen15 "Бэйба! Я удивлен, что ты еще не крутишься голая на этом пилоне!"
    img 13769
    m "Разве я должна?"
    img 13770
    citizen15 "Конечно! Все девочки так делают при виде меня!"
    img 13771
    m "Я не из таких."
    img 13772
    citizen15 "Ты что, лезбиянка?"
    img 13773
    m "Нет!"
    citizen15 "Отлично! Значит так: показывай свои сисечки и пулей на пилон!"
    citizen15 "Я за это плачу!"
    img 13774
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            music Power_Bots_Loop
            img 13775
            with fade
            m "Хватит с тебя того, что ты уже видел!"
            img 13776
            citizen15 "Я знаю, ты передумаешь!"
            return False
    img 13777
    with fade
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет..."
    img 13778
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13779
    citizen15 "Ну ты как обычно, ладно!"
    sound snd_fabric1
    img 12444
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13780
    with fadelong
    citizen15 "Давай, залазь!"
    img 13781
    with diss
    mt "Когда-нибудь моему терпению придет конец..."
    # движение на пилоне
    music Molten_Alloy
    img 13782
    with fadelong
    w
    img 13783
    with diss
    citizen15 "Давай, бейби, покажи на что ты способна!"
    # движение на пилоне еще
    img 13784
    with diss
    w
    img 13785
    with diss
    citizen15 "Вот так вот! Уверен, ты уже мокрая!"
    img 13786
    with diss
    mt "И не надейся..."
    # моника слезает с шеста
    music Groove2_85
    img 13787
    with fadelong
    citizen15 "И это все? Не густо..."
    citizen15 "Ааа... Я тебя понял! Ты меня дразнишь... Хорошо..."
    img 13655
    mt "И не надейся, ничтожество."
    img 13788
    with diss
    citizen15 "Ладно, держи, заработала."
    $ nakedBoobsDanceFirstly_Cit15 = True
    return True

# танцы с сиськами вариант 1
label cit15_naked_boobs_dance_variant1:
    music Groove2_85
    img 13789
    with fade
    citizen15 "Ну что, ты готова меня развлекать?"
    citizen15 "Зачем я спрашиваю? Я же знаю, что да!"
    citizen15 "Раздевайся и на пилон!"
    img 13790
    m "Нет."
    img 13774
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            music Power_Bots_Loop
            img 13775
            with fade
            m "Хватит с тебя того, что ты уже видел!"
            img 13776
            citizen15 "Я знаю, ты передумаешь!"
            return False
    img 13778
    with fade
    m "Хорошо. Только отвернись!"
    citizen15 "Что с тобой не так? Все девочки хотят, чтобы я на них смотрел!"
    # отворачиваются
    img 13779
    citizen15 "Ладно, сыграем снова в твою игру!"
    sound snd_fabric1
    img 12444
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13780
    with fadelong
    citizen15 "Начинай уже!"
    img 13781
    with diss
    mt "Когда-нибудь моему терпению придет конец..."
    # движение на пилоне
    music Molten_Alloy
    img 13792
    with fadelong
    w
    img 13791
    with diss
    citizen15 "О да! Девочка вошла во вкус!"
    # движение на пилоне еще
    img 13793
    with diss
    w
    img 13794
    with diss
    citizen15 "Йо! Вот это ты раскрутилась!"
    citizen15 "Уверен, ты не против также покрутиться на моем толстом члене!"
    img 13786
    with diss
    mt "Скорее, я не против его оторвать..."
    # моника слезает с шеста
    music Groove2_85
    img 13787
    with fadelong
    citizen15 "И это все? Не густо..."
    citizen15 "Ааа... Ты продолжаешь меня дразнить... Хорошо..."
    img 13655
    mt "И не надейся, ничтожество."
    img 13788
    citizen15 "Вот твои деньги, девочка. И я тут подумал: если ты попросишь, чтобы я тебя трахнул, скорее всего, я соглашусь, но я не уверен."
    # кадр как ситизен держится за член, который пока в штанах и моника видит какой он большой
    # короче у этого негра огромный хер. Моника это видит и охеревает
    sound Jump1
    img 13795
    with diss
    w
    img 13796
    with diss
    mt "Черт! У него там что, бейсбольная бита?"
    img 13797
    with fade
    citizen15 "Что, нравится мой инструмент? Я знаю, он всем нравится!"
    return True

# танцы с сиськами вариант 2
label cit15_naked_boobs_dance_variant2:
    music Groove2_85
    img 13768
    with fade
    citizen15 "Давай повторим наши танцы! И не забудь про сиськи!"
    citizen15 "И не вздумая отказываться, я ведь знаю, что ты от меня без ума."
    img 13798
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            music Power_Bots_Loop
            img 13775
            with fade
            m "Хватит с тебя того, что ты уже видел!"
            img 13776
            citizen15 "Я знаю, ты передумаешь!"
            return False
    img 13778
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13779
    citizen15 "Ладно, сыграем снова в твою игру!"
    sound snd_fabric1
    img 12444
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13799
    with fadelong
    citizen15 "Крутись уже! И не разочаруй меня!"
    img 13781
    with diss
    mt "Когда-нибудь моему терпению придет конец..."
    # движение на пилоне
    music Molten_Alloy
    img 13801
    with fadelong
    w
    img 13800
    with diss
    citizen15 "Йо, детка, а ты сегодня в ударе!"
    # движение на пилоне еще. в это время к пилону подходит ситизен14
    img 13802
    with diss
    w
    music Groove2_85
    img 13803
    with fade
    citizen14 "Ик! Эй друг, я смотрю ты тут развлекаешься!"
    citizen14 "Кстати, ты знаешь, я нравлюсь этой девочке! Хрюк..."
    citizen14 "Пожалуй, постою с тобой!"
    img 13804
    with diss
    citizen15 "Йо! Это моя бейба, друг!"
    # моника слезает с шеста
    music Power_Bots_Loop
    img 13805
    with hpunch
    m "Какого хрена здесь еще кто-то?"
    music Loved_Up
    img 13806
    with diss
    citizen15 "Бейб, не злись, это мой друг, а у друзей не может быть секретов!"
    img 13807
    citizen14 "Хрюк!"
    music Groove2_85
    img 13808
    m "Или ты сейчас же просишь своего друга свалить отсюда или я..."
    img 13809
    with fade
    citizen15 "Ого! Какая же ты горячая когда злишься!"
    citizen15 "Я слышал, что иногда надо делать вещи, о которых просят девочки."
    citizen15 "После этого они будут лучше сосать! Я уверен скоро ты меня об этом попросишь..."
    img 13810
    with diss
    menu:
        "Перестать терпеть это.":
            # моника злая
            music Power_Bots_Loop
            img 13811
            with fade
            m "Ах ты сволочь! А ну проваливай отсюда иначе тебе не поздоровится!"
            img 13812
            with diss
            citizen15 "Йо, девочка! Ты уверена? Если я уйду, ты не ничего не получишь и все закончится тем, что ты снова ко мне придешь."
            img 13813
            m "Мне плевать! Ты меня достал!"
            img 13814
            with fade
            citizen15 "Ха-ха-ха! Ладно, как скажешь"
            # ситизен15 уходит, событие у пилона полностью заканчивается. моника не получает денег
            return 1
        "Молча слушать.":
            pass
    img 13815
    with diss
    citizen15 "Йо, друг! Думаю тебе лучше уйти, это моя девочка!"
    citizen15 "Скоро я подгоню тебе какую нибудь дешевую шлюшку, не волнуйся."
    img 13816
    with diss
    citizen14 "Ик! А ты знаешь мои слабости. Ладно, уговорил."
    # ситизен14 уходит
    img 13817
    with diss
    w
    img 13818
    with fade
    citizen15 "Ну что, не хочешь ли ты попросить меня кое о чем?"
    img 13819
    m "Да. Где мои деньги?"
    img 13820
    with fade
    citizen15 "Я не совсем это имел ввиду, ну да ладно, в другой раз. Надо нагулять апетит."
    citizen15 "Вот твои деньги, бейба."
    return 2

label citizen15_autorun_comment1:
    mt "Мерзавец..."
    return
