default dickReceptionStage = 0
default dickReceptionVisited = False
default dickReceptionWhoreTalked = False

label EP1_dick_office_entrance:
    $ print "dick_office_entrance"
    $ miniMapData = []

    $ scene_name = "dick_office_entrance"
    $ scene_caption = t_("Dick's Office Reception")
    $ clear_scene_from_objects(scene_name)
    if dickReceptionStage == 0 or dickReceptionStage == 2 or dickReceptionStage == 3 or dickReceptionStage == 4:
        $ scene_image = "scene_Office_Dick_Entrance_Monica_Reception_AfterJail_1"
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_1_Monica", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
        $ EP1_add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_1_Reception", "click" : "EP1_dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})
    if dickReceptionStage == 1:
        $ scene_image = "scene_Office_Dick_Entrance_Monica_Reception_AfterJail_2"
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_2_Monica", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
        $ EP1_add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_2_Reception", "click" : "EP1_dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})
    if dickReceptionStage == 5:
        $ scene_image = "scene_Office_Dick_Entrance_Monica_Reception_Whore_1"
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_Whore_1", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
        $ EP1_add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_2_Reception", "click" : "EP1_dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})


    $ EP1_add_object_to_scene("Desk", {"type":2, "base":"Office_Dick_Entrance_Desk", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flower", {"type":2, "base":"Office_Dick_Entrance_Flower", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Paint", {"type":2, "base":"Office_Dick_Entrance_Paint", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Vase", {"type":2, "base":"Office_Dick_Entrance_Vase", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chandelier", {"type":2, "base":"Office_Dick_Entrance_Chandelier", "click" : "EP1_dick_office_entrance_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Inside", {"type":3, "text" : t_("ОФИСЫ"), "rarrow" : "arrow_right_2", "base":"Office_Dick_Entrance_Teleport_Inside", "click" : "EP1_dick_office_entrance_teleport", "xpos" : 1530, "ypos" : 190, "zorder":9})
    $ EP1_add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НА УЛИЦУ"), "larrow" : "arrow_left_2", "base":"Office_Dick_Entrance_Teleport_Street", "click" : "EP1_dick_office_entrance_teleport", "xpos" : 647, "ypos" : 190, "zorder":9})
    music Groove2_85
    if dickReceptionVisited == False:
        hide screen Rain
        call EP1_after_jail_dick_reception_dialogue0()
#        $ EP1_autorun_to_object("dick_office_entrance", "after_jail_dick_reception_dialogue0")
        $ dickReceptionVisited = True
    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label EP1_dick_office_entrance_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if dickReceptionStage == 0:
            call EP1_after_jail_dick_reception_dialogue1()
            return
        if dickReceptionStage == 1:
            mt "Дика нет..."
            "Надо придти к нему завтра..."
        if dickReceptionStage == 2:
            call EP1_afterJail_Day2_DickOffice_entrance_dialogue1()
            return
        if dickReceptionStage == 3:
            if dickOfficeHallVisited == False:
                $ EP1_autorun_to_object("dick_office_hall1", "dick_office_hall1_dialogue1")
            if dickOfficeSecretaryMonicaStage <= 7:
                music Stealth_Groover

            call EP1_change_scene("dick_office_hall1", "Fade_long", "snd_lift")
            return
        if dickReceptionStage == 4:
            call EP1_afterJail_Day2_DickOffice_entrance_dialogue3()
            return
        if dickReceptionStage == 5:
            if dickReceptionWhoreTalked == False:
                call EP1_dickAfterJail_entrance_dialogue1()
                return
            call EP1_change_scene("dick_office_hall1", "Fade_long", "snd_lift")
    if obj_name == "Teleport_Street":
        if dickReceptionStage == 1:
            $ dickReceptionStage = 0
        call EP1_change_scene("street_dick_office")
    return
label EP1_dick_office_entrance_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if dickReceptionStage == 1:
            mt "Значит Дик будет только завтра..."
            "Но где же мне ночевать, черт возьми!!!"
            return
        mt "Здесь обитает Дик..."
    if obj_name == "Reception":
        if act == "l":
            mt "Мне кажется она старовата для работы здесь."
            "Хотя для своего возраста она выглядит неплохо."
        if act == "t":
            if dickReceptionStage == 0:
                call EP1_after_jail_dick_reception_dialogue1()
                return
            if dickReceptionStage == 1:
                mt "Дика нет..."
                "Надо придти к нему завтра..."
            if dickReceptionStage == 2:
                call EP1_afterJail_Day2_DickOffice_entrance_dialogue1()
                return
            if dickReceptionStage == 3:
                if dickOfficeSecretaryMonicaStage > 0:
                    call EP1_afterJail_Day2_DickOffice_entrance_dialogue3_a()
                    return
                call EP1_afterJail_Day2_DickOffice_entrance_dialogue2()
                return
            if dickReceptionStage == 4:
                call EP1_afterJail_Day2_DickOffice_entrance_dialogue3()
                return
            if dickReceptionStage == 5:
                if dickReceptionWhoreTalked == False:
                    call EP1_dickAfterJail_entrance_dialogue1()
                    return
                reception_secretary "Мэм."
                "Проходите."
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
