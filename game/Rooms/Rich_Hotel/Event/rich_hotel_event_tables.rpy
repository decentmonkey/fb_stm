label rich_hotel_event_tables:
    $ print "rich_hotel_event_tables"
    $ miniMapData = []

    $ scene_image = "scene_rich_hotel_event_tables"
    return

label rich_hotel_event_tables_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_tables_Monica_[cloth]", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "rich_hotel_event_tables_Philip", "click" : "rich_hotel_event_tables_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Chair1", {"type" : 2, "base" : "rich_hotel_event_tables_Chair1", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair2", {"type" : 2, "base" : "rich_hotel_event_tables_Chair2", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair3", {"type" : 2, "base" : "rich_hotel_event_tables_Chair3", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair4", {"type" : 2, "base" : "rich_hotel_event_tables_Chair4", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair5", {"type" : 2, "base" : "rich_hotel_event_tables_Chair5", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair6", {"type" : 2, "base" : "rich_hotel_event_tables_Chair6", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair7", {"type" : 2, "base" : "rich_hotel_event_tables_Chair7", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Chair8", {"type" : 2, "base" : "rich_hotel_event_tables_Chair8", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})

    $ add_object_to_scene("Drinks", {"type" : 2, "base" : "rich_hotel_event_tables_Drinks", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Flower", {"type" : 2, "base" : "rich_hotel_event_tables_Flower", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People", {"type" : 2, "base" : "rich_hotel_event_tables_People", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Table1", {"type" : 2, "base" : "rich_hotel_event_tables_Table1", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Table2", {"type" : 2, "base" : "rich_hotel_event_tables_Table2", "click" : "rich_hotel_event_tables_environment", "actions" : "l", "zorder":0})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Hall", {"type":3, "text" : t_("ИДТИ КО СЦЕНЕ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow", "click" : "rich_hotel_event_sofa_teleport", "xpos" : 1633, "ypos" : 997, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_tables_teleport:
    if obj_name == "Teleport_Rich_Hotel_Hall":
        call change_scene("rich_hotel_event_hall") from _call_change_scene_70
        return
    return
label rich_hotel_event_tables_environment:
    if obj_name == "Monica":
        mt "Вот мерзавец!"
        "Что же мне делать?"
        "Я ведь не буду соглашаться на его предложение, так ведь?!?!"
        "Это безумие!"
        "Ведь у меня есть другой выход?!?! Или нет??..."
        return
    if obj_name == "Philip":
        if act == "l":
            mt "Я не могу поверить в то что этот мерзавец сказал мне только что!!!"
            "Что же мне делать?"
            "Я ведь не буду соглашаться на его предложение, так ведь?!?!"
            "Это безумие!"
            "Ведь у меня есть другой выход?!?! Или нет??..."
            return
        if act == "t":
            return

    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4":
        mt "Мне не до этого сейчас!"
        "Мне надо найти деньги, срочно!"
        return
    if obj_name == "Chair5" or obj_name == "Chair6" or obj_name == "Chair7" or obj_name == "Chair8":
        mt "Я не собираюсь сидеть за столиком с этим мерзавцем!"
        return
    if obj_name == "Drinks":
        mt "Здесь полно недорогого алкоголя!"
        "Кто бы мог подумать что это вино столько стоит!!!"
        return
    if obj_name == "Flower":
        mt "Мне не до этого сейчас!"
        "Мне надо найти деньги, срочно!"
        return
    if obj_name == "People":
        mt "Может быть попросить помощи у кого-нибудь???"
        "Но вряд-ли это поможет. Судя по виду, здесь все такие же мерзавцы как этот Филипп!"
        return
    if obj_name == "Table1":
        mt "Мне не до этого сейчас!"
        "Мне надо найти деньги, срочно!"
        return
    if obj_name == "Table2":
        mt "Я не собираюсь сидеть за столиком с этим мерзавцем!"
        return

    return
