default monicaBettyNeighbor1 = False # клик на соседа, квест с Бетти активирован
default monicaBettyNeighbor2 = False # Бетти решила отнести утюг соседу
default monicaBettyNeighbor3 = False # Бетти решила помочь Лиаму и показать, как пользоваться утюгом
default monicaBettyNeighbor4 = False # Бетти согласилась потрогать член Лиама
default monicaBettyNeighbor5 = False # у Бетти с соседом был секс

default ep215_betty_visit2_cumzone = 0
default ep215_betty_after_visit2_kisszone = 0

#call ep215_dialogues2_betty_1() # Моника видит, что во дворе дома Фред разговаривает с соседом
#call ep215_dialogues2_betty_2() # сосед пришел к Бетти за утюгом
#call ep215_dialogues2_betty_3() # Бетти дома, думает, идти ли к соседу
#call ep215_dialogues2_betty_4() # Бетти с утюгом спрашивает у Фреда, где живет сосед
#call ep215_dialogues2_betty_5() # Бетти впервые пришла к соседу
#call ep215_dialogues2_betty_6() # Бетти второй пришла к соседу, h-сцена
#call ep215_dialogues2_betty_7() # после секса с соседом, разговор с Ральфом в гостиной




# при условии, что Моника уже спит с Ральфом
# в один из дней, когда Моника возвращается домой вечером
label ep215_dialogues2_betty_1:
    # во дворе дома Фред стоит возле машины рядом с ним стоит негр-сосед
    # они разговаривают о чем-то, смеются (вид со стороны)
    # Монику не показываем (вид из ее глаз)
    # Моника подозрительно
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 19226
    mt "А этот неудачник что тут делает?!"
    mt "Я думала, что он уже не живет здесь!"
    mt "!!!"
    mt "Зачем он пришел?!"
    mt "Какие у него могут быть общие темы для разговора с Фредом?!"
    mt "..."
    if neighborOffendedSue == True or neighborOffendedSueBig == True:
        mt "Я тогда хотела обратиться к своему адвокату (чертов Дик!!) и закатить ему иск..."
    #
    if neighborOffendedSueBig == True:
        $ notif(_("Моника хотела закатить соседу иск на $ 100 000."))
    #
    imgf 19227
    mt "Вот черт!"
    mt "Что если он сейчас увидит меня! В такой одежде!"
    mt "Что он подумает обо мне?!"
    mt "?!?!?!"
    mt "Мне нужно незаметно пробежать мимо..."
    mt "Но если я узнаю, что мерзавец Фред что-нибудь рассказал этому никчемному соседу обо мне!"
    mt "Я ему оторву его корнишончик! Клянусь!"
    mt "!!!"
    # Моника быстро проходит в дом, отвернув лицо от Фреда с соседом
    # сосед стоит спиной к ней и не смотрит на нее
    # а Фред видит, как Моника пытается быть незаметной, и мерзко улыбается
    # Моника заходит дом
    fadeblack
    sound highheels_run2
    pause 2.0
    music Groove2_85
    imgfl 19234
    w
    # а Фред тем временем прощается с соседом
    imgf 19228
    liam "Эй, Фред, мне пора по делам!"
    liam "Загляну еще к тебе поболтать."
    imgd 19229
    fred "До встречи, Лиам."
    fadeblack 2.0
    # сосед Лиам уходит
    # Фред смотрит на крыльцо, куда забежала Моника и мерзко улыбается
    $ monicaBettyNeighbor1 = True # клик на соседа, квест с Бетти активирован
    return



# после этого (на след. день-?) Моника заходит в любую локацию
# возникает надпись "Тем временем"
label ep215_dialogues2_betty_2:
    # показываем двор дома, сосед отходит от Фреда и идет к крыльцу
    # затемнение, звонок в дверь, звук шагов и звук открываемой двери
    # на крыльце стоит Бетти
    # сосед неуверенно
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Утро...")) from _rcall_textonblack_60
#    call textonblack(t_("Тем временем..."))
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 19230
    sound snd_door_bell1
    w
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.0
    music Groove2_85
    imgf 19231
    liam "Мэм... Добрый день!"
    # Бетти держится с ним высокомерно, как и полагается хозяйке богатого дома и порядочной жене
    imgd 19232
    betty "Вы кто?"
    liam "Я Лиам, живу в доме по-соседству..."
    betty "Здравствуйте, Лиам... Вы что-то хотели?"
    # Лиам чешет затылок и осматривает Бетти с головы до ног
    imgf 19233
    liam "Да, Мэм... Дело в том, что..."
    # Бетти вопросительно на него смотрит
    imgd 19235
    betty "Что?"
    imgf 19236
    liam "Понимаете, Мэм, у меня сгорел утюг..."
    liam "А мне надо ехать в банк... По поводу рассрочки по кредиту за мой дом..."
    liam "Мне надо произвести на менеджера должное впечатление..."
    imgd 19237
    liam "И я не могу поехать на встречу в мятых брюках..."
    liam "А у меня совсем не осталось времени на то, чтобы покупать другой утюг."
    imgf 19238
    betty "Вы хотите взять мой утюг?"
    imgd 19239
    liam "Да, Мэм... Всего на несколько минут..."
    betty "Лиам, я хозяйка богатого дома и такими вопросами занимается моя гувернантка."
    if monicaRestHouse == False:
        betty "Я помогла бы вам, но моей гувернантки сейчас нет дома."
    betty "Сожалею, но ничем не могу вам сейчас помочь."
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.0
    # затемнение, звук закрываемой двери
    # сосед стоит на крыльце один, расстроенно смотрит и уходит
    return

# показываем Бетти в доме
label ep215_dialogues2_betty_3:
    # Бетти стоит, как всегда, у зеркала и смотрит на себя
    fadeblack 1.5
    music Groove2_85
    imgfl 14655
    betty_t "Этот Лиам думает, что всю работу по дому делаю я сама?"
    betty_t "У хозяйки такого роскошного дома всегда есть гувернантка!"
    betty_t "И ему совсем не обязательно знать, что Я все делаю по дому, а не эта нерадивая гувернантка!"
    betty_t "Все потому, что я порядочная жена и хорошая хозяйка!"
    menu:
        "Помочь соседу.":
            music Hidden_Agenda
            imgf 19246
            betty_t "Хммм..."
            betty_t "Теперь сосед будет думать, что я плохая хозяйка..."
            betty_t "Раз я не знаю, где в моем собственном доме находится утюг."
            betty_t "А это не так! Я хорошая хозяйка!"
            imgd 14656
            betty_t "Черт! Мне надо найти утюг и отнести ему!"
            betty_t "Там где я выросла, соседи приыкли поддерживать хорошие отношения и помогать друг другу."
            $ monicaBettyNeighbor2 = True # Бетти решила отнести утюг соседу
            pass
        "Это не мои проблемы! (прерывание квеста)":
            imgf 19246
            betty_t "И вообще, у меня есть другие важные дела!"
            betty_t "Почему я должна тратить свое время на него?!"
            fadeblack 1.5
            return False
    # Бетти выходит из комнаты
    # затемнение
    return True

# Бетти с утюгом выходит во двор дома
label ep215_dialogues2_betty_4:
    # Фред стоит возле машины, Бетти подходит к нему
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19240
    betty "Фред, ты не знаешь, в каком доме живет наш сосед?"
    imgf 19241
    fred "Какой сосед, Миссис Робертс?"
    imgd 19242
    betty "Который сейчас приходил. По-моему, его зовут Лиам..."
    imgf 19243
    fred "Его дом сразу за забором, слева."
    imgd 19244
    sound highheels_short_walk
    betty "Спасибо, Фред."
    imgf 19245
    w
    # она отходит от него и он, мерзко улыбаясь, смотрит ей вслед
    return

# надпись Несколько минут спустя...
# Бетти идет по двору дома соседа к крыльцу
# он стоит на крыльце, расстроенный, в трусах
label ep215_dialogues2_betty_5:
    # Бетти подходит к нему, в руках утюг
    # сосед удивленно
#    scene black_screen
#    with Dissolve(1)
#    stop music fadeout 1.0
#    call textonblack(t_("Несколько минут спустя..."))
#    scene black_screen
#    with Dissolve(1)
#    pause 1.0
    music Groove2_85
    imgfl 19326
    liam "Мэм?!"
    betty "Лиам... Я все-таки решила помочь вам и нашла утюг. Берите."
    # он обрадованно
    liam "О, спасибо! Мэм, вы так выручили меня!"
    # а сам смотрит на утюг и хмурится
    imgf 19327
    betty "Что-то не так?"
    music Hidden_Agenda
    imgd 19328
    liam "Эээ..."
    liam "Здесь так много кнопок..."
    liam "Мэм, сможете показать мне, как его включить?"
    liam "Пожалуйста..."
    menu:
        "Помочь Лиаму.":
            $ monicaBettyNeighbor3 = True # Бетти решила помочь Лиаму и показать, как пользоваться утюгом
            pass
        "Сам разберется! (прерывание квеста)":
            music Groove2_85
            imgf 19329
            betty "Там нет ничего сложного, поэтому вы сами сможете разобраться!"
            sound highheels_short_walk
            imgd 19332
            liam "Спасибо, Мэм..."
            # Бетти разворачивается и уходит, а он смотрит ей вслед
            return False
    # Бетти задумчиво
    music Groove2_85
    imgf 19330
    betty_t "Если я сейчас откажу ему, он подумает, что я сама не знаю, как пользоваться утюгом..."
    betty_t "А это не так! Я же хорошая хозяйка..."
    imgd 19331
    betty "Да, Лиам, я помогу вам."
    liam "Тогда проходите в дом, Мэм. Мы сразу включим утюг."
    # затемнение, звук двери, шаги
    # Бетти и Лиам стоят в его гостиной
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.0
    music Groove2_85
    imgfl 19247
    betty "Куда я могу включить утюг?"
    # Лиам рукой указывает в сторону
    # сам смотрит не на утюг, а на грудь Бетти
    imgf 19248
    liam "Вон там есть розетка, Мэм."
    imgd 19249
    w
    # Бетти идет в сторону стены с розеткой, наклоняется, чтобы включить утюг (провода и включение не показываем)
    # сосед подходит к ней
    # Бетти стоит спиной к нему и объясняет как пользоваться утюгом
    # сосед стоит сразу сзади нее, прижимаясь
    sound highheels_short_walk
    imgf 19250
    w
    sound switch_steve
    imgd 19251
    w
    imgf 19252
    betty "Смотрите, достаточно включить утюг..."
    betty "Потом эту кнопку повернуть сюда..."
    betty "А потом нажать вот сюда и гладить."
    music Hidden_Agenda
    imgd 19253
    liam "Это так сложно, Мэм..."
    liam "Я привык к старым железным утюгам, где была одна кнопка... Большая."
    # Бетти продолжает держаться с ним немного высокомерно, общается, как бы делая ему одолжение
    music Groove2_85
    imgf 19254
    betty "Это современная тонкая техника."
    betty "В моих умелых руках она работает безотказно."
    # сосед смотрит на нее уже похотливо
    music Hidden_Agenda
    imgd 19255
    liam "Мэм, а я предпочитаю одну кнопку, зато большую."
    # сосед прижимается к ней сзади и она чувствует его стояк
    # на лице Бетти удивлениеи растерянность
    sound Jump1
    imgd 19256
    liam "Уверен, она тоже сработала бы безотказно и выполнила бы все нужные функции..."
    liam "Особенно, в таких умелых руках, как ваши, Мэм..."
    # Бетти поворачивается к нему, опускает взгляд и видит, что у него встал
#    music Groove2_85
    imgf 19257
    betty "..."
    menu:
        "Отказать ему!":
            pass
    # Бетти возмущена
    music Pyro_Flow
    imgd 19258
    betty_t "Он что, пристает ко мне?!"
    betty_t "Да как он смеет?!"
    betty_t "Я порядочная женщина и верная жена!!!"
    # Бетти поспешно ставит утюг и идет к двери
    sound highheels_short_walk
    imgf 19259
    betty "Мне срочно нужно идти!"
    music Groove2_85
    liam "Мэээм! Я принесу вам утюг завтра!"
    liam "Спасибо, Мэм!"
    # Бетти с возмущенным видом уходит
    return True

# после этого игра переключается на события с Моникой

# на след. день, когда Моника кликает на любую локацию и хочет выйти из дома
# возникает надпись "Тем временем"
# Бетти стучится в дверь соседского дома
label ep215_dialogues2_betty_6:
    # затемнение, звук двери, шаги
    # Бетти и Лиам стоят в гостиной его дома
    # Лиам удивлен ее визиту
#    scene black_screen
#    with Dissolve(1)
#    stop music fadeout 1.0
#    call textonblack(t_("Тем временем..."))
#    scene black_screen
#    with Dissolve(1)
    fadeblack 1.5
    sound snd_door_knock
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.0
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19260
    liam "Мэм? Рад вас видеть."
    # Бетти общается высокомерно
    betty "Добрый день."
    betty "Я... Я пришла за утюгом..."
    imgf 19261
    liam "Не стоило утруждаться, Мэм."
    liam "Я сам собирался принести вам утюг."
    # Бетти мнется
    music Hidden_Agenda
    imgd 19262
    betty "Я сделала это, потому что у меня..."
    betty "У меня сегодня запланировано много дел..."
    betty "Мне нужно успеть много чего перегладить для своего мужа Ральфа."
    betty "Вы принесли бы мне утюг, а я была бы уже не успела этого сделать..."
    # сосед улыбается
    music Groove2_85
    imgf 19263
    liam "Мэм очень милая и заботливая!"
    liam "Я завидую вашему мужу, Мэм."
    liam "У него такая красивая и такая порядочная жена!"
    liam "К тому же еще и хорошая хозяйка!"
    # Бетти нравятся его комплименты, она горделиво улыбается
    music Hidden_Agenda
    imgd 19264
    betty "Да, я очень порядочная женщина и хорошая хозяйка!"
    betty "А вы смогли разобраться с кнопками, Лиам?"
    imgf 19265
    liam "Да, Мэм... Как вы и говорили, ничего сложного."
    liam "Я нажал на все кнопки и утюг стал нагреваться."
    liam "Так что принцип действия такой же, как и с одной большой кнопкой, Мэм..."
    # он кладет руку себе на пояс, а Бетти смотрит ему в область паха, потом снова на него
    imgd 19266
    w
    imgd 19267
    betty "..."
    imgf 19268
    liam "Вы вчера так выручили меня, Мэм..."
    liam "Ваши умелые ручки так ловко управляются с кнопочками..."
    liam "Не хотите помочь мне еще с одной проблемой, Мэм? По-соседски?"

    # с этого момента можно начать повторную сцену, если Бетти отказалась сначала
    music Groove2_85
    imgd 19269
    betty "Помочь? С чем помочь, Лиам?"
    betty "У вас какие-то проблемы?"
    # сосед неуверенно
    imgd 19270
    liam "Да, Мэм. У меня имеется одна достаточно большая проблема..."
    liam "Я могу обратиться с этой просьбой только к хорошему человеку..."
    liam "А точнее, к хорошей соседке... Такой как вы, Мэм."
    # Бетти озабоченно
    sound man_steps
    imgf 19271
    betty "Лиам, расскажете мне о своей проблеме?"
    liam "Да, Мэм. Эта проблема меня давно терзает..."
    liam "Мне когда-то давно одна женщина сказала об этом..."
    liam "Я даже ходил к врачам, но они сказали, что не могут мне помочь."
    imgd 19272
    liam "Еще врачи сказали, что для решения этой проблемы надо, чтобы..."
    liam "Чтобы кто-то другой опроверг мнение той женщины."
    liam "По этому поводу у меня сильные душевные расстройства."
    liam "Я даже не сплю по ночам, Мэм..."
    imgf 19273
    betty "Все настолько серьезно?"
    liam "Да, Мэм..."
    betty "А что это за проблема, Лиам?"
    # сосед мнется, потом смущенно говорит
    music Hidden_Agenda
    imgd 19274
    liam "Кхм..."
    liam "Мне так неудобно говорить об этом..."
    liam "Я так переживаю, что вы не сможете опровергнуть слова той женщины..."
    liam "Мне... У меня..."
#    music Groove2_85
    imgd 19275
    betty "Говорите смелее, не переживайте."
    liam "Мне кажется, что он у меня недостаточно твердый..."
    # сосед приспускает штаны и достает свой большой член
    imgf 19276
    w
    sound Jump2
    imgd 19277
    liam "Вот. Посмотрите, Мэм."
    # Бетти удивленно смотрит на его член
    music Groove2_85
    img 19278 vpunch
    betty "И? С какой стати вы думаете, что я могу помочь?"
    liam "Вы же не оставите в беде своего соседа, Мэм..."
    # Бетти не отводит глаз от его члена
    imgd 19279
    betty "Ну..."
    betty "На вид он достаточно упругий."
    # Лиам расстроенно
    music Hidden_Agenda
    imgf 19280
    liam "Мэм, я вижу, что вы говорите это, чтобы просто меня утешить..."
    liam "На самом деле вы так не считаете, Мэм."
    imgd 19281
    liam "А это значит, что теперь уже две женщины считают, что это так!"
    liam "Теперь я совсем потеряю сон!"
    # Бетти продолжает смотреть на его член
    imgf 19282
    betty "Лиам, я говорю то, что вижу."
    betty "Ваш член выглядит вполне упругим."
    # Лиам все также расстроен
    imgd 19283
    liam "Я уверен, Мэм, вы так не стали бы говорить, если потрогали бы его..."
    music Groove2_85
    img 19284 vpunch
    betty "Я? Что?"
    betty "Потрогать?"
    menu:
        "Я просто потрогаю и все.":
            $ monicaBettyNeighbor4 = True # Бетти согласилась потрогать член Лиам
            pass
        "Нет! Я не буду этого делать! (прерывание квеста)":
            # Бетти встает руки в боки, возмущенно
            music Power_Bots_Loop
            imgd 19285
            betty "Как вы можете мне предлагать подобные вещи?!"
            betty "Я верная жена и порядочная женщина!"
            imgd 19286
            betty "Вы придумали сами себе какую-то нелепую проблему!"
            betty "Вот сами с этим и разбирайтесь!"
            betty "Где мой утюг?!"
            # сосед отходит к столу и возвращается с утюгом
            music Groove2_85
            imgf 19287
            sound man_steps
            w
            imgd 19288
            liam "Вот он, Мэм. Спасибо вам, Мэм..."
            # Бетти разворачивается и уходит возмущенно, а он смотрит ей вслед
            sound highheels_short_walk
            imgf 19289
            w
            fadeblack
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 1.0
            return False
    # Бетти не в силах отвести взгляд от члена соседа, но продолжает ломаться
    music Groove2_85
    imgd 19284
    liam "Да, Мэм. Только потрогать."
    # Бетти возмущается
    imgf 19290
    betty "Я не собираюсь прикасаться к вам ТАМ!"
    betty "Вообще-то, у меня есть муж!"
    music Hidden_Agenda
    imgd 19291
    liam "Мэм, если вы прикоснетесь к нему своими умелыми ручками..."
    liam "И скажете, что он упругий, то я поверю вам, Мэм."
    liam "И тогда, возможно, моя проблема перестанет терзать меня..."
    liam "При всем уважении к вашему мужу, это не касается отношений между людьми."
    liam "Вы сейчас мой врач, а я ваш пациент!"
    # Бетти смотрит на него пристально
    imgd 19292
    betty_t "Я - врач? Никогда не была в такой роли..."
    betty_t "Если я просто к нему прикоснусь, это ведь не измена мужу."
    betty_t "Я ведь порядочная женщина и верная жена!"
    betty_t "Это же не секс, а просто прикосновение... Это не считается..."
    betty_t "Тем более, я помогаю больному человеку! Тем более, соседу!"
    betty_t "Как врач."
    # Бетти неотрывно смотрит на член соседа и тянет руку к его члену
    fadeblack 1.5
    music Loved_Up
    imgf 19293
    betty "Учтите, Лиам! Я его потрогаю, но совсем чуть-чуть!"
    # проводит пальцами по члену
    betty "Не более того!"
    # снова проводит
    imgd 19294
    betty "И я не собираюсь больше ничего с ним делать!"
    # обхватывает его рукой
    imgf 19295
    liam "Конечно, Мэм..."
    liam "Как скажете, Мэм."
    # Бетти проводит рукой по члену вверх-вниз
    music2 drkanje5
    imgd 19296
    w
    imgd 19297
    w
    imgd 19296
    w
    imgd 19297
    w
    imgd 19296
    w
    imgd 19297
    music2 stop
    w
    imgf 19298
    betty "Он у вас очень упругий и вам не о чем переживать, Лиам."
    betty "Я уже достаточно его потрогала!"
    betty "И больше не собираюсь прикасаться к нему!"
    # а сама продолжает водить рукой по нему
    imgd 19299
    liam "Мммэм... Я так рад это слышать от вас..."
    liam "Вы такая замечательная соседка, Мэм..."
    # Бетти продолжает наяривать ему рукой
    imgf 19301
    betty "И помогаю вам только по-соседски!"
    liam "Да, Мэм... Вы такая заботливая!"
    imgd 19300
    betty "Больше подобных просьб я не желаю слышать, Лиам!"
    betty "У меня есть муж! Я ему никогда и ни с кем не изменяла!"
    betty "И не собираюсь этого делать!"
    # продолжает дрочить
    music2 drkanje5
    imgd 19296
    w
    imgd 19297
    w
    imgd 19296
    w
    imgd 19297
    w
    imgd 19296
    w
    imgd 19297
    music2 stop
    w
    imgf 19302
    liam "Даааа... Мээээм..."
    liam "Хотите попробовать, какой он на вкус?"
    menu:
        "Конечно, нет!":
            pass
    # Бетти возмущенно, продолжая работать рукой
    music Groove2_85
    imgd 19303
    betty "Конечно, нет!!!"
    betty "Что за глупости?!"
    # сама наклоняетя к его члену
    sound Jump1
    imgd 19304
    betty "Почему я должна хотеть этого?!"
    # а сама уже облизывает его
    music stop
    pause 0.5
    music2 Loved_Up
    imgf 19305
    betty "Ммммм... Мне совершенно это не интересно!"
    sound lick3
    imgd 19306
    w
    sound lick3
    imgd 19305
    w
    sound lick3
    imgd 19306
    w
    sound lick3
    imgd 19305
    w
    sound lick3
    imgd 19306
    w
    sound chpok6
    imgd 19307
    w
    # Бетти делает несколько движений головой, сосед кайфует

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Betty_Neighbour_Blowjob1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob1_1 = Movie(play="video/v_Betty_Neighbour_Blowjob1_1.mkv", fps=30)
    show videov_Betty_Neighbour_Blowjob1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19308
    liam "Оооо! Мээээм!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Betty_Neighbour_Blowjob1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob1_2 = Movie(play="video/v_Betty_Neighbour_Blowjob1_2.mkv", fps=30)
    show videov_Betty_Neighbour_Blowjob1_2
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
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Betty_Neighbour_Blowjob1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob1_3 = Movie(play="video/v_Betty_Neighbour_Blowjob1_3.mkv", fps=30)
    show videov_Betty_Neighbour_Blowjob1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19309
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Betty_Neighbour_Blowjob1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob1_4 = Movie(play="video/v_Betty_Neighbour_Blowjob1_4.mkv", fps=30)
    show videov_Betty_Neighbour_Blowjob1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19310
    liam "Мэээм, как вы думаете, мой член достаточно твердый..."
    imgd 19311
    liam "Чтобы войти в вас? Ооооо!!!"
    # Бетти отрывается от него
    music2 stop
    sound plastinka1b
    img 19312 hpunch
    betty "Войти в меня?!"
    betty "Это же измена!"
    music Groove2_85
    imgd 19313
    betty "А я верная жена своего мужа!"
    liam "Мэм, я ведь только попробую, войдет или нет."
    liam "И сразу уберу его! Обещаю, Мэм!"
    menu:
        "Я верная жена!":
            $ monicaBettyNeighbor5 = True # у Бетти с соседом был секс
            pass
        "Нет! Я не буду этого делать! (прерывание квеста)":
            # Бетти встает руки в боки, возмущенно
            music Pyro_Flow
            imgf 19285
            betty "Как вы можете мне предлагать подобные вещи?!"
            betty "Я верная жена и порядочная женщина!"
            imgd 19286
            betty "Вы придумали сами себе какую-то нелепую проблему!"
            betty "Вот сами с этим и разбирайтесь!"
            betty "Где мой утюг?!"
            # сосед отходит к столу и возвращается с утюгом
            music Groove2_85
            imgf 19287
            sound man_steps
            w
            imgd 19288
            liam "Вот он, Мэм. Спасибо вам, Мэм..."
            # Бетти разворачивается и уходит возмущенно, а он смотрит ей вслед
            sound highheels_short_walk
            imgf 19289
            w
            fadeblack
            sound snd_door_open1
            pause 1.5
            sound snd_door_locked1
            pause 1.0
            return False
    # Бетти смотрит на его член
    music Hidden_Agenda
    imgf 19314
    betty_t "Я же помогаю человеку, который долгое время терзался своей проблемой."
    betty_t "Он ведь просто попробует и сразу уберет свой член..."
    betty_t "Это же не измена. Это помощь соседу."
    imgd 19315
    betty "Лиам, я верная жена и не собираюсь изменять своему мужу!"
    betty "Так что ты быстро попробуешь и сразу же уберешь его, ясно?"
    imgd 19316
    liam "Я так и сделаю, Мэм!"
    imgf 19317
    betty "Хорошо, но только быстро!"
    betty "Меня ждет мой муж! Я должна приготовить ему обед!"
    imgd 19318
    liam "Конечно, Мэм!"
    liam "Ложитесь на диван, Мэм."
    liam "Так мне будет намного удобнее."
    # Бетти ложится на диван и задирает платье
    # Лиам смотрит на ее голую киску
    sound highheels_short_walk
    imgf 19319
    w
    imgd 19320
    w
    fadeblack
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    imgfl 19333
    w
    if bettyMustNotWearPanties == True:
        # если Барди заставляет ходить без трусиков
        imgf 19335
        liam "Вы не носите трусики, Мэм?"
        betty "Я делаю это для своего мужа! Ему так нравится!"
        #
#        $ notif(_("Бетти не носит трусики по приказу Барди."))
        #
        #
    imgd 19336
    liam "Ваш муж счастливчик, Мэм!"
    liam "Хотел бы я быть на его месте!"
    liam "О такой жене, как вы, можно только мечтать!"
    imgf 19337
    betty "Да, это так!"
    #liam "Раздвиньте ваши ножки пошире, Мэм..."
    # Бетти раздвигает, сама неотрывно смотрит на член соседа
    imgd 19334
    liam "У вас такая киска... Мммм..."
    liam "Так и хочется скорее почувствовать себя внутри ее!"
    # нацеливает член на киску Бетти
    imgf 19338
    betty "Помнишь, что ты только пробуешь?!"
    betty "Один раз!"
    betty "Потом сразу уберешь свой член!"
    betty "Я не собираюсь изменять своему мужу с каким-то соседом!"
    imgd 19339
    liam "Да, конечно помню, Мэм!"
    # вводит головку в киску
    imgf 19366
    w
    sound chpok6
    img 19340 vpunch
    betty "Ооооох..."
    liam "Еще немного, Мэм..."
    liam "Я еще не распробовал..."
    # входит в нее полностью
    imgf 19341
    w

    music stop
    pause 0.5
    music2 Loved_Up2
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Betty_Neighbour_Sex1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Sex1_1 = Movie(play="video/v_Betty_Neighbour_Sex1_1.mkv", fps=30)
    show videov_Betty_Neighbour_Sex1_1
    with fade
    liam "Даааа! О, даааа!"
    liam "Мээээммммм..."
    betty "Оооо!!! Оооодин раз!"
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # он выходит из нее, но не полностью
    # Бетти требовательно
    imgd 19342
    betty "Я сказала только один раз, ты помнишь?!"

#    betty "Еще один раз попробуй, чтобы уж точно удостовериться!"
    imgf 19343
    liam "Да, Мэм!!!"
    liam "Но ведь я не вынул его!"
    liam "Мне надо его хорошенько ввести и подобрать удобное положение."
    liam "После этого я сразу выну его и это будет как раз один раз, который вы мне разрешили, Мэм!"
    imgd 19344
    betty "Давай быстрее подбирай свое удобное положение и вытаскивай его!"
    betty "Я верная жена и не собираюсь изменять своему мужу, я уже говрила тебе!"

    music2 Loved_Up2
    # снова вводит член
    imgd 19345
    betty "Аааааах!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Betty_Neighbour_Sex1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Sex1_2 = Movie(play="video/v_Betty_Neighbour_Sex1_2.mkv", fps=30)
    show videov_Betty_Neighbour_Sex1_2
    with fade
    liam "Дааааа, как же хорошо у вас внутри, Мэм!"
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19346
    betty "Мммммм!!! Даааа..."
    liam "Нет, так тоже неудобно, надо сдвинуть левее..."
    # продолжает жарить
    # Бетти поплыла, секс
    imgd 19347
    betty "Дааа! Еще!!!"
    liam "ООООО!!!"
    imgf 19348
    liam "Вот так удобнее, Мэм!"
    imgd 19349
    betty "Еще-еще!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Betty_Neighbour_Sex1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Sex1_3 = Movie(play="video/v_Betty_Neighbour_Sex1_3.mkv", fps=30)
    show videov_Betty_Neighbour_Sex1_3
    with fade
    betty "Быстрее!!!"
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19350
    liam "Я почти подобрал удобное положение, Мэм!"
    imgd 19351
    betty "Аааааах!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Betty_Neighbour_Sex1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Sex1_4 = Movie(play="video/v_Betty_Neighbour_Sex1_4.mkv", fps=30)
    show videov_Betty_Neighbour_Sex1_4
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
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Betty_Neighbour_Sex1_1.ogg"
    scene black
    image videov_Betty_Neighbour_Sex1_5 = Movie(play="video/v_Betty_Neighbour_Sex1_5.mkv", fps=30)
    show videov_Betty_Neighbour_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19352
    liam "О, Мээээм! Кончайте, Мэм!"
    # Бетти кончает
    img 19353
    sound woman_moan14
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "Ооооох!!!"
    betty "ОООООО!!!"
    menu:
        "Кончить внутрь Бетти.":
            img 19354
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            liam "Я тоже сейчааааас!!!"
            liam "Кончаааааююююю!!!"
            betty "Не вздумай кончать в меня!"
            img 19355
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            liam "ААА!"
            liam "АААААА!!"
            liam "ААААААААА!!!"
            imgf 19356
            betty "Черт! Сказала же, не в меня!!!"
            $ ep215_betty_visit2_cumzone = 1
            pass
        "Кончить на киску Бетти.":
            img 19354
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            liam "Я тоже сейчааааас!!!"
            liam "Кончаааааююююю!!!"
            betty "Не вздумай кончать в меня!"
            img 19355
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            liam "ААА!"
            liam "АААААА!!"
            img 19357
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            liam "ААААААААА!!!"
            imgf 19358
            w
            $ ep215_betty_visit2_cumzone = 2
            #betty "Черт! Сказала же, не в меня!!!"
            pass
    # затемнение
    # Бетти лежит прибалдевшая на диване, сосед стоит рядом
    # стук в дверь, голос из-за двери
    music2 stop
    fadeblack 2.0
    music Loved_Up
    imgfl 19360
    w
    sound snd_door_knock
    imgf 19359
    fred "Миссис Робертс!"
    # Бетти подрывается с дивана
    music stop
    sound plastinka1b
    img 19361 hpunch
    betty "ЧЕРТ!"
    fadeblack
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    imgfl 19362
    fred "Миссис Робертс, вас ищет ваш муж!"
    fred "Вы тут, Миссис Робертс?!"
    imgf 19363
    betty "Мне надо бежать!"
    betty "Чтобы никому ни слова о моей помощи!"
    sound highheels_run2
    imgd 19364
    w
    sound snd_door_locked1
    imgf 19365
    w
    # Бетти убегает, он смотрит ей вслед
    # забытый утюг остается стоять на столе у соседа
    # отдельно показать это
    return

# сразу после секса с соседом
# гостиная дома
label ep215_dialogues2_betty_7:
    # Ральф стоит посреди гостиной
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 19321
    ralph "Бетти, дорогая, ты где была?"
    ralph "Я тебя везде искал."
    music Hidden_Agenda
    betty "Ральф, у меня были дела."
    menu:
        "Поцеловать Ральфа в губы.":
            # Бетти приближает свои губы к губам Ральфа
            # целует его
            imgd 19323
            w
            sound kiss1
            imgd 8617
            w
            $ ep215_betty_after_visit2_kisszone = 1
            pass
        "Не целовать.":
            imgd 19322
            betty "Ты же знаешь, что я занятая женщина, Ральф!"
            betty "Не могу же я весь день сидеть возле тебя!"
            ralph "Да, дорогая, конечно."
            $ ep215_betty_after_visit2_kisszone = 0
            pass
    # кадр на ноги Бетти - по бедру стекает сперма соседа
    if monicaBettyNeighbor5 == True:
        imgf 19324
    betty "Сейчас я приготовлю тебе обед."
    betty "Подожди немного."
    imgd 19325
    ralph "Хорошо, дорогая."
    return

label ep215_dialogues2_betty_8:
    betty_t "Надо поддерживать хорошие отношения с соседями..."
    return

label ep215_dialogues2_betty_9:
    betty_t "Я теперь хозяйка богатого столичного дома и не хочу больше иметь ничего общего с провинциальной жизнью!"
    return False

label ep215_dialogues2_betty_10:
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Утро...")) from _rcall_textonblack_61
#    call textonblack(t_("Тем временем..."))
    scene black_screen
    with Dissolve(1)
    return

label ep215_dialogues2_betty_11:
    betty_t "Сосед так и не вернул утюг. Наверное, он просто забыл про него."
    betty_t "Надо зайти и забрать его."
    betty_t "Заодно поздороваюсь с Лиамом. С соседями надо поддерживать хорошие отношения..."
    return

label ep215_dialogues2_betty_12:
    mt "Ненавижу сучку Бетти!"
    mt "Я верну себе мой дом!"
    return
