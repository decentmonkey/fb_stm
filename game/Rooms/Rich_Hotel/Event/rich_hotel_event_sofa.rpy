label rich_hotel_event_sofa:
    $ print "rich_hotel_event_sofa"
    $ miniMapData = []

    $ scene_image = "scene_rich_hotel_event_sofa_Monica_Melanie_biff"
    return

label rich_hotel_event_sofa_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_sofa_Monica_[cloth]", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Biff", {"type" : 2, "base" : "rich_hotel_event_sofa_biff", "click" : "rich_hotel_event_sofa_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "rich_hotel_event_sofa_Melanie", "click" : "rich_hotel_event_sofa_environment", "actions" : "lt", "zorder":11})

    $ add_object_to_scene("Komode", {"type" : 2, "base" : "rich_hotel_event_sofa_Komode", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Lamp", {"type" : 2, "base" : "rich_hotel_event_sofa_Lamp", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("TV1", {"type" : 2, "base" : "rich_hotel_event_sofa_TV1", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("TV2", {"type" : 2, "base" : "rich_hotel_event_sofa_TV2", "click" : "rich_hotel_event_sofa_environment", "actions" : "l", "zorder":0, "group":"environment"})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})

    $ add_object_to_scene("Teleport_Rich_Hotel_Hall", {"type":3, "text" : t_("ИДТИ КО СЦЕНЕ"), "larrow" : "arrow_left_2", "base":"Rich_Hotel_Event_Sofa_Teleport_Hall", "click" : "rich_hotel_event_sofa_teleport", "xpos" : 767, "ypos" : 1014, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_sofa_teleport:
    if obj_name == "Teleport_Rich_Hotel_Hall":
        call change_scene("rich_hotel_event_hall") from _call_change_scene_76
        return
    return
label rich_hotel_event_sofa_environment:
    if obj_name == "Monica":
        if richHotelEventStage == 1:
            mt "Что же мне делать???"
            mt "Может быть как-то уговорить Бифа дать мне недостающую сумму денег?"
        if richHotelEventStage == 0:
            mt "Мне не нравится этот Биф!"
            "Надо скорее забрать у него деньги и больше с ним не встречаться!"
        return
    if obj_name == "Biff":
        if act == "l":
            mt "Мерзкий слизняк Биф!"
            "Я найду на него управу!!!"
            "Клянусь!"
            return
        if act == "t":
            return
    if obj_name == "Melanie":
        img 7108
        with fade
        if act == "l":
            mt "Мелани пристально смотрит на меня..."
            return
        if act == "t":
            mt "Мелани пристально смотрит на меня..."
            "И молчит..."
            return
        call refresh_scene_fade() from _call_refresh_scene_fade_25
        return
    if obj_name == "Komode":
        if richHotelEventStage == 1:
            mt "Может здесь внутри есть какие-нибудь деньги?"
            "Но нет... Это чушь..."
        if richHotelEventStage == 0:
            mt "..."
        return
    if obj_name == "Lamp":
        if richHotelEventStage == 1:
            mt "Мне не до этого сейчас!"
            "Мне надо найти деньги, срочно!"
        if richHotelEventStage == 0:
            mt "Милый светильник."
            "Приятный свет."
        return
    if obj_name == "TV1" or obj_name == "TV2":
        mt "Скоро на всех модных ТВ-каналах начнут показывать мое выступление..."
        "Надеюсь мои слова не слишком растиражируют..."
        "Мне надо будет потом как-то отказаться от них, объяснить что это было не так понято."
        "Я придумаю что-нибудь когда верну все назад!"
        return
    return
