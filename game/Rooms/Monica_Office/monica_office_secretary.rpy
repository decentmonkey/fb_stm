default monicaOfficeSecretaryMonicaSuffix = ""
default monicaOfficeSecretarySecretarySuffix = 2

default monicaOfficeSecretaryMonicaSuffix_forced = False

label monica_office_secretary:
    $ print "enter_monica_office_secretary"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate_4

    $ scene_image = "scene_Office_Monica_Secretary[day_suffix]"

    $ monicaOfficeSecretaryMonicaSuffix = ""
    if cloth == "Whore":
        if renpy.random.randint(1,2) == 2:
            $ monicaOfficeSecretaryMonicaSuffix = "2"
    if monicaOfficeSecretaryMonicaSuffix_forced != False:
        $ monicaOfficeSecretaryMonicaSuffix = monicaOfficeSecretaryMonicaSuffix_forced
        $ monicaOfficeSecretaryMonicaSuffix_forced = False

    music Mandeville
    return

label monica_office_secretary_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Secretary_Monica_[cloth][monicaOfficeSecretaryMonicaSuffix][day_suffix]", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":10})
    $ add_object_to_scene("Secretary", {"type" : 2, "base" : "Office_Monica_Secretary_Secretary[monicaOfficeSecretarySecretarySuffix][day_suffix]", "click" : "monica_office_secretary_environment", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Books1", {"type" : 2, "base" : "Office_Monica_Secretary_Books1", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Books2", {"type" : 2, "base" : "Office_Monica_Secretary_Books2", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Globe", {"type" : 2, "base" : "Office_Monica_Secretary_Globe", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Music_Instrument", {"type" : 2, "base" : "Office_Monica_Secretary_Music_Instrument", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Table", {"type" : 2, "base" : "Office_Monica_Secretary_Table", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Teatable", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Object", "click" : "monica_office_secretary_environment", "actions" : "lw", "zorder":0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type" : 2, "base" : "Office_Monica_Secretary_Windows", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0, "group":"environment"})

    $ add_object_to_scene("Teleport_Monica_Office_Photostudio", {"type":3, "text" : t_("ФОТОСТУДИЯ"), "larrow" : "arrow_left_2", "base":"empty", "click" : "monica_office_secretary_teleport", "xpos" : 178, "ypos" : 1014, "zorder":11, "teleport":True})

    $ add_object_to_scene("Teleport_Monica_Office_Cabinet", {"type":3, "text" : t_("КАБИНЕТ МОНИКИ"), "rarrow" : "arrow_down_2", "base":"Office_Monica_Secretary_Teleport_Cabinet", "click" : "monica_office_secretary_teleport", "xpos" : 1692, "ypos" : 756, "zorder":11, "teleport":True})

    $ add_object_to_scene("Teleport_Monica_Office_Entrance", {"type":3, "text" : t_("ЛИФТ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_secretary_teleport", "xpos" : 780, "ypos" : 956, "zorder":11, "teleport":True, "high_sprite_hover":True})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_secretary_teleport:
    if obj_name == "Teleport_Monica_Office_Entrance":
        call change_scene("monica_office_entrance", "Fade_long", "snd_lift") from _call_change_scene_131
        return
    if obj_name == "Teleport_Monica_Office_Cabinet":
        call change_scene("monica_office_cabinet") from _call_change_scene_132
        return
    if obj_name == "Teleport_Monica_Office_Photostudio":
        call change_scene("monica_office_photostudio") from _call_change_scene_133
        return

    return
label monica_office_secretary_environment:
    if obj_name == "Globe":
        return
    if obj_name == "Monica":
        mt "Это этаж моего главного офиса."
        "У меня здесь все под рукой."
        "Моя секретарь, фото-студия и мой кабинет."
        "Вернее сейчас кабинет не мой, но скоро будет МОЙ снова!!!"

    if obj_name == "Books1" or obj_name == "Books2":
        mt "Моя секретарь слишком много увлекается чтением."

    if obj_name == "Music_Instrument":
        mt "Моя секретарь играет на музыкальных инструментах."

    if obj_name == "Table":
        mt "За этим столом моя секретарь проводит почти все рабочее время."

    if obj_name == "Windows":
        mt "Из этих окон ужасный вид на город!"
    if obj_name == "Teatable":
        if obj_data["action"] == "l":
            mt "Это чайный столик."
            "Моя секретарь обычно угощает чаем, либо кофе тех, кто ожидает моего приема."
            "Неудивительно что выпечки и кофе здесь больше нет..."
            "А жаль, я бы с удовольствием съела что-нибудь!"

        if obj_data["action"] == "w":
            call change_scene("monica_office_secretary_teatable") from _call_change_scene_134
            return

    if obj_name == "Secretary":
        if obj_data["action"] == "l":
            img Monica_Secretary_Alone
            mt "Это моя секретарша."

            mt "Одна из немногих нормальных женщин, которые знают как держать себя с окружающими."

            "Она очень воспитана и интеллигентна."
            "Я знаю, она сохранит верность мне и поможет вернуть все назад..."
            return
        if obj_data["action"] == "t":
            music casualMusic
            return
    return




















    #
