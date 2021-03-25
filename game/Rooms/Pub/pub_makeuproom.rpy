default pubMakeupRoomSkipMusicOnce = False

default pub_makeuproom_monica_suffix = 1
default pub_makeuproom_claire_suffix = 1
default pub_makeuproom_molly_suffix = 1

default pub_makeuproom_tips_initialized = False

label pub_makeuproom:
    $ print "enter_pub_makeuproom"
    $ miniMapData = []

    $ scene_image = "scene_Pub_MakeupRoom"
    if pub_makeuproom_tips_initialized == True:
        $ scene_image = "scene_Pub_MakeupRoom_notips"
    if pubMakeupRoomSkipMusicOnce == True:
        $ pubMakeupRoomSkipMusicOnce = False
    else:
        music Groove2_85
#        music2 stop
        music2 pub_noise1_low

    return
label pub_makeuproom_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Pub_MakeupRoom_Monica_[cloth]_[pub_makeuproom_monica_suffix]", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder" : 10}, scene="pub_makeuproom")

    $ add_object_to_scene("Pub_StripteaseGirl2", {"type" : 2, "base" : "Pub_MakeupRoom_Clare_[pub_makeuproom_claire_suffix]", "click" : "pub_makeuproom_environment", "actions" : "lt", "zorder":8, "active":False}, scene="pub_makeuproom")
    $ add_object_to_scene("Pub_StripteaseGirl1", {"type" : 2, "base" : "Pub_MakeupRoom_Molly_[pub_makeuproom_molly_suffix]", "click" : "pub_makeuproom_environment", "actions" : "lt", "zorder":8, "active":False}, scene="pub_makeuproom")

    $ add_object_to_scene("Carpet", {"type" : 2, "base" : "Pub_MakeupRoom_Carpet", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("Cloth1", {"type" : 2, "base" : "Pub_MakeupRoom_Cloth1", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("Cloth2", {"type" : 2, "base" : "Pub_MakeupRoom_Cloth2", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.7]}, scene="pub_makeuproom")
    $ add_object_to_scene("Journals", {"type" : 2, "base" : "Pub_MakeupRoom_Journals", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("JOY", {"type" : 2, "base" : "Pub_MakeupRoom_JOY", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("MoulinRouge", {"type" : 2, "base" : "Pub_MakeupRoom_MoulinRouge", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("Picture", {"type" : 2, "base" : "Pub_MakeupRoom_Picture", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":1, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("TableClaire", {"type" : 2, "base" : "Pub_MakeupRoom_TableClaire", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("TableMolly", {"type" : 2, "base" : "Pub_MakeupRoom_TableMolly", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("Trash1", {"type" : 2, "base" : "Pub_MakeupRoom_Trash1", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")
    $ add_object_to_scene("Vents", {"type" : 2, "base" : "Pub_MakeupRoom_Vents", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_makeuproom")

    $ add_object_to_scene("Teleport_Pub", {"type":3, "text" : t_("ВЫХОД ИЗ ГРИМЕРНОЙ КОМНАТЫ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "pub_makeuproom_teleport", "xpos" : 1101, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="pub_makeuproom")
    return

label pub_makeuproom_init2:
    $ add_object_to_scene("Picture", {"type" : 2, "base" : "Pub_MakeupRoom_Picture", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":1, "group":"environment"}, scene="pub_makeuproom")
    return
label pub_makeuproom_init3:
    $ add_object_to_scene("Picture", {"type" : 2, "base" : "Pub_MakeupRoom_Picture_Marked", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":1, "group":"environment"}, scene="pub_makeuproom")
    return

label pub_makeuproom_init4:
    $ pub_makeuproom_tips_initialized = True
    $ add_object_to_scene("Tips", {"type" : 2, "base" : "Pub_MakeupRoom_Tips", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":1, "group":"environment"}, scene="pub_makeuproom")
    return

label pub_makeuproom_init5:
    $ add_object_to_scene("Picture_MonicaQueen", {"type" : 2, "base" : "Pub_MakeupRoom_Picture_MonicaQueen", "click" : "pub_makeuproom_environment", "actions" : "l", "zorder":1, "group":"environment"}, scene="pub_makeuproom")
    return

label pub_makeuproom_teleport:
    if obj_name == "Teleport_Pub":
        if cloth_type == "StripOutfit":
            call change_scene("pub_stage1", "Fade_long") from _rcall_change_scene_73
            return
        call change_scene("pub", "Fade_long") from _rcall_change_scene_74
    return

label pub_makeuproom_environment:
    if obj_name == "Monica":
        call dialogue_5_dance_strip_30a() from _rcall_dialogue_5_dance_strip_30a
        return
    if obj_name == "Pub_StripteaseGirl1":
        if act=="l":
            if ep29_quests_pub_forgiveness_dancing_stage == 0:
                call dialogue_5_dance_strip_25a() from _rcall_dialogue_5_dance_strip_25a
            if ep29_quests_pub_forgiveness_dancing_stage > 0:
                call dialogue_5_dance_strip_25() from _rcall_dialogue_5_dance_strip_25
            return

        if ep29_quests_pub_monica_knows_molly == False:
            call dialogue_5_dance_strip_2b() from _rcall_dialogue_5_dance_strip_2b
        else:
            call dialogue_5_dance_strip_27() from _rcall_dialogue_5_dance_strip_27
            call refresh_scene_fade() from _rcall_refresh_scene_fade_26
            return
        return

    if obj_name == "Pub_StripteaseGirl2":
        if act=="l":
            if ep29_quests_pub_monica_knows_claire == False:
                call dialogue_5_dance_strip_8a() from _rcall_dialogue_5_dance_strip_8a
            else:
                call dialogue_5_dance_strip_26() from _rcall_dialogue_5_dance_strip_26
            return
        return

    if obj_name == "Carpet":
        call dialogue_5_dance_strip_30k() from _rcall_dialogue_5_dance_strip_30k
    if obj_name == "Cloth1":
        call dialogue_5_dance_strip_30d() from _rcall_dialogue_5_dance_strip_30d
    if obj_name == "Cloth2":
        if act=="l":
            call dialogue_5_dance_strip_30d() from _rcall_dialogue_5_dance_strip_30d_1
    if obj_name == "Journals":
        call dialogue_5_dance_strip_30e() from _rcall_dialogue_5_dance_strip_30e
    if obj_name == "JOY":
        call dialogue_5_dance_strip_30o() from _rcall_dialogue_5_dance_strip_30o
    if obj_name == "MoulinRouge":
        call dialogue_5_dance_strip_30j() from _rcall_dialogue_5_dance_strip_30j
    if obj_name == "Picture":
        call dialogue_5_dance_strip_30c() from _rcall_dialogue_5_dance_strip_30c
        call refresh_scene_fade() from _rcall_refresh_scene_fade_27
        return
    if obj_name == "TableClaire":
        call dialogue_5_dance_strip_30h() from _rcall_dialogue_5_dance_strip_30h
        call refresh_scene_fade() from _rcall_refresh_scene_fade_28
        return
    if obj_name == "TableMolly":
        call dialogue_5_dance_strip_30g() from _rcall_dialogue_5_dance_strip_30g
        call refresh_scene_fade() from _rcall_refresh_scene_fade_29
        return
    if obj_name == "Trash1":
        call dialogue_5_dance_strip_30f() from _rcall_dialogue_5_dance_strip_30f
    if obj_name == "Vents":
        call dialogue_5_dance_strip_30b() from _rcall_dialogue_5_dance_strip_30b

    if obj_name == "Picture_MonicaQueen":
        call ep215_dialogues1_pub_14b() from _rcall_ep215_dialogues1_pub_14b
        call refresh_scene_fade() from _rcall_refresh_scene_fade_116
    return
