default monicaCitizens15Slums1 = False  #  Моника согласилась сдать апартаменты в аренду парню в синей куртке и его подруге
default monicaCitizens15Slums2 = False  #  Моника сказала, что ей нравится парень в синей куртке при его подруге
default monicaCitizens15Slums3 = False  #  Моника делала минет парню в синей куртке, т.к. его подруга ушла
default monicaCitizens15Slums4 = False  #  Моника подсматривала за сексом Фрэнка и его подруги
default monicaCitizens15Slums5 = False  #  Моника согласилась сделать минет Фрэнку, когда он занимался сексом со своей подругой
default monicaCitizens15Slums6 = False  #  Моника согласилась пойти с геем в свои апартаменты
default monicaCitizens15Slums7 = False  #  Моника разрешила гею потрогать свою киску

default monicaCitizen15SlumsCumZone1 = 0

#call ep216_dialogues3_citizens_1() # сцена с парнем в синей куртке
#call ep216_dialogues3_citizens_2() # мысли после сцены с парнем в синей куртке и его подругой
#call ep216_dialogues3_citizens_3() # мысли, если хочет сразу зайти в апартаменты, когда оставила там парочку
#call ep216_dialogues3_citizens_4() # сцена с геем

# при клике на чувака в синей куртке (Frank)
label ep216_dialogues3_citizens_1:
    music Groove2_85
    imgr Dial_Citizen_15_3
    citizen15 "Йо! Бэби! Что ты хочешь?"
    citizen15 "Решила подкатить ко мне?"
    imgl Dial_begin35_17
    mt "Как меня раздражает этот самодовольный козел!"
    m "Еще чего?!"
    m "Конечно, нет!"
    imgr Dial_Citizen_15_2
    citizen15 "Да ладно тебе, крошка!"
    citizen15 "Я давно заметил, что я тебе нравлюсь!"
    citizen15 "Но я расстрою тебя, на сегодня у меня уже есть подруга."
    imgl Dial_Monica_Whore_1
    m "Мне все равно!"
    imgr Dial_Citizen_15_1
    citizen15 "Кстати, про подругу... У меня к тебе есть дело, Бэби."
    citizen15 "Давай отойдем в менее людное место?"
    m "..."
    menu:
        "Пойти с ним.":
            imgl Dial_begin35_21
            mt "Что этому придурку от меня надо?"
            mt "Может, он предложит мне заработать?"
            m "Пошли..."
            # затемнение
            pass
        "Нет!":
            music Stealth_Groover
            imgl Dial_begin35_16
            mt "Фу, какой он мерзкий!"
            m "Нет!"
            m "Я не собираюсь никуда с тобой отходить!"
            music Groove2_85
            imgr Dial_Citizen_15_4
            citizen15 "Зря, крошка..."
            citizen15 "Но если захочешь подзаработать, ты знаешь, где меня найти."
            return -1
    # стоят у пилона
    # рендерить отсюда!!! до этого в движке
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 12409
    citizen15 "Я сегодня познакомился с отличной чикой..."
    citizen15 "И она уже готова раздвинуть передо мной ноги."
    imgd 12410
    m "К делу!"
    m "Меня не интересуют подробности твоей личной жизни!"
    m "!!!"
    imgd 12411
    citizen15 "А ты нетерпеливая, крошка..."
#    sound Jump1
    img 40338
    w
    # подмигивает Монике
    imgf 40339
    citizen15 "В общем, я договорился о встрече с ней."
    citizen15 "Но тут такое дело... Мне некуда ее вести."
    citizen15 "Обычно я делал это на хате одной моей телки."
    imgd 12474
    citizen15 "Но потом ей надоело, что я трахаю в этой хате не только ее."
    citizen15 "Теперь она не пускает меня туда. Йо!"
    citizen15 "Мне нужно место на пару часов..."
    imgd 12440
    m "А я здесь при чем?!"

    if monicaCitizensPunksBlowjob1 == True:
        # если Моника приводила домой панков
        imgf 13768
        citizen15 "Мне два чувака сказали, что у тебя есть хата..."
        citizen15 "Которую тебе арендует твой сутенер."
        citizen15 "Ты их знаешь. Тим и Том."
        $ notif(_("Моника приводила в свои апартаменты в трущобах Тима и Тома."))
        music Power_Bots_Loop
        img 13775 hpunch
        m "Что?!"
        m "!!!"
        m "Два придурка! Идиоты!"
        m "Это все неправда!!!"
        music Groove2_85
        imgd 13776
        citizen15 "Да ладно тебе, Бэби!"
        citizen15 "Ты чего так распереживалась?"
        img 13778
        m "!!!"
        imgd 13779
        citizen15 "Ну так что?"
    #

    imgd 13789
    citizen15 "У тебя нет места, куда можно будет привести мою подругу?"
    citizen15 "Я заплачу за аренду!"
    imgd 40340
    m "Заплатишь за аренду?"
    citizen15 "Да. Аренда на два часа. И я все оплачу."
    m "..."
    $ menu_corruption = [slumsCitizen15Option1]
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                imgf 40333
                mt "Хммм..."
                mt "Деньги за аренду места..."
                mt "..."
                mt "Черт! Но мне некуда его вести!"
                #
                $ notif(t_("Монике некуда вести клиентов."))
                #
                imgd 12471
                m "Мне некуда тебя вести!"
                imgf 12411
                citizen15 "Жаль, Бэби..."
                citizen15 "Могла бы немного подзаработать..."
                return -2
            # если арендует квартиру у Джека
            $ monicaCitizens15Slums1 = True # Моника согласилась сдать апартаменты в аренду парню в синей куртке и его подруге
            pass
        "Мой дом не место для каких-то проституток с улицы!":
            music Pyro_Flow
            imgd 40333
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            img 13771
            m "Нет!"
            m "Мой дом не место для каких-то проституток с улицы!"
            music Groove2_85
            imgd 13772
            citizen15 "Жаль, Бэби..."
            citizen15 "Могла бы немного подзаработать..."
            return -2
    # Моника в сомнениях
    music Groove2_85
    imgf 40333
    mt "Хммм..."
    mt "Деньги за аренду моих апартаментов всего на два часа..."
    mt "Это намного лучше, чем танцевать у пилона перед каким-нибудь никчемным неудачником."
    mt "А мне нужны деньги..."
    mt "..."
    menu:
        "Сколько ты мне заплатишь?":
            pass
    imgd 13773
    m "Сколько ты готов заплатить за аренду?"
    imgf 12417
    citizen15 "Бэби, я тебе щедро заплачу."
    citizen15 "Целых $ 10, крошка."
    imgd 40341
    m "Десять долларов?!"
    imgf 40342
    citizen15 "Да, Бэби! Я же сказал, что буду щедр с тобой!" # подмигивает
    imgd 40343
    w
    imgd 11940
    m "..."
    imgd 40344
    mt "Вот дьявол!"
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."
    mt "Эта дыра, которую я снимаю, стоит непомерно дорого."
    # выглядывает мамочка
    music Master_Disorder
    img 24343 vpunch
    mt "И эта старая карга следит за мной..."
    imgd 24344
    w
    if ep214_perry_debt > 0:
        #
        $ notif(_("Моника должна выплачивать Перри долг в размере $ 50 000."))
        imgd 19174
        mt "Я должна выплачивать долг этой мерзкой извращенке Перри!"
        #
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 19044
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    music Groove2_85
    imgf 12416
    m "Два часа аренды и ни минутой больше!"
    citizen15 "Без проблем, крошка."
    citizen15 "Говори адрес."
    # затемнение, спустя некоторое время
    # стук в дверь, звук открывающейся двери
    # апартаменты Моники
    # Моника, чувак в синей куртке и покупательница с магазина стоят в гостиной у Моники
    # подруга чувака огрядывается с пренебрежительным видом
    fadeblack 1.5
    call ep211_quests_slums_apartments2_check_enter_forced() from _rcall_ep211_quests_slums_apartments2_check_enter_forced # Моника входит в апартаменты (смена одежды)
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_70
    scene black_screen
    with Dissolve(1)
    sound snd_door_knock
    pause 1.5
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    imgfl 40345
    w
    imgf 40346
    mt "Это и есть его подруга?!"
    # если Моника работала манекеном в магазине
    if monicaAgreedToSellDress == True:
        #
        $ notif(_("Моника работала манекеном в магазине одежды."))
        #
        imgd 40346
        mt "Где-то я уже видела эту особу..."
        mt "Только где?"
        mt "Хммм..."
        mt "Может, на точке проституток?"
        mt "Хотя, нет..."
        mt "Тогда где?.."
        mt "..."
        music Pyro_Flow
        img 40347
        mt "Вот черт!"
        mt "Она была в этом отвратительном магазине одежды!"
        mt "И отказалась покупать у меня платье!"
        imgd 40448
        mt "Точно, она требовала скидку! Жадная сучка!"
        mt "Надеюсь, она меня не вспомнит!"
        imgd 40348
        mt "С другой стороны, какая разница?"
        mt "Она все равно не знает, кто я такая на самом деле."
        mt "!!!"
    #
    music Stealth_Groover
    imgd 40349
    mt "Кошмар!"
    mt "Она больше похожа на его мамочку или тетю!"
    mt "Пришла с этим никчемным неудачником сюда..."
    mt "Чтобы заниматься всякими извращенскими штуками!"
    imgd 40350
    mt "А строит из себя приличную даму! Фи!"
    mt "Моника, такой изысканной леди, как ты, не место среди этих мерзких существ!"
    mt "!!!"
    music Groove2_85
    imgf 40351
    cit7 "Это что за приют для бездомных?"
    cit7 "Какого хрена ты меня сюда привел?!"
    cit7 "Я думала, что мы сначала хотя бы посидим в кафе!"
    # парень ведет себя очень самоуверенно, приобнимает ее за талию
    music Marty_Gots_a_Plan
    imgd 40352
    citizen15 "Эй, детка, полегче!"
    citizen15 "Я снял эти апартаменты специально для нас с тобой!"
    imgd 40353
    citizen15 "К чему тратить время на кафе?"
    citizen15 "Мы и тут можем неплохо посидеть!"
    imgf 40354
    citizen15 "Смотри, тут даже мохито есть! Специально для тебя, крошка!"
    music Pyro_Flow
    img 40355
    m "Это мой мохито!"
    m "Я не для вас его делала!"
    m "Если выпьете, стоимость аренды увеличится!"
    m "!!!"
    music Groove2_85
    imgf 40356
    cit7 "А я не хочу мохито!"
    cit7 "Я, может быть, что-то другое хотела бы выпить!"
    imgd 40357
    citizen15 "Эй, хватит капризничать, детка!"
    # подруга подозрительно смотрит на Монику
    imgf 40358
    cit7 "И вообще, это кто такая?!"
    cit7 "Что она тут делает?!"
    imgd 40359
    citizen15 "Это официантка, которая убирает эти апартаменты и обслуживает постояльцев!"
    music Power_Bots_Loop
    img 40360 hpunch
    m "ЧТО???"
    m "КТО Я???"
    # если Моника работала манекеном в магазине
    if monicaAgreedToSellDress == True:
        #
        $ notif(_("Моника работала манекеном в магазине одежды."))
        #
        music Groove2_85
        imgd 40361
        cit7 "Я тебя вспомнила! Ты же работала в магазине одежды манекеном..."
        cit7 "Предлагала купить платье, которое было на тебе..."
        m "Да, и что с этого?!"
        imgd 40362
        cit7 "Так ты живешь в этой помойке?! Кошмар!"
        cit7 "Хорошо, что я не купила то платье!"
        imgd 40363
        cit7 "Его пришлось бы сразу сдавать в химчистку после тебя!"
        cit7 "Здесь у тебя, наверное, даже душа нет!"
        music Stealth_Groover
        imgd 40364
        m "Да, хорошо, что не купила..."
        m "Это платье хорошо сидит только на такой идеальной фигуре, как у меня."
        m "На тебе оно ужасно смотрелось!"
        #
    # Моника зло на нее смотрит
    music Power_Bots_Loop
    img 40365
    mt "Дрянь!"
    mt "!!!"
    music Groove2_85
    imgd 40366
    citizen15 "Эй, девочки. Полегче."
    imgd 40367
    cit7 "А почему она так со мной разговаривает?!"
    music Marty_Gots_a_Plan
    citizen15 "Она тебе просто завидует, детка!"
    cit7 "Завидует?"
    imgf 40368
    citizen15 "Конечно!"
    citizen15 "Ведь на твоем месте сейчас мечтает оказаться любая девочка из этого района!"
    imgd 40369
    citizen15 "Обо мне мечтают все чики! Даже такая, как эта!" # указывает на Монику
    # Моника недовольно на него смотрит
    img 40370
    m "..."
    imgd 40371
    citizen15 "Ну? Чего молчишь, Бэби?"
    citizen15 "Ты ведь мечтаешь сейчас оказаться на ее месте?"
    citizen15 "Хотела бы уединиться с таким брутальным мужчиной, как я?"
    music Power_Bots_Loop
    img 40372 vpunch
    m "ЧТО??? Я???"
    # он подходит к Монике и шепчет ей на ухо и Моника отвечат так, что девушка не слышит
    music Groove2_85
    imgf 32497
    sound man_steps
    w
    imgd 40373
    citizen15 "Слушай, чика, если ты скажешь моей подруге, что я тебе нравлюсь..."
    citizen15 "И вообще сделаешь так, чтобы она мне сегодня дала..."
    music Pyro_Flow
    img 40374
    m "С чего я еще должна что-то говорить твоей подруге и что-то делать?!"
    m "Достаточно того, что ты арендуешь место в моих апартаментах!"
    m "!!!"
    music Groove2_85
    imgd 40375
    citizen15 "Полегче, Бэби! Дослушай меня сначала..."
    citizen15 "Если ты это сделаешь, я тебе вместо десяти баксов заплачу 100! Йо!"
    m "Сто долларов?!"
    citizen15 "Да."
    imgd 40376
    mt "..."
    $ menu_corruption = [0, slumsCitizen15Option2]
    menu:
        "Я не собираюсь говорить этого!":
            music Stealth_Groover
            imgd 40377
            mt "Какие же они оба мерзкие!"
            mt "Моника, ты собралась отдать свою постель этим людишкам?!"
            imgd 40378
            mt "Чтобы они занимались своими грязными извращениями на ней?!"
            mt "Ты в своем уме?!"
            mt "?!?!?!"
            # Моника зло
            imgf 40379
            m "Нет!"
            m "Я мечтаю о том, чтобы вы оба убрались отсюда!"
            imgd 40380
            citizen15 "Эй, крошка!"
            citizen15 "Ты чего?! Мы так не договаривались!"
            music Pyro_Flow
            img 40381
            m "Я передумала!"
            m "Вон отсюда!"
            # парень смотрит на свою подругу
            music Marty_Gots_a_Plan
            imgf 40382
            citizen15 "Детка, я тут подумал..."
            citizen15 "Почему бы нам не пойти в кафе?"
            imgd 40383
            cit7 "Пошли."
            cit7 "Я не собираюсь больше ни минуты оставаться в этой жуткой квартире!"
            imgd 40384
            cit7 "Где ты вообще нашел эту козу?!" # указывает на Монику
            music Pyro_Flow
            img 40385 hpunch
            m "Это Я коза?!"
            m "ВОН ОТСЮДА!!!"
            m "БЫСТРО!!!"
            m "!!!"
            # парочка уходит
            fadeblack 1.5
            music Groove2_85
            imgfl 40386
            sound highheels_short_walk
            # если Моника работала манекеном в магазине
            if monicaAgreedToSellDress == True:
                cit7 "Всего лишь продавщица..."
                cit7 "Даже не продавщица, а манекен!"
                cit7 "А ведет себя так, как-будто она бизнес-леди какая-нибудь!"
                cit7 "Даже смешно!"
            else:
                cit7 "Хорошо, что мы уходим отсюда..."
                cit7 "Мне не нравится, как эта девка смотрит на тебя."
            citizen15 "Не обращай на нее внимания, крошка."
            citizen15 "Она тебе просто завидует! Йо!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 2.0
            music Stealth_Groover
            imgf 40387
            mt "Грязные трущобные жители!"
            mt "Невоспитанные!"
            mt "Мерзкие!"
            mt "!!!"
            return -3
        "Сказать, что он нравится Монике.":
            $ monicaCitizens15Slums2 = True # Моника сказала, что ей нравится парень в синей куртке при его подруге
            pass
    # Моника зло
    music Hidden_Agenda
    imgf 40378
    mt "Какие же они оба мерзкие! Фу!"
    mt "Но если я сейчас не подыграю этому никчемному неудачнику..."
    mt "Он не заплатит мне деньги... Целых $ 100..."
    imgd 40377
    mt "..."
    mt "Черт! Мне нужны эти сто долларов! Они уже мои!!!"
    imgf 40388
    m "..."
    m "Да, я мечтаю побыть с ним как-нибудь..."
    music Groove2_85
    cit7 "Серьезно?!"
    cit7 "И что тебе мешает?"
    m "Я..."
    citizen15 "Эта чика в очереди. Она ждет, когда у меня выдастся свободный вечер дня нее."
    imgd 40387
    mt "Придурок!"
    #
    $ notif(_("Моника танцевала у пилона за деньги."))
    #
    music Marty_Gots_a_Plan
    imgf 40389
    citizen15 "Да, эта чика мне даже свою задницу показывала!"
    citizen15 "Чтобы я обратил на нее внимание!"
    # подруга в сомнениях смотрит на Монику
    imgd 40390
    cit7 "Да ладно!"
    cit7 "Не может быть!"
    citizen15 "Да, это так."
    # обращается к Монике
    imgd 40391
    citizen15 "Да, Бэби?" # смотрит на Монику
    # Моника недовольно
    music Groove2_85
    imgd 40392
    mt "Черт!"
    mt "Сто долларов, Моника!"
    mt "Всего лишь за то, что ты подыграешь этому самовлюбленному идиоту..."
    imgd 40393
    m "Да!"
    # парень горделиво
#    music Marty_Gots_a_Plan
    music Loved_Up
    imgf 40394
    citizen15 "Вот видишь, детка, как тебе повезло сегодня."
    # подружка смущенно хихикает и смотрит на него
    citizen15 "Ты узнаешь, как это - быть в постели с настоящим мужчиной!" # показательно хватает себя за причиндалы
    imgd 40395
    citizen15 "Хочешь поскорее увидеть моего питона, детка?"
    citizen15 "Я знаю, ты мечтаешь об этом."
    # он притягивает свою подружку к себе и начинает лапать, она хихикает, но не сопротивляется
    # Моника недовольно смотрит на них
    imgf 40396
    w
    imgd 40397
    w
    imgf 40398
    w
    music Groove2_85
    imgd 40399
    mt "Их что, совсем не смущает, что они тут не одни?!"
    mt "Кошмар!"
    mt "Но мне сначала надо забрать свои деньги."
    imgd 40400
    m "Так, стоп!"
    m "Отдавай мне мои деньги, а потом занимайтесь тут своими гадостями!"
    imgd 40401
    citizen15 "Эй, Бэби, подожди, не торопись..."
    citizen15 "Может, сделаешь нам пару коктейлей мохито?"
    # его подруга тем временем встает перед ним на колени и трогает его хозяйство
    img 40402
    m "Какой еще мохито?!"
    m "Я выполнила свою часть сделки!"
    m "Давай мне деньги!"
    # его подруга тем временем встает перед ним на колени и трогает его хозяйство
    imgd 40401
    cit7 "Фрэнк, какого черта она до сих пор тут?!"
    cit7 "Она что, собирается пялиться на нас?!"
    cit7 "Пусть выйдет!"
    imgd 32491
    citizen15 "Йо, чика, ты слышала?!"
    citizen15 "Оставь нас с этой крошкой наедине."
    citizen15 "Я с тобой позже расчитаюсь... За аренду места..."
    m "Я и не собиралась смотреть на эти ваши гадости!"
    m "Я подожду, когда ты мне заплатишь, на кухне!"
    # Моника недовольно на него смотрит и уходит на кухню
    sound snd_walk_barefoot
    imgf 32492
    w
    # на кухне стоит и ворчит на них
    fadeblack
    sound snd_walk_barefoot
    pause 2.0
    music Stealth_Groover
    imgf 32493
    mt "Мерзкие грязные людишки! Фи!"
    mt "Занимаются всякими непотребствами в МОИХ апартаментах!"
    mt "Никчемные и бесполезные отбросы общества!"
    mt "!!!"
    # голоса с гостиной
#    music Groove2_85
    img 32494 hpunch
    cit7 "ЧТО ЭТО ТАКОЕ?!"
    citizen15 "Это мой огромный питон, детка!"
    cit7 "ОГРОМНЫЙ?!"
    cit7 "ТЫ ОХРЕНЕЛ?!"
    citizen15 "Эй, Бэби, иди сюда!"
    imgd 32495
    mt "Черт! Это он мне?!"
    citizen15 "Чика, хватит делать вид, что ты не слышишь!"
    citizen15 "Иди к нам!"
    mt "Твою мать! Что этим человечишкам еще от меня нужно?!"
    # Моника заходит в гостиную, парень стоит без штанов
    # подруга стягивает с него штаны, а там корнишончик, она в шоке смотрит на него
    fadeblack 1.5
    sound snd_walk_barefoot
    pause 2.0
    music Groove2_85
    imgfl 40404
    w
    imgf 40405
    cit7 "Это что, член?!"
    cit7 "!!!"
    # начинает возмущаться
    sound Jump1
    imgd 40403
    cit7 "Ты издеваешься?!"
    cit7 "Кому такое вообще может нравится?!"
    img 40406
    cit7 "Ты говорил, что у тебя огромный член!"
    cit7 "А это что вообще такое?!"
    # Моника тоже смотрит на его член
    imgf 40407
    mt "Этот кретин все это время строил из себя самца..."
    mt "Который всем нравится..."
    mt "А у него в штанах маленький корнишончик!"
    mt "!!!"
    # парень остается спокойным
    imgd 40409
    w
    music Marty_Gots_a_Plan
    imgd 40408
    citizen15 "Детка, он тебе только кажется маленьким...#it"
    citizen15 "Его надо взять в руки и ты поймешь, какой он огромный на самом деле!"
    # подруга смотрит на него недоверчиво, потом на Монику
    img 40410
    cit7 "Такое не может показаться огромным!"
    citizen15 "Может. Попробуй, детка."
    # подруга смотрит на Монику
    cit7 "Я не собираюсь трогать такую смешную вещь!"
    imgd 40411
    citizen15 "Эй, чика! Потрогай его!#it"
    citizen15 "Скажи, что на ощупь он огромный! Йо!#it"
    music Pyro_Flow
    img 40412
    m "Что?!"
    m "Я?!"
    m "С какой стати?!"
    m "!!!"
    music Groove2_85
    imgd 40413
    cit7 "Да. Если ты сейчас возьмешь его в руку и скажешь, что он огромный...#it"
    cit7 "Тогда я поверю."
    cit7 "Иначе я ухожу отсюда!"
    music Marty_Gots_a_Plan
    imgd 40414
    citizen15 "Эй, Бэби, давай сделай это."
    citizen15 "Скажи этой детке, что у меня огромный член."
    citizen15 "А потом я с тобой расплачусь, как договаривались."
    img 40415
    mt "!!!"
    $ menu_corruption = [0, slumsCitizen15Option3]
    menu:
        "Я не собираюсь делать этого!":
            music Stealth_Groover
            imgd 40387
            mt "Какие же они оба мерзкие!"
            mt "Моника, ты собралась отдать свою постель этим людишкам?!"
            mt "Чтобы они занимались своими грязными извращениями на ней?!"
            mt "Ты в своем уме?!"
            mt "?!?!?!"
            # Моника зло
            img 40416 vpunch
            m "Нет! Я не собираюсь делать этого!"
            m "Уходите оба отсюда! Аренда отменяется!"
            #music Groove2_85
            imgd 40417
            citizen15 "Эй, крошка!"
            citizen15 "Ты чего?! Мы так не договаривались!"
            m "Я передумала!"
            # парень смотрит на свою подругу
            music Marty_Gots_a_Plan
            imgf 40418
            citizen15 "Детка, я тут подумал..."
            citizen15 "Почему бы нам не пойти в кафе?"
            music Groove2_85
            imgd 40419
            cit7 "Я никуда с тобой не пойду!"
            # встает и направляется к выходу
            sound highheels_short_walk
            imgf 40420
            cit7 "Я не собираюсь больше ни минуты оставаться в этой жуткой квартире!"
            cit7 "И тем более, прикасаться к твоему отростку!"
            cit7 "Пошел к черту!"
            # если Моника работала манекеном в магазине
            if monicaAgreedToSellDress == True:
                cit7 "Пусть этот манекен тебя держит за твою смешную штуку!"
                cit7 "Она же так этого хочет! Ха-ха!"
                cit7 "Придурки!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 2.0
            # уходит
            label ep216_dialogues3_citizens_1a:
                pass
            # парень стоит со спущенными штанами, Моника напротив него
            music Groove2_85
            imgfl 40421
            citizen15 "Эй, чика!"
            citizen15 "Смотри, что ты натворила!"
            citizen15 "Эта детка ушла!"
            citizen15 "Мы же договорились, что ты мне подыграешь!"
            imgf 40423
            m "Мы договаривались, что я скажу ей, что ты мне нравишься..."
            m "А то, что я должна прикасаться к тебе!"
            m "Этого не было в нашем соглашении!"
            imgd 40424
            m "Так что я выполнила свою часть! Давай мои деньги!"
            imgd 40422
            citizen15 "Ничего ты не выполнила!"
            citizen15 "У меня обломался секс с такой аппетитной чикой из-за тебя!"
            imgd 40425
            citizen15 "Теперь тебе придется отрабатывать самой эти деньги, Бэби!"
            citizen15 "Так что, давай, приступай!"
            music Pyro_Flow
            img 40426 vpunch
            m "Отрабатывать?!"
            m "!!!"
            music Groove2_85
            imgf 40427
            citizen15 "Да, накину тебе еще 10 баксов."
            citizen15 "Всего $ 20 за отработку!"
            citizen15 "Легкие деньги, чика! Йо!"
            imgd 40428
            m "Я не собираюсь этого делать!"
            m "!!!"
            imgf 40429
            citizen15 "Эй, Бэби, никто не узнает!"
            citizen15 "Мы же у тебя на хате, нас никто не видит!"
            music Marty_Gots_a_Plan
            imgd 40430
            citizen15 "Я знаю, мой питон понравился тебе!"
            citizen15 "Он нравится таким чикам, как ты!#it"
            img 40431
            mt "Боже, какой идиот!"
            mt "!!!"
            imgd 40432
            citizen15 "Чего ты молчишь?"
            citizen15 "Если откажешься, то я тебе вообще ничего не заплачу, Бэби."
            citizen15 "А если отсосешь у меня - 20 баксов будут твои."
            mt "..."
            $ menu_corruption = [0, slumsCitizen15Option4]
            menu:
                "Я не собираюсь делать этого!":
                    music Pyro_Flow
                    img 40433 vpunch
                    mt "ЧТО?!"
                    mt "Он в своем уме?!"
                    mt "Я еще не опустилась до такой степени!"
                    mt "Грязное похотливое животное!"
                    mt "!!!"
                    # Моника зло
                    img 40435
                    m "Нет! Засовывай свой корнишончик обратно в штаны и убирайся!"
                    citizen15 "Эй!"
                    m "Иди отсюда! Можешь засунуть свои сто баксов себе в одно место!"
                    imgd 40436
                    m "Твой корнишончик сегодня невостребован!"
                    m "Вон отсюда!"
                    imgd 40437
                    citizen15 "Видимо, так тебе нужны деньги..."
                    img 40438 hpunch
                    m "ВОН ОТСЮДА!!!"
                    m "БЫСТРО!!!"
                    m "!!!"
                    # парень уходит
                    sound man_steps
                    imgf 40439
                    mt "Сволочь!"
                    mt "Мерзкий отброс общества!"
                    mt "Ненавижу эти трущобы и каждого его жителя!!!"
                    mt "!!!"
                    fadeblack
                    sound snd_door_open1
                    pause 1.5
                    sound snd_door_locked1
                    pause 2.0
                    return -4
                "Мне нужны деньги. (in Extra version) (disabled)" if game.extra != True:
                    pass
                "Мне нужны деньги." if game.extra == True:
                    music Pyro_Flow
                    imgd 40433
                    mt "Мне противно даже думать о том, что я буду прикасаться к его грязному отростку!"
                    mt "Я, Моника Бакфетт, леди из высшего общества..."
                    mt "И какой-то грязный отброс из трущоб! Фу!"
                    mt "Кошмар!"
                    mt "!!!"
                    music Hidden_Agenda
                    imgd 40434
                    mt "С другой стороны..."
                    mt "Из-за этой старой карги я не могу ничего заработать на улице!"
                    mt "А $ 20 не будут для меня лишними..."
                    mt "Об этом все равно никто не узнает."
                    mt "А мне чем-то надо платить за эту дыру!"
                    mt "..."
                    music Groove2_85
                    imgf 40440
                    m "Только быстро!"
                    m "И покажи мне деньги!"
                    # парень показывает купюру
                    sound vjuh3
                    imgd 40441
                    citizen15 "Давай, Бэби."
                    citizen15 "Просто возьми его в свой ротик.#it"
                    citizen15 "И ты почувствуешь, какой он огромный.#it"
                    # Моника зло на него смотрит, потом встает на колени перед ним
                    imgf 40442
                    w
                    imgd 40436
                    w
                    fadeblack 1.5
                    music Groove2_85
                    imgf 40443
                    w
                    imgd 40444
                    citizen15 "Сначала подними свою майку, Бэби."
                    citizen15 "Хочу посмотреть на твои сиськи..."
                    img 40445
                    m "Нет! Достаточно того, что я сейчас тебе буду делать!"
                    citizen15 "Я доплачу $ 5 за твои голые сиськи."
                    imgd 40446
                    m "..."
                    m "Черт!"
                    menu:
                        "Поднять майку.":
                            pass
                    # Моника обнажает грудь
                    imgf 40447
                    mt "Животное!"
                    mt "!!!"
                    sound Jump2
                    imgd 32498
                    citizen15 "Да, крошка..."
                    citizen15 "Сиськи у тебя ничего так..."
                    citizen15 "Теперь открывай свой ротик."
                    imgf 32504
                    mt "Интересно, этот никчемный придурок действительно считает..."
                    mt "Что о его смешном корнишончике мечтают все?"
                    mt "Какая ни на чем не основанная самоуверенность!"
                    citizen15 "Эй, чика, ты чего тормозишь?"
                    citizen15 "Моему питону уже не терпится попробовать твой ротик! Йо!"
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 32499
                    w

                    $ localSoundVolume = 0.75
                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob1_1.ogg"
                    scene black
                    image videov_Monica_Citizen15_Blowjob1_1 = Movie(play="video/v_Monica_Citizen15_Blowjob1_1.mkv", fps=30)
                    show videov_Monica_Citizen15_Blowjob1_1
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 32500
                    citizen15 "Вау... Отличный горячий ротик."

                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob1_1.ogg"
                    scene black
                    image videov_Monica_Citizen15_Blowjob1_2 = Movie(play="video/v_Monica_Citizen15_Blowjob1_2.mkv", fps=30)
                    show videov_Monica_Citizen15_Blowjob1_2
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 32501
                    w

                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob1_1.ogg"
                    scene black
                    image videov_Monica_Citizen15_Blowjob1_3 = Movie(play="video/v_Monica_Citizen15_Blowjob1_3.mkv", fps=30)
                    show videov_Monica_Citizen15_Blowjob1_3
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 32502
                    citizen15 "Ммммм..."
                    imgf 32503
                    citizen15 "Соси мой огромный член!"
                    music Loved_Up2
                    imgd 32505
                    citizen15 "Давай, детка..."

                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob1_1.ogg"
                    scene black
                    image videov_Monica_Citizen15_Blowjob1_4 = Movie(play="video/v_Monica_Citizen15_Blowjob1_4.mkv", fps=30)
                    show videov_Monica_Citizen15_Blowjob1_4
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 32506
                    w
                    sound lick3
                    imgd 32507
                    w
                    sound lick3
                    imgd 32506
                    w
                    sound lick3
                    imgd 32507
                    w
                    sound lick3
                    imgd 32506
                    w
                    sound lick3
                    imgd 32507
                    w
                    sound lick3
                    imgd 32506
                    w
                    sound lick3
                    imgd 32507
                    w

                    img black_screen
                    with diss
                    stop music2
                    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music")
                    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob1_1.ogg"
                    scene black
                    image videov_Monica_Citizen15_Blowjob1_5 = Movie(play="video/v_Monica_Citizen15_Blowjob1_5.mkv", fps=30)
                    show videov_Monica_Citizen15_Blowjob1_5
                    with fade
                    wclean
                    stop music2
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 32507
                    citizen15 "Оооо..."
                    imgf 32508
                    citizen15 "Как Бэби старательно сосет! Да!"
                    citizen15 "Я сейчас кончу, Бэби!"
                    menu:
                        "Кончить в рот Моники.":
                            $ monicaCitizen15SlumsCumZone1 = 1
                            # кончает Монике в рот
                            img 32509
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            citizen15 "МММММ!"
                            citizen15 "ОООООХ!!!"
                            citizen15 "ОООО..."
                            img 32510
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan8
                            w
                            # Моника зло смотрит на него
                            fadeblack 1.5
                            music Pyro_Flow
                            imgf 32511
                            w
                            imgd 32512
                            mt "ФУУУ!!!"
                            mt "Как это мерзко!"
                            mt "!!!"
                            pass
                        "Кончить на лицо Моники.":
                            $ monicaCitizen15SlumsCumZone1 = 2
                            # кончает Монике на лицо
                            img 32513
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan8
                            citizen15 "АААААААА!!!"
                            citizen15 "КААААЙФ!!!"
                            citizen15 "ДАААА..."
                            music stop
                            pause 1.0
                            # Моника зло смотрит на него
                            imgd 32514
                            sound hlup19
                            w
                            music Loved_Up2
                            imgd 32515
                            mt "ФУУУ!!!"
                            mt "Как это мерзко!"
                            mt "!!!"
                            pass
                        "Кончить на грудь Моники.":
                            $ monicaCitizen15SlumsCumZone1 = 3
                            # кончает Монике на грудь
                            img 32513
                            sound bulk1
                            show screen photoshot_screen()
                            with hpunch
                            pause 0.7
                            hide screen photoshot_screen
                            sound man_moan8
                            citizen15 "АААААААА!!!"
                            citizen15 "КААААЙФ!!!"
                            citizen15 "ДАААА..."
                            music stop
                            pause 1.0
                            # Моника зло смотрит на него
                            imgd 32516
                            sound hlup19
                            w
                            fadeblack 1.5
                            music Loved_Up2
                            imgf 32517
                            mt "ФУУУ!!!"
                            mt "Как это мерзко!"
                            mt "!!!"
                            pass
                    # затемнение
                    # парень стоит одетый
                    fadeblack
                    sound snd_fabric1
                    pause 2.0
                    music Groove2_85
                    imgf 32519
                    citizen15 "Вау, Бэби!"
                    citizen15 "Я не ожидал, но мне понравилось!"
                    imgd 32518
                    m "!!!"
                    m "Давай мне мои $ 25!"
                    citizen15 "Держи, крошка..."
                    $ add_money(25.0)
                    music Marty_Gots_a_Plan
                    imgd 32520
                    citizen15 "Когда найду себе детку посговорчивее моей сегодняшней подруги..."
                    citizen15 "То обращусь к тебе..." # подмигивает
                    m "Все! Иди отсюда!"
                    fadeblack
                    sound snd_door_open1
                    pause 1.5
                    sound snd_door_locked1
                    pause 2.0
                    music Pyro_Flow
                    # парень уходит
                    imgf 32521
                    mt "Сволочь!"
                    mt "Мерзкий отброс общества!"
                    mt "Ненавижу эти трущобы и каждого его жителя!!!"
                    mt "!!!"
                    $ add_corruption(20, "citizen15_blowjob_alone")
                    $ monicaCitizens15Slums3 = True # Моника делала минет парню в синей куртке, т.к. его подруга ушла
                    return 1
        "Взять в руку его член.":
            pass
    # Моника в сомнениях
    music Pyro_Flow
    imgf 40378
    mt "Мне противно даже думать о том, что я буду прикасаться к его грязному отростку!"
    mt "Я, Моника Бакфетт, леди из высшего общества..."
    mt "И какой-то грязный отброс из трущоб! Фу!"
    mt "Кошмар!"
    mt "!!!"
    music Hidden_Agenda
    imgd 32522
    mt "С другой стороны... Сто долларов..."
    mt "Они не будут для меня лишними..."
    mt "Мне ведь нужно будет просто сказать, что его корнишончик большой..."
    mt "Зато у меня станет на сто долларов больше."
    # Моника подходит к парню и садится рядом с его подругой перед ним, смотрят на его член
    fadeblack
    sound snd_walk_barefoot
    pause 2.0
    music Groove2_85
    imgfl 32523
    w
    imgf 32524
    cit7 "Видно же, что у него маленький отросточек..."
    cit7 "А строил из себя брутального самца!"
    imgd 32525
    mt "Потому что он придурок!"
    mt "!!!"
    # Моника берет в руку его член
    mt "Придурок с корнишончиком!"
    music Hidden_Agenda
    imgf 32526
    m "..."
    m "Это просто кажется, что он маленький...#it"
    m "Он у него просто огромный.#it"
    m "Попробуй."
    music Groove2_85
    # Моника убирает свою руку
    cit7 "Да ладно!" # удивленно
    # подруга тоже берет его в руку, потом возмущается
    imgd 32527
    w
    cit7 "Ничего подобного!"
    cit7 "Что за чушь?!"
    citizen15 "Эй, крошка! Ты что, не слышала, что сказала тебе эта Бэби?"
    citizen15 "Он ведь огромный!#it"
    music Hidden_Agenda
    m "..."
    m "Да..."
    music Groove2_85
    imgd 32528
    cit7 "Я не знаю, что за цирк вы тут устроили!"
    cit7 "Вообще то, я знаю твоего брата!" # указывает пальцем на парня
    cit7 "У него такой же маленький, как у тебя!"
    citizen15 "Нет! У меня не так!"
    cit7 "Именно так!"
    mt "Эта шлюха что, знает все члены в этих трущобах?"
    mt "Какой кошмар! Фи!"
    mt "!!!"
    imgd 32529
    citizen15 "А спорим, мой огромный член еле поместится во рту у этой чики?"
    music Power_Bots_Loop
    img 32530 hpunch
    m "Что?!"
    m "!!!"
    music Marty_Gots_a_Plan
    imgf 32529
    citizen15 "Ты же мечтаешь взять в рот его. Да, чика?#it"
    citizen15 "Ты давно уже хотела сделать это."
    citizen15 "Вот твой шанс. Воспользуйся им, Бэби!"
    citizen15 "Ну, давай же!"
    img 32530
    m "!!!"
    $ menu_corruption = [0, slumsCitizen15Option5]
    menu:
        "Я не собираюсь делать этого!":
            music Pyro_Flow
            imgd 40415
            mt "Он что, совсем охренел!?"
            mt "Чтобы Я брала его грязный отросток в свой рот?!"
            mt "!!!"
            # Моника зло
            img 40416
            m "Ты в своем уме, придурок?!"
            m "?!?!?!"
            m "Я не собираюсь делать этого!"
            m "И вообще!"
            m "Уходите оба отсюда! Аренда отменяется!"
            # отсюда вставить предыдущие арты, где они уже одетые
            imgd 40417
            citizen15 "Эй, крошка!"
            citizen15 "Ты чего?! Мы так не договаривались!"
            m "Я передумала!"
            # парень смотрит на свою подругу
            music Marty_Gots_a_Plan
            imgf 40418
            citizen15 "Детка, я тут подумал..."
            citizen15 "Почему бы нам не пойти в кафе?"
            music Groove2_85
            imgd 40419
            cit7 "Я никуда с тобой не пойду!"
            # встает и направляется к выходу
            sound highheels_short_walk
            imgf 40420
            cit7 "Я не собираюсь больше ни минуты оставаться в этой жуткой квартире!"
            cit7 "Тем более, с тобой!"
            cit7 "Пойду, найду себе чувака с нормальным членом!"
            cit7 "Пошел к черту!"
            # если Моника работала манекеном в магазине
            if monicaAgreedToSellDress == True:
                cit7 "Пусть этот манекен тебя держит за твою смешную штуку!"
                cit7 "Она же так этого хочет! Ха-ха!"
                cit7 "Придурки!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 2.0
            # уходит
            jump ep216_dialogues3_citizens_1a
        "Взять в рот его член.":
            pass
    # Моника медлит
    music Groove2_85
    imgd 32525
    mt "Черт!"
    mt "Моника!"
    mt "Из-за каких-то ста долларов!"
    mt "Не могу поверить, что ты собралась делать это!"
    mt "Еще и в присутствии этой курицы!"
    mt "!!!"
    # Моника наклоняется к нему и берет в рот его член
    # его подруга с интересом смотрит
    fadeblack 1.5
    music Groove2_85
    sound chpok6
    img 32531 hpunch
    w

    $ localSoundVolume = 0.75
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob2_1 = Movie(play="video/v_Monica_Citizen15_Blowjob2_1.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob2_1
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
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob2_2 = Movie(play="video/v_Monica_Citizen15_Blowjob2_2.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob2_2
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
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob2_3 = Movie(play="video/v_Monica_Citizen15_Blowjob2_3.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob2_3
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
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob2_4 = Movie(play="video/v_Monica_Citizen15_Blowjob2_4.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob2_4
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
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob2_5 = Movie(play="video/v_Monica_Citizen15_Blowjob2_5.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob2_5
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
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob2_6 = Movie(play="video/v_Monica_Citizen15_Blowjob2_6.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob2_6
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32532
    cit7 "Ну?"
    imgd 32531
    m "Мммм!"
    $ add_corruption(10, "citizen15_blowjob_group")
    music Marty_Gots_a_Plan
    imgf 32533
    citizen15 "Вот видишь, крошка, какой он большой!#it"
    citizen15 "Она им чуть не подавилась! Йо!"
    citizen15 "Да, чика?"
    # Моника отстраняется
    cit7 "И что? Хочешь сказать, что он большой?#it"
    imgd 32534
    m "..."
    menu:
        "Сказать, что он маленький.":
            music Pyro_Flow
            imgd 32535
            mt "Да пошел этот придурок со своим отростком к черту!"
            mt "!!!"
            # Моника зло
            fadeblack 1.5
            music Stealth_Groover
            imgf 40417
            m "Он настолько маленький, что я его даже не почувствовала!#it"
            m "!!!"
            citizen15 "Эй, крошка!"
            m "Да! Он маленький!#it"
            m "Просто крошечный!"
            music Groove2_85
            imgd 40419
            cit7 "Я так и знала!"
            cit7 "Обманщик!!!"
            img 40416
            m "И вообще!"
            m "Уходите оба отсюда! Аренда отменяется!"
            citizen15 "Ты чего?! Мы так не договаривались!"
            m "Я передумала!"
            # парень смотрит на свою подругу
            music Marty_Gots_a_Plan
            imgd 40418
            citizen15 "Детка, я тут подумал..."
            citizen15 "Почему бы нам не пойти в кафе?"
            music Groove2_85
            cit7 "Я никуда с тобой не пойду!"
            # встает и направляется к выходу
            sound highheels_short_walk
            imgf 40420
            cit7 "Я не собираюсь больше ни минуты оставаться в этой жуткой квартире!"
            cit7 "Тем более, с тобой!"
            cit7 "Пойду, найду себе чувака с нормальным членом!"
            cit7 "Пошел к черту!"
            # если Моника работала манекеном в магазине
            if monicaAgreedToSellDress == True:
                cit7 "Пусть этот манекен тебя держит за твою смешную штуку!"
                cit7 "Она же так этого хочет! Ха-ха!"
                cit7 "Придурки!"
            fadeblack
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 2.0
            # уходит
            jump ep216_dialogues3_citizens_1a
        "Сказать, что он огромный.":
            pass
    music Hidden_Agenda
    imgf 32535
    mt "Я сейчас скажу, что он большой...#it"
    mt "Только чтобы эти двое отстали от меня!"
    mt "И заберу у этого придурка свои деньги!"
    mt "Мне уже надоел весь этот цирк!"
    imgd 32536
    m "..."
    m "Он у него огромный...#it"
    cit7 "Да ну?!"
    cit7 "Правда?!"
    m "Да... Еле поместился у меня во рту..."
#    music Groove2_85
    citizen15 "Вот видишь, крошка!"
    citizen15 "Давай, попробуй сама..."
    # его подруга с интересом смотрит на его член
    # Моника встает
    fadeblack 1.5
    music Groove2_85
    imgfl 32537
    m "Давай мне деньги."
    m "И я оставлю вас вдвоем."
    m "Я уже выполнила нашу договоренность..."
    # он протягивает ей деньги
    music Marty_Gots_a_Plan
    $ add_money(100.0)
    imgf 32538
    citizen15 "Держи, Бэби..." # подмигивает
    citizen15 "Может, останешься с нами, м?"
    citizen15 "Я тебе доплачу за это немного..."
    citizen15 "Моя крошка не будет против, если ты останешься... Да?"
    # смотрит на свою подругу, она берет в рот его член
    imgd 32539
    w
    sound chpok6
    imgd 32540
    cit7 "Мммм..."
    imgf 32541
    citizen15 "Вот видишь, она не против..."
    citizen15 "Останешься?"
    m "..."
    menu:
        "Подождать на кухне, пока они закончат.":
            music Groove2_85
            imgd 32542
            mt "Ну уж нет!"
            mt "Я не собираюсь смотреть на их грязные извращенства!"
            mt "Но их одних в своих апартаментах я не оставлю!"
            mt "Мне нужно проконтролировать, что они ничего у меня не украли..."
            mt "Или не сломали..."
            # Моника встает, подруга сосет
            sound snd_walk_barefoot
            imgf 32543
            m "Я подожду на кухне."

            music Loved_Up
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(0.5, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Blowjob1_1.ogg"
            scene black
            image videov_Citizen15_ShopVisitor7_Blowjob1_1 = Movie(play="video/v_Citizen15_ShopVisitor7_Blowjob1_1.mkv", fps=30)
            show videov_Citizen15_ShopVisitor7_Blowjob1_1
            with fade
            wclean
            citizen15 "Если надумаешь - присоединяйся к нам." # подмигивает ей
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(0.5, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Blowjob1_1.ogg"
            scene black
            image videov_Citizen15_ShopVisitor7_Blowjob1_2 = Movie(play="video/v_Citizen15_ShopVisitor7_Blowjob1_2.mkv", fps=30)
            show videov_Citizen15_ShopVisitor7_Blowjob1_2
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")


            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(0.5, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Blowjob1_1.ogg"
            scene black
            image videov_Citizen15_ShopVisitor7_Blowjob1_3 = Movie(play="video/v_Citizen15_ShopVisitor7_Blowjob1_3.mkv", fps=30)
            show videov_Citizen15_ShopVisitor7_Blowjob1_3
            with fade
            m "Нет!"
            m "И аккуратнее тут с мебелью!"
            m "И не смейте трогать мой мохито!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")


            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(0.5, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Blowjob1_1.ogg"
            scene black
            image videov_Citizen15_ShopVisitor7_Blowjob1_4 = Movie(play="video/v_Citizen15_ShopVisitor7_Blowjob1_4.mkv", fps=30)
            show videov_Citizen15_ShopVisitor7_Blowjob1_4
            with fade
            citizen15 "Окей, чика!"
            citizen15 "Без проблем! Йо!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")



            # уходит на кухню
            # смена кадра, Моника стоит на кухне
            # с комнаты доносятся стоны
            fadeblack
            sound snd_walk_barefoot
            pause 2.0
            music Groove2_85
            imgf 32494
            citizen15 "Вау... Какая ты горячая, крошка..."
            citizen15 "Дай мне скорее свою киску!"
            cit7 "Ммммм..."
            cit7 "Ооох!!!"
            citizen15 "Давай, детка..."
            cit7 "Оооо..."
            citizen15 "Не так быстро, детка, а то я сейчас кончу..."
            citizen15 "Да, так... Оооо..."
            cit7 "Аааах..."
            # Моника злится
            imgd 32493
            mt "Долго они там собираются делать свои мерзости?!"
            mt "И вообще! Могли бы потише!"
            mt "Не у себя дома!"
            mt "!!!"
            menu:
                "Посмотреть, что они делают.":
                    music Hidden_Agenda
                    imgd 32495
                    mt "Черт!"
                    mt "Может посмотреть, чем они там занимаются?"
                    mt "Наверняка, они меня не увидят..."
                    # затемнение
                    $ monicaCitizens15Slums4 = True # Моника подсматривала за сексом Фрэнка и его подруги
                    pass
                "Не смотреть. Просто подождать.":
                    # спустя некоторое время
                    # Моника также стоит на кухне
                    music Pyro_Flow
                    imgd 32549
                    citizen15 "ООООО!!!"
                    citizen15 "КОНЧАЮЮЮЮ!!!"
                    cit7 "ААААА!!!"
                    # Моника недовольно
                    mt "!!!"
                    mt "Ну наконец-то!!!"
                    # затемнение, звук каблуков, спустя пять минут
                    # Моника выходит в гостиную, чувак с подругой уже одетые
                    scene black_screen
                    with Dissolve(1)
                    music stop
                    call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_71
                    scene black_screen
                    with Dissolve(1)
                    sound snd_walk_barefoot
                    pause 2.0
                    music Marty_Gots_a_Plan
                    imgfl 32544
                    w
                    imgf 32545
                    citizen15 "Эй, Бэби, зря не присоединилась к нам!" # подмигивает
                    citizen15 "Эта крошка на редкость горячая штучка!"
                    cit7 "Хи-хи-хи..."
                    citizen15 "Мы к тебе если что обратимся снова!"
                    music Groove2_85
                    img 32546
                    m "Еще чего!"
                    m "Хватит с вас одного раза!"
                    m "Все! Идите отсюда!"
                    # парень с подругой уходят
                    sound highheels_short_walk
                    imgf 32547
                    # если Моника работала манекеном в магазине
                    if monicaAgreedToSellDress == True:
                        cit7 "Пока, манекенчик! Хи-хи!"
                        m "!!!"
                    else:
                        cit7 "Наконец-то, я ухожу из этой грязной дыры!"
                        cit7 "И как ты здесь живешь?! Фу!"
                        m "!!!"
                    fadeblack
                    sound snd_door_open1
                    pause 1.5
                    sound snd_door_locked1
                    pause 2.0
                    music Pyro_Flow
                    imgf 32548
                    mt "Мерзкие отбросы общества!"
                    mt "Ненавижу эти трущобы и каждого его жителя!!!"
                    mt "!!!"
                    return -5
        "Выйти на улицу. (пропуск сцены)":
            music Pyro_Flow
            imgd 32542
            mt "Ну уж нет!"
            mt "Я не собираюсь смотреть на их грязные извращенства!"
            mt "Деньги я уже забрала."
            mt "Так что с меня достаточно!"
            # Моника встает, подруга сосет
            sound snd_walk_barefoot
            imgf 32543
            m "Нет!"
            m "У меня есть более важные дела!"
            music Loved_Up
            m "Когда я вернусь, чтобы вас обоих тут не было!"
            m "!!!"

            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(0.5, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Blowjob1_1.ogg"
            scene black
            image videov_Citizen15_ShopVisitor7_Blowjob1_1 = Movie(play="video/v_Citizen15_ShopVisitor7_Blowjob1_1.mkv", fps=30)
            show videov_Citizen15_ShopVisitor7_Blowjob1_1
            with fade
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

#            music Groove2_85
            imgf 32543
            citizen15 "Окей, чика!"
            citizen15 "Без проблем! Йо!"
            # Моника идет к выходу, оказывается на улице
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 1.0
            return -6
    # кадр на гостиную
    # парень и его подруга голые, она стоит раком, опершись о кушетку, он пристроился сзади
    fadeblack
    sound snd_walk_barefoot
    pause 2.0
    music Loved_Up
    imgfl 32550
    cit7 "Оооох... Ну давай уже!"
    citizen15 "Сейчас, детка... Я уже почти вошел..."
    imgf 32551
    citizen15 "Ох черт!"
    imgd 32552
    citizen15 "Сейчас, сейчас..."
    imgd 32553
    cit7 "Фрэнк, ну сколько можно?!"
    # он поворачивает голову в сторону и замечает Монику (Монику не показываем)
    music Marty_Gots_a_Plan
    imgf 32554
    citizen15 "Эй, Бэби!"
    citizen15 "Ты решила к нам присоединиться?!"
    citizen15 "Иди сюда, крошка!"
    citizen15 "Мне нужна твоя помощь!"
    # подруга тоже поворачивается
    imgd 32555
    cit7 "Сделай ты ему хоть что-нибудь, чтоб у него не выпадал!"
    cit7 "У него не хватает длины, чтобы держаться там!"
    cit7 "Он уже достал меня!"
    citizen15 "Чика, ну что ты там стоишь?"
    citizen15 "Хочешь еще немного заработать денежек?"
    citizen15 "Иди ко мне!"
    citizen15 "Ты же знаешь, я щедрый..."
    $ menu_corruption = [slumsCitizen15Option6]
    menu:
        "Подойти к ним.":
            pass
        "Выйти на улицу. (пропуск сцены)":
            # Моника заходит в гостиную
            music Pyro_Flow
            imgd 32546
            mt "Ну уж нет!"
            mt "Я не собираюсь смотреть на их грязные извращенства!"
            mt "Деньги я уже забрала."
            mt "Так что с меня достаточно!"
            img 32556
            m "Нет!"
            m "У меня есть более важные дела!"
            m "Когда я вернусь, чтобы вас обоих тут не было!"
            m "!!!"
            music Groove2_85
            imgd 32564
            citizen15 "Окей, чика!"
            citizen15 "Без проблем! Йо!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 2.0
            # Моника идет к выходу, оказывается на улице
            return -7
    # Моника заходит в гостиную, смотрит недовольно на парочку
    music Groove2_85
    imgf 32546
    mt "Чего ему от меня надо?"
    mt "???"
    mt "Он что-то сказал, про деньги..."
    mt "Это все, конечно, грязно и мерзко..."
    mt "Но он только за этот цирк перед его дурой-подругой заплатил мне $ 100..."
    music Hidden_Agenda
    imgd 32557
    mt "Может, я смогу еще немного заработать?"
    mt "Черт! Моника, не могу поверить, что для тебя такой способ заработка стал нормой..."
    mt "Но ничего... Это все временные трудности!"
    mt "Тем более, никто здесь не знает кто я такая."
    mt "А, значит, это делаю не Я!"
    music Groove2_85
    imgf 32558
    m "..."
    m "Чего тебе?"
    cit7 "У него все время падает!"
    cit7 "Я бы уже давно кончила и свалила бы отсюда к черту!"
    imgd 32559
    cit7 "Сколько уже можно это терпеть!"
    cit7 "Сделай что-нибудь!"
    citizen15 "Да, Бэби!"
    imgf 32560
    citizen15 "Моему дружку нужно немного твоего внимания!"
    citizen15 "Я я тебя щедро отблагодарю за это..."
    citizen15 "Что скажешь?"
    imgd 32558
    m "Насколько щедро?"
    citizen15 "Я тебе дам еще $ 30, чика."
    citizen15 "$ 30 за то, что ты подержишь моего дружка у себя во рту..."
    m "..."
    $ menu_corruption = [slumsCitizen15Option7]
    menu:
        "Взять его член в рот.":
            $ monicaCitizens15Slums5 = True # Моника согласилась сделать минет Фрэнку, когда он занимался сексом со своей подругой
            pass
        "Выйти на улицу. (пропуск сцены)":
            # Моника заходит в гостиную
            music Pyro_Flow
            imgd 32546
            mt "Ну уж нет!"
            mt "Я не собираюсь смотреть на их грязные извращенства!"
            mt "Деньги я уже забрала."
            mt "Так что с меня достаточно!"
            img 32556
            m "Нет!"
            m "У меня есть более важные дела!"
            m "Когда я вернусь, чтобы вас обоих тут не было!"
            m "!!!"
            music Groove2_85
            imgd 32564
            citizen15 "Окей, чика!"
            citizen15 "Без проблем! Йо!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 2.0
            # Моника идет к выходу, оказывается на улице
            return -8
    # Моника медлит
    music Hidden_Agenda
    imgf 32561
    mt "..."
    mt "$ 30..."
    mt "Зато они быстрее закончат и уберутся отсюда..."
    mt "А я заработаю еще денег..."
    mt "А что подумает обо мне эта особа?"
    mt "Получается, что я за деньги буду оказывать интимные услуги?"
    imgd 32562
    mt "С другой стороны..."
    mt "Она ведь сама меня просит помочь ему..."
    mt "Тем более, она все равно не знает, кто я такая на самом деле."
    # если Моника работала манекеном в магазине
    if monicaAgreedToSellDress == True:
        #
        $ notif(_("Моника работала манекеном в магазине одежды."))
        #
        mt "Она думает, что я просто какая-то никчемная продавщица в магазине одежды."
        #
    mt "Черт!"
    m "..."
    music Groove2_85
    imgd 32563
    cit7 "Да возьми ты у него в рот!"
    cit7 "Мы тут до ночи будем возиться с его отростком!"
    citizen15 "Да, давай!"
    citizen15 "Мой огромный член очень хочет в твой ротик, чика! Йо!"
    citizen15 "Но сначала подними свою майку, Бэби."
    citizen15 "Хочу посмотреть на твои сиськи..."
    img 32564
    m "Нет! Достаточно того, что я сейчас тебе буду делать!"
    citizen15 "Я доплачу $ 5 за твои голые сиськи."
    m "..."
    m "Черт!"
    menu:
        "Поднять майку.":
            pass
    # Моника обнажает грудь
    fadeblack 1.5
    music Groove2_85
    imgf 32565
    w
    sound vjuh3
    imgd 32566
    w
    imgf 32567
    w
    imgd 32568
    citizen15 "Да, крошка..."
    citizen15 "Сиськи у тебя ничего так..."
    citizen15 "Теперь открывай свой ротик."
    citizen15 "Иди скорее сюда!"
    # он поворачивается к Монике
    # она с отвращением на лице подходит к нему
    sound snd_walk_barefoot
    imgf 32569
    citizen15 "Да, крошка..."
    # опускается на колени перед ним
    fadeblack 1.5
    music Loved_Up
    imgfl 32570
    w
    imgf 32571
    mt "!!!"
    citizen15 "Теперь открывай свой ротик."
    # Моника берет в рот его член
    imgd 32572
    w
    fadeblack 1.5
    $ add_money(35.0)
    music Loved_Up
    sound2 chpok6
    img 32573 vpunch
    w

    $ localSoundVolume = 0.75
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob3_1 = Movie(play="video/v_Monica_Citizen15_Blowjob3_1.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob3_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    citizen15 "Вау... Отличный горячий ротик."
    imgd 32574
    w

    imgf 32576
    citizen15 "Ммммм..."
    imgd 32575
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob3_2 = Movie(play="video/v_Monica_Citizen15_Blowjob3_2.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob3_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32577
    cit7 "Мммм..."
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_ShopVisitor7_Masturbation1_1.ogg"
    scene black
    image videov_ShopVisitor7_Masturbation1_2 = Movie(play="video/v_ShopVisitor7_Masturbation1_2.mkv", fps=25)
    show videov_ShopVisitor7_Masturbation1_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound drkanje5
    imgd 32578
    w
    sound drkanje5
    imgd 32579
    w
    sound drkanje5
    imgd 32578
    w
    sound drkanje5
    imgd 32579
    w
    sound hlup25
    imgd 32580
    w
    imgf 32505
    citizen15 "Соси мой огромный член!"
    imgd 32581
    citizen15 "Давай, детка..."

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen15_Blowjob2_2.ogg"
    scene black
    image videov_Monica_Citizen15_Blowjob3_3 = Movie(play="video/v_Monica_Citizen15_Blowjob3_3.mkv", fps=30)
    show videov_Monica_Citizen15_Blowjob3_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound chpok6
    imgd 32582
    citizen15 "Оооо..."
    citizen15 "Как Бэби старательно сосет! Да!"

    imgf 32506
    w
    sound lick3
    imgd 32507
    w
    sound lick3
    imgd 32506
    w
    sound lick3
    imgd 32507
    w
    sound lick3
    imgd 32506
    w
    sound lick3
    imgd 32507
    w
    sound lick3
    imgd 32506
    w
    sound lick3

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_ShopVisitor7_Masturbation1_1.ogg"
    scene black
    image videov_ShopVisitor7_Masturbation1_1 = Movie(play="video/v_ShopVisitor7_Masturbation1_1.mkv", fps=25)
    show videov_ShopVisitor7_Masturbation1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32507
    citizen15 "Я сейчас кончу, Бэби!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,3))*2.0) + " loop 0.0>Sounds/v_ShopVisitor7_Masturbation1_1.ogg"
    scene black
    image videov_ShopVisitor7_Masturbation1_3 = Movie(play="video/v_ShopVisitor7_Masturbation1_3.mkv", fps=25)
    show videov_ShopVisitor7_Masturbation1_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32583
    citizen15 "О! Вставляй его скорее в эту киску!#it"
    imgd 32584
    w
    # подруга стоит в той же позе
    # Моника отстраняется от его члена
    # берет в руку и направляет в киску подружки, вставляет
    imgd 32585
    w
    imgf 32586
    w
    imgd 32587
    citizen15 "Да, чика, держи его так, чтобы он не выскочил!#it"
    $ add_corruption(10, "citizen15_blowjob_hold_dick")
    # Моника держит его член, он в это время пялит свою подругу
    imgf 32588
    w
    sound hlup25
    img 32589 hpunch
    w
    imgd 32590
    cit7 "О, дааа!!"
    imgd 32591
    mt "Боже, Моника, какого черта ты принимаешь участие в этом безумии?!"
    mt "Как ты могла согласиться на подобное?!"
    mt "?!?!?!"
    ## можно вставить мысли Моники о том, как она на это согласилась
    # потом тянет руку и лапает грудь Моники
    #m "!!!"
    #m "Что ты делаешь?!"
    #m "Какого черта ты меня лапаешь, придурок?!"
    #m "!!!"
    #citizen15 "Чтобы мой питон был еще больше! Йо!"
    #citizen15 "Когда я держу тебя за сиськи, он просто огромный!#it"
    #citizen15 "И не падает! Оооо!!!"
    # продолжает пялить свою подругу и держит Монику за грудь
    # Моника злая
    #mt "Гребаный неудачник!"
    #mt "Лапает меня своими грязными руками!"
    #mt "За мою прекрасную грудь!"
    #mt "!!!"
    music Loved_Up2
    imgf 32592
    citizen15 "ООООО!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_1 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_1.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32590
    cit7 "ААААА!!!"
    cit7 "Наконец-то!!! Да!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_2 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_2.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32594
    w
    imgd 32593
    citizen15 "Дааа, крошкаааа... Аааа!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_3 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_3.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_4 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_4.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32595
    citizen15 "Какие у меня клевые чикииии!!! Оооо!!!"
    imgd 32596
    w
    imgf 32597
    citizen15 "Мой питон стал просто огромным от вас!!! Дааа!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_5= Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_5.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_5
    with fade
    cit7 "Аааа!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_6 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_6.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_6
    with fade
    citizen15 "Тебе нравится, как мой огромный член заполняет твою киску?"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_7 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_7.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_7
    with fade
    cit7 "Дааа!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32598
    citizen15 "Аааааа!!!"
    citizen15 "Какие сиськи у тебя, чика!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Citizen15_ShopVisitor7_Sex2_1.ogg"
    scene black
    image videov_Citizen15_ShopVisitor7_Sex2_8 = Movie(play="video/v_Citizen15_ShopVisitor7_Sex2_8.mkv", fps=30)
    show videov_Citizen15_ShopVisitor7_Sex2_8
    with fade
    citizen15 "Когда-нибудь я трахну тебя между ними!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32599
    citizen15 "О, да!!!"
    citizen15 "Оооо!!!"
    menu:
        "Кончить в подругу Фрэнка.":
            $ monicaCitizen15SlumsCumZone2 = 1
            # оба кончают
            img 32600
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan11
            citizen15 "КОНЧАЮЮЮЮ!!!"
            cit7 "ДААААА!!!"
            img 32601
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan8
            citizen15 "МММММ!"
            imgf 32604
            cit7 "ААААА!!!"
            imgd 32602
#            citizen15 "ОООООХ!!!"
            citizen15 "ОООО..."
            # Моника зло смотрит на него
            imgd 32603
            mt "ФУУУ!!!"
            mt "Как это мерзко!"
            mt "!!!"
            pass
        "Кончить на попу подруги Фрэнка.":
            $ monicaCitizen15SlumsCumZone2 = 2
            # оба кончают
            img 32600
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan11
            citizen15 "ООООО!!!"
            cit7 "ААААА!!!"
            img 32605
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            citizen15 "КОНЧАЮЮЮЮ!!!"
            cit7 "ДААААА!!!"
            img 32606
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan8
            citizen15 "МММММ!"
            citizen15 "ОООООХ!!!"
            citizen15 "ОООО..."
            # Моника зло смотрит на него
            imgd 32607
            mt "ФУУУ!!!"
            mt "Как это мерзко!"
            mt "!!!"
            pass
        "Кончить на грудь Моники.":
            # кончает подруга Фрэнка
            img 32600
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan11
            citizen15 "ООООО!!!"
            cit7 "ААААА!!!"
            cit7 "ДААААА!!!"
            # она кончила, Фрэнк нет, он вытаскивает член из подурги и говорит Монике
            imgf 32608
            w
            imgd 32609
            citizen15 "Подставляй свои сиськи, чика! Быстро!"
            citizen15 "Еще $ 10 баксов!"
            img 32610
            citizen15 "МММММ!"
            citizen15 "КОНЧАЮЮЮЮ!!!"
            $ menu_corruption = [slumsCitizen15Option8]
            menu:
                "Подставить грудь.":
                    $ add_corruption(5, "citizen15_blowjob_cum_boobs")
                    $ monicaCitizen15SlumsCumZone2 = 3
                    # Моника подставляет грудь
                    img 32611
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen15 "ОООООХ!!!"
                    citizen15 "ОООО..."
                    $ add_money(10.0)
                    imgd 32612
                    w
                    # Моника зло смотрит на него
                    imgd 32613
                    mt "ФУУУ!!!"
                    mt "Как это мерзко!"
                    mt "!!!"
                    imgd 32614
                    w
                    pass
                "Нет!":
                    img 32615 vpunch
                    m "Нет!"
                    imgd 32616
                    m "С меня достаточно!"
                    # он отворачивается и кончает на попу своей подруги
                    imgd 32617
                    citizen15 "Тогда это достанется тебе, красотка!"
                    imgd 32618
                    cit7 "Давай, мой половой гигант, сделай это!"
                    img 32619
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen15 "ОООООХ!!!"
                    imgd 32620
                    citizen15 "ОООО..."
                    # Моника зло смотрит на него
                    imgd 32621
                    mt "ФУУУ!!!"
                    mt "Как это мерзко!"
                    mt "!!!"
                    pass
    # затемнение
    # смена кадра, гостиная, все одеты
    # Фрэнк крайне доволен собой
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 32622
    w
    imgf 32623
    citizen15 "Вау, чики!"
    citizen15 "Это было круто!!! Йо!"
    citizen15 "Вы обе на редкость горячие телки!"
    imgd 32624
    m "!!!"
    cit7 "Хи-хи-хи..."
    citizen15 "Может, повторим еще разок?!"
    music Pyro_Flow
    img 40380
    m "Еще чего!!!"
    m "Хватит с тебя одного раза!!!"
    imgd 40381
    m "Все! Идите отсюда!"
    m "!!!"
    ## фраза подруги о том, что она еще зайдет в магазин
    music Groove2_85
    imgf 40448
    # если Моника работала манекеном в магазине
    if monicaAgreedToSellDress == True:
        cit7 "Ты знаешь, мне понравилось..."
        cit7 "Может, как-нибудь встретимся еще в магазине..."
        cit7 "Я даже готова арендовать тебя, манекенчик! Хи-хи!"
        m "!!!"
        if monicaBoughtCasualDress1 == False and monicaOffendedCit3 == False:
            cit7 "Также как тот клиент, которому ты сосала член, чтобы продать платье..."
            img 40381
            m "Откуда ты..?"
            imgd 40448
            cit7 "Сегодня я убедилась, что у тебя нет с этим проблем."
            cit7 "Думаю, я найду применение для такой как ты..."

    else:
        cit7 "Ты знаешь, мне понравилось..."
        cit7 "Может, как-нибудь повторим. Я заплачу тебе..."
        cit7 "За аренду. Хи-хи!"
        m "!!!"
    # парень с подругой уходят
    sound highheels_short_walk
    imgf 40386
    mt "Вот сучка!"
    mt "!!!"
    ## это арт для мыслей Моники о том, что она испугалась, что подруга все поняла
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 2.0
    music Groove2_85
    imgf 32654
    mt "А вдруг она решила, что я какая-то проститутка?"
    mt "Вдруг она расскажет о произошедшем кому-нибудь?!"
    mt "Что тогда?!"
    mt "?!"
    imgd 40387
    mt "Хотя..."
    mt "Она все равно не знает, кто я такая на самом деле!"
    mt "..."
    mt "Мерзкие отбросы общества!"
    mt "Ненавижу эти трущобы и каждого его жителя!!!"
    mt "!!!"
    return 2


# после сцены с парнем в синей куртке и его подругой, мысли Моники
label ep216_dialogues3_citizens_2:
    # не рендерить!!
    mt "Как же это все отвратительно и грязно!"
    mt "Зато я заработала денег!"
    mt "Я, Моника Бакфетт, всегда умела зарабатывать деньги..."
    mt "И это только начало..."
    mt "Скоро я верну себе все, что у меня пытались отнять!"
    mt "И взорву эти трущобы со всеми их никчемными и бесполезными жителями!"
    mt "!!!"
    return

# если хочет сразу зайти в апартаменты, когда оставила там парочку, мысли Моники
label ep216_dialogues3_citizens_3:
    # не рендерить!!
    mt "Мне нужно дождаться, когда эти двое уйдут!"
    mt "Не хочу их видеть!"
    mt "У меня есть другие, более важные дела!"
    mt "!!!"
    return False

# при клике на гея (Angelo)
label ep216_dialogues3_citizens_4:
    # не рендерить, рендерить чуть ниже!
    music Groove2_85
    imgr Dial_Citizen_13_3
    citizen13 "Ой, подруга, привет!"
    citizen13 "Ты не поверишь, я только что вспоминал тебя!"
    imgl Dial_begin35_18
    m "Да неужели?!"
    citizen13 "Да, подруга!"
    imgr Dial_Citizen_13_1
    citizen13 "Ты даже не представляешь, что у меня случилось!"
    citizen13 "И мне очень нужна твоя дружеская поддержка!"
    citizen13 "Пойдем в более тихое место? Я тебе все расскажу."
    m "..."
    menu:
        "Пойти с ним.":
            imgl Dial_begin35_21
            mt "Интересно, что ему от меня надо?"
            mt "Что он может мне предложить?"
            m "Ну пошли..."
            # затемнение
            pass
        "Нет!":
            music Stealth_Groover
            imgl Dial_begin35_16
            mt "Мне плевать на его проблемы!"
            mt "Сейчас мне точно не до этого!"
            m "Нет!"
            m "Я не собираюсь никуда с тобой отходить!"
            m "У меня есть более важные дела!"
            music Groove2_85
            imgr Dial_Citizen_13_2
            citizen13 "Эх..."
            citizen13 "А я думал, что мы с тобой друзья..."
            return False
    # стоят у пилона
    # рендерить отсюда!!! до этого в движке
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 12323
    citizen13 "Подруга, в общем..."
    citizen13 "Даже не знаю, с чего начать..."
    citizen13 "В общем..."
    imgf 40329
    citizen13 "У меня есть бойфренд..."
    citizen13 "Он очень богат!"
    citizen13 "Он работает в сфере шоу-бизнеса."
    imgd 40334
    mt "О Боже! И почему я не удивлена?!"
    imgf 13692
    citizen13 "У нас с ним серьезные отношения."
    citizen13 "Мы встречаемся уже давно."
    imgd 13698
    m "..."
    imgf 13703
    citizen13 "И он говорил мне, что любит меня!"
    citizen13 "Что он сделает меня знаменитым актером! Или моделью!"
    citizen13 "Что он заберет меня отсюда в богатый район!"
    imgd 12372
    mt "О нет! Только не моделью!"
    mt "И вообще, что это за друг?!"
    mt "Интересно, я его знаю?"
    imgf 40330
    citizen13 "А вчера я узнал, что он мне изменяет!"
    citizen13 "Он ходит в какой-то дорогой отель к проституткам!"
    citizen13 "Ты представляешь?!"
    imgd 40331
    citizen13 "Он изменяет мне с какими-то шлюхами-эскортницами!!!"
    citizen13 "Он променял меня! Друга! На каких-то женщин!"
    imgd 40332
    m "..."
    # если Моника работает в эскорте
    if monicaHotelAdminAgreement3 == True and ep212_escort_monica_fired == False:
        #
        $ notif(t_("Моника работает в ВИП-эскорте отеля Ле Гранд."))
        #
        music Hidden_Agenda
        imgd 40333
        mt "Вот дьявол!"
        mt "А вдруг это один из тех неудачников, с которыми я..."
        mt "Которые приходили в Ле Гранд?!"
        #
    music Groove2_85
    imgf 12354
    citizen13 "Теперь ты, подруга, понимаешь, как я расстроен?!"
    citizen13 "И ладно бы, как раньше, ходил бы в клуб и флиртовал там с парнями!"
    citizen13 "Так нет! Он пошел по шлюхам!"
    imgd 40334
    mt "Хм... Что говорят в этих случаях?.."
    imgf 40335
    m "Вот он кобель..."
    citizen13 "Да!!!"
    m "А я здесь при чем?!"
    citizen13 "Мне нужна твоя помощь... По-дружески."
    m "???"
    imgd 40336
    citizen13 "Я хочу отплатить ему тем же!"
    citizen13 "И изменить ему с женщиной! А именно, с тобой!"
    music stop
    sound plastinka1b
    img 40337 hpunch
    m "Что?!"
    m "С чего ты решил, что я буду заниматься с тобой сексом?!"
    music Groove2_85
    imgd 12348
    citizen13 "Нет, подруга... Ну какой секс? О чем ты?"
    citizen13 "Измена - это если ты снимешь с себя одежду и поцелуешься со мной..."
    citizen13 "По-дружески..."
    citizen13 "А я тебе за это по-дружески дам немного денег."
    imgd 12331
    m "Сколько?"
    imgd 12332
    citizen13 "У меня есть 20 баксов. Я готов их отдать тебе за твою поддержку."
    imgd 12330
    m "..."
    $ menu_corruption = [slumsCitizen13Option1]
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                music Stealth_Groover
                imgf 13263
                mt "Деньги за поцелуй?"
                mt "..."
                mt "Черт! Но мне некуда его вести!"
                #
                $ notif(t_("Монике некуда вести клиентов."))
                #
                imgd 12324
                m "Мне некуда тебя вести!"
                m "А здесь я это делать не собираюсь!"
                music Groove2_85
                imgd 12325
                citizen13 "Жаль, подруга..."
                return -1
            # если арендует квартиру у Джека
            $ monicaCitizens15Slums6 = True # Моника согласилась пойти с геем в свои апартаменты
            pass
        "Отказаться.":
            music Stealth_Groover
            imgd 13263
            mt "Я не собираюсь заниматься всякими глупостями!"
            mt "Пусть сам разбирается со своим бойфрендом!"
            img 12324
            m "Нет!"
            m "Я не собираюсь никуда с тобой отходить!"
            m "У меня есть более важные дела!"
            music Groove2_85
            imgf 12325
            citizen13 "Эх..."
            citizen13 "А я думал, что мы с тобой друзья..."
            return -1
    # Моника в сомнениях
    music Hidden_Agenda
    imgf 13263
    mt "Хммм..."
    mt "$ 20 за поцелуй с этим неудачником..."
    mt "..."
    imgd 13265
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."
    # выглядывает мамочка
    music Master_Disorder
    img 24343 vpunch
    mt "И эта старая карга следит за мной..."
    imgd 24344
    w
    if ep214_perry_debt > 0:
        #
        $ notif(_("Моника должна выплачивать Перри долг в размере $ 50 000."))
        imgd 19174
        mt "Я должна выплачивать долг этой мерзкой извращенке Перри!"
        #
    music Groove2_85
    # если Монику выгнали с эскорта
    if ep212_escort_monica_fired == True:
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 19044
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    imgf 13695
    m "У меня есть одно условие!"
    m "Я не собираюсь перед тобой раздеваться!"
    imgd 13701
    citizen13 "Но..."
    img 13702
    m "Никаких 'но'!"
    m "Иначе я с тобой никуда не пойду!"
    imgd 13703
    citizen13 "Окей, подруга..."
    citizen13 "Договорились..."
    # затемнение
    # апартаменты Моники
    # гей стоит оглядывается, Моника заходит в гостину уже в домашней одежде
    fadeblack 1.5
    call ep211_quests_slums_apartments2_check_enter_forced() from _rcall_ep211_quests_slums_apartments2_check_enter_forced_1 # Моника входит в апартаменты (смена одежды)
    fadeblack 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 40449
    w
    imgf 40450
    citizen13 "Вау, подруга!"
    citizen13 "Ты такая красотка! Обалдеть!"
    citizen13 "Тебе очень идет этот наряд!"
    music Stealth_Groover
    imgd 40451
    mt "Еще бы! Перед тобой стоит самая красивая женщина этого города... Нет, страны!"
    mt "Любой мужчина мечтал бы оказаться на твоем месте, неудачник..."
    imgd 40452
    mt "И он заплатил бы за поцелуй со мной, Моникой Бакфетт, не какие-то $ 20..."
    mt "А намного-намного больше!"
    # он смотрит с зависть на ее грудь
    music Groove2_85
    imgf 40453
    w
    imgd 40454
    citizen13 "Когда-нибудь я себе сделаю такие же..."
    citizen13 "И тогда мой парень даже думать не захочет о каких-то шлюхах!"
    imgf 40455
    citizen13 "Можно я тебя обниму по-дружески? А потом поцелую, как мы договаривались..."
    menu:
        "Позволить ему поцеловать Монику.":
            pass
    imgd 40456
    m "Деньги вперед... По-дружески..."
    imgd 40457
    citizen13 "Да, подруга, без проблем. Держи."
    $ add_money(20.0)
    # он начинает лезть к ней обниматься, потом лезет целоваться
    fadeblack 1.5
    music Loved_Up
    imgfl 40458
    w
    imgf 40459
    w
    imgd 40460
    w
    imgd 40461
    w
    imgf 40462
    w
    sound kiss2
    imgd 40463
    w
    sound kiss1
    imgd 40464
    w
    imgf 40465
    citizen13 "Я впервые целуюсь с женщиной..."
    citizen13 "Это так... Необычно..."
    citizen13 "Ты вся такая мягкая... Нежная..."
    # поцелуй
    imgd 40466
    w
    sound kiss1
    imgd 40467
    w
    sound vjuh3
    imgd 40468
    w
    # проводит рукой по ее груди
    music stop
    sound plastinka1b
    img 40469 hpunch
    w
    music Power_Bots_Loop
    img 40470
    m "Эй, мы не договаривались, что ты будешь меня лапать!"
    music Groove2_85
    imgd 40471
    citizen13 "Я совсем немного, подруга. Через одежду..."
    citizen13 "Просто если я сейчас смогу возбудиться, значит я ему отомстил..."
    citizen13 "И мне станет намного легче..."
    citizen13 "Я не собираюсь делать ничего большего."
    menu:
        "Разрешить ему потрогать Монику через одежду.":
            pass
    music Pyro_Flow
    imgd 40472
    mt "Черт!"
    mt "!!!"
    $ add_corruption(5, "citizen13_touch_monica")
    imgd 40473
    m "Только совсем немного!"
    music Groove2_85
    citizen13 "Хорошо, подруга..."
    citizen13 "Но я пока никак не могу возбудиться..."
    imgd 40474
    citizen13 "Давай поцелуемся еще раз?"
    # и снова лезет целоваться, кладет руку ей на попу
    music Loved_Up
    imgf 40475
    w
    sound kiss2
    imgd 40476
    w
    sound vjuh3
    imgd 40477
    w
    imgf 40478
    w
    sound Jump1
    imgd 40479
    w
    imgd 40478
    w
    sound Jump1
    imgd 40479
    w
    imgd 40478
    w
    sound Jump1
    imgd 40479
    w
    imgf 40480
    citizen13 "Ммм, такая упругая попка."
    citizen13 "Почти как у меня..."
    img 40481
    mt "Что?!"
    mt "?!?!?!"
    mt "Нашел с чем сравнивать мою попу!!!"
    # он снова ее целует, потом отстраняется и отходит от Моники
    # говорит расстроенно
    imgf 40482
    w
    sound kiss2
    imgd 40483
    w
    sound kiss1
    imgd 40484
    w
    fadeblack 1.5
    music Groove2_85
    imgfl 40485
    citizen13 "Подруга... У меня член даже немного не приподнялся..."
    imgf 40486
    mt "И снова я почему-то этому не удивлена..."
    mt "..."
    imgd 40487
    citizen13 "Может, ты снимешь одежду?"
    citizen13 "Или хотя бы дашь залезть к себе в трусики?"
    citizen13 "Я ни разу не трогал киску..."
    citizen13 "А вдруг мне понравится?"
    $ menu_corruption = [slumsCitizen13Option2]
    menu:
        "Разрешить ему потрогать киску Моники.":
            imgd 40506
            m "Только если ты доплатишь за это!"
            citizen13 "Я могу дать тебе еще $ 5."
            citizen13 "Больше у меня нет денег, подруга."
            imgd 40507
            m "Всего $ 5?!"
            m "?!"
            music Hidden_Agenda
            imgf 40495
            mt "Черт!"
            mt "Он ведь хочет просто потрогать..."
            mt "А у меня станет на пять долларов больше..."
            mt "Я же помогаю ему по-дружески..."
            mt "Тем более, об этом все равно никто не узнает..."
            imgd 40508
            m "Только быстро!"
            m "И только потрогать!"
            citizen13 "Да, конечно, подруга..."
            $ add_money(5.0)
            $ add_corruption(5, "citizen13_touch_pussy")
            # снова подходит к ней
            # запускает руку под трусики сзади
            fadeblack 1.5
            music Loved_Up
            imgf 40509
            w
            sound Jump2
            imgd 40510
            citizen13 "О, это так... Непривычно..."
            citizen13 "Надо же..."
            imgf 40511
            citizen13 "Она у тебя такая... Горячая...#it"
            citizen13 "И такая нежная..."
            # водит пальцами по киске
            imgd 40512
            citizen13 "Интересно, как ощущать свой член внутри нее?#it"
            citizen13 "Может, это и правда так круто..."
            citizen13 "Что даже мой парень пошел к проституткам-эскортницам?"
            music Pyro_Flow
            img 40513 vpunch
            m "!!!"
            m "Так! Стоп!"
            m "Хватит!"
            m "Этого достаточно!"
            # он убирает руку и отходит от Моники
            $ monicaCitizens15Slums7 = True # Моника разрешила гею потрогать свою киску
            pass
        "Нет!":
            music Pyro_Flow
            imgd 40488
            m "Нет!"
            m "Мы договаривались только о поцелуе!"
            m "Я не собираюсь соглашаться на большее!"
            if monicaBitch == True:
                imgd 40489
                m "Или плати мне $ 200!"
                m "По-дружески!"
                imgd 40490
                citizen13 "У меня нет таких денег, подруга..."
                m "Ну тогда ответ 'нет'!"
            pass
    # он расстроенно
    fadeblack 1.5
    music Groove2_85
    imgfl 40491
    citizen13 "У меня не встал..."
    m "Я не знаю ни одного мужчину, который не желал бы МЕНЯ!"
    music Stealth_Groover
    imgf 40492
    m "И раз у тебя ничего не шевелится там..." # указывает на его штаны
    m "То я не вижу смысла тратить время на это!"
    imgd 40493
    citizen13 "Видимо, ты права, подруга..."
    citizen13 "Я не могу пойти против своей природы и заставить себя..."
    citizen13 "Но ты не обижайся, дело ведь не в тебе!"
    imgd 40494
    citizen13 "Ты офигительная красотка!"
    citizen13 "Тебе бы на обложку модного журнала!"
    # Моника испуганно
    music Pyro_Flow
    img 40495 vpunch
    mt "Твою мать!"
    mt "О что-то знает обо мне?!"
    music Groove2_85
    imgd 40496
    citizen13 "Но я знаю, что ты простая девушка из трущоб..."
    citizen13 "И тебе остается только мечтать о подобном."
    img 40497
    mt "Уф... Придурок! Напугал меня!"
    imgd 40498
    m "Так! Все!"
    m "Я думаю, этого достаточно!"
    imgd 40499
    citizen13 "Да, мне стало намного легче..."
    citizen13 "Я, наверное, пойду мириться со своим парнем..."
    imgd 40500
    m "Да-да... Иди уже!"
    citizen13 "Спасибо за помощь, подруга!"
    imgf 40501
    citizen13 "Если что, я к тебе буду приходить в гости!"
    citizen13 "А может, познакомлю тебя со своим бойфрендом!"
    music Stealth_Groover
    img 40502
    m "Не вздумай!"
    m "Никаких 'познакомлю'!"
    m "Этого мне еще не хватало!"
    sound man_steps
    imgf 40503
    citizen13 "Да ладно тебе! До встречи, подруга!"
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 2.0
    music Stealth_Groover
    # уходит
    imgf 40504
    mt "Боже! Я так испугалась, что он узнал меня!"
    mt "Ведь он мог видеть меня на обложке моего журнала!"
    mt "А я совсем не удивлюсь, что он их читает!"
    mt "Кошмар! Он всем рассказал бы, кто Я на самом деле!"
    mt "Это был бы провал!"
    mt "Даже не хочу думать о том, что могло бы за этим последовать!"
    mt "..."
    imgd 40505
    mt "И, вообще, какого хрена?!"
    mt "Я - самая лучшая женщина в этом городе!"
    mt "Я что, не возбудила его?!"
    mt "Да как он смеет!"
    mt "Меня должны хотеть все!"
    mt "Даже геи!!!"
    mt "!!!"
    return 1
