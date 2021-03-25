default juliaHomeBathroomShowerMonicaSuffix = 1
default juliaHomeBathroomShowerJuliaSuffix = 1
default juliaHomeBathroomJuliaCloth = ""
default juliaHomeBathroomShowerSceneSuffix = ""
label juliahome_bathroomshower:
    $ print "enter_juliahome_bathroom"
    $ miniMapData = []
    call miniMapJuliaHomeGenerate() from _rcall_miniMapJuliaHomeGenerate_1

    $ scene_image = "scene_JuliaHome_BathroomShower[juliaHomeBathroomShowerSceneSuffix]"

    $ set_active("Monica", False)
    $ set_active("Julia", False)

    if day_time == "day":
        music Stealth_Groover
    else:
        music Stealth_Groover
    return

label juliahome_bathroomshower_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "JuliaHome_BathroomShower_Monica_[cloth]_[juliaHomeBathroomShowerMonicaSuffix]", "click" : "juliahome_bathroomshower_environment", "actions" : "l", "zorder":10, "active":False}, scene="juliahome_bathroomshower")
    $ add_object_to_scene("Julia", {"type" : 2, "base" : "JuliaHome_BathroomShower_Julia_[juliaHomeBathroomJuliaCloth][juliaHomeBathroomShowerJuliaSuffix]", "click" : "juliahome_bathroomshower_environment", "actions" : "lt", "zorder":10, "active":False}, scene="juliahome_bathroomshower")

    $ add_object_to_scene("Teleport_Bathroom", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "juliahome_bathroomshower_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="juliahome_bathroomshower")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label juliahome_bathroomshower_init2:
    $ add_object_to_scene("Shower", {"type" : 2, "base" : "JulliaHome_Bathroom_Shower_Shower", "click" : "juliahome_bathroomshower_environment", "actions" : "lh", "zorder":10}, scene="juliahome_bathroomshower")
    return

label juliahome_bathroomshower_teleport:
    if obj_name == "Teleport_Bathroom":
        call change_scene("juliahome_bathroom") from _rcall_change_scene_68
    return
label juliahome_bathroomshower_environment:
    if obj_name == "Shower":
        call ep213_dialogues5_julia_15c() from _rcall_ep213_dialogues5_julia_15c
    return
