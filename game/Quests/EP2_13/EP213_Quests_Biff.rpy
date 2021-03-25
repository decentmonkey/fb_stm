default ep213_quests_biff1_inited = False
default ep213_dialogues4_biff_2_day = 0
default ep213_presentation2_completed_day = 0
label ep213_quests_biff1_init: # инициализация второй презентации
    call ep213_dialogues4_biff_1() from _rcall_ep213_dialogues4_biff_1
    if _return == False:
        $ questHelp("office_43", False)
        $ questHelp("office_44", False)
#        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
#        call change_scene("street_monica_office", "Fade_long")
        return
    $ questHelp("office_43", True)
    $ questHelp("office_44")
    $ ep213_quests_biff1_inited = True
    $ add_hook("Biff", "ep213_quests_biff2_biff", scene="monica_office_cabinet_table", label=["monica_presentation2", "evening_time_temp"])
    $ ep213_dialogues4_biff_2_day = day
    $ add_hook("enter_scene", "ep213_dialogues4_biff_2", scene="monica_office_entrance", label="monica_presentation2")
    $ add_hook("before_open", "ep213_quests_biff3_presentation", scene="monica_office_cabinet", label="monica_presentation2")
    $ add_hook("before_open", "ep213_quests_biff3_presentation", scene="monica_office_cabinet_table", label="monica_presentation2")
    return False

label ep213_quests_biff2_biff:
    if act=="l":
        return
    call ep213_dialogues4_biff_1b() from _rcall_ep213_dialogues4_biff_1b
    return False

label ep213_quests_biff3_presentation:
    # перезентация
    if ep213_dialogues4_biff_2_day == day or day_time != "evening":
        return
    call ep213_dialogues4_biff_3() from _rcall_ep213_dialogues4_biff_3
    $ questHelp("office_44", True)
    $ questHelp("photoshoot_14")
#    $ questHelpDesc("photoshoot_desc14")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ miniMapEnabledOnly = ["Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("AlexPhotograph", "ep213_quests_biff4_Alex", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_hook("Teleport_Monica_Office_MakeupRoom", "ep213_quests_biff5_makeup_room", scene="monica_office_photostudio", label="monica_presentation2")

    $ add_objective("go_photostudio", t_("Идти в фотостудию и провести фотосессию."), c_orange, 115)
    $ autorun_to_object("ep213_dialogues4_biff_4", scene="monica_office_secretary")
    call change_scene("monica_office_secretary", "Fade_long") from _rcall_change_scene_89
    return False

label ep213_quests_biff4_Alex:
    if act=="l":
        return
    call ep213_dialogues4_biff_5() from _rcall_ep213_dialogues4_biff_5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_62
    return False

label ep213_quests_biff5_makeup_room:
    call ep213_dialogues4_biff_6() from _rcall_ep213_dialogues4_biff_6
    if _return == False:
        $ miniMapEnabledOnly = []
        call putoff_work_clothes() from _rcall_putoff_work_clothes_6
        $ remove_hook(label="monica_presentation2")
        $ remove_hook(label="presentation2_block")
        $ remove_objective("go_photostudio")
        $ questHelp("photoshoot_14", False)
        $ add_hook("Biff", "ep213_quests_biff6_biff_repeat", scene="monica_office_cabinet_table", label="monica_presentation2") # Повторный разговор с Бифом о работе
        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_90
        return False
    # фотосессия
    call ep213_photoshoot10() from _rcall_ep213_photoshoot10_1
    if _return == False:
        $ remove_hook(label="monica_presentation2")
        $ remove_hook(label="presentation2_block")
        $ remove_objective("go_photostudio")
        $ questHelp("photoshoot_14", False)
        $ add_hook("Biff", "ep213_quests_biff8_repeat2", scene="monica_office_cabinet_table", label="monica_presentation2")
        $ miniMapEnabledOnly = []
        call putoff_work_clothes() from _rcall_putoff_work_clothes_7
        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
        fadeblack 2.0
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_91
        return False

label ep213_quests_biff5_makeup_room_photoshoot_completed:
#    $ miniMapEnabledOnly = []
    $ ep213_presentation2_completed_day = day
    $ questHelp("photoshoot_14", True)
    $ questHelp("photoshoot_14a", skipIfExists=True)
    $ questHelp("office_45b", skipIfExists=True)
    $ questHelp("office_45", skipIfExists=True)
#    $ questHelp("office_45a", skipIfExists=True)
    $ monicaOutfitsEnabled[9] = True # активируем регулярную фотосессию
    call ep215_quests_workers1_init() from _rcall_ep215_quests_workers1_init
    $ remove_hook(label="monica_presentation2")
    $ remove_hook(label="presentation2_block")
    $ remove_objective("go_photostudio")
    fadeblack 2.0
    $ autorun_to_object("ep213_dialogues4_biff_11", scene="street_monica_office")
    $ add_hook("Biff", "ep22_quests_office6", scene="monica_office_cabinet_table", label="photoshoot") #Мне надо получить деньги от Бифа
    $ add_hook("Biff", "ep213_quests_biff7_biff_after_photoshoot", scene="monica_office_cabinet_table", label="monica_presentation2")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_dialogue6_7a", scene="monica_office_secretary", label="photoshoot", priority = 105) #Блокируем выход пока не получили деньги от Бифа
    call change_scene("monica_office_cabinet", "Fade_long") from _rcall_change_scene_92
    return False

label ep213_quests_biff6_biff_repeat: # Повторный разговор с Бифом о работе
    if act=="l":
        return
    call ep213_dialogues5_photoshoot_7() from _rcall_ep213_dialogues5_photoshoot_7
    if _return == False:
        $ miniMapEnabledOnly = []
        call putoff_work_clothes() from _rcall_putoff_work_clothes_8
        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_93
        return False
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ miniMapEnabledOnly = ["Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("AlexPhotograph", "ep213_quests_biff4_Alex", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_hook("Teleport_Monica_Office_MakeupRoom", "ep213_quests_biff5_makeup_room", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_objective("go_photostudio", t_("Идти в фотостудию и провести фотосессию."), c_orange, 115)
    call change_scene("monica_office_secretary", "Fade_long") from _rcall_change_scene_94

    return False


label ep213_quests_biff7_biff_after_photoshoot:
    if act=="l":
        return
    $ remove_hook()
    call ep213_dialogues4_biff_10() from _rcall_ep213_dialogues4_biff_10
    $ miniMapEnabledOnly = []
    return

label ep213_quests_biff8_repeat2: # Повторный приход для завершения фотосессии
    if act=="l":
        return
    call ep211_dialogues3_photoshoot_9() from _rcall_ep211_dialogues3_photoshoot_9
    if _return == False:
        call putoff_work_clothes() from _rcall_putoff_work_clothes_9
        fadeblack 2.0
        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_95
        return False

    $ remove_hook()
    call ep213_photoshoot10_repeat_end() from _rcall_ep213_photoshoot10_repeat_end
    jump ep213_quests_biff5_makeup_room_photoshoot_completed
