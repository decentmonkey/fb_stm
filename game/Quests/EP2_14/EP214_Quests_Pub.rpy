default ep214_quests_pub1_check_inited_flag = False
default ep214_quests_poster_day = 0
default ep214_quests_claire_visited_monica_office1_day = 0
default ep214_quests_claire_show1_day = 0
default ep214_quests_claire_talkafter_show1_day = 0
default ep214_quests_activated_alt_day = 0

label ep214_quests_pub1_check_init:
    # проверка на инициализацию
    if pubPrivate2Count < 1 or ep214_quests_pub1_check_inited_flag == True or dancePrivateLastDay == day or monicaDancedLastDay == day or ep211_quests_photoshot8_opened_day == 0 or ep213_quests_pub10_molly_complete == False or ep213_quests_pub9_claire_complete == False or ep214_quests_activated_alt_day == day:
        return
    $ ep214_quests_pub1_check_inited_flag = True
    call ep214_quests_pub2_enter_scene() from _rcall_ep214_quests_pub2_enter_scene
#    $ enter_scene("ep214_quests_pub2_enter_scene")


    return


label ep214_quests_pub2_enter_scene:
    $ remove_hook()
    call ep214_dialogues1_pub_1() from _rcall_ep214_dialogues1_pub_1
    call pub_init3() from _rcall_pub_init3
    $ add_hook("Poster1", "ep214_dialogues1_pub_1a", scene="pub", label="pub_poster1")
    $ move_object("Bartender_Waitress", "empty")
    $ add_hook("before_open", "ep214_quests_pub3_makeuproom", scene="pub_makeuproom", label="pub_poster1", priority=10000)
    $ questHelp("shinyhole_37", True)
    $ questHelp("shinyhole_37a")
    $ ep214_quests_poster_day = day
#    call pub_dance_start_direct()
    $ set_active("Teleport_Pub_MakeupRoom", True, scene="pub")
    $ add_hook("Teleport_Hostel_Street", "ep214_dialogues1_pub_1b", scene="pub", label="pub_poster_block", priority=10000)
    $ add_hook("Bartender", "ep214_dialogues1_pub_1b", scene="pub", label="pub_poster_block")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_106
    return

label ep214_quests_pub3_makeuproom: # разговор с Эшли в гримерке
    $ remove_hook()
    $ remove_hook(label="pub_poster_block")
    $ set_active("Teleport_Pub_MakeupRoom", False, scene="pub")
    $ move_object("Pub_StripteaseGirl1", "empty")
    $ move_object("Pub_StripteaseGirl2", "empty")
    $ move_object("Bartender_Waitress", "pub")
    $ add_talk("Pub_StripteaseGirl2", "ep214_quests_pub4_claire", scene="pub_makeuproom", label="pub_poster1")
    $ add_objective("talk_claire", t_("Поговорить с Клэр о требовании Эшли"), c_orange, 125)
    call ep214_dialogues1_pub_2() from _rcall_ep214_dialogues1_pub_2
    $ questHelp("shinyhole_37a", True)
    $ questHelp("shinyhole_38")
    call change_scene("pub", "Fade_long") from _rcall_change_scene_136
    return

label ep214_quests_pub4_claire: #разговор с Клэр
    $ remove_hook()
    call ep214_dialogues1_pub_3() from _rcall_ep214_dialogues1_pub_3
    $ questHelp("shinyhole_38", True)
    $ questHelp("office_46")
    $ questHelpDesc("shinyhole_desc9", "shinyhole_desc13")

    $ remove_objective("talk_claire")
    $ questLog(76, True)
    $ add_talk("Pub_StripteaseGirl2", "ep214_dialogues1_pub_4", scene="pub_makeuproom", label="pub_poster1_claire_repeat")
    $ autorun_to_object("ep214_dialogues1_pub_5")
    $ add_hook("before_open", "ep214_quests_pub5", scene="monica_office_entrance", label="pub_poster1")
    $ add_objective("talk_claire", t_("Надеть лучшее платье и встретиться с Клэр в офисе"), c_green, 135)
    $ pub_makeuproom_monica_suffix = 2
    call refresh_scene_fade() from _rcall_refresh_scene_fade_107
    return False

label ep214_quests_pub5:
    if day_time != "day" or week_day == 7 or cloth != "CasualDress1":
        return
    $ remove_hook()
    $ remove_hook(label="pub_poster1_claire_repeat")
    call ep214_dialogues1_pub_6() from _rcall_ep214_dialogues1_pub_6
    call ep214_dialogues1_pub_7() from _rcall_ep214_dialogues1_pub_7
    call ep214_dialogues1_pub_8() from _rcall_ep214_dialogues1_pub_8
    call ep214_dialogues1_pub_9() from _rcall_ep214_dialogues1_pub_9
    $ questHelp("office_46", True)
    $ questHelp("shinyhole_39", skipIfExists=True)
    $ questHelpDesc("shinyhole_desc13", "shinyhole_desc14")
    $ questLog(76, False)
    $ questLog(77, True)
    $ remove_objective("talk_claire")
    $ add_talk("Pub_StripteaseGirl2", "ep214_quests_pub6_claire", scene="pub_makeuproom", label="pub_poster1")
    $ ep214_quests_claire_visited_monica_office1_day = day
    call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_137
    return

label ep214_quests_pub6_claire: #разговор с Клэр после визита в офис
    $ remove_hook()
    call ep214_dialogues1_pub_10() from _rcall_ep214_dialogues1_pub_10
    $ pubDanceAfterBlockEvents = True
    $ questHelp("shinyhole_39", True)
    $ questHelp("shinyhole_40")
    $ questHelpDesc("shinyhole_desc14", "shinyhole_desc15")

    $ add_talk("Pub_StripteaseGirl2", "ep214_dialogues1_pub_11", scene="pub_makeuproom", label="pub_poster1_claire_repeat")
    $ add_hook("before_open", "ep214_quests_pub7_after_dance", scene="pub_makeuproom", label="pub_poster1")
    return False

label ep214_quests_pub7_after_dance:
    if monicaDancedLastDay != day:
        return
    # если Моника уже потанцевала, ее в гримерке ждет Эшли
    $ remove_hook()
    $ remove_hook(label="pub_poster1_claire_repeat")
    call ep214_dialogues1_pub_12() from _rcall_ep214_dialogues1_pub_12
    if _return == False: # увольнение
        call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_6
        return False

    $ add_hook("Teleport_Pub", "ep214_quests_pub8", scene="pub_makeuproom", label="pub_poster1")
    return

label ep214_quests_pub8:
    if cloth_type != "StripOutfit":
        call ep211_dialogues5_shiny_hole_8() from _rcall_ep211_dialogues5_shiny_hole_8_3
        return False
    $ remove_hook()
    call ep214_dialogues1_pub_13() from _rcall_ep214_dialogues1_pub_13 # начало сцены
    call ep214_dialogues1_pub_14() from _rcall_ep214_dialogues1_pub_14
    if _return == False: # увольнение
        $ questHelp("shinyhole_40", False)
        call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_7
        return False
    $ questHelp("shinyhole_40", True)
    $ questHelp("shinyhole_41", True)
    $ questHelp("shinyhole_41a", skipIfTrue=True)
    $ questHelp("shinyhole_42", skipIfTrue=True)
    $ ep214_quests_claire_show1_day = day

    $ enter_scene("ep214_dialogues1_pub_16", label="pub_poster1", once=True)
    $ remove_hook(label="pub_poster1")
    $ set_active("Poster1", False, scene="pub")
    $ add_talk("Pub_StripteaseGirl2", "ep214_quests_pub9_claire", scene="pub_makeuproom", label="pub_poster1")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_108
    return False

label ep214_quests_pub9_claire: # разговор с Клэр после сцены
    $ remove_hook()
    if cloth != "Whore":
        sound snd_fabric1
        fadeblack 1.5
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep214_dialogues1_pub_15() from _rcall_ep214_dialogues1_pub_15
    $ questHelp("shinyhole_41a", True)
    $ ep214_quests_claire_talkafter_show1_day = day
    return False











#
