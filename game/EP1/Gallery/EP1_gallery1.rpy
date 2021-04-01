
label gallery_1018:
    music casualMusic
#    $ map_enabled = True
#    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)
#    $ add_objective("take_bath", _("Принять душ"), c_green, 1)
#    $ add_objective("eat", _("Позавтракать"), c_green, 2)
#    $ add_objective("go_outside", _("Одеться и идти на улицу"), c_orange, 10)

#    $ miniMapDisabled = ["Basement"]

#    m "test!"
#    call bedroom1 from _call_bedroom1
#    jump show_scene
#    imgc monica_homecloth1_disgust1

#    show monica_homecloth1_отвращение1 at dialogue_image_left

#    show screen dialogue_image_center("monica_homecloth1_отвращение1", config.screen_width / 2, config.screen_height)
#    show img_1011 at dialogue_image_left
#    $ dialogue_active_flag = False
    img 1010
    with fadelong
#    music All_Stars_Loop
    m "Доброе утро! Меня зовут Моника Бакфетт! Я замужем."

    "Мы с мужем поженились 12 лет назад."

    img 1011
#    music BossaBossa
    "Мой муж очень богат.
    После свадьбы мы поселились в этом большом доме."

    "Люблю-ли я мужа?
    Можно сказать что люблю.
    Он такой мягкий и пушистый."

    img 1010
#    music All_Stars_Loop
    "Я с удовольствием им управляю."

    img 1011
    sound snd_far_hit
    mt "На улице что-то хлопнуло"

    img img_1010
    pause 0.5
    img img_1013
    with Dissolve(0.5)
#    music BossaBossa
    m "Любовь?
    Моя главная любовь - это власть и управление людьми."

    "А еще я считаю что я очень красива.
    Я люблю свою красоту, вот моя любовь :)"

    "У меня свой бизнес.
    Я владею очень популярным журналом моды.
    Многие девушки завидуют мне."

    "Мне вообще все завидуют."

    "Но я считаю что это их проблемы.
    Неудачники всегда завидуют таким успешным людям."

    "Таким как я :)"

    "Впрочем что-то я задумалась.
    Пора вставать, собираться и ехать заниматься своим любимым делом :)"

    img 1018
    "Итак, что мне надо сделать."

    "Надо одеться в домашнюю одежду.
    Надо принять душ. Надо позавтракать.
    Надо одеться на выход и идти на улицу."

    "Фред (это мой водитель) должен ждать меня на улице."

    img 1019
    "И только пусть попробует его там не оказаться когда я выйду! (злобно ухмыляется)."

    "Он старается, но у него и так уже много промахов.
    Я подумываю о том чтобы его заменить."

    img 1020
    "Людей вообще надо почаще менять.
    Независимо от того стараются они или нет."

    "Люди..."

    img 1021
    "Люди просто надоедают вот и все."

    w
#    $ scene_refresh_flag = True
#    $ scene_transition = "Fade"
#    call change_scene("bedroom1", "Fade_long") from _call_change_scene_84

#    $ add_inventory("phone", 1, True)
    return

label gallery_1035:
#    if scene_name == "floor1":
#        if day == 1 and day_time == "evening":
#            call julia_day1_evening(obj_name, obj_data) from _call_julia_day1_evening
#            return
#        if day == 2 and day_time == "day":
#            call julia_day2_day(obj_name, obj_data) from _call_julia_day2_day
#            return
#        if day == 2 and day_time == "evening":
#            call julia_day2_evening(obj_name, obj_data) from _call_julia_day2_evening
#            return
#        if day == 3 and day_time == "day":
#            call julia_day3_day(obj_name, obj_data) from _call_julia_day3_day
#            return


#        if julia_monica_revenge_in_progress == True:
#            jump floor2_julia_monica_revenge_julia_punish2
#        if juliaSeen == False:
#            if obj_data["action"] == "l":
#                img 1028
#                img 1029
#                mt "А вот и Юлия.
#                Она работает у меня гувернанткой."

#                img 1030
#                mt "Она из бедной семьи.
#                Старается работать, но немного туповата."

#                img 1031
#                "Постоянно что-то путает и не туда кладет.
#                Ее можно научить делать все как надо, но мне лень этим заниматься"

#                img 1032
#                "Я считаю что если человек пришел куда-то работать, то должен уже уметь это делать."

#                "Юлии повезло что я пока добрая, но это ненадолго."

#                "...."

#                $ juliaSeen_action = True

#            if obj_data["action"] == "t":
#                if juliaSeen_action == False:

#                    img 1028
#                    img 1029
#                    mt "А вот и Юлия.
#                    Она работает у меня гувернанткой."

#                    img 1030
#                    mt "Она из бедной семьи.
#                    Старается работать, но немного туповата."

#                    img 1031
#                    "Постоянно что-то путает и не туда кладет.
#                    Ее можно научить делать все как надо, но мне лень этим заниматься"

#                    img 1032
#                    "Я считаю что если человек пришел куда-то работать, то должен уже уметь это делать."

#                    "Юлии повезло что я пока добрая, но это ненадолго."

#                    "...."

#                    $ juliaSeen_action = True
    music casualMusic
    img 1028
    img 1029
    mt "А вот и Юлия.
    Она работает у меня гувернанткой."

    img 1030
    mt "Она из бедной семьи.
    Старается работать, но немного туповата."

    img 1032
    with Dissolve(0.5)
    menu:
        "Позвать Юлию грубо":
#            $ juliaMonicaYell = True
#            call bitch(5, "call_julia1") from _call_bitch_29
            img 1033
            m "Юлия!
            Что ты там копаешься???"

            "Быстро подойди ко мне!!!"

            img 1034
            "Я сказала БЫСТРО!!!"

            sound highheels_run2
            wc
            img 1035
            julia "Да, миссис Бакфетт?
            Чем я могу Вам помочь?"

            img 1036
            m "Я не должна говорить тебе чем можно мне помочь.

            Знаешь что должно быть вместо этого??"

            julia "Что, миссис...?"

            m "Вместо этого ты сама должна знать чем помочь, а не спрашивать!!!"

            m "Ясно тебе?"

            img 1037
            julia "Да, миссис, я поняла."

            julia "Я стараюсь."

            m "Приготовь мне завтрак и сходи посмотри на улицу что там случилось."

            img 1038
            julia "Да, миссис, я все сделаю тот час."

            m "Ну, и?
            Что ты стоишь???"

            img 1039
            "БЫСТРО!!!"
            sound highheels_run1
#            $ juliaLocation = "kitchen"
#            $ juliaSeen = True
#            call refresh_scene() from _call_refresh_scene_9
            show screen notify (_("Юлия убежала на кухню."))
#            $ juliaNeedToCheckStreet = True

            menu:
                "Ехидный комментарий в адрес Юлии.":
#                    call bitch(2, "call_julia1") from _call_bitch_30
                    img 1040
                    m "Глупое никчемное создание."

                    "Я наверное очень добрая раз терплю вокруг всех этих недалеких людей."

                    "Мне, наверное, надо какую-то награду за доброту."

                    "Типа как Мать Тереза."

                    img 1041
                    "Интересно, какую шляпку я бы одела если бы меня награждали..."

                    "Впрочем, я снова замечталась."

                    if bathTaken == False:
                        "Надо скорее принять душ и покушать."
                    else:
                        "Надо скорее покушать."
                    return
                "Продолжить заниматься делами.":
                    return

        "Позвать Юлию вежливо":
            sound highheels_run1
#            $ juliaMonicaYell = False
#            call bitch(-5, "call_julia1") from _call_bitch_31
            img 1032
            m "Юлия!
            Не могла-бы ты подойти ко мне?"

            img 1038
            julia "Да, миссис Бакфетт."

            "Чем могу Вам помочь?"

            menu:
                "Спросить у Юлии что случилось на улице.":
                    img 1038
                    m "Юлия, ты не знаешь что был за шум на улице с утра?"

                    julia "Нет, Миссис Бакфетт, не знаю."

                    m "Юлия, могла-бы ты узнать что случилось?"

                    julia "Да, Миссик Бакфетт, конечно, я узнаю."

                    "Позвольте вначале подать Вам на стол?"

                    m "Конечно, Юлия, подай на стол, затем может пойти узнать."

                    julia "Конечно, Миссис Бакфетт.
                    Одну минуту.
                    Сейчас подам Вам."

                    sound highheels_run1
#                    $ juliaLocation = "kitchen"
#                    $ juliaSeen = True
#                    call refresh_scene() from _call_refresh_scene_10
                    show screen notify (_("Юлия убежала на кухню."))
#                    $ juliaNeedToCheckStreet = True

                "Попросить подать еду.":
                    img 1038
                    m "Юлия, можешь подавать еду на стол."

                    julia "Конечно, Миссис Бакфетт.
                    Одну минуту.
                    Сейчас подам Вам."
                    sound highheels_run1
#                    $ juliaLocation = "kitchen"
#                    $ juliaSeen = True
#                    call refresh_scene() from _call_refresh_scene_11
                    show screen notify (_("Юлия убежала на кухню."))

#        if juliaSeen == True:
#            call julia_interact3(obj_name, obj_data) from _call_julia_interact3

#    if scene_name == "kitchen":
#        call julia_interact2(obj_name, obj_data) from _call_julia_interact2
    return

label gallery_1047:
#    if obj_name == "Monica":
#        if monicaBathroomForbidden == True:
#            mt "Эта сучка Бетти запретила мне пользоваться ванной комнатой!"
#            return
#        m "Что бы мне принять?"

#        "Душ?"

#        "Или ванну?"

#    if obj_name == "Bath":
#        if monicaBathroomForbidden == True:
#            mt "Эта сучка Бетти запретила мне пользоваться ванной!"
#            return
#        if obj_data["action"] == "l":
#            m "Я обожаю свою ванну."

#            "В ней можно наслаждаться уединением и ни о чем не думать."

#            "Ни о чем не думать - это не так-то просто для такой умной девушки как я."

#        if obj_data["action"] == "h":
#            if gameStage > 2 and monicaBathroomForbidden == False:
#                call afterJailHouse_dialogue9() from _call_afterJailHouse_dialogue9
#                return
#            if cloth_type != "HomeCloth":
#                m "Не полезу же я в платье в ванную!"
#                "Мне надо переодеться сначала!"
#                return
#            if bathTakenJust == True:
#                m "Я недавно принимала водные процедуры.
#                Но почему-бы не понежиться еще..."
#                wc
    sound snd_bathroom
    img 1047
    with fade
    w
    img 1048
    w
    img 1049
    w
    img 1050
    m "Как же хорошо понежиться в ванной!"
    w
#            $ remove_objective("take_bath")
#            $ bathTaken = True
#            $ bathTakenJust = True
#            $ scene_transition = "Fade"
    return

label gallery_1045:
#    if obj_name == "Shower":
#        if monicaBathroomForbidden == True:
#            mt "Эта сучка Бетти запретила мне пользоваться душем!"
#            return
#        if obj_data["action"] == "l":
#            m "Душ мне по душе."

#            "Мне нравится как капельки воды стекают по моему телу."

#        if obj_data["action"] == "h":
#            if gameStage > 2 and monicaBathroomForbidden == False:
#                call afterJailHouse_dialogue9() from _call_afterJailHouse_dialogue9_1
#                return
#            if cloth_type != "HomeCloth":
#                m "Не пойду же я в платье в душ!"
#                "Мне надо переодеться сначала!"
#                return
#            if bathTakenJust == True:
#                m "Я недавно принимала водные процедуры.
#                Но почему-бы не понежиться еще..."
#                wc
    sound snd_shower
    img 1045
    with fade
    w
    img 1046
    w
    img 1048
    w
    img 1049
    w
    img 1050
    m "Как же хорошо принять душ!"
    w
#            $ remove_objective("take_bath")
#            $ bathTaken = True
#            $ bathTakenJust = True
#            $ scene_transition = "Fade"
    return

label gallery_1053:
#    if juliaLocation != "kitchen":
#        m "Мне надо распорядиться гувернантке подать еду на стол."

#        "Я не собираюсь заниматься этим сама!"

#        return
#    if day == 3:
#        if day_time == "day":
#            jump eat_day3
#    if day == 2:
#        if day_time == "day":
#            jump eat_day2
#        if day_time == "evening":
#            jump eat_day2_evening
#    if day == 1:
#        if day_time == "day":
    music casualMusic
    img 1051
    "Юлия! Можешь подавать еду!"
    img 1052
    julia "Да, Миссис Бакфетт, одну секунду!"
    wc
    sound highheels_run2
    img 1053
    with fade
    julia "Пожалуйста, Миссис Бакфетт."

    "Приятного аппетита!"

    menu:
        "Спасибо и брысь отсюда!":
            img 1054
            m "Спасибо..."

            "И..."

            m "Брысь отсюда!"
#                    call bitch(2, "julia_eat_1_morning") from _call_bitch_25

            julia "Да, Миссис Бакфетт.
            Не смею Вам мешать."

        "Спасибо!":
            img 1054
            m "Спасибо..."

            "Можешь идти."

#                    call bitch(-2, "julia_eat_1_morning") from _call_bitch_26

            julia "Да, Миссис Бакфетт.
            Не смею Вам мешать."

    sound highheels_run1
    wc
    img 1055
    with fade
    m "Юлия готовит довольно вкусно."

    "Мда, определенно вкусно."

    "Может стоит ее похвалить?"

    menu:
        "Что за вздор, кого еще хвалить?":
            img 1056
            m "Что за вздор."
            "Кого хвалить?"
            "Какую-то служанку?"
#                    call bitch(2, "julia_eat_2_morning") from _call_bitch_27

        "Похвалить при случае":
            img 1055
            m "Похвалю ее при случае."
#                    call bitch(-2, "julia_eat_2_morning") from _call_bitch_28
#                    $ juliaPraiseOnOccasion = True

#            $ monicaEated = True
#            $ remove_objective("eat")
#            $ juliaLocation = "none"

    wc
    img 1055
    with fade
    imgc Monica_HomeCloth1_Thinking1
    m "Ну что-ж."

    "Я Поела."
#            if bathTaken == True:
#                "Помылась."

#                "Теперь пора одеваться и идти на улицу."
#            else:
    "Осталось принять душ, одеваться и идти на улицу"

    "К Фреду."
    "Пока этот никчемный болван куда-нибудь не подевался."

    "Я собираюсь одеть новое платье.
    Надеюсь Юлия его подготовила и повесила в шкаф.
    Надо пойти в спальню проверить."
    return

label gallery_1086:
#    $ floor2SpotJustMade = False
    music casualMusic
    if julia_monica_revenge_undo_in_progress == False:
        img 1080
        with fade
        m "ВОТ!"
        menu:
            "Обвинить во всем Юлию":
                m "ВОТ!"
                m "ПОСМОТРИ ЧТО ТЫ НАДЕЛАЛА!!!"
#                call bitch(5, "monica_julia_revenge_lie") from _call_bitch_15
#                $ juliaMonicaLied = True
                img 1092
                julia "Аххххх!!!"

                img 1081
                julia "Но Миссис Бакфетт!
                Когда я проходила здесь в последний раз, этого пятна не было!"

                img 1082
                m "И?"

                "ЧТО ТЫ ХОЧЕШЬ СКАЗАТЬ?"

                "ЧТО ЭТО Я ПОСТАВИЛА ЭТО ПЯТНО???"

                img 1083
                julia "Нет, конечно, Миссис Бакфетт!"

                "Я ни в коем случае не говорила этого!"

                img 1082
                m "А ОТКУДА ТОГДА ЭТО ПЯТНО?"

                m "И ГЛАВНОЕ!
                ЧТО ТЕПЕРЬ С ЭТИМ ДЕЛАТЬ???"


            "Признаться что сама поставила пятно":
#                $ juliaMonicaLied = False
#                call bitch(-5, "monica_julia_revenge_lie") from _call_bitch_16
                m "Посмотри что из-за тебя случилось!"
                "Пока я носилась сама с этим платьем, я поставила пятно на ковер!"
                julia "Аххххх!!!"

        img 1083
        julia "Миссис Бакфетт, пожалуйста!"

        "Это пятно так просто не оттереть."

        "Этому ковру нужна химчистка!"

        menu:
            "Ты что, серьезно? Ты сама ототрешь это пятно!!!":
#                call bitch(10, "monica_julia_revenge_punished") from _call_bitch_17
#                $ juliaPunished = True
#                $ juliaPunishedLow = False
#                $ juliaPunishedVoluntarily = False
#                $ juliaLocation = "floor2"
                img 1084
                m "Правда?"

                "Да ты что, серьезно??"

                "У меня как раз есть партнер у которого сеть элитных химчисток!"

                "И исправить этот ковер будет совсем недорого!"

                "Всего около $10.000."

                "И я думаю вычту это с твоей зарплаты."

#                if juliaMonicaLied == False:
#                    "Хоть это пятно сделала и не ты, но в твои обязанности входит следить за порядком в доме."
#                    "Так что отвечать за это придется тебе!"

                "Даже не знаю сколько тебе придется работать."

                "Но это в любом случае будет дешевле для тебя, чем увольняться и платить неустойку за 3 года работы."

                "Согласно нашему трудовому договору."

                mt "Дик молодец."

                "Всегда делает договора какие надо."

                img 1086
                julia "О Боже!!!"

                "Миссис Бакфетт!"

                "Умоляю!"

                img 1085
                "Пожалуйста!"

                "Не надо!"

                "(плачет)"

                img 1087
                m "..."

                "Моя бедная девочка."

                "Не думай что я такой же злой работодатель как и все."

                "Напротив, я очень добрая."

                "Я оказываю тебе безмерное доверие."

                "Я разрешаю тебе оттереть это пятно до завтрашнего дня."

                "Если ты этого не сделаешь, то я уволю тебя с неустойкой."

                "Тебе понято?"

                img 1088
                julia "Да, Миссис Бакфетт."

                "Мне понятно."

                "(хмык)"

                img 1089
                m "Вот и славно."

                "Не подведи мое доверие, девочка."

                julia "(хмык)"

                "Я не подведу Вас, Миссис Бакфетт."

                m "Надеюсь ты ценишь мою доброту, Юлия."

                img 1090
                julia "Я очень ценю Вашу доброту, Миссис Бакфетт."

                "Спасибо Вам."

            "Я знаю что его не оттереть, я не буду заставлять тебя это делать.":
#                call bitch(-10, "monica_julia_revenge_punished") from _call_bitch_18
#                $ juliaPunished = False
#                $ juliaPunishedLow = True
#                $ juliaPunishedVoluntarily = False
#                $ juliaLocation = "floor1"
                img 1089
                m "Деточка, я знаю что это пятно не оттереть."
                "Я могла бы заставить тебя и ты бы стала пытаться это делать, верно?"

                img 1083
                julia "Конечно, Миссис Бакфетт!"
                "Если бы Вы приказали, я бы сделала все что в моих силах!"

                img 1089
                m "Но я не буду заставлять тебя это делать, хотя ты и заслуживаешь хорошего наказания."
                m "Надеюсь ты ценишь мою доброту, Юлия."
                img 1090
                julia "Я очень ценю Вашу доброту, Миссис Бакфетт."
                "Спасибо Вам."
    if julia_monica_revenge_undo_in_progress == True:
        img 1080
        with fade
#        call bitch(-15, "monica_julia_revenge_punished") from _call_bitch_19
        m "Вот!"
        "Посмотри что я нечаянно сделала."

        julia "Аххххх!!!"
        img 1083
        julia "Миссис Бакфетт, пожалуйста!"

        "Это пятно так просто не оттереть."

        "Этому ковру нужна химчистка!"

        img 1089
        m "Я знаю, Юлия."
        "Это моя вина."

        "Я все-равно собиралась выкидывать этот ковер, так что не стоит переживать."

        img 1083
        julia "Миссис Бакфетт!"
        "Я бы могла попытаться оттереть это пятно."
        "Это может занять много времени, но вы так добры ко мне, что я хотела бы вам помочь."
        "Я могу заниматься этим пятном по утрам, пока Вы спите."
        "Я могу это делать тихо, чтобы не беспокоить Вас."

        menu:
            "Да, Юлия, попытайся его оттереть в свободное время.":
#                call bitch(5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_20
#                $ juliaPunished = False
#                $ juliaPunishedLow = False
#                $ juliaPunishedVoluntarily = True
#                $ juliaLocation = "floor1"
                img 1089
                m "Да, Юлия, попытайся его оттереть в свободное время."
                "Но не слишком усердствуй, ты и так очень устаешь."
                img 1083
                julia "Хорошо, Миссис Бакфетт."
                "Я займусь им в свободное время."

            "Нет, Юлия. Не стоит пытаться сделать невозможную работу.":
#                call bitch(-5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_21
#                $ juliaPunished = False
#                $ juliaPunishedLow = False
#                $ juliaPunishedVoluntarily = False
#                $ juliaPunishedNone = True
#                $ juliaLocation = "floor1"
                img 1089
                m "Нет, Юлия. Не стоит пытаться сделать невозможную работу."
                "Я не садист."
                img 1083
                julia "Как скажете, Миссис Бакфетт."

#    $ julia_monica_revenge_in_progress = False
#    $ julia_monica_revenge_undo_in_progress = False
#    $ subst_to_object("Teleport_Street", False)
#    $ scene_transition = "Fade"
#    call refresh_scene() from _call_refresh_scene_2
    return

label gallery_1105:
#    $ houseStreetFenceLocationOpened = True
#    m "Позови его сюда.
#    Быстро."

#    fred "Одну минуту, Мэм!"
    music casualMusic
    #neighbor
    img 4260
    with fadehold
    w
    img 4261
    w
    img 4262
    w
    img 4263
    w
    img 4264
    neighbor "Вау...!"

    img 1099
    with fade
    neighbor "Здравствуйте, Мэм!"

    "Я Ваш сосед."
    "Я..."

    menu:
        "Мне без разницы кто он. Очередной тупица.":
#            $ neighborOffended1 = True
#            call bitch(2, "neighbor_dial1") from _call_bitch_2
            m "Я вижу что сосед."

            "Как вы объясните то что произошло?"

        "Поздороваться вежливо, все-таки он мой сосед.":
#            call bitch(-2, "neighbor_dial1") from _call_bitch_3
#            $ neighborOffended1 = False
            m "Добрый день.
            Будем знакомы, я Моника."
            "Так что же случилось с утра?"

    neighbor "Видите-ли, дело в том что я с утра решил покосить траву в своем дворе."

    "Все было хорошо, но между домом и забором с Вашей стороны очень тесно."

    "Я пробовал аккуратно стричь газон, но газонокосилка зацепила за забор и взлетела."

    "Она чуть не убила меня!"

    "Я чуть не погиб!"

    menu:
        "Мне нет дела до того погиб-бы ты или нет, придурок!":
#            $ neighborOffended2 = True
#            call bitch(2, "neighbor_dial2") from _call_bitch_4
            img 1100
            m "Меня не волнует состояние вашей жизни."

            "Покажите где это случилось."

        "Он был в опасности, это стоит сострадания.":
#            $ neighborOffended2 = False
#            call bitch(-2, "neighbor_dial2") from _call_bitch_5
            m "Ничего себе, вам повезло что Вы остались живы!"
            "Я рада что Вы целы!"
            img 1101
            neighbor "Эммм...
            Спасибо, Мэм."
            m "Покажите, пожалуйста, где это случилось?"

    img 1101
    neighbor "Сейчас я Вам покажу."

    "Удобнее будет с Вашей стороны двора."

    menu:
        "Решили потоптать в моем дворе?":
#            $ neighborOffended3 = True
#            call bitch(2, "neighbor_dial3") from _call_bitch_6
            img 1102
            m "Решили потоптать в моем дворе?"

            "Или заляпать мне все своими грязными ботинками?"

            img 1103
            w
            img 4265
            neighbor "Вау...!"

            img 1103
            neighbor "Но мэм! У меня чистные ботинки."

            img 1104
            m "У вас грязные ботинки."

            "Да вы и сами грязный. Фу."

            "Показывайте мне быстрее где это случилось."

            img 1105
            neighbor "Пойдемте, мэм, я покажу."


        "Раз удобнее с моей стороны двора, то пойдемте посмотрим с ней.":
#            $ neighborOffended3 = False
#            call bitch(-2, "neighbor_dial3") from _call_bitch_7
            img 1097
            m "Хорошо, если так удобнее, то пойдемте."

    img 1106
    with fade
    neighbor "Смотрите, Мэм."

    "Тут всего-лишь маленькая царапинка."
    img 1107
    w

    menu:
        "Ох ничего себе! Он сломал мне забор!":
#            $ neighborOffended4 = True
#            call bitch(5, "neighbor_dial4") from _call_bitch_8
#            jump neighbor_quest1_3
            img 1108
            m "Ох ничего себе!"

            "Маленькая царапинка!"

            "Вы хоть знаете сколько стоит этот забор?"

            img 1109
            neighbor "Да, мэм, но его можно починить."

            "Это совсем не сложно."

            img 1110
            m "У меня был забор."

            "Мне он очень нравился."

            "Мне не так-то много вещей вообще может понравиться."

            "Но этот забор был той вещью, которая мне пришлась по душе."

            img 1111
            "И вы лишили меня этой вещи."

            img 1112
            neighbor "Но мэм!"
            "Его же можно починить."
            "Тут дел на 5 минут!"

            img 1113
            m "Если его починить, то это все-равно уже будет не тот забор, который мне нравился."

            menu:
                "Закатить соседу иск.":
#                    $ neighborOffended5 = False
#                    $ neighborOffendedSue = True
                    label gallery_1115:

                    m "Вы отобрали у меня мою вещь."

                    "Я считаю что пострадала."

                    "Меня устроит комненсация в размере ..."
                    menu:
                        "$50.000":
#                            $ neighborOffendedSueBig = True
#                            call bitch(10, "neighbor_suebig") from _call_bitch_10
                            m "Меня устроит комненсация в размере $50.000."

                            "Сюда я включаю ремонт забора и моральный ущерб."

                            "Если моральный ущерб вообще можно оценить."

                            img 1114
                            neighbor "Сколько???"

                            "Мэм!"

                            "Вы в своем уме?"

                            "За какую-то царапину такие деньги!"

                            img 1115
                            m "Что?"

                            "Вы еще и употребили некорректное выражение в мой адрес?"

                            "Теперь ущерб составляет $100.000."

                            "Я сегодня же свяжусь со своим адвокатом."

                            "Его зовут Дик.
                            Думаю вы слышали про него."

                            "Он закатит вам иск, гораздо превышающий мое условие."

                            "И победит."

                            img 1116
                            neighbor "Дик Адвокат?"

                            "О нет!"

                            "Я знаю этого человека, Он акула-людоед."

                            "Он вытряхивает из людей все до последнего цента."
                            m "..."

                            img 1117
                            neighbor "Мэм!"

                            "Я прошу Вас!"

                            "У меня и так много долгов."

        #                    if neighborOffendedSueBig == False:
        #                        "Может быть вы просто простите мне эту оплошность?"

                            "Банк уже собирается описывать часть моего имущества, включая мою ферму через дорогу."

                            menu:
                                "Так эта вонючая ферма через дорогу принадлежит вам?":
        #                            call bitch(3, "neighbor_offendfarm") from _call_bitch_11
        #                            $ neighborOffendedFarm = True
                                    img 1118
                                    m "Так эта вонючая ферма через дорогу принадлежит вам?"

                                    "Мне все не доходили руки заняться ей."

                                    "Она портит мне вид из окна."

                                    "И я уверена, что если подойти к ней, то она будет вонять."

                                    "А меня это не устраивает."

                                    img 1119
                                    neighbor "Мэм."

                                    "Это мое хобби."

                                    "Там нет ничего такого что бы могло портить окружающую среду."

                                    img 1120
                                    m "Она выглядит некрасиво, этого достаточно."

                                "Какая еще ферма? Что с деньгами?":
        #                            $ neighborOffendedFarm = False
                                    img 1108
                                    m "Какая еще ферма?"
                                    "Что по поводу компенсации ущерба??"


        #                    if neighborOffendedSueBig == True:
                            img 1121
                            neighbor "Но Мэм!"

                            "Прошу Вас!"

                            "У меня и так много долгов."

                            "Ваш иск просто сломает мне жизнь!!"
                            "Прошу Вас."

                            "Умоляю!"

                            "Не делайте этого!"

                            img 1122
                            m "После того как Дик оставит вас без штанов, я надеюсь вы уберетесь отсюда со своей фермой."

                            m "И я больше никогда не увижу ваше лицо."

        #                    if neighborOffendedSueBig == False:


                        "$500":
#                            $ neighborOffendedSueBig = False
                            m "$500.
                            Буду честна, эта царапина больше не стоит."
                            img 1116
                            neighbor "Хмммм...
                            Мэм, спасибо!"
                            "Это достаточно небольшая сумма, но...."
                            m "..."

                            img 1117
                            neighbor "Мэм!"

                            "Я прошу Вас!"

                            "У меня и так много долгов."

                            #if neighborOffendedSueBig == False:
                            "Может быть вы просто простите мне эту оплошность?"

                            "Банк уже собирается описывать часть моего имущества, включая мою ферму через дорогу."

                            menu:
                                "Так эта вонючая ферма через дорогу принадлежит вам?":
        #                            call bitch(3, "neighbor_offendfarm") from _call_bitch_11
        #                            $ neighborOffendedFarm = True
                                    img 1118
                                    m "Так эта вонючая ферма через дорогу принадлежит вам?"

                                    "Мне все не доходили руки заняться ей."

                                    "Она портит мне вид из окна."

                                    "И я уверена, что если подойти к ней, то она будет вонять."

                                    "А меня это не устраивает."

                                    img 1119
                                    neighbor "Мэм."

                                    "Это мое хобби."

                                    "Там нет ничего такого что бы могло портить окружающую среду."

                                    img 1120
                                    m "Она выглядит некрасиво, этого достаточно."

                                "Какая еще ферма? Что с деньгами?":
        #                            $ neighborOffendedFarm = False
                                    img 1108
                                    m "Какая еще ферма?"
                                    "Что по поводу компенсации ущерба??"
                            img 1121
                            neighbor "Мэм.
                            Я постараюсь компенсировать эту сумму как можно скорее."
                            "Я отдам ее в течении недели!"

                            img 1122
                            m "Если в течении недели денег не будет, то вы заплатите сумму большую в 10 раз."
                            "Мой адвокат позаботится об этом."

                    m "И это считайте что я очень добрая."

                    img 1123
                    m "Люди часто не ценят мою доброту и потом об этом жалеют."

                    img 1122
                    m "А сейчас покиньте мою собственность, иначе я вызову полицию."

                    img 1124
                    m "Грязный бомж."
                    w
                    return

                "Прогнать этого идиота":
#                    $ neighborOffended5 = True
                    img 1124
                    m "Так что проваливайте отсюда, пока я не разозлилась по настоящему!"
                    m "Грязный бомж."
                    return

        "Эту царапину еле видно! Из-за чего весь шум?":
#            $ neighborOffended4 = False
#            call bitch(-5, "neighbor_dial4") from _call_bitch_9
            img 1113
            m "И это все?"
            "Из-за этого был весь шум?"
            neighbor "Да, Мэм!"
            "Это всего-лишь царапина, как я и говорил!"
            "Можно я пойду?"
            img 1113
            "Хорошо, идите.
            У меня и так много дел."
            img 1119
            neighbor "До свидания, Мэм.
            Простите что так вышло..."
            return

label gallery_1446:
#    if obj_data["action"] == "l":
#        $ img_num = renpy.random.randint(1,4)
#        if img_num == 1:
#            img 1446
#        if img_num == 2:
#            img 1483
#        if img_num == 3:
#            img 1940
#        if img_num == 4:
#            img 3395
#            img 3396
#        mt "Я считаю что эта гувернантка недостаточно старается."
#        mt "Бесполезное создание...
#        Фи..."

#    if obj_data["action"] == "t":
#        if day ==1 and day_time == "evening":
#            jump julia_punished_talk_day1_evening
#        if day == 2 and day_time == "day":
#            jump julia_punished_talk_day2_day
#        if day == 2 and day_time == "evening":
#            jump julia_punished_talk_day2_evening
#        if day == 3 and day_time == "day":
#            jump julia_punished_talk_day3_day
    sound snd_scrub
    img 3395
    w
    img 3396
    w
    img 1446
    w
    stop sound

    img 1450
    julia "Миссис Бакфетт!"

    "Я ототру это пятно."

    "Я не подведу Ваше доверие."

    "Обещаю!"

    "Пожалуйста!"

    sound snd_scrub
    return

label gallery_1486:
#    if monicaEated == True:
#        if businessCloth2NotFoundDay2 == True:
#            music Groove2_85
#            img 1496
#            m "Деточка."
#            stop sound fadeout 1.0
#            img 1497
#            julia "Да, миссис Бакфетт?"
#            img 1498
#            m "Где мой бизнес наряд?"
#            "Отвечай очень осторожно."
#            "А не то ты вылетишь прямо сейчас!"
#            img 1497
#            julia "Миссис Бакфетт!"
#            "Он готов!"
#            "Я в 4 утра занималась им!"
#            "Он постиран."
#            "Поглажен."
#            "Надушен всеми освежителями для гардероба!"
#            "Он благоухает и готов для того чтобы Вы его одели."
#            img 1499
#            "На свое восхитительное тело!"
#            img 1500
#            m "Я и так знаю что у меня красивое тело."
#            img 1501
#            "Нет нужды постоянно подчеркивать это."
#            julia "Да, миссис Бакфетт."
#            "Я поняла."
#            m "Принеси мне его в шкаф."
#            julia "Одну секунду, миссис Бакфетт!"
#            sound highheels_run1
#            img black_screen
#            with fadelong
#            img 1502
#            with fade
#            julia "Миссис Бакфетт."
#            "Ваш наряд в шкафу."
#            img 1503
#            m "Хорошо, деточка."
#            "Продолжай работать."
#            img 1504
#            julia "Хорошо, миссис Бакфетт."
#            "Спасибо!"

#            $ remove_objective("ask_julia_businesscloth2")
#            music Mandeville
#            $ businessCloth2NotFoundDay2 = False
#            $ businessCloth2FoundedDay2 = True
#            call refresh_scene_fade() from _call_refresh_scene_fade_111
#            return
#        img 1505
#        with fade
#        julia "Миссис Бакфетт!"

#        "Я ототру это пятно."

#        "Я не подведу Ваше доверие."

#        "Обещаю!"

#        "Пожалуйста!"
#        return
    music Stealth_Groover
    img 1483
    w
    img 1484
    m "ЮЛИЯ!!"
    julia "Да, Миссис Бакфетт?"
    "хмык..."
    img 1485
    m "ЧТО С ПЯТНОМ?"
    img 1486
    julia "Миссис Бакфетт!"
    "Я терла его всю ночь!"
    "Оно стало меньше."
    "Пожалуйста!"
    "хмык..."
    "Миссис Бакфетт!"
    "Умоляю!"
    "Дайте мне еще один день!"
    "хмык..."
    img 1487
    "Я все сделаю!"
    "Я оправдаю Ваше доверие, Миссис Бакфетт!"
    "хмык..."
#    label julia_punished_talk_day2_day_menu_loop1:
    menu:
#        "Уволить эту сучку прямо сейчас! (disabled)":
#            jump julia_punished_talk_day2_day_menu_loop1
        "Помучать эту сучку еще один день...":
            img 1488
            mt "Хммм..."
            "Я решила уволить ее завтра."
            "Почему-бы и не дать ей этот день."
            "Ну раз уж она так хочет оттереть это пятно."
            "Это у нее сейчас прямо цель в жизни."
            img 1489
            "Какие-то глупые люди."
            "С глупыми целями."
            img 1490
            "Эх."
            "Как тяжело с ними таким как Я."

            img 1491
            m "Хорошо, деточка."
            "Я разрешаю тебе тереть до завтрашнего утра."
#            call bitch(5, "day2dayMonicaJuliaPunishment") from _call_bitch_115
            "Если завтра с утра будет хоть что-то заметно, то ты уволена максимально жестко."
            img 1492
            "Ты поняла меня?"
            img 1493
            julia "Да, Миссис Бакфетт!"
            "Я поняла!"
            "Спасибо Вам!"
            "Спасибо большое!"
            "хмык..."
            img 1494
            m "А сейчас деточка."
            "Я хочу видеть еду на столе."
            "Ты ведь не забыла про свои обязанности?"
            "Правда?"

            img 1495
            julia "Одну минуту, Миссис Бакфетт."
            "Все готово!"
        "Простить ее...":
#            $ juliaMonicaForgivenessAfterPunishment = True
            img 1488
            mt "Хммм..."
            "Может мне простить ее?"
            img 1489
            mt "Она действительно старается стереть это пятно..."
#            if juliaMonicaLied == True:
#                mt "Пятно, которое я же и поставила, но обвинила ее в этом..."
            img 1490
            mt "Но я ведь ни какая-нибудь сучка и ни тиран!"
            img 1491
            m "Юлия, я считаю что ты не справишься с этим пятном..."
            img 1493
            julia "Миссис Бакфетт! Я справлюсь!"
            "Не увольняйте меня, пожалуйста!!!"
            img 1494
            m "Деточка, я не буду увольнять тебя.
            Пока..."
            "А сейчас быстро встань."
            img 1503
            julia "Миссис... Бакфетт..."
            "хмык..."
            "Вы правда не будете меня увольнять?"
            "хмык..."
#            if bitchmeterValue > maxBitchness / 2:
#                bitchmeterValue = maxBitchness / 2
#            call bitch(-20, "juliaMonicaForgivenessAfterPunishment") from _call_bitch_116
#            $ juliaMonicaForgivenessAfterPunishment = True
            m "Нет..."
            julia "А как-же пятно?"
            m "Можешь убирать его... В свободное время..."
            "Если оно у тебя бывает..."
            "..."
            m "А сейчас деточка."
            "Пока я не передумала"
            "Я хочу видеть еду на столе."
            "Ты ведь не забыла про свои обязанности?"
            "Правда?"
            img 1504
            julia "Одну минуту, Миссис Бакфетт."
            "Все готово!"


#    music Mandeville
#    $ juliaPunishedChecked = True
#    $ juliaLocation = "kitchen"
#    $ remove_objective("julia_check_spot")
    sound highheels_run1
#    call refresh_scene_fade() from _call_refresh_scene_fade_112
    show screen notify (_("Юлия убежала на кухню."))
    return

label gallery_1946:
#    if cloth_type == "BusinessCloth":
#        imgc Dial_Monica_BusinessCloth2_Thinking
#        mt "Я только с улицы."
#        "Сначала надо переодеться."
#        return

#    if monicaEated == True:
#        stop sound fadeout 1.0
#        img 1958
#        with fade
#        julia "Миссис Бакфетт!"
#        "Я ототру это пятно."
#        "Я не подведу Ваше доверие."
#        "Обещаю!"
#        "Пожалуйста!"
#        call refresh_scene_fade() from _call_refresh_scene_fade_113
#        return

    music Stealth_Groover
    img 1937
    with fadelong
    w
    img 1938
    with fade
    w
    img 1939
    with fade
    w
    img 1940
    with fade
    w
    img 1941
    with fade
    w
    stop sound fadeout 1.0
    julia "Добрый вечер, Миссис Бакфетт!"
    "Пятно уже стало меньше!"
    m "Ах, оно все еще есть?"
    "Как жаль."
    "У тебя же было время только до вечера, детка?"
    "Значит все?"
    img 1942
    julia "Миссис Бакфетт!"
    "Вы же обещали что у меня время до завтра!"
    "У меня есть еще одна ночь впереди!"
    "Пожалуйста!"
    "(хмык)"
    img 1943
    m "Я помню, детка."
    "Я пошутила."
    "У тебя совершенно нет чувства юмора."
    "..."
    img 1944
    "Или ты считаешь что это у меня нет чувства юмора, Юлия?"
    img 1945
    julia "Что Вы, Миссис Бакфетт!"
    "У Вас очень хорошее чувство юмора!"
    "Оно очень тонкое и изысканное!"
    img 1946
    "Как Вы сама!"

    img 1947
    m "Вот."
    "То-то же."
    "..."
    img 1948
    "Юлия?"
    julia "Да, Миссис Бакфетт?"
    img 1949
    m "Юлия."
    "Может быть ты устала?"
    "Все-таки ты не спала больше суток."
    img 1950
    "И собираешься не спать еще ночь?"
    "Может быть передохнешь?"

    img 1951
    julia "Миссис Бакфетт!"
    "Спасибо за заботу."

    img 1952
    "Но мне очень нужно оттереть это пятно до завтра!"

    img 1953
    m "Хорошо, детка."
    "Я стараюсь о тебе заботиться, но я не буду препятствовать твоим желаниям."

    img 1954
    "Я же хорошая?"

    img 1955
    julia "Вы очень хорошая, Миссис Бакфетт!"
    img 1956
    m "Хорошо."
    "А сейчас приготовь ужин."
    "Потом можешь продолжать."

    img 1957
    julia "Одну минуту, Миссис Бакфетт!"
#    $ juliaLocation = "kitchen"
    sound highheels_run1
#    call refresh_scene_fade() from _call_refresh_scene_fade_114
    show screen notify (_("Юлия убежала на кухню."))
#    music Mandeville
    return

label gallery_2000:
#    if monicaEated == True:
#        stop sound fadeout 1.0
#        img 1958
#        with fade
#        julia "Миссис Бакфетт!"
#        "Я ототру это пятно."
#        "Я не подведу Ваше доверие."
#        "Обещаю!"
#        "Пожалуйста!"
#        call refresh_scene_fade() from _call_refresh_scene_fade_115
#        return
#    if juliaFirePlanned == False:
#        img 1994
#        with fade
#        w
#        img 1995
#        w
#        img 1996
#        m "Юлия!"
#        img 2006
#        with fade
#        julia "Ой!"
#        "Миссис Бакфетт!"
#        "Это Вы?"

#        "Я ототру это пятно до утра, обещаю!"
#        img 2007
#        m "Уже утро, деточка!"
#        img 2008
#        julia "Как?"

#        "Как же так?"

#        "Этого не может быть!"

#        "(хмык)"
#        img 2009
#        julia "Миссис Бакфетт!!! Умоляю ВАС!!!"
#        "Дайте мне еще немного времени!"
#        "Еще чуть-чуть!!!"
#        "(хмык)"
#        img 2010
#        with fade
#        m "Тебе повезло, Юлия!"
#        "У меня сегодня хорошее настроение. Поэтому я решила пожалеть тебя."
#        img 2008
#        m "До завтрашнего дня, не более!"
#        if fredFirePlanned == True:
#            m "А вот Фреду сегодня не повезло, так что цени свое везение, деточка!"
#        img 2010
#        m "А теперь беги с сделай мне завтрак, пока я не передумала!"
#        julia "Да, Миссис Бакфетт! Я уже бегу!!!"

#        $ juliaLocation = "kitchen"
#        sound highheels_run1
#        call refresh_scene_fade() from _call_refresh_scene_fade_116
#        show screen notify (_("Юлия убежала на кухню."))
#        music Cheery_Monday
#        return
    music Pyro_Flow
    img 1994
    with fade
    w
    img 1995
    w
    img 1996
    w
    img 1998
    w
    img 1999
    w
    stop sound fadeout 1.0
    img 2000
    with fade
    w
    stop music fadeout 1.0
    img 2001
    with fade
    w
    img 2002
    with fade
    sound snd_bodyfall
    w
    img 2003
    w
    img 2004
    music Pyro_Flow
    m "Привет, дорогуша."

    img 2005
    with fade
    julia "Ой!"
    "Миссис Бакфетт!"
    "Это Вы?"

    img 2006
    "Я ототру это пятно до утра, обещаю!"

    img 2007
    m "Уже утро, деточка!"

    img 2008
    julia "Как?"

    "Как же так?"

    img 2009
    "Этого не может быть!"

    "(хмык)"

    img 2010
    m "Ты уволена, детка."
    "Тебе по почте придет уведомление о сумме неустойки."

    img 2011
    "Собирай свои вещи и чтобы через 15 минут тебя не было."

    "ЯСНО??"

    img 2012
    julia "Миссис Бакфетт!"

    "(хмык)"

    "Пожалуйста!"

    "(хмык)"

    "Не делайте этого!"

    "У моей семьи много долгов!"

    "Если вы меня уволите, то моей семье будет нечего есть!"

    "Пожалуйста!"

    "(хмык)"

    img 2013
    m "Ой."

    "Еще одна зануда про еду и долги."

    "Мне скучно."

    "Я все сказала тебе."

    "Если я тебя увижу через 15 минут, то вызову полицию."

    "Ты меня хорошо слышишь, деточка?"

    img 2014
    julia "Да, Миссис Бакфетт..."

    "(хмык)"

    "Я пошла..."

    img 2015
    m "Стой."

    "Я совсем забыла."

    "Ты пойдешь после того как приготовишь мне завтрак."

    img 2016
    "То что ты уволена, не освобождает тебя от обязанности прислуживать мне."

    img 2017
    "Быстро приготовь мне и проваливай отсюда."

    img 2018
    julia "Хорошо, Миссис Бакфетт..."
#    $ juliaLocation = "kitchen"
    sound highheels_run1

    img 2019
    with fadelong
    show screen notify (_("Юлия убежала на кухню."))
    mt "Пятно так и осталось."
    "Нерадивые сотрудники вечно оставляют за собой недоделанную работу."

    "Пятно придется оттирать следующей гувернантке."

    img 2020
    "С удовольствием поиграю с ней как с Юлией."

    "Это пятно - отличная идея."

    "С помощью него я поднимаю настроение каждое утро!"

    "Хи-хи"

#    call refresh_scene_fade() from _call_refresh_scene_fade_117
#    music Cheery_Monday
    return

label gallery_2026:
#    if juliaFirePlanned == True:
    music Cheery_Monday
    img 2021
    with fadelong
    m "Юлия! Можешь подавать еду!"
    img 2022
    "В последний раз."

    img 2023
    julia "Я все несу..."
    "(хмык)"
    sound highheels_run1
    img 2024
    with fade
    julia "Пожалуйста, Миссис Бакфетт."
    "(хмык)"

    img 2025
    "Приятного аппетита!"
    "(хмык)"

    img 2026
    m "Ты свободна."

    julia "Миссис Бакфетт..."

    "Может быть Вы передумаете?"

    menu:
        "Вон отсюда, малявка!":
            music Pyro_Flow
            img 2027
            with fade
            m "НЕТ!"
#            call bitch(5, "julia_firing") from _call_bitch_137
            "Вон отсюда, малявка!"

            img 2028
            w
            sound highheels_run1
#            $ juliaLocation = "none"
#            $ remove_objective("fire_julia")

            img 2029
            with fadelong
            show screen notify (_("Юлия расплакалась и убежала."))
            music Cheery_Monday
            mt "Я поела."
            "Вечером мне уже будет готовить другая служанка."
            "Уверена что будет гораздо вкуснее."
            "Предвкушаю вечерний ужин."
            "Мммммм..."
        "Пожалеть Юлию...":
#            $ juliaFirePlanned = False
#            $ juliaFireCancelled = True
            img 2029
            with fade
            m "Хорошо, Юлия."
            "Так уж и быть."
#            call bitch(-3, "julia_firing") from _call_bitch_138
            "Я разрешаю тебе тереть пятно еще до завтрашнего утра."
            img 2026
            "А сейчас брысь отсюда, пока я не передумала!"
            img 2025
            julia "Спасибо, Миссис Бакфетт!"
            "Спасибо ВАМ!!!"
#            $ juliaLocation = "floor2"
            sound highheels_run1
            show screen notify (_("Юлия убежала тереть пятно."))

#    $ monicaEated = True
#    $ remove_objective("eat")
#    call refresh_scene_fade() from _call_refresh_scene_fade_194
    return

label gallery_4009:
    call textonblack(_("ТЕМ ВРЕМЕНЕМ..."))
    img black_screen
    with Dissolve(1)
    #juliaNeedToCheckStreet
    #juliaHasSexInPool
#    $ scene_transition = "Fade"
#    call refresh_scene()
#    return
    music Groove2_85

    if juliaNeedToCheckStreet == True:
        img 4001
        julia "Мистер Фрэд!
        Наконец-то я нашла Вас!"
        img 4002
        "Что вы здесь делаете?
        Вы же должны быть на улице, ждать Миссис Бакфетт!"

        img 4003
        fred "Юлия, ты знаешь, я профессионал.
        Я всегда буду вовремя."
    else:
        img 4004
        julia "Мистер Фрэд!
        Что вы здесь делаете?"
        img 4003
        fred "Привет, Юлия...
        А что ты здесь делаешь?"
        img 4005
        julia "Я пришла чтобы заняться вещами Миссис Бакфетт.
        Я иду в прачечную."

    img 4006
    fred "Юлия...
    Ты помнишь про условия сделки?"

    img 4007
    julia "Ккккакой сделки...
    Ммииситер Фред..."

    img 4008
    fred "О сделке, которую мы заключили, когда я устроил вас на работу сюда."
    "Это ведь я порекомендовал вас Миссис Бакфетт.
    Вы бы никогда не попали сюда."
    "Ведь у вас нет хорошоего резюме и..."

    music Hidden_Agenda
    img 4009
    julia "Мистер Фред... Вы про это..."

    img 4010
    fred "Да, Юлия.
    И я пришел сюда получить то о чем мы договорились тогда."

    img 4011
    julia "Мистер Фред, я была в таком состоянии..."
    "Мне так нужна была эта работа...
    Я была готова на все, лишь бы попасть сюда."
    img 4012
    "И я согласилась на то что вы предложили, но...
    если честно, я думала что это какая-то шутка."
    img 4013
    "Ведь вы не будете требовать этого от меня, правда?"

    img 4014
    fred "Юлия, я устроил вас сюда, потому что вы представились как профессионал."
    "У вас нет резюме и я поверил вам на слово. Я поверил вам что вы профессионал."

    img 4015
    "Несоблюдение сделки - это непрофессионально."
    "Миссис Бакфетт не нужны непрофессионалы на работе!"

    img 4016
    julia "Мистер Фред, но ведь Миссис Бакфетт не в курсе этого!
    А если она узнает?"
    img 4017
    fred "Миссис Бакфетт вообще нет дела до этого!"
    "Она не вдается в проблемы таких как вы, Юлия.
    Ей достаточно мнения профессионала о вас, такого как я."

    music Power_Bots_loop
    img 4018
    "И этого хватит чтобы вас уволить.
    Вы ведь этого хотите?"

    img 4019
    w
    img 4018
    w
    img 4020
    julia "Мистер Фред, нет!
    Пожалуйста!"
    img 4021
    "Для меня потеря этой работы - это как конец света!!"

    img 4022
    fred "Я рад, Юлия, что ты понимаешь это."

    music Hidden_Agenda
    img 4023
    julia "Что мне надо сделать, Мистер Фред?"

    img 4024
    fred "Снимай одежду и иди ко мне..."

    img 4025
    menu:
        "Подчиниться Мистеру Фреду, у меня нет выхода.":
            img 4029
            julia "Хорошо, Мистер Фред."
            img 4030
            julia "Хмык"

            fred "..."
            fred "Ну?"
            img 4031
            music Groove2_85
            with fadelong
            sound snd_fabric1
            w
            img 4033
            jump gallery_julia_scene_basement1_1

        "Отказать ему, он требует невозможного.":
            music Groove2_85
            img 4026
            julia "Мистер Фред!"
            img 4027
            "Вы требуете невозможного, мне надо подумать."
#            julia "Мистер Фред, вы требуете невозможного, мне надо подумать."

            img 4028
            fred "Думайте, Юлия, у вас есть немного времени."
            "Но потом не жалуйтесь на проблемы, которые у вас могут возникнуть."
            "А сейчас идемте со мной, мне надо кое-что показать вам."
            sound highheels_run1
#    $ scene_transition = "Fade"
#    $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
#    music casualMusic
#    call refresh_scene() from _call_refresh_scene_24

    label gallery_julia_scene_basement1_1:
#    $ juliaBasementSceneStage = 1
#    $ juliaBasementWarningActive = True
#    $ juliaHasSexInPool = True
    img 4034
    w
    julia "Что дальше, Мистер Фред?"

    img 4033
    sound snd_fabric1
    fred "Дальше?"

    img 4035
    fred "Вот что дальше!"
    img 4036
    sound snd_julia_scream1
    julia "АХХХХХ!!"
    img 4037
    julia "О БОЖЕ!!!"
    img 4036
    fred "Садись на колени и возьми мой член в ротик."
    menu:
        "У меня нет выхода...":
            label gallery_4047:
#            $ juliaBasementSceneStage = 2
            img 4039
            with fadelong
            w
            img 4040
            julia "Какой он огромный..."
            img 4041
            julia "Мистер Фред!
            Я не могу его взять его, он слишком большой... наверное..."
            fred "Юлия!
            Не испытывай моего терпения!
            Быстро возьми его, иначе наша сделка разорвана!"
            sound snd_gulp
            julia "..."
            "Хорошо, Мистер Фред..."
            img 4042
            with fade
        #    sound snd_gag10
            w
            stop music fadeout 1.0
        #    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob1.mp4", loops=-1)
        #    $ renpy.scene()
            scene black
        #    show black_screen
            image videoBasement_Fred_Julia_Blowjob1 = Movie(play="video/Basement_Fred_Julia_Blowjob1.mp4", fps=30)
        #    pause 0.5
            show videoBasement_Fred_Julia_Blowjob1
        #    hide black_screen
            wclean
        #    sound snd_gag9
            img 4043
            with fade
            w
            img 4044
            music Groove2_85
            julia "Мммхмммпфффф...."
            fred "Продолжай, Юлия..."
            stop music fadeout 1.0
            scene black
            image videoBasement_Fred_Julia_Blowjob2 = Movie(play="video/Basement_Fred_Julia_Blowjob2.mp4", fps=30)
            show videoBasement_Fred_Julia_Blowjob2
            wclean
        #    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob2.mp4", loops=-1)
        #    sound snd_gag9
            img 4045
            with fade
            music Groove2_85
            w
            img 4046
            julia "Мммхмммпфффф...."
            img 4047
            fred "Продолжай..."
            stop music fadeout 1.0
            scene black
            image videoBasement_Fred_Julia_Blowjob3 = Movie(play="video/Basement_Fred_Julia_Blowjob3.mp4", fps=30)
            show videoBasement_Fred_Julia_Blowjob3
            wclean
        #    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob3.mp4", loops=-1)
            img 4048
            with fade
            music Groove2_85
            w
            img 4049
            fred "Продолжай..."
            img 4050
            w
            stop music fadeout 1.0
            scene black
            image videoBasement_Fred_Julia_Blowjob5 = Movie(play="video/Basement_Fred_Julia_Blowjob5.mp4", fps=30)
            show videoBasement_Fred_Julia_Blowjob5
            wclean
            img 4051
            w
            stop music fadeout 1.0
            scene black
            image videoBasement_Fred_Julia_Blowjob4 = Movie(play="video/Basement_Fred_Julia_Blowjob4.mp4", fps=30)
            show videoBasement_Fred_Julia_Blowjob4
            wclean
        #    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob4.mp4", loops=-1)
        #    sound snd_fred_argh
            img 4052
            music Groove2_85
            fred "ААААРГХХХХ!!!"
            julia "О БОЖЕ!!!"
            img 4053
            fred "ХА-ХААА!!!"
        #    sound snd_fred_argh
            img 4054
            fred "ААААРГХХХХ!!!"
            img 4055
            with fade
            fred "Не переживай, Юлия..."
            img 4056
            fred "Это полезно для кожи лица!"
            img 4057
            with fade
            fred "Можешь вставать, Юлия."
            img 4058
            fred "Как ты себя чувствуешь?"
            img 4059
            menu:
                "Я даже не знаю, Мистер Фред. Вы сделали со мной такие вещи...":
                    img 4060
                    julia "Я даже не знаю, Мистер Фред. Вы сделали со мной такие вещи..."
                    "Я могу идти?"
                    label gallery_4090:
#                    $ juliaBasementSceneStage = 3
                    img 4063
                    fred "Юлия, задержись еще на минутку..."
                    julia "Мистер Фред, но зачем?"
                    img 4064
                    sound snd_julia_scream1
                    fred "Вот зачем!!!"
                    img 4065
                    julia "АХХХХХ!!"
                    img 4066
                    julia "Что вы делаете???"
                    fred "Снимаю с вас трусики, Юлия!
                    Могли бы помочь мне!"
                    img 4067
                    julia "Но зачем?
                    Вы же уже кончили!"
                    "У Вас же уже не стоит!"
                    img 4068
                    fred "Как это не стоит?
                    А это что??!"
                    img 4069
                    julia "АХХХХХ!!"
                    img 4070
                    fred "Видишь?
                    Он уже снова готов!"
                    img 4071
                    julia "Как он так быстро?
                    Не могу поверить!"
                    img 4072
                    julia "Что вы хотите, Мистер Фред?
                    Чтобы я снова глотала его?"
                    img 4073
                    fred "Юлия, у меня идея получше!
                    Я ведь вижу что он понравился вам!"
                    julia "Но Мистер Фред!"
                    img 4074
                    fred "Юлия! Иди ко мне моя девочка..."
                    img 4075
                    julia "АХХХХХ!!"
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Teasing1_1 = Movie(play="video/Basement_Fred_Julia_Teasing1_1.mp4", fps=30)
                    show videoBasement_Fred_Julia_Teasing1_1
                    w
                    img 4076
                    music Groove2_85
                    julia "Мистер Фред...
                    ну хватит, пожалуйста..."
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Teasing1_2 = Movie(play="video/Basement_Fred_Julia_Teasing1_2.mp4", fps=30)
                    show videoBasement_Fred_Julia_Teasing1_2
                    julia "АХХХХХ!!"
                    w
                    img 4077
                    w
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Teasing1_3 = Movie(play="video/Basement_Fred_Julia_Teasing1_3.mp4", fps=30)
                    show videoBasement_Fred_Julia_Teasing1_3
                    w
                    img 4078
                    w
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Teasing2_1 = Movie(play="video/Basement_Fred_Julia_Teasing2_1.mp4", fps=30)
                    show videoBasement_Fred_Julia_Teasing2_1
                    w
                    img 4079
                    w
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Teasing2_2 = Movie(play="video/Basement_Fred_Julia_Teasing2_2.mp4", fps=30)
                    show videoBasement_Fred_Julia_Teasing2_2
                    w
                    img 4080
                    w
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Teasing2_3 = Movie(play="video/Basement_Fred_Julia_Teasing2_3.mp4", fps=30)
                    show videoBasement_Fred_Julia_Teasing2_3
                    w
                    img 4081
                    music Groove2_85
                    fred "Юлия, развернись-ка!"
                    img 4082
                    julia "Мистер Фред, но зачем?"
                    img 4083
                    fred "Вот зачем, Юлия!
                    Ха-ха!"
                    img 4084
                    sound snd_julia_scream1
                    w
                    img 4085
                    julia "АХХХХХ!!"
                    img 4086
                    julia "Что Вы сделали, Мистер Фред?"
                    img 4087
                    "И что Вы собираетесь делать?"
                    img 4088
                    fred "Вот что, Юлия!
                    Ха-ха!"
                    w
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_1 = Movie(play="video/Basement_Fred_Julia_Sex_1_1.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_1
                    julia "АХХХХХ!!"
                    wclean
                    img 4089
                    w
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_2 = Movie(play="video/Basement_Fred_Julia_Sex_1_2.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_2
                    wclean
                    img 4090
                    music Groove2_85
                    julia "Мистер Фред, что вы делаете?.."
                    w
                    img 4091
                    julia "АХХХХХ!!"
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_3 = Movie(play="video/Basement_Fred_Julia_Sex_1_3.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_3
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_3
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_4 = Movie(play="video/Basement_Fred_Julia_Sex_1_4.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_4
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_4
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_5 = Movie(play="video/Basement_Fred_Julia_Sex_1_5.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_5
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_5
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_6 = Movie(play="video/Basement_Fred_Julia_Sex_1_6.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_6
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_6
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_7 = Movie(play="video/Basement_Fred_Julia_Sex_1_7.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_7
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_7
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_8 = Movie(play="video/Basement_Fred_Julia_Sex_1_8.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_8
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_8
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_9 = Movie(play="video/Basement_Fred_Julia_Sex_1_9.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_9
                    wclean
                    hide videoBasement_Fred_Julia_Sex1_9
                    stop music fadeout 1.0
                    scene black
                    image videoBasement_Fred_Julia_Sex1_10 = Movie(play="video/Basement_Fred_Julia_Sex_1_10.mp4", fps=30)
                    show videoBasement_Fred_Julia_Sex1_10
                    wclean
                    img 4092
                    w
                    img 4093
                    fred "ХА-ХА!"
                    img 4094
                    julia "АХХХХХ!!"
                    img 4095
                    w
                    img 4096
                    w
                    img 4097
                    w
                    img 4098
                    w

#                    $ scene_transition = "Fade"
#                    $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
#                    music casualMusic
#                    call refresh_scene() from _call_refresh_scene_38

#                    return

                    label gallery_4112:
                    sound highheels_short_walk

                    img 4099
                    music Indo_Rock
                    with fadelong
                    w
                    img 4100
                    julia "АХХХХХ!!"
                    img 4101
                    fred "Еще немного, Юлия!
                    Я почти закончил!"
                    img 4102
                    julia "АХХХХХ!!"
                    img 4103
                    w
                    img 4104
                    julia "Очень глубоко, Фред!"
                    img 4105
                    fred "Мистер Фред!"
                    img 4106
                    julia "Мистер Фред!"
                    img 4107
                    julia "АХХХХХ!!"
                    img 4108
                    julia "ААААА.. АААААААААА..."
                    img 4109
                    julia "МММММММММФФФФФФ...."
                    img 4110
                    julia "АХХХХХ!!"
                    img 4111
                #    sound snd_fred_argh
                    fred "ААААРГХХХХ!!!"
                    img 4112
                    w
                    img 4113
                    julia "АХХХХХ!!"
                    img 4114
                    music Groove2_85
                    fred "Поздравляю, Юлия.
                    Наша сделка закрыта."
                    img 4115
                    w
                    img 4116
                    fred "Вы проявили себя как профессионал, поздравляю вас."
                    img 4117
                    fred "Вы отлично умеете справляться с профессиональными обязанностями!"
                    img 4118
                    fred "Можете вставать."
                    img 4119
                    with fade
                    w
                    img 4120
                    fred "А у вас красивая фигура!"
                    img 4121
                    fred "Юлия, я уверен что вам понравилось!"
                    img 4122
                    fred "Ведь это так?"
                    img 4123
                    julia "Мистер Фред, Я..."
                    "Я..."
                    menu:
                        "Мистер Фред, я не знаю что вам ответить...":
#                            $ juliaBasementSexLiked = True
                            julia "Мистер Фред, я не знаю что вам ответить..."
                            img 4124
                            fred "Юлия, вы в порядке?"
                            img 4125
                            julia "Да, Мистер Фред.
                            Я в порядке..."
                            img 4129
                            julia "Мистер Фред...
                            Что это он делает?
                            Снова встает??!?!?"
                            img 4130
                            fred "Да, Юлия.
                            Вы ему очень понравились.
                            Пожалуй, он хочет еще разок, ложитесь на пол."

                        "Да как вы посмели!!!":
                            img 4126
                            julia "МНЕ??? ПОНРАВИЛОСЬ???
                            Да как вы посмели!!!"
                            img 4127
                            julia "Я - бедная девушка!
                            Поверила ВАМ!!"
                            img 4128
                            julia "Посмотрите что теперь со мной!"
                            img 4129
                            julia "Постойте!"
                            "Что это он делает?
                            Снова встает??!?!?"
                            img 4130
                            fred "Да, Юлия.
                            Его очень возбуждает когда вы ругаетесь."
                            "Он вас сразу начинает хотеть.
                            Ложитесь на пол, скорее!"


#                    $ juliaBasementSceneStage = 4
                    sound highheels_short_walk
#                    $ juliaBasementWarningActive = False
                    img black_screen
                    with fadelong
                    img 4131
                    julia "О БОЖЕ!!!"
                    "Там кто-то идет!"
                    "Наверное это Миссис Бакфетт!"
                    img 4132
                    fred "Идем, Юлия.
                    Здесь есть другой выход на улицу."
                    img 4133
                    w
                    sound highheels_run1
#                    music casualMusic
#                    $ scene_sound = False
#                    $ scene_transition = "Fade_long"
#                    call refresh_scene() from _call_refresh_scene_39

                "Это отвратительно!!!":
                    img 4061
                    julia "Это отвратительно!!!"
                    "Вы кажетесь приличным человеком!
                    Я не думала что вы на такое способны!!!"
#                    sound highheels_run1
#                    $ juliaBasementWarningActive = False

#            $ scene_transition = "Fade"
#            $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
#            music casualMusic
#            call refresh_scene() from _call_refresh_scene_25
            return

        "Я не буду делать этого! (убежать)":
            img 4038
            julia "Я не буду этого делать!"
            sound highheels_run1
#            $ juliaBasementWarningActive = False
#            $ scene_transition = "Fade"
#            $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
#            music casualMusic
#            call refresh_scene() from _call_refresh_scene_37
            return
    #секс в бассейне в подвале
    return

label gallery_4692:
    music Mandeville
    img 1458
    with fade
    m "Юлия!"
    img 1459
    "Можешь подавать еду!"
    julia "Да, Миссис Бакфетт, одну секунду!"
    sound highheels_run1
    img 1460
    with fadelong
    julia "Пожалуйста, Миссис Бакфетт."
    "Приятного аппетита!"
    m "..."
    m "Юлия?"
    m "Да, миссис Бакфетт?"
    img 1461
#            if juliaPunishedLow == True:
#                m "Если я не заставила тебя убирать пятно, то это не значит что у тебя нет других обязанностей!"
#                "Ты уже все сделала по дому?"
#                img 1462
#                julia "Еще нет..."
#                "..."
#                julia "Слушаюсь, миссис Бакфетт!"
#                $ monicaEated = True
#                $ remove_objective("eat")
#                $ juliaLocation = "floor1"
#                sound highheels_run1
#                show screen notify (_("Юлия убежала выполнять обязанности."))
#                call refresh_scene_fade() from _call_refresh_scene_fade_181
#                return
#            if juliaPunishedVoluntarily == True:
    m "Спасибо за еду.
    Ты свободна."
    img 4692
    julia "Миссис Бакфетт, рада служить Вам!"
#    $ monicaEated = True
#    $ remove_objective("eat")
#    $ juliaLocation = "floor1"
    sound highheels_run1
#    call refresh_scene_fade() from _call_refresh_scene_fade_183
    return

label gallery_5075:
    music Loved_up2
    img 5059
    with fadelong
    w
    img 5060
    with fade
    w
    img 5061
    w
    img 5062
    w
    img 5063
    fred "О! Какой вид!"
    img 5064
    with fade
    w
    sound snd_fabric1
    img 5065
    with fadelong
    w
    img 5067
    with fade
    w
    sound snd_fabric1
    img 5068
    julia "Мистер Фред, это ВЫ???"
    img 5069
    w
    #юлия трет пятно
    #фред снимает штаны
    #фред спускает трусы юлии
    #юлия в шоке смотрит вперед стоя на четвереньках
    img 5070
    "Что вы делаете???"
    img 5071
    w
    img 5072
    w
#    sound snd_fabric1
    sound Jump2
    img 5073
    with fadelong
    fred "Я помогаю вам справиться с пятном, Юлия!"
    img 5074
    julia "Таким образом???"
    img 5075
    fred "Да, Юлия! Вы, как профессионал, должны понимать связь между моими действиями."
    img 5076
    "Вы проявляете себя как профессионал, а я сообщаю об этом Миссис Бакфетт!"
    menu:
        "Вы правда попросите ее не увольнять меня?":
            img 5077
            with fade
            julia "Вы правда попросите ее не увольнять меня?"
            #начинается секс
            img 5078
            fred "Я считаю что не стоит увольнять профессиональных сотрудников!"
#            stop music fadeout 1.0
            scene black
            image videovJulia_Fred_Sex_1_1 = Movie(play="video/vJulia_Fred_Sex_1_1.mp4", fps=30)
            show videovJulia_Fred_Sex_1_1
            wclean
            #секс
            img vJulia_Fred_Sex_1_2_00
            fred "По тому как вы стараетесь, я могу сделать вывод о вашей настойчивости в достижении целей."
            scene black
            image videovJulia_Fred_Sex_1_2 = Movie(play="video/vJulia_Fred_Sex_1_2.mp4", fps=30)
            show videovJulia_Fred_Sex_1_2
            wclean
            #секс
            img vJulia_Fred_Sex_1_3_00
            fred "Это хорошее качество. И оно должно быть оценено по достоинству вашим начальством."
            scene black
            image videovJulia_Fred_Sex_1_3 = Movie(play="video/vJulia_Fred_Sex_1_3.mp4", fps=30)
            show videovJulia_Fred_Sex_1_3
            wclean
            scene black
            image videovJulia_Fred_Sex_1_4 = Movie(play="video/vJulia_Fred_Sex_1_4.mp4", fps=30)
            show videovJulia_Fred_Sex_1_4
            wclean
            #секс
            img 5079
            fred "Я также являюсь вашим начальством, поэтому и надо доказывать свой профессионализм мне."
            scene black
            image videovJulia_Fred_Sex_1_5 = Movie(play="video/vJulia_Fred_Sex_1_5.mp4", fps=30)
            show videovJulia_Fred_Sex_1_5
            wclean
            scene black
            image videovJulia_Fred_Sex_1_6 = Movie(play="video/vJulia_Fred_Sex_1_6.mp4", fps=30)
            show videovJulia_Fred_Sex_1_6
            wclean
            #секс
            img 5080
            fred "Ааааррргххххх...."
            music Groove2_85
            img 5081
            julia "Мистер Фред! Вы кончили прямо на пятно на ковре!"

            img 5082
            with fadelong
            fred "Вы убедили меня в том что не стоит мешать вам достигать своей цели."
            img 5083
            "Вы можете рассчитывать что я не буду настаивать на вашем увольнении при разговоре с Миссис Бакфетт."
            #юлия испуганно косится на фреда
            img 5084
            julia "Не будете настаивать чтобы меня увольнять? А как же помощь???"
            img 5085
            fred "К сожалению, я пока еще не все решаю здесь."
            img 5086
            "Но поверьте, вы уже добились очень многого в моих глазах."
            img 5085
            "Продолжайте работу, Юлия. Желаю вам удачи."
            img 5086
            "Сегодня вы уже не понадобитесь мне..."
            julia "..." #смотрит с обидой

        "Нет, Мистер Фред! Здесь нет никакой связи!":
            #юлия вскакивает
            music Groove2_85
            img 5087
            with fadelong
            julia "Нет, Мистер Фред! Здесь нет никакой связи!"
            "Позвольте мне продолжить выполнять мои прямые профессиональные обязанности!"
            #фред улыбается
            fred "Хорошо, Юлия. Как скажете..."
    #фред присовывает
    return

label gallery_5589:
#    if homeVisited == True:
#        mt "Мне лучше не приближаться к своему дому."
#        "Иначе меня заберет полиция!!!"
#        return

    # охранник
    music Power_Bots_Loop
    sound dogs_barking
    img 5588
    with fadelong
    house_guard "Мэм!"
    "Это частная собственность!"
    "Вы не имеет права здесь находиться!"
    img 5589
    m "Да!"
    "Это частная собственность!"
    "И она моя!"
    "А ты кто такой вообще?"
    "Дай пройти!"
    img 5590
    house_guard "Мэм."
    "Я еще раз повторяю что это частная собственность."
    m "Это мой дом!"
    "Пусти меня!"
    img 5591
    house_guard "Нет, Мэм."
    "Это дом Мистера Робертса."
    "Он меня нанял."
    "Я не знаю кто Вы."
    "Меня никто не предупреждал."
    img 5592
    m "Это не его дом!"
    "Его захватили нечестным путем!"
    "Это мой дом!"
    "МОЙ!!!"
    img 5593
    house_guard "Мэм."
    "Пожалуйста, сделайте несколько шагов назад."
    m "ПРОПУСТИ МЕНЯ!!!"
    img 5594
    house_guard "Мэм."
    "Я сейчас вызову полицию!"
    m "ПУСТИ МЕНЯ!!!"
    "ЭТО МОЙ ДОМ!!!"
    "ААААААААА!!!"
    img 5595
    house_guard "Мэм."
    "Я вызываю патруль."

    img black_screen
    with Dissolve(1)
    sound snd_phone1
    $ renpy.pause(2.0)

    img 5596
    with fadelong
    policeman "Полиция слушает."
    house_guard "Сэр!"
    "Это звонят с западной окраины города."
    "Я охранник частного дома."
    "Тут какая-то ненормальная пытается незаконно проникнуть на территорию."
    "Мне кажется она наркоманка."
    "Ведет себя неадекватно."
    "Пожалуйста, пришлите патруль!"
    policeman "Хорошо, сэр."
    "Патруль выезжает."
    img 5597
    mt "..."
    "О БОЖЕ!!!"
    "СЮДА ЕДЕТ ПОЛИЦИЯ!!!"
    img 5598
    "МНЕ НАДО СКОРЕЕ УБИРАТЬСЯ ОТСЮДА!!!"
    "ИНАЧЕ КОНЕЦ!!!"
#    $ homeVisited = True
#    $ remove_objective("home_visit")
#    $ autorun_to_object("street_house_outside", "after_jail_house_outside2")
#    if dickSearch == True and homeVisited == True and hotelVisited == True:
#        $ s2ClothShopStage = 1

#    call refresh_scene_fade() from _call_refresh_scene_fade_93

    return

label gallery_3337:
    music RnB4_100
    img 3336
    with fadelong
    mt "Моника!"
    "Моника!"
    "Ты дома!"
    "Да!"
    "Пусть все совсем не так как ты хотела!"
    "Но ты снова под этой крышей!"
    img 3337
    "Жизнь, кажется, начинает налаживаться."
    "Ну хоть чуть-чуть!"
    img 3338
    "Мне сейчас надо переодеться."
    "Принять ванну."
    "Плотно покушать."
    "Как я хочу нормально наесться наконец!"
    "И идти ложиться спать."

    img 3339
    "Наверняка хозяева заняли мою спальню."
    "Еще какую-то комнату занял мальчик."

    img 3340
    "Остается еще спальня для гостей!"
    "Я наконец-то нормально высплюсь!"
    "В мягкой постели, приятно пахнущей ароматом лаванды!"
    "Моника!"
    "Я так за себя рада!"

#    music Groove2_85

#    $ add_objective("take_governess_cloth", _("Одеть униформу"), c_blue, 10)
#    $ add_objective("take_bath", _("Принять душ"), c_green, 11)
#    $ add_objective("to_eat", _("Поесть"), c_orange, 12)

#    $ monicaEated = False
#    $ bathTaken = False

#    $ autorun_to_object("bedroom_second", "afterJailHouse_dialogue2")
#    $ autorun_to_object("bedroom_bardie", "afterJailHouse_dialogue3")
#    $ autorun_to_object("living_room", "afterJailHouse_dialogue4")
#    $ autorun_to_object("bedroom1", "afterJailHouse_dialogue5")
#    $ autorun_to_object("kitchen", "afterJailHouse_dialogue6")
#    $ autorun_to_object("kitchen2", "afterJailHouse_dialogue6")
#    $ autorun_to_object("bathroom_bath", "afterJailHouse_dialogue7")

#    $ subst_to_object("Teleport_Kitchen", "afterJailHouse_dialogue1a")
#    $ subst_to_object("Teleport_Bedroom", "afterJailHouse_dialogue1a")

#    $ miniMapEnabledOnly = ["Bathroom", "Floor1", "Floor2", "Basement", "Street_Yard"]

#    $ autorun_to_object("floor1", "afterJailHouse_dialogue1b")

#    call refresh_scene_fade() from _call_refresh_scene_fade_129
    return

label gallery_3348: #bathroom forbid
    sound highheels_run2
    music Pyro_Flow
    img 3344
    with fadelong
    betty "Это что это ты собралась делать, дорогуша??"
    img 3346
    music Hidden_Agenda
    m "Миссис Робертс, я хотела принять ванну."
    mt "СВОЮ ВАННУ В СВОЕМ ДОМЕ!!!"
    "И Я НЕ ХОЧУ СПРАШИВАТЬ КАКИХ-ТО ЛЕВЫХ БАБ РАЗРЕШЕНИЯ НА ЭТО!!!"
    img 3347
    m "Простите, мне надо было спросить разрешения у Вас?"
    "Я заранее прошу прощения, Миссис Робертс."

    music Pyro_Flow
    img 3348
    betty "!!!"
    "Какое разрешение, детка???"
    "Ты что, собираешься мыть свое тело с такой жуткой фигурой в моей ванне?"
    "Или в моем душе?"
    "Твое дело - это убирать дом!"
    "А пользоваться удобствами - это привилегия хозяев!"
    img 3349
    "Скажи, ты здесь хозяйка?"
    mt "ДА ДА ДА, СУЧКА!!!"
    "Я ЗДЕСЬ ХОЗЯЙКА, А ТЫ НИКТО!!!"
    music Hidden_Agenda
    img 3350
    m "Нет, Миссис Робертс."
    "Здесь хозяйка Вы..."
    music Pyro_Flow
    betty "Тогда выйди отсюда и чтобы я тебя больше здесь не видела!"
    m "Да, Миссис Робертс. Прошу прощения."

#    $ monicaBathroomForbidden = True
#    $ remove_objective("take_bath")
#    $ bathTaken = True

#    music casualMusic

#    $ autorun_to_object("floor2", "afterJailHouse_dialogue11")

#    call change_scene("floor2") from _call_change_scene_226
    return

label gallery_3358:
    sound highheels_run2
    music Pyro_Flow
    img 3354
    with fadelong
    betty "Я не поняла!"
    "Что ты здесь делаешь???"
    music Hidden_Agenda
    img 3355
    with fade
    m "Мэм..."
    "Я зашла просто покушать..."
    img 3356
    "Вернее, простите, Мэм, я не так сказала."
    "Я хотела начать готовить ужин, чтобы Вы и Ваш муж и ребенок могли покушать перед сном."
    img 3358
    music Pyro_Flow
    betty "Детка!"
    "Запомни правило!"
    "В этом доме готовлю Я!"
    "Для своего мужа!"
    img 3359
    "И мне не нужно, чтобы в мою семью влезала какая-то проститутка!"
    "ЯСНО ТЕБЕ!!!"
    music Hidden_Agenda
    img 3360
    with fade
    m "Миссис Робертс.."
    "Я не имела ввиду.. Я просто..."
    music Pyro_Flow
    img 3361
    betty "Если я еще раз увижу тебя на кухне."
    "Или увижу что пропали хоть какие-то продукты..."
    img 3362
    with hpunch
    "Я тебя сразу уволю!"
    "Ты поняла?"
    img 3363
    m "Да, Миссис Робертс..."
    "Я поняла..."
    betty "Я буду проверять холодильник!"
    "И другие вещи в доме!"
    "Мебель, одежду, все!"
    "Я подозреваю что такая проститутка, как ты, может что-то украсть!"
    img 3364
    "А сейчас, пожалуйста, покинь кухню!"

#    $ remove_objective("to_eat")
#    $ monicaEated = True

#    $ monicaKitchenForbidden = True

#    $ autorun_to_object("floor1", "afterJailHouse_dialogue14")

#    music casualMusic

#    call change_scene("floor1") from _call_change_scene_227
    return

label gallery_3377:
    #render+
    #Моника в подвале
    music Power_Bots_Loop
    img 5795
#    imgl Dial_begin37_18
    with fadelong
    mt "Снова этот вонючий подвал..."
    "Я поклялась себе что никогда сюда не спущусь..."
    "Но что мне делать???"
    "Идти на улицу?"

    music As_long_as_a_word_remains_unspoken
    img 5796
#    imgl Dial_begin37_19
    mt "Моника!"
    "Как же тебя угораздило так влипнуть?"
    "Ты бродишь по подвалу в собственном доме..."
    "В поисках постели..."

#    call refresh_scene_fade() from _call_refresh_scene_fade_134

#    mt "Какой страшный корридор..."
#    "Мне нигде не найти спальню для прислуги."
#    "Там в конце есть какой-то свет."
#    "Может быть сходить проверить?"
#    return

#label afterJailHouse_dialogue19:
    img 3365
    with fadelong
    mt "Я не знаю куда ведет этот коридор."
#    img 3366
    img 5797
    mt "Он темный."
    "Я никогда по нему не ходила."
    "Может быть где-то там ночевала Юлия?"

#    $ autorun_to_object("basement_bedroom2", "afterJailHouse_dialogue20")
#    call afterJailHouse_dialogue20() from _call_afterJailHouse_dialogue20
#    return

#label afterJailHouse_dialogue20:
#    img black_screen
#    with Dissolve(1.0)
#    help "Вы можете безопасно сохраниться в этой локации для того, чтобы использовать сохранение в Эпизоде 2."
    img 3374
    with fadelong
    mt "Вот где жила Юлия..."
    img 3375
    with fade
    mt "Узкая темная каморка, без окон."
    mt "В то время пока я нежилась в постели из шелка..."
    img 3376
    with fade
    mt "..."
    "Там на столике что-то лежит..."

#    $ miniMapEnabledOnly = ["none"]


#    $ add_objective("take_journal", _("Там на столике что-то лежит..."), c_white, 15)

#    call refresh_scene_fade()
#    return

#label afterJailHouse_dialogue21:
#    $ basementBedroomJournal = False

#    sound snd_take_paper
    img 3378
    with fadelong
    mt "Это мой журнал."
    "Я на обложке."
    "Зачем он Юлии?"
    img 3377
    with fade
    mt "Наверное она смотрела на него и думала про меня."
    "Про ту кто живет наверху..."
    "..."
    img 3379
    with fade
    mt "Моника."
    "Что с тобой стало?"
    "..."
    "Не могу сейчас ни о чем думать."
    "Главное что я под крышей над головой, а не в ледяной камере или еще где похуже."
    "..."
    "Надо раздеться и ложиться спать..."

#    $ remove_objective("take_journal")
#    $ add_inventory("journal", 1, True)
#    $ basementBedroomStage = 1
#    $ autorun_to_object("basement_bedroom1", "afterJailHouse_dialogue22")

#    call change_scene("basement_bedroom2", "Fade", False) from _call_change_scene_228
    return

label gallery_5799:
#    if cloth != "Governess":
#        mt "Я не хочу разговаривать с ним в таком виде."
#        "Мне надо переодеться!"
#        return
    #render+
    #Моника говорит с Барди в его комнате
    music Hidden_Agenda
    img 5798
#    imgr Dial_Bardie_1
    bardie "Я тебя сюда устроил, помнишь?"
    "Ты мне должна!"
    img 5799
#    imgl Dial_begin37_2
    m "Я тебе ничего не должна, мальчик!"
    "Веди себя вежливо по отношению ко старшим!"

    music Power_Bots_Loop
    img 5800
#    imgr Dial_Bardie_2
    bardie "Ах ты так!"
    bardie_t "Ну она у меня попляшет!"

#    $ monicaBardieOffended1 = True

#    music casualMusic
    return

label gallery_5805:
#    $ ralphAskedAboutPayment = True
    #render
    #Моника спрашивает у Ральфа про деньги. Гостиная
    music Groove2_85
    img 5805
#    imgl Dial_begin37_13
    with fadelong
    m "Мистер Робертс."
    "Позвольте спросить?"

    img 5806
#    imgr Dial_Ralph_2
    ralph "Да, Моника, спрашивай."
    "Освоилась в доме?"
    img 5807
    m "Еще не до конца, Мистер Робертс."
    img 5808
    ralph "Осваивайся, удачи тебе!"
    img 5809
    m "Спасибо, Мистер Робертс. Можно вопрос?"
    ralph "Да?"
    img 5810
#    imgl Dial_begin37_14
    m "Мистер Робертс. Мне Ваша супруга только что сказала что я слишком дорого для Вас стою."
    "И что у меня зарплата $90 в час..."
    img 5811
    with fadelong
#    imgr Dial_Ralph_3
    ralph "..."
    "Хм..."
    "И что ты хочешь узнать?"
    img 5812
#    imgl Dial_begin37_15
    with fade
    m "Мистер Робертс."
    "Фред сказал мне что я буду работать за бесплатно."
    "И я хотела бы узнать..."
    img 5813
    ralph "Что бы ты хотела узнать, Моника?"
    img 5814
    m "..."
    img 5813
    "..."
    img 5814
    m "..."
    img 5815
#    imgr Dial_Ralph_4
    with fade
    ralph "Ладно."
    "Фред уговорил меня взять тебя."
    "Я не очень-то хотел."
    "Честно говоря, Бетти и сама хорошо справлялась с домом."
    "И нам не нужна была гувернантка."
    img 5816
    "Тем более что почти все наши деньги Бетти тратит на себя."
    "Так что то что она немного работает и приносит пользу - меня устраивало."
    "Фред предложил мне идею..."
    "В общем Бетти я сказал что буду платить тебе $90 в час."
    "Для того чтобы хоть какие-то деньги оставались при мне."
    img 5817
#    imgr Dial_Ralph_5
    ralph "Ну.. Ты понимаешь, Моника?"
    "Бетти такая строгая..."

    music Pyro_Flow
    img 5818
#    imgl Dial_begin37_16
    with hpunch
    mt "О! Я понимаю!"
    "Я понимаю, склизкий червяк!"
    img 5819
    "Что ты будешь забирать мои деньги себе и тратить на шлюх!"
    "Я прекрасно понимаю!"
    music Groove2_85
    img 5820
#    imgl Dial_begin37_17
    m "Да, Сэр. Я понимаю."
    img 5821
#    imgr Dial_Ralph_6
    with fade
    ralph "Если честно, я сам немного побаиваюсь этой авантюры."
    "Так что если ты не хочешь, то можешь не работать."
    "Хочешь я прямо сейчас скажу Бетти что ты уходишь?"
    img 5822
    m "Нет, Сэр."
    "Я буду работать."
    img 5823
    "..."
    "Сэр. Я Вам еще нужна?"
    img 5824
#    imgr Dial_Ralph_7
    ralph "Нет, Моника, можешь идти."
    m "До свидания, Мистер Робертс."
    img 5825
    with fade
    mt "..."
    mt "СВОЛОЧЬ!!!"

#    $ remove_objective("ask_ralph")

#    call refresh_scene_fade() from _call_refresh_scene_fade_128
    return

label gallery_1130:
#    call bitch(1, "fred_monica_office2") from _call_bitch_66
    sound snd_car_engine
    imgr 1128
    with fade
    fred "Куда мы направляемся, Мэм?"

    imgl 1129
    m "Надо же, удосужился спросить."

    "Едешь куда глаза глядят, как всегда."

    "Даже не знаешь куда."

    fred "Я еду и ожидаю Ваших распоряжений, Мэм."

    fred "Как я могу предположить, мы едем, как обычно, в фитнесс зал?"

    imgl 1130
    m "Ты не угадал на этот раз, Фред!"

    m "Мы не едем в фитнесс зал!"

    fred "Куда же мы едем, Мэм?"

    imgl 1131
    m "Мы едем в Офис."

    m "Из-за таких растяп как ты, я сегодня потратила много времени и уже опаздываю."

    m "Так что едь быстрее."

    imgr 1133
    fred "Я еду по правилам, Мэм!"

    imgl 1132
    m "Правила задаю Я!"

    "Запомни!"

    menu:
        "Продолжить задирать Фреда":
            jump gallery_drive_speak_monica_office_3
        "Молча ехать и смотреть инстаграм.":
            return

    label gallery_drive_speak_monica_office_3:
#    call bitch(1, "fred_monica_office3") from _call_bitch_67
    sound snd_car_engine
    imgl 1131
    with fade
    m "Да, кстати, Фред!"

    imgr 1133
    fred "Слушаю, Мэм."

    m "У меня сегодня встреча вечером."

    "Так что будь вовремя у моего офиса, ты понял??"

    fred "Мэм, я буду вовремя, как всегда!"

    imgl 1129
    m "Ты не всегда бываешь вовремя, Фрэд!"

    fred "Мэм, я ни разу не опаздывал к Вам."

    "Если Вы про тот случай, то я просто стоял чуть подальше чем обычно."

    "Так как рядом не было парковочных мест!"

    imgl 1131
    m "Я вышла.
    Тебя на месте не было."

    "Все просто!"

    imgr 1133
    fred "Я стараюсь, Мэм!"

    menu:
        "Продолжить задирать Фреда":
            jump gallery_drive_speak_monica_office_4
        "Молча ехать и смотреть инстаграм.":
            return

    label gallery_drive_speak_monica_office_4:
#    call bitch(1, "fred_monica_office4") from _call_bitch_68
    sound snd_car_engine
    imgr 1133
    with fadelong
    fred "Уже почти приехали, Мэм!"

    imgl 1127
    m "Помолчи.

    Ты меня уже утомил."

    imgr 1128
    with fadelong
    fred "Мэм, мы приехали."

    imgl 1130
    m "Мог бы ехать и побыстрее!"

    fred "Я старался, Мэм!"

    imgl 1132
    m "Плохо старался, Фред!"

    fred "Простите, Мэм."

    m "Жди меня здесь."

    fred "Конечно, Мэм!"
    return

label gallery_1674:
#    img 1649
#    w
#    $ add_objective("goto_bank1", _("Ехать в Банк по вопросу денег от Стива"), c_red, 20)
#    $ remove_objective("goto_bank1")
    music Stealth_Groover
    img 1650
    with fadelong
    bank_clerk "Добрый день, Мэм!"
    "Чем могу Вам помочь?"

    img 1651
    m "Здравствуйте."
    "Я пришла уточнить ньюансы по движению на моих счетах."

    img 1652
    bank_clerk "Да, пожалуйста."
    "Ваши документы."

    img 1653
    m "Пожалуйста, возьмите."
    bank_clerk "Спасибо."

    img 1654
    m "Вот здесь бумага на которой написаны интересующие меня реквизиты."

    img 1655
    bank_clerk "Спасибо."
    "Уточняю."
    "..."

    img 1656
    with fadelong
    bank_clerk "Извините, Мэм."
    "По данным реквизитам движения средств отсутствуют."

    img 1657
    m "То есть вы хотите сказать что никаких денег не поступало?"

    bank_clerk "Нет, Мэм."

    m "То есть это не ваша задержка, а мне не перечислили деньги?"

    bank_clerk "Движения средств не зарегистрированы, Мэм."

    img 1658
    with fade
    m "Значит этот мешок с дерьмом все-таки мне соврал..."

    img 1659
    bank_clerk "Простите, Мэм?"

    img 1660
    m "Я говорю почему эти данные не были предоставлены моему секретарю?"

    "Почему я должна ездить."

    "Тратить свое время?"

    img 1661
    m "СКАЖИТЕ МНЕ??"

    img 1662
    bank_clerk "Простите, Мэм."
    "На ваших сотрудников закончилась доверенность."
    "Вам необходимо оформить новую и..."
    menu:
        "ВЫ ОБНАГЛЕЛИ В КОНЕЦ!":
#            $ clerksOffended = True
            img 1663
            m "ЭТО НЕ ДОВЕРЕННОСТЬ ЗАКОНЧИЛАСЬ!"
#            call bitch(2, "bank_office1") from _call_bitch_91

            "ЭТО ВЫ ОБНАГЛЕЛИ В КОНЕЦ!"
            "Я держу свои деньги в вашем банке!"
            "А вы меня дурите какими-то доверенностями!"
            img 1664
            bank_clerk "Мэм, простите, но..."
            img 1665
            m "Никаких простите!"
            "Твое имя?"
            "БЫСТРО!"
            img 1666
            bank_clerk "Мэм, но..."
            img 1665
            m "БЫСТРО Я СКАЗАЛА!!"
            img 1667
            bank_clerk "Patricia Dolares, Мэм."
            img 1668
            m "Отлично, я запомню."
            "Я подам на тебя жалобу, Patricia."
            img 1669
            bank_clerk "Мэм, пожалуйста, не надо!"
            "Я работаю здесь недавно."
            "У меня будут проблемы из-за этого."
            img 1670
            m "Это даже лучше!"
            "Спасибо за информацию!"
            img 1671
            bank_clerk "Мне очень жаль, Мэм."
            img 1672
            m "Мне не жаль!"
            "До свидания!"
            img 1673
            bank_clerk "До свидания, Мэм..."
            img 1674
            w
#            $ autorun_to_object("bank_office", "bank_office_thinking1")

        "Я понимаю...":
            img 1669
            m "Ладно, я понимаю."
            "Это недосмотр кого-то из моего персонала."
            "Вы ни при чем."
            img 1652
            bank_clerk "Спасибо, Мэм!"
            "Я рада что Вы понимаете..."
            img 1669
            m "До свидания!"
            img 1652
            bank_clerk "До свидания, Мэм..."

#    music casualMusic
#    $ bankOfficeState = 2

#    $ add_objective("goto_office1", _("Ехать в Офис"), c_pink, 20)
#    $ drivingPlacePlannedArray["Steve_Office"] = "steve1_drive1"
#    $ focus_map("Teleport_Monica_Office", "steve1_drive1_discard_others")
#    $ mapSubstMonicaOfficeToSteve = True

#    $ unfocus_map()
#    call refresh_scene_fade() from _call_refresh_scene_fade_45
    return

label gallery_2052:
    img scene_Map
    music Walking_Sax2
    sound snd_car_engine
    imgl 2030
    with fadelong
    if fredOffendedDriveReturnDress1 == True:

        m "Едем в офис, Корнюшон."
        imgr 2031
        fred "..."
        imgr 2032
        "Да, Мэм."

        "Хорошо."

        "..."

    else:
        m "Едем в офис, Фред."
        imgr 2032
        "Да, Мэм."

        "Хорошо."



    sound snd_car_engine
    imgl 2033
    with fadelong
    if fredFirePlanned == True:
        mt "Надо сказать ему что он уволен."

        "Сказать сразу или поиграть?"

        "Надо поиграть, это же весело!"

        "..."

        imgl 2034
        m "Корнюшон."

        imgr 2031
        fred "..."

        imgr 2032
        "Да, Мэм."

        imgl 2035
        m "У меня есть монетка."

        "В конце рабочего дня я ее кину."
        "Если выпадет орел, то ты дальше работаешь."

        "Если решка, то ты уволен."

        imgl 2036
        mt "Выпадет решка."

        "А пока пусть надеется."

        fred "Мэм."

        "За что Вы хотите уволить меня?"

        imgl 2037
        m "Ты несоответствуешь требуемому профессиональному уровню."

        fred "Мэм."

        "У меня нет ни одной аварии."

        "Ни одного опоздания. Я всегда вовремя."

        imgl 2038
        m "У тебя нет керосина, Корнюшон!"

        fred "..."

        "Мэм."
        "Я профессионал."

        "Я найду другую работу."

        imgl 2039
        m "Ты не найдешь ее."

        imgl 2040
        "Я сделаю звонок в кадровое агентство, откуда тебя прислали."

        "Скажу чтобы ты больше не работал."

        "Как думаешь, послушают они меня?"

        "Я думаю да."

        "Я знаю волшебные слова."

        "Такие как я их знают."

        "Ты знаешь волшебные слова?"

        "Скажи какое-нибудь?"

        fred "Слово пожалуйста?"

        imgl 2041
        m "Нет, наивный."

        "Тебе не понять."

        imgl 2042
        "Так вот."

        "Твое агентство сообщит в другие агентства."

        "И так далее."

        fred "..."

        imgl 2043
        m "В общем ты понял."

        fred "..."

        m "Вечером твоя самая главная лотерея, Корнюшончик!"

        "Удача любит тебя, правда?"

        imgr 2031
        fred "Мэм..."


    #marcus
    imgl empty
    imgr empty
    with fadelong
    sound snd_phone_ring
    help "Телефонный звонок..."
    sound snd_phone_short_beeps
    $ renpy.pause(1.0)

    imgl 2044
    mt "Не успела взять."

    "Какой-то незнакомый номер."

    imgl 2045
    "Может быть это какой-нибудь поклонник?"

    "Очень интересно."

    imgl empty
    imgr empty

    $ renpy.pause(2.0)
    sound snd_phone_ring
    help "Телефонный звонок..."

    imgl 2046
    mt "Снова он!"

    sound snd_phone2
    imgl 2047
    marcus "Миссис Бакфетт?"

    m "Да, Сэр."

    "Я вас слушаю."

    imgl 2048
    "У вас такой приятный голос."

    "Что вы хотели от самой красивой девушки с обложки?"

    imgl 2049
    mt "Хи-хи."

    "Позаигрываю с ним."

    "Это интересно!"

    imgl 2048
    marcus "Мэм."

    "Вас беспокоит офицер Маркус."

    "Я из полиции."

    imgl 2050
    m "Фи!"

    "Мне не интересно!"

    "Я-то думала?"

    marcus "Простите, Мэм."

    "Можете уделить буквально минутку?"

    "Это важно."

    imgl 2051
    m "Ладно, уговорили."

    "Только за то что у вас был приятный голос вначале."

    "По крайней мере, мне так показалось."

    marcus "Хм.."

    "Миссис Бакфетт."

    "Могли бы Вы подъехать к нам в отделение полиции?"

    imgl 2052
    m "Нет."

    "Зачем мне это надо?"

    "У меня есть юристы, адвокаты."

    "Решайте вопросы с ними."

    "Вы хоть знаете кто Я?"

    marcus "Мэм."

    "Я понимаю."

    "Пожалуйста, простите меня."

    imgl 2053
    "Это не займет много времени."

    "Это чистая формальность."

    "Буквально на пять минут."

    "Это касается неоплаченных штрафов."

    m "Каких еще штрафов?"

    marcus "Штрафов за парковку, Мэм."

    imgl 2054
    m "И?"

    "Вы в своем уме?"

    "Я буду к вам ехать из-за каких-то штрафов?"

    "Да я вообще не вожу машину!"

    "У меня есть водитель!"

    marcus "Да, Мэм."

    "Я понимаю."

    "Но дело в том, что эти штрафы получены в таком месте."

    "Гхмм."

    "В общем это не совсем обычное место, Мэм."

    "Я подозреваю что Вы не были в курсе что Ваша машина находилась там."

    imgl 2055
    mt "Так-так."

    "Какие-то новые подробности про Фрэда?"

    "Это интересно."

    label gallery_police_phone_dialogue1_loop1:
    menu:
        "Почему бы не заехать?":
            pass
        "Я заеду в другое время, не сейчас. (Happy End)" if bitchmeterValue <= 153 and fireAmount == 0:
#            $ _dismiss_pause = False
            label gallery_4695:
            img scene_Map
            music Euro_Loop1
            imgl empty
            imgr empty
            imgc 2049
            with fadelong
            m "Мистер Маркус, я понимаю всю ответственность."
            "И, поверьте, я бы очень хотела заехать к Вам."
            "Но у меня сейчас много дел, много работы."
            "Можно-ли сделать это чуть позже?"
            "Еще я давно не видела мужа и хотела бы пообщаться с ним."
            "Вы понимаете меня, правда?"
            marcus "Гхмм. Мэм..."
            "Если честно, я не ожидал такого ответа."
            "У меня есть определенные инструкции на этот счет."
            "Пожалуйста, минуту, я вам перезвоню."
            m "Конечно, Мистер Маркус."
            "В любое время."
            marcus "Гхм. Спасибо..."
            sound snd_phone_short_beeps
            $ renpy.pause(2)
            sound snd_car_engine
            sound snd_phone_ring
            imgc 2048
            with fadelong
            $ renpy.pause(1)
            sound snd_phone2
            m "Да, Мистер Маркус?"
            marcus "Миссис Бакфетт..."
            "Я связался с моим куратором, очень влиятельным человеком."
            "Не знаю почему так произошло, но он сказал что видел вас где-то недавно."
            "И вы показались ему очень порядочной и доброй девушкой..."
            m "Конечно, Мистер Маркус."
            "Я добрая и порядочная девушка. Вы разве не знали?"
            marcus "Гхмм..."
            "Если честно, Миссис Бакфетт, я немного в растерянности."
            "Мне приказано закрыть дело о Ваших штрафах за парковку, Мэм."
            "Вы можете не приезжать."
            imgc 2049
            with fadelong
            m "О! Большое спасибо, Мистер Маркус!"
            "Если я понадоблюсь, вы всегда можете связаться со мной!"
            marcus "Гхмм... Спасибо, Миссис Бакфетт."
            "По всей видимости, этого не понадобится."
            "Хорошего Вам дня!"
            m "Вам тоже, Мистер Маркус!"
            sound snd_phone_short_beeps
            $ renpy.pause(1)
            sound snd_phone_ring
            imgc 2048
            with fadelong
            $ renpy.pause(1)
            sound snd_phone2
            m "Да, дорогой!"
            "Я тебя слушаю!"
            husband "Моника, любимая моя!"
            "Мне только что дали позвонить тебе!"
            "Ты не представляешь в какую ситуацию я попал!"
            "Но сейчас все хорошо, меня отпускают домой!"
            "Я скучаю по тебе, Моника!"
            m "Я тоже скучаю по тебе, любимый!"
            "Приезжай скорее!"
            img 4695
            with fadelong
            m "Фред, разворачивайся."
            "Я еду домой..."
        #    $ renpy.pause(17, hard=True)
            img img_happy_end
            with Dissolve(2)
            $ renpy.pause(3)
            define alpha_happy_end = AlphaDissolve("alpha_control", delay=12)
            scene white_screen
            with alpha_happy_end

            img 4696
            with fadelong
            $ renpy.pause(2)
            img img_happy_end2
            with Dissolve(3)
        #    $ renpy.pause(3, hard=True)
#            $ renpy.pause(100)
#            $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))

            return

        "Я заеду в другое время, не сейчас. (Happy End, Моника недостаточно добрая) (disabled)" if bitchmeterValue >= 600 or fireAmount > 0:
            jump gallery_police_phone_dialogue1_loop1

    imgl 2056
    mt "Почему бы не заехать?"

    "Всего пять минут он говорит?"

    "Тем более это по пути."

    "Всего пять минут, но какие новые карты я могу получить для игры с ним!"

    imgl 2057
    mt "Время есть до самого вечера, когда я уволю его."

    "И это время надо провести интересно!"

    imgl 2058
    m "Хорошо, сэр."

    "Вы уговорили меня."

    "Я сейчас заеду к вам."

    imgl 2059
    m "Но если это займет больше пяти минут, то вы лишитесь работы."

    "Вам понятно?"

    imgl 2060
    marcus "Да, Мэм."

    "Конечно, я понимаю."

    "Простите меня еще раз."

    "Спасибо Вам что найдете время заехать."

    imgl 2061
    m "Считайте что я согласилась из-за того что хочу посмотреть на хозяина такого красивого голоса."

    marcus "Гхм. Мэм."

    "Спасибо."

    "Буду ждать Вас."

    imgl 2062
    m "До встречи."

    sound snd_phone_short_beeps

    $ renpy.pause(3)

    sound snd_car_engine
    imgl 2063
    m "Ну что, Корнюшон."

    "Вот ты и попался!"

    imgr 2032
    fred "Мэм."

    "Вы о чем?"

    m "Мне позвонили из полиции."

    "Скоро я узнаю о твоих темных делишках!"

    "Я знаю что мозгов у тебя нет."

    "Но мне даже интересно что же ты такого додумался натворить."

    fred "Мэм."

    "Я ничего не творил."

    "Я честно работаю у Вас."

    imgl 2064
    m "Хи-хи."

    "Скоро узнаем."

    imgl 2065
    mt "День становится все интереснее!"

    "Я в предвкушении!"

    "Мммммм..."
#    music Cheery_Monday
#    $ add_objective("go_to_police", _("Заехать по пути в полицию на 5 минут"), c_green, 30)
    return


label gallery_5748:
    music Groove2_85
    img 3092
    with fadelong
    m "Дик!"
    "Наконец-то я тебя увидела!"
    img 3093
    dick "Я тоже рад встрече, дорогая моя."
    "Как твои дела?"
    "Давненько я не видел тебя."
    "Не звонишь мне, не пишешь."
    img 3094
    "Я подумал ты про меня совсем забыла..."
    img 3095
    with fade
    music Power_Bots_Loop
    m "Дик!"
    "Я пришла к тебе не просто так!"
    "Со мной произошли невиданные, СОВЕРШЕННО НЕВИДАННЫЕ ВЕЩИ!"
    "Ты просто не представляешь!!!"
    img 3096
    dick "Что случилось, дорогая?"
    img 3097
    m "Меня продержали в тюрьме!"
    "Две недели!"
    "Ты представляешь, Дик!?"
    img 3098
    "МЕНЯ!!!"
    "В ТЮРЬМЕ!!!"
    img 3099
    "Мне угрожали какими-то немыслимыми, дикими вещами!"
    img 3100
    "Я чуть не сошла с ума там!"
    "..."
    "А после того как меня выпустили, я пошла домой."
    img 3101
    "Дик!"
    "Ты представляешь, в моем доме кто-то живет!!!"
    "Дик!!!"
    "ТЫ ПРЕДСТАВЛЯЕШЬ СЕБЕ???"
    img 3102
    music Groove2_85
    dick "Да, милая."
    "Я немного в курсе этих дел."
    "Мне очень жаль что все так вышло."
    img 3103
    music Pyro_Flow
    m "ТЕБЕ ЖАЛЬ???"
    "ДИК!"
    "Разберись с этим!"
    img 3104
    "НЕМЕДЛЕННО!"
    "И отвези меня домой!"
    img 3105
    m "ДИК!"
    "ТЫ МЕНЯ СЛЫШИШЬ?"
    "НЕМЕДЛЕННО!!!"
    "!!!!!!!!!"

    img 3106
    music Groove2_85
    dick "Милая Моника."
    "Видишь-ли, тут такое дело..."
    "В общем это все не просто какая-то ерунда."
    "Это действительно серьезные проблемы."
    "И так просто их не решить..."
    img 3107
    m "Что за проблемы?"
    "Я так ничего и не поняла, что случилось?"
    "В чем именно меня обвинили?"
    "НИ ЗА ЧТО!!!"
    img 3108
    dick "Видишь-ли, Моника."
    "Твой муж вляпался в очень крупное дело."
    "Это как-то связано с выборами."
    img 3109
    "А ты знаешь какие там ставки."
    img 3109
    "А он поставил не на того кандидата и в общем..."
    "Теперь он за это расплачивается."
    "У него появились очень могущественные враги."
    img 3110
    "И все твои проблемы связаны с этим..."
    img 3111
    m "Дик!"
    "А что с моим домом?"
    "Что с ним?"
    "Почему там живут другие люди?"
    img 3112
    dick "Видишь-ли, Моника."
    "Твой дом был записан на одну из твоих фирм."
    "Все твои фирмы так или иначе аффилированы с компанией моды, которая принадлежит тебе."
    "Принадлежала..."
    img 3113
    m "!!!!!!!!!!"
    img 3112
    dick "Все твое имущество было арестовано."
    "И компания перешла в управление других структур."
    "Дом также, получается, записан на компанию, поэтому новое руководство делает с ним все что сочтет нужным."
    "Они могут его продать, могут туда кого-то заселить."
    "В общем это уже их дело, а не наше."
    "Моника."
    "..."
    img 3114
    with fade
    m "!!!!!"
    "Дик!"
    "А что с моими документами?"
    "Мне сказали что я получила гражданство незаконно, но ведь у меня есть старое гражданство."
    "Мне сказали оно тоже недействительно."
    img 3115
    music Power_Bots_Loop
    m "Дик!"
    "Как же мне быть?"
    "У меня вообще нет никаких бумаг!"
    "Скажи что это все неправда, Дик!"
    "Скажи!"
    img 3116
    music Groove2_85
    dick "Моника."
    "Они сказали правду."
    "Ты действительно беспечно отнеслась к этому вопросу в свое время."
    "Мне очень жаль..."
    img 3117
#    music Pyro_Flow
    m "Дик!"
    "Скажи, ты ведь решишь с моими документами?"
    "Мне это надо уладить в первую очередь!"
    img 3118
    music Groove2_85
    dick "Да, конечно, милая."
    "Думаю я смогу восстановить твое старое гражданство."
    "Я задействовал кое-какие связи в твоей стране."
    "И, думаю, получится это сделать."
    img 3119
    m "Спасибо, Дик!"
    "Когда это будет улажено?"
    img 3120
    "Завтра?"
    img 3121
    music Power_Bots_Loop
    dick "Нет, милая."
    "Это может занять несколько месяцев."
    img 3122
    "А может и лет..."
    img 3123
    with hpunch
    m "ЧТО????"
    "КАК ТАКОЕ МОЖЕТ БЫТЬ???"
    img 3124
    dick "Я не пишу законы, Моника."
    "Я лишь нахожу лазейки в них."
    "Это все что я могу сделать для тебя."
    img 3125
    music Pyro_Flow

    menu:
        "ТЫ! ЖИРНЫЙ СЛИЗНЯК!":
#            $ dickMonicaCabinetOffended = True
            m "ЧТОООО?"
            "И ВСЕ???"
            "..."
            img 3126
            "ТЫ!"
            "ЖИРНЫЙ СЛИЗНЯК!"
            "ТЫ ВООБЩЕ НЕ ХОЧЕШЬ МНЕ ПОМОГАТЬ!!!"
            img 3127
            "ЖИРНЫЙ УРОД!!!"
            "...."
            img 3128
            "!!!!"
            img 3129
            music Groove2_85
            dick "Моника."
            img 3130
            "Пожалуйста, успокойся."
            img 3129
            music Power_Bots_Loop
            "Я понимаю твое состояние."
            "Однако я и так делаю все что в моих силах."
            img 3131
            "Не забывай."
            img 3132
            "Если бы не я, то ты бы не вышла из тюрьмы."
            img 3133
            dick "Я задействовал очень большие связи и много денег, чтобы это случилось."
            "А ты кричишь на меня."
            img 3134
            "Мне обидно, Моника."
            img 3135
            m "..."
            img 3136
            dick "..."
            img 3137
            m "..."
            img 3138
            music Hidden_Agenda
            m "Дик..."
            "Дик... В общем я.."

            img 3139
            "Я извиняюсь перед тобой что накричала."
            "Прости меня."
            "Ты правда очень много сделал."
            "Там был жуткий кошмар и я почти потеряла надежду."
            img 3140
            "Спасибо что вытащил меня."
            "..."
        "Дик, но как же так... Помоги мне, пожалуйста... хмык...":
#            $ dickMonicaCabinetOffended = False

            #debug
#            $ dickDriveDialOffend1 = True
#            $ richHotelRestaurantDickOffended1ChoiceMade = True
#            $ dickClothShopOffended1 = True
#            $ dickClothShopOffended2 = True
#            $ dickDriveRestaurantOffended1 = True
#            $ dickMonicaSaidToFredOffend = True
#            $ dickClothShopOffended4 = True
#            $ dickDriveDialOffend1 = False
#            $ richHotelRestaurantDickOffended1ChoiceMade = False
#            $ dickClothShopOffended1 = False
#            $ dickClothShopOffended2 = False
#            $ dickDriveRestaurantOffended1 = False
#            $ dickMonicaSaidToFredOffend = False
#            $ dickClothShopOffended4 = False
            label gallery_5695:
            music Hidden_Agenda

            #render+
            img 5694
            with fade
            m "Дик... но как же так..."
            "Ты ведь такой умный, ты самый умный человек, которого я знаю!"
            img 5695
            "Неужели ты не можешь ничего придумать?"
            if dickDriveDialOffend1 == True: #Я сегодня уже слышала это. И тот кто это сказал был болваном.
                show screen notify (_("Моника нагрубила Дику про погоду... (негатив)"))
#                $ dickSavesMonica = False
                img 5696
                dick "Раньше ты говорила по другому, Моника."
                "Ты называла меня болваном что бы я ни сказал. Даже про погоду..."
                img 5697
                m "Дик, я же просто шутила..."
            if richHotelRestaurantDickOffended1ChoiceMade == True: #Сказать Дику что он смешной. Ресторан
                show screen notify (_("Моника сказала в ресторане что Дик смешной... (негатив)"))
#                $ dickSavesMonica = False
                img 5698
                dick "Я смешной, Моника. Это твои слова."
                img 5699
                m "Ты не смешной, Дик. Ты очень умный..."

            if dickClothShopOffended1 == True and dickClothShopOffended2 == True: #ты уродливый и уродливый галстук
                show screen notify (_("Моника сказала в магазине что Дик уродливый... (негатив)"))
#                $ dickSavesMonica = False
                img 5700
                dick "К сожалению, Моника, ум - это не все что заставляет мужчину действовать ради женщины."
                img 5701
                m "А что же?"
                img 5702
                dick "Эмоции. Мужчина хочет нравиться женщине."
                img 5703
                m "Ты мне нравишься, Дик!"
                if dickClothShopOffended4 == True:
                    img 5704
                    dick "Нравлюсь как плюшевый мишка?"
                else:
                    img 5705
                    m "Ты мой кавалер. Помнишь я тебе говорила?"
                img 5706
                dick "Ты считаешь что я уродливый, Моника. И ты говорила мне это в лицо."
                img 5707
                "Это расстраивает меня."
            if dickDriveRestaurantOffended1 == True: #ты виноват что уже поздно, не отвез меня в нормальный магазин
                show screen notify (_("Моника сказала в машине что во всем виноват Дик... (негатив)"))
#                $ dickSavesMonica = False
                img 5708
                dick "Как бы я ни старался, я всегда останусь виноват у тебя."
                img 5709
                "Будь это юридическим делом, либо магазином одежды."
                img 5710
                "Тебе никогда ничего не нравится, Моника. Чем бы я ни занимался."
                img 5711
                m "Это не так, Дик!"
                "Мне очень нравится что ты занимаешься моим делом."

            if dickSavesMonica == True:
                if dickMonicaSaidToFredOffend == False: #Дик жирный урод!
                    #начинает играть музыка
                    img 5714
                    dick "Моника, я..."
#                    music living_the_daydream
                    music epicenters_eve
                    img 5715
                    m "Дик, ты знаешь..."
                    img 5716
                    "Да, у тебя не всегда получалось угодить мне."
                    img 5717
                    "Но я всегда знала что ты действительно меня любишь."
                    "Я даже другим людям говорила что ты хороший, Дик..."
                    img 5718
                    dick "Моника, это правда?"
                    img 5719
                    m "Да, Дик."
                    "Еще я была замужем и понимаю что никогда не любила своего мужа."
                    img 5720
                    dick "Ты и сейчас замужем."
                    img 5721
                    m "Можешь считать что нет. Мой муж дал на меня показания, чтобы выйти на свободу самому."
                    dick "Мерзавец..."
                    img 5722
                    m "Да, Дик. И, ты знаешь, я понимаю, что хоть у меня и было богатство, но настоящего мужчины рядом не было."
                    "Может быть потому я и была такой, как про меня многие думают."
                    img 5723
                    "Эта история открыла мне глаза на то как устроен мир."
                    img 5724
                    "И что в этом мире есть мужчина, который действительно заботится обо мне."
                    img 5725
                    dick "..."
                    img 5726
                    m "И этот мужчина ты, Дик..."
                    img 5727
                    dick "Моника, то есть ты согласна..."
                    img 5728
                    m "Да, Дик. Если вдруг ты собирался сделать мне предложение, то можешь это сделать сейчас."
                    "Мой ответ будет ДА..."
                    img 5729
                    dick "Моника, это меняет дело..."
                    img 5730
                    with fadelong
                    dick_secretary "Мистер Дик!"
                    "У меня есть срочный факс для вас!"
                    img 5731
                    dick "Виктория, подожди за дверью!"
                    img 5732
                    dick_secretary "Но мистер Дик!"
                    img 5733
                    dick "Я сказал подожди!!!"
                    img 5734
                    dick_secretary "..."
                    img 5735
                    with fadelong
                    dick "Моника, если ты будешь рядом со мной, то я стану гораздо сильнее."
                    img 5736
                    "Давай надерем задницу тем ублюдкам, кто посмел тронуть тебя."
                    img 5737
                    m "Давай, Дик!"
                    "Мы сделаем это вместе!"
                    # переход
                    # день свадьбы

                    stop music fadeout 1.0
                    call textonblack(_("Спустя некоторое время..."))
                    music tour_of_the_flowers
                    img black_screen
                    with Dissolve(1)
                    img 5745
                    with fadelong
                    dick "Дорогая!"
                    "Гости нас уже ждут в ресторане!"
                    "Там собралась куча влиятельных политиков и адвокатов..."
                    "Ты точно хочешь сделать эту фотосессию сейчас?"
                    "Может быть завтра?"
                    img 5746
                    m "Дик, милый."
                    img 5747
                    "Для меня это важно. Завтра выходит новая обложка и я хочу быть на ней."
                    img 5748
                    "Я обещала себе это. В самые трудные минуты своей жизни..."
                    img 5749
                    "Пожалуйста... Ты не против?"
                    dick "Хорошо, дорогая! Только скорее!"
                    img 5750
                    m "Алекс?"
                    alex_photograph "Да, Мэм?"
                    m "Ты мой самый лучший фотограф!"
                    "Сделай это красиво! Пожалуйста!"
                    img 5751
                    alex_photograph "Мэм! Вы так со мной вежливы!"
                    "Обещаю, это будет самая красивая фотосессия среди всех журналов, когда-либо видевших свет!"
                    img 5752
                    m "Хорошо, Алекс. Это хорошо."
                    img 5753
                    with fadelong
                    w
                    img 5754
                    call photoshop_flash()
                    w
                    img 5755
                    call photoshop_flash()
                    w
                    img 5756
                    call photoshop_flash()
                    w
                    img 5757
                    call photoshop_flash()
                    w
                    img 5758
                    call photoshop_flash()
                    w
                    img 5759
                    call photoshop_flash()
                    w
                    music beautiful_messenger_piano
                    img black_screen
                    with Dissolve(1.0)
                    img 5760
                    with fadelong
#                    call photoshop_flash()
                    alex_photograph "Мэм! Я отснял достаточно материала!"
                    "Это будет фантастический выпуск!"
                    img 5761
                    with fadelong
                    w
                    m "Спасибо, Алекс..."
                    img 5762
                    with fadelong
                    m "Дорогой..."
                    img 5763
                    with fade
                    "Мы можем ехать."
                    img 5764
                    with fade
                    "Теперь я готова..."

#                    call episode1End_Dick()
                    return
                    #Victoria
                else:
                    show screen notify (_("Моника говорила другим людям про Дика плохо... (негатив)"))
            img 5713
            dick "Моника, я уже сказал."
            img 5712
            "Это все что я могу сделать для тебя."

    music Groove2_85
    img 3141
    with fadelong
    m "Дик."
    "Я так понимаю что у меня теперь нет денег?"
    img 3142
    dick "Нет, Моника, нету."
    img 3143
    m "И нет дома?"
    img 3142
    dick "Нет."
    img 3144
    m "И нет ни фирм, ни документов..."
    dick "Нет, моя милая."
    "Мне очень жаль..."
    img 3145
    m "Дик."
    "Я разберусь со всем этим."
    "Надеюсь ты мне поможешь."
    dick "Конечно, Моника, я тебе помогу."
    img 3146
    m "Скажи, у тебя можно остаться ночевать?"

#    $ dickOfficeCabinetStage = 3
#    call refresh_scene_fade() from _call_refresh_scene_fade_174

    return

label gallery_3268:
#    img black_screen
#    with Dissolve(0.5)
#    sound snd_car_turn_on
#    $ renpy.pause(2)
    sound snd_car_engine
    $ renpy.pause(0.5)

    $ renpy.music.stop("rain")
    music snd_moderate_rain_music
    img scene_Map
    show screen Rain_overlay
    imgr 3230
    $ rain = False
    $ rainIntencity = 3
    with fadelong
    m "Фрэд, так что там за урод, который теперь живет в моем доме?"

    imgl 3229
    fred "Там теперь живет Мистер Робертс, Мэм."
    "Возможно Вы его заочно знаете."
    "Он работал младшим менеджером в дочерней компании Стива, в другом городе, провинциальном."
    "Его повысили после Вашего ухода."
    "И теперь он живет здесь."
    "Он только переехал."
    "Со своей семьей."
    imgr 3231
    music Pyro_Flow
    m "Я помню его."
    "Я видела его отчеты."
    "Ни на что неспособное мелкое ничтожество."
    "!!!!!!!!!!!"
    imgr 3232
    music snd_moderate_rain_music
    imgl 3228
    fred "Он Вас лично не знает, Мэм."
    "Поэтому не советую называть свою фамилию."
    "Если новые хозяева узнают кто Вы, то они не дадут Вам работы."
    imgr 3231
    music Pyro_Flow
    m "За бесплатно???"
    "Я еще должна к этому сремиться???"
    "Стремиться работать у какого-то мелкого менеджера, такого муравья, которого я даже не замечала!"
    "Да еще и без денег!"

    music snd_moderate_rain_music
    fred "Мэм."
    "Вы получите самое главное."
    m "Что это?"
    fred "Вы получите крышу над головой, Мэм."
    "И Вам не придется спать на улице."
    "А Вы знаете, это опасно."
    imgl 3229
    w
    imgr 3232
    mt "!!!!!!!!!!!!!!!!"
    "(хмык)"
    "...."
    m "И что мне там придется делать?"
    fred "Я не знаю, Мэм."
    "У меня никогда не было гувернантки."
    "Наверное убирать дом и делать что скажут."
    "В Ваших интересах во всем выполнять приказы хозяев."
    "Иначе Вы можете лишиться крыши над головой."
    mt "!!!!!!!!!!!!"
    fred "Вы слышите меня, Мэм?"
    m "Да, я слышу, Фред..."

    stop music fadeout 1.0
    img black_screen
    hide screen Rain_overlay
    with Dissolve(0.5)
    sound snd_car_engine
    $ renpy.pause(2.0)
    music snd_moderate_rain_music
    img scene_Map
    show screen Rain_overlay
    imgl 3229
    with fadelong
    fred "Мистер Робертс живет со своей супругой. Миссис Робертс."
    imgr 3232
    m "А имя есть у супруги?"
    fred "Ее зовут Бетти, Мэм."
    "Но я советую обращаться к ней соответствующим образом."
    mt "!!!!!!!!!!!!"
    imgl 3228
    fred "Так же с ними живет сын Мистера Робертса."
    "Барди."
    "Он не в ладах с Миссис Робертс, потому что это не его родная мать."
    "Вам надо учитывать это."
    "Вам надо вписаться в их семью, принять их правила."
    "Чтобы остаться там жить."
    music Power_Bots_Loop
    hide screen Rain_overlay
    img 3233
    with hpunch
    mt "СОБЛЮДАТЬ ПРАВИЛА, ЧТОБЫ ОСТАТЬСЯ ЖИТЬ!"
    "В СВОЕМ ЖЕ ДОМЕ!!!"
    "О БОЖЕ!!!"


    stop music fadeout 1.0
    img black_screen
    hide screen Rain_overlay
    with Dissolve(0.5)
    sound snd_car_engine
    $ renpy.pause(2.0)
#    music snd_moderate_rain_music
    img 3234
    music Groove2_85
    m "Фред."
    "Куда ты меня привез?"
    "Я думала мы едем к дому?"
    "Ты же торопился."
    img 3235
    fred "Да, Миссис Бакфетт."
    "Мы правда туда едем."
    "Мы остановились всего на несколько минут."
    img 3236
    m "Зачем, Фред?.."
    fred "Понимаете, Миссис Бакфетт..."
    "Я потратил много усилий и времени чтобы помочь Вам."
    m "И что?"
    fred "И мне надо что-то взамен."
    img 3237
    m "Я позднее распоряжусь выдать тебе чаевые, Фред."
    fred "Большое спасибо заранее, Миссис Бакфетт."
    "Но мне нужно что-то сейчас..."
    img 3238
    m "Что же ты хочешь сейчас?"
    fred "Ничего особенного, Миссис Бакфетт."
    "Никто никого ни к чему не принуждает."
    "Вы вольны делать все что захотите."
    img 3239
    "..."
    "Просто поцелуйте мой член."
    music Pyro_Flow
    img 3240
    with hpunch
    m "ЧТООО!?!?!?"
    "КАК ТЫ ТАКОЕ МОЖЕШЬ ГОВОРИТЬ, ФРЕД????"
    img 3241
    fred "Мэм."
    "Если Вы не хотите, то можете этого не делать."
    "Как я говорил, никто никого не заставляет."
    img 3242
    m "Конечно же я не хочу, Фред!"
    "И не буду!!!"

    stop music fadeout 1.0
    img black_screen
    hide screen Rain_overlay
    with Dissolve(0.5)
    sound snd_car_door
    $ renpy.pause(1.0)

    img 3243
    with fadelong
    music Power_Bots_Loop
    m "Зачем ты смотришь на дверь, Фред?"
    fred "Мэм."
    "Наша встреча закончена."
    img 3244
    m "Как же так, Фред?"
    "А как же дом?"
    "Как же работа, которую ты предлагаешь?"
    img 3245
    fred "Никто никого не заставляет, Мэм."
    "Я не заставляю Вас."
    "Вы не заставляете меня Вам помогать."
    m "Это шантаж, Фред?!"
    fred "Нет, Мэм."
    "При шантаже Ваши условия ухудшаются если Вы не выполните требование."
    "Здесь-же, все остаются при своих."
    "Я без поцелуя на члене."
    "Вы без крыши над головой."
    "Все просто."
    "..."
    img 3246
    with fade
    fred "Мэм."
    "Попрошу Вас выйти, я тороплюсь!"
    img 3247
    mt "ЧТО ЖЕ МНЕ ДЕЛАТЬ???"
    "НА УЛИЦЕ СНОВА ДОЖДЬ!!!"
    "МНЕ ПРИДЕТСЯ ВЕСЬ ДЕНЬ ХОДИТЬ ПОД НИМ."
    "ИСКАТЬ КУДА ПРИЮТИТЬСЯ НА НОЧЬ!"
    img 3248
    mt "БОЛЬШЕ ВСЕГО Я БОЮСЬ ЧТО НЕ НАЙДУ ГДЕ ПЕРЕНОЧЕВАТЬ!"
    "У МЕНЯ ПРЕДЧУВСТВИЕ ЧТО ТАК И БУДЕТ!"
    img 3249
    mt "Этот Фред."
    "Извращенец."
    "Он хочет чтобы я поцеловала его грязный вонючий отросток..."
    img 3250
    mt "А Я НЕ ХОЧУ!!!"
    "..."
    music Groove2_85
    img 3253
    fred "Мэм."
    "Пожалуйста, выходите скорее."

    m "Фред.."
    "Это твое окончательное решение?"
    fred "Если Вы измение свое, то и я тоже."
    label gallery_afterJailFredDialogue3_menu_loop1:
        img 3250
        menu:
            "Я не хочу и не буду делать этого, Фред!":
                m "Я не хочу и не буду делать этого, Фред!"
                img 3246
                fred "Мэм."
                "Попрошу Вас выйти, я тороплюсь!"
                mt "О БОЖЕ!!!"
                jump gallery_afterJailFredDialogue3_menu_loop1
            "Фред, я никогда не делала этого...":
                pass

    img 3254
    m "Фред, я никогда не делала этого..."
    fred "Вы никогда не целовали член мужчины???"
    "А муж??"
    img 3255
    m "Мы..."
    "Мы с ним занимались этим всего пару раз."
    "И это было без таких извращений..."
    img 3256
    fred "Вам это не нравится, Миссис Бакфетт?"
    img 3257
    m "Я не люблю секс, Фред."
    "Я не понимаю что в нем такого."
    "Это вы мужчины любите его."
    img 3258
    fred "Хорошо, я Вам покажу."
    "Это просто, Миссис Бакфетт."
    "Расстегните мне ширинку."
    img 3259
    m "..."
    img 3260
    fred "..."
    img 3261
    w
    img 3262
    "Вот так."

    img 3263
    mt "БОЖЕ!!!"
    img 5895
#    img 3264
    "КАК ПРОТИВНО!!!"
    img 5896
#    img 3265
    m "Что дальше?"
    img 5897
#    img 3266
    fred "Возьмите его в вашу ручку, Миссис Бакфетт."
    img 5898
#    img 3267
    with fade
    w
    img 5899
#    img 3268
    w
    img 5900
#    img 3269
    m "Что дальше, Фред?"
    img 5901
#    img 3270
    fred "Теперь водите своей ручкой вверх и вниз, Миссис Бакфетт."

    stop music fadeout 1.0
    scene black
    image videoFred_Monica_Car_Blowjob_1_1 = Movie(play="video/Fred_Monica_Blowjob_1_1.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_1
    wclean
    scene black
    image videoFred_Monica_Car_Blowjob_1_2 = Movie(play="video/Fred_Monica_Blowjob_1_2.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_2
    wclean
    scene black
    image videoFred_Monica_Car_Blowjob_1_3 = Movie(play="video/Fred_Monica_Blowjob_1_3.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_3
    wclean
    scene black
    image videoFred_Monica_Car_Blowjob_1_4 = Movie(play="video/Fred_Monica_Blowjob_1_4.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_4
    wclean

    music Loved_up2
    menu:
        "Ускорить движения...":
#            $ monicaFredWasForcedBlowjob = False
            #video быстрого минета
            label gallery_5903:
            stop music fadeout 1.0
            scene black
            image videoFred_Monica_Car_Blowjob_1_4_fast = Movie(play="video/Fred_Monica_Blowjob_1_4_fast.mp4", fps=30)
            show videoFred_Monica_Car_Blowjob_1_4_fast
            wclean
            #render
            img 5902
            fred "Ааааааааахх!"
            img 5903
            with fadelong
            w

            music Power_Bots_Loop
            img 3281
            with fadelong
            fred "Вы оказались на высоте, Миссис Бакфетт!"
            "Ваша часть договора выполнена."
            "Теперь мы можем ехать."

        "Фред, может быть хватит?":
#            $ monicaFredWasForcedBlowjob = True
            label gallery_3277:
            music Loved_up2
            img 3272
            m "Фред, может быть хватит?"
            "Пожалуйста!"
            img 3273
            fred "Миссис Бакфетт! Сядьте, пожалуйста, ровно на кресло!"
            img 3274
            m "Уфффф... Наконец-то!.."
            fred "Миссис Бакфетт. Я попросил Вас сесть ровно."
            img 3275
            m "Хорошо, Фред."
            "Но я не понимаю зачем."
            "Может быть уже поедем?"
            music Gearhead
            img 3276
            fred "Вот зачем!"
            img 3277
            m "О БОЖЕ!!!"

            scene black
            image videoFred_Monica_Car_Sex_1_1 = Movie(play="video/Fred_Monica_Car_Sex_1_1.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_1
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_2 = Movie(play="video/Fred_Monica_Car_Sex_1_2.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_2
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_3 = Movie(play="video/Fred_Monica_Car_Sex_1_3.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_3
            wclean
        #    video:3381_1
        #    video:3382
        #    video:3381_1
        #    video:3385
        #    video:3382

            img black_screen
            with Dissolve(0.5)
            "..."
            "..."
            fred "Ааааааааахх!"
            "..."
            "ЕЩЕ!!!"

            scene black
            image videoFred_Monica_Car_Sex_1_4 = Movie(play="video/Fred_Monica_Car_Sex_1_4.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_4
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_5 = Movie(play="video/Fred_Monica_Car_Sex_1_5.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_5
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_6 = Movie(play="video/Fred_Monica_Car_Sex_1_6.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_6
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_7 = Movie(play="video/Fred_Monica_Car_Sex_1_7.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_7
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_8 = Movie(play="video/Fred_Monica_Car_Sex_1_8.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_8
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_9 = Movie(play="video/Fred_Monica_Car_Sex_1_9.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_9
            wclean
        #    video:3387
        #    video:3388
        #    video:3389
        #    video:3390
        #    video:3393
        #    video:3394
            label gallery_5904:
            music Power_Bots_Loop
            img 3383
            with fadelong
            m "Ф... Ф...."
            "Ф... ФРЕД!!!"
            img 3279
            "ЧТО ТЫ СДЕЛАЛ?!?!?!"
            fred "Миссис Бакфетт."
            "Даже не вздумайте выплевывать."
            "Если Вы выплюнете, это разорвет наш договор!"
            "И Вы можете уходить!"
            img 3280
            m "..."
            "...."
            "..."
            stop music fadeout 1.0
            fred "НУ?!?!"
            "ГЛОТАЙТЕ!"
            menu:
                "Проглотить...":
#                    $ monicaFredWasSpermEat = True
                    m "..."

                    sound snd_gulp
                    "Глоток"
                "Выплюнуть...":
                    img 5904
                    with fade
                    mt "(Сплевывание)"
                    fred "Понимаю, Вам еще предстоит это освоить..."
                    "Итак..."

            music Power_Bots_Loop
            fred "Вы оказались на высоте, Миссис Бакфетт!"
            img 3281
            "Ваша часть договора выполнена."
            "Теперь мы можем ехать."


    img black_screen
    with Dissolve(0.5)
    sound snd_car_turn_on
    $ renpy.pause(2)
    sound snd_car_engine
    $ renpy.pause(0.5)

    music snd_moderate_rain_music
    img scene_Map
    show screen Rain_overlay
    $ rain = False
    $ rainIntencity = 3

    img 3282
    with fadelong
    m "Чччасть... договора..."
    "...??????????..."
    "...!!!!!!!!!!!!!!!!"
    music Pyro_Flow
    img 3283
    "Ах ты ублюдок!!!"
    img 3284
    "СВОЛОЧЬ!!!"
    img 3285
    "Я УБЬЮ ТЕБЯ, СЛЫШИШЬ?!?!?!"
    img 3286
    fred "Мэм!"
    "Если Вы будете препятствовать водителю вести транспортное средство, то я вынужден буду высадить Вас!"
    "По инструкции безопасности!"
    img 3287
    "ВЫ МЕНЯ СЛЫШИТЕ, МЭМ?!?!"


    stop music fadeout 1.0
    img black_screen
    with Dissolve(0.5)
    sound snd_car_engine
    $ renpy.pause(2.0)

    music Groove2_85
    img 3288
    fred "Миссис Бакфетт!"
    "Не забудьте, что Вы гувернантка."
    "С солидным опытом."
    "Вы все умеете делать очень хорошо."
    "Ведите себя скромно."
    "Называйте всех Сэр и Мэм."
    "А также Мистер и Миссис."
    "От того какое впечатление вы произведете, зависит возьмут-ли Вас на работу."
    img 3289
    m "Но Фред."
    "Я думала ты уже договорился?"
    fred "Я договорился только с Мистером Робертсом."
    "С его супругой я не общался."
    "Вам надо произвести на нее впечатление."
    img 3290
    m "......"
    img 3291
    fred "Дождь закончился, Миссис Бакфетт."
    img 3290
    m "......"

#    $ miniMapEnabledOnly = ["Street_Yard"]
#    $ map_enabled = False
#    $ hud_preset_current = "default"
#    $ map_hud_preset_current = "map"
#    $ unfocus_map()
#    $ subst_to_object("Teleport_Gate", "afterJailHouseFamily_dialogue1")
#    $ subst_to_object("Teleport_House", "afterJailHouseFamily_dialogue1")
#    $ subst_to_object("Teleport_Fence", "afterJailHouseFamily_dialogue1")

#    $ remove_objective("come_to_fred")
#    $ add_objective("come_to_family", _("Идти к новым хозяевам"), c_orange, 10)
#    $ autorun_to_object("street_house_main_yard", "afterJailHouseFamily_dialogue0")

    $ rain = False
    $ renpy.music.stop("rain")

#    $ streetHouseMainYardStage = 1

    return

label gallery_3296:
#    $ remove_objective("come_to_family")
    music Groove2_85
    img 3294
    with fadelong
    w
    img 3295
    with fade
    w
    img 3296
    with fade
    ralph "Здравствуй."
    "Как тебя зовут?"
    img 3297
    m "Меня зовут Моника, Мистер Робертс."
    img 3298
    ralph "Приятно познакомиться, Моника."
    "Мы тебя как раз ждали."
    img 3299
    m "Мне тоже приятно познакомиться, Мистер Робертс и .."
    img 3300
    "...Миссис Робертс."
    img 3301
    "У Вас такой забавный мальчик!"
    img 3302
    bardie "Я не мальчик!"
    "Я уже взрослый!"
    "Меня зовут Барди!"
    "Мне 18!"
    img 3303
    m "Конечно, Барди."
    "Я и с тобой рада познакомиться."
    img 3304
    music Pyro_Flow
    betty "Фи!"
    "Ральф!"
    "Зачем нам такая гувернантка?"
    "Неужели она что-то умеет?"
    "Да и вообще! Посмотри на нее!"
    img 3305
    "Она же некрасивая!"
    "Посмотри на ее фигуру! Какие у нее толстые неровные бедра!"
    "И какая нелепая грудь!"
    img 3306
    "Да и одета она как шлюха."
    "Посмотри на нее, Ральф."
    "Посмотри на ее одежду!"
    "Я не удивлюсь если она еще час назад ублажала мужчину!"
    img 3307
    with fade
    w
    img 3308
    w
    img 3309
    "Ральф? Тебе нужны шлюхи в доме?"
    "Мне нет!"
    img 3310
    mt "ССССССУЧКА!!!!"
#    music Hidden_Agenda
#    img 3311
#    bardie_t "Я считаю что шлюх много не бывает..."
#    "Надо рассмотреть эту MILF'у поближе"

    music Groove2_85
    img 3295
#    img 3312
    ralph "Итак, Моника."
    "Что ты умеешь?"
    "Нам надо делать уборку в доме."
#    img 3313
    img 3314
    m "Да, Мистер Робертс."
    "Я имею большой опыт в деле уборки."
    "Я уже занималась уборкой в богатых домах."
    mt "Да! Я вру!"
    "Но мне же надо устроиться сюда!"
#    img 3315
    img 3316
    ralph "Видишь, Бетти?"
    "Она умеет делать уб..."
    music Pyro_Flow
    betty "Помолчи, Ральф!"
    "Я не разрешала тебе говорить!"
    ralph "Прости, дорогая..."

#    img 3311
#    sound man_steps
#    img black_screen
#    with Dissolve(0.5)
#    $ renpy.pause(1.0)
#    img 3317
#    with fade
#    sound wow
#    w
    music Power_Bots_Loop
#    img 3318
#    with fade
    mt "МНЕ НАДО КАК-ТО УБЕДИТЬ ЭТУ СУЧКУ ВЗЯТЬ МЕНЯ!"
    "ААААААААРГХХ"
    "МОНИКА!"
    "КАК ЭТО ВСЕ МОГЛО СЛУЧИТЬСЯ????"
    music Hidden_Agenda
#    img 3319
    m "Миссис Робертс."
    "Пожалуйста, возьмите меня."
    img 3320
    "Я Вас очень прошу!"
    "Я буду делать всю работу по дому и буду выполнять все Ваши приказы."
    img 3321
    "..."
    "Пожалуйста, не обращайте внимание на мой внешний вид."
    "Дело в том что мое платье испачкалось и мне пришлось одеть что попалось, так как я торопилась к Вам!"
    music Pyro_Flow
    img 3322
    betty "Нет, я не думаю."
    "Твоя прическа мне тоже не нравится."
#    music Hidden_Agenda
#    img 3323
#    bardie_t "Хм..."
#    "Неплохо было бы переубедить мачеху..."
#    "Эта гувернантка весьма горяча..."
#    img 3324
#    "Еще такая послушная кукла может пригодиться для моих планов относительно мачехи..."

#    sound man_steps
#    img black_screen
#    with Dissolve(0.5)
#    $ renpy.pause(1.0)

#    music Hidden_Agenda
#    img 3325
#    bardie "Бетти!"
#    "Послушай."
#    "Давай возьмем эту гувернантку."
#    betty "С чего бы вдруг?"
#    bardie "Я думаю она может хорошо работать."
#    img 3326
#    bardie_t "Своей киской, хе-хе"
#    img 3326
#    bardie "А я начну тебя слушаться."
#    "И перестану донимать."
#    "Стану хорошо учиться и не буду лезть в то что ты тратишь много денег на одежду!"
#    betty "Хм..."
#    "Обещаешь?"
#    bardie "Обещаю, Бетти!"
#    bardie_t "Ты мне потом заплатишь за мои лишения, сполна! Хе-хе"
#    img 3327
#    betty "Ой, ну ладно..."
#    "Раз уж так..."
#    "Но Барди!"
#    "Я запомню твое обещание!"
#    bardie "Конечно, Бетти!"
    img 3328
    betty "Хорошо."
    music Groove2_85
    "Ральф, пусть она работает у нас."
    "Может быть буду брать ее иногда в фитнес-зал."
    "Поправлю ее ужасную фигуру."
    img 3329
    music Power_Bots_Loop
    mt "!!!!!!!!"
    "ТВАРЬ!!!!"
    "НЕНАВИЖУ!!!"
#    music Hidden_Agenda
#    img 3330
#    bardie "Добро пожаловать, Моника!"
#    bardie_t "Хе-хе"

    music Groove2_85
    img 3331
    ralph "..."
    "Моника."
    "Ты можешь проходить в дом."
    "Мы сегодня не выспались, так как у нас были гости."
    "Но Бетти уже все убрала, поэтому на сегодня у тебя работы нет."
    "Мы сегодня пораньше ляжем спать."
    "Так что ты можешь отдыхать."
    "Завтра с утра ты можешь приступать к работе."

    m "Хорошо, Сэр."
    "Спасибо Вам."
    img 3332
    "..."
    "Спасибо, Миссис Робертс."
    img 3333
    betty "Фи..."
    mt "!!!!!!!"
    "СУЧКА!!!!!!"

    stop music fadeout 1.0
    sound man_steps
    img black_screen
    with Dissolve(0.5)
    sound highheels_short_walk
    $ renpy.pause(1.0)
    music Groove2_85
    img 3334
    with fadelong
    betty "Твоя униформа находится в ванной комнате."
    "Иди переоденься."
    "Мне не нравится что по дому кто-то гуляет в таком виде!"
    img 3335
    with fade
    "И да!"
    "Я буду присматривать за тобой!"


#    $ streetHouseMainYardStage = 2

#    $ miniMapEnabledOnly = ["Floor1", "Street_Yard"]
#    $ casualMusic = "Groove2_85"

#    $ bettyLocation = "Bedroom1"
#    $ bardieLocation = "BedroomBardie"
#    $ ralphLocation = "LivingRoom"

#    $ subst_to_object("Teleport_House_Outside_Outside", "afterJailHouseFamily_dialogue4")
#    $ subst_to_object("Teleport_Gate", False)
#    $ subst_to_object("Teleport_House", False)
#    $ subst_to_object("Teleport_Fence", False)
#    $ autorun_to_object("basement_pool", False)
#    $ autorun_to_object("floor1", "afterJailHouse_dialogue1")
#    call refresh_scene_fade() from _call_refresh_scene_fade_2
    return
