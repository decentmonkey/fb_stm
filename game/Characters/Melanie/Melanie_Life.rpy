default Melanie_Life_evening2_skip_once = False

label Melanie_Life_init:
    $ add_hook("change_time_day", "Melanie_Life_day", scene="global")
    $ add_hook("change_time_evening", "Melanie_Life_evening", scene="global")
    $ add_hook("Melanie_Life_day", "Melanie_Life_day1", scene="global")
    $ add_hook("Melanie_Life_evening", "Melanie_Life_evening1", scene="global")
    return

label Melanie_Life_day:
    call process_hooks("Melanie_Life_day", "global") from _call_process_hooks_4
    return True

label Melanie_Life_evening:
    call process_hooks("Melanie_Life_evening", "global") from _call_process_hooks_5
    return True

label Melanie_Life_day1: #Днем Мелани в студии
    $ move_object("Melanie", "monica_office_photostudio")
    return

label Melanie_Life_day2: #Днем Мелани в гримерке
    $ move_object("Melanie", "monica_office_makeup_room")
    return False

label Melanie_Life_evening1:
    $ move_object("Melanie", "empty")
    return

label Melanie_Life_evening2: #Вечером Мелани в гримерке
    if Melanie_Life_evening2_skip_once == True:
        $ Melanie_Life_evening2_skip_once = False
        return False
    $ move_object("Melanie", "monica_office_makeup_room")
    return False

label Melanie_Life_disappeared: # Мелани нигде нет
    $ move_object("Melanie", "empty")
    return False
