default citizen4BoobsShowedFirstTime = False
default citizen4BoobsShowedSecondTimeCount = 0
default citizen4BoobsNakesShowingActive = False
default citizen4BoobsNakesShowedLastDay = 0
default citizen4BoobsNakedDancedLastDay = 0
default citizen4NakedBoobsRefuseFlag = False
default citizen4BoobsNakedDancedCount = -1
default citizen4BoobsNakedDancedCount1a = 0

default citizen4BoobsNakedDancedCount1 = 0
default citizen4BoobsNakedDancedCount2 = 0
default citizen4BoobsNakedDancedCount3 = 0

default citizen4DanceCloth = 0

label citizen4_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_4_1
    if citizen4_offered_last_day == day:
        imgr Dial_Citizen_4_4
        citizen4 "Нельзя!"
        return
    citizen4 "Да?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen4_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen4_refuse_probability) > 0:
                imgr Dial_Citizen_4_2
                call reduce_flyers() from _call_reduce_flyers_2
                citizen4 "Хорошо."
                citizen4 "А что на нем?"
                m "Это реклама вкусного кебаба... Там же написано!"
                imgr Dial_Citizen_4_3
                citizen4 "А я подумал Вы решили познакомиться со мной!"
                menu:
                    "У меня нет желания знакомиться с Вами!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "У меня нет желания знакомиться с Вами!"
                    "Что Вы подразумеваете под знакомством?":
                        m "Что вы имеете ввиду?"
                        citizen4 "Я бы хотел узнать по ближе такую красотку. Думаю, мы бы договорились."
                        m "Договорились о чем?"
                        citizen4 "Что за вопросы? Обычно девушки вашей профессии это понимают."
                        mt "Да что за люди здесь живут?! Всем надо одно и то же..."
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."
            else:
                imgr Dial_Citizen_4_4
                citizen4 "Давайте в другой раз!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen4_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_4_1
    m "Привет! Помню, ты хотел познакомиться поближе?"
    imgr Dial_Citizen_4_3
    citizen4 "Конечно, давай познакомимся."
    m "Ну я не о близком знакомстве...Немного о другом."
    citizen4 "Да не вопрос, я понимаю о чем речь. Любой из нашего района тебя поймет с полуслова."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_185
    call pylonController(2, 1) from _call_pylonController_36
    with fade
    citizen4 "Ну что, давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    $ showedNakedBoobsDance = False
    $ earnedMoney = 0
    if ep214_quests_citizens_stage2 == True:
        jump ep214_quests_citizens_regular
    label citizen4_dialogue_pilon_loop4:
    call pylonController(1, 1) from _call_pylonController_37
    if ep214_slums_offer_activated == False and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired + 1 and ep214_slums_offer_day != day:
        $ questHelp("work_slums_46", skipIfExists=True)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_38
            citizen4 "Покажи мне свои сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(3, 3) from _call_pylonController_39
            with fade

            $ questHelp("work_slums_6", True)
            $ questHelp("work_slums_16", skipIfExists=True)
            if questHelpFlag17 == False:
                $ questHelpFlag17 = True
                $ questHelpDesc("workslums_desc3", "workslums_desc4")

            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_6
            call pylonController(5, 3) from _call_pylonController_40
            # img показывает сиськи
            citizen4 "Да, очень хорошо, но я видел сиськи и получше!"
            call pylonController(5, 1) from _call_pylonController_41
            mt "Козел!"
            call pylonController(3, 1) from _call_pylonController_42
            citizen4 "Хотя весьма не плохо."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)


            # Разовое событие после которого появится еще 1 события у пилона -  голая грудь
            #Первый раз!!!
            # Ситизен предлагает Монике показать грудь за $ 50
            if citizen4BoobsShowedFirstTime == False:
                $ store_music()
                call citizen4_show_boobs_first_time() from _call_citizen4_show_boobs_first_time
                $ restore_music()
                if _return == True:
                    $ citizen4BoobsShowedFirstTime = True
            jump citizen4_dialogue_pilon_loop4
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_43
            citizen4 "Покажи свой задницу."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_44
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5) from _call_pylonController_45
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4) from _call_showRandomImages_7
            call pylonController(4, 5) from _call_pylonController_46
            citizen4 "Красивая задница, но я люблю побольше!"
            call pylonController(4, 5) from _call_pylonController_47
            citizen4 "Но ее можно увеличить, подумай об этом."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen4_dialogue_pilon_loop4
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_48
            citizen4 "Покрутись на шесте немного. Надеюсь, ты хорошо двигаешься."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_49
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_50
            with fade
            m "Хорошо, только не долго."
            $ citizen4DanceCloth += 1
            if citizen4DanceCloth >= 3:
                $ questHelp("work_slums_16", True)
                $ questHelp("work_slums_24", skipIfExists=True)


            call showRandomImages(pylonClothDanceImages3, 4) from _call_showRandomImages_8
#            call pylonController(4, 5)
            citizen4 "Сойдет. У меня есть знакомая стриптизерша. Если хочешь, могу вас познакомить."
            "Уж она то научит тебя всему."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_51
            with fade
            mt "И что ты за козел?!"
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen4_dialogue_pilon_loop4
#        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
        "Голые сиськи. (disabled)" if ((pylonpart4startsCompleted == False and citizen4BoobsShowedFirstTime == True) or citizen4BoobsNakesShowedLastDay == day) and not (citizen4BoobsNakesShowingActive == True and citizen4BoobsNakesShowedLastDay != day):
            pass
        "Голые сиськи." if citizen4BoobsNakesShowingActive == True and citizen4BoobsNakesShowedLastDay != day:
            $ citizen4BoobsNakesShowedLastDay = day
#            if ep214_slums_offer_activated == False and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired+1 and ep214_slums_offer_day != day:
#                call ep214_slums1_offer()
#                if _return == True:
#                    return False
#                jump citizen4_dialogue_pilon_loop4
            $ store_music()
            call citizen4_show_boobs_regular_time() from _call_citizen4_show_boobs_regular_time
            $ restore_music()
            jump citizen4_dialogue_pilon_loop4

            #регулярный показ (активировать позже!)
            call pylonController(4, 1) from _call_pylonController_52
            citizen4 "А теперь покажи своих малышек, похоже им там тесно."
            mt "Как он может так говорить о моей прекрасной груди?! Извращенец..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_53
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
            jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5) from _call_pylonController_54
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикоснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_9
            call pylonController(4, 5) from _call_pylonController_55
            citizen4 "А ничего такие сиськи, но я видел и лучше."
            call pylonController(4, 1) from _call_pylonController_56
            mt "Очень сомневаюсь..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4

            # DEPRECATED (старый диалог, замененный из citizen4!)
            call pylonController(4, 1) from _call_pylonController_57
            citizen4 "Показывай сиськи, только не забудь все снять."
            mt "Урод..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_58
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5) from _call_pylonController_59
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_10
            call pylonController(4, 5) from _call_pylonController_60
            citizen4 "Должен признать, твои сиськи хороши."
            mt "Ну еще бы!"
            citizen4 "Хотя страшно подумать, что с ними станет лет через 10..."
            mt "Что?"
            citizen4 "Знаешь, мой знакоый может тебе помочь кое в чем... За каких нибудь 500$ твои подруги наберут вес."
            citizen4 "Тебе дать его номер?"
            call pylonController(4, 1) from _call_pylonController_61
            m "Меня это не интересует! С тебя хватит!"

            citizen4 "Погоди минутку. Потряси ка своими сочными сиськами!"
            label citizen4_dialogue_pilon_loop4_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothNakedBoobsShakeCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothNakedBoobsShakeCorruptionRequired] corruption"
                        jump citizen4_dialogue_pilon_loop4_1
                    m "Ладно."
                    call pylonController(3, 4) from _call_pylonController_62
                    with fade
                    w
                    call showRandomImages(nakedboobsshakeImages, 1) from _call_showRandomImages_11
                    call pylonController(3, 4) from _call_pylonController_63
                    citizen4 "О да! Теперь мне еще больше хочется их потрогать!"
                    m "Даже не думай!"
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_64
                    m "Не собираюсь, и так достаточно."
                    citizen4 "Как хочешь. Похоже, мне придется найти другую шлюху."

            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4

        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen4BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen4BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen4BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired:
#            if ep214_slums_offer_activated == False and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired + 1 and ep214_slums_offer_day != day:
#                call ep214_slums1_offer()
#                if _return == True:
#                    return False
#                jump citizen4_dialogue_pilon_loop4
            $ store_music()
            if citizen4BoobsNakedDancedCount == -1:
                call cit4_naked_boobs_dance_1st() from _call_cit4_naked_boobs_dance_1st
                if _return != False:
                    $ citizen4BoobsNakedDancedCount += 1
            else:
                if citizen4BoobsNakedDancedCount%2 == 0:
                    call cit4_naked_boobs_dance_variant1() from _call_cit4_naked_boobs_dance_variant1
                if citizen4BoobsNakedDancedCount%2 == 1:
                    call cit4_naked_boobs_dance_variant2() from _call_cit4_naked_boobs_dance_variant2
                $ citizen4BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen4BoobsNakedDancedCount1a = citizen4BoobsNakedDancedCount + 1
                if citizen4BoobsNakedDancedCount1a >= 3:
                    $ questHelp("work_slums_36", True)

                $ citizen4BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen4_dialogue_pilon_loop4

        "Минет." if ep214_slums_offer_activated == False and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired + 1 and ep214_slums_offer_day != day:
            call ep214_slums1_offer() from _rcall_ep214_slums1_offer
            if _return == True:
                return False
            jump citizen4_dialogue_pilon_loop4

        "Достаточно на сегодня.":
            if showedBoobs == True or showedButt == True or showedDance == True or showedNakedBoobs == True or showedNakedBoobsDance == True:
                if showedBoobs == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedButt == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedDance == True:
                    $ earnedMoney += monicaWhoringClothDanceMoney
                if showedNakedBoobs == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoney
                if showedNakedBoobsDance == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoneyDance
                call pylonController(2, 1) from _call_pylonController_65
                citizen4 "А ты ничего такая, надо будет вернуться к нашему знакомству. Держи, заслужила."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_66
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_67
            citizen4 "Какое то не продуктивное вышло знакомство. Надеюсь, в другой раз будет лучше."
            return False
    return





label citizen4_show_boobs_first_time:
    # Ситизен предлагает Монике показать грудь за $ 50
    music Groove2_85
    img 10571
    with fade
    citizen4 "Хотя... Ты красивая девочка. Хочу оценить их без одежды."
    "Я недавно провернул одно дельце и у меня есть лишние 50$. Что скажешь?"
    menu:
        "Согласиться..." if corruption >= monicaWhoringClothNakedBoobsCorruptionRequired and fallingPathServedCustomersTotal >= 20:
            pass
        "Согласиться... (low corruption, required: [monicaWhoringClothNakedBoobsCorruptionRequired], 20 customers served) (disabled)" if corruption < monicaWhoringClothNakedBoobsCorruptionRequired or fallingPathServedCustomersTotal < 20:
            pass
#        if fallingPathServedCustomersTotal >= 20 and citizen4BoobsShowedFirstTime == False:
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10572
            with fade
            m "Да за кого ты меня принимаешь?!"
            m "Этого не будет никогда!"
            img 10571
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False
#                call pylonController(1, 1) #моника просто стоит у пилона
    img 10573
    with fade
    mt "50$ были бы не лишними... Хорошо, что здесь никого нет."
    img 10574
    with diss
    m "50$ ?"
    img 10575
    citizen4 "Все верно, девочка. Покажешь своих подружек и они твои."
    img 10576
    with fade
    mt "Черт! Моника, ты уверена что станешь делать это???"
    mt "Станешь показывать свою грудь какому-то нищему за жалкие 50$?"
    img 10577
    with diss
    mt "Но, с другой стороны, это же не я показываю грудь, а какая-то шлюха в трущобах."
    mt "Ведь никто даже представить себе не может что это делает Моника Бакфетт."
    mt "Это как какая-то виртуальная игра, в которой все не по настоящему..."
    mt "Но вот 50$, которые я получу, вполне реальны!"
#                call pylonController(3, 1)
    img 10578
    with fade
    m "Ладно, только не трогать!"
    img 10579
    citizen4 "Об этом не волнуйся, детка. Я не хочу проблем с твоим сутенером."
    music Power_Bots_Looop
    img 10580
    mt "Да за кого он меня принимает?"
#                call pylonController(3, 2)
    img 10581
    m "Хорошо, давай деньги."
    music Groove2_85
    img 10582
    with diss
    citizen4 "Только после того, как покажешь."
    citizen4 "Деньги вперед я могу дать только твоему сутенеру!"
    citizen4 "Извини, но таким девочкам как ты я на слово не верю..."
#                citizen4 "А ты не глупая девочка. Вот, держи."
#                $ add_money(50)
#                with fade
#                call showRandomImages(nakedboobsImages, 4)
#                call pylonController(3, 5) #моника показывет голые сиськи
    img 10583
    m "!!!"
    m "Отвернись!"
    img 10584
    with fade
    w
    music Loved_Up
    img 10585
    with fade
    w
    #показывает
    img 10586
    with fade
    w
    img 10587
    with Dissolve(0.3)
    $ renpy.pause(1.5)
    music stop
    sound plastinka2
    img 10586
    with Dissolve(0.3)
    music Groove2_85
    citizen4 "Эй! Куда ты их спрятала?!"
    img 10588
    with diss
    m "Я показала тебе свою грудь! Давай деньги!"
    citizen4 "Ты что, пошутила?! Я ничего не успел рассмотреть!"
    m "Ты увидел достаточно! Давай деньги, скорее!"
    img 10589
    with fade
    citizen4 "Я не дам тебе ничего, пока ты не покажешь мне грудь нормально!"
    citizen4 "Я хочу рассмотреть ее как следует! Иначе никаких денег!"
    img 10590
    with fadelong
    m "!!!"
    menu:
        "Согласиться...":
            pass
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10591
            with fade
            m "Да за кого ты меня принимаешь?!"
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False
    #Моника снова показывает грудь быстро
    music Loved_Up
    img 10592
    with Dissolve(0.3)
    $ renpy.pause(0.5)
    music stop
    sound plastinka2
    img 10590
    with Dissolve(0.3)
    music Groove2_85
    citizen4 "Эй! Хватит кривляться! Покажи грудь нормально!"

    img 10593
    citizen4 "Покажи грудь, а я досчитаю до пяти!"
    citizen4 "Если ты уберешь грудь раньше, то не получишь никаких денег!"
    img 10594
    with fade
    m "..."
    citizen4 "..."
    m "..."
    citizen4 "50$!"
    menu:
        "Согласиться...":
            pass
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10572
            with fade
            m "Да за кого ты меня принимаешь?!"
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False

    #Моника показывает грудь, а citizen ее обсматривает
    music Loved_Up
    img 10595
    with Dissolve(1.0)
    w
    img 10596
    with fade
    citizen4 "Один..."
    img 10597
    with fade
    citizen4 "Два..."
    img 10598
    with fade
    citizen4 "Три..."
    img 10599
    with fade
    w
    img 10600
    with fade
    w
    img 10601
    with diss
    w
    img 10602
    with fade
    citizen4 "Четыре..."
    img 10603
    with fade
    w
    img 10604
    with fade
    w
    citizen4 "Пять..."
    #Моника убирает грудь
    music Groove2_85
    img 10606
    with diss
    m "Доволен?"
    citizen4 "Более чем..."
    $ add_money(50)
#    $ pylonpart3startsCompleted = True
    # Добавить сколько то corruption
    $ questHelp("work_slums_24", True)
    $ questHelp("work_slums_25", skipIfExists=True)

    $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
    $ citizen4BoobsShowedFirstTime = True
    $ citizen4BoobsNakesShowingActive = True
    $ citizen4BoobsNakesShowedLastDay = day
    $ add_hook("enter_scene", "citizen4_dialogue_after_boobs_first_time", scene="hostel_edge_1_a")
    return True


label citizen4_show_boobs_regular_time:
    if (citizen4BoobsShowedSecondTimeCount < 2 or rand(1,2) == 1) and citizen4BoobsShowedSecondTimeCount != 1: #Показываем первые 1 раз точно, затем по рандому, кроме 2-го раза!
        #если активно ограничение показа груди
        img 10571
        with fade
        citizen4 "А теперь покажи своих малышек, похоже им там тесно."
        img 10573
        with fade
        mt "Мне надо как-то получить больше денег с этого бродяги..."
        mt "Может быть показать ему снова мою грудь?"
        mt "Он ведь уже видел ее..."
        img 10583
        with fade
        m "Если ты хочешь, я могу показать тебе свою грудь..."
        m "Снова..."
        img 10589
        citizen4 "Конечно! Я соскучился по твоим малышкам!"
        img 10581
        m "50$!"
        img 10593
        citizen4 "Что? Какие еще 50$?"
        citizen4 "Я уже видел твоих малышек!"
        citizen4 "Хочешь снова 50$ - покажи мне другие!"
        citizen4 "Ты можешь привести кого-нибудь и поделить с ней деньги."
        citizen4 "Но учти, я уже видел почти всех малышек в этом районе!"
        citizen4 "За малышек, которые я уже видел, я готов заплатить [monicaWhoringNakedBoobsMoney]$!"

        music Pyro_Flow
        img 10572
        with fade
        m "Мне некого приводить!"
        m "И моя грудь самая лучшая!"
        mt "Черт! Все мировые издания об этом писали!"
        music Groove2_85
        img 10571
        citizen4 "Я готов заплатить тебе [monicaWhoringNakedBoobsMoney]$ и не более..."
        menu:
            "Согласиться...":
                pass
            "Отказаться.":
    #            call pylonController(4, 1)
                m "Да за кого ты меня принимаешь?!"
                $ questHelp("work_slums_25", False)
                return False
        music Hidden_Agenda
        sound snd_fabric1
        img 10585
        with fadelong
        w
        img 10586
        with fade
        w
        img 10592
        with diss
        m "Так и быть, только руками не трогать."
        img 10596
        with diss
        mt "Только попробуй к ним прикоснуться и я сломаю тебе пальцы."
        img 10603
        with diss
        citizen4 "А ничего такие сиськи, но я видел и лучше."
        img 10606
        with fade
        mt "Очень сомневаюсь..."
        $ showedNakedBoobs = True
        $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))

        $ citizen4BoobsShowedSecondTimeCount += 1
        return True

    #Если не хочет смотреть на них
    img 10573
    with fade
    mt "Мне надо как-то получить больше денег с этого бродяги..."
    mt "Может быть показать ему снова мою грудь?"
    mt "Он ведь уже видел ее..."
    img 10583
    with fade
    m "Если ты хочешь, я могу показать тебе свою грудь..."
    m "Снова..."
    img 10593
    citizen4 "Сегодня я не хочу смотреть твоих малышек!"
    citizen4 "Покажи их кому-нибудь другому!"
    citizen4 "Уверен, ты сможешь заработать [monicaWhoringNakedBoobsMoney]$."
    $ questHelp("work_slums_25", True)
    if game.extra == True:
        $ questHelp("work_slums_26", skipIfExists=True)
    $ questHelp("work_slums_36", skipIfExists=True)

    if citizen4NakedBoobsRefuseFlag == False:
        $ citizen4NakedBoobsRefuseFlag = True
        $ add_hook("enter_scene", "citizen4_dialogue_after_boobs_second_time", scene="hostel_edge_1_a")

    return

label citizen4_dialogue_after_boobs_first_time:
    $ remove_hook()
    mt "Дьявол!"
    mt "Я не уверена что мне стоило делать это!"
    mt "Я думала это будет проще!"
    mt "Этот урод заставил меня пол дня стоять на улице, сверкая своей обнаженной бесценной, очаровательной грудью!"
    mt "Но за эти же деньги мне пришлось бы два месяца носить рекламу кебаба..."
    mt "Главное - это то что меня никто не видел."
    mt "И никто не знает кто я на самом деле, так что я могу делать все что потребуется."
    mt "Мне пришлось показать грудь - пускай!"
    mt "Это поможет мне сэкономить время на поиск еды, чтобы потратить его на решение моих главных проблем."
    mt "Моя цель - это вернуть назад мою роскошную жизнь."
    mt "И я не остановлюсь ни перед чем!"
    return


label citizen4_dialogue_after_boobs_second_time:
    $ remove_hook()
    mt "Вот мерзавец!"
    mt "Он отказался смотреть на мою грудь даже за [monicaWhoringNakedBoobsMoney]$ !"
    mt "Может быть показать мою грудь кому-нибудь еще?"
    mt "Это звучит дико, но мне нужны деньги..."
    mt "Похоже, в этом районе все относятся совершенно нормально к таким вещам..."
    mt "А я нахожусь здесь анонимно..."
    mt "То что здесь происходит никак не связано с жизнью Моники Бакфетт."
    mt "Так что мне нечего стесняться."
    mt "Мне это глубоко противно, но я отношусь к этому с хладнокровием."
    mt "В конце концов, это ненадолго."
    $ questHelp("work_slums_27", skipIfExists=True)
    $ questHelp("work_slums_28", skipIfExists=True)
    $ questHelp("work_slums_29", skipIfExists=True)
    $ questHelp("work_slums_30", skipIfExists=True)
    $ questHelp("work_slums_31", skipIfExists=True)
    $ questHelp("work_slums_32", skipIfExists=True)
    $ questHelp("work_slums_33", skipIfExists=True)
    $ questHelp("work_slums_34", skipIfExists=True)
    $ questHelp("work_slums_35", skipIfExists=True)


    $ pylonpart4startsCompleted = True
#    help "Будет доступно в следующем обновлении игры. Следите за новостями!"
    return

# первый раз танцы с сиськами
label cit4_naked_boobs_dance_1st:
    music Groove2_85
    img 13371
    with fade
    citizen4 "Я бы посмотрел на твои сиськи еще разок, но в танце. Что скажешь?"
    img 13372
    m "Не слишком ли многого ты хочешь?!"
    img 13373
    citizen4 "Девочка, ты забыла где ты? В этом районе каждая вторая готова таким образом заработать пару лишних долларов."
    citizen4 "Решайся быстрее, у меня нет времени. Ну дак что?"
    img 13374
    with fade
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13375
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13376
    with fade
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет..."
    img 13377
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13378
    citizen4 "Ладно, только в этот раз..."
    img 13379
    with diss
    w
    music Loved_Up
    sound snd_fabric1
    img 13380
    with diss
    w
    # поворачиваются, моника стоит с голыми сиськами
    img 13381
    with fadelong
    citizen4 "Залезай уже на пилон и начинай!"
    music Groove2_85
    img 13382
    m "Почему Вы такой грубый?"
    img 13383
    citizen4 "Я нормальный, да и не твое это дело! Твое дело крутить жопой на пилоне! Начинай!"
    img 13384
    with fade
    menu:
        "Хорошо.":
            pass
        "Я передумала.":
            img 13386
            m "Знаете, я передумала!"
            return False
    img 13385
    with fade
    m "Хорошо."
    mt "Мне нужны эти деньги... Черт..."
    # движение на пилоне
    music RocknRoll_loop
    img 13387
    with fadelong
    w
    img 13388
    with diss
    citizen4 "А знаешь, не плохо!"
    # движение на пилоне еще
    img 13389
    with diss
    w
    img 13390
    with diss
    w
    img 13391
    with diss
    citizen4 "Жопу бы тебе побольше!"
    # движение на пилоне еще
    img 13392
    with diss
    w
    img 13393
    with diss
    citizen4 "Да, очень не дурно."
    # движение на пилоне еще
    img 13394
    with diss
    w
    music Groove2_85
    img 13395
    with fadelong
    citizen4 "Знаешь, у тебя есть будущее, но надо больше практики и накачай жопу!"
    # моника слезает с шеста
    img 13396
    with fade
    citizen4 "Вот держи, заработала!"
    mt "!!!"
    $ nakedBoobsDanceFirstly_Cit4 = True
    return True

# танцы с сиськами вариант 1
label cit4_naked_boobs_dance_variant1:
    music Groove2_85
    img 13400
    with fade
    citizen4 "Думаю, стоит закрепить начатое. Полезай на пилон. И блузку сними!"
    img 13397
    m "Зачем мне снимать блузку, если ты не хочешь смотреть на мою грудь?"
    img 13401
    citizen4 "Это не твое дело! Я говорю, ты делаешь."
    citizen4 "Ну дак что?"
    img 13398
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13402
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13399
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13403
    citizen4 "Все равно мне не интересны твои сиськи."
    sound snd_fabric1
    img 13404
    with diss
    mt "Как он может такое говорить? Моя прекрасная грудь много кого интересует!"
    # поворачиваются, моника стоит с голыми сиськами
    img 13381
    with fadelong
    citizen4 "Залезай уже на пилон и начинай!"
    img 13382
    m "Хорошо."
    mt "Мерзавец..."
    # движение на пилоне
    music RocknRoll_loop
    img 13405
    with fadelong
    w
    img 13406
    with diss
    citizen4 "Мне кажется, я начинаю любить твои сиськи!"
    # движение на пилоне еще
    img 13407
    with diss
    w
    img 13408
    with diss
    citizen4 "Да, вот так, двигайся!"
    # движение на пилоне еще
    img 13409
    with diss
    w
    img 13410
    with diss
    citizen4 "Знаешь, все равно что-то не то. Кое чего не хватает."
    # движение на пилоне еще
    # ситизен пытается схватить монику за жопу во время ее вращения, но не выходит.
    # на варианте 2 он схватит ее за зад. должна быть такая поза, когда ты держишься за пилон в позе сидя
    # моника на повороте ударяет его ногой
    img 13411
    with diss
    w
    img 13412
    with diss
    w
    sound Jump1
    img 13413
    with diss
    w
    sound snd_punch_face1
    img 13414
    with diss
    w
    sound snd_down1
    music Power_Bots_Loop
    img 13415
    with diss
    citizen4 "Черт! Ты меня ударила!"
    # моника слезает с шеста
    img 13416
    with fade
    m "Вообще то я не хотела, ты подошел слишком близко!"
    img 13417
    citizen4 "Ты мне сломала нос!"
    img 13418
    m "Не правда, у тебя даже крови нет. В следующий раз не подходи близко."
    mt "Иначе я сделаю это специально!"
    music Groove2_85
    img 13419
    with fade
    citizen4 "Ха-ха-ха! Девочка начинает входить во вкус?"
    citizen4 "Следующий раз..."
    img 13420
    m "Плати!"
    img 13421
    citizen4 "Да не вопрос!"
    img 13422
    with fade
    mt "Все это толко для того, чтобы заработать немного денег. Ведь так, Моника?"
    return True

# танцы с сиськами вариант 2
label cit4_naked_boobs_dance_variant2:
    music Groove2_85
    img 13423
    with fade
    citizen4 "Думаю, стоит закрепить начатое. Полезай на пилон. И блузку сними!"
    img 13424
    m "Зачем мне снимать кофту, если ты не хочешь смотреть на мою грудь?"
    img 13425
    citizen4 "Это не твое дело! Я говорю, ты делаешь."
    citizen4 "Ну дак что?"
    img 13426
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13427
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13399
    with fade
    m "Хорошо. Только отвернись!"
    # отворачиваются
    img 13403
    citizen4 "Все равно мне не интересны твои сиськи."
    sound snd_fabric1
    img 13404
    with diss
    mt "Как он может такое говорить? Моя прекрасная грудь много кого интересует!"
    # поворачиваются, моника стоит с голыми сиськами
    img 13381
    with fadelong
    citizen4 "Залезай уже на пилон и начинай!"
    img 13382
    m "Хорошо."
    mt "Мерзавец..."
    # движение на пилоне
    music RocknRoll_loop
    img 13428
    with fadelong
    w
    img 13429
    with diss
    citizen4 "Мне кажется, я начинаю любить твои сиськи!"
    # движение на пилоне еще
    img 13430
    with diss
    w
    img 13431
    with diss
    citizen4 "Да, вот так, двигайся!"
    # движение на пилоне еще
    img 13432
    with diss
    w
    img 13433
    with diss
    w
    img 13434
    with diss
    citizen4 "Знаешь, все равно что-то не то. Кое чего не хватает."
    # движение на пилоне еще
    # ситизен пытается схватить монику за жопу во время ее вращения. Выходит.
    img 13821
    with diss
    w
    sound Jump1
    img 13822
    with diss
    w
    sound Jump2
    img 13436
    with diss
    w
    img 13435
    with diss
    citizen4 "Вот чего не хватает! Моей руки на твоей сочной жопе!"
    music Power_Bots_Loop
    img 13437
    with hpunch
    m "Какого черта? Отпути меня!"
    img 13438
    with diss
    citizen4 "Не, мне нравится твой зад!"
    img 13439
    with fade
    mt "Черт, если я отпущу пилон, он может меня отпустить и я упаду... Что делать?"
    img 13440
    with diss
    menu:
        "Отпустить руки.":
            # моника отпускает руки и ситизен отпускает ее. моника падает
            music Groove2_85
            sound Jump1
            img 13446
            with diss
            w
            sound snd_down1
            img 13447
            with diss
            w
            img 13448
            with diss
            w
            sound snd_bodyfall
            img 13449
            with diss
            w
            img 13450
            with fade
            citizen4 "Ха-ха-ха! Глупая девочка!"
            $ citizen4BoobsNakedDancedCount1 += 1
            pass
        "Угрожать.":
            music Power_Bots_Loop
            img 13441
            with diss
            m "Знаешь что! Если ты меня не отпустишь, у тебя будут проблемы!"
            music Groove2_85
            img 13442
            citizen4 "Девочка, ты не в тех условиях, чтобы угрожать!"
            citizen4 "Погоди минутку..."
            # лапает
            sound Jump2
            img 13443
            with diss
            citizen4 "О да, отличный зад!"
            # лапает
            img 13444
            with diss
            citizen4 "Эх, маловат, но вполне годный!"
            # отпускает
            $ citizen4BoobsNakedDancedCount2 += 1
            pass
        "Терпеть.":
            img 13445
            with fade
            mt "Похоже, у меня нет выбора..."
            # лапает
            sound Jump2
            img 13443
            with diss
            citizen4 "О да, отличный зад!"
            # лапает
            img 13444
            with diss
            citizen4 "Эх, маловат, но вполне годный!"
            # отпускает
            $ citizen4BoobsNakedDancedCount3 += 1
            pass
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    img 13451
    with fadelong
    m "Я тебя убью!"
    img 13452
    with diss
    citizen4 "Началось... Вот твои два бакса, заработала."
    citizen4 "И вот еще один, за твой красивый зад!"
    $ earnedMoney +=1 # доллар за зад
    # моника злая
    img 13453
    with fade
    mt "Когда нибудь ты за это ответишь, я обещаю!"
    return True
