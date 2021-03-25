default street_house_outside_monica_suffix = 1
default street_house_outside_monica_suffix_str = ""
default street_house_outside_betty_suffix = 1

label street_house_outside:
    if EP1==True:
        jump street_house_outside_EP1
    $ print "enter_street_house_outside"
    $ miniMapData = []
    if miniMapTurnedOff2 == False:
        call miniMapHouseGenerate() from _call_miniMapHouseGenerate_20

    $ sceneIsStreet = True
    $ scene_image = "scene_Street_House_Outside[day_suffix]"

    $ street_house_outside_monica_suffix_str = ""
    if cloth == "CasualDress1" or cloth == "SchoolOutfit1":
        $ street_house_outside_monica_suffix_str = "_" + str(street_house_outside_monica_suffix)

    music night_ambience
    return

label street_house_outside_init:
    if EP1==True:
        return
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Outside_Monica_[cloth][day_suffix]", "click" : "street_house_outside_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, {"cloth":{"v":"CasualDress1", "base":"Street_House_Outside_Monica_[cloth]_[street_house_outside_monica_suffix][day_suffix]"}, "cloth":{"v":"SchoolOutfit1", "base":"Street_House_Outside_Monica_[cloth]_[street_house_outside_monica_suffix][day_suffix]"}})

    $ add_object_to_scene("Teleport_House_Outside_Outside", {"type":3, "text" : t_("ИДТИ ПО ДОРОГЕ"), "rarrow" : "arrow_down_2", "base":"Street_House_Outside_Teleport_Outside", "click" : "street_house_outside_teleport", "xpos" : 200, "ypos" : 790, "zorder":11, "teleport":True, "house_out_teleport":True})
    $ add_object_to_scene("Teleport_House_Gate", {"type":3, "text" : t_("НАЗАД К ВОРОТАМ"), "larrow" : "arrow_left_2", "base":"Street_House_Outside_Teleport_Gate", "click" : "street_house_outside_teleport", "xpos" : 1531, "ypos" : 605, "zorder":9, "b":0.2, "tint":[1.0, 1.0, 0.7], "teleport":True})
    return

label street_house_outside_init2:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Outside_Monica_[cloth][street_house_outside_monica_suffix_str][day_suffix]", "click" : "street_house_outside_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="street_house_outside")
    return

label street_house_outside_init3:
    $ add_object_to_scene("Teleport_House_Outside_Neighbour", {"type":3, "text" : t_("ДОМ СОСЕДА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "street_house_outside_teleport", "xpos" : 300, "ypos" : 790, "zorder":11, "teleport":True}, scene="street_house_outside")
    $ add_object_to_scene("Betty", {"type" : 2, "base" : "Street_House_Outside_Betty_[street_house_outside_betty_suffix][day_suffix]", "click" : "street_house_outside_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="street_house_outside")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_outside_teleport:
    if EP1==True:
        jump street_house_outside_teleport_EP1
    if obj_name == "Teleport_House_Gate":
        call change_scene("street_house_gate") from _call_change_scene_149
        return
    if obj_name == "Teleport_House_Outside_Outside":
        call map_show() from _call_map_show_1
        return
    return
label street_house_outside_environment:
    if EP1==True:
        jump street_house_outside_environment_EP1
    if obj_name == "Monica":
        mt "Я помню как стучалась в эти ворота недавно..."
        "Это все какой-то кошмар!"
        "Скоро это все должно закончиться!"
        return
    return




# EP1


label street_house_outside_EP1:
    $ print "enter_street_house_outside"
    $ miniMapData = []
    if miniMapTurnedOff == False:
        call miniMapHouseGenerate() from _call_miniMapHouseGenerate_18

    $ scene_name = "street_house_outside"
    $ sceneIsStreet = True
    $ scene_caption = t_("House Outside")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Street_House_Outside_Monica_" + cloth + day_suffix

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Outside_Monica_" + cloth + day_suffix, "click" : "street_house_outside_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Teleport_House_Outside_Outside", {"type":3, "text" : t_("ИДТИ ПО ДОРОГЕ"), "rarrow" : "arrow_down_2", "base":"Street_House_Outside_Teleport_Outside", "click" : "street_house_outside_teleport", "xpos" : 200, "ypos" : 790, "zorder":11})
    $ add_object_to_scene("Teleport_House_Gate", {"type":3, "text" : t_("НАЗАД К ВОРОТАМ"), "larrow" : "arrow_left_2", "base":"Street_House_Outside_Teleport_Gate", "click" : "street_house_outside_teleport", "xpos" : 1531, "ypos" : 605, "zorder":9, "b":0.2, "tint":[1.0, 1.0, 0.7]})
    if gameStage == 2:
        $ add_object_to_scene("Teleport_House_Gate", {"type":3, "text" : t_("ВОРОТА"), "larrow" : "arrow_left_2", "base":"Street_House_Outside_Teleport_Gate", "click" : "street_house_outside_teleport", "xpos" : 1531, "ypos" : 605, "zorder":9, "b":0.2, "tint":[1.0, 1.0, 0.7]})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_outside_teleport_EP1:
    if obj_name == "Teleport_House_Gate":
        if gameStage == 2 or (gameStage == 3 and gameSubStage < 2):
            call after_jail_house_outside() from _call_after_jail_house_outside
            return
        call change_scene("street_house_gate") from _call_change_scene_52
        return
    if obj_name == "Teleport_House_Outside_Outside":
        call map_show() from _call_map_show_1
        return
    return
label street_house_outside_environment_EP1:
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Я помню как стучалась в эти ворота недавно..."
            "Это все какой-то кошмар!"
            "Скоро это все должно закончиться!"
            return
        if gameStage == 2 or gameStage == 3:
            mt "Мой дом!"
            "Я так хочу домой!!!"
            "(хмык)"
            "Я обязательно попаду туда и снова буду жить там! В своем доме!!!"
            "Клянусь!"
            return
        if day_time == "day":
            m "Снаружи дома довольно красиво, но я не понимаю что я здесь делаю?"
        if day_time == "evening":
            m "Здесь снаружи, ночью, я чувствую себя немного неуютно."
            "Если честно, мне даже немного страшно.
            Пожалуй, стоит идти назад к дому."
        return
    return
