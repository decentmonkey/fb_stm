default ep213_quests_pub1_inited = False
default ep213_quests_pub2_day = 0
default ep213_quests_stole_tips_count = 0
default ep213_quests_molly_earning_tips = True # Молли зарабатывает чаевые и кладет их в банку
default ep213_quests_monica_punished_for_stealing_molly_tips = False
default ep213_quests_monica_punished_for_stealing_molly_tips_day = 0

default ep213_quests_pub9_claire_complete = False
default ep213_quests_pub10_molly_complete = False

label ep213_quests_pub1:
    if ep29_quests_dancing_with_claire_last_day > 0 and pubPrivate1Count > 0: # при условии, что были приваты перед банкиром и клиентом паба и Моника хотя бы раз станцевала в паре с Клэр
        $ questHelp("shinyhole_32", skipIfExists=True)
        $ add_hook("before_open", "ep213_quests_pub2", scene="pub_makeuproom", label="ep213_pub")
        $ ep213_quests_pub1_inited = True
    return


label ep213_quests_pub2: # Моника приходит на работу в паб и заходит в гримерку
#    if ep213_quests_pub2_day != 0 and day - ep213_quests_pub2_day < 6: # Если игнорили, повтор через неделю
#        return
    if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False:
        return
    $ remove_hook()
    call ep213_dialogues3_pub_1() from _rcall_ep213_dialogues3_pub_1
    $ pub_makeuproom_monica_suffix = 2
    if _return == False:
        $ ep213_quests_pub2_day = day
        $ add_hook("Pub_StripteaseGirl1", "ep213_quests_pub2_molly", scene="pub_makeuproom", label="ep213_pub")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_87
        return False
    $ questHelp("shinyhole_32", True)
    $ questHelp("shinyhole_34", skipIfExists=True)
    $ questHelpDesc("shinyhole_desc12", False)
    $ remove_hook(label="ep213_pub")
    $ add_hook("Pub_StripteaseGirl1", "ep213_quests_pub3_molly_refuse", scene="pub_makeuproom", label="ep213_pub")
    $ add_hook("Teleport_Pub", "ep213_quests_pub4", scene="pub_makeuproom", label="ep213_pub")
    return False

label ep213_quests_pub2_molly: # повтор диалога с Молли по клику на нее
    if act=="l":
        return
    call ep213_quests_pub2() from _rcall_ep213_quests_pub2
    return False

label ep213_quests_pub3_molly_refuse:
    if act=="l":
        return
    call ep213_dialogues3_pub_2() from _rcall_ep213_dialogues3_pub_2
    return False

label ep213_quests_pub4: # гримерка, в этот же день после сцены
    if monicaDancedLastDay != day or cloth_type != "Whore":
        return
    call ep213_dialogues3_pub_3() from _rcall_ep213_dialogues3_pub_3
    if _return == False:
        $ questHelp("shinyhole_34", False)
        return
    $ remove_hook(label="ep213_pub")
    call pub_makeuproom_init4() from _rcall_pub_makeuproom_init4 # инициализируем чаевые
    call locations_init_pub_makeuptoom_mollytable() from _rcall_locations_init_pub_makeuptoom_mollytable
    $ add_hook("Teleport_Pub_MakeupRoom", "ep213_dialogues3_pub_3c", scene="pub_makeuproom_mollytable", label="ep213_pub_block")
    call change_scene("pub_makeuproom_mollytable", "Fade_long") from _rcall_change_scene_118
    $ add_hook("Tips", "ep213_quests_pub5_tips", scene="pub_makeuproom_mollytable", label="ep213_pub")
    return False

label ep213_quests_pub5_tips:
    if act=="l":
        call ep213_dialogues3_pub_3a() from _rcall_ep213_dialogues3_pub_3a
        return False
    $ questHelp("shinyhole_34", True)
    $ questHelp("shinyhole_34a", skipIfExists=True)
    $ ep213_quests_stole_tips_count +=1
    if ep213_quests_stole_tips_count == 1: # воруем первый раз
        $ remove_hook(label="ep213_pub_block")
        call ep213_dialogues3_pub_3b() from _rcall_ep213_dialogues3_pub_3b
        $ set_active("Tips", False)
        $ set_active("Tips", False, scene="pub_makeuproom")
        $ set_active("Teleport_Pub_MakeupRoom", True, scene="pub_makeuproom_mollytable")
        $ add_hook("TableMolly", "ep213_quests_pub6_tablemolly", scene="pub_makeuproom", label="ep213_pub_teleport_mollytable")
        $ add_hook("Tips", "ep213_quests_pub6_tablemolly", scene="pub_makeuproom", label="ep213_pub_teleport_mollytable")
        call change_scene("pub_makeuproom") from _rcall_change_scene_119
        return False
    if ep213_quests_stole_tips_count == 2:
        $ questHelp("shinyhole_34a", True)
        $ questHelp("shinyhole_36", skipIfExists=True)
        if cloth_type != "Whore":
            sound snd_fabric1
            fadeblack 2.0
            $ cloth = "Whore"
            $ cloth_type = "Whore"
        call ep213_dialogues3_pub_4a() from _rcall_ep213_dialogues3_pub_4a
        if _return == False:
            $ ep213_quests_stole_tips_count -=1
        $ set_active("Tips", False)
        $ set_active("Tips", False, scene="pub_makeuproom")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_88
        return False
    if ep213_quests_stole_tips_count == 3:
        if cloth_type != "Whore":
            sound snd_fabric1
            fadeblack 2.0
            $ cloth = "Whore"
            $ cloth_type = "Whore"
        call ep213_dialogues3_pub_4() from _rcall_ep213_dialogues3_pub_4
        if _return == False:
            $ ep213_quests_stole_tips_count -=1
            call refresh_scene_fade() from _rcall_refresh_scene_fade_89
            return False

        $ questHelp("shinyhole_36", True)
        $ questHelp("shinyhole_43", skipIfExists=True)



#        $ set_active("Tips", False)
#        $ set_active("Tips", False, scene="pub_makeuproom")
        $ ep213_quests_monica_punished_for_stealing_molly_tips = True
        $ ep213_quests_monica_punished_for_stealing_molly_tips_day = day
        $ stage_low_tips = True
        $ add_hook("Pub_StripteaseGirl1", "ep213_quests_pub7_molly_punishment", scene="pub_makeuproom", label="ep213_pub")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_90
        return False

    if ep213_quests_stole_tips_count == 4:
        $ ep213_quests_stole_tips_count -= 1
        call ep213_dialogues3_pub_5a() from _rcall_ep213_dialogues3_pub_5a
        return False

    return False

label ep213_quests_pub6_tablemolly:
    if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") != False or get_active_objects("Pub_StripteaseGirl2", scene="pub_makeuproom") != False:
        call ep213_dialogues3_pub_2a() from _rcall_ep213_dialogues3_pub_2a
        call refresh_scene_fade() from _rcall_refresh_scene_fade_91
        return False
    call change_scene("pub_makeuproom_mollytable", "Fade_long") from _rcall_change_scene_120
    return False

label ep213_quests_pub7_molly_punishment: # Моника разговаривает с Молли после объявления ей наказания от Эшли
    if act=="l":
        return
    call ep213_dialogues3_pub_6() from _rcall_ep213_dialogues3_pub_6
    if _return == 0: # отказалась мириться
        $ questHelp("shinyhole_43", False)
        call refresh_scene_fade() from _rcall_refresh_scene_fade_92
        return False
    if _return == 1: # увольнение
        $ questHelp("shinyhole_43", False)
        call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_4
        return False
    $ questHelp("shinyhole_43", True)
    $ questHelp("shinyhole_44")
    $ remove_hook()
    $ add_hook("Pub_StripteaseGirl1", "ep213_quests_pub3_molly_refuse", scene="pub_makeuproom", label="ep213_pub")
    $ ep213_dialogues3_pub_7_planned = True
    call refresh_scene_fade() from _rcall_refresh_scene_fade_93
    return False


label ep213_quests_pub8_first_dance_nude: # вызывается при первом танце обнаженной
    $ pubDanceAfterBlockEvents = True # нет других событий после первого танца
    $ ep213_dialogues3_pub_12_planned = True
    $ add_hook("enter_scene", "ep213_dialogues3_pub_11", scene="pub_makeuproom", label="ep213_pub", once=True, priority= 1000)
    $ questLog(75, True)
    $ add_hook("Pub_StripteaseGirl1", "ep213_quests_pub10_molly", scene="pub_makeuproom", label="ep213_pub")
    $ add_hook("Pub_StripteaseGirl2", "ep213_quests_pub9_claire", scene="pub_makeuproom", label="ep213_pub")
    return

label ep213_quests_pub9_claire: # разговор с Клэр после танца
    if act=="l":
        return
    $ remove_hook()
    call ep213_dialogues3_pub_13() from _rcall_ep213_dialogues3_pub_13
    $ ep213_quests_pub9_claire_complete = True
    $ questHelp("shinyhole_44c", True)
    if pubPrivate2Count < 1 or ep214_quests_pub1_check_inited_flag == True or dancePrivateLastDay == day or monicaDancedLastDay == day or ep211_quests_photoshot8_opened_day == 0 or ep213_quests_pub10_molly_complete == False or ep213_quests_pub9_claire_complete == False:
        pass
    else:
        $ questHelp("shinyhole_37", skipIfExists=True)
    $ add_char_progress("Pub_StripteaseGirl2", 25, "molly_punishment_nude_claire_help_offer")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_94
    return False

label ep213_quests_pub10_molly: # разговор с Молли после танца
    if act=="l":
        return
    $ remove_hook()
    call ep213_dialogues3_pub_14() from _rcall_ep213_dialogues3_pub_14
    $ ep213_quests_pub10_molly_complete = True
    $ questHelp("shinyhole_44b", True)
    if pubPrivate2Count < 1 or ep214_quests_pub1_check_inited_flag == True or dancePrivateLastDay == day or monicaDancedLastDay == day or ep211_quests_photoshot8_opened_day == 0 or ep213_quests_pub10_molly_complete == False or ep213_quests_pub9_claire_complete == False:
        pass
    else:
        $ questHelp("shinyhole_37", skipIfExists=True)
        $ ep214_quests_activated_alt_day = day
    if _return == False: # увольнение
        call ep211_quests_pub3_fired() from _rcall_ep211_quests_pub3_fired_5
        return False
    $ add_char_progress("Pub_StripteaseGirl1", 25, "molly_punishment_nude")
    $ pub_makeuproom_monica_suffix = 2
    call refresh_scene_fade() from _rcall_refresh_scene_fade_95
    return False

label ep213_quests_pub_private2_1:
    if cloth_type != "StripOutfit":
        call ep211_dialogues5_shiny_hole_8() from _rcall_ep211_dialogues5_shiny_hole_8_2
        return False
    # сцена
    $ remove_objective("go_dance_private")
    $ remove_hook(label="pub_private_dance1")
    $ dancePrivateLastDay = day
    call ep213_dialogues3_pub_16() from _rcall_ep213_dialogues3_pub_16
    if _return == -1:
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_18
        return
    $ questHelp("shinyhole_35", True)

    if pubPrivate2Count < 1 or ep214_quests_pub1_check_inited_flag == True or dancePrivateLastDay == day or monicaDancedLastDay == day or ep211_quests_photoshot8_opened_day == 0 or ep213_quests_pub10_molly_complete == False or ep213_quests_pub9_claire_complete == False:
        pass
    else:
        $ questHelp("shinyhole_37", skipIfExists=True)
        $ ep214_quests_activated_alt_day = day
    $ pubPrivate2Count += 1

    $ customer9_after_private = True
    $ questHelp("shinyhole_58b", skipIfExists=True)
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_19
    return
