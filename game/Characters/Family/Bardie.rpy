default bardieLocation = "none"
default monicaBardieOffended1 = False
default bardieMonicaCleaningInteractFirstTime = True
default bardieHeardAboutMarcus = False
default bardieBlackmailStage = 0
default bardieFollowMonicaDuringCleaning = True

label bardieInteract1:
    if act == "l":
        mt "Этот маленький оболтус меня бесит!"
        return
    if act == "t":
        if scene_name == "street_house_main_yard":
            if bettyNotFeedingMonicaKitchen == True:
                mt "Надо подождать вечера и придти к нему в комнату."
                return
            call bardie_comment5() from _call_bardie_comment5
            return
        if scene_name == "bedroom_bardie":
            if day_time == "day":
                call bardieDialogue1() from _call_bardieDialogue1
            else:
                call bardie_comment5() from _call_bardie_comment5_1
            return
    return
#        if bardieLocation == "BedroomBardie":
#            call bardieDialogue1()
#            return

#    if bardieLocation == "Floor1" and act == "w":
#        call change_scene("floor1_fountain", "Fade", "snd_fountain")


    return


label bardieMonicaCleaningInteract:
    return
    if act == "l":
        mt "Он так и пытается подкрасться ко мне!"
        "Мне надо быть осторожнее..."
        return False
    if act == "t":
        if bardieMonicaCleaningInteractFirstTime == True:
            $ bardieMonicaCleaningInteractFirstTime = False
#            if char_info["Bardie"]["level"] == 1:
#                $ questLog(0, True)
#                $ questHelp("house_3")
#                $ questHelpDesc("house_desc1", "house_desc2")
        if bardieBlackmailStage < 3:
            if scene_name == "floor1":
                call cleaning_bardie_comment1() from _call_cleaning_bardie_comment1
            if scene_name == "bedroom_bardie":
                call cleaning_bardie_comment2() from _call_cleaning_bardie_comment2
            if scene_name == "bedroom_second":
                call cleaning_bardie_comment3() from _call_cleaning_bardie_comment3
        if bardieBlackmailStage >= 3:
            if scene_name == "floor1":
                call cleaning2_bardie_comment1() from _call_cleaning2_bardie_comment1
            if scene_name == "bedroom_bardie":
                call cleaning2_bardie_comment2() from _call_cleaning2_bardie_comment2
            if scene_name == "bedroom_second":
                call cleaning2_bardie_comment3() from _call_cleaning2_bardie_comment3
        $ move_object("Bardie", "empty")
        $ monicaCleaningObject = "" # Ставим Монику в исходное положение стоя
        if bardieBlackmailStage < 5:
            if bardieBlackmailStage < 2 and char_info["Bardie"]["level"] == 2:
                pass
            else:
                if bardieBlackmailStage == 3:
                    $ add_char_progress("Bardie", bardieCleaningUpskirtTry2, "cleaning_upskirt_day " + str(day))
                    call EP22_Quests_Bardie4_check_progress() from _call_EP22_Quests_Bardie4_check_progress
                else:
                    if bardieBlackmailStage == 4:
    #                    if monicaBettyPantiesId != bettyPantiesLog[1]:
    #                        $ add_char_progress("Bardie", bardieCleaningUpskirtTry3_wrong_panties, "cleaning_upskirt_day " + str(day)) #wrong panties
    #                    else:
                        $ add_char_progress("Bardie", bardieCleaningUpskirtTry3, "cleaning_upskirt_day " + str(day))

                    else:
                        $ add_char_progress("Bardie", bardieCleaningUpskirtTry, "cleaning_upskirt_day " + str(day))
        else:
            call process_hooks("bardie_cleaning_interact_after", "misc") from _call_process_hooks_48

        call refresh_scene_fade() from _call_refresh_scene_fade_20
        return False
    return

label bardieMonicaCleaningInteract_wrong_panties:
    if bardieBlackmailStage >= 5:
        call process_hooks("bardie_cleaning_interact_wrongpanties", "misc") from _call_process_hooks_49
        return
    $ add_char_progress("Bardie", bardieCleaningUpskirtTry3_wrong_panties, "cleaning_upskirt_wrong_panties_day " + str(day))

    return

label bardieProgressLevelUp1:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ add_hook("monica_cleaning_end", "bardieProgressApplyAfterCleaning", scene="global")
        $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
        if ep22_started == False:
            $ char_data["enabled"] = False
            $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
            $ char_data["show_caption_diabled"] = True
#        $ char_data["enabled"] = False #закрываем прогресс до следующей версии
    if char_data["level"] == 3 and bardieBlackmailStage < 3:
        char_data["level"] = char_data["level"] - 1
        char_data["current_progress"] = 90
        $ char_data["show_caption_diabled"] = False
        return
    if char_data["level"] == 3:
        $ questHelp("house_8", True)
#        $ char_data["enabled"] = False
#        $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
#        $ char_data["show_caption_diabled"] = True
#        $ char_data["caption_diabled"] = t_("Work in progress...")
        return
    if char_data["level"] == 4:
        call ep24_quests_bardie1b() from _call_ep24_quests_bardie1b_2
#        $ char_data["enabled"] = False
#        $ char_data["caption_diabled"] = t_("Work in progress...")
    if char_data["level"] == 5:
        if char_info["Betty"]["level"] < 5:
            $ char_data["enabled"] = False
            $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
            $ char_data["show_caption_diabled"] = True
            return
        call ep24_quests_betty5() from _call_ep24_quests_betty5_1
    if char_data["level"] == 6:
        $ char_data["enabled"] = False
        $ char_data["show_caption_diabled"] = False
        $ char_data["caption_diabled"] = t_("Work in progress...")
        help "Уровень Барди максимален для этой версии игры. Ожидайте обновлений!"
        if char_info["Betty"]["level"] >= 6:
            $ questHelp("house_16", True)
    return

label bardieProgressApplyAfterCleaning:
    $ add_hook("Bardie_Life_evening", "Bardie_Life_evening2", scene="global")
    $ add_hook("Bardie", "bardieStairsFloor1Hook1", scene="floor1_stairs", label="bardie_catch_monica_at_stairs") # Диалог с Барди у лестницы
    $ add_hook("Teleport_Basement_Pool", "bardieCatchAtStaitsTeleportPoolHook", scene="floor1_stairs", label="bardie_catch_monica_at_stairs_onetime")
    $ add_hook("mimimap_teleport", "bardieCatchAtStaitsMinimapHook", scene="global", label="bardie_catch_monica_at_stairs_onetime")
    $ remove_hook()
    return


label bardieStairsFloor1Hook1:
    if cloth_type != "Governess":
        bardie "Моника! Покажи трусики!"
        return False
    call bardie_comment4() from _call_bardie_comment4
    $ add_hook("exit_scene", "bardieStairsLeaveOnMonicaLocationExit", scene="floor1_stairs")
    return False

label bardieCatchAtStaitsMinimapHook:
    if target_scene_name == "basement_bedroom2" and get_active_objects("Bardie", scene="floor1_stairs") != False and cloth_type == "Governess":
        call bardie_comment4() from _call_bardie_comment4_1
        call change_scene("floor1_stairs", "Fade", False) from _call_change_scene_39
        $ add_hook("exit_scene", "bardieStairsLeaveOnMonicaLocationExit", scene="floor1_stairs")
        return False
    return True

label bardieCatchAtStaitsTeleportPoolHook:
    if get_active_objects("Bardie", scene="floor1_stairs") != False and cloth_type == "Governess":
        call bardie_comment4() from _call_bardie_comment4_2
        $ add_hook("exit_scene", "bardieStairsLeaveOnMonicaLocationExit", scene="floor1_stairs")
        return False
    return

label bardieStairsLeaveOnMonicaLocationExit:
    $ move_object("Bardie", "bedroom_bardie")
    $ remove_hook()
    return
