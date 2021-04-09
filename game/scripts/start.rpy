define debugMode = False

default gameStage = 0
default gameSubStage = 0
default afterJail = False
default rain = False
default rainIntencity = 0
default lightning = False
default sceneIsStreet = False
default hudDaySkipToEveningEnabled = True
default objectives_list = []
default currentMusic = False
default currentMusicPriority = 0
default currentMusic2 = False
default currentMusic3 = False
default storedMusic = []
default storedMusicPriority = []
default day_time = "day"
default day = 0
default week_day = 1
default owner = "Monica"
default showObjectsNotOwner = True
default episode = 1
default notifList = []
default lastNotifTime = 0

default menu_corruption = []
default menu_price = []
default menu_bitchiness = []
default menu_required = {}

default hud_preset_current = "default"
default hud_preset_default = "default"
default minimap_coords_preset = 0
default blur_effect = False

default after_load_ready_to_render = False
default nextFriday = -1

default act = ""

default episode2part = 1
default bardieCensored = False

default EP1 = False
default EP1_skipintro = False
default SteamVersion1 = False

label start:
    $ SteamVersion1 = True
    imgfl scene_Map_Evening
    menu:
        "Episode 1":
            jump EP1_start
        "Episode 2":
            pass
    #new game

label startfromep1:
    if _preferences.language == "spanish" or _preferences.language == "chinese" or _preferences.language == "turkish":
        $ _preferences.language = "english"
    $ EP1 = False
    python:
        teleportHomeFredBlowjobFlag = False
        mapSubstMonicaOfficeToPolice = False
        mapSubstMonicaOfficeToSteve = False
        teleportDickOfficeHeavyRainFlag = False
        teleportDickOfficeEveningFlag = False
        mapSubstClothingShopToStreetCorner = False
    $ translation_load_EP2()
    $ bardieCensored = True
    $ after_load_ready_to_render = True
    $ refresh_list_files_forced()
    $ episode = 2
#    $ debugMode = True

    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []
    $ objectives_list = []

    if EP1_skipintro == False:
        $ cloth_type = "Nude"
        $ cloth = "Nude"
        $ bitchmeterValue = 280
        call intro_questions() from _call_intro_questions
        $ ralphAskedAboutPayment = False
    if ralphAskedAboutPayment == False:
        $ add_objective("ask_ralph", t_("Узнать у Ральфа по поводу оплаты"), c_orange, 13)
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)
    call start_game() from _call_start_game
    return

label start_saved_game:
    $ bardieCensored = True
    if scene_name != "basement_bedroom1" and scene_name != "basement_bedroom2":
        img black_screen
        help "Пожалуйста, используйте сохранение из финальной локации в подвале дома."
        scene black_screen
        with Dissolve(1)
        $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
        return

    $ refresh_list_files_forced()
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []
    call intro_questions_save() from _call_intro_questions_save
    $ objectives_list = []
    if ralphAskedAboutPayment == False:
        $ add_objective("ask_ralph", t_("Узнать у Ральфа по поводу оплаты"), c_orange, 13)
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)
    $ teleportHomeFredBlowjobFlag = False
    call start_game() from _call_start_game_1
    return

label start_game:

    $ gameStage = 0
    $ gameSubStage = 0
    $ afterJail = True
    $ rain = False
    $ sceneIsStreet = False

    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1

    $ day = 5
    $ monicaEatedLastDay = day
    $ week_day = (day)%7
    if week_day == 0:
        $ week_day = 7

    $ day_time = "evening"
    $ day_suffix = ""
    $ money = 0.0

    $ hud_preset_current = "default"

    call questLog_init() from _call_questLog_init
    $ questLog(19, True)
    $ questLog(18, True)
    $ questLog(15, True)
    $ questLog(6, True)
    $ questLog(3, True)

    call game_init() from _call_game_init
#    python:
#        for i in renpy.exports.get_image_load_log():
#            print i

    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : t_("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : t_("УГОЛ УЛИЦЫ"), "xpos" : 124, "ypos" : 476, "base" : "map_marker", "state" : "visible"},
            "Teleport_Dick_Office" : {"text" : t_("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "visible"},
            "Teleport_Gas_Station" : {"text" : t_("ЗАПРАВКА"), "xpos" : 1125, "ypos" : 910, "base" : "map_marker", "state" : "visible"},
            "Teleport_Police" : {"text" : t_("ПОЛИЦИЯ"), "xpos" : 912, "ypos" : 809, "base" : "map_marker", "state" : "visible"},
            "Teleport_Rich_Hotel" : {"text" : t_("ОТЕЛЬ ЛЯ ГРАНД"), "xpos" : 1782, "ypos" : 593, "base" : "map_marker", "state" : "visible"},
            "Teleport_Fitness" : {"text" : t_("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "visible"},
            "Teleport_Steve_Office" : {"text" : t_("ОФИС СТИВА"), "xpos" : 1333, "ypos" : 724, "base" : "map_marker", "state" : "visible"},
            "Teleport_Bank" : {"text" : t_("БАНК"), "xpos" : 1212, "ypos" : 439, "base" : "map_marker", "state" : "visible"},
            "Teleport_Cloth_Shop" : {"text" : t_("МАГАЗИН ОДЕЖДЫ"), "xpos" : 340, "ypos" : 901, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : t_("УГОЛ УЛИЦЫ"), "xpos" : (88+15), "ypos" : 942, "base" : "map_marker", "state" : "visible"},
            "Teleport_Hostel2" : {"text" : t_("ГРЯЗНАЯ УЛИЦА"), "xpos" : 259, "ypos" : 1046, "base" : "map_marker", "state" : "invisible"},
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active"}
    }
#mousedown_3, hide_windows
#    $ print(config.keymap["game_menu"])
#    $ config.keymap["hide_windows"] = []
#    $ print(config.keymap)
#    pause

    $ bFredFollowingMonica = False

    $ scene_refresh_flag = True
    $ map_scene = "House"
    $ map_enabled = True
    $ map_disabled_forced = False
    $ scene_name = "none"
    $ api_scene_name = "none"
    call locations_init() from _call_locations_init
    call citizens_init() from _call_citizens_init
    call characters_init() from _call_characters_init
    call basement_shower_init() from _call_basement_shower_init
    call kebab_work_init() from _call_kebab_work_init

    $ add_hook("exit_scene", "hook_basement_bedroom2_change_view_to_suffix3", scene="basement_bedroom2")
    # Запрет Бетти ходить по дому
    $ add_hook("enter_scene", "afterJailHouse_dialogue10", scene="bathroom_bath", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue15", scene="kitchen", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue15b", scene="kitchen2", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue16a", scene="bedroom2", label="betty_forbidden")

    # Проверка одежды при хождении по дому и покидании его
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom1")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom2")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom_cupboard")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom_table")
    $ add_hook("map_teleport", "hook_basement_bedroom_check_exit_cloth_map", scene="global", priority=1000)
    $ add_hook("Gates", "hook_basement_bedroom_check_exit_cloth_gates", scene="street_house_gate")

    # Жизнь персонажей
    $ add_hook("change_time_day", "citizens_init_day", scene="global")
    $ add_hook("change_time_evening", "citizens_init_evening", scene="global")

    call Bardie_Life_init() from _call_Bardie_Life_init
    call Betty_Life_init() from _call_Betty_Life_init
    call Ralph_Life_init() from _call_Ralph_Life_init
    call Fred_Life_init() from _call_Fred_Life_init
    call Biff_Life_init() from _call_Biff_Life_init

    # Постель в подвале
    $ add_hook("BasementBed", "basement_bed_hook", scene="basement_bedroom2")
    $ add_hook("basement_monica_after_sleep", "basement_monica_after_sleep", scene="global")
    $ add_hook("basement_monica_after_nap", "basement_monica_after_nap", scene="global")
    $ add_hook("basement_monica_after_sleep_dialogue", "basement_monica_after_sleep_dialogue1", scene="global")
    $ add_hook("basement_monica_after_nap_dialogue", "basement_monica_after_nap_dialogue1", scene="global")
    # Уборка в доме
    $ add_hook("enter_scene", "house_cleaning", scene="floor1")
    $ add_hook("enter_scene", "house_cleaning", scene="floor2")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom_bardie")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom_second")
    $ add_hook("enter_scene", "house_cleaning", scene="living_room")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom1")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom2")
    $ add_hook("monica_cleaning_start", "Bardie_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Bardie_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Betty_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Betty_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Ralph_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Ralph_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Fred_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Fred_Life_Monica_Cleaning_End", scene="global")
    # Офис Моники
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4a", scene="monica_office_secretary")


    # Узнать про оплату у Ральфа
    $ add_hook("enter_scene", "Ralph_Life_Ask_About_Payment", scene="living_room")

    # Офис Дика вначале закрыт
    $ add_hook("Teleport_Inside", "monica_dick_office_dialogue1a", scene="dick_office_entrance")
    $ move_object("DickTheLawyer", "empty")

    # Офис Моники
    $ add_hook("Teleport_Monica_Office_Secretary", "monica_office_entrance_biff_dialogue1", scene="monica_office_entrance")
    $ move_object("Secretary", "monica_office_secretary")
    $ add_hook("Secretary", "monica_office_secretary_dialogue2", scene="monica_office_secretary") # Регулярный разговор попросить деньги
    $ add_hook("Secretary", "monica_office_secretary_dialogue1", scene="monica_office_secretary", label="secretary1")
    $ add_hook("Teleport_Monica_Office_Photostudio", "monica_office_secretary_dialogue1", scene="monica_office_secretary", label="secretary1")

    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4a", scene="monica_office_secretary", label="check_bill_at_place", priority=150)
    $ add_hook("Table", "monica_office_cabinet_biff_dialogue1", scene="monica_office_cabinet", label="biff1")
    $ add_hook("Biff", "monica_office_cabinet_biff_dialogue1", scene="monica_office_cabinet", label="biff1")

    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue1", scene="monica_office_secretary", label="secretary1")

    $ move_object("Melanie", "monica_office_cabinet")
    $ add_hook("Melanie", "monica_office_photostudio_melanie_dialogue1", scene="monica_office_secretary")
    $ move_object("AlexPhotograph", "monica_office_photostudio")
    $ add_hook("AlexPhotograph", "monica_office_photostudio_alex_dialogue1", scene="monica_office_photostudio") # Приветствие Алекса

    # Заправка
    $ add_hook("enter_scene", "monica_gas_station_thief_dialogue1", scene="gas_station_view1")

#    $ remove_hook(label="betty_forbidden", scene="House", recursive=True)
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_51
    $ changeDayTime("day")

    $ miniMapDisabled = {"House":[], "Street_Corner":["Hostel_Street", "Hostel_Street2", "Hostel_Street3", "Hostel_Edge_1_c"]}
    $ miniMapEnabledOnly = []

    # Закрываем вначале доп. локации в Street_Corner (бедный квартал)
    $ add_hook("Teleport_Street_Hostel", "kebab_work_block_teleports", scene="whores_place_shawarma", label="kebab_work_block_teleports")
    $ add_hook("Teleport_Hostel_Street3", "kebab_work_block_teleports", scene="street_corner", label="kebab_work_block_teleports")

    $ scene_transition = "Fade_long"

    $ add_hook("before_open", "food_basement_room_init", scene="basement_bedroom2", label="food_basement_room_init", priority = 200)
    $ add_hook("before_open", "food_basement_room_init2", scene="basement_bedroom_table", label="food_basement_room_init", priority = 200)
    $ define_inventory_object("food_package", {"description" : t_("Еда"), "label_suffix" : "_use_food", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/food_package" + res.suffix + ".png"})
    $ ep23_quests_initialized = True

    call floor2_init_addition1() from _call_floor2_init_addition1_1 #Барди floor2
    call bedroom1_init_addition1() from _call_bedroom1_init_addition1_1 # Барди bedroom1
    call monica_cheats_init() from _rcall_monica_cheats_init_1
    $ ep24_quests_initialized = True
    $ ep26_quests_initialized = True
    $ ep27_quests_initialized = True
    $ ep29_quests_initialized = True
    $ ep210_quests_load_init_flag = True
    $ ep211_quests_load_init_flag = True
    $ ep212_quests_load_init_flag = True
    $ ep213_quests_load_init_flag = True
    $ ep214_quests_load_init_flag = True
    $ ep215_quests_load_init_flag = True
    $ ep216_quests_load_init_flag = True

    # quest help
    call questHelp_init() from _rcall_questHelp_init_2
    python:
        questHelp("other1")
        questHelp("other2")
        questHelp("house_1")
        questHelp("work_slums_1")
        questHelp("office_1")
        if ralphAskedAboutPayment == False:
            questHelp("house_2")
        questHelpActivated = True
        questHelp("marcus_1")
        questHelpDesc("house_desc1")
        questHelpDesc("marcus_desc1")
        questHelpDesc("office_desc1")

#    $ changeDayTime("evening")
#    $ scene_data = process_scene_objects_list(scene_name) #парсим содержимое свойств объектов перед выводом
#    $ print scene_data

#    $ cloth = "CasualDress1"
#    $ cloth_type = "CasualDress"
#    $ day_time = "evening"
#    $ day_suffix = "_Evening"
#    call locations_init_monicahome()
#    call locations_init_juliahome()
#    call locations_init_public_event2()
#    call locations_init_rich_hotel_restaurant2()
#    call locations_init_rich_hotel_restaurant()
#    call rich_hotel_reception_init2()
#    call rich_hotel_reception_init3()
#    call change_scene("rich_hotel_reception") #debug !!!!!
#    jump show_scene
#    $ renpy.pause(100, hard=True)
    $ bardieCensored = True
    $ add_hook("change_time_day", "ep00_check_game_end", scene="global", priority = 1)

#    $ autorun_to_object("intro_scene", "intro_scene_start")
    music stop
#    $ _dismiss_pause = False
    scene black_screen
    with Dissolve(1)
    call textonblack_long("FASHION BUSINESS") from _call_textonblack_long
    scene black_screen
    with Dissolve(1)
    call textonblack_long("EPISODE 2: NEW LIFE") from _call_textonblack_long_1
    scene black_screen
    with Dissolve(1)
#    $ _dismiss_pause = True
    call sleep_scene1() from _call_sleep_scene1

    $ questHelpActivated = True
    $ episode = 2
    jump show_scene

label start_new_game:
    music casualMusic
#    $ map_enabled = True
#    $ add_objective("dress_homecloth", t_("Одеть домашнюю одежду"), c_blue, 0)

#    $ miniMapDisabled = ["Basement"]


#    $ add_inventory("phone", 1, True)
    return

label empty_label:
    return









#
