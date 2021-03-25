default ep215_quests_betty_stage = 0
default ep215_quests_betty_refused = False
default ep215_quests_betty_visit1_day = 0
default ep215_quests_betty_visit2_day = 0
default ep215_quests_betty_visit2_completed_day = 0

default ep215_stored_scenename = ""
default ep215_stored_vars = {}
default ep215_betty_floor2 = False
default showObjectsNotOwner_stored = False

label ep215_quests_betty_check:
    if monicaBettyRalphSeduction4 == True and ep215_quests_betty_stage == 0:
        # Моника замечает соседа
        call ep215_dialogues2_betty_1() from _rcall_ep215_dialogues2_betty_1
        $ ep215_quests_betty_stage = 1
        # на следующий день Бетти идет к соседу
        $ add_hook("change_time_day", "ep215_quests_betty1_init1", scene="global", label="ep215_quests_betty1_init1", priority=1)
        return

    return

label ep215_quests_betty1_init1:
    $ remove_hook()
    # Сосед приходит к Бетти
    call ep215_dialogues2_betty_2() from _rcall_ep215_dialogues2_betty_2
    call ep215_dialogues2_betty_3() from _rcall_ep215_dialogues2_betty_3
    if _return == False:
        $ ep215_quests_betty_refused = True
        $ questHelp("house_42", False)
        return
    call ep215_dialogues2_betty_4() from _rcall_ep215_dialogues2_betty_4

    $ questHelp("house_42", True)
    $ questHelp("house_43")

    $ remove_hook(label="change_owner_default_hook")
    $ add_hook("change_owner", "change_owner_default", scene="global", label="change_owner_default_hook")

    # инициализируем дом соседа с Бетти
    call locations_init_house_neighbour() from _rcall_locations_init_house_neighbour
    call street_house_outside_init3() from _rcall_street_house_outside_init3
    $ street_house_neighbour_betty_suffix = 1
    $ street_house_outside_betty_suffix = 1
    $ street_house_neighbour_neighbour_suffix = 1
    $ set_active("Betty", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Neighbour", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Outside", False, scene="street_house_outside")
    $ set_active("Betty", True, scene="street_house_neighbour")
    $ set_active("Neighbour", True, scene="street_house_neighbour")
    $ add_hook("Betty", "ep215_dialogues2_betty_8", scene="street_house_outside", label="betty_neighbour", owner="Betty")
    $ add_hook("Teleport_House_Outside_Neighbour", "ep215_quests_betty1_teleport_neighbour", scene="street_house_outside", label="betty_neighbour", owner="Betty")

    $ add_hook("Betty", "ep215_dialogues2_betty_8", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ add_hook("Neighbour", "ep215_dialogues2_betty_8", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ add_hook("Teleport_House_Neighbour_Farm", "ep215_dialogues2_betty_9", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ add_hook("Teleport_House_Outside", "street_house_neighbour_teleport", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ set_active("Door", False, scene="street_house_neighbour")
    $ add_hook("Neighbour", "ep215_quests_betty2_talk_neighbour", scene="street_house_neighbour", label="ep215_quests_betty2_talk_neighbour", owner="Betty")
    $ showObjectsNotOwner_stored = showObjectsNotOwner
    $ showObjectsNotOwner = False

    $ ep215_stored_vars["scene_name"] = scene_name
    $ ep215_stored_vars["miniMapEnabledOnly"] = miniMapEnabledOnly
    $ ep215_stored_vars["hudDaySkipToEveningEnabled"] = hudDaySkipToEveningEnabled
    $ ep215_betty_floor2 = get_active_objects("Betty", "floor2")
    call change_owner("Betty") from _rcall_change_owner
    $ remove_objective("bardie_college")
    $ map_objects = {
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active", "owner":"Betty"}
    }
    $ miniMapEnabledOnly = ["none"]
    $ hudDaySkipToEveningEnabled = False
    call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_164
    return

label ep215_quests_betty1_teleport_neighbour:
    call change_scene("street_house_neighbour", "Fade_long") from _rcall_change_scene_165
    return

label ep215_quests_betty2_talk_neighbour:
    if act=="l":
        return
    $ remove_hook()
    call ep215_dialogues2_betty_5() from _rcall_ep215_dialogues2_betty_5
    $ questHelp("house_43")
    if _return == False:
        $ ep215_quests_betty_refused = True
        $ questHelp("house_44", False)
        $ questHelp("house_43", False)
    else:
        # планируем второй приход
        $ add_hook("change_time_day", "ep215_quests_betty3_init", scene="global", label="ep215_quests_betty1_init1", priority=1)
        $ questHelp("house_43", True)
        $ questHelp("house_44")

    $ ep215_quests_betty_visit1_day = day
    call change_owner("Monica") from _rcall_change_owner_1
    $ showObjectsNotOwner = showObjectsNotOwner_stored
    $ set_active("Teleport_House_Outside_Neighbour", False, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Outside", True, scene="street_house_outside")
    $ miniMapEnabledOnly = ep215_stored_vars["miniMapEnabledOnly"]
    $ hudDaySkipToEveningEnabled = ep215_stored_vars["hudDaySkipToEveningEnabled"]
    $ move_object("Betty", "empty")
    if ep215_betty_floor2 == True:
        $ move_object("Betty", "floor2")

    fadeblack 2.0
    call change_scene(ep215_stored_vars["scene_name"], "Fade_long") from _rcall_change_scene_166

    return False

label ep215_quests_betty3_init:
    if week_day == 6:
        return
    $ remove_hook()
    # второй приход к соседу
    $ street_house_neighbour_betty_suffix = 2
    $ street_house_outside_betty_suffix = 2
    $ set_active("Betty", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Neighbour", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Outside", False, scene="street_house_outside")
    $ set_active("Betty", True, scene="street_house_neighbour")
    $ set_active("Neighbour", False, scene="street_house_neighbour")
    $ set_active("Door", True, scene="street_house_neighbour")
    $ add_hook("Door", "ep215_quests_betty3_enter_door", scene="street_house_neighbour", label="ep215_quests_betty3_enter_door", owner="Betty")

    $ ep215_stored_vars["scene_name"] = scene_name
    $ ep215_stored_vars["miniMapEnabledOnly"] = miniMapEnabledOnly
    $ ep215_stored_vars["hudDaySkipToEveningEnabled"] = hudDaySkipToEveningEnabled
    $ ep215_betty_floor2 = get_active_objects("Betty", "floor2")
    call change_owner("Betty") from _rcall_change_owner_2
    $ map_objects = {
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active", "owner":"Betty"}
    }
    $ miniMapEnabledOnly = ["none"]
    $ hudDaySkipToEveningEnabled = False
    $ showObjectsNotOwner_stored = showObjectsNotOwner
    $ showObjectsNotOwner = False

    call ep215_dialogues2_betty_10() from _rcall_ep215_dialogues2_betty_10
    $ autorun_to_object("ep215_dialogues2_betty_11", scene="street_house_outside")

    call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_167

    return

label ep215_quests_betty3_enter_door:
    if act=="l":
        call ep215_dialogues2_betty_8() from _rcall_ep215_dialogues2_betty_8
        return False
    $ remove_hook()
    # второй приход к соседу
    $ ep215_quests_betty_visit2_day = day
    call ep215_dialogues2_betty_6() from _rcall_ep215_dialogues2_betty_6
    if _return == False:
        $ ep215_quests_betty_refused = True
        $ questHelp("house_44", False)
    else:
        $ ep215_quests_betty_visit2_completed_day = day
        $ questHelp("house_44", True)
#        $ questHelp("house_45")

    # Бетти возвращается к Ральфу
    call ep215_dialogues2_betty_7() from _rcall_ep215_dialogues2_betty_7
    call change_owner("Monica") from _rcall_change_owner_3
    $ showObjectsNotOwner = showObjectsNotOwner_stored
    $ set_active("Teleport_House_Outside_Neighbour", False, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Outside", True, scene="street_house_outside")
    $ miniMapEnabledOnly = ep215_stored_vars["miniMapEnabledOnly"]
    $ hudDaySkipToEveningEnabled = ep215_stored_vars["hudDaySkipToEveningEnabled"]
    $ move_object("Betty", "empty")
    if ep215_betty_floor2 == True:
        $ move_object("Betty", "floor2")

    fadeblack 2.0
    $ autorun_to_object("ep215_dialogues2_betty_12", scene=ep215_stored_vars["scene_name"])
    call change_scene(ep215_stored_vars["scene_name"], "Fade_long") from _rcall_change_scene_168
    $ ep215_stored_vars = {}

    return False
