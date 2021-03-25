default dickOfficeSecretaryMonicaSuffix = 1
default dickOfficeSecretarySecretarySuffix = 1

label dick_office_secretary:
    $ print "dick_office_secretary"
    $ miniMapData = []
    $ scene_image = "scene_Office_Dick_Secretary"
    return

label dick_office_secretary_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Secretary_Monica_Secretary_Monica_[cloth]_[dickOfficeSecretaryMonicaSuffix]", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("DickSecretary", {"type":2, "base":"Office_Dick_Secretary_Secretary_[dickOfficeSecretarySecretarySuffix]", "click" : "dick_office_secretary_environment", "actions" : "lt", "zorder" : 0})

    $ add_object_to_scene("Computer", {"type":2, "base":"Office_Dick_Secretary_Computer", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1, "group":"environment", "active":False})
    $ add_object_to_scene("Papers", {"type":2, "base":"Office_Dick_Secretary_Papers", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1, "group":"environment", "active":False})
    $ add_object_to_scene("Phone", {"type":2, "base":"Office_Dick_Secretary_Phone", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1, "group":"environment", "active":False})
    $ add_object_to_scene("Printer", {"type":2, "base":"Office_Dick_Secretary_Printer", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1, "group":"environment", "active":False})
    $ add_object_to_scene("Terminal", {"type":2, "base":"Office_Dick_Secretary_Terminal", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1, "group":"environment", "active":False})

    $ add_object_to_scene("Door", {"type":2, "base":"Office_Dick_Secretary_Door", "click" : "dick_office_secretary_teleport", "actions" : "lw", "zorder" : 0, "teleport":True})

    $ add_object_to_scene("Teleport_Hall", {"type":3, "text" : t_("НАЗАД В ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "dick_office_secretary_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_secretary_teleport:
    if obj_name == "Teleport_Hall":
        call change_scene("dick_office_hall1") from _call_change_scene_180
        return
    if obj_name == "Door":
        if act == "l":
            mt "Дверь... за ней должен быть Дик..."
            return

        if act == "w":
            call change_scene("dick_office_cabinet") from _call_change_scene_181
        return
    return
label dick_office_secretary_environment:
    if obj_name == "Monica":
        if monicaBitch == True:
            mt "Эта сучка много на себя берет!"
        else:
            mt "Она много на себя берет!"
        return

    if obj_name == "DickSecretary":
        if act == "l":
            if monicaBitch == True:
                mt "Эта сучка много на себя берет!"
            else:
                mt "Она много на себя берет!"
#            mt "(хмык)"
            return
        if act == "t":
            return

    if obj_name == "Computer":
        mt "Когда эта дура пялится в компьютер, выражение ее лица особенно глупое..."
    if obj_name == "Papers":
        mt "Какие-то никчемные бумажки!"
        return
    if obj_name == "Phone":
        mt "Какой смешной старый телефон!"
        return
    if obj_name == "Printer":
        mt "Похоже здесь эта сучка печатает документы Дику на подпись."
    if obj_name == "Terminal":
        mt "Терминал?"
        "Для записи на прием?"
        return
    return
