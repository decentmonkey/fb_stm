label basement_pool:
    $ print "enter_basement_pool"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_6

    $ scene_image = "scene_Basement_Pool"
    music Mandeville
    return

label basement_pool_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Pool_Monica_[cloth]", "click" : "basement_pool_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Bidet", {"type":2, "base":"Basement_Pool_Bidet_b", "click" : "basement_toilet_interact", "actions" : "lh", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Mat", {"type":2, "base":"Basement_Pool_Mat_b", "click" : "basement_pool_environment", "actions" : "l", "zorder" : 0, "b": 0.15, "s":1.1, "group":"environment"})
    $ add_object_to_scene("Rags", {"type":2, "base":"Basement_Pool_Rags_b", "click" : "basement_pool_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Shower_Cabin", {"type":2, "base":"Basement_Pool_Shower_Cabin_b", "click" : "basement_shower_interact", "actions" : "lh", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Pool_Water", {"type":2, "base":"Basement_Pool_Water_b", "click" : "basement_pool_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Basement_Pool_Lamps_b", "click" : "basement_pool_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Basement_Pool_Door1_b", "click" : "basement_pool_teleport", "xpos" : 1043, "ypos" : 173, "zorder":0, "tint": [1.0, 1.0, 0.6], "teleport":True})
    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("ПРАЧЕЧНАЯ"), "larrow" : "arrow_left_2", "base":"Basement_Pool_Door2_b", "click" : "basement_pool_teleport", "xpos" : 1561, "ypos" : 408, "zorder":0, "tint": [1.0, 1.0, 0.6], "teleport":True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label basement_pool_teleport:
    if obj_name == "Teleport_Floor1_Stairs":
        call change_scene("floor1_stairs", "Fade_long", "highheels_run2") from _call_change_scene_71
        return
    if obj_name == "Teleport_Basement_Laundry":
        call change_scene("basement_laundry") from _call_change_scene_72
        return
    return

label basement_pool_environment:
    if obj_name == "Monica":
        call basement_shower_check() from _call_basement_shower_check
        return
#        m "Насколько помню, здесь одна дверь ведет назад в дом, а вторая в прачечную."

    if obj_name == "Lamps":
        mt "Здесь не бывает настоящего солнца... "
        return
#    if obj_name == "Bidet":
#        if monicaBathroomForbidden == True:
#            mt "Бетти запретила мне пользоваться ванной наверху."
#            "Может быть мне можно пользоваться туалетом здесь?"
#            "Но я сейчас не хочу..."
#        return

    if obj_name == "Mat":
        mt "Какой-то неприятный коврик."
        return

    if obj_name == "Rags":
        mt "Какие-то полотенца..."
        return

#    if obj_name == "Shower_Cabin":
#        if monicaBathroomForbidden == True:
#            mt "Бетти запретила мне пользоваться ванной наверху."
#            "Может быть мне можно пользоваться душем здесь?"
#            return

    if obj_name == "Pool_Water":
        mt "Вот и бассейн.
        Не понимаю зачем он нужен здесь."
        return
    return
