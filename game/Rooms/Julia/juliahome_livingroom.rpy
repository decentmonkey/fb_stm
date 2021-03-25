default juliaHomeLivingRoomMonicaSuffix = 1
default juliaHomeLivingRoomJuliaSuffix = 1
default juliaHomeLivingRoomJuliaCloth = ""

default juliaHomeLivingRoomSceneSuffix = ""
label juliahome_livingroom:
    $ print "enter_juliahome_livingroom"
    $ miniMapData = []
    call miniMapJuliaHomeGenerate() from _rcall_miniMapJuliaHomeGenerate_3

    $ scene_image = "scene_JuliaHome_LivingRoom[day_suffix][juliaHomeLivingRoomSceneSuffix]"

    if juliaHomeLivingRoomJuliaSuffix != 1 and juliaHomeLivingRoomJuliaSuffix != 2 and juliaHomeLivingRoomMonicaSuffix != 1 and juliaHomeLivingRoomMonicaSuffix != 4:
        $ set_active("Bed1", True)

    if day_time == "day":
        music Mandeville
    else:
        music street13_ambulance
    return

label juliahome_livingroom_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "JuliaHome_LivingRoom_Monica_[cloth]_[juliaHomeLivingRoomMonicaSuffix][day_suffix]", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":10}, scene="juliahome_livingroom")
    $ add_object_to_scene("Julia", {"type" : 2, "base" : "JuliaHome_LivingRoom_Julia_[juliaHomeLivingRoomJuliaCloth][juliaHomeLivingRoomJuliaSuffix][day_suffix]", "click" : "juliahome_livingroom_environment", "actions" : "lt", "zorder":10}, scene="juliahome_livingroom")

    $ add_object_to_scene("Bed1", {"type" : 2, "base" : "JulliaHome_LivingRoom_Bed1", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Books", {"type" : 2, "base" : "JulliaHome_LivingRoom_Books", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Cupboard", {"type" : 2, "base" : "JulliaHome_LivingRoom_Cupboard", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("KitchenItem1", {"type" : 2, "base" : "JulliaHome_LivingRoom_KitchenItem1", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Picture1", {"type" : 2, "base" : "JulliaHome_LivingRoom_Picture1", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Picture2", {"type" : 2, "base" : "JulliaHome_LivingRoom_Picture2", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Plaid", {"type" : 2, "base" : "JulliaHome_LivingRoom_Plaid", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")

    $ add_object_to_scene("Table1", {"type" : 2, "base" : "JulliaHome_LivingRoom_Table1", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Wardrobe", {"type" : 2, "base" : "JulliaHome_LivingRoom_Wardrobe", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")
    $ add_object_to_scene("Windows", {"type" : 2, "base" : "JulliaHome_LivingRoom_Windows", "click" : "juliahome_livingroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_livingroom")

    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "juliahome_livingroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="juliahome_livingroom")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label juliahome_livingroom_teleport:
    if obj_name == "Teleport_Kitchen":
        call change_scene("juliahome_kitchen") from _rcall_change_scene_71
        return
    return
label juliahome_livingroom_environment:
    if obj_name == "Monica":
        call ep211_dialogues4_julia_11a() from _rcall_ep211_dialogues4_julia_11a
    if obj_name == "Julia":
        if act=="l":
            call ep210_dialogues5_julia_3_2() from _rcall_ep210_dialogues5_julia_3_2_1
            return
    if obj_name == "Picture1" or obj_name == "Picture2":
        call ep211_dialogues4_julia_11b() from _rcall_ep211_dialogues4_julia_11b_1
    if obj_name == "Bed1":
        if act=="l":
            call ep211_dialogues4_julia_11c() from _rcall_ep211_dialogues4_julia_11c
            return
    if obj_name == "Table1":
        call ep211_dialogues4_julia_11d() from _rcall_ep211_dialogues4_julia_11d_1
    if obj_name == "Wardrobe":
        call ep211_dialogues4_julia_11e() from _rcall_ep211_dialogues4_julia_11e
    if obj_name == "Plaid":
        call ep211_dialogues4_julia_11m() from _rcall_ep211_dialogues4_julia_11m
        return
    if obj_name == "Cupboard":
        call ep211_dialogues4_julia_11n() from _rcall_ep211_dialogues4_julia_11n
    if obj_name == "Books":
        call ep211_dialogues4_julia_11o() from _rcall_ep211_dialogues4_julia_11o
    if obj_name == "KitchenItem1":
        call ep211_dialogues4_julia_11g() from _rcall_ep211_dialogues4_julia_11g_1
        return
    if obj_name == "Windows":
        call ep211_dialogues4_julia_11p() from _rcall_ep211_dialogues4_julia_11p
    return
