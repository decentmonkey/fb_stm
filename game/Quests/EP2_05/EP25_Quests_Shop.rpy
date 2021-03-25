default ep25_quests_shop1_shop_inited = False
default monicaHasCasualDress1 = False
default monicaBoughtCasualDress1 = False
default monicaStealCasualDress1 = False
default monicaTriedToStealDress = False
default monicaKickedVivianForDress = False
default monicaNeedToSellDress = False
default monicaAgreedToSellDress = False
default monicaLickedVivianNipple = False
default monicaOffendedCit3 = False # Моника заставила покупателя купить платье силой

default clothShopUsualDayVisitorsAmount = 4
default clothShopUsualEveningVisitorsAmount = 0
default clothShopSellingDressDayVisitorsAmount = 4

default clothShopSellingDressVisitorsStage = 0

default shopVisitorsList = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]

label ep25_quests_shop1:
    # Вход в магазин одежды (первый раз)
    $ remove_hook()
    call locations_init_clothing_shop() from _call_locations_init_clothing_shop

    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop2", scene="street_cloth_shop", label=["cloth_shop_enter1", "cloth_shop_quests"])
    $ autorun_to_object("ep25_dialogues1_shop1c", scene="cloth_shop_view1")

    $ add_hook("Cashier", "ep25_quests_shop3", scene="cloth_shop_cashier", label="cloth_shop_quests")

#    call ep25_quests_steve1()
    call ep25_quests_shop2() from _call_ep25_quests_shop2

    return False

label ep25_quests_shop2:
    # Вход в магазин одежды, обычный
    if cloth != "Whore":
        return

    $ set_active(False, group="cloth_shop_visitors", scene="Cloth_Shop", recursive=True)

    # Скрываем посетителей, кроме 4-х случайных
    $ shopVisitorsListOriginal = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]
    $ shopVisitorsList = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]
    $ currentVisitorsAmount = clothShopUsualDayVisitorsAmount
    if day_time == "evening":
        $ currentVisitorsAmount = clothShopUsualEveningVisitorsAmount
        $ activeVisitors = random.sample(set(shopVisitorsList), currentVisitorsAmount)
        python:
            for visitorName in activeVisitors:
                set_active(visitorName, True, scene="cloth_shop_view1", recursive=True)
                set_active(visitorName, True, scene="cloth_shop_view2", recursive=True)

    call change_scene("cloth_shop_view1") from _call_change_scene_252

    return False

label ep25_quests_shop2a:
    # Вход в магазин одежды, Моника продает платье
    if cloth != "Whore":
        return

    $ set_active(False, group="cloth_shop_visitors", scene="Cloth_Shop", recursive=True)

    # Скрываем посетителей, кроме 4-х случайных
    $ shopVisitorsListOriginal = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]
#    $ shopVisitorsList = ["Shop_Visitor1", "Shop_Visitor2", "Shop_Visitor3", "Shop_Visitor4", "Shop_Visitor5", "Shop_Visitor6", "Shop_Visitor7", "Shop_Visitor8", "Shop_Visitor9", "Shop_Visitor10"]
    $ currentVisitorsAmount = clothShopSellingDressDayVisitorsAmount
    if day_time == "evening":
        $ currentVisitorsAmount = clothShopUsualEveningVisitorsAmount
    if clothShopSellingDressVisitorsStage == 0: # Обычное заполнение магазина
        $ shopVisitorsList = list(set(shopVisitorsList))
        if len(shopVisitorsList) >= currentVisitorsAmount:
            $ activeVisitors = random.sample(set(shopVisitorsList), currentVisitorsAmount)
        else:
            # Если не хватает покупателей, чтобы забить магазин
            $ activeVisitors = []
            if shopVisitorStage3 == 3 or 1==1: # Если третий уже stage = 3, то добавляем его
                $ activeVisitors = shopVisitorsList
                $ activeVisitors.append("Shop_Visitor3")
                $ activeVisitors = list(set(activeVisitors)) #unique
            python:
                while len(activeVisitors) < currentVisitorsAmount: # добавляем покупателей до нужного кол-ва
                    activeVisitors.append(random.choice(shopVisitorsListOriginal))
                    activeVisitors = list(set(activeVisitors))

        python:
            for visitorName in activeVisitors:
                set_active(visitorName, True, scene="cloth_shop_view1", recursive=True)
                set_active(visitorName, True, scene="cloth_shop_view2", recursive=True)

    call change_scene("cloth_shop_view1") from _call_change_scene_253
    return False


label ep25_quests_shop3:
    # Разговор с кассиром (поиск платья и покупка)
    if act=="l":
        return
    $ remove_hook()

    call ep25_dialogues1_shop2() from _call_ep25_dialogues1_shop2
    if _return == False:
        $ clothShopUsualDayVisitorsAmount = 0 # В магазине никого нет
        $ questHelp("shop_4")
        $ add_hook("Cashier", "ep25_quests_shop6", scene="cloth_shop_cashier", label=["cloth_shop_quests", "steal_dress"]) # Теперь платье можно и украсть
        $ add_hook("open", "ep25_quests_shop5", scene="cloth_shop_view1", label=["cloth_shop_quests", "steal_dress"])
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4a", scene="street_cloth_shop", label=["cloth_shop_enter2", "cloth_shop_quests"]) # блокируем вход в магазин
        $ add_hook("change_time_day", "ep25_quests_shop4b", scene="global") # Разблокируем вход в магазин на следующий день

        call change_scene("street_cloth_shop") from _call_change_scene_254
        return False

    $ monicaHasCasualDress1 = True
    $ monicaBoughtCasualDress1 = True
    $ questHelp("steve_7")
    $ remove_objective("find_casual_dress")
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    call ep25_quests2() from _call_ep25_quests2
    $ autorun_to_object("ep25_dialogues1_shop2a", scene="street_cloth_shop") # Комментарий на улице о покупке платья
    call change_scene("street_cloth_shop", "Fade_long", False) from _call_change_scene_255

    $ remove_hook(label="cloth_shop_quests")
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
    return False

label ep25_quests_shop4:
    # Моника не хочет заходить в магазин после покупки платья или после того как отобрала его
    if check_hook(label="bardie_eric_quest_college_shop", scene="street_cloth_shop") == True:
        return
    call ep25_dialogues1_shop3() from _call_ep25_dialogues1_shop3
    return False

label ep25_quests_shop4a:
    # Моника не хочет заходить в магазин сегодня
    call ep25_dialogues1_shop4a() from _call_ep25_dialogues1_shop4a
    return False
label ep25_quests_shop4b:
    # Вход в магазин разблокируется на следующий день
    $ remove_hook()
    $ remove_hook(label="cloth_shop_enter2")
    return

label ep25_quests_shop4c:
    # Моника не хочет заходить в магазин после отработки платья и после лесби сцены
    if check_hook(label="bardie_eric_quest_college_shop", scene="street_cloth_shop") == True:
        return
    call ep25_dialogues1_shop11() from _call_ep25_dialogues1_shop11
    return False


label ep25_quests_shop5:
    # В магазине мало народа. Может быть украсть платье?
    if lastSceneName != "street_cloth_shop":
        return
    call ep25_dialogues1_shop4() from _call_ep25_dialogues1_shop4
    call ep25_dialogues1_shop5() from _call_ep25_dialogues1_shop5
    if _return == True:
        call ep25_quests_shop7() from _call_ep25_quests_shop7
        return False
    call change_scene("cloth_shop_cashier") from _call_change_scene_256
    return
label ep25_quests_shop6:
    # Моника может купить или украсть платье
    if act=="l":
        return

    # Говорим о том чтобы купить платье
    call ep25_dialogues1_shop2() from _call_ep25_dialogues1_shop2_1
    if _return == False:
        $ questHelp("shop_4")
        call change_scene("street_cloth_shop") from _call_change_scene_257
        return False

    $ monicaHasCasualDress1 = True
    $ monicaBoughtCasualDress1 = True
    $ questHelp("steve_7")
    $ remove_objective("find_casual_dress")
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    call ep25_quests2() from _call_ep25_quests2_1
    $ autorun_to_object("ep25_dialogues1_shop2a", scene="street_cloth_shop") # Комментарий на улице о покупке платья
    call change_scene("street_cloth_shop", "Fade_long", False) from _call_change_scene_258

    $ remove_hook(label="cloth_shop_quests")
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
    return

label ep25_quests_shop7:
    # Воруем платье
    $ questHelp("shop_4", True)
    call ep25_dialogues1_shop6() from _call_ep25_dialogues1_shop6

    if _return == False:
        # Бьем продавца и убегаем
        $ questHelp("shop_2", False)
        $ questHelp("shop_3", False)
        $ questHelp("shop_4", False)
        $ monicaHasCasualDress1 = True
        $ monicaBoughtCasualDress1 = True
        $ questHelp("steve_7")
        $ remove_objective("find_casual_dress")
        $ cloth = "CasualDress1"
        $ cloth_type = "CasualDress"
        call ep25_quests2() from _call_ep25_quests2_2
        $ autorun_to_object("ep25_dialogues1_shop2a", scene="street_cloth_shop") # Комментарий на улице о покупке платья
        call change_scene("street_cloth_shop") from _call_change_scene_259

        $ remove_hook(label="cloth_shop_quests")
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
        return False
    call ep25_dialogues1_shop7() from _call_ep25_dialogues1_shop7
    $ autorun_to_object("ep25_dialogues1_shop8", scene="street_cloth_shop") # Размышление о том что неплохо бы продать платье
    $ changeDayTime("evening")
    $ remove_hook(label="steal_dress")
    $ add_hook("Cashier", "ep25_quests_shop8", scene="cloth_shop_cashier", label=["cloth_shop_quests", "sell_dress_dialogue"]) # Теперь платье можно и украсть
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop2a", scene="street_cloth_shop", label=["cloth_shop_quests", "sell_dress_enter"]) # Заполнение магазина

    $ add_hook("Shop_Visitor1", "ep25_quests_shop_visitors1", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor2", "ep25_quests_shop_visitors2", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor3", "ep25_quests_shop_visitors3", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor4", "ep25_quests_shop_visitors4", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor5", "ep25_quests_shop_visitors5", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor6", "ep25_quests_shop_visitors6", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor7", "ep25_quests_shop_visitors7", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor8", "ep25_quests_shop_visitors8", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor9", "ep25_quests_shop_visitors9", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("Shop_Visitor10", "ep25_quests_shop_visitors10", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitors_dialogue"]) # Диалоги с посетителями
    $ add_hook("change_time_day", "ep25_quests_shop9", scene="global", label=["cloth_shop_quests"]) # Обнуление блокировки входа в магазин

    $ questHelp("shop_2", False)
    $ questHelp("shop_3", False)
    $ questHelp("shop_4", True)
    $ questHelp("shop_6")
    $ remove_objective("find_casual_dress")
    $ add_objective("find_casual_dress", t_("Продать платье в магазине одежды"), c_blue, 15)

    call change_scene("street_cloth_shop", "Fade_long", False) from _call_change_scene_260
    $ char_info["Cashier"]["enabled"] = True
    $ char_info["Cashier"]["caption"] = t_("Вивиан ждет что Моника продаст платье.")
    $ add_char_progress("Cashier", 100, "cloth_shop_cashier_steal_lesbian1" + str(day), duplicate=True)

    return

label ep25_quests_shop8:
    # Моника приходит к продавцу продавать платье
    if act=="l":
        return
    call ep25_dialogues1_shop9() from _call_ep25_dialogues1_shop9
    if _return == 0:
        call change_scene("street_cloth_shop", "Fade_long") from _call_change_scene_261
    if _return == 1:
        # Покупаем платье
        call question_helper_disable() from _call_question_helper_disable
        $ monicaHasCasualDress1 = True
        $ monicaBoughtCasualDress1 = True
        $ questHelp("steve_7")
        $ remove_objective("find_casual_dress")
        $ cloth = "CasualDress1"
        $ cloth_type = "CasualDress"
        call ep25_quests2() from _call_ep25_quests2_3
        $ autorun_to_object("ep25_dialogues1_shop2a", scene="street_cloth_shop") # Комментарий на улице о покупке платья
        call change_scene("street_cloth_shop") from _call_change_scene_262

        $ remove_hook(label="cloth_shop_quests")
        $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4c", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
    if _return == 2:
        # Начинаем работу
        $ monicaSellingDressInProgress = True
        $ monicaSellingDressDays += 1
        $ add_hook("Teleport_Street_Cloth_Shop", "ep25_quests_shop10", scene="cloth_shop_view1", label="sell_dress_process") # Блокируем выход на улицу
        $ add_hook("Cashier", "ep25_quests_shop11", scene="cloth_shop_cashier", label="sell_dress_process") # Разговор с продавцом о конце продажи платья на сегодня
        $ add_hook("Monica", "ep25_dialogues1_shop22", scene="cloth_shop_view1", label="sell_dress_process") # Клик на Монику
        $ add_hook("Monica", "ep25_dialogues1_shop22", scene="cloth_shop_view2", label="sell_dress_process")
        $ cloth = "EveningDress"
        $ cloth_type = "SellingDress"
        sound snd_fabric1
        img black_screen
        with diss
        pause 1.0
        call question_helper_enable("question_clothing_shop_sell_dress") from _call_question_helper_enable
        call change_scene("cloth_shop_view1", "Fade_long", False) from _call_change_scene_263

    return False


label ep25_quests_shop9:
    # С утра убираются хуки закрытия входа в магазин (если Моника психанула или уже торговала сегодня)
    $ remove_hook(label="shop_today_refuse")
    return

label ep25_quests_shop10:
    # Блокировка выхода из магазина пока продается платье
    if cloth == "Nude":
        call ep25_dialogues1_shop20a() from _call_ep25_dialogues1_shop20a
    else:
        call ep25_dialogues1_shop20() from _call_ep25_dialogues1_shop20
    return False

label ep25_quests_shop11:
    if act=="l":
        return
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop10b() from _call_ep25_dialogues1_shop10b
        return False

    call ep25_dialogues1_shop10a() from _call_ep25_dialogues1_shop10a
    if _return == False:
        call change_scene("cloth_shop_view1", "Fade_long") from _call_change_scene_264
        return False
    call ep25_quests_shop11a() from _call_ep25_quests_shop11a
    return False

label ep25_quests_shop11a:
    # Заканчивание работы
    call ep25_dialogues1_shop10() from _call_ep25_dialogues1_shop10 # Заканчиваем работу на сегодня
    call question_helper_disable() from _call_question_helper_disable_1
    $ monicaSellingDressInProgress = False
    $ changeDayTime("evening")
    $ remove_hook(label="sell_dress_process")
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop12", scene="street_cloth_shop", label="shop_today_refuse")
    $ remove_hook(label="cloth_shop_sell_dialogue_morning")
    $ add_hook("basement_monica_after_sleep_dialogue", "ep25_dialogues1_shop16", scene="global", label=["cloth_shop_quests", "cloth_shop_sell_dialogue_morning"]) # На утро думаем о продаже платья

    $ cloth = "Whore"
    $ cloth_type = "Whore"
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    call change_scene("street_cloth_shop", "Fade_long") from _call_change_scene_265
    return


label ep25_quests_shop12:
    # Сегодня Моника не хочет заходить в магазин, потому что уже работала там
    call ep25_dialogues1_shop14() from _call_ep25_dialogues1_shop14
    return False

label ep25_quests_shop13:
    # Проверка на то, что посетителей больше нет (конец работы)
    if get_active_objects(scene="Cloth_Shop", recursive=True, group="cloth_shop_visitors") == False:
        $ autorun_to_object("ep25_quests_shop14", scene="cloth_shop_view1")
        call ep25_quests_shop11a() from _call_ep25_quests_shop11a_1 # Заканчиваем работу на сегодня
    return False

label ep25_quests_shop14: # пустое лейбл для очистки autorun
    return


label ep25_quests_shop15:
    # Моника продала платье, требует награду
    call question_helper_disable() from _call_question_helper_disable_2
    $ remove_hook(label="cloth_shop_quests")
    call ep25_dialogues1_shop12() from _call_ep25_dialogues1_shop12
    $ autorun_to_object("ep25_dialogues1_shop12a", scene="street_cloth_shop")

    $ questHelp("shop_6", True)
#    $ questHelp("steve_8")
    $ questHelp("steve_7")
#    $ questHelp("office_24")
    $ questHelpDesc("shop_desc1", "shop_desc2")
    $ monicaHasCasualDress1 = True
    $ questHelp("steve_7")
    $ remove_objective("find_casual_dress")
    call ep25_quests2() from _call_ep25_quests2_4
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop16", scene="street_cloth_shop", label=["cloth_shop_enter3"])
    $ add_char_progress("Cashier", 100, "cloth_shop_cashier_dress_sell", duplicate=True)

    call change_scene("street_cloth_shop", "Fade_long") from _call_change_scene_266
    return False

label ep25_quests_shop16:
    # Моника пытается зайти в магазин после того как отработала платье
    if check_hook(label="bardie_eric_quest_college_shop", scene="street_cloth_shop") == True:
        return
    call ep25_dialogues1_shop11() from _call_ep25_dialogues1_shop11_1
    return False











#
