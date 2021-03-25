default photostudioAlexSuffix = 3
default photostudioMelanieSuffix = 3

default monicaOfficePhotoStudioSkipMusicOneTime = False

label monica_office_photostudio:
    $ print "enter_monica_office_photostudio"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_8

    $ scene_image = "scene_Office_Monica_PhotoStudio"

    if monicaOfficePhotoStudioSkipMusicOneTime == False:
        music Mandeville
    $ monicaOfficePhotoStudioSkipMusicOneTime = False
    return

label monica_office_photostudio_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Monica_[cloth]", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Melanie[photostudioMelanieSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10})
    $ add_object_to_scene("AlexPhotograph", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Alex[photostudioAlexSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png" })

    $ add_object_to_scene("Box1", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Box1", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"})
    $ add_object_to_scene("Boxes", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Boxes", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"})
    $ add_object_to_scene("Cloth", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Cloth", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("SpotLight1", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight1", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":1 ,"b":0.15, "group":"environment"})
    $ add_object_to_scene("SpotLight2", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight2", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":1 ,"b":0.15, "group":"environment"})
    $ add_object_to_scene("SpotLight3", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight3", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"})
    $ add_object_to_scene("SpotLight4", {"type" : 2, "base" : "Office_Monica_PhotoStudio_SpotLight4", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":2 ,"b":0.15, "group":"environment"})
    $ add_object_to_scene("Top_Spotlights", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Top_Spotlights", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":0 ,"b":0.15, "group":"environment"})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : t_("К СЕКРЕТАРЮ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_photostudio_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_photostudio_teleport:
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary") from _call_change_scene_117
        return
    if obj_name == "Teleport_Monica_Office_MakeupRoom":
        call change_scene("monica_office_makeup_room") from _call_change_scene_234
        return
    return
label monica_office_photostudio_environment:
    if obj_name == "Monica":
        mt "Я все переделаю здесь, когда верну назад свой офис!"
        return
    if obj_name == "Melanie":
        if obj_data["action"] == "l":
            "Мелани - это топ-модель на сегодняшний день."
            "Похоже она неплохо себя чувствует пока меня нет..."
            return
        if obj_data["action"] == "t":
            return

    if obj_name == "AlexPhotograph":
        if obj_data["action"] == "l":
            mt "Алекс - мой фотограф.
            Самый лучший профессионал в стране, которого можно купить за деньги."
            return
        if obj_data["action"] == "t":
            return

    if obj_name == "Box1":
        mt "Этот световой бокс для заполняющего света, снизу."
    if obj_name == "Boxes":
        mt "Какие-то ящики с хламом."
        "Конечно там не хлам, а дорогое оборудование, но тем не менее..."
    if obj_name == "Cloth":
        mt "Полотно для фона во время съемок."
        $ photostudioLightsCntLooked += 1
    if obj_name == "SpotLight1" or obj_name == "SpotLight2":
        mt "Софтбокс для бокового света, насколько я помню..."
        $ photostudioLightsCntLooked += 1
    if obj_name == "SpotLight3":
        mt "Это просветный зонт, для заливающего света."
        $ photostudioLightsCntLooked += 1
    if obj_name == "SpotLight4":
        mt "Это контровой свет.
        Цветной."
        $ photostudioLightsCntLooked += 1

    if obj_name == "Top_Spotlights":
        mt "Эти прожекторы освещают модель сверху, а также подсвечивают фон за ней."
        $ photostudioLightsCntLooked += 1


    return





#
