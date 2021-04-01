default photostudioEmpty = False
default melanieAlexBeforePhotoshoot = True
default melanieAlexAfterPhotoshoot = False
default photostudioLightsCntLooked = 0

label EP1_monica_office_photostudio:
    $ print "enter_monica_office_photostudio"
    $ miniMapData = []

    $ scene_name = "monica_office_photostudio"
    $ scene_caption = t_("Photostudio")
    $ clear_scene_from_objects(scene_name)

    if photostudioEmpty == True:
        $ scene_image = "scene_Office_Monica_PhotoStudio"
    else:
        if melanieAlexBeforePhotoshoot == True:
            $ scene_image = "scene_Office_Monica_PhotoStudio_Melanie_Alex"
            $ EP1_add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Melanie1", "click" : "EP1_monica_office_photostudio_environment", "actions" : "lt", "zorder":10})
            $ EP1_add_object_to_scene("AlexPhotograph", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Alex1", "click" : "EP1_monica_office_photostudio_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png" })

        if melanieAlexAfterPhotoshoot == True:
            $ scene_image = "scene_Office_Monica_PhotoStudio_Melanie_Alex2"
            $ EP1_add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Melanie2", "click" : "EP1_monica_office_photostudio_environment", "actions" : "lt", "zorder":10})
            $ EP1_add_object_to_scene("AlexPhotograph", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Alex2", "click" : "EP1_monica_office_photostudio_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png" })


    $ EP1_add_object_to_scene("Box1", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Box1", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15})
    $ EP1_add_object_to_scene("Boxes", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Boxes", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15})
    $ EP1_add_object_to_scene("Cloth", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Cloth", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":0})
    $ EP1_add_object_to_scene("SpotLight1", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight1", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":1 ,"b":0.15})
    $ EP1_add_object_to_scene("SpotLight2", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight2", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":1 ,"b":0.15})
    $ EP1_add_object_to_scene("SpotLight3", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight3", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15})
    $ EP1_add_object_to_scene("SpotLight4", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight4", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":2 ,"b":0.15})
    $ EP1_add_object_to_scene("Top_Spotlights", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Top_Spotlights", "click" : "EP1_monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15})

    $ EP1_add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : t_("К СЕКРЕТАРЮ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_monica_office_photostudio_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_monica_office_photostudio_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Monica_Office_Secretary":
        call EP1_change_scene("monica_office_secretary")
        return
    return
label EP1_monica_office_photostudio_environment(obj_name, obj_data):
    if obj_name == "Melanie":
        if obj_data["action"] == "l":
            "Мелани - это моя топ-модель на сегодняшний день."
            "Посмотрим, долго-ли она будет ей оставаться..."
        if obj_data["action"] == "t":
            if melanieAlexBeforePhotoshoot == True:
                jump EP1_monkeys_monica_photostudio1_2
            if melanieAlexAfterPhotoshoot == True:
                call EP1_monkeys_melanie_alex_after_photoshoot1(obj_name, obj_data)
                return

    if obj_name == "AlexPhotograph":
        if obj_data["action"] == "l":
            "Алекс - мой фотограф.
            Самый лучший профессионал в стране, которого можно купить за деньги."
        if obj_data["action"] == "t":
            if melanieAlexBeforePhotoshoot == True:
                jump EP1_monkeys_monica_photostudio1_2
            if melanieAlexAfterPhotoshoot == True:
                call EP1_monkeys_melanie_alex_after_photoshoot1(obj_name, obj_data)
                return

    if obj_name == "Box1":
        m "Этот световой бокс для заполняющего света, снизу."
    if obj_name == "Boxes":
        m "Какие-то ящики с хламом."
        "Конечно там не хлам, а дорогое оборудование, но тем не менее..."
    if obj_name == "Cloth":
        m "Полотно для фона во время съемок."
        $ photostudioLightsCntLooked += 1
    if obj_name == "SpotLight1" or obj_name == "SpotLight2":
        m "Софтбокс для бокового света, насколько я помню..."
        $ photostudioLightsCntLooked += 1
    if obj_name == "SpotLight3":
        m "Это просветный зонт, для заливающего света."
        $ photostudioLightsCntLooked += 1
    if obj_name == "SpotLight4":
        m "Это контровой свет.
        Цветной."
        $ photostudioLightsCntLooked += 1

    if obj_name == "Top_Spotlights":
        m "Эти прожекторы освещают модель сверху, а также подсвечивают фон за ней."
        $ photostudioLightsCntLooked += 1

    if photostudioLightsCntLooked == 5:
        m "Сколько же света надо, чтобы модель получилась красивой!"
        "Далеко не все знают науку о том как надо использовать свет!
        И в фото, и в фильмах и в компьютернах играх!"


    return


label EP1_monica_office_photostudio_autorun_monica_day_1:
    m "Ага!"
    "Здесь как раз Мелани и Алекс."
    "Смотрю они как раз собираются делать фотосессию."
    if monkeysOffended1 == True:
        m "Хорошая возможность, чтобы показать этим мартышкам... кто они..."
    else:
        m "Хорошая возможность показать кандидаткам, что они не подходят."
    return





#
