label gallery_5166:
#    if jailDay == 4:
    img 5159
    with fade
    w
    img 5160
    w
    img 5162
    music Loved_up2
    with fadelong
    w
    img 5161
    with fade
    w
    img 5164
    w
    img 5165
    w
    img 5166
    w
    img 5167
    w
#    music Groove2_85
    return

label gallery_5322:
    music Stealth_Groover
    img 5312
    m "Эй вы!"
    img 5110
    prisoner1 "???"
    img 5102
    prisoner5 "???"
    img 5313
    m "Да, вы!"
    "Как зовут этого жир..."
    img 5314
    mt "Черт! Он же может услышать!"
    img 5313
    m "Как зовут нашего надзирателя?"
#                sound prison_yell
    stop music fadeout 1.0
    music prison_yell_music
    img 5112
    prisoner1 "Ребята! Шлюха нас о чем-то спрашивает!"
    "Шлюхе нужна наша помощь!"
    img 5102
    prisoner5 "Да! Поможем ей!"
    img 5101
    prisoner3 "Да! Вгоним свои члены прямо в нее! Да!"
    "Поможем шлюхе!"
    img 5315
    mt "Сволочи!!! НЕНАВИЖУ!!!"
    img 5316
    mt "Моника! Терпение! Это самое большое испытание в твоей жизни!"
    "Справишься - и дальше будет проще!"
    img 5312
    m "Как зовут надзирателя?!?!?!"
    img 5112
    prisoner1 "Шлюхе нужна наша помощь!"
    img 5113
    "Что у шлюх требуют взамен помощи?"
    img 5102
    prisoner5 "Сиськи!"
    img 5100
    prisoner2 "Да! Сиськи!"
    img 5103
    prisoner6 "Сиськи! Сиськи!"
    "Покажи сиськи!"
    img 5099
    prisoner1 "Детка! Покажи сиськи! И мы тебе скажем!"
    img 5101
    prisoner3 "Давай! Ты все-равно их показываешь налево-направо!"
    "Мы же видим!"
    img 5317
    mt "О БОЖЕ!!!"
    "У меня есть выбор."
    "Жуткий выбор, Моника!"
    img 5318
    mt "О БОЖЕ!!!"
    "Показать им свою грудь. Один раз."
    img 5319
    "Или делать это каждый день тому жирному ублюдку."
    "Что же мне делать?"
    menu:
        "Показать грудь в обмен на имя надзирателя.":
            img 5321
            m "Только один раз!"
            img 5322
            "И имя вперед!"
#                        sound prison_yell
            img 5102
            prisoner5 "Сиськи!"
            img 5103
            prisoner6 "Сиськи! Сиськи!"
            img 5114
            prisoner1 "Нет, шлюха! Сначала сиськи! Голые!"
            "Мы шлюхам не верим, да ребята?"
            img 5101
            prisoner3 "Не верим!"
            prisoner4 "Мы не верим шлюхам!"
            img 5102
            prisoner5 "Сиськи!"
            img 5103
            prisoner6 "Сиськи! Сиськи!"
            menu:
                "Показать грудь в обмен на имя надзирателя.":
                    label gallery_5324:
                    music prison_yell_music
                    img 5108
                    prisoner5 "Сиськи!"
                    prisoner6 "Сиськи! Сиськи!"
                    #сиськи выглядывают из-за решетки
                    img black_screen
                    with fadelong
                    img 5625
                    with fadelong
                    prisoner5 "Сиськи!"
                    prisoner6 "Сиськи! Сиськи!"
                    music Loved_up2
                    img 5323
                    with Dissolve(0.5)
                    w
                    img 5324
                    w
                    img 5325
                    w
                    sound prison_yell
                    img 5106
                    prisoner2 "Да! Сиськи!"
                    img 5326
                    w
                    img 5327
                    w
                    img 5108
                    sound prison_yell
                    prisoner5 "Сиськи!"
                    prisoner6 "Сиськи! Сиськи!"
                    img 5328
                    w
                    img 5329
                    w
                    img 5108
                    sound prison_yell
                    prisoner6 "Сиськи! Сиськи!"
                    img 5330
                    w
                    img 5331
                    w
                    img 5332
                    w
                    #еще картинки с сиськами
                    music prison_yell_music
                    img 5113
                    prisoner1 "Хорошо, шлюшка!"
                    "Его имя Боб!"
                    "Если бы ты не была тупой шлюхой, то ты бы запомнила это имя тогда когда тебя привели сюда!"
                    "Ха-ха"
                    music Jail_Clock
                    img 5333
                    with fadelong
                    mt "Сволочи!!!"
                    "(хмык)"
#                    $ jailCageShowedBoobsForBobName = True
#                    $ monicaKnowOverseerName = True
                    return
                "Не показывать.":
                    music Pyro_Flow
                    img 5320
                    m "Я не собираюсь вам ничего показывать! Я не шлюха!"
                    sound prison_yell
                    img 5108
                    prisoner5 "Сиськи!"
                    prisoner6 "Сиськи! Сиськи!"
                    img 5113
                    prisoner1 "Детка! Подумай! У тебя много времени впереди!"
                    "Хе-хе!"
#                    music Jail_Clock
                    return
        "Не показывать.":
            music Pyro_Flow
            img 5320
            m "Я не собираюсь вам ничего показывать! Я не шлюха!"
            sound prison_yell
            img 5108
            prisoner5 "Сиськи!"
            prisoner6 "Сиськи! Сиськи!"
            img 5113
            prisoner1 "Детка! Подумай! У тебя много времени впереди!"
            "Хе-хе!"
#            music Jail_Clock
            return
    return

label gallery_5414:
    music Power_Bots_Loop
    img 5378
    m "Что вам надо снова???"
    img 5115
    prisoner1 "Шлюха, ты знаешь что нам надо!"
    "Давай быстрее, не испытывай наше терпение!!!"
    img 5379
    menu:
        "Я знаю как заткнуть рот этим мерзавцам...":
            label gallery_5444:
            music Pyro_Flow
            img 5441
            with fadelong
            m "Знаете что?"
            "Вы что-то расшумелись сегодня и мешаете мне спать!"
            "Мне без разницы что вы там напридумывали себе!"
            img 5442
            "Вы гниете тут заживо и стали сходить с ума, похоже!"
            "Но я вам скажу одну вещь!"
            img 5443
            "Если вы с этой же минуты не заткнетесь и пророните хоть один звук..."
            "То я скажу надзирателю что вы шумите, когда его нет!"
            img 5444
            "И особенно шумишь ты, жирдяй!"
            img 5445
            prisoner1 "(сглатывает)"
            img 5446
            m "Не знаю почему вы так боитесь шуметь при нем."
            "Но я предупреждаю вас!"
            img 5447
            "Еще хоть один звук и я все ему расскажу!"
            "И не сомневайтесь что он мне поверит!"
            img 5448
            "ЯСНО ВАМ?!?!"
            img 5449
            prisoner1 "Все... все... Не кипятись!"
            "Мы все поняли, мы больше не шумим!"
            "Не надо ему говорить про это!"
            music Jail_Clock
            img 5450
            m "То-то же!!!"
            img 5451
            mt "..."
            "Как я их, а?"
            img 5452
            "Моника, ты умеешь поставить на место зарвавшихся мерзавцев!"
            "Ты молодец!"
            img 5453
            "Интересно, почему они так боятся шуметь при этом жирном слизняке?"
            img 5454
            "Но это и не важно!"
            "Меня это никак не касается!"
            return
        "У меня нет выбора...":
            music prison_yell_music
            img 5369
            with fadelong
            m "..."
            "..."
            "..."
            # вылазят сиськи
            music Loved_up2
            img 5370
            with Dissolve(0.5)
            w
            music Power_Bots_Loop
            img 5114
            prisoner1 "Нет, мы уже их видели!"
            prisoner1 "Шлюха! Никому уже не нужны твои сиськи!"
            "Нам нужно больше!"
            img 5100
            prisoner2 "Да!"
            img 5103
            prisoner6 "Да!"
            img 5101
            prisoner4 "Надо больше!"
            prisoner3 "Да!"
            img 5380
            m "Что вам надо, ублюдки??!?!"
            img 5113
            prisoner1 "Нам нужна твоя попка!"
            img 5100
            prisoner2 "Да!"
            img 5103
            prisoner6 "Да!"
            img 5101
            prisoner4 "Ее попка!"
            prisoner3 "Да!"
            img 5381
            m "Я не буду вам показывать ничего такого!"
            img 5382
            "Это уже слишком!!!"
            img 5114
            prisoner1 "Ты шлюха! Ты хорошая шлюха!"
            "Ты должна слушаться нас!"
            "Плохая шлюха будет наказана!"
            "Плохая шлюха хочет убежать отсюда!"
            img 5100
            prisoner2 "Да!"
            img 5103
            prisoner6 "Да!"
            img 5101
            prisoner4 "Плохая шлюха!"
            prisoner3 "Да!"
            img 5383
            mt "О БОЖЕ!!!"
            "Это заходит слишком далеко!"
            img 5384
            "Я хотела просто потянуть время, но они требуют невозможного!"
            "Я хочу отсюда выбраться, но моя честь дороже всего для меня!"
            img 5385
            "Я ЛЕДИ, а не какая-то потаскуха!"
            img 5386
            menu:
                "Я не буду вам ничего показывать! Ни за что!!!":
                    music Pyro_Flow
                    img 5387
                    m "Делайте что хотите!"
                    "Это для меня уже слишком!"
                    music Jail_Clock
                    img 5388
                    mt "О БОЖЕ!!!"
                    "КАКАЯ МЕРЗОСТЬ!!!"
#                    $ jailCageBlackmailStage = 3
#                    $ jailDaySceneStage = 3
#                    call refresh_scene_fade() from _call_refresh_scene_fade_56

                "Может быть как-то потянуть время?":
                    music Hidden_Agenda
#                    $ jailCageBlackmailAssShowed = True
                    img 5389
                    mt "Я вот-вот выберусь отсюда!"
                    "Мне надо совсем-совсем еще немного времени!"
                    img 5390
                    "Нельзя вот так все испортить, когда я уже почти у цели!"
                    img black_screen
                    with Dissolve(1)
                    img 5391
                    m "Эй вы!"
                    img 5392
                    "Хорошо! Я покажу вам!"
                    img 5393
                    "Но я не буду раздеваться сейчас!"
                    img 5394
                    "Я буду делать это постепенно, каждый день!"
                    img 5393
                    "Вы ведь хотите растянуть удовольствие!"
                    img 5112
                    prisoner1 "Да! Хотим!"
                    img 5111
                    "Хорошо, шлюха! Вставай скорее к нам задом! Нагибайся! Скорее!"
                    img 5395
                    mt "УБЛЮДКИ!!!"
                    img 5396
                    w
                    music Loved_up2
                    img black_screen
                    with Dissolve(1)
                    img 5397
                    with fadelong
                    w
                    img 5398
                    w
                    img 5399
                    w
                    img 5400
                    w
                    img 5401
                    w
                    img 5402
                    w
                    img 5403
                    w
                    "НЕНАВИЖУ!!!"
                    img 5404
                    w
                    img 5405
                    w
                    img 5406
                    w
                    img 5407
                    w
                    img 5408
                    "НЕНАВИЖУУУУУ!!!"
                    # моника встает задом
                    img 5115
                    prisoner1 "Ниже! Наклонись ниже!"
                    "Неопытная шлюха!"
                    # моника наклоняется сильнее
                    img 5409
                    with fadelong
                    w
                    img 5410
                    w
                    img 5411
                    w
                    img 5412
                    mt "ТВАРИ!!!"
                    img 5413
                    w
                    img 5414
                    w
                    img 5415
                    w
                    img 5416
                    "УБЛЮДКИ!!!"
                    img 5417
                    w
                    img 5418
                    w
                    img 5419
                    "ВАМ ВСЕМ КОНЕЦ!!!"
                    img 5420
                    w
                    img 5421
                    "КЛЯНУСЬ!!!"
                    img 5105
                    prisoner1 "Давай! Больше действий! Повиляй бедрами, шлюха!"
                    "Давай!"
                    img 5422
                    w
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_1 = Movie(play="video/Police_Jail_Monica_Butt_1_1.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_1
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_2 = Movie(play="video/Police_Jail_Monica_Butt_1_2.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_2
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_3 = Movie(play="video/Police_Jail_Monica_Butt_1_3.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_3
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_4 = Movie(play="video/Police_Jail_Monica_Butt_1_4.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_4
                    wclean
#                        scene black
#                        image videoPolice_Jail_Monica_Butt_1_5 = Movie(play="video/Police_Jail_Monica_Butt_1_5.mp4", fps=30)
#                        show videoPolice_Jail_Monica_Butt_1_5
#                        wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_6 = Movie(play="video/Police_Jail_Monica_Butt_1_6.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_6
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_7 = Movie(play="video/Police_Jail_Monica_Butt_1_7.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_7
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_8 = Movie(play="video/Police_Jail_Monica_Butt_1_8.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_8
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_9 = Movie(play="video/Police_Jail_Monica_Butt_1_9.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_9
                    wclean
                    scene black
                    image videoPolice_Jail_Monica_Butt_1_10 = Movie(play="video/Police_Jail_Monica_Butt_1_10.mp4", fps=30)
                    show videoPolice_Jail_Monica_Butt_1_10
                    wclean
                    # моника морщится и виляет бедрами
                    img 5423
                    w
                    music Power_Bots_Loop
                    img 5105
                    prisoner1 "Да! Вот так!"
                    "И последнее условие!"
                    img 5424
                    m "Какие еще условия??? Вам что, мало???"
                    img 5115
                    prisoner1 "Мы разрешили тебе раздеваться медленно, шлюха!"
                    "Поэтому мы здесь ставим условия! А ты не пререкаешься!"
                    img 5425
                    m "Какое условие?"
                    img 5112
                    prisoner1 "Скажи что ты хорошая шлюха!"
                    img 5426
                    m "ЧТО СКАЗАТЬ?!?!"
                    img 5114
                    prisoner1 "Скажи что ты хорошая шлюха!"
                    img 5427
                    m "Я НЕ БУДУ ЭТОГО ГОВОРИТЬ!!!"
                    img 5115
                    prisoner1 "Скажи или ты станешь плохой шлюхой! А ты знаешь что грозит плохой шлюхе здесь!!!"
                    img 5428
                    mt "О БОЖЕ!!!"
                    "КАК УНИЗИТЕЛЬНО!"
                    "НЕУЖЕЛИ Я ЭТО СДЕЛАЮ???"
                    menu:
                        "Я НЕ СДЕЛАЮ ЭТО НИ ЗА ЧТО!!!":
                            # моника встает
                            music Pyro_Flow
                            img 5439
                            m "Я никогда этого не скажу!"
                            "Я - леди!"
                            img 5440
                            "А вы - ублюдки!"
#                            music Jail_Clock

                        "У меня нет выбора...":
                            # моника почти плачет
                            img 5429
                            with fadelong
                            w
                            img 5430
                            with fade
                            m "Я хорошая шлюха..."
                            img 5115
                            prisoner1 "Громче! Мы не слышим!"
                            img 5431
                            w
                            img 5432
                            w
                            img 5433
                            w
                            img 5434
                            w
                            img 5435
                            m "Я хорошая шлюха!"
                            img 5115
                            prisoner1 "Громче! Громко и ясно!"
                            img 5436
                            m "Я ХОРОШАЯ ШЛЮХА!!!"
#                            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
                            img 5099
                            prisoner1 "Хорошая шлюха! Завтра в это же время!"
                            # моника плачет в углу
                            img black_screen
                            with Dissolve(1)
                            img 5437
                            with fadelong
                            mt "Мне надо скорее убираться отсюда..."
                            img 5438
                            "Я не знаю как мне жить с тем что я сейчас сделала..."
                            "Но больше моя гордость не выдержит - это точно..."
#            $ jailCageBlackmailStage = 3
#            $ jailDaySceneStage = 3
#            call refresh_scene_fade() from _call_refresh_scene_fade_57
#            return
    return

label gallery_2564:
    img 2535
    music Power_Bots_Loop
    "Мистер Маркус!"
    "Пожалуйста!"
    "Выпустите меня!"
    img 2536
    music Groove2_85
    marcus "Миссис Бакфетт."
    "Свобода исключена."
    "Вы пожизненно пробудете на Ранчо 218."
    img 2537
    m "Что это за название?"
    "Почему это называется Ранчо?"
    "И что значат эти цифры?"
    img 2538
    marcus "Это номер в реестре исправительных учреждений."
    "Оно вполне официально и финансируется из бюджета."
    "Хотя оно построено моими силами и обладает определенными особенностями."
    img 2539
    "Это моя гордость, Миссис Бакфетт!"
    img 2540
    m "Какими особенностями???"
    img 2541
    music Power_Bots_Loop
    marcus "Это рабовладельческая ферма."
#    $ jailCabinetState = 2
#    call refresh_scene_fade() from _call_refresh_scene_fade_106
#    return
#label jail_cabinet_dialogue4:
    img 2542
    with fadelong
    m "Кккакая...?"
    img 2543
    marcus "Миссис Бакфетт."
    "Там содержатся люди, которых официально не существует."
    "Вы забыли что Вас больше нет?"
    "Вам повезло."
    "Вы обладаете определенной красотой и бывшим статусом."
    "Это привлекает гостей Ранчо."
    "Если бы Вы не были женщиной, то Вы подлежали бы утилизации."
    "Правительство не желает тратить деньги на людей, которых нет."
    music Groove2_85
    "Вы же знаете, там сплошная бюрократия."
    "Нет бумаги, значит нет и человека."
    img 2544
    m "Кккаких гостей...?"
    img 2543
    marcus "Это будет зависеть от Training, которые Вы освоите."
    "Чем больше Вы сможете освоить и быстрее примете свою судьбу, тем лучше питание Вы будете получать."
    "Masters будут Вас меньше пороть плетьми."
    img 2545
    "В общем сплошные выгоды, Миссис Бакфетт!"
    img 2546
    music Power_Bots_Loop
    m "Какие Training???"
    "Какие Masters?"
    "Боже!!!"
    "Маркус!!!"
    "О чем ВЫ????"
    img 2547
    music Groove2_85
    marcus "О!"
    "Спасибо что спросили, Миссис Бакфетт!"
    "Я люблю поговорить на эту тему!"
    "Значит так."
    "Сначала Вы пройдете обычный Sex Training, чтобы Вы смогли с легкостью поглощать член любого мужчины."
    "Уметь сокращать мышцы так, чтобы мужчина кончил даже не двигая своим членом."
    "Затем Вы пройдете Anal Training."
    "Где то же самое должны будете уметь делать своим анальным отверстием."
    "При этом, training включает полную разработку отверстий до stage 2."
    img 2548
    music Power_Bots_Loop
    m "Какой stage 2?"
    "Сколько их всего???"
    mt "О УЖАС!!!"
    img 2549
    music Groove2_85
    marcus "Всего их 5."
    "Вы пройдете их все."
    "Начиная со стадии 3 начнется Animal Training."
    "После достижения пятой стадии, Вы пройдете Painslut Training."
    "Это все обязательное обучение."
    "Дальше есть еще несколько факультативных Training, но их Вы можете проходить по желанию."
    img 2550
    "Хотя оно должно у Вас возникнуть!"
    "Ведь чем Вы больше освоите, тем лучше будет Ваша жизнь!"
#    $ jailCabinetState = 3
#    call refresh_scene_fade() from _call_refresh_scene_fade_107
#    return
#label jail_cabinet_dialogue5:
    img 2551
    with fadelong
    m "Ччччто.. значит...."
    "Animal Training...??"
    img 2552
    marcus "Видите-ли, Миссис Бакфетт."
    "Существуют много богатых людей и политиков, которые имеют домашних животных."
    "У самих людей уже есть и богатство и любые женщины, которые придутся им по вкусу."
    "Однако, они также любят своих питомцев и хотят для них самого лучшего!"
    "Мое Ранчо 218 позволяет снять напряжение у их питомцев."
    "При этом, хозяева любят наблюдать за процессом."
    "Делать частные фото и видеозаписи."
    "Это не запрещено."
    "Иногда они сначала оценивают сами."
    "В этот момент Вам надо будет особенно стараться."
    img 2553
    "НО!"
    "Все-же, самое главное - это сделать так чтобы питомец остался доволен!"
    "Если этого не будет, Ваша жизнь станет намного сложнее, Миссис Бакфетт!"
    img 2554
    music Power_Bots_Loop
    m "Но... разве.."
    "Разве животные не должны заниматься этим с такими же как они?"
    img 2555
    music Groove2_85
    marcus "Да, они делают и это, но это постепенно выходит из моды в высоких кругах."
    "Хозяевам питомцев неинтересно наблюдать за этим процессом."
    img 2556
    "А вот с девушками гораздо интереснее."
    img 2555
    "Не переживайте, там Вы будете не одна."
    "Сейчас там находится порядка тридцати других девушек."
    "Со одной стороны, это даст Вам возможность общения."
    img 2557
    "Но, с другой, это дополнительная конкуренция."
    "Потому что все стараются."
    img 2558
    music Power_Bots_Loop
    m "И...."
    "И..."
    "И с ...."
    "И с... каким... животными.. мне надо будет это делать?"
    marcus "Со всеми."
    m "В смысле... со всеми?"
    img 2559
    music Groove2_85
    marcus "Конечно не со всеми сразу!"
    img 2560
    "Вам сначала придется растянуть свои отверстия до stage 3, чтобы заниматься этим с песиками."
    "Далее Вам будут предложены поросята."
    "Затем Лошади и другой крупный рогатый скот."
    img 2561
    music Pyro_Flow
    m "Вы больной!!!"
    "Больной ублюдок!!!"
    "Это же ненормально!!!"
#    $ jailCabinetMonicaStanding = True
#    $ jailCabinetState = 4
#    call refresh_scene_fade() from _call_refresh_scene_fade_108
#    return
#label jail_cabinet_dialogue6:
    img 2562
    music Groove2_85
    marcus "Не переживайте, Миссис Бакфетт!"
    img 2563
    "Вы через небольшое время примете свою судьбу и с головой погрузитесь в процесс."
    img 2564
    music Power_Bots_Loop
    m "БОЖЕ!!!"
    "ЗА ЧТО МНЕ ЭТО????"
    "КАК ТАКОЕ СЛУЧИЛОСЬ???"
    img 2565
    music Groove2_85
    marcus "Миссис Бакфетт."
    "Могу Вам сказать что основное внимание Вы привлекли своей обложкой на журнале."
    "Если бы Вы сидели и участвовали в своих локальных конкурсах красоты, то скорее всего этого бы ничего не было."
    "Вы захотели славы."
    "И вы получите славу, хотя и в довольно узких кругах."
    img 2566
    "Но поверьте, те люди, которые будут на Вас смотреть, владеют почти всем миром."
    "И Вы должны ценить это!"
    img 2567
    "Но Ваша работа не пропадет!"
    "Я собираюсь открыть частный глянцевый журнал для узкого круга лиц."
    "На его страницах будут питомцы наших гостей."
    "Самым лучшим из них будут посвящены отдельные обложки."
    "На которых Вы будете с ними совокупляться."
    "Учитывая большой тираж модного журнала с Вами на обложке."
    "Наш новый журнал будет пользоваться популярностью в наших узких кругах!"
    "Конечно на место на обложке будут претендовать и другие участницы!"
    img 2568
    "Но у Вас есть фора!"
    "Запомните!"
#    $ jailCabinetState = 5
#    call refresh_scene_fade() from _call_refresh_scene_fade_109
#    return
#label jail_cabinet_dialogue7:
    music Power_Bots_Loop
    img 2569
    with fadelong
    m "Ммммистер... Маркус......"
    "Я прошу Вас!......"
    "(хмык)"
    img 2570
    "Я умоляю Вас!....."
    "(хмык)"
    img 2571
    "Пожалуйста!....."
    "(хмык)"
    img 2572
    "Не надо меня туда посылать....."
    "(хмык)"
    img 2573
    music Groove2_85
    marcus "Решение принято, Миссис Бакфетт."
    "Через неделю Вы отправитесь туда."
    "Со временем Вы привыкнете и забудете прошлую жизнь."
    "Вам сейчас она кажется такой яркой, такой близкой."
    img 2574
    "Но память со временем все сотрет."
    "Вы примете новую жизнь и будете гордиться тем что находитесь на обложке в обнимку с обаятельным питомцем!"
    img 2575
    m "Сэр...."
    "Я...."
    img 2576
    "У меня..."
    "Кружится голова...."
    img black_screen
    with Dissolve(1)
    sound snd_bodyfall
    w
    img 2577
    with fade
    marcus "Миссис Бакфет."
    "Я понимаю."
    "Вас переполняют чувства радости от того что Вы останетесь жить."
    "Пожалуйста, отдыхайте."
    "Поговорим с Вами позже."

    stop music fadeout 0.5
    sound man_steps
    img black_screen
    with Dissolve(1)
    img 5501
    with fadelong
    music Groove2_85
    marcus "Боб."
    overseer "Да, Мистер Маркус?"
    marcus "Боб."
    "Прибери в нижнем кабинете."
    overseer "Так точно, Мистер Маркус!"

    img black_screen
    with fade
    $ renpy.pause(1)
    img 2578
    with fadelong
    overseer "Опять ты бардак развела!"
    "Одни проблемы от тебя!"
    return

label gallery_2581:
    img black_screen
    with Dissolve(1)
    music Groove2_85
    #
    img 5599
    with fadelong
    overseer "Джимми."
    "Не трогай пока эту сучку."
    img 5600
    "Я боюсь что она может двинуть концы."
    "А Мистер Маркус имеет к ней какой-то интерес."
    "Я не хочу проблем."
    img 5601
    prisoner1 "Но Боб!"
    "Я же победил!"
    "Где моя награда!"
    img 5602
    overseer "Через неделю можешь начинать."
    "Она придет в себя и успокоится."
    img 5603
    prisoner1 "У меня будет 2 недели, Боб!"
    img 5604
    overseer "Через 2 недели я подселю нового победителя, Джимми."
    "Это не обсуждается."
    img 5605
    prisoner1 "А как же я?"
    "Получается у меня будет всего неделя?"
    img 5606
    "Я не успею раздолбать эту попу!"
    img 5607
    "Посмотри какая она тугая!"
    img 5608
    "Вон!"
    img 5609
    "Видишь?"
    img 5610
    w
    img 5611
    w
    img 5612
    w
#    img 5613
#    w
    img 5614
    overseer "Хорошо, Джимми."
    "Тебя устроит если я подселю следующего победителя и вы будете заниматься ей вдвоем?"
    "У тебя будет как раз лишняя неделя."
    img 5615
    prisoner1 "Вдвоем?"
    overseer "Да."
    img 5616
    "Может быть я тоже присоединюсь."
    "У нее же три отверстия."
    img 5617
    prisoner1 "Хорошо, Боб."
    "Так уж и быть."
    #
    img black_screen
    with fade
    sound snd_jail_door
    $ renpy.pause(1)
    img 5618
    with fadelong
    prisoner1 "Ну что, детка!"
    "Тебе повезло!"
    "Через неделю ты будешь наслаждаться сразу двумя членами в твоей попке!"
    "Хе-хе!"
    "А пока я буду тренировать своего Жесткого Боба!"
    stop music fadeout 1.0
    img black_screen
    with fade
    $ renpy.pause(2)
    music Groove2_85
    sound snd_phone_ring
    img 5619
    with fadelong
    overseer "Да, Мистер Маркус?"
    "..."
    "Да!"
    "..."
    "Так точно!"
    img 2579
    with fadelong
    overseer "Заключенная!"
    "Встать!"
    "Хватит здесь валяться целыми днями!"
    img 2580
    with fade
    m "мммм.."
    "м...."
    "(хмык)"
    "С лошадьми..."
    "Он сказал с лошадьми...."
    "(хмык)"
    "......"
    "ммм...."
    "хххх....."
    "На обложке...."
    "ууммммммпппффф...."
    img 2581
    with fade
    overseer "Что ты там мычишь все?"
    "Я сказал встать!"
    m "Ч...."
    "Что же... со мной будет....."
    "О БОЖЕ...."
    overseer "ВСТАААТЬ!!!"
    "А то сейчас снова окачу из шланга!"
    img 2582
    with fadelong
    overseer "То-то же!"
    "А теперь одевайся!"
    "Мистер Маркус велел тебе одеться и идти к нему в кабинет!"
    label gallery_5623:
    img 2583
    music Power_Bots_Loop
    m "О..."
    "Оддд..."
    "Одежда...."
    "О Боже!"
    "Одежда!"
    "Мое платье!!!"
    "Дайте!!!"
    "Дайте я скорее одену его!!!"
    "Дайте мне его сюда!!!!"
    "Быстрее!!!!"
    music Groove2_85
    overseer "Да бери ты!"
    "Не порви только!"
    "Другого же нет!"
    img black_screen
    with Dissolve(1)
    sound snd_fabric1
    $ renpy.pause(1)
    img 2584
    with fadelong
    m "Сэр..."
    "Сэр..."
    "А где мое белье?"
    "Здесь нет моего белья..."
    img 2585
    overseer "Я его порвал, когда снимал!"
    "Зачем оно тебе?"
    m "Но как-же я одену платье без трусиков?"
    overseer "Одевай давай!"
    "Все-равно скоро снимать!"
    "Ты его ненадолго одела."
    "Только чтобы подняться наверх к Мистеру Маркусу!"
    img 2586
    with fadelong
    overseer "Идем!"
    "Шевелись давай!"
    #
    sound prison_yell
    img 5620
    prisoner1 "Шлюха!"
    prisoner4 "Шлюха!"
    sound prison_yell
    img 5621
    prisoner3 "Покажи задницу, шлюха!"
    prisoner5 "Покажи сиськи!"
    sound prison_yell
    img 5622
    prisoner2 "Повиляй задницей!"
    prisoner1 "Будь хорошей шлюхой!"
    img 5623
    w
#    $ marcusCabinetState = 4
#    $ sceneStages = ["_s2"]
#    $ autorun_to_object("police_marcuscabinet_s2", "marcus_cabinet_dialogue9")
#    call change_scene("police_marcuscabinet", False, False) from _call_change_scene_194
    return

label gallery_2612:
    music Groove2_85
    img 2592
    with fadelong
    marcus "Здравствуйте, Миссис Бакфетт."
    "Вы догадываетесь зачем Вы здесь?"
    img 2593
    music Power_Bots_Loop
    m "Я догадываюсь."
    "Вы хотите отправить меня на свою свиноферму."
    img 2594
    "Вы хотите моей смерти!!!"
    "О Боже!!!"
    img 2595
    music Groove2_85
    marcus "Миссис Бакфетт."
    "Смерть на Ранчо 218 грозит только тем кто не выполняет приказы Master."
    "Остальные процессы происходят так, что боль не приводит к смертельному исходу."
    "Наши Masters в этом очень опытны."
    "Но я Вас позвал не для этого."
#    $ marcusCabinetState = 6
#    call refresh_scene_fade() from _call_refresh_scene_fade_201
#    return
#label marcus_cabinet_dialogue11:
    img 2596
    with fadelong
    m "А..."
    "Для чего....?"
    img 2597
    marcus "Миссис Бакфетт."
    "Возникла неожиданная ситуация."
    "Я Вам объясню ее, а потом Вы должны будете сделать выбор."
    img 2598
    "Но хорошо подумайте прежде чем сделать это!"
    img 2599
    m "Какой выбор?"
    "У меня есть какой-то выбор?"
    img 2600
    marcus "Да, Миссис Бакфетт."
    "Мы не ожидали что за вас могут заступиться серьезные люди."
    "Учитывая Ваш характер и образ жизни."
    img 2601
    m "Люди???"
    "Друзья???"
    img 2602
    music RnB4_100
    mt "ДРУЗЬЯ!!!"
    "МНЕ КТО-ТО РЕШИЛ ПОМОЧЬ!!!"
    "У МЕНЯ НЕТ СЛОВ!"
    "Я ДУМАЛА НАДЕЖДЫ БОЛЬШЕ НЕТ!!!"
    img 2603
    music Groove2_85
    marcus "Да, некто очень хорошо известный."
    "И Вам и Нам."
    img 2604
    m "Кто???"
    img 2603
    marcus "Дик Адвокат."
    img 2605
    music RnB4_100
    m "ДИК!!"
    mt "ДИК!! ДИК!!"
    mt "ДИК!! ДИК!!"
    mt "ТЫ СДЕЛАЛ ЭТО!"
    "ТЫ НЕ ОСТАВИЛ МЕНЯ!"
    img 2606
    music Groove2_85
    marcus "Да, Дик."
    "Но не спешите радоваться."
    "У него далеко не такие связи как у людей, которые ждут Вас!"
    "Я уже обещал многим и на Вас уже очередь!"
    "Он использовал кое-какие связи."
    "Но главное - это лазейку в законе."
    img 2607
    with fade
    music Power_Bots_Loop
    "Она очень..."
    "ОЧЕНЬ!"
    "ОЧЕНЬ ХРУПКАЯ!"
    music Groove2_85
    img 2608
    "Мне очень жаль, но я не имею права Вас удерживать, Миссис Бакфетт."
    img 2609
    music RnB4_100
    m "!!!!!!!!!"
    img 2610
    music Power_Bots_Loop
    marcus "Не спешите радоваться, Миссис Бакфетт."
    "И подумайте что Вас ждет."
    "У Вас нет ничего."
    "Вы никто."
    "Нет никаких документов что Вы существуете."
    img 2611
    "У любого бомжа больше прав чем у Вас!"
    img 2612
    music RnB4_100
    m "У МЕНЯ ЕСТЬ ДРУЗЬЯ!!!"
    marcus "Вы так считаете, Миссис Бакфетт."
    "Но я думаю Вы ошибаетесь."
    img 2613
    "В любом случае Вы ненадолго покинете эти стены."
    music Power_Bots_Loop
#    $ marcusCabinetState = 7
#    call refresh_scene_fade() from _call_refresh_scene_fade_202
#    return
#label marcus_cabinet_dialogue12:
    img 2614
    with fadelong
    m "ПОЧЕМУ???"
    img 2615
    marcus "Потому что никакие обвинения с Вас не сняты."
    "Эта лазейка касается самого процесса."
    "Мы допустили незначительное нарушение."
    "Однако, хоть Вы и выйдете отсюда."
    img 2616
    "Но любое."
    img 2617
    "Я повторю!"
    "ЛЮБОЕ!"
    img 2618
    "Любое нарушение приведет Вас сюда и процесс пойдет как и раньше."
    "Любой полицейский, который проверит у Вас документы, доставит Вас сюда."
    img 2619
    "Если Вы перейдете дорогу в неположенном месте, Вас доставят сюда."
    "Если Вы станете где-то кричать, Вас доставят сюда."
    img 2620
    "В общем."
    "Шансов у Вас нет."
    "Вы вернетесь сюда."
    img 2621
    "Вам даже негде жить."
    img 2622
    "Если Вас застанут ночью спящей на улице - это нарушение закона."
    img 2623
    "Вас доставят сюда."
    img 2624
    music Groove2_85
    "Я готов поставить свой лучший виски на Ранчо 218 что Вы вернетесь сюда уже завтра."
    img 2625
    "В связи с этим у Вас есть выбор."
    img 2626
    m "Какой выбор?"
    img 2627
    marcus "Вы можете идти сейчас."
    "Прямо сейчас."
    img 2628
    "Чтобы вернуться завтра."
    img 2629
    "Либо Вы можете отказаться уходить и отправиться на Ранчо 218 прямо сейчас."
    img 2630
    "Во втором случае Вы пройдете стандартный набор Training."
    img 2631
    music Villainous_Treachery
    "Но если Вы уйдете и вернетесь завтра, то Вы начнете свой путь на Ранчо 218."
    img 2632
    "Как fuck meat."
    "С самого низа."
    "И не сможете добиться каких-либо успехов, потому что во время карьерного роста растеряете всю красоту."
    img 2633
    "..."
    img 2634
    "Я повторю."
    "То что Вы вернетесь сюда - это абсолютно точно."
    img 2635
    "Вы можете сходить погулять, но этим Вы погубите свою будущую жизнь."
    "Хорошенько подумайте."
    img 2636
    "..."
    img 2637
    m "..."
    img 2636
    marcus "..."
    img 2638
    w
    img 2639
    m "..."
    img 2636
    marcus "Итак."
    "Что Вы выбираете?"
#    $ marcusCabinetState = 8
#    call refresh_scene_fade() from _call_refresh_scene_fade_203
#    return
#label marcus_cabinet_dialogue13:
    menu:
        "Выйти на свободу (временно)":
            pass
#        "Отправиться на Ранчо 218 (отдельное дополнение)":
#            help "Дополнение в разработке. Следите за новостями!"
#            jump marcus_cabinet_dialogue13
        "Продолжить думать...":
            return
    music Pyro_Flow
    img 2640
    with fadelong
    m "Я выбираю свободу, Маркус."
    img 2641
    marcus "Уффф.."
    img 2642
    "Хорошо, Миссис Бакфетт."
    "До скорой встречи."
    "Жаль, я надеялся Вы сделаете блестящую карьеру на Ранчо 218."
    "Мне жаль губить такой талант в качестве fuck meat."
    img 2643
    m "Надеюсь что не до скорой встречи, Маркус."
    img black_screen
    with Dissolve(1)
    sound snd_phone1
    $ renpy.pause(2.0)
    marcus "Вывести заключенную."
#    music Power_Bots_Loop
#    $ policeEntranceState = 4
#    $ autorun_to_object("police_entrance_s2", "entrance_dialogue7")
#    call change_scene("police_entrance_s2") from _call_change_scene_272
    return

label gallery_5489:
#    $ jailDay = 13
#    $ day = day + 1
#    $ jailDaySceneStage = 0
#    $ jailScenePlace = 0
#    stop music fadeout 1.0
#    call textonblack(_("ДЕНЬ 13")) from _call_textonblack_28
    img black_screen
    with Dissolve(1)
    music Jail_Clock
    img 2505
    with fadelong
    mt "Что же мне делать?"
    "(хмык)"
    "Мне конец..."
    "(хмык)"
    "Я умру здесь, умру!"
    music Groove2_85
    img black_screen
    with Dissolve(1)
    #заключенный подходит
    sound snd_jail_lock
    img black_screen
    with Dissolve(1)
    img 2505
    with fadelong
    overseer "Заходи, Джимми!"
    sound man_steps
    img 5473
    "Ты победитель!"
    img 5474
    "Но помни!"
    "Через две недели я тебя выселю отсюда!"
    img 5475
    prisoner "Нет проблем, Боб!"
    img 5476
    "Я буду торопиться!"
    "В день по пять раз - это семьдесят раз!"
    img 5477
    overseer "А ты сможешь?"
    prisoner "Смогу, Боб!"
    img 5478
    "Я уже давно не засовывал член в женскую киску!"
    img 5479
    "И в ротик!"
    "И в попу тоже!"
    img 5480
    overseer "Удачно провести время, Джимми!"
    img black_screen
    with Dissolve(1)
    #уходит
    sound snd_jail_lock
    img 5116
    with fadelong
    w
    music Groove2_85
    img 5481
    with fadelong
    prisoner "Ну что, детка!"
    img 5482
    "Знакомься с нами!"
    img 5483
    "Меня зовут Джимми!"
    img 5484
    "А это мой друг!"
    "Жесткий Боб!"
    img 5485
    with fadelong
    sound Jump2
    "Мы теперь будем жить вместе!"
    img 5486
    w
    img 5487
    w
    img 5488
    w
    img 5489
    w
    img 5490
    w
    img 5491
    "Ты ему понравилась!"
    img 5492
    w
    img 5493
    w
    img 5494
    w
    img 5495
    w
    stop music fadeout 0.5
    img black_screen
    with Dissolve(1)
    sound man_steps
    #заходит Маркус
    music Groove2_85
    img 5496
    with fadelong
    overseer "Всем тихо!"
    "Мистер Маркус идет!"
    img 5498
    w
    img 5497
    prisoner "Упс!"
    img 5499
    overseer "Быстро назад в свою камеру!!!"
    img 5500
    w
    sound snd_jail_lock
    img black_screen
    with Dissolve(1)
    #Маркус подходит к Бобу
    music Groove2_85
    img 5501
    with fadelong
    marcus "Добрый день, Боб!"
    overseer "Добрый день, Мистер Маркус!"
    "Что я могу для Вас сделать?"
    marcus "Как там новая заключенная?"
    overseer "Немного переживает, но в целом в порядке."
    "Еще не смирилась."
    marcus "Ясно."
    img 5502
    "Я сейчас проведу процесс с Господином Судьей, а потом вызову тебя, чтобы ты привел ее ко мне."
    overseer "Так точно, Мистер Маркус!"
    #В комнате допросов
    stop music fadeout 1.0
    call textonblack(_("СПУСТЯ 15 МИНУТ..."))
    img black_screen
    with Dissolve(1)
    music Groove2_85
    img 5503
    with fadelong
    judge "Хорошо, Маркус."
    "Я оформлю решение как полагается."
    "Не забудь меня пригласить, когда она станет покладистой."
    marcus "Конечно!"
    "До встречи!"
    judge "До встречи, Маркус."
    img black_screen
    with Dissolve(1)
    img 5503
    with fadelong
    sound snd_phone1
    overseer "Да, Мистер Маркус?"
    marcus "Боб, давай веди ее сюда!"
    "Пора ей узнать что ее ждет."
    overseer "Конечно, Мистер Маркус, одну минуту!"
    label gallery_5510:
    img black_screen
    with Dissolve(1)
    music Groove2_85
    img 2507
    with fadelong
    overseer "Эй!"
    "Давай вставай!"
    "Хватит тут отдыхать!"
    "Мистер Маркус вызывает тебя!"
    img 2508
    m "Мистер Маркус!"
    "Все-таки он согласился со мной поговорить?"
    "Пожалуйста, отведите меня к нему!"
    img 2509
    "Я все ему объясню!"
    "Это какая-то ошибка!"
    "Он должен выпустить меня отсюда!"
    img 2510
    overseer "Вот вставай и иди."
    "Я тебя не собираюсь нести к нему."
    #
    img 2511
    with fadelong
    overseer "Иди за мной!"
#    if jailCageBlackmailMonicaSaidSheIsAWhore == True:
    img 5504
    with fade
    sound prison_yell
    prisoner2 "Шлюха! Шлюха!"
    img 5505
    with fade
    prisoner1 "Хорошая Шлюха!"
    sound prison_yell
    img 5506
    with fade
    prisoner3 "Хорошая Шлюха!"
    img 5507
    with fade
    prisoner4 "Да! Хорошая Шлюха!"
    img 5508
    with fade
    prisoner1 "Хорошая Шлюха!"
    sound prison_yell
    img 5509
    with fade
    prisoner6 "Шлюха! Хорошая!"
    img 5510
    with fade
    prisoner5 "Хорошая Шлюха!"
    sound prison_yell
    img 5511
    with fade
    prisoner2 "Шлюха! Шлюха!"
    img 5512
    with fade
    sound prison_yell
    prisoner1 "Хорошая Шлюха!"
    img 5513
    with fade
    w
    img 5514
    with fade
    w
    sound prison_yell
    img 5515
    with fade
    w
    img 5516
    with fade
    w
    sound prison_yell
    img 5517
    with fade
    w
    img black_screen
    with Dissolve(1)
    img 2512
    with fadelong
    overseer "Мистер Маркус!"
    "Заключенная доставлена."
    img 2513
    marcus "Хорошо, Боб."
    "Можешь ступать."
    img 2514
    overseer "Мистер Маркус!"
    "Если я понадоблюсь, только позовите!"
    img 2515
    marcus "Не надоедай, Боб!"
    "Брысь отсюда."
    overseer "Так точно, Мистер Маркус!"
#    $ autorun_to_object("police_jailcabinet", "jail_cabinet_dialogue1")
#    call change_scene("police_jailcabinet", False, False) from _call_change_scene_245
    return

label gallery_5540:
#    $ jailCabinetMonicaPunished = True
    music Power_Bots_Loop
    #
    img 5518
    with fadelong
    m "Маркус! Ты мерзкий ублюдок!"
    "Ты ничтожество!"
    "Ты понимаешь вообще КТО Я???"
    img 5519
    "Какие-то stage... Какие-то цифры..."
    "Это ты собрался оценивать меня по ним?!?!"
    img 5520
    "Я - Моника Бакфетт!"
    img 5521
    "И я никогда и никому не позволю оценивать меня подобным образом!!!"
    img 5522
    m "..."
    img 5523
    marcus "..."
    img 5524
    w
    # улбыается
    img 5525
    marcus "..."
    img 5526
    w
    # наклоняется и говорит куда-то
    sound beep1
    img 5527
    "Досмотр заключенной!"
    # заходят полицейские и надзиратель
    sound snd_jail_door
    img 5528
    with fade
    m "Что?"
    img 5529
    "Что вы...."
    img 5530
    w
    img 5531
    w
    img 5532
    sound snd_woman_scream1a
    "Что вы делаете?!?!"
    img 5533
    w
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_1 = Movie(play="video/Police_Jail_Monica_Humiliation_1_1.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_1
    wclean
    img 5534
    w
    img 5535
    w
    img 5536
    w
    img 5537
    w
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_2 = Movie(play="video/Police_Jail_Monica_Humiliation_1_2.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_2
    wclean
    img 5538
    w
    img 5539
    "Пустите меня!"
    "Отпустите меня немедленно!!!"
    sound snd_woman_scream1a
    img 5540
    "Ааааааааааа!!!!"
    img 5541
    "Что вы делаете?!?!"
    img 5542
    w
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_3 = Movie(play="video/Police_Jail_Monica_Humiliation_1_3.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_3
    wclean
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_4 = Movie(play="video/Police_Jail_Monica_Humiliation_1_4.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_4
    wclean
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_5 = Movie(play="video/Police_Jail_Monica_Humiliation_1_5.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_5
    wclean
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_6 = Movie(play="video/Police_Jail_Monica_Humiliation_1_6.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_6
    wclean
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_7 = Movie(play="video/Police_Jail_Monica_Humiliation_1_7.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_7
    wclean
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_8 = Movie(play="video/Police_Jail_Monica_Humiliation_1_8.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_8
    wclean
    img 5543
    w
    img 5544
    w
    img 5545
    w
    img 5546
    m "..."
    img 5547
    "Помогите, кто-нибудь!!!"
    img 5548
    w
    # Маркусу
    img 5549
    w
    img 5550
    m "Что ты делаешь???"
    "Не трогай меня!!!"
    img 5551
    marcus "Миссис Бакфетт. Вот видите."
    "Вы позволили мне себя оценить."
    "Спасибо."
    img 5552
    "Итак..."
    img 5553
    w
    img 5554
    w
    img 5555
    with Dissolve(1.0)
    sound snd_woman_scream1a
    "Вагина Миссис Бакфетт..."
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_9 = Movie(play="video/Police_Jail_Monica_Humiliation_1_9.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_9
    wclean
    scene black
    image videoPolice_Jail_Monica_Humiliation_1_10 = Movie(play="video/Police_Jail_Monica_Humiliation_1_10.mp4", fps=30)
    show videoPolice_Jail_Monica_Humiliation_1_10
    wclean
    img 5556
    "Хм... да вы почти девственница, Миссис Бакфетт!"
    img 5557
    w
    img 5558
    "Скажите, у вас был до этого вагинальный секс? И сколько раз?"
    # молчит и с ненавистью смотрит
    img 5559
    m "..."
    img 5560
    w
    img 5561
    w
    img 5562
    marcus "Вы решили молчать? Это плохо."
    img 5563
    "В таком случае мы сейчас протестируем Вас на питомце."
    "У меня как раз есть один в соседней комнате."
    # лай собаки
    sound dogs_barking2
    img 5564
    "Боб, приведи Вуфи."
    sound snd_woman_scream2
    img 5565
    m "НЕЕЕЕЕТ!!!"
    m "Я скажу! Только не надо никого приводить!"
    img 5566
    marcus "Хорошо, Миссис Бакфетт."
    "Если вы будете себя хорошо вести, то мы отложим эту процедуру, на пару дней..."
    img 5567
    "Итак, сколько раз у вас был секс?"
    m "Два раза..."
    img 5568
    marcus "Два? Нехорошо врать, Миссис Бакфетт..."
    img 5569
    m "Три! Может четыре! Я не помню!"
    "Но меньше пяти!"
    img 5570
    "Пожалуйста, отпустите меня!"
    img 5571
    marcus "Это больше похоже не правду."
    img 5572
    marcus "Хм... у вас девственный анус!"
    img 5573
    "Пожалуй мы не будем начинать с anal training, а лишим Вас анальной девственности сразу с подходящим питомцем."
    img 5573
    w
    img 5574
    "Одного из наших клиентов. Он будет доволен!"
    img 5575
    m "Нет! Пожалуйста!"
    img 5576
    "Не надо!"
    img 5577
    marcus "Ваше мнение совершенно не важно, Миссис Бакфетт!"
    img 5578
    "Вы просто вещь."
    img 5579
    "Хорошо, досмотр закончен!"
    img 5580
    with fade
    w
    sound snd_bodyfall
    img 5581
    with fade
    w
    img 5582
    with fade
    w
    img 5583
    with fade
    w
    img 5584
    with fade
    w
    img 5585
    with fade
    w
    img 5586
    with fade
    # полицейским
    "Вы свободны!"
    img 5587
    with fadelong
    w
    sound snd_jail_door
#    call jail_cabinet_dialogue7() from _call_jail_cabinet_dialogue7
    return
