label ep28_dialogues_jail1:
    # Моника ложится спать
    # Монике снится сон с Маркусом.
    music dream
    img white_screen
    with fade
    $ renpy.pause(5.0, hard=True)
    img black_screen
    music stop
    with Dissolve(2.0)
    music Villainous_Treachery
    img 21241
    with diss
    m "Маркус?!"
    m "ГДЕ Я?!"
    img 21242
    with diss
    m "У меня все болит!"
    m "О БОЖЕ!"
    music Malicious
    img 21253
    with fadelong
    w
    img 21254
    with diss
    w
    music Gearhead
    img 21243
    with fadelong
    marcus "Ты знаешь где ты..."
    img 21244
    with diss
    m "Это... Это Ранчо 218?!"
    m "Я... Я попала сюда?!"
    m "Но нет! Этого не может быть!"
    img 21245
    with diss
    m "Этого еще не случилось!"
    sound snd_woman_scream1a
    with hpunch
    m "НЕЕЕЕТ!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music Malicious
    img 21255
    with fadelong
    w
    img 21256
    with diss
    overseer "Охх... Ыыыыы..."

    music Master_Disorder
    img 21246
    with fadelong
    marcus "Это скоро случится..."
    img 21247
    with diss
    m "Зачем! Зачем ты снишься мне!"
    m "Уйди отсюда! Я должна отсюда выбраться!"
    m "Я должна проснуться!"
    img 21248
    with fade
    marcus "Я снюсь тебе, чтобы сказать как избежать всего этого..."
    img 21249
    with diss
    m "Что?"
    m "Ты... Ты можешь мне сказать как этого избежать?!"
    img 21250
    with diss
    m "Что мне сделать? Я сделаю все, абсолютно все!"
    img 21251
    with fade
    marcus "Полюбить меня..."
    img 21252
    with diss
    m "Что..."
    # Конец сна
#    return



#label ep28_dialogues_jail2:
# Боб приходит в камеру и начинает трогать Монику во сне
# Моника просыпается от кошмара и кричит на Боба что он делает здесь
# Боб смущается и отвечает что принес ей похлебку.
# Моника смотрит на похлебку с отвращением и говорит что ей не нужна эта жуткая еда
# Ей надо встретиться с Мистером Маркусом и уйти из этого жуткого места

    music Malicious
    img 21257
    with fadelong
    m "Что..."
    m "Что это?!"
    img 21258
    with diss
    m "Кто здесь!!!"
    music Power_Bots_Loop
    img 21259
    with fade
    m "БОБ?!"
    m "Что ты делаешь здесь?!"
    overseer "А... Кхм..."
    overseer "Я... Экхм..."
    music Groove2_85
    img 21260
    with fade
    overseer "Я принес тебе похлебку."
    m "!!!"
    mt "Фу! Какая гадость! Я и забыла как это выглядит..."
    music Power_Bots_Loop
    img 21261
    with diss
    m "Мне не нужна эта жуткая еда!"
    m "Мне надо встретиться с Мистером Маркусом! И я уйду из этого жуткого места!"
    m "Мне нечего делать здесь!"

# Боб отвечает что Мистер Маркус занят и пока не может встретиться с ней.
# Ей надо подождать его дольше.
# Моника возмущается как это так?! Ей что, ждать его здесь, в камере?!
# Боб отвечает что это не его дело. Она арестант и сидит в камере.
# Боб собирается уходить
# Моника останавливает Боба и берет еду
    music Groove2_85
    img 21262
    with fade
    overseer "Мистер Маркус еще занят и он не может встретиться с тобой."
    overseer "Тебе надо подождать его дольше."
    music Power_Bots_Loop
    img 21263
    with diss
    m "Как это так?! Мне что, ждать его здесь, в камере?!"
    music Groove2_85
    img 21264
    with fade
    overseer "Это не мое дело. Ты арестант и сидишь в камере."
    # уходит
    music Hidden_Agenda
    img 21265
    with diss
    mt "Черт! Я не помню, когда ела в последний раз..."
    mt "И еще неизвестно, сколько мне придется ждать этого Маркуса..."
    m "Стой!"
    m "Боб..."
    overseer "Чего тебе?"
    m "Боб... Дай сюда еду..."
    music stop
    img black_screen
    with diss
    sound man_steps
    img black_screen
    with Dissolve(1.5)
    call textonblack(t_("День 1")) from _call_textonblack_33
    img black_screen
    with Dissolve(2.0)
    return

label ep28_dialogues_jail3:
# Моника думает что же ей делать. Какой ужас и тд
# Моника может позвать Боба, но он не подходит
    music Malicious
    music2 stop
    img 21266
    with fadelong
    mt "Что же мне делать?"
    mt "Какой ужас! Я пришла к Маркусу, чтобы поговорить с ним."
    mt "А, вместо этого, снова оказалась здесь, в этой жуткой камере."
    img 21267
    with diss
    mt "Мне надо добиться этой встречи! Я сделаю это!"
    mt "Я не останусь здесь!"
    return

label ep28_dialogues_jail3b:
    mt "Он не подходит..."
    mt "Он не слышит или не желает подходить..."
    music2 stop
    music Villainous_Treachery
    img 21268
    with fade
    mt "А это кто?"
    mt "Похоже это детектив, который встречал меня вчера..."
    mt "Что он делает здесь?"
    return
# Вечером перед сном Монику окликивают заключенные
# Моника с ужасом видит что они у ее решетки
# Моника спрашивает что вы делаете здесь?! Как Вы сюда попали?

label ep28_dialogues_jail3a:
    mt "Никого нет..."
    call change_scene("police_cell2", "Fade_long") from _call_change_scene_389
    return False

label ep28_dialogues_jail4:
    music stop
    music2 stop
    img black_screen
    with diss
    pause 2.0
    music2 prison_yell_music
    img 21269
    with fadelong
    prisoner1 "Эй, подойди сюда!"
    img 21270
    with diss
    m "Что? Кто это зовет меня?"
    img 21271
    with fade
    prisoner1 "Подойди сюда! Мы тебя ждем!"
    music Power_Bots_Loop
    img 21272
    with hpunch
    m "Что?! Заключенные?!"

    img 21273
    with fade
    m "Что Вы делаете здесь?! Как Вы сюда попали?!"

# Заключенные отвечают что Боб разрешает выходить на прогулку перед сном.
# Моника спрашивает где Боб, они отвечают что его нет, он вернется позднее.
    music Groove2_85
    music2 stop
    img 21274
    with diss
    prisoner1 "Мы на прогулке!"
    prisoner1 "Боб разрешает нам выходить на прогулку перед сном."
    img 21275
    with fade
    m "Где Боб?!"
    mt "Мне надо тщательнее прикрываться. У меня внизу нет никакой одежды."
    mt "Я не могу допустить, чтобы эти животные увидели хотя бы краешек любого из интимных мест..."
    mt "Моего восхитительного тела."
    img 21276
    with diss
    prisoner1 "Боба нет. Он вернется позднее."

# Моника с ужасом говорит что вы же раньше не гуляли здесь. Уйдите отсюда!
# Те отвечают что Боб разрешил им гулять, потому что ему не удалось выполнить условие их молчания
# Какое еще условие?
# Заключенный спрашивает что шлюха что, забыла?
    music Power_Bots_Loop
    img 21277
    with fade
    m "Вы же раньше не гуляли здесь! Уйдите отсюда!"
    m "Немедленно!"

    music Groove2_85
    img 21278
    with diss
    prisoner1 "Боб разрешил нам гулять, потому что ему не удалось выполнить условие нашего молчания. Хе-хе."
    img 21279
    with diss
    m "Какое еще условие?"
    img 21280
    with fade
    prisoner1 "Шлюха, ты что, забыла?"

# Боб обещал им веселье с Моникой за то что те молчат и не надоедают Бобу своим шумом
# Вы не зайдете сюда!
# Заключенный отвечает что мы зайдем к тебе. Жаль что после этого Боб, скорее всего, запретит им гулять.
# Но это веселье того стоит!
    prisoner1 "Боб обещал нам веселье с тобой!"
    prisoner1 "За то что мы будем тихо себя вести и не надоедать Бобу своим шумом."
    music Power_Bots_Loop
    img 21281
    with diss
    m "Вы не зайдете сюда!"
    img 21282
    with fade
    prisoner1 "Мы зайдем к тебе, шлюха!"
    prisoner1 "После выполнения этого условия, Боб, скорее всего, запретит нам гулять и впредь."
    prisoner1 "Но это веселье того стоит!"
# Моника отвечает что никогда! Она должна встретиться с Мистером Маркусом и они не смеют трогать ее!
# Заключенные отвечают что Боб уже пообещал, что она будет принадлежать им сразу после встречи с Мистером Маркусом
# Моника отвечает что они не дождутся! Она не вернется сюда после встречи с ним!
# Заключенные смеются а куда же ты денешься?
    img 21283
    with diss
    m "Никогда! Никогда этого не будет!"
    m "Я скоро встречусь с Мистером Маркусом. Он ждет меня!"
    m "И Вы не смеете трогать меня!"
    img 21284
    with fade
    prisoner1 "Да, верно! Боб нам обещал тебя сразу после твоей встречи с Мистером Маркусом!"
    prisoner1 "Скоро ты будешь принадлежать нам!"
    img 21285
    with diss
    m "Не дождетесь! Я не вернусь сюда после встречи с ним!"
    img 21286
    with fade
    prisoner1 "Ха-ха-ха! А куда же ты денешься?"

# Про себя думает О Боже! Я не поеду на ферму!
# Отвечает что она вернется на свободу после Мистера Маркуса и никогда не увидит эти отвратительные морды!
    music stop
    img black_screen
    with diss
    pause 1.5
    music Malicious
    img 21287
    with fade
    mt "Куда я денусь..."
    mt "Куда?"
    mt "О БОЖЕ! Я не поеду на ферму, клянусь!"
    img 21288
    with diss
    m "После встречи с Мистером Маркусом я выйду на свободу!"
    m "И больше никогда не увижу ваших отвратительных морд! Вы бы только посмотрели на себя! Фи!"

# Заключенный отвечает чтобы она попросила прощения у них за свои слова!
# Моника отвечает что не собирается! У них действительно отвратительные морды!
# И они даже не представляют с кем разговаривают сейчас!
# Заключенный отвечает что они разговаривают со шлюхой.
    music2 prison_yell_music
    img 21289
    with fade
    prisoner1 "Попроси прощения за свои слова."
    music Pyro_Flow
    img 21290
    with fade
    m "И не собираюсь! У Вас действительно отвратительные морды!"
    m "Вы выглядите как жалкие гниющие червяки!"
    m "Вы даже не представляете с кем разговариваете сейчас!"
    music Groove2_85
    img 21291
    with diss
    prisoner1 "Мы?!"
    prisoner1 "Мы разговариваем со шлюхой."
# Только они пока не решили хорошая шлюха или плохая.
# ЧТООО?! Да как ты смеешь, урод, называть меня так!
# Заключенный отвечает, что шлюха, похоже, забыла, что хотела сбежать отсюда.
# Сегодня с утра приходил детектив от Мистера Маркуса и спрашивал про тебя, нарушала-ли ты какие-нибудь правила?
    prisoner1 "Только мы пока не решили хорошая шлюха или плохая."
    music Power_Bots_Loop
    img 21292
    with fade
    m "ЧТООО?! Да как ты смеешь, урод, называть меня так!"
    music2 stop
    music Master_Disorder
    img 21293
    with diss
    prisoner1 "Похоже шлюха забыла, что хотела сбежать отсюда!"
    prisoner1 "Сегодня с утра приходил детектив от Мистера Маркуса и спрашивал про тебя..."
    img 21294
    with diss
    prisoner1 "Нарушала-ли ты какие-нибудь правила?"
# Не нарушала-ли дисциплину здесь или что-нибудь еще?
# Моника в шоке
# Шлюхой очень интересуются. А шлюха, в то же время, вступила в сговор с надзирателем с целью побега.
# Моника отвечает что они ничего не докажут!
# Заключенные отвечают что запомнили дни, когда Боб отлучался в банк и встречался с риелтором.
    prisoner1 "Не нарушала-ли дисциплину здесь или что-нибудь еще?"
    img 21295
    with hpunch
    m "!!!"
    img 21296
    with fade
    prisoner1 "Шлюхой очень интересуются..."
    prisoner1 "А шлюха, в то же время, вступила в сговор с надзирателем с целью побега."
    music Power_Bots_Loop
    img 21297
    m "Вы ничего не докажете!"
    music Master_Disorder
    img 21298
    with fade
    prisoner1 "Мы запомнили дни, когда Боб отлучался в банк и встречался с риелтором."
    prisoner1 "Мы все слышали!"
# Детектив проведет расследование и быстро расколет Боба.
# Тогда Боба заменят и они будут этому рады. Другой надзиратель будет поумнее и с ним будет проще договориться.
# А заключенным увеличат паек, они уверены в этом. Паек, да! Паек!
    prisoner1 "Детектив проведет расследование и быстро расколет Боба."
    prisoner1 "Тогда Боба заменят и мы будем этому рады!"
    prisoner1 "Другой надзиратель будет поумнее и нам с ним будет проще договориться."
    prisoner1 "А нам за сотрудничество увеличат паек! Мы уверены в этом!"
    music prison_yell_music
    img 21299
    with diss
    prisoners "Паек, Да! Паек!"

# Так что пусть шлюха хорошенько подумает и ответит какая она? Хорошая или плохая?
# Плохая шлюха хотела сбежать, плохая шлюха нам не нужна здесь!
    music Groove2_85
    img 21300
    with fade
    prisoner1 "Так что пусть шлюха хорошенько подумает и ответит... Какая она?"
    prisoner1 "Хорошая или плохая?"
    prisoner1 "Плохая шлюха хотела сбежать, плохая шлюха не нужна нам здесь!"

# Моника в шоке смотрит
    img 21301
    m "!!!"

# Итак, отвечай!
    img 21302
    with fade
    prisoner1 "Итак, отвечай!"

# Моника думает что это ужас!
# Они расскажут Маркусу про то что она собиралась сбежать отсюда.
# Судя по тому, что здесь рыскает детектив, они так и ищут способ отправить Монику на ферму.
# Но, видимо, у них нет зацепок, чтобы сделать это.
# И, если заключенные все расскажут, то это будет конец!
# О БОЖЕ, Моника! Что же мне делать?
    music Malicious
    img 21303
    with fade
    mt "О УЖАС!"
    mt "Они расскажут Маркусу про то, что я собиралась сбежать отсюда!"
    mt "Судя по тому, что здесь рыскает детектив, они так и ищут способ отправить меня на ту ферму!"
    img 21304
    with diss
    mt "..."
    mt "Но, видимо, у них нет зацепок, чтобы сделать это."
    mt "Но, если заключенные им расскажут про мои попытки сбежать, то это будет конец!"
    mt "О БОЖЕ, Моника! Что же мне делать?"

# Неужели мне придется притворяться какой-то шлюхой здесь?!
# Но иначе мне не выжить! Это вопрос жизни и смерти.
# А, судя по словам Мелани, может быть и еще похуже смерти.
    img 21305
    with diss
    mt "Неужели мне придется притворяться какой-то шлюхой здесь?!"
    mt "..."
    mt "Но иначе мне не выжить! Это вопрос жизни и смерти."
    mt "А, судя по словам Мелани, может быть и еще похуже смерти..."

# Что же мне делать?
    mt "Что же мне делать?"
# Выбор:
# Притворяться шлюхой.
# Поставить их на место!
    menu:
        "Притворяться шлюхой.":
            pass
        "Поставить их на место!":
# Если поставить на место, то Моника говорит чтобы они заткнулись!
# Они сами нарушают правила тем, что заключают сделки с надзирателем.
# Гуляют здесь без разрешения администрации.
            $ questHelp("marcus_4a", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners
            return False

# Если притворяться шлюхой
# Заключенный спрашивает раздраженно. Ну, отвечай! Хорошая ты шлюха или плохая?!
# Моника отвечает, что она... хорошая шлюха
# Заключенные радуются: да, хорошая шлюха. Шлюха хорошая!
# Как зовут шлюху? Как у шлюхи имя?
    img 21306
    with fade
    prisoner1 "Ну, отвечай!"
    prisoner1 "Хорошая ты шлюха или плохая?!"
    m "..."
    mt "Я не могу допустить, чтобы Маркус узнал о моей попытке сбежать отсюда!"
    mt "Мне нужно как-то тянуть время..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 21314
    with fadelong
    mt "!!!"
    m "Я... Хорошая шлюха..."
    music prison_yell_music
    img 21315
    with diss
    prisoners "Да, хорошая шлюха!"
    prisoners "Шлюха хорошая!"
    music Groove2_85
    img 21316
    with fade
    prisoner1 "Как зовут шлюху? Какое у шлюхи имя?"
# Выбор
# Назвать свое имя
# Назваться Мэрилин (если открыто)
# Моника называет имя
    img 21314
    with diss
    menu:
        "Назвать свое имя.":
            $ monica_jail_name = t__("Моника Бакфетт")
            pass
        "Назваться [monica_pub_name]" if monicaWorkingAsDishwasher == True:
            $ monica_jail_name = monica_pub_name
            $ ep28_quests_monica_called_monicapubname = True
            pass
    img 21317
    with fade
    m "Меня зовут [monica_jail_name]..."
# Заключенные кричат да! Моника Бакфетт, шлюха!
# Заключенный говорит, скажи кто ты
    music2 prison_yell_music
    prisoners "Да! [monica_jail_name]! Шлюха!"
    music2 stop
    music Villainous_Treachery
    img 21318
    with fade
    prisoner1 "Скажи, кто ты!"
    img 21314
    with diss
    m "!!!"
    img 21318
    with fade
    prisoner1 "Ну же!"
# Я... Хорошая шлюха...
# О БОЖЕ!! Какой кошмар!
    img 21319
    with diss
    m "Я... Хорошая шлюха..."
    mt "О БОЖЕ! Какой кошмар!"

# Назови свое имя и скажи кто ты!
# ...
# Ну же!
# Меня зовут... Моника Бакфетт...
# И я... хорошая шлюха....
# Я делаю это чтобы выжить! Какой ужас!
    img 21320
    with fade
    prisoner1 "Назови свое имя и скажи кто ты!"
    img 21321
    with diss
    m "..."
    img 21322
    with hpunch
    prisoner1 "Ну же!"
    prisoner1 "И смотри на нас!"
    music Hidden_Agenda
    img 21323
    with diss
    m "Меня зовут... [monica_jail_name]..."
    m "И Я... хорошая шлюха..."
    mt "Какой ужас! Но я делаю это чтобы выжить..."

# Да! Да!
# Хорошая шлюха должна извиниться перед нами!
# И должна сказать что хочет показать нам свои сиськи!
# Да! Да! Сиськи!
    music prison_yell_music
    img 21324
    with fade
    prisoners "Да! Да!"
    prisoners "Хорошая шлюха должна извиниться перед нами!"
    img 21325
    with diss
    prisoner1 "И должна сказать, что хочет показать нам свои сиськи!"
    img 21324
    with fade
    prisoners "Да! Да!"
    prisoners "Сиськи!"

# Извиниться перед заключенными
# Поставить их на место!
    music Malicious
    img 21326
    with diss
    menu:
        "Извиниться перед заключенными.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_4a", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_1
            return False

# Мне надо делать что они говорят, иначе конец!
# Я буду притворяться и потяну время. Сегодня Мистер Маркус не смог встретиться со мной.
# Но я уверена, что завтра я увижусь с ним и этот кошмар закончится для меня!
    mt "Мне надо делать что они говорят, иначе конец!"
    mt "Я буду притворяться и потяну время."
    mt "Сегодня Мистер Маркус не смог встретиться со мной."
    mt "Но я уверена, что завтра я увижусь с ним и этот кошмар закончится для меня!"

# Ну же!
    music Villainous_Treachery
    img 21327
    with fade
    prisoner1 "Ну же!"

# Я... Я хорошая шлюха.
# И?!
# И я прошу прощения у вас. За то что назвала Вас некрасивыми.
# И?! Кто мы?!
    music Hidden_Agenda
    img 21328
    with diss
    m "Я... Я хорошая шлюха..."
    prisoner1 "И?!"
    m "И я прошу прощения у Вас. За то что назвала Вас некрасивыми..."
    music Villainous_Treachery
    img 21329
    with fade
    prisoner1 "И?! Кто Мы?!"
# Вы... Вы очень красивые мужчины и...
# И что?! Давай, шлюха! Говори это!
# И... И я хотела бы показать Вам свою грудь...
# Сиськи! Не груд, а сиськи! Скажи!
# !!!
    music Hidden_Agenda
    img 21330
    with diss
    m "Вы... Вы очень красивые мужчины и..."
    m "..."
    music Villainous_Treachery
    img 21331
    with fade
    prisoner1 "И что?! Давай, шлюха! Говори это!"
    img 21332
    with diss
    m "И... И я хотела бы показать Вам свою грудь..."
    img 21333
    with fade
    prisoner1 "Сиськи! Не грудь, а сиськи! Скажи!"

    img 21334
    with diss
    mt "!!!"
# Показать Вам... свои сиськи...
# Ну же! Показывай! Давай!
# Сиськи! Сиськи!
    m "Показать Вам... свои сиськи..."
    img 21335
    with fade
    prisoner1 "Ну же! Показывай! Давай!"
    music prison_yell_music
    img 21336
    prisoners "Сиськи! Сиськи!"

# Показать грудь
# Поставить их на место!
    img 21337
    with diss
    menu:
        "Показать грудь.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_4a", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_2
            return False

# Моника показывает грудь, закрывая другой рукой киску.
# Сиськи! Сиськи!

    mt "..."
    img 21338
    with fade
    prisoners "Сиськи! Сиськи!"
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21339
    with fadelong
    w
    img 21340
    with diss
    prisoner1 "Ближе! Подойди ближе! Нам плохо видно!"
    sound highheels_short_walk
    music2 prison_yell_music
    img 21341
    with fade
    prisoners "Сиськи! Сиськи!"
    music2 stop
    img 21342
    with diss
    w
    img 21343
    with diss
    mt "Боже! Как это унизительно!"
    mt "Похоже на какой-то очередной кошмарный сон..."
    mt "..."
    w
    music2 prison_yell_music
    prisoners "Сиськи! Сиськи!"


# Шлюха хочет показать нам и киску!
# Да! Киску! Киску!

# Ну же, шлюха! Давай показывай!
# Киску! Киску!
    img 21344
    with fade
    prisoner1 "Шлюха хочет показать нам и киску!"
    img 21345
    with diss
    prisoners "Да!"
    prisoners "Киску! Киску!"
    music Villainous_Treachery
    img 21346
    with fade
    prisoner1 "Ну же, шлюха! Давай показывай!"
    img 21347
    with diss
    prisoners "Киску! Киску!"
    img 21348
    with diss
# Показать свою киску
# Поставить их на место!
    menu:
        "Показать свою киску.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_4a", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_3
            return False

# Моника поднимает вторую руку вверх, держа робу.
    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21349
    with fadelong
    m "..."


# Да! Киска! Киска! Да!
    music2 prison_yell_music
    img 21350
    with diss
    prisoners "Да! Киска!"
    music2 stop
    img 21351
    with diss
    w
    img 21352
    with diss
    w
    img 21353
    with diss
    w
    music2 prison_yell_music
    img 21354
    with fade
    prisoner1 "Киска! Да!"
    mt "Это невыносимо!!!"
    mt "Если это и правда сон, то я хочу поскорее проснуться..."

# Шлюха хочет показать нас свою задницу!
# Давай шлюха, спрашивай разрешения у нас! Ты хочешь показать нам свою задницу!
# Давай, спрашивай нас!
    music Villainous_Treachery
    music2 stop
    img 21355
    with fade
    prisoner1 "Шлюха хочет показать нам свою задницу!"
    prisoner1 "Давай, шлюха, спрашивай разрешение у нас!"
    img 21356
    with diss
    prisoner1 "Ты хочешь показать нам свою задницу!"
    prisoner1 "Давай, спрашивай нас!"

# О БОЖЕ! Неужели мне придется сказать это?!
# Эту... гадость...
    music Malicious
    img 21357
    with fade
    mt "О БОЖЕ! Неужели мне придется сказать это?!"
    mt "Это... гадость..."

# Попросить разрешение показать свою попу
# Поставить их на место!
    menu:
        "Попросить разрешение показать свою попу.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_4a", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_4
            return False

# Я... Я прошу...
# Кто ты! Называй себя!
# Я... Хорошая шлюха...
# И я... прошу... разрешения показать свою спину...
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21358
    with fadelong
    m "Я... Я прошу..."
    prisoner1 "Кто ты! Называй себя!"
    img 21359
    with diss
    m "Я... Хорошая шлюха..."
    m "..."
    m "И Я... прошу... разрешения показать свою спину..."

# Задницу, шлюха! Свою задницу! Скажи это!
# Задницу! Да, задницу! Да!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21360
    with fade
    prisoner1 "Задницу, шлюха!"
    prisoner1 "Свою задницу!"
    prisoner1 "Скажи это!"
    img 21361
    with diss
    prisoners "Задницу! Да, задницу!"
    prisoners "Да! Да!"

# Я... прошу разрешения показать свою... свою задницу...
    music2 stop
    music Hidden_Agenda
    img 21362
    with fade
    m "Я... прошу разрешения показать свою... свою задницу..."

# Да, jail_name хорошая шлюха! Да!
# Мы разрешаем тебе показать свою задницу, шлюха! Давай!
    music Villainous_Treachery
    music2 stop
    img 21363
    with fade
    prisoner1 "Да, [monica_jail_name] хорошая шлюха! Да!"
    prisoner1 "Мы разрешаем тебе показать свою задницу, шлюха! Давай!"
    prisoner1 "И поставь ноги пошире! Да!"

# Моника показывает свой зад
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    img 21364
    with fadelong
    m "!!!"
    img 21365
    with diss
    w
    music2 prison_yell_music
    img 21366
    with fade
    prisoner1 "Подыми одежду! Мы не видим твоей задницы!"
    prisoner1 "Ты же сама просила показать ее нам!"
    img 21367
    with diss
    prisoners "Задница! Да, задница!"
    prisoners "Да! Да!"

# Да, хорошая задница! Да!
    music2 stop
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21368
    with fadelong
    mt "Не могу поверить, что показываю свое восхитительное тело в таком грязном месте..."
    mt "Каким-то заключенным..."
    img 21369
    with diss
    w
    music2 prison_yell_music
    img 21370
    with fade
    prisoner1 "Да, хорошая задница! Да!"
    music2 stop
    img 21372
    with diss
    w
    img 21371
    with diss
    w

# Мы хотим потрогать ее! Да!
# Да! Потрогать! Мы хотим потрогать шлюху! Потрогать, да!

    music stop
    img black_screen
    with diss
    pause 1.5
    music Villainous_Treachery
    music2 prison_yell_music
    img 21373
    with fadelong
    prisoner1 "Мы хотим потрогать ее! Да!"
    prisoners "Да! Потрогать!"
    img 21374
    with diss
    prisoners "Мы хотим потрогать шлюху!"
    img 21375
    with diss
    prisoners "Потрогать, Да!"

# Нет! Ни за что! Я не дам Вам трогать меня!
    music2 stop
    music Power_Bots_Loop
    img 21377
    with hpunch
    m "Нет! Ни за что!"
    img 21376
    with diss
    m "Я не дам Вам трогать меня!"

# Тогда ты будешь плохой шлюхой! А ты знаешь что будет с плохой шлюхой!
# Да! Плохая шлюха! Плохая! Нам не нужна плохая шлюха!
# Нам нужна хорошая шлюха, да!
    music Villainous_Treachery
    img 21378
    with fade
    prisoner1 "Тогда ты будешь плохой шлюхой!"
    prisoner1 "А ты знаешь что будет с плохой шлюхой!"
    music2 prison_yell_music
    img 21379
    with diss
    prisoners "Да! Плохая шлюха! Плохая!"
    prisoners "Нам не нужна плохая шлюха!"
    prisoners "Нам нужна хорошая шлюха! Да!"
    img 21380
    with diss
    m "!!!"
# Хорошая шлюха идет к нам, чтобы мы потрогали ее, да!
    img 21381
    with fade
    prisoner1 "Хорошая шлюха идет к нам, чтобы мы потрогали ее! Да!"
    prisoner1 "Мы не будем трахать шлюху пока! Мы только хотим потрогать ее!"

# Моника думает что это какой-то кошмар.
# Что чтобы выжить, ей приется дать себя облапать каким-то ничтожествам.
# Каким-то заключенным. Облапать ее, Монику Бакфетт!
# Как это может быть?! Неужели все это реальность?! О БОЖЕ!
    music2 stop
    music Malicious
    img 21382
    with fade
    mt "Это какой-то кошмар... Я не могу в это поверить..."
    mt "Чтобы выжить, мне придется дать себя облапать каким-то ничтожествам..."
    mt "Каким-то заключенным... Облапать меня, Монику Бакфетт!!!"
    mt "Как такое может быть?! Неужели все это реальность?!"
    mt "О БОЖЕ!"

    music Groove2_85
    img 21383
    with fade
    prisoner1 "Ну же! Иди сюда!"
    prisoner1 "Я только потрогаю какая твоя попа на ощупь!"
    prisoner1 "Только Я! Больше никто! Можешь не бояться!"
    prisoner1 "И на сегодня все!"

# Что же мне делать?!
    music Malicious
    img 21384
    with diss
    mt "Что же мне делать?"

# Подойти к заключенным.
# Поставить их на место!
    menu:
        "Подойти к заключенным.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_4a", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_5
            return False

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Malicious
    music2 prison_yell_music
    sound highheels_short_walk
    img 21385
    with fadelong
    mt "Это единственный выход..."
    img 21386
    with diss
    mt "Если они сообщат детективу хоть что-то о моих прошлых планах побега..."
    img 21387
    with diss
    mt "То меня ждет участь намного хуже этой..."
# Моника подходит к заключенным, спиной
# Ее лапают.
    music Gearhead
    sound Jump2
    img 21388
    with hpunch
    m "О БОЖЕ!"
    menu:
        "Вырваться.":
            img black_screen
            with diss
            pause 1.0
            music2 stop
            sound anger4
            img 21624
            with fade
            with hpunch
            m "Аааргхх!!!"
            music2 prison_yell_music
            prisoner2 "Ааааа! Она укусила меня!"
            prisoner2 "Эта сучка укусила меня!"
            img 21625
            with diss
            prisoner2 "Эта сучка откусила мне палец! Аааааа!!!"
            sound snd_kick_fred1
            music2 stop
            img 21626
            with hpunch
            m "На! Получай!"
            music2 prison_yell_music
            prisoner1 "Ааааа! Мои яйца!!!"
            prisoner1 "Она раздавила их каблуком! Аааааа!!!"
            prisoner2 "Эта сучка ненормальная!"
            prisoner2 "Бежим от нее!"
            music2 stop
            music Pyro_Flow
            img 21627
            with fadelong
            m "Только попробуйте еще раз приблизиться ко мне, ничтожества!"
            m "И я оторву ваши яйца и заставлю сожрать их!!!"
            $ ep28_quests_monica_kicked_prisoners = True
            $ questHelp("marcus_4a", False)
            return False
        "Если я буду сопротивляться, то они расскажут Маркусу про меня...":
            pass

    #sound звук облапывания Моники в камере
    sound scream1
    img 21389
    with fade
    m "Вы же обещали!"
#    m "..."

# Да! Хорошая! Шлюха!
# Шлюха хорошая! Да!
# И я хочу! И мне тоже дайте!
    #sound хватают за ягодицу
    sound grabbing4
    img 21390
    with diss
    prisoners "Да! Хорошая! Шлюха!"
    img 21391
    with diss
    prisoners "Шлюха хорошая! Да!"
    prisoner3 "И я хочу! И мне тоже дайте!"
# И мне! И мне!
# Потрогать шлюху!
# О чередь! Шлюха одна, а нас много!
# Да, очередь! Очередь!
    prisoner5 "И мне!"
    prisoner6 "И мне!"
    #sound хватают за грудь
    sound grabbing3
    img 21392
    with fade
    mt "Нет!"
    prisoner1 "В очередь! Шлюха одна, а нас много!"
    #sound хватают за вторую грудь
    sound grabbing3
    img 21393
    with diss
    mt "!!!"
    prisoner2 "Потрогать шлюху!"
    #sound хватают за вторую грудь еще одной рукой
    sound grabbing6
    img 21394
    with fade
    mt "Не-е-е-ет!"
    prisoners "Да, очередь! Очередь!"
    #sound хватают за талию
    sound grabbing7
    img 21395
    with diss
    prisoners "Да! Хорошая! Шлюха!"
    #sound хватают за ягодицу
    sound grabbing4
    img 21396
    with diss
    prisoner2 "Потрогать шлюху!"
    img 21397
    with diss


# Моника в шоке.
# Моника думает что я сплю, это какой-то кошмарный сон.
# Это не в реальности!
    mt "!!!"
    mt "Я сплю..."
    mt "Это какой-то кошмарный сон..."
    #sound хватают за ягодицу ближе к киске
    sound grabbing7
    img 21398
    with diss
    mt "Это не в реальности..."
    img 21399
    with fade
    mt "Этого не может быть..."
    #sound хватают за киску снизу
    sound grabbing9
    img 21400
    with hpunch
    m "АЙ!!!"
    img 21401
    with fade
    mt "Я... чувстую как каждый сантиметр моей кожи лапают эти грязные руки..."
    $ questHelp("marcus_4a", True)

# Кто-то кричит Боб! Боб идет!
# Быстро в камеры, ребята!
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music2 prison_yell_music
    img 21402
    with fadelong
    prisoners "Да! Хорошая! Шлюха!"
    prisoners "Шлюха хорошая! Да!"

    img 21403
    with hpunch
    prisoner6 "Боб! Боб идет!"
    prisoner1 "Быстро в камеры, ребята!"
    music stop
    music2 stop
    img black_screen
    with diss
    #sound заключенные убегают
    sound running
    pause 2.0
    music I_Feel_You
    img 21404
    with fadelong
    mt "Что... Это было..."
    mt "Он сказал, что потрогает меня один..."
    mt "Но на что я рассчитывала? О БОЖЕ!"
    mt "У меня не было другого выхода, не было!"
    img 21405
    with diss
    mt "Может быть, рассказать Бобу о том, что они шантажируют меня?"
    mt "Но нет... Он такой глупый, что будет только хуже..."
    mt "Мне надо скорее об этом забыть!"
    return True

label ep28_dialogues_jail5:
    # Моника может постучать в решетку и Боб кричит я занят, хватит шуметь!
    overseer "Я занят! Хватит шуметь!"
    return False
# Моника ложится спать и думает что надо заснуть, завтра я проснусь и этот кошмарный сон исчезнет.
label ep28_dialogues_jail6:
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music I_Feel_You
    img 21406
    with fadelong
    mt "Надо заснуть... Мне надо заснуть..."
    mt "Завтра я проснусь и этот кошмарный сон исчезнет..."
    mt "..."
    mt "Эта лампа... Как она мешает мне..."
    return

label ep28_dialogues_jail7:
# С утра Моника встает и думает что надо позвать Боба, Мистер Маркус должен встретиться с ней!
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("День 2")) from _call_textonblack_35
    img black_screen
    with Dissolve(2.0)
    music Malicious
    img 21407
    with fadelong
    mt "Мне надо позвать Боба! Мистер Маркус должен встретиться со мной!"
    music stop
    img black_screen
    with diss
    pause 1.5
    return

# Приходит Боб.
# Моника спрашивает где Мистер Маркус?
# Боб отвечает что он еще занят и не распоряжался о встрече.
# Моника говорит скажите ему что я хочу встретиться с ним, пожалуйста!
label ep28_dialogues_jail8:
    music stop
    music2 stop
    img black_screen
    with diss
    sound man_steps
    pause 2.0
    music Groove2_85
    img 21408
    with fadelong
    overseer "Чего тебе?"
    m "Где Мистер Маркус?"
    img 21409
    with diss
    overseer "Мистер Маркус занят и не распоряжался о встрече."
    m "Боб, скажите ему, что я хочу встретиться с ним, пожалуйста!"
# Боб отвечает что это не его дело, но, вроде бы Мистер Маркус освободится завтра.
# И он может дать ей поесть, если та хочет.
# Либо не шуметь!
# Моника говорит что да, дай, пожалуйста, поесть. Боб уходит и приносит еду.
    img 21410
    with fade
    overseer "Это не мое дело! Хотя, вообще-то, кажется я слышал Мистер Маркус освободится завтра."
    overseer "Я могу дать тебе поесть, если хочешь."
    overseer "Либо не шуми больше!"
    m "Да, Мистер Боб... Дайте, пожалуйста, мне поесть..."
    #Боб уходит и приносит еду.
# Итак, завтра! Завтра я встречусь с Мистером Маркусом и этот кошмар закончится, я уверена!
    music stop
    img black_screen
    with diss
    sound snd_eating
    pause 2.0
    music Malicious
    img 21411
    with fadelong
    mt "Итак, завтра!"
    mt "Завтра я встречусь с Мистером Маркусом и этот кошмар закончится, я уверена!"
    return

label ep28_dialogues_jail9:
    music stop
    music2 stop
    img black_screen
    with diss
    pause 2.0
    music2 prison_yell_music
# Моника ложится спать.
# Ее будят крики шлюха!
# Шлюха! Нам нужна наша шлюха!
    img 21412
    with fadelong
    w
    img 21413
    with diss
    prisoners "Шлюха! Нам нужна наша шлюха!"
    img 21414
    with fade
    prisoners "Шлюха!"

# Моника встает и кричит на них: что вам снова надо от меня!
# Нам нужна шлюха! jail_name, наша шлюха!
# Шлюха сегодня хорошая?! Или шлюха снова плохая?!
# Шлюха, отвечай!
    music Power_Bots_Loop
    img 21415
    with diss
    m "Что Вам снова надо от меня?!"
    music stop
    img 21416
    with fade
    prisoners "Нам нужна шлюха! [monica_jail_name], наша шлюха!"
    music Villainous_Treachery
    img 21417
    with diss
    prisoner1 "Шлюха сегодня хорошая?"
    prisoner1 "Или шлюха снова плохая?!"
    prisoner1 "Шлюха, отвечай!"

# О БОЖЕ! Снова они!
# Что же мне делать?! Мне надо как-то дождать завтрашнего дня!
# Если они расскажут обо мне, то мне конец! Всего один день!
# Может быть стоит перетерпеть это? Эти унижения! Это путь к моей свободе!
# Мне надо пройти его! Но смогу-ли Я?!
    music2 stop
    music Malicious
    img 21418
    with fade
    mt "О БОЖЕ! Снова они!"
    mt "Что же мне делать?! Мне надо как-то дождаться завтрашнего дня!"
    mt "Если они расскажут обо мне, то мне конец!"
    mt "Всего один день!"
    img 21419
    with diss
    mt "..."
    mt "Может быть стоит перетерпеть это? Эти унижения..."
    mt "Это пусть к моей свободе..."
    mt "Мне надо пройти его!"
    mt "Но смогу-ли Я?.."

# Притворяться шлюхой.
# Поставить их на место!
    menu:
        "Притворяться шлюхой.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_6
            return False

# Я... Я хорошая шлюха...
# Хорошая шлюха встанет на колени и повернется к нам задницей! Да!
# Мы предвкушаем твою задницу, шлюха!
# Достают члены
# Мы хотим получить удовольствие от нее, прямо сейчас!
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21420
    with fadelong
    m "Я... Я хорошая шлюха..."
    music Villainous_Treachery
    music2 prison_yell_music
    img 21421
    with diss
    prisoner1 "Хорошая шлюха встанет на колени и повернется к нам задницей! Да!"
    prisoner1 "Мы предвкушаем твою задницу, шлюха!"
# Достают члены
    sound snd_fabric1
    img 21422
    with fade
    w
    sound Jump2
    img 21423
    with hpunch
    prisoner1 "Мы хотим получить удовольствие от нее, прямо сейчас!"

# О БОЖЕ!
# Что Вы собираетесь делать?!
# Мы будем дрочить на тебя, шлюха! Скоро ты будешь наша!
# А пока мы хотим подрочить на твою задницу! Вставай своей задницей, сейчас же!
    music2 stop
    music Malicious
    img 21424
    with fade
    m "О БОЖЕ!"
    m "Что Вы собираетесь делать?!"
    music Villainous_Treachery
    music2 prison_yell_music
    img 21425
    with diss
    prisoner1 "Мы будем дрочить, шлюха! Скоро ты будешь наша!"
    music stop
    sound Jump1
    img 21426
    with hpunch
    w
    sound Jump1
    img 21427
    with hpunch
    w
    sound Jump1
    img 21428
    with hpunch
    w
    sound Jump2
    img 21429
    with hpunch
    w
    music Villainous_Treachery
    img 21430
    with fade
    prisoner1 "А пока мы хотим подрочить на твою задницу!"
    prisoner1 "Садись на колени и вставай своей задницей к нам, сейчас же!"

# Сделать как велят заключенные.
# Поставить их на место!
    music Malicious
    img 21431
    with diss
    menu:
        "Сделать как велят заключенные.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_7
            return False

    mt "У меня нет другого выхода..."
    mt "Мне надо притворяться будто я слушаю их..."
    mt "Иначе мне конец..."

    sound highheels_short_walk
    img 21432
    with diss
    mt "Боже! Я не могу поверить что делаю это..."
    music Villainous_Treachery
    img 21433
    with fade
    prisoner1 "Ближе, шлюха!"
    prisoner1 "Сядь ближе! Нам не видно твоей задницы!"
    music Malicious
    img 21434
    with diss
    menu:
        "Сесть ближе к заключенным.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_8
            return False
# Моника встает на колени, голой попой к заключенным.
    mt "Я пододвинусь к ним... Аккуратно..."
    mt "Главное чтобы они не смогли схватить меня..."
    mt "Как в прошлый раз..."
    music stop
    music2 stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    img 21435
    with fadelong
    m "..."
# Заключенные дрочат.
# Да, шлюха! Скажи! Скажи что эта шлюха и ее задница принадлежат нам!
# Скажи!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21436
    with fade
    prisoner1 "Выше! Выше задницу!"
    prisoner1 "Нам плохо видно!"
    prisoner1 "Шлюха должна поднять одежду, чтобы был лучший обзор! Да!"

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Villainous_Treachery
    img 21437
    with diss
    prisoner1 "Да, шлюха!"
    img 21438
    with diss
    w
    prisoner1 "Скажи что эта шлюха и ее задница принадлежат нам!"
    prisoner1 "Скажи!"

# О БОЖЕ!! Неужели я скажу такое?!
    music Malicious
    music2 stop
    img 21439
    with fade
    mt "О БОЖЕ! Неужели я скажу такое?!"

# Ну же, шлюха! Мы ждем!
    music2 prison_yell_music
    img 21440
    with fade
    prisoner1 "Ну же, шлюха! Мы ждем!"

# Сказать что Моника шлюха и что ее задница принадлежит заключенным.
# Поставить их на место!

    menu:
        "Сказать, что Моника шлюха и что ее задница принадлежит заключенным.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_9
            return False

# Главное - понтянуть время, Моника! Я скажу им все что угодно, чтобы выиграть время...
# Эта... Эта шлюха хорошая...
# Эта шлюха и ее задница... принадлежат вам...

    mt "Главное - потянуть время, Моника!"
    mt "Я скажу им все что угоодно, чтобы выиграть время..."
    music2 stop
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21441
    with fadelong
    m "Эта... Эта шлюха хорошая..."
    img 21442
    with diss
    m "Эта шлюха и ее задница... принадлежат вам..."

# Да! Хорошая шлюха!
# Хорошая шлюха, Да! Да!

# Скажи что эта задница всегда будет к нашим услугам, скажи!
# Скажи! Скажи! Задница! Скажи!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21443
    with fade
    prisoners "Да! Хорошая шлюха!"
    prisoners "Хорошая шлюха! Да! Да!"

    img 21444
    with diss
    prisoner1 "Открой свою киску!"
    prisoner1 "Покажи нам что у шлюхи внутри!"

    menu:
        "Положить палец на свою киску и раздвинуть ее.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_10
            return False
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    #sound Моника раскрывает киску
    sound chpok3
    music Loved_Up
    img 21446
    with fadelong
    w
#    img 21447
    music2 prison_yell_music
    img 21445
    with diss
    prisoners "Хорошая шлюха! Да! Да!"
    img 21448
    with diss
    prisoners "Да! Хорошая шлюха!"
    music Villainous_Treachery
    img 21449
    with fade
    prisoner1 "Скажи что эта задница всегда будет к нашим услугам! Скажи!"
    img 21450
    with diss
    prisoners "Скажи! Скажи! Задница! Скажи!"

# Сказать что попа Моники всегда к услугам заключенных.
# Поставить их на место!
    menu:
        "Сказать, что попа Моники всегда к услугам заключенных.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_11
            return False

# Как я могу сказать такое?! Неужели я это сделаю?!
# Это все сон! Это какой-то кошмар! Я не верю в то что это происходит!
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Malicious
    img 21451
    with fadelong
    mt "Как я могу сказать такое?! Неужели Я это сделаю?!"
    mt "Это все сон!"
    mt "Это какой-то кошмар!"
    mt "Я не верю в то, что это просходит на самом деле!"

# Ну же, шлюха!
# Мы ждем!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21452
    with fade
    prisoner1 "Ну же, шлюха!"
    prisoner1 "Мы ждем!"

# Задница этой шлюхи всегда к вашим услугам...
# В любое время, шлюха! Скажи это!
    img 21453
    with diss
    mt "..."
    mt "Грязные животные..."
    mt "Я скажу это... Эту мерзость..."
    mt "Только бы они не трогали меня больше..."
    mt "Я не смогу пережить это еще раз!"
    m "Задница этой шлюхи всегда к Вашим услугам..."
    prisoner1 "В любое время, шлюха! Скажи это!"

# Задница этой шлюхи всегда к вашим услугам... в лобое время...
    music Hidden_Agenda
    music2 stop
    img 21454
    with fade
    m "Задница этой шлюхи всегда к Вашим услугам... в любое время..."

# Да! Шлюха! Да!
# Кончают...
# Хорошая шлюха! Хорошая! Да!
# Скоро мы вставим свои члены в эту аппетитную задницу! Да!
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    music2 prison_yell_music
    img 21455
    with fadelong
    prisoners "Да! Шлюха! Да!"
    # Кончают...
    sound bulk1
    img 21456
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner1 "АААааааххх!!!"
    sound bulk1
    img 21457
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner2 "АААааааххх!!!"

    img 21458
    with fade
    prisoners "Хорошая шлюха! Хорошая! Да!"
    prisoner1 "Скоро мы вставим свои члены в эту аппетитную задницу! Да!"
# Скажи, шлюха! Скажи, что ты ждешь наши члены в своей заднице!
# Скажи это, шлюха!
    music Villainous_Treachery
    prisoner1 "Скажи, шлюха! Скажи, что ты ждешь наши члены в своей заднице!"
    prisoner1 "Скажи это, шлюха!"
# m "!!!"
# Нет!!!
    music2 stop
    music Power_Bots_Loop
    img 21459
    with hpunch
    mt "!!!"
    m "Нет!!!"
# Скажи, шлюха! А не то ты станешь плохой шлюхой!
# Да! Да! Плохая шлюха, да!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21460
    with fade
    prisoner1 "Скажи, шлюха! А не то ты станешь плохой шлюхой!"
    img 21461
    with diss
    prisoners "Да! Да! Плохая шлюха! Да!"

# О БОЖЕ!!! Что мне делать?!
    music2 stop
    music Malicious
    img 21462
    with fade
    mt "О БОЖЕ!!! Что мне делать?!"

# Сказать что Моника ждет члены заключенных в своей попе
# Поставить их на место!
    menu:
        "Сказать, что Моника ждет члены заключенных в своей попе.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_12
            return False

# Я... Я жду ваши члены...
# Где?! Где ты ждешь наши члены, шлюха?! Отвечай нам!
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21463
    with fadelong
    m "Я... Я жду Ваши члены..."
    music Villainous_Treachery
    music2 prison_yell_music
    img 21464
    with fade
    prisoner1 "Где?! Где ты ждешь наши члены, шлюха?! Отвечай нам!"

# Я... Я жду ваши члены... в своей попе...
# О БОЖЕ!!!

    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21465
    with fadelong
    m "Я... Я жду Ваши члены... в своей попе..."
    mt "О БОЖЕ!!!"

# Скажи, скажи что ты хочешь, чтобы они поскорее оказались там!
# Скажи это!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21464
    with fade
    prisoner1 "Скажи, скажи что ты хочешь, чтобы они поскорее оказались там!"
    prisoner1 "Скажи это!"

# Как я могу такое сказать?! Но мне не важно что я говорю...
# Все-равно этого никогда не будет... А мне надо выиграть время...
# Всего-лишь время!
    music Malicious
    img 21462
    with fade
    mt "Как я могу такое сказать?! Но мне не важно, что я говорю..."
    mt "Все равно этого никогда не будет... А мне надо выиграть время..."
    mt "Всего лишь время!"

# Я... Я жду ваши члены... в своей попе...
# Я... Я хочу, чтобы они поскорее оказались там...
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21466
    with fadelong
    m "Я... Я жду Ваши члены... в своей попе..."
    m "Я... Я хочу, чтобы они поскорее оказались там..."

# Да, хорошая шлюха! Да! До завтра, шлюха!
# Завтра ты будешь сосать наши члены!
# У всех нас, одновременно!
# Да! Да! Хорошая шлюха!
# Одновременно, сосать, да!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21467
    with fade
    prisoner1 "Да, хорошая шлюха! Да!"
    prisoner1 "До завтра, шлюха!"
    prisoner1 "Завтра ты будешь сосать наши члены!"
    prisoner1 "У всех нас, одновременно!"
    img 21469
    with diss
    prisoners "Да! Да! Хорошая шлюха!"
    prisoners "Одновременно, сосать, Да!"

# НЕТ!!!
# О БОЖЕ!!!
# Я не буду делать этого!!!
    music Power_Bots_Loop
    img 21468
    with hpunch
    m "НЕТ!!!"
    m "О БОЖЕ!!!"
    m "Я не буду делать этого!!!"

# Ты будешь! Иначе ты будешь плохой шлюхой, да!
# Скажи это! Скажи что ты будешь сосать наши члены завтра!
# Скажи! Мы хотим это услышать!
    music Villainous_Treachery
    img 21470
    with fade
    prisoner1 "Ты будешь! Иначе ты будешь плохой шлюхой, Да!"
    prisoner1 "Скажи это! Скажи, что ты будешь сосать наши члены завтра!"
    prisoner1 "Скажи! Мы хотим услышать это!"

# Да! Да!
# Услышать! Да!
    img 21471
    with diss
    prisoners "Да! Да!"
    prisoners "Услышать! Да!"

# О БОЖЕ!
# Что мне делать?!
# Завтра Мистер Маркус примет меня.
#Мне надо сказать что угодно, чтобы они отстали от меня!
    music Malicious
    music2 stop
    img 21472
    with fade
    mt "О БОЖЕ!"
    mt "Что мне делать?!"
    mt "Завтра Мистер Маркус примет меня."
    mt "Мне надо сказать что угодно, чтобы они отстали от меня!"

# Сказать что завтра Моника будет сосать члены заключенных.
# Поставить их на место!
    menu:
        "Сказать, что завтра Моника будет сосать члены заключенных.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_6", False)

            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_13
            return False

# Я... Я буду сосать Ваши члены... Завтра...
# Одновременно! Одновременно все наши члены! Да!
# Я... Я буду сосать завтра все Ваши члены... Одновременно...
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 21473
    with fade
    m "Я... Я буду сосать Ваши члены... Завтра..."
    $ questHelp("marcus_6", True)
    $ questHelp("marcus_8")
    music Villainous_Treachery
    music2 prison_yell_music
    img 21474
    with diss
    prisoner1 "Одновременно! Одновременно все наши члены! Да!"
    music Groove2_85
    img 21475
    with fade
    m "Я... Я буду сосать завтра все Ваши члены... Одновременно..."
    mt "Мерзавцы... Никогда этого не будет!"

# Да! Хорошая шлюха!
# Да!
# Шлюха может отдыхать на сегодня! Да!
# Мы придем к шлюхе завтра! Да!
    music Villainous_Treachery
    prisoner1 "Да! Хорошая шлюха!"
    prisoners "Да!"
    img 21476
    with diss
    prisoner1 "Шлюха может отдыхать на сегодня! Да!"
    prisoners "Мы придем к шлюхе завтра! Да!"
    $ questHelp("marcus_6", True)
    #sound заключенные уходят (топают)
    sound steps_jail


# О Боже! Что я сказала?!
# Но какая разница?!
# Завтра я встречусь с Маркусом и этот кошмар закончится!
# Мне надо спать! Я хочу поскорее уснуть!
    music stop
    music2 stop
    img black_screen
    with diss
    pause 2.0
    music Malicious
    img 21477
    with fadelong
    mt "О Боже! Что Я сказала?!"
    img 21478
    with diss
    mt "!!!"
    mt "Но какая разница?!"
    mt "Завтра я встречусь с Маркусом и это кошмар закончится!"
    mt "Мне надо спать! Я хочу поскорее уснуть!"
    return

label ep28_dialogues_jail10:
# Моника ложится спать.
# Я наговорила кучу ерунды сегодня.
# Но это не важно. Все это не уйдет дальше этих жутких стен.
# А для меня главное - это выбраться отсюда.
# И завтра я добьюсь своей цели!
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music I_Feel_You
    img 21479
    with fadelong
    mt "Я наговорила кучу ерунды сегодня."
    mt "Но это не важно. Все это не уйдет дальше этих жутких стен."
    mt "А для меня главное - это выбраться отсюда."
    mt "И завтра я добьюсь своей цели!"
    return

label ep28_dialogues_jail11:
# Утро
# Мне надо позвать Боба.
# Мне надо встретиться с Мистером Маркусом скорее!
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("День 3")) from _call_textonblack_36
    img black_screen
    with Dissolve(2.0)
    music Malicious
    img 21480
    with fadelong
    mt "Мне надо позвать Боба."
    mt "Мне надо встретиться с Мистером Маркусом скорее!"
    return

label ep28_dialogues_jail12:
# Боб приходит. Чего тебе?!
# Я хочу встретиться с Мистером Маркусом!
# Мистер Маркус сегодня снова занят.
# КАК?! НЕТ!!!
# МИСТЕР МАРКУС ДОЛЖЕН МЕНЯ СЕГОДНЯ ПРИНЯТЬ!
# ПОЖАЛУЙСТА!!!
# МИСТЕР БОБ!!!
    music stop
    music2 stop
    img black_screen
    with diss
    sound man_steps
    pause 2.0
    music Groove2_85
    img 21481
    with fadelong
    overseer "Чего тебе?!"
    m "Я хочу встретиться с Мистером Маркусом!"
    overseer "Мистер Маркус сегодня занят."
    music Power_Bots_Loop
    img 21482
    with hpunch
    m "КАК?! НЕТ!!!"
    m "МИСТЕР МАРКУС ДОЛЖЕН МЕНЯ СЕГОДНЯ ПРИНЯТЬ!"
    m "ПОЖАЛУЙСТА!!!"
    m "МИСТЕР БОБ!!!"

# Мистер Маркус сказал что примет тебя завтра!
# Подожди еще один день!
# НЕТ! МИСТЕР БОБ!
# ВЫ НЕ ПОНИМАЕТЕ! МНЕ НУЖНО ВСТРЕТИТЬСЯ С НИМ СЕГОДНЯ!
# МНЕ НЕЛЬЗЯ ЖДАТЬ ЕЩЕ ОДИН ДЕНЬ!
    music Groove2_85
    img 21483
    with fade
    overseer "Мистер Маркус сказал, что примет тебя завтра!"
    overseer "Подожди еще один день."
    music Power_Bots_Loop
    img 21484
    with diss
    m "НЕТ! МИСТЕР БОБ!"
    m "ВЫ НЕ ПОНИМАЕТЕ! МНЕ НУЖНО ВСТРЕТИТЬСЯ С НИМ СЕГОДНЯ!"
    m "МНЕ НЕЛЬЗЯ ЖДАТЬ ЕЩЕ ОДИН ДЕНЬ!"
# Это меня не касается!
# Ты будешь жрать или нет?!
# Я... Я... Что?
# Я спрашиваю ты будешь жрать?! Или мне уйти?!
# Да, мистер Боб... Спасибо...
    music Groove2_85
    img 21485
    with fade
    overseer "Это меня не касается!"
    overseer "Ты будешь жрать или нет?!"
    img 21486
    with diss
    m "Я... Я... Что?"
    img 21487
    with fade
    overseer "Я спрашиваю ты будешь жрать?! Или мне уйти?"
    m "Да, Мистер Боб... Спасибо..."
    music stop
    img black_screen
    with diss
    sound snd_eating
    pause 2.0
# О БОЖЕ!
# Еще один день!
# Мне надо пораньше лечь спать. Этот день быстро пролетит.
# Еще одна ночь и я встречусь с Мистером Маркусом.
# И все это закончится!
    music Malicious
    img 21488
    with fadelong
    mt "О БОЖЕ!"
    mt "Еще один день!"
    img 21489
    with diss
    mt "Мне надо пораньше лечь спать."
    mt "Этот день быстро пролетит."
    return

label ep28_dialogues_jail13:
# Я лягу спать пораньше...
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music I_Feel_You
    img 21490
    with fadelong
    mt "Я лягу спать пораньше..."
    return
# Моника ложится спать. Просыпается от шума заключенных.

label ep28_dialogues_jail14:
# Шлюха! Шлюха! Мы пришли к тебе!
# Шлюха!
    music stop
    music2 stop
    sound man_steps
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_37
    img black_screen
    with Dissolve(1)
    music2 prison_yell_music
    img 21491
    with fadelong
    prisoners "Шлюха! Шлюха! Мы пришли к тебе!"
    prisoners "Шлюха!"

# О БОЖЕ!!! Я совсем забыла!
# Они снова пришли!
# Я... О БОЖЕ!!! Что я пообещала им вчера?!
# Что же мне делать?!
    music Power_Bots_Loop
    img 21492
    with hpunch
    mt "О БОЖЕ!!! Я совсем забыла!"
    mt "Они снова пришли!"
    mt "Я... О БОЖЕ!!! Что я пообещала им вчера?!"
    mt "Что же мне теперь делать?!"

# Что Вам снова надо?! Зачем Вы снова пришли сюда!
# Уходите!
    music2 stop
    img 21493
    with fade
    m "Что Вам снова надо?! Зачем Вы снова пришли сюда?!"
    m "Уходите!"

# Мы пришли к нашей шлюхе! Да!
# К хорошей шлюхе! Которая будет сосать наши члены сегодня!
# Достают члены
# Да! Да! Сосать!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21494
    with diss
    prisoner1 "Мы пришли к нашей шлюхе! Да!"
    prisoner1 "К хорошей шлюхе! Которая будет сосать наши члены сегодня!"
    # Достают члены
    sound Jump1
    img 21495
    with diss
    prisoners "Да! Да! Сосать!"

# Я не буду делать этого! Никогда, Вы слышите?!
# Ты будешь сосать! Будешь! Иначе ты плохая шлюха!
# Да!
# Ты надоела нам! Если ты будешь плохой шлюхой, мы все расскажем детективу про тебя!
    music2 stop
    music Power_Bots_Loop
    img 21496
    with fade
    m "Я не буду делать этого! Никогда, Вы слышите?!"
    music Villainous_Treachery
    music2 prison_yell_music
    img 21497
    with diss
    prisoner1 "Ты будешь сосать! Будешь! Иначе ты плохая шлюха!"
    prisoners "Да! Будет плохой шлюхой!"
    img 21498
    with diss
    prisoner1 "Ты надоела нам! Если ты будешь плохой шлюхой, мы все расскажем детективу про тебя!"

# НЕТ! Вы не сделаете этого!
    music Malicious
    music2 stop
    img 21499
    with fade
    mt "Тянуть время..."
    mt "Мне просто нужно тянуть время..."
    m "НЕТ! Вы не сделаете этого!"

# Если шлюха будет хорошей, мы не будем этого делать!
# Садись на колени и соси наши члены!
# Будь хорошей шлюхой, jail_name
    music2 prison_yell_music
    music Villainous_Treachery
    img 21498
    with diss
    prisoner1 "Если шлюха будет хорошей, мы не будем этого делать!"
    img 21500
    with diss
    prisoner1 "Садись на колени и соси наши члены!"
    prisoner1 "Будь хорошей шлюхой, [monica_jail_name]."

# НЕТ! Я не буду! Ни за что!!!
    music Power_Bots_Loop
    music2 stop
    img 21501
    with hpunch
    m "НЕТ! Я не буду! Ни за что!!!"
    mt "Боже! Как это мерзко!!!"
    mt "!!!"

# Тогда мы уходим! Позовите детектива, ребята!
# Да, мы пошли звать детектива.
# Плохая шлюха!
    music stop
    img black_screen
    with diss
    pause 1.5
    music2 prison_yell_music
    music Power_Bots_Loop
    img 21502
    with fadelong
    prisoner1 "Тогда мы уходим! Позовите детектива, ребята!"
    prisoners "Да, мы пошли звать детектива."
    prisoners "Плохая шлюха!"

# Уходят

# Нет! Стойте!
# Не делайте этого!
    music2 stop
    img 21503
    with diss
    mt "Что?!"
    mt "!!!"
    mt "Нет-нет! Мне нельзя этого допустить!"
    m "Нет! Стойте!"
    m "Не делайте этого!"

# Мы сделаем это! Ты плохая шлюха!
# Да! Да!
# Мы сделаем это!
    music2 prison_yell_music
    img 21504
    with fade
    prisoner1 "Мы сделаем это! Ты плохая шлюха!"
    prisoners "Да! Да!"
    prisoners "Мы сделаем это!"

# Не делайте!
# Я... Я...
    music2 stop
    img 21505
    with diss
    m "Не делайте!"
    m "Я... Я..."
    mt "!!!"
    mt "Черт! Что 'Я'?.."
    mt "Я не смогу этого сделать! Не смогу!!!"

# Возвращаются

# Ты? Что ты?!
# Мы знаем что ты шлюха!
# Но ты хорошая шлюха или плохая?!
# Отвечай!
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    sound Jump1
    music2 prison_yell_music
    music Villainous_Treachery
    img 21506
    with diss
    prisoner1 "Ты? Что ты?!"
    prisoner1 "Мы знаем что ты шлюха!"
    prisoner1 "Но ты хорошая шлюха или плохая?!"
    prisoner1 "Отвечай!"

# Сделать что они хотят.
# Поставить их на место!
    menu:
        "Сделать, что они хотят.":
            pass
        "Поставить их на место!":
            $ questHelp("marcus_8", False)
            call ep28_dialogues_monica_offending_prisoners() from _call_ep28_dialogues_monica_offending_prisoners_14
            return False

# Я... Я...
# Ну же!
# Я... Я хорошая шлюха...
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21507
    with fadelong
    m "Я... Я..."
    music Villainous_Treachery
    music2 prison_yell_music
    img 21508
    with diss
    prisoner1 "Ну же!"
    music2 stop
    music Hidden_Agenda
    img 21509
    with fade
    m "Я... Я хорошая шлюха..."

# Вставай на колени и соси наши члены!
# Хорошая шлюха обещала сосать их сегодня!
    music Villainous_Treachery
    music2 prison_yell_music
    img 21508
    with diss
    prisoner1 "Снимай свою одежду!"
    img 21510
    with diss
    m "..."
    img 21511
    with fade
    prisoner1 "Давай!"

    music stop
    music2 stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music2 prison_yell_music
    img 21512 # вид одежды
    with fadelong
    w
    music Villainous_Treachery
    img 21513
    with diss
    prisoner1 "Вставай на колени и соси наши члены!"
    prisoner1 "Хорошая шлюха обещала сосать их сегодня!"

# Я...
    music Malicious
    img 21514
    with diss
    m "Я..."

# Всавай на колени!
    music Villainous_Treachery
    img 21515
    prisoner1 "Вставай на колени!"

# Моника встает на колени
    music stop
    music2 stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Malicious
    music2 prison_yell_music
    img 21516
    with fadelong
    m "..."
    mt "Я не смогу... Не смогу..."
    mt "От них воняет... Ужасно!"
    mt "Меня тошнит..."

# Принимай мой член! Давай, скорее!
# А то я сейчас кончу тебе на лицо.
    music Villainous_Treachery
    img 21517
    with fade
    prisoner1 "Принимай мой член! Давай, скорее!"
    prisoner1 "А то я сейчас кончу тебе на лицо. Уже не могу терпеть!"

# Что здесь за беспорядок?! Заходит Боб.
# Боб, мы пришли к нашей шлюхе! Ты обещал, Боб!
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Groove2_85
    img 21518
    with fadelong
    overseer "Что здесь за беспорядок?!"

    music stop
    music2 stop
    img black_screen
    with diss
    #sound заключенные бегут к стене и встают руки за спину
    sound running
    pause 1.0
    music Groove2_85
    img 21519
    with fadelong
    prisoner1 "Боб, мы пришли к нашей шлюхе!"
    prisoner1 "Ты обещал, Боб!"

# Я пущу Вас к ней после того, как она побывает у Мистера Маркуса!
# Но Боб! Мы не занимаемся с ней сексом! Она просто сосет наши члены!
# Она сама хочет этого!
# Сама?
    img 21520
    with diss
    overseer "Я пущу Вас к ней после того, как она побывает у Мистера Маркуса!"
    img 21521
    with fade
    prisoner1 "Но Боб! Мы не занимаемся с ней сексом!"
    prisoner1 "Она просто сосет наши члены. Ничего такого..."
    prisoner1 "Она сама хочет этого!"
    img 21522
    with diss
    overseer "Сама?"
# Да, эта шлюха сама этого хочет!
# Да, шлюха?! Отвечай!
# Я... Я...
# Отвечай, шлюха! Ты знаешь что надо ответить, чтобы быть хорошей шлюхой!

    prisoner1 "Да, эта шлюха сама этого хочет!"
    music Villainous_Treachery
    img 21523
    with fade
    prisoner1 "Да, шлюха?! Отвечай!"
    music Malicious
    img 21524
    with diss
    m "Я... Я..."
# И ты знаешь что будет с плохой шлюхой!
# Ты знаешь это!
# Я... Я...
# Мистер Боб... Я... Их члены...
    music Villainous_Treachery
    img 21525
    with fade
    prisoner1 "И ты знаешь что будет с плохой шлюхой!"
    prisoner1 "Ты знаешь это!"

    music Malicious
    img 21526
    with diss
    m "Я... Я..."
    mt "О БОЖЕ! Если я скажу Бобу правду, то они точно расскажут все детективу!"
    mt "Боба уберут отсюда, а что будет со мной - Я даже боюсь представить!"
# Ну же, шлюха!
# Я хочу их члены... сосать...
# Видишь, Боб?
    img 21527
    with fade
    prisoner1 "Ну же, шлюха!"
    img 21528
    with diss
    m "Я хочу их члены... сосать..."
    music Groove2_85
    img 21529
    with fade
    prisoner1 "Видишь, Боб?"
# Она сама хочет! Открой нам дверь!
# Мы хотим попасть к ней! Это неудобно делать через решетку!
# Наши члены не такие длинные! Нам неудобно, Боб!
# overseer "И что, ты правда сама этого хочешь?"
# Тебя никто не заставлял?
    prisoner1 "Она сама хочет! Открой нам дверь!"
    prisoner1 "Мы хотим попасть к ней! Это неудобно делать через решетку!"
    prisoner1 "Наши члены не настолько длинные...."
    img 21530
    with diss
    prisoner1 "Нам неудобно, Боб!"
    img 21531
    with fade
    overseer "И что, ты правда сама этого хочешь?"
    overseer "Тебя никто не заставлял?"
# Нннет... Мистер Боб...
# Мммменя... Никто... Не заставлял...
# Ну хорошо, я открою. Только давайте быстро! Скоро отбой!
# И у меня начинает болеть голова из-за вас!
    music Malicious
    img 21532
    with diss
    m "Ннннет... Мистер Боб..."
    m "Ммммменя... Никто... Не заставлял..."
    music Groove2_85
    img 21533
    with fade
    overseer "Ну хорошо, я открою. Только давайте быстро! Скоро отбой!"
    overseer "И у меня начинает болеть голова из-за вас!"
# У Вас есть 10 минут!
# Да! Ура! Ребята, залетай!
    img 21534
    with diss
    overseer "У Вас есть 10 минут!"
    music stop
    img black_screen
    with diss
    sound snd_jail_door
    pause 2.0
    music3 Indo_Rock
    img 21535
    with fade
    prisoner1 "Да! Ура! Ребята, залетай!"
    m "О БОЖЕ!"
    mt "НЕТ!!!"
    mt "!!!"
    sound snd_bodyfall
#    music stop
    img black_screen
    with diss
    pause 2.0

# Да, хорошая шлюха! Соси! Соси наши члены!
# Да!
# Давай, да!
# Моника сосет кучу членов.
    img 21536
    with fadelong
    mt "..."
    mt "Как же отвратительно от него воняет!"
    mt "!!!"
    mt "Мне придется сделать ЭТО!"
    mt "10 минут... Мне нужно продержаться всего 10 минут..."
    mt "Это же так мало..."
    prisoner1 "Да, хорошая шлюха! Соси! Соси наши члены!"
    #sound входит член blowjob
    $ renpy.music.set_volume(0.4, delay=1.0, channel='music3')
    sound chavc26
    #sound music начинается чавк-чавк
    music long_chavc4
    img 21537 # входит
    with diss
    mt "Фуууу!"
    mt "!!!"
    mt "Ненавижу!"
    music2 prison_yell_music
    img 21538
    with diss
    w
    music2 stop
    img 21539
    with diss
    prisoner1 "Да!"
    img 21540
    with diss
    w
    img 21541
    with diss
    prisoner1 "Давай, Да!"
    music stop
    sound bulk1
    img 21542 # кончает
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "!!!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner1 "ААааахххх!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
# Моника сосет кучу членов.

# Эй, моя очередь.
# Эй, посторонись, дай мне тоже вставить член ей в ротик.
# Да, какой ротик.
# Как приятно, ребята, да!
    music2 prison_yell_music
    img 21543
    with fade
    prisoner2 "Эй, моя очередь!"
    mt "Еще один!"
    mt "Мне кажется, прошла уже целая вечность! Где этот чертов Боб!"
    mt "Я не хочу делать ЭТО!"
    mt "!!!"
    music2 stop
    img 21544
    with diss
    prisoner2 "Давай! Попробуй моего малыша!"
    #sound входит blowjob
    sound chavc26
    #sound music чав-чавк уже больше и быстрее
    music long_chavc3
    img 21545
    with diss
    m "Ммммпфххххх... Мммммннн..."
    img 21546
    with diss
    w
    img 21547
    with diss
    w
    img 21548
    with diss
    prisoner2 "Я почти все..."
    music stop
    sound bulk1
    img 21549 # кончает
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "Фуууу!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner2 "ААааахххх!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    music2 prison_yell_music
    img 21550
    with fade
    w
    img 21551
    with diss
    mt "Какая мерзость!!!"
    w
    img 21552
    with diss
    prisoner4 "Эй, посторонись, дай мне тоже вставить член ей в ротик."
    mt "!!!"
    music2 stop
    #sound входит blowjob
    sound chavc26
    #sound music чавк-чавк еще сильнее
    music long_chavc9
    img 21553 # Вставляет
    with diss
    w
    mt "Ненавижу их всех!!!"
    img 21554
    with diss
    w
    img 21555
    with diss
    prisoner4 "Да, какой ротик!"
    img 21556
    with diss
    w
    img 21557
    with diss
    prisoner4 "Как приятно, ребята, да!"
    mt "Хочется сжать зубы и посмотреть, как это животное будет корчиться от боли..."
    music2 prison_yell_music
    img 21559
    with fade
    prisoner5 "Продвигайтесь быстрее! Мы тоже ждем!"
    img 21558
    with diss
    w
# ААааахххх!
# Эй! Кончай на нее! Не разбрызгивай на нас!
# Моя очередь!
# ААааааааххх!
    music stop
    music2 stop
    sound bulk1
    img 21560
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner4 "ААааахххх!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    music2 prison_yell_music
    img 21561
    with fade
    prisoner5 "Эй! Кончай на нее! Не разбрызгивай на нас!"
    img 21562
    with diss
    prisoner3 "Эй! Подвинься!"
    mt "Я не могу больше!"
    mt "У меня болит все во рту!"
    mt "!!!"

# Продвигайтесь быстрее! Мы тоже ждем!
# ААааааааххх!
# Следующий!
#    prisoner3 "Эй! Подвинься!"
    img 21563
    with fade
    prisoner3 "Моя очередь!"
    prisoner3 "Кто закончил, отходите в сторону!"
    music2 stop
    #sound входит blowjob
    sound chavc26
    #sound music чавк-чавк очень сильный и быстрый
    music long_chavc8
    img 21564 # вставляет
    with diss
    w
    img 21565
    with diss
    w
    img 21566
    with diss
    mt "!!!"


#    prisoner5 "ААааахххх!"
##    prisoner3 "ААааахххх!"
# Кто закончил, отходите в сторону!
# ААааааааххх!
#    prisoner3 "ААааахххх!"
# Не задерживайте очередь!
# Ну же! Кончай скорее!
# Я почти!
    music2 prison_yell_music
    img 21567
    with fade
    prisoner5 "Не задерживайте очередь!"
    prisoner5 "Ну же! Кончай скорее!"
    img 21568
    with diss
    prisoner3 "Я почти!"
# Давай! Долби ее активнее!
# ААааааааххх!
# Следующий!
    img 21569
    with diss
    prisoner6 "Давай! Долби ее активнее!"
    music2 stop
    music stop
    sound bulk1
    img 21570
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner3 "ААааахххх!"
    mt "КОГДА ВСЕ ЭТО ЗАКОНЧИТСЯ???"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "ФУ-У-У-У!!!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "!!!"
# Эй! Ты куда лезешь!
# Ты после меня!
# ААааааааххх!
    music2 prison_yell_music
    img 21571
    with diss
    m "!!!"
    m "Сволочи, хватит кончать на меня!"
    img 21572
    with fade
    prisoner1 "А куда нам кончать? Нам нельзя пачкать камеру."
    img 21573
    with diss
    m "Куда-нибудь! В унитаз!"

    img 21574
    with fade
    prisoner1 "Кстати! Спасибо что напомнила!"
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    sound snd_man_piss1
    img 21575 # писает
    with fadelong
    prisoner1 "Я весь день терпел..."

    img 21576
    with fade
    prisoner6 "Эй! Ты куда лезешь?!" # Говорит 5-му
    prisoner6 "Ты после меня!"
    music2 stop
    #sound входит blowjob
    sound chavc26
    #sound music чавк-чавк очень сильный
    music long_chavc9
    img 21577 # вставляет
    with diss
    m "!!!"
    img 21578
    with diss
    w
    sound snd_man_piss1b
    img 21579
    with diss
    w
    img 21580
    with diss
    w
    img 21581
    with diss
    w
    img 21582
    with diss
    w
    music stop
    sound bulk1
    img 21583
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner6 "ААааахххх!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
#    prisoner6 "На! Украшу твою мордашку!"
    w
    img 21584
    with diss
    mt "!!!"
    mt "Мои глаза!!!"
    mt "Я не могу открыть их!!!"
    mt "!!!"
    music2 prison_yell_music
    img 21585
    with fade
    prisoner5 "Моя очередь!"

    #sound входит blowjob
    sound chavc26
    #sound music чав-чавк очень сильный и быстрый
    music long_chavc3
    img 21587 # вставляет
    mt "!!!"
    mt "Хватит! Мне больно!"
    img 21588
    with diss
    w
    img 21589
    with diss
    w
    img 21590
    with diss
    w

# Время!
    music2 stop
    music stop
    img 21586
    with hpunch
    overseer "Время!"
# Скорее, скорее!
# Дай мне!
# Я еще не все!
    music2 prison_yell_music
    img 21591
    with diss
    prisoner1 "Скорее, скорее!"
    img 21592
    with diss
    prisoner1 "Дай мне!"
    img 21593
    with diss
    prisoner5 "Я еще не все!"
# Дай я тогда тоже засуну!
# Я должен успеть!
    img 21594
    with diss
    prisoner1 "Дай я тогда тоже засуну! Еще раз!"
    prisoner1 "Я должен успеть!"
# Да, давай, растягивай ей ротик!
# ААааааааххх!
# ААааааааххх!
    music2 stop
    #sound входит blowjob сразу 2, жуткий звук :)
    sound chavc6
    #sound music чав-чавк двойной
    music long_chavc1
    img 21595
    with diss
    mt "БОЖЕ!!!"
    mt "!!!"
    prisoner3 "Да, давай, растягивай ей ротик!"
#    mt "Боже! Я сейчас с ума сойду! Как же больно!!!"
    mt "!!!"
    img 21596
    with diss
    prisoner1 "Смотрите, парни! Наши члены, с трудом, но влезли в ее рот!"
    img 21597
    with diss
    prisoner1 "Может быть у этой шлюхи уже есть большой опыт?"
    img 21598
    with diss
    prisoner3 "Да нет, она неопытная... Но у нее есть задатки, чтобы стать первоклассной шлюхой!"
    music stop
    sound bulk1
    img 21599
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner5 "ААааахххх!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    prisoner1 "ААааахххх!"
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
# Все, брысь отсюда!
    music stop
    music2 stop
    music3 stop
    $ renpy.music.set_volume(1.0, delay=1.0, channel='music3')
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Groove2_85
    music2 prison_yell_music
    img 21600
    with fadelong
    overseer "Все, брысь отсюда!"

    $ questHelp("marcus_8", True)


# О БОЖЕ!!! Что это было...
# У меня сводит челюсть, я не могу пошевелить ей...
# А это что?! # Боб стоит с членом
# Боб?!
    music stop
    music2 stop
    img black_screen
    with diss
    #sound толпа заключенных уходит
    sound steps_jail
    pause 2.0
    if game.extra == True:
        music Malicious
        img 21601
        with fadelong
        w
        img 21602
        with diss
        mt "О БОЖЕ!!! Что это было..."
        img 21603
        with diss
        mt "У меня сводит челюсть, я не могу пошевелить ей..."
        mt "И горло ужасно болит!"
        mt "Мои глаза! Я не могу разлепить их!"
        mt "Я вся в этой мерзкой гадости!!!"
        mt "Что мне делать теперь с челюстью? Я не могу закрыть рот!"
        sound Jump1
        img 21604
        with diss
        mt "Наверное, мне надо помассировать ее..."
        img 21605
        with diss
        mt "Клянусь, больше ни один вонючий отросток никогда не коснется моих губ!"
        sound Jump2
        img 21606
        with hpunch
        mt "А это что?!"
        $ ep28_quests_bob_dick = True
        music Power_Bots_Loop
        img 21607
        with fade
        m "БОБ?! ТЫ?!"
    # Ну ты любишь делать это... Ты сама сказала...
    # И я подумал, что...
    # Уйди отсюда, Боб!
    # Никогда в жизни я не буду этого делать!
        music Groove2_85
        img 21608
        with diss
        overseer "Ну... Ты любишь делать это... Ты сама сказала..."
        overseer "И Я подумал, что..."
        music Power_Bots_Loop
        img 21609
        with fade
        m "Уйди отсюда, Боб!"
        m "Размечтался!"
        m "Никогда этого не будет!"
        # Мерзавцы!
        # Твари!
        # Ладно, ладно, ухожу...
        img 21610
        with diss
        with hpunch
        m "Мерзавцы!"
        with hpunch
        m "Твари!"
        with hpunch
        m "Знали бы Вы кто Я такая!"
        overseer "Ладно, ладно, ухожу..."
        music stop
        img black_screen
        with diss
        sound man_steps
        pause 2.0

# Моника ложится спать...
# Я не могу поверить... Их... Столько...
# Я...
# Как такое могло случиться...
    music Malicious
    img 21611
    with fadelong
    mt "Я не могу поверить... Их... Столько..."
    mt "Я..."
    mt "Как такое могло случиться..."
    mt "Как я согласилась на ЭТО?!"
    music Pyro_Flow
    img 21612
    with diss
    mt "..."
    mt "Я клянусь что уничтожу всех этих ублюдков!"
    mt "Они ответят за все!"
    mt "Они ответят за свой гнусный шантаж!"
    music Hidden_Agenda
    img 21613
    with diss
    mt "..."
    mt "Мне надо умыться..."
    return
# И... Как я выдержала это...
# Мне надо лечь спать...
# Не могу поверить что я решилась на это...
# Как такое могло случиться?
# Мне лучше об этом забыть...
# Я сплю...
label ep28_dialogues_jail15:
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music I_Feel_You
    img 21614
    with fadelong
    mt "И... Как я выдержала это..."
    mt "Мне надо лечь спать..."
    mt "Не могу поверить, что я решилась на это..."
    mt "Может быть, был другой путь?"
    mt "Как такое могло случиться, со мной?"
    img 21615
    with diss
    mt "..."
    mt "Мне лучше об этом забыть..."
    mt "Я сплю..."
    return

# Утро
# Мне надо позвать Боба. Мистер Маркус должен встретиться со мной!
label ep28_dialogues_jail16:
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("День 4")) from _call_textonblack_38
    img black_screen
    with Dissolve(2.0)
    music Power_Bots_Loop
    img 21616
    with fadelong
    mt "Мне надо позвать Боба. Мистер Маркус должен встретиться со мной, наконец!"
    mt "Я не буду оставаться здесь более ни на один день, ни на один час!"
    return
# Мистер Маркус ждет тебя!
# Иди за мной!
# Ура! Наконец-то!
# Наконец-то я покину это жуткое место!
# Наконец-то!
label ep28_dialogues_jail17:
    music stop
    music2 stop
    img black_screen
    with diss
    sound man_steps
    pause 2.0
    music Groove2_85
    img 21617
    with fadelong
    overseer "Мистер Маркус ждет тебя!"
    overseer "Иди за мной!"
    music RnB3_65
    img 21618
    with diss
    m "Ура! Наконец-то!"
    mt "Наконец-то, я покину это жуткое место!"
    mt "Наконец-то!"
    return
# Моника идет вдоль заключенных. Они кричат хорошая шлюха (или молчат)
    # идет если поставила заключенных на место
label ep28_dialogues_jail18:
    $ notif(t_("Моника поставила заключенных на место."))
    sound snd_jail_door
    music stop
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    pause 2.0
    sound man_steps
    music Pyro_Flow
    img 21620
    with fadelong
    mt "Грязные похотливые животные! Фи!"
    sound man_steps
    img 21621
    with diss
    w
    return

label ep28_dialogues_jail19:
    # идет если поддалась
    $ notif(t_("Моника подчинилась заключенным."))
    sound snd_jail_door
    music stop
    img black_screen
    with diss
    pause 1.0
    sound highheels_run2
    pause 2.0
    music Malicious
    music2 prison_yell_music
    sound man_steps
    img 21622
    with fadelong
    mt "Боже! Нет! Только не прикасайтесь ко мне!!!"
    prisoners "Хорошая шлюха!"
    prisoners "Да! Хорошая шлюха!"
    sound man_steps
    img 21623
    with diss
    prisoners "Мы ждем нашу шлюху!"
    prisoners "Хорошая шлюха!"
    music2 stop
    return


label ep28_dialogues_jail1_piss:
    # Моника писает
    music stop
    img black_screen
    with diss
    pause 1.5
    sound snd_piss
    img 21628
    with fadelong
    mt "Мне холодно сидеть на нем..."
    mt "Но я хочу писать..."
    img 21629
    with diss
    mt "Надеюсь, никто не смотрит на меня..."
    return

label ep28_dialogues_jail1_bed:
    mt "Мне надо кого-то позвать!"
    "Я не могу находиться здесь!!!"
    return


label ep28_dialogues_monica_offending_prisoners: # Моника наезжает на заключенных
    music Pyro_Flow
    music2 stop
    img 21307
    with fadelong
    m "Слышите, Вы?!"
    m "Вы сами нарушаете правила!"
    m "Нарушаете тем, что заключаете сделки с надзирателем!"
    m "Гуляете здесь без разрешения администрации."
# И, как к ним будет относиться другой надзиратель. Учитывая что они заложили предыдущего!
# Вы ни о чем с ним не договоритесь! Вы будете гнить в камерах, никогда не выходя из них!
    img 21308
    with diss
    m "И, подумайте! Как к Вам будет относиться другой надзиратель, учитывая что Вы заложили предыдущего!"
    m "Вы ни о чем с ним не договоритесь!"
    img 21309
    with diss
    m "Вы будете гнить в камерах, никогда не выходя из них!"
    m "И будете вспоминать доброго Боба!"
    prisoner "..."
    img 21310
    with fade
    m "Давайте! Зовите сюда детектива! Мне есть что сказать ему!"
# Заключенные боятся
# Говорят что ладно, ладно, мы пошутили.
# Моника говорит что теперь пошли отсюда вон!
# Заключенные уходят
    music Groove2_85
    img 21311
    with diss
    prisoners "Она расскажет?"
    prisoners "Она расскажет про нас?"

    prisoner1 "Ладно, ладно... Мы пошутили..."
    music Pyro_Flow
    img 21312
    with fade
    m "А теперь пошли вон отсюда!"
    m "Животные!"
    music Groove2_85
    img 21313
    with diss
    prisoner1 "Ладно. Мы уходим..."
    return


#
