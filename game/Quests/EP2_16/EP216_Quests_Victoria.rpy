default ep216_victoria_visit_day1 = 0
default ep216_quests_victoria1_init_flag = False

default ep216_victoria_visit_day2 = 0 # приходит админ и свидание админа с викторией
default ep216_victoria_visit_day3 = 0 # приходит админ и свидание админа с моникой
default ep216_victoria_visit_day4 = 0 # админ смотрит на Монику после свидания с ней

label ep216_quests_victoria1_init: # Юлия сообщает что надо ехать к Виктории на девичник
    $ add_hook("office_work_process", "ep216_quests_victoria2_init", scene="global", label="ep216_quests_victoria2_init", priority = 90)
    $ ep216_quests_victoria1_init_flag = True
    return

label ep216_quests_victoria2_init: # инициализация во время работы
    $ remove_hook()
    $ monicaOfficeWorkedToday = True
    call ep216_dialogues5_victoria_1() from _rcall_ep216_dialogues5_victoria_1
    $ questHelp("office_47", True)
    $ questHelp("victoria_12")
    $ add_objective("go_victoria", t_("Идти к Виктории."), c_red, 125)
    call locations_init_victoriahome1() from _rcall_locations_init_victoriahome1 # инициализируем локацию Виктории
    $ map_objects ["Teleport_VictoriaHome"] = {"text" : t_("АПАРТАМЕНТЫ ВИКТОРИИ"), "xpos" : 1403, "ypos" : 260, "base" : "map_marker", "state" : "visible"}

    # блокируем перемещения
    $ focus_map("Teleport_VictoriaHome", "ep216_dialogues5_victoria_12b")
    $ move_object("Melanie", "empty")
    $ hudDaySkipToEveningEnabled = False # выключаем телепорт в кровать
    # выключаем сон
    $ add_hook("slums_apartments_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
    $ add_hook("hostel_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
    $ add_hook("juliahome_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
    $ add_hook("basement_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")

    # блокируем перемещения и работу
    $ add_hook("Building", "ep216_dialogues5_victoria_12", scene="street_police", label="ep216_victoria_block") # блокируем полицию
    $ add_hook("JuliaHome", "ep216_dialogues5_victoria_12", scene="street_juliahome", label="ep216_victoria_block") # блокируем Юлию
    $ ep216_juliahome_blocked_day = day # блокируем мини-карту у дома Юлии


    $ add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_dick_office", label="ep216_victoria_block")
    $ add_hook("MonicaTable", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
    $ add_hook("MonicaChair", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
    $ add_hook("Julia", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
    $ add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_monica_office", label="ep216_victoria_block")
    $ add_hook("before_open", "ep216_quests_victoria3_street", scene="street_monica_office", label="ep216_victoria_block")
    $ add_hook("Worker1", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker2", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker5", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
    $ add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
    $ add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
    $ add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
    $ add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")

    $ add_hook("VictoriaHome_Enter", "ep216_quests_victoria4_enter", scene="street_victoriahome", label="ep216_victoria_visit_day1")
    $ add_hook("enter_scene", "ep216_quests_victoria3_street2", scene="street_victoriahome", label="ep216_victoria_visit_day1", once=True)
    $ autorun_to_object("ep216_dialogues5_victoria_12b", scene="working_office_cabinet")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_119
    return False

label ep216_quests_victoria3_street: # Моника выходит на улицу и наступает вечер
    $ remove_hook()
    if day_time != "evening":
        $ changeDayTime("evening")
    return

label ep216_quests_victoria3_street2: # Попадаем к Виктории на улицу
    $ unfocus_map()
    return

label ep216_quests_victoria4_enter: # вход к Виктории
    if act=="l":
        return
    if cloth != "CasualDress1":
        call ep216_dialogues5_victoria_8a() from _rcall_ep216_dialogues5_victoria_8a
        return False
    $ remove_hook()
    $ remove_hook(label="ep216_victoria_block")
    $ hudDaySkipToEveningEnabled = True
    $ ep216_juliahome_blocked_day = day-1 # разблокируем мини-карту у дома Юлии
    call ep216_dialogues5_victoria_2() from _rcall_ep216_dialogues5_victoria_2
    call ep216_dialogues5_victoria_4() from _rcall_ep216_dialogues5_victoria_4
    $ questHelp("victoria_12", True)
    if melanieVictoriaMonicaTable1 == True: # Моника осудила Мелани в гостях у Виктории, воткнула в нее розу
        call ep216_dialogues5_victoria_6() from _rcall_ep216_dialogues5_victoria_6
        $ questHelp("victoria_13", True)
        $ questHelp("victoria_14", False)

    else:
        $ autorun_to_object("ep216_dialogues5_victoria_5", scene="street_victoriahome")
        $ questHelp("victoria_13", False)
        $ questHelp("victoria_14", True)
    $ questHelp("office_48")
    $ add_hook("Melanie", "ep216_dialogues5_victoria_7", scene="monica_office_makeup_room", label="ep216_victoria_visit_day1_after")
    $ move_object("Melanie", "empty")
    $ ep216_victoria_visit_day1 = day
    $ officeWorker2BlockedUntilDay = day+1
    $ remove_objective("go_victoria")

    # инициализируем приход админа
    $ add_hook("office_work_process", "ep216_quests_victoria5_admin", scene="global", label="ep216_quests_victoria5_admin", priority = 90)


    call refresh_scene_fade() from _rcall_refresh_scene_fade_120
    return False

label ep216_quests_victoria5_admin: # приход админа и свидание с Викторией
    if ep216_victoria_visit_day2 == 0:
        call ep216_dialogues6_victoria_admin_1() from _rcall_ep216_dialogues6_victoria_admin_1
        $ ep216_victoria_visit_day2 = day
        $ questHelp("office_48", True)
#        $ questHelp("victoria_15", True)
        $ questHelp("office_49")
        # инициализируем приход админа второй день
        $ officeWorker2BlockedUntilDay = day+1
        return
    if ep216_victoria_visit_day3 == 0:
        # приход админа и свидание с Моникой
        $ remove_hook(label="ep216_quests_victoria5_admin")
        call ep216_dialogues6_victoria_admin_2() from _rcall_ep216_dialogues6_victoria_admin_2

#        $ questHelp("office_49", True)
#        $ questHelp("victoria_16")

        $ add_objective("go_victoria", t_("Идти к Виктории."), c_red, 125)
        $ monicaOfficeWorkedToday = True

        # блокируем перемещения
        $ focus_map("Teleport_VictoriaHome", "ep216_dialogues5_victoria_12b")
        $ move_object("Melanie", "empty")
        $ hudDaySkipToEveningEnabled = False # выключаем телепорт в кровать
        # выключаем сон
        $ add_hook("slums_apartments_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
        $ add_hook("hostel_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
        $ add_hook("juliahome_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")
        $ add_hook("basement_monica_before_sleep", "ep216_dialogues5_victoria_12", scene="global", label="ep216_victoria_block")

        # блокируем перемещения и работу
        $ add_hook("Building", "ep216_dialogues5_victoria_12", scene="street_police", label="ep216_victoria_block") # блокируем полицию
        $ add_hook("JuliaHome", "ep216_dialogues5_victoria_12", scene="street_juliahome", label="ep216_victoria_block") # блокируем Юлию
        $ ep216_juliahome_blocked_day = day # блокируем мини-карту у дома Юлии

        $ add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_dick_office", label="ep216_victoria_block")
        $ add_hook("MonicaTable", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
        $ add_hook("MonicaChair", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
        $ add_hook("Julia", "ep216_dialogues5_victoria_12", scene="working_office_cabinet", label="ep216_victoria_block")
        $ add_hook("Teleport_Inside", "ep216_dialogues5_victoria_12", scene="street_monica_office", label="ep216_victoria_block")
        $ add_hook("before_open", "ep216_quests_victoria3_street", scene="street_monica_office", label="ep216_victoria_block")
        $ add_hook("Worker1", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker2", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker5", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office", label="ep216_victoria_block")
        $ add_hook("Worker3", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
        $ add_hook("Worker4", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
        $ add_hook("Worker6", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")
        $ add_hook("Worker7", "ep216_dialogues5_victoria_12", scene="working_office2", label="ep216_victoria_block")

        $ add_hook("VictoriaHome_Enter", "ep216_quests_victoria6_dating", scene="street_victoriahome", label="ep216_victoria_visit_day3")

        $ autorun_to_object("ep216_dialogues5_victoria_12b", scene="working_office_cabinet")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_121

        return False
    return


label ep216_quests_victoria6_dating: #свидание админа и Моники
    if act=="l":
        return
    $ unfocus_map()
    if cloth != "CasualDress1":
        call ep216_dialogues5_victoria_8a() from _rcall_ep216_dialogues5_victoria_8a_1
        return False
    $ remove_hook()
    $ remove_hook(label="ep216_victoria_block")
    $ hudDaySkipToEveningEnabled = True
    $ ep216_juliahome_blocked_day = day-1 # разблокируем мини-карту у дома Юлии
    $ remove_objective("go_victoria")
    $ ep216_victoria_visit_day3 = day
    call ep216_dialogues6_victoria_admin_3() from _rcall_ep216_dialogues6_victoria_admin_3
    call ep216_dialogues6_victoria_admin_4() from _rcall_ep216_dialogues6_victoria_admin_4

#    $ questHelp("victoria_16", True)
    $ questHelp("office_49", True)
    $ questHelp("office_49a")

    $ autorun_to_object("ep216_dialogues6_victoria_admin_5", scene="street_victoriahome")

    $ add_hook("before_open", "ep216_quests_victoria7_admin_office", scene="working_office_cabinet", label="ep216_victoria_visit_day3_after")
    $ add_hook("before_open", "ep216_quests_victoria7_admin_office", scene="working_office", label="ep216_victoria_visit_day3_after")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_122
    return False

label ep216_quests_victoria7_admin_office: # Моника идет мимо админа на след. день
    if day_time != "day" or week_day == 7 or get_active_objects("Worker2", scene="working_office") == False:
        return
    $ remove_hook(label="ep216_victoria_visit_day3_after")
    call ep216_dialogues6_victoria_admin_6() from _rcall_ep216_dialogues6_victoria_admin_6
    $ ep216_victoria_visit_day4 = day
    $ questHelp("office_49a", True)
    $ autorun_to_object("ep216_dialogues6_victoria_admin_6b", scene="working_office_cabinet")
    call change_scene("working_office_cabinet", "Fade_long") from _rcall_change_scene_191
    return











#
