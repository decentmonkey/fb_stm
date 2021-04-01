screen EP1_hud_minimap(minimapData):
    layer "master"
    zorder 60
    fixed:
        if len(minimapData) > 0:
            pos (int(1711 * gui.resolution.koeff), int(85 * gui.resolution.koeff))
            if miniMapOpened == False:
                button:
                    action [
                        Call("EP1_miniMapOpen")
                    ]
                    yanchor 0.0
                    xanchor 0.5
                    xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                    padding (0,0)
                    $ imgName = get_image_filename("Open_Button_Map1" + res.suffix)
                    add imgName
                    text "":
                        xanchor 0.5
                        xpos 0.465
                        ypos 0.5
                        style "minimap_open_button_text"
            else:
                vbox:
                    button:
                        yanchor 0.0
                        xanchor 0.5
                        xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                        padding (0,0)
                        add get_image_filename("Open_Button_Map2" + res.suffix)
                        text "":
                            xanchor 0.5
                            xpos 0.465
                            ypos 0.5
                            style "minimap_open_button_text"
                        action [
                            Call("EP1_miniMapClose")
                        ]
                    null:
                        height 10
                    for minimapCell in minimapData:
#                       $ print minimapCell
                        $ locationDisabledFlag = False
                        if len(miniMapEnabledOnly) > 0:
                            if minimapCell["name"] in miniMapEnabledOnly:
                                $ locationDisabledFlag = False
                            else:
                                $ locationDisabledFlag = True
                        if minimapCell["name"] in miniMapDisabled:
                            $ locationDisabledFlag = True
                        $ print miniMapDisabled
                        button:
                            yanchor 0.0
                            xanchor 0.5
                            xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                            padding (0,0)
                            if locationDisabledFlag == False:
                                add get_image_filename(minimapCell["img"] + res.suffix)
                            else:
                                add get_image_filename(minimapCell["img"] + "_Disabled" + res.suffix)
                            if _preferences.language != "chinese":
                                text t__(minimapCell["caption"]):
                                    ypos 0.5
                                    xanchor 0.5
                                    xpos 0.465
                                    style "minimap_button_text"
                            else:
                                text t__(minimapCell["caption"]):
                                    ypos 0.5
                                    xanchor 0.5
                                    xpos 0.465
                                    style "minimap_button_text_chinese"
                            if locationDisabledFlag == False:
                                action [
                                    Return(["miniMapHouseGenerateTeleport", minimapCell["name"], minimapCell])
#                                   Return(False)
                                ]
                            else:
                                action [
                                    Return(["miniMapDisabled", minimapCell["name"], minimapCell])
                                ]
#                    hovered tt.Action("This is City 1")
                        null:
                            height 10
#        pos renpy.get_mouse_pos()
