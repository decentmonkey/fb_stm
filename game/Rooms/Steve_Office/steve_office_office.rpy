default steve_office_office_steve_suffix = 1

label steve_office_office:
    $ print "enter_steve_office_office"
    $ miniMapData = []
    $ scene_image = "scene_Steve_Office_Office"
    return

label steve_office_office_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Office_Monica_[cloth]", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 9}, scene="steve_office_office")
    $ add_object_to_scene("Steve", {"type":2, "base":"Steve_Office_Office_Steve_[steve_office_office_steve_suffix]", "click" : "steve_office_office_environment", "actions" : "lt", "icon_t":"/Icons/talk" + res.suffix +".png", "zorder" : 10}, scene="steve_office_office")

    $ add_object_to_scene("Bar", {"type":2, "base":"steve_office_office_Bar", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Chair1", {"type":2, "base":"steve_office_office_Chair1", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Chair2", {"type":2, "base":"steve_office_office_Chair2", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Chair3", {"type":2, "base":"steve_office_office_Chair3", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Chair4", {"type":2, "base":"steve_office_office_Chair4", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Chair5", {"type":2, "base":"steve_office_office_Chair5", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Sofa", {"type":2, "base":"steve_office_office_Sofa", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office")
    $ add_object_to_scene("Table", {"type":2, "base":"steve_office_office_Table_Object", "click" : "steve_office_office_teleport", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="steve_office_office")

    $ add_object_to_scene("Teleport_Steve_Office_Secretary", {"type":3, "text" : t_("НАЗАД К СЕКРЕТАРШЕ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "steve_office_office_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover":True, "teleport":True}, scene="steve_office_office")

    return

label steve_office_office_teleport:
    if obj_name == "Teleport_Steve_Office_Secretary":
        call change_scene("steve_office_secretary") from _call_change_scene_245
    if obj_name == "Table":
        if act == "l":
            mt "Большой стол..."
            "Стив любит делать собрания."
            if monicaBitch == True:
                "Тщеславный ублюдок..."
        if act == "w":
            call change_scene("steve_office_office_table") from _call_change_scene_246
            return
    return

label steve_office_office_environment:
    if obj_name == "Monica":
        mt "Неплохо устроился Стив!"
        "НА МОИ ДЕНЬГИ!!!"

    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4" or obj_name == "Chair5" or obj_name == "Chair6" or obj_name == "Chair7" or obj_name == "Chair8" or obj_name == "Chair9" or obj_name == "Chair10":
        mt "Много стульев..."
        "Стив любит делать собрания."
        if monicaBitch == True:
            "Тщеславный ублюдок..."

    if obj_name == "Sofa":
        mt "Диван в кабинете?"
        "Это, наверное, здесь происходит ПРОДВИЖЕНИЕ по карьерной лестнице?"
    if obj_name == "Bar":
        mt "Милый бар..."
        "Книжки, цветочки."
        "Пускает пыль в глаза."
        "Я уверена что, если порыться, то в каждой книжке окажется спрятана бутылка алкоголя!"

    if obj_name == "Steve":
        if obj_data["action"] == "l":
            mt "Стив..."
            "Мой младший партнер..."
            if monicaBitch == True:
                mt "Скользкий мешок с дерьмом..."
            return
        if obj_data["action"] == "t":
            return
    return
