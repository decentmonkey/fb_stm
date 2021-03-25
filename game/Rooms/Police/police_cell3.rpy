default monicaPoliceCell3Suffix = 1
default cageInteractCnt = 0
define cageInteractAmount = 5

label police_cell3:
    $ print "enter_police_cell3"
    $ miniMapData = []

    music Jail_Clock
    if police_cell1_monica_breath == True:
        music2 audio_woman_breathing_painfully

    $ cageInteractCnt = cageInteractAmount
    $ scene_image = "scene_Police_Cell3"
    return

label police_cell3_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Police_Cell3_Monica_[cloth]_[monicaPoliceCell3Suffix]", "click" : "police_cell3_environment", "actions" : "l", "zorder" : 10}, scene="police_cell3")

    $ add_object_to_scene("Cage", {"type":2, "base":"Police_Cell_3_Cage", "click" : "police_cell3_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="police_cell3")
    $ add_object_to_scene("Teleport_Cage2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "police_cell3_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="police_cell3")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_cell3_teleport:
    if obj_name == "Teleport_Cage2":
        call change_scene("police_cell2", "Fade_long") from _call_change_scene_383
        return
    return

label police_cell3_environment:
    if obj_name == "Cage":
        $ cageInteractCnt = cageInteractCnt - 1
        if cageInteractCnt > 0:
            sound snd_jail_door_locked
            with vpunch
            return
        sound snd_jail_door_locked
        call process_hooks("cage_interact", "police") from _call_process_hooks_72
        $ cageInteractCnt = cageInteractAmount
        return
    if obj_name == "Monica":
        mt "Надо дергать эту проклятую решетку!"
        mt "Иначе меня никто не услышит!"
    return
