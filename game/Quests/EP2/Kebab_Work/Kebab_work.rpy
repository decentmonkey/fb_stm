default kebabWorkInProgress = False
default monicaKnowAboutKebabWork = False #Знает-ли Моника об этой работе
default kebabWorkFirstTime = True
default kebabWorkFlyersLeft = 0
default kebabWorkFlyersTotal = 0
default kebabWorkMonicaRefusedAmount = 0
default kebabWorkHarassmentAmount = 0
default monicaKebabWorkLastDay = 0

default kebabOffendQuestJustCompleted = False

default cloth_type_last = "Whore"
default cloth_last = "Whore"

label kebab_work_init:
    $ add_hook("Shawarma_Trader", "kebab_work_trader_interact1", scene="whores_place_shawarma", label="kebab_dialogue")
    return

label reduce_flyers:
    $ kebabWorkFlyersLeft = kebabWorkFlyersLeft - 1
    $ notif(t_("Флаеры убавлено"))
    call kebab_work_objective_refresh() from _call_kebab_work_objective_refresh
    if kebabWorkFlyersLeft == 0:
        $ autorun_to_object("monica_shawarma_dialogue3a")
        call refresh_scene_fade() from _call_refresh_scene_fade_16
    return

label kebab_work_trader_interact1: # первый разговор о кебабах
    if act == "l":
        return
    if act == "t":
        if day_time == "evening":
            # нет вечерних рендеров разговора о работе
            call monica_shawarma_dialogue0() from _call_monica_shawarma_dialogue0 # он уже закрывается
            call refresh_scene_fade() from _call_refresh_scene_fade_17
            return False
#        call kebab_work_start()
#        return
        call monica_shawarma_dialogue1() from _call_monica_shawarma_dialogue1
        if questHelpFlag16 == False:
            $ questHelpFlag16 = True
            $ questHelp("work_slums_1", True)
            $ questHelp("work_slums_2")
            $ questHelpDesc("workslums_desc1", "workslums_desc2")
        if monicaKnowAboutKebabWork == True:
            $ replace_hook("kebab_work_trader_interact2", scene="all", label="kebab_dialogue")
            call kebab_work_start() from _call_kebab_work_start

    return

label kebab_work_start:
    $ hudDaySkipToEveningEnabled = False
    $ kebabWorkFlyersLeft = monicaKebabWorkFlyersAmount
    $ rnd1 = rand(0, monicaKebabWorkFlyersAmountRandomDiff)
    if rand(0,1) == 1:
        $ rnd1 = rnd1 * -1
    $ kebabWorkFlyersLeft = kebabWorkFlyersLeft + rnd1
    $ kebabWorkFlyersTotal = kebabWorkFlyersLeft

    $ add_hook("Teleport_Clothing_Shop", "monica_shawarma_dialogue5", scene="whores_place_shawarma", label="kebab_work")
    if kebabWorkFirstTime == True:
        $ questLog(15, False)
        $ questLog(16, True)
        $ add_hook("enter_scene", "monica_shawarma_dialogue6", scene="hostel_street", label="kebab_work")
        $ add_hook("enter_scene", "monica_shawarma_dialogue7", scene="hostel_street2", label="kebab_work")
        $ add_hook("enter_scene", "monica_shawarma_dialogue9", scene="hostel_street3", label="kebab_work")
        $ add_hook("enter_scene", "monica_shawarma_dialogue8", scene="hostel_edge_1_c", label="kebab_work")
        $ rooms_list = get_rooms_recursive("Street_Corner")
        python:
            for room_name in rooms_list:
                add_hook("Monica", "monica_shawarma_dialogue11", scene=room_name, label="kebab_work")

        #monica_shawarma_dialogue10 mt "В этом районе одни наркоманы и извращенцы!"
    $ add_hook("Teleport_Hostel_1_a", "kebab_work_block_hostel_edge_1_a", scene="hostel_edge_1_c", label="kebab_work")

    $ last_map_enabled = map_enabled
    $ map_enabled = False

    $ cloth_type_last = cloth_type
    $ cloth_last = cloth

    $ cloth_type = "Kebab"
    $ cloth = "Kebab"
    call kebab_work_objective_refresh() from _call_kebab_work_objective_refresh_1
    $ kebabWorkFirstTime = False
    $ kebabWorkInProgress = True
    $ kebabWorkMonicaRefusedAmount = 0
    $ kebabWorkHarassmentAmount = 0
    $ miniMapDisabled["Street_Corner"] = []
    $ map_objects["Teleport_Hostel2"]["state"] = "visible"
    $ remove_hook(label="kebab_work_block_teleports")
    return

label kebab_work_objective_refresh:
    $ print "kebab refresh"
    $ print kebabWorkFlyersLeft
    if kebabWorkFlyersLeft > 0:
        $ remove_objective("give_flyers")
        $ add_objective("give_flyers", t__("Осталось флаеров") + " " + str(kebabWorkFlyersLeft), c_orange, 20)
    else:
        $ remove_objective("give_flyers")
    return

label kebab_work_trader_interact2:
    if act == "l":
        return
    if act == "t":
        if kebabWorkInProgress == True:
            call kebab_work_end() from _call_kebab_work_end
            call refresh_scene_fade() from _call_refresh_scene_fade_18
            return False
        if monicaEatedLastDay == day and (monica_cheats_hungry_enabled == True or monicaKebabWorkLastDay == day):
            if slumsApartmentsShawarmaTraderDialogue1Active == True:
                call ep211_slums_apartments_quest1_menu() from _rcall_ep211_slums_apartments_quest1_menu
                if _return == False:
                    return False
            call monica_shawarma_dialogue4() from _call_monica_shawarma_dialogue4 #Моника сыта
            return False
        if day_time == "evening":
            if slumsApartmentsShawarmaTraderDialogue1Active == True:
                call ep211_slums_apartments_quest1_menu() from _rcall_ep211_slums_apartments_quest1_menu_1
                if _return == False:
                    return False
            call monica_shawarma_dialogue2a() from _call_monica_shawarma_dialogue2a
            return False
        if day_time == "day":
            if slumsApartmentsShawarmaTraderDialogue1Active == True:
                call ep211_slums_apartments_quest1_menu() from _rcall_ep211_slums_apartments_quest1_menu_2
                if _return == False:
                    return False
            call monica_shawarma_dialogue2() from _call_monica_shawarma_dialogue2
            return False
    m "interact2"
    return

label kebab_work_end:
    menu:
        "Я раздала все флаеры, где мой кебаб?" if kebabWorkFlyersLeft == kebabWorkFlyersTotal or kebabWorkFlyersLeft <= 0:
            if kebabWorkFlyersLeft == kebabWorkFlyersTotal: #Моника не раздала ни одного флаера
                call monica_shawarma_dialogue3_end_no_food() from _call_monica_shawarma_dialogue3_end_no_food #Монику НЕ кормим
            if kebabWorkFlyersLeft <= 0: #Моника раздала все флаеры
                call monica_shawarma_dialogue3_food() from _call_monica_shawarma_dialogue3_food
                call monicaEat() from _call_monicaEat
                $ questHelp("work_slums_2", True)
                $ add_corruption(monicaKebabWorkCorruptionAddingPerDay, "monicaKebabWorkCorruptionAddingPerDay_day" + str(day))
        "У меня не получилось раздать все флаеры..." if kebabWorkFlyersLeft > 0 and kebabWorkFlyersLeft < kebabWorkFlyersTotal: #Моника раздала не все флаеры
            call monica_shawarma_dialogue3_end_half_food() from _call_monica_shawarma_dialogue3_end_half_food
            call monicaEat() from _call_monicaEat_1
            $ questHelp("work_slums_2", True)
            $ add_corruption(monicaKebabWorkCorruptionAddingPerDay, "monicaKebabWorkCorruptionAddingPerDay_day" + str(day))
        "Уйти.":
            return

    $ remove_objective("give_flyers")
    $ remove_hook(label="kebab_work")
    $ kebabWorkInProgress = False
    $ cloth_type = cloth_type_last
    $ cloth = cloth_last
    $ map_enabled = last_map_enabled
    $ monicaKebabWorkAmount +=1
    $ monicaKebabWorkLastDay = day
    if kebabOffendQuestJustCompleted == True:
        $ kebabOffendQuestJustCompleted = False
        call change_scene("hostel_street2") from _call_change_scene_184
        return
    $ hudDaySkipToEveningEnabled = True
    $ changeDayTime("evening")
    call refresh_scene_fade() from _call_refresh_scene_fade_19
    return


label kebab_work_block_hostel_edge_1_a:
    if act == "l":
        return
    call kebab_work_block_teleports() from _call_kebab_work_block_teleports
    return False

label kebab_work_block_teleports:
    mt "Я не пойду в эту вонючую подворотню!"
    "Что там забыла такая девушка как Я!??"
    return False
