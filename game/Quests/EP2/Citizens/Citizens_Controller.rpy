default fallingPathStarted = False
default whorePlaceFounded = False

default citizensAmountDay = 8
default citizensAmountEvening = 5
#define citizensAmountDay = 15
#define citizensAmountEvening = 15

# чем больше, тем меньше вероятность что откажет
default citizen1_refuse_probability = 5
default citizen2_refuse_probability = 5
default citizen3_refuse_probability = 5
default citizen4_refuse_probability = 5
default citizen5_refuse_probability = 5
default citizen6_refuse_probability = 5
default citizen7_refuse_probability = 5
default citizen8_refuse_probability = 5
default citizen9_refuse_probability = 5
default citizen10_refuse_probability = 5
default citizen11_refuse_probability = 5
default citizen12_refuse_probability = 5
default citizen13_refuse_probability = 5
default citizen14_refuse_probability = 5
default citizen15_refuse_probability = 5


default citizen1_offered_last_day = 0
default citizen2_offered_last_day = 0
default citizen3_offered_last_day = 0
default citizen4_offered_last_day = 0
default citizen5_offered_last_day = 0
default citizen6_offered_last_day = 0
default citizen7_offered_last_day = 0
default citizen8_offered_last_day = 0
default citizen9_offered_last_day = 0
default citizen10_offered_last_day = 0
default citizen11_offered_last_day = 0
default citizen12_offered_last_day = 0
default citizen13_offered_last_day = 0
default citizen14_offered_last_day = 0
default citizen15_offered_last_day = 0

default citizen12_forced = False

label citizens_dialogue:
    if kebabWorkFlyersLeft == 0 and kebabWorkInProgress == True:
        call monica_shawarma_dialogue3a() from _call_monica_shawarma_dialogue3a
        return
    call citizens_dialogue_process() from _call_citizens_dialogue_process
    if kebabWorkFlyersLeft > 0:
        if kebabWorkMonicaRefusedAmount + kebabWorkHarassmentAmount > 0 and (kebabWorkMonicaRefusedAmount+kebabWorkHarassmentAmount) % 3 == 0:
            $ autorun_to_object("monica_shawarma_dialogue10")
#    call refresh_scene_fade()
    $ restore_music()
    return
label citizens_dialogue_refuse:
    if fallingPathStarted == False:
        mt "Я не собираюсь с ним разговаривать без надобности!"
        "Мне противны эти люди!"
        "Они не соответствуют моему статусу!"
    else:
        mt "Я боюсь подходить к людям в вечернее время."
        "Это опасно..."
    return
label citizens_dialogue_process:
    $ store_music()
    $ citizenMusic = "DarxieLand"
    $ citizenObjName = obj_name

    # ГК. надо переделать :)
    if citizenObjName == "Citizen_1" or citizenObjName == "Citizen_2":
        if act=="l":
            mt "Панки... Выглядят не очень дружелюбно."
            return
        if kebabWorkInProgress == False:
            if (fallingPathStarted == False or day_time == "Evening"):
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse
                return
            call citizen1_dialogue_pilon() from _call_citizen1_dialogue_pilon
            return
        music citizenMusic
        call citizen1_dialogue() from _call_citizen1_dialogue

    if citizenObjName == "Citizen_3":
        if act=="l":
            mt "Хитрый взгляд... Похоже, этому человеку есть что скрывать."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_1
                return
            call citizen3_dialogue_pilon() from _call_citizen3_dialogue_pilon
            return
        music citizenMusic
        call citizen3_dialogue() from _call_citizen3_dialogue
    if citizenObjName == "Citizen_4":
        if act=="l":
            mt "Еще один обитатель трущоб. Таких тут полно."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_2
                return
            call citizen4_dialogue_pilon() from _call_citizen4_dialogue_pilon
            return
        music citizenMusic
        call citizen4_dialogue() from _call_citizen4_dialogue
    if citizenObjName == "Citizen_5":
        if act=="l":
            mt "Откуда этот парень? Что он тут делает?"
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_3
                return
            call citizen5_dialogue_pilon() from _call_citizen5_dialogue_pilon
            return
        music citizenMusic
        call citizen5_dialogue() from _call_citizen5_dialogue
    if citizenObjName == "Citizen_6":
        if act=="l":
            mt "Этот парень не выглядит злым. Надеюсь, так оно и есть."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_4
                return
            call citizen6_dialogue_pilon() from _call_citizen6_dialogue_pilon
            return
        music citizenMusic
        call citizen6_dialogue() from _call_citizen6_dialogue
    if citizenObjName == "Citizen_7":
        if act=="l":
            mt "Уличные художники. Даже в таком районе они есть."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_5
                return
            call citizen7_dialogue_pilon() from _call_citizen7_dialogue_pilon
            return
        music citizenMusic
        call citizen7_dialogue() from _call_citizen7_dialogue
    if citizenObjName == "Citizen_8":
        if act=="l":
            mt "Этот человек выглядит опасным. С ним надо быть настороже."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_6
                return
            call citizen8_dialogue_pilon() from _call_citizen8_dialogue_pilon
            return
        music citizenMusic
        call citizen8_dialogue() from _call_citizen8_dialogue
    if citizenObjName == "Citizen_9":
        if act=="l":
            mt "Сразу видно, что наркоман. Ему тут самое место."
            "Фи!"
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_7
                return
            $ act = "t"
            call ep22_quests_falling_path4() from _call_ep22_quests_falling_path4
#            call citizen9_dialogue_pilon()
            return
        music citizenMusic
        call citizen9_dialogue() from _call_citizen9_dialogue
    if citizenObjName == "Citizen_10":
        if act=="l":
            mt "И почему этот старик целый день на улице?"
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_8
                return
            call citizen10_dialogue_pilon() from _call_citizen10_dialogue_pilon
            return
        music citizenMusic
        call citizen10_dialogue() from _call_citizen10_dialogue
    if citizenObjName == "Citizen_11":
        if act=="l":
            mt "С этим все понятно: редкий день для него обходится без бутылки."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_9
                return
            call citizen11_dialogue_pilon() from _call_citizen11_dialogue_pilon
            return
        music citizenMusic
        call citizen11_dialogue() from _call_citizen11_dialogue
    if citizenObjName == "Citizen_12":
        if act=="l":
            mt "Еще один обитатель трущоб. Таких тут полно."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_10
                return
#            call citizen12_dialogue_pilon() from _call_citizen12_dialogue_pilon
            return
        else:
            if questOffendMonicaFlyersCitizen12Completed == True: # уже нападал на Монику
                call citizen12_dialogue_refuse_after_offend() from _call_citizen12_dialogue_refuse_after_offend
                return

        music citizenMusic
        call citizen12_dialogue() from _call_citizen12_dialogue
    if citizenObjName == "Citizen_13":
        if act=="l":
            mt "Какой милашка. Ха! Держу пари, девушки ему неинтересны..."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_11
                return
            call citizen13_dialogue_pilon() from _call_citizen13_dialogue_pilon
            return
        music citizenMusic
        call citizen13_dialogue() from _call_citizen13_dialogue
    if citizenObjName == "Citizen_14":
        if act=="l":
            mt "Еще один обитатель трущоб. Таких тут полно."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_12
                return

            call citizen14_dialogue_pilon() from _call_citizen14_dialogue_pilon
            return
        music citizenMusic
        call citizen14_dialogue() from _call_citizen14_dialogue
    if citizenObjName == "Citizen_15":
        if act=="l":
            mt "Еще один обитатель трущоб. Таких тут полно."
            return
        if kebabWorkInProgress == False:
            if fallingPathStarted == False or day_time == "Evening":
                call citizens_dialogue_refuse() from _call_citizens_dialogue_refuse_13
                return
            call citizen15_dialogue_pilon() from _call_citizen15_dialogue_pilon
            return
        music citizenMusic
        call citizen15_dialogue() from _call_citizen15_dialogue

#    call refresh_scene_fade()
    return

label citizens_init:
    $ citizens_list_source = {
        "Citizen_1":{"id":1},
        "Citizen_2":{"id":2},
        "Citizen_3":{"id":3},
        "Citizen_4":{"id":4},
        "Citizen_5":{"id":5},
        "Citizen_6":{"id":6},
        "Citizen_7":{"id":7},
        "Citizen_8":{"id":8},
        "Citizen_9":{"id":9},
        "Citizen_10":{"id":10},
        "Citizen_11":{"id":11},
        "Citizen_12":{"id":12},
        "Citizen_13":{"id":13},
        "Citizen_14":{"id":14},
        "Citizen_15":{"id":15},
    }
    return

label citizens_init_day:
#    if debugMode == True:
#        $ citizensAmountDay = 15 #debug!!!!
    call citizens_init() from _call_citizens_init_2
    python:
        citizensDayList = random.sample(set(list(citizens_list_source.keys())), citizensAmountDay)
#        citizensDayList = citizens_list_source.keys() #debug!!!
        if "Citizen_1" in citizensDayList:
            citizensDayList.append("Citizen_2")
        if "Citizen_2" in citizensDayList:
            citizensDayList.append("Citizen_1")
        if "Citizen_3" in citizensDayList:
            citizensDayList.append("Citizen_9")
        if "Citizen_9" in citizensDayList:
            citizensDayList.append("Citizen_3")
        if ep214_slums_citizen4_aborted == True:
            if "Citizen_4" in citizensDayList:
                citizensDayList.remove("Citizen_4")
        if ep214_quests_citizens_stage2 == True:
            if "Citizen_7" not in citizensDayList:
                citizensDayList.append("Citizen_7")

        if citizen12_forced == True:
            if "Citizen_12" not in citizensDayList:
                citizensDayList.append("Citizen_12")

        if day <= citizen14BlockedByDay and "Citizen_14" in citizensDayList:
            citizensDayList.remove("Citizen_14")
        if day <= citizen15BlockedByDay and "Citizen_15" in citizensDayList:
            citizensDayList.remove("Citizen_15")
        if ep214_quests_citizens_stage2 == True and ep215_slums1_citizen15_last_day == 0 and "Citizen_15" not in citizensDayList:
            citizensDayList.append("Citizen_15")

        if day <= citizen13BlockedByDay and "Citizen_13" in citizensDayList:
            citizensDayList.remove("Citizen_13")
        if ep214_quests_citizens_stage2 == True and ep215_slums1_citizen13_last_day == 0 and "Citizen_13" not in citizensDayList:
            citizensDayList.append("Citizen_13")


        citizensDayList = list(set(citizensDayList)) #unique
        set_active(False, scene="all", group="citizens")
        for var1 in citizensDayList:
            set_active(var1, True, scene="all")
#    $ print citizensDayList

    return
label citizens_init_evening:
    call citizens_init() from _call_citizens_init_3
    python:
        citizensEveningList = random.sample(set(list(citizens_list_source.keys())), citizensAmountEvening)
        if "Citizen_1" in citizensEveningList:
            citizensEveningList.append("Citizen_2")
        if "Citizen_2" in citizensEveningList:
            citizensEveningList.append("Citizen_1")
        if "Citizen_3" in citizensEveningList:
            citizensEveningList.append("Citizen_9")
        if "Citizen_9" in citizensEveningList:
            citizensEveningList.append("Citizen_3")
        if ep214_slums_citizen4_aborted == True:
            if "Citizen 4" in citizensEveningList:
                citizensEveningList.remove("Citizen 4")

        if day <= citizen14BlockedByDay and "Citizen_14" in citizensEveningList:
            citizensEveningList.remove("Citizen_14")
        if day <= citizen15BlockedByDay and "Citizen_15" in citizensEveningList:
            citizensEveningList.remove("Citizen_15")
        if day <= citizen13BlockedByDay and "Citizen_13" in citizensEveningList:
            citizensEveningList.remove("Citizen_13")

        citizensEveningList = list(set(citizensEveningList)) #unique
        set_active(False, scene="all", group="citizens")
        for var1 in citizensEveningList:
            set_active(var1, True, scene="all")
#    $ print citizensEveningList
    return

label citizens_init_monica_offend: # Инит ситизенов перед нападением на Монику
    python:
        # убираем всех ситизенов
        for citizenName in citizens_list_source:
            set_active(citizenName, False, scene="all")
        # оставляем участников сцены нападения
        set_active("Citizen_12", True, scene="all")
        set_active("Citizen_6", True, scene="all")
    return

label needToFindWhorePlace:
    mt "Мне надо найти какое-то тихое место."
    "Не собираюсь-же я делать это здесь..."
    return
