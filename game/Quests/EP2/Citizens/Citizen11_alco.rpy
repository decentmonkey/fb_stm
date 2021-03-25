default vodkaTaken = False

label take_trash_bottle:
    #img #моника смотрит на помойку и видит бутыль. Ей кажетсячто она полная(она ее видитт только на половину)
    img 8481
    with fade
    if act == "l":
        m "Похоже кто-то выкинул бутылку водки... Может ли она мне пригодиться?"
        return
    m "Похоже кто-то выкинул бутылку водки... Может ли она мне пригодиться?"
    menu:
        "Взять бутылку.":
            sound bottle1
            img 8482
            with fade
            mt "Не знаю зачем, но думаю она может пригодиться."
            #img моника берет бутылку, попутно на нее может что-то упасть, либо она за ней будет наклоняться,
            #но тогда не понятно как обыграть, что бутылка кажется полной.
            img 8483
            with fade
            m "Черт! Из нее уже кто-то пил!"
            #тут опять же хз: можно добавить диалог аля Оставить себе или Выкинуть, но стоит ли загружать игру диалогами с выбором
            menu:
                "Оставить бутылку себе.":
                    m "Ну и ладно, оставлю ее у себя, вдруг пригодится."
                    sound bottle1
                    #take bottle
                    $ vodkaTaken = True
                    $ define_inventory_object("vodka", {"description" : t_("Водка"), "label_suffix" : "_use_bottle", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/vodka" + res.suffix + ".png"})
                    $ add_inventory("vodka", 1, True)
                    $ set_active("Bottle", False, scene="hostel_edge_1_b")
#    if check_inventory("vodka"):
                    pass
                "Поставить бутылку на место.":
                    mt "Оставлю бутылку здесь. Мне ни к чему это пойло!"
                    sound bottle1
                    return
        "Не брать.":
            m "Ну уж нет, я не собираюсь лазать по помойкам!"
    call refresh_scene_fade() from _call_refresh_scene_fade_58
    return
