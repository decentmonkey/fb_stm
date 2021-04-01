default policeJailObjectsEnabled = True
default policeJailObjectsBed1Enabled = True
default policeJailObjectsTeleportForced = False
label EP1_police_jail_scene:
    $ print "enter_police_jail_scene"
    $ miniMapData = []

    $ scene_name = "police_jail_scene"
    $ scene_caption = t_("JAIL")
    $ clear_scene_from_objects(scene_name)

    if jailScenePlace == 0:
        $ scene_image = policeCellStageName1
        $ EP1_add_object_to_scene("Monica", {"type":2, "base": policeCellMonica1, "click" : policeCellMonicalabel, "actions" : "l", "zorder" : 10})
        if policeJailObjectsBed1Enabled == True:
            $ EP1_add_object_to_scene("Bed1", {"type":2, "base":"Police_Cell_1_Bed", "click" : policeCellBedlabel, "actions" : "lh", "zorder" : 1})
        if policeJailObjectsEnabled == True:
            $ EP1_add_object_to_scene("Bed2", {"type":2, "base":"Police_Cell_1_Bed2", "click" : policeCellBed2label, "actions" : "l", "zorder" : 1})
            $ EP1_add_object_to_scene("Lamp", {"type":2, "base":"Police_Cell_1_Lamp", "click" : policeCellLamplabel, "actions" : "lh", "zorder" : 1})
            $ EP1_add_object_to_scene("Sortir", {"type":2, "base":"Police_Cell_1_Sortir", "click" : policeCellSortirlabel, "actions" : "lh", "zorder" : 1})
            $ EP1_add_object_to_scene("Teleport_Cage", {"type":3, "text" : t_("РЕШЕТКА"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "EP1_police_jail_scene_teleport", "xpos" : 1680, "ypos" : 233, "zorder":5})
        if policeJailObjectsTeleportForced == True:
            $ EP1_add_object_to_scene("Teleport_Cage", {"type":3, "text" : t_("РЕШЕТКА"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "EP1_police_jail_scene_teleport", "xpos" : 1680, "ypos" : 233, "zorder":5})

    if jailScenePlace == 1:
        $ scene_image = policeCellStageName2
        $ EP1_add_object_to_scene("Monica", {"type":2, "base": policeCellMonica2, "click" : policeCellMonicalabel, "actions" : "l", "zorder" : 10})
        if policeJailObjectsBed1Enabled == True:
            $ EP1_add_object_to_scene("Bed1", {"type":2, "base":"Police_Cell_2_Bed", "click" : policeCellBedlabel, "actions" : "lh", "zorder" : 1})
        if policeJailObjectsEnabled == True:
            $ EP1_add_object_to_scene("Bed2", {"type":2, "base":"Police_Cell_2_Bed2", "click" : policeCellBed2label, "actions" : "l", "zorder" : 1})
            $ EP1_add_object_to_scene("Cage", {"type":2, "base":"Police_Cell_2_Cage", "click" : policeCellCagelabel, "actions" : "lw", "zorder" : 1})
            $ EP1_add_object_to_scene("Teleport_Bed", {"type":3, "text" : t_("КАМЕРА"), "larrow" : "arrow_left_2", "base":"empty", "click" : "EP1_police_jail_scene_teleport", "xpos" : 190, "ypos" : 326, "zorder":5})
        if policeJailObjectsTeleportForced == True:
            $ EP1_add_object_to_scene("Teleport_Bed", {"type":3, "text" : t_("КАМЕРА"), "larrow" : "arrow_left_2", "base":"empty", "click" : "EP1_police_jail_scene_teleport", "xpos" : 190, "ypos" : 326, "zorder":5})
#        $ EP1_add_object_to_scene("Prisoners", {"type":2, "base": "Police_Cell_2_Prisoners", "base_mask":"empty", "click" : "EP1_police_jail_scene_environment", "actions" : "l", "zorder" : 1})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_police_jail_scene_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Cage":
        if jailDay == 1 and jailDaySceneStage == 0:
            $ jailDaySceneStage = 1
            call EP1_jail_day1_2()
            return
        if jailDay == 1 and jailDaySceneStage == 1:
            call EP1_jail_day1_3()
            $ jailScenePlace = 1
            call EP1_change_scene(scene_name, "Fade", False)
            return

        $ jailScenePlace = 1
        call EP1_change_scene(scene_name, "Fade", False)
#        call EP1_change_scene(scene_name, "Fade", "barefoot_walk2")
        return
    if obj_name == "Teleport_Bed":
        $ jailScenePlace = 0
        call EP1_change_scene(scene_name, "Fade", False)
#        call EP1_change_scene(scene_name, "Fade", "barefoot_walk3")
        return

    return
label EP1_police_jail_scene_environment(obj_name, obj_data):
    return
