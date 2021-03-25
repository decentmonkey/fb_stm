default basement_bedroom_table_opened_buttplug_suffix = 1

label basement_bedroom_table_opened:
    $ print "basement_bedroom_table_opened"
    $ miniMapData = []

    $ scene_image = "scene_Basement_Bedroom_Table_Opened_Gun"

#    music Mandeville
    return

label basement_bedroom_table_opened_init:
    $ add_object_to_scene("Gun", {"type" : 2, "base" : "Basement_Bedroom_Table_Opened_Gun", "click" : "basement_bedroom_table_opened_environment", "actions" : "lh", "zorder":10}, scene="basement_bedroom_table_opened")
    $ add_object_to_scene("ButtPlug", {"type" : 2, "base" : "Basement_Bedroom_Table_Opened_ButtPlug[basement_bedroom_table_opened_buttplug_suffix]", "click" : "basement_bedroom2_environment", "actions" : "lh", "zorder":10, "active":False}, scene="basement_bedroom_table_opened")

    $ add_object_to_scene("Teleport_Basement_Bedroom2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom_table_opened_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="basement_bedroom_table_opened")

    return

label basement_bedroom_table_opened_teleport:
    if obj_name == "Teleport_Basement_Bedroom2":
        call change_scene("basement_bedroom2", "Fade_long", "desk_close") from _rcall_change_scene_61
        return

    return

label basement_bedroom_table_opened_environment:
    if obj_name == "Gun":
        if act=="l":
            mt "Это... Пистолет???"
            return
    return
