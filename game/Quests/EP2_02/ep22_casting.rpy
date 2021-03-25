label ep22_casting:
    label ep22_dialogue6_6_loop1:
        #первый вызов
#        help "Пока доступны только две возможностьи. Другие пункты будут доступны в следующих версиях игры."
        $ menu_corruption = [0, 0, biffCastingModelPosesCorruptionRequired, biffCastingKneesCorruptionRequired, biffCastingFloorCorruptionRequred]
        menu:
            "Показать обнаженную грудь.":
                #Моника показывает грудь в зависимости от одежды
                $ store_music()
                music Loved_Up
                if castingCloth == 1:
                    if chickMode == True:
                        img 8441
                        with Dissolve(0.5)
                        m "Моника Бакфетт хочет показать папочке грудь..."
                        img 8442
                        with fade
                        w
                        img 8444
                        with Dissolve(0.5)
                        w
                    else:
                        img 8441
                        with Dissolve(0.5)
                        m "Я покажу тебе грудь, потому что ты заставил меня..."
                        img 8442
                        with fade
                        w
                        img 8443
                        with Dissolve(0.5)
                        w
                if castingCloth == 2:
                    if chickMode == True:
                        sound snd_fabric1
                        img 8460
                        with fade
                        m "Леди Нуар хочет показать папочке грудь..."
                        img 8461
                        biff "Давай, Леди Нуар! Показывай свои сиськи!"
                        "Не прячь их от папочки!"
                        img 8456
                        with Dissolve(0.5)
                        w
                        img 8457
                        with Dissolve(0.5)
                        w
                        img 8458
                        with Dissolve(0.5)
                        w
                        img 8459
                        with Dissolve(0.5)
                        w

                    else:
                        sound snd_fabric1
                        img 8453
                        with fade
                        m "Биф, мне обязательно это делать?"
                        img 8454
                        biff "Давай, Леди Нуар! Показывай свои сиськи!"
                        "Не прячь их от папочки!"
                        "А то я заставлю Леди Нуар показать еще кое-что!"
                        img 8455
                        with fade
                        w
                        img 8445
                        biff "Я жду!"
                        img 8455
                        with fade
                        w
                        img 8456
                        with Dissolve(0.5)
                        w
                        img 8457
                        with Dissolve(0.5)
                        w
                        img 8458
                        with Dissolve(0.5)
                        w
                        img 8459
                        with Dissolve(0.5)
                        w
                if castingCloth == 3:
                    if chickMode == True:
                        img 8473
                        with fade
                        m "Девушка с календаря хочет показать папочке грудь..."
                        sound snd_fabric1
                        img 8477
                        with Dissolve(0.5)
                        w
                        img 8478
                        with Dissolve(0.5)
                        w
                        img 8479
                        with Dissolve(0.5)
                        w
                    else:
                        img 8469
                        with fade
                        m "Я знаю, я должна показать тебе грудь..."
                        "Но можно я не буду делать этого?"
                        img 8470
                        biff "Давай! Девушка с календаря!"
                        "Показывай свои сиськи!"
                        "Иначе я скажу Алексу чтобы эти голые сиськи смотрели прямо с календаря!"
                        img 8471
                        with fade
                        mt "Черт! У меня молоток... Может убить этого мерзавца?!"
                        "Сколько мне терпеть это???"
                        "..."
                        "Нет... Слишком опасно..."
                        img 8472
                        biff "Ну же! Сиськи!"
                        img 8471
                        with fade
                        w
                        img 8474
                        with Dissolve(0.5)
                        w
                        img 8475
                        with Dissolve(0.5)
                        m "На, смотри..."
                        img 8476
                        with Dissolve(0.5)
                        w
                        "Мне не нужны проблемы..."
                        w
                if castingCloth == 4:
                    if chickMode == True:
                        img 9477
                        with fade
                        sound snd_fabric1
                        m "Роза надежды хочет показать папочке грудь..."
                        img 9478
                        with Dissolve(0.5)
                        w
                        img 9479
                        with Dissolve(0.5)
                        w
                        img 9480
                        with Dissolve(0.5)
                        w
                    else:
                        img 9481
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставил меня..."

                        img 9482
                        with Dissolve(0.5)
                        w
                        img 9483
                        with Dissolve(0.5)
                        w
                if castingCloth == 5:
                    if chickMode == True:
                        img 9500
                        with fade
                        sound snd_fabric1
                        m "Стюардесса хочет показать папочке грудь..."
                        img 9501
                        with Dissolve(0.5)
                        w
                        img 9502
                        with Dissolve(0.5)
                        w
                        img 9503
                        with Dissolve(0.5)
                        w
                        img 9504
                        with Dissolve(0.5)
                        w
                    else:
                        img 9500
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставляешь меня это делать!.."
                        img 9501
                        with Dissolve(0.5)
                        w
                        img 9502
                        with Dissolve(0.5)
                        w
                        img 9503
                        with Dissolve(0.5)
                        w
                        img 9504
                        with Dissolve(0.5)
                        w
                if castingCloth == 6:
                    if chickMode == True:
                        img 20184
                        with fade
                        sound snd_fabric1
                        m "Алая Жемчужина хочет показать папочке грудь..."
                        img 20185
                        with Dissolve(0.5)
                        w
                        img 20186
                        with Dissolve(0.5)
                        w
                        img 20187
                        with Dissolve(0.5)
                        w
                    else:
                        img 20184
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставляешь меня это делать!.."
                        img 20185
                        with Dissolve(0.5)
                        w
                        img 20186
                        with Dissolve(0.5)
                        w
                        img 20187
                        with Dissolve(0.5)
                        w
                if castingCloth == 7:
                    if chickMode == True:
                        img 20202
                        with fade
                        m "Запретное Желание хочет показать папочке грудь..."
                        img 20203
                        with Dissolve(0.5)
                        w
                        img 20204
                        with Dissolve(0.5)
                        w
                        img 20205
                        with Dissolve(0.5)
                        w
                        img 20206
                        with diss
                        w
                    else:
                        img 20202
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставляешь меня это делать!.."
                        img 20203
                        with Dissolve(0.5)
                        w
                        img 20204
                        with Dissolve(0.5)
                        w
                        img 20205
                        with Dissolve(0.5)
                        w
                        img 20206
                        with diss
                        w
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                #если уже несколько раз
                biff "Но папочке начинает надоедать одно и то же..."
            "Показать обнаженную попу." if shotsAmountCompleted >= shotsTotalAmount:
                $ store_music()
                music Loved_Up
                if castingCloth == 1:
                    if chickMode == True:
                        img 9443
                        with Dissolve(0.5)
                        m "Моника Бакфетт хочет показать папочке свой зад..."
                        img 9444
                        with fade
                        w
                        img 9445
                        with fade
                        w
                        img 9446
                        with Dissolve(0.5)
                        w
                    else:
                        img 9443
                        with Dissolve(0.5)
                        m "Я покажу тебе зад, потому что ты заставил меня..."
                        img 9444
                        with fade
                        w
                        img 9445
                        with fade
                        w
                        img 9446
                        with Dissolve(0.5)
                        w
                if castingCloth == 2:
                    if chickMode == True:
                        sound snd_fabric1
                        img 9447
                        with fade
                        m "Леди Нуар хочет показать папочке свой зад..."
                        img 9448
                        biff "Давай, Леди Нуар! Показывай свои зад!"
                        "Не прячь его от папочки!"
                        img 9452
                        with fade
                        w
                        img 9453
                        with Dissolve(0.5)
                        w
                        img 9454
                        with Dissolve(0.5)
                        w
                        img 9455
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9457
                        with Dissolve(0.5)
                        w
                        img 9458
                        with Dissolve(0.5)
                        w
                    else:
                        sound snd_fabric1
                        img 9449
                        with fade
                        m "Биф, мне обязательно это делать?"
                        img 9450
                        biff "Давай, Леди Нуар! Показывай свои зад!"
                        "Не прячь его от папочки!"
                        "А то я заставлю Леди Нуар показать свой зад на камеру!"
                        img 9451
                        with fade
                        w
                        biff "Я жду!"
                        img 9452
                        with fade

                        img 9453
                        with Dissolve(0.5)
                        w
                        img 9454
                        with Dissolve(0.5)
                        w
                        img 9455
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9457
                        with Dissolve(0.5)
                        w
                        img 9458
                        with Dissolve(0.5)
                        w
                if castingCloth == 3:
                    if chickMode == True:
                        img 9459
                        with fade
                        m "Девушка с календаря хочет показать папочке свою попу..."
                        img 9460
                        biff "Давай! Девушка с календаря!"
                        "Показывай свой зад!"
                        img 9464
                        with fade
                        w
                        sound snd_fabric1
                        img 9465
                        with Dissolve(0.5)
                        w
                        m "На, смотри..."
                        img 9466
                        with Dissolve(0.5)
                        w
                        img 9467
                        with Dissolve(0.5)
                        w
                        img 9468
                        with Dissolve(0.5)
                        w
                        img 9469
                        with Dissolve(0.5)
                        w
                    else:
                        img 9461
                        with fade
                        m "Я знаю, я должна показать тебе свой зад..."
                        "Но можно я не буду делать этого?"
                        img 9462
                        biff "Давай! Девушка с календаря!"
                        "Показывай свой зад!"
                        "Иначе я скажу Алексу чтобы этот голый зад смотрел на всех прямо с календаря!"
                        img 9463
                        biff "Ну же! Зад!"
                        img 9464
                        with fade
                        w
                        sound snd_fabric1
                        img 9465
                        with Dissolve(0.5)
                        w
                        m "На, смотри..."
                        img 9466
                        with Dissolve(0.5)
                        w
                        img 9467
                        with Dissolve(0.5)
                        w
                        img 9468
                        with Dissolve(0.5)
                        w
                        img 9469
                        with Dissolve(0.5)
                        "Мне не нужны проблемы..."
                if castingCloth == 4:
                    if chickMode == True:
                        img 9485
                        with fade
                        sound snd_fabric1
                        m "Роза надежды хочет показать папочке свой зад..."
                        img 9486
                        biff "Давай, Роза!"
                        "Показывай свой зад!"

                        img 9487
                        with Dissolve(0.5)
                        w
                        img 9488
                        with Dissolve(0.5)
                        w
                        img 9489
                        with Dissolve(0.5)
                        w
                        img 9490
                        with Dissolve(0.5)
                        w
                        img 9491
                        with Dissolve(0.5)
                        w
                        img 9492
                        with Dissolve(0.5)
                        w
                    else:
                        img 9484
                        with fade
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
                        img 9486
                        biff "Давай, Роза!"
                        "Показывай свой зад!"

                        img 9487
                        with Dissolve(0.5)
                        w
                        img 9488
                        with Dissolve(0.5)
                        w
                        img 9489
                        with Dissolve(0.5)
                        w
                        img 9490
                        with Dissolve(0.5)
                        w
                        img 9491
                        with Dissolve(0.5)
                        w
                        img 9492
                        with Dissolve(0.5)
                        w
                if castingCloth == 5:
                    if chickMode == True:
                        img 9506
                        with fade
                        sound snd_fabric1
                        m "Стюардесса Fashion Airlines хочет показать папочке свой зад..."
                        img 9507
                        biff "Давай, Стюардесса!"
                        "Показывай свой зад!"
                        img 9508
                        with fade

                        img 9509
                        with Dissolve(0.5)
                        w
                        img 9510
                        with Dissolve(0.5)
                        w
                        img 9511
                        with Dissolve(0.5)
                        w
                        img 9512
                        with Dissolve(0.5)
                        w
                        img 9513
                        with Dissolve(0.5)
                        w
                        img 9514
                        with Dissolve(0.5)
                        w
                    else:
                        img 9505
                        with fade
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
                        img 9507
                        biff "Давай, Стюардесса!"
                        "Показывай свой зад!"
                        img 9508
                        with fade

                        img 9509
                        with Dissolve(0.5)
                        w
                        img 9510
                        with Dissolve(0.5)
                        w
                        img 9511
                        with Dissolve(0.5)
                        w
                        img 9512
                        with Dissolve(0.5)
                        w
                        img 9513
                        with Dissolve(0.5)
                        w
                        img 9514
                        with Dissolve(0.5)
                        w
                if castingCloth == 6:
                    if chickMode == True:
                        img 20188 #9506
                        with fade
                        sound snd_fabric1
                        m "Алая Жемчужина хочет показать папочке свой зад..."
#                        img 9507
                        biff "Давай, Жемчужина!"
                        "Показывай свой зад!"
                        img 20189 #9508
                        with fade
                        m "Биф, можно Я не буду снимать костюм?"
                        m "Это долго..."

                        img 20190
                        with fade
                        biff "Хорошо, цыпочка."
                        biff "У папочки нет времени на переодевания."

                        img 20191
                        biff "Пусть цыпочка сядет на стол."
                        biff "Папочка хочет посмотреть на сидящую цыпочку."

                        img 20192
                        with diss
                        m "Так, Биф?"
                        img 20193
                        biff "Да, цыпочка. Привыкай сидеть на жердочке."
                        biff "Скоро ты займешь место рядом с малышкой Мелани!"

                        img 20194
                        mt "!!!"

                    else:
                        img 20188 #9506
                        with fade
                        sound snd_fabric1
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
#                        img 9507
                        biff "Давай, Жемчужина!"
                        "Показывай свой зад!"
                        img 20189 #9508
                        with fade
                        m "Биф, можно Я не буду снимать костюм?"
                        m "Это долго..."

                        img 20190
                        with fade
                        biff "Хорошо, цыпочка."
                        biff "У папочки нет времени на переодевания."

                        img 20191
                        biff "Пусть цыпочка сядет на стол."
                        biff "Папочка хочет посмотреть на сидящую цыпочку."

                        img 20192
                        with diss
                        m "Так, Биф?"
                        img 20193
                        biff "Да, цыпочка. Привыкай сидеть на жердочке."
                        biff "Скоро ты займешь место рядом с малышкой Мелани!"

                        img 20194
                        mt "!!!"
                if castingCloth == 7:
                    if chickMode == True:
                        img 20207
                        with fade
                        sound snd_fabric1
                        m "Запретное Желание хочет показать папочке свой зад..."
                        img 20208
                        with diss
                        biff "Давай, Запретное Желание!"
                        "Показывай свой зад!"
                        img 20209
                        with fade
                        w

                        img 20210
                        with Dissolve(0.5)
                        w
                        img 20211
                        with Dissolve(0.5)
                        w
                        img 20212
                        with Dissolve(0.5)
                        w
                    else:
                        img 20207
                        with fade
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
                        img 20208
                        biff "Давай, Запретное Желание!"
                        "Показывай свой зад!"
                        img 20209
                        with fade
                        w

                        img 20210
                        with Dissolve(0.5)
                        w
                        img 20211
                        with Dissolve(0.5)
                        w
                        img 20212
                        with Dissolve(0.5)
                        w
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                #если уже несколько раз
#                biff "Но папочке начинает надоедать одно и то же..."
            "Показать обнаженную попу. (фотосессия не завершена) (disabled)" if shotsAmountCompleted < shotsTotalAmount:
                pass
            "Раздеться и принимать различные модельные позы." if char_info["Biff"]["level"] >= 2 and biffLevel3Opened == True:
                $ store_music()
                call ep210_dialogues1_office_biff_1a() from _rcall_ep210_dialogues1_office_biff_1a
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                if biffCastingStage < 1:
                    $ biffCastingStage = 1
                if char_info["Biff"]["level"] <= 2:
                    $ add_char_progress("Biff", biffFlashCardQuestReportPose1, "biffFlashCardQuestReportPose1" + str(day))
            "Раздеться и принимать различные модельные позы. (требуется ур.2) (disabled)" if char_info["Biff"]["level"] < 2 or biffLevel3Opened != True:
                pass
            "Раздеться и встать на колени задом к Бифу." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 1:
                $ store_music()
                call ep210_dialogues1_office_biff_1b() from _rcall_ep210_dialogues1_office_biff_1b
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                if biffCastingStage < 2:
                    $ biffCastingStage = 2
                if char_info["Biff"]["level"] <= 2:
                    $ add_char_progress("Biff", biffFlashCardQuestReportPose2, "biffFlashCardQuestReportPose2" + str(day))
            "Раздеться и встать на колени задом к Бифу. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 1:
                pass
            "Раздеться и лечь на пол раздвинув ноги." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 2:
                $ store_music()
                call ep210_dialogues1_office_biff_1c() from _rcall_ep210_dialogues1_office_biff_1c
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                if biffCastingStage < 3:
                    $ biffCastingStage = 3
                if char_info["Biff"]["level"] <= 2:
                    $ add_char_progress("Biff", biffFlashCardQuestReportPose3, "biffFlashCardQuestReportPose3" + str(day))
            "Раздеться и лечь на пол раздвинув ноги. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 2:
                pass
            "Раздеться и сесть на стол.":
                $ menu_corruption = [biffCastingOneLegOnTheTable, biffCastingTableLegsOpen, biffCastingTableBack, biffCastingTableBlowjob]
                menu:
                    "Поставить на стол одну ногу." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 3:
                        $ store_music()
                        call ep212_dialogues7_biff1() from _rcall_ep212_dialogues7_biff1
                        $ restore_music()
                        img 8445
                        biff "Хорошо, папочка доволен!"
                        if biffCastingStage < 4:
                            $ biffCastingStage = 4
                        if char_info["Biff"]["level"] <= 2:
                            $ add_char_progress("Biff", biffFlashCardQuestReportPose4, "biffFlashCardQuestReportPose4" + str(day))

                    "Поставить на стол одну ногу. (disabled)" if char_info["Biff"]["level"] < 2 and biffCastingStage < 3:
                        pass
                    "Сесть на стол лицом к Бифу, широко раздвинув ноги." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 4:
                        $ store_music()
                        call ep212_dialogues7_biff2() from _rcall_ep212_dialogues7_biff2
                        $ restore_music()
                        img 8445
                        biff "Хорошо, папочка доволен!"
                        if biffCastingStage < 5:
                            $ biffCastingStage = 5
                        if char_info["Biff"]["level"] <= 2:
                            $ add_char_progress("Biff", biffFlashCardQuestReportPose5, "biffFlashCardQuestReportPose5" + str(day))
                    "Сесть на стол лицом к Бифу, широко раздвинув ноги. (disabled)" if char_info["Biff"]["level"] < 2 and biffCastingStage < 4:
                        pass
                    "Сесть на стол спиной к Бифу." if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 5 and monicaOutfitsEnabled[9] == True:
                        $ store_music()
                        call ep216_dialogues0_biff1() from _rcall_ep216_dialogues0_biff1
                        $ restore_music()
                        if biffCastingStage < 6:
                            $ biffCastingStage = 6
                        if char_info["Biff"]["level"] <= 3:
                            $ add_char_progress("Biff", 50, "ep216_dialogues0_biff1" + str(day))
                    "Сесть на стол спиной к Бифу. (disabled)"  if char_info["Biff"]["level"] < 2 or biffCastingStage < 5 or monicaOutfitsEnabled[9] != True:
                        pass
                    "Сесть на стол, достать член Бифа и взять его в рот."  if char_info["Biff"]["level"] >= 2 and biffCastingStage >= 6 and monicaOutfitsEnabled[9] == True:
                        $ store_music()
                        call ep216_dialogues0_biff2() from _rcall_ep216_dialogues0_biff2
                        $ restore_music()
                        if _return == -1: # убежала, закрываем доступ в офис на неделю
                            call ep216_quests_biff_block_office() from _rcall_ep216_quests_biff_block_office
                            return -1
                        if biffCastingStage < 7:
                            $ biffCastingStage = 7
                        if char_info["Biff"]["level"] <= 3:
                            $ add_char_progress("Biff", 50, "ep216_dialogues0_biff2" + str(day))
                    "Сесть на стол, достать член Бифа и взять его в рот. (disabled)" if char_info["Biff"]["level"] < 2 or biffCastingStage < 6 or monicaOutfitsEnabled[9] != True:
                        pass
                    "Сесть на стол. достать член Бифа и возить им по киске. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и вставить его в свою киску. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и вставить его в анальное отверстие. (disabled)":
                        pass
                    "Назад.":
                        jump ep22_dialogue6_6_loop1
            "Раздеться и сесть на Бифа.":
                menu:
                    "Сесть к Бифу на коленки лицом к нему. (disabled)":
                        pass
                    "Сесть к Бифу на коленки спиной. (disabled)":
                        pass
                    "Сесть Бифу киской на лицо. (disabled)":
                        pass
                    "Достать член Бифа и сесть на него лицом к Бифу (disabled)":
                        pass
                    "Достать член Бифа и сесть на него спиной к Бифу (disabled)":
                        pass
                    "Достать член Бифа и сесть на него анальным отверстием (disabled)":
                        pass
                    "Полизать папочке зад. (disabled)":
                        pass
                    "Назад.":
                        jump ep22_dialogue6_6_loop1
            "Позвать секретаршу.":
                label ep22_dialogue6_6_loop2:
                    menu:
                        "Поцеловать секретаршу. (disabled)":
                            pass
                        "Полизать секретарше грудь. (disabled)":
                            pass
                        "Полизать секретарше киску. (disabled)":
                            pass
                        "Засунуть секретарше язык глубоко в анальное отверстие. (disabled)":
                            pass
                        "Достать член Бифа и засунуть его в секретаршу. (disabled)":
                            pass
                        "Засунуть член в ее киску, затем вытащить и облизать его. (disabled)":
                            pass
                        "Засунуть член в ее анальное отверстие, затем вытащить и облизать его. (disabled)":
                            pass
#                        "Назад.":
#                                jump ep22_dialogue6_6_loop2
                        "Назад.":
                            jump ep22_dialogue6_6_loop1
    return
