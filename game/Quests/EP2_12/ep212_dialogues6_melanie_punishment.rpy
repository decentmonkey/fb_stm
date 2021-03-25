default monicaMelanieVictoriaPunishment1 = False  # Моника согласилась выслушать план Мелани
default monicaMelanieVictoriaPunishment2 = False  # Мелани согласилась на откровенную фотосессию
default monicaMelanieVictoriaPunishment3 = False  # Мелани согласилась на секс с Алексом на камеру

#call ep212_dialogues6_melanie_punishment_1() # кабинет Моники, пришла Мелани
#call ep212_dialogues6_melanie_punishment_2() # Моника в конце рабочего дня (мысли)
#call ep212_dialogues6_melanie_punishment_3() # Моника пытается пойти к Мелани в любом наряде, кроме одежды шлюхи (мысли)
#call ep212_dialogues6_melanie_punishment_4() # квартира Мелани, приходят Алекс и Виктория
#call ep212_dialogues6_melanie_punishment_5() # фотосессия
#call ep212_dialogues6_melanie_punishment_6() # сцена с блоуджобом
#call ep212_dialogues6_melanie_punishment_7() # Алекс ушел, Виктория рисует на портрете
#call ep212_dialogues6_melanie_punishment_8() # мысли Моники, после того как ушла от Мелани, если Мелани отказала Виктории
#call ep212_dialogues6_melanie_punishment_9() # мысли Моники, после того как ушла от Мелани, если сцена была проиграна полностью
#call ep212_dialogues6_melanie_punishment_10() # офис, сотрудники рассматривают обложку журнала



# после того, как был паблик ивент в новом ресторане
# Моника приходит на работу в офис
# кабинет Моники
label ep212_dialogues6_melanie_punishment_1:
    # Моника сидит за своим столом, Юлия работает за своим
    music Stealth_Groover
    img 22009
    with fadelong
    mt "В этом отделе собрали самых никчемных сотрудников."
    mt "Они целыми днями сидят, зарывшись в своих бумажках."
    img 20335
    with fade
    mt "И думают, что их отчеты кому-то здесь нужны."
    mt "Неудачники. Бесполезные людишки..."
    # смотрит на Юлию
    img 22008
    with diss
    mt "А эта Юлия вообще готова до поздней ночи сидеть и делать никому ненужную работу."
    mt "От нее больше пользы было, когда она работала гувернанткой..."
    # открывается дверь и в ее кабинет заходит Мелани, встает перед Моникой
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music ZigZag
    img 15409
    with fadelong
    w
    img 17256
    with fade
    melanie "Здравствуйте, Миссис Бакфетт."
    # Моника заметно пугается, вскакивает со стула
    music Master_Disorder
    img 17257
    with diss
    w
    sound Jump1
    img 15414
    with diss
    w
    img 15421
    with fade
    mt "Мелани?!"
    mt "Зачем она снова ко мне пришла? Какое-то чертово дежа-вю!"
    img 15422
    with diss
    mt "Неужели снова эта мерзкой Виктории что-то нужно?!"
    mt "?!?!?!"
    # Юлия с интересом наблюдает за поведением Моники
    music Groove2_85
    img 15419
    with fade
    julia "???"
    img 15423
    with diss
    mt "!!!"
    # Моника бросает взгляд на Юлию, потом делает покер-фейс, садится обратно на свой стул и обращается к Мелани
    img 15424
    with diss
    m "Мелани, ты вернулась?"
    m "Где ты пропадала столько времени?"
    # Мелани невозмутимо отвечает
    music ZigZag
    img 15410
    with fade
    melanie "Я брала несколько выходных дней у Бифа..."
    m "Надеюсь, ты пришла не для того, чтобы пригласить меня на девичник?"
    img 15412
    with diss
    melanie "Как раз об этом я и хотела с Вами поговорить, Миссис Бакфетт..."
    melanie "..."
    # Моника смотрит на Мелани и думает
    music Master_Disorder
    img 20270
    with fade
    mt "Чтобы я еще раз пошла на встречу с этой сучкой Викторией?!"
    mt "Ни за что!!!"
    img 20808
    with diss
    mt "Если Мелани согласна на еще один такой девичник..."
    mt "То пусть развлекает сама эту мелкую дрянь!"
    mt "!!!"
    img 17258
    with diss
    m "Да, Мелани, я слушаю..."
    # Юлия все это время с подозрением смотрит на Монику
    # Мелани поворачивается, смотрит на Юлию
    music ZigZag
    img 17259
    with fade
    melanie "..."
    # потом снова на Монику
    img 17260
    with diss
    w
    # Моника тоже обращает внимание, что Юлия греет уши
    music Stealth_Groover
    img 17261
    with diss
    mt "..."

    # если есть отношения с Юлией и Моника уже сказала ей, что та ей нравится
    if ep210_julia_first_date_begin_day > 0:
        $ notif(t_("У Моники с Юлией отношения"))
        img 17261
    #    with diss
        m "Юлия, мне нужно обсудить с Мелани важный рабочий момент."
        # Юлия бросает на Мелани ревнивый взгляд
        img 17262
        with diss
        julia "!!!"
        img 17263
        with fade
        m "..."
        music Groove2_85
        img 20800
        with diss
        julia "Я... Мне выйти, Миссис Бакфетт? "
        img 22288
        with diss
        m "Да, выйди ненадолго."
        # Юлия недовольная выходит из кабинета
        sound highheels_short_walk
        img 17266
        with fade
        w
        music stop
        img black_screen
        with diss
        sound highheels_short_walk
        sound2 snd_door_close1
        pause 1.0
    else:
        # если нет отношений с Юлией
        music Stealth_Groover
        img 20810
        with fade
        m "Юлия!"
        m "Я смотрю, наш разговор с Мелани тебя интересует больше, чем работа?!"
        img 17264
        with diss
        julia "Н-нет, Миссис Бакфетт..."
        julia "Извините..."
        img 20811
        with fade
        m "Выйди из кабинета!"
        img 17265
        with diss
        julia "Д-да, конечно."
        img 20798
        with hpunch
        m "Быстро!"
        # Юлия недовольная выходит из кабинета
        sound highheels_short_walk
        img 17266
        with fade
        w
        music stop
        img black_screen
        with diss
        sound highheels_short_walk
        sound2 snd_door_close1
        pause 1.0

    # Моника, как только Юлия выходит из кабинета, вскакивает со своего стула
    music Master_Disorder
    img 17267
    with fadelong
    m "Мелани!"
    m "Больше никаких встреч с этой сучкой Викторией!!!"
    m "Я даже слышать об этом ничего не хочу!"
    img 17268
    with fade
    mt "Какая-то выскочка решила поиграть со мной, Моникой Бакфетт, в свои извращенские игры!!!"
    mt "И думает, что ей это просто так сойдет с рук!!!"
    # Мелани спокойно смотрит на Монику
    music ZigZag
    img 15418
    with diss
    melanie "Именно это я и хотела обсудить с Вами, Миссис Бакфетт..."
    # Моника смотрит на нее с возмущением
    img 17269
    with diss
    m "!!!"
    menu:
        "Я тебя слушаю, Мелани.":
            $ monicaMelanieVictoriaPunishment1 = True # Моника согласилась выслушать план Мелани
            pass
        "Я больше ни слова не хочу слышать об этой стерве!!! (пропуск событий с Мелани)":
            # Сделать из 2-х артов, не более
            music Pyro_Flow
            img 15424
            with fade
            m "Мелани! Я больше ни слова не хочу слышать об этой стерве!"
            m "И ничего не собираюсь обсуждать!"
            img 15425
            with diss
            melanie "Вы уверены, Миссис Бакфетт?"
            melanie "Это ведь в Ваших интересах..."
            # Моника перебивает Мелани
            img 17270
            with fade
            m "Я это уже слышала от тебя, Мелани!"
            m "Я больше не хочу ничего обсуждать!!!"
            music ZigZag
            img 15420
            with diss
            melanie "Хорошо, Миссис Бакфетт. Я Вас услышала..."
            melanie "До свидания, Миссис Бакфетт."
            img 15427
            with fade
            sound highheels_short_walk
            melanie_t "Миссис Бакфетт, конечно, не самая умная женщина..."
            melanie_t "И в такие моменты я в этом убеждаюсь лишний раз..."
            # Мелани выходит из кабинета
            return False
    # Моника садится на свой стул
    music ZigZag
    img 17271
    with fade
    m "Я тебя слушаю, Мелани."
    img 17272
    with diss
    melanie "Миссис Бакфетт, я согласна с Вами."
    melanie "Просто так нельзя оставлять то, что Виктория сделала в тот вечер."
    img 15412
    with diss
    melanie "Я рассчитываю на Ваше содействие в том, чтобы поставить ее на место."
    melanie "И лишить ее возможности манипулировать нами."
    img 20905
    with fade
    m "Эту стерву уже давно следовало бы поставить на место!"
    m "!!!"
    m "Вопрос в том, как это сделать?!"
    img 17273
    with diss
    melanie "Дело в том, что я навела кое-какие справки..."
    music Master_Disorder
    img 20362
    with fade
    mt "Хм... Интересно..."
    mt "Что бы там ни было, я сделаю все, чтобы отомстить этой мелкой сучке!"
    music ZigZag
    img 17274
    with diss
    melanie "Я задействовала свои связи..."
    melanie "И узнала, что у одного фотографа есть знакомый папарацци..."
    melanie "Он одно время интересовался Викторией и у него есть фото, компрометирующее ее."
    # Моника смотрит на нее недоверчиво
    img 17258
    with fade
    m "И что это за фото?"
    melanie "На этой фотографии доказательство того, что Виктория изменяет Дику."
    # Моника смотрит на нее удивленно
    music stop
    sound plastinka1b
    img 15413
    with hpunch
    m "?!?!?!"
    music ZigZag
    img 17275
    with fade
    melanie "Да. Она сделала это прямо в его кабинете на рабочем столе."
    melanie "Я пообщалась с фотографом и попросила достать эту фотографию..."
    img 20247
    with diss
    m "И?"
    m "Это фото у тебя?"
    img 17276
    with fade
    melanie "В том и дело, что нет."
    melanie "Он не готов просто так отдавать эту фотографию и выдвинул определенное условие..."
    img 17277
    with diss
    m "Какое условие? Что ему нужно? Деньги?"
    m "Мелани, ты же понимаешь, что нам просто необходимо достать это фото?!"
    m "Заплати ему!"
    img 17278
    with fade
    melanie "Понимаю, Миссис Бакфетт."
    melanie "Его условие следующее: взамен фото я позволю ему снять меня на камеру."
    melanie "Он уже давно вьется вокруг меня..."
    img 17279
    with diss
    melanie "Неоднократно просил эксклюзивную фотосессию, но я ему всегда отказывала."
    melanie "Поэтому я не удивлена, что он выдвинул такое условие."
    img 17280
    with diss
    m "Ты собираешься раздеться?"
    melanie "Ни в коем случае. Он бы хотел этого, но будет достаточно взять более сексуальный ракурс..."
    music Groove2_85
    img 20269
    with fade
    mt "Всего лишь очередная фотосессия для Мелани."
    mt "Подумаешь..."
    mt "Не вижу здесь ничего сложного для нее."
    mt "Только..."
    img 17281
    with diss
    m "Мелани, а ты уверена, что у этого фотографа действительно есть это фото?"
    m "А если он нас обманет?"
    music ZigZag
    img 17256
    with fade
    melanie "Я не думаю, Миссис Бакфетт."
    melanie "Он достаточно известен в индустрии моды и ему ни к чему ссорится со мной..."
    melanie "Или с Вами."
    img 20372
    with diss
    m "Когда назначена встреча с ним? И где?"
    img 15412
    with fade
    melanie "Сегодня вечером, Миссис Бакфетт. У меня дома."
    img 17282
    with diss
    m "Договорились, Мелани."
    melanie "До встречи, Миссис Бакфетт."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    sound2 snd_door_close1
    pause 2.0
    # Мелани уходит
    music Groove2_85
    img 20335
    with fade
    mt "Надеюсь, что никаких проблем этот никчемный фотограф не доставит."
    mt "В конце концов, давно пора поставить сучку Викторию на место!"
    mt "Ненавижу эту тварь!"
#    $ log1 = t_("Пойти домой к Мелани вечером")
    return True

label ep212_dialogues6_melanie_punishment_1a:
    mt "Сегодня вечером, после работы."
    return

# Моника в конце рабочего дня
# мысли
label ep212_dialogues6_melanie_punishment_2:
    # не рендерить!!
    mt "Я, конечно, могу не ехать к Мелани..."
    mt "Она и без меня может провести встречу с этим никчемным фотографом..."
    mt "Но я должна проконтролировать, что все пройдет как нужно..."
    mt "И у нас будет компромат на сучку Викторию!"
    mt "Не могу дождаться этого момента!"
    mt "!!!"
    menu:
        "Лечь спать.":
            return
        "Не ложиться.":
            return False

# Моника пытается пойти к Мелани в любом наряде, кроме одежды шлюхи
# мысли
label ep212_dialogues6_melanie_punishment_3:
    # не рендерить!!
    mt "В прошлый раз я была у Мелани в костюме шлюхи. Сегодня тоже нужно надеть его."
    return

# квартира Мелани
label ep212_dialogues6_melanie_punishment_4:
    # Моника заходит в квартиру Мелани, садится на диван (или стул)
    # Мелани в красном пеньюаре
    # Моника переживает
    music stop
    sound highheels_run2
    img black_screen
    with diss
    pause 2.0
    music ZigZag
    img 17283
    with fadelong
    sound snd_door_knock
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music ZigZag
    img 17284
    with fade
    m "Мелани, этот твой фотограф еще не пришел?"
    img 17285
    with diss
    melanie "Нет, Миссис Бакфетт. Он должен подойти с минуты на минуту."
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 17286
    with fadelong
    m "Мелани..."
    m "..."
    m "А вдруг Виктория узнает о том, что у нас есть на нее компромат..."
    m "Еще до того, как мы покажем это фото Дику?"
    # Мелани абсолютно спокойна
    music ZigZag
    img 17287
    with fade
    melanie "Миссис Бакфетт, я абсолютно уверена в этом фотографе."
    melanie "У него не хватит мозгов, чтобы создать такую интригу."
    melanie "Я уверена, что наш план сработает."
    img 17288
    with diss
    melanie "И мы с Вами, наконец-то, избавимся от нашей 'милой подружки'..."
    melanie "Меня тошнит от того, что я должна целовать ее при встрече."
    melanie "Я больше никогда не стану делать этого!"
    img 15531
    with fade
    m "Не могу дождать этого момента."
    # стук в дверь, Мелани идет открывать дверь
    # заходит Алекс, Викторию пока не видно
    # смотрит на Мелани с довольной улыбкой
    sound snd_door_knock
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music ZigZag
    img 17289
    with fadelong
    w
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Groove2_85
    img 17290
    with fadelong
    alex_photograph "Привет, Мелани!"
    melanie "Здравствуй, Алекс."
    img 17291
    with vpunch
    m "Алекс?!" # удивленно
    # Алекс переводит взгляд на Монику и удивленно
    img 17292
    with diss
    alex_photograph "Миссис Бакфетт?!"
    alex_photograph "Здравствуйте, не ожидал Вас здесь увидеть..."
    alex_photograph "Приятно удивлен..."
    # Моника подозрительно смотрит на Алекса
    img 17293
    with diss
    mt "Хмм... Мелани не говорила, что это будет Алекс..."
    mt "Она действительно уверена, что этому фотографу-извращенцу можно доверять?.."
    mt "???"
    # Алекс делает шаг в квартиру Мелани и за ним заходит Виктория с самодовольным видом
    sound highheels_short_walk
    img 17294
    with fade
    victoria "Привет, подружки."
    # Моника вскакивает со стула, Мелани в шоке
    music Power_Bots_Loop
    sound Jump1
    img 17295
    with hpunch
    melanie "!!!"
    img 17296
    with hpunch
    m "!?!?!?!"
    music Groove2_85
    img 17297
    with fade
    victoria "Я так рада нашей встрече."
    victoria "Я тут подумала, что мы давно не встречались с вами..."
    victoria "И я решила сделать вам сюрприз."
    # подружки в ступоре, Виктория ехидно смотрит на них, Алекс пялится на грудь Мелани
    sound highheels_short_walk
    img 17298
    with diss
    victoria "Удивлены?"
    victoria "Не знали, что мы с Алексом знакомы?"
    melanie "..."
    m "..."
    victoria "Мне кажется или мои подружки не рады видеть меня?"
    # Моника с Мелани переглядываются
    music Master_Disorder
    img 17300
    with fade
    mt "Как!"
    mt "Такое!"
    mt "Могло!"
    mt "Случиться?!"
    mt "!?!?!?!"
    mt "Мелани!!!"
    music Power_Bots_Loop
    img 17301
    with diss
    mt "Алекс!!!" # переводит вгляд на Алекса и злобно смотрит на него
    music Master_Disorder
    img 17299
    with fade
    melanie_t "Эта сучка в курсе наших планов!"
    melanie_t "!!!"
    img 17302
    with diss
    melanie_t "Алекс!!!" # тоже смотрит на Алекса, потом переводит взгляд на Викторию
    melanie "..."
    img 17303
    with fade
    melanie "Конечно, мы рады нашей встрече... Подружка..."
    # Виктория смотрит на портрет Мелани, который она разрисовывала на девичнике, помада стерта
    sound Jump2
    img 17304
#    with diss
    victoria "???"
    # потом снова смотрит на Мелани
    music Groove2_85
    img 17305
    with fade
    victoria "..."
    victoria "Мелани..."
    melanie "..."
    victoria "Ты хорошая подружка?"
    melanie "Да..."
    img 17306
    with diss
    victoria "Ты уверена в том, что ты хорошая подружка?"
    img 17307
    with fade
    melanie "..."
    melanie "Уверена..."
    img 17308
    with diss
    victoria "Что ты должна сделать, если ты и правда рада нашей встрече?"
    # выбор у Мелани, Моника стоит позади и бросает гневные взгляды на Алекса
    img 17309
    with diss
    m "!!!"
    melanie "..."
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани целует Викторию в щечку, Виктория хихикает
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 17310
    with fadelong
    sound snd_kiss2
    w
    img 17311
    with fade
    w
    img 15549
    with diss
    sound snd_woman_laugh3
    w
    # потом Виктория проходит и по-хозяйски садится на диван, все остальные тоже садятся
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 17312
    with fadelong
    m "Алекс!"
    m "Я не знала, что ты знаком с нашей подружкой Викторией..."
    img 17313
    with fade
    alex_photograph "Да, Миссис Бакфетт..."
    # Виктория перебивает его
    victoria "Да, мы знакомы..."
    victoria "Алекс рассказал мне про эксклюзивную фотосессию."
    img 17314
    with diss
    victoria "Он также сокрушался о том, что Мелани соглашается только на приличные кадры."
    victoria "И я предложила ему свою помощь."
    # Моника испепеляет Алекса взглядом, Мелани вопросительно смотрит на Алекса
    music Power_Bots_Loop
    img 17315
    with diss
    m "!!!"
    melanie "???"
    music Groove2_85
    img 17316
    with fade
    alex_photograph "Мисс Виктория сказала, что ..."
    # Виктория снова перебивает его
    img 17317
    with diss
    victoria "Я сказала Алексу, что моя подружка Мелани не откажет мне..."
    victoria "Если я попрошу ее сделать эту фотосессию несколько откровенной."
    img 17318
    with fade
    melanie "Откровенной?"
    victoria "Именно."
    # Виктория обращает внимание на Монику
    img 17319
    with diss
    victoria "Может быть, Миссис Бакфетт тоже захочет поучаствовать?"
    music Master_Disorder
    img 17320
    with fade
    mt "НЕТ!"
    mt "!!!"
    music Groove2_85
    img 17321
    with diss
    victoria "..."
    victoria "Но маловероятно, чтобы сама Моника Бакфетт снизошла до такого... Возможно, в следующий раз..."
    victoria "Но она тоже моя подружка, поэтому будет не против этой фотосессии."
    victoria "Ты же не против, подружка Моника?"
    # взгляд на Мелани
    music Master_Disorder
    img 17322
    with fade
    mt "По-моему, она поняла, что этот план придумала Мелани..."
    mt "И решила наказать ее..."
    melanie "..."
    # потом снова смотрит на Викторию
    img 17323
    with diss
    mt "Эта мелкая дрянь узнала обо всем! От Алекса!"
    mt "!!!"
    mt "Я даже представить не могу, что она собирается сделать..."
    img 17324
    with diss
    mt "..."
    mt "Мерзкая извращенка!"
    mt "!!!"
    # Моника отвечает
    menu:
        "Дать согласие на фотосессию Мелани":
            pass
    img 17325
    with fade
    m "Я не против..."
    music Groove2_85
    img 17326
    with diss
    victoria "Хорошо."
    victoria "А что скажет подружка Мелани?"
    victoria "Она ведь не откажет МНЕ?"
    # Мелани смотрит на нее, потом на Алекса
    img 17327
    with diss
    melanie "..."
    menu:
        "Согласиться на фотосессию":
            $ monicaMelanieVictoriaPunishment2 = True # Мелани согласилась на откровенную фотосессию
            pass
        "Отказаться (пропуск событий с Мелани)":
            # Максимум 3 арта
            music ZigZag
            img 17328
            with fade
            melanie_t "Я больше не позволю этой мелкой сучке унижать меня."
            melanie_t "Да еще и в присутствии Алекса."
            img 17330
            with diss
            sound highheels_short_walk
            melanie "..."
            melanie "Подружка... Я согласна удвоить еженедельные взносы в счет нашей дружбы..."
            # Ехидно
            music Groove2_85
            img 17331
            with fade
            victoria "Хорошо, подружка..."
            victoria "Так уж и быть..."
            victoria "Жду тебя как обычно..."
            music stop
            scene black_screen
            with Dissolve(1)
            # затемнение экрана
            return False
    music Master_Disorder
    img 17328
    with fade
    melanie_t "Значит, Алекс ей все рассказал..."
    melanie_t "Я не предполагала что они знакомы."
    melanie_t "У Алекса совсем нет мозгов, мне следовало быть более осторожной с ним..."
    melanie_t "Но с Алексом я разберусь позже."
    img 17329
    with diss
    melanie_t "Эта сучка теперь будет мстить мне за попытку раздобыть компромат на нее."
    melanie_t "Нужно согласиться на эту фотосессию."
    melanie_t "Пусть Виктория думает, что я раскаиваюсь..."
    melanie_t "А снимки я позже заберу у этого безмозглого Алекса."
    music ZigZag
    img 17330
    with fade
    sound highheels_short_walk
    melanie "..."
    melanie "Я согласна."
    img 17332
    with diss
    w
    music Groove2_85
    img 17331
    with fade
    victoria "Я знала, что ты не сможешь отказать мне, подружка Мелани."
    victoria "Так..."
    # смотрит на наряд Мелани оценивающе
    img 17333
    with diss
    victoria "Эта одежда вполне сойдет для фотосессии..."
    victoria "Ну что? Приступим?"

#    music ZigZag
    music Molten_Alloy
    img 17428
    with fadelong
    alex_photograph "Мелани, я так рад, что ты согласилась на эту фотосессию."
    # смотрит на него холодно
    melanie "..."
    alex_photograph "Ну что, начнем."
    return


# квартира Мелани
# фотосессия
label ep212_dialogues6_melanie_punishment_5:
    # Моника наблюдает со стороны, Мелани позирует
    # Виктория комментирует и заставляет принимать максимально открытые позы и брать соотв. ракурсы



    # завершения фотосессии
    # Алекс доволен
    music Groove2_85
    img 17355
    with fade
    alex_photograph "Это была отличная работа, Мелани!"
    alex_photograph "Мисс Виктория, спасибо Вам за помощь!"
    alex_photograph "Вы подсказали много интересных ракурсов."
    # Виктория самодовольно смотрит на Мелани
    img 17359
    with diss
    sound snd_woman_laugh3
    victoria "Всегда рада помочь своей подружке."
    # Мелани с покерфейсом
    music Master_Disorder
    img 17356
    with fade
    melanie_t "Надеюсь, на этом все?"
    melanie_t "Не хочу больше видеть их в своем доме."
    melanie_t "Виктория выглядит вполне довольной. Получила, что хотела. Сучка!"
    melanie_t "Завтра я заберу эти кадры у Алекса."
    melanie_t "Я не могу позволить, чтобы такая фотосессия хранилась у кого бы то ни было."
    melanie_t "Существует шанс того, что она просочится в мир."
    # Моника смотрит на Мелани
    img 17324
    with diss
    mt "Какой кошмар!"
    mt "Не представляю, если бы эта дрянь заставила меня делать подобные кадры!"
    mt "!!!"
    music ZigZag
    img 17344
    with fade
    melanie "Алекс, пожалуйста, оставь эти кадры пока при себе."
    melanie "Завтра мне надо будет поговорить с тобой..."
    return

# квартира Мелани
label ep212_dialogues6_melanie_punishment_6:
    # после фотосессии все сидят снова на своих местах
    # Моника с Мелани недовольны
    music stop
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("Минуту спустя...")) from _rcall_textonblack_38
    scene black_screen
    with Dissolve(1)
    music Master_Disorder
    img 17334
    with fadelong
    w
    img 17324
    with fade
    mt "Скорее бы оказаться подальше от этой дряни!"
    mt "Вместе с этим фотографом-извращенцем!"
    mt "Придурок!!!"
    mt "!!!"
    # Виктория обращается к Алексу, тот сидит довольный и пялится на Мелани
    music Groove2_85
    img 17335
    with diss
    victoria "Ну что, Алекс, ты доволен?"
    alex_photograph "Конечно, Виктория! Я так рад что тебе удалось убедить Мелани!"
    alex_photograph "Не знал что вы с ней такие близкие подруги!"
    img 17336
    with fade
    victoria "Алекс, что скажешь насчет моего портфолио?"
    victoria "Мне кажется, что тебе ничего не стоит помочь мне в его продвижении."
    victoria "Всего несколько рекомендаций нужным людям."
    victoria "Уверена, для тебя это не составит никакого труда."
    # Алекс смотрит на Викторию, потом снова на Мелани
    img 17337
    with diss
    w
    img 17338
    with diss
    alex_photograph "Виктория, конечно, для меня это не трудно..."
    alex_photograph "Но я привыке помогать в продвижении девушкам с такими данными, как у Мелани."
    alex_photograph "С девушками с обычной внешностью я не работаю."
    # Виктория зло смотрит на Мелани
    music Master_Disorder
    img 17339
    with fade
    victoria "!!!"
    # Мелани про себя злорадствует и смотрит на нее высокомерно
    img 17340
    with diss
    melanie "..."
    # Виктория снова обращается к Алексу
    music Groove2_85
    img 17341
    with fade
    victoria "Алекс, а если я расскажу тебе ее маленький секрет?"
    alex_photograph "???"
    # Мелани с Моникой в шоке
    music Master_Disorder
    img 17342
    with diss
    melanie_t "Что эта сучка может рассказать ему?"
    melanie_t "Она собирается рассказать про Маркуса?"
    # Алекс заинтересованно смотрит на Викторию
    music Groove2_85
    img 17343
    with fade
    victoria "Так как мы с Мелани очень хорошие подружки..."
    victoria "Она делится со мной всеми своими секретами."
    victoria "И она говорила мне, что хочет переспать с тобой, Алекс."
    music Pyro_Flow
    sound Jump1
    img 17344
    with diss
    melanie "Что?"
    melanie "Это не так, Алекс."
    melanie "Я..."
    # Виктория перебивает ее и снова обращается к Алексу
    img 17345
    with diss
    victoria "Что, если Мелани позволит тебе переспать с ней?"
    melanie "Нет. Это исключено."

    # Виктория ехидно
    music Groove2_85
    img 17346
    with fade
    victoria "Мелани, подружка, ну признайся!"
    victoria "Ты хотела, чтобы он тебе принес фото."
    victoria "А на самом деле это был просто предлог, чтобы переспать с ним?"
    music Pyro_Flow
    img 17347
    with diss
    melanie "!!!"
    # Алекс в шоке
    music Groove2_85
    img 17348
    with fade
    alex_photograph "Мелани... Я..."
    alex_photograph "Я и не знал, что нравлюсь тебе..."
    alex_photograph "Ты поэтому избегала меня все это время?"
    music Master_Disorder
    img 17349
    with diss
    melanie_t "Что за бред несет эта дряная Виктория?!"
    melanie_t "Чего она добивается?"
    melanie_t "Фотосессии было недостаточно?"
    img 17350
    with fade
    melanie "..."
    victoria "Ну, подружка Мелани, не стесняйся. Признайся, что хочешь этого."
    # угрожающе
    img 17351
    with diss
    victoria "Ты ведь хорошая подружка, не правда-ли?"

    # Мелани сквозь зубы, зло
    img 17352
    with fade
    melanie "Да..."
    img 17353
    with diss
    victoria "Что 'да'?"
    menu:
        "Я хочу переспать с Алексом":
            pass
    img 17354
    with fade
    melanie "Я пригласила сюда Алекса, чтобы..."
    melanie "Чтобы переспать с ним."
    melanie "..."
    # Виктория самодовольно
    music Groove2_85
    img 17355
    with diss
    victoria "Хорошая подружка."
    victoria "Ты же не будешь против, если мы с подружкой Моникой будем присутствовать при этом?"
    music Pyro_Flow
    img 17356
    with fade
    melanie_t "Я уничтожу эту дрянь Викторию!"
    melanie_t "Я задействую для этого все свои связи!"
    melanie_t "!!!"
    music Master_Disorder
    img 17357
    with diss
    melanie "Нет, я не против."
    # Моника в шоке
    img 17358
    with fade
    mt "О, Боже!"
    mt "Я не могу поверить, что эта сучка заставляет Мелани делать это!"
    mt "!!!"

    # Виктория хихикает и продолжает командовать
    music Groove2_85
    img 17359
    with diss
    sound snd_woman_laugh3
    w
    img 17360
    with fade
    victoria "Отлично!"
    victoria "Алекс, раз уж ты привык все снимать на камеру, то почему бы не снять то, как вы будете делать это?"
    victoria "Подружка Мелани любит, когда ее снимают на камеру."
    victoria "Даже во время секса. Да, Мелани?"
    music Master_Disorder
    img 17340
    with diss
    melanie "..." # зло
    img 17361
    with fade
    victoria "Я не слышу ответа. Ты же хочешь, чтобы я сняла вас с Алексом на камеру?"
    # Мелани в ярости
    img 17362
    with diss
    melanie "..."
    melanie "Виктория, это не идет ни в какие рамки!!! Я..."
    victoria "Хорошая подружка хочет этого."
    victoria "Плохая подружка не будет дружить со мной..."
    melanie "!!!"
    menu:
        "Да, хочу...":
            pass
    # Мелани сквозь зубы, злобно смотрит на Алекса
    img 17363
    with fade
    melanie "Да, хочу..."
    img 17364
    with diss
    melanie_t "Я готова потерпеть Алекса."
    melanie_t "..."
    melanie_t "Пусть эта стерва порадуется."
    music Pyro_Flow
    img 17342
    with diss
    melanie_t "Потом я сотру ее в порошок!"
    melanie_t "Я найду способ!"
    melanie_t "!!!"
    # Алекс думает, что Мелани и правда хочет его и радуется
    music Groove2_85
    img 17365
    with fade
    alex_photograph "Мелани, я тоже не против!"
    alex_photograph "Не знал, что ты настолько любишь камеру!"
    victoria "Подружка Мелани любит ролевые игры, поэтому это будет не просто секс..."
    alex_photograph "Ух ты! Даже так?!"
    img 17366
    with diss
    victoria "Да, Алекс."
    victoria "Мы разыграем небольшую сцену."
    victoria "И так как ты, Алекс, будешь занят, то я, так уж и быть, сама готова снять это на свой телефон."
    img 17367
    with diss
    victoria "Сейчас ты, подружка Мелани, на камеру скажешь, что..."
    victoria "Что, как обычно, сделаешь минет за $ 50, а сексом займешься за $ 100."
    victoria "И сделаешь это."
    victoria "А Алекс нам подыграет."
    # Моника напугана происходящим
    music Master_Disorder
    img 17320
    with fade
    mt "Эта белобрысая дрянь - настоящий дъявол!"
    mt "Как она могла вообще до такого додуматься?!"
    mt "!!!"
    img 17323
    with diss
    mt "А что, если бы я сейчас был на месте Мелани?!"
    mt "Кошмар!!!"
    mt "!!!"
    # Мелани зло смотрит на Викторию
    img 17340
    with fade
    melanie "..."
    melanie "Подружка Виктория, может, мы сделаем это в другой раз?"
    melanie "В какой-нибудь более подходящей обстановке?"
    img 17368
    with diss
    melanie "Да, Алекс?"
    music Groove2_85
    img 17360
    with fade
    victoria "Не стоит так стесняться, подружка Мелани."
    victoria "Просто снимем небольшое видео. Повеселимся."
    victoria "Ты же не будешь спорить и сделаешь все, что я тебе скажу?"
    victoria "Ты же хорошая подружка, Мелани?" # угрожающе
    melanie "..."
    menu:
        "Сделать как требует Виктория":
            $ monicaMelanieVictoriaPunishment3 = True # Мелани согласилась на секс с Алексом на камеру
            pass
        "Отказаться (пропуск сцены)":
            # Максимум 3 арта
            music ZigZag
            img 17342
            with fade
            melanie_t "Я больше не позволю этой мелкой сучке унижать меня."
            melanie_t "Да еще и в присутствии Алекса."
            img 17345
            with diss
            sound highheels_short_walk
            melanie "..."
            melanie "Подружка... Я согласна удвоить еженедельные взносы в счет нашей дружбы..."
            # Ехидно
            music Groove2_85
            img 17359
            with fade
            sound snd_woman_laugh3
            victoria "Хорошо, подружка..."
            victoria "Так уж и быть..."
            victoria "Жду тебя как обычно..."
            music stop
            scene black_screen
            with Dissolve(1)
            # затемнение экрана
            return False
    music Master_Disorder
    img 17369
    with diss
    melanie "Да, я хорошая подружка..."
    melanie "Я сделаю, как ты скажешь..."
    melanie "..."
    # переглядываются с Моникой
    music stop
    sound plastinka1b
    img 17370
    with hpunch
    mt "!!!"
    mt "!!!!!!"
    img 17371
    with diss
    w
    # затемнение
    # Мелани сидит в кресле, Виктория снимает все на камеру на телефоне
    # Алекс подходит к Мелани со спущенными штанами, его видно со спины
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    sound snd_zip
    pause 2.0
    music Groove2_85
    img 17372
    with fadelong
    alex_photograph "Какой у тебя прейскурант, Мелани?"
    melanie "!!!"
    victoria "???"
    # Мелани отвечает
    img 17373
    with fade
    melanie "Как обычно, сделаю минет за 50 долларов, секс стоит 100 долларов."
    # Алек бросает ей 50 баксов
    img 17374
    with diss
    alex_photograph "Вот твой сегодняшний заработок."
    alex_photograph "Соси!"
    # Мелани медлит
    music Pyro_Flow
    img 17375
    with fade
    melanie_t "Этот гребаный Алекс еще и подыгрывает ей!"
    melanie_t "Я сотру эту стерву в порошок!"
    melanie_t "Сейчас просто нужно сделать вид, что я ее слушаюсь."
    melanie_t "!!!"
    music Groove2_85
    img 17376
    with diss
    alex_photograph "Ну? Отрабатывай свои деньги!"
    # делает минет Алексу
    music stop
    img black_screen
    with diss
    pause 1.5
    music2 Loved_Up
    img 17377
    with fade
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Melanie_Alex_Blowjob1_1.ogg"
    scene black
    image videov_Melanie_Alex_Blowjob1_1 = Movie(play="video/v_Melanie_Alex_Blowjob1_1.mkv", fps=30)
    show videov_Melanie_Alex_Blowjob1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17378
    with diss
    alex_photograph "Ооооо, Меланиииии!!!"
    img 17379
    with fade
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Melanie_Alex_Blowjob1_1.ogg"
    scene black
    image videov_Melanie_Alex_Blowjob1_2 = Movie(play="video/v_Melanie_Alex_Blowjob1_2.mkv", fps=30)
    show videov_Melanie_Alex_Blowjob1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17384
    with diss
    alex_photograph "Ааааааа!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Melanie_Alex_Blowjob1_1.ogg"
    scene black
    image videov_Melanie_Alex_Blowjob1_3 = Movie(play="video/v_Melanie_Alex_Blowjob1_3.mkv", fps=30)
    show videov_Melanie_Alex_Blowjob1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17380
    with fade
    alex_photograph "Возьми его глубже!"
    img 17381
    with diss
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Melanie_Alex_Blowjob1_1.ogg"
    scene black
    image videov_Melanie_Alex_Blowjob1_4 = Movie(play="video/v_Melanie_Alex_Blowjob1_4.mkv", fps=30)
    show videov_Melanie_Alex_Blowjob1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.3, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Melanie_Alex_Blowjob1_1.ogg"
    scene black
    image videov_Melanie_Alex_Blowjob1_5 = Movie(play="video/v_Melanie_Alex_Blowjob1_5.mkv", fps=30)
    show videov_Melanie_Alex_Blowjob1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    alex_photograph "Ещеееее!!!"
    img 17382
    with fade
    w
    alex_photograph "Быстрее! Быстрее!!!"
    music2 stop
    music Loved_up2
    img 17383
    with diss
    w
    # Алекс кончает
    menu:
        "Кончить в рот Мелани.":
            img 17386
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "Дааа..."
            alex_photograph "Дааа!!!"
            img 17390
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            alex_photograph "ДААААААА!!!"
            img 17392
            with fade
            w
            $ ep212_quests_alex_cummed_area = 1
            pass
        "Кончить на лицо Мелани.":
            img 17387
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "Дааа..."
            alex_photograph "Дааа!!!"
            img 17390
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            alex_photograph "ДААААААА!!!"
            img 17391
            with fade
            w
            $ ep212_quests_alex_cummed_area = 2
            pass
        "Кончить на грудь Мелани.":
            img 17388
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "Дааа..."
            alex_photograph "Дааа!!!"
            img 17390
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            alex_photograph "ДААААААА!!!"
            img 17389
            with fade
            w
            $ ep212_quests_alex_cummed_area = 3
            pass
    music Groove2_85
    img 17385
    with fade
    victoria "Видео снято!"
    victoria "Алекс, спасибо!"
    # затемнение
    return

# квартира Мелани
label ep212_dialogues6_melanie_punishment_7:
    # кадр меняется, Мелани с Моникой и Викторией одни, Алекс ушел
    # Виктория хихикает
    music stop
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("Спустя некоторое время...")) from _rcall_textonblack_39
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    img 17393
    with fadelong
    victoria "Подружки, мы отлично с вами повеселились сегодня."
    victoria "Теперь у меня на память есть видео."
    victoria "Оно побудет у меня. Вы же не против, подружки?"
    img 17359
    with fade
    sound snd_woman_laugh3
    victoria "Хорошие подружки доверяют друг другу."
    victoria "И, ради хорошей подружки Мелани, я это видео никому не покажу..."
    victoria "Может быть, только Мистеру Дику..."
    # Мелани сидит злая, Моника в шоке
    music Master_Disorder
    img 17375
    with diss
    melanie_t "Я уничтожу эту сучку Викторию!"
    img 17394
    with diss
    mt "Она покажет ЭТО Дику?!"
    mt "?!?!?!"
    music Groove2_85
    img 17361
    with fade
    victoria "И еще, подружка Мелани..."
    img 17395
    with diss
    victoria "Я кажется тебе запрещала стирать мой рисунок с этой фотографии?"
    img 17367
    with fade
    melanie "..."
    victoria "Почему ты меня ослушалась?"
    victoria "Ты хочешь стать плохой подружкой?"
    # Мелани безразлично
    img 17340
    with diss
    melanie "Нет. Я просто забыла..."
    img 17396
    with diss
    victoria "На первый раз я тебя прощаю..."
    victoria "Но если такое повторится, я тебя накажу, подружка Мелани!"
    # она подходит с помадой к фото Мелани и подрисовывает член

    img 17397
    with fade
    w
    img 17398
    with diss
    victoria "Подружка Моника, отойди отсюда."
    m "..."
    img black_screen
    with diss
    sound vjuh3
    pause 1.0
    sound vjuh4
    pause 1.0
    music Groove2_85
    img 17399
    with fadelong
    sound vjuh3
    melanie "!!!"
    mt "!!!"
    img 17400
    with fade
    victoria "Так намного лучше."
    img 17426
    with diss
    w
    img 17401
    with fade
    sound highheels_short_walk
    victoria "Все, подружки, мне пора."
    victoria "Надеюсь, скоро снова увидимся."
    # Виктория уходит, Моника с Мелани вдвоем
    # Моника говорит
    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Master_Disorder
    img 17402
    with fadelong
    m "Мелани!"
    m "Мелани, ты в порядке? Ты слышишь меня?"
    img 17403
    with fade
    melanie "Миссис Бакфетт..."
    melanie "Я сотру стерву Викторию в порошок!"
    melanie "Я сделаю для этого абсолютно все!"
    melanie "!!!"
    music stop
    img black_screen
    with diss
    pause 2.0
    return

# мысли Моники, после того как ушла от Мелани, если Мелани отказала Виктории
label ep212_dialogues6_melanie_punishment_8:
    # не рендерить!!
    mt "Судя по всему, Мелани тоже еженедельно приносит Виктории деньги..."
    mt "Ей это делать гораздо проще! У нее они есть!"
    mt "И она не спешит делиться со мной!"
    mt "!!!"
    return

# мысли Моники, после того как ушла от Мелани, если сцена была проиграна полностью
label ep212_dialogues6_melanie_punishment_9:
    # не рендерить!!
    mt "Никогда не видела Мелани такой обозленной..."
    mt "Даже после того девичника..."
    mt "Виктория мерзкая сучка!"
    mt "Ненавижу ее!"
    mt "!!!"
    return

label ep212_dialogues6_melanie_punishment_9a:
    if act=="l":
        return
    melanie "Миссис Бакфетт... Пожалуйста..."
    melanie "Я хочу побыть одна!"
    return False

# через несколько дней после фотосессии в наряде "Королева сердец"
# Моника заходит в свой отдел отчетов
label ep212_dialogues6_melanie_punishment_10:
    # офис полон сотрудников, несколько из них (серая мышка, близняшки и китаянки Лин) стоят в кучке возле стола
    # они что-то рассматривают на столе и обсуждают
    music Blue_Ska
    img 17404
    with fadelong
    w
    img 17425
    with fade
    w
    img 17405
    with diss
    w1 "Ой... Какой кошмар!!!" # серая мышка
    w3 "А я и не удивлена!" # одна из близняшек
    img 17406
    with diss
    w3 "Это еще только начало!"
    w4 "Да-да! Позже будут публиковать фотографии еще хуже! Вот увидите!" # вторая близняшка
    sound highheels_short_walk
    img 17407
    with fade
    w
    img 17408
    with diss
    w7 "Тихо!" # китаянка Лин
    music Groove2_85
    sound Jump1
    img 17409
    with diss
    w
    # они видят Монику и замолкают, все смотрят на нее
    img 17410
    with fade
    mt "Это еще что такое?!"
    mt "Почему эти никчемные сотрудники так на меня смотрят?!"
    # подбегает подхалим
    music Sneaky_Snitch
    sound man_steps
    img 17411
    with diss
    w5 "Миссис Бакфет! Вы сегодня прекрасно выглядите!" # подхалим Джон
    w5 "Хотите чашечку горячего кофе?"
    music Groove2_85
    img 17412
    with fade
    m "Нет."
    m "Что здесь происходит?!" # сердито
    m "Почему половина офиса не на рабочих местах?!" # включаем большого босса
    # подбегает Гретта
    sound highheels_short_walk
    img 17413
    with diss
    w6 "Миссис Бакфетт, а они сегодня целый день ничего не делают!" # Гретта
    w6 "Только сидят и сплетничают!"
    music Pyro_Flow
    img 17414
    with fade
    m "Так! Быстро все за работу!!!"
    m "Или я уволю вас всех сегодня же!!!"
    m "!!!"
    music Groove2_85
    img 17415
    with diss
    w5 "Не понятно, за что они деньги получают!"
    w5 "Ничего не делают!"
    w5 "Целый день сегодня сидят и какой-то неприличный журнал обсуждают!"
    # в разговор вмешивается айтишник
    w2 "Гретта, они читают наш журнал."
    w2 "В котором мы работаем."
    w5 "А? Наш?!"
    music Loved_Up
    img 17416
    with fade
    w2 "Кстати, Миссис Бакфетт..."
    w2 "Отличная фотосессия получилась!"
    img 17417
    with diss
    w5 "Согласен на все сто."
    w5 "Это лучшее, что я видел в своей жизни, Миссис Бакфетт!"
    img 17418
    with fade
    m "Ты о чем?"
    w5 "Вам очень идет то красное платье..."
    w2 "И корона. Вы как настоящая королева на снимках."
    # Моника сначала не понимает, о чем они, но постепенно до нее доходит
    music Groove2_85
    img 17419
    with diss
    mt "Красное платье и корона?"
    mt "???"
    mt "?!?!?!"
    music stop
    sound plastinka1b
    img 17420
    with hpunch
    mt "ЧТОООООО?!"
    # шок, злость
    # потом орет на всех
    music Power_Bots_Loop
    img 17421
    with fade
    m "Быстро все за работу!!!"
    m "!!!"
    m "Бездельники!!!"
    m "!!!!!"
    # идет в свой кабинет
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Pyro_Flow
    img 17422
    with fadelong
    mt "Боже!"
    mt "Какой кошмар!"
    mt "Теперь все эти никчемные сотрудники видели мои фото с той ужасной фотосессии!!!"
    mt "!!!"
    img 17423
    with fade
    mt "Это все Бифф!"
    mt "Если бы не его дурацкая смена курса журнала!"
    mt "Никто и никогда не увидел бы подобных фотографий Моники Бакфетт!"
    mt "Потому что их не было бы!!!"
    mt "!!!"
    img 17424
    with diss
    mt "Я ненавижу этого мерзавца Биффа!"
    mt "Ненавижу!"
    mt "Убью его!"
    mt "!!!"
    mt "!!!!!!"
    return
