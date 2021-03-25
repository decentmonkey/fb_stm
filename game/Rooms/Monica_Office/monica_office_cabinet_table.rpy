default monicaOfficeWhiskeyOnTable = False

label monica_office_cabinet_table:
    $ print "enter_monica_office_cabinet_table"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_2

    if monicaOfficeWhiskeyOnTable == False:
        $ scene_image = "scene_Office_Monica_Cabinet_Table[day_suffix]"
    else:
        $ scene_image = "scene_Office_Monica_Cabinet_Table_Whiskey[day_suffix]"

    if get_active_objects("Biff", scene="monica_office_cabinet") != False: #Если Биф в офисе, то помещаем его и сюда тоже
        $ set_active("Biff", True)
    return

label monica_office_cabinet_table_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Monica_[cloth][day_suffix]", "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Biff", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_biff[day_suffix]", "click" : "monica_office_cabinet_table_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Flowers", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Flowers", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":2, "group":"environment"})
    $ add_object_to_scene("Paints", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Paints", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":2, "group":"environment"})
    $ add_object_to_scene("Water", {"type" : 2,  "active":False, "base" : "Office_Monica_Cabinet_Table_Water", "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":2, "group":"environment"}, {"monicaOfficeWhiskeyOnTable":{"v":False, "active":True}})
    $ add_object_to_scene("Whiskey", {"type" : 2, "active":False, "base" : "Office_Monica_Cabinet_Table_Whiskey_Object", "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":2, "group":"environment"}, {"monicaOfficeWhiskeyOnTable":{"v":True, "active":True}})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : t_("К СЕКРЕТАРЮ"), "larrow" : "arrow_left_2", "base":"Office_Monica_Cabinet_Table_Exit", "click" : "monica_office_cabinet_table_teleport", "xpos" : 723, "ypos" : 166, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.85], "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_cabinet_table_teleport:
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary") from _call_change_scene_69
        return
    return
label monica_office_cabinet_table_environment:
    if obj_name == "Biff":
        if act == "l":
            mt "Я ненавижу этого мерзавца!!!"
        return
    if obj_name == "Monica":
        mt "Меня бесит что я стою перед этим столом, словно какая-то попрошайка!!!"
        "Это мой стол! МОЙ!!!"
        return
    if obj_name == "Journal":
        mt "Что он смотрит в моем журнале?"
        "Это мой журнал, который я любила разглядывать. Что ему надо там?"
        return

    if obj_name == "Water":
        mt "Я любила пить эту воду..."
        return
    if obj_name == "Whiskey":
        mt "Виски???"
        "На рабочем месте?!?!"
        "Этот мерзавец не заслуживает своего положения!"
        "Это возмутительно!"
    return


#
