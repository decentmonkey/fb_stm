################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

screen show_image_screen_image(image_name):
    layer "master"
    zorder 15

    if assetsStorageDirectory == False:
        $ assetsStorageDirectory = renpy.config.savedir.replace("/saves", "/assets")
    if image_name.find(assetsStorageDirectory) != -1:
        python:
            f = open(image_name,"rb")
            image_binary=f.read()
            f.close()
            img1 = im.Data(image_binary, image_name)

        fixed:
#            add img1 at convert_resolution_transform
            if blur_effect == 0:
                add img1
            else:
                add img1 at blur
                add img1:
                    alpha 0.2
                    xoffset -30
                if blur_effect > 1:
                    add img1:
                        alpha 0.2
                        xoffset 30
                if blur_effect > 2:
                    add img1:
                        alpha 0.2
                        yoffset -30
                if blur_effect > 3:
                    add img1:
                        alpha 0.2
                        yoffset 30
    else:
        fixed:
#            add image_name at convert_resolution_transform
            if blur_effect == 0:
                add image_name
            else:
                add image_name
                add image_name:
                    alpha 0.2
                    xoffset -30
                if blur_effect > 1:
                    add image_name:
                        alpha 0.2
                        xoffset 30
                if blur_effect > 2:
                    add image_name:
                        alpha 0.2
                        yoffset -30
                if blur_effect > 3:
                    add image_name:
                        alpha 0.2
                        yoffset 30



    if renpy.android:
        button:
            xfill True
            yfill True
            action [
                Return()
            ]
            alternate ShowMenu("save")

screen show_image_screen_image_overlay(image_name, canvas_offsets, overlayName):
    layer "master"
    zorder 16
    if canvas_offsets != False and canvas_offsets.has_key(str(overlayName)) != False:
        $ canvas_data = canvas_offsets[str(overlayName)]

        $ croppedOverlay = im.Crop(image_name, (getRes(canvas_data[3]), getRes(canvas_data[2]), getRes(canvas_data[1]), getRes(canvas_data[0])))
        add croppedOverlay:
            xpos getRes(canvas_data[5])
            ypos getRes(canvas_data[4])

screen show_image_screen(image_name):
    layer "master"
    if assetsStorageDirectory == False:
        $ assetsStorageDirectory = renpy.config.savedir.replace("/saves", "/assets")
    if image_name.find(assetsStorageDirectory) != -1:
        python:
            f = open(image_name,"rb")
            image_binary=f.read()
            f.close()
            img1 = im.Data(image_binary, image_name)

        fixed:
            add img1
    else:
        fixed:
            add image_name

screen credits_screen(creditsList):
    frame:
        background None
        at credits_transform

        $ ptr = 0
        for line1 in creditsList:
            $ lineType = line1[0]
            if lineType == 0:
                $ ptr += gui.credits.offset1
            if lineType == 1:
                text line1[1]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.5
                    style "credits_line1"
                $ ptr = ptr + gui.credits.offset2
            if lineType == 2:
                text line1[1]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.5
                    style "credits_line2"
                $ ptr = ptr + gui.credits.offset3
            if lineType == 3:
                text line1[1]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.5
                    style "credits_line3"
                $ ptr = ptr + gui.credits.offset4

            if lineType == 4:
                text line1[1] + "   ":
                    xpos 0.5
                    ypos ptr
                    xanchor 1.0
                    style "credits_line1"
                text "   " + line1[2]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.0
                    style "credits_line1"
                $ ptr = ptr + gui.credits.offset5

screen screen_sprites(data):
    zorder 10
    layer "master"
    default idle_num = 0.0

    fixed:
            button:
                xfill True
                yfill True
                action [
                    Hide("say"),
                    Hide("dialogue_image_left"),
                    Hide("dialogue_image_right"),
                    Hide("dialogue_image_center"),
                    Hide("dialogue_down_arrow"),
                    Hide("action_menu_screen"),
                    Hide("action_menu_tooltip_screen")
                ]
                if renpy.android:
                    alternate ShowMenu("save")

#                alternate [
#                    Hide("say"),
#                    Hide("dialogue_image_left"),
#                    Hide("dialogue_image_right"),
#                    Hide("dialogue_image_center"),
#                    Hide("dialogue_down_arrow"),
#                    Hide("action_menu_screen"),
#                    Hide("action_menu_tooltip_screen")
#                    Call("call_save")
#                ]

#            $ data = scenes_data["objects"][scene_name] if scene_name in scenes_data["objects"] else False
            if data != False and game_version1_screen_ready_to_render == True and episode == 2 and after_load_ready_to_render == True:
                $ zorder_list = []
                $ for i in data: zorder_list.append([i, data[i]["zorder"]])
                $ zorder_list.sort(key=lambda x:x[1])
#                $ print zorder_list
                for pass_num in range(1,3): #pass1 - overlays, pass2 - sprites and masks
                    for zorder_ptr in zorder_list:
                        $ i = zorder_ptr[0]
                        if (data[i].has_key("active") == False or data[i]["active"] == True) and (showObjectsNotOwner == True or checkObjectOwnerVisible(i, data[i]) == True):
                            $ tooltip_data = data[i]["tooltip"] if "tooltip" in data[i] else False
                            $ day_time_suffix = "_" + day_time if day_time in ["evening"] else ""
                            $ brightness_adjustment = 0.1
                            $ saturation_adjustment = 1.0
                            $ contrast_adjustment = 1.2
                            if data[i]["type"] == 0 :
                                $ varName = data[i]["text"]
                                text t__(varName)

                            $ mask_canvas_offset = data[i]["canvas_img" + day_time_suffix + "_mask"] if data[i].has_key("canvas_img" + day_time_suffix + "_mask") != False else data[i]["canvas_img_mask"] if data[i].has_key("canvas_img_mask") != False else False
                            $ canvas_offset = data[i]["canvas_img" + day_time_suffix] if data[i].has_key("canvas_img" + day_time_suffix) != False else data[i]["canvas_img"] if data[i].has_key("canvas_img") else False
                            if canvas_offset == False:
                                $ canvas_offset = mask_canvas_offset
                            $ overlay_canvas_offset = data[i]["canvas_img" + day_time_suffix + "_overlay"] if data[i].has_key("canvas_img" + day_time_suffix + "_overlay") != False else data[i]["canvas_img_overlay"] if data[i].has_key("canvas_img_overlay") else False

                            if data[i]["type"] == 2: #overlay image, with mask (if exists)
        #                        $ print data[i]
                                $ spriteImageStr = data[i]["img" + day_time_suffix] if data[i]["img" + day_time_suffix] != False else data[i]["img"] if data[i]["img"] != False else scene_image_file
                                $ maskName = data[i]["img" + day_time_suffix + "_mask"] if data[i]["img" + day_time_suffix + "_mask"] != False else data[i]["img" +"_mask"] if data[i]["img" +"_mask"] != False else False

        #                        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskName)),zoom_factor) if maskName != False else im.FactorScale(Image(spriteImageStr),zoom_factor)
        #                        if data[i].has_key("name") and data[i]["name"] == "Spot":
        #                            $ print data[i]
                                $ screenCache = True
                                if pass_num == 2:
                                    if sceneSpriteSurfacesCacheIdle.has_key(scene_name + i) == False or 1==1:
                                        $ screenCache = False
                                        if canvas_offset != False and spriteImageStr == scene_image_file:
                #                            $ idleImg = Image(spriteImageStr)
                                            $ maskImage = Image(maskName)
                                            $ maskImageSize = getImageSize(maskImage, maskName)
                                            $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                                            $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                                            $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                                            $ idleImg = im.AlphaMask(croppedImg, maskImage) if maskName != False else Image(spriteImageStr)
                                        else:
                                            if canvas_offset != False and spriteImageStr != scene_image_file and maskName != False:
                                                $ maskImage = Image(maskName)
                                                $ maskImageSize = getImageSize(maskImage, maskName)
                                                $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                                                $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                                                $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                                                $ idleImg = im.AlphaMask(croppedImg, maskImage) if maskName != False else Image(spriteImageStr)
                                            else:
                                                $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskName)) if maskName != False else Image(spriteImageStr)
#                                        $ idleImg = Flatten(idleImg)
                                        #$ sceneSpriteSurfacesCacheIdle[scene_name + i] = Flatten(idleImg)
                                    else:
                                        $ idleImg = sceneSpriteSurfacesCacheIdle[scene_name + i]
                                    $ hoverImg = idleImg
                                $ overlayName = data[i]["img" + day_time_suffix + "_overlay"] if data[i]["img" + day_time_suffix + "_overlay"] != False else data[i]["img" + "_overlay"] if data[i]["img" + "_overlay"] != False else False
                                if pass_num == 1:
                                    if overlayName != False:
#                                        add overlayName at convert_resolution_transform:
                                        add overlayName:
                                            if overlay_canvas_offset != False:
                                                xpos overlay_canvas_offset[1]
                                                ypos overlay_canvas_offset[0]
                                            if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                                xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                                ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                        if data[i]["hover_overlay"] == True:
                                            if overlay_canvas_offset != False and mask_canvas_offset != False:
                                                $ overlayImage = Image(overlayName)
                                                $ overlayImageSize = getImageSize(overlayImage, overlayName)
                                                $ overlay_canvas_offset[2] = overlay_canvas_offset[0] + overlayImageSize[1] - 1
                                                $ overlay_canvas_offset[3] = overlay_canvas_offset[1] + overlayImageSize[0] - 1
                                                $ maskCompositeImage = im.Composite((overlay_canvas_offset[3] - overlay_canvas_offset[1] + 1, overlay_canvas_offset[2] - overlay_canvas_offset[0]+1), (mask_canvas_offset[1] - overlay_canvas_offset[1], mask_canvas_offset[0] - overlay_canvas_offset[0]), maskName)
                                                $ hoverImg = im.AlphaMask(Image(overlayName), maskCompositeImage)
                                            else:
                                                $ hoverImg = im.AlphaMask(Image(overlayName), Image(maskName)) if maskName != False else Image(overlayName)

            #                                $ hoverImg = im.FactorScale(im.AlphaMask(Image(overlayName), Image(maskName)),zoom_factor) if maskName != False else im.FactorScale(Image(overlayName),zoom_factor)
                                if pass_num == 2:
                                    if spriteImageStr != scene_image_file:
                                        add idleImg:
                                            if canvas_offset != False:
                                                xpos canvas_offset[1]
                                                ypos canvas_offset[0]
                                            if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                                xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                                ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                    if spriteImageStr == scene_image_file: #добавляем яркость на фоновых предметах
                                        $ brightness_adjustment = 0.1
                                        $ saturation_adjustment = 1.07
                                        $ contrast_adjustment = 1.3
                                    $ if data[i].has_key("b") == True: brightness_adjustment = data[i]["b"]
                                    $ if data[i].has_key("s") == True: saturation_adjustment = data[i]["s"]
                                    $ if data[i].has_key("c") == True: contrast_adjustment = data[i]["c"]
                                    $ tint_adjustment = False
                                    $ if data[i].has_key("tint") == True: tint_adjustment = data[i]["tint"]
                                    if data[i].has_key("hover_enabled") == False or data[i]["hover_enabled"] == True:
                                        if sceneSpriteSurfacesCache.has_key(scene_name + i) == False or screenCache == False or 1==1:
                                            if tint_adjustment != False:
                                                $ hoveredImage = im.MatrixColor(
                                                    idleImg,
                                                    im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
                                                )
                                            else:
                                                $ hoveredImage = im.MatrixColor(
                                                    hoverImg,
                                                    im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment)
                                                )
                                            #$ hoveredImage = Flatten(hoveredImage)
                                            #$ sceneSpriteSurfacesCache[scene_name + i] = hoveredImage
                                        else:
                                            $ hoveredImage = sceneSpriteSurfacesCache[scene_name + i]
                                        imagebutton:
                                            if canvas_offset != False:
                                                xpos canvas_offset[1]
                                                ypos canvas_offset[0]
                                            if data[i]["hover_overlay"] == True:
                                                xpos overlay_canvas_offset[1]
                                                ypos overlay_canvas_offset[0]

                                            if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                                xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                                ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                            idle hoveredImage
                                            hover hoveredImage
                                            if data[i].has_key("hovered_caption"):
                                                hovered [SetScreenVariable("idle_num", 0.4), Show("sprite_hovered_caption_screen", None, data[i]["hovered_caption"])]
                                            else:
                                                hovered [SetScreenVariable("idle_num", 0.4)]
                                            unhovered Hide("sprite_hovered_caption_screen")
                                            at imagebutton_hover_type1(idle_num)
                                            focus_mask True
                                            if data[i]["actions"] == "l" and check_object_has_character(i) == False: #если объекту не заданы действия кроме просмотра, то не выводим доп. меню
                                                action [
                                                    Return(["process_object_click", data[i]["click"], i, data[i]]),
                                                ]
                                            else:
                                                action [
                                                    Show("action_menu_screen", None, data[i]["click"], i, data[i]),
                                                ]

            #                                alternate Show("action_menu_screen", None, data[i]["click"], i, data[i])
#                                            alternate Call("call_save")

                            if data[i]["type"] == 3: #text with image
                                $ button_layout = data[i]["layout"] if data[i].has_key("layout") else text_button_default_layout
                                $ tint_adjustment = [1.0, 1.0, 1.0]
                                $ if data[i].has_key("b") == True: brightness_adjustment = data[i]["b"]
                                $ if data[i].has_key("s") == True: saturation_adjustment = data[i]["s"]
                                $ if data[i].has_key("c") == True: contrast_adjustment = data[i]["c"]
                                $ if data[i].has_key("tint") == True: tint_adjustment = data[i]["tint"]
                                $ spriteStr = data[i]["img" + day_time_suffix] if data[i]["img" + day_time_suffix] != False else data[i]["img"] if data[i]["img"] != False else False
                                $ maskStr = data[i]["img" + day_time_suffix + "_mask"] if data[i]["img" + day_time_suffix + "_mask"] != False else data[i]["img" +"_mask"] if data[i]["img" +"_mask"] != False else False
                                $ if spriteStr != False: maskStr = False #убираем маску если есть спрайт
                                $ overlayName = data[i]["img" + day_time_suffix + "_overlay"] if data[i]["img" + day_time_suffix + "_overlay"] != False else data[i]["img" + "_overlay"] if data[i]["img" + "_overlay"] != False else False

                                $ left_arrow = data[i]["larrow"]
                                $ right_arrow = data[i]["rarrow"]
                                $ disableSprite = False
                                $ if spriteStr == False and maskStr == False and overlayName == False: disableSprite = True
                                if pass_num == 1:
                                    if overlayName != False:
#                                        add overlayName at convert_resolution_transform:
                                        add overlayName:
                                            if overlay_canvas_offset != False:
                                                xpos overlay_canvas_offset[1]
                                                ypos overlay_canvas_offset[0]
                                            if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                                xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                                ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                            if data[i].has_key("sprite_align"):
                                                if data[i]["sprite_align"] == "dc":
                                                    anchor (0.5, 1.0)

                                if pass_num == 2:
                                    $ object_z_order = int(data[i]["zorder"])
                                    $ highSpriteHover = False
                                    $ if data[i].has_key("high_sprite_hover") and data[i]["high_sprite_hover"] == True: highSpriteHover = True #костыль
                                    button:
                                        xpos int(float(data[i]["xpos"]) / 1920.0 * config.screen_width)
                                        ypos int(float(data[i]["ypos"]) / 1080.0 * config.screen_height)
                                        anchor (0.5,0.5)
                                        frame:
                                            background Solid("#18181a")
                                            margin (0,0)
                                            padding text_button_layouts[button_layout]["text_button.padding"]
                                            style "sprite_textbutton_frm"
                                            hbox:
                                                if left_arrow != False:
                                                    null:
                                                        width text_button_layouts[button_layout]["text_button.spacing1"]
                                                    add left_arrow:
                                                        yalign 0.5
                                                null:
                                                    width text_button_layouts[button_layout]["text_button.spacing2"]
                                                if _preferences.language != "chinese":
                                                    text t__(data[i]["text"]) style text_button_layouts[button_layout]["text_button.style"]
                                                else:
                                                    text t__(data[i]["text"]) style text_button_layouts[button_layout]["text_button.style"]:
                                                        font gui.text_font_chinese
                                                null:
                                                    width text_button_layouts[button_layout]["text_button.spacing2"]
                                                if right_arrow != False:
                                                    add right_arrow:
                                                        yalign 0.5
                                                    null:
                                                        width text_button_layouts[button_layout]["text_button.spacing1"]

                                        if highSpriteHover == False:
                                            hovered [
                                                Show("hover_text_sprite", None, spriteStr, maskStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data[i], canvas_offset,i)
            #                                   With(dissolve)
                                            ]
                                        else:
                                            hovered [
                                                Show("hover_text_sprite_high_hover_sprite", None, spriteStr, maskStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data[i], canvas_offset,i)
            #                                   With(dissolve)
                                            ]
                                        if highSpriteHover == False:
                                            unhovered [
                                                Hide("hover_text_sprite", Dissolve(0.4)),
                                            ]
                                        else:
                                            unhovered [
                                                Hide("hover_text_sprite_high_hover_sprite", Dissolve(0.4)),
                                            ]
                                        action Return(["process_object_click", data[i]["click"], i, data[i]])

                                    $ spriteImageStr = spriteStr if spriteStr != False else scene_image_file
            #                        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskStr)),zoom_factor) if maskStr != False else im.FactorScale(Image(spriteImageStr),1.5)
            #                        $ idleImg = Image(spriteImageStr)
                                    if sceneSpriteSurfacesCacheIdle.has_key(scene_name + i) == False or 1==1:
                                        if maskStr != False:
                                            if mask_canvas_offset != False and spriteImageStr == scene_image_file:
                #                                $ idleImg = Image(spriteImageStr)
                                                $ maskImage = Image(maskStr)
                                                $ maskImageSize = getImageSize(maskImage, maskStr)
                                                $ mask_canvas_offset[2] = mask_canvas_offset[0] + maskImageSize[1] - 1
                                                $ mask_canvas_offset[3] = mask_canvas_offset[1] + maskImageSize[0] - 1
                                                $ croppedImg = im.Crop(spriteImageStr, (mask_canvas_offset[1], mask_canvas_offset[0], mask_canvas_offset[3]-mask_canvas_offset[1]+1, mask_canvas_offset[2] - mask_canvas_offset[0]+1))
                                                $ idleImg = im.AlphaMask(croppedImg, maskImage)
                                            else:
                                                $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskStr)) if maskStr != False else Image(spriteImageStr)

    #                                        else:
    #                                            $ idleImg = Image(spriteImageStr)
                                        else:
                                            $ idleImg = Image(spriteImageStr)
                                        #$ sceneSpriteSurfacesCacheIdle[scene_name + i] = Flatten(idleImg)
                                    else:
                                        $ idleImg = sceneSpriteSurfacesCacheIdle[scene_name + i]

                                    if sceneSpriteSurfacesCache.has_key(scene_name + i) == False or 1==1:
                                        $ spriteImage = im.MatrixColor(
                                            idleImg,
                                            im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
                                        )
                                        #$ sceneSpriteSurfacesCache[scene_name + i] = Flatten(spriteImage)
                                    else:
                                        $ spriteImage = sceneSpriteSurfacesCache[scene_name + i]

                                    if spriteStr != False or maskStr != False or overlayName != False:
                                        imagebutton:
                                            if canvas_offset != False:
                                                xpos canvas_offset[1]
                                                ypos canvas_offset[0]
                                            if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                                xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                                ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                            if data[i].has_key("sprite_align"):
                                                if data[i]["sprite_align"] == "dc":
                                                    anchor (0.5, 1.0)
                                            idle spriteImage
                                            hover spriteImage
                                            hovered [
                                                SetScreenVariable("idle_num", 0.4),
                                                Show("hover_sprite_text", None, i, data[i], left_arrow, right_arrow, button_layout)
            #                                    Show("hover_sprite_text", Dissolve(0.2), i, data[i])
                                            ]
            #                                unhovered Hide("hover_sprite_text", Dissolve(0.4))
                                            unhovered Hide("hover_sprite_text", None)
                                            at imagebutton_hover_type1(idle_num)
                                            focus_mask True
                                            action Return(["process_object_click", data[i]["click"], i, data[i]])

    key "e" action [
        Return(["show_questhelp"]),
    ]

screen hover_text_sprite(spriteImageStr, maskImageStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data, canvas_offset, i=""):
    layer "master"
#    zorder 10

    if disableSprite == False:
        $ spriteImageStr = spriteImageStr if spriteImageStr != False else scene_image_file
#        $ print maskImageStr
#        $ print spriteImageStr
#        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)),zoom_factor) if maskImageStr != False else im.FactorScale(Image(spriteImageStr),zoom_factor)

        if sceneSpriteSurfacesCacheIdle.has_key(scene_name + i) == False or sceneSpriteSurfacesCache.has_key(scene_name + i) == False or 1==1:
            if maskImageStr != False:
                if canvas_offset != False and spriteImageStr == scene_image_file:
                    $ maskImage = Image(maskImageStr)
                    $ maskImageSize = getImageSize(maskImage, maskImageStr)
                    $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                    $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                    $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                    $ idleImg = im.AlphaMask(croppedImg, maskImage)
                else:
                    $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)) if maskImageStr != False else Image(spriteImageStr)
    #                $ idleImg = Image(spriteImageStr)
            else:
                $ idleImg = Image(spriteImageStr)
    #        $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)) if maskImageStr != False else Image(spriteImageStr)
            #$ sceneSpriteSurfacesCacheIdle[scene_name + i] = Flatten(idleImg)
        else:
            $ idleImg = sceneSpriteSurfacesCacheIdle[scene_name + i]

        if sceneSpriteSurfacesCache.has_key(scene_name + i) == False or 1==1:
            $ spriteImage = im.MatrixColor(
                idleImg,
                im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
            )
            #$ sceneSpriteSurfacesCache[scene_name + i] = Flatten(spriteImage)
        else:
            $ spriteImage = sceneSpriteSurfacesCache[scene_name + i]
        fixed:
            add spriteImage at hover_text_sprite_transform:
                if canvas_offset != False:
                    xpos canvas_offset[1]
                    ypos canvas_offset[0]
                if data.has_key("xsprite") and data.has_key("ysprite"):
                    xpos int(float(data["xsprite"]) / 1920.0 * config.screen_width)
                    ypos int(float(data["ysprite"]) / 1080.0 * config.screen_height)
                if data.has_key("sprite_align"):
                    if data["sprite_align"] == "dc":
                        anchor (0.5, 1.0)
screen hover_text_sprite_high_hover_sprite(spriteImageStr, maskImageStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data, canvas_offset, i=""):
    layer "master"
    zorder 100

    if disableSprite == False:
        $ spriteImageStr = spriteImageStr if spriteImageStr != False else scene_image_file
#        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)),zoom_factor) if maskImageStr != False else im.FactorScale(Image(spriteImageStr),zoom_factor)

        if sceneSpriteSurfacesCacheIdle.has_key(scene_name + i) == False or 1==1:
            if maskImageStr != False:
                if canvas_offset != False and spriteImageStr == scene_image_file:
                    $ maskImage = Image(maskImageStr)
                    $ maskImageSize = getImageSize(maskImage, maskImageStr)
                    $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                    $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                    $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                    $ idleImg = im.AlphaMask(croppedImg, maskImage)
                else:
                    $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)) if maskImageStr != False else Image(spriteImageStr)
                    #$ idleImg = Image(spriteImageStr)
            else:
                $ idleImg = Image(spriteImageStr)
    #        $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)) if maskImageStr != False else Image(spriteImageStr)
            #$ sceneSpriteSurfacesCacheIdle[scene_name + i] = Flatten(idleImg)
        else:
            $ idleImg = sceneSpriteSurfacesCacheIdle[scene_name + i]

        if sceneSpriteSurfacesCache.has_key(scene_name + i) == False or 1==1:
            $ spriteImage = im.MatrixColor(
                idleImg,
                im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
            )
            #$ sceneSpriteSurfacesCache[scene_name + i] = Flatten(spriteImage)
        else:
            $ spriteImage = sceneSpriteSurfacesCache[scene_name + i]
        fixed:
            add spriteImage at hover_text_sprite_transform:
                if canvas_offset != False:
                    xpos canvas_offset[1]
                    ypos canvas_offset[0]
                if data.has_key("xsprite") and data.has_key("ysprite"):
                    xpos int(float(data["xsprite"]) / 1920.0 * config.screen_width)
                    ypos int(float(data["ysprite"]) / 1080.0 * config.screen_height)
                if data.has_key("sprite_align"):
                    if data["sprite_align"] == "dc":
                        anchor (0.5, 1.0)

screen hover_sprite_text(name, data, left_arrow, right_arrow, button_layout):
    layer "master"
    zorder 11
    button:
        xpos int(float(data["xpos"]) / 1920.0 * config.screen_width)
        ypos int(float(data["ypos"]) / 1080.0 * config.screen_height)
        anchor (0.5,0.5)
        frame:
            background Solid("#18181a")
            margin (0,0)
            padding text_button_layouts[button_layout]["text_button.padding"]
            style "sprite_textbutton_frm"
            hbox:
                if left_arrow != False:
                    null:
                        width text_button_layouts[button_layout]["text_button.spacing1"]
                    add left_arrow:
                        yalign 0.5
                null:
                    width text_button_layouts[button_layout]["text_button.spacing2"]
                if _preferences.language != "chinese":
                    text t__(data["text"]) style text_button_layouts[button_layout]["text_button.force_hovered.style"]
                else:
                    text t__(data["text"]) style text_button_layouts[button_layout]["text_button.force_hovered.style"]:
                        font gui.text_font_chinese
                null:
                    width text_button_layouts[button_layout]["text_button.spacing2"]
                if right_arrow != False:
                    add right_arrow:
                        yalign 0.5
                    null:
                        width text_button_layouts[button_layout]["text_button.spacing1"]

# Меню по клику правой кнопки мыши
screen action_menu_screen(click_label, name, data):
    default tt = Tooltip("No button selected.")
    $ getMousePosition()
    default x = -1
    default y = -1
    if x == -1 and y == -1:
        $ x,y = renpy.get_mouse_pos()
    $ menu_len = (len(data["actions"]) + len(inventory)) * gui.resolution.action_menu.inventory_len1 + gui.resolution.action_menu.inventory_len2
    if x + menu_len > config.screen_width:
        $ x = config.screen_width - menu_len
    if y + gui.resolution.action_menu.menu_height > config.screen_height:
        $ y = config.screen_height - gui.resolution.action_menu.menu_height

    layer "master"
    zorder 20

    fixed:
        button:
            xfill True
            yfill True
            action [
                Hide("say"),
                Hide("dialogue_image_left"),
                Hide("dialogue_image_right"),
                Hide("dialogue_image_center"),
                Hide("dialogue_down_arrow"),
                Hide("action_menu_screen"),
                Hide("action_menu_tooltip_screen")
            ]
#            alternate [
#                Hide("say"),
#                Hide("dialogue_image_left"),
#                Hide("dialogue_image_right"),
#                Hide("dialogue_image_center"),
#                Hide("dialogue_down_arrow"),
#                Hide("action_menu_screen"),
#                Hide("action_menu_tooltip_screen")
#            ]

        frame:
#            background Solid("#242426")
            background Frame("gui/frame2.png", left=2, top=2, right=2, bottom=2)
            pos(x, y)
            anchor(-10, -10)
            xpadding gui.resolution.action_menu.padding1
            ypadding gui.resolution.action_menu.padding1
            hbox:
                spacing gui.resolution.action_menu.spacing1
                #actions
                $ actions_list = get_object_actions(data["actions"])
                $ idx = 0
                $ item_offset = gui.resolution.action_menu.item_offset_init
                for action_data in actions_list:
#                    $ icon_image = Image(action_data["icon"])
                    $ iconImg = action_data["icon"]
                    if data.has_key("icon_" + action_data["action"]):
                        $ iconImg = data["icon_" + action_data["action"]]
                    $ icon_image_idle = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/action_icon_background_idle" + res.suffix + ".jpg", (0,0), parseFileNameResSuffix(iconImg))
                    $ icon_image_hover = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/action_icon_background_hover" + res.suffix + ".jpg", (0,0), parseFileNameResSuffix(iconImg))
                    imagebutton:
                        background Solid("#000000")
                        xysize(gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size)
                        idle icon_image_idle
                        hover icon_image_hover xalign 0.5 yalign 0.5
                        action [
                            Hide("action_menu_tooltip_screen"),
                            Return(["process_object_click_alternate_action", idx, actions_list, click_label, name, data])
                        ]
                        hovered Show("action_menu_tooltip_screen", None, x, y, item_offset, action_data["description"], "#83bac4")
                        unhovered Hide("action_menu_tooltip_screen")
                    $ idx += 1
                    $ item_offset += gui.resolution.action_menu.item_offset

                if len(inventory) > 0:
                    null:
                        width 0
                    $ item_offset += gui.resolution.action_menu.item_offset_inv
                #inventory
                for idx in range(0, len(inventory)):
#                    $ print(inventory[idx])
                    $ inventory_data = inventory_objects[inventory[idx][0]]
                    $ icon_image_idle = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/inventory_icon_background_idle" + res.suffix + ".jpg", (0,0), parseFileNameResSuffix(inventory_data["icon"]))
                    $ icon_image_hover = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/inventory_icon_background_hover" + res.suffix + ".jpg", (0,0), parseFileNameResSuffix(inventory_data["icon"]))
                    imagebutton:
                        id inventory[idx][0] + "_displayable"
                        xysize(gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size)
                        idle icon_image_idle
                        hover icon_image_hover xalign 0.5 yalign 0.5
                        hovered Show("action_menu_tooltip_screen", None, x, y, item_offset, inventory_data["description"], "#ffa8a8")
                        unhovered Hide("action_menu_tooltip_screen")
                        action [
                            Hide("action_menu_tooltip_screen"),
                            Return(["process_object_click_alternate_inventory", idx, inventory_data, click_label, name, data])
                        ]
                    $ item_offset += gui.resolution.action_menu.item_offset

screen dialogue_down_arrow(): #мигающая стрелка внизу
    fixed:
        add "down_arrow" at dialogue_down_arrow_transform

screen sprites_hover_dummy_screen():
    layer "master"
    zorder 25
    fixed:
        button:
            xfill True
            yfill True
            action Return(False)

screen sprite_hovered_caption_screen(caption_text):
    layer "master"
    zorder 51
    fixed:
        xpos getRes(1920/2)
        ypos getRes(130)
#        xpos 0
#        ypos 0

        frame:
            anchor (0.5,0.5)
            xpos 0
            ypos 0
            background Solid("#18181a")
            margin (0,0)
            padding text_button_layouts[text_button_default_layout]["text_button.padding"]
            style "sprite_textbutton_frm"
            hbox:
                null:
                    width text_button_layouts[text_button_default_layout]["text_button.spacing2"]
                if _preferences.language != "chinese":
                    text t__(caption_text) style text_button_layouts[text_button_default_layout]["text_button.force_hovered.style"]
                else:
                    text t__(caption_text) style text_button_layouts[text_button_default_layout]["text_button.force_hovered.style"]:
                        font gui.text_font_chinese
                null:
                    width text_button_layouts[text_button_default_layout]["text_button.spacing2"]


screen dialogue_image_black_overlay():
    layer "master"
    zorder 28
    fixed:
        xpos 0.0
        ypos 0.0
        button:
            padding (0,0)
            xfill True
            yfill True
            add "Overlays/black.png"
            action Return(False)


screen dialogue_image_left(img, img_width, img_height): #изображение слева
    layer "master"
    zorder 30
    fixed:
        xpos 0.0
        ypos 0.0
        xmaximum 0.5
        ymaximum 1.0
        add img at dialogue_image_left:
            maxsize (img_width,img_height)

screen dialogue_image_right(img, img_width, img_height): #изображение справа
    layer "master"
    zorder 30
    fixed:
        xpos 0.5
        ypos 0.0
        xmaximum 0.5
        ymaximum 1.0
        add img at dialogue_image_right:
            maxsize (img_width,img_height)

screen dialogue_image_center(img, img_width, img_height): #изображение по центру
    layer "master"
    zorder 30
    fixed:
        xpos 0.0
        ypos 0.0
        add img at dialogue_image_center:
            maxsize (img_width,img_height)

screen action_menu_tooltip_screen(in_x, in_y, item_offset, tooltip_text, in_text_color):
    $ in_x = in_x + item_offset + gui.resolution.action_menu.tooltip.offset_x
    $ in_y = in_y + gui.resolution.action_menu.tooltip.offset_y

    frame:
        xpos in_x
        ypos in_y
        xanchor 0.5
        background Frame("gui/frame2.png", left=2, top=0, right=2, bottom=2)
        if _preferences.language != "chinese":
            text t__(tooltip_text):
                size gui.resolution.action_menu.tooltip.font_size
    #            color "#ffc9c9"
                color in_text_color
        else:
            text t__(tooltip_text):
                size gui.resolution.action_menu.tooltip.font_size
                color in_text_color
                font gui.text_font_chinese

screen character_info_screen(obj_name, x, y):
    $ width1 = int(720 * gui.resolution.koeff)
    $ height1 = int(320 * gui.resolution.koeff)
    $ style1 = char_info[obj_name]["style"]
    $ x = x - int(width1/3)
    $ y = y - int(height1/3)
    if (1920*gui.resolution.koeff) - (x + width1) < 273*gui.resolution.koeff:
        $ x = int((1920*gui.resolution.koeff) - width1 - (273*gui.resolution.koeff))
    if x < ((273+210)*gui.resolution.koeff):
        $ x = int((273+210)*gui.resolution.koeff)
    if (1080*gui.resolution.koeff) - (y + height1 )< (144*gui.resolution.koeff):
        $ y = int((1080*gui.resolution.koeff) - height1 - (144*gui.resolution.koeff))
    if y < (300*gui.resolution.koeff):
        $ y = int((300*gui.resolution.koeff))

    if char_info[obj_name]["enabled"] == True:
        $ captionText = t__(char_info[obj_name]["caption"])
        $ barSuffix = char_info[obj_name]["bar_suffix"]
        $ barValue = (100.0 / char_info[obj_name]["max_progress"] * char_info[obj_name]["current_progress"]) / 100.0
    else:
        $ captionText = t__(char_info[obj_name]["caption_diabled"])
        $ barSuffix = "disabled"
        $ barValue = 1.0
    layer "master"
    zorder 40
    fixed:
        button:
            xfill True
            yfill True
            action [
                Hide("say"),
                Hide("dialogue_image_left"),
                Hide("dialogue_image_right"),
                Hide("dialogue_image_center"),
                Hide("dialogue_down_arrow"),
                Hide("action_menu_screen"),
                Hide("action_menu_tooltip_screen"),
                Hide("sprites_hover_dummy_screen"),
                Hide("character_info_screen")
            ]
#            alternate [
#                Hide("say"),
#                Hide("dialogue_image_left"),
#                Hide("dialogue_image_right"),
#                Hide("dialogue_image_center"),
#                Hide("dialogue_down_arrow"),
#                Hide("action_menu_screen"),
#                Hide("action_menu_tooltip_screen"),
#                Hide("sprites_hover_dummy_screen"),
#                Hide("character_info_screen")
#            ]

        frame:
#            background Solid("#242426")
            background Frame("gui/frame3" + res.suffix + ".png", left=2, top=int(80*gui.resolution.koeff), right=2, bottom=2)
            pos(x, y)
            anchor(0, 0)
            xysize (width1, height1)
            $ imgName = get_image_filename(char_info[obj_name]["face"])
            add imgName:
                xpos int(-80 * gui.resolution.koeff)
                ypos 0.5
                anchor(0.5,0.5)

#            text t__(data[i]["text"]) style text_button_layouts[button_layout]["text_button.style"]
            if _preferences.language != "chinese":
                text t__(char_info[obj_name]["name"]) style (style1 + "_head")
                text t__(char_info[obj_name]["progress_caption"]) + "{c}" + str(char_info[obj_name]["level"]) + "{/c}" style "char_face_style_progress"
                text str(char_info[obj_name]["current_progress"]) + " / " + str(char_info[obj_name]["max_progress"]) style "char_face_style_progress2"
            else:
                text t__(char_info[obj_name]["name"]) style (style1 + "_head"):
                    font gui.text_font_chinese
                text t__(char_info[obj_name]["progress_caption"]) + "{c}" + str(char_info[obj_name]["level"]) + "{/c}" style "char_face_style_progress":
                    font gui.text_font_chinese
                text str(char_info[obj_name]["current_progress"]) + " / " + str(char_info[obj_name]["max_progress"]) style "char_face_style_progress2":
                    font gui.text_font_chinese
            bar:
                xpos 0.52
                ypos 0.61
                xsize int(365 * gui.resolution.koeff)
                anchor (0.5, 0.0)
                value barValue
#                xysize(gui.resolution.hud_screen.bitchmeter_x_size,gui.resolution.hud_screen.bitchmeter_y_size)
                bar_vertical False
                right_bar "/icons/bar/bar2_empty" + res.suffix + ".png"
                left_bar "/icons/bar/bar2_full_" + barSuffix + res.suffix + ".png"
            if _preferences.language != "chinese":
                text t__(captionText) style "char_face_style_caption":
                    xsize int(width1 / 1.94594595)
                    justify True
            else:
                text t__(captionText) style "char_face_style_caption":
                    xsize int(width1 / 1.94594595)
                    justify True
                    font gui.text_font_chinese
#                thumb "/icons/bar/bar_thumb" + res.suffix + ".png"
            imagebutton:
                xpos 1.0
                ypos 0.0
                anchor (0.5, 0.5)
                idle "/icons/window_close" + res.suffix + ".png"
                hover "/icons/window_close_hover" + res.suffix + ".png"
                action [
                    Hide("say"),
                    Hide("dialogue_image_left"),
                    Hide("dialogue_image_right"),
                    Hide("dialogue_image_center"),
                    Hide("dialogue_down_arrow"),
                    Hide("action_menu_screen"),
                    Hide("action_menu_tooltip_screen"),
                    Hide("sprites_hover_dummy_screen"),
                    Hide("character_info_screen")
                ]
screen hud_minimap(minimapData):
    layer "master"
    zorder 60
    python:
        if minimap_coords_preset == 0:
            minimap_pos_x = gui.resolution.hud_screen.minimap_x_pos
            minimap_pos_y = gui.resolution.hud_screen.minimap_y_pos
        if minimap_coords_preset == 1:
            minimap_pos_x = gui.resolution.hud_screen.minimap_x_pos_owner
            minimap_pos_y = gui.resolution.hud_screen.minimap_y_pos_owner

    if miniMapTurnedOff2 == False:
        fixed:
            if len(minimapData) > 0:
                pos (int(minimap_pos_x * gui.resolution.koeff), int(minimap_pos_y * gui.resolution.koeff))
                if miniMapOpened == False:
                    button:
                        yanchor 0.0
                        xanchor 0.5
                        xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                        padding (0,0)
                        action [
                            Call("miniMapOpen")
                        ]
    #                        imgName = get_image_filename(miniMapOpenButtonImg + res.suffix)
                        add get_image_filename(miniMapOpenButtonImg + res.suffix)
                        text "":
                            xanchor 0.5
                            xpos 0.465
                            ypos 0.5
                            style "minimap_open_button_text"
    #                    action Call("miniMapOpen")
                else:
                    vbox:
                        button:
                            yanchor 0.0
                            xanchor 0.5
                            xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                            padding (0,0)
                            add get_image_filename(miniMapOpenButtonImg2 + res.suffix)
                            text "":
                                xanchor 0.5
                                xpos 0.465
                                ypos 0.5
                                style "minimap_open_button_text"
                            action [
                                Call("miniMapClose")
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
    #                        if minimapCell["name"] in miniMapDisabled:
    #                            $ locationDisabledFlag = True
                            $ minimapCheckMapScene = map_scene
                            if map_scene == "Hostel2" or map_scene == "Cloth_Shop":
                                $ minimapCheckMapScene = "Street_Corner"
                            if miniMapDisabled.has_key(minimapCheckMapScene) and minimapCell["name"] in miniMapDisabled[minimapCheckMapScene]:
                                $ locationDisabledFlag = True
                            if (cloth == "CasualDress1" or cloth == "SchoolOutfit1") and miniMapDisabled2.has_key(minimapCheckMapScene) and minimapCell["name"] in miniMapDisabled2[minimapCheckMapScene]:
                                $ locationDisabledFlag = True
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

screen hud_screen(hud_presets):
    layer "master"
    zorder 50
    fixed:
        pos (gui.resolution.hud_screen.value1_1,gui.resolution.hud_screen.value1_2)
        vbox:
            hbox:
                spacing gui.resolution.hud_screen.spacing2
                #время дня
                if hud_presets["display_daytime"] == True:
                    if day_time == "day":
                        if dialogue_active_flag == True or sceneIsStreet != True or hudDaySkipToEveningEnabled == False:
                            imagebutton:
                                yoffset -2
                                xanchor 2
                                idle "/icons/daytime_day" + res.suffix + ".png"
                                hover "/icons/daytime_day_hover_disabled" + res.suffix + ".png"
                                action [
                                    Play("sound", "Sounds/click_denied.ogg")
                                ]
                        else:
                            imagebutton:
                                yoffset -2
                                xanchor 2
                                idle "/icons/daytime_day" + res.suffix + ".png"
                                hover "/icons/daytime_day_hover" + res.suffix + ".png"
                                action [
                                    Return(["time_management_street_wait_until_evening"])
                                ]
#                        add "icons/daytime_day" + res.suffix + ".png":
#                            yoffset -2
#                            xanchor 2
                    if day_time == "evening":
                        if dialogue_active_flag == True or sceneIsStreet != True or hudDaySkipToEveningEnabled == False or map_enabled != True or owner != "Monica":
                            imagebutton:
                                yoffset -2
                                xanchor 5
                                idle "/icons/daytime_evening" + res.suffix + ".png"
                                hover "/icons/daytime_evening" + res.suffix + ".png"
                                action [
                                    Play("sound", "Sounds/click_denied.ogg")
                                ]
                        else:
                            imagebutton:
                                yoffset -2
                                xanchor 5
                                idle "/icons/daytime_evening" + res.suffix + ".png"
                                hover "/icons/daytime_evening_hover" + res.suffix + ".png"
                                action [
                                    Return(["time_management_street_fast_sleep"])
                                ]

                if hud_presets["display_calendar"] == True:
                    null:
                        width 0
                    fixed:
                        xmaximum gui.resolution.hud_screen.value2
                        ymaximum gui.resolution.hud_screen.value2
                        add "icons/calendar" + res.suffix + ".png":
                            yoffset -3
                        $ current_calendar_day = calendar_days[(day-1)%7]
                        if _preferences.language != "chinese":
                            text t__(current_calendar_day):
                                xalign gui.resolution.hud_screen.calendar_text_x_align
                                yalign gui.resolution.hud_screen.calendar_text_y_align
                                font "fonts/montserrat-bold.ttf"
                                color "#303030"
                                kerning -1
                                size gui.resolution.hud_screen.font1_size
                                outlines [(1, "#ffffff", -0.5,0.5), (1, "#e0e0e0", 0.5, -0.5)]
                        else:
                            text t__(current_calendar_day):
                                xalign gui.resolution.hud_screen.calendar_text_x_align
                                yalign gui.resolution.hud_screen.calendar_text_y_align
                                font "fonts/NotoSerifCJKsc-Regular.otf"
                                color "#303030"
                                kerning -1
                                size gui.resolution.hud_screen.font1_size
                                outlines [(1, "#ffffff", -0.5,0.5), (1, "#e0e0e0", 0.5, -0.5)]

                if hud_presets["display_money"] == True:
                    if gui.flag720 != True:
                        null:
                            width 0
                    if money == 100000000.0:
                        add "icons/money_rich" + res.suffix + ".png":
                            yalign 0.5
                        $ money_text = "$ " + '{:10,.2f}'.format(money)
                        text money_text:
                            color "#00a000"
                            xalign 0.0
                            yalign 0.5
                            yoffset gui.resolution.hud_screen.yoffset3
                            outlines [(3, "#000000", 0, 0)]
                    else:
                        if money < 10000000:

                            if money == 0:
                                pass
                            else:
                                if money < 5:
                                    add "icons/money_dollar" + res.suffix + ".png":
                                        yalign 0.5
                                else:
                                    if money < 50:
                                        add "icons/money_five" + res.suffix + ".png":
                                            yalign 0.5
                                    else:
                                        if money < 10000:
                                            add "icons/money_lower_100" + res.suffix + ".png":
                                                yalign 0.5


                            $ money_text = "$ " + '{:2,.2f}'.format(money)
                            if money < 10:
                                text money_text:
                                    color "#e80000"
                                    xalign 0.0
                                    yalign 0.5
                                    yoffset gui.resolution.hud_screen.yoffset3
                                    outlines [(3, "#000000", 0, 0)]
                            if money >= 10 and money < 5000:
                                text money_text:
                                    color c_orange
                                    xalign 0.0
                                    yalign 0.5
                                    yoffset gui.resolution.hud_screen.yoffset3
                                    outlines [(3, "#000000", 0, 0)]
                            if money >= 5000:
                                text money_text:
                                    color c_green
                                    xalign 0.0
                                    yalign 0.5
                                    yoffset gui.resolution.hud_screen.yoffset3
                                    outlines [(3, "#000000", 0, 0)]

            fixed:
                yoffset gui.resolution.hud_screen.yoffset1
                vbox:
                    spacing gui.resolution.hud_screen.spacing1
                    null:
                        height gui.resolution.hud_screen.height1
                    if hud_presets["display_objectives"] == True:
                        for objective in objectives_list:
                            if _preferences.language != "chinese":
                                text "- " + t__(objective[1]):
                                    color objective[2]
                                    font objectivesFont
                                    size gui.resolution.hud_screen.font2_size
                                    outlines [(2, "#000000", 0, 0)]
                            else:
                                text "- " + t__(objective[1]):
                                    color objective[2]
                                    font gui.text_font_chinese
                                    size gui.resolution.hud_screen.font2_size
                                    outlines [(2, "#000000", 0, 0)]
                    null:
                        height gui.resolution.hud_screen.height1
                    imagebutton:
                        idle "icons/achievement_icon" + res.suffix + ".png"
                        hover "icons/achievement_icon_hover" + res.suffix + ".png"
                        action [
                            Return(["show_achievements"])
                        ]
                    if hud_presets.has_key("display_questlog") == False or hud_presets["display_questlog"] == True:
                        null:
                            height gui.resolution.hud_screen.height1
                        imagebutton:
                            if questLogJustUpdated == True:
#                                idle "icons/questlog_icon" + res.suffix + ".png" at quest_log_transform
                                idle "icons/questlog_icon_new" + res.suffix + ".png"
                                hover "icons/questlog_icon_new_hover" + res.suffix + ".png"
                            else:
                                idle "icons/questlog_icon" + res.suffix + ".png"
                                hover "icons/questlog_icon_hover" + res.suffix + ".png"
                            action [
                                Return(["show_questlog"])
                            ]
                    if hud_presets.has_key("display_questhelp") == False or hud_presets["display_questhelp"] == True:
                        null:
                            height gui.resolution.hud_screen.height1
                        imagebutton:
                            xoffset 5
                            if questHelpJustUpdated == True:
                                idle "icons/questhelp_icon_new" + res.suffix + ".png"
                                hover "icons/questhelp_icon_new_hover" + res.suffix + ".png"
                            else:
                                idle "icons/questhelp_icon" + res.suffix + ".png"
                                hover "icons/questhelp_icon_hover" + res.suffix + ".png"
                            action [
                                Return(["show_questhelp"])
                            ]
                    if questionHelperEnabled == True:
                        null:
                            height gui.resolution.hud_screen.height1
                        imagebutton:
                            idle "icons/question_icon" + res.suffix + ".png"
                            hover "icons/question_icon_hover" + res.suffix + ".png"
                            action [
                                Return(["question_helper_call"])
                            ]
    frame:
        background None
        right_padding 8
        top_padding 8
        xpos 1.0
        xanchor 1.0
        vbox:
            hbox:
                if hud_presets["display_scene_caption"] == True:
                    if _preferences.language != "chinese":
                        text t__(scene_caption):
    #                        font "fonts/baskerville_bold_win95bt.ttf"
    #                        font "fonts/bebasneue book.ttf"
                            font "fonts/bebasneue regular.ttf"
    #                        font "fonts/linotte-semibold.otf"
    #                        font "fonts/ubuntu-condensed.ttf"
    #                        font "fonts/tahoma.ttf"
    #                        font "fonts/montserrat-bold.ttf"
                            size gui.resolution.hud_screen.font3_size
                            outlines [(2, "#000000", 0, 0)]
                            yoffset gui.resolution.hud_screen.yoffset2
                            xoffset gui.resolution.hud_screen.xoffset2
                    else:
                        text t__(scene_caption):
                            font gui.text_font_chinese
                            size gui.resolution.hud_screen.font3_size
                            outlines [(2, "#000000", 0, 0)]
                            yoffset gui.resolution.hud_screen.yoffset2_chinese
                            xoffset gui.resolution.hud_screen.xoffset2

                if hud_presets["display_scene_map"] == True:
                    if map_enabled == True and mapStreetCheckShowing == True and map_disabled_forced == False:
                        imagebutton:
                            xoffset 7
                            yoffset -7
                            idle "icons/map_icon2_idle" + res.suffix + ".png"
                            hover "icons/map_icon2_hover" + res.suffix + ".png"
#                           at mega_test_image_anim
#                           hover "mega_test_image"
#                           at map_icon_button_transform
                            action [
                                Return(["map_show"])
#                                Notify("Map")
                            ]

                    else:
                        add "icons/map_icon2_disabled" + res.suffix + ".png":
                            xoffset 7
                            yoffset -7

    fixed:
#            size (200, 327)
        if hud_presets.has_key("display_face_hud") and hud_presets["display_face_hud"] == True:
#            add "gui/frame5" + res.suffix + ".png":
#                pos gui.resoultion.hud_screen.face_hud_image_background_pos
            add "/icons/" + faceHudImage + res.suffix + ".png":
                pos gui.resolution.hud_screen.face_hud_image_pos
        if hud_presets.has_key("display_bitchmeter") and hud_presets["display_bitchmeter"] == True:
#            $ bitchmeter_description = get_bitchmeter_description() + " (" + str(bitchmeterValue) + ")"
            $ bitchmeter_description = get_bitchmeter_description()
            if _preferences.language != "chinese":
                text t__(bitchmeter_description):
                    xpos config.screen_width - gui.resolution.hud_screen.bitchmeter_desc_x_pos
                    ypos gui.resolution.hud_screen.bitchmeter_desc_y_pos
                    xanchor 0.5
                    yanchor 0.5
                    xalign 0.5
                    yalign 0.5
    #                    color c_blue
    #                    color "#d3ea5f" #white green
    #                    color "#e0e85c"
                    color "#c8da2b"
    #                    color "#6383c2"
    #                    font "fonts/arial.ttf"
                    font "fonts/linotte-semibold.otf"
    #                        font "fonts/ubuntu-condensed.ttf"
    #                        font "fonts/tahoma.ttf"
                    size gui.resolution.hud_screen.bitchmeter_desc_font_size
                    outlines [(2, "#808080", -1, 1), (2, "#404040", 0, 0)]
                    at bitchmeter_style_transform
            else:
                text t__(bitchmeter_description):
                    xpos config.screen_width - gui.resolution.hud_screen.bitchmeter_desc_x_pos
                    ypos gui.resolution.hud_screen.bitchmeter_desc_y_pos
                    xanchor 0.5
                    yanchor 0.5
                    xalign 0.5
                    yalign 0.5
                    color "#c8da2b"
                    font gui.text_font_chinese
                    size gui.resolution.hud_screen.bitchmeter_desc_font_size
                    outlines [(2, "#808080", -1, 1), (2, "#404040", 0, 0)]
                    at bitchmeter_style_transform

            $ corruption_description = "Corruption: " + str(corruption) + ""
            text t__(corruption_description):
                xpos config.screen_width - gui.resolution.hud_screen.corruption_desc_x_pos
                ypos gui.resolution.hud_screen.bitchmeter_desc_y_pos
                xanchor 0.5
                yanchor 0.5
                xalign 0.5
                yalign 0.5
#                    color c_blue
#                    color "#d3ea5f" #white green
#                    color "#e0e85c"
                color c_pink
#                    color "#6383c2"
#                    font "fonts/arial.ttf"
                font "fonts/linotte-semibold.otf"
#                        font "fonts/ubuntu-condensed.ttf"
#                        font "fonts/tahoma.ttf"
                size gui.resolution.hud_screen.bitchmeter_desc_font_size
                outlines [(2, "#000000", 1, -1), (2, "#404040", 0, 0)]
                at corruption_style_transform

            bar:
                xpos config.screen_width - gui.resolution.hud_screen.bitchmeter_x_pos
                ypos gui.resolution.hud_screen.bitchmeter_y_pos
                value (100.0 / maxBitchness * bitchmeterValue) / 100.0
                xoffset 5
                xysize(gui.resolution.hud_screen.bitchmeter_x_size,gui.resolution.hud_screen.bitchmeter_y_size)
                bar_vertical True
                top_bar "/icons/bar/bar_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/bar_full" + res.suffix + ".png"
                thumb "/icons/bar/bar_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.bitchmeter_bottom_gutter
                top_gutter gui.resolution.hud_screen.bitchmeter_top_gutter
                thumb_offset gui.resolution.hud_screen.bitchmeter_thumb_offset
            bar:
                xpos config.screen_width - gui.resolution.hud_screen.corruption_x_pos
                ypos gui.resolution.hud_screen.bitchmeter_y_pos
                value (100.0 / corruptionMax * corruption) / 100.0
                xoffset 5
                xysize(gui.resolution.hud_screen.bitchmeter_x_size,gui.resolution.hud_screen.bitchmeter_y_size)
                bar_vertical True
                top_bar "/icons/bar/bar3_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/bar3_full" + res.suffix + ".png"
                thumb "/icons/bar/bar3_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.bitchmeter_bottom_gutter
                top_gutter gui.resolution.hud_screen.bitchmeter_top_gutter
                thumb_offset gui.resolution.hud_screen.bitchmeter_thumb_offset

screen questlog_screen(inText):
    zorder 60
    modal True
    fixed:
        add "Icons2/Questlog_background.png":
            xpos getRes(587)
            ypos getRes(42)

#        $ lastCategory = False
#        for idx in questLogData:
#            if questLogData[idx][3] != lastCategory:
#                $ lastCategory =
#        frame:
#            background None
#            side ("c r"):
#                area (getRes(700), getRes(95), getRes(750), getRes(1001))
#                viewport id "questlog_journal":
#                    draggable True mousewheel True
#        viewport:
#            xinitial getRes(587)
#            yinitial getRes(42)
#            child_size (getRes(580), getRes(700))
#            scrollbars "vertical"
#            mousewheel True
#            draggable True
#            pagekeys True

#            side_yfill True

#            vbox:
#                transclude
        button:
            xfill True
            yfill True
            action [
                Return()
            ]
        viewport id "questlog_viewport":
#            xinitial getRes(587)
#            yinitial getRes(42)
            xpos getRes(700)
            ypos getRes(95)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(650)
            ymaximum getRes(878)
            mousewheel True
            pagekeys True
            if _preferences.language != "chinese":
                text inText:
                    xsize getRes(580)
                    style "questlog_text_style"
            else:
                text inText:
                    xsize getRes(580)
                    style "questlog_text_style"
                    font gui.text_font_chinese
#        vbar value YScrollValue("questlog_viewport")
#                    xpos getRes(700)
#                    ypos getRes(95)
#                    xsize getRes(580)
        #                vbar value YScrollValue("questlog_journal")
        imagebutton:
            xpos getRes(1280)
            ypos getRes(80)
            anchor (0.5, 0.5)
            idle "/icons/window_close" + res.suffix + ".png"
            hover "/icons/window_close_hover" + res.suffix + ".png"
            action [
                Return()
            ]
screen vignette_screen():
    zorder 100
    fixed:
        add "Sprites/Utils/vignette.png"

screen photoshot_screen():
    zorder 100
    fixed:
        add "Overlays/white_screen.jpg" at photoshoot_transform

screen photoshot_screen_low():
    zorder 100
    fixed:
        add "Overlays/white_screen.jpg" at photoshoot_transform2

screen textonblack_screen(in_text):
    zorder 100
    layer "master"
    frame:
        xfill True
        yfill True
        background Solid("#000000")
        if _preferences.language != "chinese":
            text t__(in_text) style "text_on_black_style":
                xanchor 0.5
                yanchor 0.5
                xalign 0.5
                yalign 0.5
        else:
            text t__(in_text) style "text_on_black_style":
                xanchor 0.5
                yanchor 0.5
                xalign 0.5
                yalign 0.5
                font gui.text_font_chinese

screen intro_image(image_name):
    zorder 190
    fixed:
        add get_image_filename(image_name)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 200
    style_prefix "say"

    python:
        try:
            eWho = eval(who)
            who_color = eWho.who_args["color"] if eWho.who_args.has_key("color") else False
            what_color = eWho.what_args["color"] if eWho.what_args.has_key("color") else False
            what_italic = eWho.what_args["italic"] if eWho.what_args.has_key("italic") else False
            who_name = eWho.name
        except:
            who_color = False
            what_color = False
            what_italic = False
            who_name = who
    window:
        id "window"
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                if _preferences.language != "chinese":
                    if who_color != False:
                        text t__(who_name) id "who":
                            color who_color
                    else:
                        text t__(who_name) id "who"
                else:
                    if who_color != False:
                        text t__(who_name) id "who":
                            color who_color
                            font gui.text_font_chinese
                    else:
                        text t__(who_name) id "who":
                            font gui.text_font_chinese

        if _preferences.language != "chinese":
            if what_color != False:
                text what id "what":
                    color what_color
                    italic what_italic
            else:
                text what id "what":
                    italic what_italic
        else:
            if what_color != False:
                text what id "what":
                    color what_color
                    italic what_italic
                    font gui.text_font_chinese
            else:
                text what id "what":
                    italic what_italic
                    font gui.text_font_chinese

    fixed:
        button:
            xfill True
            yfill True
            action [
#                Notify("click!"),
                Return(True)
            ]
            alternate [
#                Notify("hide!"),
                #Hide("say")
                Function(check_hide_text)
            ]
    key "h" action Function(check_hide_text)
    key "c" action [
        Call("mycopytext_label" ,what),
    ]
    key "/" action [
        Return(True)
    ]
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is dialogue_text
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            if _preferences.language != "chinese":
                text t__(prompt) style "input_prompt"
                input id "input"
            else:
                text t__(prompt) style "input_prompt":
                    font gui.text_font_chinese
                input id "input":
                    font gui.text_font_chinese

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    fixed:
        button:
            style "menu_choice_empty_background_button"
            xfill True
            yfill True
            action [
                NullAction()
            ]

    vbox:
        python:
            buttons_list = []
            priority = 100
            if menu_corruption == False:
                menu_corruption = []
            if menu_price == False:
                menu_price = []
            corruptionListLen = len(menu_corruption)
            priceListLen = len(menu_price)
            # creating native buttons list
            idx = 0
            for imenu in items:
                if imenu.action:
                    str1 = imenu.caption
                    button_obj = {"priority": priority, "native":True, "caption":str1, "action":imenu.action, "active":True}
                    if " (disabled)" in imenu.caption or " (deaktiviert)" in imenu.caption or " (déactivé)" in imenu.caption or " (devredışı)" in imenu.caption or " (disabilitato)" in imenu.caption or " (Disabled)" in imenu.caption or " (Deaktiviert)" in imenu.caption or " (Déactivé)" in imenu.caption or " (Devredışı)" in imenu.caption or " (Disabilitato)" in imenu.caption:
                        str1 = t__(imenu.caption)
                        str1 = str1.replace(" (disabled)", "")
                        str1 = str1.replace(" (deaktiviert)", "")
                        str1 = str1.replace(" (déactivé)", "")
                        str1 = str1.replace(" (devredışı)", "")
                        str1 = str1.replace(" (disabilitato)", "")
                        str1 = str1.replace(" (Disabled)", "")
                        str1 = str1.replace(" (Deaktiviert)", "")
                        str1 = str1.replace(" (Déactivé)", "")
                        str1 = str1.replace(" (Devredışı)", "")
                        str1 = str1.replace(" (Disabilitato)", "")
                        button_obj["caption"] = str1
                        button_obj["active"] = False
                    if corruptionListLen>idx:
                        # corruption
                        if menu_corruption[idx] >0:
                            if corruption >= menu_corruption[idx]:
                                str1 = t__(imenu.caption)
                                str1 = str1 + "{color=#31e8b1}" + t__(" (corruption: ") + str(menu_corruption[idx]) + "){/color}"
                                button_obj["caption"] = str1
                            else:
                                str1 = t__(imenu.caption)
                                str1 = str1 + t__(" (low corruption, required ") + str(menu_corruption[idx]) + ")"
                                button_obj["caption"] = str1
                                button_obj["active"] = False
                    if priceListLen>idx:
                        # price
                        if menu_price[idx] >0:
                            if money >= menu_price[idx]:
                                str1 = t__(imenu.caption)
                                str1 = str1 + "  {color=#31e8b1}$ " + '{:5,.2f}'.format(menu_price[idx]) + "{/color}"
                                button_obj["caption"] = str1
                            else:
                                str1 = t__(imenu.caption)
                                str1 = str1 + "  {color=#880000}$ " + '{:5,.2f}'.format(menu_price[idx]) + "{/color}"
                                button_obj["caption"] = str1
                                button_obj["active"] = False

                    if menuName != False and menu_required.has_key(menuName) and menu_required[menuName].has_key(imenu.caption):
                        menuCellData = menu_required[menuName][imenu.caption]
                        if menuCellData.has_key("level"):
                            charData = char_info[menuCellData["name"]]
                            if charData["level"] > menuCellData["level"] or (charData["level"] >= menuCellData["level"] and charData["current_progress"] >= menuCellData["current_progress"]):
                                str1 = t__(imenu.caption)
                                if menuCellData["current_progress"] > 0 and 1==2:
                                    str1 = str1 + "  {color=#31e8b1} " + t__("Ур. отношений") + ": " + str(menuCellData["level"]) + ", " + t__("прогресс") + ": " + str(menuCellData["current_progress"]) + "/100 {/color}"
                                else:
                                    str1 = str1 + "  {color=#31e8b1} " + t__("Ур. отношений") + ": " + str(menuCellData["level"]) + " {/color}"
                                button_obj["caption"] = str1
                            else:
                                str1 = t__(imenu.caption)
                                if menuCellData["current_progress"] > 0:
                                    str1 = str1 + "  {color=#880000} " + t__("Ур. отношений") + ": " + str(menuCellData["level"]) + ", " + t__("прогресс") + ": " + str(menuCellData["current_progress"]) + "/100 {/color}"
                                else:
                                    str1 = str1 + "  {color=#880000} " + t__("Ур. отношений") + ": " + str(menuCellData["level"]) + " {/color}"
                                button_obj["caption"] = str1
                                button_obj["active"] = False



                    buttons_list.append(button_obj)
                priority -= 10
                idx +=1

            if menuName != False:
                menu_hooks_list = get_hooks_for_object(menuName, "menu")

                # creating hooks buttons list
                for ihooks in menu_hooks_list:
                    button_obj = {"priority":ihooks["priority"], "native":False, "caption": ihooks["caption"] if ihooks.has_key("caption") else ihooks["hook_label"], "active": ihooks["active"] if ihooks.has_key("active") else True, "action":ihooks["hook_label"]}
                    if isinstance(button_obj["active"], basestring):
                        button_obj["active"] = globals()[button_obj["active"]]()
                    len1 = len(buttons_list)
                    if len1>0:
                        for jmenu in reversed(range(0,len1)):
                            if buttons_list[jmenu]["caption"] == button_obj["caption"]:
                                del buttons_list[jmenu]
                    buttons_list.append(button_obj)

            # sorting priority
            buttons_list = sort_hooks(buttons_list)
            buttons_list.reverse()

        # display choices buttons
        for button_data in buttons_list:
            if button_data["native"] == True:
                if button_data["active"] == True:
                    if _preferences.language != "chinese":
                        textbutton t__(button_data["caption"]):
                            action [
                                SetVariable("menu_corruption", False),
                                SetVariable("menu_price", False),
                                SetVariable("dialogue_active_flag", False),
                                SetVariable("menuName", False),
                                button_data["action"]
                            ]
                    else:
                        textbutton t__(button_data["caption"]) text_style "text_chinese":
                            action [
                                SetVariable("menu_corruption", False),
                                SetVariable("menu_price", False),
                                SetVariable("dialogue_active_flag", False),
                                SetVariable("menuName", False),
                                button_data["action"]
                            ]
                else:
                    if _preferences.language != "chinese":
                        textbutton t__(button_data["caption"]) text_style "choice_button_disabled_text"
                    else:
                        textbutton t__(button_data["caption"]) text_style "choice_button_disabled_text_chinese"
            else:
                if button_data["active"] == True:
                    $ menuLastName = menuName
                    if _preferences.language != "chinese":
                        textbutton t__(button_data["caption"]):
                            action [
                                SetVariable("menu_corruption", False),
                                SetVariable("menu_price", False),
                                SetVariable("dialogue_active_flag", False),
                                SetVariable("menuName", False),
                                Call("call_hook", button_data["action"], menuLastName)
#                                Return(["call_hook", button_data["action"], menuLastName]),
                            ]
                    else:
                        textbutton t__(button_data["caption"]) text_style "text_chinese":
                            action [
                                SetVariable("menu_corruption", False),
                                SetVariable("menu_price", False),
                                SetVariable("dialogue_active_flag", False),
                                SetVariable("menuName", False),
                                Call("call_hook", button_data["action"], menuLastName)
#                                Return(["call_hook", button_data["action"], menuLastName]),
                            ]
                else:
                    if _preferences.language != "chinese":
                        textbutton t__(button_data["caption"]) text_style "choice_button_disabled_text"
                    else:
                        textbutton t__(button_data["caption"]) text_style "choice_button_disabled_text_chinese"




screen temp_old_data():
        for i in items:
            $ print get_hooks_for_object(menuName, "menu")
            if i.action:
                if " (disabled)" in i.caption:
                    $ str1 = t__(i.caption)
#                    $ print str1

#                    textbutton i.caption text_style "choice_button_disabled_text"
                    textbutton str1.replace(" (disabled)", "") text_style "choice_button_disabled_text"
                else:
                    textbutton i.caption:
                        action [
#                       Notify("click!"),
                            SetVariable("dialogue_active_flag", False),
                            i.action
                        ]


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos gui.resolution.choice_box.y_pos
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton t_("Back") action Rollback()
            textbutton t_("History") action ShowMenu('history')
            textbutton t_("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton t_("Auto") action Preference("auto-forward", "toggle")
            textbutton t_("Save") action ShowMenu('save')
            textbutton t_("Q.Save") action QuickSave()
            textbutton t_("Q.Load") action QuickLoad()
            textbutton t_("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton t_("Start") action Start()

        else:

            textbutton t_("History") action ShowMenu("history")

            textbutton t_("Save") action ShowMenu("save")

        textbutton t_("Load") action ShowMenu("load")

#        if renpy.android != True:
#            textbutton t_("UPDATE GAME") action Start("show_game_updater") text_color "#31e8b1" text_hover_color "#9ff5dd"

        textbutton t_("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton t_("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton t_("Main Menu") action MainMenu()

#        textbutton t_("New Episodes") action OpenURL("http://decent-monkey.com/news/")
        textbutton t_("Guide") action OpenURL("http://decent-monkey.com/the-guide-for-episode-2/")
#        textbutton ("Become Supporter") action OpenURL("http://www.patreon.com/decentmonkey/")
        $ flag1 = False
        if game.extra == True and renpy.current_screen().screen_name[0] == "load":
            if check_saves_for_migration() == True:
#                textbutton t_("MIGRATE FROM 720p") action Start("migrate_saves") text_color "#e8b131" text_hover_color "#f8f131"
                $ flag1 = True
#        if flag1 == False:
#            textbutton t_("My Thanks") action ShowMenu("about")


        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
#            textbutton t_("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton t_("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    fixed:
#        imagebutton:
#            xpos get_resolution_x(1525)
#            ypos get_resolution_y(35)
#            idle "gui/patreon_button.png"
#            hover "gui/patreon_button_hover.png"
#            action OpenURL("https://www.patreon.com/decentmonkey")

        imagebutton:
            xpos get_resolution_x(1524)
            ypos get_resolution_y(162)
            idle "gui/web_button.png"
            hover "gui/web_button_hover.png"
            action OpenURL("http://decent-monkey.com/news/")

        add "gui/resolution_caption.png":
            xpos get_resolution_x(1345)
            ypos get_resolution_y(440)

        frame:
#            pos (get_resolution_x(1570), get_resolution_y(650))
            pos (gui.resolution.main_menu.lang.left, get_resolution_y(650))
            padding (gui.resolution.main_menu.lang.padding1,gui.resolution.main_menu.lang.padding2)
            xysize (get_resolution_x(gui.resolution.main_menu.lang.width), get_resolution_y(gui.resolution.main_menu.lang.height))
            anchor (0,0)
            background Frame("gui/frame_lang.png", left=0, top=0, right=5, bottom=0)
            vbox:
                pos (0,0)
                anchor (0,0)
                style_prefix "navigation"
                label t_("Language"):
                    text_size gui.resolution.main_menu.font_size1
                textbutton "English" action Language("english"):
                    text_size gui.resolution.main_menu.font_size2
                textbutton "German" action Language("german"):
                    text_size gui.resolution.main_menu.font_size2
                textbutton "French" action Language("french"):
                    text_size gui.resolution.main_menu.font_size2
                textbutton "Russian" action Language(None):
                    text_size gui.resolution.main_menu.font_size2

        if language_credits.has_key(str(_preferences.language)):
            frame:
                pos (gui.resolution.main_menu.lang.thanks_text_left, get_resolution_y(650) + get_resolution_y(gui.resolution.main_menu.lang.height) + getRes(10))
                anchor (0, 0)
                background None
                text t__(language_credits[str(_preferences.language)]) style "main_menu_credits_text"

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize gui.resolution.main_menu_frame
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
    color "f6861f"
    outlines [(0, "#000000", 1, 1)]
#    outlines [(0, "#000000", 0, 0)]
#    outlines [(0, "#696935", 1, 1)]


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton t_("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(t_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text t_("Version [config.version!t]\n")


            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about]\n"

#            text t_("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu
    if (gui.save_game.enabled == False or dialogue_active_flag == True) and 1==2:
        use game_menu("Save"):
            fixed:
                order_reverse True
            text "Save disabled during dialogues.\nIt causes major bugs with the game.\nI'm sorry :("
    else:
        use file_slots(t_("Save"))


screen load():

    tag menu

    use file_slots(t_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=t_("Page {}"), auto=t_("Automatic saves"), quick=t_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action [
                            FileAction(slot),
                        ]

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=t_("{#file_time}%A, %B %d %Y, %H:%M"), empty=t_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton t_("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton t_("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton t_("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton t_(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(t_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label t_("Display")
                        textbutton t_("Window") action Preference("display", "window")
                        textbutton t_("Fullscreen") action Preference("display", "fullscreen")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
#                box_wrap True

                vbox:
                    xminimum gui.resolution.menu_pause_before_change_slide.value

                    style_prefix "radio"
                    label t_("Pause before change slide")
                    textbutton t_("Enable") action SetField(persistent, "pause_before_change_slide", True)
                    textbutton t_("Disable") action SetField(persistent, "pause_before_change_slide", False)

                vbox:
                    xmaximum gui.resolution.preferences1

                    if config.has_music:
                        label t_("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label t_("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton t_("Test") action Play("sound", config.sample_sound)


                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton t_("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height 20
            hbox:
                vbox:
                    xminimum gui.resolution.menu_pause_before_change_slide.value
                    style_prefix "pref"

                    label t_("Language")
                    textbutton "English" action Language("english")
                    textbutton "German" action Language("german")
                    textbutton "French" action Language("french")
                    textbutton "Russian" action Language(None)

                vbox:
                    style_prefix "radio"
                    label "Auto Clipboard"
                    textbutton t_("Enable") action SetField(persistent, "auto_clipboard", True)
                    textbutton t_("Disable") action SetField(persistent, "auto_clipboard", False)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(t_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:
                    if _preferences.language != "chinese":
                        label t__(h.who):
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    else:
                        label t__(h.who) text_style "text_chinese":
                            style "history_name"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                if _preferences.language != "chinese":
                    text t__(what)
                else:
                    text t__(what):
                        font gui.text_font_chinese

        if not _history_list:
            label t_("The dialogue history is empty.")

screen Rain_overlay:
    layer "master"
    zorder 29
    if rainIntencity == 1:
        add "rain":
            alpha .05
    if rainIntencity == 2:
        add "rain":
            alpha .10
    if rainIntencity == 3:
        add "rain":
            alpha .15


screen Reporters_Shoots_Screen:
    timer 2 repeat True action [SPlay("snd_photo_capture2", "thunder1"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]
    timer 2.5 repeat True action [SPlay("snd_photo_capture3", "thunder2"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]
    timer 4.5 repeat True action [SPlay("snd_photo_capture4", "thunder3"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]
    timer 1.3 repeat True action [SPlay("snd_photo_capture5", "thunder1"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]
    timer 2.2 repeat True action [SPlay("snd_photo_capture2", "thunder2"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]
    timer 3.1 repeat True action [SPlay("snd_photo_capture3", "thunder3"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]

screen Reporters_Shoots_Screen2:
    timer 2 repeat True action [SPlay("snd_photo_capture2", "thunder1")]
    timer 2.5 repeat True action [SPlay("snd_photo_capture3", "thunder2")]
    timer 4.5 repeat True action [SPlay("snd_photo_capture4", "thunder3")]
    timer 1.3 repeat True action [SPlay("snd_photo_capture5", "thunder1")]
    timer 2.2 repeat True action [SPlay("snd_photo_capture2", "thunder2")]
    timer 3.1 repeat True action [SPlay("snd_photo_capture3", "thunder3")]

screen Reporters_Shoots_Screen3:
    timer 3.0 action [Hide("Reporters_Shoots_Screen"), Show("Reporters_Shoots_Screen3")]

screen Reporters_Shoots_Screen4_low:
    timer 4.5 repeat True action [SPlay("snd_photo_capture4", "thunder3"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]
    timer 3.1 repeat True action [SPlay("snd_photo_capture3", "thunder3"), Hide("photoshot_screen_low"), Show("photoshot_screen_low")]

screen Rain:
    # включаем и выключаем дождь вместе с экраном
    if rain == True:
        if rainIntencity == 1:
            on 'show' action SPlay("snd_light_rain", "rain", loop=True)
        if rainIntencity == 2:
            on 'show' action SPlay("snd_moderate_rain", "rain", loop=True)
        if rainIntencity == 3:
            on 'show' action SPlay("snd_heavy_rain", "rain", loop=True)
        # можно остановить только дождь SStop("rain"),
        # тогда начавшийся гром догремит и стихнет сам
        on 'hide' action SStop()
        # псевдо-рандомные раскаты
        if lightning == True:
            if rainIntencity >= 1:
                timer 10.5 repeat True action [SPlay("snd_lightning", "thunder1"), Hide("photoshot_screen"), Show("photoshot_screen")]
            if rainIntencity >= 2:
                timer 17.5 repeat True action [SPlay("snd_lightning_medium", "thunder2"), Hide("photoshot_screen"), Show("photoshot_screen")]
            if rainIntencity >= 3:
                timer 26.5 repeat True action [SPlay("snd_lightning_long", "thunder3"), Hide("photoshot_screen"), Show("photoshot_screen")]
    #    timer 6.5 repeat True action SPlay("snd_lightning_medium", "thunder2")
    #    timer 15.0 repeat True action SPlay("snd_lightning_long", "thunder3")
        # картинка с молниями
    #    timer .1 repeat True action NewXA()
    #    add "light":
    #        xalign xa
        # дождь
        if rainIntencity == 1:
            add "rain":
                alpha .05
        if rainIntencity == 2:
            add "rain":
                alpha .10
        if rainIntencity == 3:
            add "rain":
                alpha .15

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(t_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton t_("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton t_("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton t_("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label t_("Enter")
        text t_("Advances dialogue and activates the interface.")

    hbox:
        label t_("Space")
        text t_("Advances dialogue without selecting choices.")

    hbox:
        label t_("Arrow Keys")
        text t_("Navigate the interface.")

    hbox:
        label t_("Escape")
        text t_("Accesses the game menu.")

    hbox:
        label t_("Ctrl")
        text t_("Skips dialogue while held down.")

    hbox:
        label t_("Tab")
        text t_("Toggles dialogue skipping.")

    hbox:
        label t_("Page Up")
        text t_("Rolls back to earlier dialogue.")

    hbox:
        label t_("Page Down")
        text t_("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text t_("Hides the user interface.")

    hbox:
        label "S"
        text t_("Takes a screenshot.")

    hbox:
        label "V"
        text t_("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label t_("Left Click")
        text t_("Advances dialogue and activates the interface.")

    hbox:
        label t_("Middle Click")
        text t_("Hides the user interface.")

    hbox:
        label t_("Right Click")
        text t_("Accesses the game menu.")

    hbox:
        label t_("Mouse Wheel Up\nClick Rollback Side")
        text t_("Rolls back to earlier dialogue.")

    hbox:
        label t_("Mouse Wheel Down")
        text t_("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label t_("Right Trigger\nA/Bottom Button")
        text t_("Advances dialogue and activates the interface.")

    hbox:
        label t_("Left Trigger\nLeft Shoulder")
        text t_("Rolls back to earlier dialogue.")

    hbox:
        label t_("Right Shoulder")
        text t_("Rolls forward to later dialogue.")


    hbox:
        label t_("D-Pad, Sticks")
        text t_("Navigate the interface.")

    hbox:
        label t_("Start, Guide")
        text t_("Accesses the game menu.")

    hbox:
        label t_("Y/Top Button")
        text t_("Hides the user interface.")

    textbutton t_("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label t_(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton t_("Yes") action yes_action
                textbutton t_("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text t_("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"
    if message != "notifList":
        frame at notify_appear:
            ypos 0.2
            if _preferences.language != "chinese":
                text t__(message)
            else:
                text t__(message) style "text_chinese"
        timer 3.25 action [Hide('notify'), SetVariable("notifList", [])]
    else:
        $ notifOffset = 0
        for msg in notifList:
            frame at notify_appear:
                ypos 0.2
                yoffset notifOffset
                if _preferences.language != "chinese":
                    text t__(msg)
                else:
                    text t__(msg) style "text_chinese"
            $ notifOffset += notifyLineOffset
#        timer (3.25*len(notifList)) action [Hide('notify'), SetVariable("notifList", [])]
        if len(notifList) > 2:
            $ notifTimerLen = (2.0 * len(notifList))
            if notifTimerLen > 6.0:
                $ notifTimerLen = 6.0
            timer notifTimerLen action [SetVariable("notifList", []), Hide('notify')]
        else:
            timer (3.25) action [SetVariable("notifList", []), Hide('notify')]



transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            if _preferences.language != "chinese":
                textbutton t__(i.caption):
                    action i.action
                    style "nvl_button"
            else:
                textbutton t__(i.caption) text_style "text_chinese":
                    action i.action
                    style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    if _preferences.language != "chinese":
                        text t__(d.who):
                            id d.who_id
                    else:
                        text t__(d.who):
                            id d.who_id
                            font gui.text_font_chinese

                if _preferences.language != "chinese":
                    text t__(d.what):
                        id d.what_id
                else:
                    text t__(d.what):
                        id d.what_id
                        font gui.text_font_chinese


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton t_("Back") action Rollback()
        textbutton t_("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton t_("Auto") action Preference("auto-forward", "toggle")
        textbutton t_("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
