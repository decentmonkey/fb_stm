default ep24_quests_initialized = False
default ep24_quests_fix_initialized = False
default ep24_quests_fix2_initialized = False

label ep24_quests_init:
    # Инициализация v0.4
    $ set_var("Monica", zorder=15, scene="hostel_edge_1_a")
    call floor2_init_addition1() from _call_floor2_init_addition1 #Барди floor2
    call bedroom1_init_addition1() from _call_bedroom1_init_addition1 # Барди bedroom1
    if char_info["Bardie"]["level"] == 3:
        $ char_info["Bardie"]["enabled"] = False
        $ char_info["Bardie"]["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
        $ char_info["Bardie"]["show_caption_diabled"] = True
        help "Открыто продолжение истории с Барди"
    if char_info["Betty"]["level"] == 4:
        $ char_info["Betty"]["enabled"] = False
        $ char_info["Betty"]["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
        $ char_info["Betty"]["show_caption_diabled"] = True
        help "Открыто продолжение истории с Бетти"

    $ ep24_quests_initialized = True

    return

label ep24_quests_fix:
    if ep24_quests_fix2_initialized == False and char_info.has_key("Bardie") and char_info["Bardie"]["level"] == 3 and char_info["Bardie"]["enabled"] == False:
        $ ep24_quests_fix2_initialized = True
        $ char_info["Bardie"]["enabled"] = True
    if ep24_quests_fix_initialized == True:
        return
    $ ep24_quests_fix_initialized = True
    if steveVisit1PlannedComplete == False and melanieDisappeared == True: # Если Стива еще не было и Мелани пропала
        if monicaCleaningInProgressEngineWorkingFlag == True:
            $ houseCleaningStoredScene2 = store_scene("House", recursive=True)
            $ restore_scene(houseCleaningStoredScene)
            call ep24_quests_steve1() from _call_ep24_quests_steve1
            $ houseCleaningStoredScene = store_scene("House", recursive=True)
            $ restore_scene(houseCleaningStoredScene2)
            $ houseCleaningStoredScene2 = False
        else:
            call ep24_quests_steve1() from _call_ep24_quests_steve1_1
        return
    if steveVisit1PlannedComplete == True and bettyMustNotWearPanties == True:
        # Второй приход Стива уже запланирован
        return
    if steveVisit1PlannedComplete == True:
        # Иначе вешаем хук на Ральфа для второго прихода Стива
        if monicaCleaningInProgressEngineWorkingFlag == True:
            $ houseCleaningStoredScene2 = store_scene("House", recursive=True)
            $ restore_scene(houseCleaningStoredScene)
            $ add_hook("Ralph", "ep24_quests_steve34", scene="living_room", label="steve_ralph_visit2")
            $ houseCleaningStoredScene = store_scene("House", recursive=True)
            $ restore_scene(houseCleaningStoredScene2)
            $ houseCleaningStoredScene2 = False

        else:
            $ add_hook("Ralph", "ep24_quests_steve34", scene="living_room", label="steve_ralph_visit2")


#    if fitness_gym_visited_amount >= 1 and steveVisit1PlannedComplete == False:
#        call ep24_quests_steve1() from _call_ep24_quests_steve1_1 #Планируем в субботу приход Стива

    return
