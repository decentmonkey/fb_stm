#default dickOfficeCabinetStage = 0

default dickOfficeMonicaState = 2
default dickOfficeDickState = 4

label dick_office_cabinet:
    $ print "dick_office_cabinet"
    $ miniMapData = []

    $ scene_image = "scene_Office_Dick_Cabinet"
    return

label dick_office_cabinet_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Cabinet_Dick_Monica_Whore_[dickOfficeMonicaState]_Monica", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Office_Dick_Cabinet_Dick_Monica_Whore_[dickOfficeDickState]_Dick", "click" : "dick_office_cabinet_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.14, "s":1.3, "tint":[1.0, 1.0, 0.8]})

    $ add_object_to_scene("Book1", {"type":2, "base":"Office_Dick_Cabinet_Book1", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Book2", {"type":2, "base":"Office_Dick_Cabinet_Book2", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Bust", {"type":2, "base":"Office_Dick_Cabinet_Bust", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Chair1", {"type":2, "base":"Office_Dick_Cabinet_Chair1", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Office_Dick_Cabinet_Chair2", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Chair3", {"type":2, "base":"Office_Dick_Cabinet_Chair3", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Flower1", {"type":2, "base":"Office_Dick_Cabinet_Flower1", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Flower2", {"type":2, "base":"Office_Dick_Cabinet_Flower2", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Sculpture", {"type":2, "base":"Office_Dick_Cabinet_Sculpture", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Vase", {"type":2, "base":"Office_Dick_Cabinet_Vase", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})
    $ add_object_to_scene("Portrait", {"type":2, "base":"Office_Dick_Cabinet_Portrait", "click" : "dick_office_cabinet_environment", "actions" : "l", "zorder" : 0, "active":False, "group":"environment"})

    $ add_object_to_scene("Teleport_Secretary", {"type":3, "text" : t_("СЕКРЕТАРЬ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "dick_office_cabinet_teleport", "xpos" : 220, "ypos" : 545, "zorder":11, "teleport":True})

    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_cabinet_teleport:
    if obj_name == "Teleport_Secretary":
        call change_scene("dick_office_secretary") from _call_change_scene_152
        return
    return
label dick_office_cabinet_environment:
    if obj_name == "Monica":
        "Я не верю в то что происходит!!!"
        return
    if obj_name == "DickTheLawyer":
        if act == "l":
            mt "Мне надо как-то вырвать Дика из когтей этой сучки!"
#            mt "Вот он! Жирный ублюдок, за которым я столько бегала!"
            return
        if act == "t":
            return

    if obj_name == "Book1" or obj_name == "Book2":
        mt "Умные юридические книжки."
        "Дик в них зарылся."
        "Надеюсь с них будет толк в моем деле, иначе от них нет никакой пользы!"
    if obj_name == "Bust":
        img 3163
        with fade
        mt "Что это такое? Это ведь не Дик?"
        "Может это тот на кого он пытается быть похож?"
        "Ему до этого далеко!"
    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3":
        mt "Здесь столько стульев!"
        "Дик мог бы и предложить мне один!"
    if obj_name == "Flower1" or obj_name == "Flower2" or obj_name == "Vase":
        mt "Вазы, цвет..."
        "Откуда все это здесь?"
        "Явно чья-то женская рука..."
    if obj_name == "Sculpture":
        mt "Что это?"
    if obj_name == "Portrait":
        #render+
        #изображение фото секретарши в кабинете Дика
        img 5693
        with fade
        mt "ЧТО????"
        "ОНА?? ЗДЕСЬ?!?!"
    return
