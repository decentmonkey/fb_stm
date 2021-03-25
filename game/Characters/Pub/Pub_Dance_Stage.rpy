default stageMusicControlEnabled = False # включено-ли произвольное управление музыкой
default stageMusicMode = 0 # 0 - последовательно, 1 - случайно, 2 - произвольная музыка
default stageLastMusic = -1 # индекс последней игравшей музыки
default stageCustomMusic = 0 # индекс произвольной музыки

default stageCurrentMusicIntro = False
default stageCurrentMusicLoop = False

default stage_Monica_shoots_array = []
default stage_Monica_shoots_array_current = []
default stage_Monica_last_shoots_array = []
default stage_Monica_last_zone = False

default stage_Monica_Excitement_Current = 0
default stage_Monica_Excitement_Last = 0

default stage_shoots_total_amount_default = 27
default stage_shoots_total_amount_claire = 24
default stage_shoots_total_amount_nude = 25
default stage_shoots_total_amount_cur = 27
default stage_achievements_list = []

default stage_low_tips = False

default stage_dance_nude_planned = False
default stage_dance_nude_last_day = 0

default arrowStop = True
#monicaDancingStage

label pub_dance1_stage_start1:
    $ stageMusicControlEnabled = True
    if stage_low_tips == True:
        $ pub_dance_dialogues_tips_list = 1
    else:
        $ pub_dance_dialogues_tips_list = 0
    music stop
    music2 stop
    call dialogue_5_dance_strip_scene_menu() from _rcall_dialogue_5_dance_strip_scene_menu # выбор музыки
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
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
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
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
            [9,9,9], #9
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
    pause 2.0
    if cloth == "StripOutfit2":
        music stageCurrentMusicLoop
    else:
        music stageCurrentMusicIntro
    call pub_dance_dialogues_start_dancing() from _rcall_pub_dance_dialogues_start_dancing # Комментарий при начале танца


    $ shotsTotalAmount = stage_shoots_total_amount_cur
    $ stage_Monica_shoots_array_current = []

    if cloth == "StripOutfit2":
        jump pub_dance1_stage_start1_topless
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    if ep29_quests_claire_dance_planned == True:
        $ arrowStop = False

    #stage_Monica_shoots_array

    # Поза1
    # A
    $ pose = 1
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
        image videov_Monica_Strip_A1 = Movie(play="video/v_Monica_Strip_A1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A1_end.jpg")
        show videov_Monica_Strip_A1
        pause 1.8
        hide videov_Monica_Strip_A1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react
        $ stage_achievements_list.append("v_Monica_Strip_A1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_A2 = Movie(play="video/v_Monica_Strip_A2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A2_end.jpg")
        show videov_Monica_Strip_A2
        pause 1.8
        hide videov_Monica_Strip_A2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_1
        $ stage_achievements_list.append("v_Monica_Strip_A2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_A3 = Movie(play="video/v_Monica_Strip_A3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A3_end.jpg")
        show videov_Monica_Strip_A3
        pause 1.8
        hide videov_Monica_Strip_A3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_2
        $ stage_achievements_list.append("v_Monica_Strip_A3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # B
    $ pose = 2
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_B1 = Movie(play="video/v_Monica_Strip_B1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B1_end.jpg")
        show videov_Monica_Strip_B1
        pause 1.8
        hide videov_Monica_Strip_B1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_3
        $ stage_achievements_list.append("v_Monica_Strip_B1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_B2 = Movie(play="video/v_Monica_Strip_B2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B2_end.jpg")
        show videov_Monica_Strip_B2
        pause 1.8
        hide videov_Monica_Strip_B2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_4
        $ stage_achievements_list.append("v_Monica_Strip_B2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_B3 = Movie(play="video/v_Monica_Strip_B3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B3_end.jpg")
        show videov_Monica_Strip_B3
        pause 1.8
        hide videov_Monica_Strip_B3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_5
        $ stage_achievements_list.append("v_Monica_Strip_B3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # C
    $ pose = 3
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_C1 = Movie(play="video/v_Monica_Strip_C1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C1_end.jpg")
        show videov_Monica_Strip_C1
        pause 1.8
        hide videov_Monica_Strip_C1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_6
        $ stage_achievements_list.append("v_Monica_Strip_C1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_C2 = Movie(play="video/v_Monica_Strip_C2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C2_end.jpg")
        show videov_Monica_Strip_C2
        pause 1.8
        hide videov_Monica_Strip_C2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_7
        $ stage_achievements_list.append("v_Monica_Strip_C2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_C3 = Movie(play="video/v_Monica_Strip_C3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C3_end.jpg")
        show videov_Monica_Strip_C3
        pause 1.8
        hide videov_Monica_Strip_C3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_8
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
                call dialogue_5_dance_strip_4g() from _rcall_dialogue_5_dance_strip_4g
                jump pub_dance1_stage_end
            $ questHelp("shinyhole_14", True)
            $ questHelp("shinyhole_18", skipIfExists=True)
            call dialogue_5_dance_strip_4h() from _rcall_dialogue_5_dance_strip_4h
        "Завершить танец." if ep29_quests_claire_dance_planned == False:
            jump pub_dance1_stage_stop

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
label pub_dance1_stage_start1_topless:
    $ monicaDancingTopless = True
    if monicaDancingStage < 1:
        $ monicaDancingStage = 1
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # D
    $ pose = 4
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    music2 stop
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
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
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_9
        $ stage_achievements_list.append("v_Monica_Strip_D1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_D2 = Movie(play="video/v_Monica_Strip_D2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D2_end.jpg")
        show videov_Monica_Strip_D2
        pause 1.8
        hide videov_Monica_Strip_D2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_10
        $ stage_achievements_list.append("v_Monica_Strip_D2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_D3 = Movie(play="video/v_Monica_Strip_D3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D3_end.jpg")
        show videov_Monica_Strip_D3
        pause 1.8
        hide videov_Monica_Strip_D3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_11
        $ stage_achievements_list.append("v_Monica_Strip_D3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # E
    $ pose = 5
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_E1 = Movie(play="video/v_Monica_Strip_E1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E1_end.jpg")
        show videov_Monica_Strip_E1
        pause 1.8
        hide videov_Monica_Strip_E1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_12
        $ stage_achievements_list.append("v_Monica_Strip_E1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_E2 = Movie(play="video/v_Monica_Strip_E2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E2_end.jpg")
        show videov_Monica_Strip_E2
        pause 1.8
        hide videov_Monica_Strip_E2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_13
        $ stage_achievements_list.append("v_Monica_Strip_E2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_E3 = Movie(play="video/v_Monica_Strip_E3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E3_end.jpg")
        show videov_Monica_Strip_E3
        pause 1.8
        hide videov_Monica_Strip_E3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_14
        $ stage_achievements_list.append("v_Monica_Strip_E3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # F
    $ pose = 6
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_F1 = Movie(play="video/v_Monica_Strip_F1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F1_end.jpg")
        show videov_Monica_Strip_F1
        pause 1.8
        hide videov_Monica_Strip_F1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_15
        $ stage_achievements_list.append("v_Monica_Strip_F1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_F2 = Movie(play="video/v_Monica_Strip_F2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F2_end.jpg")
        show videov_Monica_Strip_F2
        pause 1.8
        hide videov_Monica_Strip_F2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_16
        $ stage_achievements_list.append("v_Monica_Strip_F2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_F3 = Movie(play="video/v_Monica_Strip_F3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F3_end.jpg")
        show videov_Monica_Strip_F3
        pause 1.8
        hide videov_Monica_Strip_F3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_17
        $ stage_achievements_list.append("v_Monica_Strip_F3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # G
    $ pose = 7
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
        call dialogue_5_dance_strip_4k() from _rcall_dialogue_5_dance_strip_4k
        jump pub_dance1_stage_end
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
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_18
        $ stage_achievements_list.append("v_Monica_Strip_G1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_G2 = Movie(play="video/v_Monica_Strip_G2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G2_end.jpg")
        show videov_Monica_Strip_G2
        pause 1.8
        hide videov_Monica_Strip_G2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_19
        $ stage_achievements_list.append("v_Monica_Strip_G2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_G3 = Movie(play="video/v_Monica_Strip_G3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G3_end.jpg")
        show videov_Monica_Strip_G3
        pause 1.8
        hide videov_Monica_Strip_G3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_20
        $ stage_achievements_list.append("v_Monica_Strip_G3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # H
    $ pose = 8
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_H1 = Movie(play="video/v_Monica_Strip_H1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H1_end.jpg")
        show videov_Monica_Strip_H1
        pause 1.8
        hide videov_Monica_Strip_H1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_21
        $ stage_achievements_list.append("v_Monica_Strip_H1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_H2 = Movie(play="video/v_Monica_Strip_H2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H2_end.jpg")
        show videov_Monica_Strip_H2
        pause 1.8
        hide videov_Monica_Strip_H2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_22
        $ stage_achievements_list.append("v_Monica_Strip_H2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_H3 = Movie(play="video/v_Monica_Strip_H3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H3_end.jpg")
        show videov_Monica_Strip_H3
        pause 1.8
        hide videov_Monica_Strip_H3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_23
        $ stage_achievements_list.append("v_Monica_Strip_H3_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # I
    $ pose = 9
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_I1 = Movie(play="video/v_Monica_Strip_I1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I1_end.jpg")
        show videov_Monica_Strip_I1
        pause 1.8
        hide videov_Monica_Strip_I1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_24
        $ stage_achievements_list.append("v_Monica_Strip_I1_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_I2 = Movie(play="video/v_Monica_Strip_I2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I2_end.jpg")
        show videov_Monica_Strip_I2
        pause 1.8
        hide videov_Monica_Strip_I2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_25
        $ stage_achievements_list.append("v_Monica_Strip_I2_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_I3 = Movie(play="video/v_Monica_Strip_I3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I3_end.jpg")
        show videov_Monica_Strip_I3
        pause 1.8
        hide videov_Monica_Strip_I3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result) from _rcall_pub_dance_dialogues_react_26
        $ stage_achievements_list.append("v_Monica_Strip_I3_end")


    if ep29_quests_claire_dance_planned == True:
        jump pub_dance2_claire_dance

    if stage_dance_nude_planned != True:
        jump pub_dance1_stage_end

    music stageCurrentMusicIntro
    with fadelong
    call ep213_dialogues3_pub_9() from _rcall_ep213_dialogues3_pub_9 # Диалог о том чтобы полностью раздеться
    if _return == False:
        jump pub_dance1_stage_end

    $ questHelp("shinyhole_44", True)
    if questHelpFlag15 == False:
        $ questHelpFlag15 = True
#        $ questHelp("shinyhole_42")
        $ questHelp("shinyhole_44a", skipIfExists=True)
        $ questHelp("shinyhole_44b")
        $ questHelp("shinyhole_44c")
        $ questHelpDesc("shinyhole_desc12", "shinyhole_desc12a")

    $ stage_dance_nude_last_day = day
    $ pub_dance_dialogues_tips_list = 0
    # Танец обнаженной
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    # Поза1
    # H
    $ pose = 18
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    fadeblack 1.0
    music stageCurrentMusicLoop
    if result == "up":
        scene black
        image videov_Monica_Strip_Nude_01 = Movie(play="video/v_Monica_Strip_Nude_01.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_01_end.jpg")
        show videov_Monica_Strip_Nude_01
        pause 1.8
        hide videov_Monica_Strip_Nude_01
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_01_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react
        $ stage_achievements_list.append("v_Monica_Strip_Nude_01_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_02 = Movie(play="video/v_Monica_Strip_Nude_02.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_02_end.jpg")
        show videov_Monica_Strip_Nude_02
        pause 1.8
        hide videov_Monica_Strip_Nude_02
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_02_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_1
        $ stage_achievements_list.append("v_Monica_Strip_Nude_02_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_03 = Movie(play="video/v_Monica_Strip_Nude_03.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_03_end.jpg")
        show videov_Monica_Strip_Nude_03
        pause 1.8
        hide videov_Monica_Strip_Nude_03
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_03_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_2
        $ stage_achievements_list.append("v_Monica_Strip_Nude_03_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 19
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_04 = Movie(play="video/v_Monica_Strip_Nude_04.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_04_end.jpg")
        show videov_Monica_Strip_Nude_04
        pause 1.8
        hide videov_Monica_Strip_Nude_04
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_04_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_3
        $ stage_achievements_list.append("v_Monica_Strip_Nude_04_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_05 = Movie(play="video/v_Monica_Strip_Nude_05.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_05_end.jpg")
        show videov_Monica_Strip_Nude_05
        pause 1.8
        hide videov_Monica_Strip_Nude_05
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_05_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_4
        $ stage_achievements_list.append("v_Monica_Strip_Nude_05_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_06 = Movie(play="video/v_Monica_Strip_Nude_06.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_06_end.jpg")
        show videov_Monica_Strip_Nude_06
        pause 1.8
        hide videov_Monica_Strip_Nude_06
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_06_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_5
        $ stage_achievements_list.append("v_Monica_Strip_Nude_06_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 20
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_07 = Movie(play="video/v_Monica_Strip_Nude_07.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_07_end.jpg")
        show videov_Monica_Strip_Nude_07
        pause 1.8
        hide videov_Monica_Strip_Nude_07
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_07_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_6
        $ stage_achievements_list.append("v_Monica_Strip_Nude_07_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_08 = Movie(play="video/v_Monica_Strip_Nude_08.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_08_end.jpg")
        show videov_Monica_Strip_Nude_08
        pause 1.8
        hide videov_Monica_Strip_Nude_08
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_08_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_7
        $ stage_achievements_list.append("v_Monica_Strip_Nude_08_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_09 = Movie(play="video/v_Monica_Strip_Nude_09.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_09_end.jpg")
        show videov_Monica_Strip_Nude_09
        pause 1.8
        hide videov_Monica_Strip_Nude_09
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_09_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_8
        $ stage_achievements_list.append("v_Monica_Strip_Nude_09_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 21
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_10 = Movie(play="video/v_Monica_Strip_Nude_10.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_10_end.jpg")
        show videov_Monica_Strip_Nude_10
        pause 1.8
        hide videov_Monica_Strip_Nude_10
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_10_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_9
        $ stage_achievements_list.append("v_Monica_Strip_Nude_10_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_11 = Movie(play="video/v_Monica_Strip_Nude_11.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_11_end.jpg")
        show videov_Monica_Strip_Nude_11
        pause 1.8
        hide videov_Monica_Strip_Nude_11
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_11_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_10
        $ stage_achievements_list.append("v_Monica_Strip_Nude_11_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_12 = Movie(play="video/v_Monica_Strip_Nude_12.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_12_end.jpg")
        show videov_Monica_Strip_Nude_12
        pause 1.8
        hide videov_Monica_Strip_Nude_12
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_12_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_11
        $ stage_achievements_list.append("v_Monica_Strip_Nude_12_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 22
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_13 = Movie(play="video/v_Monica_Strip_Nude_13.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_13_end.jpg")
        show videov_Monica_Strip_Nude_13
        pause 1.8
        hide videov_Monica_Strip_Nude_13
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_13_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_12
        $ stage_achievements_list.append("v_Monica_Strip_Nude_13_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_14 = Movie(play="video/v_Monica_Strip_Nude_14.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_14_end.jpg")
        show videov_Monica_Strip_Nude_14
        pause 1.8
        hide videov_Monica_Strip_Nude_14
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_14_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_13
        $ stage_achievements_list.append("v_Monica_Strip_Nude_14_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_15 = Movie(play="video/v_Monica_Strip_Nude_15.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_15_end.jpg")
        show videov_Monica_Strip_Nude_15
        pause 1.8
        hide videov_Monica_Strip_Nude_15
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_15_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_14
        $ stage_achievements_list.append("v_Monica_Strip_Nude_15_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 23
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_16 = Movie(play="video/v_Monica_Strip_Nude_16.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_16_end.jpg")
        show videov_Monica_Strip_Nude_16
        pause 1.8
        hide videov_Monica_Strip_Nude_16
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_16_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_15
        $ stage_achievements_list.append("v_Monica_Strip_Nude_16_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_17 = Movie(play="video/v_Monica_Strip_Nude_17.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_17_end.jpg")
        show videov_Monica_Strip_Nude_17
        pause 1.8
        hide videov_Monica_Strip_Nude_17
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_17_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_16
        $ stage_achievements_list.append("v_Monica_Strip_Nude_17_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_18 = Movie(play="video/v_Monica_Strip_Nude_18.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_18_end.jpg")
        show videov_Monica_Strip_Nude_18
        pause 1.8
        hide videov_Monica_Strip_Nude_18
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_18_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_17
        $ stage_achievements_list.append("v_Monica_Strip_Nude_18_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 24
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_19 = Movie(play="video/v_Monica_Strip_Nude_19.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_19_end.jpg")
        show videov_Monica_Strip_Nude_19
        pause 1.8
        hide videov_Monica_Strip_Nude_19
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_19_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_18
        $ stage_achievements_list.append("v_Monica_Strip_Nude_19_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_20 = Movie(play="video/v_Monica_Strip_Nude_20.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_20_end.jpg")
        show videov_Monica_Strip_Nude_20
        pause 1.8
        hide videov_Monica_Strip_Nude_20
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_20_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_19
        $ stage_achievements_list.append("v_Monica_Strip_Nude_20_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_21 = Movie(play="video/v_Monica_Strip_Nude_21.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_21_end.jpg")
        show videov_Monica_Strip_Nude_21
        pause 1.8
        hide videov_Monica_Strip_Nude_21
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_21_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_20
        $ stage_achievements_list.append("v_Monica_Strip_Nude_21_end")

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ pose = 25
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
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
        image videov_Monica_Strip_Nude_22 = Movie(play="video/v_Monica_Strip_Nude_22.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_22_end.jpg")
        show videov_Monica_Strip_Nude_22
        pause 1.8
        hide videov_Monica_Strip_Nude_22
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_22_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_21
        $ stage_achievements_list.append("v_Monica_Strip_Nude_22_end")
    if result == "side":
        scene black
        image videov_Monica_Strip_Nude_23 = Movie(play="video/v_Monica_Strip_Nude_23.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_23_end.jpg")
        show videov_Monica_Strip_Nude_23
        pause 1.8
        hide videov_Monica_Strip_Nude_23
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_23_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_22
        $ stage_achievements_list.append("v_Monica_Strip_Nude_23_end")
    if result == "down":
        scene black
        image videov_Monica_Strip_Nude_24 = Movie(play="video/v_Monica_Strip_Nude_24.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_24_end.jpg")
        show videov_Monica_Strip_Nude_24
        pause 1.8
        hide videov_Monica_Strip_Nude_24
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_24_end.jpg")
        wclean
        call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_23
        $ stage_achievements_list.append("v_Monica_Strip_Nude_24_end")

    if result == "up":
        $ pose = 26
        $ arrowUp = False
        $ arrowSide = True
        $ arrowDown = False
        show screen poledance_camera_icon(stage_Monica_shoots_array)
        show screen poledance()
        $ result = ui.interact()
        if result == "stop":
            jump pub_dance1_stage_stop
        hide screen poledance
        hide screen poledance_camera_icon
        hide screen love_bar_screen
        hide screen poledance_shoot
        hide screen poledance_coins
        $ result = "side"
        if result == "side":
            scene black
            image videov_Monica_Strip_Nude_25 = Movie(play="video/v_Monica_Strip_Nude_25.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Nude_25_end.jpg")
            show videov_Monica_Strip_Nude_25
            pause 1.8
            hide videov_Monica_Strip_Nude_25
            show screen poledance_shoot("/images/Slides/v_Monica_Strip_Nude_25_end.jpg")
            wclean
            call pub_dance_nude_dialogues_react(pose, result) from _rcall_pub_dance_nude_dialogues_react_24
            $ stage_achievements_list.append("v_Monica_Strip_Nude_25_end")


    if monica_shiny_hole_queen_day > 0: # Если Моника королева
        call ep215_dialogues1_pub_14a() from _rcall_ep215_dialogues1_pub_14a
        if _return == False:
            jump pub_dance1_stage_end
    jump pub_dance1_stage_end












##############################################


#############################

label pub_dance1_stage_stop:
    # Прерывание танца
    call dialogue_5_dance_strip_4m() from _rcall_dialogue_5_dance_strip_4m_1
    jump pub_dance1_stage_end

label pub_dance1_stage_end:
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

    if len(list(set(stage_Monica_shoots_array))) >= 27:
        $ questHelp("shinyhole_16", True)
        $ questHelp("shinyhole_23", skipIfExists=True)
    if len(list(set(stage_Monica_shoots_array))) >= 51:
        $ questHelp("shinyhole_24", True)
    if len(list(set(stage_Monica_shoots_array))) >= 76:
        $ questHelp("shinyhole_44a", True)
    pause 1.0
    $ stage_Monica_last_shoots_array = stage_Monica_shoots_array_current
    return

label pub_dance_stage_flash:
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return
