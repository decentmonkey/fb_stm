default pub_dance_claire_dialogues_up_list = []
default pub_dance_claire_dialogues_up_list2 = []

default pub_dance_claire_ahley_comment1_flag = False

label pub_dance2_claire_dance: # Танец с Клэр
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins

    $ ep29_quests_dancing_with_claire_last_day = day
    $ shotsTotalAmount = stage_shoots_total_amount_cur
    python:
        excitementTableUp = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
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
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
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


    music stop
    img black_screen
    with diss
    pause 0.5
    music stageCurrentMusicIntro
    call ep210_dialogue_5_dance_clare() from _rcall_ep210_dialogue_5_dance_clare
    if pub_dance_claire_ahley_comment1_flag == False:
        call ep210_dialogues4_dance_strip_9() from _rcall_ep210_dialogues4_dance_strip_9
        $ pub_dance_claire_ahley_comment1_flag = True

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 10
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    music stageCurrentMusicLoop
    img black_screen
    with diss
    pause 1.5
    if result == "up":
        scene black
        image videov_Monica_Strip_J1 = Movie(play="video/v_Monica_Strip_J1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_J1_end.jpg")
        show videov_Monica_Strip_J1
        pause 1.8
        hide videov_Monica_Strip_J1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_J1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react
        $ stage_achievements_list.append("v_Monica_Strip_J1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_J2 = Movie(play="video/v_Monica_Strip_J2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_J2_end.jpg")
        show videov_Monica_Strip_J2
        pause 1.8
        hide videov_Monica_Strip_J2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_J2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_1
        $ stage_achievements_list.append("v_Monica_Strip_J2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_J3 = Movie(play="video/v_Monica_Strip_J3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_J3_end.jpg")
        show videov_Monica_Strip_J3
        pause 1.8
        hide videov_Monica_Strip_J3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_J3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_2
        $ stage_achievements_list.append("v_Monica_Strip_J3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 11
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_K1 = Movie(play="video/v_Monica_Strip_K1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_K1_end.jpg")
        show videov_Monica_Strip_K1
        pause 1.8
        hide videov_Monica_Strip_K1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_K1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_3
        $ stage_achievements_list.append("v_Monica_Strip_K1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_K2 = Movie(play="video/v_Monica_Strip_K2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_K2_end.jpg")
        show videov_Monica_Strip_K2
        pause 1.8
        hide videov_Monica_Strip_K2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_K2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_4
        $ stage_achievements_list.append("v_Monica_Strip_K2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_K3 = Movie(play="video/v_Monica_Strip_K3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_K3_end.jpg")
        show videov_Monica_Strip_K3
        pause 1.8
        hide videov_Monica_Strip_K3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_K3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_5
        $ stage_achievements_list.append("v_Monica_Strip_K3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 12
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_L1 = Movie(play="video/v_Monica_Strip_L1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_L1_end.jpg")
        show videov_Monica_Strip_L1
        pause 1.8
        hide videov_Monica_Strip_L1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_L1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_6
        $ stage_achievements_list.append("v_Monica_Strip_L1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_L2 = Movie(play="video/v_Monica_Strip_L2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_L2_end.jpg")
        show videov_Monica_Strip_L2
        pause 1.8
        hide videov_Monica_Strip_L2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_L2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_7
        $ stage_achievements_list.append("v_Monica_Strip_L2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_L3 = Movie(play="video/v_Monica_Strip_L3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_L3_end.jpg")
        show videov_Monica_Strip_L3
        pause 1.8
        hide videov_Monica_Strip_L3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_L3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_8
        $ stage_achievements_list.append("v_Monica_Strip_L3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 13
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_M1 = Movie(play="video/v_Monica_Strip_M1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_M1_end.jpg")
        show videov_Monica_Strip_M1
        pause 1.8
        hide videov_Monica_Strip_M1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_M1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_9
        $ stage_achievements_list.append("v_Monica_Strip_M1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_M2 = Movie(play="video/v_Monica_Strip_M2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_M2_end.jpg")
        show videov_Monica_Strip_M2
        pause 1.8
        hide videov_Monica_Strip_M2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_M2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_10
        $ stage_achievements_list.append("v_Monica_Strip_M2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_M3 = Movie(play="video/v_Monica_Strip_M3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_M3_end.jpg")
        show videov_Monica_Strip_M3
        pause 1.8
        hide videov_Monica_Strip_M3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_M3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_11
        $ stage_achievements_list.append("v_Monica_Strip_M3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 14
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_N1 = Movie(play="video/v_Monica_Strip_N1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_N1_end.jpg")
        show videov_Monica_Strip_N1
        pause 1.8
        hide videov_Monica_Strip_N1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_N1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_12
        $ stage_achievements_list.append("v_Monica_Strip_N1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_N2 = Movie(play="video/v_Monica_Strip_N2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_N2_end.jpg")
        show videov_Monica_Strip_N2
        pause 1.8
        hide videov_Monica_Strip_N2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_N2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_13
        $ stage_achievements_list.append("v_Monica_Strip_N2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_N3 = Movie(play="video/v_Monica_Strip_N3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_N3_end.jpg")
        show videov_Monica_Strip_N3
        pause 1.8
        hide videov_Monica_Strip_N3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_N3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_14
        $ stage_achievements_list.append("v_Monica_Strip_N3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 15
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_O1 = Movie(play="video/v_Monica_Strip_O1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_O1_end.jpg")
        show videov_Monica_Strip_O1
        pause 1.8
        hide videov_Monica_Strip_O1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_O1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_15
        $ stage_achievements_list.append("v_Monica_Strip_O1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_O2 = Movie(play="video/v_Monica_Strip_O2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_O2_end.jpg")
        show videov_Monica_Strip_O2
        pause 1.8
        hide videov_Monica_Strip_O2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_O2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_16
        $ stage_achievements_list.append("v_Monica_Strip_O2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_O3 = Movie(play="video/v_Monica_Strip_O3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_O3_end.jpg")
        show videov_Monica_Strip_O3
        pause 1.8
        hide videov_Monica_Strip_O3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_O3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_17
        $ stage_achievements_list.append("v_Monica_Strip_O3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 16
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_P1 = Movie(play="video/v_Monica_Strip_P1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_P1_end.jpg")
        show videov_Monica_Strip_P1
        pause 1.8
        hide videov_Monica_Strip_P1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_P1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_18
        $ stage_achievements_list.append("v_Monica_Strip_P1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_P2 = Movie(play="video/v_Monica_Strip_P2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_P2_end.jpg")
        show videov_Monica_Strip_P2
        pause 1.8
        hide videov_Monica_Strip_P2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_P2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_19
        $ stage_achievements_list.append("v_Monica_Strip_P2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_P3 = Movie(play="video/v_Monica_Strip_P3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_P3_end.jpg")
        show videov_Monica_Strip_P3
        pause 1.8
        hide videov_Monica_Strip_P3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_P3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_20
        $ stage_achievements_list.append("v_Monica_Strip_P3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    $ pose = 17
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_Q1 = Movie(play="video/v_Monica_Strip_Q1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Q1_end.jpg")
        show videov_Monica_Strip_Q1
        pause 1.8
        hide videov_Monica_Strip_Q1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Q1_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_21
        $ stage_achievements_list.append("v_Monica_Strip_Q1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Q2 = Movie(play="video/v_Monica_Strip_Q2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Q2_end.jpg")
        show videov_Monica_Strip_Q2
        pause 1.8
        hide videov_Monica_Strip_Q2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Q2_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_22
        $ stage_achievements_list.append("v_Monica_Strip_Q2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Q3 = Movie(play="video/v_Monica_Strip_Q3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Q3_end.jpg")
        show videov_Monica_Strip_Q3
        pause 1.8
        hide videov_Monica_Strip_Q3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Q3_end.jpg")
        wclean
        call pub_dance_claire_dialogues_react(pose, result) from _rcall_pub_dance_claire_dialogues_react_23
        $ stage_achievements_list.append("v_Monica_Strip_Q3_end")

    jump pub_dance1_stage_end
