default EP1_whores_place_shawarma_s2_crossroad_blocked = False
label EP1_whores_place_shawarma_s2:
    $ print "enter_whores_place_shawarma_s2"
    $ miniMapData = []

    $ scene_name = "whores_place_shawarma_s2"
    $ sceneIsStreet = True
    $ scene_caption = t_("Shawarma")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_street_whores_place_shawarma_Monica" + day_suffix
    $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Street_whores_place_shawarma_Monica_" + cloth + day_suffix, "click" : "EP1_whores_place_shawarma_environment2", "actions" : "l", "zorder" : 10})
    $ EP1_add_object_to_scene("Shawarma_Trader", {"type":2, "base":"Street_whores_place_shawarma_Trader" + day_suffix, "click" : "EP1_whores_place_shawarma_environment2", "actions" : "lt", "zorder" : 5})

    $ EP1_add_object_to_scene("Shawarma_Stall", {"type":2, "base":"Street_whores_place_shawarma_Stall", "click" : "EP1_whores_place_shawarma_environment2", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_whores_place_shawarma_Street_Fencing1", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ EP1_add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_whores_place_shawarma_Street_Fencing2", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ EP1_add_object_to_scene("Trash_Can", {"type":2, "base":"Street_whores_place_shawarma_Trash_Can", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Fire_Valve", {"type":2, "base":"Street_whores_place_shawarma_Fire_Valve", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash1", {"type":2, "base":"Street_whores_place_shawarma_Trash1", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash2", {"type":2, "base":"Street_whores_place_shawarma_Trash2", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash3", {"type":2, "base":"Street_whores_place_shawarma_Trash3", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash4", {"type":2, "base":"Street_whores_place_shawarma_Trash4", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash5", {"type":2, "base":"Street_whores_place_shawarma_Trash5", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash6", {"type":2, "base":"Street_whores_place_shawarma_Trash6", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash7", {"type":2, "base":"Street_whores_place_shawarma_Trash7", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash8", {"type":2, "base":"Street_whores_place_shawarma_Trash8", "click" : "EP1_whores_place_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Clothing_Shop", {"type":3, "text" : t_("К МАГАЗИНУ ОДЕЖДЫ"), "larrow" : "arrow_down_2", "base":"Street_whores_place_shawarma_Teleport_Clothing_Shop", "click" : "EP1_whores_place_shawarma_teleport2", "xpos" : 304, "ypos" : 856, "zorder":15})
    $ EP1_add_object_to_scene("Teleport_Street_Hostel", {"type":3, "text" : t_("ПОДВОРОТНЯ"), "larrow" : "arrow_left_2", "base":"Street_whores_place_shawarma_Teleport_Street_Hostel", "click" : "EP1_whores_place_shawarma_teleport2", "xpos" : 182, "ypos" : 376, "zorder":15})
    if EP1_whores_place_shawarma_s2_crossroad_blocked == False:
        $ EP1_add_object_to_scene("Teleport_Whores_Place", {"type":3, "text" : t_("К ПЕРЕКРЕСТКУ"), "rarrow" : "arrow_right_2", "base":"Street_whores_place_shawarma_Teleport_Whores_Place", "click" : "EP1_whores_place_shawarma_teleport2", "xpos" : 1375, "ypos" : 1022, "zorder":15})

    if whoresMonicaDisturb == True:
        $ EP1_autorun_to_object("whores_place_s2", "afterjail_whores_disturb_dialogue1")

    $ whoresPlacePreviousLocation = "shawarma"

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_whores_place_shawarma_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_Clothing_Shop":
        if shawarmaTraderStage == 1:
            call EP1_dress_return_shawarma_talk2()
            return
        call EP1_change_scene("street_cloth_shop", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Street_Hostel":
        if streetHostelPathEnabled == False:
            mt "Я не пойду в эту вонючую подворотню!"
            "Что там забыла такая девушка как Я!??"
            return
        call EP1_change_scene("hostel_street", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Whores_Place":
        call EP1_change_scene("whores_place", "Fade_long", "highheels_run2")
        return

    return
label EP1_whores_place_shawarma_environment2(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 3 and gameSubStage == 1:
            call EP1_hostelAfterJail_street_dialogue3()
            return
        return
    if obj_name == "Shawarma_Stall":
        mt "Какой-то грязный ларек, который продает помои!"
        "Кто может это есть?"
    if obj_name == "Shawarma_Trader":
        if obj_data["action"] == "l":
            mt "Грязный продавец. Я не выношу даже его вида! Фу!"
        if obj_data["action"] == "t":
            if gameStage == 3 and gameSubStage == 1:
                mt "Мне не о чем разговаривать с ним!"
                return
            if gameStage == 2 and gameSubStage == 1:
                mt "Мне не о чем разговаривать с ним!"
                return
            if gameStage == 2 and gameSubStage == 2:
                if hostelReceptionVisited == True:
                    call EP1_afterJail_Day2_Shawarma_dialogue2()
                    return
                call EP1_afterJail_Day2_Shawarma_dialogue1()
                return
            hide screen Rain
            music DarxieLand
            img 2653
            with fadelong
            shawarma "Мадаме!"
            img 2654
            "Вы передумали?"
            "Попробуете мою шаверму?"
            img 2655
            if shawarmaTraderOffended1 == True:
                m "Отстань, животное!"
            else:
                m "Оставьте меня в покое!"
            img 2656
            mt "Может стоило у него спросить про ночлег?"
            img 2657
            mt "..."
            if shawarmaTraderOffended1 == True:
                "Нет, не у этого животного точно!"
            else:
                "Нет, не у этого человека точно!"
            music stop
            call EP1_refresh_scene_fade()
        return
