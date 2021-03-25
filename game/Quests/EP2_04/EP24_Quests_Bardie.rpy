default bettyBardieFitnessStage = 0
default bardieMonicaNonNudeCount = 0
default bardieMonicaPunishmentCount = 0

default bardieBettyBlackmailingStarted = False
default bardieBettyBlackmailingSteveStartFailed = False

label ep24_quests_bardie1:
    # Барди зовет Монику после уборки (после первого застолья со Стивом)
    # Либо после (если уровень не прокачан)
    $ restore_music()
    $ remove_hook()
    $ remove_hook(label="bardie_blackmail_planned")
#    if char_info["Bardie"]["level"] < 3 or char_info["Betty"]["level"] < 4:
#        $ bardieBettyBlackmailingSteveStartFailed = True
#        return
#    $ bardieBettyBlackmailingStarted == True
    call ep24_dialogues1_bardie() from _call_ep24_dialogues1_bardie
    if _return == False:
        $ add_hook("Bardie", "ep24_quests_bardie2", scene="bedroom_bardie")
        $ questHelp("house_11", False)
    else:
        $ questLog(34, True)
        $ questHelp("house_12")
        $ questHelp("house_11", True)
        $ questHelpDesc("house_desc8")
        $ add_hook("floor2_betty_fitness_dialogue", "ep24_quests_bardie3", scene="menu", caption=t_("Согласиться и предупредить Барди..."), priority=95, active=True)
        $ add_hook("enter_scene", "ep24_quests_bardie1a", scene="basement_bedroom2")
        $ add_hook("Bardie_Life_day", "Bardie_Life_day4", scene="global", priority = 101, label="bardie_fitness_global")
        $ add_hook("Bardie_Life_evening", "Bardie_Life_evening4", scene="global", priority = 101, label="bardie_fitness_global")
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_210
    return

label ep24_quests_bardie1b:
    # Барди зовет Монику после уборки (проверка регулярная, если сразу после прихода Стива у Барди не был уровень 3)
    if bardieBettyBlackmailingStarted == True or bardieBlackmailStage >= 5:
        $ bardieBettyBlackmailingStarted = True
        return
    if char_info["Bardie"]["level"] < 4 or char_info["Betty"]["level"] < 4:
        return
    $ bardieBettyBlackmailingStarted = True
    $ add_hook("monica_cleaning_end", "ep24_quests_bardie1", scene="global", label="bardie_blackmail_planned")
    return

label ep24_quests_bardie1a:
    # Активация прогресса Барди
    $ remove_hook()
    call ep24_dialogues1_bardie3() from _call_ep24_dialogues1_bardie3
    $ char_info["Bardie"]["enabled"] = True
    $ bardieBlackmailStage = 5
    return

label ep24_quests_bardie2:
    # Моника отказалась от помощи Барди, повтор диалога начинается у Барди в комнате
    if act=="l":
        return
    if cloth != "Governess":
        return
    call ep24_dialogues2_bardie() from _call_ep24_dialogues2_bardie
    if _return == True:
        $ remove_hook()
        call ep24_quests_bardie1() from _call_ep24_quests_bardie1
        return False
    return False

label ep24_quests_bardie3:
    # Нажато меню Согласиться и предупредить Барди...
    $ EP22_Quests_Betty3Flag1 = True
    if questHelpFlag1 == False:
        $ questHelpFlag1 = True
        $ questHelp("fitness_2")
    call ep24_dialogues5_betty0() from _call_ep24_dialogues5_betty0
    $ move_object("Bardie", scene="bedroom_bardie")
    $ add_hook("Bardie", "ep24_quests_bardie4", scene="bedroom_bardie", label=["day_time_temp", "bardie_fitness"])
    call refresh_scene_fade() from _call_refresh_scene_fade_73
    return

label ep24_quests_bardie4:
    # Моника сообщает Барди о том что они едут на фитнесс
#    $ remove_hook()
    if cloth != "Governess":
        return
    call ep24_dialogues3_fitness1() from _call_ep24_dialogues3_fitness1
    if _return == True:
        $ add_hook("Betty", "ep24_quests_bardie5", scene="floor2", label=["day_time_temp", "bardie_fitness"])

    call refresh_scene_fade() from _call_refresh_scene_fade_74
    return False

label ep24_quests_bardie5:
    # Моника говорит Бетти что она вернулась от Барди и можно ехать на фитнесс
    call ep22_dialogues4_1a0() from _call_ep22_dialogues4_1a0
    if _return == False:
        return False

    $ remove_hook(label="bardie_fitness")
    $ add_cleaning(True)
    $ add_hook("open", "EP22_Quests_Betty4", scene="street_fitness")
    $ add_hook("fitness_end", "ep24_quests_bardie6", scene="global")
    call change_scene("street_fitness", "Fade_long", "snd_car_engine") from _call_change_scene_211
    return False

label ep24_quests_bardie6:
    # Моника говорит Барди что Бетти осталась одна
    $ remove_hook()
    call ep24_dialogues3_fitness2() from _call_ep24_dialogues3_fitness2
    if bettyBardieFitnessStage == 0:
        call ep24_dialogues3_fitness3() from _call_ep24_dialogues3_fitness3
        $ add_hook("enter_scene", "ep24_quests_bardie7", scene="street_house_main_yard")
        music stop
        call EP22_Quests_Betty8() from _call_EP22_Quests_Betty8
#        $ basement_bedroom2_MonicaSuffix = 2
#        call change_scene("basement_bedroom2", "Fade_long", False)
        return False
    if bettyBardieFitnessStage == 1:
        call ep24_dialogues3_fitness3b() from _call_ep24_dialogues3_fitness3b
        $ add_hook("enter_scene", "ep24_quests_bardie7", scene="street_house_main_yard")
        music stop
        call EP22_Quests_Betty8() from _call_EP22_Quests_Betty8_1
        return False
    if bettyBardieFitnessStage == 2:
        call ep24_dialogues3_fitness3c() from _call_ep24_dialogues3_fitness3c
        $ add_hook("enter_scene", "ep24_quests_bardie7", scene="street_house_main_yard")
        music stop
        call EP22_Quests_Betty8() from _call_EP22_Quests_Betty8_2
        return False
    if bettyBardieFitnessStage == 3:
        call ep24_dialogues3_fitness3d() from _call_ep24_dialogues3_fitness3d
        $ add_hook("enter_scene", "ep24_quests_bardie7", scene="street_house_main_yard")
        music stop
        call EP22_Quests_Betty8() from _call_EP22_Quests_Betty8_3
        $ questHelp("house_12", True)
        $ questHelp("fitness_2", True)
        $ questHelp("house_13")
        return False

    return False

label ep24_quests_bardie7:
    # Моника оказывается в спальне в подвале после фитнеса с Барди
    $ remove_hook()
    call ep24_dialogues3_fitness5() from _call_ep24_dialogues3_fitness5
    $ add_hook("basement_monica_before_sleep", "ep24_quests_bardie8", scene="global", priority = 200, label="bardie_fitness")
    $ add_hook("Bardie", "ep24_quests_bardie9", scene="bedroom_bardie")
    return

label ep24_quests_bardie8:
    # спать не лечь, пока не поговорила с Барди
    call ep24_dialogues3_fitness5() from _call_ep24_dialogues3_fitness5_1
    return False

label ep24_quests_bardie9:
    # Моника разговаривает с Барди после фитнеса
    if act=="l":
        return
    $ remove_hook()
    $ remove_hook(label="bardie_fitness")
    $ add_hook("Bardie", "ep24_quests_bardie9a", scene="bedroom_bardie", label="bardie_fitness")
    call ep24_dialogues4_bardie1() from _call_ep24_dialogues4_bardie1
    $ questHelp("house_9", True)
#    if melanieDisappeared == False:
#        $ questHelp("house_9a")

    $ bettyBardieFitnessStage += 1
    $ add_char_progress("Bardie", 25, "bardie_fitness" + str(bettyBardieFitnessStage))
    if bettyBardieFitnessStage == 4:
        $ add_hook("change_time_day", "ep24_quests_bardie10", scene="global")
        $ remove_hook(label="bardie_fitness")
        $ remove_hook("floor2_betty_fitness_dialogue", "ep24_quests_bardie3", scene="menu")
        $ questLog(34, False)
        $ questLog(35, True)
        $ add_hook("bardie_cleaning_interact_after", "ep24_quests_bardie11", scene="misc")
        $ add_hook("bardie_cleaning_interact_wrongpanties", "ep24_quests_bardie12", scene="misc")
    call refresh_scene_fade() from _call_refresh_scene_fade_75
    return False

label ep24_quests_bardie9a:
    # повтор разговора с Барди после фитнеса
    if act=="l":
        return
    call ep24_dialogues4_bardie1() from _call_ep24_dialogues4_bardie1_1
    return False

label ep24_quests_bardie10:
    # Инициализация хуков разговора Моники и Бетти о том что Моника может проверять трусики Бетти
    if monicaRestHouse != True:
        return
    $ remove_hook()
    $ remove_hook(label="bardie_fitness_global")

    $ questHelp("house_13", True)
    $ questHelp("house_14")

    $ add_hook("map_teleport", "ep24_quests_betty1", scene="global", label="betty_catch1", priority = 1001)
    $ add_hook("before_open", "ep24_quests_betty1", scene="floor1_stairs", label="betty_catch1") # Переход ногами на лестницу из подвала
    $ add_hook("before_open", "ep24_quests_betty1", scene="bedroom1", label="betty_catch1")
    $ add_hook("before_open", "ep24_quests_betty1", scene="bedroom2", label="betty_catch1")
    $ add_hook("before_open", "ep24_quests_betty1", scene="bathroom_bath", label="betty_catch1")
    $ add_hook("before_open", "ep24_quests_betty1", scene="floor1", label="betty_catch1")
    $ add_hook("before_open", "ep24_quests_betty1", scene="floor2", label="betty_catch1")
    $ add_hook("before_open", "ep24_quests_betty1", scene="kitchen2", label="betty_catch1")
    $ add_hook("before_open", "ep24_quests_betty1", scene="street_house_main_yard", label="betty_catch1")
    return

label ep24_quests_bardie11:
    # Добавление Барди прогресса за подглядывание во время уборки
    $ add_char_progress("Bardie", bardieCleaningUpskirtTry4, "cleaning_upskirt_day " + str(day))
    return False

label ep24_quests_bardie12:
    # Убавление прогресса Барди за неправильные трусики
    $ add_char_progress("Bardie", bardieCleaningUpskirtTry4_wrong_panties, "cleaning_upskirt_wrong_panties_day " + str(day))
    return False

label ep24_quests_bardie13:
    # Регулярный разговор с Барди на floor2
    if act=="l":
        return
    $ menuName = "floor2_bardie_dialogue_regular_menu"
    menu:
        "Уйти.":
            return False
        "":
            pass
    return False
label ep24_quests_bardie14:
    # Регулярный разговор с Барди в спальне хозяев
    $ menuName = "bedroom1_bardie_dialogue_regular_menu"
    menu:
        "Уйти.":
            return False
        "":
            pass
    return False

label ep24_quests_bardie15:
    # Проверка на наказание Моники за то что носит трусики (вызывается в конце уборки)
    if bardieMonicaNonNudeCount < bardieCleaningNonNudeDuringPunishment:
        return
    $ bardieMonicaNonNudeCount = 0
    call ep24_dialogues4_bardie3() from _call_ep24_dialogues4_bardie3
    call ep24_dialogues4_bardie4() from _call_ep24_dialogues4_bardie4

    $ questHelp("house_16b", True)
    $ questHelpDesc("house_desc11", False)

    if _return != False:
        $ basement_bedroom2_MonicaSuffix = 2
        call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_212
    return False
