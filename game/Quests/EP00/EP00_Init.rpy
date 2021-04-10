default ep00_check_game_end_flag = False

label ep00_init1:
    python:
        questHelpRemove("house_3")
        questHelpRemove("house_5")
        questHelpRemove("house_6")
        questHelpRemove("house_7")
        questHelpRemove("house_8")
        questHelpRemove("house_9")
        questHelpRemove("house_11")
        questHelpRemove("house_12")
        questHelpRemove("house_13")
        questHelpRemove("house_16")
        questHelpRemove("house_16b")
        questHelpRemove("house_17")
        questHelpRemove("house_18")
        questHelpRemove("house_19")
        questHelpRemove("house_20")
        questHelpRemove("house_21")
        questHelpRemove("house_22")
        questHelpRemove("house_23")
        questHelpRemove("house_24")
        questHelpRemove("house_25")
        questHelpRemove("house_26")
        questHelpRemove("house_27")
        questHelpRemove("house_27a")
        questHelpRemove("house_28")
        questHelpRemove("house_29")
        questHelpRemove("house_30")
        questHelpRemove("house_34")
        questHelpRemove("house_37")
        questHelpRemove("house_41")
        questHelpRemove("college_1")
        questHelpRemove("college_2")
        questHelpRemove("college_3")
        questHelpRemove("college_4")
        questHelpRemove("college_5")
        questHelpRemove("college_6")
        questHelpRemove("college_7")
        questHelpRemove("college_8")
        bardieCensored = True

    return

label ep00_check_game_end:
    if ep00_check_game_end_flag == True:
        return
    if questHelpGetQuestsAmount() == 0:
        music Continue_Life
        scene black_screen
        with Dissolve(1)
        call textonblack_long("FASHION BUSINESS")
        scene black_screen
        $ steam_achievement("ach67")
        if monica_cheats_iteration_count == 0:
            $ steam_achievement("ach64")
        else:
            $ steam_achievement("ach65")

        help "Вы прошли все существующие квесты в данной версии игры."
        help "Вы можете жить дальше в этом мире, либо продолжить в следующей версии игры!"
        scene black_screen
        with fadelong
        pause 3.0
        $ ep00_check_game_end_flag = True

    return
