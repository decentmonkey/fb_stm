default pubStag1SkipMusicOnce = False

default pub_stage1_monica_suffix = 1
default pub_stage1_bartender_suffix = 1
default pub_stage1_bartenderwaitress_suffix = 1
default pub_stage1_claire_suffix = 1
label pub_stage1:
    $ print "enter_pub_stage1"
    $ miniMapData = []

    $ scene_image = "scene_Pub_Stage1"

    if pubStag1SkipMusicOnce == True:
        $ pubStag1SkipMusicOnce = False
    else:
        music RocknRoll_loop
        if get_active_objects(scene="pub", group="visitors") != False:
            music2 pub_noise1

    return
label pub_stage1_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Pub_Stage1_Monica_[cloth]_[pub_stage1_monica_suffix]", "click" : "pub_stage1_environment", "actions" : "l", "zorder" : 10}, scene="pub_stage1")

    $ add_object_to_scene("Bartender", {"type" : 2, "base" : "Pub_Stage1_Bartender[pub_stage1_bartender_suffix]", "click" : "pub_stage1_environment", "actions" : "lt", "zorder":8}, scene="pub_stage1")
    $ add_object_to_scene("Bartender_Waitress", {"type" : 2, "base" : "Pub_Stage1_Bartender_Waitress[pub_stage1_bartenderwaitress_suffix]", "click" : "pub_stage1_environment", "actions" : "lt", "zorder":8}, scene="pub_stage1")
    $ add_object_to_scene("Pub_StripteaseGirl2", {"type" : 2, "base" : "Pub_Stage1_Clare_[pub_stage1_claire_suffix]", "click" : "pub_stage1_environment", "actions" : "lt", "zorder":8}, scene="pub_stage1")

    $ add_object_to_scene("Stage", {"type" : 2, "base" : "Pub_Stage1_Stage", "click" : "pub_stage1_environment", "actions" : "lw", "zorder":0, "group":"environment"}, scene="pub_stage1")

    $ add_object_to_scene("Teleport_MakeupRoom", {"type":3, "text" : t_("ГРИМЕРНАЯ КОМНАТА"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "pub_stage1_teleport", "xpos" : 782, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="pub_stage1")
    return

label pub_stage1_teleport:
    if obj_name == "Teleport_MakeupRoom":
        call change_scene("pub_makeuproom", "Fade_long") from _rcall_change_scene_72
    return

label pub_stage1_environment:
    if obj_name == "Monica":
        call dialogue_5_dance_strip_4n() from _rcall_dialogue_5_dance_strip_4n
        return
    if obj_name == "Bartender" or obj_name == "Bartender_Waitress":
        jump pub_environment
    if obj_name == "Stage":
        if act=="l":
            call dialogue_5_dance_strip_4n() from _rcall_dialogue_5_dance_strip_4n_1
            return
        if monicaDancedLastDay == day:
            if monicaDancingTopless == False:
                call dialogue_5_dance_strip_4m() from _rcall_dialogue_5_dance_strip_4m
            else:
                call dialogue_5_dance_strip_11() from _rcall_dialogue_5_dance_strip_11
            return
        call process_hooks("monica_pole_dance", "global") from _rcall_process_hooks_7
        call process_hooks("monica_pole_dance_end", "global") from _rcall_process_hooks_8
        return
    return
