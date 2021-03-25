
label gallery_11566:
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
            return
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
    call textonblack(t_("Минуту спустя...")) from _rcall_textonblack_16
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
            return

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
            return

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
    return

label gallery_11629:
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
    call gallery_20385_1() from _rcall_gallery_20385_1 # Стив кончает
    call gallery_20385_2() from _rcall_gallery_20385_2 # Моника уходит
    return

label gallery_11664:
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
    call gallery_20385_1() from _rcall_gallery_20385_1_1 # Стив кончает
    call gallery_20385_2() from _rcall_gallery_20385_2_1 # Моника уходит
    return

label gallery_11645:
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
    call gallery_20385_1() from _rcall_gallery_20385_1_2 # Стив кончает
    call gallery_20385_2() from _rcall_gallery_20385_2_2 # Моника уходит
    return

label gallery_11669:
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
    call textonblack(t_("СПУСТЯ 15 МИНУТ...")) from _rcall_textonblack_17
    img black_screen
    with Dissolve(1)
# Моника зло продолжает сосать член.
    call gallery_20385_1() from _rcall_gallery_20385_1_3 # Стив кончает
    call gallery_20385_2() from _rcall_gallery_20385_2_3 # Моника уходит
    return

label gallery_11659:
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
    call gallery_20385_1() from _rcall_gallery_20385_1_4 # Стив кончает
    call gallery_20385_2() from _rcall_gallery_20385_2_4 # Моника уходит
    return

label gallery_11699:
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
#    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() from _rcall_gallery_20385_2_5 # Моника уходит
    return

label gallery_12633:
# Приходит к Джейн.
# Джейн с улыбкой смотрит на Монику.
# Моника говорит чтобы Джейн встала, когда перед ней стоит ее Босс!
# Джейн встает.
    music stop
    img black_screen
    with diss
    pause 1.5
    sound highheels_short_walk
    img 12578
    music Sneaky_Snitch
    with fadelong
    jane "Миссис Бакфетт?"
    music Pyro_Flow
    img 12579
    with fade
    m "!!!"
    img 12580
    jane "..."
    img 12581
    with diss
    m "Джейн!"
    m "Встань, когда перед тобой стоит твой Босс!"
    img 12582
    with fade
    w
# Моника надменно спрашивает что Джейн хочет узнать у Моники по поводу ее великолепной фигуры?
# Джейн спрашивает как Монике удалось достичь такой превосходной формы?
# Моника отвечает что все дело в правильном питании и регулярном занятии фитнессом.
# Джейн спрашивает, можно-ли ей рассмотреть Монику поближе.
# Моника надменно отвечает что не видит в этои необходимости, но так уж и быть.
# Джейн спрашивает у Моники чем она питается в данный момент? Какая сейчас лучшая диета?
    music Stealth_Groover
    img 12583
    with fadelong
    m "Итак..."
    m "Что ты хочешь узнать относительно моей великолепной фигуры?"
    img 12584
    jane "Миссис Бакфетт, скажите, как Вам удалось достичь такой превосходной формы?"
    img 12585
    with diss
    m "Все дело в правильном питании и регулярном занятии фитнесом."
    img 12586
    jane "Миссис Бакфетт, можно-ли мне рассмотреть Вашу фигуру поближе?"
    img 12587
    with fade
    m "Я не вижу в этом особой необходимости..."
    img 12588
    with diss
    jane "..."
    img 12589
    with fade
    m "Но, так уж и быть!"
    #Джейн подходит и осматривает Монику
    music stop
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    music Sneaky_Snitch
    img 12590
    with fade
    w
    img 12591
    with diss
    sound highheels_short_walk
    w
    img 12592
    with fade
    jane "Миссис Бакфетт, скажите, чем Вы питаетесь в данный момент?"
    jane "Какая сейчас лучшая диета?"

# Моника сконфужена...
# Чем я питаюсь? Моя диета?
# Да уж! Я боюсь что эта толстая корова не сможет выжить на моей сегодняшней диете...
    music Hidden_Agenda
    img 12593
    with fade
    mt "Чем я питаюсь?"
    mt "Моя диета?"
    mt "Да уж!"
    mt "Я боюсь что эта толстая корова не сможет выжить на моей сегодняшней диете..."

# Моника отвечает что за ее рационом следит известный доктор, который скурпулезно составляет необходимые вещества.
# В общем, Джейн. Ты себе такого позволить не сможешь. Если есть другие вопросы, то задавай скорее и закончим.
    music Stealth_Groover
    img 12594
    with fade
    m "За моим рационом следит известный доктор!"
    m "Который скурпулезно составляет список блюд, содержащих необходимые вещества и витамины."
    img 12595
    with diss
    m "В общем, Джейн."
    img 12596
    jane "..."
    img 12597
    m "Ты себе такого позволить не сможешь."
    m "Если есть другие вопросы, то задавай скорее и закончим с этим."

# Джейн обсматривает Монику.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Sneaky_Snitch
    img 12598
    with fadelong
    w
    img 12599
    with diss
    w
    img 12600
    with diss
    jane "..."
    img 12601
    with diss
    m "..."

# Миссик Бакфетт, Вы говорили что-то по поводу фитнесса.
# Да, Джейн. Фитнесс и йога - неотъемлемая часть построения изящной фигуры...
    img 12602
    with fadelong
    jane "Миссис Бакфетт."
    jane "Вы говорили по поводу фитнеса..."
    img 12603
    m "Да, Джейн."
    m "Фитнес и йога - неотъемлемая часть построения изящной фигуры..."

# Джейн спрашивает в какой фитнесс-центр сейчас ходит Моника и может-ли она помочь ей тоже устроиться туда на занятия.
# Моника отвечает что с ней занимается личный тренер, который внешне соответствует здоровому образу жизни.
# А также знает толк в упражнениях для достижения нужной цели.
    img 12604
    with fade
    jane "Миссис Бакфетт."
    jane "А в какой фитнес-центр Вы сейчас ходите заниматься?"
    img 12605
    jane "Могли-бы Вы мне помочь тоже устроиться туда на занятия?"
    music Stealth_Groover
    img 12606
    with fade
    m "Со мной занимается личный тренер, который даже внешне соответствует здоровому образу жизни."
    m "А также знает толк в упражнениях для достижения нужной цели!"

# Однако, к этому тренеру многие стараются попасть и у тебя, Джейн, нет никаких шансов на это.
    img 12607
    m "Однако, к этому тренеру многие стараются попасть."
    m "И у тебя, Джейн, нет никаких шансов на это!"

# Джейн спрашивает, можно-ли попасть в ее фитнесс-центр к другому тренеру?
# Моника отвечает что ее центр - только для элитных девушек, имеющих положение в обществе
# и туда можно попасть только по приглашению.
# Моника, естественно, не собирается это пришлашение Джейн давать!
    img 12608
    jane "Можно-ли попасть в Ваш фитнес-центр к другому тренеру?"
    img 12609
    with fade
    m "Фитнес-центр, куда я хожу - только для элитных девушек, имеющих положение в обществе!"
    m "И туда можно попасть только по приглашению."
    img 12610
    jane "..."
    img 12611
    with diss
    m "И, разумеется, я не собираюсь давать это приглашение для тебя, Джейн!"

# Моника думает про себя, что ей не хватало еще в фитнесс центре Джейн или этой проститутки Тиффани.
# Учитывая как Бетти обращается с Моникой там, не будет ничего хорошего если эти дуры станут свидетелями этого.
    music Hidden_Agenda
    img 12612
    with fade
    mt "Еще мне не хватало в фитнес-центре Джейн или этой проститутки..."
    mt "Как ее там..."
    mt "Тиффани..."
    img 12613
    with diss
    mt "!!!"
    mt "Учитывая, как Бетти обращается со мной там, не будет ничего хорошего если эти дуры станут свидетелями этого..."

# Джейн обиженно смотрит.
# Джейн говорит: Миссис Бакфетт.
    music Sneaky_Snitch
    img 12614
    with fade
    jane "..."
    jane "Миссис Бакфетт..."

# Моника прерывает. Джейн! Ты еще не закончила со своими дурацкими вопросами?!
# Я оказываю безмерную услугу Стиву тем, что согласилась ответить на несколько вопросов для его будущей супруги.
# Но ты начинаешь меня утомлять, Джейн!
# Давай заканчивай!
# Моника думает (я хочу побыстрее пообедать в дорогом ресторане!)
    music Power_Bots_Loop
    img 12615
    with fade
    m "Джейн! Ты еще не закончила со своими дурацкими вопросами?!"
    m "Я оказываю безмерную услугу Стиву тем, что согласилась ответить на несколько вопросов для его будущей супруги."
    img 12616
    m "Но ты начинаешь меня утомлять, Джейн!"
    m "Давай заканчивай!"
    img 12617
    with diss
    mt "Мне надоела эта Джейн!"
    mt "Я хочу побыстрее пообедать в дорогом ресторане!"

# Джейн говорит: Миссис Бакфетт. Мистер Стив сказал что Вы покажете мне свою грудь...
# Моника шипит. Джейн, ты не перегибаешь палку?!
# Джейн отвечает, Миссис Бакфетт, простите! Просто так сказал Мистер Стив!...
# Я не хотела как-то оскорбить Вас!
    music stop
    img black_screen
    with diss
    pause 1.0
    music Sneaky_Snitch
    img 12618
    with fadelong
    jane "Миссис Бакфетт..."
    jane "Мистер Стив сказал, что Вы покажете мне свою грудь..."
    music Power_Bots_Loop
    img 12619
    with diss
    mt "!!!"
    img 12620
    m "Джейн! Ты не перегибаешь палку?!"
    img 12621
    with fade
    jane "Миссис Бакфетт, простите! Просто так сказал Мистер Стив!..."
    jane "Я не хотела как-то оскорбить Вас!"

# выбор Моники:
# показать грудь
# не показывать грудь (нарушение контракта)
    img 12622
    with fade
    menu:
        "Показать грудь":
            pass
        "Не показывать грудь (нарушение контракта)":
# Моника не показывает грудь:
# Моника говорит что не собирается ничего показывать Джейн. Достаточно и так!
            img 12623
            with fade
            m "Я не собираюсь ничего показывать, Джейн!"
            m "Достаточно и так!"

# После этого, Моника возвращается к Стиву закрыть контракт.
# Моника говорит Стиву что сделала как они договорились и она ждет тикет на ланч в ресторане.
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.5
            music Hidden_Agenda
            img 12645
            with fadelong
            m "Стив!"
            m "Я достаточно рассказала твоей невесте, как мы договорились."
            img 12646
            m "Я жду сертификат на ланч в ресторане."

# Если Моника не показала грудь Джейн, то Стив заявляет что Моника нарушила контракт и не показала грудь.
# За это полагается неустойка, в виде одного бесплатного контракта на массаж его члена.
# Моника злится и говорит чтобы Стив пошел к черту со своими контрактами!
            music Groove2_85
            img 12647
            with fade
            steve "Моника, но ты не показала свою грудь Джейн!"
            steve "Ты нарушила контракт!"
            img 12648
            with diss
            steve "За это полагается неустойка в виде бесплатного контракта на массаж моего члена, хе-хе!"
            music Power_Bots_Loop
            img 12649
            with fadelong
            m "Иди ты к черту со своими контрактами!!!"
            return

# Моника говорит что Стив умолял Монику сделать это.
# К тому же, Монике есть чем гордится и она, так уж и быть, сделает это.
# Моника показывает грудь Джейн.
    img 12624
    with fade
    mt "!!!"
    img 12625
    with diss
    jane "..."
    music Hidden_Agenda
    img 12626
    with fade
    m "Ладно..."
    m "Стив умолял меня сделать это..."
    img 12627
    jane "..."
    img 12628
    m "К тому же, мне есть чем гордиться."
    m "И я, так уж и быть, сделаю это..."

# Моника показывает грудь.
    label gallery_12638:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 12629
    with fadelong
    w
    img 12630
    with diss
    w
    img 12631
    with diss
    w
# Джейн спрашивает, а они настоящие? можно-ли потрогать?
# выбор Моники: Можно потрогать или не дать трогать грудь
    img 12632
    jane "Миссис Бакфетт, а они настоящие?"
    jane "Можно потрогать?"
    img 12633
    with diss
    menu:
        "Дать потрогать свою грудь.":
# Если дает потрогать, то:
# Моника шипит: Можно, только быстро, Джейн!
# Джейн трогает грудь
# Моника закрывается и говорит что довольно.
            img 12634
            with fade
            m "Можно, только быстро, Джейн!"
            music Loved_Up2
            img 12636
            with diss
            w
            img 12635
            with diss
            w
            img 12637
            with diss
            mt "Как же мне противно!"
            img 12638
            with diss
            jane "..."
            music Power_Bots_Loop
            img 12639
            with fade
            m "Довольно!"

        "Не дать потрогать свою грудь.":

# Моника говорит что нельзя потрогать грудь:
# Моника шипит и говорит Джейн что только попробуй!
# Джейн ошеломленно отвечает что просто хотела проверить, настоящие они или нет?
# Моника отвечает что они настоящие, как и сама Моника, в отличие от Джейн, которая является лишь тенью Стива.
            music Power_Bots_Loop
            img 12640
            with fade
            m "Только попробуй!"
            img 12641
            jane "Простите, Миссис Бакфетт."
            jane "Я только хотела проверить, настоящие они или нет..."
            img 12642
            with diss
            m "Они настоящие, как и я сама!"
            m "В отличие от тебя Джейн!"
            img 12643
            m "Ты являешься лишь тенью Стива!"
# Джейн обиженно смотрит.
            img 12644
            jane "!!!"


# Если Моника показала грудь Джейн, то Стив дает тикет на ланч в ресторане (предмет)
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    img 12650
    with fadelong
    m "Стив!"
    m "Я достаточно рассказала твоей невесте, как мы договорились."
    img 12651
    m "Я жду сертификат на ланч в ресторане."

    # Стив кладет сертивикат
    sound snd_folder_drop
    img 12652
    with fade
    steve "Моника!"
    steve "Ты жестокая женщина!"
    sound snd_take_paper
    img 12653
    with diss
    steve "Сначала ты оставила меня без денег, а теперь оставляешь и без еды!"
    # Моника уходит
    music Power_Bots_Loop
    img 12654
    with fadelong
    m "Не забывай при каких обстоятельствах это происходило!"
    m "Ты еще ответишь за все, что сделал!"
    return

######################### Ле Гранд, Филлип

label gallery_22982:

    # Моника заказывает еду у официантки ( ep26_dialogues4_restaurant - разговор с официанткой и заказ еды)
    # пока ждет, когда принесут ее заказ, сидит на стуле с задумчивым видом
    music Poppers_and_Prosecco
    img 22946
    with fadelong
    mt "Наконец-то моя прежняя жизнь постепенно возвращается..."
    mt "Я на верном пути."
    mt "Совсем недавно я могла себе позволить только ужасный кебаб..."
    mt "Или не менее ужасное пирожное..."
    img 22947
    with fade
    mt "А сейчас я в ресторане, на мне красивое платье..."
    mt "Я поела такой вкусный ужин..."
    mt "Скоро Моника Бакфетт вернет себе все, что у нее отняли!"
    mt "И накажет всех, кто посмел недостойно себя вести в отношении нее..."
    # приносят ужин и тут ее мысли прерывает мужской голос
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    img 22948
    with hpunch
    sound plastinka1b
    philip "Миссис Бакфетт, какая неожиданная и приятная встреча!"
    # Моника поднимает взгляд, рядом с ее столиком стоит Филипп
    music Pyro_Flow
    img 22949
    with fade
    mt "О нет! Только не этот мерзкий тип!"
    mt "Что он здесь делает?!"
    # Филипп продолжает любезно улыбаться
    music Groove2_85
    img 22950
    with diss
    sound kiss1
    philip "Добрый вечер, Миссис Бакфетт. Позвольте вашу ручку?"
    # Филипп целует ее руку и садится за ее столик. Она вопросительно смотрит на него
    img 22951
    with fade
    philip "Я впечатлен Вашей презентацией, Миссис Бакфетт."
    img 22952
    with diss
    m "Спасибо, Филипп."
    mt "Что ему от меня надо?"
    img 22953
    with fade
    philip "На этой презентации я увидел у Вас кое-что интересное, Мэм..."
    m "..."

    # если Моника делала ему минет в туалете
    if monicaMadeBlowjobToPhilip == True:
        philip "Я, конечно, не использую одну и ту же женщину дважды..."
        #
        $ notif(t_("Моника делала Филиппу минет в туалете"))
        #
        philip "Но у Вас я пробовал только ротик..."
        philip "Я решил, что неплохо было бы мне засунуть член в Ваше отверстие."
    else:
        # если Моника НЕ делала ему минет в туалете
        img 22954
        with diss
        m "Это не твое дело, Филипп! Мне без разницы, что ты там увидел..."
        img 22953
        with fade
        philip "Как что? Вашу прекрасную попу, Миссис Бакфетт!"
        philip "И я решил, что неплохо было бы мне засунуть член в Ваше отверстие."
        #

    music Power_Bots_Loop
    img 22954
    with diss
    mt "!!!"
    m "Даже не мечтай, Филипп! Ты никогда не сможешь этого сделать!"
    music Groove2_85
    img 22955
    with fade
    philip "Я всегда могу сделать это с Вами. За деньги."
    # Моника злится, говорит возмущенно
    img 22956
    with diss
    m "Ты меня считаешь проституткой?!"
    m "С чего ты взял, что меня можно купить?!"
    # Филипп, улыбаясь
    img 22957
    with fade
    philip "Я знаю это."
    philip "Я куплю Вашу киску за 300 долларов."
    music Pyro_Flow
    img 22958
    with diss
    mt "!!!"
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            m "Как ты смеешь предлагать мне подобное?"
            img 22959
            with fade
            m "Моя... Она стоит миллионы долларов!"
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 22960
            with diss
            mt "Мерзкий самовлюбленный извращенец!"
            m "Уходи отсюда и не порти мне аппетит!"
            mt "Сволочь!"
            music Groove2_85
            img 22961
            with fade
            philip "Вы уверены, Миссис Бакфетт?"
            img 22962
            with diss
            m "!!!"
            img 22963
            with fade
            philip "Хорошо, сейчас я уйду..."
            philip "Но в следующий раз..."
            music Pyro_Flow
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит, тот мерзко улыбается и уходит
            return
        "А почему 300?!":
            pass

    # Моника возмущенно
    img 22964
    with fade
    m "А почему 300?!"
    music Groove2_85
    img 22965
    with diss
    philip "Ну вот видите, Вы уже торгуетесь..."
    philip "Вы обычная шлюха, которую я сейчас куплю."
    music Pyro_Flow
    img 22966
    with fade
    m "Как ты смеешь такое обсуждать со мной?!"
    m "Я не шлюха! Меня нельзя купить!!!"
    music Groove2_85
    img 22967
    with diss
    philip "..." # улыбается
    img 22968
    with fade
    m "И вообще, почему 300?!"
    m "В прошлый раз ты предлагал 500 долларов и за меньшее!"
    m "Ты считаешь, что моя... Неважно... Что она стоит так мало?!"
    img 22969
    with diss
    philip "Ваши акции дешевеют, Миссис Бакфетт..."
    music Power_Bots_Loop
    img 22970
    with hpunch
    m "???"
    music Groove2_85
    img 22971
    with fade
    philip "Ваша киска сейчас стоит не более 100 долларов..."
    philip "И я делаю Вам щедрое предложение, предлагая 300."
    # Моника смотрит на него зло
    img 22972
    with diss
    mt "Черт!"
    mt "Мне нужны деньги..."
    mt "Но не таким же способом!"
    mt "!!!"
    mt "Какая же сволочь этот Филипп!"
    img 22973
    with fade
    m "..."
    m "Ты хочешь сделать это и рассказать всем?"
    img 22974
    with diss
    philip "Это не в моих интересах..."
    philip "Я не хочу, чтобы все знали, что я покупаю женщину так дешево."
    music Power_Bots_Loop
    img 22975
    with fade
    mt "!!!"
    music Groove2_85
    img 22976
    with diss
    philip "Миссис Бакфетт, вы закончили свою трапезу?"
    philip "Мы можем идти."
    img 22977
    with diss
    mt "Как он смеет такое мне предлагать?!"
    mt "С другой стороны, мне нужны деньги..."
    mt "Скоро я все верну и мне нельзя подрывать свою репутацию..."
    mt "А он сказал, что никому не расскажет об этом."
    mt "Что же мне делать?!"
    mt "Моника, неужели ты способна на такое пойти?!"
    mt "..."

    # Моника смотрит на него пристально
    music Groove2_85
    img 22978
    with fade
    philip "Мы можем идти."
    m "Если про это кто-то узнает - я тебя убью!"
    img 22979
    with diss
    philip "Не беспокойтесь, мой член бывал и не в таких местах..."
    philip "И при этом у меня все прекрасно."
    m "..."
    img 22980
    with fade
    m "Оплати мой счет."
    # Моника смотрит на него, тот ей улыбается в ответ
    img 22981
    with diss
    philip "Это повысит общую стоимость моих расходов, и они превысят стоимость Вашей киски."
    music Power_Bots_Loop
    m "Мерзавец!"
    m "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Poppers_and_Prosecco
    img 22982
    with fadelong
    philip "Пойдемте, Миссис Бакфетт. Думаю, что мне пора попробовать Вашу киску."
    return

label gallery_23018:

    # Моника заказывает еду у официантки ( ep26_dialogues4_restaurant - разговор с официанткой и заказ еды)
    # пока ждет, когда принесут ее заказ, сидит на стуле с задумчивым видом
    music Poppers_and_Prosecco
    img 22983
    with fadelong
    mt "Надеюсь, я не увижу этого извращенца Филиппа сегодня..."
    mt "Это было ужасно!"
    mt "Как он посмел так со мной обращаться?!"
    mt "Сволочь!"
    mt "Почему меня, такую добрую и красивую женщину, окружают одни подлецы?!"
    # ее мысли прерывает мужской голос
    img 22984
    with fade
    hotel_staff "Мэм... Добрый вечер, Мэм..."
    # Моника смотрит на него вопросительно, тот стоит, смущаясь
    m "Что?"
    # если не было сцены в туалете с Филиппом и со служащим отеля
    mt "Что могло понадобиться этому неудачнику от меня?!"

    # если была сцена в туалете
    if monicaMadeBlowjobToPhilip == True:
        music Pyro_Flow
        img 22985
        with diss
        mt "Я помню этого неудачника!"
        #
        $ notif(t_("Моника делала минет Филиппу в туалете"))
        #
        mt "Это он тогда был в туалете, когда я..."
        mt "Когда мерзавец Филипп заставил меня..."
        mt "Делать всякие его извращенские гадости!"
        #

    music Groove2_85
    img 22986
    with fade
    hotel_staff "Один наш очень уважаемый клиент сказал мне, что..."
    hotel_staff "..."
    m "Что?"
    img 22987
    with diss
    hotel_staff "Кхм... Что я могу договориться и..."
    hotel_staff "Вам не нужно будет оплачивать Ваш ужин, Мэм."
    img 22988
    with fade
    m "???" # удивленно
    m "Ужин за счет ресторана?"
    img 22989
    with diss
    mt "Может быть, кто-то из моих поклонников решил таким образом сделать мне приятное?"
    mt "Тогда почему этот никчемный представитель обслуживающего персонала мне об этом сообщает?"
    mt "А не администратор или, хотя бы, официант?"
    mt "Странно это все..."
    m "..."
    img 22990
    with fade
    hotel_staff "Так Вы позволите, Мэм?"
    m "Что позволю?"
    # парень еще больше смутившись
    img 22991
    with diss
    hotel_staff "..."
    hotel_staff "Мистер Филипп сказал мне, что если я... Кхм..."
    music Pyro_Flow
    img 22992
    with fade
    mt "!!!"
    music Groove2_85
    img 22993
    with diss
    hotel_staff "Если я договорюсь, что Ваш ужин будет бесплатным для Вас, то..."
    hotel_staff "Тогда вы пойдете со мной. И за 50 долларов проведете со мной время..."
    hotel_staff "В каком-нибудь уединенном месте."
    hotel_staff "Я знаю одно такое место, Мэм."
    # Моника в шоке
    music Power_Bots_Loop
    img 22994
    with hpunch
    m "ЧТО???"
    m "Филипп?!"
    music Groove2_85
    img 22995
    with fade
    hotel_staff "Да, Мэм."
    mt "!!!"
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            music Power_Bots_Loop
            img 22996
            with hpunch
            m "Я поверить не могу!"
            m "Халдей, как ты смеешь предлагать мне подобное?!"
            m "Как ты вообще посмел подойти к МОЕМУ столику?!"
            m "И заговорить со МНОЙ?!"
            m "!!!"
            img 22997
            with fade
            m "Никчемный неудачник!"
            m "Еще слово - и я сделаю так. Что тебя сегодня же вышвырнут с этой работы!!!"
            m "Пошел вон отсюда!!!"
            m "!!!"
            # Моника зло на него смотрит, тот вконец смутившись, уходит
            return
        "50 долларов?!":
            pass
    # Моника возмущенно спрашивает

    m "50 долларов?!"
    music Pyro_Flow
    img 22998
    with diss
    mt "Мало того, что этот мерзавец сказал этому неудачнику..."
    mt "Что можно купить меня..."
    mt "Так еще и за 50 долларов!!!"
    img 22999
    with fade
    m "!!!"
    m "За 50 долларов ты можешь пойти и сам с собой провести время!"
    music Groove2_85
    img 23000
    with diss
    hotel_staff "Мэм, но ведь... Помимо этих 50 долларов..."
    hotel_staff "Вам не нужно будет оплачивать Ваш чек."
    img 23001
    with fade
    m "И что?!"
    m "Ужин я и сама могу оплатить!"
    img 23002
    with diss
    mt "Хотя ужинать здесь чертовски дорого для меня сейчас..."
    img 23003
    with fade
    hotel_staff "Я готов дать вам 55 долларов, Мэм."
    hotel_staff "Извините, но у меня просто больше нет денег."
    hotel_staff "55 долларов и бесплатный ужин."
    # Моника зло смотрит на него
    img 23004
    with diss
    mt "Это все отвратительно и мерзко!"
    mt "С другой стороны... 55 долларов... Они не будут лишними."
    mt "А если кто-нибудь узнает?!"
    img 23005
    with fade
    m "..."
    m "Я не могу согласиться на такое..."
    img 23006
    with diss
    hotel_staff "Мэм, Вы можете не переживать. Об этом никто не узнает."
    # Моника молчит и смотрит на него с подозрением
    img 23007
    with diss
    mt "Черт! Мне действительно нужны эти деньги..."
    mt "Я могу пригрозить этому неудачнику увольнением, если он кому-то расскажет..."
    mt "Тогда он испугается и об этом никто никогда не узнает."
    mt "Зато у меня прибавится 55 долларов. Плюс бесплатный ужин."
    mt "И я не собираюсь делать ничего из такого, что требовал Филипп от меня..."
    mt "..."
    # говорит служащему с угрозой

    music Pyro_Flow
    img 23008
    with fade
    m "Ты пожалеешь, если расскажешь об этом хоть одной живой душе!"
    m "Я сделаю так, что тебя выкинут с работы!"
    if monicaWorkingAsDishwasher == True:
        m "И ты после этого не сможешь устроиться на работу даже..."
        # если работала в пабе посудомойщицей
        #
        $ notif(t_("Моника работает посудомойщицей в Shiny Hole"))
        #
        m "Даже посудомойщиком в какой-нибудь грязной дыре в трущобах!"


    img 23009
    with diss
    m "Думаю, ты догадываешься о том..."
    m "Что у меня много знакомых, которые легко смогут это устроить..."
    m "Я большой и влиятельный человек в этом городе!"
    music Groove2_85
    img 23010
    with fade
    hotel_staff "Конечно, Мэм! Я никому не скажу, Мэм!"
    hotel_staff "Сотрудникам отеля запрещено пользоваться услугами проституток. За это могут уволить..."
    # Моника возмущенно
    music Power_Bots_Loop
    img 23011
    with diss
    m "Проституток?!"
    m "!!!"
    m "По-твоему, я проститутка?!"
    # парень испугавшись, что сморозил что-то не то
    music Groove2_85
    img 23012
    with fade
    hotel_staff "Нет, Мэм! Конечно, нет!!!"
    hotel_staff "Просто..."
    hotel_staff "Никто из руководства разбираться не будет."
    hotel_staff "Меня просто уволят и все."
    # Моника грозно смотрит на него
    img 23013
    with diss
    m "Что за уединенное место?"
    m "..."
    m "Если это какой-то туалет, то даже не думай!"
    # парень радостно
    hotel_staff "Мэм, я взял ключи от пустого роскошного номера..."
    hotel_staff "Мы можем пройти туда незаметно. Нас никто не увидит..."
    # Моника задумчиво смотрит на него
    img 23014
    with fade
    mt "Хм... В таком случае..."
    mt "Минимален риск того, что меня кто-нибудь увидит и..."
    mt "Догадается, что я оказала услугу за деньги этому неудачнику."
    m "..."
    img 23015
    with diss
    hotel_staff "..."
    hotel_staff "Мэм? Могу я Вас пригласить в этот номер?"
    # Моника бросает на него еще один грозный взгляд
    music Pyro_Flow
    img 23016
    with fade
    m "Я тебя предупредила, если кто-нибудь узнает..."
    m "!!!"
    music Groove2_85
    img 23017
    with diss
    hotel_staff "Не переживайте, Мэм. Об этом никто никогда не узнает."
    hotel_staff "Пойдемте, Мэм?"
    music stop
    img black_screen
    with diss
    pause 2.0
    music Poppers_and_Prosecco
    # Моника встает и идет за служащим
    img 23018
    with fadelong
    sound highheels_short_walk
    w
    return

label gallery_16086:
    # Моника с Филиппом стоят в туалете
    music Groove2_85
    if monicaMadeBlowjobToPhilip == True:
        # если Моника делала ему минет в туалете
        img 16086
        with fadelong
        sound highheels_short_walk
        m "Снова это жуткое место..."
        #
        $ notif(t_("Моника делала Филиппу минет в туалете"))
        #
        m "Неужели нельзя было в этот раз подобрать место получше?!"
        img 16087
        with fade
        philip "Гостиничный номер будет стоить гораздо дороже Вашей киски!"
        philip "Как Вы знаете, я умею считать деньги!"
    else:
        # если Моника НЕ делала ему минет в туалете
        img 16086
        with fadelong
        sound highheels_short_walk
        m "Куда ты меня привел, Филипп?"
        m "Это мужской туалет!"
        img 16087
        with fade
        philip "Миссис Бакфетт!"
        philip "Мне будет неудобно находиться в женском туалете!"
        philip "Ну а для Вас, полагаю, нет никакой разницы, ведь так?"
        img 16088
        with diss
        m "Я думала это будет хотя бы гостиничный номер!"
        img 16089
        with fade
        philip "Гостиничный номер будет стоить гораздо дороже Вашей киски!"
        philip "Как Вы знаете, я умею считать деньги!"
        philip "Поэтому туалет как раз подойдет для этой цели!"
        #

    # Моника зло на него смотрит
    img 16090
    with diss
    philip "Задирайте платье, Миссис Бакфетт. Покажите мне Вашу киску."
    music Pyro_Flow
    m "!!!"
    m "Что, прямо вот так?! Так быстро?!"
    music Groove2_85
    img 16091
    with fade
    philip "Да. Я это купил и это уже мое."
    img 16092
    with diss
    mt "Мерзавец!"
    m "..."
    img 16093
    with fade
    menu:
        "Уйти!":
            # Монику бомбит
            music Pyro_Flow
            img 16094
            with diss
            m "Как ты смеешь так со мной обращаться?!"
            m "Моя... Она стоит миллионы долларов!"
            img 16095
            with fade
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 16096
            with diss
            mt "Мерзкий самовлюбленный извращенец!"
            mt "Сволочь!"
            music Groove2_85
            img 16097
            with fade
            philip "Вы уверены, Миссис Бакфетт?"
            img 16098
            with diss
            m "!!!"
            philip "Хорошо..."
            philip "Но в следующий раз..."
            music Pyro_Flow
            img 16099
            with fade
            sound highheels_short_walk
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return
        "Ударить мерзавца и уйти! (прерывание квеста)":
            label gallery_16102:
            # Монику бомбит, она подходит к нему ближе и орет на него
            music Power_Bots_Loop
            img 16094
            with diss
            m "Как ты смеешь так со мной обращаться?!"
            m "Мерзкий самовлюбленный извращенец!"
            m "!!!"
            # бьет между ног коленом
            sound anger2
            img 16100
            w
            sound snd_kick_fred1
            img 16101
            with diss

            m "Сволочь!"
            m "!!!"
            sound snd_fred_argh
            img 16102
            with diss
            philip "АААААААА!!!" # падает
            philip "Сучка!!!"
            img 16103
            with fade
            m "Да пошел ты, придурок!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return
        "Задрать платье.":
            pass
    # Моника неуверенно поворачивается к нему задом и задирает платье немного
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16104
    with fadelong
    philip "Это никуда не годится, Миссис Бакфетт..."
    philip "Я за это и цента не заплачу."
    img 16105
    with fade
    philip "Поднимай платье еще выше."
    # Моника задирает его до талии и стоит перед ним с голой попой
    label gallery_16115:
    music Loved_Up
    img 16106
    with diss
    sound snd_fabric1
    w
    img 16107
    with diss
    philip "А теперь предложите мне себя..."
    philip "Раздвиньте ноги и покажите мне, что там между ними."
    # Моника злится
    music Groove2_85
    img 16108
    with fade
    m "!!!"
    m "Но..."
    img 16109
    with diss
    philip "Никаких 'но'. Будете много разговаривать, ничего не заработаете."
    philip "Раздвигайте ноги!"
    mt "!!!"
    img 16110
    with diss

    music Pyro_Flow
    # Моника нагибается и раздвигает ноги
    img 16111
    with fade
    mt "Ненавижу!!!"
    # он расстегивает ширинку и достает член
    music stop
    img black_screen
    with diss
    sound snd_zip
    pause 1.0
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16112
    with fadelong
    philip "Давно я не трахал таких 'леди' в туалете ресторана."
    m "!!!"
    # подходит к ней ближе и засовывает член в нее
    # Моника в ужасе, но не сопротивляется
    img 16113
    with fade
    mt "Я постараюсь это сейчас перетерпеть, потому что мне нужны деньги."
    mt "Но потом я ему отомщу!"
    mt "Он будет одним из первых, кого Моника Бакфетт накажет за все его мерзкие поступки!"
    # секс с Филиппом
    sound chpok6
    img 16114
    with hpunch
    w
    music stop
    music2 Loved_Up2
    img 16115
    with fade
    w
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_1 = Movie(play="video/v_Monica_Philip_Sex2_1.mkv", fps=30)
    show videov_Monica_Philip_Sex2_1
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_2 = Movie(play="video/v_Monica_Philip_Sex2_2.mkv", fps=30)
    show videov_Monica_Philip_Sex2_2
    with fade
    philip "У Вас неплохая киска, Миссис Бакфетт..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_3 = Movie(play="video/v_Monica_Philip_Sex2_3.mkv", fps=30)
    show videov_Monica_Philip_Sex2_3
    with fade
    philip "Конечно, она не стоит 300 долларов..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_4 = Movie(play="video/v_Monica_Philip_Sex2_4.mkv", fps=30)
    show videov_Monica_Philip_Sex2_4
    with fade
    philip "Но все же..."
    philip "Ммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16116
    with diss
    w
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_5 = Movie(play="video/v_Monica_Philip_Sex2_5.mkv", fps=30)
    show videov_Monica_Philip_Sex2_5
    with fade
    philip "Мне приятно Вас трахать, Миссис Бакфетт..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    if game.extra == True:
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_Philip_Sex2_6 = Movie(play="video/v_Monica_Philip_Sex2_6.mkv", fps=30)
        show videov_Monica_Philip_Sex2_6
        with fade
        philip "Думаю, это не последняя наша с Вами встреча..."
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_Philip_Sex2_7 = Movie(play="video/v_Monica_Philip_Sex2_7.mkv", fps=30)
        show videov_Monica_Philip_Sex2_7
        with fade
        philip "Ммммм..."
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_8 = Movie(play="video/v_Monica_Philip_Sex2_8.mkv", fps=30)
    show videov_Monica_Philip_Sex2_8
    with fade
    wclean
    stop music
    music stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    sound ahhh11
    img 16117
    with fade
    philip "Даааа..."
    # кончает
    img 16118
    with diss
    philip "АААААААА!!!"
    w
    img 16119
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 16120
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    img 16121
    with fade
    w
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    # кадр меняется, Филипп с застегнутой ширинкой, Моника с недовольным видом поправляет платье
    img 16122
    with fadelong
    philip "Неплохо, Миссис Бакфетт..."
    philip "Можете забирать свои деньги."
    # кладет деньги куда-нибудь на столик или раковины
    img 16123
    with fade
    m "Мерзавец!"
    m "!!!"
    img 16124
    with diss
    philip "Вы знаете, Миссис Бакфетт..."
    philip "Я готов сделать исключение из своего правила не использовать одну и ту же женщину дважды..."
    # протягивает ей свою визитку
    img 16125
    with fade
    m "???"
    m "Что это значит?"
    img 16126
    with diss
    philip "Это значит, что мне нужна шлюха выходного дня."
    music Pyro_Flow
    img 16127
    with fade
    m "Что за мерзкое название?"
    img 16098
    with diss
    philip "Я предлагаю Вам быть моей личной шлюхой, которая приходит ко мне по субботам..."
    m "!!!"
    music Groove2_85
    img 16128
    with fade
    philip "Это исключение, которое я делаю далеко немногим."
    philip "Будешь приходить в субботу. Остальные дни у меня расписаны."
    philip "Вообще, субботняя шлюха у меня уже есть... Но она иногда по субботам приходить не может."
    img 16091
    with diss
    philip "Поэтому Вы, Миссис Бакфетт, будете субботней шлюхой номер два... На замену."
    philip "Придете ко мне вечером в субботу. Я плачу 100 долларов за вечер."
    music Power_Bots_Loop
    img 16095
    with fade
    m "!!!"
    m "Я никогда на такое не пойду!"
    # Моника злобно смотрит на него, тот улыбается мерзкой улыбочкой
    music Groove2_85
    img 16129
    with diss
    philip "Не забудьте, Миссис Бакфетт! Вечером в субботу."
    music Power_Bots_Loop
    img 16099
    with fade
    sound highheels_short_walk
    m "Иди к черту!"
    m "!!!"
    # Моника уходит
#    $ log1 = t_("У меня появилась возможность дополнительного заработка по субботам. У Филиппа. Но смогу ли я?") # квест лог
    return

label gallery_16262:

    # Моника оглядывается с отвращением

    music Pyro_Flow
    img 16256
    with fadelong
    m "Это и есть твое уединенное место?!"
    m "Это что вообще?! Служебный коридор?!"
    img 16257
    with fade
    m "!!!"
    m "Ты же говорил, что у тебя есть ключи от номера..."
    # служащий, смущаясь
    music Groove2_85
    img 16258
    with diss
    hotel_staff "Это у мистера Филиппа есть деньги на номер в отеле."
    hotel_staff "Он водит в специальные номера всех девушек, которые стоят больше $ 100."
    hotel_staff "А я всего лишь служащий здесь и у меня нет столько денег."
    img 16259
    with diss
    hotel_staff "Если бы я сразу сказал, что это обычный коридор..."
    hotel_staff "То Вы не согласились бы, Мэм."
    hotel_staff "Однако, прошу Вас, поверьте! Здесь никто никогда не ходит!"
    # Моника оглядывается, при этом думает
    img 16260
    with fade
    mt "У этого мерзавца Филиппа совести и денег хватает только на грязный туалет!"
    mt "Сволочь! Наговорил этому неудачнику непонятно что про меня!!!"
    mt "..."
    music Pyro_Flow
    img 16261
    with diss
    mt "Стоп... Он водит в номера только тех, кто стоит дороже $ 100???"
    mt "Но Я... Вот сволочь!!!"
    mt "Ненавижу его!"
    music Groove2_85
    img 16262
    with fade
    hotel_staff "Кхм..." # Моника смотрит на него
    hotel_staff "Мэм, мне очень хотелось бы, чтобы Вы..."
    hotel_staff "Поработали своим ротиком..." # очень смущается

    # если Халдей имел blowjob с Моникой
    if monicaMadeBlowjobToHotelStaff == True:
        img 16263
        with diss
        hotel_staff "У Вас очень удобный для члена ротик..."
        #
        $ notif(t_("Моника по приказу Филиппа делала служащему отеля минет в туалете"))
        #
        hotel_staff "Мне в прошлый раз очень понравилось..."
        hotel_staff "И мне хочется повторить..."

    if monicaMadeBlowjobToPhilip == True and hotelStaffOffended1 == False:
        # Моника хорошо относилась к Халдею и он ушел, не став оставаться на сцену
        img 16263
        with diss
        hotel_staff "У Вас очень удобный для члена ротик..."
        #
        $ notif(t_("Моника была вежлива со служащим отеля и он не остался в туалете, как предлагал ему Филипп."))
        #
        music Power_Bots_Loop
        # Моника возмущенно
        img 16264
        with hpunch
        m "Что?!"
        m "Да как ты смеешь так со мной говорить?!"
        m "!!!"
        music Groove2_85
        img 16265
        with fade
        hotel_staff "Но, Мэм..."
        hotel_staff "Так сказал мистер Филипп. А еще он сказал, что Вы согласитесь..."
        hotel_staff "Я отказался от Вашего предложения в прошлый раз..."
        img 16266
        with diss
        hotel_staff "Но потом жалел об этом. Я... Я передумал."
        hotel_staff "И хочу, чтобы Вы сделали это, Мэм..."
        mt "Этот неудачник Филипп еще пожалеет об этом!"
        #

    img 16267
    with diss
    mt "!!!"
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            music Power_Bots_Loop
            img 16268
            with fade
            m "Как ты смеешь предлагать мне подобное?!"
            m "!!!"
            m "Никчемный неудачник!"
            sound highheels_short_walk
            img 16269
            with diss
            m "Оставь себе свои 55 долларов и развлекай себя сам!"
            m "Я ни за что не стану делать этого!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return
        "Сделать ему минет.":

            pass
    # служащий мнется и стесняется
    img 16270
    with fade
    hotel_staff "Мэм, простите, что я говорю что-то не так..."
    hotel_staff "Просто я очень... Стесняюсь... И никак не хотел Вас обидеть."
    hotel_staff "..."
    music Pyro_Flow
    img 16271
    with diss
    m "Ну и отлично! Тогда я пошла."
    img 16272
    with diss
    mt "Достаточно и того, что мне не нужно оплачивать чек."
    music Groove2_85
    img 16273
    with fade
    hotel_staff "Мэм, в таком случае. Я вынужден буду сообщить охране, что Вы не оплатили свой чек."
    # при этом он снимает штаны и смотрит на нее выжидающе
    music Pyro_Flow
    img 16274
    with diss
    m "Никчемный сотрудник никчемного отеля!"
    sound snd_fabric1
    img 16275
    with fade
    hotel_staff "Мэм, простите, но я жду, когда Вы начнете..."
    music Pyro_Flow
    img 16276
    with diss
    mt "Черт! И зачем я только согласилась?!"
    # Моника подходит к нему, смотрит на него
    sound highheels_short_walk
    img 16277
    with fade
    mt "Моника, неужели ты сейчас сделаешь это?!"
    mt "Но ведь 55 долларов не будут лишними..."
    img 16278
    with diss
    mt "Да и я уже свыклась с мыслью, что мне не надо платить за счет в ресторане..."
    mt "..."
    mt "К черту! Все-равно об этом никто не узнает..."
    img 16279
    with diss
    mt "А я в такой ситуации, когда приходится идти на жертвы..."
    mt "Хотя я никогда не предполагала, что жертвой будет необходимость трогать член какого-то халдея..."
    mt "Моими восхитительными губами... О БОЖЕ!!!"
    label gallery_16283:
    music Groove2_85
    img 16280
    with fade
    hotel_staff "Мэм... Простите... Я жду..."
    hotel_staff "Мне надо скорее закончить, ведь меня ждут важные дела..."
    hotel_staff "В отеле много гостей и мне надо предложить каждому отести его одежду в гардероб..."
    img 16281
    with diss
    mt "Это... Важные дела?!"
    mt "Он считает это важнее того, что перед ним стою Я?!"
    img 16282
    with fade
    hotel_staff "Мэм. Если Вы не решитесь, то я вынужден буду уйти."
    hotel_staff "А Вы - платить за счет в ресторане..."
    mt "!!!"
    # опускается перед ним на колени и берет его член в рот, начинает делать ему минет
    music stop
    img black_screen
    with diss
    pause 1.5
    sound chpok6
    pause 1.0
    music2 Loved_Up2
    img 16283
    with fadelong
    hotel_staff "ОООООО!!!"

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_1 = Movie(play="video/v_Monica_Helper_Blowjob_2_1.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16284
    with fade
    hotel_staff "Какой каааайф!"
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_2 = Movie(play="video/v_Monica_Helper_Blowjob_2_2.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16285
    with diss
    hotel_staff "ААААААХ! О, Мэм, сделайте так еще раз!"
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_3 = Movie(play="video/v_Monica_Helper_Blowjob_2_3.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16286
    with fade
    hotel_staff "Да, еще-еще!"
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_4 = Movie(play="video/v_Monica_Helper_Blowjob_2_4.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16287
    with diss
    hotel_staff "МММММММ!"
    if game.extra == True:
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
        scene black
        image videov_Monica_Helper_Blowjob_2_5 = Movie(play="video/v_Monica_Helper_Blowjob_2_5.mkv", fps=30)
        show videov_Monica_Helper_Blowjob_2_5
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_6 = Movie(play="video/v_Monica_Helper_Blowjob_2_6.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_6
    with fade
    wclean
    stop music
    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    # заходит китаянка-админ, грозно смотрит на служащего
    sound plastinka1b
    music stop
    label gallery_16292:
    music Villainous_Treachery
    img 16288
    with hpunch
    reception "Ага!!! Я так и знала!!!"
    reception "Тебе нельзя пользоваться услугами нелегальных шлюх!"
    sound Jump2
    img 16289
    with hpunch
    hotel_staff "А... Что... Нет-нет!"
    hotel_staff "Я не..."
    sound snd_runaway
    img 16290
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Pyro_Flow
    # не договаривает, убегает, на ходу натягивая штаны
    # админ смотрит теперь на Монику, та испугана
    img 16291
    with fadelong
    reception "И кто посмел оказывать этому халдею такие услуги?!"
    reception "Ага! Я так и знала, что это ты, шлюха!"
    img 16292
    with fade
    reception "Еще раз тут появишься - сдам тебя полиции!!!"
    reception "А сейчас быстро пошла отсюда, пока я не позвала охрану!"
    # Моника смотрит на нее зло и уходит (вытирая рот)
    img 16293
    with diss
    mt "!!!"
    return

label gallery_16340:

    # в коридоре стоят или сидят все девочки, их четверо, Моника с китаянкой стоят перед ними

    music Groove2_85
    img 16321
    with fadelong
    sound highheels_short_walk
    w
    img 16322
    with fade
    reception "У нас тут дружный коллектив."
    reception "Поэтому все девочки должны одобрить твою кандидатуру."
    img 16323
    with diss
    girl_1 "А, это она... Я тут раньше ее видела..." # брюнетка, каре с челкой - смотрит нагло
    img 16324
    with fade
    girl_2 "Я так и знала, что она не просто посетитель, а работает здесь..." # рыжая с каре - равнодушно
    img 16325
    with diss
    girl_3 "Она и правда тут работала?!" # шатенка с хвостом - удивляется
    # girl_4 - брюнетка с длинными волосами, молча смотрит надменно
    img 16326
    with fade
    reception "Да, девочки. Я вывела ее на чистую воду."
    reception "Она пыталась отобрать у вас клиентов."
    img 16327
    with diss
    reception "Теперь она хочет стать одной из вас."
    reception "Подходит она или нет? Как вы считаете?"
    # Моника спрашивает у китаянки
    img 16328
    with fade
    m "Эти девушки что, все работают здесь?"
    img 16329
    with diss
    reception "Да. И работают они легально."
    reception "В отличие от тебя!"
    img 16330
    with fade
    mt "..."
    mt "Черт! По-моему, они не очень дружелюбно настроены..."
    # девочки начинают возмущаться
    music Groove2_85
    img 16331
    with diss
    girl_4 "Нас и так много..."
    girl_4 "Зачем нам еще одна? Еще и такая?" # надменно
    img 16332
    with fade
    girl_1 "Согласна. Она пыталась отнять у нас наш заработок!" # критикуя
    girl_3 "Да ладно. Пусть разденется. Давайте посмотрим сначала на нее." # с любобытством
    girl_1 "Да. Вдруг у нее жирная задница?"
    music Power_Bots_Loop
    img 16333
    with diss
    mt "!!!"
    mt "На свою задницу посмотрела бы!"
    mt "Сучка!"
    music Groove2_85
    img 16334
    with diss
    reception "Да. Давай, раздевайся!"
    mt "???"
    menu:
        "Что за бред?! Я не собираюсь раздеваться!":
            # Моника высокомерно
            music Pyro_Flow
            img 16335
            with fade
            m "Ты сейчас серьезно?!"
            m "Я должна раздеться, чтобы эти..."
            m "Эти девушки..."
            m "Решали, подойду я для работы или нет?!"
            m "!!!"
            img 16336
            with diss
            m "Я!"
            m "Не собираюсь!"
            m "Раздеваться перед вами!"
            m "К черту ваш второсортный отель и ваши правила!"
            img 16337
            with fade
            m "В отличие от вас всех я умная..."
            m "И легко найду другой способ заработать деньги!"
            # Моника зло на нее смотрит и уходит
            img 16338
            with diss
            reception "Посмотрим, как много ты заработаешь..." # ехидно
            reception "На нищих с улицы!"
            sound highheels_short_walk
            img 16339
            with fade
            reception "Когда в кармане не останется ни цента..."
            reception "Ты знаешь, к кому обращаться." # Монике вслед
            # Моника поворачивает, бросает злобный взгляд
            m "Сучка!!!"
            # уходит
            return
        "Раздеться.":
            pass
    # Моника раздевается и стоит перед девочками голая, прикрываясь
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16340
    with fadelong
    w
    img 16341
    with fade
    mt "!!!"
    mt "Эти сучки осматривают меня, как товар."
    mt "Как это мерзко!"
    # девочки ее обсуждают
    music Groove2_85
    img 16342
    with diss
    girl_2 "А она красивая..." # равнодушно
    girl_1 "Да ну! А вдруг у нее задница жирная?" # критикуя
    girl_3 "А ну-ка повернись!" # с любобытством
    # girl_4 смотрит надменно
    img 16343
    with diss
    reception "Чего стоишь?! Поворачивайся!"
    mt "!!!"
    # Моника поворачивается
    music Loved_Up
    img 16344
    with fadelong
    w
    img 16345
    with diss
    girl_3 "Ну смотри, у нее отличная задница!"
    girl_1 "Ну и что? Зачем нам еще одна нужна?"
    girl_1 "Да, девочки? Зачем она нам?"
    girl_2 "Ага..." # равнодушно
    music Groove2_85
    img 16346
    with fade
    reception "Послушайте, вы всегда отказываетесь обслуживать проблемных клиентов..."
    girl_3 "Пффф... С какой стати мы должны обслуживать всяких козлов?!"
    img 16347
    with diss
    reception "А у нас приличное заведение с отличной репутацией."
    reception "Ни один клиент не должен уйти неудовлетворенным, даже проблемный!"
    img 16348
    with fade
    girl_4 "Ты хочешь, чтобы она работала с проблемными? Не отбирала наших?" # с насмешливой легкой улыбкой
    img 16349
    with diss
    reception "Да, все верно."
    mt "!!!"
    reception "Она провинилась и ей нужно сначала заслужить наше доверие."
    reception "Поэтому она будет работать с проблемными клиентами!"
    music Pyro_Flow
    img 16350
    with fade
    mt "О боже! Они хотят меня отправить ко всяким извращенцам!!!"
    mt "С которыми сами не хотят работать!!!"
    mt "!!!"
    music Groove2_85
    img 16351
    with diss
    girl_4 "Думаю, это хорошая идея..."
    img 16352
    with fade
    girl_1 "Давно надо было так сделать!"
    girl_3 "Да, я согласна с девочками! А ты что скажешь?" # спрашивает у girl_2
    img 16353
    with diss
    girl_2 "Ага. Я тоже так считаю..."
    # админ обращается к Монике
    img 16354
    with fade
    reception "Можешь одеться."
    # кадр меняется. Моника стоит на том же месте, уже в одежде
    m "..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16355
    with fadelong
    reception "Ну что? Ты согласна работать с теми, кого мы тебе дадим?"
    reception "У нас здесь строгие правила."
    reception "Будешь зарабатывать 50 процентов от суммы, оплаченной клиентом."
    img 16330
    with fade
    mt "50 процентов? Всего?"
    m "..."
    img 16356
    with diss
    reception "Решение по вопросу чаевых принимается отдельно."
    reception "Нельзя говорить 'нет' клиентам."
    reception "Любая запрошенная услуга, если она есть в прайсе, должна быть оказана!"
    img 16357
    with fade
    reception "А в нашем прайсе есть практически все!"
    reception "За отказ или грубость к клиенту - предупреждение или увольнение."
    reception "И еще у тебя нет права выбирать клиентов, как у других девушек."
    mt "!!!"
    img 16358
    with diss
    reception "Тебе нужно просто сидеть за столиком. Клиент сам подойдет к тебе."
    reception "А если поступит вызов, то тебя позовут."
    img 16334
    with fade
    reception "Если согласна на такие условия..."
    reception "То завтра можешь приступать к работе."
    img 16359
    with diss
    mt "..."
    menu:
        "Нет. Я не смогу.":
            # Моника нерешительно
            music Pyro_Flow
            img 16360
            with fade
            mt "Она сказала, что у меня будут проблемные клиенты..."
            mt "Значит, будут одни извращенцы."
            img 16361
            with diss
            mt "Неизвестно, чего мне от них ожидать..."
            mt "Нет! Я не могу согласиться на такое!"
            music Groove2_85
            img 16335
            with fade
            m "Я..."
            m "Я не смогу..."
            m "Мне нужно время, чтобы подумать..."
            img 16338
            with diss
            reception "Здесь у тебя будет неплохой заработок..."
            reception "Если, конечно, будешь хорошо себя вести с клиентами."
            img 16339
            with fade
            reception "Подумай..."
            reception "Ты знаешь, где меня найти."
            # Моника уходит
            return
        "Согласиться.":
            pass
    # Моника сомневаясь
    music Pyro_Flow
    img 16361
    with fade
    mt "Она сказала, что у меня будут проблемные клиенты..."
    mt "Значит, будут одни извращенцы."
    mt "Неизвестно, чего мне от них ожидать..."
    mt "..."
    img 16360
    with diss
    mt "С другой стороны, мне нужны деньги."
    mt "А 50 процентов от суммы, которую платит здесь клиент - это немало."
    mt "Мне ничего не мешает сейчас согласиться..."
    mt "А если что-то пойдет не так с клиентом, я просто уйду отсюда и все."
    mt "Мне нужно попытаться заработать хоть какие-то деньги..."
    # Моника нерешительно
    music Groove2_85
    img 16322
    with fade
    m "Я..."
    m "Согласна на любую работу."
    m "Обещаю, что не буду отбирать у девочек их клиентов."
    # брюнетка с каре
    img 16362
    with diss
    girl_1 "Да зачем она нам нужна?!"
    girl_1 "Давай, не будем ее брать!"
    img 16363
    with fade
    reception "Все! Решение принято, вопрос закрыт!" # обращаясь к girl_1
    reception "Все, девочки! Расходимся! Пора работать!"
    # девочки расходятся и смотрят на Монику, кто с любопытством, кто надменно
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 0.5
    sound highheels_short_walk
    music Groove2_85
    img 16364
    with fadelong
    w
    sound highheels_short_walk
    img 16365
    with fade
    girl_4 "Добро пожаловать в наш дружный коллектив." # насмешливо, проходя мимо Моники
    music Pyro_Flow
    mt "!!!" # смотрит на нее подозрительно
    img 16366
    with diss
    mt "Они тут все сучки! А эта - особенно."
    m "..."
    music Groove2_85
    img 16326
    with fade
    reception "Да, совсем забыла... Как тебя зовут то?"
    img 16328
    with diss
    m "Меня зовут..."

    m "Меня зовут [monica_hotel_name]."
    # девочки разошлись, админ обращается к Монике
    img 16329
    with fade
    reception "Завтра жду тебя на работе, [monica_hotel_name]!"
#    $ log1 = t_("Прийти в отель ЛеГранд завтра.")
#    $ log1 = t_("Мне предложили работу в эскорте! Неужели я решусь на такое?! Хотя... Там можно неплохо заработать.") # квест лог
    return

label gallery_16404:

    # Филипп садится на диван перед ТВ
    music Groove2_85
    img 16385
    with fadelong
    philip "У меня была тяжелая неделя."
    philip "Я хочу, чтобы шлюха номер 2 расслабила меня своим ротиком."
    mt "..."
    # он берет пульт от ТВ и смотрит телевизор
    music Pyro_Flow
    img 16386
    with fade
    mt "Моника, неужели ты способна на такое пойти?!"
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16387
            with diss
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16388
            with fade
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            sound highheels_short_walk
            img 16389
            with diss
            m "!!!"
            # Моника уходит
            return
        "Сделать, что требует Филипп.":
            pass
    # Филипп поворачивается к Монике
    music Groove2_85
    img 16390
    with diss
    m "..."
    philip "В чем дело? Мне долго еще ждать?"
    img 16387
    with fade
    mt "..."
    mt "Боже! Как же это все омерзительно!"
    mt "Но мне нужны эти деньги..."
    # Моника подходит к дивану, на котором сидит Филипп, и опускается перед ним на колени
    img 16391
    with diss
    philip "Открывай свой ротик и приступай к работе."
    # расстегивает ширинку, достает член и продолжает смотреть в ТВ
    music stop
    img black_screen
    with diss
    sound snd_zip
    pause 1.5
    music Groove2_85
    img 16392
    with fade
    m "Я тебе буду делать это... А ты... Будешь смотреть телевизор?!"
    m "!!!"
    img 16393
    with diss
    philip "Это тебя не касается."
    philip "Шлюха номер 2 должна отрабатывать свои деньги..."
    philip "А не задавать мне глупые вопросы."
    music Power_Bots_Loop
    img 16394
    with fade
    mt "!!!"
    mt "Мерзавец!"
    mt "Ненавижу!!!"
    # Моника берет в рот его член, Филипп в это время продолжает смотреть ТВ со скучающим видом
    # минет
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound chpok6
    pause 1.0
    music2 Loved_Up

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
    scene black
    image videov_Monica_Philip_Blowjob2_1 = Movie(play="video/v_Monica_Philip_Blowjob2_1.mkv", fps=30)
    show videov_Monica_Philip_Blowjob2_1
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16395
    with fadelong
    philip "Да... Вот так..."
    img 16396
    with fade
    w
    sound keyboard
    img 16397
    with diss
    w
    sound keyboard
    img 16398
    with diss
    w
    sound keyboard
    img 16399
    with fade
    philip "Возьми его глубже..."
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
    scene black
    image videov_Monica_Philip_Blowjob2_2 = Movie(play="video/v_Monica_Philip_Blowjob2_2.mkv", fps=30)
    show videov_Monica_Philip_Blowjob2_2
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16400
    with diss
    w
    sound keyboard
    img 16401
    with fade
    w
    sound keyboard
    img 16402
    with diss
    w
    sound keyboard
    img 16403
    with diss
    w
    music2 Loved_Up2
    img 16404
    with fade
    philip "Еще глубже."
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
    scene black
    image videov_Monica_Philip_Blowjob2_3 = Movie(play="video/v_Monica_Philip_Blowjob2_3.mkv", fps=30)
    show videov_Monica_Philip_Blowjob2_3
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16405
    with diss
    w
    img 16406
    with fade
    w
    sound keyboard
    img 16407
    with diss
    w
    sound keyboard
    img 16408
    with diss
    w
    if game.extra == True:
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
        scene black
        image videov_Monica_Philip_Blowjob2_4 = Movie(play="video/v_Monica_Philip_Blowjob2_4.mkv", fps=30)
        show videov_Monica_Philip_Blowjob2_4
        with fade
        philip "Мммммм..."
        wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16409
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 16410
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    philip "Мммммм..."
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    # сперма стекает изо рта Моники
    img 16411
    with fadelong
    philip "Теперь проглоти это."
    m "..."
    menu:
        "Выплюнуть.":
            # Моника смотрит на него с отвращением
            music Pyro_Flow
            img 16412
            with fade
            mt "Я не смогу проглотить это!"
            mt "Меня стошнит."
            # выплевывает
            img 16413
            with diss
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
#            sound highheels_short_walk
#            img 16389
#            with fade
#            w
#            pass
        "Проглотить.":
            pass
            img 16414
            with fade
            sound snd_gulp
            w
    # Филипп достает из кармана купюру 100 долларов и кидает ее на диван
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16415
    with fade
    philip "Субботняя шлюха номер 2 может забрать свои деньги."
    philip "И уходить."
    # Моника забирает деньги
    img 16416
    with diss
    m "..."
    img 16419
    with fade
    menu:
        "Попросить еще денег.":
            img 16417
            with diss
            mt "Может, поросить у него еще денег?"
            mt "Ведь в прошлый раз он заплатил мне 300 долларов."
            img 16420
            with fade

            m "Филипп, я..."
            m "..."
            m "Хотела спросить, не мог бы ты дать мне еще немного денег?"
            # поворачивается к ней
            img 16421
            with diss
            philip "???"
            philip "Моей субботней шлюхе нужны деньги?"
            img 16422
            with diss
            philip "Я тебе их только что заплатил."
            philip "Хочешь еще денег - приходи через неделю."
            # отворачивается
            music Pyro_Flow
            img 16423
            with fade
            mt "Жадный неудачник!"
            return
        "Уйти.":
            pass
    music Pyro_Flow
    img 16417
    with diss
    mt "Сволочь!"
    mt "!!!"
    sound highheels_short_walk
    img 16418
    with fade
    # Моника уходит
    return

label gallery_16446:

    # Филипп садится на диван
    music Groove2_85
    img 16424
    with fadelong
    philip "Сейчас шлюха номер 2 предложит мне себя, как в прошлый раз."
    philip "А я пока подумаю, что я с ней сегодня сделаю."
    # выбор: уйти или предложить себя Филиппу
    music Pyro_Flow
    img 16386
    with fade
    mt "Моника, неужели ты способна на такое пойти?!"
    mt "..."
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16387
            with diss
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16425
            with fade
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            sound highheels_short_walk
            img 16418
            with diss
            return
        "Предложить себя Филиппу.":
            pass
    # Моника стоит перед ним в нерешительности
    music Groove2_85
    img 16426
    with diss
    m "..."
    m "Ч-что мне сделать?"
    img 16427
    with fade
    philip "Задирай платье и нагибайся, раздвинув ноги."
    # Моника поворачивается к нему задом и делает, как он сказал
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16428
    with fade
    w
    img 16429
    with diss
    philip "Что же шлюха может предложить мне сегодня?"
    philip "Возможно, свою задницу?"
    music Pyro_Flow
    img 16430
    with fade
    mt "О, нет! Он хочет сделать это с моей попой?!"
    mt "Нет! Я не перенесу этого!"
    mt "!!!"
    music Loved_Up
    img 16431
    with diss
    philip "Хммм... Нет, задницу я оставлю на потом..."
    philip "Я подожду, когда твои акции подешевеют..."
    philip "А сейчас... Может быть, ротик?"
    # Филипп расстегивает штаны, достает стояк, начинает подрачивать его
    img 16432
    with diss
    philip "Субботняя шлюха, повернись и покажи мне свою грудь, приспусти платье."
    # Моника поворачивается и приспускает платье, смотрит на него зло
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16433
    with fade
    philip "Хорошо. Мне нравится, что моя шлюха такая послушная."
    img 16434
    with diss
    mt "Сволочь!"
    mt "!!!"
    img 16435
    with fade
    philip "Кстати, я даже не предложил своей субботней шлюхе номер 2 присесть..."
    philip "Иди сюда. Присаживайся."
    # Моника смотрит на диван и делает шаг
    img 16436
    with diss
    philip "Нет, не на диван. Садись на мой член."
    img 16437
    with diss
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            music Pyro_Flow
            img 16438
            with fade
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16439
            with diss
            m "Нет. Я..."
            m "Я не буду этого делать!"
            img 16440
            with fade
            sound highheels_short_walk
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            return
        "Сесть на член Филиппа.":
            pass
    # Моника смотрит на его член
    music Groove2_85
    img 16441
    with fade
    mt "Ненавижу этого мерзавца!"
    mt "!!!"
    img 23177
    with fadelong
    w
    sound snd_fabric1
    img 23178
    with fadelong
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound chpok6
    pause 1.0
    music2 Loved_Up2
    # подходит к нему и нерешительно выполняет, сев к нему на колени, лицом к нему
    # тот, откинувшись на диван, самодовольно ухмыляется
    img 16442
    with fadelong
    philip "Давай, выполняй. Шлюха же хочет заработать денег?"
    # секс, Моника на его коленях, двигается вверх-вниз, он лапает ее за попу и за грудь
    img 16448
    with fade
    mt "Это так... Так неприятно..."
    mt "Скорее бы это закончилось."
    mt "Хочу забрать деньги и уйти отсюда."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_1 = Movie(play="video/v_Monica_Philip_Sex1_1.mkv", fps=30)
    show videov_Monica_Philip_Sex1_1
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16443
    with diss
    philip "Да..."
    img 16444
    with fade
    philip "Давай, быстрее..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_2 = Movie(play="video/v_Monica_Philip_Sex1_2.mkv", fps=30)
    show videov_Monica_Philip_Sex1_2
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_3 = Movie(play="video/v_Monica_Philip_Sex1_3.mkv", fps=30)
    show videov_Monica_Philip_Sex1_3
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16445
    with diss
    philip "Еще..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_4 = Movie(play="video/v_Monica_Philip_Sex1_4.mkv", fps=30)
    show videov_Monica_Philip_Sex1_4
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    # Моника смотрит на него с отвращением
    img 16446
    with diss
    w
    img 16447
    with diss
    m "..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_5 = Movie(play="video/v_Monica_Philip_Sex1_5.mkv", fps=30)
    show videov_Monica_Philip_Sex1_5
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16449
    with fade
    philip "Оооо... Даааа..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_7 = Movie(play="video/v_Monica_Philip_Sex1_7.mkv", fps=30)
    show videov_Monica_Philip_Sex1_7
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_6 = Movie(play="video/v_Monica_Philip_Sex1_6.mkv", fps=30)
    show videov_Monica_Philip_Sex1_6
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    # кончает ей на платье или на живот
    img 16450
    with diss
    philip "Мммммм..."
    w
    img 16451
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 16452
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    img 16453
    with diss
    w
    # Филипп одевается и бросает на диван купюру
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16415
    with fade
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 2 может забрать свои деньги."
    philip "И уходить."
    # Моника одевается и забирает деньги
    img 16416
    with diss
    m "..."
    menu:
        "Попросить еще денег.":
            img 16417
            with fade
            mt "Может, поросить у него еще денег?"
            mt "Ведь в прошлый раз он заплатил мне 300 долларов."
            img 16420
            with diss
            m "Филипп, я..."
            m "..."
            m "Хотела спросить, не мог бы ты дать мне еще немного денег?"
            # смотрит на нее
            img 16421
            with fade
            philip "???"
            philip "Моей субботней шлюхе нужны деньги?"
            img 16422
            with diss
            philip "Я тебе их только что заплатил."
            philip "Хочешь еще денег - приходи через неделю."
            # отворачивается
            music Pyro_Flow
            img 16423
            with fade
            sound highheels_short_walk
            mt "Жадный неудачник!"

            return
        "Уйти.":
            pass
    music Pyro_Flow
    img 16418
    with fade
    sound highheels_short_walk
    mt "Сволочь!"
    mt "!!!"
    # Моника уходит
    return

label gallery_16455:

    # Моника заходит в дом Филиппа, стоит рядом с входной дверью в гостиной
    # Филипп на диване или стоит посередине гостиной

    music Groove2_85
    img 16373
    with fadelong
    philip "..."
    m "Филипп, я пришла..."
    m "..."
    sound highheels_short_walk
    img 16374
    with fade
    w
    img 16375
    with diss
    philip "Скажи, кто ты?"
    philip "Кто ко мне пришел?"
    img 16376
    with diss
    m "???"

    music Pyro_Flow
    img 16377
    with fade
    mt "Черт!"
    mt "Я не хочу это говорить!"
    mt "Но если я не скажу это..."
    img 16378
    with diss
    mt "Он выгонит меня и я не смогу заработать денег."
    mt "..."
    music Groove2_85
    img 16379
    with fade
    m "Я субботняя... Субботняя ш-шлюха..."
    philip "У меня уже есть одна субботняя шлюха. А ты кто?"
    img 16380
    with diss
    m "Субботняя шлюха номер 2."



    # если Филипп в этот день с шлюхой номер 1
    # к нему подходит другая девушка с отеля и он ее обнимает
    # шлюха номер 1 на Монику смотрит пренебрежительно
    sound plastinka1b
    music Loved_Up
    img 16381
    with fade
    philip "У меня сегодня субботняя шлюха номер 1."
    img 16454
    with diss
    philip "Субботняя шлюха номер 2 может прийти через неделю."
    img 16455
    with fade
    w
    # Моника оказывается на улице

    return

label gallery_16068:

    return
