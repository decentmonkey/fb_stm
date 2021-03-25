default monicaMollyBattle1 = False # Моника узнала от Эшли о том, что Молли не платит проценты
default monicaMollyBattle2 = False # Моника пошла на 1-й батл с Молли
default monicaMollyBattle3 = False # Моника с Молли дерутся в гримерке - catfight
default monicaMollyBattle4 = False # Моника пошла на 2-й батл с Молли

#call ep215_dialogues1_pub_1() # Моника перед выходом на сцену, а Молли уже уходит
#call ep215_dialogues1_pub_2() # Моника приходит в гримерку, разговор с Молли
#call ep215_dialogues1_pub_3() # клик на Молли, разговор перед батлом
#call ep215_dialogues1_pub_4() # с Молли возле сцены, перед первым батлом
#call ep215_dialogues1_pub_5() # с Молли на сцене, первый батл
#call ep215_dialogues1_pub_6() # крики посетителей паба во время батла
#call ep215_dialogues1_pub_7() # в гримерке после 1-го батла
#call ep215_dialogues1_pub_8() # барная стойка, клик на Эшли после 1-го батла
#call ep215_dialogues1_pub_9() # клик на Молли перед дракой
#call ep215_dialogues1_pub_9_loop1() # сцена драки
#call ep215_dialogues1_pub_10() # с Молли на сцене, второй батл
#call ep215_dialogues1_pub_11() # в гримерке после 2-го батла
#call ep215_dialogues1_pub_12() # клик на Молли после того как Моника стала королевой
#call ep215_dialogues1_pub_13() # клик на Клэр после того как Моника стала королевой
#call ep215_dialogues1_pub_14() # клик на Эшли после того как Моника стала королевой



# при условии, что был обнаженный приват всех девочек Shiny Hole перед банкиром
# возле сцены
# Моника перед выходом на сцену, а Молли уже уходит
label ep215_dialogues1_pub_1:
    # Молли подходит к Эшли, она в одежде
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 31964
    w
    imgf 31965
    w
    imgd 31966
    w
    # делает вид, как-будто Моника - пустое место, обращается к Эшли
    imgf 31967
    molly "Эшли, я на сегодня все."
    # Эшли ей улыбается
    ashley "Хорошо, Молли. Сколько ты сегодня заработала?"
    molly "Сегодня не так много... 90 баксов."
    imgd 31968
    ashley "А ты выполнила свои королевские обязанности?"
    molly "Конечно, Эшли..."
    ashley "Молодец, детка."
    molly "Ну ладно, я пошла. Давай, пока."
    # Молли бросает ехидный взгляд на Монику и уходит
    sound highheels_short_walk
    imgf 31969
    w
    # Моника возмущена
    music Pyro_Flow
    imgd 31970
    m "В смысле 'пока'?!"
    m "?!?!?!"
    m "А почему она не заплатила процент от чаевых?"
    music Groove2_85
    ashley "Молли - королева Shiny Hole."
    ashley "Она самая лучшая девочка здесь."
    ashley "Неужели ты думаешь, что я буду брать проценты у нее?"
    music Pyro_Flow
    imgd 31971
    m "Что за бред?!"
    m "Почему я плачу, а эта рыжая стерва все себе забирает?!"
    music Groove2_85
    ashley "Это не бред, [monica_pub_name], а королевская привилегия."
    ashley "Если бы ты поменьше качала тут права и поактивнее работала на сцене..."
    ashley "Твоя попка могла бы занять место Молли."
    ashley "Но пока Молли королева Shiny Hole, она пользуется этой привилегией."
    imgf 31972
    m "!!!"
    ashley "Все, [monica_pub_name]. Хватит. Иди работай!"
    # Эшли уходит
    # Моника стоит злая
    fadeblack 1.5
    music Power_Bots_Loop
    imgf 31973
    mt "Эта охреневшая шлюха все это время не платит процент?!"
    mt "Королевская привилегия?!"
    mt "Какая-то шлюха не платит, а я - Моника Бакфетт, плачу процент?!"
    mt "Потому что, видите-ли, она королева?!"
    mt "БЕСИТ!"
    mt "НЕНАВИЖУ!!!"
    mt "!!!"
    $ monicaMollyBattle1 = True # Моника узнала от Эшли о том, что Молли не платит проценты
    music2 stop
    return

# после этого диалога, другой день
# Моника приходит в гримерку в день, работает Молли
# при клике на Молли
label ep215_dialogues1_pub_2:
    # Моника стоит у двери
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 16130
    mt "Ненавижу эту сучку!"
    mt "!!!"
    # Молли поворачивается к Монике и опять начинает цеплять Монику
    imgf 16132
    w
    sound highheels_short_walk
    imgd 22815
    molly "О, пришла любительница потрясти своим голым задом на сцене!"
    molly "Аха-ха-ха!"
    # Моника зло
    music Power_Bots_Loop
    imgd 22818
    m "Иди в жопу, Молли!"
    # Молли продолжает издеваться
    music Groove2_85
    imgf 19194
    molly "Ты мне просто завидуешь, сучка. Признайся."
    molly "Мне не нужно полностью раздеваться на сцене, чтобы заинтересовать посетителей бара."
    molly "И заработать много чаевых."
    molly "А вот у тебя получается сделать это, только сняв трусы перед всеми!"
    imgd 19195
    sound snd_woman_laugh
    molly "Кстати, зачем они тебе? Может быть ты вообще не будешь носить их?"
    molly "Аха-ха-ха!"
    # Моника злобно на нее смотрит
    music Power_Bots_Loop
    imgd 19196
    mt "Она что, что-то знает?.."
    mt "Нет, не думаю..."
    m "!!!"
    # Молли продолжает веселиться
    music Groove2_85
    imgf 19197
    molly "Поэтому ты и воруешь у меня деньги, сучка!"
    molly "Тебе со мной, королевой Shiny Hole, не сравниться! Никогда!"
    molly "И ты всегда будешь получать жалкие пару долларов за то, что голая кривляешься на сцене!"
    molly "Неудачница!"
    molly "Аха-ха-ха!"
    # Монику бомбит
    music Pyro_Flow
    img 19198 vpunch
    m "Это я неудачница?!"
    m "Ты совсем охренела, стерва?!?!?!!?"
    m "Ты думаешь, раз ты надела корону в этой грязной дыре, куда ходят одни алкаши!.."
    m "То значит ты здесь лучшая?!"
    imgd 19199
    m "Если я только захочу, я с тебя эту корону сниму в два счета!"
    m "Поняла, сучка!!!"
    # Молли язвительно
    music Groove2_85
    imgf 19200
    molly "Если только в твоих снах! Аха-ха!"
    molly "Даже не мечтай об этом!"
    molly "Тебе никогда со мной не сравниться, поняла!"
    # Моника злится
    music Stealth_Groover
    imgd 18225
    mt "Эта сучка с каждым днем все отвратительнее себя ведет!"
    mt "Хабалка! Ненавижу!"
    mt "Не имеющая вкуса, не разбирающаяся в моде дешевая шлюха!"
    mt "Мне нужно поставить эту стерву на место!"
    mt "!!!"
    imgf 19201
    m "Что?! Это мне с тобой не сравниться?!"
    m "Выйди со мной на сцену и мы посмотрим, кто здесь настоящая королева!"
    m "Уверена, это будешь не ты! Даже если разденешься догола!"
    # Молли ведет себя уверенно и с вызовом говорит
    music Groove2_85
    imgd 19202
    molly "Ты хочешь соревноваться на сцене со мной? С самой королевой Shiny Hole?"
    imgd 19203
    m "Да! Или ты боишься потерять свою корону?!"
    sound snd_woman_laugh
    imgf 19195
    molly "Аха-ха-ха!"
    molly "Не смеши меня!"
    molly "Ты же неудачница. Что бы ты на сцене не сделала, ты обречена на провал!"
    molly "Так что мне не о чем переживать, сучка!"
    # Молли отворачивается от Моники к своему зеркалу
    music Stealth_Groover
    imgd 18224
    mt "Мерзкая рыжая стерва!"
    mt "Я сделаю все, чтобы лишить ее короны!"
    mt "Здесь только одна королева - Я, Моника Бакфетт!"
    mt "!!!"
    return

# при клике на Молли после этого диалога
# меню возникает единовременно, пока это событие не произойдет
label ep215_dialogues1_pub_3:
    # Моника стоит у двери
    music Groove2_85
    imgf 22813
    molly "Ну что, сучка?!"
    molly "Тебе не терпится опозориться на сцене?"
    m "!!!"
    $ menu_corruption = [pubMollyBattle1CorruptionRequired]
    menu:
        "Батл с Молли.":
            music Stealth_Groover
            imgd 22814
            m "Опозориться?!"
            m "Сегодня королевой стану Я!!!"
            imgf 16136
            molly "Я на твоем месте не была бы так уверена в этом!"
            molly "Ты вообще себя в зеркало видела?!"
            molly "Аха-ха!"
            music Power_Bots_Loop
            imgd 22823
            mt "ААААААА!"
            mt "Тварь!!!"
            mt "!!!"
            $ monicaMollyBattle2 = True # Моника пошла на 1-й батл с Молли
            pass
        "Не сегодня.":
            music Stealth_Groover
            imgd 22814
            m "Еще чего!"
            m "У меня сегодня нет времени на тебя, сучка."
            music Groove2_85
            imgf 22816
            molly "Правильно, неудачница, иди зарабатываей свои несчастные центы."
            imgd 22820
            molly "И не забудь отдать процент Эшли!"
            molly "Аха-ха!"
            return False
    music Stealth_Groover
    imgf 16138
    m "Да пошла ты, сучка!"
    if monicaPubMollyDanceNude5 == True:
        imgd 22679
        molly "Сучка из нас двоих только одна. Это ТЫ!"
        molly "И ты сама в этом призналась."
        #
        $ notif(_("Моника признала себя сучкой перед Молли."))
        #
    imgd 22679
    m "!!!"
    imgf 16135
    molly "Пойдем, я надеру тебе задницу перед всеми!"
    return True

# Моника и Молли у сцены, обе в жилетах
label ep215_dialogues1_pub_4:
    # Моника ведет себя спокойно, Молли не перестает ее цеплять и ехидничать
    # на сцене они ведут себя также
    sound snd_fabric1
    fadeblack 1.5
    sound highheels_short_walk
    pause 2.0
    music Road_Trip
    music2 pub_noise1_low
    imgfl 31837
    w
    imgf 31838
    molly "Готова к провалу, сучка?!"
#    music Stealth_Groover
    imgd 31839
    m "Заткнись, Молли!"
    m "Сегодня ты останешься без своей короны!"
    music2 stop
    return

# Моника и Молли на сцене
# выигрыш определяется криками толпы и баром
label ep215_dialogues1_pub_5:
    $ musicOrder = [1, 0, 2, 3, 4, 5, 6, 7]
    # Моника ведет себя спокойно, Молли ехидничает и заметно нервничает
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music musicList[musicOrder[0]]["intro"]

#    music Road_Trip
    imgfl 31840
    w
    imgf 31841
    w
    imgd 31842
    molly "Я начну первой, как и подобает королеве Shiny Hole!"
    imgd 31843
    molly "Смотри и учись, неудачница!"
    m "Да пошла ты!"
    # 1-й раунд
    # Молли в одежде, Моника в одежде
    # Молли начинает танцевать первая, делает три движения
    # потом Моника выходит, загораживая ее
#    music musicList[musicOrder[0]]["loop"]
    call pub_dance_battle1_Molly1() from _rcall_pub_dance_battle1_Molly1

    menu:
        "Теперь моя очередь! Я покажу как надо танцевать!":
            pass
    hide screen poledance_shoot
    music musicList[musicOrder[1]]["intro"]
    imgf 31844
    w
    imgd 31845
    w
    imgd 31846
    m "И это все, на что ты способна?!"
    m "Фи!"
    # Моника делает три движения
#    music musicList[musicOrder[1]]["loop"]
    call pub_dance_battle1_Monica1() from _rcall_pub_dance_battle1_Monica1
#    imgf black_screen
#    w

    hide screen poledance_shoot
    fadeblack 1.5
    music musicList[musicOrder[1]]["intro"]
    # по крикам толпы Моника проигрывает, шкала бара у Молли выше
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31847
    ## здесь были правильны мысли Моники о том, почему эти плебеи недовольны и что то нужно предпринять##
    molly "Аха-ха!"
    molly "Поняла!? Уступи место настоящей королеве!"
    menu:
        "Снять корсет.":
            pass
    imgf 31847
    mt "Что этим плебеям еще нужно?!"
    mt "Как они могут отдавать предпочтение этой рыжей корове?!"
    mt "Сейчас я ей устрою!"
    hide screen love_bar_screen_battle
    # 2-й раунд
    # Моника не отходит, а снимает жилет и делает еще три движения
    sound snd_fabric1
    imgd 31848
    w
    imgd 31849
    w

    call pub_dance_battle1_Monica2() from _rcall_pub_dance_battle1_Monica2
#    music musicList[musicOrder[1]]["loop"]
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31850
    w
    # публика кричит ВАУ
    # Молли злится и отталкивает Монику
    hide screen love_bar_screen_battle
    fadeblack 1.5
    music musicList[musicOrder[2]]["intro"]
    imgd 31851
    molly "Иди отсюда, сучка!"
    molly "Сейчас моя очередь!"
    sound vjuh2
    img 31852 hpunch
    m "Давай, покажи свои силиконовые сиськи."
    sound snd_fabric1
    imgd 31853
    molly "Молчи, куда тебе со своими прыщиками до меня?!"
    # Молли тоже снимает жилет и танцует три движения

#    music musicList[musicOrder[2]]["loop"]
    call pub_dance_battle1_Molly2() from _rcall_pub_dance_battle1_Molly2

    # толпа кричит, что Молли королева, шкала бара у Молли выше
    # 3-й раунд

    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31854
    w
    imgd 31855
    mt "Черт! Эта сучка уже второй раз выигрывает!"
    mt "Я не позволю этой дряни обойти меня, Монику Бакфетт!"
    mt "!!!"
    menu:
        "Оттолкнуть сучку и снять трусики! Я должна победить!":
            pass
    hide screen love_bar_screen_battle
    fadeblack 2.0
    music musicList[musicOrder[3]]["intro"]
    # Моника отталкивает Молли, начинает танцевать и снимает трусики
    imgf 31856
    w
    sound vjuh2
    img 31857 hpunch
    w
    imgf 31859
    w
    imgd 31858
    w
    sound Jump1
    imgd 31860
    w
    imgd 31861
    w

#    music musicList[musicOrder[3]]["loop"]
    call pub_dance_battle1_Monica3() from _rcall_pub_dance_battle1_Monica3

    # толпа орет, что Моника королева
    # Моника торжествующе смотрит на Молли
    # Молли злится
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31862
    w
    imgd 31863
    molly "Ах ты дрянь!"
    molly "Думаешь, что покажешь свою голую задницу, как ты привыкла это делать, и обыграешь меня?!"
    molly "Я тебе не позволю этого, сучка!"

    hide screen love_bar_screen_battle
    fadeblack 2.0
    music musicList[musicOrder[4]]["intro"]
    imgf 31864
    w
    sound Jump1
    imgd 31865
    w
    # Молли тоже раздевается, танцует, но выигрыша нет, шкала бара у Моники становится выше
#    music musicList[musicOrder[4]]["loop"]
    call pub_dance_battle1_Molly3() from _rcall_pub_dance_battle1_Molly3


    # Молли зло смотрит на Монику, ее бомбит, Моника спокойна
    # 4-й раунд
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31866
    w
    imgd 31867
    w
    hide screen love_bar_screen_battle
    fadeblack 2.0
    music musicList[musicOrder[5]]["intro"]
    imgf 31868
    molly "Это будет МОЯ победа!"
    molly "И корона только МОЯ!!!"
    # Молли со злостью срывает с себя маску и начинает грязно позировать
    imgf 31869
    w
    sound vjuh2
    imgd 31870
    w

#    music musicList[musicOrder[5]]["loop"]
    call pub_dance_battle1_Molly4() from _rcall_pub_dance_battle1_Molly4

    # толпа орет, что Молли королева, шкала бара у Молли выше, чем у Моники
    # Моника смотрит на нее с отвращением
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31871
    mt "Вот тварь!"
    mt "!!!"
    hide screen love_bar_screen_battle
    menu:
        "Снять маску.":
            fadeblack 2.0
            music Groove2_85
            imgd 31872
            mt "Я не готова снять маску!"
            mt "Вдруг меня кто-то узнает?!"
            mt "Я даже не хочу думать о последствиях!!!"
            mt "!!!"
            pass
        "Не делать этого!":
            fadeblack 2.0
            music Groove2_85
            imgd 31872
            mt "Я не буду делать этого!"
            mt "Это отвратительно и грязно!"
            mt "!!!"
            pass
    # Молли с видом победительницы подходит к Монике
    imgf 31873
    w
    imgd 31874
    molly "Ну что, сучка, уяснила, кто из нас настоящая королева?!"
    molly "Тебя здесь хотят видеть только из-за того..."
    molly "Что ты готова танцевать перед любой публикой с голой задницей!"
    molly "Ради популярности!"
    # Моника злобно на нее смотрит
    music Power_Bots_Loop
    imgf 31875
    m "Ненавижу тебя!"
    m "Подлая сука!!!"
    m "!!!"
    $ money -= monica_strip_tips_today
    $ monica_strip_tips_today = 0
    python:
        for movement in stage_achievements_list:
            check_achievement(movement)

    return

# крики толпы
label ep215_dialogues1_pub_6:
    # 1-й раунд (в одежде) - Молли выигрывает
    customers1 "ВАУ!!! Битва сучек!" # танцует Молли
    customers3 "Охренительно, детка! Ты настоящая королева!" # танцует Молли
    customers2 "Да, рыжая королева! Покрути жопой! Вот так! ДАААА!" # танцует Молли
    customers4 "Давай, раздевайся, крошка!" # танцует Моника
    customers5 "Покажи нам свои сиськи!" # танцует Моника
    # 2-й раунд (в трусиках и масках) - Молли выигрывает
    customers1 "ВАААУ!" # танцует Моника
    customers5 "Потряси своими сиськами для нас! Давай еще!" # танцует Моника
    customers4 "Королева Молли! Покажи класс!" # танцует Молли
    customers3 "ДААА! Настоящая королева Shiny Hole!" # танцует Молли
    customers2 "ДА! Покажи нам свою королевскую попку!!!" # танцует Молли
    # 3-й раунд (только в масках) - Моника выигрывает
    customers5 "Вот она, королева! Охренительно, детка!" # танцует Моника
    customers2 "ДААА! Точно! Она королева!" # танцует Моника
    customers1 "Королева Shiny Hole! А где вторая голая попка?" # танцует Моника
    customers4 "Вау!!! Какая горячая детка!" # танцует Молли
    customers3 "Покажи нам свою киску, крошка!" # танцует Молли
    # 4-й раунд (Молли без маски) - Молли выигрывает
    customers5 "ДААААААА!" # танцует Молли
    customers4 "МОЛЛИ, КРОШКА, ТЫ ЭТО СДЕЛАЛАААААА!" # танцует Молли
    customers3 "МОЯ КОРОЛЕВА!" # танцует Молли
    customers2 "ДААА! КОРОЛЕВА SHINY HOLE!" # танцует Молли
    customers1 "ВАААААУ!" # танцует Молли
    return

# гримерка, после батла
# Моника и Молли стоят вдвоем
label ep215_dialogues1_pub_7:
    # Молли смотрит на Монику и ехидно хихикает
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 19204
    molly "Неудачница!"
    molly "Аха-ха-ха!"
    imgd 19205
    m "Заткнись, сучка!"
    # в гримерку забегает Эшли, она в восторге
    sound man_steps
    imgf 19206
    ashley "Вот это вы устроили!!!"
    ashley "Так держать, девочки!!!"
    ashley "Красотки!!!"
    # Эшли смотрит на Молли
    imgd 19207
    ashley "Молли, детка, сколько заплатили эти денежные мешки?"
    imgf 19208
    molly "Что-то около 150 баксов..."
    imgd 19209
    ashley "Отлично!"
    ashley "Молли, раз ты победила, то забираешь все чаевые, что вы заработали!"
    # Моника возмущенно
    music Power_Bots_Loop
    img 19210 hpunch
    m "ВСЕ?!"
    m "?!!!?!?"
    # Молли ехидно смотрит на Монику
    music Groove2_85
    imgf 19211
    molly "Хорошо, Эшли. Мне же не нужно платить тебе проценты? Все как обычно?"
    music Loved_Up
    imgd 19212
    ashley "Конечно не нужно, крошка!"
    imgd 19213
    ashley "У королевы Shiny Hole есть свои привилегии!"
    # Эшли смотрит на Монику, потом подмигивает Молли и хлопает по попе
    imgf 19214
    ashley "Учись, [monica_pub_name], как нужно зарабатывать деньги!"
    imgd 19215
    w
    sound snd_slap1
    img 19216 vpunch
    w
    imgd 19367
    sound snd_woman_laugh
    molly "Хи-хи-хи!"
    imgd 19368
    w
    sound man_steps
    imgf 19217
    ashley "Королева, не забудь ко мне зайти перед уходом."
    ashley "Я соскучилась по твоей попке."
    # Эшли уходит
    # Моника зло смотрит на Молли
    sound snd_fabric1
    fadeblack 2.0
    music Pyro_Flow
    imgfl 19218
    m "Сучка!"
    # Молли самодовольно
    music Groove2_85
    imgf 19219
    molly "Может я и сучка, но я все заработанные деньги оставляю у себя..."
    # Молли уходит
    # Монику бомбит про себя
    music Pyro_Flow
    imgd 19220
    mt "Почему эта рыжая шлюха не платит проценты Эшли?!"
    mt "А Я должна платить!"
    mt "Еще эта сучка при каждом удобном случае подставлет меня перед Эшли!"
    mt "И я отдаю ей ВЕСЬ СВОЙ ЗАРАБОТОК!!!"
    imgd 19221
    mt "Это несправедливо!!!"
    mt "Почему?!"
    mt "Почему меня оружают эти мерзкие люди?!"
    mt "Почему такая добрая и изысканная натура как я должна страдать из-за них?!"
    mt "!!!"
    mt "Если она мне скажет еще хоть слово!.."
    mt "Я ее убью!!!"
    mt "!!!"
    sound snd_fabric1
    fadeblack 1.5
    return

# при клике на Эшли, когда Моника отдает чаевые в день 1-го батла с Молли
label ep215_dialogues1_pub_8:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 31974
    w
    imgf 31975
    ashley "[monica_pub_name], стой!"
    # Моника зло
    m "Я сегодня ничего не заработала!"
    # Эшли ей игриво
    imgd 31976
    ashley "А я сегодня болела за тебя, [monica_pub_name]..." # подмигивает
    ashley "Если бы ты выиграла, то стала бы королевой Shiny Hole..."
    ashley "А королева вообще не платит чаевые, как это сейчас делает Молли."
    ashley "Конечно, у королевы есть не только привилегии, но и определенные обязанности..." # взгляд на попу Моники
    ashley "Но это уже мелочи."
    music Stealth_Groover
    imgf 31977
    mt "Мне плевать на эти обязанности!"
    mt "Я стану здесь королевой и со мной никто не сможет сравниться!"
    mt "!!!"
    music2 stop
    return

# при условии, что был перый батл с Молли
# след. рабочий день, когда смена Молли
# клик на Молли
label ep215_dialogues1_pub_9:
    # Молли снова начинает цеплять Монику
    music Groove2_85
    imgfl 31924
    w
    imgf 31925
#    molly "Пришла?"
    molly "Я думала, что ты постыдишься выходить на сцену после своего провала!"
    molly "Аха-ха!"
    # Моника злобно
    imgd 31926
    m "!!!"
    molly "Мало того, что неудачница, еще и воровка! Хи-хи!"
    molly "Мне, в отличие от тебя, не нужно платить проценты Эшли..."
    molly "Или воровать чужие деньги. Хи-хи!"
    molly "Давай, иди виляй своей голой жирной задницей, шлюха."
    imgd 31927
    m "!!!"
    menu:
        "Проигнорировать рыжую шлюху!":
            music Stealth_Groover
            imgf 31928
            mt "Я не хочу разговаривать с этой сучкой!"
            mt "Она специально провоцирует меня, чтобы снова подставить перед Эшли!"
            mt "И вообще, Моника!"
            imgd 31929
            mt "Тебе не стоит опускаться до уровня этой тупой провинциалки, которая возомнила из себя королеву!"
            mt "Ты таких, как она, даже к кастингу в свой журнал не допускала!"
            mt "Мерзкая рыжая дрянь!"
            imgf 31930
            m "Иди в жопу, Молли!"
            # не будет доступна ни драка, ни второй батл
            return False
        "Врезать ей!":
            $ monicaMollyBattle3 = True # Моника с Молли дерутся в гримерке - catfight
            pass
    # Монику бомбит, Молли надменно
    music Power_Bots_Loop
    imgd 31931
    m "Ты, сучка! Ты победила только потому что сняла маску и опозорилась перед всем Shiny Hole!"
    m "И ты сверкала своей голой задницей!"
    music Groove2_85
    imgf 31932
    molly "Мою задницу и меня любит весь Shiny Hole."
    molly "Я королева здесь, а ты - жалкая подстилка."
    molly "Твое дело - разносить пиво за пару центов чаевых..."
    imgd 31933
    molly "И ты снова грубо разговариваешь со мной."
    molly "Пожалуй, попрошу Эшли снова заставить тебя просить прощения передо мной."
    molly "Также, попрошу ее повысить процент, который она забирает с твоих чаевых."
    molly "Дешевая уличная шлюха..."
    # Моника в бешенстве
    music Power_Bots_Loop
    img 31934 hpunch
    m "ТВАРЬ!"
    # подбегает к Молли
    return True

# интерактивная сцена драки,
# меню выбора действий Моники в зависимости от бичности
# зациклить драку в одном из пунктов меню
# возможность проиграть или выиграть в зависимости от выбора игрока
label ep215_dialogues1_pub_9_loop1:
    menu:
        "Толкнуть сучку!": # высокая бичность
            music Turbo_Tornado
            imgd 31935
            m "Мерзкая дешевая потаскуха!!!"
            # толкает Молли, та падает со стула
            sound anger2
            imgd 31936
            m "Никчемная шлюха!!!"
            # та вскакивает и толкает Монику в ответ
            sound snd_bodyfall
            img 31937 vpunch
            w
            imgd 31938
            w
            sound Jump1
            imgf 31939
            w
            sound angry_cat1
            imgd 31940
            w
            imgd 31941
            molly "АХ ТЫ ДРЯНЬ!!!"
            menu:
                "Вцепиться в ее волосы!": # высокая бичность
                    # Моника хватает Молли за волосы
                    imgf 31942
                    w
                    imgd 31943
                    w
                    sound vjuh3
                    img 31944 vpunch
                    w
                    imgd 31945
                    m "МЕРЗКАЯ СУКА!!!"
                    sound scream1
                    imgd 31946
                    molly "ААААА!!!"
                    molly "СУЧКАААА!!!"
                    # Молли в ответ хватает Монику за волосы
                    sound vjuh3
                    img 31982 vpunch
                    w
                    sound snd_julia_scream1
                    imgd 31983
                    w
                    imgd 31984
                    w
                    menu:
                        "Ударить эту сучку по груди!": # высокая бичность
                            # Моника бьет Молли по груди
                            imgf 31985
                            m "НЕНАВИЖУ!!!#тебя"
                            # sound anger2
                            imgd 31986
                            w
                            sound snd_punch_face2
                            img 31987 hpunch
                            m "УБЬЮ ТЕБЯ!!!"
                            sound scream3
                            imgd 31988
                            w
                            # Молли ослабляет свою хватку
                            menu:
                                "Врезать ей по лицу!": # высокая бичность
                                    imgf 31989
                                    w
                                    imgd 31990
                                    sound anger2
                                    w
                                    sound snd_punch_face1
                                    img 31991 vpunch
                                    w
                                    sound scream3
                                    imgd 31992
                                    w
                                    sound snd_bodyfall
                                    img 31993 hpunch
                                    w
                                    imgf 31994
                                    w
                                    imgd 31995
                                    w
                                    # Моника с размаху бьет Молли по лицу, та теряет равновесия и падает на пол
                                    # падая, хватается за жилет Моники и срывает его
                                    # Молли на полу, Моника с размаху бьет ее ногой в живот
                                    menu:
                                        "Добить сучку ногами!":
                                            pass
                                    imgf 31996
                                    w
                                    imgd 31997
                                    sound anger2
                                    w
                                    sound Damage3
                                    img 31998 vpunch
                                    m "Получай, шлюха!"
                                    imgd 31997
                                    #sound anger2
                                    w
                                    sound Damage3
                                    img 31998 vpunch
                                    m "Ненавижу!#тебя"
                                    imgd 31997
                                    #sound anger2
                                    w
                                    sound Damage3
                                    img 31998 vpunch
                                    m "Тварь!!!"
                                    # Молли скрючивается от боли, но потом хватает Монику за ногу в момент след удара
                                    # Моника теряет равновесие и падает на пол
                                    sound scream1
                                    imgf 31999
                                    w
                                    imgd 32000
                                    w
                                    sound snd_bodyfall
                                    img 32001 hpunch
                                    w
                                    imgd 32002
                                    w
                                    pass
                                "Толкнуть ее!":
                                    # Моника толкает Молли, та теряет равновесия и падает на пол
                                    imgf 32003
                                    w
                                    imgd 32004
                                    w
                                    # падая, хватается за грудь Моники, срывает жилет
                                    imgd 32005
                                    sound anger2
                                    w
                                    sound snd_bodyfall
                                    img 32006 vpunch
                                    w
                                    # Моника хватается за грудь, а Молли в это время бьет ее по ногам и Моника тоже падает
                                    imgf 32008
                                    w
                                    imgd 32007
                                    sound2 down
                                    #sound anger2
                                    w
                                    sound snd_julia_scream1
                                    imgd 32009
                                    m "АААА!!!"
                                    pass
                            # Моника на полу бьет локтем Молли по лицу
                            sound snd_bodyfall
                            img 32010 vpunch
                            w
                            #sound anger2
                            imgd 32011
                            w
                            menu:
                                "Защититься от сучки!":
                                    pass
                            sound Damage3
                            img 32012 vpunch
                            w
                            # та закрывается от боли
                            sound scream3
                            imgd 32013
                            molly "Сукаааа!!!"
                            molly "Аааа!!!"
                            # Моника лезет на Молли, садится сверху и хватает ее за шею
                            imgf 32014
                            w
                            sound angry_cat1
                            menu:
                                "Вцепиться ей в горло!":
                                    pass
                            #sound anger2
                            img 32015 vpunch
                            w
                            imgf 32016
                            w
                            imgd 32017
                            w
                            # Молли вцепляется ногтями в лицо Моники и сталкивает ее с себя
                            sound snd_punch_face1
                            img 32018 hpunch
                            w
                            imgd 32019
                            sound anger2
                            w
                            sound snd_bodyfall
                            img 32020 vpunch
                            w
                            imgf 32021
                            w
                            imgd 32022
                            w
                            pass
                        "Попытаться увернуться от Молли.": # Моника приличная
                            # Моника пытается увернуться от Молли, которая пытается вцепится в ее волосы
                            imgf 32023
                            w
                            imgd 32024
                            sound anger2
                            m "ААААА!!!"
                            # но Молли хватает ее за волосы, резко опускает ее голову и бьет коленом по лицу
                            sound Damage3
                            img 32025 vpunch
                            molly "Получай, шлюха!"
                            sound snd_julia_scream1
                            imgd 32026
                            w
                            imgd 32027
                            w
                            imgd 32028
                            w
                            sound snd_julia_scream1
                            imgd 32029
                            m "АААААА!!!"
                            menu:
                                "Ударить ее чем-нибудь!":
                                    imgf 32030
                                    #sound anger2
                                    w
                                    # Моника тянется за стулом, но Молли опережает ее и отталкивает Монику
                                    # Моника падает на пол
                                    sound snd_bodyfall
                                    img 32031 vpunch
                                    w
                                    sound angry_cat1
                                    imgd 32032
                                    w
                                    imgd 32033
                                    w
                                    # Молли подбегает к Монике, садится сверху нее и начинает душить
                                    sound vjuh3
                                    imgd 32034
                                    w
                                    imgd 32035
                                    w
                                    imgd 32036
                                    sound anger2
                                    w
                                    imgd 32037
                                    molly "Сукаааа!!!"
                                    imgd 32039
                                    molly "Убью тебяяяяя!!!"
                                    imgd 32038
                                    menu:
                                        "Вцепиться сучке в лицо!":
                                            pass
                                    m "АААА!!!"
                                    # Молли сидит на Монике сверху и душит ее
                                    # Моника вцепляется ногтями в лицо Молли и сталкивает ее с себя
                                    sound snd_punch_face1
                                    img 32040 vpunch
                                    w
                                    imgd 32041
                                    #sound anger2
                                    w
                                    sound snd_bodyfall
                                    img 32042 hpunch
                                    w
                                    imgd 32043
                                    w
                                    pass
                                "Толкнуть ее!":
                                    # Моника толкает Молли, но та бьет Монику по лицу
                                    imgd 32044
                                    w
                                    sound anger2
                                    imgd 32045
                                    w
                                    sound snd_punch_face1
                                    img 32046 hpunch
                                    w
                                    imgd 32047
                                    molly "Сучка!!!"
                                    # Моника падает и хватается за трусы Молли, стаскивает их
                                    imgd 32048
                                    w
                                    sound Jump1
                                    imgd 32049
                                    w
                                    sound snd_bodyfall
                                    img 32050 vpunch
                                    molly "ААА!!!"
                                    imgf 32051
                                    w
                                    # Молли падает вслед за ней, потом быстро садится на Монику сверу и начинает душить
                                    imgd 32033
                                    w
                                    #sound anger2
                                    sound angry_cat1
                                    imgd 32052
                                    w
                                    imgd 32053
                                    w
                                    imgd 32054
                                    w
                                    #sound anger2
                                    imgd 32055
                                    w
                                    imgd 32039
                                    w
                                    imgd 32038
                                    menu:
                                        "Вцепиться сучке в лицо!":
                                            pass
                                    m "АААА!!!"
                                    sound snd_punch_face1
                                    img 32056 vpunch
                                    w
                                    imgd 32057
                                    w
                                    sound snd_bodyfall
                                    img 32058 hpunch
                                    w
                                    sound anger2
                                    imgd 32059
                                    w
                                    imgd 32043
                                    w
                                    pass
                            pass
        "Дать ей пощечину!": # Моника приличная
            music Turbo_Tornado
            imgd 32060
            m "Ах ты дрянь!!!"
            # размахивается и бьет Молли ладонью по лицу
            imgd 32061
            w
            img 32062
            w
            sound snd_punch_face1
            img 32063 hpunch
            w
            #sound anger2
            imgd 32064
            m "Как ты смеешь?!"
            imgf 32065
            molly "Ну все, сучка!"
            molly "Ты за это ответишь!"
            # Молли размахивается и бьет Моника в ответ по лицу кулаком
            # Моника едва удерживается на ногах
            # в шоке смотрит на Молли
            sound anger2
            imgd 32066
            w
            sound down
            img 32067 vpunch
            w
            imgd 31934
            w
            # переход на начальное меню, где доступен пункт "Толкнуть сучку!"
            jump ep215_dialogues1_pub_9_loop1
        "Уйти.":
            music Stealth_Groover
            imgf 31927
            mt "Я не хочу разговаривать с этой сучкой!"
            mt "Она специально провоцирует меня, чтобы снова подставить перед Эшли!"
            sound highheels_short_walk
            imgd 31928
            w
            imgd 31929
            w
            imgf 31930
            m "Иди в жопу, Молли!"
            # Моника уходит
            return 0


    # обе лежат на полу снова вцепившись друг другу в волосы
    # они толкаются, таскают друг друга за волосы
    # тут забегает Эшли и начинает орать на них
    fadeblack
    sound Damage3
    pause 0.5
    sound snd_punch_face1
    pause 0.5
    sound snd_julia_scream1
    pause 0.5
    sound snd_break_dress
    pause 1.5
    music Turbo_Tornado
    imgf 32068
    w
    imgd 32069
    w
    sound man_steps
    imgf 32070
    w
    music Power_Bots_Loop
    img 32071 vpunch
    ashley "А ну-ка хватит!!!"
    ashley "Битву сучек надо устраивать на сцене!"
    ashley "Это, по крайней мере, приносит деньги!"
    ashley "А не устраивать тут драку!"
    imgf 32070
    ashley "Вы что, совсем охренели, такой шум тут подняли!?!?!?"
    # Молли с Моникой, несмотря на крики Эшли продолжают таскать друг друга за волосы
    menu:
        "Врезать сучке коленом в живот!":
            music Turbo_Tornado
            imgd 32072
            w
            imgd 32073
            # Моника пытается пнуть Молли ногой, но у нее не получается
            m "Ненавижу!!!#тебя"
            imgd 32074
            #sound anger2
            # Молли вцепляется ногтями в грудь Моники
            w
            sound down
            img 32075 vpunch
            m "АААА!!!"
            # Моника отпускает Молли и резко отстраняется
            # при этом она задевает Эшли, та теряет равновесие и падает между ними, юбка задирается
            sound snd_julia_scream1
            imgd 32076
            w
            sound scream3
            imgd 32077
            w
            sound snd_bodyfall
            img 32078 hpunch
            w
            imgd 32079
            w
            pass
        "Вцепиться ногтями в ее грудь!": # высокая бичность
            # Моника убирает руки от волос Молли и вцепляется в ее грудь когтями
            music Turbo_Tornado
            imgd 32072
            w
            imgd 32080
            #sound anger2
            w
            sound down
            img 32081 vpunch
            w
            sound scream3
            imgd 32082
            molly "АААААА!!!"
            molly "ТВААААРЬ!!!"
            imgd 32076
            w
            sound scream3
            imgd 32077
            w
            sound snd_bodyfall
            img 32078 hpunch
            w
            imgd 32079
            w
            # Молли отпускает Монику и резко отстраняется
            # при этом она задевает Эшли, та теряет равновесие и падает между ними, юбка задирается
            pass
    # все трое на полу, Эшли пытается выбраться
    imgd 32083
    sound anger2
    w
    img 32084 vpunch
    ashley "Мать вашу!!!"
    # начинают колотить друг друга на полу, один удар перепадает Эшли, которая пытается встать
    # Молли через Эшли пытается дотянуться до лица Моники и расцарапать его
    imgd 32085
    #sound anger2
    w
    sound down
    img 32086 vpunch
    w
    sound Damage3
    img 32087 vpunch
    w
    ## арты будут смотреться если в сопровождении будет звук ударов ##
    sound scream3
    imgd 32088
    w
    menu:
        "Укусить ее!": # Моника приличная
            # в тот момент, когда рука Молли рядом с лицом Моники, Моника зубами вцепляется в ее руку
            # Молли орет
            sound anger2
            img 32089 vpunch
            w
            sound scream3
            imgd 32090
            molly "СУУУУКААА!!! Я ТЕБЕ СЕЙЧАС!!!"
            # Молли облокачивается на Эшли, которая так и не может встать, перегибается через нее и колотит Монику по голове
            #sound anger2
            imgd 32092
            ashley "Дайте мне встать!"
            imgd 32091
            w
            imgd 32093
            #sound anger2
            w
            sound Damage3
            img 32094 vpunch
            m "АААААА!!!"
            # Моника пытается закрываться от ударов
            # Эшли отталкивает с себя Молли, Эшли встает и начинает орать
            sound snd_julia_scream1
            imgd 32092 hpunch
            ashley "Вы совсем охренели?!"
            pass
        "Врезать ей!": # высокая бичность
            # Эшли уже почти удалось встать, но Моника толкает ее локтем, Эшли снова падает
            # Моника цепляется за рубашку Эшли, рубашка задирается (рвется?), грудь Эшли выскакивает наружу
            # Моника облокотившись на груди Эшли начинает колотить Молли куда попало - лицо, голова, грудь
            imgd 32106
            ashley "Дайте мне встать!"
#            w
            #sound anger2
            imgd 32107
            w
            sound snd_punch_face1
            img 32108 vpunch
            w
            imgd 32110
            #sound anger2
            w
            sound Damage3
            img 32109 vpunch
            m "На!"
            m "Получай!"
            imgd 32110
            #sound anger2
            w
            sound Damage3
            img 32109 vpunch
            m "Мразь!"
            m "Тварь!"
            # Эшли отталкивает с себя Монику, Эшли встает и начинает орать
            img 32111 hpunch
            ashley "Вы совсем охренели?!"
            pass
    fadeblack 2.0
    music Power_Bots_Loop
    imgfl 32095
    ashley "Быстро прекратили!"
    ashley "[monica_pub_name]!"
    ashley "Мне что, вызвать полицию, чтобы вас разнять?!"
    # Эшли хватает Монику и поднимает ее на ноги
    music Groove2_85
    imgf 32096
    w
    # Моника злая, как собака, и лохматая, стоит рядом с Эшли, готова набросится на Молли, Эшли ее удерживает
    sound Jump2
    imgd 32097
    ashley "ХВАТИТ!"
    # Молли встает с пола
    imgf 32098
    ashley "[monica_pub_name]!"
    ashley "Молли!"
    ashley "Быстро на сцену! Обе!"
    ashley "Выясняйте отношения там!!!"
    # Моника с Молли зло смотрят друг на друга
    imgd 32099
    m "!!!"
    $ menu_corruption = [pubMollyBattle2CorruptionRequired]
    menu:
        "Батл с Молли.":
            music Pyro_Flow
            imgf 32100
            m "Сегодня я точно надеру тебе задницу, мерзкая шлюха!"
            molly "За свою задницу беспокойся, сучка!"
            imgd 32101
            mt "Тварь!!!"
            mt "!!!"
            $ monicaMollyBattle4 = True # Моника пошла на 2-й батл с Молли
            pass
        "Отказаться.":
            music Pyro_Flow
            imgf 32102
            m "Еще чего!"
            m "С меня достаточно!"
            m "Я не собираюсь делить сцену с этой сучкой!!!"
            molly "Правильно, неудачница, иди зарабатываей свои несчастные центы."
            molly "И не забудь отдать процент Эшли!"
            molly "Аха-ха!"
            # Эшли уходит
            imgd 32103
            ashley "[monica_pub_name], тогда иди быстро на сцену!"
            ashley "Какого черта ты до сих пор тут?!"
            # Моника идет танцевать одна
            # если не идти на батл, а снова кликнуть на Молли, то можно будет повторить сцену драки
            return -2
    music Groove2_85
    imgf 32104
    ashley "Быстро тащите свои задницы на сцену!"
    # Моника с Молли переглядываются зло и идут к выходу с гримерки
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgf 32105
    w
    # Эшли выходит на ними следом
    return 1

# Моника и Молли на сцене
# выигрыш определяется криками толпы и баром
label ep215_dialogues1_pub_10:
    $ musicOrder = [6, 0, 1, 5, 6, 4, 2, 7]
    # Моника ведет себя спокойно, Молли ехидничает и заметно нервничает
    fadeblack
    sound highheels_short_walk
    pause 2.0
#    music Road_Trip
    music musicList[musicOrder[0]]["intro"]
    imgfl 31876
    w
    imgf 31877
    w
    imgd 31878
    molly "У тебя нет шансов победить меня, сучка!"
    imgd 31876
    m "Снова будешь ползать по сцене своей голой задницей, шлюха?"
    molly "Заткнись!!!"
    # 1-й раунд
    # Молли в одежде, Моника в одежде
    # Молли начинает танцевать первая, делает три движения
#    fadeblack 2.0
    imgf 31879
    w
#    music musicList[musicOrder[0]]["loop"]
    call pub_dance_battle1_Molly5() from _rcall_pub_dance_battle1_Molly5

    # потом Моника выходит, загораживая ее
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31880
    menu:
        "Оттолкнуть Молли.":
            pass
    hide screen love_bar_screen_battle
    imgd 31881
    m "Все? Покривлялась, сучка?!"

    fadeblack 2.0
    music musicList[musicOrder[1]]["intro"]

    imgf 31882
    w
    imgd 31883
    m "Иди отсюда!"
    sound Jump2
    img 31884 vpunch
    w
    # Моника делает три движения
#    music musicList[musicOrder[1]]["loop"]
    call pub_dance_battle1_Monica5() from _rcall_pub_dance_battle1_Monica5
#    img black_screen
#    w

    music musicList[musicOrder[1]]["intro"]
    # по крикам толпы Моника проигрывает, шкала бара у Молли выше
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31885
    mt "Не понимаю, эта сучка им что, нравится больше чем Я?!"
#    w
    ## возможно уместны какие-нибудь мысли Моники о том, почему она проигрывает ##
    hide screen love_bar_screen_battle
    imgd 31886
    mt "Нет, я этого не допущу!"
#    w

    imgd 31887
    molly "Моя очередь!"
    molly "Убери свою жирную задницу!"
    menu:
        "Снять корсет.":
            pass
    # 2-й раунд
    # Моника не отходит, а снимает жилет и делает еще три движения
    imgf 31888
    m "Сиди в своем углу, сучка! Я еще не закончила!"
#    w
    sound snd_fabric1
    imgd 31889
    w
    imgd 31890
    w

#    music musicList[musicOrder[1]]["loop"]
    call pub_dance_battle1_Monica6() from _rcall_pub_dance_battle1_Monica6

    fadeblack 2.0
    music musicList[musicOrder[2]]["intro"]
    # Молли злится и отталкивает Монику
    imgf 31891
    w
    imgd 31892
    molly "Убирайся отсюда!"
    molly "Неудачница!"
    sound Jump2
    img 31893 vpunch
    w
    sound snd_fabric1
    imgd 31894
    m "Да пошла ты, жирная корова!"
    # Молли тоже снимает жилет и танцует три движения
#    music musicList[musicOrder[2]]["loop"]
    call pub_dance_battle1_Molly6() from _rcall_pub_dance_battle1_Molly6
    # толпа кричит, что Молли королева, шкала бара у Молли выше
    # 3-й раунд

    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31895
    mt "Ненавижу эту сучку!"
    mt "!!!"
    hide screen love_bar_screen_battle
    ## может какие-нибудь мысли Молли ##
    imgd 31896
    molly "Ну что, шлюха, теперь ты все поняла?"
    w
    imgd 31897
    menu:
        "Оттолкнуть Молли и снять трусики.":
            pass
    mt "Я должна сегодня выиграть эту битву!"
    mt "Иначе я не Моника Бакфетт!!!"
    mt "!!!"

    fadeblack 2.0
    music musicList[musicOrder[3]]["intro"]
    # Моника отталкивает Молли, начинает танцевать и снимает трусики
    imgf 31898
    w
    sound Jump2
    img 31899 vpunch
    w
    imgd 31900
    w
    sound snd_fabric1
    imgf 31901
    w
    imgd 31902
    w

#    music musicList[musicOrder[3]]["loop"]
    call pub_dance_battle1_Monica7() from _rcall_pub_dance_battle1_Monica7

    # толпа орет, что Моника королева
    # Моника торжествующе смотрит на Молли
    # Молли злится

    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31903
    w
    hide screen love_bar_screen_battle
    fadeblack 2.0
    music musicList[musicOrder[4]]["intro"]
    imgd 31904
    molly "Думаешь, ты кого-то удивишь своей голой задницей?!"
    molly "Она здесь всем уже надоела!"
    molly "Аха-ха!"
    # Молли тоже раздевается, танцует, но выигрыша нет, шкала бара у Моники становится выше
    imgf 31905
    w
    imgd 31906
    w
    sound snd_fabric1
    imgd 31907
    w

#    music musicList[musicOrder[4]]["loop"]
    call pub_dance_battle1_Molly7() from _rcall_pub_dance_battle1_Molly7

    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31908
    m "Я лучше тебя, сучка! Ты - никто против меня!"
    imgd 31909
    molly "Рано радуешься, дешевая уличная шлюха!"
    # Молли зло смотрит на Монику, ее бомбит, Моника спокойна
    # 4-й раунд
    imgf 31910
    molly "Ты снова опозорилась, неудачница!!!"
    molly "Грязная воровка!!!"

    hide screen love_bar_screen_battle
    fadeblack 2.0
    music musicList[musicOrder[5]]["intro"]
    # Молли со злостью срывает с себя маску и начинает грязно позировать 3 движения
    imgd 31911
    w
    sound Jump1
    imgd 31912
    w

#    music musicList[musicOrder[5]]["loop"]
    call pub_dance_battle1_Molly8() from _rcall_pub_dance_battle1_Molly8

    # толпа орет, что Молли королева, шкала бара у Молли выше, чем у Моники
    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    imgf 31913
    w
    imgd 31914
    mt "Мерзкая подлая сука!"
    mt "В этот раз я не позволю тебе выиграть!"
    mt "!!!"
    hide screen love_bar_screen_battle
    $ menu_corruption = [pubMollyBattle2TakeOffMaskCorruptionRequired]
    menu:
        "Снять маску!":
            fadeblack 2.0
            music musicList[musicOrder[6]]["intro"]
            imgf 31915
            w
            sound Jump1
            imgd 31916
            mt "К черту эту маску!"
            mt "Никто не сможет узнать Монику Бакфетт в этой дыре!"
            mt "!!!"
            pass
        "Не делать этого!":
            fadeblack 2.0
            music Groove2_85
            imgf 31872
            mt "Я не буду делать этого!"
            mt "Это отвратительно и грязно!"
            mt "!!!"
            # возможность повтора драки и этого батла
            return False
    # Моника выходит вперед, загораживая Молли и снимает с себя маску
    # Моника начинает тоже грязно позировать 3 движения потом встает
    imgf 31917
    w
    # толпа ревет, что Моника королева, шкала бара у Моники на максимуме
    # безоговорочная победа Моники, триумф
    # она стоит посреди сцены, обнаженная и без маски
    # высокомерно смотрит на злую Молли
#    music musicList[musicOrder[6]]["loop"]
    call pub_dance_battle1_Monica8() from _rcall_pub_dance_battle1_Monica8

    show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
    menu:
        "Принимать еще более грязные позы. Я должна быть уверена в победе! Я пойду на все!" if game.extra == True:
#            music musicList[musicOrder[6]]["loop"]
            hide screen love_bar_screen_battle
#            hide screen poledance_shoot
            call pub_dance_battle1_Monica9() from _rcall_pub_dance_battle1_Monica9
        "Принимать еще более грязные позы. Я должна быть уверена в победе! Я пойду на все! (Extra version) (disabled)" if game.extra == False:
            pass
        "Завершить танец.":
            pass

    hide screen poledance_shoot
    hide screen love_bar_screen_battle
    fadeblack 2.0
    music Road_Trip
    imgd 31918
    w
    $ applauseSound = "snd_applause" + str(3)
    sound applauseSound
    imgd 31920
    w
    imgf 31919
    w
    sound highheels_short_walk
    imgd 31921
    w
    imgf 31922
    w
    imgd 31923
    m "Поняла, дрянь, кто из нас королева?!"
    m "Корона теперь моя, а ты никто!"
    molly "!!!"
    python:
        for movement in stage_achievements_list:
            check_achievement(movement)
    # Молли сидит на сцене голая, полулежа, смотрит на Монику снизу вверх, как поверженный враг (на лице отчаяние)
    return True

# Показываем картину с Моникой в гримерке вместо картины с Молли (королева shiny hole)

# гримерка после батла
# Моника вдвоем с Молли
label ep215_dialogues1_pub_11:
    # Моника торжествует, Молли злая и униженная
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 19222
    m "Ну что, сучка?! Что ты скажешь новой королеве Shiny Hole?"
    imgf 19223
    w
    imgd 24353
    w
    molly "Я тебе этого просто так не оставлю!" # смотрит на картину (вид из картины)
    imgd 19224
    m "Ты еще угрожаешь мне, своей королеве?"
    # забегает довольная Эшли, обращается к Монике
    music Groove2_85
    imgf 19225
    ashley "Я всегда знала, что эта попка покорит нашу сцену!"
    ashley "[monica_pub_name], теперь ты новая королева!"
    imgd 31947
    ashley "И чтобы больше никаких драк!!!"
    ashley "Это вас обеих касается! Тебе понятно, Молли?!"
    # Молли зло отвечает
    imgd 31948
    molly "ДА!"
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    # затемнение, Молли оделась
    imgfl 31949
    w
    imgf 31950
    w
    imgd 31951
    w
    imgf 31952
    ashley "С этого дня ты, Молли, должна отдавать мне проценты со своих чаевых."
    ashley "А [monica_pub_name] всю выручку будет забирать себе."
    # Эшли смотрит на Монику игриво
    music Loved_Up
    imgd 31953
    ashley "Это твоя королевская привелегия, [monica_pub_name]..."
    # Эшли кладет руку на ее попу и сжимает ее, Моника делает вид, что не замечает этого
    sound Jump2
    img 31954 vpunch
    w
    imgf 31956
    m "..."
    imgd 31955
    ashley "У королевской попки должны быть королевские чаевые..."
    # Моника все это время высокомерно смотрит на Молли, та молча зло на нее
    imgf 31957
    molly "!!!"
#    m "!!!"

    # держа руку на попе Моники, игриво
    imgd 31958
    ashley "И, Молли, если королева пожалуется мне, то тебе придется извиняться перед ней..."
    # Молли с психом уходит
    imgd 31959
    sound highheels_short_walk
    molly "Рано радуешься, су... королева! Я отомщу тебе!"
    w
    # Эшли пошло подмигивает Монике и тоже выходит
    imgf 31954
    w
    imgd 31960
    w
    # Моника про себя злорадствует
    sound man_steps
    imgf 31961
    w
    music Stealth_Groover
    imgd 31962
    mt "Я сегодня заработала [monica_strip_tips_today] долларов за одно выступление!"
    mt "И ни цента не должна теперь никому отдавать!"
    mt "В отличие от рыжеволосой шлюхи!"
    mt "Так и надо этой сучке! Пусть знает свое место!"
    mt "Неважно где и неважно как, но я всегда была и остаюсь королевой!"
    if monicaBitch == True:
        img 31963
        mt "И никакие жалкие людишки не смогут встать у меня на пути!"
#    $ log1 = _("Теперь корона Shiny Hole принадлежит МНЕ! Я буду пользоваться королевскими привилегиями! А эта сучка Молли теперь никто!") # квест-лог
    return

# в другой рабочий день после 2-го батла Моника заходит в гримерку
# работает Молли
label ep215_dialogues1_pub_12:
    # не рендерить!!
    # Моника смотрит на Молли высокомерно, та на нее зло
    mt "Я не собираюсь с ней разговаривать!"
    mt "Не королевское это дело общаться с плебеями!"
    return False

# в другой рабочий день после 2-го батла Моника заходит в гримерку
# работает Клэр
label ep215_dialogues1_pub_13:
    # Клэр, как обычно, сидит за своим столиком
    music Groove2_85
    imgf 16148
    mt "Интересно, Клэр знает о том, как я поставила рыжую шлюху на место?"
    # Клэр поворачивается к Монике
    imgd 16141
    clare "Моника, привет!"
    img 24353
    clare "Слышала о твоем триумфе! Поздравляю!" # указывает на картину
    imgd 16142
    m "Привет, Клэр!"
    m "Да, я проучила рыжую стерву! Ты бы это видела!"
    imgf 16174
    clare "Я рада, что ты ее проучила и теперь сможешь хоть что-то здесь зарабатывать."
    clare "Но все равно будь аккуратнее с Молли..."
    clare "Она захочет теперь отомстить тебе."
    clare "Если что, ты знаешь, что я всегда готова помочь тебе, Моника."
    imgd 16149
    m "Спасибо, Клэр!"
    return

# при клике на Эшли, когда Моника отдает чаевые после того, как стала королевой
label ep215_dialogues1_pub_14:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 31978
    w
    imgf 31979
    ashley "[monica_pub_name], ты теперь королева Shiny Hole..."
    ashley "И тебе полагается не отдавать мне процент от заработка."
    mt "Наконец-то!!!"
    # Эшли улыбается, облизываясь и смотрит на попу Моники
    music Loved_Up
    imgd 31980
    ashley "Но не забывай про свои королевские обязанности..."
    m "..."
    # подмигивает Монике и уходит
    music Stealth_Groover
    imgf 31981
    mt "Извращенка!"
    mt "Что это еще за королевские обязанности?"
    mt "У королев нет никаких обязанностей!"
    mt "Мне плевать на это, я буду наслаждаться своими королевскими привилегиями!"
    mt "Моника, ты это заслужила!"
    music2 stop
    return

label ep215_dialogues1_pub_14a:
    menu:
        "Снять маску.":
            mt "Я сделала это один раз, когда была зла на Молли, но я пока не готова повторять это..."
            mt "Вдруг меня кто-то узнает..."
            mt "Хотя меня тут все и так обсуждают новую королеву Shiny Hole, но все же..."
            help "В следующих обновлениях!"
            return True
        "Завершить танец.":
            return False
    return False

label ep215_dialogues1_pub_14b:
    imgf 24353
    mt "Боже, Моника, какой кошмар!"
    mt "Я не могу поверить что изображение голой Моники Бакфетт с раздвинутыми ногами висит в какой-то дыре в трущобах!"
    mt "Меня успокаивает только то, что здесь, в этой гримерке, никого не бывает."
    mt "А эти пьяницы в зале неспособны узнать кто я такая на самом деле."
    mt "Когда я верну свое положение назад, я уничтожу эту картину и все это заведение!"
    mt "Ну а пока..."
    mt "Положение королевы этой дыры дает мне возможность забирать все чаевые себе."
    mt "Это мне пригодится для того, чтобы выбраться из этого временного недоумения, в котором я очутилась."
    return



    # 1-й раунд
    # Молли в одежде, Моника в одежде
    # Молли начинает танцевать первая, делает три движения
    # Molly 50
    # потом Моника выходит, загораживая ее
    # Моника делает три движения
    # Monica 30
    # по крикам толпы Моника проигрывает, шкала бара у Молли выше
    # 2-й раунд
    # Моника не отходит, а снимает жилет и делает еще три движения
    # Monica 70
    # публика кричит ВАУ
    # Молли злится и отталкивает Монику
    # Молли тоже снимает жилет и танцует три движения
    # Molly 80
    # толпа кричит, что Молли королева, шкала бара у Молли выше
    # 3-й раунд
    # Моника отталкивает Молли, начинает танцевать и снимает трусики
    # Monica 100
    # толпа орет, что Моника королева
    # Моника торжествующе смотрит на Молли
    # Молли злится
    # Молли тоже раздевается, танцует, но выигрыша нет, шкала бара у Моники становится выше
    # Molly 90
    # Молли зло смотрит на Монику, ее бомбит, Моника спокойна
    # 4-й раунд
    # Молли со злостью срывает с себя маску и начинает грязно позировать
    # Molly 100
    # Monica 50
    # толпа орет, что Молли королева, шкала бара у Молли выше, чем у Моники
    # Моника смотрит на нее с отвращением




    # Молли в одежде, Моника в одежде
    # Молли начинает танцевать первая, делает три движения
    # Molly +30
# потом Моника выходит, загораживая ее
# Моника делает три движения
# Monica + 20
# по крикам толпы Моника проигрывает, шкала бара у Молли выше
# Моника не отходит, а снимает жилет и делает еще три движения
# Monica + 30 (50)
# Молли злится и отталкивает Монику
# Молли тоже снимает жилет и танцует три движения
# Molly +30 (60)
# толпа кричит, что Молли королева, шкала бара у Молли выше
# Моника отталкивает Молли, начинает танцевать и снимает трусики
    # Monica +50 (100)
    # толпа орет, что Моника королева
    # Моника торжествующе смотрит на Молли
    # Молли злится
    # Молли тоже раздевается, танцует, но выигрыша нет, шкала бара у Моники становится выше
    # Molly + 20 (80)
        # Молли зло смотрит на Монику, ее бомбит, Моника спокойна
    # 4-й раунд
    # Молли со злостью срывает с себя маску и начинает грязно позировать 3 движения
    # Molly +30 (100)
    # Monica - 40 (60)
    # толпа орет, что Молли королева, шкала бара у Молли выше, чем у Моники
        # Моника выходит вперед, загораживая Молли и снимает с себя маску
    # Monica +50 (100)
    # Molly - 50 (50)
    # Моника начинает тоже грязно позировать 3 движения потом встает
        # толпа ревет, что Моника королева, шкала бара у Моники на максимуме
    # Monica +50 (100)
    # Molly - 30 (20)
    # безоговорочная победа Моники, триумф
    # она стоит посреди сцены, обнаженная и без маски
    # высокомерно смотрит на злую Молли

# крики толпы, второй батл
label ep215_dialogues1_pub_15:
    customers1 "ВАУ!!! Еще одна битва сучек!" # Molly
    customers2 "Да, рыжая королева! Покрути жопой! Вот так! ДАААА!" # Molly
    customers4 "Давай, раздевайся, крошка!" # Monica
    customers3 "Охренительно, детка! Ты настоящая королева!" # Molly
    customers2 "ДА! Покажи нам свою королевскую попку!!!" # Molly
    # 2-й раунд (в трусиках и масках)
    customers1 "ВАААУ!"  # Monica
    customers5 "О, да! Вот это сиськи!" # Monica
    customers4 "Королева Молли! Покажи класс!" # Molly
    customers3 "ДААА! Настоящая королева Shiny Hole!" # Molly
    customers5 "Давай, покрути своей задницей!" # Monica
    # 3-й раунд (только в масках)
    customers5 "Вот она, королева! Охренительно, детка!" # Monica
    customers2 "ДААА! Точно! Она королева!" # Monica
    customers1 "Вау, детка! У меня уже в штанах дымится! Иди сюда!" # Molly
    customers4 "Пошли в приват, детка!" # Monica
    customers3 "Покажи нам свою киску, крошка!" # Molly
    # 4-й раунд (Молли без маски)
    customers5 "ДААААААА!" # Molly
    customers5 "Королева Молли!" # Molly
    customers4 "Это же [monica_pub_name]!!!" # Monica
    customers1 "ОХРЕНЕЕЕТЬ!!!" # Monica
    customers3 "[monica_pub_name] КОРОЛЕВА! ДААА!!!" # Monica
    customers2 "ДААА! КОРОЛЕВА SHINY HOLE!" # Monica
    return
