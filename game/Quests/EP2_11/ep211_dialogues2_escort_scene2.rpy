default monicaEscortNed1 = False  # Моника сразу призналась друзьям клиента Нэда, что работает в эскорте
default monicaEscortNed2 = False  # Моника согласилась пойти с Дэниелем и заняться с ним сексом
default monicaEscortNed3 = False  # Моника смирилась с прейскурантом и занялась сексом с Марти
default monicaEscortNed4 = False  # Моника после секса с Дэниелем и Марти занялась сексом с Нэдом

#call ep211_escort_scene2_1() # диалог с официанткой в ресторане - Монику вызывает администраторша
#call ep211_escort_scene2_2() # Моника подходит к ресепшену, адинистраторши там нет
#call ep211_escort_scene2_3() # служебный коридор, разговор с администратором и клиентом
#call ep211_escort_scene2_3a() # Дэниел встречает Монику и Нэда возле дома
#call ep211_escort_scene2_4() # знакомство Моники с гостями в гостиной дома
#call ep211_escort_scene2_5() # гостиная, Нэд говорит парням, что Моника с эскорта и он выиграл пари
#call ep211_escort_scene2_6() # соседняя комната, секс с Дэниелем
#call ep211_escort_scene2_7() # гостиная, сидят жены и Нэд с Марти, пока Моника с Дэниелем в соседней комнате
#call ep211_escort_scene2_8() # соседняя комната, секс с Дэниелем, приходит Марти
#call ep211_escort_scene2_9() # гостиная, сидят жены и Нэд с Дэниелем, пока Моника с Марти в соседней комнате
#call ep211_escort_scene2_10() # соседняя комната, секс с Марти
#call ep211_escort_scene2_11() # гостиная, жены, Дэниел и Нэд; Нэд собирается проведать Монику
#call ep211_escort_scene2_12() # соседняя комната, секс Нэда с Моникой
#call ep211_escort_scene2_13() # гостиная, вся компания в полном составе, в том числе и Моника
#call ep211_escort_scene2_14() # служебный коридор, разговор с администратором после возвращения



# Моника сидит за столиком в ожидании клиента
label ep211_escort_scene2_1:
    # подходит официантка
    music Poppers_and_Prosecco
    img 30061
    with fadelong
    w
    sound highheels_short_walk
    img 30062
    with fade
    waitress "Здравствуйте, Мэм! Администратор Вас ждет на ресепшене."
    if waitressMonicaOffended1 == False and waitressMonicaFired == False:
        #
        $ notif(t_("У Моники хорошие отношения с официанткой."))
        #
        img 30063
        with diss
        waitress "Вы? Вы здесь работаете?!" # удивленно
        waitress "Я, даже не думала, что..."
        # Моника немного растеряна
        music Hidden_Agenda
        img 30064
        with fade
        m "Я..."
        m "Я здесь не работаю... Я жду, когда мне принесут еду."
        music Poppers_and_Prosecco
        img 30065
        with diss
        waitress "Мэм, но Вы же ничего не заказывали..."
        img 30066
        with diss
        mt "Вот черт!"
        music Hidden_Agenda
        img 30067
        with fade
        m "Да?"
        m "..."
        m "А, ну конечно. Не заказывала..." # выдавливает улыбку
        img 30068
        with diss
        m "Я... Жду здесь человека."
        m "..."
        m "Кто там меня звал? Администратор?"
        img 30069
        with fade
        waitress "Да, Мэм."
        img 30070
        with diss
        m "Я сейчас подойду к ней."
        # официантка уходит
    else:
        #
        $ notif(t_("У Моники плохие отношения с официанткой."))
        #
        img 30063
        with diss
        waitress "Вы?!" # удивленно
        img 30070
        with fade
        m "Да, это Я!"
        m "Удивительно, что ты все еще работаешь здесь!"
        img 30065
        with diss
        waitress "Мэм..."
        waitress "А для меня удивительно, что Вы работаете здесь..."
        img 30071
        with fade
        m "!!!"
        m "С чего ты взяла, что я здесь работаю?!" # высокомерно
        m "По-твоему, я похожа на работника ресторана?!"
        img 30069
        with diss
        waitress "Мэм... Вас администратор попросила позвать к себе..." # подозрительно
        waitress "Она сказала, что Вы одна из..."
        # Моника перебивает ее
        music Power_Bots_Loop
        img 30072
        with hpunch
        m "Это неважно, что она сказала!"
        m "Я не собираюсь выслушивать от тебя всякие глупости!"
        img 30073
        with diss
        m "Никчемная официантка!"
        # официантка уходит

#    $ log1 = t_("Пойти на ресепшн к администратору.")
    return

# Моника подходит к ресепшену, администратора там нет
label ep211_escort_scene2_2:
    music Groove2_85
    img 30074
    with fadelong
    sound highheels_short_walk
    w
    img 30075
    with fade
    mt "Странно, что ее здесь нет."
    mt "Возможно, она в служебном коридоре?"
    return

# служебный коридор
label ep211_escort_scene2_3:
    # Там стоит заказчик (Ned) и администраторша
    # они смотрят на Монику
    music Groove2_85
    img 30039
    with fadelong
    sound highheels_short_walk
    w
    img 30040
    with fade
    client "Да, вот эта девушка. Я хочу ее."
    img 30041
    with diss
    reception "Это [monica_hotel_name]. Вы уверены?"
    reception "У нас есть другие девушки для такого заказа."
    img 30042
    with diss
    client "Меня интересует именно эта."
    client "Она больше подойдет для меня, чем остальные девушки."
    # администраторша поворачивается к Монике
    img 30043
    with fade
    reception "У тебя сегодня выезд к клиенту."
    reception "Ты должна будешь сопровождать этого джентельмена на встрече."
    reception "И вести себя, как его девушка."
    music Hidden_Agenda
    img 30044
    with diss
    reception "..."
    reception "Правда, мне не понятно, почему клиент выбрал именно тебя..."
    # парень в этом время рассматривает Монику, потом поправляет администратора
    music Groove2_85
    img 30045
    with fade
    client "Не просто вести себя как моя девушка!"
    client "Нужно сделать так, чтобы никто не догадался, что я плачу за это."
    client "Это очень важно!"
    img 30046
    with diss
    reception "Будьте спокойны. Наши девушки - профессионалы."
    reception "Если что-то будет не так..."
    reception "То Вам будет компенсирована сумма вдвое больше той..."
    reception "Которую Вы заплатите за заказ."
    img 30047
    with diss
    client "Очень надеюсь на это."
    client "Для меня это принципиально важный момент."
    # Моника
    img 30048
    with fade
    m "Что мне нужно будет делать?"
    img 30049
    with diss
    client "Вам надо будет быть моей девушкой. Луизой."
    # Моника удивленно
    img 30050
    with diss
    m "Почему Луизой?"
    # Администратор цикает на нее
    music Power_Bots_Loop
    img 30051
    with fade
    reception "Помолчи!"
    reception "Это желание клиента и у тебя нет права обсуждать его!"
    # Моника злится
    img 30056
    with diss
    mt "Никчемная администраторша!"
    # Администратор обращается к клиенту
    music Groove2_85
    img 30052
    with fade
    reception "Вы уверены, что Вам нужен только эскорт?"
    reception "Не хотите ли воспользоваться опцией секса с этой девушкой?"
    reception "Согласно нашего прейскуранта?"
    img 30053
    with diss
    client "Нет. Для меня важно, чтобы она вела себя как моя девушка."
    client "Больше меня никакие услуги не интересуют."
    client "Очень важно, чтобы она была похожа на мою девушку!"
    img 30054
    with fade
    reception "Вы можете воспользоваться любой услугой из прейскуранта..."
    reception "Если передумаете."
    img 30055
    with diss
    reception "В наших интересах оказать как можно больше услуг для того..."
    reception "Чтобы наш клиент остался максимально доволен."
    # Моника кривится
    img 30056
    with diss
    mt "Она прямо навязывает ему услуги из прейскуранта."
    mt "Ее, видимо, не устраивает, что мне попался нормальный клиент."
    mt "А не какой-нибудь извращенец."
    mt "Эти сучки теперь будут мне завидывать."
    # Администраторша смотрит на Монику
    img 30057
    with fade
    reception "Ну что, ты все поняла?"
    reception "Будешь осуществлять эскорт, играя роль его девушки."
    music Power_Bots_Loop
    reception "Если будешь делать это плохо, то будешь оштрафована!"
    img 30058
    with diss
    reception "Тебе понятно, [monica_hotel_name]?!"
    # Моника сквозь зубы
    music Groove2_85
    img 30059
    with fade
    m "Да, мне все понятно."
    img 30060
    with diss
    sound highheels_short_walk
    reception "Иди переодевайся."
    reception "Для этого заказа тебе надо кое-что поприличнее."
    return

# перед домом, Моника с клиентом. их встречает хозяин дома - Дэниел
label ep211_escort_scene2_3a:
    music stop
    img black_screen
    with diss
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)

#    music stop
#    call textonblack(t_("Спустя некоторое время..."))
#    img black_screen
#    with Dissolve(1)
    music Groove2_85
    img 16514
    with fadelong
    w
    img 16515
    with fade
    mt "Это его друг? Больше похож на его босса..."
    client "Эй, Дэниел! Привет!"
    daniel "Привет, Нэд! Как всегда, опаздываешь!"
    img 16516
    with diss
    ned "Да, мы с моей девушкой немного задержались..."
    ned "Кстати, познакомься. Это Луиза."
    img 16517
    with fade
    ned "Луиза, это мой друг и коллега Дэниел."
    ned "Сегодня он устраивает небольшую вечеринку для друзей."
    img 16518
    with diss
    daniel "Ну, наконец-то, Нэд познакомил меня со своей девушкой!"
    daniel "Луиза, вы очаровательны!"
    img 16519
    with fade
    m "Приятно познакомиться, Дэниел."
    img 16520
    with diss
    daniel "Проходите в дом. Там вас давно уже все ждут."
    return

# Смена кадра. Моника с заказчиком подходит к столику, где сидят две пары:
# Daniel, Emma и Marty, ​​Natalie.
# Daniel богаче заказчика (возможно его босс)
label ep211_escort_scene2_4:
    # Заказчик знакомит Монику, представляет ее как свою девушку Луизу.
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 16521
    with fadelong
    sound highheels_short_walk
    w
    img 16522
    with fade
    w
    img 16523
    with diss
    ned "Эй, ребята, привет!"
    ned "Хочу представить вам мою девушку. Ее зовут Луиза."
    ned "Луиза, это мои коллеги и друзья."
    # показывает на первую пару, потом на вторую
    img 16524
    with fade
    ned "Дэниел и его жена Эмма."
    emma "Приятно познакомиться!"
    img 16525
    with diss
    ned "Марти и его жена Натали."
    marty "Привет!"
    natalie "Присаживайтесь к нам."
    natalie "Наконец-то, Нэд познакомил нас со своей девушкой."
    natalie "Я очень рада познакомиться, Луиза."
    # они садятся за столик
    img 16526
    with fade
    m "Мне тоже приятно познакомиться."
    music RnB3_65
    img 16527
    with diss
    mt "Моника, тебе сегодня повезло с клиентом..."
    mt "Вкусный ужин, светские разговоры в компании приличных людей..."
    mt "И никаких извращенцев."
    mt "Все, к чему ты так привыкла... И чего так не хватает теперь."
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 16528
    with fadelong
    ned "Луиза, дорогая, хочешь вина?"
    m "Пожалуй, я не откажусь."
    music stop
    img black_screen
    with diss
    sound pour_wine
    pause 2.0
    music Groove2_85
    # Между всеми происходят какие-то диалоги
    img 16529
    with fade
    daniel "Нэд, так вот почему ты стал опаздывать на работу!" # подмигивает
    daniel "Очевидно, что с такой прекрасной девушкой ты не спишь целыми ночами!"
    daniel "Аха-ха!"
    # Эмма его одергивает
    img 16530
    with diss
    emma "Дэниел, оставь свои пошлые шуточки."
    emma "Ты смущаешь ими Луизу!"
    daniel "Да ладно тебе, детка."
    img 16531
    with fade
    emma "И перестань называть меня деткой. Ты же знаешь, мне это не нравится!"
    img 16532
    with diss
    daniel "Хорошо, любимая, как скажешь."
    # в это время Марти сидит, уткнувшись в телефон и что-то там просматривает
    img 16533
    with fade
    daniel "Эй, Марти! Ты когда-нибудь расстаешься с телефоном?"
    daniel "Натали, он в постель его тоже берет? Аха-ха!"
    img 16534
    with diss
    natalie "Марти очень много работает."
    natalie "Даже сейчас он просматривает документы по работе."
    natalie "Совсем не отдыхает. Да, дорогой?"
    marty "Угу..."
    # камера сзади Марти, он листает фотки на порно-сайте (его жене не видно, что он там смотрит)
    img 16535
    with diss
    w
#    music Groove2_85
    music BossaBossa
    img 16536
    with fade
    emma "Луиза, расскажи нам, чем ты занимаешься?"
    emma "Нэд ничего нам не рассказывал про тебя..."
    # Моника с удовольствие ловит свою минуту славы, расправляет плечи и с гордостью говорит
    img 16537
    with diss
    m "Я являюсь руководителем в одной крупной компании."
    img 16538
    with hpunch
    natalie "Ого!"
#    music BossaBossa
    img 16539
    with fade
    m "Да. Помимо основной деятельности, связанной с индустрией моды..."
    m "У меня еще бизнес в сфере недвижимости."
    img 16540
    with diss
    emma "О, серьезно?!" # удивленно
    img 16541
    with fade
    m "Да, у меня в подчинении много сотрудников."
    music Groove2_85
    img 16542
    with diss
    daniel "Твоя деятельность связана с модной индустрией?"
    emma "Расскажи нам. Это очень интересно!" # заинтересованность
    music BossaBossa
    img 16543
    with fade
    m "По работе мне часто приходится посещать публичные мероприятия..."
    m "Выступать перед публикой, давать интервью."
    m "И, конечно же, я всегда в курсе всех событий в мире моды."
    img 16544
    with diss
    ned "Да, Луиза очень занятая девушка." # дружелюбно
    ned "Редко такое бывает, что мы можем провести вечер вместе..."
    ned "Я вас давно хотел с ней познакомить, но у нее не бывает свободного времени."
    img 16545
    with diss
    ned "По вечерам она обычно ведет какие-нибудь переговоры..."
    ned "И важные бизнес-встречи."
    ned "Ведь такие встречи очень важны для развития ее бизнеса."
    ned "Да, дорогая?"
    img 16546
    with fade
    m "Все верно."
    m "У меня широкий круг знакомых, которые имеют немалый вес в этом городе..."
    m "И даже в стране."
    music Groove2_85
    img 16547
    with diss
    daniel "И как у тебя хватает времени на что-то, кроме работы?" # удивленно
    # Моника преисполнена важности, ей нравится здесь
    music BossaBossa
    img 16548
    with fade
    mt "Никчемные людишки..."
    mt "Млеют при виде меня и от мысли том, кто я такая!!!"
    img 16549
    with diss
    m "Да, это довольно непросто..."
    m "Грамотное планирование своего рабочего времени..."
    m "А также помощь моих личных ассистентов..."
    m "Позволяют мне иногда провести вечер не на работе, а в свое удовольствие."
    # Моника поворачивается к Нэду
    img 16550
    with fade
    m "Нэд, налей мне еще вина!" # в приказном тоне
    m "..."
    music Hidden_Agenda
    img 16551
    with diss
    m "Пожалуйста, дорогой." # выдавливает из себя улыбку
    music Groove2_85
    img 16552
    with diss
    ned "Конечно, любимая."
    # Затемнение, вино не показываем
    music stop
    img black_screen
    with diss
    sound pour_wine
    pause 2.0
    music Groove2_85
    img 16553
    with fadelong
    emma "Луиза, как тебе наш с Дэниелем дом?"
    emma "Мы его так долго выбирали..."
    emma "Это наш гостевой дом. Мы любим устраивать здесь вечеринки с друзьями."
    emma "У нас есть даже рояль!"
    img 16554
    with fade
    natalie "Но, к сожалению, никто из нас не умеет играть на нем..."
    img 16555
    with diss
    emma "Да..."
    m "Эмма, у вас чудесный дом. Он очень изысканный."
    img 16527
    with diss
    mt "Конечно, не такой изысканный как мой дом..."
    img 16556
    with fade
    m "А что касается игры на пианино..."
    music BossaBossa
    m "Я из высшего общества, как вы уже поняли..."
    m "Соответственно, у меня очень хорошее образование и воспитание."
    img 16557
    with diss
    m "В высшем обществе считается дурным тоном для девушки..."
    m "Неумение владеть каким-либо музыкальным инструментом."
    m "И я когда-то посещала занятия в музыкальной школе."
    # девушки смотрят на нее с восхищением
    music Groove2_85
    img 16558
    with fade
    emma "Правда?! Это замечательно, Луиза!"
    natalie "Сыграй нам что-нибудь, пожалуйста!!!"
    img 16559
    with diss
    m "Легко! Для меня это не составит никакого труда!"
    img 16560
    with fade
    emma "Мальчики, Луиза сейчас будет играть на пианино!"
    natalie "Нэд, почему ты раньше не познакомил нас с такой замечательной девушкой?!"
    img 16561
    with diss
    ned "..."
    # все внимание присутствующих на Монике, она встает и подходит к пианино
    # играет мелодию
    # все сидят на стульях за ней, открыв рты
    # после того, как Моника закончила играть, все хлопают и восхищенно на нее смотрят
    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 2.5
    music Prelude_in_C_BWV_846
    img 16563
    with fadelong
    w
    img 16564
    with fade
    w
    img 16565
    with diss
    w
    img 16566
    with diss
    w
    img 16567
    with fade
    w
    img 16568
    with diss
    w
    img 16569
    with fade
    w
    img 16570
    with diss
    w
    img 16571
    with diss
    w
    img 16572
    with fade
    w
    img 16573
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music BossaBossa
    img 16574
    with fade
    sound applause2
    w
    img 16575
    with diss
    w
    # затемнение, что прошло какое-то время, снова за столом (поменять им позы)
    # Моника сидит расслабленная, вся компания дружелюбно общается
    music stop
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16548
    with fadelong
    mt "Похоже, что эта работа не так уж и плоха..."
    mt "Нет, конечно это отвратительно, но..."
    mt "Учитывая другие варианты заработать деньги, эскорт не так уж плох..."
    mt "Я думала, что работа в эскорте будет моим кошмаром."
    mt "Однако, в большинстве своем, это вполне безобидное общение."
    img 16562
    with fade
    mt "Я, пожалуй, поработаю здесь, пока не решу все свои проблемы."
    mt "В любом случае, никто меня здесь не знает..."
    mt "Даже если будут вопросы, я скажу, что это мой двойник."
    mt "Если будет нужно, я найду где-нибудь в стране девушку, похожую на меня..."
    img 16527
    with diss
    mt "И предъявлю тем, кто будет что-то подозревать."
    mt "Конечно, она будет всего-лишь похожа на меня..."
    mt "У нее, конечно, не может быть такой красоты, которой обладаю Я!"
    mt "Но, все-же..."
    # Моника смотрит на Нэда, тот общается с Дэниелем
    img 16576
    with fade
    ned "Если у нас получится заключить с ними контракт..."
    ned "Наши продажи взлетят в несколько раз."
    img 16577
    with diss
    daniel "Нэд, я не стал бы делать такие оптимистичные прогнозы."
    daniel "С ними не так просто договориться, уж поверь мне..."
    daniel "Но если у тебя это получится сделать..."
    daniel "Я поговорю с директором о твоем повышении."
    # Моника перебивает их
    music BossaBossa
    img 16578
    with fade
    m "Нэд, подай мне салфетку."
    # Нэд не очень доволен, что она тут командует им, но выполняет ее просьбу
    img 16579
    with diss
    ned "..."
    ned "Конечно, дорогая."
    img 16580
    with fade
    m "И налей мне еще вина."
    img 16581
    with diss
    ned "..."
    # затемнение, не показываем как дается вино
    # в затемнении звук наливаемого вина # sound pour_wine
    # он снова отворачивается к Дэниелу
    music stop
    img black_screen
    with diss
    sound pour_wine
    pause 2.0
    music Groove2_85
    img 16582
    with fadelong
    natalie "Луиза, наши мужья всегда так себя ведут..."
    natalie "Постоянно только и разговоров, что о работе."
    img 16583
    with fade
    emma "Это точно."
    emma "Но мы с Натали уже привыкли."
    emma "Так что и ты привыкнешь."
    img 16584
    with diss
    natalie "Луиза, а какие у вас с Нэдом планы?"
    natalie "Вы уже живете вместе или просто встречаетесь?"
    emma "А может, вы собираетесь пожениться?"
    img 16585
    with diss
    natalie "Это было бы чудесно! Вы такая красивая пара!"
    emma "Нэд не делал тебе предложение?"
    # Моника
    music BossaBossa
    img 16586
    with fade
    m "Нэд только и думает, что о работе."
    m "Уверена, ему мысль о женитьбе даже в голову не приходила."
    img 16587
    with diss
    m "Но когда Нэд все-таки решится..."
    m "Ему придется постараться, чтобы я рассмотрела его предложение..."
    # девушки хихикают и смотрят на своих мужей
    img 16588
    with diss
    sound snd_woman_laugh3
    emma "Хи-хи-хи..."
    # те общаются, не обращая на них внимания
    music Groove2_85
    img 16589
    with fade
    natalie "Девочки, мне нужно выйти на улицу, во двор."
    natalie "Дэниел не разрешает курить в доме."
    natalie "Никто не хочет составить мне компанию?"
    img 16590
    with diss
    emma "Я с тобой, Натали."
    emma "Луиза, пойдем с нами?"
    img 16546
    with fade
    m "Да, пойдем."
    # в этот момент Нэд поворачивается к Монике
    img 16552
    with diss
    ned "Луиза, дорогая, останься со мной, пожалуйста."
    ned "Мы с тобой немного позже прогуляемся."
    img 16591
    with fade
    sound highheels_short_walk
    w
    # Моника остается с мужчинами, Натали с Эммой выходят из гостиной
    return

# в гостиной только Нэд, Дэниел, Марти и Моника
label ep211_escort_scene2_5:
    music stop
    img black_screen
    with diss
    pause 2.0
    # Моника сидит с самоуверенным видом, Нэд смотрит на нее, потом поворачивается к Дэниелу, смеясь
#    music Groove2_85
    music Turbo_Tornado
    img 16592
    with fadelong
    ned "Ну что, Дэниел! Я выиграл наше пари! Аха-ха!!!"
    ned "Гони мне мои деньги! Я сделал это!"
    ned "У меня получилось! Наконец-то!"
    # Дэниел в шоке, Марти удивленно откладывает свой телефон
    music stop
    img 16593
    with hpunch
    sound plastinka1b
    daniel "Что?!"
    marty "???"
    daniel "Ты про что?" # смотрит на Монику
    # ему приходит озарение
    music Turbo_Tornado
    img 16594
    with hpunch
    daniel "Ты про... про... Она что, проститутка?!" # с изумлением смотрит на Нэда
    img 16595
    with diss
    ned2 "Да!" # торжествующе
    m "Ч-что?" # Моника не верит в происходящее, растеряна
    m "???"
    img 16596
    with diss
    mt "Мне это послышалось?"
    sound Jump2
    img 16597
    with fade
    daniel "Не могу поверить! Нет!"
    daniel "Сколько раз ты пытался нас провести..."
    daniel "Я всегда чую проституток за версту!"
    daniel "Но как?! Нет! Я не верю!"
    # Марти с Дэниелем в шоке смотрят на Монику
    m "..."
    img 16598
    with diss
    marty "Пусть она сама нам скажет!"
    # Нэд поворачивается к Монике
    img 16599
    with fade
    ned2 "Ну? Скажи им, кто ты?"
    # Моника в напряжении как струна
    music Power_Bots_Loop
    img 16600
    with diss
    mt "!!!"
    mt "Я не могу поверить!!!"
    mt "Он это все... Подстроил из-за спора?!"
    mt "?!?!?!"
    music Hidden_Agenda
    img 16601
    with fade
    m "Я... Я его девушка..."
    # Дэниел смеется
    music Turbo_Tornado
#    music Groove2_85
    img 16602
    daniel "Аха-ха!"
    daniel "Ну что я говорил тебе! Я не могу ошибиться!"
    daniel "Ты не смог провести меня в те разы, не сможешь и теперь!"
    # Нэд недоволен, что ему не верят
    sound Jump2
    img 16603
    with hpunch
    ned2 "Нет! Она проститутка! Ее зовут [monica_hotel_name]."
    ned2 "Мы заключили пари..."
    ned2 "Если я приведу проститутку и ты не сможешь ее определить, то пари мое!"
    # Дэниел все еще не верит Нэду и спрашивает у Моники
    img 16604
    with fade
    daniel "Скажи, кто ты?"
    daniel "Ты ведь Луиза, правда?"
    # Моника пытается сохранить хорошую мину при плохой игре
    music Hidden_Agenda
    with fade
    m "Да. Я Луиза."
    m "Я девушка Нэда..."
    # Нэд злится на нее
    music Groove2_85
    img 16605
    with hpunch
    ned2 "Ну хватит уже!"
    ned2 "Говори им, кто ты! Твоя игра закончена, [monica_hotel_name]!"
    m "..."
    img 16606
    with diss
    ned2 "Если ты не скажешь, то я сообщу администратору сервиса эскорта..."
    ned2 "Что ты не выполняешь условия заказа!!!"
    music Power_Bots_Loop
    img 16607
    with diss
    mt "!!!"
    mt "Сволочь! Мерзавец!"
    menu:
        "Сказать, что я его девушка и уйти!":
            # Моника встает
            music BossaBossa
            img 16608
            with fade
            m "Я БЫЛА твоей девушкой!"
            m "Но, после того как ты посмел устроить такое при своих друзьях!"
            m "Я больше не хочу тебя видеть!"
            ned2 "!!!"
            # Моника гордо уходит
            sound highheels_short_walk
            img 16609
            with diss
            w
            music Groove2_85
            img 16610
            with fade
            daniel "Ну что, Нэд? Ты снова облажался!" # язвительно
            marty "Аха-ха!!!"
            img 16611
            with diss
            ned2 "..." # сидит злой, смотрит Монике вслед
            img 16612
            with diss
            daniel "Я тебе говорил, что за версту вижу шлюх!"
            return False
        "Сказать, что я работаю в эскорте.":
            $ monicaEscortNed1 = True # Моника сразу призналась друзьям клиента Нэда, что работает в эскорте
            pass
    # Моника зло смотрит на Нэда
    music Groove2_85
    img 16613
    with fade
    m "В условиях заказа было то, что я говорю, что я твоя девушка!"
    m "А не доказываю обратное!!!"
    m "Я соблюдаю условия!"
    # Нэд довольно восклицает
    music Turbo_Tornado
    img 16614
    with diss
    ned2 "Ага!"
    ned2 "Она заговорила про условия!"
    ned2 "Она призналась! Видишь, Дэниел?!"
    # Дэниел и Марти в шоке, смотрят на Монику
    img 16615
    with hpunch
    daniel "Что?!"
    daniel "Так ты действительно работаешь в эскорте?!"
    # Моника отвечает, напряженно
    music Hidden_Agenda
    with fade
    m "Я... Я действительно здесь не совсем из чувственных побуждений..."
    music Groove2_85
    img 16616
    with fade
    marty "А из каких?"
    # Моника кидает злой взгляд на Нэда
    img 16617
    with diss
    ned2 "Говори!"
    music Hidden_Agenda
    m "..."
    m "Из... Из несколько... Меркантильных..."
#    music Groove2_85
    music Turbo_Tornado
    img 16618
    with fade
    ned2 "Да она обычная проститутка из ВИП Эскорта!"
    ned2 "Из отеля Ле Гранд! Я там нашел ее!"
    mt "!!!"
    img 16619
    with diss
    marty "Я знаю всех, кто там работает..."
    marty "Я не видел ее там!"
    img 16620
    with fade
    ned2 "Она там работает совсем недавно, потому я ее и заприметил."
    ned2 "Я знал, что вы не могли ее там видеть."
    ned2 "И она держится так статно, что сложно поверить в то..."
    ned2 "Что она обычная проститутка."
    # Монику сидит злая
    music Power_Bots_Loop
    img 16621
    with diss
    mt "!!!"
    mt "Мерзавец! Никчемный неудачник!"
    mt "НЕНАВИЖУ!!!"
    # Дэниел вопросительно смотрит на Нэда
    music Groove2_85
    img 16622
    with fade
    daniel "То есть... Погоди... Если она все же проститутка..."
    daniel "То зачем ты притащил ее на эту встречу?!"
    daniel "Ведь здесь же наши жены, Нэд!!!" # возмущенно
    daniel "Ты что, совсем сдурел?! Ты за кого нас держишь, а?!"
    # Нэд самодовольно
    img 16623
    with diss
    ned2 "Я знал, что ты не сможешь раскусить ее здесь, при Эмме. Аха-ха!"
    ned2 "Если бы я привел ее в нашу сауну, как обычно приводил других..."
    ned2 "То не смог бы выиграть наше пари!"
    # Дэниел недовольно смотрит на него
    img 16624
    with fade
    daniel "Ладно, твоя взяла."
    daniel "Хотя..." # задумчиво
    music Sneaky_Snitch
    img 16625
    with diss
    daniel "Ты утверждаешь, что она проститутка..."
    daniel "И, если она проститутка, то, получается, я могу ее трахнуть?"
    ned2 "Конечно, можешь!"
    # Моника вскикивает
    music Power_Bots_Loop
    img 16626
    with hpunch
    m "ЧТО?!"
    m "Нет!"
    m "Мы так не договаривались!"
    m "Ты меня нанял только сопровождать тебя!!!"
    # Нэд спокойно отвечает
    music Groove2_85
    img 16627
    with fade
    ned2 "Твоя администраторша навязывала мне ваш прейскурант."
    ned2 "Она сказала, что я могу передумать в любой момент!"
    # Монику бомбит
    music Power_Bots_Loop
    img 16628
    with hpunch
    m "Нет!"
    m "!!!"
    music Groove2_85
    img 16611
    with fade
    ned2 "Твое агентство гарантировало мне, что с тобой не будет проблем!"
    ned2 "Мне позвонить твоему начальству?!"
    # Моника злится
    music Power_Bots_Loop
    img 16629
    with diss
    mt "Сволочь!!!"
    mt "Компания придурков!"
    mt "Жалкие неудачники!"
    mt "!!!"
    # Дэниел и Марти смотрят на Монику и пускают слюни
    # Подмигивает
    music Sneaky_Snitch
    img 16630
    with fade
    daniel "Нэд, скажи, ты уже далал это?"
    daniel "Пробовал ее? Ну и как она?"
    img 16631
    with diss
    ned2 "Если честно, то нет."
    ned2 "Я договорился только сопровождать меня."
    ned2 "Доплачивать за секс $ 500 - для меня дороговато."
    img 16632
    with diss
    ned2 "А вдруг бы ты раскусил ее? Тогда наше пари не покрыло бы мои расходы."
    ned2 "Так что с нашим пари? Ты признаешь, что я выиграл?"
    music Turbo_Tornado
    img 16612
    with fade
    daniel "Да, черт возьми!"
    daniel "И если ты ее еще не пробовал, то я буду первым!"
    daniel "Я хочу трахнуть ее прямо сейчас!"
    # Марти удивленно
    img 16616
    with diss
    marty "А как же Эмма?"
    marty "Она и Натали придут с минуты на минуту!"
    # Дэниел отмахивается
    img 16633
    with fade
    daniel "К черту! Ребята, соврите что-нибудь!"
    daniel "Скажите, что у меня важный звонок, а у Луизы..."
    daniel "У Луизы закружилась голова и она ушла в уборную!"
    daniel "И попросила ее не беспокоить!"
    # Дэниел обращается к Монике
    img 16634
    with diss
    daniel "Как там тебя зовут?"
    m "..."
    ned2 "[monica_hotel_name]."
    daniel "[monica_hotel_name], пойдем за мной!"
    # Моника растеряна
    img 16635
    with fade
    m "Но..."
    m "Нет... Я не пойду... Я..."
    # Нэд берет в руки телефон, говорит сердито
    music Power_Bots_Loop
    img 16636
    with diss
    sound snd_phone1
    ned2 "Все! Я звоню в ВИП Эскорт!"
    ned2 "Скажу, что девушка отказывается работать по прейскуранту!"
    img 16607
    with fade
    mt "Черт! Что же мне делать?!"
    mt "Я просто хотела заработать немного денег..."
    mt "Я не предполагала, что это зайдет так далеко!"
    mt "!!!"
    # Нэд говорит по телефону
    music Groove2_85
    img 16637
    with diss
    ned2 "Добрый вечер. Да, я передумал..."
    ned2 "Я хочу взять некоторые пункты из вашего прейскуранта."
    # ему по телефону отвечает администратор, показывается из рецепшина отеля. Администратор улыбается в трубку
    img 30116
    with fadelong
    reception "Да, сэр. Мы рады оказать Вам любые перечисленные в прейскуранте услуги!"
    img 16638
    with fade
    ned2 "Видите ли... Эта девушка... Она..." # Нэд смотрит на Монику
    img 30117
    with fadelong
    reception "Она что, отказывается что-то делать?!"
    reception "Передайте ей, что она будет оштрафована или уволена!"
    img 16639
    with fade
    ned2 "Она..."
    # Нэд отстраняется от телефона и говорит Монике
    ned2 "Так ты согласна?"
    img 16640
    with diss
    m "!!!"
    $ menu_corruption = [0, monicaEscortScene2CorruptionRequired1]
    menu:
        "Уйти!":
            # Моника встает
            music Power_Bots_Loop
            img 16641
            with hpunch
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            music Groove2_85
            img 16642
            with fade
            ned2 "Эй... Полегче!"
            ned2 "А то останешься без денег!"
            music Power_Bots_Loop
            img 16643
            with diss
            sound highheels_short_walk
            m "Засунь их себе в задницу!"
            m "!!!"
            return False
        "Согласиться пойти с Дэниелем.":
            $ monicaEscortNed2 = True # Моника согласилась пойти с Дэниелем и заняться с ним сексом
            pass
    # Моника злится
    music Power_Bots_Loop
    img 16621
    with fade
    mt "!!!"
    mt "Мерзавец!!!"
    mt "Если я сейчас откажусь, меня выгонят из эскорта!"
    mt "Что же делать?!"
    mt "Я не могу потерять эту работу..."
    img 16644
    with diss
    mt "Я Моника Бакфетт и никогда не соглашусь на что-то подобное!"
    mt "..."
    music Groove2_85
    img 16607
    with fade
    mt "Мне нужно представить, что я не Моника Бакфетт, а [monica_hotel_name]."
    mt "Для [monica_hotel_name] обслужить клиента - несложное дело."
    mt "Для [monica_hotel_name] важна только сумма заработка за вечер."
    mt "Поэтому [monica_hotel_name] сейчас согласится пойти с Дэниелем..."
    # Моника сквозь зубы
    music Hidden_Agenda
    img 16617
    with diss
    m "Я все слышала и нет необходимости никого увольнять."
    m "Я согласна."
    # мужчины ехидно улыбаются
    music Turbo_Tornado
    img 16604
    with fade
    ned "Ну вот. Другое дело."
    daniel "[monica_hotel_name], пошли за мной."
    daniel "Давай, быстрее. У меня не так много времени."
    # Дэниел встает и идет к выходу их гостиной, Моника идет за ним с каменным лицом
    return

# вторая комната в доме
label ep211_escort_scene2_6:
    # Моника с Дэниелем заходят в комнату, он поворачивается к ней и хваает ее за попу, прижимает к себе
    # Монике противно, но она не сопротивляется
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_5
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 16681
    with fadelong
    w
    img 16682
    with fade
    daniel "Я с самого начала вечера захотел трахнуть тебя, [monica_hotel_name]."
    music Power_Bots_Loop
    img 16683
    with diss
    mt "Эмма, видимо, и не подозревает, какой он козел на самом деле."
    mt "Может, рассказать ей?"
    # Дэниел продолжает лапать Монику
    music Groove2_85
    img 16685
    with fade
    daniel "Даже если ты была бы женой Нэда..."
    daniel "Я непременно сделал бы это в один из дней!"
    img 16684
    with diss
    daniel "Я весь вечер раздумывал над тем, как осуществить это..."
    daniel "И вовсе не ожидал, что трахнуть такую как Луиза будет так просто!"
    music Power_Bots_Loop
    img 16686
    with fade
    mt "!!!"
    mt "Мерзавец!"
    music Groove2_85
    img 16692
    with diss
    daniel "Скорее раздевайся!"
    # Моника парится
    img 16687
    with fade
    m "Дэниел, я... Могу я тебя попросить?"
    daniel "Что такое, [monica_hotel_name]?"
    img 16688
    with diss
    m "Я не хочу, чтобы о том, что здесь произойдет, кто-то узнал..."
    img 16689
    with fade
    daniel "Конечно, [monica_hotel_name]!"
    daniel "Я не собираюсь никому рассказывать про такую сладкую детку."
    img 16690
    with diss
    daniel "Я не хочу делиться тобой с кем-то!"
    daniel "Я буду заказывать тебя и трахать тебя сам!"
    daniel "Снимай с себя это скорее! Мне не терпится!"
    # Моника медлит
    music Power_Bots_Loop
    img 16691
    with fade
    mt "[monica_hotel_name] сейчас снимет с себя платье."
    mt "И будет зарабатывать деньги."
    mt "Это просто работа."
    # Моника раздевается, Дэниел приспускает штаны
    music Loved_Up
    img 16693
    with diss
    sound snd_fabric1
    daniel "Ложись на диван и раздвинь ноги."
    # Моника ложится на диван, Дэниел наваливается на нее сверху, лапает грудь, попу, рассматривает ее прелести
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music2 Loved_Up

    img 16694
    with fadelong
    daniel "Ммммм, какая же ты охренительная, детка..."


    img 16695
    with fade
    daniel "Я никому тебя не отдам."
    daniel "Я буду твоим постоянным клиентом."

    img 16696
    with diss
    daniel "Ты будешь трахаться только со мной."
    img 16697
    with fade
    mt "У тебя, неудачник, денег на меня не хватит..."


    # Дэниел входит в киску Моники и начинает двигаться
    img 16698
    with diss
    daniel "О, ты просто супер, [monica_hotel_name]!"
    daniel "Такая горячая! Такая охренительная!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent1_Monica_Guy1_Sex_1_1 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_1.mkv", fps=30)
    show videov_EscortEvent1_Monica_Guy1_Sex_1_1
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent1_Monica_Guy1_Sex_1_2 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_2.mkv", fps=30)
    show videov_EscortEvent1_Monica_Guy1_Sex_1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16699
    with fade
    daniel "Дааа! Хочу трахать тебя каждый день!"
    daniel "Мммммм..."

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
        scene black
        image videov_EscortEvent1_Monica_Guy1_Sex_1_3 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_3.mkv", fps=30)
        show videov_EscortEvent1_Monica_Guy1_Sex_1_3
        with fade
        wclean
        stop music
    #    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent1_Monica_Guy1_Sex_1_4 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_4.mkv", fps=30)
    show videov_EscortEvent1_Monica_Guy1_Sex_1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 16700
    with diss
    daniel "О, просто чертовски охренительно!!!"
    daniel "Даааа!"


    img 16701
    sound ahhh4
    with diss
    daniel "Ааааа!!!"
    music stop
    music2 stop
    # затемнение экрана, надпись "В это время в гостиной..."
    return

# смена кадра. гостиная
label ep211_escort_scene2_7:
    # Показывается как сидит компания, Эмма с Натали уже вернулись и сидят за столом
    # Меняем им позы!
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("В это время в гостиной...")) from _rcall_textonblack_6
    pause 1.5
    music Groove2_85
    img 16645
    with fadelong
    emma "Нэд, Марти, а где Дэниел?"
    music Marty_Gots_a_Plan
    img 16646
    with fade
    marty "Ему позвонили с работы. Какой-то срочный звонок."
    marty "Он пошел в свой кабинет на второй этаж, чтобы поговорить без посторонних."
    marty "Он не хочет, чтобы ему мешали разговаривать по телефону."
    music Groove2_85
    img 16538
    with diss
    natalie "А где Луиза?"
    music Marty_Gots_a_Plan
    img 16647
    with fade
    ned2 "У нее началось небольшое недомогание и она ушла в туалет."
    ned2 "Попросила нас пока веселиться и не беспокоить ее."
    ned2 "Она скоро придет."
    img 16648
    with diss
    natalie "Странно."
    marty "Что странного?"
    natalie "Что парень и девушка одновременно отсутствуют..."
    # Эмма хихикает
    music Groove2_85
    img 16649
    with fade
    emma "Натали, уж не думаешь ли ты, что такая как Луиза..."
    emma "Станет общаться с моим оболтусом и хамом?"
    music Marty_Gots_a_Plan
    img 16650
    with diss
    marty "..."
    img 16651
    with diss
    ned2 "..."
    music Groove2_85
    img 16652
    with fade
    emma "Да и я его знаю..."
    emma "Дэниел никогда бы не стал поступать так по отношению к Нэду."
    emma "Так что, не говори ерунды. Они скоро придут."
    emma "А пока давайте веселиться!"
    img 16590
    with diss
    natalie "Да, ты права. Я слишком подозрительна..."
    natalie "Марти, дорогой, налей мне еще вина."
    # кадр меняется на вторую комнату в доме
    return

# вторая комната в доме
label ep211_escort_scene2_8:
    # Снова сцена секса Дэниела и Моники
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("В соседней комнате...")) from _rcall_textonblack_7
    pause 1.5
#    music Loved_Up
    music stop
    music2 Turbo_Tornado
    img 16702
    with fadelong
    daniel "Мммммм..."
    daniel "Какие же у тебя сиськи!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent1_Monica_Guy1_Sex_1_5 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_5.mkv", fps=30)
    show videov_EscortEvent1_Monica_Guy1_Sex_1_5
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent1_Monica_Guy1_Sex_1_6 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_6.mkv", fps=30)
    show videov_EscortEvent1_Monica_Guy1_Sex_1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16703
    with fade
    sound ahhh6
    daniel "Даааа!"
    daniel "В следующий раз я куплю тебя на всю ночь!"

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent1_Monica_Guy1_Sex_1_1.ogg"
        scene black
        image videov_EscortEvent1_Monica_Guy1_Sex_1_7 = Movie(play="video/v_EscortEvent1_Monica_Guy1_Sex_1_7.mkv", fps=30)
        show videov_EscortEvent1_Monica_Guy1_Sex_1_7
        with fade
        wclean
        stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 16704
    with diss
    daniel "И буду трахать тебя до утра!"
    daniel "Ааааа!!!"
    # в комнату заходит Марти
    # Дэниел испуганно
    music2 stop
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Pyro_Flow
    img 16705
    with hpunch
    sound plastinka1b
    daniel "Эй! Что ты делаешь здесь?!"
    daniel "Что-то случилось?!"
    daniel "Эмма что-то заподозрила?!"
    img 16706
    with diss
    w
    img 16707
    with fade
    marty "Нет, все в порядке!"
    img 16708
    with diss
    daniel "Тогда зачем ты приперся сюда?"
    marty "Я сказал, что пойду проверю, все ли у тебя хорошо."
    # Дэниел отворачивается от Марти, смотрит на Монику
    # делает еще несколько движений и кончает
    music Loved_Up2
    img 16762
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    daniel "Ааааа..."
    img 16763
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    daniel "Твою мать! ДА!!!"
    img 16764
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan3
    daniel "АААААА!!!"
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound snd_zip
    pause 1.0
    music Groove2_85
    # отлепляется от Моники, встает и надевает штаны
    # Моника садится на диване, прикрывается руками и тянется за своим платьем
    img 16709
    with fade
    daniel "У меня все хорошо, как видишь."
    # Марти ухмыляется
    music Loved_Up
    img 16710
    with diss
    marty "Вижу..."
    marty "Вообще-то, я спросил у Нэда..."
    marty "И он разрешил мне тоже воспользоваться Луизой или как там ее зовут."
    img 16711
    with fade
    m "!!!"
    daniel "Аха-ха!"
    daniel "Я уже закончил, так что можешь делать с ней все, что хочешь!"
    # Моника возмущенно
    music Power_Bots_Loop
    img 16712
    with vpunch
    m "Нет!!!"
    m "Я занималась этим с одним человеком!"
    m "Не было условия, чтобы делать это с кем-то еще!!!"
    music Groove2_85
    img 16713
    with fade
    marty "Нэд сказал, что дополнительный клиент стоит сверху $ 400."
    marty "Это входит в твой прейскурант."
    m "А почему $ 400?! Разве не должно быть дороже, если клиентов больше?!"
    img 16714
    with diss
    marty "Администратор сказала Нэду, что у тебя индивидуальный прейскурант."
    marty "Чем больше мужчин, тем дешевле!"
    marty "Аха-ха!"
    img 16715
    with diss
    daniel "Аха-ха!"
    # Монику бомбит
    img 16716
    with fade
    sound man_steps
    w
    music Power_Bots_Loop
    img 16717
    with diss
    mt "Сволочь!"
    mt "Сучка!!!"
    mt "Ненавижу эту тварь!!!"
    mt "Она специально сделала это!"
    img 16718
    with diss
    mt "Она мстит мне за то, что я обозвала ее никчемной и обещала уволить!"
    mt "Между прочим, вполне заслуженно!"
    mt "Это несправедливо!!!"
    mt "Дьявол!!!"
    # Дэниел уходит, Марти остается и смотрит на Монику вопросительно
    music Groove2_85
    img 16719
    with fade
    marty "Ну так что? Я могу сделать это?"
    m "!!!"
    $ menu_corruption = [0, monicaEscortScene2CorruptionRequired2]
    menu:
        "Уйти!":
            # Моника встает
            music Power_Bots_Loop
            img 16720
            with hpunch
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            music Groove2_85
            img 16721
            with fade
            marty "Эй... Полегче!"
            marty "А то останешься без денег!"
            music Power_Bots_Loop
            img 16722
            with diss
            sound highheels_short_walk
            m "Засунь их себе в задницу!"
            m "!!!"
            return False
        "Смириться с прейскурантом.":
            $ monicaEscortNed3 = True # Моника смирилась с прейскурантом и занялась сексом с Марти
            pass
    # Моника смотрит на него с ненавистью
    music Power_Bots_Loop
    img 16723
    with diss
    mt "!!!"
    mt "Ненавижу их всех!"
    img 16724
    with diss
    mt "Поотрывала бы им яйца!!!"
    mt "Мерзкие неудачники!"
    music Groove2_85
    img 16725
    with fade
    marty "Ну? Чего молчишь? Ты согласна?"
    img 16726
    with diss
    mt "С другой стороны..."
    mt "[monica_hotel_name] за этот вечер неплохо заработает."
    mt "И, так получается, что деньги у меня с ней общие..."
    img 16727
    with fade
    m "Да... Согласна..."
    # Марти приспускает штаны, указывает Монике на диван или еще куда-нибудь, на окно (подоконник), например
    img 16728
    with diss
    marty "Снимай платье и иди к дивану!"
    marty "Вставай раком!"
    marty "Давай, быстрее! Пока моя жена ничего не заподозрила!"
    # Моника зло на него смотрит и выполняет приказ, Марти подходит к ней сзади
    # затемнение экрана, надпись "В это время в гостиной..."
    return

# гостиная
label ep211_escort_scene2_9:
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("В это время в гостиной...")) from _rcall_textonblack_8
    pause 1.0
    music Groove2_85
    # все в сборе, кроме Марти и Моники, Натали смотрит вопросительно на Дэниела
    img 16653
    with fadelong
    natalie "Дэниел, куда Марти ушел?"
    # Дэниел спокойно сидит и врет ей
    music Marty_Gots_a_Plan
    daniel "Марти нашел меня и спросил, все ли у меня в порядке."
    daniel "Я как раз закончил разговор и собирался возвращаться."
    daniel "Тогда Марти решил зайти в туалет и я проводил его."
    img 16654
    with fade
    daniel "Нам пришлось идти в другой туалет, потому что основной был занят."
    daniel "Там, видимо, сейчас Луиза."
    daniel "Мы даже слышали какие-то звуки. Похоже, что ее тошнит."
    music Groove2_85
    img 16655
    natalie "Бедняжка!"
    # с сочувствием, Дэниел с Нэдом заговорщицки переглядываются и усмехаются
    img 16656
    with diss
    natalie "Она, должно быть, выбрала какое-то не то сочетание продуктов."
    natalie "Эмма, может быть, нам стоит сходить к ней?" # обращается к Эмме
    natalie "Проверим, все ли с ней хорошо?"
    # кадр меняется на вторую комнату в доме
    return

# вторая комната в доме
label ep211_escort_scene2_10:
    # Снова сцена секса Марти и Моники, Моника стоит нагнувшись, Марти пристроился сзади и двигается
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("В соседней комнате...")) from _rcall_textonblack_9
    pause 1.5
    music2 Turbo_Tornado
    img 16729
    with fadelong
    marty "Мммм, какая у тебя клевая попка!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_1 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_1.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16730
    with fade
    sound ahhh7
    marty "Такая упругая..."
    # Моника со злым лицом

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_2 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_2.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16731
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_3 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_3.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16732
    with fade
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_4 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_4.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16733
    with diss
    w
    img 16734
    with fade
    mt "Когда же он уже кончит и отстанет от меня?"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_5 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_5.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_5
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_6 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_6.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16735
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_7 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_7.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_7
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16736
    with fade
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy3_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy3_Sex_1_8 = Movie(play="video/v_EscortEvent2_Monica_Guy3_Sex_1_8.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy3_Sex_1_8
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 16737
    with diss
    marty "О, дааа!"
    marty "Мммммм..."
    # Марти он кончает
#    music2 stop
#    music Loved_Up2
    img 16738
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    marty "ААААААХ!!!"
    w
    img 16739
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "Ну наконец-то!!!"
    mt "Надо одеваться и скорее уходить из этого чертового дома!!!"
    img 16740
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan5
    music stop
    music2 stop
    # затемнение экрана, надпись "В это время в гостиной..."
    return

# гостиная
label ep211_escort_scene2_11:
    # Переключение на компанию
    # Заказчик говорит Натали и Эмме
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("В это время в гостиной...")) from _rcall_textonblack_10
    pause 1.5
    music Marty_Gots_a_Plan
    img 16657
    with fadelong
    ned2 "Не стоит. Я сейчас сам пойду к Луизе и проверю, как она себя чувствует."
    music Groove2_85
    img 16658
    with fade
    emma "Да, конечно. Пусть Нэд идет." # обращается к Натали, потом говорит Нэду
    img 16659
    with diss
    emma "Нэд, тебе стоит заботиться о такой хорошей девушке, как Луиза."
    emma "Иначе ты рискуешь ее потерять."
    img 16660
    with fade
    emma "Должно быть, у нее действительно к тебе чувства..."
    emma "Раз такая как она согласилась встречаться с тобой."
    # Нэд еле заметно ухмыляется
    music Marty_Gots_a_Plan
    img 16661
    with diss
    ned2 "Да, Эмма. Луиза моя девушка и я очень горжусь этим!"
    # кадр меняется на вторую комнату в доме
    return

# вторая комната в доме
label ep211_escort_scene2_12:
    # Марти одевает штаны, Моника уже надела платье и поправляет его
    # Забегает Нэд.
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("В соседней комнате...")) from _rcall_textonblack_11
    pause 1.5
    music Turbo_Tornado
    img 16741
    with vpunch
    ned2 "Черт! Пустите меня!"
    ned2 "Теперь моя очередь! Дайте сюда!"
    ned2 "Я должен ее трахнуть тоже! Все-таки, это моя девушка!!!"
    # Моника смотрит на него зло и хочет что-то сказать
    music Power_Bots_Loop
    img 16742
    with fade
    m "!!!"
    m "Ты..."
    # Нэд перебивает ее
    music Turbo_Tornado
    img 16743
    with diss
    ned2 "$ 200! Следующий клиент стоит $ 200!!!"
    ned2 "Я специально подождал, чтобы получить скидку!!!"
    img 16744
    with fade
    ned2 "Жаль, мы не взяли с собой Джима!"
    ned2 "Тогда мне бы это обошлось всего в $ 100!"
    music Power_Bots_Loop
    img 16745
    with diss
    mt "Жалкий жадный неудачник!!!"
    mt "Подонок!!!"
    m "!!!"
    $ menu_corruption = [0, monicaEscortScene2CorruptionRequired3]
    menu:
        "Уйти!":
            # Моника встает
            music Power_Bots_Loop
            img 16750
            with hpunch
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            music Groove2_85
            img 16751
            with fade
            ned2 "Эй... Полегче!"
            ned2 "А то останешься без денег!"
            music Power_Bots_Loop
            img 16752
            with diss
            sound highheels_short_walk
            m "Засунь их себе в задницу!"
            m "!!!"
            return False
        "Смириться, иначе меня ждет штраф или увольнение.":
            $ monicaEscortNed4 = True # Моника после секса с Дэниелем и Марти занялась сексом с Нэдом
            pass
    # Моника смотрит на него с ненавистью
    music Groove2_85
    img 16746
    with fade
    mt "!!!"
    mt "Это просто работа..."
    # Нэд хватает Монику под попу, прислоняет ее спиной к стене, расстегивает штаны, задирает ее платье и входит в нее
    music Turbo_Tornado
    img 16747
    with diss
    ned2 "Даааа!!!"
    # Марти стоит смотрит на них
    img 16748
    with fade
    marty "Эй, Нэд! Натали ничего не спрашивала про меня?"
    # Нэд, не прекращая трахать Монику
    img 16749
    with diss
    ned2 "Нет, но беги скорее, а то тебя начнут искать!"
    m "!!!"
    ned2 "Раздевайся!"
    ned2 "Я хочу трахнуть тебя прямо на этом пуфе!"
    # Марти убегает довольный
    # спустя несколько минут
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music2 Turbo_Tornado
    img 16753
    with fadelong
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_1 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_1.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16754
    with fade
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_2 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_2.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16755
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_3 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_3.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_3
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_4 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_4.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_4
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_5 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_5.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16756
    with fade
    ned2 "Аааа..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_6 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_6.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_6
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
    scene black
    image videov_EscortEvent2_Monica_Guy2_Sex_1_7 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_7.mkv", fps=30)
    show videov_EscortEvent2_Monica_Guy2_Sex_1_7
    with fade
    wclean
    stop music
#    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    if game.extra == True:
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_EscortEvent2_Monica_Guy2_Sex_1_1.ogg"
        scene black
        image videov_EscortEvent2_Monica_Guy2_Sex_1_8 = Movie(play="video/v_EscortEvent2_Monica_Guy2_Sex_1_8.mkv", fps=30)
        show videov_EscortEvent2_Monica_Guy2_Sex_1_8
        with fade
        wclean
        stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 stop
    img black_screen
    with diss
    pause 1.5
    img 16757
    music Loved_Up2
    with fadelong
    sound ahhh8
    ned2 "Аааааа..."
    img 16758
    with fade
    w

    img 16759
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    ned2 "Аааааааа..."
    img 16760
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    ned2 "АААААА!!!" # кончает
    w
    img 16761
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan8
    # затемнение экрана
    return

# гостиная
label ep211_escort_scene2_13:
    # Снова сцена компании, где все сидят за столом, включая Монику
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_12
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16662
    with fadelong
    w
    img 16663
    with fade
    mt "Я не могу смотреть на этих похотливых козлов!"
    mt "Они только что изменили своим женам!"
    mt "Изменили, сделав... сделав... Даже не хочу об этом думать!"
    mt "А теперь сидят и лгут им! Как ни в чем не бывало!"
    music Power_Bots_Loop
    img 16664
    with diss
    mt "Как же это мерзко!"
    mt "А более мерзко то, что мне после всего..."
    mt "После всей этй грязи..."
    mt "Мне нужно тоже притворяться перед Эммой и Натали!"
    mt "Это какой-то кошмар!"
    # Нэд обращается к Монике
    music Groove2_85
    img 16665
    with fade
    ned2 "Луиза, любимая, ты себя уже лучше чувствуешь?"
    m "Да..."
    m "Спасибо за твою заботу, дорогой..."
    music Power_Bots_Loop
    img 16666
    with diss
    mt "Подонок!!!"
    music Groove2_85
    img 16667
    with fade
    natalie "Луиза, мы с Эммой так переживали за тебя."
    emma "Тебе точно стало лучше? Может, тебе дать какие-нибудь лекарства?"
    music Power_Bots_Loop
    img 16668
    with diss
    mt "Дайте мне яду. Я налью его в бокалы ваших козлов!"
    music Groove2_85
    img 16669
    with diss
    m "Мне уже лучше, спасибо."
    img 16553
    with fade
    natalie "Ну и хорошо. Луиза, у меня на завтра запланирован шоппинг."
    natalie "Эмма тоже ко мне присоединиться. Не хочешь составить нам компанию?"
    emma "Да, это отличная идея!"
    emma "Луиза, ты же хорошо разбираешься в моде..."
    img 16670
    with diss
    emma "Пойдем завтра с нами!"
    emma "Погуляем по магазинам, зайдем в ресторан."
    natalie "Потом можно будет сходить в СПА. Мы отлично проведем время!"
    music Hidden_Agenda
    img 16671
    with fade
    m "Спасибо за предложение, девочки, но..."
    m "У меня завтра много работы."
    m "У меня каждый день расписан буквально поминутно."
    m "К сожалению, у меня не будет времени."
    music Groove2_85
    img 16664
    with diss
    mt "Не хватало еще тратить на всякую ерунду деньги, которые я заработала с таким трудом..."
    mt "Тем более, их даже не хватит на новую сумочку..."
    img 16584
    with fade
    emma "Жаль..."
    natalie "Луиза, у тебя такой плотный рабочий график."
    natalie "Когда вы успеваете встречаться с Нэдом?"
    img 16665
    with diss
    m "..."
    m "По вечерам... Мы уделяем друг другу время."
    ned2 "Да, любимая. Мы стараемся встречаться каждый вечер."
    img 16547
    with fade
    emma "Наверное, это так волнительно - ждать вечера, чтобы встретиться с любимым..."
    m "..."
    natalie "Луиза, а Нэд часто дарит тебе подарки?"
    img 16648
    with diss
    natalie "Мне вот Марти дарит цветы только по праздникам..."
    marty "Дорогая, ну ты же итак знаешь, что я тебя люблю..."
    natalie "Знаю. Но мне все равно хочется внимания."
    natalie "А ты только и знаешь, что сидишь целыми вечерами в телефоне и работаешь!"
    marty "Ну не обижайся. Я стараюсь ради нас с тобой." # целуются
    music Loved_Up
    img 16673
    with diss
    sound snd_kiss2
    w
    img 16530
    with fade
    emma "А мой Дэниел часто балует меня цветами и всякими приятными сюрпризами."
    daniel "Конечно, любимая. Мне нравится делать тебя счастливой." # тоже целуются
    music Loved_Up
    img 16674
    with diss
    sound snd_kiss2
    w
    music Power_Bots_Loop
    img 16675
    with fade
    mt "Боже... Меня сейчас стошнит от этого всего..."
    music Groove2_85
    img 16672
    with diss
    ned2 "Луиза, дорогая. Мне кажется, тебе снова нехорошо."
    ned2 "Может быть, я отвезу тебя домой?"
    m "Да, дорогой. Я буду тебе очень благодарна."
    img 16676
    with fade
    m "Спасибо за приятный вечер." # говорит с натянутой улыбкой
    m "Я была рада с вами познакомиться."
    # Моника с Нэдом встают, Эмма с Натали подходят к Монике, целуют в щечку или обнимают
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16677
    with fadelong
    emma "Я надеюсь, вы с Нэдом к нам еще приедете."
    emma "Я буду очень рада тебя видеть, Луиза!"
    img 16678
    with fade
    natalie "И мы обязательно еще сходим с тобой на шоппинг!"
    m "Хорошо. Обязательно."
    music Marty_Gots_a_Plan
    img 16679
    with diss
    marty "Пока, Луиза. Приятно было познакомиться."
    img 16680
    with diss
    daniel "И мне тоже было приятно. Пока."
    # Моника выдавливает из себя улыбку
    # затемнение экрана
    return

# служебный коридор ресторана в отеле Ле Гранд
label ep211_escort_scene2_14(escort2_status):
    # разговор администраторши и Моники
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 30016
    with fadelong
    sound highheels_short_walk
    w
    img 30017
    with fade
    mt "Ненавижу эту никчемную администраторшу!"
    mt "!!!"

    if escort2_status != 1:
        # Если Моника ушла от клиентов, отказавшись обслуживать любого из них, то администратор орет на Монику
        music Power_Bots_Loop
        img 30018
        with diss
        reception "[monica_hotel_name]!!!"
        reception "Мне звонил клент!"
        reception "Он крайне недоволен твоим поведением!"
        reception "Какого черта ты решила, что можешь диктовать свои условия клиенту?!"
        music Groove2_85
        img 30020
        with fade
        m "Он изменил первоначальные условия..."
        music Power_Bots_Loop
        img 30021
        with diss
        reception "Да!!! И он имел на это право!!!"
        music Groove2_85
        img 30022
        with fade
        reception "Я тебя прощаю на первый раз и ограничусь только штрафом!"
        reception "В следующий раз ты за подобное поведение вылетишь отсюда!!!"
        img 30023
        with diss
        reception "У нас ВИП Эскорт! Такое отношение к клиентам недопустимо!"
        reception "Ты поняла меня?!?!"
        img 30024
        with fade
        m "Да..."
        music Power_Bots_Loop
        img 30025
        with diss
        mt "Сучка!"
        mt "Ненавижу!"
        music Groove2_85
        img 30019
        with diss
        sound highheels_short_walk
        w
        sound vjuh2
        img 30026
        with fade
        reception "Клиент за сопровождение заплатил $500."
        reception "Ты оштрафована за невыполнение услуг согласно прейскуранту."
        img 30027
        with diss
        reception "И с этих денег ты не получаешь ни цента!"
        img 30028
        with diss
        mt "!!!"
        m "Как?"
        img 30029
        with fade
        reception "Да, ни цента! И это ты еще легко отделалась!"
        reception "Еще хоть одно малейшее нарушение и тебя ждет увольнение!!!"
        reception "Тебе все понятно, [monica_hotel_name]?!"
        help "Увольнение будет реализовано в следующих апдейтах..."
        img 30030
        with diss
        m "Да..."
        music Power_Bots_Loop
        img 30031
        with diss
        $ notif_monica()
        if monicaBitch == True:
            mt "Гори в аду, мразь!"
        else:
            mt "!!!"

    else:
        # Если Моника обслужила клиентов
        music Groove2_85
        img 30032
        with fade
        reception "Ты хорошо справилась с сегодняшним заказом..."
        reception "Но клиент сказал, что ты вела себя нерешительно."
        img 30033
        with diss
        reception "[monica_hotel_name] должна сама предлагать услуги из прейскуранта!"
        reception "И не заставлять клиентов уговаривать себя!"
        img 30034
        with diss
        reception "Если подобное поведение будет встречено еще раз..."
        reception "То ты будешь оштрафована, понятно?!"
        img 30024
        with fade
        m "Да..."
        mt "!!!"
        img 30035
        with diss
        reception "Клиент заплатил $500 за сопровождение на вечере..."
        reception "И $1100 за три дополнительные услуги из прейскуранта."
        reception "Твой заработок составляет 50 процентов от суммы."
        sound vjuh3
        img 30036
        with fade
        reception "То есть $800."
        reception "Вот твои деньги."
        # отдает ей 800 долларов
        $ add_money(800.0)
        img 30037
        with diss
        reception "Завтра можешь приходить снова."
        reception "На сегодня все. Клиенты не любят использованный товар."
        if char_info["ReceptionGirl"]["level"] == 1:
            $ add_char_progress("ReceptionGirl", 25, "ReceptionGirl_escort_scene2")
        img 30038
        with fade
        sound highheels_short_walk
        mt "Вот сучка!"
        mt "!!!"
        # Моника уходит
    return

label ep211_escort_scene2_15:
    mt "Не могу поверить что я позволила сделать такое с собой..."
    mt "С другой стороны, это немаленькие деньги для меня сейчас."
    mt "И все думают что я [monica_hotel_name]."
    mt "Никто не знает кто я такая на самом деле..."
    return
