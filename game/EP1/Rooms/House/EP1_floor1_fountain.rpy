label EP1_floor1_fountain:
    $ print "enter_floor1_fountain"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "floor1_fountain"
    $ scene_caption = t_("Fountain")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Floor1_Fountain" + day_suffix

    $ EP1_add_object_to_scene("Fountain", {"type":2, "base":"Floor1_Fountain_Fountain", "click" : "EP1_floor1_fountain_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Curtains", {"type":2, "base":"Floor1_Fountain_Curtains", "click" : "EP1_floor1_environment", "actions" : "l", "zorder" : 0, "b":0.2})
    $ EP1_add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Fountain_Lamps", "click" : "EP1_floor1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Windows", {"type":2, "base":"Floor1_Fountain_Windows", "click" : "EP1_floor1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Picture", {"type":2, "base":"Floor1_Fountain_Picture", "click" : "EP1_floor1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Fountain_Furniture", "click" : "EP1_floor1_environment", "actions" : "l", "zorder" : 0})

    if gameStage >= 3:
        if bardieLocation == "Floor1":
            $ scene_image = "scene_Floor1_Fountain_Bardie" + day_suffix
            $ EP1_add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Fountain_Bardie" + day_suffix, "click" : "EP1_bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})


    $ EP1_add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_floor1_fountain_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

#    $ EP1_add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "EP1_floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_floor1_fountain_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor1":
        call EP1_change_scene("floor1")
        return

label EP1_floor1_fountain_environment(obj_name, obj_data):
    if obj_name == "Fountain":

        m "Люстра может упасть только в фонтан."

        "Но я же не полезу в него, верно?"
        if gameStage > 2:
            return

        "Так что я в безопасности.
        Можно не бояться этой люстры."

        "Вообще не представляю кому бы понадобилось в него залезать."

        "Может только этой бестолковой Юлии, чтобы что-то в нем почистить?"

        "Наверное Юлия бы не испугалась этого сделать.
        Потому что она просто глупая."

        "Глупость рождает бесстрашие."

        "Мне повезло что я умная!"
