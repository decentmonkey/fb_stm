# blowjob Man
label cit3_dialog_1:
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
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit3_dialog_1")
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
    $ menu_corruption = [90]
    menu:
        "Встать ближе.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False

    $ add_corruption(1, "cit3_dialog_1b")
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
    return True

label cit3_dialog_2:
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

    $ menu_corruption = [100]
    menu:
        "Да, Мистер. Посетители могут прикасаться к манекену...":
            pass
        "Нет, Мистер. Это исключено!":
            music Power_Bots_Loop
            img 11159
            with fade
            m "Нет, Мистер. Это исключено!"
            $ monicaSellingDressRefuseLastDay = day
            return False

    $ add_corruption(3, "cit3_dialog_2")
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
    # corruption +5 req 110
    $ menu_corruption = [110]
    menu:
        "Да, Мистер. Посетители могут прикасаться к манекену...":
            pass
        "Нет, Мистер. Это исключено!":
            m "Нет, Мистер. Это исключено!"
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(5, "cit3_dialog_2b")
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
    return True


label cit3_dialog_3:
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

    # corruption +15 req 140

    $ menu_corruption = [140]
    menu:
        "Сделать Покупателю минет за покупку...":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 11214
            with fade
            m "Нет, знаете, я на такое не способна!"
            cit3 "Хорошо, я приду, когда найду другую детку, которая подходит под это платье!"
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(15, "cit3_dialog_3")

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
            $ monicaOffendedCit3 = True
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
            music stop
            call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_28
            img black_screen
            with Dissolve(1)
            return True
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

    $ add_corruption(30, "monica_clothing_shop_blowjob")

    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.0, 'music2')

    music stop
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_22
    img black_screen
    with Dissolve(1)

    # Моника сидит, сняв штаны
#    cit3 "Да! Я не сомневался!"
#    cit3 "Такие как ты готовы на все ради денежной выгоды!"
#    m "Дело не в выгоде. У меня... гораздо более высокие цели..."
    # сцена миньета
    # кончает
    # далее сцена с продавцом о покупке
    return True







    #
