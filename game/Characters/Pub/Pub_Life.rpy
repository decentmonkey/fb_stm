label Pub_Life_init: # Первое время, когда Моника только обнаруживает бар. Много народа
    $ add_hook("change_time_day", "Pub_Life_day", scene="global")
    $ add_hook("change_time_evening", "Pub_Life_evening", scene="global")
    $ add_hook("Pub_Life_day", "Pub_Life_day1", scene="global", label="pub_life")
    $ add_hook("Pub_Life_evening", "Pub_Life_evening1", scene="global", label="pub_life")

    # Сразу наполняем бар
    if day_time == "day":
        call Pub_Life_day() from _call_Pub_Life_day
    else:
        call Pub_Life_evening() from _call_Pub_Life_evening
    return

label Pub_Life2_init: # Обычное наполнение бара
    $ remove_hook(label="pub_life")
    $ add_hook("Pub_Life_day", "Pub_Life_day2", scene="global", label="pub_life")
    $ add_hook("Pub_Life_evening", "Pub_Life_evening2", scene="global", label="pub_life")
    return

label Pub_Life_day:
    call process_hooks("Pub_Life_day", "global") from _call_process_hooks_32
    return True

label Pub_Life_evening:
    call process_hooks("Pub_Life_evening", "global") from _call_process_hooks_33
    return True

label Pub_Life_day1: # Первое время, когда Моника только обнаруживает бар. Много народа
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", True, scene="pub")
    call Pub_Visitors_RemoveAll() from _call_Pub_Visitors_RemoveAll
    call Pub_Visitors_Add_Random(3,5) from _call_Pub_Visitors_Add_Random
    call Pub_Visitors_Full_Food() from _call_Pub_Visitors_Full_Food # у всех еда
    $ set_active("Pub_Visitor1", True, scene="pub") # эти посетители есть на кадре
    $ set_active("Pub_Visitor11", True, scene="pub")
    $ set_active("Pub_Visitor6", True, scene="pub")
    call Pub_Visitors_CheckStripLooking() from _call_Pub_Visitors_CheckStripLooking # Если есть стриптизерши, то смотрят, иначе нет
    return
label Pub_Life_evening1:
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", True, scene="pub")

    call Pub_Visitors_RemoveAll() from _call_Pub_Visitors_RemoveAll_1
    call Pub_Visitors_Add_Random(5,7) from _call_Pub_Visitors_Add_Random_1
    call Pub_Visitors_Full_Food() from _call_Pub_Visitors_Full_Food_1 # Все посетители + у всех еда
    $ set_active("Pub_Visitor1", True, scene="pub") # эти посетители есть на кадре
    $ set_active("Pub_Visitor11", True, scene="pub")
    $ set_active("Pub_Visitor6", True, scene="pub")
    call Pub_Visitors_CheckStripLooking() from _call_Pub_Visitors_CheckStripLooking_1 # Если есть стриптизерши, то смотрят, иначе нет
    return


label Pub_Life_day2: # Обычное наполнение бара, все с едой
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", False, scene="pub")
    call Pub_Visitors_RemoveAll() from _call_Pub_Visitors_RemoveAll_2
    call Pub_Visitors_Add_Random(2,4) from _call_Pub_Visitors_Add_Random_2
    if pubMonicaWorkingWaitress == True and pubMonicaWorkedWaitressLastDay != day:
        call Pub_Visitors_Remove_Food() from _call_Pub_Visitors_Remove_Food # убираем еду у всех
    else:
        call Pub_Visitors_Full_Food() from _call_Pub_Visitors_Full_Food_2 # у всех еда
    call Pub_Visitors_CheckStripLooking() from _call_Pub_Visitors_CheckStripLooking_2 # Если есть стриптизерши, то смотрят, иначе нет
    return
label Pub_Life_evening2:
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", False, scene="pub")
    if day%2 == 0:
        $ set_active("Pub_StripteaseGirl1", True, scene="pub")
    else:
        $ set_active("Pub_StripteaseGirl2", True, scene="pub")

    call Pub_Visitors_RemoveAll() from _call_Pub_Visitors_RemoveAll_3
    call Pub_Visitors_Add_Random(5,7) from _call_Pub_Visitors_Add_Random_3
    if pubMonicaWorkingWaitress == True and pubMonicaWorkedWaitressLastDay != day:
        call Pub_Visitors_Remove_Food() from _call_Pub_Visitors_Remove_Food_1 # убираем еду у всех
    else:
        call Pub_Visitors_Full_Food() from _call_Pub_Visitors_Full_Food_3 # Все посетители + у всех еда
    call Pub_Visitors_CheckStripLooking() from _call_Pub_Visitors_CheckStripLooking_3 # Если есть стриптизерши, то смотрят, иначе нет
    return
