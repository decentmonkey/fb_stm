default ep29_revenge_quest1_inited = False
default ep29_revenge_quest_started = False
default ep29_revenge_quest_aborted = False
default ep29_revenge_quest_last_try_day = 0 # Прошлый день, когда была попытка начать квест
default ep29_revenge_quest_blocked = False # Квест заблокирован

default ep29_revenge_quest_table_opened = False

label ep29_revenge_quest1_init:
    if ep29_revenge_quest1_inited == True:
        return
    $ ep29_revenge_quest1_inited = True
    # вешаем проверку на revenge quest при входе в спальню
    $ add_hook("before_open", "ep29_revenge_quest1_check", scene="basement_bedroom2", label="ep29_revenge_quest1_check", quest="revenge_quest")
    if marcus_visit1_completed == True:
        call basement_bedroom2_init2() from _call_basement_bedroom2_init2 # Оставляем в basement_bedroom2 анальную пробку
        return
    return
label ep29_revenge_quest1_init_repeat: # костыль
    $ add_hook("before_open", "ep29_revenge_quest1_check", scene="basement_bedroom2", label="ep29_revenge_quest1_check", quest="revenge_quest")
    return

label ep29_revenge_quest1_check:
    if cloth != "Governess" or day_time != "day":
        return
    $ print "CHECK REVENGE QUEST"
    if marcus_visit1_completed != True or ep29_victoria_melanie_licking != True or monica_teacher_sex != True or day-monica_teacher_sex_day < 2 or day - ep29_revenge_quest_last_try_day < ep29_revenge_quest_retry_days or ep29_revenge_quest_blocked == True or ep29_revenge_quest_started == True:
        return
    call ep215_quests_revenge_fix() from _rcall_ep215_quests_revenge_fix
    # Начинаем revenge quest
    call ep29_dialogues5_gun_monica_1() from _call_ep29_dialogues5_gun_monica_1
    if _return == 0: # одеты трусики
        $ ep29_revenge_quest_last_try_day = day
        $ add_hook("enter_scene", "dialogue_classmate_15a", scene="basement_pool", once=True)
        call change_scene("basement_pool", "Fade_long", False) from _call_change_scene_470
        return
    if _return == 1: # Моника убежала
        $ questHelp("revenge_1", False)
        $ ep29_revenge_quest_blocked = True # Блокируем квест
        $ questHelp("revenge_1", False)
        $ add_hook("enter_scene", "dialogue_classmate_15a", scene="basement_pool", once=True)
        call change_scene("basement_pool", "Fade_long", False) from _call_change_scene_471
        return
    $ questHelp("revenge_1", True)
    $ questHelp("revenge_1a")
    $ ep29_revenge_quest_started = True
    $ add_hook("ButtPlug", "ep29_revenge_quest1_buttplug", scene="basement_bedroom2", label="revenge_quest_buttplug", quest="revenge_quest")
    return

label ep29_revenge_quest1_buttplug:
    if act=="l":
        return
    $ remove_hook()
    return
    $ questHelp("revenge_1a", True)
    call ep29_dialogues5_gun_monica_2() from _call_ep29_dialogues5_gun_monica_2
    $ questHelp("revenge_2")
    $ add_objective("find_key", t_("Найти ключ от прикроватной тумбочки"), c_green, 120)
    # Инициализируем среду поиска ключа и открытого стола
    call locations_init_laundry_wash_machine() from _call_locations_init_laundry_wash_machine
    call locations_init_basement_bedroom_table_opened() from _call_locations_init_basement_bedroom_table_opened
    call basement_laundry_init2() from _call_basement_laundry_init2
    $ add_hook("Panties_Box", "ep29_revenge_quest1_laundry_boxes", scene="basement_laundry", label = "revenge_quest_boxes", quest="revenge_quest")
    $ add_hook_multi("ep29_revenge_quest1_laundry_boxes", scene="basement_laundry", label = "revenge_quest_boxes", quest="revenge_quest", filter={"group":"laundry_boxes"})
    $ add_hook("IronDesk", "ep29_revenge_quest1_laundry_irondesk", scene="basement_laundry", label = "revenge_quest_boxes", quest="revenge_quest")
    $ add_hook("WashMachine", "ep29_revenge_quest1_laundry_washmachine", scene="basement_laundry", label = "revenge_quest_boxes", quest="revenge_quest")
    $ add_hook("RevengeKeys", "ep29_revenge_quest1_laundry_revenge_keys", scene="basement_laundry_washmachine", label="revenge_quest_keys", quest="revenge_quest")
    $ add_hook("Gun", "ep29_revenge_quest1_table_gun", scene="basement_bedroom_table_opened", label="ep29_revenge_quest1_table_gun", quest="revenge_quest")
    $ add_hook("Teleport_Basement_Bedroom2", "ep29_revenge_quest1_move_buttplug", scene="basement_bedroom_table_opened", label="ep29_revenge_quest1_move_buttplug", quest="revenge_quest")
    $ define_inventory_object("revenge_keys", {"description" : t_("Ключи"), "label_suffix" : "_use_revenge_keys", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/revenge_keys" + res.suffix + ".png"})

    # Комментарии
    $ autorun_to_object("ep29_dialogues5_gun_monica_3", scene="basement_bedroom2")
    $ add_hook("BasementBed", "ep29_dialogues5_gun_monica_4", scene="basement_bedroom2", label="ep29_revenge_quest1_comment", quest="revenge_quest")
    $ add_hook("basement_monica_before_nap", "ep29_revenge_quest1_exit_nap", scene="global", label="ep29_revenge_quest1_nap", quest="revenge_quest")
    $ add_hook("BasementWardrobe", "ep29_dialogues5_gun_monica_5", scene="basement_bedroom1", label="ep29_revenge_quest1_wardrobe", quest="revenge_quest")
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_6", scene="basement_pool", label="ep29_revenge_quest1_comment", quest="revenge_quest", once=True)
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_7", scene="basement_hole", label="ep29_revenge_quest1_comment2", quest="revenge_quest", once=True)
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_7", scene="floor1", label="ep29_revenge_quest1_comment2", quest="revenge_quest", once=True)
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_7", scene="floor2", label="ep29_revenge_quest1_comment2", quest="revenge_quest", once=True)
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_7", scene="bedroom2", label="ep29_revenge_quest1_comment2", quest="revenge_quest", once=True)
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_7", scene="bathroom_bath", label="ep29_revenge_quest1_comment2", quest="revenge_quest", once=True)
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_7", scene="street_house_main_yard", label="ep29_revenge_quest1_comment2", quest="revenge_quest", once=True)
    $ add_hook("Teleport_House_Outside_Outside", "ep29_revenge_quest1_exit_outside", scene="street_house_outside", label="ep29_revenge_quest1_exit_outside", quest="revenge_quest")
    $ add_hook("map_teleport", "ep29_revenge_quest1_exit_map", scene="global", label="ep29_revenge_quest1_exit_map", quest="revenge_quest", priority = 10000)

    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_8", scene="basement_laundry", label="ep29_revenge_quest1_comment", quest="revenge_quest", once=True)

    $ cloth = "Governess"
    $ cloth_type = "Governess"

    call refresh_scene_fade() from _call_refresh_scene_fade_229
    return False

label ep29_revenge_quest1_laundry_boxes:
    if obj_name == "Panties_Box":
        call ep29_dialogues5_gun_monica_9() from _call_ep29_dialogues5_gun_monica_9
        $ remove_hook()
        return
    $ set_active("Box5", False, scene="basement_laundry")
    $ set_active("Box6", False, scene="basement_laundry")
    if obj_name == "Box2" or obj_name == "Box4" or obj_name == "Box6":
        call ep29_dialogues5_gun_monica_9b() from _call_ep29_dialogues5_gun_monica_9b
    if obj_name == "Box3" or obj_name == "Box5":
        call ep29_dialogues5_gun_monica_9b2() from _call_ep29_dialogues5_gun_monica_9b2

    $ set_active(obj_name, False, scene="basement_laundry")
    if get_active_objects(group="laundry_boxes", scene="basement_laundry") == False:
        $ set_active("IronDesk", True)
    return

label ep29_revenge_quest1_laundry_irondesk:
    call ep29_dialogues5_gun_monica_9b3() from _call_ep29_dialogues5_gun_monica_9b3
    $ set_active("IronDesk", False, scene="basement_laundry")
    $ set_active("WashMachine", True, scene="basement_laundry")
    call refresh_scene_fade() from _call_refresh_scene_fade_230
    return False

label ep29_revenge_quest1_laundry_washmachine:
    if act=="l":
        call ep29_dialogues5_gun_monica_9b4() from _call_ep29_dialogues5_gun_monica_9b4
        return False
    $ add_hook("enter_scene", "ep29_dialogues5_gun_monica_9b5", scene="basement_laundry_washmachine", once=True, quest="revenge_quest")
    call change_scene("basement_laundry_washmachine") from _call_change_scene_472
    return False

label ep29_revenge_quest1_laundry_revenge_keys:
    if act=="l":
        return
    call ep29_dialogues5_gun_monica_9b6() from _call_ep29_dialogues5_gun_monica_9b6
    $ questHelp("revenge_2", True)
    $ questHelp("revenge_3")
    $ set_active("RevengeKeys", False, scene="basement_laundry_washmachine")
    $ add_inventory("revenge_keys", 1, True)
    $ set_active("WashMachine", False, scene="basement_laundry")
    $ remove_hook(label="revenge_quest_boxes")
    sound fx_coins
    $ add_hook("Box", "ep29_revenge_quest1_table_box_opening", scene="basement_bedroom_table", label="revenge_quest_keys", quest="revenge_quest")
    $ remove_objective("find_key")
    $ remove_hook("enter_scene", "ep29_dialogues5_gun_monica_6", scene="basement_pool")
    $ remove_hook(label="ep29_revenge_quest1_wardrobe")
    $ remove_hook(label="ep29_revenge_quest1_comment")
    $ remove_hook(label="ep29_revenge_quest1_nap")
    $ remove_hook(label="ep29_revenge_quest1_exit_map")
    $ remove_hook(label="ep29_revenge_quest1_exit_outside")

    $ add_objective("open_table", t_("Открыть запертый ящик"), c_red, 120)
    call refresh_scene_fade() from _call_refresh_scene_fade_231
    return

label ep29_revenge_quest1_table_box_opening:
    if act=="l":
        return
    if check_inventory("revenge_keys",1) != True:
        return
    if cloth != "Governess":
        call change_scene("basement_bedroom1", "Fade_long", False) from _rcall_change_scene_38
        call wardrobePutGovernessWithoutPanties() from _rcall_wardrobePutGovernessWithoutPanties
        return False
    music stop
    img black_screen
    with diss
    sound fx_coins
    pause 1.5
    sound desk_open
    if ep29_revenge_quest_table_opened == False:
        call ep29_dialogues5_gun_monica_10() from _call_ep29_dialogues5_gun_monica_10
#        $ remove_hook()
        $ remove_objective("open_table")
        $ ep29_revenge_quest_table_opened = True
    call change_scene("basement_bedroom_table_opened", "Fade", "desk_open") from _call_change_scene_473
    return False

label ep29_revenge_quest1_table_gun:
    if act=="l":
        return
    if cloth != "Governess":
        call change_scene("basement_bedroom1", "Fade_long", False) from _rcall_change_scene_39
        call wardrobePutGovernessWithoutPanties() from _rcall_wardrobePutGovernessWithoutPanties_1
        return
    call ep29_dialogues5_gun_monica_10b() from _call_ep29_dialogues5_gun_monica_10b
    if _return == False:
        $ questHelp("revenge_3", False)
        call refresh_scene_fade() from _call_refresh_scene_fade_232
        return False
    python:
        for categoryName in questHelpData:
            if categoryName != t_("ПУТЬ МЕСТИ"):
                questsFailByCategory(categoryName)
    $ basementBedSkipUntilFridayEnabled = False
    $ questHelp("revenge_3", True)
    $ questHelp("revenge_3a")
    call ep210_revenge_quest2() from _rcall_ep210_revenge_quest2
    return False

label ep29_revenge_quest1_exit_nap: # Выход из квеста, через кровать
    call ep29_dialogues5_gun_monica_4a() from _call_ep29_dialogues5_gun_monica_4a
    if _return == True:
        return False
    $ questsFailByCategory(t_("ПУТЬ МЕСТИ"))
    $ remove_hook(quest="revenge_quest")
    $ remove_objective("find_key")
    $ remove_objective("open_table")
    if check_inventory("revenge_keys",1) == True:
        $ remove_inventory("revenge_keys", 1, False)

    $ ep29_revenge_quest_aborted = True
    return
#

label ep29_revenge_quest1_exit_outside:
    if get_active_objects("ButtPlug", scene="basement_bedroom_table_opened") != False:
        # костыль для фикса отмены квеста мести
        $ remove_hook(label="ep29_revenge_quest1_wardrobe")
        $ remove_hook(label="ep29_revenge_quest1_comment")
        $ remove_hook(label="ep29_revenge_quest1_nap")
        $ remove_hook(label="ep29_revenge_quest1_exit_map")
        $ remove_hook(label="ep29_revenge_quest1_exit_outside")
        return
    call ep29_dialogues5_gun_monica_4a() from _call_ep29_dialogues5_gun_monica_4a_1
    if _return == True:
        return False
    $ questsFailByCategory(t_("ПУТЬ МЕСТИ"))
    $ remove_hook(quest="revenge_quest")
    $ remove_objective("find_key")
    $ remove_objective("open_table")
    if check_inventory("revenge_keys",1) == True:
        $ remove_inventory("revenge_keys", 1, False)
    $ ep29_revenge_quest_aborted = True
    return

label ep29_revenge_quest1_exit_map:
    if obj_name != "Teleport_House":
        if get_active_objects("ButtPlug", scene="basement_bedroom_table_opened") != False:
            # костыль для фикса отмены квеста мести
            $ remove_hook(label="ep29_revenge_quest1_wardrobe")
            $ remove_hook(label="ep29_revenge_quest1_comment")
            $ remove_hook(label="ep29_revenge_quest1_nap")
            $ remove_hook(label="ep29_revenge_quest1_exit_map")
            $ remove_hook(label="ep29_revenge_quest1_exit_outside")
            return

        call ep29_dialogues5_gun_monica_4a() from _call_ep29_dialogues5_gun_monica_4a_2
        if _return == True:
            return False
        $ questsFailByCategory(t_("ПУТЬ МЕСТИ"))
        $ remove_hook(quest="revenge_quest")
        $ remove_objective("find_key")
        $ remove_objective("open_table")
        if check_inventory("revenge_keys",1) == True:
            $ remove_inventory("revenge_keys", 1, False)
        $ ep29_revenge_quest_aborted = True
    return

label Box_use_revenge_keys:
    if scene_name=="basement_bedroom_table":
        if check_inventory("revenge_keys",1) != True:
            return
        if cloth != "Governess":
            call change_scene("basement_bedroom1", "Fade_long", False) from _rcall_change_scene_40
            call wardrobePutGovernessWithoutPanties() from _rcall_wardrobePutGovernessWithoutPanties_2
            return
        if ep210_revenge_quest2_box_blocked_fred == True:
            return
        music stop
        img black_screen
        with diss
        sound fx_coins
        pause 1.5
        sound desk_open
        if ep29_revenge_quest_table_opened == False:

            call ep29_dialogues5_gun_monica_10() from _call_ep29_dialogues5_gun_monica_10_1
            $ remove_objective("open_table")
            $ ep29_revenge_quest_table_opened = True
        call change_scene("basement_bedroom_table_opened", "Fade", "desk_open") from _call_change_scene_474
    return

label ep29_revenge_quest1_move_buttplug:
    if get_active_objects("ButtPlug", scene="basement_bedroom2") != False:
        $ move_object("ButtPlug", "basement_bedroom_table_opened")
    return
