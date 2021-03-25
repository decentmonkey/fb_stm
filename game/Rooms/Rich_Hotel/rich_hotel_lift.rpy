default richHotelLiftMonicaSuffix = 1
default richHotelLiftSceneSuffix = "" # default lift open
default richHotelListVisitor3Suffix = 1
default richHotelListVisitor2Suffix = 1

label rich_hotel_lift:
    $ print "enter_rich_hotel_lift"
    $ miniMapData = []
    $ scene_image = "scene_RichHotel_Lift[richHotelLiftSceneSuffix]"

    music Groove2_85
    return

label rich_hotel_lift_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "RichHotel_Lift_Monica_[cloth]_[richHotelLiftMonicaSuffix]", "click" : "rich_hotel_lift_environment", "actions" : "l", "zorder":10}, scene="rich_hotel_lift")
    $ add_object_to_scene("EscortCustomer1", {"type" : 2, "base" : "RichHotel_Lift_EscortCustomer1", "click" : "rich_hotel_lift_environment", "actions" : "l", "b":0.15, "zorder":9, "active":False}, scene="rich_hotel_lift")

    $ add_object_to_scene("Lift", {"type" : 2, "base" : "RichHotel_Lift_TeleportLift", "click" : "rich_hotel_lift_environment", "actions" : "lw", "b":0.15, "zorder":1}, scene="rich_hotel_lift")

    $ add_object_to_scene("Teleport_Reception", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "rich_hotel_lift_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="rich_hotel_lift")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_lift_init2:
    $ add_object_to_scene("Visitor3", {"type" : 2, "base" : "RichHotel_Lift_Visitor3_[richHotelListVisitor3Suffix]", "click" : "rich_hotel_lift_environment", "actions" : "l", "b":0.15, "zorder":9, "active":False}, scene="rich_hotel_lift")
    return

label rich_hotel_lift_init3:
    $ add_object_to_scene("Visitor2", {"type" : 2, "base" : "Rich_Hotel_Lift_Visitor2_[richHotelListVisitor2Suffix]", "click" : "rich_hotel_lift_environment", "actions" : "lt", "b":0.15, "zorder":9, "active":False}, scene="rich_hotel_lift")
    return

label rich_hotel_lift_teleport:
    if obj_name == "Teleport_Reception":
        call change_scene("rich_hotel_reception", "Fade_long") from _rcall_change_scene_60
    return
label rich_hotel_lift_environment:
    if obj_name == "Monica":
        call ep211_escort_scene1_11() from _rcall_ep211_escort_scene1_11

    if obj_name == "Lift":
        if act=="l":
            call ep211_escort_scene1_12() from _rcall_ep211_escort_scene1_12
            return
        call ep211_escort_scene1_13() from _rcall_ep211_escort_scene1_13_2
        return
    return
