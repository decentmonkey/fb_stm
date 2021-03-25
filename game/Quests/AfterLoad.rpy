label process_afterload:
    call questHelp_init() from _rcall_questHelp_init

    if monicaWorkingAtBiffOffice == False and monicaOutfitsEnabled[6] == True:
        $ remove_hook(label="biff_work_dialogue1")
        $ ep26_quests_biff1_Flag = False
        call ep26_quests_biff1() from _call_ep26_quests_biff1_1

    call ep28_quests() from _call_ep28_quests
    call ep29_quests_init() from _rcall_ep29_quests_init
    call ep29_revenge_quest1_init() from _rcall_ep29_revenge_quest1_init
    call monica_cheats_init() from _rcall_monica_cheats_init
    call ep210_quests_load_init() from _rcall_ep210_quests_load_init
    call ep211_quests_load_init() from _rcall_ep211_quests_load_init
    call ep212_quests_load_init() from _rcall_ep212_quests_load_init
    call ep213_quests_load_init() from _rcall_ep213_quests_load_init
    call ep214_quests_load_init() from _rcall_ep214_quests_load_init
    call ep215_quests_load_init() from _rcall_ep215_quests_load_init
    call ep216_quests_load_init() from _rcall_ep216_quests_load_init

    if bardieCensored == False:
        call ep00_init1()
    return
