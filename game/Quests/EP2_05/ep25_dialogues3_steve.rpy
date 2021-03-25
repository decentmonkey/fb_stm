default ep25_dialogues3_steve2Flag1 = False

# Любой другой день (регулярное посещение)
label ep25_dialogues3_steve1(steve_status):
    img 11488
    with fade
#    img 11490
    jane "Миссис Бакфетт?"

    music Pyro_Flow
    img 11489
    with diss
    m "Джейн! Мелкая подлиза!"
    m "Встать, когда с тобой говорит Босс!"
    # Джейн встает
    img 11490
    with fade
    w
    img 11491
    with diss
    m "Стив у себя?!"
    img 11492
    with fade
    if monicaEarnedWeeklyMoney == True:
        $ notif(t_("Моника уже заработала деньги для Виктории."))
    if steve_status == 2:
        jane "Нет, Миссис Бакфетт, Мистер Стив будет только на следующей неделе."
    if steve_status == 1:
        jane "Нет, Миссис Бакфетт, Мистер Стив будет только завтра."
    if steve_status == 0:
        jane "Да, Миссис Бакфетт. Мистер Стив у себя в кабинете."
    return True

label ep25_dialogues3_steve1aa:
    # Моника все-равно заходит к Стиву
    menu:
        "Зайти в кабинет.":
            pass
        "Уйти.":
            return False
    img 11373
    with diss
    m "Мне не важно! Я Босс и захожу когда захочу."
    return True

label ep25_dialogues3_steve1a:
    # Регулярный разговор со Стивом
    # заходит
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11493
    with fadelong
    steve "Моника, привет!"
    steve "Рад тебя видеть!"
    steve "Ты пришла заключить контракт?"
# В любой другой день Моника может придти и закрыть сделку со Стивом
# Выбор: закрыть сделку со Стивом
# Есть выбор сцен:
# Контракт со Стивом
# Контракт с Джейн
# Контракт с Тиффани
    img 11494
    with diss
    menu:
        "Закрыть сделку со Стивом." if monicaSteveCumDealActive == True:
            return 1
        "Контракт со Стивом." if monicaSteveCumDealActive == False or monicaSteveCumDealRejected == True:
            return 2
        "Контракт со Стивом. (сначала надо закрыть сделку) (disabled)" if monicaSteveCumDealActive == True and monicaSteveCumDealRejected == False:
            pass
        "Контракт с Джейн. (сначала надо закрыть сделку) (disabled)" if monicaSteveCumDealActive == True and monicaSteveCumDealRejected == False:
            pass
        "Контракт с Джейн. (disabled)" if (monicaSteveCumDealActive == True and monicaSteveCumDealRejected == False) or janeContractCompletedThisWeek == True:
            pass
        "Контракт с Джейн." if (monicaSteveCumDealActive == False or monicaSteveCumDealRejected == True) and janeContractCompletedThisWeek == False:
            return 3
        "Контракт с Тиффани (в следующем обновлении) (disabled)":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 11487
            with fadelong
            m "Я просто ошиблась дверью, Стив!"
            return 0
    return


label ep25_dialogues3_steve1b:
    # Закрыть сделку со Стивом

# Моника говорит Стиву чтобы встал с ее места и садится туда.
# Затем говорит что хочет закрыть их сделку.
# Стив отвечает что это можно сделать прямо сейчас.
# Моника говорит что ее только беспокоит возможность нежелательной беременности.
# Стив говорит что с этим нет проблем, у него есть специальная таблетка.
# Стив кладет таблетку перед Моникой
# Он всегда ее держит на всякий случай. Улыбается.
# Моника злится. Я знаю что ты трахаешь всех налево и направо, Стив!
# Ты мерзавец!
# Стив отвечает что он не мерзавец, он честный бизнесмен, который заключает хорошие сделки!
# Моника зло смотрит
# Стив спрашивает, будет-ли Моника пить таблетку?
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 11495
    with fadelong
    m "Встань с моего стула, Стив!"
    # Моника садится на стул
    img 11496
    with fade
    steve "..."
    img 11497
    with diss
    m "Я хочу закрыть нашу сделку, Стив!"
    img black_screen
    with diss
    pause 1.0
    img 11498
    with fadelong
    w
    img 11499
    with fade
    m "Которую мы заключили у бассейна в моем доме..."
    img 11500
    with diss
    steve "Моника, это можно сделать прямо сейчас."
    img 11501
    with fade
    m "Стив, меня беспокоит возможность нежелательной беременности."
    img 11502
    with diss
    steve "О, Моника! С этим нет проблем!"
    steve "У меня есть специальная таблетка."
    # Стив кладет таблетку
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 11503
    with fadelong
    w
    img 11504
    with fade
    steve "Я всегда держу ее на всякий случай."
    # Стив улыбается
    img 11505
    with diss
    steve "..."
    img 11506
    w
    img 11507
    with diss
    m "!!!"
    img 11508
    with fade
    steve "..."
    music Power_Bots_Loop
    img 11509
    with diss
    m "Я знаю, что ты трахаешь всех налево и направо, Стив!"
    m "Ты мерзавец!"
    music Groove2_85
    img 11510
    with fade
    steve "Моника, я не мерзавец. Я честный бизнесмен."
    steve "Который заключает хорошие сделки!"
    music Power_Bots_Loop
    img 11511
    with diss
    m "!!!"
    img 11512
    with fade
    steve "Моника, будешь-ли ты пить таблетку?"
    img 11513
    with diss
    menu:
        "Я не собираюсь рисковать!":
# Выбор:
# Я не собираюсь рисковать!
# Уходит
            img 11514
            with fadelong
            m "Я не собираюсь рисковать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            $ monicaSteveCumDealRejected = True
            return False
        "Я выпью эту гребаную таблетку...":
            pass
# Я выпью эту гребаную таблетку...
# Стив отвечает. Хорошо, сейчас я попрошу Джейн принести стакан воды.
# Ты ведь будешь запивать таблетку?
# Моника зло смотрит и отвечает: буду...
# Стив зовет Джейн
# Джейн заходит и спрашивает что угодно Мистеру Стиву
# Стив просит Джейн принести стакан воды, у Миссис Бакфетт болит голова и ей надо запить таблетку.
# Джейн приносит воду и ставит на стол перед Моникой. Говорит: пожалуйста, Миссис Бакфетт.
# Моника зло смотрит на Джейн
    music Groove2_85
    mt "Не могу поверить что я соглашаюсь на это..."
    img 11515
    with diss
    m "Я выпью эту гребаную таблетку..."
    img 11516
    with fade
    steve "Хорошо, Моника."
    steve "Сейчас я попрошу Джейн принести стакан воды."
    steve "Ты ведь будешь запивать таблетку?"
    music Power_Bots_Loop
    img 11517
    with diss
    m "!!!"
    music Groove2_85
    img 11518
    with fade
    steve "..."
    img 11519
    with diss
    m "Буду..."
    # Бип телефон
    music stop
    img black_screen
    with diss
    sound snd_phone_short_beeps
    img 11519
    with fade
    steve "Джейн! Зайди, пожалуйста, сюда!"
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11520
    with fadelong
    jane "..."
    img 11521
    with diss
    jane "Да, Мистер Стив."
    jane "Что Вам угодно?"
    img 11522
    with fade
    steve "Джейн, принести, пожалуйста, стакан воды."
    steve "У Миссис Бакфетт болит голова и ей надо запить таблетку."
    img 11523
    with diss
    jane "Хорошо, Мистер Стив, одну минуту."

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Минуту спустя...")) from _call_textonblack_20
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    sound highheels_short_walk
    img 11524
    with fadelong

    # уходит, приходит
# Джейн приносит воду и ставит на стол перед Моникой. Говорит: пожалуйста, Миссис Бакфетт.
# Моника зло смотрит на Джейн
    w
    img 11525
    with fade
    jane "Вот, пожалуйста, Миссис Бакфетт."
    music Power_Bots_Loop
    img 11526
    with diss
    m "!!!"
# Джейн уходя подходит к Стиву и спрашивает: все хорошо, милый?
# Стив отвечает что да, малышка, все хорошо.
# Закрой, пожалуйста, дверь. Нам с Миссис Бакфетт надо закрыть сложный контракт и он бы не хотел чтобы кто-то мешал.
# Джейн отвечает: Да, Мистер Стив.
    music Groove2_85
    img 11527
    with fade
    jane "Все хорошо, Милый?"
    img 11528
    with diss
    steve "Да, малышка, все хорошо."
    steve "Закрой, пожалуйста, дверь."
    img 11529
    with diss
    steve "Нам с Миссис Бакфетт надо закрыть сложный контракт."
    steve "И я бы не хотел чтобы кто-то мешал."
    img 11530
    with fade
    jane "Да, Мистер Стив."


# Джейн уходит
# Моника смотрит на стакан с водой
# Стив говорит Монике что она может выпить таблетку
# Выбор:
# Выпить таблетку или уйти
    sound highheels_short_walk
    img 11531
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11532
    with fadelong
    m "..."
    steve "..."
    img 11533
    with diss
    m "..."
    img 11534
    with fade
    steve "Моника, ты можешь выпить таблетку."
    img 11535
    with diss
    menu:
        "Выпить таблетку.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 11536
            with fadelong
            m "Я не собираюсь рисковать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            $ monicaSteveCumDealRejected = True
            return False

# Если выпить:
# Моника пьет стакан.
# Стив говорит Монике: теперь ты можешь встать и задрать юбку. Мне требуется доступ к
# объекту аренды в соответствии с контрактом
# Моника зло смотрит:
# Уйти или задрать юбку
    music stop
    img 11537
    with fade
    w
    #глоток
    sound snd_gulp
    img 11538
    with diss
    w
    img 11539
    with diss
    w
    sound snd_drinking_water
    img 11540
    with diss
    w
    sound snd_glass_table
    img 11541
    with diss
    w
    music Groove2_85
    img 11542
    with fadelong
    steve "Моника, теперь ты можешь встать и задрать платье."
    img 11543
    with diss
    steve "Мне требуется доступ к объекту аренды в соответствии с контрактом."
    img 11544
    with fade
    menu:
        "Поднять платье.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 11536
            with fadelong
            m "Я не собираюсь этого делать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            $ monicaSteveCumDealRejected = True
            return False

# Если задрать юбку:
# Моника встает и задирает юбку.
# Там трусики Юлии
# Стив говорит: какие интересные у тебя трусики
# В прошлый раз ты была в них-же, либо в прошлый раз ты была в других
# Моника зло отвечает что это не его дело, пусть быстро закрывает контракт и отсылает деньги!
# Стив входит в Монику и трахает ее.
    img 11545
    with diss
    w
    img 11546
    with diss
    w
    img 11547
    with fade
    m "!!!"
    img 11548
    with diss
    w
    sound snd_fabric1
    img 11549
    with diss
    w
    img 11550
    with diss
    w
    img 11551
    with diss
    w
    img 11552
    with diss
    w
    img 11553
    with fade
    steve "О! Моника!"
    steve "Ты не одеваешь трусики?"
    img 11554
    with diss
    steve "Это похвально!"

#    steve "Какие интересные у тебя трусики..."
    # если была в них
#    steve "Не помню, в прошлый раз ты была в них же или была в других..."

    img 11555
    with fade
    steve "У тебя нет трусиков под это платье или тебе просто нравится ходить без них?"
    music Power_Bots_Loop
    img 11556
    with diss
    m "Это не твое дело, Стив!"
    img 11557
    with diss
    m "Быстро закрывай контракт и отсылай деньги!"
    music Groove2_85
    img 11558
    with fade
    steve "Моника, у тебя слишком длинные ноги!"
    img 11559
    with diss
    steve "Можешь, пожалуйста, присесть пониже?"
    steve "Мне нудобно вставать на цыпочки, как в прошлый раз, когда я брал в аренду твою..."
    music Power_Bots_Loop
    img 11560
    m "Заткнись, Стив!"
    img 11561
    with diss
    m "ТАК?!"
    music Groove2_85
    img 11562
    with fade
    steve "Да! Хе-хе!"


    music stop
    # video sex
    img 11563
    with diss
    w
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_1 = Movie(play="video/v_Steve_Monica_Sex_4_1.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_2 = Movie(play="video/v_Steve_Monica_Sex_4_2.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_2
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_3 = Movie(play="video/v_Steve_Monica_Sex_4_3.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_4 = Movie(play="video/v_Steve_Monica_Sex_4_4.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_4
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_5 = Movie(play="video/v_Steve_Monica_Sex_4_5.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_5
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_6 = Movie(play="video/v_Steve_Monica_Sex_4_6.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_6
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_7 = Movie(play="video/v_Steve_Monica_Sex_4_7.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_8 = Movie(play="video/v_Steve_Monica_Sex_4_8.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_8
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_9 = Movie(play="video/v_Steve_Monica_Sex_4_9.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_9
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_11 = Movie(play="video/v_Steve_Monica_Sex_4_11.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_11
    with fadelong
    wclean

    stop music
    music Loved_Up2
    img 11564
    with diss
    w
    img 11565
    with diss
    w
    img 11566
    with diss
    w
    img 11567
    with diss
    w
    img 11568
    with diss
    w
    img 11569
    with diss
    w


# Затем кончает.
    music Loved_Up2
    img 11570
    with fade
    sound bulk1
    steve "АААААХХХХ!!!"
# Моника говорит чтобы он скорее высунул его мерзкий отросток из ее тела!
# Стив говорит погоди, я еще не до конца кончил
# Кончает снова
# Моника зло говорит что теперь все?!
# Стив кончает еще и еще и еще
# Моника вскакивает и держится за киску, зло ругается на Стива что тот пожалеет о том что сделал!

    img 11571
    with diss
    m "Вытаскивай скорее свой мерзкий отросток из моего тела!"
    img 11572
    with fade
    steve "Погоди, я еще не до конца кончил."
    sound bulk1
    steve "АААААХХХХ!!!"
    img 11573
    with diss
    m "Ну что, теперь все?!"
    img 11574
    with fade
    sound bulk1
    steve "АААААХХХХ!!!"
    img 11575
    with diss
    sound bulk1
    steve "АААААХХХХ!!!"
    img 11576
    with diss
    sound bulk1
    steve "АААААХХХХ!!!"

    img 11741
    with fade
    w
    img 11742
    with diss
    w

    music Power_Bots_Loop
    img 11577
    with fadelong
    m "Мерзавец!"
    m "Ты пожалеешь о том что ты сделал!!!"
    img 11578
    with diss
    m "Быстро переводи деньги!"
    $ add_corruption(monicaSteveCumSexDeal, "monicaSteveCumSexDeal")
    music Groove2_85
    img 11579
    with fade
    steve "Да, Моника, конечно!"
    steve "Наш контракт закрыт!"

# Стив перечисляет деньги
    img 11580
    with fadelong
    steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
    steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
    m "!!!"
    return True





label ep25_dialogues3_steve2:
# Контракт со Стивом:
# первый раз:
# Стив, мне нужна какая-нибудь работа.
# Временно. Назначь меня на какую-нибудь руководящую должность.
# Только не слишком низко, ты ведь знаешь мой уровень!
# Стив отвечает Монике что руководящих должностей свободных нет.
# Моника спрашивает: хорошо, тогда назначь меня на какую-нибудь обычную должность, но с высокой зарплатой!
# Стив говорит что обычных должностей тоже свободных нет.
    # Моника не выгоняет Стива со стула
    img 11581
    with fadelong
    m "Стив, мне нужна какая-нибудь работа."
    m "Временно."
    if ep25_dialogues3_steve2Flag1 == False:
        $ ep25_dialogues3_steve2Flag1 = True
        img 11582
        with diss
        m "Назначь меня на какую-нибудь руководящую должность."
        m "Только не слишком низко, ты ведь знаешь мой уровень!"
        img 11583
        with fade
        steve "Моника, прости, но руководящих должностей свободных нет."
        m "!!!"
        img 11584
        with diss
        m "Хорошо, тогда назначь меня на какую-нибудь обычную должность, но с высокой зарплатой!"
        img 11585
        with fade
        steve "Моника, прости, но обычных должностей вакантных тоже нет."

    # Сейчас кризис и он и так собирается сокращать персонал.
    # Моника говорит чтобы он уволил одну из тех дур, которые его окружают.
    # Стив говорит что это невозможно, так как без них он как без рук.
    # Моника злится и говорит Стиву что он пожалеет об этом!
    # Стив говорит что у него есть контракт для Моники.
    # Моника спрашивает какой контракт?
        steve "Сейчас кризис и я и так собираюсь сокращать персонал."
        img 11586
        with diss
        m "Тогда уволь одну из тех дур, которые тебя окружают."
        img 11587
        with diss
        steve "Моника, это невозможно, я без них как без рук!"
        music Power_Bots_Loop
        img 11588
        with fade
        m "Стив! Мерзавец!"
        m "Ты пожалеешь об этом!"
    music Groove2_85
    img 11589
    with fade
    steve "Моника, у меня есть контракт для тебя!"
    img 11590
    with diss
    m "Какой еще контракт?"
# Стив говорит что сегодня был сложный рабочий день и что заплатит ей $5000 если она расслабит его и сделает ему массаж.
# Моника спрашивает что этот извращенец имеет ввиду под расслабить и какого рода массаж ему нужен?
# Стив говорит что Моника может забраться под стол и сделать массаж его члену.
# Его член целый день провел в неподвижности и очень затек. Ему требуется массаж.
# Моника зло смотрит на Стива.
    img 11591
    with fade
    steve "Моника, сегодня был сложный рабочий день."
    steve "Я заплачу тебе $ 5000, если ты расслабишь меня и сделаешь мне массаж."
    img 11592
    with diss
    m "Стив, извращенец, что ты имеешь ввиду под расслабить тебя?"
    m "И какого рода массаж тебе нужен?"
    music stop
    img black_screen
    with diss
    #zip sound
    sound snd_zip
    pause 1.0
    music Loved_Up
    img 11593
    with fadelong
    steve "Моника, ты можешь забраться под стол и сделать массаж моему члену."
    img 11594
    with diss
    steve "Мой член целый день провел в неподвижности и очень затек."
    steve "Ему требуется массаж."
    music Power_Bots_Loop
    img 11595
    with fade
    m "!!!"
# Я тебе что, дешевая проститутка, чтобы ты предлагал мне сосать твой член у тебя под столом?!
# А что будет если войдет твоя невеста Джейн, А?!
# Стив отвечает, что по условиям контракта Моника будет это делать инкогнито и не привлекать внимания.
# Никто про это не узнает. У Стива нет цели испортить деловую репутацию Моники.
# Это никак не связано с сексом за деньги, это просто контракт.
# Да в нем фигурирует член Стива и рот Моники, но, если абстрагироваться от всего, то это просто бизнес.
# А Моника - бизнес-леди и привыкла иметь дело с контрактами.
# В этом нет ничего особенного. Зато $5000 сразу отправятся на любимый адрес Моники.
    img 11596
    with diss
    m "Я ТЕБЕ ЧТО, ДЕШЕВАЯ ПРОСТИТУТКА?!"
    m "ЧТОБЫ ТЫ ПРЕДЛАГАЛ МНЕ СОСАТЬ ТВОЙ ЧЛЕН У ТЕБЯ ПОД СТОЛОМ?!"
    img 11597
    with diss
    m "А что будет, если войдет твоя невеста Джейн, А?!"
    music Groove2_85
    img 11598
    with fade
    steve "Моника, по условиям контракта ты будешь делать это инкогнито и не привлекать внимание."
    steve "Не волнуйся, Моника. Никто про это не узнает."
    steve "У меня нет цели портить твою деловую репутацию."
    img 11599
    with diss
    steve "Это никак не связано с сексом за деньги."
    steve "Это просто контракт."
    img 11600
    with fade
    steve "Да, в нем фигурирует мой член и твой ротик."
    steve "Но, если абстрагироваться от всего, то это просто бизнес."
    img 11601
    with diss
    steve "А ты, Моника, бизнес-леди и привыкла иметь дело с контрактами."
    steve "В этом нет ничего особенного."
    steve "Зато $ 5000 сразу отправятся на твой любимый адрес!"
# Так что, Моника?
    img 11602
    with fade
    m "!!!"
    img 11603
    with diss
    steve "Так что, Моника?"
    img 11604
    with diss
    menu:
        "Уйти.":
# Уйти
            music Power_Bots_Loop
            img 11606
            with fadelong
            m "Я не собираюсь делать этого!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return False
        "Залезть под стол.":
            pass
# Залезть под стол.
# Мне надо больше денег, Стив!
# Хотя бы $5500!
# Моника, это невозможно! Даже $5000 для меня слишком большие деньги!
# Могу предложить тебе 5010$!
    img 11607
    with fade
    mt "До сих пор не могу поверить в то что происходит..."
    mt "Но, по крайней мере, про это никто не узнает."
    mt "В отличии от фотосессий у Бифа, где на меня смотрит весь мир..."
    img 11608
    with diss
    m "Мне надо больше денег, Стив!"
    m "Хотя бы $ 5500!"
    $ chooseVar = 0
    if monicaSteveContractPenaltyActive == True:
        call ep26_dialogues2_steve4() from _call_ep26_dialogues2_steve4
        if _return == False:
            # Моника ушла
            return 0
        $ chooseVar = -1
    else:
        img 11609
        with fade
        steve "Моника, это невозможно!"
        steve "Даже $ 5000 для меня слишком большие деньги!"
        img 11610
        with diss
        steve "Могу предложить тебе $ 5050!"
        img 11611
        with diss
        m "!!!"
        menu:
            "Согласиться на $ 5050":
    # Согласиться на 5050
    # Хорошо, Стив! 10$ Ты мне дашь наличными, понял?!
    # Конечно, Моника, можешь приступать
                img 11612
                with fade
                m "Хорошо, Стив!"
                m "$ 50 ты мне дашь наличными, понял?!"
                img 11613
                with diss
                steve "Конечно, Моника. Можешь приступать."
                $ chooseVar = 1
            "Согласиться на $ 5000":

    # Согласиться на 5000
    # Мне не нужны твои жалкие подачки, Стив! Пусть будет $5000
    # Конечно, Моника, можешь приступать
                music Power_Bots_Loop
                img 11614
                with fade
                m "Мне не нужны твои жалкие подачки, Стив!"
                m "Пусть будет $ 5000."
                music Groove2_85
                img 11613
                with diss
                steve "Конечно, Моника. Можешь приступать."
                $ chooseVar = 2

# Моника залезает под стол.
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up
    img 11615
    with fadelong
    w
    img 11616
    with diss
    w
    img 11617
    with diss
    w
    img 11618
    with diss
    w
    img 11619
    with diss
    w
    #blowjob

    music audio_Monica_Steve_Blowjob_IMG_1
#    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    $ blowjobVideos = [1,2,3,4,5,6,7,8,9]
    $ videosList = random.sample(set(blowjobVideos), 4)

    if 1 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_1 = Movie(play="video/v_Steve_Monica_Blowjob_2_1.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_1
        with fadelong
        wclean


#    music audio_Monica_Steve_Blowjob_IMG_1

    img 11620
    with diss
    w
    if 2 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_2 = Movie(play="video/v_Steve_Monica_Blowjob_2_2.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_2
        with fadelong
        wclean
    if 3 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_3 = Movie(play="video/v_Steve_Monica_Blowjob_2_3.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_3
        with fadelong
        wclean
    img 11621
    with diss
    w
    if 4 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_4 = Movie(play="video/v_Steve_Monica_Blowjob_2_4.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_4
        with fadelong
        wclean
    if 5 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_5 = Movie(play="video/v_Steve_Monica_Blowjob_2_5.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_5
        with fadelong
        wclean
    img 11622
    with diss
    w
    if 6 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_6 = Movie(play="video/v_Steve_Monica_Blowjob_2_6.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_6
        with fadelong
        wclean
    if 7 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_7 = Movie(play="video/v_Steve_Monica_Blowjob_2_7.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_7
        with fadelong
        wclean
    img 11623
    with diss
    w
    if 8 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_8 = Movie(play="video/v_Steve_Monica_Blowjob_2_8.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_8
        with fadelong
        wclean
    if 9 in videosList:
        img black_screen
        with diss
        stop music
        play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Music/audio_Monica_Steve_Blowjob_IMG_1.ogg"
        scene black
        image videov_Steve_Monica_Blowjob_2_9 = Movie(play="video/v_Steve_Monica_Blowjob_2_9.mkv", fps=30)
        show videov_Steve_Monica_Blowjob_2_9
        with fadelong
        wclean
    img 11624
    with diss
    w
    stop music
    music stop
    music2 stop
    return chooseVar
# Затем срабатывает одна из сцен:


label ep25_dialogues3_steve3a:
# Входит Джейн
# Сцена 1
# Джейн входит и говорит Стиву что ему пришел факс.
# Стив отвечает что положи, пожалуйста, его на стол.
# Джейн спрашивает все-ли хорошо? Миссис Бакфетт уже ушла?
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11625
    with fadelong
    jane "Стив, тебе пришел факс."
    img 11626
    with diss
    steve "Хорошо, Джейн."
    steve "Положи, пожалуйста, его на полку."
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11627
    with diss
    w
    #
    music Groove2_85
    img 11628
    with fade
    w
    img 11629
    with diss
    w
    jane "Все-ли хорошо, Милый?"
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11630
    with diss
    jane "Миссис Бакфетт уже ушла?"
# Стив отвечает что она ушла Джейн просто не заметила ее.
# Стив знает что Джейн все время отлучается от рабочего места.
# И, если бы не ее хорошая попка, то он бы давно уволил ее за это.
# Джейн отвечает, что дело не только в этом и чтобы Стив не забывал.
# Джейн уходит
    music Groove2_85
    img 11631
    with fade
    steve "Да, Джейн."
    steve "Она уже ушла. Просто ты не заметила этого."

    music audio_Monica_Steve_Blowjob_IMG_1
    #blowjob
    img 11632
    with fade
    w
    #
    music Groove2_85
    img 11633
    with diss
    steve "Я знаю, что ты все время отлучаешься от рабочего места."
    steve "И, если бы не твоя хорошая попка, то я давно бы уволил тебя за это."
    img 11634
    with diss
    jane "Дело не только в моей попке, Стив."
    jane "Не забывай этого!"
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call ep25_dialogues3_steve5a() from _call_ep25_dialogues3_steve5a # Стив кончает
    $ add_corruption(monicaSteveRegularBlowjobDeal, "monicaSteveRegularBlowjobDeal" + str(day))
    call ep25_dialogues3_steve5() from _call_ep25_dialogues3_steve5 # Моника уходит
    return

label ep25_dialogues3_steve3b:
# Сцена 2
# Джейн входит и спрашивает у Стива не забыл-ли он про свадьбу.
# Стив отвечает что не забыл.
# Джейн спрашивает когда будет дата свадьбы?
# Стив отвечает что это будет очень скоро, Стив работает над этим!
# Джейн отвечает: хорошо, милый и целует его в щечку
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11635
    with fadelong
    w
    img 11637
    with diss
    jane "Милый, ты не забыл про нашу свадьбу?"
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11627
    with diss
    w
    #
    music Groove2_85
    img 11636
    with fade
    steve "Нет, милая, я не забыл."
    img 11638
    with diss
    steve "Я все помню!"
    img 11640
    with fade
    jane "Ты уже решил насчет даты, Милый?"

    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11641
    with fade
    w
    #

    music Groove2_85
    img 11642
    with fade
    steve "Еще нет, Милая, но это будет очень скоро."
    img 11639
    with diss
    steve "Я работаю над этим!"
    img 11643
    with fade
    jane "Хорошо, милый."
    music stop
    img 11644
    with diss
    w
    sound kiss2
    img 11645
    with diss
    jane "Чмок!"
    #уходит
    music Groove2_85
    sound highheels_short_walk
    img 11646
    with fadelong
    w
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call ep25_dialogues3_steve5a() from _call_ep25_dialogues3_steve5a_1 # Стив кончает
    $ add_corruption(monicaSteveRegularBlowjobDeal, "monicaSteveRegularBlowjobDeal" + str(day))
    call ep25_dialogues3_steve5() from _call_ep25_dialogues3_steve5_1 # Моника уходит
    return

label ep25_dialogues3_steve3c:
# Сцена 3
# Джейн входит и говорит что соскучилась по любимому.
# А Стив? Стив отвечает что тоже соскучился.
# Джейн подходит ближе и спрашивает, любит-ли ее Стив?
# Стив отвечает что очень любит малышку Джейн.
# Джейн спрашивает: правда? Ты больше никого не любишь?
# У тебя больше никого нет кроме меня?
# Стив отвечает что любит только Джейн и она у него единственная.
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11635
    with fadelong
    w
    sound highheels_short_walk
    img 11647
    with fade
    jane "Милый, Я соскучилась по тебе."

    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11648
    with diss
    w
    img 11649
    with diss
    w
    #
    music Groove2_85
    img 11650
    with diss
    steve "..."
    jane "А ты?"
    music Loved_Up
    img 11651
    with diss
    steve "..."
    music Groove2_85
    img 11652
    with diss
    jane "А, Стив?! Ты меня слышишь?"
    img 11653
    with fade
    steve "А?! Да, Джейн, я тоже соскучился по тебе."

    # Джейн подходит ближе
    sound highheels_short_walk
    img 11654
    with fade
    w
    img 11655
    with fade
    w
    img 11656
    with diss
    jane "Ты меня любишь, Стив?"

    img 11657
    with diss
    steve "Я очень люблю малышку Джейн!"
    img 11658
    with fade
    jane "Правда?"
    jane "Ты больше никого не любишь?"
    jane "У тебя больше никого нет кроме меня?"
    img 11659
    with diss
    jane "Я соблюдаю твой дурацкий дресс-код."
    jane "И я жду свадьбы, Стив!"
    img 11660
    with fade
    steve "Джейн, я люблю только тебя!"
#    #blowjob
#    music audio_Monica_Steve_Blowjob_IMG_1
#    img 11632
#    with fade
#    w
#    music Groove2_85
#    img 11660
#    with fade
    steve "И ты у меня единственная!"
    music stop
    sound kiss2
    img 11661
    with diss
    jane "Чмок!"
    #уходит
    music Groove2_85
    img 11646
    with fadelong
    w
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call ep25_dialogues3_steve5a() from _call_ep25_dialogues3_steve5a_2 # Стив кончает
    $ add_corruption(monicaSteveRegularBlowjobDeal, "monicaSteveRegularBlowjobDeal" + str(day))
    call ep25_dialogues3_steve5() from _call_ep25_dialogues3_steve5_2 # Моника уходит
    return

label ep25_dialogues3_steve4a:
# Входит Тиффани
# Сцена 1
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив говорит чтобы она положила их на стол
# Джейн кладет сексуально и уходит
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11662
    with fadelong
    tiffany "Мистер Стив, можно войти?"
    img 11663
    with diss
    steve "Да, Тиффани, заходи!"
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11627
    with diss
    w
    #
    sound highheels_short_walk
    music Groove2_85
    img 11664
    with fadelong
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    img 11665
    with diss
    steve "Да, Тиффани, можешь положить их на стол."
    sound snd_folder_drop
    img 11666
    with diss
    tiffany "..."

    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call ep25_dialogues3_steve5a() from _call_ep25_dialogues3_steve5a_3 # Стив кончает
    $ add_corruption(monicaSteveRegularBlowjobDeal, "monicaSteveRegularBlowjobDeal" + str(day))
    call ep25_dialogues3_steve5() from _call_ep25_dialogues3_steve5_3 # Моника уходит
    return


label ep25_dialogues3_steve4b:
# Сцена 2
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив просит Тиффани подойти поближе.
# Тиффани подходит и спрашивает что будет угодно ее Боссу?
# Стив говорит Тиффани что она такая красивая.
# Что Стив очень хочет оценить ее красоту.
# Стив кладет руку на ее ногу пониже попы
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11662
    with fadelong
    tiffany "Мистер Стив, можно войти?"
    img 11663
    with diss
    steve "Да, Тиффани, заходи!"

    music audio_Monica_Steve_Blowjob_IMG_1
    #blowjob
    img 11632
    with fade
    w

    sound highheels_short_walk
    music Groove2_85
    img 11664
    with fadelong
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    sound snd_folder_drop
    img 11667
    with diss
    steve "Тиффани, можешь подойти поближе?"
    sound highheels_short_walk
    img 11668
    with fadelong
    tiffany "Да, Босс, что Вам будет угодно?"
    music Loved_Up
    music2 audio_Monica_Steve_Blowjob_IMG_1
    img 11669
    with fade
    steve "Тиффани, малышка."
    steve "Ты такая красивая..."
    music2 stop
    img 11670
    with diss
    steve "Я так хочу оценить твою красоту!"
# Стив кладет руку на ее ногу пониже попы
    sound Jump2
    img 11671
    with diss
    w

# Тиффани спрашивает помнит-ли Мистер Стив ее условие?
# Стив отвечает что ее условие трудно выполнимо, но ведь это не помешает ему насладиться ее красотой?
# Тиффани жестко отвечает чтобы Стив убрал руку, иначе она заявит о харрасменте.
# Стив убирает руку.
    music Groove2_85
    img 11672
    with fade
    tiffany "Помнит-ли Мистер Стив мое условие?"
    img 11673
    with diss
    steve "Тиффани, твое условие трудно выполнимо."
    img 11674
    with diss
    steve "Но ведь это не помешает мне насладиться твоей красотой?"
    img 11675
    with fade
    tiffany "Уберите руку, Мистер Стив!"
    img 11676
    with diss
    tiffany "Иначе я заявлю о харрасменте!"
    img 11677
    with diss
    w
    music stop
    img 11678
    with diss
    w

# У Стива падает член.
    #звук вниз
    sound snd_down1
    img 11679
    with diss
    w
# Тиффани уходит
    music Groove2_85
    img 11680
    with fade
    w
    sound highheels_short_walk
    img 11681
    with fadelong
    tiffany "..."
    sound highheels_short_walk
    img 11682
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
# Моника зло говорит из-под стола что у Стива упал член.
# И что теперь? Из-за этой дешевой шлюхи ей придется снова его поднимать?
# Стив отвечает что сложности бывают, но, Моника, что поделать, это твоя работа!
# Моника зло продолжает сосать член.
    music Groove2_85
    img 11683
    with fadelong
    w
    music Power_Bots_Loop
    img 11684
    with diss
    m "У тебя упал член, Стив!"
    img 11685
    with diss
    steve "..."
    img 11686
    with fade
    m "И что теперь?"
    m "Из-за этой дешевой шлюхи мне придется снова его поднимать?"
    music Groove2_85
    img 11687
    with diss
    steve "Моника, во время выполнения любого контракта бывают сложности."
    steve "Но что поделать? Это твоя работа."
    music Power_Bots_Loop
    img 11688
    with fade
    m "!!!"
    music Groove2_85
    img 11689
    with diss
    steve "Моника, ты можешь продолжать. Контракт еще не закрыт."
    img 11690
    with fade
    m "!!!"
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11691
    with fade
    w
    stop music fadeout 1.0
    call textonblack(t_("СПУСТЯ 15 МИНУТ...")) from _call_textonblack_21
    img black_screen
    with Dissolve(1)
# Моника зло продолжает сосать член.
    call ep25_dialogues3_steve5a() from _call_ep25_dialogues3_steve5a_4 # Стив кончает
    $ add_corruption(monicaSteveRegularBlowjobDeal, "monicaSteveRegularBlowjobDeal" + str(day))
    call ep25_dialogues3_steve5() from _call_ep25_dialogues3_steve5_4 # Моника уходит
    return


label ep25_dialogues3_steve4c:
# Сцена 3
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив просит Тиффани подойти поближе
# Тиффани подходит и говорит что все уже сказала.
# Ее ответ нет и она догадывается что Стив хочет сейчас сделать.
# Стив подносит руку к Тиффани
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11662
    with fadelong
    tiffany "Мистер Стив, можно войти?"
    img 11663
    with diss
    steve "Да, Тиффани, заходи!"
    sound highheels_short_walk
    music Groove2_85
    img 11664
    with fadelong
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    sound snd_folder_drop
    img 11667
    with diss
    steve "Тиффани, можешь подойти поближе?"
# Тиффани подходит и говорит что все уже сказала.

    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    img 11692
    with fadelong
    tiffany "Мистер Стив, я Вам все уже сказала."
    tiffany "Я догадываюсь что Вы сейчас хотите сделать."
    img 11693
    with diss
    tiffany "Мой ответ НЕТ!"

# Стив подносит руку к Тиффани
    sound Jump1
    img 11694
    with diss
    w
    img 11695
    with fade
# Тиффани говорит: только попробуйте, Мистер Стив...
# Стив говорит, что Тиффани так красива, так прекрасна
# Что Стив настолько сильно хочет ее, если бы она только знала...
# Что он.. он... Аааххх! Стив хватает Тиффани за попу под трусиками и кончает Монике в рот
    tiffany "Только попробуйте, Мистер Стив..."
    music Loved_Up
    img 11697
    with diss
    steve "О, Тиффани!"
    img 11696
    with diss
    steve "Ты так красива!"
    steve "Так прекрасна!"
    img 11698
    with diss
    steve "Если бы только знала как я хочу тебя!"
    music Loved_Up2
    sound Jump2
    img 11699
    with diss
    steve "Если бы ты только, Аааах!!"
# Что он.. он... Аааххх! Стив хватает Тиффани за попу под трусиками и кончает Монике в рот
    img 11700
    with diss
    tiffany "!!!"
    img 11701
    with diss
    steve "Аааах!"
    img 11702
    with diss
    steve "Аааах!"
    #звук кончания
    img 11703
    with diss
    sound bulk1
    steve "АААААААААААРГХХХХХ!!!"
    img 11704
    with diss
    w
    img 11705
    with diss
    sound bulk1
    steve "АААААААААААРГХХХХХ!!!"
    m "!!!"

# Тиффани смеется.
    music Groove2_85
    img 11706
    with fadelong
    tiffany "Ха!"
# Вы там что, кончили, Мистер Стив?
# Хи-хи-хи. Вы пополнили мою смешную коллекцию мужчин, которые кончают себе в штаны при моем виде.
# Моника зло смотрит из-под низа
# Хорошего рабочего дня, Мистер Стив...
# Уходит
    tiffany "Вы там что, кончили, Мистер Стив?"
    img 11707
    with diss
    steve "..."
    sound highheels_short_walk
    img 11708
    with fadelong
    tiffany "Хи-хи-хи."
    tiffany "Вы дополнили мою смешную коллекцию мужчин, которые при виде меня кончают в штаны."
    img 11709
    with diss
    w
    img 11710
    with diss
    m "!!!"
    sound highheels_short_walk
    img 11711
    with fadelong
    tiffany "Хорошего рабочего дня, Мистер Стив!"

    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
#    call ep25_dialogues3_steve5a() # Стив кончает
    $ add_corruption(monicaSteveRegularBlowjobDeal, "monicaSteveRegularBlowjobDeal" + str(day))
    call ep25_dialogues3_steve5() from _call_ep25_dialogues3_steve5_5 # Моника уходит
    return

label ep25_dialogues3_steve5a:
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


label ep25_dialogues3_steve5:
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
        call ep26_dialogues2_steve4b() from _call_ep26_dialogues2_steve4b
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












#
