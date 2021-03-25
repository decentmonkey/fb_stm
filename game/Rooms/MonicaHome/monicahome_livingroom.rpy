default monicaHomeLivingRoomMonicaSuffix = 1
default monicaHomeLivingRoomJackSuffix = 1
default monicaHomeLivingRoomSceneSuffix = ""
default monicaHomeLivingRoomSceneSuffix2 = ""
label monicahome_livingroom:
    $ print "enter_monicahome_livingroom"
    $ miniMapData = []
    call miniMapSlumsApartmentsGenerate() from _rcall_miniMapSlumsApartmentsGenerate_3
    $ scene_image = "scene_MonicaHome_LivingRoom[day_suffix][monicaHomeLivingRoomSceneSuffix][monicaHomeLivingRoomSceneSuffix2]"

    if day_time == "day":
        music Mandeville
    else:
        music street13_ambulance

    $ monicaHomeBathroomMonicaSuffix = 1
    return

label monicahome_livingroom_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "MonicaHome_LivingRoom_Monica_[cloth]_[monicaHomeLivingRoomMonicaSuffix][day_suffix][monicaHomeLivingRoomSceneSuffix2]", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":10}, scene="monicahome_livingroom")
    $ add_object_to_scene("Shawarma_Trader", {"type" : 2, "base" : "MonicaHome_LivingRoom_Jack_[monicaHomeLivingRoomJackSuffix][day_suffix][monicaHomeLivingRoomSceneSuffix2]", "click" : "monicahome_livingroom_environment", "actions" : "lt", "zorder":9}, scene="monicahome_livingroom")
    $ add_object_to_scene("Cocktail", {"type" : 2, "base" : "MonicaHome_LivingRoom_Cocktail[monicaHomeLivingRoomSceneSuffix2]", "click" : "monicahome_livingroom_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Bed1", {"type" : 2, "base" : "MonicaHome_LivingRoom_Bed1", "click" : "monicahome_livingroom_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Chair1", {"type" : 2, "base" : "MonicaHome_LivingRoom_Chair1", "click" : "monicahome_livingroom_environment", "actions" : "lw", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Commode", {"type" : 2, "base" : "MonicaHome_LivingRoom_Commode", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Fish", {"type" : 2, "base" : "MonicaHome_LivingRoom_Fish", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Lamp1", {"type" : 2, "base" : "MonicaHome_LivingRoom_Lamp1", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Lamp2", {"type" : 2, "base" : "MonicaHome_LivingRoom_Lamp2", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Lamp3", {"type" : 2, "base" : "MonicaHome_LivingRoom_Lamp3", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Picture1", {"type" : 2, "base" : "MonicaHome_LivingRoom_Picture1", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Picture2", {"type" : 2, "base" : "MonicaHome_LivingRoom_Picture2", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Table1", {"type" : 2, "base" : "MonicaHome_LivingRoom_Table1", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")
    $ add_object_to_scene("Window", {"type" : 2, "base" : "MonicaHome_LivingRoom_Window", "click" : "monicahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroom")

    $ add_object_to_scene("Teleport_Bathroom", {"type":3, "text" : t_("ВАННАЯ КОМНАТА"), "rarrow" : "arrow_right_2", "base":"Street_MonicaHome_TeleportSlums", "click" : "monicahome_livingroom_teleport", "xpos" : 1525, "ypos" : 1006, "zorder":15, "teleport":True, "high_sprite_hover":True}, scene="monicahome_livingroom")
    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "rarrow" : "arrow_down_2", "base":"MonicaHome_LivingRoom_TeleportKitchen", "click" : "monicahome_livingroom_teleport", "xpos" : 244, "ypos" : 1006, "zorder":15, "teleport":True, "high_sprite_hover":True}, scene="monicahome_livingroom")
    $ add_object_to_scene("Teleport_Wardrobe", {"type":3, "text" : t_("ГАРДЕРОБ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "monicahome_livingroom_teleport", "xpos" : 220, "ypos" : 545, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="monicahome_livingroom")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monicahome_livingroom_teleport:
    if obj_name == "Teleport_Bathroom":
        call change_scene("monicahome_bathroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_48
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("monicahome_kitchen", "Fade", "snd_walk_barefoot") from _rcall_change_scene_49
        return
    if obj_name == "Teleport_Wardrobe":
        call change_scene("monicahome_livingroomwardrobe", "Fade", "snd_walk_barefoot") from _rcall_change_scene_50
        return
    return
label monicahome_livingroom_environment:
    if obj_name == "Monica":
        call ep211_dialogues6_slum_apartment_8a() from _rcall_ep211_dialogues6_slum_apartment_8a_1
    if obj_name == "Shawarma_Trader":
        if act=="l":
            mt "Грязный продавец. Я не выношу даже его вида! Фу!"
    if obj_name == "Cocktail":
        if act=="l":
            call ep211_dialogues6_slum_apartment_8l() from _rcall_ep211_dialogues6_slum_apartment_8l
        if act=="h":
            call ep211_dialogues6_slum_apartment_8n() from _rcall_ep211_dialogues6_slum_apartment_8n_1
        return
    if obj_name == "Bed1":
        if act=="l":
            call ep211_dialogues6_slum_apartment_8c() from _rcall_ep211_dialogues6_slum_apartment_8c
        if act=="w":
            return
    if obj_name == "Chair1":
        if act=="l":
            call ep211_dialogues6_slum_apartment_8d() from _rcall_ep211_dialogues6_slum_apartment_8d
        if act=="w":
            call ep211_dialogues6_slum_apartment_8a() from _rcall_ep211_dialogues6_slum_apartment_8a_2
            return
    if obj_name == "Commode":
        call ep211_dialogues6_slum_apartment_8db() from _rcall_ep211_dialogues6_slum_apartment_8db
    if obj_name == "Fish":
        call ep211_dialogues6_slum_apartment_23() from _rcall_ep211_dialogues6_slum_apartment_23
    if obj_name == "Lamp1":
        call ep211_dialogues6_slum_apartment_24() from _rcall_ep211_dialogues6_slum_apartment_24
    if obj_name == "Lamp2" or obj_name == "Lamp3":
        call ep211_dialogues6_slum_apartment_25() from _rcall_ep211_dialogues6_slum_apartment_25
    if obj_name == "Picture1" or obj_name == "Picture2":
        call ep211_dialogues6_slum_apartment_26() from _rcall_ep211_dialogues6_slum_apartment_26
    if obj_name == "Table1":
        call ep211_dialogues6_slum_apartment_27() from _rcall_ep211_dialogues6_slum_apartment_27
    if obj_name == "Window":
        call ep211_dialogues6_slum_apartment_8m() from _rcall_ep211_dialogues6_slum_apartment_8m
    return
