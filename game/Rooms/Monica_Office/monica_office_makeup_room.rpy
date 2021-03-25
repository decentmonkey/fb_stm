default makeupRoomMelanieSuffix = 1

default monicaOfficeMakeupRoomSkipMusicOneTime = False

label monica_office_makeup_room:
    $ print "enter_monica_office_makeup_room"
    $ miniMapData = []
    call miniMapOfficeGenerate() from _call_miniMapOfficeGenerate

    $ scene_image = "scene_office_monica_makeuproom"

    if monicaOfficeMakeupRoomSkipMusicOneTime == False:
        music Mandeville
    $ monicaOfficeMakeupRoomSkipMusicOneTime = False

    if check_hook("Melanie", "ep23_quests_melanie7", scene="monica_office_makeup_room") == True and day_time == "evening":
        $ autorun_to_object("dialogue_classmate_3_2a2", scene="monica_office_makeup_room")
#        $ move_object("Melanie", "monica_office_makeup_room")
    return

label monica_office_makeup_room_init:
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_PhotoStudio_Monica_[cloth]", "click" : "monica_office_photostudio_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Melanie", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Melanie[makeupRoomMelanieSuffix]", "click" : "monica_office_photostudio_environment", "actions" : "lt", "zorder":10, "active":False}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Boxes", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Boxes", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":0,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("MelaniePhoto1", {"type" : 2, "base" : "Office_Monica_MakeupRoom_MelaniePhoto1", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":3,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("MelaniePhoto2", {"type" : 2, "base" : "Office_Monica_MakeupRoom_MelaniePhoto2", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":3,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Mirror1", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Mirror1", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":1,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Mirror2", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Mirror2", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":1,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Table1", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Table1", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":2,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Table2", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Table2", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":3,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")
    $ add_object_to_scene("Table3", {"type" : 2, "base" : "Office_Monica_MakeupRoom_Table3", "click" : "monica_office_makeup_room_environment", "actions" : "l", "zorder":4,"b":0.15, "group":"environment"}, scene="monica_office_makeup_room")

    $ add_object_to_scene("Teleport_Monica_Office_Photostudio", {"type":3, "text" : t_("ФОТОСТУДИЯ"), "rarrow" : "arrow_down_2", "base":"Office_Monica_MakeupRoom_Teleport_Photostudio", "click" : "monica_office_makeup_room_teleport", "xpos" : 1688, "ypos" : 846, "zorder":11, "teleport":True}, scene="monica_office_makeup_room")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_makeup_room_teleport:
    if obj_name == "Teleport_Monica_Office_Photostudio":
        call change_scene("monica_office_photostudio") from _call_change_scene_191
        return

    return
label monica_office_makeup_room_environment:
    if obj_name == "Boxes":
        mt "Это ящики с оборудованием и с одеждой для съемок."
        mt "Я ввела строгий учет всех вещей, поэтому мне не получится украсть что-то здесь..."
        if monicaBitch == True:
            mt "Но я не жалею об этом!"
            "Когда я верну это место себе, я введу еще более строгий учет здесь!"
    if obj_name == "MelaniePhoto1" or obj_name == "MelaniePhoto2":
        img 9663
        with fade
        mt "Мелани все завесила своими фото."
        mt "Она очень любит себя."
    if obj_name == "Mirror1" or obj_name == "Mirror2":
        mt "Зеркала..."
        mt "Я люблю смотреть на себя в зеркало, но не когда я одета в это!!!"
    if obj_name == "Table1" or obj_name == "Table3":
        mt "Гримерный столик одной из моих моделей..."
        mt "У меня ощущение что Мелани захватила и его тоже..."
    if obj_name == "Table2":
        img 9663
        with fade
        mt "Гримерный столик Мелани..."
        mt "Я смотрю Мелани здесь неплохо обосновалась, пока меня нет..."
    return





#
