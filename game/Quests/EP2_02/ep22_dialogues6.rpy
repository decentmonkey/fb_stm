# Если Моника уже заработала 5000, то Бифа нет

# Если Биф есть, то Моника спрашивает еще о работе
# Биф говорит нет проблем, иди в студию, но сначала ты пройдешь кастинг.
# И если Моника не проходила его в прошлый раз, то Биф говорит что ты увиливаешь от кастинга, но тебе придется его пройти, иначе не будет карьерного роста.
# Моника идет к Алексу, одевается в выбранную одежду (еще 2 варианта одежды)
# Затем появляется идти к Бифу на кастинг или не идти (если не идти, то прогресс у Бифа не растет)
# Кастинг пока - грудь, по паре-тройке поз. Биф говорит прими какую-нибудь позу с голой грудью, покажи папочке как ты привлекательна.
# Если Моника не заставляла мартышек раздеваться, то прогресс у Бифа растет без кастинга

# Моника делает фотосессию в выбранной одежде. В конце каждой фотосессии развратные позы.
# После каждой фотосессии растет прогресс у Алекса. На lvl.2 он встает

# Моника возвращается к Бифу и спрашивает про деньги.
# (Если Моника обещала вести себя как хорошая цыпочка, то Биф не хочет давать деньги), но Моника упрашивает его говоря
# что она хорошая цыпочка и заслужила денежку.
# Первый раз Биф говорит что наличных у него в этот раз для нее нет. Моника дает бумажку и просит купить этот сертификат на этот адрес.
# Биф отвечает окей.
# В следующие разы Биф спрашивает что купить такой же сертификат как тогда?
# Моника отвечает что да, Биф шутит что куда она девает все те аксессуары, которые покупает?
# Ей, видимо нравится ходить в таком виде. Моника злится.

# Моника встречает секретаршу, та говорит что все хорошо, мистер Биф заботится о нас.
# Мы должны делать что он говорит. Моника спрашивает что с тобой сделали???
# В этот момент идет вызов и Биф называет секретаршу сиськой и говорит чтобы она подошла в кабинет
# Та отвечает да, мистер Биф, уже беги и идет
# У нее рендер в штанах с голой задницей с трусами
default monicaCasualDress1BiffFirstTime = True
default monicaCasualDress1AlexFirstTime = True

label ep22_dialogue6_1:
    #Диалог секретарши с Моникой, когда Моника пытается зайти к Бифу
    music Groove2_85
    img 8268
    with fade
    m "Дорогуша, как у тебя дела?"
    img 8269
    secretary "..." #Сидит как истукан
    img 8270
    with fade
    m "Я знаю что на тебя сильно давит новый Босс."
    "Но, поверь, я скоро разберусь со всем этим!"
    img 8271
    secretary "Мистер Биф лучше нас знает что нам необходимо."
    secretary "Мистер Биф заботится о нас..."
    img 8272
    m "Что?"
    "Что ты такое говоришь, дорогуша???"
    img 8271
    with fade
    secretary "Мы должна благодарить Мистера Бифа что работаем у него..."
    img 8273
    m "Что они с тобой сделали???"

    sound beep1
    img 8274
    with fade
    #звук коммутатора
    pause 1.0
    biff "Эй! Сиська!"
    "Быстро зайди ко мне в кабинет!"
    "И захвати еще виски!!!"
    secretary "Да, Мистер Биф! Одну секунду!"

    music Funk_loop8
    img 8275
    with fade
    "Где же?!"
    "Где же виски???"
    img 8276
    with Dissolve(0.5)
    "Здесь нет!"
    "Он все выпил..."
    img 8277
    w
    sound highheels_short_walk
    img 8278
    with fade
    "Ах, я же спрятала еще бутылку здесь, чтобы он сразу не нашел..."
    sound highheels_run1
    img 8279
    with fade
    "Вот оно!"
    #Секретарша уходит, Моника смотрит на ее зад
    img 8280
    w
    img 8281
    with fade
    mt "О БОЖЕ!!!"
    "Бедняжка! Что они с тобой сделали?!?!"
    #пауза спустя 5 минут
    #Секретарша возвращается
    img black_screen
    with Dissolve(1.0)
    sound highheels_run1
    pause 2.0
    return

label ep22_dialogue6_2a:
    mt "Бедняжка! Что они с тобой сделали?!?!"
    return

label ep22_dialogue6_2:
    #render
    #Моника разговаривает с секретаршей повторно
    if act == "l":
        return

    $ store_music()
    music Stealth_Groover
    if cloth == "Whore":
        img 8282
        with fade
        secretary "Мистер Биф лучше нас знает что нам необходимо."
        secretary "Мистер Биф заботится о нас..."
        img 8283
    if cloth == "CasualDress1":
        img 11242
        with fade
        secretary "Мистер Биф лучше нас знает что нам необходимо."
        secretary "Мистер Биф заботится о нас..."
        img 11243
    if cloth == "WorkingOutfit1":
        img 12771
        with fade
        secretary "Мистер Биф лучше нас знает что нам необходимо."
        secretary "Мистер Биф заботится о нас..."
        img 12772

    #если Моника сегодня не просила деньги, то появляется меню выбора
    menu:
        "Попросить деньги в долг.":
            "Дорогая..."
            secretary "Да, Миссис Бакфетт?"
            m "Скажи, у тебя не будет немного денег?"
            if cloth == "Whore":
                img 8284
            if cloth == "CasualDress1":
                img 11244
            if cloth == "WorkingOutfit1":
                img 12773

            with fade
            secretary "Миссис Бакфетт! Я пока не видела зарплаты здесь, после Вашего ухода..."
            #если у Моники меньше 5 долларов, то дает, иначе нет
            if money > 2:
                secretary "Поэтому у меня нет никаких денег сейчас, Миссис Бакфетт!"
                "Простите!"
                m "А как же Биф? Он что, не дает тебе деньги?"
                if cloth == "Whore":
                    img 8285
                if cloth == "CasualDress1":
                    img 11240
                if cloth == "WorkingOutfit1":
                    img 12769
                with fade
                secretary "Мистер Биф лучше нас знает что нам необходимо."
            else:
                #
                secretary "У меня есть только кредитная карточка, но мне надо платить за ипотечный кредит."
                "У меня есть $ 5 наличными и все..."
                m "Дорогуша, дай мне, пожалуйста, эти $ 5..."
                if cloth == "Whore":
                    img 8286
                if cloth == "CasualDress1":
                    img 11245
                if cloth == "WorkingOutfit1":
                    img 12774
                with fade
                secretary "Да, Миссис Бакфетт!"
                "Держите..."
                $ add_money(5)
                #дает 5 баксов

        "Дорогуша, ты не видела Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5b() from _call_ep23_dialogue9_5b

        "Заставить секретаршу показать грудь в трущобах. (bitchiness)" if game.extra == True and ep27_quests_secretary1_show_boobs_active == True and pylonpart4startsCompleted == True and monicaWorkingAtBiffOffice == True:
            call ep27_quests_secretary1() from _call_ep27_quests_secretary1
            if _return == False:
                return False
        "Уйти.":
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"
    $ restore_music()
    return

label ep22_dialogue6_2b:
    if get_active_objects("Biff", scene="monica_office_cabinet") == False:
        music Groove2_85
        if day_time == "day":
            if cloth == "Whore":
                #render
                img 8284
                with fade
                secretary "Миссис Бакфетт!"
                "Мистера Бифа сейчас нет на месте!"
                img 8283
                m "Когда он будет?"
                img 8285
                secretary "Он сказал что будет вечером!"
                img 8284
                m "Хорошо, дорогая, спасибо."
            else:
                if cloth == "CasualDress1":
                    #render
                    img 11244
                    with fade
                    secretary "Миссис Бакфетт!"
                    "Мистера Бифа сейчас нет на месте!"
                    img 11243
                    m "Когда он будет?"
                    img 11240
                    secretary "Он сказал что будет вечером!"
                    img 11244
                    m "Хорошо, дорогая, спасибо."
                else:
                    if cloth == "WorkingOutfit1":
                        #render
                        img 12773
                        with fade
                        secretary "Миссис Бакфетт!"
                        "Мистера Бифа сейчас нет на месте!"
                        img 12772
                        m "Когда он будет?"
                        img 12769
                        secretary "Он сказал что будет вечером!"
                        img 12773
                        m "Хорошо, дорогая, спасибо."
                    else:
                        secretary "Миссис Бакфетт!"
                        "Мистера Бифа сейчас нет на месте!"
                        m "Когда он будет?"
                        secretary "Он сказал что будет вечером!"
                        "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                        m "Хорошо, дорогая, спасибо."
            return False
        if day_time == "evening":
            if cloth == "Whore":
                #render
                img 8284
                with fade
                secretary "Миссис Бакфетт!"
                "Мистера Бифа сейчас нет на месте!"
                img 8283
                m "Когда он будет?"
                img 8285
                secretary "Он сказал что будет завтра!"
                "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                img 8284
                m "Хорошо, дорогая, спасибо."
            else:
                if cloth == "CasualDress1":
                    #render
                    img 11244
                    with fade
                    secretary "Миссис Бакфетт!"
                    "Мистера Бифа сейчас нет на месте!"
                    img 11243
                    m "Когда он будет?"
                    img 11240
                    secretary "Он сказал что будет завтра!"
                    "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                    img 11244
                    m "Хорошо, дорогая, спасибо."
                else:
                    if cloth == "WorkingOutfit1":
                        #render
                        img 12773
                        with fade
                        secretary "Миссис Бакфетт!"
                        "Мистера Бифа сейчас нет на месте!"
                        img 12772
                        m "Когда он будет?"
                        img 12769
                        secretary "Он сказал что будет завтра!"
                        "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                        img 12773
                        m "Хорошо, дорогая, спасибо."
                    else:
                        secretary "Миссис Бакфетт!"
                        "Мистера Бифа сейчас нет на месте!"
                        m "Когда он будет?"
                        secretary "Он сказал что будет завтра!"
                        "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
                        m "Хорошо, дорогая, спасибо."
            return False
    return

label ep22_dialogue6_3:
    #render
    #Моника заходит регулярно к Бифу по работе
    if cloth == "CasualDress1" and monicaCasualDress1BiffFirstTime == True:
        $ monicaCasualDress1BiffFirstTime = False
        img 11286
        biff "О! Цыпочка!"
        biff "Ты наконец-то начала тратить деньги, которые я плачу тебе!"
        img 11287
        biff "Ты редкая находка!"
        biff "Нечасто десятидолларовую шлюху можно одеть и получить такой раскошный результат!"
        img 11288
        mt "Я не шлюха, мерзавец!"
        mt "И я рождена, чтобы раскошно одеваться!"
        mt "Скоро я верну все назад!"
        img 11289
        m "Да, Биф..."
        m "Спасибо за комплимент."

    menu:
        "Спросить о работе":
            pass
        "Биф, ты не видел Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5c() from _call_ep23_dialogue9_5c
            return False
        "Уйти.":
            return False
    music Groove2_85
    if ep211_quests_publicevent2_completed == False and ep22_quests_monica_presentation_completed == True and math.floor((day+1)/7) > math.floor((ep22_quests_monica_presentation_completed_day+1)/7) and ((len(list(set(PS8_shoots_array))) >= 24 or photoshoot8_nude_completed == True)):
        # Если был первый паблик евент и наступила следующая неделя
        if biffWeeklyPhotoShootEnabled == True: # Если Моника может сделать фотосессию
            call ep211_quests_publicevent2_1() # from _rcall_ep211_quests_publicevent2_1 # Первый разговор о втором паблик евенте
            return False
    if ep211_quests_photoshot8_opened_day != 0 and biffWeeklyPhotoShootEnabled == True and ep213_quests_biff1_inited == False:
        call ep213_quests_biff1_init() from _rcall_ep213_quests_biff1_init
        return False
    if ep213_presentation2_completed_day > 0 and day - ep213_presentation2_completed_day >= 6 and ep215_quests_escort_initialized == False: #EP25 hotfix1
        call ep215_quests_esort1_init() from _rcall_ep215_quests_esort1_init # инициализируем свидание с инвестором

    if cloth == "Whore":
        img 8287
        with fade
        m "Биф..."
        "Я хотела узнать у тебя..."
        "Есть-ли еще работа?"
        img 8288
        "Мне нужны деньги..."
    if cloth == "CasualDress1":
        img 11250
        with fade
        m "Биф..."
        "Я хотела узнать у тебя..."
        "Есть-ли еще работа?"
        img 11251
        "Мне нужны деньги..."
    if cloth == "WorkingOutfit1":
        img 12779
        with fade
        m "Биф..."
        "Я хотела узнать у тебя..."
        "Есть-ли еще работа?"
        img 12780
        "Мне нужны деньги..."

    call process_hooks("photoshoots_work_available_check", "global") from _call_process_hooks_31
    if biffWeeklyPhotoShootEnabled == False or _return == False:
        #Если не прошла неделя
        if cloth == "Whore":
            img 8289
            with fade
            biff "Нет, цыпочка!"
            "Сейчас очередь других цыпочек!"
            "Ты пока еще не настолько полюбилась папочке!"
            img 8290
            mt "УРОД!!!"
        if cloth == "CasualDress1":
            img 11252
            with fade
            biff "Нет, цыпочка!"
            "Сейчас очередь других цыпочек!"
            "Ты пока еще не настолько полюбилась папочке!"
            img 11253
            mt "УРОД!!!"
        if cloth == "WorkingOutfit1":
            img 12781
            with fade
            biff "Нет, цыпочка!"
            "Сейчас очередь других цыпочек!"
            "Ты пока еще не настолько полюбилась папочке!"
            img 12782
            mt "УРОД!!!"

        menu:
            "Уйти...":
                return False
            "А если я пройду дополнительный кастинг?...":
                if cloth == "Whore":
                    img 8291
                    with fade
                    m "А если я пройду дополнительный кастинг?..."
                    img 8292
                    biff "Эта цыпочка пока слишком скучная для дополнительного кастинга!"
                    "Я держу эту куклу только из-за того что она похожа на сучку Бакфетт!"
                    "Иди и не отвлекай папочку! Ему нужно заботить о других цыпочках!"
                    img 8290
                    with fade
                    mt "Я НЕНАВИЖУ ЭТОГО УРОДА!!!"
                    "КОГДА Я ВЕРНУ СВОЕ МЕСТО НАЗАД?!?!"
                if cloth == "CasualDress1":
                    img 11254
                    with fade
                    m "А если я пройду дополнительный кастинг?..."
                    img 11255
                    biff "Эта цыпочка пока слишком скучная для дополнительного кастинга!"
                    "Я держу эту куклу только из-за того что она похожа на сучку Бакфетт!"
                    "Иди и не отвлекай папочку! Ему нужно заботить о других цыпочках!"
                    img 11253
                    with fade
                    mt "Я НЕНАВИЖУ ЭТОГО УРОДА!!!"
                    "КОГДА Я ВЕРНУ СВОЕ МЕСТО НАЗАД?!?!"
                if cloth == "WorkingOutfit1":
                    img 12783
                    with fade
                    m "А если я пройду дополнительный кастинг?..."
                    img 12784
                    biff "Эта цыпочка пока слишком скучная для дополнительного кастинга!"
                    "Я держу эту куклу только из-за того что она похожа на сучку Бакфетт!"
                    "Иди и не отвлекай папочку! Ему нужно заботить о других цыпочках!"
                    img 12782
                    with fade
                    mt "Я НЕНАВИЖУ ЭТОГО УРОДА!!!"
                    "КОГДА Я ВЕРНУ СВОЕ МЕСТО НАЗАД?!?!"
                return False
    # Проверка на то что Моника мало работала эти дни
    if monicaWorkingAtBiffOffice == True and get_office_working_status(6) < 1 and ep26_quest_work_start_day != day:
        img 12781
        with fade
        biff "Нет, цыпочка!"
        biff "Ты слишком часто прогуливаешь работу!"
        "Сейчас очередь других цыпочек зарабатывать деньги!"
        "Цыпочек, которые не увиливают от посещения работы!"
        music Power_Bots_Loop
        img 12782
        with diss
        mt "УРОД!!!"
        $ notif(t_("Монике надо ходить на работу в офис хотя бы раз в неделю."))
        return False

    if cloth == "Whore":
        img 8293
    if cloth == "CasualDress1":
        img 11256
    if cloth == "WorkingOutfit1":
        img 12785
    with fade
    biff "Да, цыпочка!"
    "Работа есть!"
    "Иди в студию!"

    if biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True:
        if monicaWorkingAtBiffOffice == True:
            img 8294
            biff "Только цыпочка! Тебе надо пройти кастинг после фотосессии!"
            biff "Цыпочка теперь работает у папочки в офисе!"
            biff "Значит цыпочка должна развлекать папочку!"
            if cloth == "Whore":
                img 8295
            if cloth == "CasualDress1":
                img 11257
            if cloth == "WorkingOutfit1":
                img 12786
            mt "О БОЖЕ!!!"
            "Только не это!!!"
        else:
#        if biffMonicaCastingsEnabled == True:
            $ notif(t_("Моника заставляла моделей проходить обнаженный кастинг"))
            #если надо пройти кастинг
            img 8294
            biff "Только цыпочка! Тебе надо пройти кастинг!"
            if cloth == "Whore":
                img 8295
            if cloth == "CasualDress1":
                img 11257
            if cloth == "WorkingOutfit1":
                img 12786
            mt "О БОЖЕ!!!"
            "Только не это!!!"



        if biffMonicaLastCastingSkipped == True:
            #если Моника увиливала от кастинга в прошлый раз
            if cloth == "Whore":
                img 8296
                with fade
                biff "Я знаю ты увиливаешь от кастинга, но тебе придется его пройти!"
                "Иначе не будет карьерного роста!"
                "Ты понимаешь?"
                img 8297
                m "Да, я понимаю, Биф..."
                img 8290
                mt "Сволочь!!!"
            if cloth == "CasualDress1":
                img 11258
                with fade
                biff "Я знаю ты увиливаешь от кастинга, но тебе придется его пройти!"
                "Иначе не будет карьерного роста!"
                "Ты понимаешь?"
                img 11259
                m "Да, я понимаю, Биф..."
                img 11253
                mt "Сволочь!!!"
            if cloth == "WorkingOutfit1":
                img 12787
                with fade
                biff "Я знаю ты увиливаешь от кастинга, но тебе придется его пройти!"
                "Иначе не будет карьерного роста!"
                "Ты понимаешь?"
                img 12788
                m "Да, я понимаю, Биф..."
                img 12782
                mt "Сволочь!!!"

    if monicaWorkingAtBiffOffice == True and monicaWorkFlashCardQuestActive == True and day-monicaWorkFlashCardReportLastDay > 14: # Моника долго не сдавала отчеты
        call ep27_dialogues4_biff7() from _call_ep27_dialogues4_biff7
#        $ add_char_progress("Biff", biffFlashCardQuestBiffNoticeNoReportsRegress, "biffFlashCardQuestBiffNoticeNoReportsRegress" + str(day))


    #блокировать выход на monica_office_secretary_dialogue6
    return

label ep22_dialogue6_4:
    #render
    #Моника пришла к Алексу, фотосессии еще нет
    if act=="l":
        return
    $ store_music()
    music Stealth_Groover
    if cloth == "Whore":
        img 6352
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Здравствуйте!"
        img 6353
        m "Здравствуй, Алекс..."
        img 6354
        alex_photograph "Вы хотите сделать еще одну фотосессию?"
    if cloth == "CasualDress1":
        img 11232
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Здравствуйте!"
        img 11233
        m "Здравствуй, Алекс..."
        if monicaCasualDress1AlexFirstTime == True:
            $ monicaCasualDress1BiffFirstTime = False
            img 11290
            alex_photograph "Миссис Бакфетт, я не припомню этого платья в фотореквизите."
            alex_photograph "Вы одели новое поступление?"
            img 11291
            m "Нет, Алекс! Это мое платье!"
            img 11292
            alex_photograph "Вы купили его?"
            img 11293
            m "Да... Я... Я купила его."
            m "И хватит задавать глупые вопросы!"
        img 11234
        alex_photograph "Вы хотите сделать еще одну фотосессию?"

    if cloth == "WorkingOutfit1":
        img 12761
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Здравствуйте!"
        img 12762
        m "Здравствуй, Алекс..."
        img 12763
        alex_photograph "Вы хотите сделать еще одну фотосессию?"


    menu:
        "Алекс... А где Мелани?" if monicaNeedToAskMelanieForHelp == True and day_time == "evening":
            call ep23_dialogues5_1() from _call_ep23_dialogues5_1
            return False
        "Алекс... А где Мелани?" if get_active_objects("Melanie", scene="monica_office_makeup_room") != False:
            call ep23_dialogues8_1() from _call_ep23_dialogues8_1
            return False
        "Алекс... А где Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5a() from _call_ep23_dialogue9_5a
            return False
        "Пока нет...":
            pass
    m "Пока нет..."
    alex_photograph "Миссис Бакфетт! Приходите в любой момент!"
    img 6358
    "Я всегда рад фотографировать Вас!"
    if cloth == "Whore":
        img 6353
    if cloth == "CasualDress1":
        img 11233
    if cloth == "WorkingOutfit1":
        img 12762
    mt "!!!"
    $ restore_music()
    return

label ep22_dialogue6_5:
    #render
    #Моника пришла к Алексу, фотосессия начинается
    if act=="l":
        return
    music Stealth_Groover
    if cloth == "Whore":
        img 6352
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Здравствуйте!"
        img 6353
        m "Здравствуй, Алекс..."
        img 6354
        alex_photograph "Вы хотите сделать еще одну фотосессию?"
    if cloth == "CasualDress1":
        img 11232
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Здравствуйте!"
        img 11233
        m "Здравствуй, Алекс..."
        img 11234
        alex_photograph "Вы хотите сделать еще одну фотосессию?"
    if cloth == "WorkingOutfit1":
        img 12761
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Здравствуйте!"
        img 12762
        m "Здравствуй, Алекс..."
        img 12763
        alex_photograph "Вы хотите сделать еще одну фотосессию?"

    menu:
        "Да... (черт!)":
            pass
        "Алекс... А где Мелани?" if monicaNeedToAskMelanieForHelp == True and day_time == "evening":
            call ep23_dialogues5_1() from _call_ep23_dialogues5_1_1
            return False
        "Алекс... А где Мелани?" if get_active_objects("Melanie", scene="monica_office_makeup_room") != False:
            call ep23_dialogues8_1() from _call_ep23_dialogues8_1_1
            return False
        "Алекс... А где Мелани?" if melanieDisappeared == True:
            call ep23_dialogue9_5a() from _call_ep23_dialogue9_5a_1
            return False

        "Пока нет...":
            return False
    m "Да, Алекс..."
    "Еще одну..."
    if cloth == "Whore":
        img 8314
        mt "Дьявол! Не знаю куда эти грязные фотосессии меня заведут!"
        "Надо кончать с этим скорее!"

        img 6354
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Вы уже знаете кем в каком наряде Вы будете сниматься в этот раз?"

        img 6353
        m "Еще не знаю..."
        "Что там Биф придумал на этот раз?"

        img 6527
        w
    if cloth == "CasualDress1":
        img 11235
        mt "Дьявол! Не знаю куда эти грязные фотосессии меня заведут!"
        "Надо кончать с этим скорее!"

        img 11234
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Вы уже знаете кем в каком наряде Вы будете сниматься в этот раз?"

        img 11233
        m "Еще не знаю..."
        "Что там Биф придумал на этот раз?"

        img 11236
        w

    if cloth == "WorkingOutfit1":
        img 12764
        mt "Дьявол! Не знаю куда эти грязные фотосессии меня заведут!"
        "Надо кончать с этим скорее!"

        img 12763
        with fade
        alex_photograph "Миссис Бакфетт!"
        "Вы уже знаете кем в каком наряде Вы будете сниматься в этот раз?"

        img 12762
        m "Еще не знаю..."
        "Что там Биф придумал на этот раз?"

        img 12765
        w

    return True

label ep22_dialogue6_5a:
    #выбор наряда завершен
    if cloth == "Whore":
        img 6357
        with fade
        alex_photograph "Отлично, Миссис Бакфетт!"
        "Можете переодеваться здесь! Я не буду смотреть!"
        img 6356
        m "Я переоденусь в гримерке!"
        "Надеюсь Мелани не закрыла ее в этот раз?"
        img 8315
        alex_photograph "Нет, Миссис Бакфетт, она открыта..." #грустно
        img 8316
        with fade
        m "Я скоро вернусь!"
    if cloth == "CasualDress1":
        img 11247
        with fade
        alex_photograph "Отлично, Миссис Бакфетт!"
        "Можете переодеваться здесь! Я не буду смотреть!"
        img 11246
        m "Я переоденусь в гримерке!"
        "Надеюсь Мелани не закрыла ее в этот раз?"
        img 11248
        alex_photograph "Нет, Миссис Бакфетт, она открыта..." #грустно
        img 11249
        with fade
        m "Я скоро вернусь!"

    if cloth == "WorkingOutfit1":
        img 12776
        with fade
        alex_photograph "Отлично, Миссис Бакфетт!"
        "Можете переодеваться здесь! Я не буду смотреть!"
        img 12775
        m "Я переоденусь в гримерке!"
        "Надеюсь Мелани не закрыла ее в этот раз?"
        img 12777
        alex_photograph "Нет, Миссис Бакфетт, она открыта..." #грустно
        img 12778
        with fade
        m "Я скоро вернусь!"


    img black_screen
    with Dissolve(1.0)
    sound snd_fabric1
    pause 2.0
    return

    # СТАРЫЙ КОНТЕНТ
    call ep22_photoshoot1() from _call_ep22_photoshoot1
    "Выберите наряд для фотосессии сегодня!"

    m "Я выбираю это..."
    #Если кастинг у Бифа
    menu:
        "Идти на кастинг к Бифу.":
            call ep22_dialogue6_6() from _call_ep22_dialogue6_6
        "Не идти к Бифу.":
            pass
    #fade

    #начинается фотосессия
    music Molten_Alloy
    alex_photograph "Начинайте, позировать!"
    "Мотор!"
    img black_screen
    with Dissolve(1.0)
    #фотосессия Моники обычная
#    $ add_char_progress("AlexPhotograph", photoshot2AlexProgressAmount, "photoshot_day_" + str(day))

#    call photoshop_flash() from _call_photoshop_flash

    alex_photograph "Миссис Бакфетт! Примите, пожалуйста, эту позу!"
    m "Алекс, снова ты за свое!"
    alex_photograph "Мэм! Это теперь моя работа!"
    menu:
        "Смириться с неизбежностью откровенных поз...":
            pass
        "Предложить Алексу другой вариант... (Alex, low progress) (disabled)":
            pass
    #развратные позы
    menu:
        "Продолжить делать кадры. (corruption)" if corruption >= monicaBiffWorkPhotoShot1PervertCorruptionRequired:
            $ add_char_progress("AlexPhotograph", photoshot1AlexProgressPervertAmount, "photoshot1_corruption")
            $ add_corruption(monicaBiffWorkPhotoShot1PervertCorruptionAdding, "monicaBiffWorkPhotoShot1PervertCorruptionAdding")

            alex_photograph "Мы закончили, Мэм!"
            "Хотите переодеться назад?"
        "Продолжить делать кадры. (low corruption, required [monicaBiffWorkPhotoShot1PervertCorruptionRequired]) (disabled)" if corruption < monicaBiffWorkPhotoShot1PervertCorruptionRequired:
            pass
        "Прекратить это.":
            music Stealth_Groover
            m "Я не буду так сниматься!"
            m "Мы сделали достаточно кадров!"
            alex_photograph "Хотите переодеться назад?"


    #Если кастинг у Бифа не необходим
    #Рост прогресса у Бифа
    return

label ep22_dialogue6_6:
    #render
    #Кастинг у Бифа
    #Моника в зависимости от одетой одежды

    # если Моника обещала вести себя как цыпочка
    biff "О! Цыпочка! Ты пришла?"
    "Что надо сказать?"
    "Помнишь, что ты обещала?"
    m "Цыпочка пришла на кастинг к папочке..."
    mt "Ненавижу!!!"
    biff "Молодец цыпочка!"
    # иначе
    biff "О! Цыпочка! Ты пришла?"
    m "Да, Биф! Я пришла, потому что ты заставил!"
    #

    biff "Итак, цыпочка пришла на кастинг..."
    "Чем цыпочка готова удивить папочку в этот раз?"


    mt "Мерзавец!"
    #рост прогресса у Бифа
    return

label ep22_dialogue6_7a:
    mt "Я сделала фотосессию!"
    mt "Мне надо получить деньги от Бифа!"
    return False
label ep22_dialogue6_7:
    #render
    # Моника возвращается к Бифу и спрашивает про деньги.
    music Groove2_85
    if cloth == "Whore":
        img 8298
    if cloth == "CasualDress1":
        img 11262
    if cloth == "WorkingOutfit1":
        img 12791
    with fade
    m "Биф! Я сделала фотосессию!"
    "Где мои деньги?"

    if monicaSaidBiffSheIsWillBeAGoodChick == True:
        #Если Моника хорошая цыпочка
        $ notif(t_("Моника обещала быть хорошей цыпочкой."))
        biff "Только хорошие цыпочки получают деньги от папочки!"
        "Моника хорошая цыпочка?"
        menu:
            "Моника хорошая цыпочка...":
                pass
            "Уйти без денег...":
                music Power_Bots_Loop
                if cloth == "Whore":
                    img 8290
                if cloth == "CasualDress1":
                    img 11263
                if cloth == "WorkingOutfit1":
                    img 12792

                with fade
                mt "Я лучше уйду без денег, чем скажу это снова!!!"
                return False

        if cloth == "Whore":
            img 8299
        if cloth == "CasualDress1":
            img 11264
        if cloth == "WorkingOutfit1":
            img 12793
        with fade
        m "Моника хорошая цыпочка."
        "Моника заслужила денежку..."
        mt "!!!"
        #иначе

    if monicaAskBiffGiftCertificateFirstTime == True:
        $ monicaAskBiffGiftCertificateFirstTime = False
        #Если первый раз
        img 8300
        with fade
        biff "Цыпочка! У меня нет наличных!"
        img 8301
        m "Можно купить сертификат и послать его на этот адрес..." #дает бумажку
        biff "Окей, цыпочка! Нет проблем!"
    else:
        #иначе
        if cloth == "Whore":
            img 8302
        if cloth == "CasualDress1":
            img 11265
        if cloth == "WorkingOutfit1":
            img 12794
        biff "Цыпочке купить такой же сертификат как обычно?"
        m "Да..."
        $ questHelp("office_15", True)

    $ questHelp("office_13", True)

    #fade
    img 8303
    with fade
    $ monicaEarnedWeeklyMoney = True
    $ notif(t_("Подарочный сертификат на $ 5000 отправлен Виктории"))
    biff "Все готово!"
    if cloth == "Whore":
        img 8304
    if cloth == "CasualDress1":
        img 11266
    if cloth == "WorkingOutfit1":
        img 12795
    with fade

    #
    if photoShootDisabledNextWeek == True:
        if cloth == "Whore":
            img 8293
            with fade
            biff "Да, цыпочка!"
            biff "На следующей неделе я не нуждаюсь в твоих услугах!"
            biff "Приходи позднее!"
            img 8306
            music Power_Bots_Loop
            m "КАК?!!"
            m "Биф, но ты говорил что это регулярная работа!"
            img 8293
            with fade
            biff "Это регулярная работа, цыпочка. Но на следующей неделе ты мне не нужна."
            img 8295
            with fade
            mt "Дьявол! Где же я достану деньги для Виктории!"
            music Groove2_85
            img 8305
            with fade
            m "Биф, хорошо, но мне все-равно нужны деньги..."
            img 8294
            biff "Цыпочка! Ты начинаешь утомлять папочку!"
            biff "Тебя что-то не устраивает? Ты хочешь разорвать наше соглашение?"
            img 8287
            with fade
            m "Нет... Биф..."
            img 8288
            m "В этом нет... необходимости"
        if cloth == "CasualDress1":
            img 11267
            with fade
            biff "Да, цыпочка!"
            biff "На следующей неделе я не нуждаюсь в твоих услугах!"
            biff "Приходи позднее!"
            img 11268
            music Power_Bots_Loop
            m "КАК?!!"
            m "Биф, но ты говорил что это регулярная работа!"
            img 11267
            with fade
            biff "Это регулярная работа, цыпочка. Но на следующей неделе ты мне не нужна."
            img 11269
            with fade
            mt "Дьявол! Где же я достану деньги для Виктории!"
            music Groove2_85
            img 11270
            with fade
            m "Биф, хорошо, но мне все-равно нужны деньги..."
            img 8294
            biff "Цыпочка! Ты начинаешь утомлять папочку!"
            biff "Тебя что-то не устраивает? Ты хочешь разорвать наше соглашение?"
            img 11271
            with fade
            m "Нет... Биф..."
            img 11272
            m "В этом нет... необходимости"

        if cloth == "WorkingOutfit1":
            img 12796
            with fade
            biff "Да, цыпочка!"
            biff "На следующей неделе я не нуждаюсь в твоих услугах!"
            biff "Приходи позднее!"
            img 12797
            music Power_Bots_Loop
            m "КАК?!!"
            m "Биф, но ты говорил что это регулярная работа!"
            img 12796
            with fade
            biff "Это регулярная работа, цыпочка. Но на следующей неделе ты мне не нужна."
            img 12798
            with fade
            mt "Дьявол! Где же я достану деньги для Виктории!"
            music Groove2_85
            img 12799
            with fade
            m "Биф, хорошо, но мне все-равно нужны деньги..."
            img 8294
            biff "Цыпочка! Ты начинаешь утомлять папочку!"
            biff "Тебя что-то не устраивает? Ты хочешь разорвать наше соглашение?"
            img 12800
            with fade
            m "Нет... Биф..."
            img 12801
            m "В этом нет... необходимости"
label ep22_dialogue6_7b:
    menu:
        "Ты что-то говорил по поводу работы в офисе?" if monicaWorkingAtBiffOffice == False:
            if cloth == "Whore":
                img 8305
                with fade
                m "Ты что-то говорил по поводу работы в офисе?"
                biff "Да, когда ты станешь очень хорошей цыпочкой, я возьму тебя сюда в офис!"
                "Ты полезная кукла, я смогу продавать тебя здесь!"
                img 8306
                m "Что значит продавать меня???"
                img 8307
                biff "Торговать твоим личиком!"
                "Ты ведь похожа на Монику Бакфетт!"
                "Ты наверное уже забыла!"
                "Ха-Ха-Ха!"
                img 8290
                mt "!!!"
                img 8308
                with fade
                biff "Но, может быть и не только личиком!"
                "Думаю многие партнеры готовы будут неплохо заплатить, чтобы запустить свои пальчики..."
                "В киску Моники Бакфетт!"
                "И не только пальчики!"
                "Ха-Ха-Ха!"
                "И все будут думать что ты настоящая!"
                img 8309
                mt "!!!"
                img 8308
                biff "Тебе это очень понравится!"
                "Ты будешь заниматься тем же самым чем занимаешься на улице сейчас..."
                "Только будешь значительно больше получать за это!"
                img 8310
                with fade
                m "Нет, Биф!"
                "Давай пока ограничимся личиком!"
                img 8311
                biff "Без проблем, крошка!"
                "Все-равно тебе еще надо заработать это доверие!"
                "А это значит быть хорошей цыпочкой!"
                img 8312
                biff "К тому же, тебе придется значительно чаще развлекать меня."
                "Проводить кастинги."
                "И придумывай что-нибудь новое почаще!"
                "Папочке может наскучить однообразная цыпочка!"
                img 8313
                with fade
                mt "!!!"
                m "Я могу идти?"
                biff "Да, цыпочка! Иди!"
            if cloth == "CasualDress1":
                img 11273
                with fade
                m "Ты что-то говорил по поводу работы в офисе?"
                biff "Да, когда ты станешь очень хорошей цыпочкой, я возьму тебя сюда в офис!"
                "Ты полезная кукла, я смогу продавать тебя здесь!"
                img 11274
                m "Что значит продавать меня???"
                img 11275
                biff "Торговать твоим личиком!"
                "Ты ведь похожа на Монику Бакфетт!"
                "Ты наверное уже забыла!"
                "Ха-Ха-Ха!"
                img 11276
                mt "!!!"
                img 8308
                with fade
                biff "Но, может быть и не только личиком!"
                "Думаю многие партнеры готовы будут неплохо заплатить, чтобы запустить свои пальчики..."
                "В киску Моники Бакфетт!"
                "И не только пальчики!"
                "Ха-Ха-Ха!"
                "И все будут думать что ты настоящая!"
                img 11277
                mt "!!!"
                img 8308
                biff "Тебе это очень понравится!"
                "Ты будешь заниматься тем же самым чем занимаешься на улице сейчас..."
                "Только будешь значительно больше получать за это!"
                img 11278
                with fade
                m "Нет, Биф!"
                "Давай пока ограничимся личиком!"
                img 11279
                biff "Без проблем, крошка!"
                "Все-равно тебе еще надо заработать это доверие!"
                "А это значит быть хорошей цыпочкой!"
                img 8312
                biff "К тому же, тебе придется значительно чаще развлекать меня."
                "Проводить кастинги."
                "И придумывай что-нибудь новое почаще!"
                "Папочке может наскучить однообразная цыпочка!"
                img 11280
                with fade
                mt "!!!"
                m "Я могу идти?"
                biff "Да, цыпочка! Иди!"
            return True

        "Биф... Мог бы ты дать еще немного денег?":
            call ep23_dialogues1() from _call_ep23_dialogues1
            jump ep22_dialogue6_7b

        "Уйти.":
            pass
    if cloth == "Whore":
        img 8288
    if cloth == "CasualDress1":
        img 11251
    if cloth == "WorkingOutfit1":
        img 12780
    with diss
    m "Я могу идти?"
    biff "Да, цыпочка! Иди!"
    return True
