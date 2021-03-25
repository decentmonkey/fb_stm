default ep216_quests_julia1_start_day = 0
default ep216_juliahome_blocked_day = 0

label ep216_quests_julia1_start:
    $ ep216_quests_julia1_start_day = day
    call ep216_dialogues4_fred_1() from _rcall_ep216_dialogues4_fred_1
    sound snd_fabric1
    fadeblack 2.0
    $ cloth = monica_juliahome_outside_cloth
    $ cloth_type = monica_juliahome_outside_cloth_type
    $ juliaNotifBlockedOnce = True
    call change_scene("street_juliahome", "Fade_long") from _rcall_change_scene_190
    $ autorun_to_object("ep216_dialogues4_fred_2", scene="street_juliahome")
    $ ep216_juliahome_blocked_day = day
    $ add_hook("JuliaHome", "ep216_quests_julia2_blockhome", scene="street_juliahome", label=["ep216_quests_julia2_blockhome", "day_time_temp"])
    $ add_talk("Julia", "ep216_quests_julia3_julia", scene="working_office_cabinet", label="ep216_quests_julia3_julia")
    $ add_talk("Driver", "ep216_quests_julia4_fred", scene="street_house_main_yard", label="ep216_quests_julia4_fred")
    return

label ep216_quests_julia2_blockhome:
    call ep216_dialogues4_fred_4() from _rcall_ep216_dialogues4_fred_4
    return False

label ep216_quests_julia3_julia:
    if day_time != "day":
        return
    $ remove_hook()
    call ep216_dialogues4_fred_5() from _rcall_ep216_dialogues4_fred_5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_118
    return False

label ep216_quests_julia4_fred: # Моника при клике на Фреда после его визита к Юлии в квартиру, мысли
    call ep216_dialogues4_fred_6() from _rcall_ep216_dialogues4_fred_6
    return False
