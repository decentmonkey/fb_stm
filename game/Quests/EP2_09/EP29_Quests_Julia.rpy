default juliaQuestStage1_workers_progress = 0
default juliaQuestStage1_workers_progress_day = 0

label ep29_quests_julia1:
    #Заставить Юлию включить неработающий компьютер, progress 5
    call ep29_dialogues1_julia_2() from _call_ep29_dialogues1_julia_2
    $ juliaQuestLastDay = day
    if _return == True:
        if juliaQuestStage1_Progress <= 5:
            $ questHelp("julia_18", True)
            $ questHelp("julia_19", skipIfExists=True)
            $ add_hook("before_open", "ep29_quests_julia_fred_catch1", scene="monica_office_entrance", label="ep29_quests_julia_fred_catch1", priority=1001)

    $ workingOfficeCabinetMonicaSuffix = 2
    call refresh_scene_fade() from _call_refresh_scene_fade_196
    return

label ep29_quests_julia_fred_catch1:
    # Фред ловит Монику вечером на выходе из офиса (в гримерке)
    $ remove_hook()
    call ep29_dialogues1_julia_3() from _call_ep29_dialogues1_julia_3
    $ questHelp("julia_19", True)
    if _return == False:
        $ juliaQuestMonicaRefusedFred = True
        $ remove_objective("find_julia_panties_color")
        $ remove_hook(label="ep29_quests_julia3_workers")
        $ questHelp("julia_20", False)
        $ questsFailByCategory(t_("ЮЛИЯ"))
    else:
        $ juliaQuestStage1_Progress = 6
        $ questHelp("julia_20", skipIfExists=True)

    return

label ep29_quests_julia2:
    #Заставить Юлию принести горячий кофе, progress 6
    call ep29_dialogues1_julia_4() from _call_ep29_dialogues1_julia_4
    $ juliaQuestLastDay = day
    if juliaQuestStage1_Progress <= 6:
        $ juliaQuestStage1_Progress = 7
        $ questHelp("julia_20", True)
        $ questHelp("julia_21", skipIfExists=True)

    $ workingOfficeCabinetMonicaSuffix = 2
    $ workingOfficeCabinet2MonicaSuffix = 2
    call change_scene("working_office_cabinet2", "Fade_long", False) from _call_change_scene_431
#    call refresh_scene_fade()
    return

label ep29_quests_julia3:
    #Есть же подчиненные. Поручить им выполнить просьбу Фреда, progress 7
    if juliaQuestStage1_workers_progress == 0:
        call ep29_dialogues1_julia_5() from _call_ep29_dialogues1_julia_5
        $ juliaQuestStage1_workers_progress = 1
        $ add_hook("Worker5", "ep29_quests_julia3_worker5", scene="working_office", label="ep29_quests_julia3_workers")
        $ add_hook("Worker6", "ep29_quests_julia3_worker6", scene="working_office", label="ep29_quests_julia3_workers")
        $ add_hook("Worker6", "ep29_quests_julia3_worker6", scene="working_office2", label="ep29_quests_julia3_workers")
        $ add_hook("before_open", "ep29_quests_julia3b", scene="working_office", label="ep29_quests_julia3b")
        $ add_hook("before_open", "ep29_quests_julia3b", scene="working_office_cabinet", label="ep29_quests_julia3b")
        $ questHelp("julia_21", True)
        $ questHelp("julia_22", skipIfExists=True)
        $ juliaQuestStage1_workers_progress_day = day
        call refresh_scene_fade() from _call_refresh_scene_fade_197
        return
    if juliaQuestStage1_workers_progress >= 1 and juliaQuestStage1_workers_progress < 3:
        call ep29_dialogues1_julia_8a() from _call_ep29_dialogues1_julia_8a
        return
    if juliaQuestStage1_workers_progress >= 3:
        call ep29_dialogues1_julia_8b() from _call_ep29_dialogues1_julia_8b
        return
    return

label ep29_quests_julia3_worker5:
    if act=="l":
        return
    menu:
        "Узнать как продвигается выполнение задания.":
            call ep29_dialogues1_julia_6() from _call_ep29_dialogues1_julia_6
            call refresh_scene_fade() from _call_refresh_scene_fade_198
        "Собрать отчет." if monicaWorkFlashCardQuestActive == True and monicaWorkFlashCardReportLastDay != day and "Worker5" not in ep27_flash_card_reports_done_arr:
            return
        "Разговор." if monicaWorkFlashCardQuestActive == False or monicaWorkFlashCardReportLastDay == day or "Worker5" in ep27_flash_card_reports_done_arr:
            return
        "Уйти.":
            return False
    return False

label ep29_quests_julia3_worker6:
    if act=="l":
        return
    menu:
        "Узнать как продвигается выполнение задания.":
            call ep29_dialogues1_julia_7() from _call_ep29_dialogues1_julia_7
            call refresh_scene_fade() from _call_refresh_scene_fade_199
        "Собрать отчет." if monicaWorkFlashCardQuestActive == True and monicaWorkFlashCardReportLastDay != day and "Worker6" not in ep27_flash_card_reports_done_arr:
            return
        "Разговор." if monicaWorkFlashCardQuestActive == False or monicaWorkFlashCardReportLastDay == day or "Worker6" in ep27_flash_card_reports_done_arr:
            return
        "Уйти.":
            return False
    return False

label ep29_quests_julia3b:
    # Моника приходит на работу. Грета делает попытку с Юлией
    if juliaQuestStage1_workers_progress_day == day or week_day == 7 or day_time != "day":
        return
    $ remove_hook(label="ep29_quests_julia3b")
    call ep29_dialogues1_julia_8() from _call_ep29_dialogues1_julia_8 #Грета делает попытку с Юлией
    $ juliaQuestStage1_workers_progress = 1
    $ add_hook("before_open", "ep29_quests_julia3c", scene="working_office", label="ep29_quests_julia3c")
    $ add_hook("before_open", "ep29_quests_julia3c", scene="working_office_cabinet", label="ep29_quests_julia3c")
    $ juliaQuestStage1_workers_progress_day = day
    return

label ep29_quests_julia3c:
    # Моника приходит на работу. Джон делает попытку с Юлией
    if juliaQuestStage1_workers_progress_day == day or week_day == 7 or day_time != "day":
        return
    $ remove_hook(label="ep29_quests_julia3c")
    call ep29_dialogues1_julia_9() from _call_ep29_dialogues1_julia_9
    $ juliaQuestStage1_workers_progress = 2
    $ add_hook("before_open", "ep29_quests_julia3d", scene="working_office", label="ep29_quests_julia3d")
    $ add_hook("before_open", "ep29_quests_julia3d", scene="working_office_cabinet", label="ep29_quests_julia3d")
    $ juliaQuestStage1_workers_progress_day = day
    return

label ep29_quests_julia3d:
    # Джон и Грета стоят возле рабочего стола Джона в их офисе.
    if juliaQuestStage1_workers_progress_day == day or week_day == 7 or day_time != "day":
        return
    $ remove_hook(label="ep29_quests_julia3d")
    call ep29_dialogues1_julia_10() from _call_ep29_dialogues1_julia_10
    $ questHelp("julia_22", True)
    $ questHelp("julia_22a")
    $ juliaQuestStage1_workers_progress = 3
    $ juliaQuestStage1_workers_progress_day = day
    call ep210_quests_julia_init() from _rcall_ep210_quests_julia_init
#    $ add_hook("before_open", "ep29_quests_julia3e", scene="working_office", label="ep29_quests_julia3e")
#    $ add_hook("before_open", "ep29_quests_julia3e", scene="working_office_cabinet", label="ep29_quests_julia3e")
    return

label ep29_quests_julia3e:
    # Продолжение квеста
    call ep210_quests_julia_init() from _rcall_ep210_quests_julia_init_1
    $ remove_hook(label="ep29_quests_julia3e")
    return





#
