default monicaKitchenForbidden = True

label kitchen:
    if EP1==True:
        jump kitchen_EP1
    $ print "enter_kitchen"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_7

    $ scene_image = "scene_Kitchen[day_suffix]"
    music Mandeville

#    if gameStage > 2:
#        if monicaKitchenForbidden == True and scene_name != lastSceneName:
#            $ autorun_to_object(scene_name, "afterJailHouse_dialogue15")
    return

label kitchen_init:
    if EP1==True:
        return
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Kitchen_Monica_[cloth]", "click" : "kitchen_environment", "actions" : "l", "zorder":12, "tint": monica_tint})

    $ add_object_to_scene("Food", {"type":2, "base":"Kitchen_Food", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Fridge", {"type":2, "base":"Kitchen_Fridge", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":0.2, "c":1.8, "group":"environment"})
    $ add_object_to_scene("Gas_Cooker", {"type":2, "base":"Kitchen_Gas_Cooker", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Kitchen_Lamps", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":-0.15, "group":"environment"})
    $ add_object_to_scene("Microwave_Oven", {"type":2, "base":"Kitchen_Microwave_Oven", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Plates", {"type":2, "base":"Kitchen_Plates", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Ventilation", {"type":2, "base":"Kitchen_Ventilation", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Drawers", {"type":2, "base":"Kitchen_Drawers", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Wine", {"type":2, "base":"Kitchen_Wine", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Kitchen2", {"type":3, "text" : t_("ОБЕДЕННЫЙ СТОЛИК"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "kitchen_teleport", "xpos" : 1620, "ypos" : 520, "zorder":15})


    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label kitchen_teleport:
    if EP1==True:
        jump kitchen_teleport_EP1
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1") from _call_change_scene_73
        return
    if obj_name == "Teleport_Kitchen2":
        call change_scene("kitchen2") from _call_change_scene_74
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("kitchen") from _call_change_scene_75
        return

label kitchen_environment:
    if EP1==True:
        jump kitchen_environment_EP1
    if monicaKitchenForbidden == True:
        if get_active_objects("Betty", scene="House", recursive=True) != False:
            call afterJailHouse_dialogue15a() from _call_afterJailHouse_dialogue15a_1
            return
        call ep22_dialogue1_5_kitchen() from _call_ep22_dialogue1_5_kitchen_1
        return
    return






# EP1



label kitchen_EP1:
    $ print "enter_kitchen"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_5

    $ scene_name = "kitchen"
    $ scene_caption = t_("Kitchen")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Kitchen_Monica_" + cloth + day_suffix

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Kitchen_Monica_" + cloth, "click" : "kitchen_environment", "actions" : "l", "zorder":12, "tint": monica_tint})
#    if juliaPunished == False and juliaLocation == "kitchen":
    if juliaLocation == "kitchen":
        $ add_object_to_scene("Julia", {"type" : 2, "base" : "Kitchen_Julia1", "click" : "julia_interact", "actions" : "l", "zorder":10})
    if juliaPunished == True and juliaLocation == "floor1":
        $ add_object_to_scene("Julia", {"type" : 2, "base" : "Kitchen_Julia1", "click" : "julia_interact", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Food", {"type":2, "base":"Kitchen_Food", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fridge", {"type":2, "base":"Kitchen_Fridge", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":0.2, "c":1.8})
    $ add_object_to_scene("Gas_Cooker", {"type":2, "base":"Kitchen_Gas_Cooker", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Kitchen_Lamps", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":-0.15})
    $ add_object_to_scene("Microwave_Oven", {"type":2, "base":"Kitchen_Microwave_Oven", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Plates", {"type":2, "base":"Kitchen_Plates", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Ventilation", {"type":2, "base":"Kitchen_Ventilation", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Drawers", {"type":2, "base":"Kitchen_Drawers", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Wine", {"type":2, "base":"Kitchen_Wine", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover": True})
    $ add_object_to_scene("Teleport_Kitchen2", {"type":3, "text" : t_("ОБЕДЕННЫЙ СТОЛИК"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "kitchen_teleport", "xpos" : 1620, "ypos" : 520, "zorder":15})

    if gameStage > 2:
        if monicaKitchenForbidden == True and scene_name != lastSceneName:
            $ autorun_to_object(scene_name, "afterJailHouse_dialogue15")

    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label kitchen_teleport_EP1:
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1") from _call_change_scene_18
        return
    if obj_name == "Teleport_Kitchen2":
        call change_scene("kitchen2") from _call_change_scene_19
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("kitchen") from _call_change_scene_20
        return

label kitchen_environment_EP1:
    if gameStage > 2:
        if monicaKitchenForbidden == False:
            call afterJailHouse_dialogue12() from _call_afterJailHouse_dialogue12
            return
        else:
            mt "Бетти запретила мне притрагиваться к чему-либо..."
            "Мне лучше уйти отсюда скорее, пока она не заметила меня!"
            return
    if obj_name == "Wine":
        m "Это вино.
        Естественно, очень дорогое."

        m "Я могу иногда выпить бокальчик вина во время обеда."

        "Даже завтрака.
        Я аристократка.
        Я могу себе это позволить."

    if obj_name == "Drawers":
        m "В этих ящика хранится всевозможная кухонная утварь."

        "Мне совершенно неинтересно что именно там лежит!"

    if obj_name == "Food":
        m "Это какая-то уже готовая еда."

        "Не помню приказывала-ли я Юлии готовить или нет."

        "Хотя... она же сама должна об этом заботиться."

        "Надеюсь хоть что-то можно поручить работникам делать без моего вмешательства!"

    if obj_name == "Fridge":
        m "Это холодильник."

        "Он всегда должен быть заполнен свежими продуктами."

        "Об этом должна заботиться Юлия."

        "Нет продуктов - работа не сделана.
        Служащий - уволен."

        "Это мое кредо!"

    if obj_name == "Gas_Cooker":
        m "На этой газовой плите Юлия готовит еду для меня."

        "Мне лично подходить к таким вещам неприятно."

        "Такие очаровательные девушки как я должны украшать этот мир, а не стоять у плиты!"

        "Для стояния у плиты есть такие как Юлия!"

    if obj_name == "Lamps":
        m "Лампочки!!!
        Уииии!!"

    if obj_name == "Microwave_Oven":
        m "Юлия может использовать эту микроволновую печь, но только чтобы разогреть еду ДЛЯ СЕБЯ!"

        "Моя еда всегда свежая и горячая, только что приготовленная!"

    if obj_name == "Plates":
        m "Чистая посуда."

        "Даже ту посуду, которая не испачкана, гувернантка обязана регулярно протирать от пыли."

    if obj_name == "Ventilation":
        m "Просто кухонная вытяжка..."

        "Скучно..."


    if obj_name == "Monica":
        if scene_name == "kitchen":
            m "Моя кухня."

            "Моя она в том смысле что Я решаю кому можно здесь находиться."

            "Готовить, разумеется я здесь не собираюсь."

            "Для этого есть обычные люди, которые рады трудиться в таком прекрасном месте."
        if scene_name == "kitchen2":
            m "В этой части кухни стоит мой обеденный столик."

            "Я могла бы обедать в нашей роскошной гостиной."

            "Но я считаю что в этом слишком много пафоса."

            "Ведь я же скромняшка!"

            "Да, и я в детстве всегда кушала на кухне."

            "Наверное эта привычка - оттуда."
    return
