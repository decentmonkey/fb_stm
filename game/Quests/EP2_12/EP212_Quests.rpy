default ep212_quests_load_init_flag = False

label ep212_quests_load_init:
    if ep212_quests_load_init_flag == False:
        if monica_college_stage == 3:
            call ep212_quests_bardie_ralph1() from _rcall_ep212_quests_bardie_ralph1_1
        $ ep212_quests_load_init_flag = True
        if ep211_julia_second_date_completed == True:
            $ add_hook("before_open", "ep212_quests_julia2_fred_catch", scene="working_office", label="ep212_quests_julia2_fred_catch", priority=1000)
            $ add_hook("before_open", "ep212_quests_julia2_fred_catch", scene="working_office_cabinet", label="ep212_quests_julia2_fred_catch", priority=1000)
        if monicaOutfitsEnabled[8] == True and ep211_quests_photoshot8_opened_day == 0:
            $ ep211_quests_photoshot8_opened_day = day
            call ep212_quests_photoshoot8_after_init() from _rcall_ep212_quests_photoshoot8_after_init_1
        if pubInited == True:
            $ add_hook("enter_scene", "ep212_quests_pub_reset_pub", scene="pub", once=True, priority = 10000, label="pub_reset")


    return
