default ep211_quests_escort1_inited = False

default ep211_quests_stored_cloth = False
default ep211_quests_stored_cloth_type = False

default monicaEscortLastDay = 0 # Когда крайний раз Моника работала в эскорте

default monicaEscortSceneDay = 0
default monicaEscortScene1Day = 0
default monicaEscortScene2Day = 0
default monicaEscortScene3Day = 0
default monicaEscortScene4Day = 0
default monicaEscortScene5Day = 0
default monicaEscortScene6Day = 0

default monicaEscortScenesCount = 0
default monicaEscortFailedScenesCount = 0

default escortRestaurantEnterForced = 0

label ep211_quests_escort1:
    if ep211_quests_escort1_inited == False:
        call locations_init_rich_hotel_restaurant2() from _rcall_locations_init_rich_hotel_restaurant2
        call rich_hotel_reception_init3() from _rcall_rich_hotel_reception_init3
        $ add_hook("Teleport_Lift", "ep211_quests_escort3_lift_check", scene="rich_hotel_reception", label="rich_hotel_lift_block")
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep211_quests_escort1_enter", scene="street_rich_hotel", label="rich_hotel_escort_enter_check")
        $ add_hook("Door", "ep211_quests_escort3_door_check", scene="rich_hotel_reception", label="rich_hotel_door_block")
        $ ep211_quests_escort1_inited = True
    $ richHotelLiftMonicaSuffix = 1
    $ richHotelLiftSceneSuffix = "_Closed"

    call ep210_dialogues7_escort_hotel_8a() from _rcall_ep210_dialogues7_escort_hotel_8a
    $ ep211_quests_stored_cloth = cloth
    $ ep211_quests_stored_cloth_type = cloth_type
    $ cloth = "EscortDress1"
    $ cloth_type = "EscortDress"
    $ add_hook("ReceptionGirl", "ep211_quests_escort2_exit_dialogue", scene="rich_hotel_reception", quest="work_escort")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep211_quests_escort2_exit", scene="rich_hotel_reception", quest="work_escort")
    $ add_hook("Teleport_Restaurant", "ep211_quests_escort4_restaurant", scene="rich_hotel_reception", quest="work_escort")
    $ add_hook("MonicaTable", "ep211_quests_escort5_restaurant_wait_customer", scene="rich_hotel_restaurant", quest="work_escort")
    $ monicaEscortLastDay = day
    if char_info["ReceptionGirl"]["level"] == 1:
        $ char_info["ReceptionGirl"]["enabled"] = True
        $ char_info["ReceptionGirl"]["caption"] = t_("Сутенерша в Le Grand.")

    if monicaEscortClientHotel5 == True:
        $ questHelp("escort_6", skipIfExists=True)
    if monicaEscortClientHotel7 == True:
        $ questHelp("escort_7", skipIfExists=True)
    if monicaEscortClientHotel9 == True and monicaHotelStaffEscort2 == True:
        $ questHelp("escort_9", skipIfExists=True)
    if monicaEscortClientHotel8 == True and monicaEscortClientHotel9 == True:
        $ questHelp("escort_11", skipIfExists=True)
    if ep215_quests_escort_completed_day > 0 and monicaEscortRevengeGirl2 == True:
        $ questHelp("escort_13", skipIfExists=True)



    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_2
    return

label ep211_quests_escort1_enter: # проверка на вход в отель
    if monicaEscortLastDay == day:
        call ep210_dialogues7_escort_hotel_7d() from _rcall_ep210_dialogues7_escort_hotel_7d
        return False
    return

label ep211_quests_escort2_exit:
    call ep211_escort_scene1_14() from _rcall_ep211_escort_scene1_14
    if _return == 1:
        call ep211_escort_scene1_15() from _rcall_ep211_escort_scene1_15
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day
    if _return == 3:
        call ep215_quests_esort_change_name() from _rcall_ep215_quests_esort_change_name
        return False
    return False

label ep211_quests_escort2_exit_dialogue:
    if act=="l":
        return
    call ep211_escort_scene1_14() from _rcall_ep211_escort_scene1_14_1
    if _return == 1:
        call ep211_escort_scene1_15() from _rcall_ep211_escort_scene1_15_1
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_1
    if _return == 3:
        call ep215_quests_esort_change_name() from _rcall_ep215_quests_esort_change_name_1
        return False
    return False

label ep211_quests_escort2_end_day:
    if ep212_escort_monica_fired == False:
        if monicaEscortClientHotel5 == True:
            $ questHelp("escort_6", skipIfExists=True)
        if monicaEscortClientHotel7 == True:
            $ questHelp("escort_7", skipIfExists=True)
        if monicaEscortClientHotel9 == True and monicaHotelStaffEscort2 == True:
            $ questHelp("escort_9", skipIfExists=True)
        if monicaEscortClientHotel8 == True and monicaEscortClientHotel9 == True:
            $ questHelp("escort_11", skipIfExists=True)
        if ep215_quests_escort_completed_day > 0 and monicaEscortRevengeGirl2 == True:
            $ questHelp("escort_13", skipIfExists=True)

    $ remove_hook(quest="work_escort")
    $ remove_hook(quest="work_escort")
    $ remove_hook(label="escort_scene1")
    $ remove_hook(label="escort_scene2")
    $ remove_objective("go_administrator")
    $ cloth = ep211_quests_stored_cloth
    $ cloth_type = ep211_quests_stored_cloth_type
    call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _rcall_change_scene_9
    return

label ep211_quests_escort3_lift_check: # Проверка на вход в лифт
    if cloth_type != "EscortDress":
        call ep211_escort_scene1_13() from _rcall_ep211_escort_scene1_13
        return False
    return

label ep211_quests_escort3_door_check:
    if act=="l":
        call ep211_escort_scene1_13a() from _rcall_ep211_escort_scene1_13a
        return False
    call ep211_escort_scene1_13() from _rcall_ep211_escort_scene1_13_1
    return False

label ep211_quests_escort4_restaurant: # Вход в ресторан
    music stop
    img black_screen
    with diss
    pause 1.5
    $ rnd1 = rand(1,4)
    if ep215_quests_linda_restaurant_dialogue_planned == True:
        $ ep215_quests_linda_restaurant_dialogue_planned = False # встреча с Линдой после того как ее унизили
        $ ep215_quests_linda_restaurant_dialogue_day = day
        call ep215_dialogues3_escort_22() from _rcall_ep215_dialogues3_escort_22
        call change_scene("rich_hotel_restaurant", "Fade_long") from _rcall_change_scene_163
        return False
    if ep214_dialogues3_escort_10_flag1 == True:
        $ ep214_dialogues3_escort_10_flag1 = False
        call ep214_dialogues3_escort_10() from _rcall_ep214_dialogues3_escort_10
        call change_scene("rich_hotel_restaurant", "Fade_long") from _rcall_change_scene_127
        return False

    if escortRestaurantEnterForced > 0:
        $ rnd1 = escortRestaurantEnterForced
        $ escortRestaurantEnterForced = 0
    if rnd1 == 1:
        if ep214_dialogues3_escort_10_flag2 == True:
            call ep214_dialogues3_escort_10() from _rcall_ep214_dialogues3_escort_10_1
            call change_scene("rich_hotel_restaurant", "Fade_long") from _rcall_change_scene_128
            return False
        if ep212_escort3_completed == True:
            call ep212_dialogues3_escort_hotel_7_3() from _rcall_ep212_dialogues3_escort_hotel_7_3
        else:
            call ep210_dialogues7_escort_hotel_8a2() from _rcall_ep210_dialogues7_escort_hotel_8a2
    if rnd1 == 2:
        call ep210_dialogues7_escort_hotel_8b() from _rcall_ep210_dialogues7_escort_hotel_8b
    if rnd1 == 3:
        call ep210_dialogues7_escort_hotel_8c() from _rcall_ep210_dialogues7_escort_hotel_8c
    if rnd1 == 4:
        call ep210_dialogues7_escort_hotel_8d() from _rcall_ep210_dialogues7_escort_hotel_8d
    call change_scene("rich_hotel_restaurant", "Fade_long") from _rcall_change_scene_10
    return False

label ep211_quests_escort5_restaurant_wait_customer:
    call ep211_escort_scene1_1a() from _rcall_ep211_escort_scene1_1a
    if _return == False:
        call change_scene("rich_hotel_reception", "Fade_long") from _rcall_change_scene_11
        return False
    if _return == -1:
        music stop
        img black_screen
        with diss
        pause 1.5
        music Poppers_and_Prosecco
        $ autorun_to_object("ep211_escort_scene1_16", scene="rich_hotel_restaurant")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_3
        return False
    if _return == 1: # Эскорт сцена 1
        $ monicaEscortScene1Day = day
        $ monicaEscortSceneDay = day
        $ monicaEscortScenesCount += 1
        music stop
        img black_screen
        with diss
        pause 2.0
        call ep211_escort_scene1_1() from _rcall_ep211_escort_scene1_1
        if _return == False:
            $ questHelp("escort_4", False)
            call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_2
            return False
        $ add_objective("go_administrator", t_("Пойти на ресепшн к администратору."), c_orange, 105)
        $ move_object("EscortCustomer1", "rich_hotel_lift")
        $ add_hook("EscortCustomer1", "ep211_escort_scene1_3", scene="rich_hotel_lift", label="escort_scene1")
        $ add_hook("Monica", "ep211_escort_scene1_3", scene="rich_hotel_lift", label="escort_scene1")
        $ add_hook("Teleport_Reception", "ep211_escort_scene1_3", scene="rich_hotel_lift", label="escort_scene1")

        $ autorun_to_object("ep211_escort_scene1_3", scene="rich_hotel_lift")
        $ richHotelLiftSceneSuffix = ""
        $ add_hook("Lift", "ep211_quests_escort6_scene1c", scene="rich_hotel_lift", label="escort_scene1")
        $ add_hook("Teleport_Restaurant", "ep211_escort_scene1_17", scene="rich_hotel_reception", label="escort_scene1")
        $ add_hook("Teleport_Lift", "ep211_escort_scene1_17", scene="rich_hotel_reception", label="escort_scene1")
        $ add_hook("ReceptionGirl", "ep211_quests_escort6_scene1a", scene="rich_hotel_reception", label="escort_scene1")
        call change_scene("rich_hotel_reception", "Fade_long") from _rcall_change_scene_12
        return False



    if _return == 2: # Эскорт сцена 2
        $ monicaEscortScene2Day = day
        $ monicaEscortSceneDay = day
        $ monicaEscortScenesCount += 1
        call ep211_quests_escort6_scene2a() from _rcall_ep211_quests_escort6_scene2a
    if _return == 3: # Эскорт сцена 3
        $ monicaEscortScene3Day = day
        $ monicaEscortSceneDay = day
        $ monicaEscortScenesCount += 1
        call ep212_escort3_1() from _rcall_ep212_escort3_1
    if _return == 4:
        call ep212_escort4_1() from _rcall_ep212_escort4_1
        if _return == True:
            $ monicaEscortScene4Day = day
            $ monicaEscortSceneDay = day
            $ monicaEscortScenesCount += 1
            call ep214_quests_escort1() from _rcall_ep214_quests_escort1
    if _return == 5:
        $ monicaEscortScene5Day = day
        $ monicaEscortSceneDay = day
        $ monicaEscortScenesCount += 1
        call ep213_escort5_1() from _rcall_ep213_escort5_1

    if _return == 6:
        call ep214_quests_escort2() from _rcall_ep214_quests_escort2
        if _return != False:
            $ monicaEscortScene6Day = day
            $ monicaEscortSceneDay = day
            $ monicaEscortScenesCount += 1
    if _return == 7:
        $ monicaEscortScene1Day = day
        $ monicaEscortSceneDay = day
        $ monicaEscortScenesCount += 1
        music stop
        img black_screen
        with diss
        pause 2.0
        call ep216_dialogues2_escort_1() from _rcall_ep216_dialogues2_escort_1
        $ add_objective("go_corridor", t_("Пойти в служебный коридор."), c_orange, 105)
        $ move_object("ReceptionGirl", "empty")
        $ add_hook("Teleport_Street_Rich_Hotel", "ep216_dialogues2_escort_3a", scene="rich_hotel_reception", label="escort_scene7")
        $ add_hook("Door", "ep211_quests_escort6_scene7", scene="rich_hotel_reception", label="escort_scene7")
        $ add_hook("MonicaTable", "ep216_dialogues2_escort_3a", scene="rich_hotel_restaurant", label="escort_scene7")
        $ set_active("Visitor2", False, scene="rich_hotel_restaurant")
        $ set_active("Visitor3", False, scene="rich_hotel_restaurant")


    return False


label ep211_quests_escort6_scene1a:
    if act=="l":
        return
    $ remove_objective("go_administrator")
    call ep211_escort_scene1_2() from _rcall_ep211_escort_scene1_2
    $ add_objective("change_clothes", t_("Пойти в служебный коридор и переодеться."), c_pink, 105)
    $ add_hook("Teleport_Lift", "ep211_escort_scene1_18", scene="rich_hotel_reception", label="escort_scene1")
    $ add_hook("Teleport_Restaurant", "ep211_escort_scene1_18", scene="rich_hotel_reception", label="escort_scene1")
    $ add_hook("ReceptionGirl", "ep211_escort_scene1_18", scene="rich_hotel_reception", label="escort_scene1")
    $ add_hook("Door", "ep211_quests_escort6_scene1b", scene="rich_hotel_reception", label="escort_scene1")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_4
    return False

label ep211_quests_escort6_scene1b:
    if act=="l":
        return
    $ remove_hook()
    $ remove_objective("change_clothes")
    call ep211_escort_scene1_2_1() from _rcall_ep211_escort_scene1_2_1
    $ richHotelLiftMonicaSuffix = 2
    $ add_objective("go_customer", t_("Пойти к клиенту. Он ждет у лифта."), c_blue, 105)
    call change_scene("rich_hotel_lift", "Fade_long", "snd_lift") from _rcall_change_scene_13
    return False

label ep211_quests_escort6_scene1c: #Лифт
    if act=="l":
        return
    $ remove_objective("go_customer")
    call ep211_escort_scene1_4() from _rcall_ep211_escort_scene1_4
    if _return == False:
        $ questHelp("escort_4", False)
        $ monicaEscortFailedScenesCount += 1
        $ autorun_to_object("ep211_escort_scene1_8", scene="street_rich_hotel")
        $ remove_hook(label="escort_scene1")
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_3
        return False

    $ questHelp("escort_4", True)
    $ questHelp("escort_5", skipIfExists=True)

    $ add_hook("Teleport_Lift", "ep211_escort_scene1_17", scene="rich_hotel_reception", label="escort_scene1")
    $ add_hook("Teleport_Restaurant", "ep211_escort_scene1_17", scene="rich_hotel_reception", label="escort_scene1")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep211_quests_escort6_scene1d_exit", scene="rich_hotel_reception", label="escort_scene1")
    $ add_hook("ReceptionGirl", "ep211_quests_escort6_scene1e_admin", scene="rich_hotel_reception", label="escort_scene1")
    $ add_corruption(monicaEscortScene1CorruptionAdd, "escort_scene1")
    $ richHotelLiftMonicaSuffix = 1
    $ richHotelLiftSceneSuffix = "_Closed"
    $ move_object("EscortCustomer1", "empty")
    $ add_objective("go_customer", t_("Пойти на ресепшн и отдать 50 процентов от заработка администратору."), c_red, 105)
    call change_scene("rich_hotel_reception", "Fade_long", "snd_lift") from _rcall_change_scene_14


    return False

label ep211_quests_escort6_scene1d_exit: # Уход из отеля без отдачи денег
    call ep211_escort_scene1_14() from _rcall_ep211_escort_scene1_14_2
    if _return == 1:
        call ep211_escort_scene1_6() from _rcall_ep211_escort_scene1_6
        call refresh_scene_fade() from _rcall_refresh_scene_fade_5
        return False
    return False

label ep211_quests_escort6_scene1e_admin: # Отдача денег администраторше
    if act=="l":
        return
    call ep211_escort_scene1_5() from _rcall_ep211_escort_scene1_5
    $ autorun_to_object("ep211_escort_scene1_7", scene="street_rich_hotel")
    $ remove_hook(label="escort_scene1")
    $ remove_objective("go_customer")
    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_4
    return False


label ep211_quests_escort6_scene2a:
    call ep211_escort_scene2_1() from _rcall_ep211_escort_scene2_1
    $ add_objective("go_administrator", t_("Пойти на ресепшн к администратору."), c_orange, 105)
    $ add_hook("MonicaTable", "ep211_escort_scene1_17", scene="rich_hotel_restaurant", label="escort_scene2")
    $ move_object("ReceptionGirl", "empty")
    $ add_hook("Door", "ep211_quests_escort6_scene2b", scene="rich_hotel_reception", label="escort_scene2")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep211_escort_scene1_17", scene="rich_hotel_reception", label="escort_scene2")
    $ add_hook("before_open", "ep211_escort_scene2_2", scene="rich_hotel_reception", label="escort_scene2", once=True)
    call refresh_scene_fade() from _rcall_refresh_scene_fade_6
    return

label ep211_quests_escort6_scene2b: # служебный коридор
    if act=="l":
        return
    $ remove_objective("go_administrator")
    call ep211_quests_escort6_scene2c() from _rcall_ep211_quests_escort6_scene2c
    if day_time != "evening":
        $ changeDayTime("evening")
    $ move_object("ReceptionGirl", "rich_hotel_reception")
    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_7
    return False

label ep211_quests_escort6_scene2c: # сцена
    call ep211_escort_scene2_3() from _rcall_ep211_escort_scene2_3 #стоит заказчик (Ned) и администраторша
    call ep211_escort_scene2_3a() from _rcall_ep211_escort_scene2_3a # сцена
    call ep211_escort_scene2_4() from _rcall_ep211_escort_scene2_4
    call ep211_escort_scene2_5() from _rcall_ep211_escort_scene2_5
    $ questHelp("escort_6", skipIfExists=True)
    if _return == False: # отказалась совсем
        call ep211_escort_scene2_14(0) from _rcall_ep211_escort_scene2_14
        $ monicaEscortFailedScenesCount += 1
        $ questHelp("escort_5", False)
        return False

    call ep211_escort_scene2_6() from _rcall_ep211_escort_scene2_6
    $ add_corruption(monicaEscortScene2CorruptionAdd1, "monicaEscortScene2CorruptionAdd1")
    call ep211_escort_scene2_7() from _rcall_ep211_escort_scene2_7
    call ep211_escort_scene2_8() from _rcall_ep211_escort_scene2_8
    $ questHelp("escort_5", True)
    if _return == False: # отказалась со 2-ым
        call ep211_escort_scene2_14(-1) from _rcall_ep211_escort_scene2_14_1
        $ monicaEscortFailedScenesCount += 1
        return False
    call ep211_escort_scene2_9() from _rcall_ep211_escort_scene2_9
    call ep211_escort_scene2_10() from _rcall_ep211_escort_scene2_10
    $ add_corruption(monicaEscortScene2CorruptionAdd2, "monicaEscortScene2CorruptionAdd2")
    call ep211_escort_scene2_11() from _rcall_ep211_escort_scene2_11
    call ep211_escort_scene2_12() from _rcall_ep211_escort_scene2_12
    if _return == False: # отказалась с 3-им
        call ep211_escort_scene2_14(-2) from _rcall_ep211_escort_scene2_14_2
        $ monicaEscortFailedScenesCount += 1
        return False
    $ add_corruption(monicaEscortScene2CorruptionAdd3, "monicaEscortScene2CorruptionAdd3")
    call ep211_escort_scene2_13() from _rcall_ep211_escort_scene2_13
    call ep211_escort_scene2_14(1) from _rcall_ep211_escort_scene2_14_3
    $ autorun_to_object("ep211_escort_scene2_15", scene="street_rich_hotel")
    return True


label ep211_quests_escort6_scene7:
    if act=="l":
        return
    $ remove_objective("go_corridor")
    $ remove_hook(label="escort_scene7")
    $ move_object("ReceptionGirl", "rich_hotel_reception")
    $ autorun_to_object("ep216_dialogues2_escort_3", scene="street_rich_hotel")
    $ monicaEscortScene7LastDay = day
    $ set_active("Visitor2", True, scene="rich_hotel_restaurant")
    $ set_active("Visitor3", True, scene="rich_hotel_restaurant")
    call ep216_dialogues2_escort_2() from _rcall_ep216_dialogues2_escort_2
    $ questHelp("escort_13", True)
#    $ questHelp("escort_14", skipIfExists=True)
    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_17

    return False







#
