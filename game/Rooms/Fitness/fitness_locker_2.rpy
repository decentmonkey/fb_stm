label fitness_locker_2:
    if EP1==True:
        jump fitness_locker_2_EP1
    $ print "enter_fitness_locker_2"
    $ miniMapData = []

    $ scene_name = "fitness_locker_2"

#    if fitnessStephanieRebeccaInLocker == True:
#        $ scene_image = "scene_fitness_locker_1_Stephanie_Rebecca"
#        $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_1_Stephanie", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
#        $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_1_Rebecca", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
#    else:

    $ scene_image = "scene_fitness_locker_2"

label fitness_locker_2_init:
    if EP1==True:
        return
    $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_2_Stephanie", "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12}, scene="fitness_locker_2")
    $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_2_Rebecca", "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12}, scene="fitness_locker_2")
    $ add_object_to_scene("Betty", {"type":2, "base":"fitness_locker_2_Betty", "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12}, scene="fitness_locker_2")
    $ add_object_to_scene("Teleport_Locker", {"type":3, "text" : t_("ЖДАТЬ В РАЗДЕВАЛКЕ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "fitness_locker_2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11}, scene="fitness_locker_2")

#    $ add_object_to_scene("Lockers", {"type":2, "base":"fitness_locker_1_Lockers", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 0})
#    $ add_object_to_scene("Benches", {"type":2, "base":"fitness_locker_1_Benches", "click" : "fitness_locker_1_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Teleport_Lockers", {"type":3, "text" : t_("ШКАФЧИКИ ДЛЯ ПЕРЕОДЕВАНИЯ"), "larrow" : "arrow_down_2", "base":"fitness_locker_1_Lockers", "click" : "fitness_locker_1_teleport", "xpos" : 1492, "ypos" : 311, "zorder":11})
#    $ add_object_to_scene("Teleport_Gym", {"type":3, "text" : t_("НАЗАД В ЗАЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "fitness_locker_1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
#    if driveTriggers.has_key("stephanie_return_event") == True and driveTriggers["stephanie_return_event"] == "on":
#        call stephanie_fitness_return_scene() from _call_stephanie_fitness_return_scene
#        call refresh_scene_fade() from _call_refresh_scene_fade_41
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_locker_2_teleport:
    if EP1==True:
        jump fitness_locker_2_teleport_EP1
    if obj_name == "Teleport_Locker":
        call EP22_Quests_Betty6() from _call_EP22_Quests_Betty6
        return
    return

label fitness_locker_2_environment:
    if EP1==True:
        jump fitness_locker_2_environment_EP1
    if obj_name == "Stephanie" or obj_name == "Rebecca" or obj_name == "Betty":
        call EP22_Quests_Betty7() from _call_EP22_Quests_Betty7
    return





# EP1




label fitness_locker_2_EP1:
    $ print "enter_fitness_locker_2"
    $ miniMapData = []

    $ scene_name = "fitness_locker_2"
    $ scene_caption = t_("Fitness Gym")
    $ clear_scene_from_objects(scene_name)
    if fitnessStephanieRebeccaInLocker == True:
        if fitnessStephanieRebeccaTalked == False:
            $ scene_image = "scene_fitness_locker_2_Stephanie_Rebecca_Monica_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Stephanie_Rebecca_Monica_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
        else:
            $ scene_image = "scene_fitness_locker_2_Stephanie_Rebecca_Monica2_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Stephanie_Rebecca_Monica2_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
        $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_2_Stephanie", "click" : "fitness_locker_2_environment", "actions" : "lt", "zorder" : 12})
        $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_2_Rebecca", "click" : "fitness_locker_2_environment", "actions" : "lt", "zorder" : 12})

    else:
        if cloth_type == "BusinessCloth":
            $ scene_image = "scene_fitness_locker_2_Monica_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Monica_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
        if cloth == "FitnessSuit":
            if fitnessMonicaTrained == False:
                $ scene_image = "scene_fitness_locker_2_Monica_" + cloth
                $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Monica_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
            else:
                $ scene_image = "scene_fitness_locker_2_Monica2_" + cloth
                $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Monica2_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})




    $ add_object_to_scene("Monica_Locker", {"type":2, "base":"fitness_locker_2_Monica_Locker", "click" : "fitness_locker_2_environment", "actions" : "lh", "zorder" : 0})
    $ add_object_to_scene("Benches", {"type":2, "base":"fitness_locker_2_Benches", "click" : "fitness_locker_1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Gym", {"type":3, "text" : t_("НАЗАД В ЗАЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "fitness_locker_2_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_locker_2_teleport_EP1:
    if obj_name == "Teleport_Gym":
        call change_scene("fitness_gym") from _call_change_scene_160
        return

    return
label fitness_locker_2_environment_EP1:
    if obj_name == "Stephanie":
        if obj_data["action"] == "l":
            mt "Это Стефани.
            Моя подружка."
            "У нее очень богатые и влиятельные родители.
            Потому я резрешаю ей дружить со мной."
            "Но она слишком помешана на мужчинах, как я считаю."
        if obj_data["action"] == "t":
            if fitnessStephanieRebeccaTalked == False:
                call fitness1_stephanie_rebecca_talk1() from _call_fitness1_stephanie_rebecca_talk1
                return
            call fitness1_stephanie_talk2() from _call_fitness1_stephanie_talk2
            return
    if obj_name == "Rebecca":
        if obj_data["action"] == "l":
            mt "Это Ребекка.
            Они слишком любит деньги и тех кто ими обладает.
            Но она часто льстит мне, потому я держу ее рядом со мной."
        if obj_data["action"] == "t":
            if fitnessStephanieRebeccaTalked == False:
                call fitness1_stephanie_rebecca_talk1() from _call_fitness1_stephanie_rebecca_talk1_1
                return
            call fitness1_rebecca_talk2() from _call_fitness1_rebecca_talk2
            return
    if obj_name == "Monica":
        if fitnessStephanieRebeccaTalked == False:
            mt "А вот и мои подружки!"
            return
        if fitnessMonicaTrained == False and cloth_type == "BusinessCloth":
            mt "Мне надо переодеться в мою спортивную форму."
            return
        if fitnessMonicaTrained == False and cloth_type == "FitnessSuit":
            mt "В нем так удобно!!"

        if fitnessMonicaTrained == True and cloth_type != "BusinessCloth":
            mt "Я позанималась."
            "Обожаю это состояние легкости в теле."
            "Мне надо почаще приходить сюда..."
            "А теперь надо переодеться."
            return
        if fitnessMonicaTrained == True and cloth_type == "BusinessCloth":
            mt "Я позанималась."
            "Обожаю это состояние легкости в теле."
            "Мне надо почаще приходить сюда..."
            "А теперь надо ехать в Банк."
            "У меня подозрения насчет Стива..."

    if obj_name == "Monica_Locker":
        if obj_data["action"] == "l":
            mt "Мой шкафчик.
            Здесь я могу переодеться."
        if obj_data["action"] == "h":
            if fitnessStephanieRebeccaTalked == False:
                call fitness1_stephanie_rebecca_talk1() from _call_fitness1_stephanie_rebecca_talk1_2
                return
            if fitnessStephanieRebeccaInLocker == True:
                menu:
                    "Переодеться...":
                        call fitness1_change_cloth1() from _call_fitness1_change_cloth1
                        return
                    "Отойти.":
                        return
            if fitnessMonicaTrained == True and cloth_type == "FitnessSuit":
                menu:
                    "Переодеться...":
                        call fitness1_change_cloth2() from _call_fitness1_change_cloth2
                        return
                    "Отойти.":
                        return
            if fitnessMonicaTrained == True and cloth_type == "BusinessCloth":
                mt "Мне не к чему переодеваться, пора ехать по делам!"
                return

#                    $ add_objective("change_cloth_to_fitness", t_("Переодеться в раздевалке"), c_green, 20)


    return
