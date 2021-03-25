default ep214_quests_melanie_day = 0

label ep214_quests_melanie:
    $ remove_hook()
    $ ep214_quests_melanie_day = day
    call ep214_dialogues4_melanie_alex_1() from _rcall_ep214_dialogues4_melanie_alex_1
    call ep214_dialogues4_melanie_alex_2() from _rcall_ep214_dialogues4_melanie_alex_2
    $ questHelp("melanie_19", True)
    $ questHelp("victoria_9")
    $ move_object("Melanie", "empty")
    $ move_object("AlexPhotograph", "empty")
    $ Melanie_Life_evening2_skip_once = True
    $ add_hook("change_time_day", "ep214_quests_melanie1_spawn_alex_morning", scene="global", once=True, label="ep214_quests_melanie1_spawn_alex_morning")
    return

label ep214_quests_melanie1_spawn_alex_morning:
    $ move_object("AlexPhotograph", "monica_office_photostudio")
    return
