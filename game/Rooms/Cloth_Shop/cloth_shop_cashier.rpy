label cloth_shop_cashier:
    if EP1==True:
        jump cloth_shop_cashier_EP1
    $ print "enter_cloth_shop_cashier"
    $ miniMapData = []

    $ scene_caption = t_("Clothing Shop")

    $ scene_image = "scene_cloth_shop_cashier"
    return

label cloth_shop_cashier_init:
    if EP1==True:
        return
    $ add_object_to_scene("Cashier", {"type":2, "base":"Cloth_Shop_Cashier_Character", "click" : "cloth_shop_cashier_environment", "actions" : "lt", "zorder" : 5}, scene="cloth_shop_cashier")
    $ add_object_to_scene("Teleport_Dressing_Room", {"type":3, "text" : t_("К ПРИМЕРОЧНОЙ"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "cloth_shop_cashier_teleport", "xpos" : 1640, "ypos" : 152, "zorder":11, "teleport":True}, scene="cloth_shop_cashier")
    $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_cashier_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="cloth_shop_cashier")

    return

label cloth_shop_cashier_teleport:
    if EP1==True:
        jump cloth_shop_cashier_teleport_EP1
    if obj_name == "Teleport_Cloth_Shop_View1":
        call change_scene("cloth_shop_view1") from _call_change_scene_271
        return
    if obj_name == "Teleport_Dressing_Room":
        call change_scene("cloth_shop_dressing_room") from _call_change_scene_272
        return
    return


label cloth_shop_cashier_environment:
    if EP1==True:
        jump cloth_shop_cashier_environment_EP1
    if obj_name == "Cashier":
        if act == "l":
            img Cloth_Shop_Cashier2
            with fade
            w
            img Cloth_Shop_Cashier3
            mt "Фу! Какая-то лесбиянка!"
            return

    return
