default bettyCollegeDay1JobFinished = False
default bettyCollegeDay = 0
default bettyCollegeTeacherRefused = False
default bettyCollegeTeacherStage = 0
default bettyCollegeMonicaLesbieInited = False
default ep28_betty_college2_flag = False

default ep28_day_var1 = 0

label ep28_betty_college_init:
    call dialogue_betty_college_0_1() from _call_dialogue_betty_college_0_1
#    $ add_hook("Teleport_BedroomBardie",
    $ add_hook("enter_scene", "dialogue_betty_college_0_1b", scene="floor2", once=True)
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    call change_scene("floor2", "Fade_long") from _call_change_scene_390
    $ questHelp("house_20", True)
    $ questHelp("college_1")
    $ add_hook("change_time_day", "ep28_betty_college2", scene="global", label="ep28_betty_college2", priority=99)
    return

label ep28_betty_college2:
    if monicaRestHouse != True:
        return
    if check_hook("ep24_quests_steve2", scene="global_week_day") == True or check_hook("ep24_quests_steve13", scene="global_week_day") == True:
        return
    if check_scene_parent(scene_name, "House", recursive=True) == False:
        return
    $ remove_hook()
    if ep28_betty_college2_flag == False:
        call dialogue_betty_college_1() from _call_dialogue_betty_college_1 # Барди говорит Бетти что надо идти в колледж
        $ ep28_betty_college2_flag = True
        $ questHelp("college_1", True)
        $ questHelp("college_2")
        $ questHelpDesc("college_desc1")



    # инициализируем колледж

    $ streetCollegeBettySuffix = 1 # Бетти смотрит на школу
    $ set_active("Betty", True, scene="street_college")
    $ set_active("Betty", True, scene="college_class")
    $ add_hook("Betty", "dialogue_betty_college_1_1s", scene="street_college", label="betty_college_common", owner="Betty")
    $ add_hook("Betty", "dialogue_betty_college_1_1s", scene="college_class", label="betty_college_common", owner="Betty")

    $ add_hook("College", "ep28_betty_college2_building", scene="street_college", label=["betty_college_common"], owner="Betty")
    $ add_hook("College", "ep28_betty_college2_building_day1", scene="street_college", label=["betty_college_common", "betty_college_day1"], owner="Betty")

    $ add_hook("Teleport_Street_College", "ep28_betty_college2_class_teleport_back", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Books", "dialogue_betty_college_1_1m", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Desk", "dialogue_betty_college_1_1n", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Formulas", "dialogue_betty_college_1_1r", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_SchoolTables", "dialogue_betty_college_1_1p", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Windows", "dialogue_betty_college_1_1l", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_WorldMap", "dialogue_betty_college_1_1o", scene="college_class", label="betty_college_common", owner="Betty")

    $ add_hook("Teacher", "ep28_betty_college2_teacher", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("Teacher", "ep28_betty_college2_teacher_day1", scene="college_class", label="betty_college_day1", owner="Betty")

    $ add_hook("enter_scene", "dialogue_betty_college_1_1a", scene="street_house_main_yard", once=True, owner="Betty")
    call locations_init_college() from _call_locations_init_college
    call ep28_betty_init() from _call_ep28_betty_init
    $ move_object("Ralph", "living_room")
    $ add_objective("bardie_college", t_("Уладить проблему Барди в колледже"), c_green, 15)
    return

label ep28_betty_college2_building:
    if act=="l":
        call dialogue_betty_college_1_1s() from _call_dialogue_betty_college_1_1s
        return
    call dialogue_betty_college_1_1b() from _call_dialogue_betty_college_1_1b
    return False

label ep28_betty_college2_building_day1:
    if act=="l":
        return
    call change_scene("college_class", "Fade_long", "highheels_run2") from _call_change_scene_391
    return False

label ep28_betty_college2_class_teleport_back:
    $ streetCollegeBettySuffix = 2
    call change_scene("street_college", "Fade_long", "highheels_run2") from _call_change_scene_392
    return

label ep28_betty_college2_teacher:

    if act=="l":
        call dialogue_betty_college_1_1k() from _call_dialogue_betty_college_1_1k
        return
    return


label ep28_betty_college2_teacher_day1: # Сцена учителя с Бетти день 1
    if act=="l":
        call dialogue_betty_college_1_1_2() from _call_dialogue_betty_college_1_1_2
        return False
    $ bettyCollegeDay = 1
    call dialogue_betty_teacher_1() from _call_dialogue_betty_teacher_1
    $ questHelp("college_2", True)
    if _return == True:
        $ bettyCollegeDay1JobFinished = True
        $ bettyCollegeTeacherRefused = False
        $ add_hook("enter_scene", "dialogue_betty_college_1_1_3", scene="street_college", owner="Betty", once=True)
        $ questHelp("college_3")
    else:
        $ bettyCollegeTeacherRefused = True
        $ questHelp("college_3", False)

    $ remove_hook(label="betty_college_day1")

    $ streetCollegeBettySuffix = 2
    call change_scene("street_college", "Fade_long", "highheels_run2") from _call_change_scene_393

    $ move_object("Bardie", "street_house_main_yard")
    $ add_hook("Bardie", "ep28_betty_college2_teacher_day1b", scene="street_house_main_yard", owner="Betty", label="betty_college_day1")
    $ add_hook("Betty", "dialogue_betty_college_1_1i", scene="street_house_main_yard", owner="Betty", label="betty_college_day1")
    $ add_hook("Driver", "dialogue_betty_college_1_1a0", scene="street_house_main_yard", owner="Betty", label="betty_college_day1")

    return False

label ep28_betty_college2_teacher_day1b: # Бетти возвращается из колледжа, говорит с Барди
    if act=="l":
        call dialogue_betty_college_1_1c() from _call_dialogue_betty_college_1_1c
        return False
    if bettyCollegeDay1JobFinished == True:
        call dialogue_betty_college_2() from _call_dialogue_betty_college_2
    else:
        call dialogue_betty_college_2_1() from _call_dialogue_betty_college_2_1
        $ add_hook("change_time_day", "ep28_betty_college2_teacher_day1d", scene="global", label="betty_college_aborted")

    $ remove_hook(label="betty_college_day1")
    $ move_object("Bardie", "empty")
    $ add_hook("enter_scene", "ep28_betty_college2_teacher_day1c", scene="floor1", owner="Betty", once=True)
    call refresh_scene_fade() from _call_refresh_scene_fade_180
    return False

label ep28_betty_college2_teacher_day1_resume: # Возобновляем квест с Бетти после наказания от Барди
    $ add_hook("change_time_day", "ep28_betty_college2", scene="global", label="ep28_betty_college2", priority=99)
    return

label ep28_betty_college2_teacher_day1c: # Бетти заходит в дом (переход управления к Монике)
    if bettyCollegeDay1JobFinished == True:
        call dialogue_betty_college_3() from _call_dialogue_betty_college_3
    $ move_object("Betty", "bedroom1")
    music stop
    img black_screen
    with diss
    pause 1.5
    $ hudDaySkipToEveningEnabled = True
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_394
    $ map_objects["Teleport_College"]["state"] = "visible"

    call change_owner("Monica") from _call_change_owner

    if bettyCollegeDay1JobFinished == True:
        $ add_hook("change_time_day", "ep28_betty_college2_teacher_day2", scene="global", label="betty_college_day2", priority = 99)

    return False

label ep28_betty_college2_teacher_day1d: # Квест остановлен
    if monicaRestHouse != True:
        return
    return


label ep28_betty_college2_teacher_day2: # Инициализация 2-го дня похода к учителю
    if monicaRestHouse != True:
        return
    if check_hook("ep24_quests_steve2", scene="global_week_day") == True or check_hook("ep24_quests_steve13", scene="global_week_day") == True:
        return

    if week_day == 7:
        return
    if check_scene_parent(scene_name, "House", recursive=True) == False: # Проверяем что мы в доме (а не где-то у Маркуса и тд)
        return
    $ remove_hook()

    $ add_hook("enter_scene", "dialogue_betty_college_1_1_4", scene="street_college", once=True, owner="Betty")
    $ add_hook("College", "ep28_betty_college2_building_day1", scene="street_college", label="betty_college_day2", owner="Betty")
    $ add_hook("Teacher", "ep28_betty_college2_teacher_day2_teacher", scene="college_class", label="betty_college_day2", owner="Betty")

    $ move_object("Ralph", "living_room")

    $ streetCollegeBettySuffix = 1

    call change_owner("Betty") from _call_change_owner_1
    $ set_active("Betty", True, scene="House", recursive=True)
    $ set_active("Betty", True, scene="street_college", recursive=True)
    $ hudDaySkipToEveningEnabled = False

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_39
    img black_screen
    with Dissolve(2.0)

    call change_scene("street_house_main_yard") from _call_change_scene_395
    return

label ep28_betty_college2_teacher_day2_teacher: # Разговор с учителем
    if act=="l":
        return
    call dialogue_betty_teacher_2() from _call_dialogue_betty_teacher_2

    $ questHelp("college_3", True)
    $ questHelp("college_4")

    $ bettyCollegeDay = 2

    $ add_hook("enter_scene", "dialogue_betty_college_1_1_5", scene="street_college", owner="Betty", once=True)
    $ remove_hook(label="betty_college_day2")
    $ streetCollegeBettySuffix = 2

    music stop
    img black_screen
    with diss
    pause 2.0
    call change_scene("street_college", "Fade_long", "highheels_run2") from _call_change_scene_396

    $ move_object("Bardie", "street_house_main_yard")
    $ add_hook("Bardie", "ep28_betty_college2_teacher_day2b", scene="street_house_main_yard", owner="Betty", label="betty_college_day2")
    $ add_hook("Betty", "dialogue_betty_college_1_1i", scene="street_house_main_yard", owner="Betty", label="betty_college_day2")
    $ add_hook("Driver", "dialogue_betty_college_1_1a0", scene="street_house_main_yard", owner="Betty", label="betty_college_day2")


    return False

label ep28_betty_college2_teacher_day2b: # Разговор с Барди после сцены 2-го дня
    if act=="l":
        call dialogue_betty_college_1_1c() from _call_dialogue_betty_college_1_1c_1
        return False
    call dialogue_betty_college_4() from _call_dialogue_betty_college_4

    $ remove_hook(label="betty_college_day2")
    $ move_object("Bardie", "empty")
    $ move_object("Betty", "bedroom1")
    music stop
    img black_screen
    with diss
    pause 2.5
    $ hudDaySkipToEveningEnabled = True
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_397
    $ map_objects["Teleport_College"]["state"] = "visible"
    call change_owner("Monica") from _call_change_owner_2
    $ add_hook("change_time_day", "ep28_betty_college2_teacher_day3", scene="global", label="betty_college_day3", priority=99)
    $ ep28_day_var1 = day + 1
    return

#label ep28_betty_college2_teacher_day3a:
#    $ remove_hook()
#    $ add_hook("change_time_day", "ep28_betty_college2_teacher_day3", scene="global", label="betty_college_day3", priority=99)
#    return
label ep28_betty_college2_teacher_day3: # Инициализация дня 3
    if monicaRestHouse != True:
        return
    if week_day == 7 or ep28_day_var1 >= day:
        return
    if check_hook("ep24_quests_steve2", scene="global_week_day") == True or check_hook("ep24_quests_steve13", scene="global_week_day") == True:
        return
    if check_scene_parent(scene_name, "House", recursive=True) == False: # Проверяем что мы в доме (а не где-то у Маркуса и тд)
        return

    $ remove_hook()
    $ add_hook("enter_scene", "dialogue_betty_college_1_1_6", scene="street_college", once=True, owner="Betty")
    $ add_hook("College", "ep28_betty_college2_building_day1", scene="street_college", label="betty_college_day3", owner="Betty")
    $ add_hook("Teacher", "ep28_betty_college2_teacher_day3_teacher", scene="college_class", label="betty_college_day3", owner="Betty")

    $ move_object("Ralph", "living_room")

    $ streetCollegeBettySuffix = 1

    call change_owner("Betty") from _call_change_owner_3
    $ set_active("Betty", True, scene="House", recursive=True)
    $ set_active("Betty", True, scene="street_college", recursive=True)
    $ hudDaySkipToEveningEnabled = False

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_40
    img black_screen
    with Dissolve(2.0)

    call change_scene("street_house_main_yard") from _call_change_scene_398

    return

label ep28_betty_college2_teacher_day3_teacher: # Разговор с учителем день 3
    if act=="l":
        return
    call dialogue_betty_teacher_3() from _call_dialogue_betty_teacher_3
    $ bettyCollegeDay = 3

    $ add_hook("enter_scene", "dialogue_betty_college_1_1_7", scene="street_college", owner="Betty", once=True)
    $ remove_hook(label="betty_college_day3")
    $ streetCollegeBettySuffix = 2

    music stop
    img black_screen
    with diss
    pause 2.0
    call change_scene("street_college", "Fade_long", "highheels_run2") from _call_change_scene_399

    $ move_object("Bardie", "street_house_main_yard")
    $ add_hook("Bardie", "ep28_betty_college2_teacher_day3b", scene="street_house_main_yard", owner="Betty", label="betty_college_day3")
    $ add_hook("Betty", "dialogue_betty_college_1_1i", scene="street_house_main_yard", owner="Betty", label="betty_college_day3")
    $ add_hook("Driver", "dialogue_betty_college_1_1a0", scene="street_house_main_yard", owner="Betty", label="betty_college_day3")

    return False

label ep28_betty_college2_teacher_day3b: # Разговор с Барди день 3
    if act=="l":
        call dialogue_betty_college_1_1c() from _call_dialogue_betty_college_1_1c_2
        return False
    call dialogue_betty_college_5() from _call_dialogue_betty_college_5

    $ questHelp("college_4", True)
    $ questHelp("house_24")
    $ questHelpDesc("college_desc1", "college_desc2")

    music stop
    img black_screen
    with diss
    pause 2.0

#    music stop
#    img black_screen
#    with diss
#    pause 3.0
#    call dialogue_doublephoto_1()

    $ remove_hook(label="betty_college_day3")
    call ep28_betty_house_init_ext1() from _call_ep28_betty_house_init_ext1 # Инициализируем доп. локации в доме
    $ set_active("Betty", True, scene="House", recursive=True)
    $ add_hook("Teleport_BedroomBardie", "ep28_betty_college2_teacher_day3c", scene="floor2", label=["betty_college_day3"], owner="Betty")
    $ move_object("Bardie", "empty")
    $ add_objective("go_to_bardie", t_("Идти к Барди в комнату"), c_orange, 45)
    $ minimapBettyFloor2Enabled = True
    call refresh_scene_fade() from _call_refresh_scene_fade_181
    return

label ep28_betty_college2_teacher_day3c:
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Stairs_Betty[floor2StairsBettySuffix]", "click" : "floor2_stairs_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
    $ remove_objective("go_to_bardie")
    $ move_object("Betty", "bedroom1")
    music stop
    img black_screen
    with diss
    pause 2.0
    call dialogue_betty_college_6() from _call_dialogue_betty_college_6
    music stop
    img black_screen
    with diss
    pause 2.5
    $ questHelp("house_24", True)
    $ hudDaySkipToEveningEnabled = True
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_400
    $ map_objects["Teleport_College"]["state"] = "visible"
    call change_owner("Monica") from _call_change_owner_4
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_401

    $ questHelp("house_25")

    $ bettyCollegeTeacherStage = 1
    call ep28_betty_college_double_photo_init() from _call_ep28_betty_college_double_photo_init
    return False

label ep28_betty_college_double_photo_init:
    $ map_enabled = False
    $ miniMapEnabledOnly = ["Floor2", "Basement"]
    $ move_object("Betty", "bedroom_bardie")
    $ add_hook("enter_scene", "dialogue_doublephoto_1a", scene="basement_bedroom2", once=True, label="double_photo_block")
    $ add_hook("enter_scene", "dialogue_doublephoto_1a", scene="basement_pool", once=True, label="double_photo_block")
    $ add_hook("enter_scene", "dialogue_doublephoto_1a", scene="floor1", once=True, label="double_photo_block")


    $ add_hook("enter_scene", "dialogue_doublephoto_1a", scene="floor2", label="double_photo_block")
#    $ add_hook("Teleport_Floor2_Stairs", "dialogue_doublephoto_1a", scene="floor2", label="double_photo_block")
    $ add_hook("Teleport_Basement_Side", "dialogue_doublephoto_1a", scene="basement_hole", label="double_photo_block")
    $ add_hook("Teleport_Street", "dialogue_doublephoto_1a", scene="floor1", label="double_photo_block")
    $ add_hook("Teleport_Kitchen", "dialogue_doublephoto_1a", scene="floor1", label="double_photo_block")

    $ add_hook("Teleport_BedroomBardie", "ep28_betty_college_double_photo1", scene="floor2", label="double_photo_block")
    $ monicaLastCleaningOfferedDay = day

    return

label ep28_betty_college_double_photo1:
    $ remove_hook(label="double_photo_block")
    $ map_enabled = True
    $ miniMapEnabledOnly = []
    call dialogue_doublephoto_1() from _call_dialogue_doublephoto_1
    $ move_object("Betty", "bedroom1")
#    $ add_hook("change_time_day", "ep28_monica_college_bardie_erick_quest_check", scene="global", label="ep28_monica_college_bardie_erick_quest_check")
#    $ add_hook("enter_scene", "dialogue_classmate_15a", scene="floor2", once=True)
    $ autorun_to_object("dialogue_classmate_15a", scene="floor2")
#    if ep28_monica_bardie_eric_college_inited == False:
#        call ep28_monica_bardie_eric_college_init()

    if ep28_monica_eric_meeting_completed == False:
        call ep28_monica_bardie_eric_meeting_init() from _call_ep28_monica_bardie_eric_meeting_init # Инициализируем знакомство с Эриком вечером

    call refresh_scene_fade() from _call_refresh_scene_fade_182
    return False

label ep28_betty_college_monica_lesbie_init: # Инициализация сцены Бетти и Моники
    if bettyCollegeMonicaLesbieInited == True:
        return

    $ bettyCollegeMonicaLesbieInited = True
    return

#
