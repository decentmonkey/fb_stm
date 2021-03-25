default steve_office_office_table_monica_suffix = 1
default steve_office_office_table_steve_suffix = ""

label steve_office_office_table:
    $ print "enter_steve_office_office_table"
    $ miniMapData = []
    $ scene_image = "scene_Steve_Office_Office_Table"
    return

label steve_office_office_table_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Office_Table_Monica_[cloth]_[steve_office_office_table_monica_suffix]", "click" : "steve_office_office_table_environment", "actions" : "l", "zorder" : 9}, scene="steve_office_office_table")
    $ add_object_to_scene("Steve", {"type":2, "base":"Steve_Office_Office_Table_Steve[steve_office_office_table_steve_suffix]", "click" : "steve_office_office_table_environment", "actions" : "lt", "icon_t":"/Icons/talk" + res.suffix +".png", "zorder" : 10}, scene="steve_office_office_table")

    $ add_object_to_scene("Bar", {"type":2, "base":"steve_office_office_table_Bar", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair1", {"type":2, "base":"steve_office_office_table_Chair1", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair2", {"type":2, "base":"steve_office_office_table_Chair2", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair3", {"type":2, "base":"steve_office_office_table_Chair3", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair4", {"type":2, "base":"steve_office_office_table_Chair4", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair5", {"type":2, "base":"steve_office_office_table_Chair5", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair6", {"type":2, "base":"steve_office_office_table_Chair6", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair7", {"type":2, "base":"steve_office_office_table_Chair7", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair8", {"type":2, "base":"steve_office_office_table_Chair8", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair9", {"type":2, "base":"steve_office_office_table_Chair9", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Chair10", {"type":2, "base":"steve_office_office_table_Chair10", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Door", {"type":2, "base":"steve_office_office_table_Door", "click" : "steve_office_office_table_teleport", "actions" : "lw", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Sofa", {"type":2, "base":"steve_office_office_table_Sofa", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")
    $ add_object_to_scene("Steve_Chair", {"type":2, "base":"steve_office_office_table_Steve_Chair", "click" : "steve_office_office_table_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="steve_office_office_table")

    return

label steve_office_office_table_teleport:
    if obj_name == "Door":
        if obj_data["action"] == "l":
            mt "Дверь в кабинет Стива."
            "Мне все-время кажется что за ней кто-то подслушивает..."
        if obj_data["action"] == "w":
            call change_scene("steve_office_secretary") from _call_change_scene_249
            return
    return

label steve_office_office_table_environment:
    if obj_name == "Steve_Chair":
        mt "Мне нравится стул Стива."
        "Пожалуй, он слишком хорош для него..."
    if obj_name == "Monica":
        if catchSteveInProgress == True:
            mt "Неплохо устроился Стив!"
            "НА МОИ ДЕНЬГИ!!!"
    if obj_name == "Steve":
        if act == "l":
            mt "Склизкий червяк все время пытается обмануть меня..."
        if act == "t":
            return
    return
