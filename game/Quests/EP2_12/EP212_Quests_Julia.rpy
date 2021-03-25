default ep212_julia_third_date_active = False
default ep212_julia_third_date_inited = False
default ep212_monica_known_julia_panties_color = False # Моника знает цвет трусиков Юлии
default ep212_monica_julia_quest2_started = False
default ep212_monica_said_fred_panties_color = False

label ep212_quests_julia1_third_date_init: # Инициализация третьего свидания
    $ ep212_julia_third_date_inited = True
    call ep212_dialogues5_julia_2() from _rcall_ep212_dialogues5_julia_2
    $ questHelp("julia_31", True)
    $ questHelp("julia_32", skipIfExists=True)
    $ add_objective("go_date_julia", t_("Пойти к Юлии домой после работы."), c_green, 115)
    $ add_hook("Julia", "ep212_dialogues5_julia_2_1", scene="working_office_cabinet", label="julia_third_date")
    $ ep210_julia_evening_at_work = False # вечером Юлии на работе нет
    $ add_hook("enter_scene", "ep212_dialogues5_julia_2_2", scene="street_monica_office", label="julia_third_date")
#    $ autorun_to_object("ep212_dialogues5_julia_2_2", scene="working_office_cabinet")
    $ add_hook("JuliaHome", "ep212_quests_julia3_third_date_start", scene="street_juliahome", label="julia_third_date")
    return False

label ep212_quests_julia2_fred_catch: # Фред перехватывает Монику
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance" or ep211_julia_second_date_completed_day == day:
        return
    $ remove_hook(label="ep212_quests_julia2_fred_catch")
    $ juliaFredCatchFromDay = day
    music stop
    sound snd_lift
    pause 1.0
    call ep212_dialogues5_julia_1() from _rcall_ep212_dialogues5_julia_1
    music stop
    img black_screen
    with diss
    pause 1.0
    $ questHelp("julia_29", True)
    if _return == False:
        $ juliaQuestMonicaRefusedFred = True
        $ questsFailByCategory(t_("ЮЛИЯ"))
        $ char_info["Julia"]["caption"] = t_("Юлия боится Монику")
        $ char_info["Julia"]["level"] = 1
        $ remove_objective("find_julia_panties_color")
        $ questLog(64, False)
        $ questLog(63, False)
        $ remove_hook(label="ep29_quests_julia3_workers")
        $ remove_hook(label="julia_dating_regular")
        $ questHelp("julia_30", False)
    else:
        $ ep212_julia_third_date_active = True
        $ questHelp("julia_30", skipIfExists=True)
    call change_scene("working_office") from _rcall_change_scene_83
    return

label ep212_quests_julia3_third_date_start: # Начало свидания
    if day_time != "evening":
        return
    if act=="l":
        call ep210_dialogues5_julia_3_2() from _rcall_ep210_dialogues5_julia_3_2_2
        return False
    if cloth != "CasualDress1":
        call ep210_dialogues5_julia_3_4a() from _rcall_ep210_dialogues5_julia_3_4a_1
        return False
    $ remove_objective("go_date_julia")
    $ remove_hook(label="julia_third_date")
    call ep212_dialogues5_julia_3() from _rcall_ep212_dialogues5_julia_3 # Встречаются, Юлия уходит в ванную
    if _return == False:
        $ questsFailByCategory(t_("ЮЛИЯ"))
        $ juliaQuestMonicaRefusedFred = True
        $ char_info["Julia"]["caption"] = t_("Юлия боится Монику")
        $ char_info["Julia"]["level"] = 1
        $ remove_hook(label="julia_dating_regular")
        $ remove_objective("find_julia_panties_color")
        $ questLog(64, False)
        $ questLog(63, False)
        $ remove_hook(label="ep29_quests_julia3_workers")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_11
        return False

    call ep212_dialogues5_julia_4() from _rcall_ep212_dialogues5_julia_4 # Юлия возвращается из ванной
    $ ep212_monica_known_julia_panties_color = True
    $ questHelp("julia_32", True)
    if _return == False:
        $ juliaQuestMonicaRefusedFred = True
        $ questsFailByCategory(t_("ЮЛИЯ"))
        $ char_info["Julia"]["caption"] = t_("Юлия боится Монику")
        $ char_info["Julia"]["level"] = 1
        $ remove_hook(label="julia_dating_regular")
        $ remove_objective("find_julia_panties_color")
        $ questLog(63, False)
        $ questLog(64, False)
        $ remove_hook(label="ep29_quests_julia3_workers")
        $ questHelp("julia_34", False)
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_12
        return False
    else:
        $ ep212_monica_julia_quest2_started = True
        $ questHelp("julia_34", skipIfExists=True)
        $ questHelp("julia_desc3", "julia_desc4")

    $ remove_objective("find_julia_panties_color")
    call ep212_dialogues5_julia_5() from _rcall_ep212_dialogues5_julia_5 # Просыпаются с утра
    $ ep210_julia_evening_at_work = True
    $ questLog(73, True)
    $ questLog(63, False)
    $ autorun_to_object("ep212_dialogues5_julia_5_1", scene="street_juliahome")
    $ add_hook("Julia", "ep212_dialogues5_julia_5_3", scene="working_office_cabinet", label="julia_quest2") # Смотрим на Юлию в кабинете
    $ add_char_progress("Julia", 100, "monica_julia_progress_third_date")

    $ add_hook("before_open", "ep212_quests_julia4_fred_catch", scene="working_office", label="ep212_quests_julia4_fred_catch", priority=1000)
    $ add_hook("before_open", "ep212_quests_julia4_fred_catch", scene="working_office_cabinet", label="ep212_quests_julia4_fred_catch", priority=1000)
    $ remove_hook(label="ep29_quests_julia3_workers")

    $ monicaRestJuliaHome = True
    $ monicaRestJuliaHomeDay = day
    $ monicaRestHouse = False
    $ monicaRestApartments = False

    $ changeDayTime("day")

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_13
    return False

label ep212_quests_julia4_fred_catch: # Фред перехватывает Монику
    if ep212_monica_said_fred_panties_color == True or ep212_monica_known_julia_panties_color == False:
        return
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    call ep212_dialogues5_julia_6() from _rcall_ep212_dialogues5_julia_6 # Моника говорит Фреду цвет трусиков
    $ ep212_monica_said_fred_panties_color = True
    $ questLog(47, False)
    $ questHelp("julia_34", True)
    $ questHelp("julia_35", skipIfExists=True)
#    $ remove_hook(label="ep212_quests_julia4_fred_catch")
    call change_scene("working_office") from _rcall_change_scene_84
    return
