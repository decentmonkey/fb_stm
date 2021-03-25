label Betty_Life_init:
    $ add_hook("change_time_day", "Betty_Life_day", scene="global")
    $ add_hook("change_time_evening", "Betty_Life_evening", scene="global")
    $ add_hook("Betty_Life_day", "Betty_Life_day1", scene="global")
    $ add_hook("Betty_Life_evening", "Betty_Life_evening1", scene="global")

    $ add_hook("Betty", "Betty_Life_Dialogue_Floor2", scene="floor2")
    $ add_hook("Betty", "Betty_Life_Dialogue_Bedroom1", scene="bedroom1")
    return

label Betty_Life_day:
    call process_hooks("Betty_Life_day", "global") from _call_process_hooks_17
    return True


label Betty_Life_evening:
    call process_hooks("Betty_Life_evening", "global") from _call_process_hooks_18
    return True

label Betty_Life_day1:
    call bettyGetTodayPanties() from _call_bettyGetTodayPanties_1
    $ bedroom1_betty_suffix = ""
#    $ move_object("biff", "empty")
    $ rnd = rand(1,3)
    if rnd == 1 or rnd == 2:
        $ move_object("Betty", "floor2")
    if rnd == 3:
        $ move_object("Betty", "bedroom1")

    if get_active_objects("Bardie", scene="bedroom1") != False:
        $ move_object("Betty", "bedroom1")
    return

label Betty_Life_day2: #Бетти чаще бывает в спальне
    call bettyGetTodayPanties() from _call_bettyGetTodayPanties_3
    $ bedroom1_betty_suffix = ""
    $ rnd = rand(1,3)
    if rnd == 3:
        $ move_object("Betty", "floor2")
    if rnd == 1 or rnd == 2:
        $ move_object("Betty", "bedroom1")

    if get_active_objects("Bardie", scene="bedroom1") != False:
        $ move_object("Betty", "bedroom1")
    return

label Betty_Life_day1_lower:
    $ move_object("Betty", "floor2")
    return

label Betty_Life_evening1:
#    $ move_object("biff", "monica_office_cabinet")
    $ bedroom1_betty_suffix = bettyPantiesCurrent
    if bettyPantiesCurrent == 0:
        $ bedroom1_betty_suffix = bettyPantiesLog[0]
    $ move_object("Betty", "bedroom1")
    #bedroom1_betty_suffix
    return

label Betty_Life_Monica_Cleaning_Start:
    return

label Betty_Life_Monica_Cleaning_End:
    return

label Betty_Life_Dialogue_Floor2:
    if act == "t":
        if cloth_type == "Governess":
            call cleaning_betty_comment1() from _call_cleaning_betty_comment1
        else:
            call bettyDialogue3() from _call_bettyDialogue3
        return False
    return

label Betty_Life_Dialogue_Bedroom1:
    if act == "t":
        if day_time == "day":
            if cloth_type == "Governess":
                call bettyDialogue1() from _call_bettyDialogue1_1
            else:
                call bettyDialogue3() from _call_bettyDialogue3_1
            return False
        if day_time == "evening":
            call bettyDialogue2() from _call_bettyDialogue2
            return False
    return

label Betty_Life_none:
    # Бетти нигде нет
    $ move_object("Betty", "empty")
    return False
