label EP1_floor1_stairs:
    $ print "enter_floor1_stairs"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "floor1_stairs"
    $ scene_caption = "Stairs Ground Floor"
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Floor1_Stairs_Monica_" + cloth + day_suffix

    $ monica_tint = [1.0, 1.0, 1.0]
    if (cloth_type == "Lingerie" or cloth_type == "HomeCloth"):
        $ monica_tint = [0.9, 0.9, 1.0]
    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Floor1_Stairs_Monica_" + cloth, "click" : "EP1_floor1_stairs_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ EP1_add_object_to_scene("Flower", {"type":2, "base":"Floor1_Stairs_Flower", "click" : "EP1_floor1_stairs_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Stairs_Furniture", "click" : "EP1_floor1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Stairs_Lamps", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Basement_Pool", {"type":3, "text" : t_("ЛЕСТНИЦА В ПОДВАЛ"), "rarrow" : "arrow_down_2", "base":"Floor1_Stairs_StairsDown", "click" : "EP1_floor1_stairs_teleport", "xpos" : 635, "ypos" : 365, "zorder":9})

    if bardieLocation == "Floor1_Stairs":
        $ scene_image = "scene_Floor1_Stairs_Bardie" + day_suffix
        $ EP1_add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Stairs_Bardie" + day_suffix, "click" : "EP1_bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ EP1_add_object_to_scene("Teleport_Basement_Pool", {"type":3, "text" : t_("ЛЕСТНИЦА В ПОДВАЛ"), "rarrow" : "arrow_down_2", "base":"Floor1_Stairs_StairsDown", "click" : "EP1_floor1_stairs_teleport", "xpos" : 535, "ypos" : 365, "zorder":9})


    $ EP1_add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_floor1_stairs_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    $ EP1_add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА ВВЕРХ"), "rarrow" : "arrow_up_2", "base":"Floor1_Stairs_StairsUp", "click" : "EP1_floor1_stairs_teleport", "xpos" : 857, "ypos" : 250, "zorder":9})
    return

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_floor1_stairs_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor2_Stairs":
        call EP1_change_scene("floor2_stairs", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Basement_Pool":
        if notWantToBasement == True:
            m "Эта лестница ведет в подвал.
            Что я там забыла?"
            menu:
                "Все-равно идти вниз по лестнице.":
                    wc
                    call EP1_change_scene("basement_pool", "Fade_long", "highheels_run2")
                    return
                "Не идти туда.":
                    m "Вот и правильно!
                    Нечего мне шляться по всяким подвалам!"
                    return
        if juliaBasementWarningActive == True:
            call EP1_julia_scene_basement1_monica_warning()
        call EP1_change_scene("basement_pool")
        return
    if obj_name == "Teleport_Floor1":
        call EP1_change_scene("floor1")
        return
    return

label EP1_floor1_stairs_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Они ничего не собираются делать с лестницей."
            "Конечно, с какой стати им что-то делать с ней?"
            "У них, очевидно, нет такого вкуса как у меня!"
            "Они счастливы жить в том что создала Я!!!"
            "ЭТО НЕСПРАВЕДЛИВО!!!"
            return
        m "Я сама утверждала дизайн этой лестницы."

        "Поэтому она такая красивая.

        Прямо как Я."

    if obj_name == "Flower":
        if gameStage > 2:
            mt "Это мои цветы!"
            "МОИ!!!"
            return
        m "Цветы - лучшее украшение интерьера."

    return
