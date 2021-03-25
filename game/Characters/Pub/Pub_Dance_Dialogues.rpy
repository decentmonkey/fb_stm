default pub_dance_dialogues_up_list = []
default pub_dance_dialogues_up_list2 = []
default pub_dance_dialogues_side_list = []
default pub_dance_dialogues_side_list2 = []
default pub_dance_dialogues_down_list = []
default pub_dance_dialogues_down_list2 = []

default pub_dance_dialogues_up_list3 = []
default pub_dance_dialogues_up_list4 = []
default pub_dance_dialogues_side_list3 = []
default pub_dance_dialogues_side_list4 = []
default pub_dance_dialogues_down_list3 = []
default pub_dance_dialogues_down_list4 = []

default pub_dance_dialogues_tips_list = 0

label pub_dance_dialogues_start_dancing:
    # Моника вышла на сцену
    if monicaDancingStage == 0:
        if cloth == "StripOutfit1":
            img 22901
        if cloth == "StripOutfit2":
            img 22903
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call dialogue_5_dance_strip_4a() from _rcall_dialogue_5_dance_strip_4a
        if rand1 == 2:
            call dialogue_5_dance_strip_4b() from _rcall_dialogue_5_dance_strip_4b

    if monicaDancingStage == 1:
        if cloth == "StripOutfit1":
            img 22900
        if cloth == "StripOutfit2":
            img 22903
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call dialogue_5_dance_strip_4c() from _rcall_dialogue_5_dance_strip_4c
        if rand1 == 2:
            call dialogue_5_dance_strip_4d() from _rcall_dialogue_5_dance_strip_4d

    if monicaDancingStage == 2:
        if cloth == "StripOutfit1":
            img 22902
        if cloth == "StripOutfit2":
            img 22903
        with fadelong
        if ep213_dialogues3_pub_8_planned == True:
            call ep213_dialogues3_pub_8() from _rcall_ep213_dialogues3_pub_8
            $ ep213_dialogues3_pub_8_planned = False
            return
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call dialogue_5_dance_strip_4e() from _rcall_dialogue_5_dance_strip_4e
        if rand1 == 2:
            call dialogue_5_dance_strip_4f() from _rcall_dialogue_5_dance_strip_4f
    return

label pub_dance_dialogues_react(pose, zone): # Реакция зала

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
        call pub_dance_dialogues_excitement_down(pose, zone) from _rcall_pub_dance_dialogues_excitement_down
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        $ idx = rand(1,4)
        $ crowdSound = "snd_crowd_uuu" + str(idx)
        sound crowdSound
        if zone == "up":
            if pose < 4:
                call dialogue_5_dance_strip_5a1() from _rcall_dialogue_5_dance_strip_5a1
            else:
                call dialogue_5_dance_strip_5d2() from _rcall_dialogue_5_dance_strip_5d2
        if zone == "side":
            if pose < 4:
                call dialogue_5_dance_strip_5b2() from _rcall_dialogue_5_dance_strip_5b2
            else:
                call dialogue_5_dance_strip_5e2() from _rcall_dialogue_5_dance_strip_5e2
        if zone == "down":
            if pose < 4:
                call dialogue_5_dance_strip_5c2() from _rcall_dialogue_5_dance_strip_5c2
            else:
                call dialogue_5_dance_strip_5f2() from _rcall_dialogue_5_dance_strip_5f2
    else:
        # Движение понравилось
        call pub_dance_dialogues_excitement_up(pose, zone) from _rcall_pub_dance_dialogues_excitement_up
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        call pub_dance_dialogues_excitement_tips() from _rcall_pub_dance_dialogues_excitement_tips
        $ idx = rand(1,3)
        $ applauseSound = "snd_applause" + str(idx)
        sound applauseSound
        call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_6
        if zone == "up":
            if pose < 4:
                call dialogue_5_dance_strip_5a() from _rcall_dialogue_5_dance_strip_5a
            else:
                call dialogue_5_dance_strip_5d() from _rcall_dialogue_5_dance_strip_5d
        if zone == "side":
            if pose < 4:
                call dialogue_5_dance_strip_5b() from _rcall_dialogue_5_dance_strip_5b
            else:
                call dialogue_5_dance_strip_5e() from _rcall_dialogue_5_dance_strip_5e
        if zone == "down":
            if pose < 4:
                call dialogue_5_dance_strip_5c() from _rcall_dialogue_5_dance_strip_5c
            else:
                call dialogue_5_dance_strip_5f() from _rcall_dialogue_5_dance_strip_5f


#    wclean
    $ notif_clean()

    return


label pub_dance_nude_dialogues_react(pose, zone): # Реакция зала

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
        call pub_dance_dialogues_excitement_down(pose, zone) from _rcall_pub_dance_dialogues_excitement_down_2
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        $ idx = rand(1,4)
        $ crowdSound = "snd_crowd_uuu" + str(idx)
        sound crowdSound
        if zone == "up":
            call dialogue_5_dance_strip_5d2() from _rcall_dialogue_5_dance_strip_5d2_1
        if zone == "side":
            call dialogue_5_dance_strip_5f2() from _rcall_dialogue_5_dance_strip_5f2_1
        if zone == "down":
            call dialogue_5_dance_strip_5f2() from _rcall_dialogue_5_dance_strip_5f2_2
    else:
        # Движение понравилось
        call pub_dance_dialogues_excitement_up(pose, zone) from _rcall_pub_dance_dialogues_excitement_up_2
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        call pub_dance_dialogues_excitement_tips() from _rcall_pub_dance_dialogues_excitement_tips_2
        $ idx = rand(1,3)
        $ applauseSound = "snd_applause" + str(idx)
        sound applauseSound
        call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_8
        if zone == "up":
            call ep213_dialogues3_pub_10() from _rcall_ep213_dialogues3_pub_10
        if zone == "side":
            call ep213_dialogues3_pub_10() from _rcall_ep213_dialogues3_pub_10_1
        if zone == "down":
            call ep213_dialogues3_pub_10() from _rcall_ep213_dialogues3_pub_10_2


#    wclean
    $ notif_clean()

    return

label pub_dance_claire_dialogues_react(pose, zone): # Реакция зала

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
            $ notif(t_("Моника с Клэр делали это движение в прошлый раз"))
        if zoneRepeated == True:
            $ notif(t_("Моника с Клэр повторяют направления танца"))
        call pub_dance_dialogues_excitement_down(pose, zone) from _rcall_pub_dance_dialogues_excitement_down_1
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        $ idx = rand(1,4)
        $ crowdSound = "snd_crowd_uuu" + str(idx)
        sound crowdSound
        call ep210_dialogue_5_dance_strip_5aa1() from _rcall_ep210_dialogue_5_dance_strip_5aa1
    else:
        # Движение понравилось
        call pub_dance_dialogues_excitement_up(pose, zone) from _rcall_pub_dance_dialogues_excitement_up_1
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        call pub_dance_dialogues_excitement_tips() from _rcall_pub_dance_dialogues_excitement_tips_1
        $ idx = rand(1,3)
        $ applauseSound = "snd_applause" + str(idx)
        sound applauseSound
        call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_7
        call ep210_dialogue_5_dance_strip_5a() from _rcall_ep210_dialogue_5_dance_strip_5a


#    wclean
    $ notif_clean()

    return

label pub_dance_dialogues_excitement_up(pose, zone):
    python:
        idx1 = 0
        if zone == "up":
            idx1 = 0
        if zone == "side":
            idx1 = 1
        if zone == "down":
            idx1 = 2
        excitementAmount = excitementTableUp[pose-1][idx1]
        stage_Monica_Excitement_Last = stage_Monica_Excitement_Current
        stage_Monica_Excitement_Current += excitementAmount
        if stage_Monica_Excitement_Current > 100:
            stage_Monica_Excitement_Current = 100
    return

label pub_dance_dialogues_excitement_down(pose, zone):
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

label pub_dance_dialogues_excitement_tips():
#    $ kupury = [1,2,5,10,20,50]
    if pub_dance_dialogues_tips_list == 0:
        $ kupury = [20,10,5,2,1]
    if pub_dance_dialogues_tips_list == 1:
        $ kupury = [10,5,2,2,1]
    if stage_Monica_Excitement_Current <= 27:
        $ moneyTips1 = rand(2,4)
    else:
        if stage_Monica_Excitement_Current <= 54:
            $ moneyTips1 = rand(4,6)
        else:
            if stage_Monica_Excitement_Current <= 69:
                $ moneyTips1 = rand(6,8)
            else:
                if stage_Monica_Excitement_Current <= 84:
                    $ moneyTips1 = rand(11,17)
                else:
                    if stage_Monica_Excitement_Current <= 100:
                        $ moneyTips1 = rand(27, 40)

    python:
        kupury_out = []
        curMoney = 0

        while curMoney < moneyTips1:
            flag1 = False
            for idx1 in range(0, len(kupury)):
                if kupury[idx1] <= moneyTips1-curMoney:
                    kupury_out.append(kupury[idx1])
                    curMoney += kupury[idx1]
                    flag1 = True
            if flag1 == False:
                curMoney = money
        shuffle(kupury_out)
        for kupura in kupury_out:
            money += kupura
            monica_strip_tips_today += kupura
    if money < 9:
        sound2 fx_coins_b3
    else:
        if moneyTips1 < 20:
            sound2 fx_coins_b2
        else:
            sound2 fx_coins_b1
    show screen poledance_coins(kupury_out)
    return

label pub_dance_battle_dialogues_react():
    # Движение понравилось
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    $ temp1 = stage_Monica_Excitement_Current
    $ stage_Monica_Excitement_Current = (stage_Monica_Excitement_Current + stage_Molly_Excitement_Current)/2
    call pub_dance_dialogues_excitement_tips() from _rcall_pub_dance_dialogues_excitement_tips_3
    $ stage_Monica_Excitement_Current = temp1
    call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_9
#    wclean
#    $ notif_clean()
    return

label pub_dance_battle_dialogues_applause(applauseSound):
    if applauseSound == "std":
        $ idx = rand(1,3)
        $ applauseSound = "snd_applause" + str(idx)
        sound applauseSound
