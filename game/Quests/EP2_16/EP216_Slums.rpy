default citizen15BlockedByDay = 0
default ep215_slums1_citizen15_last_day = 0
default ep215_slums1_citizen15_return = 0

default citizen13BlockedByDay = 0
default ep215_slums1_citizen13_last_day = 0

label ep215_slums1_dialogue_citizen15:
    call ep216_dialogues3_citizens_1() from _rcall_ep216_dialogues3_citizens_1
    if _return == -1: # отказалась идти к пилону
        return False
    if _return == -2: # отказалась вести на квартиру
        fadeblack 2.5
        $ questHelp("work_slums_50", False, skipIfTrue=True)
        call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_192
        return False

    $ questHelp("work_slums_50", True)
    $ set_active("Citizen_15", False, scene="all")
    $ citizen15BlockedByDay = day + 3
    $ ep215_slums1_citizen15_last_day = day

    $ ep215_slums1_citizen15_return = _return

    if _return == -3: # прогнала из квартиры
        fadeblack 2.5
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_193
        return False
    if _return == -4: # Моника отказалась брать член чтобы сказать что он большой и отказалась делать минет после этого
        fadeblack 2.5
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_194
        return False

    if _return == 1: # Моника сделала минет одному citizen15
        fadeblack 2.5
        $ autorun_to_object("ep216_dialogues3_citizens_2", scene="monicahome_livingroom")
        $ notif(t_("Моника обслужила 'Клиента'"))
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_195
        return False

    if _return == -5: # Моника просто подождала на кухне
        fadeblack 2.5
        $ notif(t_("Моника обслужила 'Клиента'"))
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_196
        return False
    if _return == -6: # Моника решила подождать на улице
        fadeblack 2.5
        $ add_hook("HomeEnter", "ep216_dialogues3_citizens_3", scene="street_monicahome", label=["day_time_temp", "ep216_dialogues3_citizens_3"])
        $ add_hook("MonicaWindow", "ep216_dialogues3_citizens_3", scene="street_monicahome", label=["day_time_temp", "ep216_dialogues3_citizens_3"])
        $ monicaHomeMiniMapEnabled = False
        $ add_hook("change_time_evening", "ep215_slums1_dialogue_citizen15_evening", scene="global", once=True, label="ep215_slums1_dialogue_citizen15_evening")
        $ notif(t_("Моника обслужила 'Клиента'"))
        call ep211_quests_slums_apartments3_check_exit_wardrobe() from _rcall_ep211_quests_slums_apartments3_check_exit_wardrobe
        call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_197
        return False
    if _return == -7: # Моника решила не подходить к парочке
        fadeblack 2.5
        $ add_hook("HomeEnter", "ep216_dialogues3_citizens_3", scene="street_monicahome", label=["day_time_temp", "ep216_dialogues3_citizens_3"])
        $ add_hook("MonicaWindow", "ep216_dialogues3_citizens_3", scene="street_monicahome", label=["day_time_temp", "ep216_dialogues3_citizens_3"])
        $ monicaHomeMiniMapEnabled = False
        $ add_hook("change_time_evening", "ep215_slums1_dialogue_citizen15_evening", scene="global", once=True, label="ep215_slums1_dialogue_citizen15_evening")
        $ notif(t_("Моника обслужила 'Клиента'"))
        call ep211_quests_slums_apartments3_check_exit_wardrobe() from _rcall_ep211_quests_slums_apartments3_check_exit_wardrobe_1
        call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_198
        return False

    if _return == -8: # Моника отказалась делать минет парочке, вышла на улицу
        fadeblack 2.5
        $ add_hook("HomeEnter", "ep216_dialogues3_citizens_3", scene="street_monicahome", label=["day_time_temp", "ep216_dialogues3_citizens_3"])
        $ add_hook("MonicaWindow", "ep216_dialogues3_citizens_3", scene="street_monicahome", label=["day_time_temp", "ep216_dialogues3_citizens_3"])
        $ monicaHomeMiniMapEnabled = False
        $ add_hook("change_time_evening", "ep215_slums1_dialogue_citizen15_evening", scene="global", once=True, label="ep215_slums1_dialogue_citizen15_evening")
        $ notif(t_("Моника обслужила 'Клиента'"))
        call ep211_quests_slums_apartments3_check_exit_wardrobe() from _rcall_ep211_quests_slums_apartments3_check_exit_wardrobe_2
        call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_199
        return False

    if _return == 2: # Моника полностью завершила сцену
        fadeblack 2.5
        $ autorun_to_object("ep216_dialogues3_citizens_2", scene="monicahome_livingroom")
        $ notif(t_("Моника обслужила 'Клиента'"))
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_200
        return False
    return False


label ep215_slums1_dialogue_citizen15_evening:
    $ monicaHomeMiniMapEnabled = True
    return


label ep215_slums1_dialogue_citizen13:
    call ep216_dialogues3_citizens_4() from _rcall_ep216_dialogues3_citizens_4
    if _return == False:
        return False
    $ questHelp("work_slums_51", True)
    if _return == -1:
        fadeblack 2.5
        call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_201
        return False
    if _return == 1:
        $ set_active("Citizen_13", False, scene="all")
        $ citizen13BlockedByDay = day + 3
        $ ep215_slums1_citizen13_last_day = day

        fadeblack 2.5
        $ notif(t_("Моника обслужила 'Клиента'"))
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_202

    return False


















#
