default dickDoorBlockedDay = 0
default biffWaitingForMonicaToWork = False
default monicaTalkedSecretary1 = False
default monica_office_cabinet_biff_dialogue3Flag = False
default charityEventCompleted = False

label fred_talk_monica1:
    if monicaRestHouse != True:
        return
    $ add_hook("before_open", "fred_talk_monica1a", scene="street_house_main_yard", label="fred_talk1")
    $ add_hook("map_teleport", "fred_talk_monica1aMap", scene="global", label="fred_talk1")
    $ add_hook_multi("fred_talk_monica1b", scene="street_house_main_yard", filter={"teleport":True})
    $ remove_hook()
    return

label fred_talk_monica1aMap:
    if day_time != "day":
        return
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    call fred_talk_monica1a() from _call_fred_talk_monica1a
    return False

label fred_talk_monica1a:
    if day_time != "day" or cloth != "Whore":
        return
    $ miniMapEnabledOnly = ["none"]
    $ map_enabled = False
#    $ cloth = "Whore"
#    $ cloth_type = "Whore"

    $ add_hook("Driver", "fred_talk_monica1c", scene="street_house_main_yard", label="fred_talk1a")

    $ map_source_scene = "street_house_main_yard"
    $ autorun_to_object("fred_talk_monica1b", scene="street_house_main_yard")
    return

label fred_talk_monica1b:
    if day_time != "day" or cloth != "Whore":
        return
    call monica_fred_about_dick_dialogue1() from _call_monica_fred_about_dick_dialogue1
    return False

label fred_talk_monica1c:
    if act == "l":
        return
    $ miniMapEnabledOnly = []
    $ map_enabled = True
    $ remove_hook(label="fred_talk1")
    $ remove_hook("fred_talk_monica1b")
    $ replace_hook("Driver", "fred_talk_monica1c", "fred_talk_monica1d")
    call ep2_open_dick1() from _call_ep2_open_dick1
    call fred_talk_monica1d() from _call_fred_talk_monica1d
    return _return

label fred_talk_monica1d:
    call monica_fred_about_dick_dialogue2() from _call_monica_fred_about_dick_dialogue2
    $ add_objective("go_dick", t_("Отправиться на встречу с Диком"), c_green, 30)
    call refresh_scene_fade() from _call_refresh_scene_fade
    return False

label ep2_open_dick1:
    $ move_object("DickTheLawyer", "dick_office_cabinet")
    $ add_hook("DickSecretary", "dick_secretary_talk1", scene="dick_office_secretary", label="secretary1")
    $ add_hook("Door", "dick_secretary_talk1", scene="dick_office_secretary", label="secretary1")
    return

label dick_secretary_talk1:
    $ remove_hook(label="fred_talk1a")
    if act == "l":
        return
    if obj_name == "DickSecretary":
        call monica_dick_secretary_dialogue1() from _call_monica_dick_secretary_dialogue1
        $ monicaTalkedSecretary1 = True
    else:
        if monicaTalkedSecretary1 == False:
            call monica_dick_secretary_dialogue1() from _call_monica_dick_secretary_dialogue1_1
            $ monicaTalkedSecretary1 = True
        call monica_dick_secretary_dialogue1a() from _call_monica_dick_secretary_dialogue1a
        $ remove_hook("Door", "dick_secretary_talk1")
        $ add_hook("enter_scene", "dick_the_lawyer_enter1", scene="dick_office_cabinet")
        $ add_hook("DickTheLawyer", "dick_the_lawyer_talk1", scene="dick_office_cabinet")

    return

label dick_the_lawyer_enter1:
    $ remove_objective("go_dick")
    $ remove_hook()
    call monica_dick_dialogue1a() from _call_monica_dick_dialogue1a

    return

label dick_the_lawyer_talk1:
    if act == "l":
        return
    call monica_dick_dialogue1() from _call_monica_dick_dialogue1
    $ questHelp("dick_1", True)
    $ questHelp("dick_1a")
    $ dickDoorBlockedDay = day
    $ add_hook("Door", "monica_dick_secretary_dialogue4a", scene="dick_office_secretary", label="dick_blocked")
    $ replace_hook("dick_secretary_talk2", scene="dick_office_secretary", label="secretary1")
    $ add_hook("Teleport_Hall", "monica_dick_secretary_dialogue2a", scene="dick_office_secretary", label="secretary1")
    $ autorun_to_object("monica_dick_secretary_dialogue2a", scene="dick_office_secretary")
    $ autorun_to_object("monica_dick_office_dialogue2", scene="street_dick_office")
    $ nextFriday = getNextDayByWeekDay(5)
#    $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday, evening=True)
    $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday)
    $ remove_hook(label="biff_refuse1") # очищаем дорогу к Бифу
    $ add_hook("Secretary", "monica_office_secretary_talk_before_work_request", scene="monica_office_secretary", label="monica_secretary2")
    $ add_hook_multi("monica_office_secretary_talk_before_work_request", scene="monica_office_secretary", filter={"teleport":True}, label="monica_secretary2_teleport", priority=160)
    $ add_hook("Biff", "monica_office_biff_talk_about_work1", scene="monica_office_cabinet_table", label="biff2")
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_cabinet_biff_dialogue2a", scene="monica_office_secretary", priority=120)
    call change_scene("dick_office_secretary") from _call_change_scene_19
    return

label dick_secretary_talk2:
    if act == "l":
        return
    call monica_dick_secretary_dialogue2() from _call_monica_dick_secretary_dialogue2
    $ add_objective("dicksecretary_find_money", t_("Принести Виктории $ 5000 до вечера пятницы"), c_red, 30)
    $ questLog(10, True)
    $ questHelp("dick_1a", True)
    $ questHelp("office_3")
    $ questHelpDesc("dick_desc1", "dick_desc2")
    $ add_char_progress("DickSecretary", 20, "dick_secretary_talk2")
    $ remove_hook(label="secretary1")
    $ add_hook("DickSecretary", "dick_secretary_talk3", scene="dick_office_secretary")
    return

label dick_secretary_talk3: #регулярный
    if act == "l":
        return
    call monica_dick_secretary_dialogue3() from _call_monica_dick_secretary_dialogue3
    return False


label dick_secretary_time_to_pay1:
#    if biffWaitingForMonicaToWork == False:
#        "но пока не надо!"
#        $ nextFriday = getNextDayByWeekDay(5)
#        $ remove_hook()
#        $ add_hook_day("dick_secretary_time_to_pay1", day = nextFriday, evening=True)
#        return
    $ add_hook("Teleport_Inside", "monica_dick_office_refuse_dialogue1", scene="street_dick_office", label="dick_blocked")
    $ add_hook("BasementBed", "basement_bed_hook", scene="basement_bedroom2")
    $ add_hook("basement_monica_before_sleep", "dick_secretary_time_to_pay2", scene="global")
    $ add_hook("basement_monica_after_sleep_dialogue", "dick_secretary_time_to_pay1a", scene="global")
    $ remove_hook()
    return
label dick_secretary_time_to_pay1a:
    mt "Сегодня пятница. Мне надо {c}найти $ 5000 до вечера{/c}!"
    "Тогда Дик убедится в моей лояльности и вытащит меня из этой ситуации, в которую я попала!"
    $ remove_hook()
    return
label dick_secretary_time_to_pay2:
    mt "Я не могу идти спать. Я должна {c}принести сегодня $ 5000 Дику{/c}!"
    return False

label monica_office_secretary_talk_before_work_request:
    if obj_name == "Secretary" and act == "l":
        return
    call monica_office_secretary_dialogue3() from _call_monica_office_secretary_dialogue3
    $ remove_hook(label="monica_secretary2_teleport")
    return False

label monica_office_biff_talk_about_work1: #Моника разговаривает с Бифом второй раз, уже о работе.
    if act == "l":
        return
    call monica_office_cabinet_biff_dialogue3() from _call_monica_office_cabinet_biff_dialogue3
    $ monicaOfficeSecretaryMonicaSuffix_forced = ""
    if _return == False:
        return False
    $ questHelp("office_3", True)
    $ questHelp("office_4")
    $ questHelpDesc("office_desc2", "office_desc3")
    $ questLog(9, True)
    call change_scene("monica_office_secretary") from _call_change_scene_20
    $ autorun_to_object("monica_office_secretary_dialogue5", scene="monica_office_secretary")
    if nextFriday != day:
        $ biffOnlyFridayEvening = True
        $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_cabinet_biff_dialogue2", scene="monica_office_secretary", label="biff_refuse1") # Если не пятница, то блокируем Бифа на сегодня
        $ add_hook("enter_scene", "monica_office_secretary_dialogue5a", scene="monica_office_secretary", label="biff_comment1") #При входе в офис Моника думает все-же согласиться на фотосессию
        $ add_hook("change_time_day", "monica_office_biff_talk_about_work1_next_day", scene="global")
    $ remove_hook(label="monica_secretary2")
    if nextFriday == day: # уже пятница, активируем
        $ replace_hook("monica_office_biff_talk_about_work2", scene="monica_office_cabinet_table", label="biff2") # Разговариваем с Бифом в 3-ий раз, соглашаясь на обнажение постепенно

#    $ biffOnlyFridayEvening = True # Бифф будет только в пятницу вечером
    return False

label monica_office_biff_talk_about_work1_next_day: # Если вчера была не пятница, то вешаем хуки об отсутствии Бифа до пятницы (хрень какая-то, так и есть :) )
    $ remove_hook()
    $ remove_hook(label="biff_refuse1")
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4", scene="monica_office_secretary", label="biff_refuse1", priority=160)
#    $ remove_hook(label="biff_refuse1")
    $ replace_hook("monica_office_biff_talk_about_work2", scene="monica_office_cabinet_table", label="biff2")  # Разговариваем с Бифом в 3-ий раз, соглашаясь на обнажение постепенно

    return

label monica_office_biff_talk_about_work2: #Моника разговаривает с Бифом третий раз.
    if act == "l":
        return
    call monica_office_cabinet_biff_dialogue4() from _call_monica_office_cabinet_biff_dialogue4
    if _return == False:
        return False
    $ questHelp("photoshoot_1")
    $ questHelpDesc("photoshoot_desc1")
    $ remove_hook(label="biff_comment1")
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshot_exit_refuse")
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshot_exit_refuse")
    $ add_hook("AlexPhotograph", "monica_office_photoshot1", scene="monica_office_photostudio")
    $ remove_hook()
    call change_scene("monica_office_secretary") from _call_change_scene_21
    return False

label monica_office_photoshot1:
    if act == "l":
        return
    call monica_office_photostudio_alex_dialogue2() from _call_monica_office_photostudio_alex_dialogue2
    call refresh_scene_fade() from _call_refresh_scene_fade_1
    if _return == False:
        return False
    $ cloth_type = "PhotoDress"
    $ cloth = "PhotoDress"
    $ remove_hook()
    $ remove_hook(label="photoshot_exit_refuse")

    $ add_hook("AlexPhotograph", "monica_office_dialogue9", scene="monica_office_photostudio", label="after_photoshot")
    $ add_hook("Secretary", "monica_office_secretary_dialogue7", scene="monica_office_secretary", label="after_photoshot") # Комментарий Моники в платье
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_dialogue9", scene="monica_office_secretary", label="after_photoshot")
    $ add_hook("Biff", "monica_office_photoshot1_biff_talk1", scene="monica_office_cabinet_table", label="biff3")
    $ questHelp("office_5")
    $ questHelp("photoshoot_1", True)
    $ questHelpDesc("photoshoot_desc1", "photoshoot_desc8a")
    $ questHelp("photoshoot_8a")
    return False

label monica_office_photoshot1_biff_talk1:
    if act=="l":
        return
#    call monica_charity_event1() #debug!!
#    return

    call monica_office_cabinet_biff_dialogue5() from _call_monica_office_cabinet_biff_dialogue5
    $ remove_hook()
    $ remove_hook(label="after_photoshot")

    $ questHelp("office_6")
    $ questHelp("office_7")
    $ questHelp("office_7b")
    $ questHelpDesc("office_desc3", "office_desc4")


    # идем на эвент
    call monica_charity_event1() from _call_monica_charity_event1
    return False

label monica_charity_event1:
    # Charity Event
    $ move_object("Philip", "rich_hotel_event_hall")
    $ add_hook("Philip", "monica_charity_event_philip_talk1", scene="rich_hotel_event_hall")
    $ move_object("HotelStaff", "rich_hotel_event_hall")
    $ add_hook("HotelStaff", "monica_charity_event_hotelstaff_talk1", scene="rich_hotel_event_hall")
    $ move_object("Melanie", "rich_hotel_event_scene")
    $ move_object("Biff", "rich_hotel_event_scene")
#    $ map_enabled = False
    $ questHelp("office_5", True)
    call monica_rich_hotel_event_drive() from _call_monica_rich_hotel_event_drive
    call monica_rich_hotel_entrance() from _call_monica_rich_hotel_entrance
    call monica_charity_event_dialogue1() from _call_monica_charity_event_dialogue1
    music stop
    sound Piano_Between
    call monica_charity_event_dialogue2() from _call_monica_charity_event_dialogue2

    $ add_hook("Monica", "monica_charity_event_talk1", scene="rich_hotel_event_scene")
    call change_scene("rich_hotel_event_scene", "Fade_long", False) from _call_change_scene_23
    return

label monica_charity_event_talk1:
    call monica_charity_event_dialogue2a() from _call_monica_charity_event_dialogue2a
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_2
        return False

    $ questHelp("office_6", True)
    $ questHelp("office_7", True)
    $ questHelp("office_8")

    $ add_hook("Teleport_Rich_Hotel_Reception", "monica_charity_event_dialogue4a", scene="rich_hotel_event_hall")
    $ set_active("Teleport_Rich_Hotel_Tables", False, scene="rich_hotel_event_hall")
    $ move_object("Philip", "empty")
    $ move_object("Biff", "rich_hotel_event_sofa")
    $ move_object("Melanie", "rich_hotel_event_sofa")
    $ add_hook("HotelStaff", "monica_charity_event_hotelstaff_talk1", scene="rich_hotel_event_hall")
    $ add_hook("Biff", "monica_charity_event_biff_talk1", scene="rich_hotel_event_sofa", label="biff4")
    $ autorun_to_object("monica_charity_event_dialogue3", scene="rich_hotel_event_hall")
    music Backbay_Lounge
    call change_scene("rich_hotel_event_hall", "Fade_long", False) from _call_change_scene_24
    return


label monica_charity_event_hotelstaff_talk1: #наезд вначале
    if act == "l":
        return
    call monica_charity_event_dialogue6() from _call_monica_charity_event_dialogue6
    $ questHelpFlag10 = True
    $ questHelp("office_7b", True)

    $ replace_hook("HotelStaff", "monica_charity_event_hotelstaff_talk1", "monica_charity_event_hotelstaff_talk2", scene="rich_hotel_event_hall")
    call refresh_scene_fade() from _call_refresh_scene_fade_3
    return
label monica_charity_event_hotelstaff_talk2: #регулярно
    if act == "l":
        return
    call monica_charity_event_dialogue7() from _call_monica_charity_event_dialogue7
    call refresh_scene_fade() from _call_refresh_scene_fade_4
    return False

label monica_charity_event_biff_talk1:
    if act == "l":
        return
    call monica_charity_event_dialogue4() from _call_monica_charity_event_dialogue4
    $ replace_hook("monica_charity_event_biff_talk2", label="biff4")
    $ move_object("Philip", "rich_hotel_event_hall")
    $ add_hook("Philip", "monica_charity_event_philip_talk1", scene="rich_hotel_event_hall")
    return
label monica_charity_event_biff_talk2:
    if act == "l":
        return
    call monica_charity_event_dialogue5() from _call_monica_charity_event_dialogue5
    return

label monica_charity_event_biff_talk3:
    if act == "l":
        return
    call monica_charity_event_dialogue10() from _call_monica_charity_event_dialogue10

    $ questHelp("office_5", True)
    $ questHelp("office_8", True)
    $ questHelp("office_9")
    $ questHelpDesc("office_desc4", "office_desc5")
    $ questHelp("philip_1")
    $ questHelp("office_10")
    $ questHelpDesc("philip_desc1")

    $ remove_hook()
    $ richHotelEventStage = 1
    $ questLog(10, False)
    $ questLog(11, True)
    $ remove_hook("Teleport_Rich_Hotel_Tables", "monica_charity_event_dialogue9", scene="rich_hotel_event_hall")
    $ set_active("Teleport_Rich_Hotel_Tables", False, scene="rich_hotel_event_hall")
    $ move_object("Philip", "rich_hotel_event_hall")
    $ add_hook("Philip", "monica_charity_event_philip_talk3", scene="rich_hotel_event_hall")
#    music Stealth_Groover
    music Pyro_Flow
#    music Malicious
    $ set_var("Monica", base="Rich_Hotel_Event_Hall_Monica2_[cloth]", scene="rich_hotel_event_hall")
    $ replace_hook("Teleport_Rich_Hotel_Reception", "monica_charity_event_dialogue4a", "monica_charity_event_dialogue12a", scene="rich_hotel_event_hall")
    $ add_hook("Teleport_Rich_Hotel_Sofa", "monica_charity_event_dialogue12", scene="rich_hotel_event_hall", label="block_teleport1")
    $ autorun_to_object("monica_charity_event_dialogue11", scene="rich_hotel_event_hall")
    call change_scene("rich_hotel_event_hall") from _call_change_scene_25
    return

label monica_charity_event_biff_talk4: #я буду хорошей цыпочкой
    if act == "l":
        return
    call monica_charity_event_dialogue16() from _call_monica_charity_event_dialogue16
    $ questHelp("office_11")
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_5
        return False
    # уезжают в офис
    $ questHelp("office_11", True)
    $ questHelp("office_9", True)
    $ questHelp("office_10", True)
    $ questHelp("philip_1", False)
    $ questHelp("philip_2", False)
    $ questHelp("office_12")
    $ questHelpDesc("dick_desc2", "dick_desc3")
    if questHelpFlag10 == False:
        $ questHelp("office_7b", False)
    $ add_money(1000)
    call monica_after_charity_event() from _call_monica_after_charity_event
    return False

label monica_charity_event_melanie_talk1:
    return

label monica_charity_event_philip_talk1:
    if act == "l":
        return
    call monica_charity_event_dialogue8() from _call_monica_charity_event_dialogue8
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_6
        return False
    $ remove_hook()
    $ move_object("Philip", "rich_hotel_event_sittable")
    $ add_hook("Philip", "monica_charity_event_philip_talk2", scene="rich_hotel_event_sittable")
    music Lobby_Time
    call change_scene("rich_hotel_event_sittable", "Fade_long", False) from _call_change_scene_26
    return

label monica_charity_event_philip_talk2:
    if act == "l":
        return
    $ remove_hook()
    call monica_charity_event_dialogue8a() from _call_monica_charity_event_dialogue8a
    $ move_object("Philip", "rich_hotel_event_tables")
    $ set_active("Teleport_Rich_Hotel_Tables", True, scene="rich_hotel_event_hall")
    $ add_hook("Teleport_Rich_Hotel_Tables", "monica_charity_event_dialogue9", scene="rich_hotel_event_hall")
    $ replace_hook("monica_charity_event_biff_talk3", label="biff4", scene="rich_hotel_event_sofa")
    $ autorun_to_object("monica_charity_event_dialogue9", scene="rich_hotel_event_hall")
    call change_scene("rich_hotel_event_hall") from _call_change_scene_28
    return

label monica_charity_event_philip_talk3:
    if act == "l":
        return
    call monica_charity_event_dialogue14() from _call_monica_charity_event_dialogue14
    if _return == False:
        music Backbay_Lounge
        call refresh_scene_fade() from _call_refresh_scene_fade_7
        return False

    $ questHelp("philip_1", True)
    $ questHelp("philip_2")
    music Malicious
    $ remove_hook()
    $ set_active("Teleport_Rich_Hotel_Tables", True, scene="rich_hotel_event_hall")
    $ move_object("Philip", "rich_hotel_event_tables")
    $ add_hook("Philip", "monica_charity_event_philip_talk4", scene="rich_hotel_event_tables")
    $ autorun_to_object("monica_charity_event_dialogue15", scene="rich_hotel_event_hall")
    $ remove_hook(label="block_teleport1")
    $ add_hook("Biff", "monica_charity_event_biff_talk4", scene="rich_hotel_event_sofa")
    call refresh_scene_fade() from _call_refresh_scene_fade_8
    return

label monica_charity_event_philip_talk4: #танец с согласием на миньет
    if act == "l":
        return
    call monica_charity_event_dialogue17() from _call_monica_charity_event_dialogue17
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_9
        return False
    $ remove_hook()
#    $ hotelStaffOffended1 = False
    call monica_charity_event_dialogue18() from _call_monica_charity_event_dialogue18 #сцена blowjob
    $ move_object("Philip", "empty")
    $ move_object("HotelStaff", "empty")
    $ set_active("Teleport_Rich_Hotel_Tables", False, scene="rich_hotel_event_hall")
    if _return == False:
        call change_scene("rich_hotel_event_hall") from _call_change_scene_29
        return False
    call monica_charity_event_dialogue19() from _call_monica_charity_event_dialogue19
    music stop
    call monica_after_charity_event() from _call_monica_after_charity_event_1

    $ questHelp("philip_2", True)
    $ questHelpDesc("philip_desc1", "philip_desc2")
    $ questHelpDesc("dick_desc2", "dick_desc3")
    $ questHelp("office_12")


    $ questHelp("office_11", False)
    $ questHelp("office_9", True)
    $ questHelp("office_10", False)
    if questHelpFlag10 == False:
        $ questHelp("office_7b", False)
    return False
#    $ add_char_progress("Biff", 20, "photoshot1")


label monica_after_charity_event:
    $ move_object("Melanie", "empty")
    $ move_object("Biff", "monica_office_cabinet")
    call monica_rich_hotel_event_drive_back() from _call_monica_rich_hotel_event_drive_back
    call monica_office_biff_dialogue_evening1() from _call_monica_office_biff_dialogue_evening1
    $ questLog(11, False)
    $ questHelp("office_4", True)
    $ autorun_to_object("monica_office_dialogue1", scene="street_monica_office")
    $ add_hook("Teleport_Inside", "monica_office_dialogue1", scene="street_monica_office", label="block_monica_office")
    $ add_hook("Teleport_Inside", "monica_after_charity_event_dick_entrance_talk1", scene="dick_office_entrance", label="dick_office_entrance")
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    $ rain = True
    $ rainIntencity = 3
    $ lightning = True
    $ remove_hook(label="dick_blocked")
    $ move_object("DickTheLawyer", "empty")
    $ focus_map("Teleport_Dick_Office", "monica_after_charity_event_go_dick")
    $ charityEventCompleted = True
    call monicaEat() from _call_monicaEat_6
#    $ map_enabled = True
    call change_scene("street_monica_office", "Fade_long") from _call_change_scene_30
    return

label monica_after_charity_event_dick_entrance_talk1:
    $ remove_hook()
    call monica_dick_office_entrance_dialogue1() from _call_monica_dick_office_entrance_dialogue1

    $ questHelp("office_12", True)
    $ questHelp("dick_2")
    $ questHelpDesc("office_desc5", "office_desc6")
    $ remove_objective("dicksecretary_find_money")
    $ add_objective("dick_money_tomorrow", t_("Принести деньги Дику завтра"), c_blue, 40)
    $ unfocus_map()
    $ move_object("Biff", "empty")
    $ move_object("AlexPhotograph", "empty")
    $ remove_hook(label="block_monica_office")
    $ remove_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4", scene="monica_office_secretary")
    $ add_hook("enter_scene", "monica_after_charity_event_return_home", scene="basement_bedroom2")
    $ add_hook("before_open", "monica_after_charity_event_return_home1", scene="street_house_main_yard")
    $ dickReceptionMonicaSuffix = 3
    call refresh_scene_fade() from _call_refresh_scene_fade_10
    return False

label monica_after_charity_event_go_dick:
    call monica_office_dialogue1() from _call_monica_office_dialogue1
    return

label monica_after_charity_event_return_home:
#    $ monicaCantSleepHungry = False
    $ dickReceptionMonicaSuffix = 1
    music Continue_Life high
    $ remove_hook()
    $ remove_hook("basement_monica_before_sleep", "dick_secretary_time_to_pay2", scene="global")
    $ add_hook("basement_monica_before_sleep", "monica_after_charity_event_home_sleep", scene="global")
    return
label monica_after_charity_event_return_home1:
    $ remove_hook()
    $ rainIntencity = 1
    $ lightning = False
    return

label monica_after_charity_event_home_sleep:
    call monica_basement_bedroom_before_sleep1() from _call_monica_basement_bedroom_before_sleep1
    return
