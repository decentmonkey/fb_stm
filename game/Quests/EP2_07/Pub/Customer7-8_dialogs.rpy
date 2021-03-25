# 2 парня у шеста

default customer78_dance_comment_stage = 0

label customer78_1stmeeting:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music RocknRoll_loop
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14453
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14425
        with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14426
    with diss
    customer7 "Заказ? Да, готовы, но мы скажем, что мы хотим официантке, а Ты поднимайся! Надоело уже смотреть на эту стриптизершу."
    # смотрит на монику
    img 14427
    with diss
    m "Я и есть официантка..."
    img 14428
    with fade
    customer7 "Да? Да быть не может! Ты гораздо эффектнее смотрелась бы на пилоне!"
    customer7 "Ты новенькая?"
    customer7 "Как тебя зовут?"
    img 14429
    with diss
    m "Да, я тут недавно. Меня зовут [monica_pub_name]"
    img 14430
    with fade
    customer7 "[monica_pub_name], ты хочешь заработать?"
    img 14431
    with diss
    mt "Да я зарабатываю побольше, чем вся твоя семья и твой товарищ, и все их родственники во всем мире!"
    img 14432
    with diss
    m "Да, именно за этим я здесь."
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14454
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14433
        with fadelong
    customer7 "Я так и думал... Просто для информации: гораздо больше можно заработать тут.." # показывает на шест
    img 14434
    with diss
    m "Мне это не интересно."
    img 14435
    with fade
    customer7 "Да, да, все так говорят, пока не узнают какие тут деньги..."
    img 14437
    mt "Неужели и правда большие?"
    img 14455
    with diss
    menu:
        "И какие же?":
            img 14456
            with fade
            m "И какие же?"
            img 14457
            with fade
            customer7 "Ну за представление можно заработать 100 долларов..."
            customer7 "Но все зависит от того, что ты покажешь..."
            img 14458
            m "Я поняла, мне это неинтересно."
            img 14459
            with diss
            mt "100 долларов за вечер? Немаленькие деньги для такой дыры..."
            mt "Но это не для меня! Я не собираюсь танцевать у всех на виду!"
            pass
        "Мне это не интересно.":
            img 14460
            with fade
            m "Говорю же, мне это не интересно."
            img 14461
            with diss
            customer7 "Конечно, конечно, это пока..."
            pass
    img 14462
    with fade
    customer7 "А пока, принеси нам два шота! На свой вкус."
    img 14463
    with diss
    m "Хорошо."
    # уходит принтсит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music RocknRoll_loop
    img 14464
    with fade
    w
    img 14465
    with diss
    w
    sound snd_plates1
    img 14466
    with diss
    w
    sound snd_beer_table
    img 14467
    with fade
    customer7 "То что надо! Похоже, ты умеешь читать мысли!"
    $ add_tips(1.0)
    customer7 "Вот, держи!" # дает доллар
    customer7 "Приходи к нам чаще! Я вижу в тебе потенциал."
    img 14468
    mt "Какой еще потенциал?"
    img 14469
    with diss
    m "До свидания."
    return

label customer78_serve1:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music RocknRoll_loop

    img 14470
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer78_dance_comment_stage == 1:
        customer7 "Эй, детка! Когда уже разденешься на сцене?!"
        m "Я... Я не танцую..."
        customer7 "Мы это уже слышали. Не танцует она! Аха-ха!!!"
        customer7 "Запомни: чем меньше одежды на сцене, тем больше чаевые!"
        m "!!!"
        mt "Похотливые животные! Ненавижу!"
        m "Я..."
        customer7 "А если пойдешь с нами в приват, то заработаешь раз в десять больше!"
        m "Я не танцую!"
        mt "!!!"
        customer7 "А если будешь работать официанткой с голыми сиськами..."
        customer7 "То чаевых будет еще больше! Аха-ха!!!"
        mt "!!!"



    if monicaStartedStripDanceFlag == True and customer78_dance_comment_stage == 0:
        customer7 "О, детка! Правильно сделала, что послушалась нашего совета!"
        m "Какого совета?"
        customer7 "Отпадные сиськи! На сцене выглядишь охренительно!"
        m "Я официантка, а не стриптизерша..."
        customer7 "Конечно, конечно... А то я тебя не разглядел на сцене отсюда!"
        m "Я..."
        customer7 "В следующий раз снимай с себя все эти тряпки на сцене."
        customer7 "Если хочешь заработать хорошие чаевые."
        mt "!!!"
        $ customer78_dance_comment_stage = 1

    #


    m "Что будете..."
    img 14471
    with diss
    customer7 "Нам два шота! И быстро! Хотим их выпить перед очередным выступлением!"
    img 14472
    with diss
    m "Хорошо, один момент!"
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14464
    with fade
    w
    img 14465
    with diss
    w
    sound snd_plates1
    img 14466
    with diss
    w
    sound snd_beer_table
    img 14473
    with diss
    m "Вот, пожалуйста! Что-нибудь еще?"
    img 14474
    with fade
    customer7 "Да, вот еще что! Не могла бы ты в следующия раз быть побыстрее!"
    customer7 "Похоже тебя сюда взяли по двум причинам. Эти причины: сиськи и жопа! Но уж точно не скорость!"
    music RocknRoll_loop
    img 14467
    with diss
    w
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14454
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14433
        with fadelong
    customer7 "А теперь иди, шоу уже началось!"
    img 14475
    with diss
    mt "Козлы..."
    return

#label customer78_serve2:
#    m "Здравствуйте, Вы готовы сделать заказ?"
#    customer7 "О, новенькая! Ты знаешь, у нас с товарищем небольшая проблема."
#    customer7 "Ты же знаешь, что у вас при покупке двух шотов третий в подарок?"
#    customer7 "А нас, как ты видишь двое...Выпей с нами!"
#    m "Вы можете купить четыре шота, Вам принесут шесть и Вы их сможете выпить вдвоем."
#    m "И мне нельзя пить на работе."
#    customer7 "Да брось, детка! Напомни, тебя как зовут?"
#    mt "Может быть стоит быть с ними полюбезнее, тогда они оставят на чай..."
#    m "[monica_pub_name]"
#    customer7 "Отлично, [monica_pub_name]! Ну дак что, выпьешь с нами? Ты ведь любишь чаевые?"
#    mt "Конечно, я не фанат алкоголя, но что может быть от одного шота? К тому же они дадут чаевые..."
#    mt "Хотя может быть не стоит, я довольно давно не пила..."
#    menu:
#        "Хорошо, я выпью с Вами.":
#            m "Хорошо, я выпью с Вами."
#            customer7 "Вот и славно!"
#            # обращается к 8
#            customer7 "Эй, дружище, сбегай к стойке за шотами."
#            # 8 отходит, возвращается, с 3 маленькими шотами
#            customer7 "Отлично! Ну что, выпьем?"
#            # пьют моника морщится
#            customer7 "Что, не понравился Shiny шот?! Ха-ха-ха!"
#            customer7 "А по-моему он прекрасен!"
#            m "Что-нибудь еще?"
#            customer7 "Да, тебя!"
#            m "Что?"
#            customer7 "Ха-ха-ха! Ладно, я пошутил, больше ничего не нужно!"
#            customer7 "Вот, держи." # дает 10 баксов
#            mt "Десять долларов? Маловато..."
#            return
#        "Я на работе, мне нельзя.":
#            m "Я на работе, мне нельзя."
#            customer7 "Ууу... Какая ты правильная... Тогда нам два пива!"
#            m "Хорошо."
#            # уходит за пивом, приносит.
#            m "Вот, пожалуйста."
#            customer7 "Можешь идти!"
#            mt "Да, свои чаевые я не получила... Возможно стоило согласиться на их предложеине?"
#            return

label customer78_afterserve1:
    mt "Два козла!"
    return
