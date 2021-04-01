label street_house_fence:
    $ print "enter_street_house_fence"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_15

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_House_Fence[day_suffix]"
    if day_time == "day":
        music Mandeville
    else:
        music night_ambience
    return

label street_house_fence_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Fence_Monica_[cloth][day_suffix]", "click" : "street_house_fence_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Scratch", {"type":2, "base":"Street_House_Fence_Scratch", "click" : "street_house_fence_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

#    $ add_object_to_scene("Teleport_House_Fence_Scratch", {"type":3, "text" : t_("ЦАРАПИНА"), "rarrow" : "arrow_up_2", "base":"Street_House_Gate_Teleport_Outside", "click" : "street_house_fence_teleport", "xpos" : 638, "ypos" : 564, "zorder":11})
    $ add_object_to_scene("Teleport_House_Yard", {"type":3, "text" : t_("НАЗАД ВО ДВОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_house_fence_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_fence_teleport:
    if obj_name == "Teleport_House_Yard":
        call change_scene("street_house_main_yard") from _call_change_scene_115
        return
    if obj_name == "Teleport_House_Outside":
        call change_scene("street_house_outside") from _call_change_scene_116
        return
    return
label street_house_fence_environment:
    if obj_name == "Monica":
        mt "Я помню эту царапину."
        "Кажется будто это было еще вчера..."
        "Она так и не починена."
        "Эти хозяева недостойны моего дома!"
        "Я верну его назад, клянусь!"
        return
    if obj_name == "Scratch":
        mt "Я помню эту царапину."
        "Кажется будто это было еще вчера..."
        "Она так и не починена."
        "Эти хозяева недостойны моего дома!"
        "Я верну его назад, клянусь!"
        return
    return
