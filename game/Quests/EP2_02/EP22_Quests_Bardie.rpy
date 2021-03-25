default EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = 0

default EP22_Quest_Monica_has_dream = False

label EP22_Quests_Bardie_Monica_Rest_After_Cleaning:
    #Предложение отдыха после уборки
    if bardieBlackmailStage < 4:
        call ep22_dialogues3_1() from _call_ep22_dialogues3_1
    if bardieBlackmailStage == 4:
        call ep22_dialogues3_8() from _call_ep22_dialogues3_8


    $ remove_hook(label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    if bardieBlackmailStage == 0:
        sound highheels_short_walk
        music Groove2_85 high
        call bardie_comment4() from _call_bardie_comment4_3
        if bardieHeardAboutMarcus == True:
            # Барди будет ждать внизу
            $ EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = day
            call EP22_Quests_Bardie_Monica_Blackmail_Stage2_init() from _call_EP22_Quests_Bardie_Monica_Blackmail_Stage2_init

        $ remove_hook(label="bardie_catch_monica_at_stairs_onetime")
        $ autorun_to_object("EP22_Quests_Bardie_Monica_Rest_After_Cleaning_comment1", scene="basement_bedroom2")
        call change_scene("basement_bedroom2") from _call_change_scene_227
        return
    if bardieBlackmailStage == 1:
        call change_scene("basement_bedroom2") from _call_change_scene_228
        call EP22_Quests_Bardie1() from _call_EP22_Quests_Bardie1
        return
    if bardieBlackmailStage == 2:
        call change_scene("basement_bedroom2") from _call_change_scene_229
        call EP22_Quests_Bardie1() from _call_EP22_Quests_Bardie1_1
        return
    if bardieBlackmailStage == 4:
        call change_scene("basement_bedroom2") from _call_change_scene_230
        call EP22_Quests_Bardie5() from _call_EP22_Quests_Bardie5
        $ questHelp("house_9")
        $ questHelpDesc("house_desc4","house_desc5")
        return

#    m "Передых"
    return

label EP22_Quests_Bardie_Monica_Blackmail_Stage2_init:
    $ bardieBlackmailStage = 1
    $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    call Bardie_Life_day2_init() from _call_Bardie_Life_day2_init
    $ bardieFollowMonicaDuringCleaning = False
    $ add_hook("before_open", "EP22_Quests_Bardie1", scene="basement_bedroom2", label="bardie_blackmail_basement")
    return

label EP22_Quests_Bardie_Monica_Rest_After_Cleaning_comment1:
#    mt "Барди..."
#    mt "Он вертится вокруг как назойливая муха!"
#    mt "Надо как-то избавиться от него..."
    return

label EP22_Quests_Bardie1:
    if EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day == day:
        return
    #Барди слышал о Маркусе и идет вниз шантажировать Монику (на следующий день)
    if cloth == "Governess":
        if bardieBlackmailStage == 1:
            $ EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = day
#            $ remove_hook()
            $ remove_hook(label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
            call ep22_dialogues3_2() from _call_ep22_dialogues3_2
            $ questHelp("house_5", True)
            $ questHelp("house_6")
            $ add_hook("basement_monica_after_sleep", "EP22_Quests_Bardie2", scene="global") # Ночью будет сон
            $ add_hook("open", "EP22_Quests_Bardie3", scene="police_entrance") # Днем Барди в полиции
            call refresh_scene_fade() from _call_refresh_scene_fade_80
        if bardieBlackmailStage == 2:
            $ remove_hook()
            $ remove_hook(label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
            call EP22_Quests_Bardie4() from _call_EP22_Quests_Bardie4
            call refresh_scene_fade() from _call_refresh_scene_fade_81
    return

label EP22_Quests_Bardie2: #сон
    $ remove_hook()
    #сон
    call ep22_dialogues3_3() from _call_ep22_dialogues3_3
#    $ unfocus_map()
    $ EP22_Quest_Monica_has_dream = True
    $ focus_map("Teleport_Police", "ep22_dialogues3_3a")
    $ hudDaySkipToEveningEnabled = False
    $ add_hook("basement_monica_before_nap", "ep22_dialogues3_3b", scene="global", label="hurry_to_police")
    $ EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = day
    return

label EP22_Quests_Bardie3: #разговор в полиции
    if EP22_Quest_Monica_has_dream == False:
        return
    $ remove_hook()
    $ remove_hook(label="hurry_to_police")
    call ep22_dialogues3_4() from _call_ep22_dialogues3_4
    $ questHelp("house_6", True)
    $ questHelp("house_7")
    $ autorun_to_object("ep22_dialogues3_5", scene="street_police")
    $ unfocus_map()
    $ hudDaySkipToEveningEnabled = True
    call change_scene("street_police") from _call_change_scene_231
    $ bardieBlackmailStage = 2
    $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    return

label EP22_Quests_Bardie4: #второй разговор с Барди
    call ep22_dialogues3_6() from _call_ep22_dialogues3_6
    $ questHelp("house_7", True)
    $ questHelp("house_8")
    $ questHelp("house_3", True)
    $ questHelpDesc("house_desc2", "house_desc4")
    $ remove_hook("Bardie_Life_day", "Bardie_Life_day3", scene="global")
    $ remove_hook("Bardie_Life_evening", "Bardie_Life_evening2", scene="global")
    $ remove_hook("Bardie_Life_evening", "Bardie_Life_evening3", scene="global")
    $ bardieFollowMonicaDuringCleaning = True
    $ bardieBlackmailStage = 3
    $ questLog(0, False)
    $ questLog(1, True)
    $ char_info["Bardie"]["caption"] = t_("Барди имеет полный доступ к трусикам Моники.")
    $ basement_bedroom2_MonicaSuffix = 2
    $ add_hook("Bardie", "bardie_comment5a", scene="bedroom_bardie")
    $ autorun_to_object("ep22_dialogues3_7", scene="basement_bedroom2")
    return

label EP22_Quests_Bardie4_check_progress:
    if char_info["Bardie"]["level"] == 3 and bardieBlackmailStage == 3:
        $ bardieBlackmailStage = 4
        $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    return


label EP22_Quests_Bardie5: #третий разговор с Барди (трусики Бетти)
    call ep22_dialogues3_9() from _call_ep22_dialogues3_9
    $ monicaMustWearBettyPanties = True
    $ miniMapHousePreset = "laundry"
    $ basement_bedroom2_MonicaSuffix = 2
    $ autorun_to_object("ep22_dialogues3_10", scene="basement_bedroom2")
    $ autorun_to_object("ep22_dialogues3_11", scene="basement_laundry")
    $ autorun_to_object("ep22_dialogues3_11a", scene="bedroom1")
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Laundry1_Monica_[cloth]", "click" : "ep22_dialogues3_11", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="basement_laundry")
    $ add_object_to_scene("Panties_Box", {"type":2, "base":"Basement_Laundry1_Panties_Box", "click" : "EP22_Quests_Bardie6_panties_box", "actions" : "lh", "zorder" : 0, "group":"environment", "active":True}, scene="basement_laundry")
    $ questLog(1, False)
    $ questLog(2, True)
    call basement_bedroom1_init() from _call_basement_bedroom1_init_1
    call basement_bedroom2_init() from _call_basement_bedroom2_init_2
    return

label EP22_Quests_Bardie6_panties_box:
    if act == "l":
        call ep22_dialogues3_11() from _call_ep22_dialogues3_11
        return
    if cloth == "Whore":
        mt "Я не могу одеть никакие трусики под эти кошмарные джинсовые шорты..."
        return
    if cloth == "CasualDress1":
        mt "Я не могу одеть никакие трусики под это платье..."
        return
    if cloth == "SchoolOutfit1":
        mt "Я не могу одеть никакие трусики под эти обтягивающие шорты..."
        return

    $ store_music()
    music Hidden_Agenda
    call ep22_dialogues3_12() from _call_ep22_dialogues3_12 #какие трусики мне надеть?
    if monicaLaundryBettyPantiesSelectMode == 0:
        show screen screen_betty_panties_select()
    if monicaLaundryBettyPantiesSelectMode == 1:
        show screen screen_betty_panties_select2()
    with Dissolve(0.2)
label EP22_Quests_Bardie6_panties_box_loop1:
    $ result = ui.interact()
    if result == -1:
        sound click_denied
        jump EP22_Quests_Bardie6_panties_box_loop1
    if result == 6:
        $ monicaBettyPanties = False
        $ monicaBettyPantiesId = 1
        $ monicaUnder = "Panties"
    else:
        if result == 7:
            $ monicaBettyPanties = False
            $ monicaBettyPantiesId = 1
            $ monicaUnder = "Nude"
        else:
            $ monicaBettyPanties = True
            $ monicaBettyPantiesId = result
            $ monicaUnder = "Panties"

    if monicaLaundryBettyPantiesSelectMode == 0:
        hide screen screen_betty_panties_select
    if monicaLaundryBettyPantiesSelectMode == 1:
        hide screen screen_betty_panties_select2
    call ep22_Act_Images_monica_put_up_panties() from _call_ep22_Act_Images_monica_put_up_panties_1
    $ restore_music()
    call refresh_scene_fade() from _call_refresh_scene_fade_82
    return
