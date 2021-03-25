# квест с показом груди секретаршей Моники
default ep27_quests_secretary1_show_boobs_monica_refused1 = False # Моника отказалась от этой затеи в самом начале
default ep27_quests_secretary1_show_boobs_active = True
default hostelStreet3SecretarySuffix = ""
default ep27_quests_secretart1_monica_let_secretary_out = False # Моника отпустила секретаршу
default ep27_quests_secretart1_monica_secretary_showed_boobs = False
default ep27_quests_secretart1_monica_secretary_touched_boobs = False


label ep27_quests_secretary1:
    call ep27_dialogues5_secretary_boobs1() from _call_ep27_dialogues5_secretary_boobs1
    if _return == -1 or _return == 0:
        call refresh_scene_fade() from _call_refresh_scene_fade_157
        return True
    $ add_object_to_scene("Secretary", {"type" : 2, "base" : "Hostel_Street3_Secretary[hostelStreet3SecretarySuffix][day_suffix]", "click" : "ep27_dialogues5_secretary_boobs2", "actions" : "l", "zorder":10}, scene="hostel_street3")
    $ add_hook("Monica", "ep27_dialogues5_secretary_boobs2", scene="hostel_street3", label="secretary_boobs_quest1")
    $ add_hook("Citizen_3", "ep27_dialogues5_secretary_boobs3", scene="hostel_street3", label="secretary_boobs_quest1")
    $ add_hook("Citizen_4", "ep27_quests_secretary2", scene="hostel_street3", label="secretary_boobs_quest1")
    $ add_hook("Citizen_7", "ep27_dialogues5_secretary_boobs3", scene="hostel_street3", label="secretary_boobs_quest1")
    $ add_hook("Teleport_Hostel_Street_Corner", "ep27_dialogues5_secretary_boobs4", scene="hostel_street3", label="secretary_boobs_quest1")
    $ add_hook("Teleport_Hostel_Street2", "ep27_dialogues5_secretary_boobs4", scene="hostel_street3", label="secretary_boobs_quest1")
    $ move_object("Secretary", "hostel_street3")

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    $ move_object("Citizen_4", "hostel_street3")

    $ miniMapEnabledOnly = ["none"]
    $ hudDaySkipToEveningEnabled = False
    $ map_enabled = False
    call process_change_map_location("Hostel2") from _call_process_change_map_location_2

    call change_scene("hostel_street3", "Fade_long", "highheels_run1") from _call_change_scene_362
    music street3
    return False

label ep27_quests_secretary2:
    # клик на ситизена, которому показывать грудь

    call ep27_dialogues5_secretary_boobs6() from _call_ep27_dialogues5_secretary_boobs6
    $ ep27_quests_secretary1_show_boobs_active = False
    $ miniMapEnabledOnly = []
    $ hudDaySkipToEveningEnabled = True
    $ map_enabled = True

    if _return == True:
        $ autorun_to_object("ep27_dialogues5_secretary_boobs7", scene="hostel_edge_1_a")

    $ move_object("Secretary", "monica_office_secretary")
    $ remove_hook(label="secretary_boobs_quest1")
    call change_scene("hostel_edge_1_a", "Fade_long", "highheels_run1") from _call_change_scene_363
    return False
