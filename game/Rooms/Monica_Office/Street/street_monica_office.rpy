label street_monica_office:
    $ print "enter_street_monica_office"
    $ miniMapData = []

    $ sceneIsStreet = True

    $ scene_image = "scene_Street_Monica_Office[day_suffix]"
    if day_time == "day":
        music street9
    else:
        music street_evening1
    return

label street_monica_office_init:

    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Monica_Office_Teleport_Inside", "click" : "street_monica_office_teleport2", "actions" : "lw", "zorder" : 0})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_monica_office_teleport2:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Это здание принадлежит моей компании."
            "Вернее принадлежало..."
            "(хмык)"
            "Но я верну все назад!"
            "Клянусь!"
            "Мне просто надо немного времени!"
        if obj_data["action"] == "w":
            music Stealth_Groover
            call change_scene("monica_office_entrance", "Fade_long", "highheels_run2") from _call_change_scene_98
            return
    return
label street_monica_office_environment2:
    return
