default juliaHomeBathroomMonicaSuffix = 1
default juliaHomeBathroomJuliaSuffix = 2

default juliaHomeBathroomSceneSuffix = ""
label juliahome_bathroom:
    $ print "enter_juliahome_bathroom"
    $ miniMapData = []
    call miniMapJuliaHomeGenerate() from _rcall_miniMapJuliaHomeGenerate

    if lastSceneName != "juliahome_bathroomshower":
        $ juliaHomeBathroomMonicaSuffix = 1

    $ scene_image = "scene_JuliaHome_Bathroom[juliaHomeBathroomSceneSuffix]"

    if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 1:
        $ set_active("Shower", False)
        sound2 snd_shower
    else:
        $ set_active("Shower", True)

    if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 2:
        $ set_active("Toilet", False)
    else:
        $ set_active("Toilet", True)

    if day_time == "day":
        music Stealth_Groover
    else:
        music Stealth_Groover
    return

label juliahome_bathroom_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "JuliaHome_Bathroom_Monica_[cloth]_[juliaHomeBathroomMonicaSuffix]", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":10}, scene="juliahome_bathroom")
    $ add_object_to_scene("Julia", {"type" : 2, "base" : "JuliaHome_Bathroom_Julia_[juliaHomeLivingRoomJuliaCloth][juliaHomeBathroomJuliaSuffix]", "click" : "juliahome_bathroom_environment", "actions" : "lt", "zorder":10, "active":False}, scene="juliahome_bathroom")

    $ add_object_to_scene("Basket1", {"type" : 2, "base" : "JulliaHome_Bathroom_Basket1", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Basket2", {"type" : 2, "base" : "JulliaHome_Bathroom_Basket2", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Items1", {"type" : 2, "base" : "JulliaHome_Bathroom_Items1", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Items2", {"type" : 2, "base" : "JulliaHome_Bathroom_Items2", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Items3", {"type" : 2, "base" : "JulliaHome_Bathroom_Items3", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Items4", {"type" : 2, "base" : "JulliaHome_Bathroom_Items4", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("TableItems", {"type" : 2, "base" : "JulliaHome_Bathroom_TableItems", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Shower", {"type" : 2, "base" : "JulliaHome_Bathroom_TeleportShower", "click" : "juliahome_bathroom_environment", "actions" : "lw", "zorder":0, "b":0.18, "tint":[1.0, 1.0, 0.7], "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("Toilet", {"type" : 2, "base" : "JulliaHome_Bathroom_Toilet", "click" : "juliahome_bathroom_environment", "actions" : "lh", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")

    $ add_object_to_scene("WashMachine", {"type" : 2, "base" : "JulliaHome_Bathroom_WashMachine", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("ToiletPaper", {"type" : 2, "base" : "JulliaHome_Bathroom_ToiletPaper", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")
    $ add_object_to_scene("ToiletStick", {"type" : 2, "base" : "JulliaHome_Bathroom_ToiletStick", "click" : "juliahome_bathroom_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="juliahome_bathroom")


    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "juliahome_bathroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="juliahome_bathroom")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label juliahome_bathroom_teleport:
    if obj_name == "Teleport_Kitchen":
        call change_scene("juliahome_kitchen", "Fade", "highheels_run2") from _rcall_change_scene_63
    return
label juliahome_bathroom_environment:
    if obj_name == "Monica":
        call ep211_dialogues4_julia_6b() from _rcall_ep211_dialogues4_julia_6b
    if obj_name == "Basket1" or obj_name == "Basket2":
        call ep211_dialogues4_julia_11l() from _rcall_ep211_dialogues4_julia_11l
    if obj_name == "WashMachine":
        call ep211_dialogues4_julia_11l() from _rcall_ep211_dialogues4_julia_11l_1
    if obj_name == "ToiletPaper":
        call ep211_dialogues4_julia_11l() from _rcall_ep211_dialogues4_julia_11l_2
    if obj_name == "ToiletStick":
        call ep211_dialogues4_julia_11l() from _rcall_ep211_dialogues4_julia_11l_3
    if obj_name == "TableItems":
        call ep211_dialogues4_julia_11i() from _rcall_ep211_dialogues4_julia_11i
    if obj_name == "Items1" or obj_name == "Items2" or obj_name == "Items3" or obj_name == "Items4":
        call ep211_dialogues4_julia_11l() from _rcall_ep211_dialogues4_julia_11l_4
    if obj_name == "Toilet":
        if act=="l":
            call ep211_dialogues4_julia_11h() from _rcall_ep211_dialogues4_julia_11h
            return
        call ep211_dialogues4_julia_11h() from _rcall_ep211_dialogues4_julia_11h_1
        return
    if obj_name == "Shower":
        if act=="l":
            call ep211_dialogues4_julia_11j() from _rcall_ep211_dialogues4_julia_11j
            return
        call change_scene("juliahome_bathroomshower") from _rcall_change_scene_64
        return
    return
