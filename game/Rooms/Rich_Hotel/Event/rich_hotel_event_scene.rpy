label rich_hotel_event_scene:
    $ print "rich_hotel_event_scene"
    $ miniMapData = []

    $ scene_image = "scene_rich_hotel_event_scene_melanie_biff_monica_photodress"
    hide screen Reporters_Shoots_Screen2
    hide screen Reporters_Shoots_Screen
    hide screen Reporters_Shoots_Screen3
    show screen Reporters_Shoots_Screen
    show screen Reporters_Shoots_Screen3
    music Master_Disorder
    return

label rich_hotel_event_scene_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "rich_hotel_event_scene_Monica_[cloth]", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Biff", {"type" : 2, "base" : "rich_hotel_event_scene_biff", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":9, "icon_t":"/Icons/talk" + res.suffix +".png"})
    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "rich_hotel_event_scene_Melanie", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Cloth", {"type" : 2, "base" : "rich_hotel_event_scene_Cloth", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Door", {"type" : 2, "base" : "rich_hotel_event_scene_Door", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Flower1", {"type" : 2, "base" : "rich_hotel_event_scene_Flower1", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Flower2", {"type" : 2, "base" : "rich_hotel_event_scene_Flower2", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Lamp", {"type" : 2, "base" : "rich_hotel_event_scene_Lamp", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("PosterMelanie", {"type" : 2, "base" : "rich_hotel_event_scene_PosterMelanie", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People1", {"type" : 2, "base" : "rich_hotel_event_scene_People1", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People2", {"type" : 2, "base" : "rich_hotel_event_scene_People2", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People3", {"type" : 2, "base" : "rich_hotel_event_scene_People3", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People4", {"type" : 2, "base" : "rich_hotel_event_scene_People4", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People5", {"type" : 2, "base" : "rich_hotel_event_scene_People5", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People6", {"type" : 2, "base" : "rich_hotel_event_scene_People6", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People7", {"type" : 2, "base" : "rich_hotel_event_scene_People7", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("People8", {"type" : 2, "base" : "rich_hotel_event_scene_People8", "click" : "rich_hotel_event_scene_environment", "actions" : "l", "zorder":0})

#    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3], "group":"environment"})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_event_scene_teleport:
    return
label rich_hotel_event_scene_environment:
    if obj_name == "Monica":
        return
    if obj_name == "Biff":
        hide screen Reporters_Shoots_Screen
        show screen Reporters_Shoots_Screen2
        img 6697
        biff "Ну, давай кукла!"
        "Притворись Моникой Бакфетт!"
        img 6698
        "Или тебя надо шлепнуть по попке, чтобы ты заговорила?!"
        call refresh_scene_fade() from _call_refresh_scene_fade_12
        return
    if obj_name == "Melanie":
        hide screen Reporters_Shoots_Screen
        show screen Reporters_Shoots_Screen2
        img 6699
        with fade
        mt "Мелани смотрит на меня."
        "Интересно что она думает обо всем этом..."
        call refresh_scene_fade() from _call_refresh_scene_fade_13
        return

    if obj_name == "People1" or obj_name == "People2" or obj_name == "People3" or obj_name == "People4" or obj_name == "People5" or obj_name == "People6" or obj_name == "People7" or obj_name == "People8":
        mt "Эти люди..."
        "Здесь столько людей... Они все смотрят на меня..."
        "Ждут..."
        "Что же мне делать???"
        "Сказать им правду?"
        return
    if obj_name == "Cloth":
        mt "Эта одежда закрывает собой мой постер!"
        return
    if obj_name == "Door":
        mt "Эта дверь... Может быть мне просто убежать?"
        "Но нет, это не выход из положения..."
        return
    if obj_name == "Flower1" or obj_name == "Flower2":
        mt "Это место так украшено цветами..."
        return
    if obj_name == "Lamp":
        mt "Милый светильник."
        "Приятный свет."
        return
    if obj_name == "PosterMelanie":
        hide screen Reporters_Shoots_Screen
        show screen Reporters_Shoots_Screen2
        img 6680
        mt "Мелани?! Здесь?!"
        "А почему не Я?!"
        call refresh_scene_fade() from _call_refresh_scene_fade_14
        return

    return
