label whores_place_street1:
    $ print "enter_whores_place_street1"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_8

    $ sceneIsStreet = True
    $ scene_image = "scene_street_Whores_Street1[day_suffix]"

    $ whoresPlacePreviousLocation = "street"
    if day_time == "day":
        music street4
    else:
        if rand(1,4) > 1:
            music street_evening3
        else:
            music street13_ambulance
    return

label whores_place_street1_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Street1_Monica_[cloth][day_suffix]", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Citizen_14", {"type":2, "base":"Street_Whores_Street1_Citizen_14[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_15", {"type":2, "base":"Street_Whores_Street1_Citizen_15[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

    $ add_object_to_scene("Fire_Valve", {"type":2, "base":"Street_Whores_Street1_Fire_Valve", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_Whores_Street1_Street_Fencing1", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_Whores_Street1_Street_Fencing2", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Street_Light", {"type":2, "base":"Street_Whores_Street1_Street_Light", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Street_Sign", {"type":2, "base":"Street_Whores_Street1_Street_Sign", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash_Can", {"type":2, "base":"Street_Whores_Street1_Trash_Can", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Street_Corner", {"type":3, "text" : t_("УГОЛ УЛИЦЫ"), "rarrow" : "arrow_right_2", "base":"Street_Whores_Street1_Teleport_Street_Corner", "click" : "whores_place_street1_teleport", "xpos" : 1724, "ypos" : 462, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Whores_Place", {"type":3, "text" : t_("ПЕРЕКРЕСТОК"), "larrow" : "arrow_left_2", "base":"Street_Whores_Street1_Teleport_Whores_Place", "click" : "whores_place_street1_teleport", "xpos" : 557, "ypos" : 830, "zorder":15, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label whores_place_street1_teleport:
    if obj_name == "Teleport_Street_Corner":
        call change_scene("street_corner", "Fade", "highheels_run2") from _call_change_scene_80
        return
    if obj_name == "Teleport_Whores_Place":
        call change_scene("whores_place", "Fade", "highheels_run2") from _call_change_scene_81
        return
    return
label whores_place_street1_environment:
    if obj_name == "Monica":
        mt "Отвратительное место!"
        return
    if obj_name == "Fire_Valve":
        mt "Что это? Пожарный вентиль?
        Из позапрошлого века??"
    if obj_name == "Street_Fencing1" or obj_name == "Street_Fencing2":
        mt "Эти старые ржавые ограждения очень опасны."
        return
    if obj_name == "Street_Light":
        mt "Хорошо бы чтоб этот фонарь не упал на меня, пока я здесь иду!"
    if obj_name == "Street_Sign":
        mt "Какой-то старый ржавый дорожный знак..."
    if obj_name == "Trash_Can":
        mt "Мусорка? Зачем она здесь нужна?"
        "Все это место - сплошная помойка!"
    return
