label ep25_dialogues1_shop1:

# Моника пытается зайти к Стиву в офис.
# Если Моника не ходила к Виктории, то она говорит что сначала надо проверить перевел-ли Стив деньги.
    mt "Мне надо сначала узнать, перевел-ли Стив деньги Виктории..."
    return

# Если не куплена новая одежда, то она говорит что не пойдет туда в таком виде.
# Что она леди и Босс и ей надо выглядеть подобающе. Говорит что надо наведаться в магазин одежды
label ep25_dialogues1_shop1a:
    mt "Я не могу идти туда в таком виде."
    mt "Вообще-то я Леди!"
    mt "И Босс!"
    mt "И мне надо выглядеть подобающе."
    mt "Возможно, стоит наведаться в тот магазин одежды, куда меня водил Дик?"
    mt "Это еще та дыра, но, может быть, я смогу найти там что-то подходящее."
    mt "Из того что я могу себе позволить в данный момент..."
    mt "!!!"
    mt "Когда же кончится этот кошмар!"
    return

label ep25_dialogues1_shop1b:
    if check_hook(label="bardie_eric_quest_college_shop", scene="street_cloth_shop") == True:
        return
    # Магазин закрыт
    mt "Магазин закрыт..."
    "Интересно почему..."
    return False

label ep25_dialogues1_shop1c:
    mt "Чтобы что-то найти среди этого хлама, надо спросить у продавца..."
    mt "Но смогу-ли я себе позволить что-то купить даже здесь?"
    mt "Дьявол..."
    return

label ep25_dialogues1_shop1d:
    # Моника одевает платье в подвале
    mt "Наконец-то у меня есть приличная одежда. Мне не стоит привыкать к плохому. Я - Леди!"
    return

label ep25_dialogues1_shop2:
    # Если не whore outfit, то магазин закрыт!

# Моника приходит в магазин одежды.
# Там, в зависимости от ее предыдущего поведения, ее встречает продавец.
# Моника спрашивает есть-ли что-то приличное из деловой одежды.
# Продавец показывает самое приличное что есть. Бизнес костюм.
# Моника говорит что это дешевая подделка и есть-ли что-то получше.
# Продавец отвечает что получше ничего нет.
# Костюм стоит $1000.
    music Groove2_85
    img 10619
    with fadelong
    cashier "Здравствуйте, Мэм!"
    img 10620
    cashier "Чем могу быть Вам полезна?"
    img 10621
    with diss
    m "Мне нужно подобрать что-то приличное."
    m "Что-то, что смотрится по деловому, но, в тот же момент, очень стильное."
    m "Что-нибудь что подойдет для такой бизнес-леди..."
#    music Hidden_Agenda
    img 10622
    with diss
    # смущенно смотрит на себя. продавщица тоже
    m "Как Я..."
    img 10623
    with diss
    cashier "..."
    img 10624
    with diss
    m "..."
    music Groove2_85
    img 10625
    with fade
    cashier "Мэм, пройдемте, я покажу Вам самое лучшее платье, которое имеется в продаже."
    $ questHelp("shop_1", True)
    $ questHelp("shop_2", skipIfExists=True)
    $ questHelp("shop_3", skipIfExists=True)
    $ questHelp("shop_4", skipIfExists=True)
    # Показывает платье Моники
    img black_screen
    with diss
    sound highheels_short_walk
    img 10626
    with fadelong
    cashier "Пожалуйста! Лучшее платье в этом магазине!"
    music Power_Bots_Loop
    img 10627
    with diss
    mt "О БОЖЕ! Это же мое платье!"
    mt "То платье, которое я вернула."
    img 10628
    mt "Оно мне сейчас кажется таким красивым!"
    music Hidden_Agenda
    img 10629
    with fade
    m "Простите, Мэм..."
    m "Я бы предпочла сейчас что-нибудь подешевле..."
    sound highheels_short_walk
    img 10630
    with fadelong
    cashier "Хорошо, вот еще неплохое платье, оно подойдет Вам."
    # Моника смотрит на еще одно платье
    img 10631
    with diss
    w
    img 10632
    with fade
    m "Сколько стоит это платье?"
    cashier "Это платье стоит $ 250, Мэм."
    music Groove2_85
    img 10633
    with fade
    m "Я разбираюсь в моде и вижу что это подделка под более дорогой бренд."
    img 10634
    cashier "Мэм, это прекрасное платье. По очень доступной цене."
label ep25_dialogues1_shop2_loop1:
    music Groove2_85
    menu:
        "Попросить скидку.":
            if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False and clothShopCashierFirstNightOffended == False:
                music Hidden_Agenda
                img 10635
                with fade
                m "Скажите, можно-ли сделать какую-то скидку?"
                img 10636
                cashier "Мэм, вообще-то это платье не продается по скидке..."
                img 10637
                with fade
                m "Я очень прошу Вас. Вы ведь узнаете меня? Я очень лояльный клиент."
                music RnB3_65
                img 10638
                with fade
                cashier "..."
                $ notif(t_("Моника была добра к продавцу."))
                cashier "Да, я узнала Вас. Хотя Вы и одеты сегодня немного странно."
                img 10639
                with fade
                cashier "Хорошо, я сделаю скидку в 50 процентов, только ради Вас!"
                menu:
                    "Купить платье за $ 125." if money>=125:
                        music Ready_and_Waiting
                        m "Давайте я померю его."
                        cashier "Проходите в примерочную..."
                        # примерочная
                        img 10646
                        with fade
                        w
                        img 10647
                        with fadelong
                        m "Мне нравится."
                        m "Я беру его."
                        cashier "Мэм, пройдемте на кассу."
                        $ questHelp("shop_2", True)
                        $ questHelp("shop_3", True)
                        $ questHelp("shop_4", False)
                        $ add_money(-125.0)
                        return True
                    "Купить платье за $ 125. (не хватает денег) (disabled)" if money < 125:
                        pass
                    "Поискать другой способ получить платье...":
                        music Groove2_85
                        img 10645
                        with diss
                        m "Хорошо, я подумаю."
                        m "Возможно вернусь позже."
                        cashier "Да, Мэм. Возвращайтесь! Мы всегда рады Вам."
                        return False
            else:
                music Hidden_Agenda
                img 10640
                with fade
                m "Скажите, можно-ли сделать какую-то скидку?"
                img 10641
                cashier "Мэм, вообще-то это платье не продается по скидке..."
                img 10642
                with fade
                m "Я очень прошу Вас. Вы ведь узнаете меня? Я очень лояльный клиент."
                music Groove2_85
                img 10643
                with diss
                cashier "..."
                $ notif(t_("Моника была недостаточно добра к продавцу."))
                cashier "Я узнала Вас! И я не могу сказать что Вы лояльный клиент нашего магазина."
                cashier "Для Вас цена составляет $ 250!"
                music Power_Bots_Loop
                img 10644
                if monicaBitch == True:
                    mt "Сучка!"
                else:
                    mt "!!!"
                jump ep25_dialogues1_shop2_loop1

        "Купить платье за $ 250. (не хватает денег) (disabled)" if money < 250:
            pass
        "Купить платье за $ 250." if money >= 250:
            music Ready_and_Waiting
            m "Давайте я померю его."
            cashier "Проходите в примерочную..."
            # примерочная
            img 10646
            with fadelong
            w
            img 10647
            with fadelong
            m "Мне нравится."
            m "Я беру его."
            cashier "Мэм, пройдемте на кассу."
            $ questHelp("shop_2", True)
            $ questHelp("shop_3", False)
            $ questHelp("shop_4", False)
            $ add_money(-250.0)
            return True

        "Поискать другой способ получить платье...":
            img 10645
            with fade
            m "Хорошо, я подумаю."
            m "Возможно вернусь позже."
            cashier "Да, Мэм. Возвращайтесь! Мы всегда рады Вам."
            return False

label ep25_dialogues1_shop2a:
    mt "Ура! Наконец-то я выгляжу как леди!"
    mt "Ну... почти как леди..."
    mt "Все-таки эту каблуки могут выдать меня..."
    mt "И это платье... Оно не такое уж дорогое..."
    mt "Однако никто не сможет вывернуть его наизнанку и посмотреть на бирку!"
    mt "Так что это неважно."
    mt "На вид его цену может определить только такой профессионал моды как Я..."
    return

label ep25_dialogues1_shop3:
    # Моника пытается зайти в магазин после покупки платья за деньги или после того как отобрала его
    mt "Мне нечего делать там сейчас..."
    return

label ep25_dialogues1_shop4:
# Моника замечает что в этот раз в магазине мало народа и она может украсть его.
    img 10648
    with fadelong
    mt "А в этом магазине сегодня на удивление никого нет..."
    img 10649
    mt "Может быть мне попробовать... украсть это платье?"
    return

label ep25_dialogues1_shop4a:
    mt "Я уже была там сегодня."
    mt "Может быть зайти в другой день, когда будет поменьше посетителей?"
    return


label ep25_dialogues1_shop5:
    # Моника заходит в магазин снова
    img 10650
    with fadelong
    menu:
        "Обратиться к продавцу.":
            return False
        "Украсть платье.":
            return True
    return

label ep25_dialogues1_shop6:
    # Моника пытается украсть платье
# Если пытается украсть, то ее ловит продавец.
# Происходит перепалка и продавец хочет вызвать полицию.
# Моника просит не делать этого.
# В зависимости от того как Моника вела себя, продавец затаскивает ее в примерочную, где делает femdom.
# Диалоги отличаются в зависимости от поведения Моники.
# Если Моника вела себя хорошо и она скромная, то можно сказать что ей сейчас трудно и она отдаст деньги после.
# Продавец тогда соглашается. Моника затем не входит в магазин, т.к. ей пока не до отдачи долгов.
# Затаскивание в примерочную:
# Продавец говорит что помнит Монику. Что она- та сучка, которая ругалась на нее и вернула платье.
# Моника просит, пожалуйста, не надо вызывать полицию.
# Моника может ударить продавщицу и убежать
# Либо Продавщица говорит Монике одеть то платье, которое она возвращала.
# Моника спрашивает: но зачем?
# Продавщица говорит делать что сказано, иначе через 5 минут она будет в полцейском участке.

    $ monicaTriedToStealDress = True
    img 10651
    with fadelong
    w
    img 10652
    with diss
    w
    m "Манекену одежда ни к чему!"
    sound snd_fabric1
    img 10653
    with diss
    w
    sound Jump1
    img 10654
    with diss
    w
    sound highheels_run2
    img 10655
    with fadelong
    w
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 10657
    with fade
    cashier "Ну что, сучка, далеко собралась?!"
    img 10656
    cashier "Думаешь из этого магазина можно что-то украсть?"
    img 10658
    with fade
    m "Что Вы от меня хотите?!"
    m "Не трогайте меня!"
    m "Дайте мне пройти!"
    img 10659
    with diss
    cashier "Тебе некуда идти, я закрыла магазин, чтобы ты не убежала."
    cashier "Я вызываю полицию!"
    music Pyro_Flow
    img 10660
    m "Что?! Да как ты смеешь! Я респектабельный клиент!"
    music Power_Bots_Loop
    img 10661
    if clothShopCashierFirstNightOffended == True:
        cashier "Я узнала тебя! В прошлый раз тебе удалось отвертеться, но в этот раз полиция схватит тебя!"

    cashier "Я видела, ты пыталась украсть это платье!"
    cashier "Ты отсюда не уйдешь!"
    img 10662
    with fade
    m "Что?! Полиция?!"
    m "Мне не нельзя в полицию!!!"
    img 10663
    cashier "Это уже твои проблемы!"
    sound snd_phone1
    img 10664
    with fade
    cashier "Алло! Полиция?"
    cashier "У меня в магазине вор, я прошу Вас приехать скорее."
    img 10665
    mt "О БОЖЕ!!! ЧТО МНЕ ДЕЛАТЬ?!"
    menu:
        "Ударить продавца и убежать!" if monicaBitch == True:
            $ monicaKickedVivianForDress = True
            music Pyro_Flow
            img 10666
            with fade
            m "Ты не могла успеть закрыть дверь!"
            m "Ты все врешь!"
            sound snd_punch_face1
            img 10667
            with diss
            m "Получай, На!"
            sound snd_bodyfall
            cashier "Аххх!"
            # Моника убегая
            sound highheels_run2
            img 10668
            with fade
            m "Это мое платье! Я заслужила его!"
            return False
        "Ударить продавца и убежать! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass
        "Умолять не вызывать полицию...":
            return True

label ep25_dialogues1_shop7:
    # Умоляет не вызывать полицию
    music Power_Bots_Loop
    img 10669
    with fade
    m "Пожалуйста, не надо!"
    m "Я готова на ВСЕ!!!"
    m "ВЫ СЛЫШИТЕ?! Я ГОТОВА НА ВСЕ!!!"
    m "Только не вызывайте полицию! Пожалуйста!"
    music Hidden_Agenda
    img 10670
    with fade
    cashier "На все говоришь?"
    policeman "Пожалуйста, назовите адрес..."
    music Power_Bots_Loop
    img 10671
    m "Да, НА ВСЕ!!!"
    m "ПОЖАЛУЙСТА, ПОЛОЖИТЕ ТРУБКУ!"
    music Hidden_Agenda
    img 10672
    with fade
    cashier "У меня есть идея."
    sound snd_phone_short_beeps
    img 10673
    with diss
    cashier "Вас плохо слышно, я перезвоню."
    # кладет трубку

    img 10674
    with fade
    cashier "..."
    img 10675
    with fade
    cashier "..."
    music Indo_Rock
    img 10676
    with fadelong
    cashier "Идем за мной."

    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    # Приводит в примерочную
    img 10677
    with fadelong
    cashier "Жди здесь."
    # Берет манекен с красивым платьем
    sound highheels_run2
    img 10678
    with fadelong
    w
    sound snd_bodyfall
    img 10679
    with fade
    cashier "Вот, одевай!"

    m "Мое платье?! Но зачем?"


    img 10680
    cashier "Оно не твое! Ты вернула его, забыла?"
    cashier "Быстро одевай!"
    # Моника одевает платье
    sound snd_fabric1
    img black_screen
    with diss
    pause 1.0
    img 10681
    with fadelong
    w
    img 10682
    with fade
    w
    cashier "А теперь ложись!"
    img 10683
    m "Зачем?"
    cashier "Еще одно зачем и я вызываю полицию!"
    img 10684
    with fade
    m "Хорошо, я ложусь..."
    img 10685
    with diss
    w
    img 10686
    with diss
    w
    img 10687
    with diss
    w
    sound snd_fabric1
    img 10688
    with diss
    w
    img 10689
    with diss
    w
    img 10690
    with diss
    w
    img 10691
    with diss
    w
    img 10692
    with diss
    w
    img 10693
    with diss
    w
    img 10694
    with fade
    m "Эй, что Вы делаете?!"



    music stop
    music2 Indo_Rock

    # Продавец садится на Монику
    img 10695
    with fade
    cashier "Я Вас обслуживала ранее."
    img 10696
    with diss
    cashier "И теперь хотела бы получить фидбек."
    sound Jump2
    img 10697
    with diss
    m "Да как Вы смеете?!"
    m "Мммпфххх...."
    img 10698
    with diss
    cashier "Вам понравилось обслуживание?"
    m "Мммпфххх...."

    img black_screen
    with Dissolve(0.5)
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_1 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_1.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_2 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_2.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_2
    with fadelong
    wclean
    stop music

    img 10699
    with diss
    cashier "Только попробуй сказать нет..."
    img 10700
    with diss
    cashier "Вам понравилось обслуживание?"
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_3 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_3.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_4 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_4.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_4
    with fadelong
    wclean
    stop music
    img 10701
    with diss
    m "Мммм... Да..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_5 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_5.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_5
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_6 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_6.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_6
    with fadelong
    wclean
    stop music
    img 10702
    with diss
    cashier "Оцените обслуживание по десятибальной шкале!"
    cashier "Вы ведь оцениваете обслуживание на десять баллов, правда?"
    m "Мммпфхх..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_7 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_7.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_8 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_8.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_8
    with fadelong
    wclean
    stop music
    img 10703
    with diss
    cashier "Отвечай, сучка. Иначе отправишься в полицию прямо сейчас."
    img 10704
    with diss
    m "Мммпфхх... Да..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_9 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_9.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_9
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_10 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_10.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_10
    with fadelong
    wclean
    stop music
    img 10705
    with diss
    cashier "Посоветуете-ли Вы этот магазин своим друзьям и знакомым?"
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_1.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_1_11 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_1_11.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_1_11
    with fadelong
    wclean
    stop music
    img 10706
    with diss
    m "Мммпфхх... Да..."
    music stop
    music2 Loved_Up2
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img 10707
    with fadelong
    cashier "А теперь я хочу попробовать твою розовую киску. Мммм..."

    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_1 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_1.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_2 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_2.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_2
    with fadelong
    wclean
    stop music
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_9 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_9.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_9
    with fadelong
    wclean
    stop music

    img 10708
    with diss
    m "Мммпфхх..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_3 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_3.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_4 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_4.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_4
    with fadelong
    wclean
    stop music
    img 10709
    with fade
    cashier "Ммммм... Какая прелесть..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_5 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_5.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_5
    with fadelong
    wclean
    stop music
    img 10710
    with diss
    m "Мммпфхх..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_6 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_6.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_6
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_7 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_7.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_7
    with fadelong
    wclean
    stop music
    img 10711
    with diss
    cashier "Ммммм... Такая вкусная киска мне еще не попадалась..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_8 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_8.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_8
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_9 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_9.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_9
    with fadelong
    wclean
    stop music
    img 10712
    with diss
    cashier "Ммммм..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ClothShopTrader_Monica_Lesbian_2.mp3"
    scene black
    image videov_ClothShopTrader_Monica_Lesbian_2_10 = Movie(play="video/v_ClothShopTrader_Monica_Lesbian_2_10.mkv", fps=30)
    show videov_ClothShopTrader_Monica_Lesbian_2_10
    with fadelong
    wclean
    stop music
    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    # встает
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 10713
    with fadelong
    cashier "А теперь быстро переодевайся назад!"

    # Моника переодевается

# Дает платье.
# Моника в шоке: мое! мое платье! оно такое красивое!
# Продавщица говорит Монике скорее одеть его. Продавщица говорит идти в примерочную.
# Моника одевает платье.
# Продавщица заходит и говорит Монике ложиться на пол!
# Моника не понимает зачем?
# Продавщица зло смотрит.
# Моника ложится.
# Продавщица говорит что она обслуживала ее и теперь хочет получить фидбек.
# Продавщица садится Монике на лицо (femdom)
# По ходу сцену, Продавщица говорит диалоги о том как Вам понравилось обслуживание?
# Монике приходится отвечать что ей очень понравилось.

# В конце продавщица кончает и говорит Монике что у нее есть предложение.
# Что она может отдать ей ту одежду что Моника хотела украсть в случае, если Моника поможет продать
# это гребаное платье.
# Моника спрашивает, а можно ей отдать это платье?
# Продавщица говорит что нет. Это самое дорогое платье в этом магазине.
# Здесь нет ни у кого денег, чтобы купить такую дорогую тряпку.
# И поставщик отказывается принимать это платье назад.
# Так что, это платье надо продать, чтобы не потерять премиальные за квартал.
# На манекене оно смотрится хуже, чем на тебе, сучка.
# Потому у тебя есть шансы продать его.
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    img 10714
    with fadelong
    cashier "Ты можешь идти, но не вздумай даже смотреть на то платье, которое собиралась украсть."
    img 10715
    cashier "Хотя..."
    cashier "У меня есть предложение для тебя..."
    m "Кккккакое предложение?"
    img 10716
    with diss
    cashier "Я могу тебе подарить то платье, что ты хотела украсть."
    cashier "Но только в случае, если ты сможешь продать другое."
    m "Какое другое?"
    img 10717
    cashier "То платье, которое ты вернула некоторое время назад."
    cashier "То, в котором ты сейчас была на полу."
    music Hidden_Agenda
    img 10718
    with fade
    m "А можно... Просто подарить мне его."
    music Groove2_85
    img 10719
    with fade
    cashier "Нет! Это самое дорогое платье в этом магазине."
    cashier "В этом районе ни у кого нет денег, чтобы купить такую дорогую тряпку."
    cashier "И поставщик отказывается принимать это платье назад."
    music Power_Bots_Loop
    img 10720
    with fade
    cashier "Мне надо продать это платье, иначе я рискую потерять премиальные за квартал."
    cashier "На манекене оно смотрится хуже, чем на тебе, сучка."
    img 10721
    cashier "Потому у тебя гораздо больше шансов продать его."

# Моника спрашивает что от нее требуется?
# Продавщица говорит что ей надо будет одеть это платье и показывать его покупателям.
# Ей не важно что Моника будет делать, но если продаст его, то получит взамен ту одежду.
# И пусть даже не думает о том, чтобы убежать в этом дорогом платье!
# Продавщица фотографирует Монику в платье.
# Говорит этот снимок сразу отправится в полицию, если она попробует убежать.
# Выбор:
# Согласиться продавать платье.
# Отказаться.
    music Groove2_85
    img 10722
    with fade
    m "Что от меня требуется?"
    m "Как я буду его продавать? Я буду работать продавцом?"
    img 10723
    with diss
    mt "О БОЖЕ! Кажется я нашла нормальную работу!"
    img 10724
    with fade
    cashier "Здесь уже есть продавец!"
    img 10725
    with diss
    cashier "Тебе надо будет работать манекеном!"
    sound snd_fabric1
    img 10726
    with fade
    cashier "Ты оденешь это платье и будешь показывать его покупателям."
    img 10727
    cashier "И мне не важно как будешь уговаривать покупателей его купить."
    cashier "Но, если ты продашь его, то получишь в награду взамен ту одежду, что хотела украсть."
    music Power_Bots_Loop
    img 10728
    with fade
    m "Но, разве можно продавать одежду, которая надета на продавце?"
    music Groove2_85
    img 10729
    with fade
    cashier "Не на продавце, а на манекене!"
    cashier "И если этот манекен умеет убеждать купить одежду, то так даже лучше!"
    img 10730
    with diss
    cashier "В любом случае, я уже испробовала все другие варианты продать его!"
    music Power_Bots_Loop
    img 10731
    with fade
    mt "РАБОТАТЬ... МАНЕКЕНОМ!!!"
    cashier "Да, кстати."
    # щелкает ее на телефон
    img 10732
    call photoshop_flash() from _call_photoshop_flash_102
    w
    cashier "И только попробуй что-нибудь украсть."
    cashier "Этот снимок сразу отправится в полицию!"
    m "!!!"
    music Groove2_85
    img 10733
    with fade
    cashier "Ну так что, ты согласна?"
    img 10734
    with diss
    $ monicaNeedToSellDress = True
    menu:
        "Согласиться работать манекеном.":
            $ monicaAgreedToSellDress = True
            music Hidden_Agenda
            img 10735
            with fade
            m "Я... Я согласна..."
            cashier "Приходи завтра днем!"
            cashier "Сегодня посетителей уже не будет!"
            return True
        "Отказаться.":
            music Hidden_Agenda
            img 10736
            with fade
            m "Я... пока не готова..."
            cashier "Если надумаешь, приходи!"
            return False
    return

label ep25_dialogues1_shop8:
    # Моника рассуждает на улице
    mt "Работать манекеном?"
    mt "Какой ужас!"
    mt "..."
    mt "С другой стороны, у меня может появиться нормальная одежда."
    mt "НОРМАЛЬНАЯ!!!"
    mt "А не эти тряпки!!!"
    return

label ep25_dialogues1_shop9:
    # Моника приходит в магазин работать манекеном
    menu:
        "Купить платье за $ 250. (не хватает денег) (disabled)" if money < 250:
            pass
        "Купить платье за $ 250." if money >= 250:
            music Ready_and_Waiting
            img 10621
            with fade
            m "Я хочу купить то платье, которое случайно забыла убрать с руки, когда выходила из магазина."
            img 10641
            with fade
            cashier "Ты хотела украсть его!"
            cashier "И получила по заслугам!"
            img 10640
            with fade
            m "Достаточно!"
            m "Давай я померяю это платье."
            cashier "Проходите в примерочную..."
            # примерочная
            img 10646
            with fadelong
            w
            img 10647
            with fadelong
            m "Мне нравится."
            m "Я беру его."
            cashier "Мэм, пройдемте на кассу."
            $ questHelp("shop_2", True)
            $ questHelp("shop_3", False)
            $ questHelp("shop_4", False)
            $ questHelp("shop_6", False)
            $ add_money(-250.0)
            return 1



        "Работать манекеном...":
            music Groove2_85
            img 10737
            with fade
            m "Я... Я пришла работать манекеном..."
            if day_time != "day":
                cashier "Приходи днем! Вечером мало посетителей!"
                return 0
            img 10738
            with diss
            cashier "Хорошо. Переодевайся и выходи работать!"
            label ep25_dialogues1_shop9a:
                menu:
                    "Попросить белье.":
                        img black_screen
                        with diss
                        sound snd_fabric1
                        pause 2.0
                        img 10739
                        with fadelong
                        m "Мне еще нужен лифчик и трусики под платье."
                        sound Jump2
                        img 10740
                        with diss
                        cashier "Я не разрешаю тебе носить лифчик и трусики."
                        img 10741
                        cashier "Платье лучше смотрится без этого."
                        img 10742
                        with fade
                        m "Но как?! Ведь трусики не видно из-под платья!"
                        m "А если кто-то попросить примерить?"
                        img 10743
                        m "МНЕ ЧТО, ОСТАВАТЬСЯ ГОЛОЙ?!"
                        music Loved_Up
                        img 10744
                        with fade
                        cashier "Ты все верно поняла."
                        img 10745
                        m "Но зачем?! Какой в этом резон?!"
                        img 10746
                        with diss
                        cashier "Мне так хочется."
                        cashier "Мне нравится раздевать твою белоснежную попку."
                        music Groove2_85
                        img 10747
                        with fade
                        m "!!!"
                        img 10748
                        with diss
                        cashier "К тому же, я сама делала нечно подобное неколько раз."
                        music Power_Bots_Loop
                        img 10749
                        with fade
                        m "!!!"
                        mt "Чертова лесбиянка!"
                        music Groove2_85
                        jump ep25_dialogues1_shop9a
                    "Идти работать.":
                        return 2
            return 0
        "Уйти.":
            return 0

label ep25_dialogues1_shop10:
    # Моника заканчивает работу
    music Groove2_85
    img 10750
    with fadelong
    m "Я весь день пыталась продать это платье."
    m "Никто не хочет его покупать!"

    # Если Моника отказывалась
    if monicaSellingDressRefuseLastDay == day:
        music Loved_Up
        img 10751
        with fade
        cashier "Если ты хочешь продать это платье..."
        img 10752
        with diss
        w
        img 10753
        with diss
        cashier "То тебе надо более внимательно относиться к пожеланиям клиентов."
        img 10754
        with fade
        m "Ненавижу эту лесбиянку!"
        m "Она заплатит за то что лапает меня!"
        img 10755
        with fade
        m "Моника, терпи!"
        m "Тебе нужно то платье!"
        m "Это важный шаг, чтобы вернуть все назад!"
        #
        img 10756
        with fade
        cashier "Иди переодевайся и приходи завтра."
        return

    img 10756
    with fade
    cashier "Иди переодевайся и приходи завтра."
    return

label ep25_dialogues1_shop10a:
    menu:
        "Снять платье.":
            return True
        "Уйти.":
            return False
    return

label ep25_dialogues1_shop10b:
    $ store_music()
    music Groove2_85
    img 10739
    with fade
    cashier "У тебя покупатель в примерочной! Иди и обслуживай его!"
    $ restore_music()
    return

label ep25_dialogues1_shop11:
    # Моника пытается зайти в магазин после получения платья, отработав его
    mt "Мне нечего там делать."
    mt "Я не хочу общаться с этой лесбиянкой"
    mt "Лучше не пытаться ничего украсть, иначе не представляю что она еще заставит меня делать..."
    return

label ep25_dialogues1_shop12:
    # Моника продала платье
    img black_screen
    with diss
    pause 3.0
    music Groove2_85
    img 10757
    with fadelong
    m "Я продала платье!"
    m "Теперь выполняй свою часть сделки!"
    img 10758
    with diss
    cashier "Да, я помню. Ты продашь дорогое платье, полижешь мне киску и я подарю тебе то платье за $ 250."
    music Power_Bots_Loop
    img 10759
    with fade
    m "Я продам дорогое платье и ты подаришь мне платье за $ 250."
    m "Я ничего не собираюсь лизать тебе, извращенка!"

    music Loved_Up
    img 10760
    with fade
    cashier "Жаль."
    img 10761
    with diss
    cashier "Я уже представила твой белоснежный ротик у себя между ног..."
    img 10762
    with diss
    cashier "Ммммммм..."

    music Power_Bots_Loop
    img 10763
    with fade
    m "Хватит мечтать! Давай мне платье скорее!"
    cashier "А мне показалось в прошлый раз что тебе понравилось..."
    m "Отдай мое платье, сейчас же!"
    music Loved_Up
    img 10764
    with fade
    cashier "Обожаю когда ты ругаешься."
    cashier "Я попрошу тебя ругаться, когда ты будешь лизать мою киску снова..."
    music Power_Bots_Loop
    img 10765
    with fade
    m "ПЛАТЬЕ!!!"
    cashier "Хорошо, можешь забирать его..."

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Ready_and_Waiting
    img 10766
    with fadelong
    w
    img 10767
    with diss
    w
    img 10768
    with diss
    cashier "Если снова захочешь поработать манекеном, дай мне знать..."
    img 10769
    with fadelong
    m "НИКОГДА!!!"

    music stop
    img black_screen
    with diss
    pause 3.0
    music Loved_Up
    img 10770
    with fadelong
    cashier "..."
    return

label ep25_dialogues1_shop12a:
    # Моника на улице
    mt "БОЖЕ!"
    mt "Какие унижения мне пришлось пережить, чтобы получить это новое платье!"
    mt "!!!"
    mt "Как я могла докатиться до такого!"
    mt "Но зато у меня есть это замечательное платье!"
    mt "Оно дешевое, но, если честно, этого почти незаметно."
    mt "Нужно быть ценителем моды. Таким как Я. Чтобы увидеть отличие."
    mt "..."
    mt "К слову, теперь я снова выгляжу как Леди!"
    mt "Я очень рада!"
    mt "..."
    mt "Стив!!!"
    mt "Теперь мне не стыдно показаться перед ним!"
    mt "И перед его проститутками, которых он нанял на работу!"
    mt "Я устрою им! Я покажу им кто такая Моника Бакфетт!"
    return


label ep25_dialogues1_shop13:
    # Моника купила платье и больше не хочет заходить в магазин
    mt "Мне нечего делать в этом дешевом магазине."
    return

label ep25_dialogues1_shop14:
    # Моника сегодня уже работала манекеном, пытается зайти в магазин.
    mt "Я уже наелась этим магазином на сегодня."
    mt "Это дурацкое платье невозможно продать!"
    mt "И я не намерена больше унижаться перед этими ничтожными покупателями!"
    mt "По крайней мере, не сегодня..."
    return

label ep25_dialogues1_shop15:
    # Моника работает манекеном и срывается после очередного жесткого покупателя
    mt "Все! С меня хватит!"
    mt "Я больше не в состоянии терпеть это!"
    call ep25_quests_shop11a() from _call_ep25_quests_shop11a_2
    return

label ep25_dialogues1_shop16:
    # Моника рассуждает с утра, если в предыдущий день работала манекеном
    if rand(1,2) == 1:
        return
    mt "Я вспоминаю вчерашний день, когда я работала манекеном."
    mt "Я! Моника Бакфетт!"
    mt "..."
    mt "Мне кажется, это платье невозможно продать."
    mt "И у меня больше нет желания заниматься этим."
    mt "Или, все-же, стоит попробовать снова? Вдруг мне сегодня повезет?"
    return

label ep25_dialogues1_shop17:
    # Моника пытается зайти в банк в платье
    mt "У меня нет ни денег ни документов."
    mt "Даже учитывая что я хорошо одета, мне там пока делать нечего."
    return

label ep25_dialogues1_shop18:
    # Моника пытается зайти к Дику в платье
    mt "Мне лучше не показываться этой сучке Виктории в моем новом платье."
    mt "Я уверена, она решит что я хорошо живу и поднимет сумму."
    mt "Сумму, которую требует, чтобы Дик занимался моим делом."
    mt "Ненавижу ее!"
    return

label ep25_dialogues1_shop19:
    # Моника не работает сейчас
    mt "Если я хочу продавать платье, то мне придется его сначала одеть..."
    mt "Ненавижу все это!"
    return

label ep25_dialogues1_shop20:
    # Моника пытается выйти из магазина во время продажи платья
    mt "Лучше не пытаться ничего украсть, иначе не представляю что она еще заставит меня делать..."
    return

label ep25_dialogues1_shop20a:
    # Моника пытается выйти из магазина во время продажи платья обнаженной
    mt "Я не выйду на улицу в таком виде! Я еще не сошла с ума!"
    return

label ep25_dialogues1_shop21:
    # Моника пытается подойти к клиенту, пока идет обслуживание другого
    mt "Меня ждет покупатель в примерочной."
    return

label ep25_dialogues1_shop22:
    # Моника продает платье, клик на Монику
    mt "Не могу поверить что я продаю свое же платье!"
    mt "В каком-то дешевом магазине в трущобах!"
    return False

label ep25_dialogues1_shop23:
    # Моника комментирует покупателя
    if monicaSellingDressInProgress == True:
        mt "Какой-то придурок..."
    return

label ep25_dialogues1_shop24a:
    if monicaSellingDressInProgress == True:
        mt "Какая-то дура..."
    return
label ep25_dialogues1_shop24b:
    if monicaSellingDressInProgress == True:
        mt "Ненормальная покупательница..."
    return
label ep25_dialogues1_shop24c:
    if monicaSellingDressInProgress == True:
        mt "Тут бывает хоть кто-то нормальный?"
    return
label ep25_dialogues1_shop24d:
    if monicaSellingDressInProgress == True:
        mt "В этот магазин приходят только ненормальные стервы!"
    return


#    if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False and clothShopCashierFirstNightOffended == False:

# Если отказаться, то затем можно вернуться и сказать снова.

# Продавщица говорит, чтобы Моника приходила завтра днем.
# Моника приходит, выбор:
# Работать манекеном.
# Уйти

# В магазине народ

# Моника подходит к людям и предлагает платье

# Платье продается в несколько этапов.
# Этап 1
# Моника стоит в платье.
# Подходят люди и спрашивают сколько оно стоит.
# Моника может отвечать цену, либо промолчать
# Также Моника может говорить что это платье из хорошего материала и будет смотреться отлично на любой девушке.
# Говорят что слишком дорого

# Этап 2
# Моника стоит в платье.
# Подходят люди и спрашивают сколько оно стоит.
# Говорят что слишком дорого
# Подходит покупатель и спрашивает про цену
# Моника отвечает.
# Покупатель просит повернуться спиной
# Моника поворачивается и продолжает говорить что это хорошая покупка
#














#
