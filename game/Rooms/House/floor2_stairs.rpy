default floor2StairsBettySuffix = 1

label floor2_stairs:
    $ print "enter_floor2_stairs"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_11

    $ scene_image = "scene_Floor2_Stairs"
    music houseMusic
    return

label floor2_stairs_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Stairs_Monica_[cloth][day_suffix]", "click" : "floor2_stairs_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Flower1", {"type":2, "base":"Floor2_Stairs_Flowers", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor2_Stairs_Lamps", "click" : "floor2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor2_stairs_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА ВНИЗ"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Stairs", "click" : "floor2_stairs_teleport", "xpos" : 735, "ypos" : 331, "zorder":11, "teleport":True})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label floor2_stairs_init2:
    $ add_object_to_scene("Betty", {"type" : 2, "base" : "Floor2_Stairs_Betty[floor2StairsBettySuffix]", "click" : "floor2_stairs_environment", "actions" : "l", "zorder":10}, scene="floor2_stairs")
    return

label floor2_stairs_teleport:
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_96
        return
    if obj_name == "Teleport_Floor1_Stairs":
        call change_scene("floor1_stairs", "Fade_long", "highheels_run2") from _call_change_scene_97
        return
    return

label floor2_stairs_environment:
    if obj_name == "Monica":
        mt "Они ничего не собираются делать с лестницей."
        "Конечно, с какой стати им что-то делать с ней?"
        "У них, очевидно, нет такого вкуса как у меня!"
        "Они счастливы жить в том что создала Я!!!"
        "ЭТО НЕСПРАВЕДЛИВО!!!"
        return
    return
