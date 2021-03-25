default ep211_quests_load_init_flag = False
default ep211_quests_load_init_bug_pub_flag = False

label ep211_quests_load_init:
    if ep211_quests_load_init_flag == False:
        # check Monica pub name, костыль для испорченных сейвов
        if monicaWorkingAsDishwasher == True and monica_pub_name == False:
            $ monica_pub_name = t__("Мэрилин")
        # fix pub Bartender silent bug
        if scenes_data["hooks"].has_key("pub") == True and scenes_data["hooks"]["pub"].has_key("Bartender") == False and scene_name == "pub":
            $ autorun_to_object("ep23_quests_pub1a", scene="pub")
            $ set_active("Pub_Washbasin", False, scene="pub")
            $ pubLocationInitializedForced = True
            $ ep211_quests_load_init_bug_pub_flag = True


        if ep22_quests_monica_presentation_completed == True and ep22_quests_monica_presentation_completed_day == -1:
            $ ep22_quests_monica_presentation_completed_day = day

        if char_info.has_key("Julia") and char_info["Julia"]["level"] == 4:
            $ char_info["Julia"]["enabled"] = True
            $ char_info["Julia"]["caption"] = t_("Юлия приняла ухаживания Моники, но еще побаивается ее.")


        $ ep211_quests_load_init_flag = True
    return
