label street_dick_office:
    if EP1==True:
        jump street_dick_office_EP1
    $ print "enter_street_dick_office"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Dick_Office[day_suffix]"
    if day_time == "day":
        music street9
    else:
        music street_evening2
    return

label street_dick_office_init:
    if EP1==True:
        return
    $ add_object_to_scene("Building", {"type":2, "base":"Street_Dick_Office_Building", "click" : "street_dick_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Dick_Office_Building_Enter" + day_suffix, "click" : "street_dick_office_teleport", "actions" : "lw", "zorder" : 0, "b":0.2, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_dick_office_teleport:
    if EP1 == True:
        jump street_dick_office_teleport_EP1
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Вход в офисное здание где заседает Дик..."
            return
        if obj_data["action"] == "w":
#            mt "У меня нет галстука для Дика, что мне там делать... (хмык)"
#            return
            $ dickReceptionMonicaSuffix = 1
            call change_scene("dick_office_entrance") from _call_change_scene_162
            return
    return
label street_dick_office_environment:
    if EP1==True:
        jump street_dick_office_environment_EP1
    if obj_name == "Building":
        m "В этом офисном здании заседает Дик."
        "Оно такое же мрачное, как и его работа."
        "И такое же скучное, как он сам!"
    return


# EP1


default streetDickOfficeStage = 0
default dickOfficeUnlocked = False
default streetDickOfficeVisited = False
default dickWaitingMonica1 = True

default streetDickOfficeAutorunIdx = 0

label street_dick_office_EP1:

    $ print "enter_street_dick_office"
    $ miniMapData = []

    $ scene_name = "street_dick_office"
    $ sceneIsStreet = True
    $ scene_caption = t_("Dick's Office")
    $ clear_scene_from_objects(scene_name)

    if streetDickOfficeStage == 0:
        if bFredFollowingMonica == True:
            $ scene_image = "scene_Street_Dick_Office_Driver" + day_suffix
            $ add_object_to_scene("Driver", {"type":2, "base":"Street_Dick_Office_Driver", "click" : "street_dick_office_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
            $ add_object_to_scene("Car", {"type":2, "base":"Street_Dick_Office_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
            $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Dick_Office_Driver_Building_Enter" + day_suffix, "click" : "street_dick_office_teleport", "actions" : "lw", "zorder" : 0, "b":0.2})
            $ add_object_to_scene("Building", {"type":2, "base":"Street_Dick_Office_Building", "click" : "street_dick_office_environment", "actions" : "l", "zorder" : 0})
        else:
            $ scene_image = "scene_Street_Dick_Office" + day_suffix
            $ add_object_to_scene("Building", {"type":2, "base":"Street_Dick_Office_Building", "click" : "street_dick_office_environment", "actions" : "l", "zorder" : 0})
            $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Dick_Office_Building_Enter" + day_suffix, "click" : "street_dick_office_teleport", "actions" : "lw", "zorder" : 0, "b":0.2})

    if streetDickOfficeStage == 1:
        $ scene_image = "scene_Street_Dick_Office_Driver" + day_suffix
        $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Dick_Office_Building_Enter" + day_suffix, "click" : "street_dick_office_teleport", "actions" : "lw", "zorder" : 0, "b":0.2})
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Dick_Office_Driver", "click" : "street_dick_office_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Dick_Office_Car", "click" : "street_dick_office_environment", "actions" : "l", "zorder" : 3})
        $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Dick_Office_Driver_Building_Enter" + day_suffix, "click" : "street_dick_office_teleport", "actions" : "lw", "zorder" : 0, "b":0.2})
    if streetDickOfficeStage == 2:
        $ scene_image = "scene_Street_Dick_Office_Driver" + day_suffix


    if streetDickOfficeVisited == False:
        $ autorun_to_object("street_dick_office", "dick_meeting1")
    $ streetDickOfficeVisited = True

    if streetDickOfficeAutorunIdx == 1:
        $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue6")
    if streetDickOfficeAutorunIdx == 2:
        $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue9")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_dick_office_teleport_EP1:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Вход в офисное здание где заседает Дик..."
            if dickWaitingMonica1 == True:
                call dick_waiting_monica_dialogue1() from _call_dick_waiting_monica_dialogue1
        if obj_data["action"] == "w":
            if streetDickOfficeStage == 1:
                mt "У меня нет галстука для Дика, что мне там делать... (хмык)"
                return
            if dickOfficeUnlocked != True:
                m "Что мне там делать?
                Пусть Дик сам ко мне ходит!"
                if dickWaitingMonica1 == True:
                    call dick_waiting_monica_dialogue1() from _call_dick_waiting_monica_dialogue1_1
                return
            call change_scene("dick_office_entrance") from _call_change_scene_90
            return
    return
label street_dick_office_environment_EP1:
    if obj_name == "Building":
        m "В этом офисном здании заседает Дик."
        "Оно такое же мрачное, как и его работа."
        "И такое же скучное, как он сам!"
        if dickWaitingMonica1 == True:
            call dick_waiting_monica_dialogue1() from _call_dick_waiting_monica_dialogue1_2
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            if streetDickOfficeStage == 1:
                mt "Фред!!!"
                "ФРЕД!!!"
                return
            call monica_looking_to_fred1() from _call_monica_looking_to_fred1_3
            if dickWaitingMonica1 == True:
                call dick_waiting_monica_dialogue1() from _call_dick_waiting_monica_dialogue1_3
            return
        if obj_data["action"] == "t":
            if streetDickOfficeStage == 1:
                call afterJailFredDialogue2() from _call_afterJailFredDialogue2
                return
            call get_to_drive_dialogue() from _call_get_to_drive_dialogue_5
            return
    if obj_name == "Car":
        if streetDickOfficeStage == 1:
            mt "Моя машина... Как я соскучилась по ней!!!"
        return
    return
