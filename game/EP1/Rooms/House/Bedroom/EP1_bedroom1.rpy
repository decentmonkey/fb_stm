label EP1_bedroom1:
    $ print "enter_bedroom1"
    $ miniMapData = []
    call EP1_miniMapHouseGenerate()
    $ miniMapSubst["all"] = "miniMapBedroomCheckCloth"

    $ scene_name = "bedroom1"
    $ scene_caption = t_("Bedroom")
    $ scene_image = "scene_Bedroom1_Monica_" + cloth + day_suffix
    $ clear_scene_from_objects(scene_name)

    if gameStage <= 2:
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom1_Monica_" + cloth, "click" : "EP1_monica_show_cloth", "actions" : "l", "zorder":10})
    if gameStage > 2:
        $ EP1_add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom1_Monica_" + cloth, "click" : "EP1_bedroom2_environment", "actions" : "l", "zorder":10})

    if bettyLocation == "Bedroom1":
        if day_time == "day":
            $ EP1_add_object_to_scene("Betty", {"type" : 2, "base" : "Bedroom1_Betty", "click" : "EP1_bettyInteract1", "actions" : "lt", "zorder":10})

    $ EP1_add_object_to_scene("Chair", {"type":2, "base":"Bedroom1_Chair", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair2", {"type":2, "base":"Bedroom1_Chair2", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Bed", {"type":2, "base":"Bedroom1_Bed", "click" : "EP1_bedroom1_environment", "actions" : "lh"})
    $ EP1_add_object_to_scene("Curtains", {"type":2, "base":"Bedroom1_Curtains", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flowers", {"type":2, "base":"Bedroom1_Flowers", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0, "b":0.12})
    $ EP1_add_object_to_scene("Lamp", {"type":2, "base":"Bedroom1_Lamp", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Mess", {"type":2, "base":"Bedroom1_Mess", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Mirror", {"type":2, "base":"Bedroom1_Mirror", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 11})
    $ EP1_add_object_to_scene("Table", {"type":2, "base":"Bedroom1_Table", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Windows", {"type":2, "base":"Bedroom1_Windows", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0, "c":1.0, "b":0.1})
    $ EP1_add_object_to_scene("Carpet", {"type":2, "base":"Bedroom1_Carpet", "click" : "EP1_bedroom1_environment", "actions" : "l", "zorder" : 0})

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3
    $ EP1_add_object_to_scene("Teleport_Bedroom2", {"type":3, "text" : t_("ГАРДЕРОБ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "EP1_bedroom1_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11})


    return
#    jump EP1_show_scene



label EP1_bedroom1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bedroom2":
        call EP1_change_scene("bedroom2")
    return

label EP1_bedroom1_environment(name, obj_data):
    if name == "Chair":
        if gameStage > 2:
            mt "Мой любимый удобный стул... Эхххх...."
            return
        $ action_name = obj_data["action"]
        m "Мой стул..."

        "Он очень удобный.
        Я люблю сидеть в нем и листать свежую прессу."

        "Свежая пресса - это обычно свежие издания моих журналов.
        Хи-хи."

    if name == "Chair2":
        if gameStage > 2:
            mt "Один из моих бывших стульев..."
            return
        m "На этом стуле я обычно не сижу..."

        "На нем никто не сидит."

        "Вернее сидит муж... иногда..."

        "В общем эта вещь явно лишняя в моей спальне."

    if name == "Bed":
        if gameStage > 2:
            mt "Моя любимая кроватка!"
            "Она такая удобная!"
            "Как я скучаю по ней!"
            "Я ВЕРНУ ЕЕ!!!"
            return
        m "Моя любимая кроватка..."

        "Когда я в ней сплю, мне всегда снятся хорошие сны."

    if name == "Curtains":
        if gameStage > 2:
            mt "Я помню как эти шторы спасали меня от солнечного света..."
            return
        m "Эти шторы довольно плотные, однако они не спасают меня от утреннего солнца."

    if name == "Flowers":
        if gameStage > 2:
            mt "Мои цветы! Мои любимые цветы!"
            return
        m "Я люблю цветы.
        Особенно красивые цветы.
        Мне нравится как они украшают мою комнату."

        "Они называются..."

        "Называются..."

        "Она называются 'Красивые Цветы', точно!!!"

    if name == "Lamp":
        if gameStage > 2:
            mt "Я помню каждую лампу в моем доме..."
            return
        m "Да, эта лампа горит."

        "В моем доме всегда горит свет.
        Свет украшает интерьер."

        "Счета за электричество?
        Вы про что?
        Я богата!
        Я не знаю что такое счета за электричество!"

    if name == "Mess":
        if gameStage > 2:
            mt "Я складывала сюда свои длинные ножки..."
            "Красивые, не то что у этой Бетти!"
            return
        m "У меня длинные ноги, но я их не складываю сюда когда сплю."

        "Я использую это место когда переодеваюсь."

    if name == "Mirror":
        if gameStage > 2:
            mt "Я уверена что я скоро увижу себя в этом зеркале снова в дорогом платье!"
            return
        m "Зеркало."

        "В моем доме много зеркал.
        Я их люблю."

        "Зеркала не любят только те кому не нравится свое отражение в них."

    if name == "Table":
        if gameStage > 2:
            mt "Этот столик такой романтичный."
            "Я оставлю его после того как сменю дизайн этого дома."
            return
        m "Этот столик такой романтичный.
        Я люблю романтику."

        "В моей жизни мало романтики.
        Мое положение в обществе накладывает определенные ограничения."

        "Но меня это не беспокоит.
        Власть я люблю гораздо больше романтики."

    if name == "Windows":
        if gameStage > 2:
            mt "Я помню вид из своего окна..."
            return
        if day_time == "day":
            m "Эти окна такие солнечные!"

            "Мне это нравится!
            Правда солнце будит меня по утрам."

            "А я люблю поспать.
            Не знаю как вы!"

        if day_time == "evening":
            m "За окнами темно."

            "Уже вечер!"

    if name == "Carpet":
        if gameStage > 2:
            mt "Мой коврик..."
            return
        m "Коврик.
        Я люблю коврики.
        Коврики - это мило."

        "Помню когда-то в детстве я испачкала ковер."

        "Меня сильно ругали за это."

    elif name == "none":
        "none ((("

    return

label EP1_teleport_label1(name, obj_data):
    "teleport!"

    return

label EP1_Bed_hand(name, obj_data):
    call EP1_check_sleep()
    return _return
