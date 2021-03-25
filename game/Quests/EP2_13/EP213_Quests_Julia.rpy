default ep213_quests_julia_stage = 0
default monica_living_at_juliahome = False
default monica_juliahome_outside_cloth = False
default monica_juliahome_outside_cloth_type = False

default monica_juliahome_cloth = "JuliaCloth1"

default juliahome_evening_sleep_event_active = False
default juliahome_julia_shower_day = 0
default juliahome_work_action_day = 0
default juliahome_work_action_evening_day = 0
default julia_progress_list = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
default juliahome_julia_shower_time = 0
default juliahome_kitchen_events_activated = False

default juliahome_julia_piss1_day = 0
default juliaNotifBlockedOnce = False

label ep213_quests_julia1: # Моника предлагает Юлии жить вместе
    call ep213_dialogues5_julia_16() from _rcall_ep213_dialogues5_julia_16
    $ ep213_quests_julia_stage = 1
    $ ep210_julia_evening_at_work = False # Вечером Юлия не на работе (а дома)
    $ add_hook("JuliaHome", "ep213_quests_julia2", scene="street_juliahome", label="juliahome1")
    $ add_objective("come_julia_evening", t_("Прийти к Юлии домой вечером."), c_pink, 105)

    return

label ep213_quests_julia2: # Заходит вечером в дом
    if act=="l" or day_time != "evening":
        return
    if cloth != "CasualDress1":
        call ep210_dialogues5_julia_3_4a() from _rcall_ep210_dialogues5_julia_3_4a_2
        return False
    $ remove_hook()
    call ep213_dialogues5_julia_7() from _rcall_ep213_dialogues5_julia_7
    # Инициализируем жизнь в доме
    python:
        questHelp("julia_35", True)
        questHelp("julia_36")
        questHelp("julia_38")
        questHelpDesc("julia_desc4", "julia_desc5")
        remove_objective("come_julia_evening")
        ep213_quests_julia_stage = 2
        monica_living_at_juliahome = True
        ep210_julia_evening_at_work = True # Вечером Юлия на работе
        move_object("Julia", "juliahome_livingroom")
        set_var("Julia", base="JuliaHome_LivingRoom_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeLivingRoomJuliaSuffix][day_suffix]", scene="juliahome_livingroom")
        set_var("Wardrobe", actions="lh", scene="juliahome_livingroom")
        set_var("Bed1", actions="lh", scene="juliahome_livingroom")
        set_var("Julia", base="JuliaHome_Bathroom_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeBathroomJuliaSuffix]", scene="juliahome_bathroom")
        set_var("Julia", base="JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeKitchenJuliaSuffix]", scene="juliahome_kitchen")
        set_var("Julia", base="JuliaHome_Kitchen_Julia_[juliaHomeLivingRoomJuliaCloth]_[juliaHomeKitchenJuliaSuffix]", scene="juliahome_bathroomshower")
        juliaHomeLivingRoomMonicaSuffix = 3
        juliaHomeLivingRoomJuliaSuffix = 3
        monica_juliahome_outside_cloth = cloth
        monica_juliahome_outside_cloth_type = cloth_type
        cloth = monica_juliahome_cloth
        cloth_type = "juliahome"
        juliaHomeLivingRoomJuliaCloth = "JuliaCloth1"
        minimapJuliaGenerateEnabled = True
    call juliahome_kitchen_init2() from _rcall_juliahome_kitchen_init2
    call juliahome_bathroomshower_init2() from _rcall_juliahome_bathroomshower_init2

    $ add_char_progress("Julia", 100, "monica_julia_live_together_start")
    $ char_info["Julia"]["level"] = 8
    $ add_hook("Monica", "ep213_quests_julia21_monica_click", scene="juliahome_bathroom", label="juliahome_shower", quest="juliahome")

    $ add_hook("Shower", "ep213_quests_julia3_shower", scene="juliahome_bathroomshower", label="juliahome_shower", quest="juliahome")
    $ add_hook("Kitchen", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item1", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item2", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item3", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item4", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Kitchen_Item5", "ep213_quests_julia4_kitchen", scene="juliahome_kitchen", label="juliahome_kitchen", quest="juliahome")
    $ add_hook("Teleport_Street", "ep213_quests_julia5_exit_street", scene="juliahome_kitchen", label="juliahome_exit", quest="juliahome")
    $ add_hook("Wardrobe", "ep213_quests_julia6_wardrobe", scene="juliahome_livingroom", label="juliahome_wardrobe", quest="juliahome")
    $ add_hook("Toilet", "ep213_quests_julia7_toilet", scene="juliahome_bathroom", label="juliahome_toilet", quest="juliahome")
    $ add_hook("JuliaHome", "ep213_quests_julia9_enter_building", scene="street_juliahome", label="juliahome_enter", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_livingroom", label="juliahome_julia_regular1", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_kitchen", label="juliahome_julia_regular1", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia11_julia", scene="juliahome_bathroom", label="juliahome_julia_regular1", quest="juliahome")
    $ add_hook("Bed1", "juliahome_bed", scene="juliahome_livingroom", label="juliahome_bed", quest="juliahome")
    $ add_location("World", caption=("World"), label="world", init_label="world_init", parent="none")

    $ add_hook("exit_scene", "ep213_quests_julia12_exit_livingroom", scene="juliahome_livingroom", label="juliahome_livingroom_exit", quest="juliahome")
    $ add_hook("before_open", "ep213_quests_julia13_enter_livingroom", scene="juliahome_livingroom", label="juliahome_livingroom_enter", quest="juliahome")
    $ add_hook("before_open", "ep213_quests_julia20_check_julia_movement", scene="juliahome_kitchen", label="juliahome_kitchen_enter", quest="juliahome")

    $ add_hook("map_teleport", "ep213_quests_julia14_map_teleport", scene="global", label="juliahome_map_teleport", priority=10000, quest="juliahome")
    $ add_hook("map_teleport_after", "ep213_quests_julia16_exit_house", scene="global", label="juliahome_map_teleport", priority=10000, quest="juliahome")
    $ add_hook("exit_scene", "ep213_quests_julia3_shower_exit", scene="juliahome_bathroom", label="juliahome_bathroom_exit", quest="juliahome")
    $ add_hook("change_time_evening", "ep213_quests_julia17_life_evening", scene="global", label="juliahome_julia_life_evening", quest="juliahome")

    $ add_hook("juliahome_monica_after_sleep", "ep213_quests_julia21_monica_after_sleep", scene="global", label="juliahome_julia_life_after_sleep", quest="juliahome")
    $ add_hook("Julia", "ep213_quests_julia22_work_julia_regular", scene="working_office_cabinet", label="juliawork_lovestory_regular", quest="juliahome")

    $ questLog(74, True)

    call ep213_quests_julia2_req_init() from _rcall_ep213_quests_julia2_req_init

    call change_scene("juliahome_livingroom", "Fade_long", False) from _rcall_change_scene_97
    return False

label ep213_quests_julia2_req_init:
    python:
        menu_required["julia_work1"] = {
            "Массаж для Юлии.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene1},
            "На рабочем столе Моники.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene3},
            "На диване в комнате отдыха.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene6},
            "Под столом Юлии.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene7},
            "В отделе отчетов.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene9},
            "Укрепление отношений.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene9},
            "Приласкать ее грудь.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene2},
            "Приласкать ее киску.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene2b},
            "Продолжить ласкать Юлию.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene2c},
            "Поцеловать Юлию.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene5}
        }

        menu_required["julia_work2"] = {
            "Продолжить ласкать Юлию.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene5b},
            "Заняться сексом.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene5c},
            "Зайти в душ к Юлии.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene4},
            "Поцеловать Юлию.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene8},
            "Приласкать ее киску.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene8b},
            "Засунуть в нее дилдо.":{"name":"Julia", "level":8, "current_progress":juliaMonicaRelationshipRequiredScene8c}
        }
    return

label ep213_quests_julia3_shower: # клик на душ
    if act=="l":
        return

    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return False
    call ep213_dialogues5_julia_15c2() from _rcall_ep213_dialogues5_julia_15c2
    if char_info["Julia"]["level"] >= 8 and char_info["Julia"]["current_progress"] >= juliaMonicaRelationshipRequiredScene10 and get_active_objects("Julia", scene="street_juliahome", recursive=True) != False:
        call ep213_dialogues5_julia_10b() from _rcall_ep213_dialogues5_julia_10b
    $ monicaLastShowerDay = day # Последний день, когда Моника принимала душ
    $ monicaLastShowerDayTime = day_time
    $ juliaHomeBathroomMonicaSuffix = 3
    if day_time != "evening":
        call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life
    call change_scene("juliahome_bathroom") from _rcall_change_scene_98

    return False

label ep213_quests_julia3_shower_exit: # выход из ванной (где туалет)
    if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 2:
        $ move_object("Julia", "juliahome_livingroom")
        call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life_1
    return

label ep213_quests_julia4_kitchen: # клик на кухню (еда)
    if act=="l":
        return

    if get_active_objects("Julia", scene="street_juliahome", recursive=True) != False and juliaHomeLivingRoomJuliaSuffix == 2 and week_day != 7: # Если Юлия дома и спит
        $ juliahome_kitchen_events_activated = True
        call ep213_dialogues5_julia_9() from _rcall_ep213_dialogues5_julia_9
        if _return != False:
            $ monica_eated()
#            call ep213_quests_julia17_life()
        $ move_object("Julia", "juliahome_bathroom")
        $ juliaHomeLivingRoomMonicaSuffix = 3
        $ juliaHomeLivingRoomJuliaSuffix = 3
        $ juliaHomeBathroomMonicaSuffix = 1
        $ juliaHomeBathroomJuliaSuffix = 2
        call refresh_scene_fade() from _rcall_refresh_scene_fade_64
        return False

    if monicaEatedLastDay != day:
        fadeblack
        imgf 30842
        sound snd_eating
        w
#        pause 1.5
        $ monica_eated()
        call refresh_scene_fade() from _rcall_refresh_scene_fade_65
    else:
        call ep213_dialogues5_julia_15b() from _rcall_ep213_dialogues5_julia_15b
    return False

label ep213_quests_julia5_exit_street: # Моника выходит на улицу
    $ cloth = monica_juliahome_outside_cloth
    $ cloth_type = monica_juliahome_outside_cloth_type
#    $ juliaHomeLivingRoomJuliaSuffix = 3
    if scene_name == "juliahome_kitchen":
        $ autorun_to_object("ep213_dialogues5_julia_15e", scene="street_juliahome")

    if get_active_objects("Julia", scene="street_juliahome", recursive=True) != False and ep213_dialogues5_julia_13_day != day and day_time == "day":
        if cloth == "CasualDress1":
            if week_day != 7:
                call ep213_dialogues5_julia_13() from _rcall_ep213_dialogues5_julia_13
            else:
                call ep213_dialogues5_julia_13a() from _rcall_ep213_dialogues5_julia_13a
            $ ep213_dialogues5_julia_13_day = day

    call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life_2
    call change_scene("street_juliahome", "Fade_long", "snd_door_close1") from _rcall_change_scene_99
    return False

label ep213_quests_julia6_wardrobe: # гардероб
    if act=="l":
        call ep213_dialogues5_julia_17() from _rcall_ep213_dialogues5_julia_17
        return False
    call ep213_dialogues5_julia_18_wardrobe() from _rcall_ep213_dialogues5_julia_18_wardrobe
    if _return == 0:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_66
        return False
    $ monica_juliahome_outside_cloth = cloth
    $ monica_juliahome_outside_cloth_type = cloth_type
    call ep213_quests_julia5_exit_street() from _rcall_ep213_quests_julia5_exit_street
    return False

label ep213_quests_julia7_toilet: # Моника писает
    if act=="l":
        return
    if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 1:
        mt "Я - Леди!"
        mt "И я не собираюсь писать на глазах у своей гувернантки!"
        mt "Тем более, не знаю, что этой дуре может еще прийти в голову..."
        return False
    if monicaLastPissedDay == day and day_time == monicaLastPissedDayTime:
        mt "Я уже писала недавно. Я пока не хочу."
        return False
    call ep213_dialogues5_julia_15d() from _rcall_ep213_dialogues5_julia_15d
    $ monicaLastPissedDay = day # Последний день, когда Моника писала
    $ monicaLastPissedDayTime = day_time
    call refresh_scene_fade() from _rcall_refresh_scene_fade_67
    return False

label ep213_quests_julia8_minimap_teleport: # Телепорт по миникарте
    if minimapTeleportButtonName == "JuliaHome_Street":
        if scene_name != "street_juliahome":
            call ep213_quests_julia5_exit_street() from _rcall_ep213_quests_julia5_exit_street_1
        return
    if scene_name == "street_juliahome":
        call ep213_quests_julia10_check_enter_home() from _rcall_ep213_quests_julia10_check_enter_home
        fadeblack
        $ monica_juliahome_outside_cloth = cloth
        $ monica_juliahome_outside_cloth_type = cloth_type
        $ cloth = monica_juliahome_cloth
        $ cloth_type = "juliahome"
        sound snd_fabric1
        pause 1.0

    if minimapTeleportButtonName == "JuliaHome_LivingRoom":
        call change_scene("juliahome_livingroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_100
    if minimapTeleportButtonName == "JuliaHome_Kitchen":
        call change_scene("juliahome_kitchen", "Fade", "snd_walk_barefoot") from _rcall_change_scene_101
    if minimapTeleportButtonName == "JuliaHome_Bathroom":
        call change_scene("juliahome_bathroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_102

    call ep213_quests_julia20_check_julia_movement() from _rcall_ep213_quests_julia20_check_julia_movement

    return

label ep213_quests_julia9_enter_building: # входит с улицы через вход
    if act=="l":
        return
    call ep213_quests_julia10_check_enter_home() from _rcall_ep213_quests_julia10_check_enter_home_1
    fadeblack
    $ monica_juliahome_outside_cloth = cloth
    $ monica_juliahome_outside_cloth_type = cloth_type
    $ cloth = monica_juliahome_cloth
    $ cloth_type = "juliahome"
    sound snd_fabric1
    pause 1.0
    call change_scene("juliahome_livingroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_103
    return False

label ep213_quests_julia10_check_enter_home: # события при входе в дом
    $ juliaHomeLivingRoomMonicaSuffix = 3
    $ juliaHomeLivingRoomJuliaSuffix = 3
    if day_time == "evening":
        $ move_object("Julia", "juliahome_livingroom")
    return

label ep213_quests_julia11_julia: # регулярный разговор с Юлией (везде)
    if act=="l":
        call ep210_dialogues5_julia_3_2() from _rcall_ep210_dialogues5_julia_3_2_3
        return False

    if scene_name == "juliahome_bathroom" and juliaHomeBathroomJuliaSuffix == 1: # Юлия принимает душ
#        if # хватает уровня
        call ep213_dialogues5_julia_10() from _rcall_ep213_dialogues5_julia_10
        if _return == False:
            call change_scene("juliahome_kitchen", "Fade_long", "snd_walk_barefoot") from _rcall_change_scene_104
            return False

        $ move_object("Julia", "juliahome_livingroom")
        $ juliaHomeBathroomMonicaSuffix = 3
        call change_scene("juliahome_bathroomshower", "Fade_long", False) from _rcall_change_scene_105
        call change_scene("juliahome_bathroom", "Fade_long", False) from _rcall_change_scene_106
        return False

    if scene_name == "juliahome_bathroom" and juliaHomeBathroomJuliaSuffix == 2 and char_info["Julia"]["level"] >= 9: # Юлия сидит на унитазе
        call ep213_dialogues5_julia_10a() from _rcall_ep213_dialogues5_julia_10a
        if _return == False:
            call change_scene("juliahome_kitchen", "Fade_long", "snd_walk_barefoot") from _rcall_change_scene_130
            return False
        $ juliahome_julia_piss1_day = day
        $ move_object("Julia", "juliahome_livingroom")
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
        $ enter_scene("ep213_dialogues5_julia_10a2", once=True)
        call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life_6
        call change_scene("street_juliahome", "Fade_long") from _rcall_change_scene_131
        return False

    if scene_name == "juliahome_kitchen": # Регулярный разговор на кухне
        call ep213_dialogues5_julia_9b() from _rcall_ep213_dialogues5_julia_9b
        call refresh_scene_fade() from _rcall_refresh_scene_fade_68
        return False

    if scene_name == "juliahome_livingroom" and juliaHomeLivingRoomJuliaSuffix == 1:
        call ep213_dialogues5_julia_8() from _rcall_ep213_dialogues5_julia_8
        if _return == 0: # Просыпается только Моника
            $ juliaHomeLivingRoomMonicaSuffix = 2
            $ juliaHomeLivingRoomJuliaSuffix = 2
            if juliahome_kitchen_events_activated == False:
                $ autorun_to_object("ep213_dialogues5_julia_19_about_kitchen")
            call refresh_scene_fade() from _rcall_refresh_scene_fade_69
            return False

        if _return == 1: # Просыпаются
            $ juliaHomeLivingRoomMonicaSuffix = 3
            $ juliaHomeLivingRoomJuliaSuffix = 3
            call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life_3
            call refresh_scene_fade() from _rcall_refresh_scene_fade_70
            return False

        if _return == 2: # Поспать еще (Моника спит, Юлия уходит, либо остается если выходной)
            $ juliaHomeLivingRoomMonicaSuffix = 3
            $ juliaHomeLivingRoomJuliaSuffix = 3
            call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life_4
            call refresh_scene_fade() from _rcall_refresh_scene_fade_71
            return False

    if scene_name == "juliahome_livingroom" and juliaHomeLivingRoomJuliaSuffix == 3 and week_day == 7 and day_time != "evening":
        call ep213_dialogues5_julia_12a() from _rcall_ep213_dialogues5_julia_12a
        $ move_object("Julia", "empty")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_72
        return False
    call ep213_dialogues5_julia_16a() from _rcall_ep213_dialogues5_julia_16a
    return False

label ep213_quests_julia12_exit_livingroom:
    if juliaHomeLivingRoomMonicaSuffix == 1:
        if day_time == "day":
            $ juliaHomeLivingRoomMonicaSuffix = 2
            $ juliaHomeLivingRoomJuliaSuffix = 2
    return

label ep213_quests_julia13_enter_livingroom:
    if cloth_type != "juliahome":
        $ monica_juliahome_outside_cloth = cloth
        $ monica_juliahome_outside_cloth_type = cloth_type
        $ cloth = monica_juliahome_cloth
        $ cloth_type = "juliahome"

    if juliaHomeLivingRoomJuliaSuffix == 1 or juliaHomeLivingRoomJuliaSuffix == 2:
        $ juliaHomeLivingRoomJuliaSuffix = 2
        $ juliaHomeLivingRoomMonicaSuffix = 2
    if juliaHomeLivingRoomJuliaSuffix != 1 and juliaHomeLivingRoomJuliaSuffix != 2:
        $ set_active("Bed1", True, scene="juliahome_livingroom")

    return

label ep213_quests_julia14_map_teleport: # вызов перед уходом по карте
    # переодеваем Монику назад
    if lastSceneName == "juliahome_livingroom":
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
    return


label ep213_quests_julia16_exit_house: # Жизнь Юлии при выходе из дома
    if previous_map_scene == "JuliaHome":
        if check_scene_parent(scene_name, "street_juliahome") == True:
            return
        call ep213_quests_julia17_life() from _rcall_ep213_quests_julia17_life_5
    return

label ep213_quests_julia17_life:
    if week_day != 7 and day_time != "evening":
        if get_active_objects("Julia", scene="street_juliahome", recursive=True) != False and juliaNotifBlockedOnce == False:
            $ notif(t_("Юлия ушла на работу."))
            $ juliaNotifBlockedOnce = False
        $ juliaHomeLivingRoomJuliaSuffix = 3
        $ move_object("Julia", "working_office_cabinet") # Юлия уходит на работу
    return

label ep213_quests_julia17_life_evening:
    if check_scene_parent(scene_name, "street_juliahome", recursive = True) != False:
        $ move_object("Julia", "juliahome_livingroom")
#        $ juliaHomeLivingRoomMonicaSuffix = 3
        $ juliaHomeLivingRoomJuliaSuffix = 3

    return


label ep213_quests_julia18_progress(scene_idx, status, amount):
    python:
        if status != julia_progress_list[scene_idx]:
            julia_progress_list[scene_idx] = status
            if status == True:
                add_char_progress("Julia", amount, "julia_relations_progress_idx_" + str(scene_idx), duplicate = True)
            else:
                add_char_progress("Julia", -amount, "julia_relations_progress_idx_" + str(scene_idx), duplicate = True)
    return


label ep213_quests_julia19_evening_scene: # вечерняя сцена
    call ep213_dialogues5_julia_11() from _rcall_ep213_dialogues5_julia_11
    return

label ep213_quests_julia20_check_julia_movement:
    if day_time == "evening" and get_active_objects("Julia", scene="juliahome_livingroom") != False and juliahome_julia_shower_day != day and scene_name != "juliahome_livingroom":
        $ notif(t_("Юлия ушла в душ."))
        $ juliahome_julia_shower_day = day
        $ move_object("Julia", "juliahome_bathroom")
        $ juliaHomeBathroomJuliaSuffix = 1
        python:
            rooms_list1 = get_rooms_recursive("street_juliahome")
            for room1 in rooms_list1:
                add_hook("before_open", "ep213_quests_julia20_check_julia_movement_after_shower", scene=room1, label=["evening_time_temp", "juliahome_aftershower"])
            juliahome_julia_shower_time = 0

    return

label ep213_quests_julia20_check_julia_movement_after_shower:
    $ juliahome_julia_shower_time += 1
    if juliahome_julia_shower_time > 2:
        if get_active_objects("Julia", scene="juliahome_bathroom") != False and juliaHomeBathroomJuliaSuffix == 1: # Если Юлия в душе
            $ move_object("Julia", "juliahome_livingroom")
            $ juliaHomeLivingRoomJuliaSuffix = 3
        $ remove_hook(label="juliahome_aftershower")
    return

label ep213_quests_julia21_monica_click:
    if act=="l":
        call ep211_dialogues4_julia_11l() from _rcall_ep211_dialogues4_julia_11l_5
        return False
    return

label ep213_quests_julia21_monica_after_sleep:
    $ move_object("Julia", "juliahome_livingroom")
    return


label ep213_quests_julia22_work_julia_regular:
    call ep213_quests_julia2_req_init() from _rcall_ep213_quests_julia2_req_init_1
    if monica_living_at_juliahome == False:
        return
    if act == "l":
        return
    if day_time != "evening":
        call ep213_dialogues5_julia_1() from _rcall_ep213_dialogues5_julia_1
    else:
        call ep213_dialogues5_julia_1a() from _rcall_ep213_dialogues5_julia_1a
    if _return == 0:
        if day_time != "evening":
            call ep210_dialogues5_julia_4_1() from _rcall_ep210_dialogues5_julia_4_1
            $ ep210_julia_kissed_day_day = day
        else:
            call ep210_dialogues5_julia_4_3() from _rcall_ep210_dialogues5_julia_4_3
            $ ep210_julia_kissed_day_evening = day

    if _return == 1: # Массаж для Юлии
        call ep213_dialogues5_julia_2() from _rcall_ep213_dialogues5_julia_2
        $ juliahome_work_action_day = day
    if _return == 2: # На рабочем столе Моники.
        call ep213_dialogues5_julia_3() from _rcall_ep213_dialogues5_julia_3
        $ juliahome_work_action_day = day
    if _return == 3: # На диване в комнате отдыха
        call ep213_dialogues5_julia_4() from _rcall_ep213_dialogues5_julia_4
        $ juliahome_work_action_day = day
    if _return == 4: # Под столом Юлии
        call ep213_dialogues5_julia_5() from _rcall_ep213_dialogues5_julia_5
        $ juliahome_work_action_day = day
    if _return == 5: # В отделе отчетов
        call ep213_dialogues5_julia_6() from _rcall_ep213_dialogues5_julia_6
        $ move_object("Julia", "juliahome_livingroom")
        $ juliahome_work_action_evening_day = day
        call change_scene("working_office2", "Fade_long", False) from _rcall_change_scene_107
        return False
    if _return == 6: # Ласкать попу Юлии
        call ep216_dialogues4_fred_7() from _rcall_ep216_dialogues4_fred_7
        $ juliahome_work_action_day = day



    call refresh_scene_fade() from _rcall_refresh_scene_fade_73
    return False
