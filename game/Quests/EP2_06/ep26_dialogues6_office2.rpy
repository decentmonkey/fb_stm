# Марта
#
# Эмма
# Элла
# Джон
# Грета
# Лин

label ep26_dialogues6_office2_1_lift:
    menu:
        "Модный Журнал.":
            return 1
        "Офисы.":
            return 2
        "Вестибюль.":
            return 3
    return

label ep26_dialogues6_office2_1:
# Моника спускается вниз
# Итак, это здесь. Посмотрим.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 20213
    with fadelong
    mt "Итак, это здесь. Посмотрим."
    img 20214
    with diss
    mt "Очередная кучка никчемных людишек."
    mt "И теперь я их Босс!"
    img 20215
    mt "Наконец-то, Моника!"
    mt "Наконец-то!"
    img 20216
    with fade
    mt "..."
    mt "Итак..."
    music Pyro_Flow
    img 20217
    with diss
    m "ВСЕМ ВСТАТЬ!"

    # все встают и удивленно смотрят
    img 20218
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Sneaky_Snitch
    img 20219
    with fadelong
    w
    img 20220
    with fade
    w5 "Миссис Бакфетт?"
    # подбегает к Монике
    sound highheels_short_walk
    img 20221
    with diss
    w5 "Неожиданно видеть Вас здесь!"
    w5 "Чем мы обязаны Вашим вниманием?"
    sound highheels_short_walk
    img 20222
    with diss
    w5 "Могу-ли Я чем-то помочь Вам?"
    music Stealth_Groover
    img 20223 #1
    with fade
    m "Я Ваш новый Босс!"
    m "Вернее, я и так была Вашим Боссом, но я решила временно поработать здесь."
    m "Недолго."
    img 20224
    with diss
    m "Этот никчемный отдел привлек мое внимание и я собираюсь навести здесь порядок."
    m "Где здесь расположен кабинет Босса?"
    music Sneaky_Snitch
    img 20225
    with fade
    w5 "Мэм, это очень неожиданно и..."
    music Pyro_Flow
    img 20226
    with diss
    m "Замолчи и ответь где кабинет."
    img 20227
    with diss
    w5 "Мэм, прямо по коридору."
#    m "Ясно, а сейчас всем за работу!"
    sound snd_bodyfall
    img 20228
    with fade
    m "Через 10 минут всем явиться к Боссу, то есть ко мне!"
    w5 "Да, мэм, конечно, мэм."

    # Заходит в кабинет
    music stop
    img black_screen
    with diss
    pause 2.0
    sound highheels_short_walk
    music Groove2_85
    img 20229
    with fadelong
    mt "Значит вот мое рабочее место."
    mt "Безвкусица, фи!"
    mt "Но вполне подойдет на первое время..."
    return

label ep26_dialogues6_office2_1a:
    m "ЧТО?! Юлия?!"
    return False
label ep26_dialogues6_office2_2:

# ЧТО?! Юлия?!
# julia "Миссис Бакфетт?"
# m "Что ты делаешь здесь?"
# julia "Я... Я здесь работаю, Миссис Бакфетт..."
    # в движке

    music Groove2_85
    img 20231
    with fadelong
    julia "Миссис Бакфетт?" # ошарашена
    img 20230
    m "Что ты делаешь здесь?"
    img 20232
    with diss
    julia "Я... Я здесь работаю, Миссис Бакфетт..."

    if juliaFirePlanned == True and juliaFireCancelled == False: # Моника уволила Юлию
# Если Моника уволила Юлию
        $ notif(t_("Моника уволила Юлию."))
        music Pyro_Flow
        img 20233
        with fade
        m "Я уже уволила тебя, нерадивая гувернантка!"
        m "Значит тебя в дверь, а ты в окно?!"
        img 20234
        with diss
        w
        sound highheels_short_walk
        img 20235
        with diss
        w
        music stop
        img black_screen
        with diss
        pause 1.0
        music Pyro_Flow
        # Моника садится
        img 20236
        with fadelong
        m "Встать сюда!"
        sound highheels_short_walk
        img 20237
        with diss
        w
        img 20238
        with fade
        m "После увольнения из моего дома, ты решила устроиться ко мне в офис?!"
        img 20239
        with diss
        m "Ты за кого меня принимаешь, Юлия?"
        img 20240
        with fade
        julia "Миссис Бакфетт... Я... Я не знала что это Ваш офис..."
        julia "Меня сюда устроил Мистер Фред..."
        img 20241
        with diss
        m "Фред? Этот мерзавец! Он все-время ведет игру за моей спиной!"
        m "Сначала он подсунул нерадивую гувернантку ко мне в дом!"
        m "А теперь привел ее в мой офис!"
        img 20242
        with diss
        m "С какой стати он делает тебе такие одолжения, Юлия?!"
        m "Ты что, спишь с ним?!"
        # если Юлия имела секс
        if juliaHasSexInPool == True:
            $ notif(t_("Юлии пришлось переспать с Фредом."))
            music Hidden_Agenda
            img 20243
            with fadelong
            julia "..." # (напряженно смотрит)
        else:
            # если не имела секс
            $ notif(t_("Юлия отказалась от секса с Фредом, ни смотря ни на что."))
            music Power_Bots_Loop
            img 20244
            with fadelong
            julia "Я не сплю с ним, Миссис Бакфетт!"

    else:
        # Если Моника не увольняла Юлию
        if juliaFireCancelled == True:
            $ notif(t_("Моника решила уволить Юлию, но затем пожалела ее."))
        else:
            $ notif(t_("Моника не выгоняла Юлию с работы."))
        music stop
        img black_screen
        with diss
        sound highheels_short_walk
        pause 1.0
        music Groove2_85
        img 20245
        with fadelong
        m "Как ты здесь оказалась?"
        img 20246
        with fade
        julia "Миссис Бакфетт, Мистер Фред сказал мне что Вы надолго уехали и у меня теперь нет работы в доме."
        julia "Мне было долго не найти другую работу, но, в конце концов, Мистер Фред помог мне устроиться сюда."

    # продолжение после разветвления
    music Groove2_85
    img 20247
    with fade
    m "Ладно, опустим детали."
    m "Итак, ты теперь работаешь здесь и снова подчиняешься мне."
    m "Я буду работать в этом же кабинете."
    img 20248
    with diss
    julia "Миссис Бакфетт, я думала что у меня самая низкая должность здесь."
    julia "Для меня удивительно что я буду работать рядом с Вами..."
    img 20249
    with fade
    m "В моей компании не бывает незначительно работы, Юлия."
    m "Обработка этих отчетов очень важна для нас."
    m "Я буду присутствовать здесь, чтобы проследить тщательность, с которой ты будешь выполнять эту ответственную работу."
    img 20252
    with fade
    julia "Да, Миссис Бакфетт. Как скажете..." #(боится)
    img 20250
    with diss
    mt "Эти никчемные отчеты никому не нужны!"
    mt "Биф просто решил почесать свое эго, проявив власть надо мной."
    mt "Что-ж, мне стоит подыграть ему."
    img 20251
    with diss
    mt "Он даже не догадывается, что рядом с ним настоящая Моника Бакфетт!"
    mt "Умная, расчетливая и хладнокровная!"
    mt "И я верну назад мою компанию и все остальное!"
    img 20253
    with diss
    mt "Даже если мне придется переступить через себя и рыться в этом бумажном хламе..."
    mt "Временно..."

    return

label ep26_dialogues6_office2_2a:
    m "Юлия, где там эти растяпы?"
    julia "Миссис Бакфетт, кого Вы имеете ввиду?"
    m "Этих никчемных работников, когда они уже придут?"
    julia "Я слышу шаги, Миссис Бакфетт. Кажется, они идут."
    return
label ep26_dialogues6_office2_3:
    # Заходят подчиненные
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 0.5
    sound highheels_run2
    pause 0.5
    sound highheels_short_walk
    pause 0.5
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 20254
    with fadelong
    w
    img 20255
    with diss
    m "Все в сборе?"
    img 20256
    with fade
    w5 "Да, Миссис Бакфетт, здесь весь отдел."
    img 20257
    with diss
    m "Хорошо. Если кто-то отсутствует здесь, то передайте что он уволен."
    music stop
    sound plastinka2
    img 20258
    with hpunch
    w5 "!!!"
    img 20259
    with fade
    w
    music Groove2_85
    w5 "Мэм... Все здесь."
    img 20260
    with diss
    w
    img 20261
    with fade
    m "Итак, сразу скажу что управлять Вами - не мой уровень."
    img 20262
    m "Я нахожусь здесь для того, чтобы своими глазами убедиться в эффективности организации работы компании."
    img 20263
    with diss
    m "Эффективность должна быть везде, даже в таком никчемном отделе, как этот."
    img 20264
    with fade
    m "Потому я требую строгого подчинения."
    m "Нарушение моих распоряжений наказывается немедленным увольнением."
    m "Вам ясно?"
    img 20265
    with fade
    w5 "Да, Мэм..."
    w6 "Да, Мэм..."
    img 20266
    with diss
    w1 "Мэм, можно задать вопрос?"
    music Pyro_Flow
    img 20267
    with diss
    m "Нельзя!"
    m "Зайдешь ко мне отдельно и задашь свой вопрос."
    img 20268
    with fade
    m "А сейчас все вон отсюда!"
    m "Приступайте к работе!"
    music stop
    img black_screen
    with diss
    pause 2.0
    music I_Feel_You
    pause 1.0
    img 20269
    with fadelong
    mt "Итак..."
    mt "Я - снова Босс!"
    img 20270
    with diss
    mt "Моника, мне не верится в то, что это происходит наяву."
    mt "После всего того что было..."
    img 20271
    with diss
    mt "Хоть это и далеко до того положения, к которому я привыкла..."
    mt "Но я даже немного счастлива сейчас..."
    img 20272
    with diss
    mt "Я верну все назад, клянусь!"
    mt "Я самая умная и самая красивая!"
    img 20274
    with diss
    mt "Эти неудачники даже не сравнятся со мной!"
    mt "Я справлюсь со всеми неприятностями и снова буду владеть этой компанией!"
    img 20273
    with diss
    mt "Скоро, Моника!"
    mt "Уже скоро!"
    return

#mt "Итак, мне надо пройти дальше и сесть за тот стол."
#mt "Мне надо отвлечь Юлию. Не хватало чтобы она увидела меня сзади..."

#m "Юлия, что там за бумаги?"
#julia "Где, Миссис Бакфетт?"
#m "Вон там, сзади тебя!"
#julia "Где?"

# Моника быстро проходит и садится
#julia "Миссис Бакфетт, там такие же отчеты как и везде..."
#m "Я уже вижу, Юлия."

#выбор Моники
# Начать работать, либо Заставить все делать Юлию

# Если начать работать
#m "Юлия, принеси мне набор документов, запланированных на обработку сегодня."
#julia "Да, Миссис Бакфетт, вот, пожалуйста."

label ep26_dialogues6_office2_4:
    # Проходит время
    music Stealth_Groover
    $ imagesList = random.sample(set([20275,20276,20277]), 1)
    img imagesList[0]
    with fade
    mt "Все, мне надоело возиться с этой кучкой неудачников."
    mt "Мой рабочий день закончен!"
    return

label ep26_dialogues6_office2_4a:
    mt "Мой рабочий день закончен!"
    return

label ep26_dialogues6_office2_5:
    # Разговор я Юлией вечером
    sound highheels_short_walk
    music Groove2_85
    img 20294
    with fadelong
    m "Юлия, ты еще не закончила?"
    img 20295
    julia "Нет, Миссис Бакфетт. Я буду работать допоздна."
    #julia "Я на новом месте и хочу проявить себя."
    #m "Это похвально, Юлия."
    img 20296
    with diss
    m "Ты не покинешь рабочего места, пока не закончишь с работой, Юлия."
    img 20297
    with diss
    julia "Да, Миссис Бакфетт..."
    julia "Я сделаю всю работу сегодня..."
    return
#m "Юлия, что там за бумаги?"
#julia "Где, Миссис Бакфетт?"
#m "Вон там, сзади тебя!"
#julia "Где?"
# Моника выбегает

label ep26_dialogues6_office2_6:
    # Нажатие на стол, либо на стул
    menu:
        "Работать до вечера.":
            pass
        "Завершить другие дела.":
            return False
    return True

label ep26_dialogues6_office2_7:
    # Если обратиться к Юлии
    music Groove2_85
    img 20278
    with fadelong
    m "Юлия, подойди ко мне!"
    sound highheels_run2
    img 20279
    with fade
    julia "Да, Миссис Бакфетт?"
    img 20280
    with diss
    m "Юлия, что там с отчетами, которые надо обработать сегодня?"
    img 20281
    julia "Их очень много, Миссис Бакфетт."
    julia "У меня впечатление, что это объем для обработки двумя сотрудниками."
    img 20282
    with diss
    julia "Я не представляю как справлюсь с этим!"
    julia "Мне придется работать с этим до ночи!"
    menu:
        "Заставить Юлию работать допоздна.":
            pass
        "Пожалеть Юлию.":
            music Stealth_Groover
            img 20287
            with fade
            m "Юлия, да, отчетов дейтвительно много."
            m "Однако, это не повод задерживаться допоздна."
            m "Сделай сколько успеешь до конца рабочего дня и можешь быть свободна."
            call bitch(-20, "ep26_dialogues6_office2_7") from _call_bitch_193
            img 20288
            with diss
            julia "Миссис Бакфетт, большое спасибо Вам!"
            $ monicaOfficeWorkKindCount1 += 1
            return False
    img 20284
    with fade
    m "Юлия, ты здесь новый сотрудник."
    m "И ты должна проявить себя."
    m "Я здесь для того, чтобы приглядывать за тобой."
    img 20285
    with diss
    m "Ты ведь не намекаешь на то, что я должна помогать тебе в этой работе?"
    if juliaOfficeOffended1 == False:
        $ juliaOfficeOffended1 = True
        $ juliaOfficeOffendedDay = day
    call bitch(20, "ep26_dialogues6_office2_7") from _call_bitch_194
    img 20286
    julia "Нет, Миссис Бакфетт. Что Вы?"
    img 20283
    with diss
    julia "Я сделаю все сама."
    julia "Пожалуйста. Извините меня!"

    $ monicaOfficeWorkOffendedCount1 += 1
    # скип до вечера с событиями
    return True

label ep26_dialogues6_office2_8:
    music Stealth_Groover
    img 20291
    with fadelong
    mt "Все, я свободна на сегодня!"
    img 20292
    with diss
    mt "Пусть Юлия делает всю работу."
    mt "Работать от зари до зари - это ее предназначение, таких как она."
    img 20293
    with diss
    mt "Я - это совершенно другое!"
    return

#    # компьютер
#    img 20289 # день
#    img 20290 # вечер
#    mt "Компьютер не работает."
#    mt "Я не удивлена."
#    mt "Биф не хочет, чтобы я имела доступ хоть к чему-то ценному..."
#    if monicaBitch == True:
#        mt "Сволочь!"
# Регулярные разговоры с Юлией


label ep26_dialogues6_office2_9:
    # Выходной
    mt "Эти бездельники не пришли на работу. Видите-ли сегодня выходной."
    mt "Когда я верну себе компанию, я отменю выходные..."
    mt "Нечего бездельничать!"
    return

label ep26_dialogues6_office2_10:
    mt "Сегодня выходной."
    mt "Из-за того что эти бездельники не работают по выходным, мне нечего здесь делать сейчас."
    mt "Отвратительно!"
    return


label ep26_dialogues6_office2_monica_julia:
    # Смотрит на Юлию
    mt "Это Юлия."
    mt "Моя бывшая гувернантка."
    if monicaBitch == True:
        mt "Бесполезное создание."
        mt "Не верю что мне снова приходится возиться с ней."
    else:
        mt "Странное совпадение что она снова рядом."
    return



label ep26_dialogues6_office2_monica_sofa:
    mt "Мммм..."
    mt "Как приятно понежиться на таком мягком диванчике..."
    return

label ep26_dialogues6_office2_minimap_active:
    help "Активировано меню быстрого перемещения по офису."
    return

label ep26_dialogues6_office2_monica_visit1:
    # Моника приходит первый раз вечером, когда никого нет
    mt "Дьявол! Уже вечер!"
    mt "Никого из этих никчемных подчиненных нет на месте!"
    mt "И я не знаю куда здесь идти."
    mt "Придется придти завтра..."
    return

label ep26_dialogues6_office2_monica_visit1a:
    mt "Ага, вот вы где!"
    mt "Сейчас вы познакомитесь с новым Боссом!"
    return

label ep26_dialogues6_office2_monica_visit1b:
    m "Где там эти растяпы?"
    return False
























#
