default hostel_edge_1_a_visited = False

label EP1_hostel_edge_1_a:
    $ print "enter_hostel_edge_1_a"
    $ miniMapData = []

    $ scene_name = "hostel_edge_1_a"
    $ sceneIsStreet = True
    $ scene_caption = t_("BLIND ALLEY")
    $ clear_scene_from_objects(scene_name)

    $ localDaySuffix = ""
    if day_suffix != "":
        $ localDaySuffix = day_suffix + "2"
    $ scene_image = "scene_hostel_edge_1_a" + localDaySuffix
    $ EP1_add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_a_Monica_" + cloth + localDaySuffix, "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 10})

    $ EP1_add_object_to_scene("Bar24", {"type":2, "base":"Hostel_Edge_1_a_Bar24", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13})
    $ EP1_add_object_to_scene("Boxes", {"type":2, "base":"Hostel_Edge_1_a_Boxes", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13})
    $ EP1_add_object_to_scene("Door1", {"type":2, "base":"Hostel_Edge_1_a_Door1", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Door2", {"type":2, "base":"Hostel_Edge_1_a_Door2", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Letters", {"type":2, "base":"Hostel_Edge_1_a_Letters", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13})
    $ EP1_add_object_to_scene("Poster", {"type":2, "base":"Hostel_Edge_1_a_Poster", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13})
    $ EP1_add_object_to_scene("Pylon", {"type":2, "base":"Hostel_Edge_1_a_Pylon", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Trash1", {"type":2, "base":"Hostel_Edge_1_a_Trash1", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Trash2", {"type":2, "base":"Hostel_Edge_1_a_Trash2", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Trash3", {"type":2, "base":"Hostel_Edge_1_a_Trash3", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Trash4", {"type":2, "base":"Hostel_Edge_1_a_Trash4", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Trash5", {"type":2, "base":"Hostel_Edge_1_a_Trash5", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Window1", {"type":2, "base":"Hostel_Edge_1_a_Window1", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Window2", {"type":2, "base":"Hostel_Edge_1_a_Window2", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ EP1_add_object_to_scene("Window3", {"type":2, "base":"Hostel_Edge_1_a_Window3", "click" : "EP1_hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13})
#    $ EP1_add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"hostel_edge_1_a_Teleport_Hostel_Edge_a", "click" : "EP1_hostel_edge_1_a_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8]})

    $ EP1_add_object_to_scene("Teleport_Hostel_1_c", {"type":3, "text" : t_("??????????"), "rarrow" : "arrow_right_2", "base":"Hostel_Edge_1_a_Teleport_Hostel_Edge_C", "click" : "EP1_hostel_edge_1_a_teleport", "xpos" : 1800, "ypos" : 780, "zorder":15})
    $ EP1_add_object_to_scene("Teleport_Hostel_1_b", {"type":3, "text" : t_("???????????? ??????????????"), "larrow" : "arrow_down_2", "base":"Hostel_Edge_1_a_Teleport_Hostel_Edge_B", "click" : "EP1_hostel_edge_1_a_teleport", "xpos" : 550, "ypos" : 933, "zorder":15})

    $ hostel_edge_1_a_visited = True
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_hostel_edge_1_a_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_1_c":
        if cloth_type == "Nude":
            call EP1_change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot")
            return
        call EP1_change_scene("hostel_edge_1_c")
        return
    if obj_name == "Teleport_Hostel_1_b":
        if cloth_type == "Nude":
            call EP1_change_scene("hostel_edge_1_b", "Fade", "snd_walk_barefoot")
            return
        call EP1_change_scene("hostel_edge_1_b")
        return
    return
label EP1_hostel_edge_1_a_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 3 and gameSubStage == 1:
            call EP1_hostelAfterJail_street_dialogue3()
            return
        if hostelStreetStage == 0:
            mt "?????? ?????????????? ?? ??????????."
            "???????? ?????????? ?????? ????????????????."
            "?? ?????? ???????? ???? ??????????!"

    if obj_name == "Bar24":
        mt "??????24?"
        "?????? ?????????????? ???? ????????????-???? ????????."
        "??????????????????????..."
    if obj_name == "Boxes":
        mt "??????????-???? ??????????????..."
        "????????????..."
    if obj_name == "Door1":
        mt "??????????-???? ??????????..."
    if obj_name == "Door2":
        mt "??????????? ?????????"
    if obj_name == "Letters":
        mt "?????????????????????? ?????????? ???? ??????????????..."
    if obj_name == "Poster":
        mt "???????????? ?????????????????????? ????????????..."
    if obj_name == "Pylon":
        mt "?????? ?????????"
        "?????????????"
        "?????????????"
    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5":
        mt "???????????? ??????????..."
    if obj_name == "Window1" or obj_name == "Window2" or obj_name == "Window3":
        mt "???????????????????????? ????????..."

    return
