default hostelStreet3MonicaFromSideSuffix = ""

label hostel_street3:
    $ print "enter_hostel_street2"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_3

    $ sceneIsStreet = True

    $ scene_image = "scene_Hostel_Street3[day_suffix]"

    $ hostelStreet2MonicaFromSideSuffix = ""
    if day_time == "day":
        music street3
    else:
        if rand(1,4) > 1:
            music street_evening4
        else:
            music street13_ambulance
    return
label hostel_street3_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street3_Monica_[cloth][hostelStreet3MonicaFromSideSuffix][day_suffix]", "click" : "hostel_street3_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Citizen_3", {"type" : 2, "base" : "Hostel_Street3_Citizen_3[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_4", {"type" : 2, "base" : "Hostel_Street3_Citizen_4[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_7", {"type" : 2, "base" : "Hostel_Street3_Citizen_7[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

    $ add_object_to_scene("Teleport_Hostel_Street_Corner", {"type":3, "text" : t_("УГОЛ УЛИЦЫ"), "rarrow" : "arrow_right_2", "base":"Hostel_Street3_Teleport_Street_Corner", "click" : "hostel_street3_teleport", "xpos" : 1661, "ypos" : 1012, "zorder":15, "teleport":True, "high_sprite_hover":True})
    $ add_object_to_scene("Teleport_Hostel_Street2", {"type":3, "text" : t_("ГРЯЗНАЯ УЛИЦА"), "larrow" : "arrow_left_2", "base":"Hostel_Street3_Teleport_Hostel_Street2", "click" : "hostel_street3_teleport", "xpos" : 329, "ypos" : 1035, "zorder":15, "teleport":True, "high_sprite_hover":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street3_teleport:
    if obj_name == "Teleport_Hostel_Street_Corner":
        if cloth_type == "Nude":
            call change_scene("street_corner", "Fade", "snd_walk_barefoot") from _call_change_scene_14
            return
        call change_scene("street_corner", "Fade", "highheels_run2") from _call_change_scene_15
        return
    if obj_name == "Teleport_Hostel_Street2":
        if cloth_type == "Nude":
            call change_scene("hostel_street2", "Fade", "snd_walk_barefoot") from _call_change_scene_16
            return
        call change_scene("hostel_street2", "Fade", "highheels_run2") from _call_change_scene_17
        return

    return
label hostel_street3_environment:

    return
