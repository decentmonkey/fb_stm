label rich_hotel_event_sittable:
    $ print "rich_hotel_event_sittable"
    $ miniMapData = []

    $ scene_image = "scene_rich_hotel_event_sittable_Philip_Monica"
    return

label rich_hotel_event_sittable_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_sittable_Monica", "click" : "rich_hotel_event_sittable_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Philip", {"type" : 2, "base" : "rich_hotel_event_sittable_Philip", "click" : "rich_hotel_event_sittable_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Drinks", {"type" : 2, "base" : "rich_hotel_event_sittable_Drinks", "click" : "rich_hotel_event_sittable_environment", "actions" : "l", "zorder":0})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_sittable_teleport:
    return
label rich_hotel_event_sittable_environment:
    if obj_name == "Monica":
        mt "Этот вечер нравится мне все больше..."
        return
    if obj_name == "Philip":
        if act == "l":
            mt "Мне надо как-то использовать этого мужчину..."
            "Не зря же я согласилась посидеть с ним!"
            return
        if act == "t":
            return


    if obj_name == "Drinks":
        mt "Судя по виду, это вино очень дорогое..."
        return
    return
