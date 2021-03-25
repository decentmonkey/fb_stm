default e210_quests_julia_aborted = False # Квест завершен
default ep210_julia_not_at_work = False
default ep210_julia_evening_at_work = False
default ep210_julia_first_date_begin_day = 0

default ep210_julia_kissed_day_day = 0
default ep210_julia_kissed_day_evening = 0
default ep210_julia_massage_day = 0
default ep210_monica_julia_massage_peek_try_count = 0
default ep210_monica_julia_massage_count = 0
default ep210_julia_monica_massage_count = 0

label ep210_quests_julia_init:
    $ add_hook("Julia", "ep210_quests_julia1", scene="working_office_cabinet", label="ep210_quests_julia1")
    return

label ep210_quests_julia1: # Разговор после атаки офисных работников
    if act=="l":
        return
    $ remove_hook()
    call ep210_dialogues5_julia_1() from _call_ep210_dialogues5_julia_1
    $ questHelp("julia_22a", True)
    if _return == False:
        $ questsFailByCategory(t_("ЮЛИЯ"))
        $ e210_quests_julia_aborted = True
        $ questLog(47, False)
        $ remove_objective("find_julia_panties_color")
        $ remove_hook(label="ep29_quests_julia3_workers")
        $ questHelp("julia_23", False)
        call refresh_scene_fade() from _call_refresh_scene_fade_251
        return False
    $ questLog(63, True)
    $ questHelp("julia_23", skipIfExists=True)
    $ questHelpDesc("julia_desc1", "julia_desc2")

    $ add_hook("Julia", "ep210_quests_julia1b", scene="working_office_cabinet", label="ep210_quests_julia1b")
    $ add_hook("enter_scene", "ep210_quests_julia1c", scene="working_office_cabinet", label="ep210_quests_julia1c")
    $ ep210_julia_not_at_work = True
    $ ep210_julia_first_date_begin_day = day
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_39
    return False

label ep210_quests_julia1b: # Повторный клик
    if act=="l":
        return
    call ep210_dialogues5_julia_1_2() from _call_ep210_dialogues5_julia_1_2
    call refresh_scene_fade() from _call_refresh_scene_fade_252
    return False

label ep210_quests_julia1c: # Юлии нет в офисе (надо идти на свидание)
    if ep210_julia_first_date_begin_day == day:
        return
    $ remove_hook()
    $ remove_hook(label="ep210_quests_julia1b")
    call ep210_dialogues5_julia_2() from _call_ep210_dialogues5_julia_2
    $ add_objective("go_to_julia", t_("Пойти на свидание с Юлией."), c_green, 80)

    # Инициализируем локацию Юлии
    $ map_objects ["Teleport_JuliaHome"] = {"text" : t_("ДОМ ЮЛИИ"), "xpos" : 521, "ypos" : 1014, "base" : "map_marker", "state" : "visible"}
    call locations_init_julia_street() from _call_locations_init_julia_street
    call street_corner_init2() from _call_street_corner_init2
    $ add_hook("JuliaCafe", "ep210_quests_julia2_cafe_regular", scene="street_juliahome", label="julia_cafe_regular")
    $ add_hook("JuliaCafe", "ep210_quests_julia2_cafe", scene="street_juliahome", label="julia_first_date")
    $ add_hook("Teleport_StreetCorner", "ep25_quests4", scene="street_juliahome", label="casual_dress_slums_forbidden", priority = 900)
    $ add_hook("Monica", "ep210_dialogues5_julia_3_2", scene="street_juliahome", label="julia_first_date")
    return

label ep210_quests_julia2_cafe: # Клик на кафе
    if act=="l":
        call ep210_dialogues5_julia_3_1() from _call_ep210_dialogues5_julia_3_1
        return False
    if cloth != "CasualDress1":
        call ep210_dialogues5_julia_3_4a() from _call_ep210_dialogues5_julia_3_4a
        return False
    call ep210_dialogues5_julia_3_8() from _call_ep210_dialogues5_julia_3_8
    if _return == False:
        return False
    $ remove_objective("go_to_julia")
    img black_screen
    with diss
    $ ep210_julia_not_at_work = False
    $ remove_hook()
    $ questLog(63, False)
    if day_time != "evening":
        $ changeDayTime("evening")
    call ep210_dialogues5_julia_3() from _call_ep210_dialogues5_julia_3
    $ questHelp("julia_23", True)

    if _return == False:
        $ e210_quests_julia_aborted = True
        $ questHelp("julia_24", False)
        $ questsFailByCategory(t_("ЮЛИЯ"))
        $ questLog(47, False)
        $ remove_objective("find_julia_panties_color")
        $ remove_hook(label="ep29_quests_julia3_workers")
        call process_change_map_location("House") from _call_process_change_map_location_7
        call change_scene("street_house_outside", "Fade_long") from _call_change_scene_500
        return False

    $ questHelp("julia_24", skipIfExists=True)
    $ questHelpDesc("julia_desc3")
    $ add_money(-15.0)
    $ move_object("Julia", "street_juliahome")
    $ char_info["Julia"]["enabled"] = True
    $ char_info["Julia"]["caption"] = t_("Мне надо притворяться что Юлия мне нравится.")
    $ add_hook("office_work_process", "ep210_quests_julia3_massage", scene="global", label="julia_massage")
    $ add_hook("change_time_day", "ep210_quests_julia2_cafe_after", scene="global", once=True)
    $ streetJuliaHomeMonicaSuffix = 2
    $ set_active("JuliaHome", True, scene="street_juliahome")
    $ add_hook("JuliaHome", "ep210_quests_julia2_juliahome", scene="street_juliahome", label="julia_home1")
    $ add_hook("Monica", "ep210_dialogues5_julia_3_3", scene="street_juliahome", label="evening_time_temp")
    $ add_hook("Julia", "ep210_quests_julia2_julia", scene="street_juliahome", label="evening_time_temp")
    $ add_hook("Julia", "ep210_quests_julia3", scene="working_office_cabinet", label="julia_dating_regular")
    $ ep210_julia_evening_at_work = True
    $ questLog(64, True)
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_40
    return False

label ep210_quests_julia2_cafe_after:
    $ streetJuliaHomeMonicaSuffix = 1
    return

label ep210_quests_julia2_cafe_regular: # Регулярный клик на кафе
    if act=="l":
        call ep210_dialogues5_julia_3_6() from _call_ep210_dialogues5_julia_3_6
        return False
    call ep210_dialogues5_julia_3_7() from _call_ep210_dialogues5_julia_3_7
    return False

label ep210_quests_julia2_juliahome: # Клик на дом Юлии
    if act=="l":
        call ep210_dialogues5_julia_3_5() from _call_ep210_dialogues5_julia_3_5
        return False
    call ep210_dialogues5_julia_3_3() from _call_ep210_dialogues5_julia_3_3
    return False

label ep210_quests_julia2_julia: # Клик на Юлию
    if act=="l":
        call ep210_dialogues5_julia_3_3() from _call_ep210_dialogues5_julia_3_3_1
        return False
    call ep210_dialogues5_julia_3_4() from _call_ep210_dialogues5_julia_3_4
    return False


label ep210_quests_julia3: # Новые отношения с Юлией (клик на нее)
    if act=="l":
        return
    if day_time == "day":
        call ep210_julia_dialogue1() from _call_ep210_julia_dialogue1
    else:
        call ep210_julia_dialogue1_evening() from _call_ep210_julia_dialogue1_evening
    if _return == 0:
        call refresh_scene_fade() from _call_refresh_scene_fade_253
        return False
    if _return == 1:
        call ep210_dialogues5_julia_4_1() from _call_ep210_dialogues5_julia_4_1
        $ ep210_julia_kissed_day_day = day
        if char_info["Julia"]["level"] < 4 or char_info["Julia"]["level"] == 5 or char_info["Julia"]["level"] == 7:
            $ add_char_progress("Julia", monicaJuliaKissProgress, "monicaJuliaKissProgress_day" + str(day))
        call refresh_scene_fade() from _call_refresh_scene_fade_254
        return False
    if _return == 2:
        call ep210_dialogues5_julia_4_3() from _call_ep210_dialogues5_julia_4_3
        $ ep210_julia_kissed_day_evening = day
        if char_info["Julia"]["level"] < 4 or char_info["Julia"]["level"] == 5 or char_info["Julia"]["level"] == 7:
            $ add_char_progress("Julia", monicaJuliaKissProgress, "monicaJuliaKissProgress_evening" + str(day))
        call refresh_scene_fade() from _call_refresh_scene_fade_255
        return False
    if _return == 3:
        call ep210_dialogues5_julia_5() from _call_ep210_dialogues5_julia_5
        $ questHelp("julia_25", True)
        if _return == True:
            $ ep210_monica_julia_massage_peek_try_count += 1
        else:
            if char_info["Julia"]["level"] < 4 or char_info["Julia"]["level"] == 5 or char_info["Julia"]["level"] == 7:
                $ add_char_progress("Julia", monicaJuliaKissProgress, "monicaJuliaMassageProgress_day" + str(day))
        $ ep210_monica_julia_massage_count += 1
        $ ep210_julia_massage_day = day
        call refresh_scene_fade() from _call_refresh_scene_fade_256
        return False
    if _return == 4:
        call ep211_quests_julia1() from _rcall_ep211_quests_julia1 # второе свидание
        call refresh_scene_fade() from _rcall_refresh_scene_fade
        return False
    if _return == 5: # Третье свидание
        call ep212_quests_julia1_third_date_init() from _rcall_ep212_quests_julia1_third_date_init
        call refresh_scene_fade() from _rcall_refresh_scene_fade_47
        return False
    if _return == 6: # Предложение жить вместе
        call ep213_quests_julia1() from _rcall_ep213_quests_julia1
        return False

    return False

label ep210_quests_julia3_massage: # Юлия делает Монике массаж
    if char_info["Julia"]["level"] < 4: # Если уповень меньше 4
        return
    if get_active_objects("Julia", scene="working_office_cabinet") == False or ep210_julia_kissed_day_day != day: # Если Юлии нет или Моника ее не целовала
        return
    if ep210_monica_julia_massage_count <= 0: # Если Моника не делал массаж Юлии до этого
        return
    call ep210_dialogues5_julia_4_2() from _call_ep210_dialogues5_julia_4_2
    if _return != False:
        $ ep210_julia_monica_massage_count += 1
    return








    #
