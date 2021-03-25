default driverOnHouseYard = True
default houseStreetFenceLocationOpened = False
default neighborAsked = False
default driverMode = 0

default streetHouseMainYardStage = 0

label EP1_street_house_main_yard:
    $ print "enter_street_house_main_yard"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "street_house_main_yard"
    $ sceneIsStreet = True
    $ scene_caption = t_("House Yard")
    $ clear_scene_from_objects(scene_name)

    if streetHouseMainYardStage == 0:
        $ scene_image = "scene_Street_House_Monica_" + cloth + day_suffix
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Monica_" + cloth + day_suffix, "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        if driverOnHouseYard == True:
            $ EP1_add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
            $ EP1_add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver" + day_suffix, "click" : "EP1_street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})
        else:
            $ EP1_add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})

        $ EP1_add_object_to_scene("Teleport_House", {"type":3, "text" : t_("В ДОМ"), "rarrow" : "arrow_up_2", "base":"Street_House_Teleport_House", "click" : "EP1_street_house_main_yard_teleport", "xpos" : 1683, "ypos" : 858, "zorder":11, "b":-0.05, "tint":[1.0, 1.0, 0.85]})

    if streetHouseMainYardStage == 1:
        $ scene_image = "scene_Street_House_Driver_Family_Monica_Whore"
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Driver_Family_Monica_Whore_Monica", "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        $ EP1_add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
        $ EP1_add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver_Family_Monica_Whore_Driver", "click" : "EP1_street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ EP1_add_object_to_scene("Family", {"type" : 2, "base" : "Street_House_Driver_Family_Monica_Whore_Family", "click" : "EP1_street_house_main_yard_environment", "actions" : "lw", "zorder":10, "tint": monica_tint})

    if streetHouseMainYardStage == 2:
        $ scene_image = "scene_Street_House_Monica_" + cloth + day_suffix
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Monica_" + cloth + day_suffix, "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        $ EP1_add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
        $ EP1_add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver" + day_suffix, "click" : "EP1_street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ EP1_add_object_to_scene("Teleport_House", {"type":3, "text" : t_("В ДОМ"), "rarrow" : "arrow_up_2", "base":"Street_House_Teleport_House", "click" : "EP1_street_house_main_yard_teleport", "xpos" : 1683, "ypos" : 858, "zorder":11, "b":-0.05, "tint":[1.0, 1.0, 0.85]})

    if bardieLocation == "Street_Yard":
        $ EP1_add_object_to_scene("Bardie", {"type" : 2, "base" : "Street_House_Bardie" + day_suffix, "click" : "EP1_bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})


    if houseStreetFenceLocationOpened == True:
        $ EP1_add_object_to_scene("Teleport_Fence", {"type":3, "text" : t_("К ЗАБОРУ"), "larrow" : "arrow_left_2", "base":"Street_House_Teleport_Fence", "click" : "EP1_street_house_main_yard_teleport", "xpos" : 758, "ypos" : 154, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.9]})

    $ EP1_add_object_to_scene("Teleport_Gate", {"type":3, "text" : t_("К ВОРОТАМ"), "larrow" : "arrow_left_2", "base":"Street_House_Teleport_Gate", "click" : "EP1_street_house_main_yard_teleport", "xpos" : 433, "ypos" : 660, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.85]})


    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_street_house_main_yard_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Fence":
        call EP1_change_scene("street_house_fence", "Fade", "highheels_run2")
        return
    if obj_name == "Teleport_Gate":
        call EP1_change_scene("street_house_gate", "Fade", "highheels_run2")
        return
    if obj_name == "Teleport_House":
        music casualMusic
        call EP1_change_scene("floor1", "Fade_long", "highheels_run2")
        return
    return
label EP1_street_house_main_yard_environment(obj_name, obj_data):
    if obj_name == "Car":
        if gameStage > 2:
            mt "Моя бывшая машина..."
            "Но я верну все назад, клянусь!"
            "Я устроим им всем АД!!!"
            return
        call EP1_look_at_car(0)
        return
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            if gameStage > 2:
                mt "Фред... Мой бывший водитель..."
                "Редкий ублюдок..."
                "Он не избежит своей участи!"
                return
            call EP1_monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            if streetHouseMainYardStage == 2:
                call EP1_afterJailHouseFamily_dialogue2a()
                return
            if streetHouseMainYardStage == 1:
                call EP1_afterJailHouseFamily_dialogue2()
                return
            if driverMode == 1:
                call EP1_monica_fred_day1_evening_dialogue2()
                return
            if driverMode == 2:
                call EP1_monica_fred_day2_morning_dialogue1()
                return
            if neighborAsked == False:
                $ neighborAsked = True
                call EP1_neighbor_quest1()
                $ scene_transition = "Fade_long"
                music casualMusic
                call EP1_refresh_scene()
                return
            else:
                call EP1_get_to_drive_dialogue()
                return
    if obj_name == "Monica":
        if streetHouseMainYardStage == 1 or streetHouseMainYardStage == 2:
            mt "(хмык)"
            return
        m "Мой уютный дворик."
        "За домом есть бассейн, где я люблю расслабляться.
        Но сейчас нет на это времени."
        if day_time == "evening":
            m "Но сейчас уже слишком темно."

    if obj_name == "Family":
        if act == "l":
            if streetHouseMainYardStage == 1:
                mt "Мне надо подойти к ним..."
                "Мне надо где-то ночевать!!!"
        if act == "w":
            if streetHouseMainYardStage == 1:
                call EP1_afterJailHouseFamily_dialogue3()
                return
    return

















#
