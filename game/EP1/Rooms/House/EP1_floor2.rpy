default floor2SpotJustMade = False
default floor2SpotEnabled = False
default flowerViewed = False

label EP1_floor2:
    $ print "enter_floor2"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "floor2"
    $ scene_caption = t_("Hall Top Floor")
    $ clear_scene_from_objects(scene_name)
    $ monica_tint = [1.0, 1.0, 1.0]
    if (cloth_type == "Lingerie" or cloth_type == "HomeCloth"):
        $ monica_tint = [0.9, 0.9, 1.0]

    if gameStage < 2:
        if floor2SpotEnabled == True and (juliaPunished == False or juliaLocation != "floor2"):
            if juliaPunishedVoluntarily == False:
                $ EP1_add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Monica_" + cloth_type + "_Spot", "img_mask": "Floor2_Spot_Mask", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10, "hover_overlay":True})
            else:
                $ EP1_add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Monica_" + cloth_type + "_Spot", "img_mask": "Floor2_Spot_Mask", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":5, "hover_enabled":False})

        $ EP1_add_object_to_scene("Sofa", {"type":2, "base":"Floor2_Sofa", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Object", "click" : "EP1_floor2_teleport", "xpos" : 1030, "ypos" : 158, "zorder":9})
        if juliaPunished == False or juliaMonicaForgivenessAfterPunishment == True:
            $ scene_image = "scene_Floor2_Monica_" + cloth + day_suffix
            $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_" + cloth + day_suffix, "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
            if juliaPunishedVoluntarily == True:
                $ EP1_add_object_to_scene("Julia_Washing_Accessories", {"type" : 2, "base" : "Floor2_Washing_Accessories", "click" : "EP1_", "actions" : "l", "zorder":10, "hover_enabled":False})
                $ EP1_add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Monica_" + cloth_type + "_Spot", "img_mask": "Floor2_Spot_Washing_Accessories_Mask", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":5, "hover_overlay":True})
                $ EP1_add_object_to_scene("Sofa", {"type":2, "base":"Floor2_Sofa_Washing_Accessories", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
        else:
            $ scene_image = "scene_Floor2_Monica_Julia_" + cloth + day_suffix
            $ print "Floor2_Monica_Julia_" + cloth + day_suffix
            $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_Julia_" + cloth + day_suffix, "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
            if juliaLocation == "floor2":
                $ EP1_autorun_to_object("floor2", "floor2_julia_punished_autorun")
                $ EP1_add_object_to_scene("Julia", {"type" : 2, "base" : "Floor2_Julia_Punished_HomeCloth" + day_suffix, "click" : "EP1_julia_interact_punished", "actions" : "lt", "zorder":10})
                $ EP1_add_object_to_scene("Sofa", {"type":2, "base":"Floor2_Sofa_Washing_Accessories", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
            else:
                $ EP1_add_object_to_scene("Julia_Washing_Accessories", {"type" : 2, "base" : "Floor2_Washing_Accessories", "click" : "EP1_", "actions" : "l", "zorder":10, "hover_enabled":False})
                $ EP1_add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Monica_" + cloth_type + "_Spot", "img_mask": "Floor2_Spot_Washing_Accessories_Mask", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":5, "hover_overlay":True})
                $ EP1_add_object_to_scene("Sofa", {"type":2, "base":"Floor2_Sofa_Washing_Accessories", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})

            $ EP1_add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Object", "click" : "EP1_floor2_teleport", "xpos" : 1030, "ypos" : 58, "zorder":9})

        if floor2SpotEnabled == False:
            if hairDyeTaken == False:
                $ EP1_add_object_to_scene("Carpet", {"type" : 2, "base" : "Floor2_Carpet", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
            else:
                $ EP1_add_object_to_scene("Carpet", {"type" : 2, "base" : "Floor2_Carpet", "click" : "EP1_floor2_environment", "actions" : "lh", "zorder":10, "tint": monica_tint})
        $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors_Object", "click" : "EP1_floor2_environment", "actions" : "lw", "zorder" : 2})
        $ EP1_add_object_to_scene("Teleport_Bedroom", {"type":3, "text" : t_("СПАЛЬНЯ"), "rarrow" : "arrow_down_2", "base":"Floor2_Teleport_Bedroom", "click" : "EP1_floor2_teleport", "xpos" : 350, "ypos" : 1006, "zorder":11})
        $ EP1_add_object_to_scene("Teleport_Bathroom", {"type":3, "text" : t_("ВАННАЯ КОМНАТА"), "larrow" : "arrow_left_2", "base":"Floor2_Bathroom", "click" : "EP1_floor2_teleport", "xpos" : 350, "ypos" : 250, "zorder":15, "b":0.15, "tint":[1.0, 1.0, 0.9]})

    if gameStage >= 3:
        if bettyLocation == "Floor2":
            $ scene_image = "scene_Floor2_Monica_" + cloth + "_Evening"
            $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_" + cloth + "_Evening", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
            $ EP1_add_object_to_scene("Betty", {"type" : 2, "base" : "Floor2_Betty_" + str(renpy.random.randint(1,3)) + "_Evening", "click" : "EP1_bettyInteract1", "actions" : "lt", "zorder":10})
        else:
            $ scene_image = "scene_Floor2_Monica_" + cloth + day_suffix
            $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_" + cloth + day_suffix, "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        $ EP1_add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Spot", "click" : "EP1_floor2_environment", "actions" : "l", "zorder":10})
        $ EP1_add_object_to_scene("Teleport_BedroomBardie", {"type":3, "text" : t_("КОМНАТА БАРДИ"), "larrow" : "arrow_left_2", "base":"Floor2_Teleport_BedroomBardie", "click" : "EP1_floor2_teleport", "xpos" : 341, "ypos" : 454, "zorder":11})
        $ EP1_add_object_to_scene("Teleport_BedroomSecond", {"type":3, "text" : t_("СПАЛЬНЯ ДЛЯ ГОСТЕЙ"), "larrow" : "arrow_left_2", "base":"Floor2_Teleport_BedroomSecond", "click" : "EP1_floor2_teleport", "xpos" : 420, "ypos" : 916, "zorder":15, "b":0.15, "tint":[1.0, 1.0, 0.9]})
        $ EP1_add_object_to_scene("Teleport_Bedroom", {"type":3, "text" : t_("СПАЛЬНЯ ХОЗЯЕВ"), "larrow" : "arrow_down_2", "base":"Floor2_Teleport_Bedroom", "click" : "EP1_floor2_teleport", "xpos" : 1570, "ypos" : 1006, "zorder":11})
        $ EP1_add_object_to_scene("Teleport_Bathroom", {"type":3, "text" : t_("ВАННАЯ КОМНАТА"), "larrow" : "arrow_left_2", "base":"Floor2_Bathroom", "click" : "EP1_floor2_teleport", "xpos" : 350, "ypos" : 250, "zorder":15, "b":0.15, "tint":[1.0, 1.0, 0.9]})
        $ EP1_add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Object", "click" : "EP1_floor2_teleport", "xpos" : 1030, "ypos" : 58, "zorder":9})
        $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors_Object", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})


    $ EP1_add_object_to_scene("Flower1", {"type":2, "base":"Floor2_Flower1", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flower2", {"type":2, "base":"Floor2_Flower2", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Lamps", {"type":2, "base":"Floor2_Lamps", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})

#    $ EP1_add_object_to_scene("Teleport_Floor2_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Floor2_Stairs_Object", "click" : "EP1_floor2_teleport", "xpos" : 1030, "ypos" : 158, "zorder":9})

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

    return

label EP1_floor2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor2_Stairs":
        call EP1_change_scene("floor2_stairs")
    if obj_name == "Teleport_Bedroom":
        call EP1_change_scene("bedroom2")
    if obj_name == "Teleport_Bathroom":
        call EP1_change_scene("bathroom_bath")
    if obj_name == "Teleport_BedroomBardie":
        call EP1_change_scene("bedroom_bardie")
        return
    if obj_name == "Teleport_BedroomSecond":
        call EP1_change_scene("bedroom_second")
        return

    return

label EP1_floor2_environment(name, obj_data):
    if name == "Lamps":
        if gameStage > 2:
            mt "Мне всегда нравилось когда много света."
            "Ничего, скоро я снова буду радоваться этому!"
            return
        m "Свет! Много света!"

        "Много света - это признак вкуса!"

        "А вкус у меня есть, ведь я владею самым модным журналом!"

        "А если вы попробуете возразить, то я напишу в своем журнале что это у вас нет вкуса!"

        "И все это будут знать!
        Хи-хи."

    if name == "Sofa":
        m "Диваны, кресла."

        "Мебель, конечно дорогая..."

        "Конечно удобная, но..."

        "Мне уже скучно это разглядывать"

    if name == "Flower1":
        if gameStage > 2:
            mt "Это мои цветы!"
            "МОИ!!!"
            return
        m "Это..."

        if flowerViewed == False:
            "Buxus!"
        else:
            "Тоже Buxus!"

        "Он отлично сочитается с интерьером!"
        $ flowerViewed = True
    if name == "Flower2":
        if gameStage > 2:
            mt "Это мои цветы!"
            "МОИ!!!"
            return
        m "Это..."

        if flowerViewed == False:
            "Buxus!"
        else:
            "Тоже Buxus!"

        "Он похож на елочку.

        Он еще мне кое-что напоминает..."

        "Не могу вспомнить что.
        Да и ладно..."

        $ flowerViewed = True

    if name == "Mirrors":
        if obj_data["action"] == "l":
            if gameStage > 2:
                mt "Это мои зеркала с косметикой..."
                "Сейчас их захватила эта сучка Бетти."
                "Но это ненадолго!"
                return
            m "Мои любимые зеркала."

            "Духи, тени, косметика...
            Ну.. в общем все такое."

            "Это мое!!!"

        if obj_data["action"] == "w":
            call EP1_change_scene("floor2_mirrors")
            return


    if name == "Carpet":
        if obj_data["action"] == "l":
            m "Я люблю ковры."

            "Мне нравится этот, но..."

            "Мне кажется что его уже пора поменять."

            if julia_monica_revenge_in_progress == True:
                m "Отличное место для того чтобы что-то разлить сюда!"
                "Я думаю Юлия будет рада!
                Хи-хи."
        if obj_data["action"] == "h":
            call EP1_floor2_julia_monica_revenge_spill_hairdye_confirm()
            return

    if name == "Monica":
        if gameStage > 2:
            m "Они захватили мой дом, но я верну его!"
            return
        if floor2SpotEnabled == False and juliaPunished == False:
            m "Этот просторный холл я использую для того чтобы приводить себя в порядок."

            "Здесь мои зеркала и косметика."

            "Мне здесь очень уютно.
            Я люблю когда много места."

            "Не понимаю людей, которые ютятся в тесных каморках.
            Фи!"

        if floor2SpotEnabled == True and juliaPunished == False:
            m "Мой любимый холл..."

            "Теперь его дополняет это очаровательное пятно на полу."

            "Хм..."

        if juliaPunished == True:
            if juliaLocation != "floor2":
                m "На вид пятно не уменьшилось.
                Налицо некомпетентность..."
                return
            m "В этом холле прекрасно все!"

            "Кроме елозящего туда-сюда зада этой неумехи Юлии!"

            if juliaMonicaLied == False:
                m "Которая ужа так долго возится с каким-то небольшим пятнышком на ковре!"

                "Я не думаю что она сердится, ведь я нечаянно его поставила."

                "Меня ведь никто не будет ругать за это?
                Хи-хи :)"

            else:
                m "Которая ужа так долго возится с каким-то небольшим пятнышком на ковре!"

                "Которое сама же и поставила!"

                "Ей трудно будет его оттереть, но люди должны отвечать на свои промахи.
                Хи-хи :)"

    if name == "Spot":
        if obj_data["action"] == "l":
            if gameStage >= 3:
                mt "Пятно на ковре все еще здесь..."
                "Может быть эта Бетти не заметила его?"
                "Я уж точно не собираюсь его убирать!"
                "Этому ковру нужна химчистка!"
                return
            if floor2SpotJustMade == True:
                img 1065
                if julia_monica_revenge_undo_in_progress == False:
                    m "Отлично!
                    Так-то лучше!"

                    "Все.
                    Теперь я себя чувствую отлично."

                    "Можно ехать по делам."
                else:
                    m "Не знаю правильно-ли я сделала.
                    Но теперь ничего не изменишь."

                    "Хотя, все-равно я хотела менять этот ковер."
                    "Ладно, поеду по делам."
                return

            if juliaPunishedLow == True:
                m "Грязное пятно."
                if juliaMonicaLied == True:
                    m "Нерадивые работники никогда не убирают за собой."
                else:
                    m "Возможно я еще заставлю Юлию его убрать.
                    Подумаю..."
                return
            if juliaPunishedVoluntarily == True:
                m "Надеюсь у Юлии получится его убрать.
                Если не получится, то я не буду ее мучать."
                "Проще заменить ковер."
                return
            if juliaPunished == True:
                m "На вид пятно не уменьшилось.
                Налицо некомпетентность..."
                return
            m "Зря я его поставила."
            "Теперь точно придется менять ковер."


    return
