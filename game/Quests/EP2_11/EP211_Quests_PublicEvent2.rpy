default questsPublicEvent2Stage = 0
default questsPublicEvent2StageDay = -1

default ep211_quests_publicevent2_2_flag = False
default ep211_quests_publicevent2_3_guest1_flag = False
default ep211_quests_publicevent2_3_guest2_flag = False
default ep211_quests_publicevent2_3_guest3_flag = False
default ep211_quests_publicevent2_3_guest4_flag = False
default ep211_quests_publicevent2_3_guest56_flag = False
default ep211_quests_publicevent2_3_guest_girlfriends_stage = 0
default ep211_quests_publicevent2_3_guest8_flag = False
default ep211_quests_guests_progress = []
default ep211_quests_guests_progress_cur = 0

default ep211_quests_photoshoot_stage = 0

default ep211_quests_publicevent2_completed = False
default ep211_quests_photoshot8_opened_day = 0

default monicaOfficeFiredType1 = False

# Первый разговор в втором паблик евенте
label ep211_quests_publicevent2_1:
    call ep211_dialogues2_public_event_1() from _rcall_ep211_dialogues2_public_event_1
    if _return == False:
        $ autorun_to_object("ep211_dialogues2_public_event_41", scene="monica_office_cabinet")
        return False

    $ questHelp("office_35", True)
    $ questHelp("office_36")
    $ questHelpDesc("office_desc10", "office_desc11")

    $ add_hook("Biff", "ep211_quests_publicevent2_2", scene="monica_office_cabinet_table", label="public_event2") # Разговор с Бифом на следующий день
    $ questsPublicEvent2Stage = 1
    $ questsPublicEvent2StageDay = day
    $ questLog(67, True)
    $ autorun_to_object("ep211_dialogues2_public_event_41", scene="monica_office_secretary")
    call change_scene("monica_office_secretary", "Fade_long") from _rcall_change_scene_18
    return False

label ep211_quests_publicevent2_2: # второй день
    if act=="l":
        return
    if day == questsPublicEvent2StageDay:
        call ep211_dialogues2_public_event_2() from _rcall_ep211_dialogues2_public_event_2 # вернулась в тот же день
        return False
    # следующий день
    call ep211_dialogues2_public_event_3() from _rcall_ep211_dialogues2_public_event_3
    if ep211_quests_publicevent2_2_flag == True:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_11
        return False
    $ miniMapEnabledOnly = ["Office_Biff_Cabinet", "Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("Teleport_Monica_Office_Entrance", "ep211_dialogues2_public_event_4", scene="monica_office_secretary", label="public_event2_block")
    $ add_hook("AlexPhotograph", "ep211_quests_publicevent2_3_alex", scene="monica_office_photostudio", label="public_event2")
    $ move_object("Melanie", "empty")
    $ add_objective("get_dress", t_("Переодеться в вечернее платье."), c_orange, 95)
    $ ep211_quests_publicevent2_2_flag = True
    call refresh_scene_fade() from _rcall_refresh_scene_fade_12

    return False

label ep211_quests_publicevent2_3_alex:
    if act=="l":
        return
    $ remove_objective("get_dress")
    $ remove_hook()
    $ remove_hook(label="public_event2_block")
    $ remove_hook(label="public_event2")
    call ep211_dialogues2_public_event_5() from _rcall_ep211_dialogues2_public_event_5
    call ep211_dialogues2_public_event_6() from _rcall_ep211_dialogues2_public_event_6
    call ep211_dialogues2_public_event_7() from _rcall_ep211_dialogues2_public_event_7
    call locations_init_public_event2() from _rcall_locations_init_public_event2
    $ questHelp("office_36", True)
    $ questHelp("office_37")
    $ questHelp("office_38")
    $ set_active("Investor1", False, scene="public_event2")
    $ set_active("PublicGuest7", False, scene="public_event2")
    $ set_active("PublicGuest8", False, scene="public_event2")
    $ renpy.music.set_volume(0.3, 0.0, 'music2')
    $ add_hook("FitnessRebecca", "ep211_quests_publicevent2_3_guest_girlfriends", scene="public_event2", label="public_event2")
    $ add_hook("FitnessStephanie", "ep211_quests_publicevent2_3_guest_girlfriends", scene="public_event2", label="public_event2")
    $ add_hook("Investor1", "ep211_quests_publicevent2_3_investor1", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest1", "ep211_quests_publicevent2_3_guest1", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest2", "ep211_quests_publicevent2_3_guest2", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest3", "ep211_quests_publicevent2_3_guest3", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest4", "ep211_quests_publicevent2_3_guest4", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest5", "ep211_quests_publicevent2_3_guest56", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest6", "ep211_quests_publicevent2_3_guest56", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest7", "ep211_quests_publicevent2_3_guest7", scene="public_event2", label="public_event2")
    $ add_hook("PublicGuest8", "ep211_quests_publicevent2_3_guest8", scene="public_event2", label="public_event2")
    $ ep211_quests_guests_progress = ["PublicGuest1", "PublicGuest2", "PublicGuest3", "PublicGuest4", "PublicGuest5", "PublicGuest6", "PublicGuest7", "PublicGuest8", "Girlfriends"]
    call change_scene("public_event2", "Fade_long") from _rcall_change_scene_19
    $ add_objective("talk_people", t_("Пообщаться с гостями ([ep211_quests_guests_progress_cur]/9)."), c_orange, 95)
    return False

label ep211_quests_publicevent2_3_checkquesthelp:
    if ep211_quests_publicevent2_3_guest1_flag == True and ep211_quests_publicevent2_3_guest2_flag == True and ep211_quests_publicevent2_3_guest3_flag == True and ep211_quests_publicevent2_3_guest4_flag == True and ep211_quests_publicevent2_3_guest56_flag == True:
        $ questHelp("office_37", True)
    return

label ep211_quests_publicevent2_3_guest1:
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest1_flag == False:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_9() from _rcall_ep211_dialogues2_public_event_9
        $ autorun_to_object("ep211_dialogues2_public_event_9b", scene="public_event2")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_13
        $ ep211_quests_publicevent2_3_guest1_flag = True
        if "PublicGuest1" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest1")
        call ep211_quests_publicevent2_3_checkquesthelp()
        call refresh_scene_fade() from _rcall_refresh_scene_fade_14
        return False
    call ep211_dialogues2_public_event_10() from _rcall_ep211_dialogues2_public_event_10
    return False

label ep211_quests_publicevent2_3_guest2:
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest2_flag == False:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_12() from _rcall_ep211_dialogues2_public_event_12
        $ autorun_to_object("ep211_dialogues2_public_event_12b", scene="public_event2")
        $ ep211_quests_publicevent2_3_guest2_flag = True
        if "PublicGuest2" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest2")
        call ep211_quests_publicevent2_3_checkquesthelp()
        call refresh_scene_fade() from _rcall_refresh_scene_fade_15
        return False
    call ep211_dialogues2_public_event_13() from _rcall_ep211_dialogues2_public_event_13
    return False

label ep211_quests_publicevent2_3_guest3:
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest3_flag == False:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_15() from _rcall_ep211_dialogues2_public_event_15
        $ ep211_quests_publicevent2_3_guest3_flag = True
        if "PublicGuest3" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest3")
        $ autorun_to_object("ep211_dialogues2_public_event_15b", scene="public_event2")
        call ep211_quests_publicevent2_3_checkquesthelp()
        call refresh_scene_fade() from _rcall_refresh_scene_fade_16
        return False
    call ep211_dialogues2_public_event_16() from _rcall_ep211_dialogues2_public_event_16
    return False

label ep211_quests_publicevent2_3_guest4:
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest4_flag == False:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_18() from _rcall_ep211_dialogues2_public_event_18
        $ ep211_quests_publicevent2_3_guest4_flag = True
        if "PublicGuest4" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest4")
        $ autorun_to_object("ep211_dialogues2_public_event_18b", scene="public_event2")
        call ep211_quests_publicevent2_3_checkquesthelp()
        call refresh_scene_fade() from _rcall_refresh_scene_fade_17
        return False
    call ep211_dialogues2_public_event_19() from _rcall_ep211_dialogues2_public_event_19
    return False

label ep211_quests_publicevent2_3_guest56:
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest56_flag == False:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_21() from _rcall_ep211_dialogues2_public_event_21
        $ ep211_quests_publicevent2_3_guest56_flag = True
        call ep211_dialogues2_public_event_23() from _rcall_ep211_dialogues2_public_event_23 # интервью прессе
        $ questHelp("office_38", skipIfExists=True)

        if "PublicGuest5" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest5")
        if "PublicGuest6" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest6")
        call ep211_quests_publicevent2_3_checkquesthelp()
        $ autorun_to_object("ep211_dialogues2_public_event_21b", scene="public_event2")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_18
        return False
    call ep211_dialogues2_public_event_22() from _rcall_ep211_dialogues2_public_event_22
    return False

label ep211_quests_publicevent2_3_guest7:
    if act=="l":
        return
    hide screen Reporters_Shoots_Screen4_low
    music2 stop
    call ep211_dialogues2_public_event_33() from _rcall_ep211_dialogues2_public_event_33
    $ questHelp("office_40", True)
    $ questHelp("office_41", skipIfExists=True)
    $ set_active("PublicGuest7", False)
    if "PublicGuest7" in ep211_quests_guests_progress:
        $ ep211_quests_guests_progress.remove("PublicGuest7")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_19
    return False

label ep211_quests_publicevent2_3_guest_girlfriends:
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest_girlfriends_stage == 0:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_25() from _rcall_ep211_dialogues2_public_event_25
        $ questHelp("office_38", True)
        $ questHelp("office_39", skipIfExists=True)
        $ ep211_quests_publicevent2_3_guest_girlfriends_stage = 1
        $ set_active("PublicGuest8", True)
        $ add_objective("talk_terner", t_("Поговорить с Тернером."), c_blue, 105)
        call refresh_scene_fade() from _rcall_refresh_scene_fade_20
        return False
    if ep211_quests_publicevent2_3_guest_girlfriends_stage == 1:
        call ep211_dialogues2_public_event_26() from _rcall_ep211_dialogues2_public_event_26
    if ep211_quests_publicevent2_3_guest_girlfriends_stage == 2: # уже поговорили со звездой
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        $ questHelp("office_38", True)
        $ remove_objective("talk_girlfriends")
        call ep211_dialogues2_public_event_30() from _rcall_ep211_dialogues2_public_event_30
        if "Girlfriends" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("Girlfriends")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_21
        $ ep211_quests_publicevent2_3_guest_girlfriends_stage = 3
        return False
    if ep211_quests_publicevent2_3_guest_girlfriends_stage == 3:
        call ep211_dialogues2_public_event_31() from _rcall_ep211_dialogues2_public_event_31

    return False

label ep211_quests_publicevent2_3_guest8: #звезда
    if act=="l":
        return
    if ep211_quests_publicevent2_3_guest8_flag == False:
        hide screen Reporters_Shoots_Screen4_low
        music2 stop
        call ep211_dialogues2_public_event_28() from _rcall_ep211_dialogues2_public_event_28
        $ questHelp("office_39", True)
        $ questHelp("office_38")
        $ questHelp("office_40", skipIfExists=True)
        $ remove_objective("talk_terner")
        $ add_objective("talk_girlfriends", t_("Вернуться к Ребекке и Стефани."), c_pink, 105)
        $ ep211_quests_publicevent2_3_guest8_flag = True
        $ ep211_quests_publicevent2_3_guest_girlfriends_stage = 2
        if "PublicGuest8" in ep211_quests_guests_progress:
            $ ep211_quests_guests_progress.remove("PublicGuest8")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_22
        return False
    call ep211_dialogues2_public_event_29() from _rcall_ep211_dialogues2_public_event_29
    return False

label ep211_quests_publicevent2_3_investor1:
    if act=="l":
        return
    hide screen Reporters_Shoots_Screen4_low
    music2 stop
    call ep211_dialogues2_public_event_35() from _rcall_ep211_dialogues2_public_event_35
    $ questHelp("office_41", True)
    $ questHelp("office_42", skipIfExists=True)
    $ questHelp("photoshoot_13")
    $ remove_objective("talk_people")
    music2 stop
    $ renpy.music.set_volume(1.0, 0.0, 'music2')
    $ remove_objective("talk_terner")
    music stop
    img black_screen
    with diss
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    $ miniMapEnabledOnly = []
    $ remove_objective("talk_investor1")
    $ ep211_quests_publicevent2_completed = True
    $ autorun_to_object("ep211_dialogues2_public_event_42", scene="street_monica_office")
    $ remove_hook(label="public_event2")
    call putoff_work_clothes() from _rcall_putoff_work_clothes_1
    $ add_hook("Teleport_Inside", "ep211_dialogues2_public_event_42", scene="street_monica_office", label="evening_time_temp")
    $ add_hook("before_open", "ep211_quests_publicevent2_photoshoot1", scene="monica_office_cabinet", label="photoshoot9_1")
    $ add_hook("before_open", "ep211_quests_publicevent2_photoshoot1", scene="monica_office_cabinet_table", label="photoshoot9_1")
    $ add_hook("enter_scene", "ep211_dialogues3_photoshoot_1", scene="monica_office_entrance", once=True, label="photoshoot9")
    call change_scene("street_monica_office", "Fade_long", False) from _rcall_change_scene_20
    return False

label ep211_quests_publicevent2_photoshoot1: # Моника заходит в кабинет Бифа
    if day_time != "evening":
        return
    $ remove_hook(label="photoshoot9_1")
    call ep211_dialogues3_photoshoot_2() from _rcall_ep211_dialogues3_photoshoot_2
    $ move_object("Melanie", "empty")
    $ add_objective("change_cloth", t_("Идти в фотостудию и переодеться."), c_orange, 105)
    $ miniMapEnabledOnly = ["Office_Biff_Cabinet", "Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока идет фотосессия
    $ add_hook("AlexPhotograph", "ep22_quests_office4", scene="monica_office_photostudio", label="photoshoot_alex") # Алекс стартует фотосессию
    $ add_hook("Biff", "ep22_quests_office5", scene="monica_office_cabinet_table", label="photoshoot") # Мне надо идти в фотостудию, блок на Биффа

    $ monicaOutfitsAltEnabled = True
    $ monicaOutfitsEnabled_Alt = [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
    $ ep211_quests_photoshoot_stage = 1
    call change_scene("monica_office_secretary") from _rcall_change_scene_21
    return False

label ep211_quests_publicevent2_photoshoot2: # Моника одела платье в первый раз
    $ remove_objective("change_cloth")
    $ ep211_quests_photoshoot_stage = 2
    call ep211_dialogues3_photoshoot_3() from _rcall_ep211_dialogues3_photoshoot_3
    call ep211_dialogues3_photoshoot_4() from _rcall_ep211_dialogues3_photoshoot_4
    if _return == False:
        $ questHelp("office_42", False)
        $ questHelp("photoshoot_13", False)
        $ monicaPhotoShootInProgress = False
        $ monicaOutfitsAltEnabled = False
        $ miniMapEnabledOnly = []
        $ remove_hook(label="public_event2_block")
        $ add_hook("Biff", "ep211_quests_publicevent2_photoshoot2_biff_repeat", scene="monica_office_cabinet_table", label="photoshoot9_repeat")
        $ autorun_to_object("ep211_dialogues3_photoshoot_4b", scene="street_monica_office")
        $ remove_hook(label="photoshoot")
        $ remove_hook(label="photoshoot_alex")
        call putoff_work_clothes() from _rcall_putoff_work_clothes_2
        call change_scene("street_monica_office", "Fade_long", False) from _rcall_change_scene_22
        return False
    $ questHelp("office_42", True)
    $ questHelp("photoshoot_13")
#    $ questHelpDesc("photoshoot_desc13")

    call change_scene("monica_office_cabinet_table") from _rcall_change_scene_23
    jump ep211_quests_publicevent2_photoshoot3
#    return False

label ep211_quests_publicevent2_photoshoot2_biff_repeat: # Повтор подхода к Бифу насчет фотосессии
    if act=="l":
        return
    call ep211_dialogues3_photoshoot_5() from _rcall_ep211_dialogues3_photoshoot_5
    if _return == False:
        $ autorun_to_object("ep211_dialogues3_photoshoot_4b", scene="street_monica_office")
        call putoff_work_clothes() from _rcall_putoff_work_clothes_3
        call change_scene("street_monica_office", "Fade_long", False) from _rcall_change_scene_24
        return False
    $ monicaOutfitsAltEnabled = True
    $ remove_hook(label="photoshoot9_repeat")
    $ add_objective("change_cloth", t_("Идти в фотостудию и переодеться."), c_orange, 105)
    $ miniMapEnabledOnly = ["Office_Biff_Cabinet", "Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("Teleport_Monica_Office_Entrance", "monica_office_secretary_dialogue6", scene="monica_office_secretary", label="photoshoot") #Блокируем выход пока идет фотосессия
    $ add_hook("AlexPhotograph", "ep22_quests_office4", scene="monica_office_photostudio", label="photoshoot_alex") # Алекс стартует фотосессию
    $ add_hook("Biff", "ep22_quests_office5", scene="monica_office_cabinet_table", label="photoshoot") # Мне надо идти в фотостудию, блок на Биффа
    $ monicaOutfitsAltEnabled = True

    return False

label ep211_quests_publicevent2_photoshoot3: # Фотосессия
    $ monicaOutfitsAltEnabled = False
    $ remove_objective("change_cloth")
    call ep211_dialogues3_photoshoot_6() from _rcall_ep211_dialogues3_photoshoot_6_1 # фотосессия
    call ep211_dialogues3_photoshoot_7() from _rcall_ep211_dialogues3_photoshoot_7_1
    $ remove_hook(label="public_event2_block")
    if _return == 0: # Моника отказалась
        $ monicaPhotoShootInProgress = False
        $ monicaOutfitsAltEnabled = False
        $ miniMapEnabledOnly = []
        $ remove_hook(label="public_event2_block")
        $ add_hook("Biff", "ep211_quests_publicevent2_photoshoot2_biff_repeat", scene="monica_office_cabinet_table", label="photoshoot9_repeat")
        $ autorun_to_object("ep211_dialogues3_photoshoot_4b", scene="street_monica_office")
        $ remove_hook(label="photoshoot")
        $ remove_hook(label="photoshoot_alex")
        call putoff_work_clothes() from _rcall_putoff_work_clothes_4
        call change_scene("street_monica_office", "Fade_long", False) from _rcall_change_scene_25
        return False
    if _return == -1: # Моника УВОЛИЛАСЬ
        $ monicaPhotoShootInProgress = False
        $ monicaOutfitsAltEnabled = False
        $ miniMapEnabledOnly = []
        $ remove_hook(label="public_event2_block")
        $ add_hook("Biff", "ep211_quests_publicevent2_photoshoot2_biff_repeat", scene="monica_office_cabinet_table", label="photoshoot9_repeat")
#        $ autorun_to_object("ep211_dialogues3_photoshoot_4b", scene="street_monica_office")
        $ remove_hook(label="photoshoot")
        $ remove_hook(label="photoshoot_alex")
        $ remove_objective("reports_to_biff")
        call putoff_work_clothes() from _rcall_putoff_work_clothes_5
        $ questsFailByCategory(t_("ФОТОСЕССИИ"))
        $ questsFailByCategory(t_("ОФИС"))

        $ questLog(64, False)
        $ questLog(63, False)
        $ questLog(47, False)
        $ questLog(6, False)
        $ questLog(43, False)
        $ questLog(46, False)
        $ questLog(7, False)
        $ questLog(8, False)
        $ questLog(9, False)
        $ questLog(67, False)
        $ questLog(68, True)
        $ autorun_to_object("ep211_dialogues3_photoshoot_8b", scene="street_monica_office")
        $ add_hook("Teleport_Inside", "ep211_dialogues3_photoshoot_8b", scene="street_monica_office", label="monica_office_fired1", priority=10001)
        $ monicaOfficeFiredType1 = True
        call change_scene("street_monica_office", "Fade_long", False) from _rcall_change_scene_26
        return False
    $ add_hook("before_open", "ep211_quests_publicevent2_photoshoot4", scene="monica_office_cabinet", label="photoshoot9_2")
    $ add_hook("before_open", "ep211_quests_publicevent2_photoshoot4", scene="monica_office_cabinet_table", label="photoshoot9_2")
    $ add_objective("talk_biff", t_("Пойти в кабиент к Бифу и узнать, что решил инвестор."), c_blue, 105)
    $ miniMapEnabledOnly = []
    $ monicaOutfitsEnabled[8] = True # Открываем костюм для регулярной съемки
    $ ep211_quests_photoshot8_opened_day = day
    call ep212_quests_photoshoot8_after_init() from _rcall_ep212_quests_photoshoot8_after_init
    sound snd_fabric1
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    $ remove_hook(label="photoshoot_alex")
    $ add_hook("Biff", "ep22_quests_office6", scene="monica_office_cabinet_table", label="photoshoot") #Мне надо получить деньги от Бифа
    $ add_hook("Teleport_Monica_Office_Entrance", "ep22_dialogue6_7a", scene="monica_office_secretary", label="photoshoot", priority = 105) #Блокируем выход пока не получили деньги от Бифа
    call change_scene("monica_office_cabinet", "Fade_long") from _rcall_change_scene_27
    return False

label ep211_quests_publicevent2_photoshoot4: # Моника возвращается к Бифу после фотосессии
    if day_time != "evening":
        return
    $ remove_objective("talk_biff")
    $ remove_hook(label="photoshoot9_2")
    call ep211_dialogues3_photoshoot_8() from _rcall_ep211_dialogues3_photoshoot_8
    $ autorun_to_object("ep22_dialogue6_7a", scene="monica_office_cabinet_table")
    call change_scene("monica_office_cabinet_table") from _rcall_change_scene_28
    $ add_corruption(monicaPhotoshoot9CorruptionAdd, "photoshoot9")
    $ ep211_quests_photoshoot_stage = 3
    return False








#
