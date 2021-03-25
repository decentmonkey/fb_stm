default ep210_quests_load_init_flag = False

label ep210_quests_load_init:
    if ep210_quests_load_init_flag == False:
        call question_helper_disable() from _call_question_helper_disable_4
        call ep210_quests_bardie_init() from _call_ep210_quests_bardie_init_1
        $ add_hook("change_time_day", "ep210_quest_everyday_check", scene="global", label="ep210_quest_everyday_check")
        $ ep210_quests_load_init_flag = True
    return

label ep210_quest_everyday_check:
    return
