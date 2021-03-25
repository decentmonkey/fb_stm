default basement_monica_after_sleep_dialogue1_skip = True
default basementBedroomMonicaNapGfx = False
default basementBedroomMonicaNapGfxBettyPanties = False
default basementBedroomMonicaSleepGfx = False
default basementBedNapIndex = 0
default basementBedSleepIndex = 0

default basementBedSkipUntilFridayEnabled = False
default skipDaysInterrupted = False # Флаг того что надо заблокировать пропускание дней и проснуться
default skipDaysActiveFlag = False # В данный момент пропускаются дни (инфа для хуков)

default skipUntilFridayTargetDay = 5

default monicaRestApartments = False
default monicaRestApartmentsDay = 0
default monicaRestHouse = False
default monicaRestHouseDay = 0
default monicaRestJuliaHome = False
default monicaRestJuliaHomeDay = 0

label basement_bed_hook:
    if act == "l":
        return True
    if act == "h":
        $ set_rest_place("basement_bed")
        if day_time == "day":
            call monica_take_nap() from _call_monica_take_nap
            return _return
        if day_time == "evening":
            call monica_gosleep1() from _call_monica_gosleep1
            return _return
    return


label monica_wakeup1:
    #Моника встает с утра
    mt "Еще одно утро в этой дыре! Мне надо что-то придумать, чтобы вернуть все назад как было!"

    mt "Я не высыпаюсь на этой кровати."
    "Мне нужна нормальная постель!"

    mt "Такая королева как я не может привыкнуть спать в таких условиях!"
    "Я заслуживаю лучшего!"

    mt "Это мой дом! Я не заслуживаю того чтобы спать в подвале!"

    mt "Мне надо что-то придумать, чтобы вернуть все назад как было!"
    return

label monica_take_nap:
    if cloth == "CasualDress1":
        call ep25_dialgues5_basement2() from _call_ep25_dialgues5_basement2
        $ cloth_type = "Nude"
        if monicaUnder == "Nude":
            $ cloth = "Nude"
        else:
            $ cloth = "GovernessPants"
        $ monicaBettyPanties = False

    if cloth == "GovernessPants" and monicaBettyPanties == True:
        $ basementBedroomMonicaNapGfxBettyPanties = True
    if cloth == "Governess" and  monicaBettyPanties == True:
        $ basement_bedroom2_Monica_Nap_Betty_Suffix = "_Betty_" + str(monicaBettyPantiesId)
    $ basementBedroomMonicaNapGfx = True
    call basement_monica_nap_transition1() from _call_basement_monica_nap_transition1
    $ autorun_to_object("monica_take_nap1")
    return False
label monica_take_nap1:
    $ set_active("BasementBed", True, scene="basement_bedroom2")
    $ basement_bedroom2_MonicaSuffix = 2
    menu:
        "Лечь и ждать вечера.":
            $ basementBedroomMonicaNapGfx = False
            $ basementBedroomMonicaNapGfxBettyPanties = False
            $ basement_bedroom2_Monica_Nap_Betty_Suffix = ""
            img black_screen
            with Dissolve(0.2)
            #транзиция на отдых
            call process_hooks("basement_monica_before_nap", "global") from _call_process_hooks_29
            if _return == False:
                $ basement_bedroom2_MonicaSuffix = 2
                call refresh_scene_fade() from _call_refresh_scene_fade_43
                return False
            $ changeDayTime("evening")
            call process_hooks("basement_monica_after_nap", "global") from _call_process_hooks_30
            call refresh_scene_fade() from _call_refresh_scene_fade_44
            return False
        "Не ложиться.":
            $ basementBedroomMonicaNapGfx = False
            $ basementBedroomMonicaNapGfxBettyPanties = False
            $ basement_bedroom2_Monica_Nap_Betty_Suffix = ""
            call refresh_scene_fade() from _call_refresh_scene_fade_45
            return False
    return

label monica_gosleep1:
    #если Моника голодная
    if monicaBettyPanties == True:
        call ep22_dialogues3_13() from _call_ep22_dialogues3_13_4
        $ monicaBettyPanties = False
    if monicaEatedLastDay < day:
        if day - monicaEatedLastDay >= 3 and (monicaCantSleepHungry2 == True or debugMode == False) and debugMode == False:
            #если Моника не ела 3 дня
            $ autorun_to_object("basement_monica_hungry_cant_sleep")
            call refresh_scene_fade() from _call_refresh_scene_fade_46
            return False
        else:
            $ basement_bedroom2_MonicaSuffix = 2
            $ basementBedroomMonicaSleepGfx = True
            call basement_monica_sleep_transition1() from _call_basement_monica_sleep_transition1
            $ autorun_to_object("monica_gosleep1a")
            return False
    $ basementBedroomMonicaSleepGfx = True
    call basement_monica_sleep_transition1() from _call_basement_monica_sleep_transition1_1
    $ autorun_to_object("monica_gosleep1b")
    return False
label monica_gosleep1a:
    $ set_active("BasementBed", True, scene="basement_bedroom2")
    mt "Я сегодня ничего не ела! Лечь спать голодной?"
    menu:
        "Поесть и лечь спать." if food_basement_check_food_func() == True:
            $ sleepAfterEat = True
            call change_scene("basement_bedroom_table") from _call_change_scene_237
            return False
        "Лечь спать голодной.":
            img black_screen
            with Dissolve(0.2)
            call monica_process_sleep() from _call_monica_process_sleep
            return False
#            $ basementBedroomMonicaSleepGfx = False
#            call process_hooks("basement_monica_before_sleep", "global") from _call_process_hooks_31
#            if _return == False:
#                $ basement_bedroom2_MonicaSuffix = 2
#                call refresh_scene_fade() from _call_refresh_scene_fade_47
#                return False
#            call processHouseCleaningEvening() from _call_processHouseCleaningEvening
#            if cloth != "Nude":
#                $ cloth_type = "Nude"
#                $ cloth = "GovernessPants"
#            $ changeDayTime("day")
#            call process_hooks("basement_monica_after_sleep", "global") from _call_process_hooks_32
#            call refresh_scene_fade() from _call_refresh_scene_fade_48
#            return False
        "Пропустить до..." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
            menu:
                "Пропустить до Понедельника." if basementBedSkipUntilFridayEnabled == True and week_day > 5 and week_day < 7:
                    $ skipUntilFridayTargetDay = 1
                    jump basement_bed_skip_until_day1
                "Пропустить до Вторника." if basementBedSkipUntilFridayEnabled == True and (week_day > 5):
                    $ skipUntilFridayTargetDay = 2
                    jump basement_bed_skip_until_day1
                "Пропустить до Среды." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 2):
                    $ skipUntilFridayTargetDay = 3
                    jump basement_bed_skip_until_day1
                "Пропустить до Четверга." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 3):
                    $ skipUntilFridayTargetDay = 4
                    jump basement_bed_skip_until_day1
                "Пропустить до Пятницы." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
                    img black_screen
                    with Dissolve(0.2)
                    $ basementBedroomMonicaSleepGfx = False
                    $ skipUntilFridayTargetDay = 5
                    call monica_skip_until_friday() from _call_monica_skip_until_friday
                    return False
                "Не ложиться.":
                    $ basementBedroomMonicaSleepGfx = False
                    call refresh_scene_fade() from _rcall_refresh_scene_fade_32
                    return False
        "Не ложиться.":
            $ basementBedroomMonicaSleepGfx = False
            call refresh_scene_fade() from _call_refresh_scene_fade_49
            return False

label monica_gosleep1b:
    $ set_active("BasementBed", True, scene="basement_bedroom2")
    $ basement_bedroom2_MonicaSuffix = 2
    menu:
        "Лечь спать.":
            img black_screen
            with Dissolve(0.2)
            call monica_process_sleep() from _call_monica_process_sleep_1
            return False
#            $ basementBedroomMonicaSleepGfx = False
#            call process_hooks("basement_monica_before_sleep", "global") from _call_process_hooks_33
#            if _return == False:
#                $ basement_bedroom2_MonicaSuffix = 2
#                call refresh_scene_fade() from _call_refresh_scene_fade_50
#                return False
#            call processHouseCleaningEvening() from _call_processHouseCleaningEvening_1
#            if cloth != "Nude":
#                $ cloth_type = "Nude"
#                $ cloth = "GovernessPants"
#            $ changeDayTime("day")
#            call process_hooks("basement_monica_after_sleep", "global") from _call_process_hooks_34
#            call refresh_scene_fade() from _call_refresh_scene_fade_51
#            return False
        "Пропустить до..." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
            menu:
                "Пропустить до Понедельника." if basementBedSkipUntilFridayEnabled == True and week_day > 5 and week_day < 7:
                    $ skipUntilFridayTargetDay = 1
                    jump basement_bed_skip_until_day2
                "Пропустить до Вторника." if basementBedSkipUntilFridayEnabled == True and (week_day > 5):
                    $ skipUntilFridayTargetDay = 2
                    jump basement_bed_skip_until_day2
                "Пропустить до Среды." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 2):
                    $ skipUntilFridayTargetDay = 3
                    jump basement_bed_skip_until_day2
                "Пропустить до Четверга." if basementBedSkipUntilFridayEnabled == True and (week_day > 5 or week_day < 3):
                    $ skipUntilFridayTargetDay = 4
                    jump basement_bed_skip_until_day2
                "Пропустить до Пятницы." if basementBedSkipUntilFridayEnabled == True and week_day != 5 and week_day != 4:
                    $ basementBedroomMonicaSleepGfx = False
                    if cloth != "Nude":
                        $ cloth_type = "Nude"
                        if monicaUnder == "Nude":
                            $ cloth = "Nude"
                        else:
                            $ cloth = "GovernessPants"
                        $ monicaBettyPanties = False
                    img black_screen
                    with Dissolve(0.2)
                    $ skipUntilFridayTargetDay = 5
                    call monica_skip_until_friday() from _call_monica_skip_until_friday_1
                    return False
                "Не ложиться.":
                    $ basementBedroomMonicaSleepGfx = False
                    call refresh_scene_fade() from _rcall_refresh_scene_fade_33
                    return False
        "Не ложиться.":
            $ basementBedroomMonicaSleepGfx = False
            call refresh_scene_fade() from _call_refresh_scene_fade_52
            return False
    return False

label monica_process_sleep:
    $ basement_bedroom2_MonicaSuffix = 2
    $ basementBedroomMonicaSleepGfx = False
    call process_hooks("basement_monica_before_sleep", "global") from _call_process_hooks_51
    if _return == False:
        $ basement_bedroom2_MonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_91
        return False
    call processHouseCleaningEvening() from _call_processHouseCleaningEvening
    if cloth != "Nude":
        $ cloth_type = "Nude"
        if monicaUnder == "Nude":
            $ cloth = "Nude"
        else:
            $ cloth = "GovernessPants"
        $ monicaBettyPanties = False
    $ changeDayTime("day")
    call process_hooks("basement_monica_after_sleep", "global") from _call_process_hooks_52
    call refresh_scene_fade() from _call_refresh_scene_fade_92
    return False

label basement_monica_nap_transition1:
#    $ basementBedNapIndex = rand(1,4)
    $ basementBedNapIndex = ((day+1)%4) + 1
    if cloth == "SchoolOutfit1":
        $ basementBedNapIndex = 1
    $ set_active("BasementBed", False, scene="basement_bedroom2")
    call refresh_scene("Dissolve_05") from _call_refresh_scene_9
    return
#    img black_screen
#    with Dissolve(0.5)
#    call refresh_scene_fade()
    return
label basement_monica_sleep_transition1:
    $ basementBedSleepIndex = ((day+1)%4) + 1
    $ set_active("BasementBed", False, scene="basement_bedroom2")
    call refresh_scene("Dissolve_05") from _call_refresh_scene_10
#    img black_screen
#    with Dissolve(0.5)
#    call refresh_scene_fade()
    return

label basement_monica_after_nap:
    $ autorun_to_object("basement_monica_after_nap_dialogue")
    return

label basement_monica_after_nap_dialogue:
    call process_hooks("basement_monica_after_nap_dialogue", "global") from _call_process_hooks_35
    return
label basement_monica_after_nap_dialogue1:
    if day - monicaEatedLastDay >= 2:
        mt "Неплохо было бы что-то поесть..."
    else:
        mt "Я передохнула. Что дальше?"
    return

label basement_monica_after_sleep:
    $ autorun_to_object("basement_monica_after_sleep_dialogue", scene="basement_bedroom2")
    return
label basement_monica_after_sleep_dialogue:
    call process_hooks("basement_monica_after_sleep_dialogue", "global") from _call_process_hooks_36
    return

label monica_skip_until_friday: # Пропуск дней до пятницы
    img black_screen
    with Dissolve(0.5)
    $ skipDaysInterrupted = False
    $ skipDaysActiveFlag = True
    label monica_skip_until_friday_loop1:
        if day_time == "day":
            call process_hooks("basement_monica_before_nap", "global") from _call_process_hooks_53
            if _return == False:
                $ basement_bedroom2_MonicaSuffix = 2
                $ skipDaysInterrupted = True
            else:
                $ changeDayTime("evening")
                call process_hooks("basement_monica_after_nap", "global") from _call_process_hooks_54
        if day_time == "evening":
            call process_hooks("basement_monica_before_sleep", "global") from _call_process_hooks_55
            if _return == False:
                $ basement_bedroom2_MonicaSuffix = 2
                $ skipDaysInterrupted = True
            else:
                #call processHouseCleaningEvening()
                $ changeDayTime("day")
                call process_hooks("basement_monica_after_sleep", "global") from _call_process_hooks_56
        if week_day != skipUntilFridayTargetDay and skipDaysInterrupted == False:
            jump monica_skip_until_friday_loop1

    if skipDaysInterrupted == True:
        $ add_hook("basement_monica_after_sleep_dialogue", "monica_skip_until_friday_interrupted", scene="global", label="monica_skip_until_friday_interrupted", priority = 10000)
        $ add_hook("basement_monica_after_nap_dialogue", "monica_skip_until_friday_interrupted", scene="global", label="monica_skip_until_friday_interrupted", priority = 10000)
    $ skipDaysActiveFlag = False
    $ skipDaysInterrupted = False
    call refresh_scene_fade() from _call_refresh_scene_fade_93
    return False

label monica_skip_until_friday_interrupted:
    $ remove_hook(label="monica_skip_until_friday_interrupted")
    empty_name "Пропускание дней прервано..."
    return

label basement_monica_after_sleep_dialogue1:
    #Моника встает с утра
#    if basement_monica_after_sleep_dialogue1_skip == True:
#        $ basement_monica_after_sleep_dialogue1_skip = False
#        return
    $ rnd = rand(1,5)
    if rnd == 1:
        mt "Еще одно утро в этой дыре! Мне надо что-то придумать, чтобы вернуть все назад как было!"

    if rnd == 2:
        mt "Я не высыпаюсь на этой кровати."
        "Мне нужна нормальная постель!"

    if rnd == 3:
        mt "Такая королева как я не может привыкнуть спать в таких условиях!"
        "Я заслуживаю лучшего!"

    if rnd == 4:
        mt "Это мой дом! Я не заслуживаю того чтобы спать в подвале!"

    if rnd == 5:
        mt "Мне надо что-то придумать, чтобы вернуть все назад как было!"
    return

label basement_monica_hungry_cant_sleep:
    #если Моника не ела 3 дня
    mt "{c}Я не ела{/c} уже третий день!"
    "Я не могу лечь спать в таком состоянии!"
    "Я ХОЧУ ЕСТЬ!!!"
    call food_basement_check_food() from _call_food_basement_check_food
    if _return == True:
        $ sleepAfterEat = True
        $ basement_bedroom2_MonicaSuffix = 2
        call change_scene("basement_bedroom_table") from _call_change_scene_238
        return
    "..."
    mt "Может быть я смогу что-то найти на заправке?"
    mt "Или у кого-нибудь занять деньги на еду?"
    return

label basement_bed_skip_until_day1:
    img black_screen
    with Dissolve(0.2)
    $ basementBedroomMonicaSleepGfx = False
    call monica_skip_until_friday() from _rcall_monica_skip_until_friday
    return False
    return

label basement_bed_skip_until_day2:
    $ basementBedroomMonicaSleepGfx = False
    if cloth != "Nude":
        $ cloth_type = "Nude"
        if monicaUnder == "Nude":
            $ cloth = "Nude"
        else:
            $ cloth = "GovernessPants"
        $ monicaBettyPanties = False
    img black_screen
    with Dissolve(0.2)
    call monica_skip_until_friday() from _rcall_monica_skip_until_friday_1
    return False
