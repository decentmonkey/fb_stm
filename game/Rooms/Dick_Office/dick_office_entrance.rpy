default dickReceptionStage = 0
default dickReceptionMonicaSuffix = 1

label dick_office_entrance:
    $ print "dick_office_entrance"
    $ miniMapData = []

    $ scene_image = "scene_Office_Dick_Entrance"
    music Groove2_85
    return

label dick_office_entrance_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_[cloth]_[dickReceptionMonicaSuffix]", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_[dickReceptionMonicaSuffix]", "click" : "dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})

    $ add_object_to_scene("Desk", {"type":2, "base":"Office_Dick_Entrance_Desk", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Flower", {"type":2, "base":"Office_Dick_Entrance_Flower", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Paint", {"type":2, "base":"Office_Dick_Entrance_Paint", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Vase", {"type":2, "base":"Office_Dick_Entrance_Vase", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chandelier", {"type":2, "base":"Office_Dick_Entrance_Chandelier", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Inside", {"type":3, "text" : t_("ОФИСЫ"), "rarrow" : "arrow_right_2", "base":"Office_Dick_Entrance_Teleport_Inside", "click" : "dick_office_entrance_teleport", "xpos" : 1530, "ypos" : 190, "zorder":9, "teleport":True})
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НА УЛИЦУ"), "larrow" : "arrow_left_2", "base":"Office_Dick_Entrance_Teleport_Street", "click" : "dick_office_entrance_teleport", "xpos" : 647, "ypos" : 190, "zorder":9, "teleport":True})
    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_entrance_teleport:
    if obj_name == "Teleport_Inside":
        call change_scene("dick_office_hall1", "Fade_long", "snd_lift") from _call_change_scene_163
        return
    if obj_name == "Teleport_Street":
        call change_scene("street_dick_office") from _call_change_scene_164
    return
label dick_office_entrance_environment:
    if obj_name == "Monica":
        mt "Здесь обитает Дик..."
    if obj_name == "Reception":
        if act == "l":
            mt "Мне кажется она старовата для работы здесь."
            "Хотя для своего возраста она выглядит неплохо."
        if act == "t":
            if get_active_objects("DickTheLawyer", scene="dick_office_cabinet") != False:
                reception_secretary "Мэм."
                "Проходите."
            else:
                reception_secretary "Мэм, я могу Вам чем-то помочь?"
                mt "..."
            return

    if obj_name == "Desk":
        mt "За этой стойкой находится рецепшин на входе в офисное здание Дика."
    if obj_name == "Flower":
        mt "Красивый цветок, но мне сейчас не до красоты..."
    if obj_name == "Paint":
        mt "Надо же? Фото-картина в здании Дика?"
        "Не ожидала от этого толстяка..."
        "Но мне сейчас не до этого!"
    if obj_name == "Vase":
        mt "Ваза... Судя по виду дорогая..."
    if obj_name == "Chandelier":
        mt "Хорошо что я вовремя заметила эту огромную люстру!"
        "Я буду обходить это место..."
    return
