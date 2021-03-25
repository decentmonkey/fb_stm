default ep214_dialogues3_escort_10_flag1 = False
default ep214_dialogues3_escort_10_flag2 = False
default ep214_dialogues3_escort_6b_flag = False

label ep214_quests_escort1:
    call ep214_dialogues3_escort_1() from _rcall_ep214_dialogues3_escort_1
    if _return == False:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_105
        return False
    call ep214_dialogues3_escort_2() from _rcall_ep214_dialogues3_escort_2
    if _return == False: # увольнение
        call bitch(20, "escort4") from _rcall_bitch_13
#        call ep212_dialogues3_escort_hotel_5_1()
        $ questsFailByCategory(t_("ВИП-ЭСКОРТ"))
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_11
        return False
    call ep214_dialogues3_escort_3() from _rcall_ep214_dialogues3_escort_3
    if _return == -1: # увольнение
        $ questHelp("escort_9", False)
        $ questsFailByCategory(t_("ВИП-ЭСКОРТ"))
        call bitch(20, "escort4") from _rcall_bitch_14
        call ep212_dialogues3_escort_hotel_5_1() from _rcall_ep212_dialogues3_escort_hotel_5_1_3
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_12
        return False
    if _return == -2: # увольнение, укусила
        $ questHelp("escort_9", False)
        $ questsFailByCategory(t_("ВИП-ЭСКОРТ"))
        call bitch(20, "escort4") from _rcall_bitch_15
        call ep214_dialogues3_escort_4() from _rcall_ep214_dialogues3_escort_4
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_13
        return False
    # Моника все сделала
    call ep214_dialogues3_escort_5() from _rcall_ep214_dialogues3_escort_5
    $ questHelp("escort_9", True)
    $ questHelp("escort_11", skipIfExists=True)
    $ add_corruption(25, "escort4")
    $ autorun_to_object("ep211_escort_scene2_15", scene="street_rich_hotel")
    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_14
    return False


label ep214_quests_escort2:
    # сцена с местью
    call ep214_dialogues3_escort_6() from _rcall_ep214_dialogues3_escort_6
    if _return == False:
        return False
    $ ep214_dialogues3_escort_6b_flag = False
    $ richHotelLiftSceneSuffix = ""
    $ move_object("EscortCustomer1", "rich_hotel_lift")
    $ richHotelLiftMonicaSuffix = 2
    $ set_active("Teleport_Reception", False, scene="rich_hotel_lift")
    $ add_hook("EscortCustomer1", "ep214_dialogues3_escort_6b", scene="rich_hotel_lift", label="escort6")
    $ add_hook("Monica", "ep214_dialogues3_escort_6b", scene="rich_hotel_lift", label="escort6")
    $ add_hook("Lift", "ep214_quests_escort2b", scene="rich_hotel_lift", label="escort6")
    call change_scene("rich_hotel_lift", "Fade_long", "snd_lift") from _rcall_change_scene_135
    return True


label ep214_quests_escort2b:
    if act=="l":
        return
    if ep214_dialogues3_escort_6b_flag == False:
        call ep214_dialogues3_escort_6b() from _rcall_ep214_dialogues3_escort_6b
    $ remove_hook(label="escort6")
    $ richHotelLiftSceneSuffix = "_Closed"
    $ richHotelLiftMonicaSuffix = 1
    $ move_object("EscortCustomer1", "empty")
    $ set_active("Teleport_Reception", True, scene="rich_hotel_lift")
    sound snd_lift
    call ep214_dialogues3_escort_7() from _rcall_ep214_dialogues3_escort_7
    $ questHelp("escort_11", True)
    if _return == False:
        $ questHelp("escort_8", False)
        $ autorun_to_object("ep214_dialogues3_escort_9", scene="street_rich_hotel")
        $ add_money(100.0)
        call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_15
        return True
    $ questHelp("escort_8", True)
    call bitch(15, "escort6") from _rcall_bitch_16
    $ autorun_to_object("ep214_dialogues3_escort_8", scene="street_rich_hotel")
    $ ep214_dialogues3_escort_10_flag1 = True
    $ ep214_dialogues3_escort_10_flag2 = True
    call ep211_quests_escort2_end_day() from _rcall_ep211_quests_escort2_end_day_16
    $ add_money(300.0)
    return False

















#
