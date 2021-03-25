label cloth_shop_view2:
    if EP1== True:
        jump cloth_shop_view2_EP1
    $ print "enter_cloth_shop_view2"
    $ miniMapData = []

    $ scene_caption = t_("Clothing Shop")

    $ scene_image = "scene_Cloth_Shop_View2"
    return

label cloth_shop_view2_init:
    if EP1 == True:
        return
    $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_View2_Monica_[cloth]", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 10}, scene="cloth_shop_view2")

    $ add_object_to_scene("Shop_Visitor3", {"active": False, "type":2, "base":"Cloth_Shop_View2_v3", "click" : "cloth_shop_view2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors", "icon_t":"/Icons/talk" + res.suffix +".png"}, scene="cloth_shop_view2")
    $ add_object_to_scene("Shop_Visitor7", {"active": False, "type":2, "base":"Cloth_Shop_View2_v7", "click" : "cloth_shop_view2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view2")
    $ add_object_to_scene("Shop_Visitor8", {"active": False, "type":2, "base":"Cloth_Shop_View2_v8", "click" : "cloth_shop_view2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view2")
    $ add_object_to_scene("Shop_Visitor9", {"active": False, "type":2, "base":"Cloth_Shop_View2_v9", "click" : "cloth_shop_view2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view2")
    $ add_object_to_scene("Shop_Visitor10", {"active": False, "type":2, "base":"Cloth_Shop_View2_v10", "click" : "cloth_shop_view2_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view2")

    $ add_object_to_scene("Teleport_Cashier", {"type":3, "text" : t_("К КАССЕ"), "rarrow" : "arrow_right_2", "base":"Cloth_Shop_View2_Teleport_Cashier", "click" : "cloth_shop_view2_teleport", "xpos" : 1602, "ypos" : 917, "zorder":11, "teleport":True}, scene="cloth_shop_view2")
    $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="cloth_shop_view2")

    return

label cloth_shop_view2_teleport:
    if EP1 == True:
        jump cloth_shop_view2_teleport_EP1
    if obj_name == "Teleport_Cloth_Shop_View1":
        call change_scene("cloth_shop_view1") from _call_change_scene_305
        return
    if obj_name == "Teleport_Cashier":
        call change_scene("cloth_shop_cashier") from _call_change_scene_306
        return
    return


label cloth_shop_view2_environment:
    if EP1 == True:
        jump cloth_shop_view2_environment_EP1
    if obj_name == "Shop_Visitor3":
        if act== "l":
            mt "Покупатель в этом жутком магазине."
        if act == "t":
            if monicaBitch == True:
                mt "Мне не о чем говорить с этим ничтожеством!"
            else:
                mt "Мне не о чем говорить с этим покупателем!"
    if obj_name == "Shop_Visitor7" or obj_name == "Shop_Visitor8" or obj_name == "Shop_Visitor9" or obj_name == "Shop_Visitor10":
        if act == "l":
            mt "Покупатель в этом жутком магазине."
        if act == "t":
            if monicaBitch == True:
                mt "Мне не о чем говорить с этим ничтожеством!"
            else:
                mt "Мне не о чем говорить с этим покупателем!"
    return
