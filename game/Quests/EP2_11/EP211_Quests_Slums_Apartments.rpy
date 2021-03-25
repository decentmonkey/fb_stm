default slumsApartmentsCheckInitialized = False

default slumsApartmentsMiniMapActive = False
default slumsDirtyStreetMiniMapActive = True

default slumsEnterClothStored = False
default slumsEnterClothTypeStored = False

default monicaHasWhoreOutfit1 = True

default monicaSlumsApartmentsCocktailDrinked = 0

default slumsApartmentsShawarmaTraderDialogue1Active = False

label ep211_quests_slums_apartments0_init:
    $ add_hook("enter_scene", "ep211_quests_slums_apartments0_check", scene="hostel_street", label="slums_apartments_check")
    $ slumsApartmentsCheckInitialized = True
    return

label ep211_quests_slums_apartments0_check:
    if pubMonicaWorkingWaitress != True:
        return
    $ remove_hook()
    $ add_objective("ask_kebab", t_("Спросить у продавца шавермы про аренду квартиры."), c_blue, 105)
    $ add_hook("enter_scene", "ep211_dialogues6_slum_apartment_2", scene="whores_place_shawarma", label="slums_apartments_begin", once=True)
    $ slumsApartmentsShawarmaTraderDialogue1Active = True
    call ep211_dialogues6_slum_apartment_1() from _rcall_ep211_dialogues6_slum_apartment_1
    $ print "hook finished!"
    return

label ep211_quests_slums_apartments1_init:
    call locations_init_monicahome() from _rcall_locations_init_monicahome
    call hostel_street_init2() from _rcall_hostel_street_init2
    $ add_hook("HomeEnter", "ep211_quests_slums_apartments2_check_enter", scene="street_monicahome", quest="monica_apartments", label="monica_apartments_enter")
    $ add_hook("MonicaWindow", "ep211_quests_slums_apartments2_check_enter", scene="street_monicahome", quest="monica_apartments", label=["monica_apartments_enter", "monica_apartments_enter_window"])
    $ add_hook("Teleport_Street", "ep211_quests_slums_apartments3_check_exit_door", scene="monicahome_livingroomwardrobe", quest="monica_apartments", label="monica_apartments_exit")
    $ add_hook("before_open", "ep211_quests_slums_apartments4_monica_suffix", scene="street_monicahome", quest="monica_apartments", label="monica_apartments_street_enter_check")

    $ add_hook("Street_MonicaHome_TeleportSlums", "ep22_dialogue1_3_slums", scene="street_monicahome", quest="monica_apartments", label="monica_governess_outfit_restrictions")
    $ add_hook("Street_MonicaHome_TeleportSlums", "dialogue_classmate_3_1_1a", scene="street_monicahome", quest="monica_apartments", label="school_outfit_slums_forbidden")
    $ add_hook("Street_MonicaHome_TeleportSlums", "ep25_quests4", scene="street_monicahome", quest="monica_apartments", label="casual_dress_slums_forbidden", priority=900)
    $ add_hook("slums_apartments_check_exit_wardrobe", "ep211_quests_slums_apartments3_check_exit_wardrobe", scene="monicahome_livingroomwardrobe", quest="monica_apartments", label="slums_apartments_check_exit_wardrobe")
    call ep211_quests_slums_apartments1_initb() from _rcall_ep211_quests_slums_apartments1_initb
    return

label ep211_quests_slums_apartments1_inita:
    $ slumsApartmentsMiniMapActive = True
    $ slumsDirtyStreetMiniMapActive = False
    $ map_objects["Teleport_Slums_Apartments"] = {"text" : t_("ДОМ В ТРУЩОБАХ"), "xpos" : 408, "ypos" : 728, "base" : "map_marker", "state" : "visible"}
    $ set_active("Teleport_Slums_Apartments", True, scene="hostel_street")
    return

label ep211_quests_slums_apartments1_initb:
    $ add_hook("Cocktail", "ep211_quests_slums_apartments5_cocktail", scene="monicahome_livingroom", quest="monica_apartments", label="slums_apartments_cocktail")
    $ add_hook("Chair1", "ep211_quests_slums_apartments6_chair", scene="monicahome_livingroom", quest="monica_apartments", label="slums_apartments_chair")
    $ add_hook("Bed1", "slums_basement_bed", scene="monicahome_livingroom", quest="monica_apartments", label="slums_apartments_bed")
    $ add_hook("Kitchen_Items1", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Kitchen_Items2", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Kitchen_Items3", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Kitchen_Items4", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Kitchen_Items5", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Kitchen_Items6", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Kitchen_Table1", "slums_basement_kitchen_eat", scene="monicahome_kitchen", quest="monica_apartments", label="slums_apartments_kitchen")
    $ add_hook("Toilet", "ep211_quests_slums_apartments7_piss", scene="monicahome_bathroom", quest="monica_apartments", label="slums_apartments_piss")
    $ add_hook("Shower", "ep211_quests_slums_apartments8_shower", scene="monicahome_bathroom", quest="monica_apartments", label="slums_apartments_shower")

    $ add_hook("change_time_day_slums_apartments", "citizens_init_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Bardie_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Betty_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Ralph_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Fred_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Biff_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Melanie_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Dick_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "ep22_quests_falling_path2", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Pub_Life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "office_life_day", scene="global")
    $ add_hook("change_time_day_slums_apartments", "Steve_Life_day", scene="global")

    $ add_hook("change_time_evening_slums_apartments", "citizens_init_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Bardie_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Betty_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Ralph_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Fred_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Biff_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Melanie_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Dick_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Pub_Life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "office_life_evening", scene="global")
    $ add_hook("change_time_evening_slums_apartments", "Steve_Life_evening", scene="global")

    $ add_hook("slums_apartments_monica_after_nap", "slums_basement_monica_after_nap", scene="global")
    $ add_hook("slums_basement_monica_after_nap_dialogue", "slums_basement_monica_after_nap_dialogue1", scene="global")

    $ add_hook("slums_apartments_monica_after_sleep", "slums_basement_monica_after_sleep", scene="global")
    $ add_hook("slums_basement_monica_after_sleep_dialogue", "slums_basement_monica_after_sleep_dialogue1", scene="global")
    return

label ep211_quests_slums_apartments2_check_enter:
    if act=="l":
        return

label ep211_quests_slums_apartments2_check_enter_forced:
    if cloth != "HomeCloth4":
        $ slumsEnterClothStored = cloth
        $ slumsEnterClothTypeStored = cloth_type
        sound snd_fabric1
        $ cloth = "HomeCloth4"
        $ cloth_type = "HomeCloth"
    sound2 snd_keys_door_open
    return

label ep211_quests_slums_apartments2_check_enter_minimap:
    if cloth_type != "HomeCloth":
        $ slumsEnterClothStored = cloth
        $ slumsEnterClothTypeStored = cloth_type
        sound snd_fabric1
        $ cloth = "HomeCloth4"
        $ cloth_type = "HomeCloth"
    if scene_name == "street_monicahome":
        sound2 snd_keys_door_open
    return

label ep211_quests_slums_apartments2_check_enter_minimap_bathroom:
    call ep211_quests_slums_apartments2_check_enter_minimap() from _rcall_ep211_quests_slums_apartments2_check_enter_minimap
    if _return == False:
        return False
    if scene_name == "street_monicahome":
        $ monicaHomeBathroomMonicaSuffix = 1
        call change_scene("monicahome_bathroom", "Fade") from _rcall_change_scene_29
    else:
        call change_scene("monicahome_bathroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_30
    return
label ep211_quests_slums_apartments2_check_enter_minimap_kitchen:
    call ep211_quests_slums_apartments2_check_enter_minimap() from _rcall_ep211_quests_slums_apartments2_check_enter_minimap_1
    if _return == False:
        return False
    if scene_name == "street_monicahome":
        $ monicaHomeKitchenMonicaSuffix = 1
        call change_scene("monicahome_kitchen", "Fade") from _rcall_change_scene_31
    else:
        call change_scene("monicahome_kitchen", "Fade", "snd_walk_barefoot") from _rcall_change_scene_32
    return
label ep211_quests_slums_apartments2_check_enter_minimap_livingroom:
    call ep211_quests_slums_apartments2_check_enter_minimap() from _rcall_ep211_quests_slums_apartments2_check_enter_minimap_2
    if _return == False:
        return False
    if scene_name == "street_monicahome":
        $ monicaHomeLivingRoomMonicaSuffix = 1
        call change_scene("monicahome_livingroom", "Fade") from _rcall_change_scene_33
    else:
        call change_scene("monicahome_livingroom", "Fade", "snd_walk_barefoot") from _rcall_change_scene_34
    return
label ep211_quests_slums_apartments2_check_enter_minimap_livingroomwardrobe:
    call ep211_quests_slums_apartments2_check_enter_minimap() from _rcall_ep211_quests_slums_apartments2_check_enter_minimap_3
    if _return == False:
        return False
    if scene_name == "street_monicahome":
        $ monicaHomeLivingRoomWardrobeMonicaSuffix = 1
        call change_scene("monicahome_livingroomwardrobe", "Fade") from _rcall_change_scene_35
    else:
        call change_scene("monicahome_livingroomwardrobe", "Fade", "snd_walk_barefoot") from _rcall_change_scene_36
    return


label ep211_quests_slums_apartments3_check_exit_minimap:
    call process_hooks("slums_apartments_check_exit_wardrobe", "monicahome_livingroomwardrobe") from _rcall_process_hooks
    if _return == False:
        return False
    call change_scene("street_monicahome", "Fade", "snd_door_close1") from _rcall_change_scene_37
    $ streetMonicaHomeMonicaSuffix = 2
    return


label ep211_quests_slums_apartments3_check_exit_door:
    if act=="l":
        return
    call process_hooks("slums_apartments_check_exit_wardrobe", "monicahome_livingroomwardrobe") from _rcall_process_hooks_1
    if _return == False:
        return False
    sound2 snd_door_close1
    return

label ep211_quests_slums_apartments3_check_exit_wardrobe:
    if cloth_type == "HomeCloth":
        sound2 snd_fabric1
        $ cloth = slumsEnterClothStored
        $ cloth_type = slumsEnterClothTypeStored
    $ streetMonicaHomeMonicaSuffix = 2
    return True

label ep211_quests_slums_apartments4_monica_suffix:
    if lastSceneName != "monicahome_livingroom" and lastSceneName != "monicahome_livingroomwardrobe" and lastSceneName != "monicahome_kitchen" and lastSceneName != "monicahome_bathroom":
        $ streetMonicaHomeMonicaSuffix = 1
    return

label ep211_quests_slums_apartments5_cocktail:
    if act=="l":
        return
    call ep211_dialogues6_slum_apartment_8n() from _rcall_ep211_dialogues6_slum_apartment_8n
    $ monicaSlumsApartmentsCocktailDrinked += 1
    $ set_active("Cocktail", False, scene="monicahome_livingroom")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_23
    return False

label ep211_quests_slums_apartments6_chair:
    if act=="l":
        return
    $ monicaHomeLivingRoomMonicaSuffix = 5
    $ autorun_to_object("ep211_dialogues6_slum_apartment_35", scene="monicahome_livingroom")
    call refresh_scene("Dissolve_05") from _rcall_refresh_scene
    return False

label ep211_quests_slums_apartments7_piss:
    if act=="l":
        return
    if monicaLastPissedDay == day and monicaLastPissedDayTime == day_time:
        mt "Я уже писала недавно. Я пока не хочу."
        return
    $ store_music()
    music stop
    if cloth == "HomeCloth4":
        $ toilet_images = ["23617", "23618", "23619", "23620", "23621"]
        $ images = random.sample(set(toilet_images), 3)
    if cloth == "BathCloth1":
        $ toilet_images = ["23612", "23613", "23614", "23615", "23616"]
        $ images = random.sample(set(toilet_images), 3)

    img images[0]
    with fade
    w
    sound snd_piss
    img images[1]
    with diss
    w
    img images[2]
    with diss
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Фи! Никогда бы не подумала, что моя попа будет прикасаться к такому ужасному унитазу!"
    if rnd == 2:
        mt "Такая красивая женщина, как я, не заслуживает всего, что со мной произошло."
    if rnd == 3:
        mt "Я не собираюсь оставаться в этой ужасной дыре надолго! Скоро я верну себе все!"

    $ monicaLastPissedDay = day
    $ monicaLastPissedDayTime = day_time
    $ restore_music()
    call refresh_scene_fade() from _rcall_refresh_scene_fade_24

    return False

label ep211_quests_slums_apartments8_shower:
    if act=="l":
        return
    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return
    $ store_music()
    music stop
    img black_screen
    with diss
    pause 1.5
    music snd_shower2

    $ shower_images = ["23623", "23624", "23625", "23626", "23627", "23628", "23629", "23631", "23632", "23633"]
    $ images = random.sample(set(shower_images), 5)

    img images[0]
    with fade
    w
    img images[1]
    with diss
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Я вынуждена мыть свое прекрасное тело в этом жалком подобии душа!"
    if rnd == 2:
        mt "Какой идиот придумал сделать душ из куска ржавой трубы?!"
    if rnd == 3:
        mt "По крайней мере, здесь есть горячая вода..."
    img images[2]
    with diss
    w
    img images[3]
    with diss
    w
    img images[4]
    with diss
    w
    $ cloth = "BathCloth1"
    $ cloth_type = "HomeCloth"
    $ monicaHomeBathroomMonicaSuffix = 2
    $ autorun_to_object("ep211_dialogues6_slum_apartment_34_after_shower", scene="monicahome_bathroom")
    $ monicaLastShowerDay = day
    $ monicaLastShowerDayTime = day_time
    $ restore_music()
    call refresh_scene_fade() from _rcall_refresh_scene_fade_25

    return False
