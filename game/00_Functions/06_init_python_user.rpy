init python:
    def changeDayTime(dayTime):
        global day_time, day_suffix, day, week_day, scene_name
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            renpy.call("changeDayTime_evening_hooks")
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            week_day = (day)%7
            if week_day == 0:
                week_day = 7
            if week_day == 6:
                renpy.free_memory()

            renpy.call("changeDayTime_day_hooks")
            return
        return

    def changeDayTimeSlumsApartments(dayTime):
        global day_time, day_suffix, day, week_day, scene_name
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            renpy.call("changeDayTime_evening_hooks_slums_apartments")
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            week_day = (day)%7
            if week_day == 0:
                week_day = 7
            if week_day == 6:
                renpy.free_memory()

            renpy.call("changeDayTime_day_hooks_slums_apartments")
            return
        return

    def changeDayTimeHostel(dayTime):
        global day_time, day_suffix, day, week_day, scene_name
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            renpy.call("changeDayTime_evening_hooks_hostel")
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            week_day = (day)%7
            if week_day == 0:
                week_day = 7
            if week_day == 6:
                renpy.free_memory()

            renpy.call("changeDayTime_day_hooks_hostel")
            return
        return

    def changeDayTimeJuliaHome(dayTime):
        global day_time, day_suffix, day, week_day, scene_name
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            renpy.call("changeDayTime_evening_hooks_juliahome")
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            week_day = (day)%7
            if week_day == 0:
                week_day = 7
            if week_day == 6:
                renpy.free_memory()
            renpy.call("changeDayTime_day_hooks_juliahome")
            return
        return

    def getNextDayByWeekDay(target_week_day): #найти дату для следующего дня недели
        if target_week_day == week_day:
            return day + 7
        if target_week_day < week_day:
            return day + 7 - week_day + target_week_day
        if target_week_day > week_day:
            return day + target_week_day - week_day
        return

    def get_scene_label(scene_label):
        global sceneStages
        for idx in reversed(range(0, len(sceneStages))):
            if renpy.has_label(scene_label + sceneStages[idx]):
                return scene_label + sceneStages[idx]
        return scene_label

    def checkTimeDay():
        return day_time == "day"

label changeDayTime_day_hooks:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="evening_time_temp")
    call process_hooks("change_time_day", "global") from _call_process_hooks_19
    call process_hooks("change_time_day_global", "global") from _rcall_process_hooks_2
    call process_hooks("week_day_" + str(week_day), "global_week_day") from _call_process_hooks_20
    call process_hooks("day_" + str(day), "global_day") from _call_process_hooks_21
    return
label changeDayTime_evening_hooks:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="day_time_temp")
    call process_hooks("change_time_evening", "global") from _call_process_hooks_22
    call process_hooks("change_time_evening_global", "global") from _rcall_process_hooks_3
    call process_hooks("day_" + str(week_day) + "_evening", "global_week_day") from _call_process_hooks_23
    call process_hooks("day_" + str(day) + "_evening", "global_day") from _call_process_hooks_24
    return


label changeDayTime_day_hooks_slums_apartments:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="evening_time_temp")
    call process_hooks("change_time_day", "global") from _rcall_process_hooks_20
#    call process_hooks("change_time_day_slums_apartments", "global") from _call_process_hooks_19b
    call process_hooks("change_time_day_global", "global") from _rcall_process_hooks_4
    call process_hooks("week_day_" + str(week_day), "global_week_day") from _call_process_hooks_20b
    call process_hooks("day_" + str(day), "global_day") from _call_process_hooks_21b
    return
label changeDayTime_evening_hooks_slums_apartments:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="day_time_temp")
    call process_hooks("change_time_evening", "global") from _rcall_process_hooks_21
    call process_hooks("change_time_evening_slums_apartments", "global") from _call_process_hooks_22b
    call process_hooks("change_time_evening_global", "global") from _rcall_process_hooks_5
    call process_hooks("day_" + str(week_day) + "_evening", "global_week_day") from _call_process_hooks_23b
    call process_hooks("day_" + str(day) + "_evening", "global_day") from _call_process_hooks_24b
    return

label changeDayTime_day_hooks_hostel:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="evening_time_temp")
    call process_hooks("change_time_day", "global") from _rcall_process_hooks_42
    call process_hooks("change_time_day_global", "global") from _rcall_process_hooks_43
    call process_hooks("week_day_" + str(week_day), "global_week_day") from _rcall_process_hooks_44
    call process_hooks("day_" + str(day), "global_day") from _rcall_process_hooks_45
    return

label changeDayTime_evening_hooks_hostel:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="day_time_temp")
    call process_hooks("change_time_evening", "global") from _rcall_process_hooks_46
    call process_hooks("change_time_evening_hostel_apartments", "global") from _rcall_process_hooks_47
    call process_hooks("change_time_evening_global", "global") from _rcall_process_hooks_48
    call process_hooks("day_" + str(week_day) + "_evening", "global_week_day") from _rcall_process_hooks_49
    call process_hooks("day_" + str(day) + "_evening", "global_day") from _rcall_process_hooks_50
    return

label changeDayTime_day_hooks_juliahome:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="evening_time_temp")
    call process_hooks("change_time_day", "global") from _rcall_process_hooks_22
#    call process_hooks("change_time_day_slums_apartments", "global") from _call_process_hooks_19b
    call process_hooks("change_time_day_global", "global") from _rcall_process_hooks_23
    call process_hooks("week_day_" + str(week_day), "global_week_day") from _rcall_process_hooks_24
    call process_hooks("day_" + str(day), "global_day") from _rcall_process_hooks_25
    return
label changeDayTime_evening_hooks_juliahome:
    if monica_cheats_hungry_enabled == False:
        $ monica_eated()
    $ remove_hook(label="day_time_temp")
    call process_hooks("change_time_evening", "global") from _rcall_process_hooks_26
    call process_hooks("change_time_evening_global", "global") from _rcall_process_hooks_27
    call process_hooks("day_" + str(week_day) + "_evening", "global_week_day") from _rcall_process_hooks_28
    call process_hooks("day_" + str(day) + "_evening", "global_day") from _rcall_process_hooks_29
    return
