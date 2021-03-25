# Girl4
label cit7_dialog_1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10935
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10936
    with diss
    cit7 "Что тебе надо, девочка?"
    cit7 "Ты не похожа на продащицу."
    # corruption +1 req 80

    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit7_dialog_1")

    img 10937
    with fade
    m "Я... Я работаю здесь манекеном."
    img 10938
    with diss
    cit7 "Манекеном?! Фи!"
    #Исчезает
    return True
label cit7_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10939
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10940
    with fade
    cit7 "Это кто? Снова девочка-манекен?"
    # corruption +1 req 80
    $ menu_corruption = [85]
    menu:
        "Да, Мэм.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit7_dialog_2")
    img 10941
    with fade
    m "Да, Мэм."
    m "Пожалуйста, рассмотрите приобретение этого замечательного платья."
    img 10942
    with fade
    cit7 "Этого?"
    cit7 "Хм... Оно вполне ничего..."
    img 10943
    with diss
    if monicaBitch == True:
        mt "Еще бы вполне ничего, сучка! Это самое дорогое платье в этой дыре!"
    else:
        mt "Еще бы вполне ничего! Это самое дорогое платье в этой дыре!"
    img 10944
    with fade
    cit7 "Сегодня я уже потратила деньги."
    cit7 "Манекен, продемонстрируй мне это платье в следующий раз."
    m "Да, Мэм..."
    #исчезает
    return True
label cit7_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10945
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 10946
    with fade
    cit7 "Это кто? Снова девочка-манекен?"
    m "Да, Мэм.":
    img 10947
    with diss
    cit7 "Я помню это платье."
    cit7 "Пойдем я его померю."
    return


label cit7_dialog_3a:
    #уходят в примерочную
    music Groove2_85
    sound snd_fabric1
    img 10948
    with fadelong
    m "..."

    img black_screen
    with diss
    pause 1.0
    img 10949
    with fadelong
    cit7 "Ну? Что стоишь?"
    img 10950
    with diss
    cit7 "Снимай его!"
    # corruption +2 req 90

    $ menu_corruption = [90]
    menu:
        "Снять платье...":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(2, "cit7_dialog_3a")
    # Моника снимает платье, покупатель одевает
    # Моника стоит обнаженная, закрывается
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 10951
    with fadelong
    cit7 "Ну как?"
    img 10952
    with diss
    cit7 "Как я тебе в этом платье?"
    m "Мэм. Вы выглядите в нем великолепно."
    img 10953
    with fade
    cit7 "Хорошо, я куплю это платье со скидкой 50 процентов!"
    m "Мэм, простите. На это платье не действует скидка..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 10954
    with fadelong
    cit7 "Тогда УВЫ!"
    #исчезает
    return True
