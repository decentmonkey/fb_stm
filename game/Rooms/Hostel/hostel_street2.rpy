default hostelStreet2MonicaFromSideSuffix = ""

label hostel_street2:
    if EP1==True:
        jump hostel_street2_EP1
    $ print "enter_hostel_street2"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_9

    $ sceneIsStreet = True

    $ scene_image = "scene_Hostel_Street2[day_suffix]"

    $ hostelStreet3MonicaFromSideSuffix = "2"

    if day_time == "day":
        music street2
    else:
        if rand(1,4) > 1:
            music street_evening3
        else:
            music street13_ambulance
    return
label hostel_street2_init:
    if EP1==True:
        return
    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street2_Monica_[cloth][hostelStreet2MonicaFromSideSuffix][day_suffix]", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Citizen_6", {"type" : 2, "base" : "Hostel_Street2_Citizen_6[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_8", {"type" : 2, "base" : "Hostel_Street2_Citizen_8[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_10", {"type" : 2, "base" : "Hostel_Street2_Citizen_10[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_12", {"type" : 2, "base" : "Hostel_Street2_Citizen_12[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})
    $ add_object_to_scene("Citizen_13", {"type" : 2, "base" : "Hostel_Street2_Citizen_13[day_suffix]", "click" : "citizens_dialogue", "actions" : "lt", "zorder":5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"citizens"})

    $ add_object_to_scene("Teleport_Hostel_Edge_1_c", {"type":3, "text" : t_("УГОЛ ДОМА"), "larrow" : "arrow_left_2", "base":"Hostel_Street2_Teleport_Hostel_Edge_1_c", "click" : "hostel_street2_teleport", "xpos" : 240, "ypos" : 905, "zorder":15, "teleport":True, "high_sprite_hover":True})
    $ add_object_to_scene("Teleport_Hostel_Street3", {"type":3, "text" : t_("БЕДНЫЙ РАЙОН"), "rarrow" : "arrow_right_2", "base":"Hostel_Street2_Teleport_Hostel_Street3", "click" : "hostel_street2_teleport", "xpos" : 1608, "ypos" : 1030, "zorder":15, "teleport":True, "high_sprite_hover":True})

#    $ add_object_to_scene("Teleport_Hostel_Whores_Place", {"type":3, "text" : t_("ПЕРЕКРЕСТОК"), "larrow" : "arrow_down_2_a", "base":"Hostel_Street2_Teleport_Whores_Place", "click" : "hostel_street2_teleport", "xpos" : 560, "ypos" : 978, "zorder":15, "teleport":True, "high_sprite_hover":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street2_teleport:
    if EP1==True:
        jump hostel_street2_teleport_EP1
    if obj_name == "Teleport_Hostel_Edge_1_c":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot") from _call_change_scene_137
            return
        call change_scene("hostel_edge_1_c", "Fade", "highheels_run2") from _call_change_scene_138
        return
    if obj_name == "Teleport_Hostel_Street3":
        if cloth_type == "Nude":
            call change_scene("hostel_street3", "Fade", "snd_walk_barefoot") from _call_change_scene_139
            return
        call change_scene("hostel_street3", "Fade", "highheels_run2") from _call_change_scene_140
        return
    if obj_name == "Teleport_Hostel_Whores_Place":
        if cloth_type == "Nude":
            call change_scene("whores_place", "Fade", "snd_walk_barefoot") from _call_change_scene_141
            return
        call change_scene("whores_place", "Fade", "highheels_run2") from _call_change_scene_142
        return


    return
label hostel_street2_environment:
    if EP1==True:
        jump hostel_street2_environment_EP1

    return






# EP1


label hostel_street2_EP1:
    $ print "enter_hostel_street2"
    $ miniMapData = []

    $ scene_name = "hostel_street2"
    $ sceneIsStreet = True
    $ scene_caption = t_("HOSTEL ENTRANCE")
    $ clear_scene_from_objects(scene_name)


    $ scene_image = "scene_hostel_street2" + day_suffix

    $ add_object_to_scene("Teleport_hostel_reception", {"type":2, "base":"Hostel_Street2_Door", "click" : "hostel_street2_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})
    $ add_object_to_scene("Poster", {"type":2, "base":"Hostel_Street2_Poster", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})
    $ add_object_to_scene("Pipes", {"type":2, "base":"Hostel_Street2_Pipes", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})

#    $ add_object_to_scene("Car", {"type":2, "base":"hostel_street2_Car", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_street2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street2_teleport_EP1:
    if obj_name == "Teleport_Hostel_Street":
        if cloth_type == "Nude":
            call change_scene("hostel_street", "Fade", "snd_walk_barefoot") from _call_change_scene_128
            return
        call change_scene("hostel_street") from _call_change_scene_129
        return
    if obj_name == "Teleport_hostel_reception":
        if act == "l":
            mt "Это вход в хостел..."
        if act == "w":
            if hostelReceptionStage == 0:
                music Stealth_Groover
                $ autorun_to_object("hostel_reception", "hostelAfterJail_dialogue1")
            if hostelReceptionStage > 1:
                music Groove2_85

            call change_scene("hostel_reception", "Fade_long", "snd_jail_door") from _call_change_scene_130
            return
        return
    if obj_name == "Teleport_hostel_street22":
        if act == "l":
            if gameStage == 2 and gameSubStage == 2:
                call hostel_street2_dialogue1() from _call_hostel_street2_dialogue1
                return
        if act == "w":
            $ autorun_to_object("hostel_street22", "hostel_street2_dialogue1")
            call change_scene("hostel_street22") from _call_change_scene_131
            return
    return
label hostel_street2_environment_EP1:
    if obj_name == "Poster":
        if hostelStreetStage == 0:
            mt "Это такая рекламная вывеска отеля?"
            "Они что, пытаются рассмешить меня???"
    if obj_name == "Pipes":
        if hostelStreetStage == 0:
            mt "Это что за канализация?"
            "Надеюсь мне не придется из этого пить там?"
            "Я надеюсь у них хорошая бутилированная вода?"
            "Как может быть иначе?"

    return
