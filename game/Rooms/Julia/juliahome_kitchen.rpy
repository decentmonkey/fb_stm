default juliaHomeKitchenMonicaSuffix = 1
default juliaHomeKitchenJuliaSuffix = 1

default juliaHomeKitchenSceneSuffix = ""
label juliahome_kitchen:
    $ print "enter_juliahome_kitchen"
    $ miniMapData = []
    call miniMapJuliaHomeGenerate() from _rcall_miniMapJuliaHomeGenerate_2

    $ scene_image = "scene_JuliaHome_Kitchen[juliaHomeKitchenSceneSuffix]"

    if get_active_objects("Julia", scene="juliahome_livingroom") != False and juliaHomeLivingRoomJuliaSuffix != 1 and juliaHomeLivingRoomJuliaSuffix != 2:
        $ set_active("Julia", True, scene="juliahome_kitchen")
    else:
        $ set_active("Julia", False, scene="juliahome_kitchen")

    if day_time == "day":
        music Stealth_Groover
    else:
        music Stealth_Groover
    return

label juliahome_kitchen_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "JuliaHome_Kitchen_Monica_[cloth]_[juliaHomeKitchenMonicaSuffix]", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":10}, scene="juliahome_kitchen")
    $ add_object_to_scene("Julia", {"type" : 2, "base" : "JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth][juliaHomeKitchenJuliaSuffix]", "click" : "juliahome_kitchen_environment", "actions" : "lt", "zorder":10, "active":False}, scene="juliahome_kitchen")

    $ add_object_to_scene("Kitchen_Item1", {"type" : 2, "base" : "JulliaHome_Kitchen_Item1", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Kitchen_Item2", {"type" : 2, "base" : "JulliaHome_Kitchen_Item2", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Kitchen_Item3", {"type" : 2, "base" : "JulliaHome_Kitchen_Item3", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Kitchen_Item4", {"type" : 2, "base" : "JulliaHome_Kitchen_Item4", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Kitchen_Item5", {"type" : 2, "base" : "JulliaHome_Kitchen_Item5", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Picture1", {"type" : 2, "base" : "JulliaHome_Kitchen_Picture1", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Flower1", {"type" : 2, "base" : "JulliaHome_Kitchen_Flower1", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.21, "tint":[1.0, 1.0, 0.7], "group":"environment"}, scene="juliahome_kitchen")
    $ add_object_to_scene("Flower2", {"type" : 2, "base" : "JulliaHome_Kitchen_Flower2", "click" : "juliahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_kitchen")

    $ add_object_to_scene("Teleport_Bathroom", {"type":3, "text" : t_("ВАННАЯ КОМНАТА"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "juliahome_kitchen_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True}, scene="juliahome_kitchen")
    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("СПАЛЬНЯ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "juliahome_kitchen_teleport", "xpos" : 220, "ypos" : 920, "zorder":11, "teleport":True}, scene="juliahome_kitchen")
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "juliahome_kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="juliahome_kitchen")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label juliahome_kitchen_init2:
    $ add_object_to_scene("Kitchen", {"type" : 2, "base" : "JulliaHome_Kitchen_Kitchen", "click" : "juliahome_kitchen_environment", "actions" : "lh", "zorder":-1, "b":0.1, "group":"environment"}, scene="juliahome_kitchen")

    return
label juliahome_kitchen_teleport:
    if obj_name == "Teleport_Street":
        call change_scene("street_juliahome", "Fade", "highheels_run2") from _rcall_change_scene_65
    if obj_name == "Teleport_LivingRoom":
        call change_scene("juliahome_livingroom") from _rcall_change_scene_66
    if obj_name == "Teleport_Bathroom":
        call change_scene("juliahome_bathroom") from _rcall_change_scene_67

    return
label juliahome_kitchen_environment:
    if obj_name == "Monica":
        call ep211_dialogues4_julia_11f() from _rcall_ep211_dialogues4_julia_11f
    if obj_name == "Kitchen_Item1" or obj_name == "Kitchen_Item2" or obj_name == "Kitchen_Item3" or obj_name == "Kitchen_Item4" or obj_name == "Kitchen_Item5":
        call ep211_dialogues4_julia_11g() from _rcall_ep211_dialogues4_julia_11g
    if obj_name == "Picture1":
        call ep211_dialogues4_julia_11b() from _rcall_ep211_dialogues4_julia_11b
    if obj_name == "Flower1" or obj_name == "Flower2":
        call ep211_dialogues4_julia_11d() from _rcall_ep211_dialogues4_julia_11d
    if obj_name == "Kitchen":
        call ep211_dialogues4_julia_11g() from _rcall_ep211_dialogues4_julia_11g_2
    return
