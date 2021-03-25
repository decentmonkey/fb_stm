label basement_laundry_washmachine:
    $ print "basement_laundry_washmachine"
    $ miniMapData = []

    $ scene_image = "scene_Basement_Laundry_WashMachine"

#    music Mandeville
    return

label basement_laundry_washmachine_init:
    $ add_object_to_scene("RevengeKeys", {"type" : 2, "base" : "Basement_Laundry_WashMachine_Keys", "click" : "basement_laundry_washmachine_environment", "actions" : "lh", "zorder":10, "b":0.5}, scene="basement_laundry_washmachine")
    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_washmachine_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="basement_laundry_washmachine")

    return

label basement_laundry_washmachine_teleport:
    if obj_name == "Teleport_Basement_Laundry":
        call change_scene("basement_laundry") from _rcall_change_scene_62
        return

    return

label basement_laundry_washmachine_environment:
    if obj_name == "RevengeKeys":
        if act=="l":
            mt "Какие-то ключи..."
            return
    return
