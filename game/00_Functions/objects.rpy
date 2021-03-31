init python:
    obj_properties_prefix = "img"
    obj_properties_suffixes = {" ":"sprite", "_evening":"sprite", "_mask":"mask", "_overlay":"overlay", "_evening_mask":"mask", "_evening_overlay":"overlay"}

    def fill_object_properties(name, obj_data):
        obj_base = obj_data["base"]
        asset_found = False
        for suffix in obj_properties_suffixes:
            suffix_type = obj_properties_suffixes[suffix]
            if suffix == " ":
                suffix = ""
            obj_prop_name = obj_properties_prefix + suffix
            if obj_data.has_key(obj_prop_name) == False or obj_data[obj_prop_name] == False:
                obj_data[obj_prop_name] = get_image_filename(obj_base + suffix)
                canvas_base_name = obj_base + suffix
                canvas_offset = get_canvas_offset(canvas_base_name)
                if obj_data[obj_prop_name] != False: asset_found = True
            else:
                canvas_base_name = obj_data[obj_prop_name]
                canvas_offset = get_canvas_offset(canvas_base_name)
                obj_data[obj_prop_name] = get_image_filename(obj_data[obj_prop_name])

            if canvas_offset != False:
                obj_data["canvas_" + obj_prop_name] = canvas_offset

        if asset_found == False and (showObjectsNotOwner == True or checkObjectOwnerVisible(name, obj_data) == True):
            ui.text("Assets not found for " + name + "\nScene name: " + api_scene_name + "\n" + str(obj_base), size=40, xalign=0.5, yalign=0.5)
            renpy.pause()
        return obj_data

#    def add_object_to_scene(obj_name, data, room_name = False): #adds to current scene
    def add_object_to_scene(*args, **kwargs): #adds to scene
        if kwargs.has_key("scene") == True:
            room_name = kwargs["scene"]
        else:
            room_name = api_scene_name
        obj_name = args[0]
        data = args[1]
        if kwargs.has_key("owner") == True:
            data["owner"] = kwargs["owner"]
        if len(args) > 2:
            conditions = args[2]
            data["conditions"] = conditions

#        if room_name == False: room_name = scene_name
        if scenes_data["objects"].has_key(room_name) == False:
            scenes_data["objects"][room_name] = {}

        if data.has_key("active") == False:
            data["active"] = True
        scenes_data["objects"][room_name][obj_name] = data
#        print obj_data
#        print scenes_data
        return

    def process_scene_objects_list(room_name):
        global scenes_data
        if scenes_data["objects"].has_key(room_name) == False:
            return
        obj_list = {}
        for obj_name in scenes_data["objects"][room_name]:
            if scenes_data["objects"][room_name][obj_name].has_key("active") and scenes_data["objects"][room_name][obj_name]["active"] == True:
                obj_list[obj_name] = process_scene_object(obj_name, scenes_data["objects"][room_name][obj_name])
        return obj_list

    def process_scene_object(obj_name, obj_data_source):
        obj_data = copy.deepcopy(obj_data_source)
        if obj_data.has_key("conditions"):
            #процессим conditions
            for var1 in obj_data["conditions"]:
                if globals().has_key(var1) == True and globals()[var1] == obj_data["conditions"][var1]["v"]:
                    #значение совпало, мержим!
#                    obj_data = obj_data["conditions"][var1].update(obj_data)
                    for var2 in obj_data["conditions"][var1]:
                        obj_data[var2] = obj_data["conditions"][var1][var2]
                    if obj_data["conditions"][var1].has_key("stop") and obj_data["conditions"][var1]["stop"] == True:
                        break
        obj_data.pop("conditions", None)
        for var1 in obj_data: #парсим переменные в свойствах
            if isinstance(obj_data[var1], basestring) == True:
                obj_data[var1] = parse_str(obj_data[var1])

        obj_data = fill_object_properties(obj_name, obj_data)
        obj_data["name"] = obj_name
        if obj_data.has_key("actions") == False: obj_data["actions"] = "l" # по дефолту всегда есть взгляд в действиях с предметом
        if obj_data.has_key("zorder") == False: obj_data["zorder"] = 0
        if obj_data.has_key("larrow") == False:
            obj_data["larrow"] = False
        else:
            obj_data["larrow"] = get_image_filename(obj_data["larrow"] + res.suffix)
        if obj_data.has_key("rarrow") == False:
            obj_data["rarrow"] = False
        else:
            obj_data["rarrow"] = get_image_filename(obj_data["rarrow"] + res.suffix)
        obj_data["hover_overlay"] = obj_data["hover_overlay"] if obj_data.has_key("hover_overlay") else False
        obj_data["hover_enabled"] = obj_data["hover_enabled"] if obj_data.has_key("hover_enabled") else True
        return obj_data

    def remove_object_from_scene(scene, obj_name):
        if obj_name in scenes_data["objects"][scene]: del scenes_data["objects"][scene][obj_name]
        return

    def clear_scene_from_objects(scene):
        if scenes_data["objects"].has_key(scene) != True:
            return
        list1 = []
        for key1 in scenes_data["objects"][scene]:
            list1.append(key1)
        for key1 in list1:
            if key1 != "data":
                del(scenes_data["objects"][scene][key1])
        return


    def subst_to_object(obj_name, subst_func, **kwargs):
        if kwargs.has_key("scene"):
            room_name = kwargs["scene"]
            del kwargs["scene"]
        else:
            room_name = api_scene_name

        if scenes_data["substs"].has_key(room_name) == False:
            scenes_data["substs"][room_name] = {}
        if subst_func != False:
            scenes_data["substs"][room_name][obj_name] = subst_func
        else:
            if obj_name in scenes_data["substs"][room_name]:
                del scenes_data["substs"][room_name][obj_name]
        return

#    def autorun_to_object(obj_name, autorun_func, **kwargs):
    def autorun_to_object(*args, **kwargs):
        if len(args) > 1:
            obj_name = "scene"
            room_name = args[0]
            autorun_func = args[1]
        else:
            obj_name = "scene"
            room_name = api_scene_name
            autorun_func = args[0]
            if kwargs.has_key("scene"):
                room_name = kwargs["scene"]
                del kwargs["scene"]
            else:
                room_name = api_scene_name
        if scenes_data["autorun"].has_key(room_name) == False:
            scenes_data["autorun"][room_name] = {}
        if autorun_func != False:
            scenes_data["autorun"][room_name][obj_name] = autorun_func
        else:
            if obj_name in scenes_data["autorun"][room_name]:
                del scenes_data["autorun"][room_name][obj_name]
        return

    def get_object_actions(actions_str):
        actions = []
        for idx in range(0, len(actions_str)):
            if actions_objects.has_key(actions_str[idx]):
                objects_to_append = actions_objects[actions_str[idx]]
                objects_to_append["action"] = actions_str[idx]
                actions.append(objects_to_append)

        return actions

    def move_object(*args, **kwargs): #(obj_name, scene_name), (obj_name, scene=scene_name)
        if len(args) > 1:
            obj_name = args[0]
            target_scene = args[1]
        else:
            obj_name = args[0]
            target_scene = kwargs["scene"]
        set_active(obj_name, False, scene="all")
        set_active(obj_name, True, scene=target_scene)
        return

    def get_active_objects(*args, **kwargs):
        if len(args) > 0:
            obj_name = args[0]
        else:
            obj_name = False
            kwargs["active"] = True
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["objects"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            rooms_list = [api_scene_name]
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(rooms_list[0])
        kwargs.pop("recursive", None)
        return_objects_list = []
        for room_name in rooms_list:
            if obj_name != False and len(rooms_list) == 1:
                if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key(obj_name) == True and scenes_data["objects"][room_name][obj_name]["active"] == True:
                    return_objects_list.append(scenes_data["objects"][room_name][obj_name])
            else:
                if obj_name == False:
                    if scenes_data["objects"].has_key(room_name) == True:
                        for obj1 in scenes_data["objects"][room_name]:
                            if check_filter(kwargs, scenes_data["objects"][room_name][obj1]) == True:
                                return_objects_list.append([scenes_data["objects"][room_name][obj1], obj1, room_name])
                else:
                    if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key(obj_name) == True and scenes_data["objects"][room_name][obj_name]["active"] == True:
                        if check_filter(kwargs, scenes_data["objects"][room_name][obj_name]) == True:
                            return_objects_list.append([scenes_data["objects"][room_name][obj_name], obj_name, room_name])

        if len(return_objects_list) > 0:
            return return_objects_list
        return False

    def get_objects(*args, **kwargs):
        if len(args) > 0:
            obj_name = args[0]
        else:
            obj_name = False
#            kwargs["active"] = True
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["objects"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            rooms_list = [api_scene_name]
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(rooms_list[0])
        kwargs.pop("recursive", None)
        return_objects_list = []
        for room_name in rooms_list:
            if obj_name != False and len(rooms_list) == 1:
                if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key(obj_name) == True:
                    return_objects_list.append(scenes_data["objects"][room_name][obj_name])
            else:
                if obj_name == False:
                    if scenes_data["objects"].has_key(room_name) == True:
                        for obj1 in scenes_data["objects"][room_name]:
                            if check_filter(kwargs, scenes_data["objects"][room_name][obj1]) == True:
                                return_objects_list.append([scenes_data["objects"][room_name][obj1], obj1, room_name])
                else:
                    if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key(obj_name) == True:
                        if check_filter(kwargs, scenes_data["objects"][room_name][obj_name]) == True:
                            return_objects_list.append([scenes_data["objects"][room_name][obj_name], obj_name, room_name])

        if len(return_objects_list) > 0:
            return return_objects_list
        return False

    def set_active(*args, **kwargs):
        if len(args)>1:
            #ищем по объекту
            obj_name = args[0]
            active_state = args[1]
            if kwargs.has_key("scene"):
                if kwargs["scene"] == "all":
                    rooms_list = list(scenes_data["objects"].keys())
                else:
                    rooms_list = [kwargs["scene"]]
                del kwargs["scene"]
            else:
                rooms_list = [api_scene_name]
            if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
                rooms_list = get_rooms_recursive(rooms_list[0])
            kwargs.pop("recursive", None)

            flag1 = False
            for room_name in rooms_list:
                if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key(obj_name) == True:
                    scenes_data["objects"][room_name][obj_name]["active"] = active_state
                    flag1 = True
#                    return True
            return flag1
        else:
            #ищем объекты по фильтру
            active_state = args[0]
            if kwargs.has_key("scene"):
                if kwargs["scene"] == "all":
                    rooms_list = list(scenes_data["objects"].keys())
                else:
                    rooms_list = [kwargs["scene"]]
                del kwargs["scene"]
            else:
                rooms_list = list(scenes_data["objects"].keys())
            if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
                rooms_list = get_rooms_recursive(rooms_list[0])
            kwargs.pop("recursive", None)
            flag1 = False
            for room_name in rooms_list:
                    for obj_name in scenes_data["objects"][room_name]:
                        if check_filter(kwargs, scenes_data["objects"][room_name][obj_name]) == True:
                            scenes_data["objects"][room_name][obj_name]["active"] = active_state
                            flag1 = True
            return flag1

    def check_scene_parent(room_name, parent, **kwargs): #recursive=True
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive_up(room_name)
        else:
            rooms_list = [room_name]
        for room_name in rooms_list:
            if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key("data") == True and scenes_data["objects"][room_name]["data"].has_key("parent") == True and scenes_data["objects"][room_name]["data"]["parent"] == parent:
                return True

        return False

    def scene_get_parent(room_name):
        if scenes_data["objects"].has_key(room_name) == True and scenes_data["objects"][room_name].has_key("data") == True and scenes_data["objects"][room_name]["data"].has_key("parent") == True:
            return scenes_data["objects"][room_name]["data"]["parent"]
        return False

    def get_rooms_recursive(start_room):
        rooms_list = [start_room]
        parent = start_room
        cnt = 1
        while cnt > 0:
            cnt = 0
            for room_name in scenes_data["objects"]:
                if scenes_data["objects"][room_name].has_key("data") == True and scenes_data["objects"][room_name]["data"].has_key("parent") == True:
                    if (scenes_data["objects"][room_name]["data"]["parent"] in rooms_list) and (room_name not in rooms_list):
                        cnt = cnt + 1
                        rooms_list.append(room_name)

        return rooms_list

    def get_rooms_recursive_up(start_room):
        rooms_list = [start_room]
#        parent = start_room
        room_ptr = start_room
        while scenes_data["objects"].has_key(room_ptr) and scenes_data["objects"][room_ptr].has_key("data") == True and scenes_data["objects"][room_ptr]["data"].has_key("parent") == True:
            parent_room = scenes_data["objects"][room_ptr]["data"]["parent"]
            if parent_room != "none":
                rooms_list.append(parent_room)
            room_ptr = parent_room

#        cnt = 1
#        while cnt > 0:
#            cnt = 0
#            for room_name in scenes_data["objects"]:
#                if scenes_data["objects"][room_name].has_key("data") == True and scenes_data["objects"][room_name]["data"].has_key("parent") == True:
#                    if (scenes_data["objects"][room_name]["data"]["parent"] not in rooms_list):
#                        cnt = cnt + 1
#                        rooms_list.append(scenes_data["objects"][room_name]["data"]["parent"])

        return rooms_list


    def set_var(obj_name, **kwargs):
        if kwargs.has_key("scene"):
            room_name = kwargs["scene"]
            del kwargs["scene"]
        else:
            room_name = api_scene_name
        if scenes_data["objects"].has_key(room_name) == False or scenes_data["objects"][room_name].has_key(obj_name) == False:
            return False
        for var1, value1 in kwargs.items():
            scenes_data["objects"][room_name][obj_name][var1] = value1
        return True

    def parse_str(str1):
        result = re.findall(r'\[(.*?)\]', str1)
        for var1 in result:
            if globals().has_key(var1):
                str1 = str1.replace("[" + var1 + "]", str(globals()[var1]))
        return str1

label process_object_click(func_name, obj_name_source, obj_data_source):
#    $ config.has_autosave = False
#    $ config.autosave_on_choice = False

    $ obj_name = obj_name_source
    $ obj_data = obj_data_source
    if clickHoldMode == True and clickHoldFlag == True:
        $ x,y = renpy.get_mouse_pos()
        if time.time() - clickHoldLastTime < 1 and abs(x - clickHoldLastMouseX) < 3 and abs(y - clickHoldLastMouseY) < 3:
#            $ clickHoldFlag = False
#            show screen notify ("click holded!!!")
            return

    if interface_blocked_flag == True:
        return
#    $ print renpy.get_screen("say")
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        if engine2_inited_flag == True:
            return
        else:
            $ renpy.pop_call()
            jump show_scene_loop2
    if scenes_data["substs"].has_key(scene_name) and scenes_data["substs"][scene_name].has_key(obj_name):
        if scenes_data["substs"][scene_name][obj_name] != False:
            $ func_name = scenes_data["substs"][scene_name][obj_name]
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    $ obj_data["action"] = obj_data["actions"]
    $ interface_blocked_flag = True
    $ screenActionHappened = False
    $ act = obj_data["action"]
#    $ print obj_data
    call process_hooks(obj_name, api_scene_name) from _call_process_hooks_10
    if _return != False and ((obj_data.has_key("owner") == False and owner == "Monica") or (obj_data.has_key("owner") == True and obj_data["owner"] == owner)):
        call expression func_name from _call_expression_1
        if _return != False:
            $ scene_refresh_flag = True
        else:
            $ scene_refresh_flag = False
    else:
        $ scene_refresh_flag = True
    $ interface_blocked_flag = False

    if screenActionHappened == True:
        $ clickHoldFlag = True
        $ clickHoldLastTime = time.time()
        $ clickHoldLastMouseX,clickHoldLastMouseY = renpy.get_mouse_pos()

#        $ dialogue_active_flag = False
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    call remove_dialogue() from _call_remove_dialogue
    if engine2_inited_flag == True:
        return
    else:
        $ renpy.pop_call()
        jump show_scene_loop2

label process_object_click_alternate_action(idx, actions_list, click_label, name, data):
#    $ config.has_autosave = False
#    $ config.autosave_on_choice = False

    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        if engine2_inited_flag == True:
            return
        else:
            $ renpy.pop_call()
            jump show_scene_loop2
    if idx == 0:
        $ func_name = click_label
    else:
        if renpy.has_label(name + actions_list[idx]["label_suffix"]) == False:
            $ func_name = click_label
        else:
            $ func_name = name + actions_list[idx]["label_suffix"]

#    call showLog("alternate action click!") from _call_showLog
    hide screen action_menu_screen
    $ data["action"] = actions_list[idx]["action"]
    #проверяем подстановку
    if data["action"] == "i": #info
        show screen sprites_hover_dummy_screen()
        $ x,y = renpy.get_mouse_pos()
        show screen character_info_screen(name, x, y)
        return
    if func_name == click_label:
        if scenes_data["substs"].has_key(scene_name) and scenes_data["substs"][scene_name].has_key(name):
            if scenes_data["substs"][scene_name][name] != False:
                $ func_name = scenes_data["substs"][scene_name][name]

    show screen sprites_hover_dummy_screen()
    $ interface_blocked_flag = True
    $ act = data["action"]

#    call expression func_name pass (name, data)
    $ obj_name = name
    $ obj_data = data
    call process_hooks(obj_name, api_scene_name) from _call_process_hooks_11
    if _return != False and ((obj_data.has_key("owner") == False and owner == "Monica") or (obj_data.has_key("owner") == True and obj_data["owner"] == owner)):
        call expression func_name from _call_expression_2
        if _return != False:
            $ scene_refresh_flag = True
        else:
            $ scene_refresh_flag = False
#        $ dialogue_active_flag = False
    else:
        $ scene_refresh_flag = True
    $ interface_blocked_flag = False
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    call remove_dialogue() from _call_remove_dialogue_1

    if engine2_inited_flag == True:
        return
    else:
        $ renpy.pop_call()
        jump show_scene_loop2

label process_object_click_alternate_inventory(idx, inventory_data, click_label, name, data):
#    $ config.has_autosave = False
#    $ config.autosave_on_choice = False

    if interface_blocked_flag == True:
        if engine2_inited_flag == True:
            return
        else:
            $ renpy.pop_call()
            jump show_scene_loop2
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        if engine2_inited_flag == True:
            return
        else:
            $ renpy.pop_call()
            jump show_scene_loop2
    $ func_name = name + inventory_data["label_suffix"]
    $ shortFunction = True
    if renpy.has_label(func_name) == False:
        $ func_name = inventory_data["default_nolabel"]
        $ shortFunction = False

#    call showLog("alternate inventory click!") from _call_showLog_1
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()

    $ data["action"] = "inv"
    $ interface_blocked_flag = True
    $ act = data["action"]
    $ obj_name = name
    if shortFunction == False:
        call expression func_name pass (name, inventory[idx], inventory_data, data) from _call_expression_3
    else:
        call expression func_name from _call_expression_4
    $ interface_blocked_flag = False
    if _return != False:
        $ scene_refresh_flag = True
    else:
        $ scene_refresh_flag = False
#        $ dialogue_active_flag = False
#        jump show_scene
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    if engine2_inited_flag == True:
        return
    else:
        $ renpy.pop_call()
        jump show_scene_loop2
#    jump show_scene

label process_object_click_forced(obj_name, act):
#label process_object_click_alternate_action(idx, actions_list, click_label, name, data):
    $ actions_list = get_object_actions(scenes_data["objects"][scene_name][obj_name]["actions"])
    $ interface_blocked_flag = False
    call process_object_click_alternate_action(scenes_data["objects"][scene_name][obj_name]["actions"].find(act), actions_list, scenes_data["objects"][scene_name][obj_name]["click"], obj_name, scenes_data["objects"][scene_name][obj_name]) from _rcall_process_object_click_alternate_action
    return
