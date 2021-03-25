default ep27_flash_card_reports_done_arr = []
default ep27_flash_card_reports_done_count = 0
default ep27_flash_card_reports_skip_offered_day = 0

label ep27_quests_office_workers1: #Клик на воркеров, когда идет сбор отчетов
    if act=="l":
        return
    if monicaWorkFlashCardQuestActive == False or monicaWorkFlashCardReportLastDay == day:
        return
    if obj_name in ep27_flash_card_reports_done_arr: # уже собирали отчет у этого сотрудника
        return

    $ monicaWorkFlashCardNeedReportsAmount = 6

    if ep27_flash_card_reports_done_count >= 1 and ep27_flash_card_reports_skip_offered_day < day:
        $ ep27_flash_card_reports_skip_offered_day = day
        menu:
            "Пропустить (Собрать все отчеты сразу).":
                $ monicaWorkFlashCardReportsCollected = monicaWorkFlashCardNeedReportsAmount
                jump ep27_quests_office_workers1_end
            "Собирать отчеты.":
                pass

    if obj_name == "Worker1":
        call takeReportsFlashCard_Worker1() from _call_takeReportsFlashCard_Worker1
    if obj_name == "Worker2":
        call takeReportsFlashCard_Worker2() from _call_takeReportsFlashCard_Worker2
    if obj_name == "Worker3":
        call takeReportsFlashCard_Worker3() from _call_takeReportsFlashCard_Worker3
    if obj_name == "Worker4":
        call takeReportsFlashCard_Worker4() from _call_takeReportsFlashCard_Worker4
    if obj_name == "Worker5":
        call takeReportsFlashCard_Worker5() from _call_takeReportsFlashCard_Worker5
    if obj_name == "Worker6":
        call takeReportsFlashCard_Worker6() from _call_takeReportsFlashCard_Worker6
    if obj_name == "Worker7":
        call takeReportsFlashCard_Worker7() from _call_takeReportsFlashCard_Worker7


    $ ep27_flash_card_reports_done_arr.append(obj_name)
    if obj_name != "Worker2":
        $ monicaWorkFlashCardReportsCollected += 1

label ep27_quests_office_workers1_end:
    if monicaWorkFlashCardReportsCollected == monicaWorkFlashCardNeedReportsAmount: # Проверяем что собраны все отчеты
        $ monicaWorkFlashCardQuestReportsCollectedBySelf = True # Моника собрала отчеты сама
        $ monicaWorkFlashCardQuestNeedGiveReports = True
        $ monicaWorkFlashCardQuestReportsNeedTalkBiff = True
        $ monicaWorkFlashCardReportLastDay = day
        $ ep27_flash_card_reports_done_count += 1
        $ remove_objective("reports_to_biff")
        $ add_objective("reports_to_biff", t_("Отдать собранные отчеты для Бифа."), c_green, 20)
        $ autorun_to_object("ep27_dialogues6_julia2", scene=scene_name)
        $ move_object("Julia", "empty") # Юлия уходит с работы (обычный день)
        $ changeDayTime("evening") # Изменяем на вечер
        $ add_office_working_day(True) # Отмечаем рабочий день
    call refresh_scene_fade() from _call_refresh_scene_fade_173
    return False

label Worker1_use_flash_card:
label Worker2_use_flash_card:
label Worker3_use_flash_card:
label Worker4_use_flash_card:
label Worker5_use_flash_card:
label Worker6_use_flash_card:
label Worker7_use_flash_card:
    if obj_name in ep27_flash_card_reports_done_arr: # уже собирали отчет у этого сотрудника
        call ep27_dialogues4_biff9() from _call_ep27_dialogues4_biff9
        return
    call ep27_quests_office_workers1() from _call_ep27_quests_office_workers1
    return
