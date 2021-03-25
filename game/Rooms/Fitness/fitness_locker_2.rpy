label fitness_locker_2:
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
    if obj_name == "Teleport_Locker":
        call EP22_Quests_Betty6() from _call_EP22_Quests_Betty6
        return
    return

label fitness_locker_2_environment:
    if obj_name == "Stephanie" or obj_name == "Rebecca" or obj_name == "Betty":
        call EP22_Quests_Betty7() from _call_EP22_Quests_Betty7
    return
