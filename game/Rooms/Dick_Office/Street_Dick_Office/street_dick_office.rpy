label street_dick_office:

    $ print "enter_street_dick_office"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Dick_Office[day_suffix]"
    if day_time == "day":
        music street9
    else:
        music street_evening2
    return

label street_dick_office_init:
    $ add_object_to_scene("Building", {"type":2, "base":"Street_Dick_Office_Building", "click" : "street_dick_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Dick_Office_Building_Enter" + day_suffix, "click" : "street_dick_office_teleport", "actions" : "lw", "zorder" : 0, "b":0.2, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_dick_office_teleport:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Вход в офисное здание где заседает Дик..."
            return
        if obj_data["action"] == "w":
#            mt "У меня нет галстука для Дика, что мне там делать... (хмык)"
#            return
            $ dickReceptionMonicaSuffix = 1
            call change_scene("dick_office_entrance") from _call_change_scene_162
            return
    return
label street_dick_office_environment:
    if obj_name == "Building":
        m "В этом офисном здании заседает Дик."
        "Оно такое же мрачное, как и его работа."
        "И такое же скучное, как он сам!"
    return
