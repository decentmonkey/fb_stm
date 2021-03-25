default melanieHomeInit2_completed = False
default melanieHomeMelanieSuffix = ""
label melanie_home:
    $ print "enter_melanie_home"
    $ miniMapData = []
    if melanieHomeInit2_completed == True:
        music ZigZag
    $ scene_image = "scene_MelanieHome"
    return

label melanie_home_init:
    return


label melanie_home_init2:
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "MelanieHome_Melanie[melanieHomeMelanieSuffix]_[melanie_cloth]", "click" : "melanie_home_environment", "actions" : "l", "zorder":10}, scene="melanie_home")
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "MelanieHome_Monica_[cloth]", "click" : "melanie_home_environment", "actions" : "l", "zorder":10, "active":False}, scene="melanie_home")
    $ add_object_to_scene("Victoria", {"type" : 2, "base" : "MelanieHome_Victoria", "click" : "melanie_home_environment", "actions" : "l", "zorder":10, "active":False}, scene="melanie_home")

    $ add_object_to_scene("Chair", {"type" : 2, "base" : "MelanieHome_Chair", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Lamp1", {"type" : 2, "base" : "MelanieHome_Lamp1", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Lamp2", {"type" : 2, "base" : "MelanieHome_Lamp2", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Photo1", {"type" : 2, "base" : "MelanieHome_Photo1", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Photo2", {"type" : 2, "base" : "MelanieHome_Photo2", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Photo3", {"type" : 2, "base" : "MelanieHome_Photo3", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Photo4", {"type" : 2, "base" : "MelanieHome_Photo4", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Photo5", {"type" : 2, "base" : "MelanieHome_Photo5", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Sofa", {"type" : 2, "base" : "MelanieHome_Sofa", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Sofa2", {"type" : 2, "base" : "MelanieHome_Sofa2", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("TV", {"type" : 2, "base" : "MelanieHome_TV", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"}, scene="melanie_home")
    $ add_object_to_scene("Wine", {"type" : 2, "base" : "MelanieHome_Wine1", "click" : "melanie_home_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment", "active":False}, scene="melanie_home")

    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("В ГОРОД"), "larrow" : "arrow_left_2", "base":"empty", "click" : "melanie_home_teleport", "xpos" : 170, "ypos" : 986, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="melanie_home")
    $ melanieHomeInit2_completed = True

    return

label melanie_home_teleport:
    if obj_name == "Teleport_Map":
        call map_show() from _rcall_map_show_1
    return

label melanie_home_environment:
    return
