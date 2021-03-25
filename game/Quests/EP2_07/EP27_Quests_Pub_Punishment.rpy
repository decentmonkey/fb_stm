default pubMonicaWaitressTipsPunishmentJoeStage = 0
default pubMonicaWaitressTipsPunishmentAshleyStage = 0

label ep22_quests_pub_punishment_joe:
    music2 stop
    call ep27_dialogues7_pub9() from _call_ep27_dialogues7_pub9
    if _return == False:
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_13
        return False
    music stop
    img black_screen
    with diss
    img scene_Pub_BackRoom1
    with fadelong
    call ep27_dialogues7_pub9a() from _call_ep27_dialogues7_pub9a
    $ sceneIdx = _return
    music stop
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_26
    img black_screen
    with Dissolve(1)
    $ questHelpDesc("shinyhole_desc5")
    if sceneIdx == 1:
        call ep27_dialogues7_pub10() from _call_ep27_dialogues7_pub10
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_355
            return False
        $ pubMonicaWaitressTipsPunishmentJoeStage = 1
        $ questHelp("shinyhole_8", True)
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress1")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive
        call ep27_dialogues7_pub14() from _call_ep27_dialogues7_pub14
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_14
        return
    if sceneIdx == 2:
        call ep27_dialogues7_pub11() from _call_ep27_dialogues7_pub11
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_356
            return False
        $ questHelp("shinyhole_8a", True)
        $ pubMonicaWaitressTipsPunishmentJoeStage = 2
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress2")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_1
        call ep27_dialogues7_pub14() from _call_ep27_dialogues7_pub14_1
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_15
        return
    if sceneIdx == 3:
        call ep27_dialogues7_pub12() from _call_ep27_dialogues7_pub12
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_357
            return False
        $ questHelp("shinyhole_8b", True)
        $ pubMonicaWaitressTipsPunishmentJoeStage = 3
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress3")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_2
        call ep27_dialogues7_pub14() from _call_ep27_dialogues7_pub14_2
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_16
        return
    if sceneIdx == 4:
        call ep27_dialogues7_pub13() from _call_ep27_dialogues7_pub13
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_358
            return False
        $ questHelp("shinyhole_8c", True)
        $ pubMonicaWaitressTipsPunishmentJoeStage = 4
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress4")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_3
        call ep27_dialogues7_pub14() from _call_ep27_dialogues7_pub14_3
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_17
        return
    return

label ep22_quests_pub_punishment_joe1:
    return

label ep22_quests_pub_punishment_ashley:
    music2 stop
    call ep27_dialogues7_pub14a() from _call_ep27_dialogues7_pub14a
    if _return == False:
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_18
        return False
    music stop
    img black_screen
    with diss
    img scene_Pub_BackRoom1
    with fadelong
    call ep27_dialogues7_pub14b() from _call_ep27_dialogues7_pub14b
    $ sceneIdx = _return
    music stop
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_27
    img black_screen
    with Dissolve(1)
    $ questHelpDesc("shinyhole_desc6")
    if sceneIdx == 1:
        call ep27_dialogues7_pub15() from _call_ep27_dialogues7_pub15
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_359
            return False
        $ questHelp("shinyhole_7", True)
        $ pubMonicaWaitressTipsPunishmentAshleyStage = 1
        $ add_char_progress("Bartender_Waitress", monicaTipsPunishmentAshleyProgress, "monicaTipsPunishmentAshleyProgress1")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_4
        call ep27_dialogues7_pub18() from _call_ep27_dialogues7_pub18
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_19
        return
    if sceneIdx == 2:
        call ep27_dialogues7_pub16() from _call_ep27_dialogues7_pub16
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_360
            return False
        $ questHelp("shinyhole_7a", True)
        $ pubMonicaWaitressTipsPunishmentAshleyStage = 2
        $ add_char_progress("Bartender_Waitress", monicaTipsPunishmentAshleyProgress, "monicaTipsPunishmentAshleyProgress2")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_5
        call ep27_dialogues7_pub18() from _call_ep27_dialogues7_pub18_1
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_20
        return
    if sceneIdx == 3:
        call ep27_dialogues7_pub17() from _call_ep27_dialogues7_pub17
        if _return == False:
            call change_scene("hostel_street", "Fade_long") from _call_change_scene_361
            return False
        $ questHelp("shinyhole_7b", True)
        $ pubMonicaWaitressTipsPunishmentAshleyStage = 3
        $ add_char_progress("Bartender_Waitress", monicaTipsPunishmentAshleyProgress, "monicaTipsPunishmentAshleyProgress3")
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_6
        call ep27_dialogues7_pub18() from _call_ep27_dialogues7_pub18_2
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_21
        return
    return

label ep22_quests_pub_punishment_ashley1:
    return
