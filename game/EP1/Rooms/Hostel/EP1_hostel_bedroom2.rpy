label EP1_hostel_bedroom2:
    $ print "enter_hostel_bedroom2"
    $ miniMapData = []

    $ scene_name = "hostel_bedroom2"
    $ scene_caption = t_("HOSTEL BEDROOM")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_hostel_bedroom2_Monica_Nude"
    $ EP1_add_object_to_scene("Monica", {"type":2, "base":"hostel_bedroom2_Monica_Nude", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 10})

    $ EP1_add_object_to_scene("BedHostel", {"type":2, "base":"Hostel_Bedroom2_Bed", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ EP1_add_object_to_scene("Blanket", {"type":2, "base":"Hostel_Bedroom2_Blanket", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ EP1_add_object_to_scene("Cloth", {"type":2, "base":"Hostel_Bedroom2_Cloth", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 2, "b":0.13})
    $ EP1_add_object_to_scene("Trash", {"type":2, "base":"Hostel_Bedroom2_Trash", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ EP1_add_object_to_scene("WhoreBody", {"type":2, "base":"Hostel_Bedroom2_WhoreBody", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 1, "b":0.13})
    $ EP1_add_object_to_scene("WhoreFeet", {"type":2, "base":"Hostel_Bedroom2_WhoreFeet", "click" : "EP1_hostel_bedroom2_environment", "actions" : "l", "zorder" : 0, "b":0.13})

    $ EP1_add_object_to_scene("Teleport_Hostel_Bedroom", {"type":3, "text" : t_("ДУШ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_hostel_bedroom2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})


    $ hostelReceptionVisited = True
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_hostel_bedroom2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Bedroom":
        call EP1_change_scene("hostel_bedroom", "Fade", "snd_walk_barefoot")
        return

    return
label EP1_hostel_bedroom2_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "О Боже! Что это за существо???"
        "Оно живое?"
    if obj_name == "BedHostel":
        mt "Эта ржавая грязная кровать выглядит ужасно."
        "Мне, похоже, придется спать на такой же..."
    if obj_name == "Blanket":
        mt "Это одеяло, похоже, никогда не стирали."
    if obj_name == "Trash":
        mt "Куча окурков..."
    if obj_name == "Cloth":
        img 5629
        with fadelong
        mt "Жуткие лохмотья самой дешевой шлюхи..."
        "Не представляю как надо опуститься до того чтобы посить такое, по своей воле!"
        call EP1_refresh_scene_fade()
        return
    if obj_name == "WhoreBody":
        img 5628
        with fadelong
        mt "Дешевая шлюха, Фу!"
        "Могла бы одевать белье, когда спит!"
        "Никому здесь не нужны ее прелести!"
        "И мне спать рядом с ЭТИМ?!?!"
        call EP1_refresh_scene_fade()
        return
    if obj_name == "WhoreFeet":
        img 5629
        with fadelong
        call EP1_bitch(-3, "hostel_monica_whorefeet_look")
        mt "Похоже она весь день ходит на каблуках, судя по ее мазолям."
        "Вернее не ходит, а стоит, я даже знаю где."
        "Надеюсь я вижу ее последний раз..."
        call EP1_refresh_scene_fade() 
        return

    return
