default monicaHomeLivingRoomWardrobeMonicaSuffix = 1

label monicahome_livingroomwardrobe:
    $ print "enter_monicahome_livingroomwardrobe"
    $ miniMapData = []
    call miniMapSlumsApartmentsGenerate() from _rcall_miniMapSlumsApartmentsGenerate
    $ scene_image = "scene_MonicaHome_LivingRoomWardrobe"

    if day_time == "day":
        music Mandeville
    else:
        music street13_ambulance

    if monicaHasCasualDress1 == True:
        $ set_active("Wardrobe_CasualDress1", True, scene="monicahome_livingroomwardrobe")
    else:
        $ set_active("Wardrobe_CasualDress1", False, scene="monicahome_livingroomwardrobe")

    if monicaHasWhoreOutfit1 == True:
        $ set_active("Wardrobe_Whore", True, scene="monicahome_livingroomwardrobe")
    else:
        $ set_active("Wardrobe_Whore", False, scene="monicahome_livingroomwardrobe")

    if cloth != "HomeCloth4":
        $ set_active("Wardrobe_HomeCloth4", True, scene="monicahome_livingroomwardrobe")
    else:
        $ set_active("Wardrobe_HomeCloth4", False, scene="monicahome_livingroomwardrobe")

    if monicaHasSchoolOutfit1 == True and day_time != "evening":
        $ set_active("Wardrobe_SchoolOutfit1", True, scene="monicahome_livingroomwardrobe")
    else:
        $ set_active("Wardrobe_SchoolOutfit1", False, scene="monicahome_livingroomwardrobe")

    $ monicaHomeLivingRoomMonicaSuffix = 1
    $ monicaHomeBathroomMonicaSuffix = 1
    return

label monicahome_livingroomwardrobe_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_Monica_[cloth]_[monicaHomeLivingRoomWardrobeMonicaSuffix]", "click" : "monicahome_livingroomwardrobe_environment", "actions" : "l", "zorder":10}, scene="monicahome_livingroomwardrobe")
    $ add_object_to_scene("Wardrobe_CasualDress1", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_CasualDress1", "click" : "monicahome_livingroomwardrobe_environment", "actions" : "l", "zorder":3, "b":0.15, "group":"wardrobe"}, scene="monicahome_livingroomwardrobe")
    $ add_object_to_scene("Wardrobe_HomeCloth4", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_HomeCloth4", "click" : "monicahome_livingroomwardrobe_environment", "actions" : "l", "zorder":4, "b":0.15, "group":"wardrobe"}, scene="monicahome_livingroomwardrobe")
    $ add_object_to_scene("Wardrobe_SchoolOutfit1", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_SchoolOutfit1", "click" : "monicahome_livingroomwardrobe_environment", "actions" : "l", "zorder":2, "b":0.15, "group":"wardrobe"}, scene="monicahome_livingroomwardrobe")
    $ add_object_to_scene("Wardrobe_Whore", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_Whore", "click" : "monicahome_livingroomwardrobe_environment", "actions" : "l", "zorder":1, "b":0.15, "group":"wardrobe"}, scene="monicahome_livingroomwardrobe")

    $ add_object_to_scene("Picture", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_Picture", "click" : "monicahome_livingroomwardrobe_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="monicahome_livingroomwardrobe")
    $ add_object_to_scene("Teleport_Street", {"type" : 2, "base" : "MonicaHome_LivingRoomWardrobe_TeleportStreet", "click" : "monicahome_livingroomwardrobe_teleport", "actions" : "lw", "zorder":0, "b":0.15, "group":"teleport", "teleport":True}, scene="monicahome_livingroomwardrobe")

    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("СПАЛЬНЯ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "monicahome_livingroomwardrobe_teleport", "xpos" : 1630, "ypos" : 545, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monicahome_livingroomwardrobe_teleport:
    if obj_name == "Teleport_Street":
        if act=="l":
            call ep211_dialogues6_slum_apartment_29() from _rcall_ep211_dialogues6_slum_apartment_29
            return
        call change_scene("street_monicahome", "Fade") from _rcall_change_scene_43
        return
    if obj_name == "Teleport_LivingRoom":
        call change_scene("monicahome_livingroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_44
        return
    return
label monicahome_livingroomwardrobe_environment:
    if obj_name == "Monica":
        call ep211_dialogues6_slum_apartment_8a() from _rcall_ep211_dialogues6_slum_apartment_8a

    if obj_name == "Picture":
        call ep211_dialogues6_slum_apartment_28() from _rcall_ep211_dialogues6_slum_apartment_28

    if obj_name == "Wardrobe_HomeCloth4":
        $ cloth = "HomeCloth4"
        $ cloth_type = "HomeCloth"
        sound snd_fabric1
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_6
        return

    if obj_name == "Wardrobe_CasualDress1" or obj_name == "Wardrobe_SchoolOutfit1" or obj_name == "Wardrobe_Whore":
        call process_hooks("slums_apartments_check_exit_wardrobe", "monicahome_livingroomwardrobe") from _rcall_process_hooks_6
        if _return == False:
            return
        if obj_name == "Wardrobe_CasualDress1":
            $ cloth = "CasualDress1"
            $ cloth_type = "CasualDress"
        if obj_name == "Wardrobe_SchoolOutfit1":
            $ cloth = "SchoolOutfit1"
            $ cloth_type = "SchoolOutfit"
        if obj_name == "Wardrobe_Whore":
            $ cloth = "Whore"
            $ cloth_type = "Whore"
        sound2 snd_fabric1
        call change_scene("street_monicahome", "Fade") from _rcall_change_scene_45
        return

    return
