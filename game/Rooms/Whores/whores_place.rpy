#default whoresPlacePreviousLocation = ""
default streetWhoresPlacePerrySuffix = 1
default street_whores_perry_active = False

label whores_place:
    $ print "enter_whores_place"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_1

    $ sceneIsStreet = True

    $ scene_image = "scene_Street_Whores_Place_Whores[day_suffix]"

    $ hostelStreet2MonicaFromSideSuffix = "2"

    if street_whores_perry_active == True:
        if day_time == "day":
            $ set_active("Perry", True)
        else:
            $ set_active("Perry", False)

    if day_time == "day":
        music street1
    else:
        if rand(1,4) > 1:
            music street_evening2
        else:
            music street13_ambulance
    return

label whores_place_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Place_Whores_Monica_[cloth][day_suffix]", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 10}, {"whoresPlacePreviousLocation":{"v":"shawarma", "base":"Street_Whores_Place_Whores_Monica_[cloth]2[day_suffix]"}})

    $ add_object_to_scene("Mommy", {"type":2, "base":"Street_Whores_Place_Mommy[day_suffix]", "click" : "whores_place_environment2", "actions" : "lt", "zorder" : 5})
    $ add_object_to_scene("GrayMouse2", {"type":2, "base":"Street_Whores_Place_GrayMouse2[day_suffix]", "click" : "whores_place_environment2", "actions" : "lt", "zorder" : 5})

    $ add_object_to_scene("Whore1", {"type":2, "base":"Street_Whores_Place_Whores_Whore1b[day_suffix]", "click" : "whores_place_environment2", "actions" : "lt", "zorder" : 5})

    $ add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_Whores_Place_Fencing1", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_Whores_Place_Fencing2", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Trash_Can", {"type":2, "base":"Street_Whores_Place_Trash_Can", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Street_Whores_Place_Trash1", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Street_Whores_Place_Trash2", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Street_Whores_Place_Trash3", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Street_Whores_Place_Trash4", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Street_Whores_Place_Trash5", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash6", {"type":2, "base":"Street_Whores_Place_Trash6", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : t_("ВНИЗ ПО УЛИЦЕ"), "larrow" : "arrow_left_2", "base":"Street_Whores_Place_Teleport_Shawarma", "click" : "whores_place_teleport2", "xpos" : 195, "ypos" : 778, "zorder":15, "teleport":True})
#    $ add_object_to_scene("Teleport_Hostel_Street2", {"type":3, "text" : t_("ГРЯЗНАЯ УЛИЦА"), "rarrow" : "arrow_right_2", "base":"Street_Whores_Place_Teleport_Hostel_Street2", "click" : "whores_place_teleport2", "xpos" : 1642, "ypos" : 218, "zorder":15, "teleport":True})
#    $ add_object_to_scene("Teleport_Street1", {"type":3, "text" : t_("ВВЕРХ ПО УЛИЦЕ"), "rarrow" : "arrow_right_2", "base":"Street_Whores_Place_Teleport_Street1", "click" : "whores_place_teleport2", "xpos" : 1497, "ypos" : 882, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Street1", {"type":3, "text" : t_("ВВЕРХ ПО УЛИЦЕ"), "rarrow" : "arrow_right_2", "base":"Street_Whores_Place_Teleport_Hostel_Street2", "click" : "whores_place_teleport2", "xpos" : 1542, "ypos" : 238, "zorder":15, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3
label whores_place_init2:
    $ add_object_to_scene("Perry", {"type":2, "base":"Street_Whores_Place_Perry_[streetWhoresPlacePerrySuffix]", "click" : "whores_place_environment2", "actions" : "lw", "zorder" : 5}, scene="whores_place")
    return

label whores_place_teleport2:
    if obj_name == "Teleport_Street1":
        call change_scene("whores_place_street1", "Fade", "highheels_run2") from _call_change_scene_7
        return
    if obj_name == "Teleport_Shawarma":
        call change_scene("whores_place_shawarma", "Fade", "highheels_run2") from _call_change_scene_8
        return
    if obj_name == "Teleport_Hostel_Street2":
        call change_scene("hostel_street2", "Fade", "highheels_run2") from _call_change_scene_9
        return
    return
label whores_place_environment2:
    if obj_name == "Monica":
        "Проститутки..."
        "Фу..."
    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5" or obj_name == "Trash6" or obj_name == "Trash7" or obj_name == "Trash8":
        mt "О Боже!!!"
        "ГДЕ Я???"
        "Это же настоящая помойка!"
        "Не в переносном смысле, а в прямом!!!"

    if obj_name == "Mommy":
        if obj_data["action"] == "l":
            mt "Судя по всему, это их мамочка."
            "Помогает им продавать свои тела...
            За бесценок..."
        if obj_data["action"] == "t":
            mt "Я не собираюсь разговаривать с этой отвратительной мамочкой!!"
    if obj_name == "Whore1":
        if obj_data["action"] == "l":
            mt "Обычная уличная проститутка..."
            "Самая дешевая..."
            "Они обычно все так одеваются."
            "По крайней мере, как я видела в кино."
            "Я не могу смотреть на это без отвращения!"
        if obj_data["action"] == "t":
            mt "Я не собираюсь общаться с со шлюхами."
            "Я что, ненормальная?"
            if kebabWorkInProgress == True:
                mt "Тем более в таком виде!"
                "Ужас!"
    if obj_name == "GrayMouse2":
        if obj_data["action"] == "l":
            mt "Я знаю эту проститутку."
            "О Боже! Моника!"
            "ТЫ!!!"
            "ЗНАЕШЬ!!!"
            "ПРОСТИТУТКУ!!!"
            "Я не верю в это."
        if obj_data["action"] == "t":
            mt "Я не собираюсь общаться с со шлюхами."
            "Я что, ненормальная?"
            if kebabWorkInProgress == True:
                mt "Тем более в таком виде!"
                "Ужас!"

    return
