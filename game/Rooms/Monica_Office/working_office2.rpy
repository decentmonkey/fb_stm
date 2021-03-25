label working_office2:
    $ print "enter_working_office2"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_3

    $ scene_image = "scene_WorkingOffice2[day_suffix]"
    music Stealth_Groover
    return

label working_office2_init:

#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "WorkingOffice_Monica_[cloth]", "click" : "working_office2_environment", "actions" : "l", "zorder":10}, scene="working_office2")

    $ add_object_to_scene("Worker3", {"type" : 2, "base" : "WorkingOffice2_w3", "click" : "working_office_environment", "actions" : "lt", "zorder":5, "group":"workers"}, scene="working_office2")
    $ add_object_to_scene("Worker4", {"type" : 2, "base" : "WorkingOffice2_w4", "click" : "working_office_environment", "actions" : "lt", "zorder":5, "group":"workers"}, scene="working_office2")
    $ add_object_to_scene("Worker6", {"type" : 2, "base" : "WorkingOffice2_w6", "click" : "working_office_environment", "actions" : "lt", "zorder":5, "group":"workers"}, scene="working_office2")
    $ add_object_to_scene("Worker7", {"type" : 2, "base" : "WorkingOffice2_w7", "click" : "working_office_environment", "actions" : "lt", "zorder":5, "group":"workers"}, scene="working_office2")

    $ add_object_to_scene("Computer1", {"type" : 2, "base" : "WorkingOffice2_Computer1", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")
    $ add_object_to_scene("Computer2", {"type" : 2, "base" : "WorkingOffice2_Computer2", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")
    $ add_object_to_scene("Computer3", {"type" : 2, "base" : "WorkingOffice2_Computer3", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")
    $ add_object_to_scene("Computer4", {"type" : 2, "base" : "WorkingOffice2_Computer4", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")
    $ add_object_to_scene("Computer5", {"type" : 2, "base" : "WorkingOffice2_Computer5", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")
    $ add_object_to_scene("Computer6", {"type" : 2, "base" : "WorkingOffice2_Computer6", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")

    $ add_object_to_scene("Folders1", {"type" : 2, "base" : "WorkingOffice2_Folders1", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")
    $ add_object_to_scene("Folders2", {"type" : 2, "base" : "WorkingOffice2_Folders2", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office2")

    $ add_object_to_scene("Teleport_Cabinet", {"type":3, "text" : t_("В КАБИНЕТ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "working_office2_teleport", "xpos" : 1680, "ypos" : 906, "zorder":11, "teleport":True}, scene="working_office2")
    $ add_object_to_scene("Teleport_WorkingOffice", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "working_office2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="working_office2")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label working_office2_teleport:
    if obj_name == "Teleport_WorkingOffice":
        call change_scene("working_office") from _call_change_scene_314
        return
    if obj_name == "Teleport_Cabinet":
        $ workingOfficeCabinetMonicaSuffix = 1        
        call change_scene("working_office_cabinet") from _call_change_scene_315
        return
    return
label working_office2_environment:
    return
