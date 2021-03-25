# Бетти:
# Если Бетти прокачана до ур.3, то она предлагает Монике сходить на фитнесс. Разрешает ей не убираться в этот день.
# Потом фитнесс активируется через 3 дня. Если сегодня фитнеса нет, то Бетти говорит что я пойду на днях.

# На фитнесе в первый раз Моника в шоке что это тот фитнесс где занимается она.
# Приходит туда, там Стефани и Ребекка. Моника в шоке, общается с ними и с Бетти.
# Пускает пыль в глаза что это все специально, девочки, вы потом удивитесь тому что я задумала.
# Те удивляются и идут заниматься
# Сцена занятия

# В конце Стефани обнаженная пристает к Ребекке. Та ее отшивает

# Заходит Бетти и говорит Монике ждать на улице. Моника ждет час.

# При повторе, Стефани и Ребекка спрашивают у Моники что когда она закончит свое приключение? Та отвечает что скоро.
# Они удивляются и идут заниматься.
# При входе Моники они обнаженные (только повтор) У Ребекки зад показан не совсем.
# Одеваются и идут заниматься

# Бетти также говорит Монике ждать на улице.

# Бетти качается фитнесом также как и уборкой и достигает ур.4. На этом все


# Если Бетти прокачана до ур.3, то она предлагает Монике сходить на фитнесс. Разрешает ей не убираться в этот день.
# Потом фитнесс активируется через 3 дня. Если сегодня фитнеса нет, то Бетти говорит что я пойду на днях.

default ep22_dialogues4_7a_flag1 = True

label ep22_dialogues4_1b:
    mt "Бетти говорила что сегодня день поездки в фитнесс-зал."
    mt "Но мне надо сначала закончить уборку..."
    return
label ep22_dialogues4_1:
    # Если Бетти ур.3
#    call ep22_Quests_Betty_Monica_Governess_outfit() #debug!!!

    img 6018
    with fade
    betty "Моника, гувернантка."
    img 6019
    "Как я выгляжу?"
    img 6020
    "Тебе нравится?"
    img 6021
    mt "!!!"
    img 6022
    m "Да, Мэм. Вы выглядите великолепно."
    img 6023
    betty "Да, получше чем ты!"
    img 6024
    # Если фитнесс сегодня есть:
    if bettyFitnessToday == True:
        img 6029
        betty "Моника, я могу взять тебя с собой на фитнесс."
        "Покажу тебе что надо делать, чтобы выглядеть так как Я."
        "Понесешь мои вещи."
        "Ты можешь наблюдать за мной, возможно, даже я куплю тебе однажды абонемент туда..."
        $ menuName = "floor2_betty_fitness_dialogue"
        menu:
            "Согласиться...":
                img 6028
                m "Да, Миссис Робертс, я готова."
                img 6027
                betty "Хорошо, ты можешь переодеться, только не в свои грязные тряпки, как у проститутки!"
                img 6029
                m "Миссис Робертс, я могу поехать в униформе, если Вы разрешите..."
                betty "Хорошо, можешь ехать в униформе."
                "В конце концов, ты прислуга и это стоит подчеркивать!"
                img 6025
                mt "!!!"
                img black_screen
                with Dissolve(1.0)
                pause 1.0
                img 8531
                with fade
                w
                img 8532
                sound snd_car_turn_on
                pause 2.0
                sound snd_car_engine
                img scene_Map
                with fade
                w
                return True
#            "Согласиться и предупредить Барди...":
#                img 10607
#                m "Миссис Робертс, Вы дадите мне минуту, чтобы собраться?"
#                img 6027
#                betty "Не более минуты, гувернантка. Я не собираюсь ждать тебя."
#                img 10608
#                m "Да, Миссис Робертс, я быстро вернусь..."
            "Отказаться.":
                img 6028
                m "Миссис Робертс. Простите. Я планировала еще заняться пятном на ковре..."
                betty "Хорошо, Моника, занимайся..."
                return False
            "":
                pass
    else:
        # Если фитнеса сегодня нет
        img 6029
        betty "Я собираюсь поехать на фитнесс на днях. Если ты хочешь, я смогу взять тебя с собой."
        betty "Он {c}по вторникам и четвергам{/c}"
        betty "Напомни мне."
        img 6028
        m "Да, Миссис Робертс. Хорошо..."
        if bettyPantiesFloor2TalkFlag == True:
            $ menuName="monica_betty_dialogue_floor2_end_menu"
            menu:
                "Уйти.":
                    pass
                "":
                    pass
    return False

label ep22_dialogues4_1a0:
    #Моника приходит после разговора с Барди (когда его предупреждает)
    menu:
        "Я готова, Миссис Робертс...":
            music Hidden_Agenda
            img 6028
            with fade
            m "Я готова, Миссис Роберс..."
            img 6026
            betty "Я заждалась тебя, нерадивая гувернантка."
            betty "Быстро бери мою сумку и поехали скорее!"
            img 10608
            with fade
            m "Да, Миссис Робертс..."
            music stop
            img black_screen
            with Dissolve(1.0)
            pause 1.0
            img 8531
            with fade
            w
            img 8532
            sound snd_car_turn_on
            pause 2.0
            sound snd_car_engine
            img scene_Map
            with fade
            w
            return True
        "Уйти.":
            return False

    return

label ep22_dialogues4_1a:
    # На улице. Водитель Фред, Бетти и Моника. Первый раз
    if ep22_quest_flag1 == False:
        $ ep22_quest_flag1 = True
        mt "О БОЖЕ!!!"
        "Это же фитнесс-зал куда я ходила!!!"
        "Мне нельзя туда в таком виде!!!"
        betty "Моника, гувернантка, почему ты отстаешь от меня?"
        "Поторопись! За мной!"
    return

label ep22_dialogues4_2:
    # повтор
    betty "Моника, гувернантка, почему ты отстаешь от меня?"
    "Поторопись! За мной!"
    return
label ep22_dialogues4_2a:
    # повтор
    betty "Моника, гувернантка, почему ты отстаешь от меня?"
    "Поторопись! За мной!"
    return False

label ep22_dialogues4_3a:
    mt "Черт! Этот инструктор!"
    "Мне надо как-то повернуться, чтобы он не узнал меня!"
    return False
label ep22_dialogues4_3:
    if fitness_gym_visited_amount == 0:
        # Зал фитнеса, autorun первый раз
        mt "Черт! Этот инструктор!"
        "Мне надо как-то повернуться, чтобы он не узнал меня!"


    fitness_instructor "Добрый день, Миссис Робертс!"
    "Вы сегодня выглядите очаровательно."

    betty "Ой, спасибо!"
    "Ты заставляешь краснеть меня!"

    mt "Эта сучка что, флиртует с ним?!"
    return

label ep22_dialogues4_4: #клик по Бетти ил иниструктору в фитнесс-зале
    if act == "l":
        mt "Эта сучка что, флиртует с ним?!"
        return
    call ep22_dialogues4_2a() from _call_ep22_dialogues4_2a
    return False

label ep22_dialogues4_5:
    # Моника заходит в раздевалку, там Стефани и Ребекка
    mt "ДЬЯВОЛ!!!"
    "Эти дуры здесь, как всегда!"
    "Мне надо как-то выкрутиться!"
    "Я не могу себе позволить упасть в их глазах!"
    "Мне еще с ними общаться после того как это все закончится!"
    return

label ep22_dialogues4_5a:
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

label ep22_dialogues4_6:
    #render
    #Сцена занятия йогой.
    #Стефани, Ребекка, Бетти


    #выбор
#    img 7755

    $ imagesListIdx = 0

    if obj_name == "Stephanie":
        menu:
            "Смотреть на Стефани.":
                pass
            "Нет.":
                return False

        music Ready_and_Waiting
        #Stephanie - 7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829,
        # 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911
        $ images = [7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829, 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911]
        $ imagesAmount = 25
        $ imagesList = random.sample(set(images), imagesAmount)
        $ imagesList.sort()
        label ep22_dialogues4_6_loop1:
            if imagesListIdx < imagesAmount:
                $ imageName = str(imagesList[imagesListIdx])
                img imageName
                if imagesListIdx == 0:
                    with fadelong
                w
                $ imagesListIdx += 1
                jump ep22_dialogues4_6_loop1

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
        $ add_corruption(monicaFitnessLookAtGirlsCorruption, "monicaFitnessLookAtGirlsCorruption" + str(day))

    if obj_name == "Rebecca":
        menu:
            "Смотреть на Ребекку.":
                pass
            "Нет.":
                return False

        music Ready_and_Waiting
        #Rebecca - 7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832,
        # 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916
        $ images = [7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832, 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916]
        $ imagesAmount = 27
        $ imagesList = random.sample(set(images), imagesAmount)
        $ imagesList.sort()
        $ videoFlag = False
        label ep22_dialogues4_6_loop2:
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
                jump ep22_dialogues4_6_loop2

        #Инструктор подходит к Ребекке
        music Loved_Up
        img 7931
        with fadelong
        fitness_instructor "Ребекка, давай я помогу тебе..."
        img 7932
        rebecca "Спасибо, не надо..."
        $ add_corruption(monicaFitnessLookAtGirlsCorruption, "monicaFitnessLookAtGirlsCorruption" + str(day))

    if obj_name == "Betty":
        menu:
            "Смотреть на Бетти.":
                pass
            "Нет.":
                return False
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
        label ep22_dialogues4_6_loop3:
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
                jump ep22_dialogues4_6_loop3


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

        $ add_corruption(monicaFitnessLookAtGirlsCorruption, "monicaFitnessLookAtGirlsCorruption" + str(day))
        $ fitness_gym_betty_first_time_interact_with_trainer = False

    return

label ep22_dialogues4_7:
    #render
    #Конец занятия йогой, Бетти говорит с Моникой
    music Groove2_85
    img 7726
    with fadelong
    betty "Моника, гувернантка, подожди меня на улице, я скоро выйду."
    m "Да, Миссис Робертс..."
    return

label ep22_dialogues4_7a:
    #Сменяется на город
    if ep22_dialogues4_7a_flag1 == True:
        mt "Черт! Уже прошел час!"
        "Что там делает эта сучка Бетти?!"
    $ ep22_dialogues4_7a_flag1 = True
    if bettyKnowsAboutPanties == True:
        call ep24_dialogues3_fitness6() from _call_ep24_dialogues3_fitness6
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    $ add_hook("open", "EP22_Quests_Betty6b", scene="street_fitness")
    call change_scene("street_fitness") from _call_change_scene_219
    return

label ep22_dialogues4_7b:
    #fade
    betty "Я закончила. Поехали, Фред!"
    fred "Поехали, Мэм!"
    call EP22_Quests_Betty8() from _call_EP22_Quests_Betty8_4
    return

# При повторе, Стефани и Ребекка спрашивают у Моники что когда она закончит свое приключение? Та отвечает что скоро.
# Они удивляются и идут заниматься.
# При входе Моники они обнаженные (только повтор) У Ребекки зад показан не совсем.
# Одеваются и идут заниматься

label ep22_dialogues4_8:
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
# На фитнесе в первый раз Моника в шоке что это тот фитнесс где занимается она.
# Приходит туда, там Стефани и Ребекка. Моника в шоке, общается с ними и с Бетти.
# Пускает пыль в глаза что это все специально, девочки, вы потом удивитесь тому что я задумала.
# Те удивляются и идут заниматься
# Сцена занятия
