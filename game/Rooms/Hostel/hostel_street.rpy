#default hostelStreetSceneName = "scene_Hostel_Street[day_suffix]"

label hostel_street:
    $ print "enter_hostel_street"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_6

    $ sceneIsStreet = True

    $ scene_image = "scene_Hostel_Street_Pub[day_suffix]"

    $ hostelStreet2MonicaFromSideSuffix = "2"

    music2 stop

    if day_time == "day":
        music street1
    else:
        if rand(1,4) > 1:
            music street_evening4
        else:
            music street13_ambulance
    return
label hostel_street_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street_Monica_[cloth][day_suffix]", "click" : "hostel_street_environment", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("Teleport_Hostel_Street_Door", {"type":2, "base":"Hostel_Street_Teleport_Hostel_Street2", "click" : "hostel_street_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True})

    $ add_object_to_scene("Citizen_1", {"type" : 2, "base" : "Hostel_Street_Citizen_1[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_2", {"type" : 2, "base" : "Hostel_Street_Citizen_2[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_9", {"type" : 2, "base" : "Hostel_Street_Citizen_9[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_11", {"type" : 2, "base" : "Hostel_Street_Citizen_11[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

#    $ add_object_to_scene("Car", {"type":2, "base":"hostel_street_Car", "click" : "hostel_street_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Edge_C", {"type":3, "text" : t_("УГОЛ ДОМА"), "rarrow" : "arrow_right_2", "base":"Hostel_Street_Teleport_Hostel_Edge_C", "click" : "hostel_street_teleport", "xpos" : 1609, "ypos" : 1030, "zorder":15, "teleport":True, "high_sprite_hover":True})
    $ add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : t_("НАЗАД К ШАВЕРМЕ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow_Short1", "click" : "hostel_street_teleport", "xpos" : 210, "ypos" : 1030, "zorder":15, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street_init2:
    $ add_object_to_scene("Teleport_Slums_Apartments", {"type":3, "text" : t_("ДОМ В ТРУЩОБАХ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "hostel_street_teleport", "xpos" : 220, "ypos" : 545, "zorder":3, "teleport":True}, scene="hostel_street")
    return

label hostel_street_teleport:
    if obj_name == "Teleport_Slums_Apartments":
        if cloth_type == "Nude":
            call change_scene("street_monicahome", "Fade", "snd_walk_barefoot") from _rcall_change_scene_55
            return
        call change_scene("street_monicahome", "Fade", "highheels_run2") from _rcall_change_scene_56
        return

    if obj_name == "Teleport_Hostel_Edge_C":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot") from _call_change_scene_47
            return
        call change_scene("hostel_edge_1_c", "Fade", "highheels_run2") from _call_change_scene_48
        return
    if obj_name == "Teleport_Shawarma":
        call change_scene("whores_place_shawarma", "Fade", "highheels_run2") from _call_change_scene_49
        return
    if obj_name == "Teleport_Hostel_Street_Door":
        if act == "l":
            mt "Я не пойду туда! Там насильники! И я теперь должна $10.000 управляющей этой дыры."
            return
        if act == "w":
            call change_scene("hostel_street_door") from _call_change_scene_50
            return
    if obj_name == "Teleport_Hostel_Pub":
        if cloth == "Kebab":
            mt "Я не могу зайти туда одетой в рекламу кебеба..."
            mt "Я просто застряну в проходе!"
            return
        call ep29_quests_pub1_begin_dance_quest_check() from _rcall_ep29_quests_pub1_begin_dance_quest_check # проверяем условия старта квеста на танцы в баре
        call change_scene("pub") from _call_change_scene_192
        return
    return
label hostel_street_environment:
    if obj_name == "Monica":
        pass

    return
