default collegeClassMonicaSuffix = 1
default collegeClassBettySuffix = 1
default collegeClassTeacherSuffix = 1

label college_class:

    $ print "enter_college_class"
    $ miniMapData = []

    $ scene_image = "scene_College_Class"

#    music
    music school-corridor-1
    return

label college_class_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"College_Class_Monica[collegeClassMonicaSuffix]", "click" : "college_class_environment", "actions" : "l", "zorder" : 10}, scene="college_class")
    $ add_object_to_scene("Betty", {"type":2, "base":"College_Class_Betty[collegeClassBettySuffix]", "click" : "college_class_environment", "actions" : "l", "zorder" : 10}, scene="college_class")
    $ add_object_to_scene("Teacher", {"type":2, "base":"College_Class_Teacher[collegeClassTeacherSuffix]", "click" : "college_class_environment", "actions" : "lt", "icon_t":"/Icons/talk" + res.suffix +".png", "zorder" : 8}, scene="college_class")

    $ add_object_to_scene("College_Class_Books", {"type":2, "base":"College_Class_Books", "click" : "college_class_environment", "actions" : "l", "zorder" : 0}, scene="college_class")
    $ add_object_to_scene("College_Class_Desk", {"type":2, "base":"College_Class_Desk", "click" : "college_class_environment", "actions" : "l", "zorder" : 0}, scene="college_class")
    $ add_object_to_scene("College_Class_Formulas", {"type":2, "base":"College_Class_Formulas", "click" : "college_class_environment", "actions" : "l", "zorder" : 0}, scene="college_class")
    $ add_object_to_scene("College_Class_SchoolTables", {"type":2, "base":"College_Class_SchoolTables", "click" : "college_class_environment", "actions" : "l", "zorder" : 0}, scene="college_class")
    $ add_object_to_scene("College_Class_Windows", {"type":2, "base":"College_Class_Windows", "click" : "college_class_environment", "actions" : "l", "zorder" : 0}, scene="college_class")
    $ add_object_to_scene("College_Class_WorldMap", {"type":2, "base":"College_Class_WorldMap", "click" : "college_class_environment", "actions" : "l", "zorder" : 0}, scene="college_class")

    $ add_object_to_scene("Teleport_Street_College", {"type":3, "text" : t_("НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_class_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="college_class")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_class_teleport:
    if obj_name == "Teleport_Street_College":
        call change_scene("street_college", "Fade_long", "highheels_run2") from _call_change_scene_402
        return
    return
label college_class_environment:
    if obj_name == "College_Class_Books":
        call dialogue_classmate_3_3d() from _call_dialogue_classmate_3_3d
    if obj_name == "College_Class_Desk":
        call dialogue_classmate_3_3e() from _call_dialogue_classmate_3_3e
    if obj_name == "College_Class_Formulas":
        call dialogue_classmate_3_3h() from _call_dialogue_classmate_3_3h
    if obj_name == "College_Class_SchoolTables":
        call dialogue_classmate_3_3g() from _call_dialogue_classmate_3_3g
    if obj_name == "College_Class_Windows":
        call dialogue_classmate_3_3c() from _call_dialogue_classmate_3_3c
    if obj_name == "College_Class_WorldMap":
        call dialogue_classmate_3_3f() from _call_dialogue_classmate_3_3f

    if obj_name == "Monica":
        call dialogue_classmate_3_3i() from _call_dialogue_classmate_3_3i

    if obj_name == "Teacher":
        if act=="l":
            call dialogue_classmate_3_3b() from _call_dialogue_classmate_3_3b

    return
