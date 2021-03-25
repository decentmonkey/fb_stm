label gallery_18659:
    # служебный коридор, Моника со служащим заходят, а там сидят все девочки эскорта
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 18603
    w
    imgf 18604
    w
    music Pyro_Flow
    img 18605
    mt "Какого черта?!"
    mt "?!?!?!"
    # брюнетка с каре злорадно
    music Groove2_85
    imgf 18606
    girl_1 "Ой, девочки, смотрите!"
    girl_1 "А вы говорили мне, что она не пойдет на это!"
    girl_1 "Я выиграла спор!"
    girl_1 "Хи-хи-хи!"
    # Линда насмешливо
    imgd 18607
    linda "Говорят, что она это ему уже делала здесь."
    linda "Еще и бесплатно..."
    # шатенка с хвостом с любобытством
    imgd 18608
    girl_3 "Правда?!"
    girl_3 "Ха-ха!"
    girl_3 "Я хочу посмотреть на это!"
    # девочки хихикают над Моникой, она зло на них смотрит
    music Power_Bots_Loop
    imgf 18609
    m "Что здесь происходит?!"
    m "Какого черта вы тут расселись?!"
    m "У вас что, закончились клиенты?!"
    m "!!!"
    # рыжая с короткой стрижкой, равнодушно
    music Groove2_85
    imgd 18610
    girl_2 "У нас технический перерыв."
    girl_2 "Еще целых 20 минут."
    girl_1 "Так что ты можешь поработать, а мы посмотрим." # брюнетка с каре, злорадно
    music Power_Bots_Loop
    imgd 18611
    m "Что?!"
    m "Я не собираюсь работать с клиентом при вас!"
    m "Что за бред?!"
    m "!!!"
    music Groove2_85
    imgd 18612
    linda "Боюсь, у тебя нет выбора..."

    # если была сцена с Линдой и инвестором
    if monicaEscortLindaTable1 == True:
        #
        $ notif(_("Моника назвала Линду проституткой-эскортницей."))
        #
        linda "Теперь посмотрим, кто из нас проститутка..."
        linda "Притом дешевая..."
    img 18613
    m "!!!"
    menu:
        "Пошли они все к черту!!! (прерывание квеста и увольнение с эскорта)":
            # Моника возмущенно
            label gallery_18623:
            music Power_Bots_Loop
            imgf 18614
            mt "Да они издеваются надо мной!"
            mt "!!!"
            # встает руки в боки
            music Pyro_Flow
            img 18615 hpunch
            m "Да вы хоть знаете, с кем разговариваете?!"
            m "Никчемные серые мыши!"
            m "Бесполезные и никому ненужные шлюшки!"
            m "!!!"
            # брюнетка с каре
            music Groove2_85
            imgd 18616
            girl_1 "Что ты сказала, стерва?!"
            girl_1 "Я пожалуюсь на тебя администратору!"
            girl_1 "Она вышвырнет тебя отсюда!"
            music Power_Bots_Loop
            imgd 18617
            m "И наконец-то!!!"
            sound vjuh2
            img 18618
            sound anger2
            m "Иди жалуйся, дрянь!"
            sound snd_bodyfall
            img 18619 vpunch
            w
            sound highheels_run2
            imgd 18620
            m "Не могу больше видеть вас всех!"
            m "Тупые сучки!"
            # Моника уходит, служащий растерянно ей вслед
            music Groove2_85
            imgf 18621
            hotel_staff "Но, Мэм! Мы же договорились!"
            # она зло на него смотрит
            music Power_Bots_Loop
            img 18622 hpunch
            m "Молчать!!!"
            m "Жалкое ничтожество!!!"
            imgd 18623
            m "Ненавижу вас всех!"
            m "!!!"
            return
        "Сказать служащему отеля, чтоб нашел другое место!":
            pass
    # Моника зло смотрит на девочек
    music Groove2_85
    imgf 18624
    hotel_staff "Мэм..."
    hotel_staff "У меня осталось совсем мало времени, Мэм..."
    imgd 18625
    m "Мы не можем пойти в другое место?!"
    mt "Кретин!"
    imgf 18626
    hotel_staff "Нет, Мэм..."
    hotel_staff "Сожалею, но больше уединиться негде."
    hotel_staff "Мэм... А если мы сделаем это в присутствии девочек?"
    hotel_staff "Мне было бы приятно, чтобы они поприсутствовали..."
    music Pyro_Flow
    imgd 18627
    m "Что ты такое несешь, халдей?"
    m "Что здесь приятного?!"
    music Groove2_85
    imgf 18628
    hotel_staff "Вы, Мэм, будете делать мне минет, а все девочки будут смотреть на мой член."
    hotel_staff "Меня одна мысль об этом возбуждает, Мэм..."
    m "Ты что, извращенец?!"
    # Линда перебивает их
    imgd 18629
    linda "Девочки, по-моему, она нарушает одно из важных правил нашего ВИП-эскорта."
    linda "Администратору будет интересно узнать, что она спорит с клиентом."
    linda "И отказывается выполнять его пожелания."
    # рыжая с короткой стрижкой, равнодушно
    imgf 18630
    girl_2 "Да, спорить с клиентом категорически нельзя."
    girl_2 "Администратор за это, в лучшем случае, штрафует."
    # Моника злая
    music Pyro_Flow
    imgd 18631
    m "Мог бы и не говорить об этом при всех!"
    m "Какой же ты придурок!"
    m "!!!"
    # любопытная шатенка с хвостом
    music Groove2_85
    imgf 18632
    girl_3 "Ой! Она еще и оскорбляет клиента!"
    girl_3 "Какой кошмар!!!"
    girl_3 "Это уже тянет на увольнение!"
    girl_3 "Да, девочки?!"
    # брюнетка с каре
    sound highheels_short_walk
    imgd 18633
    girl_1 "Да скорее бы ее уже вышвырнули отсюда!"
    girl_1 "Я сразу говорила, что нам эта шлюха не нужна в нашем ВИП-эскорте!"
    girl_1 "Корчит из себя знатную даму, а на самом деле дешевая проститутка!"
    girl_1 "Смотреть на нее противно!"
    menu:
        "Пошли они все к черту!!! (прерывание квеста и увольнение с эскорта)":
            # Моника возмущенно
            music Power_Bots_Loop
            imgf 18614
            mt "Да они издеваются надо мной!"
            mt "!!!"
            # встает руки в боки
            music Pyro_Flow
            img 18615 hpunch
            m "Это я дешевая проститутка?!"
            m "Да вы хоть знаете, с кем разговариваете?!"
            m "Никчемные серые мыши!"
            m "Бесполезные и никому ненужные шлюшки!"
            m "!!!"
            # брюнетка с каре
            music Groove2_85
            imgd 18616
            girl_1 "Что ты сказала, стерва?!"
            girl_1 "Я пожалуюсь на тебя администратору!"
            girl_1 "Она вышвырнет тебя отсюда!"
            music Power_Bots_Loop
            imgd 18617
            m "И наконец-то!!!"
            sound vjuh2
            img 18618
            sound anger2
            m "Иди жалуйся, дрянь!"
            sound snd_bodyfall
            img 18619 vpunch
            w
            sound highheels_run2
            imgd 18620
            m "Не могу больше видеть вас всех!"
            m "Тупые сучки!"
            # Моника уходит, служащий растерянно ей вслед
            music Groove2_85
            imgf 18621
            hotel_staff "Но, Мэм! Мы же договорились!"
            # она зло на него смотрит
            music Power_Bots_Loop
            img 18622 hpunch
            m "Молчать!!!"
            m "Жалкое ничтожество!!!"
            img 18623
            m "Ненавижу вас всех!"
            m "!!!"
            return
        "Сделать служащему отеля минет.":
            pass
    # Моника кипит от злости
    music Power_Bots_Loop
    imgf 18634
    mt "Что мне теперь делать?"
    mt "Неужели мне придется унижаться перед этими сучками?!"
    # служащий расстегивает ширинку
    music Groove2_85
    imgd 18635
    hotel_staff "Мэм, пожалуйста!"
    hotel_staff "!!!"
    img 18636
    mt "Фу!"
    mt "Смотреть на него не могу!"
    mt "Какой же он мерзкий!!!"
    mt "!!!"
    imgf 18637
    girl_1 "Ооо! Давай, сделай это!"
    hotel_staff "Вам нравится?"
    imgd 18638
    girl_1 "О, да!"
    girl_1 "Мы хотим посмотреть на это!"
    girl_1 "Давай, начинай!"
    music Power_Bots_Loop
    imgd 18639
    mt "Вот тварь!"
    mt "Она еще провоцирует этого неудачника!"
    mt "Сучка!"
    img 18640
    mt "Сейчас я сделаю это!"
    mt "Но с ней я потом разберусь отдельно!"
    mt "Эта мерзкая дрянь будет ползать у меня в ногах!"
    mt "!!!"
    # Моника зло поворачивается к служащему
    music Groove2_85
    imgf 18641
    m "Может, тебе достаточно будет подрочить перед этими сучками?!"
    m "?!?!?!"
    imgd 18642
    hotel_staff "Мэм, конечно, нет!"
    hotel_staff "Мне не терпится ввести его в Ваш ротик."
    music Pyro_Flow
    img 18643
    mt "АААААА!"
    mt "!!!"
    # Моника опускается перед ним на колени и злобно смотрит на него снизу вверх
    fadeblack 1.5
    music Groove2_85
    imgfl 18644
    w
    imgf 18645
    hotel_staff "Ооо, Мээээм..."
    hotel_staff "Откройте Ваш ротик..."
    menu:
        "Открыть рот.":
            pass
        "Пошли они все к черту!!! (прерывание квеста и увольнение с эскорта)":
            # Моника возмущенно
            imgd 18646
            mt "!!!"
            # встает руки в боки
            music Power_Bots_Loop
            imgf 18647
            m "Я, по-твоему, такая же дешевая проститутка, как они?!"
            m "Да ты хоть знаешь, с кем разговариваешь?!"
            m "Никчемное бесполезное животное!"
            m "!!!"
            # брюнетка с каре
            music Groove2_85
            imgd 18616
            girl_1 "Что ты сказала, стерва?!"
            girl_1 "Ты оскорбляешь своего клиента!"
            girl_1 "Я пожалуюсь на тебя администратору!"
            girl_1 "Она вышвырнет тебя отсюда!"
            music Power_Bots_Loop
            imgd 18617
            m "И наконец-то!!!"
            sound vjuh2
            img 18618
            sound anger2
            m "Иди жалуйся, дрянь!"
            sound snd_bodyfall
            img 18619 vpunch
            w
            sound highheels_run2
            imgd 18620
            m "Не могу больше видеть вас всех!"
            m "Тупые сучки!"
            # Моника уходит, служащий растерянно ей вслед
            music Groove2_85
            imgf 18621
            hotel_staff "Но, Мэм! Мы же договорились!"
            # она зло на него смотрит
            music Power_Bots_Loop
            img 18622 hpunch
            m "Молчать!!!"
            m "Жалкое ничтожество!!!"
            img 18623
            m "Ненавижу вас всех!"
            m "!!!"
            return
    # Моника со злобным лицом открывает рот
    # служащий вводит свой член в нее
    music Groove2_85
    imgd 18646
    w
    fadeblack
    sound hlup19
    pause 1.5
    music Loved_Up
    imgfl 18648
    hotel_staff "Оооо, как же охренительно!!!"
    hotel_staff "Какой удобный роооотик!!!"
    mt "!!!"
    imgf 18649
    hotel_staff "Мэм, потрогайте его своим язычком..."
    imgd 18650
    hotel_staff "Ах, да так..."
    imgd 18651
    hotel_staff "Еще-еще..."
    imgd 18652
    w
    imgd 18651
    w
    imgd 18650
    w
    imgd 18651
    w
    imgd 18652
    w
    imgd 18651
    w
    imgd 18650
    w
    hotel_staff "Мммм... Да..."
    # брюнетка вмешивается с комментами
    music Groove2_85
    imgf 18654
    girl_1 "Да насаживай уже ее голову на свой стояк!"
    girl_1 "Чего ты с ней возишься?!"
    girl_1 "Давай, амеба, покажи, что ты вообще мужчина!"
    mt "!!!"
    # служащий смотрит на брюнетку, потом на Монику
    imgd 18655
    w
    sound vjuh2
    img 18656 vpunch
    hotel_staff "ДАААА!!!"
    m "!!!"
    imgd 18657
    m "ХПФМММ!"
    imgd 18658
    m "ММПППХХХФФФФ!!!"
    menu:
        "Укусить его!!! (прерывание квеста и увольнение с эскорта)":
            music Pyro_Flow
            imgf 18675
            mt "Ублюдок!"
            mt "А что будет, если я укушу его мерзкий член?"
            # Моника поднимает взгляд на прибалдевшего служащего и сжимает челюсти на его члене
            sound hlup25
            imgd 18676
            m "!!!"
            sound Jump1
            imgd 18677
            w
            sound vjuh2
            img 18678
            w
            # он загибается
            sound scream_steve3
            img 18679 hpunch
            hotel_staff "АААААА!!!"
            imgd 18680
            hotel_staff "ОНА УКУСИЛА МЕНЯЯЯЯЯ!!!"
            sound scream_steve3
            hotel_staff "ААААААААААААА!!!"
            hotel_staff "СУЧКАААААА!!!"
            # девочки в шоке, вскакивают, подбегают к нему
            sound highheels_run2
            imgd 18681
            sound scream_steve3
            hotel_staff "ААААААААААААА!!!"
            # служащий убегает из служебного коридора с воплями
            sound snd_runaway
            imgf 18682
            sound scream_steve3
            hotel_staff "ААААААААААААА!!!"
            # смена кадра - ресепшн
            # он бежит мимо рецепции, админ на него смотрит в шоке
            fadeblack 1.5
            music Turbo_Tornado
            sound scream_steve3
            imgf 18687
            sound snd_runaway
            hotel_staff "ОНА УКУСИЛА МЕНЯЯЯЯЯ!!!"
            img 18688
            sound scream_steve3
            hotel_staff "АААААА!!!"
            hotel_staff "ААААААААААААА!!!"
            # убегает
            # смена кадра - служебный коридор
            # Моника со злобным видом смотрит вслед убежавшего служащего и вытирает рот
            # брюнетка с каре
            fadeblack 2.0
            music Groove2_85
            imgf 18683
            girl_1 "Ты что натворила, идиотка?!"
            girl_1 "Администратор вышвырнет тебя с этой работы!"
            music Power_Bots_Loop
            imgd 18684
            m "И наконец-то!!!"
            sound vjuh2
            img 18685
            sound anger2
            m "Не могу больше видеть вас всех!"
            img 18619 vpunch
            w
            sound highheels_run2
            imgd 18686
            m "Тупые сучки!"
            m "Ненавижу!"
            m "!!!"
            # Моника уходит
            return
        "Продолжить минет.":
            pass
    music Power_Bots_Loop
    imgf 18659
    mt "!!!"
    mt "Я убью эту мерзкую тварь!"
    # минет продолжается, служащий тащится и кончает
    fadeblack 1.5
    music2 Loved_Up2

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob3_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob3_1 = Movie(play="video/v_Monica_Helper_Blowjob3_1.mkv", fps=30)
    show videov_Monica_Helper_Blowjob3_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18660
    hotel_staff "Даааа!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob3_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob3_2 = Movie(play="video/v_Monica_Helper_Blowjob3_2.mkv", fps=30)
    show videov_Monica_Helper_Blowjob3_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18661
    hotel_staff "Оооох!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob3_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob3_3 = Movie(play="video/v_Monica_Helper_Blowjob3_3.mkv", fps=30)
    show videov_Monica_Helper_Blowjob3_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18662
    hotel_staff "Ооооо!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob3_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob3_4 = Movie(play="video/v_Monica_Helper_Blowjob3_4.mkv", fps=30)
    show videov_Monica_Helper_Blowjob3_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18663
    w
    imgd 18664
    mt "!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob3_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob3_5 = Movie(play="video/v_Monica_Helper_Blowjob3_5.mkv", fps=30)
    show videov_Monica_Helper_Blowjob3_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18665
    menu:
        "Кончить Монике в рот.":
            img 18666
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            hotel_staff "Аааа... Кончаю!"
            hotel_staff "Я хочу кончить в Ваш удобный ротик, Мэм!!"
            img 18667
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            hotel_staff "ИИИИИИИ!!!"
            img 18670
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            mt "!!!"
            imgf 18671
            w
            pass
        "Кончить Монике на лицо.":
            img 18666
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            hotel_staff "Аааа... Кончаю!"
            hotel_staff "Я хочу кончить на Ваше прекрасное личико, Мэм!!"
            img 18667
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            hotel_staff "ИИИИИИИ!!!"
            img 18668
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            mt "!!!"
            imgf 18669
            w
            pass
    # девочки все хихикают и аплодируют
    # Моника злая, служащий стоит довольный, штаны все еще расстегнуты
    sound applause1
    imgd 18672
    girl_1 "Да! Красавчик!"
    girl_2 "Молодец!"
    girl_3 "Ты сделал это!"
    linda "Хи-хи-хи!"
    music2 stop
    fadeblack 1.5
    music Power_Bots_Loop
    imgf 18673
    mt "Мерзкие сучки!"
    mt "Я им всем отомщу за это!"
    imgd 18674
    mt "И первой будет эта стерва!" # кадр на брюнетку с каре
    mt "Ненавижу!"
    return

label gallery_18757:
    # некоторое время спустя
    # Моника вдвоем с клиентом заходят в номер
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Некоторое время спустя..."))
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 18708
    client "Мисс [monica_hotel_name], я так мечтал повторить нашу с Вами встречу!"
    client "Никто из девочек вашего эскорта не доставлял мне такого удовольствия!"
    client "Только Вы, Мисс [monica_hotel_name]!"
    # Моника самодовольно улыбается
    imgf 18709
    sound highheels_short_walk
    mt "Хм, еще бы! Кто они и кто Я!"
    mt "Им всем не сравниться с такой шикарной женщиной, как Я!"
    # в номер заходит брюнетка
    # видит сначала только клиента и улыбается ему, флиртуя (Монику не замечает сразу)
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    sound2 highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 18710
    girl_1 "Мистер, извиняюсь за то, что Вам пришлось ждать."
    girl_1 "Администратор мне сказала, что Вы хотели встретиться именно со мной?"
    # Моника злорадно
    music Stealth_Groover
    imgf 18711
    m "Да, именно с тобой..."
    # брюнетка удивленно смотрит на нее
    img 18712 vpunch
    m "И со мной."
    music Groove2_85
    img 18713
    girl_1 "А ТЫ что здесь делаешь?!"
    girl_1 "Администратор сказала, что Я работаю с этим клиентом!"
    girl_1 "Иди отсюда!"
    imgf 18714
    m "Администратор говорит, что правило нашего ВИП-эскорта - выполнять все желания клиента."
    m "А Мистер сегодня хочет провести время с двумя девочками."
    music Hidden_Agenda
    imgd 18715
    m "Да, Мистер?" # обращается к клиенту
    # клиент похотливо смотрит на Монику
    client "Да, Мисс [monica_hotel_name]..."
    # снова обращается к брюнетке
    imgd 18716
    m "Или ты хочешь нарушить это правило?"
    m "В таком случае, я вынуждена рассказать все администратору..."
    # брюнетка зло смотрит на Монику
    music Groove2_85
    imgf 18717
    girl_1 "Ты это специально подстроила?"
    # Моника улыбается
    imgd 18718
    m "Так ты отказываешься работать?"
    # брюнетка бесится, но потом справляется с эмоциями
    img 18719
    girl_1 "Стерва!" # Монике
    # потом поворачивается к клиенту
    imgf 18720
    girl_1 "Конечно, нет..."
    girl_1 "Как я могу отказать такому... Такому красивому мужчине?"
    music Stealth_Groover
    imgd 18721
    mt "Боишься штрафа от администратора, сучка?"
    mt "Сейчас я покажу тебе, кто из нас дешевая шлюха, а кто Леди из высшего общества!"
    # Моника обращается к клиенту
    music Hidden_Agenda
    imgf 18722
    m "Мистер, вы хотите сделать также, как и в прошлый раз?"
    client "Да, Мисс [monica_hotel_name]!"
    client "Я мечтаю об этом!"
    imgd 18723
    m "Сегодня Мистера ожидает двойное удовольствие." # многообещающе улыбается ему
    imgd 18724
    client "Оооо, давайте быстрее начинать!"
    # затемнение, звук snd_fabric
    # Моника и брюнетка стоят полуголые перед клиентом
    # Моника в том же нижнем белье и в чулках
    # клиент голый, сидит на кровати
    # брюнетка зло шипит на Монику
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 18725
    w
    imgf 18726
    w
    imgd 18727
    girl_1 "Только попробуй сделать что-нибудь не так!"
    girl_1 "Я администратору про тебя такое расскажу, что ты вылетишь с этой работы!"
    music Stealth_Groover
    imgf 18728
    mt "Она вздумала пугать меня, Монику Бакфетт, каким-то администратором?"
    mt "Никчемная дешевая шлюшка!"
    imgd 18729
    m "Серьезно? Ты пытаешься угрожать мне?"
    m "Работа в эскорте - предел мечтаний такой, как ТЫ!"
    m "Тебе на лучшее не стоит даже надеяться..."
    m "В отличие от меня!"
    imgd 18730
    m "Можешь рассказывать администратору все, что хочешь."
    m "Мне все равно."
    m "Тем более, она поверит словам клиента, а не тебе."
    music Groove2_85
    img 18731
    girl_1 "ТЫ!" # бесится, но ее перебивает клиент
    imgf 18732
    client "Девочки, вы же не забыли про меня?"
    sound hlup10
    imgd 18733
    w
    sound hlup2
    imgd 18732
    w
    sound hlup10
    imgd 18733
    w
    sound hlup2
    imgd 18732
    w
    sound hlup10
    imgd 18733
    w
    sound hlup2
    imgd 18732
    w
    sound hlup10
    imgd 18733
    # ему не терпится
    # он дергает свой грустный член
    imgf 18734
    m "Конечно, не забыли, Мистер..."
    client "Мисс [monica_hotel_name]..."
    client "Сядете на кровать, как в прошлый раз?"
    menu:
        "Сесть на кровать":
            pass
    # брюнетка остается стоять возле кровати, Моника садится на кровать, а клиент на колени перед ее ногами
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    imgfl 18735
    client "Позвольте Вашу ножку, Мисс..."
    # Моника протягивает ему свою ногу, как в прошлый раз
    # клиент начинает облизывать ее
    imgf 18736
    w
    imgd 18737
    client "О, дааа..."
    imgd 18738
    client "Мисс, Вы великолепны!"
    imgd 18739
    client "Мммм..."
    imgd 18738
    w
    imgd 18739
    w
    imgd 18738
    w
    imgd 18739
    w
    imgd 18738
    w
    imgd 18739
    w
    imgf 18740
    client "Какие ножки!"
    # брюнетка стоит и удивленно наблюдает за тем, как у клиента встает
    # Моника высокомерно и со злорадством на нее смотрит
    imgd 18741
    w
    sound Jump1
    imgd 18742
    w
    img 18743 hpunch
    w
    music Stealth_Groover
    imgf 18744
    mt "Удивлена, дрянь?"
    mt "Ни у одной сучки из эскорта не получалось возбудить клиента!"
    mt "А мне для этого достаточно позволить ему целовать мою ножку!"
    # клиент отрывается от ноги Моники и обращается к брюнетке
    music Groove2_85
    imgd 18745
    client "Смотри, какой он твердый!" # гордый собой
    client "Я хочу, чтобы ты поработала своей рукой."
    client "Иди сюда!"
    # брюнетка зло смотрит на Монику, потом подходит к клиенту, садится рядом и игриво ему
    imgd 18746
    w
    sound highheels_short_walk
    imgf 18747
    girl_1 "Ммм, он и правда очень твердый..."
    imgd 18748
    client "Тебе нравится?"
    girl_1 "Да..."
    girl_1 "Что бы Мистер хотел, чтобы я сделала?"
    # клиент смотрит на ногу Моники и не глядя на брюнетку говорит
    imgf 18749
    client "Просто продолжай работать рукой."
    # он снова принимается за ногу Моники
    music Loved_Up
    music2 drkanje5
    imgd 18750
    w
    imgd 18751
    w
    imgd 18752
    w
    imgd 18751
    w
    imgd 18750
    w
    imgd 18751
    w
    imgd 18752
    w
    imgd 18751
    w
    music stop
    music2 stop
    fadeblack 1.5
    music2 Loved_Up

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Petting1.ogg"
    scene black
    image videov_Monica_Visitor3_EscortCustomer1_Escort6_Petting1_1 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Petting1_1.mkv", fps=30)
    show videov_Monica_Visitor3_EscortCustomer1_Escort6_Petting1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18753
    w
    imgd 18754
    client "Какие у Мисс прекрасные ножки!"
    imgf 18755
    w
    imgd 18756
    client "Мммм..."
    imgf 18757
    w
    # Моника высокомерно смотрит на брюнетку, та работает рукой и злобно поглядывает на Монику
    music2 Stealth_Groover
    imgd 18758
    mt "Завидуешь, сучка?"
    mt "Тебе нужно работать рукой..."
    mt "А мне даже не нужно прикасаться к этому неудачнику..."
    mt "Такой шикарной женщине, как Я, достаточно ему позволить целовать мои ноги."

    music2 Loved_Up
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Petting1.ogg"
    scene black
    image videov_Monica_Visitor3_EscortCustomer1_Escort6_Petting1_2 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Petting1_2.mkv", fps=30)
    show videov_Monica_Visitor3_EscortCustomer1_Escort6_Petting1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 stop
    fadeblack 1.5
    # клиент отрывается от ног Моники и говорит брюнетке
    music Groove2_85
    imgf 18759
    client "Мисс... А Вы говорили про секс..."
    imgd 18760
    mt "Что этот извращенец задумал?"
    music Stealth_Groover
    imgf 18761
    m "Да, говорила..."
    m "Но я не имела ввиду себя."
    imgd 18762
    m "Можешь воспользоваться ею." # указывает на брюнетку
    img 18763 vpunch
    girl_1 "Чтоо?!"
    # клиент обращает внимание на брюнетку
    music Groove2_85
    imgd 18764
    client "Хватит!"
    client "Раздевайся!"
    # та встает и снимает белье
    sound snd_fabric1
    imgf 18765
    client "Мисс [monica_hotel_name]..." # Монике
    # указывая на снимающую трусики брюнетку
    client "Вы же не запретите мне целовать Ваши ножки, пока я буду ею пользоваться?"
    imgd 18766
    mt "Хмм..."
    menu:
        "Я вам позволяю, Мистер.":
            pass
        "Нет, я не хочу!":
            music Pyro_Flow
            imgf 16818
            mt "Фу! Нет!"
            mt "Я не собираюсь терпеть все эти грязные извращенства из-за какой-то мерзкой сучки!"
            mt "Она не стоит таких жертв с моей стороны!"
#            $ questHelp("escort_8", False)
            # высокомерно говорит клиенту
            music Stealth_Groover
            imgd 16819
            m "Нет!"
            m "На сегодня достаточно!"
            m "Мне нужно идти."
            imgd 18768
            m "А она останется с вами, Мистер." # указывает на брюнетку
            m "Можете делать с ней все, что захотите."
            # клиент расстроенно
            client "Да, Мисс [monica_hotel_name]... Как скажете..."
            imgf 18769
            mt "Он даже не пытается уговорить меня остаться?"
            mt "Никчемный неудачник!"
            mt "Бесполезный!"
            mt "Фи!"
            # Моника уходит
            return
    music Stealth_Groover
    imgf 18767
    mt "Он хочет ее использовать?"
    mt "Как какую-то вещь..."
    mt "Хи-хи!"
    # затемнение
    # Моника сидит на тумбочке у кровати
    # голая брюнетка сидит на кровати
    # клиент стоит у кровати и рассматривает брюнетку
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 18770
    client "Я не хотел бы использовать ее киску, Мисс..."
    imgf 18771
    mt "И?"
    mt "Эта серая мышь что, совсем его не возбуждает?"
    imgd 18772
    client "Если Мисс [monica_hotel_name] мне позволит, то..."
    client "Я использовал бы зад этой эскортницы..." # указывает на попу брюнетки
    menu:
        "Я вам позволяю, Мистер.":
            pass
    imgf 18773
    m "Хорошая идея, Мистер."
    m "Я позволяю!"
    # брюнетка пытается что-то возразить
    girl_1 "Я не..."
    # Моника ее перебивает
    music Stealth_Groover
    img 18774
    m "Ты пытаешься перечить клиенту?"
    m "Или мне показалось?" # угрожающе
    # брюнетка зло шипит ей
    music Groove2_85
    imgd 18775
    girl_1 "Тебе показалось!"
    girl_1 "Стерва!"
    # клиент нетерпеливо
    imgf 18776
    client "Ложись на живот!"
    client "Подставляй скорее мне свой зад!"
    # затемнение
    # голый клиент лежит на кровати сверху на брюнетке, Моника также сидит у кровати
    # у него сразу не получается войти в ее попу, т.к. у него член немного загрустил
    fadeblack 2.0
    music Groove2_85
    imgfl 18777
    w
    imgf 18778
    client "Так..."
    client "Черт!"
    client "Сейчас..."
    # поднимает взгляд на Монику
    imgd 18779
    client "Мисс [monica_hotel_name]..."
    client "Мой член снова упал..."
    client "Я хочу еще раз поцеловать Вашу ножку."
    imgf 18780
    client "Иначе у меня ничего не получится."
    client "Вы же не против, Мисс?"
    imgd 18781
    m "Конечно, Мистер..." # снисходительно
    # протягивает ему ногу
    # он снова облизывает пальчики Моники, к нему возвращается стояк
    fadeblack 1.5
    music2 Loved_Up
    imgf 18782
    client "Ммммм..."
    imgd 18783
    client "Он твердеет!"
    client "Даааа..."
    client "Мисс, смотрите, какой он твердый!"
    # потом отстраняется, тыкается несколько раз в брюнетку и наконец входит в нее (анальный секс)
    sound hlup19
    img 18784 hpunch
    girl_1 "Ай!"
    client "Оооооо!!!"
    girl_1 "Аааа!!"
    # клиент снова тянется ртом к ноге Моники, берет в рот ее пальчики
    imgf 18785
    client "Ммммм!!"
    # сосет их и в одновременно шпилит брюнетку, накрывая ее своим жиром

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_1 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_1.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18786
    girl_1 "Черт! Мне тяжело!"
    girl_1 "Ай!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_2 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_2.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_3 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_3.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18787
    client "Какая Вы великолепная, Мииииисс [monica_hotel_name]!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_4 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_4.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18788
    client "Как же хорошооооо!"
    client "Оооо... Мисс..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_5 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_5.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 stop
    fadeblack 1.5
    music Groove2_85
    imgf 18789
    client "Мисс [monica_hotel_name]..."
    client "Я хотел бы, что бы эта эскортница тоже попробовала..."
    client "Вы же позволите, Мисс?"
    imgd 18790
    mt "Что попробовала?"
    mt "Хм, этот извращенец что, хочет и ее ноги облизывать?"
    mt "Я планировала немного не так..."
    mt "..."
    menu:
        "Да, Мистер.":
            pass
        "Нет, я не хочу!":
            music Pyro_Flow
            imgf 18791
            mt "Фу! Нет!"
            mt "Я не собираюсь терпеть все эти грязные извращенства из-за какой-то мерзкой сучки!"
            mt "Она не стоит таких жертв с моей стороны!"
            # высокомерно говорит клиенту
            music Stealth_Groover
            imgd 18792
            m "Нет!"
            m "На сегодня достаточно!"
            m "Мне нужно идти."
            imgd 18793
            m "А она останется с вами, Мистер." # указывает на брюнетку
            m "Можете делать с ней все, что захотите."
            # клиент расстроенно
            music Groove2_85
            imgf 18794
            client "Да, Мисс [monica_hotel_name]... Как скажете..."
            music Stealth_Groover
            imgd 18795
            mt "Он даже не пытается уговорить меня остаться?"
            mt "Никчемный неудачник!"
            mt "Бесполезный!"
            mt "Фи!"
            # Моника уходит
            return
    music Stealth_Groover
    imgf 18796
    mt "С другой стороны, Моника, твоя ножка его уже возбудила."
    mt "И эта сучка от этого бесится."
    mt "Хи-хи!"
#    imgd 18797
    imgd 18789
    m "Да, Мистер. Пусть она тоже попробует."
#    if questHelpFlag12 == False:
#        $ questHelpFlag12 = True
#        $ questHelp("escort_13", skipIfExists=True)
#        $ questHelpDesc("escort_desc2", "escort_desc4")
    # клиент говорит брюнетке
    music Groove2_85
    imgf 18798
    client "Поцелуй эту прекрасную ножку."
    client "Я хочу посмотреть на это!"
    client "Это так возбуждает!"
    client "Мисс [monica_hotel_name] такая сексуальная!"
    # брюнетка в молчаливой ярости смотрит на Монику
    # Моника удивлена предложением клиента и ей оно нравится
#    img 18799
    music Stealth_Groover
    imgd 18796
    mt "?!"
    mt "Этот неудачник придумал отличную идею!"
    mt "Хи-хи!"
    fadeblack 1.5
    music Stealth_Groover
    # Моника говорит брюнетке
    imgfl 18797
    w
    imgf 18799
    w
    imgd 18800
    m "Ну? Чего ты ждешь?"
    music Groove2_85
    img 18801
    girl_1 "!!!"
    girl_1 "!!!!!!"
    # брюнетка в ярости
    # Моника протягивает ей ногу, брюнетка медлит
    girl_1 "Мистер, может быть..."
    girl_1 "Хотите, я поцелую вашу ногу?"
    # Моника ее перебивает
    music Stealth_Groover
    imgd 18802
    m "Ты слышала, чего желает клиент?"
    m "Это твоя работа!"
    m "Выполняй!"
    # клиент нетерпеливо
    music Groove2_85
    imgf 18803
    client "Целуй ножку Мисс [monica_hotel_name]!"
    client "Я хочу увидеть это!"
    # брюнетка приближает лицо к ноге Моники
    # брезгливо прикасается к ней губами
    music Loved_Up
    imgd 18804
    client "Не так!"
    client "Поработай своим язычком!"
    # брюнетка проводит языком по ступне Моники
    imgf 18805
    w
    imgd 18806
    client "Даааа..."
    imgd 18805
    w
    imgd 18806
    w
    imgd 18805
    w
    imgd 18806
    w
    imgf 18807
    client "Теперь возьми ее пальчик себе в ротик!"
    client "А теперь соси его!"
    # брюнетка выполняет
    # клиент взглядом маньяка смотрит вблизи на это
    # анальный секс, брюнетка сосет пальцы Моники
    fadeblack 1.5
    music2 Loved_Up
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_1 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_1.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18808
    client "Оооо..."
    client "Соси!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_2 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_2.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_3 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_3.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18809
    client "Вот так, дааа..."
    client "Облизывай ее пальчики еще!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.3333333) + " loop 0.0>Sounds/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2.ogg"
    scene black
    image videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_4 = Movie(play="video/v_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_4.mkv", fps=30)
    show videov_Monicav_Monica_Visitor3_EscortCustomer1_Escort6_Sex2_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 stop
    fadeblack 1.5
    music Groove2_85
    imgd 18810
    client "Скажи, они великолепны, да?"
    # брюнетка отстраняется от ноги и зло смотрит на Монику
    img 18811
    girl_1 "!!!"
    imgf 18812
    m "Клиент задал тебе вопрос..."
    m "Скажи нам, тебе нравится целовать мои ножки?"
    # клиент возбужденно
    imgd 18813
    client "Да-да, скажи это!"
    girl_1 "Нравится!!!" # с яростью
    # брюнетка бросает на Монику яростные взгляды, Моника смотрит на нее и торжествует
    music Stealth_Groover
    imgf 18814
    mt "Ну что, мерзкая сучка, нравится тебе?"
    mt "Мне целуют ноги, а тобой просто пользуются!"
    mt "Потому что ты - никто, а я - Королева!"
    mt "Теперь ты знаешь свое место, ничтожная шлюшка!"
    mt "!!!"
    music Loved_Up2
    imgd 18815
    client "Оооо!!! Я сейчас!!!"
    client "Еще чуть-чуууууть!!!"
    # клиент кончает
    menu:
        "Кончить внутрь девочки с эскорта.":
            img 18816
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            client "Аааа..."
            client "Ааааа!!!"
            img 18817
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan9
            client "ДАААААА!!!"
            pass
        "Кончить на попу девочки с эскорта.":
            img 18816
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            client "Аааа..."
            client "Ааааа!!!"
            img 18818
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan9
            client "ДАААААА!!!"
            sound hlup25
            imgd 18819
            w
            pass
        "Кончить на ножку Моники.":
            imgd 18816
            client "Аааа..."
            client "Я сейчас кончу, Мииисс!"
            imgf 18820
            client "Позвольте Вашу ножку!!!"
            client "О, быстрее! Быстрее!"
            # Моника протягивает ногу
            img 18821
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            client "Ааааа!!!"
            client "ДАААААА!!!"
            # кончает на ступню Моники
            img 18822
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan9
            mt "Мог бы не пачкать мою ножку!"
            mt "Какая гадость!"
            mt "Фууу!"
            mt "!!!"
            menu:
                "Заставить сучку с эскорта слизать сперму клиента.":
                    label gallery_18828:
                    music Hidden_Agenda
                    imgf 18823
                    mt "Хммм..."
                    imgd 18825
                    m "Я думаю, что Мистеру будет приятно посмотреть на то..."
                    m "Как она слижет это с моей ножки..."
                    music Groove2_85
                    imgf 18826
                    client "О, Мисс [monica_hotel_name]!"
                    client "Да-да! Очень хочу посмотреть на это!"
                    # смотрит на брюнетку
                    imgd 18827
                    client "Слышишь?"
                    client "Оближи ее ножку!"
                    client "Видишь, я ее испачкал?"
                    girl_1 "Мистер хочет, чтобы я..."
                    music Stealth_Groover
                    img 18799
                    m "Да!"
                    m "И это желание клиента!"
                    m "Давай, работай!"
                    # брюнетка зло выполняет, клиент смотрит вблизи и балдеет
                    imgf 18835
                    w
                    fadeblack 1.5
                    music Loved_Up2
                    imgf 18828
                    girl_1 "!!!"
                    client "Еще вот здесь лизни."
                    imgd 18829
                    client "Да, так!"
                    client "И здесь..."
                    client "Ооооо!"
                    pass
                "Не делать этого.":
                    music Stealth_Groover
                    imgf 18824
                    mt "Нет!"
                    mt "Не хочу, чтобы она снова ко мне прикасалась своим противным ртом!"
                    mt "Фи!"
                    pass
            pass
    # затемнение
    # все трое стоят в номере одетые
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 18830
    client "Мисс [monica_hotel_name], Вы самая лучшая девочка здесь!"
    client "Я буду очень надеятся еще на одну встречу с Вами!"
    # Моника улыбается ему и злорадно смотрит на брюнетку
    imgf 18831
    client "Вот Ваши деньги, Мисс."
    client "Это был восхитительный вечер!"
    # отдает деньги Монике ($ 800-?)
    # клиент уходит, брюнетка возмущенно ему вслед
    sound man_steps
    imgd 18832
    w
    imgf 18833
    girl_1 "Сучка!"
    girl_1 "Я тебе этого просто так не оставлю!"
    # Моника лишь злорадно хихикает в ответ и уходит
    music Stealth_Groover
    imgd 18834
    m "Хи-хи-хи!!"
    return

label gallery_19717:
    # у лифта стоит Линда
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19712
    w
    imgf 19713
    linda "Олаф, дорогой!"
    linda "Какой приятный сюрприз!"
    if monicaHotelAdminAgreement3 == True:
        # Моника зло смотрит на Линду
        music Power_Bots_Loop
        imgd 19714
        mt "А эта сучка что здесь вынюхивает?!"
        mt "Ненавижу ее!"
    # она видит Олафа и радостно ему улыбается
    music Groove2_85
    imgd 19715
    linda "Я так рада, что ты все-таки решил прийти ко мне сегодня!"
    # подходит к нему и хочет его обнять
    # Моника вопросительно смотрит на Олафа
    imgf 19716
    mt "Он что, постоянный клиент здесь?!"
    mt "?!?!?!"
    # Олаф резко отстраняется, стесняясь при Монике
    sound Jump2
    img 19717 hpunch
    olaf "Ты что, сошла с ума?!"
    # Линда в растерянности останавливается
    imgf 19718
    linda "Но Олаф..."
    imgd 19719
    olaf "Отойди от меня! Ты меня позоришь!"
    # Линда офигевшая смотрит на Монику и на Олафа
    # Олаф заходит в лифт
    fadeblack
    sound man_steps
    pause 2.0
    if monicaHotelAdminAgreement3 == True:
        music Pyro_Flow
        imgfl 19720
        w
        imgf 19721
        linda "Решила забрать себе моего клиента, стерва?!"
        linda "Ты за это поплатишься!"
        linda "Я заставлю тебя вылизывать мою киску на глазах у всех девочек, дрянь!"
        # Моника смотрит на нее надменно
        imgd 19722
        m "Еще чего!"
        m "Иди в жопу, Линда!"
        sound highheels_short_walk
        imgf 19723
        w
        fadeblack
    sound snd_lift
    pause 2.0
    return

label gallery_19887:
    # Моника с Олафом заходят в номер
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19885
    olaf "Проходите, Миссис Бакфетт."
    olaf "Извините за этот инцидент у лифта."
    # Моника с гордым видом идет к столику и садится на диванчик
    imgf 19886
    w
    sound highheels_short_walk
    imgd 19887
    w
    fadeblack 2.0
    music Stealth_Groover
    imgfl 19888
    m "Кто эта девушка у лифта?"
    m "Вы ее знаете?"
    music Groove2_85
    imgf 19889
    olaf "Эта девушка, меня, должно быть с кем-то перепутала."
    olaf "Не обращайте внимания, Миссис Бакфетт."
    imgd 19890
    olaf "Могу я предложить Вам вина?"
    imgf 19891
    m "Да, пожалуй я не откажусь от бокала хорошего вина..."
    m "Вы составите мне компанию, Олаф?"
    imgd 19892
    olaf "Нет, Миссис Бакфетт. Я не буду пить вино, но с удовольствием угощу Вас."
    olaf "Какое вино Вы предпочитаете?"
    # Моника задумчиво
    music Hidden_Agenda
    imgf 19893
    mt "Хммм... Моника, тебе на руку, что у этого никчемного неудачника проблемы с алкоголем..."
    mt "Пусть закажет дорогое вино..."
    mt "Я не буду его пить..."
    mt "Сдам назад, получив за него деньги."
    mt "Это гениальная идея, Моника!"
    imgd 19894
    m "Олаф, я предпочитаю пить только первоклассные вина."
    m "Поэтому к любому вину, дешевле $ 5 000 за бутылку, я даже не стану притрагиваться..."
    # Олаф нажимает кнопку коммуникатора (или звонит по телефону на ресепшн)
    fadeblack 1.5
    sound snd_phone1
    pause 2.0
    music Groove2_85
    imgfl 19895
    olaf "Здравствуйте."
    olaf "У вас имеется вино Domaine de la Romanee-Conti, Montrachet Grand 2007 года?"
    olaf "..."
    imgf 19896
    olaf "Хорошо. Принесите его в номер 618, пожалуйста."
    olaf "..."
    olaf "Спасибо. Жду."
    # Олаф садится на стул недалеко от Моники, смотрит на нее, пуская слюни, но не решаясь на большее
    fadeblack 2.0
    music Groove2_85
    imgfl 19897
    olaf "Я заказал для Вас, Миссис Бакфетт, самое восхитительное вино, которое я когда-либо пробовал."
    olaf "Я уверен, Вы оцените этот божественный вкус по достоинству."
    olaf "Самой лучшей женщине нашего города только все самое лучшее!"
    # наклоняется к ней, она протягивает надменно руку, он ее целует
    music Stealth_Groover
    imgf 19898
    m "..."
    imgd 19899
    mt "Этот жалкий подкаблучник готов исполнять любой мой каприз..."
    mt "Нужно будет получить его согласие на инвестицию и заканчивать этот цирк."
    mt "И мне плевать, что там Биф обещал ему!"
    imgd 19900
    mt "Он перечислит свои деньги в мой журнал и мне для этого не придется делать никаких грязный извращений!"
    mt "Я Миссис Моника Бакфетт, а не какая-то проститутка!"
    mt "Я могу убедить его, используя свой навык деловых переговоров."
    mt "Ведь я не только самая красивая, но и самая умная женщина в этом городе! Вернее, в стране!"
    # стук в дверь
    sound snd_door_knock
    imgf 19901
    olaf "О, вот и Ваше вино, Миссис Бакфетт!"
    # Олаф сидит, держа руку Моники в своей руке после поцелуя, и говорит в сторону двери
    olaf "Войдите!"
    # Если Моника работает в эскорте
    if monicaHotelAdminAgreement3 == True:
        # заходит администратор
        fadeblack
        sound highheels_short_walk
        pause 2.0
        music Groove2_85
        imgfl 19902
        reception "Я прощу меня извинить, Мистер..."
        reception "У меня небольшая просьба к Вашей спутнице..."
        reception "Если Вы позволите, я поговорю с ней буквально пару минут?"
        # Олаф недовольно
        imgf 19903
        olaf "Какая это еще может быть просьба?!"
        imgd 19904
        mt "Черт!"
        mt "Гребаная администраторша!"
        # Моника спокойно говорит
        imgf 19905
        m "Одну секунду, Олаф. Я сейчас вернусь..."
        # Моника встает с дивана и идет к выоду из номера, Олаф смотрит ей вслед, на попу
    # затемнение
    return

label gallery_19948:
    # Олаф сидит, держа руку Моники в своей руке после поцелуя
    # в номер заходит Линда
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19919
    linda "Ваше вино..."
    olaf "Хорошо. Поставьте бутыку на столик."
    # если Моника не работает и не работала в эскорте
    if monicaHotelAdminAgreement3 == False:
        # Линда недовольно смотрит на Монику и Олафа, потом на их руки
        imgf 19920
        w
        sound snd_plates1
        imgd 19927
        w
        imgf 19921
        linda "Пожалуйста, Мистер..."
        linda "Приятного вечера." # говорит Олафу ехидно
        olaf "Спасибо. Вы можете идти."
        # Линда бросает еще один недовольный взгляд на Монику и уходит
        imgd 19922
        w
        imgd 19923
        mt "Почему эта никчемная официантка так на меня смотрит?!"
        mt "Отвратительное обслуживание!"
    # Если работает, приход Линды в номер
    if monicaHotelAdminAgreement3 == True:
        # Линда подходит с бутылкой вина (подносом) к столику
        imgf 19920
        sound snd_plates1
        w
        imgd 19927
        w
        imgf 19925
        w
        if ep212_escort_monica_fired == True:
            #
            $ notif(_("Моника больше не работает в ВИП-эскорте."))
            #
            music Stealth_Groover
            imgd 19923
            mt "!!!"
            mt "Она мне завидует, что у меня свидание с ее знакомым?!"
            mt "Ну и пусть завидует..."
            mt "Это удел таких проституток, как она - обслуживать клиентов!"
            imgd 19924
            mt "А такая шикарная леди, как Я, пьет дорогое вино и наслаждается вниманием мужчины..."
            mt "Который все для меня готов сделать!"
        else:
            music Stealth_Groover
            imgd 19923
            mt "Какого черта эта сучка так на меня смотрит?!"
            mt "Дешевая проститука-эскортница! Фи!"
            mt "!!!"
            mt "Она мне завидует, что у меня свидание с ее знакомым?!"
            mt "Да, точно. Завидует!"
            imgd 19924
            mt "Ну и пусть..."
            mt "Это удел таких проституток, как она - обслуживать клиентов!"
            mt "А такая шикарная леди, как Я, отдыхает, пьет дорогое вино и наслаждается вниманием мужчины..."
            mt "Который все для меня готов сделать!"
        # ставит вино и поворачивается к Олафу, требовательно
        label gallery_40141:
        fadeblack 1.5
        music Groove2_85
        img 19926 vpunch
        linda "Олаф! Я думала ты меня любишь!"
        linda "Что ты здесь делаешь с этой шлюхой?!"
        linda "Как ты мог променять меня на такую стерву, как она?!"
        linda "Я думала, у нас с тобой искренние и светлые чувства!!!"
        # Олаф в шоке, вскакивает со своего места и подбегает к Линде
        sound Jump2
        img 19928 vpunch
        olaf "ТИШЕ!"
        olaf "Молчи!!"
        # Моника высокомерно наблюдает за происходящим
        # Линда возмущенно
        imgf 19929
        linda "С какой стати я должна молчать?!"
        linda "Ведь она же просто..."
        # Олаф перебивает ее и шипит угрожающе
        img 19930 vpunch
        olaf "Тише!!!"
        # с опаской смотрит на Монику, потом снова на Линду, шепчет ей
        sound Jump1
        imgd 19931
        w
        imgf 19932
        olaf "Не подставляй меня!"
        olaf "Это не то, что ты думаешь!"
        olaf "Я здесь по важному делу!"
        imgd 19933
        linda "По какому еще делу?!"
        linda "Что у тебя может быть общего с этой..."
        imgd 19934
        olaf "Молчи, я сказал!"
        linda "Но Олаф!"
        # Олаф ей шепчет
        imgf 19935
        olaf "Линда, я дам тебе $ 1 000 прямо сейчас, если ты замолчишь и уйдешь отсюда сейчас же!"
        linda "$ 1 000?!"
        olaf "Да!"
        # отдает ей деньги
        music Pyro_Flow
        img 19936 vpunch
        mt "$ 1 000?!"
        mt "Этой сучке?!"
        mt "?!?!?!"
        menu:
            "Отыграться на Линде. (Extra version) (disabled)" if game.extra == False:
                pass
            "Отыграться на Линде." if game.extra == True:
                imgf 19937
                mt "С какой стати?!"
                mt "Он ей дает такие деньги просто для того, чтобы она ушла?!"
                mt "!!!"
                mt "!!!!!!"
                mt "И это после того, как эта дрянь угрожала мне у лифта..."
                mt "Что она заставит меня делать на глазах у остальных сучек всякие гадости?!"
                imgd 19938
                mt "Вот стерва!!!"
                mt "!!!"
                mt "Я ей этого просто так не оставлю!"
                mt "Пусть знает свое место!"
                mt "!!!"
                # Моника зло
                img 19941 vpunch
                m "Олаф!"
                # Олаф испуганно
                olaf "Да?"
                m "Постойте!"
                # Моника встает с дивана и подходит к Олафу и Линде
                fadeblack
                sound highheels_short_walk
                pause 2.0
                music Stealth_Groover
                imgfl 40103
                mt "Ну сучка, сейчас ты у меня попляшешь!"
                # Моника встает руки в боки и с наездом говорит Олафу
                imgf 40104
                m "Итак, Олаф, вы решили пригласить меня сюда!"
                m "Сюда, где встречаетесь с какими-то шлюхами?!"
                m "Вы посмели сделать это?!"
                m "!!!"
                # Олаф в шоке
                imgd 40105
                olaf "Миссис Бак..."
                m "ТИХО!!"
                m "Не смей произносить мое имя в присутствии этой падшей женщины!"
                # Линда хочет возмутиться, но Олаф ее перебивает и шепчет ей
                music Groove2_85
                imgf 40106
                linda "Да как?!..."
                imgd 40107
                olaf "Тихо, молчи!"
                olaf "Я прошу тебя, не говори ничего!"
                olaf "Я сделаю для тебя все, что хочешь... Потом..."
                olaf "А сейчас молчи!"
                # Линда слушается, замолкает и просто молча злобно смотрит на Монику
                # Моника продолжает устраивать Олафу разнос
                music Stealth_Groover
                imgf 40108
                m "Посмотри, кто она и кто Я!"
                m "Она - какая-то дешевая проститука!"
                m "Я с подобными особами ни разу в жизни даже не встречалась!"
                m "Не говоря уже о том, чтобы делить с ними внимание мужчины!"
                imgd 40109
                m "Как вы могли меня поставить в такое ужасное и унизительное положение, Олаф?!"
                m "МЕНЯ!!!"
                m "Эта падшая женщина недостойна даже того, чтобы..."
                if monicaEscortLindaTable1 == True:
                    imgd 40110
                    m "Чтобы быть чем-то незаметным в помещении, где я нахожусь!"
                    #
                    $ notif(_("Моника работала реквизитом Линды, когда Линда была в номере с другим инвестором."))
                    #
                    imgd 40110
                    m "Каким-нибудь предметом интерьера!"
                    m "Столиком, например!"
                    m "!!!"
                else:
                    imgd 40110
                    m "Чтобы даже находиться в одном помещении со мной!!!"
                    m "!!!"
                # Олаф крайне напуган
            #    music Groove2_85
                imgf 40111
                olaf "Миссис Ба..."
                m "Кажется, я запрещала упоминать мое имя!"
                olaf "Да, простите..."
                olaf "Позвольте, я заглажу свою вину..."
                imgd 40112
                m "Я позволю!"
                m "Только на своих условиях!"
                olaf "Я все сделаю..."
                imgf 40113
                olaf "Только не расстраивайтесь, прошу Вас!..."
                # Моника злобно на них смотрит, потом разворачивается и направляется к кровати
                # садится на нее
                sound highheels_short_walk
                imgd 40114
                m "Вы оба!"
                m "Идите сюда!"
                # Олаф шепчет Линде
                fadeblack
                sound highheels_short_walk
                pause 1.5
                music Groove2_85
                imgf 40115
                olaf "Линда, милая, я прошу тебя..."
                olaf "Не спорь с ней и делай все, что она скажет."
                linda "Но Олаф!"
                linda "Как эта стерва себе позволяет с тобой обращаться?!"
                imgd 40116
                olaf "Линда, тише! Прошу тебя!"
                olaf "Это очень важно для меня!"
                imgf 40117
                linda "А я здесь причем?"
                linda "Я не собираюсь выслуживаться перед этой сучкой!"
                sound Jump2
                img 40118 vpunch
                olaf "Линда..."
                olaf "Ты... Ты не представляешь, какие проблемы мне угрожают!"
                olaf "В таком случае, я... У меня..."
                olaf "Я больше не буду оплачивать твои апартаменты!"
                imgd 40119
                linda "Олаф, ну что ты сразу начинаешь?"
                linda "Причем здесь это?"
                imgf 40120
                olaf "Либо ты делаешь все, что она скажет..."
                olaf "Либо я больше ни цента не внесу за твои апартаменты!"
                imgd 40121
                linda "Ну хорошо... Я сделаю, как ты говоришь, дорогой."
                linda "Но я готова терпеть это только ради тебя!"
                imgd 40122
                olaf "Все. Пойдем."
                olaf "И не вздумай спорить с ней! Вообще, молчи!"
                # Олаф и Линда подходят к кровати
                fadeblack
                sound highheels_short_walk
                pause 2.0
                music Stealth_Groover
                imgfl 40123
                m "Олаф, вы мне сегодня говорили, что я самая красивая женщина в вашей жизни."
                m "Это действительно так, Олаф?"
                olaf "Да, конечно, Миссис Ба... Кхм... Мэм..."
                imgf 40124
                mt "Этот Олаф настолько жалок..."
                mt "Он готов сделать все, что я прикажу."
                mt "Подкаблучник!"
                mt "Сейчас я с помощью этого неудачника поставлю сучку Линду на место!"
                mt "Ну держись, дрянь!"
                m "Олаф..."
                m "Кто красивее, я или она?"
                imgd 40125
                olaf "Конечно Вы, Мэм!"
                # Линда злобно смотрит на нее, потом на Олафа
                # Моника ехидно усмехается, глядя на Линду
                imgf 40126
                m "Раздевайся, падшая женщина!"
                music Groove2_85
                linda "Что?!"
                # Олаф снова шепчет Линде
                imgd 40127
                olaf "Тише!"
                olaf "Делай, что она говорит!"
                olaf "Иначе я буду вынужден исполнить то, о чем мы говорили несколько минут назад."
                linda "Но Олаф!"
                olaf "Делай что говорит тебе Мэм!"
                imgf 40128
                w
                fadeblack
                sound snd_fabric1
                pause 2.0
                music Groove2_85
                # Линда снова бросает испепеляющий взгляд на Монику
                # затемнение, шуршание одежды
                # кадр, ноги Линды и ее платье на полу
                # Линда стоит перед Моникой обнаженная
                # Моника издевательски смотрит на нее
                imgfl 40129
                w
                imgf 40130
                w
                imgd 40131
                m "Олаф!"
                olaf "Да, Мэм?"
                music Stealth_Groover
                imgf 40132
                m "Мне не нравится, как эта особа на меня смотрит..."
                m "Я хочу, чтобы она извинилась передо мной за свое строптивое поведение."
                olaf "Конечно, Мэм!"
                # протягивает свою руку, затянутую в перчатку
                imgd 40133
                m "Целуй!"
                # Линда зло смотрит на нее
                # Олаф снова ей шепчет
                music Groove2_85
                imgf 40134
                olaf "Давай выполняй!"
                olaf "Мы с тобой договорились, помнишь?"
                # Линда наклоняется и целует руку Моники, зло на нее поглядывая
                imgd 40136
                w
                sound snd_kiss2
                imgd 40135
                w
                music Stealth_Groover
                imgf 40137
                m "Думаю, этого недостаточно..."
                m "Пусть она просит прощения, целуя мои ноги!"
                # Линда в шоке
                img 40138 vpunch
                linda "Что?!"
                linda "Ты!.. Да как ты!.."
                m "Олаф, эта особа снова демонстрирует свое непослушание!"
                # Линда смотрит на Олафа
                imgd 40139
                olaf "Линда!"
                olaf "Не спорь с Мэм!"
                linda "!!!"
                imgd 40140
                mt "Эта сучка думала, что отделается, поцеловав мою руку?"
                mt "После того, что она сказала мне у лифта?!"
                mt "Жалкая дешевая проститутка!"
                mt "Сейчас ты заплатишь за каждое свое слово, дрянь!"
                # Линда опускается на колени и целует каблук Моники
                # Моника надменно смотрит на нее, потом наклоняется к ней и шепчет
                imgf 40197
                m "Целуй!"
                linda "..."
                olaf "Линда, делай, как говорит Мэм!"

                imgd 40196
                linda "!!!"

                imgf 40142
                w
                sound snd_kiss2
                imgd 40141
                w
                sound snd_kiss2
                imgf 40198
                m "Помнишь, сучка, что ты мне сегодня сказала у лифта?"

                sound Jump1
                imgd 40143
                # Линда смотрит на Монику с ненавистью и молчит
                linda "!!!"
                m "Спасибо за идею, шлюшка..."
                # Моника распрямляется и говорит Олафу
                imgf 40144
                m "Олаф, раздевайтесь!"
                m "Покажите мне, как вы изменяете своей жене с этой проституткой..."
                olaf "Но, Мэм..."
                olaf "Я не..."
                imgd 40145
                m "Не стоить пытаться меня обманывать, Олаф."
                m "И я не советую вам спорить со МНОЙ!"
                imgd 40146
                olaf "Мэм, у меня на этот вечер были другие планы..."
                imgf 40147
                m "Позвольте, я угадаю. Вы планировали заняться со мной своими грязными извращениями?!"
                olaf "Мэм... Кхм... Я..."
                m "Выбор этого отеля - ваша большая ошибка, Олаф."
                m "И чтобы я вас простила, вам придется постараться."
                olaf "Да, Мэм..."
                # затемнение, шуршание одежды
                # Линда стоит голая и Олаф тоже голый, эрекции у него нет, смотрит виновато на Монику
                imgd 40148
                mt "Пусть теперь сучка Линда почуствует себя моим реквизитом!"
                mt "В следующий раз будет знать, как плести интриги со своей мерзкой подружкой-шлюшкой против МЕНЯ!"
                mt "!!!"
                mt "Я - Моника Бакфетт! А она - никто. Пустое место."
                fadeblack
                sound snd_fabric1
                pause 2.0
                music Groove2_85
                imgfl 40149
                m "Можете приступать, Олаф."
                m "Я жду."
                olaf "Но, Миссис Ба... Мэм..."
                olaf "Есть небольшая проблема..."
                # смотрит на свой грустный член
                imgf 40150
                m "Что, эта падшая невзрачная особа..."
                m "Которая продает свое тело за деньги разным мужчинам..."
                m "Совсем вас не возбуждает, Олаф?"
                # Олаф виновато смотрит на Линду
                imgd 40151
                olaf "Нет, Мэм..."
                music Stealth_Groover
                imgf 40152
                m "Конечно, она не сравнится со мной."
                imgd 40153
                m "Но вам сегодня повезло, Олаф..."
                m "Я сегодня в хорошем настроении, поэтому..."
                m "Так уж и быть... Я продемонстрирую вам, Олаф, что есть истинная женская красота."
                # затемнение, шуршание одежды
                # Моника сидит на кровати с надменным видом обнаженная, в одних перчатках и каблуках
                fadeblack
                sound snd_fabric1
                pause 2.0
                music Loved_Up
                imgfl 40154
                w
                # Моника ехидно смотрит на Линду, та на нее - с ненавистью
                imgf 40155
                olaf "О, Мэм!"
                olaf "Вы восхитительны, Мэм!"

                imgd 40156
                linda "!!!"

                music Stealth_Groover
                imgf 40157
                m "Я знаю, Олаф, о чем вы мечтали сегодня весь вечер."
                m "Пока угощали меня ужином в ресторане и сыпали комплиментами..."
                # насмешливый взгляд на Линду
                imgd 40158
                m "Но поскольку эта особа осмелилась нарушить наши с вами планы..."
                m "Я разрешу смотреть вам на меня..."
                m "Пока она будет извиняться передо мной за свое неповиновение."
                imgf 40159
                olaf "О, Миссис Бак... Мэм!"
                # Моника раздвигает ноги и приказывает Линде
                sound Jump2
                imgd 40160
                m "А ты чего ждешь, падшая женщина?"
                m "Приступай. Я разрешаю тебе поцеловать мою киску."
                # Линда в шоке, смотрит на Монику, потом на Олафа
                # Олаф прситально смотрит ан голую Монику, на Линду ноль эмоций
                # член у него встает
                # тот ей снова шепчет
                music stop
                sound plastinka1b
                img 40156 hpunch
                linda "!!!"
                music Loved_Up
                imgf 40161
                w
                imgd 40162
                w
                imgf 40163
                w
                sound Jump1
                imgd 40164
                w
                music Groove2_85
                imgf 40165
                linda "Олаф! Я не буду этого делать!"
                olaf "Линда! Помнишь то дело, с которым ты пришла ко мне за помощью?"
                linda "Это здесь совсем ни при чем!"
                olaf "Это мне решать! И я не смогу помочь тебе, если ты откажешь сейчас!"
                imgd 40166
                linda "Нет! Ты не посмеешь! Ты же обещал мне!"
                linda "Ты же знаешь, как это важно для меня!"
                imgf 40167
                olaf "Знаю..."
                olaf "И я сдержу свое обещание, если ты сделаешь, как приказывает Мэм."
                olaf "Делай, что тебе говорят!"
                imgd 40168
                linda "!!!"
                # взгляд Моники полон высокомерия и насмешки над Линдой
                # та вынуждена послушаться и снова опускается на колени перед Моникой
                # взгляд полон ненависти, но деньги Линда любит больше
                # Линда начинает лизать киску Моники, Моника на нее насмешливо смотрит
                music Stealth_Groover
                imgf 40169
                mt "Ну что, сучка?"
                mt "Теперь ты поняла, что ты по сравнению со мной - никто!"
                mt "Жалкая дешевка с непомерно завышенной самооценкой!"
                mt "Никому не нужная и ничего из себя не представляющая!"
                mt "Знай свое место, шлюшка!"
                mt "!!!"
                # Моника смотрит на Олафа
                fadeblack 2.0
                music2 Loved_Up
                imgfl 40170
                w
                imgf 40171
                m "Я позволяю тебе поцеловать мою киску..."
                m "Приступай..."

                imgd 40172
                linda "Стерва!"
                linda "!!!"

                imgf 40199
                w
                imgd 40173
                w
                imgf 40174
                w

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Licking1_1 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_1.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Licking1_1
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Licking1_2 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_2.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Licking1_2
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                sound lick3
                imgd 40175
                w
                sound lick3
                imgd 40174
                w
                sound lick3
                imgd 40175
                w
                sound lick3
                imgd 40174
                w
                sound lick3
                imgd 40175
                w
                sound lick3
                imgd 40174
                w
                sound lick3
                imgd 40175
                w

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Licking1_3 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_3.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Licking1_3
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Licking1_4 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_4.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Licking1_4
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                imgf 40176
                m "А вам, Олаф, я разрешаю воспользоваться телом этой проститутки."
                olaf "Мэм..."
                m "И не разрешаю спорить со мной..."
                # Олаф пристраивается сзади Линды и входит в нее
                # Моника говорит Линде
                fadeblack 1.5
                music2 Loved_up2
                img 40177 hpunch
                sound chpok3
                w
                imgfl 40178
                m "А тебе никто не позволял останавливаться!"
                m "Продолжай!"
                imgf 40179
                linda "!!!"

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_1 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_1.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_1
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_2 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_2.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_2
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                # сам смотрит на Монику и на то, как Линда лижет ее киску
                imgd 40180
                olaf "Оооо, Мэм..."
                m "Олаф, вы представляете, что ваш член сейчас внутри меня?"
                imgf 40181
                olaf "Даа, Мэээм..."
                olaf "Аааа..."

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_3 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_3.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_3
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                imgd 40182
                olaf "Как я мечтаю попробовать вашу киску, Мэм!!!"
                olaf "Ммммм..."

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_4 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_4.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_4
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                imgf 40183
                olaf "Киску самой Миссис...!!!"
                m "Олаф, молчать!"
                imgd 40184
                olaf "О, дааа..."
                olaf "О, Мэээээм!!!"

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_5 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_5.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_5
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")


                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_6 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_6.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_6
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_7 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_7.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_7
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                scene black
                image videov_Visitor2_Monica_Investor2_Sex1_8 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_8.mkv", fps=30)
                show videov_Visitor2_Monica_Investor2_Sex1_8
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")


                imgd 40185
                olaf "Оооо!"
                olaf "Я сейчас кончу!!!"
                menu:
                    "Кончить внутрь Линды.":
                        img 40186
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        olaf "Аааа..."
                        olaf "АААА!!"
                        img 40187
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        sound man_moan3
                        olaf "ААААААА!!!!"
                        imgf 40189
                        w
                        pass
                    "Кончить на киску Линды.":
                        img 40186
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        olaf "Аааа..."
                        olaf "АААА!!"
                        img 40188
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        sound man_moan3
                        olaf "ААААААА!!!!"
                        imgf 40190
                        w
                        pass
                # Олаф отстраняется от Линды, а она отстраняется от Моники
                # Моника злорадно на нее смотрит
                # Линда шипит ей, пока Олаф не слышит
                music2 stop
                fadeblack 2.0
                music Stealth_Groover
                imgfl 40191
                m "Ты свободна на сегодня."
                m "Мистер более не нуждается в услугах проститутки."
                imgf 40192
                linda "Сука!"
                imgd 40193
                m "Продажная шкура!"
                imgd 40194
                linda "Я тебе этого просто так не оставлю!"
                return
            "Забрать у Линды часть денег.":
                imgd 19937
                mt "С какой стати?!"
                mt "Он ей дает такие деньги просто для того, чтобы она ушла?!"
                mt "!!!"
                mt "!!!!!!"
                # Линда говорит Олафу
                music Groove2_85
                imgf 19939
                linda "Нууу..."
                linda "Хорошо!"
                imgd 19940
                olaf "Все!"
                olaf "Иди!"
                # Моника надменно его перебивает
                imgd 19941
                m "Олаф, подождите..."
                # Олаф испуганно смотрит на Монику, Линда со злостью
                fadeblack
                sound highheels_short_walk
                pause 1.5
                music Stealth_Groover
                imgfl 19947
                m "Олаф, эта девочка, видимо, что-то перепутала..."
                m "Можно я кое-что скажу ей?"
                # Олаф испуганно отвечает
                olaf "Да, конечно!"
                # Моника с Линдой отходят в другую сторону номеру, к кровати
                # Моника шепчет ей
                sound highheels_short_walk
                imgf 19948
                w
                music Groove2_85
                imgd 19949
                m "Если ты действительно хочешь заработать денег..."
                m "То с этой тысячи ты мне отдашь $ 500."
                # Линда шипит
                imgd 19950
                linda "С какой стати я отдам их тебе?!"
                linda "Это мои деньги!"
                # Моника отвечает угрожающе
                imgf 19951
                m "Ты отдашь их мне!"
                m "Иначе тебе будет хуже!"
                # Линда зло на нее смотрит, потом смотрит на Олафа
                imgd 19952
                linda "Ну ладно..."
                linda "Это МОЙ клиент, а обслуживаешь его ты..."
                linda "Я отдам тебе деньги."
                linda "Но только внизу после того, как ты закончишь трахаться с ним."
                imgd 19953
                m "!!!"
                menu:
                    "Отыграться на Линде. (Extra version) (disabled)" if game.extra == False:
                        pass
                    "Отыграться на Линде." if game.extra == True:
                        music Pyro_Flow
                        imgf 19954
                        mt "Эта сучка что, пытается сейчас обмануть меня?!"
                        mt "Меня?! Монику бакфетт?!"
                        mt "Ах ты, дрянь!"
                        mt "!!!"
                        # Моника злобно смотрит на Линду
                        imgd 19956
                        m "Отдашь деньги внизу, говоришь?"
                        linda "Да." # с улыбочкой
                        # Моника возвращается к Олафу и зовет Линду подойти
                        sound highheels_short_walk
                        imgf 19959
                        m "Иди сюда!"
                        fadeblack
                        sound highheels_short_walk
                        pause 2.0
                        music Stealth_Groover
                        imgfl 40103
                        mt "Ну сучка, сейчас ты у меня попляшешь!"
                        # Моника встает руки в боки и с наездом говорит Олафу
                        imgf 40104
                        m "Итак, Олаф, вы решили пригласить меня сюда!"
                        m "Сюда, где встречаетесь с какими-то шлюхами?!"
                        m "Вы посмели сделать это?!"
                        m "!!!"
                        # Олаф в шоке
                        imgd 40105
                        olaf "Миссис Бак..."
                        m "ТИХО!!"
                        m "Не смей произносить мое имя в присутствии этой падшей женщины!"
                        # Линда хочет возмутиться, но Олаф ее перебивает и шепчет ей
                        music Groove2_85
                        imgf 40106
                        linda "Да как?!..."
                        imgd 40107
                        olaf "Тихо, молчи!"
                        olaf "Я прошу тебя, не говори ничего!"
                        olaf "Я сделаю для тебя все, что хочешь... Потом..."
                        olaf "А сейчас молчи!"
                        # Линда слушается, замолкает и просто молча злобно смотрит на Монику
                        # Моника продолжает устраивать Олафу разнос
                        music Stealth_Groover
                        imgf 40108
                        m "Посмотри, кто она и кто Я!"
                        m "Она - какая-то дешевая проститука!"
                        m "Я с подобными особами ни разу в жизни даже не встречалась!"
                        m "Не говоря уже о том, чтобы делить с ними внимание мужчины!"
                        imgd 40109
                        m "Как вы могли меня поставить в такое ужасное и унизительное положение, Олаф?!"
                        m "МЕНЯ!!!"
                        m "Эта падшая женщина недостойна даже того, чтобы..."
                        if monicaEscortLindaTable1 == True:
                            imgd 40110
                            m "Чтобы быть чем-то незаметным в помещении, где я нахожусь!"
                            #
                            $ notif(_("Моника работала реквизитом Линды, когда Линда была в номере с другим инвестором."))
                            #
                            imgd 40110
                            m "Каким-нибудь предметом интерьера!"
                            m "Столиком, например!"
                            m "!!!"
                        else:
                            imgd 40110
                            m "Чтобы даже находиться в одном помещении со мной!!!"
                            m "!!!"
                        # Олаф крайне напуган
                    #    music Groove2_85
                        imgf 40111
                        olaf "Миссис Ба..."
                        m "Кажется, я запрещала упоминать мое имя!"
                        olaf "Да, простите..."
                        olaf "Позвольте, я заглажу свою вину..."
                        imgd 40112
                        m "Я позволю!"
                        m "Только на своих условиях!"
                        olaf "Я все сделаю..."
                        imgf 40113
                        olaf "Только не расстраивайтесь, прошу Вас!..."
                        # Моника злобно на них смотрит, потом разворачивается и направляется к кровати
                        # садится на нее
                        sound highheels_short_walk
                        imgd 40114
                        m "Вы оба!"
                        m "Идите сюда!"
                        # Олаф шепчет Линде
                        fadeblack
                        sound highheels_short_walk
                        pause 1.5
                        music Groove2_85
                        imgf 40115
                        olaf "Линда, милая, я прошу тебя..."
                        olaf "Не спорь с ней и делай все, что она скажет."
                        linda "Но Олаф!"
                        linda "Как эта стерва себе позволяет с тобой обращаться?!"
                        imgd 40116
                        olaf "Линда, тише! Прошу тебя!"
                        olaf "Это очень важно для меня!"
                        imgf 40117
                        linda "А я здесь причем?"
                        linda "Я не собираюсь выслуживаться перед этой сучкой!"
                        sound Jump2
                        img 40118 vpunch
                        olaf "Линда..."
                        olaf "Ты... Ты не представляешь, какие проблемы мне угрожают!"
                        olaf "В таком случае, я... У меня..."
                        olaf "Я больше не буду оплачивать твои апартаменты!"
                        imgd 40119
                        linda "Олаф, ну что ты сразу начинаешь?"
                        linda "Причем здесь это?"
                        imgf 40120
                        olaf "Либо ты делаешь все, что она скажет..."
                        olaf "Либо я больше ни цента не внесу за твои апартаменты!"
                        imgd 40121
                        linda "Ну хорошо... Я сделаю, как ты говоришь, дорогой."
                        linda "Но я готова терпеть это только ради тебя!"
                        imgd 40122
                        olaf "Все. Пойдем."
                        olaf "И не вздумай спорить с ней! Вообще, молчи!"
                        # Олаф и Линда подходят к кровати
                        fadeblack
                        sound highheels_short_walk
                        pause 2.0
                        music Stealth_Groover
                        imgfl 40123
                        m "Олаф, вы мне сегодня говорили, что я самая красивая женщина в вашей жизни."
                        m "Это действительно так, Олаф?"
                        olaf "Да, конечно, Миссис Ба... Кхм... Мэм..."
                        imgf 40124
                        mt "Этот Олаф настолько жалок..."
                        mt "Он готов сделать все, что я прикажу."
                        mt "Подкаблучник!"
                        mt "Сейчас я с помощью этого неудачника поставлю сучку Линду на место!"
                        mt "Ну держись, дрянь!"
                        m "Олаф..."
                        m "Кто красивее, я или она?"
                        imgd 40125
                        olaf "Конечно Вы, Мэм!"
                        # Линда злобно смотрит на нее, потом на Олафа
                        # Моника ехидно усмехается, глядя на Линду
                        imgf 40126
                        m "Раздевайся, падшая женщина!"
                        music Groove2_85
                        linda "Что?!"
                        # Олаф снова шепчет Линде
                        imgd 40127
                        olaf "Тише!"
                        olaf "Делай, что она говорит!"
                        olaf "Иначе я буду вынужден исполнить то, о чем мы говорили несколько минут назад."
                        linda "Но Олаф!"
                        olaf "Делай что говорит тебе Мэм!"
                        imgf 40128
                        w
                        fadeblack
                        sound snd_fabric1
                        pause 2.0
                        music Groove2_85
                        # Линда снова бросает испепеляющий взгляд на Монику
                        # затемнение, шуршание одежды
                        # кадр, ноги Линды и ее платье на полу
                        # Линда стоит перед Моникой обнаженная
                        # Моника издевательски смотрит на нее
                        imgfl 40129
                        w
                        imgf 40130
                        w
                        imgd 40131
                        m "Олаф!"
                        olaf "Да, Мэм?"
                        music Stealth_Groover
                        imgf 40132
                        m "Мне не нравится, как эта особа на меня смотрит..."
                        m "Я хочу, чтобы она извинилась передо мной за свое строптивое поведение."
                        olaf "Конечно, Мэм!"
                        # протягивает свою руку, затянутую в перчатку
                        imgd 40133
                        m "Целуй!"
                        # Линда зло смотрит на нее
                        # Олаф снова ей шепчет
                        music Groove2_85
                        imgf 40134
                        olaf "Давай выполняй!"
                        olaf "Мы с тобой договорились, помнишь?"
                        # Линда наклоняется и целует руку Моники, зло на нее поглядывая
                        imgd 40136
                        w
                        sound snd_kiss2
                        imgd 40135
                        w
                        music Stealth_Groover
                        imgf 40137
                        m "Думаю, этого недостаточно..."
                        m "Пусть она просит прощения, целуя мои ноги!"
                        # Линда в шоке
                        img 40138 vpunch
                        linda "Что?!"
                        linda "Ты!.. Да как ты!.."
                        m "Олаф, эта особа снова демонстрирует свое непослушание!"
                        # Линда смотрит на Олафа
                        imgd 40139
                        olaf "Линда!"
                        olaf "Не спорь с Мэм!"
                        linda "!!!"
                        imgd 40140
                        mt "Эта сучка думала, что отделается, поцеловав мою руку?"
                        mt "После того, что она сказала мне у лифта?!"
                        mt "Жалкая дешевая проститутка!"
                        mt "Сейчас ты заплатишь за каждое свое слово, дрянь!"
                        # Линда опускается на колени и целует каблук Моники
                        # Моника надменно смотрит на нее, потом наклоняется к ней и шепчет
                        imgf 40197
                        m "Целуй!"
                        linda "..."
                        olaf "Линда, делай, как говорит Мэм!"

                        imgd 40196
                        linda "!!!"

                        imgf 40142
                        w
                        sound snd_kiss2
                        imgd 40141
                        w
                        sound snd_kiss2
                        imgf 40198
                        m "Помнишь, сучка, что ты мне сегодня сказала у лифта?"

                        sound Jump1
                        imgd 40143
                        # Линда смотрит на Монику с ненавистью и молчит
                        linda "!!!"
                        m "Спасибо за идею, шлюшка..."
                        # Моника распрямляется и говорит Олафу
                        imgf 40144
                        m "Олаф, раздевайтесь!"
                        m "Покажите мне, как вы изменяете своей жене с этой проституткой..."
                        olaf "Но, Мэм..."
                        olaf "Я не..."
                        imgd 40145
                        m "Не стоить пытаться меня обманывать, Олаф."
                        m "И я не советую вам спорить со МНОЙ!"
                        imgd 40146
                        olaf "Мэм, у меня на этот вечер были другие планы..."
                        imgf 40147
                        m "Позвольте, я угадаю. Вы планировали заняться со мной своими грязными извращениями?!"
                        olaf "Мэм... Кхм... Я..."
                        m "Выбор этого отеля - ваша большая ошибка, Олаф."
                        m "И чтобы я вас простила, вам придется постараться."
                        olaf "Да, Мэм..."
                        # затемнение, шуршание одежды
                        # Линда стоит голая и Олаф тоже голый, эрекции у него нет, смотрит виновато на Монику
                        imgd 40148
                        mt "Пусть теперь сучка Линда почуствует себя моим реквизитом!"
                        mt "В следующий раз будет знать, как плести интриги со своей мерзкой подружкой-шлюшкой против МЕНЯ!"
                        mt "!!!"
                        mt "Я - Моника Бакфетт! А она - никто. Пустое место."
                        fadeblack
                        sound snd_fabric1
                        pause 2.0
                        music Groove2_85
                        imgfl 40149
                        m "Можете приступать, Олаф."
                        m "Я жду."
                        olaf "Но, Миссис Ба... Мэм..."
                        olaf "Есть небольшая проблема..."
                        # смотрит на свой грустный член
                        imgf 40150
                        m "Что, эта падшая невзрачная особа..."
                        m "Которая продает свое тело за деньги разным мужчинам..."
                        m "Совсем вас не возбуждает, Олаф?"
                        # Олаф виновато смотрит на Линду
                        imgd 40151
                        olaf "Нет, Мэм..."
                        music Stealth_Groover
                        imgf 40152
                        m "Конечно, она не сравнится со мной."
                        imgd 40153
                        m "Но вам сегодня повезло, Олаф..."
                        m "Я сегодня в хорошем настроении, поэтому..."
                        m "Так уж и быть... Я продемонстрирую вам, Олаф, что есть истинная женская красота."
                        # затемнение, шуршание одежды
                        # Моника сидит на кровати с надменным видом обнаженная, в одних перчатках и каблуках
                        fadeblack
                        sound snd_fabric1
                        pause 2.0
                        music Loved_Up
                        imgfl 40154
                        w
                        # Моника ехидно смотрит на Линду, та на нее - с ненавистью
                        imgf 40155
                        olaf "О, Мэм!"
                        olaf "Вы восхитительны, Мэм!"

                        imgd 40156
                        linda "!!!"

                        music Stealth_Groover
                        imgf 40157
                        m "Я знаю, Олаф, о чем вы мечтали сегодня весь вечер."
                        m "Пока угощали меня ужином в ресторане и сыпали комплиментами..."
                        # насмешливый взгляд на Линду
                        imgd 40158
                        m "Но поскольку эта особа осмелилась нарушить наши с вами планы..."
                        m "Я разрешу смотреть вам на меня..."
                        m "Пока она будет извиняться передо мной за свое неповиновение."
                        imgf 40159
                        olaf "О, Миссис Бак... Мэм!"
                        # Моника раздвигает ноги и приказывает Линде
                        sound Jump2
                        imgd 40160
                        m "А ты чего ждешь, падшая женщина?"
                        m "Приступай. Я разрешаю тебе поцеловать мою киску."
                        # Линда в шоке, смотрит на Монику, потом на Олафа
                        # Олаф прситально смотрит ан голую Монику, на Линду ноль эмоций
                        # член у него встает
                        # тот ей снова шепчет
                        music stop
                        sound plastinka1b
                        img 40156 hpunch
                        linda "!!!"
                        music Loved_Up
                        imgf 40161
                        w
                        imgd 40162
                        w
                        imgf 40163
                        w
                        sound Jump1
                        imgd 40164
                        w
                        music Groove2_85
                        imgf 40165
                        linda "Олаф! Я не буду этого делать!"
                        olaf "Линда! Помнишь то дело, с которым ты пришла ко мне за помощью?"
                        linda "Это здесь совсем ни при чем!"
                        olaf "Это мне решать! И я не смогу помочь тебе, если ты откажешь сейчас!"
                        imgd 40166
                        linda "Нет! Ты не посмеешь! Ты же обещал мне!"
                        linda "Ты же знаешь, как это важно для меня!"
                        imgf 40167
                        olaf "Знаю..."
                        olaf "И я сдержу свое обещание, если ты сделаешь, как приказывает Мэм."
                        olaf "Делай, что тебе говорят!"
                        imgd 40168
                        linda "!!!"
                        # взгляд Моники полон высокомерия и насмешки над Линдой
                        # та вынуждена послушаться и снова опускается на колени перед Моникой
                        # взгляд полон ненависти, но деньги Линда любит больше
                        # Линда начинает лизать киску Моники, Моника на нее насмешливо смотрит
                        music Stealth_Groover
                        imgf 40169
                        mt "Ну что, сучка?"
                        mt "Теперь ты поняла, что ты по сравнению со мной - никто!"
                        mt "Жалкая дешевка с непомерно завышенной самооценкой!"
                        mt "Никому не нужная и ничего из себя не представляющая!"
                        mt "Знай свое место, шлюшка!"
                        mt "!!!"
                        # Моника смотрит на Олафа
                        fadeblack 2.0
                        music2 Loved_Up
                        imgfl 40170
                        w
                        imgf 40171
                        m "Я позволяю тебе поцеловать мою киску..."
                        m "Приступай..."

                        imgd 40172
                        linda "Стерва!"
                        linda "!!!"

                        imgf 40199
                        w
                        imgd 40173
                        w
                        imgf 40174
                        w

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Licking1_1 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_1.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Licking1_1
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Licking1_2 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_2.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Licking1_2
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        sound lick3
                        imgd 40175
                        w
                        sound lick3
                        imgd 40174
                        w
                        sound lick3
                        imgd 40175
                        w
                        sound lick3
                        imgd 40174
                        w
                        sound lick3
                        imgd 40175
                        w
                        sound lick3
                        imgd 40174
                        w
                        sound lick3
                        imgd 40175
                        w

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Licking1_3 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_3.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Licking1_3
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Licking1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Licking1_4 = Movie(play="video/v_Visitor2_Monica_Investor2_Licking1_4.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Licking1_4
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        imgf 40176
                        m "А вам, Олаф, я разрешаю воспользоваться телом этой проститутки."
                        olaf "Мэм..."
                        m "И не разрешаю спорить со мной..."
                        # Олаф пристраивается сзади Линды и входит в нее
                        # Моника говорит Линде
                        label gallery_40179:
                        fadeblack 1.5
                        music2 Loved_up2
                        img 40177 hpunch
                        sound chpok3
                        w
                        imgfl 40178
                        m "А тебе никто не позволял останавливаться!"
                        m "Продолжай!"
                        imgf 40179
                        linda "!!!"

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_1 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_1.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_1
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_2 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_2.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_2
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        # сам смотрит на Монику и на то, как Линда лижет ее киску
                        imgd 40180
                        olaf "Оооо, Мэм..."
                        m "Олаф, вы представляете, что ваш член сейчас внутри меня?"
                        imgf 40181
                        olaf "Даа, Мэээм..."
                        olaf "Аааа..."

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_3 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_3.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_3
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        imgd 40182
                        olaf "Как я мечтаю попробовать вашу киску, Мэм!!!"
                        olaf "Ммммм..."

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_4 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_4.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_4
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        imgf 40183
                        olaf "Киску самой Миссис...!!!"
                        m "Олаф, молчать!"
                        imgd 40184
                        olaf "О, дааа..."
                        olaf "О, Мэээээм!!!"

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_5 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_5.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_5
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")


                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_6 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_6.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_6
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_7 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_7.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_7
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")

                        img black_screen
                        with diss
                        stop music
                        $ renpy.music.set_volume(0.5, 0.5, channel="music")
                        $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Visitor2_Monica_Investor2_Sex1_1.ogg"
                        scene black
                        image videov_Visitor2_Monica_Investor2_Sex1_8 = Movie(play="video/v_Visitor2_Monica_Investor2_Sex1_8.mkv", fps=30)
                        show videov_Visitor2_Monica_Investor2_Sex1_8
                        with fade
                        wclean
                        stop music
                        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                        $ renpy.music.set_volume(1.0, 0.5, channel="music")


                        imgd 40185
                        olaf "Оооо!"
                        olaf "Я сейчас кончу!!!"
                        menu:
                            "Кончить внутрь Линды.":
                                img 40186
                                sound bulk1
                                show screen photoshot_screen()
                                with hpunch
                                pause 0.7
                                hide screen photoshot_screen
                                olaf "Аааа..."
                                olaf "АААА!!"
                                img 40187
                                sound bulk1
                                show screen photoshot_screen()
                                with hpunch
                                pause 0.7
                                hide screen photoshot_screen
                                sound man_moan3
                                olaf "ААААААА!!!!"
                                imgf 40189
                                w
                                pass
                            "Кончить на киску Линды.":
                                img 40186
                                sound bulk1
                                show screen photoshot_screen()
                                with hpunch
                                pause 0.7
                                hide screen photoshot_screen
                                olaf "Аааа..."
                                olaf "АААА!!"
                                img 40188
                                sound bulk1
                                show screen photoshot_screen()
                                with hpunch
                                pause 0.7
                                hide screen photoshot_screen
                                sound man_moan3
                                olaf "ААААААА!!!!"
                                imgf 40190
                                w
                                pass
                        # Олаф отстраняется от Линды, а она отстраняется от Моники
                        # Моника злорадно на нее смотрит
                        # Линда шипит ей, пока Олаф не слышит
                        music2 stop
                        fadeblack 2.0
                        music Stealth_Groover
                        imgfl 40191
                        m "Ты свободна на сегодня."
                        m "Мистер более не нуждается в услугах проститутки."
                        imgf 40192
                        linda "Сука!"
                        imgd 40193
                        m "Продажная шкура!"
                        imgd 40194
                        linda "Я тебе этого просто так не оставлю!"
                        return
                    "Согласиться на ее условие":
                        music Stealth_Groover
                        imgf 19954
                        mt "Эта сучка никуда не денется."
                        mt "Она побоится, что если она мне откажет, я настрою Олафа против нее."
                        mt "Поэтому она не посмеет обмануть меня."
                        mt "Мне просто надо будет подойти на ресепшн после ухода Олафа."
                        mt "И забрать мои $ 500."
                        imgd 19955
                        mt "По-моему, это отличный план, Моника!"
                        mt "Ты не только самая красивая, ты еще и самая умная женщина!"
                        mt "И сегодня у тебя в кармане станет намного больше денег!"
                        # Моника говорит Линде
                        music Groove2_85
                        imgd 19956
                        m "Я найду тебя после того, как он уйдет."
                        linda "Договорились..." #  с улыбочкой
                        # Моника возвращается на свое место на диване
                        # Олаф снова берет ее за руку
                        sound highheels_short_walk
                        imgf 19957
                        w
                        fadeblack
                        sound highheels_short_walk
                        pause 2.0
                        music Stealth_Groover
                        imgfl 19958
                        w
                        sound highheels_short_walk
                        imgf 19944
                        m "Не нравится мне, как работает эта официантка..."
                        m "Какая-то она странная..."
                        m "Наверное, я уволю ее..."
                        imgd 19945
                        olaf "Не обращайте внимания, Миссис Бакфетт..."
                        olaf "Это простое недоразумение..."
                        olaf "Надеюсь, больше нас никто не побеспокоит..."
                        imgd 19946
                        m "Я надеюсь..."
            "Пусть эта шлюха уходит":
                music Stealth_Groover
                imgf 19937
                mt "Хммм..."
                mt "С другой стороны, пусть платит ей."
                mt "Не хочу видеть эту дрянь здесь!"
                mt "Мне важнее закрыть вопрос с его инвестированием в мой журнал..."
                mt "А эта сучка может ему проговориться, что я работаю в этом гребаном эскорте!"
                imgd 19938
                mt "Даже не представляю, какие будут последствия после этого!"
                mt "!!!"
                mt "Тем более..."
                mt "После встречи с этим подкаблучником я сдам бутылку вина."
                mt "И останусь при деньгах..."
                music Groove2_85
                imgf 19939
                linda "Нууу..."
                linda "Хорошо!"
                imgd 19940
                olaf "Все!"
                olaf "Иди!"
                # Линда возмущенно смотрит на Монику, та ей ехидно улыбается
                imgf 19942
                olaf "Иди, Линда!"
                olaf "Не создавай мне лишних проблем!"
                olaf "Иди! Иди!"
                # Линда сквозь зубы, глядя на Монику
                imgd 19943
                linda "Сучка!!!"
                # уходит
                # Олаф возвращается к Монике и снова берет ее за руку
                fadeblack
                sound highheels_short_walk
                pause 2.0
                music Stealth_Groover
                imgfl 19944
                m "Что это было, Олаф?!"
                olaf "Прошу прощения, Миссис Бакфетт."
                imgf 19945
                olaf "Не обращайте внимание... Это простое недоразумение..."
                olaf "Больше нас никто не побеспокоит..."
                imgd 19946
                m "Я надеюсь..."
    # затемнение
    fadeblack 2.0
    music Groove2_85
    # Олаф берет бутылку в руки
    imgfl 19960
    olaf "Самое лучшее вино для самой восхитительной женщины!"
    # Моника смотрит пристально на бутылку
    imgf 19961
    mt "Черт! Если он ее сейчас откроет, я не смогу сдать ее обратно!"
    mt "!!!"
    imgd 19962
    m "Чуть позже, Олаф..."
    imgf 19963
    olaf "Как пожелаете, Миссис Бакфетт."
    imgd 19964
    mt "Мне нужно подвести его к принятию положительного решения относительно инвестирования."
    mt "Как бы это сделать поизящнее?"
    mt "..."
    imgd 19965
    m "Олаф..."
    olaf "Да, Миссис Бакфетт?"
    menu:
        "Олаф, а вы знаете о том, что несколько инвесторов уже дали свое согласие?":
            music Hidden_Agenda
            imgf 19966
            m "А вы знаете о том, что несколько инвесторов из числа тех..."
            m "Кто присутствовал на моей презентации..."
            m "Уже дали свое согласие и даже перевели свои деньги в мою компанию."
            imgd 19967
            olaf "Серьезно? Я не знал об этом..."
            imgf 19968
            m "Да, Олаф..."
            m "И в отличие от них, Олаф, вы рискуете остаться без прибыли..."
            imgd 19969
            olaf "Я готов принять решение, Миссис Бакфетт..."
            olaf "Сегодня... Немного позже..."
            music Groove2_85
            imgd 19970
            mt "Черт!"
        "Что вы думаете о графиках Мистера Кэмпбелла?":
            music Hidden_Agenda
            imgf 19966
            m "А что вы скажете о графиках, которые продемонстрировал Мистер Кэмпбелл?"
            m "Мне кажется, что они выглядят достаточно убедительно..."
            imgd 19967
            olaf "Не подумайте, что я не доверяю такому уважаемому человеку, как Мистер Кэмпбелл..."
            olaf "Но я предпочел бы не торопиться в таких серьезных вопросах..."
            olaf "Ведь речь идет о достаточно больших денежных средствах."
            imgd 19969
            olaf "Я не привык рисковать такими суммами..."
            olaf "Сегодня я приму решение, Миссис Бакфетт... Но не сейчас... Немного позже..."
            music Groove2_85
            imgf 19970
            mt "!!!"
        "Вы хотели бы иметь в моем лице не только делового партнера, но и друга?":
            music Hidden_Agenda
            imgf 19966
            m "Олаф, мы могли бы с вами стать не только деловыми партнерами..."
            m "Если вы, конечно, дадите согласие на инвестицию в мой журнал..."
            imgd 19968
            m "В таком случае..."
            m "Мы могли бы с вами общаться и в более неформальной обстановке..."
            m "Иногда... Изредка..."
            imgf 19969
            olaf "О, Миссис Бакфетт!"
            olaf "Я мог только мечтать об этом!"
            imgd 19967
            olaf "Вы и правда хотели бы со мной встречаться?"
            olaf "Это была бы большая честь для меня, Миссис Бакфетт!"
            imgf 19971
            m "Дело за малым, Олаф..."
            m "Просто инвестируйте в мой журнал..."
            imgd 19972
            mt "А потом я пошлю тебя ко всем чертям, неудачник!"
            imgd 19973
            olaf "Я готов принять решение, Миссис Бакфетт..."
            olaf "Сегодня... Немного позже..."
            music Groove2_85
            imgf 19970
            mt "Что за идиот?!"
            mt "!!!"
        "Вы действительно считаете меня самой красивой женщиной в своей жизни?":
            music Hidden_Agenda
            imgf 19966
            m "Олаф, вы действительно считаете меня самой красивой женщиной?"
            imgd 19967
            olaf "Да, Миссис Бакфетт!"
            olaf "Я восхищаюсь Вашей красотой, Вашим умом, Вашей деловой хваткой..."
            olaf "А Ваша смелость в ведении бизнеса!"
            imgd 19969
            olaf "Эта Ваша последняя фотосессия!!"
            olaf "Я впечатлен, Миссис Бакфетт!!!"
            imgf 19968
            m "Приятно это слышать, Олаф..."
            m "Я надеюсь, что это не только слова..."
            imgd 19971
            m "Я заинтересована в том, чтобы мы с вами были не только хорошими знакомыми..."
            m "Но и партнерами."
            # Олаф залипает на ее грудь
            imgd 19974
            olaf "Да, Миссис Бакфетт... Партнерами..."
            imgf 19975
            m "Так вы согласны, Олаф?"
            olaf "Я? На что?"
            m "Сделать инвестицию в мой журнал..."
            imgd 19973
            olaf "Я... Я готов принять решение, Миссис Бакфетт..."
            olaf "Сегодня... Но немного позже..."
            music Groove2_85
            imgf 19970
            mt "Да сколько можно?!"
            mt "!!!"
            pass
    # Моника недовольно смотрит на Олафа
    music Groove2_85
    imgd 19937
    mt "Этот никчемный денежный мешок сегодня должен дать свое согласие!"
    mt "Биф сказал, что если он откажется, то он поставит во главе МОЕГО журнала..."
    mt "Какую-то глупую, безмозглую куклу!!!"
    mt "Мне нельзя допустить этого ни в коем случае!!!"
    imgd 19938
    mt "Это МОЙ журнал!!!"
    mt "!!!"
    mt "Но как мне заставить этого кретина Олафа инвестировать в журнал?"
    mt "???"
    mt "Может быть..."
    menu:
        "Соблазнить Олафа.":
            pass
    # Моника встает с дивана и направляется к кровати
    music Stealth_Groover
    imgf 19976
    mt "Этот никчемный Олаф не сможет устоять перед моей красотой!"
    mt "Он сделает эту инвестицию!"
    mt "Притом без всяких извращенств, о которых говорил сволочь Биф!"
    mt "Иначе я не Моника Бакфетт!"
    # Олаф как загипнотизированный смотрит на нее
    label gallery_40033:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 19977
    w
    sound Jump1
    imgf 19978
    mt "Сейчас он посмотрит на мою совершенную красоту..."
    mt "И просто не сможет сказать мне 'нет'!"
    imgd 19979
    m "Олаф..."
    olaf "Да, М-миссис Бакфетт?"
    m "Я подожду здесь, пока вы принимаете решение..."
    # Олаф смущенно смотрит на нее, потом встает и идет к кровати
    music Groove2_85
    imgf 19980
    olaf "Миссис Бакфетт, мне кажется, Вы могли бы помочь ускорить этот процесс..."
    m "Процесс принятия решения?"
    sound Jump2
    imgd 19982
    olaf "Да..."
    olaf "Если Вы не против, конечно..."
    olaf "Сейчас только от Вашего согласия зависит, будет ли мое решение положительным..."
    img 19981 hpunch
    m "???"
    # он протягивает руку и проводит по ноге Моники
    music Pyro_Flow
    m "!!!"
    imgf 19983
    mt "Вот дьявол!"
    mt "Он намекает на ЭТО?!"
    mt "?!?!?!"
    mt "Он предлагает мне, Миссис Монике Бакфетт, переспать с ним?!"
    mt "Из-за какой-то там инвестиции?!"
    mt "?!?!?!"
    mt "С другой стороны..."
    imgd 19984
    mt "Если он откажется, то я лишусь доступа в свой офис!"
    mt "ААААА!!!"
    mt "Что же мне делать?!"
    mt "А что, если потерпеть этого никчемного Олафа?.."
    mt "Если это даст гарантию того, что он сделает эту чертову инвестицию..."
    mt "..."
    menu:
        "Не соглашаться так быстро.":
            pass
    music Stealth_Groover
    imgf 19985
    m "Я не привыкла вести деловые переговоры в постели, Олаф!"
    m "Я, вообще-то, серьезная бизнес леди!"
    imgd 19986
    olaf "А я - серьезный бизнесмен, Миссис Бакфетт."
    olaf "И всегда держу свое слово!"
    olaf "Я инвестирую в Ваш журнал завтра же..."
    olaf "Если Вы поволите мне..."
    # кладет руку на ее попу
    img 19987 hpunch
    mt "!!!"
    menu:
        "Не соглашаться так быстро.":
            imgf 19988
            m "Олаф, а если об этом кто-то узнает?!"
            m "Я не хочу, чтобы моя репутация была подмочена!"
            imgd 19989
            olaf "Миссис Бакфетт, не в моих интересах распространять подобную информацию..."
            olaf "Вы ведь сами видели, какая у меня ревнивая жена."
            olaf "Мне не нужны лишние проблемы с ней."
            pass
        "Промолчать.":
            pass
    # затемнние, шуршание одежды
    # Моника сидит на кровати без брюк, в перчатках, каблуках и топе
    # Моника закрывается рукой (оттягивая верх от костюма)
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 40028
    olaf "Мы проведем с Вами вместе вечер на этой постели."
    olaf "И считайте, я стал Вашим инвестором, Миссис Бакфетт."
    imgf 40029
    mt "!!!"
    # смотрит на ее киску
    imgd 40030
    w
    menu:
        "Раздвинуть ноги.":
            pass
    fadeblack 2.0
    music Groove2_85
    imgd 40030
    w
    imgd 40031
    w
    imgf 40032
    olaf "Ооо... Как Вы прекрасны, Миссис Бакфетт!"
    imgd 40033
    w
    imgd 40034
    w
    menu:
        "Черт! У меня кончились доводы...":
            pass
    # Олаф мнет ее грудь через топ или наклоняется и целует ее живот, задирая топ
    music Loved_Up
    imgf 40035
    w
    sound kiss1
    imgd 40036
    w
    sound kiss1
    imgd 40037
    w
    imgf 40038
    w
    sound Jump1
    imgd 40039
    w
    sound kiss1
    imgf 40040
    w
    imgd 40041
    mt "Фу! Как это все омерзительно!"
    mt "Ненавижу! Ненавижу!"
    mt "!!!"
    # далее он наклоняется над ее лицом, тянется губами за ее поцелуем
    imgf 40042
    w
    img 40043 vpunch
    w
    sound snd_longkiss1
    imgf 40044
    w
    imgd 40045
    w
    imgd 40046
    w
    imgd 40045
    w
    imgf 40047
    olaf "Я не могу поверить в происходящее..."
    olaf "В моей постели..."
    olaf "Сама Миссис Бакфетт..."
    # снимает с нее блузку, оголяя грудь
    # целует
    sound vjuh3
    imgd 40048
    w
    imgd 40049
    w
    sound snd_kiss2
    imgf 40050
    w
    sound snd_kiss2
    imgd 40051
    w
    sound snd_kiss2
    imgd 40052
    w
    imgd 40053
    olaf "С самой первой презентации я мечтал об этом..."
    olaf "И Вы меня единственного из всех инвесторов удостоили этой чести..."
    if monicaEscortLindaTable6 == True:
        #
        $ notif(_("У Моники был секс с одним из инвесторов."))
        #
        imgf 40054
        mt "Ты не единственный, придурок!"
        mt "Но об этом знаю только я..."
    # инвестор лежит голый на кровати рядом с Моникой, она голая, в одних перчатках
    label gallery_40079:
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 40055
    w
    imgf 40056
    olaf "Миссис Бакфетт, смотрите, какой он у меня твердый..."
    olaf "Я хочу, чтобы Вы прикоснулись к нему своей рукой..."
    olaf "Затянутой в перчатку..."
    olaf "Я так возбужден, Миссис Бакфетт..."
    imgd 40057
    mt "Фу! Я сейчас испачкаю об него свою перчатку!"
    mt "Но, может быть, этим он и ограничится?"
    mt "..."
    # Моника протягивает руку и обхватывает его член
    imgf 40058
    olaf "Оооо!!!"
    olaf "Обхватите его еще крепче, Миссис Бакфееееетт!"
    sound man_moan3
    imgd 40060
    olaf "Даааа!!!"
    imgf 40059
    olaf "Потрясающе!!!"
    imgd 40061
    w
    # спустя останавливает ее
    imgd 40062
    olaf "А теперь идите ко мне..."
    olaf "Позвольте мне насладиться Вашей красотой..."
    fadeblack 1.5
    music Loved_Up
    # Моника ложится на спину
    imgf 40063
    w
    imgd 40064
    olaf "Раздвиньге Ваши ножки, Миссис Бакфетт..."
    imgf 40065
    m "Это обязательно?!"
    imgd 40066
    olaf "Мммм... Да, Миссис Бакфетт..."
    olaf "У нас ведь деловые переговоры..."
    imgf 40067
    olaf "Я должен внимательно рассмотреть все пункты нашей договоренности."
    m "!!!"
    menu:
        "Раздвинуть ноги.":
            pass
    # Моника раздвигает ноги, лицо недовольное
    fadeblack 1.5
    music2 Loved_Up
    imgf 40067
    w
    imgd 40068
    olaf "Оооо... Дааа..."
    # тянется к ней рукой, водит по киске
    imgf 40069
    w
    sound hlup25
    imgd 40070
    w
    imgd 40069
    w
    sound hlup25
    imgd 40070
    w
    imgd 40069
    w
    sound hlup25
    imgd 40070
    w
    imgd 40069
    w
    sound hlup25
    imgd 40070
    w
    imgf 40071
    mt "Ох..."
    mt "Снова эти странные ощущения!"
    mt "Мне это совсем не нравится!!"
    mt "Так... Так необычно..."
    $ blur_effect = 1
    imgd 40071
    mt "Кажется, вино немного дало мне в голову..."
    $ blur_effect = 0
    imgd 40072
    olaf "Ммммм..."
    olaf "Не могу поверить, что я сейчас буду обладать самой Миссис Моникой Бакфетт!"
    # вводит в нее палец
    sound chpok3
    img 40073 hpunch
    olaf "Что я сейчас введу в нее свой член..."
    imgd 40074
    olaf "О, дааа..."
    imgd 40073
    w
    sound hlup19
    imgd 40074
    w
    imgd 40073
    w
    sound hlup19
    imgd 40074
    w
    imgd 40073
    w
    sound hlup19
    imgd 40074
    w
    imgf 40075
    w
    sound ahhh4
    imgd 40076
    mt "Ой..."
    mt "Это становится все сильнее!!"
    mt "Надо прекратить это немедленно!!!"
    mt "Меня пугает это!!!"
    mt "!!!"
    # инвестор убирает палец из Моники
    imgf 40077
    olaf "Миссис Бакфетт..."
    olaf "Позвольте Ваши ножки..."
    # хватает Монику под коленями и задирает высоко ее ноги
    # он приближает к ней член и водим им между ног Моники вверх-вниз
    sound vjuh3
    imgd 40078
    olaf "Оооо..."
    olaf "Сейчас я войду в Вас, Миссис Бакфетт."
    olaf "Сейчас Вы почувствуете внутри себя мой член."
    imgf 40079
    mt "Ох! Черт! Черт!"
    mt "Я не понимаю, что со мной происходит!"
    mt "Мне нужно подумать о чем-то другом!"
    imgd 40080
    mt "Нужно отвлечься!!"
    mt "О чем подумать?!"
    mt "?!"
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    imgf 40081
    w
    sound hlup2
    imgd 40082
    olaf "Я вижу, как Вы этого желаете..."
    sound hlup25
    imgd 40081
    w
    sound hlup2
    imgd 40082
    w
    sound hlup25
    imgd 40081
    w
    sound hlup2
    imgd 40082
    w
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 40083
    olaf "Дааа... Ваша киска уже вся мокрая..."
    # прислоняет головку члена к ее киске и вводит на пол шишечки
    olaf "Хотите почувствовать его внутри своей влажной киски, Миссис Бакфетт?"
    imgd 40084
    m "!!!"
    mt "Нет!!!"
    imgf 40085
    olaf "А в постели Вы молчунья, Миссис Бакфетт..."
    olaf "Можете не отвечать..."
    # вводит член
    olaf "Я чувствую, как Вы этого жаждете..."
    # Монике приятно, но она в итоге не кончит
    sound chpok3
    sound2 ahhh5
    img 40086 vpunch
    olaf "Аааа..."
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_1 = Movie(play="video/v_Monica_Investor2_Sex1_1.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 40087
    olaf "Какая горячая влажная киска!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_2 = Movie(play="video/v_Monica_Investor2_Sex1_2.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound ahhh6
    imgd 40088
    mt "Боже, когда это все закончится?!"
    mt "Я не могу справится с этим странным чувством внутри..."
    mt "Внутри меня!!!"
    sound ahhh7
    imgd 40089
    mt "Оно нарастает!"
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    mt "Как волна!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_3 = Movie(play="video/v_Monica_Investor2_Sex1_3.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music2 Loved_up2
    imgf 40090
    olaf "Ммммм..."
    olaf "Киска самой Миссис Моники Бакфетт!!!"
    imgd 40091
    olaf "О, дааа..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_4 = Movie(play="video/v_Monica_Investor2_Sex1_4.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound ahhh8
    imgf 40092
    mt "Все сильнее!"
    mt "Наполняет меня... Всю..."
    mt "Ох..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_5 = Movie(play="video/v_Monica_Investor2_Sex1_5.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_6 = Movie(play="video/v_Monica_Investor2_Sex1_6.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 40093
    olaf "О, Миссис Бакфеееет!!!"
    olaf "Оооо!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Investor2_Sex1_1.ogg"
    scene black
    image videov_Monica_Investor2_Sex1_7 = Movie(play="video/v_Monica_Investor2_Sex1_7.mkv", fps=30)
    show videov_Monica_Investor2_Sex1_7
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound man_moan3
    sound2 ahhh7
    imgf 40095
    olaf "Я сейчас кончу!!!"
    menu:
        "Кончить внутрь Моники.":
            img 40096
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            olaf "Аааа..."
            olaf "АААА!!"
            img 40094
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan3
            olaf "ААААААА!!!!"
            imgf 40098
            w
            pass
        "Кончить на киску Моники.":
            img 40096
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            olaf "Аааа..."
            olaf "АААА!!"
            img 40097
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan3
            olaf "ААААААА!!!!"
            imgf 40099
            w
            pass
    # Моника лежит растерянная
    music2 stop
    fadeblack 1.5
    music Stealth_Groover
    imgfl 40100
    mt "Боже!"
    mt "Что это было?!"
    img 40101 vpunch
    mt "У меня что, был только что секс?!"
    mt "Как я это позволила! Фи!"
    mt "Видимо, у меня серьезные проблемы с нервами..."
    mt "Да... Это все нервы..."
    if monicaHotelAdminAgreement3 == True:
        imgd 40102
        mt "Или этот дурацкий отель на меня так влияет, мне надо заканчивать с этим эскортом!"
        mt "..."
    imgd 40102
    mt "Хорошо, что он закончил и это странное пугающее чувство прекратилось!"
    mt "!!!"
    # затемнение
    label gallery_19992:
    # Моника сидит на кровати недовольная
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    if monicaHotelAdminAgreement3 == True:
        imgfl 19990
        mt "Ненавижу это все!!!"
        mt "Мало того, что пришлось терпеть этого мерзкого Олафа!"
        imgf 19991
        mt "Теперь еще я должна отдать $ 450 этой сучке администраторше!!!"
        mt "!!!"
        music Stealth_Groover
        imgd 19992
        mt "Хорошо, что есть бутылка вина, которую я сдам!"
        mt "С этих денег я отдам процент администраторше."
        # инвестор в это время идет по направлению к столику, на котором стоит вино
        imgd 19993
        mt "Остальное заберу себе."
        mt "Это будет моя моральная компенсация за сегодняшний вечер!"
        mt "Осталось только подтвердить его согласие на сделку..."
    else:
        imgfl 19990
        mt "Ненавижу это все!!!"
        mt "Мне пришлось терпеть этого мерзкого Олафа!"
        imgf 19991
        mt "Из-за дурацких приказов сволочи Бифа!!!"
        mt "Бесит!!!"
        mt "!!!"
        music Stealth_Groover
        imgd 19992
        mt "Хорошо, что есть бутылка вина, которую я сдам!"
        # инвестор в это время идет по направлению к столику, на котором стоит вино
        mt "Это будет моя моральная компенсация за сегодняшний вечер!"
        imgd 19993
        mt "Осталось только подтвердить его согласие на сделку..."
    # Олаф стоит возле столика и смотрит на бутылку
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 19994
    olaf "Миссис Бакфетт..."
    olaf "Сегодня был такой нервный вечер..."
    olaf "Я... Я не верю в то что это все-таки случилось..."
    imgf 19995
    olaf "Миссис Бакфетт, меня... меня бросает в пот..."
    olaf "Я... Мне надо.. Мне надо..."
    # хватает быстро бутылку, открывает пробку
    sound bottle1
    imgd 19996
    w
    sound Jump2
    imgd 19997
    mt "!!!" # Моника в ужасе смотрит на бутылку
    olaf "Все же выпью!"
    olaf "И отмечу тем самым свою новую инвестицию!"
    olaf "В Ваш журнал!"
    sound snd_drinking_water
    imgd 19998
    w
    fadeblack 1.5
    sound snd_drinking_water
    w
    sound snd_drinking_water
    w
    # выпивает всю бутылку в один глоток
    music Power_Bots_Loop
    img 19999 hpunch
    mt "Нет! Нет!"
    mt "Твою мать!!!"
    mt "КРЕТИН!!!"
    mt "!!!"
    # Олаф отлипает от уже опустевшей бутылки
    music Groove2_85
    imgf 40000
    olaf "АХ! Напиток Богов, Миссис Бакфетт!"
    olaf "Жаль, что Вы не попробовали!"
    music Pyro_Flow
    imgd 40001
    mt "АААА!!!"
    mt "Выпил!? Он выпил всю бутылку, одним залпом?!"
    mt "Мои $ 5 000!!! ВЫПИЛ!!!"
    mt "Ненавижу!!!"
    mt "!!!"
    imgd 40002
    mt "Так, спокойно, Моника!"
    mt "Ты можешь исправить эту ситуацию!"
    mt "Подумай, как это сделать..."
    mt "Думай, Моника, думай!!!"
    # Моника встает с кровати и подходит к Олафу
    label gallery_40019:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 40003
    m "Олаф, я рада, что мы с вами заключили эту сделку."
    olaf "О, а как я рад, Миссис Бакфетт!!!" # пьяненький уже
    m "Да..."
    m "Думаю, что на этом можно завершить нашу встречу, Олаф?"
    imgf 40004
    olaf "Не хотите поехать со мной в клуб, Миссис Бакфетт?"
    olaf "Выпьем еще вина?"
    olaf "Или возьмем чего покрепче, а?"
    olaf "Виски? Или водка?"
    imgd 40005
    m "Нет, Олаф..."
    m "У меня на сегодня еще запланированы дела."
    m "Сами понимаете, работа..."
    imgd 40006
    olaf "Жаль..."
    olaf "Тогда поеду один. И куплю себе водки!"
    music Hidden_Agenda
    imgf 40007
    m "Олаф, не забудьте оставить $ 1000 на чай персоналу..."
    # Олаф возмущенно
    imgd 40008
    olaf "Тысячу?!"
    olaf "Но, Миссис Бакфетт, нас не обслуживали на такую сумму!"
    # Моника раздраженно
    imgf 40009
    m "Олаф, это мой отель и я привыкла хорошо относиться к своим сотрудникам!"
    music Groove2_85
    imgd 40010
    olaf "О, Миссис Бакфетт, Вы такая добрая!"
    olaf "Мне кажется, Ваши сотрудники слишком эксплуатируют Вашу доброту!"
    olaf "Я не допущу такого отношения к Вам, Миссис Бакфетт!"
    sound man_steps
    imgf 40011
    olaf "Сейчас я поставлю их всех на место!"
    # идет к выходу из номера
    music stop
    sound plastinka1b
    img 40012 vpunch
    mt "Черт!"
    mt "!!!"
    music Stealth_Groover
    imgd 40013
    m "Олаф!"
    m "Не надо ни с кем говорить!"
    m "Это мой отель и мои сотрудники!"
    m "Я все решаю здесь сама!"
    imgf 40014
    olaf "Как скажете, Миссис Бакфетт..."
    olaf "Но если что, я всегда готов защитить Вас!"
    music Hidden_Agenda
    imgd 40015
    m "Хорошо, хорошо..."
    m "Тогда оставьте хотя бы $ 700..."
    m "Или я посчитаю вас жадным, Олаф!"
    # Олаф хитро улыбаясь
    olaf "Мистер Биф сказал, что любые деньги должны идти через Вашу фирму..."
    m "$ 500!!!"
    if monicaHotelAdminAgreement3 == True:
        imgd 40016
        m "Или я заставлю вас заплатить за этот номер в 5 раз больше, Олаф!"
        m "Официально, через мою компанию!"
    # Олаф с сомнением смотрит на нее
    imgf 40017
    olaf "Ну хорошо, Миссис Бакфетт!"
    olaf "Я согласен оставить $ 500 на чай..."
    music Stealth_Groover
    imgd 40018
    mt "Наконец-то!"
    mt "!!!"
    sound vjuh3
    imgf 40019
    olaf "Кому отдать эти чаевые?"
    m "Вы можете отдать их мне, Олаф."
    if monicaHotelAdminAgreement3 == True:
        imgd 40019
        m "Я не являюсь одним из тех испорченных властью боссов..."
        m "Которые гнушаются сами передать чаевые своим сотрудникам!"
        imgd 40020
        mt "Дьявол, получается я заработала всего $ 50! За все что мне пришлось терпеть здесь!"
        mt "Моника, ты же самая богатая женщина этого города!"
        mt "Ты умеешь зарабатывать сотни миллионов!.."
        with hpunch
        mt "ТОГДА КАКОГО ХРЕНА ВСЕГО $50!!!"
        # затемнение
        imgf 40021
        m "Да, кстати, Олаф!"
        m "У меня подозрения насчет тебя и сотрудницы моего отеля!"
        # Олаф испуганно смотрит на нее
        imgd 40022
        olaf "П-подозрения?!"
        imgf 40023
        mt "Не хватало еще чтобы эта сучка Линда разболтала ему про то что я работаю здесь..."
        mt "Конечно, никто в это не поверит..."
        mt "Что Моника Бакфетт работает в эскорте в каком-то второсортном отеле..."
        imgd 40024
        mt "Тем более это не Моника Бакфетт, а [monica_hotel_name]..."
        mt "Но все-же..."
        imgf 40025
        m "Мне сдается, вы пытаетесь действовать разлагающе на коллектив моей компании, Олаф!"
        m "Я запрещаю вам приближаться к этой шлюхе и к этому отелю!"
        m "Олаф, вам все понятно?!"
        imgd 40026
        olaf "Да, Миссис Бакфетт, конечно!"
    imgd 40025
    m "Все, Олаф, вы свободны!"
    imgf 40027
    m "Завтра я узнаю у Бифа по поводу вашего перевода денежных средств!"
    # затемнение
    return
