default richHotelReceptionMonicaSuffix = 1
default richHotelReceptionReceptionSuffix = 1
default richHotelReceptionPhilipSuffix = 1
default richHotelReceptionHotelStaffSuffix = 1

default richHotelReceptionSkipMusicOnce = False

label rich_hotel_reception:
    $ print "enter_rich_hotel_reception"
    $ miniMapData = []

    $ scene_image = "scene_Rich_Hotel_Reception"

    if richHotelReceptionMonicaSuffix == 2 and cloth == "EscortDress1":
        $ richHotelReceptionMonicaSuffix = 1

    if richHotelReceptionSkipMusicOnce == False:
        music Stealth_Groover
    $ richHotelReceptionSkipMusicOnce = False
    return

label rich_hotel_reception_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Rich_Hotel_Reception_Monica[richHotelReceptionMonicaSuffix]_[cloth]", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder":10}, scene="rich_hotel_reception")
    $ add_object_to_scene("ReceptionGirl", {"type" : 2, "base" : "Rich_Hotel_Reception_Reception_[richHotelReceptionReceptionSuffix]", "click" : "rich_hotel_reception_environment", "actions" : "lt", "zorder":4}, scene="rich_hotel_reception")

    $ add_object_to_scene("Logo", {"type":2, "base":"Rich_Hotel_Reception_Logo", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3]}, scene="rich_hotel_reception")
    $ add_object_to_scene("Clocks", {"type":2, "base":"Rich_Hotel_Reception_Clocks", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3}, scene="rich_hotel_reception")
    $ add_object_to_scene("Door", {"type":2, "base":"Rich_Hotel_Reception_Door", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3, "b":0.15}, scene="rich_hotel_reception")
    $ add_object_to_scene("Flowers", {"type":2, "base":"Rich_Hotel_Reception_Flowers", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3}, scene="rich_hotel_reception")
    $ add_object_to_scene("Jug1", {"type":2, "base":"Rich_Hotel_Reception_Jug1", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3}, scene="rich_hotel_reception")
    $ add_object_to_scene("Jug2", {"type":2, "base":"Rich_Hotel_Reception_Jug2", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3}, scene="rich_hotel_reception")
    $ add_object_to_scene("Tea", {"type":2, "base":"Rich_Hotel_Reception_Tea", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 15}, scene="rich_hotel_reception")
    $ add_object_to_scene("Desk", {"type":2, "base":"Rich_Hotel_Reception_Desk", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3}, scene="rich_hotel_reception")
    $ add_object_to_scene("Chair", {"type":2, "base":"Rich_Hotel_Reception_Chair", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3}, scene="rich_hotel_reception")

    $ add_object_to_scene("Teleport_Restaurant", {"type":3, "text" : t_("РЕСТОРАН"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Reception_Teleport_Restaurant", "click" : "rich_hotel_reception_teleport", "xpos" : 1018, "ypos" : 103, "zorder":11, "teleport":True}, scene="rich_hotel_reception")
    $ add_object_to_scene("Teleport_Street_Rich_Hotel", {"type":3, "text" : t_("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "rich_hotel_reception_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="rich_hotel_reception")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_reception_init2:
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "Rich_Hotel_Reception_Philip[richHotelReceptionPhilipSuffix]", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder":5, "active":False}, scene="rich_hotel_reception")
    $ add_object_to_scene("HotelStaff", {"type" : 2, "base" : "Rich_Hotel_Reception_HotelStaff[richHotelReceptionHotelStaffSuffix]", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder":4, "active":False}, scene="rich_hotel_reception")
    return

label rich_hotel_reception_init3:
    # escort
    $ add_object_to_scene("Teleport_Restaurant", {"type":3, "text" : t_("РЕСТОРАН"), "larrow" : "arrow_left_2", "base":"Rich_Hotel_Reception_Teleport_Restaurant2", "click" : "rich_hotel_reception_teleport", "xpos" : 1687, "ypos" : 202, "zorder":11, "teleport":True}, scene="rich_hotel_reception")
    $ add_object_to_scene("Teleport_Lift", {"type":3, "text" : t_("ЛИФТ"), "rarrow" : "arrow_down_2", "base":"Rich_Hotel_Reception_Teleport_Lift", "click" : "rich_hotel_reception_teleport", "xpos" : 1219, "ypos" : 110, "zorder":11, "teleport":True}, scene="rich_hotel_reception")
    $ add_object_to_scene("Door", {"type":2, "base":"Rich_Hotel_Reception_Door_Corridor", "click" : "rich_hotel_reception_environment", "actions" : "lw", "b":0.15, "zorder" : 1}, scene="rich_hotel_reception")
    return

label rich_hotel_reception_teleport:
    if obj_name == "Teleport_Street_Rich_Hotel":
        call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_331
        return
    if obj_name == "Teleport_Restaurant":
        call change_scene("rich_hotel_restaurant_entrance", "Fade_long") from _call_change_scene_332
        return
    if obj_name == "Teleport_Lift":
        call change_scene("rich_hotel_lift", "Fade_long") from _rcall_change_scene_59
        return

    return
label rich_hotel_reception_environment:
    if obj_name == "Clocks":
        mt "Часы..."
        "Нью-Йорк, Токио, Лондон..."
    if obj_name == "Door":
        mt "Какая-то дверь за рецепшином."
    if obj_name == "Flowers":
        mt "Цветы... Похоже искусственные. Но я не буду трогать их чтобы проверить."
    if obj_name == "Jug1" or obj_name == "Jug2":
        mt "Кувшин. На вид недорогой."
    if obj_name == "Tea":
        mt "Чайник. Как я соскучилась по горячему чаю!"
    if obj_name == "Desk":
        mt "Стойка Администратора."
    if obj_name == "Chair":
        mt "Стул..."
    if obj_name == "Monica":
        mt "Это далеко, далеко не самый лучше ресторан где Я была..."
        mt "Но сейчас он кажется мне раем..."
    if obj_name == "ReceptionGirl":
        if obj_data["action"] == "l":
            if monicaBitch == True:
                mt "Сучка!"
                "Тварь!"
                "НЕНАВИЖУ!!!"
                "Я УВОЛЮ ЕЕ, КЛЯНУСЬ!!!"
            else:
                mt "Она все время смотрит на меня с подозрением..."
                return
        if obj_data["action"] == "t":
            if monicaBitch == True:
                mt "Я не собираюсь общаться с этой сучкой!"
            else:
                mt "Я не хочу к ней подходить!"
                return

    return
