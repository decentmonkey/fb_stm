label Ralph_Life_init:
    $ add_hook("change_time_day", "Ralph_Life_day", scene="global")
    $ add_hook("change_time_evening", "Ralph_Life_evening", scene="global")
    $ add_hook("Ralph_Life_day", "Ralph_Life_day1", scene="global")
    $ add_hook("Ralph_Life_evening", "Ralph_Life_evening1", scene="global")

    if ralphAskedAboutPayment == False:
        $ add_hook("Ralph", "ralphDialogue2", scene="living_room", priority=200)
#    $ add_hook("Ralph", "ralphInteract1", scene="living_room", priority=200)
    return

label Ralph_Life_day:
    call process_hooks("Ralph_Life_day", "global") from _call_process_hooks_2
    return True


label Ralph_Life_evening:
    call process_hooks("Ralph_Life_evening", "global") from _call_process_hooks_3
    return True

label Ralph_Life_day1:
    if ralphAskedAboutPayment == False:
        $ move_object("Ralph", "living_room")
    return

    $ rnd = rand(1,2)
    if rnd == 1:
        $ move_object("Ralph", "empty")
    if rnd == 2:
        $ move_object("Ralph", "living_room")
#    $ move_object("biff", "empty")
    return

label Ralph_Life_evening1:
#    $ move_object("biff", "monica_office_cabinet")
    if ralphAskedAboutPayment == False:
        $ move_object("Ralph", "empty") #рендеры только дневные
        return
    $ move_object("Ralph", "living_room")
    return

label Ralph_Life_Monica_Cleaning_Start:
    return

label Ralph_Life_Monica_Cleaning_End:
    return

label Ralph_Life_Ask_About_Payment:
    if ralphAskedAboutPayment == True:
        $ remove_hook()
        return
    if get_active_objects("Ralph") != False:
        mt "Надо узнать у Ральфа по поводу моей оплаты."
    return
