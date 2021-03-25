default ep26_quests_initialized = False
label ep26_quests1:
    # Инициализация v0.6
    $ ep26_quests_initialized = True
    $ add_hook_day("ep26_quests_steve1", week_day = 6) # вешаем сброс посещений офиса Стива каждую субботу утром
    if melanieDisappeared == True:
        $ monicaOutfitsEnabled[5] = True # Открываем следующий костюм
        $ questHelp("photoshoot_5", skipIfExists=True)
        $ autorun_to_object("ep26_dialogues5_office1_1", scene="monica_office_cabinet_table")


    if monicaMustNotWearPanties == True and bettyMustNotWearPanties == True:
        call ep26_quests_bardie1() from _call_ep26_quests_bardie1_1

    return
