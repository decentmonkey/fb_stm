label ep27_police1_init:
    $ add_hook("Building", "ep27_police2_enter", scene="street_police", label="police_quest1")
    return


label ep27_police2_enter: #вход в здание полиции
    if act=="l":
        return
    if day_time == "evening": # Вечером не заходим
        call ep27_dialogues_marcus1_1b() from _call_ep27_dialogues_marcus1_1b
        return False
    if cloth != "CasualDress1":
        call ep27_dialogues_marcus1_1c() from _call_ep27_dialogues_marcus1_1c
        return False
    call ep27_dialogues_marcus1_1a() from _call_ep27_dialogues_marcus1_1a
    if _return == False:
        $ questHelp("marcus_1", False)
        $ questHelp("marcus_2", False)

        return False
    $ autorun_to_object("ep27_dialogues_marcus1_1", scene="police_entrance")
    $ add_hook("Reception", "ep27_police2_reception_dialogue", scene="police_entrance", label="police_entrance_dialogue1")
    $ add_hook("Teleport_Inside", "ep27_police2_reception_dialogue", scene="police_entrance", label="police_entrance_dialogue1")
    $ set_var("Reception", actions="lt", scene="police_entrance")
    return

label ep27_police2_reception_dialogue: # Разговор в проходной (начало квеста)
    if act=="l" and obj_name != "Teleport_Inside":
        call ep27_dialogues_marcus1_1d() from _call_ep27_dialogues_marcus1_1d
        return
    call ep27_dialogues_marcus1_2() from _call_ep27_dialogues_marcus1_2 # Приходит Детектив
    if _return == False:
        $ questHelp("marcus_1", False)
        $ questHelp("marcus_2", False)
        $ autorun_to_object("ep27_dialogues_marcus1_1d", scene="street_police")
        call change_scene("street_police", "Fade_long") from _call_change_scene_380
        return False
    $ remove_hook(label="police_entrance_dialogue1")
    $ set_var("Reception", actions="l", scene="police_entrance")

    call ep27_dialogues_marcus1_3() from _call_ep27_dialogues_marcus1_3 # Входят в тюрьму
    call ep27_dialogues_marcus1_4() from _call_ep27_dialogues_marcus1_4 # Входят в камеру
    call ep27_dialogues_marcus1_5() from _call_ep27_dialogues_marcus1_5 # Моника в камере

    $ questHelp("marcus_2", True)
    $ questHelp("marcus_3")

    $ cloth = "JailRobe" # Переодеваем Монику
    $ cloth_type = "Jail"
    $ inventory = [] # Забираем весь инвентарь
    $ money = 0 # отбираем деньги

    $ add_hook("cage_interact", "ep27_police3_interact_cage1", scene="police", label="cage_interact1")

    call locations_init_police_jail_cage() from _call_locations_init_police_jail_cage # Инициализируем камеру
    call change_scene("police_cell1", "Fade_long", False) from _call_change_scene_381


#    call ep27_dialogues_marcus1_9() # Боб
#    call ep27_dialogues_marcus1_11()
    return False

label ep27_police3_interact_cage1:
    call ep27_dialogues_marcus1_9() from _call_ep27_dialogues_marcus1_9
    $ questHelp("marcus_3", True)
    music stop
    img black_screen
    with diss
    pause 1.5
    call change_scene("police_cell1", "Fade_long") from _call_change_scene_382
    return
