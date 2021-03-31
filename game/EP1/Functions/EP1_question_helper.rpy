#default questionHelperEnabled = False
#default questionHelperFuncName = False

label EP1_question_helper_enable(funcName):
    hide screen hud_screen
    $ questionHelperEnabled = True
    $ questionHelperFuncName = funcName
    show screen hud_screen(hud_presets[hud_preset_current])
    return

label EP1_question_helper_disable:
    $ questionHelperEnabled = False
    hide screen hud_screen
    show screen hud_screen(hud_presets[hud_preset_current])
    return

label EP1_question_helper_call:
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    if renpy.has_label("EP1_" + questionHelperFuncName):
        call expression "EP1_" + questionHelperFuncName from _ep1_call_expression_13b
    else:
        call expression questionHelperFuncName from _ep1_call_expression_13
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
