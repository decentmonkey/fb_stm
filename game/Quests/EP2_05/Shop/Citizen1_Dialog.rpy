# Man 1 - curly hair
label cit1_dialog_1:
    $ store_music()
    music Hidden_Agenda
    sound highheels_short_walk
    img 11101
    with fadelong
    m "Пожалуйста, рассмотрите покупку этого красивого платья..."
    music Groove2_85
    img 11102
    with diss
    cit1 "Ой уйди, не до тебя сейчас... Я забыл как убить Супермена... Какой то камень криптошит или магманит..."
    img 11103
    m "Но Вы даже не знаете, что я предлагаю, послушайте меня."
    cit1 "Я же сказал, мне не интересно, пока!"
    $ restore_music()
    return True

label cit1_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11104
    with fadelong
    m "Пожалуйста, рассмотрите покупку этого красивого платья..."
    img 11105
    with fade
    cit1 "Что?"
    m "Я предлагаю Вам купить это платье!"
    cit1 "Какое платье?"
    music Groove2_85
    img 11106
    with diss
    mt "Что за идиот..."
    img 11107
    m "Вот это, оно надето на мне."
    cit1 "Вот это? Интересно... Кстати, дамочка, а Вы здесь вообще работаете?"
    m "Ну конечно, я же продаю Вам платье..."
    img 11108
    with fade
    cit1 "Как то это все очень подозрительно... А где Ваш бейдж?"
    m "Понимаете, я только временно здесь работаю. У меня нет бейджа."
    cit1 "Дай подумать... Если у тебя нет бейджа, значит ты не сотрудник... Кто же ты?"
    # corruption +1 req 80

    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit1_dialog_2")
    music Hidden_Agenda
    img 11109
    with fade
    m "Я... Я работаю здесь манекеном."
    cit1 "Отлично, рассмотрю тебя поближе."
    # подходит к монике сзади, рассматривает зад, она поворачивается
    music Loved_Up
    img 11110
    with diss
    w
    img 11111
    with diss
    w
    img 11112
    with diss
    w
    music Groove2_85
    img 11113
    with fade
    cit1 "Эй, похоже ты бракованый манекен! Манекены не двигаются!"
    cit1 "Подними руки!"
    # corruption +1 req 90
    $ menu_corruption = [90]
    menu:
        "Да, конечно...":
            pass
        "Нет, Мистер!":
            music Power_Bots_Loop
            img 11139
            with fade
            m "Нет, Мистер!"
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit1_dialog_2b")
    # моника поднимает руки вверх, клиент ходит вокруг. если платье короткой, возможно будет видно зад
    music Loved_Up
    img 11114
    with fade
    cit1 "Какой хороший манекен!"
    img 11115
    with diss
    w
    # трогает за руку, ходит вокруг
    img 11116
    with diss
    w
    img 11117
    with diss
    w
    music Groove2_85
    img 11118
    with fade
    cit1 "Черт, совсем забыл, надо успеть в мой любимый магазин комиксов! Еще увидимся, манекен!"
    mt "Да как ты смеешь такое говорить? Что за гик..."
    return True

label cit1_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11119
    with fadelong
    m "Пожалуйста, рассмотрите покупку этого красивого платья..."
    img 11120
    with diss
    cit1 "О, манекен! Да, давай рассмотрю..."
    cit1 "Замри!"
    m "Зачем? По моему и так платье можно рассмотреть без проблем."
    img 11121
    cit1 "А ну помолчи! Манекены не двигаются и не говорят."
    # Смена картинок как он поднимает монике рукм, ходит вокруг, трогает
    music Groove2_85
    img 11122
    with fade
    m "Эй! Что ты делаешь?"
    img 11123
    with fade
    cit1 "А что, непонятно? Оцениваю товар."
    cit1 "Ты же хочешь, чтобы я купил платье?"
    # corruption +2 req 90
    $ menu_corruption = [100]
    menu:
        "Да, конечно...":
            pass
        "Нет, это уже слишком...":
            music Power_Bots_Loop
            img 11139
            with fade
            m "Нет, это уже слишком...Хватит с меня!"
            m "А ну вали отсюда!!!"
            #злая моника
            cit1 "Ааа!!! Бракованный манекен!!!"
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(2, "cit1_dialog_3")

    music Loved_Up
    m "Ну...да..."
    cit1 "Прекрасно, тогда помолчи и не шевелись."
    img 11124
    with diss
    #еще несколько экшенов
    w
    img 11125
    with diss
    w
    img 11126
    with diss
    w
    img 11127
    with diss
    w

    # кастомер поднимает руку моники и нюхает подмышку. Не уверен насчет этого, но монгим такое нравится
    sound Jump1
    img 11128
    with fade
    cit1 "Оу... Какой приятный запах! Странно, откуда он у манекена..."

    music Power_Bots_Loop
    img 11129
    with diss

    # corruption +3 req 100

    $ menu_corruption = [110]
    menu:
        "Позволить клиенту продолжить.":
            pass
        "Это уже слишком!":
            img 11139
            with fade
            m "Это уже слишком! Что ты себе позволяешь?"
            #злая моника
            cit1 "Ааа!!! Бракованный манекен!!!"
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(3, "cit1_dialog_3b")
    music Loved_Up
    # еще пара картинок
    img 11130
    with fadelong
    w
    img 11131
    with diss
    w
    img 11132
    with fade
    w
    img 11133
    with diss
    cit1 "Очень хорошо, хотел бы я такого манекена себе домой!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 11134
    with fade
    m "Вам все понравилось? Вы готовы купить это замечательное платье?"
    cit1 "Да, мне все понравилось!"
    img 11135
    with diss
    m "Пройдем на кассу?"
    img 11136
    with fade
    cit1 "Зачем? У меня все равно нет денег, а ты отличный манекен!"
    music Power_Bots_Loop
    img 11137
    with diss
    m "Ах ты... Да ты меня всю облапал!"
    cit1 "Ну вообще то, ты сама предложила рассмотреть товар, вот я и рассмотрел. Платье к слову так себе..."
    img 11138
    with fadelong
    m "Урод!"
#    cit1 "Ладно, не злись, еще увидимся!"
    return True
