default ep212_escort_monica_fired = False
default ep212_escort3_monica_fired = False

default ep212_escort3_completed = False

default ep212_escort5_completed = False
default ep212_escort5_monica_fired = False

# сцена 3 эскорта
label ep212_escort3_1:
    call ep212_dialogues3_escort_hotel_1() from _rcall_ep212_dialogues3_escort_hotel_1 # Моника за столиком в ресторане, разговор с официанткой
    $ add_objective("go_reception", t_("Пойти на ресепшн к администратору."), c_orange, 135)
    $ add_hook("MonicaTable", "ep211_escort_scene1_17", scene="rich_hotel_restaurant", label="escort3")
    $ add_hook("Teleport_Street_Rich_Hotel", "ep211_escort_scene1_17", scene="rich_hotel_reception", label="escort3")
    $ add_hook("ReceptionGirl", "ep212_escort3_1a", scene="rich_hotel_reception", label="escort3")
    return

label ep212_escort3_1a:
    if act=="l":
        return
    call ep212_dialogues3_escort_hotel_2() from _rcall_ep212_dialogues3_escort_hotel_2
    $ remove_objective("go_reception")
    $ add_hook("Teleport_Reception", "ep212_dialogues3_escort_hotel_2_1", scene="rich_hotel_lift", label="escort3")
    call rich_hotel_lift_init2() from _rcall_rich_hotel_lift_init2
    $ move_object("Visitor3", "rich_hotel_lift")
    $ add_hook("Visitor3", "ep212_dialogues3_escort_hotel_2_1", scene="rich_hotel_lift", label="escort3")
    $ add_hook("Lift", "ep212_escort3_2", scene="rich_hotel_lift", label="escort3")
    $ richHotelLiftSceneSuffix = ""
    $ richHotelLiftMonicaSuffix = 3
    $ autorun_to_object("ep212_dialogues3_escort_hotel_2_1", scene= "rich_hotel_lift")
    call change_scene("rich_hotel_lift", "Fade_long") from _rcall_change_scene_77

    return False

label ep212_escort3_2: # сцена
    if act=="l":
        return
    $ richHotelLiftSceneSuffix = "_Closed"
    $ richHotelLiftMonicaSuffix = 1
    $ ep212_escort3_completed = False
    $ move_object("Visitor3", "rich_hotel_restaurant")
    $ set_active("Visitor3", True, scene="rich_hotel_restaurant_entrance")
    $ remove_hook(label="escort3")
    call ep212_dialogues3_escort_hotel_3() from _rcall_ep212_dialogues3_escort_hotel_3
    if _return == 0: # прерывание сцены
        call ep212_dialogues3_escort_hotel_5() from _rcall_ep212_dialogues3_escort_hotel_5
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7", scene="street_rich_hotel")
    if _return == -1: # увольнение
        call ep212_dialogues3_escort_hotel_5_1() from _rcall_ep212_dialogues3_escort_hotel_5_1
        $ ep212_escort_monica_fired = True
        $ ep212_escort3_monica_fired = True
        $ questsFailByCategory(t_("ВИП-ЭСКОРТ"))
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
#        call change_scene("street_rich_hotel", "Fade_long")
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_6
        $ questHelp("escort_6", False)
        return False
    if _return == 1: # сцена завершена успешно
        call ep212_dialogues3_escort_hotel_4() from _rcall_ep212_dialogues3_escort_hotel_4
        call ep212_dialogues3_escort_hotel_5() from _rcall_ep212_dialogues3_escort_hotel_5_2
        $ ep212_escort3_completed = True
        $ autorun_to_object("ep212_dialogues3_escort_hotel_6", scene="street_rich_hotel")
        $ escortRestaurantEnterForced = 1


    $ questHelp("escort_6", True)
    $ questHelp("escort_7", skipIfExists=True)
    $ questHelp("escort_8", skipIfExists=True)
    $ questHelpDesc("escort_desc1", "escort_desc2")
#    $ questHelp("escort_8", skipIfExists=True)
#    $ questHelpDesc("escort_desc2")

    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_7
    call change_scene("street_rich_hotel", "Fade_long") from _rcall_change_scene_78
    return False

label ep212_escort4_1:
    call ep212_dialogues3_escort_hotel_8() from _rcall_ep212_dialogues3_escort_hotel_8
    if _return == True:
        return True
    call refresh_scene_fade() from _rcall_refresh_scene_fade_48
    return False



























#
