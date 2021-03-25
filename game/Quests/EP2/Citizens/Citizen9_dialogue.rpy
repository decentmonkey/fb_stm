default citizen9BoobsNakesShowedLastDay = 0
default citizen9BoobsNakedDancedLastDay = 0
default citizen9BoobsNakesShowedCount = -1
default citizen9BoobsNakedDancedCount = -1
default citizen9BoobsNakesShowedCount1 = 0
default citizen9BoobsNakedDancedCount1 = 0
default citizen9DanceCloth = 0

default citizen9BoobsNakesEvent1 = False

label citizen9_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_9_1
    if citizen9_offered_last_day == day and monicaGotJoint != True:
        imgr Dial_Citizen_9_4
        citizen9 "Хэй! Мы уже разговаривали."
        return
    citizen9 "А? Да?"
    "Что?"
    menu:
        "Потрогай мою сиську." if monicaGotJoint == True:
            imgl Dial_Monica_Sandwich_0
            m "Потрогай мою сиську."
            imgr Dial_Citizen_9_3
            citizen9 "Как скажешь, дамочка."
            #подходит к монике сзади и хватает за грудь. так как на ней табличка, ей сложно сопротивляться.
            $ imagesArr = ["7110", "7111", "7112", "7113", "7114"]
            $ images = random.sample(set(imagesArr), 2)
            sound Jump2
            img images[0]
            w
            img images[1]
            w
            img scene_Hostel_Street
            imgl Dial_Monica_Sandwich_0
            imgr Dial_Citizen_9_3
            m "Идиот! Что ты делаешь?"
            imgr Dial_Citizen_9_3
            citizen9 "То, что ты мне сказала! Хе-хе-хе. Отличная грудь кстати!"
            m "Идиот! Я от Джека!"
            imgr Dial_Citizen_9_2
            citizen9 "Ууу, дамочка, с этого и надо было начинать. Что у тебя?"
            #citizen9 отходит
            menu:
                "Дать косяк.":
                    $ remove_inventory("joint", 1, True)
                    imgl Dial_Monica_Sandwich_0
                    $ add_corruption(1, "monica_give_joint_day_" + str(day))
                    m "Вот."
                    imgr Dial_Citizen_9_3
                    citizen9 "Отлично. Узнаю старину Джека. Отличная вещь. Хочешь?"
                    imgl Dial_Monica_Sandwich_1
                    call reduce_flyers() from _call_reduce_flyers_7
                    m "Нет, спасибо. Вот, возьми еще флаер."
                    imgr Dial_Citizen_9_2
                    citizen9 "Флаер? Ладно. Как насчет потрогать сиську еще раз?"
                    imgl Dial_Monica_Sandwich_2
                    m "Нет!"
                    mt "Идиот."
                    $ monicaGotJoint = False
                    $ citizen9_offered_last_day = day
                    $ kebabWorkHarassmentAmount +=1
                    return
                "Ничего":
                    imgl Dial_Monica_Sandwich_0
                    m "Ничего, я, кажется, ошиблась..."
                    return

        "Возьмите, пожалуйста, этот флаер..." if citizen9_offered_last_day != day:
            imgl Dial_Monica_Sandwich_1
            $ citizen9_offered_last_day = day
            #если нет косяка
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen9_refuse_probability) > 0:
                imgr Dial_Citizen_9_2
                citizen9 "А? Что?"
                "Флаер?"
                call reduce_flyers() from _call_reduce_flyers_8
                imgr Dial_Citizen_9_3
                "Хорошо..."
                citizen9 "Ооо, дамочка, а пойдемте к пилону! я потрогаю твою сиську еще разок!"
                menu:
                    "Да ни за что на свете!":
                        $ kebabWorkHarassmentAmount +=1
                        #img Моника злится
                        m "Мне ничего от тебя не нужно!"
                    "Ну точно не сейчас.":
                        m "Не в этот раз."
                        citizen9 "Ооо, ты не отказываешься... Хорошо. Тогда приходи, как будешь не так занята. Кстати, у Найджела есть деньги!"
            else:
                imgr Dial_Citizen_9_4
                citizen9 "Отстань, дамочка! Я пытаюсь кое-что вспомнить..."
                citizen9 "Вы меня отвлекаете!"
                $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
#        "Уйти.":
#            pass
    return

label Citizen_9_use_joint:
    $ obj_name = "Citizen_9"
    call citizens_dialogue_process() from _call_citizens_dialogue_process_1
    $ restore_music()
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen9_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_9_1
    m "Привет! Ты ведь покупал кое что у Джека?"
    citizen9 "Не совсем понимаю к чему ты клонишь..."
    imgr Dial_Citizen_9_3
    citizen9 "Ууу, дамочке нужна наличка?"
    m "Ну, не совсем..."
    citizen9 "Ага, рассказывай... По твоей одежде мне все понятно..."
    imgl Dial_begin35_18
    mt "Ах ты деревенщина! Ты даже не знаешь кто я такая!"
    citizen9 "Да ладно, дамочка, не злись."
    citizen9 "Знаешь подворотню с пилоном? Там часто появляются желающие заработать. Пойдем туда."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_213
    call pylonController(2, 1) from _call_pylonController_123
    with fadelong
    citizen9 "Ладно, дамочка, что там у тебя?"
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False
    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen9_dialogue_pilon_loop9:
    call pylonController(1, 1) from _call_pylonController_124
    if (pylonpart4startsCompleted == True and citizen9BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen9BoobsNakesShowedCount>=0:
        $ questHelp("work_slums_43", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_125
            citizen9 "Сиськи!"
            m "Что, это значит?"
            citizen9 "Дамочка, а что это может значить? Давай показывай!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_126
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(3, 3) from _call_pylonController_127
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_36
            call pylonController(3, 3) from _call_pylonController_128
            # img показывает сиськи
            citizen9 "Ну хоть что-то."
            call pylonController(3, 1) from _call_pylonController_129
            w
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_130
            citizen9 "Жопа!"
            m "Что 'Жопа!'?"
            call pylonController(4, 1) from _call_pylonController_131
            citizen9 "Повернись ко мне задом и показывай!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_132
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(4, 5) from _call_pylonController_133
            with fade
            m "Я не собираюсь раздеваться, только так."
            $ questHelp("work_slums_12", True)
            $ questHelp("work_slums_21", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")

            call showRandomImages(assImages, 4) from _call_showRandomImages_37
            call pylonController(4, 5) from _call_pylonController_134
            # img показывает зад
            citizen9 "Мда, скучно как-то. Приходи сюда вечером, увидишь как можно реально заработать."
            call pylonController(2, 1) from _call_pylonController_135
            w
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_136
            citizen9 "Потанцуй! Для этого здесь пилон и поставили!"
            mt "Наркоман...Надеюсь скоро тебя поймают..."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_137
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_138
            with fade
            m "Хорошо, только не долго."
            $ citizen9DanceCloth += 1
            if citizen9DanceCloth >= 3:
                $ questHelp("work_slums_21", True)

            call showRandomImages(pylonClothDanceImages8, 4) from _call_showRandomImages_38
#            call pylonController(4, 5)
            citizen9 "А у тебя неплохо выходит."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_139
            with fade
            w
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen9BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen9BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen9BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen9BoobsNakesShowedCount == -1:
                call cit9_naked_boobs_1st() from _call_cit9_naked_boobs_1st
                if _return != False:
                    $ citizen9BoobsNakesShowedCount += 1
            else:
                if citizen9BoobsNakesShowedCount%2 == 0:
                    call cit9_naked_boobs_variant1() from _call_cit9_naked_boobs_variant1
                if citizen9BoobsNakesShowedCount%2 == 1:
                    call cit9_naked_boobs_variant2() from _call_cit9_naked_boobs_variant2
                $ citizen9BoobsNakesShowedCount += 1
            if _return == 2:
                $ scene_sound = "snd_runaway"
                $ autorun_to_object("citizen9_comment1", scene="hostel_edge_1_a")
                call refresh_scene_fade() from _call_refresh_scene_fade_154
                sound snd_runaway
                return False
            if _return != False:
                $ citizen9BoobsNakesShowedCount1 = citizen9BoobsNakesShowedCount + 1
                if citizen9BoobsNakesShowedCount1 >= 3:
                    $ questHelp("work_slums_33", True)
                $ citizen9BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen9_dialogue_pilon_loop9




            call pylonController(4, 1) from _call_pylonController_140
            citizen9 "Голые сиськи! Я их люблю!"
            m "Что?"
            citizen9 "Да, дорогая, похоже, умом ты не отличаешься."
            "Покажи мне свои сисечки, только голыми!"
            mt "Когда нибудь я сдам тебя в полицию..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_141
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(4, 5) from _call_pylonController_142
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикаснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_39
            call pylonController(4, 5) from _call_pylonController_143
            citizen9 "Ууу... Так намного лучше! Ходи так всегда!"
            call pylonController(4, 1) from _call_pylonController_144
            mt "Размечтался..."
            citizen9 "Ты знаешь, тут не далеко продают кебабы, хотя ты конечно знаешь!"
            "Если ты сходишь мне вот так за кебабом, я дам тебе 100$. Что скажешь?"
            call pylonController(4, 1) from _call_pylonController_145
            m "Что значит Вот так?!"
            citizen9 "А что тут не понятно? Ну в одежде, которая на тебе сейчас."
            m "Да ни за что!"
            mt "Хотя 100$ - не маленькие деньги..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen9_dialogue_pilon_loop9


        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen9BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen9BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen9BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen9BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen9BoobsNakedDancedCount == -1:
                call cit9_naked_boobs_dance_1st() from _call_cit9_naked_boobs_dance_1st
                if _return != False:
                    $ citizen9BoobsNakedDancedCount += 1
            else:
                if citizen9BoobsNakedDancedCount%2 == 0:
                    call cit9_naked_boobs_dance_variant1() from _call_cit9_naked_boobs_dance_variant1
                if citizen9BoobsNakedDancedCount%2 == 1:
                    call cit9_naked_boobs_dance_variant2() from _call_cit9_naked_boobs_dance_variant2
                $ citizen9BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen9BoobsNakedDancedCount1 = citizen9BoobsNakedDancedCount + 1
                if citizen9BoobsNakedDancedCount1 >= 3:
                    $ questHelp("work_slums_43", True)
#                    $ questHelp("work_slums_52", skipIfExists=True)
                $ citizen9BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen9_dialogue_pilon_loop9

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
                call pylonController(2, 1) from _call_pylonController_146
                citizen9 "Ну что-то ты заслужила..."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_147
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_148
            citizen9 "Дамочка, ни цента! Ничего не получишь!"
            return False
    return

# первый раз
label cit9_naked_boobs_1st:
    music Groove2_85
    img 12240
    with fade
    citizen9 "Эй дамочка, ты же хочешь еще доллар?"
    img 12241
    m "..."
    img 12242
    citizen9 "Дамочка, когда тебя спрашивают, нужно отвечать!"
    img 12243
    with diss
    mt "Проклятье, мне нужны деньги..."
    m "Да."
    img 12244
    citizen9 "А вот и славно! Давай посмотрим что ты прячешь под кофточкой!"
    img 12245
    m "Под ней ничего нет..."
    img 12246
    citizen9 "Да, кроме твоих сисечек! Покажи их мне!"
    img 12247
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 12248
            m "Хватит и того, что ты уже видел!"
            return False
    img 12249
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12250
    citizen9 "Ох, какая ты скучная..."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 12251
    with fadelong
    w
    img 12252
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    music Loved_Up
    img 12253
    with diss
    w
    img 12255
    citizen9 "Ууу! Просто бомба!"
    citizen9 "Шикарно."
    # сиськи еще
    img 12256
    w
    img 12257
    w
    img 12258
    citizen9 "Слушай, а не найдется лу у тебя косячка?"
    citizen9 "Зрелище стало бы куда интереснее."
    # моника продолжает показывать
    img 12259
    with diss
    w
    img 12260
    w
    img 12261
    citizen9 "Ну ладно, можешь не отвечать..."
    # сиськи еще
    img 12262
    with diss
    w
    img 12263
    with diss
    w
    music Groove2_85
    img 12264
    with fade
    citizen9 "А ты ниче такая! Горячая штучка!"
    citizen9 "Я бы тебя каждый день..."
    img 12265
    with fade
    m "Ну ладно, хватит!"
    img 12266
    citizen9 "Ну что ты за обломщица?"
    img 12267
    with fade
    m "Хорошего понемногу."
    $ nakedBoobsFirstly_Cit9 = True
    return True

# вариант 1
label cit9_naked_boobs_variant1:
    music Groove2_85
    img 12268
    with fade
    citizen9 "Йо! Дамочка, давай заценим твои сисечки еще разок!"
    img 12269
    m "..."
    mt "Грязный наркоман... Но мне нужны деньги."
    img 12270
    citizen9 "Какая же ты некультурная. Нужно отвечать 'Давай!', а ты молчишь..."
    citizen9 "Ну дак что, глянем на твоих подружек еще разок?"
    img 12271
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12272
            m "Хватит и того, что ты уже видел!"
            return False
    img 12273
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12274
    citizen9 "..."
    # отворачивается, моника переодевается... сиизен пытается схватить, но моника замечает
    sound snd_fabric1
    img 12275
    with fadelong
    w
    sound Jump1
    img 12276
    with diss
    w
    music Power_Bots_Loop
    sound Jump2
    img 12277
    with hpunch
    w
    img 12278
    m "Какого черта?!"
    img 12279
    with diss
    citizen9 "Эй, детка, все путем!"
    img 12280
    m "Ничего не путем! Я просила тебя отвернуться."
    img 12281
    with diss
    citizen9 "Эй, дамочка, все честно! Да, просила, но я же не ответил."
    img 12282
    with fade
    m "Все, я ухожу..."
    music Groove2_85
    img 12283
    citizen9 "Йо, дамочка, так дела не делаются."
    $ add_money(1.0)
    citizen9 "Ладно, вот твой доллар, все путем да?"
    img 12284
    with diss
    m "..."
    m "Да."
    mt "Проклятье, Моника, до чего ты дошла..."
    img 12285
    citizen9 "Я знал, что это решит наш маленький конфликт!"
    citizen9 "Продолжим?"
    return True

# вариант 2
label cit9_naked_boobs_variant2:
    music Groove2_85
    img 12286
    with fade
    citizen9 "Дамочка, покажи сиськи!"
    img 12287
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12288
            m "Хватит и того, что ты уже видел!"
            return False
    img 12289
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12290
    citizen9 "..."
    # отворачивается, моника переодевается...
    music Loved_Up
    sound snd_fabric1
    img 12291
    with fadelong
    w
    img 12292
    with diss
    w
    img 12293
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    img 12294
    with diss
    w
    img 12295
    with diss
    w
    img 12296
    w
    img 12297
    citizen9 "Йо! Шик!"
    # сиськи
    img 12298
    with diss
    w
    img 12299
    w
    music Groove2_85
    img 12300
    with fade
    citizen9 "Классные дойки, дамочка! Я бы за них подергал!"
    img 12301
    citizen9 "Кстати, у меня идея!"
    citizen9 "Закрой глаза!"
    img 12302
    with diss
    m "Это еще зачем?"
    img 12303
    citizen9 "Да так, у меня для тебя сюрприз!"
    img 12304
    mt "Этот изврашенец что-то задумал?"
    menu:
        "Закрыть глаза.":
            # закывает глаза ситизен подходит сзади и хватает
            img 12305
            with fade
            w
            img 12306
            with diss
            w
            sound Jump1
            img 12307
            with diss
            citizen9 "Сюрприз!"
            music Power_Bots_Loop
            sound Jump2
            img 12308
            with hpunch
            w
            img 12309
            with fade
            m "Что?! Ах ты гад! Да я тебя!"
            img 12310
            with diss
            citizen9 "О! Они просто восхитительные! Ты знаешь, однажды я также схватил дамочку, которая раздавала флаеры..."
            # Сделать какую то привязку к тому событию или по простому: моника ему наваляет и он убегает?
            music stop
            sound snd_punch_face1
            img 12311
            with diss
            w
            sound snd_punch_face2
            img 12312
            with diss
            w
            sound snd_punch_face
            img 12313
            with diss
            w
            img black_screen
            with diss
            sound snd_down1
            pause 3.0
            return 2
            $ citizen9BoobsNakesEvent1 = True
        "Ну уж нет!":
            img 12314
            with fade
            m "Ну уж нет!"
            img 12315
            citizen9 "Дамочка, ты меня разочаровываешь..."
            pass
    # сиськи
    img 12316
    with diss
    w
    img 12317
    with diss
    w
    music Groove2_85
    img 12318
    with fade
    m "Ну все, хватит."
    img 12319
    citizen9 "Ну ты даешь! Я только представил как засовываю между них мой большой..."
    img 12320
    m "Я поняла!"
    img 12321
    citizen9 "Йо! Да неужели? И вероятно еще и представила! Ха-ха-ха!"
    img 12322
    with fade
    mt "Извращенец, когда я верну свое положение, я найду тебя..."
    return True

label citizen9_comment1:
    mt "Мерзавец!"
    return

# первый раз танцы с сиськами
label cit9_naked_boobs_dance_1st:
    music Groove2_85
    img 13631
    with fade
    citizen9 "Йо, дамочка! Давай посмотрим на твои сисечки!"
    img 13632
    mt "Как же ты меня бесишь, если бы мне не были так нужны деньги, то я..."
    img 13633
    citizen9 "И ты же уже знаешь, зачем нужен пилон..."
    citizen9 "Лезь на него!"
    img 13634
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            music Power_Bots_Loop
            img 13635
            with fade
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13316
    with fade
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет..."
    img 13636
    m "Знаешь что, я тебе не верю. Деньги сразу!"
    img 13637
    citizen9 "Вот это ты придумала!"
    citizen9 "А если мне не понравится?"
    img 13638
    mt "Ах ты сволочь..."
    img 13639
    m "Тебе же нравилось все, что ты видел до этого..."
    img 13640
    citizen9 "Ладно, дамочка, держи! А теперь раздевайся!"
    img 13641
    m "Отвернись!"
    # отворачивается
    img 13642
    citizen9 "Так и быть!"
    sound snd_fabric1
    img 12251
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13643
    with fadelong
    w
    img 13644
    with diss
    citizen9 "Йо! Ну неужели сама не догадываешься, что пилон уже тебя заждался?!"
    # движение на пилоне
    music RocknRoll_loop
    img 13645
    with fadelong
    w
    img 13646
    with diss
    citizen9 "О да!"
    # движение на пилоне еще
    img 13648
    with diss
    w
    img 13647
    with diss
    citizen9 "Порадуй старину Найджела!"
    # движение на пилоне еще
    img 13649
    with diss
    w
    img 13650
    with diss
    citizen9 "Горяча!"
    # моника слезает с шеста
    music Groove2_85
    img 13651
    with fadelong
    m "Все, достаточно!"
    img 13652
    citizen9 "И правда хватит. Пора засунуть мой член меджу твоих сисек!"
    citizen9 "Я же уже заплатил..."
    music Power_Bots_Loop
    img 13653
    with hpunch
    m "?!"
    music Groove2_85
    img 13654
    with fade
    citizen9 "Шутка! Дамочка, в тебе ни капли чувства юмора."
    img 13655
    mt "Зато твое чувство юмора ужасно... Мерзавец!"
    $ nakedBoobsDanceFirstly_Cit9  = True
    return True

#  танцы с сиськами 1 вариант
label cit9_naked_boobs_dance_variant1:
    music Groove2_85
    img 13663
    with fade
    citizen9 "Йо, я соскучился по твоим танцам на пилоне!"
    citizen9 "Станцуй!"
    img 13634
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            music Power_Bots_Loop
            img 13635
            with fade
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13664
    with fade
    m "Знаешь что, почему ты так плохо со мной обращаешься?"
    img 13665
    citizen9 "Не, дамочка, с тобой я еще хорошо обращаюсь!"
    citizen9 "Здесь недалеко есть пара шлюх, вот с ними я..."
    img 13666
    m "Мне неинтересно!"
    img 13667
    citizen9 "Ну и ладно! Тогда пулей на пилон! И разденься!"
    img 13668
    m "А ты отвернись!"
    # отворачивается. достает тел и по тихому снимает как моника переодевается
    sound Jump1
    img 13669
    with diss
    citizen9 "О да! Это видео непременно пойдет в мою коллекцию..."
    img 13670
    call photoshop_flash() from _call_photoshop_flash_151
    w
    sound snd_fabric1
    img 13671
    with fadelong
    # поворачивается моника стоит с сиськами
    w
    img 13672
    citizen9 "Класс! Я доволен!"
    img 13673
    with diss
    mt "Интересно чем..."
    img 13674
    citizen9 "Танцуй же уже!"
    # движение на пилоне
    music RocknRoll_loop
    img 13675
    with fadelong
    w
    img 13676
    with diss
    citizen9 "Да, дамочка, это твое призвание!"
    # движение на пилоне
    img 13677
    with diss
    w
    img 13678
    with diss
    citizen9 "Да ты просто бомба!"
    # моника слезает с шеста
    music Groove2_85
    img 13651
    with fadelong
    m "Все, достаточно!"
    img 13652
    citizen9 "Я бы так не сказал, но в любом случае, дома у меня будет еще неколько часов важных дел..."
    citizen9 "Я буду смотреть порно!"
    img 13653
    with diss
    m "Я и без тебя это поняла..."
    img 13654
    citizen9 "А ты догадливая ... Иногда..."
    citizen9 "Но все равно, надеюсь, к следующему разу ты разучишь больше движений."
    return True

#  танцы с сиськами 2 вариант
label cit9_naked_boobs_dance_variant2:
    music Groove2_85
    img 13663
    with fade
    citizen9 "Расчехляй близняжек и на шест!"
    img 13634
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13635
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13637
    with fade
    citizen9 "Я даже сам отвернусь..."
    img 13638
    mt "Что это с ним?"
#    w
#    img 1225
    # поворачивается, моника с сиськами
    sound snd_fabric1
    img 13643
    with fadelong
    citizen9 "Залезай пожалуйста на шест."
    img 13673
    mt "А где же Йо? Что с ним сегодня?"
    # движение на пилоне
    music RocknRoll_loop
    img 13680
    with fadelong
    w
    img 13679
    with diss
    citizen9 "Очень красиво!"
    # движение на пилоне
    img 13681
    with diss
    w
    img 13682
    with diss
    citizen9 "Очень, очень красиво!"
    # моника слезает с шеста
    music Groove2_85
    img 13683
    with fadelong
    m "Что с тобой сегодня?"
    img 13684
    citizen9 "Со мной все в порядке, просто я прочитал в гороскопе, что в течение дня мне лучше быть вежливым и, возможно, я добьюсь чего-то большего."
    img 13685
    mt "Возможно, но явно не со мной."
    img 13686
    with fade
    citizen9 "Вот, возьми пожалуйста твои деньги."
    # моника берет дкньги
    img 13687
    with fadelong
    citizen9 "И все?"
    img 13688
    with diss
    m "А чего ты хотел?"
    img 13689
    citizen9 "Ну я же был вежлив..."
    img 13690
    with diss
    m "Ну тебе же ясно в гороскопе сказали 'возможно добьетесь'. Со мной ничего не удалось."
    img 13691
    citizen9 "Йо, дамочка! Все гороскопы отстой, я знал это!"
    return True

label cit9_groping_first:
    citizen9 "Йо! Угадай, что я тебе принес сегодня!"
    m "..."
    mt "Мне ничего не нужно от таких как ты!"
    citizen9 "Что, никаких идей?"
    citizen9 "Ну и скучная ты дамочка!"
    citizen9 "Я принес тебе 5 долларов!"
    mt "Предел мечтаний..."
    citizen9 "Дамочка, я готов тебе их дать!"
    m "Ну дак дай, что тебя останавливает?"
    citizen9 "Да ничего! Только перед этим я хочу подержаться за твою попку!"
    m "Что?!"
    citizen9 "Да, ты все правильно услышала."
    citizen9 "Вот только не надо никаких комментариев."
    citizen9 "Просто скажи хочешь ли ты 5 долларов?"
    m "Не таким способом! Чтобы меня трогал такой как ты?"
    citizen9 "Какой? Вообше-то я красавчик!"
    citizen9 "Давай дамочка, решай уже быстрее. Да или нет."
    mt "Неужели я позволю этому ничтожному наркоману потрогать мою попу?"
    mt "Он заплатит, но это так немного... Что же делать?"
    menu:
        "Ладно, мне нужны деньги.":
            m "Ладно."
            pass
        "Я не пойду на такое.":
            m "Я не готова пойти на такое."
            m "Мне не нужны твои жалкие 5 долларов!"
            citizen9 "Йо, дамочка, не груби! Сегодня не нужны, завтра будут нужны!"
            return False
    citizen9 "Йо! Правильно, дамочка! 5 долларов на дороге не валяются!"
    citizen9 "Давай уже начнем!"
    menu:
        "...":
            m "..."
            pass
        "Я передумала.":
            m "Я передумала."
            mt "Ты отвратителен..."
            citizen9 "Йо, дамочка, так дела не делаются!"
            m "Мне плевать, я передумала."
            return False
    # подошел к монике
    citizen9 "Дамочка, что-то мне подсказывает, что ты тоже этого хочешь."
    mt "И не надейся..."
    # подходит, обнимает монику и держит за жопу
    citizen9 "Йо! Вот это жопа!"
    citizen9 "Я уже давно не трогал такую!"
    citizen9 "Высший класс!"
    m "Ну все, хватит, надоел!"
    citizen9 "Не жадничай, дамочка!"
    m "Я сказала хватит!"
    #отпускает
    citizen9 "Вот ты жадина!"
    citizen9 "Но я доволен! Не каждые день трогаешь такую попку!"
    citizen9 "Если что, у меня есть еще 5 долларов. Хочешь?"
    m "Нет."
    mt "Как же ты мне надоел своими разговорами..."
    citizen9 "Обманщица!"
    citizen9 "Ладно, дамочка, держи."
    citizen9 "В другой раз продолжим!"
    return True

    # опция помять или сунуть руку - спешал

label cit9_groping_regular:
    citizen9 "Дамочка, угадай, кто соскучился по твоей попке?"
    mt "Когда-нибудь я не выдержу и ударю тебя по-настоящему..."
    citizen9 "Йо! Ну это же простой вопрос!"
    citizen9 "Конечно же я!"
    citizen9 "И угадай, что я тебе принес?"
    m "..."
    citizen9 "Ну конечно же 5 долларов!"
    citizen9 "И если ты скажешь, что ты рада, долларов станет 6!"
    mt "Доллар за два слова этому грязному наркоману..."
    mt "Ведь больше этого никто не услышит..."
    mt "И естественно, это не правда..."
    menu:
        "Я рада.":
            m "Я рада."
            citizen9 "Да! А уж я то как рад! Давай уже быстрее начнем!"
            pass
        "Молчать.":
            m "Я не собираюсь говорить ничего подобного!"
            citizen9 "Какая же ты все-таки скучная! Не хочешь доллар..."
            pass
    citizen9 "Дамочка, подойди на шаг ближе!"
    # моника становится чуть ближе и ситизен схватив ее за зад начинает его сильно мять
    m "Ай! Какого черта?!"
    m "Больно!"
    citizen9 "Хе-хе! Не обманывай, с тобой такое делают по 10 раз на дню!"
    citizen9 "Я знаю, что тебе это нравится!"
    m "Хватит."
    # моника отталкивает и ситизен падает
    citizen9 "Йо! Как грубо!"
    citizen9 "Да что с тобой не так? Все мужики так делают со своими цыпочками!"
    m "Я не твоя цыпочка! И никогда ей не буду!"
    m "И я позволила дотронуться до моей попы, а не мять ее!"
    citizen9 "Ах вот ты как! Тогда не получишь 5 долларов!"
    # моника зло:
    m "Ты меня всю облапал и теперь говоришь, что ничего мне не дашь?!"
    m "Ты уверен?"
    citizen9 "Йо, дамочка! Я пошутил! Ты же любишь шутки?"
    citizen9 "Кстати, я тут учавствую в стендапе в одном из баров...Приходи!"
    mt "Да ни за что..."
    citizen9 "Вот твои 5 долларов! Йо!"
    return True

label cit9_special:
    citizen9 "Йо! Дамочка, я хочу извиниться!"
    m "Ты?!"
    m "Извиниться?!"
    citizen9 "Да, именно извиниться."
    m "И за что же?"
    mt "Хотя уж тебе-то есть за что извиняться, грязный наркоман..."
    citizen9 "За то, что слишком сильно мял твою восхитительную попку!"
    citizen9 "Тебе наверное было больно?"
    mt "Да что с ним такое?"
    citizen9t "Расслабься, дамочка, у меня для тебя сюрприз..."
    citizen9 "Я даже принес тебе 10 долларов! Я же хочу извиниться!"
    mt "Что-то тут не так...Чего он хочет?"
    mt "Может, стоит просто забрать у него эти 10 долларов и сказать, что извинение принято?"
    menu:
        "Извинение принято.":
            m "Извинение принято."
            pass
        "Я не собираюсь тебя прощать.":
            m "Я не собираюсь тебя прощать!"
            mt "Он ведет себя очень странно. Я не знаю, что у него на уме, но лучше закончить этот разговор."
            m "И не нужны мне твои деньги!"
            citizen9 "Йо! Вот ты как...Ну ничего, думаю, скоро вернемся к этому разговору."
            return False
    citizen9 "Я знал, что ты добрая!"
    m "Да. А теперь, дай мне 10 долларов!"
    citizen9 "Конечно, дамочка, но только после того, как я подуржусь за твою попку!"
    citizen9 "Я обещаю, я не буду ее мять."
    citizen9 "И я дам тебе 10 долларов! Вспомни, до этого я давал тебе только 5!"
    mt "Стоит ли доверять этому лживому наркоману?"
    citizen9 "И я даже готов дать тебе сейчас половину. Вот, возьми!"
    # дает монике 5 долларров
    citizen9 "А теперь, дай потрогать твою попку!"
    mt "Я уже позволяла ему это..."
    mt "Черт, мне нужны деньги!"
    mt "Тем более, он обещал не мять мою попку..."
    mt "Стоит ли ему верить?"
    citizen9t "Давай, дамочка, соглашайся..."
    menu:
        "Ладно.":
            m "Ладно."
            citizen9 "Йо! Я знал, что ты не откажешь себе в этом удовольствии!"
            mt "Каком еще удовольствии? В этом нет никакого удовольствия..."
            pass
        "Нет!":
            m "Нет!"
            citizen9 "Нет?! Йо, я дал тебе 5 долларов!"
            m "И что? Я не дам тебе трогать мою попу!"
            citizen9 "Тогда отдавай мои 5 долларов!"
            m "Ты же сам сказал, что это извинение."
            m "Извинение принято."
            citizen9 "...."
            return False
    citizen9 "Давай же уже начнем!"
    # подходит и кладет руки на попу
    citizen9 "Прекрасное чувство..."
    citizen9t "Ну же, дамочка, расслабься..."
    mt "Он просто держит руки у меня на попе..."
    mt "И долго это будет продолжаться?!"
    citizen9t "Уже почти...Вот сейчас!"
    # ситизен резко отрывает руки, и сует их монике под шерты
    # и засовывает палец в зад
    m "Ай!!! Больно!"
    citizen9 "Какой у тебя зад, дамочка! Я уже и не встречал!"
    # вынимает палец и руки из под шерт моники. она в ярости
    m "Я убью тебя, грязный наркоман!!!"
    citizen9 "Ой-ой, похоже, кто-то не в духе..."
    citizen9 "Не кипятись, дамочка!"
    m "Тебе конец!"
    # отходит, моника наступает
    citizen9 "Йо! Я тут вспомнил об одном важном деле... Пожалуй я пойду... Точнее побегу..."
    citizen9 "До встречи, дамочка!"
    citizen9 "Приходи, как будешь в настроении!"
    # ситизен убегает. это конец диалога с ним дальше действия на пилоне не доступны в рамках дня
    mt "Этот грязный наркоман засунул свой грязный палец в мою попу..."
    mt "Я убью его!"
    mt "..."
    mt "Черт, это ужасно...Здесь одни извращенцы..."
    mt "Надо быть еще более осторожной..."
    return True
