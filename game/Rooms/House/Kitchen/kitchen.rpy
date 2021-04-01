default monicaKitchenForbidden = True

label kitchen:
    $ print "enter_kitchen"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_7

    $ scene_image = "scene_Kitchen[day_suffix]"
    music Mandeville

#    if gameStage > 2:
#        if monicaKitchenForbidden == True and scene_name != lastSceneName:
#            $ autorun_to_object(scene_name, "afterJailHouse_dialogue15")
    return

label kitchen_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Kitchen_Monica_[cloth]", "click" : "kitchen_environment", "actions" : "l", "zorder":12, "tint": monica_tint})

    $ add_object_to_scene("Food", {"type":2, "base":"Kitchen_Food", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Fridge", {"type":2, "base":"Kitchen_Fridge", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":0.2, "c":1.8, "group":"environment"})
    $ add_object_to_scene("Gas_Cooker", {"type":2, "base":"Kitchen_Gas_Cooker", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Kitchen_Lamps", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":-0.15, "group":"environment"})
    $ add_object_to_scene("Microwave_Oven", {"type":2, "base":"Kitchen_Microwave_Oven", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Plates", {"type":2, "base":"Kitchen_Plates", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Ventilation", {"type":2, "base":"Kitchen_Ventilation", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Drawers", {"type":2, "base":"Kitchen_Drawers", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Wine", {"type":2, "base":"Kitchen_Wine", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Kitchen2", {"type":3, "text" : t_("ОБЕДЕННЫЙ СТОЛИК"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "kitchen_teleport", "xpos" : 1620, "ypos" : 520, "zorder":15})


    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label kitchen_teleport:
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1") from _call_change_scene_73
        return
    if obj_name == "Teleport_Kitchen2":
        call change_scene("kitchen2") from _call_change_scene_74
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("kitchen") from _call_change_scene_75
        return

label kitchen_environment:
    if monicaKitchenForbidden == True:
        if get_active_objects("Betty", scene="House", recursive=True) != False:
            call afterJailHouse_dialogue15a() from _call_afterJailHouse_dialogue15a_1
            return
        call ep22_dialogue1_5_kitchen() from _call_ep22_dialogue1_5_kitchen_1
        return
    return
