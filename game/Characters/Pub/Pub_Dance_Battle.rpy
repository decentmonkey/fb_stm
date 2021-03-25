# BATTLE1
default stage_Molly_Excitement_Current = 0
default stage_Molly_Excitement_Last = 0

label pub_dance_battle1_Molly1:
    $ stage_Monica_Excitement_Current = 0
    $ stage_Monica_Excitement_Last = 0
    $ stage_Molly_Excitement_Current = 0
    $ stage_Molly_Excitement_Last = 0
    $ stage_achievements_list = []
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
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly1_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[0]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly1"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly1A = Movie(play="video/v_StripBattle1_Molly1A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly1A_end.jpg")
            show videov_StripBattle1_Molly1A
            pause 1.8
            hide videov_StripBattle1_Molly1A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly1A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(15)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react
            customers1 "ВАУ!!! Битва сучек!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly1A_end")
            jump pub_dance_battle1_Molly1_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly1B = Movie(play="video/v_StripBattle1_Molly1B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly1B_end.jpg")
            show videov_StripBattle1_Molly1B
            pause 1.8
            hide videov_StripBattle1_Molly1B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly1B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(15)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_1
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_1
            customers3 "Охренительно, детка! Ты настоящая королева!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly1B_end")
            jump pub_dance_battle1_Molly1_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly1C = Movie(play="video/v_StripBattle1_Molly1C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly1C_end.jpg")
            show videov_StripBattle1_Molly1C
            pause 1.8
            hide videov_StripBattle1_Molly1C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly1C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(20)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_2
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_2
            customers2 "Да, рыжая королева! Покрути жопой! Вот так! ДАААА!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly1C_end")
            jump pub_dance_battle1_Molly1_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
#    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica1:

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica1_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[1]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica1"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica1A = Movie(play="video/v_StripBattle1_Monica1A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica1A_end.jpg")
            show videov_StripBattle1_Monica1A
            pause 1.8
            hide videov_StripBattle1_Monica1A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica1A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_3
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_3
            $ stage_achievements_list.append("v_StripBattle1_Monica1A_end")
            jump pub_dance_battle1_Monica1_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica1B = Movie(play="video/v_StripBattle1_Monica1B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica1B_end.jpg")
            show videov_StripBattle1_Monica1B
            pause 1.8
            hide videov_StripBattle1_Monica1B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica1B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_4
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_4
            customers4 "Давай, раздевайся, крошка!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica1B_end")
            jump pub_dance_battle1_Monica1_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica1C = Movie(play="video/v_StripBattle1_Monica1C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica1C_end.jpg")
            show videov_StripBattle1_Monica1C
            pause 1.8
            hide videov_StripBattle1_Monica1C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica1C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_5
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_5
            customers5 "Покажи нам свои сиськи!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica1C_end")
            jump pub_dance_battle1_Monica1_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
#    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()

    return

label pub_dance_battle1_Monica2:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica2_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[1]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica1"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica2A = Movie(play="video/v_StripBattle1_Monica2A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica2A_end.jpg")
            show videov_StripBattle1_Monica2A
            pause 1.8
            hide videov_StripBattle1_Monica2A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica2A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_6
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_6
            customers1 "ВАААУ!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica2A_end")
            jump pub_dance_battle1_Monica2_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica2B = Movie(play="video/v_StripBattle1_Monica2B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica2B_end.jpg")
            show videov_StripBattle1_Monica2B
            pause 1.8
            hide videov_StripBattle1_Monica2B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica2B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_7
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_7
            customers5 "Потряси своими сиськами для нас! Давай еще!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica2B_end")
            jump pub_dance_battle1_Monica2_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica2C = Movie(play="video/v_StripBattle1_Monica2C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica2C_end.jpg")
            show videov_StripBattle1_Monica2C
            pause 1.8
            hide videov_StripBattle1_Monica2C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica2C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_8
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_8
            customers5 "Покажи нам свои сиськи!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica2C_end")
            jump pub_dance_battle1_Monica2_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly2:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly2_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[2]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly2"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly2A = Movie(play="video/v_StripBattle1_Molly2A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly2A_end.jpg")
            show videov_StripBattle1_Molly2A
            pause 1.8
            hide videov_StripBattle1_Molly2A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly2A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_9
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_9
            customers4 "Королева Молли! Покажи класс!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly2A_end")
            jump pub_dance_battle1_Molly2_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly2B = Movie(play="video/v_StripBattle1_Molly2B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly2B_end.jpg")
            show videov_StripBattle1_Molly2B
            pause 1.8
            hide videov_StripBattle1_Molly2B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly2B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_10
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_10
            customers3 "ДААА! Настоящая королева Shiny Hole!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly2B_end")
            jump pub_dance_battle1_Molly2_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly2C = Movie(play="video/v_StripBattle1_Molly2C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly2C_end.jpg")
            show videov_StripBattle1_Molly2C
            pause 1.8
            hide videov_StripBattle1_Molly2C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly2C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_11
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_11
            customers2 "ДА! Покажи нам свою королевскую попку!!!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly2C_end")
            jump pub_dance_battle1_Molly2_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica3:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica3_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[3]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica3"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica3A = Movie(play="video/v_StripBattle1_Monica3A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica3A_end.jpg")
            show videov_StripBattle1_Monica3A
            pause 1.8
            hide videov_StripBattle1_Monica3A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica3A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_12
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_12
            customers5 "Вот она, королева! Охренительно, детка!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica3A_end")
            jump pub_dance_battle1_Monica3_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica3B = Movie(play="video/v_StripBattle1_Monica3B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica3B_end.jpg")
            show videov_StripBattle1_Monica3B
            pause 1.8
            hide videov_StripBattle1_Monica3B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica3B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_13
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_13
            customers2 "ДААА! Точно! Она королева!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica3B_end")
            jump pub_dance_battle1_Monica3_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica3C = Movie(play="video/v_StripBattle1_Monica3C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica3C_end.jpg")
            show videov_StripBattle1_Monica3C
            pause 1.8
            hide videov_StripBattle1_Monica3C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica3C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_14
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_14
            customers1 "Королева Shiny Hole! А где вторая голая попка?" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica3C_end")
            jump pub_dance_battle1_Monica3_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly3:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly3_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[4]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly3"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly3A = Movie(play="video/v_StripBattle1_Molly3A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly3A_end.jpg")
            show videov_StripBattle1_Molly3A
            pause 1.8
            hide videov_StripBattle1_Molly3A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly3A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_15
            sound3 men_scream2
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_15
            customers4 "Вау!!! Какая горячая детка!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly3A_end")
            jump pub_dance_battle1_Molly3_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly3B = Movie(play="video/v_StripBattle1_Molly3B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly3B_end.jpg")
            show videov_StripBattle1_Molly3B
            pause 1.8
            hide videov_StripBattle1_Molly3B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly3B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_16
            sound3 men_scream1
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_16
            customers3 "Покажи нам свою киску, крошка!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly3B_end")
            jump pub_dance_battle1_Molly3_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly3C = Movie(play="video/v_StripBattle1_Molly3C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly3C_end.jpg")
            show videov_StripBattle1_Molly3C
            pause 1.8
            hide videov_StripBattle1_Molly3C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly3C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_17
            sound3 men_scream2
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_17
            wclean
            $ stage_achievements_list.append("v_StripBattle1_Molly3C_end")
            jump pub_dance_battle1_Molly3_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly4:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly4_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[5]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly4"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly4A = Movie(play="video/v_StripBattle1_Molly4A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly4A_end.jpg")
            show videov_StripBattle1_Molly4A
            pause 1.8
            hide videov_StripBattle1_Molly4A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly4A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-15)
            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_18
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_18
            customers5 "ДААААААА!" # танцует Молли
            customers4 "МОЛЛИ, КРОШКА, ТЫ ЭТО СДЕЛАЛАААААА!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly4A_end")
            jump pub_dance_battle1_Molly4_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly4B = Movie(play="video/v_StripBattle1_Molly4B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly4B_end.jpg")
            show videov_StripBattle1_Molly4B
            pause 1.8
            hide videov_StripBattle1_Molly4B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly4B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-15)
            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_19
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_19
            customers3 "МОЯ КОРОЛЕВА!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly4B_end")
            jump pub_dance_battle1_Molly4_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly4C = Movie(play="video/v_StripBattle1_Molly4C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly4C_end.jpg")
            show videov_StripBattle1_Molly4C
            pause 1.8
            hide videov_StripBattle1_Molly4C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly4C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-10)
            sound3 men_scream3
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_20
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_20
            customers2 "ДААА! КОРОЛЕВА SHINY HOLE!" # танцует Молли
            customers1 "ВАААААУ!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly4C_end")
            jump pub_dance_battle1_Molly4_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return




# BATTLE 2

label pub_dance_battle1_Molly5:
    $ stage_Monica_Excitement_Current = 0
    $ stage_Monica_Excitement_Last = 0
    $ stage_Molly_Excitement_Current = 0
    $ stage_Molly_Excitement_Last = 0
    $ stage_achievements_list = []
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
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly5_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[0]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly5"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly5A = Movie(play="video/v_StripBattle1_Molly5A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly5A_end.jpg")
            show videov_StripBattle1_Molly5A
            pause 1.8
            hide videov_StripBattle1_Molly5A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly5A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
#            $ pub_dance_dialogues_set_excitement_monica(-15)
            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_21
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_21
            customers1 "ВАУ!!! Еще одна битва сучек!"
            $ stage_achievements_list.append("v_StripBattle1_Molly5A_end")
            jump pub_dance_battle1_Molly5_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly5B = Movie(play="video/v_StripBattle1_Molly5B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly5B_end.jpg")
            show videov_StripBattle1_Molly5B
            pause 1.8
            hide videov_StripBattle1_Molly5B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly5B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
#            $ pub_dance_dialogues_set_excitement_monica(-15)
            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_22
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_22
            customers2 "Да, рыжая королева! Покрути жопой! Вот так! ДАААА!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly5B_end")
            jump pub_dance_battle1_Molly5_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly5C = Movie(play="video/v_StripBattle1_Molly5C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly5C_end.jpg")
            show videov_StripBattle1_Molly5C
            pause 1.8
            hide videov_StripBattle1_Molly5C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly5C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
#            $ pub_dance_dialogues_set_excitement_monica(-10)
            sound3 men_scream3
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_23
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_23
            customers3 "Охренительно, детка! Ты настоящая королева!" # Molly
            customers2 "ДА! Покажи нам свою королевскую попку!!!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly5C_end")
            jump pub_dance_battle1_Molly5_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica5:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica5_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[1]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica5"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica5A = Movie(play="video/v_StripBattle1_Monica5A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica5A_end.jpg")
            show videov_StripBattle1_Monica5A
            pause 1.8
            hide videov_StripBattle1_Monica5A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica5A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_24
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_24
            $ stage_achievements_list.append("v_StripBattle1_Monica5A_end")
            wclean
            jump pub_dance_battle1_Monica5_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica5B = Movie(play="video/v_StripBattle1_Monica5B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica5B_end.jpg")
            show videov_StripBattle1_Monica5B
            pause 1.8
            hide videov_StripBattle1_Monica5B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica5B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(5)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_25
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_25
            $ stage_achievements_list.append("v_StripBattle1_Monica5B_end")
            wclean
            jump pub_dance_battle1_Monica5_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica5C = Movie(play="video/v_StripBattle1_Monica5C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica5C_end.jpg")
            show videov_StripBattle1_Monica5C
            pause 1.8
            hide videov_StripBattle1_Monica5C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica5C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(5)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_26
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_26
            customers4 "Давай, раздевайся, крошка!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica5C_end")
            jump pub_dance_battle1_Monica5_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica6:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica6_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[1]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica6"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica6A = Movie(play="video/v_StripBattle1_Monica6A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica6A_end.jpg")
            show videov_StripBattle1_Monica6A
            pause 1.8
            hide videov_StripBattle1_Monica6A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica6A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_27
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_27
            customers1 "ВАААУ!"  # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica6A_end")
            jump pub_dance_battle1_Monica6_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica6B = Movie(play="video/v_StripBattle1_Monica6B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica6B_end.jpg")
            show videov_StripBattle1_Monica6B
            pause 1.8
            hide videov_StripBattle1_Monica6B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica6B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_28
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_28
            customers5 "Давай, покрути своей задницей!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica6B_end")
            jump pub_dance_battle1_Monica6_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica6C = Movie(play="video/v_StripBattle1_Monica6C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica6C_end.jpg")
            show videov_StripBattle1_Monica6C
            pause 1.8
            hide videov_StripBattle1_Monica6C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica6C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_29
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_29
            customers5 "О, да! Вот это сиськи!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica6C_end")
            jump pub_dance_battle1_Monica6_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly6:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly6_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[2]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly6"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly6A = Movie(play="video/v_StripBattle1_Molly6A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly6A_end.jpg")
            show videov_StripBattle1_Molly6A
            pause 1.8
            hide videov_StripBattle1_Molly6A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly6A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
#            $ pub_dance_dialogues_set_excitement_monica(-15)
#            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_30
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_30
            customers4 "Королева Молли! Покажи класс!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly6A_end")
            jump pub_dance_battle1_Molly6_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly6B = Movie(play="video/v_StripBattle1_Molly6B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly6B_end.jpg")
            show videov_StripBattle1_Molly6B
            pause 1.8
            hide videov_StripBattle1_Molly6B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly6B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
#            $ pub_dance_dialogues_set_excitement_monica(-15)
#            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_31
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_31
            wclean
            $ stage_achievements_list.append("v_StripBattle1_Molly6B_end")
            jump pub_dance_battle1_Molly6_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly6C = Movie(play="video/v_StripBattle1_Molly6C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly6C_end.jpg")
            show videov_StripBattle1_Molly6C
            pause 1.8
            hide videov_StripBattle1_Molly6C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly6C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
#            $ pub_dance_dialogues_set_excitement_monica(-10)
#            sound3 men_scream3
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_32
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_32
            customers3 "ДААА! Настоящая королева Shiny Hole!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly6C_end")
            jump pub_dance_battle1_Molly6_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return


label pub_dance_battle1_Monica7:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica7_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[3]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica7"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica7A = Movie(play="video/v_StripBattle1_Monica7A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica7A_end.jpg")
            show videov_StripBattle1_Monica7A
            pause 1.8
            hide videov_StripBattle1_Monica7A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica7A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_33
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_33
            customers5 "Вот она, королева! Охренительно, детка!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica7A_end")
            jump pub_dance_battle1_Monica7_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica7B = Movie(play="video/v_StripBattle1_Monica7B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica7B_end.jpg")
            show videov_StripBattle1_Monica7B
            pause 1.8
            hide videov_StripBattle1_Monica7B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica7B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_34
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_34
            customers2 "ДААА! Точно! Она королева!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica7B_end")
            jump pub_dance_battle1_Monica7_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica7C = Movie(play="video/v_StripBattle1_Monica7C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica7C_end.jpg")
            show videov_StripBattle1_Monica7C
            pause 1.8
            hide videov_StripBattle1_Monica7C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica7C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
#            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_35
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_35
            customers4 "Пошли в приват, детка!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica7C_end")
            jump pub_dance_battle1_Monica7_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly7:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly7_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[4]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly7"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly7A = Movie(play="video/v_StripBattle1_Molly7A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly7A_end.jpg")
            show videov_StripBattle1_Molly7A
            pause 1.8
            hide videov_StripBattle1_Molly7A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly7A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(7)
#            $ pub_dance_dialogues_set_excitement_monica(-15)
#            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_36
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_36
            customers1 "Вау, детка! У меня уже в штанах дымится! Иди сюда!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly7A_end")
            jump pub_dance_battle1_Molly7_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly7B = Movie(play="video/v_StripBattle1_Molly7B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly7B_end.jpg")
            show videov_StripBattle1_Molly7B
            pause 1.8
            hide videov_StripBattle1_Molly7B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly7B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(7)
#            $ pub_dance_dialogues_set_excitement_monica(-15)
#            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_37
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_37
            customers3 "Покажи нам свою киску, крошка!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly7B_end")
            jump pub_dance_battle1_Molly7_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly7C = Movie(play="video/v_StripBattle1_Molly7C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly7C_end.jpg")
            show videov_StripBattle1_Molly7C
            pause 1.8
            hide videov_StripBattle1_Molly7C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly7C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(6)
#            $ pub_dance_dialogues_set_excitement_monica(-10)
#            sound3 men_scream3
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_38
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_38
            wclean
            $ stage_achievements_list.append("v_StripBattle1_Molly7C_end")
            jump pub_dance_battle1_Molly7_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()

    return

label pub_dance_battle1_Molly8:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly8_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[5]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly8"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly8A = Movie(play="video/v_StripBattle1_Molly8A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly8A_end.jpg")
            show videov_StripBattle1_Molly8A
            pause 1.8
            hide videov_StripBattle1_Molly8A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly8A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-15)
#            sound3 men_scream5
            sound3 men_scream2
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_39
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_39
            customers5 "ДААААААА!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly8A_end")
            jump pub_dance_battle1_Molly8_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly8B = Movie(play="video/v_StripBattle1_Molly8B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly8B_end.jpg")
            show videov_StripBattle1_Molly8B
            pause 1.8
            hide videov_StripBattle1_Molly8B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly8B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-15)
#            sound3 men_scream4
#            sound3 men_scream2
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_40
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_40
            $ stage_achievements_list.append("v_StripBattle1_Molly8B_end")
            jump pub_dance_battle1_Molly8_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly8C = Movie(play="video/v_StripBattle1_Molly8C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly8C_end.jpg")
            show videov_StripBattle1_Molly8C
            pause 1.8
            hide videov_StripBattle1_Molly8C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly8C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-10)
#            sound3 men_scream3
#            sound3 men_scream2
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_41
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_41
            customers5 "Королева Молли!" # Molly
            $ stage_achievements_list.append("v_StripBattle1_Molly8C_end")
            jump pub_dance_battle1_Molly8_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return


label pub_dance_battle1_Monica8:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica8_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[6]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica8"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica8A = Movie(play="video/v_StripBattle1_Monica8A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica8A_end.jpg")
            show videov_StripBattle1_Monica8A
            pause 1.8
            hide videov_StripBattle1_Monica8A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica8A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
            $ pub_dance_dialogues_set_excitement_molly(-20)
            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_42
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_42
            customers4 "Это же [monica_pub_name]!!!" # Monica
            customers4 "Она работает здесь официанткой!"
            customers1 "ОХРЕНЕЕЕТЬ!!!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica8A_end")
            jump pub_dance_battle1_Monica8_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica8B = Movie(play="video/v_StripBattle1_Monica8B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica8B_end.jpg")
            show videov_StripBattle1_Monica8B
            pause 1.8
            hide videov_StripBattle1_Monica8B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica8B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
            $ pub_dance_dialogues_set_excitement_molly(-20)
            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_43
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_43
            customers1 "Видели? Вы это видели?!"
            customers3 "[monica_pub_name] КОРОЛЕВА! ДААА!!!" # Monica
            $ stage_achievements_list.append("v_StripBattle1_Monica8B_end")
            jump pub_dance_battle1_Monica8_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica8C = Movie(play="video/v_StripBattle1_Monica8C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica8C_end.jpg")
            show videov_StripBattle1_Monica8C
            pause 1.8
            hide videov_StripBattle1_Monica8C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica8C_end.jpg")
            wclean
            sound3 men_scream3
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_44
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_44
            customers2 "ДААА! КОРОЛЕВА SHINY HOLE!" # Monica
            customers3 "[monica_pub_name] новая королева Shiny Hole!!!"
            $ stage_achievements_list.append("v_StripBattle1_Monica8C_end")
            jump pub_dance_battle1_Monica8_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
#    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica9:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica9_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[6]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica9"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica9A = Movie(play="video/v_StripBattle1_Monica9A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica9A_end.jpg")
            show videov_StripBattle1_Monica9A
            pause 1.8
            hide videov_StripBattle1_Monica9A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica9A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_45
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_45
            customers5 "Посмотрите что эта крошка творит на сцене!"
            $ stage_achievements_list.append("v_StripBattle1_Monica9A_end")
            jump pub_dance_battle1_Monica9_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica9B = Movie(play="video/v_StripBattle1_Monica9B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica9B_end.jpg")
            show videov_StripBattle1_Monica9B
            pause 1.8
            hide videov_StripBattle1_Monica9B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica9B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_46
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_46
            customers3 "Эта официантка горячая штучка!"
            $ stage_achievements_list.append("v_StripBattle1_Monica9B_end")
            jump pub_dance_battle1_Monica9_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica9C = Movie(play="video/v_StripBattle1_Monica9C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica9C_end.jpg")
            show videov_StripBattle1_Monica9C
            pause 1.8
            hide videov_StripBattle1_Monica9C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica9C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            sound3 men_scream3
            call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_47
            call pub_dance_battle_dialogues_react() from _rcall_pub_dance_battle_dialogues_react_47
            customers5 "Я трахну тебя в привате, крошка!"
            customers1 "Вставай в очередь!"
            customers2 "Держи на чай, детка! Ты заслужила это!"
            $ stage_achievements_list.append("v_StripBattle1_Monica9C_end")
            jump pub_dance_battle1_Monica9_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return



#
