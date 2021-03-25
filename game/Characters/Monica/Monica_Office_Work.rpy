default cloth_before_work = False # одежда перед входом на работу
default cloth_type_before_work = False
default officeWorkingLog = []
default monicaOfficeWorkedToday = False

default office_work_comment1_1_lastDay = 0

default monicaWorkedDaysTotal = 0
default monicaWorkFlashCardReportLastDay = 0

init python:
    def add_office_working_day(status): #True - был рабочий день, #False - не было рабочего дня
        global cleaningLog, monicaWorkedDaysTotal
        if status == True:
            monicaWorkedDaysTotal += 1
        officeWorkingLog.insert(0, status)
        return

    def get_office_working_status(days): # Подсчитывает кол-во пропусков работы за последние days дней
        # На входе необходимое кол-во дней
#        if len(officeWorkingLog) < days:
#            return False
#        need_amount = days
        working_days_amount = 0
        if days > len(officeWorkingLog):
            days = len(officeWorkingLog)
        for idx1 in range(0,days):
            if officeWorkingLog[idx1] == True:
                working_days_amount = working_days_amount + 1
        return working_days_amount



label put_work_clothes:
    if cloth_type != "WorkingOutfit":
        $ cloth_before_work = cloth
        $ cloth_type_before_work = cloth_type
        $ cloth = "WorkingOutfit1"
        $ cloth_type = "WorkingOutfit"
    return
label putoff_work_clothes:
    $ cloth = cloth_before_work
    $ cloth_type = cloth_type_before_work
    return


label office_work_init:
    # Первичная инициализация

    # вход/выход из офиса
    $ add_hook("Teleport_Monica_Office_Entrance", "office_work_lift", scene="monica_office_secretary", label="office_lift")
    $ add_hook("Teleport_Monica_Office_Secretary", "office_work_lift", scene="monica_office_entrance", label="office_lift")
    $ add_hook("Teleport_Monica_Office_Lift", "office_work_lift", scene="working_office", label="office_lift")

    $ add_hook("change_time_day", "office_work_init_next_morning", scene="global")

    # Инициализация локаций
    call locations_init_working_office() from _call_locations_init_working_office

    return

label office_work_init_next_morning:
    $ remove_hook()
    $ questLog(43, True)
    return

label office_work_init2:
    # Вторичная инициализация
    # жизнь офиса
    $ add_hook("change_time_day", "office_life_day", scene="global")
    $ add_hook("change_time_evening", "office_life_evening", scene="global")
    $ add_hook("office_life_day", "office_life_day1", scene="global")
    $ add_hook("office_life_evening", "office_life_evening1", scene="global")

    $ add_hook("begin_office_work_dialogue", "office_work_begin1", scene="global", label="office_work_begin1_menu")
    $ add_hook("office_work_process", "office_work_process1", scene="global", label="office_work_process1")

    # Комментарий при входе на работу (если никого нет)
    $ add_hook("enter_scene", "office_work_comment1", scene="working_office", label="working_office_comment1")
    return

label office_life_day:
    call process_hooks("office_life_day", "global") from _call_process_hooks_60
    return True


label office_life_evening:
    call process_hooks("office_life_evening", "global") from _call_process_hooks_61
    return True

label office_life_day1:
    $ monicaOfficeWorkedToday = False
    if week_day != 7: # Если не воскресенье
        if ep210_julia_not_at_work == False and monicaRestJuliaHome != True:
            $ move_object("Julia", "working_office_cabinet") # Юлия идет на работу
        $ set_active(True, group="workers", scene="working_office") # Сотрудники на работе
        $ set_active(True, group="workers", scene="working_office2")
    else:
        if ep210_julia_not_at_work == False and monicaRestJuliaHome != True:
            $ move_object("Julia", "empty") # Юлия отдыхает


#    $ move_object("Biff", "empty")
    return

label office_life_evening1:
    if monicaOfficeWorkedToday == True:
        $ add_office_working_day(True)
        if ep27_quests_flash_quest1_inited == False:
            call ep27_quests_office1() from _call_ep27_quests_office1 # Инициализация квестов со флешкой (этап1)
    else:
        $ add_office_working_day(False)
    $ monicaOfficeWorkedToday = False

    if ep210_julia_evening_at_work == False:
        $ move_object("Julia", "empty") # Юлия отдыхает
    $ set_active(False, group="workers", scene="working_office") # Сотрудники уходят с работы
    $ set_active(False, group="workers", scene="working_office2")

    return


label office_work_lift:
    call ep26_dialogues6_office2_1_lift() from _call_ep26_dialogues6_office2_1_lift
    if _return == 1:
        if scene_name == "monica_office_secretary":
            return False
        # Этаж модного журнала
        if cloth_type != "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call put_work_clothes() from _call_put_work_clothes
        call process_hooks("office_work_lift", "misc") from _call_process_hooks_66
        if _return == False:
            call refresh_scene_fade() from _call_refresh_scene_fade_158
            return
        call change_scene("monica_office_secretary", "Fade_long", "snd_lift") from _call_change_scene_308
        return False
    if _return == 2:
        # Отдел Моники
        if scene_name == "working_office":
            return False
        if cloth_type != "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call put_work_clothes() from _call_put_work_clothes_1
        call process_hooks("office_work_lift", "misc") from _call_process_hooks_67
        if _return == False:
            call refresh_scene_fade() from _call_refresh_scene_fade_159
            return
        call change_scene("working_office", "Fade_long", "snd_lift") from _call_change_scene_309
        return False
    if _return == 3:
        # Вестибюль
        if scene_name == "monica_office_entrance":
            return False
        if cloth_type == "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call putoff_work_clothes() from _call_putoff_work_clothes
        call process_hooks("office_work_lift", "misc") from _call_process_hooks_68
        if _return == False:
            call refresh_scene_fade() from _call_refresh_scene_fade_160
            return
        call change_scene("monica_office_entrance", "Fade_long", "snd_lift") from _call_change_scene_310
        return False
    return

label office_work_minimap_teleport:
    #minimapCell["teleport_scene_name"]
    $ target_scene = minimapCell["teleport_scene_name"]
#    $ print target_scene
    if target_scene == scene_name:
        call refresh_scene_fade() from _call_refresh_scene_fade_145
        return
    call process_hooks("office_work_lift_minimap", "misc") from _call_process_hooks_69
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_161
        return

    if target_scene == "monica_office_entrance":
        if cloth_type == "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call putoff_work_clothes() from _call_putoff_work_clothes_1
    if scene_name == "monica_office_entrance":
        if cloth_type != "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call put_work_clothes() from _call_put_work_clothes_2
    if target_scene == "working_office_cabinet":
        $ workingOfficeCabinetMonicaSuffix = 1
    if (target_scene == "monica_office_photostudio" or target_scene == "monica_office_cabinet_table" or target_scene == "monica_office_secretary" or target_scene=="monica_office_secretary_teatable" or target_scene == "monica_office_makeup_room") and (scene_name == "monica_office_photostudio" or scene_name == "monica_office_cabinet_table" or scene_name == "monica_office_secretary" or scene_name=="monica_office_secretary_teatable" or scene_name == "monica_office_makeup_room"):
        call change_scene(target_scene, "Fade_long") from _call_change_scene_311
        return
    if (target_scene == "working_office" or target_scene == "working_office2" or target_scene == "working_office_cabinet" or target_scene =="working_office_cabinet2") and (scene_name == "working_office" or scene_name == "working_office2" or scene_name == "working_office_cabinet" or scene_name =="working_office_cabinet2"):
        call change_scene(target_scene, "Fade_long") from _call_change_scene_312
        return
    call change_scene(target_scene, "Fade_long", "snd_lift") from _call_change_scene_313
    return

label office_work_begin_event:
    call process_hooks("begin_office_work_dialogue", "global") from _call_process_hooks_62
    return

label office_work_begin1:
    if week_day == 7: # Выходной
        call ep26_dialogues6_office2_10() from _call_ep26_dialogues6_office2_10
        return False
    if day_time == "evening":
        call ep26_dialogues6_office2_4a() from _call_ep26_dialogues6_office2_4a
        return False
    # Типичный рабочий день
    call ep26_dialogues6_office2_6() from _call_ep26_dialogues6_office2_6
    if _return == False:
        return False
    call process_hooks("office_work_process", "global") from _call_process_hooks_63
    if _return == False:
        return
    call ep29_quests_melanie_check() from _rcall_ep29_quests_melanie_check # Проверка продолжения квеста с Мелани
    call ep212_quests_melanie_check() from _rcall_ep212_quests_melanie_check # Проверка продолжения квеста с Мелани
    img black_screen
    with diss
    pause 1.5
    $ monicaOfficeWorkedToday = True
    if ep210_julia_evening_at_work == False:
        $ move_object("Julia", "empty") # Юлия уходит с работы (обычный день)
    $ changeDayTime("evening")
    $ rand1 = random.choice([2,3,4,5])
    $ workingOfficeCabinetMonicaSuffix = rand1
    call ep26_dialogues6_office2_4() from _call_ep26_dialogues6_office2_4
    call refresh_scene_fade() from _call_refresh_scene_fade_146
    return

label office_work_begin2:
    # Рабочий день с приказами Юлии
    call process_hooks("office_work_process", "global") from _call_process_hooks_64
    call ep29_quests_melanie_check() from _rcall_ep29_quests_melanie_check_1 # Проверка продолжения квеста с Мелани
    call ep212_quests_melanie_check() from _rcall_ep212_quests_melanie_check_1 # Проверка продолжения квеста с Мелани
    img black_screen
    with diss
    pause 1.5
    $ monicaOfficeWorkedToday = True
    $ changeDayTime("evening")
    $ move_object("Julia", "working_office_cabinet")
    $ rand1 = random.choice([2,3,4,5])
    $ workingOfficeCabinetMonicaSuffix = rand1
    call refresh_scene_fade() from _call_refresh_scene_fade_147
    return

label office_work_process1:
    # Процессим работу
    # Заходит 1 человек в день
    if ep210_julia_not_at_work == False:
        call ep26_quests_office_workers2(1) from _call_ep26_quests_office_workers2
    return

label office_work_comment1:
    if get_active_objects(scene="working_office", group="workers") == False: # На работе никого нет
        if day_time == "day": # Если день (вечером их и так нет)
            if day != office_work_comment1_1_lastDay: # И если сегодня еще не делали комментария
                $ office_work_comment1_1_lastDay = day
                call ep26_dialogues6_office2_9() from _call_ep26_dialogues6_office2_9 # Комментарий по поводу выходного
    return
