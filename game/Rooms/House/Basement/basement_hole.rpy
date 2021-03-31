#default basementHoleIncomingDirection = ""

label basement_hole:
    $ print "enter_basement_hole"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_4

    $ scene_image = "scene_Basement_Hole"
    music Sneak_n_Get_Caught
    return

label basement_hole_init:

    $ monica_tint = [1.0, 1.0, 0.9]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Hole_Monica_[cloth]_1", "click" : "basement_hole_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, {"basementHoleIncomingDirection":{"v":"Bedroom", "base" : "Basement_Hole_Monica_[cloth]_2"}})

    $ add_object_to_scene("Lamp", {"type":2, "base":"Basement_Hole_Lamp", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Basement_Hole_Trash1", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Basement_Hole_Trash2", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Basement_Hole_Trash3", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Basement_Hole_Trash4", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Basement_Hole_Trash5", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Basement_Bedroom", {"type":3, "text" : t_("СПАЛЬНЯ ДЛЯ ПРИСЛУГИ"), "rarrow" : "arrow_right_2", "base":"Basement_Hole_Teleport_Bedroom", "click" : "basement_hole_teleport", "xpos" : 1334, "ypos" : 232, "zorder":15, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("ПРАЧЕЧНАЯ"), "larrow" : "arrow_down_2", "base":"Basement_Hole_Teleport_Laundry", "click" : "basement_hole_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Basement_Side", {"type":3, "text" : t_("ТЕМНЫЙ ПРОХОД"), "rarrow" : "arrow_right_2", "base":"Basement_Hole_Teleport_Side", "click" : "basement_hole_teleport", "xpos" : 693, "ypos" : 184, "zorder":15, "high_sprite_hover": True, "teleport":True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label basement_hole_teleport:
    if obj_name == "Teleport_Basement_Laundry":
        call change_scene("basement_laundry") from _call_change_scene_45
        return
    if obj_name == "Teleport_Basement_Bedroom":
        call change_scene("basement_bedroom1") from _call_change_scene_46
        return
    if obj_name == "Teleport_Basement_Side":
        mt "В том коридоре нет света. Я туда не пойду!"
    return

label basement_hole_environment:
    if obj_name == "Monica":
        mt "Какой жуткий коридор..."

    if obj_name == "Lamp":
        mt "Я не знала что в моем доме есть такие древние лампы..."

    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5":
        mt "Какой-то бесполезный хлам..."
    return
