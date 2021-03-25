label bedroom2:
    $ print "enter_bedroom2"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_23

    $ scene_image = "scene_Bedroom2[day_suffix]"
    music Mandeville

#    if gameStage > 2:
#        if scene_name != lastSceneName and lastSceneName != "bedroom1":
#            $ autorun_to_object(scene_name, "afterJailHouse_dialogue16a")
    return

label bedroom2_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_[cloth][day_suffix]", "click" : "bedroom2_environment", "actions" : "l", "zorder":10}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom2_Monica_[cloth]_Cleaning_[monicaCleaningObject]"}})

    $ add_object_to_scene("Mess", {"type":2, "base":"Bedroom2_Mess", "click" : "bedroom1_environment", "actions" : "l", "group":"environment"})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Bedroom2_Chair", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Table", {"type":2, "base":"Bedroom2_Table", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Table2", {"type":2, "base":"Bedroom2_Table2", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture", {"type":2, "base":"Bedroom2_Picture", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type":2, "base":"Bedroom2_Windows", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "c":1.0, "b":0.1, "group":"environment"})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Bedroom2_Curtains", "click" : "bedroom1_environment", "actions" : "l", "zorder" : -1, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom2_Curtains_Dust"}})
    $ add_object_to_scene("Carpet", {"type":2, "base":"Bedroom2_Carpet", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Wardrobe", {"type":2, "base":"Bedroom2_Wardrobe", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom2_Wardrobe_Dust"}})

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3
    $ add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : t_("КРОВАТЬ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "bedroom2_teleport", "xpos" : 220, "ypos" : 545, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "rarrow" : "arrow_right_2", "base":"Bedroom2_Teleport_Floor2", "click" : "bedroom2_teleport", "xpos" : 1330, "ypos" : 1005, "zorder":11, "teleport":True})

    return
#    jump show_scene

label bedroom2_teleport:
    if obj_name == "Teleport_Bedroom1":
        call change_scene("bedroom1") from _call_change_scene_176
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_177
    return

label bedroom2_environment:
    if obj_name == "Monica":
        mt "Моя спальня..."
        "Я скучаю по ней!"
        "ОНА МОЯ!!!"
        "НЕНАВИЖУ!!!"
        "Как такое могло случиться???"
        if get_active_objects("Betty") != False:
            mt "А теперь на моей кровати лежит эта жирная корова!"
            "А я вынуждена смотреть на это и выполнять все ее капризы!"
            "(хмык)"

    if obj_name == "Table2":
        mt "Мой любимый маленький столик..."
        return
    if obj_name == "Picture":
        mt "Масляная живопись."
        "Так и висит..."
        return
    if obj_name == "Wardrobe":
        mt "Мой любимый гардеробный шкаф..."
        "Сейчас там висят тряпки ненавистной Бетти!"
        "НЕНАВИЖУ!!!"
    return
