default bettyShowedPantiesLastDay = 0
default bettyPantiesFloor2TalkFlag = False
default bettyKnowsAboutPanties = False

label ep24_quests_betty1:
    # Бетти ловит Монику, чтобы сказать что теперь Моника может проверять ее трусики
    if cloth != "Governess" or day_time != "day":
        return
    call ep24_dialogues5_betty1() from _call_ep24_dialogues5_betty1
    $ questHelp("house_15")
    $ questHelp("house_14", True)
    $ questHelpDesc("house_desc9", "house_desc10")
    $ remove_hook(label="betty_catch1")
    $ add_hook("Betty", "ep24_quests_betty2", scene="floor2", group="dialouge_regular")
    $ add_hook("Betty", "ep24_quests_betty6", scene="bedroom1", group="dialouge_regular")
    $ add_hook("Bardie", "ep24_quests_bardie13", scene="floor2", group="dialogue_regular", priority=105)
    $ add_hook("Bardie", "ep24_quests_bardie14", scene="bedroom1", group="dialogue_regular", priority=105)
    $ add_hook("Bardie_Life_day", "Bardie_Life_day5", scene="global")

    $ add_hook("ep24_quests_betty2_menu1", "ep24_quests_betty3", scene="menu", label="menu_betty_panties_show_to_monica", caption=t_("Миссис Робертс, я бы хотела проверить Ваши трусики..."), priority = 90)
    $ add_hook("monica_betty_dialogue_floor2_end_menu", "ep24_quests_betty3", scene="menu", label="menu_betty_panties_show_to_monica", caption=t_("Миссис Робертс, я бы хотела проверить Ваши трусики..."))
    $ add_hook("floor2_betty_fitness_dialogue", "ep24_quests_betty3", scene="menu", label="menu_betty_panties_show_to_monica", caption=t_("Миссис Робертс, я бы хотела проверить Ваши трусики..."), priority = 80)
    $ add_hook("betty_bedroom_dialogue_regular_menu", "ep24_quests_betty7", scene="menu", label="menu_betty_panties_show_to_monica", caption=t_("Миссис Робертс, я бы хотела проверить Ваши трусики..."), priority = 104, active="checkTimeDay")
    $ add_hook("betty_bedroom_dialogue_regular_menu", "Betty_Life_Dialogue_Bedroom1", scene="menu", label="menu_betty_regular_dialogue", caption=t_("Говорить."), priority = 105)

    $ add_hook("floor2_bardie_dialogue_regular_menu", "ep24_quests_betty8", scene="menu", label="menu_betty_panties_show_to_bardie", caption=t_("Смотреть."), active="checkTimeDay")
    $ add_hook("bedroom1_bardie_dialogue_regular_menu", "ep24_quests_betty9", scene="menu", label="menu_betty_panties_show_to_bardie", caption=t_("Смотреть."), active="checkTimeDay")

    $ add_hook("betty_showed_panties_to_monica", "ep24_quests_betty4", scene="misc", label="menu_betty_panties_show_to_monica_progress")
    $ bettyPantiesFloor2TalkFlag = True

    $ char_info["Betty"]["enabled"] = True
    $ char_info["Betty"]["caption"] = t_("Бетти должна показать, если я спрошу ее об этом....")
    $ questLog(20, False)
    $ questLog(35, False)
    $ questLog(36, True)
    $ questLog(37, True)

    $ bettyKnowsAboutPanties = True
    $ monicaPussyShaved = True

    $ add_hook("enter_scene", "ep24_quests_betty1a")

    call floor2_init_addition1() from _call_floor2_init_addition1_2
    call bedroom1_init_addition1() from _call_bedroom1_init_addition1_2

    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_39
    return

label ep24_quests_betty1a:
    # Показывание что прогресс с Бетти активирован
    $ remove_hook()
    call ep24_dialogues5_betty0a() from _call_ep24_dialogues5_betty0a
    return

label ep24_quests_betty2:
    # Регулярный разговор с Бетти у зеркал floor2
    if act=="l":
        return
    if cloth != "Governess":
        call bettyDialogue3() from _call_bettyDialogue3_3
        return False
    $ EP22_Quests_Betty3Flag1 = False
    if monicaCleaningInProgressEngineWorkingFlag == True:
        $ menuName = "ep24_quests_betty2_menu1"
        menu:
            "Говорить." if bettyFitnessToday == True:
                call ep22_dialogues4_1b() from _call_ep22_dialogues4_1b_1
            "Миссис Робертс. Барди зовет Вас в свою комнату..." if bardieCalledBettyForPunishment == True:
                call ep26_quests_bardie7() from _call_ep26_quests_bardie7
            "Уйти.":
                pass
            "":
                pass
        return False
    call ep22_dialogues4_1() from _call_ep22_dialogues4_1_1
    $ lastReturn = _return

    $ _return = lastReturn
    if EP22_Quests_Betty3Flag1 == True:
        $ EP22_Quests_Betty3Flag1 = False #Флаг, чтобы ничего не делать (для меню сообщения Барди о фитнесе)
        return False
    if _return == False:
        if bettyFitnessToday == True:
            $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15}, {"driverOnHouseYard":{"v":False, "active":False}}, scene="street_house_main_yard")
            $ move_object("Betty", "empty")
            $ move_object("Driver", "empty")
            call refresh_scene_fade() from _call_refresh_scene_fade_83
        return False
    $ add_cleaning(True)
    $ add_hook("open", "EP22_Quests_Betty4", scene="street_fitness")
    call change_scene("street_fitness", "Fade_long", "snd_car_engine") from _call_change_scene_232
    return False

label ep24_quests_betty3:
    # Моника просит Бетти показать трусики у зеркала
    $ EP22_Quests_Betty3Flag1 = True
    $ Bardie_Life_day5_day = day
    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_40
    if bettyMustNotWearPanties == False:
        call ep24_dialogues5_betty4() from _call_ep24_dialogues5_betty4
    else:
        call ep24_dialogues5_betty7() from _call_ep24_dialogues5_betty7
    if _return != False:
        call process_hooks("betty_showed_panties_to_monica", "misc") from _call_process_hooks_41
        $ bettyShowedPantiesLastDay = day
    call refresh_scene_fade() from _call_refresh_scene_fade_84
    return False

label ep24_quests_betty4:
    # Прогресс после показывания Бетти трусиков Монике
    $ add_char_progress("Betty", bettyShowPantiesToMonicaProgress, "betty_showed_panties_to_monica" + str(day))
    return

label ep24_quests_betty6:
    # Регулярный разговор с Бетти в спальне
    if act=="l":
        return
    $ menuName = "betty_bedroom_dialogue_regular_menu"
    $ Bardie_Life_day5_day = day
    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_42
    menu:
        "Миссис Робертс. Барди зовет Вас в свою комнату..." if bardieCalledBettyForPunishment == True:
            call ep26_quests_bardie7() from _call_ep26_quests_bardie7_1
            return False
        "Уйти.":
            return False
        "":
            pass
    return False
label ep24_quests_betty7:
    # Моника просит Бетти показать трусики в спальне (регулярный разговор)
    if bettyMustNotWearPanties == False:
        call ep24_dialogues5_betty3() from _call_ep24_dialogues5_betty3
    else:
        call ep24_dialogues5_betty6() from _call_ep24_dialogues5_betty6
    if _return != False:
        call process_hooks("betty_showed_panties_to_monica", "misc") from _call_process_hooks_43
        $ bettyShowedPantiesLastDay = day
    call refresh_scene_fade() from _call_refresh_scene_fade_85
    return False


label ep24_quests_betty8:
    # Барди проверяет трусики Бетти на floor2
    $ Bardie_Life_day5_day = day
    call ep24_dialogues5_betty2b() from _call_ep24_dialogues5_betty2b
    call process_hooks("betty_showed_panties_to_bardie", "misc") from _call_process_hooks_44
    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_45
    sound snd_runaway
    call refresh_scene_fade() from _call_refresh_scene_fade_86
    return False
label ep24_quests_betty9:
    # Барди проверяет трусики Бетти в bedroom1
    $ Bardie_Life_day5_day = day
    call ep24_dialogues5_betty2() from _call_ep24_dialogues5_betty2
    call process_hooks("betty_showed_panties_to_bardie", "misc") from _call_process_hooks_46
    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_47
    sound snd_runaway
    call refresh_scene_fade() from _call_refresh_scene_fade_87
    return False

label ep24_quests_betty5:
    # Продолжение квеста (Барди заставляет ходить без трусиков)
    $ add_hook("change_time_day", "ep24_quests_betty10", scene="global")
    return

label ep24_quests_betty10:
    if monicaRestHouse != True:
        return
    # Инициализация catch Бетти Моники с утра
    $ remove_hook()
    $ add_hook("map_teleport", "ep24_quests_betty11", scene="global", label="betty_catch2", priority = 1001)
    $ add_hook("before_open", "ep24_quests_betty11", scene="floor1_stairs", label="betty_catch2") # Переход ногами на лестницу из подвала
    $ add_hook("before_open", "ep24_quests_betty11", scene="bedroom1", label="betty_catch2")
    $ add_hook("before_open", "ep24_quests_betty11", scene="bedroom2", label="betty_catch2")
    $ add_hook("before_open", "ep24_quests_betty11", scene="bathroom_bath", label="betty_catch2")
    $ add_hook("before_open", "ep24_quests_betty11", scene="floor1", label="betty_catch2")
    $ add_hook("before_open", "ep24_quests_betty11", scene="floor2", label="betty_catch2")
    $ add_hook("before_open", "ep24_quests_betty11", scene="kitchen2", label="betty_catch2")
    $ add_hook("before_open", "ep24_quests_betty11", scene="street_house_main_yard", label="betty_catch2")

    return

label ep24_quests_betty11:
    if cloth != "Governess" or day_time != "day":
        return
    call ep24_dialogues5_betty5() from _call_ep24_dialogues5_betty5
    $ questHelp("house_16")
    $ questHelp("house_16b")
    $ questHelpDesc("house_desc10", "house_desc11")
    $ questHelpDesc("house_desc12")
    $ remove_hook(label="betty_catch2")
    $ monicaMustNotWearPanties = True
    $ bettyMustNotWearPanties = True
    $ monicaMustWearBettyPanties = False
    $ monicaLaundryBettyPantiesSelectMode = 1 #Выбор в прачечной
    $ monicaLaundryBettyPantiesSelectNudeDisabled = False

    call bettyGetTodayPanties() from _call_bettyGetTodayPanties_4
    call bedroom1_init_addition2() from _call_bedroom1_init_addition2

    $ char_info["Betty"]["enabled"] = True
    $ char_info["Bardie"]["enabled"] = True
    $ char_info["Betty"]["caption"] = t_("Бетти запрещено носить трусики....")
    $ add_hook("wardrobe_menu", "wardrobePutGovernessWithoutPanties", scene="menu", label="menu_governess_without_panties", caption = t_("Униформа гувернантки (без трусиков)"), active="checkGovernessWithoutPantiesActive", priority = 80)

#    $ add_hook("change_time_day", "ep24_quests_steve9", scene="global")

    $ add_hook("monica_cleaning_end", "ep24_quests_bardie15", scene="global", label="bardie_punishment_check")

    $ questLog(36, False)
    $ questLog(38, True)
    $ questLog(37, False)
    $ questLog(39, True)

    # Инициализация квестов в v0.6!
    call ep26_quests_bardie1() from _call_ep26_quests_bardie1

    $ autorun_to_object("basement_bedroom2", "ep24_dialogues5_betty5a")
    $ basement_bedroom2_MonicaSuffix = 2
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_233

    return False
