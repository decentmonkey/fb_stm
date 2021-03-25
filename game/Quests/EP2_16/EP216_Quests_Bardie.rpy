default ep216_quests_bardie_completed_day = 0
default ep216_quests_bardie_completed_webcam_day = 0

default ep216_quests_bardie_catch_active = False

label ep216_quests_bardie_check_init:
    return
    if int(ep216_quests_bardie_completed_day/7) < int(day/7) and monicaBardieRalphSeducingStage >= 6:
        if check_hook(label="ep216_quests_bardie_catch_after_cleaning", scene="global") == False and check_hook(label="ep216_quests_bardie3_enter_room", scene="floor2") == False:
            $ add_hook("monica_cleaning_end", "ep216_quests_bardie2_catch", scene="global")
        $ ep216_quests_bardie_catch_active = True
    return


label ep216_quests_bardie2_catch: # Барди перехватывает Монику
    if ep216_quests_bardie_catch_active == True:
        $ ep216_quests_bardie_catch_active = False
        if day_time != "day":
            return
    #    $ remove_hook(label="ep216_quests_bardie2_catch")
        $ restore_music()
        call ep216_dialogues1_bardie_1() from _rcall_ep216_dialogues1_bardie_1
        # Инициализация похода к Барди
        $ autorun_to_object("ep216_dialogues1_bardie_1b", scene="basement_bedroom2")
    #    $ add_hook("basement_monica_after_nap_dialogue", "dialogue_classmate_1b", scene="global", once=True)
        $ add_objective("go_to_bardie", t_("Идти к Барди в комнату вечером"), c_orange, 85)
        $ add_hook("Teleport_BedroomBardie", "ep216_quests_bardie3_enter_room", scene="floor2", label="ep216_quests_bardie3_enter_room")

        call change_scene("basement_bedroom2", "Fade_long") from _rcall_change_scene_185

    return


label ep216_quests_bardie3_enter_room:
    if day_time == "day":
        return

    $ remove_objective("go_to_bardie")
    call ep216_dialogues1_bardie_1c() from _rcall_ep216_dialogues1_bardie_1c
    if _return == False: #Моника убежала
        $ remove_hook(label="ep216_quests_bardie3_enter_room")
        $ questHelp("house_41", False)
        $ autorun_to_object("ep216_dialogues1_bardie_2", scene="floor2")
        call change_scene("floor2", "Fade_long") from _rcall_change_scene_186
        return False
#    if questHelpFlag5 == False:
#        $ questHelpFlag5 = True
    $ questHelp("house_41", True)
    if _return == 2: # Отдала деньги
        $ remove_hook(label="ep216_quests_bardie3_enter_room")
        $ remove_objective("go_to_bardie")
        $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["monica_bardie_meeting_block_room", "evening_time_temp"]) # блокируем вход к Барди до утра
        $ ep216_quests_bardie_completed_day = day
        $ autorun_to_object("ep216_dialogues1_bardie_3", scene="floor2")
        call change_scene("floor2", "Fade_long") from _rcall_change_scene_187
        return False
    if _return == True:
        $ remove_hook(label="ep216_quests_bardie3_enter_room")
        $ remove_objective("go_to_bardie")
        $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["monica_bardie_meeting_block_room", "evening_time_temp"]) # блокируем вход к Барди до утра
        $ ep216_quests_bardie_completed_day = day
        $ ep216_quests_bardie_completed_webcam_day = day
        $ ep216_quests_bardie_completed_day = day
        $ autorun_to_object("ep216_dialogues1_bardie_4", scene="floor2")
        $ add_corruption(20, "ep216_quests_bardie3_webcam" + str(day))
        call change_scene("floor2", "Fade_long") from _rcall_change_scene_188

    return False





























#
