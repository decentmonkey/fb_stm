default officeMonicaVisitedByWorker1_cnt = 0
default officeMonicaVisitedByWorker2_cnt = 0
default officeMonicaVisitedByWorker3_cnt = 0
default officeMonicaVisitedByWorker4_cnt = 0
default officeMonicaVisitedByWorker5_cnt = 0
default officeMonicaVisitedByWorker6_cnt = 0
default officeMonicaVisitedByWorker7_cnt = 0

default officeWorker2BlockedUntilDay = 0

label ep26_quests_office_workers1:
    # Клик на работников
    if obj_name == "Worker1":
        if act=="l":
            call worker1_look() from _call_worker1_look
            call refresh_scene_fade() from _call_refresh_scene_fade_131
        if act=="t":
            call worker1_dialogue_workplace() from _call_worker1_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_132
    if obj_name == "Worker2":
        if act=="l":
            call worker2_look() from _call_worker2_look
            call refresh_scene_fade() from _call_refresh_scene_fade_133
        if act=="t":
            call worker2_dialogue_workplace() from _call_worker2_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_134
    if obj_name == "Worker3":
        if act=="l":
            call worker3_look() from _call_worker3_look
            call refresh_scene_fade() from _call_refresh_scene_fade_135
        if act=="t":
            call worker3_dialogue_workplace() from _call_worker3_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_136
    if obj_name == "Worker4":
        if act=="l":
            call worker4_look() from _call_worker4_look
            call refresh_scene_fade() from _call_refresh_scene_fade_137
        if act=="t":
            call worker4_dialogue_workplace() from _call_worker4_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_138
    if obj_name == "Worker5":
        if act=="l":
            call worker5_look() from _call_worker5_look
            call refresh_scene_fade() from _call_refresh_scene_fade_139
        if act=="t":
            call worker5_dialogue_workplace() from _call_worker5_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_140
    if obj_name == "Worker6":
        if act=="l":
            call worker6_look() from _call_worker6_look
            call refresh_scene_fade() from _call_refresh_scene_fade_141
        if act=="t":
            call worker6_dialogue_workplace() from _call_worker6_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_142
    if obj_name == "Worker7":
        if act=="l":
            call worker7_look() from _call_worker7_look
            call refresh_scene_fade() from _call_refresh_scene_fade_143
        if act=="t":
            call worker7_dialogue_workplace() from _call_worker7_dialogue_workplace
            call refresh_scene_fade() from _call_refresh_scene_fade_144

    return

label ep26_quests_office_workers2(amount):
    # Работники заходят к Монике (сколько вызовов, столько и приходов)
    $ workersToVisit = [1,2,3,4,5,6,7]
    if officeWorker2BlockedUntilDay >= day:
        $ workersToVisit.remove(2)
    $ workersList = random.sample(set(workersToVisit), amount)
    $ idx = 0
    label ep26_quests_office_workers2_loop1:
        music stop
        img black_screen
        with diss
        pause 1.0
        sound snd_door_open1
        pause 0.5
        if idx >= len(workersList):
            return
        $ workerIdx = workersList[idx]
        if workerIdx == 1:
            call worker1_dialogue_office() from _call_worker1_dialogue_office
            $ officeMonicaVisitedByWorker1_cnt += 1
        if workerIdx == 2:
            call worker2_dialogue_office() from _call_worker2_dialogue_office
            $ officeMonicaVisitedByWorker2_cnt += 1
        if workerIdx == 3:
            call worker3_dialogue_office() from _call_worker3_dialogue_office
            $ officeMonicaVisitedByWorker3_cnt += 1
        if workerIdx == 4:
            call worker4_dialogue_office() from _call_worker4_dialogue_office
            $ officeMonicaVisitedByWorker4_cnt += 1
        if workerIdx == 5:
            call worker5_dialogue_office() from _call_worker5_dialogue_office
            $ officeMonicaVisitedByWorker5_cnt += 1
        if workerIdx == 6:
            call worker6_dialogue_office() from _call_worker6_dialogue_office
            $ officeMonicaVisitedByWorker6_cnt += 1
        if workerIdx == 7:
            call worker7_dialogue_office() from _call_worker7_dialogue_office
            $ officeMonicaVisitedByWorker7_cnt += 1
        music stop
        img black_screen
        with diss
        sound snd_door_close1
        pause 1.0
    # Выбираем случайного работника
    return
