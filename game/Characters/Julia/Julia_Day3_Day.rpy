label julia_day3_day(obj_name, obj_data):
    if obj_data["action"] == "l":
        call floor1_monica_julia_revenge_interact_look() from _call_floor1_monica_julia_revenge_interact_look_3
        return
    if obj_data["action"] == "t":
        if monicaEated == True:
            call julia_day3_monica_eated() from _call_julia_day3_monica_eated
            return
        if juliaMonicaYell == False and juliaPunished == False:
            $ imageName = "4254" + day_suffix
            img imageName
        if juliaMonicaYell == True and juliaPunished == False:
            $ imageName = "4255" + day_suffix
            img imageName

        if juliaPunished == True:
            $ imageName = "4256" + day_suffix
            img imageName
        with fade

        julia "Миссис Бакфетт.
        Вам подать еду?"
        m "Да, Юлия.
        Можешь подавать."
        julia "Слушаюсь, Миссис Бакфетт!"
        $ juliaLocation = "kitchen"
        sound highheels_run1
        call refresh_scene_fade() from _call_refresh_scene_fade_103
        show screen notify (t_("Юлия убежала на кухню."))
        return
    return

label julia_day3_monica_eated:
    if juliaMonicaYell == False and juliaPunished == False:
        $ imageName = "4254" + day_suffix
        img imageName

    if juliaMonicaYell == True and juliaPunished == False:
        $ imageName = "4255" + day_suffix
        img imageName

    if juliaPunished == True:
        $ imageName = "4256" + day_suffix
        img imageName
    with fade
    julia "Миссис Бакфетт.
    Вы уже кушали недавно."
    "Вам подать снова?"

    menu:
        "Не надо, продолжай работу.":
            m "Не надо, продолжай работу."
            if juliaPunishedVoluntarily == True:
                m "Не забудь про уборку пятна в свободное время..."
            if juliaPunishedLow == True:
                m "Я не заставила тебя убирать пятно, но у тебя есть другие обязанности."
                "Не забывай про них."
            if juliaMonicaForgivenessAfterPunishment == True:
                m "И смотри, чтобы я не пожалела о том что простила тебя!"
            julia "Конечно, Миссис Бакфетт."

    return
