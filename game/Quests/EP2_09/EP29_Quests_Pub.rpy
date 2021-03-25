default ep29_quests_pub_forgiveness_dancing_enabled = True
default ep29_quests_pub_forgiveness_dancing_quest_in_progress = False
default ep29_quests_pub_forgiveness_dancing_stage = 0
default ep29_quests_pub_monica_knows_claire = False
default ep29_quests_pub_monica_knows_molly = False
default ep29_quests_pub_block_money_return = False
default monica_strip_forgiveness_money_left = 500
default pubMakeupRoomGirlsRandomSuffix = False
default ep29_quests_claire_talk_last_day = 0
default ep29_quests_joe_catched_monica_claire = False
default ep29_quests_monica_gave_money_forgivenes_last_day = 0
default ep29_quests_only_claire = False
label ep29_quests_pub1_dance_agree:
    # Моника согласилась отрабатывать танцами (из меню)
    call dialogue_5_dance_strip_1() from _call_dialogue_5_dance_strip_1 # Моника мнется
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_212
        return

    $ questsFailByCategory(t_("SHINY HOLE"))
    $ questHelp("shinyhole_9", True)
    $ questHelp("shinyhole_10")
    $ questHelpDesc("shinyhole_desc1", False)
    $ questHelpDesc("shinyhole_desc2", False)
    $ questHelpDesc("shinyhole_desc3", False)
    $ questHelpDesc("shinyhole_desc4", False)
    $ questHelpDesc("shinyhole_desc5", False)
    $ questHelpDesc("shinyhole_desc6", False)
    $ questHelpDesc("shinyhole_desc7")
    $ monica_strip_forgiveness_money_left = 500
    $ add_objective("go_to_makeuproom", t_("Идти в гримерку, чтобы подготовиться к выступлению на сцене."), c_orange, 100)
    $ add_hook("Bartender", "dialogue_5_dance_strip_4na", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ add_hook("Bartender_Waitress", "dialogue_5_dance_strip_4na", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ add_hook("Teleport_Hostel_Street", "ep29_quests_pub1_dance_exit_pub", scene="pub", label="monica_dance_forgiveness_exit", quest="monica_dance_forgiveness")

    $ add_hook("Pub_StripteaseGirl1", "ep29_quests_pub1_day1_molly", scene="pub_makeuproom", label="monica_dance_forgiveness_dialogue")

    $ add_hook("before_open", "dialogue_5_dance_strip_2", scene="pub_makeuproom", once=True, label="monica_dance_block")
    $ add_hook("enter_scene", "pub_dance_scene_return", scene="pub_stage1", label="monica_dance_return_stage", quest="monica_dance_forgiveness")
#    $ autorun_to_object("dialogue_5_dance_strip_4n", scene="pub_stage1")
    $ questLog(57, True) #Мне нужно отработать долг $500, выступая на сцене в пабе.
    $ ep29_quests_pub_forgiveness_dancing_quest_in_progress = True
    $ monicaStartedStripDanceFlag = True
    call pub_ini2() from _call_pub_ini2 # добавляем телепорт в гримерную комнату
    $ set_active("Teleport_Pub_MakeupRoom", True, scene="pub")
    call locations_init_pub_stage() from _call_locations_init_pub_stage # инициализируем локации гримерки и у сцены
    call characters_pub_init2() from _call_characters_pub_init2
    call pub_dance_movegirls_to_makeuproom() from _call_pub_dance_movegirls_to_makeuproom
    call refresh_scene_fade() from _call_refresh_scene_fade_213
    return


label ep29_quests_pub1_dance_exit_pub:
    $ remove_objective("go_to_makeuproom")
    $ remove_hook(label="monica_dance_block")
    $ remove_hook(label="monica_dance_forgiveness")
    $ remove_hook(label="monica_dance_forgiveness_dialogue")
    $ remove_objective("go_dance")
    $ remove_objective("talk_claire")
    $ remove_objective("go_to_makeuproom")
    $ set_active("Teleport_Pub_MakeupRoom", False, scene="pub")
    call pub_dance_movegirls_to_stage() from _call_pub_dance_movegirls_to_stage
    return


label ep29_quests_pub1_begin_dance_quest_check:
    if day_time != "evening":
        return
    if pubDanceGirlsBlockedDay != day:
        if ep29_quests_pub_forgiveness_dancing_stage == 0 and pubMonicaWaitressTipsStolen == True:
            # сегодня работает Молли
            $ move_object("Pub_StripteaseGirl2", "empty")
            $ move_object("Pub_StripteaseGirl1", "pub")
        if ep29_quests_pub_forgiveness_dancing_stage == 1:
            # сегодня работает Клэр
            $ move_object("Pub_StripteaseGirl1", "empty")
            $ move_object("Pub_StripteaseGirl2", "pub")
        if ep29_quests_pub_forgiveness_dancing_stage == 2:
            # сегодня работает Молли
            $ move_object("Pub_StripteaseGirl2", "empty")
            $ move_object("Pub_StripteaseGirl1", "pub")
        if ep29_quests_pub_forgiveness_dancing_stage == 3 or ep29_quests_only_claire == True:
            # сегодня работает Клэр
            $ move_object("Pub_StripteaseGirl1", "empty")
            $ move_object("Pub_StripteaseGirl2", "pub")

        if pubMakeupRoomGirlsRandomSuffix == True:
            $ pub_makeuproom_claire_suffix= rand(1,7)
            $ pub_makeuproom_molly_suffix = rand(1,8)

    return

label ep29_quests_pub1_day1_molly:
    if act=="l":
        return
    $ remove_hook()
    $ remove_objective("go_to_makeuproom")
    call dialogue_5_dance_strip_2a() from _call_dialogue_5_dance_strip_2a
    $ add_objective("ask_ashley_about_cloth", t_("Спросить у Эшли костюм для выступления."), c_blue, 100)
    $ questLog(58,True)
    $ questHelp("shinyhole_10", True)
    $ questHelp("shinyhole_11")
    $ questHelpDesc("shinyhole_desc8")

    $ add_hook("Bartender", "ep29_quests_pub1_day1_joe", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ add_hook("Teleport_Hostel_Street", "dialogue_5_dance_strip_4nb", scene="pub", label="monica_dance_block2")
    $ move_object("Bartender_Waitress", "empty")

    call change_scene("pub", "Fade_long") from _call_change_scene_445
    return False

label ep29_quests_pub1_day1_joe:
    if act=="l":
        return
    $ remove_hook()
    $ remove_objective("ask_ashley_about_cloth")
    call dialogue_5_dance_strip_3() from _call_dialogue_5_dance_strip_3
    $ questHelp("shinyhole_11", True)
    $ questHelp("shinyhole_12")
    $ add_objective("talk_claire", t_("Поговорить в пабе с другой стриптизершей."), c_green, 100)
    $ add_hook("Bartender", "dialogue_5_dance_strip_4nc", scene="pub", label="evening_time_temp")
    $ add_hook("change_time_day", "ep29_quests_pub1_day2_init", scene="global")
    $ remove_hook(label="monica_dance_block2")
    call refresh_scene_fade() from _call_refresh_scene_fade_214
    return False

label ep29_quests_pub1_day2_init:
    # утро второго дня
    $ remove_hook()
    $ move_object("Bartender_Waitress", "pub")
    $ add_hook("Bartender", "ep29_quests_pub1_day2_ashley2", scene="pub", label="monica_dance_forgiveness_dialogue1", quest="monica_dance_forgiveness")
    $ add_hook("Bartender_Waitress", "ep29_quests_pub1_day2_ashley2", scene="pub", label="monica_dance_forgiveness_dialogue1", quest="monica_dance_forgiveness")
    $ add_hook("Bartender", "ep29_quests_pub1_day2_ashley", scene="pub", label="monica_dance_forgiveness_day2", quest="monica_dance_forgiveness")
    $ add_hook("Bartender_Waitress", "ep29_quests_pub1_day2_ashley", scene="pub", label="monica_dance_forgiveness_day2", quest="monica_dance_forgiveness")
    $ add_hook("Pub_StripteaseGirl2", "ep29_quests_pub1_day2_claire1", scene="pub_makeuproom", label="monica_dance_forgiveness_dialogue1", quest="monica_dance_forgiveness")
    $ ep29_quests_pub_forgiveness_dancing_stage = 1
    return

label ep29_quests_pub1_day2_ashley:
    if act=="l":
        return
    call dialogue_5_dance_strip_6() from _call_dialogue_5_dance_strip_6
    if _return == -1:
        call refresh_scene_fade() from _call_refresh_scene_fade_215
        return False
    if _return == 1:
        $ ep29_quests_pub_forgiveness_dancing_quest_in_progress = False
        $ ep29_quests_pub_forgiveness_dancing_stage = 0
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_8
        $ remove_hook(quest="monica_dance_forgiveness")
        $ remove_objective("talk_claire")
        call refresh_scene_fade() from _call_refresh_scene_fade_216
        return False
    if _return == 0:
        $ remove_hook(label="monica_dance_forgiveness_day2")
        call refresh_scene_fade() from _call_refresh_scene_fade_217
        return False
    $ add_objective("go_to_makeuproom", t_("Идти в гримерку, чтобы подготовиться к выступлению на сцене."), c_orange, 110)


    $ add_hook("Bartender", "dialogue_5_dance_strip_4na", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ add_hook("Bartender_Waitress", "dialogue_5_dance_strip_4na", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ questLog(57, True)
    $ set_active("Teleport_Pub_MakeupRoom", True, scene="pub")
    call pub_dance_movegirls_to_makeuproom() from _call_pub_dance_movegirls_to_makeuproom_1
    call refresh_scene_fade() from _call_refresh_scene_fade_218
    return False

label ep29_quests_pub1_day2_ashley2: # Эшли встречает Монику, если та ушла и не стала танцевать
    if act=="l":
        return
    call dialogue_5_dance_strip_7() from _call_dialogue_5_dance_strip_7
    if _return == 1:
        $ ep29_quests_pub_forgiveness_dancing_quest_in_progress = False
        $ ep29_quests_pub_forgiveness_dancing_stage = 0
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_9
        $ remove_hook(quest="monica_dance_forgiveness")
        call refresh_scene_fade() from _call_refresh_scene_fade_219
        return False
    if _return == 0:
        call refresh_scene_fade() from _call_refresh_scene_fade_220
        return False
    $ add_objective("go_to_makeuproom", t_("Идти в гримерку, чтобы подготовиться к выступлению на сцене."), c_orange, 110)
    $ add_hook("Bartender", "dialogue_5_dance_strip_4na", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ add_hook("Bartender_Waitress", "dialogue_5_dance_strip_4na", scene="pub", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ questLog(57, True)
    $ set_active("Teleport_Pub_MakeupRoom", True, scene="pub")
    call pub_dance_movegirls_to_makeuproom() from _call_pub_dance_movegirls_to_makeuproom_2
    call refresh_scene_fade() from _call_refresh_scene_fade_221
    return False

label ep29_quests_pub1_day2_claire1: # первый разговорс Клэр
    if act=="l":
        return
    $ remove_hook()
    $ char_info["Pub_StripteaseGirl1"]["name"] = t_("Молли")
    $ char_info["Pub_StripteaseGirl2"]["name"] = t_("Клэр")
    call dialogue_5_dance_strip_8() from _call_dialogue_5_dance_strip_8
    $ questHelp("shinyhole_12", True)
    $ questHelp("shinyhole_13")
    $ questHelpDesc("shinyhole_desc9")

    $ ep29_quests_pub_monica_knows_claire = True
    $ ep29_quests_pub_monica_knows_molly = True
    $ remove_objective("talk_claire")
    $ remove_objective("go_to_makeuproom")
    $ add_objective("go_dance", t_("Выйти на сцену паба и танцевать."), c_orange, 110)
    $ add_hook("Pub_StripteaseGirl2", "dialogue_5_dance_strip_9b", scene="pub_makeuproom", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ pub_makeuproom_claire_suffix = "Look1"
    $ add_hook("change_time_day", "ep29_quests_pub1_day3_init", scene="global")
    $ add_hook("Teleport_Pub", "ep29_quests_pub1_day2_teleport_stage", scene="pub_makeuproom", label="monica_dance_block_stage", quest="monica_dance_forgiveness")
    $ add_hook("monica_pole_dance", "ep29_quests_dance", scene="global", label="monica_pole_dance", quest="monica_dance_forgiveness")
    $ add_hook("monica_pole_dance_end", "ep29_quests_pub1_day2_ashley3_init", scene="global", label="monica_pole_dance_ashley", quest="monica_dance_forgiveness")
    $ add_hook("enter_scene", "dialogue_5_dance_strip_9a", scene="pub_stage1", quest="monica_dance_forgiveness", once=True)
    $ move_object("Bartender", "pub_stage1")
    $ add_hook("Bartender", "ep29_quests_pub1_day2_joe", scene="pub_stage1", label="monica_dance_joe_catch1", quest="monica_dance_forgiveness")
    $ add_hook("Stage", "ep29_quests_pub1_day2_joe", scene="pub_stage1", label="monica_dance_joe_catch1", quest="monica_dance_forgiveness")
    $ ep29_quests_pub_block_money_return = True
    $ cloth = "StripOutfit1"
    $ cloth_type = "StripOutfit"
    $ questLog(59, True)
    call refresh_scene_fade() from _call_refresh_scene_fade_222
    return False

label ep29_quests_pub1_day2_joe:
    if act=="l":
        if obj_name == "Bartender":
            call dialogue_5_dance_strip_9a() from _call_dialogue_5_dance_strip_9a
            return False
        return
    $ remove_hook(label="monica_dance_joe_catch1")
    call dialogue_5_dance_strip_9() from _call_dialogue_5_dance_strip_9
    $ move_object("Bartender", "pub")
    call refresh_scene_fade() from _call_refresh_scene_fade_223
    return False

label ep29_quests_pub1_day2_ashley3_init:
    $ remove_hook()
    $ add_hook("enter_scene", "dialogue_5_dance_strip_10", scene="pub_makeuproom", quest="monica_dance_forgiveness", once=True)
    $ set_var("Cloth2", actions="lh", scene="pub_makeuproom")
    $ add_hook("Cloth2", "ep29_quests_dance_change_cloth", scene="pub_makeuproom", label="ep29_quests_dance_change_cloth")
    $ add_hook("Stage", "dialogue_5_dance_strip_4m", scene="pub_stage1", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ add_hook("Teleport_Pub", "ep29_quests_pub1_day2_ashley3", scene="pub_makeuproom", label="monica_dance_block", quest="monica_dance_forgiveness")
    $ pub_makeuproom_monica_suffix = 2
    call pub_dance_remove_stage_visitors() from _call_pub_dance_remove_stage_visitors
    $ remove_hook(label="monica_dance_block_stage")
    music stop
    img black_screen
    with diss
    pause 1.5
    call change_scene("pub_makeuproom") from _call_change_scene_446
    return False
label ep29_quests_pub1_day2_ashley3:
    if cloth_type != "StripOutfit":
        $ remove_hook()
        call dialogue_5_dance_strip_12() from _call_dialogue_5_dance_strip_12
        $ add_hook("Bartender", "dialogue_5_dance_strip_4m", scene="pub", label=["evening_time_temp"], quest="monica_dance_forgiveness")
        $ add_hook("Bartender_Waitress", "dialogue_5_dance_strip_4m", scene="pub", label=["evening_time_temp"], quest="monica_dance_forgiveness")
        $ set_active("Teleport_Pub_MakeupRoom", False, scene="pub")
        $ remove_hook(label="monica_dance_forgiveness_day2")
        $ pubDanceGirlsBlockedDay = day
    return

label ep29_quests_pub1_day2_teleport_stage:
    call change_scene("pub_stage1", "Fade_long") from _call_change_scene_447
    return False

label ep29_quests_pub1_day3_init:
    $ remove_hook()
    $ ep29_quests_pub_forgiveness_dancing_stage = 2
    $ add_hook("before_open", "dialogue_5_dance_strip_14", scene="pub_makeuproom", quest="monica_dance_forgiveness", once=True)
    $ add_hook("Pub_StripteaseGirl1", "ep29_quests_pub1_day3_molly", scene="pub_makeuproom", label="monica_dance_forgiveness_dialogue_molly1", quest="monica_dance_forgiveness")
    $ add_hook("Cloth2", "ep29_quests_pub1_day3_molly", scene="pub_makeuproom", label="monica_dance_forgiveness_dialogue_molly1", quest="monica_dance_forgiveness")
    return

label ep29_quests_pub1_day3_molly:
    if act=="l":
        return
    $ remove_hook(label="monica_dance_forgiveness_dialogue_molly1")
    call dialogue_5_dance_strip_14a() from _call_dialogue_5_dance_strip_14a
    $ remove_objective("go_to_makeuproom")
    $ add_objective("go_dance", t_("Выйти на сцену паба и танцевать."), c_orange, 110)
    $ add_hook("monica_pole_dance_end", "ep29_quests_pub1_day3_dance_end", scene="global", label="monica_pole_dance_end", quest="monica_dance_forgiveness")
    $ add_hook("Teleport_Pub", "ep29_quests_pub1_day2_ashley4", scene="pub_makeuproom", label="monica_dance_forgiveness_ashley_debt", quest="monica_dance_forgiveness")
    $ pub_makeuproom_monica_suffix = 2
    call refresh_scene_fade() from _call_refresh_scene_fade_224
    return False

label ep29_quests_pub1_day3_dance_end:
    $ remove_hook()
    $ add_hook("enter_scene", "dialogue_5_dance_strip_15", scene="pub_makeuproom", once=True, quest="monica_dance_forgiveness")
    call change_scene("pub_makeuproom", "Fade_long") from _call_change_scene_448
    call pub_dance_remove_stage_visitors() from _call_pub_dance_remove_stage_visitors_1
    $ pub_makeuproom_monica_suffix = 2
    $ set_active("Teleport_Pub_MakeupRoom", False, scene="pub")
    $ add_hook("change_time_day", "ep29_quests_pub1_day4_init", scene="global")
    return False

label ep29_quests_pub1_day2_ashley4: # Эшли забирает у Моники деньги после выступлений в счет долга
    if monicaDancedLastDay != day:
        return
    if cloth_type != "StripOutfit":
        if pubDanceCount <= 3:
            if ep29_quests_monica_gave_money_forgivenes_last_day != day:
                call dialogue_5_dance_strip_13() from _call_dialogue_5_dance_strip_13
                $ questHelp("shinyhole_15", True)
                $ questHelp("shinyhole_17", skipIfExists=True)
                $ ep29_quests_monica_gave_money_forgivenes_last_day = day
        else:
            # Монику прощают
            call dialogue_5_dance_strip_19() from _call_dialogue_5_dance_strip_19
            $ questLog(57, False)
            $ questLog(60, True)
            $ remove_hook(quest="monica_dance_forgiveness")
            call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_10
            $ questHelp("shinyhole_17", True)
            $ questHelp("shinyhole_19", skipIfExists=True)
            $ questHelpDesc("shinyhole_desc7", "shinyhole_desc10")

            $ ep29_quests_pub_forgiveness_dancing_enabled = False
            $ ep29_quests_pub_forgiveness_dancing_quest_in_progress = False
            $ monica_shared_tips_with_ashley_last_day = day
            $ add_hook("Bartender", "pub_dance_joe_after", scene="pub", label="monica_dance_joe_after", quest="monica_dance_forgiveness")
            $ add_hook("Bartender_Waitress", "pub_dance_ashley_after", scene="pub", label="monica_dance_ashley_after", quest="monica_dance_forgiveness")
            call pub_dance_init() from _call_pub_dance_init # инициализируем добровольные танцы
        $ add_hook("Bartender", "dialogue_5_dance_strip_4m", scene="pub", label=["evening_time_temp"], quest="monica_dance_forgiveness")
        $ add_hook("Bartender_Waitress", "dialogue_5_dance_strip_4m", scene="pub", label=["evening_time_temp"], quest="monica_dance_forgiveness")
        $ pubDanceGirlsBlockedDay = day
    return

label ep29_quests_pub1_day4_init:
    $ remove_hook()
    $ ep29_quests_pub_forgiveness_dancing_stage = 3
    $ add_hook("Pub_StripteaseGirl2", "ep29_quests_pub1_day4_claire", scene="pub_makeuproom", label="monica_dance_forgiveness_claire_dialogue2", quest="monica_dance_forgiveness")
#    $ add_hook("Cloth2", "ep29_quests_pub1_day4_claire", scene="pub_makeuproom", label="monica_dance_forgiveness_claire_dialogue2", quest="monica_dance_forgiveness")
    $ add_hook("Teleport_Pub", "ep29_quests_pub1_day4_joe", scene="pub_makeuproom", label="monica_dance_forgiveness_joe_catch2", quest="monica_dance_forgiveness")
    $ add_hook("monica_pole_dance_end", "ep29_quests_pub1_day4_dance_end", scene="global", label="monica_pole_dance_end", quest="monica_dance_forgiveness")
    $ pubMakeupRoomGirlsRandomSuffix = True
    return

label ep29_quests_pub1_day4_claire:
    if act=="l":
        return
#    $ remove_hook(label="monica_dance_forgiveness_claire_dialogue2")
    if ep29_quests_claire_talk_last_day == day or cloth != "Whore":
        call dialogue_5_dance_strip_28() from _call_dialogue_5_dance_strip_28
        $ pub_makeuproom_claire_suffix = "1"
        call refresh_scene_fade() from _call_refresh_scene_fade_225
        return False
    $ ep29_quests_claire_talk_last_day = day
    call dialogue_5_dance_strip_16() from _call_dialogue_5_dance_strip_16
    $ autorun_to_object("dialogue_5_dance_strip_16a", scene="pub_makeuproom")
    $ pub_makeuproom_claire_suffix = "Look1"
    $ pub_makeuproom_monica_suffix = 1
    music Molten_Alloy
    $ pubMakeupRoomSkipMusicOnce = True
    call refresh_scene_fade() from _call_refresh_scene_fade_226
#    mt "Черт! Снова эта сцена! И толпа пьяных неудачников!"
    call ep210_quests_pub9_claire_offer_check() from _rcall_ep210_quests_pub9_claire_offer_check
    $ add_objective("go_dance", t_("Выйти на сцену паба и танцевать."), c_orange, 110)
    $ remove_objective("go_to_makeuproom")
    return False

label ep29_quests_pub1_day4_joe:
    if cloth != "Whore":
        $ remove_hook()
        call dialogue_5_dance_strip_17() from _call_dialogue_5_dance_strip_17
        $ ep29_quests_joe_catched_monica_claire = True
        $ pubDanceGirlsBlockedDay = day
        $ move_object("Pub_StripteaseGirl2", "empty")
        $ ep29_quests_pub_forgiveness_dancing_stage = 4
        call refresh_scene_fade() from _call_refresh_scene_fade_227

    return

label ep29_quests_pub1_day4_dance_end:
    $ add_hook("enter_scene", "dialogue_5_dance_strip_18", scene="pub_makeuproom", once=True)
    call pub_dance_remove_stage_visitors() from _call_pub_dance_remove_stage_visitors_2
    $ pub_makeuproom_monica_suffix = 2
    call change_scene("pub_makeuproom", "Fade_long") from _call_change_scene_449
    return False

label ep29_quests_dance:
    call pub_dance1() from _call_pub_dance1
    return

label ep29_quests_dance_change_cloth:
    if act=="l":
        return
    call dialogue_5_dance_strip_29() from _call_dialogue_5_dance_strip_29
    if _return == 0:
        $ pub_makeuproom_monica_suffix = 1
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    if _return == 1:
        $ pub_makeuproom_monica_suffix = 1
        $ cloth = "StripOutfit2"
        $ cloth_type = "StripOutfit"
    if _return == 2:
        $ pub_makeuproom_monica_suffix = 2
        $ cloth = "Whore"
        $ cloth_type = "Whore"

    $ remove_objective("go_to_makeuproom")
    if monicaDancedLastDay != day and cloth_type == "StripOutfit":
        $ add_objective("go_dance", t_("Выйти на сцену паба и танцевать."), c_orange, 110)

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    call refresh_scene_fade() from _call_refresh_scene_fade_228
    return False

#
