label citizen10_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_10_1
    if citizen10_offered_last_day == day:
        imgr Dial_Citizen_10_4
        citizen10 "Я Вас не знаю! Не отвлекайте меня!"
        return
    citizen10 "Да? Я Вас откуда-то знаю?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen10_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen10_refuse_probability) > 0:
                imgr Dial_Citizen_10_2
                call reduce_flyers() from _call_reduce_flyers
                citizen10 "Флаер? Хорошо..."
                imgr Dial_Citizen_10_3
                citizen10 "Оу! Какая ты красотка! Прямо как бутон молодой орхидеи."
                imgl Dial_Monica_Sandwich_0
                mt "Что? Странный тип..."
                citizen10 "Как насчет того, чтобы продолжить нашу беседу?"
                menu:
                    "Хватит с меня разговоров!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        m "Мы уже достаточно с вами поговорили!"
                    "А о чем бы вы хотели поговорить?":
                        m "О чем бы вы хотели поговорить?"
                        citizen10 "Понимаете, я флорист. Я изучаю растения. Но также меня интересует красота женского тела. Это меня вдохновляет."
                        m "Нет, спасибо, как нибудь в другой раз."
                        mt "Он вообще нормальный?"
            else:
                imgr Dial_Citizen_10_4
                citizen10 "У меня полные карманы всяких бумажек!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
    # ФЛОРИСТ - его ветка в 04
label citizen10_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_10_4
    m "Эй, простите..."
    citizen10 "Не сейчас, я занят!"
    mt "Что это с ним?"
    return False
