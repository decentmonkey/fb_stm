default streetMonicaHomeMonicaSuffix = 0
default streetMonicaHomeJackSuffix = 1
default monicaHomeMiniMapEnabled = True

label street_monicahome:
    $ print "enter_street_monicahome"
    $ miniMapData = []
    if slumsApartmentsRentActive == True:
        call miniMapSlumsApartmentsGenerate() from _rcall_miniMapSlumsApartmentsGenerate_4
    $ sceneIsStreet = True

    $ scene_image = "scene_Street_MonicaHome[day_suffix]"

    if day_time == "day":
        music street4
    else:
        if rand(1,4) > 1:
            music street_evening3
        else:
            music street13_ambulance

    $ monicaHomeBathroomMonicaSuffix = 1
    $ monicaHomeLivingRoomMonicaSuffix = 1
    return

label street_monicahome_init:
#    $ clear_scene_from_objects("street_monicahome")
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_MonicaHome_Monica_[cloth]_[streetMonicaHomeMonicaSuffix][day_suffix]", "click" : "street_monicahome_environment", "actions" : "l", "zorder":10}, scene="street_monicahome")
    $ add_object_to_scene("Shawarma_Trader", {"type" : 2, "base" : "Street_MonicaHome_Jack1_[streetMonicaHomeJackSuffix][day_suffix]", "click" : "street_monicahome_environment", "actions" : "lt", "zorder":9}, scene="street_monicahome")
    $ add_object_to_scene("ClosedWindow1", {"type" : 2, "base" : "Street_MonicaHome_ClosedWindow1", "click" : "street_monicahome_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="street_monicahome")
    $ add_object_to_scene("ClosedWindow2", {"type" : 2, "base" : "Street_MonicaHome_ClosedWindow2", "click" : "street_monicahome_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="street_monicahome")
    $ add_object_to_scene("Trash", {"type" : 2, "base" : "Street_MonicaHome_Trash", "click" : "street_monicahome_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="street_monicahome")
    $ add_object_to_scene("HomeEnter", {"type" : 2, "base" : "Street_MonicaHome_Enter", "click" : "street_monicahome_teleport", "actions" : "lw", "zorder":0, "b":0.15, "group":"teleport"}, scene="street_monicahome")
    $ add_object_to_scene("MonicaWindow", {"type" : 2, "base" : "Street_MonicaHome_MonicaWindow", "click" : "street_monicahome_teleport", "actions" : "lw", "zorder":0, "b":0.15, "group":"teleport"}, scene="street_monicahome")

    $ add_object_to_scene("Street_MonicaHome_TeleportSlums", {"type":3, "text" : t_("ТРУЩОБЫ"), "rarrow" : "arrow_right_2", "base":"Street_MonicaHome_TeleportSlums", "click" : "street_monicahome_teleport", "xpos" : 1574, "ypos" : 1003, "zorder":3, "teleport":True}, scene="street_monicahome")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_monicahome_teleport:
    if obj_name == "Street_MonicaHome_TeleportSlums":
        if cloth_type == "Nude":
            call change_scene("hostel_street", "Fade", "snd_walk_barefoot") from _rcall_change_scene_51
            return
        call change_scene("hostel_street", "Fade", "highheels_run2") from _rcall_change_scene_52
        return
    if obj_name == "HomeEnter":
        if act=="l":
            call ep211_dialogues6_slum_apartment_4() from _rcall_ep211_dialogues6_slum_apartment_4_1
            return
        call change_scene("monicahome_livingroom") from _rcall_change_scene_53
        return
    if obj_name == "MonicaWindow":
        if act=="l":
            call ep211_dialogues6_slum_apartment_22() from _rcall_ep211_dialogues6_slum_apartment_22
            return
        call change_scene("monicahome_livingroom") from _rcall_change_scene_54
        return
    return
label street_monicahome_environment:
    if obj_name == "Monica":
        call ep211_dialogues6_slum_apartment_4() from _rcall_ep211_dialogues6_slum_apartment_4_2
    if obj_name == "Shawarma_Trader":
        if act=="l":
            mt "Грязный продавец. Я не выношу даже его вида! Фу!"
    if obj_name == "ClosedWindow1" or obj_name == "ClosedWindow2":
        call ep211_dialogues6_slum_apartment_21() from _rcall_ep211_dialogues6_slum_apartment_21
    if obj_name == "Trash":
        call ep211_dialogues6_slum_apartment_20() from _rcall_ep211_dialogues6_slum_apartment_20
    return
