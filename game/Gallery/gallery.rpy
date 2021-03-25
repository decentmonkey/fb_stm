default gallery_mode = False

label process_gallery(gallery_label):
    music stop
    img black_screen
    with diss
#    python:
#        storedRain = rain
#        rain = False
#        storedVar = {}
#        for key1 in dir():
#            if key1 != "storedVar":
#                try:
#                    storedVar[key1] = globals()[key1]
#                except TypeError:
#                    pass
    pause 0.5
    $ gallery_mode = True
    $ money_stored = money
    call expression gallery_label
    $ gallery_mode = False
    $ money = money_stored
    hide screen photoshoot_camera_icon
    hide screen photoshoot
#    python:
#        rain = storedRain
#        for key1 in storedVar:
#            globals()[key1] = storedVar[key1]
#        storedVar = False

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_5
    return


############ Betty 1############

label gallery_7293:
    #render
    #сцена Бетти и Фреда в прачечной
    #Бетти что-то делает
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_18
    scene black_screen
    with Dissolve(1)
    music Loved_Up
    img 7272
    with fade
    w
    img 7269
    with fade
    w
    img 7270
    w
    img 7271
    with fade
    w
    img 7273
    with fade
    fred "О! Мэм! Вы пришли..."
    img 7274
    betty "Я пришла, Фред."
    img 7275
    fred "Мэм, что Вы прикажете делать мне?"
    img 7276
    with fade
    betty "Покажи его..."
    #фред раздевается
    #звук одежды
    #fade
    sound snd_fabric1
    img 7277
    with fadelong
    w
    img 7278
    w
    img 7279
    betty "..."
    img 7281
    w
    img 7282
    fred "..." #улыбается
    img 7283
    w
    img 7280
    betty "Можно я потрогаю его?"
    img 7282
    fred "Конечно, Мэм!"
    img 7284
    with fade
    w
    img 7285
    w
    img 7286
    betty "..."
    img 7287
    betty "Упругий..."
    img 7288
    fred "Вы можете потрогать его язычком..."
    img 7289
    betty "..."
    menu:
        "Коснуться члена Фреда язычком...":
            pass
        "Нет времени на это...":
            return
    #Бетти садится и трогает член Фреда я языком
    img 7290
    with fade
    w
    img 7291
    w
    img 7292
    w
    img 7293
    w
    img 7294
    w
    #касается языком
    img 7295
    with fade
    w
    img 7296
    w
    img 7297
    w
    img 7298
    w
    img 7299
    with fade
    betty "Соленый..."
    img 7300
    fred "Мэм..."
    "Вы можете взять его в свой ротик..."
    img 7301
    w
    img 7302
    with fade
    betty "В следующий раз!"
    "Мало времени, Фред!"
    img 7303
    "Меня ждет Ральф!"
    menu:
        "Сделай это быстро...":
            pass
        "Я ухожу...":
            "Меня ждет Ральф!"
            betty "Я ухожу..."
            fred "Как скажете, Мэм..."
            return
    img 7304
    with fade
    "Давай скорее!"
    img 7305
    with Dissolve(0.5)
    w
    img 7306
    with Dissolve(0.5)
    w
    img 7307
    with Dissolve(0.5)
    w
    img 7308
    with fade
    fred "Давайте я подержу Ваши трусики, Мэм!"
    w
    img 7309
    with fade
    w
    #Бетти нагибается задом
    img 7310
    w
    img 7311
    w
    img 7312
    w
    #Фред одевает трусики на член
    sound Jump2
    img 7313
    with fade
    w
    img 7314
    w
    img 7315
    w
    img 7316
    with fade
    betty "Фред! Давай скорее!"
    "Меня ждет Ральф!"
    img 7317
    with fade
    fred "Как скажете, Миссис Робертс!"
    img 7318
    "Вы мой Босс!"
    #Фред трахает Бетти сзади

    label gallery_7320:
    music Indo_Rock
    img 7319
    w
    img 7320
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_1 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_1.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_1
    wclean
    img 7321
    w
    img 7322
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_2 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_2.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_2
    wclean
    img 7323
    w
    img 7324
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_3 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_3.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_3
    wclean
    img 7325
    w
    img 7326
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_4 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_4.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_4
    wclean
    img 7327
    w
    img 7328
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_5 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_5.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_5
    wclean
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_6 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_6.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_6
    wclean
    img 7329
    w
    img 7330
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_7 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_7.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_7
    wclean
    img 7331
    w
    img 7332
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_8 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_8.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_8
    wclean
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_9 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_9.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_9
    wclean
    img 7333
    w
    img 7334
    w
    img 7335
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_12 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_12.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_12
    wclean
    img 7336
    w
    img 7337
    w
    img 7338
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_13 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_13.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_13
    wclean
    img 7339
    w
    img 7340
    w
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_14 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_14.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_14
    wclean
    scene black
    image videov_Basement_Laundry_Fred_Betty_Sex_1_15 = Movie(play="video/v_Basement_Laundry_Fred_Betty_Sex_1_15.mkv", fps=30)
    show videov_Basement_Laundry_Fred_Betty_Sex_1_15
    wclean
    img 7341
    w
    img 7342
    w
    img 7343
    with fade
    fred "Ааааагх!!!"
    img 7344
    betty "Не вздумай кончить в меня!"
    fred "Да, Мэм! Как скажете!"
    img 7345
    with fade
    fred "Ааааагх!!!"
    img 7346
    w

    #Фред кончает Бетти на лицо
    music Groove2_85
    img 7347
    with fade
    betty "Что ты сделал?"
    "Зачем ты кончил мне на лицо???"
    img 7348
    with fade
    w
    img 7349
    "Мои трусики???" #Смотрит на член Фреда
    img 7350
    w
    img 7351
    fred "Мэм, Вы просто не в курсе..."
    "В больших городах принято после секса кончать девушке на лицо..."
    "Все прогрессивные люди делают это!"
    img 7352
    with fade
    betty "Правда? Так принято?"
    fred "Да, Мэм!"

    img 7353
    betty "Где мой шарф? Ты видел его?"
    img 7354
    with fade
    fred "Вы имеете ввиду этот шарф, Миссис Робертс?"
    img 7355
    w
    img 7356
    w
    img 7357
    w
    img 7358
    with fade
    w
    #Бетти недовольно смотрит на него и одевает шарф
    img 7359
    w
    img 7360
    with fade
    betty "..."
    img 7361
    fred "..."

    img 7362
    with fade
    betty "Кто-то идет!"
#    "Скорее всего это оболтус Барди!"
    fred "Мэм! Я знаю отсюда другой выход."
    "Не беспокойтесь, меня не увидят."
    img 7363
    with fade
    betty "Я скажу тебе когда захочу снова."
    fred "Конечно, Мэм!"
    "Это моя работа!"
    return

label gallery_7692:
    # render
    # Моника подходит к раздевалкам, либо к Стефани и Ребекке
    # первый раз
    #rebecca
    #stephanie
    music Groove2_85
    img 7678
    with fade
    w
    img 7679
    with fade
    w
    img 7680
    w
    img 7681
    w
    img 7682
    w
    sound Jump1
    img 7683
    with hpunch
    w
    # Подружки смотрят на нее с удивлением
    sound Jump1
    img 7684
    with hpunch
    w
    img 7685
    with fade
    w
    img 7686
    w
    img 7687
    with fade
    betty "Гуверантка! Где моя сумка с униформой?"
    img 7688
    betty "Быстро неси ее сюда!"
    img 7689
    m "Вот Ваша сумка, Миссис Робертс."
    img 7690
    w
    #fade
    img 7691
    sound snd_fabric1
    with fadelong
    w
    img 7692
    betty "Гувернантка, ты можешь подождать меня здесь, пока я занимаюсь." #Вид на голую грудь Бетти
    img 7694
    w
    img 7695
    w
    img 7696
    w

    img 7693
    m "Да, Миссис Робертс" # Монику корежит, на нее смотрят

    # Бетти в спортивном
    img 7697
    with fade
    betty "Можешь посидеть здесь или понаблюдать за мной."

    # Бетти уходит
    img 7698

    #fade
    img black_screen
    with Dissolve(1.0)
    pause 2.0
    music BossaBossa
    img 7699
    with fadelong
    stephanie "Моника! Что это значит?!"
    stephanie "Почему эта провинциальная дура разговаривает с тобой в таком тоне?!"

    img 7700
    rebecca "И почему ты одета в это?!"
    "Это что, униформа гувернантки?!"
    img 7701
    "Фу! Моника!"
    img 7702
    stephanie "И куда ты пропала?"
    img 7703
    "У нас был девичник и мы не смогли дозвониться до тебя!"
    img 7704
    mt "ЧЕРТ!!!"
    "Я влипла!!!"
    "Я знаю что я очень умная, но как возможно выкрутиться из этого!"
    img 7705
    "Правду говорить им точно не стоит!"
    "Помощи от них не будет никакой!"
    "Они только разболтают об этом всему городу!"
    "ДЬЯВОЛ!!!"

    img 7706
    with fade
    m "Ой! Девочки!"
    "Пожалуйста, тише!"
    "Не выдавайте меня этой дуре!"
    img 7707
    stephanie "Но почему, Моника!"
    rebecca "Моника, что все это значит?!"
    img 7708
    m "Тсссс! Тише!"
    "Девочки! Я не могу Вам пока рассказать!"
    "Но обзавидуетесь мне, когда потом все узнаете!"
    img 7709
    "Это секретная операция, меня надоумил Дик на нее!"
    "Скоро все будет закончено и я окажусь на первых полосах всех газет!"
    "Вот увидите!"
    img 7710
    "Но сейчас я претворяюсь гувернанткой этой дуры."
    img 7711
    "Ее муж крупный мафиози и мы выведем его на чистую воду!"
    img 7712
    rebecca "Секретная операция, мафиози..."
    "Моника, зачем тебе это все надо?"
    img 7713
    stephanie "Да, Моника!"
    "Я допускаю что Вы играете с Диком в какие-то странные игры."
    "Но зачем позволять так общаться с собой, как делает эта провинциальная дура!"
    img 7714
    m "Ой! Девочки!"
    "Не учите меня жить!"
    "Я испытала гораздо больше удовольствий чем Вы за всю свою жизнь!"
    "И мне становится скучно!"
    "Я хочу разнообразия, адреналина!"
    img 7715
    "Вы живете скучно, девочки!"
    "Я потом расскажу Вам все, Вы обзавидуетесь, обещаю!"
    img 7716
    stephanie "Ну не знаю, Моника... Возможно..."
    "Но обещай что все расскажешь потом!"
    img 7717
    rebecca "Да, Моника! Нам же интересно!"
    img 7718
    m "Конечно, девочки!"
    "Вы же знаете, у меня от Вас нет секретов!"
    img 7719
    rebecca "Хорошо, Моника!"
    "Нам не терпится узнать!"
    img 7720
    stephanie "Моника, а ты придешь на следующий девичник?"
    "Он уже скоро!"
    img 7721
    m "Я подумаю, девочки."
    "Мне это кажется сейчас скучным."
    img 7722
    with fade
    rebecca "Моника, но мы все-равно будем ждать тебя!"
    img 7723
    stephanie "Моника, приходи!"
    "Заодно расскажешь все!"
    img 7724
    m "Хорошо, девочки."
    "Вы можете идти заниматься..."
    stephanie "Пока, Моника!"
    rebecca "Пока, подружка!"
    m "Пока, девочки!"
    img 7725
    with fade
    w
    return

label gallery_8563:
    # В один из дней Бетти находится в спальне. Заходит Фред.
    # Бетти в белье (заранее определяется какое белье, запуск когда в определенном)
    # Бетти зло спрашивает что он тут делает?
    # Фред говорит что его послал Мистер Робертс, чтобы позвать Бетти, потому что он уезжает с Фредом по делам
    # и хочет поцеловать супругу перед отъездом.
    # Бетти спрашивает и что, ради этого он послал прислугу водителя в ее спальню?
    # Фред отвечает что вообще-то нет, просто кое-кто еще хочет ее поцелуя.
    # И снимает штаны.
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _rcall_textonblack_19
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 8536
    with fade
    w
    img 8537
    with fade
    w
    img 8538
    with fade
    w
    img 8539
    betty "Фред?!"
    img 8540
    betty "Фред! Что ты делаешь здесь?! В спальне хозяев!"
    img 8541
    with fade
    fred "Миссис Робертс! Меня послал Мистер Робертс, чтобы я позвал Вас спуститься вниз к нему!"
    fred "Мистер Робертся собирается уезжать по делам, до вечера, и хочет поцеловать супругу перед отъездом!"
    img 8542
    betty "И что, ради этого от прислал прислугу водителя в нашу спальню?"
    img 8543
    fred "Мэм, вообще-то нет..."
    sound snd_zip
    #fade
    img 8544
    with fadelong
    "Просто кое-кто еще хочет Ваш поцелуй..."
    # И снимает штаны.

    # Бетти говорит что он сошел с ума? Здесь ходит Барди, не хватало чтобы он это увидел.
    # И что он вообще себе позволяет в ее спальне?
    # Фред отвечает что закрыл дверь и ведет себя профессионально, так как хозяйка богатого дома хочет поцеловать его член.
    # Бетти смотрит на Фреда, спускается и целует.
    # Фред говорит что хозяйка дома хочет взять член в рот поглубже. Бетти делает минет.
    # Фред кончает и говорит что спасибо, теперь можно идти к Мистеру Робертсу.
    img 8545
    with fade
    w
    img 8546
    with Dissolve(0.5)
    w
    img 8547
    betty "Фред?! Ты сошел с ума?!"
#    "Здесь ходит Барди! Не хватало чтобы он это увидел!"
    img 8548
    with fade
    betty "И что ты вообще себе позволяешь?!"
    sound hlup10
    img 8549
    with fade
    "Прямо в спальне хозяев дома!"
    img 8550
    fred "Мэм, я профессионал и поэтому предусмотрительно закрыл дверь."
    fred "Я веду себя профессионально, так как знаю что хозяйка богатого дома хочет этот член..."
    betty "!!!"
    menu:
        "Посмотреть вниз...":
            pass
        "В другой раз, Фред!":
            betty "В другой раз, Фред!"
            music stop
            img black_screen
            with Dissolve(2.0)
            return
    img 8551
    with fade
    betty "..."
    fred "..."
    img 8552
    betty "..."
    img 8553
    with fade
    w
    music Loved_Up
    img 8554
    with fade
    w
    img 8555
    with Dissolve(0.5)
    w
    img 8556
    with fade
    w
    img 8557
    with Dissolve(0.5)
    fred "Ну-же..."
    img 8558
    with fade
    w
    #dissolve
    img 8559
    with Dissolve(0.5)
    w
    music stop
    sound kiss2
    img 8560
    with Dissolve(0.5)
    w
    music snd_licking1
    img 8561
    w
    img 8562
    w
    img 8563
    w
    img 8564
    w
    img 8565
    with Dissolve(0.5)
    w

    # Бетти смотрит на Фреда, спускается и целует.
    music Loved_Up
    img 8566
    with fade
    fred "Хозяйка богатого дома хочет взять член в рот поглубже..."
    sound hlup19

    img 8567
    betty "..."
    img 8568
    with fade
    w
    img 8569
    with fade
    w
    #video
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(0.7)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_1 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_1.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_1
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_2 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_2.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_2
    wclean
    stop music
    $ renpy.music.set_volume(0.7)
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_3 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_3.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_4 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_4.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_5 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_5.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Bedroom_Fred_Betty_Blowjob_1.ogg"
    scene black
    image videov_Bedroom_Fred_Betty_Blowjob_1_6 = Movie(play="video/v_Bedroom_Fred_Betty_Blowjob_1_6.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Blowjob_1_6
    wclean
    $ renpy.music.set_volume(1.0)
    music stop
    music Loved_Up
    img 8570
    with fade
    w
    img 8571
    with fade
    w
    img 8572
    with fade
    w
    img 8573
    with fade
    sound bulk1
    fred "ААААаааааххх!"
    #longfade
    music Groove2_85
    img 8574
    with fadelong
    fred "Спасибо, Мэм."
    "Теперь можно идти к Мистеру Робертсу."
    img 8575
    with Dissolve(0.5)
    w
    img 8576
    w

    # Бетти говорит что куда это он собрался, давай быстрее и тд. Повторяется сцена секса (можно взять из прошлой версии)
    # Фред кончает. Бетти говорит что не вздумай снова кончить на лицо, раздается крик Ральфа: Бетти, ты где?
    # Фред снова кончает на лицо, Бетти зло смотрит и вытирает его.

    img 8577
    with fade
    menu:
        "Куда это ты собрался?!":
            pass
        "Пойдем...":
            betty "Пойдем..."
            return

    betty "Куда это ты собрался?!"
    sound snd_fabric1
    img 9615
    with fade
    betty "А как же я?!"
    img 8578
    sound snd_bodyfall
    #звук падающих предметов
    w
    music Loved_Up2
    img 8579
    with fade
    betty "Давай быстрее!"
    img 8580
    fred "Как скажете, Мэм!"
    "Вы мой Босс!"
    img 8581
    betty "И не забудь вытереть свой член от спермы, прежде чем начнешь!"
    #fade
    img 8582
    with fade
    fred "Да, Мэм! Конечно!"
    img 8583
    betty "Вовсе необязательно делать это о мою занавеску!"
    #fade
    img 8584
    with fade
    fred "Простите, Мэм!"
    img 8585
    fred "Я приношу свои извинения."
    img 8586
    fred "Как профессионал!"
    #sex
    sound hlup10
    img 8587
    with fade
    w
    img 8588
    w
    img 8589
    w
    music stop
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.8)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_1 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_1.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_1
    with fade
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.8)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_2 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_2.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_2
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_3 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_3.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_3
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_4 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_4.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_4
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_5 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_5.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_5
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_6 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_6.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_6
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_7 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_7.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_7
    wclean
    stop music
    play music "Sounds/audio_Bedroom_Fred_Betty_Sex_1.ogg"
    $ renpy.music.set_volume(0.7)
    scene black
    image videov_Bedroom_Fred_Betty_Sex_1_8 = Movie(play="video/v_Bedroom_Fred_Betty_Sex_1_8.mkv", fps=30)
    show videov_Bedroom_Fred_Betty_Sex_1_8
    wclean
    label gallery_8591:
    music Loved_Up2
    $ renpy.music.set_volume(1.0)
    img 8590
    with fade
    w
    img 8591
    with fade
    w
    img 8592
    with fade
    fred "ААААаааааххх!"
    music Groove2_85
    img 8593
    betty "Фред! Не вздумай кончить в меня!"
    img 8594
    with Dissolve(0.5)
    betty "..."
    #fade
    img 8595
    ralph "Бетти!"
    img 8596
    betty "И не вздумай кончить мне на лицо, как в прошлый раз!"
    img 8597
    with fade
    music stop
    ralph "Бетти! Ты где?"
    sound bulk1
    img 8598
    with fade
    fred "ААААаааааххх!"
    #fade
    music Groove2_85
    img 8599
    with fadelong
    betty "!!!"
    img 8600
    fred "..."
    img 8601
    with fade
    betty "..."
    img 8602
    w
    #fade
    img 8603
    with fade
    w
    ralph "Бетти! Ты где?"
    # Кричит в ответ: Ральф, я иду, хватит орать на весь дом!
    # Они спускаются вниз. Фред говорит Ральфу что дверь в комнату Бетти была закрыта и он ждал, пока она закончит макияж.
    # Бетти спрашивает Ральфа зачем он ее звал.
    # Ральф отвечает что едет на важную встречу и хотел чтобы Бетти поцеловала его (Бетти только что была вся в сперме)
    # Бетти решает целовать его или нет. Если целовать, то в губы или в щеку.
    music Pyro_Flow
    img 8604
    with Dissolve(0.5)
    betty "Ральф, я иду!"
    "Хватит орать на весь дом!"
    return

label gallery_9844:
# Бетти уходит на кухню, там к ней приходит Стив и общается с Бетти.
# Стив спрашивает у Бетти как она устроилась, нравится-ли ей город.
# Бетти общается улыбаясь, говорит что завидует Стиву в том что он давно уехал из той провинции, где она жила.
# Стив говорит помнишь-ли старые времена. Говорит что скучал по тебе, малышка Бетти.
# И по твоей сладкой попке.
# Хорошо-ли Бетти ее сохранила. Бетти отвечает что следит за собой.
# Стив снимает штаны и говорит чтобы Бетти скорее показала ему как она следит за собой.
# Секс Стива и Бетти
# Конец сцены.
    img black_screen
    with Dissolve(1.0)
    music Lobby_Time
    sound snd_washing_dishes2
    img 9802
    with fadelong

    w
    img 9803
    with fade
    w
    img 9804
    with fade
    w
    img 9805
    w
    music Groove2_85
    img 9806
    with fade
    betty "Что ты здесь делаешь, Стив?"
    sound highheels_short_walk
    img 9807
    with fade
    betty "Не видишь? У меня много работы по дому."
    music BossaBossa
    img 9808
    with fade
    steve "О! Бетти!"
    "Малышка Бетти!"
    steve "Скажи, как ты устроилась здесь?"
    "Нравится-ли тебе столица?"
    img 9809
    betty "Да, Стив. Мне нравится."
    "Если честно, я завидую тому, что ты давно уехал из нашей провинции и все это время жил здесь, а не там."
    img 9810
    with fade
    steve "Бетти! Но ведь нам есть что вспомнить!"
    steve "Помнишь наши вечеринки у костра?"
    steve "Мы собирались всеми друзьями. Пили и танцевали до утра."
    img 9811
    betty "Помню, Стив. Я думала ты уже забыл."
    betty "Ты ведь теперь такой большой Босс..."
    img 9812
    with fade
    steve "Бетти! У меня есть кое-кто, кто постоянно напоминает о тебе!"
    img 9813
    betty "И кто же это?"
    # Стив достает член
    # Бетти смотрит все время на член

    sound snd_zip
    music Pyro_Flow
    img 9814
    with Dissolve(1.0)
    steve "Вот он, Бетти!"
    "Это мой член!"
    img 9815
    with fade
    "Он все время напоминает о тебе!"
    img 9816
    with diss
    "Он помнит, Бетти!"
    "Он помнит твою попку!"
    img 9817
    with diss
    "Ведь он провел столько времени в ней!"
    img 9818
    with fade
    betty "..."
    img 9819
    with fade
    steve "Скажи, Бетти!"
    "Твоя попка помнит его, так ведь?"
    menu:
        "Да, помнит...":
            pass
        "Я замужем, Стив!":
            img 9821
            betty "Я замужем, Стив!"
            "Пожалуйста, оденься и иди домой!"
            steve "Хорошо, Бетти!"
            "Но я еще вернусь к тебе."
            return

    music Loved_up
    img 9820
    with fade
    betty "Да, помнит..."
    img 9822
    steve "Он скучает по твоей попке, Бетти!"
    "Мне даже пришлось повысить Ральфа, чтобы твоя попка была поближе к моему члену."
    img 9823
    with fade
    betty "Стив, ты ведь знаешь, я теперь замужем за Ральфом."
    img 9824
    "Я люблю его и он мой муж."
    img 9825
    with fade
    steve "Бетти, малышка!"
    "Я не собираюсь жениться на тебе!"
    img 9826
    "Я потратил столько денег, чтобы доставить эту попку сюда!"
    "Скажи, она в такой же форме как и раньше?"
    "Ты хорошо сохранила ее?"
    "Я ведь не буду разочарован?"
    img 9827
    with fade
    betty "Я слежу за собой, Стив."
    "Я регулярно занимаюсь фитнесом и йогой."
    img 9828
    with fade
    steve "Значит Бетти хорошо сохранила свою попку для Стива?"
    "Скорее повернись ко мне задом, покажи ее!"
    "Мой член уже не может, он хочет поскорее попробовать твою попку, вспомнить ее вкус!"
    img 9829
    betty "Стив, я замужем..."
    img 9830
    with fade
    sound Jump2
    steve "Бетти, скажи."
    "Твоей попке не нравилось когда он был внутри нее?"
    menu:
        "Это неважно, Стив! Я замужем!":
            music Pyro_Flow
            img 9837
            with fade
            betty "Это неважно, Стив! Я замужем!"
            return
        "Нравилось...":
            pass
    img 9831
    with fade
    betty "Нравилось..."
    img 9832
    sound Jump1
    steve "И что, твоя попка не хочет, чтобы мой член снова оказался в ней?"
    menu:
        "Хочет...":
            pass
        "Это неважно, Стив! Я замужем!":
            music Pyro_Flow
            img 9837
            with fade
            betty "Это неважно, Стив! Я замужем!"
            return

    img 9833
    with fade
    betty "Хочет..."
    betty "..."
    music Groove2_85
    img 9834
    with diss
    betty "Ой!"
    betty "Стив! Что я сказала?!"
    betty "Я замужем, я не могу заниматься этим с тобой!"
    betty "Я не могу изменять Ральфу..."
    music Loved_up
    img 9835
    with fade
    sound Jump1
    steve "Бетти! Это не измена!"
    steve "Он просто хочет вспомнить твой вкус!"
    img 9836
    with diss
    steve "Это как поцелуй старых друзей!"
    steve "В этом нет ничего плохого!"
    menu:
        "Хорошо, Стив... Только быстро...":
            pass
        "Это неважно, Стив! Я замужем!":
            music Pyro_Flow
            img 9837
            with fade
            betty "Это неважно, Стив! Я замужем!"
            return
    # Бетти снимает трусики
    sound snd_fabric1
    music Loved_up2
    img 9838
    with fade
    betty "Хорошо, Стив... Только быстро..."
    img 9839
    with fade
    w
    img 9840
    with diss
    w
    img 9841
    with diss
    w
    img 9842
    with diss
    w
    img 9843
    with fade
    betty "Стив! Давай быстрее!"
    "Мало времени!"
    img 9842
    with diss
    w
    img 9844
    with Dissolve(0.5)
    betty "Стив! Давай быстрее!"
    music stop
    img black_screen
    with Dissolve(1.0)


    stop music
    play music "Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_1 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_1.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_1
    with fade
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_2 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_2.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_2
    with fade
    steve "О! Бетти! Твоя попка бесподобна!"
    steve "Я так рад, что она теперь поблизости!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_3 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_3.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_3
    with fade
    steve "Я теперь смогу навещать эту попку когда захочу..."
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_4 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_4.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_4
    with fade
    betty "Не получится, Стив!"
    betty "Я не собираюсь изменять Ральфу!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_5 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_5.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_5
    with fade
    steve "О! Бетти!"
    "Малышка Бетти!"
    steve "Тебе не нравится?"
    "Хочешь чтобы я остановился?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_6 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_6.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_6
    with fade
    betty "Нет, Стив. Не останавливайся..."
    betty "Ахххх..."
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_7 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_7.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_7
    with fade
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_8 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_8.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_8
    with fade
    wclean

    # Идет секс

    music Loved_up2
    img 9845
    with fade
    sound bulk1
    steve "АААААрггхххххх!!!!"
    music Pyro_Flow
    img 9846
    with fade
    betty "Черт, Стив!"
    betty "Ты что, кончил в меня?!"

    img 9847
    with fadelong
    steve "Бетти, малышка! Прости, я увлекся..."
    steve "Хе-хе."
    img 9848
    betty "Мне надо скорее помыться и принять таблетку."
    betty "А ты свободен, Стив!"
    music stop


    return

label gallery_10147:
# Идет сцена занятия Бетти с тренером, где он лапает ее по разному.
# Барди подсматривает и снимает на телефон.
# Далее, тренер говорит что одежда мешает ей до конца выгнуть спинку. Снимает лифчик.
# Бетти без лифчика делает упражнения.
# Ноги все еще плохо гнутся. Тренер предлагает Бетти снять одежду и с низа.
# Бетти остается голая. Говорит что ей немного не комфортно.
# Продолжают заниматься.
# Затем тренер раздевается и говорит что Бетти надо немного энергии. Для этого предлагает заняться
# медитацией (сексом)
# Вариант выбора соглашаться или сказать что она замужем.
# Если согласилась, идет секс.

    # Занятие 1
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
#    music Loved_Up
    music Ready_and_Waiting
    img 10142
    with fadelong
    fitness_instructor "Бетти, расслабься."
    "Здесь только мы одни..."
    betty "Хорошо, я постараюсь..."
    img 10143
    fitness_instructor "Делай вот так, выгибай ногу сильнее."
    betty "Я стараюсь..."
    img 10144
    with fade
    fitness_instructor "Я помогу тебе, надо только немного поддержать..."
    img 10145
    betty "Вот так?"
    img 10146
    with fade
    fitness_instructor "Да, тебе надо держать корпус ровнее..."
    "Я помогу тебе..."
    # кладет руку на попу
#    img 10147
#    with diss
#    sound Jump2
#    w
#    img 10149
#    w
#    call photoshop_flash() from _rcall_photoshop_flash_14
#    w
    img 10148
    betty "Хорошо..."

    #Барди
#    music Sneaky_Snitch
#    img 10149
#    with fade
#    bardie "Мне надо продолжать следить за Бетти."
#    bardie "Уверен, что я могу увидеть больше!"
    #

    ######
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    img 10249
    with fadelong
    music Loved_Up
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    betty "Хорошо..."
    return

label gallery_10162:
    # Занятие 2
    # рука уже на попе
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Ready_and_Waiting
    img 10150
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    img 10151
    fitness_instructor "Тебе надо больше выгибать спинку, постарайся..."
    img 10152
    with fade
    betty "Я пытаюсь, у меня не получается выгнуться сильнее..."

    music Loved_Up
    img 10153
    with fadelong
    fitness_instructor "У тебя очень обтягивающая форма."
    img 10154
    fitness_instructor "Она сковывает твои движения."

    img 10155
    with fadelong
    fitness_instructor "Попробуй снять свой верх."
    img 10156
    fitness_instructor "Увидишь, тебе сразу станет свободнее двигаться."
    img 10157
    with fade
    betty "Правда?"
    "Я немного смущаюсь?"

    img 10158
    with fade
    sound Jump1
    fitness_instructor "Бетти, я всего-лишь фитнесс тренер."
    fitness_instructor "Я желаю, чтобы ты добилась результатов."
    img 10159
    fitness_instructor "Доверься мне!"
    betty "Хорошо..."

    #Снимает лифчик
    sound snd_fabric1
    img 10160
    with fade
    w
    img 10161
    with fade
    w
    img 10162
    with fade
    w
#    img 10163
#    sound Jump2
#    bardie "!!!"

    img 10164
    with fade
    w
    call photoshop_flash() from _rcall_photoshop_flash_15
    W

    # Занимается без лифчика
    img 10165
    with fadelong
    fitness_instructor "Вот так, Бетти!"
    img 10166
    "Чувствуешь, как тебе стало свободнее двигаться?"
    "У тебя сразу получилось прогнуть спинку, как следует!"
    img 10167
    "Ты чувствуешь?"

    img 10168
    betty "Да, я действительно выгнулась гораздо сильнее..."

#    img 10173
#    w
    img 10169
    with fade
    w
    call photoshop_flash() from _rcall_photoshop_flash_16
    w
    img 10170
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_17
    w
    img 10171
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_18
    w
    img 10172
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_19
    w

    #Барди
#    music Sneaky_Snitch
#    img 10173
#    with fade
#    bardie "Мне надо продолжать следить за Бетти."
#    bardie "Уверен, что я могу увидеть больше!"

    ############
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Loved_Up
    img 10250
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    betty "Хорошо..."
    return

label gallery_10206:

    # Занятие 3
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Ready_and_Waiting
    img 10174
    with fade
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "Ты помнишь что без верха у тебя лучше результаты."
    img 10175
    betty "Да, помню."
    img 10174
    with fade
    fitness_instructor "Пожалуйста, сними его."
    img 10175
    betty "Хорошо."

    #Бетти снова снимает лифчик
    music Loved_Up
    sound snd_fabric1
    img 10176
    with fade
    w
    #Барди
#    img 10177
#    bardie "!!!"
    img 10178
    with fade
    w
    call photoshop_flash() from _rcall_photoshop_flash_20
    w
    img 10179
    with fadelong
    fitness_instructor "Молодец."
    fitness_instructor "Теперь тяни ножку, тяни сильнее..."
    img 10180
    betty "Я не могу, мне дальше никак..."
    fitness_instructor "Тебе больно, Бетти?"
    betty "Нет, мне уже не больно..."
    "Она... Она просто не гнется дальше и все..."
    img 10181
    betty "У меня не получается!"
    with diss
    img 10182
    with fade
    fitness_instructor "Бетти, я знаю что тебе мешает..."
    fitness_instructor "Я знаю что тебе мешает добиться лучших результатов..."
    img 10181
    betty "Что же?"
    img 10183
    with fade
    fitness_instructor "Твой низ, Бетти!"
    fitness_instructor "Он слишком обтягивает тебя, сковывает твои движения!"
    img 10184
    fitness_instructor "Твои связки могут позволить тебе сделать упражнение как надо."
    fitness_instructor "Но твоя одежда не позволяет тебе сделать это."
    img 10185
    with fade
    betty "Что же делать с этим?"
    img 10186
    fitness_instructor "Ты можешь снять с себя это, Бетти."
    betty "Но я... Стесняюсь..."
    img 10187
    with fadelong
    sound Jump1
    fitness_instructor "Бетти, я твой инструктор!"
    img 10188
    fitness_instructor "Я провожу персональные занятия с тобой."
    fitness_instructor "Я делаю это бесплатно, потому что вижу в тебе потенциал!"
    img 10189
    betty "Правда? У меня есть потенциал?"
    fitness_instructor "Да, Бетти!"
    fitness_instructor "Ты прекрасна!"
    img 10190
    with fade
    fitness_instructor "Доверься мне! Я лишь хочу чтобы у тебя получалось!"
    fitness_instructor "Я хочу чтобы ты была успешной!"
    img 10191
    with fade
    betty "Хорошо, только..."
    img 10192
    with diss
    betty "Я ведь правда не толстая?"
    img 10193
    with diss
    fitness_instructor "Бетти, ты прекрасна! Тебе не стоит стесняться своего тела!"
    img 10194
    with fade
    betty "Хорошо..."
    # Бетти раздевается полностью
    music Loved_Up2
    sound snd_fabric1
    img 10195
    with fadelong
    w
    img 10196
    with Dissolve(0.5)
    w
#    img 10197
#    with fade
#    bardie "..." #Улыбается
    img 10198
    with Dissolve(0.5)
    w
    call photoshop_flash() from _rcall_photoshop_flash_21
    w
    img 10199
    w
    img 10200
    with diss
    w
    img 10201
    with Dissolve(0.5)
    w
    img 10202
    with Dissolve(0.5)
    w
    call photoshop_flash() from _rcall_photoshop_flash_22
    w
    img 10203
    with fade
    betty "Так хорошо?"
    call photoshop_flash() from _rcall_photoshop_flash_23
    w
    fitness_instructor "Да, Бетти. Давай продолжим."
    img 10204
    with fadelong
    #Занимается обнаженной
    fitness_instructor "Вот так, Бетти!"
    img 10205
    fitness_instructor "У тебя получается, ты чувствуешь?"
    img 10206
    with fade
    betty "Да, я правда смогла поднять ногу выше..."
    call photoshop_flash() from _rcall_photoshop_flash_24
    w
    img 10207
    with diss
    fitness_instructor "Отлично!"
    fitness_instructor "Ты чувствуешь себя свободной?"
    img 10208
    with diss
    betty "Да..."
    call photoshop_flash() from _rcall_photoshop_flash_25
    w

    img 10209
    fitness_instructor "Тебе комортно, ты больше не стесняешься меня?"
    img 10210
    betty "Да, мне очень комфортно..."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Loved_Up
    img 10211
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    return

label gallery_10245:
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Ready_and_Waiting
    # Занятие 4
    img 10212
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "Ты помнишь что одежда сковывает тебя?"
    img 10213
    betty "Да, помню..."
    img 10214
    fitness_instructor "Если ты хочешь, ты можешь снять ее."
    fitness_instructor "Тогда мы сможем достичь большего прогресса."
    img 10213
    betty "Хорошо..."
    #Снимает одежду

    sound snd_fabric1
    music Loved_Up
    img 10215
    with fade
    w
#    img 10216
#    with fade
#    w
    img 10217
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_26
    w
    img 10218
    with diss
#    sound kiss2
    w
    call photoshop_flash() from _rcall_photoshop_flash_27
    w
    img 10219
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_28
    w
    img 10220
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_29
    w
    img 10221
    with fade
    w
    call photoshop_flash() from _rcall_photoshop_flash_30
    w
    sound snd_fabric1
    img 10223
    with fade
    w
    img 10222
    with fade
    w
    img 10224
    with fade
    w
    #Барди
#    img 10225
#    w
#    call photoshop_flash() from _rcall_photoshop_flash_31
#    w


    img 10226
    with fadelong
    fitness_instructor "Теперь тянись, тянись как можешь..."
    betty "..."
    img 10227
    with fade
    fitness_instructor "Вот так, хорошо..."
    fitness_instructor "Давай, ты можешь еще, я знаю."
    img 10228
    betty "Мне никак!"
    betty "Я стараюсь!"
    img 10229
    fitness_instructor "Бетти, ты слишком напряжена, ты чувствуешь это?"
    betty "Да, я чувствую..."
    fitness_instructor "Тебе надо расслабиться, Бетти."
    img 10230
    betty "Но как это сделать?"
    betty "Я волнуюсь, я хочу чтобы у меня получалось..."
    img 10231
    with fade
    fitness_instructor "Тебе нужно пройти сеанс медитации, Бетти."
    fitness_instructor "Тогда ты сможешь расслабиться и у тебя все получится."
    img 10230
    betty "Но как? Я не умею медитировать."
    img 10231
    fitness_instructor "Хочешь чтобы я показал тебе как это надо делать?"
    img 10232
    betty "Да, очень хочу..."

    # тренер встает и раздевается
    music Loved_Up2
    sound snd_fabric1
    img 10234
    with fadelong
    w
    fitness_instructor "Я буду твоим проводником, Бетти."
    img 10233
    fitness_instructor "Твоим проводником на пути к достижению душевного равновесия."
    # обнимает Бетти и лапает за попу
    img 10235
    with fade
    sound Jump1
    fitness_instructor "Я проведу тебя через весь путь."
    img 10236
    with diss
    sound Jump2
    fitness_instructor "Ты поймешь что такое настоящий Дзен..."
    call photoshop_flash() from _rcall_photoshop_flash_32
    w

#    img 10238
#    bardie "!!!" #довольный фоткает
    img 10236
    w
#    img 10237
#    w
#    call photoshop_flash() from _rcall_photoshop_flash_33
#    w

    img 10239
    with fade
    fitness_instructor "Ты хочешь этого?"
#    img 10240
#    with fade
    menu:
        "Да, я очень хочу...":
            pass
        "Я хочу, но не таким путем. Я замужем!":
            music Groove2_85
            img 10241
            with fade
            betty "Я хочу, но не таким путем. Я замужем!"
            betty "А это выглядит как измена!"
            img 10242
            fitness_instructor "..."
            img 10243
            with fade
            betty "Я оденусь и мы продолжим."
            betty "Я уверена, что смогу добиться успеха не прибегая к медитациям..."
            fitness_instructor "Хорошо, Бетти..."
            return

    img 10244
    with fade
    w
    img 10245
    with fade
    w
    img 10246
    with diss
    betty "Да, я очень хочу..."
    img 10247
    with fadelong
    fitness_instructor "Тогда начнем!"
    img 10248
    fitness_instructor "Расслабься и чувствуй меня!"

    #идет секс
    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_1 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_1.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_1
    show screen camera_record_screen()
    fitness_instructor "Чувствуй меня, следуй за мной!"
    betty "Да! Хорошо!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_2 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_2.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_3 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_3.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_4 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_4.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_5 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_5.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_5
    fitness_instructor "Ты чувствуешь меня?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_6 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_6.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_7 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_7.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_7
    wclean

    music stop
    img black_screen
    hide screen camera_record_screen
    with Dissolve(1.0)
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_1 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_1.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_1
    show screen camera_record_screen()
    with fadelong
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_2 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_2.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_3 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_3.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_3
    fitness_instructor "Ты чувствуешь как тебя заполняет энергия равновесия?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_4 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_4.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_5 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_5.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_6 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_6.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_6
    fitness_instructor "Ты чувствуешь прилив энергетических сил?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_7 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_7.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_7
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_8 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_8.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_9 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_9.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_10 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_10.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_10
    wclean


#############

    music stop
    img black_screen
    hide screen camera_record_screen
    with Dissolve(1.0)
    pause 1.0
    stop music
    play music "Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_1 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_1.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_1
    show screen camera_record_screen()
    with fadelong
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_2 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_2.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_2
    fitness_instructor "Ты следуешь за мной по дороге к Дзен?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_3 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_3.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_4 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_4.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_5 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_5.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_5
    fitness_instructor "Тебе нравится эта медитация?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_6 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_6.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_6
    fitness_instructor "Очень нравится?"
    betty "Да, очень!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_7 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_7.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_7
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_8 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_8.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_9 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_9.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_10 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_10.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_10
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_11 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_11.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_11
    wclean

    hide screen camera_record_screen
######
    music stop
#    music Power_Bots_Loop
#    call gallery_10245_1() from _rcall_gallery_10245_1
#    music stop
    img black_screen
    with Dissolve(1.0)
    pause 2.0

    return

label gallery_10245_1:
    return

label gallery_20385:

# К сценам контракта со Стивом добавляется сцена, где Бетти приходит к нему.
# Только вторник и четверг (посещение фитнеса)
# Бетти заходит.
# Если первый раз:
# Заходит с Джейн
# Стив удивлен, здоровается с Бетти.
# Говорит что удивлен увидеть ее здесь
# Бетти говорит что Ральф заболел и остался дома, но ему нужно передать отчеты для Стива.
# Ральф очень переживает из-за того что отчеты окажутся у Стива невовремя.
# Поэтому он послал Бетти для того, чтобы отвезти их.
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_20
    scene black_screen
    with Dissolve(1)
    music Loved_Up

    music Groove2_85
    img 12666
    with fadelong
    jane "Мистер Стив, к Вам пришла некая Миссис Робертс."
    jane "Она говорит что пришла от Мистера Ральфа."
    img 12667
    with diss
    jane "Также она говорит что Вы ее знаете..." # Смотрит прищюренно и подозрительно
    img 12668
    with diss
    steve "..."
    img 12669
    with diss
    jane "!!!"
    img 12670
    with fadelong
    jane "Она говорит что ее супруг заболел и остался дома, а она привезла Вам его отчеты."
    img 12671
    with diss
    steve "Ах, Бетти..."
    steve "Да, Джейн! Я знаю ее."
    img 12673
    with diss
    steve "Это супруга Ральфа, он работает в нашей компании."
    steve "Ты должна быть знакома с ним."
    img 12674
    jane "..."
    img 12673
    steve "..."
    img 12675
    with fade
    steve "Бетти!"
    steve "Разве у Стива нет подчиненных, чтобы доставить отчеты?"
    steve "К чему заставлять себя ехать через весь город?"
    img 12676
    with diss
    betty "Ральф взял их с собой домой, чтобы проверить их и привезти сегодня тебе."
    img 12677
    with fade
    steve "Бетти, у Вас есть отличная гувернантка!"
    steve "Ты бы могла поручить это ей!"
    img 12678
    with fade
    betty "Если ты говоришь про ту нерадивую гувернантку, которую Ральф откуда-то подобрал..."
    betty "То я не доверяю ей даже стирать одежду и готовить еду!"
    img 12679
    with diss
    steve "Правда? А мне показалось, что ей можно доверить самое ценное что у меня есть..."
    # Моника смотрит на член Стива и злится
    img 12680
    with diss
    w
    img 12681
    with fade
    betty "Стив, это мое дело, кому доверять, а кому нет!"
    betty "Я пришла для того, чтобы передать отчеты!"
    betty "Я согласилась на это только потому, что сегодня посещала фитнес в городе."
    img 12682
    betty "И нашла минуту, чтобы помочь моему супругу."
    betty "Вот отчет, Стив!"
    betty "А я поехала назад к своему мужу!"
    img 12683
    with fade
    steve "Бетти, постой!"
    steve "Джейн, все в порядке, ты можешь идти."
    steve "Сейчас я проверю отчеты и отпущу Миссис Робертс."
    img 12684
    with diss
    jane "Хорошо, Мистер Стив."
    jane "Позовете меня, если что-то потребуется."

    # Джейн уходит
    img 12686
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 12685
    with fadelong
    betty "Что тебе надо, Стив?!"
    betty "Я принесла отчеты и уже тороплюсь!"

    # Стив встает, у него спущены штаны и стоит член
    music Loved_Up
    img 12687
    with diss
    sound Jump2
    steve "Ах, Бетти!"
    steve "Моя любимая Бетти!"
    steve "Я так рад что ты пришла ко мне!"
    music Groove2_85
    img 12688
    with diss
    betty "Стив, почему ты без штанов?!"
    music Loved_Up
    img 12689
    with fade
    steve "Я ждал тебя, Бетти! Я так ждал тебя!"
    music Groove2_85
    img 12690
    with diss
    betty "Стив, надень штаны!"
    betty "Или я ухожу!"
    music Loved_Up
    img 12691
    with fade
    steve "Бетти, ты не можешь уйти!"
    steve "Посмотри!"
    img 12692
    with diss
    steve "Посмотри, как я соскучился по тебе!"
    steve "Неужели ты не видишь, Бетти?"
    img 12693
    with fade
    w
    img 12707
    with diss
    w
    img 12708
    with diss
    betty "..."
    img 12694
    with fade
    steve "..."
    music Groove2_85
    img 12695
    with fade
    betty "Стив, я тороплюсь!"
    img 12696
    steve "Бетти, подойди ко мне!"
    steve "Подойди ко мне поближе, скорее, Бетти!"
    img 12708
    with fade
    menu:
        "Взять член Стива.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 12694
            with fade
            betty "Стив, я не понимаю, чего ты от меня хочешь?"
            betty "Я же ясно сказала тебе, что тороплюсь!"
            music stop
            img black_screen
            with diss
            sound snd_door_close1
            pause 2.0
            call gallery_20385_1() from _rcall_gallery_20385_1_5 # Стив кончает
            call gallery_20385_2() from _rcall_gallery_20385_2_6 # Моника уходит
            return

    # Бетти подходит и берет Стива за член
    music stop
    img black_screen
    with diss
    pause 0.5
    music Groove2_85
    img 12697
    with fadelong
    betty "Стив, я не понимаю, чего ты от меня хочешь?"
    betty "Я же ясно сказала тебе, что тороплюсь!"
    img 12709
    with diss
    w
    img 12710
    mt "!!!"
    img 12698
    with diss
    betty "Меня дома ждет муж!"
    music Loved_Up
    img 12699
    steve "Ах, Бетти!"
    steve "Я хочу тебя! Хочу твою попку!"
    img 12711
    with diss
    w
    img 12712
    w
    img 12700
    with fade
    steve "Мысль о том, что ты только что тренировала ее на фитнесе, возбуждает меня!"
    # Стив задирает юбку Бетти
    sound Jump1
    img 12701
    steve "Ты тренировала ее для меня!"
    steve "Для моего члена!"
    img 12713
    with diss
    w
    img 12714
    w
    img 12702
    with diss
    steve "Для того, чтобы я вогнал его в твою попку!"
    steve "В твою аппетитную попку, Бетти!"
    img 12703
    betty "..."
    img 12715
    with fade
    w
    img 12716
    with diss
    w
    music Groove2_85
    img 12704
    with fade
    betty "Я не хочу изменять мужу, Стив!"
    music Loved_Up
    img 12705
    with diss
    steve "Скорее! Cкорее, Бетти, повернись!"
    steve "Дай я вгоню в тебя свой член!"
    img 12717
    with fade
    steve "Это не измена, Бетти!"
    img 12718
    with diss
    steve "Это, всего-лишь, акт старой дружбы!"
    music Groove2_85
    img 12706
    with diss
    betty "!!!"
    betty "..."
    menu:
        "Ладно, Стив. Только быстро!":
            pass
        "Уйти.":
            music Power_Bots_Loop
            betty "Стив, я не понимаю, чего ты от меня хочешь?"
            betty "Я же ясно сказала тебе, что тороплюсь!"
            music stop
            img black_screen
            with diss
            sound snd_door_close1
            pause 2.0
            call gallery_20385_1() from _rcall_gallery_20385_1_6 # Стив кончает
            call gallery_20385_2() from _rcall_gallery_20385_2_7 # Моника уходит
            return
    # Бетти снимает трусы
    music Loved_Up
    sound snd_fabric1
    img 12719
    with fade
    betty "Ладно, Стив."
    img 12720
    with diss
    w
    img 12721
    with diss
    betty "Только быстро!"
    img 12722
    w
    img 12723
    with diss
    betty "Меня дома ждет муж!"
    # бросает их перед Моникой возле стола
    img 12724
    with diss
    w
    music Groove2_85
    img 12725
    with fade
    betty "Стив, куда мне деть мои трусики?"
    img 12726
    with diss
    w
    img 12727
    with diss
    steve "Бетти, давай их сюда!"
    img 12728
    w
    sound Jump1
    img 12729
    with diss
    w
    mt "Знакомые трусики..."
    mt "Черт! Это точно сучка Бетти!"
    img 12730

    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up2
    img 20379
    with fadelong
    betty "Ты куда залез, Стив?!"
    #video
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_1 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_1.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_1
    with fadelong
    wclean
    music Loved_Up2
    img 20380
    with fade
    steve "Да, Бетти! Да!"
    w
    img 20382
    with diss
    betty "Ай!!!"
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_2 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_2.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_2
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_3 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_3.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_3
    with fadelong
    wclean
    music Loved_Up2
    img 20381
    with fade
    steve "В твою попку, Бетти!"
    steve " Я так давно хотел тебя трахнуть в попку!"
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_4 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_4.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_4
    with fadelong
    wclean
    music Loved_Up2
    img 20383
    with fade
    betty "Мне больно!"

    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_5 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_5.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_5
    with fadelong
    steve "Твоя попка, Бетти!"
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_6 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_6.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_6
    with fadelong
    steve " Мне нравиться трахать тебя в твою дырочку!"
    wclean

    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_7 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_7.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_7
    with fadelong
    steve "Она бесподобна!"
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_SteveOffice_Steve_Betty_Anal_1.mp3"
    scene black
    image videov_SteveOffice_Steve_Betty_Anal_1_8 = Movie(play="video/v_SteveOffice_Steve_Betty_Anal_1_8.mkv", fps=30)
    show videov_SteveOffice_Steve_Betty_Anal_1_8
    with fadelong
    steve "Я хочу кончить в нее"
    wclean
    music stop
    img black_screen
    with diss
    pause 1.0
    sound bulk1
    steve "ААААААААХХХ!"

    music Groove2_85
    img 20384
    with fadelong
    if bettySteveKitchenSex == True:
        betty "Черт, Стив! Ты снова кончил в меня?!"
        img 20385
        with diss
        mt "Снова?!"
    else:
        betty "Черт, Стив! Ты кончил в меня?!"


    img 20386
    with diss
    steve "Бетти, это всего-лишь твоя попка!"
    img 20387
    with diss
    steve "Не волнуйся!"

    img 20388
    with fade
    mt "Дьявол! Эта Бетти совсем обнаглела!"
    mt "Она смеет трахаться прямо в кабинете у Стива!"
    mt "Да еще и при мне!"

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    # Бетти одевает трусы
    img 13187
    with fadelong
    betty "Все, Стив!"
    betty "Я пошла!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    # fade
    img 12731
    with fadelong
    m "Стив! Ты совсем обнаглел!"
    m "Ты трахаешь шлюх прямо у меня на глазах!"
    img 12732
    m "Ты поплатишься за такую наглость!"
    m "Я... Я!!!"
    music Loved_Up
    img 12733
    with fade
    steve "Моника, я знаю, ты собираешься убить меня..."
    music Power_Bots_Loop
    img 12734
    with diss
    m "Я не просто убью тебя, Стив!"
    m "Я сделаю это с особой жестокостью!"
    img 12735
    m "Я сделаю тебя ничтожеством! Ты будешь побираться на улицах до конца своих никчемных дней!"
    music Groove2_85
    img 12736
    with fade
    steve "Моника, но за что?!"
    steve "Я честный бизнесмен! Я облегчил тебе выполнение контракта!"
    img 12737
    steve "Вместо того, чтобы кончить в твой ротик, я кончил в зад другой женщины."
    steve "Или ты хочешь, чтобы я отдал эти деньги ей?"
    music Power_Bots_Loop
    img 12738
    with diss
    m "ЭТО МОИ ДЕНЬГИ! МОИ!!!"
    music Groove2_85
    img 12739
    with fade
    steve "Но ты нарушила условия сделки! Моя сперма только что ушла отсюда!"
    steve "Сделка не закрыта!"
    music Power_Bots_Loop
    img 12740
    with diss
    m "Как, по твоему, я могла закрыть эту сделку?!"
    m "Ты кончил в задницу этой шлюхи!"
    img 12741
    m "Ты сделал это сам!"
    music Groove2_85
    img 12742
    with fade
    steve "Моника, сперма очень долго висела перед твоим лицом, я видел это!"
    steve "У тебя были все возможности проглотить ее!"

    # выбор:
    # уйти без денег или наехать на Стива. В зависимости от сучности
    music Power_Bots_Loop
    img 12743
    with fade
    w
    menu:
        "Уйти без денег.":
            # Если уходит без денег
            img 12744
            with fadelong
            m "Ты мерзавец, Стив!"
            return False
        "Разозлиться на Стива.":
            pass

    # Наехать на Стива
    # Моника злая, подходик к Стиву
    # +bitchiness
    music stop
    img black_screen
    with diss
    pause 1.0
    music Pyro_Flow
    img 12745
    with fadelong
    m "Стив..."
    m "Повтори еще раз..."
    img 12746
    with diss
    m "Значит ты..."
    m "Хотел..."
    img 12747
    with diss
    m "Чтобы я проглотила твою гребаную сперму..."
    m "Сперму, которая..."
    img 12748
    with fade
    m "Вытекла из задницы Бетти?!"
    img 12749
    with diss
    steve "..."
    # Моника берет Стива за яйца
    sound Jump2
    img 12750
    with diss
    m "Кажется, моему терпению пришел конец, Стив!"
    m "Мне неважно что со мной будет. Я убью тебя и оторву твои яйца..."
    img 12751
    steve "Моника! Контракт закрыт!"
    steve "Пожалуйста! Я же пошутил!"
    img 12752
    w
    img 12753
    with diss
    m "Еще раз пошути так, Стив..."
    m "И останешься без своих яиц..."
    m "Тебе понятно?!"
    img 12754
    with fade
    steve "Да, Моника! Пожалуйста!"
    steve "Успокойся! Не надо злиться!"
    img 12755
    steve "Отпусти мои... Отпусти меня и я переведу деньги немедленно!"
    # Моника разжимает руку
    music Groove2_85
    sound Jump1
    img 12756
    with diss
    w
    img 12757
    with fade
    m "Я отпустила твои яйца, Стив..."
    img 12758
    with diss
    steve "..."
    img 12759
    with fade
    m "На этот раз..."
    # Моника уходит
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 12760
    with fadelong
    m "Но не расчитывай на это снова!"
    return

label gallery_20385_1:
    # Стив кончает
    music Loved_Up2
    img 11712
    with fadelong
    sound bulk1
    steve "АААААААААААРГХХХХХ!!!"
    img 11713
    with diss
    w
    img 11714
    sound bulk1
    with diss
    w
    return

label gallery_20385_2:
    # Моника стоит перед Стивом после сцены blowjob
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11715
    with fadelong
    m "Тьфу!"
    mt "Мерзость!"

    music Power_Bots_Loop
    img 11716
    with fadelong
    m "Доволен, Стив?!"
    img 11717
    with diss
    m "Мы закрыли контракт!"
    if monicaSteveContractPenaltyActive == True:
        $ monicaSteveContractPenaltyActive = False
        call gallery_20385_3() from _rcall_gallery_20385_3
    else:
        img 11718
        with diss
        steve "Да, Моника, деньги ушли."

    img 11719
    with fade
    m "Стив, ты мерзавец и изменник!"
    music Groove2_85
    img 11720
    with diss
    steve "Моника, не будь так категорична!"
    steve "Давай это будет нашим маленьким секретом!"
    img 11721
    with diss
    steve "Ты сохранишь его со своей стороны."
    steve "А я со своей..."
    music Power_Bots_Loop
    img 11722
    with fade
    m "!!!"
    m "Подонок! Только попробуй кому-нибудь рассказать про это!"

    img 11723
    with diss
    steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
    steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
    m "!!!"
    return
#

# В конце Стив говорит что неустойка компенсирована сполна.
# Что Стив ждет Монику для новых контрактов.
label gallery_20385_3:
    music Groove2_85
    img 12665
    with fadelong
    steve "Неустойка компенсирована сполна."
    steve "Я жду тебя для новых контрактов, Моника!"
    return

############ ClothingShop 1############


label gallery_10667:

    music Groove2_85
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
            return
        "Ударить продавца и убежать! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass
        "Умолять не вызывать полицию...":
            return

label gallery_10698:
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
    call photoshop_flash() from _rcall_photoshop_flash_34
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
    menu:
        "Согласиться работать манекеном.":
            music Hidden_Agenda
            img 10735
            with fade
            m "Я... Я согласна..."
            cashier "Приходи завтра днем!"
            cashier "Сегодня посетителей уже не будет!"
            return
        "Отказаться.":
            music Hidden_Agenda
            img 10736
            with fade
            m "Я... пока не готова..."
            cashier "Если надумаешь, приходи!"
            return
    return

label gallery_10819:
    # Ухотят и моника заходит в примерочную
    music Groove2_85
    img 10782
    with fadelong
    cit4 "Насколько я знаю, в примерочные не разрешается заходить сотрудникам!"
    # corruption +1 req 80
    menu:
        "Ну я не совсем сотрудник...":
            pass
        "Она права, а если так, то мне не передать ей платье.":
            return
    m "Ну я не совсем обычный сотрудник."
    m "Я... Я работаю здесь манекеном."
    m "И я помогу Вам одеться."
    label gallery_10792:
    music Loved_Up
    img 10783
    with fadelong
    cit4 "Эм... Ну ладно."
    img 10784
    with diss
    m "..."
    img 10785
    with diss
    cit4 "Ну же? Я жду!"
    m "!!!"
#    img 10787
#    w
    img black_screen
    with diss
    pause 1.0
    sound snd_fabric1
    img 10788
    with fadelong
    w
    img 10789
    with diss
    w
    img 10786
    with diss
    w
    # моника снимает платье клиент одевает
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    img 10790
    with fadelong
    cit4 "Ну как мне?"
    m "Вам очень идет!"
    cit4 "Правда? Вроде бы неплохо, но я не уверена..."
    img 10791
    with diss
    m "Да нет же, все прекрасно!"
    img 10792
    with fade
    cit4 "Мне нужно подумать, одну секундочку..."
    img 10793
    with diss
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 10794
    with fadelong
    cit4 "Хорошо, я куплю его, пойду на кассу!"
    m "Подождите!"
    music Power_Bots_Loop
    img 10795
    with fade
    mt "Дьявол! А как же Я?"
    mt "Как же мне отсюда выйти?"
    mt "У меня нет одежды!"
    img 10796
    with diss
    mt "Может одеть тряпки этой покупательницы?"
    mt "Она забрала их!"
    # Моника выглядывает
    img 10797
    with fade
    mt "Где же она?"

    music stop
    call textonblack(t_("Спустя некоторое время...")) from _rcall_textonblack_21
    img black_screen
    with Dissolve(1)
    music Groove2_85
    # Проходит время
    img 10798
    with fadelong
    cashier "Эй! Что ты здесь делаешь?"
    cashier "Работникам нельзя занимать примерочную!"
    img 10799
    with diss
    cashier "И кто будет продавать это платье?!"
    cashier "Ты захотела в полицию, воришка?!"
    cashier "Быстро работать!"
    img 10800
    with fade
    m "Покупатель ушла на кассу."
    m "Она должна была купить платье"
    img 10801
    with diss
    cashier "Никто не подходил к кассе!"
    cashier "Иди и ищи эту покупательницу, иначе я посчитаю что ты украла платье!"

    img 10802
    with fade
    mt "!!!"
    m "Могли бы Вы найти ее?"
    m "Я... Не совсем одета..."

    music Loved_Up
    img 10803
    with fadelong
    cashier "Я могу привести ее сюда..."
    img 10804
    with diss
    m "..."
    img 10805
    with fade
    cashier "Если ты пососешь мне сосок..."
    # Показывает грудь
    music Power_Bots_Loop
    img 10806
    with fade
    m "!!!"
    img 10807
    with diss
    w
    img 10808
    with diss
    mt "Эта лесбиянка уже достала меня!"
    mt "Когда я верну свою жизнь назад, я закрою этот магазин и уволю ее к чертовой матери!"
    music Groove2_85
    img 10809
    with fade
    cashier "Ну?"
    cashier "Или ты хочешь идти в зал искать ее сама?"
    img 10810
    with fade
    menu:
        "Пососать сосок...":
            mt "Я не хочу этого делать!"
            mt "Мне, Монике Бакфетт!"
            mt "Лизать сосок у какой-то продавщицы-лесбиянки!"
            mt "Как могло до такого дойти?!"
            img 10811
            with fade
            mt "И для чего!"
            mt "Для того, чтобы не идти голой по магазину."
            mt "Не искать покупательницу, которая ходит в моем же платье!"
            mt "Чтобы уговорить ее купить его."
            mt "Купить, для того, чтобы больше не работать манекеном и получить хоть какую-то приличную одежду!"
            img 10810
            with fade
            mt "Моника, какой ужас!"
            mt "..."
            mt "Похоже мне придется преодолеть себя и сделать это."
            mt "Моника, представь что это происходит не с тобой..."
            # лижет сосок
            music Loved_Up
            img 10812
            with fade
            w
            img 10813
            with diss
            w
            img 10814
            with diss
            w
            img 10815
            with diss
            w
            #лижет
            music2 audio_LickingNipple
            img 10816
            with diss
            w
            img 10817
            with diss
            w
            img 10818
            with diss
            w
            img 10819
            with diss
            w
            img 10820
            with diss
            w
            img 10821
            with diss
            w
            img 10822
            with diss
            w
            img 10823
            with diss
            w
            music2 stop
            music Groove2_85
            img 10824
            with fade
            cashier "Молодец, хорошая девочка."
            img 10825
            with diss
            cashier "А теперь пососи второй..."
            img 10826
            with fade
            w
            img 10827
            with diss
            cashier "Давай, воришка, исправляйся..."
            img 10828
            with fade
            mt "!!!"
            img 10829
            with diss
            cashier "Ну же, девочка... Поспеши..."
            img 10830
            with fade
            menu:
                "Пососать сосок...":
                    # лижет второй сосок
                    label gallery_10832:
                    music Loved_Up
                    music2 audio_LickingNipple
                    img 10831
                    with fadelong
                    w
                    img 10832
                    with diss
                    w
                    img 10833
                    with diss
                    w
                    img 10834
                    with diss
                    w
                    music2 stop
                    music Groove2_85
                    img 10835
                    with fade
                    cashier "Хорошая девочка..."
                    # приводит покупателя
                    music stop
                    call textonblack(t_("Спустя некоторое время...")) from _rcall_textonblack_22
                    img black_screen
                    with Dissolve(1)
                    music Groove2_85
                    img 10836
                    with fadelong
                    cit4 "Я передумала покупать это платье!"
                    cit4 "Оно неподходит под цвет моих туфель!"
                    img 10837
                    with diss
                    cit4 "Пожалуйста, помогите мне переодеться назад."
                    music Power_Bots_Loop
                    img 10838
                    with fade
                    mt "!!!"
                    return 1
                "Идти в зал искать покупательницу...":
                    music Power_Bots_Loop
                    img 10839
                    with fade
                    m "Я пойду и поищу покупательницу сама!"
                    img 10840
                    with diss
                    cashier "Как хочешь..."
                    cashier "Но я запрещаю тебе одевать что-то кроме этого платья."
                    cashier "До конца рабочей смены."
                    img 10841
                    with fade
                    m "Я не собираюсь слушаться тебя!"
                    cashier "Тогда ты отправишься в полицию!"
                    img 10842
                    with fade
                    m "Ты ничего не докажешь!"
                    m "Это было несколько дней назад!"
                    music Groove2_85
                    sound snd_phone2
                    img 10843
                    with fadelong
                    cashier "Так я звоню в полицию, ты не против?"
                    img 10844
                    with diss
                    m "!!!"
                    music Hidden_Agenda
                    img 10845
                    with fade
                    m "Не надо звонить в полицию..."
                    m "Я сделаю как ты хочешь..."
                    mt "Я УБЬЮ ТЕБЯ ПОТОМ, КЛЯНУСЬ!!!"
                    music stop
                    img black_screen
                    with diss
                    pause 2.0
                    return

#            cashier "Хорошо."
#            cashier "Сейчас я принесу тебе платье."
            return
        "Идти в зал искать покупательницу...":
            music Power_Bots_Loop
            img 10839
            with fade
            m "Я пойду и поищу покупательницу сама!"
            img 10840
            with diss
            cashier "Как хочешь..."
            cashier "Но я запрещаю тебе одевать что-то кроме этого платья."
            cashier "До конца рабочей смены."
            img 10841
            with fade
            m "Я не собираюсь слушаться тебя!"
            cashier "Тогда ты отправишься в полицию!"
            img 10842
            with fade
            m "Ты ничего не докажешь!"
            m "Это было несколько дней назад!"
            music Groove2_85
            sound snd_phone2
            img 10843
            with fadelong
            cashier "Так я звоню в полицию, ты не против?"
            img 10844
            with diss
            m "!!!"
            music Hidden_Agenda
            img 10845
            with fade
            m "Не надо звонить в полицию..."
            m "Я сделаю как ты хочешь..."
            mt "Я УБЬЮ ТЕБЯ ПОТОМ, КЛЯНУСЬ!!!"
            music stop
            img black_screen
            with diss
            pause 2.0
            return
    return

label gallery_10864:
    # Моника подходит к продавщице
    music Power_Bots_Loop
    sound highheels_short_walk
    img 10851
    with fadelong
    m "Она не отдает платье!"
    m "Эта сучка ходит в нем по магазину!"
    m "Я сейчас схвачу ее за волосы и заставлю снять это платье!"
    music Groove2_85
    img 10852
    with fade
    cashier "Не смей грубить клиентам магазина!"
    img 10853
    with diss
    m "!!!"
    img 10854
    with diss
    w
    img 10855
    with diss
    w
    img 10856
    with diss
    cashier "Так что ты от меня хочешь?"
    music Power_Bots_Loop
    img 10857
    with fade
    m "Если ты не хочешь, чтобы я убила ее прямо здесь, то скажи ей переодеться назад!"
    music Groove2_85
    img 10858
    with fade
    cashier "Если хочешь, чтобы я тебе помогла, то перестань закрываться руками."
    cashier "Манекен не должен ничего прятать."
    music Power_Bots_Loop
    img 10859
    with fade
    m "!!!"
    cashier "Ну же?"
    menu:
        "Убрать руки и встать прямо.":
            # моника встает прямо
            music Groove2_85
            img 10861
            with fadelong
            w
            img 10862
            with diss
            m "Довольна?!"
            m "Теперь пойдем к этой чертовой покупательнице!"
            music stop
            img black_screen
            with diss
            pause 2.0
            music Groove2_85
            img 10863
            with fadelong
            cashier "Мэм, можно Вас на минутку?"
            cit4 "Да, конечно..."
            # Подходят к покупательнице, Моника стоит прямо

            music stop
            img black_screen
            with diss
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            img 10864
            with fadelong
            cashier "Мэм, если Вы не будете покупать платье..."
            cashier "То, пожалуйста, верните его на манекен."
            img 10865
            with diss
            cit4 "Я не буду покупать это платье."
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            img 10866
            with fadelong
            cit4 "До свидания."
            cashier "Да, Мэм. Возвращайтесь! Мы всегда рады Вам."
            music Power_Bots_Loop
            img 10867
            with fade
            if monicaBitch == True:
                mt "СУЧКА!!!"
                mt "НЕНАВИЖУ!!!"
            else:
                mt "!!!"
            return

        "Отказаться.":
            music Power_Bots_Loop
            img 10860
            with fade
            m "Я не буду этого делать, гребаная лесбиянка!"
            m "Я знаю что у тебя на уме!"
            return
    return

label gallery_10902:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10880
    with fadelong
    m "Добрый день, Девушка."
    m "Можно к Тебе обратиться?"
    img 10881
    with fade
    cit5 "Да..."
    img 10882
    with fade
    m "Ну что, ты взяла с собой деньги сегодня?"
    img 10883
    with fade
    cit5 "Да..."
    img 10884
    with fade
    m "Покажи их..."
    img 10885
    with diss
    w
    img 10886
    with fade
    w
    sound Jump1
    img 10887
    with diss
    # Девушка задирает юбку и показывает киску
    w
    music Groove2_85
    img 10888
    m "ЭТО ЧТО ЕЩЕ?!"
    img 10889
    with fade
    w
    img 10890
    with diss
    cit5 "Покажи свою киску и я куплю это платье..."

    music Power_Bots_Loop
    img 10891
    with fade
    m "ЧТООООО?!!!"
    cit5 "Твою киску!"
    cit5 "Покажи ее и я куплю это платье..."
    music Groove2_85
    img 10892
    with fade
    mt "Эта девочка что, ненормальная?!"
    mt "Она думает что Моника Бакфетт будет показывать ей свои интимные места в какой-то примерочной?!"
    mt "Да, у меня временные проблемы, но я не настолько опустилась, чтобы делать это!"
    music Hidden_Agenda
    img 10893
    with fade
    mt "..."
    mt "С другой стороны, никто здесь не знает кто я такая."
    mt "И, если эта девочка купит платье, то этот кошмар с ненормальными клиентами закончится."
    mt "Я получу другое платье, как договорилась с продавщицей и смогу пойти к Стиву."
    mt "Я буду выглядеть красиво!"
    # corruption +5 req 120
    menu:
        "Показать девочке что она просит.":
            pass
        "Уйти.":
            return

    music Groove2_85
    img 10894
    with fade
    mt "Никого рядом нет..."
    img 10895
    with diss
    m "Хорошо, я сделаю это. Пока никто не видит."
    # Моника показывает
    sound snd_fabric1
    img 10896
    with fadelong
    w
    img 10897
    with diss
    w
    img 10898
    with diss
    w
    img 10899
    with diss
    w
    img 10900
    with diss
    w
    img 10901
    with diss
    w
    img 10902
    with diss
    w
    sound Jump1
    music stop
    img 10903
    with fade
    cit5 "Я пошутила! Хи-хи!"
    sound highheels_run1
    img black_screen
    with diss
    pause 2.0
    music Power_Bots_Loop
    img 10904
    mt "Вот дьявол!"
    mt "О чем я только думала?! Откуда у этой дуры деньги на платье?!"
    mt "Моника, ты уже совсем сходишь с ума."
    mt "Как ты могла показать что-то без гарантий?!"
    mt "Хотя какие к черту гарантии?! С какой стати я вообще что-то кому-то показала?!"
    mt "Я - Моника Бакфетт!"
    return

label gallery_10932:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10921
    with fadelong
    m "Здравствуйте! К Вам можно обратиться?"
    music Groove2_85
    img 10922
    with fade
    cit6 "Ну попробуйте, а Вы кто?"
    # corruption +1 req 80
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            return

    img 10923
    with fade
    m "Я... Я работаю здесь манекеном."
    cit6 "Точно! Как я могла забыть?! Манекен, давай продолжим тестировать платье."
    m "Давайте. Что Вас интересует?"
    cit6 "Похоже, не только у меня провалы в памяти. Раздвигай свои красивые ноги!"
    # моника разводит ноги
    music Loved_Up
    img 10924
    with fade
    cit6 "Вот! Отлично, так и стой! А теперь положи руки за голову!"

    cit6 "Я хочу осмотреть товар."
    # corruption +3 req 100
    menu:
        "Хорошо.":
            pass
        "Ну уж нет.":
            music Power_Bots_Loop
            img 10913
            with fade
            m "Прошу прощения, нужно идти к другому покупателю."
            return
    img 10925
    with diss
    m "Так?"
    # Моника кладет руки за голову
    img 10926
    with diss
    cit6 "Да! А теперь немного нагнись, совсем чуть-чуть."
    img 10927
    with fade
    mt "Что она от меня хочет? Надеюсь, после этого она его купит..."
    # Нагибается
    img 10928
    with diss
    w
    cit6 "Какой хороший манекен, а теперь не шевелись!"
    # Моника стоит какое то время, клиент подходит и шлепает ее по жопе
    img 10929
    with diss
    w
    music stop
    img 10930
    with diss
    w
    sound Spank12
    img 10931
    with diss
    w
    music Groove2_85
    img 10932
    with fade
    m "Ай! Что Вы себе позволяете?"
    cit6 "Как что? Проверяю товар."
    img 10933
    with fade
    m "Но почему так?!"
    cit6 "Вы похоже забыли, что клиент всегда прав, хотя манекену простительно. Знаете что, не буду я у Вас ничего покупать."
    music Power_Bots_Loop
    img 10934
    with fadelong
    mt "Сучка!"
    return

label gallery_10950:
    #уходят в примерочную
    music Groove2_85
    sound snd_fabric1
    img 10948
    with fadelong
    m "..."

    img black_screen
    with diss
    pause 1.0
    img 10949
    with fadelong
    cit7 "Ну? Что стоишь?"
    img 10950
    with diss
    cit7 "Снимай его!"
    # corruption +2 req 90
    menu:
        "Снять платье...":
            pass
        "Уйти.":
            return
    # Моника снимает платье, покупатель одевает
    # Моника стоит обнаженная, закрывается
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 10951
    with fadelong
    cit7 "Ну как?"
    img 10952
    with diss
    cit7 "Как я тебе в этом платье?"
    m "Мэм. Вы выглядите в нем великолепно."
    img 10953
    with fade
    cit7 "Хорошо, я куплю это платье со скидкой 50 процентов!"
    m "Мэм, простите. На это платье не действует скидка..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 10954
    with fadelong
    cit7 "Тогда УВЫ!"
    #исчезает
    return

label gallery_10986:
    # примерочная
    music Loved_Up
    img 10968
    with fadelong
    w
    img 10969
    with diss
    w
    img 10970
    with diss
    w
    img 10971
    with fade
    cit8 "Снимай его скорее!"

    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    img 10972
    with fadelong
    w
    # жадно смотрит на Монику
    # посетительница надела платье
    img 10973
    with fade
    cit8 "Помоги мне, манекенчик!"
    img 10974
    with diss
    m "Да, Мэм. Вам что-то мешает?"
    cit8 "Да, мне мешает, вот здесь снизу." #Показывает в ноги
    img 10975
    with diss
    m "Где, Мэм?"
    cit8 "Еще ниже, вон там."
    img 10976
    with diss
    w
    img 10977
    with fade
    m "Где, Мэм?"
    cit8 "Встань на коленки, тебе отсюда не видно."
    # corruption +3 req 100
    menu:
        "Встать на колени.":
            pass
        "Уйти.":
            return
    #Моника встает на колени
    img black_screen
    with diss
    pause 1.0
    img 10978
    with fade
    w
    img 10979
    with diss
    w
    img 10980
    with diss
    w
    img 10981
    with diss
    m "Где, Мэм?"
    sound snd_fabric1
    img 10982
    with fadelong
    w
    img 10983
    with diss
    w
    img 10984
    with diss
    cit8 "Чуть повыше!"
    img 10985
    with diss
    m "Где?"
    # Посетительница притягивает голову Моники между ног :)
    # Звук чавкания
    music Indo_Rock
    sound Jump1
    img 10986
    with diss
    sound hlup19
    w
    sound hlup10
    img 10987
    with diss
    cit8 "Вот здесь! Здесь, манекенчик!"
    sound hlup10
    img 10988
    with diss
    m "ММмммммм!!!"
    sound hlup21
    img 10989
    with diss
    cit8 "Лижи! Лижи вот здесь!"
    sound hlup10
    img 10990
    with diss
    w
    sound hlup21
    img 10991
    with diss
    m "МММммпфффф!!!"
    sound hlup10
    img 10992
    with diss
    cit8 "Не вырывайся, манекенчик. Я держу тебя крепко."
    sound hlup19
    img 10993
    with diss
    cit8 "Аххххххх!!!"
    sound hlup10
    img 10994
    with diss
    m "ММмммммм!!!"
    img 10995
    with diss
    m "ФУ! КАКАЯ МЕРЗОСТЬ!!!"

    #уходит
    sound snd_bodyfall
    music stop
    img black_screen
    with diss
    pause 2.0
    img 10996
    with fadelong
    w
    music Power_Bots_Loop
    img 10997
    with fade
    mt "Эта сучка и не собиралась покупать платье!"
    return

label gallery_11025:
    # уходят в примерочную
    music Groove2_85
    img 11019
    with fadelong
    cit9 "Разденься и повесь платье на вешалку."
    menu:
        "Раздеться и повесить платье на вешалку.":
            pass
        "Не раздеваться.":
            music Power_Bots_Loop
            img 11020
            with fade
            m "Я не буду этого делать..."
            img 11021
            with diss
            cit9 "Правда? Мне сообщить продавцу что манекен отказывается показывать товар?"
            img 11022
            with fade
            menu:
                "В этом нет необходимости. Я сниму платье.":
                    pass
                "Это не имеет значения. Я не буду снимать платье.":
                    music Groove2_85
                    img 11023
                    with fade
                    m "Мэм. Покупатели могут снимать вещи с манекена только в случае примерки."
                    m "Если Вы собираетесь примерить это платье, то дайте мне знать."
                    return
            m "В этом нет необходимости. Я сниму платье."


#    mt "И зачем я это делаю? Надеюсь, это поможет мне продать платье..."
    # Моника стоит голая и платье на вешалке
    music Groove2_85
    sound snd_fabric1
    img black_screen
    with diss
    pause 1.0
    img 11024
    with fadelong
    w
    img 11025
    with diss
    cit9 "Ха! Вот теперь я точно вижу, что была права!"
    img 11026
    with diss
    cit9 "Но было интересно. Пока, манекен!"
    m "Мэм, Вы купите?..."
    # клиент уходит
    music Power_Bots_Loop
    img 11027
    with fade
    mt "Стерва!"
    return

label gallery_11062:
    #примерочная
    music Groove2_85
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    img 11047
    with fadelong
    cit10 "Снимай его, я примерю."
    img 11048
    with diss
    m "..."
    img 11049
    with fadelong
    cit10 "Ну?"
    menu:
        "Раздеться и отдать платье.":
            pass
        "Уйти.":
            return
    #Моника раздевается, покупатель одевает платье
#    cit10 "А туфли?"
#    m "Мэм, туфли продаются отдельно."
    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11050
    with fadelong
    w
    img 11051
    with fade
    cit10 "Одень мне туфли, я хочу примерить платье в них."
    img 11052
    with diss
    m "Да, Мэм, конечно."
    img 11053
    with diss
    # Ставит туфли
    w
    img 11054
    with fadelong
    cit10 "Я сказала одеть туфли мне на ноги."
    music Power_Bots_Loop
    img 11055
    with fade
    m "Мэм, Вы не можете сделать этого сами?"
    cit10 "Это сделаешь ты..."
    img 11056
    with fade
    m "Дьявол! Ненавижу!!!"
    # corruption +2 req 100
    menu:
        "Одеть туфли покупательнице.":
            pass
        "Уйти.":
            return
    # Моника одевает туфли
    music Groove2_85
    img 11057
    with diss
    w
    img 11058
    with diss
    w
    sound highheels_short_walk
    img 11059
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 11060
    with fadelong
    cit10 "Вторую..."
    img 11061
    with diss
    w
    img 11062
    with diss
    w
    img 11063
    with diss
    w
    sound highheels_short_walk
    img 11064
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11065
    with fadelong
    w
    img 11066
    with diss
    w
    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11067
    with fade
    cit10 "Нет, это не мой стиль!"
    #исчезает
    return

label gallery_11096:
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
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            return
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
    menu:
        "Нагнуться вперед.":
            pass
        "Нет, Мистер!":
            music Power_Bots_Loop
            img 11095
            with fade
            m "Нет, Мистер!"
            return
    #Моника нагибается
    #Посетитель хватает сзади Монику за ляжки
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
    return
