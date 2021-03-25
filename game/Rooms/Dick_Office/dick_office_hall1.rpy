default dickOfficeHallMonicaSuffix = 1

label dick_office_hall1:
    $ print "dick_office_hall1"
    $ miniMapData = []
    $ scene_image = "scene_Office_Dick_Hall1"

    return

label dick_office_hall1_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Hall1_Monica_[cloth]_[dickOfficeHallMonicaSuffix]", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Door", {"type":2, "base":"Office_Dick_Hall1_Door", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Exhibit1", {"type":2, "base":"Office_Dick_Hall1_Exhibit1", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Exhibit2", {"type":2, "base":"Office_Dick_Hall1_Exhibit2", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Exhibit3", {"type":2, "base":"Office_Dick_Hall1_Exhibit3", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Exhibit4", {"type":2, "base":"Office_Dick_Hall1_Exhibit4", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Entrance", {"type":3, "text" : t_("ЛИФТ ВНИЗ"), "rarrow" : "arrow_down_2", "base":"Office_Dick_Hall1_Teleport_Entrance", "click" : "dick_office_hall1_teleport", "xpos" : 1534, "ypos" : 781, "zorder":9, "teleport":True})
    $ add_object_to_scene("Teleport_Secretary", {"type":3, "text" : t_("СЕКРЕТАРЬ ДИКА"), "larrow" : "arrow_left_2", "base":"Office_Dick_Hall1_Teleport_Secretary", "click" : "dick_office_hall1_teleport", "xpos" : 273, "ypos" : 850, "zorder":9, "teleport":True})

    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_hall1_teleport:
    if obj_name == "Teleport_Entrance":
        call change_scene("dick_office_entrance", "Fade_long", "snd_lift") from _call_change_scene_178
        return
    if obj_name == "Teleport_Secretary":
        call change_scene("dick_office_secretary") from _call_change_scene_179
        return
    return
label dick_office_hall1_environment:
    if obj_name == "Monica":
        mt "Галстук..."
        mt "(хмык)"
        return
    if obj_name == "Door":
        sound snd_door_locked1
        mt "Хм.. закрыто..."
        "Что это за дверь?"
        "Куда она ведет?"
    if obj_name == "Exhibit1" or obj_name == "Exhibit2" or obj_name == "Exhibit3" or obj_name == "Exhibit4":
        mt "Что это такое?"
        "Какие-то экспонаты?"
        "Это нравится Дику???"
    return
