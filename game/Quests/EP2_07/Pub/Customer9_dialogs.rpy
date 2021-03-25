default customer9_dance_comment_stage = 0
default customer9_after_private = False

label customer9_1stmeeting:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14394
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14395
    with diss
    customer9 "Оу! Новенькая? Скажи, ты любишь подарки?"
    img 14396
    mt "Подарки? Вероятно, он о чаевых..."
    img 14397
    with diss
    menu:
        "Ну да...":
            music Hidden_Agenda
            img 14398
            with fade
            m "Да."
            img 14399
            with diss
            customer9 "Я так и думал. Вот скажи, что тебе подарить?"
            img 14400
            with diss
            m "У меня все есть, но чаевые были бы кстати."
            img 14401
            with fade
            customer9 "Нет, я не о чаевых. Как насчет страстного поцелуя?"
            music Groove2_85
            img 14402
            with diss
            m "Нет, спасибо."
            img 14403
            with diss
            mt "Да как он может подобное спрашивать у такой как Я!?"
            if monicaBitch == True:
                mt "Придурок!"
            pass
        "Я не готова отвечать на этот вопрос.":
            music Groove2_85
            img 14404
            with fade
            m "Я не готова отвечать на этот вопрос."
            img 14405
            with diss
            customer9 "Я понял... Свидетели... Хорошо, не отвечай, потом расскажешь!"
            pass
    # смотрит на монику
    img 14406
    with fade
    customer9 "Ты любишь классический секс или в попу?"
    music Power_Bots_Loop
    img 14407
    with hpunch
    m "А?!"
    img 14408
    customer9 "Я понял! Это значит в попу... Иначе ты бы не работала в Shiny Hole."
    img 14403
    with diss
    mt "Он нормальный?"
    img 14409
    with fade
    customer9 "Мне пожалуй ничего, но я очень рад нашему знакомству!"
    img 14410
    with diss
    mt "Неадекватный урод..."
    return

label customer9_serve1:
    if customer9_after_private == True:
        call ep213_dialogues3_pub_17() from _rcall_ep213_dialogues3_pub_17
        return _return
    music Hidden_Agenda
    sound highheels_short_walk
    img 14411
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer9_dance_comment_stage == 1:
        customer9 "Эй, не могу дождаться, когда ты покажешь свою голую попку со сцены!"
        m "Вы меня с кем-то..."
        customer9 "Я хочу, чтобы ты сняла с себя трусики на сцене и бросила их мне..."
        customer9 "Я хочу забрать их..."
        customer9 "Я готов заплатить за это. Сколько? Назови цену."
        mt "?!"
        m "Я не танцую на..."
        customer9 "Не хочешь говорить? Хорошо, я буду ждать этого момента."
        customer9 "А потом просто заберу их..."
        mt "..."
        mt "Человек, озабоченный чужими трусами!"
        mt "Кого только не встретишь в этой дыре!"
        mt "!!!"


    if monicaStartedStripDanceFlag == True and customer9_dance_comment_stage == 0:
        customer9 "У меня в штанах дымится, когда вижу тебя на сцене!"
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer9 "Расскажи это кому-нибудь другому."
        m "Я официантка, а не стрип..."
        customer9 "Охренительная задница!!!"
        customer9 "Не могу дождаться, когда ты ее оголишь на сцене перед всеми!"
        m "Я..."
        customer9 "А еще хочу увидеть, как ты танцуешь только для меня..."
        mt "Долбанный извращенец!"
        mt "По-моему, здесь все такие!"
        mt "!!!"
        mt "Как мне надоела эта дыра!"
        $ customer9_dance_comment_stage = 1

    #


    m "Что будете заказывать?"
    # чел резко хватает монику и садит себе на колени
    music Groove2_85
    sound Jump1
    img 14476
    with vpunch
    m "Ай!"
    sound Jump2
    img 14477
    with hpunch
    customer9 "Скажи, ты была хорошей девочкой?"
    customer9 "Расскажи Санте!"
    customer9 "И возможно, Санта сделает тебе хороший подарок!"
#    mt "Меня посадил к себе на колени незнакомый мужик! Возможно, стоит ему подыграть..."
    img 14478
    with diss
    $ menu_corruption = [0, pubCustomer9_serve1_Corruption]
    menu:
        "Быстро отпусти меня!":
            music Power_Bots_Loop
            sound snd_punch_face2
            img 14479
            with diss
            m "Быстро отпусти меня!"
            sound Jump1
            img 14480
            with diss
            m "Еще раз попробуй сделай так и я сломаю тебе нос, урод!"
            # моника вырывается
            img 14481
            with fade
            customer9 "Ах вот ты как! Ну и вали! Ваше пиво кстати отстой!"
            img 14482
            with diss
            mt "Что же ты его тогда пьешь?"
            return False
        "Да, я была хорошей девочкой.":
            music Hidden_Agenda
            img 14483
            with fade
            m "Да, я была хорошей девочкой."
            img 14484
            with diss
            customer9 "Я так и думал! Уверен, ты обслужила очень много клиентов и они остались довольны."
            # кладет ей под чулок купюру
            sound snd_take_paper
            img 14485
            with diss
            w
            $ add_tips(20.0)
            img 14486
            with fade
            customer9 "Ладно, беги, у меня еще есть пиво."
            img 14487
            with diss
            mt "Он дал мне 20 долларов! Ничего себе..."
            $ add_corruption(10, "pubCustomer9_serve1_Corruption")
            return True

label customer9_afterserve1:
    mt "Очередной ненормальный посетитель..."
    return
label customer9_afterserve2:
    mt "Но стоит-ли мне позволять так вести с собой?! Моника, не забывай кто ты такая!"
    return
