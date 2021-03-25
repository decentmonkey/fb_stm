screen screen_betty_panties_select():
    modal True
    fixed:
        xpos getRes(312)
        ypos getRes(280)
        $ offsetIdx = 0
        for pantiesIdx in range(1,6):
            hbox:
                if pantiesIdx != bettyPantiesCurrent:
                    imagebutton:
                        xpos (offsetIdx * getRes(340))
                        idle "Icons2/Betty_Panties_Icon_" + str(pantiesIdx) + ".png"
                        hover "Icons2/Betty_Panties_Icon_" + str(pantiesIdx) + "_hover.png"
                        action Return(pantiesIdx)
                    $ offsetIdx += 1

        imagebutton:
            xpos getRes(500)
            ypos getRes(340)
            idle "Icons2/Betty_Panties_Icon_6.png"
            hover "Icons2/Betty_Panties_Icon_6_hover.png"
            action Return(6)

screen screen_betty_panties_select2():
    modal True
    fixed:
        xpos getRes(312-153)
        ypos getRes(280)
        $ offsetIdx = 0
        for pantiesIdx in range(1,6):
            hbox:
                if pantiesIdx != bettyPantiesCurrent or bettyMustNotWearPanties == True:
                    imagebutton:
                        xpos (offsetIdx * getRes(340))
                        idle "Icons2/Betty_Panties_Icon_" + str(pantiesIdx) + ".png"
                        hover "Icons2/Betty_Panties_Icon_" + str(pantiesIdx) + "_hover.png"
                        action Return(pantiesIdx)
                    $ offsetIdx += 1

        imagebutton:
            xpos getRes(500)
            ypos getRes(340)
            idle "Icons2/Betty_Panties_Icon_6.png"
            hover "Icons2/Betty_Panties_Icon_6_hover.png"
            action Return(6)
        if monicaLaundryBettyPantiesSelectNudeDisabled == False:
            imagebutton:
                xpos getRes(500 + 340)
                ypos getRes(340)
                idle "Icons2/Betty_Panties_Icon_7.png"
                hover "Icons2/Betty_Panties_Icon_7_hover.png"
                action Return(7)
        else:
            imagebutton:
                xpos getRes(500 + 340)
                ypos getRes(340)
                idle "Icons2/Betty_Panties_Icon_7_Disabled.png"
                action Return(-1)

screen choose_photoshoot_outfit():
    modal True
    fixed:
        xpos getRes(480-200)
        ypos getRes(220)
        $ offsetYIdx = 0
        $ idx = 0
        for row1 in range(0,2):
            $ offsetXIdx = 0
            for col1 in range(0,7):
                imagebutton:
                    xpos (offsetXIdx * getRes(200))
                    ypos (offsetYIdx * getRes(330))
                    if (monicaOutfitsEnabled[idx] == True and monicaOutfitsAltEnabled == False) or (monicaOutfitsEnabled_Alt[idx] == True and monicaOutfitsAltEnabled == True):
                        idle monicaOutfitsIcons2[idx] + ".png"
                        hover monicaOutfitsIcons2[idx] + "_hover.png"
                        action Return(idx)
                    else:
                        if monicaOutfitsIcons2[idx] == "":
                            idle "/Icons2/Photoshoot_Empty_Icon_Disabled.png"
                        else:
                            idle monicaOutfitsIcons2[idx] + "_Disabled.png"
                        action Return(-1)
                $ idx += 1
                $ offsetXIdx += 1
            $ offsetYIdx +=1

screen choose_melanie_photoshoot_outfit():
    modal True
    fixed:
        xpos getRes(480)
        ypos getRes(220)
        $ offsetYIdx = 0
        $ idx = 0
        for row1 in range(0,2):
            $ offsetXIdx = 0
            for col1 in range(0,5):
                imagebutton:
                    xpos (offsetXIdx * getRes(200))
                    ypos (offsetYIdx * getRes(330))
                    if melanieOutfitsEnabled[idx] == True:
                        idle melanieOutfitsIcons[idx] + ".png"
                        hover melanieOutfitsIcons[idx] + "_hover.png"
                        action Return(idx)
                    else:
                        if melanieOutfitsIcons[idx] == "":
                            idle "/Icons2/Photoshoot_Empty_Icon_Disabled.png"
                        else:
                            idle melanieOutfitsIcons[idx] + "_Disabled.png"
                        action Return(-1)
                $ idx += 1
                $ offsetXIdx += 1
            $ offsetYIdx +=1

screen photoshoot_camera_icon(shootsArr):
    $ list1 = list(set(shootsArr))
    fixed:
        xpos getRes(40)
        ypos getRes(20)
        hbox:
            add "/Icons2/Photo_Cinema_icon.png"
            null width getRes(8)
            text str(len(list(set(shootsArr)))) + " / " + str(shotsTotalAmount) style "photoshoot_cinema_text_style"
    fixed:
        xpos getRes(40)
        ypos getRes(935)
        hbox:
            add "/Icons2/Photo_camera_icon2.png"
            null width getRes(5)
            text str(shotsAmount) style "photoshoot_camera_text_style":
                if shotsAmount <= 5:
                    color "#f83c2e"


screen photoshoot():
    fixed:
#        xpos getRes(1600)
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(-40)
                idle "/Icons2/photo_up.png"
                hover "/Icons2/photo_up_hover.png"
                action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/photo_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(0)
                ypos getRes(80)
                idle "/Icons2/photo_left.png"
                hover "/Icons2/photo_left_hover.png"
                action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/photo_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(200)
                idle "/Icons2/photo_down.png"
                hover "/Icons2/photo_down_hover.png"
                action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/photo_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5
        #next
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos getRes(170)
            ypos getRes(80)
            idle "/Icons2/photo_next2.png"
            hover "/Icons2/photo_next2_hover.png"
            action Return("next")

screen photoshoot2(arrowImages, alreadyImagesList):
    fixed:
#        xpos getRes(1600)
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            if len(arrowImages) > 0 and arrowImages[0] in alreadyImagesList:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(-40)
                    idle "/Icons2/photo_up_already.png"
                    hover "/Icons2/photo_up_already_hover.png"
                    action [SetVariable("arrowUp", False), Return("up")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(-40)
                    idle "/Icons2/photo_up.png"
                    hover "/Icons2/photo_up_hover.png"
                    action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/photo_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            if len(arrowImages) > 1 and arrowImages[1] in alreadyImagesList:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(0)
                    ypos getRes(80)
                    idle "/Icons2/photo_left_already.png"
                    hover "/Icons2/photo_left_already_hover.png"
                    action [SetVariable("arrowSide", False), Return("side")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(0)
                    ypos getRes(80)
                    idle "/Icons2/photo_left.png"
                    hover "/Icons2/photo_left_hover.png"
                    action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/photo_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            if len(arrowImages) > 2 and arrowImages[2] in alreadyImagesList:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(200)
                    idle "/Icons2/photo_down_already.png"
                    hover "/Icons2/photo_down_already_hover.png"
                    action [SetVariable("arrowDown", False), Return("down")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(200)
                    idle "/Icons2/photo_down.png"
                    hover "/Icons2/photo_down_hover.png"
                    action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/photo_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5
        #next
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos getRes(170)
            ypos getRes(80)
            idle "/Icons2/photo_next2.png"
            hover "/Icons2/photo_next2_hover.png"
            action Return("next")


screen photoshoot_no_next():
    fixed:
#        xpos getRes(1600)
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(-40)
                idle "/Icons2/photo_up.png"
                hover "/Icons2/photo_up_hover.png"
                action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/photo_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(0)
                ypos getRes(80)
                idle "/Icons2/photo_left.png"
                hover "/Icons2/photo_left_hover.png"
                action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/photo_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(200)
                idle "/Icons2/photo_down.png"
                hover "/Icons2/photo_down_hover.png"
                action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/photo_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5

screen photoshoot_no_next2(arrowImages, alreadyImagesList):
    fixed:
#        xpos getRes(1600)
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            if len(arrowImages) > 0 and arrowImages[0] in alreadyImagesList:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(-40)
                    idle "/Icons2/photo_up_already.png"
                    hover "/Icons2/photo_up_already_hover.png"
                    action [SetVariable("arrowUp", False), Return("up")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(-40)
                    idle "/Icons2/photo_up.png"
                    hover "/Icons2/photo_up_hover.png"
                    action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/photo_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            if len(arrowImages) > 1 and arrowImages[1] in alreadyImagesList:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(0)
                    ypos getRes(80)
                    idle "/Icons2/photo_left_already.png"
                    hover "/Icons2/photo_left_already_hover.png"
                    action [SetVariable("arrowSide", False), Return("side")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(0)
                    ypos getRes(80)
                    idle "/Icons2/photo_left.png"
                    hover "/Icons2/photo_left_hover.png"
                    action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/photo_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            if len(arrowImages) > 2 and arrowImages[2] in alreadyImagesList:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(200)
                    idle "/Icons2/photo_down_already.png"
                    hover "/Icons2/photo_down_already_hover.png"
                    action [SetVariable("arrowDown", False), Return("down")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(200)
                    idle "/Icons2/photo_down.png"
                    hover "/Icons2/photo_down_hover.png"
                    action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/photo_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5

screen camera_record_screen():
    fixed:
        xpos getRes(1600)
        ypos getRes(43)
        add "images/Icons2/Rec_Icon1.png" at camera_record_icon_transform

screen camera_viewfinder_screen():
    add "images/Icons2/Camera_ViewFinder.png"

screen pylon_screen(sceneImage, objectsList):
    layer "master"
    add sceneImage:
        xpos 0
        ypos 0
    for objData in objectsList:
        $ canvas_offset = get_canvas_offset(objData[0])
        if canvas_offset == False:
            $ canvas_offset = [0, 0]
        add objData[1]:
            xpos canvas_offset[1]
            ypos canvas_offset[0]

screen achievements_screen():
    $ width1 = int(1217 * gui.resolution.koeff)
    $ height1 = int(872 * gui.resolution.koeff)
    $ x1 = int(377 * gui.resolution.koeff)
    $ y1 = int(107 * gui.resolution.koeff)

    $ rowOffset = getRes(22) #244x137
    $ cellSizeX = getRes(296)
    $ cellSizeY = getRes(170)
    $ cellsInRow = 4
    $ category_height = gui.resolution.gallery.category_height

    # calculate viewport size
    $ rowsAmount = 0
    for category in achievements_categories:
        $ rowsAmount += int(math.ceil(float(len(achievements_list[category[0]]))/float(cellsInRow)))
    $ viewportHeight = len(achievements_categories) * (category_height+gui.resolution.gallery.category_margin_down) + rowsAmount * cellSizeY

    layer "master"
    zorder 60
    modal True
    button:
        xfill True
        yfill True
        action [
            Return()
        ]
    frame:
        background Frame("gui/frame4" + res.suffix + ".png", left=2, top=int(80*gui.resolution.koeff), right=2, bottom=2)
        pos(x1, y1)
        anchor(0, 0)
        xysize (width1, height1)
        imagebutton:
            xpos 1.0
            ypos 0.0
            anchor (0.5, 0.5)
            idle "/icons/window_close" + res.suffix + ".png"
            hover "/icons/window_close_hover" + res.suffix + ".png"
            action [
                Return()
            ]
        viewport id "questlog_viewport":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos 0
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(1217-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
            child_size (getRes(852-85), viewportHeight)
            $ galleryX = 0
            $ galleryY = 0
            $ curY = 0
            for category in achievements_categories:
#                text category[1] style "char_face_style_caption":
                text t__(category[1]):
                    pos(rowOffset, curY)
                    font "fonts/BebasNeue Regular.ttf"
                    color category[2]
                    size 40
                $ curY += category_height
                $ cellsList = achievements_list[category[0]]

                for i in range(0,len(cellsList)):
                    $ posX = i%cellsInRow * cellSizeX + rowOffset
                    $ posY = int(i/cellsInRow) * cellSizeY
                    if get_achievement(cellsList[i][0]) == True or 1==1:           ##### убрать  'or 1==1' !!!
                        if len(cellsList[i]) >= 3 and cellsList[i][2] != False:
                            add "images/Achievements/ach_" + cellsList[i][0] + ".jpg":
                                pos(posX, posY + curY)
                            imagebutton:
                                idle "gui/gallery_frame_play" + res.suffix + ".png"
                                hover "gui/gallery_frame_play_hover" + res.suffix + ".png"
                                xpos posX-gui.resolution.gallery.frame.offset
                                ypos posY-gui.resolution.gallery.frame.offset + curY
                                action [
                                    Call("process_gallery", cellsList[i][2])
                                ]
                        else:
                            add "images/Achievements/ach_" + cellsList[i][0] + ".jpg":
                                pos(posX, posY + curY)
                            add "gui/gallery_frame" + res.suffix + ".png":
                                pos(posX-gui.resolution.gallery.frame.offset, posY-gui.resolution.gallery.frame.offset + curY)
                    else:
                        add "images/Achievements/ach_" + cellsList[i][0] + "_disabled.jpg":
                            pos(posX, posY + curY)
                        add "gui/gallery_frame" + res.suffix + ".png":
                            pos(posX-gui.resolution.gallery.frame.offset, posY-gui.resolution.gallery.frame.offset + curY)
                    text t__(cellsList[i][1]) style "gallery_caption_text":
                        pos(posX + getRes(244/2), posY + curY + getRes(137+15))
                        anchor (0.5, 0.5)
                $ curY += int(math.ceil(float(len(cellsList))/float(cellsInRow))) * cellSizeY + gui.resolution.gallery.category_margin_down


screen love_bar_screen(oldBarValue, newBarValue):
    fixed:
            bar:
                xpos getRes(17)
                ypos getRes(260)
                value AnimatedValue(float(newBarValue)/100, 1.0, 1.0, float(oldBarValue)/100)
                xoffset 5
                xysize(gui.resolution.hud_screen.love_bar_xysize)
                bar_vertical True
                top_bar "/icons/bar/love_bar_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/love_bar_full" + res.suffix + ".png"
                thumb "/icons/bar/love_bar_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.love_bar_bottom_gutter
                top_gutter gui.resolution.hud_screen.love_bar_top_gutter
                thumb_offset gui.resolution.hud_screen.love_bar_thumb_offset


screen poledance_camera_icon(shootsArr):
    $ list1 = list(set(shootsArr))
    fixed:
        xpos getRes(40)
        ypos getRes(20)
        hbox:
            add "/Icons2/Photo_Cinema_icon.png"
            null width getRes(8)
            text str(len(list(set(shootsArr)))) + " / " + str(shotsTotalAmount) style "photoshoot_cinema_text_style"



screen poledance():
    fixed:
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            if str(pose) + "up" in stage_Monica_shoots_array:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(-40)
                    idle "/Icons2/dance_up_already.png"
                    hover "/Icons2/dance_up_already_hover.png"
                    action [SetVariable("arrowUp", False), Return("up")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(-40)
                    idle "/Icons2/dance_up.png"
                    hover "/Icons2/dance_up_hover.png"
                    action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/dance_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            if str(pose) + "side" in stage_Monica_shoots_array:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(0)
                    ypos getRes(80)
                    idle "/Icons2/dance_left_already.png"
                    hover "/Icons2/dance_left_already_hover.png"
                    action [SetVariable("arrowSide", False), Return("side")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(0)
                    ypos getRes(80)
                    idle "/Icons2/dance_left.png"
                    hover "/Icons2/dance_left_hover.png"
                    action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/dance_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            if str(pose) + "down" in stage_Monica_shoots_array:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(200)
                    idle "/Icons2/dance_down_already.png"
                    hover "/Icons2/dance_down_already_hover.png"
                    action [SetVariable("arrowDown", False), Return("down")]
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos getRes(50)
                    ypos getRes(200)
                    idle "/Icons2/dance_down.png"
                    hover "/Icons2/dance_down_hover.png"
                    action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/dance_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5
        #next
        if arrowStop == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(170)
                ypos getRes(80)
                idle "/Icons2/dance_stop.png"
                hover "/Icons2/dance_stop_hover.png"
                action Return("stop")
        else:
            add "/Icons2/dance_stop_Disabled.png":
                xanchor 0.5
                yanchor 0.5
                xpos getRes(170)
                ypos getRes(80)


screen poledance_shoot(imagePath):
    add imagePath at pole_dance_shake



screen poledance_coins(coinsArr):

    zorder 100
    style_prefix "notify"

    $ notifOffset = 0
    $ idx1 = 0
    for coin in coinsArr:
        $ msg =  ("+ $" + str(coin))
        if idx == 0:
            frame at coin_appear1:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
        if idx == 1:
            frame at coin_appear2:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
        if idx == 2:
            frame at coin_appear3:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
        if idx == 3:
            frame at coin_appear4:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
        if idx == 4:
            frame at coin_appear5:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
        if idx == 5:
            frame at coin_appear6:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
        if idx == 6:
            frame at coin_appear7:
                ypos 0.2
                yoffset notifOffset
                text t__(msg)
                $ notifOffset += notifyLineOffset
                $ idx1 += 1
    timer (3.25) action [Hide('poledance_coins')]


screen screen_marcus_cat_training1(numb):
    modal True
    fixed:
        imagebutton:
            xpos 0.5
            ypos 0.5
            xanchor 0.5
            yanchor 0.5
            idle "Icons2/" + marcusCatTrainingButtons[numb] + ".png"
            hover "Icons2/" + marcusCatTrainingButtons[numb] + "_hover.png"
            action Return(True)

screen screen_marcus_cat_training2():
    modal True
    fixed:
        xpos getRes(312-153)
        ypos getRes(210)
        $ offsetIdx = 0
        for commandIdx in range(0,len(marcusCatTrainingButtons)):
            hbox:
                imagebutton:
                    xpos (offsetIdx%5 * getRes(340))
                    ypos (int(offsetIdx/5) * getRes(340))
                    idle "Icons2/" + marcusCatTrainingButtons[commandIdx] + ".png"
                    hover "Icons2/" + marcusCatTrainingButtons[commandIdx] + "_hover.png"
                    action Return(commandIdx)
                $ offsetIdx += 1

screen love_bar_screen_battle(oldBarValue, newBarValue, oldBarValue2, newBarValue2):
    fixed:
            bar:
                xpos getRes(27)
                ypos getRes(260)
                value AnimatedValue(float(newBarValue)/100, 1.0, 1.0, float(oldBarValue)/100)
                xoffset 5
                xysize(gui.resolution.hud_screen.love_bar_xysize)
                bar_vertical True
                top_bar "/icons/bar/love_bar_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/love_bar_full" + res.suffix + ".png"
                thumb "/icons/bar/love_bar_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.love_bar_bottom_gutter
                top_gutter gui.resolution.hud_screen.love_bar_top_gutter
                thumb_offset gui.resolution.hud_screen.love_bar_thumb_offset
            add "/icons/monica_battle_icon" + res.suffix + ".png":
                xpos getRes(25)
                ypos(getRes(720))

            bar:
                xpos getRes(140)
                ypos getRes(260)
                value AnimatedValue(float(newBarValue2)/100, 1.0, 1.0, float(oldBarValue2)/100)
                xoffset 5
                xysize(gui.resolution.hud_screen.love_bar_xysize)
                bar_vertical True
                top_bar "/icons/bar/love_bar2_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/love_bar2_full" + res.suffix + ".png"
                thumb "/icons/bar/love_bar2_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.love_bar_bottom_gutter
                top_gutter gui.resolution.hud_screen.love_bar_top_gutter
                thumb_offset gui.resolution.hud_screen.love_bar_thumb_offset
            add "/icons/molly_battle_icon" + res.suffix + ".png":
                xpos getRes(147)
                ypos(getRes(720))

screen poledance_battle():
    fixed:
        xpos getRes(1650)
        ypos getRes(430)
        #up
        if arrowUp == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(-40)
                idle "/Icons2/dance_up.png"
                hover "/Icons2/dance_up_hover.png"
                action [SetVariable("arrowUp", False), Return("up")]
        else:
            add "/Icons2/dance_up_Disabled.png":
                xpos getRes(50)
                ypos getRes(-40)
                xanchor 0.5
                yanchor 0.5
        #left
        if arrowSide == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(0)
                ypos getRes(80)
                idle "/Icons2/dance_left.png"
                hover "/Icons2/dance_left_hover.png"
                action [SetVariable("arrowSide", False), Return("side")]
        else:
            add "/Icons2/dance_left_Disabled.png":
                xpos getRes(0)
                ypos getRes(80)
                xanchor 0.5
                yanchor 0.5
        #down
        if arrowDown == True:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos getRes(50)
                ypos getRes(200)
                idle "/Icons2/dance_down.png"
                hover "/Icons2/dance_down_hover.png"
                action [SetVariable("arrowDown", False), Return("down")]
        else:
            add "/Icons2/dance_down_Disabled.png":
                xpos getRes(50)
                ypos getRes(200)
                xanchor 0.5
                yanchor 0.5

transform coin_appear1:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

transform coin_appear2:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear3:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear4:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear5:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear6:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear7:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0











#
