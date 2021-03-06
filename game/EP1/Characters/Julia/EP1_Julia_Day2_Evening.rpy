label EP1_julia_day2_evening(obj_name, obj_data):
    if cloth_type == "BusinessCloth":
        imgc Dial_Monica_BusinessCloth2_Thinking
        mt "Я только с улицы."
        "Сначала надо переодеться."
        return

    if obj_data["action"] == "l":
        call EP1_floor1_monica_julia_revenge_interact_look()
        return
    if obj_data["action"] == "t":
        if monicaEated == True:
            call EP1_julia_day2_evening_monica_eated()
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
        call EP1_refresh_scene_fade()
        $ notif (t_("Юлия убежала на кухню."))
        return
    return

label EP1_julia_day2_evening_monica_eated:
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



#
