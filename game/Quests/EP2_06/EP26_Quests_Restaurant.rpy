default ep26_quests_restaurant_inited = False
default richHotelSuccessfullyPassedDay = 0
default richHotelMonicaEatedDay = 0

default restaurantFoodHistory = []

label ep26_quests_restaurant1:
    # Вход в ресторан
    if ep26_quests_restaurant_inited == False:
        # Инициализируем локации, если не сделано
        $ ep26_quests_restaurant_inited = True
        call locations_init_rich_hotel_restaurant() from _call_locations_init_rich_hotel_restaurant
        if waitressMonicaOffended1 == True:
            $ richHotelRestaurantEntranceWaitressSuffix = "Angry"
        else:
            $ richHotelRestaurantEntranceWaitressSuffix = "Smile"
        $ add_hook("Teleport_Restaurant", "ep26_quests_restaurant2", scene="rich_hotel_reception", label="reception_capturing_monica")
        $ add_hook("Waitress", "ep26_quests_restaurant3", scene="rich_hotel_restaurant_entrance", label="restaurant_waitress_dialogue")

    if richHotelMonicaEatedDay == day:
        call ep26_dialogues4_restaurant5() from _call_ep26_dialogues4_restaurant5
        return False
    $ richHotelReceptionMonicaSuffix = 1
    $ richHotelReceptionReceptionSuffix = 1
    call change_scene("rich_hotel_reception", "Fade_long", "snd_door_bell1") from _call_change_scene_340

    return

label ep26_quests_restaurant2:
    # Рецепшин перехватывает Монику при входе в ресторан
    if richHotelMonicaEatedDay == day:
        call ep26_dialogues4_restaurant5() from _call_ep26_dialogues4_restaurant5_1
        return False
    if monicaMadeBlowjobToPhilip == True: # рецепшин видела Монику, делающую blowjob
        if richHotelSuccessfullyPassedDay != day:
            call ep26_dialogues4_restaurant1() from _call_ep26_dialogues4_restaurant1
            if _return == False:
                music Groove2_85
    #            $ richHotelReceptionSkipMusicOnce = True
    #            $ richHotelReceptionMonicaSuffix = 2
    #            $ richHotelReceptionReceptionSuffix = 2
                $ autorun_to_object("ep26_dialogues4_restaurant1a", scene="street_rich_hotel")
                call change_scene("street_rich_hotel", "Fade_long", "snd_door_bell1") from _call_change_scene_341
                return False
        $ richHotelSuccessfullyPassedDay = day
        return True
    else:
        if richHotelSuccessfullyPassedDay != day:
            call ep26_dialogues4_restaurant2() from _call_ep26_dialogues4_restaurant2
        $ richHotelSuccessfullyPassedDay = day
    return True

label ep26_quests_restaurant3:
    if act=="l":
        return
    # Общение с официанткой, заказ блюд
    if waitressMonicaOffended1 == True:
        # Если Моника ругалась на официантку
        call ep26_dialogues4_restaurant3() from _call_ep26_dialogues4_restaurant3
        if _return == True:
            $ richHotelMonicaEatedDay = day
            call monicaEat() from _call_monicaEat_15
        $ richHotelReceptionMonicaSuffix = 2
        $ richHotelReceptionReceptionSuffix = 2
        if restaurant_block_return_flag_once == False:
            call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_342
        $ restaurant_block_return_flag_once = False
    else:
        # Если Моника помогла официантке
        call ep26_dialogues4_restaurant4() from _call_ep26_dialogues4_restaurant4
        if _return == True:
            $ richHotelMonicaEatedDay = day
            call monicaEat() from _call_monicaEat_16
        $ richHotelReceptionMonicaSuffix = 2
        $ richHotelReceptionReceptionSuffix = 2
        if restaurant_block_return_flag_once == False:
            call change_scene("rich_hotel_reception", "Fade_long") from _call_change_scene_343
        $ restaurant_block_return_flag_once = False
    return
