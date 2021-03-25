default monicaHomeKitchenMonicaSuffix = 1
default monicaHomeKitchenSceneSuffix = ""
label monicahome_kitchen:
    $ print "enter_monicahome_kitchen"
    $ miniMapData = []
    call miniMapSlumsApartmentsGenerate() from _rcall_miniMapSlumsApartmentsGenerate_2
    $ scene_image = "scene_MonicaHome_Kitchen[monicaHomeKitchenSceneSuffix]"

    if day_time == "day":
        music Mandeville
    else:
        music street13_ambulance

    $ monicaHomeLivingRoomMonicaSuffix = 1
    $ monicaHomeBathroomMonicaSuffix = 1
    return

label monicahome_kitchen_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "MonicaHome_Kitchen_Monica_[cloth]_[monicaHomeKitchenMonicaSuffix]", "click" : "monicahome_kitchen_environment", "actions" : "l", "zorder":10}, scene="monicahome_kitchen")

    $ add_object_to_scene("Kitchen_Items1", {"type" : 2, "base" : "MonicaHome_Kitchen_Items1", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")
    $ add_object_to_scene("Kitchen_Items2", {"type" : 2, "base" : "MonicaHome_Kitchen_Items2", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")
    $ add_object_to_scene("Kitchen_Items3", {"type" : 2, "base" : "MonicaHome_Kitchen_Items3", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")
    $ add_object_to_scene("Kitchen_Items4", {"type" : 2, "base" : "MonicaHome_Kitchen_Items4", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")
    $ add_object_to_scene("Kitchen_Items5", {"type" : 2, "base" : "MonicaHome_Kitchen_Items5", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")
    $ add_object_to_scene("Kitchen_Items6", {"type" : 2, "base" : "MonicaHome_Kitchen_Items6", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")

    $ add_object_to_scene("Kitchen_Table1", {"type" : 2, "base" : "MonicaHome_Kitchen_Table1", "click" : "monicahome_kitchen_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")
    $ add_object_to_scene("Kitchen_Towel1", {"type" : 2, "base" : "MonicaHome_Kitchen_Towel1", "click" : "monicahome_kitchen_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_kitchen")

    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("СПАЛЬНЯ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monicahome_kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="monicahome_kitchen")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monicahome_kitchen_teleport:
    if obj_name == "Teleport_LivingRoom":
        call change_scene("monicahome_livingroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_47
        return
    return
label monicahome_kitchen_environment:
    if obj_name == "Monica":
        call ep211_dialogues6_slum_apartment_8f() from _rcall_ep211_dialogues6_slum_apartment_8f
    if obj_name == "Kitchen_Items1" or obj_name == "Kitchen_Items2" or obj_name == "Kitchen_Items3" or obj_name == "Kitchen_Items4" or obj_name == "Kitchen_Items5" or obj_name == "Kitchen_Items6":
        call ep211_dialogues6_slum_apartment_8g() from _rcall_ep211_dialogues6_slum_apartment_8g
    if obj_name == "Kitchen_Towel1":
        call ep211_dialogues6_slum_apartment_8g() from _rcall_ep211_dialogues6_slum_apartment_8g_1
    if obj_name == "Kitchen_Table1":
        if act=="l":
            call ep211_dialogues6_slum_apartment_30() from _rcall_ep211_dialogues6_slum_apartment_30
            return
        return
    return
