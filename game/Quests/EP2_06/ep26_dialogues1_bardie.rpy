# После перехода уровня Барди и Бетти к тому, что Моника ходит дома без трусиков,
# появляется возможность придти к Барди вечером, когда он сидит в кабинете.
# до этого показывается сцена того, как Барди расслабляется перед журналом Моники и комментирует процесс
# Также делает замечание по поводу груди Моники на журнале и думает что упустил этот момент из виду.

label ep26_dialogues1_bardie1:

    return

label ep26_dialogues1_bardie1a:

    return

label ep26_dialogues1_bardie2:

    return

label ep26_dialogues1_bardie3a:

    return
label ep26_dialogues1_bardie3:
    # не рендерить
    # Моника пытается зайти к Барди в этот же день, а также при выходе из комнаты Барди

    return

label ep26_dialogues1_bardie4:

    return

label ep26_dialogues1_bardie5:

    return

label ep26_dialogues1_bardie5a:

    return

# Моника теперь может заходить на кухню.
label ep26_dialogues1_bardie6:
    # Моника заходит на кухню первый раз (либо любой раз, пока Моника еще не показывала грудь)

# Если Моника заходит так, то прибегает Бетти и говорит Монике чтобы та убиралась с кухни!
# Что ей вообще не нужны проститутки в доме и что ей уже надоело присматривать за дурной гувернанткой
# Которая так и норовит нарушить дисциплину!
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 13131
    with fadelong
    betty "Моника, гувернантка!"
    betty "Что ты делаешь здесь!"
    img 13132
    betty "Я запретила тебе заходить на кухню!"
    betty "Быстро убирайся отсюда!"
    img 13133
    with diss
    betty "И вообще... Мне не нужны проститутки в доме!"
    betty "И мне надоело присматривать за дурной гувернанткой, которая так и норовит нарушить дисциплину!"
# Моника спрашивает: есть-ли правила, которые позволяют ей питаться здесь?
# Бетти смущается и говорит что есть кое-какое правило и гувернантка сама про него знает. (злится)
# Говорит Монике чтобы та выметалась с кухни
    music Hidden_Agenda
    img 13134
    with fade
    m "Миссис Робертс..."
    m "Есть-ли правила, которые позволяют мне питаться здесь?"
    img 13135
    with diss
    betty "..."
    img 13136
    m "???"
    img 13137
    betty "!!!"
    music Groove2_85
    img 13138
    with fade
    betty "Есть кое-какое правило... И ты, гувернантка, сама знаешь про него..."
    betty "А сейчас, выметайся с кухни!"
# Моника делает выбор:
# Уйти или Оголить грудь (corruption)
    img 13139
    with diss
    $ menu_corruption = [monicaBettyKitchenBoobsCorruption]
    menu:
        "Оголить грудь...":
            pass
        "Уйти...":
            sound highheels_run2
            img 13140
            with fade
            w
            return 0
# Если оголяет: А так?
# Если оголяет первый раз, то Моника про себя думает о том что же она творит, но, с другой стороны.
# Никто кроме Бетти этого не видит и это лучше, чем разносить флаеры за еду или что-то еще похуже.
    music Hidden_Agenda
    img 13142
    with fade
    mt "Моника, что ты творишь?"
    mt "Неужели ты пойдешь на это?"
    img 13141
    with diss
    mt "С другой стороны... Никто кроме Бетти этого не видит"
    mt "И это лучше, чем разносить флаеры за еду или делать что-то еще похуже..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    #fade
    music Loved_Up
    img 13143
    with fadelong
    m "А так?"

# Бетти злится и говорит что у гувернантки нет никакого стыда.
# И чтобы та убиралась отсюда.
    img 13144
    with diss
    betty "!!!"
    img 13145
    with diss
    m "..." # Моника стервозно улыбается
    music Groove2_85
    img 13146
    with fade
    betty "Гувернантка, у тебя нет никакого стыда!"
    betty "Немедленно убирайся отсюда!"
# Моника спрашивает: Вы уверены, Миссис Робертс? Что я должна выйти отсюда?
# Бетти злится и говорит чтобы та садилась за стол.
    music Loved_Up
    img 13147
    with fade
    m "Вы уверены, Миссис Робертс!"
    m "Вы уверены что я должна выйти отсюда?"
    img 13148
    with diss
    betty "!!!"
    music Groove2_85
    img 13149
    with fade
    betty "Садись за стол, сейчас подам тебе..."
# Моника садится.
# Бетти подает еду и говорит что если Ральф увидит ее в таком виде, то ей уже ничего не поможет.
# Даже мелкий засранец, с которым Моника спелась.
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13150
    with fadelong
    betty "И не вздумай в таком виде шляться по дому!"
    betty "Если Ральф увидит тебя в таком виде, то я вышвырну тебя!"
    img 13151
    betty "И тебе никто не поможет!"
#    betty "Даже мелкий засранец Барди, с которым ты спелась!"

    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5

    $ rnd = rand(1,3)

    #
    music RnB3_65
    if rnd == 1:
        img 13167
        with fadelong
        mt "Мммм... Наконец-то я ем вкусную еду..."
        img 13168
        with diss
        mt "В своем доме..."

    if rnd == 2:
        img 13167
        with fadelong
        mt "Мой дом... Моя любимая кухня..."
        mt "Все не так уж плохо..."
        img 13168
        with diss
        mt "Это только первые шаги..."
        mt "Скоро дом будет снова мой..."

    if rnd == 3:
        #
        img 13169
        with fadelong
        mt "Ммм... Я кушаю на своей любимой кухне."
        img 13170
        with diss
        mt "А Бетти прислуживает мне..."
        mt "Так мне нравится намного больше..."

    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_plates
    music RnB3_65

#    $ images = random.sample(set(images_set1, images_set2, images_set3), 1)

    $ rnd = rand(1,3)
    if rnd == 1:
        img 13152
        with fadelong
        w
        $ images_set1 = [13153, 13154, 13155, 13156]
        $ images = random.sample(set(images_set1), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда1
        music Groove2_85
        img 13174
        with fade
        m "Миссис Робертс. Пожалуйста, подайте мне другие приборы."
        m "Эти недостаточно хорошо вымыты."
        img 13177
        betty "!!!"

    if rnd == 2:
        img 13157
        with fadelong
        w
        $ images_set2 = [13158, 13159, 13160, 13161]
        $ images = random.sample(set(images_set2), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда2
        music Groove2_85
        img 13176
        with fade
        m "Миссис Робертс. Пожалуйста, подогрейте еду."
        m "Она недостаточно горячая."
        img 13177
        betty "!!!"

    if rnd == 3:
        img 13162
        with fadelong
        w
        $ images_set3 = [13163, 13164, 13165, 13166]
        $ images = random.sample(set(images_set3), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда3
        music Groove2_85
        img 13175
        with fade
        m "Миссис Робертс. Вы вкусно готовите."
        m "Это похвально."
        img 13177
        betty "!!!"


    # Моника ест
#    img 13152
#    w
#    img 13153
#    w
#    img 13154
#    w
#    img 13155
#    mt "Мммм... Наконец-то я ем вкусную еду..."
#    img 13156
#    mt "В своем доме..."

    #
#    img 13157
#    with fade
#    w
#    img 13158
#    w
#    img 13159
#    w
#    img 13160
#    mt "Мой дом... Моя любимая кухня..."
#    mt "Все не так уж плохо..."
#    img 13161
#    mt "Это только первые шаги..."
#    mt "Скоро дом будет снова мой..."

    #
#    img 13162
#    w
#    img 13163
#    w
#    img 13164
#    w
#    img 13165
#    mt "Ммм... Я кушаю на своей любимой кухне."
#    mt "А Бетти прислуживает мне..."
#    mt "Так мне нравится намного больше..."
#    img 13166
#    mt "Мммм... Наконец-то я ем вкусную еду..."
#    mt "В своем доме..."


    # Моника поела
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13171
    with fadelong
    m "Благодарю Вас, Миссис Робертс."
    m "Я поела."
    img 13172
    betty "!!!"
    return 1

label ep26_dialogues1_bardie7:
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 13135
    with fadelong
    # Моника заходит на кухню регулярно
    # Моника делает выбор:
    # Уйти или Оголить грудь (corruption)
    menu:
        "Оголить грудь...":
            pass
        "Не оголять грудь...":
            img 13131
            with fade
            betty "Моника, гувернантка!"
            betty "Что ты делаешь здесь!"
            img 13134
            with diss
            betty "Я запретила тебе заходить на кухню!"
            betty "Быстро убирайся отсюда!"
            img 13133
            with diss
            betty "И вообще... Мне не нужны проститутки в доме!"
            betty "И мне надоело присматривать за дурной гувернанткой, которая так и норовит нарушить дисциплину!"
            return 0

#    img 13144
#    betty "!!!"
    sound snd_fabric1
    music Loved_Up
    img 13145
    with fadelong
    m "..." # Моника стервозно улыбается
    music Groove2_85
    img 13146
    betty "Гувернантка, у тебя нет никакого стыда!"
    betty "Немедленно убирайся отсюда!"
    img 13147
    with diss
    m "Вы уверены, Миссис Робертс!"
    m "Вы уверены что я должна выйти отсюда?"
    # На каждое 5-ое посещение дома, Бетти начинает козлить и идет переход на ep26_dialogues1_bardie8
    if monicaBettyKitchenEatedCount % 4 == 0 and bardieForcedBettyToFeedMonica != True:
        call ep26_dialogues1_bardie8() from _call_ep26_dialogues1_bardie8
        $ questHelp("house_22", skipIfExists=True)
        return 1
    img 13148
    betty "!!!"
    img 13149
    with diss
    betty "Садись за стол, сейчас подам тебе..."

# Если Бетти ведет себя хорошо, то:

# Бетти подает еду и говорит приятного аппетита
# Моника язвительно смотрит и просит что-то из еды еще или типа того
# Моника думает про то, что наконец-то ест в собственном доме, что это уже прогресс и что она вернет его назад.
    # еда1-3



    #

# Если Бетти ведет себя плохо.
    if monicaBettyKitchenEatedCount % 4 == 3: # Раз перед тем как откажет в еде
        $ bettyOffendedBardieKitchen = True
        img 13150
        with fade
        betty "И не вздумай в таком виде шляться по дому!"
        betty "Если Ральф увидит тебя в таком виде, то я вышвырну тебя!"
        img 13151
        betty "И тебе никто не поможет!"
#        betty "Даже мелкий засранец Барди, с которым ты спелась!"
        img 13178
        with diss
        m "Вы уверены что так следует отзываться о хозяине дома?"
        img 13179
        betty "Это не твое дело, проститутка!"

#

    # Моника ест
#    mt "Мммм... Наконец-то я ем вкусную еду..."
#    mt "В своем доме..."

    #
#    mt "Мой дом... Моя любимая кухня..."
#    mt "Все не так уж плохо..."
#    mt "Это только первые шаги..."
#    mt "Скоро дом будет снова мой..."

    #
#    mt "Ммм... Я кушаю на своей любимой кухне."
#    mt "А Бетти прислуживает мне..."
#    mt "Так мне нравится намного больше..."

    # Моника поела
#    m "Благодарю Вас, Миссис Робертс."
#    m "Я поела."
#    betty "!!!"

    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5

    $ rnd = rand(1,3)

    #
    music RnB3_65
    if rnd == 1:
        img 13167
        with fadelong
        mt "Мммм... Наконец-то я ем вкусную еду..."
        img 13168
        with diss
        mt "В своем доме..."

    if rnd == 2:
        img 13167
        with fadelong
        mt "Мой дом... Моя любимая кухня..."
        mt "Все не так уж плохо..."
        img 13168
        with diss
        mt "Это только первые шаги..."
        mt "Скоро дом будет снова мой..."

    if rnd == 3:
        #
        img 13169
        with fadelong
        mt "Ммм... Я кушаю на своей любимой кухне."
        img 13170
        with diss
        mt "А Бетти прислуживает мне..."
        mt "Так мне нравится намного больше..."

    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_plates
    music RnB3_65

#    $ images = random.sample(set(images_set1, images_set2, images_set3), 1)

    $ rnd = rand(1,3)
    if rnd == 1:
        img 13152
        with fadelong
        w
        $ images_set1 = [13153, 13154, 13155, 13156]
        $ images = random.sample(set(images_set1), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда1
        music Groove2_85
        img 13174
        with fade
        m "Миссис Робертс. Пожалуйста, подайте мне другие приборы."
        m "Эти недостаточно хорошо вымыты."
        img 13177
        betty "!!!"

    if rnd == 2:
        img 13157
        with fadelong
        w
        $ images_set2 = [13158, 13159, 13160, 13161]
        $ images = random.sample(set(images_set2), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда2
        music Groove2_85
        img 13176
        with fade
        m "Миссис Робертс. Пожалуйста, подогрейте еду."
        m "Она недостаточно горячая."
        img 13177
        betty "!!!"

    if rnd == 3:
        img 13162
        with fadelong
        w
        $ images_set3 = [13163, 13164, 13165, 13166]
        $ images = random.sample(set(images_set3), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда3
        music Groove2_85
        img 13175
        with fade
        m "Миссис Робертс. Вы вкусно готовите."
        m "Это похвально."
        img 13177
        betty "!!!"

    # Моника поела
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13171
    with fadelong
    m "Благодарю Вас, Миссис Робертс."
    m "Я поела."
#    img 13172
    betty "!!!"
    return 2

label ep26_dialogues1_bardie8:
# Через 5 посещений кухни, Бетти заявляет что правило не работает и чтобы нерадивая гувернантка убиралась отсюда.
    music Power_Bots_Loop
    img 13180
    with fade
    betty "Это дурацкое правило больше не работает!"
    betty "Я не собираюсь больше такое терпеть!"
    img 13181
    betty "Убирайся отсюда, нерадивая гувернантка!"
    betty "Пока я не вышвырнула тебя из дома на улицу!"

# Монике приходится уходить с голой грудью
    sound highheels_run2
    img 13182
    with fade
    m "!!!"
    return

label ep26_dialogues1_bardie8a:
    # не рендерить
    mt "Бетти вконец обнаглела!"
#    mt "Мне стоит пожаловаться на нее Барди!"
    return

label ep26_dialogues1_bardie9:

    return
label ep26_dialogues1_bardie9a:
    # не рендерить
    # Моника выходит
    mt "Эта мелюзга продолжает издеваться надо мной!"
    mt "Может к черту это все?"
    mt "Я найду где мне есть!"
    return
label ep26_dialogues1_bardie10:

    return

label ep26_dialogues1_bardie11:

    return

label ep26_dialogues1_bardie12:

    return


# Если Бетти зарывалась, то Моника может сказать об этом Барди в его комнате.
# Барди говорит Монике позвать Бетти

# У Бетти появляется диалог о том что Барди зовет ее в свою комнату.
# Бетти напряженно смотрит и говорит что скоро придет туда.

# После этого, в течении времени суток, если зайти в комнату Барди, идет сцена наказания Бетти.
# Бетти шлепают по попе.
# Барди говорит что поняла-ли она что хозяина дома надо слушаться.
# Бетти отвечает что да.




label ep26_dialogues1_bardie12a:
#    mt "Барди сказал что я могу питаться только днем."
    mt "Мне лучше уйти, пока Бетти на меня не наорала..."
    return

label ep26_dialogues1_bardie12b:
    mt "Я уже кушала здесь сегодня."
    mt "У меня нет желания трясти своей грудью целый день!"
    mt "Это унизительно!"
    return






























label ep26_dialogues1_bardie:
    return
