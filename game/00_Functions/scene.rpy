init python:
    def store_scene(scene_name, **kwargs): #сохранить сцену в переменную
        stored_scene = {"objects":{}, "hooks":{}, "substs":{}, "autorun":{}, "rooms_list":[]}
        rooms_list = [scene_name]
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(rooms_list[0])

        for room_name in rooms_list:
            if scenes_data["objects"].has_key(room_name) == True:
                stored_scene["objects"][room_name] = copy.deepcopy(scenes_data["objects"][room_name])
            else:
                stored_scene["objects"][room_name] = {}
            if scenes_data["hooks"].has_key(room_name) == True:
                stored_scene["hooks"][room_name] = copy.deepcopy(scenes_data["hooks"][room_name])
            else:
                stored_scene["hooks"][room_name] = {}
            if scenes_data["substs"].has_key(room_name) == True:
                stored_scene["substs"][room_name] = copy.deepcopy(scenes_data["substs"][room_name])
            else:
                stored_scene["substs"][room_name] = {}
            if scenes_data["autorun"].has_key(room_name) == True:
                stored_scene["autorun"][room_name] = copy.deepcopy(scenes_data["autorun"][room_name])
            else:
                stored_scene["autorun"][room_name] = {}
            stored_scene["rooms_list"].append(room_name)
#        scenes_data["temp"] = stored_scene
        return stored_scene

    def restore_scene(stored_scene_data): #восстановить сцену из переменной
        for room_name in stored_scene_data["rooms_list"]:
            if stored_scene_data["objects"].has_key(room_name):
                scenes_data["objects"][room_name] = stored_scene_data["objects"][room_name]
            if stored_scene_data["hooks"].has_key(room_name):
                scenes_data["hooks"][room_name] = stored_scene_data["hooks"][room_name]
            if stored_scene_data["substs"].has_key(room_name):
                scenes_data["substs"][room_name] = stored_scene_data["substs"][room_name]
            if stored_scene_data["autorun"].has_key(room_name):
                scenes_data["autorun"][room_name] = stored_scene_data["autorun"][room_name]

        return stored_scene_data
