default citizen11TookBottle = False

label citizen11_dialogue:
    imgl Dial_Monica_Sandwich_0
#    "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_11_1
    if citizen11_offered_last_day == day:
        imgr Dial_Citizen_11_4
        citizen11 "Ох, не сейчас..."
        return
    if citizen11TookBottle == True:
        imgl Dial_Monica_Sandwich_1
        imgr Dial_Citizen_11_3
        citizen11 "Моя спасительница! Для тебя, все что угодно!"
        m "Возьмите, пожалуйста, этот флаер..."
        citizen11 "Флаер? Да хоть два! Давай свой флаер!"
        call reduce_flyers() from _call_reduce_flyers_14
        citizen11 "Ты такая красивая! А дай я тебя поцелую!"
        m "Отвали, алкаш..."
        imgr Dial_Citizen_11_4
        citizen11 "Ах вот ты как... Ну ничего, я тебя это припомню!"
        mt "Я лучше пойду..."
        return
    citizen11 "Да? Что? Ох, моя голова..."
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen11_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
#                    if renpy.random.randint(0, 1) == 0:
            imgr Dial_Citizen_11_2
            citizen11 "Милая, флаер это последнее, что мне сейчас нужно. Нет ли у тебя чего покрепче?"
            m "Вы про алкоголь?"
            citizen11 "Господи, ну конечно..."
            menu:
                #этот пункт меню будет появляться если моника найдет к примеру рядом с помойкой или где еще полупустую бутылку. Надо подумать куда ее поставить.
                "Вот, возьмите." if check_inventory("vodka"):
                    sound bottle1
                    $ remove_inventory("vodka", 1, True)
                    m "Вот, возьмите, тут кое что есть."
                    $ citizen11TookBottle = True
#                            imgl Dial_Monica_Gives_Bottle
                    imgr Dial_Citizen_11_6
                    sound bottle_drinking
                    w
                    imgr Dial_Citizen_11_5
                    citizen11 "(Пьет) Ооо, Богиня! Ты меня спасла! Давай выпьем со мной, мне одному грустно."
                    m "Нет, что-то, не хочется."
                    mt "Ни за что."
                    citizen11 "И очень даже зря. Божественный напиток. Дак что ты хотела?"
                    m "Возьмите, пожалуйста, этот флаер..."
                    citizen11 "Флаер? Конечно, сколько угодно!"
                    call reduce_flyers() from _call_reduce_flyers_15
                "У меня нет алкоголя.":
                    imgl Dial_Monica_Sandwich_1
                    m "Мистер, у меня нет алкоголя, только флаеры с рекламой вкуснейших кебабов..."
                    imgr Dial_Citizen_11_4
                    citizen11 "Каких еще кебабов? Проваливай отсюда!"
                    imgl Dial_Monica_Sandwich_0
                    mt "Старый алкаш..."
                    $ kebabWorkMonicaRefusedAmount += 1
                    return
#                    else:
#                        img Dial_Citizen_11_3
#                        # можно ему бутыль в руку дорисовать?
#                        citizen11 "Не отрывай меня от глубоких мыслей! Я размышляю о бренности этого великолепного напитка!"
    return

    # диалог доступен только когда моника не работает на раздаче флаеров и если дала бутылку
label citizen11_dialogue_pilon:
    if citizen11TookBottle == False:
        mt "Старый алкаш..."
        return False
    imgl Dial_begin35_17
    imgr Dial_Citizen_11_1
    m "Привет! Помнишь меня?"
    imgr Dial_Citizen_11_3
    citizen11 "Конечно! Как я могу забыть мою спасительницу?"
    imgr Dial_Citizen_11_5
    citizen11 "Знаешь, недавно выплатили пособие по безработице и я купил один божественный напиток. Угостишься?"
    menu:
        "Нет, спасибо.":
            m "Думаю, в другой раз."
            citizen11 "Как хочешь, ты не знаешь от чего отказываешься..."
    mt "Похоже, его единственный интерес - алкоголь. Думаю, мне лучше уйти."
    m "Ладно, я пойду."
    return False
