label intro_questions:
    img 1201
    with fade
    help "Прежде чем начать игру, пожалуйста, напомните, как вела себя Моника в Эпизоде 1?"
    menu:
        "Ответить очень кратко.":
            call intro_questions_short() from _call_intro_questions_short
            img 3367
            with fade
            help "Спасибо за ответ!"
        "Ответить очень подробно.":
            call intro_questions_long() from _call_intro_questions_long
            img 3367
            with fade
            help "Спасибо за ответы!"
    help "Последний вопрос. В чем Моника легла спать?"
    label .into_loop1:
        menu:
            "Моника легла спать в трусиках Юлии.":
                $ cloth_type = "Nude"
                $ cloth = "GovernessPants"

            "Моника легла спать обнаженной (доступно только в сохранении Эпизода 1) (disabled)":
                jump .intro_loop1
    img black_screen
    with Dissolve(1.0)
#    pause(1.0)
    return

label intro_questions_save:
    img 3370
    with fadelong
    help "В чем Моника легла спать?"
    menu:
        "Моника легла спать в трусиках Юлии.":
            $ cloth_type = "Nude"
            $ cloth = "GovernessPants"

        "Моника легла спать обнаженной.":
            $ cloth_type = "Nude"
            $ cloth = "Nude"
    img black_screen
    with Dissolve(1.0)
#    pause(1.0)
    return

label intro_questions_long:
    img 1105
    with fade
    menu:
        "Моника общалась с соседом.":
            $ neighborAsked = True
            $ neighborCalled = True
            $ set_active("Teleport_Fence", True, scene="street_house_main_yard")
            menu:
                "Моника поздоровалась с соседом.":
                    call bitch(-2, "neighbor_dial1") from _call_bitch_8

                "Моника не стала здороваться.":
                    call bitch(2, "neighbor_dial1") from _call_bitch_9
                    $ neighborOffended1 = True

            menu:
                "Монике было все-равно что сосед чуть не погиб.":
                    $ neighborOffended2 = True
                    call bitch(2, "neighbor_dial2") from _call_bitch_10
                "Моника проявила обеспокоенность.":
                    call bitch(-2, "neighbor_dial2") from _call_bitch_11
            menu:
                "Моника сказала что сосед грязный.":
                    call bitch(2, "neighbor_dial3") from _call_bitch_12
                    $ neighborOffended3 = True
                "Нет.":
                    call bitch(-2, "neighbor_dial3") from _call_bitch_13

            menu:
                "Ох ничего себе! Он сломал мне забор!":
                    call bitch(5, "neighbor_dial4") from _call_bitch_14
                    $ neighborOffended4 = True
                "Эту царапину еле видно! Из-за чего весь шум?":
                    call bitch(-5, "neighbor_dial4") from _call_bitch_15
            menu:
                "Моника прогнала соседа.":
                    $ neighborOffended5 = True
                "Моника закатила соседу большой иск.":
                    call bitch(10, "neighbor_suebig") from _call_bitch_16
                    $ neighborOffendedSue = True
                    $ neighborOffendedSueBig = True
                    menu:
                        "Моника высказалась по поводу фермы соседа.":
                            $ neighborOffendedFarm = True
                            call bitch(3, "neighbor_offendfarm") from _call_bitch_17
                        "Нет.":
                            pass
                "Моника решила отсудить маленькую сумму.":
                    $ neighborOffendedSue = True

        "Моника не видела соседа.":
            pass

    img 1035
    with fade
    menu:
        "Моника обращается с Юлией криком":
            $ juliaMonicaYell = True
            call bitch(5, "call_julia1") from _call_bitch_18
        "Моника общается более вежливо.":
            call bitch(-5, "call_julia1") from _call_bitch_19

    img 1080
    with fade
    menu:
        "Юлия наказана и убирает пятно все время.":
            $ juliaPunished = True
            call bitch(10, "monica_julia_revenge_punished") from _call_bitch_20
            menu:
                "Моника простила Юлию после строгого наказания.":
                    $ juliaMonicaForgivenessAfterPunishment = True
                    call bitch(-20, "juliaMonicaForgivenessAfterPunishment") from _call_bitch_21
                "Нет.":
                    pass
        "Юлия наказана криком, но пятно можно не убирать.":
            call bitch(-10, "monica_julia_revenge_punished") from _call_bitch_22
            $ juliaPunishedLow = True
        "Юлия наказана и убирает пятно в свободное время.":
            $ juliaPunishedVoluntarily = True
            call bitch(5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_23
        "Юлию не наказана за пятно никак.":
            $ juliaPunishedNone = True
            call bitch(-10, "monica_julia_revenge_punished") from _call_bitch_24
            call bitch(-5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_25

    menu:
        "Моника соврала про то что пятно поставила Юлия, а не Моника.":
            $ juliaMonicaLied = True
            call bitch(5, "monica_julia_revenge_lie") from _call_bitch_26
        "Моника сказала правду про пятно.":
            pass

    img 4082
    with fade
    menu:
        "Юлии пришлось заняться сексом со Фредом.":
            $ juliaHasSexInPool = True
            img 4090
            with fade
            menu:
                "Юлия не стала говорить Фреду что секс ей не понравился.":
                    $ juliaBasementSexLiked = True
                "Юлия взывала к совести Фреда.":
                    pass
        "Юлия не решилась на это...":
            pass

    img 1328
    with fade
    menu:
        "Моника сказала Стиву по телефону что он мешок с дерьмом.":
            $ steveOffended1 = True
            call bitch(2, "steve_offended1") from _call_bitch_27
        "Нет.":
            pass

    img 1198
    with fade
    menu:
        "Моника обозвала моделей мартышками.":
            $ monkeysOffended1 = True
            call bitch(2, "monkeys_offend1") from _call_bitch_28
        "Моника повела себя вежливо.":
            call bitch(-8, "monkeys_offend1") from _call_bitch_29

    menu:
        "Моника заставила моделей полностью раздеться.":
            $ monkeysOffended2 = True
            $ monkeysOffended3 = True
            call bitch(2, "monkeys_offend2") from _call_bitch_30
            call bitch(8, "monkeys_offend3") from _call_bitch_31
        "Моника не стала издеваться на моделями.":
            pass

    img 1299
    with fade
    menu:
        "Моника показала моделям фотосессию Мелани.":
            $ melaniePhotoShotProcessed = True
            menu:
                "Моника накричала на моделей после фотосессии.":
                    $ monkeysOffended4 = True
                    call bitch(2, "monkeys_offend4") from _call_bitch_32
                "Моника вежливо отказала.":
                    pass
        "Моника сказала моделям уйти.":
            pass
    img 1880
    with fade
    menu:
        "Моника смеялась над моделью, когда увидела ее работающей проституткой.":
            $ grayMouse2WhoreOffended = True
            call bitch(8, "dress_return_whore1") from _call_bitch_33
        "Моника не стала смеяться над ней.":
            pass

    img 1308
    with fade
    menu:
        "Моника сказала Мелани, чтобы та следила за своей фигурой, иначе может уволить ее.":
            $ melanieOffended1 = True
            call bitch(2, "melanie_offended1") from _call_bitch_34
        "Моника похвалила Мелани.":
            call bitch(-2, "melanie_offended1") from _call_bitch_35

    menu:
        "Моника сказала Алексу, что он будет уволен если продолжит брать пикантные ракурсы.":
            $ alexPhotographOffended1 = True
            call bitch(2, "alexphotograph_offended1") from _call_bitch_36
        "Моника попросила Алекса войти в ее положение.":
            call bitch(-2, "alexphotograph_offended1") from _call_bitch_37


    img 1328
    with fade
    menu:
        "Моника сказала Дику что вокруг одни идиоты.":
            call bitch(2, "dick_phone_call1_dial1") from _call_bitch_38
            $ dickMonicaIdiotsAround = True
        "Моника сказала Дику что она самостоятельная.":
            call bitch(-2, "dick_phone_call1_dial1") from _call_bitch_39


    menu:
        "Моника сказала что не любит общаться с Диком.":
            $ dickMonicaOffended1 = True
            call bitch(2, "dick_phone_call1_dial2") from _call_bitch_40
        "Моника согласилась на встречу.":
            pass


    img black_screen
    imgc 1911
    with fade
    menu:
        "Моника все время ругалась на Фреда.":
            call bitch(1, "fred_monica_office1") from _call_bitch_41
            call bitch(1, "fred_monica_office2") from _call_bitch_42
            call bitch(1, "fred_monica_office3") from _call_bitch_43
            call bitch(1, "fred_monica_office4") from _call_bitch_44
            call bitch(1, "fred_monica_fuel1") from _call_bitch_45
            call bitch(2, "fred_monica_fuel2") from _call_bitch_46
            call bitch(1, "fredOffendedDriveFitness1") from _call_bitch_47
            call bitch(1, "fredOffendedDriveFitness2") from _call_bitch_48
            call bitch(1, "fredOffendedDriveFitness4") from _call_bitch_49
            call bitch(1, "fredOffendedDriveFitness3") from _call_bitch_50

            $ fredOffendedRefuel = True
            $ fredOffendedRefuel2 = True
            $ fredOffendedDriveFitness1 = False # Едут на фитнесс. Фред, ты говоришь как болван.
            $ fredOffendedDriveFitness2 = False # У тебя есть в машине керосин?
            $ fredOffendedDriveFitness3 = False # Почти мне не интересно. Когда приедем, тогда скажи.
            $ fredOffendedDriveFitness4 = False # Продолжить задирать Фреда
            $ fredOffendedDriveReturnDress1 = False # И в этом другом мире нет всех этих нищих! Ты зеленый помидор, раздавленный на дороге!
        "Моника иногда ругалась на Фреда.":
            call bitch(1, "fred_monica_office4") from _call_bitch_51
            call bitch(1, "fred_monica_fuel1") from _call_bitch_52
            call bitch(2, "fred_monica_fuel2") from _call_bitch_53
            call bitch(1, "fredOffendedDriveFitness1") from _call_bitch_54
            call bitch(1, "fredOffendedDriveFitness2") from _call_bitch_55
            $ fredOffendedRefuel = True
            $ fredOffendedDriveFitness1 = False # Едут на фитнесс. Фред, ты говоришь как болван.
            $ fredOffendedDriveFitness2 = False # У тебя есть в машине керосин?
        "Моника не ругалась на Фреда никогда.":
            pass

    img Gas_Station_Monica_OilTrader_18
    with fade
    menu:
        "Моника позвала продавщицу на заправке.":
            $ gasStationSaleswomanCalledOut = True
            call bitch(-10, "gas_saleswoman_decision") from _call_bitch_56
        "Моника разбила бутылку, чтобы привлечь внимание.":
            $ gasStationSaleswomanMischiefed = True
            $ gasStationSaleswomanAlmostCummed = True
            call bitch(7, "gas_saleswoman_decision") from _call_bitch_57
            menu:
                "Моника обвинила в этом кассиршу.":
                    $ gasStationMonicaLied = True
                    call bitch(10, "gas_station_monicalied") from _call_bitch_58
                "Моника согласилась возместить ущерб.":
                    call bitch(-5, "gas_station_monicalied") from _call_bitch_59


    img 1394
    with fade
    menu:
        "Моника при покупке платья общалась в продавцом грубо":
            $ clothShopCashierOffended2 = True
            call bitch(2, "clothShopCashierOffended2") from _call_bitch_60
        "Вежливо.":
            call bitch(-2, "clothShopCashierOffended2") from _call_bitch_61

    menu:
        "Моника заплатила за платье сама.":
            $ dressMonicaPaid = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3") from _call_bitch_62
            $ dickClothShopOffended3 = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3") from _call_bitch_63
        "За платье заплатил Дик.":
            pass
    menu:
        "Моника грубила когда возвращала платье.":
            $ clothShopCashierOffended3ReturnDress = True
            call bitch(3, "clothShopCashierOffended3ReturnDress") from _call_bitch_64
        "Моника общалась вежливо.":
            call bitch(-3, "clothShopCashierOffended3ReturnDress") from _call_bitch_65

    img 5640
    with fade
    menu:
        "Моника ругалась на продавца когда та застала ее утром в примерочной":
            $ clothShopCashierFirstNightOffended = True
            call bitch(5, "clothShopCashierFirstNightOffended") from _call_bitch_66
        "Моника выкрутилась за счет вежливости.":
            call bitch(-5, "clothShopCashierFirstNightOffended") from _call_bitch_67

    img 1437
    with fade
    menu:
        "Моника ругалась на Дика в машине и не стала подвозить его.":
            $ dickDriveDialOffend1 = True
            call bitch(1, "dickDriveDialOffend1") from _call_bitch_68
            $ dickCarKickedOut = True
            call bitch(5, "dickCarKickedOut") from _call_bitch_69
            $ dickDriveRestaurantOffended1 = True
            call bitch(1, "dickDriveRestaurantOffended1") from _call_bitch_70
        "Моника общалась с Диком мило.":
            call bitch(-2, "dickCarKickedOut") from _call_bitch_71

    menu:
        "Моника сказала Дику что он уродливый.":
            $ dickClothShopOffended1 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue1") from _call_bitch_72
            $ dickClothShopOffended2 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue2") from _call_bitch_73
        "Моника только пошутила насчет галстука.":
            pass

    menu:
        "Моника назвала Дика плюшевым мишкой и сказала что он смешной.":
            $ dickClothShopOffended4 = True
            call bitch(1, "dickClothShopOffended4") from _call_bitch_74
            $ richHotelRestaurantDickOffended1ChoiceMade = True
            call bitch(5, "richHotelRestaurantDickOffended1") from _call_bitch_75
        "Моника назвала Дика кавалером.":
            call bitch(-1, "dickClothShopOffended4") from _call_bitch_76

    img 1427
    menu:
        "Дик собирается помочь подать иск на соседа.":
            $ dickHelpsMoniceSue = True
        "Нет.":
            pass


    menu:
        "Дик проговорился что хочет Мелани.":
            $ richHotelRestaurantDickOffended1 = True
            $ dickWantFuckMelanie = True
        "Нет.":
            pass

    menu:
        "Моника ругалась на официантку и сказала Дику ее уволить.":
            $ waitressMonicaOffended1 = True
            call bitch(3, "waitressMonicaOffended1") from _call_bitch_77
            $ waitressMonicaFired = True
            call bitch(5, "waitressMonicaFired") from _call_bitch_78
        "Моника попросила Дика оставить официантке чаевые.":
            call bitch(-3, "waitressMonicaOffended1") from _call_bitch_79
            $ waitressMonicaTips = True
            call bitch(-5, "waitressMonicaTips") from _call_bitch_80


    menu:
        "Моника сказала Фреду что Дик жирный урод.":
            call bitch(1, "dickMonicaSaidToFredOffend") from _call_bitch_81
            $ dickMonicaSaidToFredOffend = True
        "Моника сказала Фреду что Дик старался угодить ей.":
            call bitch(-1, "dickMonicaSaidToFredOffend") from _call_bitch_82


    if bitchmeterValue > maxBitchness_EP1 / 2:
        img 4591
        with fade
        menu:
            "У Фреда был секс с Кристиной.":
                $ christineFuckedByFred = True
                img 4621
                with fade
                menu:
                    "У Фреда с Кристиной был миньет и анал.":
                        $ christineFuckedByFredBlowjob = True
                        $ christineFuckedByFredAnal = True
                    "Кристина не выдержала и убежала.":
                        pass
            "Нет.":
                pass

    img 1646
    with fade
    menu:
        "Моника грубо отшила инструктора по фитнесу":
            call bitch(1, "fitness_trainer1") from _call_bitch_83
            $ fitness1_trainer_talk2_choice_rough = True
        "Вежливо отказала.":
            call bitch(-1, "fitness_trainer1") from _call_bitch_84
    img 4757
    menu:
        "У Stephanie был секс с инструктором":
            $ stephanieFitnessJustSex = True
        "Нет.":
            pass

    img 1667
    with fade
    menu:
        "Моника ругалась на клерка в банке.":
            $ clerksOffended = True
            call bitch(2, "bank_office1") from _call_bitch_85
        "Моника вошла в положение.":
            call bitch(-2, "bank_office1") from _call_bitch_86

    img 1822
    with fade
    menu:
        "Моника сказала Стиву что он отсосет у собаки если соврал.":
            $ monicaSteveDogOffended = True
            call bitch(4, "steve_dog_offend") from _call_bitch_87
        "Моника не стала такого говорить.":
            pass

    img 1901
    with fade
    menu:
        "Моника назвала продавца кебабов животным.":
            call bitch(2, "shawarmaTraderOffended1") from _call_bitch_88
            $ shawarmaTraderOffended1 = True
        "Моника не стала его так называть.":
            call bitch(-1, "shawarmaTraderOffended1") from _call_bitch_89

    img 1974
    with fade
    menu:
        "Моника решила уволить Юлию":
            $ juliaFirePlanned = True
            call bitch(5, "juliaFirePlanned") from _call_bitch_90
            menu:
                "Моника в итоге пожалела Юлию и не стала увольнять ее":
                    $ juliaFireCancelled = True
                    call bitch(-3, "julia_firing") from _call_bitch_91
                "Уволила.":
                    pass

        "Нет.":
            call bitch(-5, "juliaFirePlanned") from _call_bitch_92

    menu:
        "Моника запланировала уволить Тиффани и Джейн":
            $ janeTiffanyFirePlanned = True
            call bitch(5, "janeTiffanyFirePlanned") from _call_bitch_93
        "Моника решила еще проследить за ними.":
            call bitch(-5, "janeTiffanyFirePlanned") from _call_bitch_94


    menu:
        "Моника запланировала уволить Фреда":
            $ fredFirePlanned = True
            call bitch(5, "fredFirePlanned") from _call_bitch_95
        "Моника решила еще подумать над этим.":
            call bitch(-5, "fredFirePlanned") from _call_bitch_96


    if bitchmeterValue <= maxBitchness_EP1 / 2:
        img 5176
        with fade
        menu:
            "Моника показывала Бобу грудь за еду.":
                $ jailBoobsForFoodShowed = True
            "Моника показала грудь заключенным, чтобы узнать имя Боба":
                $ jailCageShowedBoobsForBobName = True

    img 5338
    with fade
    menu:
        "Монике пришлось показать заключенным грудь во время шантажа.":
            $ jailCageBlackmailBoobsShowed = True
            img 5406
            with fade
            menu:
                "Монике пришлось также показать заключенным зад.":
                    $ jailCageBlackmailAssShowed = True
                    img 5412
                    with fade
                    menu:
                        "Монику заставили сказать что она хорошая шлюха.":
                            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
                        "Моника отказалась это говорить.":
                            pass
                "Моника поставила заключенных на место.":
                    pass

        "Моника поставила заключенных на место.":
            pass

    img 3114
    with fade
    menu:
        "Моника накричала на Дика в его кабинете.":
            $ dickMonicaCabinetOffended = True
            call bitch(2, "dickMonicaCabinetOffended") from _call_bitch_97
        "Моника пробовала уговорить Дика.":
            call bitch(-1, "dickMonicaCabinetOffended") from _call_bitch_98

    img 5900
    with fade
    menu:
        "Моника делала миньет Фреду.":
            $ monicaFredWasForcedBlowjob = True
            img 5904
            with fade
            menu:
                "Моника проглотила сперму Фреда.":
                    $ monicaFredWasSpermEat = True
                "Моника выплюнула сперму Фреда.":
                    pass
        "Моника обошлась без миньета.":
            pass


    return

label intro_questions_short:
    img 1200
    with fade
    menu:
        "Моника вела себя как сучка!":
            $ neighborAsked = True
            $ neighborCalled = True
            $ neighborOffended1 = True
            call bitch(2, "neighbor_dial1") from _call_bitch_99
            $ neighborOffended2 = True
            call bitch(2, "neighbor_dial2") from _call_bitch_100
            $ neighborOffended3 = True
            call bitch(2, "neighbor_dial3") from _call_bitch_101
            $ neighborOffended4 = True
            call bitch(5, "neighbor_dial4") from _call_bitch_102
            call bitch(10, "neighbor_suebig") from _call_bitch_103
            $ neighborOffendedSue = True
            $ neighborOffendedSueBig = True
            $ neighborOffendedFarm = True

            call bitch(3, "neighbor_offendfarm") from _call_bitch_104
            $ juliaMonicaYell = True
            call bitch(5, "call_julia1") from _call_bitch_105
            $ juliaPunished = True
            call bitch(10, "monica_julia_revenge_punished") from _call_bitch_106
            $ juliaMonicaLied = True
            call bitch(5, "monica_julia_revenge_lie") from _call_bitch_107
            $ juliaHasSexInPool = True
            $ juliaBasementSexLiked = True
            $ steveOffended1 = True
            call bitch(2, "steve_offended1") from _call_bitch_108
            $ monkeysOffended1 = True
            call bitch(2, "monkeys_offend1") from _call_bitch_109
            $ monkeysOffended2 = True
            $ monkeysOffended3 = True
            call bitch(2, "monkeys_offend2") from _call_bitch_110
            call bitch(8, "monkeys_offend3") from _call_bitch_111
            $ melaniePhotoShotProcessed = True
            $ monkeysOffended4 = True
            call bitch(2, "monkeys_offend4") from _call_bitch_112
            $ grayMouse2WhoreOffended = True
            call bitch(8, "dress_return_whore1") from _call_bitch_113
            $ melanieOffended1 = True
            call bitch(2, "melanie_offended1") from _call_bitch_114
            $ alexPhotographOffended1 = True
            call bitch(2, "alexphotograph_offended1") from _call_bitch_115
            call bitch(2, "dick_phone_call1_dial1") from _call_bitch_116
            $ dickMonicaIdiotsAround = True
            $ dickMonicaOffended1 = True
            call bitch(2, "dick_phone_call1_dial2") from _call_bitch_117
            call bitch(1, "fred_monica_office1") from _call_bitch_118
            call bitch(1, "fred_monica_office2") from _call_bitch_119
            call bitch(1, "fred_monica_office3") from _call_bitch_120
            call bitch(1, "fred_monica_office4") from _call_bitch_121
            call bitch(1, "fred_monica_fuel1") from _call_bitch_122
            call bitch(2, "fred_monica_fuel2") from _call_bitch_123
            call bitch(1, "fredOffendedDriveFitness1") from _call_bitch_124
            call bitch(1, "fredOffendedDriveFitness2") from _call_bitch_125
            call bitch(1, "fredOffendedDriveFitness4") from _call_bitch_126
            call bitch(1, "fredOffendedDriveFitness3") from _call_bitch_127

            $ fredOffendedRefuel = True
            $ fredOffendedRefuel2 = True
            $ fredOffendedDriveFitness1 = False # Едут на фитнесс. Фред, ты говоришь как болван.
            $ fredOffendedDriveFitness2 = False # У тебя есть в машине керосин?
            $ fredOffendedDriveFitness3 = False # Почти мне не интересно. Когда приедем, тогда скажи.
            $ fredOffendedDriveFitness4 = False # Продолжить задирать Фреда
            $ fredOffendedDriveReturnDress1 = False # И в этом другом мире нет всех этих нищих! Ты зеленый помидор, раздавленный на дороге!
            $ gasStationSaleswomanMischiefed = True
            $ gasStationSaleswomanAlmostCummed = True
            call bitch(7, "gas_saleswoman_decision") from _call_bitch_128
            call bitch(10, "gas_station_monicalied") from _call_bitch_129
            $ gasStationMonicaLied = True
            $ clothShopCashierOffended2 = True
            call bitch(2, "clothShopCashierOffended2") from _call_bitch_130
            $ dressMonicaPaid = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3") from _call_bitch_131
            $ dickClothShopOffended3 = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3") from _call_bitch_132
            $ clothShopCashierOffended3ReturnDress = True
            call bitch(3, "clothShopCashierOffended3ReturnDress") from _call_bitch_133
            $ clothShopCashierFirstNightOffended = True
            call bitch(5, "clothShopCashierFirstNightOffended") from _call_bitch_134
            $ dickDriveDialOffend1 = True
            call bitch(1, "dickDriveDialOffend1") from _call_bitch_135
            $ dickCarKickedOut = True
            call bitch(5, "dickCarKickedOut") from _call_bitch_136
            $ dickDriveRestaurantOffended1 = True
            call bitch(1, "dickDriveRestaurantOffended1") from _call_bitch_137
            $ dickClothShopOffended1 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue1") from _call_bitch_138
            $ dickClothShopOffended2 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue2") from _call_bitch_139
            $ dickClothShopOffended4 = True
            call bitch(1, "dickClothShopOffended4") from _call_bitch_140
            $ richHotelRestaurantDickOffended1ChoiceMade = True
            call bitch(5, "richHotelRestaurantDickOffended1") from _call_bitch_141
            $ dickHelpsMoniceSue = True
            $ richHotelRestaurantDickOffended1 = True
            $ waitressMonicaOffended1 = True
            call bitch(3, "waitressMonicaOffended1") from _call_bitch_142
            $ waitressMonicaFired = True
            call bitch(5, "waitressMonicaFired") from _call_bitch_143
            call bitch(1, "dickMonicaSaidToFredOffend") from _call_bitch_144
            $ dickMonicaSaidToFredOffend = True
            $ christineFuckedByFred = True
            $ christineFuckedByFredBlowjob = True
            $ christineFuckedByFredAnal = True
            call bitch(1, "fitness_trainer1") from _call_bitch_145
            $ fitness1_trainer_talk2_choice_rough = True
            $ stephanieFitnessJustSex = True
            $ clerksOffended = True
            call bitch(2, "bank_office1") from _call_bitch_146
            $ monicaSteveDogOffended = True
            call bitch(4, "steve_dog_offend") from _call_bitch_147
            $ juliaFirePlanned = True
            call bitch(5, "juliaFirePlanned") from _call_bitch_148
            $ janeTiffanyFirePlanned = True
            call bitch(5, "janeTiffanyFirePlanned") from _call_bitch_149
            $ fredFirePlanned = True
            call bitch(5, "fredFirePlanned") from _call_bitch_150
            $ jailCageBlackmailBoobsShowed = True
            $ jailCageBlackmailAssShowed = True
            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
            $ dickMonicaCabinetOffended = True
            call bitch(2, "dickMonicaCabinetOffended") from _call_bitch_151
            $ monicaFredWasForcedBlowjob = True
            $ monicaFredWasSpermEat = True
            $ shawarmaTraderOffended1 = True
        "Моника старалась быть вежливой насколько умеет...":
            $ neighborAsked = True
            $ neighborCalled = True
            call bitch(-2, "neighbor_dial1") from _call_bitch_152
            call bitch(-2, "neighbor_dial2") from _call_bitch_153
            call bitch(-2, "neighbor_dial3") from _call_bitch_154
            call bitch(-5, "neighbor_dial4") from _call_bitch_155
            call bitch(-5, "call_julia1") from _call_bitch_156
            $ juliaPunishedNone = True
            call bitch(-10, "monica_julia_revenge_punished") from _call_bitch_157
            call bitch(-5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_158
            $ juliaHasSexInPool = True
            $ juliaBasementSexLiked = True
            call bitch(-8, "monkeys_offend1") from _call_bitch_159
            $ melaniePhotoShotProcessed = True
            call bitch(-2, "melanie_offended1") from _call_bitch_160
            call bitch(-2, "alexphotograph_offended1") from _call_bitch_161
            call bitch(-2, "dick_phone_call1_dial1") from _call_bitch_162
            $ gasStationSaleswomanCalledOut = True
            call bitch(-10, "gas_saleswoman_decision") from _call_bitch_163
            call bitch(-2, "clothShopCashierOffended2") from _call_bitch_164
            call bitch(-3, "clothShopCashierOffended3ReturnDress") from _call_bitch_165
            call bitch(-5, "clothShopCashierFirstNightOffended") from _call_bitch_166
            call bitch(-2, "dickCarKickedOut") from _call_bitch_167
            call bitch(-1, "dickClothShopOffended4") from _call_bitch_168
            call bitch(-3, "waitressMonicaOffended1") from _call_bitch_169
            $ waitressMonicaTips = True
            call bitch(-5, "waitressMonicaTips") from _call_bitch_170
            call bitch(-1, "dickMonicaSaidToFredOffend") from _call_bitch_171
            call bitch(-1, "fitness_trainer1") from _call_bitch_172
            $ stephanieFitnessJustSex = True
            call bitch(-2, "bank_office1") from _call_bitch_173
            call bitch(-5, "juliaFirePlanned") from _call_bitch_174
            call bitch(-5, "janeTiffanyFirePlanned") from _call_bitch_175
            call bitch(-5, "fredFirePlanned") from _call_bitch_176
            $ jailBoobsForFoodShowed = True
            $ jailCageShowedBoobsForBobName = True
            $ jailCageBlackmailBoobsShowed = True
            $ jailCageBlackmailAssShowed = True
            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
            call bitch(-1, "dickMonicaCabinetOffended") from _call_bitch_177
            $ monicaFredWasForcedBlowjob = True
            $ monicaFredWasSpermEat = True
    return
