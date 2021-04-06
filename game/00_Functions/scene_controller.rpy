default pause_enter = 0
default pause_exit = 0
default sceneStages = []
default lastSceneName = False
default refreshed_scene_name = False
default game_version1_screen_ready_to_render = False
default patch32applied = False
default scene_caption = ""
default exitHookCalled = False
default scene_name = "none"
default api_scene_name = "none"
default engine2_inited_flag = False
#default sprites_hover_dummy_screen_flag = False

label show_scene:
    $ exitHookCalled = False
    $ show_scene_loop_flag = False
    if scene_refresh_flag == False:
        jump show_scene_loop
    $ hide_screens_for_scene()
#    if dialogue_active_flag == True:
#        $ renpy.show_screen("dialogue_down_arrow")
#        $ renpy.pause()
#        $ renpy.hide_screen("dialogue_down_arrow")

label show_scene_now:
    if define_version_current != define_version:
        call define_autorun() from _call_define_autorun
#    $ config.has_autosave = True
#    $ print "pause_enter"
#    $ print pause_enter
#    $ print "pause_exit"
#    $ print pause_exit
    if rain != True or sceneIsStreet != True:
        hide screen Rain

    $ interface_blocked_flag = True
    $ list_files_scene_drop_flag = False
    if scene_sound != False:
        $ sound_to_play = get_filename(scene_sound)
        play sound sound_to_play
        $ scene_sound = False
    $ empty1 = "Bitchiness"
    $ empty1 = bitchmeterValue
    hide screen sprites_hover_dummy_screen

#    window hide
#    window show
    $ config.keymap["hide_windows"] = []
#    config.keymap["hide_windows"] = ["mouseup_3", "mouseup_2", "h"]

    if scene_transition != False and gui.scenes_transitions == True:
#        $ _dismiss_pause = False
        if scene_transition == "Fade" or scene_transition == "Fade_fast":
            if refreshed_scene_name == scene_name and scene_transition != "Fade_fast":
                scene black_screen
                with Dissolve(0.2)
#                $ renpy.pause(0.2, hard=True)
            else:
                scene black_screen
                with Dissolve(0.1)
    #            $ renpy.pause(0.2, hard=True)
        if scene_transition == "Fade_long":
            scene black_screen
            with Dissolve(0.7)
#            $ renpy.pause(0.7, hard=True)
#        $ _dismiss_pause = True

    $ renpy.scene()
    $ scene_image_file = get_image_filename(parse_str(scene_image), True)
    $ scene_refresh_flag = False
    show screen show_image_screen(scene_image_file)
    $ image_screen_scene_flag = True
    call map_street_scene_visibility_check() from _call_map_street_scene_visibility_check
    show screen hud_screen(hud_presets[hud_preset_current])
    if EP1 == True:
        show screen EP1_hud_minimap(miniMapData)
    else:
        show screen hud_minimap(miniMapData)

    if rain == True and sceneIsStreet == True:
        show screen Rain
        stop music fadeout 1.0

    define idle_len = 0.0
    $ parse_transition_flag = True
    $ interface_blocked_flag = False

    $ makeDump()
    $ scene_data = process_scene_objects_list(scene_name) #парсим содержимое свойств объектов перед выводом
    $ scene_data = process_character_info_buttons(scene_data) #добавляем кнопки info для персонажей со свойствами
    show screen screen_sprites(scene_data)
    if parse_transition_flag == True:
#        $ _dismiss_pause = False
        if scene_transition != False and gui.scenes_transitions == True:
            if scene_transition == "Fade":
                if refreshed_scene_name == scene_name:
                    with Dissolve(0.2)
                else:
                    with Dissolve(0.1)
            if scene_transition == "Fade_long":
                with Dissolve(0.7)
            if scene_transition == "Dissolve_fast":
                with Dissolve(0.3)
            if scene_transition == "Dissolve_05":
                with Dissolve(0.5)
            if scene_transition == "Dissolve_07":
                with Dissolve(0.7)
            if scene_transition == "Dissolve_10":
                with Dissolve(1.0)
#        $ _dismiss_pause = True
    $ scene_transition = False

    if refreshed_scene_name != scene_name:
        $ refreshed_scene_name = scene_name
        call process_hooks("enter_scene", "global") from _rcall_process_hooks_51
        if _return != False:
            call process_hooks("enter_scene", scene_name) from _call_process_hooks_13 #хук вызывается после входа на сцену и отрисовки (как autorun)
        call remove_dialogue() from _call_remove_dialogue_2
    if scene_refresh_flag == True:
        jump show_scene

    if EP1 == True:
        if scenes_data["autorun"].has_key(scene_name):
            $ autorunFunc = scenes_data["autorun"][scene_name]
            $ del scenes_data["autorun"][scene_name]
            show screen sprites_hover_dummy_screen()
            if renpy.has_label("EP1_" + autorunFunc):
                $ autorunFunc = "EP1_" + autorunFunc
            call expression autorunFunc from _ep1_call_expression_7
            $ scene_refresh_flag = True
            jump show_scene

    if EP1 == False:
        if scenes_data["autorun"].has_key(scene_name) and scenes_data["autorun"][scene_name].has_key("scene"):
            $ autorunFunc = scenes_data["autorun"][scene_name]["scene"]
            $ del scenes_data["autorun"][scene_name]["scene"]
            show screen sprites_hover_dummy_screen()
            if EP1==True:
                if renpy.has_label("EP1_" + autorunFunc):
                    $ autorunFunc = "EP1_" + autorunFunc
            call expression autorunFunc from _call_expression_6
    #        hide screen sprites_hover_dummy_screen
            $ scene_refresh_flag = True
            jump show_scene



label show_scene_loop:
    $ pause_enter += 1
    $ engine2_inited_flag = True
    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data is None:
        $ interact_data = False
    if interact_data != None and interact_data != False:
        if interact_data[0] == "process_object_click":
            if EP1 == False:
                call process_object_click(interact_data[1], interact_data[2], interact_data[3]) from _rcall_sprites_action1
            else:
                call EP1_process_object_click(interact_data[1], interact_data[2], interact_data[3]) from _ep1_rcall_sprites_action1
        if interact_data[0] == "process_object_click_alternate_action":
            if EP1 == False:
                call process_object_click_alternate_action(interact_data[1], interact_data[2], interact_data[3], interact_data[4], interact_data[5]) from _rcall_sprites_action2
            else:
                call EP1_process_object_click_alternate_action(interact_data[1], interact_data[2], interact_data[3], interact_data[4], interact_data[5]) from _ep1_rcall_sprites_action2
        if interact_data[0] == "process_object_click_alternate_inventory":
            if interact_data is not None:
                if EP1 == False:
                    call process_object_click_alternate_inventory(interact_data[1], interact_data[2], interact_data[3], interact_data[4], interact_data[5]) from _rcall_sprites_action3
                else:
                    call EP1_process_object_click_alternate_inventory(interact_data[1], interact_data[2], interact_data[3], interact_data[4], interact_data[5]) from _ep1_rcall_sprites_action3
        if interact_data[0] == "time_management_street_wait_until_evening":
            call time_management_street_wait_until_evening() from _rcall_sprites_action4
        if interact_data[0] == "show_questlog":
            call show_questlog() from _rcall_sprites_action5
        if interact_data[0] == "show_questhelp":
            call show_questhelp() from _rcall_show_questhelp
        if interact_data[0] == "question_helper_call":
            call question_helper_call() from _rcall_sprites_action6
        if interact_data[0] == "map_show":
            if EP1 == False:
                call map_show() from _rcall_sprites_action7
            else:
                call EP1_map_show() from _ep1_rcall_sprites_action7
        if interact_data[0] == "call_hook":

            call call_hook(interact_data[1], interact_data[2]) from _rcall_sprites_action8
        if interact_data[0] == "miniMapHouseGenerateTeleport":
            if EP1 == False:
                call miniMapHouseGenerateTeleport(interact_data[1], interact_data[2]) from _rcall_sprites_action9
            else:
                call EP1_miniMapHouseGenerateTeleport(interact_data[1], interact_data[2]) from _ep1_rcall_sprites_action9

        if interact_data[0] == "miniMapDisabled":
            if EP1 == False:
                call miniMapDisabled(interact_data[1], interact_data[2]) from _rcall_sprites_action10
            else:
                call EP1_miniMapDisabled(interact_data[1], interact_data[2]) from _ep1_rcall_sprites_action10

        if interact_data[0] == "show_achievements":
            call show_achievements() from _rcall_sprites_action11
        if interact_data[0] == "time_management_street_fast_sleep":
            call bed_basement_fast_sleep() from _rcall_bed_basement_fast_sleep


label show_scene_loop2:
#    pause
    $ pause_exit += 1
    if show_scene_loop_flag == False:
        show screen screen_sprites(scene_data)
        jump show_scene_loop
    else:
        jump show_scene


label change_scene(new_scene_name, in_transition_name="Fade", in_sound_name="highheels_short_walk"):
    $ notifCheckTimeout()
    $ target_scene_name = new_scene_name
    $ target_scene_parent = scene_get_parent(target_scene_name)
    $ _return = None
    if exitHookCalled == False:
        call process_hooks("exit_scene", scene_name) from _call_process_hooks_14 #хук выхода со сцены
        $ exitHookCalled = False
    if _return == False: #Если False, то прерываем смену сцены
        return
    if scenes_data["objects"].has_key(new_scene_name) == False or scenes_data["objects"][new_scene_name].has_key("data") == False:
        $ notif ("No scene found! : " + new_scene_name)
        $ makeDump()
        return
    $ sceneIsStreet = False
    $ scene_transition = in_transition_name
    $ scene_sound = in_sound_name
    $ scene_refresh_flag = True
#    $ scene_label = get_scene_label(scene_label)
    $ lastSceneName = scene_name
    $ scene_name = new_scene_name
    $ refreshed_scene_name = False
    $ scene_caption = scenes_data["objects"][scene_name]["data"]["caption"]
    $ scene_label = scenes_data["objects"][scene_name]["data"]["label"]
    $ api_scene_name = new_scene_name

    if sceneSpriteSurfacesCacheSceneName != scene_name:
        $ sceneSpriteSurfacesCacheIdle = {}
        $ sceneSpriteSurfacesCache = {}
    call process_hooks("before_open", scene_name) from _call_process_hooks_15 #хук до инициализации сцены
#    $ renpy.free_memory()
    call expression scene_label from _call_expression_7
    call process_hooks("open", scene_name) from _call_process_hooks_16 #хук сразу после инициализации сцены
    return

label refresh_scene(fade_param = False):

    if fade_param != False:
        $ scene_transition = fade_param

    if EP1 == True:
        jump EP1_refresh_scene

    if sceneSpriteSurfacesCacheSceneName != scene_name:
        $ sceneSpriteSurfacesCacheIdle = {}
        $ sceneSpriteSurfacesCache = {}

    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ lastSceneName = scene_name
    call expression scene_name from _call_expression_8
    return

label refresh_scene_fade():
    $ scene_transition = "Fade"
    $ lastSceneName = scene_name
    call refresh_scene() from _call_refresh_scene
    return
label refresh_scene_fade_long():
    $ scene_transition = "Fade_long"
    $ lastSceneName = scene_name
    call refresh_scene() from _call_refresh_scene_1
    return

label remove_dialogue():
    python:
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = False
    return


label after_load():
#    $ renpy.free_memory()
#    if episode2part > 1:
#        img black_screen
#        help "Please use the newer version of the game."
##        help "Пожалуйста, используйте для загрузки более новую версию игры!"
#        $ MainMenu(confirm=False)()
#        return
    if SteamVersion1 == False:
        help "This save file is incompatible with the current game version. Please, start new game! Sorry!"
        $ MainMenu(confirm=False)()
        return
    $ list_files_active = True
    $ refresh_list_files ()
    if renpy.get_screen("show_image_screen") or renpy.get_screen("screen_sprites"):
        $ after_load_ready_to_render = False
        $ imageSizeClearCache()
        $ scene_data = process_scene_objects_list(scene_name) #парсим содержимое свойств объектов перед выводом
        $ scene_data = process_character_info_buttons(scene_data) #добавляем кнопки info для персонажей со свойствами
        if renpy.get_screen("show_image_screen"):
            show screen show_image_screen(scene_image_file)
        hide screen screen_sprites
#        if dialogue_active_flag == True or renpy.get_screen("dialogue_image_black_overlay") or renpy.get_screen("show_image_screen"):
#        if dialogue_active_flag == True or renpy.get_screen("dialogue_image_black_overlay") or renpy.get_screen("show_image_screen"):
#            pass
#        else:
#            show screen show_image_screen(scene_image_file)
        show screen screen_sprites(scene_data)
    $ after_load_ready_to_render = True

##    $ refresh_list_files_forced()
#    if episode < 2:
#        call start_saved_game() from _call_start_saved_game
#        return

#    if bardieCensored == False:
#        img black_screen
#        help "This game version is incompatible with this save file. Please, start new game."
##        help "Пожалуйста, используйте для загрузки более новую версию игры!"
#        $ MainMenu(confirm=False)()
#        return

#    if patch32applied == False:
#        $ remove_hook("map_teleport", "hook_basement_bedroom_check_exit_cloth_map", scene="global")
#        $ add_hook("map_teleport", "hook_basement_bedroom_check_exit_cloth_map", scene="global", priority=1000)
#        $ patch32applied = True
    if game_version1_screen_ready_to_render == False:
        $ game_version1_screen_ready_to_render = True
        call refresh_scene() from _call_refresh_scene_2
#    if ep23_quests_initialized == False:
#        call ep23_Quests_init() from _call_ep23_Quests_init
#    if ep24_quests_initialized == False:
#        call ep24_quests_init() from _call_ep24_quests_init
#    call ep24_quests_fix() from _call_ep24_quests_fix
#    if ep26_quests_initialized == False:
#        call ep26_quests1() from _call_ep26_quests1
#    if ep27_quests_initialized == False:
#        call ep27_quests1() from _call_ep27_quests1
#    call process_afterload() from _call_process_afterload

    $ imagesSizesCache = {}
#    call run_after_load() from _call_run_after_load
    return
    $ scene_refresh_flag = True #???
    $ show_scene_loop_flag = True
    jump show_scene
#    return

label call_save():
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    call screen save()
    return
