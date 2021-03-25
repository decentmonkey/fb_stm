default monicaBathroomForbidden = True

label bathroom_bath:
    $ print "enter_bathroom_bath"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_14

    $ scene_image = "scene_Bathroom_Bath"

#    $ autorun_to_object(scene_name, "afterJailHouse_dialogue10")
    return

label bathroom_bath_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Bath_Monica_[cloth]", "click" : "bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Bath", {"type":2, "base":"Bathroom_Bath_Bath", "click" : "bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "bathroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Bathroom_Shower", {"type":3, "text" : t_("ДУШ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "bathroom_teleport", "xpos" : 1650, "ypos" : 520, "zorder":11, "teleport":True})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label bathroom_teleport:
    if obj_name == "Teleport_Bathroom_Shower":
        call change_scene("bathroom_shower") from _call_change_scene_112
        return
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_113
        return
    if obj_name == "Teleport_Bathroom_Bath":
        call change_scene("bathroom_bath") from _call_change_scene_114
        return

label bathroom_environment:
    if obj_name == "Monica":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться ванной комнатой!"
            return

    if obj_name == "Bath":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться ванной!"
            return

    if obj_name == "Shower":
        if monicaBathroomForbidden == True:
            mt "Эта сучка Бетти запретила мне пользоваться душем!"
            return
    return
