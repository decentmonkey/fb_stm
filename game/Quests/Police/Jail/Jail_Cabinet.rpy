label jail_cabinet_dialogue1:
    img 2516
    with fade
    marcus "Здравствуйте, Миссис Бакфетт!"
    "Присаживайтесь!"
    call refresh_scene_fade() from _call_refresh_scene_fade_104
    return

label jail_cabinet_dialogue2:
    img 2518
    with fadelong
    marcus "Здравствуйте, Миссис Бакфетт!"
    marcus "Отлично выглядите."
    "Это платье Вам очень идет!"
    img 2519
    music Pyro_Flow
    m "Какое платье, Маркус!"
    "Верни мне одежду!"
    "Так нельзя обращаться с девушками моего положения!"
    img 2520
    "Когда ты меня выпустишь отсюда???"
    "Ты!!!"
    "Ублюдок!!!"
    img 2521
    music Groove2_85
    "(хмык)"
    img 2522
    marcus "Миссис Бакфетт..."
    "Эх... Миссис Бакфетт."
    "Вы слишком грубо общаетесь со мной."
    "А ведь я только что спас Вашу жизнь!"
    img 2523
    m "В каком смысле?"
    img 2524
    marcus "Мы только что провели суд по Вашему делу."
    "Я применил все свои связи и влияние чтобы Вас не направили на электрический стул."
    "Потому что ситуация для Вас ухудшилась за все это время."
    img 2525
    music Power_Bots_Loop
    m "Почему ухудшилась?"
    "Что вы имеете ввиду?"
    img 2526
    marcus "Ваш муж."
    "Он все свалил на Вас."
    "И привел убедительные доказательства."
    "Тем самым он спас себя."
    "Он, возможно, даже через какое-то разумное время выйдет на свободу."
    img 2527
    "В отличие от Вас, Миссис Бакфетт."
    img 2528
    "..."
    "Хммм.."
    "Мне нравится называть Вас так."
    img 2529
    m "Но ведь во всем виноват он!"
    img 2530
    music Groove2_85
    marcus "Я тоже так считаю, Миссис Бакфетт."
    "Потому Вы должны понять что я ваш лучший друг!"
    $ jailCabinetState = 1
    call refresh_scene_fade() from _call_refresh_scene_fade_105

    return

label jail_cabinet_dialogue3:
    img 2531
    with fadelong
    m "Но как мог проходить суд здесь???"
    "А где присяжные заседатели???"
    "Где сам процесс???"
    "Ведь так делать нельзя!"
    "Я знаю как устроена эта система!"
    img 2532
    marcus "Миссис Бакфетт."
    "Учитвая секретные материалы, которые не подлежат публичному разглашению."
    "И которые фигурируют в деле."
    "Заседание прошло в закрытом режиме."
    img 2533
    "Да, возможно место Вас может немного смутить."
    "Но все бумаги будут в порядке."
    "Зато это позволило мне направить Вас в нужное мне заведение."
    img 2534
    m "В какое заведение?"
    "Что это значит?"
    "И сколько я там пробуду?"
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
    $ jailCabinetState = 2
    call refresh_scene_fade() from _call_refresh_scene_fade_106
    return

label jail_cabinet_dialogue4:
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
    $ jailCabinetState = 3
    call refresh_scene_fade() from _call_refresh_scene_fade_107
    return

label jail_cabinet_dialogue5:
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
    $ jailCabinetMonicaStanding = True
    $ jailCabinetState = 4
    call refresh_scene_fade() from _call_refresh_scene_fade_108
    return

label jail_cabinet_dialogue6:

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
    $ jailCabinetState = 5
    call refresh_scene_fade() from _call_refresh_scene_fade_109

    return

label jail_cabinet_dialogue7:
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

    stop music fadeout 1.0
    call textonblack(t_("СПУСТЯ 15 МИНУТ...")) from _call_textonblack_19
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

    $ marcusCabinetState = 4
    $ sceneStages = ["_s2"]
    $ autorun_to_object("police_marcuscabinet_s2", "marcus_cabinet_dialogue9")
    call change_scene("police_marcuscabinet", False, False) from _call_change_scene_194
    return

label jail_cabinet_punishment:
    $ jailCabinetMonicaPunished = True
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
    call jail_cabinet_dialogue7() from _call_jail_cabinet_dialogue7
    return
