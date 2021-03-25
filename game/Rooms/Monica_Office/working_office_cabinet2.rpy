default workingOfficeCabinet2MonicaSuffix = 1

label working_office_cabinet2:
    $ print "enter_working_office_cabinet2"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_1

    $ scene_image = "scene_WorkingOfficeCabinet2[day_suffix]"
    music Stealth_Groover
    return

label working_office_cabinet2_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "WorkingOfficeCabinet2_Monica[workingOfficeCabinet2MonicaSuffix]_[cloth][day_suffix]", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":10}, scene="working_office_cabinet2")


    $ add_object_to_scene("Books1", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books1", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books2", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books2", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books3", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books3", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books4", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books4", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books5", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books5", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books6", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books6", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books7", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books7", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Books8", {"type" : 2, "base" : "WorkingOfficeCabinet2_Books8", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")

    $ add_object_to_scene("Chair", {"type" : 2, "base" : "WorkingOfficeCabinet2_Chair", "click" : "working_office_cabinet2_environment", "actions" : "lw", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Cup", {"type" : 2, "base" : "WorkingOfficeCabinet2_Cup", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("JuliaFolders", {"type" : 2, "base" : "WorkingOfficeCabinet2_JuliaFolders", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Lamp1", {"type" : 2, "base" : "WorkingOfficeCabinet2_Lamp1", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Lamp2", {"type" : 2, "base" : "WorkingOfficeCabinet2_Lamp2", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Picture", {"type" : 2, "base" : "WorkingOfficeCabinet2_Picture", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Sofa1", {"type" : 2, "base" : "WorkingOfficeCabinet2_Sofa1", "click" : "working_office_cabinet2_environment", "actions" : "lw", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("Sofa2", {"type" : 2, "base" : "WorkingOfficeCabinet2_Sofa2", "click" : "working_office_cabinet2_environment", "actions" : "lw", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")


    $ add_object_to_scene("TableBook", {"type" : 2, "base" : "WorkingOfficeCabinet2_TableBook", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")
    $ add_object_to_scene("TableFlower", {"type" : 2, "base" : "WorkingOfficeCabinet2_TableFlower", "click" : "working_office_cabinet2_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet2")

    $ add_object_to_scene("Teleport_Working_Office_Cabinet", {"type":3, "text" : t_("РАБОЧЕЕ МЕСТО"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "working_office_cabinet2_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="working_office_cabinet2")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label working_office_cabinet2_teleport:
    if obj_name == "Teleport_Working_Office_Cabinet":
        if day_time == "day":
            $ workingOfficeCabinetMonicaSuffix = 7
        else:
            $ workingOfficeCabinetMonicaSuffix = 1
        call change_scene("working_office_cabinet") from _call_change_scene_307
        return
    return
label working_office_cabinet2_environment:
    if obj_name == "Monica":
        mt "А здесь уютно..."
    if obj_name == "Books1" or obj_name == "Books2" or obj_name == "Books3" or obj_name == "Books4" or obj_name == "Books5" or obj_name == "Books6" or obj_name == "Books7" or obj_name == "Books8":
        mt "Бесполезная литература..."
        mt "Тщетное навязывание видимости интеллекта..."
    if obj_name == "Cup":
        mt "Здесь нет еды, но, по крайней мере, я могу пить кофе сколько захочу..."
    if obj_name == "Lamp1":
        mt "Забавная лампа..."
        mt "Я люблю лампы..."
    if obj_name == "Lamp2":
        mt "Эти кувшины сделаны лампочками..."
        mt "Очень симпатично..."
    if obj_name == "TableBook" or obj_name == "TableFlower":
        mt "Мило..."
    if obj_name == "Picture":
        mt "Я не понимаю что там изображено..."
        if monicaBitch == True:
            mt "А это значит, что там нет ничего стоящего..."
    if obj_name == "Chair":
        if act=="l":
            mt "Этот стул жесткий и неудобный."
        if act=="w":
            mt "Наверняка здесь найдется что-то поудобнее!"
    if obj_name == "Sofa1":
        if act=="l":
            mt "Хоть я и худенькая, но этот диван несколько тесноват..."
        if act=="w":
            mt "Я туда не помещусь, может прилечь на тот большой?"
    if obj_name == "Sofa2":
        if act=="l" or workingOfficeCabinet2MonicaSuffix == 2:
            mt "Какой уютный диванчик..."
            return
        if act=="w":
            $ workingOfficeCabinet2MonicaSuffix = 2
            call refresh_scene("Dissolve_05") from _call_refresh_scene_12
            $ autorun_to_object("ep26_dialogues6_office2_monica_sofa", scene="working_office_cabinet2")
            return

    return
