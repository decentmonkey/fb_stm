label EP1_street_monica_office:
    $ print "enter_street_monica_office"
    $ miniMapData = []

    $ scene_name = "street_monica_office"
    $ sceneIsStreet = True
    $ scene_caption = t_("Monica's Office Outside")
    $ clear_scene_from_objects(scene_name)
    if bFredFollowingMonica == True:
        $ scene_image = "scene_Street_Monica_Office_Driver" + day_suffix
        $ EP1_add_object_to_scene("Driver", {"type":2, "base":"Street_Monica_Office_Driver", "click" : "EP1_street_monica_office_environment", "actions" : "lt", "zorder" : 2, "icon_t":"/Icons/talk" + res.suffix +".png" , "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.7]})
        $ EP1_add_object_to_scene("Car", {"type":2, "base":"Street_Monica_Office_Car", "click" : "EP1_street_monica_office_environment", "actions" : "l", "zorder" : 1, "b":0.2, "tint":[1.0, 1.0, 0.7]})
        $ EP1_add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Monica_Office_Driver_Teleport_Inside", "click" : "EP1_street_monica_office_teleport", "actions" : "lw", "zorder" : 0})
    else:
        $ scene_image = "scene_Street_Monica_Office" + day_suffix
        $ EP1_add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Monica_Office_Teleport_Inside", "click" : "EP1_street_monica_office_teleport", "actions" : "lw", "zorder" : 0})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_street_monica_office_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Это здание принадлежит моей компании.
            Вернее компании мужа, но уже частично."
            "Уже несколько этажей принадлежат лично мне."
            "И я собираюсь продолжить этот процесс."
            "Я считаю что лучше могу управлять всем этим!"
        if obj_data["action"] == "w":
            call EP1_change_scene("monica_office_entrance", "Fade_long", "highheels_run2")
            return
    return
label EP1_street_monica_office_environment(obj_name, obj_data):
    if obj_name == "Car":
        call EP1_look_at_car(0)
        return
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call EP1_monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            if monicaOfficeDay2PhoneLost == True:
                imgl Dial_Monica_BusinessCloth2_Angry1
                m "Фрэд!"
                "Ты не видел мой телефон?"

                imgr Driver_Stand
                fred "Мэм, я видел как Вы выходили с ним!"
                m "Ясно, буду искать!"
                return
            call EP1_get_to_drive_dialogue()
            return


    return
