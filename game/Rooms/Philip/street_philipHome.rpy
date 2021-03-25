default streetPhilipHomeMonicaSuffix = 1
default streetPhilipHomeBitch1Suffix = 1

label street_philiphome:
    $ print "enter_street_philiphome"
    $ miniMapData = []

    $ sceneIsStreet = True

    $ scene_image = "scene_Street_PhilippHome[day_suffix]"
    music Groove2_85
    return


label street_philiphome_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_PhilippHome_Monica_[cloth]_[streetPhilipHomeMonicaSuffix][day_suffix]", "click" : "street_philiphome_environment", "actions" : "l", "zorder" : 10}, scene="street_philiphome")
    $ add_object_to_scene("Bitch1", {"type":2, "base":"Street_PhilippHome_Monica_Bitch1_[streetPhilipHomeBitch1Suffix][day_suffix]", "click" : "street_philiphome_environment", "actions" : "lt", "zorder" : 5, "active":False}, scene="street_philiphome")

    $ add_object_to_scene("Teleport_Building", {"type":3, "text" : t_("ВХОД"), "larrow" : "arrow_left_2", "base":"Street_PhilippHome_Enter", "click" : "street_philiphome_teleport", "xpos" : 1586, "ypos" : 432, "zorder":15, "teleport":True}, scene="street_philiphome")
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("В ГОРОД"), "larrow" : "arrow_left_2", "base":"empty", "click" : "street_philiphome_teleport", "xpos" : 130, "ypos" : 986, "zorder":15, "teleport":True, "high_sprite_hover":True}, scene="street_philiphome")
    return

label street_philiphome_teleport:
    if obj_name == "Teleport_Map":
        call map_show() from _rcall_map_show
        return
    return

label street_philiphome_environment:
    if obj_name == "Monica":
        if monica_philip_visited_last_day == day:
            call ep210_dialogues2_escort_start_Phillip_20() from _rcall_ep210_dialogues2_escort_start_Phillip_20
            return
        call ep210_dialogues2_escort_start_Phillip_10() from _rcall_ep210_dialogues2_escort_start_Phillip_10

    if obj_name == "Bitch1":
        mt "Дешевая шлюха, которая приходит к Филиппу."
        mt "Как можно пасть так низко, Фу!"
    return
