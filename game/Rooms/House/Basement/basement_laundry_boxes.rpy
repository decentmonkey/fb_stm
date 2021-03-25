default laundry_box1_cnt = 0
default laundry_box2_cnt = 0
default laundry_box3_cnt = 0
default laundry_box4_cnt = 0
default laundry_box5_cnt = 0
default laundry_box6_cnt = 0

default laundry_box6_empty = False
default laundry_box6_dress_looked = False
default laundry_box6_dress_taken = False

label basement_laundry_box1:
    $ scene_name = "basement_laundry_box1"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_Box1"

    $ add_object_to_scene("Box1_Rags1", {"type":2, "base":"Basement_Laundry_Box1_Rags1", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Box1_Rags2", {"type":2, "base":"Basement_Laundry_Box1_Rags2", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Box1_Rags3", {"type":2, "base":"Basement_Laundry_Box1_Rags3", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry_box2:
    $ scene_name = "basement_laundry_box2"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_Box2"

    $ add_object_to_scene("Box2_Rags1", {"type":2, "base":"Basement_Laundry_Box2_Rags1", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Box2_Rags2", {"type":2, "base":"Basement_Laundry_Box2_Rags2", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry_box3:
    $ scene_name = "basement_laundry_box3"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_Box3"

    $ add_object_to_scene("Box3_Detergents", {"type":2, "base":"Basement_Laundry_Box3_Detergents", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Box3_Sprays", {"type":2, "base":"Basement_Laundry_Box3_Sprays", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Box3_Tablets", {"type":2, "base":"Basement_Laundry_Box3_Tablets", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry_box4:
    $ scene_name = "basement_laundry_box4"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_Box4"

    $ add_object_to_scene("Box4_Toilet_Paper", {"type":2, "base":"Basement_Laundry_Box4_Toilet_Paper", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry_box5:
    $ scene_name = "basement_laundry_box5"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_Box5"

    $ add_object_to_scene("Box5_Towels", {"type":2, "base":"Basement_Laundry_Box5_Towels", "click" : "basement_laundry_boxes_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry_box6:
    $ scene_name = "basement_laundry_box6"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    if laundry_box6_empty == False:
        $ scene_image = "scene_Laundry1_Box6"
        $ add_object_to_scene("Box6_Dress", {"type":2, "base":"Basement_Laundry_Box6_Dress", "click" : "basement_laundry_boxes_environment", "actions" : "lh", "zorder" : 0})
    else:
        $ scene_image = "scene_laundry1_box6_empty"

    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry_boxes_teleport(obj_name, obj_data):
    call change_scene("basement_laundry", "Fade", "desk_close") from _call_change_scene_50
    return

label basement_laundry_boxes_environment(obj_name, obj_data):
    if scene_name == "basement_laundry_box1":
        if obj_name == "Box1_Rags1":
            m "Какие-то тряпки..."
            "Желтые..."
            if laundrySearchingForDress == True:
                "Это не мое платье..."
            if laundrySearchingForIron == True:
                "Здесь нет утюга..."
            $ laundry_box1_cnt+=1
        if obj_name == "Box1_Rags2":
            m "Розовая одежда, это не то..."
            $ laundry_box1_cnt+=1

        if obj_name == "Box1_Rags3":
            m "Это скомканная простыня или что-то вроде того..."
            $ laundry_box1_cnt+=1

        if laundry_box1_cnt == 3:
            m "Что я тут пытаюсь найти?
            Здесь нет ничего полезного!"

    if scene_name == "basement_laundry_box2":
        if obj_name == "Box2_Rags1":
            m "Белый комок ткани."
            if laundrySearchingForDress == True:
                "Мне не понять что это, но это не мое платье."
            if laundrySearchingForIron == True:
                "Это не утюг..."

            $ laundry_box2_cnt+=1
        if obj_name == "Box2_Rags2":
            m "Синяя тряпка..."
            $ laundry_box2_cnt+=1

        if laundry_box2_cnt == 2:
            if laundrySearchingForDress == True:
                m "Среди эти тряпок нет моего платья!!!"
            if laundrySearchingForIron == True:
                m "Среди эти тряпок нет утюга!!!"

    if scene_name == "basement_laundry_box3":
        if obj_name == "Box3_Detergents":
            m "Какие-то чистящие средства..."
            $ laundry_box3_cnt+=1
        if obj_name == "Box3_Sprays":
            m "Какие-то спреи для чистки и увлажнения."
            $ laundry_box3_cnt+=1
        if obj_name == "Box3_Tablets":
            m "Таблетки от накипи и стиральный порошок."
            $ laundry_box3_cnt+=1

        if laundry_box3_cnt == 3 and laundrySearchingForDress == True:
            m "ЗДЕСЬ НЕТ МОЕГО ПЛАТЬЯ, ЧЕРТ!!!"
            "Здесь одни таблетки и чистящие средства!
            Что я здесь вообще пытаюсь увидеть??
            Я в своем уме?"

    if obj_name == "Box4_Toilet_Paper":
        m "Туалетная бумага..."
        "Как оригинально..."

    if obj_name == "Box5_Towels":
        m "Полотенца..."
        "Синие..."
        if laundrySearchingForDress == True:
            "Мне нужно красное...
            И не полотенце, А ПЛАТЬЕ!!!"
        if laundrySearchingForIron == True:
            "А мне нужен утюг!"
            "Любого цвета!!!"

    if obj_name == "Box6_Dress":
        if obj_data["action"] == "l":
            m "Вот оно!
            Мое платье!!!"
            $ laundry_box6_dress_looked = True
        if obj_data["action"] == "h":
            sound snd_found_dress
            $ autorun_to_object("basement_laundry_box6", "basement_laundry_box6_take_dress")
            $ laundry_box6_empty = True
            call refresh_scene() from _call_refresh_scene_8
            return
    return

label basement_laundry_box6_take_dress:
    $ remove_objective("laundry_find_dress")
    if laundry_box6_dress_looked == False:
        m "Вот оно!
        Мое платье!!!"
    $ define_inventory_object("crumpled_dress", {"description" : t_("Мятое платье"), "label_suffix" : "_use_crumpled_dress", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/crumpled_dress" + res.suffix + ".png"})
    $ add_inventory("crumpled_dress", 1, True)
    $ laundry_box6_dress_taken = True
    $ laundrySearchingForDress = False
    $ laundrySearchingForIron = True
    $ laundryDressFound = True

    if juliaMonicaYell == True:
        imgc Monica_HomeCloth1_Smile1
        m "Эта Юлия ни на что не способна.
        Зато я все могу, как всегда!"
        "Я талант!
        Всегда добиваюсь чего хочу!"

        imgc Monica_HomeCloth1_Arrogance1
        m "Так.
        Платье мятое."

        m "Эта сучка мало того что не принесла мне его.
        Она его даже не погладила!!!"

        m "...."
    else:
        imgc Monica_HomeCloth1_Thinking1
        m "Так.
        Платье мятое."

    imgc Monica_HomeCloth1_Thinking1
    m "Мы не сдаемся.
    Где-то тут должен быть утюг."
    $ add_objective("laundry_find_iron", t_("Отыскать в прачечной утюг"), c_blue, 20)
    $ laundry_box1_cnt = 0
    $ laundry_box2_cnt = 0
    $ laundry_box3_cnt = 0
    return






















#
