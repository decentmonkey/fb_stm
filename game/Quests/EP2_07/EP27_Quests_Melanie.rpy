default ep27_quests_melanie_init_flag = False
default ep27_melanie_going_to_victoria = False
default ep27_melanie_refused_victoria_meeting = False
default ep27_melanie_visited_victoria = False
default ep27_melanie_refused_victoria_friendship = False #Мелани решила подумать стать-ли подружкой Виктории
default ep27_melanie_refused_victoria_leg_finger = False #Мелани не стала брать в рот палец Виктории

label ep27_quests_melanie1_init:
    if melanieMonicaSawFarmTattoo == True and ep27_quests_melanie_init_flag == False:
        $ remove_hook(label="melanie_returned_dialogue1")
        $ add_hook("Melanie", "ep27_quests_melanie2_dialogue", scene="monica_office_makeup_room", label="melanie_returned_dialogue2")
        $ ep27_quests_melanie_init_flag = True

    return

label ep27_quests_melanie2_dialogue: # Диалог с Мелани
    call ep27_dialogues1_melanie1() from _call_ep27_dialogues1_melanie1
    if _return == False:
        $ ep27_melanie_refused_victoria_meeting = True
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_22
        return False
    $ questHelp("melanie_7a", True)
    $ questHelp("melanie_8")
    $ questHelpDesc("melanie_desc7", "melanie_desc8")
    $ remove_hook(label="melanie_returned_dialogue2")
    $ add_hook("Melanie", "ep27_dialogues1_melanie1a", scene="monica_office_makeup_room", label="melanie_returned_dialogue3")
    $ autorun_to_object("ep27_dialogues1_melanie1a", scene="monica_office_photostudio")
    $ add_hook("basement_monica_after_sleep_dialogue", "ep27_quests_melanie2_dialogue_aftersleep", scene="global") # Диалог о Мелани после просыпания
    $ add_hook("change_time_day", "ep27_quests_melanie2_init_map", scene="global")
    call change_scene("monica_office_photostudio", "Fade_long") from _call_change_scene_364
    return False

label ep27_quests_melanie2_dialogue_aftersleep:
    $ remove_hook()
    call ep27_dialogues1_melanie1b() from _call_ep27_dialogues1_melanie1b
    return

label ep27_quests_melanie2_init_map: # Инициализация посещения Мелани (карта)
    $ remove_hook()
    call locations_init_melanie_home() from _call_locations_init_melanie_home
    $ add_objective("go_to_melanie", t_("Идти к Мелани домой"), c_red, 30)
    $ map_objects["Teleport_Melanie_Home"] = {"text" : t_("АПАРТАМЕНТЫ МЕЛАНИ"), "xpos" : 1726, "ypos" : 791, "base" : "map_marker", "state" : "visible"}
    $ add_hook("map_teleport", "ep27_quests_melanie4_melanie_check_whore_cloth", scene="global", priority = 2000, label="melanie_home_checkcloth")
    $ add_hook("open", "ep27_quests_melanie3_melanie_home_scene", scene="melanie_home")
    return

label ep27_quests_melanie3_melanie_home_scene:
    $ remove_hook()
    $ remove_hook(label="melanie_returned_dialogue3")
    $ remove_hook(label="melanie_home_checkcloth")
    $ add_hook("map_teleport", "ep27_quests_melanie3a_block_melanie_home", scene="global", priority = 2000, label="melanie_home_restrict") # Блокируем дом Мелани
    call ep27_dialogues1_melanie2() from _call_ep27_dialogues1_melanie2

    $ questHelp("melanie_8", True)
    $ questHelp("marcus_2")
    $ questHelp("melanie_9")
    $ questHelpDesc("melanie_desc8", "melanie_desc9")
    $ questHelpDesc("marcus_desc1", "marcus_desc2")

    $ photoshoot8_melanie_forced = True
    music stop
    img black_screen
    with diss
    pause 1.5
    $ remove_objective("go_to_melanie")
    $ questLog(19, False)
    $ questLog(54, True)
    $ add_hook("change_time_day", "ep27_quests_melanie5_victoria_scene1", scene="global") # Виктория звонит Мелани
    $ changeDayTime("evening")
    $ autorun_to_object("ep27_dialogues1_melanie3", scene="street_house_outside") # Комментарий после встречи с Мелани
    $ add_hook("Melanie", "ep27_quests_melanie7_block_melanie", scene="monica_office_makeup_room", label="ep27_melanie_block_end1") # Блокируем Мелани
    call ep27_police1_init() from _call_ep27_police1_init

#    $ rain = True
#    $ rainIntencity = 3
#    $ lightning = True
#    $ add_hook("before_open", "ep27_quests_melanie3b_stop_rain", scene="World", recursive=True, label="stop_rain_temp")
    call process_change_map_location("House") from _call_process_change_map_location_3
    call change_scene("street_house_outside", "Fade_long", "highheels_run2") from _call_change_scene_365
    return

label ep27_quests_melanie3a_block_melanie_home: # Блокируем дом Мелани на карте
    if obj_name == "Teleport_Melanie_Home":
        call ep27_dialogues1_melanie4() from _call_ep27_dialogues1_melanie4
        return False
    return

label ep27_quests_melanie3b_stop_rain: # Выключаем дождь
    if scene_name == "map" or check_scene_parent(scene_name, "House", recursive=True) == True:
#    if scene_name == "map" or scene_name == "street_house_outside":
        return
    $ remove_hook(label="stop_rain_temp")
    $ rain = False
    $ rainIntencity = 3
    $ lightning = False
    hide screen Rain
    stop music
    $ SStop()
    return

label ep27_quests_melanie4_melanie_check_whore_cloth: # Переодеваем Монику перед приходом к Мелани
    if cloth != "Whore" and cloth_type != "Nude" and obj_name == "Teleport_Melanie_Home":
        mt "Мелани просила меня придти в другой... Одежде..."
        return False
    if cloth_type == "Nude":
        $ cloth = "Whore" #Принудительно переодеваем Монику
        $ cloth_type = "Whore"

#        menu:
#            "Переодеться в одежду шлюхи.":
#                $ cloth = "Whore" #Принудительно переодеваем Монику
#                $ cloth_type = "Whore"
    return


label ep27_quests_melanie5_victoria_scene1:
    $ remove_hook()
    call ep27_dialogues2_melanie1() from _call_ep27_dialogues2_melanie1
    if _return == True:
        $ ep27_melanie_going_to_victoria = True
        $ add_hook("map_teleport", "ep27_quests_melanie6_victoria_scene1", scene="global", label="victoria_scene1")
        $ add_hook("change_time_evening", "ep27_quests_melanie6_victoria_scene1", scene="global", label="victoria_scene1")
    else:
        $ questHelp("melanie_9", False)
        $ questHelp("victoria_2", False)
    return

label ep27_quests_melanie6_victoria_scene1:
    $ remove_hook(label="victoria_scene1")
    call ep27_dialogues2_melanie2() from _call_ep27_dialogues2_melanie2
    $ questHelp("melanie_9", True)
    if _return == 0: # Мелани решила подумать стать-ли подружкой Виктории
        $ ep27_melanie_refused_victoria_friendship = True
        $ questHelp("victoria_2", False)
        pass
    else:
        $ questHelp("victoria_2")
        $ questHelpDesc("victoria_desc2")

    if _return == 1: # Мелани не стала брать в рот палец Виктории
        $ ep27_melanie_refused_victoria_leg_finger = True
        pass


    music stop
    img black_screen
    with diss
    pause 2.0

    $ ep27_melanie_visited_victoria = True
    return

label ep27_quests_melanie7_block_melanie: # Блокируем диалог с Мелани
    if act=="l":
        return
    call ep27_dialogues1_melanie4() from _call_ep27_dialogues1_melanie4_1
    return False
