# парень на переднем плане

default customer4_dance_comment_stage = 0

label customer4_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14320
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14321
    with diss
    customer4 "Оу! Какая красивая мордашка! Новенькая?"
    # смотрит на монику
    music Groove2_85
    img 14322
    with diss
    m "Кто, Я?!"
    img 14323
    with fade
    customer4 "Нет, твоя мордашка! Ну конечно же ты!"
    customer4 "Мда... Понятно почему ты официантка."
    customer4 "Как зовут? Только не спрашивай кого..."
    img 14324
    mt "Он что, думает, что Я глупая?"
    mt "Я?!"
    img 14325
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14326
    with fade
    customer4 "Отлично, [monica_pub_name]! Я не буду говорить как меня зовут, и даже делать заказ."
    customer4 "Ты новенькая, не уверен, что эта информация уместится в твоей красивой головке."
    customer4 "Можешь идти, увидимся!"
    img 14327
    with diss
    mt "Почему он так со мной разговаривает? Я не глупая!"
    return

label customer4_serve1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14328
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer4_dance_comment_stage == 1:
        customer4 "А вот и официанточка, она же стриптизерша!"
        m "Я не стритизерша."
        customer4 "Ну, конечно! Еще скажи, что я снова перепутал."
        customer4 "Ты думала, в маске никто не узнает, кто ты на самом деле?"
        mt "???"
        mt "Он... узнал... м-меня?"
        mt "!!!"
        customer4 "Ты боишься, если узнают, что ты еще и официанткой тут работаешь, то приставать будут?"
        customer4 "Ладно. Я не скажу никому. Притворяйся дальше."
        mt "Как же этот придурок напугал меня!"
        mt "Фу-у-у... Что-то с нервами у меня совсем непорядок!"
        m "..."


    if monicaStartedStripDanceFlag == True and customer4_dance_comment_stage == 0:
        customer4 "Эй, отлично выступаешь на сцене!"
        m "Вы меня с кем-то путаете."
        m "Я здесь не танцую."
        customer4 "Я не могу тебя с кем-то путать. Я тебя видел на сцене!"
        m "Я не танцую на сцене."
        customer4 "Хммм... Странно..."
        mt "!!!"
        mt "Какое ему дело до этого?!"
        $ customer4_dance_comment_stage = 1

    #

    m "Вам что-нибудь принести?"
    img 14329
    with diss
    customer4 "Да! Принеси мне пива и Ваш восхитительный Shiny бургер!"
    img 14330
    with diss
    m "Да, конечно."
    img 14331
    with fade
    customer4 "Запомнила? Одно пиво и Shiny бургер. Не харчо и не пасту!"
    music Groove2_85
    img 14332
    m "Я поняла!"
    img 14333
    customer4 "Я надеюсь..."
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14334
    with fade
    w
    sound snd_plates1
    img 14335
    with diss
    w
    sound snd_beer_table
    img 14336
    with diss
    m "Вот, пожалуйста!"
    img 14337
    with fade
    customer4 "Ой, какая молодец! Все как надо!"
    $ add_tips(1.0)
    customer4 "Держи доллар за красивую мордашку! А если улыбнешься, дам два!"
    img 14338
    with diss
    $ menu_corruption = [pubCustomer4_serve1_Corruption]
    menu:
        "Улыбнуться.":
            music Hidden_Agenda
            img 14339
            with diss
            mt "Доллар за одну улыбку... Чтож, пускай..."
            mt "Он не знает что я буду думать, пока улыбаюсь ему..."
            music Loved_Up
            img 14340
            with fadelong
            w
            mt "Придурок..."
            w
            img 14341
            with diss
            $ add_tips(1.0)
            customer4 "Какая умничка, держи еще доллар!"
            $ add_corruption(2, "pubCustomer4_serve1_Corruption")
            return
        "Не улыбаться.":
            # стоит с каменным лицом
            music Groove2_85
            img 14342
            with fade
            mt "С чего бы мне улыбаться этой деревенщине?"
            img 14343
            with diss
            m "..."
            img 14344
            with diss
            customer4 "Не хочешь? Это все потому, что ты тут недавно..."
            return

label customer4_afterserve1:
    mt "Глупый пингвин..."
    return
