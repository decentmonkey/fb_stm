default street_house_neighbour_betty_suffix = 1
default street_house_neighbour_monica_suffix = 1
default street_house_neighbour_neighbour_suffix = 1

label street_house_neighbour:
    $ print "enter_street_house_neighbour"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Neighbour[day_suffix]"

    music night_ambience
    return

label street_house_neighbour_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Neighbour", {"type" : 2, "base" : "Street_Neighbour_Neighbour_[street_house_neighbour_neighbour_suffix][day_suffix]", "click" : "street_house_neighbour_environment", "actions" : "lw", "zorder":10, "tint": monica_tint}, scene="street_house_neighbour")
    $ add_object_to_scene("Betty", {"type" : 2, "base" : "Street_Neighbour_Betty_[street_house_neighbour_betty_suffix][day_suffix]", "click" : "street_house_neighbour_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="street_house_neighbour")
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Outside_Monica_[cloth]_[street_house_neighbour_monica_suffix][day_suffix]", "click" : "street_house_neighbour_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="street_house_neighbour")

    $ add_object_to_scene("Door", {"type" : 2, "base" : "Street_Neighbour_Door", "click" : "street_house_neighbour_environment", "actions" : "lw", "zorder":2, "tint":[1.0, 1.0, 0.85]}, scene="street_house_neighbour")

    $ add_object_to_scene("Teleport_House_Neighbour_Farm", {"type":3, "text" : t_("ФЕРМА СОСЕДА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "street_house_neighbour_teleport", "xpos" : 350, "ypos" : 790, "zorder":11, "teleport":True, "house_out_teleport":True}, scene="street_house_neighbour")
    $ add_object_to_scene("Teleport_House_Outside", {"type":3, "text" : t_("НАЗАД К ДОМУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_house_neighbour_teleport", "xpos" : 1260, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="street_house_neighbour")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_neighbour_teleport:
    if obj_name == "Teleport_House_Outside":
        call change_scene("street_house_outside") from _rcall_change_scene_182
        return
    return
label street_house_neighbour_environment:
    return
