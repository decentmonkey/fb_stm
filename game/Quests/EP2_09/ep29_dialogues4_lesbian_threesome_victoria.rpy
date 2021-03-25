# дом Мелани, вечер
# управление продолжается за Мелани
default victoria_drawn_melanie_photo1 = False
default ep29_victoria_melanie_victoria_quest_fully_completed = False
default ep29_victoria_melanie_licking = False # Лизали-ли девочки киску Виктории на девичники
label ep29_dialogues4_lesbian_threesome_victoria_1:
    # Мелани дома одна, как обычно стоит перед зеркалом
    music stop
    img black_screen
    with diss
    pause 2.0
    music ZigZag
    img 15498
    with fadelong
    w
#    melanie_t "Скоро придет эта сучка Виктория. Надо быть с ней осторожнее."
#    melanie_t "Она не должна догадаться, что я ищу способ, как поставить ее на место."
    # Мелани смотрит на часы
    img 15499
    with diss
    melanie_t "Миссис Бакфетт уже должна придти. Надеюсь, она не проигнорирует эту встречу..."
    melanie_t "Интересно, она поняла, о каком друге я ей говорила?"
    sound snd_door_knock
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Master_Disorder
    # стук в дверь
    # Мелани подходит к двери, открывает
    # за ней стоит Моника в наряде шлюхи
    # Моника напряжена, заходит в квартиру, оглядывается
    img 15500
    with fadelong
    m "Мелани?"
    img 15501
    with diss
    melanie "Да, Миссис Бакфетт?"
    img 15502
    with fade
    m "А когда должен придти наш общий друг?"
    # Мелани безэмоционально отвечает
    music ZigZag
    img 15503
    with diss
    melanie "С минуты на минуту, Миссис Бакфетт."
    music Power_Bots_Loop
    img 15504
    with fade
    m "!!!"
    # предлагает ей присесть на диван, на столике перед ним стоит три бокала с вином
    music ZigZag
    img 15505
    with diss
    melanie "Присаживайтесь, Миссис Бакфетт."
    melanie "Не переживайте так. Сделайте глоток вина."

    # Моника смотрит на эти три бокала
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Master_Disorder
    img 15506
    with fadelong
    mt "Если бы случилось что-то страшное... То Маркус не приглашал бы меня выпить вина у Мелани дома..."
    mt "Он тогда, наверняка, послал бы полицейских за мной."
    mt "Хотя... Он же не знает, где я живу."
    img 15507
    with fade
    mt "..."
    mt "Значит, Маркус выбрал квартиру Мелани, чтобы заманить меня сюда!"
    mt "А потом он меня схватит и снова отведет в свой жуткий кабинет!!!"  # если была сцена в тюрьме с анальной пробкой
    if ep28_quests_completed_day > 0: # если была сцена в тюрьме с анальной пробкой
        music Power_Bots_Loop
        img 15508
        with diss
        mt "А у меня нет с собой анальной пробки!"
        mt "Он накажет меня за это!"
    # стук в дверь, Моника в ужасе смотрит на Мелани
    #sound стук в дверь
    sound snd_door_knock
    img 15509
    with diss
    mt "!!!"
    # Мелани смотрит на Монику, она абсолютно спокойна
    # Мелани встает, подходит к двери
    # Мелани открывает дверь, заходит Виктория с сумочкой в руках
    # смотрит на Мелани, потом поворачивается и видит Монику, недобро ухмыляется
    # Моника сидит на диване спиной ко входу и продолжает напряженно смотреть на бокалы, заметно, что она нервничает
    # Виктория подходит к дивану, Моника поворачивает голову и видит, что пришел не Маркус, а Виктория
    # Моника в шоке, вскакивает с дивана, смотрит на Викторию

    img 15510
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Groove2_85
    img 15511
    with fadelong
    w
    img 15512
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Power_Bots_Loop
    img 15513
    with hpunch
    sound plastinka1b
    w
    sound Jump1
    img 15514
    with diss
    w
    img 15515
    with fade
    mt "ВИКТОРИЯ?!"
    mt "Какого черта?!"
    mt "!!!"
    # потом на Мелани
    music Master_Disorder
    img 15516
    with diss
    mt "Как ОНА оказалась у Мелани дома???"
    mt "???"
    # Моника смотрит Мелани
    music stop
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("РАНЕЕ В ЭТОТ ДЕНЬ...")) from _call_textonblack_47
    scene black_screen
    with Dissolve(1)
    # появляется затемнение экрана "Ранее в этот день..."
    return

# возврат в этот же день, игра за Мелани
# после окончания игры за Мелани

# квартира Мелани, управление за Мелани (продолжение сцены)
label ep29_dialogues4_lesbian_threesome_victoria_1a:
    music stop
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("СЕЙЧАС...")) from _call_textonblack_48
    scene black_screen
    with Dissolve(1)
    # Виктория смотрит на Монику с ухмылкой
    music Groove2_85
    img 15517
    with fade
    victoria "Подружка Моника, ты скучала по мне?"
    # Виктория поворачивается к Мелани
    img 15518
    with diss
    victoria "Эта подружка по мне скучала, она всегда так рада меня видеть..."
    victoria "Правда, рада?"
    img 15519
    with fade
    victoria "Что ты делаешь при встрече, подружка Мелани?"
    # пристально с высока смотрит на Мелани и показыват пальцем на свою щеку
    music Master_Disorder
    img 15520
    with diss
    melanie "..."
    img 15521
    with diss
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани немного медлит, потом подходит к ней и чмокает ее в щеку
    # Моника смотрит на это в полнейшем изумлении
    music Groove2_85
    img 15522
    with fade
    sound highheels_short_walk
    w
    music Loved_Up
    img 15523
    with diss
    sound snd_kiss2
    w
    music Master_Disorder
    img 15524
    with fade
    mt "???"
    mt "Виктория указывает Мелани?"
    mt "Я ничего не понимаю..."
    # Мелани садится за столик, берет бокал в руку
    # Виктория говорит Мелани
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 15525
    with fadelong
    victoria "Молодец, ты хорошая подружка."
    # поворачивается к Монике
    img 15526
    with fade
    victoria "А ты?"
    victoria "Ты моя подружка?"
    # Моника нерешительно
    music Master_Disorder
    img 15527
    with diss
    m "Д-да..."
    # Виктория пристально смотрит на Монику
    img 15528
    with fade
    victoria "Скажи это!"
    img 15529
    with diss
    m "Я... Я твоя... Подружка."
    music Power_Bots_Loop
    img 15530
    with fade
    victoria "Скажи это еще раз! Я не расслышала!"
    music Master_Disorder
    img 15531
    with diss
    m "Я твоя подружка!"
    # Виктория продолжает сверлить Монику взглядом
    img 15532
    with fade
    victoria "Ты моя ХОРОШАЯ подружка? Скажи мне!"
    img 15533
    with diss
    m "Да, я хорошая подружка..."
    music Power_Bots_Loop
    img 15534
    with fade
    mt "Какого черта она тут делает?"
    mt "Что ей нужно?"
    img 15535
    with diss
    mt "Может, она хочет, чтобы я платила ей еще больше денег?"
    mt "???"
    # Виктория говорит Монике
    music Groove2_85
    img 15536
    with fade
    victoria "Если ты хорошая подружка, то должна была скучать по мне..."
    victoria "И радоваться нашей встрече."
    victoria "Ты рада видеть меня, подружка Моника?"
    m "..."
    # Моника непонимающе смотрит на Мелани, та сидит за столиком с бокалом в руке и наблюдает за сценой
    # Моника поворачивается снова к Виктории, та вопросительно поднимает брови
    img 15537
    with diss
    victoria "Ты настолько рада, что не можешь найти слов?"
    img 15538
    with fade
    m "Я так рада нашей встрече, что не могу найти подходящих слов..."
    img 15539
    with diss
    victoria "Странно, что ты не можешь сказать мне ничего приятного при встрече."
    victoria "Ты точно скучала по мне?"
    img 15540
    with fade
    m "Да... Скучала..."
    music Power_Bots_Loop
    img 15541
    with diss
    mt "Ненавижу эту маленькую дрянь!!!"
    mt "!!!"
    # Виктория продолжает смотреть на Монику
    music Groove2_85
    img 15542
    with fade
    victoria "Мелани хорошая подружка. Она целует меня при встрече..."
    victoria "А ты? Ты же скучала?"
    victoria "Почему ты не хочешь поцеловать меня?"
    # Моника медлит
    music Master_Disorder
    img 15543
    with diss
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
        "Не делать этого! (пропуск сцены)":
            img 15545
            with fade
            mt "Фу! Мне к ней не то что прикасаться, мне на нее смотреть противно!"
            music Power_Bots_Loop
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            music stop
            img black_screen
            with diss
            sound highheels_run2
            ##### арт Моника убегает
            $ questHelp("victoria_3", False)
            return False
    mt "Просто надо чмокнуть эту стерву в щеку, как сделала Мелани..."
    mt "Тогда она отвяжется от меня."
    img 15544
    with fade
    mt "Фу! Мне к ней не то что прикасаться, мне на нее смотреть противно!"
    mt "!!!"
    # Моника подходит к Виктории и чмокает ее в щеку, та довольно хихикает
    # Виктория подходит к столику, ставит сумочку на него, берет бокал
    img 15545
    with fade
    w
    img 15546
    with diss
    sound highheels_short_walk
    w
    music Loved_Up
    img 15547
    with diss
    w
    img 15548
    with diss
    sound snd_kiss2
    w
    img 15549
    with diss
    sound snd_woman_laugh3
    victoria "Подружка Моника, садись за столик. Девичник начинается!" # хихикает
    # Моника садится напротив Мелани, берет бокал в руку
    # Виктория протягивает свой бокал к ним
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 15550
    with fadelong
    victoria "Подружки, наконец-то мы с вами все вместе встретились..."
    # чокаются со звоном бокалов
    # Виктория с интересом оглядывает квартиру Мелани, та вместе с Моникой смотрят на нее
    img 15551
    with fade
    victoria "Мне нравится квартира моей подружки Мелани..."
    img 15552
    with diss
    victoria "Особенно ее фотографии..."
    victoria "Хочу поближе их рассмотреть. Ты же не против, подружка?"
    # Мелани отвечает равнодушно, не глядя на нее
    img 15553
    with fade
    melanie "Я не против..."
    # Виктория подходит к портретам Мелани на стене и рассматривает их
    sound highheels_short_walk
    img 15554
    with diss
    victoria "Фотографии мне нравятся, но чего-то все равно не хватает..."
    img 15555
    with diss
    victoria "Хмм..." # делает вид, что задумалась
    # Виктория подходит к столику с косметикой, берет помаду Мелани (или достает ее из своей сумочки, если нет столика)
    # потом идет к фотографиям на стене
    # помадой рисует на портрете Мелани ей улыбку
    # Мелани молча бесится, убийственным взглядом наблюдая за этим действием
    sound highheels_short_walk
    img 15556
    with fade
    w
    img 15557
    with diss
    sound swish
    w
    img 15558
    with diss
    sound Jump1
    w
    music Power_Bots_Loop
    img 15559
    with diss
    melanie "!!!"
    # Виктория поворачивается к ней
    music Groove2_85
    img 15560
    with fade
    sound vjuh3
    w
    img 15561
    with diss
    sound vjuh4
    w
    $ victoria_drawn_melanie_photo1 = True
    img 15562
    with fade
    victoria "Так портрет смотрится намного гармоничнее."
    victoria "Ты согласна со мной, подружка Моника?"
    # Моника вопросительно смотрит на Мелани, та зло молчит
    music Power_Bots_Loop
    img 15563
    with diss
    melanie "!!!"
    # Моника снова смотрит на Викторию
    img 15564
    with diss
    m "Да... Так стало еще лучше..."
    # Виктория смеется, потом смотрит на Мелани
    music Groove2_85
    img 15565
    with fade
    sound snd_woman_laugh3
    victoria "А ты что скажешь, подружка Мелани?"
    # Мелани зло на нее смотрит
    music Power_Bots_Loop
    img 15566
    with diss
    melanie "!!!"
    # потом делает глоток из бокала, берет себя в руки и говорит спокойно
    music ZigZag
    img 15567
    with fade
    sound snd_beer_table
    melanie "Я согласна с Миссис Бакфетт."
    music Groove2_85
    img 15568
    with diss
    victoria "В чем именно ты согласна с моей подружкой Моникой?"
    victoria "Скажи мне это!"
    music ZigZag
    img 15569
    with fade
    melanie "Мои портреты стали еще лучше..."
    music Groove2_85
    img 15570
    with diss
    victoria "И кого ты должна поблагодарить за это?"
    music ZigZag
    img 15571
    with fade
    melanie "Тебя... Подружка."
    music Groove2_85
    img 15572
    with diss
    sound highheels_short_walk
    victoria "А как ты меня будешь благодарить, подружка Мелани?"
    # Мелани вопросительно смотрит на нее
    img 15573
    with fade
    melanie "..."
    melanie "Скажу тебе спасибо."
    # Виктория смеется
    img 15574
    with diss
    sound snd_woman_laugh3
    victoria "Этого недостаточно!"
    # Мелани вопросительно поднимает бровь
    # Виктория делает серьезную мину
    music Power_Bots_Loop
    img 15575
    with fade
    melanie "!!!"
    melanie "!!!!!!"
    melanie "!!!!!!!!!"
    w
    music Groove2_85
    img 15576
    with diss
    victoria "Во-первых, не вздумай стирать это со своих фотографий!"
    victoria "Тебе же нравится моя работа?"
    # Мелани напряжанно отвечает
    music Power_Bots_Loop
    img 15577
    with fade
    melanie "Да..."
    music Groove2_85
    img 15578
    with diss
    sound highheels_short_walk
    victoria "Я не слышу!"
    music Power_Bots_Loop
    img 15579
    with fade
    melanie "Да. Мне нравится твоя работа."
    music Groove2_85
    img 15580
    with diss
    victoria "Во-вторых..."
    # делает многозначительную паузу, подходит к столику, за которым сидят Мелани с Моникой
    img 15581
    with fade
    victoria "Во-вторых, я, как и обещала, принесла вам, мои подружки, подарок..."
    # смотрит с улыбкой на Мелани, потом на Монику
    img 15582
    with diss
    victoria "Подружки ведь хотят узнать, какой подарок я для них приготовила?"
    victoria "Это подарок только для хороших подружек..."
    victoria "Вы же хорошие подружки?"
    # Мелани с Моникой переглядываются напряженно
    music Master_Disorder
    img 15583
    with fade
    melanie "..."
    img 15584
    with diss
    m "..."
    img 15585
    with diss
    melanie "Мы хорошие подружки..."
    music Groove2_85
    img 15586
    with fade
    victoria "Чьи вы хорошие подружки?"
    img 15587
    with diss
    m "Твои хорошие подружки..."
    img 15588
    with fade
    victoria "Мои хорошие подружки хотят получить подарок от меня?"
    music Master_Disorder
    img 15589
    with diss
    melanie "Да..."
    # Виктория самодовольно хихикает, ставит одну ногу на столик, смотрит на Монику с Мелани сверху вниз
    # проводит пальцами вверх по своему бедру и немного приподнимает свое платье, становится видно, что она без трусиков
    music Groove2_85
    img 15549
    with diss
    sound snd_woman_laugh3
    w
    img 15590
    with fade
    sound Jump1
    victoria "Тогда подружки должны заслужить свой подарок!"
    img 15591
    with diss
    sound plastinka1b
    w
    img 15592
    with diss
    w
    # Моника с Мелани в шоке смотрят на нее, но ничего не предпринимают
    music Power_Bots_Loop
    img 15594
    with fade
    melanie "..."
    img 15593
    with diss
    m "!!!"
    music Groove2_85
    img 15595
    with fade
    victoria "Подружки, скажите, я красивая? Вам нравится на меня смотреть?"
    img 15596
    with diss
    m "..."
    img 15597
    with fade
    melanie "Ты красивая и нам нравится на тебя смотреть..."
    img 15598
    with diss
    victoria "Раз я вам так нравлюсь, подружки, то я разрешаю вам поцеловать меня..."
    victoria "Кто из подружек хочет сделать это первой, м?"
    # Мелани с Моникой молча переглядываются, лицо Мелани остается безэмоциональным, у Моники отвращение на лице
    music Power_Bots_Loop
    img 15599
    with fade
    melanie "..."
    img 15600
    with diss
    m "!!!"
    music Groove2_85
    img 15601
    with fade
    victoria "Вижу, что вы никак не можете решить, кто из вас будет первой..."
    victoria "Я помогу вам, вы ведь мои хорошие подружки."
    victoria "Вы что, хотите, чтобы я вам помогла?"
    # молчание
    music Master_Disorder
    img 15604
    with diss
    mt "Черт! Она сейчас разозлится..."
    mt "Потом еще и увеличит сумму еженедельных выплат..."
    mt "Где я найду столько денег для нее?!"
    img 15605
    with fade
    mt "Одного слова этой дряни достаточно, чтобы Дик сдал меня Маркусу и его людям..."
    mt "Этот тюфяк полностью в ее власти!"
    mt "!!!"
    music Power_Bots_Loop
    img 15606
    with hpunch
    mt "Неужели мне придется сделать ЭТО?!"
    mt "ФУУУУ! Какая мерзость!!!"
    mt "!!!"
    # Мелани задумчиво смотрит на сумочку Виктории
    music Master_Disorder
    img 15603
    with fade
    melanie_t "Эта мелкая дрянь принесла что-то в сумочке и не хочет это давать просто так..."
    melanie_t "Возможно, это какая-то важная информация."
    melanie_t "Маленькая дрянь хочет сначала поиграться..."
    img 15602
    with diss
    melanie_t "Самый простой выход - притвориться, что я не против."
    melanie_t "Все равно, я скоро найду способ наказать ее за все это..."
    music Power_Bots_Loop
    img 15607
    with vpunch
    victoria "Я НЕ СЛЫШУ ОТВЕТА!"
    victoria "Подружки нехорошие?!"
    victoria "Они хотят меня расстроить?!"
    # Моника с Мелани вздрагивают, смотрят друг на друга, молчание
    music Master_Disorder
    img 15608
    with fade
    melanie "..."
    img 15609
    with diss
    m "..."
    img 15610
    with fade
    menu:
        "Подыграть Виктории":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15604
            with fade
            mt "Я не собираюсь заниматься этими извращенскими мерзостями!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            $ questHelp("victoria_3", False)
            return False
    # Моника, глядя на Мелани
    img 15611
    with diss
    m "Мы не хотим тебя расстраивать... Подружка..."
    # Мелани, глядя на Монику
    img 15612
    with diss
    melanie "Мы хотим, чтобы ты помогла нам... Подружка."
    # поворачиваются к ней
    music Groove2_85
    img 15613
    with fade
    victoria "Так-то лучше!"
    victoria "А то я в какой-то момент стала подозревать..."
    victoria "Что вы только притворяетесь моими подружками..."
    # молчание, Виктория с нехорошей ухмылкой смотрит на них
    music Power_Bots_Loop
    img 15602
    with diss
    melanie "..."
    img 15531
    with diss
    m "..."
    # перемещая палец в сторону Моники
    music Groove2_85
    img 15614
    with fade
    victoria "Итак! Я придумала!"
    victoria "Ты, подружка Моника, помнишь, что тебе нельзя трогать мою киску?"
    victoria "Ты пока допущена только до моей попы!"
    victoria "Ты еще не достаточно хорошая подружка для моей киски."
    # Мелани удивленно приподнимает брови и смотрит на Монику
    img 15615
    with diss
    m "..."
    # Виктория указывает пальцем на Мелани
    img 15616
    with fade
    victoria "Ты, подружка Мелани, трогаешь только мою киску."
    victoria "Попу тебе трогать нельзя. Она только для подружки Моники."
    music Hidden_Agenda
    img 15617
    with diss
    victoria "Я разрешу тебе это делать, потом..."
    victoria "Уверена, ты меня сама попросишь об этом..."
    # обе подружки не торопятся исполнять указание Виктории
    music Power_Bots_Loop
    img 15618
    with fade
    melanie "..."
    m "..."
    music Groove2_85
    img 15619
    with diss
    victoria "Можете начинать! Давайте, я жду!"
    # Виктория поднимает свое платье выше
    # Мелани ставит бокал на стол, бросает еще один взгляд на Монику, поднимается с дивана и подходит к Виктории
    # смотрит на нее в упор
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 15620
    with fadelong
    w
    music Groove2_85
    img 15621
    with diss
    victoria "Я вижу, подружка Мелани, что тебе не терпится поцеловать мою киску. Скажи мне это."
    music Power_Bots_Loop
    img 15622
    with fade
    melanie "..."
    img 15623
    with diss
    menu:
        "Сказать, что приказывает Виктория":
            pass
    img 15624
    with fade
    melanie "Мне... Мне не терпится поцеловать тебя..."
    # Моника все еще на диване и смотрит с отвращением
    music Groove2_85
    img 15625
    with diss
    victoria "Нет, не так! Скажи это еще раз!"
    music Power_Bots_Loop
    img 15626
    with fade
    melanie "Мисс Виктория, мне не терпится поцеловать вашу... Вашу киску..."
    # Виктория, улыбаясь
    music Groove2_85
    img 15627
    with diss
    victoria "Хорошая подружка Мелани."
    victoria "Моей киске тоже не терпится... Она уже вся влажная."
    victoria "На колени!"
    # Мелани медлит, смотрит в глаза Виктории
    music Power_Bots_Loop
    img 15628
    with fade
    melanie "..."
    img 15629
    with diss
    menu:
        "Встать на колени и поцеловать киску Виктории":
            pass
    # Мелани опускается на колени, киска Виктории прямо у нее перед глазами
    # смотрит, потом приближает лицо и прикасается губами к ней
    music stop
    img black_screen
    with diss
    sound snd_paper1
    pause 1.0
    music Loved_Up
    img 15630
    with fadelong
    sound lick10
    victoria "М-м-м-м-м..."
    victoria "Какая хорошая подружка Мелани!"
    img 15631
    with fade
    victoria "Давай еще разочек!"
    # Мелани целует еще раз, потом немного отстраняется
    # Виктория немного разворачивается, киска раскрывается, она кладет руку на голову Мелани
    # потом поворачивается к Монике
    img 15632
    with diss
    victoria "А подружка Моника хорошая?"
    victoria "Или она хочет отказаться от моего подарка и расстроить меня?"
    # Моника молчит
    music Power_Bots_Loop
    img 15606
    with fade
    mt "Фу!!! Я не представляю, как я буду делать это!"
    mt "Какая мерзость!!!"
    mt "!!!"
    # Виктория смотрит на нее в упор, Моника ставит бокал на стол, бросает взгляд на Мелани
    # Моника поднимается с дивана и подходит к Виктории сзади, медлит
    music Master_Disorder
    img 15633
    with diss
    mt "!!!"
    menu:
        "Поцеловать попу Виктории":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15633
            with fade
            mt "Нет! Я, Моника Бакфетт! Я леди!"
            mt "Я не собираюсь целовать тощую задницу этой мелкой стервы!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            $ questHelp("victoria_3", False)
            return False
    # встает на колени
    music stop
    img black_screen
    with diss
    sound snd_paper1
    pause 1.0
    music Groove2_85
    img 15635
    with fade
    victoria "Давай, подружка Моника, целуй меня!"
    victoria "Тебе же нравится моя попа?"
    music Power_Bots_Loop
    img 15636
    with diss
    mt "Твоя попа отвратительна!!! Также как и ты!!!"
    img 15637
    with diss
    m "Да... Нравится..."
    music Groove2_85
    img 15638
    with fade
    victoria "Прикоснись к ней губами."
    # Моника прикасается губами к ягодицам, сначала к одной
    music stop
    stop music
    music2 Loved_Up
    img 15634
    with diss
    sound lick10
    victoria "Да, подружка хорошая! Поцелуй еще!"

    # причесать
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.66666667) + " loop 0.0>Sounds/v_Victoria_Monica_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Monica_Melanie_Licking1_1 = Movie(play="video/v_Victoria_Monica_Melanie_Licking1_1.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Licking1_1
    with fadelong
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    music2 Loved_Up
    # Моника прикасается ко второй ягодице губами
    #victoria "А теперь подружка Моника потрогает руками мою попу..."
    #victoria "Раздвинет ее половинки в стороны и поцелует мою дырочку..."
    # Моника кладет ладони, разводит ягодицы, смотрит, на лице отвращение
    #mt "!!!"
    # Виктория переключается на Мелани
    img 15639
    with fade
    victoria "Хорошая подружка Мелани сейчас поцелует мою киску еще раз."
    victoria "Тебе ведь нравится целовать мою киску, м?"
    music2 Power_Bots_Loop
    img 15640
    with diss
    melanie "Да. Нравится."
    music2 Groove2_85
    img 15641
    with fade
    victoria "Что тебе нравится?"
    music2 Power_Bots_Loop
    img 15642
    with diss
    melanie "Мне нравится целовать твою киску..."
    music2 Loved_Up
    img 15643
    with fade
    victoria "Я разрешаю тебе поцеловать мою киску еще, раз тебе это так нравится."
    # Мелани снова прикасается губами к киске Виктории
    img 15644
    with diss
    victoria "А теперь я разрешаю подружке Мелани потрогать мою киску язычком." # клитор
    victoria "М-м-м-м. Да, хорошая подружка!"
    victoria "И еще раз... Да, так!"

    img 15645
    with fade
    victoria "А теперь подружка Мелани найдет мою дырочку и полижет ее." # влагалище
    victoria "Давай, да!"
    sound lick10
    victoria "А подружка Моника чего ждет?"
    #mt "!!!"
#    victoria "Я ей уже разрешила целовать мою вторую дырочку!"
    # Моника с отвращением прикасается губами к анусу, отстраняется
    # причесать

    img 15646
    with diss
#    victoria "А теперь я разрешаю полизать подружке Монике мою вторую дырочку."
    # Моника проводит кончиком языка
    #mt "Фуууу!!!"
    victoria "А теперь еще раз, подружка Моника! И посмелее!"
    # Моника снова проводит языком по анусу

    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    play music "<from " + str(float(rand(1,4))*1.66666667) + " loop 0.0>Sounds/v_Victoria_Monica_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Monica_Melanie_Licking1_2 = Movie(play="video/v_Victoria_Monica_Melanie_Licking1_2.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Licking1_2
    with fadelong
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    music Loved_Up

    img 15647
    with fade
    victoria "Да, так! Давай! М-м-м-м..."
#    victoria "Подружка Мелани, теперь засунь свой язычок в мою дырочку."
    # Мелани выполняет, начинает двигать языком внутрь-наружу. Моника продолжает лизать.
    # Виктория приспускает лямки на своем платье, обнажает грудь
    # сжимает обеими руками свои соски, откидывает голову назад, глаза закрыты
    sound lick10
    img 15648
    with diss
    sound ahhh1
    w
    img 15649
    with diss
    victoria "Да-а-а... М-м-м-м..."
    img 15650
    with fade
    victoria "Какие подружки хорошие... Как они стараются получить мой подарок..."
    # Виктория наклоняется немного, дотягивается рукой до сумочки, достает из нее телефон
    music stop
    music2 stop
    img black_screen
    with diss
    sound vjuh3
    pause 1.0
    music Loved_Up
    img 15651
    with fadelong
    victoria "Хорошие подружки не останавляваются!"
    victoria "Они продолжают лизать своим язычками мои обе дырочки!"
    w
    sound camera_lens1
    img 15719
    with Dissolve(0.2)
    w
    call photoshop_flash() from _call_photoshop_flash_179
    w
    img 15652
    with fade
    sound lick10
    victoria "Подружки знают, что мне это нравится..."
    w
    call photoshop_flash() from _call_photoshop_flash_180
    w
    # Виктория делает селфи, держа телефон над собой на вытянутой руке, на фото видно головы Моники и Мелани
    victoria "Подружки не должны останавляваться, иначе я огорчусь."
    # Виктория делает еще селфи сбоку, теперь на фото видно лица Моники и Мелани
    # убирает телефон обратно в сумочку, выпрямляется и говорит
    img 15653
    with diss
    victoria "Думаю, что время подарка уже пришло..."
    victoria "Хорошие подружки заслужили подарок!"
    victoria "СТОП!!!"
    # Мелани и Моника отстраняются от Виктории
    # Моника с отвращением вытирает рот рукой, Мелани тоже вытирает рот, при этом заинтересованно смотрит на сумочку Виктории
    # Виктория снимает ногу со стола
    music Groove2_85
    img 15654
    with fade
    victoria "Подружки хорошо постарались..."
    victoria "Пришло время подарка. Кто хочет первый его получить?"
    $ ep29_victoria_melanie_licking = True
    # молчание
    music Master_Disorder
    img 15655
    with diss
    melanie "..."
    img 15656
    with diss
    m "..."
    music Groove2_85
    img 15657
    with fade
    victoria "Мне кажется, что подружка Мелани будет первой..."
    victoria "Потому что ей так хотелось поласкать язычком мою дырочку... Что ее не пришлось заставлять..."
    img 15658
    with diss
    victoria "Да, подружка?"
    victoria "Чтобы получить подарок от меня, тебе нужно снять одежду... И трусики тоже..."
    # Мелани удивленно смотрит на Викторию, продолжая сидеть на коленях
    music Power_Bots_Loop
    img 15659
    with fade
    melanie "Снять одежду и трусики? Зачем?"
    # Виктория смотрит на нее сверху вниз
    music Groove2_85
    img 15660
    with diss
    victoria "Потому что Я тебе так сказала сделать!"
    victoria "Снимай все с себя!"
    img 15661
    with diss
    victoria "И подружка Моника сделает сейчас тоже самое!"
    victoria "Мне же не придется просить ее об этом дважды?!"
    # поворачивает голову и смотрит на Монику
    music Power_Bots_Loop
    img 15543
    with fade
    mt "!!!"
    mt "Какого черта эта стерва здесь устроила?!"
    img 15534
    with diss
    mt "Недостаточно было всех этих извращений?!"
    mt "Что ей еще нужно?!"
    # Мелани смотрит на Монику, та на нее
    music Master_Disorder
    img 15662
    with fade
    melanie_t "Нужно сделать, как эта мелкая дрянь требует. Чтобы она не сомневалась в моем послушании..."
    melanie_t "После этого вечера нужно будет срочно предпринимать меры против нее."
    melanie_t "Она слишком многое себе позволяет..."
    img 15663
    with diss
    menu:
        "Снять одежду":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15604
            with fade
            mt "Это все зашло слишком далеко!"
            mt "Я, Моника Бакфетт, не собираюсь играть по ее правилам!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            $ questHelp("victoria_3", False)
            return False

    # Мелани встает, снимает платье, бросает его на пол
    # Моника смотрит на Мелани, тоже встает и начинает раздеваться
    # Виктория внимательно наблюдает за ними, осматривая их прелести, самодовольно улыбается
    img 15664
    with fade
    w
    img 15665
    with diss
    w
    img 15666
    with diss
    w
    img 15667
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15668
    with fadelong
    w
    img 15669
    with fade
    sound snd_woman_laugh3
    victoria "Я уверена, что вам понравится мой подарок."
    victoria "Я его выбирала специально для вас, мои подружки!"
    # Виктория снимает с себя платье, подходит к столику, берет сумочку и обходит диван с другой стороны
    # стоит спиной к Мелани и Монике
    # те заинтересованно на нее смотрят, переглядываются между собой, им не видно, что там делает Виктория
    # через несколько минут
    # камера на Викторию, она стоит спиной, на ней надеты стринги, голову в полоборота
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Master_Disorder
    img 15670
    with fadelong
    sound swish
    w
    img 15671
    with fade
    w
    music Groove2_85
    img 15672
    with diss
    victoria "Подружка Моника садится на диван и смотрит!"
    victoria "Подружка Мелани, ты готова увидеть подарок?"
    # Моника садится на диван
    img 15673
    with fade
    melanie "Да..."
    img 15674
    with diss
    victoria "Что 'да'?"
    victoria "Ты хочешь сказать, что ты хорошая подружка... И будешь рада получить от меня подарок?"
    victoria "Скажи мне это. Я хочу это услышать..."
    img 15675
    with fade
    melanie "Я хорошая подружка и буду рада получить подарок от мисс Виктории."
    # Виктория довольно ухмыляется и поворачивается к Мелани и Монике
    # на ней надет страпон какого-нибудь нелепого цвета (н-р, ярко-розовый)
    # у ее подружек шок !!! даже у Мелани
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    img 15676
    with diss
    w
    sound vjuh4
    img 15700
    with diss
    sound plastinka1b
    w
    music Power_Bots_Loop
    img 15677
    with hpunch
    melanie "!!!"
    img 15678
    with fade
    melanie_t "Страпон?!"
    melanie_t "Она решила подарить мне СТРАПОН?!"
    melanie_t "Мерзкая сучка! Она заставила нас думать, что у нее есть какой-то компромат!"
    img 15679
    with hpunch
    m "!!!"
    img 15680
    with fade
    mt "ЧТО?!"
    mt "Мне пришлось вылизывать ее зад, чтобы она подарила эту ужасную штуку!!!"
    img 15681
    with diss
    mt "!!!"
    mt "Ненавижу!!!"
    # Виктория довольна произведенным эффектом
    music Groove2_85
    img 15682
    with fade
    victoria "Мои хорошие подружки рады подарку?"
    victoria "Подружка Мелани, тебе нравится?"
    # Мелани молчит и смотрит на нее, как на сумасшедшую
    music Power_Bots_Loop
    img 15683
    with diss
    melanie "..."
    music Groove2_85
    img 15684
    with fade
    victoria "Я вижу, что тебе нравится мой подарок, подружка Мелани."
    victoria "Тебе не терпится ощутить его внутри себя. Но ты стесняешься признаться в этом..."
    victoria "Не стоит стесняться, подружка. Скажи мне это!"
    # смотрит на Мелани пристально
    music Power_Bots_Loop
    img 15685
    with diss
    melanie "..."
    img 15686
    with diss
    menu:
        "Сказать, как приказывает Виктория":
            pass
        "Отказаться!":
            music Master_Disorder
            img 15687
            with fade
            melanie_t "Я не позволю это мелкой дряни так унижать меня..."
            melanie_t "Да еще и в присутствии Миссис Бакфетт."
            # Мелани смотрит на Викторию пристально
            img 15688
            with diss
            melanie "Я думаю, Мисс Виктория, что подружки не дарят друг другу такие подарки..."
            # Виктория строго смотрит на нее, подходит к ней, говорит с угрозой
            music Power_Bots_Loop
            img 15689
            with fade
            victoria "ХОРОШИЕ подружки дарят, Мисс Мелани!!!"
            victoria "Хотя... Мы можем перестать быть хорошими подружками прямо сейчас."
            img 15690
            with diss
            victoria "У меня есть другой подарок... Для нашего общего друга...."
            victoria "Он им очень заинтересуется... Мисс Мелани..."
            img 15691
            with diss
            melanie "..."
            # Мелани смотрит на Викторию высокомерно
            music Master_Disorder
            img 15692
            with fade
            melanie_t "Я не просто избавлюсь от нее."
            melanie_t "Сначала я ей отомщу. Заставлю пожалеть о том, что она сейчас делает."
            music Groove2_85
            img 15693
            with diss
            victoria "Итак! Что хорошая подружка сейчас должна мне сказать?"
            pass
    music Master_Disorder
    img 15694
    with fade
    melanie "Мне... Не терпится... Получить от вас подарок, мисс Виктория..."
    img 15695
    with diss
    victoria "Точно не терпится? Ты уверена?"
    img 15696
    with fade
    melanie "Да, мне не терпится..."
    img 15697
    with diss
    victoria "Что именно тебе хочется, м? Скажи мне!"
    music Power_Bots_Loop
    img 15698
    with fade
    melanie "Мне не терпится ощутить ваш подарок внутри меня... мисс Виктория."
    # Виктория смотрит Мелани в глаза и ухмыляется

#label v_Victoria_Melanie_Sex_test:

    music Groove2_85
    img 15699
    with diss
    victoria "На колени!"
    victoria "Оближи его как следует! Покажи мне, как ты хочешь его!"
    # Мелани медлит, потом опускается на колени, облизывает дилдо
#    sound vjuh3
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 15701
    with fadelong
    w
    img 15702
    with diss
    w

    img 15703
    with diss
    w
    img 15704
    with fade
    victoria "Вот так, да!"
    victoria "Теперь возьми его в рот!"
    victoria "Я хочу, чтобы ты отсосала у меня, мисс Мелани!"
    music Power_Bots_Loop
    img 15705
    with hpunch
    mt "О боже! Какой кошмар!"
    mt "Я не смогу этого сделать!"
    mt "!!!"
    music Loved_Up
    img 15706
    with fade
    w
    ################################
    img black_screen
    with diss
    scene black
    image videov_Victoria_Monica_Melanie_Blowjob1_1 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_1.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Blowjob1_1
    with fadelong
    wclean
    ################################
    if game.extra == True:
        ################################
        img black_screen
        with diss
        scene black
        image videov_Victoria_Monica_Melanie_Blowjob1_2 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_2.mkv", fps=30)
        show videov_Victoria_Monica_Melanie_Blowjob1_2
        with fadelong
        wclean
        ################################
    # запихивает дилдо ей в рот, Мелани давится, отстраняется, дилдо становится мокрым, с него тянется слюна
    # Моника с ужасом наблюдает
    # Виктория строго говорит Мелани
    ################################
    ################################
    img 15707
    with diss
    w


    img black_screen
    with diss
    scene black
    image videov_Victoria_Monica_Melanie_Blowjob1_4 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_4.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Blowjob1_4
    with fadelong
    wclean
    ################################
    if game.extra == True:
        img black_screen
        with diss
        scene black
        image videov_Victoria_Monica_Melanie_Blowjob1_3 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_3.mkv", fps=30)
        show videov_Victoria_Monica_Melanie_Blowjob1_3
        with fadelong
        wclean
    img 15708
    with fade
    w
    ################################
    img 15709
    with diss
    w

    music Groove2_85
    img 15710
    with fade
    victoria "Теперь на диван! Встань на колени и покажи мне свой фирменный зад!"
    # та поднимается, убивает Викторию взглядом, но исполняет
    # Виктория встает сзади нее (доги-стайл), шлепает ее по ягодице
    music Power_Bots_Loop
    img 15711
    with diss
    w
    music Master_Disorder
    img 15712
    with fade
    sound highheels_short_walk
    w
    img 15720
    with diss
    w
#    img 15721
#    sound vjuh4
#    pause 0.5
#    sound snd_slap1
#    img 15722
#    with vpunch
#    melanie "Ах!"
#    img 15723
#    with diss
#    w
    ################################
    img v_Victoria_Melanie_Spanking1_1_start
    with fade
    w
    scene black
    sound v_Victoria_Melanie_Spanking1_1
    image videov_Victoria_Melanie_Spanking1_1 = Movie(play="video/v_Victoria_Melanie_Spanking1_1.mkv", fps=30, loop=False, image="/images/Slides/v_Victoria_Melanie_Spanking1_1_end.jpg")
    show videov_Victoria_Melanie_Spanking1_1
#    sound2 vjuh4
    pause 0.5
#    sound2 snd_slap1
    melanie "Ах!"
    music Master_Disorder
    wclean
    #################################

    # у Мелани остается красный отпечаток на попе
    music Master_Disorder
    img 15724
    with fade
    victoria "Какая отличная задница у вас, Мисс Мелани!"
    # шлепает еще раз

    ################################
    if game.extra == True:
        img v_Victoria_Melanie_Spanking1_2_start
        with fade
        w
        scene black
        sound v_Victoria_Melanie_Spanking1_2
        image videov_Victoria_Melanie_Spanking1_2 = Movie(play="video/v_Victoria_Melanie_Spanking1_2.mkv", fps=30, loop=False, image="/images/Slides/v_Victoria_Melanie_Spanking1_2_end.jpg")
        show videov_Victoria_Melanie_Spanking1_2
    #    sound2 vjuh4
        pause 0.5
    #    sound2 snd_slap1
        melanie "Ах!"
        music Master_Disorder
        wclean
        #################################

    music stop
    img black_screen
    with diss
    pause 1.5
#    music Master_Disorder
    sound chpok6
    img 15725
    with hpunch
    w
    music Loved_Up2
    img black_screen
    with diss
#    music stop
#    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_1 = Movie(play="video/v_Victoria_Melanie_Sex1_1.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_1
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    img 15726
    sound vjuh4
    pause 0.5
    sound snd_slap1
    img 15727
    with vpunch
    melanie "Ах!"




    img 15728
    with fade
    victoria "Тебе ведь нравится, подружка Мелани?"
    victoria "Скажи, что хочешь еще! Говори!!!"
    music Power_Bots_Loop
    img 15729
    with diss
    melanie "Мне... Мне нравится..."
########################################
    music Loved_Up2
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_4 = Movie(play="video/v_Victoria_Melanie_Sex1_4.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_4
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")



########################################
    # Виктория снова шлепает ее, ягодицы у Мелани становятся красными
#    music Master_Disorder
    img 15730
    with diss
    sound vjuh4
    pause 0.5
    sound snd_slap1
    img 15731
    with vpunch
    melanie "Ах!"
    # Виктория направляет дилдо в киску Мелани и вводит его
    # Моника продолжает с ужасом смотреть на эту картину
#    music Power_Bots_Loop
    img 15732
    with fade
    mt "!!!"
    # Виктория поворачивается к Монике, при этом двигается в Мелани, схватив ту за волосы
########################################
    music Loved_Up2
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_2 = Movie(play="video/v_Victoria_Melanie_Sex1_2.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_2
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
########################################

    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 15733
    with fadelong
    victoria "Подружка Моника, тебе нравится смотреть на нас?"
    victoria "Скажи, что тебе нравится!"
    music Power_Bots_Loop
    img 15734
    with fade
    mt "!!!"
    menu:
        "Сказать Виктории, что мне нравится":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15735
            with fade
            mt "Это отвратительно!"
            mt "Эта Виктория - спятившая извращенка!!!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            $ questHelp("victoria_3", False)
            return False
    m "Д-да... Нравится..."
    img 15735
    with diss
    mt "Это отвратительно!"
    mt "Эта Виктория - спятившая извращенка!!!"
    mt "!!!"
    music Loved_Up
    img 15736
    with fade
    victoria "Что именно тебе нравится?"
    victoria "Ты хочешь оказаться на месте нашей подружки? Скажи мне!"
    music Power_Bots_Loop
    img 15738
    with diss
    mt "Нет-нет! Это так мерзко!!!"
    music Loved_Up
    img 15737
    with fadelong
    m "Д-да..."
    img 15739
    with fade
    victoria "Тогда раздвинь ноги и подготовь свою киску для меня."
    victoria "Покажи мне, как тебе нравится смотреть на меня."
    music Power_Bots_Loop
    img 15681
    with diss
    mt "!!!"
    menu:
        "Раздвинуть ноги":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15738
            with fade
            mt "Это отвратительно!"
            mt "Пошла она к черту!!!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            $ questHelp("victoria_3", False)
            return False
    # Моника подчиняется, раздвигает ноги, смотрит на Викторию
    music Loved_Up
    img 15740
    with fadelong
    victoria "Теперь ласкай свою киску!"
    victoria "Я хочу посмотреть, как ты это делаешь!"
    img 15741
    with diss
    mt "ЧТО!?"
    # Моника опускает руку и прикасается к себе там, начинает водить пальцами по киске
    # Виктория самодовольно ухмыляется
    music Loved_Up2
    img 15742
    with diss
    w

########################################
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_3 = Movie(play="video/v_Victoria_Melanie_Sex1_3.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_3
    with fadelong
    wclean
    stop music2

    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_7 = Movie(play="video/v_Victoria_Melanie_Sex1_7.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_7
    with fadelong
    wclean
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    stop music2
########################################

#    music Loved_Up
    img 15743
    with diss
    w
    img 15744
    with fade
    victoria "Нравится тебе?"
#    music Power_Bots_Loop
    img 15745
    with diss
    m "Да..."
    # Виктория снова шлепает Мелани по ягодицам и продолжает натягивать ее на свой страпон

########################################
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_5 = Movie(play="video/v_Victoria_Melanie_Sex1_5.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_5
    with fadelong
    wclean
    stop music2
    if game.extra == True:
        stop music2
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
        scene black
        image videov_Victoria_Melanie_Sex1_6 = Movie(play="video/v_Victoria_Melanie_Sex1_6.mkv", fps=30)
        show videov_Victoria_Melanie_Sex1_6
        with fadelong
        wclean
        stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
########################################
#    music Loved_Up
    img 15746
    with diss
    sound vjuh3
    w
    img 15747
    with diss
    sound snd_slap1
    pause 0.5
    img 15748
    with hpunch
    melanie "Ах!"
    # Виктория спрашивает у Мелани
    img 15749
    with fade
    victoria "Тебе нравится, подружка Мелани?"
    victoria "У тебя такая киска! Она вся влажная!"
    img 15750
    with diss
    victoria "Я вижу, что тебе нравится..."
    victoria "Подружка Моника, тебе нравится киска нашей подружки Мелани?"
#    music Power_Bots_Loop
    img 15751
    with fade
    m "Нравится..."

########################################
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_8 = Movie(play="video/v_Victoria_Melanie_Sex1_8.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_8
    with fadelong
    wclean
    stop music2

    if game.extra == True:
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
        scene black
        image videov_Victoria_Melanie_Sex1_9 = Movie(play="video/v_Victoria_Melanie_Sex1_9.mkv", fps=30)
        show videov_Victoria_Melanie_Sex1_9
        with fadelong
        wclean
        stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

##########################################
    music Loved_Up
    img 15752
    with diss
    victoria "А твоя киска уже стала влажной?"
    victoria "Она готова к тому, чтобы я вошла в нее?"
    music Power_Bots_Loop
    img 15753
    with fade
    mt "!!!"
    mt "Боже! Какой кошмар!!!"
    img 15754
    with diss
    mt "Я не хочу говорить ей это! Какая пошлость!!!"
    mt "!!!"
    music Groove2_85
    img 15755
    with fade
    victoria "Подружка Моника, я не слышу... Скажи мне это!"
    # сама в это время продолжает натягивать Мелани, делает это жестко, держа ее за волосы
    img 15756
    with diss
    m "Да... Готова..."
    img 15757
    with fade
    victoria "К чему ты готова, подружка Моника?"
    music Power_Bots_Loop
    img 15758
    with diss
    m "Готова к тому, чтобы ты... Вошла в меня..."
    music Loved_Up
    img 15759
    with fade
    victoria "Хорошая подружка! Мне нравится, что ты такая послушная."
    # Виктория еще раз шлепает Мелани по попе, у нее она вся красная от шлепков
    sound vjuh3
    img 15726
    with diss
    pause 0.5
    sound snd_slap1
    img 15727
    with hpunch
    melanie "Ах!"
    img 15760
    with diss
    sound chpok6
    victoria "Подружка Мелани тоже хорошая!"
    victoria "Можешь теперь посмотреть на то, как я дарю подарок подружке Монике!"
    # вытаскивает из нее дилдо с хлюпом, отпускает ее волосы
    # Мелани встает, волосы растрепаны, смотрит ненавидящим взглядом на Викторию, но молчит
    music Power_Bots_Loop
    img 15761
    with fade
    melanie "..."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    # садится на диван, берет бокал вина и делает несколько глотков
    # Виктория смотрит на Монику, с ухмылкой подзывает ее к себе пальчиком
    img 15762
    with fade
    w
    img 15763
    with diss
    menu:
        "Встать коленями на диван и нагнуться":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15681
            with fade
            mt "Это отвратительно!"
            mt "Пошла она к черту!!!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            $ questHelp("victoria_3", False)
            return False
    mt "У Мелани все получилось... И я смогу. Я сильная."
    mt "!!!"
    mt "Скорее бы эта извращенка ушла отсюда!"
    # Моника подходит к дивану, нерешительно смотрит на Викторию. та пальцем ей показывает на диван
    # Моника встает в ту же позу, что и Мелани. Виктория смотрит на нее сзади, шлепает ее по ягодице
    sound Jump1
    img 15764
    with fade
    w
#    img 15765
#    with diss
#    sound vjuh3
#    pause 0.5
#    sound snd_slap1
#    img 15766
#    with hpunch
    img v_Victoria_Monica_Spanking1_2_start
    with fade
    w
    scene black
    sound v_Victoria_Monica_Spanking1_2
    image videov_Victoria_Monica_Spanking1_2 = Movie(play="video/v_Victoria_Monica_Spanking1_2.mkv", fps=30, loop=False, image="/images/Slides/v_Victoria_Monica_Spanking1_2_end.jpg")
    show videov_Victoria_Monica_Spanking1_2
#    sound2 vjuh4
    pause 0.5
#    sound2 snd_slap1
    m "Ах!"
    music Master_Disorder
    wclean
    img 15767
    with diss
    w
    img 15768
    with diss
    victoria "Нет, подружка Моника!"
    victoria "Я хочу видеть твое лицо!"
    victoria "На спину!"
    # Моника ложится на спину, Виктория задирает ее ноги вверх, открывая себе доступ к ее киске и грубо входит в нее
    # Моника ойкает, гримаса боли
    music stop
    img black_screen
    with diss
    sound vjuh3
    pause 1.0
    music Groove2_85
    img 15769
    with fadelong
    w
    img 15770
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 15771
    sound chpok6
    with hpunch
    m "Аааа!"


    img 15772
    with fade
    victoria "М-м-м... Как же мне нравится ваша киска, Миссис Бакфетт."
    victoria "Вы ее хорошо подготовили для меня. Вы хорошая подружка, Миссис Бакфетт..."
    # выходит из нее полностью, снова направляет дилдо в киску и опять грубо входит
    # у Моники снова гримаса боли, Виктория смотрит на нее и довольно улыбается

    img 15773
    with diss
    victoria "Тебе нравится чувствовать в себе мой подарок? Скажи, что тебе нравится!"
    music Power_Bots_Loop
    img 15774
    with diss
    m "М-мне... Н-нравится чувствовать в себе... Это..."
    # Виктория снова выходит и входит, Моника ахает
    music Loved_Up2
    img 15775
    with hpunch
    m "Ай!"


    img 15776
    with diss
    victoria "Что именно тебе нравится, подружка Моника?"
    victoria "Я хочу услышать это!"
    img 15777
    with fade
    m "М-мне... Н-нравится как ты... Делаешь это..."

    img 15778
    with diss
    victoria "Что 'ЭТО'?"
    victoria "Монике Бакфетт нравится, что я трахаю ее искусственным членом?"
#    img 15779
#=======================================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_1 = Movie(play="video/v_Victoria_Monica_Sex1_1.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_1
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #=======================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_2 = Movie(play="video/v_Victoria_Monica_Sex1_2.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_2
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #=======================

    music Power_Bots_Loop
    img 15780
    with fade
    m "Д-да-а..."
    mt "Когда же этот кошмар уже закончится?!"
    mt "!!!"
    # Виктория начинает двигаться туда-обратно, удерживая ноги Моники, смотрит на ее лицо
    # Мелани пьет вино и смотрит с каменным лицом на разыгрывающуюся перед ней сцену
    # Виктория поворачивается к Мелани и ухмыляется
    music Loved_Up2
    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_3 = Movie(play="video/v_Victoria_Monica_Sex1_3.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_3
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================
    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_4 = Movie(play="video/v_Victoria_Monica_Sex1_4.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_4
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================

    if game.extra == True:
        #========================
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        img black_screen
        with diss
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
        scene black
        image videov_Victoria_Monica_Sex1_5 = Movie(play="video/v_Victoria_Monica_Sex1_5.mkv", fps=30)
        show videov_Victoria_Monica_Sex1_5
        with fadelong
        wclean
        stop music2
        $ renpy.music.set_volume(1.0, 0.5, channel="music")
        #======================

    img 15781
    with diss
    victoria "Хотелось бы тебе оказаться на моем месте, подружка Мелани?"
    # Мелани вопросительно поднимает бровь, но молчит
    img 15782
    with fade
    melanie "..."

    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_6 = Movie(play="video/v_Victoria_Monica_Sex1_6.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_6
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================

    img 15783
    with diss
    victoria "Возможно, в следующий наш девичник... Я разрешу тебе побыть на моем месте, подружка..."
    victoria "Скажи, что хочешь этого!"
    music Power_Bots_Loop
    img 15784
    with fade
    melanie "..."
    melanie "Да, я хочу этого..." # равнодушно
    # Виктория самодовольно улыбается, смотрит на Мелани, продолжая двигаться в Монике
    # потом поворачивается к Монике, ускоряет движения
    music Loved_up2
    if game.extra == True:
        #========================
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        img black_screen
        with diss
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
        scene black
        image videov_Victoria_Monica_Sex1_7 = Movie(play="video/v_Victoria_Monica_Sex1_7.mkv", fps=30)
        show videov_Victoria_Monica_Sex1_7
        with fadelong
        wclean
        stop music2
        $ renpy.music.set_volume(1.0, 0.5, channel="music")
        #======================

    img 15785
    with diss
    victoria "М-м-м-м... Да-а-а!"
    victoria "Как же охренительно трахать саму Монику Бакфетт!"

    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_8 = Movie(play="video/v_Victoria_Monica_Sex1_8.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_8
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================

    img 15786
    with fade
    victoria "А-а-а-а"
    victoria "Да-а!!!"
    # еще несколько резких движений и Виктория кончает
    img 15787
    sound woman_moan14
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    victoria "ААААА!!!"
    victoria "Чертовски здорово!!! Да-а-а-а!!!"
    # Виктория отпускает ноги Моники, с хлюпом вытаскивает из нее дилдо
    # садится на диван в расслабленной позе, страпон торчит вверх, весь мокрый
    music stop
    img black_screen
    with diss
    sound chpok6
    pause 2.0
    music Groove2_85
    img 15788
    with fadelong
    w
    img 15789
    with fade
    victoria "М-м-м-м..."
    # Моника садится в закрытую позу, стараясь быть подальше от Виктории
    # Моника и Мелани смотрят на страпон, Виктория ухмыляется, видя это
    img 15790
    with diss
    victoria "Ну что, подружки, вам понравился наш девичник?"
    music Master_Disorder
    img 15791
    with fade
    melanie "Да..."
    music Groove2_85
    img 15792
    with diss
    victoria "Что 'да'? Вам понравилось?"
    victoria "Вы хотели бы повторить наш девичник? Подружки."
    music Master_Disorder
    img 15793
    with fade
    m "Нам понравился девичник..."
    music Power_Bots_Loop
    img 15763
    with diss
    mt "!!!"
    mt "Ни за что!!!"
    mt "НЕНАВИЖУ!!!"
    img 15794
    with diss
    melanie "И мы хотели бы повторить..."
    # Виктория самодовольно смеется
    music Groove2_85
    img 15795
    with fade
    sound snd_woman_laugh3
    victoria "Я оставлю мой подарок здесь..."
    victoria "В следующий наш девичник он мне пригодится..."
    victoria "Хотя, возможно, я принесу своим хорошим подружкам еще какой-нибудь подарок."
    # хихикает
    # спустя несколько минут
    # Виктория стоит возле входной двери, смотрит на своих подружек, ухмыляется, подмигивает им и уходит
    # дверь за Викторией закрывается
    # камера на Монику с Мелани. они сидят одетые, держат в руке бокалы, смотрят друг на друга
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 15800
    with fadelong
    w
    img 15796
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Power_Bots_Loop
    img 15797
    with fadelong
    m "Я! НЕНАВИЖУ! ЭТУ СУЧКУ!"
    music Master_Disorder
    img 15798
    with fade
    melanie "Миссис Бакфетт. Думаю, наши интересы относительно Мисс Виктории совпадают."
    melanie "У меня есть идея, как избавиться от нее..."
    melanie "Я могу расчитывать на Вашу помощь?"
    img 15799
    with diss
    m "Да, Мелани... Я готова на все ради этого..."
    # они обе преисполнены мести и готовы "дружить" против Виктории, бокалы сближаются, звук чокающихся бокалов
    # и мокрый страпон на диване
    $ ep29_victoria_melanie_victoria_quest_fully_completed = True
    music stop
    img black_screen
    with diss
    pause 3.0
    $ questHelp("victoria_3", True)
    return
