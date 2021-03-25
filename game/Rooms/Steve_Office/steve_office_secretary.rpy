default steve_office_secretary_suffix = 1

label steve_office_secretary:
    $ print "enter_steve_office_secretary"
    $ miniMapData = []
    $ scene_image = "scene_Steve_Office_Secretary"
    music Groove2_85
    return

label steve_office_secretary_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Secretary_Monica_[cloth]", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 10}, scene="steve_office_secretary")
    $ add_object_to_scene("Jane", {"type":2, "base":"Steve_Office_Secretary_[steve_office_secretary_suffix]", "click" : "steve_office_secretary_environment", "actions" : "lt", "zorder" : 9}, scene="steve_office_secretary")

    $ add_object_to_scene("Monitor", {"type":2, "base":"steve_office_secretary_Monitor", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")
    $ add_object_to_scene("Folders1", {"type":2, "base":"steve_office_secretary_Folders1", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")
    $ add_object_to_scene("Folders2", {"type":2, "base":"steve_office_secretary_Folders2", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")
    $ add_object_to_scene("Flower1", {"type":2, "base":"steve_office_secretary_Flower1", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")
    $ add_object_to_scene("Flower2", {"type":2, "base":"steve_office_secretary_Flower2", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")
    $ add_object_to_scene("Flower3", {"type":2, "base":"steve_office_secretary_Flower3", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")
    $ add_object_to_scene("Flower4", {"type":2, "base":"steve_office_secretary_Flower4", "click" : "steve_office_secretary_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_secretary")

    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "steve_office_secretary_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover":True, "teleport":True}, scene="steve_office_secretary")
    $ add_object_to_scene("Teleport_Steve_Office_Office", {"type":3, "text" : t_("КАБИНЕТ СТИВА"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "steve_office_secretary_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True}, scene="steve_office_secretary")

    return

label steve_office_secretary_teleport:
    if obj_name == "Teleport_Street":
        call change_scene("street_steve_office", "Fade_long", "snd_lift") from _call_change_scene_276
    if obj_name == "Teleport_Steve_Office_Office":
        call change_scene("steve_office_office") from _call_change_scene_277
        return
    return

label steve_office_secretary_environment:
    if obj_name == "Flower1" or obj_name == "Flower2" or obj_name == "Flower3" or obj_name == "Flower4":
        if monicaBitch == True:
            mt "Эта сучка наставила цветов везде."
        else:
            mt "Эта секретарша наставила цветов везде."
        "Хочет быть похожей на меня?"
        "Она не понимает, что для этого надо нечно большее!"
    if obj_name == "Folders1" or obj_name == "Folders2":
        if monicaBitch == True:
            "Не слишком-ли много Стив доверяет этой сучке?"
        else:
            "Не слишком-ли много Стив доверяет этой секретарше?"
    if obj_name == "Monitor":
        mt "Какой большой экран у нее.
        Я уверена что там открыты не рабочие документы, а какой-нибудь женский магазин!"
        "Никчемный работник!"
    if obj_name == "Monica":
        mt "Я доберусь до этого Стива! Здесь его логово!"
    if obj_name == "Jane":
        if obj_data["action"] == "l":
            if monicaBitch == True:
                mt "Я еще разберусь с этой сучкой..."
            else:
                mt "Я еще разберусь с этой Джейн..."

    return
