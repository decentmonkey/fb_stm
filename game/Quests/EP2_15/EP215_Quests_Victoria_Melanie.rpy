default ep215_quests_victoria_melanie_inited1 = False
default ep215_quests_victoria_melanie_inited2 = False
default ep215_quests_victoria_melanie_inited3 = False
default ep215_victoria_visit_day = 0
default ep215_victoria_visit_alex_day = 0
default ep215_victoria_visit_melaniehome_day = 0
default ep215_victoria_dick_visit_day = 0

label ep215_quests_victoria_melanie1: # Виктория приходит к Монике в офис (общается с Юлией)
    $ ep215_quests_victoria_melanie_inited1 = True
    $ add_hook("before_open", "ep215_quests_victoria_melanie2", scene="working_office", label="ep215_quests_victoria_melanie2")
    $ add_hook("before_open", "ep215_quests_victoria_melanie2", scene="working_office_cabinet", label="ep215_quests_victoria_melanie2")

    return

label ep215_quests_victoria_melanie2: # Моника проходит мимо сотрудников
    if ep212_quests_photoshoot9_after_init_planned == True or week_day == 7 or day_time != "day":
        return
    $ remove_hook(label="ep215_quests_victoria_melanie2")
    call ep215_dialogues4_julia_1() from _rcall_ep215_dialogues4_julia_1
    call ep215_dialogues4_julia_2() from _rcall_ep215_dialogues4_julia_2
    $ workingOfficeCabinetMonicaSuffix = 2
    $ questHelp("victoria_9", True)
    $ questHelp("victoria_10")
#    $ add_hook("before_open", "ep215_quests_victoria_melanie3", scene="working_office_cabinet", label=["ep215_quests_victoria_melanie3", "day_time_temp"])
    $ ep215_victoria_visit_day = day
    $ workingOfficeCabinetMonicaSuffix = 2
    call change_scene("working_office_cabinet") from _rcall_change_scene_172
    return

#label ep215_quests_victoria_melanie3: # Моника заходит в кабинет
#    $ remove_hook()
#    call ep215_dialogues4_julia_2()
#    $ workingOfficeCabinetMonicaSuffix = 2
#    return

label ep215_quests_victoria_melanie4: # Виктория приходит к Алексу (у лифта)
    $ ep215_quests_victoria_melanie_inited2 = True
    $ add_hook("before_open", "ep215_quests_victoria_melanie5", scene="monica_office_entrance", label="ep215_quests_victoria_melanie4")
    return

label ep215_quests_victoria_melanie5:
    $ remove_hook()
    $ ep215_victoria_visit_alex_day = day
    call ep215_dialogues5_alex_1() from _rcall_ep215_dialogues5_alex_1
    call ep215_quests_victoria_melanie6() from _rcall_ep215_quests_victoria_melanie6
    $ questHelp("victoria_10", True)
    $ questHelp("victoria_11")


    call change_scene("street_monica_office", "Fade_long", "highheels_run2") from _rcall_change_scene_173
    return False

label ep215_quests_victoria_melanie6: # Виктория приходит к Мелани домой
    $ ep215_quests_victoria_melanie_inited3 = True
    $ add_hook("change_time_evening", "ep215_quests_victoria_melanie7", scene="global", label="ep215_quests_victoria_melanie7")
    return

label ep215_quests_victoria_melanie7:
    $ remove_hook()
    call ep215_dialogues5_alex_2() from _rcall_ep215_dialogues5_alex_2
    call ep215_dialogues5_alex_3() from _rcall_ep215_dialogues5_alex_3
    $ ep215_victoria_visit_melaniehome_day = day
    $ questHelp("victoria_11", True)
    $ questHelp("melanie_20")
    $ add_hook("before_open", "ep215_quests_victoria_melanie8", scene="monica_office_cabinet", label="ep215_quests_victoria_melanie8")
    $ add_hook("before_open", "ep215_quests_victoria_melanie8", scene="monica_office_photostudio", label="ep215_quests_victoria_melanie8")
    $ add_hook("before_open", "ep215_quests_victoria_melanie8", scene="monica_office_secretary", label="ep215_quests_victoria_melanie8")
    $ add_hook("before_open", "ep215_quests_victoria_melanie8", scene="working_office_cabinet", label="ep215_quests_victoria_melanie8")
    $ add_hook("before_open", "ep215_quests_victoria_melanie8", scene="working_office", label="ep215_quests_victoria_melanie8")
    $ move_object("Melanie", "empty")
    $ move_object("AlexPhotograph", "empty")
    $ Melanie_Life_evening2_skip_once = True
    $ add_hook("change_time_day", "ep214_quests_melanie1_spawn_alex_morning", scene="global", once=True, label="ep214_quests_melanie1_spawn_alex_morning")
    return

label ep215_quests_victoria_melanie8: # Моника заходит в лифт и попадает в фотостудию
    if day_time != "day" or day - ep215_victoria_visit_melaniehome_day < 2:
        return
    $ remove_hook(label="ep215_quests_victoria_melanie8")
    $ ep215_victoria_dick_visit_day = day
    sound snd_lift
    fadeblack 1.5
    call ep215_dialogues5_alex_4() from _rcall_ep215_dialogues5_alex_4
    call ep215_dialogues5_alex_5() from _rcall_ep215_dialogues5_alex_5
    call ep215_dialogues5_alex_6() from _rcall_ep215_dialogues5_alex_6
    call ep215_dialogues5_alex_7() from _rcall_ep215_dialogues5_alex_7
    call ep215_dialogues5_alex_8() from _rcall_ep215_dialogues5_alex_8

    $ questHelp("melanie_20", True)
    $ questHelp("dick_5", True)
    $ questHelp("office_47")
    $ questHelp("melanie_21", True)
    $ questHelpDesc("dick_desc6", "dick_desc5")
    $ questHelpDesc("melanie_desc9", "melanie_desc10")
    $ move_object("Melanie", "empty")
    call change_scene("monica_office_photostudio", "Fade_long") from _rcall_change_scene_174
    return









#
