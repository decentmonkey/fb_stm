default pubMonicaSuffix = 1
default pubBartenderSuffix = 1
default pubBartenderWaitressSuffix = 1
default pubStripteaseGirl1Suffix = 1
default pubStripteaseGirl2Suffix = 1
default pubVisitor1Suffix = ""
default pubVisitor2Suffix = ""
default pubVisitor3Suffix = ""
default pubVisitor4Suffix = ""
default pubVisitor5Suffix = ""
default pubVisitor6Suffix = ""
default pubVisitor7Suffix = ""
default pubVisitor8Suffix = ""
default pubVisitor9Suffix = ""
default pubVisitor10Suffix = ""
default pubVisitor11Suffix = ""
default pubVisitor12Suffix = ""

default pubLocationInitializedForced = False

label pub:
    $ print "enter_pub"
    $ miniMapData = []

    $ scene_image = "scene_pub"

    $ pubStripteaseGirl1Suffix = rand(1,4)
    $ pubStripteaseGirl2Suffix = rand(1,4)

    if slumsApartmentsCheckInitialized == False:
        call ep211_quests_slums_apartments0_init() from _rcall_ep211_quests_slums_apartments0_init

    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False or get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        music RocknRoll_loop
    else:
        music Indo_Rock2

    if get_active_objects(scene="pub", group="visitors") != False:
        music2 pub_noise1

#    if pubLocationInitializedForced == False and monicaWorkingAsDishwasher == False:
    if scenes_data["hooks"]["pub"].has_key("Bartender") == False and ep211_quests_load_init_bug_pub_flag == False:
        $ add_hook("enter_scene", "ep23_quests_pub1", scene="pub")
        $ set_active("Pub_Washbasin", False, scene="pub")
        $ pubLocationInitializedForced = True

    if ep213_quests_pub1_inited == False:
        call ep213_quests_pub1() from _rcall_ep213_quests_pub1 # Проверка на продолжение квестов

    if ep214_quests_pub1_check_inited_flag == False:
        call ep214_quests_pub1_check_init() from _rcall_ep214_quests_pub1_check_init

    if ep214_quests_claire_show1_day > 0 and ep215_quests_pub1_inited == False:
        call ep215_quests_pub1() from _rcall_ep215_quests_pub1

    $ set_active("Pub_Washbasin", False)
    return
label pub_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"pub_Monica_[cloth][pubMonicaSuffix]", "click" : "pub_environment", "actions" : "l", "zorder" : 200}, scene="pub")
#    $ add_object_to_scene("Teleport_pub_Door", {"type":2, "base":"pub_Teleport_pub2", "click" : "pub_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True})

    $ add_object_to_scene("Bartender", {"type" : 2, "base" : "Pub_Bartender[pubBartenderSuffix]", "click" : "pub_environment", "actions" : "lt", "zorder":30, "icon_t":"/Icons/talk" + res.suffix +".png"}, scene="pub")
    $ add_object_to_scene("Bartender_Waitress", {"type" : 2, "base" : "Pub_Bartender_Waitress[pubBartenderWaitressSuffix]", "click" : "pub_environment", "actions" : "lt", "zorder":30}, scene="pub")

    $ add_object_to_scene("Pub_StripteaseGirl1", {"type" : 2, "base" : "Pub_StripteaseGirl1_[pubStripteaseGirl1Suffix]", "click" : "pub_environment", "actions" : "lw", "zorder":1}, scene="pub")
    $ add_object_to_scene("Pub_StripteaseGirl2", {"type" : 2, "base" : "Pub_StripteaseGirl2_[pubStripteaseGirl2Suffix]", "click" : "pub_environment", "actions" : "lw", "zorder":1}, scene="pub")

    $ add_object_to_scene("Pub_Visitor1", {"type" : 2, "base" : "Pub_Visitor1[pubVisitor1Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":30, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor2", {"type" : 2, "base" : "Pub_Visitor2[pubVisitor2Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":60, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor3", {"type" : 2, "base" : "Pub_Visitor3[pubVisitor3Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":0, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"strip_lookers"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor4", {"type" : 2, "base" : "Pub_Visitor4[pubVisitor4Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":110, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor5", {"type" : 2, "base" : "Pub_Visitor5[pubVisitor5Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":100, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor6", {"type" : 2, "base" : "Pub_Visitor6[pubVisitor6Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":40, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor7", {"type" : 2, "base" : "Pub_Visitor7[pubVisitor7Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":20, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"strip_lookers"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor8", {"type" : 2, "base" : "Pub_Visitor8[pubVisitor8Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"strip_lookers"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor9", {"type" : 2, "base" : "Pub_Visitor9[pubVisitor9Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":80, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor10", {"type" : 2, "base" : "Pub_Visitor10[pubVisitor10Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":70, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor11", {"type" : 2, "base" : "Pub_Visitor11[pubVisitor11Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":50, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")
    $ add_object_to_scene("Pub_Visitor12", {"type" : 2, "base" : "Pub_Visitor12[pubVisitor12Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":90, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"visitors_tables"}, scene="pub")

    $ add_object_to_scene("Pub_Bar", {"type" : 2, "base" : "Pub_Bar", "click" : "pub_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub")
    $ add_object_to_scene("Pub_Bar_Table", {"type" : 2, "base" : "Pub_Bar_Table", "click" : "pub_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub")
#    $ add_object_to_scene("Pub_Pole", {"type" : 2, "base" : "Pub_Pole", "click" : "pub_environment", "actions" : "lw", "zorder":0, "group":"environment"}, scene="pub")
    $ add_object_to_scene("Pub_Washbasin", {"type" : 2, "base" : "Pub_Washbasin", "click" : "pub_environment", "actions" : "l", "zorder":0, "group":"environment", "active":False}, scene="pub")

#    $ add_object_to_scene("Car", {"type":2, "base":"pub_Car", "click" : "pub_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : t_("ВЫХОД ИЗ HOLE"), "rarrow" : "arrow_right_2", "base":"Pub_Teleport_Hostel_Street", "click" : "pub_teleport", "xpos" : 1379, "ypos" : 1023, "zorder":250, "teleport":True, "high_sprite_hover":True}, scene="pub")

    return

label pub_ini2:
    $ add_object_to_scene("Teleport_Pub_MakeupRoom", {"type":3, "text" : t_("ГРИМЕРНАЯ КОМНАТА"), "larrow" : "arrow_left_2", "base":"empty", "click" : "pub_teleport", "xpos" : 225, "ypos" : 1023, "zorder":250, "teleport":True, "high_sprite_hover":True}, scene="pub")
    return

label pub_init3:
    $ add_object_to_scene("Poster1", {"type" : 2, "base" : "Pub_Poster1", "click" : "pub_environment", "actions" : "l", "zorder":0}, scene="pub")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label pub_teleport:
    if obj_name == "Teleport_Hostel_Street":
        music2 stop
        call change_scene("hostel_street") from _call_change_scene_169
    if obj_name == "Teleport_Pub_MakeupRoom":
        if cloth == "Whore":
            $ pub_makeuproom_monica_suffix = 1
        music2 stop
        call change_scene("pub_makeuproom", "Fade_long") from _rcall_change_scene_75
    return
label pub_environment:
    if obj_name == "Bartender":
        if act=="l":
            if monicaWorkingAsDishwasher == False:
                mt "Он похож на бармена в этой дыре..."
            else:
                mt "Это Джо. Он дал мне работу посудомойщицей."
                mt "Это ужас, конечно, но, по крайней мере, у меня есть еда..."
    if obj_name == "Bartender_Waitress":
        if act=="l":
            if monicaWorkingAsDishwasher == False:
                mt "Похоже это официантка в этой дыре или что-то вроде того..."
            else:
                mt "Это Эшли. Жена Джо."
                mt "Мне кажется что она немного странная."
                mt "Хотя что может быть не странного в этой дыре?!"

    if obj_name == "Monica":
        mt "Какое жуткое место!"
        "Я даже представить себе не могла что могу оказаться в подобном заведении!"
    if obj_name == "Pub_Bar":
        img 9662
        with fade
        mt "SHINY HOLE?!?"
        mt "О БОЖЕ!"
        "ЧТО ЭТО ЗА ДЫРА?!?"

    if obj_name == "Pub_Bar_Table":
        mt "Жуткое заведение, жуткая мебель!"
        "Какой кошмар, Моника!"

    if obj_name == "Pub_StripteaseGirl1" or obj_name == "Pub_StripteaseGirl2":
        if act=="l":
            if obj_name == "Pub_StripteaseGirl1":
                if pubStripteaseGirl1Suffix == 1:
                    img 9668
                if pubStripteaseGirl1Suffix == 2:
                    img 9669
                if pubStripteaseGirl1Suffix == 3:
                    img 9670
                if pubStripteaseGirl1Suffix == 4:
                    img 9671
            if obj_name == "Pub_StripteaseGirl2":
                if pubStripteaseGirl2Suffix == 1:
                    img 9664
                if pubStripteaseGirl2Suffix == 2:
                    img 9665
                if pubStripteaseGirl2Suffix == 3:
                    img 9666
                if pubStripteaseGirl2Suffix == 4:
                    img 9667
            with fade
            w
            if ep29_quests_pub_monica_knows_molly == True and obj_name == "Pub_StripteaseGirl1":
                call dialogue_5_dance_strip_25() from _rcall_dialogue_5_dance_strip_25_1
                call refresh_scene_fade() from _rcall_refresh_scene_fade_30
                return
            if ep29_quests_pub_monica_knows_claire == True and obj_name == "Pub_StripteaseGirl2":
                call dialogue_5_dance_strip_26() from _rcall_dialogue_5_dance_strip_26_1
                call refresh_scene_fade() from _rcall_refresh_scene_fade_31
                return
            mt "Эти девушки совсем не уважают себя!"
            "Как можно делать подобное у всех на виду?!"
            call refresh_scene_fade() from _call_refresh_scene_fade_47

        if act=="w":
            mt "Я не собираюсь подходить туда!"
            "Мне не на что там смотреть!!!"

    if obj_name == "Pub_Washbasin":
        mt "Там готовят еду и моют посуду..."
        mt "Какое жуткое место!"

    return
