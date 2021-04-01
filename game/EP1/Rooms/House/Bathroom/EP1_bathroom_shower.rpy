label EP1_bathroom_shower:
    $ print "enter_bathroom_shower"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "bathroom_shower"
    $ scene_caption = t_("Bathroom Shower")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Bathroom_Shower_Monica_" + cloth

    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Shower_Monica_" + cloth, "click" : "EP1_bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})


    $ EP1_add_object_to_scene("Shower", {"type":2, "base":"Bathroom_Shower_Shower", "click" : "EP1_bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_bathroom_teleport", "xpos" : 990, "ypos" : 956, "zorder":11, "high_sprite_hover": True})
    $ EP1_add_object_to_scene("Teleport_Bathroom_Bath", {"type":3, "text" : t_("ВАННА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "EP1_bathroom_teleport", "xpos" : 240, "ypos" : 520, "zorder":11})

    return
