default customer10_dance_comment_stage = 0

label customer10_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14359
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    sound snd_whistle1
    img 14360
    with diss
    w
    music Groove2_85
    img 14361
    with fade
    customer10 "Да! Я желаю Вас. Сколько?"
    music Power_Bots_Loop
    img 14362
    with hpunch
    m "Что? Вы это о чем? Я не продаюсь!"
    img 14363
    with diss
    customer10 "Серьезно? У всего есть цена..."
    customer10 "Как тебя зовут?"
    music Groove2_85
    img 14364
    with fade
    m "Меня зовут [monica_pub_name]."
    img 14365
    with diss
    customer10 "Любопытно... [monica_pub_name] - это сценическое имя или настоящее?"
    img 14366
    mt "Почему он спрашивает?"
    img 14367
    with diss
    m "Конечно настоящее!"
    img 14368
    with fade
    customer10 "Правда? Я думаю, тебе бы больше пошло имя Анжелина! Или Виолетта!"
    customer10 "Что думаешь?"
    img 14369
    with diss
    m "Ничего... Мне мое имя нравится..."
    img 14370
    with diss
    customer10 "А мне вот что-то не очень... Надо бы тебе придумать другое имя...Подумай над этим!"
    customer10 "А пока принеси мне что-нибудь выпить!"
    img 14371
    with diss
    m "Да, хорошо."
    # уходит приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14372
    with fade
    w
    sound snd_plates1
    img 14373
    with diss
    w
    sound snd_beer_table
    img 14374
    with diss
    customer10 "А...Виолетта! Наконец то!"
    music Groove2_85
    img 14375
    m "Я не Виолетта..."
    img 14376
    with diss
    customer10 "Это не важно, но важно то, что я тут постоянный клиент и советую тебе это запомнить, Виолетта!"
    customer10 "Но я могу тебя звать и Новенькая... Что думаешь?"
    img 14377
    mt "Что ты урод!"
    img 14378
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14379
    with fade
    customer10 "Да, Виолетта, я помню!"
    customer10 "Кстати, спасибо за выпивку. Еще увидимся."
    img 14380
    with diss
    mt "Надеюсь, нескоро."
    return

label customer10_serve1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14359
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer10_dance_comment_stage == 1:
        customer10 "Новенькая, ты мне сказала, что не танцуешь..."
        m "Не танцую."
        customer10 "Я тебя видел на сцене..."
        m "Вы меня перепутали с кем-то..."
        customer10 "Это врядли. По-моему, ты меня обманываешь."
        m "Нет. Я здесь работаю официанткой."
        customer10 "Я спрошу у Джо насчет тебя..."
        mt "!!!"


    if monicaStartedStripDanceFlag == True and customer10_dance_comment_stage == 0:
        customer10 "А, новенькая, это ты..."
        customer10 "Сколько за приват берешь?"
        m "!!!"
        m "Я не танцую ни на сцене, ни в привате."
        customer10 "Разве? Хммм..."
        m "Да..."
        mt "Как мне надоели все эти неудачники!"
        mt "!!!"
        $ customer10_dance_comment_stage = 1

    #


    m "Вам что-нибудь принести?"
    img 14368
    with diss
    customer10 "Да, новенькая! Как ты помнишь, я тут постоянный клиент."
    img 14377
    m "?"
    img 14361
    with diss
    customer10 "И знаешь, все официантки здесь еще и танцуют!"
    music Groove2_85
    img 14362
    with diss
    m "Впервые об этом слышу..."
    img 14365
    with fade
    customer10 "Очень странно, но уж мне то ты можешь поверить!"
    customer10 "Знаешь, давай так: 100 баксов и ты лезешь на пилон!"
    customer10 "Пойми, делаю это только ради тебя!"
    customer10 "Как насчет танца?"
#    mt "100 долларов?! И возможно не придется их отдавать..."
    img 14380
    with diss
    mt "100 долларов?! За один танец на пилоне..."
    mt "Да он нормальный, предлагать такое МНЕ?!"
    menu:
#        "Хорошо, давай деньги.(disabled)":
#            return
        "Я не из таких!":
            music Power_Bots_Loop
            img 14367
            with fade
            m "Знаешь что, Я не танцую!"
            img 14376
            with diss
            customer10 "Не правда, это лишь вопрос времени."
            customer10 "Кстати, забыл, как тебя зовут?"
            music Groove2_85
            img 14375
            with fade
            m "[monica_pub_name]"
            customer10 "Отлично! Я уже вижу тебя на сцене!"
            m "Этого не будет."
            img 14376
            with diss
            customer10 "А заказывать я ничего не буду, у меня все есть!"
            return

label customer10_afterserve1:
    mt "Озабоченный извращенец... Тут, похоже, все такие..."
    return
