label EP1_bedroom2:
    $ print "enter_bedroom2"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()
    $ miniMapSubst["all"] = "miniMapBedroomCheckCloth"

    $ scene_name = "bedroom2"
    $ scene_caption = t_("Bedroom")
    $ scene_image = "scene_Bedroom2_Monica_" + cloth + day_suffix

    $ monica_tint = [1.0, 1.0, 1.0]
    if gameStage <= 2:
        if (cloth_type == "Lingerie" or cloth_type == "HomeCloth"):
            $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_" + cloth, "click" : "EP1_monica_show_cloth", "actions" : "l", "zorder":10, "tint": [0.9, 0.9, 1.0]})
        else:
            $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_" + cloth, "click" : "EP1_monica_show_cloth", "actions" : "l", "zorder":10})
    if gameStage > 2:
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_" + cloth, "click" : "EP1_bedroom2_environment", "actions" : "l", "zorder":10})

    $ EP1_add_object_to_scene("Mess", {"type":2, "base":"Bedroom2_Mess", "click" : "EP1_bedroom1_environment", "actions" : "l"})
    $ EP1_add_object_to_scene("Chair2", {"type":2, "base":"Bedroom2_Chair", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Table", {"type":2, "base":"Bedroom2_Table", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Table2", {"type":2, "base":"Bedroom2_Table2", "click" : "EP1_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture", {"type":2, "base":"Bedroom2_Picture", "click" : "EP1_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Windows", {"type":2, "base":"Bedroom2_Windows", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0, "c":1.0, "b":0.1})
    $ EP1_add_object_to_scene("Curtains", {"type":2, "base":"Bedroom2_Curtains", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : -1})
    $ EP1_add_object_to_scene("Carpet", {"type":2, "base":"Bedroom2_Carpet", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})

    if gameStage <= 2:
        $ EP1_add_object_to_scene("Wardrobe", {"type":2, "base":"Bedroom2_Wardrobe", "click" : "EP1_wardrobe", "actions" : "lh", "zorder" : 0})
    if gameStage > 2:
        $ EP1_add_object_to_scene("Wardrobe", {"type":2, "base":"Bedroom2_Wardrobe", "click" : "EP1_bedroom2_environment", "actions" : "l", "zorder" : 0})

#    $ EP1_add_object_to_scene("Chair", {"type":2, "base":"Bedroom2_Chair", "click" : "EP1_bedroom2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3
    $ EP1_add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : t_("КРОВАТЬ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "EP1_bedroom2_teleport", "xpos" : 220, "ypos" : 545, "zorder":11})
    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "rarrow" : "arrow_right_2", "base":"Bedroom2_Teleport_Floor2", "click" : "EP1_bedroom2_teleport", "xpos" : 1330, "ypos" : 1005, "zorder":11})


    if gameStage > 2:
        if scene_name != lastSceneName and lastSceneName != "bedroom1":
            $ EP1_autorun_to_object(scene_name, "afterJailHouse_dialogue16a")

#    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("HALL"), "rarrow" : "arrow_right_2", "base":"Bedroom2_Teleport_Floor2", "click" : "EP1_bedroom2_teleport", "xpos" : 1310, "ypos" : 1005, "zorder":11, "b":0.4, "s":0.0, "c":1.0, "tint":[0.90625, 0.69140625, 0.19140625]})
#    $ renpy.pause(10.0, hard=True)

    return
#    jump EP1_show_scene

label EP1_bedroom2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bedroom1":
        call EP1_change_scene("bedroom1")
    if obj_name == "Teleport_Floor2":
        if cloth_type == "Lingerie":
            call EP1_monica_show_lingerie_image
            m "В доме прислуга. Я не хотела бы появляться на виду в нижнем белье."
            w
            return
        $ miniMapSubst["all"] = False
        call EP1_change_scene("floor2")

    return

label EP1_bedroom2_environment(name, obj_data):
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Моя спальня..."
            "Я скучаю по ней!"
            "ОНА МОЯ!!!"
            "НЕНАВИЖУ!!!"
            "Как такое могло случиться???"

    if obj_name == "Table2":
        if gameStage > 2:
            mt "Мой любимый маленький столик..."
            return
        m "Этот маленький столик я использую для фотографий и разной другой ерунды."

        "Использовать косметику я предпочитаю в холле около спальни."

    if obj_name == "Picture":
        if gameStage > 2:
            mt "Масляная живопись."
            "Так и висит..."
            return

        "Я люблю картины.
        Я ценитель."

        "Хотя в последнее время я предпочитаю пастельные тона."

    if obj_name == "Wardrobe":
        mt "Мой любимый гардеробный шкаф..."
        "Сейчас там висят тряпки ненавистной Бетти!"
        "НЕНАВИЖУ!!!"
    return

label EP1_miniMapBedroomCheckCloth:
    if cloth_type == "Lingerie":
        call EP1_monica_show_lingerie_image
        m "В доме прислуга. Я не хотела бы появляться на виду в нижнем белье."
        w
        return False
    $ miniMapSubst["all"] = False
    return True
#вестибюль, холл, фойе
