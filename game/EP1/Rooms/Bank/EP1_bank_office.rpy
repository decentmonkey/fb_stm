default bankOfficeState = 1
default clerksOffended = False

label EP1_bank_office:

    $ print "enter_bank_office"
    $ miniMapData = []

    $ scene_name = "bank_office"
    $ scene_caption = t_("BANK")
    $ clear_scene_from_objects(scene_name)
    if clerksOffended == False:
        $ scene_image = "scene_Bank_Clerks_1"
        $ EP1_add_object_to_scene("Clerk_A", {"type":2, "base":"BANK_Clerks_1_a", "click" : "EP1_bank_office_environment", "actions" : "lt", "zorder" : 1})
        $ EP1_add_object_to_scene("Clerk_B", {"type":2, "base":"BANK_Clerks_1_b", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 1})
    else:
        $ scene_image = "scene_Bank_Clerks_" + str(bankOfficeState)
        $ EP1_add_object_to_scene("Clerk_A", {"type":2, "base":"BANK_Clerks_" + str(bankOfficeState) + "_a", "click" : "EP1_bank_office_environment", "actions" : "lt", "zorder" : 1})
        $ EP1_add_object_to_scene("Clerk_B", {"type":2, "base":"BANK_Clerks_" + str(bankOfficeState) + "_b", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 1})


    if bankOfficeState == 1:
        $ EP1_add_object_to_scene("Chair1", {"type":2, "base":"Bank_Office_Chair1", "click" : "EP1_bank_office_environment", "actions" : "lh", "zorder" : 0})
    else:
        $ EP1_add_object_to_scene("Chair1", {"type":2, "base":"Bank_Office_Chair1", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Chair2", {"type":2, "base":"Bank_Office_Chair2", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Monitor1", {"type":2, "base":"Bank_Office_Monitor1", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Monitor2", {"type":2, "base":"Bank_Office_Monitor2", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Folder1", {"type":2, "base":"Bank_Office_Folder1", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Folder2", {"type":2, "base":"Bank_Office_Folder2", "click" : "EP1_bank_office_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_bank_office_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_bank_office_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street":
        if bankOfficeState < 2:
            imgc Dial_Monica_BusinessCloth2_Thinking
            mt "Я еще не разобралась с Банком."
            return
        if bankOfficeState < 3:
            $ bankOfficeState = 3
        call EP1_change_scene("street_bank", "Fade_long")
        return
    return
label EP1_bank_office_environment(obj_name, obj_data):
    if obj_name == "Chair1" or obj_name == "Chair2":
        if obj_data["action"] == "l":
            mt "Какой-то дешевый офисный стул!"
            "И они предлагают сидеть в этом стуле таким VIP персонам как Я?!"
        if obj_data["action"] == "h":
            call EP1_bank_office_talk1()
            return

    if obj_name == "Monitor1" or obj_name == "Monitor2":
        mt "Дешевые компьютеры.
        За которыми сидят дешевые люди, выполняющие дешевую работу."
        "Фи!"
    if obj_name == "Folder1" or obj_name == "Folder2":
        mt "Эти клерки целыми днями роются в бумагах, как крысы."
    if obj_name == "Clerk_A":
        if obj_data["action"] == "l":
            mt "Интересно. Это у нее свой цвет волос?"
            "Больше похоже на дешевую краску."
            "Или на дешевые волосы...
            Хи-хи..."
        if obj_data["action"] == "t":
            if bankOfficeState == 1:
                call EP1_bank_office_talk1()
                return
            if bankOfficeState == 2 or bankOfficeState == 3:
                if clerksOffended == False:
                    call EP1_bank_office_talk2_not_offended()
                else:
                    call EP1_bank_office_talk2()
                return
    if obj_name == "Clerk_B":
        mt "Эта клерк выглядит еще более глупой..."

    return
