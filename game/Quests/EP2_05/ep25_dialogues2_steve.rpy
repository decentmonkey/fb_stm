# Если Моника заработала $5000 на этой неделе, то Стива в офисе нет!
# Также, если Моника заработала деньги у Стива, то фотосессии заблокированы на эту неделю!


label ep25_dialogues2_steve1:
# Моника заходит в офис Стива.
# Там она встречает Джейн.
# Стива нет. Моника наезжает на Джейн.
    music m80s_Things
    img 11294
    with fadelong
    jane "Миссис Бакфетт!"
    m "Это ты, Джейн?!"
    img 11295
    with diss
    if janeTiffanyFirePlanned == True:
        $ notif(t_("Моника планировала уволить Джейн"))
        m "Стив еще не уволил тебя?!"
        m "Он обещал мне сделать это!"
    else:
        m "Удивлена что ты все еще работаешь здесь!"

    img 11296
    with fade
    jane "..."
    music Pyro_Flow
    img 11297
    with diss
    m "В чем это ты одета?"
    img 11298
    m "Ты не сделала выводов, детка?!"
    m "Ты считаешь эту респектабельную компанию прибежищем для шлюх?!"
    img 11299
    with fade
    jane "Миссис Бакфетт, Я..."
    m "Молчать!"
    m "Где Стив?!"
    jane "Миссис Бакфетт, Мистера Стива сейчас нет на месте..."
    img 11300
    with fade
    if steveOffended1 == True:
        $ notif(t_("Моника называет Стива мешком с дерьмом"))
        m "Когда будет на месте этот мешок с дерьмом?!"
    else:
        m "Когда этот бездельник будет на месте?!"
    img 11301
    with diss
    jane "Мистер Стив сказал что он будет только завтра..."
    jane "Хотите я ему позвоню?"
    img 11302
    with diss
    m "Не надо звонить ему."
    m "Тогда этот слизняк точно ускользнет от меня."
    m "Не говори ему что я приходила, понятно тебе?!"
    img 11303
    with fade
    jane "Да, Миссис Бакфетт, я не скажу Мистеру Стиву что Вы приходили."
    return

label ep25_dialogues2_steve1a:
    # Моника обращается повторно
    img 11304
    with fadelong
    jane "Миссис Бакфетт, Мистера Стива сейчас нет на месте..."
    music Pyro_Flow
    img 11305
    with diss
    m "Я знаю это. Без таких шлюх как ты, Джейн!"
    img 11306
    with fade
    jane "Миссис Бакфетт!"
    img 11307
    with diss
    m "Посмотри на свой внешний вид, Джейн!"
    return

label ep25_dialogues2_steve1b:
    # Моника пытается зайти в офис Стива в плохой одежде
    mt "Я не могу идти туда в таком виде."
    mt "Вообще-то я Леди!"
    mt "И Босс!"
    mt "И мне надо выглядеть подобающе."
    return


label ep25_dialogues2_steve2:
# Второй приход к Стиву. Моника встречает Джейн, а также Тиффани.
# Стива все нет. Моника наезжает на них обеих.
    img 11308
    with fadelong
    jane "Миссис Бакфетт!"
    music Pyro_Flow
    img 11309
    with fade
    m "Встать, когда с тобой говорит твой Босс!"
    img 11310
    with fade
    # Джейн встает
    jane "..."
    img 11311
    with diss
    m "Ты снова одета в это, Джейн?!"
    m "Ты решила поиграть с огнем, да?!"
    img 11312
    with fade
    jane "Миссис Бакфетт, Мистер Стив приказал мне носить это..."
    img 11313
    with diss
    m "Стив?!"
    img 11314
    with diss
    m "Кто твой Босс, Джейн?!"
    m "Стив или Я?!"
    img 11315
    with fade
    jane "..."
    img 11316
    with diss
    m "Отвечай, быстро!"
    img 11317
    with fade
    jane "Вы, Миссис Бакфетт..."
    music Groove2_85
    img 11318
    with fade
    m "Хорошо, можешь продолжать ходить в этом..."
    m "Это будет отличный повод уволить тебя!"
    img 11319
    jane "..."

    music stop
    img black_screen
    with diss
    pause 2.0
    music Indo_Rock2
    img 11321
    with fadelong
    # Заходит Тиффани
    tiffany "Джейн!"
    img 11320
    with diss
    tiffany "Я нашла то свадебное платье, которое ты хочешь!"
    img 11322
    with diss
    tiffany "Поехали скорее в тот магазин!"
    img 11323
    with diss
    jane "!!!"
    img 11324
    with diss
    tiffany "???"
    music stop
    sound plastinka2
    img 11325
    with diss
    w
    music Pyro_Flow
    img 11326
    with fadelong
    m "..."
    img 11327
    with diss
    tiffany "Ой!"
    img 11328
    with fade
    tiffany "Миссис Бакфетт..."
    tiffany "Здравствуйте..."
    img 11329
    with diss
    m "Знакомое личико..."
    if monicaBitch == True:
        $ notif_monica()
        m "Напомни-ка, сучка, как тебя зовут?!"
    else:
        m "Напомни-ка, девочка, как тебя зовут?!"
    img 11330
    with fade
    tiffany "Меня зовут Тиффани, Мэм..."
    if janeTiffanyFirePlanned == True:
        $ notif(t_("Моника планировала уволить Тиффани"))
        img 11331
        with diss
        m "Насколько я помню, тебя я тоже собиралась уволить!"
        img 11332
        with diss
        m "Посмотри на свой внешний вид!"
        img 11333
        with fade
        m "Ты недалеко ушла от этой проститутки, Джейн!"
        img 11334
        with diss
        tiffany "!!!"
        img 11335
        with diss
        jane "!!!"
    else:
        img 11331
        with diss
        m "Удивительно как тебя еще не уволили!"
        img 11332
        with diss
        m "Посмотри на свой внешний вид!"
        img 11333
        with fade
        m "Вы тут все одеты как проститутки!"
        img 11334
        with diss
        tiffany "!!!"
        img 11335
        with diss
        jane "!!!"

    music Pyro_Flow
    img 11336
    with fadelong
    m "Я разберусь и с тобой тоже!"
    img 11337
    with diss
    m "Где Стив?! Он в своем кабинете?"
    img 11338
    with diss
    jane "Миссис Бакфетт, Мистера Стива сегодня снова нет..."
    img 11339
    with fade
    m "Этот слизняк что, скрывается от меня?!"
    m "Может быть это ты предупредила его, Джейн?!"
    img 11340
    with diss
    jane "Нет, Миссис Бакфетт."
    jane "Я ничего ему не говорила, как Вы и приказали..."
    img 11341
    with fade
    m "Может быть это ты ему сообщила, Тиффани?!"
    img 11342
    with diss
    tiffany "Нет, Мэм. У меня нет личного номера Мистера Стива..."
    img 11343
    with fade
    m "Пойду-ка я проверю, вдруг Вы меня обманываете!"
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    img 11344
    with diss
    jane "Миссис Бакфетт, но в кабинет Мистера Стива запрещено заходить в его отсутствие!"
    img 11345
    with fade
    m "Джейн, ты забыла?!"
    m "Кто здесь Босс?!"
    m "Стив или Я?"
    # Джейн смотрит на Тиффани
    img 11346
    with diss
    jane "..."
    img 11347
    with diss
    w
    img 11348
    with fade
    jane "Вы, Миссис Бакфетт..."
    img 11349
    with fade
    m "А ты, Тиффани?!"
    m "Ты в курсе кто здес Босс?"
    img 11350
    with diss
    jane "Миссис Бакфетт, здесь Босс Вы..."
    img 11351
    with diss
    m "Правильный ответ."
    m "А теперь, проводите меня в кабинет!"
    # Заходят в кабинет
    # Там Стива нет

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 3.0
    music Groove2_85
    #идут
    img 11352
    with fadelong
    w
    img 11353
    with diss
    m "Этого слизняка здесь нет..."
    img 11354
    with diss
    m "Надо проверить под столом, вдруг он прячется там..."
    # Смотрит под стол, там никого нет
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11355
    with fadelong
    w
    img 11356
    with diss
    w
    img 11357
    with diss
    mt "Никого нет..."

    # Моника садится на стул Стива
    music stop
    img black_screen
    pause 1.0
    pause 2.0
    music Stealth_Groover
    img 11358
    with fadelong
    m "Итак, девочки..."
    m "Когда будет Стив?"
    img 11359
    with diss
    jane "Миссис Бакфетт..."
    jane "Мистер Стив должен быть завтра..."
    img 11360
    with fade
    m "Может быть мне подождать его здесь?"
    img 11361
    with diss
    m "Вдруг он появится... СЕГОДНЯ..."
    img 11362
    with fade
    jane "..."
    img 11363
    with diss
    m "А, Тиффани?"
    img 11364
    with fade
    tiffany "Миссис Бакфетт."
    tiffany "Мистер Стив вряд-ли появится сегодня..."
    img black_screen
    with diss
    pause 1.0
    img 11365
    with fadelong
    w
    img 11366
    with diss
    w
    sound highheels_short_walk
    img 11367
    with diss
    w
    # Моника уходит
    img 11368
    with diss
    m "Хорошо"
    img 11369
    with diss
    m "Я приду завтра."
    img 11370
    with fade
    w
    # повтор ep25_dialogues2_steve1a
    return

label ep25_dialogues2_steve2a:
    mt "Этот слизняк что, пытается избегать меня?!"
    mt "Мне надо придти завтра, я должна поймать этого Стива!"
    return

label ep25_dialogues2_steve3:
# Третий приход к Стиву. Джейн пытается сказать что Стива нет, но Моника злая.
# Заходит к Стиву в кабинет.
# Джейн бежит следом. Моника выглядит круто. Стив в шоке.
# Стив думает, что Моника вернула все назад, судя по ее виду и поведению.
# Моника говорит Стиву чтобы встал с ее стула.
#Моника злая, потому что он не перевел деньги Виктории. Либо злая просто так, если не было секса.
# Злая из-за того что Стив посмел предложить ей секс.
# Стив боится Монику
    img 11371
    with fadelong
    jane "Миссис Бакфетт!"
    music Pyro_Flow
    img 11372
    with fade
    m "Джейн?!"
    m "Где Стив?"
    jane "Миссис Бакфетт, Мистер Стив в своем кабинете."
    jane "Он просил его не беспокоить и..."
    # Моника идет в кабинет
    img 11373
    with fade
    m "Меня не волнуют его просьбы!"

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Pyro_Flow
    img 11374
    with fadelong
    jane "Мистер Стив!"
    img 11375
    with diss
    jane "К Вам пришла Миссис Бакфетт!"

    img 11376
    with fadelong
    steve "Моника?"
    img 11377
    with fade
    m "Стив! Встань с моего кресла!"
    img 11378
    with diss
    m "Быстро!"
    # Оглядывает Монику
    img 11379
    with fade
    w
    img 11380
    with diss
    w
    img 11381
    with diss
    w
    img 11382
    with diss
    steve "..."
    img 11383
    with diss
    m "Я сказала БЫСТРО!"
    # Стив встает
    img 11384
    with fade
    w

    menu:
        "Итак, Стив! Ответь мне!" if monicaHasSexWithSteveBasement == True:
            pass
        "Итак, Стив! Ответь мне! (не было сделки со Стивом) (disabled)" if monicaHasSexWithSteveBasement == False:
            pass
        "Ты собираешься переводить мне деньги, Стив?" if monicaHasSexWithSteveBasement == False:
            pass
        "Ты собираешься переводить мне деньги, Стив? (была сделка со Стивом) (disabled)" if monicaHasSexWithSteveBasement == True:
            pass
    # переход на ep25_dialogues2_steve4, либо на ep25_dialogues2_steve10
    return

label ep25_dialogues2_steve4:
# Если был секс:
# Моника спрашивает у Стива почему он не перевел деньги.
# Стив оправдывается. При этом задает вопрос почему какие-то $5000 имеют значение для Моники.
# Моника злится и говорит что она бизнес леди и все деньги имеют значение.
# Стив сомневается. Моника, скажи, ты вернула все назад? Эта компания снова принадлежит тебе?
# Моника мнется и говорит что Стив прекрасно знает что компания принадлежит ей!
# Стив просит Монику доказать это.
    img 11385
    with fadelong
    w
    img 11386
    with fade
    m "Джейн!"
    m "Вон отсюда!"
    img 11387
    with diss
    w
    img 11388
    with diss
    jane "..."
    steve "..."
    sound highheels_short_walk
    img 11389
    with fadelong
    w
    # джейн уходит
    img black_screen
    with diss
    pause 2.0
    return

label ep25_dialogues2_steve4a:
    img black_screen
    with diss
    pause 2.0
    img 11390
    music Groove2_85
    with fadelong
    m "Итак, Стив!"
    m "Ответь мне!"
    img 11391
    with diss
    m "Почему ты не перевел деньги на тот адрес?"
    img 11392
    with fade
    steve "Моника... Я..."
    steve "Я собирался это сделать..."
    img 11393
    with diss
    m "!!!"
    music stop
    sound plastinka2
    img 11394
    with diss
    steve "..."
    music Groove2_85
    img 11395
    with fadelong
    steve "Моника, погоди. Ты ведь теперь снова Босс?"
    steve "Но какое тогда значение имеют эти $ 5000 для тебя?"
    img 11396
    with diss
    m "Я - Бизнес Леди!"
    m "Для меня все деньги имеют значение!"
    img 11397
    with fade
    steve "Моника, скажи, так ты вернула все назад?"
    steve "Эта компания снова принадлежит тебе?"
    img 11398
    with diss
    m "..."
    img 11399
    with diss
    steve "..."
    img 11400
    with fade
    m "Ты прекрасно знаешь что эта компания принадлежит мне!"
    img 11401
    with diss
    steve "..."
    img 11402
    with fade
    steve "Моника, а ты можешь это доказать?"
# Моника говорит что не собирается ничего доказывать Стиву!
# И чтобы он перевел деньги немедленно!
# Стив говорит что Моника ввела его в заблуждение своим внешним видом.
# Что он действительно подумал что Моника снова Босс и она его этим напугала.
# Моника отвечает что скоро она будет Боссом и Стиву стоит бояться ее, потому что она сотрет его в порошок!
# Стив оправдывается что он всего-лишь бизнесмен.
# Моника говорит чтобы он перевел деньги немедленно.
# Стив говорит что не может сделать этого, потому что сделка не была закрыта.
# Моника спрашивает какого черта?! Стив получил что хотел и сделка закрыта.
# Стив говорит что нет.
    music Power_Bots_Loop
    img 11403
    with fade
    m "Я не собираюсь тебе ничего доказывать, жалкий слизняк!"
    m "Переводи деньги, немедленно!"
    music Groove2_85
    img 11404
    with fade
    steve "Моника, ты ввела меня в заблуждение."
    steve "Я действительно подумал что ты теперь снова мой Босс."
    img 11405
    with diss
    steve "Ты очень напугала меня!"
    music Power_Bots_Loop
    img 11406
    with fade
    m "Очень скоро я снова стану твоим Боссом!"
    m "И тебе стоит бояться меня, потому что я сотру тебя в порошок!"
    m "За то что ты сделал!"
    music Groove2_85
    img 11407
    with fade
    steve "За то что я не перевел деньги?"
    steve "Или за то что я взял в аренду твою..."
    music Power_Bots_Loop
    img 11408
    with diss
    m "Молчать! Ты прекрасно сам все понимаешь!"
    music Groove2_85
    img 11409
    with fade
    steve "Но Моника, я всего-лишь бизнесмен!"
    img 11410
    with diss
    m "Переведи деньги немедленно!"
    img 11411
    with fade
    steve "Моника, но я не могу сделать это, потому что сделка не была закрыта."
    img 11412
    with diss
    m "Какого черта, Стив?"
    m "Ты получил что хотел и сделка закрыта!"
    img 11413
    with diss
    steve "Нет, Моника, она не закрыта..."
# Моника спрашивает почему это?
# Стив отвечает что потому что доступ к объекту был прекращен раньше завершения срока аренды.
# Моника бесится: аренда была предоставлена в полной мере, сделка закрыта.
# Нет
# Почему?!
# Потому что Стив не кончил в объект аренды.
# Моника бесится: это невозможно! я не собираюсь иметь детей от такого мешка с дерьмом как ты!
# Стив говорит что у объекта аренды есть еще один вход, вполне безопасный для того чтобы туда кончить.
# Моника спрашивает у Стива что он имеет ввиду.
    img 11414
    with fade
    m "Почему это, Стив?!"
    img 11415
    with diss
    steve "Потому что доступ к объекту был прекращен раньше завершения срока аренды."
    img 11416
    with fade
    m "Аренда была предоставлена в полной мере, сделка закрыта!"
    steve "Нет!"
    img 11417
    with diss
    m "Почему?!"
    img 11418
    with fade
    steve "Потому что арендатор не смог кончить в объект аренды."
    img 11419
    with diss
    m "Это невозможно!"
    m "У владельца объекта аренды нет никакого желания иметь детей от такого мешка с дерьмом как ты!"
    img 11420
    with fade
    steve "У объекта аренды есть еще один вход, вполне безопасный для того, чтобы туда кончить."
    m "Что ты имеешь ввиду?"

# Стив молча улыбается.
# Моника догадывается: Ах ты про это?! Негодяй!
# Это невозможно!
# У Моники такого никогда не было и, она клянется, не будет никогда!
# Стив улыбается.
# Говорит что есть еще один вариант.
    img 11421
    with diss
    steve "..."
    music Power_Bots_Loop
    img 11422
    with fade
    m "Ах ты про это?! Негодяй!"
    m "Это невозможно!"
    m "У меня никогда такого не было и, я клянусь, не будет никогда!"
    music Groove2_85
    img 11423
    with fade
    steve "..."
    img 11424
    with diss
    steve "Есть еще один вариант..."
    $ questHelp("steve_9a", False)
# Моника делает выбор:
    menu:
        "Мне не нужны никакие варианты, мерзавец!":
# Мне не нужны никакие варианты, мерзавец. Если он не заплатит то Моника прибъет его прямо здесь!
# Стив платит
            music Power_Bots_Loop
            img 11425
            with fade
            w
            img 11426
            with diss
            m "Мне не нужны никакие варианты, мерзавец!"
            img 11427
            with diss
            m "Если ты не заплатишь, то я прибью тебя прямо здесь!"
            img 11428
            with fade
            steve "Хорошо, Моника!"
            steve "Я сейчас переведу деньги!"
            steve "Не надо меня прибивать!"
            return False
        "Какой вариант?":
            pass
# Либо спрашивает. Хорошо, Стив, ты мерзавец и я покончу с тобой, но мне сейчас нужен этот платеж. Какие варианты еще есть?
# Стив достает член и говорит что у объекта недвижимости есть еще один безопасный способ принять его сперму.
# Моника спрашивает что еще этот извращенец Стив имеет ввиду? Какой еще способ?
# Стив отвечает что это ротик Моники. Что она все-равно не закрывает его, так что если она подержит его открытым еще немного,
# то сможет быстро закрыть эту сделку.
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11429
    with fadelong
    m "Хорошо, Стив..."
    m "Ты мерзавец и я покончу с тобой."
    img 11430
    with diss
    m "Но мне сейчас нужен этот платеж."
    m "Какой вариант еще есть?"

    # Стив достает член
    #zip
    img black_screen
    with diss
    sound snd_zip
    pause 2.0
    sound Jump1
    img 11431
    with fadelong
    w
    img 11432
    with fade
    steve "У объекта аренды есть еще один безопасный способ принять сперму."
    music Power_Bots_Loop
    img 11433
    with fade
    m "Стив, извращенец! Что ты имеешь ввиду?"
    m "Какой еще способ?"
    music Groove2_85
    img 11434
    with diss
    steve "Это ротик объекта аренды."
    steve "Объект аренды все-равно не закрывает его."
    steve "Так что, если ротик побудет открытым еще немного, то сможет быстро закрыть эту сделку."

# Член около лица Моники.
# Моника отвечает со злобой что сделка касалась только ее....
# Стив говорит: Да, Моника, скажи это, произнеси это слово.
# Моника отвечает что не собирается произносить и что то что хочет Стив будет ему стоить в два раза дороже!
# Стив отвечает что у него сверху есть только $100.
# Моника говорит что Стив что, издевается над ней?
# Стив отвечает что нет, она ведь в курсе насчет его и Джейн.
# Что Моника и так оставит Стива без денег на ланч на целую неделю.
# Пусть Моника скорее откроет ротик, Стив уже изнемогает.
    img 11435
    with diss
    m "!!!"
    m "Сделка касалась только моей..."
    m "Моей..."
    img 11436
    with diss
    steve "Да, Моника! Скажи это!"
    steve "Произнеси это слово!"
    img 11439
    with diss
    m "Нет!"
    img 11437
    with diss
    m "Я не собираюсь ничего произносить, Стив!"
    img 11438
    m "И то что ты хочешь, будет стоить тебе в два раза дороже!"
    img 11440
    with diss
    steve "Моника, у меня сверху есть только $ 100."
    img 11441
    with fade
    w
    img 11442
    with fade
    w
    img 11443
    with diss
    m "Стив, ты что, издеваешься надо мной?!"
    img 11444
    with diss
    steve "Нет, Моника, я не издеваюсь над тобой."
    img 11445
    with diss
    steve "Ты ведь в курсе насчет меня и Джейн..."
    img 11446
    with fade
    steve "Ты и так оставишь меня без денег на ланч на целую неделю!"
    img 11447
    with fade
    steve "Открой скорее свой ротик, я уже изнемогаю!"
    img 11448
    with diss
# Моника делает выбор:
    menu:
        "Я не собираюсь заключать никаких новых сделок.":

# Я не собираюсь заключать никаких новых сделок.
# Если ты не заплатишь сейчас-же, то я убью тебя прямо здесь!
# Стив платит
            music Power_Bots_Loop
            img 11449
            with fadelong
            m "Я не собираюсь заключать никаких новых сделок."
            m "Если ты не заплатишь сейчас-же, то я убью тебя прямо здесь!"
            img 11450
            with diss
            steve "Хорошо, Моника!"
            steve "Я сейчас переведу деньги!"
            steve "Не надо меня убивать!"
            return False
        "Открыть свой ротик.":
            pass

# Либо Моника молчит и зло смотрит на Стива
# Стив говорит что ну-же! Моника!
# Сделай это и через пять минут деньги будут переведены!
# Моника думает.
# Стив смотрит.
# Моника, давай быстрее! Джейн может войти в любой момент!
# Моника молча открывает рот и зло смотрит.
# Стив вгоняет в нее член с криком О ДА!!!
# Как же я мечтал об этом дне!
# Когда я вгоню свой член в твой ротик!
# Каждый раз когда ты приходила и кричала на меня, я мечтал об этом дне!
# Моника зло смотрит.
# Стив кончает.
    m "..."
    img 11451
    with fade
    steve "Ну же, Моника!"
    img 11452
    with diss
    steve "Сделай это и через пять минут деньги будут переведены!"
    img 11453
    with diss
    m "..."
    img 11454
    with diss
    steve "..."
    sound hlup10
    img 11455
    with diss
    steve "Моника, давай быстрее!"
    img 11456
    with fade
    steve "Джейн может войти в любой момент!"
    img 11457
    w
    m "..."

    music stop
    img 11458
    with diss
    steve "Ну же!"
    sound hlup10
    img 11459
    with diss
    steve "О ДА!!!"
    music Loved_Up2
    steve "Как же я мечтал об этом дне!"
    steve "О дне, когда я вгоню свой член в твой ротик!"
    img 11460
    with diss
    steve "Каждый раз, когда ты приходила и кричала на меня, я мечтал об этом дне!"
    img 11461
    with diss
    m "!!!"


    # video
    music stop
    music2 Loved_Up2
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_1 = Movie(play="video/v_Steve_Monica_Blowjob_1_1.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_2 = Movie(play="video/v_Steve_Monica_Blowjob_1_2.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_2
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_3 = Movie(play="video/v_Steve_Monica_Blowjob_1_3.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_4 = Movie(play="video/v_Steve_Monica_Blowjob_1_4.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_4
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_5 = Movie(play="video/v_Steve_Monica_Blowjob_1_5.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_5
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_6 = Movie(play="video/v_Steve_Monica_Blowjob_1_6.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_6
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_7 = Movie(play="video/v_Steve_Monica_Blowjob_1_7.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_8 = Movie(play="video/v_Steve_Monica_Blowjob_1_8.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_8
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_9 = Movie(play="video/v_Steve_Monica_Blowjob_1_9.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_9
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_10 = Movie(play="video/v_Steve_Monica_Blowjob_1_10.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_10
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_11 = Movie(play="video/v_Steve_Monica_Blowjob_1_11.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_11
    with fadelong
    wclean
    $ renpy.music.set_volume(1.0, 0.0, 'music2')

    stop music
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.0
    img 11462
    with fadelong
    sound bulk1
    steve "АААААХХХХХХХ!!!"
    m "!!!"
    music Groove2_85
    img 11463
    with fadelong
    m "Тьфу!"
    mt "Мерзость!"

# Моника уходит вытирая рот: только попробуй не перевести деньги, мерзавец!
    $ add_corruption(monicaSteveFirstBlowjobDeal, "monicaSteveFirstBlowjobDeal")
    music Power_Bots_Loop
    img 11464
    with fadelong
    m "Только попробуй не перевести деньги, мерзавец!"
    $ monicaMadeBlowjobForSteveChair = True
    return

label ep25_dialogues2_steve5:
# На улице Моника делает комментарий по поводу того что надо бы проверить перевел-ли деньги Стив.
# Это самоубийство для него если он этого не сделал, но от такого мешка с дерьмом можно ожидать любую глупость!
    mt "Мерзкий Стив!"
    mt "Мне пришлось пойти на очередной унижение, чтобы добиться от него моих денег!"
    mt "..."
    mt "Надо бы проверить, перевел-ли Стив деньги?"
    mt "Это самоубийство для него, если он этого не сделал."
    if steveOffended1 == True:
        mt "Но от такого мешка с дерьмом можно ожидать любую глупость!"
    else:
        mt "Но от него можно ожидать любую глупость!"
    return

label ep25_dialogues2_steve5a:
    # Моника пытается зайти в офис к Стиву до того как проверен перевод денег Виктории
    mt "Мне надо проверить, перевел-ли Стив деньги!"
    mt "Надо сходить к Виктории!"
    return False

label ep25_dialogues2_steve6:
    # Моника проверят деньги у Виктории
    music Hidden_Agenda
    img 10134
    with fadelong
    m "Мисс Виктория..."
    m "Скажите... Вам приходил на почту подарочный сертификат?"
    music Groove2_85
    img 10135
    with diss
    dick_secretary "Нет, не приходил..."
    dick_secretary "Но я его жду, как обычно..."
    img 10136
    with fade
    m "Да, Мисс Виктория... Он будет, не волнуйтесь..."
    img 7965
    with diss
    dick_secretary "Я не волнуюсь, подружка!"

    music Power_Bots_Loop
    img 10137
    with fadelong
    mt "ЭТОТ СТИВ СНОВА МЕНЯ ОБМАНУЛ!!!"
    mt "ОН ЧТО, ДУМАЕТ ЧТО БЕСПЛАТНО ТРАХНУЛ МЕНЯ И ЗАСУНУЛ СВОЙ ЧЛЕН МНЕ В РОТ?!?!"
    mt "Я УБЬЮ ЭТУ СВОЛОЧЬ!!!"
    return

label ep25_dialogues2_steve7:
# Стив деньги не перевел.
    # В тот же день Стива нет
    music Power_Bots_Loop
    img 11465
    with fadelong
    m "ГДЕ СТИВ?!!"
    img 11466
    with diss
    jane "Миссис Бакфетт, Стив уехал, он будет только завтра!"
    img 11467
    with fade
    m "НЕ СМЕЙ ГОВОРИТЬ ЧТО Я ПРИХОДИЛА!"
    m "Я ПОЙМАЮ ЭТОГО МЕРЗАВЦА!"
    jane "Да... Миссис Бакфетт..."
    return

label ep25_dialogues2_steve8:
# Стив деньги не перевел.
# Моника врывается к нему злая, сметая Джейн.
# Подходит к Стиву и берет его за горло.
# Стив, ты решил свести счеты с жизнью? Ты решил обмануть меня второй раз?
# Стив говорит что не собирается обманывать Монику.
# Просто сделка не была закрыта!
# Как не была закрыта?!
# Ты воспользовался моей наивностью и глупостью целых два раза!
    music Power_Bots_Loop
    img 11468
    with fadelong
    m "ГДЕ СТИВ?!!"

    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    # заходит к Стиву
    img 11469
    with fadelong
    m "Стив!"
    img 11470
    with diss
    m "Ты решил свести счеты с жизнью?!"
    m "Ты решил обмануть меня второй раз?"
    img 11471
    with diss
    steve "Моника, я не собирался обманывать тебя!"
    steve "Просто сделка не была закрыта!"
    img 11472
    with fade
    m "Как это сделка не была закрыта?!"
    m "Ты воспользовался моей наивностью и глупостью целых два раза!"

# Стив говорит что он так и не кончил в объект аренды.
# Моника говорит что он добился в прошлый раз чего хотел и сделка закрыта!
# Стив отвечает он кончил в другой объект аренды. А для этого есть другая сделка.
# На $100. И она закрыта. Стив может дать эти деньги прямо сейчас. Такая сумма есть у него наличными.
# Моника бесится!
    music Groove2_85
    img 11473
    with fade
    steve "Но Моника!"
    steve "Я так и не кончил в объект аренды."
    img 11474
    with diss
    m "Ды добился чего хотел и сделка закрыта!"
    img 11475
    with fade
    steve "Моника, но я кончил в другой объект аренды."
    steve "И для этого была другая сделка."
    steve "Сделка на $ 100."
    img 11476
    with diss
    steve "И эта сделка закрыта."
    steve "Я могу дать тебе эти деньги прямо сейчас."
    steve "Такая сумма у меня есть наличными."
    img 11477
    with fade
    music Power_Bots_Loop
    menu:
        "Взять $ 100 и уйти.":
            img 11478
            with fadelong
            m "Давай сюда мои $ 100!"
            $ add_money(100.0)
            w

# Выбор:
# Взять $100 и уйти
# Давай сюда мои $100!
# Стив дает $100
# Также говорит напоследок, что если вдруг Моника захочет заключить еще сделку, то пусть приходит.
# Стив добропорядочный бизнесмен и всегда рад хорошей сделке!
# Моника бесится
            sound highheels_short_walk
            img 11479
            with fade
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            $ questHelp("steve_9e", True)
            $ questHelp("steve_10")
            $ questHelp("steve_17")
            $ questHelp("steve_9b", False)
            $ monicaSteveCumDealRejected = True
            $ monicaSteveCumDealActive = False
            return False
        "Как нам закрыть эту чертову сделку?!":
# Либо: Как нам закрыть эту чертову сделку?!
# Стив отвечает: нам надо сделать так, чтобы я кончил в объект аренды.
# Моника отвечает что не собирается соглашаться на это!
# Стив говорит что может подождать пока Моника подумает.
# Говорит что Моника может закрыть эту сделку в любой момент.
# Моника уходит.
# Также говорит напоследок, что если вдруг Моника захочет заключить еще сделку, то пусть приходит.
# Стив добропорядочный бизнесмен и всегда рад хорошей сделке!
            music Power_Bots_Loop
            img 11480
            with fadelong
            m "Как нам закрыть эту чертову сделку?!"
            img 11481
            with diss
            steve "Нам надо сделать так, чтобы арендатор кончил в объект аренды."
            img 11482
            with diss
            m "Я не собираюсь соглашаться на это!"
            img 11483
            with fade
            steve "Я могу подождать пока владелец объекта аренды подумает."
            steve "Владелец объекта аренды может закрыть эту сделку в любой момент."
            img 11484
            with diss
            m "!!!"
            sound highheels_short_walk
            img 11485
            with fadelong
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            $ questHelp("steve_9b")
            $ questHelp("steve_9e", True)
            return True
    return


label ep25_dialogues2_steve9:
# Моника думает на улице какой козел Стив. И что чтобы закрыть эту сделку, ей придется дать Стиву трахнуть ее снова.
# И это уже будет третий раз. Или второй? Считается-ли прошлы раз за раз или только за половину?
# Выходит он трахнет меня 2.5 раза?
# Дьявол, Моника! Какие, к черту, дроби?!
# Ты рассуждаешь о своем теле и своей чести, не забывай это!
    mt "Стив!"
    mt "Это редкий козел и мерзавец!"
    mt "Чтобы закрыть эту сделку, мне придется дать Стиву трахнуть меня снова!"
    mt "И это будет уже третий раз..."
    mt "Или второй?"
    mt "Считается-ли прошлый раз за раз или только за половину?"
    mt "Выходит, он трахнет меня 2.5 раза?"
    mt "Дьявол, Моника! Какие к черту дроби?!"
    mt "Ты рассуждаешь о своем теле и о своей чести, не забывай это!"
    return

label ep25_dialogues2_steve10:
    # приход из ep25_dialogues2_steve3

# Первый приход к Стиву. Секса не было:
# Моника говорит когда Стив пошлет деньги?
# Стив говорит что какие деньги?! Они не заключили никакой сделки!
# Выбор:
    img 11385
    with fadelong
    w
    img 11386
    with fade
    m "Джейн!"
    m "Вон отсюда!"
    img 11387
    with diss
    w
    img 11388
    with diss
    jane "..."
    steve "..."
    sound highheels_short_walk
    img 11389
    with fadelong
    w
    # джейн уходит

    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11390
    with fadelong
    m "Стив, когда ты перешлешь деньги?"
    img 11486
    with diss
    steve "Какие деньги, Моника?"
    steve "Ведь мы не заключили никакой сделки!"
    menu:
        "Мне не нужны никакие сделки, Стив!":
# Мне не нужны никакие сделки, Стив!
# Моника уходит. Стив говорит вслед что пусть приходит если захочет.
            music Power_Bots_Loop
            img 11487
            with fadelong
            m "Мне не нужны никакие сделки, Стив!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            $ questHelp("steve_10", False)
            $ questHelp("steve_17", False)
            $ questHelp("steve_9a", False)
            return False
        "Заключить сделку.":
            pass
# Заключить сделку.
# Хорошо, Стив. Давай заключим сделку.
# Ты хочешь что-то взять в аренду у меня, мерзавец?!
# Стив достает член.
# Да, Моника, я хочу взять в аренду твой ротик.
# Ты мерзавец, Стив!
# Но возможно я соглашусь, если ты заплатишь 1млн$
# Далее диалог о том что у Стива мало денег и торговля за цену.
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 11393
    with fade
    m "Хорошо, Стив."
    m "Давай заключим сделку."
    m "Ты хочешь что-то взять в аренду у меня, мерзавец?!"
# Стив достает член.
    img 11405
    with fade
    steve "Да, Моника, я хочу взять в аренду твой ротик."
    img 11416
    with diss
    m "Ты мерзавец, Стив!"
    m "Но, возможно, я соглашусь, если ты заплатишь 1 млн $"
    img 11413
    with fade
    steve "Моника, о чем ты говоришь?!"
    steve "У меня сейчас нет таких средств."

    img 11396
    with diss
    m "Я прекрасно знаю об оборотах твоей компании, Стив!"

    img 11411
    with fade
    steve "Да, но с тех пор как твою компанию возглавили другие люди, у меня начались сплошные проверки!"
    steve "Я не могу потратить ни цента, если они пойдут не на благо компании!"
    steve "Ты ведь не предлагаешь мне официально провести нашу сделку, правда Моника?!"

    img 11398
    with diss
    m "Твоя цена?"
    img 11421
    with fade
    steve "$ 1000, Моника!"

    music Power_Bots_Loop
    img 11410
    with diss
    m "СКОЛЬКО?!?!?"
    m "Ты за кого меня принимаешь, Стив?!"

    music Groove2_85
    img 11411
    with fade
    steve "Но Моника! Я могу тратить только деньги из моей официальной зарплаты!"
    steve "И я теперь помолвлен с Джейн. Она следит за тем куда я трачу свою зарплату!"

    img 11415
    with diss
    steve "Моника, я собираюсь отдать тебе все свои деньги на ланч на месяц вперед!"
    steve "Я жертвую всем! Ради тебя! Ради выгодной сделки..."

    music Power_Bots_Loop
    img 11393
    with fade
    menu:
        "Это слишком маленькие деньги, Стив! Я даже не буду это обсуждать...":
            img 11487
            with fadelong
            m "Это слишком маленькие деньги, Стив! Я даже не буду это обсуждать..."
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            $ questHelp("steve_10", False)
            $ questHelp("steve_17", False)
            $ questHelp("steve_9a", False)
            return False
        "Мне нужно хотя бы $ 10.000, Стив!":
            pass

    music stop
    img black_screen
    with diss
    sound snd_zip
    pause 2.0
    music Groove2_85
    img 11431
    with fadelong
    w
    img 11433
    with diss
    m "Мне нужно хотя бы $ 10.000, Стив!"
    img 11432
    with fade
    steve "Моника, у меня есть предложение! Давай я возьму в аренду половину твоего ротика за $ 1.500!"

    img 11435
    with diss
    m "Половину?! Это как?! Это же не гребаный этаж в тауэре, Стив!"

    img 11436
    with fade
    steve "Я буду двигаться аккуратно! Только в одну сторону! И не буду трогать другую щеку!"
    steve "Я буду соблюдать условия сделки! Я честный бизнесмен."

    if steveOffended1 == True:
        img 11434
        $ notif(t_("Моника сказала Стиву по телефону что он мешок с дерьмом.."))
        m "Ты мешок с дерьмом, а не бизнесмен!"

label ep25_dialogues2_steve10_loop1:
# Выбор: отказаться, либо череда выборов с торговлей
# В итоге сходятся на $ 5.000
    img 11437
    with fade
    menu:
        "$ 8.000 за весь объект аренды!":
            img 11438
            with fade
            m "$ 8.000 за весь объект аренды!"
            steve "$ 2.000 за половину!"
            menu:
                "Тогда за целый объект $ 7.000!":
                    img 11440
                    with fade
                    m "Тогда за целый объект $ 7.000!"
                    steve "За целый объект $ 4.000"
                    jump ep25_dialogues2_steve10_loop1
                "$ 6.000 за половину! За целый $ 10.000!":
                    img 11442
                    with fade
                    m "$ 6.000 за половину! За целый $ 10.000!"
                    steve "$ 3.500 за целый! $ 1.500 за половину!"
                    jump ep25_dialogues2_steve10_loop1
        "$ 7.000 за половину, за целый $ 10.000!":
            img 11440
            with fade
            m "$ 7.000 за половину, за целый $ 10.000!"
            steve "$ 2.000 за половину!"
            menu:
                "За половину $ 4.000, за целый $ 7.000...":
                    img 11441
                    with fade
                    m "За половину $ 4.000, за целый $ 7.000..."
                    steve "$ 2.200 за половину!"
                    jump ep25_dialogues2_steve10_loop1
                "$ 3.000 за половину, за целый $ 6.000!":
                    img 11443
                    with fade
                    m "$ 3.000 за половину, за целый $ 6.000!"
                    steve "$ 5.000 за целый!"
                    menu:
                        "Я согласна...":
                            pass
                        "$ 5.500 за целый!":
                            img 11444
                            with fade
                            m "$ 5.500 за целый!"
                            steve "За целый $4.000!"
                            jump ep25_dialogues2_steve10_loop1


    img 11443
    with fadelong
    w
    img 11444
    with diss
    w
    img 11445
    with diss
    w
    img 11446
    with diss
    m "Черт с тобой, Стив!"
    img 11447
    with diss
    mt "По крайней мере у меня будут деньги для этой сучки Виктории!"
    mt "И мне не придется позориться перед камерой на весь мир!"
    mt "Обо мне уже начинают ходить слухи..."
    mt "Это нехорошо. Я скоро верну свое положение и мне не стоит терять репутацию..."

    img 11448
    with fade
    m "Я согласна..."
    $ monicaMadeBlowjobForSteveChair = True
# Затем blowjob.
# Моника уходит, Стив переводит деньги

    m "..."
    music Loved_Up
    img 11451
    with fade
    steve "Ну же, Моника!"
    img 11453
    with diss
    m "..."
    img 11454
    with diss
    steve "..."
    sound hlup10
    img 11455
    with diss
    steve "Моника, давай быстрее!"
    img 11456
    with fade
    steve "Джейн может войти в любой момент!"
    img 11457
    w
    m "..."
    music stop
    img 11458
    with diss
    steve "Ну же!"
    sound hlup10
    img 11459
    with diss
    steve "О ДА!!!"
    music Loved_Up2
    steve "Как же я мечтал об этом дне!"
    steve "О дне, когда я вгоню свой член в твой ротик!"
    # video
    music stop
    music2 Loved_Up2
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_1 = Movie(play="video/v_Steve_Monica_Blowjob_1_1.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_2 = Movie(play="video/v_Steve_Monica_Blowjob_1_2.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_2
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_3 = Movie(play="video/v_Steve_Monica_Blowjob_1_3.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_3
    with fadelong
    wclean

    stop music
    img 11460
    with diss
    steve "Каждый раз, когда ты приходила и кричала на меня, я мечтал об этом дне!"
    img 11461
    with diss
    m "!!!"
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_4 = Movie(play="video/v_Steve_Monica_Blowjob_1_4.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_4
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_5 = Movie(play="video/v_Steve_Monica_Blowjob_1_5.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_5
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_6 = Movie(play="video/v_Steve_Monica_Blowjob_1_6.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_6
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_7 = Movie(play="video/v_Steve_Monica_Blowjob_1_7.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_8 = Movie(play="video/v_Steve_Monica_Blowjob_1_8.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_8
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_9 = Movie(play="video/v_Steve_Monica_Blowjob_1_9.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_9
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_10 = Movie(play="video/v_Steve_Monica_Blowjob_1_10.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_10
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_Steve_Blowjob1.mp3"
    scene black
    image videov_Steve_Monica_Blowjob_1_11 = Movie(play="video/v_Steve_Monica_Blowjob_1_11.mkv", fps=30)
    show videov_Steve_Monica_Blowjob_1_11
    with fadelong
    wclean

    music2 stop
    $ renpy.music.set_volume(1.0, 0.0, 'music2')

    stop music
    music stop
    music2 stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 11462
    with fadelong
    sound bulk1
    steve "АААААХХХХХХХ!!!"
    m "!!!"
    music Groove2_85
    img 11463
    with fadelong
    m "Тьфу!"
    mt "Мерзость!"

    music stop
    img black_screen
    with diss
    pause 2.0
    $ add_corruption(monicaSteveFirstBlowjobDeal, "monicaSteveFirstBlowjobDeal")
    music Power_Bots_Loop
    img 11464
    with fadelong
    m "Только попробуй не перевести деньги, мерзавец!"
    steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
    steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"


    $ questHelp("steve_10")
    $ questHelp("steve_17")
    $ questHelp("steve_9a", True)

    return True


label ep25_dialogues2_steve11:
    mt "Мне нечего там делать сегодня!"
    return






















#
