default ep212_quests_photoshoot8_after_init_completed = False
default ep212_quests_photoshoot8_after_completed_day = 0

# Коллектив смотрит на обложку журнала с королевой сердец
label ep212_quests_photoshoot8_after_init:
    if ep212_quests_photoshoot8_after_init_completed == True:
        return
    $ add_hook("before_open", "ep212_quests_photoshoot8_after_check", scene="working_office", label="ep212_quests_photoshoot8_after")
    $ add_hook("before_open", "ep212_quests_photoshoot8_after_check", scene="working_office_cabinet", label="ep212_quests_photoshoot8_after")
    $ ep212_quests_photoshoot8_after_init_completed = True
    return

label ep212_quests_photoshoot8_after_check:
    if day - ep211_quests_photoshot8_opened_day < 2 or week_day == 7 or day_time != "day":
        return
    $ remove_hook(label="ep212_quests_photoshoot8_after")
    call ep212_dialogues6_melanie_punishment_10() from _rcall_ep212_dialogues6_melanie_punishment_10
    $ questHelp("office_45a", True)
    $ ep212_quests_photoshoot8_after_completed_day = day
    call change_scene("working_office") from _rcall_change_scene_87
    return False
