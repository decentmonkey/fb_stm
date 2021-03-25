default pub_makeuproom_mollytable_initialized = False

label pub_makeuproom_mollytable:
    $ print "enter_pub_makeuproom_mollytable"
    $ miniMapData = []

    $ scene_image = "scene_Pub_MakeupRoom_MollyTable"
    music Hidden_Agenda
#        music2 stop
#        music2 pub_noise1_low

    return
label pub_makeuproom_mollytable_init:
    $ pub_makeuproom_mollytable_initialized = True
    $ add_object_to_scene("Tips", {"type" : 2, "base" : "Pub_MakeupRoom_MollyTable_Tips", "click" : "pub_makeuproom_mollytable_environment", "actions" : "lh", "zorder":0, "group":"environment"}, scene="pub_makeuproom_mollytable")
    $ add_object_to_scene("Teleport_Pub_MakeupRoom", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "pub_makeuproom_mollytable_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="pub_makeuproom_mollytable")
    return

label pub_makeuproom_mollytable_teleport:
    if obj_name == "Teleport_Pub_MakeupRoom":
        call change_scene("pub_makeuproom", "Fade") from _rcall_change_scene_122
    return

label pub_makeuproom_mollytable_environment:
    return
