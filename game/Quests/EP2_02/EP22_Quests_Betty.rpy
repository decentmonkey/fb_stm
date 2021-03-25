default ep22_quest_flag1 = False
default ep22_fitness_gym_inited = False
default fitness_gym_visited_amount = 0
default fitness_gym_betty_first_time_interact_with_trainer = True
default fitness_gym_state = 0

default EP22_Quests_Betty3Flag1 = False
default ep24_betty_refused_fitness = 0

label EP22_Quests_Betty0_Fred_scene:
    if cloth != "Governess":
        $ remove_hook()
        $ map_enabled = False
        call ep22_dialogue2_8() from _call_ep22_dialogue2_8
    return

label EP22_Quests_Betty1: #init quest
    $ add_hook("Betty_Life_day", "EP22_Quests_Betty2", scene="global", label="betty_fitness_days")
    $ add_hook("Betty", "EP22_Quests_Betty3", scene="floor2")
    $ questLog(23, True)
    $ questHelp("fitness_1")
    $ questHelpDesc("house_desc6")
    $ questHelp("house_1", True)
    call ep22_Quests_Betty_Monica_Governess_outfit() from _call_ep22_Quests_Betty_Monica_Governess_outfit
    return

label ep22_Quests_Betty_Monica_Governess_outfit:
    # инитим проверки на путешествия в костюме горничной
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep22_dialogue1_4_clothshop", scene="street_cloth_shop", label="monica_governess_outfit_restrictions")
    $ add_hook("Teleport_Shawarma", "ep22_dialogue1_3_slums", scene="street_cloth_shop", label="monica_governess_outfit_restrictions")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep22_dialogue1_2_governess_refuse_to_go", scene="monica_office_entrance", label="monica_governess_outfit_restrictions")
    $ add_hook("Teleport_Inside", "ep22_dialogue1_2_governess_refuse_to_go", scene="street_dick_office", label="monica_governess_outfit_restrictions")
    $ add_hook("map_teleport", "ep22_dialogue1_3_slums_map", scene="global", label="monica_governess_outfit_restrictions")

    return

label EP22_Quests_Betty2: #определение дня фитнеса
    if week_day == 2 or week_day == 4:
        $ bettyFitnessToday = True
        $ move_object("Betty", "floor2")
        call bettyGetTodayPanties() from _call_bettyGetTodayPanties_2
        return False
    else:
        $ bettyFitnessToday = False
    return

label EP22_Quests_Betty3:
    if act=="l":
        return
    if monicaCleaningInProgressEngineWorkingFlag == True:
        call ep22_dialogues4_1b() from _call_ep22_dialogues4_1b
        return False
    if cloth != "Governess":
        call bettyDialogue3() from _call_bettyDialogue3_2
        return False
    call ep22_dialogues4_1() from _call_ep22_dialogues4_1
    if EP22_Quests_Betty3Flag1 == True:
        $ EP22_Quests_Betty3Flag1 = False #Флаг, чтобы ничего не делать (для меню сообщения Барди о фитнесе)
        return False
    if _return == False:
        if bettyFitnessToday == True:
            $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15}, {"driverOnHouseYard":{"v":False, "active":False}}, scene="street_house_main_yard")
            $ move_object("Betty", "empty")
            $ move_object("Driver", "empty")
            call refresh_scene_fade() from _call_refresh_scene_fade_63
        return False
    $ add_cleaning(True)
    $ add_hook("open", "EP22_Quests_Betty4", scene="street_fitness")
    call change_scene("street_fitness", "Fade_long", "snd_car_engine") from _call_change_scene_201
    return False

label EP22_Quests_Betty4: #инитим улицу у фитнеса
    $ remove_hook()
    $ fitnessStreetStoredScene = store_scene("street_fitness")
    $ add_hook("Teleport_Inside", "EP22_Quests_Betty5", scene="street_fitness")
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Betty_Monica", "click" : "ep22_dialogues4_2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_object_to_scene("Betty", {"type":2, "base":"Fitness_Street_Betty", "click" : "ep22_dialogues4_2", "actions" : "lt", "zorder" : 10}, scene="street_fitness")
    $ add_object_to_scene("Car", {"type":2, "base":"Street_Fitness_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3}, scene="street_fitness")
    $ add_object_to_scene("Driver", {"type":2, "base":"Street_Fitness_Driver", "click" : "street_house_main_yard_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]}, scene="street_fitness")
    $ map_enabled = False
    $ scene_image = "scene_Fitness_Street_Driver"
    $ autorun_to_object("ep22_dialogues4_1a", scene="street_fitness")
    if ep22_fitness_gym_inited == False:
        $ add_location("fitness_gym", caption=t_("Fitness Gym"), label="fitness_gym", init_label="fitness_gym_init", parent="Fitness")
        $ add_location("fitness_locker_1", caption=t_("Fitness Gym"), label="fitness_locker_1", init_label="fitness_locker_1_init", parent="Fitness")
        $ add_location("fitness_locker_2", caption=t_("Fitness Gym"), label="fitness_locker_2", init_label="fitness_locker_2_init", parent="Fitness")
#        call fitness_gym_init()
#        call fitness_locker_1_init()
#        call fitness_locker_2_init()
        $ add_hook("Teleport_Outside", "ep22_dialogues4_2a", scene="fitness_gym")
        $ add_hook("Trainer", "ep22_dialogues4_3a", scene="fitness_gym")
        $ add_hook("Monica", "ep22_dialogues4_4", scene="fitness_gym")
        $ add_hook("Betty", "ep22_dialogues4_4", scene="fitness_gym")
        $ add_hook("Teleport_Locker_1", "EP22_Quests_Betty5a", scene="fitness_gym")
        $ ep22_fitness_gym_inited = True
    $ api_scene_name = "street_fitness"
    $ add_hook("Teleport_Inside", "EP22_Quests_Betty5", scene="street_fitness")
    $ move_object("Stephanie", "fitness_locker_1")
    $ move_object("Rebecca", "fitness_locker_1")
#    $ restore_scene(fitnessStreetStoredScene)

    return

label EP22_Quests_Betty5:
    if act=="l":
        return
    music Loved_Up
    $ autorun_to_object("ep22_dialogues4_3", scene="fitness_gym")
    $ move_object("Betty", "fitness_gym")
    call change_scene("fitness_gym") from _call_change_scene_202
    return False

label EP22_Quests_Betty5a:
    if fitness_gym_visited_amount > 0:
        $ fitness_locker_1_stephanie_rebecca_suffix = 2
        $ move_object("Betty", "fitness_locker_1")
    else:
        $ autorun_to_object("ep22_dialogues4_5", scene="fitness_locker_1")
    return

label EP22_Quests_Betty5b:
    if fitness_gym_visited_amount == 0:
        call ep22_dialogues4_5a() from _call_ep22_dialogues4_5a
    else:
        if fitness_gym_state == 0:
            call ep22_dialogues4_8() from _call_ep22_dialogues4_8
        if fitness_gym_state == 1:
            call ep23_dialogues3_2() from _call_ep23_dialogues3_2

    $ move_object("Betty", "fitness_locker_2")
    $ move_object("Stephanie", "fitness_locker_2")
    $ move_object("Rebecca", "fitness_locker_2")
    music Loved_Up
    call change_scene("fitness_locker_2", "Fade_long") from _call_change_scene_203
    return


label EP22_Quests_Betty6:
    #ждать в раздевалке
    #проверяем на сцену со Фредом
    if monicaBardieRalphSeducingStage == 5 or monicaBardieRalphSeducingStage == 6:
        call ep214_dialogues5_bardie_ralph_2() from _rcall_ep214_dialogues5_bardie_ralph_2
        menu:
            "Взять одежду Бетти и ехать домой.":
                call ep214_quests_ralph2() from _rcall_ep214_quests_ralph2
                return
            "Просто ждать.":
                pass
    if fitness_gym_state >= 1:
        call ep22_dialogues4_7() from _call_ep22_dialogues4_7
    if fitness_gym_state == 0:
        if fitness_gym_visited_amount >= 3: #на третье посещение сцена со Фредом
            call ep23_dialogues3_1() from _call_ep23_dialogues3_1
            $ fredState = 1
            $ fitness_gym_state = 1
            $ char_info["Rebecca"]["enabled"] = True
            $ char_info["Stephanie"]["enabled"] = True

            $ add_char_progress("Rebecca", 10, "fred_kicked")
            $ add_char_progress("Stephanie", 10, "fred_kicked")

            $ add_hook("monica_cleaning_spot_start", "ep23_quests_fred_cleaning_spot_init", scene="global")
            $ replace_hook("Betty_Life_day1", "Betty_Life_day2", scene="global")
            $ add_hook("Driver", "ep23_quests_fred_talking_street_yard", scene="street_house_main_yard")
            $ add_hook("change_time_day", "ep23_quests_fred_betty_sex", scene="global", priority=50)

        else:
            call ep22_dialogues4_7() from _call_ep22_dialogues4_7_1

#    if fitness_gym_visited_amount >= 1 and steveVisit1PlannedComplete == False:
    $ questHelp("house_10", True)
    if fitness_gym_visited_amount >= 1:
#        call ep24_quests_steve1() from _call_ep24_quests_steve1 #Планируем в субботу приход Стива
        if fitness_gym_visited_amount == 1:
            call ep24_dialogues3_fitness3()
        if fitness_gym_visited_amount == 2:
            call ep24_dialogues3_fitness3b()
        if fitness_gym_visited_amount == 3:
            call ep24_dialogues3_fitness3c()
        if fitness_gym_visited_amount == 4:
            call ep24_dialogues3_fitness3d()
            call ep00_ralph1() # инициализируем соблазнение Ральфа

#        call ep24_quests_bardie1b() from _call_ep24_quests_bardie1b_1 # Планируем шантаж Барди

    call process_hooks("fitness_end", "global") from _call_process_hooks_38
    if _return == False:
        return
    sound highheels_short_walk
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    $ map_enabled = False
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_2_[cloth][day_suffix]", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_hook("open", "EP22_Quests_Betty6a", scene="street_fitness")
    $ autorun_to_object("ep22_dialogues4_7a", scene="street_fitness")
    call change_scene("street_fitness", "Fade_long", False) from _call_change_scene_204

    return

label EP22_Quests_Betty6a:
    $ remove_hook()
    $ scene_image = "scene_Fitness_Street_Driver"
    return

label EP22_Quests_Betty6b:
    $ remove_hook()
    $ scene_image = "scene_Fitness_Street_Driver"
    $ autorun_to_object("ep22_dialogues4_7b", scene="street_fitness")
    $ add_object_to_scene("Betty", {"type":2, "base":"Fitness_Street_Betty2", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ autorun_to_object("ep22_dialogues4_7b")
    if char_info["Betty"]["level"] < 4: # Далее прогресс добавляется черех хук fitness_end
        $ add_char_progress("Betty", bettyFitnessProgressAmount, "fitness_day_" + str(day))

    return

label EP22_Quests_Betty7: #показ пикч занятия фитнесом
    call ep22_dialogues4_6() from _call_ep22_dialogues4_6
    if _return == False:
        return False
    call EP22_Quests_Betty6() from _call_EP22_Quests_Betty6_1
    return

label EP22_Quests_Betty8: #уезжают
    $ map_enabled = True
    $ fitness_gym_visited_amount +=1
    $ restore_scene(fitnessStreetStoredScene)
    img black_screen
    with Dissolve(1.0)
    sound snd_car_turn_on
    pause 2.0
    sound snd_car_engine
    img scene_Map
    pause 2.0
    $ move_object("Driver", "street_house_main_yard")
    $ move_object("Betty", "bedroom1")
    $ changeDayTime("evening")
#    if fitness_gym_visited_amount == 1:
#        $ questHelp("house_11")
    call change_scene("street_house_main_yard", "Fade_long", "snd_car_engine") from _call_change_scene_205
    return
