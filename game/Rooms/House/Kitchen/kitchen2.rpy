label kitchen2:
    $ print "enter_kitchen2"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate

    $ scene_image = "scene_Kitchen2[day_suffix]"
    music Mandeville
    return

label kitchen2_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Kitchen2_Monica_[cloth]", "click" : "kitchen_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Accessories", {"type":2, "base":"Kitchen2_Accessories", "click" : "kitchen2_environment", "actions" : "l", "zorder": 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Cupboard", {"type":2, "base":"Kitchen2_Cupboard", "click" : "kitchen2_environment", "actions" : "l", "zorder": 0, "group":"environment"})
    $ add_object_to_scene("Chair1", {"type":2, "base":"Kitchen2_Chair1", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Kitchen2_Chair2", "click" : "kitchen2_environment", "actions" : "lh", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chandelier", {"type":2, "base":"Kitchen2_Chandelier", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Kitchen2_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.2, "group":"environment"})
    $ add_object_to_scene("Dinner_Table", {"type":2, "base":"Kitchen2_Dinner_Table", "click" : "kitchen2_environment", "actions" : "lh", "zorder" : 11, "group":"environment"})
    $ add_object_to_scene("Food", {"type":2, "base":"Kitchen2_Food", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Fridge", {"type":2, "base":"Kitchen2_Fridge", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":0.2, "c":1.8, "group":"environment"})
    $ add_object_to_scene("Sink", {"type":2, "base":"Kitchen2_Sink", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Small_Chairs", {"type":2, "base":"Kitchen2_Small_Chairs", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type":2, "base":"Kitchen2_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.03, "group":"environment"})

    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "kitchen_teleport", "xpos" : 210, "ypos" : 520, "zorder":11})
    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":12, "teleport":True})

    return

label kitchen2_environment:
    if monicaKitchenForbidden == True:
        if get_active_objects("Betty", scene="House", recursive=True) != False:
            call afterJailHouse_dialogue15a() from _call_afterJailHouse_dialogue15a
            return
        call ep22_dialogue1_5_kitchen() from _call_ep22_dialogue1_5_kitchen
        return
    return
