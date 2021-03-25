label ep23_quests_fred_cleaning_spot_init:
    if get_active_objects("Betty", scene="floor2") == False:
        # Бетти нет, приходит Фред
        $ add_object_to_scene("Driver", {"type":2, "base":"Floor2_Fred1", "click" : "ep23_quests_fred_cleaning_spot_fred_talk1", "actions" : "lt", "zorder" : 12, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"}, scene="floor2")
    return

label ep23_quests_fred_cleaning_spot_fred_talk1:
    if act == "l":
        mt "Фред... Мой бывший водитель..."
        "Редкий ублюдок..."
        "Он не избежит своей участи!"
        return
    if act == "t":
        call ep23_dialogues3_4() from _call_ep23_dialogues3_4
        $ set_active("Driver", False, scene="floor2")
        call refresh_scene_fade() from _call_refresh_scene_fade_64
        return
    return

label ep23_quests_fred_talking_street_yard:
    if act=="l":
        return
    call ep23_dialogues3_3() from _call_ep23_dialogues3_3
    call refresh_scene_fade() from _call_refresh_scene_fade_65
    return False


label ep23_quests_fred_betty_sex:
#    if monicaRestHouse != True:
#        return
    $ remove_hook()
    if bettyTouchedFredDick == False:
        return
    call ep23_dialogues3_5() from _call_ep23_dialogues3_5
    return
