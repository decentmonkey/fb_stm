default ep28_quests_police_day1_cage1_flag = False
default ep28_quests_police_day1_bed1_flag = False
default ep28_quests_monica_offended_day1 = False # Монику использовали заключенные день1
default ep28_quests_monica_offended_day2 = False # Монику использовали заключенные день2
default ep28_quests_monica_offended_day3 = False # Монику использовали заключенные день3
default ep28_quests_monica_offended_prisoners = False # Моника сама наехала на заключенных
default ep28_quests_monica_kicked_prisoners = False # Моника ударила и укусила заключенных
default ep28_quests_monica_called_monicapubname = False
default ep28_quests_bob_dick = False # Боб запихнул член Монике в рот
default marcus_visit1_completed = False
default ep28_quests_completed_day = 0

default moneyStored = 0

label ep28_quests_police1:
    # Инициализация
    call ep28_dialogues_jail1() from _call_ep28_dialogues_jail1
    $ questHelp("marcus_4")
    $ moneyStored = money
    $ money = 0 # отбираем деньги
    $ add_hook("Sortir", "ep28_quests_police1_sortir", scene="police_cell1", label="cell_sortir") # туалет
    $ remove_hook(label="cage_interact1")
    $ add_hook("cage_interact", "ep28_quests_police_day1_cage1", scene="police", label="cage_interact_day1a")
    $ add_hook("Bed", "ep28_quests_police_bed_regular", scene="police_cell1", label="cell_bed") # кровать
    $ add_hook("Bed", "ep28_quests_police_bed_regular", scene="police_cell2", label="cell_bed") # кровать
    $ add_hook("Bed", "ep28_quests_police_day1_bed1", scene="police_cell1", label="cell_bed_day1") # кровать
    $ add_hook("Bed", "ep28_quests_police_day1_bed1", scene="police_cell2", label="cell_bed_day1") # кровать
    call change_scene("police_cell1", "Fade_long", False) from _call_change_scene_413
    return

label ep28_quests_police1_sortir: # клик на сортир
    if act=="l":
        return
    call ep28_dialogues_jail1_piss() from _call_ep28_dialogues_jail1_piss
    call refresh_scene_fade() from _call_refresh_scene_fade_190
    return False

label ep28_quests_police_day1_cage1:
    $ ep28_quests_police_day1_cage1_flag = True
    call ep28_dialogues_jail3b() from _call_ep28_dialogues_jail3b
    call change_scene("police_cell2", "Fade_long") from _call_change_scene_414
    return False

label ep28_quests_police_day1_bed1:
    if act=="l":
        return
    if ep28_quests_police_day1_bed1_flag == False:
        call ep28_dialogues_jail3() from _call_ep28_dialogues_jail3
        $ ep28_quests_police_day1_bed1_flag = True
    if ep28_quests_police_day1_cage1_flag == False:
        if ep28_quests_police_day1_bed1_flag == True:
            call ep28_dialogues_jail1_bed() from _call_ep28_dialogues_jail1_bed
        call refresh_scene_fade() from _call_refresh_scene_fade_191
        return False
    $ remove_hook(label="cage_interact_day1a")
    $ remove_hook(label="cell_bed_day1")
    call ep28_quests_police_day1_prisoners1() from _call_ep28_quests_police_day1_prisoners1
    call refresh_scene_fade() from _call_refresh_scene_fade_192
    return False

label ep28_quests_police_bed_regular:
    if act=="l":
        return
    call ep28_dialogues_jail1_bed() from _call_ep28_dialogues_jail1_bed_1
    return False

label ep28_quests_police_day1_prisoners1: # Приходят заключенные, день1
    $ remove_hook()
    call ep28_dialogues_jail4() from _call_ep28_dialogues_jail4
    if _return == False:
        $ ep28_quests_monica_offended_prisoners = True
    else:
        $ ep28_quests_monica_offended_day1 = True
        $ add_corruption(monicaJailDay1AddCorruption, "monicaJailDay1AddCorruption")
    $ add_hook("cage_interact", "ep28_dialogues_jail3a", scene="police", label="cage_interact_nobody")
    $ add_hook("cage_interact", "ep28_dialogues_jail5", scene="police", label="cage_day1")
    $ add_hook("Bed", "ep28_quests_police_day1_bed2", scene="police_cell1", label="cell_bed_day1") # кровать
    $ add_hook("Bed", "ep28_quests_police_day1_bed2", scene="police_cell2", label="cell_bed_day1") # кровать
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_28
    return

label ep28_quests_police_day1_bed2: # Моника ложится спать день 1
    if act=="l":
        return
    call ep27_dialogues_marcus1_10() from _call_ep27_dialogues_marcus1_10_1
    if _return == False:
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_29
        return False
    $ questHelp("marcus_4", True)
    call ep28_dialogues_jail6() from _call_ep28_dialogues_jail6
    call ep28_dialogues_jail7() from _call_ep28_dialogues_jail7
    $ day = day + 1
    $ remove_hook(label="cage_day1")
    $ remove_hook(label="cell_bed_day1")
    $ questHelp("marcus_5")

    $ add_hook("cage_interact", "ep28_quests_police_day2_cage1", scene="police", label="cage_day2")
    call change_scene("police_cell1", "Fade_long", False) from _call_change_scene_415
    return False

label ep28_quests_police_day2_cage1: # День2, решетка
    $ remove_hook()
    if ep28_quests_monica_offended_prisoners == True: # конец квеста
        $ remove_hook(label="cell_bed_day1")
        $ remove_hook(label="cage_day1")
        $ remove_hook(label="cage_day2")
        call ep28_quests_police_final() from _call_ep28_quests_police_final
        return False
    call ep28_dialogues_jail8() from _call_ep28_dialogues_jail8
    $ add_hook("Bed", "ep28_quests_police_day2_bed1", scene="police_cell1", label="cage_day2") # кровать
    $ add_hook("Bed", "ep28_quests_police_day2_bed1", scene="police_cell2", label="cage_day2") # кровать
    call change_scene("police_cell2", "Fade_long", False) from _call_change_scene_416
    return False

label ep28_quests_police_day2_bed1: # Кровать день2, приходят заключенные
    if act=="l":
        return
    call ep27_dialogues_marcus1_10() from _call_ep27_dialogues_marcus1_10_2
    if _return == False:
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_30
        return False
    call ep28_dialogues_jail9() from _call_ep28_dialogues_jail9
    if _return == False:
        $ ep28_quests_monica_offended_prisoners = True
    else:
        $ ep28_quests_monica_offended_day2 = True
        $ add_corruption(monicaJailDay2AddCorruption, "monicaJailDay2AddCorruption")

    $ remove_hook(label="cage_day2")
    $ add_hook("Bed", "ep28_quests_police_day2_bed2", scene="police_cell1", label="cage_day2") # кровать
    $ add_hook("Bed", "ep28_quests_police_day2_bed2", scene="police_cell2", label="cage_day2") # кровать


    call change_scene("police_cell1", "Fade_long", False) from _call_change_scene_417
#    call refresh_scene_fade_long()
    return False

label ep28_quests_police_day2_bed2: # Кровать день2, после заключенных (сон)
    if act=="l":
        return
    call ep27_dialogues_marcus1_10() from _call_ep27_dialogues_marcus1_10_3
    if _return == False:
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_31
        return False

    $ questHelp("marcus_5", True)
    call ep28_dialogues_jail10() from _call_ep28_dialogues_jail10

    $ questHelp("marcus_7")
    $ day = day + 1
    call ep28_dialogues_jail11() from _call_ep28_dialogues_jail11
    $ remove_hook(label="cage_day2")
    $ add_hook("cage_interact", "ep28_quests_police_day3_cage1", scene="police", label="cage_day3")
    call change_scene("police_cell1", "Fade_long", False) from _call_change_scene_418
    return False

label ep28_quests_police_day3_cage1: # День3, решетка
    $ remove_hook()
    if ep28_quests_monica_offended_prisoners == True: # конец квеста
        $ remove_hook(label="cell_bed_day1")
        $ remove_hook(label="cage_day1")
        $ remove_hook(label="cage_day2")
        $ remove_hook(label="cage_day3")
        call ep28_quests_police_final() from _call_ep28_quests_police_final_1
        return False
    call ep28_dialogues_jail12() from _call_ep28_dialogues_jail12
    $ add_hook("Bed", "ep28_quests_police_day3_bed1", scene="police_cell1", label="cage_day3") # кровать
    $ add_hook("Bed", "ep28_quests_police_day3_bed1", scene="police_cell2", label="cage_day3") # кровать
    call change_scene("police_cell2", "Fade_long", False) from _call_change_scene_419
    return False

label ep28_quests_police_day3_bed1: # Ден3, кровать, приход заключенных
    if act=="l":
        return
    call ep27_dialogues_marcus1_10() from _call_ep27_dialogues_marcus1_10_4
    if _return == False:
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_32
        return False
    call ep28_dialogues_jail13() from _call_ep28_dialogues_jail13
    call ep28_dialogues_jail14() from _call_ep28_dialogues_jail14
    if _return == False:
        $ ep28_quests_monica_offended_prisoners = True
    else:
        $ ep28_quests_monica_offended_day3 = True
        $ add_corruption(monicaJailDay3AddCorruption, "monicaJailDay3AddCorruption")
    $ remove_hook(label="cage_day2")
    $ remove_hook(label="cage_day3")
    $ add_hook("Bed", "ep28_quests_police_day3_bed2", scene="police_cell1", label="cage_day3") # кровать
    $ add_hook("Bed", "ep28_quests_police_day3_bed2", scene="police_cell2", label="cage_day3") # кровать

    music stop
    img black_screen
    with diss
    pause 1.5
    call change_scene("police_cell1", "Fade_long", False) from _call_change_scene_420
    return False

label ep28_quests_police_day3_bed2: #День3, кровать, сон
    if act=="l":
        return
    $ questHelp("marcus_7", True)
    call ep28_dialogues_jail15() from _call_ep28_dialogues_jail15
    $ day = day + 1
    call ep28_dialogues_jail16() from _call_ep28_dialogues_jail16
    $ questHelp("marcus_9")
    $ questHelp("marcus_10")
    $ remove_hook(label="cage_day3")
    $ add_hook("cage_interact", "ep28_quests_police_day4_cage1", scene="police", label="cage_day3")
    call change_scene("police_cell2", "Fade_long") from _call_change_scene_421
    return False

label ep28_quests_police_day4_cage1: #День4, решетка, завершение квеста
    $ remove_hook()
    call ep28_quests_police_final() from _call_ep28_quests_police_final_2
    return False


label ep28_quests_police_final: # Завершение тюремного квеста
    call ep28_dialogues_jail17() from _call_ep28_dialogues_jail17
    if ep28_quests_monica_offended_prisoners == True:
        # Моника наехала на заключенных
        call ep28_dialogues_jail18() from _call_ep28_dialogues_jail18
    else:
        # Моника подчинилась заключенным до конца
        call ep28_dialogues_jail19() from _call_ep28_dialogues_jail19

    # Разговор с Маркусом
    call ep28_dialogues_jail2_marcus1() from _call_ep28_dialogues_jail2_marcus1
    call ep28_dialogues_jail2_marcus2() from _call_ep28_dialogues_jail2_marcus2

    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    $ changeDayTime("evening")
    $ rain = True
    $ rainIntencity = 3
    $ lightning = True
#    $ day_time = "evening"
#    $ day_suffix = "_Evening"
    $ add_hook("enter_scene", "ep28_dialogues_jail2_marcus3", scene="street_police", once=True)

    $ add_money(moneyStored)
    $ define_inventory_object("butt_plug", {"description" : t_("Анальная пробка"), "label_suffix" : "_use_butt_plug", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/butt_plug" + res.suffix + ".png"})

    $ questsCompleteByCategory(t_("МАРКУС"))
    $ questHelp("marcus_1", True)
    $ questHelp("marcus_9", True)
    $ questHelp("marcus_10", True)
    $ questHelp("marcus_11")
    $ questHelpDesc("marcus_desc2", "marcus_desc3")

    $ questLog(54, False)
    $ questLog(56, True)
    $ add_inventory("butt_plug", 1, True)
    $ add_hook("enter_scene", "ep28_quests_police_final_home", scene="basement_bedroom2", once=True)
    $ add_hook("Building", "ep28_dialogues_jail2_marcus5", scene="street_police", label="marcus_block1")

    if monicaWorkFlashCardQuestActive == True:
        $ add_inventory("flash_card", 1, True)



    music stop
    img black_screen
    with diss
    pause 2.0
    call change_scene("street_police", "Fade_long", False) from _call_change_scene_422
    $ marcus_visit1_completed = True
    return

label ep28_quests_police_final_home:
    call ep28_dialogues_jail2_marcus4() from _call_ep28_dialogues_jail2_marcus4
    $ remove_inventory("butt_plug", 1, True)
    $ rain = False
    $ lightning = False
    $ ep28_quests_completed_day = day
    $ questHelp("revenge_1")
#    call ep29_revenge_quest1_init() from _call_ep29_revenge_quest1_init_1 # Запускаем проверку на revenge quest
    call basement_bedroom2_init2() from _call_basement_bedroom2_init2_1 # Оставляем в basement_bedroom2 анальную пробку
    sound chpok2
    call refresh_scene_fade() from _call_refresh_scene_fade_239
    return







#
