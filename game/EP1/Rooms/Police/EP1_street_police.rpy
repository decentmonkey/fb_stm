default streetPoliceMonicaFredTalkFlag = False

label EP1_street_police:
    $ print "enter_street_police"
    $ miniMapData = []

    $ scene_name = "street_police"
    $ scene_caption = t_("Police Station")
    $ clear_scene_from_objects(scene_name)
    if bFredFollowingMonica == True and map_scene == "Police":
        $ scene_image = "scene_street_Police_Driver_Monica_" + cloth + day_suffix
        $ EP1_add_object_to_scene("Driver", {"type":2, "base":"Street_Police_Driver", "click" : "EP1_street_police_environment", "actions" : "lt", "zorder" : 0, "icon_t":"/Icons/talk" + res.suffix +".png" , "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ EP1_add_object_to_scene("Car", {"type":2, "base":"Street_Police_Car", "click" : "EP1_street_house_main_yard_environment", "actions" : "l", "zorder" : 0, "b":0.1, "tint":[1.0, 1.0, 0.9]})
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Street_Police_Driver_Monica_" + cloth + day_suffix, "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 10})
    else:
        $ scene_image = "scene_street_Police_Monica_" + cloth + day_suffix
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Street_Police_Monica_" + cloth + day_suffix, "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 10})

    $ EP1_add_object_to_scene("Bench1", {"type":2, "base":"Street_Police_Bench1", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Bench2", {"type":2, "base":"Street_Police_Bench2", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Building", {"type":2, "base":"Street_Police_Building", "click" : "EP1_street_police_environment", "actions" : "lw", "zorder" : 0})
    $ EP1_add_object_to_scene("Poster", {"type":2, "base":"Street_Police_Poster", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 1})
    $ EP1_add_object_to_scene("Car1", {"type":2, "base":"Street_Police_Car1", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Car2", {"type":2, "base":"Street_Police_Car2", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Car3", {"type":2, "base":"Street_Police_Car3", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Car4", {"type":2, "base":"Street_Police_Car4", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Car5", {"type":2, "base":"Street_Police_Car5", "click" : "EP1_street_police_environment", "actions" : "l", "zorder" : 0})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_street_police_teleport(obj_name, obj_data):
    return
label EP1_street_police_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Какие старое мерзкое здание, Фи!"
        "Если я зайду туда, то только на пару минут!"
    if obj_name == "Building":
        if obj_data["action"] == "l":
            mt "Какие старое мерзкое здание, Фи!"
            "Если я зайду туда, то только на пару минут!"
        if obj_data["action"] == "w":
            if streetPoliceMonicaFredTalkFlag == False:
                $ streetPoliceMonicaFredTalkFlag = True
                call EP1_phone_dialogue_police_walk1_fred_talk()
            call EP1_change_scene("police_entrance")
            return
            sound highheels_short_walk
            stop music fadeout 4.0
            scene black_screen
            with Dissolve(1)
#            call EP1_textonblack_long("The End of V0.3\nYou could support me on Patreon if you like the game :)") from _call_textonblack_long_3
            scene black_screen
            with Dissolve(1)
            $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
            return
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call EP1_monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            $ streetPoliceMonicaFredTalkFlag = True
            call EP1_phone_dialogue_police_walk1_fred_talk()
            return

    if obj_name == "Bench1" or obj_name == "Bench2":
        m "На этой скамейке пыль!"
        "Да и мне некогда сидеть здесь!"
    if obj_name == "Car1" or obj_name == "Car2" or obj_name == "Car3" or obj_name == "Car4" or obj_name == "Car5":
        m "Полицейская машина."
        "Такая якобы грозная..."
        "И такая смешная, ха-ха!"
        "Я вас не боюсь! Пугайте кого-нибудь попроще!"
    if obj_name == "Poster":
        mt "Что здесь написано?..."
        mt "TO PROTECT AND SERVE THE RICH"
        "JAIL THE HOMELESS"
        "Отлично сказано!"
        "Полностью согласна!"
        "Если пересажать всех бездомных, станет меньше переходов."
        "Мне будет удобнее ездить."
        "Почему-бы нет?"

    return
