# Моника входит в Le Grand

# voucher or gift coupon

# На нее смотрит рецепшин
# Моника не хочет к ней подходить
# Моника может пойти в ресторан
label ep26_dialogues4_restaurant1:
# Если Моника занималась миньетом в туалете, то:
# При входе в ресторан, ее перехватывает рецепшионист.
# Спрашивает, Мэм, какая цель Вашего визита сюда?
# Моника отвечает что это не ее дело!
# Та отвечает что это ее дело, потому как у нее есть подозрение на незаконное занятие проституцией.
# Это запрещено в нашем отеле.
    img 20391
    with fadelong
    w
    img 20392
    with diss
    w
    music stop
    sound Jump1
    img 20393
    with hpunch
    w
    music Groove2_85
    sound highheels_run2
    img 20394
    with fadelong
    reception "Женщина, постойте-ка!"
    img 20395
    with diss
    m "!!!"
    img 20396
    with diss
    reception "Мэм, какая цель Вашего визита сюда?"
    img 20397
    m "Это не Ваше дело!"
    m "Я посещаю любые места когда захочу."
    m "И не собираюсь отчитываться ни перед кем!"
    img 20398
    with diss
    reception "Мэм, это мое дело, как сотрудника отеля."
    reception "У нас есть подозрение на незаконное занятие проституцией."
    img 20399
    with diss
    reception "Это запрещено в нашем отеле!"
# Моника отвечает да как она смеет?!
# Моника приличная леди!
# И идет просто отведать ланч в ресторане!
# Рецепшионист заявляет, чтобы Моника предъявила доказательства этого, иначе она сейчас вызовет охрану.
# выбор Моники: показать тикет на ланч, либо уйти (если тикета нет, то он серый), либо устроить скандал (если Моника сучка)
    music Power_Bots_Loop
    img 20400
    with fade
    m "ЧТО?!"
    img 20401
    m "Да как ты смеешь, никчемный работник!?"
    m "Я приличная Леди!"
    m "И иду отведать ланч в Вашем ресторане!"
    m "По приглашению!"
    music Groove2_85
    img 20402
    with fade
    reception "Мэм, пожалуйста, предъявите доказательства того, что Вы собираетесь посетить ресторан."
    reception "И Ваше приглашение."
    img 20403
    with diss
    reception "Иначе я вынуждена буду вызвать охрану."
    img 20404
    with fade
    menu:
        "Показать сертификат." if check_inventory("legrand_certificate",1) == True:
# Либо Моника показывает тикет и рецепшионист заявляет что Моника может проходить, но она будет следить за ней.
# Моника зло и надменно смотрит и проходит.
            img 20405
            with fade
            m "Абсолютно не понимаю необходимость этого ненужного действия."
            m "Но вот, пожалуйста!"
            img 20406
            with diss
            m "Если уж Вам так надо!"
            reception "..."
            return True
        "Показать сертификат. (disabled)" if check_inventory("legrand_certificate",1) == False:
            pass
        "Устроить скандал и войти":
# Моника устраивает скандал:
# Моника говорит рецепшионистке что у нее достаточно с собой денег на то, чтобы скупить весь этот отель!
# И если рецепшионистка желает, то может ходить за ней и следить.
# Однако, если она это делает с целью получить на чай от такой леди как Моника, то она выбрала неверный путь!
# А сейчас пусть уйдет с дороги, пока Моника по настоящему на разозлилась!
            music Pyro_Flow
            img 20407
            with fade
            m "Доказательства?!"
            m "У меня достаточно денег, чтобы скупить весь этот дурацкий отель!"
            reception "..."
            img 20408
            with fade
            m "Поверь, я уже все всем доказала в этой жизни!"
            m "И, если тебе кажется, что в этом есть необходимость, то можешь ходить за мной и следить."
            m "Однако, если твоя цель преследования меня получить чаевые от такой леди как Я, то ты выбрала неверный путь!"
            call bitch(5, "ep26_dialogues4_restaurant1") from _call_bitch_198
            img 20409
            with diss
            m "А сейчас, уйди с дороги, пока я по настоящему не разозлилась!"
            img 20410
            with diss
            reception "..."
            return True
        "Уйти.":
            # Если Моника уходит, то говорит что еще вернется и устроит неприятности такому нерадивому и никчемному сотруднику как она!
            music Pyro_Flow
            img 20411
            with fade
            m "Я не собираюсь предъявлять каких-то дурацких доказательств!"
            img 20412
            with diss
            m "Я ухожу!"
            m "Но я еще вернусь!"
            m "И устрою неприятности такому нерадивому и никчемному сотруднику, как Вы!"
            music Groove2_85
            img 20413
            with diss
            reception "..."
            return False

label ep26_dialogues4_restaurant1a:
    # говорит на улице
    if monicaBitch == True:
        mt "Сучка!!!"
    else:
        mt "Черт!"
    return



label ep26_dialogues4_restaurant2:
# Если Моника НЕ занималась миньетом в туалете, то:
# Рецепшионист перехватывает Монику
# Мэм. Пожалуйста, назовите цель Вашего визита.
# Я иду в ресторан!
# Хорошо, Мэм.
    music Groove2_85
    img 20414
    with fadelong
    reception "Мэм! Пожалуйста, назовите цель Вашего визита."
    img 20415
    with diss
    m "Я иду в ресторан!"
    img 20416
    with diss
    reception "Хорошо, Мэм."
    img 20417
    with fadelong
    if monicaBitch == True:
        music Power_Bots_Loop
        mt "Сучка..."
    else:
        w
    return

label ep26_dialogues4_restaurant3:
# Моника входит в ресторан:

# Если Моника обещала уволить официантку:
# waitress: Здравствуйте, Мэм! Это... Это ВЫ?!
# Моника отвечает: Да, это я!
# Удивительно что ты все еще работаешь здесь!
# waitress: Мэм... Что Вам будет угодно?! (злое лицо)
    img 20418
    with fadelong
    waitress "Здравствуйте, Мэм!"
    music Groove2_85
    $ notif(t_("У Моники плохие отношения с официанткой."))
    img 20419
    waitress "Это... Это ВЫ?!"
    img 20420
    with fade
    m "Да, это Я!"
    m "Удивительно, что ты все еще работаешь здесь!"
    img 20421
    with diss
    waitress "Мэм... Что Вам будет угодно?!"
# Моника говорит что их ресторан не дотягивает до ее требований, но она, так уж и быть,
# соблаговолит откушать здесь
# waitress: Да, Мэм... Присаживайтесь, пожалуйста, за свободный столик (злое лицо)
    img 20422
    with fade
    m "Этот ресторан не дотягивает до моих требований."
    m "Но я, так уж и быть, соблаговолю откушать здесь."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Poppers_and_Prosecco
    img 20423
    with fadelong
    waitress "Да, Мэм..."
    waitress "Присаживайтесь, пожалуйста, за свободный столик."
# Моника садится
# waitress: Мэм, Что Вам будет угодно?
    img 20424
    with diss
    waitress "Мэм, Что Вам будет угодно?"
# меню выбора блюд (если нет тикета, то указаны цены, большие):
# блюдо1
# блюдо2
# блодо3
    if check_inventory("legrand_certificate",1) != True:
        $ menu_price = [restaurantForelPrice, restaurantSeaFoodPrice, restaurantLasaniaPrice, restaurantSushiPrice]
        $ menu_price_money = [restaurantForelPrice, restaurantSeaFoodPrice, restaurantLasaniaPrice, restaurantSushiPrice]
    $ choose_var = 0
    menu:
        "Стейк из форели, греческий салат и шампанское.":
            $ choose_var = 1
            img 20425
            with fade
            m "Стейк из форели, греческий салат и шампанское."
            $ images_list = [20432, 20433, 20434, 20435]
        "Морепродукты и коктейль.":
            $ choose_var = 2
            img 20425
            with fade
            m "Морепродукты и коктейль."
            $ images_list = [20436, 20437, 20438, 20435]
        "Лазанья с кофе.":
            $ choose_var = 3
            img 20425
            with fade
            m "Лазанья с кофе."
            $ images_list = [20439, 20440, 20441, 20435]
        "Суши и сок.":
            $ choose_var = 4
            img 20425
            with fade
            m "Суши и сок."
            $ images_list = [20442, 20443, 20444, 20435]
        "Уйти.":
            # Моника уходит
            music Groove2_85
            img 20426
            with fade
            m "В этом дурацком ресторане нет нормальной еды для такой леди как Я!"
            m "Я ухожу!"
            img 20427
            with diss
            waitress "!!!"
            return False
# Моника говорит какие блюда выбрала
# Если есть тикет, то она добавляет что оплатит тикетом.
    if check_inventory("legrand_certificate",1) == True:
        sound snd_folder_drop
        img 20428
        with diss
        m "Я оплачу этим сертификатом"
        $ questHelp("steve_18", True)
        $ remove_inventory("legrand_certificate", 1, True)
        $ questHelp("steve_18", True)
        sound snd_take_paper
    else:
        $ add_money(-menu_price_money[choose_var-1])

# waitress: Да, Мэм. Несколько минут и все будет готово.
# Моника надменно говорит чтобы официантка поторопилась, если не хочет вылететь с работы прямо сейчас.
# waitress морщится в злобе
    img 20429
    with fade
    waitress "Да, Мэм. Несколько минут и все будет готово."
    music Groove2_85
    img 20430
    with diss
    m "Я советую тебе поторопиться, деточка."
    m "Если ты не хочешь вылететь с работы прямо сейчас!"
    img 20431
    with diss
    waitress "!!!"

    $ restaurantFoodHistory.append(choose_var)
# waitress: Пожалуйста, Мэм.
# Моника кушает и говорит как же вкусно.
# Она отвыкла от такой вкусной пищи, а зря!
# Надо скорее возвращать назад ее прежнюю жизнь.
    #Стейк из форели, греческий салат и шампанское.
    #Морепродукты и коктейль.
    #Лазанья с кофе.
    #Суши и сок.

    #1
    music stop
    img black_screen
    with diss
    pause 1.5
    music Poppers_and_Prosecco
    sound snd_plates
    img images_list[0]
    with fadelong
    waitress "Пожалуйста, Мэм."

    #2
    img images_list[1]
    with diss
    mt "Ммммм... Как вкусно..."
    #3
    img images_list[2]
    with diss
    mt "Я уже отвылка от такой вкусной пищи."
    #4
    img images_list[3]
    with fade
    mt "А зря!"
    mt "Надо скорее возвращать назад мою прежнюю жизнь!"
    music stop
    sound snd_eating
    img black_screen
    with diss
    pause 2.0
    $ monica_eated()

    if monica_escort_service_started == False:
        # смотрят
        music Hidden_Agenda
        img 20445
        with fadelong
        w
        #
        $ images_list = random.sample(set([20446, 20447, 20448, 20449]), 1)
        img images_list[0]
        with diss
        mt "Интересно, почему та девушка так смотрит на меня?"

    call ep210_quests_escort_eat_process() from _rcall_ep210_quests_escort_eat_process
    if _return == False:
        return True

# Моника говорит официантке. Я закончила. Было невкусно!
# waitress: Мэм, прошу прощения, в следующий раз мы постараемся угодить Вам... (злое лицо)
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20450
    with fadelong
    m "Я закончила."
    m "Было невкусно!"
    img 20451
    with diss
    waitress "Мэм, прошу прощения."
    waitress "В следующий раз мы постараемся угодить Вам..." # (злое лицо)
    return True

label ep26_dialogues4_restaurant4:
# Моника входит в ресторан:
# Если Моника помогла официантке:

# waitress: Здравствуйте, Мэм! Это... Это ВЫ?!
# Моника отвечает: Да, это Я!
# waitress: Мэм... Я очень рада видеть Вас и тепло приветствую Вас от имени заведения!
# Моника говорит что хотела бы поесть у них
# waitress: Да, Мэм... Присаживайтесь, пожалуйста, за свободный столик (доброе лицо)
    img 20452
    with fadelong
    waitress "Здравствуйте, Мэм!"
    waitress "Это... Это ВЫ?!"
    m "Да, это Я!"
    $ notif(t_("У Моники хорошие отношения с официанткой."))
    waitress "Мэм... Я очень рада видеть Вас!"
    waitress "И тепло приветствую Вас от имени заведения!"
    img 20453
    with diss
    m "Спасибо."
    m "Я бы хотела у Вас что-нибудь поесть."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Poppers_and_Prosecco
    img 20454
    with fadelong
    waitress "Да, Мэм."
    waitress "Присаживайтесь, пожалуйста, за свободный столик." # (доброе лицо)

# Моника садится
# waitress: Мэм, Что Вам будет угодно?
# waitress: Специально для Вас у нас скидка 50% на все меню.
    img 20455
    with diss
    waitress "Мэм, что Вам будет угодно?"
    waitress "Специально для Вас у нас скидка 50 процентов на все меню."
# меню выбора блюд (если нет тикета, то указаны цены, со скидкой):
# блюдо1
# блюдо2
# блодо3
    img 20457
    with fade
    if check_inventory("legrand_certificate",1) != True:
        $ menu_price = [restaurantForelPrice*0.5, restaurantSeaFoodPrice*0.5, restaurantLasaniaPrice*0.5, restaurantSushiPrice*0.5]
        $ menu_price_money = [restaurantForelPrice*0.5, restaurantSeaFoodPrice*0.5, restaurantLasaniaPrice*0.5, restaurantSushiPrice*0.5]
    $ choose_var = 0
    menu:
        "Стейк из форели, греческий салат и шампанское.":
            $ choose_var = 1
            img 20458
            with fade
            m "Стейк из форели, греческий салат и шампанское."
            $ images_list = [20432, 20433, 20434, 20435]
        "Морепродукты и коктейль.":
            $ choose_var = 2
            img 20458
            with fade
            m "Морепродукты и коктейль."
            $ images_list = [20436, 20437, 20438, 20435]
        "Лазанья с кофе.":
            $ choose_var = 3
            img 20458
            with fade
            m "Лазанья с кофе."
            $ images_list = [20439, 20440, 20441, 20435]
        "Суши и сок.":
            $ choose_var = 4
            img 20458
            with fade
            m "Суши и сок."
            $ images_list = [20442, 20443, 20444, 20435]
        "Уйти.":
            img 20456
            with fade
            m "Спасибо, я передумала. Зайду попозже."
            waitress "Мэм, мы всегда ждем Вас!"
            return False

# Моника говорит какие блюдо выбрала
# Если есть тикет, то она добавляет что оплатит тикетом.

    if check_inventory("legrand_certificate",1) == True:
        sound snd_folder_drop
        img 20428
        with diss
        m "Я оплачу сертификатом."
        $ remove_inventory("legrand_certificate", 1, True)
        sound snd_take_paper
    else:
        $ add_money(-menu_price_money[choose_var-1])

# waitress: Да, Мэм. Несколько минут и все будет готово.
    img 20459
    with fade
    waitress "Да, Мэм."
    waitress "Несколько минут и все будет готово."
    $ restaurantFoodHistory.append(choose_var)


# waitress: Пожалуйста, Мэм.
#    waitress "Пожалуйста, Мэм."
# Моника кушает и говорит как же вкусно.
# Она отвыкла от такой вкусной пищи, а зря!
# Надо скорее возвращать назад ее прежнюю жизнь.
#    m "Ммммм... Как вкусно..."
#    m "Я уже отвылка от такой вкусной пищи."
#    m "А зря!"
#    m "Надо скорее возвращать назад мою прежнюю жизнь!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Poppers_and_Prosecco
    sound snd_plates
    img images_list[0]
    with fadelong
    waitress "Пожалуйста, Мэм."

    #2
    img images_list[1]
    with diss
    mt "Ммммм... Как вкусно..."
    #3
    img images_list[2]
    with diss
    mt "Я уже отвылка от такой вкусной пищи."
    #4
    img images_list[3]
    with fade
    mt "А зря!"
    mt "Надо скорее возвращать назад мою прежнюю жизнь!"
    music stop
    sound snd_eating
    img black_screen
    with diss
    pause 2.0
    $ monica_eated()
    if monica_escort_service_started == False:
        # смотрят
        music Hidden_Agenda
        img 20445
        with fadelong
        w
        #
        $ images_list = random.sample(set([20446, 20447, 20448, 20449]), 1)
        img images_list[0]
        with diss
        mt "Интересно, почему та девушка так смотрит на меня?"

    call ep210_quests_escort_eat_process() from _rcall_ep210_quests_escort_eat_process_1
    if _return == False:
        return True

# Моника говорит официантке. Я закончила. Было очень вкусно, спасибо!
# waitress: Мэм, добро пожаловать к нам снова!
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20460
    with fadelong
    m "Я закончила."
    m "Было очень вкусно. Спасибо!"
    waitress "Мэм, добро пожаловать к нам снова!"
    return True

label ep26_dialogues4_restaurant5:
    mt "Я уже посещала ресторан сегодня."
    mt "Больше мне пока нечего там делать."
    return
