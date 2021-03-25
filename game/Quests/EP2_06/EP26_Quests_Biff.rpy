default monicaKissedBiff = False

default ep26_quests_biff1_Flag = False
default ep26_quest_work_start_day = 0

label ep26_quests_biff1:
    if ep26_quests_biff1_Flag != False or monicaWorkingAtBiffOffice == True:
#        $ remove_hook(label="biff_work_dialogue1")
        return
    # Инициализируем разговор о работе в офисе
    $ questHelp("office_24", skipIfExists=True)
    $ add_hook("Biff", "ep26_quests_biff2", scene="monica_office_cabinet_table", label="biff_work_dialogue1")
    $ ep26_quests_biff1_Flag = True
    return

label ep26_quests_biff2:
    if monicaWorkingAtBiffOffice == True:
        $ remove_hook(label="biff_work_dialogue1")
        return
    # Разговор с Бифом о работе
    if act=="l":
        return
    if cloth != "CasualDress1" and cloth_type != "WorkingOutfit":
        call ep26_dialogues5_office1_1a2() from _call_ep26_dialogues5_office1_1a2 # Говорим о том что надо одеть платье
        return

    call process_hooks("photoshoots_work_available_check", "global") from _call_process_hooks_65
    if biffWeeklyPhotoShootEnabled == False or _return == False:
        return

    call ep26_dialogues5_office1_2() from _call_ep26_dialogues5_office1_2
    if _return == False:
        call change_scene("monica_office_secretary") from _call_change_scene_320
        return False
    $ questHelp("office_24", True)
    $ questHelp("melanie_6b", True)
    $ questHelp("melanie_7")
    $ questHelp("office_25")
    $ questHelpDesc("melanie_desc6a", False)
    $ questHelpDesc("melanie_desc6", "melanie_desc7")
    # Начинаем подготовку к работе
    # Моника идет к секретарше

    $ ep26_quest_work_start_day = day

    $ remove_hook(label="biff_work_dialogue1")

    # блокируем выходы
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block1")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block1")
    $ add_hook("Secretary", "ep26_quests_biff3", scene="monica_office_secretary")
    call change_scene("monica_office_secretary") from _call_change_scene_321

    return False

label ep26_quests_biff3:
    # Говорим с секретаршей
    if act=="l":
        return
    $ remove_hook()
    call ep26_dialogues5_office1_2b() from _call_ep26_dialogues5_office1_2b
    $ remove_hook(label="biff_work_block1")
    # блокируем выходы
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_2a", scene="monica_office_secretary", label="biff_work_block2")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep26_dialogues5_office1_2a", scene="monica_office_secretary", label="biff_work_block2")
    $ add_hook("Secretary", "ep26_dialogues5_office1_2a", scene="monica_office_secretary", label="biff_work_block2")

    $ add_hook("AlexPhotograph", "ep26_quests_biff4", scene="monica_office_photostudio")
    return False

label ep26_quests_biff4:
    # Говорим с Алексом
    if act=="l":
        return
    $ remove_hook()
    call ep26_dialogues5_office1_3() from _call_ep26_dialogues5_office1_3
    $ remove_hook(label="biff_work_block2")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block3")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep26_dialogues5_office1_1a", scene="monica_office_secretary", label="biff_work_block3")

    $ add_hook("Secretary", "ep26_quests_biff5", scene="monica_office_secretary")
    call put_work_clothes() from _call_put_work_clothes_3 # Одеваем Монику в рабочую одежду

    return False

label ep26_quests_biff5:
    # Говорим с секретаршей
    if act=="l":
        return
    $ remove_hook()
    call ep26_dialogues5_office1_4() from _call_ep26_dialogues5_office1_4
    $ remove_hook(label="biff_work_block3")

    $ questHelp("office_25", True)
    $ questHelp("office_26")
    $ questHelpDesc("office_desc9")

    # возвращаем Мелани
    call ep26_quests_melanie1() from _call_ep26_quests_melanie1
    $ questHelp("melanie_6b", True)
    $ questHelp("melanie_7")

    $ remove_hook(label="biff_work_dialogue1")
    $ monicaWorkingAtBiffOffice = True

    # инициализируем работу в офисе
    call office_work_init() from _call_office_work_init
    call ep26_quests_office1() from _call_ep26_quests_office1

    $ add_hook("before_open", "ep26_quests_biff6", scene="monica_office_cabinet_table", label=["check_bill_at_place", "check_bill_at_place_cabinet_table"], priority=150)
    return False

label ep26_quests_biff6:
    # Проверяем наличие Бифа в офисе днем при переходе по миникарте
    call ep22_dialogue6_2b() from _call_ep22_dialogue6_2b
    if _return == False:
        call change_scene("monica_office_secretary") from _call_change_scene_322
    return








#
