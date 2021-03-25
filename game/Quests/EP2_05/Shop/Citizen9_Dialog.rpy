
label cit9_dialog_1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10998
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10999
    with fade
    cit9 "А?"
    m "Я бы хотела предложить Вам купить это платье!"
    cit9 "Да? Любопытно. А оно что, невидимое?"
    m "Да нет же, оно надето на мне."
    img 11000
    with diss
    cit9 "А с каких пор продавцы носят платья, которые продают?!"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit9_dialog_1")
    music Hidden_Agenda
    img 11001
    with fade
    m "Я не совсем продавец..."
    m "Я... Я работаю здесь манекеном."
    music Groove2_85
    img 11002
    with fade
    cit9 "Класс! А через пол года ты станешь Старшим Манекеном! Ха-ха-ха."
    cit9 "В общем удачи с продажей платья!"
    if monicaBitch == True:
        mt "Сучка..."
    else:
        mt "!!!"
    return True

label cit9_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11003
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 11004
    with fade
    cit9 "О, консультант. Какое платье мне предложите?"
    m "Я предложу Вам самое лучшее платье, что есть у нас!"
    m "Оно сейчас надето на мне."
    cit9 "И почему так?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit9_dialog_2")
    music Groove2_85
    img 11005
    with fade
    m "Я... Я работаю здесь манекеном."
    cit9 "Насколько я знаю, на манекены вешают не самый ходовой товар..."
    cit9 "А если говорить о Вас, то думаю, что на вешалке это платье смотрелось бы лучше!"
    return True

label cit9_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11006
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    img 11007
    with fade
    cit9 "О, консультант. Какое платье мне предложите?"
    img 11008
    with diss
    m "Я предложу Вам самое лучшее платье, что есть у нас!"
    m "Оно сейчас надето на мне."
    cit9 "И почему так?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit9_dialog_3")
    music Groove2_85
    img 11009
    with fade
    m "Я... Я работаю здесь манекеном."
    cit9 "Насколько я знаю, на манекены вешают не самый ходовой товар..."
    cit9 "А если говорить о Вас, то думаю, что на вешалке это платье смотрелось бы лучше!"
    music Power_Bots_Loop
    img 11010
    with fade
    mt "Как же она меня достала..."
    menu:
        "Это не так!":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    music Groove2_85
    img 11011
    with fade
    m "Это не так!"
    m "На мне это платье выглядит отлично, и оно самое прекрасное!"
    cit9 "Оу... Какой уверенный манекен."
    cit9 "Как насчет того, чтобы это проверить?"
    # corruption +2 req 90
    $ menu_corruption = [90]
    menu:
        "Я знаю, что я права!":
            pass
        "Я не собираюсь Вам ничего доказывать.":
            img 11012
            m "Я не собираюсь Вам ничего доказывать."
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit9_dialog_3b")
    img 11013
    with fade
    m "Мэм, я знаю, что я права."
    cit9 "Хорошо, вот давай это и проверим! У тебя есть вешалка?"
    m "Конечно, это же магазин одежды..."
    img 11014
    with diss
    cit9 "Отлично, снимай платье!"
    img 11015
    m "Мэм, я не могу этого сделать!"
    img 11016
    cit9 "Как странно, ты же манекен. Чего тебе стесняться?"
    cit9 "Хорошо, пойдем в примерочную. И не забудь захватить свою конкурентку. Ха-ха-ха."
    img 11017
    with diss
    m "Конкурентку?"
    img 11018
    with fade
    cit9 "Ну вешалку... Теперь я понимаю, почему ты манекен."
    return True


label cit9_dialog_3a:
    # уходят в примерочную
    music Groove2_85
    img 11019
    with fadelong
    cit9 "Разденься и повесь платье на вешалку."
    $ menu_corruption = [100]
    menu:
        "Раздеться и повесить платье на вешалку.":
            pass
        "Не раздеваться.":
            music Power_Bots_Loop
            img 11020
            with fade
            m "Я не буду этого делать..."
            img 11021
            with diss
            cit9 "Правда? Мне сообщить продавцу что манекен отказывается показывать товар?"
            img 11022
            with fade
            menu:
                "В этом нет необходимости. Я сниму платье.":
                    pass
                "Это не имеет значения. Я не буду снимать платье.":
                    music Groove2_85
                    img 11023
                    with fade
                    m "Мэм. Покупатели могут снимать вещи с манекена только в случае примерки."
                    m "Если Вы собираетесь примерить это платье, то дайте мне знать."
                    $ monicaSellingDressRefuseLastDay = day
                    return False
            m "В этом нет необходимости. Я сниму платье."


#    mt "И зачем я это делаю? Надеюсь, это поможет мне продать платье..."
    # Моника стоит голая и платье на вешалке
    music Groove2_85
    sound snd_fabric1
    img black_screen
    with diss
    pause 1.0
    img 11024
    with fadelong
    w
    img 11025
    with diss
    cit9 "Ха! Вот теперь я точно вижу, что была права!"
    img 11026
    with diss
    cit9 "Но было интересно. Пока, манекен!"
    m "Мэм, Вы купите?..."
    # клиент уходит
    music Power_Bots_Loop
    img 11027
    with fade
    mt "Стерва!"
    $ add_corruption(3, "cit9_dialog_3a1")
    return True
