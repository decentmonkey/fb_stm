default laundryVisited = False
default clothesPinsSeen = False

default businessClothSearchDressInProgressLaundryVisited = False

default laundrySearchingForDress = False
default laundryDressFound = False
default laundrySearchingForIron = False
default laundryIronFound = False
default landryIroningActive = False

default laundryBoxesActive = True

default laundryIroningBoardState = "Default"

label EP1_basement_laundry:
    $ print "enter_basement_laundry"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()

    $ scene_name = "basement_laundry"
    $ scene_caption = t_("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_" + laundryIroningBoardState
#    $ scene_image = "scene_Basement_Pool_Monica_BusinessCloth1"

#    $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Pool_Monica_" + cloth, "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

#    $ EP1_add_object_to_scene("Bidet", {"type":2, "base":"Basement_Pool_Bidet", "click" : "EP1_basement_pool_environment", "actions" : "l", "zorder" : 0})
#    $ EP1_add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Basement_Pool_Door1", "click" : "EP1_basement_pool_teleport", "xpos" : 1043, "ypos" : 173, "zorder":0, "tint": [1.0, 1.0, 0.6]})
#    $ EP1_add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : t_("ПРАЧЕЧНАЯ"), "larrow" : "arrow_left_2", "base":"Basement_Pool_Door2", "click" : "EP1_basement_pool_teleport", "xpos" : 1561, "ypos" : 408, "zorder":0, "tint": [1.0, 1.0, 0.6]})

    if businessClothSearchDressInProgress == True:
        $ EP1_add_object_to_scene("Accessories1", {"type":2, "base":"Basement_Laundry_Accessories1", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Accessories2", {"type":2, "base":"Basement_Laundry_Accessories2", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Basket1", {"type":2, "base":"Basement_Laundry_Basket1", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Basket2", {"type":2, "base":"Basement_Laundry_Basket2", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Cloth1", {"type":2, "base":"Basement_Laundry_Cloth1", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Drying_Machine", {"type":2, "base":"Basement_Laundry_Drying_Machine", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Rags1", {"type":2, "base":"Basement_Laundry_Rags1", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Toilet_Paper", {"type":2, "base":"Basement_Laundry_Toilet_Paper", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Towels1", {"type":2, "base":"Basement_Laundry_Towels1", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Washer", {"type":2, "base":"Basement_Laundry_Washer", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Clothes_Pin", {"type":2, "base":"Basement_Laundry_Clothes_Pin", "click" : "EP1_basement_laundry_environment", "actions" : "l", "zorder" : 0})



        $ EP1_add_object_to_scene("Teleport_Box1", {"type":2, "base":"Basement_Laundry_Box1", "click" : "EP1_basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Teleport_Box2", {"type":2, "base":"Basement_Laundry_Box2", "click" : "EP1_basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Teleport_Box3", {"type":2, "base":"Basement_Laundry_Box3", "click" : "EP1_basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Teleport_Box4", {"type":2, "base":"Basement_Laundry_Box4", "click" : "EP1_basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Teleport_Box5", {"type":2, "base":"Basement_Laundry_Box5", "click" : "EP1_basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ EP1_add_object_to_scene("Teleport_Box6", {"type":2, "base":"Basement_Laundry_Box6", "click" : "EP1_basement_laundry_teleport", "actions" : "l", "zorder" : 0})

    if laundryVisited == False and businessClothSearchDressInProgress == False:
        $ EP1_autorun_to_object("basement_laundry", "basement_laundry_first_visit")

    if businessClothSearchDressInProgress == True:
        $ laundryVisited = True
        if businessClothSearchDressInProgressLaundryVisited == False:
            $ businessClothSearchDressInProgressLaundryVisited = True
            $ EP1_autorun_to_object("basement_laundry", "basement_laundry_dress_visit")
            $ laundrySearchingForDress = True
        $ EP1_add_object_to_scene("Teleport_Basement_Ironing_Board", {"type":3, "text" : t_("ГЛАДИЛЬНАЯ ДОСКА"), "rarrow" : "arrow_down_2", "base": "Basement_Laundry_Teleport_Ironing_Board_" + laundryIroningBoardState, "click" : "EP1_basement_laundry_teleport", "xpos" : 1652, "ypos" : 555, "zorder":11})


    $ EP1_add_object_to_scene("Teleport_Basement_Hole", {"type":3, "text" : t_("В ПОДВАЛ"), "larrow" : "arrow_dl", "base":"empty", "click" : "EP1_basement_laundry_teleport", "xpos" : 203, "ypos" : 873, "zorder":11})
    $ EP1_add_object_to_scene("Teleport_Basement_Pool", {"type":3, "text" : t_("НАЗАД К БАССЕЙНУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_basement_laundry_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label EP1_basement_laundry_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Basement_Pool":
        call EP1_change_scene("basement_pool")
        return
    if obj_name == "Teleport_Basement_Hole":
        if basementHoleRefuseFlag == True:
            call EP1_basement_hole_check()
            return
        $ basementHoleIncomingDirection = "Laundry"
        call EP1_change_scene("basement_hole")
        return
    if obj_name == "Teleport_Basement_Ironing_Board":
        call EP1_change_scene("basement_laundry2")
        return
    if laundryBoxesActive == False:
        m "Мне ничего не надо в этом ящике."
        return
    if obj_name == "Teleport_Box1":
        call EP1_change_scene("basement_laundry_box1", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box2":
        call EP1_change_scene("basement_laundry_box2", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box3":
        call EP1_change_scene("basement_laundry_box3", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box4":
        call EP1_change_scene("basement_laundry_box4", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box5":
        call EP1_change_scene("basement_laundry_box5", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box6":
        call EP1_change_scene("basement_laundry_box6", "Fade", "desk_open")
        return
    return

label EP1_basement_laundry_environment(obj_name, obj_data):
    if obj_name == "Accessories1":
        m "Какие-то щетки и моющие средства."
    if obj_name == "Accessories2":
        m "Какие-то гели и губки."
    if obj_name == "Clothes_Pin":
        m "ЧТО??"
        "Прищепки для белья?
        Деревянные???"

        "Юлия этим пользуется???"

        if clothesPinsSeen == False:
            menu:
                "Юлия деревенщина":
                    call EP1_bitch(5, "julia_basement_pins")
                    m "Из какой провинциальной дыры вылезла эта нерадивая служанка?"
                    "Нужны-ли мне такие работники?
                    Большой вопрос!"

                "Юлия пользуется раритетными вещами":
                    call EP1_bitch(-5, "julia_basement_pins")
                    m "Хм.. У Юлии есть определенный вкус к раритетным вещам.
                    Я тоже люблю все раритетное, но только роскошное."

                    "А эти прищепки...
                    Ну, не знаю..."

            $ clothesPinsSeen = True

    if obj_name == "Basket1":
        m "Эта корзина пустая."
    if obj_name == "Basket2":
        m "Мне не дотянуться до этих корзин.
        Что там в них?"
    if obj_name == "Washer":
        m "Машина для сушки белья..."
        "Пустая..."
    if obj_name == "Cloth1":
        m "Какие-то тряпки.
        Я не могу назвать это одеждой."
        "Наверное это что-то из одежды Юлии.
        Фи!"
    if obj_name == "Rags1":
        m "Какие-то тряпки.
        Это явно не мое платье!"
    if obj_name == "Toilet_Paper":
        m "Туалетная бумага?!
        И я тянулась туда чтобы об этом узнать?!"
    if obj_name == "Towels1":
        m "Какие-то полотенца, но мне толком не разглядеть отсюда."
    if obj_name == "Drying_Machine":
        m "Судя по всему это стиральная машина..."
        "Пустая..."

    return

label EP1_basement_laundry_first_visit:
    m "Это прачечная."
    m "Здесь гувернантка занимается своей работой."
    m"Я не понимаю что Я здесь забыла???"
    $ laundryVisited = True
    return

label EP1_basement_laundry_dress_visit:
    m "Хммм.. прачечная."

    "Возможно где-то здесь я найду свое платье..."

    call EP1_question_helper_enable("question_helper_laundry")


    return
