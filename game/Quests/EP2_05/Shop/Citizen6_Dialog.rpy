# Girl3
label cit6_dialog_1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10905
    with fadelong
    m "Здравствуйте. Я бы хотела предложить Вам это платье!"
    music Groove2_85
    img 10906
    with diss
    cit6 "А кто тебе сказал, что мне надо что-то предлагать? Ты думаешь, я сама не смогу ничего выбрать?"
    cit6 "И вообще, кто ты такая?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit6_dialog_1")
    img 10907
    with fade
    m "Я... Я работаю здесь манекеном."
    img 10908
    with diss
    cit6 "Ладно, манекен. Позову тебя, если захочу. А сейчас уйди!"
    return True

label cit6_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10909
    with fadelong
    m "Добрый день. Скажите, Вам нравится это платье?"
    music Groove2_85
    img 10910
    with diss
    cit6 "Какое платье? Если то, что на Вас, то я бы даже и платьем это не назвала!"
    m "Ну как же! Оно очень красивое и качественное."
    img 10911
    with fade
    cit6 "Качественное говоришь... А оно эластичное?"
    m "Ну, наверное..."
    img 10912
    with fade
    cit6 "Замечательно! Давай это и проверим! Ты же тут манекен?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Что-то мне это не нравится (уйти).":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit6_dialog_2")
    music Hidden_Agenda
    img 10914
    with fade
    m "Я... Я работаю здесь манекеном."
    music Groove2_85
    img 10915
    with diss
    cit6 "Вот и чудно. А теперь, манекен, раздвинь ноги."
    # corruption +1 req 90
    $ menu_corruption = [85]
    menu:
        "Хорошо.":
            pass
        "Нет, это недопустимо.":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit6_dialog_2b")
    # Моника стоит и начинает разводить ноги в стороны
    music Loved_Up
    img 10916
    with fade
    w
    img 10917
    with diss
    w
    img 10918
    with diss
    w
    m "Вот так достаточно?"
    cit6 "Неплохо, но нужно шире!"
    # моника разводит ноги еще чуть шире
    music Groove2_85
    img 10919
    with diss
    m "Все, больше не могу!"
    cit6 "Конечно можешь! Ах, черт! Совсем забыла... У меня срочные дела. Пока, манекен! Отлично стоишь!"
    img 10920
    with fade
    m "Дак Вы купите платье?"
    cit6 "может быть, в другой раз..."
    return True

label cit6_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10921
    with fadelong
    m "Здравствуйте! К Вам можно обратиться?"
    music Groove2_85
    img 10922
    with fade
    cit6 "Ну попробуйте, а Вы кто?"
    # corruption +1 req 80
    $ menu_corruption = [90]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit6_dialog_3")

    img 10923
    with fade
    m "Я... Я работаю здесь манекеном."
    cit6 "Точно! Как я могла забыть?! Манекен, давай продолжим тестировать платье."
    m "Давайте. Что Вас интересует?"
    cit6 "Похоже, не только у меня провалы в памяти. Раздвигай свои красивые ноги!"
    # моника разводит ноги
    music Loved_Up
    img 10924
    with fade
    cit6 "Вот! Отлично, так и стой! А теперь положи руки за голову!"

    cit6 "Я хочу осмотреть товар."
    # corruption +3 req 100

    $ menu_corruption = [100]
    menu:
        "Хорошо.":
            pass
        "Ну уж нет.":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(3, "cit6_dialog_3b")

    img 10925
    with diss
    m "Так?"
    # Моника кладет руки за голову
    img 10926
    with diss
    cit6 "Да! А теперь немного нагнись, совсем чуть-чуть."
    img 10927
    with fade
    mt "Что она от меня хочет? Надеюсь, после этого она его купит..."
    # Нагибается
    img 10928
    with diss
    w
    cit6 "Какой хороший манекен, а теперь не шевелись!"
    # Моника стоит какое то время, клиент подходит и шлепает ее по жопе
    img 10929
    with diss
    w
    music stop
    img 10930
    with diss
    w
    sound Spank12
    img 10931
    with diss
    w
    music Groove2_85
    img 10932
    with fade
    m "Ай! Что Вы себе позволяете?"
    cit6 "Как что? Проверяю товар."
    img 10933
    with fade
    m "Но почему так?!"
    cit6 "Вы похоже забыли, что клиент всегда прав, хотя манекену простительно. Знаете что, не буду я у Вас ничего покупать."
    music Power_Bots_Loop
    img 10934
    with fadelong
    mt "Сучка!"
    return True
