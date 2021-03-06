default s2ClothShopStage = 0

label EP1_street_cloth_shop_s2:

    $ print "enter_street_cloth_shop_s2"
    $ miniMapData = []

    $ scene_name = "street_cloth_shop_s2"
    $ sceneIsStreet = True
    $ scene_caption = t_("Clothing Shop")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Street_Cloth_Shop_Monica_" + cloth + day_suffix
    $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Street_Cloth_Shop_Monica_" + cloth + day_suffix, "click" : "EP1_street_cloth_shop_environment", "actions" : "l", "zorder" : 12})

    $ EP1_add_object_to_scene("Parking_Cash", {"type":2, "base":"Street_Cloth_Shop_Parking_Cash", "click" : "EP1_street_cloth_shop_environment2", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trees", {"type":2, "base":"Street_Cloth_Shop_Trees", "click" : "EP1_street_cloth_shop_environment2", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Teleport_Cloth_Shop_Entrance", {"type":3, "text" : t_("Магазин Одежды"), "rarrow" : "arrow_right_2", "base": "Street_Cloth_Shop_Teleport_Inside", "click" : "EP1_street_cloth_shop_teleport2", "xpos" : 835, "ypos" : 341, "zorder":11})

    if s2ClothShopStage == 1:
        $ EP1_autorun_to_object("street_cloth_shop_s2", "after_jail_cloth_shop_street")

    if whoresPlaceOpened == True:
        $ EP1_add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : t_("Вверх по улице"), "rarrow" : "arrow_up_2", "base": "Street_Cloth_Shop_Teleport_Shawarma", "click" : "EP1_street_cloth_shop_teleport2", "xpos" : 1705, "ypos" : 887, "zorder":11})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_street_cloth_shop_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_Cloth_Shop_Entrance":
        if gameStage == 3:
            if gameSubStage == 1:
                call EP1_hostelAfterJail_street_dialogue8()
                return
            mt "Там слишком много народа! У меня не получится ничего взять там! НЕ ПОЛУЧИТСЯ!!! (хмык)"
            return
        if s2ClothShopStage == 0:
            hide screen Rain
            music Groove2_85
            img 2649
            with fadelong
            w
            img 2650
            with fade
            w
            img 2651
            mt "Я не буду спрашивать у этой сучки где мне переночевать."
            img 2652
            mt "Все-равно она дура и ничего не знает!"
            stop sound fadeout 1.0
            call EP1_refresh_scene_fade()
            return

        if gameStage == 2 and gameSubStage == 2:
            mt "Туда не стоит идти. Спать там уже не выйдет, а их дешевые платья мне не нужны!"
            return
        if gameStage == 2:
            music Stealth_Groover
        call EP1_change_scene("cloth_shop_view1", "Fade_long")
        return
    if obj_name == "Teleport_Shawarma":
        call EP1_change_scene("whores_place_shawarma", "Fade_long", "highheels_run2")
        return
    return
label EP1_street_cloth_shop_environment2(obj_name, obj_data):
    if obj_name == "Parking_Cash":
        mt "Парковочный автомат?"
    if obj_name == "Trees":
        mt "Милые деревья."
        "Но мне не до деревьев сейчас!"

    if obj_name == "Monica":
        mt "Это тот магазин куда меня приводил Дик..."


    return
