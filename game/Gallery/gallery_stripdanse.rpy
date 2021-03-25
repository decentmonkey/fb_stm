label gallery_pub_dance1_stage_start1:
    music Groove2_85
    img 22900
    with fadelong
    $ stageMusicControlEnabled = True
    music stop
    music2 stop
    call gallery_dialogue_5_dance_strip_scene_menu() from _rcall_gallery_dialogue_5_dance_strip_scene_menu # выбор музыки
    $ stageMusicMode = 1   #######
    $ stage_Monica_Excitement_Current = 0
    $ stage_Monica_Excitement_Last = 0
    $ stage_achievements_list = []
    $ stage_Monica_last_zone = False
    python:
        excitementTableUp = [
            [7,5,5], #1 - бар от 0 до 27 - 4 бакса чаевых
            [5,4,6], #2
            [5,5,7], #3 6 + 7 + 7 = до 20, 5 +4 +5 = от 14
            [8,7,11], #4 - бар от 27 до 54 - 7 баксов чаевых
            [12,8,9], #5
            [7,8,12], #6 от 18 до 30

            [10,9,15], #7 - бар от 54 до 69 - 11 баксов чаевых
            [15,10,15], #8 - бар от 69 до 84 - 20 баксов
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            # от 29 до 45
            # итого: от 61 до

            # Общее:
            # stage 1 - до 20
            # stage 2 - до 35 + 20 = 55
            # stage 3 - 55 + 45 = 100

            # максимум давать 20 баксов, т.е, 66
            #
        ]
        excitementTableDown = [
            [2,2,2], #1
            [3,3,3], #2
            [4,4,4], #3
            [4,4,4], #4
            [5,5,5], #5
            [6,6,6], #6

            [7,7,7], #7
            [8,8,8], #8
            [9,9,9], #9
        ]
        musicList = [
            {"intro":"track1_intro", "loop":"track1"},
            {"intro":"track2_intro", "loop":"track2"},
            {"intro":"track7_intro", "loop":"track7"},
            {"intro":"track3_intro", "loop":"track3"},
            {"intro":"track4_intro", "loop":"track4"},
            {"intro":"track5_intro", "loop":"track5"},
            {"intro":"track8_intro", "loop":"track8"},
            {"intro":"track6_intro", "loop":"track6"},
        ]
        if stageMusicMode == 0:
            stageLastMusic += 1
            if stageLastMusic >= len(musicList):
                stageLastMusic = 0
        if stageMusicMode == 1:
            stageLastMusic = rand(1,len(musicList)) - 1
        if stageMusicMode == 2:
            stageLastMusic = stageCustomMusic
        stageCurrentMusicIntro = musicList[stageLastMusic]["intro"]
        stageCurrentMusicLoop = musicList[stageLastMusic]["loop"]

    music stop
    img black_screen
    with diss
    pause 1.0
    if cloth == "StripOutfit2":
        music stageCurrentMusicLoop

    else:
        music stageCurrentMusicIntro

#    call gallery_pub_dance_dialogues_start_dancing() # Комментарий при начале танца


    $ shotsTotalAmount = 27
    $ stage_Monica_shoots_array_current = []

    if cloth == "StripOutfit2":
        jump gallery_pub_dance1_stage_start1_topless
    img 22900
    with fadelong
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    #stage_Monica_shoots_array

    # Поза1
    # A
    $ pose = 1
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_A1 = Movie(play="video/v_Monica_Strip_A1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A1_end.jpg")
        show videov_Monica_Strip_A1
        pause 1.8
        hide videov_Monica_Strip_A1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react
        $ stage_achievements_list.append("v_Monica_Strip_A1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_A2 = Movie(play="video/v_Monica_Strip_A2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A2_end.jpg")
        show videov_Monica_Strip_A2
        pause 1.8
        hide videov_Monica_Strip_A2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_1
        $ stage_achievements_list.append("v_Monica_Strip_A2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_A3 = Movie(play="video/v_Monica_Strip_A3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A3_end.jpg")
        show videov_Monica_Strip_A3
        pause 1.8
        hide videov_Monica_Strip_A3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_2
        $ stage_achievements_list.append("v_Monica_Strip_A3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # B
    $ pose = 2
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_B1 = Movie(play="video/v_Monica_Strip_B1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B1_end.jpg")
        show videov_Monica_Strip_B1
        pause 1.8
        hide videov_Monica_Strip_B1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_3
        $ stage_achievements_list.append("v_Monica_Strip_B1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_B2 = Movie(play="video/v_Monica_Strip_B2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B2_end.jpg")
        show videov_Monica_Strip_B2
        pause 1.8
        hide videov_Monica_Strip_B2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_4
        $ stage_achievements_list.append("v_Monica_Strip_B2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_B3 = Movie(play="video/v_Monica_Strip_B3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B3_end.jpg")
        show videov_Monica_Strip_B3
        pause 1.8
        hide videov_Monica_Strip_B3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_5
        $ stage_achievements_list.append("v_Monica_Strip_B3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # C
    $ pose = 3
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_C1 = Movie(play="video/v_Monica_Strip_C1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C1_end.jpg")
        show videov_Monica_Strip_C1
        pause 1.8
        hide videov_Monica_Strip_C1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_6
        $ stage_achievements_list.append("v_Monica_Strip_C1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_C2 = Movie(play="video/v_Monica_Strip_C2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C2_end.jpg")
        show videov_Monica_Strip_C2
        pause 1.8
        hide videov_Monica_Strip_C2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_7
        $ stage_achievements_list.append("v_Monica_Strip_C2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_C3 = Movie(play="video/v_Monica_Strip_C3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C3_end.jpg")
        show videov_Monica_Strip_C3
        pause 1.8
        hide videov_Monica_Strip_C3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_8
        $ stage_achievements_list.append("v_Monica_Strip_C3_end")

    $ menu_corruption = [monicaPutStripClothToplessStage]
    menu:
        "Снять корсет.":
            if pubDanceCount < monicaDanceAmountToTopless or len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToTopless:
                hide screen poledance
                hide screen poledance_camera_icon
                hide screen love_bar_screen
                hide screen poledance_shoot
                hide screen poledance_coins
                call gallery_dialogue_5_dance_strip_4g() from _rcall_gallery_dialogue_5_dance_strip_4g
                jump gallery_pub_dance1_stage_end
            call gallery_dialogue_5_dance_strip_4h() from _rcall_gallery_dialogue_5_dance_strip_4h
        "Завершить танец.":
            jump gallery_pub_dance1_stage_stop

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    music pub_noise1
#    music stop
    img black_screen
    with diss
    pause 1.0
    show screen photoshot_screen()
    if pubDanceCount%3 == 0:

        scene black
        image videov_Monica_Strip_Undress1A = Movie(play="video/v_Monica_Strip_Undress1A.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1A_end.jpg")
        show videov_Monica_Strip_Undress1A
        music2 snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        pause 2.1
        hide videov_Monica_Strip_Undress1A
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Undress1A_end.jpg")
        wclean
        $ stage_achievements_list.append("v_Monica_Strip_Undress1A")
    if pubDanceCount%3 == 1:

        scene black
        image videov_Monica_Strip_Undress1B = Movie(play="video/v_Monica_Strip_Undress1B.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1B_end.jpg")
        show videov_Monica_Strip_Undress1B
        music2 snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        pause 2.1
        hide videov_Monica_Strip_Undress1B
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Undress1B_end.jpg")
        wclean
        $ stage_achievements_list.append("v_Monica_Strip_Undress1B")
    if pubDanceCount%3 == 2:

        scene black
        image videov_Monica_Strip_Undress1C = Movie(play="video/v_Monica_Strip_Undress1C.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1C_end.jpg")
        show videov_Monica_Strip_Undress1C
        music2 snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        pause 2.1
        hide videov_Monica_Strip_Undress1C
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Undress1C_end.jpg")
        wclean
        $ stage_achievements_list.append("v_Monica_Strip_Undress1C")
label gallery_pub_dance1_stage_start1_topless:
    img 22903
    with fadelong
    $ monicaDancingTopless = True
    if monicaDancingStage < 1:
        $ monicaDancingStage = 1
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # D
    $ pose = 4
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    music2 stop
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    music stop
    img black_screen
    with diss
    pause 1.0
    music stageCurrentMusicLoop
    if result == "up":

        scene black
        image videov_Monica_Strip_D1 = Movie(play="video/v_Monica_Strip_D1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D1_end.jpg")
        show videov_Monica_Strip_D1
        pause 1.8
        hide videov_Monica_Strip_D1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_9
        $ stage_achievements_list.append("v_Monica_Strip_D1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_D2 = Movie(play="video/v_Monica_Strip_D2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D2_end.jpg")
        show videov_Monica_Strip_D2
        pause 1.8
        hide videov_Monica_Strip_D2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_10
        $ stage_achievements_list.append("v_Monica_Strip_D2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_D3 = Movie(play="video/v_Monica_Strip_D3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D3_end.jpg")
        show videov_Monica_Strip_D3
        pause 1.8
        hide videov_Monica_Strip_D3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_11
        $ stage_achievements_list.append("v_Monica_Strip_D3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # E
    $ pose = 5
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_E1 = Movie(play="video/v_Monica_Strip_E1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E1_end.jpg")
        show videov_Monica_Strip_E1
        pause 1.8
        hide videov_Monica_Strip_E1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_12
        $ stage_achievements_list.append("v_Monica_Strip_E1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_E2 = Movie(play="video/v_Monica_Strip_E2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E2_end.jpg")
        show videov_Monica_Strip_E2
        pause 1.8
        hide videov_Monica_Strip_E2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_13
        $ stage_achievements_list.append("v_Monica_Strip_E2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_E3 = Movie(play="video/v_Monica_Strip_E3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E3_end.jpg")
        show videov_Monica_Strip_E3
        pause 1.8
        hide videov_Monica_Strip_E3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_14
        $ stage_achievements_list.append("v_Monica_Strip_E3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # F
    $ pose = 6
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_F1 = Movie(play="video/v_Monica_Strip_F1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F1_end.jpg")
        show videov_Monica_Strip_F1
        pause 1.8
        hide videov_Monica_Strip_F1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_15
        $ stage_achievements_list.append("v_Monica_Strip_F1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_F2 = Movie(play="video/v_Monica_Strip_F2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F2_end.jpg")
        show videov_Monica_Strip_F2
        pause 1.8
        hide videov_Monica_Strip_F2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_16
        $ stage_achievements_list.append("v_Monica_Strip_F2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_F3 = Movie(play="video/v_Monica_Strip_F3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F3_end.jpg")
        show videov_Monica_Strip_F3
        pause 1.8
        hide videov_Monica_Strip_F3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_17
        $ stage_achievements_list.append("v_Monica_Strip_F3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # G
    $ pose = 7
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
        call gallery_dialogue_5_dance_strip_4k() from _rcall_gallery_dialogue_5_dance_strip_4k
        jump gallery_pub_dance1_stage_end
    if monicaDancingStage < 2:
        $ monicaDancingStage = 2

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_G1 = Movie(play="video/v_Monica_Strip_G1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G1_end.jpg")
        show videov_Monica_Strip_G1
        pause 1.8
        hide videov_Monica_Strip_G1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_18
        $ stage_achievements_list.append("v_Monica_Strip_G1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_G2 = Movie(play="video/v_Monica_Strip_G2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G2_end.jpg")
        show videov_Monica_Strip_G2
        pause 1.8
        hide videov_Monica_Strip_G2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_19
        $ stage_achievements_list.append("v_Monica_Strip_G2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_G3 = Movie(play="video/v_Monica_Strip_G3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G3_end.jpg")
        show videov_Monica_Strip_G3
        pause 1.8
        hide videov_Monica_Strip_G3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_20
        $ stage_achievements_list.append("v_Monica_Strip_G3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # H
    $ pose = 8
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_H1 = Movie(play="video/v_Monica_Strip_H1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H1_end.jpg")
        show videov_Monica_Strip_H1
        pause 1.8
        hide videov_Monica_Strip_H1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_21
        $ stage_achievements_list.append("v_Monica_Strip_H1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_H2 = Movie(play="video/v_Monica_Strip_H2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H2_end.jpg")
        show videov_Monica_Strip_H2
        pause 1.8
        hide videov_Monica_Strip_H2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_22
        $ stage_achievements_list.append("v_Monica_Strip_H2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_H3 = Movie(play="video/v_Monica_Strip_H3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H3_end.jpg")
        show videov_Monica_Strip_H3
        pause 1.8
        hide videov_Monica_Strip_H3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_23
        $ stage_achievements_list.append("v_Monica_Strip_H3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # I
    $ pose = 9
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump gallery_pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":

        scene black
        image videov_Monica_Strip_I1 = Movie(play="video/v_Monica_Strip_I1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I1_end.jpg")
        show videov_Monica_Strip_I1
        pause 1.8
        hide videov_Monica_Strip_I1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I1_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_24
        $ stage_achievements_list.append("v_Monica_Strip_I1_end")
    if result == "side":

        scene black
        image videov_Monica_Strip_I2 = Movie(play="video/v_Monica_Strip_I2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I2_end.jpg")
        show videov_Monica_Strip_I2
        pause 1.8
        hide videov_Monica_Strip_I2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I2_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_25
        $ stage_achievements_list.append("v_Monica_Strip_I2_end")
    if result == "down":

        scene black
        image videov_Monica_Strip_I3 = Movie(play="video/v_Monica_Strip_I3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I3_end.jpg")
        show videov_Monica_Strip_I3
        pause 1.8
        hide videov_Monica_Strip_I3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I3_end.jpg")
        wclean
        call gallery_pub_dance_dialogues_react(pose, result) from _rcall_gallery_pub_dance_dialogues_react_26
        $ stage_achievements_list.append("v_Monica_Strip_I3_end")

    jump gallery_pub_dance1_stage_end

label gallery_pub_dance1_stage_stop:
    # Прерывание танца
    call gallery_dialogue_5_dance_strip_4m() from _rcall_gallery_dialogue_5_dance_strip_4m
    jump gallery_pub_dance1_stage_end

label gallery_pub_dance1_stage_end:
    music stop
    music2 stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    img black_screen
    with diss
    python:
        for movement in stage_achievements_list:
            check_achievement(movement)

    pause 1.0
    $ stage_Monica_last_shoots_array = stage_Monica_shoots_array_current
    return

label gallery_pub_dance_stage_flash:
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return


label gallery_dialogue_5_dance_strip_scene_menu:
    menu:
        "Идти на сцену.":
            return
        "Музыка: Последовательно" if stageMusicControlEnabled == True and stageMusicMode == 0:
            $ stageMusicMode = 1
        "Музыка: Случайно" if stageMusicControlEnabled == True and stageMusicMode == 1:
            $ stageMusicMode = 2
            $ stageCustomMusic = 0
        "Музыка: Трек 1" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 0:
            $ stageMusicMode = 2
            $ stageCustomMusic = 1
        "Музыка: Трек 2" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 1:
            $ stageMusicMode = 2
            $ stageCustomMusic = 2
        "Музыка: Трек 3" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 2:
            $ stageMusicMode = 2
            $ stageCustomMusic = 3
        "Музыка: Трек 4" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 3:
            $ stageMusicMode = 2
            $ stageCustomMusic = 4
        "Музыка: Трек 5" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 4:
            $ stageMusicMode = 2
            $ stageCustomMusic = 5
        "Музыка: Трек 6" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 5:
            $ stageMusicMode = 2
            $ stageCustomMusic = 6
        "Музыка: Трек 7" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 6:
            $ stageMusicMode = 2
            $ stageCustomMusic = 7
        "Музыка: Трек 8" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 7:
            $ stageMusicMode = 0
            $ stageCustomMusic = 0
    jump gallery_dialogue_5_dance_strip_scene_menu


label gallery_pub_dance_dialogues_start_dancing:
    # Моника вышла на сцену
    if monicaDancingStage == 0:
        if cloth == "StripOutfit1":
            img 22901
        if cloth == "StripOutfit2":
            img 22903
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call gallery_dialogue_5_dance_strip_4a() from _rcall_gallery_dialogue_5_dance_strip_4a
        if rand1 == 2:
            call gallery_dialogue_5_dance_strip_4b() from _rcall_gallery_dialogue_5_dance_strip_4b

    if monicaDancingStage == 1:
        if cloth == "StripOutfit1":
            img 22900
        if cloth == "StripOutfit2":
            img 22903
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call gallery_dialogue_5_dance_strip_4c() from _rcall_gallery_dialogue_5_dance_strip_4c
        if rand1 == 2:
            call gallery_dialogue_5_dance_strip_4d() from _rcall_gallery_dialogue_5_dance_strip_4d

    if monicaDancingStage == 2:
        if cloth == "StripOutfit1":
            img 22902
        if cloth == "StripOutfit2":
            img 22903
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call gallery_dialogue_5_dance_strip_4e() from _rcall_gallery_dialogue_5_dance_strip_4e
        if rand1 == 2:
            call gallery_dialogue_5_dance_strip_4f() from _rcall_gallery_dialogue_5_dance_strip_4f
    return

# Мысли Моники на сцене. В зависимости от уровня corruption.
label gallery_dialogue_5_dance_strip_4a:
    mt "Мне хочется спрятаться подальше от всех этих похотливых взглядов!"
    return
label gallery_dialogue_5_dance_strip_4b:
    mt "Я должна держаться! Я сильная!"
    return
label gallery_dialogue_5_dance_strip_4c:
    mt "Мне просто нужно сделать несколько движений у пилона."
    mt "Они же просто будут смотреть."
    return
label gallery_dialogue_5_dance_strip_4d:
    mt "Нужно относиться к этому как Клэр. Я просто позволяю этим мужчинам смотреть на свою красоту..."
    mt "...недоступную для них красоту!"
    return
label gallery_dialogue_5_dance_strip_4e:
    mt "Сегодня хочется сделать так, чтобы у этой рыжей не осталось поклонников в этой дыре!"
    mt "Звезда здесь может быть только одна - Я. А она даже не конкурентка мне... У меня вообще не может быть конкуренток!!!"
    return

label gallery_dialogue_5_dance_strip_4f:
    # После того как поругалась с Молли (после d, e)
    mt "И не забывать про Молли... Надо поставить ее на место... В подворотню со шлюхами!"
    return

label gallery_dialogue_5_dance_strip_4h:
    # Переход на стадию 1 успешен

    mt "Если я сниму жилет, то заработаю больше денег..."
    mt "Они же просто будут смотреть... на голую грудь [monica_pub_name]."
    return

label gallery_pub_dance_dialogues_react(pose, zone): # Реакция зала

    show screen poledance_camera_icon(stage_Monica_shoots_array)
    python:
        checkZoneKey = str(pose) + zone
        moveRepeated = False
        if checkZoneKey in stage_Monica_last_shoots_array:
            moveRepeated = True
        zoneRepeated = False
        if zone == stage_Monica_last_zone:
            zoneRepeated = True

        stage_Monica_shoots_array_current.append(checkZoneKey)
        stage_Monica_shoots_array.append(checkZoneKey)
        stage_Monica_last_zone = zone

#    if moveRepeated == True or zoneRepeated == True: # движение не понравилось
    if zoneRepeated == True: # движение не понравилось
        if moveRepeated == True:
            $ notif(t_("Моника делала это движение в прошлый раз"))
        if zoneRepeated == True:
            $ notif(t_("Моника повторяет направления танца"))
        call gallery_pub_dance_dialogues_excitement_down(pose, zone) from _rcall_gallery_pub_dance_dialogues_excitement_down
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        $ idx = rand(1,4)
        $ crowdSound = "snd_crowd_uuu" + str(idx)
        sound crowdSound
        if zone == "up":
            if pose < 4:
                call gallery_dialogue_5_dance_strip_5a1() from _rcall_gallery_dialogue_5_dance_strip_5a1
            else:
                call gallery_dialogue_5_dance_strip_5d2() from _rcall_gallery_dialogue_5_dance_strip_5d2
        if zone == "side":
            if pose < 4:
                call gallery_dialogue_5_dance_strip_5b2() from _rcall_gallery_dialogue_5_dance_strip_5b2
            else:
                call gallery_dialogue_5_dance_strip_5e2() from _rcall_gallery_dialogue_5_dance_strip_5e2
        if zone == "down":
            if pose < 4:
                call gallery_dialogue_5_dance_strip_5c2() from _rcall_gallery_dialogue_5_dance_strip_5c2
            else:
                call gallery_dialogue_5_dance_strip_5f2() from _rcall_gallery_dialogue_5_dance_strip_5f2
    else:
        # Движение понравилось
#        call pub_dance_dialogues_excitement_up(pose, zone)
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
#        call pub_dance_dialogues_excitement_tips()
        $ idx = rand(1,3)
        $ applauseSound = "snd_applause" + str(idx)
        sound applauseSound
        call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_5
        if zone == "up":
            if pose < 4:
                call gallery_dialogue_5_dance_strip_5a() from _rcall_gallery_dialogue_5_dance_strip_5a
            else:
                call gallery_dialogue_5_dance_strip_5d() from _rcall_gallery_dialogue_5_dance_strip_5d
        if zone == "side":
            if pose < 4:
                call gallery_dialogue_5_dance_strip_5b() from _rcall_gallery_dialogue_5_dance_strip_5b
            else:
                call gallery_dialogue_5_dance_strip_5e() from _rcall_gallery_dialogue_5_dance_strip_5e
        if zone == "down":
            if pose < 4:
                call gallery_dialogue_5_dance_strip_5c() from _rcall_gallery_dialogue_5_dance_strip_5c
            else:
                call gallery_dialogue_5_dance_strip_5f() from _rcall_gallery_dialogue_5_dance_strip_5f


#    wclean
    $ notif_clean()

    return

label gallery_pub_dance_dialogues_excitement_down(pose, zone):
    python:
        idx1 = 0
        if zone == "up":
            idx1 = 0
        if zone == "side":
            idx1 = 1
        if zone == "down":
            idx1 = 2
        excitementAmount = excitementTableDown[pose-1][idx1]
        stage_Monica_Excitement_Last = stage_Monica_Excitement_Current
        stage_Monica_Excitement_Current -= excitementAmount
        if stage_Monica_Excitement_Current < 0:
            stage_Monica_Excitement_Current = 0
    return

label gallery_dialogue_5_dance_strip_5a:
    if len(pub_dance_dialogues_up_list) == 0:
        $ pub_dance_dialogues_up_list = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list.pop()

    # правильные стрелки
    if idx == 1:
        customers1 "Эй, смотри, какая телка!"
    if idx == 2:
        customers2 "Кто это такая? Я ее раньше не видел!"
    if idx == 3:
        customers3 "Это новая стриптизерша? Вау!"
    if idx == 4:
        customers4 "Эй, красотка, иди к нам!"
    if idx == 5:
        customers5 "Снимай маску! Покажи нам себя!"
    return
label gallery_dialogue_5_dance_strip_5a1:
    if len(pub_dance_dialogues_up_list2) == 0:
        $ pub_dance_dialogues_up_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_up_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Эй! Хорош уже! Давай, раздевайся!"
    if idx == 2:
        customers2 "Где стриптиз?!"
    if idx == 3:
        customers3 "Это что?! Где сиськи голые?!"
    return
# реплики для side (тело)
label gallery_dialogue_5_dance_strip_5b:
    if len(pub_dance_dialogues_side_list) == 0:
        $ pub_dance_dialogues_side_list = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_side_list.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Давай, покажи класс, детка!"
    if idx == 2:
        customers2 "О, да! Вот это сиськи!"
    if idx == 3:
        customers3 "Охренеть!"
    if idx == 4:
        customers4 "Давай, раздевайся!"
    if idx == 5:
        customers5 "Эй, покажи нам сиськи!"
    return
label gallery_dialogue_5_dance_strip_5b2:
    if len(pub_dance_dialogues_side_list2) == 0:
        $ pub_dance_dialogues_side_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_side_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Уууууу!!!"
    if idx == 2:
        customers2 "Я пришел на голые сиськи посмотреть, а не на это!"
    if idx == 3:
        customers3 "Где нормальный стриптиз?!"
    return
# реплики для down (ноги, попа)
label gallery_dialogue_5_dance_strip_5c:
    if len(pub_dance_dialogues_down_list) == 0:
        $ pub_dance_dialogues_down_list = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_down_list.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Снимай с себя эти тряпки!"
    if idx == 2:
        customers2 "Пошли в приват, детка!"
    if idx == 3:
        customers3 "Да! Давай еще!"
    if idx == 4:
        customers4 "Вау, детка! У меня уже в штанах дымится! Иди сюда!"
    if idx == 5:
        customers5 "Давай, покрути своей задницей!"
    return
label gallery_dialogue_5_dance_strip_5c2:
    if len(pub_dance_dialogues_down_list2) == 0:
        $ pub_dance_dialogues_down_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_down_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Твою мать, сними с себя хоть что-нибудь!"
    if idx == 2:
        customers2 "И это все?!"
    if idx == 3:
        customers3 "Уууууу!!!"
    return

label gallery_dialogue_5_dance_strip_5ca:
    customers2 "И это все?!"
    customers2 "Детка, иди танцуй еще!"
    return

# Моника топлесс
# реплики для верха (лицо)
label gallery_dialogue_5_dance_strip_5d:
    if len(pub_dance_dialogues_up_list3) == 0:
        $ pub_dance_dialogues_up_list3 = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list3.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "О да! Детка, ты супер!"
    if idx == 2:
        customers2 "Да! Мы тебя ждали, красотка!"
    if idx == 3:
        customers3 "Спускайся сюда!"
    if idx == 4:
        customers4 "Покажи свои сиськи!"
    if idx == 5:
        customers5 "Давай, покажи класс, детка!"
    return
label gallery_dialogue_5_dance_strip_5d2:
    if len(pub_dance_dialogues_side_list4) == 0:
        $ pub_dance_dialogues_side_list4 = random.sample(set([1,2,3,4]), 4)
    $ idx = pub_dance_dialogues_side_list4.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Сиськи показывай!"
    if idx == 2:
        customers2 "Уууууу!!!"
    if idx == 3:
        customers3 "Эй, научите ее, как надо это делать!!!"
    if idx == 4:
        customers4 "Эй, мы это уже видели в прошлый раз! Покажи что-нибудь еще!"
    return
# реплики для side (тело)
label gallery_dialogue_5_dance_strip_5e:
    if len(pub_dance_dialogues_up_list3) == 0:
        $ pub_dance_dialogues_up_list3 = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list3.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Вау! Какие сиськи!"
    if idx == 2:
        customers2 "Детка, спускайся сюда! У меня для тебя есть кое-что!"
    if idx == 3:
        customers3 "Давай в приват!"
    if idx == 4:
        customers4 "Потряси своими сиськами!"
    if idx == 5:
        customers5 "Да! Охренительно!"
    return
label gallery_dialogue_5_dance_strip_5e2:
    if len(pub_dance_dialogues_side_list4) == 0:
        $ pub_dance_dialogues_side_list4 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_side_list4.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Да разденься ты уже!!!"
    if idx == 2:
        customers2 "Я за что деньги платить должен?!"
    if idx == 3:
        customers3 "Покрути своей задницей!"
    return
# реплики для down (ноги, попа)
label gallery_dialogue_5_dance_strip_5f:
    if len(pub_dance_dialogues_up_list3) == 0:
        $ pub_dance_dialogues_up_list3 = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list3.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Эй, хочешь этих хрустящих купюр? Снимай свои трусики!"
    if idx == 2:
        customers2 "Покажи нам свою киску!"
    if idx == 3:
        customers3 "Давай, снимай с себя все!"
    if idx == 4:
        customers4 "Иди сюда! Смотри, что у меня есть для тебя!"
    if idx == 5:
        customers5 "О, какая задница! Папочка любит такие! Пошли ко мне, детка!"
    return
label gallery_dialogue_5_dance_strip_5f2:
    if len(pub_dance_dialogues_side_list4) == 0:
        $ pub_dance_dialogues_side_list4 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_side_list4.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "И это все?!"
    if idx == 2:
        customers2 "Уууууу!!!"
    if idx == 3:
        customers3 "Где нормальный стриптиз?!"
    return
