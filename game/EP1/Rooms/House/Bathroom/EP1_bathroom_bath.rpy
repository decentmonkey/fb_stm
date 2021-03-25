default bathTaken = False
default bathTakenJust = False
default monicaBathroomForbidden = False

label EP1_bathroom_bath:
    $ print "enter_bathroom_bath"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "bathroom_bath"
    $ scene_caption = t_("Bathroom Bath")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Bathroom_Bath_Monica_" + cloth

    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Bath_Monica_" + cloth, "click" : "EP1_bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})


    $ EP1_add_object_to_scene("Bath", {"type":2, "base":"Bathroom_Bath_Bath", "click" : "EP1_bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_bathroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover": True})
    $ EP1_add_object_to_scene("Teleport_Bathroom_Shower", {"type":3, "text" : t_("ДУШ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "EP1_bathroom_teleport", "xpos" : 1650, "ypos" : 520, "zorder":11})

    if gameStage > 2:
        if monicaBathroomForbidden == True and scene_name != lastSceneName:
            $ EP1_autorun_to_object(scene_name, "afterJailHouse_dialogue10")


    return

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_bathroom_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bathroom_Shower":
        call EP1_change_scene("bathroom_shower")
        return
    if obj_name == "Teleport_Floor2":
        call EP1_change_scene("floor2")
        return
    if obj_name == "Teleport_Bathroom_Bath":
        call EP1_change_scene("bathroom_bath")
        return

label EP1_bathroom_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться ванной комнатой!"
            return
        m "Что бы мне принять?"

        "Душ?"

        "Или ванну?"

    if obj_name == "Bath":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться ванной!"
            return
        if obj_data["action"] == "l":
            m "Я обожаю свою ванну."

            "В ней можно наслаждаться уединением и ни о чем не думать."

            "Ни о чем не думать - это не так-то просто для такой умной девушки как я."

        if obj_data["action"] == "h":
            if gameStage > 2 and monicaBathroomForbidden == False:
                call EP1_afterJailHouse_dialogue9()
                return
            if cloth_type != "HomeCloth":
                m "Не полезу же я в платье в ванную!"
                "Мне надо переодеться сначала!"
                return
            if bathTakenJust == True:
                m "Я недавно принимала водные процедуры.
                Но почему-бы не понежиться еще..."
                wc
            sound snd_bathroom
            img 1047
            with fade
            w
            img 1048
            w
            img 1049
            w
            img 1050
            m "Как же хорошо понежиться в ванной!"
            w
            $ remove_objective("take_bath")
            $ bathTaken = True
            $ bathTakenJust = True
            $ scene_transition = "Fade"

    if obj_name == "Shower":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться душем!"
            return
        if obj_data["action"] == "l":
            m "Душ мне по душе."

            "Мне нравится как капельки воды стекают по моему телу."

        if obj_data["action"] == "h":
            if gameStage > 2 and monicaBathroomForbidden == False:
                call EP1_afterJailHouse_dialogue9()
                return
            if cloth_type != "HomeCloth":
                m "Не пойду же я в платье в душ!"
                "Мне надо переодеться сначала!"
                return
            if bathTakenJust == True:
                m "Я недавно принимала водные процедуры.
                Но почему-бы не понежиться еще..."
                wc
            sound snd_shower
            img 1045
            with fade
            w
            img 1046
            w
            img 1048
            w
            img 1049
            w
            img 1050
            m "Как же хорошо принять душ!"
            w
            $ remove_objective("take_bath")
            $ bathTaken = True
            $ bathTakenJust = True
            $ scene_transition = "Fade"
    return
