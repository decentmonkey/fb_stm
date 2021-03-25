label street_house_gate:
    if EP1==True:
        jump street_house_gate_EP1
    $ print "enter_street_house_gate"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_3

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_House_Gate[day_suffix]"
    if day_time == "day":
        music Mandeville
    else:
        music night_ambience
    return

label street_house_gate_init:
    if EP1==True:
        return
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Gate_Monica_[cloth][day_suffix]", "click" : "street_house_gate_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Gates", {"type":2, "base":"Street_House_Gate_Teleport_Outside", "click" : "street_house_gate_environment", "actions" : "lw", "zorder" : 0, "b":0.2, "tint":[1.0, 1.0, 0.7], "teleport":True, "house_out_teleport":True})
    $ add_object_to_scene("Teleport_House_Yard", {"type":3, "text" : t_("НАЗАД ВО ДВОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_house_gate_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_gate_teleport:
    if EP1==True:
        jump street_house_gate_teleport_EP1
    if obj_name == "Teleport_House_Yard":
        call change_scene("street_house_main_yard") from _call_change_scene_43
        return
    return
label street_house_gate_environment:
    if EP1==True:
        jump street_house_gate_environment_EP1
    if obj_name == "Monica":
        mt "Ворота моего дома."
        "Вернее не моего, но это какое-то недоразумение."
        "Временное..."
        return

    if obj_name == "Gates":
        if obj_data["action"] == "l":
            mt "Ворота моего дома."
            "Вернее не моего, но это какое-то недоразумение."
            "Временное..."
            return

        if obj_data["action"] == "w":
            call change_scene("street_house_outside") from _call_change_scene_44
            return
    return




# EP1




label street_house_gate_EP1:
    $ print "enter_street_house_gate"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_14

    $ scene_name = "street_house_gate"
    $ sceneIsStreet = True
    $ scene_caption = t_("House Gates")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Street_House_Gate_Monica_" + cloth + day_suffix

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Gate_Monica_" + cloth + day_suffix, "click" : "street_house_gate_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

#    $ add_object_to_scene("Teleport_House_Outside", {"type":3, "text" : t_("ЗА ВОРОТА"), "rarrow" : "arrow_up_2", "base":"Street_House_Gate_Teleport_Outside", "click" : "street_house_gate_teleport", "xpos" : 638, "ypos" : 564, "zorder":11, "b":0.2, "tint":[1.0, 1.0, 0.7]})
    $ add_object_to_scene("Gates", {"type":2, "base":"Street_House_Gate_Teleport_Outside", "click" : "street_house_gate_environment", "actions" : "lw", "zorder" : 0, "b":0.2, "tint":[1.0, 1.0, 0.7]})
#    $ add_object_to_scene("Teleport_House_Outside", {"type":3, "text" : t_("ЗА ВОРОТА"), "rarrow" : "arrow_up_2", "base":"Street_House_Gate_Teleport_Outside", "click" : "street_house_gate_teleport", "xpos" : 638, "ypos" : 564, "zorder":11, "b":0.2, "tint":[1.0, 1.0, 0.7]})
    $ add_object_to_scene("Teleport_House_Yard", {"type":3, "text" : t_("НАЗАД ВО ДВОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_house_gate_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_gate_teleport_EP1:
    if obj_name == "Teleport_House_Yard":
        call change_scene("street_house_main_yard") from _call_change_scene_33
        return
    return
label street_house_gate_environment_EP1:
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Ворота моего дома."
            "Вернее не моего, но это какое-то недоразумение."
            "Временное..."
            return
        m "Через это место я обычно выезжаю из дома."
        if day_time == "evening":
            m "Но сейчас уже слишком темно."
    if obj_name == "Gates":
        if obj_data["action"] == "l":
            if gameStage > 2:
                mt "Ворота моего дома."
                "Вернее не моего, но это какое-то недоразумение."
                "Временное..."
                return
            if day_time == "day":
                m "Это мои ворота."
                "За ними обитают разные жуткие монстры."
                "Например, бомжи и неудачники."
                "Я стараюсь держаться от них подальше, как от зомби.
                Они ведь не смогут ворваться сюда, правда?
                Ворота крепкие."
            if day_time == "evening":
                m "Что я делаю здесь, около ворот, когда на улице так темно?"
                m "Ведь я не собираюсь идти туда, правда?"

        if obj_data["action"] == "w":
            call change_scene("street_house_outside") from _call_change_scene_34
            return
    return
