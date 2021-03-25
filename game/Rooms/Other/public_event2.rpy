default publicEvent2MonicaSuffix = 1

default publicEvent2MonicaCommentCount = 0
label public_event2:
    $ print "enter_public_event2"
    $ miniMapData = []
    $ scene_image = "scene_PublicEvent2"

    if len(ep211_quests_guests_progress) == 0:
        $ set_active("Investor1", True)
        $ remove_objective("talk_people")
        $ add_objective("talk_investor1", t_("Пообщаться с Мистером Кэмпбеллом."), c_blue, 95)
    else:
        if len(ep211_quests_guests_progress) == 1:
            $ set_active("PublicGuest7", True) # появляется дизайнер

        $ ep211_quests_guests_progress_cur = 9-len(ep211_quests_guests_progress)
        $ add_objective("talk_people", t_("Пообщаться с гостями ([ep211_quests_guests_progress_cur]/9)."), c_orange, 95)

    music crowd10
    show screen Reporters_Shoots_Screen4_low()

    music2 Poppers_and_Prosecco
    return

label public_event2_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "PublicEvent2_Monica[publicEvent2MonicaSuffix]", "click" : "public_event2_environment", "actions" : "l", "zorder":16}, scene="public_event2")

    $ add_object_to_scene("Biff", {"type" : 2, "base" : "PublicEvent2_Biff", "click" : "public_event2_environment", "actions" : "l", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("FitnessRebecca", {"type" : 2, "base" : "PublicEvent2_FitnessRebecca", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("FitnessStephanie", {"type" : 2, "base" : "PublicEvent2_FitnessStephanie", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("Investor1", {"type" : 2, "base" : "PublicEvent2_Investor1", "click" : "public_event2_environment", "actions" : "lt", "zorder":15}, scene="public_event2")
    $ add_object_to_scene("PublicGuest1", {"type" : 2, "base" : "PublicEvent2_PublicGuest1", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest2", {"type" : 2, "base" : "PublicEvent2_PublicGuest2", "click" : "public_event2_environment", "actions" : "lt", "zorder":11}, scene="public_event2")
    $ add_object_to_scene("PublicGuest3", {"type" : 2, "base" : "PublicEvent2_PublicGuest3", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest4", {"type" : 2, "base" : "PublicEvent2_PublicGuest4", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest5", {"type" : 2, "base" : "PublicEvent2_PublicGuest5", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest6", {"type" : 2, "base" : "PublicEvent2_PublicGuest6", "click" : "public_event2_environment", "actions" : "lt", "zorder":11}, scene="public_event2")
    $ add_object_to_scene("PublicGuest7", {"type" : 2, "base" : "PublicEvent2_PublicGuest7", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest8", {"type" : 2, "base" : "PublicEvent2_PublicGuest8", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label public_event2_teleport:
    if obj_name == "Teleport_Bathroom":
        call change_scene("juliahome_bathroom") from _rcall_change_scene_57
    return
label public_event2_environment:
    if obj_name == "Monica":
        if publicEvent2MonicaCommentCount%4 == 0:
            call ep211_dialogues2_public_event_36() from _rcall_ep211_dialogues2_public_event_36
        if publicEvent2MonicaCommentCount%4 == 1:
            call ep211_dialogues2_public_event_37() from _rcall_ep211_dialogues2_public_event_37
        if publicEvent2MonicaCommentCount%4 == 2:
            call ep211_dialogues2_public_event_38() from _rcall_ep211_dialogues2_public_event_38
        if publicEvent2MonicaCommentCount%4 == 3:
            call ep211_dialogues2_public_event_39() from _rcall_ep211_dialogues2_public_event_39
        $ publicEvent2MonicaCommentCount += 1
    if obj_name == "Biff":
        if act=="l":
            call ep211_dialogues2_public_event_40() from _rcall_ep211_dialogues2_public_event_40
    if obj_name == "FitnessRebecca":
        if act=="l":
            call ep211_dialogues2_public_event_24() from _rcall_ep211_dialogues2_public_event_24
    if obj_name == "FitnessStephanie":
        if act=="l":
            call ep211_dialogues2_public_event_24() from _rcall_ep211_dialogues2_public_event_24_1
    if obj_name == "Investor1":
        if act=="l":
            call ep211_dialogues2_public_event_34() from _rcall_ep211_dialogues2_public_event_34
    if obj_name == "PublicGuest1":
        if act=="l":
            call ep211_dialogues2_public_event_8() from _rcall_ep211_dialogues2_public_event_8
    if obj_name == "PublicGuest2":
        if act=="l":
            call ep211_dialogues2_public_event_11() from _rcall_ep211_dialogues2_public_event_11
    if obj_name == "PublicGuest3":
        if act=="l":
            call ep211_dialogues2_public_event_14() from _rcall_ep211_dialogues2_public_event_14
    if obj_name == "PublicGuest4":
        if act=="l":
            call ep211_dialogues2_public_event_17() from _rcall_ep211_dialogues2_public_event_17
    if obj_name == "PublicGuest5":
        if act=="l":
            call ep211_dialogues2_public_event_20() from _rcall_ep211_dialogues2_public_event_20
    if obj_name == "PublicGuest6":
        if act=="l":
            call ep211_dialogues2_public_event_20() from _rcall_ep211_dialogues2_public_event_20_1
    if obj_name == "PublicGuest7":
        if act=="l":
            call ep211_dialogues2_public_event_32() from _rcall_ep211_dialogues2_public_event_32

    if obj_name == "PublicGuest8":
        if act=="l":
            call ep211_dialogues2_public_event_27() from _rcall_ep211_dialogues2_public_event_27
    return
