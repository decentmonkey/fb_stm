# Girl1
label cit4_dialog_1:
    $ store_music()
    music Hidden_Agenda
    sound highheels_short_walk
    img 10771
    with fadelong
    m "Добрый день! Хотите примерить это платье?"
    music Groove2_85
    img 10772
    with fade
    cit4 "Какое?"
    m "Вот это, которое на мне."
    cit4 "А разве у Вас нет такого же, но нового?"
    img 10773
    with diss
    m "Это последнее, но поверьте, оно новое."
    cit4 "Ну, не знаю... Нет, пожалуй сегодня обойдусь без примерок."
    $ restore_music()
    return True

label cit4_dialog_2:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10774
    with fadelong
    m "Здравствуйте, девушка. Не желаете ли купить это чудесное платье?"
    img 10775
    with diss
    cit4 "Да, я желаю купить чудесное платье, но это не совсем то, что я ищу."
    m "А Вы попробуйте его примерить! Уверена, оно Вам подойдет."
    img 10776
    with fade
    cit4 "А вот я не очень. Кстати, а Вы вообще кто?"
    # corruption +1 req 80
    $ menu_corruption = [80]
    menu:
        "Я... Я работаю здесь манекеном.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False
    $ add_corruption(1, "cit4_dialog_2")
    img 10777
    with fade
    m "Я... Я работаю здесь манекеном."
    music Groove2_85
    img 10778
    with fade
    cit4 "Манекеном? Как интересно..."
    cit4 "Знаешь, манекен, я уже примерила сегодня несколько платьев и ни одно ни подошло."
    cit4 "В другой раз."
    return True

label cit4_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10778
    with fadelong
    m "Добрый день! Хотите примерить это платье?"
    img 10779
    with diss
    cit4 "Вы знаете, хочу!"
    img 10780
    with fade
    mt "Неужели мне наконец повезло!"
    img 10781
    with fade
    m "Тогда пройдемте в примерочную."
    return True

label cit4_dialog_3a:

    # Ухотят и моника заходит в примерочную
    music Groove2_85
    img 10782
    with fadelong
    cit4 "Насколько я знаю, в примерочные не разрешается заходить сотрудникам!"
    # corruption +1 req 80
    $ menu_corruption = [90]
    menu:
        "Ну я не совсем сотрудник...":
            pass
        "Она права, а если так, то мне не передать ей платье.":
            $ monicaSellingDressRefuseLastDay = day
            return 0
    $ add_corruption(1, "cit4_dialog_3a")
    m "Ну я не совсем обычный сотрудник."
    m "Я... Я работаю здесь манекеном."
    m "И я помогу Вам одеться."
    music Loved_Up
    img 10783
    with fadelong
    cit4 "Эм... Ну ладно."
    img 10784
    with diss
    m "..."
    img 10785
    with diss
    cit4 "Ну же? Я жду!"
    m "!!!"
#    img 10787
#    w
    img black_screen
    with diss
    pause 1.0
    sound snd_fabric1
    img 10788
    with fadelong
    w
    img 10789
    with diss
    w
    img 10786
    with diss
    w
    # моника снимает платье клиент одевает
    sound snd_fabric1
    img black_screen
    with diss
    pause 2.0
    img 10790
    with fadelong
    cit4 "Ну как мне?"
    m "Вам очень идет!"
    cit4 "Правда? Вроде бы неплохо, но я не уверена..."
    img 10791
    with diss
    m "Да нет же, все прекрасно!"
    img 10792
    with fade
    cit4 "Мне нужно подумать, одну секундочку..."
    img 10793
    with diss
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 10794
    with fadelong
    cit4 "Хорошо, я куплю его, пойду на кассу!"
    m "Подождите!"
    music Power_Bots_Loop
    img 10795
    with fade
    mt "Дьявол! А как же Я?"
    mt "Как же мне отсюда выйти?"
    mt "У меня нет одежды!"
    img 10796
    with diss
    mt "Может одеть тряпки этой покупательницы?"
    mt "Она забрала их!"
    # Моника выглядывает
    img 10797
    with fade
    mt "Где же она?"

    music stop
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_18
    img black_screen
    with Dissolve(1)
    music Groove2_85
    # Проходит время
    img 10798
    with fadelong
    cashier "Эй! Что ты здесь делаешь?"
    cashier "Работникам нельзя занимать примерочную!"
    img 10799
    with diss
    cashier "И кто будет продавать это платье?!"
    cashier "Ты захотела в полицию, воришка?!"
    cashier "Быстро работать!"
    img 10800
    with fade
    m "Покупатель ушла на кассу."
    m "Она должна была купить платье"
    img 10801
    with diss
    cashier "Никто не подходил к кассе!"
    cashier "Иди и ищи эту покупательницу, иначе я посчитаю что ты украла платье!"

    img 10802
    with fade
    mt "!!!"
    m "Могли бы Вы найти ее?"
    m "Я... Не совсем одета..."

    music Loved_Up
    img 10803
    with fadelong
    cashier "Я могу привести ее сюда..."
    img 10804
    with diss
    m "..."
    img 10805
    with fade
    cashier "Если ты пососешь мне сосок..."
    # Показывает грудь
    music Power_Bots_Loop
    img 10806
    with fade
    m "!!!"
    img 10807
    with diss
    w
    img 10808
    with diss
    mt "Эта лесбиянка уже достала меня!"
    mt "Когда я верну свою жизнь назад, я закрою этот магазин и уволю ее к чертовой матери!"
    music Groove2_85
    img 10809
    with fade
    cashier "Ну?"
    cashier "Или ты хочешь идти в зал искать ее сама?"
    img 10810
    with fade
    $ menu_corruption = [120]
    menu:
        "Пососать сосок...":
            $ monicaLickedVivianNipple = True
            mt "Я не хочу этого делать!"
            mt "Мне, Монике Бакфетт!"
            mt "Лизать сосок у какой-то продавщицы-лесбиянки!"
            mt "Как могло до такого дойти?!"
            img 10811
            with fade
            mt "И для чего!"
            mt "Для того, чтобы не идти голой по магазину."
            mt "Не искать покупательницу, которая ходит в моем же платье!"
            mt "Чтобы уговорить ее купить его."
            mt "Купить, для того, чтобы больше не работать манекеном и получить хоть какую-то приличную одежду!"
            img 10810
            with fade
            mt "Моника, какой ужас!"
            mt "..."
            mt "Похоже мне придется преодолеть себя и сделать это."
            mt "Моника, представь что это происходит не с тобой..."
            # лижет сосок
            music Loved_Up
            img 10812
            with fade
            w
            img 10813
            with diss
            w
            img 10814
            with diss
            w
            img 10815
            with diss
            w
            #лижет
            music2 audio_LickingNipple
            img 10816
            with diss
            w
            img 10817
            with diss
            w
            img 10818
            with diss
            w
            img 10819
            with diss
            w
            img 10820
            with diss
            w
            img 10821
            with diss
            w
            img 10822
            with diss
            w
            img 10823
            with diss
            w
            music2 stop
            music Groove2_85
            img 10824
            with fade
            cashier "Молодец, хорошая девочка."
            img 10825
            with diss
            cashier "А теперь пососи второй..."
            img 10826
            with fade
            w
            img 10827
            with diss
            cashier "Давай, воришка, исправляйся..."
            img 10828
            with fade
            mt "!!!"
            img 10829
            with diss
            cashier "Ну же, девочка... Поспеши..."
            img 10830
            with fade
            $ add_corruption(3, "cit4_dialog_3a1")
            $ menu_corruption = [120]
            menu:
                "Пососать сосок...":
                    # лижет второй сосок
                    $ add_corruption(3, "cit4_dialog_3a2")
                    music Loved_Up
                    music2 audio_LickingNipple
                    img 10831
                    with fadelong
                    w
                    img 10832
                    with diss
                    w
                    img 10833
                    with diss
                    w
                    img 10834
                    with diss
                    w
                    music2 stop
                    music Groove2_85
                    img 10835
                    with fade
                    cashier "Хорошая девочка..."
                    # приводит покупателя
                    music stop
                    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_19
                    img black_screen
                    with Dissolve(1)
                    music Groove2_85
                    img 10836
                    with fadelong
                    cit4 "Я передумала покупать это платье!"
                    cit4 "Оно неподходит под цвет моих туфель!"
                    img 10837
                    with diss
                    cit4 "Пожалуйста, помогите мне переодеться назад."
                    music Power_Bots_Loop
                    img 10838
                    with fade
                    mt "!!!"
                    return 1
                "Идти в зал искать покупательницу...":
                    music Power_Bots_Loop
                    img 10839
                    with fade
                    m "Я пойду и поищу покупательницу сама!"
                    img 10840
                    with diss
                    cashier "Как хочешь..."
                    cashier "Но я запрещаю тебе одевать что-то кроме этого платья."
                    cashier "До конца рабочей смены."
                    img 10841
                    with fade
                    m "Я не собираюсь слушаться тебя!"
                    cashier "Тогда ты отправишься в полицию!"
                    img 10842
                    with fade
                    m "Ты ничего не докажешь!"
                    m "Это было несколько дней назад!"
                    music Groove2_85
                    sound snd_phone2
                    img 10843
                    with fadelong
                    cashier "Так я звоню в полицию, ты не против?"
                    img 10844
                    with diss
                    m "!!!"
                    music Hidden_Agenda
                    img 10845
                    with fade
                    m "Не надо звонить в полицию..."
                    m "Я сделаю как ты хочешь..."
                    mt "Я УБЬЮ ТЕБЯ ПОТОМ, КЛЯНУСЬ!!!"
                    music stop
                    img black_screen
                    with diss
                    pause 2.0
                    return 2

#            cashier "Хорошо."
#            cashier "Сейчас я принесу тебе платье."
            return 1
        "Идти в зал искать покупательницу...":
            music Power_Bots_Loop
            img 10839
            with fade
            m "Я пойду и поищу покупательницу сама!"
            img 10840
            with diss
            cashier "Как хочешь..."
            cashier "Но я запрещаю тебе одевать что-то кроме этого платья."
            cashier "До конца рабочей смены."
            img 10841
            with fade
            m "Я не собираюсь слушаться тебя!"
            cashier "Тогда ты отправишься в полицию!"
            img 10842
            with fade
            m "Ты ничего не докажешь!"
            m "Это было несколько дней назад!"
            music Groove2_85
            sound snd_phone2
            img 10843
            with fadelong
            cashier "Так я звоню в полицию, ты не против?"
            img 10844
            with diss
            m "!!!"
            music Hidden_Agenda
            img 10845
            with fade
            m "Не надо звонить в полицию..."
            m "Я сделаю как ты хочешь..."
            mt "Я УБЬЮ ТЕБЯ ПОТОМ, КЛЯНУСЬ!!!"
            music stop
            img black_screen
            with diss
            pause 2.0
            return 2


label cit4_dialog_3b:
    # Моника в зале, обнаженная
    # первый подход к клиентке
    music Hidden_Agenda
    sound highheels_short_walk
    img 10846
    with fadelong
    m "Мэм, простите."
    m "Вы будете покупать это платье?"
    img 10847
    with fade
    cit4 "Я подумаю. Подождите..."
    return

label cit4_dialog_3c:
    # второй подход
    music Hidden_Agenda
    sound highheels_short_walk
    img 10848
    with fadelong
    m "Мэм, простите, но если Вы не будете его покупать..."
    m "То, пожалуйста, переоденьтесь назад..."
    img 10849
    with fade
    cit4 "Я подумаю..."
    music Power_Bots_Loop
    img 10850
    with fade
    mt "СУЧКА!!! ОНА ЧТО, ИЗДЕВАЕТСЯ НАДО МНОЙ?!"
    return

label cit4_dialog_3d:
    # Моника пытается подойти еще к кому-то
    mt "Я не буду подходить к людям в таком виде!!!"
    return

label cit4_dialog_3e:
    # Моника пытается выйти на улицу
    mt "Я не пойду туда в таком виде!"
    mt "Я еще не сошла с ума!"
    return

label cit4_dialog_3f:
    return

label cit4_dialog_3g:
    # Моника подходит к продавщице
    music Power_Bots_Loop
    sound highheels_short_walk
    img 10851
    with fadelong
    m "Она не отдает платье!"
    m "Эта сучка ходит в нем по магазину!"
    m "Я сейчас схвачу ее за волосы и заставлю снять это платье!"
    music Groove2_85
    img 10852
    with fade
    cashier "Не смей грубить клиентам магазина!"
    img 10853
    with diss
    m "!!!"
    img 10854
    with diss
    w
    img 10855
    with diss
    w
    img 10856
    with diss
    cashier "Так что ты от меня хочешь?"
    music Power_Bots_Loop
    img 10857
    with fade
    m "Если ты не хочешь, чтобы я убила ее прямо здесь, то скажи ей переодеться назад!"
    music Groove2_85
    img 10858
    with fade
    cashier "Если хочешь, чтобы я тебе помогла, то перестань закрываться руками."
    cashier "Манекен не должен ничего прятать."
    music Power_Bots_Loop
    img 10859
    with fade
    m "!!!"
    cashier "Ну же?"
    $ menu_corruption = [120]
    menu:
        "Убрать руки и встать прямо.":
            # моника встает прямо
            music Groove2_85
            img 10861
            with fadelong
            w
            img 10862
            with diss
            m "Довольна?!"
            m "Теперь пойдем к этой чертовой покупательнице!"
            music stop
            img black_screen
            with diss
            pause 2.0
            music Groove2_85
            img 10863
            with fadelong
            cashier "Мэм, можно Вас на минутку?"
            cit4 "Да, конечно..."
            # Подходят к покупательнице, Моника стоит прямо

            music stop
            img black_screen
            with diss
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            img 10864
            with fadelong
            cashier "Мэм, если Вы не будете покупать платье..."
            cashier "То, пожалуйста, верните его на манекен."
            img 10865
            with diss
            cit4 "Я не буду покупать это платье."
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            img 10866
            with fadelong
            cit4 "До свидания."
            cashier "Да, Мэм. Возвращайтесь! Мы всегда рады Вам."
            music Power_Bots_Loop
            img 10867
            with fade
            if monicaBitch == True:
                mt "СУЧКА!!!"
                mt "НЕНАВИЖУ!!!"
            else:
                mt "!!!"
            return True

        "Отказаться.":
            music Power_Bots_Loop
            img 10860
            with fade
            m "Я не буду этого делать, гребаная лесбиянка!"
            m "Я знаю что у тебя на уме!"
            return False

    # уходит из примерочной, моника остается таам одна голая
#    mt "Да где ее носит?"
#    mt "Черт, а если она ушла? Что же мне делать?"
    # Душевные терзания моники , возможно кто нибудь ее сфоткает...
    $ add_corruption(5, "cit4_dialog_3g1")
    return True

label cit4_dialog_3h:
    mt "О УЖАС!"
    mt "Мне надо как-то забрать свое платье у этой стервы!"
    return False
