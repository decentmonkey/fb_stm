default bedroomSecondStage = 0

label EP1_bedroom_second:
    $ print "enter_bedroom_second"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "bedroom_second"
    $ scene_caption = "GUEST'S BEDROOM"
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_House_BedroomSecond" + day_suffix

    $ monica_tint = [1.0, 1.0, 1.0]

    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "House_BedroomSecond_Monica_" + cloth + day_suffix, "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ EP1_add_object_to_scene("BedroomSecondBed", {"type":2, "base":"House_BedroomSecond_Bed", "click" : "EP1_bedroom_second_environment", "actions" : "lh", "zorder" : 0})
    $ EP1_add_object_to_scene("LampTable", {"type":2, "base":"House_BedroomSecond_LampTable", "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("LegChair", {"type":2, "base":"House_BedroomSecond_LegChair", "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("MirrorTable", {"type":2, "base":"House_BedroomSecond_MirrorTable", "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("TV", {"type":2, "base":"House_BedroomSecond_TV", "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Window1", {"type":2, "base":"House_BedroomSecond_Window1", "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Window2", {"type":2, "base":"House_BedroomSecond_Window2", "click" : "EP1_bedroom_second_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"House_BedroomSecond_Teleport_Floor2", "click" : "EP1_bedroom_second_teleport", "xpos" : 960, "ypos" : 956, "zorder":20})
    return

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_bedroom_second_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor2":
        call EP1_change_scene("floor2")
        return
    return

label EP1_bedroom_second_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if bedroomSecondStage == 1:
            mt "СУЧКА!!!"
            "ГРЕБАНАЯ БЕТТИ!!!"
            "ОНА ЗАПРЕТИЛА МНЕ СПАТЬ ЗДЕСЬ!!!"
            return
        mt "Ах, как я мечтаю скорее заснуть на этой кроватке!"
        return
    if obj_name == "BedroomSecondBed":
        if bedroomSecondStage == 1:
            mt "СУЧКА!!!"
            "ГРЕБАНАЯ БЕТТИ!!!"
            "ОНА ЗАПРЕТИЛА МНЕ СПАТЬ ЗДЕСЬ!!!"
            return
        if act == "l":
            mt "Ах, как я мечтаю скорее заснуть на этой кроватке!"
        if act == "h":
            call EP1_afterJailHouse_dialogue8()
            return
    if obj_name == "LampTable":
        if bedroomSecondStage == 1:
            mt "Милый столик.. Но мне здесь нельзя спать!"
            return
        mt "Какой милый столик с лампой, я уже и забыла про него..."
    if obj_name == "LegChair":
        if bedroomSecondStage == 1:
            mt "Я бы сложила сюда свои длинные ножки, если бы..."
            "ЕСЛИ БЫ ЭТА БЕТТИ СДОХЛА, СВОЛОЧЬ!!!"
            return
        mt "Сюда я сложу свои длинные ножки... Ммммм..."
    if obj_name == "MirrorTable":
        if bedroomSecondStage == 1:
            mt "Похоже это зеркало тоже не для меня..."
            return
        mt "Как хорошо что гостевая спалься оборудована."
        "Здесь даже есть столик с зеркалом и косметикой!"
    if obj_name == "TV":
        if bedroomSecondStage == 1:
            mt "Похоже этот телевизор тоже не для меня..."
            return
        mt "Телевизор!"
        "Я смогу посмотреть что-то по нему, чтобы отвлечься от своих проблем."
    if obj_name == "Window1" or obj_name == "Window2":
        if bedroomSecondStage == 1:
            mt "Мне без разницы какой здесь вид, мне здесь спать нельзя..."
            return
        mt "Из этих окон замечательный вид!"
    return
