label floor1_fountain:
    $ print "enter_floor1_fountain"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_1

    $ scene_image = "scene_Floor1_Fountain[day_suffix]"
    music snd_fountain_music
    return

label floor1_fountain_init:
    $ add_object_to_scene("Fountain", {"type":2, "base":"Floor1_Fountain_Fountain", "click" : "floor1_fountain_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Floor1_Fountain_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.2, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Fountain_Lamps", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type":2, "base":"Floor1_Fountain_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture", {"type":2, "base":"Floor1_Fountain_Picture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Fountain_Furniture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Fountain_Bardie[day_suffix]", "click" : "bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "active":False})

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor1_fountain_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label floor1_fountain_teleport:
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1") from _call_change_scene_18
        return

label floor1_fountain_environment:
    if obj_name == "Fountain":
        m "Люстра может упасть только в фонтан."

        "Но я же не полезу в него, верно?"
        return
    return
