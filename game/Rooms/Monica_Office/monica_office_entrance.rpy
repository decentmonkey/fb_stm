default monicaOfficeEntranceMonicaSuffix = "2"

default monicaOfficeOpened = False

label monica_office_entrance:
    $ print "enter_monica_office_entrance"
    $ miniMapData = []
    if ep216_office_blocked_day < day:
        call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_6

    $ scene_image = "scene_Office_Entrance_Monica"
    music Groove2_85
#    music Stealth_Groover
    return

label monica_office_entrance_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Monica_Office_Entrance_Monica_[cloth]_[monicaOfficeEntranceMonicaSuffix]", "click" : "monica_office_entrance_environment2", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Chest", {"type" : 2, "base" : "Monica_Office_Entrance_Chest", "click" : "monica_office_entrance_environment2", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Composition", {"type" : 2, "base" : "Monica_Office_Entrance_Composition", "click" : "monica_office_entrance_environment2", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Paint", {"type" : 2, "base" : "Monica_Office_Entrance_Paint", "click" : "monica_office_entrance_environment2", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Plants", {"type" : 2, "base" : "Monica_Office_Entrance_Plants", "click" : "monica_office_entrance_environment2", "actions" : "l", "zorder":0, "group":"environment"})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : t_("ЛИФТ"), "larrow" : "arrow_left_2", "base":"Monica_Office_Entrance_Lift", "click" : "monica_office_entrance_teleport2", "xpos" : 691, "ypos" : 884, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Street_Monica_Office", {"type":3, "text" : t_("НАЗАД"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_entrance_teleport2", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_entrance_teleport2:
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary", "Fade_long", "snd_lift") from _call_change_scene_41
        return
#        call change_scene("monica_office_secretary", "Fade_long", "snd_lift") from _call_change_scene_79
        return
    if obj_name == "Teleport_Street_Monica_Office":
        call change_scene("street_monica_office", "Fade_long", "highheels_run2") from _call_change_scene_42
        return

    return
label monica_office_entrance_environment2:
    if obj_name == "Chest":
        mt "Это просто декорация."

    if obj_name == "Composition":
        mt "Веселая композиция.
        Я сама подобрала её сюда."
        "Мне это кажется каким-то далеким..."

    if obj_name == "Plants":
        mt "Я люблю цветы..."
        "Жаль они сейчас не мои..."
        "Но это временно!!!"

    if obj_name == "Paint":
        mt "Когда я решу свою проблему, я непременно встречусь с ней..."

    if obj_name == "Monica":
        mt "Это мой личный вход в здание."
        "Кто-то его захватил."
        "Но я все верну назад!"
        "И отомщу ублюдкам!!!"

    return
