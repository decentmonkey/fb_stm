default monicaShlut1PhillipThreesome1 = False  # Моника делала куни шлюхе № 1 по приказу Филиппа
default monicaShlut1PhillipThreesome2 = False  # Моника согласилась на ass to mouth
default monicaPhillipThreesome1_cum_zone = 0

#call ep212_dialogues4_philip_threesome_1() from _rcall_ep212_dialogues4_philip_threesome_1_1 # гостиница у Филиппа дома, секс втроем
#call ep212_dialogues4_philip_threesome_2() from _rcall_ep212_dialogues4_philip_threesome_2_1 # Филипп оплачивает работу шлюхе номер 1
#call ep212_dialogues4_philip_threesome_3() from _rcall_ep212_dialogues4_philip_threesome_3_1 # разговор со шлюхой номер 1 на улице


# если у Филиппа шлюха номер 1 и Моника оказалась на улице
# при выборе пункта 'Мне нужны эти деньги' в диалоге со шлюхой номер 1 (ep210_dialogues2_escort_start_Phillip_13)
# повторяется их диалог, где шлюха номер 1 обещает ей заплатить 50 баксов за минет Филиппу (ep211_dialogues7_Phillip_home_1)

# Моника зашла в гостиную Филиппа со шлюхой номер 1, согласившись помочь ей удовлетворить его
# возникает меню ep211_dialogues7_Phillip_home_2, где пункт "Групповой секс" доступен

# если выбран пункт "Групповой секс"
label ep212_dialogues4_philip_threesome_1:
    call check_skip_scene("ep211_dialogues7_Phillip_home_2") from _rcall_check_skip_scene_3
    if _return == True:
        return True
    # Филипп сидит на диване перед телеком, Моника и шлюха стоят в гостиной возле двери
    # шлюха номер 1 поворачивается к Монике и на ухо говорит
    music Groove2_85
    img 17145
    with fadelong
    w
    img 17146
    with fade
    whore_number_1 "Слушай, у меня появилась идея..."
    whore_number_1 "Как ты смотришь на то, чтобы заработать побольше?"
    whore_number_1 "Например, баксов 200?"
    # Моника смотрит на нее с подозрением
    img 17147
    with diss
    m "200 долларов?"
    m "???"
    m "Почему ты решила заплатить в два раза больше?"
    m "Что еще за идея?"
    img 17148
    with fade
    whore_number_1 "Все просто."
    whore_number_1 "Я тебе плачу 200 баксов, но тогда одним минетом ты не отделаешься..."
    m "Ты имеешь ввиду, заняться сексом? Всем вместе?"
    img 17149
    with diss
    whore_number_1 "Ага." # довольная своей идеей
    whore_number_1 "Какая тебе разница, ты ведь уже занималась этим с ним."
    whore_number_1 "Что ты строишь из себя какую-то леди?"
    music Pyro_Flow
    img 17150
    with fade
    mt "Дъявол!"
    mt "Получается, если я соглашусь заняться сексом, то заработаю больше денег."
    mt "Но мне противно об этом даже думать!"
    mt "Я Моника Бакфетт, а не какая-то проститука, которая готова на все ради денег!!!"
    mt "!!!"
    music Groove2_85
    img 17151
    with diss
    mt "С другой стороны, об этом ведь никто не узнает..."
    mt "А мне нужны деньги."
    mt "..."
    mt "В прошлый раз мерзавец Филипп заплатил этой вульгарной девке $ 400..."
    img 17152
    with fade
    mt "В этот раз она готова отдать мне половину своего заработка..."
    mt "Я могу заработать $ 200, либо отказаться и остаться вообще сегодня без заработка."
    whore_number_1 "Ну? Чего ты тормозишь?"
    whore_number_1 "Ты согласна на 200 баксов?"

    # Моника нерешительно
    menu:
        "Об этом точно никто не узнает?":
            pass
    img 17153
    with diss
    mt "Черт! Что же мне делать?"
    img 17154
    with fade
    m "Об этом точно никто не узнает?!"
    img 17155
    with diss
    whore_number_1 "Да точно-точно. Сколько уже можно спрашивать об этом..."
    whore_number_1 "Пошли!"
    # Филипп со скучающим видом обращается к шлюхе номер 1
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 17077
    with fadelong
    philip "Субботняя шлюха номер 1, ты думаешь я плачу тебе деньги за то..."
    philip "Что я должен смотреть, как вы там шепчетесь?!"
    philip "Я долго буду ждать, когда ты начнешь работать?"
    philip "И почему субботняя шлюха номер 2 опять сюда пришла?"
    philip "Шлюха номер 1 опять решила устроить мне сюрприз?"
    img 17157
    with fade
    whore_number_1 "Да. Я уверена, что тебе понравится..." # игриво
    # Филипп со скучающим видом
    img 17156
    with diss
    philip "Ну ладно, давай..."
    philip "Что на этот раз?"
    # шлюха номер 1 снимает с себя футболку, проводит по своей груди руками и улыбается игриво Филиппу
    # потом смотрит на Монику и подходит к ней
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music2 Loved_Up
    img 17158
    with fade
    w
    img 17159
    with diss
    w
    img 17160
    with fade
    w
    img 17161
    with diss
    mt "Что эта никчемная шлюха задумала?"
    # та трогает Монику за грудь, а Моника на нее зло смотрит
    img 17162
    with fade
    w
    img 17163
    with diss
    mt "Какого черта я вообще согласилась на это?!"
    mt "С какой-то там шлюхой?!"
    mt "?!?!?!"
    # шлюха номер 1 снимает платье с Моники и трогает ее при этом
    # потом шлюха номер 1 запускает руку между ног Моники и трогает ее киску
    # Моника возмущенно смотрит на нее, но молчит
    img 17165
    with fade
    w
    img 17164
    with diss
    sound snd_fabric1
    w
    img 17166
    with diss
    w
    music2 Loved_Up
    img 17167
    with fade
    w
    img 17168
    with diss


    w
    img 17169
    with diss
    w
    img 17170
    with diss
    mt "!!!"
    mt "Она не просто шлюха, она еще и лесбиянка! Фи!"
    mt "Ей действительно все это нравится?!"
    mt "Как же все это омерзительно!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Petting1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Petting1_1 = Movie(play="video/v_Monica_WhoreN1_Petting1_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Petting1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Моника стоит голая, Филипп расстегивает брюки и начинает подрачивать свой член
    # шлюха номер 1 убирает руку от киски Моники и говорит ей
    img 17171
    with fade
    w
    img 17172
    with diss
    whore_number_1 "А теперь твоя очередь сделать мне приятное..."
    # Моника смотрит на нее непонимающе
    music2 Groove2_85
    img 17173
    with fade
    m "Я? Тебе?"
    m "Зачем?"
    img 17174
    with diss
    whore_number_1 "Филиппу это понравится."
    whore_number_1 "Посмотри на его член. Его это возбуждает."
    m "..."
    menu:
        "Раздеть шлюху номер 1.":
            pass
    music2 Loved_Up
    img 17175
    with fade
    w
    img 17176
    with diss
    mt "Черт!"
    mt "Не могу поверить, что я делаю это..."
    # Моника трогает грудь шлюхи № 1, потом снимает с нее брюки, сидя на корточках перед ней
    # та показывает на свою киску
    img 17177
    with diss
    w
    img 17178
    with fade
    w
    sound snd_fabric1
    img 17179
    with diss
    w
    img 17180
    with fade
    whore_number_1 "Теперь поиграй с моей киской своим язычком."
    music2 Power_Bots_Loop
    img 17181
    with hpunch
    mt "?!?!?!"
    # Моника возмущенно
    music2 Groove2_85
    img 17182
    with fade
    m "Нет, мы так не договаривались."
    m "Я не буду этого делать!"
    m "!!!"
    img 17183
    with diss
    philip "Шлюха номер 2, молчать!"
    # обе поворачиваются и смотрят на него
    philip "Шлюха номер 2 сейчас же перестанет спорить и полижет шлюху номер 1 между ног."
    philip "Я хочу посмотреть на это..."
    img 17184
    with diss
    mt "Вот козел!!!"
    mt "!!!"
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            music2 stop
            img black_screen
            with diss
            pause 1.5
            music Groove2_85
            img 17185
            with fade
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 17186
            with diss
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            img 16418
            with fade
            sound highheels_short_walk
            return False
        "Сделать, как требует Филипп.":
            $ monicaShlut1PhillipThreesome1 = True # Моника делала куни шлюхе № 1 по приказу Филиппа
            pass
    # Моника смотрит на киску шлюхи номер 1 в нерешительности
    music2 Groove2_85
    img 17194
    with fade
    mt "Долбанные извращенцы!"
    mt "Ненавижу их всех!"
    mt "!!!"
    # Моника начинает лизать киску
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up
    img 17187
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Licking1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Licking1_1 = Movie(play="video/v_Monica_WhoreN1_Licking1_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Licking1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17188
    with fade
    whore_number_1 "Ммммм..."
    img 17189
    with diss
    whore_number_1 "Как приятно..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Licking1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Licking1_2 = Movie(play="video/v_Monica_WhoreN1_Licking1_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Licking1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17191
    with diss
    whore_number_1 "А у тебя хорошо получается, шлюха номер 2..."

    img 17190
    with fade
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_WhoreN1_Licking1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Licking1_3 = Movie(play="video/v_Monica_WhoreN1_Licking1_3.mkv", fps=30)
    show videov_Monica_WhoreN1_Licking1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17192
    with fade
    whore_number_1 "Чувствуется, что у тебя уже есть опыт с кисками..."
    whore_number_1 "Ммммм..."
    # немного позже Филипп прерывает их
    music2 Groove2_85
    img 17193
    with diss
    philip "Достаточно!"
    philip "Сейчас обе мои шлюхи подойдут ко мне."
    # они подходят, Филипп уже снял одежду (или только брюки и расстегнул рубашку)
    sound highheels_short_walk
    img 17195
    with fade
    whore_number_1 "Тебе нравится смотреть на нас?"
    philip "Да, еще больше мне понравится, если ты сейчас сядешь на меня, шлюха номер 1..."
    # шлюха номер 1 залезает на Филиппа и садится на его член своей киской
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up
    img 17196
    with fadelong
    w
    img 17197
    with fade
    philip "Нет, не так."
    philip "Сегодня я хочу трахнуть тебя в твою упругую задницу, шлюха номер 1."
    # та делает так, как говорит Филипп и насаживается на его член попой
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up
    sound chpok6
    img 17198
    with vpunch
    philip "Дааа. Вот тааак."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex1_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex1_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex1_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex1_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex1_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex1_3.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    img 17199
    with fade
    philip "А шлюха номер 2 сядет рядом с нами и будет держать лицо около моего члена."
    # Моника непонимающе смотрит на него
    music2 Groove2_85
    img 17200
    with diss
    mt "???"
    mt "Что за бред?!"
    mt "Что этот извращенец хочет сделать?!"
    img 17201
    with diss
    philip "Делай, что тебе говорят!"
    # Моника садится рядом так, что ее лицо находится рядом с их причиндалами
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up
    img 17202
    with fadelong
    whore_number_1 "Ооооо, как же хорошоооо!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex2_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex2_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17203
    with fade
    whore_number_1 "О, Филипп, я обожаю когда ты во мне!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex2_2= Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    if game.extra == True:
        # немного позже шлюха 1 привстает и Филипп говорит Монике
        music2 stop
        img black_screen
        with diss
        pause 1.5
        scene black
        sound v_Monica_WhoreN1_Philip_Sex_3_1
        image videov_Monica_WhoreN1_Philip_Sex_3_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_3_1.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_WhoreN1_Philip_Sex_3_1_end.jpg")
        show videov_Monica_WhoreN1_Philip_Sex_3_1
        pause 2.5
        wclean
        sound hlup25
        music2 Groove2_85
        img 17207
        with hpunch
        philip "Открывай свой рот, шлюха номер 2."
        philip "Приглашай мой член войти в него."
        # Моника парится и с отвращением смотрит на его член, который он только что вытащил из попы шлюхи номер 1
#        music2 Groove2_85
        img 17208
        with diss
        mt "Что?!"
        mt "О, нет!!!"
        mt "Фууу!!!"
        mt "Какая мерзость!!!"
        img 17209
        with diss
        philip "Ну?!"
        img 17254
        with fade
        w
        # Моника с отвращением на лице
        img 17210
        with diss
        m "..."
        $ menu_corruption = [0, philipThreesomeCorruptionRequired2]
        menu:
            "Убежать!":
                # Моника смотрит с отвращением
                music2 stop
                img black_screen
                with diss
                pause 1.5
                music Pyro_Flow
                img 17211
                with fade
                mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
                mt "Я не могу пойти на это!"
                music Groove2_85
                img 17212
                with diss
                m "Нет. Я..."
                m "Я не буду этого делать!"
                m "Я не могу!"
                m "!!!"
                # Моника уходит
                img 16418
                with fade
                sound highheels_short_walk
                w
                return False
            "Сделать, как требует Филипп.":
                $ monicaShlut1PhillipThreesome2 = True # Моника согласилась на ass to mouth
                pass
        # Моника открывает рот и Филипп засовывает туда свой член
        music2 stop
        img black_screen
        with diss
        pause 1.5
        music2 Loved_Up
        img 17213
        sound hlup21
        with hpunch
        w
        img 17214
        with diss
        philip "Соси, шлюха номер 2!"
        # Моника делает несколько движений

        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_4_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex_4_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_4_1.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex_4_1
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        $ renpy.music.set_volume(1.0, 0.5, channel="music")

        img 17215
        with fade
        philip "Дааа..."
        img 17216
        with diss
        w
        img 17217
        with diss
        w

        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_4_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex_4_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_4_2.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex_4_2
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        $ renpy.music.set_volume(1.0, 0.5, channel="music")

        img 17218
        with fade
        philip "Хорошо, хватит."
        philip "Шлюха номер 2, верни мой член на место!"

        # после этого он снова входит в попу шлюхи номер 1
        # это повторяется несколько раз
        music2 stop
        img black_screen
        with diss
        pause 1.5

        scene black
        sound v_Monica_WhoreN1_Philip_Sex_5_1
        image videov_Monica_WhoreN1_Philip_Sex_5_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_5_1.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_WhoreN1_Philip_Sex_5_1_end.jpg")
        show videov_Monica_WhoreN1_Philip_Sex_5_1
        pause 3.0
        sound hlup25
        pause 0.5
        with hpunch
        music2 Loved_Up2
        wclean
        img 17219
        with diss
        w
#        img 17427
#        with diss
#        w

        img 17204
        with diss
        whore_number_1 "Давай, еще!"

        ######### цикл2
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex2_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_3.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex2_3
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")

        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex2_4 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_4.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex2_4
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        $ renpy.music.set_volume(1.0, 0.5, channel="music")

        music2 stop
        img black_screen
        with diss
        pause 1.5
        scene black
        sound v_Monica_WhoreN1_Philip_Sex_3_1
        image videov_Monica_WhoreN1_Philip_Sex_3_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_3_2.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_WhoreN1_Philip_Sex_3_2_end.jpg")
        show videov_Monica_WhoreN1_Philip_Sex_3_2
        pause 2.5
        sound hlup25
        music2 Loved_Up2
        with hpunch
        philip "Соси, шлюха номер 2!"
        philip "Соси его!"
        w

        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_4_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex_4_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_4_3.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex_4_3
        with fade
        wclean
        philip "Вставляй его назад, шлюха!"
        philip "Назад в ее задницу!"
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        $ renpy.music.set_volume(1.0, 0.5, channel="music")

        music2 stop
        img black_screen
        with diss
        pause 0.5
#        music2 Loved_Up2

        scene black
        sound v_Monica_WhoreN1_Philip_Sex_5_1
        image videov_Monica_WhoreN1_Philip_Sex_5_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_5_2.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_WhoreN1_Philip_Sex_5_2_end.jpg")
        show videov_Monica_WhoreN1_Philip_Sex_5_2
        pause 3.0
        sound hlup25
        pause 0.5
        with hpunch
        music2 Loved_Up2
        wclean

        ############ Цикл 3

        img 17205
        with fade
        whore_number_1 "Трахай меня!!!"

        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex2_5 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_5.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex2_5
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")


        scene black
        sound v_Monica_WhoreN1_Philip_Sex_3_1
        image videov_Monica_WhoreN1_Philip_Sex_3_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_3_3.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_WhoreN1_Philip_Sex_3_3_end.jpg")
        show videov_Monica_WhoreN1_Philip_Sex_3_3
        pause 2.5
        sound hlup25
        with hpunch
        philip "Давай, тупая шлюха, лижи его!"
        philip "Не жди команды!"
        wclean

        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_4_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex_4_4 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_4_4.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex_4_4
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
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_4_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex_4_5 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_4_5.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex_4_5
        with fade
        wclean
        philip "Вставляй его, шлюха! Другая шлюха тоже хочет мой член!"
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        $ renpy.music.set_volume(1.0, 0.5, channel="music")


        music2 stop
        img black_screen
        with diss
        pause 0.5

        scene black
        sound v_Monica_WhoreN1_Philip_Sex_5_1
        image videov_Monica_WhoreN1_Philip_Sex_5_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_5_3.mkv", fps=30, loop=False, image="/images/Slides/v_Monica_WhoreN1_Philip_Sex_5_3_end.jpg")
        show videov_Monica_WhoreN1_Philip_Sex_5_3
        pause 3.0
        sound hlup25
        pause 0.5
        with hpunch
        music2 Loved_Up2
        wclean


        img 17206
        with diss
        whore_number_1 "Ещееее!!!"


        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.3, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex1_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex1_3.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex1_3
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
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex2_6 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_6.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex2_6
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
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_WhoreN1_Philip_Sex2_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex2_2.mkv", fps=30)
        show videov_Monica_WhoreN1_Philip_Sex2_2
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        $ renpy.music.set_volume(1.0, 0.5, channel="music")

        music2 stop
        img black_screen
        with diss
        pause 1.5
        music Groove2_85
        img 17220
        with fade
        philip "Мне нравится, что мои субботние шлюхи стараются для меня..."
        img 17221
        with diss
        philip "Сегодня субботние шлюхи хорошо работают..."
        # Моника смотрит на все происходящее с отвращением
#        music Groove2_85
        img 17222
        with fade
        mt "Мерзкий грязный извращенец!!!"
        mt "!!!"
    img 17223
    with diss
    philip "А теперь очередь шлюхи номер 2 быть оттраханной!"
    # он выходит из шлюхи номер 1, они оба встают и смотрят на Монику
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music2 Groove2_85
    img 17224
    with fade
    philip "Ложись, подставляй мне свое отверстие..."
    philip "Покажи, как ты хочешь почувствовать мой член внутри себя..."
    m "..."
    menu:
        "Лечь на диван и раздвинуть ноги.":
            pass
    img 17200
    with diss
    mt "!!!"
    mt "Не могу поверить, что это происходит со мной..."
    # Моника ложится на спину и раздвигает ноги
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music2 Groove2_85
    img 17225
    with fade
    philip "Шлюха номер 1, проверь, готова ли шлюха номер 2 принять мой член?"
    philip "Ее отверстие достаточно влажное?"
    # шлюха номер 1 подходит к Монике и вводит в ее киску пальцы
    img 17228
    with diss
    w
    img 17229
    with diss
    whore_number_1 "Ее киска недостаточно влажная, но я сейчас подготовлю ее для тебя."
    # она водит пальцами туда-сюда в киске Монике, Филипп стоит смотрит на это и трется членом о попу шлюхи номер 1
    # та поглядывает на него, улыбается игриво
    music2 Loved_Up
    img 17230
    with fade
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.8, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_6_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex_6_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex_6_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex_6_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17231
    with diss
    w

    img 17255
    with diss
    w
    img 17232
    with fade
    w
    img 17233
    with diss
    w


    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.8, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex_6_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex_6_2= Movie(play="video/v_Monica_WhoreN1_Philip_Sex_6_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex_6_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17226
    with fade
    whore_number_1 "Теперь она готова принять твой член."
    whore_number_1 "Что ты хочешь, чтобы я еще сделала?"
    img 17227
    with diss
    philip "Я хочу, чтобы ты села на лицо шлюхи номер 2."
    # шлюха номер 1 садится на лицо Моники
    # Филипп раздвигает ноги Моники шире и входит в нее
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up2
    img 17234
    with fadelong
    philip "Ммммм..."
    philip "Шлюха номер 1 хорошо подготовила для меня это отверстие."
    sound chpok6
    img 17235
    with hpunch
    philip "Шлюха номер 1 молодец, она старается для меня."
    # шлюха номер 1 елозит у нее по лицу своей киской, трогает свою грудь, игриво смотрит на Филиппа


    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex7_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex7_4 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex7_4.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex7_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17236
    with fade
    whore_number_1 "О, как прикольно!!!"
    whore_number_1 "Даааа...."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex7_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex7_1 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex7_1.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex7_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17237
    with diss
    whore_number_1 "Ооооо... Какой каааайф!"
    img 17238
    with fade
    mt "Скорее бы закончился этот кошмар!"
    mt "Как же это все грязно и мерзко!"
    img 17239
    with diss
    mt "!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex7_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex7_2 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex7_2.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex7_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17240
    with fade
    mt "Моника, никогда бы не подумала, что ты опустишься до подобного!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex7_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex7_3 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex7_3.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex7_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17241
    with diss
    mt "И ради чего?! Из-за 200 долларов?!"
    img 17242
    with fade
    mt "!!!"
    img 17243
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_WhoreN1_Philip_Sex7_1.ogg"
    scene black
    image videov_Monica_WhoreN1_Philip_Sex7_5 = Movie(play="video/v_Monica_WhoreN1_Philip_Sex7_5.mkv", fps=30)
    show videov_Monica_WhoreN1_Philip_Sex7_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Филипп кончает
    menu:
        "Кончить внутрь Моники.":
            img 17244
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            philip "Аааа..."
            philip "Аааааааа..."

            img 17245
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            philip "ААААААА!!!"
            $ monicaPhillipThreesome1_cum_zone = 1
            pass
        "Кончить на киску Моники.":
            img 17244
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            philip "Аааа..."
            philip "Аааааааа..."

            img 17247
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            philip "ААААААА!!!"
            img 17246
            with diss
            w
            # Филипп отстраняется от Моники и смотрит на сперму на ее киске
            music2 stop
            img black_screen
            with diss
            pause 1.5
            music2 Loved_Up
            img 17252
            with fadelong
            philip "А теперь я хочу, чтобы шлюха номер 1 слизала это все со шлюхи номер 2."
            # та слезает с лица Моники и выполняет приказ Филиппа, с довольным видом
            img 17253
            with fadelong
            whore_number_1 "Ммммм..."
            $ monicaPhillipThreesome1_cum_zone = 2
            pass
        "Кончить на грудь Моники.":
            img 17244
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            philip "Аааа..."
            philip "Аааааааа..."

            img 17247
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            philip "ААААААА!!!"
            img 17248
            with diss
            w
            # Филипп отстраняется от Моники и смотрит на сперму на ее груди
            music2 stop
            img black_screen
            with diss
            pause 1.5
            music2 Loved_Up
            img 17249
            with fadelong
            philip "А теперь я хочу, чтобы шлюха номер 1 слизала это все со шлюхи номер 2."
            # та слезает с лица Моники и выполняет приказ Филиппа, с довольным видом
            img 17250
            with fadelong
            whore_number_1 "Ммммм..."
            $ monicaPhillipThreesome1_cum_zone = 3
            pass
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 17251
    with fade
    mt "Наконец-то, этот кошмар закончился!"
    mt "!!!"
    return

# после тройничка
label ep212_dialogues4_philip_threesome_2:
    # смена кадра, они уже в одежде
    # в руках у Филиппа деньги
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 17136
    with fadelong
    philip "Шлюха номер 1 снова проявила инициативу и ее идея мне понравилась."
    philip "Я, как и в прошлый раз, доволен ее работой."
    philip "Молодец, шлюха номер 1. Хорошо придумала..."
    philip "Вот, держи 700 долларов."
    # Филипп дает деньги шлюхе номер 1, шлюха стоит довольная
    img 17138
    with fade
    mt "700?! Он дал ей 700 долларов?!"
    mt "?!?!?!"
    img 17140
    with diss
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 1 может забрать свои деньги."
    img 17142
    with diss
    philip "А субботняя шлюха номер 2 недостаточно старалась..."
    philip "Ей учиться надо у шлюхи номер 1, как делать мне приятно."
    mt "!!!"
    img 17139
    with fade
    philip "Тем более, сегодня не ее очередь получать деньги."
    philip "Поэтому она сегодня ничего не заработала."
    music Pyro_Flow
    img 17138
    with diss
    mt "!!!"
    menu:
        "Почему я ничего не заработала?!":
            img 17141
            with fade
            call bitch(5, "philip_threesome1") from _rcall_bitch_4
            m "Филипп, я делала все, что ты мне говорил!"
            m "Почему я не заработала денег?!"
            m "?!?!?!"
            # смотрит на нее
            music Groove2_85
            img 17144
            with diss
            philip "???"
            philip "Моей субботней шлюхе номер 2 нужны деньги?"
            philip "Приходи через неделю."
            # отворачивается
            music Pyro_Flow
            img 16386
            with fade
            mt "Вот мерзавец!!!"
            mt "Жадный ублюдок!!!"
            return True
        "Уйти.":
            pass
    music Groove2_85
    img 17144
    with fade
    philip "Можете идти."
    call bitch(-5, "philip_threesome1") from _rcall_bitch_5
    music Pyro_Flow
    img 16386
    with diss
    mt "Сволочь!"
    mt "!!!"
    return True

# на улице после сцены у Филиппа (диалог такой же, только сумма денег разная)
label ep212_dialogues4_philip_threesome_3:
    # Моника разговаривает с субботней шлюхой номер 1
    music Groove2_85
    img 17065
    with fadelong
    m "Это было мерзко!"
    m "!!!"
    img 17072
    with fade
    whore_number_1 "Зато мы заработали денег."
    $ add_money(200.0)
    whore_number_1 "Вот твои 200 баксов, как и договаривались..."
    # дает ей деньги
    music Pyro_Flow
    img 23172
    with diss
    m "Это несправедливо! Он дал тебе 700 долларов!!!"
    music Groove2_85
    img 23173
    with fade
    whore_number_1 "Ты сама согласилась сделать это за 200 баксов!"
    whore_number_1 "Тебя никто не заставлял!"
    music Pyro_Flow
    img 17068
    with diss
    mt "Сучка!!!"
    mt "!!!"
    music Groove2_85
    img 23171
    with fade
    whore_number_1 "Все, мне пора."
    whore_number_1 "До встречи."
    # шлюха 1 уходит
    return

# мысли Моники после группового секса - ep211_dialogues7_Phillip_home_5
