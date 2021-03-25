label Dick_Life_init:
    $ add_hook("change_time_day", "Dick_Life_day", scene="global")
    $ add_hook("change_time_evening", "Dick_Life_evening", scene="global")
    $ add_hook("Dick_Life_day", "Dick_Life_day1", scene="global")
    $ add_hook("Dick_Life_evening", "Dick_Life_evening1", scene="global")
    return

label Dick_Life_day:
    call process_hooks("Dick_Life_day", "global") from _call_process_hooks_34
    return True


label Dick_Life_evening:
    call process_hooks("Dick_Life_evening", "global") from _call_process_hooks_37
    return True

label Dick_Life_day1:
    $ move_object("DickTheLawyer", "dick_office_cabinet")
    return

label Dick_Life_evening1:
    $ move_object("DickTheLawyer", "dick_office_cabinet")
    return

label Dick_Life_evening2: #Дика нет по вечерам
    $ move_object("DickTheLawyer", "empty")
    return False
