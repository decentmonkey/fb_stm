default monicaPoliceCell2Suffix = 2
default monicaPoliceCellSuffixMode = 0

default policeCell2PrisonersYell = False

label police_cell2:
    $ print "enter_police_cell2"
    $ miniMapData = []

    $ scene_image = "scene_Police_Cell2_Prisoners"

    music Jail_Clock
    if police_cell1_monica_breath == True:
        music2 audio_woman_breathing_painfully
    if policeCell2PrisonersYell == True:
        music2 prison_yell_music
    if monicaPoliceCellSuffixMode == 0:
        if monicaPoliceCell2Suffix == 2 or monicaPoliceCell2Suffix == 3:
            $ rand1 = rand(2,3)
            $ monicaPoliceCell2Suffix = rand1

    if monicaPoliceCellSuffixMode == 1:
        $ rand1 = rand(1,2)
        $ monicaPoliceCell2Suffix = rand1

    if get_active_objects("Prisoner1", scene="police_cell1") != False:
        $ set_active("Prisoner1", True)

    else:
        $ set_active("Prisoner1", False)
    return

label police_cell2_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Police_Cell2_Monica_[cloth]_[monicaPoliceCell2Suffix]", "click" : "police_cell1_environment", "actions" : "l", "zorder" : 10}, scene="police_cell2")

    $ add_object_to_scene("Bed", {"type":2, "base":"Police_Cell_2_Bed", "click" : "police_cell1_environment", "actions" : "lh", "zorder" : 0, "group":"environment"}, scene="police_cell2")

    $ add_object_to_scene("Cage", {"type":2, "base":"Police_Cell_2_Cage", "click" : "police_cell2_teleport", "actions" : "lw", "zorder" : 0, "group":"environment", "teleport":True}, scene="police_cell2")
    $ add_object_to_scene("Teleport_Cage1", {"type":3, "text" : t_("КАМЕРА"), "rarrow" : "arrow_left_2", "base":"empty", "click" : "police_cell2_teleport", "xpos" : 210, "ypos" : 326, "zorder":5, "teleport":True}, scene="police_cell2")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_cell2_init2:
    $ add_object_to_scene("Prisoner1", {"type":2, "base":"Police_Cell2_Prisoner1_[prisoner1Cell1Suffix]", "click" : "police_cell1_environment", "actions" : "lt", "zorder" : 12, "active":False}, scene="police_cell2")
    return

label police_cell2_teleport:
    if obj_name == "Teleport_Cage1":
        call change_scene("police_cell1", "Fade_long") from _call_change_scene_378
        return
    if obj_name == "Cage":
        if act=="l":
            mt "Надо дергать эту проклятую решетку!"
            mt "Иначе меня никто не услышит!"
        if act=="w":
            call change_scene("police_cell3") from _call_change_scene_379
            return
    return

label police_cell2_environment:

    return
