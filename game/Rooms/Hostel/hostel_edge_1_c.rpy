default hostelWalkStreetEnabled = False
default localDaySuffix = ""

label hostel_edge_1_c:
    $ print "enter_hostel_edge_1_c"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_7

    $ sceneIsStreet = True

    $ localDaySuffix = ""
    if day_suffix != "":
        $ localDaySuffix = day_suffix + "2"
    $ scene_image = "scene_Hostel_Edge_1_c[localDaySuffix]"

    $ hostelStreet2MonicaFromSideSuffix = "2"

    if rand(1,4) > 1:
        music street_evening1
    else:
        music street13_ambulance

    return

label hostel_edge_1_c_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_c_Monica_[cloth][localDaySuffix]", "click" : "hostel_edge_1_c_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"Hostel_Edge_1_c_Teleport_Hostel_Edge_a", "click" : "hostel_edge_1_c_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8], "teleport":True})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : t_("К ХОСТЕЛУ"), "larrow" : "arrow_up_2", "base":"Hostel_Edge_1_c_Teleport_Hostel_Street", "click" : "hostel_edge_1_c_teleport", "xpos" : 1683, "ypos" : 330, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Walk_Street", {"type":3, "text" : t_("ГУЛЯТЬ ПО УЛИЦЕ"), "larrow" : "arrow_down_2", "base":"Hostel_Edge_1_c_Teleport_Walk_Streets", "click" : "hostel_edge_1_c_teleport", "xpos" : 1528, "ypos" : 920, "zorder":15, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_edge_1_c_teleport:
    if obj_name == "Teleport_Hostel_Street":
        if cloth_type == "Nude":
            call change_scene("hostel_street", "Fade", "snd_walk_barefoot") from _call_change_scene_52
            return
        call change_scene("hostel_street", "Fade", "highheels_run2") from _call_change_scene_53
        return
    if obj_name == "Teleport_Walk_Street":
        if cloth_type == "Nude":
            call change_scene("hostel_street2", "Fade", "snd_walk_barefoot") from _call_change_scene_54
            return
        call change_scene("hostel_street2", "Fade", "highheels_run2") from _call_change_scene_57
        return
    if obj_name == "Teleport_Hostel_1_a":
        if act == "l":
            if gameStage == 3 and gameSubStage == 0:
                mt "Этот двор, тупик."
                "Он какой-то жуткий..."
                "Но здесь я могу одеться!"
                return

            if hostelStreetStage == 0:
                mt "Этот двор, тупик."
                "Он какой-то жуткий..."
                return
        if act == "w":
            if gameStage == 3 and gameSubStage == 0:
                call hostelAfterJail_street_dialogue4() from _call_hostelAfterJail_street_dialogue4
                return
            if gameStage == 2:
                $ autorun_to_object("hostel_edge_1_a", "hostel_edge_1_a_dialogue1")
            if cloth_type == "Nude":
                call change_scene("hostel_edge_1_a", "Fade", "snd_walk_barefoot") from _call_change_scene_58
                return
            call change_scene("hostel_edge_1_a") from _call_change_scene_59
            return
    return
label hostel_edge_1_c_environment:
    if obj_name == "Monica":
        pass

    return
