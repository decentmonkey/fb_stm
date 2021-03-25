default ep27_quests_initialized = False
label ep27_quests1:
    # Инициализация v0.7
    if char_info.has_key("Bartender") == False:
        call characters_pub_init() from _call_characters_pub_init_1
    $ char_info["Bartender"]["enabled"] = True

    if photoshoot7_count > 0:
        $ monicaOutfitsEnabled[7] = True # Открываем следующий костюм (черный лебедь)
        $ questHelp("photoshoot_7", skipIfExists=True)

    # Мелани
    call ep27_quests_melanie1_init() from _call_ep27_quests_melanie1_init

    if renpy.seen_label("ep24_dialogues3_steve10"): # Еще раз принудительно бреем Монику после посещения Стива дома
        $ monicaPussyShaved = True

    $ currentMusicPriority = 0
    $ ep27_quests_initialized = True
    return
