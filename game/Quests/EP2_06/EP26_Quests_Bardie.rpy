default ep26_quests_bardie_day1 = 0
default monicaShowedBoobsToBardie = False
default monicaMadeTitjobBardie = False

default ep26_quests_bardie6_stage = 0

default bettyMustFeedMonicaOnKitchenBoobs = False

label ep26_quests_bardie1:
    # Инициализация квестов 0.6
    if monicaCleaningInProgressEngineWorkingFlag == True: # Если идет уборка, вешаем эту функцию на событие после окончания уборки
        $ add_hook("monica_cleaning_end", "ep26_quests_bardie1", scene="global")
        return

    # Барди шантажирует Бетти. Может быть я могу использовать это?
    $ questHelp("house_17", skipIfExists=True)
    $ questLog(44, True)
    $ add_hook("Bardie_Life_day", "Bardie_Life_Day6", scene="global", label="bardie_day_street_yard") # Барди днем все время во дворе
    $ add_hook("before_open", "ep26_quests_bardie2", scene="bedroom_bardie") # Разговор с Барди в комнате
    $ add_hook("Bardie", "ep26_quests_bardie2b", scene="bedroom_bardie", label="ep26_bardie_pre_dialogue1")
    return

label ep26_quests_bardie1a:
    $ remove_hook()
    call ep26_quests_bardie1() from _call_ep26_quests_bardie1_2
    return

label ep26_quests_bardie2:
    # Первый разговор с Барди по поводу еды в доме, Барди дрочит
    if day_time == "day":
        return
    if cloth != "Governess":
        $ autorun_to_object("ep26_quests_bardie2a", scene="bedroom_bardie")
        return
    $ remove_hook()
    $ remove_hook(label="ep26_bardie_pre_dialogue1")
    call ep26_dialogues1_bardie1() from _call_ep26_dialogues1_bardie1
    $ autorun_to_object("ep26_dialogues1_bardie1a", scene="floor2")
    $ add_hook("Bardie", "ep26_quests_bardie3", scene="bedroom_bardie")
    call change_scene("floor2") from _call_change_scene_344
    return

label ep26_quests_bardie2a:
    mt "Мне лучше переодеться сначала."
#    mt "В таком виде Барди от меня точно попросит чего-нибудь неприличного..."
    return

label ep26_quests_bardie2b:
    call ep26_quests_bardie2a() from _call_ep26_quests_bardie2a
    return False

label ep26_quests_bardie3:
    # Моника заходит к Барди второй раз. После того как увидела что он дрочит.
    if cloth != "Governess":
        call ep26_quests_bardie2a() from _call_ep26_quests_bardie2a_1
        return False
    call ep26_dialogues1_bardie2() from _call_ep26_dialogues1_bardie2
    if _return == 0: # Моника ушла вначале
        $ autorun_to_object("ep26_dialogues1_bardie3a", scene="floor2")
        call change_scene("floor2") from _call_change_scene_345
        return False
    if _return == 1 or _return == 2: # Наказание
        call ep24_dialogues4_bardie4() from _call_ep24_dialogues4_bardie4_1
        if _return != False:
            $ basement_bedroom2_MonicaSuffix = 2
            call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_346
        return False
    if _return == 3:
        $ autorun_to_object("ep26_dialogues1_bardie3", scene="floor2")
        call change_scene("floor2") from _call_change_scene_347
        $ remove_hook("Bardie", "ep26_quests_bardie3", scene="bedroom_bardie")
        $ add_hook("Bardie", "ep26_quests_bardie4", scene="bedroom_bardie", label="ep26_bardie_dialogue3")
        $ ep26_quests_bardie_day1 = day
        $ questHelp("house_17", True)
        $ questHelp("house_18")


    return False

label ep26_quests_bardie4:
    # Моника заходит третий раз и делает titjob
    if ep26_quests_bardie_day1 == day:
        call ep26_dialogues1_bardie3() from _call_ep26_dialogues1_bardie3
        return False
    if cloth != "Governess":
        call ep26_quests_bardie2a() from _call_ep26_quests_bardie2a_2
        return False
    call ep26_dialogues1_bardie4() from _call_ep26_dialogues1_bardie4
    if _return == 0 or _return == 1: # Просто ушла вначале
        call change_scene("floor2", "Fade_long") from _call_change_scene_348
        return False
    if _return == 2: # Все завершено
        $ move_object("Bardie", "empty")
        call change_scene("floor2", "Fade_long", "snd_runaway") from _call_change_scene_349
        $ remove_hook(label="ep26_bardie_dialogue3")
        $ add_hook("Bardie", "ep26_quests_bardie5", scene="bedroom_bardie", label="ep26_bardie_dialogue4")
        $ questHelp("house_18", True)
        $ questHelp("house_19")
        return False


    return False

label ep26_quests_bardie5:
    # Моника заходит четвертый раз и узнает какое условие питания в доме
    if cloth != "Governess":
        call ep26_quests_bardie2a() from _call_ep26_quests_bardie2a_3
        return False
    call ep26_dialogues1_bardie5() from _call_ep26_dialogues1_bardie5
    if _return == 1: # Наказание
        call ep24_dialogues4_bardie4() from _call_ep24_dialogues4_bardie4_2
        if _return != False:
            $ basement_bedroom2_MonicaSuffix = 2
            call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_350
        return False

    if _return == 2: # Все ок, инициализируем Бетти
        $ questLog(44, False)
        $ remove_hook(label="ep26_bardie_dialogue4")
#        $ add_hook("Bardie", "ep26_quests_bardie6", scene="bedroom_bardie", label="ep26_bardie_dialogue5_betty_kitchen")
        $ add_hook("open", "ep26_quests_bardie6", scene="bedroom_bardie", label="ep26_bardie_dialogue5_betty_kitchen")
        $ bettyMustFeedMonicaOnKitchenBoobs = True
        $ autorun_to_object("ep26_dialogues1_bardie5a", scene="floor2")
        call ep26_quests_betty1() from _call_ep26_quests_betty1 # Инициализация питания на кухне
        call change_scene("floor2", "Fade_long") from _call_change_scene_351
        $ questHelp("house_19", True)
        $ questHelp("house_20")
        $ questHelp("house_21")
        return False
    return False

label ep26_quests_bardie6:
    # Приход к Барди из-за Бетти на кухне
    if bettyNotFeedingMonicaKitchen == True:
        if day_time == "day":
            return
        if ep26_quests_bardie6_stage == 0:
            call ep26_dialogues1_bardie9() from _call_ep26_dialogues1_bardie9_1
            $ autorun_to_object("ep26_dialogues1_bardie9a", scene="floor2")
            call change_scene("floor2", "Fade_long") from _call_change_scene_352
            $ ep26_quests_bardie6_stage = 1
            return False
        if ep26_quests_bardie6_stage == 1:
            call ep26_dialogues1_bardie10() from _call_ep26_dialogues1_bardie10
            $ questHelp("house_22", True)
            if _return == 0 or _return == 1: # Моника просто выходит
                $ autorun_to_object("ep26_dialogues1_bardie9a", scene="floor2")
                call change_scene("floor2", "Fade_long") from _call_change_scene_353
                return False
            if _return == 2 or _return == 3: # Барди разрешил дальше питаться в доме
                $ bardieForcedBettyToFeedMonica = True
                $ bettyNotFeedingMonicaKitchen = False
                if _return == 3:
                    $ add_hook("change_time_day", "ep26_quests_bardie8", scene="global", label="day_time_temp") # Планируем наказание Бетти вечером
                    $ questHelpFlag3 = True
                    $ questHelp("house_23", skipIfExists=True)
                call change_scene("floor2", "Fade_long") from _call_change_scene_354
                return False
    return

label ep26_quests_bardie7:
    # Бетти уходит к Барди
    call ep26_dialogues1_bardie11() from _call_ep26_dialogues1_bardie11
    $ move_object("Betty", "empty")
    $ add_hook("open", "ep26_quests_bardie9", scene="bedroom_bardie", label="evening_time_temp", priority = 200) # Наказание Бетти
    $ remove_objective("call_betty")
    if questHelpFlag3 == True:
        $ questHelpFlag3 = False
        $ questHelp("house_21", True)
        $ questHelp("house_23", True)
    call refresh_scene_fade() from _call_refresh_scene_fade_155
    return

label ep26_quests_bardie8:
    # Наказание Бетти протухает с утра
    if questHelpFlag3 == True:
        $ questHelpFlag3 = False
        $ questHelp("house_23", False)
    $ bardieCalledBettyForPunishment = False
    $ remove_objective("call_betty")
    return

label ep26_quests_bardie9:
    # Сцена наказания Бетти
    $ remove_hook()
    call ep26_dialogues1_bardie12() from _call_ep26_dialogues1_bardie12
    call refresh_scene_fade() from _call_refresh_scene_fade_156
#    call change_scene("floor2", "Fade_long")
    return False







#
