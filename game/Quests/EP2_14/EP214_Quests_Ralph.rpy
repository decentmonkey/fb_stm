default ep214_stored_cloth = ""
default ep214_stored_cloth_type = ""
default stored_map_objects = False
default ep214_ralph_blowjob_day = 0
default ep214_ralph_last_regular_meeting_day = 0
default ep214_ralph_last_regular_meeting_count = 0
default monica_ralph_relationships_type = 0
label ep214_quests_ralph1:
#    call ep214_dialogues5_bardie_ralph_1() from _rcall_ep214_dialogues5_bardie_ralph_1
    $ add_objective("go_fitness", t_("Поехать с Бетти на фитнес во вторник или четверг."), c_white, 15)
#    $ questHelp("house_34", True)
    $ questHelp("house_35")
    return

label ep214_quests_ralph2:
    # берем одежду Бетти и едем домой
    call ep216_quests_bardie_check_init() from _rcall_ep216_quests_bardie_check_init # инициализируем перехват Барди после уборки
    $ remove_objective("go_fitness")
    call ep214_dialogues5_bardie_ralph_2b() from _rcall_ep214_dialogues5_bardie_ralph_2b
    call ep215_quests_betty_check() from _rcall_ep215_quests_betty_check

    $ ep214_stored_cloth = cloth
    $ ep214_stored_cloth_type = cloth_type
    $ cloth = "BettyCloth"
    $ cloth_type = "BettyCloth"
    $ enter_scene("ep214_dialogues5_bardie_ralph_2c", once=True)
    $ move_object("Bardie", "empty")

    python:
        rooms_list = get_rooms_recursive("House")
        for room_name1 in rooms_list:
            add_hook("Monica", "ep214_dialogues5_bardie_ralph_2b1", scene=room_name1, label="Monica_Ralph_Quest")

    $ map_enabled = False
    $ miniMapEnabledOnly = ["Bedroom", "Bathroom", "Floor1", "Floor2", "Basement", "Laundry"]
    $ add_hook("BasementWardrobe", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom1", label="Monica_Ralph_Quest")
    $ add_hook("Table", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("BasementBed", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box1", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box2", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box3", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box4", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box5", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Box6", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Panties_Box", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Street", "ep214_dialogues5_bardie_ralph_2b1", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_2b1", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Basement_Side", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_hole", label="Monica_Ralph_Quest")
    $ add_hook("ButtPlug", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("Bidet", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_pool", label="Monica_Ralph_Quest")
    $ add_hook("Shower_Cabin", "ep214_dialogues5_bardie_ralph_2b1", scene="basement_pool", label="Monica_Ralph_Quest")
    if monicaBardieRalphSeducingStage == 5:
        $ questHelp("house_35", True)
        $ questHelp("house_36")
        $ move_object("Ralph", "living_room")
        $ add_talk("Ralph", "ep214_quests_ralph6_regular", scene="living_room", label="Monica_Ralph_Quest_regular")
        $ add_talk("Ralph", "ep214_quests_ralph3", scene="living_room", label="Monica_Ralph_Quest")
    if monicaBardieRalphSeducingStage == 6:
        $ move_object("Ralph", "empty")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_2b4", scene="bedroom_bardie", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_Street", "ep214_dialogues5_bardie_ralph_2b3", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_2b2", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_4", scene="floor1", label="Monica_Ralph_Quest", once=True)
        $ add_hook("before_open", "ep214_quests_ralph8_meeting_regular", scene="bedroom2", label="Monica_Ralph_Quest")
        $ add_hook("before_open", "ep214_quests_ralph7_search_ralph", scene="living_room", once=True, label="Monica_Ralph_Quest")


    call change_scene("basement_bedroom1", "Fade_long") from _rcall_change_scene_138

    return

label ep214_quests_ralph3: # первая сцена с Ральфом
    call ep214_dialogues5_bardie_ralph_5() from _rcall_ep214_dialogues5_bardie_ralph_5
    $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_6", scene="floor1", label="Monica_Ralph_Quest", once=True)
    $ add_objective("go_fitness", t_("Вернуться в фитнес зал."), c_orange, 125)
    $ stored_map_objects = map_objects
    $ map_objects = {
            "Teleport_Fitness" : {"text" : t_("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "visible"},
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active"}
    }
    $ char_info["Ralph"]["caption"] = t_("Ральф изменяет Бетти с гувернанткой...")
    $ map_enabled = True
    $ add_hook("before_open", "ep214_quests_ralph4", scene="street_fitness", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Street", "ep214_quests_ralph4", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_LivingRoom", "ep214_dialogues5_bardie_ralph_6a", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_6a", scene="floor1", label="Monica_Ralph_Quest")
    $ add_hook("BasementWardrobe", "ep214_dialogues5_bardie_ralph_6a", scene="basement_bedroom1", label="Monica_Ralph_Quest")
    $ add_hook("Table", "ep214_dialogues5_bardie_ralph_6a", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("BasementBed", "ep214_dialogues5_bardie_ralph_6a", scene="basement_bedroom2", label="Monica_Ralph_Quest")
    $ add_hook("Panties_Box", "ep214_dialogues5_bardie_ralph_6a", scene="basement_laundry", label="Monica_Ralph_Quest")
    $ add_hook("Teleport_Basement_Side", "ep214_quests_ralph4", scene="basement_hole", label="Monica_Ralph_Quest")
    $ ep214_ralph_blowjob_day = day
    $ questHelp("house_36", True)
#    $ questHelp("house_37")
    $ questHelp("house_38")
    call change_scene("floor1", "Fade_long") from _rcall_change_scene_139
    return False

label ep214_quests_ralph4:
    $ remove_objective("go_fitness")
    $ remove_hook(label="Monica_Ralph_Quest")
    $ miniMapEnabledOnly = []
    imgf scene_Map
    sound highheels_run1
    pause 3.0
    call ep214_dialogues5_bardie_ralph_7() from _rcall_ep214_dialogues5_bardie_ralph_7
    $ map_objects = stored_map_objects
    $ stored_map_objects = False
#    $ add_objective("talk_bardie", t_("Поговорить с Барди."), c_blue, 125)
#    $ add_hook("before_open", "ep214_quests_ralph5_bardie", scene="bedroom_bardie", label="Monica_Ralph_Quest")
    $ questHelpDesc("house_desc15", "house_desc16")
    $ monicaBardieRalphSeducingStage = 6
    $ cloth = ep214_stored_cloth
    $ cloth_type = ep214_stored_cloth_type
    sound highheels_short_walk
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    $ map_enabled = False
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_2_[cloth][day_suffix]", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_hook("open", "EP22_Quests_Betty6a", scene="street_fitness")
    $ autorun_to_object("ep22_dialogues4_7a", scene="street_fitness")
    $ ep22_dialogues4_7a_flag1 = False
    call change_scene("street_fitness", "Fade_long", False) from _rcall_change_scene_140
    return False

label ep214_quests_ralph5_bardie: # разговор с Барди
    $ remove_hook()
    call ep214_dialogues5_bardie_ralph_8() from _rcall_ep214_dialogues5_bardie_ralph_8
    $ enter_scene("ep214_dialogues5_bardie_ralph_9", once=True)
    $ remove_objective("talk_bardie")
    $ questLog(72, False)
    $ questLog(79, True)
    $ questHelp("house_37", True)
    $ questHelp("house_38")
    $ questHelp("house_39")
    $ questHelp("house_40")

    $ questHelpDesc("house_desc15", "house_desc16")
    $ questHelpFlag4 = True
#    $ add_objective("go_fitness", t_("Поехать с Бетти на фитнес во вторник или четверг."), c_blue, 125)
    $ monicaBardieRalphSeducingStage = 6
    call change_scene("floor2", "Fade_long") from _rcall_change_scene_141
    return False

label ep214_quests_ralph6_regular: # подход к Ральфу в обычное время
    if cloth == "Governess" and check_hook(label="steve_ralph_visit2", scene="living_room") != True and steveVisit2Day != day:
        call ep214_dialogues5_bardie_ralph_9a() from _rcall_ep214_dialogues5_bardie_ralph_9a
        return False
    return
label ep214_quests_ralph7_search_ralph:
    call ep214_dialogues5_bardie_ralph_10() from _rcall_ep214_dialogues5_bardie_ralph_10
    if ep214_ralph_last_regular_meeting_day == 0:
        $ add_hook("Teleport_Kitchen", "ep214_dialogues5_bardie_ralph_11a", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_11b", scene="basement_bedroom2", label="Monica_Ralph_Quest", once=True)
        $ add_hook("Teleport_Basement_Pool", "ep214_dialogues5_bardie_ralph_11b", scene="floor1_stairs", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_Street", "ep214_dialogues5_bardie_ralph_11c", scene="floor1", label="Monica_Ralph_Quest")
        $ add_hook("Teleport_BedroomBardie", "ep214_dialogues5_bardie_ralph_11d", scene="floor2", label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_11e", scene="bathroom_bath", once=True, label="Monica_Ralph_Quest")
        $ add_hook("enter_scene", "ep214_dialogues5_bardie_ralph_11f", scene="bedroom_second", once=True, label="Monica_Ralph_Quest")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_109
    return
label ep214_quests_ralph8_meeting_regular: # регулярные встречи с Ральфом
    if ep214_ralph_last_regular_meeting_day == 0:
        call ep214_dialogues5_bardie_ralph_12a() from _rcall_ep214_dialogues5_bardie_ralph_12a # первый раз нашла Ральфа

    call ep214_dialogues5_bardie_ralph_12() from _rcall_ep214_dialogues5_bardie_ralph_12
    if ep214_ralph_last_regular_meeting_day == 0:
        $ questLog(79, False)
        call ep214_dialogues5_bardie_ralph_13() from _rcall_ep214_dialogues5_bardie_ralph_13
        if _return == 1:
            $ monica_ralph_relationships_type = 1
            $ questLog(80, True)
            if questHelpFlag4 == True:
                $ questHelpFlag4 = False
                $ questHelp("house_39", True)
                $ questHelp("house_40", False)
                $ questHelp("house_41")
                $ questHelp("house_42")
                $ questHelpDesc("house_desc16", "house_desc17")
        if _return == 2:
            $ monica_ralph_relationships_type = 2
            $ questLog(81, True)
            if questHelpFlag4 == True:
                $ questHelpFlag4 = False
                $ questHelp("house_39", False)
                $ questHelp("house_40", True)
                $ questHelp("house_41")
                $ questHelp("house_42")
                $ questHelpDesc("house_desc16", "house_desc18")
    if ep214_ralph_last_regular_meeting_day > 0 and monica_ralph_relationships_type == 1:
        call ep214_dialogues5_bardie_ralph_13a() from _rcall_ep214_dialogues5_bardie_ralph_13a
    if monica_ralph_relationships_type == 2:
        if char_info["Ralph"]["level"] == 1:
            $ char_info["Ralph"]["enabled"] = True
            $ add_char_progress("Ralph", monicaRalphRegularProgress, "monicaRalphRegularProgress" + str(day))
        if ep214_ralph_last_regular_meeting_day > 0:
            call ep214_dialogues5_bardie_ralph_16() from _rcall_ep214_dialogues5_bardie_ralph_16
    $ ep214_ralph_last_regular_meeting_day = day
    $ ep214_ralph_last_regular_meeting_count += 1
    $ add_hook("enter_scene", "ep214_quests_ralph8_meeting_regular_end", scene="floor2", once=True, label="Monica_Ralph_Quest")
    call change_scene("floor2", "Fade_long") from _rcall_change_scene_142
    return

label ep214_quests_ralph8_meeting_regular_end:
    $ remove_hook(label="Monica_Ralph_Quest")
    if monica_ralph_relationships_type == 1:
        call ep214_dialogues5_bardie_ralph_14() from _rcall_ep214_dialogues5_bardie_ralph_14
    if monica_ralph_relationships_type == 2:
        call ep214_dialogues5_bardie_ralph_15() from _rcall_ep214_dialogues5_bardie_ralph_15

    $ miniMapEnabledOnly = []
    imgf scene_Map
    sound highheels_run1
    pause 3.0
    $ cloth = ep214_stored_cloth
    $ cloth_type = ep214_stored_cloth_type
    sound highheels_short_walk
    img black_screen
    with Dissolve(0.5)
    pause 2.0
    $ map_enabled = False
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_2_[cloth][day_suffix]", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_hook("open", "EP22_Quests_Betty6a", scene="street_fitness")
    $ autorun_to_object("ep22_dialogues4_7a", scene="street_fitness")
    $ ep22_dialogues4_7a_flag1 = False
    call change_scene("street_fitness", "Fade_long", False) from _rcall_change_scene_143
    return False




#
