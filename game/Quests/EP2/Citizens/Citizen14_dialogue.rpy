label citizen14_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_14_1
    if citizen14_offered_last_day == day:
        imgr Dial_Citizen_14_4
        citizen14 "Я тороплюсь! У меня много важных дел!"
        return
    citizen14 "Какая красавица! Что тебе надо от такого как Я? Ик!..."
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen14_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen14_refuse_probability) > 0:
                imgr Dial_Citizen_14_2
                citizen14 "Флаер?..."
                call reduce_flyers() from _call_reduce_flyers_5
                "Хорошо... Ик!"
                imgr Dial_Citizen_14_3
                citizen14 "Но ты же не просто так подошла ко мне!"
                "Я ведь понравился тебе? Хрюк..."
                menu:
                    "Мне никто не может понравиться в этой дыре!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Мне никто не может понравиться в этой дыре!"
                    "Может и так...":
                        m "Возможно..."
                        citizen14 "Да, я знал, что ты заметишь, что я красавец! Хрюк..."
                        citizen14 "Ну что, пойдем с тобой в подворотню!"
                        m "Да ни за что!"
                        mt "Черт, и кто тынул меня за язык..."
            else:
                imgr Dial_Citizen_14_4
                citizen14 "Не возьму... Я все-равно его потеряю... Хрюк..."
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

label citizen14_dialogue_pilon:
    if ep214_quests_citizens_stage2 == True:
        jump ep215_slums1_dialogue_alcoholic

    imgl Dial_begin35_17
    imgr Dial_Citizen_14_1
    m "Привет! Помнишь меня?"
    imgr Dial_Citizen_14_3
    citizen14 "Ик! Конечно! Ну признайся уже, что я тебе понравился."
    mt "Животное... Думаю, не стоит иметь с этим типом ничего общего..."
    m "Ладно, я пожалуй пойду."
    return False
