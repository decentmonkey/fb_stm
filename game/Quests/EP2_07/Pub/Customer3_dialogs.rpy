# скучающий чувак у шеста
default customer3_1stmeetingEvent1Count = 0
default customer3_1stmeetingEvent2Count = 0
default customer3_serve2Event1Count = 0
default customer3_serve2Event2Count = 0

default customer3_dance_comment_stage = 0

default customer3_after_private = False
default customer3_after_private_agree_count = 0

label customer3_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14261
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    music Groove2_85
    img 14262
    with vpunch
    customer3 "Ого! Вот это дамочка!"
    # смотрит на монику
    img 14263
    with fade
    customer3 "У тебя должна быть прекрасная попка!"
    customer3 "Но ничего, сейчас ты пойдешь мне за заказом и я ее рассмотрю."
    customer3 "В общем мне пиво. Давай, поворачивайся уже!"
    img 14264
    mt "Вот извращенец."
    mt "Хотя откуда могут быть нормальные люди в этой дыре?"
    img 14265
    with diss
    m "Что к пиву?"
    img 14269
    with diss
    customer3 "Ничего, давай уже!"
    # поворачивается
    sound highheels_short_walk
    img 14266
    with diss
    w
    sound Jump1
    img 14267
    with diss
    w
    sound snd_whistle1
    img 14268
    with diss
    customer3 "Да! Я знал! Ай да жопа!"
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14270
    with fade
    w
    sound snd_plates1
    img 14271
    with diss
    w
    sound snd_beer_table
    img 14272
    with diss
    m "Вот, пожалуйста."
    music Groove2_85
    img 14273
    with fade
    customer3 "О да! Жду твою жопу на пилоне!"
    img 14264
    with diss
    mt "Не дождешься..."
    return

label customer3_serve1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14274
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 1:
        customer3 "Так что? Надумала насчет моего предложения?"
        m "Какого предложения? Вы что-то хотели заказать?"
        customer3 "Тебя хочу. Сколько будет стоит?"
        mt "Моника, спокойно. Просто очередной пьяница. Их тут целый паб."
        m "Я работаю официанткой и меня нельзя заказать."
        customer3 "А если я тебе щедро заплачу?"
        mt "Отдашь всю свою зарплату за год? Думаю, даже этого будет недостаточно."
        mt "Таким неудачникам, как ты, можно только мечтать обо мне."
        mt "И не только неудачникам... Вообще всем!"
        m "Вы меня с кем-то путаете."
        customer3 "Я спрошу у Джо..."
        mt "!!!"

    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 0:
        customer3 "Я думал, ты уже не официанткой здесь работаешь... "
        customer3 "Твоя задница со сцены смотрится отлично."
        m "Вы меня с кем-то путаете."
        m "Я просто официантка..."
        customer3 "Я хорошо запоминаю задницы. И твою я отлично помню."
        customer3 "Сколько стоит приват? Я заплачу."
        m "Я не танцую здесь на сцене. Тем более, не танцую при..."
        customer3 "Окей. Можешь дальше врать, мне все равно."
        customer3 "Как надумаешь насчет приват танца, знаешь, где меня найти."
        mt "!!!"
        mt "Он что о себе возомнил?!"
        mt "Всего лишь очередной неудачик, который спускает все свои деньги на шлюх и пиво!"
        $ customer3_dance_comment_stage = 1

    #

    m "Что будете заказывать?"
    img 14275
    with diss
    customer3 "Возможно, что-то и буду..."
    customer3 "Для начала, давай поговорим, а то скучно."
    img 14276
    with diss
    menu:
        "Хорошо.":
            music Hidden_Agenda
            img 14277
            with fade
            m "Хорошо."
            img 14278
            with diss
            mt "Похоже лучше поговорить с этим придурком, иначе он разольет пиво или что-нибудь еще..."
#            mt "Нмчего же не произойдет, если я с ним немного поговорю."
            $ customer3_1stmeetingEvent1Count += 1
            pass
        "Мне некогда.":
            music Groove2_85
            img 14279
            with fade
            m "Мне некогда."
            img 14280
            with diss
            customer3 "Я клиент. И я могу сказать Джо, что ты не выполняешь мои просьбы."
            img 14281
            m "Но разговоры не входят в обязанности официантки!"
            img 14282
            with diss
            customer3 "Верно. Но тебе же нужны чаевые?"
            img 14278
            with fade
            mt "Мне противно, но если он даст чаевые, может и стоит потерпеть его дурной язык. Но только совсем чуть-чуть..."
#            mt "Здесь он прав, перекинусь с ним парой фраз..."
            img 14277
            with diss
#            m "Хорошо, немного поговрим."
            m "Хорошо, говори..."
            $ customer3_1stmeetingEvent2Count += 1
            pass

    img 14283
    with fade
    customer3 "Напомни, как тебя зовут?"
    img 14284
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14285
    with fade
    customer3 "Очень приятно. Хотя это не важно, я не запомню. И кем ты работаешь, [monica_pub_name]?"
    music Groove2_85
    img 14286
    mt "Он что, издевается?"
    img 14287
    with diss
    m "Вы не видите? Я официантка."
    img 14288
    with fade
    customer3 "Да, я это вижу! [monica_pub_name] - официантка и я Билли - директор фирмы."
    img 14278
    with diss
    mt "Да что ты знаешь обо мне?"
    img 14289
    with fade
    customer3 "Наверняка ты хотела стать актрисой.... Или нет, моделью! А возможно ты мечтала создать модный журнал?"
    img 14290
    mt "Я его уже создала!"
    img 14291
    with fade
    customer3 "Но нет, ты [monica_pub_name] - официантка. И знаешь, [monica_pub_name]... Принеси мне бургер."
    img 14292
    with diss
    m "Хорошо."
    # поворачивается
    sound highheels_short_walk
    img 14293
    with diss
    w
    sound Jump1
    img 14294
    with diss
    w
    sound snd_whistle1
    img 14295
    with diss
    customer3 "И жопа у тебя просто отпад!"
    img 14296
    with diss
    mt "Извращенец..."
    # приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14345
    with fade
    w
    sound snd_plates1
    img 14346
    with diss
    w
    sound snd_beer_table
    img 14347
    with diss
    w
    img 14348
    with diss
    $ add_tips(1.0)
    customer3 "Молодец, красивая жопа! Вот тебе целый доллар! Купи себе помаду!"
    img 14258
    with diss
    mt "Какой же он мерзкий..."
    return

label customer3_serve2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14249
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 1:
        customer3 "А, это ты?"
        customer3 "Пойдем в приват?"
        m "Я не танцую. Тем более, приват!"
        customer3 "А если я тебе щедро заплачу?"
        mt "Таким неудачникам, как ты, можно только мечтать обо мне."
        mt "И не только неудачникам... Вообще всем!"
        m "Вы меня с кем-то путаете."
        customer3 "Я спрошу у Джо..."
        mt "!!!"

    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 0:
        customer3 "Твоя задница со сцены смотрится отлично."
        m "Вы меня с кем-то путаете."
        m "Я просто официантка..."
        customer3 "Я хорошо запоминаю задницы. И твою я отлично помню."
        m "Я не танцую здесь на сцене."
        customer3 "Можешь дальше врать, мне все равно."
        mt "!!!"
        mt "Он что о себе возомнил?!"
        $ customer3_dance_comment_stage = 1

    #

    m "Вам что-нибудь принести?"
    img 14250
    with diss
    customer3 "Скучно мне..."
    img 14251
    with diss
    m "Может быть пиво?"
    img 14252
    with fade
    customer3 "Да ну его..."
    customer3 "Мне все надоело... Стриптизерши одни и те же изо дня в день, скучно..."
    customer3 "Но ты тут недавно... Как тебя зовут?"
    img 14253
    with diss
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14254
    with fade
    customer3 "Ага, ну и ладно, я все равно не запомню..."
    customer3 "Я вообще не запоминаю имена женщин, я запоминаю их жопы. И твою я запомнил!"
    customer3 "Как насчет танца?"
    img 14255
    with diss
    menu:
        "Не сегодня.":
            img 14256
            with fade
            m "Я официатка, стриптизом занимаются другие."
            img 14257
            with diss
            customer3 "Да знаю я, что другие. Но их я уже видел не один раз..."
            customer3 "Ладно, проваливай, никакого толку от тебя."
            img 14258
            with diss
            mt "Какого черта ты тут вообще сидишь, если ничего не заказываешь?"
            $ customer3_serve2Event1Count += 1
            return
        "Я что, похожа на стриптизершу?":
            music Power_Bots_Loop
            img 14259
            with fade
            m "Я что, похожа на стриптизершу?"
            m "Даже не вздумай меня спрашивать о таком!"
            img 14260
            with diss
            customer4 "Мда, скучно... А ты еще и грубиянка... Думаю, стоит рассказать об этом Джо."
            customer4 "Или не стоит... Что-то совсем лениво."
            customer4 "Иди отсюда! Клиенты ждут!"
            img 14258
            with diss
            mt "Козел!"
            $ customer3_serve2Event2Count += 1
            return

label customer3_after_serve1:
    mt "Ненавижу это место!"
    return
