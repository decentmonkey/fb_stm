#default hostelBedroomStage = 0
default hostelBedroomMonicaSuffix = 1
default hostelBedroomWhore1Suffix = 1
label hostel_bedroom:
    $ print "enter_hostel_bedroom"
    $ miniMapData = []

    $ scene_image = "scene_Hostel_Bedroom"

    call ep214_slums_hostel_bedroom_life() from _rcall_ep214_slums_hostel_bedroom_life

    music snd_moderate_rain_music
    return

label hostel_bedroom_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Bedroom_Monica_[cloth]_[hostelBedroomMonicaSuffix]", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 10}, scene="hostel_bedroom")
    $ add_object_to_scene("Whore1", {"type":2, "base":"Hostel_Bedroom_Whore1_[hostelBedroomWhore1Suffix]", "click" : "hostel_bedroom_environment", "actions" : "lw", "zorder" : 9}, scene="hostel_bedroom")

    $ add_object_to_scene("HostelBed", {"type":2, "base":"Hostel_Bedroom_Bed", "click" : "hostel_bedroom_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_bedroom")

    $ add_object_to_scene("Vase1", {"type":2, "base":"Hostel_Bedroom_Vase1", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_bedroom")
    $ add_object_to_scene("Vase2", {"type":2, "base":"Hostel_Bedroom_Vase2", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_bedroom")
    $ add_object_to_scene("Vase3", {"type":2, "base":"Hostel_Bedroom_Vase3", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_bedroom")
    $ add_object_to_scene("Window", {"type":2, "base":"Hostel_Bedroom_Window", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_bedroom")

    $ add_object_to_scene("Teleport_Hostel_Bathroom", {"type":3, "text" : _("ДУШ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_bedroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover":True}, scene="hostel_bedroom")
    $ add_object_to_scene("Teleport_Hostel_Reception", {"type":3, "text" : _("РЕЦЕПШИН"), "rarrow" : "arrow_right_2", "base":"Hostel_Bedroom_Teleport_Hostel_Reception", "click" : "hostel_bedroom_teleport", "xpos" : 1692, "ypos" : 755, "zorder":15}, scene="hostel_bedroom")


    $ hostelReceptionVisited = True
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_bedroom_teleport():
    if obj_name == "Teleport_Hostel_Reception":
        call change_scene("hostel_reception", "Fade") from _rcall_change_scene_159
        return
    if obj_name == "Teleport_Hostel_Bathroom":
        call change_scene("hostel_bathroom", "Fade") from _rcall_change_scene_160
        return

    return
label hostel_bedroom_environment():
    if obj_name == "Monica":
        mt "ГОСПОДИ! ЧТО ЭТО???"
        "И ЭТО НАЗЫВАЕТСЯ ОТЕЛЬ?!?!?"
        "Ну... пусть не отель, а хостел, но!"
        "Это какое-то место для бездомных!!!"

    if obj_name == "Whore1":
        if act == "l":
            mt "Я смотрю эта шлюха все так и спит."
            "Бесполезное создание..."
            return
        if act == "w":
            mt "Я не собираюсь подходить к этой шлюхе!"
            return

    if obj_name == "Vase1" or obj_name == "Vase2" or obj_name == "Vase3":
        mt "Это что? Какая-то ваза?"
        "Похоже в нее набросаны окурки..."
    if obj_name == "Window":
        mt "Это окно такое грязное и мутное, что оно даже не пропускает свет с улицы..."

    return
