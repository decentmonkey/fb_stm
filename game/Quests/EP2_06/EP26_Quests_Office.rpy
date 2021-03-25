label ep26_quests_office1:
    # Инициализируем первый приход Моники в офис
    $ set_active(False, group="environment", scene="working_office")
    $ set_active(False, group="workers", scene="working_office")
    $ set_active("Teleport_Cabinet", False, scene="working_office")
    $ set_active("Teleport_Monica_WorkingOffice2", False, scene="working_office")

    $ add_hook("before_open", "ep26_quests_office2", scene="working_office")
    return


label ep26_quests_office2:
    # Первый приход Моники в офис working_office
    if day_time == "evening":
        # Моника говорит что никого нет
        $ autorun_to_object("ep26_dialogues6_office2_monica_visit1", scene="working_office")
        return

    $ remove_hook()
    # Включаем всех работников
    $ set_active(True, group="environment", scene="working_office")
    $ set_active(True, group="workers", scene="working_office")
    $ set_active(False, teleport=True, scene="working_office") # Выключаем телепорты
    $ add_hook_multi("ep26_quests_office3", scene="working_office", label="office_workers_meeting_dialogue1", filter={"group":"workers"})

    $ autorun_to_object("ep26_dialogues6_office2_monica_visit1a", scene="working_office")
    return

label ep26_quests_office3:
    # Моника кликает на кого-то из работников
    call ep26_dialogues6_office2_1() from _call_ep26_dialogues6_office2_1
    $ autorun_to_object("ep26_dialogues6_office2_1a", scene="working_office_cabinet")
    $ add_hook("Teleport_WorkingOffice_Cabinet2", "ep26_dialogues6_office2_1a", scene="working_office_cabinet", label="julia_meeting_block1")
    $ add_hook("Teleport_Monica_WorkingOffice", "ep26_dialogues6_office2_1a", scene="working_office_cabinet", label="julia_meeting_block1")
    $ set_active(False, group="environment", scene="working_office_cabinet")
    $ set_active(True, group="environment", scene="working_office")
    $ set_active(True, teleport=True, scene="working_office")

    $ remove_hook(label="office_workers_meeting_dialogue1")

    $ add_hook("Julia", "ep26_quests_office4", scene="working_office_cabinet")
    call change_scene("working_office_cabinet", "Fade_long", False) from _call_change_scene_330
    return False

label ep26_quests_office4:
    # Клик на Юлию
    if act=="l":
        call ep26_dialogues6_office2_1a() from _call_ep26_dialogues6_office2_1a
        return False
    $ remove_hook()
    call ep26_dialogues6_office2_2() from _call_ep26_dialogues6_office2_2
    $ remove_hook(label="julia_meeting_block1")
    $ add_hook("Teleport_WorkingOffice_Cabinet2", "ep26_dialogues6_office2_monica_visit1b", scene="working_office_cabinet", label="julia_meeting_block2")
    $ add_hook("Teleport_Monica_WorkingOffice", "ep26_dialogues6_office2_monica_visit1b", scene="working_office_cabinet", label="julia_meeting_block2")

    $ set_active(True, group="environment", scene="working_office_cabinet")
    $ set_active("MonicaChair", False, scene="working_office_cabinet")
    $ set_active("MonicaTable", False, scene="working_office_cabinet")

    $ add_hook("Julia", "ep26_quests_office5", scene="working_office_cabinet")
    $ autorun_to_object("ep26_dialogues6_office2_monica_visit1b", scene="working_office_cabinet")
    $ workingOfficeCabinetMonicaSuffix = 2 # Моника за столом
    $ workingOfficeCabinetJuliaSuffix = 3 # Юлия работает
    call refresh_scene_fade() from _call_refresh_scene_fade_150
    return False

label ep26_quests_office5:
    # Второй разговор с Юлией (заходят работники)
    if act=="l":
        return
    $ remove_hook()
    $ remove_hook(label="julia_meeting_block2")
    $ workingOfficeCabinetJuliaSuffix = 2 # Юлия смотрит на Монику (испуганно)
    $ autorun_to_object("ep26_quests_office6", scene="working_office_cabinet")
    call refresh_scene("Dissolve_05") from _call_refresh_scene_14
    return False
label ep26_quests_office6:
    # Второй разговор с Юлией (заходят работники) autorun
    call ep26_dialogues6_office2_2a() from _call_ep26_dialogues6_office2_2a
    call ep26_dialogues6_office2_3() from _call_ep26_dialogues6_office2_3

    $ questHelp("office_26", True)
    $ questHelp("office_27")
    $ questHelp("office_29")
    $ questHelp("office_32", skipIfExists=True)

    $ set_active("MonicaChair", True, scene="working_office_cabinet")
    $ set_active("MonicaTable", True, scene="working_office_cabinet")

    $ workingOfficeCabinetJuliaSuffix = 3 # Юлия работает
    $ workingOfficeCabinetMonicaSuffix = 6 # Моника сидит (позы 2 и 3, 4- стоит у окна)
    call office_work_init2() from _call_office_work_init2 # Вторичная инициализация работы в офисе
    $ add_hook("Julia", "ep26_quests_office7", scene="working_office_cabinet")

    img black_screen
    with diss
    pause 2.0

    # Инициализация мини-карты
    $ miniMapOfficeActivated = True
    $ autorun_to_object("ep26_dialogues6_office2_minimap_active", scene="working_office_cabinet")
    $ workingOfficeSkipMusicOneTime = True
    call refresh_scene_fade() from _call_refresh_scene_fade_151
    return False

label ep26_quests_office7:
    # Моника говорит с Юлией в обычный день (заставляет работать допоздна)
    if act=="l":
        return
    call ep27_quests_julia1_init() from _call_ep27_quests_julia1_init # Чекаем инициализацию квеста с Юлией
    if day_time == "evening":
        # Юлия работает допоздна
        call ep26_dialogues6_office2_5() from _call_ep26_dialogues6_office2_5
        $ workingOfficeCabinetMonicaSuffix = 1
        call refresh_scene_fade() from _call_refresh_scene_fade_152
        return False
    call ep27_dialogues6_julia0() from _call_ep27_dialogues6_julia0 # Регулярный выбор Юлии когда она сидит
    if _return == False:
#        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_171
        return False
    if _return == 1: # Заставить Юлию работать допоздна
        call ep26_dialogues6_office2_7() from _call_ep26_dialogues6_office2_7
        if _return == False:
            $ workingOfficeCabinetMonicaSuffix = 2
            call refresh_scene_fade() from _call_refresh_scene_fade_153
            return False
#        $ questHelp("julia_1", skipIfExists=True)
#        $ questHelpDesc("julia_desc1")
        $ questHelpFlag25+=1
        if questHelpFlag25 >= 2:
            $ questHelp("office_27", True)
            $ questHelp("office_28", skipIfExists=True)

        call office_work_begin2() from _call_office_work_begin2 # Рабочий день скипается с Юлией
        call ep26_dialogues6_office2_8() from _call_ep26_dialogues6_office2_8
    if _return == 2: # Заставить Юлию собирать отчеты
        call ep27_quests_office8_julia() from _call_ep27_quests_office8_julia
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_172
        return False
    if _return == 3: #Отношения с Юлией
        call ep27_quests_julia1_relationships() from _call_ep27_quests_julia1_relationships
        return False

    return
