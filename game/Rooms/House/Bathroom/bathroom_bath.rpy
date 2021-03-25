default monicaBathroomForbidden = True

label bathroom_bath:
    if EP1==True:
        jump bathroom_bath_EP1
    $ print "enter_bathroom_bath"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_14

    $ scene_image = "scene_Bathroom_Bath"

#    $ autorun_to_object(scene_name, "afterJailHouse_dialogue10")
    return

label bathroom_bath_init:
    if EP1==True:
        return
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Bath_Monica_[cloth]", "click" : "bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Bath", {"type":2, "base":"Bathroom_Bath_Bath", "click" : "bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "bathroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Bathroom_Shower", {"type":3, "text" : t_("ДУШ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "bathroom_teleport", "xpos" : 1650, "ypos" : 520, "zorder":11, "teleport":True})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label bathroom_teleport:
    if EP1==True:
        jump bathroom_teleport_EP1
    if obj_name == "Teleport_Bathroom_Shower":
        call change_scene("bathroom_shower") from _call_change_scene_112
        return
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_113
        return
    if obj_name == "Teleport_Bathroom_Bath":
        call change_scene("bathroom_bath") from _call_change_scene_114
        return

label bathroom_environment:
    if EP1==True:
        jump bathroom_environment_EP1
    if obj_name == "Monica":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться ванной комнатой!"
            return

    if obj_name == "Bath":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться ванной!"
            return

    if obj_name == "Shower":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться душем!"
            return
    return




# EP1


default bathTaken = False
default bathTakenJust = False
default monicaBathroomForbidden = False

label bathroom_bath_EP1:
    $ print "enter_bathroom_bath"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_13

    $ scene_name = "bathroom_bath"
    $ scene_caption = t_("Bathroom Bath")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Bathroom_Bath_Monica_" + cloth

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Bath_Monica_" + cloth, "click" : "bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})


    $ add_object_to_scene("Bath", {"type":2, "base":"Bathroom_Bath_Bath", "click" : "bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "bathroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover": True})
    $ add_object_to_scene("Teleport_Bathroom_Shower", {"type":3, "text" : t_("ДУШ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "bathroom_teleport", "xpos" : 1650, "ypos" : 520, "zorder":11})

    if gameStage > 2:
        if monicaBathroomForbidden == True and scene_name != lastSceneName:
            $ autorun_to_object(scene_name, "afterJailHouse_dialogue10")


    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label bathroom_teleport_EP1:
    if obj_name == "Teleport_Bathroom_Shower":
        call change_scene("bathroom_shower") from _call_change_scene_6
        return
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_7
        return
    if obj_name == "Teleport_Bathroom_Bath":
        call change_scene("bathroom_bath") from _call_change_scene_8
        return

label bathroom_environment_EP1:
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
                call afterJailHouse_dialogue9() from _call_afterJailHouse_dialogue9
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
                call afterJailHouse_dialogue9() from _call_afterJailHouse_dialogue9_1
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
