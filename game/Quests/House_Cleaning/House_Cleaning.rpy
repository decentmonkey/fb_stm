default houseCleaningStoredScene = False
default cleaningLog = []

default rooms_clean_list_exclude = []

default spotCleaning = False
default monicaCleaningInProgressEngineWorkingFlag = False

default monicaHouseCleaningBettyAffection = True

default houseCleaningShortEnd = False
default rooms_dirty = []
#default houseCleaningCurrent = 3
#default houseCleaningCurrentList = []

label house_cleaning:
    # хук проверки на начало уборки
    if day_time != "day":
        return
    if cloth_type != "Governess":
        return
    if monicaCleaningInProgress == True:
        return
    if monicaLastCleaningOfferedDay == day:
        return


    $ monicaLastCleaningOfferedDay = day
    menu:
        "Начать уборку в доме.":
            call house_cleaning_start() from _call_house_cleaning_start
            return False
        "Не убираться сегодня...":
            return
    return

label house_cleaning_start:
    # старт уборки
    $ monicaCleaningRoomsAmount = 1
    
    $ houseCleaningShortEnd = False
    $ miniMapEnabledOnly = ["none"]
    if monicaCleaningInProgressEngineWorkingFlag == False:
        $ houseCleaningStoredScene = store_scene("House", recursive=True)
    $ monicaCleaningInProgress = True
    $ monicaCleaningInProgressEngineWorkingFlag = True
    $ monicaCleaningObject = ""
    $ rooms_clean_list = ["floor2", "floor1", "bedroom_second", "living_room", "bedroom2"]
    $ rooms_clean_list = [x for x in rooms_clean_list if x not in rooms_clean_list_exclude]
#    $ rooms_clean_list = ["floor1", "living_room"]
    $ rooms_dirty = random.sample(set(rooms_clean_list), monicaCleaningRoomsAmount)
    $ shuffle(rooms_dirty)

    if scene_name in rooms_dirty: #если мы в одной из комнат для уборки, то начинаем с нее
        $ idx1 = rooms_dirty.index(scene_name)
        $ rooms_dirty.pop(idx1)
        $ rooms_dirty.insert(0, scene_name)

    if "bedroom2" in rooms_dirty:
        $ rooms_dirty.insert(rooms_dirty.index("bedroom2"), "bedroom1")


    $ store_music()
    music Sugar_plum high

    call house_cleaning_start3() from _call_house_cleaning_start3

    call process_hooks("monica_cleaning_start", "global") from _call_process_hooks_27

    $ autorun_to_object("start_cleaning_dialogue1a", scene=rooms_dirty[0])
    call change_scene(rooms_dirty[0]) from _call_change_scene_173
#    call refresh_scene_fade()
    return

#label house_cleaning_start2:
#    call start_cleaning_dialogue1a()
#    return

label house_cleaning_start3:
    #создаем среду для уборки
    python:
        set_active(False, group="environment", scene="House", recursive=True)
        set_active(True, cleaning_group=True, scene="House", recursive=True)

    # Вешаем комментарии при входе на грязные сцены
    python:
        flag1 = False
        for room_name in rooms_dirty:
            if flag1 == False:
                autorun_to_object("start_cleaning_dialogue1", scene=room_name)
                flag1 = True
            else:
                autorun_to_object("start_cleaning_dialogue1b", scene=room_name)


    # Вешаем хуки на запрет телепортов

    python:
        for room_name in rooms_dirty:
            objects = get_objects(scene="House", recursive=True, teleport=True)
            if objects != False:
                for obj1 in objects:
                    add_hook(obj1[1], "cleaning_monica_goout1", scene=obj1[2])

    # Вешаем хуки на грязные предметы
    python:
        objects = get_objects(scene="House", recursive=True, cleaning_group=True)
        if objects != False:
            for obj1 in objects:
                add_hook(obj1[1], "house_cleaning_clean_object", scene=obj1[2])

    # Вешаем хук на Барди
    python:
        objects = get_objects("Bardie", scene="House", recursive=True)
        if objects != False:
            for obj1 in objects:
                add_hook(obj1[1], "bardieMonicaCleaningInteract", scene=obj1[2])

    # Вешаем хук на Монику
    python:
        objects = get_objects("Monica", scene="House", recursive=True)
        if objects != False:
            for obj1 in objects:
                add_hook(obj1[1], "cleaning_monica_comment", scene=obj1[2])

#    $ add_hook("Carpet", "house_cleaning_clean_object", scene="floor2")
#    $ add_hook("Sofa", "house_cleaning_clean_object", scene="floor2")
#    $ add_hook("Curtains", "house_cleaning_clean_object", scene="floor1")
#    $ add_hook("Picture", "house_cleaning_clean_object", scene="floor1")
#    $ add_hook("Furniture", "house_cleaning_clean_object", scene="floor1")
#    $ add_hook("BardieBed", "house_cleaning_clean_object", scene="bedroom_bardie")
#    $ add_hook("BedroomSecondBed", "house_cleaning_clean_object", scene="bedroom_second")
#    $ add_hook("LegChair", "house_cleaning_clean_object", scene="bedroom_second")
#    $ add_hook("TV", "house_cleaning_clean_object", scene="bedroom_second")
#    $ add_hook("Chair3", "house_cleaning_clean_object", scene="living_room")
#    $ add_hook("Chair4", "house_cleaning_clean_object", scene="living_room")
#    $ add_hook("Sofa", "house_cleaning_clean_object", scene="living_room")
#    $ add_hook("TableLamp1", "house_cleaning_clean_object", scene="living_room")
#    $ add_hook("Curtains", "house_cleaning_clean_object", scene="bedroom2")
#    $ add_hook("Wardrobe", "house_cleaning_clean_object", scene="bedroom2")
#    $ add_hook("Chair", "house_cleaning_clean_object", scene="bedroom1")
#    $ add_hook("Chair2", "house_cleaning_clean_object", scene="bedroom1")
#    $ add_hook("Bed", "house_cleaning_clean_object", scene="bedroom1")
#    $ add_hook("Mess", "house_cleaning_clean_object", scene="bedroom1")
#    $ add_hook("Carpet", "house_cleaning_clean_object", scene="bedroom1")

    return


label house_cleaning_end:
    $ autorun_to_object("house_cleaning_end2")
    call refresh_scene("Dissolve_fast") from _call_refresh_scene_5
    return
label house_cleaning_end2:
    $ add_corruption(monicaCleaningAddCorruptionPerCleaning, "monica_cleaning_corruption_day_" + str(day))
    call cleaning_monica_finished1() from _call_cleaning_monica_finished1
    $ monicaCleaningInProgress = False
    $ monicaCleaningInProgressEngineWorkingFlag = False
    $ restore_scene(houseCleaningStoredScene)
    call process_hooks("monica_cleaning_end", "global") from _call_process_hooks_28
    $ restore_music()
    $ monicaLastCleaningCompletedDay = day
    $ add_cleaning(True)
    if get_cleaning_status(3) == True and monicaHouseCleaningBettyAffection == True:
        if char_info["Betty"]["level"] < 3:
            $ add_char_progress("Betty", bettyCleaningProgessAmount, "cleaning_day_" + str(day))
        else:
            if char_info["Betty"]["level"] < 4:
                $ add_char_progress("Betty", bettyCleaningProgessAmountLevel3, "cleaning_day_" + str(day))

    $ miniMapEnabledOnly = []

    call refresh_scene_fade() from _call_refresh_scene_fade_42
    return

label house_cleaning_clean_object:
    $ cleanSound = "cleaning" + str(renpy.random.randint(1, 3))
    sound cleanSound

    $ monicaCleaningObject = obj_name #ведем Монику к очищенному объекту
    $ set_active(obj_name, False)
    if get_active_objects(cleaning_group=True) != False:
        # еще есть объекты для чистки
#        call refresh_scene_fade()
        call refresh_scene("Dissolve_fast") from _call_refresh_scene_6
        return False

    if houseCleaningShortEnd == True:
        jump house_cleaning_room_finished_short
    $ autorun_to_object("house_cleaning_room_finished")
    call refresh_scene("Dissolve_fast") from _call_refresh_scene_7
    return False

label house_cleaning_room_finished:
    $ monicaCleaningObject = ""
    if scene_name == "bedroom1":
        mt "Здесь все, теперь другую сторону."
        call change_scene(rooms_dirty.pop(0)) from _call_change_scene_174
        return False
    else:
        mt "Кажется все."
        if len(rooms_dirty) > 0:
            $ monicaCleaningObject = ""
            $ autorun_to_object("house_cleaning_room_finished2")
            call refresh_scene("Dissolve_fast") from _call_refresh_scene_8
            return False

label house_cleaning_room_finished_short:
    if spotCleaning == True:
        call house_cleaning_spot() from _call_house_cleaning_spot
        return False
    call house_cleaning_end() from _call_house_cleaning_end
    return False

label house_cleaning_room_finished2:
    call start_cleaning_dialogue2() from _call_start_cleaning_dialogue2
#    w
    call change_scene(rooms_dirty.pop(0)) from _call_change_scene_175
    return False

label processHouseCleaningEvening:
    if monicaLastCleaningCompletedDay < day:
        $ add_cleaning(False)
        if monicaHouseCleaningBettyAffection == True:
            if char_info["Betty"]["level"] < 3:
                $ add_char_progress("Betty", bettyCleaningProgessRegressAmount, "cleaning_day_" + str(day))

    return

label house_cleaning_spot:
    call process_hooks("monica_cleaning_spot_start", "global") from _call_process_hooks_50
    $ set_active(False, group="environment", scene="House", recursive=True)
    $ monicaCleaningInProgress = False
    $ set_active("Spot", True, scene="floor2")
    if monicaUnder == "Nude":
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_Cleaning_Spot_Nude_Evening", "img_overlay":"Floor2_Monica_Cleaning_Spot_Nude_Evening_Overlay", "click" : "house_cleaning_spot_click", "actions" : "l", "zorder":11, "tint": monica_tint}, scene="floor2")
    else:
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_Cleaning_Spot_Evening", "img_overlay":"Floor2_Monica_Cleaning_Spot_Evening_Overlay", "click" : "house_cleaning_spot_click", "actions" : "l", "zorder":11, "tint": monica_tint}, {"monicaBettyPanties": {"v":True, "base" : "Floor2_Monica_Cleaning_Spot_Betty_[monicaBettyPantiesId]_Evening", "img_overlay":"Floor2_Monica_Cleaning_Spot_Evening_Overlay"}}, scene="floor2")
    $ add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Spot", "click" : "house_cleaning_spot_click", "actions" : "l", "zorder":10, "group":"environment"}, scene="floor2")
    $ add_hook("Spot", "house_cleaning_spot_click", scene="floor2")
    $ add_hook("Monica", "house_cleaning_spot_click", scene="floor2")
    $ autorun_to_object("ep22_dialogue2_7a", scene="floor2")
    call refresh_scene_fade() from _call_refresh_scene_fade_88
    call change_scene("floor2") from _call_change_scene_235
    return
label house_cleaning_spot_click:
#    $ monicaCleaningInProgress = True
    $ store_music()
    music stop
    menu:
        "Смотреть...":
            music snd_scrub_music
            call ep22_Act_Images_monica_cleaning_spot() from _call_ep22_Act_Images_monica_cleaning_spot
        "Пропустить.":
            pass
    $ restore_music()
    call house_cleaning_end() from _call_house_cleaning_end_1
    #Floor2_Monica_Cleaning_Spot_Evening_Overlay
    #Floor2_Monica_Cleaning_Spot_Evening
    #Floor2_Monica_Cleaning_Spot_Betty_1_Evening
    #monicaBettyPanties
    #monicaBettyPantiesId
    return False

label house_cleaning_spot_external_call:
    $ houseCleaningStoredScene = store_scene("floor2")
    python:
        objects = get_active_objects(scene="floor2", teleport=True)
        if objects != False:
            for obj1 in objects:
                add_hook(obj1[1], "cleaning_monica_goout1", scene=obj1[2])
    $ set_active(False, group="environment", scene="floor2")
    $ set_active("Spot", True, scene="floor2")
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor2_Monica_Cleaning_Spot_Evening", "img_overlay":"Floor2_Monica_Cleaning_Spot_Evening_Overlay", "click" : "house_cleaning_spot_click_external_call", "actions" : "l", "zorder":11, "tint": monica_tint}, {"monicaBettyPanties": {"v":True, "base" : "Floor2_Monica_Cleaning_Spot_Betty_[monicaBettyPantiesId]_Evening", "img_overlay":"Floor2_Monica_Cleaning_Spot_Evening_Overlay"}}, scene="floor2")
    $ add_object_to_scene("Spot", {"type" : 2, "base" : "Floor2_Spot", "click" : "house_cleaning_spot_click_external_call", "actions" : "l", "zorder":10, "group":"environment"}, scene="floor2")
    $ add_hook("Spot", "house_cleaning_spot_click_external_call", scene="floor2")
    $ add_hook("Monica", "house_cleaning_spot_click_external_call", scene="floor2")
    call refresh_scene_fade() from _call_refresh_scene_fade_89
    call change_scene("floor2") from _call_change_scene_236
    return

label house_cleaning_spot_click_external_call:
    $ store_music()
    music stop
    menu:
        "Смотреть...":
            music snd_scrub_music
            call ep22_Act_Images_monica_cleaning_spot() from _call_ep22_Act_Images_monica_cleaning_spot_1
        "Пропустить.":
            pass
    $ restore_music()
    $ restore_scene(houseCleaningStoredScene)
    call refresh_scene_fade() from _call_refresh_scene_fade_90
    return False

label start_cleaning_dialogue1a:
    mt "Сегодня пришла очередь убрать"
    python:
        for obj1 in rooms_dirty:
            if obj1 == "floor2":
                renpy.say(mt, t__("Верхний холл."))
            if obj1 == "floor1":
                renpy.say(mt, t__("Нижний холл."))
            if obj1 == "bedroom_bardie":
                renpy.say(mt, t__("Спальню Барди."))
            if obj1 == "bedroom_second":
                renpy.say(mt, t__("Спальню для гостей."))
            if obj1 == "living_room":
                renpy.say(mt, t__("Гостиную."))
            if obj1 == "bedroom1":
                renpy.say(mt, t__("Мою бывшую спальню."))

    $ rooms_dirty.pop(0)
    call start_cleaning_dialogue1() from _call_start_cleaning_dialogue1
#    if rooms_dirty[0] != scene_name:
#    else:
#        call refresh_scene()

    return
label start_cleaning_dialogue1:
    if scene_name == "bedroom1":
        mt "Моя бывшая спальня..."
        "Но ничего! Скоро она будет снова моя! Клянусь!"
        return
    mt "Начну уборку отсюда."
    if get_active_objects("Bardie") != False:
        mt "!!!"
        mt "Снова здесь этот Барди!"
        "Догадываюсь зачем..."
        "Ненавижу эту малявку!"
    return
label start_cleaning_dialogue1b:
    if scene_name == "bedroom1":
        mt "Моя бывшая спальня..."
        "Но ничего! Скоро она будет снова моя! Клянусь!"
        return
    if get_active_objects("Bardie") != False:
        mt "!!!"
        mt "Снова здесь этот Барди!"
        "Догадываюсь зачем..."
        "Ненавижу эту малявку!"
    return
label start_cleaning_dialogue2:
    $ next_room = rooms_dirty[0]
    if scene_name == "bedroom1" and next_room == "bedroom2":
        pass
    else:
        if scene_name == "floor2":
            mt "Я убрала верхний холл."
        if scene_name == "floor1":
            mt "Я убрала нижний холл."
        if scene_name == "bedroom_bardie":
            mt "Я убрала спальню Барди."
        if scene_name == "bedroom_second":
            mt "Я убрала спальню для гостей."
        if scene_name == "living_room":
            mt "Я убрала гостиную."
        if scene_name == "bedroom1":
            mt "Я убрала мою бывшую спальню."

        if next_room == "floor2":
            mt "Теперь надо убрать верхний холл."
        if next_room == "floor1":
            mt "Теперь надо убрать нижний холл."
        if next_room == "bedroom_bardie":
            mt "Теперь надо убрать спальню Барди."
        if next_room == "bedroom_second":
            mt "Теперь надо убрать спальню для гостей."
        if next_room == "living_room":
            mt "Теперь надо убрать гостиную."
        if next_room == "bedroom2" or next_room == "bedroom1":
            mt "Теперь надо убрать мою бывшую спальню."

    return
