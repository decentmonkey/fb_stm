default ep214_quests_citizens_stage2 = False

label ep214_quests_citizens_regular:
    call ep214_dialogues2_citizens_23() from _rcall_ep214_dialogues2_citizens_23

label ep214_quests_citizens_regular_loop1:
    call pylonController(1, 1, 1) from _rcall_pylonController
    with fade
    menu:
        "Придумать что-нибудь, чтобы заработать деньги." if citizenId == 1 or citizenId == 7:
            if citizenId == 1:
                menu:
                    "Пригласить к себе.":
                        call ep214_quests_citizen1_2a() from _rcall_ep214_quests_citizen1_2a
                    "Назад.":
                        jump ep214_quests_citizens_regular_loop1
            if citizenId == 7:
                menu:
                    "Работа натурщицой.":
                        call ep214_quests_citizen7a() from _rcall_ep214_quests_citizen7a
                    "Назад.":
                        jump ep214_quests_citizens_regular_loop1

        "Придумать что-нибудь, чтобы заработать деньги. (в будущих обновлениях) (disabled)" if citizenId != 1 and citizenId != 7:
            pass
        "Уйти.":
            call pylonController(1, 1, 2) from _rcall_pylonController_1
            with fade
            m "Я... Передумала..."
            if citizenId == 1:
                call pylonController(5, 1, 1) from _rcall_pylonController_2
                citizen1 "Не ожидал я такого тетя. Думаю, ты скоро передумаешь."
            if citizenId == 3:
                call pylonController(5, 1, 1) from _rcall_pylonController_3
                citizen3 "Похоже, я только зря потратил с тобой время..."
            if citizenId == 4:
                call pylonController(5, 1, 1) from _rcall_pylonController_4
                citizen4 "Какое то не продуктивное вышло знакомство. Надеюсь, в другой раз будет лучше."
            if citizenId == 5:
                call pylonController(5, 1, 1) from _rcall_pylonController_5
                citizen5 "Мистер разочарован, он ничего не посмотрел."
            if citizenId == 6:
                call pylonController(5, 1, 1) from _rcall_pylonController_6
                citizen6 "Похоже, я зря потратил свое время, пойду найду другую шлюху."
            if citizenId == 7:
                call pylonController(5, 1, 1) from _rcall_pylonController_7
                citizen7 "Ты не дала мне ни капли вдохновения!"
            if citizenId == 8:
                call pylonController(5, 1, 1) from _rcall_pylonController_8
                citizen8 "Сделки нет, ты не выполнила свою часть."
            if citizenId == 9:
                call pylonController(5, 1, 1) from _rcall_pylonController_9
                citizen9 "Дамочка, ни цента! Ничего не получишь!"
            if citizenId == 13:
                call pylonController(5, 1, 1) from _rcall_pylonController_10
                citizen13 "Подруга, в следующий раз не халтурь."
            if citizenId == 15:
                call pylonController(5, 1, 1) from _rcall_pylonController_11
                citizen15 "Сходи поищи себе кого-нибудь еще."
            call falling_path_store_customer() from _rcall_falling_path_store_customer
            $ autorun_to_object("ep214_dialogues2_citizens_24", scene="hostel_edge_1_a")
            call refresh_scene_fade() from _rcall_refresh_scene_fade_103
            return False
    call falling_path_store_customer() from _rcall_falling_path_store_customer_1
    call refresh_scene_fade() from _rcall_refresh_scene_fade_104
    return False


label ep214_quests_citizen1_2a: # пригласить к себе (панки)
    call ep214_dialogues2_citizens_16() from _rcall_ep214_dialogues2_citizens_16
    if _return == False:
        $ questHelp("work_slums_47", False, skipIfTrue=True)
        $ autorun_to_object("ep214_dialogues2_citizens_17b", scene="hostel_edge_1_a")
        return
    $ questHelp("work_slums_47", True)
    call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_132
    call ep214_dialogues2_citizens_17() from _rcall_ep214_dialogues2_citizens_17 # апартаменты Моники в трущобах
    if _return == False:
        fadeblack 2.0
        call bitch(5, "ep214_quests_citizen1_2a") from _rcall_bitch_12
        $ autorun_to_object("ep214_dialogues2_citizens_17b", scene="street_monicahome")
        return
    fadeblack 2.0
    $ add_corruption(15, "citizen1_2_scene_blowjob")
    $ autorun_to_object("ep214_dialogues2_citizens_24b", scene="street_monicahome")

    return

label ep214_quests_citizen7a: # работа натурщицой
    call ep214_dialogues2_citizens_18() from _rcall_ep214_dialogues2_citizens_18
    if _return == -1:
        $ questHelp("work_slums_48", False, skipIfTrue=True)
        $ autorun_to_object("ep214_dialogues2_citizens_17c", scene="hostel_edge_1_a")
        return
    $ questHelp("work_slums_48", True)
    if _return == -2:
        $ autorun_to_object("ep214_dialogues2_citizens_17d", scene="hostel_edge_1_a")
        return
    if _return == -3:
        fadeblack 2.0
        $ autorun_to_object("ep214_dialogues2_citizens_17c", scene="street_monicahome")
        call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_133
        return
    fadeblack 2.0
    $ autorun_to_object("ep214_dialogues2_citizens_24b", scene="street_monicahome")
    call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_134
    return



















#
