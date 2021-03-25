label EP1_bedroom_bardie:
    $ print "enter_bedroom_bardie"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "bedroom_bardie"
    $ scene_caption = "BARDIE'S ROOM"
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_House_BedroomBardie" + day_suffix

    $ monica_tint = [1.0, 1.0, 1.0]

    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "House_BedroomBardie_Monica_" + cloth + day_suffix, "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    if bardieLocation == "BedroomBardie":
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "House_BedroomBardie_Bardie_Monica_" + cloth + day_suffix, "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        $ EP1_add_object_to_scene("Bardie", {"type" : 2, "base" : "House_BedroomBardie_Bardie" + day_suffix, "click" : "EP1_bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ EP1_add_object_to_scene("Ball1", {"type":2, "base":"House_BedroomBardie_Ball1", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Ball2", {"type":2, "base":"House_BedroomBardie_Ball2", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("BardieBed", {"type":2, "base":"House_BedroomBardie_Bed", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair", {"type":2, "base":"House_BedroomBardie_Chair", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("MusicCenter", {"type":2, "base":"House_BedroomBardie_MusicCenter", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Subwoofer", {"type":2, "base":"House_BedroomBardie_Subwoofer", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture1", {"type":2, "base":"House_BedroomBardie_Picture1", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Trash1", {"type":2, "base":"House_BedroomBardie_Trash1", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Notebook", {"type":2, "base":"House_BedroomBardie_Notebook", "click" : "EP1_bedroom_bardie_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_bedroom_bardie_teleport", "xpos" : 960, "ypos" : 956, "zorder":20})
    return

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_bedroom_bardie_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor2":
        call EP1_change_scene("floor2")
        return
    return

label EP1_bedroom_bardie_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Раньше здесь была моя гардеробная."
        "Они переделали мою гардеробную под комнату этого оболтуса!!!"
        return

    if obj_name == "Ball1" or obj_name == "Ball2":
        mt "Этот оболтус разбрасывает вещи где попало!"
    if obj_name == "BardieBed":
        mt "Я сейчас мечтаю даже о такой дурацкой кровати!"
    if obj_name == "Chair":
        mt "Стул Барди..."
        "Хорошо бы он свалился с него!!!"
    if obj_name == "MusicCenter" or obj_name == "Subwoofer":
        mt "Я выкину эти его музыкальные штуки, когда верну себе мой дом!"
    if obj_name == "Picture1":
        mt "Дурацкие детские постеры!"
    if obj_name == "Trash1":
        mt "В этой комнате куча хлама!"
        "Этот оболтус не убирает за собой!"
    if obj_name == "Notebook":
        mt "Компьютер этого оболтуса."
        "Интересно, что он там смотрит?"
        menu:
            "Посмотреть на компьютер.":
                pass
            "Уйти...":
                return
        if bardieLocation == "BedroomBardie":
            #render+
            #ноутбук Барди крупным планом и Барди
            img 5802
            with fade
            pass
        else:
            #render+
            #ноутбук Барди крупным планом без Барди
            img 5803
            with fade
            pass
        mt "Фу! Какая мерзость!"
    return
