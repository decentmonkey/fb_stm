label EP1_basement_bedroom2:
    $ print "enter_basement_bedroom2"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "basement_bedroom2"
    $ scene_caption = t_("BASEMENT")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Basement_Bedroom2_Monica_" + cloth
    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Bedroom2_Monica_" + cloth, "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    if basementBedroomJournal == True:
        $ EP1_add_object_to_scene("Journal", {"type":2, "base":"Basement_Bedroom2_Journal", "click" : "EP1_basement_bedroom2_environment", "actions" : "lw", "zorder" : 1})

    $ EP1_add_object_to_scene("BasementBed", {"type":2, "base":"Basement_Bedroom2_Bed", "click" : "EP1_basement_bedroom2_environment", "actions" : "lh", "zorder" : 0})
    $ EP1_add_object_to_scene("Book", {"type":2, "base":"Basement_Bedroom2_Book", "click" : "EP1_basement_bedroom2_environment", "actions" : "lw", "zorder" : 0})
    $ EP1_add_object_to_scene("Cupboard", {"type":2, "base":"Basement_Bedroom2_Cupboard", "click" : "EP1_basement_bedroom2_environment", "actions" : "lw", "zorder" : 0})
    $ EP1_add_object_to_scene("Lamp", {"type":2, "base":"Basement_Bedroom2_Lamp", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "b":0.18})
    $ EP1_add_object_to_scene("Picture1", {"type":2, "base":"Basement_Bedroom2_Picture1", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture2", {"type":2, "base":"Basement_Bedroom2_Picture2", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture3", {"type":2, "base":"Basement_Bedroom2_Picture3", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture4", {"type":2, "base":"Basement_Bedroom2_Picture4", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture5", {"type":2, "base":"Basement_Bedroom2_Picture5", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture6", {"type":2, "base":"Basement_Bedroom2_Picture6", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture7", {"type":2, "base":"Basement_Bedroom2_Picture7", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture8", {"type":2, "base":"Basement_Bedroom2_Picture8", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture9", {"type":2, "base":"Basement_Bedroom2_Picture9", "click" : "EP1_basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Table", {"type":2, "base":"Basement_Bedroom2_Table", "click" : "EP1_basement_bedroom2_environment", "actions" : "lw", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : t_("ШКАФ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_basement_bedroom2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label EP1_basement_bedroom2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bedroom1":
        if basementBedroomStage == 0:
            mt "Там на столике что-то лежит..."
            return
        call EP1_change_scene("basement_bedroom1")
        return
    return

label EP1_basement_bedroom2_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Видимо это и есть место где я теперь буду спать..."
    if obj_name == "BasementBed":
        if act == "l":
            mt "Вот теперь моя кровать..."
        if act == "h":
            if basementBedroomStage == 0:
                mt "Там на столике что-то лежит..."
                return
            if cloth != "Nude" and cloth != "GovernessPants":
                if cloth == "Governess":
                    img 3367
                    with fade
                mt "Мне надо раздеться сначала"
                call EP1_refresh_scene_fade()
                return
            menu:
                "Лечь спать.":
                    pass
                "Не ложиться.":
                    return
            call EP1_episode1End()
            return
    if obj_name == "Book":
        if act == "l":
            mt "Какая-то книга Юлии..."
        if act == "w":
            call EP1_change_scene("basement_bedroom_table")
            return
    if obj_name == "Cupboard":
        if act == "l":
            mt "Старый шкаф..."
        if act == "w":
            $ basementBedroom2CupboardReturnScene = "basement_bedroom2"
            call EP1_change_scene("basement_bedroom2_cupboard")
            return

    if obj_name == "Journal":
        if act == "l":
            mt "Там на столике что-то лежит..."
            return
        if act == "w":
            call EP1_change_scene("basement_bedroom_table")
            return

    if obj_name == "Lamp":
        mt "Эта тусклая лампа - это почти весь свет, который есть в этой каморке..."
    if obj_name == "Picture1" or obj_name == "Picture2" or obj_name == "Picture3" or obj_name == "Picture4" or obj_name == "Picture5" or obj_name == "Picture6" or obj_name == "Picture7" or obj_name == "Picture8" or obj_name == "Picture9":
        mt "Живопись..."
        "Я не знала что Юлия увлекается этим."
        "Она пыталась быть похожей на меня?"
        "..."
    if obj_name == "Table":
        if act == "l":
            mt "Этот старый яркий пестрый стол пытается скрасить уныние этой каморки..."
            "Тщетно..."
        if act == "w":
            call EP1_change_scene("basement_bedroom_table")
            return
    return
