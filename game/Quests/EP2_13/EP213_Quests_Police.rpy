default ep213_quests_police_inited = False

default ep213_quests_police_money_stored = 0
default ep213_quests_police_inventory_stored = []
default ep213_quests_police_objectives_stored = []

default ep213_quests_prisoner = False
default ep213_quests_prisoner1_offended = False

label ep213_quests_police1_check_init:
    if ep213_quests_police_inited == True:
        return True
    if day - ep28_quests_completed_day >= 7 or ep28_quests_completed_day == 0: # Если прошла неделя с посещения, либо день не был зафиксирован
        call ep213_dialogues_police1() from _rcall_ep213_dialogues_police1 # Если с момента прошлого посещения Маркуса прошла неделя, то Моника при клике на полицию говорит
        if _return == 0:
            $ questHelp("marcus_11", False)
            $ questHelp("marcus_11a", False)
            return False
        if _return == 1:
            $ add_objective("take_buttplug", t_("Вернуться к полиции с анальной пробкой."), c_red, 105)
            $ questHelp("marcus_11a", skipIfExists=True)
            $ remove_hook(label="police2_buttplug")
            $ add_hook("ButtPlug", "ep213_quests_police3_takeplug", scene="basement_bedroom2", label="police2_buttplug", quest="police2")
            $ add_hook("ButtPlug", "ep213_quests_police3_takeplug", scene="basement_bedroom_table_opened", label="police2_buttplug", quest="police2")
#            if get_active_objects("ButtPlug", scene="basement_bedroom2") == False and get_active_objects("ButtPlug", scene="basement_bedroom_table_opened") == False:
            call basement_bedroom2_init2() from _rcall_basement_bedroom2_init2_var1
            $ move_object("ButtPlug", "basement_bedroom2")

        if _return == 2:
            $ ep213_quests_police_inited = True
            call ep213_dialogues_police2() from _rcall_ep213_dialogues_police2
            $ autorun_to_object("ep213_dialogues_police2a", scene="police_entrance")
            $ add_hook("Teleport_Inside", "ep213_quests_police2_turniket", scene="police_entrance", quest="police2")
            $ add_hook("Reception", "ep213_quests_police2_talk_reception", scene="police_entrance", quest="police2")
            $ remove_hook(label="marcus_block1")
            $ remove_hook(label="police_quest1")
            $ questHelp("marcus_11", True)
            $ questHelp("marcus_11a", True)
            $ add_hook("Building", "ep213_quests_police4_enter_police", scene="street_police", quest="police2")
            call change_scene("police_entrance", "Fade_long") from _rcall_change_scene_108
            return False

        return False

    return True


label ep213_quests_police2_talk_reception:
label ep213_quests_police2_turniket:
    call ep213_dialogues_police2b() from _rcall_ep213_dialogues_police2b
    $ remove_objective("take_buttplug")
    $ ep213_quests_police_money_stored = money
    $ money = 0
    $ ep213_quests_police_inventory_stored = inventory
    $ inventory = []
    $ add_inventory("butt_plug", 1, False)
    $ ep213_quests_police_objectives_stored = objectives_list
    $ objectives_list = []
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)

    fadeblack
    pause 2.0
    $ cloth = "NudePlug"
    $ cloth_type = "Nude"
    $ add_hook("Monica", "ep213_dialogues_police3", scene="police_cell1", label="police_day1", quest="police2")
    $ add_hook("Teleport_Cage2", "ep213_dialogues_police4", scene="police_cell1", label="police_day1", quest="police2")
    $ add_hook("Sortir", "ep213_dialogues_police5", scene="police_cell1", label="police_day1_sortir", quest="police2")
    $ add_hook("Bed", "ep213_quests_police5_day1_bed", scene="police_cell1", label="police_day1", quest="police2")
    $ police_cell1_monica_breath = False
    $ monicaPoliceCellSuffixMode = 1
    $ monicaPoliceCell1Suffix = 1
    $ monicaPoliceCell2Suffix = 1
    $ questHelp("marcus_4")
    call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_109

    return False

label ep213_quests_police3_takeplug: # взять пробку
    if act=="l":
        return
    $ remove_hook(label="police2_buttplug")
    $ set_active("ButtPlug", False)
    fadeblack
    pause 1.0
    sound chpok2
    pause 1.5
    $ add_inventory("butt_plug", 1, True)
    call refresh_scene_fade() from _rcall_refresh_scene_fade_74
    return False

label ep213_quests_police4_enter_police:
    if act=="l":
        return
    call change_scene("police_entrance", "Fade_long") from _rcall_change_scene_110
    return False

label ep213_quests_police5_day1_bed:
    if act=="l":
        return
    $ remove_hook(label="police_day1")
    call police_cell1_init2() from _rcall_police_cell1_init2
    call police_cell2_init2() from _rcall_police_cell2_init2
    call ep213_dialogues_police7() from _rcall_ep213_dialogues_police7
    $ ep213_quests_prisoner = _return
    if _return == True:
        $ police_cell1_monica_breath = True
        $ move_object("Prisoner1", "police_cell1")
        $ add_hook("Prisoner1", "ep213_quests_police6_prisoner1_regular", scene="police_cell1", label="police_prisoner1_regular", quest="police2")
        $ add_hook("Prisoner1", "ep213_quests_police6_prisoner1_regular", scene="police_cell2", label="police_prisoner1_regular", quest="police2")
        $ add_hook("Prisoner1", "ep213_quests_police7_day1_action1", scene="police_cell1", label="police_day1", quest="police2")
        $ add_hook("Prisoner1", "ep213_quests_police7_day1_action1", scene="police_cell2", label="police_day1", quest="police2")
        $ monicaPoliceCell1Suffix = 1
        $ prisoner1Cell1Suffix = 2
        $ add_hook("cage_interact", "ep213_quests_police8_cage_prisoners", scene="police", label="cage_interact2_prisoners")
        $ policeCell2PrisonersYell = True
        $ questHelp("marcus_13")
    else:
        $ questHelp("marcus_13", False)
        $ monicaPoliceCell1Suffix = 2
    $ cloth = "Jail_Cloth3"
    $ add_hook("Sortir", "ep213_dialogues_police14", scene="police_cell1", label="police_day1_sortir", quest="police2")
    $ add_hook("Bed", "ep213_quests_police7_day1_bed2", scene="police_cell1", label="police_day1", quest="police2")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_75
    return False

label ep213_quests_police6_prisoner1_regular:
    if ep213_quests_prisoner1_offended == True:
        call ep213_dialogues_police15() from _rcall_ep213_dialogues_police15
    else:
        call ep213_dialogues_police16() from _rcall_ep213_dialogues_police16
    return False

label ep213_quests_police7_day1_bed2:
    if act=="l":
        return
    call ep27_dialogues_marcus1_10() from _rcall_ep27_dialogues_marcus1_10
    if _return == True:
        jump ep213_quests_police7_day1_action1
    return False

label ep213_quests_police7_day1_action1:
    if act=="l":
        return
    music2 stop
    if ep213_quests_prisoner == True:
        $ questHelp("marcus_13", True)
        call ep213_dialogues_police8() from _rcall_ep213_dialogues_police8
        call refresh_scene_fade() from _rcall_refresh_scene_fade_76
    else:
        $ questHelp("marcus_13", False)

    $ questHelp("marcus_12", True)
    $ questHelp("marcus_4", True)
    fadeblack
    music stop
    img black_screen
    with Dissolve(2.0)
    $ day += 1
    call textonblack(t_("День 2")) from _rcall_textonblack_49
    $ questHelp("marcus_14")
    img black_screen
    with Dissolve(2.0)

    $ remove_hook(label="police_day1")

    #### ДЕНЬ 2
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police9() from _rcall_ep213_dialogues_police9
        $ prisoner1Cell1Suffix = 3
    else:
        call ep213_dialogues_police9a() from _rcall_ep213_dialogues_police9a

    $ add_hook("cage_interact", "ep213_quests_police9_day2_cage", scene="police", label="police_day2")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_77
    return False

label ep213_quests_police8_cage_prisoners:
    if ep213_quests_prisoner == False or ep213_quests_prisoner1_offended == True:
        return
    music2 stop
    call ep213_dialogues_police18() from _rcall_ep213_dialogues_police18
    call change_scene("police_cell2", "Fade_long") from _rcall_change_scene_111
    return False




label ep213_quests_police9_day2_cage:
    $ remove_hook(label="police_day2")
    music2 stop
    call ep213_dialogues_police9b() from _rcall_ep213_dialogues_police9b
    call ep213_police_marcus_day2() from _rcall_ep213_police_marcus_day2 # Маркус день1

    $ prisoner1Cell1Suffix = 3

    if ep213_quests_prisoner == False: # Если заключенного нет
        $ autorun_to_object("ep213_dialogues_police10b", scene="police_cell1")
    else:
        call ep213_dialogues_police10() from _rcall_ep213_dialogues_police10 # Моника возвращается, заключенный спит

    $ add_hook("Bed", "ep213_quests_police9_day22_bed", scene="police_cell1", label="police_day2", quest="police2")
    call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_112
    return False

label ep213_quests_police9_day22_bed:
    if act=="l":
        return
    music2 stop
    call ep27_dialogues_marcus1_10() from _rcall_ep27_dialogues_marcus1_10_1
    if _return == True:
        # day3 start
        $ questHelp("marcus_14", True)
        fadeblack
        music stop
        img black_screen
        with Dissolve(2.0)
        $ day += 1
        call textonblack(t_("День 3")) from _rcall_textonblack_50
        img black_screen
        with Dissolve(2.0)
        $ questHelp("marcus_15")
        $ remove_hook(label="police_day2")
        $ add_hook("cage_interact", "ep213_quests_police9_day22_cage", scene="police", label="police_day2")
        call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_113

    return False

label ep213_quests_police9_day22_cage:
    $ remove_hook(label="police_day2")
    music2 stop
    call ep213_dialogues_police9b() from _rcall_ep213_dialogues_police9b_1
    call ep213_police_marcus_day3() from _rcall_ep213_police_marcus_day3 # Маркус день2
    $ prisoner1Cell1Suffix = 3
    $ add_hook("Bed", "ep213_quests_police9_day2_bed", scene="police_cell1", label="police_day2", quest="police2")
    call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_114
    call refresh_scene_fade() from _rcall_refresh_scene_fade_78
    return False


label ep213_quests_police9_day2_bed:
    if act=="l":
        return
    music2 stop
    call ep27_dialogues_marcus1_10() from _rcall_ep27_dialogues_marcus1_10_2
    if _return == True:
        call ep213_dialogues_police10c() from _rcall_ep213_dialogues_police10c
        if ep213_quests_prisoner == False or ep213_quests_prisoner1_offended == True:
            jump ep213_quests_police10_day3_start
        $ add_hook("Bed", "ep213_quests_police9_day2_bed2", scene="police_cell1", label="police_day2", quest="police2")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_79
    return False

label ep213_quests_police9_day2_bed2:
    if act=="l":
        return
    music2 stop
    call ep27_dialogues_marcus1_10() from _rcall_ep27_dialogues_marcus1_10_3
    if _return == True:
        call ep213_dialogues_police10d() from _rcall_ep213_dialogues_police10d
        jump ep213_quests_police10_day3_start
    return False

label ep213_quests_police10_day3_start:
    $ questHelp("marcus_15", True)
    music2 stop
    fadeblack
    music stop
    img black_screen
    with Dissolve(2.0)
    $ day += 1
    call textonblack(t_("День 4")) from _rcall_textonblack_51
    img black_screen
    with Dissolve(2.0)
    $ questHelp("marcus_17")
    $ remove_hook(label="police_day2")
    call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_115

    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police11() from _rcall_ep213_dialogues_police11 # Заключенный пихает свой член с утра
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        $ prisoner1Cell1Suffix = 2

    $ add_hook("cage_interact", "ep213_quests_police10_day3_cage", scene="police", label="police_day3", quest="police2")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_80
    return False

label ep213_quests_police10_day3_cage:
    music2 stop
    call ep213_dialogues_police9b() from _rcall_ep213_dialogues_police9b_2
    call ep213_police_marcus_day4() from _rcall_ep213_police_marcus_day4 # Маркус день3
#    $ autorun_to_object("ep213_dialogues_police12", scene="police_cell1")
    call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_116
    $ remove_hook(label="police_day3")
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        $ add_hook("Prisoner1", "ep213_quests_police10_day3_prisoner_bed", scene="police_cell1", label="police_day3", quest="police2")
        $ add_hook("Prisoner1", "ep213_quests_police10_day3_prisoner_bed", scene="police_cell2", label="police_day3", quest="police2")
        if ep213_quests_prisoner1_offended == False:
            $ prisoner1Cell1Suffix = 1
        fadeblack 1.5
        call refresh_scene_fade() from _rcall_refresh_scene_fade_81
        return False

    $ add_hook("Bed", "ep213_quests_police10_day3_prisoner_bed", scene="police_cell1", label="police_day3", quest="police2")
    $ prisoner1Cell1Suffix = 4
    $ autorun_to_object("ep213_dialogues_police12", scene="police_cell1")
    fadeblack 1.5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_82
    return False

label ep213_quests_police10_day3_prisoner_bed: # Клик на заключенного или на кровать
    if act=="l":
        return
    music2 stop
    if obj_name == "Bed":
        call ep27_dialogues_marcus1_10() from _rcall_ep27_dialogues_marcus1_10_4
        if _return == False:
            call refresh_scene_fade() from _rcall_refresh_scene_fade_83
            return False
    $ remove_hook(label="police_day3")
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police12a() from _rcall_ep213_dialogues_police12a
        $ autorun_to_object("ep213_dialogues_police12", scene="police_cell1")
        $ prisoner1Cell1Suffix = 2
    else:
        jump ep213_quests_police11_day4_start

    $ add_hook("Bed", "ep213_quests_police10_day3_bed2", scene="police_cell1", label="police_day3", quest="police2")
    call change_scene("police_cell1", "Fade_long", False) from _rcall_change_scene_117
    fadeblack 1.5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_84
    return False

label ep213_quests_police10_day3_bed2:
    if act=="l":
        return
    music2 stop
    call ep27_dialogues_marcus1_10() from _rcall_ep27_dialogues_marcus1_10_5
    if _return == False:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_85
        return False
    jump ep213_quests_police11_day4_start

label ep213_quests_police11_day4_start:
    $ remove_hook(label="police_day3")
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police12b() from _rcall_ep213_dialogues_police12b
    $ questHelp("marcus_17", True)
    music2 stop
    fadeblack
    img black_screen
    with Dissolve(2.0)
    $ day += 1
    call textonblack(t_("День 5")) from _rcall_textonblack_52
    img black_screen
    with Dissolve(2.0)
    $ questHelp("marcus_19")
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police13() from _rcall_ep213_dialogues_police13
        if ep213_quests_prisoner1_offended == False:
            jump ep213_quests_police11_day4_cageb

    $ add_hook("cage_interact", "ep213_quests_police11_day4_cage", scene="police", label="police_day4", quest="police2")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_86
    return False

label ep213_quests_police11_day4_cage:
    music2 stop
    call ep213_dialogues_police9b() from _rcall_ep213_dialogues_police9b_3
label ep213_quests_police11_day4_cageb:
    music2 stop
    $ questsCompleteByCategory(t_("МАРКУС"))
    $ questHelp("marcus_19", True)
    $ remove_hook(label="police_day4")
    call ep213_police_marcus_day5() from _rcall_ep213_police_marcus_day5 # Маркус день4

    return False

#
