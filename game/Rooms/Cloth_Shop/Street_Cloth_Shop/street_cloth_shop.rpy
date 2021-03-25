default s2ClothShopStage = 0

label street_cloth_shop:

    $ print "enter_street_cloth_shop"
    $ miniMapData = []

    $ scene_name = "street_cloth_shop"
    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Cloth_Shop[day_suffix]"
    if day_time == "day":
        music street7
    else:
        music street_evening4

label street_cloth_shop_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Cloth_Shop_Monica_" + cloth + day_suffix, "click" : "street_cloth_shop_environment2", "actions" : "l", "zorder" : 12})

    $ add_object_to_scene("Parking_Cash", {"type":2, "base":"Street_Cloth_Shop_Parking_Cash", "click" : "street_cloth_shop_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trees", {"type":2, "base":"Street_Cloth_Shop_Trees", "click" : "street_cloth_shop_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Cloth_Shop_Entrance", {"type":3, "text" : t_("Магазин Одежды"), "rarrow" : "arrow_right_2", "base": "Street_Cloth_Shop_Teleport_Inside", "click" : "street_cloth_shop_teleport2", "xpos" : 835, "ypos" : 341, "zorder":11, "teleport":True})

    $ add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : t_("Вверх по улице"), "rarrow" : "arrow_up_2", "base": "Street_Cloth_Shop_Teleport_Shawarma", "click" : "street_cloth_shop_teleport2", "xpos" : 1705, "ypos" : 887, "zorder":11, "teleport":True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_cloth_shop_teleport2:
    if obj_name == "Teleport_Cloth_Shop_Entrance":
        call cloth_shop_refuse1() from _call_cloth_shop_refuse1
        return
    if obj_name == "Teleport_Shawarma":
        call change_scene("whores_place_shawarma", "Fade_long", "highheels_run2") from _call_change_scene_99
        return
    return
label street_cloth_shop_environment2:
    if obj_name == "Parking_Cash":
        mt "Парковочный автомат?"
    if obj_name == "Trees":
        mt "Милые деревья."
        "Но мне не до деревьев сейчас!"

    if obj_name == "Monica":
        mt "Это тот магазин куда меня приводил Дик..."
    return
