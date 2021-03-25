
label gallery_11146:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11140
    with fadelong
    m "Добрый день, Мистер."
    m "Можно к Вам обратиться?"
    music Loved_Up
    img 11141
    with fade
    cit3 "О! Какая деточка! Пойдем в примерочную?"
    m "Мистер... Я бы хотела предложить Вам купить это платье..."
    music Groove2_85
    img 11142
    cit3 "Так ты продавец?"
    # corruption +1 req 80
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            return
    music Hidden_Agenda
    img 11143
    with fade
    m "Я... Я работаю здесь манекеном."
    cit3 "Ха-ха! Значит ты продаешь это платье?"
    m "Да..."
    music Loved_Up
    img 11144
    with fade
    cit3 "Красивое платье! Но под него мне нужна соответствующая детка!"
    cit3 "Я как раз планирую познакомиться с какой-нибудь."
    cit3 "Встань поближе, я хочу посмотреть размер. Мне надо найти такую детку, чтобы платье ей подошло!"
    # corruption +1 req 80
    menu:
        "Встать ближе.":
            pass
        "Уйти.":
            return
    # Замеряет руками
    img 11145
    with fade
    w
    sound Jump2
    img 11146
    with diss
    cit3 "Значит у нее должны быть вот такие сиськи..."
    img 11147
    with diss
    W
    sound Jump1
    img 11148
    with diss
    cit3 "И вот такая задница."
    img 11149
    with diss
    w
    img 11150
    with diss
    w
    img 11151
    with diss
    w
    music Groove2_85
    img 11152
    with fade
    cit3 "Хорошо! Я запомнил!"
    cit3 "Как только я найду подходящую детку, я куплю это платье!"
    mt "Урод!!!"
    return

label gallery_11185:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11153
    with fadelong
    m "Добрый день, Мистер."
    m "Можно к Вам обратиться?"
    img 11154
    with diss
    cit3 "Да?"
    img 11155
    with fade
    m "Я по поводу покупки платья..."
    music Loved_Up
    img 11156
    with fade
    cit3 "Да, я помню!"
    cit3 "Я нашел несколько деток, но мне надо убедиться, что это платье подойдет им!"
    img 11157
    cit3 "Мне кажется, что чашечки груди здесь имеют жесткую форму и давят на грудь."
    cit3 "Я бы не хотел, чтобы моей детке что-то давило здесь."
    img 11158
    m "Нет, Мистер. Чашечки прилегают очень свободно. Там нет никакого давления..."
    cit3 "Мне надо проверить!"
    # corruption +3 req 100

    menu:
        "Да, Мистер. Посетители могут прикасаться к манекену...":
            pass
        "Нет, Мистер. Это исключено!":
            music Power_Bots_Loop
            img 11159
            with fade
            m "Нет, Мистер. Это исключено!"
            return

    music Groove2_85
    img 11160
    with fade
    m "Да, Мистер. Посетители могут прикасаться к манекену..."
    music Loved_Up
    #Лапает за грудь
    img 11161
    with diss
    w
    img 11162
    with diss
    cit3 "Материал мягкий"
    img 11163
    with diss
    w

    sound Jump1
    img 11164
    with diss
    cit3 "Да, форма вполне упругая..."
    img 11165
    with diss
    w
    img 11166
    with diss
    w
    img 11167
    with diss
    cit3 "Да, вполне подойдет..."

    music Groove2_85
    img 11168
    with fade
    m "Мистер, Я думаю этого достаточно..."

    img 11169
    with fade
    cit3 "Ах да! Меня также смущает форма платья."
    cit3 "Мне нужно убедиться в том, какая форма задницы должна быть у моей цыпочки, чтобы платье подошло."
    img 11170
    with diss
    m "Каким образом Вы хотите убедиться в этом?"
    cit3 "Мне надо пощупать!"
    menu:
        "Да, Мистер. Посетители могут прикасаться к манекену...":
            pass
        "Нет, Мистер. Это исключено!":
            m "Нет, Мистер. Это исключено!"
            return
    # Щупает задницу
    img 11171
    with fade
    w
    img 11172
    with diss
    w
    music Hidden_Agenda
    img 11173
    with fade
    m "Да, Мистер."
    img 11174
    m "Посетители могут прикасаться к манекену..."
    music Loved_Up
    sound snd_fabric1
    img 11175
    with fade
    cit3 "Ммммм... Да."
    img 11176
    with diss
    cit3 "Да, примерно такая задница мне и нужна."
    img 11177
    with diss
    cit3 "А здесь у нее такая упругость..."
    img 11178
    with fade
    w
    img 11179
    w
    img 11180
    w
    img 11181
    with fade
    cit3 "А здесь упругость другая..."
    img 11182
    with diss
    w
    img 11183
    w
    img 11184
    w
    img 11185
    with fade
    w
    img 11186
    with fade
    w
    # звук входа пальца
    music Loved_Up2
    sound hlup19
    img 11187
    with diss
    w
    img 11188
    m "Ахххххх!"
    img 11189
    m "!!!"
    music Power_Bots_Loop
    img 11190
    with fade
    m "Мистер, Я думаю этого достаточно..."
    cit3 "А? Да!"
    img 11191
    with fade
    cit3 "Я скоро навещу Вас снова!"
    #исчезает
    img 11192
    with diss
    mt "Этот придурок собирается покупать платье или нет?!"
    return

label gallery_11229:
    music Hidden_Agenda
    sound highheels_short_walk
    img 11193
    with fadelong
    m "Добрый день, Мистер."
    m "Можно к Вам обратиться?"
    img 11194
    with diss
    cit3 "Да?"
    m "Я по поводу покупки платья..."
    music Loved_Up
    img 11195
    with fade
    cit3 "Да, я помню!"
    cit3 "Я нашел детку, которая подходит под это платье!"
    img 11196
    with diss
    mt "Ну наконец-то!"
    img 11197
    with fade
    cit3 "И у меня свидание с ней через пару часов."
    img 11198
    with fade
    m "Мистер, это прекрасный шанс порадовать ее новым платьем..."
    m "Вы можете доставить это платье ей и она будет на свидании в нем..."
    music Groove2_85
    img 11199
    with diss
    cit3 "Хм... Дело в том, что я собираюсь отменить это свидание..."
    img 11200
    m "Но почему?"
    img 11201
    with fade
    cit3 "На свидание нельзя ходить заряженным, потому что в голове вертится только одно."
    cit3 "Я начинаю говорить глупости и в итоге никакого секса."
    img 11202
    with diss
    cit3 "Предыдущую детку я бросил пару часов назад, потому мне негде разрядиться."
    sound Jump1
    img 11203
    with diss
    w
    img 11204
    with fade
    m "И что, отмена свидания как-то поможет в этом?"
    cit3 "Да, вместо свидания я просто подрочу дома!"
    img 11205
    with diss
    cit3 "Но тогда я не куплю платье!"
    img 11206
    with fade
    m "И что, есть какие-то предложения ко мне?"
    img 11207
    with diss
    cit3 "Да, сделай мне минет в примерочной и я куплю это платье!"
    music Power_Bots_Loop
    img 11208
    with fade
    m "ЧТО??!?!"
    m "Да как Вы смеете!!!"
    music Loved_Up
    img 11209
    with fade
    cit3 "Про это никто не узнает!"
    img 11210
    with diss
    cit3 "Твоя цель - продать платье и Ты сделаешь это!"
    music Groove2_85
    img 11211
    with fade
    m "Может быть Вы просто купите его?"
    cit3 "Исключено! Условие я озвучил!"
    menu:
        "Сделать Покупателю минет за покупку...":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 11214
            with fade
            m "Нет, знаете, я на такое не способна!"
            cit3 "Хорошо, я приду, когда найду другую детку, которая подходит под это платье!"
            return
    img 11212
    with fade
    mt "Черт! Что же мне делать?"
    mt "Я никогда не продам это гребаное платье!"
    mt "Не сменю ту дурацкую одежду и не выберусь из этого кошмара!"
    img 11213
    with diss
    mt "Может стоит сделать то что просит этот негодяй?"
    mt "Тем более этот мерзавец уже побывал у меня в таких местах, что..."
    mt "Это примерочная."
    mt "Для сотрудника магазина естественно находиться в примерочной вместе с клиентом..."
    mt "Никто ничего никогда не узнает..."

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 11215
    with fadelong
    m "Хорошо, я сделаю это."
    m "Мне надо продать это платье!"

    # идут
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11216
    with fadelong
    w
    # примерочная

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Loved_Up
    img 11217
    with fadelong
    cit3 "Заходи, не стесняйся!"
    cit3 "Это ведь твое рабочее место!"
    m "А ты точно купишь платье?"

    img 11218
    with fade
    cit3 "Конечно!"
    cit3 "Я же не оставлю свою детку без подарка!"
    cit3 "Давай! Сделай так, чтобы это свидание состоялось!"

    img 11219
    with fade
    cit3 "Ха-ха!"

    #zip sound
    music stop
    img black_screen
    with diss
    sound snd_zip
    pause 2.0
    music Loved_Up
    img 11220
    with fadelong
    cit3 "Отлично!"
    cit3 "Я важный клиент этого магазина."
    img 11221
    with diss
    cit3 "Я требую особого обслуживания..."
    m "Я... Не очень умею это делать..."

    music Groove2_85
    img 11222
    with diss
    w
    img 11223
    with fade
    menu:
        "Если ты меня обманешь...":
            pass
        "Ты купишь это платье просто так!":
            music Power_Bots_Loop
            img 21229
            with fadelong
            m "Ты купишь это платье просто так."
            m "Иначе я сейчас оторву тебе член..."
            with hpunch
            m "ЯСНО ТЕБЕ!"
            img 21230
            with diss
            cit3 "Ладно, ладно! Я куплю его!"
            cit3 "Пожалуйста, отпусти меня!"
            music Groove2_85
            img 21231
            with fadelong
            m "То-то же..."
            mt "Мне надо было с самого начала так и поступить."
            mt "Ни к чему было терпеть все эти унижения..."
            return
    if monicaBitch == True:
        mt "В моем списке для убийств теперь появится еще один человек..."
    m "Если ты меня обманешь..."
    img 11224
    with fade
    m "То я откушу тебе кое-что..."

    img 11225
    with fadelong
    cit3 "Я не обману тебя и куплю это платье."
    cit3 "Приступай к обслуживанию..."

    # video
    music stop
    img black_screen
    with diss
    pause 2.0
    music2 Loved_Up
    img 11226
    with fadelong
    w
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_1 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_1.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_1
    with fadelong
    wclean

    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_2 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_2.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_2
    with fadelong
    wclean
    stop music

    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    img 11227
    with diss
    cit3 "Это свидание будет волшебным..."
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_3 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_3.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_3
    with fadelong
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    img 11228
    with diss
    cit3 "Я буду смотреть на Саманту в этом платье..."
    cit3 "И представлять как ты сосала мне..."
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_4 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_4.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_4
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_5 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_5.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_5
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_6 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_6.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_6
    with fadelong
    wclean
    stop music

    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    img 11229
    with diss
    cit3 "Да, вот так..."
    cit3 "Соси..."
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_7 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_7.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_8 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_8.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_8
    with fadelong
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    img 11230
    with diss
    cit3 "Соси..."
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_9 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_9.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_9
    with fadelong
    wclean
    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    img 11231
    with diss
    cit3 "Соси..."
    cit3 "Хороший продавец..."
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_10 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_10.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_10
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.5)) + " loop 0.0>Sounds/audio_ShopVisitor2_Monica_Blowjob_1.mp3"
    scene black
    image videov_ShopVisitor2_Monica_Blowjob_1_11 = Movie(play="video/v_ShopVisitor2_Monica_Blowjob_1_11.mkv", fps=30)
    show videov_ShopVisitor2_Monica_Blowjob_1_11
    with fadelong
    wclean


    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.0, 'music2')


    img black_screen
    with Dissolve(1)
    return

label gallery_22268:

    return

label gallery_22251:

    return

############ DickVictoria 1############

label gallery_6215:
    #Моника говорит с Диком в кабинете
    #render
    $ store_music()
    music Hidden_Agenda
    img 6185
    with fade
    m "Дик! Привет!"
    "Я рада что ты обо мне вспомнил!"
    img 6186
    "Ты позвал меня чтобы сказать что передумал?"
    img 6187
    w
    sound highheels_short_walk
    img 6188
    with fade
    "Ты поможешь мне?"
    img 6189
    with Dissolve(0.5)
    "Милый..." #кокетливо смотрит
    img 6190
    w
    img 6191
    w
    img 6192
    music Master_Disorder
    w
    img 6193
#    music Pyro_Flow
    w
    img 6194
    dick "Моника, я позвал тебя чтобы напомнить о себе..."
    img 6195
    w
    music Hidden_Agenda
    img 6196
    with Dissolve(0.5)
    m "Дорогой!"
    sound snd_heavy_papers_drop
    #звук падения бумаги
    img 6197
    with fade
    w
    img 6198
    with Dissolve(0.5)
    w
    img 6199
    with Dissolve(0.5)
    m "Дорогой!"
    img 6200
    with fade
    "Я помню о тебе все время и я..."
    music stop
    sound plastinka2
    pause(0.5)
    music Master_Disorder
    img 6201
    dick "Моника, ты решила разбить его?!"
    "Разбить мое сердце?!"
    img 6200
    m "..."
    img 6201
    dick "???"

    img 6202
    with Dissolve(0.5)
    music Hidden_Agenda
    m "Нет, дорогой! Что ты!!!"
    img 6203
    with Dissolve(0.5)
    w
    img 6204
    with Dissolve(0.5)
    w
    img 6205
    with Dissolve(0.5)
    "Твое сердце - это самое важное что есть для меня..."
    img 6206
    with Dissolve(0.5)
    w
    music stop
    sound plastinka2
    pause(0.5)
    music Master_Disorder
    img 6207
    with fade
    dick "Тогда где та мелочь, о которой я попросил тебя?"
    img 6208
    w
    label gallery_6215_1:
        menu:
            "Приставать к Дику. (low corruption, required [monicaTryToDickBlowjobRequiredCorruption]) (disabled)" if corruption < monicaTryToDickBlowjobRequiredCorruption:
                call low_corruption(monicaTryToDickBlowjobRequiredCorruption) from _rcall_low_corruption
                jump gallery_6215_1
            "Приставать к Дику. (corruption)" if corruption >= monicaTryToDickBlowjobRequiredCorruption:
                #corruption check!!!
                music Loved_up
                img 6213
                with Dissolve(0.5)
                m "Дик..."
                img 6214
                with Dissolve(0.5)
                w
                img 6215
                with Dissolve(0.5)
                w
                img 6216
                with Dissolve(0.5)
                "Дик... Милый..."
                img 6217
                with fade
                w
                img 6218
                with Dissolve(0.5)
                w
                img 6219
                with Dissolve(0.5)
                "Дик..."
                img 6220
                with Dissolve(0.5)
                "Я пока не нашла деньги на..."
                img 6221
                with Dissolve(0.5)
                "Я пока не нашла деньги на твой галстук..."
                img 6222
                with Dissolve(0.5)
                "Но ведь тебе нужен не галстук, милый?"
                img 6223
                with Dissolve(0.5)
                w
                img 6224
                with Dissolve(0.5)
                "Дик! Иди ко мне!"
                img 6225
                with Dissolve(0.5)
                w

                music Power_Bots_Loop
                img 6226
                with fade
                dick "Моника, я знаю что ты лжешь."
                "Для тебя не составит труда найти эти деньги."
                img 6227
                "Ты просто не хочешь уделить мне знак внимания."

                "..."
                img 6228
                "В общем Моника. Я позвал тебя чтобы сообщить..."
                "Я не хочу больше заниматься твоим делом."
                img 6229
                w

            "Я пока не нашла деньги...":
                music Gloove2_85
                img 6209
                with fade
                m "Дик... Я...."
                "Я пока не нашла деньги на..."

                img 6210
                dick "Моника, я знаю что ты лжешь."
                "Для тебя не составит труда найти эти деньги."
                "Ты просто не хочешь уделить мне знак внимания."

                img 6211
                "..."
                music Power_Bots_Loop
                img 6212
                "В общем Моника. Я позвал тебя чтобы сообщить..."
                "Я не хочу больше заниматься твоим делом."

    img 6230
    with fade
    m "КАК?!?!"

    dick "У тебя есть другие друзья. Тот же Маркус."
    "Общайся с ними. А у меня есть свои друзья, которые думают обо мне!"
    img 6231
    "В отличии от тебя, Моника..."

    img 6232
    m "ДИК?!"
    "МАРКУС МНЕ НЕ ДРУГ!!!"
    "ОН..."

    img 6233
    dick "Моника, мне не важно кто он!"
    "Это твои связи и твои проблемы."
    "Причем тут я?!"

    img 6234
    with fade
    mt "О БОЖЕ!!! КАК ЖЕ ТАК!?!?"
    "Я НЕ ОЖИДАЛА ТАКОГО ПОВОРОТА!!!"
    "МНЕ НАДО КАК-ТО ПЕРЕУБЕДИТЬ ЕГО!!!"
    "ИНАЧЕ КОНЕЦ!!!"

    music Hidden_Agenda
    img 6235
    with fade
    m "ДИК! ПОЖАЛУЙСТА!"
    "Я могу тоже быть твоим другом!"
    "ДИК!"
    "МИЛЫЙ!"

    img 6236
    dick "У меня уже есть друг..."

    img 6237
    m "Я... могу дружить и с твоим другом тоже..."
    "Дик!"
    "Я могу быть вместе с Вами!"

    img 6238
    dick "Ты хочешь сказать что можешь поладить с Викторией?"

    img 6239
    m "Я?? С ней??"
    img 6240
    with fade
    "Конечно, Дик!"
    "Конечно! Я с радостью полажу с ней!"

    img 6241
    dick "Хм..."
    "Моника... Я не знаю..."
    "Я сомневаюсь..."

    img 6242
    m "Дорогой! Пожалуйста, не сомневайся во мне!"
    "Пожалуйста, дай мне шанс! Я не разочарую тебя!"

    img 6243
    dick "Твое дело занимает слишком много сил, а ты..."

    img 6244
    m "Цвет?"

    img 6245
    dick "Что, Моника?"

    m "Какой цвет галстука ты хочешь, милый?"

    img 6246
    dick "Хм... Я не думал..."
    "Такой чтобы понравился Виктории..."
    img 6247
    "Моника! А почему бы Вам вместе с ней не купить мне галстук?"
    "Вы хотите подружиться! Это будет прекрасный повод!"

    img 6248
    m "Да, дорогой..."
    "Я буду очень рада..."
    "Только пожалуйста, не бросай мое дело, Дик..."
    dick "Хм... Возможно Виктория еще не успела отослать факс об отмене дела..."

    music Power_Bots_Loop
    img 6249
    dick "В общем Моника, я жду того что Вы {c}подружитесь с Викторией до конца недели{/c}."
    dick "Я даю тебе шанс, Моника."
    if week_day != 5:
        "{c}В пятницу вечером галстук должен быть на мне!{/c}"
    else:
        "{c}В следующую пятницу вечером галстук должен быть на мне!{/c}"
    img 6250
    m "Да, дорогой! Я тебя не подведу!"
    img 6251
    dick "До свидания, Моника!"
    m "До свидания, Дик!"

    $ restore_music()
    return

label gallery_8002:
    #render
    # Разговор Виктории и Моники
    img 7955
    with fade
    m "Я принесла деньги!"
    img 7956
    dick_secretary "Какие деньги? Зачем?"
    img 7957
    m "Для того чтобы купить галстук Мистеру Дику!"
    "Виктория, пойдем скорее покупать его!"
    music Power_Bots_Loop
    img 7958
    with fade
    dick_secretary "Миссис Бакфетт. Вы опоздали."
    "Ваши деньги уже ни к чему."
    img 7959
    m "КАК??!?"
    "Позвоните Мистеру Дику!!!"
    img 7960
    dick_secretary "Мистер Дик просил не беспокоить его."
    m "Но ведь Вы здесь! Значит я не опоздала!"
#    img 7961
#    with fade

    #заносит палец
    img 7962
    with fade
    dick_secretary "Я решила задержаться для того чтобы при Вас нажать на Enter для посылки факса."
    dick_secretary "Замечательно что Вы пришли, я отправляю его..."
    m "НЕТ!!!"
    m "Мисс Виктория! Пожалуйста!"
    "Я прошу Вас! Не посылайте этот факс!"
    img 7963
    with fade
    dick_secretary "С какой стати я должна не выполнять приказ своего Босса?"

    img 7964
    m "У меня есть деньги! Пожалуйста!"
    "Мне необходим Ваш изысканный вкус для того чтобы угодить Мистеру Дику!"
    music Groove2_85
    img 7965
    dick_secretary "Изысканный вкус?"
    img 7966
    dick_secretary "Хорошо, я могу взять эти деньги и купить галстук сама."
    "Вас все-равно не никогда не дождешься!"
    img 7967
    m "Да, пожалуйста! Возьмите деньги!"
    img 7968
    "Купите галстук Мистеру Дику!"
    img 7969
    with fade
    mt "Мне надо чтобы этот гребаный галстук был куплен!"
    "Тогда этот кошмар закончится для меня!"

    # Если Моника опоздала
    if monicaLateToDick == True:
        img 7970
        with fade
        dick_secretary "Только Вы слишком сильно опоздали, Миссис Бакфетт!"
        img 7971
        "У меня уже нет времени идти покупать его."
        img 7972
        m "Я прошу Вас, найдите пару минут купить его, пожалуйста!"
        img 7973
        mt "Сучка!!!"
        "Она издевается надо мной!"
        img 7974
        with fade
        dick_secretary "Хм... Как бы Вас наказать за опоздание..."
        #щелчок клавиши
        sound keyboard_click
        img 7975
        w
        img 7976
        dick_secretary "Мне надо как-то дискредитировать Вас, Миссис Бакфетт!"
        "Что Вы можете подсказать мне?"
        "Как лучше это сделать?"
        img 7977
        m "Что Вы имеете ввиду?"
        "Зачем меня дискредитировать?"
        sound keyboard_click
        #целчок клавиши
        img 7978
        w
        img 7979
        w
        img 7980
        w
        img 7981
        with fade
        dick_secretary "Покажите грудь, я хочу сфотографировать ее, на свой телефон..."
        music Power_Bots_Loop
        img 7982
        m "ЧТО?!?!"
        m "ЗАЧЕМ?!?!"
        img 7983
        dick_secretary "Это может принести мне пользу, Миссис Бакфетт."
        img 7984
        m "!!!"
        # Виктория подносит телефон к груди Моники
        img 7986
        with fade
        dick_secretary "Я говорю покажите свою грудь."
        img 7985
        "Иначе можете быть свободны. Факс отправится немедленно!"
        img 6285
        mt "О БОЖЕ!!!"
        "ЭТО БУДЕТ КОНЕЦ!!"
        img 7991
        w
        menu:
            "У меня нет выбора... (low corruption, required [monicaVictoriaShowBoobsToCameraCorruptionRequired]) (disabled)" if corruption < monicaVictoriaShowBoobsToCameraCorruptionRequired:
                pass
            "У меня нет выбора... (corruption)" if corruption >= monicaVictoriaShowBoobsToCameraCorruptionRequired:
                # Моника показывает грудь, сгорая от стыда
                img 7992
                dick_secretary "Ну?"
                music Hidden_Agenda
                img 7993
                with fade
                w
                sound snd_fabric1
                img 7994
                with fade
                w
                img 7995
                with fade
                w
                img 7996
                with fade
                w
                img 7997
                dick_secretary "Миссис Бакфетт, наклонитесь поближе."
                "Мне неудобно вставать, чтобы сфотографировать Вашу грудь..."
                img 7998
                with fade
                dick_secretary "Посмотрите в камеру и улыбнитесь."
                img 7999
                w
                img 8000
                dick_secretary "Ну же! Смелее!"
                dick_secretary "Вы просите меня о помощи и даже не хотите улыбнуться мне?"
                img 8001
                w
                img 8002
                w
                dick_secretary "Улыбку! Улыбку, Миссис Бакфетт!"
                music Power_Bots_Loop
                img 8003
                "Если Вы не улыбнетесь искренней улыбкой, Мистеру Дику не понравится купленный галстук!"
                menu:
                    "Улыбнуться искренней улыбкой...":
                        pass
                music Hidden_Agenda
                img 8004
                with fade
                w
                img 8005
                w
                img 8006
                w

                img 8007
                with fade
                dick_secretary "Миссис Бакфетт, как Вы считаете, чья грудь лучше?"
                "Моя или Ваша?"
                img 8008
                "Отвечайте в телефон..."
                menu:
                    "Это провокация. Лучше ответить что ее грудь лучше.":
                        pass
                img 8009
                with fade
                m "Конечно Ваша, Мисс Виктория..."
                img 8010
                dick_secretary "Правильный ответ..."
                # Щелчок фотоаппарата
                img 8011
                call photoshop_flash() from _rcall_photoshop_flash_164
                w
                sound snd_woman_laugh
                img 8012
                dick_secretary "Хи-хи-хи"
                sound snd_woman_laugh2
                img 8013
                with fade
                dick_secretary "Хи-хи-хи"
                img 8014
                w
                sound snd_fabric1
                img 8015
                with fade
                w

            "Мисс Виктория, Вы такая изящная леди... (попытаться не показывать грудь).":
                music Hidden_Agenda
                img 7987
                with fade
                m "Мисс Виктория, Вы такая изящная леди..."
                "Ваша грудь намного лучше чем моя..."
                "Зачем Вам смотреть на мою грудь, когда Вы обладаете гораздо лучшими формами..."
                # sound Смеется
                sound snd_woman_laugh
                img 7988
                with Dissolve(0.5)
#                pause 1.0
#                sound snd_woman_laugh2
                dick_secretary "Хи-хи-хи"
                img 7989
                dick_secretary "Хорошо, я разрешаю Вам этого не делать."
                img 7990
                w

    music Groove2_85
    img 8016
    with fade
    dick_secretary "Вы очень хорошо учитесь целовать мою попу, Миссис Бакфетт."
    img 8017
    "Мне нравится это..."
    music Power_Bots_Loop
    img 8018
    with fade
    mt "Я НЕНАВИЖУ ЭТУ ТВАРЬ!!!"
    "Я УНИЧТОЖУ ЕЕ!!!"
    music Groove2_85
    img 8019
    with fade
    m "Когда Вы купите галстук для Мистер Дика?"
    img 8017
    dick_secretary "Сегодня..." #хитро улыбается
    img 8019
    m "Когда будет Мистер Дик?"
    img 8017
    dick_secretary "Завтра..." #хитро улыбается
    img 8020
    with fade
    m "Я зайду завтра, Мисс Виктория..."
    img 8021
    dick_secretary "Конечно, Миссис Бакфетт! Заходите!"
    return

label gallery_8067:
    # Моника заходит к Дику и нажимает на него
    music Hidden_Agenda
    img 8022
    with fade
    m "Ну что, милый?"
    "Тебе понравился галстук?"
    "А почему ты не в нем?"
    img 8023
    dick2 "О! Моника!"
    "Странно видеть тебя здесь."
    "Я думал что ты уже со своими новыми друзьями..."
    img 8024
    with fade
    m "Что ты имеешь ввиду, Дик?!"
    img 8025
    dick2 "Галстука так и нет, я отменил твое дело, Моника..."
    music Pyro_Flow
    img 8026
    with hpunch
    m "ЧТО?!?!?!"
    "ЭТА ТВАРЬ!!!!!!!"

    #Моника бежит к Виктории убивать ее
    sound highheels_short_walk
    img 8027
    with fadelong
    m "АХ ТЫ СУЧКА!!!"
    "ТЫ ВЗЯЛА ДЕНЬГИ И НЕ КУПИЛА ГАЛСТУК!!!"
    img 8028
    "Я УБЬЮ ТЕБЯ!!!"

    sound highheels_short_walk
    img 8029
    with Dissolve(0.5)
    "КУДА?!?!"
    img 8030
    w

    #Секретарша убегает к Дику, Моника бежит за ней
    sound highheels_short_walk
    img 8031
    with fadelong
    m "Я УБЬЮ ТЕБЯ!!!"
    m "ТВАРЬ!!!"

    #Секретарша стоит у Дика в хитрой позе нагнувшись
    music Groove2_85
    img 8032
    with fade
    dick_secretary "Мистер Дик! Помогите мне!"
    img 8033
    dick2 "Что такое, Моника?!"
    "Почему ты позволяешь себе кричать в моем кабинете!!!"
    music Pyro_Flow
    img 8034
    with fade
    m "ЭТА ТВАРЬ УКРАЛА МОИ ДЕНЬГИ!!!"
    "ДЕНЬГИ НА ТВОЙ ГАЛСТУК!!!"
    img 8035
    "ТЫ ХОТЬ ЗНАЕШЬ ЧЕРЕЗ ЧТО Я ПРОШЛА ЧТОБЫ ДОСТАТЬ ИХ?!?!?!"
    #Моника в шоке
    music Groove2_85
    img 8036
    with fade
    dick_secretary "Мистер Дик!"
    "Вы сказали дружить с Миссис Бакфетт!"
    img 8037
    "Я стараюсь изо всех сил!"
    "Но она не хочет дружить со мной!"
    img 8038
    "Мы договорились в пятницу сходить Вам за галстуком, но она даже не пришла!"
    img 8039
    "А сегодня она ругается на меня, как-будто это я опоздала, а не она!"
    img 8040
    "Мистер Дик!"
    "Миссис Бакфетт почему-то не любит меня!"
    img 8041
    "Я с самого начала, почему-то, не понравилась ей."
    img 8045
    with fade
    "Она предвзято относится ко мне и обижает меня!"
    img 8047
    with fade
    w
    img 8046
    w

    #Моника вообще в шоке
    img 8042
    w
    img 8043
    w
    music Pyro_Flow
    img 8044
    with fade
    m "ДИК, ПОСЛУШАЙ...!!!"

    music Groove2_85
    img 8048
    dick2 "ХВАТИТ!!!"
    "МОНИКА!!!"
    "Мне надоела твоя постоянная ложь!"
    "Я прекрасно знаю что ты не пришла вовремя в пятницу!"
    "Я был здесь и мы ушли с Викторией вместе!"
    "Мне надоело что ты все время пытаешься обвинить Викторию!"
    "Это непорочное создание!"
    "Она не заслуживает такого отношения со стороны тебя!"
    img 8049
    with fade
    w
    img 8050
    with fade
    w
    img 8051
    # Моника в шоке смотрит на Викторию
    # Виктория ехидно улыбается
    "И я не позволю тебе делать это!"
    "Тем более в моем кабинете!"
    music Power_Bots_Loop
    img 8052
    with fade
    "ВЫЙДИ ВОН!!!"
    img 8053
    menu:
        "Послать Дика к черту.":
            #bitch increase
            pass
        "Попробовать соблазнить Дика как это делает Виктория (low corruption, required [monicaDickSeduceAsVictoriaByAssCorruptionRequired]) (disabled)" if corruption < monicaDickSeduceAsVictoriaByAssCorruptionRequired:
            pass
        "Попробовать соблазнить Дика как это делает Виктория (corruption)" if corruption >= monicaDickSeduceAsVictoriaByAssCorruptionRequired:
            music Pyro_Flow
            img 8054
            with fade
            m "Дик! Я не понимаю!"
            "Что ты нашел такого в этой маленькой соске?!"
            "Тебе нравится то что она все время сверкает перед тобой своей задницей?!"
            img 8055
            with fade
            #Моника чуть не плачет
            "Я тоже могу так делать, Дик!"
            "ХОЧЕШЬ???"
            img 8056
            "ТЫ ЭТОГО ХОЧЕШЬ ОТ МЕНЯ?!"
            "ДА???"
            img 8057
            with fade
            "На! Пожалуйста!"
            img 8058
            "Ты уже довел меня до этого!"
            #Моника начинает снимать шорты. Голый зад почти полностью
            sound snd_fabric1
            img 8059
            with fade
            "На! Получай!"
            img 8060
            m "Ты с самого начала хотел увидеть это!"
            img 8061
            "Смотри!"
            img 8062
            w
            img 8063
            w
            img 8064
            w
            m "Смотри!"
            img 8065
            m "Ты добился чего хотел!"
            img 8066
            m "Я ничем не хуже ее, Дик!"
            img 8067
            m "Ну посмотри! Посмотри внимательно!"
            music Power_Bots_Loop
            img 8068
            with fade
            dick2 "МОНИКА! ПРЕКРАТИ СЕЙЧАС ЖЕ!!!"
            #Моника смотрит в оборот на Дика с обидой
            img 8069
            w

            if monicaShowedBoobsToVictoriaCamera == True:
                #Если показывала грудь Виктории
                img 8070
                with fade
                dick2 "Как-будто мало того что ты ходишь и показываешь свою грудь налево и направо!"
                img 8069
                w
                img 8071
                w
                img 8072
                mt "СУЧКА!!!"
                #Моника смотрит злобно на Викторию, та показала фото Дику
                #Виктория ехидно ухмыляется
                img 8073
                with fade
                w
                #

            img 8074
            with fade
            dick2 "Твой моральный облик очень разочаровывает меня, Моника!"
            img 8075
            "Я не могу поверить как мог быть влюблен в такую развратную и лживую женщину, как Ты!"
            #fade
            music Hidden_Agenda
            img 8076
            with fade
            m "Дик..."
            img 8077
            m "Дик, ну пожалуйста!"
            music Power_Bots_Loop
            img 8078
            with fade
            dick2 "Я сказал быстро оденься и не смущай Викторию своим видом!!!"
            #Моника смотрит почти плача
            img 8079
            dick_secretary "..."
            img 8080
            with fade
            w
            sound snd_fabric1


    music Pyro_Flow
    img 8081
    with fadelong
    m "ЗНАЕШЬ ЧТО, ДИК?!"
    "ПОШЕЛ ТЫ К ЧЕРТУ!!!"
    "МНЕ ПЛЕВАТЬ НА ТО ЧТО ТЫ ВЕЛ МОЕ ДЕЛО!!!"
    "МНЕ ПЛЕВАТЬ НА ТЕБЯ!!!"
    img 8082
    "МНЕ ПЛЕВАТЬ НА ТВОЮ НОВУЮ СОСКУ!!!"
    img 8083
    "Ты выдумал все это чтобы издеваться надо мной!"
    "Разозлился на меня за то что я не дала тебе как эта твоя соска!"
    #Виктория зло смотрит на Монику
    img 8084
    w
    img 8085
    with fade
    "Я ухожу! И надеюсь тебя больше никогда не увижу!!!"

    img 8086
    dick2 "До свидания, Моника..."

    #Телепорт к секретарше, но ее там нет, она в кабинете Дика
    return

label gallery_8137:
    #render
    #Кабинет Дика
    music Power_Bots_Loop
    img 8090
    with fade
    m "ДИК!!!"
    "ПОМОГИ МНЕ!!!"
    img 8091
    "ОНИ ВНИЗУ!!!"
    "ОНИ ИДУТ СЮДА, ЗА МНОЙ!!!"
    img 8092
    dick2 "Моника, ты шутишь?"
    "Ты только что наговорила мне такого, что..."

    music Hidden_Agenda
    img 8093
    with fade
    m "ДИК! ПРОСТИ МЕНЯ!!!"
    "Я ГЛУПАЯ НИКЧЕМНАЯ ЖЕНЩИНА!"
    img 8094
    "У МЕНЯ КУРИНЫЕ МОЗГИ!"
    "Я ЗРЯ НАГОВОРИЛА ТЕБЕ ВСЕГО!"
    img 8095
    "ПОЖАЛУЙСТА, СПАСИ МЕНЯ!!!"
    img 8096
    dick2 "Моника, ты мне уже надоела, честно!"
    img 8097
    m "ДИК!!!"
    music Groove2_85
    img 8098
    with fade
    dick2 "Если Виктория простит тебя, то я сделаю звонок, но ничего не обещаю..."
    img 8099
    m "Я ПОНЯЛА, ДИК! Я СЕЙЧАС ВЕРНУСЬ!!!"

    #Сцена меняется на секретаршу
    music Hidden_Agenda
    sound highheels_short_walk
    img 8100
    with fadelong
    m "Мисс Виктория!"
    "Пожалуйста! Простите меня!"
    "Я наговорила глупостей, но я прошу прощения у Вас!"
    img 8101
    dick_secretary "Что Вы от меня хотите, Миссис Бакфетт?"
    img 8102
    m "Я хочу чтобы Вы меня простили и хочу с Вами дружить!"
    img 8103
    w
    img 8102
    w
    music Groove2_85
    img 8104
    with fade
    dick_secretary "Вы знаете, мне понравилось то, как я сходила вчера за покупками."
    img 8105
    "Я готова Вас простить, если Вы будете {c}приносить мне $ 5000 каждую пятницу{/c}."
    "Я люблю шоппинг, наверное Вы, как женщина, меня понимаете..."
    music Power_Bots_Loop
    img 8106
    w
    img 8105
    w
    img 8107
    w
    img 8108
    with fade
    w
    img 8107
    with fade
    #Моника в шоке. несколько кадров
    menu:
        "Я согласна... (у меня нет другого выбора, иначе меня сейчас схватят!)":
            pass
    music Groove2_85
    img 8109
    with fade
    m "Я... Я согласна..."
    img 8110
    "Только пожалуйста! Идите скорее скажите Мистеру Дику что простили меня!!!"
    img 8111
    with fade
    dick_secretary "И еще у меня условие, чтобы Вы не приближались к Мистеру Дику..."
    img 8112
    m "Я согласна! Я не буду приближаться к нему!"
    "Пожалуйста, скорее!"
    img 8113
    with fade
    dick_secretary "Чем Вы докажете серьезность своих обещаний?"
    img 8114
    m "Ч.. Что...?"
    "Обещаний?"
    img 8115
    with fade
    dick_secretary "Да! Миссис Бакфетт!"
    "Я не верю просто словам! Мне надо что-то повесомее!"
    "Чем Вы можете подтвердить то что Вы очень хотите чтобы Я простила Вас?"
    img 8116
    m "Я не знаю! Что угодно!!!"
    "Только скажите Мистеру Дику что простили меня, скорее!!!"
    dick_secretary "Хорошо, Миссис Бакфетт..."
    #звук каблука
    music stop
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    sound heel1
    img 8117 #?
    with fadelong
    music Power_Bots_Loop
    "Вот..." #Ставит каблук на стол
    img 8118
    m "Что это???"
    img 8119
    dick_secretary "Это мой каблук, Миссис Бакфетт..."
    "Вы должны поцеловать его..."
    img 8120
    with fade
    m "ЧТОООООО???" # Моника в шоке
    #Виктория ехидно улыбается
    img 8121
    dick_secretary "Помимо Ваших обещаний..."
    img 8122
    "Поцелуйте также мой каблук, тогда я прощу Вас..."
    img 8123
    with fade
    mt "О БОЖЕ!!!"
    "ЧТО МНЕ ДЕЛАТЬ?!?! МЕНЯ СЕЙЧАС СХВАТЯТ И ОТВЕЗУТ К МАРКУСУ!!!"
    "И ОТТУДА Я ОТПРАВЛЮСЬ НА РАНЧО 218!!!"
    "О БОЖЕ!!!"
    img 8122
    menu:
        "Поцеловать каблук Виктории (у меня нет выбора...)":
            mt "У меня нет выбора и нет времени искать другие варианты..."
            "Похоже единственный путь к спасению - поцеловать каблук этой сучки Виктории..."
            #Моника целует каблук
            #Виктория довольно улыбается
            music Loved_Up
            img 8127
            with fade
            w
            img 8128
            with fade
            w
            img 8129
            with fade
            mt "Я постараюсь не думать об этом и быстро забыть..."
            img 8130
            w
            img 8131
            w
            img 8132
            w
            img 8133
            w
            img 8134
            sound kiss1
            w
            img 8135
            w
            img 8136
            w
            img 8137
            sound kiss1
            w
            img 8138
            with fade
            w
            img 8139
            w
            img 8140
            w
            img 8141
            w
            #смотрит на попу
            img 8142
            with fade
            w
            img 8143
            w
            img 8144
            m "Меня сейчас стошнит!..."
            img 8145
            with fade
            dick_secretary "Вы можете лизнуть мой зад, Миссис Бакфетт..."
            "Я разрешаю Вам..."
            music Power_Bots_Loop
            img 8146
            m "ЧТО?!?!"
            img 8147
            dick_secretary "Миссис Бакфетт, я сказала что Вы можете лизнуть мой зад..."
            img 8148
            with fade
            dick_secretary "Вы можете лизнуть его, я разрешаю Вам..."
            img 8149
            dick_secretary "Вам необязательно делать это..."
            dick_secretary "Я приму Ваше прощение и так..."
            dick_secretary "Но это было бы хорошим шагом в начале нашей дружбы..."
            menu:
                "Я считаю что то что я поцеловала Ваш каблук - достаточно для начала нашей дружбы, Мисс Виктория...":
                    music Hidden_Agenda
                    m "Я считаю что то что я поцеловала Ваш каблук - достаточно для начала нашей дружбы, Мисс Виктория..."
                    sound snd_woman_laugh
                    dick_secretary "Хи-хи-хи..."
                "Лизнуть зад Виктории... (corruption)" if corruption >= monicaVictoriaLickAssBeginCorruptionRequired:
                    label gallery_8157:
                    mt "От этой сучки сейчас зависит то попаду-ли я к Маркусу или нет..."
                    "Как бы это ни было противно, но, похоже, лучше сделать то что она говорит..."
                    img 8150
                    mt "В ином случае, меня могут ждать вещи в сотни раз похуже этого..."
                    music stop
                    img 8151
                    with fade
                    w
                    music Music_Licking1
                    img 8152
                    with fade
                    w
                    img 8153
                    w
                    img 8154
                    with fade
                    w
                    img 8155
                    dick_secretary "Миссис Бакфетт, Вам запрещено прикасаться к моей киске."
                    "Вы имеете допуск только к моей попе."
                    img 8156
                    "Вы можете лизать мое анальное отверстие."
                    img 8157
                    with fade
                    m "Мммммпххфф!!!"
                    img 8158
                    dick_secretary "Вот так, Миссис Бакфетт..."
                    img 8159
                    m "Мммммм!!"
                    img 8160
                    with fade
                    dick_secretary "Учитесь хорошенько лизать мой зад, Миссис Бакфетт..."
                    img 8163
                    "Это полезный навык для Вас..."
                    img 8161
                    with fade
                    m "Мммммпххфф!!!"
                    img 8162
                    w
                    img 8165
                    with fade
                    w
                    img 8164
                    w
                    music Groove2_85
                    img 8166
                    dick_secretary "Достаточно, Миссис Бакфетт!"
                    "Не увлекайтесь..."
                    "Вы вылизали свое прощение..."
                    sound snd_woman_laugh2
                    "Хи-хи-хи"
                "Лизнуть зад Виктории... (low corruption, required [monicaVictoriaLickAssBeginCorruptionRequired]) (disabled)" if corruption < monicaVictoriaLickAssBeginCorruptionRequired:
                    pass

        "Это уже слишком!":
            music Pyro_Flow
            img 8124
            with fade
            m "Мисс Виктория!"
            "Я пообещала Вам $ 5000 каждую пятницу!"
            "А также не приближаться к Мистеру Дику!"
            "Этого достаточно чтобы простить меня!"
            img 8125
            "Но целовать каблук - это уже слишком!!!"
            music Groove2_85
            sound snd_woman_laugh
            img 8126
            with fade
            dick_secretary "Хи-хи-хи"
            "Ладно, Миссис Бакфетт..."
            "Я пошутила..."
            "Или нет..."

#        monicaVictoriaLickAssAtBegin
    if monicaVictoriaLickAssAtBegin == False:
        music Groove2_85
        img 8174
        with fade
        dick_secretary "Хорошо, Миссис Бакфетт..."
        "В следующий раз Вы поцелуете мой зад..."
        "И сделаете это очень страстно!"
    else:
        music Groove2_85
        img 8167
        with fade
        mt "БОЖЕ!!! КАКАЯ МЕРЗОСТЬ!!!"
        "Я никогда этого больше не сделаю!!!"
        img 8168
        dick_secretary "Хорошо, Миссис Бакфетт..."
        "Для начала неплохо..."
        img 8169
        with fade
        "В следующий раз Вы снова поцелуете мой зад..."
        img 8170
        "Вот сюда!"
        img 8171
        "И сделаете это очень страстно!"
        "Не так скучно как сделали это сейчас!"
        img 8172
        with fade
        w

    #Моника в шоке
    img 8173
    m "?!?!?!?!?"

    img 8175
    with fade
    dick_secretary "А что такого?"
    "Все этого хотят."
    img 8176
    "Мистер Дик очень этого хочет."
    "Но немногим это позволено."
    img 8177
    with fade
    "Вы мне понравились, Миссис Бакфетт."
    "Если Вы будете хорошей подругой, то я разрешу Вам делать это..."

    music Power_Bots_Loop
    img 8178
    mt "Я УЖЕ СЛЫШУ ШАГИ!!!"
    m "Мисс Виктория! Пожалуйста! Скорее скажите Мистеру Дику!!!"

    #Виктория и Моника заходят к Дику
    music Groove2_85
    sound highheels_short_walk
    img 8179
    with fadelong
    dick_secretary "Мистер Дик..."
    "Я прощаю Миссис Бакфетт и готова дать ей еще один шанс..."
    img 8180
    w
    img 8181
    w
    img 8182
    with fade
    dick "Виктория, милая..."
    "Ты точно в этом уверена?"
    "Для меня довольно сложно снова возобновить это дело..."
    img 8183
    dick_secretary "Мистер Дик..."
    "Вы же знаете, что мое сердечко маленькое, но очень доброе..."
    "Я не могу позволить Миссис Бакфетт страдать..."
    img 8184
    dick "Ох, Виктория!"
    "Моя девочка!"
    "Ты такая прелесть!"
    img 8185
    "В этом мире меня окружают только черствые злые люди..."
    "Такие как Я..."
    "И мне так нравится в тебе твоя доброта!!!"
    img 8186
    with fade
    dick "Моника, подожди за дверью!"
    "Я сделаю звонок!"

    #Моника выходит
    #fade
    sound highheels_short_walk
    img 8187
    with fadelong
    mt "Быстрее бы Дик позвонил!"
    "Что он там копается?!?!"
    "Но..."
    "Может они не смогут найти это место?"
    "Может быть их не пропустят сюда?"
    #5 минут спустя
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("5 минут спустя...")) from _rcall_textonblack_27
    img black_screen
    with Dissolve(2.0)
    music Gearhead
    img 8188
    with fadelong
    w
    img 8189
    mt "О НЕТ!!!"
    img 8190
    mt "ЭТО ОНИ!!!!"
    #На нее идут полицейские и ухмыляются
    #Моника в ужасе

    #Моника забегает в кабинет

    sound highheels_short_walk
    img 8191
    with fadelong
    m "ДИК!!!"
    "ОНИ УЖЕ ЗДЕСЬ!!!"
    "ЭТО КОНЕЦ!!!"
    img 8192
    dick "Не волнуйся, Моника!"
    "Им сейчас сделают звонок!"
    #fade
    #звук двери
    #Полицейские в кабинете Дика, Моника в ужасе, они стоят по бокам от нее
    #Также на сцене Дик, Виктория
    sound snd_door_open1
    img 8193
    with fadelong
    policeman1 "Доброго времени дня, Мистер Дик!"
    img 8194
    dick "Да, господа? Что Вы хотели?"
    img 8195
    policeman2 "Мистер Дик, мы здесь с целью задержать эту преступницу..."
    policeman1 "Но нам только что сделали звонок и отменили задержание..."
    img 8196
    with fade
    dick "Я в курсе, мальчики!"
    "У Вас есть еще вопросы?"
    img 8197
    policeman1 "Кхм... Да..."
    "Мистер Дик, нас попросили передать Вам, что в следующий раз отмены задержания не будет..."
    img 8198
    with fade
    dick "Нет проблем, мальчики, хорошего Вам дня!"
    img 8199
    policeman1 "До свидания, Мистер Дик!"

    img 8200
    with fade
    policeman2 "Привет, сучка!"
    #Моника в ужасе
    policeman1 "Почему мы должны тебя ловить?"
    "Где ты вообще живешь?"
    policeman2 "Отвечай, быстро..."
    #Моника в шоке, не знает что сказать
    m "Я... Я живу..."
    #Их прерывает Дик
    img 8201
    with fade
    dick "Мальчики, хорошего дня Вам!"
    img 8202
    policeman1 "Да, Мистер Дик! До свидания!"
    #Уходят
    #звук двери
    #fade
    sound snd_door_open1
    music stop
    img black_screen
    with Dissolve(0.5)
    pause 3.0
    music Groove2_85
    img 8203
    with fade
    m "М... Ммммм.."
    "Мистер Дик..."
    "Спасибо Вам..."
    "Я... Я пошла..."

    img 8204
    dick_secretary "Миссис Бакфетт!"
    "Подружка!"
    "Подожди, пожалуйста, меня!"

    #телепорт на секретаршу

#        policeman1
#        policeman2
    return

label gallery_8225:
    #render
    #Моника пришла к Виктории и есть просрочка
    music Power_Bots_Loop
    img 8213
    with fade
    dick_secretary "Миссис Бакфетт!"
    "Вы просрочили деньги!"
    m "Мисс Виктория... Я... Честно..."

    img 8214
    with fade
    dick_secretary "Вы поставили меня в неудобное положение!"
    dick_secretary "Теперь Вам надо лизать прощение!"
    m "Я прошу прощения, Миссис Виктория..."
    #Виктория задирает платье и встает задом, наклонившись на стул
    music Groove2_85
    img 8215
    with fade
    dick_secretary "Лижите прощение, Миссис Бакфетт!"
    img 8216
    m "ЧТО????"
    img 8217
    dick_secretary "Давайте скорее!"
    "А то Вам придется лизать это прощение на глазах Мистера Дика!"
    img 8218
    with fade
    mt "О БОЖЕ!!!"
    img 8219
    "МНЕ?!?! ЦЕЛОВАТЬ У НЕЕ?!?!"
    "ЭТО МЕСТО?!?!"
    img 8220
    with fade
    if monicaVictoriaLickAssAtBegin == True:
        mt "СНОВА?!?!?"
    else:
        w
    img 8221
    mt "Меня сейчас стошнит!!!"
    img 8222
    dick_secretary "Давайте скорее!"
    "И не забудьте!"
    "Вы не имеете доступа к моей киске!"
    "Лизать прощение надо там куда я показываю пальцем!"
    "Это мой зад!"
    "Учитесь хорошенько лизать его!"
    menu:
        "Поцеловать зад Виктории (у меня нет выбора...)":
            pass
        "Убежать!":
            #Телепорт на hall
            return


    #Моника целует зад Виктории
    music Power_Bots_Loop
    img 8223
    with fade
    mt "У меня нет выбора!"
    "Это лучше чем оказаться в руках у Маркуса!"
    "Страшная цена свободы, Моника!"
    img 8224
    "Мне придется ее заплатить..."
    "(хмык)"
    music Loved_Up
    img 8225
    with fade
    w
    img 8226
    with Dissolve(0.5)
    w
    music Music_Licking1
    img 8227
    with Dissolve(0.5)
    w
    img 8228
    w
    dick_secretary "Миссис Бакфетт!!!"
    img 8229
    m "Мммммпххфф!!!"
    img 8230
    with fade
    dick_secretary "Вы так не добудете прощения!"
    img 8231
    dick_secretary "Вы уже вылизали мне весь зад до блеска!"
    img 8232
    dick_secretary "Но Ваше прощение находится не вокруг моей попки, а внутри нее!"
    img 8233
    dick_secretary "Напрягите язычок, Миссис Бакфетт!"
    "Ваш острый язычок!"
    "Который слишком много болтает!"
    "И засуньте его туда где ему полагается быть с самого начала!"
    music stop
    img 8234
    with fade
    w
    menu:
        "Засунуть язык глубоко в анальное отверстие Виктории...":
            pass
    img 8235
    with fade
    w
    sound hlup21
    img 8236
    with Dissolve(0.5)
    w
    music Music_Licking1
    img 8238
    dick_secretary "Да, вот так!"
    "А теперь поелозьте им в разные стороны, Да!"
    img 8237
    with fade
    dick_secretary "Вот так, Да!"
    img 8239
    dick_secretary "Прощение где-то рядом, Вы почти нащупали его!"
    img 8240
    with fade
    dick_secretary "Еще чуть-чуть! Почти!"
    img 8241
    dick_secretary "Да, все! Достаточно!"
    img 8242
    with fade

    dick_secretary "Миссис Бакфетт! Вы можете вынуть свой язык из моего зада."
    "Достаточно..."

    music Groove2_85
    img 8243
    with fadelong
    dick_secretary "Хорошая подружка!"
    "Я прощаю тебя!"
    "Но это не отменяет нашей договоренности!"
    "Я все еще собираюсь на шоппинг!"
    img 8244
    "У меня уже составлен длинный список на несколько месяцев вперед!"
    "Наша дружба будет долгой, Миссис Бакфетт!"
    img 8245
    with fade
    mt "!!!"

    return

label gallery_8249:
    #render
    #Сцена Дика и Виктории (вечер после диалога с полицейскими)
    #Виктория лежит на столе задом к окну (где свет)
    #Дик положил руку на ножку
    #Дик гладит ее по ногам и попе
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_28
    scene black_screen
    with Dissolve(1)
    music Loved_Up
    img 8246
    with fadelong
    dick "Виктория, детка моя!"
    "Можно я потрогаю твою попу?"

    img 8247
    dick_secretary "Нет, Мистер Дик!"
    "Еще пока не время..."
    img 8248
    with fade
    dick "Ну пожалуйста, Виктория!"
    "Ну детка моя!"
    dick_secretary "Нет!"
    img 8249
    dick "Ну почему же, крошка?"
    img 8250
    dick_secretary "У меня не очень хорошее настроение сегодня..."
    dick "Кто посмел испортить тебе настроение, детка?"
    dick_secretary "Миссис Бакфетт!"
    music Power_Bots_Loop
    img 8251
    with hpunch
    dick2 "ЧТО?!?!"
    "ОПЯТЬ ОНА ЗА СВОЕ?!?!"
    music Loved_Up
    dick_secretary "Нет, Мистер Дик..."
    "Она все поняла и теперь ведет себя как подруга."
    "Но она по дружески обратилась ко мне с просьбой помочь ей деньгами."
    img 8252
    "У нее сложная ситуация сейчас..."
    "Я пообещала давать ей деньги каждую неделю."
    "Я не могла отказать из-за своей доброты..."
    img 8253
    "Но теперь у меня остается совсем мало денег на уход за собой..."
    "А я привыкла хорошо выглядеть для Мистера Дика!"
    img 8254
    with fade
    "И я боюсь что Мистер Дик разлюбит Меня..."
    dick "Моя милая Виктория!"
    "Я никогда не разлюблю тебя!"
    "Не переживай, детка!"
    img 8255
    "Я буду давать тебе больше денег чем сейчас!"
    "Тебе хватит и на себя и на свою доброту, которая так нравится мне в тебе!"
    img 8256
    with fade
    #Виктория улыбается
    dick_secretary "Хорошо, Мистер Дик..."
    "Вы можете потрогать мою попу..."
    #Дик задирает платье и начинает мять попу Виктории
    img 8257
    w
    img 8258
    w
    img 8259
    with fade
    w
    img 8260
    dick "Крошка! Можно я поцелую ее?"
    img 8261
    with fade
    dick_secretary "Ой! Мистер Дик!"
    "Мою попу все хотят поцеловать!"
    img 8262
    with hpunch
    dick "А кто еще кроме меня хочет это сделать???"
    dick_secretary "Миссис Бакфетт..."
    dick "Ты что, серьезно?"

    if monicaShowedBoobsToVictoriaCamera == True or monicaShowedAssToDickAndVictoria == True:
        #Если Моника показывала грудь и раздевалась
        img 8263
        with fade
        dick_secretary "Да, Мистер Дик!"
        "Миссис Бакфетт сразу захотела меня как только мы познакомились в первый раз!"
        if monicaShowedBoobsToVictoriaCamera == True and monicaShowedAssToDickAndVictoria == True:
            "Сначала показывала мне свою грудь..."
            "Затем пыталась подражать мне перед Вами..."
    else:
        #иначе
        img 8263
        with fade
        dick_secretary "Да, Мистер Дик..."
        #

    img 8264
    dick "Малышка, можно я первый это сделаю?" #Дик улыбается
    menu:
        "Можно, Мистер Дик...":
            dick_secretary "Можно, Мистер Дик..."
            pass
        "Вы уже опоздали, Мистер Дик..." if monicaVictoriaLickAssAtBegin == True:
            img 8265
            with fade
            dick_secretary "Вы уже опоздали, Мистер Дик..."
            dick "Как это я уже опоздал?"
            img 8266
            dick_secretary "Эта Миссис Бакфетт..."
            "Я не хотела, Мистер Дик!"
            "Но она... Она сама... Буквально силой..."
            "Простите!!!"
            img 8265
            dick "О, Малышка! Я знаю эту Бакфетт!"
            "Она всегда добивается своего!"
            "Куда уж тебе, бедной девочке, справиться с ней!"
            img 8266
            dick_secretary "Да, Мистер Дик!"
            "Обещайте что будете защищать меня!"
            dick "Я буду защищать тебя, Виктория!"
            img 8267
            with fade
            dick "..."
            dick "Значит мне придется быть вторым?"
            dick_secretary "Если Вы не брезгуете ласкать меня после лица Миссис Бакфетт..."
            dick "Моника весьма чистоплотна..."
            dick_secretary "Хорошо, Мистер Дик. Как скажете..."

        "Я бы хотела чтобы Миссис Бакфетт первая сделала это... (отказать)":
            img 8267
            with fade
            dick_secretary "Я бы хотела чтобы Миссис Бакфетт первая сделала это..."
            #выход
            return


    #Виктория встает на колени на стол, а Дик ее лижет
    music Loved_Up2
    scene black
    image videov_Dick_Victoria_Sex_1_1 = Movie(play="video/v_Dick_Victoria_Sex_1_1.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_1
    with fadelong
    dick "Ммммммм"
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_2 = Movie(play="video/v_Dick_Victoria_Sex_1_2.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_2
    dick "Мммммм... ням"
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_3 = Movie(play="video/v_Dick_Victoria_Sex_1_3.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_3
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_4 = Movie(play="video/v_Dick_Victoria_Sex_1_4.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_4
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_5 = Movie(play="video/v_Dick_Victoria_Sex_1_5.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_5
    wclean
    "Виктория, ты божество!"
    scene black
    image videov_Dick_Victoria_Sex_1_6 = Movie(play="video/v_Dick_Victoria_Sex_1_6.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_6
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_7 = Movie(play="video/v_Dick_Victoria_Sex_1_7.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_7
    wclean
    dick_secretary "Мистер Дик, у меня вкусная попка?"
    dick "У тебя самая вкусная попка на свете!"
    scene black
    image videov_Dick_Victoria_Sex_1_8 = Movie(play="video/v_Dick_Victoria_Sex_1_8.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_8
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_9 = Movie(play="video/v_Dick_Victoria_Sex_1_9.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_9
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_10 = Movie(play="video/v_Dick_Victoria_Sex_1_10.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_10
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_11 = Movie(play="video/v_Dick_Victoria_Sex_1_11.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_11
    wclean
    scene black
    image videov_Dick_Victoria_Sex_1_12 = Movie(play="video/v_Dick_Victoria_Sex_1_12.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_12
    wclean
    if monicaVictoriaLickAssAtBegin == True:
        dick_secretary "Как Вы думаете, она нравится Миссис Бакфетт?"
        dick "О! Виктория! Я думаю она без ума от нее!"
    else:
        dick_secretary "Как Вы думаете, она понравится Миссис Бакфетт?"
        dick "О! Виктория! Я думаю она будет без ума от нее!"
    scene black
    image videov_Dick_Victoria_Sex_1_13 = Movie(play="video/v_Dick_Victoria_Sex_1_13.mkv", fps=30)
    show videov_Dick_Victoria_Sex_1_13
    with fade
    wclean
    music stop
    img black_screen
    with Dissolve(0.7)
    pause 1.0
    return

label gallery_14070:
    # Мелани входит в здание Дика. Ее видит секретарь на рецепшене.
    # 2-3 кадра как подходит.
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    music m80s_Things
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_29
    scene black_screen
    with Dissolve(1)
#    music Groove2_85
    img 13937
    with fadelong
    w
    img 13938
    with diss
    w
    img 13939
    with diss
    w
    img 13942
    with diss
    w
    img 13940
    with fade
    reception_secretary "Здравствуйте, Мисс Мелани!" #+
    reception_secretary "Рада снова видеть Вас!"
    reception_secretary "Вы решили навестить Мистера Дика?"
    music ZigZag
    img 13941
    with diss
    melanie "Да, верно." #-
    melanie "Его офис все там-же?"
    img 13943
    with fade
    reception_secretary "Да, его офис там же." #-
    reception_secretary "Разрешите Вас проводить туда?"
    img 13944
    with diss
    melanie "Нет необходимости в этот раз." #+
    melanie "Я помню как туда подняться."
    img 13945
    with fade
    reception_secretary "Если что-то понадобится, дайте мне знать!" #-
    img 13946
    with diss
    melanie "Спасибо." #- #уходит

    music stop
    img black_screen
    with diss
    sound snd_lift
    pause 2.0
    # звук лифта, Мелани заходит в приемную к Дику
    # Там секретарши нет
    music ZigZag
    img 13947
    with fadelong
    melanie "Странно, а где эта маленькая девочка, которая думает что знает что и в чьих интересах..." #-
    melanie "Надо высказать Дику свое неудовольствие ей."
    img 13948
    with diss
    melanie "..." #- вид из-за стола (пустого) Мелани смотрит на стол
    img 13949
    with fade
    melanie "И где сам Дик?" #+ вид сзади Мелани, на дверь
    melanie "Наверное, в своем кабинете..."

    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound highheels_short_walk
    pause 1.5
    sound snd_door_close1
    music Groove2_85
    # Мелани заходит в кабинет Дика. Там на кресле надменно сидит Виктория
    img 13950
    with fadelong
    dick_secretary "О, Мисс Мелани..." #+
    dick_secretary "Проходите, я Вас как раз ждала..."
    music ZigZag
    # Мелани надменно отвечает
    img 13951
    with fade
    melanie "Девочка, я не ошиблась кабинетом?" #-
    melanie "Или, может быть, это ты ошиблась стулом?"
    img 13952
    with diss
    melanie "Я пришла к Мистеру Дику, твоему Боссу." #+
    melanie "Любишь посидеть на его месте, пока его нет?"
    music Groove2_85
    img 13953
    with fade
    dick_secretary "Вы не ошиблись кабинетом, Мисс Мелани." #-
    dick_secretary "И Вы пришли ко мне, а не к Мистеру Дику."
    dick_secretary "Это я пригласила Вас..."
    music ZigZag
    img 13954
    with fade
    melanie "Ты?!" #-
    melanie "Не слишком-ли смелая инициатива, юная девочка?"
    melanie "Это слишком много чести для маленькой секретарши, которая спит со своим Боссом."
    melanie "Ты ведь знаешь кто я такая."
    music Groove2_85
    img 13955
    with diss
    dick_secretary "Я знаю кто Вы такая, Мисс Мелани..." #+
    music ZigZag
    img 13956
    with fade
    melanie "Ты ревнуешь и делаешь глупости, но помни." #+
    melanie "Я могу щелчком пальцев лишить тебя милости твоего Босса и этой работы."
    melanie "Ты играешь с огнем, девочка."
    music Groove2_85
    img 13957
    with fade
    dick_secretary "Мисс Мелани." #-
    dick_secretary "Меня трогают Ваши слова, но я трачу сейчас свое время на разговор, который в Ваших же интересах."
    music ZigZag
    img 13958
    with fade
    melanie "У нас с тобой разные интересы, девочка." #-
    melanie "И они никак не могут пересекаться."
    melanie "Ты не можешь сказать ничего, что могло бы заинтересовать меня."
    melanie "Ты очень предсказуемая и примитивная."
    melanie "Я вижу тебя насквозь."
    music Groove2_85
    img 13959
    with fade
    dick_secretary "Мисс Мелани, Вы продолжаете делать все, чтобы более и более нравиться мне." #-

    # Серьезное лицо
    img 13960
    with diss
    dick_secretary "Но перейдем к делу."  #+ сбоку
    img 13961
    with fade
    dick_secretary "В круг моих знакомых входит фотограф, папарацци." #+ прямо, чуть снизу
    dick_secretary "Он следит за знаменитостями, вроде Вас."

    # Надменное, напряженное, сосредоточенное
    img 13962
    with diss
    melanie "..." #+

    # Сосредоточенное, злое
    img 13963
    with diss
    dick_secretary "..." #+

    # Надменное
    music ZigZag
    img 13964
    with fadelong
    melanie "Таких знаменитых моделей как Я окружает множество извращенцев." #-
    melanie "Я к этому привыкла."
    melanie "Чем ты хочешь меня удивить, девочка?"


    # деловое
    music stop
    img black_screen
    with diss
    pause 0.5
    music Groove2_85
    img 13965
    with fade
    dick_secretary "Дело в том, что Мистер Дик уже какое-то время занимается делом некой Моники Бакфетт." #-
    dick_secretary "Она чем-то неугодила некоему Мистеру Маркусу и теперь отчаянно нуждается в помощи."
    dick_secretary "Вы знаете что-нибудь про это, Мисс Мелани?"

    # Мелани напряжена, но старается держаться надменно
    music ZigZag
    img 13966
    with fade
    melanie "Я знаю Миссис Бакфетт. Это мой бывший Босс." #-
    melanie "Она покинула место работы и теперь я не знаю что с ней."
    img 13967
    with diss
    melanie "Меня это неинтересует." #+
    melanie "Это все?"
    music Groove2_85
    sound snd_paper1
    img 13968
    with fade
    dick_secretary "Мисс Мелани." #-
    dick_secretary "Пожалуйста, взгляните на эти снимки."

    # Мелани подходит
    img 13969
    with fade
    melanie "..."
    sound snd_paper1
    img 13970
    with diss
    dick_secretary "Вот на этот."
    # Кладет на стол снимок как Мелани показывает грудь Дику
    img 13971
    with diss
    w
    img 13972
    with diss
    w
    sound snd_paper2
    img 13973
    with fade
    dick_secretary "И вот на этот."
    # Кладет снимок как Мелани общается с Моникой у нее дома
    music Power_Bots_Loop
    img 13974
    with hpunch
    w
    img 13975
    with diss
    w
    music ZigZag
    img 13976
    with fade
    melanie "И что с того?" #-
    melanie "Эти снимки сделаны в разное время."
    melanie "На первом - моя личная жизнь."
    melanie "На втором - Миссис Бакфетт навестила меня для того, чтобы..."

    music Groove2_85
    # крупным, ехидно
    sound snd_woman_laugh3
    img 13977
    with diss
    dick_secretary "Для того, чтобы попросить Вас о помощи." #+

    # зло
    music ZigZag
    img 13978
    with fade
    melanie "Это не твое дело, девочка." #+
    melanie "Я понимаю твою ревность, но смирись с тем, что Я нравлюсь твоему Боссу больше чем ТЫ."

    # Виктория злится, крупный план
    music Groove2_85
    img 13979
    with diss
    dick_secretary "..." #+

    # Виктория снова надменно улыбается
    sound snd_paper2
    img 13980
    with fadelong
    dick_secretary "Если мы положим эти снимки в следующем порядке..." #- сбоку издалека
    # Кладет снимки, где сначала разговор с Моникой, затем с Диком
    img 13981
    with fade
    dick_secretary "То становится очевидно, что Миссис Бакфетт пришла к Вам за помощью." # сверху на снимки
    dick_secretary "Затем Вы помогли ей, соблазнив Мистера Дика, моего Босса."
    img 13983
    with diss
    melanie "..." #+
    img 13984
    with fade
    dick_secretary "Мистер Маркус связывался со мной какое-то время назад." #-
    dick_secretary "И просил сообщить ему, если кто-либо еще будет пытаться помочь Миссис Бакфетт."

    # Мелани переживает
    music Power_Bots_Loop
    img 13985
    with hpunch
    melanie "!!!" #+
    img 13986
    with fade
    dick_secretary "Я решила пойти Вам навстречу и сообщила Вам об этом до того, как эти кадры попадут на публику." #+
    dick_secretary "И до того, как эти кадры попадут к Мистеру Маркусу."
    dick_secretary "Я подумала что это может заинтересовать Вас, Мисс Мелани."
    music Power_Bots_Loop
    img 13987
    with diss
    melanie "..." #-
    music Groove2_85
    img 13988
    with fade
    dick_secretary "Вам это интересно или мы можем закончить разговор?" #-
    music Hidden_Agenda
    img 13989
    with fade
    melanie "Виктория, я бы..." #+
    img 13990
    with diss
    melanie "Я бы предпочла, чтобы эти фото не попадали на публику и к Мистеру Маркусу вовсе..." # сбоку издалека
    music Groove2_85
    img 13991
    with fade
    dick_secretary "Это весьма сложно, Мисс Мелани." #-
    dick_secretary "Мой знакомый хочет заработать на этих фото."
    img 13992
    with diss
    dick_secretary "К тому же, мне показалось что Мистер Маркус влиятельный человек." #+
    dick_secretary "И может достойно отблагодарить меня за помощь."
    dick_secretary "Вы знакомы с ним?"
    music Power_Bots_Loop
    img 13993
    with hpunch
    melanie "!!!" #+
    img 13994
    with diss
    melanie "Я..." #-
    melanie "Я немного знакома с ним..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 13995
    with fadelong
    melanie "Мисс Виктория." #+
    melanie "Мы с Вами умные люди."
    melanie "Я уверена, что мы можем найти компромисс."
    melanie "Назовите сумму."
    music Groove2_85
    img 13996
    with fade
    dick_secretary "Ах, деньги..." #-
    dick_secretary "Да, это разумное предложение."
    dick_secretary "И я готова принять их, но..."
    img 13997
    with diss
    melanie "Что Но?.." #+
    img 13998
    with fade
    dick_secretary "Я не принимаю подарков от незнакомых людей..." #+
    music Power_Bots_Loop
    img 13999
    with diss
    melanie "Что ты имеешь ввиду, девочка?" #+
    music Groove2_85
    img 14000
    with diss
    dick_secretary "Мисс Виктория." #+ зло

    # злится в сторону
    music Power_Bots_Loop
    img 14001
    with fade
    melanie "..." #+

    # смотрит язвительно, но напряженно
    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 14002
    with fadelong
    melanie "Что Вы имеете ввиду, Мисс Виктория?" #-
    music Groove2_85
    img 14003
    with fadelong
    dick_secretary "Видите-ли, Мисс Мелани." #-
    dick_secretary "У меня здесь ответственная работа."
    dick_secretary "У меня строгий Босс, который учит меня не доверять незнакомым людям."
    dick_secretary "Поэтому я не могу принять у Вас Ваши деньги."
    music Power_Bots_Loop
    img 14004
    with diss
    melanie "..." #+
    img 14005
    with diss
    dick_secretary "..." #+ прищурившись зло
    music ZigZag
    img 14006
    with fadelong
    melanie "Что мне сделать, чтобы Вы стали доверять мне, Мисс Виктория." #-
    music Groove2_85
    img 14007
    with fade
    dick_secretary "Вы должны сделать так, чтобы я могла доверять Вам, Мисс Мелани." #-

    # подозрительно
    music ZigZag
    img 14008
    with fade
    melanie "Что для этого надо сделать?" #+

    # ехидно
    music Loved_Up
    sound snd_woman_laugh2
    img 14009
    with diss
    dick_secretary "Стать моей подружкой." #+
    music ZigZag
    img 14010
    with fade
    melanie "Что мне надо сделать, чтобы стать Вашей подружкой, Мисс Виктория?" #-
    music Groove2_85
    img 14011
    with fade
    dick_secretary "Мисс Мелани, Вам надо попросить меня о том, чтобы стать ей." #-
    dick_secretary "Затем вести себя как хорошая подружка."
    dick_secretary "С плохими подружками я не дружу."
    dick_secretary "И для плохих подружек я не буду идти на жертвы, чтобы не распространять их неосторожные фото..."
    music Power_Bots_Loop
    img 14012
    with diss
    melanie "..." #+ напряжена
    img 14013
    with diss
    dick_secretary "..." #+ язвительная (вообще она все время язвительная, если не злится)
    img 14014
    with diss
    melanie "!!!" #+
    img 14015
    with diss
    dick_secretary "???" #+ язвительно, смотрит искоса вопрошающе
    img 14016
    with fade
    menu:
        "Попросить Викторию стать ее подружкой.":
            pass
        "Уйти.":
            music stop
            img black_screen
            with diss
            pause 1.5
            music Power_Bots_Loop
            img 14017
            with fadelong
            melanie "Мне надо подумать!" #- уходит
            img 14018
            with diss
            dick_secretary "Думайте быстрее, Мисс Мелани!"
            return

    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 14019
    with fadelong
    melanie "Мисс Виктория..." #-
    melanie "Я хочу стать Вашей подружкой."
    music Groove2_85
    img 14020
    with diss
    dick_secretary "Неубедительно." #-
    dick_secretary "Я не верю в искренность Ваших слов."
    dick_secretary "Попробуйте еще раз."

    # в сторону
    music Power_Bots_Loop
    img 14021
    with diss
    melanie "!!!" #+
    music ZigZag
    img 14022
    with fade
    melanie "Мисс Виктория..." #-
    melanie "Я - Мелани, самая популярная модель Модного Журнала."
    melanie "Я очень известна и знаменита."
    melanie "И Я бы очень хотела стать Вашей подружкой."
    melanie "И была бы счастлива, если бы Вы приняли мою дружбу с Вами..."
    music Groove2_85
    img 14023
    with fade
    dick_secretary "Хорошо, но ты обещаешь быть хорошей подружкой?" #-
    dick_secretary "Каждый четверг присылать мне сертификат на $ 10.000 и делать все что я скажу."
    music Power_Bots_Loop
    img 14024
    with hpunch
    melanie "!!!" #+
    img 14025
    with diss
    dick_secretary "..." #+ язвительно

    # Мелани смотрит близким планом на фото
    img 14026
    with diss
    melanie "!!!"

    # Зло щурится
    img 14027
    with diss
    dick_secretary "???" #+
    music stop
    img black_screen
    with diss
    pause 1.0
    music ZigZag
    img 14028
    with fadelong
    melanie "Да, я согласна..." #-
    music Groove2_85
    img 14029
    with fade
    dick_secretary "Повтори все что я сказала!" #-
    music Power_Bots_Loop
    img 14030
    with diss
    melanie "!!!" #+
    img 14031
    with diss
    dick_secretary "!!!" #+ зло

    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 14032
    with fadelong
    melanie "Я..." #-
    melanie "Я обещаю что буду хорошей подружкой."
    melanie "И буду каждый четверг присылать Вам сертификат на $ 10.000."
    img 14033
    with diss
    dick_secretary "И?" #-
    music Power_Bots_Loop
    img 14034
    with diss
    melanie "..." #+
    img 14035
    with diss
    dick_secretary "..." #+
    music Hidden_Agenda
    img 14036
    with fadelong
    melanie "И буду делать что Вы скажете, Мисс Виктория." #-
    music Groove2_85
    img 14037
    with fade
    dick_secretary "Хорошо, подружка." #-
    dick_secretary "Пока ты будешь хорошей подружкой, эти фото останутся только у меня."
    img 14038
    with diss
    melanie "..." #+

    if monicaShowedBoobsToVictoriaCamera == True:
        img 14039
        with fade
        dick_secretary "Да, кстати." #-
        dick_secretary "У меня есть еще одна подружка, которую ты хорошо знаешь."

        # Кладет фото Моники, где она показывает грудь на телефон
        sound snd_paper2
        img 14046
        with diss
        w
        # Мелани крупным планом, напряжена
        img 14047
        with diss
        melanie "..."
        img 14048
        with diss
        dick_secretary "Она навещает меня регулярно." #крупный план фотографии Моники
        dick_secretary "Однако, она не всегда себя хорошо ведет."
        dick_secretary "И, чтобы сновать стать хорошей подружкой, ей приходится просить прощения у меня."
        sound snd_woman_laugh
        img 14049
        with diss
        melanie "..." # вид из фотографии на Мелани
    else:
        img 14039
        with fade
        dick_secretary "Да, кстати." #-
        dick_secretary "У меня есть еще одна подружка, которую ты хорошо знаешь."
        dick_secretary "Она навещает меня регулярно." #крупный план фотографии Моники
        dick_secretary "Однако, она не всегда себя хорошо ведет."
        dick_secretary "И, чтобы сновать стать хорошей подружкой, ей приходится просить прощения у меня."
        sound snd_woman_laugh
        img 14049
        with diss
        melanie "..." # вид из фотографии на Мелани

    if monicaShowedBoobsToVictoriaCamera == True:

        # Достает телефон
        sound Jump1
        img 14050
        with fade
        dick_secretary "Это хорошо что ты одела ту же шубку, что и на фото."  #-
        dick_secretary "Можно сделать хороший кадр."
        sound snd_woman_laugh3
        img 14051
        with diss
        melanie "..." #-
        img 14052
        with fade
        dick_secretary "Могу поспорить, что под этой шубкой ничего нет." #+ держит телефон
        dick_secretary "Ты ведь пришла для того, чтобы трясти своими сиськами перед Диком, да?"
        music Power_Bots_Loop
        img 14053
        with diss
        melanie "!!!" #+

        # В одной руке телефон, держащий для фото, в другой - фото Моники с грудью
        # Поворачивает фото к Мелани. Видто спину Мелани, фото и ехидную Викторию
        music Groove2_85
        sound snd_paper1
        img 14054
        with fade
        dick_secretary "Давай, показывай их, как это сделала первая подружка." #

        # Поворачивает фото к себе, держа рядом с телефоном
        img 14055
        with diss
        dick_secretary "Я хочу сделать фото и сравнить Ваши сиськи."

        # возмущенно
        music Power_Bots_Loop
        img 14056
        with fade
        melanie "!!!" #+
        img 14057
        with diss
        melanie "Я не буду показывать свою грудь!" #-
        melanie "Я уважающая себя женщина и..."

        # пренебрежительно
        # убирает телефон и фото
        sound snd_paper2
        img 14058
        with fade
        dick_secretary "Ты плохая подружка! Можешь уходить!" #-
        dick_secretary "Хорошая подружка не пререкается со мной."
        img 14059
        with diss
        melanie "!!!" #+
        img 14060
        with fade
        dick_secretary "Можешь идти, я не задерживаю тебя!" #+
        img 14061
        with diss
        melanie "!!!" #+
        img 14062
        with diss
        dick_secretary "..." #+
    else:
        # Достает телефон
        sound Jump1
        img 14052
        with fade
        dick_secretary "Это хорошо что ты одела ту же шубку, что и на фото."  #-
        dick_secretary "Можно сделать хороший кадр."
        sound snd_woman_laugh3
        img 14051
        with diss
        melanie "..." #-
        img 14052
        with fade
        dick_secretary "Могу поспорить, что под этой шубкой ничего нет." #+ держит телефон
        dick_secretary "Ты ведь пришла для того, чтобы трясти своими сиськами перед Диком, да?"
        music Power_Bots_Loop
        img 14053
        with diss
        melanie "!!!" #+

        music Power_Bots_Loop
        img 14056
        with fade
        melanie "!!!" #+
        melanie "Я не буду показывать свою грудь!" #-
        melanie "Я уважающая себя женщина и..."

        # пренебрежительно
        # убирает телефон и фото
        sound snd_paper2
        img 14058
        with fade
        dick_secretary "Ты плохая подружка! Можешь уходить!" #-
        dick_secretary "Хорошая подружка не пререкается со мной."
        img 14059
        with diss
        melanie "!!!" #+
        img 14060
        with fade
        dick_secretary "Можешь идти, я не задерживаю тебя!" #+
        img 14061
        with diss
        melanie "!!!" #+
        img 14062
        with diss
        dick_secretary "..." #+

    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 14063
    with fadelong
    melanie "..." #-
    melanie "Хорошо..."
    melanie "Я сделаю это, но на этом все, договорились?"
    music Groove2_85
    img 14064
    with fade
    dick_secretary "Это только начало, подружка!" #-
    dick_secretary "Да, и еще одно пререкание и я с тобой больше не дружу!"
    img 14065
    with diss
    melanie "!!!" #+

    # Снова достает телефон и фото
    sound Jump1
    img 14052
    with fade
    dick_secretary "Давай, показывай!" #+ держит телефон
    dick_secretary "Мне нужно фото, дискредитирующее тебя перед Мистером Диком!"
    melanie "..." #-

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    # Мелани показывает грудь
    img 14070
    with fadelong
    w
    # щелчок фото
    sound camera_lens1
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14069
    else:
        img 14068
    with Dissolve(0.2)
    w
    call photoshop_flash() from _rcall_photoshop_flash_165
    w
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14071
    else:
        img 14070
    with Dissolve(0.2)
    w
    call photoshop_flash() from _rcall_photoshop_flash_166
    w
    music Groove2_85
    img 14068
    with diss
    dick_secretary "Отлично!" #+ держит телефон
    dick_secretary "Теперь Мистер Дик поймет, что ты такая же шлюха, как и Бакфетт!"
    music Power_Bots_Loop
    img 14072
    with diss
    melanie "!!!" #+
    music Groove2_85
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14073
        with fade
        dick_secretary "У тебя красивая грудь, подружка!" #-
        img 14074
        with diss
        melanie "Я знаю..." #-
        melanie "Мисс Виктория..."
        melanie "Все мечтают о такой груди, как у меня..."

        # Удаление
        img 14075
        with fade
        dick_secretary "Но скажи, чья грудь лучше?" #-
    else:
        img 14068
        with fade
        dick_secretary "У тебя красивая грудь, подружка!" #-
        img 14072
        with diss
        melanie "Я знаю..." #-
        melanie "Мисс Виктория..."
        melanie "Все мечтают о такой груди, как у меня..."
        # Удаление
        img 14052
        with fade
        dick_secretary "Но скажи, чья грудь лучше?" #-


    # Крупным
    img 14076
    with diss
    dick_secretary "Твоя или моя?" #+
    img 14077
    with diss
    melanie "..." #+

    # прищуривается
    img 14078
    with fade
    dick_secretary "..." #+
    dick_secretary "Хорошенько подумай, прежде чем ответить, подружка..."
    img 14079
    with diss
    melanie "..." #+
    img 14080
    with diss
    melanie "Ваша грудь лучше, Мисс Виктория..." #-
    sound snd_woman_laugh

    if monicaShowedBoobsToVictoriaCamera == True:
        img 14081
    else:
        img 14076
    with fade
    dick_secretary "Правильный ответ." #-
    dick_secretary "Хорошая подружка!"

    if game.extra == True:
        dick_secretary "А теперь потряси своими сиськами. Я хочу снять видео!"
        music Power_Bots_Loop
        img 14072
        with diss
        melanie "!!!"
        music Groove2_85
        img 14068
        with fade
        dick_secretary "Мне надо повторить? Хочешь быть плохой подружкой?"
        img 14079
        with diss
        melanie "..."
        # video shaking boobs
        music stop
        img black_screen
        with diss
        pause 2.0
#        music Loved_Up2
        music audio_Melanie_Victoria_Boobs_1
        if monicaShowedBoobsToVictoriaCamera == True:
            scene black
            image videov_Melanie_Victoria_Boobs_1_1 = Movie(play="video/v_Melanie_Victoria_Boobs_1_1.mkv", fps=30)
            show videov_Melanie_Victoria_Boobs_1_1
            wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_2 = Movie(play="video/v_Melanie_Victoria_Boobs_1_2.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_2
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_3 = Movie(play="video/v_Melanie_Victoria_Boobs_1_3.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_3
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_4 = Movie(play="video/v_Melanie_Victoria_Boobs_1_4.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_4
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_5 = Movie(play="video/v_Melanie_Victoria_Boobs_1_5.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_5
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_6 = Movie(play="video/v_Melanie_Victoria_Boobs_1_6.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_6
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_7 = Movie(play="video/v_Melanie_Victoria_Boobs_1_7.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_7
        wclean
    music stop
    img black_screen
    with diss
    pause 1.5
    # Мелани закрывается
    music Groove2_85
    img 14082
    with fade
    melanie "Мисс Виктория, мы закончили?" #-
    melanie "Я могу идти?"
    img 14083
    with diss
    dick_secretary "Нет, подружка." #-
    dick_secretary "Я хочу чтобы ты мне помогла..."
    img 14084
    with diss
    melanie "..." #+
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14085
        with fade
    melanie "В чем Вы хотите чтобы я Вам помогла, Мисс Виктория?" #-
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14086
        with diss
    else:
        img 14083
        with diss
    dick_secretary "Подружка, я ждала тебя здесь целый день." #+
    # Кладет ногу в сапоге на стол
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 14087
    with fadelong
    w
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14088
        with diss
        w
    sound desk_open
    img 14089
    with diss
    w
    sound Jump1
    img 14090
    with fade
    dick_secretary "Я всегда ношу сапожки, чтобы выглядеть красиво." #-
    dick_secretary "И, пока я тебя ждала, у меня затекла ножка."

    # смотрит на ногу
    img 14091
    with diss
    melanie "..."
    img 14092
    with fade
    dick_secretary "Пожалуйста, сними этот сапожок!" #+
    dick_secretary "Будь хорошей подружкой!"
    music Power_Bots_Loop
    img 14093
    with diss
    melanie "!!!" #+

    # смотрит вопросительно - язвительно
    img 14094
    with diss
    dick_secretary "..." #+

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    # мелани начинает снимать сапог
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14096
        with fadelong
        w
    sound snd_zip
    img 14095
    with diss
    w
    img 14097
    with diss
    w
    sound snd_zip
    img 14098
    with diss
    w
    # снимает сапог
    sound snd_boot1
    img 14099
    with fade
    dick_secretary "Хорошо, а теперь сделай моей ножке массаж своей грудью..." #-
    music Power_Bots_Loop
    img 14100
    with hpunch
    melanie "ЧТО?!" #+
    img 14101
    with diss
    melanie "Моей грудью?! Трогать моей грудью твои ноги?!!" #-
    img 14102
    with diss
    dick_secretary "Кажется я слышала пререкание?" #+
    dick_secretary "Или мне послышалось?"

    # Мелани отвернулась в бешенстве
    img 14103
    with diss
    melanie "!!!" #+
    img 14104
    with fade
    dick_secretary "Мне послышалось?" #-
    dick_secretary "Или передо мной плохая подружка?!"

    # Мелани смотрит на фото
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14105
        with diss
    melanie "!!!"

    # Зло смотрит
    img 14106
    with diss
    dick_secretary "..." #+
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 14107
    with fadelong
    melanie "Вам послышалось, Мисс Виктория..." #-
    img 14108
    with fade
    dick_secretary "Давай, подружка!" #-
    dick_secretary "Твои сиськи - это твой основной рабочий инструмент."
    dick_secretary "С помощью этого инструмента ты сделала карьеру."

    # Мелани садится и тянется грудью к ноге Виктории
    sound desk_open
    img 14109
    with diss
    dick_secretary "Почему бы не использовать его, чтобы снять усталось у лучшей подружки?"
    img 14110
    with diss
    melanie "..."
    sound snd_woman_laugh2
    img 14111
    with diss
    dick_secretary "Я ведь твоя лучшая подружка, Мелани? Правда?"
    img 14112
    with diss
    melanie "!!!"
    img 14113
    with fade
    melanie "Вы..."
    melanie "Вы моя лучшая подружка, Мисс Виктория..."
    music stop
    img black_screen
    with diss
    pause 2.0
    music2 audio_Melanie_Victoria_Titjob_1b
    stop music
    play music "Sounds/audio_Melanie_Titjob_1a.mp3"
    scene black
    image videov_Melanie_Victoria_Titjob_1_1 = Movie(play="video/v_Melanie_Victoria_Titjob_1_1.mkv", fps=30)
    show videov_Melanie_Victoria_Titjob_1_1
    with fadelong
    wclean
    stop music
    play music "Sounds/audio_Melanie_Titjob_1a.mp3"
    scene black
    image videov_Melanie_Victoria_Titjob_1_2 = Movie(play="video/v_Melanie_Victoria_Titjob_1_2.mkv", fps=30)
    show videov_Melanie_Victoria_Titjob_1_2
    dick_secretary "Да, Давай!"
    wclean
    if game.extra == True:
        stop music
        play music "Sounds/audio_Melanie_Titjob_1a.mp3"
        scene black
        image videov_Melanie_Victoria_Titjob_1_4 = Movie(play="video/v_Melanie_Victoria_Titjob_1_4.mkv", fps=30)
        show videov_Melanie_Victoria_Titjob_1_4
        dick_secretary "Хорошенько работай своими сиськами, Да!"
        wclean
        stop music
        play music "Sounds/audio_Melanie_Titjob_1a.mp3"
        scene black
        image videov_Melanie_Victoria_Titjob_1_5 = Movie(play="video/v_Melanie_Victoria_Titjob_1_5.mkv", fps=30)
        show videov_Melanie_Victoria_Titjob_1_5
        dick_secretary "Меня так возбуждает!"
        wclean
        stop music
        play music "Sounds/audio_Melanie_Titjob_1a.mp3"
        scene black
        image videov_Melanie_Victoria_Titjob_1_6 = Movie(play="video/v_Melanie_Victoria_Titjob_1_6.mkv", fps=30)
        show videov_Melanie_Victoria_Titjob_1_6
        wclean

    music2 stop
    music Loved_Up
    # video
    sound hlup25
    img 14114
    with diss
    w
    if monicaShowedBoobsToVictoriaCamera == True:
        sound hlup10
        img 14115
        with diss
    dick_secretary "Эти сиськи стоят миллоны долларов."
#    w
    sound hlup10
    img 14116
    with diss
    dick_secretary "Тебе пишут сотни тысяч поклонников, Да?"
#    w
    sound hlup25
    img 14117
    with diss
    melanie "Да, Мисс Виктория..."
#    w





    # end video
    label gallery_14122:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 14118
    with fadelong
    dick_secretary "Но я думаю это лучшее применение твоим сиськам, нежели показ их Мистеру Дику!"
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14119
        with diss
    melanie "!!!"
    img 14120
    with fade
    dick_secretary "Скажи, ты рада сделать массаж своей лучшей подружке?"
    img 14121
    with diss
    melanie "!!!"
    img 14122
    with fade
    melanie "Да, я рада сделать Вам массаж, Мисс Виктория..."
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14123
        with diss
    dick_secretary "Хорошо..."
    dick_secretary "Возьми мой большой пальчик себе в рот..."
    music Power_Bots_Loop
    img 14124
    with hpunch
    menu:
        "Сделать что приказала Виктория.":
            pass
        "Уйти.":
            music stop
            img black_screen
            with diss
            pause 1.5
            music Power_Bots_Loop
            if monicaShowedBoobsToVictoriaCamera == True:
                img 14127
            else:
                img 14128
            with fadelong
            melanie "Я не готова сделать это!"
            dick_secretary "Хорошая подружка должна быть готова всегда."
            return
    # Мелани в шоке, злится
    img 14125
    with fade
    melanie "!!!"

    # ехидно
    img 14126
    with diss
    dick_secretary "Мне надо повторить?"

    # Мелани берет ногу Виктории в рот
    label gallery_14130:
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    sound hlup19
    img 14129
    with fadelong
    w
    img 14130
    with diss
    w
    # Виктория рукой держит между ног (мастурбирует)
    img 14131
    with fade
    dick_secretary "Ах! Как чудесно!"
    sound hlup21
    img 14132
    with diss
    w
    img 14133
    with diss
    dick_secretary "Ах! Ах!"

    # Мелани продолжает держать ногу во рту
    if monicaShowedBoobsToVictoriaCamera == True:
        sound hlup19
        img 14134
        with fade
    melanie "!!!"
    img 14135
    with diss
    dick_secretary "А теперь... теперь..."
    # Виктория кончает
    img 14136
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    dick_secretary "Теперь... АААаааааааххххх!!!"
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14137
    with fadelong
    dick_secretary "Ладно, подружка..." #+
    dick_secretary "На сегодня хватит..."
    dick_secretary "Мы продолжим нашу дружбу позже..."

    # Мелани встает, Виктория убирает ногу
    sound snd_woman_laugh3
    img 14128
    with fade
    dick_secretary "Ты можешь идти, подружка, но помни про наш уговор..." #-

    # Мелани уходит, закрывая рукой рот в отвращении и злобе, другой рукой закрывает шубу.

    return

label gallery_15472:
    music ZigZag
    sound highheels_short_walk
    img 15462
    with fadelong
    w
    img 15463
    with diss
    melanie "Виктория, здравствуй. Я рада нашей встрече."
    music Groove2_85
    img 15464
    with diss
    victoria "Уже лучше."
    victoria "Хорошие подружки целуются при встрече. Потому что действительно рады встрече."
    img 15465
    with fade
    victoria "..."
    victoria "Ты же хорошая подружка?"
    # Мелани молча смотрит на нее
    music ZigZag
    img 15466
    with diss
    melanie "..."
    img 15467
    with fade
    melanie_t "Эта сучка откровенно издевается надо мнойю."
    melanie_t "Сейчас я поиграю по ее правилам..."
    img 15468
    with diss
    melanie_t "Она ведь не просто так позвала меня."
    melanie_t "Нужно узнать, что она хочет."
    melanie_t "Но я не оставлю подобное поведение безнаказанным..."
    img 15469
    with diss
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани подходит и целует Виктория в щеку, та самодовольно улыбается
    sound highheels_short_walk
    img 15470
    with fade
    w
    img 15471
    with diss
    w
    music Loved_Up
    img 15472
    with fade
    sound snd_kiss2
    w
    img 15473
    with diss
    victoria "Подружка соскучилась по мне?"
    # Мелани отходит от Викториии снова встает перед ее столом, сверлит ее взглядом
    music Groove2_85
    img 15474
    with fade
    melanie "..."
    img 15475
    with diss
    victoria "Я не слышу ответа..."
    victoria "Возможно, я ошибаюсь и ты не моя подружка?"
    victoria "Ты не соскучилась по мне?"
    music ZigZag
    img 15476
    with fade
    melanie "Конечно, соскучилась... Подружка."
    # Виктория довольно хихикает
    music Loved_Up
    img 15477
    with diss
    sound snd_woman_laugh3
    victoria "Раз ты так скучаешь по мне, подружка..."
    victoria "То, так уж и быть, я найду время, чтобы навестить тебя сегодня."
    victoria "Я приду к тебе вечером в гости."
    img 15478
    with fade
    victoria "И еще я хочу, чтобы вторая наша подружка тоже пришла."
    victoria "Уверена, она тоже соскучилась по мне. Как ты думаешь?"
    # Мелани удивленно приподнимает бровь
    music Power_Bots_Loop
    img 15479
#    with diss
    melanie "Ко мне в гости?"
    melanie "..."
    music Hidden_Agenda
    img 15480
    with fade
    victoria "Да. Я тут подумала, что ни разу не была у тебя в гостях."
    victoria "А подружки ходят друг другу в гости и устраивают девичники."
    img 15481
    with diss
    victoria "Сегодня вечером я хочу устроить девичник с моими хорошими подружками."
    victoria "Ты ведь рада, что я приду к тебе в гости?"
    victoria "Ты же хорошая подружка?"
    # Мелани молчит
    music Master_Disorder
    img 15482
    with fade
    melanie "..."
    img 15483
    with diss
    menu:
        "Согласиться на предложение Виктории":
            music Master_Disorder
            img 15484
            with fade
            melanie_t "Она явно что-то задумала..."
            melanie_t "Узнать это можно только одним способом - согласиться, чтобы она пришла ко мне."
            img 15485
            with diss
            melanie_t "Эта мелкая сучка не напугает меня, как бы она не старалась."
            melanie_t "Она ничего мне не сделает. Она и может только, что угрожать и все. На большее она не способна."
            pass
        "Отказаться":
            music ZigZag
            img 15486
            with fade
            melanie "Cегодня вечером я буду занята."
            melanie "Меня не будет дома."
            # Виктория хмурится и пристально смотрит на Мелани
            music Hidden_Agenda
            img 15487
            with diss
            victoria "Подружка хочет сказать, что у нее нет времени на меня?"
            img 15466
            with fade
            melanie "..."
            img 15487
            with diss
            victoria "Хорошая подружка отменила бы все свои планы."
            victoria "Иначе она может поссориться со мной."
            music Master_Disorder
            victoria "И тогда о ее маленькой тайне узнает один наш общий друг..."
            img 15489
            with fade
            melanie "..."
            img 15490
            with diss
            victoria "Подружка же не хочет со мной ссориться?"
            melanie_t "Чертова интриганка."
            pass
    # Мелани равнодушно
    music ZigZag
    img 15491
    with fade
    melanie "Я хорошая подружка и буду ждать тебя сегодня в гости."
    # Виктория довольно улыбается
    music Groove2_85
    img 15492
    with diss
    victoria "Я очень расстроюсь, если вторая наша подружка не придет сегодня."
    victoria "Я тогда подумаю, что она не соскучилась по мне."
    victoria "Как ты думаешь, ведь вторая подружка не захочет меня расстраивать?"
    # Мелани с покерфейсом
    music ZigZag
    img 15493
    with fade
    melanie "..."
    melanie "Я уверена, что она с радостью с тобой встретится."
    # Виктория хихикает
    sound snd_woman_laugh3
    img 15494
    with diss
    victoria "Не могу дождаться нашей встречи!"
    # Мелани бросает взгляд на дверь Дика, Виктория это видит и хмурит брови
    img 15495
    with fade
    w
    music Groove2_85
    img 15496
    with diss
    victoria "Ты можешь идти, подружка."
    victoria "Я понимаю, что ты с радостью повторила бы нашу встречу в этом кабинете..."
    victoria "Поэтому ты туда так смотришь. Но не расстраивайся. Мы увидимся сегодня вечером."
    # молча смотрят друг на друга
    music Master_Disorder
    img 15497
    with fade
    w
    img 15464
    with diss
    victoria "До встречи, подружка."
    victoria "Я принесу тебе подарок сегодня."
    victoria "И не только тебе..."
    img 15466
    with fade
    melanie "..."
    # Мелани бросает на нее непроницаемый взгляд, разворачивается и уходит
    # в заданиях появляется "Вернуться в студию и поговорить с Миссис Бакфетт"
#    $ log1 = t_("Вернуться в студию и поговорить с Миссис Бакфетт")
    return

label gallery_15500:
    # Мелани дома одна, как обычно стоит перед зеркалом
    music stop
    img black_screen
    with diss
    pause 2.0
    music ZigZag
    img 15498
    with fadelong
    w
#    melanie_t "Скоро придет эта сучка Виктория. Надо быть с ней осторожнее."
#    melanie_t "Она не должна догадаться, что я ищу способ, как поставить ее на место."
    # Мелани смотрит на часы
    img 15499
    with diss
    melanie_t "Миссис Бакфетт уже должна придти. Надеюсь, она не проигнорирует эту встречу..."
    melanie_t "Интересно, она поняла, о каком друге я ей говорила?"
    sound snd_door_knock
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Master_Disorder
    # стук в дверь
    # Мелани подходит к двери, открывает
    # за ней стоит Моника в наряде шлюхи
    # Моника напряжена, заходит в квартиру, оглядывается
    img 15500
    with fadelong
    m "Мелани?"
    img 15501
    with diss
    melanie "Да, Миссис Бакфетт?"
    img 15502
    with fade
    m "А когда должен придти наш общий друг?"
    # Мелани безэмоционально отвечает
    music ZigZag
    img 15503
    with diss
    melanie "С минуты на минуту, Миссис Бакфетт."
    music Power_Bots_Loop
    img 15504
    with fade
    m "!!!"
    # предлагает ей присесть на диван, на столике перед ним стоит три бокала с вином
    music ZigZag
    img 15505
    with diss
    melanie "Присаживайтесь, Миссис Бакфетт."
    melanie "Не переживайте так. Сделайте глоток вина."

    # Моника смотрит на эти три бокала
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Master_Disorder
    img 15506
    with fadelong
    mt "Если бы случилось что-то страшное... То Маркус не приглашал бы меня выпить вина у Мелани дома..."
    mt "Он тогда, наверняка, послал бы полицейских за мной."
    mt "Хотя... Он же не знает, где я живу."
    img 15507
    with fade
    mt "..."
    mt "Значит, Маркус выбрал квартиру Мелани, чтобы заманить меня сюда!"
    mt "А потом он меня схватит и снова отведет в свой жуткий кабинет!!!"  # если была сцена в тюрьме с анальной пробкой
    music Power_Bots_Loop
    img 15508
    with diss
    mt "А у меня нет с собой анальной пробки!" # если была сцена в тюрьме с анальной пробкой
    mt "Он накажет меня за это!" # если была сцена в тюрьме с анальной пробкой
    # стук в дверь, Моника в ужасе смотрит на Мелани
    #sound стук в дверь
    sound snd_door_knock
    img 15509
    with diss
    mt "!!!"
    # Мелани смотрит на Монику, она абсолютно спокойна
    # Мелани встает, подходит к двери
    # Мелани открывает дверь, заходит Виктория с сумочкой в руках
    # смотрит на Мелани, потом поворачивается и видит Монику, недобро ухмыляется
    # Моника сидит на диване спиной ко входу и продолжает напряженно смотреть на бокалы, заметно, что она нервничает
    # Виктория подходит к дивану, Моника поворачивает голову и видит, что пришел не Маркус, а Виктория
    # Моника в шоке, вскакивает с дивана, смотрит на Викторию

    img 15510
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Groove2_85
    img 15511
    with fadelong
    w
    img 15512
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Power_Bots_Loop
    img 15513
    with hpunch
    sound plastinka1b
    w
    sound Jump1
    img 15514
    with diss
    w
    img 15515
    with fade
    mt "ВИКТОРИЯ?!"
    mt "Какого черта?!"
    mt "!!!"
    # потом на Мелани
    music Master_Disorder
    img 15516
    with diss
    mt "Как ОНА оказалась у Мелани дома???"
    mt "???"
    # Моника смотрит Мелани
    music stop
    scene black_screen
    with Dissolve(1)
    # появляется затемнение экрана "Ранее в этот день..."
    return
