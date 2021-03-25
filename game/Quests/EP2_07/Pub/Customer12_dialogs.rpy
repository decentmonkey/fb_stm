default customer12_dance_comment_stage = 0

# мужик который выглядит как баба
default customer12_serve1_event1_count = 0
label customer12_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14412
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    img 14413
    with diss
    w
    sound Jump1
    img 14414
    with diss
    w
    img 14415
    with fade
    customer12 "А время зря не теряет..."
    customer12 "Как зовут?"
    img 14416
    with diss
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14417
    with fade
    customer12 "Сколько стоят твои сиськи, [monica_pub_name]?"
    customer12 "Думаю, сколько приготовить тебе на чай. Я плачу 1 процент от цены сисек."
    music Power_Bots_Loop
    img 14418
    with hpunch
    m "Вы о чем? Они не продаются!"
    img 14419
    with fade
    customer12 "Не обмынывай! Ну дак что, сколько ты заплатила за операцию?"
    img 14420
    m "Они настоящие!"
    music Groove2_85
    img 14421
    with fade
    customer12 "Ну да, значит твои чаевые составят ноль долларов. Хотя кто знает..."
    customer12 "Другая официантка получает по 3 доллара, имей ввиду..."
    img 14422
    with diss
    mt "О чем ты вообще? Лучше бы я к тебе не подходила!"
    img 14424
    with fade
    customer12 "И это только за сиськи. А ведь есть еще и зад..."
    customer12 "Какая-то ты не разговорчивая для первого раза... Тогда и я ничего не буду заказывать..."
    img 14423
    with diss
    mt "Похоже, половина посетителей этого бара ненормальные..."
    return

label customer12_serve1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14438
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer12_dance_comment_stage == 1:
        customer12 "О, это ты! Слушай, а как насчет привата?"
        m "Я не танцую приват... И на сцене не танцую."
        customer12 "Я это уже слышал... Аха-ха!!!"
        customer12 "Хорош уже строить из себя невинную цыпочку!"
        customer12 "Сколько за приват?"
        mt "?!"
        m "Я не танцую приват!"
        customer12 "А зря! Могла бы хорошо заработать!"
        customer12 "Ладно, думаю, это временно. Скоро ты передумаешь."
        mt "!!!"
        mt "Ни за что не пойду в приват!"
        mt "За кого он меня принимает?!"


    if monicaStartedStripDanceFlag == True and customer12_dance_comment_stage == 0:
        customer12 "Эй, ты же у пилона теперь сиськами трясешь!"
        customer12 "Или ты здесь на двух работах?"
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer12 "Ну конечно! Я что, слепой что-ли?!"
        m "Я просто официантка..."
        customer12 "Ну ладно. Не хочешь - не говори."
        customer12 "Только на сцене в следующий раз танцуй без этих своих шмоток."
        m "!!!"
        customer12 "Тогда не придется подрабатывать официанткой."
        customer12 "За такие сиськи чаевых много будут платить."
        mt "Фу, как грубо!"
        mt "По-моему, здесь все такие грубияны!"
        mt "!!!"
        mt "Как мне надоела эта дыра!"
        $ customer12_dance_comment_stage = 1

    #


    m "Здравствуйте, что будете заказывать?"
    img 14439
    with diss
    customer12 "Пиво, бургер и ваш изумительный харчо!"
    img 14440
    with diss
    m "Да, хорошо, сейчас сделаем."
    # разворачивается спиной , кастомер бьет ее по жопе + звук шлепка
    sound snd_slap1
    img 14441
    with hpunch
    sound_from_side "(шлепок)"
    img 14442
    customer12 "Вот именно поэтому ты получаешь чаевые!"
    img 14443
    with diss
    $ menu_corruption = [0, pubCustomer12_serve1_Corruption]
    menu:
        "Какого?!":
            music Power_Bots_Loop
            img 14444
            with fade
            m "Еще раз так сделаешь, и тебе не сдобровать!"
            img 14445
            with diss
            customer12 "Оу, какая ты злая, оказывается..."
            customer12 "Давай, неси уже мой заказ!"
            customer12 "И кстати, ты только что обнулила свои чаевые."
            # уходит за заказом, приходит, ставит на стол
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Groove2_85
            sound snd_plates1
            img 14446
            with fade
            w
            sound snd_beer_table
            img 14447
            with diss
            w
            img 14448
            with fade
            customer12 "Можешь идти. Если в следующий раз не будешь грубить, получишь пару долларов."
            img 14449
            with diss
            mt "Идиот..."
            return False
        "Проигнорировать.":
            $ customer12_serve1_event1_count += 1
            music Hidden_Agenda
            img 14451
            with fade
            mt "И не только поэтому..."
            img 14452
            with diss
            customer12 "Постарайся сделать так, чтобы я получил свой заказ как можно скорее."
            # уходит за заказом, ставит на стол
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Hidden_Agenda
            sound snd_plates1
            img 14446
            with fade
            w
            sound snd_beer_table
            img 14447
            with diss
            w
            img 14450
            with diss
            customer12 "Как раз вовремя! Молодчина!"
            $ add_tips(2.0)
            customer12 "Вот, держи! Доллар за скорость и доллар за твою попку!"
            customer12 "Что стоишь? Иди, не заставляй клиентов ждать!"
            $ add_corruption(5, "pubCustomer12_serve1_Corruption")
            return True

label customer12_afterserve1:
    mt "Я с трудом переношу эту кошмарную работу..."
    return
