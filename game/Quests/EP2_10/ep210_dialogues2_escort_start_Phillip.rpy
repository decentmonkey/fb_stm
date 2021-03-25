default monicaPhillipHotel1 = False  # Моника торговалась с Филиппом из-за 300 баксов
default monicaPhillipHotel2 = False  # Моника согласилась пойти с Филиппом в туалет
default monicaPhillipHotel3 = False  # Моника занималась сексом с Филиппом в туалете
default monicaPhillipHotelKick = False # Моника ударила Филиппа

default monica_philip_ask_money1 = 0

# Моника приходит в ресторан на ужин
# ресторан отеля ЛеГранд
label ep210_dialogues2_escort_start_Phillip_1:
    music stop
    img black_screen
    with diss
    pause 1.0
    # Моника заказывает еду у официантки ( ep26_dialogues4_restaurant - разговор с официанткой и заказ еды)
    # пока ждет, когда принесут ее заказ, сидит на стуле с задумчивым видом
    music Poppers_and_Prosecco
    img 22946
    with fadelong
    mt "Наконец-то моя прежняя жизнь постепенно возвращается..."
    mt "Я на верном пути."
    mt "Совсем недавно я могла себе позволить только ужасный кебаб..."
    mt "Или не менее ужасное пирожное..."
    img 22947
    with fade
    mt "А сейчас я в ресторане, на мне красивое платье..."
    mt "Я поела такой вкусный ужин..."
    mt "Скоро Моника Бакфетт вернет себе все, что у нее отняли!"
    mt "И накажет всех, кто посмел недостойно себя вести в отношении нее..."
    # приносят ужин и тут ее мысли прерывает мужской голос
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    img 22948
    with hpunch
    sound plastinka1b
    philip "Миссис Бакфетт, какая неожиданная и приятная встреча!"
    # Моника поднимает взгляд, рядом с ее столиком стоит Филипп
    music Pyro_Flow
    img 22949
    with fade
    mt "О нет! Только не этот мерзкий тип!"
    mt "Что он здесь делает?!"
    # Филипп продолжает любезно улыбаться
    music Groove2_85
    img 22950
    with diss
    sound kiss1
    philip "Добрый вечер, Миссис Бакфетт. Позвольте вашу ручку?"
    # Филипп целует ее руку и садится за ее столик. Она вопросительно смотрит на него
    img 22951
    with fade
    philip "Я впечатлен Вашей презентацией, Миссис Бакфетт."
    img 22952
    with diss
    m "Спасибо, Филипп."
    mt "Что ему от меня надо?"
    img 22953
    with fade
    philip "На этой презентации я увидел у Вас кое-что интересное, Мэм..."
    m "..."

    # если Моника делала ему минет в туалете
    if monicaMadeBlowjobToPhilip == True:
        philip "Я, конечно, не использую одну и ту же женщину дважды..."
        #
        $ notif(t_("Моника делала Филиппу минет в туалете"))
        #
        philip "Но у Вас я пробовал только ротик..."
        philip "Я решил, что неплохо было бы мне засунуть член в Ваше отверстие."
    else:
        # если Моника НЕ делала ему минет в туалете
        img 22954
        with diss
        m "Это не твое дело, Филипп! Мне без разницы, что ты там увидел..."
        img 22953
        with fade
        philip "Как что? Вашу прекрасную попу, Миссис Бакфетт!"
        philip "И я решил, что неплохо было бы мне засунуть член в Ваше отверстие."
        #

    music Power_Bots_Loop
    img 22954
    with diss
    mt "!!!"
    m "Даже не мечтай, Филипп! Ты никогда не сможешь этого сделать!"
    music Groove2_85
    img 22955
    with fade
    philip "Я всегда могу сделать это с Вами. За деньги."
    # Моника злится, говорит возмущенно
    img 22956
    with diss
    m "Ты меня считаешь проституткой?!"
    m "С чего ты взял, что меня можно купить?!"
    # Филипп, улыбаясь
    img 22957
    with fade
    philip "Я знаю это."
    philip "Я куплю Вашу киску за 300 долларов."
    music Pyro_Flow
    img 22958
    with diss
    mt "!!!"
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            m "Как ты смеешь предлагать мне подобное?"
            img 22959
            with fade
            m "Моя... Она стоит миллионы долларов!"
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 22960
            with diss
            mt "Мерзкий самовлюбленный извращенец!"
            m "Уходи отсюда и не порти мне аппетит!"
            mt "Сволочь!"
            music Groove2_85
            img 22961
            with fade
            philip "Вы уверены, Миссис Бакфетт?"
            img 22962
            with diss
            m "!!!"
            img 22963
            with fade
            philip "Хорошо, сейчас я уйду..."
            philip "Но в следующий раз..."
            music Pyro_Flow
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит, тот мерзко улыбается и уходит
            return False
        "А почему 300?!":
            $ monicaPhillipHotel1 = True # Моника торговалась с Филиппом из-за 300 баксов
            pass

    # Моника возмущенно
    img 22964
    with fade
    m "А почему 300?!"
    music Groove2_85
    img 22965
    with diss
    philip "Ну вот видите, Вы уже торгуетесь..."
    philip "Вы обычная шлюха, которую я сейчас куплю."
    music Pyro_Flow
    img 22966
    with fade
    m "Как ты смеешь такое обсуждать со мной?!"
    m "Я не шлюха! Меня нельзя купить!!!"
    music Groove2_85
    img 22967
    with diss
    philip "..." # улыбается
    img 22968
    with fade
    m "И вообще, почему 300?!"
    m "В прошлый раз ты предлагал 500 долларов и за меньшее!"
    m "Ты считаешь, что моя... Неважно... Что она стоит так мало?!"
    img 22969
    with diss
    philip "Ваши акции дешевеют, Миссис Бакфетт..."
    music Power_Bots_Loop
    img 22970
    with hpunch
    m "???"
    music Groove2_85
    img 22971
    with fade
    philip "Ваша киска сейчас стоит не более 100 долларов..."
    philip "И я делаю Вам щедрое предложение, предлагая 300."
    # Моника смотрит на него зло
    img 22972
    with diss
    mt "Черт!"
    mt "Мне нужны деньги..."
    mt "Но не таким же способом!"
    mt "!!!"
    mt "Какая же сволочь этот Филипп!"
    img 22973
    with fade
    m "..."
    m "Ты хочешь сделать это и рассказать всем?"
    img 22974
    with diss
    philip "Это не в моих интересах..."
    philip "Я не хочу, чтобы все знали, что я покупаю женщину так дешево."
    music Power_Bots_Loop
    img 22975
    with fade
    mt "!!!"
    music Groove2_85
    img 22976
    with diss
    philip "Миссис Бакфетт, вы закончили свою трапезу?"
    philip "Мы можем идти."
    img 22977
    with diss
    mt "Как он смеет такое мне предлагать?!"
    mt "С другой стороны, мне нужны деньги..."
    mt "Скоро я все верну и мне нельзя подрывать свою репутацию..."
    mt "А он сказал, что никому не расскажет об этом."
    mt "Что же мне делать?!"
    mt "Моника, неужели ты способна на такое пойти?!"
    mt "..."
    $ menu_corruption = [0, monicaPhilipHotelSexCorruption]
    menu:
        "Уйти!":
            # Монику бомбит
            music Pyro_Flow
            m "Как ты смеешь предлагать мне подобное?"
            img 22959
            with fade
            m "Моя... Она стоит миллионы долларов!"
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 22960
            with diss
            mt "Мерзкий самовлюбленный извращенец!"
            m "Уходи отсюда и не порти мне аппетит!"
            mt "Сволочь!"
            music Groove2_85
            img 22961
            with fade
            philip "Вы уверены, Миссис Бакфетт?"
            img 22962
            with diss
            m "!!!"
            img 22963
            with fade
            philip "Хорошо, сейчас я уйду..."
            philip "Но в следующий раз..."
            music Pyro_Flow
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит, тот мерзко улыбается и уходит
            return False
        "Согласиться на предложение Филиппа.":
            $ monicaPhillipHotel2 = True # Моника согласилась пойти с Филиппом в туалет
            pass
    # Моника смотрит на него пристально
    music Groove2_85
    img 22978
    with fade
    philip "Мы можем идти."
    m "Если про это кто-то узнает - я тебя убью!"
    img 22979
    with diss
    philip "Не беспокойтесь, мой член бывал и не в таких местах..."
    philip "И при этом у меня все прекрасно."
    m "..."
    img 22980
    with fade
    m "Оплати мой счет."
    # Моника смотрит на него, тот ей улыбается в ответ
    img 22981
    with diss
    philip "Это повысит общую стоимость моих расходов, и они превысят стоимость Вашей киски."
    music Power_Bots_Loop
    m "Мерзавец!"
    m "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Poppers_and_Prosecco
    img 22982
    with fadelong
    philip "Пойдемте, Миссис Бакфетт. Думаю, что мне пора попробовать Вашу киску."
    return True

# ресторан отеля ЛеГранд, туалет
label ep210_dialogues2_escort_start_Phillip_2:
    # Моника с Филиппом стоят в туалете
    music Groove2_85
    if monicaMadeBlowjobToPhilip == True:
        # если Моника делала ему минет в туалете
        img 16086
        with fadelong
        sound highheels_short_walk
        m "Снова это жуткое место..."
        #
        $ notif(t_("Моника делала Филиппу минет в туалете"))
        #
        m "Неужели нельзя было в этот раз подобрать место получше?!"
        img 16087
        with fade
        philip "Гостиничный номер будет стоить гораздо дороже Вашей киски!"
        philip "Как Вы знаете, я умею считать деньги!"
    else:
        # если Моника НЕ делала ему минет в туалете
        img 16086
        with fadelong
        sound highheels_short_walk
        m "Куда ты меня привел, Филипп?"
        m "Это мужской туалет!"
        img 16087
        with fade
        philip "Миссис Бакфетт!"
        philip "Мне будет неудобно находиться в женском туалете!"
        philip "Ну а для Вас, полагаю, нет никакой разницы, ведь так?"
        img 16088
        with diss
        m "Я думала это будет хотя бы гостиничный номер!"
        img 16089
        with fade
        philip "Гостиничный номер будет стоить гораздо дороже Вашей киски!"
        philip "Как Вы знаете, я умею считать деньги!"
        philip "Поэтому туалет как раз подойдет для этой цели!"
        #

    # Моника зло на него смотрит
    img 16090
    with diss
    philip "Задирайте платье, Миссис Бакфетт. Покажите мне Вашу киску."
    music Pyro_Flow
    m "!!!"
    m "Что, прямо вот так?! Так быстро?!"
    music Groove2_85
    img 16091
    with fade
    philip "Да. Я это купил и это уже мое."
    img 16092
    with diss
    mt "Мерзавец!"
    m "..."
    img 16093
    with fade
    menu:
        "Уйти!":
            # Монику бомбит
            music Pyro_Flow
            img 16094
            with diss
            m "Как ты смеешь так со мной обращаться?!"
            m "Моя... Она стоит миллионы долларов!"
            img 16095
            with fade
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 16096
            with diss
            mt "Мерзкий самовлюбленный извращенец!"
            mt "Сволочь!"
            music Groove2_85
            img 16097
            with fade
            philip "Вы уверены, Миссис Бакфетт?"
            img 16098
            with diss
            m "!!!"
            philip "Хорошо..."
            philip "Но в следующий раз..."
            music Pyro_Flow
            img 16099
            with fade
            sound highheels_short_walk
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return 1
        "Ударить мерзавца и уйти! (прерывание квеста)":
            # Монику бомбит, она подходит к нему ближе и орет на него
            music Power_Bots_Loop
            img 16094
            with diss
            m "Как ты смеешь так со мной обращаться?!"
            m "Мерзкий самовлюбленный извращенец!"
            m "!!!"
            # бьет между ног коленом
            sound anger2
            img 16100
            w
            sound snd_kick_fred1
            img 16101
            with diss
            call bitch(20, "kickPhilipHotel") from _rcall_bitch
            m "Сволочь!"
            m "!!!"
            sound snd_fred_argh
            img 16102
            with diss
            philip "АААААААА!!!" # падает
            philip "Сучка!!!"
            img 16103
            with fade
            m "Да пошел ты, придурок!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            $ monicaPhillipHotelKick = True # Моника ударила Филиппа
            return 2
        "Задрать платье.":
            pass
    # Моника неуверенно поворачивается к нему задом и задирает платье немного
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16104
    with fadelong
    philip "Это никуда не годится, Миссис Бакфетт..."
    philip "Я за это и цента не заплачу."
    img 16105
    with fade
    philip "Поднимай платье еще выше."
    # Моника задирает его до талии и стоит перед ним с голой попой
    music Loved_Up
    img 16106
    with diss
    sound snd_fabric1
    w
    img 16107
    with diss
    philip "А теперь предложите мне себя..."
    philip "Раздвиньте ноги и покажите мне, что там между ними."
    # Моника злится
    music Groove2_85
    img 16108
    with fade
    m "!!!"
    m "Но..."
    img 16109
    with diss
    philip "Никаких 'но'. Будете много разговаривать, ничего не заработаете."
    philip "Раздвигайте ноги!"
    mt "!!!"
    img 16110
    with diss
    menu:
        "Уйти!":
            # Монику бомбит
            music Pyro_Flow
            img 16094
            with fade
            m "Как ты смеешь так со мной обращаться?!"
            m "Моя... Она стоит миллионы долларов!"
            img 16095
            with diss
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 16096
            with diss
            mt "Мерзкий самовлюбленный извращенец!"
            mt "Сволочь!"
            music Groove2_85
            img 16097
            with fade
            philip "Вы уверены, Миссис Бакфетт?"
            img 16098
            with diss
            m "!!!"
            philip "Хорошо..."
            philip "Но в следующий раз..."
            music Pyro_Flow
            img 16099
            with fade
            sound highheels_short_walk
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return 1
        "Ударить мерзавца и уйти! (завершение квеста)":
            # Монику бомбит, она подходит к нему ближе и орет на него
            music Power_Bots_Loop
            img 16094
            with fade
            m "Как ты смеешь так со мной обращаться?!"
            m "Мерзкий самовлюбленный извращенец!"
            m "!!!"
            # бьет между ног коленом
            sound anger2
            img 16100
            w
            sound snd_kick_fred1
            img 16101
            with diss
            call bitch(20, "kickPhilipHotel") from _rcall_bitch_1
            m "Сволочь!"
            m "!!!"
            sound snd_fred_argh
            img 16102
            with diss
            philip "АААААААА!!!" # падает
            philip "Сучка!!!"
            img 16103
            with fade
            m "Да пошел ты, придурок!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            $ monicaPhillipHotelKick = True # Моника ударила Филиппа
            return 2
        "Раздвинуть ноги.":
            $ monicaPhillipHotel3 = True # Моника занималась сексом с Филиппом в туалете
            pass
    music Pyro_Flow
    # Моника нагибается и раздвигает ноги
    img 16111
    with fade
    mt "Ненавижу!!!"
    # он расстегивает ширинку и достает член
    music stop
    img black_screen
    with diss
    sound snd_zip
    pause 1.0
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16112
    with fadelong
    philip "Давно я не трахал таких 'леди' в туалете ресторана."
    m "!!!"
    # подходит к ней ближе и засовывает член в нее
    # Моника в ужасе, но не сопротивляется
    img 16113
    with fade
    mt "Я постараюсь это сейчас перетерпеть, потому что мне нужны деньги."
    mt "Но потом я ему отомщу!"
    mt "Он будет одним из первых, кого Моника Бакфетт накажет за все его мерзкие поступки!"
    # секс с Филиппом
    sound chpok6
    img 16114
    with hpunch
    w
    music stop
    music2 Loved_Up2
    img 16115
    with fade
    w
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_1 = Movie(play="video/v_Monica_Philip_Sex2_1.mkv", fps=30)
    show videov_Monica_Philip_Sex2_1
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_2 = Movie(play="video/v_Monica_Philip_Sex2_2.mkv", fps=30)
    show videov_Monica_Philip_Sex2_2
    with fade
    philip "У Вас неплохая киска, Миссис Бакфетт..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_3 = Movie(play="video/v_Monica_Philip_Sex2_3.mkv", fps=30)
    show videov_Monica_Philip_Sex2_3
    with fade
    philip "Конечно, она не стоит 300 долларов..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_4 = Movie(play="video/v_Monica_Philip_Sex2_4.mkv", fps=30)
    show videov_Monica_Philip_Sex2_4
    with fade
    philip "Но все же..."
    philip "Ммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16116
    with diss
    w
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_5 = Movie(play="video/v_Monica_Philip_Sex2_5.mkv", fps=30)
    show videov_Monica_Philip_Sex2_5
    with fade
    philip "Мне приятно Вас трахать, Миссис Бакфетт..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    if game.extra == True:
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_Philip_Sex2_6 = Movie(play="video/v_Monica_Philip_Sex2_6.mkv", fps=30)
        show videov_Monica_Philip_Sex2_6
        with fade
        philip "Думаю, это не последняя наша с Вами встреча..."
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
        scene black
        image videov_Monica_Philip_Sex2_7 = Movie(play="video/v_Monica_Philip_Sex2_7.mkv", fps=30)
        show videov_Monica_Philip_Sex2_7
        with fade
        philip "Ммммм..."
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex2_1.ogg"
    scene black
    image videov_Monica_Philip_Sex2_8 = Movie(play="video/v_Monica_Philip_Sex2_8.mkv", fps=30)
    show videov_Monica_Philip_Sex2_8
    with fade
    wclean
    stop music
    music stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    sound ahhh11
    img 16117
    with fade
    philip "Даааа..."
    # кончает
    img 16118
    with diss
    philip "АААААААА!!!"
    w
    img 16119
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 16120
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    img 16121
    with fade
    w
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    # кадр меняется, Филипп с застегнутой ширинкой, Моника с недовольным видом поправляет платье
    img 16122
    with fadelong
    philip "Неплохо, Миссис Бакфетт..."
    philip "Можете забирать свои деньги."
    # кладет деньги куда-нибудь на столик или раковины
    img 16123
    with fade
    m "Мерзавец!"
    m "!!!"
    img 16124
    with diss
    philip "Вы знаете, Миссис Бакфетт..."
    philip "Я готов сделать исключение из своего правила не использовать одну и ту же женщину дважды..."
    # протягивает ей свою визитку
    img 16125
    with fade
    m "???"
    m "Что это значит?"
    img 16126
    with diss
    philip "Это значит, что мне нужна шлюха выходного дня."
    music Pyro_Flow
    img 16127
    with fade
    m "Что за мерзкое название?"
    img 16098
    with diss
    philip "Я предлагаю Вам быть моей личной шлюхой, которая приходит ко мне по субботам..."
    m "!!!"
    music Groove2_85
    img 16128
    with fade
    philip "Это исключение, которое я делаю далеко немногим."
    philip "Будешь приходить в субботу. Остальные дни у меня расписаны."
    philip "Вообще, субботняя шлюха у меня уже есть... Но она иногда по субботам приходить не может."
    img 16091
    with diss
    philip "Поэтому Вы, Миссис Бакфетт, будете субботней шлюхой номер два... На замену."
    philip "Придете ко мне вечером в субботу. Я плачу 100 долларов за вечер."
    music Power_Bots_Loop
    img 16095
    with fade
    m "!!!"
    m "Я никогда на такое не пойду!"
    # Моника злобно смотрит на него, тот улыбается мерзкой улыбочкой
    music Groove2_85
    img 16129
    with diss
    philip "Не забудьте, Миссис Бакфетт! Вечером в субботу."
    music Power_Bots_Loop
    img 16099
    with fade
    sound highheels_short_walk
    m "Иди к черту!"
    m "!!!"
    # Моника уходит
#    $ log1 = t_("У меня появилась возможность дополнительного заработка по субботам. У Филиппа. Но смогу ли я?") # квест лог
    return 0

label ep210_dialogues2_escort_start_Phillip_3a:
    mt "Что этот мерзавец здесь делает?"
    mt "Я не собираюсь подходить к нему!"
    help "Квест вип эскорта перезапущен!"
    return
label ep210_dialogues2_escort_start_HotelStaff_3b:
    mt "Что это ничтожество здесь делает?"
    mt "Я не собираюсь подходить к нему!"
    help "Квест вип эскорта запущен снова!"
    return

# Моника, выйдя на улицу после секса с Филиппом
label ep210_dialogues2_escort_start_Phillip_3:
    # не рендерить!
    mt "Боже, какой кошмар!"
    mt "Я не верю, что я смогла решиться на такое!!!"
    mt "Моника, неужели это все происходит с тобой на самом деле?!"
    mt "... (хмык)"
    mt "Как он мог мне предложить стать его субботней шлюхой?!"
    mt "Да еще и на замену!"
    mt "Он предложил это мне, Монике Бакфетт!!!"
    mt "Этот никчемный жадный неудачник думает, что я соглашусь на подобное?!"
    mt "!!!"
    return

# Моника, выйдя на улицу, если послала Филиппа и секса не было
label ep210_dialogues2_escort_start_Phillip_4:
    # не рендерить!
    mt "Мерзкий извращенец!!!"
    mt "Никчемный неудачник!!!"
    mt "Как он посмел со мной так обращаться!!!"
    mt "Ненавижу его!"
    return

# Моника, проходя мимо ресепшна отеля, когда выходит на улицу
label ep210_dialogues2_escort_start_Phillip_5:
    music Groove2_85
    img 16367
    with fadelong
    sound highheels_short_walk
    reception "А что это за мужчина присел за ваш столик, Мэм?"
    reception "Вы уверены в том, что это был просто ужин?"
    music Pyro_Flow
    img 16368
    with fade
    m "А вы уверены, что я должны отчитываться перед каким-то администратором?"
    m "Это мое личное дело и вас это не касается!"
    sound highheels_short_walk
    img 16369
    with diss
    mt "Какая-то никчемная администраторша, а задает мне такие вопросы!"
    mt "!!!"
    # Моника гордо уходит, азиатка подозрительно смотрит ей вслед (взять арты из предыдущей сцены в отеле)
    return

# мысли Моники перед посещением квартиры Филиппа
label ep210_dialogues2_escort_start_Phillip_6:
    # не рендерить!
    mt "Я же могу послать все к черту и просто не ехать к этому мерзавцу..."
    mt "И поискать другой способ заработать деньги."
    mt "С другой стороны, я быстро смогу заработать у него."
    mt "..."
    mt "Еще он говорил, что не встречается с одной женщиной дважды... А меня пригласил к себе домой..."
    mt "..."
    mt "Возможно, он неравнодушен ко мне... В принципе, как и все мужчины..."
    mt "И под такой грубой манерой общения пытается скрыть это."
    mt "..."
    mt "А еще он богат и, возможно, можно заставить его помочь мне с деньгами."
    mt "Тогда я смогу купить себе дом..."
    mt "И послать к черту тех деревенщин, что живут сейчас в моем бывшем доме."
    mt "Хммм... Мне кажется, что мне нужно будет поехать домой к Филиппу... И попытаться найти с ним общий язык."
    return

# мысли Моники (клик на дом Филиппа) суббота
label ep210_dialogues2_escort_start_Phillip_7:
    # не рендерить!
    mt "Неужели я на такое пойду?!"
    mt "Но мне нужны эти деньги..."
    menu:
        "Зайти к Филиппу.":
            return True
        "Уйти.":
            return False
    return False

# мысли Моники (клик на дом Филиппа) не суббота
label ep210_dialogues2_escort_start_Phillip_8:
    # не рендерить!
    mt "Мне сегодня нечего там делать."
    mt "Этот мерзавец сказал приходить к нему в субботу вечером."
    return

# мысли Моники (клик на дом Филиппа) суббота, день
label ep210_dialogues2_escort_start_Phillip_9:
    # не рендерить!
    mt "Мне сейчас нечего там делать."
    mt "Этот мерзавец сказал приходить к нему в субботу вечером."
    return

# мысли Моники (глазик) в красивом платье
label ep210_dialogues2_escort_start_Phillip_10:
    # не рендерить!
    mt "Я не могу поверить в происходящее..."
    mt "Я, Моника Бакфетт, приехала к этому мерзавцу!"
    mt "Возможно, я смогу сделать так, чтобы этот неудачник помог мне с деньгами."
    return

# мысли Моники (глазик) в любой одежде, кроме красивого платья
label ep210_dialogues2_escort_start_Phillip_11:
    # не рендерить!
    mt "Я не могу прийти к этому мерзавцу в такой одежде."
    mt "Он знает, что я Моника Бакфетт. Я леди. И должна выглядеть соответствующе."
    return

# дом Филиппа в субботу
label ep210_dialogues2_escort_start_Phillip_12:
    # Моника заходит в дом Филиппа, стоит рядом с входной дверью в гостиной
    # Филипп на диване или стоит посередине гостиной
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16373
    with fadelong
    philip "..."
    m "Филипп, я пришла..."
    m "..."
    sound highheels_short_walk
    img 16374
    with fade
    w
    img 16375
    with diss
    philip "Скажи, кто ты?"
    philip "Кто ко мне пришел?"
    img 16376
    with diss
    m "???"
    menu:
        "Субботняя шлюха номер 2.":
            music Pyro_Flow
            img 16377
            with fade
            mt "Черт!"
            mt "Я не хочу это говорить!"
            mt "Но если я не скажу это..."
            img 16378
            with diss
            mt "Он выгонит меня и я не смогу заработать денег."
            mt "..."
            music Groove2_85
            img 16379
            with fade
            m "Я субботняя... Субботняя ш-шлюха..."
            philip "У меня уже есть одна субботняя шлюха. А ты кто?"
            img 16380
            with diss
            m "Субботняя шлюха номер 2."

            if monica_philip_visit_whore1_exists == False:
                # если Филипп в этот день без шлюхи номер 1
                img 16379
                with fade
                philip "Субботняя шлюха номер 2 может заходить."
                # Моника проходит в гостиную
            else:
                # если Филипп в этот день с шлюхой номер 1
                # к нему подходит другая девушка с отеля и он ее обнимает
                # шлюха номер 1 на Монику смотрит пренебрежительно
                sound plastinka1b
                music Loved_Up
                img 16381
                with fade
                philip "У меня сегодня субботняя шлюха номер 1."
                img 16454
                with diss
                philip "Субботняя шлюха номер 2 может прийти через неделю."
                img 16455
                with fade
                w
                # Моника оказывается на улице
            return True
        "Моника Бакфетт!":
            music Pyro_Flow
            img 16382
            with fade
            mt "Вот мерзавец!"
            mt "Он хочет, чтобы я назвала себя какой-то шлюхой!"
            img 16383
            with diss
            mt "Не дождется!!!"
            mt "Достаточно того, что я сюда приехала!"
            img 16379
            with fade
            m "Я Моника Бакфетт!"
            philip "У меня нет ничего общего с Миссис Бакфетт."
            return False
    return

label ep210_dialogues2_escort_start_Phillip_13a: #На улице
    whore_number_1 "Шлюха номер 2, подожди!"
    return

label ep210_dialogues2_escort_start_Phillip_13b: # Моника оказывается на улице
    mt "Вот мерзавец!"
    mt "Неужели я стала шлюхой?!"
    mt "Нет. Это не так."
    mt "Это просто временные трудности!"
    mt "Я делаю это вынужденно..."
    mt "Так что этот раз не считается..."
    return

# если у Филиппа шлюха номер 1
# в один из визитов Моники, после того, как она оказалась на улице
label ep210_dialogues2_escort_start_Phillip_13:
    # к ней выходит шлюха номер 1
    music Loved_Up
    img 23167
    with fadelong
    whore_number_1 "Шлюха номер 2, подожди!"
    img 23168
    with fade
    m "???" # смотрит на нее удивленно
    img 23169
    with diss
    whore_number_1 "Слушай, я зарабатываю 200 долларов у него."
    whore_number_1 "Хочешь, я дам тебе 50 долларов?"
    img 23170
    with fade
    m "50 долларов?"
    m "За что?"
    img 23171
    with diss
    whore_number_1 "Ты мне поможешь удовлетворить Филиппа."
    music Pyro_Flow
    img 23172
    with fade
    m "Что? За 50 долларов?!"
    music Groove2_85
    img 23173
    with diss
    whore_number_1 "Да. 50 баксов тебе, остальные 150 - мои."
    img 23174
    with diss
    m "..."
    menu:
        "Отказаться.":
            # Моника зло смотрит на нее
            music Pyro_Flow
            img 23175
            with fade
            mt "Он платит этой шлюхе 200 долларов!"
            mt "А мне - какие-то жалкие 100!"
            mt "Мне! Самой красивой женщине этого города!!!"
            mt "!!!"
            # высокомерно говорит шлюхе номер 1
            img 23176
            with diss
            m "Неужели ты думала, что я соглашусь на такое?!"
            m "Конечно, нет!!!"
            mt "Да еще и за 50 долларов!"
            mt "!!!"
            return False
        "Мне нужны эти деньги...":
            return
    return

# Моника зашла в гостиную Филиппа
label ep210_dialogues2_escort_start_Phillip_14:
    music Pyro_Flow
    img 16384
    with fadelong
    mt "Мне даже думать противно о том, что мне предстоит сейчас сделать..."
    mt "Чтобы заработать какие-то жалкие 100 долларов."
    menu:
        "Минет.":
            return 1
        "Секс." if monica_philip_visits > 1:
            return 2
    return


# если выбран пункт "Минет"
label ep210_dialogues2_escort_start_Phillip_15:
    # Филипп садится на диван перед ТВ
    music Groove2_85
    img 16385
    with fadelong
    philip "У меня была тяжелая неделя."
    philip "Я хочу, чтобы шлюха номер 2 расслабила меня своим ротиком."
    mt "..."
    # он берет пульт от ТВ и смотрит телевизор
    music Pyro_Flow
    img 16386
    with fade
    mt "Моника, неужели ты способна на такое пойти?!"
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16387
            with diss
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16388
            with fade
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            sound highheels_short_walk
            img 16389
            with diss
            m "!!!"
            # Моника уходит
            return False
        "Сделать, что требует Филипп.":
            pass
    # Филипп поворачивается к Монике
    music Groove2_85
    img 16390
    with diss
    m "..."
    philip "В чем дело? Мне долго еще ждать?"
    img 16387
    with fade
    mt "..."
    mt "Боже! Как же это все омерзительно!"
    mt "Но мне нужны эти деньги..."
    # Моника подходит к дивану, на котором сидит Филипп, и опускается перед ним на колени
    img 16391
    with diss
    philip "Открывай свой ротик и приступай к работе."
    # расстегивает ширинку, достает член и продолжает смотреть в ТВ
    music stop
    img black_screen
    with diss
    sound snd_zip
    pause 1.5
    music Groove2_85
    img 16392
    with fade
    m "Я тебе буду делать это... А ты... Будешь смотреть телевизор?!"
    m "!!!"
    img 16393
    with diss
    philip "Это тебя не касается."
    philip "Шлюха номер 2 должна отрабатывать свои деньги..."
    philip "А не задавать мне глупые вопросы."
    music Power_Bots_Loop
    img 16394
    with fade
    mt "!!!"
    mt "Мерзавец!"
    mt "Ненавижу!!!"
    # Моника берет в рот его член, Филипп в это время продолжает смотреть ТВ со скучающим видом
    # минет
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound chpok6
    pause 1.0
    music2 Loved_Up

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
    scene black
    image videov_Monica_Philip_Blowjob2_1 = Movie(play="video/v_Monica_Philip_Blowjob2_1.mkv", fps=30)
    show videov_Monica_Philip_Blowjob2_1
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16395
    with fadelong
    philip "Да... Вот так..."
    img 16396
    with fade
    w
    sound keyboard
    img 16397
    with diss
    w
    sound keyboard
    img 16398
    with diss
    w
    sound keyboard
    img 16399
    with fade
    philip "Возьми его глубже..."
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
    scene black
    image videov_Monica_Philip_Blowjob2_2 = Movie(play="video/v_Monica_Philip_Blowjob2_2.mkv", fps=30)
    show videov_Monica_Philip_Blowjob2_2
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    img 16400
    with diss
    w
    sound keyboard
    img 16401
    with fade
    w
    sound keyboard
    img 16402
    with diss
    w
    sound keyboard
    img 16403
    with diss
    w
    music2 Loved_Up2
    img 16404
    with fade
    philip "Еще глубже."
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
    scene black
    image videov_Monica_Philip_Blowjob2_3 = Movie(play="video/v_Monica_Philip_Blowjob2_3.mkv", fps=30)
    show videov_Monica_Philip_Blowjob2_3
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16405
    with diss
    w
    img 16406
    with fade
    w
    sound keyboard
    img 16407
    with diss
    w
    sound keyboard
    img 16408
    with diss
    w
    if game.extra == True:
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob2_1.ogg"
        scene black
        image videov_Monica_Philip_Blowjob2_4 = Movie(play="video/v_Monica_Philip_Blowjob2_4.mkv", fps=30)
        show videov_Monica_Philip_Blowjob2_4
        with fade
        philip "Мммммм..."
        wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16409
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 16410
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    philip "Мммммм..."
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    # сперма стекает изо рта Моники
    img 16411
    with fadelong
    philip "Теперь проглоти это."
    m "..."
    menu:
        "Выплюнуть.":
            # Моника смотрит на него с отвращением
            music Pyro_Flow
            img 16412
            with fade
            mt "Я не смогу проглотить это!"
            mt "Меня стошнит."
            # выплевывает
            img 16413
            with diss
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
#            sound highheels_short_walk
#            img 16389
#            with fade
#            w
#            pass
        "Проглотить.":
            pass
            img 16414
            with fade
            sound snd_gulp
            $ monica_philip_visits_swallowed += 1
            $ add_corruption(monica_philip_visits_swallowed_corruption, "monica_philip_visits_swallowed" + str(monica_philip_visits_swallowed))
            w
    # Филипп достает из кармана купюру 100 долларов и кидает ее на диван
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16415
    with fade
    philip "Субботняя шлюха номер 2 может забрать свои деньги."
    philip "И уходить."
    # Моника забирает деньги
    img 16416
    with diss
    m "..."
    img 16419
    with fade
    menu:
        "Попросить еще денег.":
            img 16417
            with diss
            mt "Может, поросить у него еще денег?"
            mt "Ведь в прошлый раз он заплатил мне 300 долларов."
            img 16420
            with fade
            $ monica_philip_ask_money1 += 1
            $ add_corruption(monica_philip_ask_money1_corruption, "monica_philip_ask_money1" + str(monica_philip_ask_money1))
            m "Филипп, я..."
            m "..."
            m "Хотела спросить, не мог бы ты дать мне еще немного денег?"
            # поворачивается к ней
            img 16421
            with diss
            philip "???"
            philip "Моей субботней шлюхе нужны деньги?"
            img 16422
            with diss
            philip "Я тебе их только что заплатил."
            philip "Хочешь еще денег - приходи через неделю."
            # отворачивается
            music Pyro_Flow
            img 16423
            with fade
            mt "Жадный неудачник!"
            return True
        "Уйти.":
            pass
    music Pyro_Flow
    img 16417
    with diss
    mt "Сволочь!"
    mt "!!!"
    sound highheels_short_walk
    img 16418
    with fade
    # Моника уходит
    return True

# если выбран пункт "Секс"
label ep210_dialogues2_escort_start_Phillip_16:
    # Филипп садится на диван
    music Groove2_85
    img 16424
    with fadelong
    philip "Сейчас шлюха номер 2 предложит мне себя, как в прошлый раз."
    philip "А я пока подумаю, что я с ней сегодня сделаю."
    # выбор: уйти или предложить себя Филиппу
    music Pyro_Flow
    img 16386
    with fade
    mt "Моника, неужели ты способна на такое пойти?!"
    mt "..."
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16387
            with diss
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16425
            with fade
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            sound highheels_short_walk
            img 16418
            with diss
            return False
        "Предложить себя Филиппу.":
            pass
    # Моника стоит перед ним в нерешительности
    music Groove2_85
    img 16426
    with diss
    m "..."
    m "Ч-что мне сделать?"
    img 16427
    with fade
    philip "Задирай платье и нагибайся, раздвинув ноги."
    # Моника поворачивается к нему задом и делает, как он сказал
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16428
    with fade
    w
    img 16429
    with diss
    philip "Что же шлюха может предложить мне сегодня?"
    philip "Возможно, свою задницу?"
    music Pyro_Flow
    img 16430
    with fade
    mt "О, нет! Он хочет сделать это с моей попой?!"
    mt "Нет! Я не перенесу этого!"
    mt "!!!"
    music Loved_Up
    img 16431
    with diss
    philip "Хммм... Нет, задницу я оставлю на потом..."
    philip "Я подожду, когда твои акции подешевеют..."
    philip "А сейчас... Может быть, ротик?"
    # Филипп расстегивает штаны, достает стояк, начинает подрачивать его
    img 16432
    with diss
    philip "Субботняя шлюха, повернись и покажи мне свою грудь, приспусти платье."
    # Моника поворачивается и приспускает платье, смотрит на него зло
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16433
    with fade
    philip "Хорошо. Мне нравится, что моя шлюха такая послушная."
    img 16434
    with diss
    mt "Сволочь!"
    mt "!!!"
    img 16435
    with fade
    philip "Кстати, я даже не предложил своей субботней шлюхе номер 2 присесть..."
    philip "Иди сюда. Присаживайся."
    # Моника смотрит на диван и делает шаг
    img 16436
    with diss
    philip "Нет, не на диван. Садись на мой член."
    img 16437
    with diss
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            music Pyro_Flow
            img 16438
            with fade
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16439
            with diss
            m "Нет. Я..."
            m "Я не буду этого делать!"
            img 16440
            with fade
            sound highheels_short_walk
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            return False
        "Сесть на член Филиппа.":
            pass
    # Моника смотрит на его член
    music Groove2_85
    img 16441
    with fade
    mt "Ненавижу этого мерзавца!"
    mt "!!!"
    img 23177
    with fadelong
    w
    sound snd_fabric1
    img 23178
    with fadelong
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound chpok6
    pause 1.0
    music2 Loved_Up2
    # подходит к нему и нерешительно выполняет, сев к нему на колени, лицом к нему
    # тот, откинувшись на диван, самодовольно ухмыляется
    img 16442
    with fadelong
    philip "Давай, выполняй. Шлюха же хочет заработать денег?"
    # секс, Моника на его коленях, двигается вверх-вниз, он лапает ее за попу и за грудь
    img 16448
    with fade
    mt "Это так... Так неприятно..."
    mt "Скорее бы это закончилось."
    mt "Хочу забрать деньги и уйти отсюда."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_1 = Movie(play="video/v_Monica_Philip_Sex1_1.mkv", fps=30)
    show videov_Monica_Philip_Sex1_1
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16443
    with diss
    philip "Да..."
    img 16444
    with fade
    philip "Давай, быстрее..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_2 = Movie(play="video/v_Monica_Philip_Sex1_2.mkv", fps=30)
    show videov_Monica_Philip_Sex1_2
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_3 = Movie(play="video/v_Monica_Philip_Sex1_3.mkv", fps=30)
    show videov_Monica_Philip_Sex1_3
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16445
    with diss
    philip "Еще..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_4 = Movie(play="video/v_Monica_Philip_Sex1_4.mkv", fps=30)
    show videov_Monica_Philip_Sex1_4
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")


    # Моника смотрит на него с отвращением
    img 16446
    with diss
    w
    img 16447
    with diss
    m "..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_5 = Movie(play="video/v_Monica_Philip_Sex1_5.mkv", fps=30)
    show videov_Monica_Philip_Sex1_5
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16449
    with fade
    philip "Оооо... Даааа..."

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_7 = Movie(play="video/v_Monica_Philip_Sex1_7.mkv", fps=30)
    show videov_Monica_Philip_Sex1_7
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Philip_Sex1_1.ogg"
    scene black
    image videov_Monica_Philip_Sex1_6 = Movie(play="video/v_Monica_Philip_Sex1_6.mkv", fps=30)
    show videov_Monica_Philip_Sex1_6
    with fade
    philip "Мммммм..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    # кончает ей на платье или на живот
    img 16450
    with diss
    philip "Мммммм..."
    w
    img 16451
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 16452
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    img 16453
    with diss
    w
    # Филипп одевается и бросает на диван купюру
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16415
    with fade
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 2 может забрать свои деньги."
    philip "И уходить."
    # Моника одевается и забирает деньги
    img 16416
    with diss
    m "..."
    menu:
        "Попросить еще денег.":
            img 16417
            with fade
            mt "Может, поросить у него еще денег?"
            mt "Ведь в прошлый раз он заплатил мне 300 долларов."
            img 16420
            with diss
            m "Филипп, я..."
            m "..."
            m "Хотела спросить, не мог бы ты дать мне еще немного денег?"
            # смотрит на нее
            img 16421
            with fade
            philip "???"
            philip "Моей субботней шлюхе нужны деньги?"
            img 16422
            with diss
            philip "Я тебе их только что заплатил."
            philip "Хочешь еще денег - приходи через неделю."
            # отворачивается
            music Pyro_Flow
            img 16423
            with fade
            sound highheels_short_walk
            mt "Жадный неудачник!"
            $ monica_philip_ask_money1 += 1
            return True
        "Уйти.":
            pass
    music Pyro_Flow
    img 16418
    with fade
    sound highheels_short_walk
    mt "Сволочь!"
    mt "!!!"
    # Моника уходит
    return True


# мысли Моники (вышла от Филиппа, заработав деньги)
label ep210_dialogues2_escort_start_Phillip_17:
    # не рендерить!
    mt "Я заставлю пожалеть его об этом!"
    mt "Он еще будет умолять меня о прощении!"
    mt "!!!"
    return

# мысли Моники (вышла от Филиппа, НЕ заработав денег)
label ep210_dialogues2_escort_start_Phillip_18:
    # не рендерить!
    mt "Мерзкий извращенец!"
    mt "Притворяется джентельменом, а на деле ведет себя как грязный хам!"
    mt "Ненавижу его!"
    return

# мысли Моники (вышла от Филиппа, хочет снова зайти к нему домой)
label ep210_dialogues2_escort_start_Phillip_19:
    # не рендерить!
    mt "Не хочу его больше видеть!!!"
    mt "Мерзавец!"
    return False

# мысли Моники (глазик, вышла от Филиппа)
label ep210_dialogues2_escort_start_Phillip_20:
    # не рендерить!
    mt "Я не могу поверить в происходящее..."
    mt "Я, Моника Бакфетт, унижалась перед этим мерзавцем!"
    mt "Из-за каких-то 100 долларов!"
    mt "!!!"
    mt "Я заставлю его пожалеть об этом!"
    return
