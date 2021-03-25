default richHotelEventStage = 0

label rich_hotel_event_hall:
    $ print "rich_hotel_event_hall"
    $ miniMapData = []

    $ scene_image = "scene_Rich_Hotel_Event_Hall"

    return

label rich_hotel_event_hall_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Monica_[cloth]", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Philip", "click" : "rich_hotel_event_hall_environment", "actions" : "lt", "zorder":15, "icon_t":"/Icons/talk" + res.suffix +".png"})
    $ add_object_to_scene("HotelStaff", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_HotelStaff", "click" : "rich_hotel_event_hall_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Chair1", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair1", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Chair2", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair2", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Chair3", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair3", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Chair4", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Chair4", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Lamp", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Lamp", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Palm", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Palm", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("People", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_People", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Poster", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Poster", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("PosterMelanie", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_PosterMelanie", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Scene", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Scene", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Table", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Table", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Cloth", {"type" : 2, "base" : "Rich_Hotel_Event_Hall_Clothing", "click" : "rich_hotel_event_hall_environment", "actions" : "l", "zorder":0, "group":"environment"})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Reception", {"type":3, "text" : t_("ЛИФТ"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Event_Hall_Exit", "click" : "rich_hotel_event_hall_teleport", "xpos" : 319, "ypos" : 230, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Rich_Hotel_Tables", {"type":3, "text" : t_("СТОЛИКИ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow", "click" : "rich_hotel_event_hall_teleport", "xpos" : 264, "ypos" : 581, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Rich_Hotel_Sofa", {"type":3, "text" : t_("ВИП ЗОНА"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Event_Hall_Teleport_Sofa", "click" : "rich_hotel_event_hall_teleport", "xpos" : 1517, "ypos" : 1038, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_hall_teleport:
    if obj_name == "Teleport_Rich_Hotel_Reception":
#            call change_scene("rich_hotel_reception")
        return
    if obj_name == "Teleport_Rich_Hotel_Tables":
        call change_scene("rich_hotel_event_tables") from _call_change_scene_135
        return
    if obj_name == "Teleport_Rich_Hotel_Sofa":
        call change_scene("rich_hotel_event_sofa") from _call_change_scene_136
        return
    return
label rich_hotel_event_hall_environment:

    if obj_name == "Monica":
        if richHotelEventStage == 1:
            mt "Черт! Что же делать???"
            "Где мне достать деньги???"
        if richHotelEventStage == 0:
            mt "Приятное место..."
            "Я расслабляюсь..."
        return
    if obj_name == "Philip":
        if act == "l":
            mt "Какой-то кавалер..."
            "Смотрит на меня весь вечер."
            "Мило..."
            return
        if act == "t":
            return
    if obj_name == "HotelStaff":
        if act == "l":
            mt "Этот мальчик из персонала отеля."
            "Не стоит внимания..."
            return
        if act == "t":
            return

    if obj_name == "Cloth":
        mt "Эта одежда закрывает собой мой постер!"
        return
    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4":
        if richHotelEventStage == 1:
            mt "В этих стульях явно не спрятаны деньги, которые мне так нужны!"
        if richHotelEventStage == 0:
            mt "В этом месте дорогая мебель..."
            "Мило..."
        return
    if obj_name == "Lamp":
        if richHotelEventStage == 1:
            mt "Мне не до этого сейчас!"
            "Мне надо найти деньги, срочно!"
        if richHotelEventStage == 0:
            mt "Милый светильник."
            "Приятный свет."
        return
    if obj_name == "Palm":
        if richHotelEventStage == 1:
            mt "Мне не до этого сейчас!"
            "Мне надо найти деньги, срочно!"
        if richHotelEventStage == 0:
            mt "Пальма..."
            "Вспоминаю свой отдых на островах..."
        return
    if obj_name == "People":
        if richHotelEventStage == 1:
            mt "Может быть попросить помощи у кого-нибудь???"
            "Но вряд-ли это поможет. Судя по виду, здесь все такие же мерзавцы как этот Филипп!"
        if richHotelEventStage == 0:
            mt "Наверное это журналист..."
            "Надеюсь мои слова не слишком растиражируют..."
            "Мне надо будет потом как-то отказаться от них, объяснить что это было не так понято."
            "Я придумаю что-нибудь когда верну все назад!"
        return
    if obj_name == "Poster":
        mt "Постер с обложкой моего журнала."
        mt "Эта одежда закрывает собой мой постер!"
        return
    if obj_name == "PosterMelanie":
        mt "Мелани?! Здесь?!"
        "А почему не Я?!"
        return
    if obj_name == "Scene":
        mt "Я наговорила на этой сцене всякой ерунды..."
        mt "Надеюсь мои слова не слишком растиражируют..."
        "Мне надо будет потом как-то отказаться от них, объяснить что это было не так понято."
        "Я придумаю что-нибудь когда верну все назад!"
        return
    if obj_name == "Table":
        if richHotelEventStage == 1:
            mt "Мне не до этого сейчас!"
            "Мне надо найти деньги, срочно!"
        if richHotelEventStage == 0:
            mt "Может быть мне присесть за один из столиков?"
        return

    return
