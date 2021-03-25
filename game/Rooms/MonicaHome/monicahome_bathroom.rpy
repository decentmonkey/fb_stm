default monicaHomeBathroomMonicaSuffix = 1
default monicaHomeBathroomMonicaSuffix2 = ""
default monicaHomeBathroomSceneSuffix = ""
label monicahome_bathroom:
    $ print "enter_monicahome_bathroom"
    $ miniMapData = []
    call miniMapSlumsApartmentsGenerate() from _rcall_miniMapSlumsApartmentsGenerate_1
    $ scene_image = "scene_MonicaHome_Bathroom[monicaHomeBathroomSceneSuffix]"

    if day_time == "day":
        music Mandeville
    else:
        music street13_ambulance

    $ monicaHomeLivingRoomMonicaSuffix = 2
    return

label monicahome_bathroom_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "MonicaHome_Bathroom_Monica_[cloth]_[monicaHomeBathroomMonicaSuffix][monicaHomeBathroomMonicaSuffix2]", "click" : "monicahome_bathroom_environment", "actions" : "l", "zorder":10}, scene="monicahome_bathroom")

    $ add_object_to_scene("Boxes", {"type" : 2, "base" : "MonicaHome_Bathroom_Boxes", "click" : "monicahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_bathroom")
    $ add_object_to_scene("Mirror", {"type" : 2, "base" : "MonicaHome_Bathroom_Mirror", "click" : "monicahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_bathroom")
    $ add_object_to_scene("Shower", {"type" : 2, "base" : "MonicaHome_Bathroom_Shower", "click" : "monicahome_bathroom_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_bathroom")
    $ add_object_to_scene("Sink", {"type" : 2, "base" : "MonicaHome_Bathroom_Sink", "click" : "monicahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_bathroom")
    $ add_object_to_scene("Toilet", {"type" : 2, "base" : "MonicaHome_Bathroom_Toilet", "click" : "monicahome_bathroom_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_bathroom")
    $ add_object_to_scene("Towel", {"type" : 2, "base" : "MonicaHome_Bathroom_Towel", "click" : "monicahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_bathroom")

    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("СПАЛЬНЯ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monicahome_bathroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="monicahome_bathroom")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monicahome_bathroom_teleport:
    if obj_name == "Teleport_LivingRoom":
        call change_scene("monicahome_livingroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_46
        return
    return
label monicahome_bathroom_environment:
    if obj_name == "Monica":
        call ep211_dialogues6_slum_apartment_8h() from _rcall_ep211_dialogues6_slum_apartment_8h
    if obj_name == "Toilet":
        if act=="l":
            call ep211_dialogues6_slum_apartment_8i() from _rcall_ep211_dialogues6_slum_apartment_8i
            return
    if obj_name == "Sink":
        call ep211_dialogues6_slum_apartment_8j() from _rcall_ep211_dialogues6_slum_apartment_8j
        return
    if obj_name == "Shower":
        if act=="l":
            call ep211_dialogues6_slum_apartment_8k() from _rcall_ep211_dialogues6_slum_apartment_8k
            return
        return
    if obj_name == "Towel":
        call ep211_dialogues6_slum_apartment_31() from _rcall_ep211_dialogues6_slum_apartment_31
    if obj_name == "Mirror":
        call ep211_dialogues6_slum_apartment_32() from _rcall_ep211_dialogues6_slum_apartment_32
    if obj_name == "Boxes":
        call ep211_dialogues6_slum_apartment_33() from _rcall_ep211_dialogues6_slum_apartment_33
    return
