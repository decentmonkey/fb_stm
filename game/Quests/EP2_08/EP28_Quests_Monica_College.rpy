default ep28_monica_eric_meeting_completed = False
default ep28_monica_bardie_eric_college_inited = False
default ep28_monica_bardie_eric_quest_stage = 0
default monicaHasSchoolOutfit1 = False
default monicaBoughtSchoolOutfitByLicking = False
default monicaHasSchoolOutfit1Day = 0
default monicaEricQuest1Stage = 0
default ep28_monica_bardie_eric_college4_visit1_data = 0
default monicaBettyLesbian = False # у Моники и Бетти было лесби

label ep28_monica_bardie_init:
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_college_check_bardie_bedroom_clothes", scene="floor2", priority = 300, label="bedroom_bardie_check_cloth")
#    $ add_hook("basement_monica_after_nap", "ep28_monica_bardie_init2", scene="global", once=True)
    $ add_hook("enter_scene", "ep28_monica_bardie_init2", scene="basement_bedroom2", label="ep28_monica_bardie_init")
    return

label ep28_monica_bardie_init2: #next day
    if day_time != "evening":
        return
    $ remove_hook()
    call ep28_betty_college_init() from _call_ep28_betty_college_init # инициализируем линию Бетти по колледжу
#    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_meeting", scene="floor2", label="bardie_eric_meeting")
    return

label ep28_monica_college_check_bardie_bedroom_clothes:
    if cloth_type != "Governess" and get_active_objects("Bardie", scene="bedroom_bardie") != False:
        call dialogue_betty_college_7_cloth() from _call_dialogue_betty_college_7_cloth
        return False
    return

label ep28_monica_bardie_eric_meeting_init: # Инициализация знакомства с Эриком
    $ add_hook("enter_scene", "ep28_monica_bardie_eric_meeting_a", scene="basement_bedroom2", label="ep28_monica_bardie_eric_meeting_a")
    return

label ep28_monica_bardie_eric_meeting_a:
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_1() from _call_dialogue_classmate_1

    $ map_enabled = False
    $ miniMapEnabledOnly = ["Floor2", "Basement"]
    call refresh_scene_fade() from _call_refresh_scene_fade_184
    $ autorun_to_object("dialogue_classmate_1b", scene="basement_bedroom2")
    $ add_objective("go_to_bardie", t_("Идти к Барди в комнату"), c_orange, 45)
    $ move_object("Betty", "empty")

    $ add_hook("Teleport_Basement_Side", "dialogue_classmate_1c", scene="basement_hole", label="monica_bardie_eric_meeting_block")
    $ add_hook("Teleport_Street", "dialogue_classmate_1c", scene="floor1", label="monica_bardie_eric_meeting_block")
    $ add_hook("Teleport_Kitchen", "dialogue_classmate_1c", scene="floor1", label="monica_bardie_eric_meeting_block")
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_meeting", scene="floor2", label="monica_bardie_eric_meeting", priority = 100)
    $ monicaLastCleaningOfferedDay = day
    return

label ep28_monica_bardie_eric_meeting: # Знакомство с Эриком (Моника заходит вечером к Барди)
    if day_time != "evening":
        return
    call dialogue_classmate_1a() from _call_dialogue_classmate_1a
    $ remove_hook(label="monica_bardie_eric_meeting_block")
    $ remove_objective("go_to_bardie")
    $ map_enabled = True
    $ miniMapEnabledOnly = []
    $ autorun_to_object("dialogue_classmate_15a", scene="floor2")
    if _return == True:
        $ autorun_to_object("dialogue_classmate_1b1", scene="floor2")
        $ remove_hook(label="monica_bardie_eric_meeting")
        $ ep28_monica_eric_meeting_completed = True
        $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["bardie_eric_quest_college", "evening_time_temp"]) # Разблокируем комнату Барди на след.день
#        if bettyCollegeTeacherRefused == True: # Если был отказ у Бетти, то продолжаем линию квестов с Моникой без нее
        $ questHelp("house_26", True)
        $ questHelp("house_27")
    else:
        $ questHelp("house_26", False)

    call ep28_monica_bardie_eric_college_init() from _call_ep28_monica_bardie_eric_college_init
    call refresh_scene_fade() from _call_refresh_scene_fade_185
    return False

label ep28_monica_bardie_eric_college_init: # инициализация квеста колледжа с Эриком и Моникой
    $ add_hook("change_time_day", "ep28_monica_bardie_eric_college0", scene="global", label="bardie_eric_quest_college")
    $ ep28_monica_bardie_eric_college_inited = True
    return

label ep28_monica_bardie_eric_college0:
    $ remove_hook()
    $ add_hook("enter_scene", "ep28_monica_bardie_eric_college1", scene="basement_bedroom2", label="bardie_eric_quest_college")
    return
label ep28_monica_bardie_eric_college1:
    if day_time != "evening":
        return
    if check_hook("ep24_quests_steve2", scene="global_week_day") == True or check_hook("ep24_quests_steve13", scene="global_week_day") == True:
        return
    $ remove_hook()
    $ autorun_to_object("dialogue_classmate_1d", scene="basement_bedroom2")
    $ add_hook("enter_scene", "dialogue_classmate_1b", scene="floor2", label="bardie_eric_quest_college", once=True)
    $ add_hook("enter_scene", "dialogue_classmate_1b", scene="floor1", label="bardie_eric_quest_college", once=True)
    $ add_hook("enter_scene", "dialogue_classmate_1b", scene="basement_pool", label="bardie_eric_quest_college", once=True)
    $ add_hook("enter_scene", "dialogue_classmate_1b", scene="floor1_stairs", label="bardie_eric_quest_college", once=True)
    $ add_objective("go_to_bardie", t_("Идти к Барди в комнату"), c_orange, 45)
    $ move_object("Betty", "bedroom1")
    call refresh_scene_fade() from _call_refresh_scene_fade_186
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_college2", scene="floor2", label="bardie_eric_quest_college")
    return

label ep28_monica_bardie_eric_college2:
    $ remove_hook(label="bardie_eric_quest_college")
    call dialogue_classmate_2() from _call_dialogue_classmate_2 # Барди говорит Монике притворяться мамой Эрика
    $ questHelp("house_27", True)
    $ questHelp("shop_7")
    $ questHelpDesc("house_desc14")

    $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["bardie_eric_quest_college", "evening_time_temp"]) # Разблокируем комнату Барди на след.день
    $ autorun_to_object("dialogue_classmate_2_1", scene="floor2") # Моника комментирует
    $ remove_objective("go_to_bardie")
    $ add_objective("find_dress_for_college", t_("Найти наряд, чтобы притвориться мамой Эрика"), c_green, 45)
    $ add_hook("enter_scene", "dialogue_classmate_3", scene="street_cloth_shop")
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep28_monica_bardie_eric_college3_shop", scene="street_cloth_shop", label="bardie_eric_quest_college_shop")
    $ map_objects ["Teleport_College"] = {"text" : t_("КОЛЛЕДЖ"), "xpos" : 174, "ypos" : 579, "base" : "map_marker", "state" : "visible"}
    call street_college_init() from _call_street_college_init
    $ move_object("Betty", "bedroom1")
    $ add_hook("enter_scene", "ep28_monica_bardie_eric_college2_enter_regular", scene="street_college", label="bardie_eric_quest_college_regular")
    $ add_hook("before_open", "ep28_monica_bardie_eric_college2_before_open_regular" , scene="street_college", label="bardie_eric_quest_college_regular2")
    call refresh_scene_fade() from _call_refresh_scene_fade_187
    $ questLog(55, True)
    return False

label ep28_monica_bardie_eric_college2_block_schooloutfit_map: # Проверка на ограничение перемещения по карте в униформе для школы. Только дом и колледж
    if cloth_type == "SchoolOutfit" and obj_name != "Teleport_House" and obj_name != "Teleport_College":
        call dialogue_classmate_3_1_1c() from _call_dialogue_classmate_3_1_1c
        return False
    return

label ep28_monica_bardie_eric_college2_enter_regular: # Регулярный комментарий при входе в локацию колледжа
    if cloth == "CasualDress1":
        call dialogue_classmate_3_2b() from _call_dialogue_classmate_3_2b
        return
    if cloth_type == "Whore":
        call dialogue_classmate_3_2bb() from _call_dialogue_classmate_3_2bb
        return
    return

label ep28_monica_bardie_eric_college2_before_open_regular: # Регулярная проверка при входе в локацию колледжа
    if cloth_type != "SchoolOutfit":
        $ streetCollegeMonicaSuffix = 2

    if day_time == "evening" and streetCollegeMonicaSuffix == 1:
        $ streetCollegeMonicaSuffix = 2
    return
label ep28_monica_bardie_eric_college3_shop: # Моника заходит в магазин одежды за нарядом
    if cloth != "Whore":
        call dialogue_classmate_2_1a() from _call_dialogue_classmate_2_1a
        return False
    call dialogue_classmate_3_1() from _call_dialogue_classmate_3_1
    if _return == 0: # Моника отказалась заходить в магазин
        return False
    if _return == -1:
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_7
        return False
    if _return == 1 or _return == 4:
        # Моника получила костюм мамы, можно идти в колледж
        $ remove_objective("find_dress_for_college")
        $ add_objective("eric_college", t_("Уладить проблему Эрика в колледже"), c_blue, 45)
        $ remove_hook(label="bardie_eric_quest_college_shop")
        $ monicaHasSchoolOutfit1Day = day
        $ monicaHasSchoolOutfit1 = True
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep28_monica_bardie_eric_college3_shop2", scene="street_cloth_shop", label="evening_time_temp")
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep28_monica_bardie_eric_college3_shop2_check_school_outfit", scene="street_cloth_shop", label="cloth_shop_check_school_outfit", priority = 110)
        $ add_hook("Teleport_Shawarma", "dialogue_classmate_3_1_1a", scene="street_cloth_shop", label="school_outfit_slums_forbidden")
        $ add_hook("College", "ep28_monica_bardie_eric_college4_visit1", scene="street_college", label="bardie_eric_quest_day1")
        $ add_hook("Monica", "ep28_monica_bardie_eric_college4", scene="street_college", label="street_college_monica")
        $ add_hook("enter_scene", "dialogue_classmate_4", scene="street_college", label="bardie_eric_quest_day1")
        $ add_hook("map_teleport", "ep28_monica_bardie_eric_college2_block_schooloutfit_map", scene="global", priority = 850)

        $ add_hook("Teacher", "ep28_monica_bardie_eric_college4_visit1_teacher", scene="college_class", label="bardie_eric_quest_day1")
        $ bardieDayEmpty = True # днем Барди нет

        # Инициализируем перемещение в schooloutfit по дому
        call street_house_outside_init2() from _call_street_house_outside_init2
        call wardrobeBasementPutUpSchoolOutfit1() from _call_wardrobeBasementPutUpSchoolOutfit1
        $ remove_hook(label="street_house_check_cloth_outside")
        $ add_hook("before_open", "ep25_quests5", scene = "street_house_main_yard", label="street_house_check_cloth_outside", priority = 200) # Проверка на вход в дом (Моника оказывается снаружи)
        $ add_hook("Teleport_House_Gate", "ep25_quests6", scene="street_house_outside", label="street_house_check_cloth_outside", priority = 200) # Проверка при входе в ворота дома
        $ add_hook("Teleport_Floor1_Stairs", "ep25_quests7", scene="basement_pool", label="street_house_check_cloth_outside", priority = 200) # Проверка при выходе в дом из бассейна
        $ remove_hook(label="house_dark_passage")
        $ add_hook("Teleport_Basement_Side", "ep25_quests8", scene="basement_hole", label="house_dark_passage") # Активируем черный ход


        $ autorun_to_object("dialogue_classmate_3_2", scene="street_cloth_shop")

        if _return == 4:
            $ add_corruption(monicaVivianSchoolOutfitLickBuy, "monicaVivianSchoolOutfitLickBuy")
    if _return == 3:
        $ autorun_to_object("dialogue_classmate_3_1_1b", scene="street_cloth_shop")
    music stop
    img black_screen
    with diss
    pause 2.0
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_27
    return False

label ep28_monica_bardie_eric_college3_shop2:
    mt "Магазин закрыт..."
    "Интересно почему..."
    return False

label ep28_monica_bardie_eric_college3_shop2_check_school_outfit:
    if monicaHasSchoolOutfit1Day == day:
        return
    if cloth_type != "Whore":
        call dialogue_classmate_2_1a() from _call_dialogue_classmate_2_1a_1
        return False
    return
#label ep28_monica_bardie_eric_college3:
#    if bettyCollegeTeacherStage > 0:
#        call ep28_betty_college_monica_lesbie_init()
#    return
label ep28_monica_bardie_eric_college4: # Клика на Монику на улице у колледжа
    if act=="l":
        if cloth == "CasualDress1":
            call dialogue_classmate_3_2b() from _call_dialogue_classmate_3_2b_1
            return False
        if cloth_type == "Whore":
            call dialogue_classmate_3_2bb() from _call_dialogue_classmate_3_2bb_1
            return False
        if cloth_type == "SchoolOutfit":
            call dialogue_classmate_3_3() from _call_dialogue_classmate_3_3
            return False

    return
label ep28_monica_bardie_eric_college4_visit1: # Моника приходит в колледж первый раз
    if act=="l":
        return
    if day_time == "evening":
        return
    if cloth_type == "CasualDress":
        call dialogue_classmate_3_2b() from _call_dialogue_classmate_3_2b_6
        return False
    if cloth_type == "Whore":
        call dialogue_classmate_3_2bb() from _call_dialogue_classmate_3_2bb_9
        return False
    if cloth_type != "SchoolOutfit":
        call dialogue_classmate_3_2bb() from _call_dialogue_classmate_3_2bb_10
        return False
    call change_scene("college_class","Fade_long", "highheels_run2") from _call_change_scene_409
    return False

label ep28_monica_bardie_eric_college4_visit1_teacher:
    if act=="l":
        return
    call dialogue_classmate_5() from _call_dialogue_classmate_5
    if _return == False:
        $ add_hook("enter_scene", "dialogue_classmate_5_1a", scene="street_college", once=True)
        $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_college4_visit1_bardie_refuse", scene="floor2", label="bardie_eric_quest_day1b")
    else:
        $ questHelpDesc("college_desc2", "college_desc3")
        $ add_hook("enter_scene", "dialogue_classmate_5_1", scene="street_college", once=True)
        $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_college4_visit1_bardie_completed", scene="floor2", label="bardie_eric_quest_day1b")
        $ add_objective("check_teacher", t_("Сходить к Мистеру Эдвардсу, чтобы узнать решил-ли он проблему Эрика"), c_white, 55)
        $ monicaEricQuest1Stage = 1
        $ add_corruption(monicaTeacherAddCorruption1, "monicaTeacherAddCorruption1")

    $ add_objective("go_to_bardie", t_("Поговорить с Барди (он бывает в своей комнате вечером)"), c_orange, 85)
    $ move_object("Bardie", "empty")
    $ remove_hook(label="bardie_eric_quest_day1")
    $ add_hook("College", "ep28_monica_bardie_eric_college4_visit1_college_block", scene="street_college", label=["evening_time_temp", "bardie_eric_quest_day1block"]) # Блокируем колледж на сегодня
    $ streetCollegeMonicaSuffix = 2
    call change_scene("street_college","Fade_long", "highheels_run2") from _call_change_scene_410
    return False

label ep28_monica_bardie_eric_college4_visit1_college_block:
    if act=="l":
        return
    call dialogue_classmate_3_3a() from _call_dialogue_classmate_3_3a
    return False

label ep28_monica_bardie_eric_college4_visit1_bardie_refuse: #Моника отказалась от условий учителя (день1)
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_5_1b() from _call_dialogue_classmate_5_1b
    $ streetCollegeMonicaSuffix = 1
    $ remove_hook(label="bardie_eric_quest_day1block")
    $ add_hook("College", "ep28_monica_bardie_eric_college4_visit1", scene="street_college", label="bardie_eric_quest_day1") # снова активируем колледж день1
    $ add_hook("Teacher", "ep28_monica_bardie_eric_college4_visit1_teacher", scene="college_class", label="bardie_eric_quest_day1") # снова активируем учителя день1
    $ remove_objective("go_to_bardie")
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_411
    return False

label ep28_monica_bardie_eric_college4_visit1_bardie_completed: # Моника успешно сходила к учителю
    if day_time != "evening":
        return
#    help "Продолжение квеста ожидайте в следующем апдейте."
#    $ streetCollegeMonicaSuffix = 1
#    return
    $ remove_hook()
    call dialogue_classmate_6() from _call_dialogue_classmate_6
    $ questHelp("college_5", True)
    $ questHelp("college_6")
#    $ questHelp("house_28", skipIfExists=True)
    $ streetCollegeMonicaSuffix = 1
    $ ep28_monica_bardie_eric_college4_visit1_data = day
    $ remove_hook(label="bardie_eric_quest_day1block")
    $ add_hook("enter_scene", "dialogue_classmate_7", scene="street_college", once=True)
    $ add_hook("College", "ep28_monica_bardie_eric_college4_visit2", scene="street_college", label="bardie_eric_quest_day1") # снова активируем колледж день1
    $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["evening_time_temp", "bardie_eric_quest_day1block"])
    $ remove_objective("go_to_bardie")
    $ autorun_to_object("dialogue_classmate_6a", scene="floor2")
    call refresh_scene_fade() from _call_refresh_scene_fade_188
    return False

label ep28_monica_bardie_eric_college4_visit2:
    if act=="l":
        return
    if day_time == "evening":
        return
    call ep29_quests_monica_college_visit2() from _call_ep29_quests_monica_college_visit2
#    help "Продолжение квеста ожидайте в следующем обновлении игры!"
    return False

label ep28_monica_college_bardie_erick_quest_check:
    return

label ep28_monica_college_bardie_betty_lesbian_scene: # Лесби сцена Бетти и Моники (после 1-го успешного дня в колледже на следующий вечер)
    if day_time != "evening" or ep28_monica_bardie_eric_college4_visit1_data == day:
        return
    $ remove_hook()
    call dialogue_4_classmate_lesbian_1() from _call_dialogue_4_classmate_lesbian_1

#    $ questHelp("house_29")

    $ questHelp("house_28", True)
    $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["evening_time_temp", "bardie_eric_quest_day1block"])
    $ autorun_to_object("dialogue_4_classmate_lesbian_1a", scene="floor2")
    $ monicaBettyLesbian = True
    call ep210_quests_bardie_init() from _rcall_ep210_quests_bardie_init
    return False
