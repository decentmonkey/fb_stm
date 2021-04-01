default basementBedroom1MonicaSuffix = 2
default basementBedroomBettyPantiesOnly = False

label basement_bedroom1:
    $ print "enter_basement_bedroom1"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_9

    $ scene_image = "scene_basement_bedroom1"

    $ basementHoleIncomingDirection = "Bedroom"

    $ basementBedroomBettyPantiesOnly = False
    if cloth == "GovernessPants" and monicaBettyPanties == True:
        $ basementBedroomBettyPantiesOnly = True
    return

label basement_bedroom1_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[cloth]_[basementBedroom1MonicaSuffix]", "click" : "basement_bedroom1_environment", "actions" : "l", "zorder":10, "tint": [1.0, 1.0, 0.9]}, {"basementBedroomBettyPantiesOnly":{"v":True, "base":"Basement_Bedroom1_Monica_Governess_Betty_[monicaBettyPantiesId]", "img_overlay":"Basement_Bedroom1_Monica_GovernessPants_2_Overlay"}}, scene="basement_bedroom1")

    $ add_object_to_scene("Cupboard", {"type":2, "base":"Basement_Bedroom1_Cupboard", "click" : "basement_bedroom1_environment", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("BasementWardrobe", {"type":2, "base":"Basement_Bedroom1_Wardrobe", "click" : "basement_bedroom1_environment", "actions" : "lh", "zorder" : 0}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture1", {"type":2, "base":"basement_bedroom1_Picture1", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture2", {"type":2, "base":"basement_bedroom1_Picture2", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture3", {"type":2, "base":"basement_bedroom1_Picture3", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture4", {"type":2, "base":"basement_bedroom1_Picture4", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture5", {"type":2, "base":"basement_bedroom1_Picture5", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture6", {"type":2, "base":"basement_bedroom1_Picture6", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Picture7", {"type":2, "base":"basement_bedroom1_Picture7", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")
    $ add_object_to_scene("Table", {"type":2, "base":"basement_bedroom1_Table", "click" : "basement_bedroom1_environment", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="basement_bedroom1")

    $ add_object_to_scene("Teleport_Basement_Hole", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_left_2", "base":"Basement_Bedroom1_Teleport_Hole", "click" : "basement_bedroom1_teleport", "xpos" : 459, "ypos" : 877, "zorder":11, "teleport":True}, scene="basement_bedroom1")
    $ add_object_to_scene("Teleport_Basement_Bedroom2", {"type":3, "text" : t_("КРОВАТЬ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover":True}, scene="basement_bedroom1")

    return

label basement_bedroom1_teleport:
    if obj_name == "Teleport_Basement_Hole":
        call change_scene("basement_hole") from _call_change_scene_87
        return
    if obj_name == "Teleport_Basement_Bedroom2":
        if cloth == "Nude":
            call change_scene("basement_bedroom2", "Fade", "snd_walk_barefoot") from _rcall_change_scene_180
            return
        call change_scene("basement_bedroom2") from _call_change_scene_88
        return
    return

label basement_bedroom1_environment:
    if obj_name == "BasementWardrobe":
        if act == "l":
            mt "В этот старый шкаф можно повесить одежду..."
            "Если это можно назвать одеждой..."
        if act == "h":
            call wardrobeBasement() from _call_wardrobeBasement
            return
        return

    if obj_name == "Monica":
        mt "Здесь я теперь сплю..."
        "(хмык)"
        "Но это временно!!!"
        "Это какое-то недоразумение, которое скоро разрешится!"

    if obj_name == "Cupboard":
        if act == "l":
            mt "Старый шкаф..."
        if act == "w":
            $ basementBedroom2CupboardReturnScene = "basement_bedroom1"
            call change_scene("basement_bedroom2_cupboard") from _call_change_scene_89
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
            call change_scene("basement_bedroom_table") from _call_change_scene_90
            return
    return
