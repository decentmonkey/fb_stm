default monicaJuliaDate2Kiss1 = False
default monicaJuliaDate2Kiss2 = False
default monicaJuliaApartment = False  # Моника лезла к Юлии под платье у нее дома (была у Юлии в квартире)

#call ep211_dialogues4_julia_1() # разговор с Юлией при выборе в меню пункта "пригласить Юлию на второе свидание"
#call ep211_dialogues4_julia_2() # кафе, второе свидание с Юлией
#call ep211_dialogues4_julia_3() # мысли Моники перед домом Юлии
#call ep211_dialogues4_julia_4() # Моника в квартире у Юлии, до того, как пошла в туалет
#call ep211_dialogues4_julia_5() # Моника сказала, что нужно идти в туалет, повторный клик на Юлию
#call ep211_dialogues4_julia_6() # Моника заходит в туалет к Юлии
#call ep211_dialogues4_julia_7() # квартира Юлии, Моника вышла из туалета
#call ep211_dialogues4_julia_8() # мысли Моники перед домом Юлии, когда вышла от нее
#call ep211_dialogues4_julia_9() # мысли Моники перед домом Юлии, когда вышла от нее (если прекратился квест досрочно)
#call ep211_dialogues4_julia_10() # мысли Моники перед домом Юлии (глазик)
#call ep211_dialogues4_julia_11a() # мысли Моники, когда рассматривает квартиру Юлии - комната (стены, пол, окна)
#call ep211_dialogues4_julia_11b() # мысли Моники, когда рассматривает квартиру Юлии - картины на стенах
#call ep211_dialogues4_julia_11c() # мысли Моники, когда рассматривает квартиру Юлии - кровать
#call ep211_dialogues4_julia_11d() # мысли Моники, когда рассматривает квартиру Юлии - столик, цветы на нем
#call ep211_dialogues4_julia_11e() # мысли Моники, когда рассматривает квартиру Юлии - шкаф
#call ep211_dialogues4_julia_11f() # мысли Моники, когда рассматривает кухню Юлии - стены, пол
#call ep211_dialogues4_julia_11g() # мысли Моники, когда рассматривает кухню Юлии - кухонная утварь, посуда
#call ep211_dialogues4_julia_11h() # мысли Моники, когда рассматривает ванную комнату Юлии - унитаз
#call ep211_dialogues4_julia_11i() # мысли Моники, когда рассматривает ванную комнату Юлии - столик с зеркалом
#call ep211_dialogues4_julia_11j() # мысли Моники, когда рассматривает ванную комнату Юлии - душ
#call ep211_dialogues4_julia_11l() # мысли Моники, когда рассматривает ванную комнату Юлии - стиральная машинка

# при выборе в меню пункта "пригласить Юлию на второе свидание"
label ep211_dialogues4_julia_1:
    # кабинет Моники, Юлия за своим рабочим столом, а Моника замышляет дело
    music Groove2_85
    img 20886
    with fadelong
    mt "Пора уже заканчивать эту комедию с нежностями."
    mt "Мне надоело строить из себя какую-то влюбленную дурочку."
    mt "..."
    mt "Мне нужно попасть к Юлии домой."
    img 20251
    with fade
    mt "Тогда я точно смогу залезть к ней под платье..."
    mt "Или хотя бы посмотреть, какого цвета белье лежит у нее в шкафчиках."
    mt "А вдруг она меня тогда обманула и она вообще не носит трусики?"
    mt "Это бы объяснило то, что она так упорно отказывается дать заглянуть себе под юбку..."
    img 20253
    with diss
    mt "Нужно будет это выяснить."
    mt "..."
    mt "И как мне попасть к ней домой?"
    mt "???"
    img 20335
    with fade
    mt "Хм... Придется пригласить ее на свидание еще раз..."
    mt "И напроситься к ней в гости."
    img 20269
    with diss
    mt "Да, точно."
    mt "Она уже доверяет мне намного больше, чем раньше."
    mt "Думаю, в этот раз она мне не откажет."
    # Моника выдавливает из себя улыбку и подходит к Юлии
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Hidden_Agenda
    img 20906
    with fade
    w
    img 16467
    with diss
    m "Милая, я хотела бы провести с тобой вечер..."
    m "Сменить обстановку..."
    m "Мы с тобой видимся только на работе."
    m "Что скажешь?"
    # Юлия смотрит на нее радостно
    music Groove2_85
    img 16470
    with fade
    julia "Миссис Бакфетт..."
    julia "Вы... Вы приглашаете меня на свидание?!"
    music Hidden_Agenda
    img 16469
    with diss
    m "Да, милая. Я хочу пригласить тебя на ужин."
    # Юлия радостно
    music Groove2_85
    img 16468
    with fade
    julia "О, Миссис Бакфетт, это замечательная идея!"
    julia "Я с радостью проведу с Вами вечер!"
    julia "А когда?"
    img 16471
    with diss
    m "Сегодня вечером, после работы."
    m "В том же кафе рядом с твоим домом."
    julia "Хорошо, Миссис Бакфетт. С нетерпением буду ждать вечера!"
#    $ log1 = t_("После работы пойти на свидание с Юлией в кафе.")
    return

# при клике на Юлию после назначения 2-го свидания
# label ep210_dialogues5_julia_1_2


# вечер того же дня. Моника заходит в кафе в трущобах, Юлия сидит за столиком
label ep211_dialogues4_julia_2:
    # Моника подходит к столику
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Stealth_Groover
    img 16889
    with fadelong
    w
    music Loved_Up
    img 16890
    with fade
    julia "Миссис Бакфетт! Я так рада нашей встрече!"
    img 16891
    with diss
    m "Привет, милая..."
    menu:
        "Поцеловать Юлию.": #corruption
            # Моника наклоняется к Юлии и целует ее в щечку
            music Loved_Up
            img 16894
            with fade
            sound snd_kiss2
            w
            $ monicaJuliaDate2Kiss1 = True
        "Не целовать.":
            music Pyro_Flow
            img 16892
            with fade
            mt "Нет, я не хочу этого делать!" # сердито
            mt "Не хочу и не буду!"
            img 16893
            with diss
            mt "Мне надоели эти глупости!"
            mt "!!!"
    # Моника садится за столик, подходит официантка
    music Groove2_85
    img 16895
    with fade
    sound highheels_short_walk
    w
    img 16896
    with diss
    cafe_barista "Добрый вечер. Пожалуйста Ваше меню."
    # протягивает им меню
    # Юлия выбирает что-то из меню
    # Моника на свое меню даже не смотрит, внимательно следит за тем, что Юлия хочет заказать
    img 16897
    with fade
    julia "О, я так давно не ела чизкейк!"
    music Hidden_Agenda
    img 16898
    with diss
    m "Милая..."
    m "Думаю, что тебе не нужно заказывать чизкейк."
    julia "???"
    img 16899
    with fade
    m "..."
    m "Это вредно для фигуры..."
    # Юлия снова смотрит в меню
    music Loved_Up
    img 16900
    with diss
    julia "Тогда, может быть..."
    julia "..."
    # Моника косится на официантку
    music Groove2_85
    img 16901
    with fade
    mt "Долбанная официанта!"
    mt "Зачем она притащила меню?!"
#    music Groove2_85
    img 16902
    with diss
    cafe_barista "Мэм, а Вы что желаете?"
    # Моника высокомерно
    music Hidden_Agenda
    img 16903
    with fade
    m "Я ничего не буду!"
    m "Я как раз недавно плотно поела и, боюсь, еще один прием пищи может сказаться на моей фигуре."
#    music Pyro_Flow
    music Groove2_85
    img 16904
    with diss
    mt "Не хватало еще тратить здесь свои деньги!"
    mt "Откуда вообще взялись такие цены в этой дыре?!"
    # Моника снова смотрит на Юлию
    music Loved_Up
    img 16905
    with fade
    julia "Я выбрала!"
    # Юлия обращается к официантке
    img 16906
    with diss
    julia "Мне, пожалуйста, этот салат. Греческий."
    music Groove2_85
    img 16907
    with fade
    mt "Никчемная Юлия!"
    mt "Можно было выбрать что-то и подешевле!"
    music Loved_Up
    img 16908
    with diss
    julia "И еще какао, пожалуйста."
    mt "!!!"
    # Юлия обращается к Монике
    img 16909
    with fade
    julia "Миссис Бакфетт, Вы точно ничего не хотите?"
    music Hidden_Agenda
    img 16910
    with diss
    m "Нет, милая. Я не голодна..."
    # официантка Монике
    music Groove2_85
    img 16911
    with fade
    cafe_barista "Может, воды?"
    m "НЕТ!" # резко
    cafe_barista "Хорошо. Скоро принесу Ваш заказ."
    sound highheels_short_walk
    # официантка уходит, Моника смотрит на Юлию
#    music Pyro_Flow
    img 16899
    with fade
    mt "Мне снова придется платить за ужин!"
    mt "А самой сидеть и смотреть, как ест эта никчемная Юлия!"
    mt "!!!"
    music Loved_Up
    img 16912
    with diss
    julia "Миссис Бакфетт, Вы сегодня так хорошо выглядите..."
    img 16913
    with diss
    m "Спасибо... Милая..."
    m "Ты тоже."
    m "..."
    # Юлия смущенно улыбается
    music Groove2_85
    img 16914
    with fade
    mt "Мне даже не о чем с ней поговорить..."
    mt "И неудивительно! О чем может разговаривать с какой-то служанкой такая леди как Я?!"
    m "..."
#    music Groove2_85
    img 16915
    with diss
    menu:
        "Попросить Юлию рассказать о себе.":
            pass
    music Hidden_Agenda
    img 16916
    with diss
    m "Юлия, милая, расскажи о себе..."
    m "Я тут поняла, что совсем ничего о тебе не знаю..."
    # официанка приносит Юлии заказ
    music Groove2_85
    sound highheels_short_walk
    img 16917
    with fade
    cafe_barista "Ваш заказ, пожалуйста."
    julia "Спасибо."
    # Юлия начинает есть и рассказывает
    sound snd_plates1
    img 16918
    with diss
    w
    music Villainous_Treachery
    img 16952
    with fade
    w
    music Loved_Up
    img 16919
    with diss
    julia "Мне приятно, что Вас это интересует, Миссис Бакфетт..."
    m "..."
    julia "Я родилась и выросла в другой стране."
    julia "..."
    img 16920
    with fade
    julia "У моей семьи нет большого достатка."
    julia "Родители живут от зарплаты до зарплаты."
    julia "..."
    img 16921
    with diss
    julia "Я очень скучаю по своей родине, но..."
    julia "Я не хочу возвращаться туда."
    img 16922
    with fade
    sound man_steps
    m "Почему?"
    img 16923
    with diss
    sound snd_eating
    julia "У меня есть богатый и влиятельный родственник. Мой дядя."
    julia "Он пытается влиять на нашу семью и мне это совсем не нравится."
    julia "У меня с ним очень плохие отношения."
    julia "В моей семье меня никто не понимал и не поддерживал."
    img 16924
    with fade
    julia "Поэтому я уехала и живу независимо от них."
    julia "Должно произойти нечто экстраординарное, чтобы я вернулась к ним..."
    julia "..."
    # Моника внимательно смотрит на нее
    music Hidden_Agenda
    img 16925
    with diss
    mt "Странно... Дома у нее богатый родственник."
    mt "Могла бы наладить с ним отношения и не знать никакой нужды."
    mt "А она здесь работает за копейки."
    mt "Никогда не понимала логику неудачников..."
    music Groove2_85
    img 16926
    with fade
    sound snd_eating
    m "..."
    m "Сейчас ты живешь здесь, в трущобах?"
    img 16927
    with diss
    julia "Да, Миссис Бакфетт."
    julia "Я арендую тут квартиру."
    if monicaRentApartmentsInited == False:
        # Моника задумывается
        music Hidden_Agenda
        img 16928
        with fade
        mt "Хммм.."
        mt "Арендовать квартиру в трущобах - это, наверное, недорого?"
        mt "..."
#        music Pyro_Flow
        img 16929
        with diss
        mt "Но жить в трущобах!!! Фи!"
        mt "..."
    #    music Groove2_85
        mt "С другой стороны..."
        mt "Не будет деревенщины Бетти и ее мужа-подкаблучника..."
        mt "Сколько уже можно работать на эту семейку идиотов?!"
        mt "Да еще и без оплаты!"
        img 16930
        with diss
        mt "Я смогу забыть эту семейку, как страшный сон."
        mt "Начать жить независимо ни от кого."
        mt "Почему бы мне не попробовать?"
        mt "..."
        img 16931
        with fade
        mt "Только у кого мне узнать про аренду квартиры?"
        mt "Мне нужно будет подумать об этом..."
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_4
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 16933
    with fadelong
    w
    # затемнение. некоторое время спустя
    # Юлия доела ужин, официантка убирает тарелку
    sound snd_plates
    img 16932
    with fade
    cafe_barista "Мэм, с вас $ 20."
    $ add_money(-20.0)
    # Моника недовольно косится на Юлию, оплачивает ужин
    # официантка уходит
    music Loved_Up
    sound2 highheels_short_walk
    img 16934
    with diss
    julia "Миссис Бакфетт, спасибо за ужин."
    # смущается
    img 16935
    with fade
    julia "Я... Я хотела бы... в знак благодарности за вечер..."
    julia "Пригласить Вас к себе домой."
    music Hidden_Agenda
    img 16936
    with diss
    mt "!!!"
    mt "Отлично!"
    music Loved_Up
    img 16937
    with fade
    julia "Только я стесняюсь, что такая леди как Вы..."
    julia "Придет в такую конуру, в которой я живу..."
    img 16938
    with diss
    m "Да. Это, конечно, будет шокирующе для меня и непривычно..."
    m "Но ради моих чувств к тебе, милая, я готова потерпеть этот дискомфорт."
    music Hidden_Agenda
    img 16930
    with fade
    mt "Я почти у цели!"
    mt "Какой замечательный сегодня вечер!"
    music Groove2_85
    img 16939
    with diss
    sound highheels_short_walk
    julia "Спасибо, Миссис Бакфетт. Вы так добры."
    # Моника улыбается ей
    m "Ну что? Пойдем?"
    julia "Да, Миссис Бакфетт."
    # уходят с кафе
    return

# мысли Моники перед домом Юлии
# не рендерить!
label ep211_dialogues4_julia_3:
    mt "О Боже! Какой кошмарный дом!"
    mt "Как здесь можно жить?!"
    mt "Уверена, тут живут одни неудачники и... извращенцы!"
    mt "И тут небезопасно вечером..."
    if monicaRentApartmentsInited == False:
        mt "Нет. Вряд ли я смогу жить в таких условиях."
        mt "Такая леди, как я, никогда не сможет привыкнуть к подобному."
        mt "..."
        mt "Хотя... Для меня и это место сейчас бы подошло..."
    return

label ep211_dialogues4_julia_3b:
    if act=="l":
        call ep210_dialogues5_julia_3_2() from _rcall_ep210_dialogues5_julia_3_2
        return False
    m "Ну что? Пойдем?"
    julia "Да, Миссис Бакфетт."
    return False


# Моника в квартире у Юлии
label ep211_dialogues4_julia_4:
    # заходят в квартиру Юлии, Моника осматривается
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.0
    music Groove2_85
    img 23570
    with fadelong
    mt "Хммм... Я думала, будет намного хуже."
    mt "Нет, здесь все, конечно, ужасно, но..."
    mt "В моей ситуации это могло бы стать неплохим вариантом на время."
    if monicaRentApartmentsInited == False:
        img 23569
        with fade
        mt "Пожалуй, стоит обдумать вопрос аренды квартиры."
        mt "Наверняка жилье здесь почти ничего не стоит..."
        mt "И я смогу договориться с кем-нибудь о том, чтобы снимать его без лишних документов..."
        mt "И потом... Все равно никто не узнает, что я живу в трущобах."
        mt "Это ведь ненадолго."
    return

label ep211_dialogues4_julia_4a:
    # Юлия смущается, пока Моника осматривается
    img 23571
    with diss
    julia "..."
    img 23572
    with fade
    m "Юлия, милая, ты напрасно переживала."
    m "У тебя очень уютно."
    sound highheels_short_walk
    img 23573
    with diss
    julia "Правда?"
    # романтик
    music Loved_Up
    img 23574
    with fade
    m "Да, милая..."
    m "..."
    img 23575
    with diss
    w
    img 23576
    with diss
    w
    sound snd_kiss2
    img 23577
    with diss
    w
    img 23578
    with fade
    w
    sound snd_kiss2
    img 23579
    with diss
    w
    img 23580
    with diss
    sound snd_kiss2
    menu:
        "Попытаться задрать платье Юлии.": #corruption
            $ monicaJuliaApartment = True # Моника лезла к Юлии под платье у нее дома
            pass
        "Не заглядывать. (завершение сюжета с Юлией)":
            music Pyro_Flow
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело заниматься этими глупостями!"
            mt "!!!"
            sound highheels_short_walk
            img 23605
            with fade
            m "Знаешь, Юлия, у меня сегодня еще много дел."
            m "Так что, я пойду."
            music Groove2_85
            julia "Но... Миссис Бакфетт!"
            julia "Это из-за того, что я..."
            julia "Постоянно Вам отказываю?"
            music Pyro_Flow
            img 23606
            with diss
            m "Это уже не имеет значения!"
            m "Забудь все, что было!"
            m "Увидимся на работе."
            if monicaBitch == True:
                m "Дура!"
            julia "..."
            # Моника уходит, Юлия расстроена
            return False
    music Loved_Up
    img 23581
    with fade
    w
    img 23582
    with diss
    w
    img 23583
    with diss
    w
    img 23584
    with fade
    sound snd_kiss2
    w
    music Loved_Up2
    img 23585
    with diss
    w
    img 23586
    with diss
    mt "Вот он момент!"
    sound vjuh3
    img 23587
    with diss
    w
    # Моника подходит к ней и обнимает, целует в щечку, потом в губы
    # кладет руку ей на талию, потом смещает руку на попу, пытаясь поднять платье
    # Юлия отстраняется
    sound plastinka1b
    music stop
    sound Jump1
    img 23588
    with hpunch
    julia "!!!"
    music Groove2_85
    julia "Миссис Бакфетт, я... Я еще не готова..."
    menu:
        "Я просто потрогаю...":
            pass
    music Hidden_Agenda
    img 23589
    with diss
    m "Милая, я тебя просто потрогаю и не более того."
    m "У тебя ведь есть там трусики, правда?"
    img 23590
    with fade
    julia "Да, Миссис Бакфетт... Они есть..."
    img 23591
    with diss
    m "Можно я проверю это? Я только проведу там рукой, я не буду подглядывать..."
    # Юлия смущается
    img 23592
    with diss
    julia "Ну... Если только потрогать... Только совсем немного..."
    # снова поцелуй, Моника трогает ее попу и нащупывает трусики
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 23593
    with fadelong
    w
    img 23594
    with diss
    w
    sound vjuh3
    img 23595
    with diss
    mt "Ага! Она все-таки носит трусики!"
    mt "Я почти у цели!"
    img 23596
    with fade
    mt "Осталось уговорить ее приподнять платье..."
    # Моника опускает руку немного ниже и пытается залезть под платье
    # но Юлия снова отстраняется
    music Groove2_85
    sound Jump1
    img 23597
    with hpunch
    julia "Миссис Бакфетт... На сегодня этого будет достаточно..."
    # Моника расстроена
    music Power_Bots_Loop
    img 23598
#    with fade
    mt "Твою мать!!!"
    mt "!!!"
    mt "!!!!!!"
    menu:
        "Поискать трусики в ванной комнате.": #corruption
            pass
        "Уйти отсюда! (завершение сюжета с Юлией)":
            mt "Мне надоело заниматься этими глупостями!" # сердито
            mt "!!!"
            music Pyro_Flow
            img 23605
            with diss
            m "Знаешь, Юлия, у меня сегодня еще много дел."
            m "Так что, я пойду."
            music Groove2_85
            julia "Но... Миссис Бакфетт!"
            julia "Это из-за того, что я Вам отказала?"
            music Pyro_Flow
            img 23606
            with fade
            m "Это уже не имеет значения!"
            m "Забудь все, что было!"
            m "Увидимся на работе."
            if monicaBitch == True:
                m "Дура!"
            julia "..."
            # Моника уходит, Юлия расстроена
            return False
    music Groove2_85
    img 23599
    with diss
    mt "Так, Моника, спокойно."
    mt "У тебя есть еще один вариант..."
    # смотрит на Юлию, выдавливает из себя улыбку
    img 23600
    with fade
    m "Юлия, милая. Мне нужно в туалет. Подскажи, где он?"
    julia "Конечно, Миссис Бакфетт. Вон та дверь, справа."
    return

# Моника сказала, что нужно идти в туалет, повторный клик на Юлию
label ep211_dialogues4_julia_5:
    if act=="l":
        return
    julia "Дверь в туалет справа от входной двери, Миссис Бакфетт."
    return False

label ep211_dialogues4_julia_6b:
    mt "Наверняка, здесь что-то есть из ее белья!"
    return

# Моника заходит в туалет к Юлии
label ep211_dialogues4_julia_6:
    # осматривается
#    music stop
#    img black_screen
#    with diss
    sound highheels_short_walk
#    pause 1.0
#    music Pyro_Flow
    music Hidden_Agenda
    mt "Стиральная машинка... Корзина для белья... Шкафчики..."
    mt "Наверняка, здесь что-то есть из ее белья!"
    # в ванной открывает шкафчик или машинку и ищет трусики, но не находит
    img 23607
    with fade
    mt "Дьявол!"
    mt "Почему здесь ничего нет?!"
    mt "Где все белье?!"
    mt "У нее что, только одни трусики, которые сейчас на ней?!"
    # Моника злится, что снова не удалось ничего выяснить
    music Power_Bots_Loop
    mt "Какого только хлама нет, но только не трусиков!!!"
    mt "Какого черта?!"
    mt "!!!"
    mt "Никчемная Юлия!!!"
    mt "Бесит!!!"
    return

# Моника выходит из туалета к Юлии
label ep211_dialogues4_julia_7:
    # делает вид, что все в порядке, улыбается
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 23601
    with fadelong
    m "Милая, мне очень нравится твоя квартира."
    m "Она небольшая, но уютная."
    m "Я с удовольствием приду к тебе в гости еще раз..."
    julia "Я буду очень рада, Миссис Бакфетт!"
    menu:
        "Поцеловать Юлию.": #corruption
            # Моника подходит к Юлии обнимает и целует ее
            $ monicaJuliaDate2Kiss2 = True
            pass
        "Не целовать.":
            music Pyro_Flow
            mt "Нет, я не хочу этого делать!" # сердито
            mt "Не хочу и не буду!"
            mt "Мне надоели эти глупости!"
            mt "!!!"
            return
    music Loved_Up
    img 23602
    with fade
    m "Мне так не хочется уходить от тебя..."
    m "Но у меня сегодня еще дела."
    m "Скоро увидимя, милая."
    sound snd_kiss2
    img 23603
    with diss
    w
    img 23604
    with fade
    julia "До свидания, Миссис Бакфетт."
    julia "Буду очень скучать и ждать встречи с Вами."
    return

label ep211_dialogues4_julia_7a:
    if act=="l":
        return
    julia "До свидания, Миссис Бакфетт."
    julia "Буду очень скучать и ждать встречи с Вами."
    return False

# Моника перед домом Юлии, вышла от нее
# не рендерить!
label ep211_dialogues4_julia_8:
    mt "Снова ничего не получилось!!!"
    mt "!!!"
    mt "Сколько можно?!"
    mt "?!?!?!"
    return

# Моника перед домом Юлии, вышла от нее (если прекратился квест досрочно)
# не рендерить!
label ep211_dialogues4_julia_9:
    if act=="l":
        return
    mt "Все!"
    mt "С меня хватит!"
    mt "Пошло оно все к черту!"
    mt "!!!"
    return False

# Моника перед домом Юлии (глазик)
# не рендерить!
label ep211_dialogues4_julia_10:
    if day_time == "evening":
        mt "Тут небезопасно вечером..."
        mt "Наверняка, здесь полно извращенцев!"
        mt "Нужно скорее уходить отсюда!"
        mt "!!!"
        return False
    return

# мысли Моники, когда рассматривает квартиру Юлии
# не рендерить!
# комната
label ep211_dialogues4_julia_11a:
    # комната (стены, пол, окна)
    mt "Это, конечно, не шикарные апартаменты..."
    mt "Но стоит признать, что здесь довольно уютно."
    return
label ep211_dialogues4_julia_11b:
    # картины на стенах
    mt "Такие же картины висят в бывшей комнате Юлии в подвале моего дома."
    mt "Здесь они смотрятся довольно неплохо."
    return
label ep211_dialogues4_julia_11c:
    # кровать
    mt "У никчемной Юлии кровать лучше той, на которой я сплю..."
    mt "Ну ничего... Это все временно."
    return
label ep211_dialogues4_julia_11d:
    # столик, цветы на нем
    mt "Люблю, когда в доме цветы."
    mt "Они делают любое помещение уютнее и красивее."
    return
label ep211_dialogues4_julia_11e:
    # шкаф
    mt "Вот бы мне поискать белье Юлии в этом шкафу..."
    mt "Но не делать же мне это в ее присутствии."
    return
# кухня
label ep211_dialogues4_julia_11f:
    # кухня (стены, пол)
    mt "Никогда не видела такой маленькой кухни."
    mt "Выглядит достаточно чисто и аккуратно."
    return
label ep211_dialogues4_julia_11g:
    # кухонная утварь, посуда
    mt "Столько разной утвари на кухне..."
    mt "Интересно, Юлия вкусно готовит?"
    return
# ванная комната
label ep211_dialogues4_julia_11h:
    # унитаз
    mt "Фууу!"
    mt "Как здесь можно писать?!"
    return
label ep211_dialogues4_julia_11i:
    # столик с зеркалом
    mt "Столик и зеркало вместо раковины?"
    mt "А где мыть руки? В душе?"
    mt "Странно..."
    return
label ep211_dialogues4_julia_11j:
    # душ
    mt "Какое же здесь все старое! Фи!"
    mt "Я не хотела бы мыть свое прекрасное тело в таком душе!"
    return
label ep211_dialogues4_julia_11l:
    # стиральная машинка
    mt "В этой комнате все такое отвратительное..."
    mt "Фи!"
    return

label ep211_dialogues4_julia_11m:
    mt "Какой теплый плед..."
    mt "Может быть украсть его у Юлии?"
    return

label ep211_dialogues4_julia_11n:
    mt "Какая-то рухлядь Юлии..."
    mt "Зачем это ей надо, не понимаю..."
    return

label ep211_dialogues4_julia_11o:
    mt "Похоже в одной из этих глупых книг Юлия вычитала романтическую историю про отношения с начальницей..."
    mt "Это из-за той книги мне приходится притворяться перед ней."
    mt "Лучшее решение - это выкинуть их..."
    return

label ep211_dialogues4_julia_11p:
    mt "Грязные окна. Видимо Юлия их не моет, чтобы помещение не выделялось на общем фоне..."
    return

label ep211_dialogues4_julia_11q:
    $ menu_price = [20,0]
    menu:
        "Идти на свидание к Юлии.":
            return True
        "Уйти.":
            return False
    return

label ep211_dialogues4_julia_11r:
    if act=="l":
        return
    sound snd_door_locked1
    mt "Заперто"
    mt "Юлии нет дома. Интересно, где она?"
    return False

label ep211_dialogues4_julia_11s:
    mt "Пока рано уходить отсюда..."
    return False
