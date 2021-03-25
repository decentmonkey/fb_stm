default monica_escort_service_started = False
default monica_escort_service_started_day = 0
default restaurant_block_return_flag_once = False

default ep210_quests_escort_stage = 0
default monica_philip_visits = 0
default monica_philip_visits_stage = 1
default ep210_quests_escort1_philip3_map_flag = False
default monica_philip_visited_last_day = 0
default monica_philip_visit_whore1_exists = False
default monica_philip_visits_blowjobs = 0
default monica_philip_visits_sex = 0
default monica_philip_visits_swallowed = 0
default monica_philip_visits_double_blowjobs = 0
default monica_philip_visits_threesomes = 0

default ep210_quests_escort_staff_refused = False

label ep210_quests_escort_eat_process:
    if ep210_quests_escort_stage == 0 and ep22_quests_monica_presentation_completed == True:
        call ep210_quests_escort1_philip1() from _call_ep210_quests_escort1_philip1
        return False
    if ep210_quests_escort_stage == 1 and ep210_quests_escort_staff_refused == False:
        call ep210_quests_escort1_hotel_staff1() from _call_ep210_quests_escort1_hotel_staff1
        $ restaurant_block_return_flag_once = True
        return False
    return


label ep210_quests_escort1_philip1: # Первая встреча с Филиппом в ресторане
    # Приходит Филипп
    $ add_hook("Teleport_Street_Rich_Hotel", "ep210_quests_escort_reception1", scene="rich_hotel_reception", label="ep210_quests_escort_reception1")
    $ add_hook("ReceptionGirl", "ep210_quests_escort_reception1", scene="rich_hotel_reception", label="ep210_quests_escort_reception1")
    call rich_hotel_reception_init2() from _call_rich_hotel_reception_init2  # Инициализация локации рецепшина
    call ep210_dialogues2_escort_start_Phillip_1() from _call_ep210_dialogues2_escort_start_Phillip_1
    if _return == False:
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        $ move_object("Philip", "rich_hotel_reception")
        $ add_hook("Philip", "ep210_quests_escort1_philip2", scene="rich_hotel_reception", label="ep210_quests_escort1_philip2")
        $ questHelp("escort_1", False)
        $ questHelp("philip_3", False)
        $ questHelp("philip_4", False)
        $ ep210_quests_escort_stage = -1
        call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_475
        return

    $ questHelp("philip_3", True)
    # Секс в туалете
    music stop
    img black_screen
    with diss
    pause 2.0
    call ep210_dialogues2_escort_start_Phillip_2() from _call_ep210_dialogues2_escort_start_Phillip_2
    if _return == 1: # Моника отказалась, но возможен возврат
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        $ move_object("Philip", "rich_hotel_reception")
        $ add_hook("Philip", "ep210_quests_escort1_philip2", scene="rich_hotel_reception", label="ep210_quests_escort1_philip2")
        $ questHelp("philip_4", False)
        $ ep210_quests_escort_stage = -1
        call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_476
        return

    if _return == 2: # Моника ударила Филиппа
        $ questHelp("escort_1", False)
        $ questHelp("philip_4", False)
        $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_4", scene="street_rich_hotel")
        $ ep210_quests_escort_stage = -1
        call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_477

        return

    $ questHelp("escort_1")
    $ questHelp("philip_4")
    $ questHelpDesc("philip_desc2", "philip_desc3")
    $ questLog(61, True)
    $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_3", scene="street_rich_hotel")
    $ add_money(300.0)
    sound2 fx_coins
    # Инициализируем дом Филиппа
    call locations_init_philip_home() from _call_locations_init_philip_home
    $ map_objects ["Teleport_PhilipHome"] = {"text" : t_("ДОМ ФИЛИППА"), "xpos" : 1767, "ypos" : 242, "base" : "map_marker", "state" : "visible"}
    $ add_hook("map_teleport", "ep210_quests_escort1_philip3_map", scene="global", label="philiphome_outfit_restrict")
    $ add_hook("Teleport_Building", "ep210_quests_escort1_philip4_enter", scene="street_philiphome")

    # Инициализируем дальнейший прогресс в escort service
    $ ep210_quests_escort_stage = 1

    call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_478
    return

label ep210_quests_escort1_philip2: # Повторный квест с Филиппом
    $ remove_hook()
    call ep210_dialogues2_escort_start_Phillip_3a() from _call_ep210_dialogues2_escort_start_Phillip_3a
    $ move_object("Philip", "empty")
    $ ep210_quests_escort_stage = 0
    call refresh_scene_fade() from _call_refresh_scene_fade_210
    return


label ep210_quests_escort_reception1: # Рецепшин перехватывает Монику
    $ remove_hook(label="ep210_quests_escort_reception1")
    call ep210_dialogues2_escort_start_Phillip_5() from _call_ep210_dialogues2_escort_start_Phillip_5
    call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_479
    return False

label ep210_quests_escort1_philip3_map: # Проверка на одежду на карте у Филиппа
    if obj_name == "Teleport_PhilipHome":
        if cloth_type != "CasualDress":
            call ep210_dialogues2_escort_start_Phillip_11() from _call_ep210_dialogues2_escort_start_Phillip_11
            return False
        if ep210_quests_escort1_philip3_map_flag == False:
            call ep210_dialogues2_escort_start_Phillip_6() from _call_ep210_dialogues2_escort_start_Phillip_6
            $ ep210_quests_escort1_philip3_map_flag = True
        $ streetPhilipHomeMonicaSuffix = 1
    return

label ep210_quests_escort1_philip4_enter: # Вход к Филиппу домой
    if week_day != 6:
        call ep210_dialogues2_escort_start_Phillip_8() from _call_ep210_dialogues2_escort_start_Phillip_8
        return False
    if day_time != "evening":
        call ep210_dialogues2_escort_start_Phillip_9() from _call_ep210_dialogues2_escort_start_Phillip_9
        return False
    call ep210_dialogues2_escort_start_Phillip_7() from _call_ep210_dialogues2_escort_start_Phillip_7
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_211
        return False

    if monica_philip_visits_stage == 1:
        if monica_philip_visits % 2 == 1:
            # У Филиппа другая шлюха
            $ monica_philip_visit_whore1_exists = True
        else:
            $ monica_philip_visit_whore1_exists = False

        $ monica_philip_visits += 1
        call ep210_dialogues2_escort_start_Phillip_12() from _call_ep210_dialogues2_escort_start_Phillip_12
        if _return == False:
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            call refresh_scene_fade_long() from _call_refresh_scene_fade_long_33
            return False
        $ questHelp("philip_4", True)
        $ questHelp("philip_5", skipIfExists=True)
        $ questHelp("philip_6", skipIfExists=True)

        if monica_philip_visit_whore1_exists == True:
            music stop
            img black_screen
            with diss
            sound highheels_short_walk
            pause 1.5
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13a", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            $ move_object("Bitch1", "street_philiphome")
            $ add_hook("Bitch1", "ep210_quests_escort1_philip5_bitch1_street", scene="street_philiphome", label="ep210_quests_escort1_philip5_bitch1_street")
            $ add_hook("exit_scene", "ep210_quests_escort1_philip5_bitch1_street_leave", scene="street_philiphome", label="ep210_quests_escort1_philip5_bitch1_street")
            call refresh_scene_fade_long() from _call_refresh_scene_fade_long_34
            return False


        # Выбор действия
        call ep210_dialogues2_escort_start_Phillip_14() from _call_ep210_dialogues2_escort_start_Phillip_14
        if _return == 1:
            # Минет
            call ep210_dialogues2_escort_start_Phillip_15() from _call_ep210_dialogues2_escort_start_Phillip_15
            if _return == True:
                $ monica_philip_visits_blowjobs += 1
                $ add_corruption(monicaPhilipVisitBlowjobCorruption, "monicaPhilipVisitBlowjobCorruption" + str(day))
                $ add_money(100.0)
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_17", scene="street_philiphome")
            else:
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            call refresh_scene_fade_long() from _call_refresh_scene_fade_long_35
            return
        if _return == 2:
            # Секс
            call ep210_dialogues2_escort_start_Phillip_16() from _call_ep210_dialogues2_escort_start_Phillip_16
            if _return == True:
                $ questHelp("philip_5", True)
                $ monica_philip_visits_sex += 1
                $ add_corruption(monicaPhilipVisitSexCorruption, "monicaPhilipVisitBlowjobCorruption" + str(day))
                $ add_money(100.0)
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_17", scene="street_philiphome")
            else:
                $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
            $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
            $ streetPhilipHomeMonicaSuffix = 2
            call refresh_scene_fade_long() from _call_refresh_scene_fade_long_36
            return


    $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_13b", scene="street_philiphome")
    $ add_hook("Teleport_Building", "ep210_dialogues2_escort_start_Phillip_19", scene="street_philiphome", label=["philip_restict_day", "evening_time_temp"]) # Блок на вход к Филиппу в этот день
    $ streetPhilipHomeMonicaSuffix = 2
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_37
    return False


label ep210_quests_escort1_philip5_bitch1_street: # Шлюха окликает Монику на улице
    if act=="l":
        return
    $ remove_hook(label="ep210_quests_escort1_philip5_bitch1_street")
    call ep210_dialogues2_escort_start_Phillip_13() from _call_ep210_dialogues2_escort_start_Phillip_13
    if _return == False:
        $ move_object("Bitch1", "empty")
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_38
        return False
    call ep211_quests_philip() from _rcall_ep211_quests_philip
    return False

label ep210_quests_escort1_philip5_bitch1_street_leave:
    $ remove_hook(label="ep210_quests_escort1_philip5_bitch1_street")
    $ move_object("Bitch1", "empty")
    return

label ep210_quests_escort1_hotel_staff1: # К Монике подходит сотрудник отеля во время ужина
    call ep210_dialogues7_escort_hotel_1() from _call_ep210_dialogues7_escort_hotel_1
    $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_5", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
    if _return == False:
        $ autorun_to_object("ep210_dialogues7_escort_hotel_4", scene="street_rich_hotel")
        $ move_object("HotelStaff", "rich_hotel_reception")
        $ add_hook("HotelStaff", "ep210_quests_escort1_hotel_staff2", scene="rich_hotel_reception", label="ep210_quests_escort1_hotel_staff2")
        $ ep210_quests_escort_staff_refused = True
        $ questHelp("escort_1", False)
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_480
        return

    # Минет в корридоре
    call ep210_dialogues7_escort_hotel_2() from _call_ep210_dialogues7_escort_hotel_2
    if _return == False:
        $ autorun_to_object("ep210_dialogues7_escort_hotel_4", scene="street_rich_hotel")
        $ move_object("HotelStaff", "rich_hotel_reception")
        $ add_hook("HotelStaff", "ep210_quests_escort1_hotel_staff2", scene="rich_hotel_reception", label="ep210_quests_escort1_hotel_staff2")
        $ ep210_quests_escort_staff_refused = True
        $ questHelp("escort_1", False)
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_481
        return

    $ questHelp("escort_1", True)
    $ questHelp("escort_2")
    $ ep210_quests_escort_stage = 2
    $ autorun_to_object("ep210_dialogues7_escort_hotel_3", scene="street_rich_hotel")
    $ add_hook("Teleport_Restaurant", "ep210_quests_escort1_reception", scene="rich_hotel_reception", label="ep210_quests_escort1_reception")
    call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_482
    return

label ep210_quests_escort1_hotel_staff2: # Старт прихода сотрудника отеля снова
    $ remove_hook()
    call ep210_dialogues2_escort_start_HotelStaff_3b() from _call_ep210_dialogues2_escort_start_HotelStaff_3b
    $ move_object("HotelStaff", "empty")
    $ ep210_quests_escort_staff_refused = False
    call refresh_scene_fade() from _call_refresh_scene_fade_236
    return

label ep210_quests_escort1_reception: # Разговор с рецепшин о начале escort service
    call ep210_dialogues7_escort_hotel_6() from _call_ep210_dialogues7_escort_hotel_6
    if _return == False:
        $ autorun_to_object("ep210_dialogues7_escort_hotel_7b", scene="street_rich_hotel")
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_5", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_483
        $ questHelp("escort_2", False)
        return False

    $ questHelp("escort_2", True)
    # Кастинг в корридоре
    call ep210_dialogues7_escort_hotel_7() from _call_ep210_dialogues7_escort_hotel_7
    if _return == False:
        $ questHelp("escort_3", False)
        $ autorun_to_object("ep210_dialogues7_escort_hotel_7b", scene="street_rich_hotel")
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_5", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_484
        return False

    $ questHelp("escort_3", True)

    # Старт эскорта
    $ monica_escort_service_started = True
    $ monica_escort_service_started_day = day
    $ remove_hook(label="ep210_quests_escort1_reception")
    $ remove_hook(label="reception_capturing_monica")
    $ add_objective("start_escort", t_("Прийти в отель ЛеГранд завтра."), c_pink, 90)
    $ questLog(62, True)
    $ autorun_to_object("ep210_dialogues7_escort_hotel_7a", scene="street_rich_hotel")

    $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_7e", scene="street_rich_hotel", label="hotel_escort_enter1", once=True) # Комментарий при входе в отель
    $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_7c", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня

    # Вешаем обработку эскорта на вход в ресторан и на рецепшин
    $ add_hook("Teleport_Restaurant", "ep210_quests_escort2", scene="rich_hotel_reception", label="ep210_quests_escort2")
    $ add_hook("ReceptionGirl", "ep210_quests_escort2_reception", scene="rich_hotel_reception", label="ep210_quests_escort2")

    call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _rcall_change_scene_2

    return False

label ep210_quests_escort2: # Входит в отель на следующий день
    $ remove_objective("start_escort")
    call ep210_dialogues7_escort_hotel_8_menu() from _call_ep210_dialogues7_escort_hotel_8_menu
    if _return == 1:
        if richHotelMonicaEatedDay == day:
            call ep26_dialogues4_restaurant5() from _call_ep26_dialogues4_restaurant5_2
            return False
        call ep210_dialogues7_escort_hotel_8_enter_restaurant() from _call_ep210_dialogues7_escort_hotel_8_enter_restaurant
        # Входим в ресторан
        call change_scene("rich_hotel_restaurant_entrance", "Fade_long") from _call_change_scene_486
        return False
    if _return == 2:
        call ep211_quests_escort1() from _rcall_ep211_quests_escort1

    return False

label ep210_quests_escort2_reception:
    if act=="l":
        return
    call ep210_quests_escort2() from _call_ep210_quests_escort2
    return _return










#
