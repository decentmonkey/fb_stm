label street_gas_station:
    $ print "enter_street_gas_station"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_Gas_Station[day_suffix]"
    if day_time == "day":
        music street8
    else:
        music street_evening4


    $ set_active("Fuel1", False)
    $ set_active("Fuel2", False)
    $ set_active("Logo", False)
    $ set_active("Station_Building", False)
#    $ set_active("Teleport_Inside", False)
    return

label street_gas_station_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Gas_Station_Monica_[cloth][day_suffix]", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 15})

    $ add_object_to_scene("Fuel1", {"type":2, "base":"Street_Gas_Station_Fuel1", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0, "type":"environment"})
    $ add_object_to_scene("Fuel2", {"type":2, "base":"Street_Gas_Station_Fuel2", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0, "type":"environment"})
    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Gas_Station_Logo", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0, "type":"environment"})
    $ add_object_to_scene("Station_Building", {"type":2, "base":"Street_Gas_Station_Station_Building", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0, "type":"environment"})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"street_gas_station_teleport_Inside", "click" : "street_gas_station2_teleport", "actions" : "lw", "zorder" : 1, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_gas_station2_teleport:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Вход в здание заправки..."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view1") from _call_change_scene_61
            return
    return
label street_gas_station2_environment:
    if obj_name == "Monica":
        mt "Это та самая заправка..."
        return

    if obj_name == "Fuel1" or obj_name == "Fuel2":
        mt "Пистолеты для заправки бензина."
        "Мне они сейчас ни к чему!"
    if obj_name == "Logo":
        mt "Модная запрака?"
    if obj_name == "Station_Building":
        mt "Здание заправки.
        Здесь должен быть где-то вход..."
    return
