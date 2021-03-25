default ep216_office_blocked_day = 0

label ep216_quests_biff_block_office: # закрываем доступ в офис на неделю
    $ ep216_office_blocked_day = day + 14
    $ add_hook("Teleport_Monica_Office_Secretary", "ep216_quests_biff_block_office_blocked", scene="monica_office_entrance", label="ep216_quests_biff_block_office", priority=1002)
    $ monicaWorkFlashCardQuestReportsNeedTalkBiff = False
    $ remove_objective("reports_to_biff")
    call putoff_work_clothes() from _rcall_putoff_work_clothes_12
    sound snd_fabric1
    fadeblack 2.0
    $ autorun_to_object("ep216_dialogues0_biff2b", scene="street_monica_office")
    call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_189
    return

label ep216_quests_biff_block_office_blocked:
    if ep216_office_blocked_day < day:
        $ remove_hook()
        return
    call ep216_dialogues0_biff2b() from _rcall_ep216_dialogues0_biff2b
    return False
