default melanie_control_active = False

label ep29_quests_melanie_control1_init:
    # Переход управления на Мелани
    $ remove_hook(label="change_owner_default_hook")
    $ add_hook("change_owner", "change_owner_default", scene="global", label="change_owner_default_hook")

    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Dick_Entrance_Melanie_[melanie_cloth]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="dick_office_entrance")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Dick_Hall1_Melanie_[melanie_cloth]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="dick_office_hall1")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Dick_Secretary_Melanie_[melanie_cloth]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="dick_office_secretary")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Entrance_Monica_Melanie_[melanie_cloth]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_entrance")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Monica_Cabinet_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_cabinet")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Monica_Cabinet_Table_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_cabinet_table")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Melanie[makeupRoomMelanieSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10, "active":False}, {"melanie_control_active":{"v":True, "base":"Office_Monica_MakeupRoom_Melanie_[melanie_cloth]", "actions" : "l"}}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Melanie[photostudioMelanieSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10}, {"melanie_control_active":{"v":True, "base":"Office_Monica_PhotoStudio_Melanie_[melanie_cloth]", "actions" : "l"}}, scene="monica_office_photostudio")
    $ add_object_to_scene("Melanie", {"type" : 2, "active":False, "base" : "Office_Monica_Secretary_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="monica_office_secretary")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "WorkingOffice_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":10}, scene="working_office")
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "WorkingOfficeCabinet_Melanie_[melanie_cloth][day_suffix]", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":10}, scene="working_office_cabinet")

    $ set_active("Melanie", True, scene="World", recursive=True)
    $ set_active("Monica", False, scene="World", recursive=True)

    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="dick_office_entrance", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="dick_office_hall1", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f", scene="dick_office_secretary", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="monica_office_entrance", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="monica_office_cabinet", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="monica_office_makeup_room", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="monica_office_photostudio", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="monica_office_secretary", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="working_office", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1nn", scene="working_office_cabinet", owner="Melanie", label="melanie_play_interact")
    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1oo", scene="melanie_home", owner="Melanie", label="melanie_play_interact")

    # хождение
    $ add_hook("Teleport_Monica_Office_Photostudio", "ep29_quests_melanie_teleport_photostudio", scene="monica_office_makeup_room", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_MakeupRoom", "ep29_quests_melanie_teleport_makeuproom", scene="monica_office_photostudio", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_secretary", scene="monica_office_photostudio", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Photostudio", "ep29_quests_melanie_teleport_photostudio", scene="monica_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep29_quests_melanie_teleport_monica_cabinet", scene="monica_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep29_quests_melanie_teleport_lift", scene="monica_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_secretary", scene="monica_office_cabinet", owner="Melanie", label="melanie_teleports")
    $ add_hook("Biff", "ep29_quests_melanie_teleport_monica_cabinet_table", scene="monica_office_cabinet", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_secretary", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Lift", "ep29_quests_melanie_teleport_lift", scene="working_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_WorkingOffice2", "ep29_quests_melanie_teleport_melanie_workingoffice2", scene="working_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Cabinet", "ep29_quests_melanie_teleport_melanie_workingoffice_cabinet", scene="working_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Cabinet", "ep29_quests_melanie_teleport_melanie_workingoffice_cabinet", scene="working_office2", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Cabinet", "ep29_dialogues3_melanie_monica_victoria_3d", scene="working_office", owner="Melanie", label="melanie_teleports_monica_restrict")
    $ add_hook("Teleport_Cabinet", "ep29_dialogues3_melanie_monica_victoria_3d", scene="working_office2", owner="Melanie", label="melanie_teleports_monica_restrict")
    $ add_hook("Teleport_WorkingOffice", "ep29_quests_melanie_teleport_melanie_workingoffice", scene="working_office2", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_WorkingOffice", "ep29_quests_melanie_teleport_melanie_workingoffice", scene="working_office_cabinet", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Monica_Office_Secretary", "ep29_quests_melanie_teleport_lift", scene="monica_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Street_Monica_Office", "ep29_quests_melanie_teleport_monica_office_street", scene="monica_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Inside", "ep29_quests_melanie_teleport_monica_office_entrance", scene="street_monica_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Inside", "ep29_quests_melanie_teleport_dick_office_entrance", scene="street_dick_office", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Street", "ep29_quests_melanie_teleport_dick_office_street", scene="dick_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Inside", "ep29_quests_melanie_teleport_dick_office_hall1", scene="dick_office_entrance", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Entrance", "ep29_quests_melanie_teleport_dick_office_entrance2", scene="dick_office_hall1", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Secretary", "ep29_quests_melanie_teleport_dick_secretary", scene="dick_office_hall1", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Hall", "ep29_quests_melanie_teleport_dick_office_hall1b", scene="dick_office_secretary", owner="Melanie", label="melanie_teleports")
    $ add_hook("Teleport_Map", "melanie_home_teleport", scene="melanie_home", owner="Melanie", label="melanie_teleports")


    # Предметы и персонажи
    # makeup room
    $ add_hook("MelaniePhoto1", "ep29_dialogues3_melanie_monica_victoria_1a", scene="monica_office_makeup_room", owner="Melanie", label="melanie_environment")
    $ add_hook("MelaniePhoto2", "ep29_dialogues3_melanie_monica_victoria_1b", scene="monica_office_makeup_room", owner="Melanie", label="melanie_environment")
    $ add_hook("Mirror1", "ep29_dialogues3_melanie_monica_victoria_1c", scene="monica_office_makeup_room", owner="Melanie", label="melanie_environment")
    $ add_hook("Mirror2", "ep29_dialogues3_melanie_monica_victoria_1c", scene="monica_office_makeup_room", owner="Melanie", label="melanie_environment")
    $ add_hook("Table2", "ep29_dialogues3_melanie_monica_victoria_1d", scene="monica_office_makeup_room", owner="Melanie", label="melanie_environment")
    $ add_hook("Boxes", "ep29_dialogues3_melanie_monica_victoria_1e", scene="monica_office_makeup_room", owner="Melanie", label="melanie_environment")

    #photstudio
    $ add_hook("Cloth", "ep29_dialogues3_melanie_monica_victoria_1g", scene="monica_office_photostudio", owner="Melanie", label="melanie_environment")
    $ add_hook("SpotLight1", "ep29_dialogues3_melanie_monica_victoria_1h", scene="monica_office_photostudio", owner="Melanie", label="melanie_environment")
    $ add_hook("SpotLight2", "ep29_dialogues3_melanie_monica_victoria_1h", scene="monica_office_photostudio", owner="Melanie", label="melanie_environment")
    $ add_hook("SpotLight3", "ep29_dialogues3_melanie_monica_victoria_1h", scene="monica_office_photostudio", owner="Melanie", label="melanie_environment")
    $ add_hook("SpotLight4", "ep29_dialogues3_melanie_monica_victoria_1h", scene="monica_office_photostudio", owner="Melanie", label="melanie_environment")

    #monica secretary
    $ add_hook("Teatable", "ep29_dialogues3_melanie_monica_victoria_1k", scene="monica_office_secretary", owner="Melanie", label="melanie_environment")
    $ add_hook("Books1", "ep29_dialogues3_melanie_monica_victoria_1k", scene="monica_office_secretary", owner="Melanie", label="melanie_environment")
    $ add_hook("Books2", "ep29_dialogues3_melanie_monica_victoria_1k", scene="monica_office_secretary", owner="Melanie", label="melanie_environment")
    $ add_hook("Table", "ep29_dialogues3_melanie_monica_victoria_1k", scene="monica_office_secretary", owner="Melanie", label="melanie_environment")
    $ add_hook("Music_Instrument", "ep29_dialogues3_melanie_monica_victoria_1k", scene="monica_office_secretary", owner="Melanie", label="melanie_environment")
    $ add_hook("Globe", "ep29_dialogues3_melanie_monica_victoria_1k", scene="monica_office_secretary", owner="Melanie", label="melanie_environment")

    # monica cabinet
    $ add_hook("Flowers", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Paints", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Projector", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Table", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Windows", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet", owner="Melanie", label="melanie_environment")
    # monica cabinet table
    $ add_hook("Flowers", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_environment")
    $ add_hook("Paints", "ep29_dialogues3_melanie_monica_victoria_1p", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_environment")
    $ add_hook("Whiskey", "ep29_dialogues3_melanie_monica_victoria_1o", scene="monica_office_cabinet_table", owner="Melanie", label="melanie_environment")
    # working office cabinet
    $ add_hook("Chair1", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Chair2", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("JuliaComputer", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("JuliaFolders", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("MonicaChair", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("MonicaComputer", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Picture", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Requisite", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    $ add_hook("Tree", "ep29_dialogues3_melanie_monica_victoria_1x", scene="working_office_cabinet", owner="Melanie", label="melanie_environment")
    # dick secretary
    $ add_hook("Door", "ep29_dialogues3_melanie_monica_victoria_1bb", scene="dick_office_secretary", owner="Melanie", label="melanie_environment")
    # melanie home
    $ add_hook("Chair", "ep29_dialogues3_melanie_monica_victoria_1ff", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Lamp1", "ep29_dialogues3_melanie_monica_victoria_1ff", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Lamp2", "ep29_dialogues3_melanie_monica_victoria_1ff", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Photo1", "ep29_dialogues3_melanie_monica_victoria_1dd", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Photo2", "ep29_dialogues3_melanie_monica_victoria_1dd", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Photo3", "ep29_dialogues3_melanie_monica_victoria_1dd", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Photo4", "ep29_dialogues3_melanie_monica_victoria_1dd", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Photo5", "ep29_dialogues3_melanie_monica_victoria_1dd", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Sofa", "ep29_dialogues3_melanie_monica_victoria_1ff", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Sofa2", "ep29_dialogues3_melanie_monica_victoria_1ff", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("TV", "ep29_dialogues3_melanie_monica_victoria_1ff", scene="melanie_home", owner="Melanie", label="melanie_environment")
    $ add_hook("Wine", "ep29_dialogues3_melanie_monica_victoria_1ee", scene="melanie_home", owner="Melanie", label="melanie_environment")

    # События
    $ add_hook("AlexPhotograph", "ep29_quests_melanie_alex1", scene="monica_office_photostudio", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Secretary", "ep29_quests_melanie_secretary1", scene="monica_office_secretary", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Biff", "ep29_quests_melanie_biff1", scene="monica_office_cabinet", owner="Melanie", label="melanie_dialogues")
    $ move_object("Julia", "working_office_cabinet")
    $ add_hook("Julia", "ep29_dialogues3_melanie_monica_victoria_1u", scene="working_office_cabinet", owner="Melanie", label="melanie_dialogues")
    $ move_object("Monica", "working_office_cabinet")
    $ add_hook("Monica", "ep29_quests_melanie_monica1", scene="working_office_cabinet", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Reception", "ep29_quests_melanie_dick_Reception", scene="dick_office_entrance", owner="Melanie", label="melanie_dialogues")
    $ add_hook("DickSecretary", "ep29_quests_melanie_victoria1", scene="dick_office_secretary", owner="Melanie", label="melanie_dialogues")
    $ set_var("Monica", actions="lt", scene="working_office_cabinet")

    $ add_hook("enter_scene", "ep29_quests_melanie_biff_comment1", scene="monica_office_cabinet", owner="Melanie", label="melanie_popup_messages")
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1q", scene="monica_office_entrance", owner="Melanie", label="melanie_popup_messages", once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1gg", scene="street_monica_office", owner="Melanie", label="melanie_popup_messages", once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1jj", scene="dick_office_entrance", owner="Melanie", label="melanie_popup_messages", once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1mm", scene="monica_office_photostudio", owner="Melanie", label="melanie_popup_messages", once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_1oo", scene="melanie_home", owner="Melanie", label=["melanie_popup_messages", "melanie_popup_messages_early"], once=True)
    $ add_hook("enter_scene", "ep29_dialogues3_melanie_monica_victoria_3", scene="working_office", owner="Melanie", label="melanie_popup_messages", once=True)

    # Сотрудники
    $ stored_scene = store_scene("working_office")
    $ set_var("Worker1", actions = "l", active=True, scene="working_office")
    $ set_var("Worker2", actions = "l", active=True, scene="working_office")
    $ set_var("Worker3", actions = "l", active=True, scene="working_office")
    $ set_var("Worker4", actions = "l", active=True, scene="working_office")
    $ set_var("Worker5", actions = "l", active=True, scene="working_office")
    $ set_var("Worker6", actions = "l", active=True, scene="working_office")
    $ set_var("Worker7", actions = "l", active=True, scene="working_office")
    $ set_var("Worker3", actions = "l", active=True, scene="working_office2")
    $ set_var("Worker4", actions = "l", active=True, scene="working_office2")
    $ set_var("Worker6", actions = "l", active=True, scene="working_office2")
    $ set_var("Worker7", actions = "l", active=True, scene="working_office2")
    $ add_hook("Worker1", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker2", "ep29_dialogues3_melanie_monica_victoria_1t", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker3", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker4", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker5", "ep29_dialogues3_melanie_monica_victoria_1s", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker6", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker7", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker3", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office2", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker4", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office2", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker6", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office2", owner="Melanie", label="melanie_dialogues")
    $ add_hook("Worker7", "ep29_dialogues3_melanie_monica_victoria_1r", scene="working_office2", owner="Melanie", label="melanie_dialogues")



    call change_owner("Melanie") from _call_change_owner_6
    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : t_("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "active", "owner":"Melanie"},
            "Teleport_Dick_Office" : {"text" : t_("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "visible", "owner":"Melanie"},
            "Teleport_Melanie_Home" : {"text" : t_("АПАРТАМЕНТЫ МЕЛАНИ"), "xpos" : 1726, "ypos" : 791, "base" : "map_marker", "state" : "visible", "owner":"Melanie"}
    }
    $ hudDaySkipToEveningEnabled = False
    $ miniMapTurnedOff2 = True # выключаем minimap
    call change_scene("monica_office_makeup_room", "Fade_long", False) from _call_change_scene_450
#    $ add_hook("Melanie", "ep29_dialogues3_melanie_monica_victoria_1f"
    return

label ep29_quests_melanie_control1_uninit:
    $ set_var("Monica", actions="l", scene="working_office_cabinet")
    $ miniMapTurnedOff2 = False
    $ hudDaySkipToEveningEnabled = True
    call change_owner("Monica") from _call_change_owner_7
    $ restore_scene(stored_scene)
    $ set_active("Monica", True, scene="World", recursive=True)
    $ set_active("Melanie", False, scene="World", recursive=True)
    return

label ep29_quests_melanie_teleport_photostudio:
    call change_scene("monica_office_photostudio") from _call_change_scene_451
    return False

label ep29_quests_melanie_teleport_makeuproom:
    call change_scene("monica_office_makeup_room") from _call_change_scene_452
    return False

label ep29_quests_melanie_teleport_secretary:
    call change_scene("monica_office_secretary") from _call_change_scene_453
    return False

label ep29_quests_melanie_teleport_monica_cabinet:
    call change_scene("monica_office_cabinet") from _call_change_scene_454
    return False

label ep29_quests_melanie_teleport_lift:
    menu:
        "Модный Журнал.":
            call change_scene("monica_office_secretary", "Fade_long", "snd_lift") from _call_change_scene_455
        "Офисы.":
            call change_scene("working_office", "Fade_long", "snd_lift") from _call_change_scene_456
        "Вестибюль.":
            call change_scene("monica_office_entrance", "Fade_long", "snd_lift") from _call_change_scene_457
    return False


label ep29_quests_melanie_teleport_monica_cabinet_table:
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1o() from _call_ep29_dialogues3_melanie_monica_victoria_1o_2
        return False
    call change_scene("monica_office_cabinet_table") from _call_change_scene_458
    return False

label ep29_quests_melanie_teleport_melanie_workingoffice:
    call change_scene("working_office") from _call_change_scene_459
    return False

label ep29_quests_melanie_teleport_melanie_workingoffice2:
    call change_scene("working_office2") from _call_change_scene_460
    return False

label ep29_quests_melanie_teleport_melanie_workingoffice_cabinet:
    call change_scene("working_office_cabinet", "Fade_long", "snd_door_open1") from _call_change_scene_461
    return False


label ep29_quests_melanie_teleport_monica_office_street:
    call change_scene("street_monica_office", "Fade_long") from _call_change_scene_462
    return False

label ep29_quests_melanie_teleport_monica_office_entrance:
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1mm() from _call_ep29_dialogues3_melanie_monica_victoria_1mm
        return False
    call change_scene("monica_office_entrance", "Fade_long") from _call_change_scene_463
    return False

label ep29_quests_melanie_teleport_dick_office_entrance:
    if act=="l":
        call ep29_dialogues3_melanie_monica_victoria_1jj() from _call_ep29_dialogues3_melanie_monica_victoria_1jj
        return False
    call change_scene("dick_office_entrance", "Fade_long") from _call_change_scene_464
    return False

label ep29_quests_melanie_teleport_dick_office_entrance2:
    call change_scene("dick_office_entrance", "Fade_long", "snd_lift") from _call_change_scene_465
    return False

label ep29_quests_melanie_teleport_dick_office_street:
    call change_scene("street_dick_office", "Fade_long") from _call_change_scene_466
    return False

label ep29_quests_melanie_teleport_dick_office_hall1:
    call change_scene("dick_office_hall1", "Fade_long", "snd_lift") from _call_change_scene_467
    return False

label ep29_quests_melanie_teleport_dick_office_hall1b:
    call change_scene("dick_office_hall1") from _call_change_scene_468
    return False

label ep29_quests_melanie_teleport_dick_secretary:
    call change_scene("dick_office_secretary") from _call_change_scene_469
    return False






#
