label street_victoriahome:

    $ print "enter_street_victoriahome"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_VictoriaHome[day_suffix]"
    $ scene_sound = "streets_sound"
    return

label street_victoriahome_init:
    $ add_object_to_scene("VictoriaHome_Enter", {"type":2, "base":"Street_VictoriaHome_Enter", "click" : "street_victoriahome_teleport", "actions" : "lw", "b":0.12, "tint":[1.0, 1.0, 0.8], "zorder" : 0})
    $ add_object_to_scene("DickBuilding", {"type":2, "base":"Street_VictoriaHome_DickBuilding", "click" : "street_victoriahome_environment", "actions" : "l", "zorder" : 1, "b":0.12, "tint":[1.0, 1.0, 0.8], "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_victoriahome_teleport:
    if obj_name == "VictoriaHome_Enter":
        if act == "l":
            call ep216_dialogues5_victoria_9() from _rcall_ep216_dialogues5_victoria_9
        else:
            call ep216_dialogues5_victoria_10() from _rcall_ep216_dialogues5_victoria_10
    return
label street_victoriahome_environment:
    if obj_name == "DickBuilding":
        call ep216_dialogues5_victoria_11() from _rcall_ep216_dialogues5_victoria_11
    return
