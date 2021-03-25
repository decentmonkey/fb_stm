default ep212_quests_melanie_inited = False
default ep212_quests_melanie_refused1 = False
default ep212_quests_melanie_refused2 = False
default ep212_quests_melanie_made_private_photoshoot1 = False
default ep212_quests_melanie_completed = False
default ep212_quests_melanie_completed_day = 0

default ep212_quests_alex_cummed_area = -1

label ep212_quests_melanie_check: # Проверка на приход Мелани во время работы
    if ep212_quests_melanie_inited == True:
        return
    if ep211_quests_publicevent2_completed != True or ep29_quests_victoria_event_completed != True:
        return
    $ ep212_quests_melanie_inited = True
    call ep212_dialogues6_melanie_punishment_1() from _rcall_ep212_dialogues6_melanie_punishment_1
    if _return == False:
        $ ep212_quests_melanie_refused1 = True
        $ questHelp("melanie_15", False)
        $ questHelp("victoria_2", False)
        return
    $ questHelp("melanie_15", True)
    $ questHelp("melanie_16")
    $ add_objective("go_to_melanie", t_("Пойти домой к Мелани вечером"), c_green, 110)
    $ add_hook("Teleport_Melanie_Home", "ep212_quests_melanie1_check_teleport", scene="map", label=["ep212_quests_melanie", "ep212_quests_melanie_map1"])
#    $ add_hook("before_open", "ep212_quests_melanie2_enter_melanie_home", scene="melanie_home", label="ep212_quests_melanie")
    $ add_hook("slums_apartments_monica_before_sleep", "ep212_dialogues6_melanie_punishment_2", scene="global", label="ep212_quests_melanie")
    $ add_hook("basement_monica_before_sleep", "ep212_dialogues6_melanie_punishment_2", scene="global", label="ep212_quests_melanie")
    return

label ep212_quests_melanie1_check_teleport:
    if day_time != "evening":
        call ep212_dialogues6_melanie_punishment_1a() from _rcall_ep212_dialogues6_melanie_punishment_1a
        return False
    if cloth != "Whore":
        call ep212_dialogues6_melanie_punishment_3() from _rcall_ep212_dialogues6_melanie_punishment_3
        return False
    call ep212_quests_melanie2_enter_melanie_home() from _rcall_ep212_quests_melanie2_enter_melanie_home
    return False

label ep212_quests_melanie2_enter_melanie_home: # приход к Мелани
    $ hud_preset_current = map_source_scene_hud_preset
    $ remove_objective("go_to_melanie")
    $ remove_hook(label="melanie_disappeared_after_victoria") # Включаем Мелани
    $ add_hook("Melanie", "ep212_dialogues6_melanie_punishment_9a", scene="monica_office_makeup_room", label="ep212_quests_melanie_block")
    call ep212_dialogues6_melanie_punishment_4() from _rcall_ep212_dialogues6_melanie_punishment_4 # Приход к Мелани
    if _return == False:
        $ ep212_quests_melanie_refused1 = True
        $ questHelp("melanie_16", False)
        $ questHelp("victoria_2", False)
        $ remove_hook(label="ep212_quests_melanie")
        call ep212_quests_melanie3_go_monica_home() from _rcall_ep212_quests_melanie3_go_monica_home
        $ autorun_to_object("ep212_dialogues6_melanie_punishment_8", scene=_return)
        return False
    $ questHelp("melanie_16", True)
    $ questHelp("melanie_17")
    call ep212_melanie_home_photoshoot1a() from _rcall_ep212_melanie_home_photoshoot1a
    $ ep212_quests_melanie_made_private_photoshoot1 = True
    $ questHelp("melanie_18")
    call ep212_dialogues6_melanie_punishment_5() from _rcall_ep212_dialogues6_melanie_punishment_5
    call ep212_dialogues6_melanie_punishment_6() from _rcall_ep212_dialogues6_melanie_punishment_6
    if _return == False:
        $ ep212_quests_melanie_refused1 = True
        $ ep212_quests_melanie_refused2 = True
        $ questHelp("melanie_17", True)
        $ questHelp("melanie_18", False)
        $ questHelp("victoria_2", False)
        $ remove_hook(label="ep212_quests_melanie")
        call ep212_quests_melanie3_go_monica_home() from _rcall_ep212_quests_melanie3_go_monica_home_1
        $ autorun_to_object("ep212_dialogues6_melanie_punishment_8", scene=_return)
        return False
    call ep212_dialogues6_melanie_punishment_7() from _rcall_ep212_dialogues6_melanie_punishment_7
    $ questHelp("melanie_17", True)
    $ questHelp("melanie_18", True)
    $ questHelp("victoria_4")

    $ ep212_quests_melanie_completed = True
    $ ep212_quests_melanie_completed_day = day
    call ep213_quests_victoria1_init() from _rcall_ep213_quests_victoria1_init
    $ remove_hook(label="ep212_quests_melanie")
    call ep212_quests_melanie3_go_monica_home() from _rcall_ep212_quests_melanie3_go_monica_home_2
    $ autorun_to_object("ep212_dialogues6_melanie_punishment_9", scene=_return)
    return False

label ep212_quests_melanie3_go_monica_home: # Завершение квеста
    if slumsApartmentsRentActive == True:
        call process_change_map_location("Slums_Apartments") from _rcall_process_change_map_location
        call change_scene("street_monicahome", "Fade_long", False) from _rcall_change_scene_85
        return "street_monicahome"
    call process_change_map_location("House") from _rcall_process_change_map_location_1
    call change_scene("street_house_outside", "Fade_long", False) from _rcall_change_scene_86
    return "street_house_outside"
