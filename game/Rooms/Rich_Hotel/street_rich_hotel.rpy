label street_rich_hotel:
    $ print "enter_street_rich_hotel"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Rich_Hotel[day_suffix]"
    if day_time == "day":
        music rich_hotel_park
    else:
        music street_evening4
    return

label street_rich_hotel_init:
    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})
    $ add_object_to_scene("Building", {"type":2, "base":"Street_Rich_Hotel_Building", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "group":"environment"})
    $ add_object_to_scene("Teleport_Rich_Hotel_Reception", {"type":2, "base":"Street_Rich_Hotel_Teleport_Inside", "click" : "street_rich_hotel_teleport", "actions" : "lw", "zorder" : 3, "b":0.17, "c":1.5, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_rich_hotel_teleport:
    if obj_name == "Teleport_Rich_Hotel_Reception":
        if obj_data["action"] == "l":
            mt "Вход в отель..."
            return
        if obj_data["action"] == "w":
#            $ cloth_type = "PhotoDress"
#            $ cloth = "PhotoDress"
#            call change_scene("rich_hotel_event_sittable")
#            return
            if cloth == "CasualDress1":
#                help "Будет доступно в следующем обновлении игры. Следите за новостями!"
                call ep26_quests_restaurant1() from _call_ep26_quests_restaurant1
                return
            mt "Я еще не сошла с ума, чтобы идти в такой дорогой отель одетой в ЭТО!!!"
            if charityEventCompleted == True:
                mt "Я доказала этой сучке на рецепшине что Я - ЛЕДИ!"
                "И не хочу портить впечатление."
            return
            call change_scene("rich_hotel_reception") from _call_change_scene_108
        return
    return
label street_rich_hotel_environment:
    if obj_name == "Building":
        m "Это и есть Hotel Le Grand?"
        if day_time == "evening":
            m "Вечером он выглядит довольно эффектно."
        else:
            m "Днем он тоже выглядит неплохо."
        m "Это не небоскреб, в нем нет какого-то величия."
        "Но смотрится он очень мило."
        "По крайней мере это не дыра!...
        На вид..."

    if obj_name == "Logo":
        m "Le Grand?"
        "Как банально..."
    return
