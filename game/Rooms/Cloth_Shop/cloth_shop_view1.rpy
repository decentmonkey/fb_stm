default clothShopMusicType = 1

label cloth_shop_view1:
    if EP1 == True:
        jump cloth_shop_view1_EP1
    $ print "enter_cloth_shop_view1"
    $ miniMapData = []

    $ scene_caption = t_("Clothing Shop")

    $ scene_image = "scene_Cloth_Shop_View1"
    if clothShopMusicType == 1:
        music Sneaky_Snitch
    return

label cloth_shop_view1_init:
    if EP1 == True:
        return
    $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_View1_Monica_[cloth]", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 10}, scene="cloth_shop_view1")

    $ add_object_to_scene("Shop_Visitor1", {"type":2, "base":"Cloth_Shop_View1_v1", "click" : "cloth_shop_view1_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"cloth_shop_visitors"}, scene="cloth_shop_view1")
    $ add_object_to_scene("Shop_Visitor2", {"type":2, "base":"Cloth_Shop_View1_v2", "click" : "cloth_shop_view1_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"cloth_shop_visitors"}, scene="cloth_shop_view1")
    $ add_object_to_scene("Shop_Visitor4", {"type":2, "base":"Cloth_Shop_View1_v4", "click" : "cloth_shop_view1_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view1")
    $ add_object_to_scene("Shop_Visitor5", {"type":2, "base":"Cloth_Shop_View1_v5", "click" : "cloth_shop_view1_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view1")
    $ add_object_to_scene("Shop_Visitor6", {"type":2, "base":"Cloth_Shop_View1_v6", "click" : "cloth_shop_view1_environment", "actions" : "lt", "zorder" : 5, "group":"cloth_shop_visitors"}, scene="cloth_shop_view1")

    $ add_object_to_scene("Teleport_Cashier", {"type":2, "base":"Cloth_Shop_View1_Cashier", "click" : "cloth_shop_view1_teleport", "actions" : "lw", "zorder" : 0, "teleport":True}, scene="cloth_shop_view1")
    $ add_object_to_scene("Teleport_Dressing_Room", {"type":2, "base":"Cloth_Shop_View1_DressingRoom", "click" : "cloth_shop_view1_teleport", "actions" : "lw", "zorder" : 0, "teleport":True}, scene="cloth_shop_view1")
    $ add_object_to_scene("Teleport_View2", {"type":3, "text" : t_("ИДТИ ДАЛЬШЕ"), "rarrow" : "arrow_up_2", "base":"Cloth_Shop_View1_Teleport_View2", "click" : "cloth_shop_view1_teleport", "xpos" : 183, "ypos" : 929, "zorder":11, "high_sprite_hover":True, "teleport":True}, scene="cloth_shop_view1")
    $ add_object_to_scene("Teleport_Street_Cloth_Shop", {"type":3, "text" : t_("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover":True, "teleport":True}, scene="cloth_shop_view1")

    return
label cloth_shop_view1_teleport:
    if EP1 == True:
        jump cloth_shop_view1_teleport_EP1
    if obj_name == "Teleport_View2":
        call change_scene("cloth_shop_view2") from _call_change_scene_267
        return
    if obj_name == "Teleport_Dressing_Room":
        if obj_data["action"] == "l":
            mt "Там примерочная."
            return
        if obj_data["action"] == "w":
            call change_scene("cloth_shop_dressing_room") from _call_change_scene_268
            return
    if obj_name == "Teleport_Cashier":
        if obj_data["action"] == "l":
            mt "Там касса..."
            return
        if obj_data["action"] == "w":
            call change_scene("cloth_shop_cashier") from _call_change_scene_269
    if obj_name == "Teleport_Street_Cloth_Shop":
        call change_scene("street_cloth_shop", "Fade_long") from _call_change_scene_270
        return
    return

label cloth_shop_view1_environment:
    if EP1 == True:
        jump cloth_shop_view1_environment_EP1
    if obj_name == "Monica":
        mt "Дешевый магазин, Фи!"

    if obj_name == "Shop_Visitor1" or obj_name == "Shop_Visitor2":
        if act== "l":
            mt "Покупатель в этом жутком магазине."
        if act == "t":
            if monicaBitch == True:
                mt "Мне не о чем говорить с этим ничтожеством!"
            else:
                mt "Мне не о чем говорить с этим покупателем!"
    if obj_name == "Shop_Visitor4" or obj_name == "Shop_Visitor5" or obj_name == "Shop_Visitor6":
        if act == "l":
            mt "Покупатель в этом жутком магазине."
        if act == "t":
            if monicaBitch == True:
                mt "Мне не о чем говорить с этим ничтожеством!"
            else:
                mt "Мне не о чем говорить с этим покупателем!"


    return
