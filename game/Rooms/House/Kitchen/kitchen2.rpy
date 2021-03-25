label kitchen2:
    if EP1==True:
        jump kitchen2_EP1
    $ print "enter_kitchen2"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate

    $ scene_image = "scene_Kitchen2[day_suffix]"
    music Mandeville
    return

label kitchen2_init:
    if EP1==True:
        return
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Kitchen2_Monica_[cloth]", "click" : "kitchen_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Accessories", {"type":2, "base":"Kitchen2_Accessories", "click" : "kitchen2_environment", "actions" : "l", "zorder": 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Cupboard", {"type":2, "base":"Kitchen2_Cupboard", "click" : "kitchen2_environment", "actions" : "l", "zorder": 0, "group":"environment"})
    $ add_object_to_scene("Chair1", {"type":2, "base":"Kitchen2_Chair1", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Kitchen2_Chair2", "click" : "kitchen2_environment", "actions" : "lh", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chandelier", {"type":2, "base":"Kitchen2_Chandelier", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "b":0.15, "group":"environment"})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Kitchen2_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.2, "group":"environment"})
    $ add_object_to_scene("Dinner_Table", {"type":2, "base":"Kitchen2_Dinner_Table", "click" : "kitchen2_environment", "actions" : "lh", "zorder" : 11, "group":"environment"})
    $ add_object_to_scene("Food", {"type":2, "base":"Kitchen2_Food", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Fridge", {"type":2, "base":"Kitchen2_Fridge", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":0.2, "c":1.8, "group":"environment"})
    $ add_object_to_scene("Sink", {"type":2, "base":"Kitchen2_Sink", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Small_Chairs", {"type":2, "base":"Kitchen2_Small_Chairs", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type":2, "base":"Kitchen2_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.03, "group":"environment"})

    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "kitchen_teleport", "xpos" : 210, "ypos" : 520, "zorder":11})
    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":12, "teleport":True})

    return

label kitchen2_environment:
    if EP1==True:
        jump kitchen2_environment_EP1
    if monicaKitchenForbidden == True:
        if get_active_objects("Betty", scene="House", recursive=True) != False:
            call afterJailHouse_dialogue15a() from _call_afterJailHouse_dialogue15a
            return
        call ep22_dialogue1_5_kitchen() from _call_ep22_dialogue1_5_kitchen
        return
    return




# EP1




label kitchen2_EP1:
    $ print "enter_kitchen2"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_15

    $ scene_name = "kitchen2"
    $ scene_caption = t_("Kitchen")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Kitchen2_Monica_" + cloth + day_suffix

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Kitchen2_Monica_" + cloth, "click" : "kitchen_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Accessories", {"type":2, "base":"Kitchen2_Accessories", "click" : "kitchen2_environment", "actions" : "l", "zorder": 0, "b":0.15})
    $ add_object_to_scene("Cupboard", {"type":2, "base":"Kitchen2_Cupboard", "click" : "kitchen2_environment", "actions" : "l", "zorder": 0})
    $ add_object_to_scene("Chair1", {"type":2, "base":"Kitchen2_Chair1", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Kitchen2_Chair2", "click" : "kitchen2_environment", "actions" : "lh", "zorder" : 0})
    $ add_object_to_scene("Chandelier", {"type":2, "base":"Kitchen2_Chandelier", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Kitchen2_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.2})
    $ add_object_to_scene("Dinner_Table", {"type":2, "base":"Kitchen2_Dinner_Table", "click" : "kitchen2_environment", "actions" : "lh", "zorder" : 11})
    $ add_object_to_scene("Food", {"type":2, "base":"Kitchen2_Food", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fridge", {"type":2, "base":"Kitchen2_Fridge", "click" : "kitchen_environment", "actions" : "l", "zorder" : 0, "b":0.2, "c":1.8})
    $ add_object_to_scene("Sink", {"type":2, "base":"Kitchen2_Sink", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Small_Chairs", {"type":2, "base":"Kitchen2_Small_Chairs", "click" : "kitchen2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Windows", {"type":2, "base":"Kitchen2_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.03})

    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : t_("КУХНЯ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "kitchen_teleport", "xpos" : 210, "ypos" : 520, "zorder":11})
    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "kitchen_teleport", "xpos" : 960, "ypos" : 956, "zorder":12})

    return

label kitchen2_environment_EP1:
    if gameStage > 2:
        if monicaKitchenForbidden == False:
            call afterJailHouse_dialogue12() from _call_afterJailHouse_dialogue12_1
            return
        else:
            mt "Бетти запретила мне притрагиваться к чему-либо..."
            "Мне лучше уйти отсюда скорее, пока она не заметила меня!"
            return
    if obj_name == "Cupboard":
        m "В этих сервантах хранится посуда."

        "Красивая и дорогая!"

    if obj_name == "Accessories":
        m "Здесь висит разная кухонная утварь."

        "Естественно - ЧИСТАЯ и намытая до БЛЕСКА!"

    if obj_name == "Chair1":
        m "Я никогда не сажусь обедать за этот стул, потому что над ним висит эта красивая и роскошная люстра."

        "Я разрешаю своему мужу сидеть здесь."

    if obj_name == "Chair2":
        if obj_data["action"] == "l":
            m "За этим стулом я обычно обедаю."

            "Он.. стоит подальше от этой красивой и дорогой люстры..."

        if obj_data["action"] == "h":
            call eat() from _call_eat

    if obj_name == "Chandelier":
        m "Ах, как я люблю красивые и роскошные люстры!"

    if obj_name == "Dinner_Table":
        if obj_data["action"] == "l":
            m "Обеденный столик."

            "Я могла бы обедать в нашей роскошной гостиной."

            "Но я считаю что в этом слишком много пафоса."

            "Ведь я же скромняшка!"

            "Да, и я в детстве всегда кушала на кухне."

            "Наверное эта привычка - оттуда."
        if obj_data["action"] == "h":
            call eat() from _call_eat_1

    if obj_name == "Sink":
        m "В этой раковине Юлия моет посуду."

        "Я не разрешаю пользоваться посудомоечной машиной, потому что..."

        "Это химия и это упростило бы ей работу."

        "Упрощать работу людям - не есть моя цель!"

        "Считаю что я и так слишком добрая ко всем!"

    if obj_name == "Small_Chairs":
        m "Эти стулья Юлия использует для того чтобы встать на них и куда-то дотянуться."

        "Естественно, на них никто не сидит."

        "Я бы не допустила здесь находиться никому."

        "Я даже мужу сюда не разрешаю заходить, только чтобы поесть."

        "Хотя.. я стараюсь чтобы он вообще поменьше заходил куда-либо в доме."

        "Я считаю что этот дом - МОЙ!"


    return
