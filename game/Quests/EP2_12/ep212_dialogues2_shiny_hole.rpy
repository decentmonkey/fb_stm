default monicaPubPrivatDanceJoe1 = False # Моника согласилась пойти в приват
default monicaPubPrivatDanceJoe2 = False # Моника согласилась назвать себя шлюхой
default monicaPubPrivatDanceJoe3 = False # Моника согласилась потереться об клиента попой

#call ep212_dialogues2_shiny_hole_1() # гримерка, разговор с Джо перед приватом
#call ep212_dialogues2_shiny_hole_2() # подсобка барменов, приват
#call ep212_dialogues2_shiny_hole_3() # работая официанткой, подошла к клиенту после привата с ним

default monicaPubPrivate1CumZone = 0

default monicaTakeLightFromFloor = False

# приват будет доступен один раз в неделю
label ep212_dialogues2_shiny_hole_menu_private:
    img scene_Pub_Stage1
    with fadelong
    menu:
        "Танец для Мистера Беркельбауха.":
            return 0
        "Приватный танец 1":
            return 1
        "Приватный танец 2" if pubPrivate1Count >= 1:
            return 2
        "Ничего.":
            return -1
    return -1


# Паб. Моника находится в гримерке после выступления на сцене.
# в гримерку заходит Джо.
label ep212_dialogues2_shiny_hole_1:
    # частично использовать имеющиеся арты
    # Джо смотрит на Монику похотливо
    music Groove2_85
    img 22870
    with fadelong
    sound man_steps
    w
    img 22871
    with fade
    joe "[monica_pub_name], тебе очень идет этот костюм."
    joe "Я тебе говорил уже об этом?"
    # Моника смотрит на него презрительно и молчит
    img 22880
    with diss
    mt "Что опять нужно от меня этому неудачнику Джо?"
    m "..."
    img 22872
    with fade
    joe "Не спеши переодеваться, [monica_pub_name]."
    img 22874
    with diss
    m "Почему это?" # раздраженно
    m "Я только что со сцены."
    m "С меня хватит!"
    img 30451
    with fade
    joe "У тебя есть еще на сегодня работа..."
    m "???" # подозрительно
    m "Какая еще работа?"
    music Marty_Gots_a_Plan
    img 30452
    with diss
    joe "Один наш постоянный клиент... В общем..."
    joe "Он хочет, чтобы ты станцевала для него..."
    img 22873
    with diss
    joe "И только для него."  # подмигивает
    music Groove2_85
    img 22876
    with fade
    m "Только для него?"
    m "Приватный танец?!" # зло
    joe "Да!"
    img 22878
    with diss
    m "Нет!"
    m "!!!"

    if monicaPubPrivatDance1 == True:
        #
        $ notif(t_("Моника танцевала приват для Мистера Беркельбауха"))
        #
    music Stealth_Groover
    img 22877
    with fade
    mt "Я не собираюсь больше танцевать приват!"
    mt "Мне хватило этого неудачника банкира в прошлый раз!"
    mt "Мало того, что пришлось прикасаться к его..."
    mt "К нему своей попой!"
    img 30453
    with diss
    mt "Так я еще ни цента за это не заработала!"
    mt "!!!"
    mt "Может, предложить ему, пусть Эшли идет в приват?"
    img 30454
    with fade
    m "Пусть ваша рыжая королева шлюх идет в приват!"
    m "Я не собираюсь заниматься этим, Джо!" # сердится
    m "!!!"
    music Groove2_85
    img 30455
    with diss
    joe "[monica_pub_name], в этот раз у тебя нет выбора."
    joe "Клиент требует именно тебя."
    joe "И я уже пообещал ему, что ты придешь..."
    joe "Он ждет тебя в подсобке барменов."
    music Stealth_Groover
    img 30456
    with fade
    m "Что значит 'нет выбора'?!"
    m "Выбор всегда есть!"
    m "Я просто не пойду сейчас к клиенту и ты ничего мне не сможешь сделать!"
    m "!!!"
    music Marty_Gots_a_Plan
    img 30457
    with diss
    joe "Да ладно тебе, [monica_pub_name]!"
    joe "Ты ведь уже танцевала в привате для какого-то клиента..."
    joe "Мне Эшли говорила, что он остался тобой очень доволен."

    if monicaPubDanceStoleTipsBankerCompleted == True:
        #
        $ notif(t_("Эшли показала свою голую попу Мистеру Беркельбауху"))
        #
    music Groove2_85
    img 30458
    with fade
    mt "Он остался доволен голым задом твой жены, придурок!"
    mt "Видимо, она тебе об этом ничего не рассказала..."
    img 30459
    with diss
    joe "Не переживай, [monica_pub_name]."
    joe "Он ничего тебе не сделает..."
    joe "Просто посмотрит и все..."
    music Marty_Gots_a_Plan
    img 30460
    with diss
    joe "А я лично проконтролирую, чтобы с тобой ничего не случилось!"
    music Groove2_85
    img 30461
    with fade
    m "Лично?!"
    m "Ты тоже собираешься присутствовать при этом?!"
    m "?!?!?!"
    img 30462
    with diss
    joe "Конечно!"
    joe "Только ради твоей безопасности!"
    joe "Я пообещал тебе, что все будет гладко."
    joe "Поэтому лично прослежу за этим!"

    if pubMonicaWaitressTipsPunishmentJoeStage >= 2:
        # если Моника просила прощения у Джо и показывала ему свою попу
        $ notif(t_("Моника просила прощения у Джо"))
        #
        music Marty_Gots_a_Plan
        img 22875
        with fade
        joe "Тем более, я уже видел твою попку..."
        joe "И не откажусь еще раз посмотреть на нее." # подмигивает

        m "!!!"

    # Подмигивает
    music Groove2_85
    img 30463
    with diss
    joe "Ты просто еще не знаешь сколько клиент обещает за твой приват..."
    m "..."
    $ menu_corruption = [ep212_private_dance1]
    menu:
        "Сколько клиент заплатит за приват?":
            $ monicaPubPrivatDanceJoe1 = True # Моника согласилась пойти в приват
            pass
        "Я не пойду в приват!":
            music Pyro_Flow
            img 30464
            with fade
            mt "Я не собираюсь раздеваться перед каким-то..."
            mt "Никчемным неудачником!"
            mt "Пусть Джо предложит своей жене повертеть голым задом перед клиентом!"
            img 30465
            with diss
            m "!!!"
            m "За кого ты меня принимаешь?!"
            m "Я не пойду ни в какой приват!"
            music Groove2_85
            img 30466
            with fade
            joe "Но [monica_pub_name]!"
            joe "Клиент уже ждет тебя!"
            music Pyro_Flow
            img 30467
            with diss
            m "Это не мои проблемы!"
            m "Ты ему обещал приват, вот ты и танцуй!"
            $ notif_monica()
            if monicaBitch == True:
                m "Мелкое ничтожество!"
            m "!!!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.5
            music Groove2_85
            sound highheels_short_walk
            img 30468
            with fadelong
            w
            # Моника гордо уходит
            return False
    music Groove2_85
    img 30469
    with fade
    m "Сколько клиент заплатит за этот приват?"
    joe "Клиент обещал заплатить 500 долларов за этот приват."
    joe "Подумай только, [monica_pub_name]."
    joe "Один танец и 500 баксов у тебя в кармане."
    joe "Это же так просто - станцуешь перед ним и все!"
    img 30464
    with diss
    mt "500 долларов?"
    mt "..."
    mt "Черт!"

    if monica_escort_service_started == True:
        # если Моника уже работает в эскорте
        $ notif(t_("Моника зарабатывает деньги, обслуживая клиентов в эскорте"))
        #
        img 30470
        with diss
        mt "Я столько за один вечер не всегда могу заработать даже в эскорте..."
        mt "Обслуживая разных извращенцев..."
        mt "А здесь.. Просто раздеться..."
        mt "Без секса и других мерзостей..."

    if slumsApartmentsRentStarted == True:
        # если Моника уже арендует шикарный апартамент
        $ notif(t_("Моника арендует апартаменты у продавца кебабов"))
        #
        img 30471
        with fade
        mt "Этих денег хватит с лихвой, чтобы продлить мои апартаменты на целую неделю..."
        mt "Без всяких скидок от этого грязного Джека!"
    img 30465
    with diss
    m "Джо, я не пойду!"
    m "Этот клиент потом всем расскажет..."
    m "Я не хочу, чтобы все знали об этом."
    m "..."
    img 30472
    with fade
    joe "Об этом можешь не переживать, [monica_pub_name]."
    joe "Я уже предупредил клиента."
    joe "Он никому не скажет."
    # улыбается от уха до уха
    music Marty_Gots_a_Plan
    img 30473
    with diss
    joe "Ты ведь знаешь, [monica_pub_name], что мне можно доверять!"
    sound man_steps
    img 22881
    with fade
    joe "Ну что, пошли?"
    # Джо выходит из гримерки
    # Моника в сомнениях
    music Groove2_85
    img 30474
    with diss
    mt "500 долларов..."
    mt "..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 23315
    with fade
    mt "Если мне что-то не понравится, я пошлю Джо к черту и уйду оттуда."
    mt "И этот никчемный Джо мне ничего не сможет сделать."
#    $ log1 = t_("Пойти в подсобку барменов.")
    return True

# подсобка барменов
label ep212_dialogues2_shiny_hole_2:
    # на диване сидит, развалившись клиент (скучающий чувак у шеста)
    # Джо стоит в стороне и наблюдает
    $ temp_var1 = monica_strip_tips_today
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 30475
    with fadelong
    customer3 "О, наконец-то пришла..."
    img 23321
    with fade
    mt "Фу! Я помню этого клиента..."
    mt "Строит из себя непонятного кого..."
    mt "А на самом деле такой же неудачник, как и все!"
    img 30476
    with diss
    customer3 "Ну давай... Как там тебя зовут?"
    m "Я..."
    customer3 "Впрочем, неважно. Я все равно не запомню."
    img 30477
    with diss
    customer3 "Я рад что ты не как Мэнсфилд..."
    customer3 "Хорошо, что ты такая же шлюха, как та рыжая..."
    music Power_Bots_Loop
    img 30478
    with fade
    mt "!!!"
    mt "Мерзавец!"
    img 30479
    with diss
    m "Я не шлюха!" # зло
    # Джо вмешивается и строго говорит
    music Groove2_85
    img 30480
    with fade
    joe "Не спорь с клиентом!!!"
    # Моника смотрит на Джо
    img 30481
    with diss
    m "!!!"
    customer3 "Да, лучше не спорь..."
    customer3 "Скажи, что ты шлюха. Я доплачу тебе за это 50 баксов."
    img 30482
    with diss
    mt "Что этот неудачник себе позвояет?!"
    mt "?!?!?!"
    $ menu_corruption = [ep212_private_dance2]
    menu:
        "Притвориться шлюхой.":
            $ monicaPubPrivatDanceJoe2 = True # Моника согласилась назвать себя шлюхой
            music Groove2_85
            img 30483
            with fade
            customer3 "Ну, отвечай..."
            customer3 "Ты шлюха?"
            m "..."
            img 30484
            with diss
            mt "Если я сейчас не сделаю, как он просит..."
            mt "Клиент будет недоволен и Джо расскажет об этом Эшли."
            img 30485
            with fade
            mt "И эта извращенка Эшли снова меня оштрафует."
            mt "Я не могу допустить того, чтобы она отбирала у меня деньги..."
            img 30486
            with diss
            mt "Тем более, это не я себя назову шл... Этим словом."
            mt "Это делает [monica_pub_name]..."
            mt "..."
            img 30487
            with fade
            m "Я..."
            m "Шлюха..."
            $ add_money(50.0)
            $ monica_strip_tips_today += 50.0
            img 30488
            with diss
            customer3 "Да..."
            customer3 "Видишь, как все просто?"
            customer3 "Сказала всего два слова и уже заработала полтинник."
            sound Jump2
            img 30489
            with fade
            customer3 "А теперь шлюха станцует для меня."
            customer3 "И получит за это еще денег..."
            customer3 "Шлюха же хочет еще денег?"
            music Power_Bots_Loop
            img 30490
            with diss
            m "..." # зло смотрит на него
            music Groove2_85
            img 30491
            with fade
            customer3 "Скучно с тобой... Даже поговорить не можешь нормально." # лениво
            customer3 "Не удивительно, что ты не можешь устроиться на нормальную работу, как Я..."
            customer3 "А зарабатываешь, показывая свою задницу со сцены..."
        "Поставить на место этого идиота! (Моника слишком приличная) (disabled)" if monicaBitch == False: #
            pass
        "Поставить на место этого идиота!" if monicaBitch == True:
            # Монику бомбит, она орет на клиента
            music Pyro_Flow
            $ notif_monica()
            img 30492
            with fade
            m "Слышишь, ты?!"
#            m "Еще раз назовешь меня шлюхой, я тебе оторву твои яйца!"
            joe "[monica_pub_name]!"
            # рявкает на Джо
            img 30493
            with hpunch
            m "Заткнись, Джо!"
            m "!!!"

                # потом снова на клиента
            img 30494
            with diss
            m "Еще раз назовешь меня шлюхой, я тебе оторву твои яйца!"
#                m "Засунь свои гребанные деньги себе в задницу!"
#                m "Инстинктивное животное!"
#                m "!!!"
            sound highheels_short_walk
            img 30495
            with fade
            w
            # уходит
    music Pyro_Flow
    img 30482
    with diss
    mt "Вот сволочь!"
    mt "Знал бы он, кто Я такая на самом деле!"
    mt "!!!"
    music Groove2_85
    sound heel1
    img 30496
    with fade
    customer3 "Я рад, что я первый, для кого ты танцуешь приват."
    customer3 "Помимо меня еще много желающих посмотреть на твою голую задниицу."
    customer3 "Но я их всех опередил."
    # Джо улыбается ехидно
    music Marty_Gots_a_Plan
    img 30497
    with diss
    joe "..."
    m "..."
    music Groove2_85
    img 30498
    with fade
    mt "Самомнение просто зашкаливает, а на деле..."
    mt "Очередной никчемный неудачник!"
    img 30499
    with diss
    customer3 "Танцуй давай!"
    menu:
        "Начать танцевать.":
            pass
    # Моника начинает танцевать
    # клиент с Джо похотливо на нее смотрят
    music Road_Trip
    img 30500
    with fade
    w
    img 30501
    with diss
    w
    img 30502
    with fade
    w
    img 30503
    with diss
    w
    img 30504
    with fade
    customer3 "Знаешь, ты хоть и скучная, но задница у тебя что надо..."
    customer3 "Я давно хотел, чтобы ты сняла свой наряд официантки и показала мне ее..."
    customer3 "Я видел почти всю твою задницу, когда заглядывал тебе под юбку в прошлый раз."
    customer3 "Но знаешь, так мне будет гораздо удобнее ее разглядеть."
    music stop
    sound plastinka2
    img 30505
    with hpunch
    mt "?!?!?!"
    img 30506
    with diss
    m "Я не..."
    music Groove2_85
    if customer3_dance_comment_stage >= 1:
        # если с клиентом уже был диалог, что он видел ее на сцене, а Моника-официантка это отрицала
        $ notif(t_("Моника говорила клиенту, что не танцует на сцене."))
        #
        img 30507
        with fade
        customer3 "Ну да, ну да..."
        customer3 "Ты не работаешь здесь официанткой... Бла-бла-бла..."
        customer3 "Неважно..."
    img 30508
    with diss
    customer3 "Снимай одежду..."
    customer3 "Я плачу деньги не за танцы в этих тряпках."
    music Power_Bots_Loop
    img 30509
    with diss
    mt "Животное!"
    mt "!!!"
    # Моника танцует и снимает с себя жилет
    # Джо стоит подрачивает под своим фартучком
    # после того как она полностью разделась, клиент достает свой член
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Road_Trip
    $ add_money(100.0)
    $ monica_strip_tips_today += 100.0
    img 23330
    with fade
    w
    img 23331
    with diss
    w
    img 30510
    with fade
    w
    img 30511
    with diss
    w
    img 30512
    with fade
    w
    img 30513
    with diss
    w
    img 30514
    with fade
    w
    img 30515
    with diss
    w
    img 30516
    with diss
    w
    sound vjuh3
    img 30517
    with fade
    w
    img 30518
    with diss
    w
    img 30519
    with diss
    w
    img 30520
    with fade
    w
    img 30521
    with hpunch
    customer3 "Эй ты, смотри что у меня для тебя есть!"
    customer3 "Иди сюда, я хочу потрогать тебя..."
    music Power_Bots_Loop
    img 30522
    with fade
    mt "Начинается!"
    mt "!!!"
    music Groove2_85
    img 30523
    with diss
    m "По правилам бара клиентам на меня можно только смотреть."
    m "Прикасаться нельзя."
    img 30524
    with fade
    customer3 "Да ладно тебе! Заработаешь больше."
    customer3 "Об этом все равно никто не узнает."
    img 30525
    with diss
    customer3 "Да, Джо?" # ехидно улыбается
    joe "Конечно!" # тоже противно улыбается
    joe "Клиент должен быть удовлетворен!"
    img 30526
    with diss
    mt "..."
    $ menu_corruption = [ep212_private_dance3]
    menu:
        "Сделать как требует клиент.":
            $ monicaPubPrivatDanceJoe3 = True # Моника согласилась потереться об клиента попой
            pass
        "Поставить на место этого идиота!": #
            # Монику бомбит, она орет на клиента
            music Pyro_Flow
            $ notif_monica()
            img 30527
            with fade
            m "Слышишь, ты, животное?!"
            m "Засунь свои гребанные деньги себе в задницу!"
            m "И не смей прикасаться ко мне!"
            m "Иначе я тебе яйца оторву!"
            img 30528
            with diss
            joe "[monica_pub_name]!"
            # рявкает на Джо
            img 30529
            with hpunch
            m "Заткнись, Джо!"
            m "!!!"
            # потом снова на клиента
            img 30530
            with diss
            m "Неудачник!"
            m "!!!"
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            img 30531
            with fade
            w
            # уходит
            return -1
    # Моника или злится
    music Pyro_Flow
    img 30532
    with fade
    m "Я здесь танцую, а не занимаюсь проституцией!" # клиенту
    img 30533
    with diss
    m "Джо, ты говорил, что ничего подобного происходить не будет!" # Джо
    m "Что он просто посмотрит и все!"
    m "!!!"
    music Marty_Gots_a_Plan
    img 30534
    with fade
    joe "Все правильно."
    joe "Клиентам к девочкам на привате нельзя прикасаться... Руками..."
    m "???"
    m "Что это значит, Джо?!"
    img 30535
    with diss
    joe "Что ты сейчас удовлетворишь клиента."
    joe "Он тебя трогать при этом не будет."
    joe "Таким образом, ты не нарушишь правила, а клиент останется доволен."
    m "!!!"
    music Pyro_Flow
    img 30536
    with fade
    mt "Мерзавец Джо!"
    mt "О чем я только думала, когда пошла сюда с ним?!"
    mt "?!?!?!"
    music Groove2_85
    img 30537
    with diss
    mt "С другой стороны..."
    mt "Он же не будет прикасаться к моему телу своими грязными руками..."
    mt "А я смогу заработать больше денег..."
    img 30538
    with diss
    mt "Вернее, [monica_pub_name]... Она это будет делать..."
    mt "Моника Бакфетт на такое никогда бы не пошла!"
    mt "Ой, Моника, перестань называть себя по имени даже в мыслях, пока ты здесь!"
    mt "..."
    # клиент встает с дивана
    sound man_steps
    img 30539
    with fade
    customer3 "Мне надоело ждать..."
    customer3 "Подвинься!"
    customer3 "Я хочу, чтоб ты сделала это на столе..."
    img 30540
    with diss
    w
    sound Jump2
    img 30541
    with diss
    w
    # клент ложится на стол
    music Power_Bots_Loop
    img 30542
    with fade
    mt "!!!"
    music Groove2_85
    img 30543
    with diss
    customer3 "Что ты так смотришь?"
    customer3 "Как будто впервые увидела член."
    customer3 "Я заплачу тебе еще 100 баксов."
    customer3 "Давай, отрабатывай..."
    img 30544
    with diss
    mt "Черт!"
    mt "..."
    menu:
        "Тереться о член клиента.":
            pass
    # Джо стоит дрочит
    # Моника неуклюже пристраивается над клиентом так, чтобы можно было тереться об его член
    # но у нее не получается ничего
    music stop
    img black_screen
    with diss
    sound heel1
    pause 1.5
    music Loved_Up
    img 30545
    with fadelong
    w
    img 30546
    with fade
    m "!!!"
    img 30547
    with diss
    customer3 "Ну что ты делаешь?.."
    customer3 "Повернись ко мне своим задом и подвинься ближе."
    # Моника делает, как сказал клиент
    music stop
    img black_screen
    with diss
    sound Jump2
    pause 1.5
    music2 Loved_Up
    img 30548
    with fadelong
    customer3 "Вооот, другое дело!"
    customer3 "Вот так мне нравится больше."
    customer3 "Теперь я могу рассмотреть твою задницу поближе..."

    img 30549
    with fade
    w
    img 30554
    with diss
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_1 = Movie(play="video/v_Monica_Private2_Teasing1_1.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 30550
    with fade
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_2 = Movie(play="video/v_Monica_Private2_Teasing1_2.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 30551
    with diss
    w
    img 30552
    with fade
    w
    img 30553
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_3 = Movie(play="video/v_Monica_Private2_Teasing1_3.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 30555
    with fade
    mt "Долбанный извращенец!"
    mt "!!!"


    music2 Loved_up2
    img 30556
    with diss
    customer3 "Давай, шустрее шевели своей задницей!"
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_4 = Movie(play="video/v_Monica_Private2_Teasing1_4.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    customer3 "Дааа..."
    customer3 "Еще быстрей..."
    # Моника со злым лицом трется о клиента

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_5 = Movie(play="video/v_Monica_Private2_Teasing1_5.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 30557
    with fade
    customer3 "Мммммм..."
    customer3 "Еще немного..."
    customer3 "Вот так..."
    customer3 "Мммммм..."
    menu:
        "Кончить на попу Моники.":
            img 30558
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            customer3 "Аааааа..."
            img 30559
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            customer3 "ААААА..."
            img 30560
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            customer3 "АААААААА!!!"
            img 30561
            with fade
            w
            # Джо тихонько кончает в кулачок
            img 30562
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan6
            joe "Оооох..."
            joe "Ммммммм..."
            # Моника зло на него смотрит
            img 30563
            with fade
            mt "Джо сволочь!!!"
            mt "Твоя жена тебя не видит!"
            mt "!!!"
            $ monicaPubPrivate1CumZone = 1
            pass
        "Кончить на лицо Моники.":
            img 30564
            with diss
            customer3 "Подставь свое лицо!"
            customer3 "Аааааа..."
            customer3 "Быстро!"
            customer3 "Дам за это сверху $ 30!"
            # Моника поворачивается и приближается лицо к его члену
            # он додрачивает и кончает на лицо
            img 30559
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 30565
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            customer3 "ААААА..."
            customer3 "АААААААА!!!"
            img 30566
            with fade
            mt "!!!"
            mt "Фууу!"
            img 30567
            with diss
            customer3 "Аха-ха!"
            $ add_money(30.0)
            $ monica_strip_tips_today += 30.0
            customer3 "Так твое лицо смотрится гораздо лучше!"
            mt "!!!"

            # Джо тихонько кончает в кулачок
            img 30562
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan6
            joe "Оооох..."
            joe "Ммммммм..."
            # Моника зло на него смотрит
            img 30566
#            img 30563
            with fade
            mt "Джо сволочь!!!"
            mt "Твоя жена тебя не видит!"
            mt "!!!"
            $ monicaPubPrivate1CumZone = 2
            pass
    # смена кадра
    # клиент стоит одетый, клиент и Джо расслабленные и довольные, Моника стоит в трусиках, злая
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    $ add_money(100.0)
    $ monica_strip_tips_today += 100.0
    img 30568
    with fadelong
    w
    img 30569
    with fade
    customer3 "Вот твой заработок..."
    customer3 "За то, что неплохо трешься задницей."
    # клиент протягивает деньги
#    customer3 "50 баксов за то, что ты шлюха..."
#    customer3 "100 баксов за танец..."
#    customer3 "И 100 баксов за то, что неплохо трешься задницей..."
    $ temp_var1 = monica_strip_tips_today - temp_var1
    customer3 "Всего [temp_var1]. Ты неплохо заработала!"
    customer3 "Почти ничего не делая..."
    music Power_Bots_Loop
    img 30570
    with diss
    m "[temp_var1] долларов?!"
    m "?!?!?!"
    music Groove2_85
    customer3 "Да..."
    customer3 "Видишь, я могу быть очень щедрым, если шлюха хорошая."
    img 30571
    with diss
    sound man_steps
    w
    # клиент уходит, Моника остается вдвоем с Джо
    # Моника сердито смотрит на него
    music Pyro_Flow
    img 30572
    with fade
    m "[temp_var1] долларов!"
    m "Джо!"
    m "Где обещанные 500?!"
    music Groove2_85
    img 30573
    with diss
    joe "[monica_pub_name], клиент обещал заплатить 500."
    joe "С тем условием, что ему все понравится."
    joe "В противном случае, клиент имеет право снизить сумму."
    joe "Тебе надо было лучше стараться, [monica_pub_name]..."
    mt "!!!"
    img 30574
    with diss
    joe "И не забудь отдать с этих денег процент Эшли."
    # Джо уходит
    sound man_steps
    img 30575
    with fade
    w
    music Pyro_Flow
    img 30576
    with diss
    mt "Он обманул меня!"
    mt "Мерзавец!"
    mt "И я еще должна платить процент Эшли!"
    img 30577
    with fade
    mt "АААААА!!!"
    mt "Ненавижу!"
    mt "!!!"
    return 1

# если Моника в другой день работает официанткой и подходит к этому клиенту и приват с ним уже был
label ep212_dialogues2_shiny_hole_3:
    # использовать имеющиеся арты
    $ questHelp("shinyhole_58a", True)
    music Hidden_Agenda
    sound highheels_short_walk
    img 14261
    with fadelong
    mt "Этот жалкий жадный неудачник!!!"
    mt "!!!"
    m "Что будете заказывать?"
    music Groove2_85
    img 14257
    with fade
    customer3 "О! Хочу снова заказать твою задницу!"
    img 14265
    with diss
    m "Это невозможно, я..."
    img 14263
    with fade
    customer3 "Ты не танцуешь приват. Ага..."
    customer3 "Это всего лишь вопрос денег..."
    customer3 "Аха-ха!!!"
    img 14255
    with diss
    mt "Долбануть бы этого козла чем-нибудь потяжелее!"
    mt "!!!"
    m "Что вам принести?"
    img 14262
    with fade
    customer3 "Какая же ты все-таки скучная..."
    customer3 "Принеси мне пива..."
    # Моника уходит и возвращается с пивом
    img 14266
    with diss
    sound highheels_short_walk
    w

    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    sound snd_plates1
    img 14271
    with fade
    w
    sound snd_beer_table
    img 14272
    with diss
    m "Пожалуйста, ваше пиво..."
    mt "Урод!"
    music Groove2_85
    img 14274
    with fade
    customer3 "Ага..."
    sound vjuh4
    img 23719
    with diss
    w
    sound snd_boot1
    img 23720
    with diss
    customer3 "Я дам тебе $ 10 на чай, если ты нагнешься и поднимешь ту зажигалку."
    customer3 "Только сделай это спиной ко мне! Аха-ха!!!"
    music Power_Bots_Loop
    img 23721
    with fade
    m "!!!"
    # если первый раз
    music Groove2_85
    img 14275
    with diss
    customer3 "Давай, не стесняйся! Я там все уже видел!"
    customer3 "Аха-ха!!!"
    img 23722
    with diss
    mt "Вот мерзавец!"
    mt "Я не собираюсь зарабатывать на чай таким образом!"
    img 23723
    with fade
    mt "..."
    mt "С другой стороны, здесь, похоже, других способов нет..."
    mt "Тем более он уже все видел..."
    img 14288
    with diss
    customer3 "Давай! Сделай это передо мной!"
    customer3 "Здесь больше никого нет!"

    if monicaTakeLightFromFloor == True:
        # если уже было
        music Groove2_85
        img 23723
        with diss
        m "Я уже поднимала эту зажигалку..."
        img 23722
        with fade
        customer3 "Но ведь ты хочешь еще чаевые?"
        customer3 "Тогда подними ее еще раз!"
        #

    img 14286
    with diss
    m "..."
    menu:
        "Нагнуться за зажигалкой.":
            pass
        "Уйти.":
            music Pyro_Flow
            img 14296
            with fade
            sound highheels_short_walk
            m "Сам поднимай свои зажигалки, придурок!"
            return False
    $ monicaTakeLightFromFloor = True
    music Groove2_85
    img 23724
    with fade
    w
    img 23725
    with diss
    mt "Не могу поверить что я это делаю..."
    img 23726
    with fade
    w
    img 23727
    with diss
    w
    img 23728
    with fade
    w
    img 23729
    with diss
    w
    img 23730
    with fade
    w
    img 23731
    with diss
    w
    img 23732
    with fade
    w
    img 23733
    with diss
    w
    $ add_tips(10.0)
    img 23734
    with diss
    customer3 "Отличная задница!"
    img 23735
    with diss
    customer3 "Скоро я всажу в нее свой член!"
    music Power_Bots_Loop
    sound Jump1
    img 23736
    with fade
    m "Этого никогда не будет!!!"
    music Groove2_85
    img 23737
    with diss
    sound highheels_short_walk
    customer3 "Иди уже."
    mt "!!!"
    return True















#
