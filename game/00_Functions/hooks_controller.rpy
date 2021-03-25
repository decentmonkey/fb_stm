default hooks_stack = []
default sprites_hover_dummy_screen_flag = False
default hooks_log = {}
default hook_log_idx = 0
init python:
    def add_hook(*args, **kwargs): #устанавливает хук
        obj_name = args[0]
        hook_label = args[1]
        if kwargs.has_key("scene"):
            room_name = kwargs["scene"]
            del kwargs["scene"]
        else:
            room_name = api_scene_name
        if len(args) >= 3:
            room_name = args[2]
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(room_name)
        else:
            rooms_list = [room_name]
        kwargs.pop("recursive", None)

        hook_data = {"hook_label":hook_label}
        for var1, value1 in kwargs.items():
            hook_data[var1] = value1
        if hook_data.has_key("priority") == False:
            hook_data["priority"] = 100

        for room_name in rooms_list:
            if scenes_data["hooks"].has_key(room_name) == False:
                scenes_data["hooks"][room_name] = {}
            if scenes_data["hooks"][room_name].has_key(obj_name) == False:
                scenes_data["hooks"][room_name][obj_name] = []

            remove_hook(obj_name, hook_label, scene=room_name)
            hooks_list = scenes_data["hooks"][room_name][obj_name]
            flag1 = False
            hooks_list.append(hook_data)
            hooks_list = sort_hooks(hooks_list)
            scenes_data["hooks"][room_name][obj_name] = hooks_list
        return

    def add_hook_multi(hook_label, **kwargs): #устанавливает хук
        if kwargs["scene"] == "all":
            rooms_list = list(scenes_data["hooks"].keys())
        else:
            rooms_list = [kwargs["scene"]]
        del kwargs["scene"]
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(rooms_list[0])
        kwargs.pop("recursive", None)
        filter_arr = {}
        for var1 in kwargs["filter"]:
            filter_arr[var1] = kwargs["filter"][var1]
        kwargs.pop("filter", None)
        for room_name in rooms_list:
            for obj_name in scenes_data["objects"][room_name]:
                if check_filter(filter_arr, scenes_data["objects"][room_name][obj_name]) == True:
                    kwargs["scene"] = room_name
                    add_hook(obj_name, hook_label, **kwargs)
        return

    def add_hook_day(hook_label, **kwargs):
        suff = ""
        if kwargs.has_key("evening") and kwargs["evening"] == True:
            suff = "_evening"
        if kwargs.has_key("day"):
            add_hook("day_" + str(kwargs["day"]) + suff, hook_label, scene="global_day")

        if kwargs.has_key("week_day"):
            add_hook("week_day_" + str(kwargs["week_day"]) + suff, hook_label, scene="global_week_day")
        return

    def remove_hook_day(hook_label, **kwargs):
        suff = ""
        if kwargs.has_key("evening") and kwargs["evening"] == True:
            suff = "_evening"
        if kwargs.has_key("day"):
            remove_hook("day_" + str(kwargs["day"]) + suff, hook_label, scene="global_day")

        if kwargs.has_key("week_day"):
            remove_hook("week_day_" + str(kwargs[week_day]) + suff, hook_label, scene="global_week_day")
        return

    def remove_hook(*args, **kwargs):
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["hooks"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            if len(args) > 0:
                rooms_list = [api_scene_name]
            else:
                rooms_list = list(scenes_data["hooks"].keys())
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(rooms_list[0])
        kwargs.pop("recursive", None)

        if len(args) == 2: #obj_name, hook_label
            obj_name = args[0]
            hook_label = args[1]
        if len(args) == 1: #hook_label
            obj_name = False
            hook_label = args[0]
        if len(args) == 0: #() удаление текущего хука, либо удаление хука по фильтру
            if len(kwargs) > 0: #удаление всех хуков на сцене по фильтру
                flag1 = False
                filter_arr = {}
                for var1, value1 in kwargs.items():
                    filter_arr[var1] = value1

                for room_name in rooms_list:
                    if scenes_data["hooks"].has_key(room_name) == True:
                        for obj_name1 in scenes_data["hooks"][room_name]:
                            flag2 = False
                            hooks_list = scenes_data["hooks"][room_name][obj_name1]

                            for idx in reversed(range(len(hooks_list))):
                                if check_filter(filter_arr, hooks_list[idx]) == True:
                                    hooks_list.pop(idx)
                                    flag2 = True

                            if flag2 == True:
                                scenes_data["hooks"][room_name][obj_name1] = hooks_list

            else:
                if scenes_data["hooks"].has_key(last_hook_scene) and scenes_data["hooks"][last_hook_scene].has_key(last_hook_obj_name) == True:
                    hooks_list = scenes_data["hooks"][last_hook_scene][last_hook_obj_name]
                    idx = find_hook_by_label(hooks_list, last_hook_label)
                    if idx != -1:
                        hooks_list.pop(idx)
                        scenes_data["hooks"][last_hook_scene][last_hook_obj_name] = hooks_list
                        return True
                    return False
        else:
            flag1 = False
            for room_name in rooms_list:
                if obj_name == False:
                    if scenes_data["hooks"].has_key(room_name):
                        for obj_name1 in scenes_data["hooks"][room_name]:
                            hooks_list = scenes_data["hooks"][room_name][obj_name1]
                            idx = find_hook_by_label(hooks_list, hook_label)
                            if idx != -1:
                                hooks_list.pop(idx)
                                hooks_list = scenes_data["hooks"][room_name][obj_name1] = hooks_list
                                flag1 = True
                else:
                    if scenes_data["hooks"].has_key(room_name) and scenes_data["hooks"][room_name].has_key(obj_name) == True:
                        hooks_list = scenes_data["hooks"][room_name][obj_name]
                        idx = find_hook_by_label(hooks_list, hook_label)
                        if idx != -1:
                            hooks_list.pop(idx)
                            hooks_list = scenes_data["hooks"][room_name][obj_name] = hooks_list
                            return True

        return flag1


    def check_hook(*args, **kwargs):
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["hooks"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            if len(args) > 0:
                rooms_list = [api_scene_name]
            else:
                rooms_list = list(scenes_data["hooks"].keys())
        if kwargs.has_key("recursive") == True and kwargs["recursive"] == True:
            rooms_list = get_rooms_recursive(rooms_list[0])
        kwargs.pop("recursive", None)

        if len(args) == 2: #obj_name, hook_label
            obj_name = args[0]
            hook_label = args[1]
        if len(args) == 1: #hook_label
            obj_name = False
            hook_label = args[0]
        if len(args) == 0: #() проверка текущего хука, либо проверка хука по фильтру
            if len(kwargs) > 0: #проверка всех хуков на сцене по фильтру
                flag1 = False
                filter_arr = {}
                for var1, value1 in kwargs.items():
                    filter_arr[var1] = value1

                for room_name in rooms_list:
                    if scenes_data["hooks"].has_key(room_name) == True:
                        for obj_name1 in scenes_data["hooks"][room_name]:
                            flag2 = False
                            hooks_list = scenes_data["hooks"][room_name][obj_name1]

                            for idx in reversed(range(len(hooks_list))):
                                if check_filter(filter_arr, hooks_list[idx]) == True:
                                    flag1 = True
                                    return True

            else:
                if scenes_data["hooks"].has_key(last_hook_scene) and scenes_data["hooks"][last_hook_scene].has_key(last_hook_obj_name) == True:
                    hooks_list = scenes_data["hooks"][last_hook_scene][last_hook_obj_name]
                    idx = find_hook_by_label(hooks_list, last_hook_label)
                    if idx != -1:
                        flag1 = True
                        return True
                    return False
        else:
            flag1 = False
            for room_name in rooms_list:
                if obj_name == False:
                    if scenes_data["hooks"].has_key(room_name):
                        for obj_name1 in scenes_data["hooks"][room_name]:
                            hooks_list = scenes_data["hooks"][room_name][obj_name1]
                            idx = find_hook_by_label(hooks_list, hook_label)
                            if idx != -1:
                                flag1 = True
                                return True
                else:
                    if scenes_data["hooks"].has_key(room_name) and scenes_data["hooks"][room_name].has_key(obj_name) == True:
                        hooks_list = scenes_data["hooks"][room_name][obj_name]
                        idx = find_hook_by_label(hooks_list, hook_label)
                        if idx != -1:
                            flag1 = True
                            return True

        return flag1

    def replace_hook(*args, **kwargs):
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["hooks"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            rooms_list = [api_scene_name]


        filter_arr = {}
        for var1, value1 in kwargs.items():
            filter_arr[var1] = value1

        if len(args) == 3: #obj_name, hook_label, new_hook_label, [scene=scene_name]
            obj_name = args[0]
            hook_label = args[1]
            new_hook_label = args[2]
            flag1 = False
            for room_name in rooms_list:
                if scenes_data["hooks"][room_name].has_key(obj_name) == True:
                    hooks_list = scenes_data["hooks"][room_name][obj_name]
                    idx = find_hook_by_label(hooks_list, hook_label)
                    if idx != -1:
                        hooks_list[idx]["hook_label"] = new_hook_label
                        scenes_data["hooks"][room_name][obj_name] = hooks_list
                        flag1 = True
            if flag1 == False and debugMode == True:
                notif("Can't find object for hook: " + str(new_hook_label))
            return flag1
        if len(args) == 2: #hook_label, new_hook_label, [scene=scene_name]
            hook_label = args[0]
            new_hook_label = args[1]
            flag1 = False
            for room_name in rooms_list:
                for obj_name in scenes_data["hooks"][room_name]:
                    hooks_list = scenes_data["hooks"][room_name][obj_name]
                    idx = find_hook_by_label(hooks_list, hook_label)
                    if idx != -1:
                        if len(filter_arr) == 0 or (len(filter_arr) > 0 and check_filter(filter_arr, hooks_list[idx]) == True):
                            hooks_list[idx]["hook_label"] = new_hook_label
                            scenes_data["hooks"][room_name][obj_name] = hooks_list
                            flag1 = True
            if flag1 == False and debugMode == True:
                notif("Can't find object for hook: " + str(new_hook_label))
            return flag1

        if len(args) == 1: #new_hook_label, [scene=scene_name, filters]
            new_hook_label = args[0]
            flag1 = False
            if len(filter_arr) > 0:
                for room_name in rooms_list:
                    for obj_name in scenes_data["hooks"][room_name]:
                        hooks_list = scenes_data["hooks"][room_name][obj_name]
                        for idx in range(len(hooks_list)):
                            if check_filter(filter_arr, hooks_list[idx]) == True:
                                hooks_list[idx]["hook_label"] = new_hook_label
                                flag1 = True
                                scenes_data["hooks"][room_name][obj_name] = hooks_list
                if flag1 == False and debugMode == True:
                    notif("Can't find object for hook: " + str(new_hook_label))
                return flag1
        return False

    def clear_hooks(*args, **kwargs):
        if kwargs.has_key("scene"):
            if kwargs["scene"] == "all":
                rooms_list = list(scenes_data["hooks"].keys())
            else:
                rooms_list = [kwargs["scene"]]
            del kwargs["scene"]
        else:
            rooms_list = [api_scene_name]
        obj_name = False
        if len(args) >= 1:
            obj_name = args[0]
        for room_name in rooms_list:
            if scenes_data["hooks"].has_key(room_name):
                if obj_name == False:
                    scenes_data["hooks"][room_name] = {}
                else:
                    if scenes_data["hooks"][room_name].has_key(obj_name):
                        scenes_data["hooks"][room_name][obj_name] = []


    def enter_scene(hook_label, **kwargs):
        add_hook("enter_scene", hook_label, scene="global", **kwargs)
        return

    def add_talk(*args, **kwargs):
        obj_name = args[0]
        hook_label = args[1]
        add_hook(obj_name, hook_label, act="th", **kwargs)
        return

    def find_hook_by_label(hooks_list, hook_label):
        for idx in range(len(hooks_list)):
            if hooks_list[idx]["hook_label"] == hook_label:
                return idx

        return -1

    def sort_hooks(hooks_list):
        priority_list = []
        for idx in range(len(hooks_list)):
            if (hooks_list[idx]["priority"] in priority_list) == False:
                priority_list.append(hooks_list[idx]["priority"])
        priority_list.sort()
        hooks_list_sorted = []
        for priority_value in priority_list:
            for idx in range(len(hooks_list)):
                if hooks_list[idx]["priority"] == priority_value:
                    hooks_list_sorted.append(hooks_list[idx])
#        print priority_list
        return hooks_list_sorted

    def get_hooks_for_object(hook_obj_name, room_name = False):
        global scenes_data, api_scene_name
        if room_name == False:
            room_name = api_scene_name
        if scenes_data["hooks"].has_key(room_name) == False or scenes_data["hooks"][room_name].has_key(hook_obj_name) == False:
            return []
        hooks_list = scenes_data["hooks"][room_name][hook_obj_name]
        return hooks_list

    def checkObjectOwnerVisible(obj_name, obj_data):
        global owner, scene_name
        if (obj_data.has_key("owner") == False and owner == "Monica") or (obj_data.has_key("owner") == True and obj_data["owner"] == owner) or (obj_data.has_key("owners_visible_forced") and obj_data["owners_visible_forced"] == True):
            return True
        if scenes_data["hooks"].has_key(scene_name) == True and scenes_data["hooks"][scene_name].has_key(obj_name):
            hooks_list = scenes_data["hooks"][scene_name][obj_name]
            for hook_data in hooks_list:
                if hook_data.has_key("owner") == False:
                    if owner == "Monica":
                        return True
                if hook_data.has_key("owner") == True and hook_data["owner"] == owner:
                    return True
        return False

label process_hooks(hook_obj_name, room_name = False, sprites_hover_dummy_screen_flag = False, noowners=False):
    $ _return = None
    if room_name == False:
        $ room_name = api_scene_name

    if scenes_data["hooks"].has_key(room_name) == False or scenes_data["hooks"][room_name].has_key(hook_obj_name) == False:
        return _return

    $ hooks_list = scenes_data["hooks"][room_name][hook_obj_name]
    $ processed_hooks = []
    $ len1 = len(hooks_list)
    if len1 == 0:
        return _return
    $ idx = len1 - 1
    label .hooks_call_loop:
        $ renpy.not_infinite_loop(3.0)
        $ hooks_list = scenes_data["hooks"][room_name][hook_obj_name] #повтор для цикла, восстановление из-за глобальных переменных
        $ hook_data = hooks_list[idx]
        $ label_name = hook_data["hook_label"]
        $ hooks_stack.append([room_name, hook_obj_name, label_name, idx, processed_hooks])
        $ last_hook_scene = room_name
        $ last_hook_obj_name = hook_obj_name
        $ last_hook_label = label_name
        if label_name not in processed_hooks: #если во время вызова стерлись несколько хуков и список сдвинулся. Защита от повторения
            if sprites_hover_dummy_screen_flag == True:
                show screen sprites_hover_dummy_screen()
                $ sprites_hover_dummy_screen_flag = False
            $ hooks_log[label_name] = hook_log_idx
            $ hook_log_idx += 1
            if (hook_data.has_key("owner") == False and owner == "Monica") or (hook_data.has_key("owner") == True and hook_data["owner"] == owner) or noowners == True:
                if hook_data.has_key("act") == False or (act in hook_data["act"]):
                    if hook_data.has_key("once") and hook_data["once"] == True:
                        $ remove_hook()
                    call expression label_name from _call_expression_5 #вызов хука
        $ stack_data = hooks_stack.pop()
        $ label_name = stack_data[2]
        $ idx = stack_data[3]
        $ processed_hooks = stack_data[4]
        $ processed_hooks.append(label_name)
        if len(hooks_stack) > 0:
            $ stack_data = hooks_stack[-1]
        $ last_hook_scene = stack_data[0]
        $ last_hook_obj_name = stack_data[1]
        $ last_hook_label = stack_data[2]
        if scenes_data["hooks"].has_key(room_name) and scenes_data["hooks"][room_name].has_key(hook_obj_name):
            $ hooks_list = scenes_data["hooks"][room_name][hook_obj_name] #повтор для цикла
        else:
            $ hooks_list = []
        if _return == False: #для продолжения череды выполнения хуков, надо возвращать не False
            return _return
        label .hooks_call_loop2:
            $ idx = idx - 1
            if idx >= len(hooks_list):
                jump .hooks_call_loop2
#        $ print idx
        if idx >= 0:
            jump .hooks_call_loop


    return _return

label call_hook(label_name, menu_name, sprites_hover_dummy_screen_flag = False):
    $ last_hook_scene = "menu"
    $ last_hook_obj_name = menu_name
    $ last_hook_label = label_name
    if sprites_hover_dummy_screen_flag == True:
        show screen sprites_hover_dummy_screen()
        $ sprites_hover_dummy_screen_flag = False
    $ hooks_log[label_name] = hook_log_idx
    $ hook_log_idx += 1
    call expression label_name from _call_expression_12 #вызов хука
#    $ stack = renpy.get_return_stack()
#    $ stack[0] = (stack[0][0], stack[0][1], stack[0][2]+2)
#    $ renpy.set_return_stack(stack)
    #$ renpy.pop_call()
    return _return
