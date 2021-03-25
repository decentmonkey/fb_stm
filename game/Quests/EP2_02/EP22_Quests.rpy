default ep22_started = False
default monicaLateToDick = False

label ep22_init:
    $ questLogDataEnabled = {"0":True, "3":True, "7":True, "18":True, "19":True}
    if monicaKnowAboutKebabWork == True:
        $ questLogDataEnabled["16"] = True
    else:
        $ questLogDataEnabled["15"] = True


    if char_info["Bardie"]["level"] == 2:
        $ char_info["Bardie"]["enabled"] = True
        if bardieBlackmailStage == 0:
            $ add_hook("Teleport_Basement_Pool", "bardieCatchAtStaitsTeleportPoolHook", scene="floor1_stairs", label="bardie_catch_monica_at_stairs_onetime")
            $ add_hook("mimimap_teleport", "bardieCatchAtStaitsMinimapHook", scene="global", label="bardie_catch_monica_at_stairs_onetime")
            $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")

    if char_info["Betty"]["level"] == 2:
        $ char_info["Betty"]["enabled"] = True

    $ move_object("AlexPhotograph", "monica_office_photostudio")
    $ replace_hook("AlexPhotograph", "monica_office_photostudio_alex_dialogue1", "ep22_dialogue6_4", scene="monica_office_photostudio")

    $ remove_objective("dick_money_tomorrow")
    $ add_objective("dick_money_tomorrow", t_("Срочно принести деньги Дику!"), c_pink, 40)
    $ add_hook("basement_monica_after_sleep_dialogue", "ep22_dialogues2_3", scene="global")


    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_13
    img black_screen
    with Dissolve(2.0)
    call ep22_dialogues2_1() from _call_ep22_dialogues2_1
#    $ questHelp("house_5")
    $ rain = False
    $ focus_map("Teleport_Dick_Office", "ep22_dialogues5_0b")
    $ hudDaySkipToEveningEnabled = False
    $ add_hook("basement_monica_before_nap", "ep22_dialogues5_0a", scene="global", lable="hurry_to_dick")
    $ add_hook("map_teleport", "ep22_betty_catch_exit_map", scene="global", label="betty_catch")
    $ add_hook("Gates", "ep22_betty_catch_exit_gates", scene="street_house_gate", label="betty_catch")


    # Инициализируем общение с Диком и Викторией
    $ remove_hook("DickSecretary", "dick_secretary_talk3", scene="dick_office_secretary")
    $ add_hook("DickSecretary", "ep22_quests_Dick1", scene="dick_office_secretary", label="dicksecretary_stage1")
    $ add_hook("Door", "ep22_dialogues5_1", scene="dick_office_secretary", label="dicksecretary_stage1")
    $ move_object("DickTheLawyer", "dick_office_cabinet")
    $ remove_hook("DickTheLawyer", "dick_the_lawyer_talk1", scene="dick_office_cabinet")
    $ add_hook("DickTheLawyer", "ep22_quests_Dick2", scene="dick_office_cabinet", label="dicksecretary_stage2")
    call Dick_Life_init() from _call_Dick_Life_init

    call basement_bedroom1_init() from _call_basement_bedroom1_init
    call basement_bedroom2_init() from _call_basement_bedroom2_init_1

    # Инициализируем Бифа
    call ep22_quests_office_init() from _call_ep22_quests_office_init

    # Инициализируем сцену с бутылкой
    if vodkaTaken == False:
        call init_location("hostel_edge_1_b", "hostel_edge_1_b_init") from _call_init_location_1

    $ ep22_started = True
    return

label ep22_betty_catch_exit_map:
    if obj_name != "Teleport_House" and map_scene == "House" and (map_source_scene == "basement_bedroom1" or map_source_scene == "basement_bedroom2"):
        call ep22_betty_catch_process() from _call_ep22_betty_catch_process
        $ map_source_scene = "floor2"
        return False
    if obj_name != "Teleport_House" and map_scene == "House":
        call ep22_betty_catch_process() from _call_ep22_betty_catch_process_1
        $ map_source_scene = "floor2"
        return False
    return
label ep22_betty_catch_exit_gates:
    if act != "w":
        return True
    call ep22_betty_catch_process() from _call_ep22_betty_catch_process_2
    return False

label ep22_betty_catch_process:
#    $ remove_hook(lable="hurry_to_dick") #debug!!!!

    $ remove_hook(label="betty_catch")
    $ add_hook("map_teleport", "EP22_Quests_Betty0_Fred_scene", scene="global") #Вешаем сцену с Бетти
    $ monicaLastCleaningOfferedDay = day

    call ep22_dialogues2_4() from _call_ep22_dialogues2_4
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    $ add_hook("Spot", "ep22_dialogue2_6a", scene="floor2")
    $ set_var("Spot", actions="l", scene="floor2")
    $ floor2WashingSport = True
    $ spotCleaning = True
    if _return == False:
        #Моника уходит, не терев пятно
        $ autorun_to_object("ep22_dialogues2_5", scene="floor2")
        $ add_char_progress("Betty", -100, "refuse_to_clean_spot1")
        $ char_info["Betty"]["level"] = 1
        $ notif(t__(char_info["Betty"]["name_orig"]) + " " + t__("прогресс понижен!"))
        call change_scene("floor2") from _call_change_scene_220
        return False
    else:
#        $ monicaBettyPanties = True
#        $ monicaBettyPantiesId = 5
        $ move_object("Betty", "floor2")
        $ monicaLateToDick = True
        $ add_cleaning(True)
        call house_cleaning_spot_external_call() from _call_house_cleaning_spot_external_call
        return False
    return

label ep22_dick_enter_map:
    return
