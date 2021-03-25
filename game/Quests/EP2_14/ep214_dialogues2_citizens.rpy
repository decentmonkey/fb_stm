default monicaPerryMommyDebt1 = False # Моника дала согласие сделать минет ситизену в подворотне у пилона
default monicaPerryMommyDebt2 = False # Моника укусила ситизена и убежала
default monicaPerryMommyDebt3 = False # у Перри есть фото, где Моника стоит на коленях перед ситизеном
default monicaPerryMommyDebt4 = False # Моника сбежала от Перри
default monicaPerryMommyDebt5 = False # Моника отказалась давать деньги или отрабатывать у Перри
default monicaPerryMommyDebt6 = False # Моника заплатила Перри часть долга
default monicaPerryMommyDebt8 = False # Моника сделала ликинг Перри и осталась в хостеле на ночь
#default monicaPerryMommyDebt9 = False # Моника отдала Мамочке ее долю

default monicaCitizensPunksBlowjob1 = False # Моника согласилась на хенджоб с панками за 15 баксов
default monicaCitizensPunksBlowjob2 = False # Моника облизала мошонку панку за 2 бакса, когда делала минет
default monicaCitizensPunksBlowjob3 = False # Моника позволила Тому засунуть член своими между грудями за 2 бакса, когда делала минет
default monicaCitizensPunksBlowjob4 = False # Моника прогнала Тома и Тима из своей квартиры

default monicaCitizensArtistNudeModel1 = False # Моника согласилась работать моделью ню перед художником
default monicaCitizensArtistNudeModel2 = False # Моника разрешила художнику потрогать свою грудь

default ep214_dialogues2_citizens_9_flag1 = False
default ep214_dialogues2_citizens_11b2_flag = False

default ep214_citizens1_2_cumzone1 = 0
default ep214_citizens1_2_cumzone2 = 0

#call ep214_dialogues2_citizens_1() # сцена с citizen4, появляется Перри, после мамочка
#call ep214_dialogues2_citizens_2() # если убежала от Перри (мысли)
#call ep214_dialogues2_citizens_3() # если сначала убежала, а потом решила вернуться к пилону; если пришла к хостелу отдавать деньги (мысли)
#call ep214_dialogues2_citizens_4() # если убежала, и сразу же хочет вернуться к пилону, мысли
#call ep214_dialogues2_citizens_5() # если укусила ситизена и сбежала (встречи с Перри не было), мысли
#call ep214_dialogues2_citizens_6() # если снова хочет позвать незнакомца, который предлагал $ 100 за минет, к пилону
#call ep214_dialogues2_citizens_7() # если пришла к хостелу отдавать деньги, мысли (глазик)
#call ep214_dialogues2_citizens_8() # зашла в хостел отдавать деньги (в первый раз), диалог с Перри
#call ep214_dialogues2_citizens_9() # зашла в номер хостела, мысли
#call ep214_dialogues2_citizens_10() # душ в хостеле, мысли
#call ep214_dialogues2_citizens_11() # номер в хостеле, Моника ложится спать, мысли
#call ep214_dialogues2_citizens_11a() # номер в хостеле, утро, мысли
#call ep214_dialogues2_citizens_11b() # Моника выходит из номера и идет к выходу, разговор с Перри
#call ep214_dialogues2_citizens_11c() # если делала ликинг Перри, потом сразу ушла из хостела, мысли
#call ep214_dialogues2_citizens_11d() # Моника вернулась в хостел, если сразу после ликинга ушла, разговор с Перри
#call ep214_dialogues2_citizens_12() # если убежала от Перри, не отрабатывая и не отдав деньги, мысли
#call ep214_dialogues2_citizens_13() # если отрабатывала у Перри, но в хостеле не осталась, мысли
#call ep214_dialogues2_citizens_14() # если ночевала в хостеле, мысли
#call ep214_dialogues2_citizens_15() # если заплатила деньги и отказалась отрабатывать, мысли
#call ep214_dialogues2_citizens_16() # подворотня, где пилон, диалог с панками
#call ep214_dialogues2_citizens_17() # апартаменты Моники в трущобах, сцена с панками
#call ep214_dialogues2_citizens_18() # подворотня, где пилон, диалог с художником, потом апартаменты Моники
#call ep214_dialogues2_citizens_20() # Моника пришла на точку с проституток, мысли
#call ep214_dialogues2_citizens_21() # Моника пришла на точку проституток, клик на мамочку
#call ep214_dialogues2_citizens_22() # повторный клик на Мамочку, если уже говорила с ней, мысли


### Перри, мамочка, ситизен

# Моника, приходит в трущобы, чтобы работать у пилона
# подходит к ситизену, который ей платил 50 баксов за показ груди
# обычный диалог, после которого они идут к пилону
# обычное меню с танцами у пилона НЕ появляется

# подворотня, где пилон
label ep214_dialogues2_citizens_1:
    # Моника стоит у пилона, ситизен напротив нее
    help "Этот выбор ведет к прерыванию действий с остальными жителями улицы."
    menu:
        "Продолжить.":
            pass
        "Назад.":
            return -1

    fadeblack 2.0
    music Groove2_85
    imgfl 19038
    w
    imgf 13400
    citizen4 "Ну что, давай начнем."
    if citizen4BoobsShowedFirstTime == True:
        citizen4 "Я бы посмотрел на твои сиськи еще разок."
        #
        $ notif(_("Моника показывала обнаженную грудь за деньги."))
        #
        citizen4 "Но это будет скучно."

    # Моника зло на него смотрит
    imgd 13377
    m "Скучно?!"
    music Stealth_Groover
    imgd 13312
    mt "Вот мерзавец!"
    mt "Как он смеет говорить подобное обо МНЕ?!"
    mt "О такой шикарной женщине, как Я, мечтает любой мужчина!"
    music Groove2_85
    imgf 13373
    citizen4 "Ага. Скучно."
    citizen4 "Я тут подумал..."
    citizen4 "Я провернул небольшое дельце и у меня есть лишние 100 баксов."
    citizen4 "Я мог бы потратить их на тебя."
    citizen4 "Но тебе для этого придется постараться, детка."
    # Моника смотрит на него с подозрением
    imgd 13316
    mt "100 долларов?"
    mt "Хмм.. Было бы неплохо."
    mt "И что хочет этот мерзавец?"
    mt "Мне нужны деньги."
    imgd 13398
    m "И что ты предлагаешь?"
    imgf 13378
    citizen4 "Ты покажешь мне свои голые сиськи."
    citizen4 "И отсосешь у меня."
    music Pyro_Flow
    img 19039 hpunch
    m "Что?!"
    m "За кого ты меня принимаешь?!"
    m "?!?!?!"
    imgd 19040
    mt "Сволочь!"
    mt "Жалкий неудачник!"
    mt "Никчемный!!"
    music Groove2_85
    imgf 13401
    citizen4 "Девочка, ты забыла где ты? В этом районе каждая вторая готова таким образом заработать пару лишних долларов."
    citizen4 "Решайся быстрее, у меня нет времени. Ну дак что?"
    imgd 19041
    mt "Черт!"
    mt "..."
    menu:
        "Ты точно мне заплатишь $ 100?":
            pass
        "Хватит с тебя того, что ты уже видел! (прерывание квеста)":
            music Stealth_Groover
            imgf 13376
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            imgd 13424
            m "Хватит с тебя того, что ты уже видел!"
            return -1
    # Моника в замешательстве
    music Groove2_85
    imgf 13399
    m "Ты точно мне заплатишь $ 100?"
    imgd 19042
    citizen4 "Ага. Вот они." # показывает купюры
    citizen4 "Снимай свою майку и приступай."
    citizen4 "У меня яйца уже дымятся."
    $ menu_corruption = [monicaSlumsFirstBlowjobCorruptionRequired, 0]
    menu:  # коррапшн! 600-?
        "Оголить грудь и сделать минет клиенту.":
            $ monicaPerryMommyDebt1 = True # Моника дала согласие сделать минет ситизену в подворотне у пилона
            pass
        "Хватит с тебя того, что ты уже видел! (прерывание квеста)":
            music Stealth_Groover
            imgf 13376
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            imgd 13424
            m "Хватит с тебя того, что ты уже видел!"
            return -1
    music Groove2_85
    imgf 19043
    mt "Это звучит дико, но мне нужны деньги..."
    mt "Похоже, в этом районе все относятся совершенно нормально к таким вещам..."
    mt "А я нахожусь здесь анонимно..."
    mt "То что здесь происходит никак не связано с жизнью Моники Бакфетт."
    mt "Так что мне нечего стесняться."
    music Stealth_Groover
    imgd 19044
    mt "Мне это глубоко противно, но я отношусь к этому с хладнокровием."
    mt "В конце концов, это ненадолго."
    mt "Моя цель - это вернуть назад мою роскошную жизнь."
    mt "И я не остановлюсь ни перед чем!"
    # клиент расстегивает штаны и достает свой стояк
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 19045
    citizen4 "Ну? Чего стоишь?"
    citizen4 "Или тебе не нужны лишние 100 баксов?"
    citizen4 "Я не люблю долго ждать."
    imgf 19046
    mt "Черт! Черт! Черт!"
    mt "!!!"
    # Моника снимает майку
    sound snd_fabric1
    imgd 19047
    w
    imgf 19048
    w
    imgd 19049
    citizen4 "У тебя неплохие сиськи, детка."
    citizen4 "Осталось проверить, как хорошо ты работаешь ртом."
    citizen4 "Начинай уже!"
    # Моника опускается перед ним на колени, смотрит на член перед своим лицом
    fadeblack 2.0
    music Loved_Up
    imgfl 19050
    w
    imgf 19051
    mt "Моника, я не могу поверить, что ты будешь делать ЭТО!"
    mt "!!!"
    imgd 19052
    citizen4 "Ты собираешься отрабатывать свои 100 баксов?!"
    citizen4 "Мне уже надоело ждать!"
    citizen4 "Открывай свой рот!"
    # Моника зло смотрит на него исподлобья
    menu:
        "Открыть рот.":
            pass
    # открывает рот
    # ситизен хватает ее за голову и входит в ее рот
    imgf 19053
    citizen4 "Давай, соси!"
    imgd 19066
    w
    sound chpok6
    img 19054 vpunch
    citizen4 "Тебе, шлюха, не привыкать делать это за деньги!"
    menu:
        "Укусить его!!! (прерывание квеста)":
            music Pyro_Flow
            imgf 19056
            mt "Это я шлюха?!"
            mt "Мерзкий грязный слизняк!!!"
            # Моника зло смотрит на ситизена и сжимает челюсти на его члене
            sound hlup25
            imgd 19055
            m "!!!"
            # он загибается
            sound Jump1
            imgd 19057
            w
            sound vjuh2
            img 19058
            w
            sound scream_steve3
            img 19059 hpunch
            citizen4 "АААААА!!!"
            citizen4 "ААААААААААААА!!!"
            sound scream_steve3
            imgf 19060
            m "Я не шлюха!"
            m "Ублюдок!!!"
            m "!!!"
            sound scream_steve3
            imgd 19061
            citizen4 "СУКАААААА!!!"
            citizen4 "ААААААААААААА!!!"
            # Моника убегает
            $ questHelp("work_slums_46", False)
            $ monicaPerryMommyDebt2 = True # Моника укусила ситизена и убежала
            return -2
        "Продолжить минет.":
            pass
    # Моника делает минет ситизену
    fadeblack 1.5
    music2 Loved_Up

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Prisoner1_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob1_1 = Movie(play="video/v_Monica_Citizen4_Blowjob1_1.mkv", fps=30)
    show videov_Monica_Citizen4_Blowjob1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19062
    citizen4 "Ааа..."
    imgd 19063
    citizen4 "Глубже давай!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Prisoner1_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob1_2 = Movie(play="video/v_Monica_Citizen4_Blowjob1_2.mkv", fps=30)
    show videov_Monica_Citizen4_Blowjob1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19065
    citizen4 "Вот тааак..."
    imgd 19064
    citizen4 "Ааааа..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Prisoner1_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob1_3 = Movie(play="video/v_Monica_Citizen4_Blowjob1_3.mkv", fps=30)
    show videov_Monica_Citizen4_Blowjob1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Над Моникой нависает Перри (внезапно)
    music2 stop
    music stop
    sound plastinka2
    img 19070 vpunch
    perry "Ах ты сучка!!!"
    # Моника отстраняется от клиента
    sound snd_bodyfall
    music Villainous_Treachery
    img 19071 hpunch
    w
    imgd 19072
    mt "Мое... Мое платье..."
    mt "Это Перри!!!"
    mt "О Боже!!! Нет!!!"
    mt "!!!"
    mt "!!!!!!"
    # Моника потрясенно смотрит на нее, клиент тем временем возмущается
    music Groove2_85
    imgf 19073
    citizen4 "Эй, детка!"
    citizen4 "Ты что, не видишь, чем эта шлюха занимается?"
    citizen4 "Или ты хочешь присоединиться к ней?"
    # Перри орет на него
    music Power_Bots_Loop
    img 19074 vpunch
    perry "Заткнись!"
    perry "Я эту сучку везде ищу!"
    perry "А она тут развлекается с мужиками!"
    music Groove2_85
    imgd 19075
    citizen4 "Эй, полегче!"
    citizen4 "Сейчас она закончит начатое дело и разбирайся с ней."
    citizen4 "Кстати, эта шлюха тут уже давно работает."
    imgd 19076
    perry "Ах ты, дрянь!"
    perry "Я так и думала, что ты проститутка!!!"
    # Перри достает телефон и делает фото
    imgf 19077
#    sound snd_photo_capture
    call photoshop_flash() from _rcall_photoshop_flash_214
    w
    music Power_Bots_Loop
    imgd 19078
    mt "Она меня сфотографировала!!!"
    mt "!!!"
    mt "!!!!!!"
    music Groove2_85
    imgf 19079
    perry "Теперь ты от меня никуда не денешься!"
    perry "По этому фото мои ребята тебя быстро найдут!"
    perry "Когда ты мне отдашь МОИ деньги?!"
    # у Моники шок
    music Power_Bots_Loop
    imgd 19080
    mt "Что мне делать?!"
    mt "?!?!!?!?!!"
    mt "Я ей должна $ 10 000!!!"
    mt "И еще она угрожала мне бандитами!!!"
    mt "ЧТО ДЕЛАТЬ?!?!?!!?"
    $ monicaPerryMommyDebt3 = True # у Перри есть фото, где Моника стоит на коленях перед ситизеном
    menu:
        "МОНИКА, БЕГИ!!! (прерывание квеста)":
            # Моника толкает ситизена, тот падает
            # возможно, задевает Перри и та тоже падает
            music Turbo_Tornado
            imgf 19081
            sound anger2
            w
            sound snd_bodyfall
            img 19082 vpunch
            w
            sound highheels_run2
            imgd 19083
            citizen4 "Твою мать!!!"
            citizen4 "Да ты охренела?!"
            imgd 19084
            perry "Держи ее! Держи!"
            perry "Она воровка!!!"
            # Моника убегает
            $ monicaPerryMommyDebt4 = True # Моника сбежала от Перри
            $ questHelp("work_slums_46", False)
            return -3
        "Попробовать договориться с Перри.":
            pass
    music Pyro_Flow
    imgf 19085
    mt "Дьявол!"
    mt "Не могу же я постоянно скрываться от этой извращенки!"
    mt "И вообще!"
    mt "С чего я должна отдавать ей $ 10 000?!"
    mt "За одну ночь!"
    imgd 19086
    mt "В какой-то занюханной грязной дыре!"
    mt "!!!"
    mt "Эта дрянь напялила МОЕ платье!"
    mt "Весь ее гребаный хостел не стоит той цены, за которую я покупала это платье!"
    # Моника встает и отходит от ситизена, смотрит на Перри
    music Groove2_85
    imgf 19087
    citizen4 "Эй!" # возмущенно
    citizen4 "Ты куда?!"
    citizen4 "Я тебе не заплачу ни цента, пока ты не закончишь!"
    citizen4 "Тебе что, 100 баксов не нужны?"
    music Power_Bots_Loop
    imgd 19088
    m "Хватит с тебя того, что я уже сделала!"
    # Перри орет возмущенно
    imgd 19089
    perry "100 баксов?!"
    perry "Эта проститутка сосет за 100 баксов?!"
    perry "И не отдает мне МОИ деньги!!!"
    # ситизен застегивает штаны
    music Groove2_85
    imgf 19090
    citizen4 "Да пошла ты, шлюха!"
    citizen4 "Даже отсосать нормально не можешь!"
    citizen4 "Пойду найду себе детку, которая за 100 баксов сделает все, что я захочу."
    sound man_steps
    imgd 19091
    w
    # ситизен уходит


#### если Моника сбежала, а потом передумала и вернулась к пилону, то диалог начинается отсюда

label ep214_dialogues2_citizens_1b:
    # Если Моника убегала и ее не было какое-то время
    if monicaPerryMommyDebt4 == True:
        fadeblack
        sound highheels_short_walk
        pause 2.0
        music Villainous_Treachery
        imgfl 19092
        perry "Ага! Вот ты где!"
        perry "Я тебя везде ищу!"

    # Моника и Перри остаются вдвоем
    # Перри снова начинает орать
    fadeblack 1.5
    music Power_Bots_Loop
    imgf 19092
    perry "Ты мне должна $ 50 000, сучка!!!"
    # Моника в шоке

    img 19093 hpunch
    m "!!!"
    m "!!!!!!"
    m "ЧТОООО?!"
    m "$ 10 000!"
    # Перри злорадно
    music Groove2_85
    imgd 19094
    perry "Ага!!!"
    perry "Вот ты и призналась!"
    imgd 19095
    m "Что?! Нет!!"
    m "Какие еще 50 тысяч?!"
    imgf 19096
    perry "Это проценты за то, что мне пришлось тебя искать, сучка!"
    perry "И вообще! Сколько времени уже прошло?!"
    m "Ты забрала мое платье за то, что я переночевала в твоей грязной ночлежке!"
    m "Ты хоть представляешь, сколько оно стоит?!"
    imgd 19097
    perry "Это платье - залог, который ты мне оставила!"
    perry "И ты получишь его только когда отдашь мне МОИ ДЕНЬГИ!!!"
    perry "Ты мне должна 50 000 баксов, сучка!"
    # Моника начинает возмущаться, но прерывается на полсулове
    imgd 19098
    m "Я не..."
    music Pyro_Flow
    m "ЧТО?! СКОЛЬКО?!"
    m "Да ты охренела!"
    m "Речь шла о 10 тысячах!"
    music Groove2_85
    imgf 19099
    perry "Это проценты за то, что ты убежала, не заплатив долг."
    perry "И с каждым днем сумма будет расти!"
    imgd 19100
    m "Иди в жопу, Перри!"
    m "Я не собираюсь тебе ничего отдавать!"
    # появляется мамочка, но кадр берется нижней части ее лица (вначале)
    fadeblack 1.5
    music Master_Disorder
    imgf 19101
    mommy "Ты отдашь эти деньги, девочка..."
    # Моника испуганно смотрит на нее
    music stop
    sound plastinka2
    img 19102 vpunch
    m "?!?!?!"
    # проститутка, которая пришла вместе с мамочкой смотрит на наряд Моники, делая шаг вперед
    music Groove2_85
    imgf 19103
    whore "На ней моя одежда, которую украли, когда я ночевала у тебя в хостеле, Перри."
    # обращается к Монике
    whore "Это ты сделала?!"
    whore "На тебе не только моя одежда, но и мои туфли!"
    music Stealth_Groover
    imgd 19104
    m "Это непотребство ты называешь одеждой?!"
    m "Это тряпки, которые почти ничего не прикрывают!"
    m "Я ее не украла! Я... Я ее позаимствовала!"
    music Groove2_85
    imgf 19105
    perry "Я же вам говорю, что она воровка!"
    imgd 19106
    mt "!!!" # Моника зло смотрит на них
    # мамочка как ни в чем ни бывало спокойно говорит
    music Master_Disorder
    imgf 19107
    mommy "Девочка, ты работаешь в моем районе без согласования со мной."
    # Моника возмущенно
    music Stealth_Groover
    imgd 19108
    m "С какой стати!!"
    m "Это все незаконно!"
    m "Я!"
    m "Я вызову полицию!"
    # мамочка невозмутима
    music Master_Disorder
    imgf 19109
    mommy "За порядком здесь и следит полиция, девочка."
    mommy "А ты нарушаешь порядок..."
    imgd 19110
    mt "Черт!"
    mt "Моника, кого ты обманываешь?"
    mt "Тебе нельзя вызывать полицию!"
    imgf 19111
#    mommy "Ты можешь продолжать работать здесь, если будешь отдавать мне половину."
    mommy "Ты можешь продолжать работать на улице..."
    mommy "Но только вместе с моими девочками, на точке."
    mommy "И будешь отдавать мне половину заработка."
    imgd 19112
    mommy "А также ты выплатишь долг этой уважаемой женщине." # указывает на Перри
    mommy "В противном случае, мы будем вынуждены обратиться к тем, кто следит за порядком здесь..."
    music Power_Bots_Loop
    img 19113 hpunch
    m "ЧТОО?!"
    m "?!?!?"
    m "???!!!!!?!?!?"
    # мамочка спокойно продолжает
    music Master_Disorder
    imgf 19114
#    mommy "И если ты, девочка, будешь себя хорошо вести..."
    mommy "Я даю тебе возможность работать вместе с моими девочками."
    mommy "Там для тебя будет много работы..."
    imgd 19115
    m "Я никогда не буду работать с твоими шлюхами на улице!"
    m "!!!"
    imgf 19116
    mommy "Жизнь непредсказуемая штука, девочка..."
    mommy "И ты в этом убедилась..."
    # мамочка собирается уходить
    imgd 19117
    mommy "Ты знаешь, где меня найти."
    mommy "И не думай, что сможешь что-то скрыть..."
    mommy "Я буду приглядывать за тобой..."
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    # уходит, ее проститутка уходит вмете с ней, бросив на Монику злой взгляд
    # Перри злорадно говорит
    imgfl 19118
    perry "Слышала, воровка, что тебе сказали?"
    perry "Если не хочешь, чтобы я тебе устроила проблемы..."
    perry "Будешь приходить ко мне в хостел и отдавать долг!"
    perry "И чтобы каждую неделю приносила мне МОИ деньги, иначе сумма будет расти! Поняла?"
    sound highheels_short_walk
    imgf 19119
    perry "Сучка!"
    # Перри уходит
    fadeblack 1.5
    music Pyro_Flow
    imgfl 19120
    mt "Вот дьявол!"
    mt "Мало того, что эта стерва забрала МОЕ платье!"
    mt "Так я теперь еще должна отдавать ей долг!"
    mt "Долг в 50 тысяч долларов!"
    mt "50!!"
    mt "!!!"
    music Stealth_Groover
    imgf 19121
    mt "Моника, тебе нужно успокоиться."
    mt "Нет таких проблем, с которыми ты не можешь справиться."
    mt "Ты сильная и умная женщина. И красивая."
    mt "А $ 50 000 - это небольшие деньги для Моники Бакфетт."
    mt "Когда все эти временные трудности закончатся..."
    imgd 19122
    mt "Когда я верну себе свою прежнюю шикарную жизнь..."
    if monicaBitch == True:
        $ notif_monica()
        mt "Я засуну эти деньги Перри в глотку!!!"
    else:
        mt "Я отдам сучке Перри эти деньги."
    mt "..."
    mt "Или найму адвоката, который сделает так, чтобы..."
    mt "Чтобы она мне заплатила сумму, многократно превышающую $ 50 000!"
    mt "Да, точно! За моральный вред, причиненный мне!"
    mt "Именно так я и сделаю!"
    if monicaBitch == True:
        $ notif_monica()
        mt "Буду слушать ее мольбы и просьбы простить ее!"
        mt "Она будет валяться у меня в ногах!"
        mt "Но я не прощу ее! Я никого не прощу из тех мерзавцев, что окружают меня сейчас!!!"
    imgd 19123
    mt "А пока что мне придется отдавать ей деньги!"
    mt "!!!"
    mt "И вообще!"
    mt "С чего эта ненормальная старая шлюха решила, что я буду работать у нее!"
    mt "Что за бред?!"
    mt "Я никогда не соглашусь на такое!!!"
    mt "НИ-КОГ-ДА!!!"
    $ questHelp("work_slums_46", True)
#    $ log1 = _("Теперь мне нужно каждую неделю приносить гребаной Перри деньги в счет оплаты долга. Черт!") # квест-лог
    return 1

# если убежала от Перри, мысли
label ep214_dialogues2_citizens_2:
    # не рендерить!!
    mt "Я не собираюсь отдавать деньги этой ненормальной извращенке!"
    mt "Достаточно того, что эта стерва забрала МОЕ платье!"
    mt "Весь ее гребаный хостел не стоит той цены, за которую я покупала это платье!"
    mt "!!!"
    return

label ep214_dialogues2_citizens_2b:
    perry "Эй! Твое время закончилось!"
    perry "Давай вали отсюда!"
    return


# если Перри сфотографировала Монику с ситизеном, мысли
# + если сначала убежала, а потом решила вернуться к пилону в другой день, мысли
# + если пришла к хостелу отдавать деньги, мысли
label ep214_dialogues2_citizens_3:
    # не рендерить!!
    mt "Эта мерзкая дрянь Перри меня сфотографировала!"
    mt "И еще она угрожала мне бандитами!!!"
    mt "!!!"
    mt "Черт! Мне придется отдавать ей долг частями..."
    return

# если убежала, и сразу же хочет вернуться к пилону, мысли
label ep214_dialogues2_citizens_4:
    # не рендерить!!
    mt "Мне сейчас нельзя туда возвращаться!"
    mt "Не хватало еще мне проблем с этими грязными людишками!"
    mt "У меня есть более важные дела!"
    mt "!!!"
    return False

# если укусила ситизена и сбежала (встречи с Перри не было), мысли
label ep214_dialogues2_citizens_5:
    # не рендерить!!
    mt "Я Леди!!!"
    mt "Я никогда не опущусь до подобной грязи!!"
    mt "Никогда!"
    mt "!!!"
    return

# если снова хочет позвать незнакомца, который предлагал $ 100 за минет, к пилону
label ep214_dialogues2_citizens_6:
    # не рендерить!!
    mt "Этот тот мерзкий тип, который предлагал мне сделать минет за $ 100!"
    mt "Нет! Я пока не хочу подходить к нему!"
    mt "Перри при нем меня обзывала воровкой!"
    mt "Я не хочу, чтобы он задавал мне лишние вопросы."
    mt "В конце концов, это не его дело!"
    mt "!!!"
    return

###
# если хотя бы одну неделю Моника не отрабатывает, то долг увеличивается
# отрабатывай - ликинг за 10 долларов
# если Моника не отрабатывает и не приносит Перри деньги, то долг вырастает на 1000 баксов
# если Моника хочет переночевать в хостеле, то надо отработать у Перри и та ей разрешит остаться на ночь
###

# если пришла к хостелу отдавать деньги, мысли (глазик)
label ep214_dialogues2_citizens_7:
    # не рендерить!!
    mt "Ненавижу эту чертову Перри!"
    mt "Никчемная извращенка!"
    mt "Взорвать бы ее вместе с этой грязной, вонючей ночлежкой!"
    mt "!!!"
    return False

# зашла в хостел отдавать деньги (в первый раз)
label ep214_dialogues2_citizens_8:
    if ep214_slums_monica_perry_talk_count == 0:
        # Моника заходит в хостел, Перри у столика, который служит ресепшном
        fadeblack 1.5
        sound highheels_short_walk
        pause 2.0
        music Groove2_85
        imgfl 19133
        mt "Не могу поверить, что я снова оказалась здесь!"
        mt "Какой кошмар!"
        # подходит к Перри
        sound highheels_short_walk
        imgf 19134
        perry "А, воровка пришла!"
        m "Я не воровка!"
        m "Не называй меня так!"
        imgd 19135
        perry "Я называю вещи своими именами!"
        perry "Ты должна мне 50 00 баксов и не отдаешь их!"
        perry "Значит, ты воровка!"
        music Power_Bots_Loop
        img 19136
        mt "Тварь!"
        mt "!!!"
        music Groove2_85
        imgf 19137
        m "Откуда такая сумма?!"
        m "Я переночевала в этой дыре всего один раз!"
        m "И договаривались мы с тобой всего на $ 10 000!"
        imgd 19138
        perry "Будешь спорить со мной, воровка, твой долг станет 100 000 баксов!"
        perry "Я тебя искала, потратила на это немало времени, а ты скрывалась от меня!"
        #
        $ notif(_("Моника согласилась сделать минет незнакомцу возле пилона."))
        #
        imgd 19138
        perry "При этом работала, отсасывая у прохожих!"
        perry "Короче, я поставила тебя на счетчик. Поэтому теперь ты мне должна 50 000 баксов."
        music Power_Bots_Loop
        imgf 19139
        mt "Мерзкая тупая стерва!"
        mt "Ненавижу ее!"
        mt "!!!"
        music Groove2_85
        imgd 19140
        perry "Ну так что?"
        perry "Ты принесла мне мои 50 000 баксов?"
    else:
    #### отсюда можно сделать регулярный разговор, когда Моника приходит к Перри
    #### + возможность скипнуть это
        fadeblack 1.5
        sound highheels_short_walk
        pause 2.0
        music Groove2_85
        imgfl 19140
        perry "Ты принесла мне остаток долга?"
        perry "$ [ep214_perry_debt]"
        #

    $ ep214_slums_monica_perry_talk_count += 1
    if money < ep214_perry_debt:
        # если денег недостаточно
        imgf 19141
        m "Я сейчас не располагаю такой суммой!"
        imgd 19142
        perry "Либо ты отдаешь мне деньги. Столько, сколько можешь сейчас отдать."
        sound highheels_short_walk
        imgf 19176
        w
        imgd 19177
        perry "Либо отрабатывай!" # раздвигает ноги и задирает юбку
        #
        sound Jump1
        imgd 19143
        mt "!!!"
        imgf 19144
        w
    $ menu_price = [20,0]
    $ menu_corruption = [0, 0, monicaPerryLickingCorruption]
    menu:
        "Отдать Перри часть долга.":
            # Моника смотрит на раздвинувшую ноги Перри с отвращением
            music Pyro_Flow
            imgd 19145
            mt "Отрабатывать?!"
            mt "?!?!?!"
            mt "Нет! Ни за что!"
            mt "Лучше я отдам ей часть моих денег!"
            music Groove2_85
            imgf 19146
            m "Перри, я могу тебе отдать сейчас $ 20."
            perry "Всего 20 баксов?"
            m "Да."
            perry "Ладно, давай."
            fadeblack 1.5
#            sound fx_coins_b3
            $ add_money(-20.0)
            $ ep214_perry_debt -= 20.0
            $ notif(t__("Моника должна Перри" + " $" + str(ep214_perry_debt)))
            $ ep214_slums_monica_paid_money_this_week = True
            pause 2.0
            music Groove2_85
            # Моника отдает ей деньги
            $ monicaPerryMommyDebt6 = True # Моника заплатила Перри часть долга
            imgfl 19147
            perry "Жду тебя {c}через неделю!{/c}"
            perry "Если не придешь, то твой долг увеличится на 1 000 баксов!"
            perry "Поняла меня, воровка?"
            imgf 19148
            mt "Черт!"
            m "Да!"
            # Перри садится на стол, обнажая киску
            imgd 19149
            perry "Может, ты все-таки хочешь полизать мою волосатую киску"
            perry "Я засчитаю за это еще $ 10..."
            perry "И разрешу остаться на одну ночь в моем хостеле. Бесплатно."
            # Моника смотрит с ужасом на киску
            imgf 19150
            m "..."
            $ menu_corruption = [monicaPerryLickingCorruption]
            menu:
                "Отработать.":
                    # Моника в сомнениях
                    music Pyro_Flow
                    imgd 19145
                    mt "Фууу!!!"
                    mt "Как она может предлагать мне подобную гадость?!"
                    mt "?!"
                    music Groove2_85
                    mt "С другой стороны..."
                    imgf 19151
                    mt "Одна ночь в хостеле бесплатно..."
                    mt "И плюс $ 10 к оплате долга..."
                    mt "Моника, неужели ты способна согласиться на такое?!"
                    mt "Но ведь об этом никто не узнает."
                    mt "Зато сумма долга станет меньше и я смогу провести ночь здесь."
                    mt "Черт!"
                    # Перри снова показывает свою киску
                    imgd 19152
                    perry "Ну? Ты надумала?"
                    perry "Давай!"
                    perry "Моя киска уже вся влажная."
                    perry "Иди сюда."
                    m "..."
                    # Моника нерешительно подходит к ней
                    music Stealth_Groover
                    imgf 19153
                    mt "Я это делаю для того, чтобы быстрее расплатиться с этой сучкой."
                    mt "Я хочу поскорее решить этот вопрос и забыть об этом."
                    mt "Когда я верну себе свою власть и деньги, я накажу эту стерву!"
                    imgd 19154
                    mt "Она не только вернет мне все деньги!"
                    mt "Она заплатит значительно более высокую сумму!"
                    mt "За все мои моральные страдания!"
                    # Моника опускается перед Перри на колени и смотирт на ее волосатую киску
                    fadeblack 1.5
                    music Groove2_85
                    imgfl 19157
                    w
                    imgf 19155
                    mt "Как я буду делать ЭТО?"
                    mt "Фу!!!"
                    mt "Меня сейчас стошнит!"
                    imgd 19156
                    perry "Тебе стоило с самого начала согласиться полизать мне киску!"
                    perry "Тогда бы у тебя не было таких долгов! Ха-ха!"
                    perry "Давай скорее!"
                    perry "Мне не терпится почувствовать твой язычок!"
                    mt "!!!"
                    fadeblack 1.0
                    # ликинг
                    music2 Loved_Up
                    imgf 19158
                    w

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_1 = Movie(play="video/v_Monica_Perry_Licking1_1.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_1
                    with fade
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 19159
                    perry "ООООО!"
                    perry "Это чертовски охренительно, детка!"

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_2 = Movie(play="video/v_Monica_Perry_Licking1_2.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_2
                    with fade
                    perry "Но я даже рада что ты такая воровка!"
                    perry "Теперь моя киска будет вылизана на годы вперед! Ха-ха!"
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 19160
                    perry "О даааа!!!"
                    perry "Давай быстрее работай язычком!"
                    imgd 19161
                    w
                    sound lick3
                    imgd 19162
                    mt "Я не могу поверить..."
                    mt "Я - Моника Бакфетт, самая богатая и влиятельная Леди этого города..."

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_3 = Movie(play="video/v_Monica_Perry_Licking1_3.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_3
                    with fade
                    mt "Лижу жуткую волосатую промежность хозяйке какого-то занюханного хостела в трущобах..."
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    sound lick3
                    imgd 19161
                    w
                    sound lick3
                    imgd 19162
                    w
                    sound lick3
                    imgd 19161
                    w
                    sound lick3

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_4 = Movie(play="video/v_Monica_Perry_Licking1_4.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_4
                    with fade
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    music2 stop
                    fadeblack 1.0
                    music2 Loved_Up2
                    imgd 19162
                    perry "Еще быстрее!!"
                    sound lick3
                    imgd 19161
                    w
                    sound lick3
                    imgd 19162
                    w
                    imgf 19163
                    perry "Я скоро кончу!!"

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_5 = Movie(play="video/v_Monica_Perry_Licking1_5.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_5
                    with fade
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # кончает
                    img 19164
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    perry "ТВОЮ МААААТЬ! ДАААА!"
                    img 19165
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound snd_melanie_cum2
                    perry "ООООО!!!"
                    perry "АААААААААА!!!"
                    # затемнение
                    # Моника с отвращением вытирает рот, Перри сидит довольная
                    $ monicaPerryMommyDebt8 = True # Моника сделала ликинг Перри
                    music2 stop
                    fadeblack 1.5
                    music Power_Bots_Loop
                    imgfl 19166
# Monica_Citizen1,2 - 1
                    mt "Это было отвратительно!!!"
                    mt "!!!"
                    mt "Меня тошнит от нее!!!"
                    music Groove2_85
                    imgf 19167
                    perry "Мне кажется, тебе понравилось, детка."
                    m "Нет!"
                    imgd 19168
                    perry "Ха! Зато мне понравилось!"
#            $ add_money(-20.0)
                    $ ep214_perry_debt -= 10.0
                    $ notif(t__("Моника должна Перри" + " $" + str(ep214_perry_debt)))
                    perry "Я засчитываю 10 баксов в счет оплаты долга."
                    perry "И можешь остаться сегодня на ночь в номере."
                    perry "Можешь лизать мою киску хоть каждый день и ночевать здесь, я не против."
                    imgd 19148
                    m "Иди ты в жопу, Перри!!!"
                    m "!!!"
                    if ep214_slums_monnica_licked_perry_first_day == 0:
                        $ ep214_slums_monnica_licked_perry_first_day = day
                    $ ep214_slums_monnica_licked_perry_last_day = day
                    $ ep214_slums_monica_rent_hostel_last_day = day
                    $ ep214_slums_monica_paid_money_this_week = True
                    $ questHelp("hostel_2", True)
                    menu:
                        "Идти в номер хостела.":
                            music Groove2_85
                            imgf 19169
                            m "Куда тут идти, чтобы поспать?!"
                            perry "Иди по коридору, детка!"
                            perry "А я посмотрю, как ты виляешь своей аппетитной попкой!"
                            perry "Аха-ха!"
                            music Power_Bots_Loop
                            imgd 19170
                            mt "!!!!!!!"
                            m "!!!"
                            # Моника уходит в номер
                            return 1
                        "Уйти отсюда!":
                            music Power_Bots_Loop
                            imgf 19136
                            mt "Я не хочу оставаться в этой вонючей дыре!"
                            mt "!!!"
                            #
                            return -1
                    return
                "Нет! Ни за что!":
                    music Pyro_Flow
                    imgd 19154
                    m "Нет! Я не буду делать этого!"
                    m "Достаточно того, что я отдала тебе часть долга!"
                    music Groove2_85
                    imgf 19149
                    perry "Если захочешь остаться в номере хостела на ночь..."
                    perry "Ты знаешь, что нужно сделать."
                    m "Да пошла ты!"
                    # уходит
                    return -4
        "Отдать Перри остаток долга (в будущем обновлении) (disabled)":
            pass
        "Отработать.":
            # отработка
            # Моника в сомнениях
            music Pyro_Flow
            imgd 19145
            mt "Фууу!!!"
            mt "Как она может предлагать мне подобную гадость?!"
            mt "?!"
            music Groove2_85
            mt "С другой стороны..."
            imgf 19151
            mt "Одна ночь в хостеле бесплатно..."
            mt "И плюс $ 10 к оплате долга..."
            mt "Моника, неужели ты способна согласиться на такое?!"
            mt "Но ведь об этом никто не узнает."
            mt "Зато сумма долга станет меньше и я смогу провести ночь здесь."
            mt "Черт!"
            # Перри снова показывает свою киску
            imgd 19152
            perry "Ну? Ты надумала?"
            perry "Давай!"
            perry "Моя киска уже вся влажная."
            perry "Иди сюда."
            m "..."
            # Моника нерешительно подходит к ней
            music Stealth_Groover
            imgf 19153
            mt "Я это делаю для того, чтобы быстрее расплатиться с этой сучкой."
            mt "Я хочу поскорее решить этот вопрос и забыть об этом."
            mt "Когда я верну себе свою власть и деньги, я накажу эту стерву!"
            imgd 19154
            mt "Она не только вернет мне все деньги!"
            mt "Она заплатит значительно более высокую сумму!"
            mt "За все мои моральные страдания!"
            # Моника опускается перед Перри на колени и смотирт на ее волосатую киску
            fadeblack 1.5
            music Groove2_85
            imgfl 19157
            mt "Мое платье... Как я скучаю по нему..."
            perry "Тебе стоило с самого начала согласиться полизать мне киску!"
            perry "Тогда бы у тебя не было таких долгов! Ха-ха!"
            imgf 19155
            mt "Как я буду делать ЭТО?"
            mt "Фу!!!"
            mt "Меня сейчас стошнит!"
            imgd 19156
            perry "Но я даже рада что ты такая воровка!"
            perry "Теперь моя киска будет вылизана на годы вперед! Ха-ха!"
            perry "Давай скорее!"
            perry "Мне не терпится почувствовать твой язычок!"
            mt "!!!"
            # ликинг
            fadeblack 1.0
            music2 Loved_Up
            imgf 19158
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_1 = Movie(play="video/v_Monica_Perry_Licking1_1.mkv", fps=30)
            show videov_Monica_Perry_Licking1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 19159
            perry "ООООО!"
            perry "Это чертовски охренительно, детка!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_2 = Movie(play="video/v_Monica_Perry_Licking1_2.mkv", fps=30)
            show videov_Monica_Perry_Licking1_2
            with fade
            perry "Но я даже рада что ты такая воровка!"
            perry "Теперь моя киска будет вылизана на годы вперед! Ха-ха!"
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 19160
            perry "О даааа!!!"
            perry "Давай быстрее работай язычком!"
            imgd 19161
            w
            sound lick3
            imgd 19162
            mt "Я не могу поверить..."
            mt "Я - Моника Бакфетт, самая богатая и влиятельная Леди этого города..."

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_3 = Movie(play="video/v_Monica_Perry_Licking1_3.mkv", fps=30)
            show videov_Monica_Perry_Licking1_3
            with fade
            mt "Лижу жуткую волосатую промежность хозяйке какого-то занюханного хостела в трущобах..."
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            sound lick3
            imgd 19161
            w
            sound lick3
            imgd 19162
            w
            sound lick3
            imgd 19161
            w
            sound lick3

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_4 = Movie(play="video/v_Monica_Perry_Licking1_4.mkv", fps=30)
            show videov_Monica_Perry_Licking1_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.0
            music2 Loved_Up2
            imgd 19162
            perry "Еще быстрее!!"
            sound lick3
            imgd 19161
            w
            sound lick3
            imgd 19162
            w
            imgf 19163
            perry "Я скоро кончу!!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_5 = Movie(play="video/v_Monica_Perry_Licking1_5.mkv", fps=30)
            show videov_Monica_Perry_Licking1_5
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # кончает
            img 19164
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            perry "ТВОЮ МААААТЬ! ДАААА!"
            img 19165
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound snd_melanie_cum2
            perry "ООООО!!!"
            perry "АААААААААА!!!"
            # затемнение
            # Моника с отвращением вытирает рот, Перри сидит довольная
            $ monicaPerryMommyDebt8 = True # Моника сделала ликинг Перри
            music2 stop
            fadeblack 1.5
            music Power_Bots_Loop
            imgfl 19166
            mt "Это было отвратительно!!!"
            mt "!!!"
            mt "Меня тошнит от нее!!!"
            music Groove2_85
            imgf 19167
            perry "Мне кажется, тебе понравилось, детка."
            m "Нет!"
            imgd 19168
            perry "Ха! Зато мне понравилось!"
            $ notif(t__("Моника должна Перри" + " $" + str(ep214_perry_debt)))
            $ ep214_perry_debt -= 10.0
            perry "Я засчитываю 10 баксов в счет оплаты долга."
            perry "И можешь остаться сегодня на ночь в номере."
            perry "Можешь лизать мою киску хоть каждый день и ночевать здесь, я не против."
            imgd 19148
            m "Иди ты в жопу, Перри!!!"
            m "!!!"
            if ep214_slums_monnica_licked_perry_first_day == 0:
                $ ep214_slums_monnica_licked_perry_first_day = day
            $ ep214_slums_monnica_licked_perry_last_day = day
            $ ep214_slums_monica_rent_hostel_last_day = day
            $ ep214_slums_monica_paid_money_this_week = True
            $ questHelp("hostel_2", True)
            return -3
            pass
        "Уйти!":
            # Моника зло
            music Pyro_Flow
            imgd 19154
            mt "Я не собираюсь отдавать ей деньги, которые я заработала с таким трудом!"
            music Groove2_85
            imgf 19137
            m "У меня нет денег!"
            imgd 19142
            perry "Тогда отрабатывай!" # показывает на свою киску
            fadeblack
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            imgfl 19143
            w
            imgf 19144
            w
            imgd 19145
            w
            music Power_Bots_Loop
            imgd 19171
            m "Нет!"
            m "Я ни за что не буду делать этого!"
            imgf 19172
            perry "Тогда твой долг вырастет на 1 000 баксов!"
            imgd 19173
            m "Пошла ты в жопу, Перри!"
            imgd 19136
            mt "Гребаная извращенка!"
            $ monicaPerryMommyDebt5 = True # Моника отказалась давать деньги или отрабатывать у Перри
            $ questHelp("hostel_2", False, skipIfTrue=True)
            # Моника уходит
            return -2
    return

# если осталась на ночь в хостеле
# зашла в номер хостела
label ep214_dialogues2_citizens_9:
    mt "Ненавижу эту мерзкую сучку Перри!"
    mt "И этот гребаный хостел ненавижу!"
    mt "Грязная вонючая ночлежка! Фу!"

    if ep214_dialogues2_citizens_9_flag1 == False:
        if get_active_objects("Whore1", scene="hostel_bedroom") == False:
            mt "Хорошо, хоть никто здесь не спит сегодня!"
        mt "Мне нужно выспаться, я так устала за сегодняшний день."
        mt "Но сначала мне нужно принять душ."
        mt "После отработки у Перри я чувствую себя грязной!"
        $ ep214_dialogues2_citizens_9_flag1 = True
    return False

# душ в хостеле
label ep214_dialogues2_citizens_10:
    # Моника заходит в душевую
    mt "А вот и душ."
    music snd_shower2
    if day_time == "day":
        imgf 24339
    else:
        imgf 24341
    mt "Душ...."
    mt "Как же хорошо..."
    mt "Мммм..."
    if day_time == "day":
        imgd 24340
    else:
        imgd 24342
    mt "Боже, я сейчас вспомнила, как я тогда напугалась в душе!"
    mt "Эти голые мужчины! Сколько их было? Целая толпа!"
    mt "Страшно представить, что бы они со мной сделали!"
    mt "!!!"
    mt "Моника, тебе нужно быть осторожной, когда ты остаешься здесь!"
    return

label ep214_dialogues2_citizens_10b:
    # выходит из душа
    mt "Все, хватит думать о плохом!"
    mt "Я хочу поскорее лечь спать..."
    return

# номер в хостеле, Моника ложится спать
label ep214_dialogues2_citizens_11:
    # Моника подходит к кровати
    mt "Отвратительная кровать!"
    mt "Как представлю, что на ней спали какие-то мерзкие людишки..."
    mt "Фи!"
    mt "Я достойна лучшего!"
    return

label ep214_dialogues2_citizens_11b2:
    # Моника ложится на кровать
    if ep214_dialogues2_citizens_11b2_flag == False:
        mt "Моника, ты со всем справишься!"
        mt "Ты умная, сильная, красивая и независимая женщина!"
        mt "Тебе по плечу любые трудности!"
        mt "Тот день, когда ты себе вернешь свою роскошную жизнь, все ближе."
        mt "И ты забудешь и этот ужасный хостел..."
        mt "И эту никчемную мерзкую Перри..."
        mt "И эту старую шлюху Мамочку..."
        mt "Ты забудешь всех этих неудачников как страшный сон."
        $ ep214_dialogues2_citizens_11b2_flag = True
    return

# номер в хостеле, утро
label ep214_dialogues2_citizens_11a:
    $ hostelReceptionPerrySuffix = 1
    $ autorun_to_object("ep214_dialogues2_citizens_11a2", scene="hostel_bedroom")
    return

label ep214_dialogues2_citizens_11a2:
    # Моника проснулась
    # не рендерить
    mt "Я совсем не выспалась..."
    mt "Ужасно жесткая и неудобная кровать!"
    mt "И этот шум с улицы! Кошмар!"
    mt "Хочу уйти отсюда поскорее!"
    return

# хостел, ресепшн
label ep214_dialogues2_citizens_11b:
    # Моника выходит из номера и идет к выходу
    # Перри на ресепшне
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19134
    perry "Жду тебя не позже, чем {c}через неделю!{/c}"
    perry "Если не придешь, то твой долг увеличится на 1 000 баксов!"
    perry "Но если захочешь бесплатно ночевать здесь..." # пошло улыбаясь
    perry "Ты можешь прийти и полизать мою киску. Аха-ха!"
    perry "10 баксов в счет оплаты долга и бесплатная ночевка."
    imgf 19137
    m "Да пошла ты!"
    imgd 19148
    mt "Мерзкая извращенка!!!"
    mt "!!!"
    # Моника уходит
    return

# если делала ликинг Перри, потом сразу ушла из хостела
# улица возле хостела
label ep214_dialogues2_citizens_11c:
    # Моника хочет снова зайти в хостел
    mt "Эта извращенка Перри сказала, что я могу остаться на ночь здесь..."
    mt "Я, конечно, ненавижу это место!"
    mt "И не хочу лишний раз встречаться с Перри!"
    mt "Но почему бы мне не остаться здесь на ночь бесплатно?"
    mt "Тем более, что я уже отработала у Перри!"
    return

# если делала ликинг Перри, потом сразу ушла из хостела
# хостел, ресепшн
label ep214_dialogues2_citizens_11d:
    # Моника заходит в хостел
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19169
    perry "А, детка, ты уже соскучилась по моей волосатой киске?"
    m "Да пошла ты, Перри!"
    m "Ты сказала, что я могу переночевать здесь бесплатно!"
    imgf 19168
    perry "Ладно, ты сегодня хорошо поработала своим язычком..."
    perry "Поэтому можешь остаться."
    imgd 19148
    m "Куда тут идти, чтобы поспать?!"
    imgf 19193
    perry "Иди по коридору, детка!"
    perry "А я посмотрю, как ты виляешь своей аппетитной попкой!"
    perry "Аха-ха!"
    imgd 19170
    m "!!!"
    return


# если убежала от Перри, не отрабатывая и не отдав деньги, мысли
# улица возле хостела
label ep214_dialogues2_citizens_12:
    # не рендерить!!
    mt "Я не собираюсь платить этой мерзкой сучке ни цента!"
    mt "Она говорит, что долг увеличится на $ 1 000?"
    mt "Мне все равно!"
    mt "Пошла она к черту!!!"
    mt "!!!"
    return

# если отрабатывала у Перри, но в хостеле не осталась, мысли
# улица возле хостела
label ep214_dialogues2_citizens_13:
    # не рендерить!!
    mt "Боже! Моника, не могу поверить, что ты сделала ЭТО!"
    mt "Какой кошмар!"
    mt "!!!"
    mt "С другой стороны, сумма долга уменьшилась."
    mt "А это значит, что я смогу быстрее расплатиться с этой сучкой Перри!"
    mt "Ненавижу ее!!!"
    mt "!!!"
    return

# если ночевала в хостеле, мысли
# улица возле хостела
label ep214_dialogues2_citizens_14:
    # не рендерить!!
    mt "Боже, какое кошмарное место!"
    mt "Но с другой стороны, я могу ночевать здесь бесплатно."
    mt "Для этого мне достаточно договориться с извращенкой Перри."
    mt "О том, как эта договоренность происходит, я не хочу даже думать! Фу!"
    return

# если заплатила деньги и отказалась отрабатывать, мысли
# улица возле хостела
label ep214_dialogues2_citizens_15:
    # не рендерить!!
    mt "Фу!"
    mt "Как она может предлагать мне подобную гадость?!"
    mt "Грязная никчемная извращенка!"
    mt "Ненавижу ее!"
    return

label ep214_dialogues2_citizens_15b:
    if monicaLastPissedDay == day and monicaLastPissedDayTime == day_time:
        mt "Я уже писала недавно. Я пока не хочу."
        return
    if cloth == "Whore":
        if day_time == "day":
            imgf 24337
        else:
            imgf 24338
    sound snd_piss
    mt "Жуткое место..."
    mt "Но я видела места и похуже..."
    mt "Не верю в то что это происходит..."
    return

### сцены с панками и художником, процент для Мамочки
# эти сцены активны только:
# если Моника должна платить деньги Мамочке и Перри
# и если Моника арендует шикарный апартамент у продавца кебабов

# Моника, приходит в трущобы, чтобы работать у пилона
# подходит к панкам
# обычный диалог, после которого они идут к пилону
# к обычному меню с танцами у пилона добавляется новый пункт "Сделать им хенджоб."

# подворотня, где пилон
label ep214_dialogues2_citizens_16:
#    menu:
#        "Пригласить к себе.":
#            pass
    # Моника стоит у пилона, панки напротив нее
    music Groove2_85
    imgf 11745
    citizen1 "Эй, у нас для тебя предложение есть!"
    citizen2 "Ага!"
    # Моника подозрительно
    imgd 11769
    mt "Что эти два никчемных недоумка от меня хотят?"
    imgf 11745
    m "Что за предложение?"
    citizen1 "Мы с Тимом теперь чуваки с деньгами."
    # Тим злорадно
    imgd 31690
    citizen2 "Зато те два школьника-ботана теперь без денег. Ха-ха-ха!" # смех
    sound male_laugh2a
    citizen1 "Ха-ха-ха!!!"
    mt "Идиоты!"
    mt "!!!"
    imgf 11768
    citizen2 "Короче, теть. Слушай."
    citizen2 "Я и Том можем стать твоими постоянными клиентами!"
    citizen1 "Да! Теперь мы будем не просто смотреть на твои сиськи."
    citizen2 "Мы хотим большего!"
    m "..."
    menu:
        "Что вам от меня нужно?":
            pass
        "Хватит с вас того, что вы уже видели! (прерывание квеста)":
            music Pyro_Flow
            imgd 11769
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            m "Хватит с вас того, что вы уже видели!"
            return False
    # Моника все так же подозрительно смотрит на них
    music Groove2_85
    imgd 11793
    mt "Какие-то они сегодня подозрительные..."
    mt "Трезвые что-ли?"
    mt "Чего им нужно?"
    mt "Они пытаются обмануть меня?"
    # Моника требовательно
    imgf 11770
    m "Вы чего от меня хотите?!"
    citizen2 "Мы с Томом хотим тебя!"
    music Power_Bots_Loop
    m "В смысле?!"
    m "Вы за кого меня принимате?!"
    m "Я не занимаюсь подобными вещами!!!"
    music Groove2_85
    imgd 11792
    citizen1 "Эй-эй, полегче, теть!"
    citizen1 "Мы за все заплатим!"
    m "Я не собираюсь терпеть домогательства двух придурков за несколько баксов!"
    imgd 11790
    citizen2 "А мы тебе предлагаем не несколько баксов."
    citizen2 "Мы тебе заплатим целых 15 баксов!"
    citizen1 "А ты нам подрочишь!"
    citizen2 "Дааа!!"
#    m "Что?!"
    mt "!!!"
    $ menu_corruption = [monicaCitizen1_2_HandjobCorruptionRequired]
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if slumsApartmentsRentActive == False:
                music Groove2_85
                imgf 13193
                mt "А если кто-то увидит?!"
                mt "Хммм..."
                mt "Может быть..."
                mt "А что, если я сделаю это, но не здесь..."
                mt "Черт! Но мне больше некуда пойти!"
                mt "А здесь я это делать не собираюсь!"
                music Pyro_Flow
                imgd 11794
                m "Нет! Я не собираюсь делать это!!"
                m "За 15 баксов можете дрочить друг у друга!"
                $ notif(t_("Монике некуда вести клиентов."))
                return False
            # если арендует квартиру у Джека
#            if monicaShawarmaApartment5 == True and monicaShawarmaApartment9 == False:
            $ monicaCitizensPunksBlowjob1 = True # Моника согласилась на хенджоб с панками за 15 баксов
        "Хватит с вас того, что вы уже видели!":
            music Stealth_Groover
            imgf 13193
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            imgd 11794
            m "Нет! Я никогда на подобное не соглашусь!!"
            m "Друг другу подрочите за 15 баксов!"
            return False
    # Моника в сомнениях
    music Pyro_Flow
    imgf 19040
    mt "Вот дьявол!"
    mt "Если я им откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."

    #
    $ notif(_("Мамочка запретила Монике работать с клиентами на улице."))
    music Master_Disorder
    imgd 10583
#    mt "Мне итак придется половину отдать этой старой шлюхе!"
    mt "А вдруг эта старая шлюха узнает, что я работаю тут?!"
    mt "?!?!?!"
    mt "Моника, что же делать?"
    #
    $ notif(_("Моника должна выплачивать Перри долг в размере $ 50 000."))
    mt "А ведь мне еще нужно выплачивать долг этой мерзкой извращенке Перри!"
    #

    if ep212_escort_monica_fired == True:
        # если Монику выгнали с эскорта
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
#    music Groove2_85
    imgf 10580
    mt "Моника..."
    mt "Неужели ты способна сделать то, что они просят?"
    mt "Тем более, здесь!"
    mt "!!!"
    imgd 11992
    mt "А если старая карга узнает об этом?!"
    mt "Хммм..."
    music Stealth_Groover
    mt "Может быть..."
    mt "А что, если я сделаю это, но не здесь..."
    imgd 11910
    mt "А в той ужасной дыре, которую я арендую у придурка Джека?!"
    mt "Эта дыра вполне подходит для таких мерзких идиотов!"
    mt "По-моему, Моника, это неплохая мысль."
    mt "Там тебя точно никто не увидит!"
    mt "И ты сможешь заработать денег!"
    # панки нетерпеливо
    music Groove2_85
    imgf 13195
    citizen2 "Эй, теть! Ты чего тормозишь?"
    m "Я не буду делать этого здесь!"
    citizen1 "А, так вот в чем проблема?!"
    citizen1 "Пошли к нашему братану на хату!"
    citizen2 "Ха, точно!"
    citizen2 "Может, ему тоже захочется, чтоб ты ему подрочила!"
    # Моника зло
    music Stealth_Groover
    imgd 13196
    m "Нет!"
    m "Вообще-то, у меня есть место..."
    m "И можно пойти туда..."
    m "Только мне нужно быть увереной, что вы мне заплатите!"
    m "Покажите деньги!"
    music Groove2_85
    citizen1 "Без проблем, теть!"
    # показывают купюры
    sound vjuh3
    imgd 31691
    citizen2 "Пошли! Нам еще пивка надо купить по дороге."
    citizen1 "Дааа, чувак! Нас ждет охренительный вечер! Ха-ха!"
    return

# апартаменты Моники в трущобах
label ep214_dialogues2_citizens_17:
    # Моника стоит посреди своей комнаты, панки оглядываются
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 31692
    w
    imgf 31693
    citizen1 "Эй, теть!"
    citizen1 "Ты эту хату снимаешь, чтоб работать тут?"
    m "Нет!!"
    m "!!!"
    imgd 31694
    citizen2 "Не, Том. Ты дебил?"
    citizen2 "Она работает, показывая сиськи у пилона за 2 бакса."
    citizen2 "А эту хату ей дал ее сутенер, чтоб она сюда водила важных клиентов, таких как мы."
    citizen2 "Так что это не ее хата. Здесь раньше работала какая-то другая шлюха."
    citizen1 "Ты откуда знаешь?"
    citizen2 "Мне братан рассказывал про хату, где он трахал ту шлюху."
    citizen2 "Сказал, что прям на обоях написано 'Fuck', а на стене рыба висит."
    citizen1 "Рыба?!"
    citizen2 "Ага, смотри, Том!"
    # Том оглядывается и смотрит на рыбу
    imgf 31695
    citizen1 "Аха-ха-ха!!!"
    sound male_laugh4
    citizen1 "Что это за хрень?!"
    citizen2 "Ха-ха-ха!"
    imgd 31696
    m "Ничего смешного!"
    citizen1 "Аха-ха-ха!!!"
    sound male_laugh2a
    citizen1 "Тим, дай свою бутылку из-под пива!"
    citizen1 "Спорим, попаду в эту рыбу отсюда?"
    music Power_Bots_Loop
    m "Не смей делать этого!"
    m "Я откажусь с вами работать!"
    m "!!!"
    music Groove2_85
    citizen2 "Тихо, чувак. Слышишь, что она говорит?"
    citizen2 "Не переживай, теть. Я бутылку еще по дороге выкинул."
    citizen2 "В следующий раз покидаем, Том."
    music Turbo_Tornado
    imgf 31697
    citizen2 "Лучше смотри, какая тут кровать! Ха-ха!"
    citizen2 "Сколько тут мужиков у тебя было, теть?"
    citizen2 "50 было? Или больше?"
    citizen2 "Сейчас 51 будет!"
    # запрыгивает на кровать в обуви, начинает прыгать на ней
    sound Jump1
    img 31698 vpunch
    w
    sound Jump1
    img 31699 vpunch
    citizen2 "Дааа!"
    citizen2 "Аха-ха-ха!!!"
#    music Power_Bots_Loop
    imgd 31700
    m "ТЫ ЧТО ДЕЛАЕШЬ?!"
    m "КРЕТИН!!!"
    m "!!!"
    m "Быстро слезь с моей кровати!!!"
    m "!!!"
    # с кровати прыгает в сторону кресла, через столик
    # опрокидывает кресло и сам падает
    sound Jump1
    img 31701
    w
    sound snd_bodyfall
    sound2 snd_heavy_papers_drop
    img 31702 vpunch
    citizen2 "Ха-ха-ха!!!"
    citizen1 "Аха-ха-ха!!!"
    sound male_laugh2a
    citizen1 "Вот ты дебил, Тим!!! Ха-ха-ха!!!"
#    sound male_laugh4
    citizen1 "Теть, а прикольно тут у тебя! Ха-ха!"
    # Тим поугарал и встает с пола
    imgf 31703
    citizen1 "Да! Мы теперь твои постоянные клиенты и будем почаще приходить к тебе!"
    music Power_Bots_Loop
    m "Вы мне тут сейчас все сломаете, идиоты!"
    m "Мне не нужны такие постоянные клиенты!"
    m "!!!"
    m "!!!!!!"
    music Groove2_85
    imgd 31704
    sound snd_cardboard2
    citizen2 "Слышь, Том, если мы что-то сломаем, сутенер накажет нашу тетю."
    citizen2 "Давай, не будем ее подставлять?"
    imgf 31703
    citizen1 "А я бы сломал, Тим. А потом посмотрел, как он ее наказывает."
    citizen2 "Аха-ха-ха!!!"
#    sound male_laugh2a
    citizen1 "Как он это делает, теть, а?"
    citizen1 "Раскладывает тебя прямо на этой кровати, да? Ха-ха!"
    music Power_Bots_Loop
    m "У меня нет никакого сутенера!"
    imgd 31705
    mt "Боже!"
    mt "Зачем я только связалась с этими тупыми придурками?!"
    mt "!!!"
    music Groove2_85
    imgf 31706
    citizen1 "Ладно, ладно."
    citizen1 "Все. Я себя буду вести хорошо."
    citizen1 "Мы же сюда пришли не за этим."
    citizen1 "Давай начнем, теть?"
    music Turbo_Tornado
    imgd 31707
    citizen2 "Подожди! Я сначала отлить хочу."
    citizen1 "Эй! Я тоже!"
    imgd 31708
    citizen1 "Давай, ты пойдешь отольешь в туалете, а я - на кухню в раковину."
    citizen2 "Не, давай я тогда здесь в окно!"
    citizen2 "Давай бросим жребий, кто куда!"
    # бросают жребий камень-ножницы-бумага
    imgf 31709
    citizen1 "Камень, ножницы, бумага..."
    # Моника прерывает их, ее бомбит
    music Power_Bots_Loop
    img 31710 hpunch
    m "ВЫ ОХРЕНЕЛИ?!"
    m "Только попробуй пойти на кухню или к окну!"
    m "По очереди сходите в туалет, недоумки!!!"
    m "!!!"
    music Groove2_85
    imgd 31711
    citizen2 "Да ладно тебе, теть!"
    citizen2 "Не твоя же хата!"
    # Моника орет
    music Power_Bots_Loop
    imgf 31712
    m "Кретины!!!"
    mt "ААААА!!!"
    mt "Бесят!!!"
    imgd 31713
    mt "!!!"
    # citizen2 бежит к окну, citizen1 выбегает из комнаты
    music Turbo_Tornado
    imgd 31714
    sound gretta_jone_run
    citizen2 "Аха-ха-ха!!!"
    sound male_laugh2a
    citizen1 "Аха-ха!!!"
    mt "ТВОЮ МААААТЬ!"
    img 31715
    m "Эй, ты куда?!"
#    fadeblack 1.5
    imgf black_screen
    sound highheels_run2
    pause 2.0
    music Turbo_Tornado
#    music Pyro_Flow
    # Моника бежит за тем, кто пошел отливать в раковину на кухне
    # кухня
    # забегает на кухню, тот стоит и расстегивает ширинку
    imgf 31717
    w
    sound anger2
    imgd 31718
    m "!!!"
    m "Пошел отсюда на хрен!!!"
    # толкает его от раковины
    citizen1 "Ай!"
    citizen1 "Больно же!"
    # Моника размахивается и лупит еще раз
    sound snd_punch_face1
    img 31719 hpunch
    citizen1 "АЙ!!!"
    citizen2 "Все-все!"
    citizen2 "Теть! Ай!"
    citizen1 "Я же пошутил! Ты чего сразу дерешься?!"
    # убегает от нее в комнату
    imgf 31716
    sound run2
    w
    music Pyro_Flow
    imgd 31720
    mt "Бесполезные!"
    mt "Никчемные!"
    mt "Отбросы общества!"
    mt "Ненавижу!!!"
    mt "!!!"
    # Моника выходит из кухни
    # комната
    # в комнате стоят оба панка
    fadeblack
    sound highheels_run2
    pause 2.0
    music Power_Bots_Loop
    imgfl 31722
    w
    imgf 31721
    m "Да, это не моя квартира! Это квартира сутенера!!!"
    m "Еще что-нибудь сделате и я позвоню ему, чтоб он вас отсюда вышвырнул!!!"
    m "И учтите, он заберет все ваши деньги за мое время, потраченное на вас!"
    music Groove2_85
    # панки слушаются
    citizen2 "Все-все-все!"
    citizen2 "Не надо никому звонить, теть."
    citizen1 "Мы так больше не будем!"
    citizen1 "Мы просто пошутили!"
    # Моника возвращается в комнату и про себя злится
    music Power_Bots_Loop
    imgd 31723
    mt "Чертовы идиоты!"
    mt "Гребаные кретины!"
    mt "ААААА!!!"
    mt "!!!"
    mt "Так, Моника!"
    mt "Успокойся!"
    music Stealth_Groover
    imgd 31724
    mt "Этой грязной дыре хуже уже не будет."
    mt "А тебе нужно возвращать назад свою прошлую жизнь!"
    mt "А для этого нужны деньги!"
    mt "Поэтому твоя цель - заработать их!"
    mt "!!!"
    # Тим и Том смотрят на нее
    music Groove2_85
    imgf 31725
    citizen2 "Теть?"
    citizen1 "Мы готовы."
    citizen1 "Начнем?"
    music Power_Bots_Loop
    imgd 31726
    m "Нет!" # зло
    m "За то, что вы здесь устроили, я не буду работать с вами за 15 баксов!"
    m "!!!"
    music Groove2_85
    citizen1 "Мы заплатим тебе больше, теть."
    citizen2 "Да, я купил пива, но у меня еще остались деньги."
    imgd 31727
    citizen1 "Сколько там у тебя осталось?"
    citizen2 "Я могу еще 5 баксов добавить."
    citizen2 "Что насчет 20 баксов, теть?"
    menu:
        "Деньги вперед!":
            pass
        "Прогнать придурков!!!":
            music Pyro_Flow
            imgf 31723
            mt "Нет!"
            mt "Я не собираюсь терпеть этих кретинов ни за какие деньги!"
            imgd 31805
            m "Пошли вон отсюда, придурки!!!"
            citizen1 "Да ладно тебе, теть!"
            citizen2 "Что мы такого сделали?!"
            music Power_Bots_Loop
            m "ВОН ОТСЮДА!" # орет на них
            m "БЫСТРО!!!"
            m "!!!"
            $ monicaCitizensPunksBlowjob4 = True # Моника прогнала Тома и Тима из своей квартиры
            return False
    music Stealth_Groover
    imgf 31723
    mt "Я не верю этим придуркам!"
    mt "Что, если они меня обманут?"
    imgd 31725
    m "Я сделаю, что вы хотите, но при условии, что сначала вы отдадите мне деньги!"
    music Groove2_85
    citizen1 "Нее, теть!"
    citizen2 "За дураков нас принимаешь?"
    citizen1 "Давай, половину сейчас, а половину после работы!"
    citizen2 "Да! По-другому никак, теть!"
    m "10 долларов сейчас, 10 долларов после работы."
    sound vjuh3
    imgf 31728
    citizen1 "Ага!"
    $ add_money(10.0)
    citizen2 "Держи 10 баксов."
    citizen2 "Том, я первый!"
    # расстегивает штаны и достает член
    fadeblack
    sound snd_zip
    pause 1.5
    music Groove2_85
    imgfl 31729
    citizen2 "Только теть, раз 20 баксов, то ты работаешь не рукой, а ртом!"
    m "Еще чего!"
    m "Я не собираюсь делать минет и тебе, и ему за $ 20!"
    citizen1 "Тогда Тиму минет, а для меня поработаешь рукой, теть."
    citizen2 "Давай уже начнем, а?"
    sound snd_zip
    imgf 31730
    citizen2 "Смотри, как он хочет к тебе в рот!"
    # указывает на свой стояк
    # второй панк тоже достает свой член
#    citizen1 "А мой стояк хочет, чтобы ты его потрогала рукой!"
    # Моника зло смотрит на них
    music Stealth_Groover
    imgd 31723
    mt "Черт!"
#    mt "Из этих 20 долларов мне половину придется отдать старой карге!"
#    mt "Мне останется всего 10!"
    mt "Терпеть такое из-за $ 20?!"
    mt "!!!"
    imgd 31724
    mt "Но это лучше, чем вообще ничего..."
    mt "На эти деньги можно купить целых 10 кебабов..."
    mt "..."
    music Turbo_Tornado
    imgf 31731
    citizen1 "Эй! Я тоже хочу, чтобы она отсосала мне!"
    citizen2 "Нет мне!"
    citizen1 "Это в прошлый раз покупал пиво!"
    citizen2 "А я покупал вкусную рыбу! Ха-ха!"
    citizen1 "Ладно, пусть тетя сама решает кому из нас сосать, а кому дрочить!"
    citizen1 "Все-равно она выберет меня!"
    citizen2 "Ха-ха! Вот увидишь, она выберет сосать у меня!"
    music Groove2_85
    imgd 31732
    mt "Какие же эти кретины мерзкие! Фу!"
    mt "Скорее бы уже их отсюда прогнать!"
    $ monicaCitizensPunksBlowjob2 = False
    $ monicaCitizensPunksBlowjob3 = False
    menu:
        "Встать на колени и взять в рот член Тима.":
            # Моника встает на колени перед Тимом
            fadeblack
            sound snd_fabric1
            pause 1.5
            sound highheels_short_walk
            pause 2.0
            music Loved_Up
            imgfl 31733
            w
            imgf 31734
            citizen2 "О, даа!"
            citizen2 "Теперь возьми его в рот."
            ## тут Моника может и посопротивляться!!
            imgd 31735
            mt "Гребаные придурки!"
            mt "!!!"
            mt "Черт! Моника!"
            mt "Никогда бы не подумала, что ты окажешься в такой ситуации!"
            mt "!!!"
            # Моника выполняет
            # Моника делает минет Тиму
            # Том стоит сбоку от них и дрочит
            fadeblack 1.5
            music2 Loved_Up
            sound chpok6
            img 31736 vpunch
            w
            imgd 31737
            citizen1 "Эй, теть!"
            citizen1 "А я?!"
            citizen1 "Давай дрочи мне!"
            menu:
                "Взять член Тома в руку.":
                    pass
            # Моника берет его в руку и начинает водить туда-сюда

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob1_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob1_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31738
            citizen1 "Тееееть, круто!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob1_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob1_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob1_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31739
            citizen2 "Дааа!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob1_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob1_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob1_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.0
            music Groove2_85
            imgf 31740
            citizen2 "Покажи свои сиськи!"
            citizen2 "Снимай майку!"
            citizen2 "Я доплачу еще 1 бакс!"
            citizen1 "Давай, снимай!"
            citizen1 "Заработаешь 21 бакс!"
            imgd 31741
            mt "Черт!"
            mt "!!!"
            menu:
                "Снять одежду.":
                    pass
            # Моника снимает майку
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Loved_Up
            imgfl 31742
            w
            imgf 31743
            citizen2 "Да!!!"
            citizen2 "Прикольные сиськи!!!"
            imgd 31744
            citizen1 "Давай работай дальше!"
            # Моника берет член в рот, а второго держит за член рукой
            # минет и хэнджоб двоим одновременно
            fadeblack 1.5
            music2 Loved_Up
            sound chpok6
            img 31745 vpunch
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob2_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob2_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob2_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31746
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob2_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob2_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob2_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob2_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob2_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob2_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31747
            citizen2 "А теперь выпусти мой ствол изо рта."
            citizen2 "Оближи мои яйца."
            # Моника выпускает член, возмущенно
            music2 stop
            fadeblack 1.5
            music Groove2_85
            imgd 31748
            m "Я не буду этого делать!"
            citizen2 "Я доплачу еще 2 бакса. Заработаешь 23 бакса."
            citizen2 "Ну же. Давай."
            mt "Черт!"
            menu:
                "Лизать яйца Тима.":
                    music Groove2_85
                    imgf 31743
                    mt "Фу! Я никогда такого не делала!"
                    mt "!!!"
                    mt "С другой стороны, он готов доплатить за это..."
                    mt "А мне нужны деньги..."
                    # Моника облизывает его мошонку
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 31749
                    citizen2 "Оооо!!!"
                    sound lick3
                    imgf 31750
                    w
                    sound lick3
                    imgd 31751
                    w
                    sound lick3
                    imgd 31750
                    w
                    sound lick3
                    imgd 31751
                    w
                    sound lick3
                    imgd 31750
                    w
                    sound lick3
                    imgd 31751
                    w
                    sound lick3
                    imgd 31750
                    w
                    sound lick3
                    imgd 31751
                    citizen2 "Прикольноооо!!!"
                    imgf 31752
                    citizen2 "Дааа!!!"
                    citizen2 "А теперь соси дальше!"
                    # Моника берет член в рот
                    $ monicaCitizensPunksBlowjob2 = True # Моника облизала мошонку панку за 2 бакса, когда делала минет
                    pass
                "Нет!":
                    music Power_Bots_Loop
                    imgf 31743
                    mt "Я не собираюсь ему все облизывать!"
                    mt "Фу!"
                    mt "Тем более, за 2 доллара!"
                    music Groove2_85
                    imgd 31753
                    m "Нет!"
                    m "Только минет!"
                    citizen2 "Тогда давай, продолжай!"
                    citizen2 "И бери его поглубже!"
                    # Моника снова берет у него в рот
                    pass
            fadeblack 1.5
            music Loved_Up2
            imgfl 31754
            citizen2 "Оооо, охренительно!!!"
            imgf 31756
            w
            sound drkanje5
            imgd 31755
            w
            imgd 31756
            w
            sound drkanje5
            imgd 31755
            w
            imgd 31756
            w
            sound drkanje5
            imgd 31755
            w
            imgd 31756
            w
            sound drkanje5
            imgd 31755
            citizen1 "Оооох, твою мать! Кончу сейчас!"
            img 31757
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan5
            citizen2 "ОООО!!!"
            citizen1 "ОООО, кончаю!!!"
            menu:
                "Кончить в рот Моники.":
                    # один кончает Монике в рот, второй на руку
                    img 31758
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen2 "ДАААА..."
                    citizen2 "АААА КААААЙФ!!!"
                    citizen1 "АААААААА!!!"
                    # Моника зло смотрит то на одного, то на второго
                    imgd 31759
                    w
                    imgf 31760
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
                    $ ep214_citizens1_2_cumzone1 = 1
                    pass
                "Кончить на лицо Моники.":
                    # один кончает Монике на лицо, второй на руку
                    img 31761
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen2 "ДАААА..."
                    citizen2 "АААА КААААЙФ!!!"
                    citizen1 "АААААААА!!!"
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31762
                    w
                    imgf 31760
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
                    $ ep214_citizens1_2_cumzone1 = 2
                    pass
                "Кончить на грудь Моники.":
                    # один кончает Монике на грудь, второй на руку
                    img 31763
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen2 "ДАААА..."
                    citizen2 "АААА КААААЙФ!!!"
                    citizen1 "АААААААА!!!"
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31764
                    w
                    imgf 31760
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
                    $ ep214_citizens1_2_cumzone1 = 3
                    pass
            music Groove2_85
            imgd 31765
            sound snd_punch_face2
            citizen2 "Это так крутоооо, тееееть!"
            citizen1 "Дааа!!!"
            citizen1 "Надо было не покупать пиво."
            citizen1 "Сейчас она и мне отсосала бы."
            citizen1 "В следующий раз она сосать будет у меня!"
            citizen2 "Договорились, чувак."
            pass

        "Встать на колени и взять в рот член Тома. (in Extra version) (disabled)" if game.extra != True:
            pass
        "Встать на колени и взять в рот член Тома." if game.extra == True:
            # Моника встает на колени перед Томом
            fadeblack
            sound snd_fabric1
            pause 1.5
            sound highheels_short_walk
            pause 2.0
            music Loved_Up
            imgfl 31766
            w
            imgf 31767
            citizen1 "Давай, тетя, начинай!"
            citizen1 "Этот член не будет сосаться сам!"
            # Моника выполняет
            # Моника делает минет Тому
            # Тим стоит сбоку от них и дрочит
            fadeblack 1.5
            music Loved_Up
            imgf 31770
            w
            sound chpok6
            imgf 31768
            w
            imgd 31769
            w
            imgf 31771
            citizen2 "Вот черт! А мой член?"
            citizen1 "Твой член в пролете, Тим! Ха-ха!"
            citizen2 "Тогда дрочи мне!"
            citizen2 "Так не честно! Я тоже заплатил деньги!"

            menu:
                "Взять член Тима в руку.":
                    pass
            # Моника берет его в руку и начинает водить туда-сюда
            # дописать сцену
            fadeblack 1.5
            music2 Loved_Up
            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31772
            citizen1 "Аааа! Это чертовски охренительно, чувак!"
            citizen2 "Дааа, чувак!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_4 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_4.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.0
            music Groove2_85
            imgf 31774
            citizen2 "Эй, теть, а сиськи?!"
            citizen2 "Снимай майку!"
            citizen2 "Я доплачу еще 1 бакс!"
            citizen1 "Давай, снимай!"
            imgd 31773
            mt "Черт!"
            mt "!!!"
            menu:
                "Снять одежду.":
                    pass
            # Моника снимает майку
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 31777
            w
            imgf 31775
            w
            imgd 31776
            citizen1 "Сиськи что надо!"
            citizen2 "Да!!!"
            citizen2 "В следующий раз будешь работать не рукой, а сиськами!"
            citizen2 "После того, как отсосешь у меня! Ха-ха!"
            mt "!!!"
            # Моника берет член в рот, а второго держит за член рукой
            # минет и хэнджоб двоим одновременно
            fadeblack 1.0
            music2 Loved_Up

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgfl 31778
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31779
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31780
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_4= Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_4.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_5 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_5.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_5
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31781
            citizen1 "Эй, теть!"
            citizen1 "Давай я засуну свой член между твоими сиськами."
            citizen2 "Это я придумал!"
            citizen1 "Тим, заткнись!"
            citizen1 "В следующий раз рот и сиськи тети будут работать для тебя!"
            # Моника выпускает член, возмущенно
            music2 stop
            fadeblack 1.5
            music Groove2_85
            imgf 31782
            m "Я не буду этого делать!"
            citizen1 "Да ладно тебе!"
            citizen1 "Я же только потрогаю их немного."
            citizen1 "Зато доплачу еще 2 бакса. Заработаешь 23 бакса."
            citizen1 "Ну же. Давай."
            mt "Черт!"
            menu:
                "Согласиться.":
                    music Groove2_85
                    imgd 31776
                    mt "Фу! Я не хочу, чтоб он прикасался к моей груди!"
                    mt "!!!"
                    mt "С другой стороны, он готов доплатить за это..."
                    mt "А мне нужны деньги..."
                    # Моника злобно на него смотрит
                    imgd 31783
                    m "Только быстро!"
                    # Том немного приседает, обхватывает груди Моникик руками и засовывает между ними член
                    music Loved_Up
                    imgf 31784
                    w
                    imgd 31785
                    w
                    # она в это время продолжает дрочить Тиму
                    imgf 31786
                    w
                    # Том делает несколько движение членом между грудями Моники
                    imgd 31787
                    w
                    imgd 31788
                    w
                    sound drkanje5
                    imgd 31787
                    w
                    imgd 31788
                    w
                    sound drkanje5
                    imgd 31787
                    w
                    imgd 31788
                    w
                    sound drkanje5
                    imgd 31787
                    w
                    imgd 31788
                    citizen2 "Оооо!!!"
                    citizen1 "Какие сиськииии!!!"
                    citizen1 "Охренеееть!!!"
                    imgf 31789
                    mt "Гребаные придурки!"
                    mt "!!!"
                    mt "Черт! Моника!"
                    mt "Никогда бы не подумала, что ты окажешься в такой ситуации!"
                    mt "!!!"
                    ## можно и эмоцию Моники какую-нибудь про этих панков
                    # потом отпускает грудь и направляет член ей в рот
                    imgd 31790
                    citizen1 "А теперь соси дальше!"
                    # Моника берет член в рот
                    $ monicaCitizensPunksBlowjob3 = True # Моника позволила Тому засунуть член между своими грудями за 2 бакса, когда делала минет
                    pass
                "Нет!":
                    music Power_Bots_Loop
                    imgd 31776
                    mt "Я не хочу, чтоб он прикасался к моей груди!"
                    mt "Своим грязным вонючим отростком!"
                    mt "Фу!"
                    mt "Тем более, за 2 доллара!"
                    music Groove2_85
                    imgf 31783
                    m "Нет!"
                    m "Только минет!"
                    citizen1 "Тогда давай, продолжай!"
                    citizen1 "И бери его поглубже!"
                    # Моника снова берет у него в рот
                    pass
            fadeblack 1.5
            music Loved_Up2
            img 31791 vpunch
            w
            sound drkanje5
            imgd 31792
            w
            imgd 31791
            w
            sound drkanje5
            imgd 31792
            w
            imgd 31791
            w
            sound drkanje5
            imgd 31792
            w
            imgd 31791
            w
            sound drkanje5
            imgd 31792
            citizen1 "Оооо, охренительно!!!"
            citizen1 "Оооох, твою мать! Кончу сейчас!"
            imgf 31793
            mt "Не могу поверить что я делаю это..."
            mt "Двум грязным панкам в какой-то дыре в трущобах..."
            img 31794
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan8
            citizen2 "Я тоже!"
            citizen2 "ОООО!!!"
            citizen1 "Аааа, кончаю!!!"
            menu:
                "Кончить в рот Моники.":
                    # один кончает Монике в рот, второй на руку
                    img 31795
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan5
                    citizen1 "АААААААА!!!"
                    citizen1 "КААААЙФ!!!"
                    citizen2 "ДАААА..."
                    # Моника зло смотрит то на одного, то на второго
                    imgd 31796
                    w
                    imgf 31797
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
                    $ ep214_citizens1_2_cumzone2 = 1
                    pass
                "Кончить на лицо Моники.":
                    # один кончает Монике на лицо, второй на руку
                    img 31798
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan5
                    citizen1 "АААААААА!!!"
                    citizen1 "КААААЙФ!!!"
                    citizen2 "ДАААА..."
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31799
                    w
                    imgf 31797
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
                    $ ep214_citizens1_2_cumzone2 = 2
                    pass
                "Кончить на грудь Моники.":
                    # один кончает Монике на грудь, второй на руку
                    img 31800
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan5
                    citizen1 "АААААААА!!!"
                    citizen1 "КААААЙФ!!!"
                    citizen2 "ДАААА..."
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31801
                    w
                    imgf 31797
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
                    $ ep214_citizens1_2_cumzone2 = 3
                    pass
            music Groove2_85
            imgd 31802
            citizen1 "Это было крутоооо, тееееть!"
            citizen2 "Дааа!!!"
            citizen2 "В следующий раз она сосать будет у меня!"
            citizen1 "Или у нас двоих!"
            citizen1 "!!!"
            pass
    # Моника зло на них смотрит, вытираясь рукой
    music Pyro_Flow
    imgf 31803
    mt "Никакого следующего раза не будет!"
    mt "Два никчемных идиота!"
    mt "Что бы я еще раз пустила в свою квартиру кого-то!!!"
    mt "Ни за что!!!"
    # затемнение
    # комната Моники
    # все стоят одетые, панки довольные, Моника злая
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85

    if monicaCitizensPunksBlowjob2 == True or monicaCitizensPunksBlowjob3 == True:
        imgfl 31804
        citizen1 "Это было круто, теть!"
        ## они же отдали ей уже 10 баксов
        $ add_money(13.0)
        citizen2 "Вот твои 13 баксов."
        citizen2 "Итого ты заработала 23 бакса, теть!"
    else:
        imgfl 31804
        citizen1 "Это было круто, теть!"
        $ add_money(11.0)
        citizen2 "Вот твои 11 баксов."
        citizen2 "Итого ты заработала 21 бакс, теть!"

    # дают ей деньги
    imgf 31725
    citizen2 "Как насчет того, чтобы отсосать у двоих сразу! Аха-ха!"
    sound male_laugh2a
    citizen1 "Надо будет братану нашему рассказать."
    citizen1 "Он уже был на этой хате с другой шлюхой."
    citizen1 "По-любому захочет тоже прийти с нами!"
    music Pyro_Flow
    imgd 31726
    m "Что?!"
    m "?!?!?!"
    m "Я больше никого сюда не пущу!"
    m "После того, что вы здесь устроили!"
    music Groove2_85
    imgf 31805
    sound man_steps
    citizen2 "Да ладно тебе, теть!"
    citizen2 "Давай, до следующей нашей встречи!"
    # уходят
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.5
    music Power_Bots_Loop
    imgfl 31806
    mt "Мерзкие тупые придурки!!!"
    mt "Безмозглые никчемные кретины!!!"
    mt "Свиньи!!!"
    mt "Не хочу их больше видеть у себя в квартире!!!"
    mt "Ненавижу их!!!"
    mt "!!!"
    return True

label ep214_dialogues2_citizens_17b:
    mt "Мерзкие тупые придурки!!!"
    return

label ep214_dialogues2_citizens_17c:
    mt "Очередной извращенец..."
    return

label ep214_dialogues2_citizens_17d:
    mt "Мне надо найти укромное место, где эта старая карга меня не найдет..."
    return


# Моника, приходит в трущобы, чтобы работать у пилона
# подходит к художнику
# обычный диалог, после которого они идут к пилону
# к обычному меню с танцами у пилона добавляется новый пункт "Работать моделью."

# подворотня, где пилон
label ep214_dialogues2_citizens_18:
#    menu:
#        "Работа натурщицой.":
#            pass
    # Моника стоит у пилона, художник напротив нее
    music Groove2_85
    imgf 12055
    citizen7 "Хочу предложить тебе работу, но для начала я должен кое-что проверить..."
    citizen7 "Тебя интересует?"
    imgd 13515
    mt "Да какую работу может предложить такой как ты?!"
    menu:
        "Что ты предлагаешь?":
            pass
    imgf 13511
    m "Что ты предлагаешь?"
    imgd 13514
    citizen7 "Да! Я знал, что тебя заинтересует!"
    citizen7 "Для начала, я тебя поздравляю! Ты скоро станешь знаменитой! И тебя будет узнавать любой на этой улице!"
    music Power_Bots_Loop
    imgd 11968
    mt "Ну уж нет!"
    mt "Такой популярности мне не нужно!"
    mt "!!!"
    music Groove2_85
    imgf 13528
    citizen7 "Теперь к делу."
    citizen7 "Мне нужно написать портрет с натуры..."
    citizen7 "И ты - идеальная модель для этого!"
    citizen7 "Я тебе заплачу за то, что ты будешь моей моделью!"
    # Моника с подозрением
    imgd 13529
    m "Просто моделью?"
    m "И больше ничего?"
    imgd 13510
    citizen7 "Да!"
    citizen7 "Ты просто будешь позировать для меня!"
    menu:
        "Сколько ты мне заплатишь?":
            pass
    music Groove2_85
    m "Сколько ты мне заплатишь за эту работу?"
    citizen7 "Я заплачу тебе целых $ 10 долларов!"
    imgf 13580
    mt "Хмм..."
    mt "$ 10 за то, чтобы просто позировать ему..."
    mt "Это намного легче, чем общаться у пилона со всякими неудачниками..."
    mt "Да еще и за какие-то несчастные несколько баксов!"
    m "Ты будешь писать свою картину здесь, у пилона?"
    imgd 12057
    citizen7 "У меня пока нет своей студии."
    citizen7 "А шум улице мешает мне сосредоточиться."
    citizen7 "Так что, если ты сможешь найти подходящее место, то сможешь заработать хорошие деньги!"
    $ menu_corruption = [monicaCitizen7_NudeArtCorruptionRequired]
    menu:
        "Согласиться.":
            # если нет аренды квартиры
            if slumsApartmentsRentActive == False:
                music Groove2_85
                imgf 12062
                mt "Черт! Но мне больше некуда пойти!"
                mt "А здесь я это делать не собираюсь!"
                m "Я не знаю никаких подходящих мест!"
                $ notif(t_("Монике некуда вести клиентов."))
                return -2
            # если арендует квартиру у Джека
#            if monicaShawarmaApartment5 == True and monicaShawarmaApartment9 == False:
#                pass
        "Отказаться.":
            music Stealth_Groover
            imgf 19174
            mt "Я не собираюсь работать моделью для какого-то никчемного художника!"
            mt "Я не хочу, чтобы он потом показывал всем мой портрет!"
            mt "И рассказывал, что он нашел себе модель в подворотне!"
            mt "А если меня кто-то узнает?!"
            mt "Нет, этого нельзя делать, Моника!"
            imgd 13511
            m "Нет! Меня не интересует эта работа!"
            return -1
    music Stealth_Groover
    imgf 19175
    mt "Может быть..."
    mt "А что, если предложить ему писать картину у меня в квартире?"
    mt "Вернее, в той ужасной дыре, которую я арендую у придурка Джека?!"
    mt "По-моему, Моника, это неплохая мысль."
    mt "Там ты сможешь спокойно поработать моделью для этого никчемного художника!"
    mt "И сможешь заработать денег!"
    imgd 12060
    m "Мы можем пойти ко мне в квартиру."
    m "Там никто не будет мешать твоей работе."
    # затемнение
    # некоторое время спустя
    # апартаменты Моники
    # Моника стоит перед художником, она в своем наряде шлюхи
    # художник стоит перед мольбертом, в руке кисть
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_53
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 19178
    citizen7 "О такой идеальной модели, как ты, мечтает каждый художник!"
    citizen7 "Чего ты стоишь?"
    citizen7 "Давай работать!"
    imgf 19179
    m "Я уже работаю."
    m "Какую позу мне принять?"
    imgd 19180
    citizen7 "Нееет!"
    citizen7 "Сначала тебе нужно снять свою ужасную одежду."
    citizen7 "Она искажает твои восхитительные формы."
    citizen7 "Я не смогу тебя писать, если ты не снимешь это!"
    music stop
    sound plastinka1b
    img 19181 hpunch
    m "Что?!"
    m "Ты!"
    m "Ты собрался писать картину, где я буду голая?!"
    m "Полностью без одежды?!"
    music Groove2_85
    imgf 19182
    citizen7 "Ну конечно!"
    m "Какого черта ты мне не сказал об этом сразу?!"
    imgd 19183
    citizen7 "Это же итак понятно!"
    citizen7 "О чем тут говорить?!"
    citizen7 "Я же собираюсь переносить на свой холст прелестное женское тело..."
    citizen7 "А не то, что сейчас вижу перед собой!"
    menu:
        "Снять одежду. (in Extra version) (disabled)" if game.extra != True:
            pass
        "Снять одежду." if game.extra == True:
            $ monicaCitizensArtistNudeModel1 = True # Моника согласилась работать моделью ню перед художником
            pass
        "Отказаться.":
            music Stealth_Groover
            imgf 19184
            mt "Я не собираюсь работать моделью для какого-то никчемного художника!"
            mt "Обнаженной моделью!!!"
            mt "Я не хочу, чтобы он потом показывал всем мой портрет!"
            mt "И рассказывал, что он нашел себе модель в подворотне!"
            imgd 19185
            mt "А если меня кто-то узнает?!"
            mt "Нет, этого нельзя делать, Моника!"
            m "Нет! Меня не интересует эта работа!"
            m "Уходи!"
            return -3
    music Pyro_Flow
    imgf 19184
    mt "Вот дьявол!"
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."

    #
    $ notif(_("Моника должна выплачивать Перри долг в размере $ 50 000."))
    imgd 19184
    mt "Ведь мне еще нужно выплачивать долг этой мерзкой извращенке Перри!"
    #

    if ep212_escort_monica_fired == True:
        # если Монику выгнали с эскорта
        #
        $ notif(_("Моника больше не работает в ВИП-эскорте."))
        #
        imgd 19185
        mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
        #
    music Groove2_85
    imgf 19185
    mt "Что же делать, Моника?"
    mt "Возможно, если я запрещу ему рисовать мое лицо..."
    imgd 19186
    m "..."
    m "Я сниму одежду только при одном условии!"
    citizen7 "Каком?"
    imgf 19187
    m "Я буду позировать так, чтобы не было видно моего лица!"
    imgd 19188
    citizen7 "Давай поробуем так."
    citizen7 "Раздевайся скорее!"
    # затемнение
    # смена кадра
    # Моника стоит обнаженная, напротив рыбы, в полоборота к художнику (или спиной к нему, отвернувшись)
    # художник стоит за мольбертом и Моника его не видит
    # пользуясь этим он стоит одной рукой периодически дрочит себе и комментирует
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 31807
    w
    imgf 31808
    citizen7 "О Боги!"
    imgd 31810
    citizen7 "Какие шикарные формы!"
    imgd 31809
    citizen7 "Ты моя прекрасная муза!"
    sound Jump1
    imgf 31811
    citizen7 "Это будет не просто очередное полотно!"
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    w
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    w
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    w
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    citizen7 "Это будет шедевр!"
    imgf 31814
    citizen7 "Эту работу увидит весь мир!!"
    citizen7 "Я стану знаменит!"
    citizen7 "И зарабоотаю много денег!"
    music Groove2_85
    imgd 31815
    m "Если я увижу, что ты нарисовал мое лицо, я уничтожу твое полотно!"
    m "!!!"
    citizen7 "Тебе не стоит так переживать из-за этого, моя муза."
    citizen7 "Ты выбрала прекрасную позу и лица совсем не видно!"
    citizen7 "Только вот..."
    citizen7 "Нужно немного подправить..."
    # подходит к Монике, берет за талию
    sound man_steps
    imgf 31816
    w
    imgd 31817
    m "Эй!"
    m "Ты что делаешь?!"
    citizen7 "Ты ничего не понимаешь!"
    citizen7 "В этой работе важен каждый изгиб, каждый миллиметр!"
    citizen7 "Я довожу твою позу до идеальной!"
    # уходит к холсту, что-то там мазюкает кистью
    sound man_steps
    imgf 31818
    w
    sound Jump1
    imgd 31819
    citizen7 "Так, здесь тоже надо подправить..."
    # снова подходит к Монике
    sound man_steps
    imgf 31816
    # кладет ладони ей на бедро, практически у попы и немного двигает
    w
    imgd 31820
    citizen7 "Эту ножку вот так."
    citizen7 "Да! Само совершенство!"
    # снова к холсту
    sound man_steps
    imgf 31818
    w
    imgd 31821
    citizen7 "У меня никогда не было такой великолепной модели!"
    imgd 31828
    citizen7 "Ты моя муза вдохновения!"
    music Stealth_Groover
    imgf 31822
    mt "Ты, неудачник, вообще никогда не видел такой шикарной женщины, как Я!"
    mt "Знал бы ты, сколько знаменитых людей искусства мечтали бы оказаться сейчас на твоем месте!"
    mt "И ты, идиот, даже не представляешь, какая известная личность сейчас тебе позирует!"
    mt "!!!"
    # художник снова подходит к Монике
    music Groove2_85
    imgd 31816
    sound man_steps
    w
    imgf 31823
    citizen7 "Эту прядь волос еще подправить..."
    # прикасается к пряди ее волос, и как бы невзначай задевает рукой ее грудь
    sound Jump1
    img 31824 hpunch
    w
    imgd 31825
    citizen7 "Ох! Это вышло случайно..."
    imgf 31826
    citizen7 "Могу я потрогать?"
    citizen7 "Мне нужно знать, какая на ощупь великолепная грудь моей музы!"
    mt "!!!" # зло смотрит на него
    citizen7 "Я доплачу тебе за это 2 доллара..."
    $ menu_corruption = [monicaCitizen7_NudeArtCorruption2Required]
    menu:
        "Позволить потрогать грудь.":
            $ monicaCitizensArtistNudeModel2 = True # Моника разрешила художнику потрогать свою грудь
            music Stealth_Groover
            imgd 31827
            mt "Он хочет облапать мою прекрасную грудь своими грязными руками!"
            mt "За 2 доллара!"
            mt "Какой кошмар!"
            mt "С другой стороны..."
            mt "Он ведь только прикоснется и все..."
            mt "Возможно, этому художнику-извращенцу это действительно необходимо для вдохновения..."
            mt "А я заработаю еще 2 доллара."
            imgd 31826
            $ add_corruption(10, "citizen7_art_boobs_touch")
            m "Только быстро!"
            # художник кладет ладони на грудь Монике, мнет груди, трогает соски
            fadeblack 1.5
            music Loved_Up
            imgfl 31829
            w
            imgf 31830
            citizen7 "Ооооо..."
            imgd 31831
            citizen7 "Она божественна..."
            imgf 31832
            citizen7 "Какая нежная кожа..."
            imgd 31833
            citizen7 "Какая упругая грудь..."
            imgf 31834
            citizen7 "Какие манящие соски..."
            img 31827
            m "Все!"
            m "Хватит!"
            mt "Извращенец!"
            pass
        "Отказаться.":
            music Pyro_Flow
            imgd 31826
            mt "Никчемный художник-извращенец!!!"
            mt "!!!"
            ## считаю что нужно поменять местами мысли и речь: сначала мысли потом речь
            imgd 31827
            m "Нет!"
            m "Мы договаривались, что я буду работать моделью!"
            m "Убери руки сейчас же!"
            m "Или забирай свои вещи и убирася вон отсюда!!!"
            citizen7 "Все-все! Хорошо!"
            citizen7 "Мне осталось дописать совсем немного!"
            # он убирает руку и уходит к холсту
#            return

    # художник убирает руки и уходит за мольберт
    # дрочит одной рукой, пока его не видно
    music Groove2_85
    imgf 31818
    sound man_steps
    w
    fadeblack 1.5
    music Loved_Up
    imgfl 31811
    citizen7 "Моя муза..."
    imgf 31812
    w
    sound drkanje5
    imgd 31813
    w
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    w
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    w
    imgd 31812
    w
    sound drkanje5
    imgd 31813
    citizen7 "Ммммм..."
    # кончает в масло, которым пишет картину
    img 31835
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan1
    citizen7 "Оооох..."
    # берет кисть, макает туда, куда кончил и наносит делает мазок на холсте, потом еще один мазок
    imgf 31836
    citizen7 "Это будет настоящий шедевр!"
    # затемнение
    # некоторое время спустя
    # Моника и художник стоят в комнате одетые
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 19189
    if monicaCitizensArtistNudeModel2 == True:
        $ add_money(12.0)
        citizen7 "Вот твои $ 12."
    else:
        $ add_money(10.0)
        citizen7 "Вот твои $ 10."
    imgf 19190
    citizen7 "Возможно, я снова тебе скоро предложу работу модели."
    citizen7 "Твое тело просто создано для этой работы!"
#    m "Ты мне покажешь эту работу?"
#    citizen7 "Да, но сначала мне нужно кое-что доработать в ней."
#    citizen7 "Сделать всего несколько окончательных штрихов."
    # уходит
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.5
    music Stealth_Groover
    imgfl 19191
    mt "Интересно, все творческие люди такие?!"
    mt "Алекс - фотограф-извращенец..."
    mt "Этот неудачник - художник-извращенец..."
    imgf 19192
    mt "Почему меня, такую красивую и хорошую женщину, окружают одни извращенцы?!"
    mt "Я знаю, это моя изумительная красота притягивает их..."
    return

# если Мамочка уже запретила Монике работать с клиентами на улице
# мысли
#label ep214_dialogues2_citizens_19:
    # не рендерить!!
#    mt "Дьявол!"
#    mt "Я не могу лечь спать!"
#    mt "Сначала мне нужно отдать этой старой карге половину моего заработка!"
#    mt "Мне нужно пойти на точку проституток."
#    mt "!!!"
#    return

# Моника пришла на точку с проституток
# мысли
label ep214_dialogues2_citizens_20:
    # не рендерить!!
    mt "Какое кошмарное место!!!"
    mt "Работать здесь - самое дно!"
    mt "Как можно стоять на улице и предлагать себя всем прохожим?!"
    return

# Моника пришла на точку проституток
# клик на Мамочку
label ep214_dialogues2_citizens_21:
    # Моника подходит к Мамочке (или она к ней)
    fadeblack 2.0
    music Master_Disorder
#    music2 street13_ambulance
    imgfl 19124
    w
    imgf 19125
    m "Я..."
    mommy "Ну что, девочка, ты надумала работать здесь?"
    mommy "Это похвально, ты приняла верное решение."
#    mommy "Сколько ты заработала сегодня?"
    music Pyro_Flow
    imgd 19128
#    m "Я заработала сегодня $ [whore_daily_money]."
    m "Нет!"
    m "Я ни за что тут не буду стоять!"
    m "!!!"
#    mommy "Хорошо. Из них 50 процентов мои."
    music Master_Disorder
    imgf 19127
    mommy "Я на твоем месте не была бы столь категорична, девочка..."
    mommy "Жизнь - штука переменчивая..."
#    m "!!!"
#    $ monicaPerryMommyDebt9 = True # Моника отдала Мамочке ее долю
    # Моника отдает деньги
    mommy "Ты ходила к Перри, девочка?"
    if ep214_slums_monica_perry_talk_count == 0 or monicaPerryMommyDebt5 == True:
        imgd 19128
        m "Она лжет, что я должна ей $ 50 000!"
        imgd 19129
        mommy "Ты должна отдать долг этой уважаемой женщине."
        m "!!!"
    else:
        imgd 19128
        m "Да, ходила."
        m "Я отдала ей часть денег..."
        imgd 19129
        mommy "Хорошо."
    imgf 19130
    mommy "Пока ты сопротивляешься тому, чтобы отдавать долги, девочка..."
    mommy "Твоя жизнь не изменится к лучшему..."
    music Power_Bots_Loop
    imgd 19131
    mt "Она еще будет учить меня жизни?!"
    mt"!!!"
    music Master_Disorder
    imgf 19132
#    mommy "Когда заработаешь еще, не забудь снова зайти ко мне..."
    mommy "Можешь идти."
    mommy "Не нужно тебе долго находиться на этом месте и смущать моих девочек."
    mommy "Либо можешь присоединиться к ним."
    mommy "Сегодня много клиентов..."
    m "Нет, спасибо!"
#    music2 stop
    return

# повторный клик на Мамочку, если уже говорила с ней, мысли
label ep214_dialogues2_citizens_22:
    # не рендерить!!
    mt "Не хочу с ней разговаривать!"
    mt "!!!"
    return False

label ep214_dialogues2_citizens_23: # Мамочка смотрит на Монику и не дает зарабатывать у пилона
    music Master_Disorder
    imgfl 24343
    mt "Дьявол, эта старая карга следит за мной!"
    imgd 24344
    mt "Похоже, мне не стоит делать это здесь."
    return

label ep214_dialogues2_citizens_24:
    mt "Эта старая шлюха не имеет права следить за такой леди как Я!"
    return

label ep214_dialogues2_citizens_24b:
    mt "Моника, тебе надо что-то придумать, чтобы закончить все это!"
    mt "Почему каждый пытается использовать мою изумительную красоту?"
    mt "Да, все в восхищении от меня здесь!"
    mt "Но мне было бы лучше сменить это место!"
    mt "Местные обитатели не достойны такой королевы, как Я!"
    return













#
