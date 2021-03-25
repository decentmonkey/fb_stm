
label cloth_shop_dressing_room:
    if EP1 == True:
        jump cloth_shop_dressing_room_EP1
    $ print "enter_cloth_shop_dressing_room"
    $ miniMapData = []

    $ scene_caption = t_("Clothing Shop")

    $ scene_image = "scene_cloth_shop_dressing_room"
    return

label cloth_shop_dressing_room_init:
    if EP1 == True:
        return
    $ add_object_to_scene("Teleport_Dressing_Room2", {"type":2, "base":"Cloth_Shop_Dressing_Room_Teleport_Dressing_Room2", "click" : "cloth_shop_dressing_room_teleport", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_dressing_room_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label cloth_shop_dressing_room_teleport:
    if EP1 == True:
        jump cloth_shop_dressing_room_teleport_EP1
    if obj_name == "Teleport_Dressing_Room2":
        if act == "l":
            mt "Эта примерочная... Я помню как спала здесь!"
            return
        if obj_data["action"] == "w":
            call change_scene("cloth_shop_dressing_room2") from _call_change_scene_250
            return
    if obj_name == "Teleport_Cloth_Shop_View1":
        call change_scene("cloth_shop_view1") from _call_change_scene_251
        return


label cloth_shop_dressing_room_environment:
    if EP1==True:
        jump cloth_shop_dressing_room_environment_EP1
    return
