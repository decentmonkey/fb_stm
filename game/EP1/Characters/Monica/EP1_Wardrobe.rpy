default businessClothEnabled = False
default businessClothNotFoundDay1 = False
default businessClothNotFoundDay1Seen = False
default businessClothSearchDressInProgress = False
default businessCloth2NotFoundDay2 = False
default businessCloth2FoundedDay2 = False
default wardrobeDay2EveningBlocked = True

init python:
    def EP1_change_cloth(in_cloth_type, in_cloth_name):
        global cloth_type, cloth
        cloth_type = in_cloth_type
        cloth = in_cloth_name

label EP1_wardrobe(name, obj_data):
    if obj_data["action"] == "l":
        m "Мой любимый гардероб."

        "Здесь я храню свою одежду.
        Конечно же не всю!
        Она бы не поместилась сюда!"

        "Здесь обычно только то что я собираюсь одевать именно сегодня."

        "В обязанности гувернантки входит содержать одежду в надлежащем порядке."

        "Ведь я никогда не одеваю одну и ту же одежду дважды!"
        return
    #1020, 1479
    #1453 night

    if day == 1:
        if day_time == "day":
            img 1479
            sound wardrobe_open
            m "Что бы мне надеть?"

            menu:
                "Нижнее белье":
                    sound snd_found_dress
#                    $ remove_dialogue()
                    img 1022
                    with fade
                    "У меня отличные бедра."
                    w
                    $ EP1_change_cloth("Lingerie", "Lingerie1")

                "Домашняя одежда":
#                    $ day_time = "evening"
#                    $ day_suffix = "_Evening"
                    $ remove_objective("dress_homecloth")
                    sound snd_found_dress
#                    $ remove_dialogue()
                    img 1023
                    with fade
                    "Очень мило смотрится."
                    img 1024
                    w
                    $ EP1_change_cloth("HomeCloth", "HomeCloth1")

                "Красивое платье":
                    if bathTaken == False:
                        m "Мне надо принять душ прежде чем одевать одежду на выход!"
                        return

                    if businessClothNotFoundDay1 == True:
                        if businessClothNotFoundDay1Seen == False:
                            m "Хм. Странно. Платья тут нет."

                        if juliaMonicaYell == True:
                            "Так, ну все.
                            Где эта Юлия???"
                            "Пойду отчитаю ее и сделаю последнее предупреждение."

                            "В любом случае у нее не более 5 минут чтобы подготовить мое платье!"
                        else:
                            "Где Юлия?"
                        if businessClothNotFoundDay1Seen == True:
                            return
                        $ businessClothNotFoundDay1Seen = True
                        $ add_objective("find_julia", t_("Найти Юлию и узнать где платье."), c_pink, 20)
                        $ EP1_autorun_to_object("floor1_stairs", "EP1_floor1_no_julia")
                        call EP1_question_helper_enable("EP1_question_helper_hairdye_find_julia")

                        call EP1_julia_scene_basement1() from _ep1call_julia_scene_basement1

                        return

                    if businessClothEnabled == False:
                        m "Рано одеваться на выход.
                        Надо доделать домашние дела."
                        return

                    $ remove_inventory("businesscloth1", 1)
                    $ remove_objective("dress_businesscloth")

                    sound snd_found_dress
#                    $ remove_dialogue()
                    img 1058
                    with fade
                    img 1059
                    "Весь мир у моего каблука!"

                    img 1060
                    mt "Теперь пойду вниз.
                    Надо выйти на улицу."

                    $ miniMapEnabledOnly = ["Bedroom", "Floor2"]

                    $ EP1_autorun_to_object("floor2", "EP1_floor2_julia_monica_revenge_start")
                    $ EP1_change_cloth("BusinessCloth", "BusinessCloth1")
                    $ EP1_subst_to_object("Wardrobe", "EP1_wardrobe_blocked_day1_day")
        if day_time == "evening":
            label EP1_wardrobe_menu_loop1:
            menu:
                "Нижнее белье":
                    sound snd_found_dress
                    img 3384
                    with fade
                    "У меня отличные бедра."
                    w
                    $ EP1_change_cloth("Lingerie", "Lingerie2")
                    $ remove_inventory("businesscloth1", 1)

                "Домашняя одежда":
                    $ remove_objective("dress_homecloth")

                    sound snd_found_dress
                    img 1454
                    with fade
                    "Очень мило смотрится."
                    $ EP1_change_cloth("HomeCloth", "HomeCloth1")
                    $ remove_inventory("businesscloth1", 1)
                "Красивое платье (disabled)":
                    jump EP1_wardrobe_menu_loop1
    if day == 2:
        if day_time == "day":
            img 1479
            sound wardrobe_open
            m "Что бы мне надеть?"
            menu:
                "Нижнее белье":
                    sound snd_found_dress
                    img 1480
                    with fade
                    "У меня шикарные бедра."
                    w
                    $ EP1_change_cloth("Lingerie", "Lingerie2")

                "Домашняя одежда":
                    $ remove_objective("dress_homecloth")
                    sound snd_found_dress
                    img 1482
                    with fade
                    "Очень мило смотрится."
                    "Для дома..."
                    $ EP1_change_cloth("HomeCloth", "HomeCloth2")

                "Бизнес наряд":
                    if bathTaken == False:
                        m "Мне надо принять душ прежде чем одевать одежду на выход!"
                        return
                    if monicaEated == False:
                        m "Мне надо поесть прежде чем одевать одежду на выход!"
                        return
                    if juliaPunished == True and juliaMonicaForgivenessAfterPunishment == False and businessCloth2FoundedDay2 == False:
                        $ businessCloth2NotFoundDay2 = True
                        img 1481
                        mt "Бизнес наряда здесь нет."
                        "Надо спросить у Юлии."
                        "..."
                        "Меня это начинает бесить."
                        $ add_objective("ask_julia_businesscloth2", t_("Спросить у Юлии где мой бизнес наряд"), c_red, 3)
                        return
                    sound snd_found_dress
                    img 1512
                    with fade
                    w
                    img 1513
                    m "Теперь я готова делать Бизнес!"

                    $ remove_objective("go_outside_fitness")
                    $ add_objective("go_fitness", t_("Ехать в фитнес зал"), c_orange, 10)
                    $ EP1_change_cloth("BusinessCloth", "BusinessCloth2")
                    $ driverMode = 2
        if day_time == "evening":
            if wardrobeDay2EveningBlocked == True:
                m "Я не доделала дела в городе. Еще рано отдыхать."
                return
            img 1479
            sound wardrobe_open
            m "Что бы мне надеть?"
            menu:
                "Нижнее белье":
                    sound snd_found_dress
                    img 3391
                    with fade
                    m "У меня шикарные бедра."
                    w
                    $ EP1_change_cloth("Lingerie", "Lingerie3")

                "Домашняя одежда":
                    sound snd_found_dress
                    img 3392
                    with fade
                    m "Очень мило смотрится."
                    "Для дома..."
                    $ EP1_change_cloth("HomeCloth", "HomeCloth2")
            $ remove_objective("dress_homecloth")

    if day == 3:
        if day_time == "day":
            img 1479
            sound wardrobe_open
            m "Что бы мне надеть?"
            menu:
                "Нижнее белье":
                    sound snd_found_dress
                    img 1988
                    with fade
                    w
                    img 1989
                    with fade
                    m "У меня шикарные бедра."
                    $ EP1_change_cloth("Lingerie", "Lingerie3")

                "Домашняя одежда":
                    $ remove_objective("dress_homecloth")
                    sound snd_found_dress
                    img 1990
                    with fade
                    w
                    img 1991
                    with fade
                    m "Очень мило смотрится."
                    $ EP1_change_cloth("HomeCloth", "HomeCloth3")
                "Красивое платье":
                    if bathTaken == False:
                        m "Мне надо принять душ прежде чем одевать одежду на выход!"
                        return
                    if monicaEated == False:
                        m "Мне надо поесть прежде чем одевать одежду на выход!"
                        return
                    img 1992
                    with fade
                    w
                    img 1993
                    with fade
                    m "Весь мир у моего каблука!"
                    $ EP1_change_cloth("BusinessCloth", "BusinessCloth3")

    $ scene_label = scene_name
    if renpy.has_label("EP1_" + scene_label):
        $ scene_label = "EP1_" + scene_label
    call expression scene_label
    return

label EP1_Wardrobe_use_businesscloth:
    sound put_dress
    $ remove_objective("dress_businesscloth")
    $ remove_inventory("businesscloth1", 1)
    $ obj_data = {"action" : "h"}
    call EP1_wardrobe("Wardrobe", obj_data)
    return

label EP1_wardrobe_blocked_day1_day(obj_name, obj_data):
    m "Мне уже надоело переодеваться.
    Нет времени, пора ехать по делам."
    return
