default richHotelRestaurantMonicaSuffix = 1
default richHotelRestaurantSceneSuffix = ""

default richHotelRestaurantVisitor1Suffix = ""
default richHotelRestaurantVisitor2Suffix = ""
default richHotelRestaurantVisitor3Suffix = ""
default richHotelRestaurantVisitor4Suffix = ""
default richHotelRestaurantVisitor5Suffix = ""

label rich_hotel_restaurant:
    $ print "enter_rich_hotel_restaurant"
    $ miniMapData = []
    $ scene_image = "scene_RichHotel_Restaurant[richHotelRestaurantSceneSuffix]"

    music Poppers_and_Prosecco
    return

label rich_hotel_restaurant_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "RichHotel_Restaurant_Monica_[cloth]_[richHotelRestaurantMonicaSuffix]", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder":16}, scene="rich_hotel_restaurant")

    $ add_object_to_scene("Visitor1", {"type" : 2, "base" : "RichHotel_Restaurant_Visitor1[richHotelRestaurantVisitor1Suffix]", "click" : "rich_hotel_restaurant_environment", "actions" : "lw", "b":0.15, "zorder":2}, scene="rich_hotel_restaurant")
    $ add_object_to_scene("Visitor2", {"type" : 2, "base" : "RichHotel_Restaurant_Visitor2[richHotelRestaurantVisitor2Suffix]", "click" : "rich_hotel_restaurant_environment", "actions" : "lw", "b":0.15, "zorder":1}, scene="rich_hotel_restaurant")
    $ add_object_to_scene("Visitor3", {"type" : 2, "base" : "RichHotel_Restaurant_Visitor3[richHotelRestaurantVisitor3Suffix]", "click" : "rich_hotel_restaurant_environment", "actions" : "lw", "b":0.15, "zorder":1}, scene="rich_hotel_restaurant")
    $ add_object_to_scene("Visitor4", {"type" : 2, "base" : "RichHotel_Restaurant_Visitor4[richHotelRestaurantVisitor4Suffix]", "click" : "rich_hotel_restaurant_environment", "actions" : "lw", "b":0.15, "zorder":1}, scene="rich_hotel_restaurant")
    $ add_object_to_scene("Visitor5", {"type" : 2, "base" : "RichHotel_Restaurant_Visitor5[richHotelRestaurantVisitor5Suffix]", "click" : "rich_hotel_restaurant_environment", "actions" : "lw", "b":0.15, "zorder":2}, scene="rich_hotel_restaurant")

    $ add_object_to_scene("MonicaTable", {"type" : 2, "base" : "Rich_Hotel_Restaurant_MonicaTable1", "click" : "rich_hotel_restaurant_environment", "b":0.15, "actions" : "l", "zorder":2}, scene="rich_hotel_restaurant")

    $ add_object_to_scene("Teleport_Reception", {"type":3, "text" : t_("ВЫХОД"), "larrow" : "arrow_left_2", "base":"RichHotel_Restaurant_TeleportReception", "click" : "rich_hotel_restaurant_teleport", "xpos" : 752, "ypos" : 114, "zorder":1, "teleport":True}, scene="rich_hotel_restaurant")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_restaurant_teleport:
    if obj_name == "Teleport_Reception":
        call change_scene("rich_hotel_reception", "Fade_long") from _rcall_change_scene_58
    return
label rich_hotel_restaurant_environment:
    if obj_name == "Monica":
        call ep211_escort_scene1_9() from _rcall_ep211_escort_scene1_9
    if obj_name == "Visitor1":
        call ep211_escort_scene1_10() from _rcall_ep211_escort_scene1_10
    if obj_name == "Visitor2":
        call ep211_escort_scene1_10() from _rcall_ep211_escort_scene1_10_1
    if obj_name == "Visitor3":
        call ep211_escort_scene1_10() from _rcall_ep211_escort_scene1_10_2
    if obj_name == "Visitor4":
        call ep211_escort_scene1_10() from _rcall_ep211_escort_scene1_10_3
    if obj_name == "Visitor5":
        call ep211_escort_scene1_10() from _rcall_ep211_escort_scene1_10_4

    if obj_name == "MonicaTable":
        pass
    return
