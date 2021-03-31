#default hostelBathroomStage = 0
default hostelBathroomMonicaSuffix = 1
label hostel_bathroom:
    $ print "enter_hostel_bathroom"
    $ miniMapData = []

    $ scene_image = "scene_Hostel_Bathroom[day_suffix]"

    music snd_moderate_rain_music2

    if day_time == "evening":
        $ add_object_to_scene("Bottle", {"type":2, "base":"Hostel_Bathroom_Bottle", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_bathroom")
        $ add_object_to_scene("Shower", {"type":2, "base":"Hostel_Bathroom_Shower", "click" : "hostel_bathroom_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="hostel_bathroom")
        $ add_object_to_scene("Toilet", {"type":2, "base":"Hostel_Bathroom_Toilet_Object", "click" : "hostel_bathroom_environment", "actions" : "lw", "zorder" : 0, "b":0.13}, scene="hostel_bathroom")
        $ add_object_to_scene("Window", {"type":2, "base":"Hostel_Bathroom_Window", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0, "b":0.13}, scene="hostel_bathroom")
    else:
        $ add_object_to_scene("Bottle", {"type":2, "base":"Hostel_Bathroom_Bottle", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0}, scene="hostel_bathroom")
        $ add_object_to_scene("Shower", {"type":2, "base":"Hostel_Bathroom_Shower", "click" : "hostel_bathroom_environment", "actions" : "lh", "zorder" : 0}, scene="hostel_bathroom")
        $ add_object_to_scene("Toilet", {"type":2, "base":"Hostel_Bathroom_Toilet_Object", "click" : "hostel_bathroom_environment", "actions" : "lw", "zorder" : 0}, scene="hostel_bathroom")
        $ add_object_to_scene("Window", {"type":2, "base":"Hostel_Bathroom_Window", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0}, scene="hostel_bathroom")
    return

label hostel_bathroom_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Bathroom_Monica_[cloth]_[hostelBathroomMonicaSuffix][day_suffix]", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 10}, scene="hostel_bathroom")

    $ add_object_to_scene("Teleport_Hostel_Bedroom", {"type":3, "text" : _("ОБЩАЯ СПАЛЬНЯ"), "rarrow" : "arrow_right_2", "base":"Hostel_Bathroom_Teleport_Hostel_Bedroom", "click" : "hostel_bathroom_teleport", "xpos" : 520, "ypos" : 240, "zorder":0}, scene="hostel_bathroom")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_bathroom_teleport():
    if obj_name == "Teleport_Hostel_Bedroom":
        call change_scene("hostel_bedroom", "Fade") from _rcall_change_scene_156
        return

    return
label hostel_bathroom_environment():
    if obj_name == "Monica":
        mt "Какое жуткое место!"
        mt "Мне надо быть внимательнее."
        mt "В прошлый раз я еле успела убежать отсюда..."
        return

    if obj_name == "Bottle":
        mt "Какая-то пустая емкость."

    if obj_name == "Window":
        mt "Здесь такие открытые окна..."
        "Надеюсь меня не будет видно с улицы?"

    if obj_name == "Toilet":
        if act == "l":
            mt "Жуткий унитаз."
        if act == "w":
            call change_scene("hostel_bathroom_toilet", "Fade") from _rcall_change_scene_157
            return

    if obj_name == "Shower":
        if act == "l":
            mt "А вот и душ."
    return
