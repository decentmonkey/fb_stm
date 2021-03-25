label gallery_23333:
    # банкир сидит, развалившись, на диване, Моника стоит перед ним в трусиках и маске, Эшли стоит возле двери
    # Моника немного растеряна, смотри на Эшли, потом на клиента
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.5
    music Groove2_85
    img 23316
    with fadelong
    w
    img 23317
    with fade
    mt "Эта извращенка Эшли не упустит своего шанса..."
    mt "Чтобы пялиться на меня!"
    mt "Делая вид, что она контролирует меня."
    img 23318
    with diss
    banker "О, детка..."
    banker "Наконец-то ты пришла, [monica_pub_name]."
    music Power_Bots_Loop
    img 23319
    with fade
    mt "Очередной никчемный неудачник."
    # банкир ведет себя оч вальяжно, самодовольно усмехается
    music Groove2_85
    img 23320
    with diss
    banker "Давай, крошка, лезь на стол."
    banker "Не заставляй меня ждать... Время - деньги."
    # Моника недовольна
    music Power_Bots_Loop
    img 23321
    with fade
    mt "Мерзкий тип!"
    mt "Если он притронется ко мне - врежу ему по яйцам!"
    music Groove2_85
    img 23322
    with diss
    ashley "Ну? Чего ты ждешь?!"
    ashley "Ты слышала, что тебе нужно сделать?"
    mt "!!!"
    menu:
        "Залезть на стол и танцевать.":
            pass
    # Моника забирается на стол и начинает танцевать
    # банкир в это время пялится на нее, периодически бросая взгляды на Эшли и рассматрия ее
    # Эшли пялится на прелести Моники, на банкра ноль внимания
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music RocknRoll_loop
    img 23323
    with fadelong
    w
    img 23324
    with fade
    w
    img 23325
    with diss
    w
    img 23326
    with fade
    w
    img 23327
    with diss
    w
    img 23328
    with diss
    w
    img 23329
    with fade
    w
    music stop
    img 23330
    with diss
    w
    sound snd_fabric1
    img 23331
    with diss
    w
    music RocknRoll_loop
    img 23332
    with fade
    w
    img 23333
    with diss
    w
    img 23334
    with fade
    w
    img 23335
    with diss
    w
    img 23336
    with diss
    w
    # через некоторое время банкир говорит Монике
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 23337
    with fadelong
    w
    img 23338
    with fade
    banker "Детка, снимай с себя трусики."
    banker "Хочу посмотреть, что ты там прячешь."
    music Power_Bots_Loop
    img 23339
    with hpunch
    mt "Черт!"
    # Моника медлит, смотрит на Эшли
    music Groove2_85
    img 23340
    with fade
    ashley "Выполняй!"
    img 23341
    with diss
    mt "!!!"
    menu:
        "Снять трусики.":
            pass
        "Не делать этого! (увольнение с паба)":
            mt "Я не собираюсь танцевать голой перед..."
            mt "Перед каким-то никчемным неудачником!"
            mt "Пусть Эшли сама вертит перед ним своим голым задом!"
            m "!!!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            m "Нет!"
            m "Я не буду этого делать!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            # Моника гордо уходит
            return
    music Groove2_85
    img 23342
    with fade
    mt "Это делает [monica_pub_name], а не я."
    mt "[monica_pub_name] просто потанцует и уйдет отсюда."
    # она снимает трусики и танцует, банкир пялится на нее, потом расстегивает штаны и достает стояк
    label gallery_23354:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 23343
    with fadelong
    w
    img 23344
    with fade
    w
    img 23345
    with diss
    w
    img 23346
    with diss
    w
    img 23347
    with fade
    w
    img 23348
    with diss
    w
    img 23349
    with fade
    w
    img 23350
    with diss
    w
    img 23351
    with fade
    w
    img 23352
    with diss
    w
    img 23353
    with fade
    w
    img 23354
    with diss
    w
    img 23355
    with fade
    w
    img 23356
    with diss
    w
    img 23357
    with diss
    w
    img 23358
    with fade
    w
    img 23359
    with diss
    w
    img 23360
    with diss
    w

    img 23361
    sound Jump2
#    sound snd_fabric1
    banker "Эй, крошка."
    banker "Смотри, что у меня для тебя есть!"
    img 23362
    with diss
    banker "Пойдем ко мне!" # хлопает себя по бедру, зовет Монику к себе на ручки
    music stop
    img 23363
    with hpunch
    sound plastinka1b
    mt "?!?!?!"
    # Моника смотрит на Эшли
    music Power_Bots_Loop
    img 23364
    with fade
    m "Эшли?!"
    m "Мы так не договаривались!!!"
    music Groove2_85
    img 23365
    with diss
    ashley "Тебе просто нужно спуститься вниз и посидеть у клиента на коленях."
    ashley "он не будет тебя трогать. это всего-лишь приватный танец!"
    ashley "Чего здесь такого?!"
    img 23366
    with fade
    ashley "Делай, что тебе говорят!"
    img 23367
    with diss
    mt "Какого черта тут происходит?!"
    mt "Она решила подложить меня под этого мерзкого типа?!"
    mt "Знала бы она с кем вообще имеет дело!!!"
    mt "!!!"
    menu:
        "Сесть на колени к банкиру.":
            pass
        "Не делать этого! (увольнение из паба)":
            mt "Я не собираюсь этого делать!"
            mt "Пусть он лапает Эшли своими грязными руками!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            m "!!!"
            m "Нет!"
            m "Я не буду этого делать!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            # Моника гордо уходит
            return
    # Моника зло смотрит на Эшли
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 23368
    with fadelong
    mt "Грязная извращенка!"
    mt "Ненавижу ее!!!"
    mt "!!!"
    # Моника спускается со стола и садится к банкиру на ручки
    # тот без особого энтузиазма лапает ее, Моника напряжена как струна
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up
    img 23369
    with fadelong
    w
    img 23370
    with fade
    banker "Мммм, какая ты аппетитная, крошка..."
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w

    img 23373
    with fade
    w
    img 23374
    with diss
    w
    # банкир, пока лапает Монику, поглядывает постоянно на Эшли
    # потом обращается к Эшли
    music Groove2_85
    img 23375
    with fade
    ashley "Ну что, Мистер Беркельбаух, Вы довольны?"
    ashley "Вы помните номер кредитного договора, по которому надо дать отсрочку?"

    img 23376
    with diss
    banker "Эшли, знаешь что больше всего в мире мне не нравится?"

    img 23377
    with fade
    ashley "Что, Мистер Беркельбаух?"

    img 23378
    with diss
    banker "Больше всего в мире мне не нравится, когда меня обманывают."

    img 23379
    with diss
    ashley "Что это значит? На что Вы намекаете? В чем обман?"

    img 23380
    with fade
    banker "Эшли, помнишь какое было условие?"
    ashley "Вы хотели увидеть самую красивую попку Shiny Hole..."
    ashley "И за это..."

    music Hidden_Agenda
    img 23381
    with diss
    banker "Я не уверен что это самая красивая попка Shiny Hole."
    banker "Возможно, ты обманываешь меня."

    music Groove2_85
    img 23382
    with fade
    ashley "ЧТО?! Я???"
    ashley "Я с самого начала говорила тебе... Вам..."
    ashley "С самого начала говорила что у Молли задница лучше, чем у [monica_pub_name]!"
    img 23383
    with diss
    ashley "Но ты... то есть Вы..."

    sound Jump1
    img 23384
    with fade
    banker "Эшли, прекрати! Задница Молли мне уже надоела."
    banker "Эта ваша королева Shiny Hole готова на все ради пары баксов на чай!"

    img 23385
    with diss
    ashley "В чем тогда дело?! Почему Вы обвиняете меня в нечестности?!"

    music Hidden_Agenda
    img 23386
    with fade
    banker "Я не уверен что у [monica_pub_name] лучшая задница, потому что я не могу сравнить их все."
    banker "Я еще не все увидел."
    banker "А, потому, я имею право сомневаться в том, что ты даешь мне то, что декларируешь."

    music Groove2_85
    ashley "Что я де... декл... Что это за слово?"

    img 23387
    with diss
    ashley "Послушайте, Мистер Беркельбаух, Вы наш постоянный клиент и Вы знаете, что Клэр не танцует приват."
    ashley "Ее задницу не получится оценить. Она танцует не ради денег."
    ashley "Я никак не могу надавить на нее. Если я буду настаивать, она просто уйдет отсюда!"

    img 23388
    with fade
    banker "Я вижу задницу Клэр через день! Пусть она в тоненьких трусиках, но я могу оценить ее из зала."

    img 23389
    with diss
    ashley "Но в чем тогда проблема? Это все что у нас есть!"
    ashley "У нас больше нет никаких попок, чтобы сравнить между ними!"
    ashley "Я честно выполнила то о чем мы договорились!"

    music Hidden_Agenda
    img 23390
    with fade
    banker "Нет, Эшли! Здесь, в Shiny Hole, есть еще одна попка, которую никто не видел!"
    banker "И ее не оценить из зала, потому что она пока не танцует, а зря!"

    music Groove2_85
    img 23391
    with diss
    ashley "Какая? Кто это? Почему я не знаю про нее?!"
    ashley "Это Джо снова притащил какую-то шлюху?!"
    ashley "Также как сделал это с [monica_pub_name]?"

    img 23392
    with diss
    mt "!!!"

    music Hidden_Agenda
    img 23393
    with fade
    banker "Нет, Эшли! Я говорю про твою попку!"

    music stop
    img 23394
    with hpunch
    sound plastinka1b
    ashley "ЧТО?! Причем здесь моя задница, Мистер Беркельбаух?!"

    music Hidden_Agenda
    img 23395
    with fade
    banker "При том, Эшли, что я подозреваю что твоя попка самая лучшая в Shiny Hole!"
    banker "И ты скрыла это от меня, тем самым обманув."
    banker "А ты уже знаешь что я больше всего не люблю..."

    music Groove2_85
    img 23396
    with diss
    ashley "Но... Но как можно сравнивать меня с..."
    ashley "С [monica_pub_name]?"

    music Hidden_Agenda
    img 23397
    with fade
    banker "Почему нельзя? Я не видел всех попок Shiny Hole и я имею право сомневаться!"

    img 23398
    with diss
    ashley "И что же ты хочешь?!"

    img 23399
    with diss
    banker "Залезай на стол и покажи свою попку, а я сравню ее с этой!"

    music Groove2_85
    img 23400
    with fade
    ashley "Вообще-то я замужем!"
    ashley "Моя попка, она... Она только для Джо, моего мужа!"

    img 23401
    with diss
    banker "Я не собираюсь сейчас трахать тебя, Эшли!"
    banker "И здесь нет твоего Джо! Он смотрит за баром, пока тебя нет."

    music Hidden_Agenda
    img 23402
    with diss
    banker "Но учти, отказ от проверки значит что ты что-то скрываешь от меня!"
    banker "Если ты не предоставишь доказательство того, что твоя попка хуже, чем у [monica_pub_name]..."
    banker "Или, если вдруг эта твоя попка не окажется хуже, чем у нее, то..."
    banker "То банк завтра же выставит требование о досрочном погашении всей вашей кредитной линии, Эшли!!!"
    banker "Я не терплю, когда меня пытаются выставить дураком, подсунув второсортный материал!"

    music Power_Bots_Loop
    img 23403
    with fade
    mt "ЧТО?!!"

    img 23404
    with diss
    ashley "!!!"
    banker "Давай! Залезай сейчас же! Я жду!"
    music Groove2_85
    banker "И пусть [monica_pub_name] встанет рядом с тобой!"

    img 23405
    with fade
    ashley "Ты мне что, не оставляешь выбора?! Ты знаешь что я вкладываю душу в этом место!"
    ashley "Я не могу потерять его!"

    music Hidden_Agenda
    img 23406
    with diss
    banker "Это ты не оставляешь мне выбора, Эшли! Ты отказываешься предъявить доказательство!"
    banker "Вертишься, юлишь..."
    banker "Ведь, если твоя попка и правда хуже, то тебе нечего бояться, правда?"

    music Power_Bots_Loop
    img 23407
    with fade
    ashley "!!!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 23408
    with fadelong
    w

    img 23409
    with fade
    banker "Да, и смотри на меня! Личико влияет на оценку любой попки!"
    banker "Исходя из специфики своей работы, я люблю все оценивать комплексно!"

    music Power_Bots_Loop
    img 23410
    with diss
    ashley "!!!"

    music Groove2_85
    img 23411
    with fade
    banker "Да, и скажи [monica_pub_name], чтобы она сняла свою маску."
    banker "Я вижу ее личико каждый день, когда она обслуживает клиентов."
    banker "Незачем скрывать его сейчас. Это помешает комплексной оценке!"

    music Power_Bots_Loop
    img 23412
    with hpunch
    m "ЧТО?!"

    music Groove2_85
    img 23413
    with fade
    ashley "Давай, снимай свою дурацкую маску, делай что он говорит!"
    ashley "И залезай сюда!"

    img 23414
    with diss
    m "Но!.."

    img 23415
    with fade
    ashley "Давай, он и так знает кто ты на самом деле!"

    music stop
    img 23416
    with hpunch
    sound plastinka1b
    m "Он знает кто Я???"

    music Groove2_85
    img 23417
    with diss
    ashley "Да, он знает, что ты новенькая официантка! Давай снимай!"
    menu:
        "Снять маску":
            pass
        "Не делать этого! (увольнение из паба)":
            m "Я не собираюсь делать подобное! Это уже слишком!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return

    # Монике
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 23418
    with fadelong
    w
    img 23419
    with fade
    w
    music Pyro_Flow
    img 23420
    with diss
    ashley "Только попробуй сделать что-то, чтобы твоя задница понравилась ему меньше моей!"
    ashley "Тогда ты не просто вылетишь отсюда..."
    ashley "Но я снова повешу на тебя все украденные чаевые, которые до этого простила тебе!"
    img 23421
    with diss
    m "!!!"
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 23422
    with fade
    w
    img 23423
    with diss
    ashley "Встань в лучшую позу, какую только можешь! Соблазни его!"
#    music Loved_Up
    img 23424
    with fade
    mt "Что я делаю... О БОЖЕ..."
    mt "Я стоя голая... АБСОЛЮТНО ГОЛАЯ!!!"
    img 23425
    with diss
    mt "Без маски..."
    mt "Стою так, чтобы моя попа понравилась больше, чем задница хозяйки дыры в трущобах!"
    img 23426
    with fade
    mt "И понравилась кому?!?!"
    mt "Какому-то никчемному клерку из кредитного отдела занюханного банка!"
    img 23427
    with diss
    mt "Ведь он даже не представляет, на какую леди он сейчас смотрит!"
    mt "Ему недостижим мой уровень, даже в его снах!"
    img 23428
    with fade
    ashley "Ну, убедился?!"
    banker "Я пока размышляю..."
    sound drkanje5
    img 23429
    with fade #repeat
    w
    sound drkanje5
    img 23430
    with diss
    w
    sound drkanje5
    img 23429
    with diss
    w
    sound drkanje5
    img 23430
    with diss
    w
    sound drkanje5
    img 23429
    with diss
    w
    sound drkanje5
    img 23430
    with diss
    w
    sound drkanje5
    img 23429
    with diss
    w
    sound drkanje5
    img 23430
    with diss
    w


    img 23431
    with fade
    banker "Какое твое мнение, Эшли?"
    img 23432
    with diss
    ashley "В смысле какое мое мнение?"
    img 23433
    with fade
    banker "Как ты думаешь, чья задница хуже? Твоя или [monica_pub_name]?"
    ashley "Мне обязательно это говорить?"

    img 23434
    with diss
    banker "Да, Эшли. Я хочу услышать это от тебя."
    banker "Я хочу услышать твою уверенность... в своей правоте..."

    img 23435
    with fade
    ashley "!!!"
    ashley "Я... Я считаю..."
    ashley "Я считаю что моя задница хуже, чем у [monica_pub_name]."

    img 23436
    with diss
    banker "Хорошо, Эшли! Твоя уверенность убедила меня."
    banker "Да и, по правде говоря, твоя задница действительно ни к черту в сравнению с попкой [monica_pub_name]!"
    music Power_Bots_Loop
    img 23437
    with fade
    ashley "!!!"
    music Groove2_85
    img 23438
    with diss
    sound vjuh3
    banker "Я подпишу бумаги."
    banker "Но, впрочем, она не настолько уж плоха для сцены."
    banker "Я бы, как зритель, одобрил, если бы ты вышла на сцену в одном лишь фартуке."
    banker "Хе-хе!"

    img 23439
    with fade
    ashley "Мистер Беркельбаух!"
    ashley "Я уже говорила Вам, что для танцев у нас есть такие шлюхи, как [monica_pub_name]."
    ashley "Я занимаюсь здесь управлением и ведением бизнеса!"
    img 23440
    with diss
    banker "Да, Эшли. Конечно!"
    banker "Хе-хе!"
    banker "Сообщи мне, если у тебя снова возникнут финансовые трудности!"

    img 23441
    with fade
    m "Мы закончили? Я могу идти?!"

    img 23442
    with diss
    banker "Не так быстро! Я все еще не кончил."
    img 23443
    with diss
    banker "Эшли, ты ведь знаешь, приватный танец должен длиться, пока клиент не будет удовлетворен..."
    ashley "Да, Мистер Беркельбаух..."

    img 23444
    with fade
    ashley "[monica_pub_name], ты должна удовлетворить клиента!"
    with hpunch
    m "Что?! Я не знала о подобном правиле!"
    m "С какой стати Я..."

    img 23445
    with diss
    ashley "Знание правил не помогает тебе придерживаться их!"
    ashley "Не забывай почему ты оказалась здесь!"
    ashley "Быстро иди и удовлетвори клиента!"

    img 23446
    with fade
    m "Но как... Как я удовлетворю его?!"
    img 23447
    with diss
    banker "Я бы хотел чтобы эта прекрасная попка потерлась о мой банковский член."
    img 23448
    with fade
    ashley "Ты слышала?! Быстро иди к нему!"
    img 23449
    with diss
    m "!!!"
    menu:
        "Тереться о член Мистера Беркельбауха...":
            pass
        "Не делать этого! (увольнение из паба)":
            m "Я не собираюсь делать подобное! Это уже слишком!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music2 Loved_Up
    img 23450
    with fadelong
    w
    img 23451
    with fade
    w
    img 23452
    with diss
    w
    img 23453
    with fade
    banker "Вот так... Да."
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_PrivateDance1_1.ogg"
    scene black
    image videov_Monica_PrivateDance1_1 = Movie(play="video/v_Monica_PrivateDance1_1.mkv", fps=30)
    show videov_Monica_PrivateDance1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 23454
    with diss
    mt "Фу!"
    mt "!!!"
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_PrivateDance1_1.ogg"
    scene black
    image videov_Monica_PrivateDance1_2 = Movie(play="video/v_Monica_PrivateDance1_2.mkv", fps=30)
    show videov_Monica_PrivateDance1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 23455
    with diss
    w
#    music Loved_Up2
    img 23456
    with diss
    banker "Хорошая девочка."
    w
    img 23457
    with fade
    w
    img 23458
    with diss
    mt "Вот он извращенец!"
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_PrivateDance1_1.ogg"
    scene black
    image videov_Monica_PrivateDance1_3 = Movie(play="video/v_Monica_PrivateDance1_3.mkv", fps=30)
    show videov_Monica_PrivateDance1_3
    with fade
    wclean
    stop music
    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 23459
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    # вставить текст в арты

    # банкир кончает
    img 23460
    sound2 Jump1
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    # ахи?
    w
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    # Моника встает, он тоже и застегивает штаны
    img 23461
    with fade
    banker "Девочки, вы хорошо поработали."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound snd_zip
    pause 1.0
    music Groove2_85
    img 23462
    with fadelong
    banker "Эшли, жду тебя завтра у себя в банке."
    banker "Обсудим детали кредитного договора."
    img 23463
    with hpunch
    sound snd_slap1
    banker "Пока, крошка." # хлопает Монику по голой попе
    img 23464
    with diss
    w
    # банкир уходит
    # Эшли зло смотрит на Монику
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.0
    sound snd_fabric1
    pause 1.0
    music Pyro_Flow
    img 23465
    with fadelong
    w
    img 23466
    with fade
    ashley "!!!"
    img 23467
    with diss
    m "!!!"
    img 23468
    with fade
    ashley "[monica_pub_name], только попробуй рассказать об этом кому-нибудь!"
    ashley "Если хоть кто-то узнает!"
    ashley "Я тебя придушу!!!"
    img 23469
    with diss
    mt "Жаль. Думаю, Джо было бы интересно услышать подробности."
    img 23471
    with fade
    ashley "Поняла меня, [monica_pub_name]?!"
    img 23472
    with diss
    m "Иди ты к черту, Эшли!"
#    m "Я не расскажу никому."
    m "Знала бы я на что мне придется идти, то лучше бы уволилась отсюда!"
    img 23473
    with fade
    ashley "Все! Иди! Ты на сегодня свободна."
    return

label gallery_30496:
    # на диване сидит, развалившись клиент (скучающий чувак у шеста)
    # Джо стоит в стороне и наблюдает
#    $ temp_var1 = monica_strip_tips_today
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 30475
    with fadelong
    customer3 "О, наконец-то пришла..."
    img 23321
    with fade
    mt "Фу! Я помню этого клиента..."
    mt "Строит из себя непонятного кого..."
    mt "А на самом деле такой же неудачник, как и все!"
    img 30476
    with diss
    customer3 "Ну давай... Как там тебя зовут?"
    m "Я..."
    customer3 "Впрочем, неважно. Я все равно не запомню."
    img 30477
    with diss
    customer3 "Я рад что ты не как Мэнсфилд..."
    customer3 "Хорошо, что ты такая же шлюха, как та рыжая..."
    music Power_Bots_Loop
    img 30478
    with fade
    mt "!!!"
    mt "Мерзавец!"
    img 30479
    with diss
    m "Я не шлюха!" # зло
    # Джо вмешивается и строго говорит
    music Groove2_85
    img 30480
    with fade
    joe "Не спорь с клиентом!!!"
    # Моника смотрит на Джо
    img 30481
    with diss
    m "!!!"
    customer3 "Да, лучше не спорь..."
    customer3 "Скажи, что ты шлюха. Я доплачу тебе за это 50 баксов."
    img 30482
    with diss
    mt "Что этот неудачник себе позвояет?!"
    mt "?!?!?!"
#    $ menu_corruption = [ep212_private_dance2]
    menu:
        "Притвориться шлюхой.":
            music Groove2_85
            img 30483
            with fade
            customer3 "Ну, отвечай..."
            customer3 "Ты шлюха?"
            m "..."
            img 30484
            with diss
            mt "Если я сейчас не сделаю, как он просит..."
            mt "Клиент будет недоволен и Джо расскажет об этом Эшли."
            img 30485
            with fade
            mt "И эта извращенка Эшли снова меня оштрафует."
            mt "Я не могу допустить того, чтобы она отбирала у меня деньги..."
            img 30486
            with diss
            mt "Тем более, это не я себя назову шл... Этим словом."
            mt "Это делает [monica_pub_name]..."
            mt "..."
            img 30487
            with fade
            m "Я..."
            m "Шлюха..."
#            $ add_money(50.0)
#            $ monica_strip_tips_today += 50.0
            img 30488
            with diss
            customer3 "Да..."
            customer3 "Видишь, как все просто?"
            customer3 "Сказала всего два слова и уже заработала полтинник."
            sound Jump2
            img 30489
            with fade
            customer3 "А теперь шлюха станцует для меня."
            customer3 "И получит за это еще денег..."
            customer3 "Шлюха же хочет еще денег?"
            music Power_Bots_Loop
            img 30490
            with diss
            m "..." # зло смотрит на него
            music Groove2_85
            img 30491
            with fade
            customer3 "Скучно с тобой... Даже поговорить не можешь нормально." # лениво
            customer3 "Не удивительно, что ты не можешь устроиться на нормальную работу, как Я..."
            customer3 "А зарабатываешь, показывая свою задницу со сцены..."
        "Поставить на место этого идиота! (Моника слишком приличная) (disabled)" if monicaBitch == False: #
            pass
        "Поставить на место этого идиота!" if monicaBitch == True:
            # Монику бомбит, она орет на клиента
            music Pyro_Flow
            $ notif_monica()
            img 30492
            with fade
            m "Слышишь, ты?!"
#            m "Еще раз назовешь меня шлюхой, я тебе оторву твои яйца!"
            joe "[monica_pub_name]!"
            # рявкает на Джо
            img 30493
            with hpunch
            m "Заткнись, Джо!"
            m "!!!"
            # потом снова на клиента
            img 30494
            with diss
            m "Еще раз назовешь меня шлюхой, я тебе оторву твои яйца!"
            sound highheels_short_walk
            img 30495
            with fade
            w
            return
    music Pyro_Flow
    img 30482
    with diss
    mt "Вот сволочь!"
    mt "Знал бы он, кто Я такая на самом деле!"
    mt "!!!"
    music Groove2_85
    sound heel1
    img 30496
    with fade
    customer3 "Я рад, что я первый, для кого ты танцуешь приват."
    customer3 "Помимо меня еще много желающих посмотреть на твою голую задниицу."
    customer3 "Но я их всех опередил."
    # Джо улыбается ехидно
    music Marty_Gots_a_Plan
    img 30497
    with diss
    joe "..."
    m "..."
    music Groove2_85
    img 30498
    with fade
    mt "Самомнение просто зашкаливает, а на деле..."
    mt "Очередной никчемный неудачник!"
    img 30499
    with diss
    customer3 "Танцуй давай!"
    menu:
        "Начать танцевать.":
            pass
    # Моника начинает танцевать
    # клиент с Джо похотливо на нее смотрят
    music Road_Trip
    img 30500
    with fade
    w
    img 30501
    with diss
    w
    img 30502
    with fade
    w
    img 30503
    with diss
    w
    img 30504
    with fade
    customer3 "Знаешь, ты хоть и скучная, но задница у тебя что надо..."
    customer3 "Я давно хотел, чтобы ты сняла свой наряд официантки и показала мне ее..."
    customer3 "Я видел почти всю твою задницу, когда заглядывал тебе под юбку в прошлый раз."
    customer3 "Но знаешь, так мне будет гораздо удобнее ее разглядеть."
    music stop
    sound plastinka2
    img 30505
    with hpunch
    mt "?!?!?!"
    img 30506
    with diss
    m "Я не..."
    music Groove2_85
    if customer3_dance_comment_stage >= 1:
        # если с клиентом уже был диалог, что он видел ее на сцене, а Моника-официантка это отрицала
        $ notif(t_("Моника говорила клиенту, что не танцует на сцене."))
        #
        img 30507
        with fade
        customer3 "Ну да, ну да..."
        customer3 "Ты не работаешь здесь официанткой... Бла-бла-бла..."
        customer3 "Неважно..."
    img 30508
    with diss
    customer3 "Снимай одежду..."
    customer3 "Я плачу деньги не за танцы в этих тряпках."
    music Power_Bots_Loop
    img 30509
    with diss
    mt "Животное!"
    mt "!!!"
    # Моника танцует и снимает с себя жилет
    # Джо стоит подрачивает под своим фартучком
    # после того как она полностью разделась, клиент достает свой член
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Road_Trip
#    $ add_money(100.0)
#    $ monica_strip_tips_today += 100.0
    img 23330
    with fade
    w
    img 23331
    with diss
    w
    img 30510
    with fade
    w
    img 30511
    with diss
    w
    img 30512
    with fade
    w
    img 30513
    with diss
    w
    img 30514
    with fade
    w
    img 30515
    with diss
    w
    img 30516
    with diss
    w
    sound vjuh3
    img 30517
    with fade
    w
    img 30518
    with diss
    w
    img 30519
    with diss
    w
    img 30520
    with fade
    w
    img 30521
    with hpunch
    customer3 "Эй ты, смотри что у меня для тебя есть!"
    customer3 "Иди сюда, я хочу потрогать тебя..."
    music Power_Bots_Loop
    img 30522
    with fade
    mt "Начинается!"
    mt "!!!"
    music Groove2_85
    img 30523
    with diss
    m "По правилам бара клиентам на меня можно только смотреть."
    m "Прикасаться нельзя."
    img 30524
    with fade
    customer3 "Да ладно тебе! Заработаешь больше."
    customer3 "Об этом все равно никто не узнает."
    img 30525
    with diss
    customer3 "Да, Джо?" # ехидно улыбается
    joe "Конечно!" # тоже противно улыбается
    joe "Клиент должен быть удовлетворен!"
    img 30526
    with diss
    mt "..."
#    $ menu_corruption = [ep212_private_dance3]
    menu:
        "Сделать как требует клиент.":
            pass
        "Поставить на место этого идиота!": #
            # Монику бомбит, она орет на клиента
            music Pyro_Flow
            $ notif_monica()
            img 30527
            with fade
            m "Слышишь, ты, животное?!"
            m "Засунь свои гребанные деньги себе в задницу!"
            m "И не смей прикасаться ко мне!"
            m "Иначе я тебе яйца оторву!"
            img 30528
            with diss
            joe "[monica_pub_name]!"
            # рявкает на Джо
            img 30529
            with hpunch
            m "Заткнись, Джо!"
            m "!!!"
            # потом снова на клиента
            img 30530
            with diss
            m "Неудачник!"
            m "!!!"
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            img 30531
            with fade
            w
            # уходит
            return
    # Моника или злится
    music Pyro_Flow
    img 30532
    with fade
    m "Я здесь танцую, а не занимаюсь проституцией!" # клиенту
    img 30533
    with diss
    m "Джо, ты говорил, что ничего подобного происходить не будет!" # Джо
    m "Что он просто посмотрит и все!"
    m "!!!"
    music Marty_Gots_a_Plan
    img 30534
    with fade
    joe "Все правильно."
    joe "Клиентам к девочкам на привате нельзя прикасаться... Руками..."
    m "???"
    m "Что это значит, Джо?!"
    img 30535
    with diss
    joe "Что ты сейчас удовлетворишь клиента."
    joe "Он тебя трогать при этом не будет."
    joe "Таким образом, ты не нарушишь правила, а клиент останется доволен."
    m "!!!"
    music Pyro_Flow
    img 30536
    with fade
    mt "Мерзавец Джо!"
    mt "О чем я только думала, когда пошла сюда с ним?!"
    mt "?!?!?!"
    music Groove2_85
    img 30537
    with diss
    mt "С другой стороны..."
    mt "Он же не будет прикасаться к моему телу своими грязными руками..."
    mt "А я смогу заработать больше денег..."
    img 30538
    with diss
    mt "Вернее, [monica_pub_name]... Она это будет делать..."
    mt "Моника Бакфетт на такое никогда бы не пошла!"
    mt "Ой, Моника, перестань называть себя по имени даже в мыслях, пока ты здесь!"
    mt "..."
    # клиент встает с дивана
    sound man_steps
    img 30539
    with fade
    customer3 "Мне надоело ждать..."
    customer3 "Подвинься!"
    customer3 "Я хочу, чтоб ты сделала это на столе..."
    img 30540
    with diss
    w
    sound Jump2
    img 30541
    with diss
    w
    # клент ложится на стол
    music Power_Bots_Loop
    img 30542
    with fade
    mt "!!!"
    music Groove2_85
    img 30543
    with diss
    customer3 "Что ты так смотришь?"
    customer3 "Как будто впервые увидела член."
    customer3 "Я заплачу тебе еще 100 баксов."
    customer3 "Давай, отрабатывай..."
    img 30544
    with diss
    mt "Черт!"
    mt "..."
    menu:
        "Тереться о член клиента.":
            pass
    # Джо стоит дрочит
    # Моника неуклюже пристраивается над клиентом так, чтобы можно было тереться об его член
    # но у нее не получается ничего
    label gallery_30550:
    music stop
    img black_screen
    with diss
    sound heel1
    pause 1.5
    music Loved_Up
    img 30545
    with fadelong
    w
    img 30546
    with fade
    m "!!!"
    img 30547
    with diss
    customer3 "Ну что ты делаешь?.."
    customer3 "Повернись ко мне своим задом и подвинься ближе."
    # Моника делает, как сказал клиент
    music stop
    img black_screen
    with diss
    sound Jump2
    pause 1.5
    music2 Loved_Up
    img 30548
    with fadelong
    customer3 "Вооот, другое дело!"
    customer3 "Вот так мне нравится больше."
    customer3 "Теперь я могу рассмотреть твою задницу поближе..."

    img 30549
    with fade
    w
    img 30554
    with diss
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_1 = Movie(play="video/v_Monica_Private2_Teasing1_1.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 30550
    with fade
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_2 = Movie(play="video/v_Monica_Private2_Teasing1_2.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 30551
    with diss
    w
    img 30552
    with fade
    w
    img 30553
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_3 = Movie(play="video/v_Monica_Private2_Teasing1_3.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 30555
    with fade
    mt "Долбанный извращенец!"
    mt "!!!"


    music2 Loved_up2
    img 30556
    with diss
    customer3 "Давай, шустрее шевели своей задницей!"
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_4 = Movie(play="video/v_Monica_Private2_Teasing1_4.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    customer3 "Дааа..."
    customer3 "Еще быстрей..."
    # Моника со злым лицом трется о клиента

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Private2_Teasing1_1.ogg"
    scene black
    image videov_Monica_Private2_Teasing1_5 = Movie(play="video/v_Monica_Private2_Teasing1_5.mkv", fps=30)
    show videov_Monica_Private2_Teasing1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 30557
    with fade
    customer3 "Мммммм..."
    customer3 "Еще немного..."
    customer3 "Вот так..."
    customer3 "Мммммм..."
    menu:
        "Кончить на попу Моники.":
            img 30558
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            customer3 "Аааааа..."
            img 30559
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            customer3 "ААААА..."
            img 30560
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            customer3 "АААААААА!!!"
            img 30561
            with fade
            w
            # Джо тихонько кончает в кулачок
            img 30562
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan6
            joe "Оооох..."
            joe "Ммммммм..."
            # Моника зло на него смотрит
            img 30563
            with fade
            mt "Джо сволочь!!!"
            mt "Твоя жена тебя не видит!"
            mt "!!!"
            pass
        "Кончить на лицо Моники.":
            img 30564
            with diss
            customer3 "Подставь свое лицо!"
            customer3 "Аааааа..."
            customer3 "Быстро!"
            customer3 "Дам за это сверху $ 30!"
            # Моника поворачивается и приближается лицо к его члену
            # он додрачивает и кончает на лицо
            img 30559
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 30565
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            customer3 "ААААА..."
            customer3 "АААААААА!!!"
            img 30566
            with fade
            mt "!!!"
            mt "Фууу!"
            img 30567
            with diss
            customer3 "Аха-ха!"
#            $ add_money(30.0)
#            $ monica_strip_tips_today += 30.0
            customer3 "Так твое лицо смотрится гораздо лучше!"
            mt "!!!"

            # Джо тихонько кончает в кулачок
            img 30562
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan6
            joe "Оооох..."
            joe "Ммммммм..."
            # Моника зло на него смотрит
            img 30566
#            img 30563
            with fade
            mt "Джо сволочь!!!"
            mt "Твоя жена тебя не видит!"
            mt "!!!"
            pass
    # смена кадра
    # клиент стоит одетый, клиент и Джо расслабленные и довольные, Моника стоит в трусиках, злая
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
#    $ add_money(100.0)
#    $ monica_strip_tips_today += 100.0
    img 30568
    with fadelong
    w
    img 30569
    with fade
    customer3 "Вот твой заработок..."
    customer3 "За то, что неплохо трешься задницей."
#    $ temp_var1 = monica_strip_tips_today - temp_var1
#    customer3 "Всего [temp_var1]. Ты неплохо заработала!"
#    customer3 "Почти ничего не делая..."
    music Power_Bots_Loop
    img 30570
    with diss
#    m "[temp_var1] долларов?!"
    m "?!?!?!"
    music Groove2_85
    customer3 "Да..."
    customer3 "Видишь, я могу быть очень щедрым, если шлюха хорошая."
    img 30571
    with diss
    sound man_steps
    w
    # клиент уходит, Моника остается вдвоем с Джо
    # Моника сердито смотрит на него
    music Pyro_Flow
    img 30572
    with fade
#    m "[temp_var1] долларов!"
    m "Джо!"
    m "Где обещанные 500?!"
    music Groove2_85
    img 30573
    with diss
    joe "[monica_pub_name], клиент обещал заплатить 500."
    joe "С тем условием, что ему все понравится."
    joe "В противном случае, клиент имеет право снизить сумму."
    joe "Тебе надо было лучше стараться, [monica_pub_name]..."
    mt "!!!"
    img 30574
    with diss
    joe "И не забудь отдать с этих денег процент Эшли."
    # Джо уходит
    sound man_steps
    img 30575
    with fade
    w
    music Pyro_Flow
    img 30576
    with diss
    mt "Он обманул меня!"
    mt "Мерзавец!"
    mt "И я еще должна платить процент Эшли!"
    img 30577
    with fade
    mt "АААААА!!!"
    mt "Ненавижу!"
    mt "!!!"
    return

label gallery_23732:
    # использовать имеющиеся арты
    music Hidden_Agenda
    sound highheels_short_walk
    img 14261
    with fadelong
    mt "Этот жалкий жадный неудачник!!!"
    mt "!!!"
    m "Что будете заказывать?"
    music Groove2_85
    img 14257
    with fade
    customer3 "О! Хочу снова заказать твою задницу!"
    img 14265
    with diss
    m "Это невозможно, я..."
    img 14263
    with fade
    customer3 "Ты не танцуешь приват. Ага..."
    customer3 "Это всего лишь вопрос денег..."
    customer3 "Аха-ха!!!"
    img 14255
    with diss
    mt "Долбануть бы этого козла чем-нибудь потяжелее!"
    mt "!!!"
    m "Что вам принести?"
    img 14262
    with fade
    customer3 "Какая же ты все-таки скучная..."
    customer3 "Принеси мне пива..."
    # Моника уходит и возвращается с пивом
    img 14266
    with diss
    sound highheels_short_walk
    w

    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    sound snd_plates1
    img 14271
    with fade
    w
    sound snd_beer_table
    img 14272
    with diss
    m "Пожалуйста, ваше пиво..."
    mt "Урод!"
    music Groove2_85
    img 14274
    with fade
    customer3 "Ага..."
    sound vjuh4
    img 23719
    with diss
    w
    sound snd_boot1
    img 23720
    with diss
    customer3 "Я дам тебе $ 10 на чай, если ты нагнешься и поднимешь ту зажигалку."
    customer3 "Только сделай это спиной ко мне! Аха-ха!!!"
    music Power_Bots_Loop
    img 23721
    with fade
    m "!!!"
    # если первый раз
    music Groove2_85
    img 14275
    with diss
    customer3 "Давай, не стесняйся! Я там все уже видел!"
    customer3 "Аха-ха!!!"
    img 23722
    with diss
    mt "Вот мерзавец!"
    mt "Я не собираюсь зарабатывать на чай таким образом!"
    img 23723
    with fade
    mt "..."
    mt "С другой стороны, здесь, похоже, других способов нет..."
    mt "Тем более он уже все видел..."
    img 14288
    with diss
    customer3 "Давай! Сделай это передо мной!"
    customer3 "Здесь больше никого нет!"

#    if monicaTakeLightFromFloor == True:
        # если уже было
#        music Groove2_85
#        img 23723
#        with diss
#        m "Я уже поднимала эту зажигалку..."
#        img 23722
#        with fade
#        customer3 "Но ведь ты хочешь еще чаевые?"
#        customer3 "Тогда подними ее еще раз!"
        #

    img 14286
    with diss
    m "..."
    menu:
        "Нагнуться за зажигалкой.":
            pass
        "Уйти.":
            music Pyro_Flow
            img 14296
            with fade
            sound highheels_short_walk
            m "Сам поднимай свои зажигалки, придурок!"
            return
    music Groove2_85
    img 23724
    with fade
    w
    img 23725
    with diss
    mt "Не могу поверить что я это делаю..."
    img 23726
    with fade
    w
    img 23727
    with diss
    w
    img 23728
    with fade
    w
    img 23729
    with diss
    w
    img 23730
    with fade
    w
    img 23731
    with diss
    w
    img 23732
    with fade
    w
    img 23733
    with diss
    w
#    $ add_tips(10.0)
    img 23734
    with diss
    customer3 "Отличная задница!"
    img 23735
    with diss
    customer3 "Скоро я всажу в нее свой член!"
    music Power_Bots_Loop
    sound Jump1
    img 23736
    with fade
    m "Этого никогда не будет!!!"
    music Groove2_85
    img 23737
    with diss
    sound highheels_short_walk
    customer3 "Иди уже."
    mt "!!!"
    return

label gallery_18248:
    # Моника еще не переоделась в костюм для стриптиза, стоит в одежде шлюхи
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 22663
    w
    sound highheels_short_walk
    imgf 22680
    mt "Я не собираюсь работать здесь за бесплатно!"
    mt "Показываю свое прекрасное тело толпе жалких пьяных неудачников Я, а деньги зарабатывает Эшли!"
    mt "И все из-за этой рыжей стервы!"
    music Power_Bots_Loop
    mt "Ненавижу ее!"
    mt "!!!"
    music Stealth_Groover
    imgd 22681
    mt "Так, Моника."
    mt "Тебе нужно просто притвориться, что ты хочешь с ней помириться."
    mt "На самом деле, это не так. Но тупая сучка Молли все равно этого не поймет."
    mt "Зато ты сможешь снова зарабатывать деньги."
    mt "И, возможно, она перестанет к тебе придираться."
    mt "..."
    # Моника подходит к Молли
    # та поворачивается и смотрит на нее вопросительно
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 22672
    w
    imgf 22673
    molly "Чего тебе надо, воровка?"
    imgd 22677
    mt "!!!"
    mt "Моника, спокойно!"
    mt "Просто сделай вид, притворись."
    imgd 22676
    m "..."
    m "Эшли сказала, чтобы мы помирились..."
    # Молли издевательски
    imgf 16135
    molly "Да ну?!"
    molly "И?"
    imgd 16139
    m "Я предлагаю сделать так, как требует Эшли."
    m "..."
    # Молли самодовольно смеется
    sound snd_woman_laugh
    imgf 22675
    molly "Это ты так просишь прощения?!"
    molly "Аха-ха!!!"
    molly "Ты вообще умеешь с людьми общаться по-нормальному?"
    molly "Ты где воспитывалась? В пещере?"
    molly "Понаедут сюда из своих деревень... Даже двух слов связать не могут!"
    # Монику бомбит
    music Pyro_Flow
    img 18224 vpunch
    mt "Сучка!"
    mt "Как эта грязная шлюха смеет говорить мне такое?!"
    mt "Тупая провинциальная дура!"
    mt "!!!"
    # Молли отворачивается от нее к своему зеркалу и равнодушно говорит
    fadeblack 1.5
    music Groove2_85
    imgf 22678
    molly "У меня есть несколько условий."
    molly "Если ты их выполнишь - я тебя прощу..."
    # Моника злобно
    imgd 18225
    mt "Она мне еще условия будет ставить?!"
    mt "?!?!?!"
    imgd 22672
    m "..."
    m "Какие еще условия?"
    # Молли продолжает также равнодушно, не смотря на Монику
    molly "Первое условие: ты признаешь, что Я - королева Shiny Hole."
    mt "?!"
    menu:
        "Сказать Молли, что она королева Shiny Hole.": # corruption
            pass
        "Не делать этого!":
            # Моника смотрит на Молли, как на дуру
            music Pyro_Flow
            imgf 18226
            mt "Нет!!!"
            mt "Я не собираюсь унижаться перед этой стервой!"
            mt "!!!"
            music Stealth_Groover
            imgd 22674
            m "Я передумала!"
            m "Ты не королева, ты обычная дешевая шлюха!"
            m "Пошла ты!"
            m "!!!"
            # уходит к своей вешалке
            sound highheels_short_walk
            imgf 16131
            w
            return
    music Pyro_Flow
    imgf 18226
    mt "Что?!"
    mt "Эта сучка теперь будет издеваться надо мной?!"
    mt "Я ни за что не признаю, что она королева!!!"
    mt "!!!"
    music Groove2_85
    imgd 18227
    mt "С другой стороны..."
    mt "Я же просто притворюсь."
    mt "Зато смогу после этого снова зарабатывать деньги, а не отдавать их Эшли."
    # Моника недовольно
    imgf 16139
    m "..."
    m "Я признаю, что ты - королева Shiny Hole..."
    # Молли смотрит на Монику и издевательски хихикает
    imgd 18228
    molly "Ну надо же!"
    molly "Ты это сказала!"
    molly "Хи-хи-хи!"
    music Power_Bots_Loop
    imgf 22677
    mt "Как же она меня бесит!"
    mt "!!!" # зло
    music Groove2_85
    # Моника собирается уйти к вешалке
    imgd 22676
    m "Это все?"
    m "Тогда я пошла."
    # Молли перестает хихикать
    imgf 16140
    molly "Стой! Я тебе сказала только первое свое условие..."
    # Моника снова возвращается к ней
    m "..."
    imgd 22673
    molly "Мое второе условие: из нас двоих сучка ТЫ, а не я. И ты это признаешь."
    mt "!!!"
    menu:
        "Сказать Молли, что я сучка.": # corruption
            pass
        "Не делать этого!":
            # Моника смотрит на Молли, как на дуру
            music Pyro_Flow
            imgf 18226
            mt "Нет!!!"
            mt "Я не собираюсь унижаться перед этой стервой!"
            mt "!!!"
            music Stealth_Groover
            imgd 22674
            m "Я передумала!"
            m "Ты наглая, беспринципная сучка! И шлюха!"
            m "Пошла ты!"
            m "!!!"
            # уходит к своей вешалке
            return
    imgd 18229
    molly "Ну?"
    molly "Чего ты молчишь? Я жду."
    # Моника злая
    music Pyro_Flow
    imgf 18225
    mt "!!!"
    mt "Моника, помни о своей цели: тебе нужны деньги."
    mt "Ты не позволишь этой стерве лишить тебя заработка!"
    mt "Моя цель - это вернуть назад мое положение."
    mt "Тогда я разнесу это заведение к чертовой матери!"
    music Groove2_85
    imgd 16137
    m "..."
    m "Я признаю, что из нас двоих сучка не ты... А я..."
    mt "Вернее, не я, а [monica_pub_name]..."
    # Молли начинает злобно смеяться
    sound snd_woman_laugh
    imgf 22675
    molly "Аха-ха!!!"
    molly "!!!"
    # Моника психует
    music Power_Bots_Loop
    imgd 16140
    m "!!!"
    m "Все!"
    m "С меня хватит!"
    m "!!!"
    # разворачивается и отходит от Молли к своей вешалке
    # Молли ей в спину с самодовольным видом
    music Groove2_85
    molly "Ты уже почти прощена... Сучка."
    # Моника злобно поворачивает к ней голову
    imgf 16135
    m "!!!"
    molly "И последнее, третье условие..."
    molly "Во время танца ты разденешься догола."
    # Моника в шоке
    music Power_Bots_Loop
    img 18230 hpunch
    m "!!!"
    m "ЧТОООО?!"
    m "Ты что, совсем охренела?!"
    m "?!?!?!"
    m "Я ни за что не сделаю этого!!!"
    m "Никто не раздевается на сцене полностью!"
    m "Ни Клэр, ни Ты!"
    # Молли равнодушно, не смотря на Монику
    music Groove2_85
    imgd 18231
    molly "Я тебя не прощу, пока ты не выполнишь это условие..."
    menu:
        "Взять стул!!! (увольнение с Shiny Hole)":
            music Power_Bots_Loop
            imgf 22822
            mt "!!!"
            # Моника берет стул и подходит к Молли, замахивается
            imgd 18242
            sound anger2
            w
            imgd 18243
            sound vjuh2
            mt "Получай, тварь!"
            # удар стулом по голове
            sound down10
            img 18244 hpunch
            w
            # Молли хватается за голову
            sound snd_julia_scream1
            imgd 18245
            molly "ААААА!!!"
            molly "СУЧКА!!!"
            # Моника снова замахивается и снова ударяет
            sound vjuh2
            imgf 18246
            sound anger2
            mt "Мерзкая дрянь!!!"
            sound down10
            img 18247 hpunch
            mt "!!!"
            # Молли падает на пол и лежит там беззвучно
            sound snd_bodyfall
            imgd 18248
            w
            imgf 18249
            mt "К черту эту грязную дыру вместе со всеми жалкими неудачниками!"
            mt "!!!"
            # уходит
            sound highheels_short_walk
            imgd 18250
            w
            return
        "Не делать этого.":
            # Моника смотрит зло на Молли
            music Pyro_Flow
            imgf 18226
            mt "Нет!!!"
            mt "Не хочу, чтобы меня уволили из-за этой сучки!"
            pass
    imgd 22676
    m "Я не собираюсь раздеваться на сцене догола!!!"
    m "!!!"
    imgf 18227
    mt "Пошла эта стерва к черту!!!"
    mt "Ненавижу ее!!!"
    mt "!!!"
    return

label gallery_31142:
    # Моника в костюме для стриптиза, с жилетом
    # Моника приходит в подсобку, там сидит клиент, который ей давал 20-ку чаевых, если садилась к нему на колени
    # Джо, как и в прошлый раз, стоит в стороне и хитро улыбается
    fadeblack 2.0
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 31076
    w
    imgf 31078
    w
#    music Power_Bots_Loop
    imgd 30478
    mt "Очередной жалкий неудачник!"
    mt "Ненавижу их всех!"
    mt "!!!"
    if corruption_places.has_key("pubCustomer9_serve1_Corruption") != False and corruption_places["pubCustomer9_serve1_Corruption"] > 0:
        # если этот клиент давал ей 20-ку чаевых
        $ notif(t_("Клиент платил Монике щедрые чаевые."))
        #
        imgf 31077
        w
        imgd 30482
        mt "Я помню его..."
        mt "Этот неудачник хотя бы не такой жадный, как остальные..."

    # клиент сидит с самодовольной мордой
    fadeblack 1.5
    music Loved_Up
    imgf 31079
    customer9 "А вот и моя девочка пришла..."
    m "..."
    customer9 "Девочка себя сейчас будет вести хорошо и станцует для меня."
    # Моника зло на него смотрит
    imgd 31080
    m "..."
    customer9 "Ну? Чего ты ждешь?"
    customer9 "Можешь начинать."
    menu:
        "Начать танцевать.":
            pass
    # Моника залезает на стол и начинает танцевать
    # танцует, раздевается
    fadeblack 2.0
    music Road_Trip
    imgfl 31081
    w
    imgd 31082
    w
    imgf 31083
    w
    imgd 31084
    customer9 "Хорошая девочка..."
    imgf 31085
    w
    imgd 31086
    w
    imgf 23330
    w
    imgd 23331
    w
    imgf 31087
    w
    imgd 31088
    customer9 "Ты мне нравишься больше, чем та рыжая..."
    imgd 31089
    w
    imgf 31090
    w
    imgd 31091
    w
    imgd 31092
    customer9 "Она мне уже надоела..."
    imgf 31093
    w
    imgd 31094
    w
    imgf 31095
    customer9 "Снимай с себя все, покажи, что ты там прячешь от меня."
    imgd 31096
    w
    imgd 31097
    customer9 "Вот так. Молодец."
    imgf 31098
    w
    imgd 31099
    w
    imgf 31100
    customer9 "А теперь раздвинь ножки и нагнись."
    imgd 31101
    w
    imgf 31102
    customer9 "Нагнись ниже..."
    imgd 31103
    w
    sound vjuh3
    imgf 31104
    w
    imgd 31105
    customer9 "Я хочу рассмотреть тебя всю."
    imgd 31106
    w
    imgf 31107
    w
    imgd 31108
    w
    imgd 31109
    customer9 "Еще ниже..."
    # расстегивает штаны и сидит, подрачивая
    # Джо тем временем стоит в сторонке и снова теребит свой член под фартуком
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 31110
    w
    imgf 31111
    w
#    sound vjuh2
    sound Jump1
    imgd 31112
    joe "..."
    # Моника смотрит на расстегнутые штаны клиента
    music Groove2_85
    img 31113 vpunch
    mt "!!!"
    mt "Надеюсь, мне не придется прикасаться своей..."
    mt "Своей голой попой к нему!"
    mt "!!!"
    music Loved_Up
    imgd 31110
    customer9 "Даа..."
    customer9 "Какая хорошая девочка!"
    # клиент убирает руку со своего члена
    imgf 31114
    customer9 "Смотри, какой он твердый."
    customer9 "Теперь сними с себя туфли..."
    customer9 "Он очень хочет, чтобы ты потрогала его своими ножками."
    # Моника удивленно смотрит на него
    music Groove2_85
    imgd 31115
    m "Снять туфли?"
    mt "И что сделать?!"
    mt "Потрогать его моими ножками?! #его - it"
    mt "Фу!!! Что за извращенец?!"
    mt "?!?!?!"
    customer9 "Да..."
    m "Но..."
    imgf 31116
    joe "[monica_pub_name], не задавай вопросов клиенту!"
    joe "Делай, что тебе говорят!"
    # Моника зло смотрит на Джо
    music Power_Bots_Loop
    imgd 30526
    mt "!!!"
    music Groove2_85
    imgf 31117
    customer9 "Ну же..."
    # смотрит на клиента, как на идиота
    imgd 31118
    m "Не в правилах бара прикасаться к клиенту."
    m "Вы можете только смотреть на меня..."
    imgf 31119
    joe "[monica_pub_name]!"
    joe "Ты опять за свое?"
    music Hidden_Agenda
    joe "Клиент не будет к тебе прикасаться."
    joe "Ты сама его будешь трогать." # хитро улыбается
    music Groove2_85
    imgd 31120
    customer9 "Да, моя девочка, давай..."
    customer9 "Я щедро заплатил хорошей девочке, чтобы она потрогала меня своими ножками..."
    m "???" # сморит на Джо
    # Джо утвердительно кивает головой
    imgd 31121
    joe "Да-да, [monica_pub_name]..."
    joe "Очень щедро!"
    m "..."
#    $ menu_corruption = [monicaPrivate2FootjobCorruption]
    menu:
        "Потрогать своей ногой член клиента.": # corruption
            pass
        "Фуу!!! Я не буду делать этого!":
            label gallery_31125:
            music Pyro_Flow
            imgf 31122
            m "Я не собираюсь прикасаться к нему!"
            m "Тем более, своей ножкой!"
            music Groove2_85
            joe "[monica_pub_name], прекрати спорить!"
            joe "Клиент уже заплатил деньги!"
            joe "Делай, что тебе говорят!"
            # Моника поворачивается к клиенту
            imgd 31123
            m "Хочешь, чтобы я прикоснулась к тебе?!"
            customer9 "Да, моя девочка..."
            customer9 "Сделай это..."
            # Моника встает перед диванов, на котором сидит, развалившись клиент
            # и прямо в туфле ставит ногу на его член, припечатывая его каблуком
            fadeblack
            sound highheels_short_walk
            pause 1.5
            music Stealth_Groover
            img 31124 hpunch
            sound scream_steve
            customer9 "АААААА!!!"
            imgf 31125
            customer9 "Что ты делаешь, сучка?!"
            customer9 "АААААА!!!"
            joe "[monica_pub_name]!!!"
            # Моника игнорит Джо и говорит клиенту
            imgd 31126
            m "Теперь ты доволен?!"
            imgf 31127
            customer9 "Да-да!"
            customer9 "Убери! Убери ногу!!!"
            m "!!!"
            music Power_Bots_Loop
            imgd 31128
            joe "Ты не получишь ни цента!"
            # Моника убирает ногу
            music Stealth_Groover
            img 31129 vpunch
            m "Да пошел ты, Джо!"
            m "Ничтожество!"
            m "!!!"
            fadeblack
            sound snd_fabric1
            pause 1.5
            music Stealth_Groover
            imgfl 31130
            sound highheels_short_walk
            w
            # Моника гордо уходит
            return
    # Моника медлит
    music Pyro_Flow
    imgf 30522
    mt "Долбанный извращенец!"
    mt "Черт!"
    mt "!!!"
    mt "Если я сейчас откажусь, никчемный Джо не отдаст мне мои 400 долларов!"
    mt "Что же делать, Моника?"
    mt "..."
    music Groove2_85
    imgd 31131
    mt "С другой стороны, он ведь просит потрогать его ногой..."
    mt "А это не так уж и мерзко... Если сравнивать с тем, чего хотят остальные извращенцы..."
    mt "..."
    # Моника садится на столик напротив клиента и снимает туфли
    imgf 31123
    customer9 "Да, детка..."
    customer9 "Какие у тебя красивые ножки..."
    customer9 "Потрогай меня скорее!"
    mt "..."
    # Моника, также сидя на столе, протягивает ногу к клиенту и прикасается к его члену своей ногой
    fadeblack
    sound snd_fabric1
    pause 2.0
    music stop
    music2 Loved_Up
    imgfl 31132
    w
    imgf 31133
    w
    imgd 31134
    w
    sound drkanje5
    imgd 31135
    customer9 "Ооооо!!!"
    imgf 31136
    customer9 "А теперь вторую ножку!"
    customer9 "Приласкай его обеими ножками!"
    imgd 31137
    mt "Он что, хочет, чтобя я его удовлетворила своими ступнями?!"
    mt "Серьезно?!"
    mt "?!"
    mt "Неужели ТАКОЕ может кому-то нравиться?!"
    mt "?!?!?!"
    # смотрит вопросительно на Джо
    imgf 31138
    joe "Делай..."
    # Моника протягивает к клиенту вторую ногу и зажимает его член между своими ступнями

    music2 stop
    fadeblack 2.0
    music2 Loved_Up
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,3))*2.4) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
    scene black
    image videov_Monica_Private_Visitor9_Footjob1_1 = Movie(play="video/v_Monica_Private_Visitor9_Footjob1_1.mkv", fps=25)
    show videov_Monica_Private_Visitor9_Footjob1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 31139
    w
    imgf 31140
    customer9 "Даааа!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,3))*2.4) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
    scene black
    image videov_Monica_Private_Visitor9_Footjob1_2 = Movie(play="video/v_Monica_Private_Visitor9_Footjob1_2.mkv", fps=25)
    show videov_Monica_Private_Visitor9_Footjob1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 31141
    w
    imgf 31142
    customer9 "Как же охренительно хорошо!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,3))*2.4) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
    scene black
    image videov_Monica_Private_Visitor9_Footjob1_3= Movie(play="video/v_Monica_Private_Visitor9_Footjob1_3.mkv", fps=25)
    show videov_Monica_Private_Visitor9_Footjob1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    customer9 "Двигай ножками быстрее, детка!"
    music2 Loved_up2

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,3))*2.4) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
    scene black
    image videov_Monica_Private_Visitor9_Footjob1_4 = Movie(play="video/v_Monica_Private_Visitor9_Footjob1_4.mkv", fps=25)
    show videov_Monica_Private_Visitor9_Footjob1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,3))*2.4) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
    scene black
    image videov_Monica_Private_Visitor9_Footjob1_5 = Movie(play="video/v_Monica_Private_Visitor9_Footjob1_5.mkv", fps=25)
    show videov_Monica_Private_Visitor9_Footjob1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,3))*2.4) + " loop 0.0>Sounds/v_Monica_Private_Visitor9_Footjob1_1.ogg"
    scene black
    image videov_Monica_Private_Visitor9_Footjob1_6 = Movie(play="video/v_Monica_Private_Visitor9_Footjob1_6.mkv", fps=25)
    show videov_Monica_Private_Visitor9_Footjob1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 31146
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    customer9 "О, дааа!!!"
    img 31147
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    customer9 "АААААА!!!"
    imgf 31148
    w
    # клиент кончает на ступни Моники
    imgd 31149
    mt "Фууу!!!"
    mt "!!!"
    # Джо не кончает, а продолжает трогать себя под фартуком
#    img 31149
    joe "Ммммммм..."
    # Моника зло на него смотрит
    music2 stop
    music Power_Bots_Loop
    imgf 30526
    mt "Сволочь!!!"
    mt "!!!"
    # смена кадра
    # клиент одетый, Моника все еще голая, стоит и прикрывается
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 31150
    w
    imgf 31151
    customer9 "Джо, заплати девочке всю сумму."
    joe "Да-да. Обязательно."
    imgd 31152
    customer9 "Она хорошо поработала. Я доволен."
    customer9 "Обязательно приду к тебе на приват еще раз."
    sound man_steps
    imgf 31153
    w
    # подмигивает, хлопает ее по попе и уходит
    # Моника остается с Джо вдвоем
    # она протягивает к нему руку
    label gallery_18351:
    fadeblack 1.5
    music Groove2_85
    imgfl 18334
    m "Джо, давай мне мои 400 долларов и я пойду!"
    imgf 18335
    joe "Подожди, [monica_pub_name]. Не торопись."
    imgd 18336
    m "В смысле?"
    m "Джо, я отработала. Отдавай мне мои деньги!"
    music Hidden_Agenda
    imgf 18337
    joe "Ты же хочешь получить 400 баксов, [monica_pub_name]?"
    music Groove2_85
    imgd 18338
    m "Да, ты мне сам сказал, то клиент заплатил $ 400."
    music Hidden_Agenda
    imgf 18339
    joe "На самом деле клиент заплатил 300 баксов."
    joe "Если ты хочешь получить не 300, а 400, то..."
    # задирает фартук и достает стояк из штанов
    imgd 18340
    joe "Сделай также, как на прошлом привате."

    # если терлась киской об клиента на прошлом привате
    $ notif(t_("Моника терлась своей киской о член клиента."))
    #
    imgf 18341
    joe "Я также, как тот клиент, лягу на стол..."
    music Power_Bots_Loop
    img 18342 hpunch
    m "ЧТОООО?!"
    m "?!?!?!"
    m "Джо! Ты охренел?!"
    m "!!!"
    m "!!!!!!"
    music Groove2_85
    imgf 18343
    joe "[monica_pub_name], ну чего ты так переживаешь?"
    joe "Ты немного потрешься об меня своей киской, а я отдам тебе 400 баксов."
    # показывает ей купюры в своей руке
    joe "И все остануться довольны."
    joe "Только Эшли ничего не должна знать!"
    # Моника смотрит на него зло
    imgd 18344
    mt "Сволочь!!!"
    mt "!!!"
#    $ menu_corruption = [monicaPrivate2JoeTeasingCorruption]
    menu:
        "Потереться о Джо. (in Extra version) (disabled)" if game.extra != True:
            return
        "Потереться о Джо." if game.extra == True: # corruption
            if game.extra == True:

                music Pyro_Flow
                imgf 18345
                mt "Грязное животное!"
                mt "Ненавижу его!"
                mt "!!!"
                mt "Но мне нужны эти деньги!"
                mt "Что же делать?!"
                mt "???"
                # Моника в сомнении
                music Hidden_Agenda
                imgd 18346
                joe "Ну что, [monica_pub_name], пошли на стол?"
                joe "Нам надо поторопиться, пока Эшли сюда не пришла."
                # Моника подозрительно
                music Groove2_85
                imgf 18347
                m "Если я сейчас сделаю это, ты мне отдашь всю сумму?"
                m "Или придумаешь еще какой-нибудь предлог, чтобы не платить мне?!"
                joe "[monica_pub_name], я заплачу тебе 400 баксов и ни центом меньше."
                joe "Для этого тебе нужно всего лишь немного потереться своей киской о мой член."
                # Джо подходит к столу и ложится, спустив штаны
                fadeblack
                sound snd_fabric1
                pause 2.0
                music Groove2_85
                imgfl 18348
                w
                imgf 18349
                mt "Дьявол!"
                mt "!!!"
                mt "Гребанный Джо!!!"
                # Моника пристраивается над Джо, чтобы можно было тереться об его член
                music2 stop
                music Loved_Up
                imgd 18350
                w
                imgd 18351
                w
                sound highheels_short_walk
                imgf 18352
                w
                imgd 18353
                w
                fadeblack 1.5
                music2 Loved_Up

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.3, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.33333333) + " loop 0.0>Sounds/v_Monica_Private_Bartender_Teasing1_1.ogg"
                scene black
                image videov_Monica_Private_Bartender_Teasing1_1 = Movie(play="video/v_Monica_Private_Bartender_Teasing1_1.mkv", fps=25)
                show videov_Monica_Private_Bartender_Teasing1_1
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                imgfl 18354
                sound Jump1
                joe "Ооооо!!! [monica_pub_name]!!!"
                imgf 18355
                joe "Какая ты горячая!!!"
                # кладет ладони ей на попу
                # Моника перестает двигаться и рычит на него
                img 18356 vpunch
                m "Не прикасайся ко мне!!!"
                m "!!!"
                # Джо убирает руки
                imgd 18357
                joe "Хорошо, хорошо!"
                joe "Продолжай, не останавливайся..."
                imgd 18358
                mt "Ублюдок!"
                mt "!!!"

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.3, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.33333333) + " loop 0.0>Sounds/v_Monica_Private_Bartender_Teasing1_1.ogg"
                scene black
                image videov_Monica_Private_Bartender_Teasing1_2 = Movie(play="video/v_Monica_Private_Bartender_Teasing1_2.mkv", fps=25)
                show videov_Monica_Private_Bartender_Teasing1_2
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                # Моника продолжает тереться
                imgf 31154
                w
                imgd 31155
                joe "Даааа..."
                imgd 31156
                w
                music2 Loved_up2
                imgf 31157
                joe "Аааа..."
                joe "Еще..."
#                imgd 31158
#                w
#                imgf 31159

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.3, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.33333333) + " loop 0.0>Sounds/v_Monica_Private_Bartender_Teasing1_1.ogg"
                scene black
                image videov_Monica_Private_Bartender_Teasing1_3 = Movie(play="video/v_Monica_Private_Bartender_Teasing1_3.mkv", fps=25)
                show videov_Monica_Private_Bartender_Teasing1_3
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                # Моника со злым лицом трется о Джо
                imgd 31160
                joe "Мммммм..."
                joe "Оооооо..."

                img black_screen
                with diss
                stop music
                $ renpy.music.set_volume(0.5, 0.5, channel="music")
                $ renpy.music.set_volume(0.3, 0.5, channel="music2")
                play music "<from " + str(float(rand(1,4))*1.33333333) + " loop 0.0>Sounds/v_Monica_Private_Bartender_Teasing1_1.ogg"
                scene black
                image videov_Monica_Private_Bartender_Teasing1_4 = Movie(play="video/v_Monica_Private_Bartender_Teasing1_4.mkv", fps=25)
                show videov_Monica_Private_Bartender_Teasing1_4
                with fade
                wclean
                stop music
                $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                $ renpy.music.set_volume(1.0, 0.5, channel="music")

                imgd 31162
                joe "Дааааа..."
                menu:
                    "Кончить на попу Моники.":
                        img 31163
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        w
                        img 31164
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        sound man_moan1
                        joe "Оооох..."
                        imgd 31165
                        joe "Ммммммм..."
                        # Моника зло на него смотрит
                        imgf 31166
                        mt "Твоя жена тебя не видит!"
                        mt "Мерзавец!"
                        mt "!!!"
                        pass
                    # не может кончить внутрь! "кончить на киску."
                    "Кончить на киску Моники.":
                        img 31167
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        w
                        img 31161
                        sound bulk1
                        show screen photoshot_screen()
                        with hpunch
                        pause 0.7
                        hide screen photoshot_screen
                        sound man_moan1
                        joe "Оооох..."
                        imgd 31167
                        joe "Ммммммм..."
                        # Моника зло на него смотрит
                        imgf 31166
                        mt "Твоя жена тебя не видит!"
                        mt "Мерзавец!"
                        mt "!!!"
                        pass
                # смена кадра
                # Джо стоит с довольной улыбкой
                music2 stop
                fadeblack
                sound snd_fabric1
                pause 2.0
                music Groove2_85
                imgfl 18359
                joe "[monica_pub_name], вот твои 400 баксов."
#                $ add_money(400.0)
#                $ monica_strip_tips_today += 400.0
                joe "И не забудь отдать Эшли процент."
                # Джо уходит, Моника злая
                sound man_steps
                imgf 30575
                w
                music Power_Bots_Loop
                imgd 30577
                mt "Грязное похотливое животное!"
                mt "Прямо за спиной у своей жены!"
                mt "Пока она работает!!!"
                mt "Мерзкий подонок!!!"
                mt "!!!"
                fadeblack 2.0
            return
        "Я оторву ему яйца!!!":
            pass
    # Монику бомбит
    label gallery_18370:
    music Power_Bots_Loop
    img 18360 hpunch
    m "А ну-ка быстро отдал мне МОИ деньги!!!"
    imgd 18361
    m "!!!"
    joe "[monica_pub_name]..."
    imgd 18362
    m "Заткнись!"
    m "Отдай мне 400 долларов!!!"
    # Моника подбегает к Джо и пытается отобрать у него деньги
    music Groove2_85
    imgf 18363
    joe "[monica_pub_name], тихо!"
    # Джо отходит от Моники, она за ним, он снова отходит
    joe "Нас могут услышать!"
    # Моника снова подходит к нему
    music Turbo_Tornado
    imgd 18364
    m "!!!"
    menu:
        "Отпинать этого козла!":
            pass
    # Джо отворачивается и снова пытается уйти от Моники, она дает ему пендель под зад
    sound snd_kick_fred1
    img 18365 hpunch
    m "Да пошел ты, козел!"
    # Джо начинает убегать от Моники по подсобке, она
    imgd 18366
    joe "АЙ!!!"
    joe "Ты что делаешь?!"
    # он убегает, она его догоняет и периодически попинывает
    sound running
    imgf 18367
    m "Отдай деньги!!!"
    m "!!!"
    imgd 18368
    joe "[monica_pub_name], я тебе могу отдать 300 баксов."
    m "Какие, к черту, 300 баксов?!" # пинок
    sound snd_kick_fred1
    img 18369 hpunch
    joe "АЙ!!!"
    imgd 18370
    m "400, Джо!!!"
    m "И ни центом меньше!!!" # пинок
    # на шум прибегает Эшли
    music Power_Bots_Loop
    imgf 18371
    ashley "[monica_pub_name]! Что здесь происходит?!"
    ashley "Тебя и твоего клиента слышно в зале!"
    imgd 18372
    joe "!!!"
    m "!!!"
    # замечает Джо, в шоке
    music stop
    sound plastinka2
    img 18373 hpunch
    ashley "Джо?"
    ashley "Джо!!!"
    # Джо с Моникой застывают на месте
    # Моника по прежнему голая, прикрывается
    # Джо растерян, пытается оправдаться
    music Hidden_Agenda
    imgf 18374
    joe "А что сразу Джо?!"
    joe "Я, между прочим, работаю!"
    music Groove2_85
    img 18375 vpunch
    ashley "Ты должен быть за барной стойкой, сволочь!"
    ashley "Какого хрена ты здесь делаешь?!"
    imgd 18376
    joe "У [monica_pub_name] был приват с клиентом, а я..."
    joe "Я пришел, чтобы убрать за ними! Вот!"
    # Эшли смотрит на Монику, потом на Джо возмущенно и подозрительно
    imgd 18378
    ashley "С каких это пор ты убираешь после приватов?! А?!"
    imgd 18377
    ashley "Нашел предлог поглазеть на эту шлюху [monica_pub_name] без трусиков?!"
    ashley "?!?!?!"
    imgd 18378
    ashley "Говори, мерзавец!!!"
    # Джо испуганно
    music Hidden_Agenda
    imgf 18379
    joe "На кого?!"
    joe "На нее что-ли?"
    # смотрит на Монику
    imgd 18380
    joe "Эшли, ты знаешь, что я смотрю только на тебя!"
    joe "Мне не интересно смотреть ни на каких шлюх, Эшли!"
    m "!!!"
    joe "Я просто пришел убрать..."
    # шепчет незаметно Монике
    music Groove2_85
    imgf 18381
    joe "Скажи ей, что я только зашел!"
    joe "Я отдам тебе все чаевые! Только скажи ей это!"
    music Power_Bots_Loop
    imgd 18382
    mt "Вот мерзавец!"
    mt "!!!"
    # Моника смотрит на Эшли, та на нее
    music Groove2_85
    imgf 18383
    ashley "[monica_pub_name]!"
    ashley "Скажи мне, он правда только что пришел сюда?"
    ashley "Или он тут уже давно глазеет на то, как ты танцуешь для клиента?!"
    imgd 18384
    ashley "Я знаю, что Джо врет, что не любит смотреть на шлюх!"
    ashley "А значит и на тебя, скорее всего, смотрел!"
    imgd 18385
    m "..."
    menu:
        "Он постоянно сюда приходит и смотрит на приват!":
            pass
        "Он только что пришел.":
            # Моника медлит
            music Groove2_85
            imgf 18386
            mt "Я бы с удовольствием рассказала все Эшли!"
            mt "Но мне нужны эти чертовы 400 долларов!"
            mt "Пусть только попробует не отдать их мне!"
            mt "!!!"
            music Hidden_Agenda
            imgd 18387
            m "Он..."
            m "Он только что зашел сюда."
            m "Сказал, что ему нужно убраться."
            # Эшли скептично
            imgf 18388
            ashley "Хочешь сказать, что он даже не глазел на тебя?"
            imgd 18389
            m "Нет, не глазел..."
            music Loved_Up
            imgf 18390
            joe "Ну! Я же тебе говорю, Эшли, дорогая!"
            joe "Как ты могла такое подумать?!" # оскорбленно
            joe "По-твоему я похож на идиота, чтобы изменять тебе прямо за твоей спиной, пока ты работаешь?!"
            imgd 18391
            ashley "Ладно..."
            ashley "Мне пора идти за барную стойку."
            music Groove2_85
            imgf 18392
            ashley "[monica_pub_name], у тебя ровно минута, чтобы одеться и выйти!"
            ashley "Нечего тут крутить своим голым задом перед Джо!"
            ashley "Во-первых, это мой муж!"
            ashley "А, во-вторых, у него все равно нет денег, чтобы платить такой шлюхе как ты!"
            m "!!!"
            sound man_steps
            imgd 18393
            w
            # Эшли выходит
            # смена кадра, Моника уже одетая требовательно смотрит на Джо
                # рендерить
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 18394
            m "Мне нужны мои 400 долларов!"
            # хитро
            music Hidden_Agenda
            joe "[monica_pub_name], ты слышала Эшли! Про какие деньги ты говоришь?"
            music Power_Bots_Loop
            imgf 18395
            m "Если хоть слово сейчас от тебя услышу - все расскажу твоей жене!"
            m "!!!"
            music Groove2_85
            imgd 18396
            sound vjuh3
            joe "Ладно, [monica_pub_name], вот твои деньги. Только не говори ничего Эшли!"
#            $ add_money(400.0)
#            $ monica_strip_tips_today += 400.0
            joe "И не забудь отдать процент."
            music Power_Bots_Loop
            imgf 18397
            m "Ничтожество!"
            m "!!!"
            # Моника гордо уходит
            return
    # Моника медлит
    label gallery_18411:
    music Pyro_Flow
    imgf 18386
    mt "Мне, конечно, нужны эти чертовы 400 долларов..."
    mt "..."
    mt "Но еще больше мне хочется наказать Джо!"
    mt "Пусть Эшли знаешь, какой ее муж мерзавец!"
    mt "!!!"
    imgd 18387
    m "Он..."
    m "Он уже не первый раз приходит на мой приват с клиентом."
    m "И смотрит танец от начала и до конца..."
    m "И при этом дергает свой стручок!"
    music Power_Bots_Loop
    img 18398 hpunch
    ashley "ЧТОООО?!?!?!" # орет
    joe "Нет, это неправда!!!"
    music Pyro_Flow
    m "А сегодня начал ко мне приставать после того, как ушел клиент!"
    m "И угрожает не заплатить мне деньги за приват!"
    m "!!!"
    joe "Не было такого!!!"
    # Эшли наступает на него, он пятится
    music Turbo_Tornado
    imgf 31168
    joe "Дорогая, она врет!!!"
    imgd 31169
    w
    # Эшли в бешенстве
    sound snd_kick_fred1
    img 31170 vpunch
    ashley "Ах ты козел!!!" # пинок
    joe "АЙ!!!"
    sound running
    imgd 31171
    ashley "Сволочь неблагодарная!!!" # пинок
    ashley "Зачем я только вышла за тебя!"
    sound snd_kick_fred1
    img 31172 vpunch
    ashley "Кобель!!!"
    joe "Да больно же!!!"
    sound snd_kick_fred1
    img 31173 vpunch
    ashley "Мерзавец!!!" # пинок
    joe "АЙ!!!"
    # Джо смывается
    # Эшли стоит руки в боки, смотрит на Монику
    fadeblack
    sound snd_runaway
    pause 2.0
    music Groove2_85
    imgfl 18399
    ashley "Вот козел!"
    ashley "!!!"
    imgf 18400
    m "Он обещал заплатить мне 400 долларов."
    m "Сказал, что взял предоплату за приват с клиента."
    m "..."
    imgd 18401
    ashley "Я заберу у него эти деньги..."
    music Loved_Up
    ashley "Только..."
    # смотрит игриво на Монику
    ashley "Сначала ты мне покажешь твою голеньку попку..."
    music Groove2_85
    imgf 18402
    m "Что?!"
    m "?!"
    music Hidden_Agenda
    imgd 18403
    ashley "Совсем немного, [monica_pub_name]..."
    ashley "Просто повернись ко мне спиной. Мне так нравится на тебя смотреть."
    music Pyro_Flow
    imgd 18404
    mt "Семейка долбанных извращенцев!!!"
    mt "Два придурка!!!"
    mt "!!!"
    mt "Может послать ее к черту?"
    mt "..."
    mt "Но мне нужны эти деньги!"
    m "..."
    menu:
        "Сделать как просит Эшли.":
            pass
        "Уйти отсюда!":
            # Моника медлит
            imgf 18405
            mt "К черту!!!"
            mt "Я не собираюсь терпеть ее грязные приставания!"
            mt "Пусть подавяться своими деньгами!!!"
            mt "!!!"
            imgd 18406
            m "Нет!"
            m "Мне на сегодня достаточно извращенцев!!!"
            m "Как же вы меня все достали!!!"
            m "!!!"
            # уходит
            fadeblack 2.0
            return
    # Моника поворачивается к Эшли спиной
    # та смотрит на ее попу и кладет на нее ладонь
    fadeblack 1.5
    music Loved_Up
    imgfl 18407
    w
    imgf 18408
    w
    imgd 18409
    w
    imgf 18410
    ashley "Мммм, какая упругая попка..."
    mt "!!!"
    ashley "Ради такой попки я отберу у идиота Джо твои деньги."
    imgd 18411
    ashley "Но при одном условии, [monica_pub_name]..."
    ashley "Если он еще раз будет приставать к тебе, ты мне сразу об этом скажешь..."
    m "..."
    imgd 18412
    ashley "Скажешь же?"
    m "Да..."
    # смена кадра
    # Моника стоит одетая в подсобке, заходи Эшли и отдает ей деньги
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 18413
    ashley "Вот твои деньги, [monica_pub_name]."
#    $ add_money(400.0)
#    $ monica_strip_tips_today += 400.0
    ashley "На сегодня все. Можешь идти."
    imgf 23473
    mt "Ненавижу их всех!"
    mt "!!!"
    fadeblack 2.0
    return

label gallery_31177:
    # по возможности использовать имеющиеся арты
    # работа официанткой, обслуживет этого клиента
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14410
    mt "Снова этот грязный извращенец!!!"
    mt "!!!"
    imgf 14394
    m "Что будете заказывать?"
    imgd 14395
    customer9 "Хорошая девочка пришла!"
    customer9 "Я до сих пор не могу забыть твои чудесные ножки, детка!"
    imgf 14398
    m "Я... Я не понимаю, о чем вы?"
    customer9 "О том, как ты мне ласкала меня, сняв свои туфли."
    customer9 "Обязательно повторим это еще раз!"
    customer9 "А пока пойдем ко мне на колени!"
    music Pyro_Flow
    imgd 14403
    mt "Черт!!!"
    mt "Он понял, что это я была на привате!!!"
    mt "!!!"
    music Groove2_85
    imgd 14406
    customer9 "Хорошая девочка сейчас посидит у меня на коленях..."
    customer9 "И получит за это хорошую денежку..."
    m "..."
    menu:
        "Сделать как просит клиент.":
            imgf 14482
            mt "Этот неудачник не такой жадный, как остальные..."
            mt "Его чаевые не будут лишними."
            # садится к нему на колени
            fadeblack 1.5
            music Loved_Up
            imgfl 14484
            customer9 "Умничка... Вот тебе денежка..."
#            sound vjuh3
            imgf 14485
#            $ add_money(20.0)
#            $ add_tips(20.0)
            w
            # он засовывает ей под чулок 20 долларов
            imgd 14486
            customer9 "Хочешь я тебе дам еще денег?"
            customer9 "Приспусти незаметно трусики и посиди еще немного."
            customer9 "Ты же знаешь, детка, что я щедрый клиент."
            m "..."
#            $ menu_corruption = [monicaCustomer9AfterPrivateTakeOffPantiesCorruption]
            menu:
                "Приспустить трусики.":
                    music Groove2_85
                    imgf 14483
                    mt "Это делает не Моника Бакфетт, а [monica_pub_name]."
                    mt "Зато у меня в кармане станет больше денег..."

                    # Моника засовывает пуки под юбку, чтобы снять трусики
                    # Моника сидит на коленях у клиента, на ногах у нее видны приспущенные трусики
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 31175
                    w
                    fadeblack 2.0
                    music Loved_Up
                    imgf 31176
                    customer9 "Хорошая девочка..."
#                    sound vjuh3
                    imgd 31177
                    #$ add_money(20.0)
#                    $ add_tips(20.0)
                    w
                    # он засовывает ей под чулок еще 20 долларов
                    imgf 14484
                    customer9 "Я доволен."
                    music Groove2_85
                    imgd 14486
                    m "Что вам принести?"
                    customer9 "Принеси мне пива и гамбургер!"
                    # Моника встает (продолжение обслуживания)
                    pass
                "С меня хватит!":
                    # Моника медлит
                    music Power_Bots_Loop
                    imgf 14483
                    mt "Хватит!"
                    mt "Меня уже тошнит от всех этих жалких извращенцев!"
                    mt "!!!"
                    m "Нет!"
                    m "Я не буду этого делать!"
                    # Моника встает
                    fadeblack 1.5
                    music Groove2_85
                    imgfl 14411
                    m "Что вам принести?"
                    customer9 "Принеси мне пива и гамбургер!"
                    pass
            pass
        "Нет! Обойдется!":
            # Моника медлит
            music Pyro_Flow
            imgf 14410
            mt "Я не хочу, чтобы он прикасался ко мне!!!"
            mt "Меня уже тошнит от всех этих жалких извращенцев!"
            mt "!!!"
            imgd 14404
            m "Нет!"
            m "Я не буду этого делать!"
            m "Вы меня с кем-то путаете!"
            m "!!!"
            music Groove2_85
            imgf 14405
            customer9 "Да? Хм... Может быть..."
            m "Что вам принести?"
            customer9 "Принеси мне пива и гамбургер!"
            pass
    # Моника уходит и возвращается с пивом
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    sound snd_beer_table
    imgfl 31174
    m "Пожалуйста, ваш заказ..."
    mt "Мерзкий жалкий неудачник!"
    customer9 "Спасибо, детка..."
    customer9 "Скоро увидимся в привате!" # подмигивает
    mt "!!!"
    music2 stop
    return

label gallery_31412:
    # банкир, Моника и Эшли, Клэр нет
    # банкир на диване, Эшли в сторонке у стены
    # Моника стоит перед столиком, она в маске и в жилете
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 31338
    w
    imgf 31339
    w
    imgd 31340
    mt "Клэр все-таки отказалась..."
    mt "Я до последнего момента надеялась, что она передумает."
    mt "..."
    mt "Эта извращенка Эшли теперь повесит плакат и слушать ничего не станет."
    mt "Мне нужно будет как-то отговорить ее."
    imgf 31341
    ashley "Наконец-то, пришла!"
    ashley "А почему ты в жилете?"
    ashley "Могла бы и снять его сразу для Мистера Беркельбауха!"
    mt "!!!"
    ashley "Чего ты так смотришь? Снимай жилет!"
    menu:
        "Снять жилет.":
            pass
        "Не делать этого! (увольнение из паба)":
            music Power_Bots_Loop
            imgd 31342
            m "Я не собираюсь раздеваться перед ним!"
            m "Достаточно было прошлого раза!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            sound highheels_short_walk
            imgf 31343
            w
            return
    music Power_Bots_Loop
    imgd 31344
    mt "Чертова изращенка Эшли со своим гребаным банкиром!"
    mt "Ненавижу!!"
    # Моника снимает жилет, стоит и смотрит на банкира
    music Groove2_85
    imgf 31345
    w
    sound vjuh2
    img 31346
    w
    imgf 31347
    banker "Эй, крошки."
    banker "Вы чего там застыли?"
    banker "Лезьте на стол и показывайте мне свои попки."
    banker "Не заставляйте меня долго ждать, я этого не люблю."
    imgd 31348
    mt "Какой же он мерзкий тип!"
    mt "!!!"
    menu:
        "Залезть на стол.":
            pass
        "Не делать этого! (увольнение из паба)":
            music Power_Bots_Loop
            imgd 31342
            m "Я не собираюсь раздеваться перед ним!"
            m "Достаточно было прошлого раза!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            sound highheels_short_walk
            imgf 31343
            w
            return
    # Моника встает на стол
    imgd 31349
    w
    sound highheels_short_walk
    imgf 31350
    w
    imgd 31351
    banker "Эшли..."
    ashley "Да, Мистер Беркельбаух?"
    banker "А где остальные крошки?"
    # заходит манерная Молли
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 31352
    w
    imgf 31353
    ashley "Молли, встань рядом с [monica_pub_name]."
    # Молли недовольно смотрит на Монику
    imgd 31354
    molly "Почему я должна стоять рядом с этой шлюхой?!"
    molly "Пусть она слезет со стола, тогда я туда встану!"
    molly "Я не хочу даже приближаться к ней!"
    # Моника возмущенно смотрит на нее
    music Power_Bots_Loop
    imgd 31355
    mt "Вот сучка!"
    mt "!!!"
    imgd 31356
    m "Да пошла ты!"
    m "Из нас двоих есть только одна шлюха. Я ее вижу сейчас перед собой!"
    music Groove2_85
    ashley "[monica_pub_name]!"
    ashley "Ты сама сейчас провоцируешь Молли!"
    ashley "Стой и помалкивай!"
    ashley "Не надо мне тут снова устраивать вашу битву сучек!"
    ashley "Ты хочешь снова извиняться перед ней?!"
    # Молли самодовольно ухмыляется и смотрит на Монику
    imgd 31357
    mt "!!!"
    molly "Ну так уж и быть, я постою с тобой рядом..."
    molly "Потерплю тебя..."
    # Молли игриво смотрит на банкира
    music Loved_Up
    imgf 31358
    molly "Но только ради Мистера Беркельбауха." # говорит, снимая трусики, поворачиваясь к нему попой, соблазнительно!!!
    imgd 31359
    w
    imgf 31360
    w
    imgd 31363
    banker "Да, крошка. Сделай это для меня."
    music Power_Bots_Loop
    imgf 31361
    mt "Вот проститутка!"
    mt "Лицемерная дрянь!"
    mt "Ненавижу ее!"
    # Молли встает на стол рядом с Моникой
    music Groove2_85
    imgd 31362
    sound highheels_short_walk
    w
    imgf 31364
    banker "Отлично..."
    banker "Какие аппетитные девочки, какие попки."
    banker "Ммм..."
    # Молли шипит на Монику
    music Turbo_Tornado
    imgd 31365
    molly "Подвинь свою жирную задницу!"
    molly "Ты мне мешаешь!"
    # толкает Монику
    sound Jump1
    imgd 31366
    m "Что?!"
    m "Ты свою задницу видела?!"
    m "Сама подвинься!!"
    # Моника толкает Молли попой в ответ
    imgf 31367
    w
    sound Jump1
    imgd 31368
    w
    imgf 31369
    banker "Хе-хе..."
    banker "Какие темпераментные крошки..."
    music Groove2_85
    banker "Будет еще лучше, если вы снимете свои маски."
    banker "Так сказать, для более объективной и встесторонней оценки."
    imgd 31370
    banker "И ты..." # указывая на Монику
    banker "Почему я до сих пор не вижу твою голую попку?"
    # Молли снимает свою маску, а Моника не торопится снимать ни трусики, ни маску и зло смотрит на Эшли
    sound snd_fabric1
    fadeblack 1.5
    music Groove2_85
    imgfl 31371
    w
    imgf 31372
    mt "!!!"
    imgd 31373
    ashley "[monica_pub_name], чего ты ждешь?"
    ashley "Делай, как говорит Мистер Беркельбаух!"
    mt "!!!"
    menu:
        "Снять маску и трусики.":
            pass
        "Не делать этого! (увольнение из паба)":
            music Power_Bots_Loop
            imgf 31374
            m "Я не собираюсь снимать маску!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            fadeblack
            sound snd_fabric1
            pause 1.5
            music Power_Bots_Loop
            imgf 31375
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return
    imgf 31372
    mt "Этот мерзкий клерк уже видел меня без одежды и без маски."
    mt "Черт!"
    mt "!!!"
    # Моника снимает маску, банкир рассматривает ее и Молли
    fadeblack
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    imgfl 31376
    w
    imgf 31377
    banker "Так, хорошо..."
    banker "..."
    banker "Эшли..."
    music Groove2_85
    imgd 31378
    ashley "Да, Мистер Беркельбаух?"
    banker "Ты помнишь условие нашей сегодняшней встречи?"
    ashley "Конечно, Мистер Беркельбаух."
    banker "И какое же это условие?"
    # Эшли нервничает
    imgf 31379
    ashley "Условие такое, что здесь будут присутствовать все девочки бара..."
    banker "Ты не выполнила это условие, Эшли..."
    banker "Я не вижу здесь третьей девочки."
    banker "Где она?"
    # Эшли начинет оправдываться
    imgd 31380
    ashley "Мистер Беркельбаух, дело в том, что..."
    ashley "В общем, с Клэр очень сложно договориться."
    ashley "Она не ходит на приватные танцы с клиентами и..."
    # банкир ее перебивет
    imgf 31381
    banker "Эшли, ты разговариваешь со мной с неправильной финансовой позиции..."
    ashley "Я? С неправильной чего?"
    banker "С неправильно финансовой позиции, Эшли."
    banker "Ты стоишь там, а должна стоять здесь." # указывает на стол рядом с девочками
    ashley "Но, Мистер Беркельбаух..."
    banker "Эшли, займи правильную финансовую позицию и объясни мне, почему нет третьей девочки."
    # Эшли лезет к Монике и Молли на стол и одновременно с этим продолжает оправдываться перед банкиром
    imgd 31384
    sound man_steps
    ashley "Я пыталась поговорить с Клэр, объяснить ей ситуацию..."
    ashley "Что у нас сегодня обязательное условие..."
    ashley "Но она все равно отказалась..."
    ashley "Бесполезно ее уговаривать, Мистер Беркельбаух..."
    # Эшли уже стоит на столе рядом с Молли и Моникой (параллельно показываем красивые виды на голые попы с разных ракурсов)
    imgf 31385
    ashley "Я правда пыталась сделать это. Я вас не обманываю."
    banker "Эшли, ты знаешь, что будет с твоим заведением..."
    banker "Если ты не выполнишь нашу договоренность."
    imgd 31386
    ashley "Мистер Беркельбаух, я уверена, что мы с вами сможем договориться!"
    banker "Нет, Эшли. Я не готов подписывать документы для заведения..."
    banker "Которое не может предоставить мне полную прозрачность своей деятельности."
    imgd 31387
    banker "К тому же, кто сможет показать мне эту прозрачность, как не владелица этого заведения?"
    banker "Я хочу увидеть и твою попку."
    banker "Давай, Эшли, поднимай свою юбку!"
    # Эшли продолжает его уговаривать, стягивая трусики
    sound snd_fabric1
    fadeblack 1.5
#    sound vjuh2
    music Groove2_85
    imgf 31389
    w
    imgd 31388
    ashley "Но Мистер Беркельбаух, здесь итак уже полная прозрачность!"
    imgf 31390
    banker "Нет, Эшли."
    banker "Я должен оценить деятельность твоего заведения встесторонне."
    banker "А ты препятствуешь этому."
    banker "Боюсь, у нас с тобой не получится достигнуть договоренности..."
    ashley "Но Мистер Беркельбаух..."
    # Эшли прерывается на полуслове из-за звука открывающейся двери
    # испуганно оглядывается
    # в дверях стоит недовольная Клэр, в руках ее хлыст для извращенцев
    # Эшли радостно
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Stealth_Groover
    imgfl 31393
    w
    imgd 31391
    w
    imgd 31394
    w
    imgd 31392
    ashley "Клэр!"
    mt "Она пришла!"
    mt "Она сделала это!"
    mt "!!!"
    # Клэр подходит к банкиру, тыкает ему в грудь хлыстом
    sound highheels_short_walk
    imgf 31395
    w
    sound vjuh4
    imgd 31396
    clare "Это тот самый извращенец, который захотел всех девочек Shiny Hole сразу?"
    # банкир смотрит на хлыст, напряженно молчит
    imgf 31397
    banker "..."
    # Клэр хлыстом приподнимает его лицо за подбородок (как делала с Эдвардсом)
    sound Jump2
    img 31398 vpunch
    clare "И этот мелкий банковский клерк смеет командовать здесь?"
    banker "..."
    # поворачивает лицо хлыстом сначала в одну сторону
    sound Jump2
    img 31399 vpunch
    w
    sound vjuh4
    img 31400 vpunch
    clare "Да... Деньги для такого как ты - единственный способ получить женское внимание."
    banker "..."
    # потом в другую сторону
    sound vjuh4
    img 31401 vpunch
    clare "Мне тебя даже жалко, клерк."
    banker "..."
    # Клэр встает на стол к остальным, снимает трусики
    # смотрит на Монику
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    imgfl 31402
    w
    sound snd_fabric1
    imgf 31403
    w
    music Groove2_85
    imgd 31404
    sound highheels_short_walk
    w
    imgf 31405
    w
    imgd 31406
    clare "..."
    m "..."
    # снимает маску
    # Эшли стоит с голой попой вместе с остальными, довольная, что Клэр пришла
    # банкир в шоке и самодовольно смотрит на четыре голые попы перед ними
    # затемнение, смена кадра - банкир уже расстегнул штаны и достал свой стояк
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 31407
    w
    imgf 31412
    w
    imgd 31408
    banker "Ну вот."
    banker "Совсем другое дело."
    banker "Теперь ничто не препятствует встесторонней и объективной оценке работы твоего заведения, Эшли."
    imgf 31412
    ashley "Да, Мистер Беркельбаух."
    ashley "Я же вам говорила, что готова предоставить все необходимое для этого."
    # начинает дрочить
    imgf 31409
    w
    sound drkanje5
    imgd 31410
    w
    imgd 31409
    w
    sound drkanje5
    imgd 31410
    w
    imgd 31409
    w
    sound drkanje5
    imgd 31410
    w
    imgd 31409
    w
    sound drkanje5
    imgd 31410
    w
    imgd 31411
    banker "Да..."
    banker "Все девочки Shiny Hole собрались для меня..."
    imgd 31412
    banker "А это значит, что ты мне предоставила полную прозрачность своей деятельности, Эшли."
    ashley "Да, Мистер Беркельбаух."
    banker "И наша с тобой договоренность в силе."
    banker "Ты выполнила свое условие, значит, я выполню свою часть договора и подпишу бумаги на продление твоей кредитной линии."
    ashley "Я рада, Мистер Беркельбаух, что мы с вами смогли договориться."
    banker "Ммммм...."
    banker "Да, Эшли... Мммм..."
    # Молли шипит на Монику
    music Turbo_Tornado
    imgf 31413
    molly "Ты дотрагиваешься до меня! Фу!"
    molly "Я уже еле терплю тебя рядом! Отодвинься от меня!"
    m "ТЫ меня терпишь?!"
    molly "Да!"
    m "Да пошла ты, стерва!"
    # Моника толкает попой Молли
    imgd 31414
    w
    sound Jump1
    imgd 31415
    w
    imgf 31416
    m "Это из-за тебя тут так мало места!"
    m "Меньше надо коктейлей пить после работы, задница станет меньше!"
    molly "Ах ты дрянь!"
    # толкает Монику
    imgd 31417
    w
    sound Jump1
    imgd 31418
    # Эшли шипит на них
    img 31419
    ashley "А ну-ка тихо!!!"
    ashley "Вы мешаете Мистеру Беркельбауху!"
    # Моника с Молли недовольно смотрят друг на друга
    imgd 31413
    w
    # банкир тем временем продолжает дрочить
    music Loved_Up
    imgf 31420
    banker "Ааааа..."
    imgd 31421
    banker "Какие попки..."
    imgf 31409
    w
    sound drkanje5
    imgd 31410
    w
    imgd 31409
    w
    sound drkanje5
    imgd 31410
    w
    music Loved_up2
    imgd 31409
    w
    sound drkanje5
    imgd 31410
    w
    imgd 31409
    w
    sound drkanje5
    imgd 31410
    banker "Даааа..."
    imgf 31422
    banker "Ааааа..."
    img 31424
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    banker "ААААА!!!"
    img 31423
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    # банкир кончает, глядя на попы
    fadeblack 1.5
    music Groove2_85
    imgf 31425
    banker "Я только что утвердил нашу договоренность, Эшли."
    ashley "Спасибо, Мистер Беркельбаух."
    ashley "Вы так добры ко мне."
    # банкир довольно улыбается
    # затемнение
    # смена кадра
    # все стоят одетые
    # банкир шлепает по попе Клэр
    fadeblack 1.5
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 31426
    w
    imgf 31427
    w
    sound snd_slap1
    img 31428 hpunch
    banker "Отличная попка!"
    # она хлыстом хлопает его по руке, он похотливо на нее смотрит
    ##
#    если тут будет звук как бьют кнутом - то думаю смотреться будет лучше
    ##
    sound vjuh4
    img 31429 vpunch
    clare "!!!"
    clare "Руки прочь!"
    # убирает руку, обращается к Эшли
    sound ma5
    img 31430
    banker "Ай!"
    w
    imgd 31431
    banker "Эшли, жду тебя завтра у себя в офисе."
    banker "Не опаздывай."
    banker "Время - деньги."
    # Моника смотрит ему вслед
    sound man_steps
    imgf 31432
    w
    music Power_Bots_Loop
    imgd 31433
    mt "Отвратительный мерзкий неудачник!"
    mt "Никчемный банкиришка!"
    mt "!!!"
    # уходит
    # девочки с Эшли в подсобке
    # Эшли встает руки в боки, включает начальницу
    music Groove2_85
    imgf 31434
    ashley "Так!"
    ashley "Никто не должен ни слова говорить о произошедшем ни одной живой душе!"
    ashley "О моих договоренностях с этим банкиром никто не должен знать!"
    ashley "Особенно Джо!!"
    ashley "Всем ясно?!"
    ashley "Если Джо про это узнает, то мне придется вышвырнуть его отсюда!"
    ashley "И ваша жизнь станет значительно хуже!"
    # Молли говорит
    imgd 31435
    molly "Да, Эшли. Без проблем."
    molly "На сегодня все?"
    ashley "Да. Все свободны."
    # Молли с Клэр уходят
    sound highheels_short_walk
    imgf 31436
    mt "Надо спросить у этой чертовой Эшли про плакат."
    fadeblack 1.5
    music Groove2_85
    imgf 31437
    m "Эшли, я выполнила твое условие."
    m "Ты обещала, что не будешь вешать плакат у барной стойки."
    ashley "Да, [monica_pub_name], я помню."
    ashley "Может, ты передумаешь?"
    ashley "Это хорошая реклама для твоей попки."
    imgf 31438
    ashley "Сможешь зарабатывать намного больше чаевых." # подмигивает
    m "Я не хочу, чтобы этот плакат висел в баре!!!"
    m "!!!"
    ashley "Ну ладно, ладно..."
    ashley "Но если вдруг передумаешь..."
    img 31439
    m "Нет!"
    m "!!!"
    ashley "Хорошо, хорошо."
    ashley "Все, иди!"
    ashley "Ты на сегодня свободна!"
    music Power_Bots_Loop
    imgf 23473
    sound highheels_short_walk
    mt "Ненавижу ее и этот гребаный бар!"
    mt "!!!"
    return

label gallery_19199:
    # Моника стоит у двери
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 16130
    mt "Ненавижу эту сучку!"
    mt "!!!"
    # Молли поворачивается к Монике и опять начинает цеплять Монику
    imgf 16132
    w
    sound highheels_short_walk
    imgd 22815
    molly "О, пришла любительница потрясти своим голым задом на сцене!"
    molly "Аха-ха-ха!"
    # Моника зло
    music Power_Bots_Loop
    imgd 22818
    m "Иди в жопу, Молли!"
    # Молли продолжает издеваться
    music Groove2_85
    imgf 19194
    molly "Ты мне просто завидуешь, сучка. Признайся."
    molly "Мне не нужно полностью раздеваться на сцене, чтобы заинтересовать посетителей бара."
    molly "И заработать много чаевых."
    molly "А вот у тебя получается сделать это, только сняв трусы перед всеми!"
    imgd 19195
    sound snd_woman_laugh
    molly "Кстати, зачем они тебе? Может быть ты вообще не будешь носить их?"
    molly "Аха-ха-ха!"
    # Моника злобно на нее смотрит
    music Power_Bots_Loop
    imgd 19196
    mt "Она что, что-то знает?.."
    mt "Нет, не думаю..."
    m "!!!"
    # Молли продолжает веселиться
    music Groove2_85
    imgf 19197
    molly "Поэтому ты и воруешь у меня деньги, сучка!"
    molly "Тебе со мной, королевой Shiny Hole, не сравниться! Никогда!"
    molly "И ты всегда будешь получать жалкие пару долларов за то, что голая кривляешься на сцене!"
    molly "Неудачница!"
    molly "Аха-ха-ха!"
    # Монику бомбит
    music Pyro_Flow
    img 19198 vpunch
    m "Это я неудачница?!"
    m "Ты совсем охренела, стерва?!?!?!!?"
    m "Ты думаешь, раз ты надела корону в этой грязной дыре, куда ходят одни алкаши!.."
    m "То значит ты здесь лучшая?!"
    imgd 19199
    m "Если я только захочу, я с тебя эту корону сниму в два счета!"
    m "Поняла, сучка!!!"
    # Молли язвительно
    music Groove2_85
    imgf 19200
    molly "Если только в твоих снах! Аха-ха!"
    molly "Даже не мечтай об этом!"
    molly "Тебе никогда со мной не сравниться, поняла!"
    # Моника злится
    music Stealth_Groover
    imgd 18225
    mt "Эта сучка с каждым днем все отвратительнее себя ведет!"
    mt "Хабалка! Ненавижу!"
    mt "Не имеющая вкуса, не разбирающаяся в моде дешевая шлюха!"
    mt "Мне нужно поставить эту стерву на место!"
    mt "!!!"
    imgf 19201
    m "Что?! Это мне с тобой не сравниться?!"
    m "Выйди со мной на сцену и мы посмотрим, кто здесь настоящая королева!"
    m "Уверена, это будешь не ты! Даже если разденешься догола!"
    # Молли ведет себя уверенно и с вызовом говорит
    music Groove2_85
    imgd 19202
    molly "Ты хочешь соревноваться на сцене со мной? С самой королевой Shiny Hole?"
    imgd 19203
    m "Да! Или ты боишься потерять свою корону?!"
    sound snd_woman_laugh
    imgf 19195
    molly "Аха-ха-ха!"
    molly "Не смеши меня!"
    molly "Ты же неудачница. Что бы ты на сцене не сделала, ты обречена на провал!"
    molly "Так что мне не о чем переживать, сучка!"
    # Молли отворачивается от Моники к своему зеркалу
    music Stealth_Groover
    imgd 18224
    mt "Мерзкая рыжая стерва!"
    mt "Я сделаю все, чтобы лишить ее короны!"
    mt "Здесь только одна королева - Я, Моника Бакфетт!"
    mt "!!!"
    return

label gallery_19224:
    # Моника торжествует, Молли злая и униженная
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 19222
    m "Ну что, сучка?! Что ты скажешь новой королеве Shiny Hole?"
    imgf 19223
    w
    imgd 24353
    w
    molly "Я тебе этого просто так не оставлю!" # смотрит на картину (вид из картины)
    imgd 19224
    m "Ты еще угрожаешь мне, своей королеве?"
    # забегает довольная Эшли, обращается к Монике
    music Groove2_85
    imgf 19225
    ashley "Я всегда знала, что эта попка покорит нашу сцену!"
    ashley "[monica_pub_name], теперь ты новая королева!"
    imgd 31947
    ashley "И чтобы больше никаких драк!!!"
    ashley "Это вас обеих касается! Тебе понятно, Молли?!"
    # Молли зло отвечает
    imgd 31948
    molly "ДА!"
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    # затемнение, Молли оделась
    imgfl 31949
    w
    imgf 31950
    w
    imgd 31951
    w
    imgf 31952
    ashley "С этого дня ты, Молли, должна отдавать мне проценты со своих чаевых."
    ashley "А [monica_pub_name] всю выручку будет забирать себе."
    # Эшли смотрит на Монику игриво
    music Loved_Up
    imgd 31953
    ashley "Это твоя королевская привелегия, [monica_pub_name]..."
    # Эшли кладет руку на ее попу и сжимает ее, Моника делает вид, что не замечает этого
    sound Jump2
    img 31954 vpunch
    w
    imgf 31956
    m "..."
    imgd 31955
    ashley "У королевской попки должны быть королевские чаевые..."
    # Моника все это время высокомерно смотрит на Молли, та молча зло на нее
    imgf 31957
    molly "!!!"
    imgd 31958
    ashley "И, Молли, если королева пожалуется мне, то тебе придется извиняться перед ней..."
    # Молли с психом уходит
    imgd 31959
    sound highheels_short_walk
    molly "Рано радуешься, су... королева! Я отомщу тебе!"
    w
    # Эшли пошло подмигивает Монике и тоже выходит
    imgf 31954
    w
    imgd 31960
    w
    # Моника про себя злорадствует
    sound man_steps
    imgf 31961
    w
    music Stealth_Groover
    imgd 31962
#    mt "Я сегодня заработала [monica_strip_tips_today] долларов за одно выступление!"
#    mt "И ни цента не должна теперь никому отдавать!"
#    mt "В отличие от рыжеволосой шлюхи!"
    mt "Так и надо этой сучке! Пусть знает свое место!"
    mt "Неважно где и неважно как, но я всегда была и остаюсь королевой!"
    if monicaBitch == True:
        img 31963
        mt "И никакие жалкие людишки не смогут встать у меня на пути!"
    return

label gallery_31938:
    # Молли снова начинает цеплять Монику
    music Groove2_85
    imgfl 31924
    w
    imgf 31925
#    molly "Пришла?"
    molly "Я думала, что ты постыдишься выходить на сцену после своего провала!"
    molly "Аха-ха!"
    # Моника злобно
    imgd 31926
    m "!!!"
    molly "Мало того, что неудачница, еще и воровка! Хи-хи!"
    molly "Мне, в отличие от тебя, не нужно платить проценты Эшли..."
    molly "Или воровать чужие деньги. Хи-хи!"
    molly "Давай, иди виляй своей голой жирной задницей, шлюха."
    imgd 31927
    m "!!!"
    menu:
        "Проигнорировать рыжую шлюху!":
            music Stealth_Groover
            imgf 31928
            mt "Я не хочу разговаривать с этой сучкой!"
            mt "Она специально провоцирует меня, чтобы снова подставить перед Эшли!"
            mt "И вообще, Моника!"
            imgd 31929
            mt "Тебе не стоит опускаться до уровня этой тупой провинциалки, которая возомнила из себя королеву!"
            mt "Ты таких, как она, даже к кастингу в свой журнал не допускала!"
            mt "Мерзкая рыжая дрянь!"
            imgf 31930
            m "Иди в жопу, Молли!"
            # не будет доступна ни драка, ни второй батл
            return
        "Врезать ей!":
            pass
    # Монику бомбит, Молли надменно
    music Power_Bots_Loop
    imgd 31931
    m "Ты, сучка! Ты победила только потому что сняла маску и опозорилась перед всем Shiny Hole!"
    m "И ты сверкала своей голой задницей!"
    music Groove2_85
    imgf 31932
    molly "Мою задницу и меня любит весь Shiny Hole."
    molly "Я королева здесь, а ты - жалкая подстилка."
    molly "Твое дело - разносить пиво за пару центов чаевых..."
    imgd 31933
    molly "И ты снова грубо разговариваешь со мной."
    molly "Пожалуй, попрошу Эшли снова заставить тебя просить прощения передо мной."
    molly "Также, попрошу ее повысить процент, который она забирает с твоих чаевых."
    molly "Дешевая уличная шлюха..."
    # Моника в бешенстве
    music Power_Bots_Loop
    img 31934 hpunch
    m "ТВАРЬ!"
    # подбегает к Молли
    label gallery_31938_loop1:
    menu:
        "Толкнуть сучку!": # высокая бичность
            label gallery_31991:
            music Turbo_Tornado
            imgd 31935
            m "Мерзкая дешевая потаскуха!!!"
            # толкает Молли, та падает со стула
            sound anger2
            imgd 31936
            m "Никчемная шлюха!!!"
            # та вскакивает и толкает Монику в ответ
            sound snd_bodyfall
            img 31937 vpunch
            w
            imgd 31938
            w
            sound Jump1
            imgf 31939
            w
            sound angry_cat1
            imgd 31940
            w
            imgd 31941
            molly "АХ ТЫ ДРЯНЬ!!!"
            menu:
                "Вцепиться в ее волосы!": # высокая бичность
                    # Моника хватает Молли за волосы
                    imgf 31942
                    w
                    imgd 31943
                    w
                    sound vjuh3
                    img 31944 vpunch
                    w
                    imgd 31945
                    m "МЕРЗКАЯ СУКА!!!"
                    sound scream1
                    imgd 31946
                    molly "ААААА!!!"
                    molly "СУЧКАААА!!!"
                    # Молли в ответ хватает Монику за волосы
                    sound vjuh3
                    img 31982 vpunch
                    w
                    sound snd_julia_scream1
                    imgd 31983
                    w
                    imgd 31984
                    w
                    menu:
                        "Ударить эту сучку по груди!": # высокая бичность
                            # Моника бьет Молли по груди
                            imgf 31985
                            m "НЕНАВИЖУ!!!#тебя"
                            # sound anger2
                            imgd 31986
                            w
                            sound snd_punch_face2
                            img 31987 hpunch
                            m "УБЬЮ ТЕБЯ!!!"
                            sound scream3
                            imgd 31988
                            w
                            # Молли ослабляет свою хватку
                            menu:
                                "Врезать ей по лицу!": # высокая бичность
                                    imgf 31989
                                    w
                                    imgd 31990
                                    sound anger2
                                    w
                                    sound snd_punch_face1
                                    img 31991 vpunch
                                    w
                                    sound scream3
                                    imgd 31992
                                    w
                                    sound snd_bodyfall
                                    img 31993 hpunch
                                    w
                                    imgf 31994
                                    w
                                    imgd 31995
                                    w
                                    # Моника с размаху бьет Молли по лицу, та теряет равновесия и падает на пол
                                    # падая, хватается за жилет Моники и срывает его
                                    # Молли на полу, Моника с размаху бьет ее ногой в живот
                                    menu:
                                        "Добить сучку ногами!":
                                            pass
                                    imgf 31996
                                    w
                                    imgd 31997
                                    sound anger2
                                    w
                                    sound Damage3
                                    img 31998 vpunch
                                    m "Получай, шлюха!"
                                    imgd 31997
                                    #sound anger2
                                    w
                                    sound Damage3
                                    img 31998 vpunch
                                    m "Ненавижу!#тебя"
                                    imgd 31997
                                    #sound anger2
                                    w
                                    sound Damage3
                                    img 31998 vpunch
                                    m "Тварь!!!"
                                    # Молли скрючивается от боли, но потом хватает Монику за ногу в момент след удара
                                    # Моника теряет равновесие и падает на пол
                                    sound scream1
                                    imgf 31999
                                    w
                                    imgd 32000
                                    w
                                    sound snd_bodyfall
                                    img 32001 hpunch
                                    w
                                    imgd 32002
                                    w
                                    pass
                                "Толкнуть ее!":
                                    # Моника толкает Молли, та теряет равновесия и падает на пол
                                    imgf 32003
                                    w
                                    imgd 32004
                                    w
                                    # падая, хватается за грудь Моники, срывает жилет
                                    imgd 32005
                                    sound anger2
                                    w
                                    sound snd_bodyfall
                                    img 32006 vpunch
                                    w
                                    # Моника хватается за грудь, а Молли в это время бьет ее по ногам и Моника тоже падает
                                    imgf 32008
                                    w
                                    imgd 32007
                                    sound2 down
                                    #sound anger2
                                    w
                                    sound snd_julia_scream1
                                    imgd 32009
                                    m "АААА!!!"
                                    pass
                            # Моника на полу бьет локтем Молли по лицу
                            sound snd_bodyfall
                            img 32010 vpunch
                            w
                            #sound anger2
                            imgd 32011
                            w
                            menu:
                                "Защититься от сучки!":
                                    pass
                            sound Damage3
                            img 32012 vpunch
                            w
                            # та закрывается от боли
                            sound scream3
                            imgd 32013
                            molly "Сукаааа!!!"
                            molly "Аааа!!!"
                            # Моника лезет на Молли, садится сверху и хватает ее за шею
                            imgf 32014
                            w
                            sound angry_cat1
                            menu:
                                "Вцепиться ей в горло!":
                                    pass
                            #sound anger2
                            img 32015 vpunch
                            w
                            imgf 32016
                            w
                            imgd 32017
                            w
                            # Молли вцепляется ногтями в лицо Моники и сталкивает ее с себя
                            sound snd_punch_face1
                            img 32018 hpunch
                            w
                            imgd 32019
                            sound anger2
                            w
                            sound snd_bodyfall
                            img 32020 vpunch
                            w
                            imgf 32021
                            w
                            imgd 32022
                            w
                            pass
                        "Попытаться увернуться от Молли.": # Моника приличная
                            # Моника пытается увернуться от Молли, которая пытается вцепится в ее волосы
                            imgf 32023
                            w
                            imgd 32024
                            sound anger2
                            m "ААААА!!!"
                            # но Молли хватает ее за волосы, резко опускает ее голову и бьет коленом по лицу
                            sound Damage3
                            img 32025 vpunch
                            molly "Получай, шлюха!"
                            sound snd_julia_scream1
                            imgd 32026
                            w
                            imgd 32027
                            w
                            imgd 32028
                            w
                            sound snd_julia_scream1
                            imgd 32029
                            m "АААААА!!!"
                            menu:
                                "Ударить ее чем-нибудь!":
                                    imgf 32030
                                    #sound anger2
                                    w
                                    # Моника тянется за стулом, но Молли опережает ее и отталкивает Монику
                                    # Моника падает на пол
                                    sound snd_bodyfall
                                    img 32031 vpunch
                                    w
                                    sound angry_cat1
                                    imgd 32032
                                    w
                                    imgd 32033
                                    w
                                    # Молли подбегает к Монике, садится сверху нее и начинает душить
                                    sound vjuh3
                                    imgd 32034
                                    w
                                    imgd 32035
                                    w
                                    imgd 32036
                                    sound anger2
                                    w
                                    imgd 32037
                                    molly "Сукаааа!!!"
                                    imgd 32039
                                    molly "Убью тебяяяяя!!!"
                                    imgd 32038
                                    menu:
                                        "Вцепиться сучке в лицо!":
                                            pass
                                    m "АААА!!!"
                                    # Молли сидит на Монике сверху и душит ее
                                    # Моника вцепляется ногтями в лицо Молли и сталкивает ее с себя
                                    sound snd_punch_face1
                                    img 32040 vpunch
                                    w
                                    imgd 32041
                                    #sound anger2
                                    w
                                    sound snd_bodyfall
                                    img 32042 hpunch
                                    w
                                    imgd 32043
                                    w
                                    pass
                                "Толкнуть ее!":
                                    # Моника толкает Молли, но та бьет Монику по лицу
                                    imgd 32044
                                    w
                                    sound anger2
                                    imgd 32045
                                    w
                                    sound snd_punch_face1
                                    img 32046 hpunch
                                    w
                                    imgd 32047
                                    molly "Сучка!!!"
                                    # Моника падает и хватается за трусы Молли, стаскивает их
                                    imgd 32048
                                    w
                                    sound Jump1
                                    imgd 32049
                                    w
                                    sound snd_bodyfall
                                    img 32050 vpunch
                                    molly "ААА!!!"
                                    imgf 32051
                                    w
                                    # Молли падает вслед за ней, потом быстро садится на Монику сверу и начинает душить
                                    imgd 32033
                                    w
                                    #sound anger2
                                    sound angry_cat1
                                    imgd 32052
                                    w
                                    imgd 32053
                                    w
                                    imgd 32054
                                    w
                                    #sound anger2
                                    imgd 32055
                                    w
                                    imgd 32039
                                    w
                                    imgd 32038
                                    menu:
                                        "Вцепиться сучке в лицо!":
                                            pass
                                    m "АААА!!!"
                                    sound snd_punch_face1
                                    img 32056 vpunch
                                    w
                                    imgd 32057
                                    w
                                    sound snd_bodyfall
                                    img 32058 hpunch
                                    w
                                    sound anger2
                                    imgd 32059
                                    w
                                    imgd 32043
                                    w
                                    pass
                            pass
        "Дать ей пощечину!": # Моника приличная
            music Turbo_Tornado
            imgd 32060
            m "Ах ты дрянь!!!"
            # размахивается и бьет Молли ладонью по лицу
            imgd 32061
            w
            img 32062
            w
            sound snd_punch_face1
            img 32063 hpunch
            w
            #sound anger2
            imgd 32064
            m "Как ты смеешь?!"
            imgf 32065
            molly "Ну все, сучка!"
            molly "Ты за это ответишь!"
            # Молли размахивается и бьет Моника в ответ по лицу кулаком
            # Моника едва удерживается на ногах
            # в шоке смотрит на Молли
            sound anger2
            imgd 32066
            w
            sound down
            img 32067 vpunch
            w
            imgd 31934
            w
            # переход на начальное меню, где доступен пункт "Толкнуть сучку!"
            jump gallery_31938_loop1
        "Уйти.":
            music Stealth_Groover
            imgf 31927
            mt "Я не хочу разговаривать с этой сучкой!"
            mt "Она специально провоцирует меня, чтобы снова подставить перед Эшли!"
            sound highheels_short_walk
            imgd 31928
            w
            imgd 31929
            w
            imgf 31930
            m "Иди в жопу, Молли!"
            # Моника уходит
            return
    fadeblack
    sound Damage3
    pause 0.5
    sound snd_punch_face1
    pause 0.5
    sound snd_julia_scream1
    pause 0.5
    sound snd_break_dress
    pause 1.5
    music Turbo_Tornado
    imgf 32068
    w
    imgd 32069
    w
    sound man_steps
    imgf 32070
    w
    music Power_Bots_Loop
    img 32071 vpunch
    ashley "А ну-ка хватит!!!"
    ashley "Битву сучек надо устраивать на сцене!"
    ashley "Это, по крайней мере, приносит деньги!"
    ashley "А не устраивать тут драку!"
    imgf 32070
    ashley "Вы что, совсем охренели, такой шум тут подняли!?!?!?"
    # Молли с Моникой, несмотря на крики Эшли продолжают таскать друг друга за волосы
    menu:
        "Врезать сучке коленом в живот!":
            music Turbo_Tornado
            imgd 32072
            w
            imgd 32073
            # Моника пытается пнуть Молли ногой, но у нее не получается
            m "Ненавижу!!!#тебя"
            imgd 32074
            #sound anger2
            # Молли вцепляется ногтями в грудь Моники
            w
            sound down
            img 32075 vpunch
            m "АААА!!!"
            # Моника отпускает Молли и резко отстраняется
            # при этом она задевает Эшли, та теряет равновесие и падает между ними, юбка задирается
            sound snd_julia_scream1
            imgd 32076
            w
            sound scream3
            imgd 32077
            w
            sound snd_bodyfall
            img 32078 hpunch
            w
            imgd 32079
            w
            pass
        "Вцепиться ногтями в ее грудь!": # высокая бичность
            # Моника убирает руки от волос Молли и вцепляется в ее грудь когтями
            music Turbo_Tornado
            imgd 32072
            w
            imgd 32080
            #sound anger2
            w
            sound down
            img 32081 vpunch
            w
            sound scream3
            imgd 32082
            molly "АААААА!!!"
            molly "ТВААААРЬ!!!"
            imgd 32076
            w
            sound scream3
            imgd 32077
            w
            sound snd_bodyfall
            img 32078 hpunch
            w
            imgd 32079
            w
            # Молли отпускает Монику и резко отстраняется
            # при этом она задевает Эшли, та теряет равновесие и падает между ними, юбка задирается
            pass
    # все трое на полу, Эшли пытается выбраться
    imgd 32083
    sound anger2
    w
    img 32084 vpunch
    ashley "Мать вашу!!!"
    # начинают колотить друг друга на полу, один удар перепадает Эшли, которая пытается встать
    # Молли через Эшли пытается дотянуться до лица Моники и расцарапать его
    imgd 32085
    #sound anger2
    w
    sound down
    img 32086 vpunch
    w
    sound Damage3
    img 32087 vpunch
    w
    ## арты будут смотреться если в сопровождении будет звук ударов ##
    sound scream3
    imgd 32088
    w
    menu:
        "Укусить ее!": # Моника приличная
            # в тот момент, когда рука Молли рядом с лицом Моники, Моника зубами вцепляется в ее руку
            # Молли орет
            sound anger2
            img 32089 vpunch
            w
            sound scream3
            imgd 32090
            molly "СУУУУКААА!!! Я ТЕБЕ СЕЙЧАС!!!"
            # Молли облокачивается на Эшли, которая так и не может встать, перегибается через нее и колотит Монику по голове
            #sound anger2
            imgd 32092
            ashley "Дайте мне встать!"
            imgd 32091
            w
            imgd 32093
            #sound anger2
            w
            sound Damage3
            img 32094 vpunch
            m "АААААА!!!"
            # Моника пытается закрываться от ударов
            # Эшли отталкивает с себя Молли, Эшли встает и начинает орать
            sound snd_julia_scream1
            imgd 32092 hpunch
            ashley "Вы совсем охренели?!"
            pass
        "Врезать ей!": # высокая бичность
            # Эшли уже почти удалось встать, но Моника толкает ее локтем, Эшли снова падает
            # Моника цепляется за рубашку Эшли, рубашка задирается (рвется?), грудь Эшли выскакивает наружу
            # Моника облокотившись на груди Эшли начинает колотить Молли куда попало - лицо, голова, грудь
            imgd 32106
            ashley "Дайте мне встать!"
#            w
            #sound anger2
            imgd 32107
            w
            sound snd_punch_face1
            img 32108 vpunch
            w
            imgd 32110
            #sound anger2
            w
            sound Damage3
            img 32109 vpunch
            m "На!"
            m "Получай!"
            imgd 32110
            #sound anger2
            w
            sound Damage3
            img 32109 vpunch
            m "Мразь!"
            m "Тварь!"
            # Эшли отталкивает с себя Монику, Эшли встает и начинает орать
            img 32111 hpunch
            ashley "Вы совсем охренели?!"
            pass
    fadeblack 2.0
    music Power_Bots_Loop
    imgfl 32095
    ashley "Быстро прекратили!"
    ashley "[monica_pub_name]!"
    ashley "Мне что, вызвать полицию, чтобы вас разнять?!"
    # Эшли хватает Монику и поднимает ее на ноги
    music Groove2_85
    imgf 32096
    w
    # Моника злая, как собака, и лохматая, стоит рядом с Эшли, готова набросится на Молли, Эшли ее удерживает
    sound Jump2
    imgd 32097
    ashley "ХВАТИТ!"
    # Молли встает с пола
    imgf 32098
    ashley "[monica_pub_name]!"
    ashley "Молли!"
    ashley "Быстро на сцену! Обе!"
    ashley "Выясняйте отношения там!!!"
    # Моника с Молли зло смотрят друг на друга
    imgd 32099
    m "!!!"
#    $ menu_corruption = [pubMollyBattle2CorruptionRequired]
    menu:
        "Батл с Молли.":
            music Pyro_Flow
            imgf 32100
            m "Сегодня я точно надеру тебе задницу, мерзкая шлюха!"
            molly "За свою задницу беспокойся, сучка!"
            imgd 32101
            mt "Тварь!!!"
            mt "!!!"
            pass
        "Отказаться.":
            music Pyro_Flow
            imgf 32102
            m "Еще чего!"
            m "С меня достаточно!"
            m "Я не собираюсь делить сцену с этой сучкой!!!"
            molly "Правильно, неудачница, иди зарабатываей свои несчастные центы."
            molly "И не забудь отдать процент Эшли!"
            molly "Аха-ха!"
            # Эшли уходит
            imgd 32103
            ashley "[monica_pub_name], тогда иди быстро на сцену!"
            ashley "Какого черта ты до сих пор тут?!"
            # Моника идет танцевать одна
            # если не идти на батл, а снова кликнуть на Молли, то можно будет повторить сцену драки
            return
    music Groove2_85
    imgf 32104
    ashley "Быстро тащите свои задницы на сцену!"
    # Моника с Молли переглядываются зло и идут к выходу с гримерки
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgf 32105
    w
    # Эшли выходит на ними следом
    return
