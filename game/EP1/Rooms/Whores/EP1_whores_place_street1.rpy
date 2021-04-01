label EP1_whores_place_street1:
    $ print "enter_whores_place_street1"
    $ miniMapData = []

    $ scene_name = "whores_place_street1"
    $ sceneIsStreet = True
    $ scene_caption = t_("Dirty street")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_street_Whores_Street1_" + cloth + day_suffix
    $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Street1_" + cloth + day_suffix, "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 10})

    $ EP1_add_object_to_scene("Fire_Valve", {"type":2, "base":"Street_Whores_Street1_Fire_Valve", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_Whores_Street1_Street_Fencing1", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ EP1_add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_Whores_Street1_Street_Fencing2", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ EP1_add_object_to_scene("Street_Light", {"type":2, "base":"Street_Whores_Street1_Street_Light", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Street_Sign", {"type":2, "base":"Street_Whores_Street1_Street_Sign", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash_Can", {"type":2, "base":"Street_Whores_Street1_Trash_Can", "click" : "EP1_whores_place_street1_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Street_Corner", {"type":3, "text" : t_("УГОЛ УЛИЦЫ"), "rarrow" : "arrow_right_2", "base":"Street_Whores_Street1_Teleport_Street_Corner", "click" : "EP1_whores_place_street1_teleport", "xpos" : 1724, "ypos" : 462, "zorder":15})
    $ EP1_add_object_to_scene("Teleport_Whores_Place", {"type":3, "text" : t_("ПЕРЕКРЕСТОК"), "larrow" : "arrow_left_2", "base":"Street_Whores_Street1_Teleport_Whores_Place", "click" : "EP1_whores_place_street1_teleport", "xpos" : 308, "ypos" : 515, "zorder":15})

    if whoresMonicaDisturb == True:
        $ EP1_autorun_to_object("whores_place_s2", "afterjail_whores_disturb_dialogue1")

    $ whoresPlacePreviousLocation = "street"

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_whores_place_street1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street_Corner":
        call EP1_change_scene("street_corner", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Whores_Place":
        call EP1_change_scene("whores_place", "Fade_long", "highheels_run2")
        return
    return
label EP1_whores_place_street1_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 2:
            mt "Отвратительное место!"
            return
        mt "Отвратительное место! Долго мне еще идти?"
    if obj_name == "Fire_Valve":
        mt "Что это? Пожарный вентиль?
        Из позапрошлого века??"
    if obj_name == "Street_Fencing1" or obj_name == "Street_Fencing2":
        if gameStage == 3:
            mt "Эти старые ржавые ограждения очень опасны."
            return
        mt "Эти старые ржавые ограждения очень опасны."
        "Их можно задеть и испачкать мой красивый наряд!"
    if obj_name == "Street_Light":
        mt "Хорошо бы чтоб этот фонарь не упал на меня, пока я здесь иду!"
    if obj_name == "Street_Sign":
        mt "Какой-то старый ржавык дорожный знак..."
    if obj_name == "Trash_Can":
        mt "Мусорка? Зачем она здесь нужна?"
        "Все это место - сплошная помойка!"
    return
