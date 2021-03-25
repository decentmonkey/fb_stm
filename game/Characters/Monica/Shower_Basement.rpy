label basement_shower_init:
    $ add_hook("enter_scene", "basement_shower_check", scene="basement_pool")
    $ add_hook("enter_scene", "basement_shower_begin", scene="basement_pool")
    return

label basement_shower_interact:
    if act == "l":
        mt "Душ..."
        "Я могу его использовать вместо верхнего душа, куда Бетти запретила мне заходить."
        "Она бы запретила и этот душ, но я могу принимать его пока она не видит..."
        return
    if act == "h":
        call basement_shower_use1() from _call_basement_shower_use1
        return
    return

label basement_toilet_interact:
    if act == "l":
        mt "Туалет..."
        mt "Я могу здесь писать пока Бетти не видит."
        "Уверена она бы и это запретила."
        return
    if act == "h":
        call basement_toilet_use1() from _call_basement_toilet_use1
        return
    return

label basement_shower_begin:
    # какой-то начальный текст
    mt "Бетти запретила мне пользоваться ванной наверху."
    "Может быть мне можно пользоваться туалетом здесь?"
    $ remove_hook()
    return

label basement_shower_check:
    if day - monicaLastPissedDay >= 3:
        mt "Было бы неплохо пописать..."
        "Я уже давно не писала и Бетти как раз нет поблизости."
        return

    if day - monicaLastShowerDay >= 3:
        mt "Было бы неплохо принять душ..."
        "Я уже давно его не принимала, а мое тело требует чистоты. Да и Бетти поблизости нет..."
        return

    return

label basement_shower_use1:
    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return

    $ store_music()
    music stop
    #Моника принимает душ
    #вариации (случайно)
    #звук душа
    music snd_shower2
    img 7095
    with fade
    w
    if monicaPussyShaved == False:
        $ shower_images = ["7096", "7097", "7098", "7099", "7100", "7101", "7102", "7103", "7104", "7105", "7106", "7107"]
    else:
        $ shower_images = ["7096", "7097", "7098", "10564", "10565", "10566", "7102", "7103", "10567", "7105", "7106", "7107"]

    $ images = random.sample(set(shower_images), 3)

    img images[0]
    w
    img images[1]
    w
    img images[2]
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Как же хорошо принять душ!"
    if rnd == 2:
        mt "Мне приятно ощущать капельки воды, стекающей по моему телу..."
    if rnd == 3:
        mt "Мое тело божественно!"

    $ monicaLastShowerDay = day
    $ monicaLastShowerDayTime = day_time
    $ restore_music()
    call refresh_scene_fade() from _call_refresh_scene_fade_28

    return

label basement_toilet_use1:
    if monicaLastPissedDay == day and monicaLastPissedDayTime == day_time:
        mt "Я уже писала недавно. Я пока не хочу."
        return
    $ store_music()
    music stop
    #Моника писает
    #звук
    #whore
    #вариации (случайно)
    if cloth == "Whore":
        $ toilet_images = ["7079", "7080", "7081", "7082", "7083", "7084", "7085", "7086", "7087"]
        $ images = random.sample(set(toilet_images), 4)

    if cloth == "CasualDress1":
        $ images = ["11724", "11725", "11726"]
        $ images = random.sample(set(images), 3)

    if cloth == "SchoolOutfit1":
        $ images = ["22274", "22275", "22276"]
        $ images = random.sample(set(images), 3)


    #governess
    if cloth == "Governess":
        if monicaUnder != "Nude":
            $ toilet_images = ["7088", "7089", "7090", "7091", "7092", "7093", "7094"]
            $ images = random.sample(set(toilet_images), 3)
        else:
            $ images = ["10568", "10569", "10570"]
            $ images = random.sample(set(images), 3)

    if monicaBettyPanties == True:
        if monicaBettyPantiesId == 1:
            $ images = [7163, 7164, 7165]
        if monicaBettyPantiesId == 2:
            $ images = [7166, 7167, 7168]
        if monicaBettyPantiesId == 3:
            $ images = [7169, 7170, 7171]
        if monicaBettyPantiesId == 4:
            $ images = [7172, 7173, 7174]
        if monicaBettyPantiesId == 5:
            $ images = [7175, 7176, 7177]


    img images[0]
    with fade
    w
    sound snd_piss
    $ rnd = rand(1,4)
    if rnd == 1:
        img images[1]
        mt "Эх... мне надо придумать как вернуть все назад..."
        img images[2]
        mt "Я такая красивая... Как со мной могло случиться такое?"
    if rnd == 2:
    #
        img images[1]
        mt "Этот дом такой большой, а мне приходится прятаться чтобы пописать..."
        img images[2]
        "Но, по крайней мере я здесь, а не на улице..."
    #
    if rnd == 3:
        img images[1]
        w
        img images[2]
        mt "Надеюсь Бетти не заметит как я делаю это..."

    #
    if rnd == 4:
        img images[1]
        w
        img images[2]
        mt "Девушка с такой красотой как у меня не заслуживает того что со мной случилось..."


    $ monicaLastPissedDay = day
    $ monicaLastPissedDayTime = day_time
    $ restore_music()
    call refresh_scene_fade() from _call_refresh_scene_fade_29

    return
