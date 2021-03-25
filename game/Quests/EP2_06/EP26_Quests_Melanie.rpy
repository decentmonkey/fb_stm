label ep26_quests_melanie1:
    # возвращение Мелани
    $ melanieDisappeared = False
    $ melanieDisappearedAndReturned = True
#    $ add_hook("change_time_day", "ep26_quests_melanie1a", scene="global")
#    $ remove_hook()
    $ add_hook("Melanie_Life_evening", "Melanie_Life_evening2", scene="global", label="melanie_makeuproom_life")
    $ remove_hook(label="melanie_disappeared_life")
    $ add_hook("Melanie", "ep26_quests_melanie2", scene="monica_office_makeup_room", label="melanie_returned_dialogue1")
    $ makeupRoomMelanieSuffix = 2
    call Melanie_Life_evening2() from _call_Melanie_Life_evening2
    return

#label ep26_quests_melanie1a:
#    # с утра инициализируем хуки появление Мелани
#    $ remove_hook()
#    $ add_hook("Melanie_Life_evening", "Melanie_Life_evening2", scene="global", label="melanie_makeuproom_life")
#    $ remove_hook(label="melanie_disappeared_life")
#    $ add_hook("Melanie", "ep26_quests_melanie2", scene="monica_office_makeup_room", label="melanie_returned_dialogue1")
#    $ makeupRoomMelanieSuffix = 2
#    call Melanie_Life_day2()
#    return


label ep26_quests_melanie2:
    # Разговор с Мелани
    if act=="l":
        return
    call ep26_dialogues7_melanie1() from _call_ep26_dialogues7_melanie1
    call ep27_quests_melanie1_init() from _call_ep27_quests_melanie1_init_1
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_12
    return False
