default fitness_locker_1_stephanie_rebecca_suffix = 1

label fitness_locker_1:
    if EP1==True:
        jump fitness_locker_1_EP1
    $ print "enter_fitness_locker_1"
    $ miniMapData = []

    $ scene_name = "fitness_locker_1"

#    if fitnessStephanieRebeccaInLocker == True:
#        $ scene_image = "scene_fitness_locker_1_Stephanie_Rebecca"
#        $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_1_Stephanie", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
#        $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_1_Rebecca", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
#    else:

    $ scene_image = "scene_fitness_locker_1"
    return
label fitness_locker_1_init:
    if EP1==True:
        return
    $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_1_Stephanie_[fitness_locker_1_stephanie_rebecca_suffix]", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12}, scene="fitness_locker_1")
    $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_1_Rebecca_[fitness_locker_1_stephanie_rebecca_suffix]", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12}, scene="fitness_locker_1")
    $ add_object_to_scene("Betty", {"type":2, "base":"fitness_locker_1_Betty", "click" : "fitness_locker_1_environment", "actions" : "ltw", "zorder" : 12, "active":False}, scene="fitness_locker_1")

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

label fitness_locker_1_teleport:
    if EP1==True:
        jump fitness_locker_1_teleport_EP1
    if obj_name == "Teleport_Gym":
        call change_scene("fitness_gym") from _call_change_scene_165
        return
    if obj_name == "Teleport_Lockers":
        call change_scene("fitness_locker_2") from _call_change_scene_166
        return

    return
label fitness_locker_1_environment:
    if EP1==True:
        jump fitness_locker_1_environment_EP1
    if obj_name == "Benches":
        mt "Скамейки в раздевалке.
        Не знаю, может быть на них что-то и удобно делать, но точно не переодеваться!"
    if obj_name == "Stephanie":
        if obj_data["action"] == "l":
            call ep22_dialogues4_5() from _call_ep22_dialogues4_5
            return
        if obj_data["action"] == "w":
            if questHelpFlag11 == False:
                $ questHelpFlag11 = True
                $ questHelp("fitness_1", True)
                $ questHelp("fitness_1a")
#                $ questHelp("house_11")
                $ questHelpDesc("house_desc3", "house_desc7")
                $ questHelpDesc("fitness_desc1")
            call EP22_Quests_Betty5b() from _call_EP22_Quests_Betty5b
            return
    if obj_name == "Rebecca":
        if obj_data["action"] == "l":
            call ep22_dialogues4_5() from _call_ep22_dialogues4_5_1
            return
        if obj_data["action"] == "w":
            if questHelpFlag11 == False:
                $ questHelpFlag11 = True
                $ questHelp("fitness_1", True)
                $ questHelp("fitness_1a")
#                $ questHelp("house_11")
                $ questHelpDesc("house_desc3", "house_desc7")
                $ questHelpDesc("fitness_desc1")
            call EP22_Quests_Betty5b() from _call_EP22_Quests_Betty5b_1
            return
    if obj_name == "Betty":
        if act == "l":
            call bettyInteract1() from _call_bettyInteract1
            return
        if act == "t":
            call ep22_dialogues4_2() from _call_ep22_dialogues4_2
        if act == "w":
            if questHelpFlag11 == False:
                $ questHelpFlag11 = True
                $ questHelp("fitness_1", True)
                $ questHelp("fitness_1a")
#                $ questHelp("house_11")
                $ questHelpDesc("house_desc3", "house_desc7")
                $ questHelpDesc("fitness_desc1")
            call EP22_Quests_Betty5b() from _call_EP22_Quests_Betty5b_2
            return


#    if obj_name == "Lockers":
#        if obj_data["action"] == "l":
#            mt "Шкафчики для переодевания.
#            Один из них мой."
#        if obj_data["action"] == "w":
#            call change_scene("fitness_locker_2") from _call_change_scene_169
#            return
    return





# EP1




label fitness_locker_1_EP1:
    $ print "enter_fitness_locker_1"
    $ miniMapData = []

    $ scene_name = "fitness_locker_1"
    $ scene_caption = t_("Fitness Gym")
    $ clear_scene_from_objects(scene_name)
    if fitnessStephanieRebeccaInLocker == True:
        $ scene_image = "scene_fitness_locker_1_Stephanie_Rebecca"
        $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_1_Stephanie", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
        $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_1_Rebecca", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
    else:
        $ scene_image = "scene_fitness_locker_1"


#    $ add_object_to_scene("Lockers", {"type":2, "base":"fitness_locker_1_Lockers", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Benches", {"type":2, "base":"fitness_locker_1_Benches", "click" : "fitness_locker_1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Lockers", {"type":3, "text" : t_("ШКАФЧИКИ ДЛЯ ПЕРЕОДЕВАНИЯ"), "larrow" : "arrow_down_2", "base":"fitness_locker_1_Lockers", "click" : "fitness_locker_1_teleport", "xpos" : 1492, "ypos" : 311, "zorder":11})
    $ add_object_to_scene("Teleport_Gym", {"type":3, "text" : t_("НАЗАД В ЗАЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "fitness_locker_1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    if driveTriggers.has_key("stephanie_return_event") == True and driveTriggers["stephanie_return_event"] == "on":
        call stephanie_fitness_return_scene() from _call_stephanie_fitness_return_scene
        call refresh_scene_fade() from _call_refresh_scene_fade_81
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_locker_1_teleport_EP1:
    if obj_name == "Teleport_Gym":
        call change_scene("fitness_gym") from _call_change_scene_165
        return
    if obj_name == "Teleport_Lockers":
        call change_scene("fitness_locker_2") from _call_change_scene_166
        return

    return
label fitness_locker_1_environment_EP1:
    if obj_name == "Benches":
        mt "Скамейки в раздевалке.
        Не знаю, может быть на них что-то и удобно делать, но точно не переодеваться!"
    if obj_name == "Stephanie":
        if obj_data["action"] == "l":
            mt "Это Стефани.
            Моя подружка."
            "У нее очень богатые и влиятельные родители.
            Потому я резрешаю ей дружить со мной."
            "Но она слишком помешана на мужчинах, как я считаю."
        if obj_data["action"] == "w":
            call change_scene("fitness_locker_2") from _call_change_scene_167
            return
    if obj_name == "Rebecca":
        if obj_data["action"] == "l":
            mt "Это Ребекка.
            Они слишком любит деньги и тех кто ими обладает.
            Но она часто льстит мне, потому я держу ее рядом со мной."
        if obj_data["action"] == "w":
            call change_scene("fitness_locker_2") from _call_change_scene_168
            return
    if obj_name == "Lockers":
        if obj_data["action"] == "l":
            mt "Шкафчики для переодевания.
            Один из них мой."
        if obj_data["action"] == "w":
            call change_scene("fitness_locker_2") from _call_change_scene_169
            return
    return
