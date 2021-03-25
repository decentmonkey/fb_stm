default pubInited = False
default monicaPubWashingDishesCount = 0 # Кол-во раз Моника мыла посуду
default pubFoodHistory = []

label ep23_quests_pub_init: #инициализация локации бара
    $ pubInited = True
#    $ hostelStreetSceneName = "scene_Hostel_Street_Pub[day_suffix]"
    $ add_hook("enter_scene", "ep23_quests_pub", scene="hostel_street")
    $ add_object_to_scene("Teleport_Hostel_Pub", {"type":3, "text" : t_("SHINY HOLE"), "larrow" : "arrow_down_2_a", "base":"Hostel_Street_Pub_Teleport_Pub", "click" : "hostel_street_teleport", "xpos" : 1641, "ypos" : 471, "zorder":16, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True, "high_sprite_hover":True}, scene="hostel_street")
    return
label ep23_quests_pub:
    $ remove_hook()
    call ep23_dialogues1_1() from _call_ep23_dialogues1_1
    $ add_location("pub", caption=t_("SHINY HOLE"), label="pub", init_label="pub_init", parent="Street_Corner")
    call characters_pub_init() from _call_characters_pub_init
    call Pub_Life_init() from _call_Pub_Life_init
    $ add_hook("Teleport_Hostel_Pub", "ep23_dialogues1_1a", scene="hostel_street")
    $ add_hook("enter_scene", "ep23_quests_pub1", scene="pub")
    return

label ep23_quests_pub1: #Моника заходит в бар первый раз
    $ remove_hook()
    call ep23_dialogues1_2() from _call_ep23_dialogues1_2
    $ add_hook("Bartender", "ep23_quests_pub2", scene="pub", label="pub_dialogue")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub2", scene="pub", label="pub_dialogue")
    call refresh_scene_fade() from _call_refresh_scene_fade_76
    return

label ep23_quests_pub1a:
    call ep23_dialogues1_2() from _call_ep23_dialogues1_3b
    $ add_hook("Bartender", "ep23_quests_pub2", scene="pub", label="pub_dialogue")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub2", scene="pub", label="pub_dialogue")
    call refresh_scene_fade() from _call_refresh_scene_fade_76bb1
    return

label ep23_quests_pub2: #при клике на бармена или барменшу
    if act=="l":
        return
    $ remove_hook()
    call ep23_dialogues1_2a() from _call_ep23_dialogues1_2a
    call refresh_scene_fade() from _call_refresh_scene_fade_77
    $ add_hook("enter_scene", "ep23_quests_pub3", scene="hostel_street")
    music2 stop
    call change_scene("hostel_street") from _call_change_scene_221
    return

label ep23_quests_pub3: #комментарий на улице
    $ remove_hook()
    call ep23_dialogues1_2c() from _call_ep23_dialogues1_2c
    $ remove_hook(label="pub_dialogue")
    $ add_hook("Bartender", "ep23_quests_pub4", scene="pub", label="pub_dialogue")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub4", scene="pub", label="pub_dialogue")
    return

label ep23_quests_pub4: # диалог о приеме на работу
    call ep23_dialogues1_3() from _call_ep23_dialogues1_3
    if _return == False:
        if act != "l":
            $ questHelp("shinyhole_1", False)
            music2 stop
            call change_scene("hostel_street") from _call_change_scene_222
        return False

    $ questHelp("shinyhole_1", True)
    $ questHelp("shinyhole_2")
    $ questHelp("shinyhole_3")
    $ questHelpDesc("shinyhole_desc1")

    $ monicaWorkingAsDishwasher = True
    $ add_location("pub_bar1", caption=t_("SHINY HOLE"), label="pub_bar1", init_label="pub_bar1_init", parent="pub")
    $ add_hook("Monica", "ep23_quests_pub6_dishes", scene="pub_bar1", label="pub_dishes_process")
    $ add_hook("Pub_Bar1_Washbasin", "ep23_quests_pub6_dishes", scene="pub_bar1", label="pub_dishes_process")
    $ add_hook("Bartender", "ep23_quests_pub6_dishes_bartender", scene="pub_bar1", label="pub_dishes_process")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub6_dishes_bartender_waitress", scene="pub_bar1", label="pub_dishes_process")

    $ remove_hook(label="pub_dialogue")
    $ add_hook("Bartender", "ep23_quests_pub5_dishes", scene="pub", label="pub_dishes")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub5_dishes", scene="pub", label="pub_dishes")
    $ add_object_to_scene("Pub_Washbasin", {"type" : 2, "base" : "Pub_Washbasin", "click" : "pub_environment", "actions" : "lh", "zorder":0, "group":"environment"}, scene="pub")
    $ add_hook("Pub_Washbasin", "ep23_quests_pub5_dishes", scene="pub", label="pub_dishes")

    $ questLog(30, True)
    call Pub_Life2_init() from _call_Pub_Life2_init # Обычное наполнение бара
    call refresh_scene_fade() from _call_refresh_scene_fade_78
    return False


label ep23_quests_pub5_dishes: # Моника моет посуду
    if cloth_type == "Waitress": #костыль, чтобы не было меню во время работы официанткой!
        $ act="l"
    if act=="l" and obj_name != "Pub_Bar1_Washbasin":
        return

    call ep23_dialogues1_4a() from _call_ep23_dialogues1_4a
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_79
        return False
#    $ rand1 = rand(1,10)
#    if rand1 >= 7:
#        $ set_active("Bartender", False, scene="pub_bar1")
#        $ set_active("Bartender_Waitress", True, scene="pub_bar1")
#    else:
#        $ set_active("Bartender", True, scene="pub_bar1")
#        $ set_active("Bartender_Waitress", False, scene="pub_bar1")
    if _return == 1: # Мыть посуду
        if monicaEatedLastDay == day:
            call ep23_dialogues1_4() from _call_ep23_dialogues1_4
            return False
        $ set_active("Bartender", True, scene="pub_bar1")
        $ set_active("Bartender_Waitress", True, scene="pub_bar1")
        call change_scene("pub_bar1") from _call_change_scene_223
        return False
    if _return == 2: # Заказать еду
        call ep23_dialogues1_6() from _call_ep23_dialogues1_6
        if _return != False:
            call monicaEat() from _call_monicaEat_12
        call change_scene("hostel_street", "Fade_long") from _call_change_scene_333
        return False
    if _return == 3: # Спросить о повышении
        call ep27_quests_pub_work1() from _call_ep27_quests_pub_work1
        return False
    if _return == 4: #Работать официанткой в Shiny Hole.
        call ep27_quests_pub_work2_begin() from _call_ep27_quests_pub_work2_begin
        return False
    if _return == 5: #Танцевать на сцене
        call pub_dance_start() from _call_pub_dance_start
        return False
    if _return == 6:
        call ep23_dialogues1_7() from _call_ep23_dialogues1_7
        call refresh_scene_fade() from _call_refresh_scene_fade_235
        return False

    return False


label ep23_quests_pub6_dishes: # Клик на Монику
    # Мытье посуды без приставаний
    call ep23_dialogues1_4a2() from _call_ep23_dialogues1_4a2
    img 9650
    with fadelong
    call ep23_dialogues1_5() from _call_ep23_dialogues1_5
    call monicaEat() from _call_monicaEat_8
    call change_scene("hostel_street", "Fade_long") from _call_change_scene_224
    return False

label ep23_quests_pub6_dishes_bartender: # Клик на Бармена
    call pub_bar1_environment() from _call_pub_bar1_environment
    call ep23_dialogues1_4a2() from _call_ep23_dialogues1_4a2_1
    call ep23_dialogues1_4b() from _call_ep23_dialogues1_4b
    call ep23_dialogues1_5() from _call_ep23_dialogues1_5_1
    call monicaEat() from _call_monicaEat_9
    call change_scene("hostel_street", "Fade_long") from _call_change_scene_225
    return False

label ep23_quests_pub6_dishes_bartender_waitress: # Клик на Барменшу
    call pub_bar1_environment() from _call_pub_bar1_environment_1
    call ep23_dialogues1_4a2() from _call_ep23_dialogues1_4a2_2
    call ep23_dialogues1_4c() from _call_ep23_dialogues1_4c
    
    call ep23_dialogues1_5() from _call_ep23_dialogues1_5_2
    call monicaEat() from _call_monicaEat_10
    call change_scene("hostel_street", "Fade_long") from _call_change_scene_226
    return False



#
