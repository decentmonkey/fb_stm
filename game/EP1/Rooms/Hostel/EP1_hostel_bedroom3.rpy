label EP1_hostel_bedroom3:
    $ print "enter_hostel_bedroom3"
    $ miniMapData = []

    $ scene_name = "hostel_bedroom3"
    $ scene_caption = t_("HOSTEL BEDROOM")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_hostel_bedroom3_Monica_Nude"
    $ EP1_add_object_to_scene("Monica", {"type":2, "base":"hostel_bedroom3_Monica_Nude", "click" : "EP1_hostel_bedroom3_environment", "actions" : "l", "zorder" : 10})

    $ EP1_add_object_to_scene("Cloth", {"type":2, "base":"Hostel_Bedroom3_Cloth", "click" : "EP1_hostel_bedroom3_environment", "actions" : "lh", "zorder" : 0, "b":0.16})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_hostel_bedroom3_teleport(obj_name, obj_data):
    return
label EP1_hostel_bedroom3_environment(obj_name, obj_data):
    if obj_name == "Monica":
        call EP1_hostelAfterJail_bedroom_dialogue6()
        return
    if obj_name == "Cloth":
        if act == "l":
            call EP1_hostelAfterJail_bedroom_dialogue6()
            return
        if act == "h":
            call EP1_hostelAfterJail_bedroom_dialogue7()
            return

    return
