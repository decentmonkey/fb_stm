label basement_bedroom_table:
    $ print "enter_basement_bedroom_table"
    $ miniMapData = []

    $ scene_image = "scene_Basement_Bedroom_Table"
    return

label basement_bedroom_table_init:
    $ add_object_to_scene("Book", {"type":2, "base":"Basement_Table_Book", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0}, scene="basement_bedroom_table")
    $ add_object_to_scene("Box", {"type":2, "base":"Basement_Table_Box", "click" : "basement_bedroom_table_environment", "actions" : "lh", "zorder" : 0, "b":0.13}, scene="basement_bedroom_table")
    $ add_object_to_scene("Lamp", {"type":2, "base":"Basement_Table_Lamp", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0}, scene="basement_bedroom_table")

    $ add_object_to_scene("FoodPaper", {"type":2, "base":"empty", "img_overlay":"Basement_Bedroom_Table_FoodPaper_Overlay", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 1, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("donut", {"type":2, "base":"Basement_Bedroom_Table_Cake1", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 6, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("cookies cherry filled", {"type":2, "base":"Basement_Bedroom_Table_Cake2", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 2, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("chocolate cake", {"type":2, "base":"Basement_Bedroom_Table_Cake3", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 3, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("cannoli", {"type":2, "base":"Basement_Bedroom_Table_Cake4", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 5, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("napoleon", {"type":2, "base":"Basement_Bedroom_Table_Cake5", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 7, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("brownie", {"type":2, "base":"Basement_Bedroom_Table_Cake6", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 6, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("cupcake", {"type":2, "base":"Basement_Bedroom_Table_Cake7", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 8, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("cookie with nuts", {"type":2, "base":"Basement_Bedroom_Table_Cake8", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 3, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
    $ add_object_to_scene("waffles", {"type":2, "base":"Basement_Bedroom_Table_Cake9", "click" : "food_basement_eat_food", "actions" : "lh", "zorder" : 4, "group":"environment", "label":"food", "active":False}, scene="basement_bedroom_table")
#    if basementBedroomJournal == True:
#        $ add_object_to_scene("Journal", {"type":2, "base":"Basement_Bedroom_Table_Journal", "click" : "basement_bedroom_table_environment", "actions" : "lh", "zorder" : 1})

    $ add_object_to_scene("Teleport_Bedroom_Back", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom_table_teleport", "xpos" : 960, "ypos" : 956, "zorder":11}, scene="basement_bedroom_table")

    return

label basement_bedroom_table_teleport:
    if obj_name == "Teleport_Bedroom_Back":
        $ sleepAfterEat = False
        $ basementBedroomMonicaSleepGfx = False
        call change_scene("basement_bedroom2") from _call_change_scene_93
        return
    return

label basement_bedroom_table_environment:
    if obj_name == "Box":
        if act == "l":
            mt "Старый ящик в старом столе..."
        if act == "h":
            sound snd_door_locked1
            $ renpy.pause(1.0)
            if ep29_revenge_quest_started == True:
                call ep29_dialogues5_gun_monica_a() from _rcall_ep29_dialogues5_gun_monica_a
                return
            mt "Закрыт..."
            "Мне неинтересно что там..."

    return
