default pubMonicaWorkingWaitress = False
default pubMonicaWorkingWaitressShiftInProgress = False
default pubMonicaWorkedWaitressLastDay = 0
default pubMonicaWaitressTips = 0
default pubMonicaWaitressTipsStolen = False
default pubMonicaWaitressServedCustomersToday = 0
default pubMonicaWaitressServedCustomersTotal = 0
default pubMonicaWaitressWorkedDaysTotal = 0
default pubMonicaWaitressVisitorsServed = []

default pubMonicaWaitressClothBefore = ""
default pubMonicaWaitressClothTypeBefore = ""

default pubMonicaWaitressTipsPunishmentTalkStage = 0


label ep27_quests_pub_work1: # Моника спрашивает о повышении
    call ep27_dialogues7_pub1() from _call_ep27_dialogues7_pub1
    music2 stop
    if _return == False or _return == -1:
#        $ questHelp("shinyhole_4", False)
        call change_scene("hostel_street", "Fade_long") from _call_change_scene_366
        return False
    # Моника принята на работу официанткой
    $ questHelp("shinyhole_4", True)
    $ questHelp("shinyhole_5")
    $ questHelpDesc("shinyhole_desc2", False)
    $ questHelpDesc("shinyhole_desc3", False)
    $ questHelpDesc("shinyhole_desc4")
    $ pubMonicaWorkingWaitress = True

    if day_time == "day":
        call process_hooks("Pub_Life_day", "global") from _call_process_hooks_70
    else:
        call process_hooks("Pub_Life_evening", "global") from _call_process_hooks_71

    $ questLog(52, True)
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_23
    return False

label ep27_quests_pub_work2_begin: #Работать официанткой в Shiny Hole.
    if pubMonicaWorkedWaitressLastDay == day: # уже работала сегодня
        call ep27_dialogues7_pub3() from _call_ep27_dialogues7_pub3
        call refresh_scene_fade() from _call_refresh_scene_fade_162
        return False

    # Начинаем работу официанткой
    $ pubMonicaWorkingWaitressShiftInProgress = True

    call ep27_dialogues7_pub4() from _call_ep27_dialogues7_pub4
    music2 stop
    $ set_var("Monica", zorder = 1, scene="pub")
#    $ set_var("Monica", zorder = 200, scene="pub")
    call ep27_pub_visitors_init() from _call_ep27_pub_visitors_init

    $ pubMonicaWaitressVisitorsServed = []
    $ pubMonicaWaitressWorkedDaysTotal += 1
    $ pubMonicaWaitressTips = 0
    $ pubMonicaWaitressServedCustomersToday = 0
    $ pubMonicaWaitressClothTypeBefore = cloth_type
    $ pubMonicaWaitressClothBefore = cloth
    $ cloth = "Waitress"
    $ cloth_type = "Waitress"
    $ add_hook("Teleport_Hostel_Street", "ep27_quests_pub_work3_exit", scene="pub", label="working_waitress")
    $ add_hook("Bartender", "ep27_quests_pub_work4", scene="pub", label="working_waitress")
    $ add_hook("Bartender_Waitress", "ep27_quests_pub_work4", scene="pub", label="working_waitress")
    $ add_hook_multi("ep27_pub_visitors_click", scene="pub", label="working_waitress", filter={"group":"visitors"})
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 0.5
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_24
    return

label ep27_quests_pub_work3_exit: # Моника пытается выйти из паба во время работы
    call ep27_dialogues7_pub6() from _call_ep27_dialogues7_pub6 # Вопрос о том, чтобы уйти без чаевых
    if _return == True:
        return False
    $ remove_hook(label="working_waitress")
    $ pubMonicaWaitressTipsStolen = True
    $ set_var("Monica", zorder = 200, scene="pub") # Делаем Монику снова спереди
    if pubMonicaWaitressTips > 0:
        $ autorun_to_object("ep27_dialogues7_pub6a", scene="hostel_street")
    $ questHelp("shinyhole_6", True)

    if pubMonicaWaitressTipsPunishmentJoeStage == 0:
        $ questHelp("shinyhole_8", skipIfExists=True)
    if pubMonicaWaitressTipsPunishmentJoeStage == 1:
        $ questHelp("shinyhole_8", skipIfExists=True)
    if pubMonicaWaitressTipsPunishmentJoeStage == 2:
        $ questHelp("shinyhole_8", skipIfExists=True)
    if pubMonicaWaitressTipsPunishmentJoeStage == 3:
        $ questHelp("shinyhole_8", skipIfExists=True)
    if pubMonicaWaitressTipsPunishmentAshleyStage == 0:
        $ questHelp("shinyhole_7", skipIfExists=True)
    if pubMonicaWaitressTipsPunishmentAshleyStage == 1:
        $ questHelp("shinyhole_7a", skipIfExists=True)
    if pubMonicaWaitressTipsPunishmentAshleyStage == 2:
        $ questHelp("shinyhole_7b", skipIfExists=True)

    $ add_hook("Teleport_Hostel_Pub", "ep27_dialogues7_pub6a", scene="hostel_street", label="evening_time_temp")
    $ add_hook("Bartender", "ep27_quests_pub_work6_tips_punishment", scene="pub", label="working_waitress_tips_punishment1")
    $ add_hook("Bartender_Waitress", "ep27_quests_pub_work6_tips_punishment", scene="pub", label="working_waitress_tips_punishment1")

    $ pubMonicaWorkingWaitressShiftInProgress = False
    $ pubMonicaWaitressTipsPunishmentTalkStage = 0

    $ cloth_type = pubMonicaWaitressClothTypeBefore
    $ cloth = pubMonicaWaitressClothBefore
    music2 stop
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    $ notif(t_("Моника украла чаевые из Shiny Hole"))
    call change_scene("hostel_street", "Fade_long") from _call_change_scene_367
    return False

label ep27_quests_pub_work4: # Клик на барменов
    if act=="l":
        return
    call ep27_dialogues7_pub7a() from _call_ep27_dialogues7_pub7a
    if _return == False:
        return False
    # Заканчиваем работу самостоятельно
    call ep27_quests_pub_work5() from _call_ep27_quests_pub_work5
    return False

label ep27_quests_pub_work5:
    $ questHelp("shinyhole_5", True)
    $ questHelp("shinyhole_6", skipIfExists=True)

    # Заканчиваем работу
    $ pubMonicaWorkingWaitressShiftInProgress = False
    call ep27_dialogues7_pub7() from _call_ep27_dialogues7_pub7
    music2 stop
    $ remove_hook(label="working_waitress")
    $ pubMonicaWorkedWaitressLastDay = day
    $ cloth_type = pubMonicaWaitressClothTypeBefore
    $ cloth = pubMonicaWaitressClothBefore
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    $ notif(t_("Моника закончила смену официантки"))
    $ set_var("Monica", zorder = 200, scene="pub") # Делаем Монику снова спереди
    call change_scene("hostel_street", "Fade_long") from _call_change_scene_368
    return

label ep27_quests_pub_work6_tips_punishment: # Наказание за кражу чаевых
    if act=="l":
        return
    call ep27_dialogues7_pub8() from _call_ep27_dialogues7_pub8
    $ questHelp("shinyhole_7", skipIfExists=True)
    $ questHelp("shinyhole_8", skipIfExists=True)
    $ questHelp("shinyhole_9", skipIfExists=True)
    if _return == 0:
        call change_scene("hostel_street", "Fade_long") from _call_change_scene_369
        return False
    if _return == 1:
        # Моника вернула деньги
        call ep27_quests_pub_work7_tips_punishment_forgive() from _call_ep27_quests_pub_work7_tips_punishment_forgive_7
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_25
        return False
    if _return == 2:
        $ pubMonicaWaitressTipsPunishmentTalkStage = 1
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_26
        return False
    if _return == 3:
        # Попросить прощения у Джо
        call ep22_quests_pub_punishment_joe() from _call_ep22_quests_pub_punishment_joe
        return False
    if _return == 4:
        # Попросить прощения у Эшли
        call ep22_quests_pub_punishment_ashley() from _call_ep22_quests_pub_punishment_ashley
        return False
    if _return == 5:
        call ep29_quests_pub1_dance_agree() from _call_ep29_quests_pub1_dance_agree
        return False
    return

label ep27_quests_pub_work7_tips_punishment_forgive: # Моника прощается
    $ pubMonicaWaitressTipsStolen = False
    $ remove_hook(label="working_waitress_tips_punishment1")
    return
