default floor1BettySuffix = 1

label floor1:
    $ print "enter_floor1"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_13

    $ scene_image = "scene_Floor1[day_suffix]"

    music houseMusic
    return

label floor1_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor1_Monica_[cloth]", "click" : "floor1_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, {"monicaCleaningInProgress":{"v":True, "base":"Floor1_Monica_[cloth]_Cleaning_[monicaCleaningObject]"}})
    $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Bardie[day_suffix]", "click" : "bardieInteract1", "actions" : "lt", "zorder":12, "active":False, "icon_t":"/Icons/talk" + res.suffix +".png"}, {"monicaCleaningInProgress":{"v":True, "base":"Floor1_Bardie_Cleaning"}})
    $ add_object_to_scene("Ralph", {"type" : 2, "base" : "Floor1_Ralph[day_suffix]", "click" : "ralphInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "active":False})

    $ add_object_to_scene("Chandelier", {"type":2, "base":"Floor1_Chandelier", "click" : "floor1_environment", "actions" : "l", "zorder" : 1, "group":"environment"})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Floor1_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Floor1_Curtains_Dust"}})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Lamps", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type":2, "base":"Floor1_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Picture", {"type":2, "base":"Floor1_Picture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Floor1_Picture_Dust"}})
    $ add_object_to_scene("Fountain", {"type":2, "base":"Floor1_Fountain_Object", "click" : "floor1_environment", "actions" : "lw", "zorder" : 1, "b":0.03, "group":"environment", "teleport":True})

    $ add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Furniture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Floor1_Furniture_Dust"}})

    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("????????????????"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "floor1_teleport", "xpos" : 1594, "ypos" : 306, "zorder":9, "b":0.15, "tint":[1.0, 1.0, 0.9], "teleport":True})

    $ add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("????????????????"), "larrow" : "arrow_left_2", "base":"Floor1_Stairs_Object", "click" : "floor1_teleport", "xpos" : 367, "ypos" : 219, "zorder":9, "b":0.15, "tint":[1.0, 1.0, 0.9], "teleport":True})
    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("??????????"), "larrow" : "arrow_left_2", "base":"Floor1_Teleport_Kitchen", "click" : "floor1_teleport", "xpos" : 130, "ypos" : 758, "zorder":15, "b":0.2, "teleport":True, "high_sprite_hover":True})
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("???? ??????????"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover": True, "teleport":True})

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

    return


label floor1_teleport:
    if obj_name == "Teleport_Floor1_Stairs":
        call change_scene("floor1_stairs") from _call_change_scene_103
    if obj_name == "Teleport_Kitchen":
        call change_scene("kitchen") from _call_change_scene_104
    if obj_name == "Teleport_LivingRoom":
        call change_scene("living_room") from _call_change_scene_105
        return
    if obj_name == "Teleport_Street":
        jump house_out

    return


label floor1_environment:
    if obj_name == "Monica":
        m "?????? ?????????????????? ?????? ??????, ???? ?? ?????????? ??????!"
        return

    if obj_name == "Furniture" or obj_name == "Furniture2":
        m "?????? ???????????? ???????????????????????? ???????? ?????????????????????? ????????????.

        ?????????? ??????????????????."

        "?????????????? ?????? ???????????????? ?? ????????, ?? ?? ?????????????? ?????? ????????????."

        m "?????????????????? ?????? ???? ?????????????"
        "???? ???? ?????? ?????????? ????????????????????..."
        return

    if obj_name == "Chandelier":
        m "?????? ???????????? ?????????? ?????????? ??????????????????."

        "?? ?? ?????????? ???????????? ?????? ??????."

        m "?????????? ?? ?????????? ???????? ??????, ?? ???????????????? ?????? ????????????..."
        return

    if obj_name == "Curtains":
        m "?????? ??????????..."
        "(????????)"
        return
    if obj_name == "Lamps":
        "?????????? ?? ?????????? ???????? ??????, ?? ???????????? ?????????? ?????? ???????????? ??????????!"
        return

    if obj_name == "Windows":
        if day_time == "day":
            m "?????????????? ?????????????????? ????????."
            m "???????? ?????? ???? ??????, ???? ???????????? ????????!"
            return

        if day_time == "evening":
            m "???? ???????????? ??????????."

            "?????? ??????????!"
    if obj_name == "Picture":
        m "?????? ?????????????? ??????-???? ?????????????? ?????????? ????????."
        m "??????????????????, ?????? ?????? ???????"
        return

    if obj_name == "Fountain":
        if obj_data["action"] == "l":
            m "?????? ????????????..."
            "????????????..."
            return

        if obj_data["action"] == "w":
            call change_scene("floor1_fountain", "Fade", "snd_fountain") from _call_change_scene_106
            return

    return
