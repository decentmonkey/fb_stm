default jailFoodLastScene = ""
default jailFoodInteractlabel EP1_= ""
label EP1_police_jail_food_scene:
    $ print "enter_police_jail_food_scene"
    $ miniMapData = []

    if scene_name != "police_jail_food_scene":
        $ jailFoodLastScene = scene_name
    $ scene_name = "police_jail_food_scene"
    $ scene_caption = t_("JAIL")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Police_Cell_Food"
    $ EP1_add_object_to_scene("Food", {"type":2, "base": "Police_Cell_Food", "click" : "EP1_police_jail_food_scene_environment", "actions" : "lh", "zorder" : 1})

    $ cageInteractCnt = cageInteractAmount
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_police_jail_food_scene_teleport(obj_name, obj_data):
    return
label EP1_police_jail_food_scene_environment(obj_name, obj_data):
    if obj_name == "Food":
        if act == "l":
            mt "БОЖЕ! НУ И МЕРЗОСТЬ!!!"
        if act == "h":
            mt "Моника! Заставь себя! Иначе ты умрешь с голода!!!"
            sound snd_eating
            stop music fadeout 1.0
            sound snd_eating
            call EP1_textonblack(t_("Спустя 5 минут..."))
            img black_screen
            with Dissolve(1)
            call EP1_change_scene(jailFoodLastScene, "Fade", False)
            call expression jailFoodInteractlabel 
            return

    return
