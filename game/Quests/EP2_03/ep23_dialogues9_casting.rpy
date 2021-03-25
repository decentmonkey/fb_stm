# Моника на следующий день идет в локацию офиса на карте.
# Мелани доступна только днем

label ep23_dialogue9_1:
    # Сцена, когда Моника уходит домой (локация на карте):
    # office_entrance.
    # Мелани разговаривает с мартышкой
    # Мелани спрашивает у мартышки: Итак, ты согласна?
    # Мартышка: Да, я согласна.
    # Так значит мне надо будет называться Моникой Бакфетт, также как зовут ту сучку?
    # Мелани: Да
    # Мартышка: А это точно будет она передо мной?
    # Мелани: Да, это будет она...
    # Ты помнишь что от тебя требуется?
    # Мартышка: Да, заставить ее раздеться, сесть на пол.
    # И приказать Вам подойти к ней.
    # Мелани: Да, скажешь как на предыдущей фотосессии.
    # Мартышка: И поцеловать Вашу киску.
    # Мелани: Да, без трусиков. Прикажешь мне их снять.
    # Мартышка: Хорошо, а остальное?
    # Мелани: В остальном может приказывать что хочешь.
    # Мартышка: Я точно могу приказывать этой сучке все что захочу???
    # Мелани: Да, но не будь слишком строгой с ней. В конце концов, она должна быть принята.
    # Мартышка: Она будет принята только если выполнит все что я скажу!!!
    # И на мне будет ее одежда! Я хочу примерить шмотки этой сучки на себя!
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_2
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    img 9173
    with fade
    melanie "Итак, ты согласна?"
    img 9174
    model1 "Да, я согласна."
    "Так значит мне надо будет называться Моникой Бакфетт, также как зовут ту сучку?"
    melanie "Да."
    model1 "А это точно будет она передо мной?"
    img 9175
    with fade
    melanie "Да, это будет она..."
    "Ты помнишь что от тебя требуется?"
    model1 "Да, заставить ее раздеться, сесть на пол."
    "И приказать Вам подойти к ней."
    melanie "Да, скажешь сделать как на предыдущей фотосессии."
    music Hidden_Agenda
    img 9176
    with fade
    model1 "И поцеловать Вашу киску."
    melanie "Да, без трусиков. Прикажешь мне их снять."
    model1 "Хорошо, а остальное?"
    melanie "В остальном можешь приказывать что хочешь."
    music Power_Bots_Loop
    img 9177
    with fade
    model1 "Я точно могу приказывать этой сучке все что захочу???"
    melanie "Да, но не будь слишком строгой с ней. В конце концов, она должна быть принята."
    model1 "Она будет принята только если выполнит все что я скажу!!!"
    "И на мне будет ее одежда! Я хочу примерить шмотки этой сучки на себя!"
    # Это мое условие!
    # Мелани: Конечно, конечно... (улыбается)
    # Мартышка: Последний вопрос...
    # Зачем она это сделает?
    # Ведь она чертовски большой Босс!
    # Мне точно за это ничего не будет?
    # Мелани: Не беспокойся, девочка. Сделаешь все как мы договорились и получишь свои $ 100...
    # Мартышка: Хорошо, но не вздумай меня обмануть!
    # Мелани улыбается
    music Groove2_85
    img 9178
    with fade
    model1 "Это мое условие!"
    melanie "Конечно, конечно..."
    model1 "И последний вопрос..."
    "Зачем она это сделает?"
    "Ведь она чертовски большой Босс!"
    "Мне точно за это ничего не будет?"
    img 9179
    melanie "Не беспокойся, девочка. Сделаешь все как мы договорились и получишь свои $ 100..."
    img 9180
    model1 "Хорошо, но не вздумай меня обмануть!"
    img 9179
    with fade
    melanie "..."
    return

label ep23_dialogue9_2:
#    jump scene_test2
    # Моника приходит к Мелани в гримерку.
    # Спрашивает к Мелани, когда она сходит к Маркусу?
    # Мелани говорит что после кастинга.
    # Готова-ли Миссис Бакфетт пройти его?
    # Ответ да или нет
    # Если да, то Мелани говорит что пойдемте в Ваш кабинет. Там Вас уже ждут...
    music Groove2_85
    img 9181
    with fade
    m "Мелани, когда ты пойдешь к Маркусу?"
    img 9182
    melanie "После кастинга, Миссис Бакфетт...."
    "Готовы-ли Вы пройти его?"
    music Power_Bots_Loop
    img 9183
    menu:
        "Да, я готова (черт!)":
            pass
        "Я пока не решилась на это...":
            music Groove2_85
            m "Я пока не решилась на это..."
            return False

    music Groove2_85
    m "Да, я готова..."
    # Моника приходит в кабинет, там сидит мартышка в ее платье.
    # Мелани сидит на краю стола и улыбается

    # Моника: ТЫ?!?!
    # .....
    # ЭТО... МОЕ ПЛАТЬЕ?!?!
    music stop
    img black_screen
    with Dissolve(1.0)
    music RnB3_65
    img 9184
    with fadelong
    mt "Моника, дыши глубже..."
    "Пусть Мелани поиграет в Босса... Ничего страшного..."
    "Зато она поможет мне вернуть мою нормальную жизнь..."
    "Я сделаю все что мне скажут, я готова пойти на это..."
    "Все зашло слишком далеко и я готова на что угодно!"

    img 9185
    with fadelong
    mt "Я дышу глубоко... Я готова..."

    img 9186
    with Dissolve(0.5)
    w
    music stop
    sound plastinka
    img 9187
    with hpunch
    w
    music Power_Bots_Loop
    img 9188
    w
    img 9189
    with fade
    m "ТЫ?!?!"
    if monkeysOffended1 == True:
        m "ГРЕБАНАЯ МАРТЫШКА!"
    m "..."
    img 9190
    with fade
    m "ЭТО... МОЕ ПЛАТЬЕ?!?!"
    img 9189
    m "Оно не сидит на тебе! Оно МОЕ!!!"

    # Мартышка отвечает молчать сучка!
    img 9191
    with fade
    model1 "Молчать, сучка!"
    # Моника ошарашенная смотрит на Мелани.
    img 9192
    with fade
    m "..."
    # Мелани говорит что Вы помните условие...
    img 9193
    with Dissolve(0.5)
    melanie "Вы помните условие..."

    # Выбор
    # Уйти или остаться и выполнять приказы
    img 9192
    with fade
    menu:
        "Остаться и выполнять приказы.":
            pass
        "Уйти.":
            # Я не собираюсь участвовать в этом фарсе!
            img 9194
            m "Я не собираюсь участвовать в этом фарсе!"
            return False

    # остаться
    # Мартышка говорит Монике зачем та пришла.
    # Моника отвечает что пришла пройти кастинг, чтобы устроиться в журнал.
    # Мартышка говорит чтобы та показала на что она способна.
    # Попринимала разные позы, привлекла внимание.
    music Groove2_85
    img 9195
    with fade
    model1 "Итак, сучка..."
    "Зачем ты пришла сюда?"
    img 9196
    m "Я..."
    "Я пришла пройти кастинг, чтобы устроиться работать в журнал."
    img 9197
    model1 "Хорошо, сними эту куртку"
    "Попринимай разные позы."
    "Привлеки внимание."

    # Моника начинает принимать позы (смущенно)
    # Мелани смотрит
    img 9198
    with fade
    w
    img 9193
    with fade
    w
    sound snd_fabric1
    img 9199
    with fade
    w
    music Loved_Up
    img 9200
    with Dissolve(0.3)
    w
    img 9201
    with Dissolve(0.3)
    w
    img 9202
    with Dissolve(0.3)
    w
    img 9203
    with Dissolve(0.3)
    w
    img 9204
    with Dissolve(0.3)
    w
    img 9205
    with Dissolve(0.3)
    w
    img 9206
    with Dissolve(0.3)
    w
    img 9207
    with Dissolve(0.3)
    w



    # Мартышка говорит что стоп! Так не годится!
    # Виляй своей задницей посильнее! Не веди себя как жирная муха!
    music Groove2_85
    img 9208
    model1 "Стоп! Так не годится!"
    model1 "Виляй своей задницей посильнее!"
    "Не веди себя как жирная муха!"

    # Моника злится!!!
    # Смотрит на Мелани
    # Мелани улыбается
    music Power_Bots_Loop
    img 9209
    with fade
    m "!!!"
    img 9193
    with fade
    melanie "..."

    music Groove2_85
    img 9210
    with Dissolve(0.5)
    model1 "Иди сюда и покажи свою жирную задницу мне!"
    img 9211
    with fade
    w
    img 9212
    w

    # Мартышка говорит Монике снять верх.
    # Моника стесняется
    # Мартышка кричит чтобы быстрее снимала верх или убиралась отсюда!
    # Моника про себя говорит сучка, ненавижу!
    img 9213
    model1 "Сними свой верх, я хочу разглядеть твои дряхлые сиськи!"
    m "..."
    music Power_Bots_Loop
    img 9214
    with fade
    "!!!"

    img 9215
    model1 "А ну-ка быстро снимай верх!"
    "Или можешь убираться отсюда!!!"
    img 9216
    with fade
    mt "СУЧКА!!!"
    "НЕНАВИЖУ!!!"

    # Мартышка говорит чтобы попозировала так...
    music Groove2_85
    sound snd_fabric1
    img 9217
    with fade
    w
    img 9218
    with fade
    w
    img 9219
    model1 "Что ты так на меня смотришь, сучка?!"
    model1 "Убирай свои руки, я хочу тебя видеть!"

    music Power_Bots_Loop
    img 9220
    with fade
    w
    img 9221
    model1 "Начинай позировать..."
    music Loved_Up
    img 9222
    with fade
    w
    img 9223
    with Dissolve(0.3)
    w
    img 9224
    with Dissolve(0.3)
    w
    img 9225
    with Dissolve(0.3)
    model1 "Руки! Не закрывай руками!"
    "Это кастинг! Ты должна показать все что у тебя есть!"

    img 9226
    with Dissolve(0.3)
    w
    model1 "Нагнись ко мне! Я хочу рассмотреть их поближе!"
    music Groove2_85
    img 9227
    with fade
    w
    img 9228
    with Dissolve(0.3)
    w
    "Вот так, да..."
    img 9229
    mt "Я убью эту сучку..."
    model1 "Подвинься ближе!"
    img 9230
    with fade
    model1 "Я хочу потрогать твою грудь..."
    img 9231
    model1 "Надо-же... Я думала она менее уругая..."
    img 9232
    with fade
    w
    img 9233
    with Dissolve(0.5)
    w
    # Затем говорит что Стоп!
    # Это никуда не годится!
    music RocknRoll_loop
    img 9234
    with fade
    model1 "Стоп!"
    "Это никуда не годится!"

    img 9235
    with fade
    w
    img 9236
    with fade
    w



    # Довольная встает, идет, берет стул и садится как Моника тогда.

    # Говорит Монике встать сюда, указывая пальцем.
    # Моника в бешенстве, но встает.
    # Про себя думает что надо пережить это унижение, потом она сотрет ее в порошок!
    # Мартышка говорит Монике повернуться своей жирной задницей и снять все что осталось!
    # Моника говорит я не буду этого делать!
    # Мартышка говорит что тогда убирайся и не трать мое время!
    # Моника смотрит на Мелани, Мелани улыбается.
    # Моника начинает снимать колготки с шортами.
    # Мартышка улыбается.
    img 9237
    with fade
    model1 "Встань сюда!"
    img 9238
    with Dissolve(0.5)
    mt "!!!"
    img 9239
    with fade
    mt "Мне надо как-то собраться с силами..."
    "И пережить это унижение..."
    "Меня греет то что я сотру в порошок эту тварь..."
    img 9240
    with fade
    model1 "Повернись ко мне своей жирной задницей и сними все что на тебе осталось!"
    music Power_Bots_Loop
    img 9241
    m "Я не буду этого делать!"
    img 9242
    model1 "Тогда убирайся отсюда и не трать мое время!"
    img 9243
    with fade
    m "???"
    img 9244
    melanie "..."
    img 9245
    with fade
    w
    img 9246
    model1 "..."

    img 9247
    w
    music RocknRoll_loop
    sound snd_fabric1
    img 9248
    with fadelong
    w
    img 9249
    with Dissolve(0.5)
    w
    img 9250
    with fade
    model1 "Повернись ко мне задом!"
    img 9251
    with fade
    w
    img 9252
    with Dissolve(0.8)
    w
    img 9253
    model1 "Эй! Убери руки!"
    model1 "Что ты там прячешь?!"
    model1 "Если ты хочешь быть моделью, то у тебя не должно быть секретов!"
    img 9254
    w
    # Мартышка говорит чтобы встала задом и нагнулась!
    # Затем положила руки себе на зад и показала задницу как полагается.
    # Что мартышка хозяйка журнала и должна оценить моделей во всех ракурсах!

    img 9255
    model1 "А теперь нагнись!"
    model1 "Положи руки себе на зад и покажи свою задницу как полагается!"
    img 9256
    with fade
    model1 "Я хозяйка журнала и должна оценить моделей во всех ракурсах!"

    # Выбор положить руки или убежать.
    img 9257
    with fade
    menu:
        "Положить руки на зад.":
            pass
        "Убежать.":
            music Power_Bots_Loop
            img 9258
            with fade
            m "Я не буду этого делать!"

            return False

    # Моника кладет руки.

    # Мартышка говорит: Итак, ты хочешь стать моделью этого журнала?
    img 9259
    with fadelong
    w
    model1 "Нагнись сильнее!"
    model1 "Мне так ничего не видно!"
    model1 "И не убирай руки со своей задницы!"
    img 9260
    with fade
    w
    img 9261
    model1 "Ха-ха! Славная задница!"
    img 9263
    with Dissolve(0.5)
    model1 "Мелани, отвечай!"
    model1 "Тебе нравится этот зад?"
    img 9264
    with fade
    melanie "Да, этот зад мне нравится..."
    melanie "Но все на Ваше усмотрение..."



    img 9265
    with fade
    model1 "Итак, ты хочешь стать моделью этого журнала?"
    music Power_Bots_Loop
    img 9266
    with fade
    menu:
        "Да, хочу.":
            pass
        "Убежать.":
            music Power_Bots_Loop
            img 9258
            with fade
            m "Я больше не могу этого выносить!"
            return False
    mt "Мне надо как-то выдержать это унижение..."
    "Я знаю, Мелани доставляет удовольствие эта сцена..."
    "Но она сейчас мой единственный шанс на свободу..."
    "И мне придется пойти на все, чтобы использовать этот шанс..."
    music RocknRoll_loop
    img 9267
    with fade
    m "Да, хочу."
    # Моника отвечает: да, хочу
    img 9268
    model1 "Очень хочешь???"
    # ОЧень хочешь?
    music Power_Bots_Loop
    img 9269
    with fade
    menu:
        "Очень хочу!":
            pass
        "Убежать.":
            music Power_Bots_Loop
            img 9258
            m "Я больше не могу этого выносить!"
            return False
    # Очень хочу!

    music RocknRoll_loop
    img 9270
    with fade
    m "Очень хочу!"

    img 9271
    with fade
    model1 "Тогда я буду говорить тебе какие позы принимать!"
    model1 "Давай, повеселимся!"
    # Далее идет серия кадров как Моника принимает разные обнаженные позы, а мартышка и Мелани улыбаются.

    img 9272
    with fade
    model1 "Начнем с этой!"
    img 9273
    with fade
    w
    model1 "Хе-хе!"
    model1 "Давай следующую!"
    img 9274
    with fade
    w
    img 9275
    with fade
    w
    model1 "Убери руку!"
    model1 "Не обязательно прикрываться, у тебя нет от нас секретов!"
    img 9276
    with Dissolve(0.3)
    w
    img 9277
    with Dissolve(0.3)
    w
    img 9278
    with fade
    model1 "Давай! Поползай еще!"
    model1 "Тебе это идет!"
    "Ползай, давай!"
    img 9279
    with Dissolve(0.3)
    w
    mt "Я выдержу!"
    mt "Я клянусь! Я выдержу!"

    img 9280
    with Dissolve(0.3)
    model1 "Встань на цыпочки! Покажи свою киску поближе!"

    img 9281
    with Dissolve(0.3)
    w
    model1 "Да, вот так! И не смотри на меня таким взглядом!"
    model1 "Я ведь знаю что тебе это нравится!"
    music Power_Bots_Loop
    img 9282
    m "Мелани!"
    m "Скоро это закончится?!"
    model1 "Молчать! Сучка!"
    model1 "Ты открыла рот! Ты не прошла кастинг!"

    music Groove2_85
    img 9284
    with fade
    m "???"
    img 9283
    with Dissolve(0.5)
    w
    img 9285
    with fade
    melanie "Да, модель себя плохо ведет..."
    melanie "Но я думаю можно дать ей последний шанс..."
    img 9286
    model1 "У тебя последний шанс, сучка!"
    model1 "Еще раз облажаешься и кастинг провален!"
    mt "!!!"
    model1 "А теперь подыми свою киску повыше!"
    model1 "Я хочу рассмотреть ее!"
    music RocknRoll_loop
    img 9287
    with fade
    model1 "Да, вот так!"
    img 9288
    with Dissolve(0.3)
    w
    img 9289
    with Dissolve(0.3)
    w
    img 9290
    with Dissolve(0.3)
    w
    img 9291
    with Dissolve(0.3)
    model1 "(так вот значит как выглядит киска на миллиард долларов...)"
    img 9292
    with fade
    model1 "Мелани, тебе нравится этот вид?"
    model1 "Тебе не кажется он ей очень идет?"

    music Groove2_85
    img 9293
    with fade
    melanie "Да, мне нравится этот вид."
    melanie "Он идет ей..."
    img 9294
    mt "!!!"
    # Мартышка раздвигает ноги и говорит Монике посмотреть что у нее там.
    # Монике отвратительно.
    # Мартышка говорит быстро! И показывает пальцем.
    # Моника садится и смотрит. Там между ног дилдо.
    img 9295
    with fadelong
    model1 "Посмотри-ка что у меня там есть!"
    img 9296
    m "!!!"
    img 9297
    with fade
    model1 "Быстро посмотри туда!"

    # Мартышка спрашивает Что там?
    # Моника отвечает там что-то есть, у Вас между ног...
    img 9298
    with fade
    model1 "Что там?"
    img 9299
    with fade
    m "Там что-то есть, у Вас между ног..."

    # Мартышка говорит чтобы Моника достала это...
    # Моника достает, это дилдо.
    model1 "Достань это!"
    music stop
    img 9300
    with fade
    w
    sound hlup10
    img 9301
    with fade
    m "..."

    # Мартышка говорит Монике встать. Моника встает.
    # Мартышка говорит Монике поднести дилдо ко рту и понюхать.
    # Моника нюхает.
    # Мартышка спрашивает чем пахнет эта вещь?
    # Моника отвечает что она пахнет Вами...
    # Мартышка говорит Монике открыть рот, очень широко.
    # Моника спрашивает зачем?
    # Мартышка ругается: Сучка, быстро открыла рот и хватит тратить мое время!
    # Моника открывает рот.
    music Power_Bots_Loop
    model1 "Теперь встань!"
    img 9302
    with fade
    w
    img 9303
    model1 "Поднеси это к своему рту."
    img 9304
    with fade
    "Теперь нюхай!"
    music stop
    m "!!!"
    sound snd_sniff1
    img 9305
    with Dissolve(0.5)
    w
    music Groove2_85
    model1 "Чем пахнет эта вещь?"
    img 9306
    with fade
    m "Она... Она пахнет Вами..."
    img 9307
    with Dissolve(0.5)
    mt "(меня сейчас стошнит)"
    img 9308
    with fade
    model1 "Теперь открой рот, очень широко!"
    m "Зачем?"
    music Power_Bots_Loop
    img 9309
    model1 "Сучка, быстро открыла рот и хватит тратить мое время!"

    music Groove2_85
    img 9310
    with fade
    w
    img 9311
    with Dissolve(0.5)
    w

    # Мартышка говорит: А теперь, вставь эту штуку себе в рот, максимально глубоко!
    # Мелани удивлена, подняла бровь...
    # Моника посмотрела на Мелани в возмущении.
    # Мелани смотрит на Монику и улыбается...
    # Говорит: Босс приказал...
    img 9312
    with fade
    model1 "А теперь вставь эту штуку себе в рот, максимально глубоко!"
    img 9313
    with Dissolve(0.5)
    melanie "???"
    music Power_Bots_Loop
    img 9314
    with fade
    m "!!!"
    img 9315
    melanie "..."
    img 9314
    m "???"
    music Groove2_85
    img 9316
    with fade
    melanie "Босс приказал..."


    # Моника смотрит на мартышку и думает: Я убью тебя...
    # Затем вставляет дилдо.
    img 9317
    with fade
    mt "Я УБЬЮ ТЕБЯ..."
    img 9318
    with fade
    w
    music stop
    img 9319
    with Dissolve(0.5)
    w
    sound hlup10
    img 9320
    with Dissolve(0.5)
    w
    music Groove2_85

    # Мартышка говорит: А теперь трахай свой рот! Хорошенько трахай!
    img 9321
    model1 "А теперь трахай свой рот!"
    "Хорошенько трахай!"
    $ monicaMelanieCastingLickedDildo = True
    # Моника начинает трахать свой рот.
    # видео
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_1_1 = Movie(play="video/v_Monica_Cabinet_Dildo_1_1.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_1_1
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_1.ogg"
    $ renpy.music.set_volume(0.7)
    scene black
    image videov_Monica_Cabinet_Dildo_1_2 = Movie(play="video/v_Monica_Cabinet_Dildo_1_2.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_1_2
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_1.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Monica_Cabinet_Dildo_1_3 = Movie(play="video/v_Monica_Cabinet_Dildo_1_3.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_1_3
    with fade
    wclean
    music stop
    music Groove2_85
    $ renpy.music.set_volume(1.0)
    img 9322
    with fade
    w

    # Мартышка говорит что ты совершенно не владеет мастерством.
    # Говорит чтобы Моника села на колени. И не высовывала дилдо!!
    # v_Monica_Cabinet_Dildo_1_1 - 1_3
    music Groove2_85
    img 9323
    with fade
    model1 "Ты совершенно не умеешь это делать!"
    "Сядь на колени!"
    "И не высовывай дилдо из своего рта!"
    img 9324
    with fade
    w


    # Мартышка говорит убери руки! Моника убирает.
    # Мартышка наклоняется и начинает рукой трахать Монике рот дилдо.
    img 9325
    with Dissolve(0.5)
    model1 "Теперь убери руки!"
    img 9326
    with fade
    model1 "Я покажу тебе как это надо делать!"
    img 9327
    with Dissolve(0.3)
    model1 "Не двигайся!"
    img 9328
    with fade
    w


    # видео
    # v_Monica_Cabinet_Dildo_2_1 - 2_7
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(0.8)
    scene black
    image videov_Monica_Cabinet_Dildo_2_1 = Movie(play="video/v_Monica_Cabinet_Dildo_2_1.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_1
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_2_2 = Movie(play="video/v_Monica_Cabinet_Dildo_2_2.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_2
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(0.7)
    scene black
    image videov_Monica_Cabinet_Dildo_2_3 = Movie(play="video/v_Monica_Cabinet_Dildo_2_3.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_3
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(0.8)
    scene black
    image videov_Monica_Cabinet_Dildo_2_4 = Movie(play="video/v_Monica_Cabinet_Dildo_2_4.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_4
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_2_5 = Movie(play="video/v_Monica_Cabinet_Dildo_2_5.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_5
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(0.9)
    scene black
    image videov_Monica_Cabinet_Dildo_2_6 = Movie(play="video/v_Monica_Cabinet_Dildo_2_6.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_6
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_2_7 = Movie(play="video/v_Monica_Cabinet_Dildo_2_7.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_2_7
    wclean

    # Мартышка спрашивает: Ты поняла как надо себя трахать?
    # Моника отвечает: "Да, поняла" или послать к черту

    music stop
    music Groove2_85
    $ renpy.music.set_volume(1.0)
    img 9329
    with fade
    model1 "Ты поняла как надо себя трахать?"
    menu:
        "Да, я поняла.":
            pass
        "Послать ее к черту!":
            music Power_Bots_Loop
            img 9330
            with fade
            m "Иди ты к черту, сучка!!!"
            return False

    # Да, я поняла.
    # Мартышка говорит: хорошо, покажи мне!
    # Ляг на спину и раздвинь ноги!
    # Моника с недовольным лицом делает это
    m "Да, я поняла."
    img 9331
    with fade
    model1 "Хорошо, покажи мне!"
    "Ляг на спину и раздвинь ноги!"
    music Power_Bots_Loop
    img 9332
    mt "!!!"
    img 9333
    with Dissolve(0.3)
    w
    music Groove2_85
    img 9334
    with fade
    w

    # Мартышка говорит: А теперь вставь эту штуку в себя!
    # Давай!
    img 9335
    with Dissolve(0.3)
    model1 "А теперь вставь эту штуку в себя!"
    "Давай!"
    music stop
    img 9336
    w
    sound hlup10
    img 9337
    with fade
    w
    music Groove2_85

    # Моника вставляет.
    # Мартышка говорит: А теперь трахай себя, сучка!
    # Трахай себя как следует!
    img 9338
    model1 "Теперь трахай себя, сучка!"
    "Трахай себя как следует!"

    # Выбор трахать себя или послать к черту
    img 9339
    menu:
        "Трахать себя.":
            pass
        "Послать к черту.":
            music Power_Bots_Loop
            img 9330
            m "Иди ты к черту, сучка!!!"
            return False

    # Если трахать:
    # видео Моника трахает себя

#audio_Monica_Cabinet_Dildo_3
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_3_1 = Movie(play="video/v_Monica_Cabinet_Dildo_3_1.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_3_1
    with fade
    wclean

    music stop
    music Loved_Up2
    img 9340
    with Dissolve(0.3)
    w
    # Мартышка спрашивает в это время: Хочешь стать моделью?
    # Моника отвечает ДА или хочу поскорее закончить это
    # v_Monica_Cabinet_Dildo_3_1 - 3_4
    model1 "Хочешь стать моделью?"
    menu:
        "Да!":
            m "Да!"
        "Хочу поскорее закончить это...":
            m "Хочу поскорее закончить это..."


    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_3_2 = Movie(play="video/v_Monica_Cabinet_Dildo_3_2.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_3_2
    with fade
    wclean

    music stop
    music Loved_Up2
    img 9341
    with Dissolve(0.3)
    w
    model1 "Громче! Хочешь стать моделью этого журнала?!"
    # Мартышка говорит громче! Хочешь стать моделью этого журнала?!
    # Громко Да или когда закончится этот кошмар?
    #

    menu:
        "ДА!!!":
            m "ДА!!!"
        "Когда же закончится этот кошмар?!":
            m "Когда же закончится этот кошмар?!"
    # Мартышка спрашивает: Тебе нравится трахать себя?
    # Моника говорит: У меня странное чувство, незнакомое... Меня что-то заполняет...
    # Мартышка спрашивает громко: ТЕБЕ НРАВИТСЯ ТРАХАТЬ СЕБЯ???
    # Моника отвечает выбор: ДА!!!

    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_3_3 = Movie(play="video/v_Monica_Cabinet_Dildo_3_3.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_3_3
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_Dildo_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_Dildo_3_4 = Movie(play="video/v_Monica_Cabinet_Dildo_3_4.mkv", fps=30)
    show videov_Monica_Cabinet_Dildo_3_4
    with fade
    wclean

    music stop
    music Loved_Up2
    img 9342
    with Dissolve(0.3)
    w

    model1 "Тебе нравится трахать себя?"
    m "У меня... У меня странное чувство, незнакомое..."
    "Меня что-то заполняет..."
    model1 "ТЕБЕ НРАВИТСЯ ТРАХАТЬ СЕБЯ???"
    img 9343
    with fade
    menu:
        "ДААА!!!":
            pass

    # После этого Моника кончает: АААаааааа!! Ааааа!!!!
    # Моника лежит раскинув руки
    img 9344
    with Dissolve(0.3)
    sound snd_orgasm1
    m "Аааааааа!! АААААА!!!"
    img 9345
    with Dissolve(0.3)
    sound snd_orgasm2
    w
    img 9346
    with Dissolve(0.3)
    sound snd_orgasm3
    "АААаАААААаа!!!"
    # Следующий кадр, Моника привстает.
    # Что это было? Что со мной случилось??? У меня никогда такого не было...
    sound snd_bodyfall
    img black_screen
    with Dissolve(0.5)
    pause 2.0

    music Loved_Up
    img 9347
    with fadelong
    w
    img 9348
    with fade
    mt "Что это было? Что со мной случилось???"
    "У меня никогда такого не было..."
    $ monicaMelanieCastingCummed = True

    # Мартышка говорит Мелани.
    # Мелани! Подойди к модели сверху и расставь ножки!
    # Пора завершить прошлую фотосессию!
    # Моника недоуменно смотрит на Мелани.
    # Мартышка говорит Мелани, чтобы та сняла трусики
    # Мелани снимает трусики и встает над Моникой
    img 9349
    with fade
    model1 "Мелани! Подойди к модели сверху и расставь ножки!"
    img 9350
    model1 "Пора завершить прошлую фотосессию!"
    # медленные шаги каблуков
    img 9351
    with fade
    w
    img 9352
    m "???"
    img 9353
    with fade
    model1 "Да, и не забудь снять свои трусики!"
    img 9354
    with Dissolve(0.5)
    w
    sound snd_fabric1
    img 9355
    with fade
    w


    # Моника говорит: Мелани, ты что? Что ты собираешь делать?
    # Мелани отвечет: Простите, Мэм. Это приказ Босса. Я здесь ни при чем...
    # Мартышка говорит чтобы Моника дотронулась языком до киски Мелани.
    img 9356
    m "Мелани, ты что?"
    img 9357
    with Dissolve(0.3)
    "Что ты собираешься делать?"
    img 9358
    with fade
    melanie "Вы это имели ввиду?"
    img 9359
    model1 "Да, стой вот так!"

    img 9360
    melanie "Простите, Мэм."
    img 9361
    with fade
    "Это приказ Босса."
    img 9362
    "Я здесь ни при чем..."
    img 9363
    model1 "Дотронься языком до ее киски!"
    img 9364
    with Dissolve(0.5)
    model1 "Давай!"
    img 9365
    with fade
    menu:
        "Мелани, ты сучка! Ты специально затеяла это!":
            pass
        "Мелани, пожалуйста, я не могу сделать это. (хорошие отношения с Мелани)" if melanieOffended2 == False and melanieOffended1 == False:
            # Выбор если Моника была добра к Мелани:
            # Мелани, пожалуйста, я не могу сделать это.
            # Мелани говорит что этого достаточно, чтобы пройти кастинг. Мартышка соглашается.
            music Groove2_85
            img 9366
            with fade
            m "Мелани, пожалуйста, я не могу сделать это."
            img 9367
            with fade
            melanie "Я думаю этого достаточно, чтобы пройти кастинг."
            "Босс, вы так не считаете?"
            model1 "..."
            model1 "Хорошо, пусть будет достаточно!"
            "Ты принята, сучка!"
            return True
        "Мелани, пожалуйста, я не могу сделать это. (плохие отношения с Мелани) (disabled)" if melanieOffended2 != False or melanieOffended1 != False:
            pass

    # Иначе:
    # Моника шепчет: Мелани, ты сучка! Ты специально затеяла это!
    # Мелани отвечает что у Миссис Бакфетт есть приказ Босса.
    # Моника трогает язычком киску Мелани.
    # Мелани балдеет от удовольствия
    $ monicaMelanieCastingLickedPussies = True
    music Power_Bots_Loop
    img 9368
    m "Мелани, ты сучка! Ты специально затеяла это!"
    music Loved_Up
    img 9369
    with fade
    melanie "Миссис Бакфетт, у Вас есть приказ Вашего Босса."

    # sound todo !!!!!!!!!!!!!!!!!
    #лижет
    music audio_Monica_Cabinet_Licking1
    img 9370
    with fade
    w
    img 9371
    with Dissolve(0.3)
    w
    img 9372
    with Dissolve(0.3)
    w
    img 9373
    with Dissolve(0.3)
    w
    img 9374
    with Dissolve(0.3)
    w
    img 9375
    with Dissolve(0.3)
    w
    img 9376
    with Dissolve(0.3)
    w
    img 9377
    with Dissolve(0.3)
    w
    img 9378
    with fade
    w
    # Мартышка говорит: Стоп, стоп!
    # Что это за нежности Вы тут развели?!
    # Где страсть?!
    # Мелани! Что ты стоишь?! Быстро сядь ей на лицо и трахни его своей киской!
    # Мелани недоуменно смотрит на Мартышку.
    # Мартышка говорит: Ты что не поняла, Мелани?! Быстро сядь на эту сучку!
label scene_test2:
    music Power_Bots_Loop
    img 9379
    model1 "Стоп, стоп!"
    "Что это за нежности Вы тут развели?!"
    "Где страсть?!"
    "Мелани! Что ты стоишь?!"
    "Быстро сядь ей на лицо и трахни его своей киской!"
    img 9380
    with fade
    melanie "???"
    img 9381
    model1 "Ты что, не поняла, Мелани?! Быстро сядь на эту сучку!"

    # Мелани продолжает смотреть удивленно на мартышку, затем смотрит вниз.
    # Моника (вид снизу) говорит: Эй, ты что собираешься делать?! Мелани?!...
    # Мелани говорит: Простите, Миссис Бакфетт, это приказ Босса.
    # Садится на Монику и начинает facesitting.
    img 9380
    with Dissolve(0.5)
    melanie "???"
    music Loved_Up
    img 9382
    with Dissolve(0.5)
    melanie "..."
    img 9383
    with fade
    m "Эй, ты что собираешься делать?!"
    "Мелани?!..."
    music stop
    img 9384
    with Dissolve(0.5)
    melanie "Простите, Миссис Бакфетт, это приказ Босса."
    sound hlup21
    img 9385
    with fadelong
    w
    music Loved_Up2
    # v_Monica_Cabinet_FaceSitting_1_1 - 1_4
    img 9386
    with Dissolve(0.3)
    w
    img 9387
    with Dissolve(0.3)
    w
    img 9388
    with Dissolve(0.3)
    w
    stop music
    play music "<from 0.23 loop 0.23>Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
#    play music "Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_1_1 = Movie(play="video/v_Monica_Cabinet_FaceSitting_1_1.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_1_1
    with fade
    wclean
    stop music
    play music "<from 0.23 loop 0.23>Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
#    play music "Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_1_2 = Movie(play="video/v_Monica_Cabinet_FaceSitting_1_2.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_1_2
    with fade
    wclean
    stop music
    play music "<from 0.23 loop 0.23>Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
#    play music "Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_1_3 = Movie(play="video/v_Monica_Cabinet_FaceSitting_1_3.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_1_3
    with fade
    wclean
    stop music
    play music "<from 0.23 loop 0.23>Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
#    play music "Sounds/audio_Monica_Cabinet_FaceSitting_1.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_1_4 = Movie(play="video/v_Monica_Cabinet_FaceSitting_1_4.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_1_4
    with fade
    wclean

    music stop
    music Loved_Up
    img 9389
    with Dissolve(0.3)
    w
    img 9390
    with Dissolve(0.3)
    w
    img 9391
    with Dissolve(0.3)
    w
    # Мартышка смотрит на это и говорит: Вот значит как выглядит pussy на миллиард долларов?
    # Черт, я не могу удержаться... Эта сучка...
    # Да пошло оно все!
    # Мартышка спрыгивает со стула и начинает лизать киску Моники.
    img 9392
    with fade
    model1 "Вот значит как выглядит киска на миллиард долларов?"
    img 9393
    model1 "Черт, я не могу удержаться... Эта сучка..."
    "Она правда красивая..."
    "Да пошло оно все!"

    # Видео threesome (всеобщие охи-вздохи)
    music Loved_Up2
    img 9394
    with fadelong
    w
    img 9395
    with Dissolve(0.3)
    w
    img 9396
    with Dissolve(0.3)
    w
    img 9397
    with Dissolve(0.3)
    w
    img 9398
    with Dissolve(0.3)
    w
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_2_1 = Movie(play="video/v_Monica_Cabinet_FaceSitting_2_1.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_2_1
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_2_2 = Movie(play="video/v_Monica_Cabinet_FaceSitting_2_2.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_2_2
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_2_3 = Movie(play="video/v_Monica_Cabinet_FaceSitting_2_3.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_2_3
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_2.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_2_4 = Movie(play="video/v_Monica_Cabinet_FaceSitting_2_4.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_2_4
    with fade
    wclean
    music stop
    music Loved_Up2
    img 9399
    with Dissolve(0.3)
    w
    img 9400
    with Dissolve(0.3)
    w
    img 9401
    with Dissolve(0.3)
    w
    img 9402
    with Dissolve(0.3)
    w
    img 9403
    with Dissolve(0.3)
    w

    # Мелани кончает.
    # sound todo !!!!!!
    sound snd_melanie_cum
    img 9404
    with fadelong
    melanie "ААААААааааааххххх!!!!"
    sound snd_melanie_cum2
    img 9405
    with Dissolve(0.5)
    melanie "ААААААааааааххххх!!!!"
    # Мелани встает.
    # Мартышка говорит: Мелани, ты все?
    # Теперь моя очередь!
    # И садится на лицо Моники.
    music Loved_Up
    img black_screen
    with Dissolve(1.0)
    img 9406
    with fadelong
    model1 "Мелани, ты все?"
    img 9407
    with Dissolve(0.5)
    "Теперь моя очередь!"

    # Мартышка говорит Мелани:
    # Мелани, ты пока можешь полизать ее киску, а потом мою!
    img 9408
    with Dissolve(0.5)
    model1 "Мелани, ты пока можешь полизать ее киску, а потом мою!"

    # Мелани надменно отвечает: Сегодня это твоя работа, девочка...
    # Мелани уходит
    music Groove2_85
    img 9409
    with fade
    melanie "Сегодня это твоя работа, девочка..."

    sound snd_fabric1
    img 9410
    with fade
    w
    img 9411
    with fade
    w
    music stop
    img 9412
    with Dissolve(0.5)
    w
    # Какое-то время Мартышка трется о лицо Моники.
    sound hlup21
    img 9413
    with fade
    w

    #видео
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_3_1 = Movie(play="video/v_Monica_Cabinet_FaceSitting_3_1.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_3_1
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_3_2 = Movie(play="video/v_Monica_Cabinet_FaceSitting_3_2.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_3_2
    with fade
    wclean
    stop music
    play music "Sounds/audio_Monica_Cabinet_FaceSitting_3.ogg"
    $ renpy.music.set_volume(1.0)
    scene black
    image videov_Monica_Cabinet_FaceSitting_3_3 = Movie(play="video/v_Monica_Cabinet_FaceSitting_3_3.mkv", fps=30)
    show videov_Monica_Cabinet_FaceSitting_3_3
    with fade
    wclean

    music stop
    music Loved_Up2
    img 9414
    with Dissolve(0.3)
    w
    img 9415
    with Dissolve(0.3)
    w
    img 9416
    with Dissolve(0.3)
    w
    img 9417
    with Dissolve(0.3)
    w
    img 9418
    with Dissolve(0.3)
    w
    img 9419
    with Dissolve(0.3)
    w

    #секретарша
    music Groove2_85
    img 9420
    with fade
    secretary "Ой! Кто это???"
    img 9421
    with fade
    melanie "Это новая модель..."
    melanie "Проходит кастинг..."
    img 9422
    with Dissolve(0.5)
    melanie "Хочет сниматься в нашем журнале..."
    music RnB4_100
    img 9423
    with fade
    secretary "(бедная девушка!)"

    img 9424
    with fade
    melanie "Пойдем, не будем их отвлекать от работы!"



    # Мартышка кончает.
    music Loved_Up2
    sound snd_monkey_cum
    img 9425
    with fade
    model1 "ААаааааааххххх!!!"
    # Встает. Говорит Монике чтобы она полизала ей зад!
    img 9426
    with fade
    model1 "А теперь лижи мой зад!"
    img 9428
    w
    # Моника смотрит на зад. Смотрит вокруг.
    img 9427
    mt "!!!"
    img 9429
    with fade
    mt "..."
    # Спрашивает, а где Мелани?
    m "А где Мелани?"


    # Мартышка отвечает: Зачем тебе Мелани, сучка? Здесь есть моя попка! Ее надо лизать!
    # Моника вскакивает и говорит: Ах ты сучка! Я убъю тебя! Ты ответишь за все что здесь было!!!
    # ТВАРЬ!!!
    # Моника напрыгивает на Мартышку.
    # Мартышка испугалась и, улыбаясь, убегает.
    img 9430
    with fade
    model1 "Зачем тебе Мелани, сучка?"
    "Здесь есть моя попка!"
    "Ее надо лизать!"

    music Power_Bots_Loop
    img 9431
    with Dissolve(0.5)
    mt "!!!"
    img 9432
    with fade
    m "Ах ты сучка! Я убъю тебя!"
    "Ты ответишь за все что здесь было!!!"
    "ТВАРЬ!!!"

    # Моника говорит: Мне надо одеться.
    # Одевается. Затем думает.
    # Где там эта Мелани?!?!
    # Пусть только попробует еще что-то захотеть!
    # Я уже достаточно здесь натерпелась!!!
    music Groove2_85
    img 9433
    with fadelong
    mt "Я достану эту тварь, клянусь!"
    "На что я только согласилась?!?!"
    "Меня, фактически, изнасиловала эта мартышка в своем-же собственном кабинете!"
    img 9434
    "А Мелани смотрела на это!"
    "О БОЖЕ!!!"
    img 9435
    with fade
    "Да, ставки очень высоки и мне приходится идти на подобные жертвы..."
    "Но, Моника, не забывай, тебе потом еще здесь жить и работать."
    "Не надо забывать о своей репутации!"
    "..."
    "Но я надеюсь что никто не узнает про то что здесь было."
    "Этой пигалице все-равно никто не поверит."
    "А Мелани... Не в ее интересах распространяться об этом."
    "Учитывая что она принимала участие..."
    "И что такое со мной произошло? Какая-то вспышка..."
    "Черт! Лучше я забуду обо всем этом побыстрее!"
    img 9436
    with fade
    "..."
    "Мне надо одеться."
    "..."
    sound snd_fabric1
    img black_screen
    with fade
    pause 2.0
    img 9437
    with fadelong
    "Где там эта Мелани?!?!"
    "Пусть только попробует еще что-то захотеть!"
    "Я уже достаточно здесь натерпелась!!!"

    return True

label ep23_dialogue9_3:
    # Монике не выйти из офиса, т.к. мне надо увидеть Мелани
    mt "Я никуда не пойду! Мне надо поговорить с Мелани!"
    return False


label ep23_dialogue9_4:
    # Моника приходит к Мелани.
    # Моника: Ну что, ты довольна?!?!
    # Мелани отвечает: Миссис Бакфетт, Вы кончили или мне показалось?
    # Моника: Мне... Я... Это тебя не касается, Мелани!
    # Мелани! Что с нашим договором?!
    # Когда ты решишь вопрос с Маркусом?!
    # Мелани отвечает: Я займусь этим завтра, Миссис Бакфетт.
    # Скоро будут новости, не волнуйстесь.
    # Моника: Я буду ждать!
    music Pyro_Flow
    img 9042
    with fade
    if monicaMelanieCastingCummed == True:
        m "ну что, ты довольна?!?!"
        melanie "Миссис Бакфетт, Вы кончили или мне показалось?"
        music Hidden_Agenda
        img 9056
        with fade
        m "Мне... Я... Это тебя не касается, Мелани!"
        img 9057
        melanie "..."
        music Groove2_85
    m "Мелани! Что с нашим договором?!"
    "Когда ты решишь вопрос с Маркусом?!"
    music Groove2_85
    img 9059
    with fade
    melanie "Я займусь этим прямо завтра, Миссис Бакфетт."
    "Скоро будут новости, не волнуйтесь."
    img 9089
    m "Я буду ждать."

    # Мелани пропадает.
    return

label ep23_dialogue9_5a:
    # Вопрос у Алекса: Где Мелани?
    # Алекс отвечает что не видел ее и, может быть, Моника знает где она.
    # Моника отвечает что нет.
    music Groove2_85
    if cloth == "Whore":
        img 6528
        with fade
        m "Алекс, ты не видел Мелани?"
        img 6529
        alex_photograph "Нет, Миссис Бакфетт, ее сегодня не было."
        "Может быть Вы знаете где она?"
        img 6527
        with fade
        m "Я... Нет, Алекс... Я не знаю где Мелани..."
    if cloth == "CasualDress1":
        img 11238
        with fade
        m "Алекс, ты не видел Мелани?"
        img 6529
        alex_photograph "Нет, Миссис Бакфетт, ее сегодня не было."
        "Может быть Вы знаете где она?"
        img 11236
        with fade
        m "Я... Нет, Алекс... Я не знаю где Мелани..."
    if cloth == "WorkingOutfit1":
        img 12767
        with fade
        m "Алекс, ты не видел Мелани?"
        img 6529
        alex_photograph "Нет, Миссис Бакфетт, ее сегодня не было."
        "Может быть Вы знаете где она?"
        img 12765
        with fade
        m "Я... Нет, Алекс... Я не знаю где Мелани..."

    return


label ep23_dialogue9_5b:
    # Вопрос у секретарши: Где Мелани?
    # Секретарша отвечает что не видела ее и, может быть, Моника знает где она.
    music Groove2_85
    if cloth == "Whore":
        img 8268
        with fade
        m "Дорогуша, ты не видела Мелани?"
        img 8285
        secretary "Нет, Миссис Бакфетт."
        "Ее все ищут!"
        "Может быть Вы в курсе где она?"
        img 8270
        with fade
        m "Нет, дорогуша..."
        "Я... Я не имею представления где она может быть..."
    if cloth == "CasualDress1":
        img 11239
        with fade
        m "Дорогуша, ты не видела Мелани?"
        img 11240
        secretary "Нет, Миссис Бакфетт."
        "Ее все ищут!"
        "Может быть Вы в курсе где она?"
        img 11241
        with fade
        m "Нет, дорогуша..."
        "Я... Я не имею представления где она может быть..."
    if cloth == "WorkingOutfit1":
        img 12768
        with fade
        m "Дорогуша, ты не видела Мелани?"
        img 12769
        secretary "Нет, Миссис Бакфетт."
        "Ее все ищут!"
        "Может быть Вы в курсе где она?"
        img 12770
        with fade
        m "Нет, дорогуша..."
        "Я... Я не имею представления где она может быть..."
    return

label ep23_dialogue9_5c:
    # Вопрос у Бифа: Где Мелани?
    # Биф отвечает что малышка Мелани куда-то пропала. И что он ее накажет, когда она появится.
    music Groove2_85
    if cloth == "Whore":
        img 6453
        with fade
        m "Биф, ты не видел Мелани?"
        biff "Нет, цыпочка, я не видел ее."
        "Малышка Мелани куда-то пропала."
        "Папочка обязательно накажет ее, когда она появится!"
        img 6451
        with fade
        mt "Черт! Бедная Мелани..."
        "Я даже боюсь представить что сейчас с ней..."
    if cloth == "CasualDress1":
        img 11260
        with fade
        m "Биф, ты не видел Мелани?"
        biff "Нет, цыпочка, я не видел ее."
        "Малышка Мелани куда-то пропала."
        "Папочка обязательно накажет ее, когда она появится!"
        img 11261
        with fade
        mt "Черт! Бедная Мелани..."
        "Я даже боюсь представить что сейчас с ней..."
    if cloth == "WorkingOutfit1":
        img 12789
        with fade
        m "Биф, ты не видел Мелани?"
        biff "Нет, цыпочка, я не видел ее."
        "Малышка Мелани куда-то пропала."
        "Папочка обязательно накажет ее, когда она появится!"
        img 12790
        with fade
        mt "Черт! Бедная Мелани..."
        "Я даже боюсь представить что сейчас с ней..."
    return

label ep23_dialogue9_5d:
    mt "От Мелани нет новостей... Я даже боюсь представить что с ней..."
#    help "Узнайте что случилось с Мелани в следующих апдейтах игры!"
    return












label ep23_dialogue9:
    return
