label EP1_floor2_stairs:
    $ print "enter_floor2_stairs"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "floor2_stairs"
    $ scene_caption = "Stairs Top Floor"
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Floor2_Stairs_Monica_" + cloth + day_suffix

    $ monica_tint = [1.0, 1.0, 1.0]
    if (cloth_type == "Lingerie" or cloth_type == "HomeCloth"):
        $ monica_tint = [0.9, 0.9, 1.0]
    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Stairs_Monica_" + cloth, "click" : "EP1_floor2_stairs_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ EP1_add_object_to_scene("Flower1", {"type":2, "base":"Floor2_Stairs_Flowers", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
    if gameStage < 2:
        $ EP1_add_object_to_scene("Sofa", {"type":2, "base":"Floor2_Stairs_Sofa", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Lamps", {"type":2, "base":"Floor2_Stairs_Lamps", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_floor2_stairs_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    $ EP1_add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА ВНИЗ"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Stairs", "click" : "EP1_floor2_stairs_teleport", "xpos" : 735, "ypos" : 331, "zorder":11})
    return

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_floor2_stairs_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor2":
        call EP1_change_scene("floor2")
        return
    if obj_name == "Teleport_Floor1_Stairs":
        call EP1_change_scene("floor1_stairs", "Fade_long", "highheels_run2")
        return
    return

label EP1_floor2_stairs_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Они ничего не собираются делать с лестницей."
            "Конечно, с какой стати им что-то делать с ней?"
            "У них, очевидно, нет такого вкуса как у меня!"
            "Они счастливы жить в том что создала Я!!!"
            "ЭТО НЕСПРАВЕДЛИВО!!!"
            return
        m "Между этажами я перемещаюсь по лестнице."

        "Сейчас модно использовать лифт, но..."

        "Впрочем, можно подумать об этом."
    return
