label street_fitness:
    if EP1==True:
        jump street_fitness_EP1
    $ print "enter_street_fitness"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Fitness_Street[day_suffix]"
    if day_time == "day":
        music street6
    else:
        music street_evening1
    return

label street_fitness_init:
    if EP1==True:
        return
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_[cloth][day_suffix]", "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Fitness_Teleport_Inside", "click" : "street_fitness_teleport2", "actions" : "lw", "zorder" : 1, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_fitness_teleport2:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            mt "Фитнес зал."
            "Я не хочу туда идти."
            "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"
            "Надо сначала решить мою небольшую проблему, а уже затем идти дальше заниматься своим телом!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Уже вечер. Фитнесс зал закрыт."
                return
            "Я не хочу туда идти."
            "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"
            "Надо сначала решить мою небольшую проблему, а уже затем идти дальше заниматься своим телом!"
    return
label street_fitness_environment2:
    if obj_name == "Monica":
        "Я не пойду туда в таком виде!"
        "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"

    return



# EP1





label street_fitness_EP1:

    $ print "enter_street_fitness"
    $ miniMapData = []

    $ scene_name = "street_fitness"
    $ sceneIsStreet = True
    $ scene_caption = t_("Fitness")
    $ clear_scene_from_objects(scene_name)

    if bFredFollowingMonica == True:
        $ scene_image = "scene_fitness_street_Driver_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Driver_Monica_" + cloth + day_suffix, "click" : "street_fitness_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Fitness_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Fitness_Driver", "click" : "street_cloth_shop_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    else:
        $ scene_image = "scene_fitness_street_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_" + cloth + day_suffix, "click" : "street_fitness_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Fitness_Teleport_Inside", "click" : "street_fitness_teleport", "actions" : "lw", "zorder" : 1})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_fitness_teleport:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Фитнес зал."
            "Не особо большой, но, по крайней мере, сюда не ходят разные нищеброды."
            "Которые любят пялиться на девушек, не имея при этом банковского счета..."
            "У меня свои правила здесь.
            Когда я занимаюсь, никто больше в зал не допущен!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Уже вечер. Фитнесс зал закрыт."
                return
            $ remove_objective("go_fitness")
            call change_scene("fitness_gym") from _call_change_scene_263
            return
            stop music fadeout 4.0
            scene black_screen
            with Dissolve(1)
            call textonblack_long("The End of V0.2\nTo be continued very soon...\nCheck for updates!") from _call_textonblack_long_4
            scene black_screen
            with Dissolve(1)
            $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))

    return
label street_fitness_environment:
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1() from _call_monica_looking_to_fred1_10
            return
        if obj_data["action"] == "t":
            call get_to_drive_dialogue() from _call_get_to_drive_dialogue_12
            return
    if obj_name == "Monica":
        m "Наконец-то я добралась до фитнеса!"

    return
