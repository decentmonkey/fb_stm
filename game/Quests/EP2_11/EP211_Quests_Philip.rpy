label ep211_quests_philip:
    call ep211_dialogues7_Phillip_home_1() from _rcall_ep211_dialogues7_Phillip_home_1
    call ep211_dialogues7_Phillip_home_2() from _rcall_ep211_dialogues7_Phillip_home_2
    if _return == 1: #double blowjob
        call ep211_dialogues7_Phillip_home_3() from _rcall_ep211_dialogues7_Phillip_home_3
        if _return == False:
            # убегает
            $ move_object("Bitch1", "empty")
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_18", scene="street_philiphome")
            call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_1
            return False
        $ questHelp("philip_6", True)
        $ questHelp("philip_7", skipIfExists=True)
        call ep211_dialogues7_Phillip_home_4() from _rcall_ep211_dialogues7_Phillip_home_4
        $ monica_philip_visits_double_blowjobs += 1
        $ move_object("Bitch1", "empty")
        $ autorun_to_object("ep211_dialogues7_Phillip_home_5", scene="street_philiphome")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_2
        return False

    if _return == 2: #threesome
        call ep212_dialogues4_philip_threesome_1() from _rcall_ep212_dialogues4_philip_threesome_1 # сцена
        if _return == False:
            # убегает
            $ move_object("Bitch1", "empty")
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_18", scene="street_philiphome")
            call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_8
            return False

        call ep212_dialogues4_philip_threesome_2() from _rcall_ep212_dialogues4_philip_threesome_2 # оплата шлюхе 1
        $ questHelp("philip_7", True)
        $ monica_philip_visits_threesomes += 1
        $ streetPhilipHomeMonicaSuffix = 2
        $ move_object("Bitch1", "street_philiphome")
        $ add_hook("Bitch1", "ep212_quests_philip_threesome1", scene="street_philiphome", label="ep210_quests_escort1_philip5_bitch1_street")
        $ add_hook("exit_scene", "ep210_quests_escort1_philip5_bitch1_street_leave", scene="street_philiphome", label="ep210_quests_escort1_philip5_bitch1_street")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_9

    return

label ep212_quests_philip_threesome1: # разговор со шлюхой на улице
    if act=="l":
        return
    $ remove_hook()
    call ep212_dialogues4_philip_threesome_3() from _rcall_ep212_dialogues4_philip_threesome_3
    $ move_object("Bitch1", "empty")
    $ autorun_to_object("ep211_dialogues7_Phillip_home_5", scene="street_philiphome")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_10
    return False
