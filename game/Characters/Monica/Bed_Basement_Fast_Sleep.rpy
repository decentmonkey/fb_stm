default fastSleepInProcess = False
default fastSleepTick = 0

label bed_basement_fast_sleep:
    $ remove_hook(label="fast_sleep_process")
    if slumsApartmentsRentActive != True and monica_living_at_juliahome != True:
        jump bed_basement_fast_sleep_monica_house
    if scene_name == "street_house_main_yard" or scene_name == "street_house_gate" or scene_name == "street_house_fence":
        jump bed_basement_fast_sleep_monica_house
    menu:
        "Дом Моники.":
            jump bed_basement_fast_sleep_monica_house
        "Дом в трущобах." if slumsApartmentsRentActive == True:
            jump bed_basement_fast_sleep_house_slums
        "Квартира Юлии." if monica_living_at_juliahome == True:
            jump bed_basement_fast_sleep_juliahome

        "Уйти.":
            return
    return

label bed_basement_fast_sleep_monica_house:
    # Идем к Монике в спальню в подвале
    if map_objects.has_key("Teleport_House") and map_objects["Teleport_House"]["state"] != "visible" and map_objects["Teleport_House"]["state"] != "active":
        sound click_denied
        return
    $ fastSleepInProcess = True
    $ fastSleepTick = pause_enter
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    imgd black_screen
    call process_change_map_location("House") from _rcall_process_change_map_location_2
    $ add_hook("before_open", "bed_basement_fast_sleep_monica_house_step1", scene="street_house_outside", label="fast_sleep_process", priority = -1)
    call change_scene("street_house_outside") from _rcall_change_scene_123
    return

label bed_basement_fast_sleep_monica_house_step1:
    if fastSleepTick != pause_enter:
        $ remove_hook(label="fast_sleep_process")
        return
    # Проверяем доступ к постели
    if (miniMapDisabled.has_key("House") and "Basement" in miniMapDisabled["House"]) or (miniMapDisabled2.has_key("House") and "Basement" in miniMapDisabled2["House"]) or (len(miniMapEnabledOnly) >0 and "Basement" not in miniMapEnabledOnly):
        return
    # Доступ к постели есть
    $ add_hook("before_open", "bed_basement_fast_sleep_monica_house_step2", scene="basement_bedroom2", label="fast_sleep_process", priority=-1)
    call change_scene("basement_bedroom2", "Fade_long") from _rcall_change_scene_124
    return

label bed_basement_fast_sleep_monica_house_step2:
    if fastSleepTick != pause_enter:
        $ remove_hook(label="fast_sleep_process")
        return
    $ add_hook("enter_scene", "bed_basement_fast_sleep_monica_house_step3", scene="basement_bedroom2", label="fast_sleep_process", priority=-1)
    return

label bed_basement_fast_sleep_monica_house_step3:
    $ remove_hook(label="fast_sleep_process")
    if fastSleepTick != pause_enter:
        return
    call process_object_click_forced("BasementBed", "h") from _rcall_process_object_click_forced_2
    return

label bed_basement_fast_sleep_house_slums:
    # Идем к Монике в спальню в дом в трущобах
    if map_objects.has_key("Teleport_Slums_Apartments") and map_objects["Teleport_Slums_Apartments"]["state"] != "visible" and map_objects["Teleport_Slums_Apartments"]["state"] != "active":
        sound click_denied
        return
    $ fastSleepInProcess = True
    $ fastSleepTick = pause_enter
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    imgd black_screen
    call process_change_map_location("Slums_Apartments") from _rcall_process_change_map_location_3
    $ add_hook("before_open", "bed_basement_fast_sleep_house_slums_step1", scene="street_monicahome", label="fast_sleep_process", priority = -1)
    call change_scene("street_monicahome") from _rcall_change_scene_125
    return


label bed_basement_fast_sleep_house_slums_step1:
    if fastSleepTick != pause_enter:
        $ remove_hook(label="fast_sleep_process")
        return
    if (miniMapDisabled.has_key("Slums_Apartments") and "MonicaHome_LivingRoom" in miniMapDisabled["Slums_Apartments"]) or (miniMapDisabled2.has_key("Slums_Apartments") and "MonicaHome_LivingRoom" in miniMapDisabled2["Slums_Apartments"]) or (len(miniMapEnabledOnly) >0 and "MonicaHome_LivingRoom" not in miniMapEnabledOnly):
        return
    # Доступ к постели есть
    $ add_hook("before_open", "bed_basement_fast_sleep_house_slums_step2", scene="monicahome_livingroom", label="fast_sleep_process", priority=-1)
    call process_object_click_forced("HomeEnter", "w") from _rcall_process_object_click_forced_3
    return

label bed_basement_fast_sleep_house_slums_step2:
    if fastSleepTick != pause_enter:
        $ remove_hook(label="fast_sleep_process")
        return
    $ add_hook("enter_scene", "bed_basement_fast_sleep_house_slums_step3", scene="monicahome_livingroom", label="fast_sleep_process", priority=-1)
    return

label bed_basement_fast_sleep_house_slums_step3:
    $ remove_hook(label="fast_sleep_process")
    if fastSleepTick != pause_enter:
        return
    call process_object_click_forced("Bed1", "h") from _rcall_process_object_click_forced_4
    return



label bed_basement_fast_sleep_juliahome:
    if map_objects.has_key("Teleport_JuliaHome") and map_objects["Teleport_JuliaHome"]["state"] != "visible" and map_objects["Teleport_JuliaHome"]["state"] != "active":
        sound click_denied
        return
    # Идем к Юлии в спальню
    $ fastSleepInProcess = True
    $ fastSleepTick = pause_enter
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    imgd black_screen
    call process_change_map_location("JuliaHome") from _rcall_process_change_map_location_4
    $ add_hook("before_open", "bed_basement_fast_sleep_juliahome_step1", scene="street_juliahome", label="fast_sleep_process", priority = -1)
    call change_scene("street_juliahome") from _rcall_change_scene_126
    return

label bed_basement_fast_sleep_juliahome_step1:
    if fastSleepTick != pause_enter:
        $ remove_hook(label="fast_sleep_process")
        return
    if (miniMapDisabled.has_key("JuliaHome") and "JuliaHome_LivingRoom" in miniMapDisabled["JuliaHome"]) or (miniMapDisabled2.has_key("JuliaHome") and "JuliaHome_LivingRoom" in miniMapDisabled2["JuliaHome"]) or (len(miniMapEnabledOnly) >0 and "JuliaHome_LivingRoom" not in miniMapEnabledOnly):
        return
    # Доступ к постели есть
    $ add_hook("before_open", "bed_basement_fast_sleep_juliahome_step2", scene="juliahome_livingroom", label="fast_sleep_process", priority=-1)
    call process_object_click_forced("JuliaHome", "w") from _rcall_process_object_click_forced_5
    return

label bed_basement_fast_sleep_juliahome_step2:
    if fastSleepTick != pause_enter:
        $ remove_hook(label="fast_sleep_process")
        return
    $ add_hook("enter_scene", "bed_basement_fast_sleep_juliahome_step3", scene="juliahome_livingroom", label="fast_sleep_process", priority=-1)
    return

label bed_basement_fast_sleep_juliahome_step3:
    $ remove_hook(label="fast_sleep_process")
    if fastSleepTick != pause_enter:
        return
    call process_object_click_forced("Bed1", "h") from _rcall_process_object_click_forced_6
    return


label bed_basement_fast_sleep_monica_house_check:
    $ remove_hook()
    m "block"
#    $ miniMapDisabled["JuliaHome"] = ["JuliaHome_LivingRoom"]
#    $ miniMapEnabledOnly = "greg"
    return
