default ep211_quests_pub_started_stole_tips = False
default monicaPubDanceStoleTipsActive = False
default monicaPubDanceStoleTipsDay = 0
default monicaPubDanceStoleTipsStage = 0
default monicaPubDanceStoleTipsBankerCompleted = False
default monicaPubDanceStoleTipsBankerPlanned = False

default monicaPubMollyNeedForgive1 = False
default monicaPubFiredTips1 = False

#default ep211_quests_pub_dialogue1_planned = False

label ep211_quests_pub1:
    # запускаем возможность украсть чаевые после танцев
    $ ep211_quests_pub_started_stole_tips = True
    $ monicaPubDanceStoleTipsActive = True
    $ add_hook("enter_scene", "ep211_dialogues5_shiny_hole_5", scene="pub", label="pub_stole_dance_tips_comment", once=True)

    return

label ep211_quests_pub2_exit_with_tips: #уход с чаевыми (попытка)
    if monicaPubDanceStoleTipsStage == 0:
        $ monicaPubDanceStoleTipsDay = day
        $ add_hook("enter_scene", "ep211_quests_pub2_exit_with_tips_comment_nextday", scene="pub", label="pub_stole_dance_tips_comment")
        $ add_hook("Teleport_Hostel_Pub", "dialogue_5_dance_strip_4m", scene="hostel_street", label="evening_time_temp")
        $ monicaPubDanceStoleTipsBankerPlanned = True
        return
    return

label ep211_quests_pub2_exit_with_tips_comment_nextday:
    if day == monicaPubDanceStoleTipsDay:
        return
    $ remove_hook()
    call ep211_dialogues5_shiny_hole_6() from _rcall_ep211_dialogues5_shiny_hole_6
    return

label ep211_quests_pub3_fired: # увольнение из паба
    $ monicaPubFiredTips1 = True
    music2 stop
    $ autorun_to_object("ep211_dialogues5_shiny_hole_7", scene="hostel_street")
    $ add_hook("Teleport_Hostel_Pub", "ep211_dialogues5_shiny_hole_7", scene="hostel_street", label="monica_pub_fired_block", priority = 10001)
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    $ questLog(69, True)
    $ questLog(66, False)
    $ questLog(52, False)
    $ questLog(48, False)
    $ questLog(49, False)
    $ questLog(50, False)
    $ questLog(51, False)
    $ questLog(53, False)
    $ questLog(57, False)
    $ questLog(60, False)
    $ questLog(58, False)
    $ questLog(59, False)
    $ questLog(75, False)
    $ questsFailByCategory(t_("SHINY HOLE"))
    $ questHelpDesc("shinyhole_desc1", False)
    $ questHelpDesc("shinyhole_desc2", False)
    $ questHelpDesc("shinyhole_desc3", False)
    $ questHelpDesc("shinyhole_desc4", False)
    $ questHelpDesc("shinyhole_desc5", False)
    $ questHelpDesc("shinyhole_desc6", False)
    $ questHelpDesc("shinyhole_desc7", False)
    $ questHelpDesc("shinyhole_desc8", False)
    $ questHelpDesc("shinyhole_desc9", False)
    $ questHelpDesc("shinyhole_desc10", False)
    $ questHelpDesc("shinyhole_desc10a", False)
    $ questHelpDesc("shinyhole_desc10b", False)
    $ questHelpDesc("shinyhole_desc11", False)
    $ questHelpDesc("shinyhole_desc12", False)
    $ questHelpDesc("shinyhole_desc12a", False)
    $ questHelpDesc("shinyhole_desc13", False)
    $ questHelpDesc("shinyhole_desc14", False)
    $ questHelpDesc("shinyhole_desc15", False)
    $ questHelpDesc("shinyhole_desc16", False)
    $ questHelpDesc("shinyhole_desc17", False)
    $ questHelpDesc("shinyhole_desc18", False)
    $ questHelpDesc("shinyhole_desc19", True)
    $ clear_hooks("exit_scene", scene="pub")
    $ clear_hooks("exit_scene", scene="pub_makeuproom")
    call change_scene("hostel_street", "Fade_long") from _rcall_change_scene_3
    return

label ep211_quests_pub3_start_banker_quest:
    $ remove_hook(label="dialogue_5_dance_strip_18")
    $ add_hook("enter_scene", "ep211_quests_pub3_start_banker_questb", scene="pub_makeuproom", label="ep211_quests_pub3_start_banker_questb")
    return

label ep211_quests_pub3_start_banker_questb:
    $ monicaPubDanceStoleTipsBankerPlanned = False
    $ remove_hook()
    call ep211_dialogues5_shiny_hole_1() from _rcall_ep211_dialogues5_shiny_hole_1
    if _return == False:
        $ questHelp("shinyhole_28", False)
        call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired
        return False

    $ questHelp("shinyhole_28", True)
    $ questHelp("shinyhole_29", skipIfExists=True)

    $ add_objective("go_dance_private", t_("Идти в подсобку барменов и станцевать приват."), c_orange, 105)
    $ add_hook("Teleport_Pub", "ep211_quests_pub4_teleport", scene="pub_makeuproom", label="pub_private_dance1", priority = 10001)
    call refresh_scene_fade() from _rcall_refresh_scene_fade_1
    return

label ep211_quests_pub4_teleport:
    if cloth_type != "StripOutfit":
        call ep211_dialogues5_shiny_hole_8() from _rcall_ep211_dialogues5_shiny_hole_8
        return False
    # сцена
    $ remove_objective("go_dance_private")
    call ep211_dialogues5_shiny_hole_2() from _rcall_ep211_dialogues5_shiny_hole_2
    if _return == False:
        $ questHelp("shinyhole_29", False)
        call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_1
        return False
    $ questHelp("shinyhole_29", True)
    $ questHelp("shinyhole_30", skipIfExists=True)
    $ questHelp("shinyhole_33", skipIfExists=True)
    $ monicaPubDanceStoleTipsBankerCompleted = True
    $ monicaPubDanceStoleTipsStage = 1
#    $ ep211_quests_pub_dialogue1_planned = True
    $ autorun_to_object("ep211_dialogues5_shiny_hole_9", scene="pub_makeuproom")
    $ remove_hook(label="pub_private_dance1")
    $ add_hook("Teleport_Pub", "ep211_quests_pub5", scene="pub_makeuproom", label="pub_private_dance1")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long
    return False

label ep211_quests_pub5: # Диалог о том что Моника должна просить прощения у Молли
    if cloth == "StripOutfit" or ep29_quests_dancing_with_claire_last_day <= 0:
        return
    $ remove_hook(label="pub_private_dance1")
    call ep211_dialogues5_shiny_hole_3() from _rcall_ep211_dialogues5_shiny_hole_3
    $ questHelp("shinyhole_30", True)
    $ questHelp("shinyhole_31", skipIfExists=True)
    if game.extra == False:
        $ questHelp("shinyhole_31", False, skipIfTrue=True)

    $ questHelpDesc("shinyhole_desc11", "shinyhole_desc12")
    $ questLog(70, True)
    $ add_hook("before_open", "ep211_quests_pub6", scene="pub_makeuproom", label="monica_pub_molly_forgive_dialogue_comment")
    $ add_hook("Pub_StripteaseGirl1", "ep211_quests_pub7_molly", scene="pub_makeuproom", label="monica_pub_molly_forgive_dialogue")
    $ monicaPubMollyNeedForgive1 = True
    return

label ep211_quests_pub6:
    if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") != False:
        $ remove_hook()
        call ep211_dialogues5_shiny_hole_4() from _rcall_ep211_dialogues5_shiny_hole_4
    return

label ep211_quests_pub7_molly:
    if act=="l":
        return
    call ep211_dialogues5_shiny_hole_4b() from _rcall_ep211_dialogues5_shiny_hole_4b
    return False
