#call ep216_dialogues0_biff1() # Сесть на стол спиной к Бифу
#call ep216_dialogues0_biff2() # Сесть на стол, достать член Бифа и взять его в рот
#call ep216_dialogues0_biff2a() # мысли после сцены у Бифа
#call ep216_dialogues0_biff2b() # мысли, если убежала
default ep216_dialogues0_biff2_cumzone = 0

label ep216_dialogues0_biff1: #Сесть на стол спиной к Бифу.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    imgfl 22908
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
    imgf 22909
    mt "Сволочь!"

    imgd 24354
    m "Биф, что ты хочешь чтобы я снова сделала?!"

    biff "Это не моя задача придумывать, чем развлекать папочку, цыпочка!"
    biff "Залезь на стол, сделай что-нибудь новое."
    biff "Цыпочка должна развлекать папочку! Папочке скучно!"

    menu:
        "Залезть на стол Моники.":
            pass

    sound snd_walk_barefoot
    imgf 24355
    mt "Ненавижу! Ненавижу!"
    fadeblack 1.5
    music Groove2_85
    imgf 24356
    w
    imgd 24357
    m "Так достаточно, Биф?"

    imgf 24358
    biff "Нет, цыпочка!"
    biff "Папочке ничего не видно!"
    biff "Покажи себя сзади!"
    biff "Папочка хочет видеть за что он платит такие большие деньги какой-то шлюхе!"

    img 24359
    m "Я не шлюха, Биф!"

    imgd 24360
    biff "Ты уличная двадцатидолларовая шлюха, которая пытается быть хорошей цыпочкой и вечелить папочку!"
    biff "Она знает, что плохая цыпочка здесь не задержится и не будет зарабатывать такие огромные деньги!"
    biff "Быстро развернись и покажи мне свою задницу!"
    biff "Читатели нашего журнала ждут, когда твоя голая задница будет на обложке журнала!"
    biff "И я должен проверить, что они не будут разочарованы!"

    menu:
        "Сесть спиной к Бифу.":
            pass
    music Pyro_Flow
    imgf 24361
    mt "БОЖЕ! На что мне приходится идти, чтобы у меня были деньги для этой сучки Виктории и Дик продолжал заниматься моим делом!"
    mt "Этот Биф издевается надо мной все больше и больше!"
    mt "Сейчас у меня нет выбора, но мне надо найти выход!"
    mt "Так не может больше продолжаться!"
    fadeblack 1.5
    music Hidden_Agenda
    imgf 24362
    m "Мне... Нужны эти деньги Биф..."
    m "Я хорошая цыпочка..."
    mt "!!!"
    music Groove2_85
    imgd 24363
    biff "Это ты называешь показать себя?"
    biff "За такое наши читатели не заплатят ни цена!"
    biff "Цыпочка сейчас ляжет на стол и вытянет свои ножки ко мне!"

    menu:
        "Лечь на стол перед Бифом.":
            pass
    fadeblack 1.5
    music Hidden_Agenda
    imgf 24364
    m "Так дебя устроит, Биф?"
    m "Я достаточно развлекла папочку?!"
    music Loved_Up
    imgd 24365
    biff "Нет, цыпочка! Еще далеко не достаточно!"
    biff "Цыпочка сейчас раздвинет свои ножки, очень широко!"

    menu:
        "Раздвинуть ноги.":
            pass
    mt "Дьявол!"

    imgd 24366
    sound Jump2
    m "Так, Биф?!"

    imgf 24367
    biff "Нет, цыпочка! Еще шире!"
    biff "Папочка сказал что цыпочка раздвинет ноги очень широко!"
    biff "Перед папочкой!"

    menu:
        "Раздвинуть ноги еще шире.":
            pass
    sound Jump2
    imgd 24368
    m "Так устроит?"
    mt "Дьявол! Чувствую себя отвратительно!"
    mt "Грязный извращенец!"

    imgf 24369
    biff "Давай, тянись ручками к своим ножкам!"
    biff "Покажи папочке свою гибкость!"
    biff "Папочка любит гибких цыпочек!"
    biff "Скажи, ты гибкая цыпочка?"
    sound Jump1
    imgd 24370
    mt "БОЖЕ! Как я ненавижу этого Бифа!"
    mt "Я убью его, клянусь!"


    imgf 24371
    m "Я... Я гибкая цыпочка, Биф..."

    imgd 24372
    biff "Отлично!"
    biff "А теперь цыпочка встанет на колени и хорошенько выгнется к папочке!"
    biff "Папочка хочет хорошенько рассмотреть то, за что скоро будут платить наши читатели!"
    music Pyro_Flow
    imgd 24373
    mt "Нет, я его не убью!"
    mt "Я буду его мучать! Я его буду долго мучать!!"
    mt "Я сделаю из него ничтожество! Он будет моим ковриком для обуви!"
    mt "Он... Он..."
    biff "Цыпочка, я жду!"

    menu:
        "Дать Бифу хорошенько рассмотреть себя.":
            pass

    mt "Дьявол!"
    fadeblack 1.5
    music Loved_Up
    imgfl 24374
    biff "Да, отлично! Вот так!"

    imgf 24375
    biff "Итак, что сейчас делает цыпочка?"

    imgd 24376
    m "Цыпочка... Показывает себя папочке..."

    imgf 24377
    biff "Правильно! Хорошая цыпочка!"

    imgd 24378
    biff "Надо же, какие у цыпочки мягкие бархатные ножки!"

    imgd 24379
    biff "И не скажешь что они принадлежат двадцатидолларовой шлюхе, которая приыкла работать на улице!"

    img 24380 vpunch
    m "Биф, я не шлюха!"

    imgd 24381
    biff "Да, ты теперь цыпочка!"
    biff "Которой папочка платит достаточно денег, чтобы ей не приходилось сосать на улице члены за $ 20!"

    mt "!!!"

    imgd 24382
    mt "Я ненавижу этого ублюдка!"
#    sound Jump1
    sound Jump1
    imgf 24383
    biff "Да, многие читатели ждут обложку с этой киской."
    biff "Думая что это и правда Моника Бакфетт."

    music Power_Bots_Loop
    img 24384 hpunch
    m "Биф, не смей меня лапать!!!"

    imgd 24385
    biff "Это обычный осмотр модели журнала!"
    biff "Если цыпочка будет пререкаться с папочкой, то вылетит на улицу прямо сейчас!"

    menu:
        "Терпеть прикосновения Бифа.":
            pass

    music Loved_Up
    imgf 24386
    mt "Дьявол, как мне выдержать это?!"

    imgd 24387
    biff "Итак, вот что вскоре ждет наших читателей..."

    imgf 24388
    biff "Читатели должны подумать, что это дейстительно киска Моники Бакфетт..."
    biff "Они платят за это свои деньги..."
    biff "В мой журнал..."

    imgd 24389
    biff "Жаль что она не настоящая..."
    biff "Мне рассказывали как выглядит настоящая киска Моники Бакфетт..."

    imgd 24390
    w
    imgd 24389
    w
    imgd 24390
    w
    imgf 24391
    biff "И, по описанию, она совсем не похожа..."

    imgd 24392
    mt "Что значит непохожа?!"
    mt "Никто не мог видеть меня обнаженной! Что за вздор!"

    imgf 24393
    w
    imgd 24394
    biff "Хотя эта киска тоже красивая..."
    biff "Хоть и обходится папочке слишком дорого..."
    sound chpok8
    imgd 24395 #чавк
    mt "!!!"
    music Pyro_Flow
    img 24396 hpunch
    m "НЕТ!!!"
    sound snd_bodyfall
    img 24397 vpunch
    m "ЧТО ЭТО ЗНАЧИТ, БИФ?!"
    music Groove2_85
    imgf 24398
    biff "Это значит что папочка проверяет свою цыпочку!"
    biff "Которой оказывает безмерное доверие, разрешая снимать свою задницу под видом Моники Бакфетт!"

    imgd 24399
    biff "Цыпочка расстроила папочку!"
    biff "Убирайся отсюда! Папочке не нужны плохие цыпочки!"
    sound Jump2
    imgf 24400
    m "Биф... Почему убираться отсюда?"
    m "Я... Я ведь сделала как ты просил..."

    imgd 24401
    biff "Ты убежала от папочки! А так хорошие цыпочки себя не ведут!"
    biff "Я поменяю тебя на другую цыпочку, которая дает себя трогать!"

    imgd 24402
    mt "Мерзавец! Он теперь что, собирается меня лапать?!"
    music Hidden_Agenda
    imgf 24403
    m "Биф... Я..."
    m "Я не убегала от тебя..."
    music Groove2_85
    imgd 24404
    biff "А что тогда это было?!"
    biff "Папочка хотел проверить киску своей цыпочки изнутри!"
    biff "А цыпочка убежала от папочки!"
    biff "Теперь эта цыпочка не получит ни цента за свою работу!"

    menu:
        "Сказать Бифу что Моника хорошая цыпочка.":
            pass

    imgd 24402
    mt "Дьявол! Мне надо что-то придумать, чтобы успокоить этого придурка!"
    music Hidden_Agenda
    imgf 24405
    m "Биф, я не убегала от тебя..."
    biff "А что тогда случилось у цыпочки?"

    imgd 24406
    m "Мне... Мне просто стало щекотно..."
    m "Я хорошая цыпочка, Биф..."
    music Groove2_85
    imgf 24407
    biff "Ахахахаха!!!"
    biff "Цекотно?! Ну да, точно!"
    biff "Ты же еще неопытная цыпочка!"
    biff "Хотя это и странно, учитывая откуда ты пришла сюда!"

    imgd 24408
    m "Биф, я могу одеться и идти?"

    imgd 24409
    biff "Цыпочка развеселила папочку и цыпочка может идти!"
    biff "Надеюсь, в следующий раз цыпочка придумает еще что-нибудь интересное..."
    music Power_Bots_Loop
    imgf 22920
    m "..."
    mt "Ненавижу этого придурка!"
    sound snd_fabric1
    fadeblack 1.5
    return


label ep216_dialogues0_biff2: #Сесть на стол, достать член Бифа и взять его в рот.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    imgfl 22908
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
    imgf 22909
    mt "Сволочь!"

    m "Я не знаю чем еще порадовать папочку..."
    m "!!!"
    mt "Мерзавец! Он и так уже заставлял меня делать вещи, что хуже некуда!"

    imgd 24410
    biff "У папочки сегодня хорошее настроение."
    biff "Папочка считает что цыпочка уже достаточно долго работает здесь и зарабатывает хорошие деньги."
    biff "И держится подальше от грязных улиц, с которых папочка ее подобрал..."
    music Power_Bots_Loop
    img 24411
    mt "!!!"
    mt "Мерзавец! Это мой офис! Это ты вылез сюда из какой-то грязной дыры!"
    music Groove2_85
    imgf 24412
    biff "Так что папочка решил позволить цыпочке и дальше развлекать его."
    biff "Папочка знает что цыпочка мечтает об этом!"

    imgd 24413
    m "Мечтает о чем???"
    mt "Я мечтаю только о том, чтобы вышвырнуть тебя из этого кресла!"

    imgd 24414
    biff "Цыпочка, залезай на стол. Ха-ха-ха!"
    sound snd_walk_barefoot
    imgf 24415
    m "!!!"
    # Моника ложится на стол
    fadeblack 1.5
    music Loved_Up
    imgfl 24416
    mt "Снова показывать этому мерзавцу свое восхитительное тело!"
    mt "Ненавижу!"

    imgf 24417
    biff "Нет, цыпочка!"
    biff "Садись наоборот! Ха-ха-ха!"

    imgd 24418
    m "В смысле наоборот?"
    m "Что это значит?"
    biff "Лицом к папочке!"

    # Моника садится лицом к Бифу
    # Биф откидывается в кресле
#    sound vjuh3
    fadeblack 1.5
    music Loved_Up
    imgf 24419
    w
    imgd 24420
    m "Биф, это все?"
    m "Я могу идти?"

    imgf 24421
    biff "Цыпочка, останься! Я знаю о чем ты сейчас думаешь!"
    biff "Папочка разрешает тебе!"

    imgd 24422
    m "Разрешает что?!"
    mt "О чем я думаю по его мнению?!"
    mt "Я хочу быстрее закончить это, вот и все о чем я думаю!"

    sound Jump1
    imgf 24423
    biff "Цыпочка, не стесняйся."
    biff "Я ведь знаю ты любишь папочку. За все что он сделал для тебя."

    imgd 24424
    m "В смысле не стесняться?!"
    m "Биф, что ты имеешь ввиду?!"
    m "Я и так перед тобой абсолютно голая!"

    imgf 24425
    biff "Протяни вперед свою ручку!"

    # Моника протягивает
    imgd 24426
    w
    biff "Ниже, цыпочка, ниже!"

    # Моника опускает еще ниже
    imgd 24427
    m "Я не понимаю..."

    biff "Еще ниже, цыпочка! Не стесняйся!"

    imgd 24428
    w
    imgf 24429
    biff "И протяни ее еще дальше!"

    img 24430
    m "Биф, но там..."

    imgf 24431
    biff "Да, цыпочка! Там моя ширинка!"
    biff "Я заметил, цыпочка все время на нее смотрит!"
    music Power_Bots_Loop
    img 24432 hpunch
    m "ЧТО?! НЕТ!"
    music Groove2_85
    imgd 24433
    biff "Да, хорошая цыпочка не будет стесняться и расстегнет папочке брюки!"

    img 24434
    m "Нет, БИФ! Зачем?!"

    imgf 24435
    biff "У папочки хорошее настроение! Скорее, сделай это пока оно не упало!"
    sound Jump1
    imgd 24436
    m "Но Биф! Я ведь работаю просто моделью!"

    imgf 24437
    biff "Ты работаешь куклой, которая похожа на Монику Бакфетт!"
    biff "И ты хорошая цыпочка, потому я тебе плачу такие деньги!"

    imgd 24438
    m "!!!"

    biff "Мое настроение начинает падать..."

    imgf 24439
    menu:
        "Расстегнуть ширинку Бифу.":
            pass
    music Power_Bots_Loop
    mt "Дьявол! Мне что, придется расстегивать ширинку у какого-то мерзавца, который сидит в моем кресле?!"
    mt "Ладно... Я сделаю это и сразу уйду..."
    fadeblack 1.5
    music Loved_Up
    # Моника расстегивает ширинку
    imgfl 24442
    biff "Да, цыпочка, вот так..."
    sound snd_zip
    imgf 24440
    biff "Осторожно... Медленно..."
    imgd 24441
    biff "Это член папочки. Это очень важная вещь в твоей жизни!"

    sound Jump1
    imgd 24443
    biff "Да, цыпочка! Видишь какое у папочки приподнятое настроение!"
    biff "Это потому, что папочка придумал чем цыпочка может его развеселить!"
    music Hidden_Agenda
    imgf 24444
    m "Биф, я сделала что ты просил. Я могу идти?!"
    music Groove2_85
    imgd 24445
    biff "Цыпочка, я хочу чтобы ты притворилась Моникой Бакфетт!"
    biff "Я плачу тебе за это и хочу увидеть как хорошо ты это делаешь!"
    biff "Я хочу чтобы ты сказала как тебя зовут и что ты хочешь попосать член у папочки!"
    biff "В ее бывшем кабинете!"

    img 24446 vpunch
    m "Моника Бакфетт такого никогда бы не сказала!!!"

    imgf 24447
    biff "Да, я слышал что она была еще той сучкой!"
    biff "Но очень хорошо что вместо нее у меня есть такая послушная кукла, похожая на нее!"
    music Power_Bots_Loop
    img 24448 hpunch
    m "Нет!"
    music Groove2_85
    imgd 24449
    biff "Давай цыпочка! Папочка ждет!"
    fadeblack 1.5
    music Power_Bots_Loop
    imgfl 24450
    m "Биф, я не хочу этого делать!"

    imgf 24451
    biff "Ты делала это сотни раз на улице, дешевая кукла!"
    biff "И теперь ты хочешь сказать папочке НЕТ???"

    imgd 24452
    m "Биф! Я..."
    music Pyro_Flow
    imgf 24453
    mt "Что мне сказать???"
    mt "Как я могу пойти на такую мерзость???"
    mt "Но я знаю что будет если я откажусь!"
    mt "Он выгонит меня из моего же офиса и перестанет платить деньги за эти ужасные фотосессии!"
    mt "И тогда мне конец!"
    music Groove2_85
    imgd 24454
    biff "Или ты уже сегодня сосала кому-то другому и не хочешь испачкать папочкин член чужой спермой?"
    music Power_Bots_Loop
    img 24455 hpunch
    m "Я..."
    mt "ЧТО?! КОМУ-ТО ДРУГОМУ???"
    mt "Он что, считает что я похожа на какую-то шлюху, которая делает это направо и налево?!"
    music Stealth_Groover
    imgd 24456
    mt "Я - Моника Бакфетт!"
    mt "Я глава этой компании!"
    mt "Да, я нахожусь в трудном положении из-за какого-то временного недоразумения!"
    mt "Но, клянусь, я верну все назад!"
    mt "Потому что Я - Леди!!!"
    mt "Я самая умная и богатая леди этого города!!!"
    music Groove2_85
    imgf 24457
    biff "Ну так что, цыпочка!"
    biff "Отвечай скорее!"
    biff "У хорошей цыпочке есть только два варианта!"
    imgd 24527
    w
    sound Jump2
    imgd 24458
    biff "Либо она уже сосала член кому-то еще, либо она Моника Бакфетт, которая хочет пососать член у папочки!"
    music Pyro_Flow
    img 24459 hpunch
    m "!!!"

    biff "Отвечай быстрее! Счтиаю до трех!"

    imgd 24460
    w
    with vpunch
    biff "Раз!"

    m "Биф, давай я не буду делать этого!"

    img 24461 vpunch
    biff "Два!"

    imgd 24462
    m "Давай я сделаю это в другой раз или... черт!"

    img 24463 vpunch
    biff "Три!"
    $ menu_corruption = [0, biffCastingTableBlowjobOption1, biffCastingTableBlowjobOption2]
    menu:
        "Убежать...":
            imgd 24464
            m "Нет! Я не буду этого делать!"
            m "И я не буду ничего говорить!"
            biff "Ты плохая цыпочка!"
            biff "Я запрещаю тебе появляться в офисе две недели!"
            biff "Пошла вон!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_run2
            pause 2.0
            return -1

        "Я уже сегодня сосала член другому мужчине, поэтому не хочу пачкать член папочки...":
            imgd 24465
            mt "Дьявол! Я не хочу трогать его вонючий отросток!"
            mt "Я скажу что угодно, лишь бы не делать этого!"
            mt "В конце концов, это просто сотрясание воздуха, просто слова!"
            music Hidden_Agenda
            imgf 24466
            m "Я... Я уже сегодня... Я..."
            imgd 24467
            biff "Говори быстрее! Папочка ждет!"
            imgd 24468
            m "Я сегодня уже..."
            m "Я уже делала это... делала это другому мужчине..."
            imgf 24469
            biff "Что ты делала другому мужчине, цыпочка?!"
            imgd 24470
            m "Я... Я сосала его член..."
            mt "О БОЖЕ!"
            imgf 24471
            biff "И? Что дальше?"
            imgd 24472
            m "И я... Я не хочу пачкать папочку..."
            music Groove2_85
            imgf 24473
            biff "Аха-ха-ха!!!"
            biff "Папочка не удивлен!"
            biff "Папочка знает что цыпочка - двадцатидолларовая шлюха!"
            biff "Шлюха неплохо зарабатывает в последнее время, но не может изменить своих привычек! Ха-ха!"
            m "!!!"
            fadeblack 1.5
            music Groove2_85
            imgd 24474
            sound snd_zip
            w
            imgd 24475
            biff "Однако, папочка любит честность..."
            biff "Но цыпочка должна учесть, что если она хочет и дальше нравиться папочке, то трахаться она должна только с папочкой!"
            biff "Или с инвесторами! Или еще с кем-то, с кем папочка скажет!"
            biff "Может быть ты не заметила, но твой ротик и твоя задница теперь стоят несколько дороже двадцати долларов, ха-ха-ха!"
            biff "Можешь идти, на сегодня ты достаточно рассмешила папочку!"
            music Power_Bots_Loop
            imgf 24476
            m "Мерзавец! Ненавижу!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_short_walk
            pause 2.0
            return -2
        "Я - Моника Бакфетт...":
            pass

    imgd 24477
    mt "Этот жалкий Биф даже не представляет мою ситуацию!"
    music Groove2_85
    imgd 24478
    biff "Ну, что молчишь?!"
    biff "Папочка ждет!"
    fadeblack 1.5
    music Groove2_85
    imgf 24479
    mt "Не могу поверить что я делаю это прямо в своем же кабинете..."
#    sound vjuh3
    imgd 24481
    w
    imgf 24482
    mt "Делаю это какому-то мерзавцу, который сидит в моем кресле..."
    imgd 24483
    mt "Как до этого могло дойти?"
    imgd 24484
    mt "Моника, я не верю во все происходящее..."
    mt "Это какой-то сон!"

    img 24485 vpunch
    biff "НУ?!"

    fadeblack 1.5
    music Loved_Up
    imgd 24486
    m "Я..."
    m "Меня зовут..."
    m "Меня зовут Моника Бакфетт..."
    m "Это... мой бывший кабинет..."
    imgd 24487

    m "..."
    imgf 24488
    biff "И???"
    music Power_Bots_Loop
    imgd 24489
    m "!!!"
    imgd 24490
    biff "!!!"
    music Groove2_85
    imgf 24491
    m "И я хочу пососать член папочки..."

    imgd 24492
    biff "Да, цыпочка! Наконец-то!"
    biff "Папочка разрешает тебе!"
    biff "Можешь приступать!"
    fadeblack 1.5
    music Loved_Up
    imgf 24493
    w
    imgd 24494
    w
    imgf 24495
    w
    imgd 24496
    mt "Я не верю... Я не верю..."

    imgf 24497
    w

    # Моника начинет делать минет
    sound hlup21
    imgd 24498
    w

    imgf 24499
    biff "Давай цыпочка, не стесняйся!"
    biff "У тебя внутри еще много места!"
    sound lick3
    imgd 24500
    biff "О Да!"

    $ localSoundVolume = 1.0
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_1 = Movie(play="video/v_Monica_Biff_Blowjob1_1.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Моника делает минет
    imgf 24501
    biff "Я буду представлять что сама Моника Бакфетт сосет папочкин член! О Да!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_2 = Movie(play="video/v_Monica_Biff_Blowjob1_2.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Loved_Up2
    imgd 24502
    w
    imgf 24503
    biff "У цыпочки маловато опыта!"
    biff "Отсасывая члены на улице за двадцать долларов она почти ничему не научилась!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_3 = Movie(play="video/v_Monica_Biff_Blowjob1_3.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 24504
    biff "Но я сделаю из тебя хорошую цыпочку!"
    biff "Я расскажу тебе как правильно поднимать настроение папочке!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_4 = Movie(play="video/v_Monica_Biff_Blowjob1_4.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound lick3
    imgf 24505
    biff "О Да!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_5 = Movie(play="video/v_Monica_Biff_Blowjob1_5.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_5
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 24506
    biff "Да, еще! Папочке нравится так! Да!"
    biff "Еще! Еще!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_6 = Movie(play="video/v_Monica_Biff_Blowjob1_6.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_6
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_7 = Movie(play="video/v_Monica_Biff_Blowjob1_7.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 24507
    menu:
        "Кончить на лицо Моники.":
            $ ep216_dialogues0_biff2_cumzone = 1
            img 24508
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            biff "Ааааааааа!!!"
            img 24509
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            sound squelch9
            imgd 24510 #хлюп :)
            w
            fadeblack 1.5
            music Groove2_85
            imgfl 24511
            m "!!!"
            mt "Отвратительно!!!"
            sound snd_zip
            imgf 24512
            biff "Цыпочка хорошо постаралась..."
            biff "Цыпочка, скажи, тебе понравился член папочки?"
            imgd 24513
            mt "Мерзавец! Это отвратительно!"
            menu:
                "Сказать что член папочки понравился.":
                    fadeblack 1.5
                    music Hidden_Agenda
                    imgf 24514
                    m "Да... Папочка... Мне понравился твой член..."
                    music Groove2_85
                    imgd 24515
                    biff "Хорошо, цыпочка!"
                    biff "Ты можешь идти."
                    biff "Папочка скоро снова нагуляет аппетит."
                    biff "Цыпочка должна не забыть развлечь его!"
                "Уйти.":
                    pass

            music Power_Bots_Loop
            imgf 24516
            m "Мерзавец! Ненавижу!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_short_walk
            pause 2.0

        "Кончить в рот Моники.":
            $ ep216_dialogues0_biff2_cumzone = 2
            sound Jump1
            img 24517 hpunch
            sound chavc6
            biff "Иди к папочке! Ближе!"
            imgd 24518
            biff "Да, вот так!"
            img 24519
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            biff "Ааааааааа!!!"
            img 24520 #хлюююююп :) bulk(?)
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            fadeblack 1.5
            music Groove2_85
            imgfl 24521
            m "!!!"

            mt "Отвратительно!!!"

            sound snd_zip
            imgf 24523
            biff "Цыпочка хорошо постаралась..."
            biff "Цыпочка, скажи, тебе понравился член папочки?"

            imgd 24522
            mt "Мерзавец! Это отвратительно!"
            menu:
                "Сказать что член папочки понравился.":
                    fadeblack 1.5
                    music Hidden_Agenda
                    imgf 24524
                    m "Да... Папочка... Мне понравился твой член..."
                    m "Мпффф, мпфффф..."
                    music Groove2_85
                    imgd 24525
                    biff "Хорошо, цыпочка!"
                    biff "Ты можешь идти."
                    biff "Папочка скоро снова нагуляет аппетит."
                    biff "Цыпочка должна не забыть развлечь его!"
                "Уйти.":
                    pass

            music Power_Bots_Loop
            imgf 24526
            m "Мерзавец! Ненавижу!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_short_walk
            pause 2.0
    return 1

label ep216_dialogues0_biff2a: #Сесть на стол, достать член Бифа и взять его в рот.
    mt "Не могу поверить что я это сказала!"
    mt "О БОЖЕ!"
    mt "Надеюсь, кроме этого мерзавца мои слова никто не услышал!"
    return

label ep216_dialogues0_biff2b: #Сесть на стол, достать член Бифа и взять его в рот.
    sound denied
    mt "Мерзавец!"
    mt "Да как он смеет! Две недели не пускать меня в мой же офис!"
    mt "Ненавижу!!!"
    return
#
