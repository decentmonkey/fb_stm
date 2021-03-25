default slumsApartmentsStatus = 0
default slumsApartmentsInited1 = False

default slumsApartmentsRentStarted = False
default slumsApartmentsRentStartedDay = 0
default slumsApartmentsRentActive = False
default slumsApartmentsRentActiveDay = 0
default slumsApartmentsMonicaKnow = False

default slumsApartmentsSkipFirstSaturdayActive = False

default ep211_slums_apartments_quest5_apartments_block_count = 0

label ep211_slums_apartments_quest1_menu:
    if slumsApartmentsStatus == 0: # Первый разговор
        call ep211_dialogues6_slum_apartment_3() from _rcall_ep211_dialogues6_slum_apartment_3
        if _return == 0:
            return True
        if _return == -1:
            return False
        if slumsApartmentsInited1 == False:
            call ep211_quests_slums_apartments1_init() from _rcall_ep211_quests_slums_apartments1_init
            call ep211_quests_slums_apartments1_inita() from _rcall_ep211_quests_slums_apartments1_inita
        else:
            call ep211_quests_slums_apartments1_inita() from _rcall_ep211_quests_slums_apartments1_inita_1
        $ slumsApartmentsMonicaKnow = True
        $ remove_objective("ask_kebab")
        $ add_hook("HomeEnter", "ep211_slums_apartments_quest2_enter_home", scene="street_monicahome", label="jack_apartments1")
        $ add_hook("MonicaWindow", "ep211_slums_apartments_quest2_enter_home", scene="street_monicahome", label="jack_apartments1")
        $ add_hook("Shawarma_Trader", "ep211_slums_apartments_quest1_jack", scene="street_monicahome", label="jack_apartments1")
        $ set_active("Street_MonicaHome_TeleportSlums", False, scene="street_monicahome")

        $ autorun_to_object("ep211_dialogues6_slum_apartment_5", scene="street_monicahome")
        #$ move_object("Shawarma_Trader", "whores_place_shawarma")
        $ move_object("Shawarma_Trader", "street_monicahome")
        $ streetMonicaHomeMonicaSuffix = 0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
        $ map_enabled = False
        $ monicaHomeMiniMapEnabled = False
        $ hudDaySkipToEveningEnabled = False
        music stop
        img black_screen
        with diss
        pause 2.0
        call change_scene("street_monicahome", "Fade_long", False) from _rcall_change_scene_4
        return False

    if slumsApartmentsStatus == 1: # Повторный разговор о заселении
        call ep211_dialogues6_slum_apartment_17() from _rcall_ep211_dialogues6_slum_apartment_17
        if _return == 0:
            return True
        $ remove_objective("talk_jack")
        if _return == -1:
            return False
        # Запускаем Монику в квартиру
        $ monicaHomeMiniMapEnabled = True
        $ slumsApartmentsRentActive = True
        $ slumsApartmentsRentActiveDay = day
        $ remove_hook(label="slums_apartments_blocked")
        $ add_objective("earn_money_rent_apartments", t_("Заработать $ 300 за аренду апартаментов до субботы."), c_green, 30)
        $ slumsApartmentsStatus = 2
        return False

    if slumsApartmentsStatus == 2:
        return True


    return False

label ep211_slums_apartments_quest1_jack:
    if act=="l":
        return
    call ep211_dialogues6_slum_apartment_5() from _rcall_ep211_dialogues6_slum_apartment_5
    return False

label ep211_slums_apartments_quest2_enter_home:
    if act=="l":
        call ep211_dialogues6_slum_apartment_4() from _rcall_ep211_dialogues6_slum_apartment_4
        return False
    $ slumsEnterClothStored = cloth
    $ slumsEnterClothTypeStored = cloth_type
    $ set_active("Teleport_Bathroom", False, scene="monicahome_livingroom")
    $ set_active("Teleport_Kitchen", False, scene="monicahome_livingroom")
    $ set_active("Teleport_Wardrobe", False, scene="monicahome_livingroom")
    $ set_active(False, teleport=True, scene="monicahome_livingroom")
    $ set_active(False, group="environment", scene="monicahome_livingroom")
    $ set_active("Cocktail", True, scene="monicahome_livingroom")
    $ move_object("Shawarma_Trader", "monicahome_livingroom")
    $ add_hook("Cocktail", "ep211_dialogues6_slum_apartment_4", scene="monicahome_livingroom", label="jack_apartments1")
    $ add_hook("Monica", "ep211_dialogues6_slum_apartment_4", scene="monicahome_livingroom", label="jack_apartments1")
    $ add_hook("Shawarma_Trader", "ep211_slums_apartments_quest3_jack", scene="monicahome_livingroom", label="jack_apartments1")
    call change_scene("monicahome_livingroom", "Fade_long", "snd_door_open1") from _rcall_change_scene_5
    return False

label ep211_slums_apartments_quest3_jack:
    if act=="l":
        return
    $ define_inventory_object("keys_apartments", {"description" : t_("Ключи от дома в трущобах"), "label_suffix" : "_use_keys_apartments", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/keys_apartments" + res.suffix + ".png"})
    call ep211_dialogues6_slum_apartment_6() from _rcall_ep211_dialogues6_slum_apartment_6
    if _return == 0 or _return == -1:
#        if _return == -1:
#            $ slumsApartmentsStatus = 1
        $ remove_hook(label="jack_apartments1")
        $ del(map_objects["Teleport_Slums_Apartments"])
        $ set_active("Teleport_Slums_Apartments", False, scene="hostel_street")
        $ move_object("Shawarma_Trader", "whores_place_shawarma")
        $ slumsApartmentsMiniMapActive = False
        $ slumsDirtyStreetMiniMapActive = True
        $ map_enabled = True
        $ hudDaySkipToEveningEnabled = True
        $ questHelp("flat_slums_2", False)

        call change_scene("hostel_street", "Fade_long") from _rcall_change_scene_6
        return False
    $ questHelp("flat_slums_2", True)
    $ questHelp("flat_slums_3", skipIfExists=True)
    $ questHelpDesc("flatslums_desc1")

    $ slumsApartmentsStatus = 1
    $ slumsApartmentsRentStarted = True
    $ slumsApartmentsRentStartedDay = day
    $ slumsApartmentsRentActive = True
    $ slumsApartmentsRentActiveDay = day
    $ questLog(71, True)
    $ add_objective("earn_money_rent_apartments", t_("Заработать $ 300 за аренду апартаментов до субботы."), c_green, 30)
    $ remove_hook(label="jack_apartments1")
    $ set_active("Teleport_Bathroom", True, scene="monicahome_livingroom")
    $ set_active("Teleport_Kitchen", True, scene="monicahome_livingroom")
    $ set_active("Teleport_Wardrobe", True, scene="monicahome_livingroom")
    $ set_active("Street_MonicaHome_TeleportSlums", True, scene="street_monicahome")
    $ set_active(True, teleport=True, scene="monicahome_livingroom")
    $ set_active(True, group="environment", scene="monicahome_livingroom")
    $ move_object("Shawarma_Trader", "whores_place_shawarma")
    $ cloth = "HomeCloth4"
    $ cloth_type = "HomeCloth"
    $ map_enabled = True
    $ monicaHomeMiniMapEnabled = True
    $ hudDaySkipToEveningEnabled = True
    $ autorun_to_object("ep211_dialogues6_slum_apartment_7", scene="monicahome_livingroom")
    if week_day > 3 and week_day != 7:
        $ slumsApartmentsSkipFirstSaturdayActive = True
    $ slumsApartmentsStatus = 2
    $ add_hook_day("ep211_slums_apartments_quest4_check_payment", week_day = 6)

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_3
    return False


label ep211_slums_apartments_quest4_check_payment:
    if slumsApartmentsRentActive == False:
        return
    if slumsApartmentsSkipFirstSaturdayActive == True:
        $ slumsApartmentsSkipFirstSaturdayActive = False
        return
    if monicaRestApartments == False:
        if money >= slumsApartmentsRentPrice:
            $ notif(t_("Оплата за апартаменты в трущобах."))
            $ slumsApartmentsRentActive = True
            $ add_money(-slumsApartmentsRentPrice)
        else:
            $ notif(t_("Оплата за апартаменты в трущобах просрочена!"))
            $ slumsApartmentsRentActive = False
            $ monicaHomeMiniMapEnabled = False
            $ add_hook("HomeEnter", "ep211_slums_apartments_quest5_apartments_block", scene="street_monicahome", label="slums_apartments_blocked")
            $ add_hook("MonicaWindow", "ep211_slums_apartments_quest5_apartments_block", scene="street_monicahome", label="slums_apartments_blocked")
            $ slumsApartmentsStatus = 1
            $ remove_objective("earn_money_rent_apartments")
        return
    else:
        # сцена оплаты
        $ cloth = "HomeCloth4"
        $ cloth_type = "HomeCloth"
        call ep211_dialogues6_slum_apartment_10() from _rcall_ep211_dialogues6_slum_apartment_10
        if _return == -1: # нет денег
            music stop
            img black_screen
            with diss
            sound snd_plates2
            $ renpy.pause(3.0, hard=True)
            sound2 snd_door_close1
            $ move_object("Shawarma_Trader", "monicahome_livingroom") # Продавец у Моники дома
            # Блокировка до оплаты
            $ add_hook("HomeEnter", "ep211_slums_apartments_quest5_apartments_block", scene="street_monicahome", label="slums_apartments_blocked")
            $ add_hook("MonicaWindow", "ep211_slums_apartments_quest5_apartments_block", scene="street_monicahome", label="slums_apartments_blocked")
            # Блокировка до вечера
            $ add_hook("HomeEnter", "ep211_dialogues6_slum_apartment_14", scene="street_monicahome", label=["slums_apartments_blocked2", "day_time_temp"])
            $ add_hook("MonicaWindow", "ep211_dialogues6_slum_apartment_14", scene="street_monicahome", label=["slums_apartments_blocked2", "day_time_temp"])

            $ monicaHomeMiniMapEnabled = False
            $ slumsApartmentsRentActive = False
            $ map_enabled = False
            $ add_hook("exit_scene", "ep211_slums_apartments_quest6_return_jack", scene="street_monicahome", label="slums_apartments_blocked2")
            $ slumsApartmentsStatus = 1
            $ remove_objective("earn_money_rent_apartments")
            $ cloth = slumsEnterClothStored
            $ cloth_type = slumsEnterClothTypeStored
            if cloth_type == "SchoolOutfit":
                $ cloth = "Whore"
                $ cloth_type = "Whore"
            $ add_hook("enter_scene", "ep211_dialogues6_slum_apartment_13", scene="street_monicahome", once=True)
            call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_7
            return False
        if _return == 1:
            # оплата полностью
            return
        if _return == 2: #скидка 10%
            call ep211_dialogues6_slum_apartment_11() from _rcall_ep211_dialogues6_slum_apartment_11
            $ questHelpFlag18 = True
            $ questHelp("flat_slums_3", True)
            $ add_corruption(slumsApartmentsRentPriceDiscount10CorruptionAdd, "slums_apartments_discount_day" + str(day))
            return

    return

label ep211_slums_apartments_quest5_apartments_block: # В квартиру не зайти
    $ ep211_slums_apartments_quest5_apartments_block_count += 1
    if ep211_slums_apartments_quest5_apartments_block_count == 1:
        # первый раз
        call ep211_dialogues6_slum_apartment_15() from _rcall_ep211_dialogues6_slum_apartment_15
        return False
    call ep211_dialogues6_slum_apartment_16() from _rcall_ep211_dialogues6_slum_apartment_16
    $ add_objective("talk_jack", t_("Поговорить с Джеком и снова заселиться в квартиру."), c_blue, 105)

    return False

label ep211_slums_apartments_quest6_return_jack: # Джек возвращается к торговле
    $ move_object("Shawarma_Trader", "whores_place_shawarma") # Продавец у Моники дома
    $ remove_hook(label="slums_apartments_blocked2")
    $ map_enabled = True
    return

label HomeEnter_use_keys_apartments:
    call process_object_click_forced("HomeEnter", "w") from _rcall_process_object_click_forced
    return
label MonicaWindow_use_keys_apartments:
    call process_object_click_forced("MonicaWindow", "w") from _rcall_process_object_click_forced_1
    return
