default ep214_slums_offer_activated = False
default ep214_slums_offer_day = 0
default ep214_slums_citizen4_aborted = False
default ep214_slums_monnica_licked_perry_last_day = 0
default ep214_slums_monnica_licked_perry_first_day = 0
default ep214_slums_monnica_licked_perry_count = 0
default ep214_slums_monica_perry_talk_count = 0
default ep214_slums_monica_rent_hostel_last_day = 0
default ep214_slums_monica_paid_money_this_week = False
default ep214_slums_enter_hostel_last_day = 0
default ep214_perry_debt = 50000.0

default ep214_monica_talked_mommy = False
default ep214_monica_talked_mommy_last_day = 0

label ep214_slums1_offer:
    $ ep214_slums_offer_day = day
    $ ep214_slums_offer_activated = True
    call ep214_dialogues2_citizens_1() from _rcall_ep214_dialogues2_citizens_1
    if _return == -1:
        $ ep214_slums_offer_activated = False
        return False
    if _return == -2: # Укусила
        $ ep214_slums_citizen4_aborted = True
        $ ep214_slums_offer_activated = False
        $ enter_scene("ep214_dialogues2_citizens_5", once=True)
        call bitch(20, "ep214_slums_citizen4_aborted") from _rcall_bitch_17
        fadeblack 2.0
        call change_scene("street_corner", "Fade_long") from _rcall_change_scene_144
        return True
    if _return == -3: # Убежала от Перри
        $ enter_scene("ep214_dialogues2_citizens_2", once=True)
        call whores_place_init2() from _rcall_whores_place_init2
        $ street_whores_perry_active = True
        $ add_hook("Perry", "ep214_slums2_perry_repeat", scene="whores_place", label="ep214_slums2_perry_repeat")
        $ add_hook("Perry", "ep214_dialogues2_citizens_7", scene="whores_place", act="l", label="ep214_slums2_perry_repeat")
        $ add_hook("Teleport_Hostel_1_a", "ep214_dialogues2_citizens_4", act="w", scene="hostel_edge_1_c", label=["day_time_temp", "ep214_slums2_perry_repeat"])
        $ changeDayTime("evening")
        fadeblack 2.0
        call change_scene("street_corner", "Fade_long") from _rcall_change_scene_145
        return True
    if _return == 1:
        call ep214_slums3_start_fp_part2() from _rcall_ep214_slums3_start_fp_part2
        $ autorun_to_object("ep214_dialogues2_citizens_3", scene="hostel_edge_1_a")
        call refresh_scene_fade() from _rcall_refresh_scene_fade_110
        call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_146
        return True
    return

label ep214_slums2_perry_repeat:
    if act=="l":
        return
    $ remove_hook(label="ep214_slums2_perry_repeat")
    $ set_active("Perry", False, scene="whores_place")
    $ street_whores_perry_active = False
    call ep214_dialogues2_citizens_1b() from _rcall_ep214_dialogues2_citizens_1b
    call ep214_slums3_start_fp_part2() from _rcall_ep214_slums3_start_fp_part2_1
    $ enter_scene("ep214_dialogues2_citizens_3", once=True)
    call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_147
    return False

label ep214_slums3_start_fp_part2: # Начало новой части квестов в трущобах (старые неактивны)
    $ questLog(82, True)

    # феилим все оставшиеся квесты в трущобах
    $ questsFailByCategory(t_("РАБОТА НА УЛИЦЕ"))
    $ questHelp("work_slums_47")
    $ questHelp("work_slums_48")
    if game.extra == False:
        $ questHelp("work_slums_48", False)

    $ questHelp("work_slums_49")
    $ questHelp("work_slums_50")
    $ questHelp("work_slums_51")
#    $ questHelp("work_slums_52")
#    $ questHelp("work_slums_53")
    $ questHelp("hostel_1")
    $ questHelpDesc("hostel_desc1")
    $ questHelpDesc("workslums_desc4", "workslums_desc5")
    $ questHelp("hostel_2")

    # инициализируем хостел
    call locations_init_hostel_inside() from _rcall_locations_init_hostel_inside
    $ add_hook("Teleport_Hostel_Street_Door", "ep214_dialogues2_citizens_7", act="l", scene="hostel_street", label="Perry_Debt")
    $ add_hook("Poster", "ep214_dialogues2_citizens_7", scene="hostel_street_door", label="Perry_Debt")
    $ add_hook("Teleport_hostel_reception", "ep214_slums4_enter_hostel", scene="hostel_street_door", label="Perry_Debt")
    $ add_hook("Perry", "ep214_dialogues2_citizens_7", scene="hostel_reception", label="Perry_Debt")

    $ add_hook_multi("ep214_citizens_click", scene="Street_Corner", recursive=True, label="citizens_interact2", filter={"group":"citizens"})
    $ add_talk("Perry", "ep214_slums5_talk_perry_first_time", scene="hostel_reception", label="Perry_Debt_talk")
    $ add_hook("Teleport_Hostel_Bedroom", "ep214_slums5_talk_perry_first_time", scene="hostel_reception", label="Perry_Debt_talk")

    $ add_hook_day("ep214_slums6_weekly", week_day = 6, label="Perry_Debt_check") #каждую субботу утром будет проверка на отдачу долга Перри

    $ add_hook("HostelBed", "ep214_dialogues2_citizens_11", act="l", scene="hostel_bedroom", label="Perry_Debt")
    $ add_hook("HostelBed", "ep214_slums7_hostelbed", act="h", scene="hostel_bedroom", label="Perry_Debt")
    $ add_hook("Shower", "ep214_slums8_hostelshower", act="h", scene="hostel_bathroom", label="Perry_Debt")
    $ add_hook("Toilet", "ep214_slums9_hosteltoilet", act="h", scene="hostel_bathroom_toilet", label="Perry_Debt")

    $ add_hook("hostel_monica_after_sleep", "ep214_dialogues2_citizens_11a", scene="global", label="Perry_Debt_aftersleep")
    $ add_hook("hostel_monica_before_sleep", "ep214_dialogues2_citizens_11b2", scene="global", label="Perry_Debt_beforesleep")

    # инициализируем точку с проститутками
    $ add_hook("enter_scene", "ep214_dialogues2_citizens_20", scene="whores_place", once=True, label="Mommy_Whore_Quest")
    $ add_talk("Mommy", "ep214_slums10_mommy", scene="whores_place", label=["Mommy_Whore_Quest", "Mommy_Whore_Quest_dialogue"])

    # меняем стадию общения с ситизенами
    $ ep214_quests_citizens_stage2 = True
    $ questLog(83, True)
    return

label ep214_slums4_enter_hostel:
    if act=="l":
        call ep214_dialogues2_citizens_7() from _rcall_ep214_dialogues2_citizens_7
        return False
    $ hostelReceptionPerrySuffix = rand(1,2)
    $ ep214_slums_enter_hostel_last_day = day
    call change_scene("hostel_reception", "Fade", "snd_jail_door") from _rcall_change_scene_148
    return False

label ep214_slums5_talk_perry_first_time: # первый разговор с Перри
    if obj_name == "Teleport_Hostel_Bedroom" and ep214_slums_monica_rent_hostel_last_day >= day:
        # проходим свободно
        return
    if ep214_slums_monica_rent_hostel_last_day >= day:
        call ep214_dialogues2_citizens_11d() from _rcall_ep214_dialogues2_citizens_11d #А, детка, ты уже соскучилась по моей волосатой киске?
        $ hostelReceptionPerrySuffix = 3
        call change_scene("hostel_bedroom") from _rcall_change_scene_149
        return False
    if ep214_slums_enter_hostel_last_day < day: # если ночевали здесь
        if ep214_perry_debt > 0:
            call ep214_dialogues2_citizens_11b() from _rcall_ep214_dialogues2_citizens_11b #Жду тебя не позже, чем через неделю!
        else:
            # ночевали и ничего не должны, просто выкидываем из локации
            call change_scene("hostel_street", "Fade_long", "snd_jail_door") from _rcall_change_scene_150
        return False

    $ hostelBedroomMonicaSuffix = 1
    call ep214_dialogues2_citizens_8() from _rcall_ep214_dialogues2_citizens_8
    if _return == 1: # Моника отдала часть денег. полизала и может ночевать, осталась ночевать
        $ add_hook("enter_scene", "ep214_dialogues2_citizens_11c", scene="hostel_street", once=True, label=["day_time_temp", "evening_time_temp", "hostel_comment"])
        $ add_hook("enter_scene", "ep214_dialogues2_citizens_9", scene="hostel_bedroom", once=True, label=["day_time_temp", "evening_time_temp", "hostel_comment"])
        call change_scene("hostel_bedroom", "Fade_long") from _rcall_change_scene_151
        return False
    if _return == -1: # Моника отдала часть денег. полизала и может ночевать, но ушла
        $ add_hook("enter_scene", "ep214_dialogues2_citizens_11c", scene="hostel_street", once=True, label=["day_time_temp", "evening_time_temp", "hostel_comment"])
        $ add_hook("enter_scene", "ep214_dialogues2_citizens_9", scene="hostel_bedroom", once=True, label=["day_time_temp", "evening_time_temp", "hostel_comment"])
        call change_scene("hostel_street", "Fade_long") from _rcall_change_scene_152
        return False
    if _return == -2: # Моника не стала ничего отдавать, уходит
        $ enter_scene("ep214_dialogues2_citizens_12", once=True)
        call change_scene("hostel_street", "Fade_long") from _rcall_change_scene_153
        return False
    if _return == -3: # Моника полизала, может ночевать, но злая
        $ add_hook("enter_scene", "ep214_dialogues2_citizens_13", scene="hostel_street", once=True, label=["day_time_temp", "evening_time_temp", "hostel_comment"])
        $ add_hook("enter_scene", "ep214_dialogues2_citizens_9", scene="hostel_bedroom", once=True, label=["day_time_temp", "evening_time_temp", "hostel_comment"])
        $ hostelReceptionPerrySuffix = 3
    if _return == -4: # Моника отдала часть денег. но не лизала (нет жилья)
        $ enter_scene("ep214_dialogues2_citizens_15", once=True)
        call change_scene("hostel_street", "Fade_long", "snd_jail_door") from _rcall_change_scene_154
        return False
    return False

label ep214_slums6_weekly: # вызывается по субботам
    if ep214_perry_debt > 0:
        if ep214_slums_monica_paid_money_this_week == True:
            $ ep214_slums_monica_paid_money_this_week = False
            return
        $ ep214_perry_debt += 1000.0
        $ notif(t_("Долг Перри увеличился на $ 1000"))
    return

label ep214_slums_hostel_bedroom_life:
    if day_time == "evening":
        $ set_active("Whore1", False)
    else:
        $ set_active("Whore1", True)
    return

label ep214_slums7_hostelbed:
    if act=="h":
        if ep214_slums_monica_rent_hostel_last_day < day:
            call ep214_dialogues2_citizens_2b() from _rcall_ep214_dialogues2_citizens_2b
            return False
    jump hostel_basement_bed

label ep214_slums8_hostelshower:
    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return
    call ep214_dialogues2_citizens_10() from _rcall_ep214_dialogues2_citizens_10
    if day_time == "evening":
        $ autorun_to_object("ep214_dialogues2_citizens_10b", scene="hostel_bathroom")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_111
    $ monicaLastShowerDay = day
    $ monicaLastShowerDayTime = day_time
    return False

label ep214_slums9_hosteltoilet:
    call ep214_dialogues2_citizens_15b() from _rcall_ep214_dialogues2_citizens_15b
    call refresh_scene_fade() from _rcall_refresh_scene_fade_112
    $ monicaLastPissedDay = day
    $ monicaLastPissedDayTime = day
    return False

label ep214_slums10_mommy:
    if ep214_monica_talked_mommy_last_day != day:
        call ep214_dialogues2_citizens_21() from _rcall_ep214_dialogues2_citizens_21
    else:
        call ep214_dialogues2_citizens_22() from _rcall_ep214_dialogues2_citizens_22
        return False
    $ enter_scene("ep214_dialogues2_citizens_22", once=True)
    call change_scene("whores_place_street1", "Fade_long") from _rcall_change_scene_155
    $ questHelp("hostel_1", True)
    $ ep214_monica_talked_mommy_last_day = day
    $ ep214_monica_talked_mommy = True
    return False

label ep214_citizens_click:
    if act=="l":
        return
#    m "here"
    return






#
