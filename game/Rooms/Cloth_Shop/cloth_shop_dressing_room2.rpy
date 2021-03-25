
label cloth_shop_dressing_room2:
    if EP1 == True:
        jump cloth_shop_dressing_room2_EP1
    $ print "enter_cloth_shop_dressing_room2"
    $ miniMapData = []

    $ scene_caption = t_("Clothing Shop")

    $ scene_image = "scene_cloth_shop_dressing_room2"
    return

label cloth_shop_dressing_room2_init:
    if EP1 == True:
        return
    $ add_object_to_scene("Shop_Visitor4", {"type":2, "base":"Cloth_Shop_dressing_room2_v4", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_dressing_room2")
    $ add_object_to_scene("Shop_Visitor7", {"type":2, "base":"Cloth_Shop_dressing_room2_v7", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_dressing_room2")
    $ add_object_to_scene("Shop_Visitor8", {"type":2, "base":"Cloth_Shop_dressing_room2_v8", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_dressing_room2")
    $ add_object_to_scene("Shop_Visitor9", {"type":2, "base":"Cloth_Shop_dressing_room2_v9", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_dressing_room2")
    $ add_object_to_scene("Shop_Visitor10", {"type":2, "base":"Cloth_Shop_dressing_room2_v10", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_dressing_room2")


    $ add_object_to_scene("Sofa", {"type":2, "base":"cloth_shop_dressing_room2_sofa", "click" : "cloth_shop_dressing_room2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Dressing_Room", {"type":3, "text" : t_("НАЗАД"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "cloth_shop_dressing_room2_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True})
#    $ add_object_to_scene("Teleport_Dressing_Room2", {"type":2, "base":"Cloth_Shop_Dressing_Room_Teleport_Dressing_Room2", "click" : "cloth_shop_dressing_room_teleport", "actions" : "lw", "zorder" : 0})
#    $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_dressing_room_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label cloth_shop_dressing_room2_teleport:
    if EP1 == True:
        jump cloth_shop_dressing_room2_EP1
    if obj_name == "Teleport_Dressing_Room":
        call change_scene("cloth_shop_dressing_room") from _call_change_scene_248
        return
    return

label cloth_shop_dressing_room2_environment:
    if EP1== True:
        jump cloth_shop_dressing_room2_environment_EP1
    if obj_name == "Sofa":
        if act == "l":
            mt "Не могу поверить что мне пришлось спать здесь!"
            mt "Мне! Монике Бакфетт!"
            return

    return
