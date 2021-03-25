default bardieStage = 0

default Bardie_Life_day5_day = 0

default bardieDayEmpty = False # днем Барди нет

label Bardie_Life_init:
    $ add_hook("change_time_day", "Bardie_Life_day", scene="global")
    $ add_hook("change_time_evening", "Bardie_Life_evening", scene="global")
    $ add_hook("Bardie_Life_day", "Bardie_Life_Day1", scene="global")
    $ add_hook("Bardie_Life_evening", "Bardie_Life_evening1", scene="global")

    return

label Bardie_Life_day:
    $ move_object("Bardie", "empty")
#    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_6
    return True

label Bardie_Life_Day1:
#    $ move_object("biff", "empty")
    $ move_object("Bardie", "empty")
    return
#    if bardieStage == 0:
    $ rand1 = rand(1,2)
    if rand1 == 1:
        $ move_object("Bardie", "street_house_main_yard") #во дворе
    if rand1 == 2:
        $ move_object("Bardie", "bedroom_bardie") #в своей комнате

    return

label Bardie_Life_evening:
    $ move_object("Bardie", "empty")
    return True
    call process_hooks("Bardie_Life_evening", "global") from _call_process_hooks_7
    return True

label Bardie_Life_evening1:
    $ move_object("Bardie", "empty")
    return
#    $ move_object("biff", "monica_office_cabinet")
    if bardieStage == 0:
        $ move_object("Bardie", "bedroom_bardie")
    return

label Bardie_Life_evening2: #Барди вечером преследует Монику у лестницы
    $ move_object("Bardie", "empty")
    return False
    $ move_object("Bardie", "floor1_stairs")
    return False

label Bardie_Life_Monica_Cleaning_Start:
    $ move_object("Bardie", "empty")
    return
    if bardieFollowMonicaDuringCleaning == True:
        if "bedroom_bardie" in rooms_dirty:
            $ move_object("Bardie", "bedroom_bardie")
            return
        if "floor1" in rooms_dirty:
            $ move_object("Bardie", "floor1")
            return
        if "bedroom_second" in rooms_dirty:
            $ move_object("Bardie", "bedroom_second")
            return

    return

label Bardie_Life_Monica_Cleaning_End:
    $ move_object("Bardie", "empty")
    return
    call Bardie_Life_day() from _call_Bardie_Life_day
    return

label Bardie_Life_day2_init: #Барди нигде нет, кроме подвала
    $ move_object("Bardie", "empty")
    return
    $ add_hook("Bardie_Life_day", "Bardie_Life_day3", scene="global")
    $ add_hook("Bardie_Life_evening", "Bardie_Life_evening3", scene="global")
    return

label Bardie_Life_day3:
    $ move_object("Bardie", "empty")
    return False
label Bardie_Life_evening3:
    $ move_object("Bardie", "empty")
    return False

label Bardie_Life_day4:
    $ move_object("Bardie", "empty")
    return False
    $ move_object("Bardie", "bedroom_bardie")
    return False
label Bardie_Life_evening4:
    $ move_object("Bardie", "empty")
    return False
    $ move_object("Bardie", "bedroom_bardie")
    return False

label Bardie_Life_day5:
    $ move_object("Bardie", "empty")
    return False
    if bardieDayEmpty == True:
        $ move_object("Bardie", "empty")
        return False
    if day == Bardie_Life_day5_day or day%2 == 0:
        return
    if get_active_objects("Betty", scene="floor2") != False:
        $ move_object("Bardie", "floor2")
        return False
    if get_active_objects("Betty", scene="bedroom1") != False:
        $ move_object("Bardie", "bedroom1")
    return False

label Bardie_Life_Day6: # Днем Барди все время во дворе
    $ move_object("Bardie", "empty")
    return
    if bardieDayEmpty == True:
        $ move_object("Bardie", "empty")
        return False
    if day == Bardie_Life_day5_day or day%2 == 0:
        $ move_object("Bardie", "street_house_main_yard")
        return False
    return
