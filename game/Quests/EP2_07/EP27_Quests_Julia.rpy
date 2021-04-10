default juliaQuestInited = False

default juliaQuestStarted = False
default juliaQuestRefused = False # Моника отказалась от квеста с Юлией (прогнала Фреда)
default juliaQuestStage = 0
default juliaQuestStage0_Progress = 0

default juliaQuestLastDay = 0

default juliaFredCatchFromDay = 0

default juliaQuestEvent1Count = 0
default juliaQuestEvent2Count = 0
default juliaQuestEvent3Count = 0
default juliaQuestEvent4Count = 0
default juliaQuestEvent5Count = 0

label ep27_quests_julia1_init: # Инит квеста с Юлией
    if juliaQuestInited == True:
        return
    $ add_hook("office_work_process", "ep27_quests_julia2", scene="global", label="ep27_quests_julia1_a")
    $ juliaQuestInited = True
    return

label ep27_quests_julia1_relationships:
    # Отношения с Юлией (меню)
    call ep27_dialogues6_julia0b() from _call_ep27_dialogues6_julia0b
    if _return == 1: #Юлия, ты сегодня хорошо выглядишь
        call ep27_quests_julia3() from _call_ep27_quests_julia3
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_163
        return False
    if _return == 2: #Юлия, ты красивая девушка и мне нравится твоя прическа...
        call ep27_quests_julia5() from _call_ep27_quests_julia5
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_164
        return False
    if _return == 3: #Сделать Юлии комплимент по поводу ее фигуры.
        call ep27_quests_julia7() from _call_ep27_quests_julia7
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_165
        return False
    if _return == 4: #Поцеловать Юлию.
        call ep27_quests_julia9() from _call_ep27_quests_julia9
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_166
        return False
    if _return == 5: #Ущипнуть Юлию за зад.
        call ep27_quests_julia11() from _call_ep27_quests_julia11
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_167
        return False
    if _return == 6: # Выяснить какого цвета трусики у Юлии
        call ep28_quests_julia_panties_menu() from _call_ep28_quests_julia_panties_menu
        return False
    return False

label ep27_quests_julia2: # Проверка на первый приход Фреда
#    if juliaOfficeOffended1 == False or juliaOfficeOffended2 == False: # Если Моника хорошо общается с Юлией, то Фред не приходит
    if juliaOfficeOffended1 == False and juliaOfficeOffended2 == False: # Если Моника хорошо общается с Юлией, то Фред не приходит
        return
    if juliaOfficeOffendedDay == day: # Ждем следующего дня
        return
    $ remove_hook()
    # Фред приходит!
    call ep27_dialogues6_julia3() from _call_ep27_dialogues6_julia3
    if _return == True:
        $ autorun_to_object("ep27_dialogues6_julia4", scene="working_office_cabinet")
        $ questHelp("office_27", True)
        $ questHelp("office_28", True)
        $ questHelp("julia_1", skipIfExists=True)
        $ questHelpDesc("julia_desc1")
        $ questLog(47, True)
        $ juliaQuestStage0_Progress = 1
        $ juliaQuestStarted = True
        call characters_init_julia() from _call_characters_init_julia
    else:
        $ questHelp("office_27", False)
        $ questHelp("julia_1", False)
        $ questHelp("office_28", False)
        $ questsFailByCategory(t_("ЮЛИЯ"))
        $ juliaQuestRefused = True
        $ remove_hook(label="ep29_quests_julia3_workers")
        $ steam_achievement("ach34")

    return False

label ep27_quests_julia3: # Юлия, ты сегодня хорошо выглядишь
    call ep27_dialogues6_julia5() from _call_ep27_dialogues6_julia5
    $ questHelp("julia_1", True)
    $ questHelp("julia_2", skipIfExists=True)
    $ juliaQuestLastDay = day
    if char_info["Julia"]["level"] == 1:
        $ add_char_progress("Julia", juliaLvl1IncreaseProgress, "juliaLvl1IncreaseProgress_day_" + str(day))
    if char_info["Julia"]["level"] == 2 or char_info["Julia"]["level"] == 3:
        $ add_char_progress("Julia", juliaLvl12IncreaseProgressLow, "juliaLvl12IncreaseProgressLow_day_" + str(day))
    $ juliaQuestEvent1Count += 1
    #fred
    if juliaQuestStage0_Progress == 1:
#        $ add_hook("Teleport_Monica_Office_Secretary", "ep27_quests_julia4_fred_catch", scene="monica_office_entrance", label="ep27_quests_julia1_b")
#        $ add_hook("office_work_lift_minimap", "ep27_quests_julia4_fred_catch_lift", scene="misc", label="ep27_quests_julia1_b")
        $ add_hook("before_open", "ep27_quests_julia4_fred_catch", scene="monica_office_entrance", recursive=True, label="ep27_quests_julia1_b", priority=1000)
        $ juliaFredCatchFromDay = day
    return

label ep27_quests_julia4_fred_catch: # Фред перехватывает Монику
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep27_quests_julia1_b")
    music stop
    sound snd_lift
    pause 1.0
    call ep27_dialogues6_julia6() from _call_ep27_dialogues6_julia6
    music stop
    img black_screen
    with diss
    pause 1.0
    $ questHelp("julia_2", True)
    $ questHelp("julia_3", skipIfExists=True)
    $ juliaQuestStage0_Progress = 2
    call change_scene("working_office") from _call_change_scene_370
    $ autorun_to_object("ep27_dialogues6_julia4a", scene=scene_name)
    return

label ep27_quests_julia5: #Юлия, ты красивая девушка и мне нравится твоя прическа...
    call ep27_dialogues6_julia7() from _call_ep27_dialogues6_julia7
    $ juliaQuestLastDay = day
    if char_info["Julia"]["level"] == 1:
        $ add_char_progress("Julia", juliaLvl1IncreaseProgress, "juliaLvl1IncreaseProgress_day_" + str(day))
    if char_info["Julia"]["level"] == 2 or char_info["Julia"]["level"] == 3:
        $ add_char_progress("Julia", juliaLvl12IncreaseProgressLow, "juliaLvl12IncreaseProgressLow_day_" + str(day))
    $ juliaQuestEvent2Count += 1
    if juliaQuestStage0_Progress == 2:
        $ questHelp("julia_3", True)
        $ questHelp("julia_4", skipIfExists=True)
        $ add_hook("before_open", "ep27_quests_julia6_fred_catch", scene="monica_office_entrance", recursive=True, label="ep27_quests_julia1_c", priority=1000)
        $ juliaFredCatchFromDay = day
    return

label ep27_quests_julia6_fred_catch:
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep27_quests_julia1_c")
    music stop
    sound snd_lift
    pause 1.0
    call ep27_dialogues6_julia8() from _call_ep27_dialogues6_julia8
    music stop
    img black_screen
    with diss
    pause 1.0
    $ questHelp("julia_4", True)
    $ questHelp("julia_5", skipIfExists=True)
    $ juliaQuestStage0_Progress = 3
    call change_scene("monica_office_photostudio") from _call_change_scene_371
    $ autorun_to_object("ep27_dialogues6_julia4a", scene=scene_name)
    return

label ep27_quests_julia7: #Сделать Юлии комплимент по поводу ее фигуры.
    call ep27_dialogues6_julia9() from _call_ep27_dialogues6_julia9
    $ juliaQuestLastDay = day
    if char_info["Julia"]["level"] == 1:
        $ add_char_progress("Julia", juliaLvl1IncreaseProgress, "juliaLvl1IncreaseProgress_day_" + str(day))
    if char_info["Julia"]["level"] == 2 or char_info["Julia"]["level"] == 3:
        $ add_char_progress("Julia", juliaLvl12IncreaseProgressLow, "juliaLvl12IncreaseProgressLow_day_" + str(day))
    $ juliaQuestEvent3Count += 1
    if juliaQuestStage0_Progress == 3:
        $ questHelp("julia_5", True)
        $ questHelp("julia_6", skipIfExists=True)
        $ add_hook("before_open", "ep27_quests_julia8_fred_catch", scene="monica_office_entrance", recursive=True, label="ep27_quests_julia1_d", priority=1000)
        $ juliaFredCatchFromDay = day
    return

label ep27_quests_julia8_fred_catch:
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep27_quests_julia1_d")
    music stop
    sound snd_lift
    pause 1.0
    call ep27_dialogues6_julia10() from _call_ep27_dialogues6_julia10
    music stop
    img black_screen
    with diss
    pause 1.0
    $ questHelp("julia_6", True)
    $ questHelp("julia_7", skipIfExists=True)
    $ juliaQuestStage0_Progress = 4
    call change_scene("working_office") from _call_change_scene_372
    $ autorun_to_object("ep27_dialogues6_julia10a", scene=scene_name)
    return

label ep27_quests_julia9: #Поцеловать Юлию.
    call ep27_dialogues6_julia11() from _call_ep27_dialogues6_julia11
    if _return == -1:
        return
    if _return == -2:
        $ juliaQuestLastDay = day
        return
    $ juliaQuestEvent4Count += 1
    $ juliaQuestLastDay = day
    if char_info["Julia"]["level"] == 2 or char_info["Julia"]["level"] == 3:
        $ add_char_progress("Julia", juliaLvl2IncreaseProgress, "juliaLvl2IncreaseProgress_day_" + str(day))
    if juliaQuestStage0_Progress == 4:
        $ questHelp("julia_7", True)
        $ questHelp("julia_8", skipIfExists=True)
        $ add_hook("before_open", "ep27_quests_julia10_fred_catch", scene="monica_office_entrance", recursive=True, label="ep27_quests_julia1_e", priority=1000)
        $ juliaFredCatchFromDay = day

    return
#

label ep27_quests_julia10_fred_catch:
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep27_quests_julia1_e")
    music stop
    sound snd_lift
    pause 1.0
    call ep27_dialogues6_julia12() from _call_ep27_dialogues6_julia12
    music stop
    img black_screen
    with diss
    pause 1.0
    $ questHelp("julia_8", True)
    $ questHelp("julia_9", skipIfExists=True)
    $ juliaQuestStage0_Progress = 5
    $ move_object("Melanie", "empty")
    call change_scene("monica_office_makeup_room") from _call_change_scene_373
    $ autorun_to_object("ep27_dialogues6_julia10a", scene=scene_name)
    return

label ep27_quests_julia11: #Ущипнуть Юлию за зад.
    call ep27_dialogues6_julia13() from _call_ep27_dialogues6_julia13
    if _return == -1:
        return
    if _return == -2:
        $ juliaQuestLastDay = day
        $ autorun_to_object("ep27_dialogues6_julia11a", scene=scene_name)
        return
    $ juliaQuestEvent4Count += 1
    $ juliaQuestLastDay = day
    if char_info["Julia"]["level"] == 3:
        $ add_char_progress("Julia", juliaLvl3IncreaseProgress, "juliaLvl3IncreaseProgress_day_" + str(day))
    if juliaQuestStage0_Progress == 5:
        $ questHelp("julia_9", True)
        $ questHelp("julia_10", skipIfExists=True)
        $ add_hook("before_open", "ep27_quests_julia12_fred_catch", scene="monica_office_entrance", recursive=True, label="ep27_quests_julia1_f", priority=1000)
        $ juliaFredCatchFromDay = day
    return

label ep27_quests_julia12_fred_catch:
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
        # next updates
    $ remove_hook(label="ep27_quests_julia1_f")
    call ep28_quests_julia_fred_catch1() from _call_ep28_quests_julia_fred_catch1
#    m "catch"
#    call ep28_betty_init()
#    return
    return
