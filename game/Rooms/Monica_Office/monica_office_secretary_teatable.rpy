label monica_office_secretary_teatable:
    $ print "enter_monica_office_secretary_teatable"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_7

    $ scene_image = "scene_Office_Monica_Secretary_Teatable[day_suffix]"

label monica_office_secretary_teatable_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Monica_[cloth][day_suffix]", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Books1", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Books", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Documents", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Documents", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Elephant", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Elephant", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Flower", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Flower", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Gong", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Gong", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Sofa", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Sofa", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":-1, "group":"environment"})
    $ add_object_to_scene("TableBooks", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_TableBooks", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0, "group":"environment"})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_secretary_teatable_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_secretary_teatable_teleport:
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary") from _call_change_scene_82
        return
    return
label monica_office_secretary_teatable_environment:
    if obj_name == "Monica":
        mt "Это чайный столик."
        "Неудивительно что выпечки и кофе здесь больше нет..."
        "А жаль, я бы с удовольствием съела что-нибудь!"
    if obj_name == "Documents":
        mt "Я в будущем разберусь со всеми делами что натворил здесь Биф!"

    if obj_name == "Flower":
        mt "Цветок..."
    if obj_name == "Gong":
        mt "Что это?"
        "Маленький Гонг?"
    if obj_name == "Sofa":
        mt "Диван для ожидающих приема гостей."
    if obj_name == "TableBooks":
        mt "Развлекательные книги для ожидающих гостей."
    if obj_name == "Elephant":
        mt "Ух-ты!
        Маленький слоник!"
        "Как это мило!..."
        call bitch(-3, "secretary_elephant") from _call_bitch_7
    return


#
