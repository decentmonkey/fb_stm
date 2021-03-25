default monicaHotelStaffEscort1 = False  # Моника согласилась пойти со служащим за 55 баксов
default monicaHotelStaffEscort2 = False  # Моника согласилась сделать минет служащему
default monicaHotelAdminAgreement1 = False  # Моника согласилась с требованиями админа (начало эскорта)
default monicaHotelAdminAgreement2 = False # Моника согласилась раздеться перед девочками в отеле
default monicaHotelAdminAgreement3 = False # Моника согласилась работать в эскорте

default monica_hotel_name = False


# Моника после недавнего секса в туалете с Филиппом снова приходит в ресторан отеля ЛеГранд на ужин
label ep210_dialogues7_escort_hotel_1:
    # Моника заказывает еду у официантки ( ep26_dialogues4_restaurant - разговор с официанткой и заказ еды)
    # пока ждет, когда принесут ее заказ, сидит на стуле с задумчивым видом
    music Poppers_and_Prosecco
    img 22983
    with fadelong
    mt "Надеюсь, я не увижу этого извращенца Филиппа сегодня..."
    mt "Это было ужасно!"
    mt "Как он посмел так со мной обращаться?!"
    mt "Сволочь!"
    mt "Почему меня, такую добрую и красивую женщину, окружают одни подлецы?!"
    # ее мысли прерывает мужской голос
    img 22984
    with fade
    hotel_staff "Мэм... Добрый вечер, Мэм..."
    # Моника смотрит на него вопросительно, тот стоит, смущаясь
    m "Что?"
    # если не было сцены в туалете с Филиппом и со служащим отеля
    mt "Что могло понадобиться этому неудачнику от меня?!"

    # если была сцена в туалете
    if monicaMadeBlowjobToPhilip == True:
        music Pyro_Flow
        img 22985
        with diss
        mt "Я помню этого неудачника!"
        #
        $ notif(t_("Моника делала минет Филиппу в туалете"))
        #
        mt "Это он тогда был в туалете, когда я..."
        mt "Когда мерзавец Филипп заставил меня..."
        mt "Делать всякие его извращенские гадости!"
        #

    music Groove2_85
    img 22986
    with fade
    hotel_staff "Один наш очень уважаемый клиент сказал мне, что..."
    hotel_staff "..."
    m "Что?"
    img 22987
    with diss
    hotel_staff "Кхм... Что я могу договориться и..."
    hotel_staff "Вам не нужно будет оплачивать Ваш ужин, Мэм."
    img 22988
    with fade
    m "???" # удивленно
    m "Ужин за счет ресторана?"
    img 22989
    with diss
    mt "Может быть, кто-то из моих поклонников решил таким образом сделать мне приятное?"
    mt "Тогда почему этот никчемный представитель обслуживающего персонала мне об этом сообщает?"
    mt "А не администратор или, хотя бы, официант?"
    mt "Странно это все..."
    m "..."
    img 22990
    with fade
    hotel_staff "Так Вы позволите, Мэм?"
    m "Что позволю?"
    # парень еще больше смутившись
    img 22991
    with diss
    hotel_staff "..."
    hotel_staff "Мистер Филипп сказал мне, что если я... Кхм..."
    music Pyro_Flow
    img 22992
    with fade
    mt "!!!"
    music Groove2_85
    img 22993
    with diss
    hotel_staff "Если я договорюсь, что Ваш ужин будет бесплатным для Вас, то..."
    hotel_staff "Тогда вы пойдете со мной. И за 50 долларов проведете со мной время..."
    hotel_staff "В каком-нибудь уединенном месте."
    hotel_staff "Я знаю одно такое место, Мэм."
    # Моника в шоке
    music Power_Bots_Loop
    img 22994
    with hpunch
    m "ЧТО???"
    m "Филипп?!"
    music Groove2_85
    img 22995
    with fade
    hotel_staff "Да, Мэм."
    mt "!!!"
    $ menu_corruption = [0, monicaHotelStaffBlowjobCorruption1]
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            music Power_Bots_Loop
            img 22996
            with hpunch
            m "Я поверить не могу!"
            m "Халдей, как ты смеешь предлагать мне подобное?!"
            m "Как ты вообще посмел подойти к МОЕМУ столику?!"
            m "И заговорить со МНОЙ?!"
            m "!!!"
            img 22997
            with fade
            m "Никчемный неудачник!"
            m "Еще слово - и я сделаю так. Что тебя сегодня же вышвырнут с этой работы!!!"
            m "Пошел вон отсюда!!!"
            m "!!!"
            # Моника зло на него смотрит, тот вконец смутившись, уходит
            return False
        "50 долларов?!":
            $ monicaHotelStaffEscort1 = True # Моника согласилась пойти со служащим за 55 баксов
            pass
    # Моника возмущенно спрашивает

    m "50 долларов?!"
    music Pyro_Flow
    img 22998
    with diss
    mt "Мало того, что этот мерзавец сказал этому неудачнику..."
    mt "Что можно купить меня..."
    mt "Так еще и за 50 долларов!!!"
    img 22999
    with fade
    m "!!!"
    m "За 50 долларов ты можешь пойти и сам с собой провести время!"
    music Groove2_85
    img 23000
    with diss
    hotel_staff "Мэм, но ведь... Помимо этих 50 долларов..."
    hotel_staff "Вам не нужно будет оплачивать Ваш чек."
    img 23001
    with fade
    m "И что?!"
    m "Ужин я и сама могу оплатить!"
    img 23002
    with diss
    mt "Хотя ужинать здесь чертовски дорого для меня сейчас..."
    img 23003
    with fade
    hotel_staff "Я готов дать вам 55 долларов, Мэм."
    hotel_staff "Извините, но у меня просто больше нет денег."
    hotel_staff "55 долларов и бесплатный ужин."
    # Моника зло смотрит на него
    img 23004
    with diss
    mt "Это все отвратительно и мерзко!"
    mt "С другой стороны... 55 долларов... Они не будут лишними."
    mt "А если кто-нибудь узнает?!"
    img 23005
    with fade
    m "..."
    m "Я не могу согласиться на такое..."
    img 23006
    with diss
    hotel_staff "Мэм, Вы можете не переживать. Об этом никто не узнает."
    # Моника молчит и смотрит на него с подозрением
    img 23007
    with diss
    mt "Черт! Мне действительно нужны эти деньги..."
    mt "Я могу пригрозить этому неудачнику увольнением, если он кому-то расскажет..."
    mt "Тогда он испугается и об этом никто никогда не узнает."
    mt "Зато у меня прибавится 55 долларов. Плюс бесплатный ужин."
    mt "И я не собираюсь делать ничего из такого, что требовал Филипп от меня..."
    mt "..."
    # говорит служащему с угрозой

    music Pyro_Flow
    img 23008
    with fade
    m "Ты пожалеешь, если расскажешь об этом хоть одной живой душе!"
    m "Я сделаю так, что тебя выкинут с работы!"
    if monicaWorkingAsDishwasher == True:
        m "И ты после этого не сможешь устроиться на работу даже..."
        # если работала в пабе посудомойщицей
        #
        $ notif(t_("Моника работает посудомойщицей в Shiny Hole"))
        #
        m "Даже посудомойщиком в какой-нибудь грязной дыре в трущобах!"


    img 23009
    with diss
    m "Думаю, ты догадываешься о том..."
    m "Что у меня много знакомых, которые легко смогут это устроить..."
    m "Я большой и влиятельный человек в этом городе!"
    music Groove2_85
    img 23010
    with fade
    hotel_staff "Конечно, Мэм! Я никому не скажу, Мэм!"
    hotel_staff "Сотрудникам отеля запрещено пользоваться услугами проституток. За это могут уволить..."
    # Моника возмущенно
    music Power_Bots_Loop
    img 23011
    with diss
    m "Проституток?!"
    m "!!!"
    m "По-твоему, я проститутка?!"
    # парень испугавшись, что сморозил что-то не то
    music Groove2_85
    img 23012
    with fade
    hotel_staff "Нет, Мэм! Конечно, нет!!!"
    hotel_staff "Просто..."
    hotel_staff "Никто из руководства разбираться не будет."
    hotel_staff "Меня просто уволят и все."
    # Моника грозно смотрит на него
    img 23013
    with diss
    m "Что за уединенное место?"
    m "..."
    m "Если это какой-то туалет, то даже не думай!"
    # парень радостно
    hotel_staff "Мэм, я взял ключи от пустого роскошного номера..."
    hotel_staff "Мы можем пройти туда незаметно. Нас никто не увидит..."
    # Моника задумчиво смотрит на него
    img 23014
    with fade
    mt "Хм... В таком случае..."
    mt "Минимален риск того, что меня кто-нибудь увидит и..."
    mt "Догадается, что я оказала услугу за деньги этому неудачнику."
    m "..."
    img 23015
    with diss
    hotel_staff "..."
    hotel_staff "Мэм? Могу я Вас пригласить в этот номер?"
    # Моника бросает на него еще один грозный взгляд
    music Pyro_Flow
    img 23016
    with fade
    m "Я тебя предупредила, если кто-нибудь узнает..."
    m "!!!"
    music Groove2_85
    img 23017
    with diss
    hotel_staff "Не переживайте, Мэм. Об этом никто никогда не узнает."
    hotel_staff "Пойдемте, Мэм?"
    music stop
    img black_screen
    with diss
    pause 2.0
    music Poppers_and_Prosecco
    # Моника встает и идет за служащим
    img 23018
    with fadelong
    sound highheels_short_walk
    w
    return

# Моника со служащим заходит в служебный коридор отеля
label ep210_dialogues7_escort_hotel_2:
    # Моника оглядывается с отвращением
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Минуту спустя...")) from _call_textonblack_77
    img black_screen
    sound highheels_short_walk
    with Dissolve(2.0)
    music Groove2_85
    music Pyro_Flow
    img 16256
    with fadelong
    m "Это и есть твое уединенное место?!"
    m "Это что вообще?! Служебный коридор?!"
    img 16257
    with fade
    m "!!!"
    m "Ты же говорил, что у тебя есть ключи от номера..."
    # служащий, смущаясь
    music Groove2_85
    img 16258
    with diss
    hotel_staff "Это у мистера Филиппа есть деньги на номер в отеле."
    hotel_staff "Он водит в специальные номера всех девушек, которые стоят больше $ 100."
    hotel_staff "А я всего лишь служащий здесь и у меня нет столько денег."
    img 16259
    with diss
    hotel_staff "Если бы я сразу сказал, что это обычный коридор..."
    hotel_staff "То Вы не согласились бы, Мэм."
    hotel_staff "Однако, прошу Вас, поверьте! Здесь никто никогда не ходит!"
    # Моника оглядывается, при этом думает
    img 16260
    with fade
    mt "У этого мерзавца Филиппа совести и денег хватает только на грязный туалет!"
    mt "Сволочь! Наговорил этому неудачнику непонятно что про меня!!!"
    mt "..."
    music Pyro_Flow
    img 16261
    with diss
    mt "Стоп... Он водит в номера только тех, кто стоит дороже $ 100???"
    mt "Но Я... Вот сволочь!!!"
    mt "Ненавижу его!"
    music Groove2_85
    img 16262
    with fade
    hotel_staff "Кхм..." # Моника смотрит на него
    hotel_staff "Мэм, мне очень хотелось бы, чтобы Вы..."
    hotel_staff "Поработали своим ротиком..." # очень смущается

    # если Халдей имел blowjob с Моникой
    if monicaMadeBlowjobToHotelStaff == True:
        img 16263
        with diss
        hotel_staff "У Вас очень удобный для члена ротик..."
        #
        $ notif(t_("Моника по приказу Филиппа делала служащему отеля минет в туалете"))
        #
        hotel_staff "Мне в прошлый раз очень понравилось..."
        hotel_staff "И мне хочется повторить..."

    if monicaMadeBlowjobToPhilip == True and hotelStaffOffended1 == False:
        # Моника хорошо относилась к Халдею и он ушел, не став оставаться на сцену
        img 16263
        with diss
        hotel_staff "У Вас очень удобный для члена ротик..."
        #
        $ notif(t_("Моника была вежлива со служащим отеля и он не остался в туалете, как предлагал ему Филипп."))
        #
        music Power_Bots_Loop
        # Моника возмущенно
        img 16264
        with hpunch
        m "Что?!"
        m "Да как ты смеешь так со мной говорить?!"
        m "!!!"
        music Groove2_85
        img 16265
        with fade
        hotel_staff "Но, Мэм..."
        hotel_staff "Так сказал мистер Филипп. А еще он сказал, что Вы согласитесь..."
        hotel_staff "Я отказался от Вашего предложения в прошлый раз..."
        img 16266
        with diss
        hotel_staff "Но потом жалел об этом. Я... Я передумал."
        hotel_staff "И хочу, чтобы Вы сделали это, Мэм..."
        mt "Этот неудачник Филипп еще пожалеет об этом!"
        #

    img 16267
    with diss
    mt "!!!"
    $ menu_corruption = [0, monicaHotelStaffBlowjobCorruption2]
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            music Power_Bots_Loop
            img 16268
            with fade
            m "Как ты смеешь предлагать мне подобное?!"
            m "!!!"
            m "Никчемный неудачник!"
            sound highheels_short_walk
            img 16269
            with diss
            m "Оставь себе свои 55 долларов и развлекай себя сам!"
            m "Я ни за что не стану делать этого!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Сделать ему минет.":
            $ monicaHotelStaffEscort2 = True # Моника согласилась сделать минет служащему
            pass
    # служащий мнется и стесняется
    img 16270
    with fade
    hotel_staff "Мэм, простите, что я говорю что-то не так..."
    hotel_staff "Просто я очень... Стесняюсь... И никак не хотел Вас обидеть."
    hotel_staff "..."
    music Pyro_Flow
    img 16271
    with diss
    m "Ну и отлично! Тогда я пошла."
    img 16272
    with diss
    mt "Достаточно и того, что мне не нужно оплачивать чек."
    music Groove2_85
    img 16273
    with fade
    hotel_staff "Мэм, в таком случае. Я вынужден буду сообщить охране, что Вы не оплатили свой чек."
    # при этом он снимает штаны и смотрит на нее выжидающе
    music Pyro_Flow
    img 16274
    with diss
    m "Никчемный сотрудник никчемного отеля!"
    sound snd_fabric1
    img 16275
    with fade
    hotel_staff "Мэм, простите, но я жду, когда Вы начнете..."
    music Pyro_Flow
    img 16276
    with diss
    mt "Черт! И зачем я только согласилась?!"
    # Моника подходит к нему, смотрит на него
    sound highheels_short_walk
    img 16277
    with fade
    mt "Моника, неужели ты сейчас сделаешь это?!"
    mt "Но ведь 55 долларов не будут лишними..."
    img 16278
    with diss
    mt "Да и я уже свыклась с мыслью, что мне не надо платить за счет в ресторане..."
    mt "..."
    mt "К черту! Все-равно об этом никто не узнает..."
    img 16279
    with diss
    mt "А я в такой ситуации, когда приходится идти на жертвы..."
    mt "Хотя я никогда не предполагала, что жертвой будет необходимость трогать член какого-то халдея..."
    mt "Моими восхитительными губами... О БОЖЕ!!!"
    music Groove2_85
    img 16280
    with fade
    hotel_staff "Мэм... Простите... Я жду..."
    hotel_staff "Мне надо скорее закончить, ведь меня ждут важные дела..."
    hotel_staff "В отеле много гостей и мне надо предложить каждому отести его одежду в гардероб..."
    img 16281
    with diss
    mt "Это... Важные дела?!"
    mt "Он считает это важнее того, что перед ним стою Я?!"
    img 16282
    with fade
    hotel_staff "Мэм. Если Вы не решитесь, то я вынужден буду уйти."
    hotel_staff "А Вы - платить за счет в ресторане..."
    mt "!!!"
    # опускается перед ним на колени и берет его член в рот, начинает делать ему минет
    music stop
    img black_screen
    with diss
    pause 1.5
    sound chpok6
    $ add_corruption(monicaHotelStaffBlowjobCorruptionEarn, "hotelstaff_blowjob1")
    pause 1.0
    music2 Loved_Up2
    img 16283
    with fadelong
    hotel_staff "ОООООО!!!"

    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_1 = Movie(play="video/v_Monica_Helper_Blowjob_2_1.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16284
    with fade
    hotel_staff "Какой каааайф!"
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_2 = Movie(play="video/v_Monica_Helper_Blowjob_2_2.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 16285
    with diss
    hotel_staff "ААААААХ! О, Мэм, сделайте так еще раз!"
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_3 = Movie(play="video/v_Monica_Helper_Blowjob_2_3.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16286
    with fade
    hotel_staff "Да, еще-еще!"
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_4 = Movie(play="video/v_Monica_Helper_Blowjob_2_4.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    img 16287
    with diss
    hotel_staff "МММММММ!"
    if game.extra == True:
        music stop
        img black_screen
        with diss
        stop music
        $ renpy.music.set_volume(0.5, 0.5, channel="music2")
        play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
        scene black
        image videov_Monica_Helper_Blowjob_2_5 = Movie(play="video/v_Monica_Helper_Blowjob_2_5.mkv", fps=30)
        show videov_Monica_Helper_Blowjob_2_5
        with fade
        wclean
        stop music
        $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.333333333333333) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_2_1.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_2_6 = Movie(play="video/v_Monica_Helper_Blowjob_2_6.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_2_6
    with fade
    wclean
    stop music
    music stop
    music2 stop
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    # заходит китаянка-админ, грозно смотрит на служащего
    sound plastinka1b
    music stop
    music Villainous_Treachery
    img 16288
    with hpunch
    reception "Ага!!! Я так и знала!!!"
    reception "Тебе нельзя пользоваться услугами нелегальных шлюх!"
    sound Jump2
    img 16289
    with hpunch
    hotel_staff "А... Что... Нет-нет!"
    hotel_staff "Я не..."
    sound snd_runaway
    img 16290
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Pyro_Flow
    # не договаривает, убегает, на ходу натягивая штаны
    # админ смотрит теперь на Монику, та испугана
    img 16291
    with fadelong
    reception "И кто посмел оказывать этому халдею такие услуги?!"
    reception "Ага! Я так и знала, что это ты, шлюха!"
    img 16292
    with fade
    reception "Еще раз тут появишься - сдам тебя полиции!!!"
    reception "А сейчас быстро пошла отсюда, пока я не позвала охрану!"
    # Моника смотрит на нее зло и уходит (вытирая рот)
    img 16293
    with diss
    mt "!!!"
    return True

# Моника, выйдя из отеля ЛеГранд после того, как делала минет служащему
label ep210_dialogues7_escort_hotel_3:
    # не рендерить!
    mt "Какой кошмар!!!"
    mt "Моника, ты делала минет какому-то служащему отеля!"
    mt "Неуверенному в себе неудачнику!"
    mt "И этот никчемный администратор все увидела!!!"
    mt "!!!"
    mt "Что же мне теперь делать?!"
    mt "Она подумала, что я проститутка! Но ведь это не так! (хмык)"
    mt "..."
    mt "С другой стороны..."
    mt "Какая мне разница, что думает какая-то там никчемная администраторша?"
    mt "Бесполезная!"
    mt "Ее мнение для меня ничего не значит!"
    return

# Моника, выйдя из отеля ЛеГранд после того, как отказала служащему
label ep210_dialogues7_escort_hotel_4:
    # не рендерить!
    mt "Никчемный сотрудник никчемного отеля!"
    mt "Как он мог предлагать мне такую мерзость?!"
    mt "Неужели он думал, что я, Моника Бакфетт, соглашусь на подобное?! Фи!"
    return

# Моника, выйдя из отеля ЛеГранд, хочет снова зайти в него
label ep210_dialogues7_escort_hotel_5:
    # не рендерить!
    mt "Я не хочу больше возвращаться в этот никчемный ресторан!"
    mt "По крайней мере, не сегодня..."
    return False

# меню согласиться с админом или отказаться в диалоге у ресепшена, меню включено в диалог ниже, повторяется в нем несколько раз
label ep210_dialogues7_escort_hotel_5_1:
    # Моника высокомерно
    music Pyro_Flow
    img 20411
    with fade
    m "Да мне плевать, что ты там думаешь!"
    m "Твое мнение для меня ничего не значит!"
    m "Стоит тут какая-то ничегонезначащая низкоквалифицированная служащая!"
    img 20397
    with diss
    m "Какого-то второсортного отеля!"
    m "Никчемная! Бесполезная!"
    m "И пытается строить из себя тут главную! Это смешно!"
    # Моника зло на нее смотрит и уходит
    sound highheels_short_walk
    img 20413
    with fade
    reception "Всегда рады видеть Вас в нашем отеле!" # Монике вслед
    # Моника поворачивает, бросает злобный взгляд
    m "Сучка!!!"
    # уходит
    return

# Моника снова приходит в ресторан после того, как делала минет сотруднику
label ep210_dialogues7_escort_hotel_6:
    # Моника хочет пройти мимо ресепшена
    music Groove2_85
    img 20391
    with fadelong
    sound highheels_short_walk
    mt "Мне нужно просто быстро пройти. Может, эта сучка меня не заметит."
    # китаянка на ресепшене смотрит на нее подозрительно
    img 20414
    with hpunch
    sound Jump1
    reception "Это снова ты?! Иди отсюда!"
    reception "Я знаю, что ты сюда пришла заниматься проституцией."
    reception "Нелегально этого делать нельзя!"
    # Моника в растерянности
    img 20402
    with diss
    m "Я пришла в ресторан, просто поужинать."
    m "Что мне сделать, чтоб ты меня пропустила?"
    img 20398
    with fade
    reception "Сначала нужно прекратить притворяться какой-то там леди."
    reception "И сказать мне, кто ты на самом деле!"
    music Pyro_Flow
    img 20397
    with diss
    m "Я на самом деле леди!"
    m "Я одна из самых богатых и влиятельных женщин этого города!"
    # администратор с насмешкой
    music Groove2_85
    img 20399
    with fade
    reception "Влиятельная женщина? Которая за деньги сосет член в коридоре у служащего отеля?"
    music Hidden_Agenda
    img 16294
    with diss
    mt "Черт!!!"
    mt "!!!"
    mt "Что же мне придумать?!"
    # Гордо вскидывает голову
    music Pyro_Flow
    img 16295
    with fade
    m "!!!"
    m "Я делала это не за деньги! Это мои личные отношения! И это тебя не должно касаться!"
    # админ с неприятной ухмылкой
    music Groove2_85
    img 16296
    with diss
    reception "Да? А служащий признался, что ты делала это за деньги."
    reception "Так что, про личные отношения расскажи кому-нибудь другому..."
    mt "!!!"
    img 20403
    with fade
    reception "Неужели ты думала, что я поверю в такую чушь?"
    reception "Если хочешь заниматься этим здесь, то можешь это делать..."
    reception "Но только легально."
    img 20404
    with diss
    mt "!!!"

    $ menu_corruption = [0, monicaReceptionConversationCorruption1]
    menu:
        "Пошла она к черту!":
            call ep210_dialogues7_escort_hotel_5_1() from _call_ep210_dialogues7_escort_hotel_5_1
            return False
        "Сказать то, что требует администратор.":
            $ monicaHotelAdminAgreement1 = True # # Моника согласилась с требованиями админа (начало эскорта)
            pass


    # Моника пристально смотрит на админа
    music Groove2_85
    img 16297
    with fade
    mt "Мне надо притвориться, что мне это интересно."
    mt "Иначе эта сучка не пустит меня в ресторан."
    music Hidden_Agenda
    img 20395
    with diss
    m "..."
    m "Я поняла. Что ты хочешь от меня услышать?"

    #### при повторном диалоге, если Моника в прошлый раз ушла, диалог можно начать отсюда

    # админ строго
    img 16298
    with fade
    reception "Ты должна признаться, что ты шлюха."
    reception "Которая ходит сюда, чтобы заниматься сексом за деньги."
    reception "С уважаемыми посетителями нашего дорогого отеля."
    music Power_Bots_Loop
    img 20400
    with diss
    mt "!!!"
    music Groove2_85
    img 16299
    with fade
    reception "Я могу понять тебя..."
    mt "???"
    img 20399
    with diss
    reception "Ты ходишь пешком, а значит обслуживаешь клиентов на улице."
    reception "И естественно, что ты хочешь обслуживать более респектабельных и богатых клиентов."
    reception "Которых можно найти только здесь, а не на улице."
    reception "В принципе, по внешнему виду ты подходишь нам..."
    img 20408
    with fade
    reception "Но для того, чтобы работать в нашем престижном месте, тебе нужно соблюдать правила."
    reception "И делиться заработанными деньгами с администрацией."
    reception "И не строить из себя какую-то леди!"
    music Pyro_Flow
    img 20401
    with diss
    m "Но я леди..."
    reception "Смотрю, ты снова за свое..."
    reception "Можешь идти отсюда!"

    $ menu_corruption = [0, monicaReceptionConversationCorruption2]
    menu:
        "Пошла она к черту!":
            call ep210_dialogues7_escort_hotel_5_1() from _call_ep210_dialogues7_escort_hotel_5_1_1
            return False
        "Сказать то, что требует администратор.":
            $ monicaHotelAdminAgreement1 = True # # Моника согласилась с требованиями админа (начало эскорта)
            pass

    music Hidden_Agenda
    img 16300
    with fade
    mt "Черт! Придется сказать этой сучке, что она требует!"
    img 16301
    with diss
    m "..."
    m "Да... Я пришла, чтобы заработать денег..."
    music Groove2_85
    reception "И? Ты леди?"
    music Hidden_Agenda
    img 16302
    with fade
    m "Нет..."
    img 16303
    with diss
    reception "А кто ты?"
    mt "!!!"

    $ menu_corruption = [0, monicaReceptionConversationCorruption3]
    menu:
        "Пошла она к черту!":
            call ep210_dialogues7_escort_hotel_5_1() from _call_ep210_dialogues7_escort_hotel_5_1_2
            return False
        "Сказать то, что требует администратор.":
            $ monicaHotelAdminAgreement1 = True # # Моника согласилась с требованиями админа (начало эскорта)
            pass

    music Hidden_Agenda
    img 16304
    with fade
    m "Да... Я... Я... Шлюха..."
    music Groove2_85
    img 16305
    with diss
    reception "Ты признаешь, что врала, что просто ужинаешь в ресторане?"
    reception "А сама пыталась заработать деньги..."
    reception "Осуществляя незаконные услуги сексуального характера. Нелегально."
    m "..."

    $ menu_corruption = [0, monicaReceptionConversationCorruption4]
    menu:
        "Пошла она к черту!":
            call ep210_dialogues7_escort_hotel_5_1() from _call_ep210_dialogues7_escort_hotel_5_1_3
            return False
        "Сказать то, что требует администратор.":
            $ monicaHotelAdminAgreement1 = True # # Моника согласилась с требованиями админа (начало эскорта)
            pass

    music Hidden_Agenda
    img 16306
    with fade
    m "Да, признаю."
    music Groove2_85
    img 16308
    with diss
    reception "В тот раз... Когда ты пришла сюда с целью снять номер..."
    reception "И врала что-то про потеряный багаж, про забытую сумочку в такси..."
    reception "Твоя истинная цель была - продать свое тело кому-то из постояльцев отеля?"
    music Hidden_Agenda
    img 16309
    with fade
    m "Да..."
    img 16310
    with diss
    reception "Что 'да'? Отвечай более развернуто!"
    music Power_Bots_Loop
    img 16294
    with fade
    mt "Ненавижу эту сучку!"

    $ menu_corruption = [0, monicaReceptionConversationCorruption5]
    menu:
        "Пошла она к черту!":
            call ep210_dialogues7_escort_hotel_5_1() from _call_ep210_dialogues7_escort_hotel_5_1_4
            return False
        "Сказать то, что требует администратор.":
            $ monicaHotelAdminAgreement1 = True # # Моника согласилась с требованиями админа (начало эскорта)
            pass

    music Hidden_Agenda
    img 16311
    with fade
    m "Да... Я пришла тогда, чтобы... Продать свое тело."
    # админ довольна, Моника стоит растерянная
    music Groove2_85
    img 16312
    with diss
    reception "Я наконец-то вывела тебя на чистую воду!"
    reception "Отныне, если ты хочешь посещать этот отель..."
    reception "Ты можешь это делать только в качестве девушки по вызову."
    img 16307
    with fade
    reception "Которая официально работает на администрацию отеля."
    reception "Ты же об этом меня хочешь попросить?"
    img 16313
    with diss
    m "..."

    $ menu_corruption = [0, monicaReceptionConversationCorruption6]
    menu:
        "Пошла она к черту!":
            call ep210_dialogues7_escort_hotel_5_1() from _call_ep210_dialogues7_escort_hotel_5_1_5
            return False
        "Сказать то, что требует администратор.":
            $ monicaHotelAdminAgreement1 = True # # Моника согласилась с требованиями админа (начало эскорта)
            pass

    music Hidden_Agenda
    m "Да, я хочу устроиться сюда на работу."
    # админ строго
    music Groove2_85
    img 16314
    with fade
    reception "Наши клиенты очень респектабельны... Поэтому наши девочки должны быть высшего качества."
    reception "Я должна быть уверена, что ты подходишь."
    reception "Надеюсь, у тебя нет проблем с тем, чтобы доказать свою пригодность?"
    img 16315
    with diss
    m "..."
    m "Я готова доказать свою пригодность к этой работе..."
    img 16316
    with fade
    sound highheels_short_walk
    reception "Пошли за мной."
    # Моника в растерянности
    music Hidden_Agenda
    img 16317
    with diss
    mt "Какой кошмар!!!"
    mt "Мне предложили работать шлюхой в отеле!"
    mt "Моника, до чего ты докатилась?!"
    mt "..."
#    img 16318
#    with fade
    mt "С другой стороны..."
    mt "Это хорошая возможность быстро заработать неплохие деньги."
    mt "Но черт! Неужели я смогу работать здесь?!"
    # админ уходит, Моника идет за ней
    return

# Моника с админом в служебном коридоре отеля
label ep210_dialogues7_escort_hotel_7:
    # в коридоре стоят или сидят все девочки, их четверо, Моника с китаянкой стоят перед ними
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("5 минут спустя...")) from _call_textonblack_78
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 16321
    with fadelong
    sound highheels_short_walk
    w
    img 16322
    with fade
    reception "У нас тут дружный коллектив."
    reception "Поэтому все девочки должны одобрить твою кандидатуру."
    img 16323
    with diss
    girl_1 "А, это она... Я тут раньше ее видела..." # брюнетка, каре с челкой - смотрит нагло
    img 16324
    with fade
    girl_2 "Я так и знала, что она не просто посетитель, а работает здесь..." # рыжая с каре - равнодушно
    img 16325
    with diss
    girl_3 "Она и правда тут работала?!" # шатенка с хвостом - удивляется
    # girl_4 - брюнетка с длинными волосами, молча смотрит надменно
    img 16326
    with fade
    reception "Да, девочки. Я вывела ее на чистую воду."
    reception "Она пыталась отобрать у вас клиентов."
    img 16327
    with diss
    reception "Теперь она хочет стать одной из вас."
    reception "Подходит она или нет? Как вы считаете?"
    # Моника спрашивает у китаянки
    img 16328
    with fade
    m "Эти девушки что, все работают здесь?"
    img 16329
    with diss
    reception "Да. И работают они легально."
    reception "В отличие от тебя!"
    img 16330
    with fade
    mt "..."
    mt "Черт! По-моему, они не очень дружелюбно настроены..."
    # девочки начинают возмущаться
    music Groove2_85
    img 16331
    with diss
    girl_4 "Нас и так много..."
    girl_4 "Зачем нам еще одна? Еще и такая?" # надменно
    img 16332
    with fade
    girl_1 "Согласна. Она пыталась отнять у нас наш заработок!" # критикуя
    girl_3 "Да ладно. Пусть разденется. Давайте посмотрим сначала на нее." # с любобытством
    girl_1 "Да. Вдруг у нее жирная задница?"
    music Power_Bots_Loop
    img 16333
    with diss
    mt "!!!"
    mt "На свою задницу посмотрела бы!"
    mt "Сучка!"
    music Groove2_85
    img 16334
    with diss
    reception "Да. Давай, раздевайся!"
    mt "???"
    $ menu_corruption = [0, monicaReceptionConversationCorruption7]
    menu:
        "Что за бред?! Я не собираюсь раздеваться!":
            # Моника высокомерно
            music Pyro_Flow
            img 16335
            with fade
            m "Ты сейчас серьезно?!"
            m "Я должна раздеться, чтобы эти..."
            m "Эти девушки..."
            m "Решали, подойду я для работы или нет?!"
            m "!!!"
            img 16336
            with diss
            m "Я!"
            m "Не собираюсь!"
            m "Раздеваться перед вами!"
            m "К черту ваш второсортный отель и ваши правила!"
            img 16337
            with fade
            m "В отличие от вас всех я умная..."
            m "И легко найду другой способ заработать деньги!"
            # Моника зло на нее смотрит и уходит
            img 16338
            with diss
            reception "Посмотрим, как много ты заработаешь..." # ехидно
            reception "На нищих с улицы!"
            sound highheels_short_walk
            img 16339
            with fade
            reception "Когда в кармане не останется ни цента..."
            reception "Ты знаешь, к кому обращаться." # Монике вслед
            # Моника поворачивает, бросает злобный взгляд
            m "Сучка!!!"
            # уходит
            return False
        "Раздеться.":
            $ monicaHotelAdminAgreement2 = True # Моника согласилась раздеться перед девочками в отеле
            pass
    # Моника раздевается и стоит перед девочками голая, прикрываясь
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 16340
    with fadelong
    w
    img 16341
    with fade
    mt "!!!"
    mt "Эти сучки осматривают меня, как товар."
    mt "Как это мерзко!"
    # девочки ее обсуждают
    music Groove2_85
    img 16342
    with diss
    girl_2 "А она красивая..." # равнодушно
    girl_1 "Да ну! А вдруг у нее задница жирная?" # критикуя
    girl_3 "А ну-ка повернись!" # с любобытством
    # girl_4 смотрит надменно
    img 16343
    with diss
    reception "Чего стоишь?! Поворачивайся!"
    mt "!!!"
    # Моника поворачивается
    music Loved_Up
    img 16344
    with fadelong
    w
    img 16345
    with diss
    girl_3 "Ну смотри, у нее отличная задница!"
    girl_1 "Ну и что? Зачем нам еще одна нужна?"
    girl_1 "Да, девочки? Зачем она нам?"
    girl_2 "Ага..." # равнодушно
    music Groove2_85
    img 16346
    with fade
    reception "Послушайте, вы всегда отказываетесь обслуживать проблемных клиентов..."
    girl_3 "Пффф... С какой стати мы должны обслуживать всяких козлов?!"
    img 16347
    with diss
    reception "А у нас приличное заведение с отличной репутацией."
    reception "Ни один клиент не должен уйти неудовлетворенным, даже проблемный!"
    img 16348
    with fade
    girl_4 "Ты хочешь, чтобы она работала с проблемными? Не отбирала наших?" # с насмешливой легкой улыбкой
    img 16349
    with diss
    reception "Да, все верно."
    mt "!!!"
    reception "Она провинилась и ей нужно сначала заслужить наше доверие."
    reception "Поэтому она будет работать с проблемными клиентами!"
    music Pyro_Flow
    img 16350
    with fade
    mt "О боже! Они хотят меня отправить ко всяким извращенцам!!!"
    mt "С которыми сами не хотят работать!!!"
    mt "!!!"
    music Groove2_85
    img 16351
    with diss
    girl_4 "Думаю, это хорошая идея..."
    img 16352
    with fade
    girl_1 "Давно надо было так сделать!"
    girl_3 "Да, я согласна с девочками! А ты что скажешь?" # спрашивает у girl_2
    img 16353
    with diss
    girl_2 "Ага. Я тоже так считаю..."
    # админ обращается к Монике
    img 16354
    with fade
    reception "Можешь одеться."
    # кадр меняется. Моника стоит на том же месте, уже в одежде
    m "..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 16355
    with fadelong
    reception "Ну что? Ты согласна работать с теми, кого мы тебе дадим?"
    reception "У нас здесь строгие правила."
    reception "Будешь зарабатывать 50 процентов от суммы, оплаченной клиентом."
    img 16330
    with fade
    mt "50 процентов? Всего?"
    m "..."
    img 16356
    with diss
    reception "Решение по вопросу чаевых принимается отдельно."
    reception "Нельзя говорить 'нет' клиентам."
    reception "Любая запрошенная услуга, если она есть в прайсе, должна быть оказана!"
    img 16357
    with fade
    reception "А в нашем прайсе есть практически все!"
    reception "За отказ или грубость к клиенту - предупреждение или увольнение."
    reception "И еще у тебя нет права выбирать клиентов, как у других девушек."
    mt "!!!"
    img 16358
    with diss
    reception "Тебе нужно просто сидеть за столиком. Клиент сам подойдет к тебе."
    reception "А если поступит вызов, то тебя позовут."
    img 16334
    with fade
    reception "Если согласна на такие условия..."
    reception "То завтра можешь приступать к работе."
    img 16359
    with diss
    mt "..."
    $ menu_corruption = [0, monicaReceptionConversationCorruption8]
    menu:
        "Нет. Я не смогу.":
            # Моника нерешительно
            music Pyro_Flow
            img 16360
            with fade
            mt "Она сказала, что у меня будут проблемные клиенты..."
            mt "Значит, будут одни извращенцы."
            img 16361
            with diss
            mt "Неизвестно, чего мне от них ожидать..."
            mt "Нет! Я не могу согласиться на такое!"
            music Groove2_85
            img 16335
            with fade
            m "Я..."
            m "Я не смогу..."
            m "Мне нужно время, чтобы подумать..."
            img 16338
            with diss
            reception "Здесь у тебя будет неплохой заработок..."
            reception "Если, конечно, будешь хорошо себя вести с клиентами."
            img 16339
            with fade
            reception "Подумай..."
            reception "Ты знаешь, где меня найти."
            # Моника уходит
            return False
        "Согласиться.":
            $ monicaHotelAdminAgreement3 = True # Моника согласилась работать в эскорте
            pass
    # Моника сомневаясь
    music Pyro_Flow
    img 16361
    with fade
    mt "Она сказала, что у меня будут проблемные клиенты..."
    mt "Значит, будут одни извращенцы."
    mt "Неизвестно, чего мне от них ожидать..."
    mt "..."
    img 16360
    with diss
    mt "С другой стороны, мне нужны деньги."
    mt "А 50 процентов от суммы, которую платит здесь клиент - это немало."
    mt "Мне ничего не мешает сейчас согласиться..."
    mt "А если что-то пойдет не так с клиентом, я просто уйду отсюда и все."
    mt "Мне нужно попытаться заработать хоть какие-то деньги..."
    # Моника нерешительно
    music Groove2_85
    img 16322
    with fade
    m "Я..."
    m "Согласна на любую работу."
    m "Обещаю, что не буду отбирать у девочек их клиентов."
    # брюнетка с каре
    img 16362
    with diss
    girl_1 "Да зачем она нам нужна?!"
    girl_1 "Давай, не будем ее брать!"
    img 16363
    with fade
    reception "Все! Решение принято, вопрос закрыт!" # обращаясь к girl_1
    reception "Все, девочки! Расходимся! Пора работать!"
    # девочки расходятся и смотрят на Монику, кто с любопытством, кто надменно
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 0.5
    sound highheels_short_walk
    music Groove2_85
    img 16364
    with fadelong
    w
    sound highheels_short_walk
    img 16365
    with fade
    girl_4 "Добро пожаловать в наш дружный коллектив." # насмешливо, проходя мимо Моники
    music Pyro_Flow
    mt "!!!" # смотрит на нее подозрительно
    img 16366
    with diss
    mt "Они тут все сучки! А эта - особенно."
    m "..."
    music Groove2_85
    img 16326
    with fade
    reception "Да, совсем забыла... Как тебя зовут то?"
    img 16328
    with diss
    m "Меня зовут..."
    $ monica_hotel_name = t__("Снежанна")
    if renpy.android == True:
        call screen input_softkeyboard
        $ monica_hotel_name = _return
    else:
        $ monica_hotel_name = renpy.input(t__("Меня зовут... (enter для ввода)"), monica_hotel_name)
    if monica_hotel_name == False:
        $ monica_hotel_name = t__("Снежанна")
    m "Меня зовут [monica_hotel_name]."
    # девочки разошлись, админ обращается к Монике
    img 16329
    with fade
    reception "Завтра жду тебя на работе, [monica_hotel_name]!"
#    $ log1 = t_("Прийти в отель ЛеГранд завтра.")
#    $ log1 = t_("Мне предложили работу в эскорте! Неужели я решусь на такое?! Хотя... Там можно неплохо заработать.") # квест лог
    return

# Моника, выйдя из отеля после того, как согласилась работать в эскорте
label ep210_dialogues7_escort_hotel_7a:
    # не рендерить!
    mt "Кошмар!!!"
    mt "Неужели я решусь на такое?! Это же проституция!"
    mt "Смогу ли я обслуживать мужчин за деньги?!"
    mt "Возможно, эти эскорт-услуги не предполагают под собой интим?"
    mt "Может, мне просто нужно будет сопровождать богатых мужчин на каких-то мероприятиях?"
    mt "Если так, то я вполне справлюсь с этим."
    mt "..."
    mt "А если потом нужно будет заниматься с ними сексом?!"
    mt "!!!"
    mt "Мне нужно будет прийти сюда завтра."
    mt "Я ведь в любой момент смогу отказаться и уйти."
    return

# Моника, выйдя из отеля после того, как отказалась от эскорта
label ep210_dialogues7_escort_hotel_7b:
    # не рендерить!
    mt "Это омерзительно!"
    mt "Я никогда не смогу решиться на такую работу!"
    mt "Я Моника Бакфетт, а не какая-то проститутка! Я леди!"
    return

# Моника, выйдя из отеля ЛеГранд, хочет снова зайти в него (если согласна на эскорт)
label ep210_dialogues7_escort_hotel_7c:
    # не рендерить!
    mt "Я не хочу больше возвращаться туда! Не сегодня."
    mt "Администратор сказала приходить завтра."
    return False

label ep210_dialogues7_escort_hotel_7d:
    mt "Я не хочу больше возвращаться туда! Не сегодня."
    return

# Моника, придя на работу в эскорт, перед отелем
label ep210_dialogues7_escort_hotel_7e:
    # не рендерить!
    mt "Неужели я решусь на такое?!"
    mt "Смогу ли я обслуживать мужчин за деньги?!"
    mt "!!!"
    mt "Я ведь в любой момент смогу отказаться и уйти..."
    return

# Моника заходит в отель работать в эскорте, ресепшен (первый раз)
label ep210_dialogues7_escort_hotel_8:
    # Моника в нерешительности подходит к стойке ресепшена
    music Groove2_85
    img 16319
    with fadelong
    sound highheels_short_walk
    w
    img 16320
    with fade
    reception "Пришла?"
    m "Да..."
    img 16314
    with diss
    reception "Хорошо."
    reception "В этой одежде чтобы я тебя на работе не видела!"
    reception "В служебном коридоре для тебя приготовлено платье."
    img 16310
    with diss
    reception "Работать в ресторане всегда только в этом платье."
    reception "Переодевайся и иди за столик."
    # Моника в растерянности
    music Villainous_Treachery
    img 16313
    with fade
    m "А мне... Мне прямо сегодня нужно будет..."
    m "Провести встречу с клиентом?"
    music Groove2_85
    img 16307
    with diss
    reception "Да. Если ты пришла заработать денег, то иди и работай."
    reception "Здесь не место разводить сопли."
    img 16309
    with diss
    mt "..."
    menu:
        "Нет. Я не смогу.":
            # Моника нерешительно
            music Pyro_Flow
            img 16300
            with fade
            mt "Нет! Я не могу это сделать!"
            img 16304
            with diss
            m "Я..."
            m "Я не смогу..."
            m "Мне нужно время, чтобы подумать..."
            music Groove2_85
            img 16305
            with fade
            reception "Здесь у тебя будет неплохой заработок..."
            reception "Если, конечно, будешь хорошо себя вести с клиентами."
            img 16310
            with diss
            reception "Подумай..."
            reception "Ты всегда меня можешь найти здесь."
            # Моника уходит
            return False
        "Переодеться и идти в ресторан.":
            pass
    music Groove2_85
    img 20398
    with fade
    reception "Запомни, никаких глупостей!" # строго
    reception "Клиент всегда прав. Ты не должна спорить с клиентом."
    reception "Если отказываешь от чего-либо, что требует клиент..."
    img 16312
    with diss
    reception "То он вправе не заплатить тебе."
    reception "Если клиент не заплатил тебе, значит он мог заплатить другой девушке..."
    reception "У которой нет глупых предрассудков."
    img 16310
    with diss
    reception "Следовательно, это потеря денег для организации."
    reception "Это неприемлемо! Тогда ты вылетишь отсюда назад на улицу!"
    img 16318
    with fade
    mt "Я просто попробую..."
    mt "Если что-то пойдет не так - уйду отсюда."
    mt "..."
    # кадр меняется, Моника в новом платье стоит в ресторане
    return

label ep210_dialogues7_escort_hotel_8_menu:
    menu:
        "Работать в эскорте.":
            return 2
        "Идти в ресторан.":
            return 1
    return

label ep210_dialogues7_escort_hotel_8_enter_restaurant:
    music Groove2_85
    img 16296
    with fadelong
    reception "Куда собралась? Тебе надо переодеться!"
    img 16304
    with diss
    m "Я не на работу. Я просто поесть..."
    img 16305
    with fade
    reception "Хорошо, иди."
    reception "Но учти, что здесь надо работать и ублажать клиентов, а не отдыхать!"
    return


# Моника заходит в отель работать в эскорте, ресепшен (регулярно)
label ep210_dialogues7_escort_hotel_8a:
    # Моника в подходит к стойке ресепшена
    music Groove2_85
    img 16319
    with fadelong
    sound highheels_short_walk
    w
    img 16320
    with fade
    reception "Пришла?"
    m "Да..."
    img 16296
    with diss
    reception "Хорошо."
    reception "Переодевайся и иди за столик."
    img 16301
    with fade
    mt "..."
    reception "Запомни, никаких глупостей!" # строго
    img 16313
    with diss
    m "Да-да, я помню..."
    img 16294
    with fade
    mt "Что-то пойдет не так - я просто уйду и все."
    # кадр меняется, Моника в новом платье стоит в ресторане
    return


# платье переодевается каждый раз, когда приходит работать в эскорт и идет в ресторан (по аналогии с офисом)


# Моника проходит мимо девочек-эскортниц, брюнетка с каре и челкой
label ep210_dialogues7_escort_hotel_8a2:
    music Groove2_85
    img 30000
    with fadelong
    sound highheels_short_walk
    w
    img 30001
    with fade
    girl_1 "О, кто к нам пришел!"
    girl_1 "Сегодня у тебя не получится уводить наших клиентов..."
    girl_1 "Будешь работать с тем, кого мы тебе дадим!"
    music Pyro_Flow
    img 30002
    with diss
    m "..."
    mt "Сучка. Не хочу с ней разговаривать."
    return

# Моника проходит мимо девочек-эскортниц, рыжая с каре
label ep210_dialogues7_escort_hotel_8b:
    music Groove2_85
    img 30003
    with fadelong
    sound highheels_short_walk
    w
    img 30004
    with fade
    girl_2 "Привет."
    girl_2 "Надеюсь, мне сегодня подвернется нормальный клиент..."
    img 30005
    with diss
    m "Да... И мне тоже."
    img 30006
    with fade
    girl_2 "Ну, не знаю... Тебе то, что останется..."
    music Pyro_Flow
    img 30007
    with diss
    mt "!!!"
    return

# Моника проходит мимо девочек-эскортниц, шатенка с хвостом
label ep210_dialogues7_escort_hotel_8c:
    music Groove2_85
    img 30008
    with fadelong
    sound highheels_short_walk
    w
    img 30009
    with fade
    girl_3 "Я тебя где-то видела раньше."
    girl_3 "Не в этом ресторане..."
    girl_3 "Хммм... Не могу вспомнить, где..."
    img 30010
    with diss
    m "Наверное, ты меня с кем-то путаешь."
    music Pyro_Flow
    img 30011
    with fade
    mt "Черт!"
    mt "Она могла видеть меня на обложке журнала!"
    mt "Или на фото репортеров с конференции!"
    mt "Я не хочу, чтобы они узнали, что я Моника Бакфетт!"
    return

# Моника проходит мимо девочек-эскортниц, брюнетка с длинными волосами
label ep210_dialogues7_escort_hotel_8d:
    music Groove2_85
    img 30012
    with fadelong
    sound highheels_short_walk
    w
    img 30013
    with fade
    girl_4 "Пришла? Это хорошо."
    girl_4 "Это значит, что у меня сегодня не будет придурков-клиентов."
    girl_4 "Чего не скажешь о тебе..."
    music Pyro_Flow
    img 30014
    with diss
    mt "Как она со мной разговаривает?!"
    mt "Я поставлю эту сучку на место!"
    img 30015
    with diss
    mt "При первой же возможности!"
    mt "!!!"
    return

# приходит в ресторан работать в эскорте и садится за столик - появляется шкала (1000 баллов)
# шкала от обычной шлюхи до ВИП эскортницы, возрастает с опытом и количеством клиентов
# отказ от какой-либо услуги - шкала убывает, согласие - возрастает
# чем выше шкала, тем больше может заработать
# хэнд-джоб +1
# блоу-джоб +5
# титс-джоб +3
# секс +7
# анальный секс +9
# фетиши +9
# групповой секс +13
# если на выезде, то +1 к услуге
# отказ от предоставления услуги -5

# Моника сидит за столиком в ожидании клиента
label ep210_dialogues7_escort_hotel_9:
    mt "Так, Моника. Соберись!"
    mt "Не надо так нервничать."
    mt "Ты в любой момент может послать всех к черту и уйти."
    # к столику подходит полный мужчина, очкарик. в приличном костюме. с виду интеллигентный интеллигент
    client "Добрый вечер, Мисс."
    client "Я Вас раньше здесь не видел. Как вас зовут?"
    m "Добрый вечер, Мистер."
    m "Меня зовут [monica_hotel_name]."
    client "[monica_hotel_name]. Какое прекрасное имя. Как и его обладательница."
    client "Я очень рад, что сегодня проведу вечер с Вами, [monica_hotel_name]."
    # Моника смотрит на него, размышляя
    mt "Хмм... Разговаривает вежливо, выглядит вполне прилично."
    mt "Думаю, от него не стоит ожидать никаких извращений..."
    client "Позволите мне сразу пригласить Вас в номер, [monica_hotel_name]?"
    mt "..."
    menu:
        "Уйти отсюда!":
            # Моника нерешительно
            mt "Нет! Я не могу это сделать!"
            m "Я..."
            m "Я не смогу с Вами пойти..."
            m "Я... Я не работаю здесь!"
            m "Я просто зашла поесть в ресторан..."
            client "О, извините, Мисс."
            client "Наверное, я перепутал столик."
            # Моника встает и уходит
            return False
        "Пойти в номер с клиентом.":
            pass
    mt "Это же совсем нестрашно."
    mt "Это просто обычный неудачник."
    mt "Наверное, приходит сюда раз в месяц в день зарплаты. Фи!"
    mt "Что-то пойдет не так - я просто уйду отсюда."
    # Моника смотрит на клиента
    m "Да, мы можем пойти в номер."
    return

# Моника с клиентм возле лифтов в отеле
label ep210_dialogues7_escort_hotel_9_1:
    client "Пройдемте в номер, [monica_hotel_name]."
    mt "..."
    mt "Это же совсем нестрашно."
    mt "Это просто обычный неудачник."
    mt "Наверное, приходит сюда раз в месяц в день зарплаты. Фи!"
    mt "Что-то пойдет не так - я просто уйду отсюда."
    return

# Моника с клиентом в номере отеля
label ep210_dialogues7_escort_hotel_10:
    # клиент сидит на кровати, Моника растерянно стоит перед ним
    m "Что мне нужно сделать?"
    mt "Дал бы денег просто так и отпустил бы..."
    mt "У меня нет никакого желания делать для него что-то."
    client "Для начала [monica_hotel_name] должна снять платье..."
    mt "Моника, не переживай."
    mt "Тебе нечего стесняться. У тебя великолепное тело."
    mt "..."
    mt "Он, наверняка, никогда не видел такой красивой женщины, как я."
    # она снимает платье и стоит перед клиентом голая
    # тот ее рассматривает внимательно
    mt "Сейчас он разденется и начнет лапать мое прекрасное тело. Фу!"
    # клиент не раздевается
    client "[monica_hotel_name], присаживайтесь рядом со мной."
    # Моника садится на кровать, клиент опускается на колени на пол перед ней
    client "Если [monica_hotel_name] позволит мне целовать ее ножку..."
    client "Я буду щедр с Мисс."
    # Моника смотрит на него удивленно
    mt "Он хочет целовать мне ноги?"
    mt "Да еще и платить за это?!"
    mt "Он это серьезно?!"
    mt "???"
    mt "Может, я ослышалась?"
    m "Мистер, Вы хотите целовать мою ногу?"
    client "Да, Мисс. Позвольте Вашу ножку."
    m "..."
    # Моника протягивает ему ногу и он начинает целовать ее, берет пальчики в рот, облизывает
    # Монике приятно
    mt "О, как же это..."
    m "Ммммм..."
    mt "Это приятно..."
    mt "Черт!"
    mt "Я готова работать так каждый вечер."
    # клиент отстраняется от ее ноги
    client "А теперь [monica_hotel_name] возьмет мой палец в свой ротик..."
    client "И пососет его..."
    # Моника смотрит удивленно на его руку, он улыбается
    mt "???"
    menu:
        "Нет, я не смогу!":
            # Моника нерешительно
            mt "Фу! Нет! Я не могу это сделать!"
            m "Я..."
            m "Я не смогу..."
            m "Я... Я не предоставляю такую услугу!"
            client "Но, Мисс... Мне сказали, что..."
            m "Нет. Я не буду этого делать!"
            # Моника встает и уходит
            return False
        "Сделать, как требует клиент.":
            pass
    # Моника с отвращением смотрит на его руку
    mt "Это унизительно и..."
    mt "Противно!"
    mt "Но он сказал, что будет щедр..."
    mt "Все же это не какое-то там гадкое извращенство..."
    # Моника с отвращением, но все приближает губы к его руке
    mt "Главное, чтобы меня не стошнило прямо на него."
    # она прикасается к его руке губами и берет в рот его палец
    client "Соси его!"
    client "Оооооо!!!"
    client "О, дааааа!"
    client "Как же приятно! Ещееее!!!"
    # в процессе он другой рукой расстегивает ширинку, достает член и дрочит, пока Моника сосет его палец
    # клиент дрочит, пока его палец во рту у Моники, и кончает на постель
    client "ААААААА!!!"
    mt "Фу! Это было мерзко!"
    # клиент доволен, застегивает штаны
    client "[monica_hotel_name] старалась и мне очень понравилось."
    # Моника молча смотрит на него, вытирается
    m "..."
    # он встает и оставляет на кровати купюры
    client "Здесь 700 долларов. Я обязательно приду к Вам еще раз, [monica_hotel_name]." # уходит
    # Моника смотрит на деньги
    mt "700 долларов?!"
    mt "Я заработала 700 долларов, облизывая палец незнакомому мужчине!"
    mt "..."
    mt "Меньше всего хочется отдавать половину этой сучке на ресепшене..."
    mt "Может, уйти и больше просто не приходить сюда?"
    mt "Что она мне сделает?"
    mt "С другой стороны, здесь я за вечер могу заработать такие большие деньги."
    mt "А она меня больше не пустит в ресторан."
    mt "Нет, мне не стоит пока терять эту возможность заработка."
    $ log1 = t_("Пойти на ресепшн и отдать 50 процентов от заработка администратору.")
    return

# Моника после клиента идет на ресепшен
label ep210_dialogues7_escort_hotel_11:
    # китаянка стоит за стойкой ресепшена
    m "Клиент заплатил 700 долларов."
    reception "И остался доволен."
    reception "Ты хорошо поработала ртом."
    mt "!!!"
    m "Откуда ты?.."
    reception "Я все знаю..."
    reception "Это моя работа!"
    reception "Вот твои деньги."
    # отдает ей 350 долларов
    reception "Завтра можешь приходить снова."
    reception "На сегодня все. Клиенты не любят использованный товар."
    mt "Вот сучка!"
    mt "Откуда она знает, что я... Работала ртом?!"
    mt "Она подглядывала?!"
    mt "!!!"
    # Моника уходит
    return

# если Моника хочет уйти, не отдавая денег
label ep210_dialogues7_escort_hotel_11_1:
    mt "Я пока не могу так рисковать!"
    mt "Эта сучка меня не пустит больше в ресторан, если я не отдам ей 50 процентов."
    mt "А мне не выгодно терять такой заработок."
    mt "..."
    return

# в неделю максимальный заработок 5500 баксов
# если заработала 5500 в отеле, то фотосессии и контракт со Стивом недоступны

# Моника, выйдя из отеля после того, как обслужила клиента
label ep210_dialogues7_escort_hotel_11a:
    # не рендерить!
    mt "Я сегодня за вечер заработала 350 долларов."
    mt "Неплохой заработок, учитывая мою временную ситуацию."
    mt "Возможно, мне стоит пересилить себя и поработать здесь еще какое-то время."
    mt "Быть может, у меня получится зарабатывать еще больше."
    mt "Мне нужно будет прийти сюда завтра."
    mt "..."
    mt "Я ведь в любой момент смогу отказаться и уйти."
    return

# Моника, выйдя из отеля после того, как отказалась обслуживать клиента
label ep210_dialogues7_escort_hotel_11b:
    # не рендерить!
    mt "Я никогда не смогу решиться на такое!"
    mt "Я Моника Бакфетт, а не какая-то проститутка!"
    return

# Моника сидит за столиком в ожидании клиента
label ep210_dialogues7_escort_hotel_12_1:
    mt "Надеюсь, сегодня я смогу заработать хоть что-нибудь..."
    mt "Мне нужны деньги."
    # походит служащий отеля. смущаясь
    hotel_staff "М-мэм?"
    # Моника злобно на него смотрит
    mt "Никчемный неудачник!"
    mt "Это от него администратор узнала, что я..."
    mt "Была с ним за деньги!"
    mt "Я ему это еще припомню!"
    hotel_staff "С ресепшена просили передать, что у Вас клиент."
    mt "И где же он?"
    hotel_staff "Он Вас ждет по этому адресу."
    # кладет на стол листочек бумаги или салфетку с адресом и уходит
    mt "..."
    mt "Хмм... Это кафе... "
    mt "Мне предстоит сопровождать клиента на мероприятии?"
    mt "???"
    mt "Ну что ж... Если мне что-то не понравится, я просто уйду из кафе."
    $ log1 = t_("Вызов к клиенту. Он ждет в кафе.")
    return

# Моника на выезде к клиенту
label ep210_dialogues7_escort_hotel_12:
    # Моника стоит в кафе, оглядывается
    mt "И где мне искать этого неудачника?"
    mt "???"
    mt "Долго мне тут стоять?!"
    # к ней подходит мужчина
    client "Вы [monica_hotel_name]?"
    client "Рад, что Вы приехали."
    mt "Ну наконец-то..."
    client "Я вперве обращаюсь к услугам девушки с эскорта." # мнется
    client "И немного переживаю, как все пройдет."
    client "Дело в том, что у меня тут мероприятие в компании знакомых и коллег."
    client "И мне нужна девушка, которая будет просто меня сопровождать..."
    client "Сделаете вид, что мы с Вами давно знакомы..."
    client "Пообщаетесь с ними, поужинаете и, в принципе, все."
    m "И все?" # удивленно
    m "На этом моя работа будет закончена?"
    client "Да-да. Мне другие услуги, которые оказывает ваша компания, не нужны."
    client "Только эскорт-сопровождение на ужине. И все."
    mt "Моника, тебе сегодня повезло с клиентом..."
    mt "Вкусный ужин, светские разговоры в компании приличных людей..."
    mt "И никаких извращенцев."
    mt "Все, к чему ты так привыкла... И чего так не хватает теперь."
    mt "Похоже, что эта работа не так уж и плоха..."
    mt "Нет, конечно это отвратительно, но..."
    mt "Учитывая другие варианты заработать деньги, эскорт не так уж плох..."
    client "[monica_hotel_name], если Вы не против, то я могу пригласить Вас к столу..."
    m "Да, пройдемте к столу."
    # кадр меняется. Моника за столом, помимо нее и клиента сидят другие люди
    client "Ребята, минуту внимания."
    client "Хочу представить вам [monica_hotel_name]."
    client "Это моя девушка и мы с ней встречаемся."
    client_friend_1 "Привет, [monica_hotel_name]!"
    client_friend_2 "Рад знакомству, [monica_hotel_name]!"
    m "Спасибо." # натягивая улыбку, ведет себя по снобски
    # все настроены дружелюбно, вежливо общаются и улыбаются
    client_friend_1 "[monica_hotel_name], расскажите, чем Вы занимаетесь?" # дружелюбно
    # Моника с важным видом
    m "Я являюсь руководителем в одной крупной компании."
    m "Помимо основной деятельности, связанной с индустрией моды..."
    m "У меня еще бизнес в сфере недвижимости."
    client_friend_2 "О, серьезно?!" # удивленно
    m "Да, у меня в подчинении много сотрудников."
    client_friend_1 "Ваша деятельность связана с модной индустрией?"
    client_friend_1 "Расскажите нам. Это очень интересно." # заинтересованность
    m "По работе мне часто приходится посещать публичные мероприятия..."
    m "Выступать перед публикой, давать интервью."
    m "И, конечно же, я всегда в курсе всех событий в мире моды."
    client "Да, [monica_hotel_name] очень занятая девушка." # дружелюбно
    client "Редко такое бывает, что мы можем провести вечер вместе..."
    client "Она по вечерам обычно ведет какие-нибудь переговоры..."
    client "И важные бизнес-встречи."
    client "Ведь такие встречи очень важны для развития ее бизнеса."
    client "Да, [monica_hotel_name]?"
    m "Все верно."
    m "У меня широкий круг знакомых, которые имеют немалый вес в этом городе..."
    m "И даже в стране."
    m "И не в моих интересах отказывать им, когда меня приглашают на встречу."
    client_friend_2 "И как у Вас хватает времени на что-то, кроме работы?" # удивленно
    # Моника преисполнена важности, ей нравится здесь
    mt "Никчемные людишки..."
    mt "Млеют при виде меня и от мысли том, кто я такая!!!"
    m "Да, это довольно непросто..."
    m "Грамотное планирование своего рабочего времени..."
    m "А также помощь моих личных ассистентов..."
    m "Позволяют мне иногда провести вечер не на работе, а в свое удовольствие."
    client_friend_1 "Удивительно, что при столь плотном графике работы..." # дружелюбно
    client_friend_1 "Вы, [monica_hotel_name], находите время на..."
    client_friend_1 "Работу в эскорте!" # дружелюбная улыбка меняется на мерзкую ухмылку
    # все смотрят на нее и противно улыбаются
    # Моника в шоке, растеряна
    m "Ч-что?"
    m "???"
    mt "Мне это послышалось?"
    mt "Или он и правда сказал что-то про... Эскорт?!"
    m "..."
    m "Простите, Мистер, я не свосем понимаю, о чем Вы..."
    # ее перебивает один из друзей клиента
    client_friend_2 "Не надо путать ее с эскортницей."
    client_friend_2 "Это обычная проститутка."
    # говорящий поворачивается к клиенту
    client_friend_2 "Ты же сам говорил, что купил ее на вечер за 900 баксов."
    # клиент весело смеется
    client "Аха-ха!!! Ты понял кто она такая, да?!"
    client_friend_2 "Да, тебе снова не удалось провести нас."
    client "Я думал, у меня получится в этот раз."
    client "Эта проститутка очень похожа на приличную девушку."
    client_friend_1 "Да ладно! Совсем не похожа!"
    client_friend_1 "Она врет о больших делах, в которых видно, что ничего не понимает!"
    mt "Что?! Это Я ничего не понимаю?!"
    mt "!!!"
    # все зло смеются, Моника понимает, что над ней посмеялись и зло смотрит на клиента, тот мерзко улыбается ей
    mt "Я не могу поверить!!!"
    mt "Он это все... Он все подстроил что-ли?!"
    mt "Они с начала вечера знали, что я... С эскорта..."
    mt "!!!"
    mt "Сволочь! Мерзавец!"
    mt "АААААА!!!"
    mt "НЕНАВИЖУ!!!"
    # Моника встает и хочет уйти, но клиент хватает ее за руку
    client "А теперь тебе нужно отработать деньги."
    client "Я плачу 900 баксов."
    client "Залезь под стол и отсоси мне!"
    # расстегивает ширинку, Моника злобно смотрит на него
    mt "Долбанный неудачник!"
    mt "!!!"
    menu:
        "Уйти!":
            # Монику бомбит
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            client "Воу... Полегче!"
            client "А то останешься без денег!"
            m "Засунь их себе в задницу!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Ударить мерзавца и уйти!":
            m "Да пошел ты к черту!"
            m "Вместе со своими друзьями!"
            m "Сборище жалких неудачников!!!"
            client "Воу... Полегче!"
            client "А то останешься без денег!"
            m "Засунь их себе в задницу!"
            m "!!!"
            # бьет его в нос, кулаком
            m "Сволочь!"
            m "!!!"
            client "Сучка!!!"
            m "Да пошел ты, придурок!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Залезть под стол и сделать клиенту минет.":
            pass
    # если
    mt "Сволочь!!!"
    mt "Они унизили меня! Посмеялись надо мной!"
    mt "Компания придурков! Жалкие неудачники!"
    mt "!!!"
    mt "Если я сейчас откажу ему..."
    mt "Я не заработаю 450 долларов. Он говорил, что заплатит 900."
    mt "А 450 долларов для меня сейчас будут совсем не лишними..."
    mt "..."
    mt "Да и потом, если я сейчас откажусь..."
    mt "Я потеряю не только деньги, но и работу."
    mt "А столько зарабатывать я больше нигде пока не смогу."
    mt "Черт!!!"
    # Моника залезает под стол, у клиента из ширинки торчит стояк. он смотрит на нее сверху
    client "Давай, отрабатывай свои деньги, шлюха!"
    mt "Ненавижу!!!" # смотрит на него снизу вверх из-под стола
    # Моника приближает лицо к его члену и берет его в рот
    client "Хорошо сосешь. Чувствуется опыт. Аха-ха!"
    mt "Интересно, что будет, если я сейчас резко сожму зубы?"
    mt "И откушу ему член."
    mt "..."
    # минет
    # клиент кончает ей в рот
    client "Мммммм..."
    # Моника выплевывает сперму под столом
    mt "Фууу!"
    # и в это время слышит
    client_friend_2 "Эй, я тоже хочу ей засунуть!"
    client_friend_2 "Только не в рот..."
    client "Без проблем, чувак. Можешь забирать ее."
    client "Мне она больше не нужна."
    mt "!!!"
    # Моника в шоке, клиент смотрит на нее сверху вниз
    client "Ты слышала?"
    client "Выбирайся оттуда!"
    m "Меня никто не предупреждал, что будет не один клиент!"
    # клиент безразлично
    client "Вообще-то, в вашей организации есть дополнительный прайс."
    client "Я плачу сверху еще 300 долларов..."
    client "И ты не можешь отказаться."
    client "Так мне сказала ваша начальница."
    client "Поняла?!"
    mt "!!!"
    mt "Мерзавец!!!"
    # Моника выбирается из-под стола, друг клиента плотоядно смотрит на нее
    client "Сейчас пойдешь с ним."
    mt "Жалкие неудачники!"
    mt "Мне администратор ничего не говорила про добавление денег по прайсу!"
    mt "Какого черта я узнаю об этом от этого мудака?!"
    mt "Эта никчемная сучка не могла меня предупредить заранее?!"
    mt "!!!"
    mt "С другой стороны... Дополнительно я заработаю еще 300 долларов."
    mt "..."
    # кадр меняется. Моника в туалете кафе с другом клиента
    # друг клиента расстегивает штаны
    client_friend_2 "Говоришь, ты большой босс? Аха-ха!"
    client_friend_2 "Никогда не трахал большого босса. Аха-ха!"
    client_friend_2 "Давай, пососи мне сначала. Шлюшка."
    mt "Никчемный неудачник!!!"
    mt "!!!"
    # тот заставляет сначала взять в рот
    client_friend_2 "Настало время трахнуть большого босса!"
    # после этого загибает ее, задирает платье и входит в нее
    # Моника злится
    mt "!!!"
    mt "Боже! Моника! Неужели ЭТО стоит терпеть из-за 900 долларов?!"
    mt "Каких-то 900 долларов!!!"
    # под конец действия приходит клиент, который купил Монику и наблюдает за ними
    client "О чувак! Давай, так ее!"
    mt "!!!"
    client_friend_2 "Эй, я трахаю большого босса. Аха-ха!"
    client "Аха-ха!!!"
    client "Так ее, эту шлюху!"
    # друг клиента кончает
    client_friend_2 "ААААААА!!!"
    # друг клиента застегивает штаны, оба мерзко улыбаются, Моника поправляет платье
    mt "Теперь я понимаю, каких клиентов имели ввиду те сучки с отеля!"
    mt "!!!"
    client_friend_2 "Шлюха в этот раз, конечно, не самый шик..."
    client "Сойдет... Под пиво. Аха-ха!!!"
    mt "!!!"
    mt "!!!!!!!"
    mt "АААААА!!!"
    # клиент кидает ей 1200 баксов
    client "Свободна!"
    # смена кадра. Моника на ресепшене в отеле.
    return

# Моника после клиента идет на ресепшен
label ep210_dialogues7_escort_hotel_11c:
    # китаянка стоит за стойкой ресепшена
    m "Клиент заплатил 900 долларов. Плюс сверху 300 долларов."
    m "За дополнительную услугу..."
    m "Он изменил условия!"
    m "Я не знала о том, что клиентам позволено такое!"
    reception "Зато клиент остался доволен!"
    reception "Есть желание клиента и есть прейскурант..."
    reception "Если тебя что-то не устраивает, можешь отправляться на улицу."
    mt "!!!"
    mt "Может, к черту эти дурацки прейскуранты?"
    mt "Попробую заработать на улице... Хоть и меньше, зато без таких унижений."
    mt "..."
    mt "Нет. Мне нужны деньги. А здесь неплохой заработок."
    mt "Я сегодня за один вечер заработала 600 долларов."
    mt "Пожалуй, мне стоит еще немного поработать здесь."
    mt "..."
    reception "Вот твои деньги."
    # отдает ей 600 долларов
    reception "Завтра можешь приходить снова."
    reception "На сегодня все. Клиенты не любят использованный товар."
    mt "Вот сучка!"
    mt "!!!"
    # Моника уходит
    return



#################################### в версии 0.11
# сцена, где клиент подходит и спрашивает про ее услуги, что-то спрашивает, а она отказывается, тот жалуется китаянка - предупреждение
# сцена по вызову, где она сидит рядом с чуваком голая на полу, а он ужинает
# фетиши
# клиент с другом, тот говорит, давай вдвоем. Моника отказывается, дала одному. а китаянка ее за это наказывает
# Ральф пришел на Моникины деньги снять Монику. одна из девочек говорит, что он стал приходить и покуапать их услуги активно, а Моника думает, сволочь! он это делает на мои деньги! ненавижу
# парень-служащий отеля будет приходит и просить, а она будет отказывать, т.к. запрещено по правилам, а он все равно будет просить
# клиент может захотеть двух девушек, но одна из них категорически против, клиент просит Монику уговорить ее
# вызов в номер. клиент в черном списке - унижение
# может прийти один из полицейских. тот говорит, что та рботает нелегально. она просит не говорить никому, и оказывает услугу бесплатно
# клиент может попросить Монику отвлечь его жену и пока ее нет сделать ему н-р минет
# + лесби контент (с китаянкой или с другими девочками)
# семейная пара - жена платит, чтобы посмотреть как муж занимается сексом с проституткой
# клиент выстраивает девушек в ряд, чтобы выбрать одну из них и заставляет что-то сделать, на что не все соглашаются
# + сцены с обычными действиями - минет, секс и т.п. - короткие сцены, их будет много
# клиент просит ее раздеться, а сам надевает ее чулки и платье и пялит ее (платье для эскорта ей выдаст админ)
