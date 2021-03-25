default customer5_dance_comment_stage = 0

label customer5_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14298
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    customer5 "Какая красота! И давно ли ты тут?"
    # смотрит на монику
    img 14299
    with fade
    m "Я? Всего пару дней..."
    music In_Your_Arms
    img 14300
    with diss
    customer5 "Ой как хорошо! Теперь я буду бывать здесь еще чаще!"
    customer5 "Скажи, у тебя есть парень?"
    customer5 "Или нет... Где же мои манеры? Как тебя зовут?"
    img 14301
    mt "Не хватало еще, чтобы ко мне подкатывал какой-то кретин..."
    img 14302
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14303
    with fade
    customer5 "Ох... [monica_pub_name] и Джери...Шикарно звучит..."
    customer5 "Мне надо все обдумать... Лучше всего это делается за пивом..."
    customer5 "Да, ты не ответила на мой вопрос: У тебя есть парень?"
    img 14304
    with diss
    m "Вообще-то я замужем."
    # смотрит на моникт руку
    img 14305
    with diss
    w
    img 14306
    with fade
    customer5 "Понятно, ты врешь, кольца нет, значит ты свободна!"
    customer5 "У меня все шансы!"
    customer5 "В общем, мне пива!"
    music Groove2_85
    img 14301
    mt "Еще чего... Размечтался... Ему никогда не светит такая леди, как Я!"
    img 14307
    with diss
    m "Хорошо."
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Groove2_85
    img 14308
    with fade
    w
    sound snd_plates1
    img 14309
    with diss
    w
    sound snd_beer_table
    img 14310
    with diss
    m "Пожалуйста."
    music In_Your_Arms
#    img 14311
#    with fade
    img 14312
    with diss
    customer5 "Да, спасибо. Можешь идти."
    $ add_tips(1.0)
    customer5 "Хотя стоп...Где же мои манеры? Вот тебе доллар. Скоро заработаешь себе на платье."
    img 14313
    with diss
    mt "Изысканные манеры... Фи!"
    return

label customer5_serve1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14314
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer5_dance_comment_stage == 1:
        customer5 "А я тебя ждал!"
        m "Да? Хотите сделать заказ?"
        customer5 "Конечно! Скажи, а сколько будет стоить приват с тобой?"
        m "!!!"
        m "Я не танцую!"
        mt "Как же они меня все достали со своими расспросами!!!"
        customer5 "Не, теперь ты меня не обманешь! Я видел тебя на сцене!"
        m "Вы меня с кем-то перепутали. Тут работает девушка, она немного похожа на меня..."
        customer5 "Да? Это она новенькая стриптизерша?"
        m "Да."
        customer5 "А как мне заказать у нее приват?"
        m "Не знаю. По-моему, она только на сцене танцует и в приват не ходит."
        customer5 "Жаль..."



    if monicaStartedStripDanceFlag == True and customer5_dance_comment_stage == 0:
        customer5 "Ого! Ты же на сцене танцуешь!"
        m "Вы меня с кем-то путаете."
        m "Я не танцую на сцене."
        customer5 "Серьезно? По-моему, это ты была!"
        m "Я работаю тут просто официанткой и не танцую стриптиз."
        customer5 "Вот черт. Видимо, я перебрал с пивом тогда..."
        mt "Неудивительно..."
        $ customer5_dance_comment_stage = 1

    #


    m "Вам что-нибудь принести?"
    img 14315
    with diss
    customer5 "Да! Мне пожалуйста два бургера, и два Ваших самых лучших коктейля!"
    img 14316
    with diss
    m "Хорошо, один момент!"
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14349
    with fade
    w
    sound snd_plates1
    img 14350
    with diss
    w
    sound snd_beer_table
    img 14351
    with diss
    w
    img 14353
    with diss
    m "Вот, пожалуйста! Что-нибудь еще?"
    music In_Your_Arms
    img 14354
    with fade
    customer5 "Да, Вас! Не зря же я купил всего по два!"
    customer5 "Садитесь рядом и давайте пообщаемся!"
    customer5 "Я верю, что мы созданы друг для друга!"
    menu:
        "Сесть рядом с клиентом. (в будущих обновлениях) (disabled)":
            # в след обнове
            return
        "Не буду!":
            # клиент злой
            m "Не буду!"
            music Power_Bots_Loop
            img 14355
            with fade
            customer5 "Ах ты глупая официантка! Даже школьницы знают этот способ знакомства!"
            customer5 "Не могла сказать сразу?!"
            img 14357
            with diss
            m "Я подумала, что Вы очень голодный."
            m "Что-нибудь еще?"
            img 14358
            with diss
            customer5 "Да! Свали отсюда!"
            return

label customer5_afterserve1:
    if monicaBitch == True:
        mt "Амбициозный задрот..."
    else:
        mt "Пьяница..."
    return
