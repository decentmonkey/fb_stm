label EP1_marcus_cabinet_dialogue1:
    detective "Сэр."
    img 2086
    with fadelong
    w
    img 2087
    with fade
    detective "Сэр."
    "Вот эта женщина."
    "Она представилась как Моника Бакфетт."

    img 2088
    marcus "Значит вот как она выглядит вживую."
    "Интересно."
    return

label EP1_marcus_cabinet_dialogue2:
    music Pyro_Flow
    img 2089
    with fadelong
    m "Значит это ты Маркус?"
    img 2090
    "Что-то мне вживую твой голос не так уж и понравился."
    img 2091
    "Это было единственное с помощью чего ты мог избежать неприятностей."
    img 2092
    "Связанных с тем что я прождала тебя больше пяти минут!"
    "Общаясь с твоими болванами!"
    img 2093
    marcus "..."
    img 2094
    m "А?"
    "Маркус!"
    "Что скажешь?"
    img 2095
    "Мне уже неинтересны твои штрафы."
    img 2096
    "Я пришла сюда чтобы высказать тебе что думаю, урод!"
    img 2097
    "Как ты смеешь отнимать мое время!"
    img 2098
    detective "Сэр.."
    img 2100
    marcus "Хорошо."
    "Значит вы подтверждаете что вы Моника Бакфетт?"
    img 2101
    m "В смысле?"
    "Подтверждаю-ли Я?"
    "А кто еще по твоему здесь стоит?"
    "Чье еще по твоему время ты отнимаешь?"
    "Каждая моя минута стоит тысячи долларов!"
    img 2102
    "И ты заплатишь за все минуты что я прождала тебя!"
    img 2098
    with fade
    detective "Сэр?"
    img 2099
    marcus "Подожди."
    img 2103
    with fade
    "Итак."
    "Моника Бакфетт?"
    img 2104
    "Во-первых, я хочу извиниться за то что заставил вас ждать."
    img 2103
    "И сказать спасибо что вы не ушли."
    img 2105
    m "Мне не нужно твое спасибо!"
    img 2106
    "И я не собираюсь тебя дальше слушать!"
    img 2107
    "Я ухожу!"
    $ marcusCabinetState = 1
    call EP1_refresh_scene_fade()
    return

label EP1_marcus_cabinet_dialogue3:
    music Power_Bots_Loop
    sound snd_door_open1
    img 2108
    with fadelong
    w
    img 2109
    w
    img 2110
    w
    img 2111
    w
    img 2112
    w
    img 2113
    marcus "Миссис Бакфетт."
    "Вам придется задержаться и дослушать меня."

    img 2115
    with fadelong
    marcus "..."

    m "..."

    img 2114
    with fade
    marcus "Надеть наручники!"

    img 2116
    m "Что?????"
    img 2117
    w
    music stop
    $ renpy.pause(1)
    sound snd_handcuffs
    call textonblack(t_("ЧТО?????"))
    img black_screen
    with Dissolve(1)

    music Power_Bots_Loop
    img 2118
    with fadelong
    w
    img 2119
    w
    img 2120
    w

    sound highheels_short_walk
    img 2121
    with fadelong
    w
    img 2122
    w
    img 2123
    w
    img 2124
    w
    img 2125
    marcus "Все свободны."
    img 2126
    "Кроме Миссис Бакфетт."
    $ steam_achievement("ach8")

    $ marcusCabinetState = 2
    call EP1_change_scene("EP1_police_marcuscabinet", "Fade", False)
    return


label EP1_marcus_cabinet_dialogue4:
    img 2127
    with fadelong
    w
    img 2128
    m "ЧТО"
    "ЗНАЧИТ"
    img 2129
    "ЭТОТ"
    "ЦИРК"
    "????"
    "..."
    "ТЫ В СВОЕМ УМЕ"
    img 2130
    "МАЛЬЧИК??"

    music Groove2_85

    img 2131
    with fadelong
    marcus "Миссис Бакфетт."
    "Хочу сказать вам спасибо что вы пришли сами."
    "И нам не пришлось производить захват."
    "У таких людей как вы часто бывает много охраны."
    "Могла возникнуть стрельба и пострадать невинные люди."
    img 2132
    "..."
    img 2133
    "Вы арестованы."
    img 2134
    m "ЧТО???"
    "НА КАКОМ ОСНОВАНИИ???"
    img 2135
    marcus "Оснований несколько."
    "Давайте начнем по порядку."
    "Скажите, из какой страны вы приехали 12 лет назад?"
    img 2136
    m "Я ничего не собираюсь говорить!"
    "Мои адвокаты разотрут вас в пыль!!!"
    img 2137
    "..."
    "Кстати, что сейчас происходит?"
    "Вот прямо сейчас!"
    "Как это называется?"

    img 2138
    marcus "Можете называть это допросом."
    img 2139
    m "ДА?"
    "ТОГДА ГДЕ МОЙ АДВОКАТ???"
    "Я ИМЕЮ НА НЕГО ПРАВО!"
    img 2140
    marcus "Не имеете."
    img 2141
    m "ЧТО???"
    "Я ГРАЖДАНКА!!!"
    "ОБ ЭТОМ ЗНАЮТ ВСЕ!!!"
    "ДАЖЕ ТА ТОЛСТУХА НА ВХОДЕ В ВАШУ ДЫРУ!!!"
    "ОНА НАЗЫВАЛА МЕНЯ ГРАЖДАНКА!!!"
    "А КАК ГРАЖДАНКА Я ИМЕЮ ПРАВО НА АДВОКАТА!!!"
    img 2142
    marcus "Не имеете."

    $ marcusCabinetState = 3
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_197
    return

label EP1_marcus_cabinet_dialogue5:
    img 2143
    with fadelong
    m "С КАКОЙ СТАТИ???"
    img 2142
    marcus "Вы не гражданка."

    m "ЧТО???"

    img 2143
    "ДА КАК ВЫ СМЕЕТЕ ТАКОЕ ГОВОРИТЬ???"
    "ВЫ ВООБЩЕ ВМЕНЯЕМЫ???"

    img 2145
    marcus "Мэм."
    "Если вы хотите чтобы я вам объяснил, то давайте продолжим с места где вы меня прервали."
    "Вы же хотите получить ответы на вопросы?"

    $ marcusCabinetState2 = 1
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_198

    return

label EP1_marcus_cabinet_dialogue6:
    img 2146
    with fadelong
    m "ХОЧУ!!!"
    img 2147
    marcus "Тогда успокойтесь и давайте продолжим."
    "Согласны?"
    m "Согласна."
    marcus "Итак, можете не отвечать мне."
    "Я знаю откуда вы прибыли."
    "Я также знаю с кем вы прибыли."
    "Вы прибыли с вашим будущим мужем."
    "С которым познакомились на местном конкурсе красоты."
    "Не знаю что вы там женщины делаете с мужчинами."
    "Но вы каким-то образом взяли его под контроль."
    "Вы вышли за него замуж."
    "Стали иметь большое состояние."
    "Вести светскую жизнь."

    $ marcusCabinetState2 = 2
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_199

    return

label EP1_marcus_cabinet_dialogue7:
    img 2148
    with fadelong
    m "И??"
    "ЭТО НЕЗАКОННО???"
    img 2149
    marcus "Мэм."
    "Вы все время считали что вы водите мужа за нос."
    "Но знаете-ли вы что в чем-то и он водил вас?"
    img 2150
    m "ЧТО ВЫ ИМЕЕТЕ ВВИДУ???"
    "У НЕГО БЫЛА ЛЮБОВНИЦА???"
    img 2151
    marcus "О, нет."
    "По крайней мере я про это не знаю."
    img 2152
    "Я знаю другое."
    "12 лет назад вы получили гражданство нашей страны."
    "Знаете-ли вы что это было сделано с нарушением закона?"
    "С задействованием коррупционных связей вашего мужа?"
    m "Нет."
    "Не знаю."
    marcus "А мы знаем."
    "Более того, в данный момент эти чиновники арестованы и отбывают сроки."
    "Все принятые ими решения аннулированы."
    "Так что у вас нет гражданства."
    img 2153
    m "У меня в любом случае есть гражданство моей страны откуда я приехала."
    img 2154
    marcus "Нет, нету."
    "Во-первых, прошло более 10 лет."
    "И вам надо было переоформлять документы."
    "Когда вы не явились на переоформление, была создана комиссия."
    "Комиссия обнаружила что вы уже являетесь гражданкой нашей страны."
    "А так как в вашей стране запрещено двойное гражданство, то гражданство вашей страны было аннулировано."
    img 2155
    m "Не понимаю."
    "Я вам не верю."
    marcus "Можете верить."
    "Можете нет."
    img 2156
    m "Где мой муж?"
    img 2157
    marcus "Ваш муж уже около недели находится под арестом."
    "Более того, сегодня был суд и его приговорили к пожизненному заключению."
    "Возможно ему даже грозит электрический стул."
    img 2158
    m "ЗА ЧТО????"
    img 2159
    marcus "Видите-ли, Миссис Бакфетт."
    "Хотя на самом деле ТАК вас называть некорректно."
    "Ведь я даже не понимаю КТО вы теперь."
    "Но давайте я буду это делать для удобства."
    img 2160
    m "!!!!!!!!!"
    img 2161
    marcus "Итак, Миссис Бакфетт."
    "Я опущу то что стартовый капитал вашего мужа был накоплен преступным путем."
    "Я перейду сразу к тому что ваш муж отмывал большие, очень большие суммы денег."
    img 2162
    "Речь о миллиардах."
    img 2161
    "Более того, эти деньги шли на преступные цели."
    img 2163
    m "Вы хотите сказать что мой муж кого-то убивал?"
    img 2164
    marcus "Нет, нет."
    "На самом деле он был просто финансовым звеном."
    "Просто зарабатывал деньги."
    img 2165
    m "Тогда почему его так строго наказали?"
    img 2166
    marcus "Видите-ли."
    "Были выборы и ваш муж поставил не на того."
    "Хотя на самом деле неважно что именно он делал."
    "Важно то что он, по факту, играл на руку интересам преступных групп."
    "Поэтому их дело объединили в одно с соответствующим наказанием."
    img 2167
    m "Слушайте!"
    "Мне неважно что там творил муж!"
    img 2168
    if bitchmeterValue > maxBitchness / 2:
        "По большому счету мне наплевать на него!"
    else:
        "Я волнуюсь за него тоже, но тем не менее!"

    "Я не понимаю почему Я здесь?"
    img 2169
    "Когда вы меня выпустите?"
    "После нашего разговора?"
    img 2170
    marcus "Давайте обсудим вопрос вашего выхода в конце."
    "И вернемся к вам."
    img 2171
    "Дело в том, что практически все компании, через которые шли преступные деньги, были оформлены на ВАС!"
    img 2172
    m "О НЕТ!"
    img 2173
    marcus "Миссис Бакфетт."
    "Я понимаю что вы вели политику максимального перехода собственности мужа в ваши руки."
    "Что вы не преследовали иных целей кроме личного обогащения."
    "И что, по большому счету, вы ни при чем."
    img 2174
    m "Я и есть ни при чем."
    "Я рада что вы это понимаете!"
    img 2175
    marcus "Да, может показаться что вы ни при чем."
    "Но вы при чем!"
    img 2176
    m "Нет!"
    img 2177
    marcus "Миссис Бакфетт."
    "Вы арестованы."
    "Более того, вы являетесь главным фигурантом в деле вашего мужа."
    "Ваш муж делал какие-то переводы."
    img 2178
    with fade
    "Но фирмы принадлежали вам, так что ваша вина значительно больше."
    img 2179
    m "О НЕТ!!!"
    "ЧТО МНЕ ГРОЗИТ???"
    img 2180
    marcus "Я думаю электрический стул."
    "Возможно пожизненное заключение в очень строгом заведении."
    img 2181
    "Я имею кое-какое влияние на это решение."
    img 2182
    marcus "Смею заверить что буду настаивать на сохранении вашей жизни, но помещении в максимально строгое место."
    "Этот процесс будет решаться в течении пары недель."
    music Power_Bots_Loop
    img 2183
    with fadelong
    marcus "Это время я бы попросил вас остаться у нас."
    img 2184
    m "ЧТО???"
    img 2185
    m "Я НЕ ОСТАНУСЬ ЗДЕСЬ!!!"
    img 2186
    "ВЫПУСТИТЕ МЕНЯ!!!"

    $ marcusCabinetDoorState = 1
    call EP1_change_scene("EP1_police_marcuscabinet_door")

    return

label EP1_marcus_cabinet_dialogue8:
    img black_screen
    with Dissolve(1)
    sound snd_door_locked1
    $ renpy.pause(0.5)
    sound snd_door_locked1
    $ renpy.pause(0.5)
    sound snd_door_locked1
    $ renpy.pause(0.5)
    sound snd_door_locked1
    $ renpy.pause(0.5)
    sound snd_door_locked1
    $ renpy.pause(0.5)

    img 2187
    with fadelong
    marcus "Дверь заперта, Миссис Бакфетт."
    "Но это не отменяет попытки побега."
    "Сейчас вас проводят в камеру."
    m "НЕЕЕЕЕТ!"

    sound snd_door_open1
    img black_screen
    with Dissolve(1)
    img 2188
    with fadelong
    w
    img 2189
    marcus "Увести ее."
    music Gearhead
    call EP1_jail_day1() from _ep1call_jail_day1
    return

label EP1_marcus_cabinet_dialogue9:
    img 2587
    with fadelong
    overseer "Мистер Маркус!"
    "Заключенная доставлена!"
    marcus "Я вижу, Боб."
    img 2588
    overseer "Мистер Маркус?"
    "Мне остаться здесь?"
    "Чтобы увести ее назад вниз."
    "Вы же ненадолго?"
    img 2589
    marcus "Боб."
    "Это не твое дело!"
    "Иди к себе в подвал и сиди там!"
    "Не задавай мне дурацких вопросов!"
    "Я не в настроении!!!"
    img 2590
    overseer "Да, Мистер Маркус!"
    "Я понял!"

    img 2591
    with fadelong
    marcus "Здравствуйте, Миссис Бакфетт."
    "Присаживайтесь."
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_200

    return

label EP1_marcus_cabinet_dialogue10:
    music Groove2_85
    img 2592
    with fadelong
    marcus "Здравствуйте, Миссис Бакфетт."
    "Вы догадываетесь зачем Вы здесь?"

    img 2593
    music Power_Bots_Loop
    m "Я догадываюсь."
    "Вы хотите отправить меня на свою свиноферму."
    img 2594
    "Вы хотите моей смерти!!!"
    "О Боже!!!"
    img 2595
    music Groove2_85
    marcus "Миссис Бакфетт."
    "Смерть на Ранчо 218 грозит только тем кто не выполняет приказы Master."
    "Остальные процессы происходят так, что боль не приводит к смертельному исходу."
    "Наши Masters в этом очень опытны."
    "Но я Вас позвал не для этого."
    $ marcusCabinetState = 6
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_201
    return

label EP1_marcus_cabinet_dialogue11:
    img 2596
    with fadelong
    m "А..."
    "Для чего....?"
    img 2597
    marcus "Миссис Бакфетт."
    "Возникла неожиданная ситуация."
    "Я Вам объясню ее, а потом Вы должны будете сделать выбор."
    img 2598
    "Но хорошо подумайте прежде чем сделать это!"
    img 2599
    m "Какой выбор?"
    "У меня есть какой-то выбор?"
    img 2600
    marcus "Да, Миссис Бакфетт."
    "Мы не ожидали что за вас могут заступиться серьезные люди."
    "Учитывая Ваш характер и образ жизни."
    img 2601
    m "Люди???"
    "Друзья???"
    img 2602
    music RnB4_100
    mt "ДРУЗЬЯ!!!"
    "МНЕ КТО-ТО РЕШИЛ ПОМОЧЬ!!!"
    "У МЕНЯ НЕТ СЛОВ!"
    "Я ДУМАЛА НАДЕЖДЫ БОЛЬШЕ НЕТ!!!"
    img 2603
    music Groove2_85
    marcus "Да, некто очень хорошо известный."
    "И Вам и Нам."
    img 2604
    m "Кто???"
    img 2603
    marcus "Дик Адвокат."
    img 2605
    music RnB4_100
    m "ДИК!!"
    mt "ДИК!! ДИК!!"
    mt "ДИК!! ДИК!!"
    mt "ТЫ СДЕЛАЛ ЭТО!"
    "ТЫ НЕ ОСТАВИЛ МЕНЯ!"
    img 2606
    music Groove2_85
    marcus "Да, Дик."
    "Но не спешите радоваться."
    "У него далеко не такие связи как у людей, которые ждут Вас!"
    "Я уже обещал многим и на Вас уже очередь!"
    "Он использовал кое-какие связи."
    "Но главное - это лазейку в законе."
    img 2607
    with fade
    music Power_Bots_Loop
    "Она очень..."
    "ОЧЕНЬ!"
    "ОЧЕНЬ ХРУПКАЯ!"
    music Groove2_85
    img 2608
    "Мне очень жаль, но я не имею права Вас удерживать, Миссис Бакфетт."
    img 2609
    music RnB4_100
    m "!!!!!!!!!"
    img 2610
    music Power_Bots_Loop
    marcus "Не спешите радоваться, Миссис Бакфетт."
    "И подумайте что Вас ждет."
    "У Вас нет ничего."
    "Вы никто."
    "Нет никаких документов что Вы существуете."
    img 2611
    "У любого бомжа больше прав чем у Вас!"
    img 2612
    music RnB4_100
    m "У МЕНЯ ЕСТЬ ДРУЗЬЯ!!!"
    marcus "Вы так считаете, Миссис Бакфетт."
    "Но я думаю Вы ошибаетесь."
    img 2613
    "В любом случае Вы ненадолго покинете эти стены."
    music Power_Bots_Loop
    $ marcusCabinetState = 7
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_202

    return

label EP1_marcus_cabinet_dialogue12:
    img 2614
    with fadelong
    m "ПОЧЕМУ???"
    img 2615
    marcus "Потому что никакие обвинения с Вас не сняты."
    "Эта лазейка касается самого процесса."
    "Мы допустили незначительное нарушение."
    "Однако, хоть Вы и выйдете отсюда."
    img 2616
    "Но любое."
    img 2617
    "Я повторю!"
    "ЛЮБОЕ!"
    img 2618
    "Любое нарушение приведет Вас сюда и процесс пойдет как и раньше."
    "Любой полицейский, который проверит у Вас документы, доставит Вас сюда."
    img 2619
    "Если Вы перейдете дорогу в неположенном месте, Вас доставят сюда."
    "Если Вы станете где-то кричать, Вас доставят сюда."
    img 2620
    "В общем."
    "Шансов у Вас нет."
    "Вы вернетесь сюда."
    img 2621
    "Вам даже негде жить."
    img 2622
    "Если Вас застанут ночью спящей на улице - это нарушение закона."
    img 2623
    "Вас доставят сюда."
    img 2624
    music Groove2_85
    "Я готов поставить свой лучший виски на Ранчо 218 что Вы вернетесь сюда уже завтра."
    img 2625
    "В связи с этим у Вас есть выбор."
    img 2626
    m "Какой выбор?"
    img 2627
    marcus "Вы можете идти сейчас."
    "Прямо сейчас."
    img 2628
    "Чтобы вернуться завтра."
    img 2629
    "Либо Вы можете отказаться уходить и отправиться на Ранчо 218 прямо сейчас."
    img 2630
    "Во втором случае Вы пройдете стандартный набор Training."
    img 2631
    music Villainous_Treachery
    "Но если Вы уйдете и вернетесь завтра, то Вы начнете свой путь на Ранчо 218."
    img 2632
    "Как fuck meat."
    "С самого низа."
    "И не сможете добиться каких-либо успехов, потому что во время карьерного роста растеряете всю красоту."
    img 2633
    "..."
    img 2634
    "Я повторю."
    "То что Вы вернетесь сюда - это абсолютно точно."
    img 2635
    "Вы можете сходить погулять, но этим Вы погубите свою будущую жизнь."
    "Хорошенько подумайте."
    img 2636
    "..."
    img 2637
    m "..."
    img 2636
    marcus "..."
    img 2638
    w
    img 2639
    m "..."
    img 2636
    marcus "Итак."
    "Что Вы выбираете?"
    $ marcusCabinetState = 8
    call EP1_refresh_scene_fade() from _ep1call_refresh_scene_fade_203
    return

label EP1_marcus_cabinet_dialogue13:
    menu:
        "Выйти на свободу (временно)":
            pass
#        "Отправиться на Ранчо 218 (отдельное дополнение)":
#            help "Дополнение в разработке. Следите за новостями!"
#            jump EP1_marcus_cabinet_dialogue13
        "Продолжить думать...":
            return

    music Pyro_Flow
    img 2640
    with fadelong
    m "Я выбираю свободу, Маркус."
    img 2641
    marcus "Уффф.."
    img 2642
    "Хорошо, Миссис Бакфетт."
    "До скорой встречи."
    "Жаль, я надеялся Вы сделаете блестящую карьеру на Ранчо 218."
    "Мне жаль губить такой талант в качестве fuck meat."
    img 2643
    m "Надеюсь что не до скорой встречи, Маркус."
    img black_screen
    with Dissolve(1)
    sound snd_phone1
    $ renpy.pause(2.0)
    marcus "Вывести заключенную."
    $ steam_achievement("ach9")
    music Power_Bots_Loop
    $ policeEntranceState = 4
    $ EP1_autorun_to_object("EP1_police_entrance_s2", "EP1_entrance_dialogue7")
    call EP1_change_scene("EP1_police_entrance_s2")

    return
