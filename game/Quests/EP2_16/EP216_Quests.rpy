default ep216_quests_load_init_flag = False

label ep216_quests_load_init:
    if ep216_quests_load_init_flag == False:
        $ ep216_quests_load_init_flag = True
        if char_info["Biff"]["level"] <= 3:
            $ char_info["Biff"]["enabled"] = True
            if char_info["Biff"]["level"] == 3:
                $ char_info["Biff"]["caption"] = t_("Цыпочке надо развлекать папочку, чтобы он продолжал давать ей работу.")

    return
