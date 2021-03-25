label cit10_dialog_1:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11028
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 11029
    with diss
    cit10 "Да, Мэм."
    cit10 "Что Вы хотели?"
    m "Я бы хотела предложить Вам купить это платье."
    cit10 "Какое платье?"
    img 11030
    with fade
    m "Вот это, которое на мне..."
    img 11031
    with fade
    cit10 "Это что, подержанное платье?"
    m "Нет, Мэм. Это новое платье..."
    cit10 "А почему оно надето на тебе?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False

    $ add_corruption(1, "cit10_dialog_1")
    img 11032
    with fade
    m "Я... Я работаю здесь манекеном."
    img 11033
    with diss
    cit10 "Я уже тороплюсь, может быть в следующий раз..."
    return True

label cit10_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11034
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img black_screen
    with diss
    pause 1.0
    img 11035
    with fade
    cit10 "Прогуляйся."
    m "В смысле?"
    img 11036
    with diss
    cit10 "Пройдись, я хочу посмотреть на это платье."
    img 11037
    with fade
    m "Хорошо..."
    # Моника прогуливается
    sound highheels_short_walk
    img 11038
    with diss
    w
    sound highheels_short_walk
    img 11039
    with diss
    w
    sound highheels_short_walk
    img 11040
    with diss
    w
    sound highheels_short_walk
    img 11041
    with diss
    w
    img 11042
    with fade
    cit10 "Хорошо, я еще подумаю."
    img 11043
    with fade
    mt "!!!"
    return True

label cit10_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11044
    with fadelong
    m "Добрый день, Мэм."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 11045
    with fade
    cit10 "По поводу платья?"
    m "Да."
    img 11046
    with fade
    cit10 "Хорошо, пойдем примерим его."
    return

label cit10_dialog_3a:
    #примерочная
    music Groove2_85
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    img 11047
    with fadelong
    cit10 "Снимай его, я примерю."
    img 11048
    with diss
    m "..."
    img 11049
    with fadelong
    cit10 "Ну?"
    $ menu_corruption = [90]
    menu:
        "Раздеться и отдать платье.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit10_dialog_3a1")
    #Моника раздевается, покупатель одевает платье
#    cit10 "А туфли?"
#    m "Мэм, туфли продаются отдельно."
    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11050
    with fadelong
    w
    img 11051
    with fade
    cit10 "Одень мне туфли, я хочу примерить платье в них."
    img 11052
    with diss
    m "Да, Мэм, конечно."
    img 11053
    with diss
    # Ставит туфли
    w
    img 11054
    with fadelong
    cit10 "Я сказала одеть туфли мне на ноги."
    music Power_Bots_Loop
    img 11055
    with fade
    m "Мэм, Вы не можете сделать этого сами?"
    cit10 "Это сделаешь ты..."
    img 11056
    with fade
    m "Дьявол! Ненавижу!!!"
    # corruption +2 req 100
    $ menu_corruption = [110]
    menu:
        "Одеть туфли покупательнице.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit10_dialog_3a2")
    # Моника одевает туфли
    music Groove2_85
    img 11057
    with diss
    w
    img 11058
    with diss
    w
    sound highheels_short_walk
    img 11059
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 11060
    with fadelong
    cit10 "Вторую..."
    img 11061
    with diss
    w
    img 11062
    with diss
    w
    img 11063
    with diss
    w
    sound highheels_short_walk
    img 11064
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11065
    with fadelong
    w
    img 11066
    with diss
    w
    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11067
    with fade
    cit10 "Нет, это не мой стиль!"
    #исчезает
    return True

















#
