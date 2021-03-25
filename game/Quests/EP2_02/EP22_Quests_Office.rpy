label ep22_quests_office_init:
    $ biffDisabled = True
    if monkeysOffended2 == True:
        $ biffMonicaCastingsEnabled = True
#        $ notif(t_("Моника заставляла моделей проходить обнаженный кастинг"))
    $ add_hook_day("ep22_quests_office2", week_day = 6, label="photoshoot_regular") #Обновляем возможность фотосессии раз в неделю по субботам
    $ add_hook("Biff", "ep22_quests_office1", scene="monica_office_cabinet_table")
    $ add_hook("AlexPhotograph", "ep22_quests_office3", scene="monica_office_photostudio", label="photoshoot_regular")
    return

label ep22_quests_office1: #регулярный разговор с Бифом на работе
    if act=="l":
        return
    if monicaOutfitsEnabled[7] == True and monicaWorkingAtBiffOffice == True and ep22_quests_biff_init_flag == False and photoshoot8_count > 0: # Если Моника открыла костюм и если работает в офисе и если хотя бы раз сделала фотосессию черный лебедь
        call ep22_quests_biff_init() from _rcall_ep22_quests_biff_init # Инициализируем разговор о первой презентации
        call change_scene("monica_office_cabinet") from _rcall_change_scene
        return

    call ep22_dialogue6_3() from _call_ep22_dialogue6_3
    if _return == False:
        call change_scene("monica_office_cabinet") from _call_change_scene_207
#        call refresh_scene_fade()
        return

#    if questHelpFlag6Noir == False:
    $ questHelp("photoshoot_2", skipIfExists=True)
    $ questHelp("photoshoot_3", skipIfExists=True)
    # Инициализируем фотосессию
    $ move_object("AlexPhotograph", "monica_office_photostudio")
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока идет фотосессия
    $ add_hook("AlexPhotograph", "ep22_quests_office4", scene="monica_office_photostudio", label="photoshoot_alex") # Алекс стартует фотосессию
    $ add_hook("Biff", "ep22_quests_office5", scene="monica_office_cabinet_table", label="photoshoot") # Мне надо идти в фотостудию, блок на Биффа
    call refresh_scene_fade() from _call_refresh_scene_fade_66
    return

label ep22_quests_office2: # Обновляем возможность фотосессии раз в неделю
    $ biffWeeklyPhotoShootEnabled = True
    return
label ep22_quests_office3: # Регулярный разговор с Алексом
    if act=="l":
        return
    call ep22_dialogue6_4() from _call_ep22_dialogue6_4
    call refresh_scene_fade() from _call_refresh_scene_fade_67
    return False
label ep22_quests_office4: # Алекс стартует фотосессию
    if act == "l":
        return
#    $ monicaPhotoShootOutfitIdx = 1
#    jump ep22_quests_office4_l1
    call ep22_dialogue6_5() from _call_ep22_dialogue6_5
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_68
        return False
    $ monicaPhotoShootInProgress = True
    # Выбор наряда
    label ep22_quests_office4_loop1:
#        img scene_Office_Monica_MakeupRoom
        call biffInitOutfitIcons() from _call_biffInitOutfitIcons
        show screen choose_photoshoot_outfit()
        with Dissolve(0.2)
        $ result = ui.interact()
        if result == -1:
            sound click_denied
            jump ep22_quests_office4_loop1
        $ monicaPhotoShootOutfitIdx = result + 1
        sound click1
        hide screen choose_photoshoot_outfit

    call ep22_dialogue6_5a() from _call_ep22_dialogue6_5a

label ep22_quests_office4_l1:
    if monicaPhotoShootOutfitIdx == 1:
        call ep22_photoshoot1() from _call_ep22_photoshoot1_1
        call ep22_photoshoot1_end() from _call_ep22_photoshoot1_end
        $ photoshoot1_count += 1
    if monicaPhotoShootOutfitIdx == 2:
        if questHelpFlag6Noir == False:
            $ questHelpFlag6Noir = True
            $ questHelp("photoshoot_2", True)
        call ep22_photoshoot2() from _call_ep22_photoshoot2
        call ep22_photoshoot2_end() from _call_ep22_photoshoot2_end
        $ photoshoot2_count += 1
        if monicaSecretaryOutfit1EnforcementPlanned == False: # После фотосессии в костюме #2 планируем переодевание секретарши
            $ monicaSecretaryOutfit1EnforcementPlanned = True
            $ add_hook("before_open", "ep22_quests_office9", scene="monica_office_secretary") # Планируем инициализацию outfit1 для секретарши
    if monicaPhotoShootOutfitIdx == 3:
        call ep22_photoshoot3() from _call_ep22_photoshoot3
        call ep22_photoshoot3_end() from _call_ep22_photoshoot3_end
        $ photoshoot3_count += 1
        if questHelpFlag7Worker == False:
            $ questHelpFlag7Worker = True
            $ questHelp("photoshoot_3", True)
#            $ questHelp("office_16")
    if monicaPhotoShootOutfitIdx == 4:
        call ep22_photoshoot4() from _call_ep22_photoshoot4
        call ep22_photoshoot4_end() from _call_ep22_photoshoot4_end
        if melanieWaitingOpenedOutfits == True:
            $ monicaOutfitsEnabled[4] = True # Открываем следующий костюм (Мелани)
            $ melanieWaitingOpenedOutfits = False
            $ questHelp("melanie_1a", True)
            $ questHelp("photoshoot_4")
        $ photoshoot4_count += 1
    if monicaPhotoShootOutfitIdx == 5:
        call ep23_dialogues5_3() from _call_ep23_dialogues5_3
        call ep22_photoshoot5_end() from _call_ep22_photoshoot5_end
        $ photoshoot5_count += 1
    if monicaPhotoShootOutfitIdx == 6:
        call ep26_photoshoot_suit6() from _call_ep26_photoshoot_suit6
        call ep26_photoshoot_suit6_end() from _call_ep26_photoshoot_suit6_end
        $ monicaOutfitsEnabled[6] = True # Открываем следующий костюм
        $ questHelp("photoshoot_6", skipIfExists=True)
        call ep26_quests_biff1() from _call_ep26_quests_biff1 # Инициализируем разговор о работе в офисе + возвращение Мелани
        $ photoshoot6_count += 1
    if monicaPhotoShootOutfitIdx == 7:
        call ep26_photoshoot_suit7() from _call_ep26_photoshoot_suit7
        call ep26_photoshoot_suit7_end() from _call_ep26_photoshoot_suit7_end
        $ photoshoot7_count += 1
        $ questHelp("photoshoot_7", skipIfExists=True)
        $ monicaOutfitsEnabled[7] = True # Открываем следующий костюм
    if monicaPhotoShootOutfitIdx == 8:
        call ep27_photoshoot_suit8() from _call_ep27_photoshoot_suit8
        if _return == False:
            img black_screen
            with Dissolve(1.0)
            pause 1.5
            img 20594
            with fadelong
            jump ep22_quests_office4_loop1
        call ep27_photoshoot_suit8_end() from _call_ep27_photoshoot_suit8_end
        $ photoshoot8_count += 1
    if monicaPhotoShootOutfitIdx == 9:
        if ep211_quests_photoshoot_stage == 1:
            jump ep211_quests_publicevent2_photoshoot2
        if ep211_quests_photoshoot_stage == 2:
            jump ep211_quests_publicevent2_photoshoot3
        if ep211_quests_photoshoot_stage == 3:
            call ep211_dialogues3_photoshoot_6() from _rcall_ep211_dialogues3_photoshoot_6 # фотосессия
            call ep211_dialogues3_photoshoot_7() from _rcall_ep211_dialogues3_photoshoot_7
            if _return == 0:
                $ monicaPhotoShootInProgress = False
                $ monicaOutfitsAltEnabled = False
                $ miniMapEnabledOnly = []
                $ autorun_to_object("ep211_dialogues3_photoshoot_4b", scene="street_monica_office")
                $ remove_hook(label="photoshoot")
                $ remove_hook(label="photoshoot_alex")
                call putoff_work_clothes() from _rcall_putoff_work_clothes
                call change_scene("street_monica_office", "Fade_long", False) from _rcall_change_scene_1
                return False
#        $ monicaOutfitsEnabled[8] = True # Открываем следующий костюм
    if monicaPhotoShootOutfitIdx == 10:
        call ep213_photoshoot10() from _rcall_ep213_photoshoot10
        $ photoshoot10_count += 1
    if ep216_office_blocked_day >= day:
        return False
    #конец фотосессии
    sound snd_fabric1
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    $ remove_hook(label="photoshoot_alex")
    $ add_hook("Biff", "ep22_quests_office6", scene="monica_office_cabinet_table", label="photoshoot") #Мне надо получить деньги от Бифа
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_dialogue6_7a", scene="monica_office_secretary", label="photoshoot", priority = 105) #Блокируем выход пока не получили деньги от Бифа
    call change_scene("monica_office_cabinet", "Fade_long") from _call_change_scene_208
    return False
label ep22_quests_office5: # Мне надо идти в фотостудию, блок на Биффа
    if act=="l":
        return
    call monica_office_secretary_dialogue6() from _call_monica_office_secretary_dialogue6
    return False

label ep22_quests_office6: #Биф, где мои деньги?
    if act=="l":
        return
    call ep22_dialogue6_7() from _call_ep22_dialogue6_7
    if _return == True:
        if monicaPhotoShootOutfitIdx == 1:
            $ add_char_progress("Biff", PS1_BiffProgress, "PS1_BiffProgress_day" + str(day))
        if monicaPhotoShootOutfitIdx == 2:
            $ add_char_progress("Biff", PS2_BiffProgress, "PS2_BiffProgress_day" + str(day))
        if monicaPhotoShootOutfitIdx == 3:
            $ add_char_progress("Biff", PS3_BiffProgress, "PS3_BiffProgress_day" + str(day))

    if questHelpFlag9 == False:
        $ questHelpFlag9 = True
        $ questHelp("office_14", True)
        $ questHelp("office_15")
        $ questHelpDesc("office_desc7", "office_desc8")
        $ questHelp("office_16", True)


    if monicaBiffFirstPhotoShoot == True:
        $ monicaBiffFirstPhotoShoot = False
        $ questLog(8, True)
    $ biffWeeklyPhotoShootEnabled = False
    $ monicaPhotoShootInProgress = False
    $ remove_objective("money_for_victoria")
    $ remove_hook(label="photoshoot")
    call change_scene("monica_office_secretary", "Fade_long") from _call_change_scene_209
    return False

label ep22_quests_office7: #enable Biff
    $ biffDisabled = False
    $ biffOnlyFridayEvening = False
    $ add_hook("Secretary", "ep22_quests_office8a", scene="monica_office_secretary", label="secretary_last_request")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep22_quests_office8", scene="monica_office_secretary", label="secretary_last_request")
    return
label ep22_quests_office8a:
    if act=="l":
        return
    jump ep22_quests_office8
label ep22_quests_office8: # Последний раз секретарша просит о помощи
    call monica_office_secretary_dialogue3() from _call_monica_office_secretary_dialogue3_1
    $ remove_hook(label="secretary_last_request")
    call refresh_scene_fade() from _call_refresh_scene_fade_69
    return False
label ep22_quests_office9:
    if biffWeeklyPhotoShootEnabled == False or day_time != "evening":
        return
    $ remove_hook()
    # инициализируем outfit1 на секретарше
    $ monicaOfficeSecretarySecretarySuffix = 4
    $ remove_hook("Secretary", "monica_office_secretary_dialogue2", scene="monica_office_secretary")
    $ add_hook("Secretary", "ep22_quests_office12", scene="monica_office_secretary", label="secretary_regular_talk")
    $ add_hook("Secretary", "ep22_quests_office10", scene="monica_office_secretary", label="secretary_last_request")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep22_quests_office11", scene="monica_office_secretary", label="secretary_last_request")
    $ replace_hook("ep22_dialogue6_2b", scene="monica_office_secretary", label="check_bill_at_place")
    return
label ep22_quests_office10: # Последний запрос о помощи со стороны секретарши
    if act=="l":
        return
    call ep22_dialogue6_1() from _call_ep22_dialogue6_1
    $ remove_hook(label="secretary_last_request")
    call refresh_scene_fade() from _call_refresh_scene_fade_70
    return False
label ep22_quests_office11:
    call ep22_dialogue6_1() from _call_ep22_dialogue6_1_1
    $ remove_hook(label="secretary_last_request")
    call refresh_scene_fade() from _call_refresh_scene_fade_71
    return False
label ep22_quests_office12: # Регулярный разговор с секретаршей
    if act=="l":
        call ep22_dialogue6_2a() from _call_ep22_dialogue6_2a
        return False
    call ep22_dialogue6_2() from _call_ep22_dialogue6_2
    call refresh_scene_fade() from _call_refresh_scene_fade_72
    return False


label ep22_quests_office13:
    return
label ep22_quests_office14:
    return
label ep22_quests_office15:
    return
