default ep210_revenge_quest2_box_blocked_fred = False

label ep210_revenge_quest2:
    $ map_enabled = False
    $ miniMapEnabledOnly = ["Basement"]
    $ day_time = "evening"
    $ day_suffix = "_Evening"

    # Инициализируем перемещение днем
    $ add_hook("Teleport_Basement_Hole", "ep210_revenge_quest3_teleport_yard", scene="basement_bedroom1", label="ep210_revenge_quest3_teleport")
    $ add_hook("Teleport_House", "ep210_revenge_quest3_teleport_bedroom", scene="street_house_main_yard", label="ep210_revenge_quest3_teleport")
    $ add_hook("Teleport_Fence", "ep210_dialogues6_gun_monica_fred_1c_false", scene="street_house_main_yard", label="ep210_revenge_quest3_block")
    $ add_hook("Teleport_Gate", "ep210_dialogues6_gun_monica_fred_1c_false", scene="street_house_main_yard", label="ep210_revenge_quest3_block")
    $ add_hook("Box", "ep210_dialogues6_gun_monica_fred_1c_false", scene="basement_bedroom_table", label="ep210_revenge_quest3_block")
    $ add_hook("Driver", "ep210_revenge_quest3_fred", scene="street_house_main_yard", label="ep210_revenge_quest3_fred")

    # Ограничиваем вечером
    $ add_hook("Teleport_Basement_Hole", "ep210_revenge_quest2_block_exit_evening", scene="basement_bedroom1", label="evening_time_temp")
    $ add_hook("Box", "ep210_revenge_quest2_block_exit_evening", scene="basement_bedroom_table", label="evening_time_temp")
    $ add_hook("change_time_day", "ep210_revenge_quest2_block_daytime_hooks", scene="global", priority = 100000, label="ep210_revenge_quest2_block_daytime_hooks")
    $ add_hook("change_time_day", "ep210_revenge_quest3_morning_comment", scene="global", priority = 100000, label="ep210_revenge_quest2_block_daytime_hooks")
    $ add_hook("change_time_evening", "ep210_revenge_quest2_block_daytime_hooks", scene="global", priority = 100000, label="ep210_revenge_quest2_block_daytime_hooks")
    $ add_hook("basement_monica_after_sleep", "ep210_revenge_quest2_block_daytime_hooks", scene="global", priority = 100000, label="ep210_revenge_quest2_block_daytime_hooks")
    $ add_hook("basement_monica_after_sleep_dialogue", "ep210_revenge_quest2_block_daytime_hooks", scene="global", priority = 100000, label="ep210_revenge_quest2_block_daytime_hooks")

    $ questLogDataEnabled = {}
    $ objectives_list = []
    $ ep210_revenge_quest2_box_blocked_fred = True
    $ monica_eated()
    $ scenes_data["hooks"]["global"]["basement_monica_before_sleep"] = []

    $ autorun_to_object("ep210_dialogues6_gun_monica_fred_1a", scene="basement_bedroom2")
    call change_scene("basement_bedroom2") from _call_change_scene_501

    return

label ep210_revenge_quest2_block_daytime_hooks: # Блокируем события смены дня
    return False

label ep210_revenge_quest2_block_exit_evening: # Не даем выйти из спальни
    call ep210_dialogues6_gun_monica_fred_1a() from _call_ep210_dialogues6_gun_monica_fred_1a
    return False

label ep210_revenge_quest3_morning_comment:
    $ remove_hook()
    call ep210_dialogues6_gun_monica_fred_1b() from _call_ep210_dialogues6_gun_monica_fred_1b

    $ questHelp("revenge_3a", True)
    $ questHelp("revenge_4")
    $ questHelpDesc("revenge_desc1")

    $ add_hook("BasementBed", "ep210_dialogues6_gun_monica_fred_1c_false", scene="basement_bedroom2", label="ep210_revenge_quest3_block")
    $ miniMapEnabledOnly = ["Basement", "Street_Yard"]
    $ move_object("Driver", "street_house_main_yard")
    $ move_object("Bardie", "empty")
    $ move_object("Betty", "empty")
    $ questLog(65, True)
    $ add_objective("find_fred", t_("Идти к Фреду"), c_red, 105)
    $ autorun_to_object("ep210_dialogues6_gun_monica_fred_1c", scene="bedroom2")
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_42
    return False

label ep210_revenge_quest3_teleport_yard:
    call change_scene("street_house_main_yard", "Fade_long") from _call_change_scene_502
    return False

label ep210_revenge_quest3_teleport_bedroom:
    call change_scene("basement_bedroom2", "Fade_long") from _call_change_scene_503
    return False

label ep210_revenge_quest3_fred: # Диалог с Фредом
    if act=="l":
        call ep210_dialogues6_gun_monica_fred_1d() from _call_ep210_dialogues6_gun_monica_fred_1d
        $ questHelp("revenge_4", True)
        $ questHelp("revenge_5")
        return False
    if cloth != "Governess":
        call change_scene("basement_bedroom1", "Fade_long", False) from _call_change_scene_504
        call wardrobePutGovernessWithoutPanties() from _call_wardrobePutGovernessWithoutPanties_3
        return False

    call ep210_dialogues6_gun_monica_fred_1d() from _call_ep210_dialogues6_gun_monica_fred_1d_1
    $ questHelp("revenge_4", True)
    $ questHelp("revenge_5")
    jump ep211_revenge_quest1
#    return
