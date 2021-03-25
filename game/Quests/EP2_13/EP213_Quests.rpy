default ep213_quests_load_init_flag = False

label ep213_quests_load_init:
    if ep213_quests_load_init_flag == False:
        $ ep213_quests_load_init_flag = True
        if ep212_quests_melanie_completed == True:
            call ep213_quests_victoria1_init() from _rcall_ep213_quests_victoria1_init_1
