default workingOfficeCabinetMonicaSuffix = 1
default workingOfficeCabinetJuliaSuffix = 1

default workingOfficeCabinetItem10Viewed = False

default workingOfficeCabinetMonicaChairEnabled = False

default workingOfficeSkipMusicOneTime = False

label working_office_cabinet:
    $ print "enter_working_office_cabinet"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_9

    # Стул неактивен, когда Моника на нем сидит
#    if workingOfficeCabinetMonicaSuffix == 1 or workingOfficeCabinetMonicaSuffix == 4:
    if workingOfficeCabinetMonicaSuffix == 1 or workingOfficeCabinetMonicaSuffix == 6 or workingOfficeCabinetMonicaSuffix == 7:
        $ workingOfficeCabinetMonicaChairEnabled = True
    else:
        $ workingOfficeCabinetMonicaChairEnabled = False

    if day_time == "day" and (workingOfficeCabinetMonicaSuffix == 4 or workingOfficeCabinetMonicaSuffix == 5):
        $ workingOfficeCabinetMonicaSuffix = 3

    $ scene_image = "scene_WorkingOfficeCabinet[day_suffix]"

    if workingOfficeSkipMusicOneTime == False:
        music Stealth_Groover
    $ workingOfficeSkipMusicOneTime = False
    return

label working_office_cabinet_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "WorkingOfficeCabinet_Monica[workingOfficeCabinetMonicaSuffix]_[cloth][day_suffix]", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":10}, scene="working_office_cabinet")

    $ add_object_to_scene("Julia", {"type" : 2, "base" : "WorkingOfficeCabinet_Julia[workingOfficeCabinetJuliaSuffix][day_suffix]", "click" : "working_office_cabinet_environment", "actions" : "lt", "zorder":5}, scene="working_office_cabinet")

    $ add_object_to_scene("MonicaChair", {"type" : 2, "base" : "WorkingOfficeCabinet_MonicaChair", "click" : "working_office_cabinet_environment", "actions" : "lw", "zorder":5, "group":"environment"}, {"workingOfficeCabinetMonicaChairEnabled":{"v":False, "active":False}}, scene="working_office_cabinet")
    $ add_object_to_scene("MonicaTable", {"type" : 2, "base" : "WorkingOfficeCabinet_MonicaTable", "click" : "working_office_cabinet_environment", "actions" : "lh", "zorder":5, "group":"environment"}, scene="working_office_cabinet")


    $ add_object_to_scene("Calendar", {"type" : 2, "base" : "WorkingOfficeCabinet_Calendar", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Chair1", {"type" : 2, "base" : "WorkingOfficeCabinet_Chair1", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Chair2", {"type" : 2, "base" : "WorkingOfficeCabinet_Chair2", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")

    $ add_object_to_scene("Item1", {"type" : 2, "base" : "WorkingOfficeCabinet_Item1", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item2", {"type" : 2, "base" : "WorkingOfficeCabinet_Item2", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item3", {"type" : 2, "base" : "WorkingOfficeCabinet_Item3", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item4", {"type" : 2, "base" : "WorkingOfficeCabinet_Item4", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item5", {"type" : 2, "base" : "WorkingOfficeCabinet_Item5", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item6", {"type" : 2, "base" : "WorkingOfficeCabinet_Item6", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item7", {"type" : 2, "base" : "WorkingOfficeCabinet_Item7", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item8", {"type" : 2, "base" : "WorkingOfficeCabinet_Item8", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item9", {"type" : 2, "base" : "WorkingOfficeCabinet_Item9", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item10", {"type" : 2, "base" : "WorkingOfficeCabinet_Item10", "click" : "working_office_cabinet_environment", "actions" : "lh", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item11", {"type" : 2, "base" : "WorkingOfficeCabinet_Item11", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Item12", {"type" : 2, "base" : "WorkingOfficeCabinet_Item12", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")

    $ add_object_to_scene("JuliaComputer", {"type" : 2, "base" : "WorkingOfficeCabinet_JuliaComputer", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("JuliaFolders", {"type" : 2, "base" : "WorkingOfficeCabinet_JuliaFolders", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")

    $ add_object_to_scene("MonicaComputer", {"type" : 2, "base" : "WorkingOfficeCabinet_MonicaComputer", "click" : "working_office_cabinet_environment", "actions" : "lh", "zorder":5, "group":"environment"}, scene="working_office_cabinet")

    $ add_object_to_scene("Picture", {"type" : 2, "base" : "WorkingOfficeCabinet_Picture", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Requisite", {"type" : 2, "base" : "WorkingOfficeCabinet_Requisite", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")
    $ add_object_to_scene("Tree", {"type" : 2, "base" : "WorkingOfficeCabinet_Tree", "click" : "working_office_cabinet_environment", "actions" : "l", "zorder":5, "group":"environment"}, scene="working_office_cabinet")

    $ add_object_to_scene("Teleport_WorkingOffice_Cabinet2", {"type":3, "text" : t_("ЗОНА ОТДЫХА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "working_office_cabinet_teleport", "xpos" : 220, "ypos" : 845, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="working_office_cabinet")
    $ add_object_to_scene("Teleport_Monica_WorkingOffice", {"type":3, "text" : t_("ВЫЙТИ К РАБОТНИКАМ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "working_office_cabinet_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True}, scene="working_office_cabinet")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label working_office_cabinet_teleport:
    if obj_name == "Teleport_Monica_WorkingOffice":
        call change_scene("working_office") from _call_change_scene_325
        return
    if obj_name == "Teleport_WorkingOffice_Cabinet2":
        $ workingOfficeCabinet2MonicaSuffix = 1
        call change_scene("working_office_cabinet2") from _call_change_scene_326
        return
    return
label working_office_cabinet_environment:
    if obj_name == "Monica":
        mt "Приятно снова почувствовать себя Боссом..."
    if obj_name == "Julia":
        if act=="l":
            call ep26_dialogues6_office2_monica_julia() from _call_ep26_dialogues6_office2_monica_julia
        return

    if obj_name == "Item1" or obj_name == "Item2" or obj_name == "Item3" or obj_name == "Item4" or obj_name == "Item5" or obj_name == "Item6" or obj_name == "Item7" or obj_name == "Item8" or obj_name == "Item9" or obj_name == "Item11" or obj_name == "Item12":
        mt "Безвкусный декор."
        mt "Не знаю от кого это досталось... Я бы оформила все по другому!"
        mt "Но я не буду ничего переделывать. Я не собираюсь надолго задерживаться здесь!"
    if obj_name == "Item10":
        if act=="l" or (act=="h" and workingOfficeCabinetItem10Viewed == False):
            mt "Камера?"
            mt "Похоже, что она сломана и выполняет роль декора."
            $ workingOfficeCabinetItem10Viewed = True
            return
        if act=="h":
            mt "Она сломана."
            mt "Зачем мне ее брать?"
    if obj_name == "Calendar":
        mt "Календарь..."
        mt "Даже не хочу смотреть."
        mt "Не хочу знать сколько уже продолжается этот кошмар..."
    if obj_name == "Chair1" or obj_name == "Chair2":
        if monicaBitch == True:
            mt "Эти стулья для аудиенции у Босса?"
            mt "Я не буду никому разрешать сидеть в присутствии МЕНЯ!"
        else:
            mt "Хм... Стулья..."
    if obj_name == "JuliaComputer":
        mt "На Юлином компьютере бесполезные отчеты."
        mt "Там нет ничего что может мне помочь."
    if obj_name == "JuliaFolders":
        mt "Юлия занимается бесполезными отчетами."
        if monicaBitch == True:
            mt "Лучше бы она работала Гувернанткой."
            mt "Все-равно у нее нет шансов приблизиться к моему уровню!"
            mt "Кто Я и кто она?!"
            mt "Фи!"
    if obj_name == "MonicaComputer":
        if act=="l":
            if day_time == "day":
                img 20289
            else:
                img 20290
            with fade
            mt "Компьютер не работает."
            mt "Я не удивлена."
            mt "Биф не хочет, чтобы я имела доступ хоть к чему-то ценному..."
        if act=="h":
            if day_time == "day":
                img 20289
            else:
                img 20290
            with fade
            mt "Компьютер сломан! Биф следит за тем, чтобы я никак не помешала его власти..."
            if monicaBitch == True:
                mt "Наивный дурачок... Он не знает с кем связался..."
        call refresh_scene_fade() from _call_refresh_scene_fade_148
        return


    if obj_name == "Picture":
        mt "А мне нравится эта картина, хоть это и странно..."
    if obj_name == "Tree":
        mt "Какое чудное деревце..."
        mt "Оно будет неплохо смотреться с тем цветком из офисов..."
    if obj_name == "MonicaChair":
        if act=="l":
            mt "Кресло Босса."
            mt "Мое кресло..."
        if act=="w":
            $ rand1 = random.choice([2,3])
            $ workingOfficeCabinetMonicaSuffix = rand1
            $ autorun_to_object("office_work_begin_event", scene="working_office_cabinet")
            call refresh_scene("Dissolve_05") from _call_refresh_scene_13
            return
    if obj_name == "MonicaTable":
        if act=="l":
            mt "За этим столом я провожу свой рабочий день..."
        if act=="h":
            call office_work_begin_event() from _call_office_work_begin_event
            call refresh_scene_fade() from _call_refresh_scene_fade_149
            return

    if obj_name == "Requisite":
        mt "А это что?"
        mt "Какой-то телескоп или прожектор?"
        mt "..."
        mt "А может быть это скрытая камера?"
        mt "Точно!"
        mt "Биф следит за мной..."
        mt "Мерзавец..."
        mt "Но я догадалась о его намерениях. Он и не подозревает какая Я умная!"
    return
