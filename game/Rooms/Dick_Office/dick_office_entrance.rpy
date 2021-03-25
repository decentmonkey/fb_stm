default dickReceptionStage = 0
default dickReceptionMonicaSuffix = 1

label dick_office_entrance:
    if EP1==True:
        jump dick_office_entrance_EP1
    $ print "dick_office_entrance"
    $ miniMapData = []

    $ scene_image = "scene_Office_Dick_Entrance"
    music Groove2_85
    return

label dick_office_entrance_init:
    if EP1==True:
        return
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
    if EP1==True:
        jump dick_office_entrance_teleport_EP1
    if obj_name == "Teleport_Inside":
        call change_scene("dick_office_hall1", "Fade_long", "snd_lift") from _call_change_scene_163
        return
    if obj_name == "Teleport_Street":
        call change_scene("street_dick_office") from _call_change_scene_164
    return
label dick_office_entrance_environment:
    if EP1==True:
        jump dick_office_entrance_environment_EP1
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


# EP1
default dickReceptionVisited = False
default dickReceptionWhoreTalked = False

label dick_office_entrance_EP1:
    $ print "dick_office_entrance"
    $ miniMapData = []

    $ scene_name = "dick_office_entrance"
    $ scene_caption = t_("Dick's Office Reception")
    $ clear_scene_from_objects(scene_name)
    if dickReceptionStage == 0 or dickReceptionStage == 2 or dickReceptionStage == 3 or dickReceptionStage == 4:
        $ scene_image = "scene_Office_Dick_Entrance_Monica_Reception_AfterJail_1"
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_1_Monica", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_1_Reception", "click" : "dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})
    if dickReceptionStage == 1:
        $ scene_image = "scene_Office_Dick_Entrance_Monica_Reception_AfterJail_2"
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_2_Monica", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_2_Reception", "click" : "dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})
    if dickReceptionStage == 5:
        $ scene_image = "scene_Office_Dick_Entrance_Monica_Reception_Whore_1"
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_Whore_1", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Reception", {"type":2, "base":"Office_Dick_Entrance_Monica_Reception_AfterJail_2_Reception", "click" : "dick_office_entrance_environment", "actions" : "lt", "zorder" : 10})


    $ add_object_to_scene("Desk", {"type":2, "base":"Office_Dick_Entrance_Desk", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Flower", {"type":2, "base":"Office_Dick_Entrance_Flower", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Paint", {"type":2, "base":"Office_Dick_Entrance_Paint", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Vase", {"type":2, "base":"Office_Dick_Entrance_Vase", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chandelier", {"type":2, "base":"Office_Dick_Entrance_Chandelier", "click" : "dick_office_entrance_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Inside", {"type":3, "text" : t_("ОФИСЫ"), "rarrow" : "arrow_right_2", "base":"Office_Dick_Entrance_Teleport_Inside", "click" : "dick_office_entrance_teleport", "xpos" : 1530, "ypos" : 190, "zorder":9})
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НА УЛИЦУ"), "larrow" : "arrow_left_2", "base":"Office_Dick_Entrance_Teleport_Street", "click" : "dick_office_entrance_teleport", "xpos" : 647, "ypos" : 190, "zorder":9})
    music Groove2_85
    if dickReceptionVisited == False:
        hide screen Rain
        call after_jail_dick_reception_dialogue0() from _call_after_jail_dick_reception_dialogue0
#        $ autorun_to_object("dick_office_entrance", "after_jail_dick_reception_dialogue0")
        $ dickReceptionVisited = True
    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_entrance_teleport_EP1:
    if obj_name == "Teleport_Inside":
        if dickReceptionStage == 0:
            call after_jail_dick_reception_dialogue1() from _call_after_jail_dick_reception_dialogue1
            return
        if dickReceptionStage == 1:
            mt "Дика нет..."
            "Надо придти к нему завтра..."
        if dickReceptionStage == 2:
            call afterJail_Day2_DickOffice_entrance_dialogue1() from _call_afterJail_Day2_DickOffice_entrance_dialogue1
            return
        if dickReceptionStage == 3:
            if dickOfficeHallVisited == False:
                $ autorun_to_object("dick_office_hall1", "dick_office_hall1_dialogue1")
            if dickOfficeSecretaryMonicaStage <= 7:
                music Stealth_Groover

            call change_scene("dick_office_hall1", "Fade_long", "snd_lift") from _call_change_scene_147
            return
        if dickReceptionStage == 4:
            call afterJail_Day2_DickOffice_entrance_dialogue3() from _call_afterJail_Day2_DickOffice_entrance_dialogue3
            return
        if dickReceptionStage == 5:
            if dickReceptionWhoreTalked == False:
                call dickAfterJail_entrance_dialogue1() from _call_dickAfterJail_entrance_dialogue1
                return
            call change_scene("dick_office_hall1", "Fade_long", "snd_lift") from _call_change_scene_148
    if obj_name == "Teleport_Street":
        if dickReceptionStage == 1:
            $ dickReceptionStage = 0
        call change_scene("street_dick_office") from _call_change_scene_149
    return
label dick_office_entrance_environment_EP1:
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
                call after_jail_dick_reception_dialogue1() from _call_after_jail_dick_reception_dialogue1_1
                return
            if dickReceptionStage == 1:
                mt "Дика нет..."
                "Надо придти к нему завтра..."
            if dickReceptionStage == 2:
                call afterJail_Day2_DickOffice_entrance_dialogue1() from _call_afterJail_Day2_DickOffice_entrance_dialogue1_1
                return
            if dickReceptionStage == 3:
                if dickOfficeSecretaryMonicaStage > 0:
                    call afterJail_Day2_DickOffice_entrance_dialogue3_a() from _call_afterJail_Day2_DickOffice_entrance_dialogue3_a
                    return
                call afterJail_Day2_DickOffice_entrance_dialogue2() from _call_afterJail_Day2_DickOffice_entrance_dialogue2
                return
            if dickReceptionStage == 4:
                call afterJail_Day2_DickOffice_entrance_dialogue3() from _call_afterJail_Day2_DickOffice_entrance_dialogue3_1
                return
            if dickReceptionStage == 5:
                if dickReceptionWhoreTalked == False:
                    call dickAfterJail_entrance_dialogue1() from _call_dickAfterJail_entrance_dialogue1_1
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
