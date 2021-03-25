label Fred_Life_init:
    $ add_hook("change_time_day", "Fred_Life_day", scene="global")
    $ add_hook("change_time_evening", "Fred_Life_evening", scene="global")
    $ add_hook("Fred_Life_day", "Fred_Life_day1", scene="global")
    $ add_hook("Fred_Life_evening", "Fred_Life_evening1", scene="global")
    return

label Fred_Life_day:
    call process_hooks("Fred_Life_day", "global") from _call_process_hooks_8
    return True


label Fred_Life_evening:
    call process_hooks("Fred_Life_evening", "global") from _call_process_hooks_9
    return True

label Fred_Life_day1:
#    $ move_object("biff", "empty")
    $ move_object("Driver", "street_house_main_yard") 
    return

label Fred_Life_evening1:
#    $ move_object("biff", "monica_office_cabinet")
    return


label Fred_Life_Monica_Cleaning_Start:
    return

label Fred_Life_Monica_Cleaning_End:
    return
