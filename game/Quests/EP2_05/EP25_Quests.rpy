default ep25_quests1Flag1 = False
default ep25_quests1Flag2 = False
default ep25_quests8Flag1 = False

label ep25_quests1:
    # Моника пытается зайти в здание Стива
    if ep25_quests1Flag1 == False:
        $ monicaPussyShaved = True # Бреем Монику
        $ ep25_quests1Flag1 = True
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_dialogues1_shop1b", scene="street_cloth_shop", label="cloth_shop_closed")
    if monicaAskedVictoriaAboutSteveMoney == False and monicaHasSexWithSteveBasement == True:
        call ep25_dialogues1_shop1() from _call_ep25_dialogues1_shop1
        return False
    if ep25_quests1Flag2 == False:
        $ ep25_quests1Flag2 = True
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop1", scene="street_cloth_shop")

    $ add_objective("find_casual_dress", t_("Найти нормальную одежду"), c_orange, 15)
    call ep25_dialogues1_shop1a() from _call_ep25_dialogues1_shop1a
    $ questHelp("steve_7", True)
    $ questHelp("shop_1")
    return False

label ep25_quests2:
    # Инициализируем новое платье в окружающем мире
    $ add_hook("photoshoots_work_available_check", "ep25_quest9", scene="global", label="weekly_money_check")

    call ep25_quests_steve1() from _call_ep25_quests_steve1 # Офис Стива
    $ add_hook("Teleport_Inside", "ep25_quests3", scene="street_dick_office", label="dick_office_enter_dress_check", priority = 200) # Вход в офис Дика
    $ add_hook("Teleport_Shawarma", "ep25_quests4", scene="street_cloth_shop", label="casual_dress_slums_forbidden", priority = 900) # Переодевание в трущобах
    $ remove_hook(label="street_house_check_cloth_outside")
    $ add_hook("Teleport_House_Gate", "ep25_quests6", scene="street_house_outside", label="street_house_check_cloth_outside", priority = 200) # Проверка при входе в ворота дома
    $ add_hook("Teleport_Floor1_Stairs", "ep25_quests7", scene="basement_pool", label="street_house_check_cloth_outside", priority = 200) # Проверка при выходе в дом из бассейна
    $ remove_hook(label="house_dark_passage")
    $ add_hook("Teleport_Basement_Side", "ep25_quests8", scene="basement_hole", label="house_dark_passage") # Активируем черный ход
    $ add_hook("map_teleport", "ep25_quests4a", scene="global", label="casual_dress_slums_forbidden", priority = 900) # Переодевание в трущобах
    $ add_hook("before_open", "ep25_quests5", scene = "street_house_main_yard", label="street_house_check_cloth_outside", priority = 200) # Проверка на вход в дом (Моника оказывается снаружи)
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Outside_Monica_[cloth][day_suffix]", "click" : "street_house_outside_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, {"cloth":{"v":"CasualDress1", "base":"Street_House_Outside_Monica_[cloth]_[street_house_outside_monica_suffix][day_suffix]"}}, scene="street_house_outside")
    call wardrobeBasementCasualDressMiniMap1() from _call_wardrobeBasementCasualDressMiniMap1
    return

label ep25_quests3:
    # Проверка на вход в офис Дика в платье
    if ep216_victoria_visit_day1 > 0 and cloth_type != "Whore":
        call ep216_dialogues5_victoria_8() from _rcall_ep216_dialogues5_victoria_8
        return False
    if cloth == "CasualDress1":
        call ep25_dialogues1_shop18() from _call_ep25_dialogues1_shop18
        return False
    return

label ep25_quests4:
    # Переодевание перед перемещением в трущобы
    if cloth == "CasualDress1" or cloth_type == "CasualDress":
        call ep25_dialogues4_map1() from _call_ep25_dialogues4_map1
        if _return == False:
            return False
        sound snd_fabric1
        img black_screen
        with diss
        pause 1.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"

    return

label ep25_quests4a:
    # Переодевание перед перемещением в трущобы
    if cloth == "CasualDress1" or cloth_type == "CasualDress":
        if obj_name == "Teleport_Street_Corner" or obj_name == "Teleport_Hostel2":
            call ep25_dialogues4_map1() from _call_ep25_dialogues4_map1_1
            if _return == False:
                return False
            sound snd_fabric1
            img black_screen
            with diss
            pause 1.0
            $ cloth = "Whore"
            $ cloth_type = "Whore"

    return

label ep25_quests5:
    # Проверка на платье при переходе в дом по карте (перекидываем наружу если одето платье)
    if cloth == "CasualDress1" or cloth == "SchoolOutfit1":
        call change_scene("street_house_outside", "Fade_long", "highheels_run2") from _call_change_scene_273
    return

label ep25_quests6:
    # Проверка на платье при входе в ворота дома
    if cloth == "CasualDress1":
        call ep25_dialogues4_map2() from _call_ep25_dialogues4_map2
        $ basementHoleIncomingDirection = "Laundry"
        call change_scene("basement_hole", "Fade_long") from _call_change_scene_274
        return False

    if cloth == "SchoolOutfit1":
        call dialogue_classmate_4a() from _call_dialogue_classmate_4a
        $ basementHoleIncomingDirection = "Laundry"
        call change_scene("basement_hole", "Fade_long") from _call_change_scene_412
        return False
    return

label ep25_quests7:
    # Проверка на платье при попытке выхода на лестницу из бассейна дома
    if cloth == "CasualDress1":
        call ep25_dialogues4_map3() from _call_ep25_dialogues4_map3
        return False
    if cloth == "SchoolOutfit1":
        call dialogue_classmate_4a() from _call_dialogue_classmate_4a_1
        return False
    return

label ep25_quests8:
    # Выход из дома через черный ход
    if cloth_type == "Governess":
        call ep25_dialogues4_map6() from _call_ep25_dialogues4_map6
        return False
    if ep25_quests8Flag1 == False:
        $ ep25_quests8Flag1 = True
        call ep25_dialogues4_map4() from _call_ep25_dialogues4_map4
        $ autorun_to_object("ep25_dialogues4_map5", scene="street_house_outside")
    $ street_house_outside_monica_suffix = 1
    call change_scene("street_house_outside", "Fade_long") from _call_change_scene_275
    return False

label ep25_quest9:
    # фотосессию у Бифе нельзя сделать, если уже заработаны деньги для Виктории
    if monicaEarnedWeeklyMoney == True: # если уже заработаны деньги
        return False # то фотосессия заблокирована
    return
