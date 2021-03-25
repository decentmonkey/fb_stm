label street_fitness:

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
