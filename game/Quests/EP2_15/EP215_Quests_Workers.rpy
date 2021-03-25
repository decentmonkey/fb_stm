default ep212_quests_photoshoot9_after_init_completed = False
default ep212_quests_photoshoot9_after_init_planned = False
label ep215_quests_workers1_init: # сотрудники после съемки в журнале
    if ep212_quests_photoshoot8_after_init_completed == False:
        return
    if ep212_quests_photoshoot9_after_init_completed == True:
        return
    $ ep212_quests_photoshoot9_after_init_planned = True
    $ add_hook("before_open", "ep215_quests_workers1_after_check", scene="working_office", label="ep215_quests_workers1_after_check")
    $ add_hook("before_open", "ep215_quests_workers1_after_check", scene="working_office_cabinet", label="ep215_quests_workers1_after_check")
    $ ep212_quests_photoshoot9_after_init_completed = True
    return

label ep215_quests_workers1_after_check:
    if day - ep213_presentation2_completed_day < 3 or week_day == 7 or day_time != "day":
        return
    $ remove_hook(label="ep215_quests_workers1_after_check")
    $ ep212_quests_photoshoot9_after_init_planned = False
    call ep215_dialogues4_julia_3() from _rcall_ep215_dialogues4_julia_3
    $ questHelp("office_45b", True)
    call change_scene("working_office") from _rcall_change_scene_175
    return
