label EP1_basement_pool:
    $ print "enter_basement_pool"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "basement_pool"
    $ scene_caption = t_("Basement Pool")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Basement_Pool_Monica_" + cloth
#    $ scene_image = "scene_Basement_Pool_Monica_BusinessCloth1"

    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Pool_Monica_" + cloth, "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    if cloth == "HomeCloth1" or cloth == "BusinessCloth1":
        $ EP1_add_object_to_scene("Bidet", {"type":2, "base":"Basement_Pool_Bidet", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Mat", {"type":2, "base":"Basement_Pool_Mat", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0, "b": 0.15, "s":1.1})
        $ EP1_add_object_to_scene("Rags", {"type":2, "base":"Basement_Pool_Rags", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0, "b":0.15})
        $ EP1_add_object_to_scene("Shower_Cabin", {"type":2, "base":"Basement_Pool_Shower_Cabin", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Pool_Water", {"type":2, "base":"Basement_Pool_Water", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Lamps", {"type":2, "base":"Basement_Pool_Lamps", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})

        $ EP1_add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Basement_Pool_Door1", "click" : "EP1_basement_pool_teleport", "xpos" : 1043, "ypos" : 173, "zorder":0, "tint": [1.0, 1.0, 0.6]})
        $ EP1_add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("ПРАЧЕЧНАЯ"), "larrow" : "arrow_left_2", "base":"Basement_Pool_Door2", "click" : "EP1_basement_pool_teleport", "xpos" : 1561, "ypos" : 408, "zorder":0, "tint": [1.0, 1.0, 0.6]})
    else:
        $ EP1_add_object_to_scene("Bidet", {"type":2, "base":"Basement_Pool_Bidet_b", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Mat", {"type":2, "base":"Basement_Pool_Mat_b", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0, "b": 0.15, "s":1.1})
        $ EP1_add_object_to_scene("Rags", {"type":2, "base":"Basement_Pool_Rags_b", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0, "b":0.15})
        $ EP1_add_object_to_scene("Shower_Cabin", {"type":2, "base":"Basement_Pool_Shower_Cabin_b", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Pool_Water", {"type":2, "base":"Basement_Pool_Water_b", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Lamps", {"type":2, "base":"Basement_Pool_Lamps_b", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})

        $ EP1_add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Basement_Pool_Door1_b", "click" : "EP1_basement_pool_teleport", "xpos" : 1043, "ypos" : 173, "zorder":0, "tint": [1.0, 1.0, 0.6]})
        $ EP1_add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("ПРАЧЕЧНАЯ"), "larrow" : "arrow_left_2", "base":"Basement_Pool_Door2_b", "click" : "EP1_basement_pool_teleport", "xpos" : 1561, "ypos" : 408, "zorder":0, "tint": [1.0, 1.0, 0.6]})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_basement_pool_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor1_Stairs":
        call EP1_change_scene("floor1_stairs", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Basement_Laundry":
        call EP1_change_scene("basement_laundry")
        return
    return

label EP1_basement_pool_environment(obj_name, obj_data):
    if obj_name == "Monica":
        m "Насколько помню, здесь одна дверь ведет назад в дом, а вторая в прачечную."

    if obj_name == "Lamps":
        if gameStage > 2:
            mt "Здесь не бывает настоящего солнца... "
            return
        m "Какой неприятный люминисцентный свет!
        Фи!"

    if obj_name == "Bidet":
        if gameStage > 2:
            if monicaBathroomForbidden == True:
                mt "Бетти запретила мне пользоваться ванной наверху."
                "Может быть мне можно пользоваться туалетом здесь?"
                "Но я сейчас не хочу..."
            return
        m "Не понимаю, зачем здесь туалетные атрибуты."

        "Тем более, зачем здесь биде?"

        "Им что, пользуется муж?"

        "Какая-то чушь!
        Наверное это случайно попало в план дизайна дома."

        "Очередное доказательство того, что стоит только не досмотреть за людьми, и они обязательно напортачат!"
    if obj_name == "Mat":
        if gameStage > 2:
            mt "Какой-то неприятный коврик."
            return
        m "Какой-то неприятный коврик."

        if juliaHasSexInPool == True:
            m "А это что, какие-то влажные следы?"

            "Наверное Юлия споткнулась и что-то разлила."

            "Никчемная гувернантка!"

        else:
            m "Мне неприятно на нем стоять!"

    if obj_name == "Rags":
        if gameStage > 2:
            mt "Какие-то полотенца..."
            return
        m "Здесь лежат какие-то тряпки мужа.
        Интересно, почему Юлия это не убрала."

    if obj_name == "Shower_Cabin":
        if gameStage > 2:
            if monicaBathroomForbidden == True:
                mt "Бетти запретила мне пользоваться ванной наверху."
                "Может быть мне можно пользоваться душем здесь?"
                "Но у меня уже нет сил... Я хочу спать..."
            return
        m "Я бы никогда не стала мыться в этой кабинке для душа."

        "Вещь должна быть либо очень модной, либо очень раскошной, как мой личный душ!"

        "Эта кабинка ни то, ни другое!"

        "Фи!"
    if obj_name == "Pool_Water":
        if gameStage > 2:
            mt "Вот и бассейн.
            Не понимаю зачем он нужен здесь."
            return
        m "Вот и бассейн.
        Не понимаю зачем он нужен здесь."

        m "Меня вполне устраивает бассейн у нас во дворе за домом."
        m "Насколько я помню, он был здесь с момента постройки.
        Еще очень давно."

        "Я никогда им не пользуюсь."

        "Здесь любит отдыхать муж, когда у него проблемы на работе."

        "Плавает здесь в одиночестве.
        И наверное плачет."

        "Тряпка."
    return
