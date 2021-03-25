default ep210_quests_bardie_init_flag = False
default ep210_quests_bardie_day = 0
default ep210_quests_erik_jerk_betty_panties = False

label ep210_quests_bardie_init:
    if ep210_quests_bardie_init_flag == False and monicaBettyLesbian == True:
        $ add_hook("before_open", "ep210_quests_bardie1", scene="basement_laundry", label="ep210_quests_bardie")
        $ questHelp("house_27a")
        $ ep210_quests_bardie_day = day
        $ ep210_quests_bardie_init_flag = True
    return

label ep210_quests_bardie1:
    # Моника заходит в прачечную
    # Начинается сцена Барди, Эрика и Бетти
    if ep210_quests_bardie_day == day or day_time != "evening" or steveVisit1Day == day or steveVisit2Day == day:
        return
    $ remove_hook()
    call ep210_dialogues3_bardie_erik_betty_1() from _call_ep210_dialogues3_bardie_erik_betty_1
    $ autorun_to_object("ep210_dialogues3_bardie_erik_betty_1a", scene="basement_laundry")
    $ add_hook("exit_scene", "ep210_quests_bardie2", scene="basement_laundry", label="ep210_quests_bardie")
    return


label ep210_quests_bardie2:
    # Моника уходит из прачечной
    call ep210_dialogues3_bardie_erik_betty_2() from _call_ep210_dialogues3_bardie_erik_betty_2
    $ ep210_quests_erik_jerk_betty_panties = True
    $ questHelp("house_27a", True)
    $ remove_hook()
    return
