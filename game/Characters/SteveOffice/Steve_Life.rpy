label Steve_Life_init:
    $ add_hook("change_time_day", "Steve_Life_day", scene="global")
    $ add_hook("change_time_evening", "Steve_Life_evening", scene="global")
    $ add_hook("Steve_Life_day", "Steve_Life_Day1", scene="global")
    $ add_hook("Steve_Life_evening", "Steve_Life_Evening1", scene="global")
    call Steve_Life_Day1() from _call_Steve_Life_Day1
    return

label Steve_Life_day:
    call process_hooks("Steve_Life_day", "global") from _call_process_hooks_58
    return True

label Steve_Life_evening:
    call process_hooks("Steve_Life_evening", "global") from _call_process_hooks_59
    return True


label Steve_Life_Day1:
    # Если деньги для Виктории заработаны, то Стива нет
    # Иначе он на месте
    if monicaEarnedWeeklyMoney == True and week_day != 6: # В субботу Стив всегда на месте
        $ move_object("Steve", "empty")
        return
    $ move_object("Steve", "steve_office_office_table")
    return

label Steve_Life_Evening1:
    # Вечером Стива нет
    $ move_object("Steve", "empty")
    return
