label police_entrance:
    $ print "enter_police_entrance"
    $ miniMapData = []

    $ scene_image = "scene_Police_Entrance"
    music Power_Bots_Loop
    return

label police_entrance_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Police_Entrance_Monica_Reception_[cloth]", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("Reception", {"type":2, "base":"Police_Entrance_Monica_Reception_Reception", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 9})

    $ add_object_to_scene("Table", {"type":2, "base":"police_entrance_Table", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Turniket", {"type":2, "base":"police_entrance_Turniket", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Teleport_Inside", {"type":3, "text" : t_("ВХОД"), "rarrow" : "arrow_right_2", "base":"police_entrance_Teleport_Inside", "click" : "police_entrance_teleport", "xpos" : 1009, "ypos" : 59, "zorder":5, "group":"environment"})
    $ add_object_to_scene("Telepost_Street_Police", {"type":3, "text" : t_("НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "police_entrance_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "group":"environment"})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_entrance_teleport:
    if obj_name == "Teleport_Inside":
        mt "Я НИ ЗА ЧТО НЕ ПОЙДУ ТУДА!"
        "Мне надо быстрее убраться из этого страшного места!"
        return
    if obj_name == "Telepost_Street_Police":
        call change_scene("street_police") from _call_change_scene_35
        return

    return
label police_entrance_environment:
    if obj_name == "Table":
        mt "Это место, где работает эта страшная женщина..."
    if obj_name == "Turniket":
        mt "Я не буду приближаться к этому турникету! Мне страшно!"
    if obj_name == "Monica":
        mt "Что я здесь делаю???"
        "Мне надо быстрее убраться из этого страшного места!"
    if obj_name == "Reception":
        mt "Я не буду говорить с этой жуткой женщиной!"
        "Мне надо быстрее убраться из этого страшного места!"
    return
