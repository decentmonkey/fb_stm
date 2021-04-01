default basementBedroomFound = False
default basementBedroomStage = 0
default basementBedroomJournal = True

label EP1_basement_bedroom1:
    $ print "enter_basement_bedroom1"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate() from _ep1call_miniMapHouseGenerate_20

    $ scene_name = "basement_bedroom1"
    $ scene_caption = t_("BASEMENT")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_basement_bedroom1_Monica_" + cloth
    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_" + cloth, "click" : "EP1_basement_bedroom1_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ EP1_add_object_to_scene("Cupboard", {"type":2, "base":"Basement_Bedroom1_Cupboard", "click" : "EP1_basement_bedroom1_environment", "actions" : "lw", "zorder" : 0})
    $ EP1_add_object_to_scene("BasementWardrobe", {"type":2, "base":"Basement_Bedroom1_Wardrobe", "click" : "EP1_basement_bedroom1_environment", "actions" : "lh", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture1", {"type":2, "base":"basement_bedroom1_Picture1", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture2", {"type":2, "base":"basement_bedroom1_Picture2", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture3", {"type":2, "base":"basement_bedroom1_Picture3", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture4", {"type":2, "base":"basement_bedroom1_Picture4", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture5", {"type":2, "base":"basement_bedroom1_Picture5", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture6", {"type":2, "base":"basement_bedroom1_Picture6", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture7", {"type":2, "base":"basement_bedroom1_Picture7", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Table", {"type":2, "base":"basement_bedroom1_Table", "click" : "EP1_basement_bedroom1_environment", "actions" : "lw", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Basement_Hole", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_left_2", "base":"Basement_Bedroom1_Teleport_Hole", "click" : "EP1_basement_bedroom1_teleport", "xpos" : 459, "ypos" : 877, "zorder":11})
    $ EP1_add_object_to_scene("Teleport_Basement_Bedroom2", {"type":3, "text" : t_("КРОВАТЬ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_basement_bedroom1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label EP1_basement_bedroom1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Basement_Hole":
        if basementBedroomStage <= 1:
            mt "У меня нет сил идти никуда..."
            return
        call EP1_change_scene("basement_hole")
        return
    if obj_name == "Teleport_Basement_Bedroom2":
        call EP1_change_scene("basement_bedroom2")
        return
    return

label EP1_basement_bedroom1_environment(obj_name, obj_data):
    if obj_name == "BasementWardrobe":
        if act == "l":
            mt "В этот старый шкаф можно повесить одежду..."
            "Если это можно назвать одеждой..."
        if act == "h":
            call EP1_wardrobeBasement()
            return
        return

    if obj_name == "Monica":
        mt "Видимо это и есть место где я теперь буду спать..."

    if obj_name == "Cupboard":
        if act == "l":
            mt "Старый шкаф..."
        if act == "w":
            $ basementBedroom2CupboardReturnScene = "basement_bedroom1"
            call EP1_change_scene("basement_bedroom2_cupboard")
            return

    if obj_name == "Picture1" or obj_name == "Picture2" or obj_name == "Picture3" or obj_name == "Picture4" or obj_name == "Picture5" or obj_name == "Picture6" or obj_name == "Picture7" or obj_name == "Picture8" or obj_name == "Picture9":
        mt "Живопись..."
        "Я не знала что Юлия увлекается этим."
        "Она пыталась быть похожей на меня?"
        "..."
    if obj_name == "Table":
        if act == "l":
            mt "Этот старый яркий пестрый стол пытается скрасить уныние этой каморки..."
            "Тщетно..."
        if act == "w":
            call EP1_change_scene("basement_bedroom_table")
            return
    return
