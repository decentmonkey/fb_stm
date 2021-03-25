# Bold Man
label cit2_dialog_1:
    $ store_music()
    music Hidden_Agenda
    sound highheels_short_walk
    img 11068
    with fadelong
    m "Добрый день, Мистер."
    m "Можно к Вам обратиться?"
    music Power_Bots_Loop
    img 11069
    with diss
    cit2 "Я сам решу что мне купить!"
    cit2 "Снова очередной консультант!"
    cit2 "В каждом магазине, куда-бы я ни пошел, одни чертовы консультанты!"
    cit2 "Которые навязывают свой дурацкий товар!"
    music Hidden_Agenda
    m "Мистер... Я... Не совсем консультант..."
    img 11070
    with fade
    cit2 "А кто же ты?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            $ restore_music()
            return False

    $ add_corruption(1, "cit2_dialog_1")
    img 11071
    with fade
    m "Я... Я работаю здесь манекеном."
    m "И я бы хотела предложить Вам купить это замечательное платье."
    music Groove2_85
    img 11072
    with fade
    cit2 "Какое? Это?"
    #Тычет пальцем
    img 11073
    m "!!!"
    m "Да, Мистер... Это..."
    img 11074
    with fade
    cit2 "Не сейчас, может в другой раз!"
    # Исчезает
    $ restore_music()
    return True

label cit2_dialog_2:
    music Hidden_Agenda
    img 11075
    with fadelong
    m "Добрый день, Мистер."
    m "Можно к Вам обратиться?"
    cit2 "А, это снова Ты?"
    cit2 "Напомни мне, кто ты?"
    # corruption +1 req 80

    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit2_dialog_2")
    music Hidden_Agenda
    img 11076
    with fade
    m "Я... Я работаю здесь манекеном."
    cit2 "Снова хочешь втюхать мне свое дурацкое платье?"
    music Groove2_85
    img 11077
    with diss
    m "!!!"
    m "Мистер, это очень хорошее платье."
    m "Оно очень дорогое!"
    img 11078
    with fade
    cit2 "Тем более дорогое!"
    cit2 "Ты пытаешься втюхать мне дорогую вещь!"
    cit2 "Ты точно глупая, как менекен!"
    img 11079
    m "!!!"
    img 11080
    with fade
    cit2 "Хотя... Это ведь дорогое платье?"
    cit2 "Можно я его потрогаю?"
    # corruption +2 req 90
    $ menu_corruption = [90]
    menu:
        "Да, посетители могут трогать товар...":
            pass
        "Нет, Мистер!":
            music Power_Bots_Loop
            img 11081
            with fade
            m "Нет, Мистер!"
            $ monicaSellingDressRefuseLastDay = day
            return False

    $ add_corruption(1, "cit2_dialog_2b")
    #Трогает за талию
    img 11082
    with fade
    m "Да, посетители могут трогать товар..."
    img 11083
    with diss
    w
    img 11084
    mt "!!!"
    sound Jump1
    img 11085
    with diss
    cit2 "Приятное на ощупь..."
    music Power_Bots_Loop
    img 11086
    with fade
    m "Мистер, Вы покупаете это платье?"
    img 11087
    with fadelong
    cit2 "Я еще подумаю!"
    # Исчезает
    return True

label cit2_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11088
    with fadelong
    m "Добрый день, Мистер."
    m "Можно к Вам обратиться?"
    music Groove2_85
    img 11089
    with diss
    cit2 "А, это снова Ты?"
    cit2 "Напомни мне, кто ты?"
    # corruption +1 req 90
    $ menu_corruption = [90]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit2_dialog_3")
    img 11090
    with fade
    m "Я... Я работаю здесь манекеном."
    m "Вы обещали подумать насчет покупки этого замечательного платья..."
    img 11091
    with diss
    cit2 "А! Этого?"
    cit2 "Я не ношу таких платьев, я мужчина!"
    img 11092
    with fade
    m "Вы могли бы купить его для своей девушки..."
    m "Ведь она заслуживает такого подарка..."
    img 11093
    with diss
    cit2 "Повернись спиной. Я хочу посмотреть."
    img 11094
    with fade
    m "Так, Мистер?" #Поворачивается
    cit2 "Нагнись вперед."
    # corruption +3 req 100
    $ menu_corruption = [100]
    menu:
        "Нагнуться вперед.":
            pass
        "Нет, Мистер!":
            music Power_Bots_Loop
            img 11095
            with fade
            m "Нет, Мистер!"
            $ monicaSellingDressRefuseLastDay = day
            return False
    #Моника нагибается
    #Посетитель хватает сзади Монику за ляжки
    $ add_corruption(3, "cit2_dialog_3b")
    img 11096
    with diss
    m "Так?"
    img 11097
    with diss
    cit2 "Нет! У моей девушки задница вдвое больше чем у тебя!"
    img 11098
    with diss
    cit2 "Это платье порвется на ней!"
    img 11099
    with fade
    cit2 "Я отказываюсь от покупки!"
    music Power_Bots_Loop
    img 11100
    with fade
    m "!!!"
    #исчезает
    return True






















#
