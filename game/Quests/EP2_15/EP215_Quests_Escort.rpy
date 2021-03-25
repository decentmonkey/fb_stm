default ep215_quests_escort_initialized = False
default ep215_quests_escort_repeat1_day = 0
default ep215_quests_escort_initialized_day = 0
default ep215_quests_escort_completed_day = 0
default ep215_quests_linda_restaurant_dialogue_planned = False
default ep215_quests_linda_restaurant_dialogue_day = 0

label ep215_quests_esort_change_name:
    call ep215_dialogues3_escort_23_change_name() from _rcall_ep215_dialogues3_escort_23_change_name
    $ autorun_to_object("ep215_dialogues3_escort_23_change_name_b")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_113
    return

label ep215_quests_esort1_init:
    $ ep215_quests_escort_initialized = True
    $ ep215_quests_escort_initialized_day = day
    # инициализируем свидание с инвестором
    $ add_hook("before_open", "ep215_quests_escort2", scene="monica_office_cabinet", label="ep215_quests_escort2")
    return

label ep215_quests_escort2:
    if ep213_presentation2_completed_day == 0: #EP25 hotfix1
        $ ep215_quests_escort_initialized = False
        $ ep215_quests_escort_initialized_day = 0
        $ remove_hook()
        $ remove_hook(label="ep215_quests_escort2_repeat")
        return

    # Моника заходит в кабинет Бифа и видит обнаженную Кристину
    if day_time != "evening" or day == ep215_quests_escort_initialized_day:
        return
    $ remove_hook()
    call ep215_dialogues3_escort_1() from _rcall_ep215_dialogues3_escort_1
    if _return == False:
        fadeblack 2.0
        $ autorun_to_object("ep215_dialogues3_escort_3", scene="street_monica_office")
        $ add_hook("Teleport_Inside", "ep215_dialogues3_escort_3", scene="street_monica_office", label=["evening_time_temp", "ep215_dialogues3_escort_3"])
        $ add_hook("Teleport_Inside", "ep215_quests_escort2_repeat", scene="street_monica_office", label="ep215_quests_escort2_repeat")
        $ add_hook("enter_scene", "ep215_quests_escort2_repeat_comment", scene="street_monica_office", label="ep215_quests_escort2_repeat_comment")
        $ questHelp("office_45", False)
        $ questHelp("escort_10", False)
        $ ep215_quests_escort_repeat1_day = day
        call putoff_work_clothes() from _rcall_putoff_work_clothes_10
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_169
        return False
    call ep215_quests_escort3_dating() from _rcall_ep215_quests_escort3_dating
    call putoff_work_clothes() from _rcall_putoff_work_clothes_11
    return False

label ep215_quests_escort2_repeat_comment:
    if ep215_quests_escort_repeat1_day == day:
        return
    $ remove_hook()
    call ep215_dialogues3_escort_4() from _rcall_ep215_dialogues3_escort_4
    return

label ep215_quests_escort2_repeat: # повторный приход к Бифу (если отказалась)
    if ep213_presentation2_completed_day == 0: #EP25 hotfix1
        $ ep215_quests_escort_initialized = False
        $ ep215_quests_escort_initialized_day = 0
        $ remove_hook()
        $ remove_hook(label="ep215_quests_escort2_repeat")
        return

    if ep215_quests_escort_repeat1_day == day:
        return

    if day_time == "day":
        $ changeDayTime("evening")
    fadeblack 2.0
    call ep215_dialogues3_escort_1b() from _rcall_ep215_dialogues3_escort_1b
    if _return == False:
        fadeblack 2.0
        $ autorun_to_object("ep215_dialogues3_escort_3", scene="street_monica_office")
        $ add_hook("Teleport_Inside", "ep215_dialogues3_escort_3", scene="street_monica_office", label=["evening_time_temp", "ep215_dialogues3_escort_3"])
#        $ add_hook("Teleport_Inside", "ep215_quests_escort2_repeat", scene="street_monica_office", label="ep215_quests_escort2_repeat")
        $ add_hook("enter_scene", "ep215_quests_escort2_repeat_comment", scene="street_monica_office", label="ep215_quests_escort2_repeat_comment")
        $ questHelp("office_45", False)
        $ questHelp("escort_10", False)
        $ ep215_quests_escort_repeat1_day = day
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_170
        return False
    call ep215_quests_escort3_dating() from _rcall_ep215_quests_escort3_dating_1
    $ remove_hook(label="ep215_quests_escort2_repeat")
    return False

label ep215_quests_escort3_dating: # свидание
    call ep215_dialogues3_escort_5() from _rcall_ep215_dialogues3_escort_5 # Моника идет в гримерку, чтобы переодеться
    call ep215_dialogues3_escort_7() from _rcall_ep215_dialogues3_escort_7 # холл, возле лифта
    call ep215_dialogues3_escort_8() from _rcall_ep215_dialogues3_escort_8 # ресторан (новая локация)
    $ questHelp("office_45", True)
    $ questHelp("office_50")
    if _return == 1:
        # Моника вынудила инвестора дать согласие на инвестирование при его жене
        $ questHelp("office_50", True)
        $ questHelp("office_51", False)
        $ questHelp("office_52")
        if monica_escort_service_started == True:
            $ questHelp("escort_10", False)
            $ questHelp("escort_12", False)
        pass
    else:
        $ questHelp("office_51", True)
        $ questHelp("office_50", False)
        $ questHelp("office_52")

        $ monicaEscortLastDay = day
        call ep215_dialogues3_escort_9() from _rcall_ep215_dialogues3_escort_9 # Ле Гранд, ресепшн
        call ep215_dialogues3_escort_10() from _rcall_ep215_dialogues3_escort_10 # у лифта
        call ep215_dialogues3_escort_11() from _rcall_ep215_dialogues3_escort_11 # номер отеля
        if monica_escort_service_started == True: # если работает или работала в эскорте
            call ep215_dialogues3_escort_12() from _rcall_ep215_dialogues3_escort_12
            call ep215_dialogues3_escort_13() from _rcall_ep215_dialogues3_escort_13
        call ep215_dialogues3_escort_14() from _rcall_ep215_dialogues3_escort_14
        if _return == 1: #отыграться на Линде
            call ep215_dialogues3_linda_punishment() from _rcall_ep215_dialogues3_linda_punishment
            if monica_escort_service_started == True:
                $ questHelp("escort_10", True)
            if questHelpFlag13 == False:
                $ questHelpFlag13 = True
                $ questHelpDesc("escort_desc3", "escort_desc5")
        else:
            if monica_escort_service_started == True:
                $ questHelp("escort_10", False)

        $ questHelp("escort_12", True)
        $ questHelp("office_52", skipIfExists=True)
        call ep215_dialogues3_escort_15() from _rcall_ep215_dialogues3_escort_15 # после окончания встречи с Олафом ресепшн
        if ep212_escort_monica_fired == True:
            $ ep212_escort_monica_fired = False

    call ep215_dialogues3_escort_21() from _rcall_ep215_dialogues3_escort_21 # после встречи с Олафом, в тот же вечер

    if monicaBiffInvestorDate2 == True:
        $ autorun_to_object("ep215_dialogues3_escort_20", scene="street_monica_office")
    else:
        if monicaBiffInvestorDate8 == True:
            $ autorun_to_object("ep215_dialogues3_escort_19", scene="street_monica_office")
            $ ep215_quests_linda_restaurant_dialogue_planned = True
        else:
            if monicaBiffInvestorDate6 == True:
                $ autorun_to_object("ep215_dialogues3_escort_18", scene="street_monica_office")
            else:

                if monicaBiffInvestorDate5 == True:
                    if monicaHotelAdminAgreement3 == True:
                        $ autorun_to_object("ep215_dialogues3_escort_17", scene="street_monica_office")
                    else:
                        $ autorun_to_object("ep215_dialogues3_escort_16", scene="street_monica_office")
    $ ep215_quests_escort_completed_day = day
    $ questHelp("office_52", True)
#    $ questHelp("office_53")
    $ add_hook("Teleport_Inside", "ep215_dialogues3_escort_24_block", scene="street_monica_office", label="evening_time_temp")
    call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_171
    return False











#
