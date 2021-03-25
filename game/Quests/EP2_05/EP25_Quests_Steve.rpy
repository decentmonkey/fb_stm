default monicaMadeBlowjobForSteveChair = False
default monicaSteveCumDealActive = False
default monicaSteveCumDealRejected = False # Моника решила осуществить сделку, но позже отказалась от нее
default monicaSteveCumDealCompleted = False # Моника закрыла сделку

default monicaSteveBlowjobDealCount = 0 # Кол-во сделок со Стивом blowjob
default monicaSteveBlowjob50DollarsCount = 0 # Кол-во раз Моника получала 50 долларов сверху

default bettySteveOfficeTouchedSteveDick = False
default bettySteveOfficeSteveSex = False

label ep25_quests_steve1:
    # инициализация сцен и входа
    call locations_init_steve_office() from _call_locations_init_steve_office
    $ move_object("Steve", "empty")
    $ add_hook("Teleport_Building", "ep25_quests_steve2", scene = "street_steve_office", priority = 200, label="steve_office_check_evening")
    $ add_hook("Teleport_Building", "ep25_quests_steve3", scene="street_steve_office", label = "steve_office_enter")

    $ move_object("Jane", "steve_office_secretary")

    $ add_hook("Jane", "ep25_quests_steve5", scene="steve_office_secretary", label="jane_dialogue_regular1")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve5", scene="steve_office_secretary", label="jane_dialogue_regular1")
    $ add_hook("Jane", "ep25_quests_steve4", scene="steve_office_secretary", label="jane_dialogue1")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve4", scene="steve_office_secretary", label="jane_dialogue1")
    $ add_hook("open", "ep25_quests_steve4a", scene="steve_office_secretary")

    $ add_hook_day("ep26_quests_steve1", week_day = 6)

    return

label ep25_quests_steve2:
    # Вход в здание Стива, проверка на вечер
    if act == "l":
        return
    if week_day == 7:
        mt "Сегодня выходной. Офис Стива закрыт."
        return False
    if day_time == "evening":
        mt "Уже вечер. Офис Стива закрыт."
        return False
    return

label ep25_quests_steve3:
    # Вход в офис Стива
    if act == "l":
        return
    if act == "w":
        if cloth != "CasualDress1":
            call ep25_dialogues2_steve1b() from _call_ep25_dialogues2_steve1b
            return False
        call change_scene("steve_office_secretary", "Fade_long", "snd_lift") from _call_change_scene_278
    return False


label ep25_quests_steve4:
    # первый разговор с Джейн
    if act=="l" and obj_name=="Jane":
        return
    $ remove_hook(label="jane_dialogue1")
    call ep25_dialogues2_steve1() from _call_ep25_dialogues2_steve1
    $ questHelp("steve_7", True)
    $ questHelp("steve_8", True)
    $ questHelp("steve_9")
    $ questHelpDesc("steve_desc4")
    call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_279
    $ add_hook("change_time_day", "ep25_quests_steve6", scene="global") # Инициализация второго прихода Моники с утра
    $ questLog(33, False)
    $ questLog(40, True)

    return False

label ep25_quests_steve4a:
    # Музыка входа Моники
    $ remove_hook()
    music m80s_Things
    return

label ep25_quests_steve5:
    # регулярный разговор с Джейн 1
    if act=="l" and obj_name == "Jane":
        return
    call ep25_dialogues2_steve1a() from _call_ep25_dialogues2_steve1a
    call refresh_scene_fade() from _call_refresh_scene_fade_105
    return False

label ep25_quests_steve6:
    # Инициализация второго прихода Моники с утра
    $ remove_hook()
    $ add_hook("Jane", "ep25_quests_steve7", scene="steve_office_secretary", label="jane_dialogue2")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve7", scene="steve_office_secretary", label="jane_dialogue2")
    return

label ep25_quests_steve7:
    # Второй диалог с Джейн (приходит Тиффани)
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="jane_dialogue2")
    call ep25_dialogues2_steve2() from _call_ep25_dialogues2_steve2

    $ autorun_to_object("ep25_dialogues2_steve2a", scene="street_steve_office")
    $ add_hook("change_time_day", "ep25_quests_steve8", scene="global") # Третьий приход Моники (инициализация с утра)
    call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_280
    return False

label ep25_quests_steve8:
    # Инициализация третьего прихода Моники с утра
    $ remove_hook()
    $ add_hook("Jane", "ep25_quests_steve9", scene="steve_office_secretary", label="jane_dialogue3")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve9", scene="steve_office_secretary", label="jane_dialogue3")
    $ steve_office_secretary_suffix = 2
    return


label ep25_quests_steve9:
    # Третий разговор с Джейн (заходит к Стиву)
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="jane_dialogue3")
    call ep25_dialogues2_steve3() from _call_ep25_dialogues2_steve3
#    $ monicaHasSexWithSteveBasement = False # debug!!
    if monicaHasSexWithSteveBasement == True: # У Моники был секс со Стивом
        call ep25_dialogues2_steve4() from _call_ep25_dialogues2_steve4
        $ questHelp("steve_9", True)
#        $ questHelp("steve_10")
#        $ questHelp("steve_17")
        $ questHelpDesc("steve_desc4", "steve_desc5")

        $ move_object("Steve", "steve_office_office_table")
        $ add_hook("Steve", "ep25_quests_steve10", scene="steve_office_office_table", label="steve_office_steve_dialogue1")
        $ add_hook("Door", "ep25_quests_steve10", scene="steve_office_office_table", label="steve_office_steve_dialogue1")
        call change_scene("steve_office_office_table", "Fade_long", False) from _call_change_scene_281
        return False
    else:
        # Секса со Стивом не было
        call ep25_dialogues2_steve10() from _call_ep25_dialogues2_steve10
        if _return == True: # Моника сделала минет Стиву
            $ notif(t_("Стив перевел деньги Виктории."))
            $ monicaEarnedWeeklyMoney = True
            $ remove_objective("money_for_victoria")
            $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива


        $ questHelp("steve_9", True)
        $ questHelp("steve_10", skipIfExists=True)
        $ questHelp("steve_17", skipIfExists=True)
        $ questHelpDesc("steve_desc4", "steve_desc5")
        $ questLog(40, False)
        $ questLog(42, True)
        # Регулярный приход к Стиву
        $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="steve_office_blocked_today") # Блокируем вход в здание на сегодня
        $ add_hook("change_time_day", "ep25_quests_steve16", scene="global") # Релуярный приход Моники (инициализация с утра)
        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_282
#    $ monicaHasSexWithSteveBasement = True
#            $ monicaSteveBasementOffended = True

    return False

label ep25_quests_steve10:
    # Разговор со Стивом (секс был)
    if act=="l":
        return
    $ remove_hook(label="steve_office_steve_dialogue1")
    call ep25_dialogues2_steve4a() from _call_ep25_dialogues2_steve4a
    if _return == False:
        # Моника не делала минет. Добилась денег угрозой
        $ questHelp("steve_9b", True)
        $ questHelp("steve_10")
        $ questHelp("steve_17")
        $ questLog(40, False)
        $ questLog(42, True)
        $ notif(t_("Стив перевел деньги Виктории."))
        $ monicaEarnedWeeklyMoney = True
        $ remove_objective("money_for_victoria")
        $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива

        # Регулярный приход к Стиву
        $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="steve_office_blocked_today") # Блокируем вход в здание на сегодня
        $ add_hook("change_time_day", "ep25_quests_steve16", scene="global") # Релуярный приход Моники (инициализация с утра)

        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_283
        return False
    else:
        # Моника сделала минет, но Стив деньги не послал
        $ questHelp("steve_9c")
        $ autorun_to_object("ep25_dialogues2_steve5", scene="street_steve_office")
        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_284
        $ add_hook("Teleport_Building", "ep25_dialogues2_steve5a", scene="street_steve_office", label="need_check_steve_money1") # Блокируем вход в здание пока не проверили деньги
        $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива
        $ add_hook("DickSecretary_Dialogue1_Menu", "ep25_quests_steve11", scene="menu", label="need_check_steve_money_victoria1", caption=t_("Стив прислал деньги."), priority=95) # У Виктории спрашиваем про деньги Стива (новый диалог)

    return

label ep25_quests_steve11:
    # Моника разговаривает с Викторией о деньгах от Стива
    call ep25_dialogues2_steve6() from _call_ep25_dialogues2_steve6
    $ remove_hook(label="need_check_steve_money1") # Разблокируем вход к Стиву
    $ add_hook("Jane", "ep25_quests_steve12", scene="steve_office_secretary", label="jane_dialogue4")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve12", scene="steve_office_secretary", label="jane_dialogue4")
    $ questHelp("steve_9c", True)
    $ questHelp("steve_9d")
    $ questHelpDesc("steve_desc2", "steve_desc3")
    return False

label ep25_quests_steve12:
    # Разговор с Джейн в 4-ый раз
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="need_check_steve_money_victoria1") # Убираем у Виктории вопрос про деньги
    $ add_hook("change_time_day", "ep25_quests_steve13", scene="global") # Пятый приход Моники (инициализация с утра)
    $ questHelp("steve_9d", True)
    $ questHelp("steve_9e")
    call ep25_dialogues2_steve7() from _call_ep25_dialogues2_steve7
    return False

label ep25_quests_steve13:
    # Пятый приход Моники (иницилизация с утра)
    $ remove_hook()
    $ remove_hook(label="jane_dialogue4")
    $ add_hook("Jane", "ep25_quests_steve14", scene="steve_office_secretary", label="jane_dialogue5")
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve14", scene="steve_office_secretary", label="jane_dialogue5")
    return

label ep25_quests_steve14:
    # Пятый диалог с Джейн (заходит к Стиву) (Стив не прислал деньги за минет)
    if act=="l" and obj_name == "Jane":
        return
    $ remove_hook(label="jane_dialogue5")
    call ep25_dialogues2_steve8() from _call_ep25_dialogues2_steve8
    if _return == True:
        $ monicaSteveCumDealActive = True
        $ autorun_to_object("ep25_dialogues2_steve9", scene="street_steve_office")
    call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_285
    $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="steve_office_blocked_today") # Блокируем вход в здание на сегодня
    $ add_hook("change_time_day", "ep25_quests_steve16", scene="global") # Релуярный приход Моники (инициализация с утра)
    $ questLog(40, False)
    $ questLog(41, True)

    return False

label ep25_quests_steve15:
    # Блок на вход в офис Стива сегодня
    call ep25_dialogues2_steve11() from _call_ep25_dialogues2_steve11
    return False

label ep25_quests_steve16:
    $ remove_hook()
    $ remove_hook(label="steve_office_blocked_today") # Убираем блок с офиса Стива
    $ steve_office_secretary_suffix = 1 # Джейн сидит
    $ remove_hook(label="jane_dialogue_regular1")
    $ add_hook("Jane", "ep25_quests_steve17", scene="steve_office_secretary", label="jane_dialogue_regular2") # Регулярный диалог с Джейн
    $ add_hook("Teleport_Steve_Office_Office", "ep25_quests_steve18", scene="steve_office_secretary", label="jane_dialogue_regular2") # Регулярный телепорт в офис Стива мимо Джейн
    call Steve_init() from _call_Steve_init # Инициализируем Стива
    $ add_hook("steve_office_dialogue", "ep25_quests_steve16a", scene="global", label="steve_first_regular_dialogue_remove_victoria_menu") # При первом регулярном разговоре со Стивом убираем упоминание про деньги у Виктории
    return

label ep25_quests_steve16a:
    # При первом регулярном разговоре со Стивом убираем упоминание про деньги у Виктории
    $ remove_hook()
    $ remove_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu") # Убираем из меню Виктории вопрос про деньги Стива
    return

label ep25_quests_steve17:
    # Регулярный диалог с Джейн 2
    if act == "l" and obj_name == "Jane":
        return
    call getSteveStatus() from _call_getSteveStatus
    call ep25_dialogues3_steve1(_return) from _call_ep25_dialogues3_steve1
    if _return == 0:
        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_286
        return False
    call refresh_scene_fade() from _call_refresh_scene_fade_106
    return False

label ep25_quests_steve18:
    # Регулярный вход в офис Стива по телепорту
    call getSteveStatus() from _call_getSteveStatus_1
    if _return != 0:
        call ep25_dialogues3_steve1(_return) from _call_ep25_dialogues3_steve1_1
        call ep25_dialogues3_steve1aa() from _call_ep25_dialogues3_steve1aa
        if _return == True:
            music Groove2_85
            call change_scene("steve_office_office", "Fade_long") from _call_change_scene_287
        else:
            call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_288
        return False

    # Регулярный разговор со Стивом
    call process_hooks("steve_office_dialogue", "global") from _call_process_hooks_57
    if _return == False:
        return False
    call ep25_dialogues3_steve1a() from _call_ep25_dialogues3_steve1a
    if _return == 0:
        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_289
        return False
    if _return == 1: # Моника закрывает cum сделку
        call ep25_dialogues3_steve1b() from _call_ep25_dialogues3_steve1b
        $ questHelp("steve_10", skipIfExists=True)
        $ questHelp("steve_17", skipIfExists=True)
        if _return == False:
            call ep25_quests_steve19() from _call_ep25_quests_steve19 # Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_290
            return False

        $ questHelp("steve_9b", True)
        $ monicaSteveCumDealActive = False
        $ monicaSteveCumDealCompleted = True
        $ notif(t_("Стив перевел деньги Виктории."))
        $ monicaEarnedWeeklyMoney = True
        $ remove_objective("money_for_victoria")
        $ questLog(40, False)
        $ questLog(41, False)
        $ questLog(42, True)
        call ep25_quests_steve19() from _call_ep25_quests_steve19_1 # Блокируем офис на сегодня (день)
        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_291
        return False

    if _return == 2: # Сделка со Стивом (blowjob)
        if monicaSteveContractJaneAwaits == True:
            call ep26_dialogues2_steve2() from _call_ep26_dialogues2_steve2 # Контракт с Джейн не произведен, контракты со Стивом блокируются
            call change_scene("steve_office_secretary", "Fade_long") from _call_change_scene_323
            return False

        call ep25_dialogues3_steve2() from _call_ep25_dialogues3_steve2
        if _return == False:
            call ep25_quests_steve19() from _call_ep25_quests_steve19_2 # Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_292
            return False
        $ choosedMoney = _return
        if choosedMoney == 0:
            # Моника ушла после того как узнала, что нужно отрабатывать неустойку
            call ep25_quests_steve19() from _call_ep25_quests_steve19_8# Блокируем офис на сегодня (день)
            call change_scene("street_steve_office", "Fade_long", False) from _call_change_scene_324
            return False

        $ noMoney = False
        if choosedMoney == -1: # При таком параметре, деньги не начисляем
            $ noMoney = True
        $ monicaSteveBlowjobDealCountOffs = monicaSteveBlowjobDealCount % 6
        if monicaSteveBlowjobDealCount > 5 and bettyVisitedSteve == False:
            $ bettyVisitedSteve = True
            call ep26_dialogues2_steve5() from _call_ep26_dialogues2_steve5
            $ questHelp("steve_16", True)
            $ questHelp("house_44a", True)
#            $ questHelp("office_30", skipIfExists=True)
            if _return == False:
                $ noMoney = True
        else:
            if monicaSteveBlowjobDealCountOffs == 0:
                # Первый приход Джейн
                call ep25_dialogues3_steve3a() from _call_ep25_dialogues3_steve3a
                $ questHelp("steve_10", True)
                $ questHelp("steve_11", skipIfExists=True)
            if monicaSteveBlowjobDealCountOffs == 1:
                call ep25_dialogues3_steve4a() from _call_ep25_dialogues3_steve4a
                $ questHelp("steve_11", True)
                $ questHelp("steve_12", skipIfExists=True)
            if monicaSteveBlowjobDealCountOffs == 2:
                call ep25_dialogues3_steve3b() from _call_ep25_dialogues3_steve3b
                $ questHelp("steve_12", True)
                $ questHelp("steve_13", skipIfExists=True)
            if monicaSteveBlowjobDealCountOffs == 3:
                call ep25_dialogues3_steve4b() from _call_ep25_dialogues3_steve4b
                $ questHelp("steve_13", True)
                $ questHelp("steve_14", skipIfExists=True)
            if monicaSteveBlowjobDealCountOffs == 4:
                call ep25_dialogues3_steve3c() from _call_ep25_dialogues3_steve3c
                $ questHelp("steve_14", True)
                $ questHelp("steve_15", skipIfExists=True)
            if monicaSteveBlowjobDealCountOffs == 5:
                call ep25_dialogues3_steve4c() from _call_ep25_dialogues3_steve4c
                $ questHelp("steve_15", True)
                $ questHelp("steve_16", skipIfExists=True)
                $ questHelp("house_44a", skipIfExists=True)

#        if monicaSteveBlowjobDealCount > 5:
#            # random
#            $ rnd1 = rand(1,6)
#            if rnd1 == 1:
#                call ep25_dialogues3_steve3a()
#            if rnd1 == 2:
#                call ep25_dialogues3_steve4a()
#            if rnd1 == 3:
#                call ep25_dialogues3_steve3b()
#            if rnd1 == 4:
#                call ep25_dialogues3_steve4b()
#            if rnd1 == 5:
#                call ep25_dialogues3_steve3c()
#            if rnd1 == 6:
#                call ep25_dialogues3_steve4c()

        $ monicaSteveBlowjobDealCount +=1
        if noMoney == False:
            if choosedMoney == 1:
                $ add_money(50.0)
                $ monicaSteveBlowjob50DollarsCount +=1
            $ notif(t_("Стив перевел деньги Виктории."))
            $ monicaEarnedWeeklyMoney = True
            $ remove_objective("money_for_victoria")

        call ep25_quests_steve19() from _call_ep25_quests_steve19_3 # Блокируем офис на сегодня (день)
        call change_scene("street_steve_office", "Fade_long", False) from _call_change_scene_293
        return False

    if _return == 3: # Сделка с Джейн (blowjob)
        call ep26_quests_steve2() from _call_ep26_quests_steve2
        return False


    return

label ep25_quests_steve19:
    # Закрываем офис Стива до вечера
    $ add_hook("Teleport_Building", "ep25_quests_steve15", scene="street_steve_office", label="day_time_temp") # Блокировка офиса до вечера
    return




#
