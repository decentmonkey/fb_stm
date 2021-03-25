default workingOfficeMonicaSuffix = ""

label working_office:
    $ print "enter_working_office"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_10

    $ scene_image = "scene_WorkingOffice[day_suffix]"
    music Stealth_Groover
    return

label working_office_init:

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "WorkingOffice_Monica[workingOfficeMonicaSuffix]_[cloth]", "click" : "working_office_environment", "actions" : "l", "zorder":10}, scene="working_office")

    $ add_object_to_scene("Worker1", {"type" : 2, "base" : "WorkingOffice_w1", "click" : "working_office_environment", "actions" : "lt", "zorder":5, "group":"workers"}, scene="working_office")
    $ add_object_to_scene("Worker2", {"type" : 2, "base" : "WorkingOffice_w2", "click" : "working_office_environment", "actions" : "lt", "icon_t":"/Icons/talk" + res.suffix +".png", "zorder":5, "group":"workers"}, scene="working_office")
    $ add_object_to_scene("Worker3", {"type" : 2, "base" : "WorkingOffice_w3", "click" : "working_office_environment", "actions" : "lw", "zorder":5, "group":"workers"}, scene="working_office")
    $ add_object_to_scene("Worker4", {"type" : 2, "base" : "WorkingOffice_w4", "click" : "working_office_environment", "actions" : "lw", "zorder":5, "group":"workers"}, scene="working_office")
    $ add_object_to_scene("Worker5", {"type" : 2, "base" : "WorkingOffice_w5", "click" : "working_office_environment", "actions" : "lt", "icon_t":"/Icons/talk" + res.suffix +".png", "zorder":5, "group":"workers"}, scene="working_office")
    $ add_object_to_scene("Worker6", {"type" : 2, "base" : "WorkingOffice_w6", "click" : "working_office_environment", "actions" : "lw", "zorder":5, "group":"workers"}, scene="working_office")
    $ add_object_to_scene("Worker7", {"type" : 2, "base" : "WorkingOffice_w7", "click" : "working_office_environment", "actions" : "lw", "zorder":5, "group":"workers"}, scene="working_office")

    $ add_object_to_scene("Computer1", {"type" : 2, "base" : "WorkingOffice_Computer1", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")
    $ add_object_to_scene("Computer2", {"type" : 2, "base" : "WorkingOffice_Computer2", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")
    $ add_object_to_scene("Computer3", {"type" : 2, "base" : "WorkingOffice_Computer3", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")
    $ add_object_to_scene("Flower", {"type" : 2, "base" : "WorkingOffice_Flower", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")
    $ add_object_to_scene("Folders1", {"type" : 2, "base" : "WorkingOffice_Folders1", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")
    $ add_object_to_scene("Folders2", {"type" : 2, "base" : "WorkingOffice_Folders2", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")
    $ add_object_to_scene("Folders3", {"type" : 2, "base" : "WorkingOffice_Folders3", "click" : "working_office_environment", "actions" : "l", "zorder":0, "b":0.15, "group":"environment"}, scene="working_office")

    $ add_object_to_scene("Teleport_Cabinet", {"type" : 2, "base" : "WorkingOffice_Teleport_Cabinet", "click" : "working_office_teleport", "actions" : "lw", "zorder":0, "b":0.15, "teleport":True}, scene="working_office")


#    $ add_object_to_scene("Teleport_Monica_Office_Lift", {"type":3, "text" : t_("ЛИФТ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "working_office_teleport", "xpos" : 1730, "ypos" : 920, "zorder":11, "teleport":True}, scene="working_office")
#    $ add_object_to_scene("Teleport_Monica_Office_Lift", {"type":3, "text" : t_("ЛИФТ"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "working_office_teleport", "xpos" : 1790, "ypos" : 920, "zorder":11, "teleport":True}, scene="working_office")
    $ add_object_to_scene("Teleport_Monica_Office_Lift", {"type":3, "text" : t_("ЛИФТ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "working_office_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="working_office")
    $ add_object_to_scene("Teleport_Monica_WorkingOffice2", {"type":3, "text" : t_("ИДТИ ДАЛЬШЕ"), "rarrow" : "arrow_up_2", "base":"WorkingOffice_Teleport_WorkingOffice2", "click" : "working_office_teleport", "xpos" : 1310, "ypos" : 896, "zorder":3, "teleport":True}, scene="working_office")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label working_office_teleport:
    if obj_name == "Teleport_Monica_WorkingOffice2":
        call change_scene("working_office2") from _call_change_scene_327
        return
    if obj_name == "Teleport_Cabinet":
        if act=="l":
            mt "Это дверь в мой временный кабинет."
            mt "Пока я не верну себе мой кабинет наверху!"
        if act == "w":
            $ workingOfficeCabinetMonicaSuffix = 1
            call change_scene("working_office_cabinet") from _call_change_scene_328
            return
    return
label working_office_environment:
    if obj_name == "Monica":
        if monicaBitch == True:
            mt "Это какая-то дыра, наполненная бездельниками."
            mt "Но ничего, скоро я все верну назад и этот офис обязательно закрою."
        else:
            mt "Наконец-то у меня есть хоть какой-то офис!"
    if obj_name == "Computer1" or obj_name == "Computer2" or obj_name == "Computer3" or obj_name == "Computer4" or obj_name == "Computer5" or obj_name == "Computer6":
        mt "На этих компьютерах нет ничего хоть сколько-то стоящего."
        mt "Только бесполезные отчеты"
        if monicaBitch == True:
            mt "Может украсть один из них?"
            mt "Его бы можно было продать..."
            mt "Хотя нет... Слишком большой риск..."
    if obj_name == "Flower":
        mt "Надо же какой роскошный цветок."
        mt "Ему явно не место здесь."
        mt "Его надо будет переселить ко мне в кабинет!"
    if obj_name == "Folders1" or obj_name == "Folders2" or obj_name == "Folders3":
        mt "Папки с бесполезными отчетами!"

    if act=="w" and (obj_name == "Worker3" or obj_name == "Worker4" or obj_name == "Worker6" or obj_name == "Worker7"):
        call change_scene("working_office2") from _call_change_scene_329
        return

    if obj_name == "Worker1" or obj_name == "Worker2" or obj_name == "Worker3" or obj_name == "Worker4" or obj_name == "Worker5" or obj_name == "Worker6" or obj_name == "Worker7":
        call ep26_quests_office_workers1() from _call_ep26_quests_office_workers1


    return

#label Computer1_use_flash_card:
#label Computer2_use_flash_card:
#label Computer3_use_flash_card:
#label Computer4_use_flash_card:
#label Computer5_use_flash_card:
#label Computer6_use_flash_card:
#    mt "Компьютер требует пароль."
#    return
