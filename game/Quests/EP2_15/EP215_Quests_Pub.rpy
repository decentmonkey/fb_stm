default ep215_quests_pub1_inited = False
default ep215_quests_vest_only_active = False
default ep215_quests_pub2_lastday = 0
default ep215_quests_ashley_dialogue1_active = False
default ep215_quests_ashley_dialogue2_active = False
default ep215_quests_molly_monica_fight_day = 0
default monica_shiny_hole_queen_day = 0

label ep215_quests_pub1:
    if ep215_quests_pub1_inited == True:
        return
    $ ep215_quests_pub1_inited = True
    $ ep215_quests_vest_only_active = True
    $ add_hook("Teleport_Pub", "ep215_quests_pub2", scene="pub_makeuproom", label="ep215_quests_pub2")

    return

label ep215_quests_pub2:
    if cloth_type != "StripOutfit" or get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False:
        return
    if day - ep215_quests_pub2_lastday < 4: # не показываем слишком часто
        return
    $ ep215_quests_pub2_lastday = day
    call ep215_dialogues1_pub_1() from _rcall_ep215_dialogues1_pub_1
    $ questHelp("shinyhole_42", True)
    $ questHelp("shinyhole_45")
    $ add_hook("before_open", "ep215_quests_pub3_molly1", scene="pub_makeuproom", label="ep215_quests_pub3_molly1")
#    $ add_talk("Pub_StripteaseGirl1", "ep215_quests_pub3_molly1", scene="pub_makeuproom", label="ep215_quests_pub3_molly1")
    return

label ep215_quests_pub3_molly1:
    if ep215_quests_pub2_lastday == day or get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False:
        return
    $ remove_hook(label="ep215_quests_pub3_molly1")
    $ remove_hook(label="ep215_quests_pub2")
    $ ep215_quests_vest_only_active = False
    call ep215_dialogues1_pub_2() from _rcall_ep215_dialogues1_pub_2
    $ questHelp("shinyhole_45", True)
    $ questHelp("shinyhole_46")
    $ add_talk("Pub_StripteaseGirl1", "ep215_quests_pub3_molly2", scene="pub_makeuproom", label="ep215_quests_pub3_molly2")
    $ pub_makeuproom_monica_suffix = 2
    return

label ep215_quests_pub3_molly2:
    if cloth_type != "Whore":
        $ cloth = "Whore"
        $ cloth_type = "Whore"
        sound snd_fabric1
        fadeblack 2.0
    call ep215_dialogues1_pub_3() from _rcall_ep215_dialogues1_pub_3 # предложение баттла
    if _return == False:
        $ pub_makeuproom_monica_suffix = 2
        $ questHelp("shinyhole_46", False)
        return False
    # баттл
    $ remove_hook()
    call ep215_dialogues1_pub_4() from _rcall_ep215_dialogues1_pub_4
    call ep215_dialogues1_pub_5() from _rcall_ep215_dialogues1_pub_5
    call ep215_dialogues1_pub_7() from _rcall_ep215_dialogues1_pub_7
    $ questHelp("shinyhole_46", True)
    $ questHelp("shinyhole_47")
    $ remove_objective("go_dance")
    $ move_object("Pub_StripteaseGirl1", "empty")
    $ monicaDancedLastDay = day
    $ ep215_quests_ashley_dialogue1_active = True
    $ ep215_quests_vest_only_active = True
    $ add_hook("Teleport_Pub", "ep215_quests_pub3_molly3", scene="pub_makeuproom", label="ep215_quests_pub3_molly3")
#    $ add_talk("Pub_StripteaseGirl1", "ep215_quests_pub3_molly3", scene="pub_makeuproom", label="ep215_quests_pub3_molly2")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_20

    return False

label ep215_quests_pub3_molly3:
    if ep215_quests_molly_monica_fight_day == day:
        return
    if cloth_type != "StripOutfit":
        return
    if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False:
        return
    call ep215_dialogues1_pub_9() from _rcall_ep215_dialogues1_pub_9
    if _return == False:
        $ questHelp("shinyhole_47", False)
        return
    # драка
    $ ep215_quests_molly_monica_fight_day = day
    call ep215_dialogues1_pub_9_loop1() from _rcall_ep215_dialogues1_pub_9_loop1
    if _return == 0: # уйти
        $ questHelp("shinyhole_47", False)
        return
    $ questHelp("shinyhole_47", True)
    if _return == -2: # Моника отказалась на второй баттл
        $ questHelp("shinyhole_48", False)
        sound snd_fabric1
        fadeblack 2.0
        $ move_object("Pub_StripteaseGirl1", "empty")
        return
    if _return == 1: # второй баттл
        $ monicaDancedLastDay = day
        $ move_object("Pub_StripteaseGirl1", "empty")
        call ep215_dialogues1_pub_10() from _rcall_ep215_dialogues1_pub_10
        $ questHelp("shinyhole_48", True)
        if _return == False:
            $ questHelp("shinyhole_49", False)
            $ pub_makeuproom_monica_suffix = 2
            call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_21
            return False

        $ questsFailByCategory(t_("SHINY HOLE"))
        $ questHelp("shinyhole_48", True)
        $ questHelp("shinyhole_49", skipIfExists=True)
        $ ep215_quests_vest_only_active = False
        $ remove_hook(label="ep215_quests_pub3_molly3")
        # Моника королева Shiny Hole
        $ ep215_quests_ashley_dialogue1_active = False
        $ ep215_quests_ashley_dialogue2_active = True

        $ monica_shiny_hole_queen_day = day
        call ep215_dialogues1_pub_11() from _rcall_ep215_dialogues1_pub_11
        $ questHelp("shinyhole_49", True)
        $ questHelp("shinyhole_49a")
#        $ questHelp("shinyhole_50")
        $ questHelpDesc("shinyhole_desc12a", "shinyhole_desc16")
        $ questHelpDesc("shinyhole_desc8", False)
        $ questHelpDesc("shinyhole_desc10b", False)

        $ questHelp("shinyhole_58")

        $ pubCustomersQueenList = []

        $ set_active("Picture", False, scene="pub_makeuproom") # убираем старую картину
        call pub_makeuproom_init5() from _rcall_pub_makeuproom_init5 # инициализируем картину
        $ remove_objective("go_dance")
        $ questLog(84, True)
        $ add_talk("Pub_StripteaseGirl1", "ep215_dialogues1_pub_12", scene="pub_makeuproom", label="monica_queen_molly_talk_refuse")
        $ add_talk("Pub_StripteaseGirl2", "ep215_quests_pub4_claire", scene="pub_makeuproom", label="ep215_quests_pub4_claire")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_22
        return False

    return False


label ep215_quests_pub4_claire:
    $ remove_hook()
    if cloth_type != "Whore":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep215_dialogues1_pub_13() from _rcall_ep215_dialogues1_pub_13
    $ questHelp("shinyhole_49a", True)
    return False











#
