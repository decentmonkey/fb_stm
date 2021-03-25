default monicaEscortHotelStaffBlowjob1 = False  # Моника согласилась сделать минет служащему за 100 баксов
default monicaEscortHotelStaffBlowjob2 = False  # Моника согласилась сделать минет служащему за 50 баксов
default monicaEscortHotelStaffBlowjob3 = False  # Моника попросила служащего отеля пойти в другое место
default monicaEscortHotelStaffBlowjob4 = False  # Моника согласилась на минет служащему при девочках
default monicaEscortHotelStaffBlowjob5 = False  # Моника открыла рот для члена
default monicaEscortHotelStaffBlowjob6 = False  # Моника укусила служащего отеля за член

default monicaEscortHotelStaffBlowjobCumZone = 0
default monicaEscortRevenge1CumZone = 0

default monicaEscortRevengeGirl1 = False  # Моника пригласила любителя футфетиша в номер
default monicaEscortRevengeGirl2 = False  # брюнетка целовала ноги Моники по требованию клиента
default monicaEscortRevengeGirl3 = False  # клиент воспользовался задом клиентки и целовал в это время ноги Монике
default monicaEscortRevengeGirl4 = False  # брюнетка слизывала с ног Моники сперму клиента


#call ep214_dialogues3_escort_1() # в меню становится кликабельным пункт "Сколько денег ты скопил?!"
#call ep214_dialogues3_escort_2() # стойка рецепции, разговор халдея и Моники с админом
#call ep214_dialogues3_escort_3() # служебный коридор, Моника, халдей и девочки
#call ep214_dialogues3_escort_4() # разговор с админом, если укусила халдея
#call ep214_dialogues3_escort_5() # ресепшн, служащий, администратор и Моника, если она сделала ему минет
#call ep214_dialogues3_escort_6() # Моника сидит в ресторане в ожидании клиента, начало мести брюнетке
#call ep214_dialogues3_escort_7() # номер отеля, сцена с клиентом и брюнеткой
#call ep214_dialogues3_escort_8() # мысли Моники, если месть удалась
#call ep214_dialogues3_escort_9() # мысли Моники, если решила не мстить и ушла
#call ep214_dialogues3_escort_10() # если была месть брюнетке, встреча с ней в ресторане


# при выборе пункта меню "Встреча с клиентом (сцена)" (лейбл ep211_escort_scene1_1a)

# ресторан
# Моника сидит в ожидании клиента
# лейбл ep212_dialogues3_escort_hotel_8 - разговор со служащим отеля
# после его предложения уединиться в меню становится кликабельным пункт "Сколько денег ты скопил?!"
label ep214_dialogues3_escort_1:
    # по возможности использовать имеющиеся арты
    music Stealth_Groover
    imgf 18571
    mt "Фу! Какой же он жалкий!"
    mt "Копит свои несчастные центы, чтобы уединиться со мной!"
    mt "К чему это все, если такая женщина как я ему не по карману?"
    mt "Никогда не понимала логику неудачников!"
    mt "..."
    mt "Интересно, и сколько денег ему удалось скопить?"
    # Моника разговаривает с ним высокомерно
    imgd 18572
    m "Сколько денег ты скопил?"
    music Poppers_and_Prosecco
    imgf 18573
    hotel_staff "Мэм..."
    hotel_staff "Я могу заплатить Вам целых 100 баксов за минет!"
    hotel_staff "И я Вам обещаю, Мэм, что на этот раз никаких проблем не будет!"
    imgf 18574
    m "Не будет?!"
    m "С чего ты взял?!"
    #
    $ notif(_("Служащий отеля убежал, когда администратор их застукала"))
    #
    imgd 17561
    hotel_staff "Мэм, этого больше не повторится!"
    hotel_staff "Я Вам обещаю!"
    music Stealth_Groover
    imgf 18575
    m "..."
    # Моника задумчиво
    mt "100 долларов..."
    mt "Я могу послать этого халдея к черту и подождать какого-нибудь клиента."
    imgd 18576
    mt "С клиентом я могу заработать намного больше, но..."
    mt "Может попасться какой-нибудь грязный извращенец..."
    mt "Который не только не заплатит мне, но еще и создаст проблемы с администраторшей..."

    # если была сцена минета со служащим в туалете
    if monicaMadeBlowjobToHotelStaff == True:
        #
        $ notif(_("Моника делала минет служащему отеля"))
        #
        mt "А этому жалкому неудачнику уже повезло как-то... Кхм..."
        mt "Побыть со мной..."

    # служащий продолжает уговаривать Монику
    music Poppers_and_Prosecco
    imgf 17556
    hotel_staff "Мэм..."
    hotel_staff "В этот раз я все предусмотрел..."
    hotel_staff "Вы ничем не рискуете, Мэм."
    music Pyro_Flow
    imgd 30077
    mt "Это все отвратительно и мерзко!"
    mt "Чтобы я, леди, пошла с этим неудачником?!"
    mt "За 100 долларов!"
    music Groove2_85
    mt "..."
    mt "С другой стороны..."
    mt "Эти 100 долларов не будут лишними."
    # Моника высокомерно
    imgd 18577
    m "Если в этот раз ты снова поставишь меня в неловкую ситуацию!"
    m "Я оторву тебе яйца!"
    m "Ты понял меня, халдей?!"
    # служащий обрадованно
    music Poppers_and_Prosecco
    imgd 18578
    hotel_staff "Да, Мэм!"
    hotel_staff "То есть, нет, Мэм!"
    hotel_staff "Никакой неловкой ситуации для Вас не возникнет!"
    imgd 18579
    hotel_staff "Вы можете не переживать из-за этого!"
    hotel_staff "Все будет в рамках правил!"
    # Моника смотрит на него с подозрением
#    music Pyro_Flow
    imgf 18580
    m "..."
    imgd 18581
    hotel_staff "Пойдемте, Мэм!"
    hotel_staff "Я так давно мечтал об этом!"
    hotel_staff "Мне не терпится!"
    menu:
        "Пойти со служащим.":
            $ monicaEscortHotelStaffBlowjob1 = True # Моника согласилась сделать минет служащему за 100 баксов
            pass
        "Послать его к черту!":
            music Stealth_Groover
            imgf 18582
            m "Нет! Я никуда не пойду с тобой, халдей!"
            m "Я леди! И не собираюсь продаваться такому ничтожеству!"
            imgd 18583
            mt "Никчемный неудачник!"
            return False
    music Pyro_Flow
    imgf 18583
    mt "Черт!"
    mt "!!!"
    # Моника встает, свысока смотрит на него и они выходят из ресторана
    return True

# ресепшн
label ep214_dialogues3_escort_2:
    # админ стоит за стойкой рецепции, халдей и Моника напротив нее
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_54
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgf 18584
    mt "Какого черта этот неудачник меня притащил сюда?!"
    mt "?!"
    # админ строго обращается к Монике
    reception "[monica_hotel_name], ты почему не на своем рабочем месте?!"
    # потом смотрит на служащего
    imgd 18585
    reception "А тебе чего снова надо от меня?!"
    imgf 18586
    hotel_staff "Вот она!"
    # он указывает на Монику
    hotel_staff "Она согласилась!"
    # администратор удивленно смотрит на Монику
    # Моника в шоке
    music Power_Bots_Loop
    img 18587 hpunch
    m "Чтооо?!"
    m "?!?!?!"
    m "Ах ты мерзавец!!!"
    mt "!!!"
    mt "!!!!!!"
    # администраторша рявкает на Монику
    music Groove2_85
    imgd 18588
    reception "[monica_hotel_name]! Тихо!"
    reception "Этот зануда уже достал всех девочек эскорта."
    reception "Он постоянно пристает то к одной, то к другой."
    reception "А с ним никто не хочет работать."
    imgd 18589
    reception "Наконец-то, хоть ты согласилась!"
    reception "Ведь кто-то должен же удовлетворить этого озабоченного служащего."
    hotel_staff "Да-да! Она согласилась!"
    # Моника кипит от злости
#    music Pyro_Flow
    img 17520
    mt "!!!"
    mt "!!!!!!"
    # администраторша ехидно смотрит на Монику
#    music Groove2_85
    imgf 18590
    reception "Хмм... Интересно, кто же выиграл спор?"
    imgd 18591
    m "Какой еще спор?!"
    reception "Девочки спорили о том, согласишься ли ты за 50 долларов обслужить его."
    # Моника в шоке
    music Pyro_Flow
    img 18592
    m "Эти сучки еще и спорили?!"
    m "!!!"
    m "И почему за $ 50?!"
    m "$ 100!!!"
    music Groove2_85
    imgd 30111
    reception "Ты забыла про процент?"
    # Моника орет
    music Pyro_Flow
    imgd 18593
    m "Нет!"
    m "Я не буду этого делать!"
    m "Ни за 100 долларов, ни, тем более, за 50!!!"
    # администраторша строго
    music Groove2_85
    img 18594
    reception "[monica_hotel_name], хватит!"
    reception "Это твой клиент, ты уже дала согласие!"
    reception "Тебе напомнить правила нашего ВИП-эскорта?"
    reception "Иди работай!"
    img 18595 hpunch
    m "!!!"
    menu:
        "Пошли они все к черту!!! (прерывание квеста и увольнение с эскорта)":
            # Моника возмущенно
            music Pyro_Flow
            imgf 17555
            mt "Да они издеваются надо мной!"
            mt "!!!"
            # встает руки в боки
            imgd 18599
            m "Да пошла ты вместе со своими сучками проститутками!"
            m "Стерва!!!"
            reception "[monica_hotel_name], ты как со мной разговариваешь?!"
            reception "Еще слово и я тебя вышвырну с ВИП-эскорта!"
            imgd 18597
            m "Наконец-то!!!"
            # Моника уходит, служащий растерянно ей вслед
            music Groove2_85
            imgf 18598
            hotel_staff "Но, Мэм! Мы же договорились!"
            # она зло на него смотрит
            music Power_Bots_Loop
            img 18599 hpunch
            m "Молчать!!!"
            m "Жалкое ничтожество!!!"
            m "Ненавижу вас всех!"
            m "!!!"
            return False
        "Пойти со служащим отеля за $ 50.":
            $ monicaEscortHotelStaffBlowjob2 = True # Моника согласилась сделать минет служащему за 50 баксов
            pass
    music Pyro_Flow
    imgf 30114
    mt "Черт! Черт! Черт!"
    mt "Что мне теперь делать?!"
    mt "Если я сейчас откажусь, то не смогу больше здесь работать!"
    mt "А мне нужны деньги! Мне нужна эта работа!"
    mt "АААА!!!"
    mt "Моника, как же могло такое с тобой случиться?!"
    mt "!!!"
    music Groove2_85
    imgd 18011
    mt "Так, спокойно."
    mt "Это делаю не я, Моника Бакфетт."
    mt "На это соглашается [monica_hotel_name]."
    mt "Для нее сделать минет за деньги - пустяк."
    m "..."
    # служащий нетерпеливо
    imgf 18600
    hotel_staff "Мэм..."
    hotel_staff "Пойдемте, Мэм?"
    hotel_staff "Мне скоро уже нужно быть на рабочем месте."
    hotel_staff "У меня осталось совсем мало времени, Мэм."
    # Моника зло на него смотрит и молчит
    music Power_Bots_Loop
    img 18601
    m "..."
    music Groove2_85
    imgd 18602
    reception "[monica_hotel_name], слышала?"
    reception "Твой клиент тебя уже заждался!"
    reception "Это недопустимо!"
    reception "Иди работай! Быстро!"
    return True

# Моника вышла на улицу после того, как послала админа со служащим (увольнение)
# лейбл ep212_dialogues3_escort_hotel_7_1

# служебный коридор
label ep214_dialogues3_escort_3:
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
            return -1
        "Сказать служащему отеля, чтоб нашел другое место!":
            $ monicaEscortHotelStaffBlowjob3 = True # Моника попросила служащего отеля пойти в другое место
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
            return -1
        "Сделать служащему отеля минет.":
            $ monicaEscortHotelStaffBlowjob4 = True # Моника согласилась на минет служащему при девочках
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
#    music Pyro_Flow
    img 18636
    mt "Фу!"
    mt "Смотреть на него не могу!"
    mt "Какой же он мерзкий!!!"
    mt "!!!"
#    music Groove2_85
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
            $ monicaEscortHotelStaffBlowjob5 = True # Моника открыла рот для члена
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
            return -1
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
#    imgf 18653
    girl_1 "Да насаживай уже ее голову на свой стояк!"
    girl_1 "Чего ты с ней возишься?!"
    girl_1 "Давай, амеба, покажи, что ты вообще мужчина!"
    mt "!!!"
    # служащий смотрит на брюнетку, потом на Монику
    # берет ее за голову и входит в ее рот до предела
#    imgd 18654
#    w
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
            $ monicaEscortHotelStaffBlowjob6 = True # Моника укусила служащего отеля за член
            return -2
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
            $ monicaEscortHotelStaffBlowjobCumZone = 1
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
            $ monicaEscortHotelStaffBlowjobCumZone = 2
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
    return 1


# если укусила служащего за член
# диалог взят частично из лейбла ep212_dialogues3_escort_hotel_5_1
# if monicaEscortHotelStaffBlowjob6 == True
label ep214_dialogues3_escort_4:
    # использовать имеющиеся арты!!
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 17554
    reception "ТЫ ЧТО НАТВОРИЛА?!"
    reception "[monica_hotel_name]!"
    # Моника орет
    music Power_Bots_Loop
    img 17508 hpunch
    m "Пошла ты со своим долбанным ВИП-эскортом к черту, сучка!!!"
    m "Я не [monica_hotel_name]!"
    m "И никогда ею не была!"
    m "!!!"
    music Groove2_85
    img 17509
    reception "ЧТООО?!"
    music Pyro_Flow
    imgd 17510
    m "Что слышала!"
    m "Я ухожу из этого никчемного отеля и возвращаться сюда не собираюсь!"
    # Моника разворачивается и идет в сторону выхода, админ зло смотрит ей в след
    sound highheels_short_walk
    imgf 17513
    reception "Стой!"
    # Моника, не поворачиваясь показывает ей фак и уходит
    sound Jump1
    img 17514
    m "!!!"
    mt "Сучка!"
    mt "Ненавижу!"
    mt "Ненавижу их всех!!!"
    mt "!!!"
    return

# Моника вышла на улицу после того, как послала админа (увольнение)
# лейбл ep212_dialogues3_escort_hotel_7_1

# после того, как Моника сделала минет служащему
# ресепшн
# служащий, администратор и Моника
label ep214_dialogues3_escort_5:
    # по возможности использовать имеющиеся арты!!
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 18585
    reception "Ну что? Теперь ты доволен?"
    reception "Все прошло нормально?"
    # служащий стоит еще прибалдевший
    imgf 18689
    hotel_staff "Дааа!"
    hotel_staff "Мэм отлично справилась со своей работой."
    hotel_staff "Вот 100 баксов, как и договаривались."
    hotel_staff "Когда накоплю еще, обязательно снова приду к Мэм!"
    # Моника зло на него смотрит и молчит
    music Power_Bots_Loop
    img 18690
    mt "Ни за что!"
    mt "!!!"
    music Groove2_85
    imgf 30111
    reception "Хорошо."
    reception "[monica_hotel_name], вот твой процент."
    $ add_money(50.0)
    # дает Монике деньги
#    sound vjuh3
    imgd 30112
    reception "На сегодня все."
    reception "Приходи завтра."
    # Моника про себя думает, что ей могли бы заплатить и больше!
    imgf 30114
    mt "Могла бы заплатить и больше! За моральный вред!"
    mt "Сучка!!!"
    mt "!!!"
    return


# месть брюнетке с каре

# если уже была сцена минета со служащим в присутствии девочек с эскорта
# Моника сидит в ресторане в ожидании клиента
label ep214_dialogues3_escort_6:
    # по возможности использовать имеющиеся арты!!
    fadeblack 1.5
    music Poppers_and_Prosecco
    imgfl 30061
    w
    imgf 30085
    mt "Так, Моника!"
    mt "Тебе нужно придумать план, как поставить эту мерзкую тварь с эскорта на место!"
    mt "Это недопустимо, чтобы какая-то серая мышь вела себя подобным образом!"

    # если была сцена с семейной парой
    if monicaEscortAngryWife1 == True:
        #
        $ notif(_("Брюнетка сказала жене клиента, что ее муж изменяет ей с Моникой"))
        #
        imgd 30070
        mt "Эта сучка подставила меня перед женой того жалкого неудачника!"
        mt "И эта провинциальная дура унижала меня по ее вине!"
        #

    # если была сцена с инвестором
    if monicaEscortLindaTable1 == True:
        #
        $ notif(_("Брюнетка подговорила Линду использовать Монику в качестве столика."))
        #
        imgf 18576
        mt "Это именно она подговорила Линду взять меня на встречу с инвестором!"
        mt "И сделать из меня реквизит!!"
        #

    # если была сцена со служащим отеля в служебном коридоре перед девочками
    if monicaEscortHotelStaffBlowjob5 == True:
        #
        $ notif(_("Брюнетка подбадривала служащего отеля, когда Моника делала ему минет"))
        #
        imgd 30084
        mt "Еще эта тварь провоцировала халдея!"
        mt "И угрожала тем, что нажалуется на меня администратору!"
        #
    music Power_Bots_Loop
    imgf 18583
    mt "Ненавижу ее!"
    mt "Моника, подобное нельзя оставлять безнаказанным!"
    mt "Тебе срочно нужен план!"
    # затемнение, спустя некоторое время
    # Моника все также сидит за столиком
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_55
    scene black_screen
    with Dissolve(1)
    music Poppers_and_Prosecco
    imgfl 18691
    mt "Я уже устала сидеть здесь."
    mt "Видимо, у [monica_hotel_name] сегодня не будет заработка..."
    # Моника встает из-за столика и в это время
    # в ресторан заходит самый первый ее клиент (толстяк, футфетиш)
    # Моника замечает его
    sound highheels_short_walk
    imgf 18693
    w
    sound man_steps
    imgd 18692
    w
    imgd 18694
    mt "!!!"
    # клиент подходит к ней
    fadeblack
    sound man_steps
    pause 2.0
    music Poppers_and_Prosecco
    imgfl 30078
    client "Добрый вечер, Мисс [monica_hotel_name]."
    client "Рад Вас видеть."
    m "Добрый вечер..."
    # если Моника сосала ему палец, пока он дрочил себе
    imgf 18571
    mt "Это же тот неудачник, который облизывал мне ноги и неплохо заплатил за это!"
    if monicaEscortClientHotel2 == True:
        #
        $ notif(_("Моника согласилась пососать палец клиента"))
        #
        mt "Правда, пришлось взять его грязный палец в свой рот. Фу!"
        mt "!!!"
        #
    imgd 30077
    mt "..."
    mt "Хммм... Возможно, с помощью этого никчемного извращенца..."
    mt "Я смогу наказать ту сучку!"
    music Stealth_Groover
    imgd 18695
    mt "Это гениально, Моника!"
    mt "Тебе давно нужно поставить ее на место!"
    mt "Пусть знает, как вставать на пути у самой Моники Бакфетт!"
    mt "Дрянь!"
    # Моника пытается флиртовать с клиентом
    imgf 30079
    m "Мистер, я тоже рада, что вы решили снова прийти ко мне..."
    # клиент любезничает с Моникой, похотливо пялится на нее, видно, что все мысли только о сексе
    client "Да, Мисс [monica_hotel_name]... Я снова вернулся."
    client "Вы и правда рады меня видеть?"
    imgd 18696
    m "Да... Конечно, рада." # Моника притворно улыбается
    imgd 18697
    mt "Нет, извращенец!"
    mt "Но я буду весьма рада, если с помощью тебя я отомщу одной сучке!"
#    music Poppers_and_Prosecco
    imgf 30080
    client "Мне так понравилось с Вами в прошлый раз, Мисс [monica_hotel_name]..."
    client "Вы такая... Такая красивая..."
    imgd 18698
    m "Спасибо, Мистер."
    imgd 18699
    mt "Ну давай уже, быстрее, пока эта стерва здесь!" # смотрит на брюнетку, та за столиком
    mt "Или мне самой приглашать тебя в номер?!"
    imgf 18700
    client "Вы настолько восхитительны, Мисс [monica_hotel_name], что я..."
    client "Я даже боялся подходить к Вам."
    client "Неужели такая, как Вы, снова захочет встретиться со мной?"
    imgd 18701
    mt "Боже, какой идиот!" # снова притворно улыбается в попытке флиртовать
    m "Я с удовольствием с Вами еще раз встречусь."
    imgf 30082
    client "Правда? А когда?"
    client "Неужели... Неужели Вам тоже понравилось?"
    m "Да, вы мне очень понравились, Мистер."
    # клиент мнется
    imgd 18702
    client "Я даже мечтать не мог о том, чтобы такая женщина, как Вы..."
    client "Со мной... Кхм..."
    client "Я..."
    music Pyro_Flow
    imgd 18703
    mt "Да сколько уже можно?!"
    mt "Я что, уговаривать его должна?!"
    mt "?!"
    menu:
        "Предложить ему пойти в номер.":
            $ monicaEscortRevengeGirl1 = True # Моника пригласила любителя футфетиша в номер
            pass
        "Нет, я не хочу!":
            imgd 30085
            mt "Фу! Нет!"
            mt "Я не собираюсь терпеть его из-за этой мерзкой сучки!"
            mt "Она не стоит таких жертв с моей стороны!"
            # высокомерно говорит ему
            music Stealth_Groover
            imgf 30086
            m "Я с Вами встречусь, но не сегодня."
            m "Как-нибудь в следующий раз!"
            client "Да, Мисс [monica_hotel_name]... Конечно..."
            imgd 30084
            mt "Никчемный неудачник!"
            mt "Бесполезный!"
            mt "Фи!"
            # Моника уходит
            return False
    imgd 30085
    mt "Черт!"
    mt "Пока он решится пригласить меня, эта сучка уйдет куда-нибудь!"
    mt "Проще самой это сделать!"
    mt "Что за идиот!"
    music Stealth_Groover
    imgf 18704
    m "Может, мы пойдем в номер прямо сейчас?"
    client "Сейчас?!"
    client "О, Мисс [monica_hotel_name]! Да!"
    client "Я никак не мог осмелиться предложить Вам это..."
    imgd 18697
    mt "Я заметила... Никчемный неудачник!"
    # Моника показывает рукой на брюнетку
    music Hidden_Agenda
    imgf 18705
    m "Только давай возьмем еще ту девочку?"
    m "Тебе будет приятно вдвойне..."
    imgd 18706
    client "Я бы с удовольствием, Мисс [monica_hotel_name], но..."
    client "Мне не хватит денег заплатить за секс сразу с двумя девочками..."
    # Моника берет клиента под руку и вдет к выходу из ресторана
    imgf 18707
    m "Мистер, не переживайте. Секс будет только с одной девочкой..."
    m "Поэтому вам хватит денег."
    imgd 30080
    client "О, ну если так, то конечно!"
    client "Мне нравится Ваше предложение!"
    # Моника злорадно смотрит на брюнетку
    music Stealth_Groover
    imgf 18699
    mt "Ну что, сучка, пришло время ответить за свое мерзкое поведение!"
    mt "!!!"
    mt "Осталось сказать администратору, что клиент хочет провести время со мной и с этой дрянью..."
    # затемнение, звук каблуков
    return True

label ep214_dialogues3_escort_6b:
    client "[monica_hotel_name], а где вторая девочка?"
    m "Она поднимется следом за нами."
    m "Пойдемте в лифт."
    $ ep214_dialogues3_escort_6b_flag = True
    return False

# номер отеля
# номер отеля
label ep214_dialogues3_escort_7:
    # некоторое время спустя
    # Моника вдвоем с клиентом заходят в номер
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_56
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
            $ monicaEscortRevengeGirl3 = True # клиент воспользовался задом клиентки и целовал в это время ноги Монике
            pass
        "Нет, я не хочу!":
            music Pyro_Flow
            imgf 16818
            mt "Фу! Нет!"
            mt "Я не собираюсь терпеть все эти грязные извращенства из-за какой-то мерзкой сучки!"
            mt "Она не стоит таких жертв с моей стороны!"
            $ questHelp("escort_8", False)
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
            return False
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
            $ monicaEscortRevengeGirl2 = True # брюнетка целовала ноги Моники по требованию клиента
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
            return False
    music Stealth_Groover
    imgf 18796
    mt "С другой стороны, Моника, твоя ножка его уже возбудила."
    mt "И эта сучка от этого бесится."
    mt "Хи-хи!"
#    imgd 18797
    imgd 18789
    m "Да, Мистер. Пусть она тоже попробует."
    if questHelpFlag12 == False:
        $ questHelpFlag12 = True
        $ questHelp("escort_13", skipIfExists=True)
        $ questHelpDesc("escort_desc2", "escort_desc4")
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
            $ monicaEscortRevenge1CumZone = 1
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
            $ monicaEscortRevenge1CumZone = 2
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
            $ monicaEscortRevenge1CumZone = 3
            menu:
                "Заставить сучку с эскорта слизать сперму клиента.":
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
                    $ monicaEscortRevengeGirl4 = True # брюнетка слизывала с ног Моники сперму клиента
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
    return True

# мысли Моники, если месть удалась
label ep214_dialogues3_escort_8:
    # не рендерить!!
    mt "Моника, это была гениальная идея!"
    mt "Теперь эта сучка будет думать, прежде чем лезть ко МНЕ!"
    mt "И подобное ждет всякого, кто посмеет встать на пути Моники Бакфетт!"
    return

# мысли Моники, если решила не мстить и ушла
label ep214_dialogues3_escort_9:
    # не рендерить!!
    mt "Возможно, это был и хороший план, но..."
    mt "Мне настолько мерзок этот никчемный неудачник! Фу!"
    return

# если была месть брюнетке, встреча с ней в другой день
# ресторан
label ep214_dialogues3_escort_10:
    # Моника за столиком, брюнетка подходит к ней
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 18839
    w
    imgf 18836
    girl_1 "Слышишь ТЫ, шлюха!"
    girl_1 "Если ты думаешь, что я это тебе оставлю просто так!.."
    music Stealth_Groover
    imgd 18837
    m "Будешь меня снова пытаться запугать?"
    m "Да пошла ты!"
    m "Сучка!"
    m "Хочешь повторить встречу с моим клиентом?"
    m "Тебе настолько понравились мои ножки? Хи-хи!"
    music Groove2_85
    imgd 18838
    girl_1 "Ты за это заплатишь!"
    girl_1 "Я сделаю все, чтобы тебя вышвырнули отсюда!"
    girl_1 "Стерва!"
    return
