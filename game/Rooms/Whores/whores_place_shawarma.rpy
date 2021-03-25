
label whores_place_shawarma:
    $ print "enter_whores_place_shawarma"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_5

    $ sceneIsStreet = True
    if kebabWorkInProgress == True:
        $ scene_image = "scene_street_whores_place_shawarma[day_suffix]"
    else:
        $ scene_image = "scene_street_whores_place_shawarma_Kebab[day_suffix]"
    $ whoresPlacePreviousLocation = "shawarma"
    if day_time == "day":
        music street4
    else:
        if rand(1,4) > 1:
            music street_evening1
        else:
            music street13_ambulance
    return

label whores_place_shawarma_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Street_whores_place_shawarma_Monica_[cloth][day_suffix]", "click" : "whores_place_shawarma_environment2", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("Shawarma_Trader", {"type":2, "base":"Street_whores_place_shawarma_Trader[day_suffix]", "click" : "whores_place_shawarma_environment2", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Shawarma_Stall", {"type":2, "base":"Street_whores_place_shawarma_Stall", "click" : "whores_place_shawarma_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_whores_place_shawarma_Street_Fencing1", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_whores_place_shawarma_Street_Fencing2", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Trash_Can", {"type":2, "base":"Street_whores_place_shawarma_Trash_Can", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Fire_Valve", {"type":2, "base":"Street_whores_place_shawarma_Fire_Valve", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Street_whores_place_shawarma_Trash1", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Street_whores_place_shawarma_Trash2", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Street_whores_place_shawarma_Trash3", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Street_whores_place_shawarma_Trash4", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Street_whores_place_shawarma_Trash5", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash6", {"type":2, "base":"Street_whores_place_shawarma_Trash6", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash7", {"type":2, "base":"Street_whores_place_shawarma_Trash7", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash8", {"type":2, "base":"Street_whores_place_shawarma_Trash8", "click" : "whores_place_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Clothing_Shop", {"type":3, "text" : t_("К МАГАЗИНУ ОДЕЖДЫ"), "larrow" : "arrow_down_2", "base":"Street_whores_place_shawarma_Teleport_Clothing_Shop", "click" : "whores_place_shawarma_teleport2", "xpos" : 304, "ypos" : 856, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Street_Hostel", {"type":3, "text" : t_("ПОДВОРОТНЯ"), "larrow" : "arrow_left_2", "base":"Street_whores_place_shawarma_Teleport_Street_Hostel", "click" : "whores_place_shawarma_teleport2", "xpos" : 182, "ypos" : 376, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Whores_Place", {"type":3, "text" : t_("К ПЕРЕКРЕСТКУ"), "rarrow" : "arrow_right_2", "base":"Street_whores_place_shawarma_Teleport_Whores_Place", "click" : "whores_place_shawarma_teleport2", "xpos" : 1375, "ypos" : 1022, "zorder":15, "teleport":True})


    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label whores_place_shawarma_teleport2:
    if obj_name == "Teleport_Clothing_Shop":
        call change_scene("street_cloth_shop", "Fade_long", "highheels_run2") from _call_change_scene_36
        return
    if obj_name == "Teleport_Street_Hostel":
        call change_scene("hostel_street", "Fade", "highheels_run2") from _call_change_scene_37
        return
    if obj_name == "Teleport_Whores_Place":
        call change_scene("whores_place", "Fade", "highheels_run2") from _call_change_scene_38
        return

    return
label whores_place_shawarma_environment2:
    if obj_name == "Monica":
        call hostelAfterJail_street_dialogue3() from _call_hostelAfterJail_street_dialogue3
        return
    if obj_name == "Shawarma_Stall":
        mt "Дешевый ларек, но пахнет оттуда вкусно..."

    if obj_name == "Shawarma_Trader":
        if obj_data["action"] == "l":
            mt "Грязный продавец. Я не выношу даже его вида! Фу!"
        if obj_data["action"] == "t":
            call refresh_scene_fade() from _call_refresh_scene_fade_15
        return
