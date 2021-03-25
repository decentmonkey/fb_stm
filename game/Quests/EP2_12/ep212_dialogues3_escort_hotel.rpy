default monicaEscortAngryWife1 = False  # Моника согласилась раздеться и лечь на пуф
default monicaEscortAngryWife2 = False  # Моника согласилась дрочить клиенту
default monicaEscortAngryWife3 = False  # Моника сказала жене, что ей не нравится секс с ее мужем
default monicaEscortAngryWife4 = False  # Моника ударила жену

default escort3MonicaLikeSex = False
default monicaEscort3CumZone = 0

#call ep212_dialogues3_escort_hotel_1() # Моника за столиком в ресторане, разговор с официанткой
#call ep212_dialogues3_escort_hotel_2() # ресепшн, разговор с китаянкой и брюнеткой
#call ep212_dialogues3_escort_hotel_2_1() # возле лифта
#call ep212_dialogues3_escort_hotel_3() # в номере отеля
#call ep212_dialogues3_escort_hotel_4() # ресепшн, после сцены в номере
#call ep212_dialogues3_escort_hotel_5() # разговор с админом после ухода компании
#call ep212_dialogues3_escort_hotel_5_1() # разговор с админом, если ударила жену
#call ep212_dialogues3_escort_hotel_6() # вышла на улицу после ресепшена, мысли
#call ep212_dialogues3_escort_hotel_7() # вышла на улицу если отказалась работать, мысли
#call ep212_dialogues3_escort_hotel_7_1() # вышла на улицу если ударила жену, мысли
#call ep212_dialogues3_escort_hotel_7_2() # пытается зайти в отель после увольнения, мысли
#call ep212_dialogues3_escort_hotel_7_3() # встречает в ресторане брюнетку после сцены в номере
#call ep212_dialogues3_escort_hotel_8() # ресторан, разговор со служащим отеля

# при выборе пункта меню "Встреча с клиентом (сцена)" (лейбл ep211_escort_scene1_1a), подпункт "Клиент в номере отеля"

# Моника сидит за столиком в ожидании клиента
label ep212_dialogues3_escort_hotel_1:
    # по возможности использовать имеющиеся арты
    music Poppers_and_Prosecco
    img 30084
    with fadelong
    mt "Моника, до сих пор не могу поверить, что ты этим занимаешься..."
    mt "Моника Бакфетт, леди из высшего общества..."
    mt "Сидит за столиком в каком-то никчемном ресторане и ждет клиента..."
    mt "Неужели для тебя это теперь в порядке вещей?"
    img 30085
    with fade
    mt "..."
    mt "С другой стороны, здесь можно неплохо заработать."
    mt "А мне нужны деньги."
    mt "..."
    mt "Это делает не Моника Бакфетт, это делает [monica_hotel_name]."
    img 30061
    with diss
    mt "Для нее - это норма. А деньги достанутся мне!"
    mt "..."
    mt "Да уж, Моника..."
    mt "Так и до биполярного расстройства недалеко..."
    mt "Хотя... Неважно."
    if monicaBitch == True:
        $ notif_monica()
        mt "Это все временно. Скоро я верну свое положение и отомщу всем этим никчемным людишкам!"
    # подходит официантка
    sound highheels_short_walk
    img 30069
    with fade
    waitress "Здравствуйте, Мэм! Администратор Вас ждет на ресепшене."

    if waitressMonicaOffended1 == False and waitressMonicaFired == False:
        #
        $ notif(t_("У Моники хорошие отношения с официанткой."))
        #
        music Groove2_85
        img 30087
        with diss
        mt "Черт!"

        # если была сцена с выездом к клиенту Нэду
        img 30077
        with fade
        mt "Надеюсь, это не выезд к клиенту в какой-нибудь гостевой дом..."
        mt "Где его друзья с женами..."
        m "Я сейчас подойду к ней."

    # официантка уходит

    else:
        #
        $ notif(t_("У Моники плохие отношения с официанткой."))
        #
        music Groove2_85
        img 30070
        with diss
        mt "Снова она!"
        img 30071
        with diss
        m "Что?"
        music Poppers_and_Prosecco
        img 30062
        with fade
        waitress "Мэм... Вас администратор попросила позвать к себе..."
        waitress "Обычно она так зовет к себе проститу... Кхм... Девочек из эскорта..." # подозрительно
        # Моника перебивает ее
        music Stealth_Groover
        img 30072
        with diss
        m "Меня не интересует, что в вашем никчемном ресторане обычно происходит!"
        m "Я не собираюсь выслушивать всякие глупости от какой-то официантки!"
        # официантка уходит
#    $ log1 = t_("Пойти на ресепшн к администратору.")
    return

# ресепшн
label ep212_dialogues3_escort_hotel_2:
    # Моника приходит на ресепшн
    # там стоит девочка из эскорта (брюнетка, карэ) и администраторша
    # они смотрят на Монику
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 17515
    with fadelong
    reception "[monica_hotel_name], есть работа."
    reception "Иди и надень что-нибудь подходящее из белья."
    reception "И быстро. Там клиентка торопится. И нервничает."
    music Pyro_Flow
    img 17516
    with fade
    m "Клиентка?"
    m "???"
    music Groove2_85
    img 17517
    with diss
    reception "Да. То есть, не совсем."
    reception "Это мужчина, наш постоянный клиент."
    reception "Он там с женой. У них в номере семейная сцена."
    reception "Никто из девочек не хочет идти туда."
    img 30111
    with diss
    reception "Но наше заведение обслуживает любых респектабельных клиентов."
    reception "Поэтому пойдете вы вдвоем."
    reception "И сделаете все, как надо!"
    reception "Клиент должен остаться доволен вашей работой!"
    # брюнетка возмущенно, указывая на Монику
    img 17518
    with fade
    girl_1 "Пусть эта идет одна!"
    girl_1 "Я не пойду никуда!"
    img 17519
    with diss
    reception "Так, тихо!"
    reception "Это твой постоянный клиент, поэтому ты пойдешь вместе с [monica_hotel_name]."
    img 17520
    with fade
    m "Зачем тогда мне идти в этот номер, если это ее клиент?"
    img 30113
    with diss
    reception "[monica_hotel_name]!"
    reception "Потому что Я сказала тебе идти туда!"
    reception "Сейчас же прекратите спорить и идите переодеваться!"
    img 17521
    with fade
    reception "Ты, [monica_hotel_name], надень белье под цвет платья." # Монике
    reception "А ты сама разберешься, какое белье больше понравится клиенту." # брюнетке
    reception "Чтобы через 5 минут были в номере!"
    img 17522
    with diss
    reception "В номер заходите сразу в белье, без платьев."
    reception "Все ясно?!"
    reception "Идите!"
    # Моника с брюнеткой недовольно смотрят друг на друга
    img 17523
    with fade
    m "!!!"
    img 17524
    with diss
    girl_1 "!!!"
    img 17525
    with fade
    reception "Поторопитесь!"
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 3.0
    return

# возле лифта
label ep212_dialogues3_escort_hotel_2_1:
    # у Моники под платьем видно белье
    # обе недовольно косятся друг на друга
    m "..."
    girl_1 "..."
    girl_1 "Иди первая..."
    girl_1 "Я зайду следом за тобой..."
    # Моника бросает на нее высокомерный взгляд и заходит в лифт
    m "..."
    return False

# номер отеля
label ep212_dialogues3_escort_hotel_3:
    # Моника с брюнеткой заходят в номер и стоят возле двери. Моника идет впереди
    # семейная пара стоит посреди номера
    # женщина зло смотрит на вошедших девушек
    # мужчина стоит, скукожившись, видно, что боится ее
    music stop
    img black_screen
    with diss
    sound snd_lift
    pause 3.0
#    music Soul4_100
#    music Modern_Jazz_Samba
    music Pyro_Flow
    sound highheels_short_walk
    img 17431
    with fadelong
    wife "Ага!"
    wife "Вот они!"
    wife "!!!"
    img 17447
    with fade
    wife "Смотри, сволочь, пришли твои потаскушки!"
    img 17432
    with diss
    husband "Д-дорогая, п-прошу тебя..."
    wife "МОЛЧАТЬ!!!" # в сторону мужа
    wife "!!!"
    # снова смотрит на девушек
    img 17433
    with fade
    wife "Смотри-ка, как разрядились!"
    wife "У вас обеих прямо на лбу написано, чем вы зарабатываете!"
    img 17448
    with diss
    wife "Давайте раздевайтесь, шлюхи!"
    wife "Пусть этот никчемный дармоед покажет на кого из вас он променял меня!"
    music Groove2_85
    img 17449
    with fade
    m "!!!"
    img 17450
    with diss
    girl_1 "Что смотришь? Давай раздевайся!"
    girl_1 "Так положено!"
    # Моника в шоке смотрит на нее
    music Pyro_Flow
    img 17434
    with fade
    mt "Боже!"
    mt "Какая-то провинциальная дура, а строит из себя..."
    mt "Кто она такая, чтобы разговаривать в таком тоне?!"
    mt "И из-за этих гребаных правил ВИП-эскорта я должна терпеть это??"
    # жена пристально рассматривает девушек, потом поворачивается к мужу (девушек она не видит при этом)
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 17435
    with fadelong
    w
    img 17436
    with diss
    wife "Ну?! Чего ты молчишь?!"
    wife "Говори, к кому из них ты постоянно бегаешь, а?!"
    # муж смотрит на брюнетку, потом на Монику
    img 17451
    with diss
    w
    img 17437
    with fade
    husband "Я..."
    wife "Говори, сволочь неблагодарная!"
    # Моника спокойна, ведь это не ее постоянный клиент
    # брюнетка заметно нервничает
    music Stealth_Groover
    img 17438
    with diss
    mt "Хорошо, что это не мой клиент."
    mt "Сейчас этой сучке из эскорта достанется!"
    mt "А я уйду отсюда."
    mt "И мне не приется иметь дела с этой мерзкой провинциалкой."
    # Клиент подходит к ним вплотную
    music Groove2_85
    sound man_steps
    img 17439
    with fade
    husband "Я... Ходил..."
    img 17452
    with diss
    w
    # Моника смотрит на брюнетку насмешливо, та поворачивается к Монике
    music Stealth_Groover
    img 17440
    with fade
    m "Давай, забирай своего клиента!"
    m "А я ухожу отсюда!"
    # брюнетка смотрит на нее зло и отворачивается
    music Groove2_85
    girl_1 "!!!"
    # брюнетка, пока жена на них не смотрит, шепчет угрожающе мужу
    img 17441
    with diss
    girl_1 "Только попробуй ей сказать правду!"
    girl_1 "!!!"
    girl_1 "Я расскажу ей все твои грязные фантазии!"
    girl_1 "Молчи!"
    girl_1 "!!!"
    img 17442
    with fade
    husband "Я... Ходил... К..."
    img 17453
    with diss
    w
    img 17443
    with fade
    girl_1 "!!!"
    girl_1 "Только попробуй!"
#    girl_1 "Молчи!"
    # жена дает ему подзатыльник, у него очки немного сползают с носа и сидят криво
    music Pyro_Flow
    img 17444
    with diss
    wife "Говори, скотина! Не скажешь ты, я сама узнаю это у их сутенерши!"
    sound vjuh4
    pause 0.5
    sound snd_slap1
    img 17445
    with vpunch
    wife "!!!"
    sound Jump1
    img 17446
#    with diss
    w
    img 17454
    with diss
    husband "Я ходил к... к ней..."
    # указыват пальцем на Монику
    music stop
    sound plastinka1b
    img 17455
    with hpunch
    m "ЧТО?!"
    m "Это неправда!!!"
    m "!!!"
    # брюнетка ехидно улыбается
    music Pyro_Flow
    img 17456
    with diss
    m "Я его первый раз вижу!"
    m "!!!"
    # жена смотрит на Монику презрительно
    music Pyro_Flow
    img 17457
    with fade
    wife "Молчи!"
    wife "Продажная девка!"
    wife "Чтобы я от тебя ни слова не слышала!"
    music Groove2_85

    img 17458
    with diss
    m "!!!"
    mt "Да как она смеет?!"
    # Моника переводит взгляд на мужа, тот стоит, потупив глаза
    img 17459
    with diss
    mt "?!?!?!"
    mt "Жалкий никчемный неудачник!"
    mt "!!!"
    # жена встает, руки в боки
    music Pyro_Flow
    img 17460
    with fade
    wife "Так!"
    wife "Ты снимаешь свои тряпки и ложишься сюда!" # отдает Монике приказ и указывает на пуф возле кровати
    img 17461
    with hpunch
    mt "!!!"
    wife "А ты можешь проваливать отсюда, если хочешь!"
    # ехидно
    music Groove2_85
    girl_1 "Можно я посмотрю?"
    img 17462
    with fade
    wife "Мне все-равно! Но чтобы ни звука!" # брюнетке
    girl_1 "Ладно. Только я оденусь сначала..."
    # несколько минут спустя брюнетка стоит одетая и ехидно улыбается Монике
    # Моника зло смотрит на нее, с ненавистью
    img 17463
    with diss
    m "!!!"
    img 17464
    with diss
    girl_1 "..."
    # затем смотрит на мужа
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Pyro_Flow
    img 17465
    with fade
    wife "И ты, сволочь, раздевайся! Чего стоишь?!"
    husband "Н-но... Дорогая... З-зачем?"
    wife "Покажешь мне, как ты делал с ней ЭТО!"
    husband "В с-смысле?.." # испуганно
    img 17466
    with vpunch
    wife "Я посмотрю, как ты с ней трахаешься, козел!"
    img 17467
    with fade
    husband "Н-но..."
    img 17468
    with diss
    wife "Я сказала раздевайся! Быстро!!!"
    img 17469
    with diss
    wife "А ты чего стоишь?! Не слышала, что тебе сказано делать?!"
    wife "Я деньги за что заплатила, а?!"
    wife "Отрабатывай!"
    # Моника медлит
    music Groove2_85
    img 17470
    with diss
    mt "..."
    menu:
        "Сказать правду и уйти отсюда!":
            # Моника возмущенно
            music Pyro_Flow
            img 17458
            with fade
            mt "Пусть эта сучка с эскорта с ними сама разбирается!"
            mt "Я не собираюсь это терпеть!"
            # указывает на брюнетку
            img 17471
            with diss
            m "Это ее клиент!"
            m "Твой муж тебе солгал, чтобы ее защитить!"
            m "Я его вообще перый раз в жизни вижу!"
            girl_1 "!!!"
            music Soul4_100
            img 17472
            with fade
            wife "Так, ну-ка быстро говори мне правду, козел!" # мужу
            wife "!!!"
            husband "П-прости, д-дорогая..."
            husband "Я... П-просто перепутал..."
            # Моника уходит
            music Pyro_Flow
            sound highheels_short_walk
            img 17473
            with diss
            mt "Сборище жалких неудачников!!!"
            mt "!!!"
            return 0
        "Сделать, как требует клиент.":
            $ monicaEscortAngryWife1 = True # Моника согласилась раздеться и лечь на пуф
            pass
    music Pyro_Flow
    img 17474
    with fade
    mt "Дъявол!"
    mt "Что же мне делать?"
    mt "Эта сучка с эскорта! Ненавижу ее!!!"
    mt "!!!"
    mt "Но если я попытаюсь сказать правду этой провинциальной дуре, она мне не поверит..."
    img 17475
    with diss
    mt "..."
    mt "А если я сейчас откажусь, то меня уволят с этой работы..."
    mt "А мне нужны деньги..."
    mt "Но черт, Моника! Как ты влипла в это?!"
    mt "..."
    # жена рявкает на Монику
    music Groove2_85
    img 17476
    with fade
    wife "Я долго должна ждать?!"
    wife "Я заплатила за час, уже итак прошло много времени!"
    wife "Давай, пошевеливайся!"
    img 17477
    with diss
    mt "Черт! Для [monica_hotel_name] это обычные рабочие будни."
    mt "Просто очередной неудачник..."
    mt "..."
    mt "Зато [monica_hotel_name] сегодня сможет заработать."
    # смена кадра, верх от нижнего белья Моника сняла, она стоит в одних чулках возле пуфа
    # муж стоит рядом в одном галстуке и ботинках, прикрывая свои причиндалы
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 17478
    with fadelong
    wife "Ну, приступайте!"
    wife "Я хочу посмотреть как это выглядит!"
    img 17479
    with fade
    mt "..."
    # Моника опирается руками и коленями на пуф
    # муж в ужасе смотрит на нее
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda
    img 17480
    with fade
    husband "Д-дорогая, д-давай пойдем домой..."
    husband "Т-там и п-поговорим."
    husband "П-пойдем, а?"
    music Pyro_Flow
    img 17481
    with fade
    wife "А ну-ка замолчи!"
    wife "Давай, покажи мне, чем ты занимаешься!"
    wife "Когда врешь мне, что ты допоздна на совещании!"
    wife "Сволочь!"
    music Power_Bots_Loop
    img 17482
    with diss
    mt "Скорее бы это закончилось!"
    mt "Кошмар!"
    music Hidden_Agenda
    img 17483
    with fade
    husband "Д-дорогая..."
    husband "М-можно я не буду этого делать?"
    music Pyro_Flow
    img 17484
    with diss
    wife "Нет! Ты сделаешь сейчас это!!!"
    music Hidden_Agenda
    img 17485
    with fade
    husband "Н-но..."
    husband "У меня не с-стоит..."
    # разводит руки в стороны и показывает свой грустный член
    img 17486
    with diss
    w
    music Pyro_Flow
    img 17487
    with diss
    wife "!!!"
    # жена зло смотрит на него, потом говорит Монике
    img 17488
    with fade
    wife "Ты, шлюха!"
    wife "Давай, делай свою работу!"
    wife "Поднимай его!"
    img 17489
    with diss
    mt "..."
    menu:
        "Сказать правду и уйти отсюда! (прерывание сцены)":
            # Использовать те же арты
            # Моника возмущенно
            music Pyro_Flow
            img 17489
            with fade
            mt "С меня хватит!"
            mt "Пусть эта сучка с эскорта с ними сама разбирается!"
            mt "!!!"
            # указывает на брюнетку
            sound Jump1
            img 17490
            with diss
            m "Это ее клиент!"
            m "Твой муж тебе солгал, чтобы ее защитить!"
            m "Я его вообще перый раз в жизни вижу!"
            img 17491
            with diss
            girl_1 "!!!"
            music Soul4_100
            img 17492
            with fade
            wife "Так, ну-ка быстро говори мне правду, козел!" # мужу
            wife "У тебя поэтому не встает на эту шлюху?"
            husband "П-прости, д-дорогая..."
            husband "Я... П-просто перепутал..."
            music Pyro_Flow
            img 17493
            sound highheels_short_walk
            mt "Сборище жалких неудачников!!!"
            mt "!!!"
            # Моника уходит
            return 0
        "Ударить эту дуру и уйти отсюда! (прерывание сцены и увольнение с эскорта)":
            # Монику бомбит, она подходит к жене и орет на нее
            music Power_Bots_Loop
            img 17494
            with fade
            m "Как ты смеешь так со мной обращаться?!"
            m "Мерзкая провинциальная дура!"
            m "!!!"
            # бьет ее кулаком в нос
            sound anger2
            img 17495
            w
            sound snd_punch_face1
            img 17496
            with hpunch
            wife "АААААААА!!!" # прячет лицо в ладони
            sound snd_woman_scream2
            img 17498
            with diss
            wife "Сучка!!!"
            # муж пугается, но подойти к ним боится, брюнетка в шоке
            music Pyro_Flow
            img 17497
            with fade
            husband "!!!"
            girl_1 "Что ты делаешь?!"
            # Замахивается на нее ладонью
            img 17499
            with diss
            m "Молчи, сучка!"
            # та шарахается в сторону, боится
            m "Разбирайся сама со своим клиентом и его женой-идиоткой!"
            m "!!!"
            img 17500
            with fade
            husband "Я н-нажалуюсь на тебя твоему н-начальству!!!"
            # Моника зло на них смотрит и уходит
            img 17493
            with diss
            sound highheels_short_walk
            m "Да пошел ты, придурок!"
            m "!!!"
            $ monicaEscortAngryWife4 = True # Моника ударила жену
            return -1
        "Сделать, как требует клиент.":
            $ monicaEscortAngryWife2 = True # Моника согласилась дрочить клиенту
            pass
    music Pyro_Flow
    img 17489
    with fade
    mt "Жена - дрянь!"
    mt "Муж - жалкий неудачник!"
    mt "Ненавижу их!"
    # Моника садится на пуф, он стоит рядом, она ему дрочит
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 17501
    with fadelong
    w
    img 17502
    with fade
    w
    img 17503
    with vpunch
    wife "Ну же, шлюха!"
    wife "Через тебя в день проходят десятки членов!"
    img 17504
    with fade
    wife "Ты что, не можешь справиться с этим?!"
    wife "Или у нормальных мужиков на такую грязную шлюху, как ты, не встает?!"
    img 17505
    with diss
    wife "Старайся лучше!"
    music Power_Bots_Loop
    img 17506
    with fade
    mt "Никчемная мерзкая дура!!!"
    mt "!!!"
    # Моника продолжает работать рукой и у него приподнимается
    music Groove2_85
    img 17507
    with diss
    wife "Да неужели!"
    wife "Шлюха встает в позу!"
    wife "А ты, сволочь, быстро засовывай в нее член, пока он не упал снова!"
    # Моника встает снова на пуф, муж пристраивается сзади и пытается засунуть полуэрогированный член в нее
    # у него ничего не получается
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 17563
    with fadelong
    w
    music Hidden_Agenda
    img 17564
    with fade
    husband "Д-дорогая..."
    husband "У м-меня все равно н-не получается..."
    husband "Д-давай, п-прекратим это?"
    music Pyro_Flow
    img 17565
    with vpunch
    wife "Засунь!"
    wife "В нее!"
    wife "Свой член!!!"
    wife "!!!"
    music Groove2_85
    # он снова пытается войти в нее
    img 17566
    with fade
    husband "Ч-черт..."
    husband "Ну же..."
    # брюнетка стоит в стороне и усмехается, Моника видит это
    music Power_Bots_Loop
    img 17567
    with diss
    mt "Сучка!"
    mt "!!!"
    music stop
    music2 Groove2_85
    img 17568
    with fade
    m "У него не получается!"
    m "Он не залезает!"
    # наконец, у него получается и он входит в Монику
    img 17569
    with diss
    wife "Давай, кобель, покажи как ты это делаешь!"
    wife "!!!"
    wife "Что эта грязная потаскуха делает такого, что ты к ней бегаешь?!"
    wife "И тратишь на это наши деньги!"
    # муж шпилит Монику, брюнетка с женой наблюдают
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music2 Turbo_Tornado
    img 17577
    with hpunch
    husband "Вошел!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
    scene black
    image videov_Monica_Escort3_Sex1_1 = Movie(play="video/v_Monica_Escort3_Sex1_1.mkv", fps=30)
    show videov_Monica_Escort3_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17570
    with fade
    husband "Д-дорогая, м-может этого д-достаточно?"
    wife "Нет, сволочь! Продолжай!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
    scene black
    image videov_Monica_Escort3_Sex1_2 = Movie(play="video/v_Monica_Escort3_Sex1_2.mkv", fps=30)
    show videov_Monica_Escort3_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    # жена подходит с другой стороны, так чтобы смотреть на лицо Моники
    img 17571
    with diss
    wife "Ты - падшая грязная женщина!"
    wife "Тебе не противно от самой себя?!"
    # Моника зло смотрит, но молчит
    mt "!!!"
    img 17572
    with fade
    wife "Молчишь?"
    wife "Ты хоть помылась после предыдущего клиента, шлюха?"
    # жена смотрит на мужа
    img 17573
    with diss
    wife "Ну и что, кобель?!"
    wife "Тебе нравится?!"
    # тот продолжает секс
#    music2 Loved_Up2

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
    scene black
    image videov_Monica_Escort3_Sex1_3 = Movie(play="video/v_Monica_Escort3_Sex1_3.mkv", fps=30)
    show videov_Monica_Escort3_Sex1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17574
    with fade
    husband "Н-нет, дорогая..."
    husband "М-мне с-совсем не н-нравится..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
    scene black
    image videov_Monica_Escort3_Sex1_4 = Movie(play="video/v_Monica_Escort3_Sex1_4.mkv", fps=30)
    show videov_Monica_Escort3_Sex1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

#    music2 Groove2_85
    img 17575
    with diss
    wife "..."
    wife "Скажи мне, кто лучше?"
    wife "Эта грязная шлюха или я?"
#    music2 Loved_Up
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
    scene black
    image videov_Monica_Escort3_Sex1_6 = Movie(play="video/v_Monica_Escort3_Sex1_6.mkv", fps=30)
    show videov_Monica_Escort3_Sex1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17576
    with fade
    husband "К-конечно же ты, л-любимая..."
    husband "Т-ты лучше в-всех..."
    wife "С кем тебе больше нравится, сволочь?!"
    img 17577
    with diss
    husband "М-мне нравится т-только с тобой, д-дорогая..."
    husband "Т-ты самая л-лучшая..."
    husband "Д-дорогая... М-может, уже достаточно?"
#    music2 Groove2_85
    img 17578
    with fade
    wife "Нет, кобель!"
    wife "!!!"
    img 17579
    with diss
    wife "Давай, трахай эту дрянь!"
    wife "Я хочу увидеть, насколько она тебе 'не нравится'!"
    # жена снова смотрит на Монику

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
    scene black
    image videov_Monica_Escort3_Sex1_5 = Movie(play="video/v_Monica_Escort3_Sex1_5.mkv", fps=30)
    show videov_Monica_Escort3_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music2 stop
    img black_screen
    with diss
    pause 1.5
#    music Groove2_85
    music2 Turbo_Tornado
    img 17580
    with fade
    wife "Ну что, шлюха?!"
    wife "Тебе нравится?!"
    wife "Тебе нравится, когда тебя трахает чистый и помытый семейный мужчина, А?!"
    wife "Уверена, для тебя это редкость!"
    wife "Отвечай!"
    # Моника зло смотрит на нее
#    music Pyro_Flow
    img 17581
    with diss
    mt "Черт!"
    mt "И что мне ответить этой дуре?!"
    mt "Чтобы она отвязалась от меня!"
    mt "!!!"
    menu:
        "Да, нравится.":
#            music Groove2_85
            img 17582
            with fade
            m "Да..."
            m "Мне нравится..."
            img 17583
            with diss
            wife "Я и не ожидала другого ответа от такой падшей женщины!"
            wife "!!!"
            wife "Спать с чужими мужьями, да еще и брать за это деньги!"
            img 17584
            with fade
            wife "И как тебе не стыдно после этого вообще смотреть мне в глаза!"
            wife "Дрянь!"
            wife "!!!"
#            music Power_Bots_Loop
            img 17585
            with diss
            mt "Дура!"
            mt "Никчемная жирная овца!"
            mt "!!!"
            $ escort3MonicaLikeSex = True
            pass
        "Не нравится.":
#            music Groove2_85
            img 17582
            with fade
            m "Нет..."
            m "Мне не нравится..."
            img 17583
            with diss
            wife "Смотри, кобель!"
            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.3, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Escort3_Sex1_1.ogg"
            scene black
            image videov_Monica_Escort3_Sex1_5 = Movie(play="video/v_Monica_Escort3_Sex1_5.mkv", fps=30)
            show videov_Monica_Escort3_Sex1_5
            with fade
            wife "Ты ее трахаешь! Даешь ей за это деньги!"
            wife "А ей еще и не нравится!!!"
            wclean
            stop music
            music stop
            $ renpy.music.set_volume(1.0, 0.5, channel="music")
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#            music Groove2_85
            img 17584
            with fade
            wife "Вот к такой грязной и бессовестной шлюхе ты бегал все это время?!"
            wife "!!!"
#            music Power_Bots_Loop
            img 17585
            with diss
            mt "Дура!"
            mt "Никчемная жирная овца!"
            mt "!!!"
            $ monicaEscortAngryWife3 = True # Моника сказала жене, что ей не нравится секс с ее мужем
            pass
    # Моника зло смотрит на жену, муж делает еще несколько движений и кончает
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 17587
    with fade
    husband "Ахххххх..."
    wife "Что? Что ты ахаешь?!"
    wife "Ты что, собираешься кончить?!!"
    img 17588
    with diss
    husband "Нет, дорогая, конечно нет, Аххх!!!"
    wife "Ты сказал что тебе не нравится, помнишь?!"
    husband "Да, дорогая, я сказал! Аххххх!!"
    menu:
        "Кончить внутрь Моники.":
            img 17589
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            sound man_moan6
            husband "Ах..."
            husband "Аааах..."
            img 17590
            with fade
            w
            $ monicaEscort3CumZone = 1
            $ monicaCumInside += 1
            pass
        "Кончить на попу Моники.":
            img 17589
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            husband "Ах..."
            husband "Аааах..."
            img 17591
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan6
            w
            img 17592
            with fade
            w
            $ monicaEscort3CumZone = 2
            pass
    music Groove2_85
    img 17586
    with diss
    if monicaEscort3CumZone == 1:
        mt "Этот придурок что, кончил в МЕНЯ?!"
    else:
        mt "Наконец-то, это безумие закончилось!"
    mt "Теперь эта провинциальная дура довольна?!"
    mt "Сняла мужу эскортницу, чтобы посмотреть, как он занимается с ней сексом!"
    mt "Идиотка!"
    mt "!!!"
    # муж испуганно смотрит на жену
    music stop
    img black_screen
    with diss
    pause 1.0
    music Pyro_Flow
    img 17593
    with hpunch
    wife "ЧТОООООО??!!!"
    wife "Раз ты кончил, сволочь, значит тебе понравилось!"
    img 17594
    with diss
    husband "Н-нет... Я..."
    wife "Ты мне врал, что она тебе не нравится!"
    music Hidden_Agenda
    img 17595
    with fade
    husband "Я нечаянно, д-дорогая..."
    husband "П-прости..."
    # Накидывается на него с кулаками
    music Turbo_Tornado
    img 17596
    with diss
    wife "Ах ты мерзавец!!!"
    # затемнение
    # вставить фразы бабах бах!
#    music stop
#    music Turbo_Tornado
    img black_screen
    with diss
    sound snd_kick_fred1
    pause 1.5
    sound snd_punch_face1
    pause 1.0
    husband "Ай! Д-дорогая"
    husband "(BASH!!! BLAM!!! BOP!!!)"
    sound snd_punch_face2
    pause 1.5
    husband "Ой!! АЙ! Ну больно же!"
    husband "(BASH!!! BASH!!!)"
    return 1

# ресепшн
label ep212_dialogues3_escort_hotel_4:
    # китаянка стоит за стойкой ресепшена, вся наша компания стоит перед стойкой
    # жена такая же злая, муж зашуганный, брюнетка довольная собой, Моника злая
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_35
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    img 17536
    with fadelong
    wife "Эта ваша проститутка ни на что не годна!"
    wife "Не понятно, за что я должна вообще платить?!"
    wife "Она что, впервые в жизни видит член?!"
    wife "Как вы такую дрянь вообще взяли на работу?!"
    img 17538
    with fade
    reception "Что случилось?"
    img 17537
    with diss
    wife "У моего мужа не встал на нее!"
    wife "Мало того! Она еще и не смогла ничего сделать с этим!"
    wife "!!!"
    # админ спрашивает у брюнетки, та скажет, что да, не встал у него
    music Groove2_85
    img 17539
    with fade
    reception "У него и правда ничего не получилось?"
    # ехидно
    img 17540
    with diss
    girl_1 "Да, у него не встал."
    # Моника в шоке
    music stop
    sound plastinka1b
    img 17541
    with hpunch
    m "Что?!"
    m "Это..."
    # Моника пытается возразить, но жена на нее рявкает
    music Pyro_Flow
    img 17542
    with fade
    wife "Заткнись!!!"
    wife "!!!"
    # Моника испепеляет взглядом брюнетку
    music Power_Bots_Loop
    img 17543
    with diss
    mt "Вот дрянь!"
    mt "!!!"
    # админ недовольно смотрит на Монику, потом снова спрашивает у брюнетки
    music Groove2_85
    img 17544
    with fade
    reception "[monica_hotel_name] вообще отказалась работать?"
    img 17545
    with diss
    girl_1 "Она старалась что-то сделать..."
    girl_1 "Но у нее ничего не получилось..."
    girl_1 "Просто зря потратила время клиентов."
    mt "!!!"
    # админ обращается к клиентке
    img 17546
    with fade
    reception "Я приношу извинения от лица нашей организации."
    reception "Так как услуга не была вам оказана, то я верну вам деньги."
    img 17547
    with diss
    wife "Хорошо." # недовольно
    wife "А с этой что будете делать?"
    img 17548
    with fade
    reception "Я приму необходимые меры в отношении [monica_hotel_name]."
    reception "Она будет наказана."
    mt "!!!"
    reception "Я ее оштрафую за ненадлежащее исполнение своих обязанностей."
    music Power_Bots_Loop
    img 17549
    with diss
    m "Оштрафуешь?!"
    m "Но..."
    wife "Молчать!!!"
    mt "!!!"
    music Pyro_Flow
    img 17550
    with fade
    wife "Ну что, грязная шлюха?"
    wife "Ты все поняла?!"
    wife "Больше не будешь с ним спать?!"
    # Моника со злостью
    music Power_Bots_Loop
    img 17551
    with diss
    m "Не буду!"
    m "Жирная овца!!!"
    m "!!!"
    # переводит взгляд на брюнетку, та стоит, подмигивает мужу и ехидно улыбается
    # занавес
    return

# ресепшн
# компания разошлась, Моника одна с админом
label ep212_dialogues3_escort_hotel_5:
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 17552
    with fadelong
    reception "[monica_hotel_name]!"
    reception "Мне пришлось вернуть деньги клиентке!"
    reception "Это недопустимо!!!"
    reception "Какого черта, [monica_hotel_name]?!"
    music Power_Bots_Loop
    img 17553
    with fade
    m "Все было совсем не так!"
    m "Эта..."
    music Groove2_85
    img 17548
    with diss
    reception "Я не хочу слышать никаких глупых оправданий!"
    reception "Ты ни цента не получишь за сегодняшнюю работу!"
    reception "А если подобное повторится, то я оштрафую тебя на 1000 долларов!"
    img 17554
    with diss
    reception "У нас ВИП Эскорт! Такое отношение к клиентам недопустимо!"
    reception "Ты поняла меня?!?!"
    m "Да..."
    if char_info["ReceptionGirl"]["level"] == 1 and ep212_escort3_completed == True:
        $ add_char_progress("ReceptionGirl", 25, "ReceptionGirl_escort_scene3")
    music Pyro_Flow
    img 17555
    with fade
    sound highheels_short_walk
    mt "Сучка!"
    mt "Ненавижу!"
    mt "Ненавижу их всех!!!"
    mt "!!!"
    return

# ресепшн
# если ударила жену кулаком
label ep212_dialogues3_escort_hotel_5_1:
    music Groove2_85
    sound highheels_short_walk
    img 30108
    with fadelong
    reception "[monica_hotel_name]!"
    reception "Ты что, уже отработала с клиентами?"
    # Моника с натянутой улыбкой
    img 30107
    with fade
    m "Нет..."
    m "Я тут подумала..."
    m "Знаешь что?!"
    # улыбка исчезает и Моника орет
    music Power_Bots_Loop
    img 17508
    with hpunch
    m "Пошла ты со своим долбанным ВИП-эскортом к черту!!!"
    # админ в шоке
    music stop
    sound plastinka1b
    img 17509
    with diss
    reception "Как ты со мной разговариваешь, [monica_hotel_name]?!"
    # Моника орет
    music Pyro_Flow
    img 17510
    with fade
    m "Я не [monica_hotel_name]!"
    m "И никогда ею не была!"
    m "!!!"
    img 17511
    with diss
    reception "Что?!"
    m "Что слышала!"
    music Groove2_85
    img 30113
    with fade
    reception "?!?!?!"
    reception "А что случилось с клиентами?!"
    reception "Если ты сделала что-то не по правилам..."
    reception "Я наложу на тебя штраф! Будешь отрабатывать его неделями!"
    music Pyro_Flow
    img 17512
    with diss
    m "Сама иди отрабатывай!"
    m "Я ухожу из этого никчемного отеля и возвращаться сюда не собираюсь!"
    m "!!!"
    # Моника разворачивается и идет в сторону выхода, админ зло смотрит ей в след
    img 17513
    with fade
    sound highheels_short_walk
    reception "Стой!"
    # Моника, не поворачиваясь показывает ей фак и уходит
    img 17514
    with diss
    m "!!!"
    mt "Сучка!"
    mt "Ненавижу!"
    mt "Ненавижу их всех!!!"
    mt "!!!"
    # с этого диалога вход в отель заказан
    return


# Моника вышла на улицу после диалога на ресепшене
label ep212_dialogues3_escort_hotel_6:
    # не рендерить!!
    mt "Я терпела эту семейку идиотов ради того, чтобы мне ничего не заплатили?!"
    mt "Мерзкая провинциальная дура!"
    mt "Она специально нажаловалась администратору!"
    mt "Меня тошнит от нее!!!"
    mt "!!!"
    mt "А эта сучка из эскорта!"
    mt "АААААА!!!"
    mt "НЕНАВИЖУ!"
    mt "!!!!!"
    return

# Моника вышла на улицу после того, как отказалась работать и ушла
label ep212_dialogues3_escort_hotel_7:
    # не рендерить!!
    mt "Пусть эта сучка из эскорта сама разбирается с этими идиотами!"
    mt "В отличие от нее, я не какая-то там проститутка!"
    mt "Я - Моника Бакфетт! Я леди!"
    mt "И я не позволю какой-то провинциальной дуре оскорблять себя!"
    return

# Моника вышла на улицу после того, как ударила жену
label ep212_dialogues3_escort_hotel_7_1:
    # не рендерить!!
    mt "Я не [monica_hotel_name]!"
    mt "Я Моника Бакфетт! Я леди!"
    mt "И я не вернусь больше в этот никчемный отель!"
    mt "!!!"
    mt "Когда я верну себе все, что у меня отняли..."
    mt "Я выкуплю этот отель!"
    mt "И уволю всех этих сучек оттуда!"
    mt "Но сначала я им отомщу!!!"
    mt "!!!"
    return

# Если Моника в любой другой день после увольнения с эскорта пытается зайти в отель
label ep212_dialogues3_escort_hotel_7_2:
    # не рендерить!!
    mt "Мне нечего делать в этом никчемном отеле!"
    mt "Не хочу видеть ни этих сучек из эскорта, ни администраторшу!"
    return False

# Моника встречает в ресторане брюнетку после того, как была сцена в номере
label ep212_dialogues3_escort_hotel_7_3:
    # брюнетка смотрит на Монику насмешливо
    music Poppers_and_Prosecco
    img 17526
    with fadelong
    w
    img 17527
    with fade
    mt "Ненавижу эту сучку!"
    sound highheels_short_walk
    img 17528
    with diss
    m "Из-за тебя, дрянь, я в тот вечер ничего не заработала!"
    m "!!!"
    img 17529
    with fade
    girl_1 "Значит, плохо работала!"
    music Pyro_Flow
    img 17530
    with diss
    m "Ты, сучка, трахалась с этим клиентом изо дня в день!"
    m "И все свалила на меня перед его женой!"
    music Poppers_and_Prosecco
    img 17531
    with fade
    girl_1 "Да, ну и что?"
    girl_1 "Я и сейчас с ним... встречаюсь..."
    music Power_Bots_Loop
    img 17532
    with vpunch
    m "Сучка! Никчемная проститутка!"
    music Poppers_and_Prosecco
    img 17533
    with fade
    girl_1 "Скажи еще хоть одно слово и я попрошу его купить тебя."
    girl_1 "Чтобы лизать мою киску... Хи-хи..."
    m "!!!"
    img 17534
    with diss
    girl_1 "Молчишь? Хи-хи!"
    girl_1 "Знай свое место, шлюха!"
    girl_1 "Ты здесь никто!"
    music Power_Bots_Loop
    img 17535
    with fade
    mt "Ненавижу эту тварь!"

#    m "Я все сделала как надо!"
#    m "Если бы ты на ресепшене сказала..."
#    girl_1 "Я видела, как ты работала!"
#    girl_1 "Будь я на месте клиента, тоже не заплатила бы ни цента!"
#    girl_1 "Воообще не понимаю, зачем тебя взяли в наш эскорт!"
#    # осматривает оценивающе
#    girl_1 "Ни внешности, ни опыта..."
#    m "Ты!"
#    m "!!!"
#    m "Ты на себя посмотри, мышь!"
#    m "Проститутки на улице выглядят лучше!!!"
#    girl_1 "Я никогда не видела проституток на улице... И не общалась с ними..."
#    girl_1 "В отличие от тебя..."
#    m "!!!"
#    girl_1 "Так, все!"
#    girl_1 "Мне некогда тут с тобой разговаривать!"
#    girl_1 "Скоро придет мой постоянный клиент..."
#    girl_1 "На этот раз без жены!"
#    girl_1 "Аха-ха!!!"
#    mt "АААААА!!!"
#    mt "НЕНАВИЖУ!"
#    mt "!!!!!"
    return

# при выборе пункта меню "Встреча с клиентом (сцена)" (лейбл ep211_escort_scene1_1a)

# ресторан
# Моника сидит в ожидании клиента
label ep212_dialogues3_escort_hotel_8:
    music Poppers_and_Prosecco
    img 30061
    with fadelong
    mt "Надеюсь, сегодня мне удастся заработать хоть что-нибудь."
    mt "Мне нужны деньги..."
    mt "..."
    # к столику Моники подходит служащий отеля
    sound man_steps
    img 17556
    with fade
    hotel_staff "Мэм..."
    hotel_staff "Добрый вечер, Мэм..."
    music Pyro_Flow
    img 17557
    with diss
    m "?!?!?!"
    m "Ты?!"
    m "Что тебе от меня нужно?!"
    if monicaHotelStaffEscort2 == True:
        #
        $ notif(t_("Моника делала минет служащему отеля в служебном коридоре"))
        #
        img 30087
        with fade
        mt "Снова хочет предложить пойти с ним в уединенное место?!"
        mt "За 50 долларов!!!"
        mt "!!!"
        music Poppers_and_Prosecco
        img 22987
        with diss
        hotel_staff "Мэм, я скопил сумму денег, достаточную для того, чтобы..."
        hotel_staff "Кхм..."
        img 17558
        with diss
        m "Что?"
        hotel_staff "Чтобы уединиться с Вами..."
        m "..."
        $ menu_corruption = [0, monicaHotelHelperScene1CorruptionRequired]
        menu:
            "Нет! Мне не нужны проблемы с администратором.":
                # Моника высокомерно
                music Stealth_Groover
                img 17559
                with fade
                m "!!!"
                m "Нет!"
                m "Во-первых, это запрещено правилами ВИП-эскорта!"
                img 17560
                with diss
                m "Во-вторых, я не хочу с тобой идти после того..."
                m "Как ты бросил тогда меня с администратором!"
                #
                $ notif(t_("Служащий отеля убежал, когда администратор их застукала"))
                #
                music Poppers_and_Prosecco
                img 17561
                with fade
                hotel_staff "Мэм, этого больше не повторится!"
                hotel_staff "Я Вам обещаю!"
                hotel_staff "Мэм..."
                hotel_staff "Я могу заплатить Вам целых 100 баксов за минет!"
                music Stealth_Groover
                img 17562
                with diss
                m "!!!"
                m "Мне не нужны проблемы с администратором из-за тебя!"
                m "Халдей!"
                m "Я леди! И не собираюсь продаваться такому ничтожеству!"
                img 30070
                with fade
                mt "Никчемный неудачник!"
                # Моника зло на него смотрит, тот смутившись, уходит
                return False
            "Сколько денег ты скопил?":
                return True
    return
