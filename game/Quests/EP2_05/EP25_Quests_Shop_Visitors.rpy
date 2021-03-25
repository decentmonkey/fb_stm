default monicaSellingDressInProgress = False
default monicaSellingDressDays = 0
default monicaSellingDressRefuseLastDay = 0
default shopVisitorStage1 = 1
default shopVisitorStage2 = 1
default shopVisitorStage3 = 1
default shopVisitorStage4 = 1
default shopVisitorStage5 = 1
default shopVisitorStage6 = 1
default shopVisitorStage7 = 1
default shopVisitorStage8 = 1
default shopVisitorStage9 = 1
default shopVisitorStage10 = 1

default ep25_quests_shop_visitors4bFlag = False

label ep25_quests_shop_visitors1:
    if shopVisitorStage1 > 3:
        return
    if act=="l":
        mt "Какой-то фрик... Может он купит это платье?"
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage1 == 1:
        call cit1_dialog_1() from _call_cit1_dialog_1
        $ shopVisitorStage1 = 2
        $ set_active("Shop_Visitor1", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_107
        call ep25_quests_shop13() from _call_ep25_quests_shop13 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage1 == 2:
        $ store_music()
        call cit1_dialog_2() from _call_cit1_dialog_2
        if _return != False:
            $ shopVisitorStage1 = 3
        $ restore_music()
        $ set_active("Shop_Visitor1", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_108
        call ep25_quests_shop13() from _call_ep25_quests_shop13_1 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage1 == 3:
        $ store_music()
        call cit1_dialog_3() from _call_cit1_dialog_3
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor1")
            $ shopVisitorStage1 = 4
        $ restore_music()
        $ set_active("Shop_Visitor1", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_109
        call ep25_quests_shop13() from _call_ep25_quests_shop13_2 # Проверка на конец работы (нет посетителей)
        return False

    return

label ep25_quests_shop_visitors2:
    if shopVisitorStage2 > 3:
        return
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_1
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_1 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage2 == 1:
        call cit2_dialog_1() from _call_cit2_dialog_1
        if _return != False:
            $ shopVisitorStage2 = 2
        $ set_active("Shop_Visitor2", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        sound highheels_short_walk
        call refresh_scene_fade() from _call_refresh_scene_fade_110
        call ep25_quests_shop13() from _call_ep25_quests_shop13_3 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage2 == 2:
        $ store_music()
        call cit2_dialog_2() from _call_cit2_dialog_2
        if _return != False:
            $ shopVisitorStage2 = 3
        $ restore_music()
        $ set_active("Shop_Visitor2", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        sound highheels_short_walk
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_2
        call ep25_quests_shop13() from _call_ep25_quests_shop13_4 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage2 == 3:
        $ store_music()
        call cit2_dialog_3() from _call_cit2_dialog_3
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor2")
            $ shopVisitorStage2 = 4
        $ restore_music()
        $ set_active("Shop_Visitor2", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        sound highheels_short_walk
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_3
        call ep25_quests_shop13() from _call_ep25_quests_shop13_5 # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors3:
    if shopVisitorStage3 > 3:
        return
    if act=="l":
        mt "Очередной ненормальный..."
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_2
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_2 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage3 == 1:
        $ store_music()
        call cit3_dialog_1() from _call_cit3_dialog_1
        if _return != False:
            $ shopVisitorStage3 = 2
        $ restore_music()
        $ set_active("Shop_Visitor3", False)
        $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_view2")
        sound highheels_short_walk
        call refresh_scene_fade() from _call_refresh_scene_fade_111
#        call ep25_quests_shop13() from _call_ep25_quests_shop13_6 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage3 == 2:
        $ store_music()
        call cit3_dialog_2() from _call_cit3_dialog_2
        if _return != False:
            $ shopVisitorStage3 = 3
            $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_view2")
            $ shopVisitorsList.remove("Shop_Visitor3")
        else:
            $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view2")
        $ restore_music()
        $ set_active("Shop_Visitor3", False)
        sound highheels_short_walk
        call refresh_scene_fade() from _call_refresh_scene_fade_112
        if shopVisitorStage3 == 2:
            call ep25_quests_shop13() from _call_ep25_quests_shop13_7 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage3 == 3:
        $ store_music()
        call cit3_dialog_3() from _call_cit3_dialog_3
        $ restore_music()
        if _return != False:
            $ shopVisitorStage3 = 4
#            $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_view2")
            $ shopVisitorsList.remove("Shop_Visitor3")
            call ep25_quests_shop15() from _call_ep25_quests_shop15 # Квест магазина закончен
            return False
        else:
            $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view2")
            $ set_active("Shop_Visitor3", False)
            sound highheels_short_walk
            call refresh_scene_fade() from _call_refresh_scene_fade_113
#        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False
    return
label ep25_quests_shop_visitors4:
    if shopVisitorStage4 > 3:
        return
    if act=="l":
        mt "Какая-то рыжеволосая стерва. Отвратительный цвет волос, Фи!"
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_3
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_3 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage4 == 1:
        call cit4_dialog_1() from _call_cit4_dialog_1
        $ shopVisitorStage4 = 2
        $ set_active("Shop_Visitor4", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_114
        call ep25_quests_shop13() from _call_ep25_quests_shop13_8 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage4 == 2:
        $ store_music()
        call cit4_dialog_2() from _call_cit4_dialog_2
        if _return != False:
            $ shopVisitorStage4 = 3
        $ restore_music()
        $ set_active("Shop_Visitor4", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_115
        call ep25_quests_shop13() from _call_ep25_quests_shop13_9 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage4 == 3:
        $ store_music()
        call cit4_dialog_3() from _call_cit4_dialog_3
#        if _return != False:
        $ move_object("Shop_Visitor4", "cloth_shop_dressing_room2")
        $ add_hook("Shop_Visitor4", "ep25_quests_shop_visitors4a", scene="cloth_shop_dressing_room2")
        call change_scene("cloth_shop_dressing_room", "Fade_long") from _call_change_scene_294
#        else:
#            $ set_active("Shop_Visitor4", False)
#            $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
#            call refresh_scene_fade()

        $ restore_music()
#        call refresh_scene_fade()
        return False

label ep25_quests_shop_visitors4a:
    # Примерочная
    $ store_music()
    call cit4_dialog_3a() from _call_cit4_dialog_3a
    $ restore_music()
    if _return == 0:
#        $ shopVisitorStage4 = 4
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        $ move_object("Shop_Visitor4", "cloth_shop_view1")
        $ set_active("Shop_Visitor4", False, scene="cloth_shop_view1")
#        $ set_active("Shop_Visitor4", False)
        call change_scene("cloth_shop_view1", "Fade_long") from _call_change_scene_295
        return False

    if _return == 1:
        $ shopVisitorStage4 = 4
        $ shopVisitorsList.remove("Shop_Visitor4")
        $ move_object("Shop_Visitor4", "cloth_shop_view1")
        $ set_active("Shop_Visitor4", False, scene="cloth_shop_view1")
        $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_dressing_room2")
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_4
        return False

    if _return == 2:
        $ move_object("Shop_Visitor4", "cloth_shop_view1")
        $ set_var("Shop_Visitor4", base="Cloth_Shop_View1_Visitor4_EveningDress", zorder=11, scene="cloth_shop_view1")
        $ add_hook_multi("ep25_quests_shop_visitors4c", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitor4"], filter={"group":"cloth_shop_visitors"})
        $ add_hook_multi("ep25_quests_shop_visitors4c", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitor4"], filter={"group":"cloth_shop_visitors"})
        $ add_hook("Shop_Visitor4", "ep25_quests_shop_visitors4b", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitor4"])
        $ add_hook("Monica", "cit4_dialog_3h", scene="cloth_shop_view1", label=["cloth_shop_quests", "shop_visitor4"])
        $ add_hook("Monica", "cit4_dialog_3h", scene="cloth_shop_view2", label=["cloth_shop_quests", "shop_visitor4"])
        $ add_hook("Cashier", "ep25_quests_shop_visitors4d", scene="cloth_shop_cashier", label=["cloth_shop_quests", "shop_visitor4"])
        $ cloth = "Nude"
        $ cloth_type = "Nude"
        call change_scene("cloth_shop_dressing_room", "Fade_long") from _call_change_scene_296
        return False

#    if _return != False:
#        $ shopVisitorStage4 = 4
#        $ shopVisitorsList.remove("Shop_Visitor4")
#        $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_dressing_room2")
#    else:
#        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_dressing_room2")
#    $ set_active("Shop_Visitor4", False)
#    call refresh_scene_fade_long()
    return

label ep25_quests_shop_visitors4b:
    # Моника говорит с посетительницей в зале (голая)
    if act=="l":
        mt "Эта стерва ходит по залу в моем платье! НЕНАВИЖУ!"
        return False
    $ store_music()
    if ep25_quests_shop_visitors4bFlag == True:
        call cit4_dialog_3c() from _call_cit4_dialog_3c
    if ep25_quests_shop_visitors4bFlag == False:
        call cit4_dialog_3b() from _call_cit4_dialog_3b
        $ ep25_quests_shop_visitors4bFlag = True
    $ restore_music()
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_5
    return False

label ep25_quests_shop_visitors4c:
    # Моника отказывается говорить с другими посетителями голой
    if act=="l":
        return
    call cit4_dialog_3d() from _call_cit4_dialog_3d
    return False

label ep25_quests_shop_visitors4d:
    # Моника голая подходит к продавщице
    if act=="l":
        return
    $ store_music()
    call cit4_dialog_3g() from _call_cit4_dialog_3g
    $ restore_music()
    if _return == False:
        call change_scene("cloth_shop_view1", "Fade_long") from _call_change_scene_297
        return False

    # Завершение квеста с shop visitor 4
    $ cloth = "EveningDress"
    $ cloth_type = "SellingDress"
    $ shopVisitorStage4 = 4
    call change_scene("cloth_shop_view1", "Fade_long") from _call_change_scene_298
    $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_view1")
    $ shopVisitorsList.remove("Shop_Visitor4")
    $ set_active("Shop_Visitor4", False)
    $ set_var("Shop_Visitor4", base="Cloth_Shop_View1_v4", zorder = 5, scene="cloth_shop_view1")
    $ remove_hook(label="shop_visitor4")
    return False


label ep25_quests_shop_visitors5:
    if shopVisitorStage5 > 3:
        return
    if act=="l":
        mt "Какая-то малявка. Что она делает в магазине? У нее есть вообще деньги?"
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_4
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_4 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage5 == 1:
        call cit5_dialog_1() from _call_cit5_dialog_1
        $ shopVisitorStage5 = 2
        $ set_active("Shop_Visitor5", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_116
        call ep25_quests_shop13() from _call_ep25_quests_shop13_10 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage5 == 2:
        call cit5_dialog_2() from _call_cit5_dialog_2
        $ shopVisitorStage5 = 3
        $ set_active("Shop_Visitor5", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_117
        call ep25_quests_shop13() from _call_ep25_quests_shop13_11 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage5 == 3:
        $ store_music()
        call cit5_dialog_3() from _call_cit5_dialog_3
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor5")
            $ shopVisitorStage5 = 4
        $ restore_music()
        $ set_active("Shop_Visitor5", False)
        $ autorun_to_object("ep25_dialogues1_shop24c", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_118
        call ep25_quests_shop13() from _call_ep25_quests_shop13_12 # Проверка на конец работы (нет посетителей)
        return False
    return
label ep25_quests_shop_visitors6:
    if shopVisitorStage6 > 3:
        return
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_5
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_5 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage6 == 1:
        $ store_music()
        call cit6_dialog_1() from _call_cit6_dialog_1
        $ restore_music()
        if _return != False:
            $ shopVisitorStage6 = 2
        $ set_active("Shop_Visitor6", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_119
        call ep25_quests_shop13() from _call_ep25_quests_shop13_13 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage6 == 2:
        $ store_music()
        call cit6_dialog_2() from _call_cit6_dialog_2
        $ restore_music()
        if _return != False:
            $ shopVisitorStage6 = 3
        $ set_active("Shop_Visitor6", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_120
        call ep25_quests_shop13() from _call_ep25_quests_shop13_14 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage6 == 3:
        $ store_music()
        call cit6_dialog_3() from _call_cit6_dialog_3
        $ restore_music()
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor6")
            $ shopVisitorStage6 = 4
        $ set_active("Shop_Visitor6", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view1")
        call refresh_scene_fade() from _call_refresh_scene_fade_121
        call ep25_quests_shop13() from _call_ep25_quests_shop13_15 # Проверка на конец работы (нет посетителей)
        return False
    return
label ep25_quests_shop_visitors7:
    if shopVisitorStage7 > 3:
        return
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_6
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_6 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage7 == 1:
        $ store_music()
        call cit7_dialog_1() from _call_cit7_dialog_1
        $ restore_music()
        if _return != False:
            $ shopVisitorStage7 = 2
        $ set_active("Shop_Visitor7", False)
        $ autorun_to_object("ep25_dialogues1_shop24b", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_122
        call ep25_quests_shop13() from _call_ep25_quests_shop13_16 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage7 == 2:
        $ store_music()
        call cit7_dialog_2() from _call_cit7_dialog_2
        $ restore_music()
        if _return != False:
            $ shopVisitorStage7 = 3
        $ set_active("Shop_Visitor7", False)
        $ autorun_to_object("ep25_dialogues1_shop24b", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_123
        call ep25_quests_shop13() from _call_ep25_quests_shop13_17 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage7 == 3:
        $ store_music()
        call cit7_dialog_3() from _call_cit7_dialog_3
        $ move_object("Shop_Visitor7", "cloth_shop_dressing_room2")
        $ add_hook("Shop_Visitor7", "ep25_quests_shop_visitors7a", scene="cloth_shop_dressing_room2")
        call change_scene("cloth_shop_dressing_room", "Fade_long") from _call_change_scene_299
#        else:
#            $ set_active("Shop_Visitor4", False)
#            $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
#            call refresh_scene_fade()

        $ restore_music()

    return False
label ep25_quests_shop_visitors7a:
    # В примерочной
    $ store_music()
    call cit7_dialog_3a() from _call_cit7_dialog_3a
    $ restore_music()
    if _return == False:
        $ autorun_to_object("ep25_dialogues1_shop24b", scene="cloth_shop_view2")
        $ move_object("Shop_Visitor7", "cloth_shop_view2")
        $ set_active("Shop_Visitor7", False, scene="cloth_shop_view2")
        call change_scene("cloth_shop_view2", "Fade_long") from _call_change_scene_300
        return False
    $ shopVisitorStage7 = 4
    $ shopVisitorsList.remove("Shop_Visitor7")
    $ autorun_to_object("ep25_dialogues1_shop24b", scene="cloth_shop_dressing_room2")
    $ move_object("Shop_Visitor7", "cloth_shop_view2")
    $ set_active("Shop_Visitor7", False, scene="cloth_shop_view2")
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_6
    return False
label ep25_quests_shop_visitors8:
    if shopVisitorStage8 > 3:
        return
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_7
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_7 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage8 == 1:
        call cit8_dialog_1() from _call_cit8_dialog_1
        $ shopVisitorStage8 = 2
        $ set_active("Shop_Visitor8", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_124
        call ep25_quests_shop13() from _call_ep25_quests_shop13_18 # Проверка на конец работы (нет посетителей)
        return False
    if shopVisitorStage8 == 2:
        $ store_music()
        call cit8_dialog_2() from _call_cit8_dialog_2
        if _return != False:
            $ shopVisitorStage8 = 3
        $ restore_music()
        $ set_active("Shop_Visitor8", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_125
        call ep25_quests_shop13() from _call_ep25_quests_shop13_19 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage8 == 3:
        $ store_music()
        call cit8_dialog_3() from _call_cit8_dialog_3
        if _return != False:
            $ move_object("Shop_Visitor8", "cloth_shop_dressing_room2")
            $ add_hook("Shop_Visitor8", "ep25_quests_shop_visitors8a", scene="cloth_shop_dressing_room2")
            call change_scene("cloth_shop_dressing_room", "Fade_long") from _call_change_scene_301
#        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        else:
            $ set_active("Shop_Visitor8", False)
            $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
            call refresh_scene_fade() from _call_refresh_scene_fade_126

        $ restore_music()
#        $ set_active("Shop_Visitor8", False)
#        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_127
#        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors8a:
    # Примерочная
    $ store_music()
    call cit8_dialog_3a() from _call_cit8_dialog_3a
    if _return != False:
        $ shopVisitorStage8 = 4
        $ shopVisitorsList.remove("Shop_Visitor8")
        $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_dressing_room2")
    else:
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_dressing_room2")
    $ move_object("Shop_Visitor8", "cloth_shop_view2")
    $ set_active("Shop_Visitor8", False, scene="cloth_shop_view2")
    $ restore_music()
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_7
    return

label ep25_quests_shop_visitors9:
    if shopVisitorStage9 > 3:
        return
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_8
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_8 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage9 == 1:
        $ store_music()
        call cit9_dialog_1() from _call_cit9_dialog_1
        $ restore_music()
        if _return != False:
            $ shopVisitorStage9 = 2
        $ set_active("Shop_Visitor9", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_128
        call ep25_quests_shop13() from _call_ep25_quests_shop13_20 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage9 == 2:
        $ store_music()
        call cit9_dialog_2() from _call_cit9_dialog_2
        $ restore_music()
        if _return != False:
            $ shopVisitorStage9 = 3
        $ set_active("Shop_Visitor9", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade() from _call_refresh_scene_fade_129
        call ep25_quests_shop13() from _call_ep25_quests_shop13_21 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage9 == 3:
        $ store_music()
        call cit9_dialog_3() from _call_cit9_dialog_3
        $ restore_music()
        if _return != False:
#        $ set_active("Shop_Visitor9", False)
            $ move_object("Shop_Visitor9", "cloth_shop_dressing_room2")
            $ add_hook("Shop_Visitor9", "ep25_quests_shop_visitors9a", scene="cloth_shop_dressing_room2")
            call change_scene("cloth_shop_dressing_room", "Fade_long") from _call_change_scene_302
#        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        else:
            $ set_active("Shop_Visitor9", False)
            call refresh_scene_fade() from _call_refresh_scene_fade_130
#        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return

label ep25_quests_shop_visitors9a:
    # В примерочной
    $ store_music()
    call cit9_dialog_3a() from _call_cit9_dialog_3a
    $ restore_music()
    if _return != False:
        $ shopVisitorStage9 = 4
        $ shopVisitorsList.remove("Shop_Visitor9")
        $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_dressing_room2")
    else:
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_dressing_room2")
    $ move_object("Shop_Visitor9", "cloth_shop_view2")
    $ set_active("Shop_Visitor9", False, scene="cloth_shop_view2")
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_8
    return

label ep25_quests_shop_visitors10:
    if shopVisitorStage10 > 3:
        return
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working() from _call_ep25_quests_shop_visitors_not_working_9
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() from _call_ep25_dialogues1_shop21_9 # Ждет покупатель в примерочной
        return False

    if shopVisitorStage10 == 1:
        $ store_music()
        call cit10_dialog_1() from _call_cit10_dialog_1
        $ restore_music()
        if _return != False:
            $ shopVisitorStage10 = 2
        $ set_active("Shop_Visitor10", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view2")
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_9
        call ep25_quests_shop13() from _call_ep25_quests_shop13_22 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage10 == 2:
        $ store_music()
        call cit10_dialog_2() from _call_cit10_dialog_2
        $ restore_music()
        if _return != False:
            $ shopVisitorStage10 = 3
        $ set_active("Shop_Visitor10", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view2")
        call refresh_scene_fade_long() from _call_refresh_scene_fade_long_10
        call ep25_quests_shop13() from _call_ep25_quests_shop13_23 # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage10 == 3:
        $ store_music()
        call cit10_dialog_3() from _call_cit10_dialog_3
        $ restore_music()
        $ move_object("Shop_Visitor10", "cloth_shop_dressing_room2")
        $ add_hook("Shop_Visitor10", "ep25_quests_shop_visitors10a", scene="cloth_shop_dressing_room2")
        call change_scene("cloth_shop_dressing_room", "Fade_long") from _call_change_scene_303
        return False
    return False

label ep25_quests_shop_visitors10a:
    # В примерочной
    $ store_music()
    call cit10_dialog_3a() from _call_cit10_dialog_3a
    $ restore_music()
    if _return == False:
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view2")
        $ move_object("Shop_Visitor10", "cloth_shop_view2")
        $ set_active("Shop_Visitor10", False, scene="cloth_shop_view2")
        call change_scene("cloth_shop_view2", "Fade_long") from _call_change_scene_304
        return False
    $ shopVisitorStage10 = 4
    $ shopVisitorsList.remove("Shop_Visitor10")
    $ move_object("Shop_Visitor10", "cloth_shop_view2")
    $ set_active("Shop_Visitor10", False, scene="cloth_shop_view2")
    $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_dressing_room2")
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_11
    return False

label ep25_quests_shop_visitors_not_working:
    call ep25_dialogues1_shop19() from _call_ep25_dialogues1_shop19
    return
