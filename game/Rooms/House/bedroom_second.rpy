label bedroom_second:
    $ print "enter_bedroom_second"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_10

    $ scene_image = "scene_House_BedroomSecond[day_suffix]"
    music houseMusic
    return

label bedroom_second_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "House_BedroomSecond_Monica_[cloth][day_suffix]", "click" : "bedroom_second_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, {"monicaCleaningInProgress":{"v":True, "base":"House_BedroomSecond_Monica_[cloth]_Cleaning_[monicaCleaningObject]"}})

    $ add_object_to_scene("Bardie", {"type" : 2, "active":False, "base" : "House_BedroomSecond_Bardie[day_suffix]", "click" : "bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "active":False}, {"monicaCleaningInProgress":{"v":True, "base":"House_BedroomSecond_Bardie_Cleaning"}})

    $ add_object_to_scene("BedroomSecondBed", {"type":2, "base":"House_BedroomSecond_Bed", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_BedroomSecond_BedroomSecondBed_Dust"}})
    $ add_object_to_scene("LampTable", {"type":2, "base":"House_BedroomSecond_LampTable", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("LegChair", {"type":2, "base":"House_BedroomSecond_LegChair", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_BedroomSecond_LegChair_Dust"}})
    $ add_object_to_scene("MirrorTable", {"type":2, "base":"House_BedroomSecond_MirrorTable", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("TV", {"type":2, "base":"House_BedroomSecond_TV", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_BedroomSecond_TV_Dust"}})
    $ add_object_to_scene("Window1", {"type":2, "base":"House_BedroomSecond_Window1", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Window2", {"type":2, "base":"House_BedroomSecond_Window2", "click" : "bedroom_second_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"House_BedroomSecond_Teleport_Floor2", "click" : "bedroom_second_teleport", "xpos" : 960, "ypos" : 956, "zorder":20, "teleport":True, "high_sprite_hover":True})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label bedroom_second_teleport:
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_94
        return
    return

label bedroom_second_environment:
    if obj_name == "Monica":
        mt "СУЧКА!!!"
        "ГРЕБАНАЯ БЕТТИ!!!"
        "ОНА ЗАПРЕТИЛА МНЕ СПАТЬ ЗДЕСЬ!!!"
        return
    if obj_name == "BedroomSecondBed":
        mt "СУЧКА!!!"
        "ГРЕБАНАЯ БЕТТИ!!!"
        "ОНА ЗАПРЕТИЛА МНЕ СПАТЬ ЗДЕСЬ!!!"
        return
    if obj_name == "LampTable":
        mt "Милый столик.. Но мне здесь нельзя спать!"
        return
    if obj_name == "LegChair":
        mt "Я бы сложила сюда свои длинные ножки, если бы..."
        "ЕСЛИ БЫ ЭТА БЕТТИ СДОХЛА, СВОЛОЧЬ!!!"
        return
    if obj_name == "MirrorTable":
        mt "Похоже это зеркало тоже не для меня..."
        return
    if obj_name == "TV":
        mt "Похоже этот телевизор тоже не для меня..."
        return
    if obj_name == "Window1" or obj_name == "Window2":
        mt "Мне без разницы какой здесь вид, мне здесь спать нельзя..."
        return
    return
