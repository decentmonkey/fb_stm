init python:
    def EP1_get_scene_label(scene_label):
        global sceneStages
        for idx in reversed(range(0, len(sceneStages))):
            if renpy.has_label(scene_label + sceneStages[idx]):
                return scene_label + sceneStages[idx]
        return scene_label

label EP1_change_scene(new_scene_name, in_transition_name="Fade", in_sound_name="highheels_short_walk"):
    if new_scene_name[:5] == "EP1_":
        $ new_scene_name = new_scene_name[5:]

    $ sceneIsStreet = False
    $ scene_transition = in_transition_name
    $ scene_sound = in_sound_name
    $ scene_refresh_flag = True
    $ lastSceneName = scene_name
    $ scene_name = new_scene_name

    $ scene_label = new_scene_name
    if renpy.has_label("EP1_" + scene_label):
        $ scene_label = "EP1_" + scene_label
    $ scene_label = EP1_get_scene_label(scene_label)
    call expression scene_label from _ep1_call_expression_7b
    return

label EP1_refresh_scene():
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ lastSceneName = scene_name
    $ scene_label = scene_name
    if renpy.has_label("EP1_" + scene_label):
        $ scene_label = "EP1_" + scene_label
    $ scene_label = EP1_get_scene_label(scene_label)
    call expression scene_label from _ep1_call_expression_5b
    return

label EP1_refresh_scene_fade():
    $ scene_transition = "Fade"
    $ lastSceneName = scene_name
    call EP1_refresh_scene() from _ep1_call_refresh_scene_34b
    return
label EP1_refresh_scene_fade_long():
    $ scene_transition = "Fade_long"
    $ lastSceneName = scene_name
    call EP1_refresh_scene() from _ep1_call_refresh_scene_35b
    return
