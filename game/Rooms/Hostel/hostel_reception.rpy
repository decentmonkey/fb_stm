default hostelReceptionStage = 0
default hostelReceptionMonicaSuffix = 1
default hostelReceptionPerrySuffix = 1

label hostel_reception:
    $ print "enter_hostel_reception"
    $ miniMapData = []

    $ scene_image = "scene_Hostel_Reception"
    music Groove2_85
    return

label hostel_reception_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Monica_[cloth]_[hostelReceptionMonicaSuffix]", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10}, scene="hostel_reception")
    $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_[hostelReceptionPerrySuffix]", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10}, scene="hostel_reception")

    $ add_object_to_scene("Carpet", {"type":2, "base":"Hostel_Reception_Carpet", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0}, scene="hostel_reception")
    $ add_object_to_scene("Clock", {"type":2, "base":"Hostel_Reception_Clock", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Door", {"type":2, "base":"Hostel_Reception_Door", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.2}, scene="hostel_reception")
    $ add_object_to_scene("Picture", {"type":2, "base":"Hostel_Reception_Picture", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("TV", {"type":2, "base":"Hostel_Reception_TV", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_reception")

    $ add_object_to_scene("Box1", {"type":2, "base":"Hostel_Reception_Box1", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box2", {"type":2, "base":"Hostel_Reception_Box2", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box3", {"type":2, "base":"Hostel_Reception_Box3", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box4", {"type":2, "base":"Hostel_Reception_Box4", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box5", {"type":2, "base":"Hostel_Reception_Box5", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box6", {"type":2, "base":"Hostel_Reception_Box6", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box7", {"type":2, "base":"Hostel_Reception_Box7", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box8", {"type":2, "base":"Hostel_Reception_Box8", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box9", {"type":2, "base":"Hostel_Reception_Box9", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box10", {"type":2, "base":"Hostel_Reception_Box10", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box11", {"type":2, "base":"Hostel_Reception_Box11", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box13", {"type":2, "base":"Hostel_Reception_Box13", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box14", {"type":2, "base":"Hostel_Reception_Box14", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box15", {"type":2, "base":"Hostel_Reception_Box15", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box16", {"type":2, "base":"Hostel_Reception_Box16", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Box17", {"type":2, "base":"Hostel_Reception_Box17", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_reception")

    $ add_object_to_scene("Computer", {"type":2, "base":"Hostel_Reception_Computer", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_reception")
    $ add_object_to_scene("Papers", {"type":2, "base":"Hostel_Reception_Papers", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_reception")

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_reception_teleport", "xpos" : 960, "ypos" : 956, "zorder":11}, scene="hostel_reception")

    $ add_object_to_scene("Teleport_Hostel_Bedroom", {"type":3, "text" : _("ОБЩАЯ СПАЛЬНЯ"), "rarrow" : "arrow_right_2", "base":"Hostel_Reception_Teleport_Bedroom", "click" : "hostel_reception_teleport", "xpos" : 1500, "ypos" : 200, "zorder":15}, scene="hostel_reception")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_reception_teleport():
    if obj_name == "Teleport_Hostel_Street":
        call change_scene("hostel_street", "Fade", "snd_jail_door") from _rcall_change_scene_161
        return
    if obj_name == "Teleport_Hostel_Bedroom":
        call change_scene("hostel_bedroom", "Fade") from _rcall_change_scene_162
        return
    return
label hostel_reception_environment():
    if obj_name == "Monica":
        mt "Ужасное место!"

    if obj_name == "Fence":
        mt "Железный забор..."
        "Нет, я преодолею все заборы в моей жизни!!!"
        "Я не сдамся!!!"

    if obj_name == "Carpet":
        mt "Что за грязный ковер здесь?"
        "Фу!!!"
    if obj_name == "Clock":
        mt "Эти грязные часы, похоже, показывают правильно время только дважды раз в день..."
    if obj_name == "Door":
        mt "Что это там за дверь?"
        "Не похоже что это дверь ведет в спальни."
        "Там еще какие-то помещения?"

    if obj_name == "Picture":
        mt "Дешевая копия..."
    if obj_name == "Computer" or obj_name == "Papers":
        mt "Компьютеры, бумаги..."
        "Неужели в этой дыре есть бухгалтерский учет?"

    if obj_name == "TV":
        mt "Здесь есть работающий телевизор?"
        "Ах да, он не работает, все в порядке..."
    if obj_name == "Box1" or obj_name == "Box2" or obj_name == "Box3" or obj_name == "Box4" or obj_name == "Box5" or obj_name == "Box6" or obj_name == "Box7" or obj_name == "Box8" or obj_name == "Box9" or obj_name == "Box10" or obj_name == "Box11" or obj_name == "Box12":
        if act == "l":
            mt "Какая-то коробка..."
            perry "Эй! Не трогай мои коробки!"
    if obj_name == "Box13" or obj_name == "Box14" or obj_name == "Box15" or obj_name == "Box16":
        if act == "l":
            mt "Какая-то коробка..."
        if act == "h":
            perry "Эй! Не трогай мои коробки!"
    if obj_name == "Box17":
        if act == "l":
            mt "Какая-то коробка..."
            perry "Эй! Не трогай мои коробки!"

    return
