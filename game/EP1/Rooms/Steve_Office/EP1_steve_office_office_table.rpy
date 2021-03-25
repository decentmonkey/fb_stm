default steveOfficeSteveTableState = 0
default steveOfficeSteveTableStateTalk = 0

label EP1_steve_office_office_table:

    $ print "enter_steve_office_office_table"
    $ miniMapData = []

    $ scene_name = "steve_office_office_table"
    $ scene_caption = t_("STEVE'S CABINET")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_steve_office_office_table_Monica_" + cloth
    if steveOfficeSteveInOffice == True:
        if steveOfficeSteveTableState == 0:
            $ scene_image = "scene_steve_office_office_table_Steve_Monica"
            $ EP1_add_object_to_scene("Steve", {"type":2, "base":"steve_office_office_table_Steve", "click" : "EP1_steve_office_office_table_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})
        if steveOfficeSteveTableState == 1:
            $ scene_image = "scene_steve_office_office_table_Steve2_Monica"
            $ EP1_add_object_to_scene("Steve", {"type":2, "base":"steve_office_office_table_Steve2", "click" : "EP1_steve_office_office_table_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"steve_office_office_table_Monica_" + cloth, "click" : "EP1_steve_office_office_table_environment", "actions" : "l", "zorder" : 1})

    else:
        $ scene_image = "scene_steve_office_office_table_Monica"
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"steve_office_office_table_Monica_" + cloth, "click" : "EP1_steve_office_office_table_environment", "actions" : "l", "zorder" : 1})

    $ EP1_add_object_to_scene("Bar", {"type":2, "base":"steve_office_office_table_Bar", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair1", {"type":2, "base":"steve_office_office_table_Chair1", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair2", {"type":2, "base":"steve_office_office_table_Chair2", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair3", {"type":2, "base":"steve_office_office_table_Chair3", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair4", {"type":2, "base":"steve_office_office_table_Chair4", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair5", {"type":2, "base":"steve_office_office_table_Chair5", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair6", {"type":2, "base":"steve_office_office_table_Chair6", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair7", {"type":2, "base":"steve_office_office_table_Chair7", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair8", {"type":2, "base":"steve_office_office_table_Chair8", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair9", {"type":2, "base":"steve_office_office_table_Chair9", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair10", {"type":2, "base":"steve_office_office_table_Chair10", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Door", {"type":2, "base":"steve_office_office_table_Door", "click" : "EP1_steve_office_office_table_environment", "actions" : "lw", "zorder" : 0})
    $ EP1_add_object_to_scene("Sofa", {"type":2, "base":"steve_office_office_table_Sofa", "click" : "EP1_steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Steve_Chair", {"type":2, "base":"steve_office_office_table_Steve_Chair", "click" : "EP1_steve_office_office_table_environment", "actions" : "l", "zorder" : 0})

#    $ EP1_add_object_to_scene("Teleport_Steve_Office_Secretary", {"type":3, "text" : t_("НАЗАД К СЕКРЕТАРШЕ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_steve_office_office_table_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_steve_office_office_table_teleport(obj_name, obj_data):
    return
label EP1_steve_office_office_table_environment(obj_name, obj_data):
    if obj_name == "Door":
        if obj_data["action"] == "l":
            mt "Дверь в кабинет Стива."
            "Мне все-время кажется что за ней кто-то подслушивает..."
        if obj_data["action"] == "w":
            if catchSteveInProgress == True:
                mt "Еще рано уходить.
                Я еще не разобралась со Стивом!"
                return
            call EP1_change_scene("steve_office_secretary")
            return
    if obj_name == "Steve_Chair":
        mt "Мне нравится стул Стива."
        "Пожалуй, он слишком хорош для него..."
    if obj_name == "Monica":
        if catchSteveInProgress == True:
            mt "Стив развел бардак."
            "Мне надо почаще бывать здесь."
    if obj_name == "Steve":
        if obj_data["action"] == "l":
            mt "Стив юлит..."
            "Склизкий червяк все время пытается обмануть меня..."
            "Но это невозможно..."
        if obj_data["action"] == "t":
            if steveOfficeSteveTableStateTalk == 0:
                call EP1_steve1_steve_talk2()
                call EP1_refresh_scene_fade()
                return
            if steveOfficeSteveTableStateTalk == 1:
                call EP1_steve1_steve_talk3()
                call EP1_refresh_scene_fade(
                return
            if steveOfficeSteveTableStateTalk == 2:
                call EP1_steve1_steve_talk4()
                call EP1_refresh_scene_fade()
                return
            if steveOfficeSteveTableStateTalk == 3:
                call EP1_steve1_steve_talk5()
                $ catchSteveInProgress = False
                call EP1_change_scene("steve_office_office")
                return

    return
