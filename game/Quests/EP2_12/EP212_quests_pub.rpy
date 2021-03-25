default pubPrivate1Count = 0
default pubPrivate2Count = 0

label ep212_quests_pub_menu_private: # Меню приватов
    call ep212_dialogues2_shiny_hole_menu_private() from _rcall_ep212_dialogues2_shiny_hole_menu_private
    if _return == -1: # Танцев не выбрано
#        $ dancePrivateLastDay = day
        return
    if _return == 0: # Танец для Мистера Беркельбауха.
        call ep211_dialogues5_shiny_hole_1() from _rcall_ep211_dialogues5_shiny_hole_1_1
        if _return == False:
            call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_2
            return False
        call ep211_dialogues5_shiny_hole_2() from _rcall_ep211_dialogues5_shiny_hole_2_1
        if _return == False:
            call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_3
            return False
        $ autorun_to_object("ep211_dialogues5_shiny_hole_9", scene="pub_makeuproom")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_14
        return
    if _return == 1: # Приват1
        $ remove_hook(label="dialogue_5_dance_strip_18")
        $ pub_makeuproom_monica_suffix = 2
        call ep212_dialogues2_shiny_hole_1() from _rcall_ep212_dialogues2_shiny_hole_1
        if _return == False:
            $ questHelp("shinyhole_33", False, skipIfTrue=True)
            return
        $ add_objective("go_dance_private", t_("Идти в подсобку барменов и станцевать приват."), c_orange, 105)
        $ add_hook("Teleport_Pub", "ep212_quests_pub_private1_1", scene="pub_makeuproom", label="pub_private_dance1", priority = 10001)
        return
    if _return == 2: # Приват2
        $ remove_hook(label="dialogue_5_dance_strip_18")
        $ pub_makeuproom_monica_suffix = 2
        call ep213_dialogues3_pub_15() from _rcall_ep213_dialogues3_pub_15
        if _return == False:
            $ questHelp("shinyhole_35", False, skipIfTrue=True)
            return
        $ pub_makeuproom_monica_suffix = 2
        $ add_objective("go_dance_private", t_("Идти в подсобку барменов и станцевать приват."), c_orange, 105)
        $ add_hook("Teleport_Pub", "ep213_quests_pub_private2_1", scene="pub_makeuproom", label="pub_private_dance1", priority = 10001)
        return
    return

label ep212_quests_pub_private1_1: # Приват 1
    if cloth_type != "StripOutfit":
        call ep211_dialogues5_shiny_hole_8() from _rcall_ep211_dialogues5_shiny_hole_8_1
        return False
    # сцена
    $ remove_objective("go_dance_private")
    $ remove_hook(label="pub_private_dance1")
    $ pubPrivate1Count += 1
    $ dancePrivateLastDay = day
    call ep212_dialogues2_shiny_hole_2() from _rcall_ep212_dialogues2_shiny_hole_2
    if _return == -1:
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_15
        return
    $ questHelp("shinyhole_33", True)
    $ questHelp("shinyhole_35", skipIfExists=True)
    if questHelpFlag14 == False:
        $ questHelpFlag14 = True
        $ questHelpDesc("shinyhole_desc10a", "shinyhole_desc10b")

    $ customer3_after_private = True
    $ questHelp("shinyhole_58a", skipIfExists=True)
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_16
    return

label ep212_quests_pub_reset_pub: # Сброс квеста shiny hole
    menu:
        "Сбросить все квесты Shiny Hole?":
            pass
        "Продолжить.":
            return
    python:
        customer1_dance_comment_stage = 0
        customer2_dance_comment_stage = 0
        customer3_1stmeetingEvent1Count = 0
        customer3_1stmeetingEvent2Count = 0
        customer3_serve2Event1Count = 0
        customer3_serve2Event2Count = 0
        customer3_dance_comment_stage = 0
        customer3_after_private = False
        customer3_after_private_agree_count = 0
        customer4_dance_comment_stage = 0
        customer5_dance_comment_stage = 0
        customer78_dance_comment_stage = 0
        customer9_dance_comment_stage = 0
        customer10_dance_comment_stage = 0
        customer11_dance_comment_stage = 0
        customer12_dance_comment_stage = 0
        ep27_dialogues7ReturnedMoneyCount = 0
        dialogue_5_dance_strip_20_flag1 = False
        monicaClaireOilingCount = 0
        monicaClaireOilingToplessCount = 0
        monicaClareStoryAboutLife = False
        monicaMollyFoto = False
        monicaPubPrivatDance1 = False
        monicaPubPrivatDance2 = False
        monicaPubPrivatDance3 = False
        monicaPubPrivatDanceJoe1 = False
        monicaPubPrivatDanceJoe2 = False
        monicaPubPrivatDanceJoe3
        monicaPubPrivate1CumZone = 0
        pubMonicaWaitressTipsPunishmentJoeStage = 0
        pubMonicaWaitressTipsPunishmentAshleyStage = 0
        visitorsVisits = {}
        pubMonicaWorkingWaitress = False
        pubMonicaWorkingWaitressShiftInProgress = False
        pubMonicaWorkedWaitressLastDay = 0
        pubMonicaWaitressTips = 0
        pubMonicaWaitressTipsStolen = False
        pubMonicaWaitressServedCustomersToday = 0
        pubMonicaWaitressServedCustomersTotal = 0
        pubMonicaWaitressWorkedDaysTotal = 0
        pubMonicaWaitressVisitorsServed = []
        pubMonicaWaitressClothBefore = ""
        pubMonicaWaitressClothTypeBefore = ""
        pubMonicaWaitressTipsPunishmentTalkStage = 0
        ep29_quests_pub_forgiveness_dancing_enabled = True
        ep29_quests_pub_forgiveness_dancing_quest_in_progress = False
        ep29_quests_pub_forgiveness_dancing_stage = 0
        ep29_quests_pub_monica_knows_claire = False
        ep29_quests_pub_monica_knows_molly = False
        ep29_quests_pub_block_money_return = False
        monica_strip_forgiveness_money_left = 500
        pubMakeupRoomGirlsRandomSuffix = False
        ep29_quests_claire_talk_last_day = 0
        ep29_quests_joe_catched_monica_claire = False
        ep29_quests_monica_gave_money_forgivenes_last_day = 0
        ep29_quests_only_claire = False
        ep210_quests_stage = 0
        ep210_picture_marked = False
        ep210_picture_marked_day = 0
        ep210_picture_was_marked = False
        ep210_picture_marked_claire_comment = False
        ep210_picture_marked_molly_comment = False
        ep29_quests_monica_molly_fine = False # Моника отдает все чаевые, пока Молли ее не простит
        ep29_quests_monica_molly_was_fine = False
        ep29_quests_claire_dance_planned = False
        ep29_quests_molly_fall_panties_planned0 = False # Запланировано падение трусиков
        ep29_quests_molly_fall_panties_planned = False # Запланировано падение трусиков
        ep29_quests_molly_fall_panties_completed = False
        ep29_quests_dancing_with_claire_active = False
        ep29_quests_dancing_with_claire_last_day = 0
        ep211_quests_pub_started_stole_tips = False
        monicaPubDanceStoleTipsActive = False
        monicaPubDanceStoleTipsDay = 0
        monicaPubDanceStoleTipsStage = 0
        monicaPubDanceStoleTipsBankerCompleted = False
        monicaPubDanceStoleTipsBankerPlanned = False
        monicaPubMollyNeedForgive1 = False
        monicaPubFiredTips1 = False
        pubPrivate1Count = 0
        pub_dance_claire_dialogues_up_list = []
        pub_dance_claire_dialogues_up_list2 = []
        pub_dance_claire_ahley_comment1_flag = False
        pub_dance_dialogues_up_list = []
        pub_dance_dialogues_up_list2 = []
        pub_dance_dialogues_side_list = []
        pub_dance_dialogues_side_list2 = []
        pub_dance_dialogues_down_list = []
        pub_dance_dialogues_down_list2 = []
        pub_dance_dialogues_up_list3 = []
        pub_dance_dialogues_up_list4 = []
        pub_dance_dialogues_side_list3 = []
        pub_dance_dialogues_side_list4 = []
        pub_dance_dialogues_down_list3 = []
        pub_dance_dialogues_down_list4 = []
        stageMusicControlEnabled = False # включено-ли произвольное управление музыкой
        stageMusicMode = 0 # 0 - последовательно, 1 - случайно, 2 - произвольная музыка
        stageLastMusic = -1 # индекс последней игравшей музыки
        stageCustomMusic = 0 # индекс произвольной музыки
        stageCurrentMusicIntro = False
        stageCurrentMusicLoop = False
        stage_Monica_shoots_array = []
        stage_Monica_shoots_array_current = []
        stage_Monica_last_shoots_array = []
        stage_Monica_last_zone = False
        stage_Monica_Excitement_Current = 0
        stage_Monica_Excitement_Last = 0
        stage_shoots_total_amount_default = 27
        stage_shoots_total_amount_claire = 24
        stage_shoots_total_amount_cur = 27
        stage_achievements_list = []
        pubDanceGirlsBlockedDay = 0
        monica_strip_tips_today = 0
        monica_shared_tips_with_ashley_last_day = 0
        pubDanceCount = 0
        monicaDancedLastDay = 0
        monicaDancingTopless = False
        monicaDancingJoeAskedAboutPrivate = False
        monicaDancingWillingly = False
        monicaAshleyTalkedAboutSharingTips = False
        monicaAshleyTalkedAboutSharingTipsDay = 0
        monicaDancingStage = 0 # 0 - корсет (1..3), 1 - топлесс (4..6), 2 - топлесс (7..9)
        monicaDancingInProgress = False
        monicaStartedStripDanceFlag = False
        monicaDanceStartHookInited = False
        dancePrivateMenuEnabled = True
        dancePrivateLastDay = 0
        pubDanceAfterBlockEvents = False
        pubInited = False
        monicaPubWashingDishesCount = 0 # Кол-во раз Моника мыла посуду
        pubFoodHistory = []
    call characters_pub_init() from _rcall_characters_pub_init
    call characters_pub_init2() from _rcall_characters_pub_init2
    $ clear_hooks("start_dance_event", scene="global")
    $ clear_hooks("monica_pole_dance_end", scene="global")
    $ clear_hooks("monica_pole_dance", scene="global")
    $ clear_hooks(scene="pub_makeuproom")
    $ clear_scene_from_objects("pub_makeuproom")
    $ clear_hooks(scene="pub_stage1")
    $ clear_scene_from_objects("pub_stage1")
    $ clear_hooks(scene="pub_bar1")
    $ clear_scene_from_objects("pub_bar1")
    $ clear_hooks(scene="pub")
    $ clear_scene_from_objects("pub")
    $ questLog(69, False)
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
    $ questLog(70, False)
    $ questLog(59, False)
    $ questLog(30, False)

    call ep23_quests_pub_init() from _rcall_ep23_quests_pub_init
    music stop
    music2 stop
    img black_screen
    with diss
    pause 3.0
    call change_scene("hostel_street", "Fade_long") from _rcall_change_scene_88
    return False
