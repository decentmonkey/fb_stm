default MonicaShowedBoobsToBettyKitchen = False
default monicaBettyKitchenEatedCount = 0
default bettyOffendedBardieKitchen = False # Бетти отозвалась о Барди на кухне плохо
default bettyNotFeedingMonicaKitchen = False # Бетти отказывается кормить Монику на кухне
default monicaEatedKitchenLastDay = 0
default bardieForcedBettyToFeedMonica = False # Барди снова заставил Бетти кормить Монику
default bardieCalledBettyForPunishment = False # Барди позвал Бетти за наказанием

# Бетти, Моника и еда на кухне
label ep26_quests_betty1:
    # Инициализация
    $ add_hook_multi("ep26_quests_betty2", scene="kitchen", label=["kitchen_betty_bardie_food1"], filter={"group":"environment"})
    $ add_hook_multi("ep26_quests_betty2", scene="kitchen2", label=["kitchen_betty_bardie_food1"], filter={"group":"environment"})
    $ add_hook("enter_scene", "ep26_quests_betty3", scene="kitchen", label="kitchen_betty_bardie_food1_enter")

    call ep28_monica_bardie_init() from _call_ep28_monica_bardie_init_1 # Инициализация v0.8 квеста с колледжем

    return

label ep26_quests_betty2:
    # Моника трогает на кухне предметы
    return

label ep26_quests_betty3:
    # Моника заходит на кухню
    if get_active_objects("Betty", scene="House", recursive=True) == False:
        return

    if day_time == "evening":
        call ep26_dialogues1_bardie12a() from _call_ep26_dialogues1_bardie12a
        return False
    call ep26_dialogues1_bardie6() from _call_ep26_dialogues1_bardie6
    if _return == 0: # Моника просто ушла
        call change_scene("floor1", "Fade_long") from _call_change_scene_334
        return False
    if _return == 1: # Моника поела с голой грудью
        $ MonicaShowedBoobsToBettyKitchen = True
        #Я могу питаться в доме. Если буду соблюдать условие...
        $ questLog(45, True)
        $ monicaBettyKitchenEatedCount += 1
        $ monicaEatedKitchenLastDay = day
        call monicaEat() from _call_monicaEat_13
        call change_scene("floor1", "Fade_long") from _call_change_scene_335
        $ remove_hook(label="kitchen_betty_bardie_food1_enter")
        $ add_hook("enter_scene", "ep26_quests_betty4", scene="kitchen", label="kitchen_betty_bardie_food2_enter")
        return False

    return False

label ep26_quests_betty4:
    # Регулярное питание на кухне с голой грудью
    if get_active_objects("Betty", scene="House", recursive=True) == False:
        return
    if day_time == "evening":
        call ep26_dialogues1_bardie12a() from _call_ep26_dialogues1_bardie12a_1
        return False
    if monicaEatedKitchenLastDay == day: # Моника уже кушала здесь сегодня
        call ep26_dialogues1_bardie12b() from _call_ep26_dialogues1_bardie12b
        return False
    call ep26_dialogues1_bardie7() from _call_ep26_dialogues1_bardie7
    if _return == 0: # Моника просто ушла
        call change_scene("floor1", "Fade_long") from _call_change_scene_336
        return False
    if _return == 1: # Бетти козлит и не кормит
        $ autorun_to_object("ep26_dialogues1_bardie8a", scene="floor1")
        $ bettyNotFeedingMonicaKitchen = True
        call change_scene("floor1", "Fade_long") from _call_change_scene_337
        return False
    if _return == 2: # Моника поела
        $ monicaEatedKitchenLastDay = day
        $ monicaBettyKitchenEatedCount += 1
        $ bardieForcedBettyToFeedMonica = False
        call monicaEat() from _call_monicaEat_14
        call change_scene("floor1", "Fade_long") from _call_change_scene_338
        return False

    return













#
