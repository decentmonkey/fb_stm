label change_owner_default:
    python:
        if owners_data[new_owner].has_key("money") == False:
            owners_data[new_owner]["money"] = 0
        if owners_data[new_owner].has_key("inventory") == False:
            owners_data[new_owner]["inventory"] = []
        if owners_data[new_owner].has_key("objectives") == False:
            owners_data[new_owner]["objectives"] = []
        if owners_data[new_owner].has_key("map_objects") == False:
            owners_data[new_owner]["map_objects"] = {}

        owners_data[owner]["money"] = money
        money = owners_data[new_owner]["money"]
        owners_data[owner]["objectives"] = copy.deepcopy(objectives_list)
        objectives_list = owners_data[new_owner]["objectives"]
        owners_data[owner]["inventory"] = copy.deepcopy(inventory)
        inventory = owners_data[new_owner]["inventory"]
        owners_data[owner]["map_objects"] = copy.deepcopy(map_objects)
        map_objects = owners_data[new_owner]["map_objects"]

    if new_owner == "Betty":
        $ showObjectsNotOwner = False
        $ faceHudImage = "Face_Betty_HUD"
        $ hud_preset_current = "betty"
        $ hud_preset_default = "betty"
        $ minimap_coords_preset = 1
        call define_hudpresets() from _call_define_hudpresets_3

    if new_owner == "Melanie":
        $ showObjectsNotOwner = False
        $ faceHudImage = "Face_Melanie_HUD"
        $ hud_preset_current = "melanie"
        $ hud_preset_default = "melanie"
        $ minimap_coords_preset = 1
        $ melanie_control_active = True
        call define_hudpresets() from _rcall_define_hudpresets
    else:
        $ melanie_control_active = False


    if new_owner == "Monica":
        $ showObjectsNotOwner = True
        $ faceHudImage = False
        $ hud_preset_current = "default"
        $ hud_preset_default = "default"
        $ minimap_coords_preset = 0

    return
