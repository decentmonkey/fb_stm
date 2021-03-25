default monicaPubPrivatDance1 = False  # Моника согласилась пойти в приват с банкиром
default monicaPubPrivatDance2 = False  # Моника согласилась снять трусики и танцевать перед банкиром голой
default monicaPubPrivatDance3 = False # Моника села к банкиру на колени

#call ep211_dialogues5_shiny_hole_1() # гримерка, Эшли заставляет Монику идти в приват к банкиру
#call ep211_dialogues5_shiny_hole_2() # подсобка барменов, приват с банкиром и Эшли
#call ep211_dialogues5_shiny_hole_3() # разговор с Эшли о танце с Молли (после обычного разговора, когда отдает чаевые)
#call ep211_dialogues5_shiny_hole_4() # в гримерке с Молли (помириться или нет)


# если Моника ушла с паба после танцев и не отдала Эшли чаевые
# на след день Моника заходит в паб, при клике на барменов
# Эшли орет на Монику, что та украла чаевые (ep27_dialogues7_pub8)
# после этого при нажатии на "Просить прощения у Эшли", Моника танцует на сцене
# потом возвращается со сцены в гримерку
label ep211_dialogues5_shiny_hole_1:
    # Моника еще не переоделась и в гримерку заходит Эшли
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 23279
    with fadelong
    ashley "[monica_pub_name], танцы на сегодня еще не закончились."
    m "???"
    sound highheels_short_walk
    img 23281
    with fade
    ashley "Тебе еще нужно будет поработать..."
    ashley "Для одного клиента."
    # Моника смотрит на нее удивленно
    m "В смысле? Что значит поработать для одного клиента?!"
    img 23282
    with diss
    ashley "У моего заведения возникли финансовые трудности, по оплате кредита..."
    ashley "Знаешь-ли, не так-то просто содержать такое яркое место..."
    ashley "Да еще и обеспечивать тебя работой!"
    img 23283
    with fade
    m "..."
    ashley "Один из посетителей паба, Мистер Беркельбаух, работает в кредитном отделе банка."
    ashley "Он готов помочь."
    m "Я тут вообще причем?"
    img 23284
    with diss
    ashley "Этот банкир готов оказать помощь не просто так..."
    ashley "Он требует приват танец для него."
    # Моника упрямо
    img 23285
    with diss
    m "Ваша рыжая королева трущоб легко с этим справится."
    music Power_Bots_Loop
    img 23286
    with fade
    ashley "Перестань цепляться к Молли!"
    ashley "Она тут самая лучшая из моих девочек!"
    img 23287
    with diss
    m "!!!"
    music Groove2_85
    img 23288
    with fade
    ashley "Клиент требует приват с тобой."

    img 23289
    with diss
    m "Я не собираюсь в этом участвовать!"
    m "Кому надо, тот пусть и танцует в привате для этого неудачника!"
    # Моника разворачивается, чтобы уйти, но Эшли повышает голос
    music Power_Bots_Loop
    img 23290
    with fade
    ashley "В таком случае, [monica_pub_name], ты уволена!"
    ashley "Мало того, что ты постоянно крадешь чаевые..."
    ashley "Так еще и споришь со мной!"
    music Groove2_85
    ashley "Да, и передай Клэр, что она тоже уволена."
    ashley "И виновата в этом будешь только ты!"
    # Моника возмущенно

    img 23291
    with diss
    m "!!!"
    m "Что?! Клэр здесь ни при чем!"
    m "И вообще! Почему сразу увольнение?!"
    m "Только из-за того, что я отказалась идти в приват с каким-то..."
    m "Никчемным банкиром!"
    # Эшли орет
    img 23292
    with fade
    ashley "Да!"
    ashley "Я вынуждена буду уволить всех, если он откажется помогать!"
    music Power_Bots_Loop
    img 23293
    with hpunch
    ashley "Поэтому или ты сейчас же сделаешь так, как я сказала..."
    ashley "Или убирайся отсюда ко всем чертям!!!"
    img 23294
    with diss
    m "!!!"
    music Groove2_85
    img 23295
    with fade
    ashley "[monica_pub_name], иных вариантов нет."
    ashley "Я даже готова простить тебе то, что ты в очередной раз украла чаевые..."
    ashley "И отменить штраф..."
    img 23296
    with diss
    ashley "Если ты сейчас пойдешь в приват с этим банкиром."
    img 23297
    with fade
    m "..."
    music Hidden_Agenda
    img 23298
    with diss
    ashley "Тебе нечего бояться."
    ashley "Ты с ним будешь только вдвоем."
    ashley "Я тоже буду присутствовать..."
    ashley "Я должна убедиться, что все пройдет, как надо."
    # Моника в растерянности
    music Power_Bots_Loop
    img 23299
    with fade
    mt "Вот черт! И что мне теперь делать?"
    mt "Она сказала, что уволит не только меня, но и Клэр..."
    mt "..."
    music Groove2_85
    img 23300
    with diss
    mt "С другой стороны..."
    mt "Это же просто танец. Только не на сцене, а для одного клиента."
    mt "Тем более, что Эшли готова меня не штрафовать, если я соглашусь..."

    img 23301
    with fade
    m "..."
    m "Я станцую для него, но только в одежде!"
    ashley "Нет, [monica_pub_name], так дело не пойдет."
    ashley "Ты покажешь ему не только свою грудь..."
    music Loved_Up
    img 23302
    with diss
    ashley "Но и свою голенькую попку." # игриво
    ashley "А я проконтролирую, чтобы твою попку было хорошо видно..."
    # Моника в шоке смотрит на нее
    music Power_Bots_Loop
    img 23303
    with fade
    m "Я не буду танцевать перед ним голая!!!"
    m "За кого ты меня принимаешь?!"
    # Эшли говорит
    img 23304
    with hpunch
    ashley "Тогда выметайся отсюда, [monica_pub_name]!"
    ashley "Мне надоело с тобой спорить!!!"
    music Groove2_85
    img 23305
    with diss
    m "!!!"
    menu:
        "Пойти в приват с клиентом.":
            $ monicaPubPrivatDance1 = True # Моника согласилась пойти в приват с банкиром
            pass
        "Не делать этого! (увольнение с паба)":
            mt "Я не собираюсь раздеваться перед каким-то..."
            mt "Никчемным неудачником!"
            mt "Пусть Эшли сама вертит перед ним своим голым задом!"
            m "!!!"
            m "За кого ты меня принимаешь?!"
            m "Я не пойду ни в какой приват!"
            music Power_Bots_Loop
            img 23306
            with fade
            ashley "Тогда выметайся отсюда, [monica_pub_name]!!!"
            music stop
            img black_screen
            with diss
            sound highheels_short_walk
            pause 2.0
            music Pyro_Flow
            img 23307
            with fade
            with diss
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            # Моника гордо уходит
            return False
    # Моника зло смотрит на Эшли
    music Groove2_85
    img 23308
    with fade
    m "А сколько клиент мне за это заплатит?"
    music Loved_Up
    img 23309
    with diss
    ashley "Нисколько!"
    ashley "Ты будешь подарком от заведения."
    music Power_Bots_Loop
    img 23310
    with hpunch
    m "!!!"
    music Groove2_85
    img 23311
    with fade
    ashley "Но я готова простить тебе штраф за это."
    img 23312
    with diss
    mt "Дьявол!"
    m "Я пойду в приват. Где он?"
    sound highheels_short_walk
    img 23313
    with fade
    ashley "Приходи в подсобку после танца."
    ashley "Я с клиентом буду ждать тебя там."
    # Эшли уходит
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Power_Bots_Loop
    img 23314
    with fadelong
    mt "!!!"
    mt "Как я это сделаю?!"
    music Pyro_Flow
    img 23315
    with fade
    mt "..."
    mt "Так... Соберись!"
    mt "Ты [monica_pub_name], а не Моника Бакфетт."
    mt "А [monica_pub_name] не леди, а обычная стриптизерша."
    mt "Она не боится танцевать голой перед всякими неудачниками."
#    $ log1 = t_("Идти в подсобку барменов и станцевать приват.")
    return


# подсобка барменов
label ep211_dialogues5_shiny_hole_2:
    # банкир сидит, развалившись, на диване, Моника стоит перед ним в трусиках и маске, Эшли стоит возле двери
    # Моника немного растеряна, смотри на Эшли, потом на клиента
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.5
    music Groove2_85
    img 23316
    with fadelong
    w
    img 23317
    with fade
    mt "Эта извращенка Эшли не упустит своего шанса..."
    mt "Чтобы пялиться на меня!"
    mt "Делая вид, что она контролирует меня."
    img 23318
    with diss
    banker "О, детка..."
    banker "Наконец-то ты пришла, [monica_pub_name]."
    music Power_Bots_Loop
    img 23319
    with fade
    mt "Очередной никчемный неудачник."
    # банкир ведет себя оч вальяжно, самодовольно усмехается
    music Groove2_85
    img 23320
    with diss
    banker "Давай, крошка, лезь на стол."
    banker "Не заставляй меня ждать... Время - деньги."
    # Моника недовольна
    music Power_Bots_Loop
    img 23321
    with fade
    mt "Мерзкий тип!"
    mt "Если он притронется ко мне - врежу ему по яйцам!"
    music Groove2_85
    img 23322
    with diss
    ashley "Ну? Чего ты ждешь?!"
    ashley "Ты слышала, что тебе нужно сделать?"
    mt "!!!"
    menu:
        "Залезть на стол и танцевать.":
            pass
    # Моника забирается на стол и начинает танцевать
    # банкир в это время пялится на нее, периодически бросая взгляды на Эшли и рассматрия ее
    # Эшли пялится на прелести Моники, на банкра ноль внимания
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music RocknRoll_loop
    img 23323
    with fadelong
    w
    img 23324
    with fade
    w
    img 23325
    with diss
    w
    img 23326
    with fade
    w
    img 23327
    with diss
    w
    img 23328
    with diss
    w
    img 23329
    with fade
    w
    music stop
    img 23330
    with diss
    w
    sound snd_fabric1
    img 23331
    with diss
    w
    music RocknRoll_loop
    img 23332
    with fade
    w
    img 23333
    with diss
    w
    img 23334
    with fade
    w
    img 23335
    with diss
    w
    img 23336
    with diss
    w
    # через некоторое время банкир говорит Монике
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 23337
    with fadelong
    w
    img 23338
    with fade
    banker "Детка, снимай с себя трусики."
    banker "Хочу посмотреть, что ты там прячешь."
    music Power_Bots_Loop
    img 23339
    with hpunch
    mt "Черт!"
    # Моника медлит, смотрит на Эшли
    music Groove2_85
    img 23340
    with fade
    ashley "Выполняй!"
    img 23341
    with diss
    mt "!!!"
    menu:
        "Снять трусики.":
            $ monicaPubPrivatDance2 = True # Моника согласилась снять трусики и танцевать перед банкиром голой
            pass
        "Не делать этого! (увольнение с паба)":
            mt "Я не собираюсь танцевать голой перед..."
            mt "Перед каким-то никчемным неудачником!"
            mt "Пусть Эшли сама вертит перед ним своим голым задом!"
            m "!!!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            m "Нет!"
            m "Я не буду этого делать!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            # Моника гордо уходит
            return False
    music Groove2_85
    img 23342
    with fade
    mt "Это делает [monica_pub_name], а не я."
    mt "[monica_pub_name] просто потанцует и уйдет отсюда."
    # она снимает трусики и танцует, банкир пялится на нее, потом расстегивает штаны и достает стояк
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 23343
    with fadelong
    w
    img 23344
    with fade
    w
    img 23345
    with diss
    w
    img 23346
    with diss
    w
    img 23347
    with fade
    w
    img 23348
    with diss
    w
    img 23349
    with fade
    w
    img 23350
    with diss
    w
    img 23351
    with fade
    w
    img 23352
    with diss
    w
    img 23353
    with fade
    w
    img 23354
    with diss
    w
    img 23355
    with fade
    w
    img 23356
    with diss
    w
    img 23357
    with diss
    w
    img 23358
    with fade
    w
    img 23359
    with diss
    w
    img 23360
    with diss
    w

    img 23361
    sound Jump2
#    sound snd_fabric1
    banker "Эй, крошка."
    banker "Смотри, что у меня для тебя есть!"
    img 23362
    with diss
    banker "Пойдем ко мне!" # хлопает себя по бедру, зовет Монику к себе на ручки
    music stop
    img 23363
    with hpunch
    sound plastinka1b
    mt "?!?!?!"
    # Моника смотрит на Эшли
    music Power_Bots_Loop
    img 23364
    with fade
    m "Эшли?!"
    m "Мы так не договаривались!!!"
    music Groove2_85
    img 23365
    with diss
    ashley "Тебе просто нужно спуститься вниз и посидеть у клиента на коленях."
    ashley "он не будет тебя трогать. это всего-лишь приватный танец!"
    ashley "Чего здесь такого?!"
    img 23366
    with fade
    ashley "Делай, что тебе говорят!"
    img 23367
    with diss
    mt "Какого черта тут происходит?!"
    mt "Она решила подложить меня под этого мерзкого типа?!"
    mt "Знала бы она с кем вообще имеет дело!!!"
    mt "!!!"
    menu:
        "Сесть на колени к банкиру.":
            $ monicaPubPrivatDance3 = True # Моника села к банкиру на колени
            pass
        "Не делать этого! (увольнение из паба)":
            mt "Я не собираюсь этого делать!"
            mt "Пусть он лапает Эшли своими грязными руками!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            m "!!!"
            m "Нет!"
            m "Я не буду этого делать!"
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            # Моника гордо уходит
            return False
    # Моника зло смотрит на Эшли
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 23368
    with fadelong
    mt "Грязная извращенка!"
    mt "Ненавижу ее!!!"
    mt "!!!"
    # Моника спускается со стола и садится к банкиру на ручки
    # тот без особого энтузиазма лапает ее, Моника напряжена как струна
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up
    img 23369
    with fadelong
    w
    img 23370
    with fade
    banker "Мммм, какая ты аппетитная, крошка..."
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w
    sound drkanje5
    img 23371
    with diss # repeat
    w
    sound drkanje5
    img 23372
    with diss
    w

    img 23373
    with fade
    w
    img 23374
    with diss
    w
    # банкир, пока лапает Монику, поглядывает постоянно на Эшли
    # потом обращается к Эшли
    music Groove2_85
    img 23375
    with fade
    ashley "Ну что, Мистер Беркельбаух, Вы довольны?"
    ashley "Вы помните номер кредитного договора, по которому надо дать отсрочку?"

    img 23376
    with diss
    banker "Эшли, знаешь что больше всего в мире мне не нравится?"

    img 23377
    with fade
    ashley "Что, Мистер Беркельбаух?"

    img 23378
    with diss
    banker "Больше всего в мире мне не нравится, когда меня обманывают."

    img 23379
    with diss
    ashley "Что это значит? На что Вы намекаете? В чем обман?"

    img 23380
    with fade
    banker "Эшли, помнишь какое было условие?"
    ashley "Вы хотели увидеть самую красивую попку Shiny Hole..."
    ashley "И за это..."

    music Hidden_Agenda
    img 23381
    with diss
    banker "Я не уверен что это самая красивая попка Shiny Hole."
    banker "Возможно, ты обманываешь меня."

    music Groove2_85
    img 23382
    with fade
    ashley "ЧТО?! Я???"
    ashley "Я с самого начала говорила тебе... Вам..."
    ashley "С самого начала говорила что у Молли задница лучше, чем у [monica_pub_name]!"
    img 23383
    with diss
    ashley "Но ты... то есть Вы..."

    sound Jump1
    img 23384
    with fade
    banker "Эшли, прекрати! Задница Молли мне уже надоела."
    banker "Эта ваша королева Shiny Hole готова на все ради пары баксов на чай!"

    img 23385
    with diss
    ashley "В чем тогда дело?! Почему Вы обвиняете меня в нечестности?!"

    music Hidden_Agenda
    img 23386
    with fade
    banker "Я не уверен что у [monica_pub_name] лучшая задница, потому что я не могу сравнить их все."
    banker "Я еще не все увидел."
    banker "А, потому, я имею право сомневаться в том, что ты даешь мне то, что декларируешь."

    music Groove2_85
    ashley "Что я де... декл... Что это за слово?"

    img 23387
    with diss
    ashley "Послушайте, Мистер Беркельбаух, Вы наш постоянный клиент и Вы знаете, что Клэр не танцует приват."
    ashley "Ее задницу не получится оценить. Она танцует не ради денег."
    ashley "Я никак не могу надавить на нее. Если я буду настаивать, она просто уйдет отсюда!"

    img 23388
    with fade
    banker "Я вижу задницу Клэр через день! Пусть она в тоненьких трусиках, но я могу оценить ее из зала."

    img 23389
    with diss
    ashley "Но в чем тогда проблема? Это все что у нас есть!"
    ashley "У нас больше нет никаких попок, чтобы сравнить между ними!"
    ashley "Я честно выполнила то о чем мы договорились!"

    music Hidden_Agenda
    img 23390
    with fade
    banker "Нет, Эшли! Здесь, в Shiny Hole, есть еще одна попка, которую никто не видел!"
    banker "И ее не оценить из зала, потому что она пока не танцует, а зря!"

    music Groove2_85
    img 23391
    with diss
    ashley "Какая? Кто это? Почему я не знаю про нее?!"
    ashley "Это Джо снова притащил какую-то шлюху?!"
    ashley "Также как сделал это с [monica_pub_name]?"

    img 23392
    with diss
    mt "!!!"

    music Hidden_Agenda
    img 23393
    with fade
    banker "Нет, Эшли! Я говорю про твою попку!"

    music stop
    img 23394
    with hpunch
    sound plastinka1b
    ashley "ЧТО?! Причем здесь моя задница, Мистер Беркельбаух?!"

    music Hidden_Agenda
    img 23395
    with fade
    banker "При том, Эшли, что я подозреваю что твоя попка самая лучшая в Shiny Hole!"
    banker "И ты скрыла это от меня, тем самым обманув."
    banker "А ты уже знаешь что я больше всего не люблю..."

    music Groove2_85
    img 23396
    with diss
    ashley "Но... Но как можно сравнивать меня с..."
    ashley "С [monica_pub_name]?"

    music Hidden_Agenda
    img 23397
    with fade
    banker "Почему нельзя? Я не видел всех попок Shiny Hole и я имею право сомневаться!"

    img 23398
    with diss
    ashley "И что же ты хочешь?!"

    img 23399
    with diss
    banker "Залезай на стол и покажи свою попку, а я сравню ее с этой!"

    music Groove2_85
    img 23400
    with fade
    ashley "Вообще-то я замужем!"
    ashley "Моя попка, она... Она только для Джо, моего мужа!"

    img 23401
    with diss
    banker "Я не собираюсь сейчас трахать тебя, Эшли!"
    banker "И здесь нет твоего Джо! Он смотрит за баром, пока тебя нет."

    music Hidden_Agenda
    img 23402
    with diss
    banker "Но учти, отказ от проверки значит что ты что-то скрываешь от меня!"
    banker "Если ты не предоставишь доказательство того, что твоя попка хуже, чем у [monica_pub_name]..."
    banker "Или, если вдруг эта твоя попка не окажется хуже, чем у нее, то..."
    banker "То банк завтра же выставит требование о досрочном погашении всей вашей кредитной линии, Эшли!!!"
    banker "Я не терплю, когда меня пытаются выставить дураком, подсунув второсортный материал!"

    music Power_Bots_Loop
    img 23403
    with fade
    mt "ЧТО?!!"

    img 23404
    with diss
    ashley "!!!"
    banker "Давай! Залезай сейчас же! Я жду!"
    music Groove2_85
    banker "И пусть [monica_pub_name] встанет рядом с тобой!"

    img 23405
    with fade
    ashley "Ты мне что, не оставляешь выбора?! Ты знаешь что я вкладываю душу в этом место!"
    ashley "Я не могу потерять его!"

    music Hidden_Agenda
    img 23406
    with diss
    banker "Это ты не оставляешь мне выбора, Эшли! Ты отказываешься предъявить доказательство!"
    banker "Вертишься, юлишь..."
    banker "Ведь, если твоя попка и правда хуже, то тебе нечего бояться, правда?"

    music Power_Bots_Loop
    img 23407
    with fade
    ashley "!!!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 23408
    with fadelong
    w

    img 23409
    with fade
    banker "Да, и смотри на меня! Личико влияет на оценку любой попки!"
    banker "Исходя из специфики своей работы, я люблю все оценивать комплексно!"

    music Power_Bots_Loop
    img 23410
    with diss
    ashley "!!!"

    music Groove2_85
    img 23411
    with fade
    banker "Да, и скажи [monica_pub_name], чтобы она сняла свою маску."
    banker "Я вижу ее личико каждый день, когда она обслуживает клиентов."
    banker "Незачем скрывать его сейчас. Это помешает комплексной оценке!"

    music Power_Bots_Loop
    img 23412
    with hpunch
    m "ЧТО?!"

    music Groove2_85
    img 23413
    with fade
    ashley "Давай, снимай свою дурацкую маску, делай что он говорит!"
    ashley "И залезай сюда!"

    img 23414
    with diss
    m "Но!.."

    img 23415
    with fade
    ashley "Давай, он и так знает кто ты на самом деле!"

    music stop
    img 23416
    with hpunch
    sound plastinka1b
    m "Он знает кто Я???"

    music Groove2_85
    img 23417
    with diss
    ashley "Да, он знает, что ты новенькая официантка! Давай снимай!"
    menu:
        "Снять маску":
            pass
        "Не делать этого! (увольнение из паба)":
            m "Я не собираюсь делать подобное! Это уже слишком!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return False

    # Монике
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 23418
    with fadelong
    w
    img 23419
    with fade
    w
    music Pyro_Flow
    img 23420
    with diss
    ashley "Только попробуй сделать что-то, чтобы твоя задница понравилась ему меньше моей!"
    ashley "Тогда ты не просто вылетишь отсюда..."
    ashley "Но я снова повешу на тебя все украденные чаевые, которые до этого простила тебе!"
    img 23421
    with diss
    m "!!!"
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 23422
    with fade
    w
    img 23423
    with diss
    ashley "Встань в лучшую позу, какую только можешь! Соблазни его!"
#    music Loved_Up
    img 23424
    with fade
    mt "Что я делаю... О БОЖЕ..."
    mt "Я стоя голая... АБСОЛЮТНО ГОЛАЯ!!!"
    img 23425
    with diss
    mt "Без маски..."
    mt "Стою так, чтобы моя попа понравилась больше, чем задница хозяйки дыры в трущобах!"
    img 23426
    with fade
    mt "И понравилась кому?!?!"
    mt "Какому-то никчемному клерку из кредитного отдела занюханного банка!"
    img 23427
    with diss
    mt "Ведь он даже не представляет, на какую леди он сейчас смотрит!"
    mt "Ему недостижим мой уровень, даже в его снах!"
    img 23428
    with fade
    ashley "Ну, убедился?!"
    banker "Я пока размышляю..."
    sound drkanje5
    img 23429
    with fade #repeat
    w
    sound drkanje5
    img 23430
    with diss
    w
    sound drkanje5
    img 23429
    with diss
    w
    sound drkanje5
    img 23430
    with diss
    w
    sound drkanje5
    img 23429
    with diss
    w
    sound drkanje5
    img 23430
    with diss
    w
    sound drkanje5
    img 23429
    with diss
    w
    sound drkanje5
    img 23430
    with diss
    w


    img 23431
    with fade
    banker "Какое твое мнение, Эшли?"
    img 23432
    with diss
    ashley "В смысле какое мое мнение?"
    img 23433
    with fade
    banker "Как ты думаешь, чья задница хуже? Твоя или [monica_pub_name]?"
    ashley "Мне обязательно это говорить?"

    img 23434
    with diss
    banker "Да, Эшли. Я хочу услышать это от тебя."
    banker "Я хочу услышать твою уверенность... в своей правоте..."

    img 23435
    with fade
    ashley "!!!"
    ashley "Я... Я считаю..."
    ashley "Я считаю что моя задница хуже, чем у [monica_pub_name]."

    img 23436
    with diss
    banker "Хорошо, Эшли! Твоя уверенность убедила меня."
    banker "Да и, по правде говоря, твоя задница действительно ни к черту в сравнению с попкой [monica_pub_name]!"
    music Power_Bots_Loop
    img 23437
    with fade
    ashley "!!!"
    music Groove2_85
    img 23438
    with diss
    sound vjuh3
    banker "Я подпишу бумаги."
    banker "Но, впрочем, она не настолько уж плоха для сцены."
    banker "Я бы, как зритель, одобрил, если бы ты вышла на сцену в одном лишь фартуке."
    banker "Хе-хе!"

    img 23439
    with fade
    ashley "Мистер Беркельбаух!"
    ashley "Я уже говорила Вам, что для танцев у нас есть такие шлюхи, как [monica_pub_name]."
    ashley "Я занимаюсь здесь управлением и ведением бизнеса!"
    img 23440
    with diss
    banker "Да, Эшли. Конечно!"
    banker "Хе-хе!"
    banker "Сообщи мне, если у тебя снова возникнут финансовые трудности!"

    img 23441
    with fade
    m "Мы закончили? Я могу идти?!"

    img 23442
    with diss
    banker "Не так быстро! Я все еще не кончил."
    img 23443
    with diss
    banker "Эшли, ты ведь знаешь, приватный танец должен длиться, пока клиент не будет удовлетворен..."
    ashley "Да, Мистер Беркельбаух..."

    img 23444
    with fade
    ashley "[monica_pub_name], ты должна удовлетворить клиента!"
    with hpunch
    m "Что?! Я не знала о подобном правиле!"
    m "С какой стати Я..."

    img 23445
    with diss
    ashley "Знание правил не помогает тебе придерживаться их!"
    ashley "Не забывай почему ты оказалась здесь!"
    ashley "Быстро иди и удовлетвори клиента!"

    img 23446
    with fade
    m "Но как... Как я удовлетворю его?!"
    img 23447
    with diss
    banker "Я бы хотел чтобы эта прекрасная попка потерлась о мой банковский член."
    img 23448
    with fade
    ashley "Ты слышала?! Быстро иди к нему!"
    img 23449
    with diss
    m "!!!"
    menu:
        "Тереться о член Мистера Беркельбауха...":
            pass
        "Не делать этого! (увольнение из паба)":
            m "Я не собираюсь делать подобное! Это уже слишком!"
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Pyro_Flow
            img 23474 # с затемнением (одевается)
            with fadelong
            sound highheels_short_walk
            ashley "Тогда выметайся отсюда!!!"
            m "С радостью!"
            mt "Наконец-то, мне не нужно больше возвращаться в эту чертову дыру!"
            return False
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music2 Loved_Up
    img 23450
    with fadelong
    w
    img 23451
    with fade
    w
    img 23452
    with diss
    w
    img 23453
    with fade
    banker "Вот так... Да."
    w
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_PrivateDance1_1.ogg"
    scene black
    image videov_Monica_PrivateDance1_1 = Movie(play="video/v_Monica_PrivateDance1_1.mkv", fps=30)
    show videov_Monica_PrivateDance1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 23454
    with diss
    mt "Фу!"
    mt "!!!"
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_PrivateDance1_1.ogg"
    scene black
    image videov_Monica_PrivateDance1_2 = Movie(play="video/v_Monica_PrivateDance1_2.mkv", fps=30)
    show videov_Monica_PrivateDance1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 23455
    with diss
    w
#    music Loved_Up2
    img 23456
    with diss
    banker "Хорошая девочка."
    w
    img 23457
    with fade
    w
    img 23458
    with diss
    mt "Вот он извращенец!"
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_Monica_PrivateDance1_1.ogg"
    scene black
    image videov_Monica_PrivateDance1_3 = Movie(play="video/v_Monica_PrivateDance1_3.mkv", fps=30)
    show videov_Monica_PrivateDance1_3
    with fade
    wclean
    stop music
    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 23459
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    # вставить текст в арты

    # банкир кончает
    img 23460
    sound2 Jump1
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    # ахи?
    w
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    # Моника встает, он тоже и застегивает штаны
    img 23461
    with fade
    banker "Девочки, вы хорошо поработали."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound snd_zip
    pause 1.0
    music Groove2_85
    img 23462
    with fadelong
    banker "Эшли, жду тебя завтра у себя в банке."
    banker "Обсудим детали кредитного договора."
    img 23463
    with hpunch
    sound snd_slap1
    banker "Пока, крошка." # хлопает Монику по голой попе
    img 23464
    with diss
    w
    # банкир уходит
    # Эшли зло смотрит на Монику
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.0
    sound snd_fabric1
    pause 1.0
    music Pyro_Flow
    img 23465
    with fadelong
    w
    img 23466
    with fade
    ashley "!!!"
    img 23467
    with diss
    m "!!!"
    img 23468
    with fade
    ashley "[monica_pub_name], только попробуй рассказать об этом кому-нибудь!"
    ashley "Если хоть кто-то узнает!"
    ashley "Я тебя придушу!!!"
    img 23469
    with diss
    mt "Жаль. Думаю, Джо было бы интересно услышать подробности."
    img 23471
    with fade
    ashley "Поняла меня, [monica_pub_name]?!"
    img 23472
    with diss
    m "Иди ты к черту, Эшли!"
#    m "Я не расскажу никому."
    m "Знала бы я на что мне придется идти, то лучше бы уволилась отсюда!"
    img 23473
    with fade
    ashley "Все! Иди! Ты на сегодня свободна."


#    banker "Эшли!"
#    ashley "Да?"
#    banker "Считай, что сделка состоялась..."
#    banker "Только у меня есть одно условие."
#    mt "Только не это!"
#    mt "Сейчас этот козел скажет, что хочет секса со мной!"
#    mt "Нет! Нет!"
#    mt "Ни за что!!!"
#    # Эшли удивленно
#    ashley "Без проблем! Что за условие?"
#    # он снова смотрит на Монику, потом на Эшли
#    banker "Залезь на стол!"
#    banker "Мы с этой крошкой хотим посмотреть как ты танцуешь!"
#    mt "!!!"
#    mt "!!!!!!" # в шоке
#    ashley "Но..."
#    ashley "Кхм..."
#    ashley "Но я не танцую..."
#    banker "Я понимаю."
#    banker "Но ты же хочешь, чтоб наша договоренность состоялась?"
#    ashley "Д-да..."
#    banker "Тогда лезь на стол..."
#    # Эшли растеряна, Моника еле сдерживает злорадную ухмылку
#    mt "Ха! Так ей и надо, этой стерве!"
#    mt "И как она теперь выкрутится?"
#    # Эшли мнется, зыркает на Монику
#    ashley "Мистер..."
#    banker "Эшли, давай без лишних разговоров."
#    banker "Я не собираюсь тебя уговаривать."
#    banker "Если не залезешь сейчас на стол и не будешь танцевать..."
#    banker "Я уйду."
#    banker "И больше не подходи ко мне со своими просьбами."
#    menu:
#        "Залезть на стол и танцевать.":
#            pass
#    # Эшли нерешительно лезет на стол и начинает двигаться, постоянно зыркая на Монику
#    # Моника сидит крайне довольная, злорадно ухмыляется
#    banker "Другое дело, Эшли."
#    banker "У тебя хорошо получается."
#    banker "А что скажешь, если я тебе предложу..."
#    banker "Не просто снижение процента по кредиту..."
#    banker "А перекредитоваться на большую сумму под более выгодный процент, м?"
#    ashley "Еще более выгодные условия?"
#    banker "Да, Эшли..."
#    ashley "Более выгодные, чем те, о которых мы говорили?"
#    banker "Да, намного выгоднее..."
#    # Эшли довольно
#    ashley "Это очень интересное предложение."
#    banker "Ну вот и отлично..."
#    ashley "..."
#    banker "Расстегивай свою рубашку!"
#    ashley "Но..."
#    banker "Эшли, мы с этой крошкой не будем предлагать тебе дважды."
#    banker "Или ты показываешь нам грудь."
#    banker "Или предложение отменятся и я ухожу."
#    mt "Ха!!!"
#    mt "Получай, сучка!"
#    mt "Определенно, мне нравится этот приват!"
#    mt "Ха-ха!"
#    # Эшли злобно смотрит на Монику, потом на банкира
#    menu:
#        "Расстегнуть рубашку.":
#            pass
#    # расстегивает рубашку и оголяет грудь
#    ashley "!!!"
#    banker "Молодец, Эшли."
#    banker "Теперь танцуй..."
#    # Эшли начинает двигаться, грудь колышется, банкир начинает дрочить, одной рукой обнимая Монику за талию
#    banker "Вот так... Да."
#    banker "Хорошая девочка."
#    # Моника видит, что банкр дрочит на Эшли
#    mt "Она так ему нравится?!"
#    mt "Фу!"
#    mt "Вот он извращенец!"
#    # смотрит на Эшли, та танцует с голой грудью, зло смотрит на Монику
#    # Моника снова злорадно ухмыляется
#    # банкир кончает
#    # Моника встает, он тоже и застегивает штаны
#    banker "Девочки, вы хорошо поработали."
#    banker "Эшли, жду тебя завтра у себя в банке."
#    banker "Обсудим детали кредитного договора."
#    banker "Пока, крошка." # хлопает Монику по голой попе
#    # банкир уходит
#    # Эшли зло смотрит на Монику
#    ashley "[monica_pub_name], только попробуй рассказать об этом кому-нибудь!"
#    ashley "Если хоть кто-то узнает!"
#    ashley "Я тебя придушу!!!"
#    mt "Жаль. Думаю, Джо было бы интересно услышать подробности."
#    ashley "Поняла меня, [monica_pub_name]?!"
#    m "Я не расскажу никому."
#    ashley "Все! Иди! Ты на сегодня свободна."
    return True

# другой день, после того, как Моника отдает чаевые
label ep211_dialogues5_shiny_hole_3:
    # Эшли забирает у Моники чаевые, потом говорит
    music Groove2_85
    img 22849
    with fade
    ashley "Кстати, [monica_pub_name]!"
    ashley "Нашим клиентам очень понравился твой танец с Клэр."
    ashley "Они теперь просят, чтобы ты станцевала с Молли!"
    ashley "А как ты знаешь, желание наших клиентов - закон!"
    # Моника возмущенно
    music Power_Bots_Loop
    img 22850
    with diss
    m "!!!"
    m "Танцевать с этой рыжей сучкой?!"
    m "Да ни за что!!!"
    music Groove2_85
    img 22868
    with fade
    ashley "Тебе придется."
    ashley "И я уже говорила, чтобы вы прекратили эту свою битву сучек!"
    ashley "Она здесь королева и ее попка для меня важнее, чем твоя!"
    music Power_Bots_Loop
    img 22853
    with diss
    m "!!!"
    music Groove2_85
    img 22851
    with fade
    ashley "Ты так и не помирилась с ней?!"
    img 22852
    with diss
    m "Еще чего!"
    m "Я еще должна сама к ней подходить и мириться?!"
    m "После того, как она меня подставила?"
    img 22861
    with fade
    ashley "Да!"
    ashley "Тебе надо попросить у Молли прощения!"
    ashley "Вам придется в следующий раз вместе танцевать на сцене!"
    ashley "И мне не надо, чтобы вы поубивали друг друга там!"
    img 22860
    with diss
    ashley "Наши клиенты должны остаться довольны."
    ashley "Они щедро платят за танцы..."
    ashley "И выручка паба в эти дни значительно увеличивается."
    ashley "Так что никаких отговорок я слышать не буду!!!"
    music Power_Bots_Loop
    img 22853
    with fade
    mt "Черт!"
    mt "Долбанная Молли!"
    mt "!!!"
    return

# другой день. гримерка. если Молли на смене
label ep211_dialogues5_shiny_hole_4:
    # Моника заходит в гримерку, видит Молли и зло думает
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22813
    with fadelong
    mt "Ненавижу эту сучку!!!"
    mt "Теперь я еще должна и просить у нее прощения!"
    mt "!!!"
    mt "Я не буду этого делать!"
    sound highheels_short_walk
    img 22814
    with fade
    mt "Возможно, я просто попробую заговорить с ней."
    img 22815
    with diss
    w
    img 22824
    with diss
    mt "..."
    return
label ep211_dialogues5_shiny_hole_4b:
    # проходит к вешалке мимо Молли, та смотрит в зеркало и на Монику не обращает внимания
    menu:
#        "Заговорить с Молли (в следующем обновлении)":
#            return False
        "Ни за что!":
            # Моника смотрит зло на Молли
            music Power_Bots_Loop
            if cloth == "Whore":
                img 22823
                with fade
            mt "Нет!!!"
            mt "Я не буду разговаривать с этой сучкой!"
            if cloth == "Whore":
                img 22825
                with diss
            mt "Мне плевать, что там Эшли говорит!"
            mt "Ей надо, пусть сама с ней и танцует!"
            pass
    # рыжая зло смотрит на Монику и отворачивается
    music Pyro_Flow
    img 22816
    with fade
    molly "!!!"
    w
    return

label ep211_dialogues5_shiny_hole_5:
    mt "Гребаная Эшли!"
    mt "Она встала на сторону этой сучки Молли!"
    mt "И еще сказала что ее попка для нее значит больше, чем моя!"
    mt "Мне... конечно без разницы это, как мое прекрасное тело оценивают в каких-то грязных трущобах, но..."
    mt "Но у меня {c}нет особого желания отдавать свои чаевые этой Эшли!{/c}"
    return

label ep211_dialogues5_shiny_hole_6:
    mt "Кажется, Эшли не заметила что я не стала отдавать ей чаевые в прошлый раз."
    mt "Отлично!"
    return

label ep211_dialogues5_shiny_hole_7:
    mt "НОГИ МОЕЙ ЗДЕСЬ БОЛЬШЕ НЕ БУДЕТ В ЭТОЙ ДЫРЕ С ИЗВРАЩЕНЦАМИ!!!"
    mt "Я ДОСТАТОЧНО УМНА, ЧТОБЫ НАЙТИ ДРУГОЙ ПУТЬ РЕШИТЬ СВОИ ПРОБЛЕМЫ!!!"
    return False

label ep211_dialogues5_shiny_hole_8:
    mt "Мне надо надеть сценический костюм."
    mt "Не хватало еще чтобы клиент узнал меня..."
    return

label ep211_dialogues5_shiny_hole_9:
    mt "Это был кошмар!"

    mt "Он узнал меня, узнал кто я! Я была без маски!"
    mt "Но, с другой стороны, он узнал что я [monica_pub_name]..."
    mt "А не кто я на самом деле."
    mt "Все-равно, мне надо быть осторожнее!"
    mt "И эта гребаная Эшли! Она заставила меня тереться своей попой о какой-то грязный член!"
    mt "И еще и за бесплатно!"
    mt "!!!"
    return

# в след. апдейт
    # если выбран пункт меню "заговорить с Молли", то Моника говорит ей, что Эшли что-то говорила про их совместный танец
    # Молли, не смотря в ее сторону говорит - да, я слышала
    # molly: я бы ни за что с тобой не стала выходить на сцену, потому что ты грязная воровка (ехидно)
    # Моника-!!!
    # Молли: но говорят, что вы с Клэр хорошо заработали тогда
    # если чаевых и правда платят намного больше, то я так уж и быть потерплю твое присутствие рядом со мной
    # Моника сквозь зубы: да, чаевых платят больше
    # Молли: тогда окей. можно попробовать. я забираю все чаевые от танца. тогда скажу Эшли, что я тебя простила
    # Моника думает, что меньше всего она хочет выходить с этой сучкой
    # но если клиенты так просят, то Эшли рано или поздно все равно заставит ее это сделать
    # какая же эта рыжеволосая дрянь мерзкая
    # а вдруг она мне прямо на сцене сделает какую-нибудь гадость?!
    # пусть только попробует! я тогда точно не сдержусь и врежу ей!
    # Молли: чего ты там копаешься? иди на сцену первая, я выйду сразу за тобой
    # Моника зло на нее смотрит, переодевается и идет на сцену
    # танец
