default richHotelRestaurantEntranceMonicaSuffix = 1
default richHotelRestaurantEntranceWaitressSuffix = ""
default richHotelRestaurantEntranceV3Suffix = ""

default richHotelRestaurantEntranceSkipMusicOnce = False

label rich_hotel_restaurant_entrance:
    $ print "enter_rich_hotel_restaurant_entrance"
    $ miniMapData = []

    $ scene_image = "scene_rich_hotel_restaurant_entrance"

    if richHotelRestaurantEntranceSkipMusicOnce == False:
        music Poppers_and_Prosecco
    $ richHotelRestaurantEntranceSkipMusicOnce = False
    return

label rich_hotel_restaurant_entrance_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Rich_Hotel_Restaurant_Entrance_Monica[richHotelRestaurantEntranceMonicaSuffix]_[cloth]", "click" : "rich_hotel_restaurant_entrance_environment", "actions" : "l", "zorder":10}, scene="rich_hotel_restaurant_entrance")
    $ add_object_to_scene("Waitress", {"type" : 2, "base" : "Rich_Hotel_Restaurant_Entrance_Waitress_[richHotelRestaurantEntranceWaitressSuffix]", "click" : "rich_hotel_restaurant_entrance_environment", "actions" : "lt", "zorder":9}, scene="rich_hotel_restaurant_entrance")

    $ add_object_to_scene("RestaurantVisitor3", {"type" : 2, "base" : "Rich_Hotel_Restaurant_Entrance_v3[richHotelRestaurantEntranceV3Suffix]", "click" : "rich_hotel_restaurant_entrance_environment", "actions" : "lt", "zorder":7}, scene="rich_hotel_restaurant_entrance")

    $ add_object_to_scene("Teleport_Reception", {"type":3, "text" : t_("РЕЦЕПШИН"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "rich_hotel_restaurant_entrance_teleport", "xpos" : 220, "ypos" : 795, "zorder":11, "teleport":True}, scene="rich_hotel_restaurant_entrance")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_restaurant_entrance_teleport:
    if obj_name == "Teleport_Reception":
        $ richHotelReceptionMonicaSuffix = 2
        $ richHotelReceptionReceptionSuffix = 2
        call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_339
        return
    return
label rich_hotel_restaurant_entrance_environment:
    if obj_name == "Monica":
        mt "Вот и ресторан.
        Куда меня приводил Дик..."
    if obj_name == "RestaurantVisitor3":
        if act=="l":
            mt "Почему эта девушка так на меня смотрит?"
        if act == "t":
            mt "Мне не о чем с ней говорить. С какой стати?"
    if obj_name == "Waitress":
        if act == "l":
            if waitressMonicaOffended1 == True:
                mt "А, это та дура, которая не могла принести нам еду вовремя..."
                if waitressMonicaFired == True:
                    mt "Ведь Дик ее должен был ее уволить..."
                    mt "Мерзавец..."
            else:
                mt "Это та официантка, которая работает без выходных..."
            return
    return
