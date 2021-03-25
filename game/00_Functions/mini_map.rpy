default miniMapData = []
default miniMapSubst = {}
default miniMapEnabledOnly = []
default miniMapDisabled = []
default miniMapDisabled2 = []
default miniMapOfficeActivated = False
default miniMapTurnedOff2 = False
default miniMapOpened = False
default miniMapOpenButtonImg = "Open_Button_Map1"
default miniMapOpenButtonImg2 = "Open_Button_Map2"

default miniMapHousePreset = "default"

default minimapBettyFloor2Enabled = False
default minimapJuliaGenerateEnabled = False

label miniMapOpen:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = True
    show screen hud_minimap(miniMapData)
    return
label miniMapClose:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = False
    show screen hud_minimap(miniMapData)
    return

label miniMapHouseGenerate:
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Map2"
    $ miniMapData = []
    if miniMapHousePreset == "default":
        if owner == "Monica":
            $ miniMapData.append({"name":"Bedroom", "caption":t_("Bedroom"), "img":"Bedroom_Map", "teleport_scene":"bedroom2", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Bathroom", "caption":t_("Bathroom"), "img":"Bathroom_Map", "teleport_scene":"bathroom_bath", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Floor1", "caption":t_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Floor2", "caption":t_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Kitchen", "caption":t_("Kitchen"), "img":"Kitchen_Map", "teleport_scene":"kitchen2", "teleport_type":"scene"})
        #    $ miniMapData.append({"name":"Basement", "caption":t_("Basement"), "img":"Basement_Map", "teleport_scene":"basement_pool", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Street_Yard", "caption":t_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out", "teleport_type":"function"})
            $ miniMapData.append({"name":"Basement", "caption":t_("Basement"), "img":"Basement_Bedroom_Map", "teleport_scene":"basement_bedroom2", "teleport_type":"scene"})
        if owner == "Betty":
            $ miniMapData.append({"name":"Street_Yard", "caption":t_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out_others", "teleport_type":"function"})
            $ miniMapData.append({"name":"Floor1", "caption":t_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
            if minimapBettyFloor2Enabled == True:
                $ miniMapData.append({"name":"Floor2", "caption":t_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
    if miniMapHousePreset == "laundry":
        if owner == "Monica":
            $ miniMapData.append({"name":"Bedroom", "caption":t_("Bedroom"), "img":"Bedroom_Map", "teleport_scene":"bedroom2", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Bathroom", "caption":t_("Bathroom"), "img":"Bathroom_Map", "teleport_scene":"bathroom_bath", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Floor1", "caption":t_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Floor2", "caption":t_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
    #        $ miniMapData.append({"name":"Kitchen", "caption":t_("Kitchen"), "img":"Kitchen_Map", "teleport_scene":"kitchen2", "teleport_type":"scene"})
        #    $ miniMapData.append({"name":"Basement", "caption":t_("Basement"), "img":"Basement_Map", "teleport_scene":"basement_pool", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Street_Yard", "caption":t_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out", "teleport_type":"function"})
            $ miniMapData.append({"name":"Laundry", "caption":t_("Laundry"), "img":"Basement_Laundry_Map", "teleport_scene":"basement_laundry", "teleport_type":"scene"})
            $ miniMapData.append({"name":"Basement", "caption":t_("Basement"), "img":"Basement_Bedroom_Map", "teleport_scene":"basement_bedroom2", "teleport_type":"scene"})
        if owner == "Betty":
            $ miniMapData.append({"name":"Street_Yard", "caption":t_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out_others", "teleport_type":"function"})
            $ miniMapData.append({"name":"Floor1", "caption":t_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
            if minimapBettyFloor2Enabled == True:
                $ miniMapData.append({"name":"Floor2", "caption":t_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
    return

label miniMapHostelGenerate:
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Hostel_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Hostel_Map2"
    $ miniMapData = []
#    $ miniMapData.append({"name":"Hostel_Edge_1_c", "caption":t_("BLIND ALLEY"), "img":"Hostel_Edge_1_c_Map", "teleport_scene":"enter_hostel_edge_1_c", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Place_Shawarma", "caption":t_("Shawarma"), "img":"Street_Whores_Place_Shawarma_Map", "teleport_scene":"whores_place_shawarma", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Place_Whores", "caption":t_("Whores place"), "img":"Street_Whores_Place_Whores_Map", "teleport_scene":"whores_place", "teleport_type":"scene"})
    if slumsDirtyStreetMiniMapActive == True:
        $ miniMapData.append({"name":"Street_Whores_Street1", "caption":t_("Dirty street"), "img":"Street_Whores_Street1_Map", "teleport_scene":"whores_place_street1", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Place_Car_Stop", "caption":t_("Street Edge"), "img":"Street_Whores_Place_Car_Stop_Map", "teleport_scene":"street_corner", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Hostel_Street3", "caption":t_("POOR STREET"), "img":"Hostel_Street3_Map", "teleport_scene":"hostel_street3", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Hostel_Street2", "caption":t_("DIRTY STREET"), "img":"Hostel_Street2_Map", "teleport_scene":"hostel_street2", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Hostel_Street", "caption":t_("HOSTEL STREET"), "img":"Hostel_Street_Map", "teleport_scene":"hostel_street", "teleport_type":"scene"})
    if slumsApartmentsMiniMapActive == True:
        $ miniMapData.append({"name":"Slums_Apartments", "caption":t_("OLD HOUSE"), "img":"MonicaHome_Street_Map", "teleport_scene":"street_monicahome", "teleport_type":"scene"})
    return

label miniMapOfficeGenerate:
    if miniMapOfficeActivated == False:
        return
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Office_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Office_Map2"
    $ miniMapData = []
    $ miniMapData.append({"name":"Office_Biff_Cabinet", "caption":t_("Biff's Office"), "img":"Office_Monica_Cabinet", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_cabinet_table", "teleport_type":"function"})
    $ miniMapData.append({"name":"Working_Office_Cabinet", "caption":t_("Monica's Office"), "img":"WorkingOfficeCabinet", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"working_office_cabinet", "teleport_type":"function"})
    $ miniMapData.append({"name":"Working_Office", "caption":t_("Employees"), "img":"WorkingOffice", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"working_office", "teleport_type":"function"})
    $ miniMapData.append({"name":"Office_PhotoStudio", "caption":t_("Photo Studiio"), "img":"Office_Monica_PhotoStudio", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_photostudio", "teleport_type":"function"})
    $ miniMapData.append({"name":"Office_Monica_Secretary", "caption":t_("Secretary"), "img":"Office_Monica_Secretary", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_secretary", "teleport_type":"function"})
    $ miniMapData.append({"name":"Office_Entrance", "caption":t_("Entrance"), "img":"Office_Entrance_Monica", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_entrance", "teleport_type":"function"})
    return

label miniMapSlumsApartmentsGenerate:
    if monicaHomeMiniMapEnabled == False:
        return
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Slumps_Apratments_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Slumps_Apratments_Map2"
    $ miniMapData = []
    $ miniMapData.append({"name":"MonicaHome_Bathroom", "caption":t_("ВАННАЯ КОМНАТА"), "img":"MonicaHome_Bathroom_Map", "teleport_scene":"ep211_quests_slums_apartments2_check_enter_minimap_bathroom", "teleport_type":"function"})
    $ miniMapData.append({"name":"MonicaHome_Kitchen", "caption":t_("КУХНЯ"), "img":"MonicaHome_Kitchen_Map", "teleport_scene":"ep211_quests_slums_apartments2_check_enter_minimap_kitchen", "teleport_type":"function"})
    $ miniMapData.append({"name":"MonicaHome_LivingRoom", "caption":t_("СПАЛЬНЯ"), "img":"MonicaHome_LivingRoom_Map", "teleport_scene":"ep211_quests_slums_apartments2_check_enter_minimap_livingroom", "teleport_type":"function"})
    $ miniMapData.append({"name":"MonicaHome_LivingRoomWardrobe", "caption":t_("ГАРДЕРОБ"), "img":"MonicaHome_LivingRoomWardrobe_Map", "teleport_scene":"ep211_quests_slums_apartments2_check_enter_minimap_livingroomwardrobe", "teleport_type":"function"})
    $ miniMapData.append({"name":"MonicaHome_Street", "caption":t_("УЛИЦА"), "img":"MonicaHome_Street_Map", "teleport_scene":"ep211_quests_slums_apartments3_check_exit_minimap", "teleport_type":"function"})
    return

    return

label miniMapJuliaHomeGenerate:
#    if monicaHomeMiniMapEnabled == False or minimapJuliaGenerateEnabled == False:
    if minimapJuliaGenerateEnabled == False:
        return
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_JuliaHome_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_JuliaHome_Map2"
    $ miniMapData = []
    $ miniMapData.append({"name":"JuliaHome_LivingRoom", "caption":t_("СПАЛЬНЯ"), "img":"JuliaHome_LivingRoom_Map", "teleport_scene":"ep213_quests_julia8_minimap_teleport", "teleport_type":"function"})
    $ miniMapData.append({"name":"JuliaHome_Kitchen", "caption":t_("КУХНЯ"), "img":"JuliaHome_Kitchen_Map", "teleport_scene":"ep213_quests_julia8_minimap_teleport", "teleport_type":"function"})
    $ miniMapData.append({"name":"JuliaHome_Bathroom", "caption":t_("ВАННАЯ КОМНАТА"), "img":"JuliaHome_Bathroom_Map", "teleport_scene":"ep213_quests_julia8_minimap_teleport", "teleport_type":"function"})
    $ miniMapData.append({"name":"JuliaHome_Street", "caption":t_("УЛИЦА"), "img":"Street_JuliaHome_Map", "teleport_scene":"ep213_quests_julia8_minimap_teleport", "teleport_type":"function"})
    return



label miniMapDisabled(name, minimapCell):
    sound snd_ui_not_working
    return

label miniMapAddDisabled(name):
    if name not in miniMapDisabled:
        $ miniMapDisabled.append(name)
    return

label miniMapRemoveDisabled(name):
    if name in miniMapDisabled:
        $ miniMapDisabled.remove(name)
    return

label miniMapHouseGenerateTeleport(name, minimapCell):
    $ target_scene_name = minimapCell["teleport_scene"]
    $ target_scene_parent = scene_get_parent(target_scene_name)
    call process_hooks("exit_scene", scene_name) from _call_process_hooks_25
    if _return == False:
        call refresh_scene() from _call_refresh_scene_3
        return
    $ exitHookCalled = True
    call process_hooks("mimimap_teleport", "global") from _call_process_hooks_26 #хук до инициализации сцены
    if _return == False:
        call refresh_scene() from _call_refresh_scene_4
        return
    if interface_blocked_flag == True:
        return
#    $ print renpy.get_screen("say")
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    $ _return = True
    if miniMapSubst.has_key("all") and miniMapSubst["all"] != False:
        call expression miniMapSubst["all"] from _call_expression_9
    if miniMapSubst.has_key(name) and miniMapSubst[name] != False:
        call expression miniMapSubst[name] from _call_expression_10
    if _return != False:
        if minimapCell["teleport_type"] == "function":
            $ minimapTeleportButtonName = name
            call expression minimapCell["teleport_scene"] from _call_expression_11
        if minimapCell["teleport_type"] == "scene":
            call change_scene(minimapCell["teleport_scene"]) from _call_change_scene_150
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
