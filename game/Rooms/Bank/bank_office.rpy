label bank_office:

    $ print "enter_bank_office"
    $ miniMapData = []
    $ scene_image = "scene_Bank_Clerks_[bankOfficeState]"

    return

label bank_office_init:
    $ api_scene_name = "bank_office"

    $ add_object_to_scene("Clerk_A", {"type":2, "base":"BANK_Clerks_[bankOfficeState]_a", "click" : "bank_office_environment", "actions" : "lt", "zorder" : 1})
    $ add_object_to_scene("Clerk_B", {"type":2, "base":"BANK_Clerks_[bankOfficeState]_b", "click" : "bank_office_environment", "actions" : "l", "zorder" : 1})

    $ add_object_to_scene("Chair2", {"type":2, "base":"Bank_Office_Chair2", "click" : "bank_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Monitor1", {"type":2, "base":"Bank_Office_Monitor1", "click" : "bank_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Monitor2", {"type":2, "base":"Bank_Office_Monitor2", "click" : "bank_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Folder1", {"type":2, "base":"Bank_Office_Folder1", "click" : "bank_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Folder2", {"type":2, "base":"Bank_Office_Folder2", "click" : "bank_office_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "bank_office_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "teleport":True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label bank_office_teleport:
    if obj_name == "Teleport_Street":
        call change_scene("street_bank", "Fade_long") from _call_change_scene_107
        return
    return
label bank_office_environment:
    if obj_name == "Chair1" or obj_name == "Chair2":
        if obj_data["action"] == "l":
            return
    if obj_name == "Monitor1" or obj_name == "Monitor2":
        mt "Дешевые компьютеры.
        За которыми сидят дешевые люди, выполняющие дешевую работу."
        "Фи!"
    if obj_name == "Folder1" or obj_name == "Folder2":
        mt "Эти клерки целыми днями роются в бумагах, как крысы."
    if obj_name == "Clerk_A":
        if obj_data["action"] == "l":
            pass
        if obj_data["action"] == "t":
            return
    if obj_name == "Clerk_B":
        mt "Эта клерк выглядит еще более глупой..."
    return
