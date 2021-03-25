default hostelBathroomToiletMonicaSuffix = 1

label hostel_bathroom_toilet:
    $ print "enter_hostel_bathroom_toilet"
    $ miniMapData = []

    $ scene_image = "scene_Hostel_Bathroom_Toilet[day_suffix]"
    return

label hostel_bathroom_toilet_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Bathroom_Toilet_Monica_[cloth]_[hostelBathroomToiletMonicaSuffix][day_suffix]", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 10}, scene="hostel_bathroom_toilet")
    $ add_object_to_scene("Toilet", {"type":2, "base":"Hostel_Bathroom_Toilet_Toilet", "click" : "hostel_bathroom_toilet_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_bathroom_toilet")
    $ add_object_to_scene("Teleport_Hostel_Bathroom", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_bathroom_toilet_teleport", "xpos" : 960, "ypos" : 956, "zorder":11,"high_sprite_hover":True}, scene="hostel_bathroom_toilet")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_bathroom_toilet_teleport():
    if obj_name == "Teleport_Hostel_Bathroom":
        call change_scene("hostel_bathroom", "Fade") from _rcall_change_scene_158
        return

    return
label hostel_bathroom_toilet_environment():
    if obj_name == "Toilet":
        if act == "l":
            mt "Жуткий унитаз."
            "Я боюсь прикасаться к нему..."
        if act == "h":
            return
    return
