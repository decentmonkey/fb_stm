default monica_kissed_julia_cafe = False

label ep210_julia_dialogue1:
    menu:
        "Поцеловать Юлию" if day_time == "day" and ep210_julia_kissed_day_day != day:
            return 1
        "Сделать Юлии массаж." if char_info["Julia"]["level"] >= 4 and ep210_julia_massage_day != day and char_info["Julia"]["level"] < 7:
            return 3
        "Сделать Юлии массаж. (требуется ур.4) (disabled)" if char_info["Julia"]["level"] < 4:
            pass
        "Пригласить Юлию на второе свидание." if char_info["Julia"]["level"] >= 4 and ep211_julia_second_date_inited == False:
            return 4
        "Пригласить Юлию на второе свидание. (требуется ур.4) (disabled)" if char_info["Julia"]["level"] < 4:
            pass
        "Пригласить Юлию на третье свидание. (требуется ур.6) (disabled)" if ep211_julia_second_date_completed == True and char_info["Julia"]["level"] < 6 and ep212_julia_third_date_inited == False and ep212_julia_third_date_active == True:
            pass
        "Пригласить Юлию на третье свидание. (требуется ур.6)" if ep211_julia_second_date_completed == True and char_info["Julia"]["level"] >= 6 and ep212_julia_third_date_inited == False and ep212_julia_third_date_active == True:
            return 5
        "Предложить Юлии жить вместе." if ep212_monica_julia_quest2_started == True and ep213_quests_julia_stage == 0:
            return 6
#        "Предложить Юлии жить вместе. (в следующем обновлении) (disabled)" if ep212_monica_julia_quest2_started == True:
#            pass

        "Уйти.":
            return 0
    return

label ep210_julia_dialogue1_evening:
    menu:
        "Поцеловать Юлию" if day_time == "evening" and ep210_julia_kissed_day_evening != day:
            return 2
        "Уйти.":
            return 0
    return
# Офис. Кабинет Моники.
# Моника заходит в свой кабинет, Юлия сидит за своим столом
# при клике на Юлию вместо обычного меню отношений вызывыется эта сцена
label ep210_dialogues5_julia_1:
    # Юлия встает со стула и, волнуясь, говорит
    music Groove2_85
    img 16456
    with fade
    julia "Миссис Бакфетт... Я..."
    # Моника раздраженно
    img 16457
    with diss
    m "Что?!"
    img 16458
    with fade
    julia "Я хотела сказать Вам, что Ваши сотрудники, Джон и Гретта..."
    julia "Они... Они ворвались в этот кабинет и пытались задрать мое платье!"
    music Hidden_Agenda
    img 16459
    with diss
    m "И что, им это удалось?"
    img 20880
    with diss
    julia "Миссис Бакфетт, конечно я не позволила им сделать это!"
    music Groove2_85
    img 16460
    with fade
    mt "Никчемные и бесполезные сотрудники..."
    img 20878
    with diss
    julia "Миссис Бакфетт, они нарушают рабочую атмосферу своим поведением!"
    music Hidden_Agenda
    img 22025
    with fade
    m "Я ничего не знаю!"
    m "Просто так они не стали бы это делать."
    m "Значит, они выполняют какое-то важное распоряжение начальства!"
    music Groove2_85
    img 22026
    with diss
    julia "???"
    julia "Какое важное распоржение, Миссис Бакфетт?"
    julia "Посмотрет мои трусики?!"
    img 22027
    with fade
    m "А я тут причем? Они просто выполняют свою работу..."
    img 22024
    with diss
    julia "Как Вы ни причем?"
    julia "..."
    julia "Это же по Вашему приказу они это делают..."
    # Моника с безразличным видом
    music Hidden_Agenda
    img 22015
    with fade
    m "Я не помню такого..."
    m "Мне до этого вообще нет дела... До каких-то низкоуровневых сотрудников."
    # Юлия удивленно
    music Groove2_85
    img 22022
    with diss
    julia "Но, Миссис Бакфетт... Как же так?"
    julia "Вы совсем недавно пытались ущипнуть меня... И поцеловать..."
    julia "Я пытаюсь понять причину, почему Вы так делаете..."
    img 22016
    with diss
    julia "Вы..."
    julia "Вы пытаетесь сблизиться со мной?"
    julia "Вы ко мне неравнодушны?"
    # Моника удивлена
    sound plastinka1b
    music stop
    img 16461
    with fade
    m "!!!"
    m "С чего ты это взяла?!"
    # Юлия смущенно
    music Hidden_Agenda
    img 16462
    with diss
    julia "Вы мне тоже очень... Нравитесь..."
    julia "Но я всегда боялась Вам сказать об этом..."
    # Моника смотрит на нее удивленно
    music Groove2_85
    img 16463
    with diss
    mt "Я ей нравлюсь?"
    mt "???"
    menu:
        "Подыграть Юлии.":
            pass
        "Как она могла про такое подумать?! (завершение сюжета с Юлией)":
            music Pyro_Flow
            img 16464
            with fade
            m "Юлия!!!"
            m "Ты о чем вообще говоришь?!"
            img 22017
            with diss
            m "Как ты могла подумать, что такой как Я!"
            m "Может понравится девушка твоего уровня?!"
            m "Ты совсем глупая?!"
            img 16465
            with diss
            mt "!!!"
            img 22350
            with fade
            m "Перестань отвлекать меня от работы этой чушью!"
            m "И сама иди займись работой!!!"
#            img 22883
#            with diss
            mt "Никчемная глупая помощница!!!"
            mt "!!!"
            return False
    music Hidden_Agenda
    img 21913
    with fade
    mt "Хммм..."
    mt "Это отличный способ выяснить то, что мне нужно..."
    mt "По-другому никак - она слишком быстро прыгает."
    mt "Сейчас мне просто нужно подыграть ей!"
    mt "Притворюсь, что она тоже мне нравится."
    mt "..."
    img 16466
    with diss
    mt "Я же не могу рассказать ей про настоящую причину своего поведения..."
    mt "Про мерзавца Фреда. Иначе она узнает правду про меня. А мне этого не нужно."
    mt "..."
    img 21952
    with diss
    mt "Я эту глупую Юлию могу легко обмануть..."
    mt "Скажу, что она мне нравится..."
    mt "И она мне все расскажет и все покажет!"
    mt "Это гениально, Моника!"
    # Моника смотрит на Юлию
    music Loved_Up
    img 16467
    with fade
    m "Я думала, что скажу об этом тебе позже..."
    m "Но ты и правда мне нравишься."
    img 16468
    with diss
    julia "!!!"
    img 16469
    with diss
    m "Именно поэтому я щипала тебя за попу..."
    img 16470
    with hpunch
    julia "Это правда?!"
    julia "Я Вам нравлюсь?!"
    julia "Поэтому Вы... Хотите залезть ко мне в трусики?"
    img 16471
    with diss
    m "Да, Юлия..."
    julia "Я просто не могу поверить, что я вам и правда нравлюсь..."
    julia "Вы такая красивая и умная. Как я могу вам нравиться?"
    music Hidden_Agenda
    img 16472
    with fade
    mt "Черт! Мне ей еще и доказывать это придется?!"
    mt "И уговаривать?!"
    mt "!!!"
    img 16473
    with diss
    mt "С другой стороны..."
    mt "Думаю, этот способ сработает с точностью в тысячу процентов."
    mt "Так что я попробую."
    # Моника подходит к Юлии и обнимает ее, при этом пытается поднять ее платье.
    # платье чуть приподнимается сбоку, но так что трусиков не видно, либо это место закрыто рукой!
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 16474
    with fadelong
    w
    sound Jump1
    img 16475
    with fade
    w
    img 16477
    with diss
    m "Да, я мечтаю залезть к тебе в трусики, Юлия..."
    # Юлия придерживает платье рукой и отстраняется
    # Юлия, смущаясь
    img 16476
    with fade
    sound snd_fabric1
    w
    img 16478
    with diss
    w
    sound Jump2
    img 16479
    with diss

    julia "Миссис Бакфетт... Сначала нам нужно узнать друг друга лучше."
    music Groove2_85
    img 16480
    with fade
    m "И что ты хочешь от меня?"
    img 20930
    with diss
    julia "Ну не знаю..."
    julia "Сначала люди ходят на свидания... Можно сходить в кафе и попить кофе."
    img 16481
    with fade
    mt "Кафе?"
    mt "..."
    img 16482
    with diss
    m "Ну хорошо. Куда ты хочешь?"
    m "Я не могу тебя вести в те пафосные места, куда хожу обычно..."
    m "Боюсь, ты будешь чувствовать себя неудобно."
    img 16483
    with fade
    m "Выбирай то место, которое нравится тебе."
    m "Например, рядом с твоим домом. Кстати, где ты живешь?"
    img 16484
    with diss
    julia "Я живу рядом с трущобами..."

    if monicaWorkingAsDishwasher == True:
        #
        img 16485
        with fade
        $ notif(t_("Моника работает в пабе Shiny Hole"))
        mt "Надеюсь, не рядом с Shiny Hole..."
        #
    music Hidden_Agenda
    img 16486
    with diss
    m "Я хочу доказать тебе, что ты мне и правда нравишься..."
    m "Поэтому с удовольствием пойду с тобой в то кафе, где ты обычно бываешь."
    m "Хочу узнать тебя получше..."
    mt "Боже. Моника, что за чушь ты несешь?"
    # Юлия радостно
    music Groove2_85
    img 16487
    with fade
    julia "Правда?!"
    julia "У меня рядом с домом есть кафе!"
    julia "Мы можем пойти туда. А когда?"
    img 16488
    with diss
    m "Думаю, завтра... Сегодня у меня много дел."
    img 16489
    with fade
    mt "Уверена в том, что мне удастся улучить момент и подсмотреть ей под юбку..."
    img 16490
    with diss
    julia "Хорошо, Миссис Бакфетт!"
    julia "Завтра встретимся с Вами в кафе."
    sound highheels_short_walk
    img 16491
    with fade
    mt "Фи... На какие жертвы приходится идти из-за этой глупой просьбы Фреда..."
    # далее обычный рабочий день.
#    $ log1 = t_("Я решила подыграть этой никчемной Юлии. Отличный способ узнать цвет ее трусиков.") # квест лог
    return

# при клике на Юлию после назначения 1-го свидания
label ep210_dialogues5_julia_1_2:
    music Loved_Up
    img 16468
    with fadelong
    julia "Миссис Бакфетт, я не могу дождаться нашего свидания в кафе!"
    julia "Скорее бы наступил завтрашний день!"
    return

# Моника на следующий день приходит на работу
# становится доступным кафе в трущобах
label ep210_dialogues5_julia_2:
    # Юлии нет на рабочем месте
    mt "А где эта никчемная помощница?!"
    mt "Вот черт! Я совсем забыла..."
    mt "Я же договорилась с ней сегодня сходить в кафе."
    mt "Оно находится где-то рядом с трущобами."
    mt "Мне нужно сейчас идти на свидание с Юлией."
    return

label ep210_dialogues5_julia_2a:
    if ep211_julia_comment_day1 != day:
        mt "А где эта никчемная помощница?!"
        mt "Вот черт! Я совсем забыла..."
        mt "Я же договорилась с ней сегодня сходить в кафе."
        mt "Мне нужно сейчас идти на свидание с Юлией."
    $ ep211_julia_comment_day1 = day
    return

# ранее:
# Моника призналась, что она сама испачкала ковер и Юлия добровольно оттирала пятно
# Моника призналась, что испачкала ковер и заставила Юлию оттирать пятно
# Моника обвинила Юлию в порче ковра и заставила оттирать пятно, а потом ее уволила
# Моника обвинила Юлию в порче ковра и заставила оттирать пятно, потом простила и оставила на работе
# в зависимости от того, как Моника относилась к Юлии, у них будет развиваться разговор в баре

# Моника стоит перед кафе, мысли при клике на кафе
label ep210_dialogues5_julia_3_1:
    mt "Фи. Какая-то дешевая забегаловка."
    return

# Моника стоит перед кафе (глазик)
label ep210_dialogues5_julia_3_2:
    mt "Мне придется притвориться, что эта никчемная Юлия мне нравится."
    mt "Поверить не могу. Это же моя бывшая гувернантка..."
    mt "Как такая, как она, может понравиться такой леди, как Я?!"
    return False

label ep210_dialogues5_julia_3_3: # На улице, глазик на Монику, либо на Юлию, либо клик на дом Юлии
    mt "Мне надо добиться чтобы она позвала меня в гости."
    mt "Там я смогу увидеть цвет этих проклятых трусиков!.."
    return False

label ep210_dialogues5_julia_3_4: # На улице, Моника говорит с Юлией
    m "Юлия, может быть ты пригласишь меня к себе в гости?"
    julia "Миссис Бакфетт, это слишком рано..."
    julia "Я еще не готова к этому..."
    julia "Спасибо за вечер, мне очень понравилось!"
    mt "Проклятие!.."
    return

label ep210_dialogues5_julia_3_4a: # Приходит в неправильной одежде
    mt "Мне лучше не ходить на свидание с Юлией в этом!"
    mt "Надо одеть мое красивое платье!"
    return

label ep210_dialogues5_julia_3_5: #Глазик на дом Юлии
    mt "Значит в этой холупе обитает Юлия?"
    mt "Я не удивлена..."
    return
label ep210_dialogues5_julia_3_6: #Глазик на кафе
    mt "Убогое кафе, с убогими клиентами, в убогом районе..."
    return
label ep210_dialogues5_julia_3_7: #Попытка зайти в кафе
    mt "У меня нет желания покупать еду по их ценам!"
    mt "Они слишком завышены для такой дыры!"
    mt "..."
    mt "Хотя... Может быть попробовать устроиться туда работать?"
    mt "Нет! Не хватало еще чтобы меня там заметила Юлия!"
    mt "Да и бариста там какая-то дура!"
    return

label ep210_dialogues5_julia_3_8:
    $ menu_price = [15,0]
    menu:
        "Идти на свидание к Юлии.":
            return True
        "Уйти.":
            return False
    return

# Моника заходит в кафе в трущобах
label ep210_dialogues5_julia_3:
    # Юлия сидит за столиком, на столике две чашки. одна для Юлии, вторая для Моники
    # Моника садится к ней за столик
    music stop
    img black_screen
    with Dissolve(1)
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_71
    img black_screen
    with Dissolve(1)
    sound highheels_short_walk
    music Stealth_Groover
    pause 1.0
    img 23076
    with fadelong
    mt "Надо же, какая она радостная..."
    img 23077
    with fade
    sound highheels_short_walk
    mt "Ну что ж, не буду портить ей настроение..."
    img 23078
    with diss
    cafe_visitor2 "Ого! Вот это телка!"
    music Groove2_85
    img 23079
    with fade
    julia "Миссис Бакфетт, я так рада, что Вы пришли!"
    julia "Я заказала Вам сок. И еще... Кхм..."
    img 23080
    with diss
    m "Что?"
    img 23081
    with fade
    julia "Я... Просто я Вас уже давно жду здесь и решила заказать себе обед..."
    img 23082
    with diss
    julia "Вы же не будете против, Миссис Бакфетт?"
    img 23083
    with fade
    mt "Зачем она мне это рассказывает? Мне должно быть это интересно?!"
    mt "Какая мне разница, что там себе заказала эта никчемная Юлия?"
    img 23084
    with diss
    m "Хорошо, Юлия. Конечно, я не против." # улыбка
    img 23086
    with fade
    julia "Спасибо, Миссис Бакфетт!"
    julia "Я так переживала, что Вы скажете мне самой оплачивать чек..."
    img 23085
    with diss
    sound snd_eating
    julia "А у меня совсем нет денег."
    julia "Я пока еще очень мало зарабатываю на моей новой работе."
    julia "А Вы самая богатая леди этого города."
    julia "Для Вас это сущий пустяк..."
    music Power_Bots_Loop
    img 23088
    with hpunch
    mt "?!"
    mt "?!?!?!"
    sound snd_eating
    img 23087
    with diss
    mt "Это Я должна оплачивать ее обед?!"
    mt "?!?!?!"
    music Pyro_Flow
    img 23089
    with fade
    m "Да, Юлия..."
    m "Конечно... Для меня это пустяк..."
    m "Ты права..."
    img 23090
    with diss
    m "Это заведение настолько дешевое, что я даже не замечу изменения баланса на моей кредитной карте!"
    img 23091
    with diss
    m "Да и честно, здесь такие посетители, что среди них дискомфортно находиться такой леди как Я!"
    music Groove2_85
    img 23092
    with fade
    w
    sound highheels_short_walk
    img 23093
    with diss
    cafe_visitor1 "Можно убирать еду!"
    cafe_visitor1 "У меня пропал аппетит!"
    img 23094
    with fade
    w
    img 23095
    with diss
    cafe_visitor1 "!!!"
    img 23096
    with fade
    mt "!!!"
    img 23097
    with diss
    sound highheels_short_walk
    w
    music stop
    img black_screen
    with diss
    sound snd_eating
    pause 1.0
    music Groove2_85
    img 23098
    with fadelong
    mt "Черт!"
    mt "Бестолковая Юлия!"
    mt "Хорошо что у меня есть деньги на этот дурацкий обед!"
    mt "Но какой ценой они мне достались!"
    img 23099
    with fade
    m "..."
    julia "Миссис Бакфетт, я всю ночь не могла уснуть..."
    julia "Неужели, я Вам и правда нравлюсь?"
    music Hidden_Agenda
    img 23100
    with diss
    m "Это правда, Юлия."
    m "Я хочу узнать тебя поближе и..."
    music Pyro_Flow
    img 23101
    with diss
    mt "Узнать цвет твоих трусиков!"
    music Hidden_Agenda
    img 23102
    with fade
    m "И проводить с тобой больше времени."
    music Groove2_85
    img 23103
    with diss
    julia "Не могу поверить в это..."
    julia "Вы такая красивая и успешная женщина, настоящая леди..."
    julia "Что Вы могли найти в такой как я?"
    img 23104
    with fade
    mt "Я что, должна сейчас ей делать комплименты какие-то?"
    mt "И как это делать?!"
    img 23105
    with diss
    m "..."

    # Моника перечисляет
    music Loved_Up
    img 23106
    with fade
    m "Ты очень милая и добрая."
    m "В моем окружении редко можно встретить таких людей..."
    img 23107
    with diss
    julia "..."
    img 23108
    with fade
    m "Ты очень ответственная и старательно выполняешь все поручения..."
    m "И еще..."
    img 23109
    with diss
    m "Ты очень красивая..."
    img 23110
    with fade
    sound Jump2
    w
    music Power_Bots_Loop
    img 23111
    with diss
    mt "!!!"
    mt "Сучка, уйди отсюда! Это не для твоих ушей!"


    if juliaPunished == True or juliaPunishedLow == True:
    # если Моника заставляла Юлию оттирать пятно на ковре
        #
        music Groove2_85
        img 23112
        with fade
        julia "Почему тогда Вы так со мной обращались, Миссис Бакфетт?"
        $ notif(t_("Моника заставляла Юлию оттирать пятно на ковре"))
        img 23113
        with diss
        mt "Черт!"
        mt "Надо что-то придумать..."
        mt "..."
        #

    music Hidden_Agenda
    img 23114
    with fade
    m "Я не могла понять, что меня в тебе так притягивает..."
    m "..."
    img 23115
    with diss
    m "И злилась на это. Поэтому так вела себя."
    img 23116
    with fade
    julia "А сейчас что изменилось?"

    img 23117
    with diss
    m "Я решила, что мне нужно сделат каминг аут, несмотря на то, что скажут остальные..."
    m "Я устала притворяться и выдавать себя не за ту, какая я есть настоящая."
    m "При этом скрывать свои чувства к другой девушке..."
    m "Хоть она и совершенно другого, несравнимого с моим, социального статуса... Гувернантка."
    music Groove2_85
    img 23118
    with fade
    julia "Это очень смелый поступок, Миссис Бакфетт."
    julia "И я готова поддержать Вас."
    #
    img 23119
    with diss
    mt "Что за чушь мне приходится говорить?!"
    mt "!!!"
    mt "Как бы подсмотреть ей под платье?"
    mt "???"
    img 23120
    with diss
    julia "Мне нужно время, чтобы привыкнуть к этому..."

    # Моника роняет ложку на пол
    music Hidden_Agenda
    img 23121
    with fade
    mt "Возможно, сейчас у меня получится заглянуть ей под платье..."
    # наклоняется под стол за ней
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать. (завершение сюжета с Юлией)":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть в эту глупую игру мерзавца Фреда!"
            mt "Да еще и притворяться перед никчемной Юлией!"
            mt "!!!"
            # садится за столик прямо
            music Pyro_Flow
            img 23166
            with diss
            sound highheels_short_walk
            m "Юлия, забудь о том, что я тебе тут наговорила."
            m "У меня сегодня полно других, более важных дел."
            julia "Но... Миссис Бакфетт!"
            m "Просто забудь!"
            m "!!!"
            # встает и уходит
            return False
    # но Юлия снова закрывается и Моника ничего не видит
    img 23122
    with diss
    sound Jump1
    mt "..."
    img 23123
    with diss
    sound vjuh3
    sound2 snd_forkfall
    m "Ой, я уронила столовый прибор!"
    img 23124
    with fade
    w
    sound Jump2
    img 23125
    with hpunch
    mt "Черт!!!"
    mt "Как обычно!"
    mt "!!!"
    img 23126
    with fade
    w
    img 23127
    with diss
    w
    # Моника поднимает ложечку и садится прямо за стол
    # Юлия смущенно
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 23128
    with fadelong
    julia "Миссис Бакфетт, зачем Вы подглядываете мне под платье?"
    # Моника без особо энтузиазма
    img 23129
    with fade
    m "Потому что ты мне нравишься..."
    music stop
    img black_screen
    with diss
    pause 1.5
    # Юлия смущается
    music Hidden_Agenda
    img 23130
    with diss
    m "Юлия, а ты вообще носишь трусики?"
    img 23131
    with fade
    julia "Да, Миссис Бакфетт..."
    img 23132
    with diss
    m "А какого они цвета?"
    music Groove2_85
    img 23133
    with fade
    julia "Миссис Бакфетт, это слишком личное..."
    img 23134
    with diss
    julia "И еще слишком рано обсуждать такие вещи..."
    img 23135
    with fade
    m "А сколько должно пройти времени?"
    img 23136
    with diss
    sound vjuh3
    w
    img 23137
    with diss
    w
    img 23138
    with diss
    sound Jump1
    w
    img 23139
    with diss
    cafe_barista "..."
    img 23140
    with fade
    cafe_barista "Ваша вилка, Мэм..."
    cafe_barista "И, кстати, если Вам интересно узнать, то..."
    music Pyro_Flow
    m "!!!"
    img 23141
    with diss
    m "Попрошу Вас не беспокоить нас!!!"
    m "У нас важный разговор, Вы мешаете нам!"
    m "Исчезните!!!"
    music Groove2_85
    img 23142
    with fade
    sound highheels_short_walk
    cafe_barista "Да, Мэм. конечно! Не смею вам мешать..."
    img 23143
    with diss
    sound highheels_short_walk
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 23144
    with fade
    julia "Я читала в одной книжке... О похожих отношениях... Таких как у нас с Вами..."
    julia "Это все... плохо закончилось там..."
    img 23145
    with diss
    m "Юлия, не бери в голову разные дурацкие книжки."
    m "Все будет хорошо, если мы захотим этого... Доверься мне..."
    music Loved_Up
    img 23146
    with fade
    julia "Возможно Вы правы, Миссис Бакфетт..."
    julia "В той книжке начальница каждый день целовала свою подчиненную... Говорила ей комплименты."
    # еще больше смущаясь
    img 23147
    with diss
    julia "И я хочу также..."
    # Моника психует
    music Power_Bots_Loop
    img 23148
    with fade
    mt "Кто написал такую дурацкую книжку?!"
    mt "!!!"
    mt "Теперь мне придется заниматься этими глупостями!"
    mt "Только для того, чтобы втереться этой никчемной Юлии в доверие!"
    music Hidden_Agenda
    img 23149
    with diss
    m "..."
    m "Если я буду делать также, ты мне поверишь?"
    music Loved_Up
    img 23150
    with fade
    julia "Да, Миссис Бакфетт..."
    music Hidden_Agenda
    img 23151
    with diss
    mt "Хорошо было бы попасть к ней в гости и там посмотреть, какого цвета у нее белье..."
    img 23152
    with fade
    m "Юлия, а ты живешь где-то рядом?"
    m "Может быть, пригласишь меня к себе в гости?"
    m "Я хочу посмотреть, как ты живешь..."
    music Groove2_85
    img 23153
    with diss
    julia "Миссис Бакфетт, после одного свидания в гости я Вас не могу пригласить..."
    julia "Мне нужно время, чтобы привыкнуть к этому..."
    julia "И вообще поверить, что я действително нравлюсь Вам."
    julia "..."
    music Power_Bots_Loop
    img 23154
    with fade
    mt "!!!"
    music Hidden_Agenda
    img 23155
    with diss
    m "Хорошо, я не буду торопить тебя."
    m "Сейчас мне нужно идти по делам."
    m "Встретимся в офисе..."
    # они встают
    # Юлия вопросительно на нее смотрит
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 23156
    with fadelong
    w
    img 23157
    with fade
    w
    img 23158
    with diss
    mt "Она что, ждет чего-то от меня?!"
    mt "Что она там говорила про свою дурацкую книжку?"
    mt "Каждый день ее нужно целовать и говорить комплименты?"
    menu:
        "Поцеловать Юлию.": #corruption
            # Моника наклоняется к Юлии и целует ее в щечку
            music Loved_Up
            img 23159
            with fade
            sound snd_kiss2
            w
            pass
            $ monica_kissed_julia_cafe = True
        "Не целовать.":
            music Power_Bots_Loop
            mt "Нет, я не хочу этого делать!" # сердито
            mt "Не хочу и не буду!"
            mt "Что за глупости?!"
            mt "!!!"
#            return False
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 23160
    with fade
    cafe_barista "С вас $ 25!"
    img 23161
    with diss
    w
    img 23162
    with diss
    w
    img 23163
    with fade
    w
    music Pyro_Flow
    img 23164
    with diss
    m "Я не ела это пирожное и не буду платить за него!"
    m "Это не вопрос денег."
    m "Это вопрос принципа!"
    music Groove2_85
    img 23165
    with fade
    cafe_barista "Хорошо, мэм. Тогда $ 15."
#    $ log1 = t_("Мне нужно каждый день целовать Юлию и говорить ей комплименты.") # квест лог
    return

# если Моника все делает правильно, то уровень Юлии повышается
# 2-е свидание становится доступно, когда Юлия достигает определенного уровня
# для 2-го свидания у Моники должны быть деньги, чтобы угостить Юлию

# Офис. Кабинет Моники. Моника, придя на работу
label ep210_dialogues5_julia_4_1:
    music Groove2_85
    img 16495
    with fadelong
    mt "Мне нужно просто чмокнуть ее в щечку..."
    mt "В это же нет ничего такого?"
    mt "Так я смогу втереться к ней в доверие."
    img 16496
    with fade
    sound highheels_short_walk
    m "..."
    # подходит к Юлии и целует ее в щечку
    music Loved_Up
    img 16497
    with diss
    m "Я так соскучилась по тебе..."
    m "Милая..."
    m "Ты прекрасно выглядишь сегодня."
    img 16498
    with fade
    sound snd_kiss2
    w
    # Юлия смущенно
    img 16499
    with diss
    julia "Миссис Бакфетт... Спасибо. Мне так приятно..."
    return

# Офис. Кабинет Моники.
label ep210_dialogues5_julia_4_2:
    music Groove2_85
    img 21954
    with fadelong
    julia "Миссис Бакфетт?"
    img 22294
    with fade
    mt "Ну что еще ей от меня нужно?!"
    mt "!!!"
    music Hidden_Agenda
    img 16492
    with diss
    m "Да, милая?"
    # Юлия встает и подходит к Монике
    music Groove2_85
    img 16493
    with fade
    julia "Вы, наверное, устали?"
    julia "Хотите, я Вам помассирую плечи?"
    menu:
        "Да, Юлия. Хорошая идея.":
            pass
        "Нет, не отвлекай меня от работы.":
            img 20889
            with diss
            m "Нет, Юлия!" # сердито
            m "Мне сейчас не до этого!"
            music Power_Bots_Loop
            img 16494
            with fade
            mt "Что за глупости?!"
            mt "!!!"
            music Groove2_85
            img 16500
            with diss
            m "Иди работай. И не отвлекай меня."
            img 22341
            with fade
            julia "..." # садится на свое место
            return False
    # Юлия делает Монике массаж на плечи, Моника закрывает глаза и расслабляется
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 16501
    with fadelong
    w
    img 16502
    with fade
    w
    img 16503
    with diss
    mt "Боже. Как же приятно!"
    mt "Я так давно не была на массаже..."
    mt "Пожалуй, в этом нелепом притворстве есть свои плюсы."
    img 16504
    with fade
    m "Ммммм..."
    img 16505
    with diss
    w
    # Юлия закончила массировать плечи
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 16506
    with fade
    julia "Вам понравилось, Миссис Бакфетт?"
    img 16507
    with diss
    m "Да, очень..."
    m "Спасибо, милая."
    # Юлия наклоняется к Монике и чмокает ее в щеку
    music Loved_Up
    img 16508
    with fade
    sound snd_kiss2
    w
    if ep212_monica_julia_quest2_started == False:
        music Hidden_Agenda
        img 16509
        with diss
        mt "Ого! Даже так?!"
        mt "Чувствую, я на верном пути..."
    # Юлия садится на свое место
    return True

# Офис. Кабинет Моники. Моника, уходя с работы
label ep210_dialogues5_julia_4_3:
    music Groove2_85
    img 20294
    with fadelong
    mt "Теперь мне нужно поцеловать ее, прощаясь..."
    img 16510
    with fade
    sound highheels_short_walk
    m "..."
    # подходит к Юлии и целует ее в щечку
    img 16512
    with diss
    sound snd_kiss2
    w
    music Loved_Up
    img 16511
    with fade
    m "Мне пора идти по делам."
    m "До встречи..."
    m "Милая..."
    m "Буду скучать по тебе."
    # Юлия смущенно
    img 16513
    with diss
    julia "Миссис Бакфетт... Я тоже по Вам буду скучать..."
    return

# Моника приходит утром на работу
label ep210_dialogues5_julia_5_1:
    music Hidden_Agenda
    img 20277
    with fadelong
    menu:
        "Сделать Юлии массаж.":
            pass
        "Пригласить Юлию на второе свидание. (в следующем обновлении)":
            return False
    return

# если выбран пункт меню "Сделать Юлии массаж"
# Офис. Кабинет Моники.
label ep210_dialogues5_julia_5:
    music Hidden_Agenda
    img 23051
    with fadelong
    mt "Что бы мне такого еще сделать для Юлии?"
    mt "Я должна как-то расположить ее к себе."
    mt "..."
    mt "Хммм..."
    mt "Массаж - это хорошая идея."

    # Моника подходит к столу Юлии
    sound highheels_short_walk
    img 23052
    with fade
    m "Юлия, милая, ты так много работаешь..."
    m "Тебе нужно отдохнуть немного."
    m "Пойдем в комнату отдыха, посидим там немного? Отдохнем."
    img 23053
    with diss
    julia "Спасибо, Миссис Бакфетт."
    julia "Я и правда устала. А еще так много работы..."
    # она садится на диванчик в комнате отдыха
    # Моника подходит к ней и кладет Юлию на диван
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 23054
    with fadelong
    m "Не переживай, я не буду делать ничего такого..."
    img 23055
    with fade
    m "Просто помогу тебе немного расслабиться. Сделаю массаж."
    img 23056
    with diss
    m "Ты можешь довериться мне..."
    img 23057
    with fade
    m "Милая."
    # делает массаж ног, все выше и выше, пытаясь подсмотреть
    img 23058
    with diss
    w
    img 23059
    with diss
    w
    img 23060
    with fade
    # Юлия лежит, балдеет
    w
    img 23061
    with diss
    m "Тебе приятно, Юлия?"
    julia "Мне приятно, Миссис Бакфетт..."
    img 23062
    with diss
    m "А так?"
    julia "Да..."
    if ep212_monica_julia_quest2_started == True:
        img 23064
        with fade
        m "Все, Юлия!"
        img 23065
        with diss
        julia "Да, Миссис Бакфетт..."
        julia "Спасибо за массаж. Мне очень понравилось."
        # уходит и садится на свое место
        sound highheels_short_walk
        img 23066
        with fade
        w
        return False
    img 23063
    with diss
    menu:
        "Заглянуть Юлии под платье.":
            pass
        "Не заглядывать.":
            music Power_Bots_Loop
            mt "Нет, я не буду этого делать!"
            mt "Мне надоело играть в эту глупую игру мерзавца Фреда!"
            mt "Да еще и притворяться перед никчемной Юлией!"
            mt "!!!"
            music Groove2_85
            img 23064
            with fade
            m "Все, Юлия!"
            img 23065
            with diss
            julia "Да, Миссис Бакфетт..."
            julia "Спасибо за массаж. Мне очень понравилось."
            m "Иди работай!" # сердито
            # уходит и садится на свое место
            sound highheels_short_walk
            img 23066
            with fade
            w
            return False
    # Юлия снова закрывается и Моника ничего не видит
    music Loved_Up
    img 23067
    with fade
    w
    img 23068
    with diss
    w
    sound plastinka1b
    music stop
    img 23069
    with diss
    w
    sound Jump1
    img 23070
    with fade
    julia "Ахххх!"
    music Power_Bots_Loop
    img 23071
    with diss
    mt "Черт!!!"
    mt "Как обычно!"
    mt "!!!"
    mt "Ну сколько можно?!"
    music Groove2_85
    img 23072
    with fade
    julia "Миссис Бакфетт, я еще к этому не готова."
    img 23073
    with diss
    m "Конечно... Милая..."
    m "..."
    img 23074
    with diss
    m "Я тебя не тороплю..." # выдавливает из себя улыбку
    img 23075
    with fade
    sound snd_kiss2
    julia "Спасибо за массаж. Мне очень понравилось."
    sound highheels_short_walk
    pause 1.0
    # чмокает Монику в щечку и уходит за свой стол. Моника сидит на диване сердитая
    music Pyro_Flow
    img 22386
    with fade
    mt "Я была почти у цели!!!"
    mt "!!!"
    mt "Еще бы чуть-чуть и я смогла бы закончить весь этот цирк!"
    mt "Как же меня это бесит!"
    mt "Никчемная бесполезная Юлия!!!"
    mt "!!!"
    return True




########################## в v0.11 #############

# Моника заходит в кафе в трущобах
label ep210_dialogues5_julia_6:
    # садятся за столик, заказывают ужин
    # Моника - расскажи о себе. я тут поняла, что совсем ничего о тебе не знаю
    # Юлия говорит, что она с состоятельной семьи из другой страны, но она не хочет к ним возвращаться
    # они никогда ее не понимали и не поддерживали, поэтому она уехала и пытается жить самостоятельно
    # Моника - почему ты не хочешь возвращаться, а работаешь здесь
    # Юлия - должно произойти нечто экстраординарное, чтобы я вернулась к ним.
    # Моник про себя - странно. дома у нее богатая семья и не будет никакой нужды, а она здесь работает за копейки
    # Моника про себя - никогда не понимала логику неудачников...
    # Моника - а сейчас ты живешь здесь, в трущобах?
    # Юлия - да, я арендую тут квартиру.
    # Моника про себя - хмм.. арендовать квартиру в трущобах - это наверное недорого?
    # Моника - но жить в трущобах!! фи!
    # Моника - с другой стороны... не будет деревенщины Бетти и озабоченного сопляка Барди...
    # сколько уже можно работать за еду на эту семейку идиотов.
    # мне нужно будет подумать об этом...
    # Юлия - Миссис Бакфетт, спасибо за ужин. и я хотела бы... в знак благодарности за вечер...
    # стесняюсь что такая леди как вы в такой конуре как у меня
    # пригласить Вас к себе домой.
    # Моника говорит что да, это, конечно, будет шокирующе для меня и непривычно, но ради моих чувств к тебе я готова пойти бла бла бла
    # Моника - отлично! я почти у цели! действительно, замечательный вечер!
    # Моника - да, я с радостью
    # уходят с кафе
    return

# мысли Моники перед домом Юлии
label ep210_dialogues5_julia_7:
    # какой кошмарный дом! и как люди тут живут?!
    # наверняка, одни неудачники и... извращенцы!
    # и тут небезопасно вечером...
    # нет. вряд ли я смогу жить в таких условиях
    # такая леди, как я, никогда не сможет привыкнуть к таким условиям
    # Хотя для меня и это место сейчас бы подошло
    return

# Моника в квартире у Юлии
label ep210_dialogues5_julia_8:
    # Моника говорит, что здесь очень уютно
    # Юлия смущается
    # Моника подходит к ней и обнимает, поцелуй
    # кладет руку ей на талию, потом смещает руку на попу, пытаясь поднять платье
    # Юлия отстраняется, говорит, что еще не готова
    # Моника говорит - дай, я тебя просто потрогаю и не более
    # Юлия смущается, но соглашается
    # снова поцелуй, Моника трогает ее попу и нащупывает трусики
    # Моника про себя - я почти у цели. осталось уговорить ее задрать платье
    # Моника опускает руку немного ниже и пытается залезть под платье
    # но Юлия снова отстраняется и говорит, что на сегодня этого будет достаточно
    # Моника - черт! может, попроситься в туалет? ванная со стиральной машинкой будет наверное там же
    # спрашивает у Юлии и идет в туалет
    # в ванной открывает шкафчик или машинку и ищет трусики, находят а там несколько штук и все разные
    # Моника злится, что снова не удалось ничего выяснить
    # поцелуй, до завтра, милая
    return
