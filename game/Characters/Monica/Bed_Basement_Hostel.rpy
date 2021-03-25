default monicaRestHostel = False
default monicaRestHostelDay = 0

label hostel_basement_bed:
    if act=="l":
        return
    if act == "h":
        $ set_rest_place("hostel")
        if day_time == "day":
            call hostel_basement_bed_take_nap() from _rcall_hostel_basement_bed_take_nap
            return _return
        if day_time == "evening":
            call hostel_basement_bed_gosleep() from _rcall_hostel_basement_bed_gosleep
            return _return

    return False

label hostel_basement_bed_take_nap:
    $ ep214_stored_cloth = cloth
    $ cloth = "Sleep"
    $ hostelBedroomMonicaSuffix = 1
    $ set_active("HostelBed", False)
    $ autorun_to_object("hostel_basement_bed_take_nap1")
    call refresh_scene("Dissolve_05") from _rcall_refresh_scene_5
    return

label hostel_basement_bed_take_nap1:
    menu:
        "Лечь и ждать вечера.":
            music stop
            $ afterNapSuffix = 2
            img black_screen
            with Dissolve(0.2)
            #транзиция на отдых
            $ cloth = ep214_stored_cloth
            call process_hooks("hostel_monica_before_nap", "global") from _rcall_process_hooks_52
            $ set_active("HostelBed", True)
            if _return == False:
                $ hostelBedroomMonicaSuffix = 2
                call refresh_scene_fade() from _rcall_refresh_scene_fade_96
                return False
            $ hostelBedroomMonicaSuffix = afterNapSuffix
            $ changeDayTimeHostel("evening")
            call process_hooks("hostel_monica_after_nap", "global") from _rcall_process_hooks_53
            call refresh_scene_fade() from _rcall_refresh_scene_fade_97
            return False
        "Не ложиться.":
            $ hostelBedroomMonicaSuffix = 2
            $ cloth = ep214_stored_cloth
            $ set_active("HostelBed", True)
            call refresh_scene_fade() from _rcall_refresh_scene_fade_98
            return False
    return


label hostel_basement_bed_gosleep:
    $ ep214_stored_cloth = cloth
    $ cloth = "Sleep"
    $ hostelBedroomMonicaSuffix = 1
    $ set_active("HostelBed", False)
    $ autorun_to_object("hostel_basement_bed_gosleep1")
    call refresh_scene("Dissolve_05") from _rcall_refresh_scene_6
    return

label hostel_basement_bed_gosleep1:
    if monicaEatedLastDay < day:
        if day - monicaEatedLastDay >= 3 and (monicaCantSleepHungry2 == True or debugMode == False) and debugMode == False:
            #если Моника не ела 3 дня
            mt "{c}Я не ела{/c} уже третий день!"
            "Я не могу лечь спать в таком состоянии!"
            "Я ХОЧУ ЕСТЬ!!!"
            $ set_active("HostelBed", True)
            $ hostelBedroomMonicaSuffix = 2
            $ cloth = ep214_stored_cloth
            call refresh_scene_fade() from _rcall_refresh_scene_fade_99
            return False

        else:
            mt "Я сегодня ничего не ела! Лечь спать голодной?"

    menu:
        "Лечь спать." if monicaEatedLastDay == day:
            call hostel_basement_bed_gosleep2() from _rcall_hostel_basement_bed_gosleep2
            return
        "Лечь спать голодной." if monicaEatedLastDay < day:
            call hostel_basement_bed_gosleep2() from _rcall_hostel_basement_bed_gosleep2_1
            return
        "Не ложиться.":
            $ set_active("HostelBed", True)
            $ hostelBedroomMonicaSuffix = 2
            $ cloth = ep214_stored_cloth
            call refresh_scene_fade() from _rcall_refresh_scene_fade_100
            return False

    return

label hostel_basement_bed_gosleep2:
    music stop
    $ afterSleepSuffix = 2
    img black_screen
    with Dissolve(0.2)
    #транзиция на отдых
    call process_hooks("hostel_monica_before_sleep", "global") from _rcall_process_hooks_54
    $ set_active("HostelBed", True)
    if _return == False:
        $ hostelBedroomMonicaSuffix = 2
        $ cloth = ep214_stored_cloth
        call refresh_scene_fade() from _rcall_refresh_scene_fade_101
        return False
    $ hostelBedroomMonicaSuffix = 2
    $ cloth = ep214_stored_cloth
    $ hostelBedroomMonicaSuffix = afterSleepSuffix
    $ changeDayTimeHostel("day")
    call process_hooks("hostel_monica_after_sleep", "global") from _rcall_process_hooks_55
    call refresh_scene_fade() from _rcall_refresh_scene_fade_102
    return
