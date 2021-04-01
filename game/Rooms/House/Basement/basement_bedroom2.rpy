default basement_bedroom2_MonicaSuffix = 2
default basement_bedroom2_MonicaSuffix2 = ""
default basement_bedroom2_Monica_Nap_Betty_Suffix = ""
default basementBedNapSuffix2 = ""
default basement_bedroom2_buttplug_suffix = 1

default basement_bedroom2_ep22_init = False
default basement_bedroom2_ep24_init = False

label basement_bedroom2:
    $ street_house_outside_monica_suffix = 1

    if cloth == "HomeCloth4":
        $ cloth = "Governess" #Принудительно переодеваем Монику в одежду гувернантки
        $ cloth_type = "Governess"

#    if basement_bedroom2_ep22_init == False:
#        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Bedroom2_Monica_[cloth]_[basement_bedroom2_MonicaSuffix][basement_bedroom2_MonicaSuffix2]", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder":10, "tint": [1.0, 1.0, 0.9]}, {"basementBedroomMonicaNapGfxBettyPanties":{"v":True, "base":"Basement_Bedroom2_Monica_Governess_Betty_[monicaBettyPantiesId]_Nap_1", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_Nap_1_Overlay"}, "basementBedroomMonicaNapGfx":{"v":True, "base":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex][basement_bedroom2_Monica_Nap_Betty_Suffix]", "img_overlay":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex]_Overlay"}, "basementBedroomMonicaSleepGfx":{"v":True, "base":"Basement_Bedroom2_Monica_Sleep_[basementBedSleepIndex]"}, "basementBedroomBettyPantiesOnly":{"v":True, "base":"Basement_Bedroom2_Monica_Governess[basement_bedroom2_MonicaSuffix]_Betty_[monicaBettyPantiesId]", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_[basement_bedroom2_MonicaSuffix]_Overlay"}}, scene="basement_bedroom2")
#        $ basement_bedroom2_ep22_init = True
#    if basement_bedroom2_ep24_init == False:
#        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Bedroom2_Monica_[cloth]_[basement_bedroom2_MonicaSuffix][basement_bedroom2_MonicaSuffix2]", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder":10, "tint": [1.0, 1.0, 0.9]}, {"basementBedroomMonicaNapGfxBettyPanties":{"v":True, "base":"Basement_Bedroom2_Monica_Governess_Betty_[monicaBettyPantiesId]_Nap_1", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_Nap_1_Overlay"}, "basementBedroomMonicaNapGfx":{"v":True, "base":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex][basement_bedroom2_Monica_Nap_Betty_Suffix][basementBedNapSuffix2]", "img_overlay":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex]_Overlay"}, "basementBedroomMonicaSleepGfx":{"v":True, "base":"Basement_Bedroom2_Monica_Sleep_[basementBedSleepIndex]"}, "basementBedroomBettyPantiesOnly":{"v":True, "base":"Basement_Bedroom2_Monica_Governess[basement_bedroom2_MonicaSuffix]_Betty_[monicaBettyPantiesId]", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_[basement_bedroom2_MonicaSuffix]_Overlay"}}, scene="basement_bedroom2")
#        $ basement_bedroom2_ep24_init = True

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Bedroom2_Monica_[cloth]_[basement_bedroom2_MonicaSuffix][basement_bedroom2_MonicaSuffix2]", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder":10, "tint": [1.0, 1.0, 0.9]}, {"basementBedroomMonicaNapGfxBettyPanties":{"v":True, "base":"Basement_Bedroom2_Monica_Governess_Betty_[monicaBettyPantiesId]_Nap_1", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_Nap_1_Overlay"}, "basementBedroomMonicaNapGfx":{"v":True, "base":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex][basement_bedroom2_Monica_Nap_Betty_Suffix][basementBedNapSuffix2]", "img_overlay":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex]_Overlay"}, "basementBedroomMonicaSleepGfx":{"v":True, "base":"Basement_Bedroom2_Monica_Sleep_[basementBedSleepIndex]"}, "basementBedroomBettyPantiesOnly":{"v":True, "base":"Basement_Bedroom2_Monica_Governess[basement_bedroom2_MonicaSuffix]_Betty_[monicaBettyPantiesId]", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_[basement_bedroom2_MonicaSuffix]_Overlay"}}, scene="basement_bedroom2")

    $ print "enter_basement_bedroom2"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_5

    $ scene_image = "scene_Basement_Bedroom2"
    $ basementHoleIncomingDirection = "Bedroom"

    $ basementBedroomBettyPantiesOnly = False
    if cloth == "GovernessPants" and monicaBettyPanties == True:
        $ basementBedroomBettyPantiesOnly = True

    $ basement_bedroom2_MonicaSuffix2 = ""
    if cloth == "Nude" and monicaPussyShaved == True and basement_bedroom2_MonicaSuffix == 2:
        $ basement_bedroom2_MonicaSuffix2 = "_Shaved"

    $ basementBedNapSuffix2 = ""
    if basementBedroomMonicaNapGfx == True and basementBedNapIndex == 3 and monicaPussyShaved == True and cloth == "Nude":
        $ basementBedNapSuffix2 = "_Shaved"

    if basementBedroomMonicaNapGfx == True and cloth == "Governess" and monicaUnder == "Nude":
        $ basementBedNapSuffix2 = "_UnderNude"

    if ep29_revenge_quest1_inited == True and check_hook("before_open", "ep29_revenge_quest1_check", scene="basement_bedroom2") == False: # костыль на старт revenge quest
        call ep29_revenge_quest1_init_repeat() from __rcall_ep29_revenge_quest1_init_repeat1
#    music Sneak_n_Get_Caught

    if cloth_type == "BettyCloth":
        $ basement_bedroom2_MonicaSuffix = 1

    music Stealth_Groover

    return

label basement_bedroom2_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Bedroom2_Monica_[cloth]_[basement_bedroom2_MonicaSuffix]", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder":10, "tint": [1.0, 1.0, 0.9]}, {"basementBedroomMonicaNapGfxBettyPanties":{"v":True, "base":"Basement_Bedroom2_Monica_Governess_Betty_[monicaBettyPantiesId]_Nap_1", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_Nap_1_Overlay"}, "basementBedroomMonicaNapGfx":{"v":True, "base":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex][basement_bedroom2_Monica_Nap_Betty_Suffix]", "img_overlay":"Basement_Bedroom2_Monica_[cloth]_Nap_[basementBedNapIndex]_Overlay"}, "basementBedroomMonicaSleepGfx":{"v":True, "base":"Basement_Bedroom2_Monica_Sleep_[basementBedSleepIndex]"}, "basementBedroomBettyPantiesOnly":{"v":True, "base":"Basement_Bedroom2_Monica_Governess[basement_bedroom2_MonicaSuffix]_Betty_[monicaBettyPantiesId]", "img_overlay":"Basement_Bedroom2_Monica_GovernessPants_[basement_bedroom2_MonicaSuffix]_Overlay"}}, scene="basement_bedroom2")

#    if basementBedroomJournal == True:
#        $ add_object_to_scene("Journal", {"type":2, "base":"Basement_Bedroom2_Journal", "click" : "basement_bedroom2_environment", "actions" : "lw", "zorder" : 1})

    $ add_object_to_scene("BasementBed", {"type":2, "base":"Basement_Bedroom2_Bed", "click" : "basement_bedroom2_environment", "actions" : "lh", "zorder" : 0}, scene="basement_bedroom2")
    $ add_object_to_scene("Book", {"type":2, "base":"Basement_Bedroom2_Book", "click" : "basement_bedroom2_environment", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Cupboard", {"type":2, "base":"Basement_Bedroom2_Cupboard", "click" : "basement_bedroom2_environment", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Lamp", {"type":2, "base":"Basement_Bedroom2_Lamp", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "b":0.18, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture1", {"type":2, "base":"Basement_Bedroom2_Picture1", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture2", {"type":2, "base":"Basement_Bedroom2_Picture2", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture3", {"type":2, "base":"Basement_Bedroom2_Picture3", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture4", {"type":2, "base":"Basement_Bedroom2_Picture4", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture5", {"type":2, "base":"Basement_Bedroom2_Picture5", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture6", {"type":2, "base":"Basement_Bedroom2_Picture6", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture7", {"type":2, "base":"Basement_Bedroom2_Picture7", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture8", {"type":2, "base":"Basement_Bedroom2_Picture8", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Picture9", {"type":2, "base":"Basement_Bedroom2_Picture9", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")
    $ add_object_to_scene("Table", {"type":2, "base":"Basement_Bedroom2_Table", "click" : "basement_bedroom2_environment", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="basement_bedroom2")

    $ add_object_to_scene("FoodPaper", {"type":2, "base":"Basement_Bedroom2_FoodPaper", "img_overlay":"Basement_Bedroom2_FoodPaper_Overlay", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 1, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("donut", {"type":2, "base":"Basement_Bedroom2_Cake1", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 6, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("cookies cherry filled", {"type":2, "base":"Basement_Bedroom2_Cake2", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 2, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("chocolate cake", {"type":2, "base":"Basement_Bedroom2_Cake3", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 3, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("cannoli", {"type":2, "base":"Basement_Bedroom2_Cake4", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 5, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("napoleon", {"type":2, "base":"Basement_Bedroom2_Cake5", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 7, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("brownie", {"type":2, "base":"Basement_Bedroom2_Cake6", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 6, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("cupcake", {"type":2, "base":"Basement_Bedroom2_Cake7", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 8, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("cookie with nuts", {"type":2, "base":"Basement_Bedroom2_Cake8", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 3, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")
    $ add_object_to_scene("waffles", {"type":2, "base":"Basement_Bedroom2_Cake9", "click" : "basement_bedroom2_teleport_to_table", "actions" : "l", "zorder" : 4, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom2")

    $ add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : t_("ШКАФ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover":True}, scene="basement_bedroom2")

    return

label basement_bedroom2_init2:
    $ add_object_to_scene("ButtPlug", {"type":2, "base":"Basement_Bedroom2_ButtPlug[basement_bedroom2_buttplug_suffix]", "click" : "basement_bedroom2_environment", "actions" : "lh", "zorder" : 1, "group":"items", "label":"toy"}, scene="basement_bedroom2")

    return

label basement_bedroom2_teleport:
    if obj_name == "Teleport_Bedroom1":
        if cloth == "Nude":
            call change_scene("basement_bedroom1", "Fade", "snd_walk_barefoot") from _rcall_change_scene_181
            return
        call change_scene("basement_bedroom1") from _call_change_scene_65
        return
    return
label basement_bedroom2_teleport_to_table:
    call change_scene("basement_bedroom_table") from _call_change_scene_189
    return
label basement_bedroom2_environment:
    if obj_name == "Monica":
        mt "Здесь я теперь сплю..."
        "(хмык)"
        "Но это временно!!!"
        "Это какое-то недоразумение, которое скоро разрешится!"
    if obj_name == "BasementBed":
        if act == "l":
#            $ print bettyPantiesCurrentList
#            $ print bettyPantiesCurrent
#            $ print char_info["Betty"]
#            return
#            $ add_corruption(100, "place1")
#            $ add_char_progress("Monica", 25, "progress1", duplicate=True)
#            $ cleaningLog = [True, True, False, True, True]
#            $ print "log"
#            $ print get_cleaning_status(3)
#            return
            mt "Моя кровать..."
            "Но это временно!!!"
            "Это какое-то недоразумение, которое скоро разрешится!"
        if act == "h":
            if cloth != "Nude" and cloth != "GovernessPants":
                mt "Мне надо раздеться сначала"
                call refresh_scene_fade() from _call_refresh_scene_fade_22
                return
            menu:
                "Лечь спать.":
                    pass
                "Не ложиться.":
                    return
            call episode1End() from _call_episode1End
            return
    if obj_name == "Book":
        if act == "l":
            mt "Какая-то книга Юлии..."
        if act == "w":
            call change_scene("basement_bedroom_table") from _call_change_scene_66
            return
    if obj_name == "Cupboard":
        if act == "l":
            mt "Старый шкаф..."
#            $ questsCompleteByCategory(t_("МАРКУС"))
#            $ questsCompleteByCategory(t_("ОФИС"))
#            $ questsCompleteByCategory(t_("РАБОТА НА УЛИЦЕ"))
#            $ questsCompleteByCategory(t_("ДОМ"))
#            $ questsCompleteByCategory(t_("ПРОЧЕЕ"))
        if act == "w":
            $ basementBedroom2CupboardReturnScene = "basement_bedroom2"
            call change_scene("basement_bedroom2_cupboard") from _call_change_scene_67
            return

    if obj_name == "Lamp":
        mt "Эта тусклая лампа - это почти весь свет, который есть в этой каморке..."
    if obj_name == "Picture1" or obj_name == "Picture2" or obj_name == "Picture3" or obj_name == "Picture4" or obj_name == "Picture5" or obj_name == "Picture6" or obj_name == "Picture7" or obj_name == "Picture8" or obj_name == "Picture9":
        mt "Живопись..."
        "Я не знала что Юлия увлекается этим."
        "Она пыталась быть похожей на меня?"
        "..."
    if obj_name == "Table":
        if act == "l":
            mt "Этот старый яркий пестрый стол пытается скрасить уныние этой каморки..."
            "Тщетно..."
        if act == "w":
            call change_scene("basement_bedroom_table") from _call_change_scene_68
            return
    if obj_name == "ButtPlug":
        if act=="l":
            mt "Эта жуткая пробка..."
            mt "Я даже боюсь вспоминать, при каких обстоятельствах она оказалась у меня..."
            return
        mt "Я не буду прикасаться к ней! Только не снова!"
        $ define_inventory_object("revenge_keys", {"description" : t_("Ключи"), "label_suffix" : "_use_revenge_keys", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/revenge_keys" + res.suffix + ".png"})
        if check_inventory("revenge_keys",1) != True and ep210_revenge_quest2_box_blocked_fred == False:
            mt "..."
            mt "Хотя..."
            mt "Что это там?"
            mt "Я что-то вижу под кроватью рядом с пробкой..."
            $ add_inventory("revenge_keys", 1, True)
            $ set_active("WashMachine", False, scene="basement_laundry")
            $ remove_hook(label="revenge_quest_boxes")
            $ remove_objective("find_key")
            $ remove_hook("enter_scene", "ep29_dialogues5_gun_monica_6", scene="basement_pool")
            $ remove_hook(label="ep29_revenge_quest1_wardrobe")
            $ remove_hook(label="ep29_revenge_quest1_comment")
            $ remove_hook(label="ep29_revenge_quest1_nap")
            $ remove_hook(label="ep29_revenge_quest1_exit_map")
            $ remove_hook(label="ep29_revenge_quest1_exit_outside")
            $ remove_hook(quest="revenge_quest")
            call locations_init_basement_bedroom_table_opened()
            $ add_hook("Gun", "ep29_revenge_quest1_table_gun", scene="basement_bedroom_table_opened", label="ep29_revenge_quest1_table_gun", quest="revenge_quest")
            $ add_hook("Box", "ep29_revenge_quest1_table_box_opening", scene="basement_bedroom_table", label="revenge_quest_keys", quest="revenge_quest")
            sound fx_coins
            $ questHelp("revenge_1", True)
            $ questHelp("revenge_3")
            call refresh_scene_fade()
            return


    return

label hook_basement_bedroom2_change_view_to_suffix3:
    $ basement_bedroom2_MonicaSuffix = 3
    return
