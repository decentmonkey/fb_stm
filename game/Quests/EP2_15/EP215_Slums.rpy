default p215_slums1_alcoholic_last_day = 0

label ep215_slums1_dialogue_alcoholic:
    # Алкоголик подзывает Монику
    call ep215_dialogues6_citizens_1() from _rcall_ep215_dialogues6_citizens_1
    if _return == 0:
        $ questHelp("work_slums_49", False, skipIfTrue=True)
        call refresh_scene_fade() from _rcall_refresh_scene_fade_114
        return False
    $ move_object("Citizen_14", "empty")
    if _return == -1: # отказалась вести домой
        $ questHelp("work_slums_49", False, skipIfTrue=True)
        call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_176
        return False
    $ questHelp("work_slums_49", True)
    $ citizen14BlockedByDay = day + 3
    if _return == -2:# отказалась пить
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
        call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_177
        call refresh_scene_fade() from _rcall_refresh_scene_fade_115
        return False
    if _return == -3: # выпила одну и остановилась
        $ cloth = "HomeCloth4"
        $ cloth_type = "HomeCloth"
        fadeblack 1.0
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="monicahome_livingroom")
        call change_scene("monicahome_livingroom", "Fade", False) from _rcall_change_scene_178
        $ changeDayTime("evening")
        $ set_rest_place("slums_apartments")
        $ changeDayTime("day")
        return False

    # выпила все и проснулась с алкашом
    $ p215_slums1_alcoholic_last_day = day

    $ changeDayTime("evening")
    $ set_rest_place("none")
    $ changeDayTime("day")

    call ep215_dialogues6_citizens_1b() from _rcall_ep215_dialogues6_citizens_1b
    fadeblack 2.0
    $ move_object("Citizen_14", "empty")
    $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
    call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_179
    return False
