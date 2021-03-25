default questOffendMonicaFlyersCitizen12Started = False
default questOffendMonicaFlyersCitizen12Completed = False

label citizen12_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_12_1
    if citizen12_offered_last_day == day:
        imgr Dial_Citizen_12_4
        citizen12 "Я тороплюсь! Мне некогда!"
        return
    citizen12 "Да, Крошка? Что ты хочешь от меня?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen12_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if questOffendMonicaFlyersCitizen12Started == True:
                citizen12 "Конечно, крошка, а ты не хочешь ничего у меня взять?"
                m "Вы это о чем?"
                imgr Dial_Citizen_12_4
                citizen12 "Сейчас, я покажу..."
                music Power_Bots_Loop
                sound snd_bodyfall
                img 8484
                with fadelong
                #звук падения тела
                w
                sound snd_woman_pain
                img 8485
                with hpunch
                m "Аххх!!!"
                # img хватает монику за плечи и сажает на колени
                img 8486
                with fade
                m "Что ты себе позволяешь?! Что ты делаешь?"

                sound snd_zip
                img 8487
                with fade
                #звук ширинки
                citizen12 "Расслабься, уверен, тебе это не впервой."
                # img ситизен расстегивает ширинку
                img 8488
                mt "Черт, из за дурацкой рекламы мне сложно двигаться..."
                img 8489
                m "Помогите! Кто-нибудь! Полиция!"
                img 8490
                with fade
                mt "Черт! Какая еще полиция?! Мне нельзя полицию!"
                img 8491
                with fade
                citizen12 "Крошка, сейчас сделаешь мне минет и получишь свои 5 долларов."
                img 8492
                w
                img 8493
                with fade
                m "Что ты сказал?! ПОМОГИТЕ, КТО НИБУДЬ!"
                # img появлятеся citizen6
                music Groove2_85
                img 8494
                with fadelong
                citizen6 "Что здесь происходит?"
                img 8495
                citizen12 "Эй, мужик, иди своей дорогой, или присоединяйся!"
                img 8496
                m "Пожалуйста, помогите мне! Я не шлюха!"
                img 8497
                citizen6 "А что мне за это будет?"
                img 8498
                m "Все, что захочешь, только помоги мне!"
                # citizen6 бьет citizen12 и тд тп
                img 8499
                with fadelong
                #звук удара
                sound snd_punch_face
                w
                #звук падения тела
                sound snd_bodyfall
                img 8500
                w
                img 8501
                w
                img 8502
                with fade
                w
                img 8503
                w
                img 8504
                w
                img 8505
                with fade
                m "Спасибо, спасибо большое!"
                citizen6 "Ага, подойдешь ко мне, обсудим мою награду."
                m "Что?"
                citizen6 "Ну ты же сама обещала, что у меня будет все, что я захочу..."
                $ set_active("Citizen_12", False, scene="all")
                $ add_hook("Citizen_12", "citizen12_dialogue_refuse_after_offend", scene="hostel_street2", priority = 200, label="monica_kebab_offend_refuse_talk")
                $ questOffendMonicaFlyersCitizen12Started = False # и это событие больше не появляется
                $ questOffendMonicaFlyersCitizen12Completed = True
                $ questHelp("work_slums_3", True)
                $ questHelp("work_slums_4", skipIfExitst=True)
                $ add_objective("thanks_for_rescue", t_("Сказать спасибо за спасение от нападения"), c_green, 40)
                $ kebabOffendQuestJustCompleted = True
                $ add_hook("Citizen_6", "citizen6_dialogue_after_offend_hook", scene="hostel_street2", label="monica_kebab_offend")
                call refresh_scene_fade() from _call_refresh_scene_fade_48
                return
            if rand(0, citizen12_refuse_probability) > 0:
                imgr Dial_Citizen_12_2
                citizen12 "Ээээ... взять что?"
                m "Возьмите, пожалуйста, этот флаер..."
                call reduce_flyers() from _call_reduce_flyers_3
                citizen12 "Ок..."
                imgr Dial_Citizen_12_3
                citizen12 "И все? А как же развлечься?"
                menu:
                    "Я никого не собираюсь развлекать!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Я никого не собираюсь развлекать!"
                    "Чем тебя развлечь?":
                        m "Ты это о чем?"
                        citizen12 "Да все просто, отойдем в сторонку, покажешь сиськи, может что еще."
                        m "Не сегодня, засранец!"
                        citizen12 "Да ладно тебе! Подумай об этом. Это быстрый способ заработать."
            else:
                imgr Dial_Citizen_12_4
                citizen12 "Мне неинтересны никакие флаеры!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

label citizen12_dialogue_refuse_after_offend: #Когда подходит в кебабе после нападения
    imgc Dial_begin35_22
    m "Он хотел меня изнасиловать... Ни за что к нему не подойду..."
    return False
