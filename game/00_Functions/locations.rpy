init python:
    def add_location(loc_name, **kwargs):
        global scenes_data, api_scene_name
        if scenes_data["objects"].has_key(loc_name) == False:
            scenes_data["objects"][loc_name] = {"data":{}}
        kwargsArr = {}
        for key1, value1 in kwargs.items():
            scenes_data["objects"][loc_name]["data"][key1] = value1

        if kwargs.has_key("init_label"):
#            add_location_stored_api_scene_name = api_scene_name
#            api_scene_name = loc_name
            renpy.call("init_location", loc_name, kwargs["init_label"])
#            api_scene_name = add_location_stored_api_scene_name
#        print kwargs
        return

label init_location(loc_name, init_label):
    $ stored_api_scene_name = api_scene_name
    $ api_scene_name = loc_name
    call expression init_label from _call_expression_14
    $ api_scene_name = stored_api_scene_name
    return
