label after_jail_house_outside:
    if homeVisited == True:
        mt "Мне лучше не приближаться к своему дому."
        "Иначе меня заберет полиция!!!"
        return

    # охранник
    music Power_Bots_Loop
    sound dogs_barking
    img 5588
    with fadelong
    house_guard "Мэм!"
    "Это частная собственность!"
    "Вы не имеет права здесь находиться!"
    img 5589
    m "Да!"
    "Это частная собственность!"
    "И она моя!"
    "А ты кто такой вообще?"
    "Дай пройти!"
    img 5590
    house_guard "Мэм."
    "Я еще раз повторяю что это частная собственность."
    m "Это мой дом!"
    "Пусти меня!"
    img 5591
    house_guard "Нет, Мэм."
    "Это дом Мистера Робертса."
    "Он меня нанял."
    "Я не знаю кто Вы."
    "Меня никто не предупреждал."
    img 5592
    m "Это не его дом!"
    "Его захватили нечестным путем!"
    "Это мой дом!"
    "МОЙ!!!"
    img 5593
    house_guard "Мэм."
    "Пожалуйста, сделайте несколько шагов назад."
    m "ПРОПУСТИ МЕНЯ!!!"
    img 5594
    house_guard "Мэм."
    "Я сейчас вызову полицию!"
    m "ПУСТИ МЕНЯ!!!"
    "ЭТО МОЙ ДОМ!!!"
    "ААААААААА!!!"
    img 5595
    house_guard "Мэм."
    "Я вызываю патруль."

    img black_screen
    with Dissolve(1)
    sound snd_phone1
    $ renpy.pause(2.0)

    img 5596
    with fadelong
    policeman "Полиция слушает."
    house_guard "Сэр!"
    "Это звонят с западной окраины города."
    "Я охранник частного дома."
    "Тут какая-то ненормальная пытается незаконно проникнуть на территорию."
    "Мне кажется она наркоманка."
    "Ведет себя неадекватно."
    "Пожалуйста, пришлите патруль!"
    policeman "Хорошо, сэр."
    "Патруль выезжает."
    img 5597
    mt "..."
    "О БОЖЕ!!!"
    "СЮДА ЕДЕТ ПОЛИЦИЯ!!!"
    img 5598
    "МНЕ НАДО СКОРЕЕ УБИРАТЬСЯ ОТСЮДА!!!"
    "ИНАЧЕ КОНЕЦ!!!"
    $ homeVisited = True
    $ remove_objective("home_visit")
    $ autorun_to_object("street_house_outside", "after_jail_house_outside2")
    if dickSearch == True and homeVisited == True and hotelVisited == True:
        $ s2ClothShopStage = 1

    call refresh_scene_fade() from _call_refresh_scene_fade_93

    return
label after_jail_house_outside2:
    mt "ЧТО"
    "МНЕ"
    "ДЕЛАТЬ???"
    "Я чуть не умерла там, в камере!"
    "Я думала что стоит только вырваться на свободу и все будет хорошо!"
    "Но мне негде даже переночевать!"
    "Мне надо найти какое-то место!"
    "Выспаться."
    "Собраться с силами."
    "Моника!"
    "Держись!"
    "Еще немного и все будет хорошо!"
    "Завтра я увижу Дика и он мне поможет!"
    return

label after_jail_dick_reception_dialogue0:
    img 2747
    with fadelong
    w
    img 2748
    with fade
    reception_secretary "Мэм!"
    "Вы куда?"
    return

label after_jail_dick_reception_dialogue1:
    if dickReceptionVisited == True:
        img 2748
        with fade
        reception_secretary "Мэм!"
        "Вы куда?"
    img 2749
    with fadelong
    m "Я в офис Дика Адвоката."
    img 2750
    reception_secretary "Мэм."
    "Его офис уже закрыт."
    "Его нет!"
    m "А вы можете с ним связаться?"
    "У вас есть его номер?"
    img 2751
    reception_secretary "Нет, Мэм."
    "У меня таких данных быть не может."
    "Я всего-лишь секретарь на рецепшене."
    img 2752
    "Заходите завтра."
    "Он должен быть."
    img 2753
    mt "Жаль..."
    m "Хорошо, спасибо."
    "Я зайду завтра."
    mt "..."
    img 2754
    with fadelong
    mt "..."
    mt "Что же мне делать?"
    mt "Хорошо, Дика я увижу завтра."
    img 2755
    mt "Но куда мне сейчас идти?"
    if homeVisited == False:
        img 2756
        with fade
        mt "Этот жирный урод что-то говорил про мой дом."
        "Что там кто-то живет."
        "В любом случае надо пойти проверить."
        img 2757
        mt "МНЕ ЖЕ НАДО ГДЕ-ТО НОЧЕВАТЬ!!!"
    $ dickSearch = True
    $ remove_objective("dick_search")
    if dickSearch == True and homeVisited == True and hotelVisited == True:
        $ s2ClothShopStage = 1

    $ dickReceptionStage = 1
    call refresh_scene_fade() from _call_refresh_scene_fade_94
    return

label after_jail_rich_hotel1:
    music Stealth_Groover
    img 2658
    with fadelong
    reception "Здравствуйте, Мэм!"
    img 2659
    m "Здравствуйте."
    "Я хочу переночевать в этом месте."
    img 2660
    reception "Конечно, Мэм!"
    "Добро пожаловать!"
    "У нас лучший отель в городе!"
    img 2661
    m "Вот и посмотрим какой он."
    "Внешне он не выглядит лучшим."
    img 2662
    "Я уже вижу много недостатков."

    img 2663
    reception "Да, Мэм!"
    "Я понимаю."
    "Судя по Вам, Вы искушены в хороших отелях."
    "Вы, наверное, много где бывали и ..."
    img 2664
    m "Да, я много где бывала."
    "И хватит об этом!"
    "Давайте быстрее заселяйте меня!"
    "Не испытывайте моего терпения!"
    img 2665
    reception "... и мы стараемся держать уровень.."
    "Гхм.."
    img 2666
    "Мэм."
    "Да, конечно."
    "Сейчас мы Вас оформим."
    "Чем Вы будете платить?"
    "Наличными или картой?"

    img 2667
    with hpunch
    music Groove2_85
    m "Ээээээ.."
    "Ммммм.."
    img 2668
    music Power_Bots_Loop
    mt "!!!!!!!!!!!!!!!!"
    "У меня же нет денег!!!"
    img 2669
    "Черт!"
    "Черт, черт, черт!!!"
    "У меня все забрали в полиции!"

    img 2670
    music Groove2_85
    mt "Это совершенно не знакомое мне чувство!"
    "Я никогда не сталкивалась с проблемой того что на что-то нет денег."
    img 2671
    "Это стресс."
    "Мне надо будет походить к психотерапевту, поделать расслабляющие массажи и СПА."
    "..."
    img 2672
    "Но что сейчас-то делать?"
    img 2673
    with fade
    m "Видите-ли."
    "Дело в том что я только что из аэропорта."
    "Там произошла задержка багажа."
    "И мне привезут его утром."
    "Потому оплату я внесу во время утреннего завтрака."
    img 2674
    mt "С утра что-нибудь придумаю!"
    "А сейчас я мечтаю о нормальной постели!"
    "Мягкой и теплой!"
    img 2675
    "И еда!!!"
    "Я хочу есть!"
    img 2676
    reception "Мэм."
    "Я даже не знаю...."
    img 2677
    music Pyro_Flow
    m "Послушайте."
    "Взгляните на меня."
    "Вы считаете что у меня нет денег на вашу дыру?"
    img 2678
    reception "Нет, Мэм."
    "Конечно."
    "Вы выглядите очень респектабельно..."
    img 2679
    m "И вы собираетесь мне отказать?"
    img 2680
    "Вы в курсе какие рейтинги у моего аккаунта в сервисах размещения?"
    img 2681
    "Если вы откажете мне, то я красочно опишу эту ситуацию!"
    img 2682
    "Другие отели готовы будут бесплатно забрать меня отсюда на такси, лишь бы я осталась у них!"
    img 2683
    "И оставила хороший отзыв!"
    img 2684
    "В котором, кстати, могу упомянуть грамотного сотрудника рецепшина."
    img 2685
    "Который заслуживает повышения по службе!"
    img 2686
    reception "Мэм, спасибо, но..."
    "..."
    img 2687
    m "..."
    music Groove2_85
    img 2688
    reception "Хорошо, Мэм!"
    "Я заселю Вас под свою ответственность."
    img 2689
    m "Сразу бы так!"
    img 2690
    music Groove2_85
    reception "Мэм."
    "Пожалуйста, Ваши документы."
    img 2691
    reception "..."
    img 2692
    m "..."
    img 2693
    reception "..."
    img 2694
    m "..."
    img 2695
    reception "Мэм?"
    img 2696
    with fade
    music Power_Bots_Loop
    mt "О Боже!"
    "Я совсем забыла!"
    "У меня же нет документов с собой!"
    img 2697
    "Более того, у меня нет вообще никаких!"
    "НИКАКИХ!!!!!"
    "О БОЖЕ!!!"
    "..."
    img 2698
    music Groove2_85
    mt "Моника!"
    "Не вешай нос!"
    "Ты выбралась из такого кошмара не для этого!"
    "Ты выпутаешься из всего этого!"
    img 2699
    "И будешь на обложке своего журнала!"
    "Блестая женской красотой."
    "..."
    img 2700
    "А не на обложке с каким-то питомцем, который в меня входит..."
    img 2701
    music Power_Bots_Loop
    mt "О БОЖЕ!!!"
    "Я не могу об этом думать!"
    "Я не буду думать об этом!"
    "Эти мысли вселяют в меня ужас!"
    img 2702
    mt "..."
    img 2703
    music Groove2_85
    reception "Мэм?"
    "Вы себя хорошо чувствуете?"
    img 2704
    m "Да, все в порядке."
    img 2705
    reception "Ваши документы, Мэм?"
    img 2706
    m "Видите-ли..."
    "Мои документы тоже были в том чемодане, который должны привезти..."
    img 2707
    "И я... ээээ..."
    img 2708
    reception "Мэм."
    "Откуда был Ваш рейс?"
    img 2709
    m "Из Парижа."
    img 2710
    reception "Значит Вы проходили пограничный контроль?"
    img 2711
    m "Ээээ... ддда..."
    img 2712
    reception "А как Вы могли пройти его без документов, Мэм?"
    "Если они были в Вашем чемодане."
    img 2711
    m "..."
    img 2713
    "Да, вы правы."
    "Они были не в чемодане."
    "Я сказала вам так чтобы упростить ситуацию."
    "Они были в сумочке, которую я забыла в такси и..."
    img 2714
    with hpunch
    reception "Мэм, Вы приехали на такси?"
    img 2715
    m "Ну конечно на такси!"
    "А как же еще???"
    img 2716
    reception "Мэм."
    "У меня здесь камеры наблюдения."
    "Я видела как Вы подходили к отелю."
    "Вы шли пешком под дождем."
    img 2717
    with fade
    music Power_Bots_Loop
    m "..."
    mt "!!!!!!"
    img 2718
    reception "????"
    "Мэм?"
    "Вы точно приехали на такси?"
    "Вы говорите правду?"
    img 2719
    stop music fadeout 1.0
    m "Я..."
    "Я... Конечно...."
    img 2720
    music Pyro_Flow
    "Конечно я говорю правду!"
    "Как Вы смели сомневаться в этом!!!"
    "Жалкий сотрудник рецепшина!"
    "Какого-то задрипанного отеля!"
    img 2721
    music Groove2_85
    reception "Мэм."
    "Я знаю что Вы говорите неправду."
    "На моих камерах точно видно что Вы не приехали на такси."
    "Смею предположить что и все остальное что Вы говорили - это тоже неправда."
    "Я вынуждена отказать Вам в заселении."
    img 2722
    music Pyro_Flow
    m "ЧТО???"
    "АХ ТЫ МЕРЗКАЯ ТВАРЬ!!!"
    img 2724
    "Я УВОЛЮ ТЕБЯ!!!"
    "Я ТЕБЯ УНИЧТОЖУ!!!"
    img 2723
    "МЕЛКИЙ ПАРАЗИТ!!!"
    "НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    "ПАРАЗИТ!!!"
    img 2725
    music Groove2_85
    reception "..."
    "Мэм."
    "Знаете что."
    "Ваше поведение."
    "Ваши истории."
    "Мелкий уровень лжи, который легко обличается."
    "Вы непохожи на леди."

    img 2726
    "Вы больше похожи на шлюху."
    "Именно они, когда приходят, так себя ведут."
    if jailCageBlackmailMonicaSaidSheIsAWhore == True:
        img 5624
        w
        music prison_yell_music
        img black_screen
        with Dissolve(1)
        # хорошая шлюха
        img 5430
        with fade
        m "Я хорошая шлюха..."
        img 5432
        with fade
        prisoner1 "Громче! Мы не слышим!"
        m "Я хорошая шлюха!"
        img 5436
        with fadelong
        prisoner1 "Громче! Громко и ясно!"
        m "Я ХОРОШАЯ ШЛЮХА!!!"
        img black_screen
        with Dissolve(1)
        music Groove2_85
        img 5624
        with fade
        w

    img 2727
    with fadelong

    reception "А шлюхам у нас вход запрещен."
    img 2728
    reception "Единственное что меня смущает - это Ваше платье."
    img 2729
    "Оно дорогое, но неизвестно где Вы его взяли."
    img 2730
    music Pyro_Flow
    m "ЧТО???"
    "ДА КАК ТЫ СМЕЕШЬ ТАК СО МНОЙ РАЗГОВАРИВАТЬ!!!"
    "ПОЗОВИ СВОЕГО БОССА!!!"
    img 2731
    music Groove2_85
    reception "Мэм."
    "Сейчас в здании за старшую нахожусь я."
    "Я могу дать Вам телефон своего начальника и завтра Вы с ним свяжетесь."
    "Однако в заселении я Вам отказываю."
    img 2732
    music Pyro_Flow
    m "Я СЕЙЧАС ПОЗВОНЮ ТВОЕМУ БОССУ!!!"
    "Я РАЗБУЖУ ЕГО!!!"
    "МЕЛКОГО ЗАСРАНЦА!!!"
    "КОТОРЫЙ ДЕРЖИТ НА РАБОТЕ ТАКИХ НЕРАДИВЫХ СУЧЕК!"
    img 2733
    music Groove2_85
    reception "Мэм."
    "Мне неинтересно как меня оскорбляет какая-то шлюха."

    img 2734
    music Pyro_Flow
    m "ДАВАЙ НОМЕР!!!"
    "СЕЙЧАС ЖЕ!!!"
    "Я ПОКАЖУ ТЕБЕ КТО ИЗ НАС ШЛЮХА!!!"
    img 2735
    music Groove2_85
    reception "Мэм."
    "Пожалуйста."
    "Возьмите его визитку."
    img 2736
    music Pyro_Flow
    m "НУ ВСЕ!!!"
    "ДЕРЖИСЬ!!!"
    "Я ЗВОНЮ ЕМУ!!!"
    img 2737
    "..."
    "Сейчас!"
    "..."
    "Уже почти набираю!!!"
    img 2738
    music Power_Bots_Loop
    mt "ЧЕРТ!!!"
    "ГДЕ МОЙ ТЕЛЕФОН???"
    img 2739
    "ОН ОСТАЛСЯ В ПОЛИЦИИ!!!"
    "ДЬЯВОЛ!!!"
    img 2740
    music Pyro_Flow
    m "Давай телефон сюда!"
    "Быстро!"
    img 2741
    reception "Мэм."
    "Служебный телефон может использоваться только для рабочих звонков."
    img 2742
    m "!!!!!!"
    "..."
    img 2743
    "!!!!!!!!"
    "..."
    "..."
    img 2744
    m "Я уйду!"
    "И напишу жалобу!"
    img 2745
    "Ты пожалеешь об этом!"
    img 2746
    music Groove2_85
    reception "Мэм."
    "Всегда рады видеть Вас!"
    $ hotelVisited = True
    $ richHotelReceptionistMode = 2
    if dickSearch == True and homeVisited == True and hotelVisited == True:
        $ s2ClothShopStage = 1

    call refresh_scene_fade() from _call_refresh_scene_fade_95
    return

label after_jail_cloth_shop_street:
    mt "Этот магазин..."
    "Он работает допоздна."
    "Похоже он еще открыт."
    "Я не знаю куда мне деться."
    "Я уже вся промокла и замерзла!"
    "На улице уже мало людей и меня вот-вот оcтановит какой-нибудь патруль!"
    "Надо заглянуть туда..."

    return

label after_jail_cloth_shop_enter:
    music Groove2_85
    img 2758
    with fadelong
    mt "Да, он открыт!"
    "Но посетителей уже нет."
    img 2759
    mt "Магазин скоро закроется."
    img 2760
    "Как же здесь тепло и уютно!"
    "Раньше мне этот магазин казался дырой."
    img 2761
    "Но, учитывая что я пережила, мне он сейчас кажется просто раем!"
    "..."
    img 2762
    mt "Я заметила что продавец все еще здесь."
    img 2763
    "Нет!"
    "Я не уйду из этого мазаина!"
    "На улице так мерзко!"
    img 2764
    "..."
    "Мне надо что-то придумать!"
    "Может быть просто спрятаться от продавца, пока он не уйдет?"
    $ autorun_to_object("cloth_shop_dressing_room2", "after_jail_cloth_shop_cashier4")
    $ add_objective("hide_trader", t_("Прятаться от продавца, пока она не уйдет"), c_orange, 20)
    call refresh_scene_fade() from _call_refresh_scene_fade_96

    return

label after_jail_cloth_shop_cashier1:
    img 2765
    with fadelong
    w
    img 2766
    cashier "Надо навести порядок перед утренней сменой..."
    $ autorun_to_object("cloth_shop_view1_s2", "after_jail_cloth_shop_cashier2")
    call refresh_scene_fade() from _call_refresh_scene_fade_97
    return

label after_jail_cloth_shop_cashier2:
    mt "Туда идти опасно! Она меня заметит!"
    return

label after_jail_cloth_shop_cashier3:
    img 2649
    with fadelong
    mt "Туда идти опасно! Она меня заметит!"
    return

label after_jail_cloth_shop_cashier4:
    mt "Спрячусь здесь!"
    "Сюда она не должна зайти!"
    stop music fadeout 1.0
    call textonblack(t_("СПУСТЯ 15 МИНУТ...")) from _call_textonblack_15
    img black_screen
    with Dissolve(1)
    music Groove2_85
    img 2767
    cashier "Весь товар выглядит опрятно."
    "Пойду домой."
    $ autorun_to_object("cloth_shop_dressing_room2", "after_jail_cloth_shop_cashier5")
    call refresh_scene_fade() from _call_refresh_scene_fade_98
    return

label after_jail_cloth_shop_cashier5:
    mt "Да скоро же эта сучка уйдет!!!"
    mt "Долго мне прятаться???"
    $ autorun_to_object("cloth_shop_dressing_room", "after_jail_cloth_shop_cashier6")
    return

label after_jail_cloth_shop_cashier6:
    img 2768
    with fadelong
    mt "Ура!"
    "Она ушла!"
    "Теперь можно согреться и передохнуть."
    "Кажется я видела на прилавке шололадку."
    "Я заслужила ее!!!"
    $ remove_objective("hide_trader")
    $ add_objective("eat_chocolate", t_("Съесть шоколадку!"), c_pink, 20)
    $ s2ClothShopStage = 2
    $ clothShopCashierAtCashDesk = False
    $ autorun_to_object("cloth_shop_cashier", "after_jail_cloth_shop_cashier7")
    call refresh_scene_fade() from _call_refresh_scene_fade_99
    return

label after_jail_cloth_shop_cashier7:
    mt "Ага! Вот она!"
    "Шоколадка!"
    "Я заслужила ее!!!"
    return

label after_jail_cloth_shop_cashier8:
    img 2769
    with fadelong
    w
    img 2770
    w
    img 2771
    w
    sound snd_eat_crunch
    mt "Ммммм..."
    "Ням-ням."
    img 2772
    "Обычно я не ем шоколад, чтобы поддерживать фигуру."
    img 2773
    "Но сейчас я сделала исключение."
    "Я считаю что я заслужила это!"
    "..."
    img 2774
    "Теперь мне надо найти место где можно отдохнуть..."

    img black_screen
    with Dissolve(1)
    sound highheels_short_walk
    img 2775
    with fadelong
    mt "Этот диван слишком жесткий."
    "Когда я на него сажусь, мне в бок упираются пружины."
    img 2776
    "Старье!!!"
    "И как Дик мог меня сюда привести?"
    img 2777
    "Невежда!"
    "У него отсутствует вкус!"
    "Ничего не знает и не умеет кроме своих юридических бумажек."
    img 2778
    "Фи!"
    "..."
    "Надо поискать еще что-нибудь."
    img black_screen
    with Dissolve(1)
    sound highheels_short_walk
    img 2779
    with fadelong
    mt "С этого стула я упаду во сне."
    "Это точно!"
    img black_screen
    with Dissolve(1)
    sound highheels_short_walk
    img 2780
    with fadelong
    mt "Этот пуфик слишком маленький."
    "Я на него не помещаюсь."
    "Хотя я и худенькая."
    "..."
    "Для кого делают такие дурацие пуфики?"
    "Уж эта продавщица, корова! Точно на него не поместится!"
    "..."
    "Может посмотреть в примерочной?"
    $ remove_objective("eat_chocolate")
    $ add_objective("look_dressroom", t_("Может посмотреть в примерочной?"), c_blue, 20)
    $ s2ClothShopStage = 3
    call change_scene("cloth_shop_view1_s2", False, False) from _call_change_scene_187
    return

label after_jail_cloth_shop_cashier9:
    img 2781
    with fadelong
    mt "Тоже не очень..."
    music RnB4_100
    img 2782
    mt "Я не могу больше ничего искать."
    "Я столько искала за день!"
    "Избегала пол города вдоль и поперек!"
    "Я столько дней толком ни ела и не спала!"
    img 2783
    "Мне себя так жаль!"
    "Я бедняжка!"
    img 2784
    music Pyro_Flow
    "Но я обязательно решу все свои проблемы и отомщу всем!"
    "ВЫ СЛЫШИТЕ!!!"
    "Я ОТОМЩУ ВСЕМ ВАМ!!!"
    "И ЭТОЙ ПРОДАВЩИЦЕ, ОТ КОТОРОЙ МНЕ ПРИШЛОСЬ ПРЯТАТЬСЯ!"
    img 2785
    "МНЕ!!!"
    "Я!!!"
    "Моника Бакфетт!!!"
    "И мне прятаться от какой-то продавщицы!"
    img 2786
#    music RnB4_100
    "Лучше не буду об этом думать."
    "Когда я обо всем этом начинаю думать, то мои мысли постепенно приходят к Маркусу."
    music Power_Bots_Loop
    img 2787
    "И его словам."
    "Что меня ждет."
    "Тогда меня начинает охватывать ужас."
    img 2788
    "Все, Моника!"
    "Хватит!"
    "Я валюсь с ног."
    music I_Feel_You
    img 2789
    with fadelong
    "Пожалуй я устроюсь поудобнее."
    img 2790
    with fadelong
    "Вот так."
    img 2791
    with fadelong
    "Все, я сплю..."
    "Пфффффф...."
    "..."
    "...."
    "....."

    scene black_screen
    with Dissolve(1)
    call textonblack_long("УТРО") from _call_textonblack_long_2
    scene black_screen
    with Dissolve(1)
    $ changeDayTime("day")

    $ rain = True
    $ rainIntencity = 1
    $ lightning = False

    img 2792
    with fadelong
    music Power_Bots_Loop
    cashier "КТО ВЫ???"
    "ЧТО ВЫ ТУТ ДЕЛАЕТЕ???"
    "ВЫ ВОР???"
    "!!!"
    img 2793
    m "Я..."
    "Ээээ..."
    img 2794
    mt "Где я?"
    "Это магазин?"
    "Что я делаю здесь?"
    img 2795
    cashier "Я ЕЩЕ РАЗ СПРАШИВАЮ, ЧТО ВЫ ЗДЕСЬ ДЕЛАЕТЕ!!!"
    img 2796
    mt "Что я делаю в магазине?"
    "Где Юлия?"
    "..."
    img 2797
    music Groove2_85
    mt "О БОЖЕ!!!"
    "Я ВСЕ ВСПОМНИЛА!!!"
    "Я проспала!"
    "Мне надо было проснуться раньше и тихо уйти."
    "Но я так устала!"
    "У меня не было сил."
    "Я отключилась и проспала до утра."
    "Пришла продавец и нашла меня!"
    "Спящую в примерочной!"
    "Какой позор, Моника!"
    "Как же ты вляпалась во все это?"
    img 2798
    music Power_Bots_Loop
    cashier "Я ВЫЗЫВАЮ ПОЛИЦИЮ!"
    img 2799
    mt "Что?"
    "Полицию?"
    "О БОЖЕ!!!"
    "Мне нельзя в полицию!!!"
    "Что же делать?"
    "..."
    img 2800
    music Groove2_85
    mt "Так, Моника. Стоп."
    "Да, ты заснула в примерочной."
    "Но с тобой говорит какая-то жалкая продавец."
    "А ты девушка с обложки модного журнала."
    "В платье, которое стоит дороже, чем все что есть в этом магазине."

# clothShopCashierOffended2 = False #Общаться с продавцом грубо. при покупке
# clothShopCashierOffended3ReturnDress = False # возвращение платья
    if clothShopCashierOffended2 == True or clothShopCashierOffended3ReturnDress == True:
        "И какая-то мелюзга на меня смеет кричать???"
    else:
        "И на меня кричит продавец, к которому я отнеслась по человечески?"
        "Была добра к ней."

    label after_jail_cloth_shop_cashier9_menuloop1:
        menu:
            "Полиция придется как раз кстати! Ты, сучка!":
                $ clothShopCashierFirstNightOffended = True
                music Pyro_Flow;
                img 2801
                m "Кто вы?"
                img 2802
                cashier "Кто я?"
                "Я продавец в этом магазине!"
                "А кто вы?"
                "И что вы здесь делаете???"
                img 2803
                "Я вызываю полицию!"
                img 2804
                m "Вызывай!"
                "Давай!"
                "Попробуй!"
                "Полиция придется как раз кстати!"
                "Давай!"


                stop music fadeout 0.2
                sound highheels_run2
                img black_screen
                with fadelong
                $ renpy.pause(0.3)

                music Pyro_Flow
                img 2805
                with fadelong
                cashier "Почему вы на меня кричите?"
                img 2806
                m "Почему я кричу?"
                "Ты!!!"
                "Отвечай!"
                "Ты вчера работала???"
                img 2807
                cashier "Да, я. А что?"
                img 2808
                m "Отлично!"
                "Вызывай полицию."
                "Я напишу заявление!"
                img 2809
                cashier "Какое заявление?"
                img 2810
                m "Я вчера вечером пришла в этот чертов магазин, чтобы посмотреть себе гардероб."
                "Выбрала вещь."
                "Зашла в примерочную."
                "Потом мне видимо стало плохо."
                "И я потеряла сознание."
                img 2811
                "А ты!"
                "МЕЛКАЯ СУЧКА!!!"
                call bitch(5, "clothShopCashierFirstNightOffended") from _call_bitch_113

                stop music fadeout 0.2
                sound highheels_run2
                img black_screen
                with fadelong
                $ renpy.pause(0.3)
                music Pyro_Flow

                img 2812
                m "Ты!"
                "Сучка!"
                "Даже не заметила меня!"
                "И не оказала мне помощь!"
                "Не вызвала медиков!"
                img 2813
                "У тебя!"
                "В твоем магазине всю ночь пролежал человек!"
                "Без сознания!!!"
                "А если бы я умерла!!"
                img 2814
                cashier "Мэм."
                "Прошу прощения, я..."
                img 2815
                m "ЧТО? ТЫ???"
                "Если ты сейчас же не извинишься передо мной, мелкая тварь!"
                "То я засужу тебя с твоим магазином!"
                "Вы будете до конца дней платить по моим искам!"
                "Ясно тебе!!!"
                "Ты вообще знаешь кто я такая???"
                cashier "Мэм."
                "Я..."
                img 2816
                with fade
                m "Быстро извинилась передо мной!"
                img 2817
                cashier "Мэм."
                "Я извиняюсь перед Вами от своего имени и от имени магазина."
                "Впредь обещаю что мы будем более внимательными к посетителям."
                "И такой ситуации больше не повторится."
                img 2818
                "Пожалуйста, простите нас!"
                img 2819
                m "То-то же!"
                "Запомни мою доброту!"
                "Но учти!"
                "Что я прощаю только один раз!"
                "На второй моего великодушия точно не хватит!"
                img 2820
                cashier "Мэм."
                "Прошу прощения еще раз..."

            "В этом нет необходимости. Я всего-лишь клиент." if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False:
                $ clothShopCashierFirstNightOffended = False
                call bitch(-5, "clothShopCashierFirstNightOffended") from _call_bitch_114
                music Stealth_Groover
                #render+
                #Моника вежливо говорит с продавщицей в магазине с утра
                img 2801
                m "Кто вы?"
                img 2802
                cashier "Кто я?"
                "Я продавец в этом магазине!"
                "А кто вы?"
                "И что вы здесь делаете???"
                img 2803
                "Я вызываю полицию!"
                img 5638
                m "В этом нет необходимости."
                img 5639
                cashier "Почему?"
                img 5640
                m "Потому что я не вор."
                img 5641
                "Посмотрите на меня, Вы меня не узнаете?"
                img 5642
                cashier "Вы... кажется я Вас уже видела..."
                img 5643
                m "Да, я недавно посещала ваш магазин. С обстоятельным джентельменом."
                "Я ваш особый клиент!"
                img 5644
                cashier "Да, я помню, но Вы вернули платье..."
                m "Да, формальности, но зато я относилась к Вам вежливо, разве Вы не помните?"
                img 5645
                cashier "Да, Мэм."
                "Я помню. Спасибо за вежливость."
                "..."
                "Мэм, но что Вы здесь делаете?"
                img 5646
                m "Я пришла сюда примерить другое платье вчера."
                "Мне было жаль что я вернула вам то платье."
                "Меня немного терзало чувство вины и..."
                img 5647
                cashier "Спасибо, Мэм!"
                img 5648
                m "Да, и я, по всей видимости, потеряла сознание прямо в примерочной."
                "Не знаю как это случилось, но я очнулась прямо сейчас перед вами."
                "Наверное это из-за похудения."
                "У меня очень строгая диета, вы, наверное, понимаете меня..."
                img 5649
                cashier "Да, я понимаю Вас, Мэм!"
                "Я действительно не проверяла примерочную вчера перед уходом."
                img 5650
                "Это моя вина. Я должна была обнаружить вас!"
                "И оказать помощь!"
                img 5651
                "Простите меня!"
                img 5652
                m "Ничего страшного, я не в обиде на вас."
                "В следующий раз будьте внимательны."
                img 5653
                cashier "Да, Мэм! Конечно!"
                img 5654
                cashier "..."
                img 5655
                "Мэм... А Вы будете покупать другое платье, как хотели?"
                img 5656
                mt "Хм... Какое другое платье???"
                "Моника, у тебя сейчас другие проблемы!!!"
                "КАКОЕ К ЧЕРТУ ПЛАТЬЕ!!!"
                img 5657
                m "Хм... Видите-ли."
                "Я себя неважно чувствую."
                img 5658
                "У меня уже нет настроения для покупок."
                "Может быть в следующий раз."
                img 5659
                cashier "Конечно, Мэм!"
                "До свидания!"
                m "До свидания..."

            "В этом нет необходимости. Я всего-лишь клиент. (disabled)" if clothShopCashierOffended2 == True or clothShopCashierOffended3ReturnDress == True:
                jump after_jail_cloth_shop_cashier9_menuloop1

        img 2821
        with fadelong
        mt "Надо идти к Дику."
        "Надо быстрее закончить этот кошмар!"
        $ remove_objective("look_dressroom")
        $ remove_objective("find_sleep")
        $ add_objective("dick_search", t_("Идти к Дику в офис."), c_blue, 5)
        $ autorun_to_object("street_cloth_shop_s2", "afterJailDay2_clothShopStreet1")

        $ s2ClothShopStage = 4
        $ clothShopCashierTalkStage = 2
        $ clothShopCashierAtCashDesk = True
        $ gameSubStage = 1
        call change_scene("cloth_shop_view1_s2", "Fade", False) from _call_change_scene_188

#    scene black_screen
#    with Dissolve(1)
#    call textonblack_long("The End of V0.4\nYou could support me on Patreon if you like the game :)")
#    scene black_screen
#    with Dissolve(1)
#    $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
    return
