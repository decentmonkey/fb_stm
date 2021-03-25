label floor2_mirrors:
    $ print "enter_floor2_mirrors"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_21

    $ scene_image = "scene_Floor2_Mirrors_no_hair_dye[day_suffix]"
    music houseMusic
    return

label floor2_mirrors_init:

    $ add_object_to_scene("Ink1", {"type":2, "base":"Floor2_Mirrors_Ink1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Bottle1", {"type":2, "base":"Floor2_Mirrors_Bottle1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Pomade1", {"type":2, "base":"Floor2_Mirrors_Pomade1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Perfume1", {"type":2, "base":"Floor2_Mirrors_Perfume1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Shadows1", {"type":2, "base":"Floor2_Mirrors_Shadows1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Shadows2", {"type":2, "base":"Floor2_Mirrors_Shadows2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Cosmetics", {"type":2, "base":"Floor2_Mirrors_Cosmetics", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Perfume2", {"type":2, "base":"Floor2_Mirrors_Perfume2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Perfume2", {"type":2, "base":"Floor2_Mirrors_Perfume2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Mirror2", {"type":2, "base":"Floor2_Mirrors_Mirror2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor2_mirrors_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label floor2_mirrors_teleport:
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_151
        return

label floor2_mirrors_environment2:
#ink1, bottle1, pomade1, perfume1, shadows1, shadows2, cosmetics, perfume2, hairdye
    if obj_name == "Mirror2":
        pass

    if obj_name == "Ink1":
        m "Это тушь для ресниц."

    if obj_name == "Bottle1":
        m "Это увлажняющий спрей для лица."

    if obj_name == "Pomade1":
        m "Помада."

    if obj_name == "Perfume1":
        m "Мои любимые духи."

    if obj_name == "Shadows1":
        m "Это тени."

    if obj_name == "Shadows2":
        m "Это тени."

    if obj_name == "Cosmetics":
        m "Одна из моих многочисленных косметичек."
    if obj_name == "Perfume2":
        pass

    return


label floor2_mirrors_environment:
    if obj_name == "Journal":
        if obj_data["action"] == "l":
            m "А что это лежит сбоку от зеркала?"

            m "Да это же выпуск моего журнала!"

            $ journalViewed = True

        if obj_data["action"] == "h":
            imgc fashion2
            $ add_inventory("journal", 1, True)
            $ journalTaken = True

            if journalViewed == False:
                m "А что это лежит сбоку от зеркала?"

                "Да это же выпуск моего журнала!"

            m "Этот выпуск особенный."

            "Его украшает мой образ."

            "Как я смотрюсь на ней?"

            "По-моему, потрясающе!"

            "Как владелец журнала, я могу позволить себе такие мелочи."

            "Такие как быть на обложке самого модного журнала."

            "Хи-хи."
            w
            call change_scene("floor2_mirrors", "Fade", "snd_take_paper") from _call_change_scene_27
            return

    return
