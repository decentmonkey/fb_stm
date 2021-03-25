default victoriaMonicaAdmin1 = False  # у Виктории и админа была встреча в кафе
default victoriaMonicaAdmin2 = False  # админ пялил Монику, думая, что это Виктория

default victoriaMonicaAdmin1CumZone = 0

#call ep216_dialogues6_victoria_admin_1() # рабочий кабинет Моники, заходит админ, потом кафе с Викторией
#call ep216_dialogues6_victoria_admin_2() # рабочий кабинет Моники, снова заходит админ
#call ep216_dialogues6_victoria_admin_3() # Моника возле дома Виктории, глазик, до сцены с админом у Виктории дома
#call ep216_dialogues6_victoria_admin_4() # сцена в апартаментах Виктории
#call ep216_dialogues6_victoria_admin_5() # Моника возле дома Виктории, мысли, после сцены с админом у Виктории дома
#call ep216_dialogues6_victoria_admin_6() # встреча с админом на работе после сцены с ним у Виктории дома



# при условии, что была сцена в апартаментах Виктории
# рабочий кабинет Моники
label ep216_dialogues6_victoria_admin_1:
    # Моника сидит за столом, Биг Босс
    # стук в дверь, заходит админ и неуверенно спрашивает
    fadeblack
    sound snd_door_knock
    pause 1.5
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    imgfl 40281
    w2 "Миссис Бакфетт, можно вопрос?"
    imgf 20372
    mt "Чего этому бездельнику от меня нужно?!"
    music Stealth_Groover
    mt "Как тяжело быть важным Боссом!"
    mt "Все от меня чего-то хотят!"
    imgd 20369
    mt "Достали со своими глупостями!"
    mt "Жалкие, никчемные людишки!"
    mt "!!!"
    imgf 40284
    m "Что ты хотел?"
    m "Говори быстрее, у меня много работы!"
    music Marty_Gots_a_Plan
    imgd 20338
    w2 "Я тут это..."
    w2 "В общем, хотел отпроситься..."
    w2 "Мне... Кхм... Мне надо отлучиться по работе..."
    # Моника злобно на него смотрит
    music Stealth_Groover
    img 20808
    m "Что значит 'по работе надо'?!"
    m "Твое рабочее место в этом отделе!"
    m "Куда ты собрался?! Рабочий день еще не окончен!"
    if monicaBitch == True:
        imgd 40283
        m "Весь этот отдел - одни никчемные бездельники!"
        m "И ты - самый главный бездельник здесь!"
    imgd 40282
    w2 "Но я... Я ненадолго..."
    m "Все! Иди отсюда!"
    m "У меня нет времени на тебя!"
    img 40285
    m "В отличие от всех вас, бездельников, Я работаю тут целыми днями!"
    m "!!!"
    imgd 40286
    w2 "Спасибо, Миссис Бакфетт..."
    music Marty_Gots_a_Plan
    imgf 40287
    sound man_steps
    w2t "Черт! Пронесло! Она отпустила меня!"
    w2t "Я думал она меня съест!"
    # админ уходит
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Pyro_Flow
    imgf 20251
    mt "Никчемные!"
    mt "Бесполезные!"
    mt "Все до единого!"
    mt "!!!"
    # смена кадра, спустя некоторое время
    # кафе, новая локация
    # Виктория и админ сидят в кафе за столиком
    # Виктория мило ему улыбается, он смущенный, ведет себя неловко, растерянно
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_75
    scene black_screen
    with Dissolve(1)
    music Marty_Gots_a_Plan
#    music Lobby_Time
    imgfl 40305
    w
    imgf 40306
    w2 "М-мисс Виктория..."
    w2 "Ваше предложение встретиться - это так... Такая неожиданность для меня..."
    w2 "Вы, наверное, хотели, чтобы я сделал какую-то работу?"
    imgd 40307
    victoria "Ну о чем ты говоришь?"
    victoria "Неужели я не могу просто так, без повода, встретиться с понравившимся мне мужчиной?"
    imgd 40308
    victoria "Кстати, как тебя зовут?"
    imgf 40309
    w2 "Я Эрик... То есть Йорик!"
    w2 "Эрик мой брат и... Я..."
    w2 "Эм..." # стесняется
    imgd 40310
    victoria "Какое интересное имя. Оно тебе очень идет!"
    w2 "Да? С-спасибо, Мисс Виктория."
    imgf 40311
    victoria "Ты можешь называть меня просто Виктория."
    img 40312
    w2 "Д-да... Х-хорошо, Ми... То есть, Виктория..."
    imgd 40313
    victoria "А чем ты увлекаешься, Йорик?"
    w2 "Я? О, я очень люблю все, что связано с репликациями многоуровневых реляционных баз данных!"
    fadeblack 1.5
    music Loved_up
    imgf 40313
    victoria "Правда?! Как интересно!"
    img 40314
    w2 "Да!.."
    w2 "То есть... А вам и правда интересно, Ми... Виктория?.."
    imgd 40315
    victoria "Конечно! Я обожаю все, что связано с базовыми многоуровнями! Камеры, например..."
    imgd 40316
    w2 "О, это здорово! Девушки редко этим интересуются!"
    w2 "А многовложенными компьютерными сетями вы тоже интересуетесь, Виктория?"
    imgf 40317
    victoria "Да, но я боюсь, что не настолько умна, чтобы хорошо в них разбираться..."
    victoria "Во взламывании компьютеров..."
    imgd 40318
    w2 "Да чего там разбираться?"
    w2 "Любой компьютер можно легко взломать за считанные минуты!"
    music Marty_Gots_a_Plan
    imgd 40319
    victoria "Серьезно?! Не может быть!"
    victoria "Ты такой умный!"
    victoria "Неудивительно, что ты работаешь в таком престижном офисе!"
    victoria "Это, наверное, так сложно?"
    imgd 40320
    w2 "Неее... Это все ерунда... Работа элементарная, раз плюнуть..."
    # Виктория в притворном восхищении
    music Loved_up
    imgf 40321
    victoria "Ты очень талантливый, Йорик!"
    victoria "Твои таланты могли бы пригодиться абсолютно любому! Даже мне. Но об этом позже..."
    victoria "Расскажешь мне про свою девушку?"
    # админ в смущении
    music Marty_Gots_a_Plan
    imgd 40322
    w2 "Я... Кхм... У меня..."
    w2 "Я знаю все об отношениях с девушками, Виктория..."
    imgd 40323
    w2 "Я видел много фильмов про это..."
    w2 "Про то как... Девушки и мужчины... Это..."
    imgd 40324
    victoria "Ты так хорошо разбираешься в отношениях?"
    victoria "А что за фильмы? Ты их много посмотрел?"
    imgf 40325
    w2 "Все..."
    victoria "А девушка у тебя есть, Йорик?"
    w2 "Нет..."
    # она удивленно
    music Loved_up
    imgd 40326
    victoria "А почему? Ты такой красивый, умный! Так много всего умеешь..."
    # он удивленно
    imgf 40327
    w2 "Вы правда так считаете, Виктория?"
    imgd 40328
    victoria "Да, Йорик... Правда..."
    victoria "Хочешь встретиться со мной еще раз, Йорик?"
    $ victoriaMonicaAdmin1 = True # у Виктории и админа была встреча в кафе
    # кадр на его удивленное лицо
    # смена кадра
    # офис Моники, она сидит психует на админа
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Тем временем...")) from _rcall_textonblack_76
    scene black_screen
    with Dissolve(1)
    music Stealth_Groover
    imgfl 22392
    mt "Вот так взять и уйти посреди рабочего дня!"
    mt "За что только он получает здесь деньги?!"
    mt "Жалкий неудачник!!!"
    imgf 40304
    mt "Самый жалкий из всех этих офисных бездельников!!!"
    mt "Никчемный!!!"
    mt "!!!"
    return


# след. приход Моники на работу в офис
# рабочий кабинет Моники
label ep216_dialogues6_victoria_admin_2:
    # Моника за своим рабочим столом
    # к ней подходит Юлия
    fadeblack 1.5
    music Groove2_85
    imgfl 30586
    julia "Миссис Бакфетт..."
    imgf 30587
    mt "Чего она опять ко мне лезет?!"
    # если у Моники отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях."))
        #
        imgd 20369
        mt "Сколько уже можно?!"
        mt "!!!"
        music Hidden_Agenda
        imgf 30585
        m "Да, милая. Ты что-то хотела?"
        #
    # если у Моники нет отношений с Юлией
    else:
        music Stealth_Groover
        imgd 20369
        mt "Никчемная бывшая гувернантка! Фи!"
        imgf 30585
        m "Что?"
        #

    fadeblack
    sound highheels_run1
    pause 2.0
    music Groove2_85
    imgf 30627
    julia "Миссис Бакфетт, сейчас звонила Мисс Виктория..."
    julia "Она сказала, что ждет Вас у себя."
    img 40265 vpunch
    mt "Черт!"
    mt "!!!"

    # если у Моники отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        music Hidden_Agenda
        imgf 40288
        julia "Миссис Бакфетт, вы говорили, что возьмете меня с собой в гости к Мисс Виктории..."
        julia "Я с большим удовольствием встретилась бы с ней!"
        img 40289
        mt "Дура!"
        imgf 40290
        m "Нет, Юлия. В другой раз..."
        # Юлия радостно
        imgd 40272
        julia "Обещаете?!"
        # Моника сквозь зубы
        imgd 40273
        m "Конечно, милая."
        # Юлия довольно чмокает Монику в губы и уходит на свое рабочее место
        fadeblack 1.5
        music Loved_up
        imgfl 40274
        sound kiss1
        w
        imgf 40275
        sound highheels_short_walk
        w
        imgd 40276
        mt "Боже!"
        mt "Надо же быть такой идиоткой!!!"
        mt "И как я только выношу ее присутствие?!"
        mt "!!!"
        #
    else:
        # если у Моники нет отношений с Юлией
        # Моника рявкает на нее раздраженно
        music Pyro_Flow
        imgd 40277
        m "Я поняла!"
        m "Иди занимайся своими отчетами!!!"
        # Юлия испуганно
        imgd 40278
        julia "Д-да, Миссис Бакфетт..."
        imgf 22338
        sound highheels_short_walk
        w
        # Юлия уходит на свое рабочее место
        #

    # Моника сидит злая как черт
    fadeblack 1.5
    music Stealth_Groover
    imgfl 40291
    mt "Что этой больной извращенке нужно от меня?!"
    mt "Меня тошнит от одного ее вида!"
    mt "И теперь мне снова нужно ехать к ней!"
    mt "!!!"
    sound snd_door_knock
    mt "Если бы я могла..."
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    # ее мысли прерывает стук в дверь
    # заходит админ
    imgf 40292
    w2 "Миссис Бакфетт..."
    m "Чего тебе?!"
    m "Не видишь, я занята?!"
    imgd 40285
    m "Я ухожу на важную встречу!"
    m "!!!"
    imgd 40293
    w2 "Я просто хотел... Кхм.. Отпроситься не пару часов..."
    music Stealth_Groover
    img 40283
    m "Что?! Снова?!"
    m "Это уже не в первый раз!"
    m "Причем в рабочее время!"
    m "Куда это ты все время ходишь?!"
    # он смущенно
    imgf 40294
    w2 "К девушке..."
    # Моника изображает удивление
    imgd 40295
    m "К девушке?! Ты серьезно?!"
    m "Не смеши меня!"
    m "Такой, как ты, не может нравится ни одной девушке на свете!"
    imgd 40296
    m "Ты хоть видел себя в зеркало?!"
    m "Никому не нужный неудачник!"
    m "!!!"
    imgf 40297
    w2 "Я..."
    # Моника его перебивает
    img 40282
    m "И вообще!.."
    m "У меня компьютер не работает уже сколько времени, а он отпрашивается!!!"
    w2 "Миссис Бакфетт, починить Ваш компьютер я могу быстро..."
    imgd 40286
    w2 "Там нужно всего лишь заменить жесткий диск."
    w2 "Это стоит всего тысячу долларов."
    music Pyro_Flow
    img 40298 hpunch
    m "Ты идиот?!"
    m "Какой еще диск?!"
    m "Он просто не включается!!!"
    m "Значит не работает кнопка, которая его включает!!!"
    m "!!!"
    music Stealth_Groover
#    imgd 40299
    imgd 40300
    w2 "..."
    m "И откуда такая сумма?!"
    imgd 40301
    w2 "Я позвонил в компанию, которая занимается поставкой комплектующих."
    w2 "Они сказали, что Ваша организация оплачивает именно такую сумму."
    w2 "Нужна только Ваша подпись, Миссис Бакфетт..."
    # Моника недовольно смотрит на него
    imgd 40302
    mt "Подпись?!"
    mt "Твою мать!"
    mt "Что на это скажет Биф?!"
    mt "Он подумает, что я решила украсть эти деньги!"
    # орет на админа
    music Pyro_Flow
    img 40283 hpunch
    m "Конечно, я знаю про подпись!"
    m "Я тут начальник, я знаю ВСЕ!"
    imgd 40303
    m "Я должна была бы уволить тебя прямо сейчас!"
    m "Но мне сейчас не до этого!"
    m "У меня есть более важные дела!"
    m "Не отвлекай меня!"
    img 40282
    m "Я без тебя поменяю эту кнопку!!"
    m "ИДИ ОТСЮДА!!!"
    w2 "Спасибо, Миссис Бакфетт..."
    # админ уходит
    fadeblack
    sound snd_door_open1
    pause 2.0
    music Stealth_Groover
    imgf 40276
    mt "Никчемный жалкий неудачник!"
    mt "!!!"
    mt "Так, Моника, соберись!"
    imgd 20362
    mt "Тебе надо ехать к сучке Виктории!"
    mt "Ненавижу эту мелкую дрянь!"
    mt "!!!"
    # если у Моники отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        imgd 20362
        mt "Еще эта Юлия лезет со своей дружбой с Викторией!"
        mt "Дура!!!"
#    $ log1 = _("Поехать к Виктории.")
    return

# Моника возле дома Виктории, глазик
label ep216_dialogues6_victoria_admin_3:
    # не рендерить!!
    mt "Настанет тот день, Моника, когда ты избавишься от сучки Виктории!"
    mt "Это будет один из самых счастливых дней!"
    mt "Не могу дождаться этого момента!"
    mt "А пока я вынуждена терпеть ее присутствие в своей жизни..."
    return

# при клике на дом Виктории
# апартаменты Виктории
label ep216_dialogues6_victoria_admin_4:
    # включется сцена, где Виктория разговаривет с Йориком в своей спальне
    # она с ним флиртует
    sound highheels_short_walk
    fadeblack 2.0
    music Groove2_85
    imgfl 40632
    victoria "Йорик, я так рада, что смог отпроситься с работы!"
    victoria "Я так переживала, что ты не сможешь прийти!"
    w2 "Нууу... Это было непросто."
#    imgf 40633
    w2 "Ваша подруга, Миссис Бакфетт, не хотела меня отпускать..."
    w2 "Она так ругалась!"
    w2 "Я вообще думал, что она меня уволит!"
    # Виктория ехидно
    music Loved_up
    imgd 40634
    victoria "Ну что ты, Йорик!"
    victoria "Моя подружка Моника очень хорошая."
    victoria "Она никогда так не поступила бы с тобой."
    # Виктория подходит к админу ближе, флиртует
    imgd 40635
    w2 "Ну, не знаю."
    imgf 40636
    victoria "Йорик... Не переживай. Все будет хорошо."
    victoria "Ведь ты такой милый..."
    victoria "Такой умный, талантливый..."
    victoria "И такой благородный..."
    # админ смущаясь
    music Groove2_85
    imgd 40637
    w2 "Виктория, я..."
    w2 "Я подумал о том что ты попросила меня сделать..."
    w2 "Это... Довольно опасно и я..."
    # Виктория перебивает его
    img 40638
    victoria "Тссссс..."
    victoria "Я считаю, что ты заслуживаешь внимания такой девушки, как я, Йорик..."
    imgd 40639
    victoria "Ты ведь такой умный и красивый..."
    victoria "И смелый..."
    victoria "Докажешь мне, что ты смелый?"
    imgf 40640
    w2 "Я... Я правда не знаю..."
    # Виктория соблазняет админа
    victoria "Тссссс..."
    sound Jump2
    music Marty_Gots_a_Plan
    img 40641 hpunch
    victoria "Ты ведь хочешь попробовать, что такое встреча с настоящей девушкой, правда?" # кладет руку ему на член
    w2 "Я..."
    imgd 40642
    victoria "Ты ведь достаточно храбрый?"
    w2 "Да! Да! Да!"
    w2 "Я хочу! Я очень хочу!"
    imgf 40643
    victoria "Ты достаточно смелый, чтобы помочь мне и сделать, что я прошу?"
    w2 "Да! Я все сделаю!"
    sound snd_door_bell1
    w
    # звонок в дверь
    # админ испуганно
    music Groove2_85
    imgd 40644
    w2 "Ой, кто это?"
    w2 "Вы кого-то ждете, Виктория?"
#    music Groove2_85
    victoria "Подожди минутку."
    # уходя, говорит ему, улыбается и посылает воздушный поцелуй
    imgf 40645
    w
    sound kiss1
    imgd 40646
    victoria "Можешь пока раздеваться, Йорик, я сейчас вернусь..."
    imgf 40647
    w
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_lift
    pause 2.0
    music Stealth_Groover
    # Виктория выходит, админ растерянно смотрит ей вслед
    # смена кадра, звук отворяющейся двери (или лифта-?)
    # холл апартаметов Виктории, в дверях стоит Моника
    imgf 40648
    mt "Я снова в этой отвратной розовой квартире! Фи!"
    mt "Лицемерная мелкая дрянь!"
    imgd 40649
    mt "Притворяется невинной овечкой, а сама - демон в юбке!"
    mt "Ненавижу ее!!!"
    mt "Что ей снова нужно от меня?!"
    mt "!!!"
    # Виктория встречает Монику с улыбочкой
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 40650
    victoria "Тссс, подружка!"
    victoria "Мне очень нужна твоя помощь..."
    victoria "Ты же не откажешь мне?"
    victoria "Ты ведь хорошая подружка?"
    # Моника подозрительно
    imgf 40651
    m "Какая помощь?"
    imgd 40652
    victoria "Ой, подружка, для тебя это сущий пустяк!"
    victoria "Там есть один человек, он кое-что может для меня сделать..."
    victoria "Для этого мне надо его соблазнить."
    music stop
    sound plastinka1b
    img 40653 hpunch
    m "Соблазнить?"
    music Groove2_85
    imgd 40654
    victoria "Да, подружка Моника. Но я ведь не могу изменять Мистеру Дику!"
    victoria "Поэтому ты меня подменишь, подружка."
    img 40655
    m "Что?!"
    m "Что все это значит?"
    music Master_Disorder
    imgf 40656
    victoria "Это значит, что подружка выручит меня..."
    victoria "Ты ведь хочешь быть для меня хорошей подружкой?"
    imgd 40657
    m "..."
    menu:
        "Да...":
            pass
    sound highheels_short_walk
    imgf 40658
    m "Да, я хорошая подружка..."
    victoria "Я тебе сейчас расскажу, что надо делать, хорошая подружка Моника..."
    # затемнение
    # смена кадра на спальню Виктории
    # Виктория заходит в комнату к админу, он уже голый, стеснительно прикрывается
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 40710
    w2 "Кто это был, Виктория?"
    # она проходит мимо него, берет в руки повязку на глаза
    imgd 40711
    victoria "Ошиблись дверью, Йорик..."
    victoria "А теперь расслабься... Давай немного поиграем..."
    # подходит к нему, завязывает ему глаза
    sound snd_fabric1
    fadeblack 1.5
    music Loved_up
    imgfl 40712
    w2 "Что? Зачем? Я хочу видеть вас..."
    victoria "Возможно, в следующий раз, а сейчас..."
    victoria "Я хочу чтобы эта встреча была особенной..."
    imgf 40713
    victoria "Просто отдайся своим ощущениям..."
    victoria "Только не снимай повязку, иначе ты меня расстроишь и я не буду больше играть с тобой."
    w2 "Д-да, В-виктория... Х-хорошо..."
    victoria "Расслабься, Йорик... Не нервничай..."
    # прикасается к нему, проводит рукой по его груди, прижимается к нему
    imgd 40714
    victoria "Почувствуй мои прикосновения, мое тело..."
    victoria "Я так хочу, чтобы ты ласкал меня, Йорик."
    victoria "Секунду, я сейчас сниму платье..."
    # отстраняется от него и смотрит в сторону двери, подзывает к себе пальцем Монику
    # Моника заходит уже голая, останавливается и в шоке смотрит на админа
    imgf 40715
    w
    fadeblack 1.5
    sound plastinka1b
    img 40716 vpunch
    mt "ЧТООООО?!"
    mt "Этот никчемный бездельник?!"
    music Pyro_Flow
    mt "Какого черта ОН ТУТ ДЕЛАЕТ?!"
    mt "?!?!?!"
    mt "Он для ЭТОГО отпрашивался?!"
    mt "Сволочь!!!"
    img 40717
    mt "!!!"
    mt "!!!!!"
    mt "А эта дрянь?! Зачем он ей нужен?!"
    mt "Что вообще тут происходит?!"
    mt "???"
    # админ нетерпеливо тянет руки в сторону Виктории
    music Loved_up
    imgf 32626
    w2 "Виктория, иди ко мне скорее!"
    w2 "Я так хочу этого!"
    # Виктория жестом указывает Монике подойти к админу
    imgd 32625
    victoria "О, да Йорик!"
    victoria "Прикоснись к моей груди, я так этого хочу!"
    # Моника с отвращением на лице подходит к нему, Виктория стоит сбоку рядом
#    img 40417
#    w
    imgd 32627
    w
    imgd 32628
    w
    imgd 32715
    w
    imgd 32629
    mt "О Боже!"
    sound Jump1
    imgd 32630
    mt "Какой кошмар!"
    imgd 32631
    mt "Какой же он мерзкий и жалкий!"
    # он тянет руки и хватается за ее грудь, начинает мять
    sound Jump2
    imgd 32632
    mt "Фуууу!!!"
    mt "!!!"
    imgd 32633
    w2 "О, Виктория!!!"
    w2 "Твоя грудь! Она потрясающая!#it"
    w2 "Такая упругая, такая..."
    victoria "О, Йорик... Поцелуй же ее скорее!#it" # Виктория говорит из-за плеча Моники, будто это она
    # админ тянется губами к ее груди и целует
    music Loved_up
    imgf 32634
    sound kiss1
    w
    imgd 32635
    sound lick3
    w
    # Моника смотрит с отвращением, потом зло на Викторию
    imgd 32636
    victoria "О, да!!!"
    victoria "Это потрясающе!"
    victoria "Еще разочек!"
    imgf 32635
    sound lick3
    w
    imgd 32634
    sound kiss1
    w
    # та ехидно смотрит на нее и снова обращается к админу
    imgf 32637
    victoria "А теперь потрогай мою киску, Йорик..."
    victoria "Хочешь поцеловать ее?#it"
    w2 "Да... Сейчас..."
    # админ тянет руку между ног Монике и трогает ее киску пальцами
    sound Jump2
    img 32638 vpunch
    w
    imgf 32639
    w
    imgd 32640
    mt "Он прикасается ко МНЕ, Монике Бакфетт! Своими грязными руками!"
    mt "Мой подчиненный!"
    mt "Лапает МЕНЯ!"
    mt "Своего Босса!!!"
#    mt "ААААААА!!!"
    # потом опускается на колени и лижет
    fadeblack 1.5
    music Loved_Up2
    imgfl 32641
    w

    $ localSoundVolume = 0.75
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Licking1_1 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Licking1_1.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Licking1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32645
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Licking1_2 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Licking1_2.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Licking1_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32642
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Licking1_3 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Licking1_3.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Licking1_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32643
    victoria "Ооооо! Даааа!!!"
    victoria "Еще! Ещееее!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Licking1_4 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Licking1_4.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Licking1_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Licking1_5 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Licking1_5.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Licking1_5
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Licking1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Licking1_6 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Licking1_6.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Licking1_6
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32644
    w2 "О, ваша киска такая горячая!"
    w2 "Хочу скорее попробовать ее!#it"
    imgf 32646
    victoria "Да, Йорик! Мне не терпится почувствовать твой член внутри себя!"
    imgd 32647
    victoria "Ох, пойдем скорее на кровать!"
    victoria "Я уже вся влажная, я так хочу тебя!"
    music Power_Bots_Loop
    img 32648 vpunch
    mt "Сучка!"
    mt "Я убью эту тварь!"
    mt "!!!"
    # админ поднимается
    fadeblack 1.5
    music Groove2_85
    imgfl 32649
    w2 "Пошли скорее, Виктория!"
    w2 "Куда идти? Я ничего не вижу!"
    # Моника зло на нее смотрит
    imgf 32650
    victoria "Я отведу тебя."
    mt "!!!"
    # админ тянет руку, Моника берет его ладонь и идут к кровати
    # Моника ведет админа к кровати
    sound vjuh3
    imgd 32651
    victoria "Давай руку, Йорик..." # Виктория протягивает руку Моники
    imgd 32652
    w
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Loved_up
    imgfl 32653
    w
    # Моника и админ стоят у кровати, Виктория садится с краю кровати, она остается одетой
    sound Jump1
    imgf 32655
    w
    # указывает Монике пальцем, что ей нужно залезть на кровать
#    sound vjuh3
    imgd 32656
    w
    imgd 32657
    w
    # Моника встает коленями на кровать, лицом к Виктории, злобно на нее смотрит
    fadeblack 1.5
    music Loved_up
    imgfl 32658
    w
    imgf 32659
    w2 "Виктория, а можно я сниму повязку?"
    music stop
    sound plastinka1b
    img 32660 vpunch
    mt "НЕТ!"
    mt "!!!"
    music Groove2_85
    w2 "Мы ведь уже поиграли немного?"
    w2 "Я так хочу увидеть твое обнаженное тело!"
    imgd 32661
    victoria "Нет, милый Йорик..."
    victoria "Мы еще играем..."
    victoria "В своих фильмах ты уже все видел."
    victoria "Я хочу подарить тебе ощущения!"
    victoria "Я скажу, когда можно будет снять повязку."
    victoria "Идем ко мне на кровать, я уже жду тебя..."
    music Loved_up
    fadeblack 1.5
    # админ трогает кровать рукой, натыкается на ногу Моники, потом лезет к ней на кровать
    imgf 32662
    w2 "О, я не верю, что сейчас я буду делать ЭТО!"
    sound Jump1
    imgd 32663
    w2 "Чувствую себя героем одного из тех фильмов, которые я смотрел..."
    imgd 32664
    w2 "Там как раз было про такие игры..."
    imgf 32665
    sound snd_woman_laugh3
    victoria "Хи-хи-хи! Да, я люблю поиграть..."
    victoria "Пойдем ко мне скорее!"
    victoria "Войди в меня!"
    # Моника встает на четвереньки (догги стайл)
    # админ лапает ее, Моника психует
    sound vjuh3
    img 32666 hpunch
    w
    music Pyro_Flow
    img 32667
    mt "Я ему оторву яйца!!!"
    mt "УВОЛЮ!!!"
    mt "УБЬЮ СУЧКУ ВИКТОРИЮ!!!"
    mt "УНИЧТОЖУ ЭТОГО НЕУДАЧНИКА!!!"
    mt "МЕРЗКАЯ СКОТИНА!!!"
    mt "НЕНАВИЖУ ВСЕХ!!!"
    mt "!!!"
    music Loved_up
    imgf 32668
    victoria "А теперь попробуй найти мою киску! Хи-хи-хи!"
    sound snd_woman_laugh3
    w2 "Я совсем ничего не вижу..."
#    w2 "Это ваша ножка... Так..."
#    victoria "А теперь выше..."
    w2 "О, какая у вас упругая попа, Виктория. Она такая клевая!#it"
    # гладит и мнет руками ягодицы Моники
    imgd 32669
    w
    sound hlup25
    imgd 32670
    w
    sound hlup25
    imgd 32669
    w
    sound hlup25
    imgd 32670
    w
    sound hlup25
    imgf 32671
    w2 "Вы были правы, с закрытыми глазами такие интересные ощущения!"
    w2 "Я представлял вас совсем другой, Виктория!"
    w2 "А на самом деле вы оказались в тысячу раз круче, чем я мог предположить!"
    w2 "Это так офигенно!!!"
    # Виктория зло смотрит на Монику
    music Master_Disorder
    imgd 32672
    victoria "..."
    # Затем, снова натягивает улыбочку
    music Groove2_85
    imgd 32673
    victoria "Да, я такая!"
    victoria "Входи же в мою киску скорее, Йорик!"
    victoria "Я больше не могу ждать!"
    # админ рукой находит киску Моники и пытается ткунться в нее членом
    # промазывает и тыкается куда-нибудь в ягодицу или ногу, член сгибается
    music Loved_up
    imgf 32674
    w
    imgd 32675
    w
    imgf 32676
    w
    sound Jump2
    img 32677 vpunch
    w
    sound snd_woman_laugh3
    imgf 32678
    victoria "Хи-хи-хи! Мимо!"
    w2 "Ох, черт!"
    # снова тыкается не туда
    imgd 32676
    w
    sound Jump2
    img 32677 vpunch
    w
    imgf 32678
    victoria "Снова мимо!"
    victoria "Ну найди же мою влажную киску скорее!"
    victoria "Она так хочет твой огромный член!"
    w2 "Сейчас... Я сейчас..."
    # снова тыкается и снова мимо
    imgd 32676
    w
    sound Jump2
    img 32677 vpunch
    w
    imgd 32678
    victoria "Ох, Йорик, я не могу больше терпеть!"
    victoria "Давай я тебе помогу, милый!"
    w2 "Да... Я совсем ничего не вижу..."
    victoria "Я направлю твой огромный член в мою киску своей рукой..."
    # Моника вопросительно смотрит на Викторию
    music Pyro_Flow
    img 32679
    mt "Какого хрена?!"
    mt "Я еще должна ему помогать?!"
    # Виктория пристально на Монику и указывает рукой на член админа
    imgd 32680
    mt "!!!"
    menu:
        "Взять член админа и засунуть его в свою киску.":
            pass
    imgd 32667
    mt "Я что, должна прикасаться к его отростку?!"
    mt "?!?!?!"
    mt "ФУУУУ!!!"
    mt "Не могу поверить, что все это происходит на самом деле!"
    mt "Какой-то нелепый кошмарный сон!"
    imgd 32681
    mt "Моим прекрасным телом сейчас овладеет какое-то ничтожество!"
    mt "Которое работает в моем подчинении!!!"
    mt "Он даже мечтать не мог о подобном!!!"
    mt "Мерзкое животное! Плебей!!!"
    mt "!!!"
    # Моника тянется рукой к члену админа и направляет в свою киску
    fadeblack 1.5
    music Loved_up
    imgfl 32683
    w
    imgf 32684
    w
    imgd 32682
    w2 "Ооооох!!!"
    w2 "Ооооо!!!"
    w2 "Мне кажется, я сейчас кончу от одних твоих прикосновений, Виктория!"
    w2 "Какая ты офигенная!!!"
    # Моника вставляет его член в себя
    sound chpok2
    img 32685 hpunch
    w
    imgd 32686
    w
    # Виктория притворно стонет
    imgf 32687
    victoria "ДААААА!!!"
    # Моника, заткнув себе рот рукой (как в камере), молчит

    $ localSoundVolume = 0.75
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_1 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_1.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32688
    w
    imgf 32689
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_2 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_2.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32690
    w2 "ООООООО!!!"
    w2 "Ох, я не могу поверить! Я наконец-то трахаюсь!!!"
    w2 "Как тепло внутри твоей киски!!! Так влажно!!!"
    w2 "ООООО!!!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_3 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_3.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32695
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_4 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_4.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32691
    victoria "Ооооох как круууутоооо!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_5 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_5.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_5
    with fade
    w2 "Охренительно!!! ДААА!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_6 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_6.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_6
    with fade
    victoria "Ты настоящий зверь! Да!!!"
    victoria "ЕЩЕЕЕ!!! ДАААА!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_7 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_7.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_8 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_8.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_8
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 32692
    w
    sound drkanje5
    imgd 32693
    w
    imgd 32692
    w
    sound drkanje5
    imgd 32693
    w
    imgd 32692
    w
    sound drkanje5
    imgd 32693
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_VictoriaHome_Worker2_Monica_Sex1_1.ogg"
    scene black
    image videov_VictoriaHome_Worker2_Monica_Sex1_9 = Movie(play="video/v_VictoriaHome_Worker2_Monica_Sex1_9.mkv", fps=30)
    show videov_VictoriaHome_Worker2_Monica_Sex1_9
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Loved_Up2
    imgf 32694
    w2 "Оооо, я больше не могууу!!! Ааааа!!!"
    w2 "Я кажется сейчас кончуууу!!!"
    # Виктория издевательски смотрит на Монику


    # админ кончает
    imgd 32696
    victoria "Кончай в меня, Йорик! Давай!"
    victoria "Давай же! Сделай это для меня!"
    if melanieVictoriaMonicaTable2 == True:
        #
        $ notif(_("Виктория недовольна, что Моника попыталась оправдать Мелани и не стала втыкать в нее розу."))
        #
        victoria "Потом я вылижу твой огромный член!"
        victoria "Хочу скорее ощутить его вкус!"
    victoria "О, даааа!!!"

    menu:
        "Кончить внутрь Моники.":
            $ victoriaMonicaAdmin1CumZone = 1
            img 32697
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w2 "КОНЧААААЮЮЮЮ!!!"
            victoria "ААА!!!"
            img 32698
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan6
            w2 "ООО!!!"
            victoria "ДАААА!!!"
            sound squelch9
            imgd 32699
            w2 "ОООООО!!!!"
            pass
    # Моника в бешенстве, но молчит
    fadeblack 1.5
    music Power_Bots_Loop
    imgf 32700
    mt "!!!"
    mt "!!!!!"
    mt "!!!!!!!"
    if melanieVictoriaMonicaTable2 == True:
        $ notif(_("Виктория недовольна, что Моника попыталась оправдать Мелани и не стала втыкать в нее розу."))
        music Groove2_85
        imgd 32696
        victoria "А теперь дай мне скорее свой член!"
        victoria "О, быстрее, Йорик!"
        # админ выходит из Моники
        # та зло смотрит на Викторию, Виктория указывает ей на член админа
        music Master_Disorder
        imgd 32680
        victoria "!!!"
        img 32701
        mt "СУЧКА!!!"
        mt "НЕНАВИЖУ!!!"
        # Моника поворачивается к админу, смотрит с отвращением
        fadeblack 1.5
        music Loved_up
        imgfl 32702
        w
        imgf 32703
        mt "Как это все мерзко!!!"
        mt "!!!!!"
        # наклоняется и облизывает языком его член
        imgd 32704
        w
        sound lick3
        imgd 32705
        w
        imgd 32706
        w
        imgf 32707
        victoria "Мммм..."
        w2 "Оооох!!!"
        w2 "О, Виктория!"
        w2 "Я даже мечтать не мог об этом!"
        w2 "Аааах!!!"
        # Моника отстраняется и зло смотрит на админа
        imgd 32708
        victoria "Йорик! Я обожаю твой член!"
        victoria "Он такой обалденный! Мммм!!"

    fadeblack
    sound snd_fabric1
    pause 2.0
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    # затемнение
    # смена кадра, холл в апартаментах Виктории
    # Виктория с админом стоят у двери, Моника голая прячется за углом
    # Виктрия провожает админа, он в восторге
    imgfl 40659
    w2 "Виктория, это такой кайф!"
    w2 "Я не ожидал, что будет настолько круто!"
    w2 "Я в восторге!!!"
    imgf 40660
    victoria "Мне тоже очень понравилось, милый Йорик!"
    victoria "Мы обязательно с тобой повторим!"
    imgd 40661
    w2 "Ооо, да!"
    w2 "Я с большим удовольствием!!!"
    w2 "Один ваш звонок, Виктория, и я приеду, несмотря ни на что!"
    # Виктория строит глазки
    imgf 40662
    victoria "Даже если это будет рабочий день? Как сегодня?"
    music Marty_Gots_a_Plan
    imgd 40663
    w2 "Скажу боссу, что у меня важные дела по работе!"
    w2 "Она все равно не узнает, где я был на самом деле!"
    imgf 40664
    w2 "Вы же ей ничего не расскажете, Виктория?"
    victoria "Ну что ты, Йорик? Конечно же, нет!"
    sound snd_woman_laugh3
    victoria "Это будет наш с тобой маленький секретик! Хи-хи!"
    imgd 40665
    w2 "Да, прикольно!"
    w2 "Тогда до встречи!"
    imgd 40666
    sound kiss1
    w
    imgf 40667
    victoria "До встречи, Йорик..."
    # админ наклоняется к Виктории, чмокает ее в щеку и уходит
    # он уходит
    # Виктория подходит к Монике, та в шоке
    fadeblack
    sound2 snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 40668
    victoria "Подружка Моника хорошая."
    victoria "Она мне помогла."
    victoria "Тебе понравилось помогать мне, подружка?"
    music Pyro_Flow
    imgf 40669
    mt "Может, долбануть ее чем-нибудь потяжелее?"
    mt "И убежать..."
    mt "Все равно все подумают на админа..."
    mt "Черт... Уверена у этой сучки здесь спрятаны камеры..."
    mt "Слишком рискованно..."
    menu:
        "Понравилось.":
            pass
    imgd 40670
    m "Да..."
    victoria "Что 'да'? Понравилось?"
    m "Да! Очень!"
    # Виктория ехидно хихикает
    music Groove2_85
    imgf 40671
    sound snd_woman_laugh3
    victoria "Хи-хи-хи!"
    victoria "Я знала, подружка, что тебе понравится помогать мне."
    victoria "И поэтому ты не откажешь мне в помощи в следующий раз, когда я тебя позову."
    imgd 40672
    m "Этот... Он мой подчиненный..."
    m "А если он узнает о том, что это была Я?"
    imgf 40673
    victoria "Уверена, что ради нашей с тобой хорошей дружбы ты сможешь потерпеть небольшие неудобства, подружка."
    music Power_Bots_Loop
    img 40674
    mt "!!!"
    fadeblack 1.0
    sound snd_lift
    fadeblack 2.5
    $ victoriaMonicaAdmin2 = True # админ пялил Монику, думая, что это Виктория
    return

# после сцены с админом у Виктории дома, Моника возле дома Виктории, мысли
label ep216_dialogues6_victoria_admin_5:
    # не рендерить!!
    mt "В МЕНЯ!"
    mt "МИССИС МОНИКУ БАКФЕТТ!"
    mt "ГЛАВУ ЖУРНАЛА!"
    mt "БОССА!!!"
    mt "ТЫКАЛСЯ СВОИМ ГРЯЗНЫМ ОТРОСТКОМ КАКОЙ-ТО ЖАЛКИЙ!.."
    mt "ЖАЛКИЙ! НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    mt "ПЛЕБЕЙ!!!"
    mt "Я УБЬЮ ВИКТОРИЮ!!!"
    mt "НЕНАВИЖУ ЭТУ МРАЗЬ!!!"
    mt "!!!"
    return

# Моника приходит на работу на др. рабочий день
# отдел отчетов
label ep216_dialogues6_victoria_admin_6:
    fadeblack 1.5
    music Stealth_Groover
    imgfl 32709
    w
    imgf 32710
    w2 "Здравствуйте, Миссис Бакфетт!"
    # она молча просто зло на него смотрит
    m "!!!"
    # он непонимающе смотрит на нее
    imgd 32711
    w2 "Что-то не так, Миссис Бакфетт?"
    # она продолжает сверлить его взглядом
    music Pyro_Flow
    img 32712
    mt "ЖАЛКИЙ! НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    mt "ПЛЕБЕЙ!!!"
    m "НИЧЕГО!"
    m "!!!"
    # и проходит просто мимо
    # он смотрит ей вслед мечтательно
    sound highheels_short_walk
    imgf 32713
    w
    music Marty_Gots_a_Plan
    imgd 32714
    w2t "Виктория, конечно, клевая..."
    w2t "Но вот добраться бы до задницы Бакфетт..."
    w2t "О ней мечтают все!"
    imgd 32716
    w2t "Эх... Жаль, что это абсолютно невозможно..."
    return


label ep216_dialogues6_victoria_admin_6b:
    mt "ЖАЛКИЙ! НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    mt "ПЛЕБЕЙ!!!"
    return
