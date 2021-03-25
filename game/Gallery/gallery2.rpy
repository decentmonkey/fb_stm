
label gallery_15521:
    music stop
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
            return
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
    label gallery_15565:
    music Groove2_85
    img 15560
    with fade
    sound vjuh3
    w
    img 15561
    with diss
    sound vjuh4
    w
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
            return
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
            return
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
    label gallery_15651:
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
    call photoshop_flash() from _rcall_photoshop_flash_153
    w
    img 15652
    with fade
    sound lick10
    victoria "Подружки знают, что мне это нравится..."
    w
    call photoshop_flash() from _rcall_photoshop_flash_154
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
            return

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
    label gallery_15703:
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
    label gallery_15728:
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
            return
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
            return
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
    label gallery_15766:
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
            return
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
    label gallery_15785:
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
    music stop
    img black_screen
    with diss
    pause 3.0
    return


############ Fitness 1############

label gallery_7739:
    # в раздевалки издалека Стефани и Ребекка обнаженные
    # render
    # Повтор, раздевалка. Стефани, Ребекка, Бетти
    music Groove2_85
    img 7727
    with fade
    w
    img 7729
    w
    img 7728
    w
    img 7730
    with fade
    betty "Гуверантка! Где моя сумка с униформой?"
    img 7731
    betty "Быстро неси ее сюда!"

    img 7732
    betty "Что ты там копаешься?!"
    img 7733
    with fade
    m "Вот Ваша сумка, Миссис Робертс."

    # Бетти уходит в спортивном
    img 7734
    with fade
    betty "Можешь посидеть здесь или понаблюдать за мной."
    img 7735
    m "Спасибо, Миссис Робертс... Я посижу здесь..."
    img 7736
    w
    #fade
    # Девочки обнаженные
    music BossaBossa
    img 7737
    with fadelong
    rebecca "Привет, Моника!"
    img 7738
    stephanie "Моника, когда ты закончишь свое приключение?"
    img 7739
    with fade
    "Ты знаешь..."
    img 7740
    with Dissolve(0.5)
    "Это смешно выглядит со стороны..."
    sound snd_fabric1
    img 7742
    with Dissolve(0.5)
    "Хи-хи!"

    img 7741
    with fade
    rebecca "И когда ты будешь снова заниматься с нами?"
    sound snd_fabric1
    img 7744
    with fade
    w
    img 7745
    with Dissolve(0.5)
    w
    img 7746
    with Dissolve(0.5)
    w
    img 7747
    "Почему ты всю тренировку сидишь здесь?"
    img 7748
    with fade
    m "Привет, девочки!"
    "Я уже скоро закончу свое приключение."
    img 7749
    "Осталось совсем немного!"
    img 7750
    "Скоро я снова буду заниматься с Вами!"
    music Groove2_85
    img 7751
    with fade
    stephanie "Ну хорошо... Как-то это все странно..."
    img 7752
    with fade
    rebecca "Хи-хи"
    img 7753
    with fade
    w
    img 7754
    mt "СУЧКИ!!!"
    return


#### исправлено
label gallery_7909:
    $ imagesListIdx = 0
    music Ready_and_Waiting
    #Stephanie - 7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829,
    # 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911
    $ images = [7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829, 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911]
    $ imagesAmount = 25
    $ imagesList = random.sample(set(images), imagesAmount)
    $ imagesList.sort()
    label gallery_7909_1:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            if imagesListIdx == 0:
                with fadelong
            w
            $ imagesListIdx += 1
            jump gallery_7909_1

    $ videoList = [1, 2, 3, 4, 5]
    $ videosAmount = 3
    $ videoList = random.sample(set(videoList), videosAmount)
    if 1 in videoList:
        scene black
        image videov_Fitness_Stephanie_1_1 = Movie(play="video/v_Fitness_Stephanie_1_1.mkv", fps=30)
        show videov_Fitness_Stephanie_1_1
        wclean
    if 2 in videoList:
        scene black
        image videov_Fitness_Stephanie_1_2 = Movie(play="video/v_Fitness_Stephanie_1_2.mkv", fps=30)
        show videov_Fitness_Stephanie_1_2
        wclean
    if 3 in videoList:
        scene black
        image videov_Fitness_Stephanie_1_3 = Movie(play="video/v_Fitness_Stephanie_1_3.mkv", fps=30)
        show videov_Fitness_Stephanie_1_3
        wclean
    if 4 in videoList:
        scene black
        image videov_Fitness_Stephanie_1_4 = Movie(play="video/v_Fitness_Stephanie_1_4.mkv", fps=30)
        show videov_Fitness_Stephanie_1_4
        wclean
    if 5 in videoList:
        scene black
        image videov_Fitness_Stephanie_1_5 = Movie(play="video/v_Fitness_Stephanie_1_5.mkv", fps=30)
        show videov_Fitness_Stephanie_1_5
        wclean

    music Loved_Up
    #Инструктор подходит к Стефани
    img 7933
    with fadelong
    fitness_instructor "Стефани, давай я помогу тебе..."
    #Если был секс
    if stephanieFitnessJustSex == True:
        img 7934
        with fade
        stephanie "Муррр..."
        stephanie "Мой тигр хочет помочь мне?..."
        img 7935
        fitness_instructor "Стефани, твой тигр всегда готов придти на помощь!"
        img 7936
        with fade
        stephanie "Муррр..."
        img 7937
        with fade
        w
        img 7938
        with fade
        w

    else:
        #Если секса не было
        music Groove2_85
        img 7933
        with fadelong
        stephanie "Я предпочитаю помощь от кого-то более сообразительного чем ты..."
        fitness_instructor "Стефани, что я могу сделать?"
        img 7939
        with fade
        stephanie "Продолжай быть настойчивым..."
        "Хи-хи..."
    return


label gallery_7793:
    $ imagesListIdx = 0
    music Ready_and_Waiting
    #Rebecca - 7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832,
    # 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916
    $ images = [7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832, 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916]
    $ imagesAmount = 27
    $ imagesList = random.sample(set(images), imagesAmount)
    $ imagesList.sort()
    $ videoFlag = False
    label gallery_7909_2:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            if imagesList[imagesListIdx] >= 7832 and videoFlag == False:
                $ videoFlag = True
                $ videoList = [1, 3, 4]
                $ videosAmount = 2
                $ videoList = random.sample(set(videoList), videosAmount)
                if 1 in videoList:
                    scene black
                    image videov_Fitness_Rebecca_1_1 = Movie(play="video/v_Fitness_Rebecca_1_1.mkv", fps=30)
                    show videov_Fitness_Rebecca_1_1
                    wclean
                if 3 in videoList:
                    scene black
                    image videov_Fitness_Rebecca_1_3 = Movie(play="video/v_Fitness_Rebecca_1_3.mkv", fps=30)
                    show videov_Fitness_Rebecca_1_3
                    wclean
                if 4 in videoList:
                    scene black
                    image videov_Fitness_Rebecca_1_4 = Movie(play="video/v_Fitness_Rebecca_1_4.mkv", fps=30)
                    show videov_Fitness_Rebecca_1_4
                    wclean

            img imageName
            if imagesListIdx == 0:
                with fadelong
            w
            $ imagesListIdx += 1
            jump gallery_7909_2

    #Инструктор подходит к Ребекке
    music Loved_Up
    img 7931
    with fadelong
    fitness_instructor "Ребекка, давай я помогу тебе..."
    img 7932
    rebecca "Спасибо, не надо..."
    return

label gallery_7926:
    $ imagesListIdx = 0
    music Ready_and_Waiting
    #Betty - 7758, 7759, 7769, 7770, 7771, 7772, 7773, 7774, 7775, 7776, 7777, 7778, 7779, 7804, 7805, 7806, 7807, 7808, 7809, 7810, 7811, 7812, 7813, 7814, 7815,
    # 7835, 7836, 7837, 7838, 7839, 7840, 7841, 7853, 7854, 7855, 7856, 7857, 7865, 7866, 7867, 7868, 7869, 7870, 7871, 7872, 7873, 7874, 7886, 7887, 7888, 7889, 7890, 7891,
    # 7905, 7906, 7907, 7917, 7918, 7919, 7920, 7921, 7922, 7923, 7924, 7925, 7926, 7927, 7928, 7929, 7930
    $ images = [7758, 7759, 7769, 7770, 7771, 7772, 7773, 7774, 7775, 7776, 7777, 7778, 7779, 7804, 7805, 7806, 7807, 7808, 7809, 7810, 7811, 7812, 7813, 7814, 7815, 7835, 7836, 7837, 7838, 7839, 7840, 7841, 7853, 7854, 7855, 7856, 7857, 7865, 7866, 7867, 7868, 7869, 7870, 7871, 7872, 7873, 7874, 7886, 7887, 7888, 7889, 7890, 7891, 7905, 7906, 7907, 7917, 7918, 7919, 7920, 7921, 7922, 7923, 7924, 7925, 7926, 7927, 7928, 7929, 7930]
    $ imagesAmount = 35
    $ imagesList = random.sample(set(images), imagesAmount)
    $ imagesList.sort()
    $ videoFlag1 = False
    $ videoFlag2 = False
    label gallery_7926_1:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            if imagesList[imagesListIdx] >= 7808 and videoFlag1 == False:
                $ videoList = [1, 2, 3, 4]
                $ videosAmount = 2
                $ videoList = random.sample(set(videoList), videosAmount)
                $ videoFlag1 = True
                if 1 in videoList:
                    scene black
                    image videov_Fitness_Betty_1_1 = Movie(play="video/v_Fitness_Betty_1_1.mkv", fps=30)
                    show videov_Fitness_Betty_1_1
                    wclean
                if 2 in videoList:
                    scene black
                    image videov_Fitness_Betty_1_2 = Movie(play="video/v_Fitness_Betty_1_2.mkv", fps=30)
                    show videov_Fitness_Betty_1_2
                    wclean
                if 3 in videoList:
                    scene black
                    image videov_Fitness_Betty_1_3 = Movie(play="video/v_Fitness_Betty_1_3.mkv", fps=30)
                    show videov_Fitness_Betty_1_3
                    wclean
                if 4 in videoList:
                    scene black
                    image videov_Fitness_Betty_1_4 = Movie(play="video/v_Fitness_Betty_1_4.mkv", fps=30)
                    show videov_Fitness_Betty_1_4
                    wclean



            img imageName
            if imagesListIdx == 0:
                with fadelong
            w
            $ imagesListIdx += 1
            jump gallery_7926_1


    #Инструктор подходит к Бетти
    music Loved_Up
    img 7940
    with fadelong
    fitness_instructor "Бетти, давай я помогу тебе..."
    betty "Конечно!"
    "С удовольствием!"
    img 7941
    with fade
    fitness_instructor "Сосредоточься на себе..."
    img 7942
    betty "Хорошо..."
    img 7943
    fitness_instructor "Давай попробуем еще одно упражнение..."
    betty "Хорошо..."
    #fade
    #если первый раз
    if fitness_gym_betty_first_time_interact_with_trainer == True:
        img 7944
        with fade
        betty "Ой! Мне больно!"
        img 7945
        fitness_instructor "Надо немножечко потерпеть..."
        betty "У меня не получается..."
        img 7946
        fitness_instructor "Бетти, ты прекрасна!"
        "У тебя все получится!"
        img 7947
        betty "Правда?"
        img 7948
        fitness_instructor "Хочешь остаться на частный урок?"
        img 7949
        "У меня есть методики, которые дадут потрясающе быстрый результат..."
        img 7950
        betty "Хочу..."
        music Groove2_85
        img 7951
        with fade
        stephanie "Эй! Прошу прощения!"
        img 7952
        "Мне тут нужна небольшая помощь в упражнениях!"
        img 7953
        with fade
        fitness_instructor "Тогда до встречи после занятий, Бетти..."
        img 7954
        betty "До встречи!"
    else:
        #если последующие разы
        img 7944
        with fade
        fitness_instructor "У тебя уже лучше получается, Бетти!"
        img 7950
        betty "Спасибо!"
        img 7948
        with fade
        fitness_instructor "Останешься сегодня снова на частный урок?"
        img 7949
        fitness_instructor "Тебе надо еще позаниматься..."
        img 7954
        betty "Да, я останусь..."
        img 7953
        with fade
        fitness_instructor "Тогда до встречи после занятий, Бетти..."
        img 7954
        betty "До встречи!"
        #


    if fitness_gym_betty_first_time_interact_with_trainer == False:
        music Ready_and_Waiting
#            if imagesList[imagesListIdx] >= 7808 and videoFlag2 == False:
#                $ videoFlag2 = True
        $ videoList = [5, 6, 7, 8, 9]
        $ videosAmount = 3
        $ videoList = random.sample(set(videoList), videosAmount)
        if 5 in videoList:
            scene black
            image videov_Fitness_Betty_1_5 = Movie(play="video/v_Fitness_Betty_1_5.mkv", fps=30)
            show videov_Fitness_Betty_1_5
            wclean
        if 6 in videoList:
            scene black
            image videov_Fitness_Betty_1_6 = Movie(play="video/v_Fitness_Betty_1_6.mkv", fps=30)
            show videov_Fitness_Betty_1_6
            wclean
        if 7 in videoList:
            scene black
            image videov_Fitness_Betty_1_7 = Movie(play="video/v_Fitness_Betty_1_7.mkv", fps=30)
            show videov_Fitness_Betty_1_7
            wclean
        if 8 in videoList:
            scene black
            image videov_Fitness_Betty_1_8 = Movie(play="video/v_Fitness_Betty_1_8.mkv", fps=30)
            show videov_Fitness_Betty_1_8
            wclean
        if 9 in videoList:
            scene black
            image videov_Fitness_Betty_1_9 = Movie(play="video/v_Fitness_Betty_1_9.mkv", fps=30)
            show videov_Fitness_Betty_1_9
            wclean
        img v_Fitness_Betty_1_5_23
        with fade
        w
        img v_Fitness_Betty_1_6_20
        with fade
        w
    return

label gallery_8649:
    music Groove2_85
    img 8618
    with fade
    w
    img 8619
    with fade
    w
    img 8620
    with fade
    fred "..."
    img 8621
    m "Фред!?"
    "Что ты здесь делаешь?! Нерадивый водитель!"
    "Твое место у машины!"
    img 8622
    fred "О! Миссис Бакфетт!"
    "Все забываю сказать что Вам очень идет эта униформа..."
    img 8623
    m "!!!"
    img 8624
    m "Что тебе здесь надо, Фред?!"
    img 8625
    fred "О! Миссис Бакфетт!"
    "Мне нужен Ваш совет..."
    m "Какой еще совет?!"
    fred "Совет в выборе попы..."
    music Pyro_Flow
    img 8626
    m "Какой еще попы?! Что ты несешь?!"
    "Иди на свое рабочее место, немедленно!"
    music Groove2_85
    img 8627
    with fade
    fred "Одной попы из тех, которые там занимаются сейчас."
    img 8628
    fred "Какую попу Вы бы предпочли, Миссис Бакфетт?"
    music Loved_Up
    img 8629
    with fade
    fred "Бетти..."
    img 8630
    with fade
    fred "Стефани..."
    img 8631
    with fade
    fred "или Ребекку?"
    music Groove2_85
    img 8632
    with fade
    mt "Вот мерзавец!!!"
    "Как он смеет разговаривать со мной о таких вещах!"
    mt "..."
    mt "Хотя..."
    # Моника говорит что бери Бетти, эта дура как раз заслуживает такого болвана как ты.
    # Фред говорит что это будет непрофессионально, т.к. он у нее работает.
    # Моника говорит что добраться до других у него шансов есть.
    # Фред говорит что Моника поможет ему в этом. Моника спрашивает с какой стати.
    # Фред отвечает что Моника что-нибудь придумает, потому что иначе ей придется пожертвовать своей попой.
    # Хватает ее за зад.
    img 8633
    m "Бери Бетти, эта дура как раз заслуживает такого болвана как ты!"
    img 8634
    fred "Миссис Бакфетт, это будет непрофесионально, так как я работаю у нее."
    "А Вы знаете, я профессионал!"
    img 8635
    m "В любом случае, добраться до остальных у тебя шансов нет!"
    img 8636
    fred "У меня есть шансы, Мэм..."
    fred  "Ведь Вы поможете мне в этом..."
    music Pyro_Flow
    img 8637
    with fade
    m "С какой стати я тебе будут помогать в твоих похотливых фантазиях, Фред?!"
    m "Тебе мало что ты уже натворил, подлец?!"
    img 8636
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    img 8638
    with fade
    m "Я не собираюсь разговаривать с тобой об этом!"
    music Groove2_85
    img 8639
    with fade
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    img 8640
    fred "Обязательно..."
    img 8641
    fred "В противном случае, Вам придется пожертвовать своей попой для этого..."
    sound Jump2
    img 8642
    with Dissolve(0.5)
    # Хватает ее за зад.
    w
    img 8643
    w
    if monicaBettyPanties == False:
        img 8668
    else:
        if monicaBettyPantiesId == 1:
            img 8669
        if monicaBettyPantiesId == 2:
            img 8670
        if monicaBettyPantiesId == 3:
            #before subd
            img 8671
        if monicaBettyPantiesId == 4:
            img 8672
        if monicaBettyPantiesId == 5:
            img 8673
    with fade
    w
    img 8644
    with fade
    w
    img 8645
    music Power_Bots_Loop
    # Моника поворачивается и, в зависимости от bitchness дает пощечину, либо дает по яйцам ногой.
    menu:
        "Ударить Фреда между ног!" if monicaBitch == True:
            label gallery_8659:
            img 8654
            with Dissolve(0.5)
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            "НИЧТОЖЕСТВО!!!"
            sound snd_kick_fred1
            img 8655
            with Dissolve(0.5)
            "ПОЛУЧАЙ!!!"
            img 8656
            with Dissolve(0.5)
            "НА!!!"
            #bodyfall
            #fade
            sound snd_bodyfall
            img 8657
            with fade
            fred "АААААххххх!!!"
            fred "Что Вы сделали, Миссис Бакфетт..."
            fred "Вы применили насилие!"
            img 8658
            "Это же..."
            "Это же... Больно..."
            # Фред падает, если ударили.
            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            img 8659
            with fade
            m "Сейчас я воткну каблук в твой рот, мерзавец!"
            img 8660
            with fade
            w
            img 8661
            "Если ты сейчас же не уберешься отсюда!!!"
            if monicaBettyPanties == False:
                img 8662
            else:
                if monicaBettyPantiesId == 1:
                    img 8663
                if monicaBettyPantiesId == 2:
                    img 8664
                if monicaBettyPantiesId == 3:
                    #before subd
                    img 8665
                if monicaBettyPantiesId == 4:
                    img 8666
                if monicaBettyPantiesId == 5:
                    img 8667
            with fade
            "Ты забыл с кем связался! Ничтожество!"
            return

        "Ударить Фреда между ног! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass

        "Дать пощечину Фреду." if monicaBitch == False:
            img 8646
            with Dissolve(0.5)
            sound snd_punch_face1
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            img 8647
            with Dissolve(0.5)
            sound snd_punch_face2
            #звук пощечины
            "НИЧТОЖЕСТВО!!!"
            #fade
            sound snd_bodyfall
            img 8648
            with fade
            fred "Айй!!"
            fred "Мои очки!"
            fred "Вы применили насилие!"

            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            img 8650
            with fade
            w
            img 8649
            m "Следующий удар будет гораздо больнее, мерзавец!"
            img 8651
            "Если ты сейчас же не уберешься отсюда!!!"
            img 8652
            with fade
            "Ты забыл с кем связался! Ничтожество!"

        "Дать пощечину Фреду. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
            pass
    # Стефани и Ребекки нравятся слова Моники и они разговаривают с ней о том наконец-то увидели прежнюю Монику.
    # А то они уже стали сомневаться по поводу ее слов.
    # Моника говорит чтобы не сомневались.
    # После этого несколько меняется диалог при встрече подруг на фитнесе.

    #Фред убегает
    music stop
    img 8653
    with fade
    sound man_steps
    w
    #fade
    music BossaBossa
    img 8674
    with fade
    stephanie "Вау! Моника!"
    rebecca "Моника! Вот это да!"
    stephanie "Наконец-то мы узнаем нашу Монику!"
    rebecca "Да, Моника, а то мы уже начали сомневаться в тебе!"
    img 8675
    m "Я хочу предупредить Вас, девочки!"
    "Если кто-то будет сомневаться во мне, то последует за тем болваном!"
    img 8676
    stephanie "Нет, Моника! Пожалуйста не надо!"
    rebecca "Мы твои верные подруги, Хи-хи!"
    stephanie "Скорее завершай свое приключение."
    "Нам не терпится все узнать!"
    rebecca "Да, Моника!"
    "Про тебя можно снимать кино!"
    img 8677
    with fade
    mt "Да уж, про меня уже можно снимать кино, это точно..."
    img 8678
    with fade
    stephanie "Пока, Моника!"
    "Чмок!"
    rebecca "Пока, Моника!"
    "Чмок!"
    m "Пока, девочки!"
    return

############ GasStation 1############

label gallery_7074:


    #Моника ворует еду

    $ store_music()
    music Hidden_Agenda
    #render
    img 7072
    with fade
    w
    img 7073
    w
    img 7074
    mt "Думаю не будет ничего страшного если я украду одно пирожное..."
    img 7075
    w

    #вариации (случайно)
    $ gasStationThiefImages = ["7076", "7077", "7078"]
    $ images = random.sample(set(gasStationThiefImages), 1)
    img images[0]
    "Я заслужила его за все то что пережила..."

    $ restore_music()
    return


############ HotelLeGrand 1############

label gallery_20424:
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
            label gallery_20434:
            $ choose_var = 1
            img 20425
            with fade
            m "Стейк из форели, греческий салат и шампанское."
            $ images_list = [20432, 20433, 20434, 20435]
        "Морепродукты и коктейль.":
            label gallery_20438:
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
            label gallery_20444:
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
            return
# Моника говорит какие блюда выбрала
# Если есть тикет, то она добавляет что оплатит тикетом.
    if check_inventory("legrand_certificate",1) == True:
        sound snd_folder_drop
        img 20428
        with diss
        m "Я оплачу этим сертификатом"
        sound snd_take_paper

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

#    $ restaurantFoodHistory.append(choose_var)
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
    return

############ House 1############

label gallery_5999:
    #Дик, Моника и водитель в машине. День. Моника в платье AfterJail
    #белый экран
    music dream
    img white_screen
    with fade
    dick "Моника..."
    dick "Моника?"
    dick "Моника!"

    #Моника просыпается в машине
    music Power_Bots_Loop
    img 5905
    with Dissolve(1.0)
    m "А? ЧТО?"
    "ГДЕ Я???"

    img 5906
    m "ДИК???"
    "Что ты здесь делаешь?"

    img 5907
    dick "Моника, что значит что я здесь делаю?"
    "Я еду с тобой в ресторан."
    img 5908
    m "В какой ресторан?"

    img 5909
    dick "В самый лучший! В отеле Le Grand!"
    img 5910
    dick "Моника, ты себя хорошо чувствуешь?"
    img 5911
    m "Я... Я не знаю..."

    img 5912
    dick "Моника, мне показалось что ты заснула."
    "Ты не выспалась сегодня?"

    img 5913
    m "Я... Заснула?..."
    "Это был сон???"

    img 5914
    dick "Сон? Дорогая, тебе что-то приснилось?"

    music RnB4_100
    img 5915
    with fade
    m "Мне... Да...."
    img 5916
    with Dissolve(0.5)
    "ЭТО БЫЛ СОН!!!"

    img 5917
    with fade
    fred "Мэм. С вами все в порядке?"

    music Stealth_Groover
    img 5918
    m "Фрэд?!?!"
    "ТЫ?!?!"

    img 5919
    fred "Да, мэм?"

    img 5920
    m "Ты уволен, Фред!!!"
    "Едь скорее на место и вон из машины!"

    img 5921
    dick "Дорогая???"
    img 5922
    fred "Миссис Бакфетт, но за что вы хотите уволить меня?"
    "В чем причина? Что за проступок я совершил?"

    img 5923
    m "Что за проступок, ты спрашиваешь?!?!"
    img 5924
    "Ты..."
    "Ты... Я не скажу что ты сделал..."
    img 5923
    "Но этого более чем достаточно для увольнения!"

    img 5925
    fred "Мэм, но я не понимаю..."

    music Hidden_Agenda
    img 5926
    with fade
    m "Значит это все-таки был сон!"
    "Получается Фред этого не делал?"
    img 5927
    "Но нет! Я не смогу находиться рядом с ним после того что я пережила, даже во сне!"

    music RnB4_100
    img 5928
    with fade
    "Сон!"
    "Ура! Сон!"

    music Stealth_Groover
    img 5929
    with fadelong
    m "Ты уволен, Фред!"

    dick "Дорогая???"

    img 5930
    m "Дик, не надоедай мне!"
    "Ты тоже хорош!"
    "Что ты здесь делаешь? Иди к своей секретарше!"

    img 5931
    "Ходи с ней по ресторанам! Ты не достоин меня!"

    img 5932
    dick "С какой секретаршей, Моника?!"
    "Мне нравишься ТЫ!"

    img 5933
    m "Так, Фред! Быстро останови машину!"
    img 5934
    with fade
    "Мистеру Дику надо выйти!"

    img 5935
    with Dissolve(0.5)
    "А мне надо позвонить!"

    img 5936
    dick "..."

    img 5937
    with fade
    m "Так, черт, где мой телефон?!"
    img 5938
    with Dissolve(0.5)
    "Дик, ты не видел его?"

    img 5939
    music Master_Disorder
    with fadelong
    dick "У тебя его не было, Моника."
    "Я не знаю почему, но ты не взяла его..."

    img 5940
    m "???"

    img 5941
    dick "Более того, ты почему-то не носишь свои украшения."
    img 5942
    music Villainous_Treachery
    with Dissolve(0.5)
    "А где твой браслет? Ты всегда одевала его..."
    img 5942
    show screen vignette_screen
    with Dissolve(1.5)
    w
    img 5943
    with Dissolve(0.5)
    m "..."

    img 5944
    with fade
    dick "И трусики, зачем-то ты их тоже не носишь."
    "Почему, Моника?"

    img 5945
    with fade
    m "..."
    img 5946
    with Dissolve(0.5)
    w
    img 5947
    with Dissolve(0.5)
    w
    img 5948
    with Dissolve(0.5)
    m "!!!"

    img 5949
    with fade
    m "Дик... Я..."
    img 5950
    with Dissolve(0.5)
    "Погоди, я не понимаю..."

    img 5951
    dick "Моника, дорогая!"
    "Не переживай!"
    "Все будет хорошо!"
    img 5952
    "Главное не забудь!"

    img 5953
    with fade
    m "Про что я не должна забыть, Дик?"

    img 5954
    with fadelong
    dick "Про галстук..."

    img 5955
    with Dissolve(0.5)
    m "!!!"

    img 5956
    with fade
    dick "У тебя все будет хорошо, Моника!"
    img 5957
    with Dissolve(0.5)
    "Главное помни про галстук и не разбей мое сердце..."

    img 5958
    with Dissolve(0.5)
    m "!!!"
    hide screen vignette_screen

    #Моника просыпается
    music Power_Bots_Loop
    sound snd_woman_scream1a
    if cloth != "Nude":
        img 5959
    else:
        img 7109
    with fade
    mt "АААААХХХ!!!!"

    mt "ГДЕ Я???"

    img 5960
    mt "Что это... что это за дыра?!?!"
    img 5961
    with fade
    mt "Где Юлия?!"

    mt "..."

    img 5962
    with fade
    mt "Черт! Я все вспомнила!"

    mt "Этого не может быть!!!"

    if cloth != "Nude":
        img 5963
    else:
        img 5964
    "НЕТ!!!"
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    #пауза
    #моника сидит думает на кровати, встает
    music Stealth_Groover
    if cloth != "Nude":
        img 5965
        with fade
    else:
        img 5966
        with fade
    mt "Стоп. Моника, не унывай!"

    "Давай подумаем что у нас есть на данный момент."

    if cloth != "Nude":
        img 5967
    else:
        img 5968
    with fade
    "У меня нет денег, нет документов."
    "Любой полицейский, который меня остановит, {c}может забрать меня к Маркусу{/c} и..."
    img 5969
    "Никаких И! Я не попаду к нему!"

    img 5970
    with fade
    "На самом деле, не все так плохо."
    "У меня есть крыша над головой, правда я не могу забыть какой ценой она досталась мне..."
    img 5971
    with Dissolve(0.5)
    "Этот Фред... Я убью его!"
    "Но это потом... Моника, давай подумаем про то что делать сейчас..."

    if cloth != "Nude":
        img 5972
    else:
        img 5973
    with fade
    "Итак... Меня пустили в свой же дом при условии что {c}я буду убираться в нем{/c}..."

    if cloth != "Nude":
        img 5974
    else:
        img 5975
    "ЗА БЕСПЛАТНО!!!"
    img 5976
    "..." #злой взгляд

    if cloth != "Nude":
        img 5977
    else:
        img 5978
    with fade
    "Но хорошо... Если мне надо пройти через это, то я пройду..."
    "Они не знают кто я такая, поэтому моя гордость не сильно пострадает..."
    "Мне надо всего-лишь притвориться... Ненадолго..."
    "Сделать вид что я убираюсь."
    "В конце концов, эта семейка идиотов что здесь живет - она недалекого ума."
    "Притвориться перед ними и обхитрить их будет пустяковой задачей..."

    img 5979
    "Они глазом не успеют моргнуть, как вылетят отсюда, из этого дома."
    "А я займу свое достойное место здесь..."
    img 5980
    with Dissolve(0.5)
    "Потому что Я - Моника Бакфетт!"
    "А они - никто!"

    img 5981
    with fade
    "Эта Бетти..."
    "Черт... Хоть она и дура, но она следит за мной."
    "Куда бы я здесь ни пошла, она следует за мной по пятам..."
    "Так что крыша у меня над головой есть, но {c}еду мне придется доставать где-то еще...{/c}"

    if cloth != "Nude":
        img 5982
    else:
        img 5983
    with fade
    "Интересно где?..."

    "Может украсть еду у той {c}дуры на заправке{/c}?"
    "Но хочу-ли я воровать?..."

    if cloth != "Nude":
        img 5984
    else:
        img 5985
    with fade
    "Или может спросить еду у того {c}продавца кебабов{/c}?"
    "Я видела как он смотрит на меня..."

    img 5986
    if shawarmaTraderOffended1 == True:
        #
        "Животное, фу!"
    else:
        #
        "Маленькое ничтожество..."

    "Конечно, ему никогда не светит прикоснуться к такой красоте как Я..."

    img 5987
    "Но... это можно использовать, чтобы достать хоть какую-то пищу..."
    "Я никогда в жизни не пробовала такой еды, но сейчас выбирать не приходится."

    if cloth != "Nude":
        img 5988
    else:
        img 5989
    with fade
    "Даже она мне кажется вкусной сейчас, учитывая что я толком ничего не ела уже давно..."
    "И уж тем более не сравнится с теми помоями, что мне пришлось выпрашивать, когда я была в подвале у Маркуса..."

    if cloth != "Nude":
        img 5990
    else:
        img 5991
    with fade
    "И мне надо как-то придумать как вернуть назад свое положение..."

    img 5992
    with Dissolve(0.5)
    "Дик... Да уж, помощник!"
    "Этот подкаблучник теперь влюблен в свою новую секретаршу."

    if cloth != "Nude":
        img 5993
    else:
        img 5994
    "Эту сучку!"
    "Это ее происки по поводу галстука!"
    "Мне надо сходить к нему еще раз, может получится {c}отбить Дика у нее{/c}?"

    if cloth != "Nude":
        img 5996
    else:
        img 5997
    with fade
    "В конце концов, чтобы вернуть назад свои деньги, мне надо сначала отделаться от Маркуса!"
    "А в этом мне может помочь только Дик!"
    "Еще эти его дурацкие слова про галстук!"
    img 5995
    with Dissolve(0.5)
    "Уверена что Дик просто шутил!"
    "Не думаю что мне стоит всерьез воспринимать его слова об этом!"

    if cloth != "Nude":
        img 5998
    else:
        img 5999
    "..."
    "Мне интересно что там происходит в {c}моем офисе{/c}?"
    "Кто-то сменил код на лифте, но может я найду способ попасть туда?"

    if cloth != "Nude":
        img 6000
    else:
        img 6001
    with fade
    "Я хочу посмотреть на того смельчака, который посмел занять мое место!"
    "Да и как это вообще возможно?!"

    img 6002
    with Dissolve(0.5)
    "Я - Моника Бакфетт!"
    "Я - лицо модного журнала!"
    "Невозможно представить журнал без меня!"
    img 6003
    "Это невозможно! И, думаю, они это прекрасно понимают!"
    "Поэтому им не обойтись без меня!"
    "Это шанс для меня вернуть все назад..."

    img 6004
    with fade
    "Стив?..."
    "Нет, к этому слизняку в таком виде идти точно не стоит."
    "Этот мешок с дерьмом сделает все чтобы использовать это небольшое недоразумение в своих целях..."
    "Я его слишком хорошо знаю..."
    if janeTiffanyFirePlanned == True:
        #если была угроза увольнения Джейн и Тиффани
        "Плюс вокруг него вьются эти две проститутки..."
        "Тиффани и Джейн..."
        "После того как я угрожала уволить их, они могут быть пострашнее той секретарши у Дика..."
        "Жалкие ничтожества..."

    img 6005
    with fade
    "И мне вообще стоит поменьше показываться в таком виде перед людьми, которые мне знакомы."
    "Это касается и моих подружек Стефани и Ребекки..."
    "В конце концов, мне придется общаться со всеми ними когда я верну положение в обществе."
    "И вообще, надо бы найти одежду получше чем те тряпки, которые я схватила у той шлюхи..."

    if cloth != "Nude":
        img 6006
    else:
        img 6007
    "Не могу поверить что мне приходится ходить в этом по городу..."
    "Может лучше ходить в униформе Юлии?"
    "Как хорошо что меня никто не узнает в этом!"
    if cloth != "Nude":
        img 6008
    else:
        img 6009
    "Никто даже подумать не может что Моника Бакфетт может ходить по улице в униформе горничной..."
    "Или в одежде проститутки..."
    "Это мне на руку!"

    img 6010
    with Dissolve(0.5)
    "..."
    "Ральф..."
    "Его было бы очень просто отбить у этой провинциальной дуры."
    "После этого выкинуть эту Бетти из дома."
    "А потом выкинуть и Ральфа..."

    img 6011
    "Но Бетти не дает возможности даже взять бутерброд на кухне, что уж говорить о том что она не даст даже близко приблизиться к Ральфу..."

    "..."

#    img 6012
#    "Барди..."
#    "Этот мелкий неудачник даже не заслуживает внимания."
#    "Он вертится вокруг как назойливая муха!"
#    "Считает что я ему обязана тем что нахожусь здесь!"
#    "Наивный дурачок!"
#    "Надо как-то избавиться от него..."

    #играет музыка kill bill
    img 6013
    with fadelong
    m "Да, это все небольшое недоразумение..."
    "И, когда я решу его, я поквитаюсь со всеми вами!"
    "Клянусь!"

    #музка гаснет
    music stop
    img 6014
    with fade
    mt "..."
    music Stealth_Groover
    "Итак..."
    "Сейчас, думаю, надо {c}притвориться горничной{/c}."
    "Затем {c}пойти поискать еду{/c}..."
    img 6015
    with fade
    "Думаю мне необязательно все время убираться здесь..."
    "Эта семейка не привыкла к тем стандартам чистоты, которые требовала я от гувернанток."
    img 6016
    with Dissolve(0.5)
    "Но иногда убираться все-же стоит. Это может вызвать доверие у Бетти."
    "Хотя зачем мне ее доверие?"
    "Мне, почему-то, кажется что еду брать она все-равно не разрешит."
    return

### исправлено
label gallery_7079:
    if monicaLastPissedDay == day and monicaLastPissedDayTime == day_time:
        mt "Я уже писала недавно. Я пока не хочу."
        return
    $ store_music()
    music stop
    #Моника писает
    #звук
    #whore
    #вариации (случайно)

    $ toilet_images = ["7079", "7080", "7081", "7082", "7083", "7084", "7085", "7086", "7087"]
    $ images = random.sample(set(toilet_images), 4)


    if monicaBettyPanties == True:
        if monicaBettyPantiesId == 1:
            $ images = [7163, 7164, 7165]
        if monicaBettyPantiesId == 2:
            $ images = [7166, 7167, 7168]
        if monicaBettyPantiesId == 3:
            $ images = [7169, 7170, 7171]
        if monicaBettyPantiesId == 4:
            $ images = [7172, 7173, 7174]
        if monicaBettyPantiesId == 5:
            $ images = [7175, 7176, 7177]


    img images[0]
    with fade
    w
    sound snd_piss
    $ rnd = rand(1,4)
    if rnd == 1:
        img images[1]
        mt "Эх... мне надо придумать как вернуть все назад..."
        img images[2]
        mt "Я такая красивая... Как со мной могло случиться такое?"
    if rnd == 2:
    #
        img images[1]
        mt "Этот дом такой большой, а мне приходится прятаться чтобы пописать..."
        img images[2]
        "Но, по крайней мере я здесь, а не на улице..."
    #
    if rnd == 3:
        img images[1]
        w
        img images[2]
        mt "Надеюсь Бетти не заметит как я делаю это..."

    #
    if rnd == 4:
        img images[1]
        w
        img images[2]
        mt "Девушка с такой красотой как у меня не заслуживает того что со мной случилось..."
    $ restore_music()
    return

label gallery_7102:
    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return

    $ store_music()
    music stop
    #Моника принимает душ
    #вариации (случайно)
    #звук душа
    music snd_shower2
    img 7095
    with fade
    w
    if monicaPussyShaved == False:
        $ shower_images = ["7096", "7097", "7098", "7099", "7100", "7101", "7102", "7103", "7104", "7105", "7106", "7107"]
    else:
        $ shower_images = ["7096", "7097", "7098", "10564", "10565", "10566", "7102", "7103", "10567", "7105", "7106", "7107"]

    $ images = random.sample(set(shower_images), 3)

    img images[0]
    w
    img images[1]
    w
    img images[2]
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Как же хорошо принять душ!"
    if rnd == 2:
        mt "Мне приятно ощущать капельки воды, стекающей по моему телу..."
    if rnd == 3:
        mt "Мое тело божественно!"

    $ restore_music()
    return
 ### исправлено
label gallery_7159:

    return

#### исправлено
label gallery_7433:
    $ images = [7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431]
    $ imagesList = random.sample(set(images), 4)
    $ amount = 4
    $ bettyHere = False
    if get_active_objects("Betty", scene="floor2") != False:
        $ bettyHere = True


    if bettyHere == True:
        img 7419
        w
    img 7421
    call showRandomImages(images, 4, True) from _rcall_showRandomImages_1
    img 7432
    w

    call gallery_7433_1() from _rcall_gallery_7433_1
    return

label gallery_7433_1:
    # Моника закончила тереть пятно
    # Пикчи того как Моника трет пятно
    # Общие 7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431

    # Если Governess Pants (Betty 7419), 7421, 7432, 7433, 7434, 7435
    # Если Governess Pants Betty_1 (Betty 7436) 7437, 7438, 7439
    # Если Governess Pants Betty_2 (Betty 7440) 7441, 7442, 7443
    # Если Governess Pants Betty_3 (Betty 7444) 7445, 7446, 7447
    # Если Governess Pants Betty_4 (Betty 7448) 7449, 7450, 7451
    # Если Governess Pants Betty_5 (Betty 7452) 7453, 7454, 7455


    mt "Все! Я устала тереть это пятно!"
    return

label gallery_7578:

    return

### исправлено
label gallery_7635:

    return

label gallery_7635_1:

    return

## исправлено
label gallery_7655:

    return

### исправлено
label gallery_7675:

    return

### исправлено
label gallery_8683:
    $ store_music()
    music Groove2_85 high

    img 8683

    with fade
    w


    img 8689
    m "Фред! Что ты шляешься здесь?!"
    "Проваливай отсюда, пока не получил по зубам!"
    fred "Мэм! Я просто прогуливаюсь!"
    "Вы знаете, Я профессионал."
    img 8690
    with fade
    "И ищу вдруг где-то надо применить мой профессионализм!"
    img 8691
    m "Это точно не здесь, Фред!"

    $ restore_music()
    return

label gallery_10322:

    return

label gallery_10615:


    return

label gallery_10555:

    return

label gallery_10559:

    return

label gallery_10563:

    return

### исправлено
label gallery_10414:

    return
