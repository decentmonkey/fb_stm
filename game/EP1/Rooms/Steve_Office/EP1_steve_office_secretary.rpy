default steveSecretaryOffended = False
default steveSecretaryFireOffended = False
default steveSecretaryTalkAfterCatch = False
default steveSecretaryExitTalkAfterCatch = False
default steveSecretaryFireOffended2 = False

label EP1_steve_office_secretary:

    $ print "enter_steve_office_secretary"
    $ miniMapData = []

    $ scene_name = "steve_office_secretary"
    $ scene_caption = t_("STEVE'S SECRETARY")
    $ clear_scene_from_objects(scene_name)
    if steveSecretaryOffended == False:
        $ scene_image = "scene_Steve_Office_Secretary_Monica_" + cloth
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Secretary_Monica_" + cloth, "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 1})
        $ EP1_add_object_to_scene("Secretary", {"type":2, "base":"Steve_Office_Secretary_Char1", "click" : "EP1_steve_office_secretary_environment", "actions" : "lt", "zorder" : 1})
    else:
        $ scene_image = "scene_Steve_Office_Secretary_Monica2_" + cloth
        $ EP1_add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Secretary_Monica2_" + cloth, "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 1})
        $ EP1_add_object_to_scene("Secretary", {"type":2, "base":"Steve_Office_Secretary_Char2", "click" : "EP1_steve_office_secretary_environment", "actions" : "lt", "zorder" : 1})


    $ EP1_add_object_to_scene("Monitor", {"type":2, "base":"steve_office_secretary_Monitor", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Folders1", {"type":2, "base":"steve_office_secretary_Folders1", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Folders2", {"type":2, "base":"steve_office_secretary_Folders2", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flower1", {"type":2, "base":"steve_office_secretary_Flower1", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flower2", {"type":2, "base":"steve_office_secretary_Flower2", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flower3", {"type":2, "base":"steve_office_secretary_Flower3", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})
    $ EP1_add_object_to_scene("Flower4", {"type":2, "base":"steve_office_secretary_Flower4", "click" : "EP1_steve_office_secretary_environment", "actions" : "l", "zorder" : 0})

    $ EP1_add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "EP1_steve_office_secretary_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    $ EP1_add_object_to_scene("Teleport_Steve_Office_Office", {"type":3, "text" : t_("КАБИНЕТ СТИВА"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "EP1_steve_office_secretary_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label EP1_steve_office_secretary_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street":
        if catchSteveInProgress == True:
            m "Я не пойду на улицу!
            Мне надо добраться до Стива!!!"
            return
        if steveSecretaryExitTalkAfterCatch == False:
            music casualMusic
            $ steveSecretaryExitTalkAfterCatch = True
            if steveSecretaryTalkAfterCatch == False or steveSecretaryFireOffended2 == True:
                call EP1_steve1_secretary_talk3()

        call EP1_change_scene("street_steve_office", "Fade_long", "snd_lift")
        return
    if obj_name == "Teleport_Steve_Office_Office":
        if steveSecretaryOffended == False:
            call EP1_steve1_secretary_talk1()
        call EP1_change_scene("steve_office_office")
        return
    return
label EP1_steve_office_secretary_environment(obj_name, obj_data):
    if obj_name == "Flower1" or obj_name == "Flower2" or obj_name == "Flower3" or obj_name == "Flower4":
        if bitchmeterValue > maxBitchness / 2:
            mt "Эта сучка наставила цветов везде."
        else:
            mt "Эта секретарша наставила цветов везде."
        "Хочет быть похожей на меня?"
        "Она не понимает, что для этого надо нечно большее!"
    if obj_name == "Folders1" or obj_name == "Folders2":
        mt "Судя по надписям на папках здесь есть довольно важные документы."
        if bitchmeterValue > maxBitchness / 2:
            "Не слишком-ли много Стив доверяет этой сучке?"
        else:
            "Не слишком-ли много Стив доверяет этой секретарше?"
    if obj_name == "Monitor":
        mt "Какой большой экран у нее.
        Я уверена что там открыты не рабочие документы, а какой-нибудь женский магазин!"
        "Никчемный работник!"
    if obj_name == "Monica":
        if catchSteveInProgress == True:
            mt "Я доберусь до этого Стива!
            Здесь его логово!"
    if obj_name == "Secretary":
        if obj_data["action"] == "l":
            if steveSecretaryOffended == False:
                mt "Кажется, я ее знаю..."
            else:
                if bitchmeterValue > maxBitchness / 2:
                    mt "Я еще разберусь с этой сучкой..."
                else:
                    mt "Я еще разберусь с этой Джейн..."
        if obj_data["action"] == "t":
            if day == 3:
                call EP1_steve1_secretary_talk4()
                call EP1_refresh_scene_fade()
                return
            if steveSecretaryOffended == False:
                call EP1_steve1_secretary_talk1()
                call EP1_refresh_scene_fade()
                return
            if steveSecretaryOffended == True and day == 2:
                call EP1_steve1_secretary_talk2()
                call EP1_refresh_scene_fade()
                return

    return
