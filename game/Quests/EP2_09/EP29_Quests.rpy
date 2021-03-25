default ep29_quests_initialized = False
default ep29_quests_fix2_initialized = False

label ep29_quests_init:
    if ep29_quests_initialized == False:
        $ ep29_quests_initialized = True
        $ set_active ("Pub_Washbasin", False, scene="pub")
    if ep29_quests_fix2_initialized == False:
        if melanie_control_active == True and ep29_melanie_refused_visit_victoria == False and ep29_monica_refused_visit_victoria == False and ep29_quests_victoria_event_completed == False:
            $ miniMapTurnedOff2 = True
            $ set_active(True, teleport=True, scene="working_office") # Включаем телепорты

        $ ep29_quests_fix2_initialized = True

    return
