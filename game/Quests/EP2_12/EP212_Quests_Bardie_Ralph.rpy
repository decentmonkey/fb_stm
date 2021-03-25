default monicaCollege1FinishedDay = 0
default monicaBardieRalphSeducingStage = 0
default monicaBardieRalphSeducingCleaningItemsCount = 0
default monicaBardieRalphSeducingCleaningCompletedToday = False

label ep212_quests_bardie_ralph1:
    $ add_hook("monica_cleaning_end", "ep212_quests_bardie_ralph2", scene="global", label="ep212_quests_bardie_ralph1")
    return

label ep212_quests_bardie_ralph2: # Барди перехватывает Монику после уборки
    $ remove_hook()
    $ restore_music()
    call ep212_dialogues1_bardie_ralph1() from _rcall_ep212_dialogues1_bardie_ralph1
    call ep212_dialogues1_bardie_ralph2() from _rcall_ep212_dialogues1_bardie_ralph2


    $ questHelp("house_30", True)
    $ questHelp("house_31")
    $ questHelpDesc("house_desc14", "house_desc15")
    $ questLog(72, True)
    $ add_objective("seduce_ralph", t_("Соблазнить Ральфа."), c_blue, 105)
    $ add_hook("monica_cleaning_start", "ep212_quests_bardie_ralph3_init_cleaning", scene="global", label="ep212_quests_bardie_ralph3_init_cleaning")
    $ add_hook("monica_cleaning_end", "ep212_quests_bardie_ralph6_cleaning_end", scene="global", label="ep212_quests_bardie_ralph3_init_cleaning")
    $ monicaBardieRalphSeducingStage = 1
    call change_scene("basement_bedroom2", "Fade_long", False) from _rcall_change_scene_79
    return

label ep212_quests_bardie_ralph3_init_cleaning:
    # Добавляем гостиную к уборке в конец
    if monicaBardieRalphSeducingStage > 3:
        return
    if check_hook(label="steve_ralph_visit2", scene="living_room") == True or steveVisit2Day == day: # Если идет квест со Стивом, не активируем уборку в гостиной
        return
    if "living_room" in rooms_dirty:
        $ rooms_dirty.remove("living_room")
    $ rooms_dirty.append("living_room")
    $ move_object("Ralph", "living_room")
    $ monicaBardieRalphSeducingCleaningItemsCount = 4
    $ monicaBardieRalphSeducingCleaningCompletedToday = False
    if monicaBardieRalphSeducingStage == 1: # первая уборка
        $ add_hook("enter_scene", "ep212_quests_bardie_ralph4", scene="living_room", label="ralph_cleaning")
    if monicaBardieRalphSeducingStage == 2: # вторая уборка
        $ add_hook("enter_scene", "ep212_quests_bardie_ralph7", scene="living_room", label="ralph_cleaning")
    if monicaBardieRalphSeducingStage == 3: # третья уборка
        $ add_hook("enter_scene", "ep212_quests_bardie_ralph9", scene="living_room", label="ralph_cleaning")
    return

label ep212_quests_bardie_ralph4: # первая уборка
    $ remove_hook()
    call ep212_dialogues1_bardie_ralph3() from _rcall_ep212_dialogues1_bardie_ralph3
    if _return == False:
        return
    call ep212_dialogues1_bardie_ralph3a() from _rcall_ep212_dialogues1_bardie_ralph3a
    if _return == False:
        return
    call ep212_dialogues1_bardie_ralph4() from _rcall_ep212_dialogues1_bardie_ralph4
    $ add_hook("Ralph", "ep212_dialogues1_bardie_ralph12b", scene="living_room", label="ralph_cleaning_interact")
    $ add_hook_multi("ep212_quests_bardie_ralph5", scene="living_room", label="ralph_cleaning_interact", filter={"group":"environment"})
    call refresh_scene_fade() from _rcall_refresh_scene_fade_49
    return

label ep212_quests_bardie_ralph5: # уборка интерактив
    call ep212_dialogues1_bardie_ralph4a() from _rcall_ep212_dialogues1_bardie_ralph4a
    $ monicaBardieRalphSeducingCleaningItemsCount-=1
    if monicaBardieRalphSeducingCleaningItemsCount == 0:
        call ep212_dialogues1_bardie_ralph4b() from _rcall_ep212_dialogues1_bardie_ralph4b
        $ monicaBardieRalphSeducingCleaningCompletedToday = True
        $ houseCleaningShortEnd = True
        $ remove_hook(label="ralph_cleaning_interact")
    return

label ep212_quests_bardie_ralph6_cleaning_end: # После уборки
    if monicaBardieRalphSeducingCleaningCompletedToday == True:
        if monicaBardieRalphSeducingStage == 1:
            $ clear_music_stack()
#            call ep212_dialogues1_bardie_ralph5() from _rcall_ep212_dialogues1_bardie_ralph5
#            $ autorun_to_object("ep212_dialogues1_bardie_ralph6", scene="basement_bedroom2")
            #$ monicaBardieRalphSeducingStage = 2
#            $ questHelp("house_31", True)
#            $ questHelp("house_32")
            $ add_hook("wardrobe_menu", "wardrobePutGovernessWithoutPanties", scene="menu", label="menu_governess_without_panties", caption = t_("Униформа гувернантки (без трусиков)"), active="checkGovernessWithoutPantiesActive", priority = 80)
            $ monicaBardieRalphSeducingStage = 3
            $ questHelp("house_31", True)
            $ questHelp("house_33")
            $ clear_music_stack()
            call change_scene("basement_bedroom2", "Fade_long", False) from _rcall_change_scene_80
            return
        if monicaBardieRalphSeducingStage == 2:
            $ clear_music_stack()
            call ep212_dialogues1_bardie_ralph9() from _rcall_ep212_dialogues1_bardie_ralph9
            $ autorun_to_object("ep212_dialogues1_bardie_ralph10", scene="basement_bedroom2")
            $ monicaBardieRalphSeducingStage = 3
            $ questHelp("house_32", True)
            $ questHelp("house_33")
            $ clear_music_stack()
            call change_scene("basement_bedroom2", "Fade_long", False) from _rcall_change_scene_81
            return
        if monicaBardieRalphSeducingStage == 3:
            $ clear_music_stack()
#            call ep212_dialogues1_bardie_ralph13() from _rcall_ep212_dialogues1_bardie_ralph13
            $ autorun_to_object("ep212_dialogues1_bardie_ralph14", scene="basement_bedroom2")
#            $ monicaBardieRalphSeducingStage = 4
            $ monicaBardieRalphSeducingStage = 5
            $ remove_objective("seduce_ralph")
            $ questHelp("house_33", True)
#            $ questHelp("house_35")
            call ep214_quests_ralph1()
            $ clear_music_stack()
            call change_scene("basement_bedroom2", "Fade_long", False) from _rcall_change_scene_82
            return
        if monicaBardieRalphSeducingStage == 4:
            $ clear_music_stack()
            $ monicaBardieRalphSeducingStage = 5
            call ep214_quests_ralph1() from _rcall_ep214_quests_ralph1
            $ clear_music_stack()
            call change_scene("basement_bedroom2", "Fade_long", False) from _rcall_change_scene_129
            return


    return

label ep212_quests_bardie_ralph7: # Вторая уборка
    $ remove_hook()
    call ep212_dialogues1_bardie_ralph3() from _rcall_ep212_dialogues1_bardie_ralph3_1
    if _return == False:
        return
    call ep212_dialogues1_bardie_ralph7() from _rcall_ep212_dialogues1_bardie_ralph7
    if _return == False:
        return
    call ep212_dialogues1_bardie_ralph8() from _rcall_ep212_dialogues1_bardie_ralph8
    $ add_hook("Ralph", "ep212_dialogues1_bardie_ralph12b", scene="living_room", label="ralph_cleaning_interact")
    $ add_hook_multi("ep212_quests_bardie_ralph8", scene="living_room", label="ralph_cleaning_interact", filter={"group":"environment"})
    call refresh_scene_fade() from _rcall_refresh_scene_fade_50
    return

label ep212_quests_bardie_ralph8: # уборка интерактив
    call ep212_dialogues1_bardie_ralph8a() from _rcall_ep212_dialogues1_bardie_ralph8a
    $ monicaBardieRalphSeducingCleaningItemsCount-=1
    if monicaBardieRalphSeducingCleaningItemsCount == 0:
        call ep212_dialogues1_bardie_ralph8b() from _rcall_ep212_dialogues1_bardie_ralph8b
        $ clear_music_stack()
        if _return == True:
            $ monicaBardieRalphSeducingCleaningCompletedToday = True
        else:
            call ep212_dialogues1_bardie_ralph8c() from _rcall_ep212_dialogues1_bardie_ralph8c
        $ houseCleaningShortEnd = True
        $ remove_hook(label="ralph_cleaning_interact")
    return

label ep212_quests_bardie_ralph9: # третья уборка
    $ remove_hook()
    call ep212_dialogues1_bardie_ralph3() from _rcall_ep212_dialogues1_bardie_ralph3_2
    if _return == False:
        return
    call ep212_dialogues1_bardie_ralph11() from _rcall_ep212_dialogues1_bardie_ralph11
    if _return == False:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_51
        return
    call ep212_dialogues1_bardie_ralph12() from _rcall_ep212_dialogues1_bardie_ralph12
    $ autorun_to_object("ep212_dialogues1_bardie_ralph12b", scene="living_room")
    $ add_hook("Ralph", "ep212_dialogues1_bardie_ralph12b", scene="living_room", label="ralph_cleaning_interact")
    $ add_hook_multi("ep212_quests_bardie_ralph10", scene="living_room", label="ralph_cleaning_interact", filter={"group":"environment"})
    call refresh_scene_fade() from _rcall_refresh_scene_fade_52
    return

label ep212_quests_bardie_ralph10:  # уборка интерактив
    call ep212_dialogues1_bardie_ralph12a() from _rcall_ep212_dialogues1_bardie_ralph12a
    $ monicaBardieRalphSeducingCleaningItemsCount-=1
    if monicaBardieRalphSeducingCleaningItemsCount == 0:
        $ clear_music_stack()
        call ep212_dialogues1_bardie_ralph12c() from _rcall_ep212_dialogues1_bardie_ralph12c
        if _return == True:
            $ monicaBardieRalphSeducingCleaningCompletedToday = True
        else:
            call ep212_dialogues1_bardie_ralph8c() from _rcall_ep212_dialogues1_bardie_ralph8c_1
        $ houseCleaningShortEnd = True
        $ remove_hook(label="ralph_cleaning_interact")
    return
