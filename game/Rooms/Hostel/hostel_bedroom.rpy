default hostelBedroomStage = 0
default hostelBedroomMonicaSuffix = 1
default hostelBedroomWhore1Suffix = 1
label hostel_bedroom:
    if EP1==True:
        jump hostel_bedroom_EP1
    $ print "enter_hostel_bedroom"
    $ miniMapData = []

    $ scene_image = "scene_Hostel_Bedroom"

    call ep214_slums_hostel_bedroom_life() from _rcall_ep214_slums_hostel_bedroom_life

    music snd_moderate_rain_music
    return

label hostel_bedroom_init:
    if EP1==True:
        return
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
    if EP1==True:
        jump hostel_bedroom_teleport_EP1
    if obj_name == "Teleport_Hostel_Reception":
        call change_scene("hostel_reception", "Fade") from _rcall_change_scene_159
        return
    if obj_name == "Teleport_Hostel_Bathroom":
        call change_scene("hostel_bathroom", "Fade") from _rcall_change_scene_160
        return

    return
label hostel_bedroom_environment():
    if EP1==True:
        jump hostel_bedroom_environment_EP1
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



# EP1


default hostelBedroomWhore1 = True
label hostel_bedroom_EP1:
    $ print "enter_hostel_bedroom"
    $ miniMapData = []

    $ scene_name = "hostel_bedroom"
    $ scene_caption = t_("HOSTEL BEDROOM")
    $ clear_scene_from_objects(scene_name)

    if hostelBedroomStage == 0 or hostelBedroomStage == 1:
        $ scene_image = "scene_Hostel_Bedroom_Monica_Nude"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Bedroom_Monica_Nude", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 10})
    if hostelBedroomStage == 2:
        $ scene_image = "scene_Hostel_Bedroom_Monica_Nude2"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Bedroom_Monica_Nude2", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Teleport_Hostel_Reception", {"type":3, "text" : t_("РЕЦЕПШИН"), "rarrow" : "arrow_right_2", "base":"Hostel_Bedroom_Teleport_Hostel_Reception", "click" : "hostel_bedroom_teleport", "xpos" : 1692, "ypos" : 755, "zorder":15})
        return


    if hostelBedroomWhore1 == True:
        if hostelBedroomStage == 0:
            $ add_object_to_scene("Whore1", {"type":2, "base":"Hostel_Bedroom_Whore1", "click" : "hostel_bedroom_environment", "actions" : "lw", "zorder" : 0, "b":0.13})
        if hostelBedroomStage == 1:
            $ add_object_to_scene("Whore1", {"type":2, "base":"Hostel_Bedroom_Whore1", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})

    if hostelBedroomStage == 0:
        $ add_object_to_scene("BedHostel", {"type":2, "base":"Hostel_Bedroom_Bed", "click" : "hostel_bedroom_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    if hostelBedroomStage == 1:
        $ add_object_to_scene("BedHostel", {"type":2, "base":"Hostel_Bedroom_Bed", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})

    $ add_object_to_scene("Vase1", {"type":2, "base":"Hostel_Bedroom_Vase1", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Vase2", {"type":2, "base":"Hostel_Bedroom_Vase2", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Vase3", {"type":2, "base":"Hostel_Bedroom_Vase3", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Window", {"type":2, "base":"Hostel_Bedroom_Window", "click" : "hostel_bedroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})

    $ add_object_to_scene("Teleport_Hostel_Bathroom", {"type":3, "text" : t_("ДУШ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_bedroom_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    $ add_object_to_scene("Teleport_Hostel_Reception", {"type":3, "text" : t_("РЕЦЕПШИН"), "rarrow" : "arrow_right_2", "base":"Hostel_Bedroom_Teleport_Hostel_Reception", "click" : "hostel_bedroom_teleport", "xpos" : 1692, "ypos" : 755, "zorder":15})


    $ hostelReceptionVisited = True
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_bedroom_teleport_EP1:
    if obj_name == "Teleport_Hostel_Reception":
        if hostelBedroomStage == 1:
            mt "Мне надо сначала принять душ!"
            return
        if hostelBedroomStage == 2:
            call hostelAfterJail_bedroom_dialogue5() from _call_hostelAfterJail_bedroom_dialogue5 #убегает
            return
        music Groove2_85
        call change_scene("hostel_reception", "Fade", "snd_walk_barefoot") from _call_change_scene_154
        return
    if obj_name == "Teleport_Hostel_Bathroom":
        if hostelBedroomStage == 0:
            music snd_moderate_rain_music2
        call change_scene("hostel_bathroom", "Fade", "snd_walk_barefoot") from _call_change_scene_155
        return

    return
label hostel_bedroom_environment_EP1:
    if obj_name == "Monica":
        if hostelBedroomStage == 1:
            mt "Жуткая ночь!"
            "У меня болит все тело от этой... кровати.."
            "Но ничего! Все почти закончилось!"
            return
        if hostelBedroomStage == 2:
            sound snd_woman_scream1
            mt "АААААААААААААААА!!!!"
            return

        mt "ГОСПОДИ! ЧТО ЭТО???"
        "И ЭТО НАЗЫВАЕТСЯ ОТЕЛЬ?!?!?"
        "Ну... пусть не отель, а хостел, но!"
        "Это какое-то место для бездомных!!!"
    if obj_name == "Whore1":
        if hostelBedroomStage == 1:
            mt "Я смотрю эта шлюха все так и спит."
            "Бесполезное создание..."
            return
        if act == "l":
            mt "Кто это там лежит?"
            "Это похоже та посетительница, о которой говорила Перри..."
            "Мне отсюда плохо видно."
        if act == "w":
            call change_scene("hostel_bedroom2", "Fade", "snd_walk_barefoot") from _call_change_scene_156
            return

    if obj_name == "BedHostel":
        if hostelBedroomStage == 1:
            mt "Я ни за что больше не буду спать ни на чем подобном!"
            return

        if act == "l":
            img 5630
            with fade
            mt "Это место где мне придется спать???"
            "Оно ничуть не лучше, чем в тюрьме!"
            "И за это я должна $10???"
            "Вернее $10.000!!!"
            "..."
            "Моника, забудь..."
            "Этот кошмар скоро закончится..."
        if act == "h":
            if hostelBathTaken == False:
                mt "Мне надо принять душ."
                "Хоть это и дыра, но здесь есть настоящий душ!"
                return
            call hostelAfterJail_bedroom_sleep1() from _call_hostelAfterJail_bedroom_sleep1
            return

    if obj_name == "Vase1" or obj_name == "Vase2" or obj_name == "Vase3":
        mt "Это что? Какая-то ваза?"
        "Похоже в нее набросаны окурки..."
    if obj_name == "Window":
        mt "Это окно такое грязное и мутное, что оно даже не пропускает свет с улицы..."

    return
