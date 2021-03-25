
label gallery_6875:
    #render
    #Моника обращается к Филиппу с танцем повторно
    $ store_music()
    music Groove2_85
    img 6864
    with fade
    w
    img 6865
    with fade
    philip "Да, Мэм?"
    "Вы надумали еще потанцевать?"

    menu:
        "Да, давай еще потанцуем.":
            pass
        "Уйти.":
            img 6866
            with fade
            m "Нет!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            $ restore_music()
            return

    m "Да, давай еще потанцуем."

    #танцуют
    #музыка
    music Last_Kiss_Goodnight
    img 6867
    with fadelong
    w
    img 6868
    with fade
    philip "Мэм! Продолжим наш светский разговор по поводу Вашего ротика?"

    img 6869
    w
    menu:
        "Я не собираюсь про это говорить!":
            music Groove2_85
            img 6870
            with fade
            m "Я не собираюсь про это говорить!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            $ restore_music()
            return
        "Хх... Хорошо... Филипп...":
            pass


    m "Хх... Хорошо... Филипп..."
    "Давай поговорим про это..."

    img 6871
    with fade
    philip "Итак... Миссис Бакфетт!"
    "$ 500 и мой член в Вашем прекрасном ротике!"

    img 6872
    m "$ 10.000, Филипп..."
    img 6873
    philip "$ 500, Миссис Бакфетт! Сегодня Ваш ротик не стоит больше..."
    "Это как на Бирже! Я покупаю акции на низкой цене!"

    img 6874
    m "Мне нужна хотя бы $ 1.000, Филипп!"

    img 6875
    philip "$ 500, Миссис Бакфетт!"
    "Ваш ротик слишком долго говорит! Скоро он начнет дешеветь!"

    music Villainous_Treachery
    img 6876
    m "$ 1.000!!!"
    "Мне никак нельзя меньше!"
    img 6877
    "(хмык)"
    img 6878
    philip "Миссис Бакфетт!"
    "Эта гостиница предоставляет разнообразные услуги!"
    "Я начинаю торопиться и скоро уже ухожу!"
    img 6879
    "Перед уходом мой член побывает в чьем-нибудь ротике!"
    "В Вашем, либо в каком-то другом!"

    img 6880
    m "..." #переживает

    img 6881
    philip "Ну так в чьем?"
    philip "Решайте скорее!"

    img 6882
    m "..."

    img 6883
    philip "Ну?!"

    img 6882
    menu:
        "В МОЕМ! (хмык)":
            pass
        "Мне... Мне надо подумать!":
            music Groove2_85
            img 6884
            with fade
            m "Мне... Мне надо подумать!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            $ restore_music()
            return

    music Power_Bots_Loop
    img 6885
    with fade
    m "В МОЕМ!" #очень переживает
    mt "(хмык)"
    img 6886
    w
    music Last_Kiss_Goodnight
    img 6887
    with fade
    philip "Хорошо, Миссис Бакфетт!"
    img 6888
    sound Jump2
    "Давайте еще немного потанцуем!"
    img 6889
    "Я хочу сделать это до того как испорчу помаду у Вас на губах!"

    #танцуют
    img 6890
    with Dissolve(0.5)
    w
    img 6891
    with Dissolve(0.5)
    w
    img 6892
    with Dissolve(0.5)
    w
    img 6893
    with Dissolve(0.5)
    w
    img 6894
    with Dissolve(0.5)
    w

    img 6895
    with fade
    philip "Мне нравится этот танец!"
    "Мне доставляет удовольствием наблюдать за Вашим ротиком!"
    "Ведь через 5 минут мой член будет глубоко в нем!"

    img 6896
    with fade
    mt "!!!"
    philip "Танцевать при таких обстоятельствах доставляет мне эстетическое удовольствие!"

    img 6897
    mt "!!!"

    img 6891
    with Dissolve(0.5)
    w
    img 6892
    with Dissolve(0.5)
    w
    img 6893
    with Dissolve(0.5)
    w

    music Groove2_85
    img 6898
    with fade
    philip "Достаточно! Пришла пора испортить Ваш макияж, Миссис Бакфетт!"
    img 6899
    "Идемте!"

    $ restore_music()
    return

label gallery_6915:
    music Groove2_85
    #render
    #Туалет. Моника. Филипп
    sound highheels_short_walk
    img 6900
    with fadelong
    m "Куда ты меня привел, Филипп?"
    "Это мужской туалет!"
    img 6901
    philip "Миссис Бакфетт!"
    "Мне будет неудобно находиться в женском туалете!"
    img 6902
    "Ну а для Вас, полагаю, нет никакой разницы, ведь так?"
    m "Я думала это будет хотя бы гостиничный номер!"
    img 6903
    philip "О, Мэм!"
    "Гостиничный номер будет стоить гораздо дороже Вашего ротика!"
    "Как Вы знаете, я умею считать деньги!"
    "Поэтому туалет как раз подойдет для этой цели!"

    img 6904
    mt "!!!"

    img 6905
    with fade
    philip "Итак, Миссис Бакфетт!"
    "Садитесь на колени! Вам будет неудобно принимать мой член стоя!"
    img 6906
    w
    img 6907
    w
    label gallery_6915_1:
        menu:
            "Сесть на колени. (corruption)" if corruption >= monicaPhilipBlojwobKneesCorruptionRequired:
                pass
            "Сесть на колени. (low corruption, required [monicaPhilipBlojwobKneesCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobKneesCorruptionRequired:
                jump gallery_6915_1
            "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!":
                img 6904
                with fade
                m "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!"
                return
    img 6908
    with fade
    mt "У меня нет времени!"
    "Это единственный выход!"
    "(хмык)"
    img 6909
    philip "Ну!?"
    "Я жду!!!"

    #Моника садится
    img 6910
    with Dissolve(1.0)
    w
    img 6911
    philip "Хорошая девочка..."
    sound snd_fabric1
    #звук раздевания
    img 6912
    with fadelong
    w
    #звук расстегивания змейки
    sound snd_zip
    img 6913
    w
    img 6914
    with fade
    w
    img 6915
    with Dissolve(0.5)
    w

    #Филипп подносит член ко рту
    img 6916
    w
    img 6917
    w
    philip "Миссис Бакфетт! Я попрошу Вас открыть свой ротик!"
    "Я мог бы сделать это своим членом..."

    "Но я привык к комфорту!"
    "Я привык что женщины сами открывают свой ротик чтобы принять мой член внутрь!"

    img 6918
    with fade
    mt "!!!"

    label gallery_6915_2:
        menu:
            "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!! (убежать)":
                music Pyro_Flow
                img 7052
                with fade
                m "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!"
                philip "Мэм! Куда-же ВЫ?!"
                "Мы ведь только начали!"
                #уходим в hall без филиппа и helper'а
                return
            "Открыть рот... (corruption)" if corruption >= monicaPhilipBlojwobOpenMouthCorruptionRequired:
                pass
            "Открыть рот... (low corruption, required [monicaPhilipBlojwobOpenMouthCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenMouthCorruptionRequired:
                jump gallery_6915_2

    #Моника открывает рот
    img 6919
    with Dissolve(0.5)
    w

    img 6920
    philip "Миссис Бакфетт!"
    "Не могли-бы Вы пошире открыть его?"
    img 6921
    "Наверное Вам оттуда плохо видно..."
    "Но поверьте, мне отсюда видно хорошо!"
    img 6922
    "Ваш ротик недостаточно открыт для того чтобы мой член комфортно вошел в него!"
    label gallery_6915_3:
        menu:
            "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!! (убежать)":
                music Pyro_Flow
                img 7052
                with fade
                m "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!"
                philip "Мэм! Куда-же ВЫ?!"
                "Мы ведь только начали!"
                #уходим в hall без филиппа и helper'а
                return
            "Делать все что говорит Филипп. У меня нет выхода. Мне нужны эти деньги!!! (corruption)" if corruption >= monicaPhilipBlojwobOpenMouth2CorruptionRequired:
                pass
            "Делать все что говорит Филипп. У меня нет выхода. Мне нужны эти деньги!!! (low corruption, required [monicaPhilipBlojwobOpenMouth2CorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenMouth2CorruptionRequired:
                jump gallery_6915_3
    img 6923
    with Dissolve(0.5)
    w
    img 6924
    with fade
    w
    img 6925
    with fade
    w
    img 6926
    with fade
    w
    music stop
    img 6927
    with fade
    w

    # звук хлюпания, вход члена в рот
    sound hlup19
    img 6928 #?????
    w


    music stop
    #video

    #Моника открывает рот сильнее
    #идет видео минета

    #идет видео минета
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_1 = Movie(play="video/v_Monica_Philip_Blowjob_1_1.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_1
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_2 = Movie(play="video/v_Monica_Philip_Blowjob_1_2.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_2
    philip "Миссис Бакфетт!"
    "Отлично!"
    "Чувствуется что у Вас недостаток практики!"
    "Но мне это даже нравится!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_3 = Movie(play="video/v_Monica_Philip_Blowjob_1_3.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_4 = Movie(play="video/v_Monica_Philip_Blowjob_1_4.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_4
    "Если честно, я сомневался что Ваш ротик стоит $ 500!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_5 = Movie(play="video/v_Monica_Philip_Blowjob_1_5.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_6 = Movie(play="video/v_Monica_Philip_Blowjob_1_6.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_6
    "Я думал что ему больше подходит цена в $ 300!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_7 = Movie(play="video/v_Monica_Philip_Blowjob_1_7.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_7
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_8 = Movie(play="video/v_Monica_Philip_Blowjob_1_8.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_8
    "Но нет!"
    "Теперь я уверен что $ 500 он стоит вполне!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_9 = Movie(play="video/v_Monica_Philip_Blowjob_1_9.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_9
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_10 = Movie(play="video/v_Monica_Philip_Blowjob_1_10.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_10
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_11 = Movie(play="video/v_Monica_Philip_Blowjob_1_11.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_11
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_12 = Movie(play="video/v_Monica_Philip_Blowjob_1_12.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_12 #????
    wclean



    #заглядывает рецепшин
    music Hidden_Agenda
    sound snd_door_open1
    img 6929
    with fade
    w
    img 6930
    w
    music Hidden_Agenda
    img 6931
    reception_t "Ага!"
    "А я уже начала было сомневаться в своем чутье!"
    "Эта шлюха искусно маскируется!"
    #видео 13
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_13 = Movie(play="video/v_Monica_Philip_Blowjob_1_13.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_13
    wclean
    music stop
    music Hidden_Agenda
    img 6933
    "Я почти поверила что она Леди!"
    "В нашей гостинице запрещено заниматься проституцией без разрешения!"
    #видео 14
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_14 = Movie(play="video/v_Monica_Philip_Blowjob_1_14.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_14
    wclean
    music stop
    music Hidden_Agenda
    img 6932
    "В прошлый раз она приходила с такой же целью, могу поспорить!"


    music Groove2_85
    img 6934
    with fade
    w
    # звук кончания в рот Филиппом
    sound bulk1
    philip "АААААААРРГГГХХХ!!!"
    img 6935
    w
    # звук кончания в рот Филиппом
    img 6936
    with fade
    sound bulk1
    philip "АААААААРРГГГХХХ!!!"

    #Моника сидит со спермой
    img 6937
    with fadelong
    w
    img 6938
    w
    img 6939
    with fade
    w

    img 6940
    philip "Спасибо, Моника Бакфетт!"
    philip "Вы заработали свои $ 500!"

    menu:
        "Пожалуйста, дайте еще $ 500!!!":
            pass

    img 6941
    m "Еще $ 500!"
    img 6942
    philip "?"

    img 6943
    m "Мне нужно еще $ 500!"
    img 6944
    "Пожалуйста! Прошу Вас!!!"

    img 6945
    philip "Миссис Бакфетт!"
    "Почему я должен давать Вам еще $ 500?"
    img 6946
    m "Мне очень надо! ОЧЕНЬ!!!"
    img 6945
    philip "Это не аргумент, Миссис Бакфетт!"
    "Что Вы можете предложить взамен?"

    img 6946
    label gallery_6915_4:
        menu:
            "Я могу сделать это еще раз... (corruption)" if corruption >= monicaPhilipBlojwobOpenOfferedAgainCorruptionRequired:
                img 6947
                with fade
                m "Мистер..."
                img 6948
                with Dissolve(0.5)
                "Я могу..."
                "Я могу сделать это еще раз..."
                img 6949
                with Dissolve(0.5)
                "Вы дадите мне еще $ 500..."
                img 6950
                philip "Мэм! Я говорил Вам про то что люблю женщин!"
                "Женщины не стареют и не теряют своей цены, потому что..."
                img 6951
                "Потому что они разные! Разные женщины, Мэм!"
                "Я никогда! Никогда не вставляю два раза член в одну и ту же женщину!"
                "Благодаря этому правилу их у меня много и я могу наслаждаться их вкусом!"
                img 6952
                m "Но пожалуйста, Мистер!"
                # звук пальца в ротике Моники
                sound squelch9
                img 6953
                philip "Миссис Бакфетт! Я уже купил Ваш ротик!"
                img 6954
                "Я не собираюсь еще раз покупать его!!!"
            "Я могу сделать это еще раз... (low corruption, required [monicaPhilipBlojwobOpenOfferedAgainCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenOfferedAgainCorruptionRequired:
                jump gallery_6915_4
            "Я не знаю... Мне нечего предложить...":
                img 6955
                m "Мне нечего предложить, но пожалуйста!"
                "Мистер!"
                "Для меня это жизнь или смерть!"

    img 6956
    with fade
    philip "Хотя..."
    "Знаете что..."
    music Power_Bots_Loop
    "Вы сделаете миньет первому мужчине, который зайдет сюда!"
    "Тогда Вы получите еще $ 500!"
    img 6957
    "Вы согласны?"

    m "Я... Я..."

    music Groove2_85
    #Заходит hotel_staff
    sound snd_door_open1
    img 6958
    hotel_staff "Ой!"
    img 6959
    with fade
    "Прошу прощения за беспокойство!"
    "Я зайду позже!"
    philip "Эй! Парень!"
    "Постой-ка!"

    img 6960
    with Dissolve(0.5)
    hotel_staff "Да, Сэр?"
    philip "Иди-ка сюда!"

    hotel_staff "Да, Сэр? Чем могу быть полезен?"
    img 6961
    philip "У тебя есть член, парень?"
    hotel_staff "Что Вы имеете ввиду, Сэр?"

    img 6962
    philip "Член! Есть член у тебя?!"
    "Я имею ввиду ту штуку что должна быть в штанах у каждого мужчины!"
    "Есть она у тебя или ее нет?"

    img 6963
    hotel_staff "Сэр... Конечно есть..."
    "Но я не понимаю зачем этот вопрос."
    "Я могу как-то помочь Вам?"

    img 6964
    philip "Да, парень!"
    "Открой глаза и посмотри!"
    "У меня здесь сидит сучка и сосет бесплатно члены!"
    "У тех кто сюда заходит!"

    img 6965
    "Для тебя бесплатно, конечно."
    "Для меня это кое-что стоит, но я готов потратить эти деньги для такого удовольствия."

    img 6966
    with fade
    "Ты только посмотри кто это!"
    sound Jump2
    img 6967
    hotel_staff "МИССИС БАКФЕТТ?!?!" #смотрит с ужасом

    #если Моника была зла к нему, то:
    img 6968
    #

    img 6969 #+
    philip "Да, это она!"
    "Парень! Такой шанс выпадает только раз!"
    "Ты счастливчик!"

    img 6970
    with Dissolve(0.5)
    "Моника Бакфетт сидит в туалете и ждет твой член!"
    "Она ждет его!"
    "Ее ротик приглашает твой член! Чтобы ты вставил его!"

    #обращается к Монике
    img 6971
    philip "Ну-ка открой свой ротик!"
    label gallery_6915_5:
        menu:
            "Открыть рот для нового члена. (corruption)" if corruption >= monicaPhilipBlojwobOpenMouthAgainCorruptionRequired:
                img 6978
                with Dissolve(0.5)
                w
                philip "Давай, парень!"
                img 6977
                philip "Этот ротик приглашает тебя!"

            "Открыть рот для нового члена. (low corruption, required [monicaPhilipBlojwobOpenMouthAgainCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenMouthAgainCorruptionRequired:
                jump gallery_6915_5
            "Не открывать самой...":
                img 6972
                with fade
                w
                img 6973
                "Приглашай его член!"
                img 6974
                w
                img 6973
                "Приглашай его член!"
                "Иначе не получишь деньги!"
                music stop
                img 6975
                w
                #Моника открывает рот
                #звук открывания рта пальцем Филиппа
                sound squelch9
                img 6976
                with Dissolve(0.5)
                w
                music Groove2_85
                img 6977
                philip "Давай, парень!"
                img 6978
                with fade
                philip "Этот ротик приглашает тебя!"
    img 6979
    philip "Видишь?"
    img 6980
    w
    img 6981
    w
    img 6980
    w
    img 6982
    w
    img 6980
    w
    label gallery_6996:
    img 6983
    philip "Давай! Засунь свой член туда!"
    img 6980
    w
    img 6984
    with fade
    w
    philip "Засовывай же скорее!"
    img 6985
    philip "Миссис Бакфетт не может ждать!"
    "Она хочет скорее твой член!"
    img 6986
    philip "Решайся, Малыш!"
    "Иначе это сделает следующий кто войдет сюда!"
    img 6987
    philip "Этот ротик не уйдет отсюда, пока не попробует еще какой-нибудь член!"
    img 6988
    philip "Мой член только что проверил! Там внутри все очень комфортно!"

    #парень смотрит в ужасе

    #если Моника была добра к нему
    if hotelStaffOffended1 == False:
        img 6990
        hotel_staff "Сэр!"
        "Но я не могу этого сделать!"
        "Эта женщина была добра ко мне!"
        "Пожалуйста, дайте ей то что она хочет!"

        img 6989
        philip "Ха-ха!"
        "Ладно, парень, как хочешь!"
        #смотрит на Монику
        img 6991
        with fade
        philip "Можешь закрыть свой ротик! Ты заслужила свои деньги!"
        #Моника закрывает рот
        img 6992
        with Dissolve(0.5)
        return

    #если Моника была зла к нему

    img 6993
    hotel_staff "А ведь она собиралась уволить меня!"
    philip "Ха-ха!"
    "Тем более!"
    sound snd_zip
    img 6994
    with fade
    "Этот ротик заслужил твой член!"
    "Давай! Вставь его! Скорее!"
    #звук одежды
    sound snd_zip
    img 6995
    with fade
    w
    img 6996
    w
    img 6997
    with fade
    w
    img 6998
    with Dissolve(0.5)
    w
    img 6999
    w
    label gallery_6996_1:
        img 7000
        philip "Открой рот! Приглашай его член в себя!"
        "Иначе не получишь деньги!!!"
        img 7001
        w
        #выбор делать или нет и повтор
        menu:
            "Открыть рот. Я решила делать все что говорит Филипп. Если я не достану эти деньги, то мне конец!":
                pass
            "Я не могу это сделать...":
                mt "Если я не получу эти деньги, то завтра попаду в руки Маркуса!"
                "О БОЖЕ!!!"
                jump gallery_6996_1
    img 7002
    with fadelong
    w
    img 7003
    with Dissolve(0.5)
    w
    img 7004
    with Dissolve(0.5)
    w
    img 7005
    with fade
    w
    img 7006
    w
    img 7007
    w
    img 7008
    w
    img 7009
    hotel_staff "А она ничего мне потом не сделает за это?"
    philip "Парень! Она не сделает тебе ничего!"
    img 7010
    with fade
    hotel_staff "Правда, Сэр?"
    philip "Правда, малыш!"
    "Сделай движение вперед, не бойся!"
    music stop
    hotel_staff "Хорошо, Сэр..."
    #чавкающий звук
    # звук входа члена в Моникин рот
    sound hlup19
    img 7011
    with Dissolve(0.5)
    w
    music Groove2_85
    philip "Смелее, малыш!"
    img 7012
    music stop
    hotel_staff "Хорошо, Сэр..."
    #чавкающий звук
    # звук чавкающий
    sound hlup25
    img 7013
    with Dissolve(0.5)
    w
    music Groove2_85
    img 7014
    hotel_staff "Так, Сэр?"
    philip "Долби ее в ротик!"
    "Чего ты с ней возишься?!"

    #парень начинает ее долбить
    #видео
    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_1 = Movie(play="video/v_Monica_Helper_Blowjob_1_1.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_1
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_2 = Movie(play="video/v_Monica_Helper_Blowjob_1_2.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_3 = Movie(play="video/v_Monica_Helper_Blowjob_1_3.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_4 = Movie(play="video/v_Monica_Helper_Blowjob_1_4.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_5 = Movie(play="video/v_Monica_Helper_Blowjob_1_5.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_6 = Movie(play="video/v_Monica_Helper_Blowjob_1_6.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_7 = Movie(play="video/v_Monica_Helper_Blowjob_1_7.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_7
    hotel_staff "Простите, Мэм!"
    "Пожалуйста, не увольняйте меня!"
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_8 = Movie(play="video/v_Monica_Helper_Blowjob_1_8.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_9 = Movie(play="video/v_Monica_Helper_Blowjob_1_9.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_10 = Movie(play="video/v_Monica_Helper_Blowjob_1_10.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_10
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_11 = Movie(play="video/v_Monica_Helper_Blowjob_1_11.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_11
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_12 = Movie(play="video/v_Monica_Helper_Blowjob_1_12.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_12
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_13 = Movie(play="video/v_Monica_Helper_Blowjob_1_13.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_13
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_14 = Movie(play="video/v_Monica_Helper_Blowjob_1_14.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_14
    wclean
#    "Я обязательно учту Ваши пожелания по поводу постера в следующий раз!"


    #парень кончает
    # звук кончания Монике в рот
    img 7015
    with fade
    hotel_staff "Иииииииииииии!!!"
    sound bulk1
    w

    music stop
    music Groove2_85
    img 7016
    with fade
    hotel_staff "Сэр, я могу идти?"
    img 7017
    philip "Сядь и открой рот!"
    "Я не говорил тебе его закрывать!"
    menu:
        "Делать как сказал Филипп...":
            pass
    img 7018
    with fade
    w
    img 7019
    with Dissolve(0.5)
    w
    sound man_steps
    img 7020
    with fadelong
    w
    img 7021
    philip "Я кое-что забыл..."

    music stop
    img 7022
    with fade
    w
    # звук слизи1
    img 7023
    with Dissolve(0.5)
    w
    sound hlup10
    # звук слизи2
    img 7024
    with Dissolve(0.5)
    w
    music Groove2_85
    img 7025
    with fade
    philip "Теперь глотай!"
    img 7026
    w
    img 7027
    philip "Глотай! И наша сделка закрыта!"
    label gallery_6996_2:
        menu:
            "Проглотить сперму двух мужчин... (corruption)" if corruption >= monicaPhilipBlojwobTakeSpermCorruptionRequired:
                #звук глотания
                music stop
                img 7028
                with fade
                w
                sound snd_gulp
                w
                music Groove2_85
                img 7031
                with fade
                philip "Покажи рот! Покажи что ты все проглотила!"
                "Иначе никакой сделки!"
                img 7033
                with Dissolve(0.5)
                w
                img 7034
                with Dissolve(0.5)
                w
                img 7035
                philip "Отлично, спасибо."
            "Проглотить сперму двух мужчин... (low corruption, required [monicaPhilipBlojwobTakeSpermCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobTakeSpermCorruptionRequired:
                jump gallery_6996_2
            "Притвориться что проглотила...":
                img 7028
                with fade
                w
                img 7029
                philip "Еще глоток! Там наверняка что-то осталось!!!"
                #звук глотания
#                sound snd_gulp
                img 7030
                w
                img 7031
                with fade
                philip "Покажи рот! Покажи что ты все проглотила!"
                "Иначе никакой сделки!"
                #если не проглотила, то выбор и звук глотания
                menu:
                    "Проглотить сперму по настоящему, иначе Филипп увидит и я не получу деньги...":
                        pass
                music stop
                img 7032
                with fade
                w
                sound snd_gulp
                w
                music Groove2_85
                img 7033
                with Dissolve(0.5)
                w
                img 7034
                with Dissolve(0.5)
                w
                img 7035
                philip "Отлично, спасибо."



    img 7036
    with fade
    philip "Иди, парень! Ты повеселил меня!"
    #звук одежды
    sound snd_fabric1
    img 7037
    with fadelong
    w
    #бросает деньги и они уходят
    sound snd_take_paper
    img 7038
    with fade
    philip "Вот Ваши деньги, Миссис Бакфетт!"
    img 7039
    "Я найду Вас когда захочу попробовать Вашу попку!"

    img 7040
    with fade
    m "Пожалуйста!"
    "Не говорите про это никому!!!"

    img 7041
    hotel_staff "Конечно, Мэм!"
    "Я никому не скажу!"

    #закрывается дверь
    sound snd_door_close1
    img 7042
    with fadelong
    mt "Что это?"
    "Деньги?"

    img 7043
    mt "Деньги!"

    img 7044
    mt "Это деньги!"
    "У меня теперь есть деньги для Дика!"
    "Я нашла их! Я сделала это!!!"

    img 7045
    with fade
    mt "Но что..."
    "ЧТО ЭТО БЫЛО???"
    "Я ДАЖЕ НЕ МОГУ ОСОЗНАТЬ ТОГО ЧТО ПРОИЗОШЛО!!!"
    "Это... ЭТО..."
    "У меня..."
    "У МЕНЯ НЕТ СЛОВ!!!"
    "ЧТО СО МНОЙ СДЕЛАЛИ???"
    "ИЗ-ЗА КАКОЙ-ТО ТЫСЯЧИ ДОЛЛАРОВ!!!"
    "МОНИКА, КАК ТЫ МОГЛА?!?!"

    img 7046
    mt "Но что мне оставалось делать?"
    "У меня был выбор между жизнью или смертью!!!"
    "..."
    "Но какая жизнь теперь после того что случилось???"

    img 7047
    with fade
    mt "Я, пожалуй, забуду о том что произошло здесь."
    "Даже если кто-то расскажет, все-равно этому никто не поверит!"
    "Что Моника Бакфетт могла сделать такое! Это звучит как абсурд!"

    #если Моника сучка
    if monicaBitch == True:
        music Pyro_Flow
        img 7048
        with fade
        mt "Ну а что касается того кто здесь был..."
        "Когда я решу свои небольшие проблемы, я найду Маркуса и узнаю у него..."
        "Наверняка есть какое-нибудь Ранчо 219 или что-то вроде того..."
        img 7049
        with fade
        mt "ДЛЯ МУЖЧИН!!!"
        "И кое-кто направится прямиком туда!!!"
        "И я не успокоюсь пока этого не случится!!!"
        "Никто не смеет сделать подобное с Моникой Бакфетт и остаться в живых!!!"
        "Клянусь!!!"
        #

    music Groove2_85
    img 7050
    with fade
    mt "Но что мне сейчас делать?"

    img 7051
    with Dissolve(0.5)
    mt "Мне надо умыться и {c}идти к Дику{/c}..."
    sound snd_water_hose
    #звук воды
    w
    return

############ Office 1############

label gallery_8285:
    #render
    #Моника разговаривает с секретаршей повторно

    $ store_music()
    music Stealth_Groover

    img 8282
    with fade
    secretary "Мистер Биф лучше нас знает что нам необходимо."
    secretary "Мистер Биф заботится о нас..."
    img 8283


    #если Моника сегодня не просила деньги, то появляется меню выбора
    menu:
        "Попросить деньги в долг.":
            "Дорогая..."
            secretary "Да, Миссис Бакфетт?"
            m "Скажи, у тебя не будет немного денег?"
            img 8284

            with fade
            secretary "Миссис Бакфетт! Я пока не видела зарплаты здесь, после Вашего ухода..."
            #если у Моники меньше 5 долларов, то дает, иначе нет
            secretary "Поэтому у меня нет никаких денег сейчас, Миссис Бакфетт!"
            "Простите!"
            m "А как же Биф? Он что, не дает тебе деньги?"

            img 8285

            with fade
            secretary "Мистер Биф лучше нас знает что нам необходимо."


        "Дорогуша, ты не видела Мелани?" if melanieDisappeared == True:
            call gallery_8285_1() from _rcall_gallery_8285_1

        "Заставить секретаршу показать грудь в трущобах. (bitchiness)" if game.extra == True and ep27_quests_secretary1_show_boobs_active == True and pylonpart4startsCompleted == True and monicaWorkingAtBiffOffice == True:
            call gallery_13869() from _rcall_gallery_13869
            if _return == False:
                return
        "Уйти.":
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"
    $ restore_music()
    return

label gallery_8285_1:
    # Вопрос у секретарши: Где Мелани?
    # Секретарша отвечает что не видела ее и, может быть, Моника знает где она.
    music Groove2_85

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

    return


label gallery_13869:


# Там Моника говорит ему что он обещал $ 50 за новую пару сисек.
# Тот отвечает что да, он заплатит $ 50, но только за новую пару малышек.
# Малышек Моники он уже видел!
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Hidden_Agenda
    img 13836
    with fadelong
    m "Ты говорил про то, что заплатишь $ 50 за новую пару сисек..."
    img 13837
    with diss
    citizen4 "Да, я помню!"
    citizen4 "Я заплачу $ 50, но только за новую пару малышек."
    citizen4 "Твоих малышек я уже видел!"
    music Power_Bots_Loop
    img 13838
    with hpunch
    mt "!!!"
# Секретарша спрашивает, Миссис Бакфетт, о чем говорит этот человек? Кто он?
# Моника говорит секретарше, чтобы та не задавала вопросов, что так надо.
# Говорит ситизену, что у нее есть с собой другая пара сисек и заплатит-ли он за них $50?
    img 13839
    with fade
    secretary "Миссис Бакфетт!"
    secretary "О чем говорит этот человек?"
    secretary "Кто он?!"
    music Groove2_85
    img 13840
    with diss
    m "Дорогуша, пожалуйста, не задавай вопросов."
    m "Так надо!"
    img 13841
    with diss
    m "..."
    music Hidden_Agenda
    img 13842
    with fade
    m "Итак, у меня есть с собой другая пара сисек."
    m "Готов-ли ты заплатить за них $ 50?"
# Тот подходит к секретарше и рассматривает ее.
    sound man_steps
    img 13843
    with diss
    w
    sound Jump1
    img 13844
    with diss
    citizen4 "..."
# Секретарша в шоке, смотрит на Монику.
    music Power_Bots_Loop
    img 13845
    with hpunch
    secretary "!!!"
    img 13846
    with diss
    secretary "!!!!!"
# Ситизен отвечает что да, он готов заплатить $ 50 за малышки этой девочки.
# Моника говорит ей, дорогуша, покажи ему свою грудь
# Секретарша спрашивает, но Миссис Бакфетт, я не могу сделать это...
# Я воспитана, у меня моральные принципы, я...
# И она не понимает зачем это надо и чем это поможет в...
    music Hidden_Agenda
    img 13847
    with fade
    citizen4 "Да, я готов заплатить $ 50 за малышки этой девочки."
    img 13848
    with diss
    m "Дорогуша, пожалуйста, покажи ему свою грудь."
    music Power_Bots_Loop
    img 13849
    with hpunch
    secretary "!!!"
    img 13850
    secretary "Но Миссис Бакфетт!"
    secretary "Я не могу сделать это..."
    secretary "Я воспитана! У меня моральные принципы! Я..."
    img 13851
    secretary "И я не понимаю, зачем это надо?"
    secretary "Чем это поможет в..."
# Моника прерывает и говорит что потом все объяснит, что та не видит всей картины.
# Что она всего-лишь работник, которые должен довериться своему Боссу на пути к действительно успешной карьере.
# Секретарша продолжает смотреть на Монику с ужасом
# Ситизен говорит собирается та показывать своих малышек или нет?
# Что он тратит свое время
    music Groove2_85
    img 13852
    with fade
    m "Дорогуша, я потом тебе все объясню!"
    m "Ты просто не видишь всей картины!"
    img 13853
    with diss
    m "Ты всего-лишь работник, и ты должна довериться мне, своему Боссу!"
    m "На пути к действительно успешной карьере!"
    img 13854
    secretary "!!!"
    img 13855
    with fade
    citizen4 "Ну так что, ты собираешься показывать мне своих малышек или нет?"
    citizen4 "Я что, зря трачу время?!"
# Моника говорит секретарше показать грудь. Скорее.
# Секретарша молчит и говорит Я... Миссис Бакфетт...
# Ситизен говорит что эта девочка не хочет показывать своих малышек, поэтому он уходит.
# Если Моника хочет, пусть покажет своих девочек снова за 1$, он готов заплатить его, раз уж уже потерял время.
    img 13856
    with fade
    m "Дорогуша, покажи свою грудь!"
    m "Скорее!"
    img 13857
    with diss
    secretary "Я..."
    secretary "Миссис Бакфетт..."
    img 13858
    with vpunch
    citizen4 "Эта девочка не хочет показывать своих малышек."
    citizen4 "Я ухожу!"
    img 13859
    with diss
    citizen4 "Хотя, если ты хочешь, покажи своих девочек снова за $ 1!"
    citizen4 "Я заплачу этот доллар, раз уж все-равно потерял время, придя сюда."
# Выбор:
# Дать ему уйти.
# Моника думает что она не сошла с ума показывать свою грудь за $ 1, при ком-то. Тем более при своей секретарше.
# Тогда он уходит.
# Секретарша спрашивает что это было, Миссис Бакфетт?
# Моника отвечает что ничего особенного, дорогуша, не обращай внимания. Я рада что ты не стала делать этого.
# Все заканчивается
    img 13860
    with diss
    menu:
        "Дать ему уйти.":
            img 13861
            with fade
            mt "Я еще не сошла с ума, показывать свою грудь за $ 1 при ком-то!"
            mt "Тем более при своей секретарше..."
            img 13862
            with diss
            citizen4 "Нет? Ну ладно, я пошел..." # Уходит
            sound man_steps
            img 13863
            with diss
            w
            music stop
            img black_screen
            with diss
            pause 1.0
            music Groove2_85
            img 13864
            with fadelong
            secretary "Миссис Бакфетт, что это было?"
            img 13865
            with diss
            m "Ничего особенного, дорогуша. Не обращай внимание."
            m "Я рада что ты не стала делать этого."
            return
        "Открыть грудь секретарши самой.":
            pass
# Открыть грудь секретарши самой.
# Моника говорит ему постой.
# Она стесняется. Сейчас я помогу ей.
    music Loved_Up
    img 13866
    with fade
    m "Постой!"
    m "Она стесняется. Сейчас я помогу ей."
# Моника открывает секретарше грудь.
# Секретарша смотрит в ужасе на свою грудь, затем на Монику
# Ситизен вблизи рассматривает грудь секретарши.
# Несколько кадров

# Затем говорит что хочет потрогать ее.
    img 13867
    with diss
    w
    sound snd_fabric1
    img 13868
    with diss
    w
    sound Jump1
    img 13869
    with diss
    w
    img 13870
    with diss
    w
    img 13871
    with diss
    w
    music Groove2_85
    img 13872
    with fade
    citizen4 "Я хочу потрогать ее. Можно?"
# Выбор:
# Запретить.
# Моника говорит что все, хватит, где ее $ 50
# разрешить.
# Моника говорит что это будет стоить еще $ 50
# Ситизен отвечает что у него столько нет и он может дать сверху только $ 10
# Выбор:
# Запретить
    img 13873
    with diss
    menu:
        "Разрешить за $ 50 сверху.":
            music Hidden_Agenda
            img 13874
            with fade
            m "Это будет стоить еще $ 50!"
            img 13875
            citizen4 "У меня столько нет!"
            citizen4 "Я могу дать сверху только $ 10!"
            menu:
                "Запретить.":
                    music Groove2_85
                    img 13876
                    with fade
                    m "Все, этого достаточно!"
                    m "Где мои $ 50?!"

                "Разрешить за $ 10 сверху.":
# Разрешить за $ 10 сверху
# Моника говорит что хорошо, $ 10 сверху и можешь потрогать ее.
# Секретарша в ужасе. Говорит Миссис Бакфетт!
# Моника отвечает что дорогуша, пожалуйста, стой спокойно, это очень важно и для нашего общего блага.
                    img 13877
                    with fadelong
                    m "..."
                    img 13878
                    with diss
                    m "Хорошо..."
                    m "$ 10 сверху и можешь потрогать ее."

                    music Power_Bots_Loop
                    img 13879
                    with hpunch
                    secretary "Миссис Бакфетт!"
                    music Loved_Up
                    img 13880
                    with fade
                    m "Дорогуша."
                    m "Пожалуйста, стой спокойно."
                    m "Это очень важно! И это для нашего общего блага."

# Ситизен лапает грудь, сжимая ее (морфы, видео). Сделать базовую сцену, где держит руки на груди
                    # Затем Моника также говорит что все, хватит, где ее $ 60
                    sound Jump2
                    img 13881
                    with diss
                    citizen4 "Какая упругая грудь!"

                    music stop
                    img black_screen
                    with diss
                    pause 1.5
                    stop music
                    play music "Sounds/audio_MonicaSecretary_Citizen4_Boobs_1.mp3"
                    scene black
                    image videov_MonicaSecretary_Citizen4_Boobs_1_2 = Movie(play="video/v_MonicaSecretary_Citizen4_Boobs_1_2.mkv", fps=30)
                    show videov_MonicaSecretary_Citizen4_Boobs_1_2
                #    with fadelong
                    wclean
                    stop music
                    play music "Sounds/audio_MonicaSecretary_Citizen4_Boobs_1.mp3"
                    scene black
                    image videov_MonicaSecretary_Citizen4_Boobs_1_3 = Movie(play="video/v_MonicaSecretary_Citizen4_Boobs_1_3.mkv", fps=30)
                    show videov_MonicaSecretary_Citizen4_Boobs_1_3
                #    with fadelong
                    wclean
                    stop music
                    music stop
                    music Loved_Up

                    img 13882
                    with diss
                    w
                    img 13883
                    with diss
                    citizen4 "я хотел бы увидеть ее на своем члене!"
                    music Groove2_85
                    img 13876
                    with fade
                    m "Все, этого достаточно!"
                    m "Где мои $ 60?!"


        "Запретить.":
            music Groove2_85
            img 13876
            with fade
            m "Все, этого достаточно!"
            m "Где мои $ 50?!"


    # уже не смотрит. Секретарша закрылась и с ужасом и стыдом смотрит на ситизена
# Ситизен говорит что пусть Моника приводит еще пару малышек и он заплатит еще $ 50.
# Секретарша спрашивает у Моники: Миссис Бакфетт, я все сделал как Вы хотели.
# Могу я идти, пожалуйста? (умоляюще)
# Моника отвечает что да, можешь идти дорогуша.
# Ты хорошо поработала. Я дам тебе потом премию за это.
    img 13884
    citizen4 "Хорошо."
    citizen4 "Ты можешь привести еще пару малышек и я заплачу тебе еще $ 50." # ситизен уходит
    sound man_steps
    img 13885
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 13886
    with fadelong
    secretary "Миссис Бакфетт..."
    secretary "Могу я идти, пожалуйста?" #(умоляюще)
    img 13887
    with diss
    m "Да, можешь идти дорогуша."
    m "Ты хорошо поработала."
    m "Я дам тебе потом премию за это."
    return

label gallery_20265:
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

label gallery_20300:
    music Groove2_85
    img 20300
    with fade
    m "Послушай..."
    w1 "Ой... Я..."
    img 20301
    m "Ты что, язык проглотила?"
    w1 "Нет... Я..."
    img 20300
    with diss
    m "А похоже, что проглотила."
    m "Когда закончишь работать с бумагами, не забудь принести их мне в офис."
    w1 "Да, мэм!"
    return

label gallery_20303:
    music Groove2_85
    img 20302
    with fade
    mt "Этот неудачник, похоже, разбирается в компьютерах... Но я в них ничего не понимаю..."
    mt "Да и мне неинтересно..."
    mt "У меня может быть какое-то дело нему?"
    menu:
        "Задать умный вопрос.":
            img 20303
            with diss
            m "Послушай, а где здесь кнопка, которая выключает интернет?"
            w2 "Что?!"
            m "Ну такая специальная кнопка, на которую нажимаешь и отключается интернет."
            w2 "(Похоже наш босс не слишком силен в этом...)"
            w2 "Она на кухне, рядом с холодильником."
            m "Хорошо, спасибо."
            w2 "(Ха-ха-ха.)"
            # моника отошла
            music Stealth_Groover
            img 20304
            with fade
            mt "Рядом с холодильником?! Так, ерунда какая-то..."
            mt "Это такая умная шутка?"
            mt "Он играет с огнем..."
#            mt "Ладно, лучше не буду в это лезть, все равно в этом ничего не понимаю..."
#            mt "Зато я точно знаю, кто в этом разбирается..."
            return
        "Уйти.":
            m "Все равно я в этом ничего не понимаю..."
            return

label gallery_20310:
    music Groove2_85
    img 20308
    with fade
    mt "Вторая сестра... Никак не могу запомнить как их зовут.."
    img 20309 #
    with diss
    m "Здравствуй. Напомни, как тебя зовут?"
    img 20310
    with fade
    w4 "Я Элла. Мою сестру зовут Эмма. Нас всегда путают!"
    img 20311
    with diss
    m "Поняла. Продолжай работать."
    return

label gallery_20314:
#    m "Послушай..."
    music Groove2_85
    img 20314
    with fade
    w6 "Как же достали эти амбициозные новички и карьеристы!"
    w6 "Ничего не делают, только сидят в своем интернете."
    img 20315
    with diss
    w6 "А как надо сделать какой-то сложный отчет дак Грета, сделай пожалуйста..."
    mt "Боже! Какое занудство!"
#    mt "Пожалуй, пойду к себе в кабинет..."
    return

label gallery_20317:
    music Groove2_85
    img 20317
    with fade
    mt "Кажется, я ее где-то видела..."
    mt "Может быть она когда-то приходила ко мне на кастинг..."
    mt "Или нет, она работала официанткой в моем любимом ресторане..."
    mt "И где я ее могла видеть?"
    img 20318
    with diss
    if shopVisitorStage10 >= 3:
        music Power_Bots_Loop
        mt "Черт! Она же была покупательницей в этом ужасном магазине, где я работала манекеном!"
        music Groove2_85
        mt "Кошмар, надеюсь она меня не узнает..."
        mt "Хотя... Не думаю что можно связать Монику Бакфетт с какой-то продавщицей в трущобах..."
        mt "В любом случае, надо поменьше общаться с ней. Вдруг она, все-же, узнает меня..."
    else:
        mt "Кажется, я ее видела в трущобах..."
        mt "Но и она меня могла видеть..."
    mt "Лучше держаться от нее подальше."
    return

label gallery_20320:
#    m "Послушай, думаю ты знаешь, кто я, а вот я никого тут не знаю."
#    m ""
    music Groove2_85
    img 20319
    with fade
    m "Мне это не очень интересно. Я здесь не надолго."
    m "Но, все-же, расскажи мне про работников этого отдела."
    img 20320
    w5 "Миссис Бакфет! Вы сегодня прекрасно выглядите и обратились как раз по адресу."
    img 20321
    with diss
    m "Я всегда хорошо выгляжу. Не подлизывайся к Боссу, тебе это не поможет."
    m "Итак?"
    img 20322
    with diss
    w5 "Вон там сидит Марта. Она занимается отчетами."
    img 20323
    with diss
    w5 "Близняшки Элла и Эмма.. Они тоже делают отчеты."
    w5 "Хотя что говорить... Мы все тут делаем отчеты."
    img 20324
    with diss
    w5 "Эту толстуху зовут Грета. Она работает тут дольше всех."
    img 20325
    with diss
    w5 "Вон там сидит Лин. Она у нас недавно."
    img 20326
    with diss
    w5 "Нашего системного администратора ты, возможно, видела. Я даже не знаю как его зовут."
    img 20328
    with diss
    w5 "Ну и наконец Я! Самый компетентный сотрудник в этом отделе и, думаю, скоро его глава."
    w5 "Меня зовут Джон."
    mt "Ну и мерзкий же ты тип, Джон."
    img 20329
    with fade
    m "Я поняла, возвращайся к работе!"
    return

label gallery_20333:
    music Sneaky_Snitch
    img 20330
    with fadelong
    w1 "Миссис Бакфетт... Можно?"
    w1 "Я принесла отчет."
    menu:
        "Да, проходи.":
            m "Да, проходи."
            img 20332
            with diss
            m "Напомни, как тебя зовут?"
            w1 "Я...Я Марта."
            music Groove2_85
            img 20333
            with fade
            m "Марта... Ты же понимаешь, что твоя работа очень важна и я на тебя надеюсь?"
            w1 "Да... Мэм..."
            m "Отлично. А теперь положи бумаги на стол и можешь идти."
            img 20334
            with diss
            w1 "Да, хорошо..."
            sound snd_folder_drop
            img 20335
            with diss
            mt "Серая мышь..."
            return
        "Я занята!":
            music Pyro_Flow
            img 20331
            with fade
            m "Ты что, не видишь, я занята!"
            w1 "Простите..."
            m "Положи отчет на стол и выметайся!"
            img 20334
            with diss
            w1 "Хорошо..."
            sound snd_folder_drop
            img 20335
            with fade
            mt "Кучка никчемных идиотов..."
            return

label gallery_20339:
    music DarxieLand
    img 20336
    with fadelong
    w2 "Босс, я все проверил. Все работает стабильно."
    menu:
        "Разве тебя не учили стучаться?":
            music Groove2_85
            img 20337
            with fade
            m "Разве тебя не учили стучаться?"
            w2 "Ну... Я постучал..."
            m "Не правда! А теперь выйди из кабинета и если ты хочешь войти, постучись."
            w2 "Хорошо..."
            music stop
            sound snd_door_close1
            img black_screen
            with diss
            pause 1.0
            sound snd_door_knock
            pause 1.0
            sound snd_door_open1
            pause 0.5
            music DarxieLand
            # выыходит - стучится
            img 20338
            with fadelong
            w2 "Миссис Бакфетт, можно?"
            m "Да, заходи."
            music Groove2_85
            img 20339
            with diss
            m "Вот видишь, все просто. Ты говоришь, что у тебя все работает..."
            m "Хорошо. А теперь можешь идти."
            w2 "?!"
            m "Да, да, иди работай."
            return
        "Больше ничего.":
            img 20340
            with fade
            w2 "Могу я чем нибудь помочь?"
            m "Больше ничего. Можешь идти."
            w2 "Хорошо. Если Вам что-то понадобится, зовите."
            music Groove2_85
            img 20341
            with fade
            mt "Хм... Он ведет себя как болван."
            mt "Возможно я смогу его как-то использовать..."
            mt "Но как? Пока не знаю..."
#            mt "Хм...Возможно я смогу использовать этого болвана..."
#            mt ""
            return

label gallery_20345:
    music ZigZag
    img 20342
    with fadelong
    w3 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20343
            with fade
            w3 "Миссис Бакфетт, в офисе очень жарко, нам нужен кондиционер."
            img 20344
            m "А что, его нет?"
            img 20345
            with diss
            w3 "В этом помещении нет и никогда не было."
            music Groove2_85
            img 20346
            with fade
            m "Эту проблему очень просто решить!"
            m "Откройте окна!"
            img 20347
            with diss
            w3 "Да, но это не совсем..."
            img 20348
            with diss
            m "Отлично, а теперь иди и продолжай работать."
            img 20349
            with fade
            mt "Никчемные люди... Все время что-то требуют..."
#            mt "Да, без кондиционера работать не комфортно... Может стоит как-нибудь помочь им..."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            img 20347
            with diss
            w3 "Ладно, но у меня проблема..."
            music Groove2_85
            img 20348
            with fade
            m "Ты что, плохо слышишь!? Я сейчас занята!"
            return

label gallery_20354:
    music ZigZag
    img 20350
    with fadelong
    w4 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20351
            with fade
            w4 "Миссис Бакфетт, у меня пропал интернет."
            img 20352
            m "Окей. И чем я тебе могу помочь?"
            img 20353
            with diss
            m "Ты же знаешь, что этими проблемами занимается наш системный администратор."
            img 20354
            with fade
            m "Пухлый коротышка в очках."
            m "Так что иди к нему со своей проблемой."
            img 20355
            with diss
            w4 "Но он не хочет мне помогать."
            music Groove2_85
            img 20356
            with fade
            m "Скажи ему, что он будет уволен, если сейчас же не решит вопрос."
            img 20357
            with diss
            w4 "Хорошо, Миссис Бакфетт."
            w4 "Я передам" # улыбается

#            m "Почему?"
#            w4 "Миссис Бакфетт, мне не очень удобно об этом говорить..."
#            m "Я твой босс, ты можешь мне рассказать, ничего страшного не произойдет..."
#            w4 "Он... Он просит, чтобы я показала ему грудь... И тогда он все починит."
#            m "Я поняла."
#            # моника берет телефон, звонит админу
#            m "Чтобы в течение 30 минут у Эллы был интернет! Ты понял?"
#            w2 "Да, мем..."
#            m "Вот и все, проблема решена."
#            w4 "Спасибо, миссис Бакфет!"
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            w4 "Ладно, но у меня проблема..."
            music Pyro_Flow
            img 20356
            with fade
            m "Ты что, не понимаешь? Я сейчас занята!"
            return

label gallery_20358:
    music Sneaky_Snitch
    img 20358
    with fadelong
    w5 "Миссис Бакфетт, я бы хотел поговорить о моем повышении!"
    menu:
        "Давай поговорим.":
            img 20359
            with diss
            m "Давай поговорим."
            img 20360
            with diss
            w5 "Миссис Бакфетт, Вы же знаете, я очень ответственный и без меня этот отдел просто развалится."
            w5 "Еще эта толстуха Грета так и норовит занять мое законное место."
            w5 "И я буду Вам бесконечно благодарен если Вы..."
            music Groove2_85
            img 20361
            with fade
            m "Достаточно..."
            m "Чем чаще ты задаешь мне такие вопросы, тем дальше от тебя эта должность."
            img 20362
            with diss
            mt "И что это вообще за должность? Почему он думает, что этому отделу нужен какой-то мифический начальник кроме меня?"
            music Sneaky_Snitch
            img 20363
            with fade
            w5 "Да, понял. Ухожу. Но знайте, миссис Бакфетт, Вы всегда можете на меня расчитывать."
            return
        "Не в этой жизни.":
            music Pyro_Flow
            img 20361
            m "Повышении?!"
            m "Не сегодня. Выйди и закрой за собой дверь."
            music Sneaky_Snitch
            img 20363
            with fade
            w5 "Хорошо. Понимаю, Вы очень заняты. Ну ничего, в другой раз."
            return

label gallery_20366:
    music Sneaky_Snitch
    img 20364
    with fadelong
    w6 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20365
            w6 "Миссис Бакфетт, Я бы хотела поговорить о ситуации в нашем отделе."
            img 20366
            with diss
            w6 "Вы же наверняка знаете на ком все держится..."
            img 20367
            with diss
            w6 "А этот карьерист Джон... Как он меня достал!"
            w6 "Думаю, с Вашими менеджерскими талантами Вы понимаете, кто достоин стать главой отдела."
            music Groove2_85
            img 20368
            with fade
            m "Уж будь в этом уверена."
            m "Придет время и ты все узнаешь."
            img 20369
            with diss
            mt "Глава отдела? Как же вы мне надоели..."
            img 20370
            with fade
            m "Я тебя услышала. Ты свободна."
#            w6 "Да, спасибо миссис Бакфет. Вот кстати отчет, который я сегодня сделала."
#            m "Спасибо, можешь положить на стол."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            music Pyro_Flow
            img 20370
            with fade
            w6 "Но как же..."
            m "Я сказала завтра, я сейчас занята!"
            return

label gallery_20375:
    music Sneaky_Snitch
    img 20371
    with fadelong
    w7 "Миссис Бакфетт, можно?"
    if shopVisitorStage10 >= 3:
        music Groove2_85
        img 20372
        with fade
        mt "Она может меня узнать... Лучше не говорить с ней долго."
        mt "Думаю, лучше будет ее вежливо выпроводить."
    img 20373
    with diss
    m "Кажется, тебя зовут Лин?"
    img 20374
    w
    img 20375
    with diss
    w7 "Да, мэм."
    img 20376
    with fade
    m "Лин, я сейчас очень занята. Если ты принесла отчет, положи пожалуйста его мне на стол. Я его обязательно посмотрю."
    img 20377
    with diss
    w7 "Хорошо, Мэм."
    sound snd_folder_drop
    if shopVisitorStage10 >= 3:
        img 20378
        with fade
        w7t "(Меня не покидает мысль, что где то Я видела эту миссис Бакфетт...)"
    return

label gallery_20752:
    music Groove2_85
    img 20751
    with fade
    m "Я за твоими отчетами? Я надеюсь, они готовы?"
    w2 "Миссис Бакфетт, я системный администратор."
    m "Это очень хорошо, а теперь возьми эту флеш карту и скопируй на нее свои отчеты."
    img 20752
    w2 "Миссис Бакфетт, я не пишу отчеты, я же говорю, я системный администратор."
    w2t "Да, похоже она совсем не разбирается в этом... С таким же успехом я могу сказать, что чищу вентиляторы... Ха-ха!"
    m "Напомни, а чем ты тут вообще занимаешься ?"
    w2 "Я слежу за работой сети, компьютеров и автоматизацией различных бизнес процессов..."
    img 20753
    with diss
    w2t "И определенно буду следить за твоей красивой попой."
    m "Я поняла. Ладно, следи."
    img 20304
    with fade
    mt "Как я могла забыть... Он разбирается в компьютерах... Нужно не забывать об этом..."
    return

label gallery_20759:
    music Groove2_85
    img 20754
    with hpunch
    m "Привет. Мне нужны отчеты, которые ты сделала."
    music Loved_Up
    img 20755
    with diss
    w1 "Но... Миссис Бакфетт, простите, я еще не доделала. И мне нужно будет их проверить..."
    menu:
        "Ничего страшного.":
            img 20756
            with diss
            m "Ничего страшного. Конечно, не следует такого допускать."
            m "Ты же постараешься сделать так, чтобы такой ситуации не повторилось?"
            w1 "Я...Да, конечно..."
            pass
        "И почему же они еще не готовы?":
            img 20757
            with diss
            m "И почему же они еще не готовы?"
            w1 "..."
            m "А?"
            img 20758
            w1 "Миссис Бакфетт, я... У меня..."
            m "Ты же знаешь, какую важную работу все мы здесь делаем!"
            w1 "Обещаю Вам, я их доделаю! Сегодня же!"
            pass
    img 20759
    with diss
    m "Отлично, а пока скопируй мне все, что у тебя есть на данный момент."
    w1 "Хорошо..."
    w1 "Я все скопировала."
    img 20760
    with diss
    m "Хорошо."
    m "И не забывай, твой вклад в работу компании очень высок."
    w1 "Да, миссис Бакфетт."
    return

label gallery_20765:
    music Groove2_85
    img 20761
    with fade
    m "Здравствуй. Скопируй, пожалуйста, отчеты, которые ты сделал. Вот флеш карта."
    music Sneaky_Snitch
    img 20762
    with diss
    w5 "Я очень рад, что Вы подошли Миссис Бакфетт. Да, конечно, я сейчас."
    # берет флешку
    img 20763
    with diss
    w5 "Хотите кофе, миссис Бакфетт?"
    m "Нет."
    w5 "Жаль, если вдруг захотите, дайте знать."
    music Loved_Up
    img 20764
    with fadelong
    w
    music Sneaky_Snitch
    img 20765
    with diss
    w5 "Вот, я все скопировал Вам папку в 'Наиболее качественные отчеты', чтобы Вам было проще."
    img 20766
    mt "Да уж, что бы я делала без этой папки?"
    m "Я сообщу, если ты мне понадобишься."
    img 20767
    with diss
    w5 "Да, миссис Бакфетт, можете на меня рассчитывать в любое время."
    return

label gallery_20772:
    music Groove2_85
    img 20768
    with fade
    m "Привет. Мне нужны твои отчеты. Скопируй их мне на флеш карту."
    w6 "Да, но зачем? Все же можно отправить на электронную почту..."
    # это все слышит воркер5
    music Sneaky_Snitch
    img 20769
    with fade
    w5 "Миссис Бакфетт, не обращайте внимания на Грету. Она не понимает всю важность этого действия."
    w5 "Давайте я помогу."
    # берет флешку вставляет в комп
    img 20770
    with diss
    w5 "Грета, скопируй все свои ответы миссис Бакфетт. Я надеюсь, в них нет ошибок."
    w6t "Ах ты сволочь..."
    music Groove2_85
    img 20771
    with fade
    w6 "В отличие от твоих, они качественные!"
    # садится за комп, копирует
    music Sneaky_Snitch
    img 20772
    with diss
    w6 "Пожалуйста, миссис Бакфетт."
    m "Спасибо."
    mt "Похоже, с этими двумя надо будет что-то решать..."
    return

label gallery_20775:
    music Groove2_85
    img 20773
    with fade
    m "Я за отчетами, надеюсь, они готовы."
    music ZigZag
    img 20774
    with diss
    w3 "Да, я только кое-что проверю..."
    m "Это не обязательно. Возьми эту карту и скопируй на нее всю свою работу."
    w3 "Да, мэм."
    m "Встань, когда с тобой говорит Босс."
    img 20775
    with fade
    w3 "Мэм, могу я спросить?"
    menu:
        "Спрашивай":
            m "Да, что ты хотела?"
            w3 "В офисе жарко. Когда нам установят кондиционер?"
            mt "Понятия не имею, скорее всего никогда."
            img 20776
            with diss
            m "Я не знаю, мне надо выдать распоряжение. Нужно подождать, пока у меня будет настроение для этого."
            w3 "Да мэм, спасибо."
            pass
        "Нет":
            img 20777
            with diss
            m "Не сейчас, я занята."
            w3 "Да мэм..."
            pass
    img 20778
    with fadelong
    w3 "Все скопировалось."
    m "Хорошо."
    m "Продолжай в том же духе."
    w3 "Да, миссис Бакфетт."
    return

label gallery_20784:
    music ZigZag
    img 20779
    with fade
    m "Здравствуй. Скопируй мне свои сделанные отчеты вот сюда."
    w4t "Интересно, почему я должна их копировать на флеш карту? Уже давно ими не пользуются..."
    w4 "Хорошо. Миссис Бакфетт, а зачем это? Я ведь могу их отправить Вам на почту."
    img 20780
    with diss
    mt "На самом деле, мне твои отчеты неинтересны ни на почте, ни на карте..."
    mt "Гребаный Биф!"
    img 20781
    with fade
    m "Сразу видно, ты ничего не понимаешь в безопасности. Это хороший способ!"
    img 20782
    with diss
    w3t "А у нашей начальницы отличная задница..."
    img 20783
    with diss
    w3t "И сиськи ничего такие, но мои определенно больше!"
    img 20784
    with fade
    w4 "Но что если на флеш карте окажется вирус, или Вы ее потеряете."
    m "Я? Я ее не потеряю."
    img 20785
    with diss
    mt "А она не такая и глупая... Или делает вид..."
    mt "Все-равно она не умнее меня!"
    return

label gallery_20788:
    music Groove2_85
    img 20786
    with fade
    m "Вот флеш карта, скопируй сюда сделанные тобою отчеты."
    img 20787
    with diss
    if shopVisitorStage10 >= 3:
        mt "Хоть бы она меня не узнала... Она могла видеть меня в трущобах..."
    w7 "Хорошо."
    if shopVisitorStage10 >= 3:
        w7t "Меня не покидает чувство, что я где-то видела Миссис Бакфетт. И определенно не здесь."
        # берет флешку cадится
        img 20788
        with diss
        w7t "Может быть в каком-то журнале..."
        w7t "Возможно..."
        w7t "Хотя нет!"
        img 20789
        with diss
        m "Эй! О чем задумалась? Я жду твои отчеты!"
        w7 "Да, мэм, копируется..."
        w7t "Черт, сбила с мысли..."
    img 20790
    with fadelong
    w7 "Готово."
    m "Хорошо, продолжай работу."
    return

############ Pub 1############

label gallery_9638:
    # Моника моет посуду
    music2 stop

    music stop
    sound snd_washing_dishes
    $ monicaWashingDishesImages = [9637, 9638, 9639]
    call showRandomImagesFirstFade(monicaWashingDishesImages, 1) from _rcall_showRandomImagesFirstFade
    $ monicaWashingDishesImages2 = [9640, 9641, 9642]
    call showRandomImagesFirstFade(monicaWashingDishesImages2, 1) from _rcall_showRandomImagesFirstFade_1
    $ rand1 = rand(1,4)
    if rand1 == 1:
        mt "Никогда бы не подумала что буду мыть посуду в подобной дыре..."
    if rand1 == 2:
        mt "Не могу поверить что я делаю это..."
    if rand1 == 3:
        mt "У меня ощущение что все это сон..."
    if rand1 == 4:
        mt "Мне надо определенно что-то менять в этой ситуации... И как можно быстрее!"

    return

label gallery_9646: # Бармен

    # Клик на бармена
    # Бармен лапает Монику
    music Hidden_Agenda
    img 9643
    with fade
    w
    img 9644
    with Dissolve(0.3)
    w
    sound Jump2
    img 9645
    with Dissolve(0.3)
    w
    mt "Черт! Кажется, этот извращенец Джо пытается меня незаметно лапать!"
    menu:
        "Не обращать внимание...":
            sound snd_washing_dishes
            music Loved_Up
            img 9646
            with Dissolve(0.3)
            w
            img 9647
            with Dissolve(0.3)
            w
            img 9648
            with Dissolve(0.3)
            w
            music Groove2_85

#        "Не обращать внимание... (low corruption, required [monicaWashHoldJoeCorruption]) (disabled)" if corruption < monicaWashHoldJoeCorruption:
#            pass
        "Прекратить это!":
            music Power_Bots_Loop
            img 9649
            with fade
            m "Джо! Ты что-то хотел взять здесь?"
            joe "Да, [monica_pub_name]!"
            "Я хочу взять чистую пивную кружку!"

    img 9650
    with fadelong
    mt "Это место - действительно Shiny Hole с извращенцами!"
    return

label gallery_9654: # Барменша
    # Клик на барменшу
    # Барменша лапает Монику
    music Hidden_Agenda
    img 9651
    with fade
    w
    img 9652
    with Dissolve(0.3)
    w
    img 9653
    with Dissolve(0.3)
    w
    sound Jump2
    img 9654
    with Dissolve(0.3)
    w

    mt "Черт! Эшли меня трогает за зад?!"
    menu:
        "Не обращать внимание...":
            sound snd_washing_dishes
            music Loved_Up
            img 9655
            with Dissolve(0.3)
            w
            img 9656
            with Dissolve(0.3)
            w
            img 9657
            with Dissolve(0.3)
            w

            music Groove2_85

#        "Не обращать внимание... (low corruption, required [monicaWashHoldAshleyCorruption]) (disabled)" if corruption < monicaWashHoldAshleyCorruption:
#            pass
        "Прекратить это!":
            music Power_Bots_Loop
            img 9658
            with fade
            m "Эшли! Ты что-то хотела взять здесь?"
            ashley "Я слежу чтобы ты лучше мыла посуду!"
            "Везде грязь!"

    img 9650
    with fadelong
    mt "О БОЖЕ!!!"
    "ЗА ЧТО МНЕ ЭТО?!"
    mt "Это место - действительно Shiny Hole с извращенцами!"
    return


label gallery_9668:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9668
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_molly == True and obj_name == "Pub_StripteaseGirl1":
        call gallery_9667_1() from _rcall_gallery_9667_1
    return

label gallery_9669:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9669
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_molly == True and obj_name == "Pub_StripteaseGirl1":
        call gallery_9667_1() from _rcall_gallery_9667_1_1
    return

label gallery_9670:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9670
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_molly == True and obj_name == "Pub_StripteaseGirl1":
        call gallery_9667_1() from _rcall_gallery_9667_1_2
    return


label gallery_9671:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9671
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_molly == True and obj_name == "Pub_StripteaseGirl1":
        call gallery_9667_1() from _rcall_gallery_9667_1_3
    return


label gallery_9664:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9664
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_claire == True and obj_name == "Pub_StripteaseGirl2":
        call gallery_9667_2() from _rcall_gallery_9667_2
    return


label gallery_9665:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9665
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_claire == True and obj_name == "Pub_StripteaseGirl2":
        call gallery_9667_2() from _rcall_gallery_9667_2_1
    return

label gallery_9666:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9666
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_claire == True and obj_name == "Pub_StripteaseGirl2":
        call gallery_9667_2() from _rcall_gallery_9667_2_2
    return

label gallery_9667:
    music2 pub_noise1_low
    music RocknRoll_loop
    img 9667
    with fadelong
    mt "Эти девушки совсем не уважают себя!"
    "Как можно делать подобное у всех на виду?!"
    if ep29_quests_pub_monica_knows_claire == True and obj_name == "Pub_StripteaseGirl2":
        call gallery_9667_2() from _rcall_gallery_9667_2_3
    return


label gallery_9667_1:
    mt "Молли. Считает себя королевой сцены Shiny Hole..."
    mt "Звезда трущоб. Фи!"
    return

label gallery_9667_2:
    mt "Эта Клэр могла бы быть моделью журнала..."
    mt "А не танцевать в пабе перед толпой пьяных неудачников!"
    return


label gallery_20482:
    music2 stop
    music Groove2_85
    img 20462
    with fadelong
    ashley "Привет, [monica_pub_name]!"
    img 20461
    with diss
    ashley "Ты пришла, чтобы мыть посуду?"
    img 20463
    with diss
    m "Нет, я хочу заказать еду!"
    img 20464
    with fade
    ashley "Правда?"
    ashley "И что же ты хочешь заказать?"
    img 20465
    with diss
    m "Я хочу заказать..."
    $ menu_price = [pubSphagettiPrice]

    $ choose_var = 0
    menu:
        "Спагетти.":
            $ choose_var = 2
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Спагетти."
            $ images_list = [20474, 20479, 20482]
        "Уйти.":
            img 20470
            with fade
            m "Я передумала."
            img 20471
            with diss
            ashley "Ах, [monica_pub_name], у тебя нет денег!"
            ashley "Но ведь ты посудомойка. Ты всегда можешь помыть посуду!"
            img 20472
            with diss
            mt "!!!"
            # на улице
            return
    img 20467
    with diss
    joe "А выпивку?"
    img 20468
    m "Спасибо, не надо!"
    img 20469
    with fade
    ashley "Хорошо, присаживайся за стол."
    ashley "Я сейчас принесу."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_plates2
    $ pubFoodHistory.append(choose_var)
    music Groove2_85
    img images_list[0]
    with fadelong
    ashley "Но ты могла бы не тратить деньги."
    ashley "Эту еду легко заработать посудомойкой."

    img 20476
    with diss
    mt "!!!"

    if monicaPubWashingDishesCount > 5:
        # если часто мыла
        img images_list[1]
        with fade
        ashley "К тому же, я уже привыкла что ты моешь посуду."
        ashley "Мне стало как-то лень заниматься этим."
        img 20480
        with diss
        m "Спасибо, Эшли."
        m "Сегодня я не хочу... мыть посуду..."
        img 20481
        with diss
        ashley "Хорошо, [monica_pub_name], если надумаешь, приходи..."
        #
    img images_list[2]
    with fade
    mt "Эшли готовит отвратительно."
    mt "Это место - действительно дыра."
    music stop
    sound snd_gulp
    img black_screen
    with diss
    mt "Но это нормальная еда, а не пирожные с заправки..."
    return

label gallery_20483:
    music2 stop
    music Groove2_85
    img 20462
    with fadelong
    ashley "Привет, [monica_pub_name]!"
    img 20461
    with diss
    ashley "Ты пришла, чтобы мыть посуду?"
    img 20463
    with diss
    m "Нет, я хочу заказать еду!"
    img 20464
    with fade
    ashley "Правда?"
    ashley "И что же ты хочешь заказать?"
    img 20465
    with diss
    m "Я хочу заказать..."
    $ menu_price = [pubShinyBurger]

    $ choose_var = 0
    menu:
        "Shiny Бургер.":
            $ choose_var = 1
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Shiny Бургер."
            $ images_list = [20473, 20478, 20483]
        "Уйти.":
            img 20470
            with fade
            m "Я передумала."
            img 20471
            with diss
            ashley "Ах, [monica_pub_name], у тебя нет денег!"
            ashley "Но ведь ты посудомойка. Ты всегда можешь помыть посуду!"
            img 20472
            with diss
            mt "!!!"
            # на улице
            return
    img 20467
    with diss
    joe "А выпивку?"
    img 20468
    m "Спасибо, не надо!"
    img 20469
    with fade
    ashley "Хорошо, присаживайся за стол."
    ashley "Я сейчас принесу."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_plates2
    $ pubFoodHistory.append(choose_var)
    music Groove2_85
    img images_list[0]
    with fadelong
    ashley "Но ты могла бы не тратить деньги."
    ashley "Эту еду легко заработать посудомойкой."

    img 20476
    with diss
    mt "!!!"

    if monicaPubWashingDishesCount > 5:
        # если часто мыла
        img images_list[1]
        with fade
        ashley "К тому же, я уже привыкла что ты моешь посуду."
        ashley "Мне стало как-то лень заниматься этим."
        img 20480
        with diss
        m "Спасибо, Эшли."
        m "Сегодня я не хочу... мыть посуду..."
        img 20481
        with diss
        ashley "Хорошо, [monica_pub_name], если надумаешь, приходи..."
        #
    img images_list[2]
    with fade
    mt "Эшли готовит отвратительно."
    mt "Это место - действительно дыра."
    music stop
    sound snd_gulp
    img black_screen
    with diss
    mt "Но это нормальная еда, а не пирожные с заправки..."
    return

label gallery_20484:
    music2 stop
    music Groove2_85
    img 20462
    with fadelong
    ashley "Привет, [monica_pub_name]!"
    img 20461
    with diss
    ashley "Ты пришла, чтобы мыть посуду?"
    img 20463
    with diss
    m "Нет, я хочу заказать еду!"
    img 20464
    with fade
    ashley "Правда?"
    ashley "И что же ты хочешь заказать?"
    img 20465
    with diss
    m "Я хочу заказать..."
    $ menu_price = [pubSoupPrice]

    $ choose_var = 0
    menu:
        "Суп харчо.":

            $ choose_var = 3
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Суп харчо."
            $ images_list = [20475, 20477, 20484]
        "Уйти.":
            img 20470
            with fade
            m "Я передумала."
            img 20471
            with diss
            ashley "Ах, [monica_pub_name], у тебя нет денег!"
            ashley "Но ведь ты посудомойка. Ты всегда можешь помыть посуду!"
            img 20472
            with diss
            mt "!!!"

            # на улице
            return
    img 20467
    with diss
    joe "А выпивку?"
    img 20468
    m "Спасибо, не надо!"
    img 20469
    with fade
    ashley "Хорошо, присаживайся за стол."
    ashley "Я сейчас принесу."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_plates2
    $ pubFoodHistory.append(choose_var)
    music Groove2_85
    img images_list[0]
    with fadelong
    ashley "Но ты могла бы не тратить деньги."
    ashley "Эту еду легко заработать посудомойкой."

    img 20476
    with diss
    mt "!!!"

    if monicaPubWashingDishesCount > 5:
        # если часто мыла
        img images_list[1]
        with fade
        ashley "К тому же, я уже привыкла что ты моешь посуду."
        ashley "Мне стало как-то лень заниматься этим."
        img 20480
        with diss
        m "Спасибо, Эшли."
        m "Сегодня я не хочу... мыть посуду..."
        img 20481
        with diss
        ashley "Хорошо, [monica_pub_name], если надумаешь, приходи..."
        #
    img images_list[2]
    with fade
    mt "Эшли готовит отвратительно."
    mt "Это место - действительно дыра."
    music stop
    sound snd_gulp
    img black_screen
    with diss
    mt "Но это нормальная еда, а не пирожные с заправки..."
    return



label gallery_20985:
#    menu:
#        "Спросить о повышении.":
#            pass
# Моника спрашивает, можно-ли ее повысить, чтобы она зарабатывала какие-то деньги?
    music2 pub_noise1_low
    music Groove2_85
    img 20953
    with fadelong
    m "Эшли..."
    m "Можно-ли попросить дать мне еще другую работу, чтобы я..."
    m "Чтобы я зарабатывала какие-то деньги здесь?"
# Далее:
# Если ур у Эшли и Джо < 1
    if char_info["Bartender_Waitress"]["level"] < 2 and char_info["Bartender"]["level"] < 2:
        img 20954
        with fade
        ashley "Хммм..."
        ashley "Если честно, я не уверена в тебе [monica_pub_name]."
        ashley "Поработай пока посудомойкой!"
        img 20955
        with diss
        m "!!!"
        help "Требуется отношение с Джо, либо Эшли выше 1."
        return

# Если у Эшли ур.1, то она говорит что не уверена в ней, но Джо отзывается о ней хорошо (показан хитрый Джо)
    if char_info["Bartender_Waitress"]["level"] < 2:
        img 20956
        with fade
        ashley "Хммм..."
        ashley "Если честно, я не уверена в тебе [monica_pub_name]."
        ashley "Но Джо отзывается хорошо о тебе."
        joe "..." # хитрый
    else:
    # Если у Эшли ур.2, то она говорит что уже успела разглядеть ее попку
        img 20957
        with fade
        ashley "Хммм..."
        ashley "Если честно, то я уже успела разглядеть твою попку, [monica_pub_name]."

# И, пока она работает, никто не пришел проверять ее из миграционной полиции или санитарного контроля.
# Также после ее мытья посуды не отравился ни один клиент.
# И Эшли было бы интересно посмотреть на ее голую попку, которая будет крутиться на пилоне.
# Поэтому она разрешает ей танцевать здесь, но трахаться с клиентами пока нельзя, хотя я знаю что ты за этим пришла сюда.
    img 20958
    with diss
    ashley "И, пока ты работаешь, никто не пришел проверять тебя из миграционной полиции или санитарного контроля."
    img 20959
    with diss
    m "..."
    img 20960
    with fade
    ashley "Также, после твоего мытья посуды не отравился ни один клиент."
    music Loved_Up
    img 20961
    with diss
    ashley "Так что мне было бы интересно посмотреть на твою голую попку, которая будет крутиться на пилоне."
    ashley "Поэтому, так уж и быть."
    ashley "Я разрешаю тебе танцевать здесь..."

    music Groove2_85
    img 20962
    with fade
    ashley "Но трахаться с клиентами пока нельзя!"
    ashley "Хотя я знаю что ты за этим пришла сюда."
# Моника в шоке. Отвечает что не собирается танцевать здесь в голом виде!
# Эшли удивленно спрашивает а что же она тогда хочет? О каком повышении говорит?
# Джо говорит что видишь Эшли, она приличная девушка, пусть она работает у нас официанткой!
# Эшли спрашивает у Джо что ты решил отдать мою работу Мэрилин?
    music Power_Bots_Loop
    img 20963
    with vpunch
    m "!!!"
    m "Я не собираюсь танцевать здесь в голом виде!"
    music Groove2_85
    img 20964
    with fade
    ashley "А что же ты тогда хочешь?"
    ashley "О каком повышении ты говоришь?"
    joe "Видишь, Эшли? [monica_pub_name] приличная девушка."
    joe "Пусть она работает у нас официанткой!"
    music Power_Bots_Loop
    img 20965
    with diss
    ashley "Джо, ты что, решил отдать мою работу [monica_pub_name]?!"
# Может быть ты на ней женишься вместо меня, Джо?!
# И будешь сам платить кредиты за это заведение?!
# Джо улыбается. Нет, Эшли, я не это имел ввиду.
# У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов, правда, Мерилин?
    img 20966
    with diss
    ashley "Может быть ты на ней женишься вместо меня, Джо?!"
    ashley "И будешь сам платить кредиты за это заведение?!"
    img 20967
    with fade
    joe "Нет, Эшли! Я не это имел ввиду!"
    joe "У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов."
    music Hidden_Agenda
    img 20968
    with diss
    joe "Правда, [monica_pub_name]?"

# Моника кривится
# Уверен, что обладательнице такой попки будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!
# Она ведь работает у нас неофициально! Скажем, отдавать ей 10 процентов от того что ей дадут клиенты.
# И ей необязательно платить основную зарплату, ей вполне хватит остатка от чаевых.
# Ведь так, Мэрилин?
    img 20969
    with diss
    mt "!!!" # Моника кривится
    img 20970
    with fade
    joe "Уверен, что обладательнице такой фигуры будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!"
    img 20971
    with hpunch
    mt "ЧТО?!"
    img 20972
    with fade
    joe "Она ведь работает у нас неофициально!"
    joe "Можно, скажем, отдавать ей 30 процентов от того, что ей дадут клиенты."
    joe "И нам необязательно платить ей основную зарплату."
    joe "Ей вполне хватит остатка от чаевых."
    img 20973
    with diss
    joe "Ведь так, [monica_pub_name]?"
# Моника кривится
# А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару.
# Эшли задумалась. Т.е., Джо, ты предлагаешь отправить Мэрилин к этим пьяницам и не платить ей деньги?
# Платить, но только 10 процентов от чаевых. Мы ничем не рискуем, Эшли! Нет зарплаты - не нужны документы!
# Эшли спрашивает: а если она нагрубит клиенту? Или заберет чаевые себе?
# Джо говорит что Мэрилин выглядит как порядочная девушка и не будет брать себе лишнего!
# Эшли спрашивает у Моники: Мэрилин, и ты согласна на такую работу?
    img 20974
    m "!!!" # Моника кривится
    img 20975
    with fade
    joe "А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару."
    music Groove2_85
    img 20976
    with fade
    ashley "..."
    ashley "То есть, Джо, ты предлагаешь отправить [monica_pub_name] к этим пьяницам и не платить ей деньги?"
    img 20977
    joe "Платить, но только 30 процентов от чаевых. Мы ничем не рискуем, Эшли!"
    joe "Нет зарплаты - не нужны документы! Не страшны никакие проверки!"
    img 20978
    with diss
    ashley "А если [monica_pub_name] нагрубит клиенту?"
    ashley "Или заберет чаевые себе?"
    img 20979
    m "!!!"
    img 20980
    with fade
    joe "[monica_pub_name] выглядит как порядочная девушка и не будет брать себе лишнего."
    img 20981
    with diss
    ashley "..."
    ashley "Ну, не знаю..."
    img 20982
    with diss
    ashley "[monica_pub_name], и ты согласна на такую работу?"

# Выбор:
# Я не согласна работать за такие копейки!
# Моника говорит что не согласна работать за такие копейки. (уходя)
# Джо говорит что если надумает, то пусть приходит
    menu:
        "Я не согласна работать за такие копейки!":
            music Power_Bots_Loop
            img 20983
            with fade
            m "Я не согласна работать за такие копейки!"
            img 20984
            with diss
            joe "[monica_pub_name], если надумаешь, то приходи." # подмигивает
            return
        "Согласиться.":
            pass
# Согласиться.
# Моника говорит что согласна работать, ей нужна хоть какая-то работа.
# Что не будет грубить клиентам, будет общаться с ними вежливо.
# И что будет отдавать чаевые им.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 20985
    with fadelong
    m "Я..."
    m "Я согласна работать. Мне нужна хоть какая-то работа."
    m "Я обещаю что не буду грубить клиентам, а буду обращаться с ними вежливо."
    img 20986
    with diss
    ashley "..."
    img 20987
    with diss
    m "И буду отдавать чаевые Вам..."
# Эшли говорит что хорошо, ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!
# Здесь не бордель! И она не потерпит официантку, которая будет вести себя как шлюха!
# Моника отвечает что Эшли может не беспокоиться, она не будет выходить за рамки рабочих обязанностей.
    music Groove2_85
    img 20988
    with fade
    ashley "Ну хорошо. Ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!"
    ashley "Здесь не бордель!"
    ashley "И я не потерплю официантку, которая будет вести себя как шлюха!"
    img 20989
    with diss
    m "Эшли, Вы можете не беспокоиться."
    m "Я не буду выходить за рамки рабочих обязанностей."
# Моника думает что ей с трудом вериться что она вообще ведет такой диалог!
# Она, Моника Бакфетт! И говорит такие слова!
# Утешает только то, что ее считают здесь Мерилин, а это значит она в этом месте не имеет ничего общего с Моникой Бакфетт.
# Иначе, она не смогла бы согласиться на такое.
    music RnB3_65
    img 20990
    with fade
    mt "О БОЖЕ!"
    mt "Мне с трудом вериться в то что я вообще такое говорю!"
    mt "Я! Моника Бакфетт!"
    mt "И говорю такие слова!"
    img 20991
    with diss
    mt "..."
    mt "Утешает только то, что меня здесь считают [monica_pub_name]."
    mt "А это значит, что в этом месте я не имею ничего общего с Моникой Бакфетт."
    mt "Но мне не стоит забывать кто Я!"
    mt "В конце концов, мне еще предстоит долгая жизнь, когда я верну свое положение назад..."
#
# Эшли говорит Мэрилин, чтобы та одевала рабочую униформу и шла работать.
#
    music Groove2_85
    with vpunch
    ashley "[monica_pub_name], ты меня слышишь?!"
    img 20992
    with fade
    m "А?" # оборачивается
    img 20993
    with diss
    ashley "[monica_pub_name], ты можешь одевать рабочую униформу и идти работать."
    return

label gallery_20996:
# При клике на барменов, Моника говорит что закончила работу и вот чаевые.
# Эшли дает ей 10 процентов и говорит приходить работать еще.
    music2 pub_noise1_low
    music Groove2_85
    img 20995
    with fadelong
    m "Эшли, я закончила работу."

    if pubMonicaWaitressTips == 0:
        m "Мне никто не дал чевых сегодня..."
    else:
        m "Вот чаевые, которые я смогла получить..."

    # если есть чаевые
        img 20996
        with diss
        ashley "Хорошо. Вот твои тридцать процентов."
        ashley "Завтра приходи работать еще."

    # если нет чаевых
#    img 20995
#    m "Мне никто не дал чевых сегодня..."
    return

label gallery_14208:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14203
    with fadelong
    mt "Надо пересилить себя..."
    m "Что будете заказывать?"
    img 14202
    with diss
    customer1 "Вообще-то я ничего не хотел, но теперь думаю, что что-то закажу."
    customer1t "И откуда этот говнюк Джо достал такую красотку?"
    customer1 "Как тебя зовут?"
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14204
    with fade
    customer1 "Отлично, [monica_pub_name]"
    customer1 "Думаю, ты тут для того, чтобы заработать, так?"
    img 14205
    with diss
    m "Ну, да..."
    mt "Надо быть осторожнее с этими пьяницами..."
    img 14206
    with fade
    customer1 "Я так и думал. Вообще, чтобы получать хорошие чаевые, нужно как минимум быть вежливой."
    customer1 "Например ты должна была сказать:"
    img 14207
    customer1 "Здравствуйте, меня зовут [monica_pub_name]..."
    customer1 "Понятно?"
    img 14208
    m "Да."
    img 14209
    with diss
    mt "Да кем он себя возомнил?"
    mt "Очередной придурок..."
    img 14210
    with fade
    customer1 "Хорошо. Думаю, в следующий раз ты будешь более вежливой. Кстати, я передумал делать заказ."
    img 14211
    with diss
    mt "Что за урод? Только зря потратила время..."
    return

label gallery_14219:
    music Hidden_Agenda
    sound highheels_short_walk

    img 14212
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer1_dance_comment_stage == 1:
        customer1 "Ты меня пытаешься надурить, детка."
        customer1 "Ты танцуешь здесь иногда у пилона!"
        m "Нет. Я же говорила, что я просто официантка..."
        customer1 "Что-то я тебе не верю..."
        mt "Да мне какая разница, веришь ты мне или нет!"
        mt "Деревенщина!"

    if monicaStartedStripDanceFlag == True and customer1_dance_comment_stage == 0:
        customer1 "А не тебя я видел виляющей попой у пилона?"
        m "Нет, Вы меня с кем-то путаете."
        m "Я работаю здесь официанткой..."
        customer1 "Только официанткой?"
        m "Еще... Еще я мою посуду..."

    #

    m "Что будете заказывать?"
    img 14213
    customer1 "Ну нет, разве я так тебя учил?"
    customer1 "Будь вежливой, скажи как тебя зовут..."
    img 14214
    menu:
        "Быть вежливой." if bitchmeterValue <= maxBitchness / 2:
            img 14215
            with fade
            mt "Насколько знаю, официантки ведут себя вежливо."
            mt "Попытаюсь притвориться, насколько у меня хватит сил..."
#            mt "Возможно, так правильнее, я совсем не знаю как работают официантки."
            img 14216
            with diss
            m "Здравствуйте, меня зовут [monica_pub_name]..."
            img 14217
            with fade
            customer1 "Отлично, [monica_pub_name]."
            customer1 "А теперь, [monica_pub_name], принеси мне пива."
            img 14218
            with diss
            m "Хорошо."
            # уходит, приносит
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Hidden_Agenda
            sound snd_plates1
            img 14219
            with fade
            w
            sound snd_beer_table
            img 14220
            with diss
            w
            img 14221
            with diss
            customer1 "Запомни, быть хорошей официанткой очень сложно. Некоторые получают по 100 долларов чаевых за заказ. А пока держи..."
            # дает 0.25
            img 14209
            with fade
            mt "Четвертак? Сколько же бокалов я должна принести, чтобы ты дал мне 100 долларов?"
#            if monicaBitch == True:
            mt "Урод..."
            return
        "Быть вежливой. (Моника недостаточно приличная) (disabled)" if bitchmeterValue > maxBitchness / 2:
            pass
        "Отказаться.":
            music Groove2_85
            img 14222
            with fade
            mt "Я не собираюсь слушаться этого деревенщину!"
            # развернуться и уйти
            sound highheels_short_walk
            img 14223
            with diss
            customer1 "Эй, ты куда?"
    return

label gallery_14231:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14225
    with fadelong
    m "Что будете заказывать?"
    img 14224
    with diss
    customer2 "Новенькая?"
    # смотрит на монику
    music Groove2_85
    img 14226
    with fade
    customer2 "Ну что сказать: нормально."
    customer2 "И откуда же ты приехала в нашу дыру?"
    img 14227
    mt "Я ни откуда не приезжала! Я просто живу в тех районах, куда такие как ты не заходят."
    img 14228
    with diss
    m "Я из этого города."
    img 14229
    with fade
    customer2 "Из этого говоришь? Я знаю всех в этом районе и ты тут недавно..."
    customer2 "Думаешь, наше знакомство лучше начать с обмана?"
    img 14230
    mt "Думаю, лучше соврать..."
    img 14231
    with diss
    m "Да, Вы правы. Я приехала недавно на заработки."
    img 14232
    with fade
    customer2 "Да, это похоже на правду."
    customer2 "И ты, похоже не из городских, иначе что тебе тут делать?"
    customer2 "Похоже, ты из какой-то деревни, коих тысячи."
    img 14233
    with diss
    mt "Из деревни здесь только ты..."
    if monicaBitch == True:
        mt "Урод..."
    img 14234
    with fade
    customer2 "Ладно, девочка, вот тебе полбакса и принеси мне пиво. Считай, это в честь первого знакомства."
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14235
    with fade
    w
    sound snd_plates1
    img 14236
    with diss
    w
    sound snd_beer_table
    img 14237
    with diss
    m "Вот, пожалуйста."
    img 14238
    with fade
    customer2 "Спасибо, можешь идти. Кстати, у тебя большой потенциал, ха-ха-ха. Буду ждать тебя на сцене."
    img 14239
    with diss
    mt "Не дождешься..."
    return

label gallery_14247:
    music Hidden_Agenda
    sound highheels_short_walk

    img 14240
    with fade

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer2_dance_comment_stage == 1:
        customer2 "Эй, я видел тебя на сцене! Это точно была ты!"
        m "Боюсь, Вы ошиблись..."
        customer2 "Не-а! Папочка не ошибается никогда!"
        mt "Чего он прицепился ко мне!!!"
        m "Я не танцую на сцене. Возможно, танцовщица просто немного похожа на меня..."
        customer2 "Да? Хммм... Ладно, я присмотрюсь внимательнее в следующий раз."
        m "Я могу идти?"


    if monicaStartedStripDanceFlag == True and customer2_dance_comment_stage == 0:
        customer2 "О-о-о-о! Ты же тут на сцене танцуешь!"
        customer2 "Решила спуститься к папочке? Аха-ха!"
        m "Нет, Вы меня с кем-то путаете."
        m "Я работаю здесь официанткой..."
        customer2 "Папочку нехорошо обманывать!"
        m "Я не обманываю..."
        customer2 "Ой, да ладно тебе!!!"
        m "Вы что-то будете заказывать? Или я могу идти?"

    #

    customer2 "Эй, официантка! Мне еще пива! Кстати, как тебя зовут?"
    # если не первый раз
    if get_pub_visitor_visits(obj_name) > 2:
        customer2 "Я все время забываю!"
    img 14241
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14242
    with fade
    customer2 "И постарайся успеть, пока я не допил свой бокал!"
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14243
    with fade
    w
    sound snd_plates1
    img 14244
    with diss
    w
    sound snd_beer_table
    img 14245
    with diss
    m "Ваше пиво."
    music Groove2_85
    img 14246
    with fade
    customer2 "Ага, могла бы и побыстрее, хотя все вы, деревенщины медлительные."
    img 14247
    with diss
    m "Вообще-то я не из деревни."
    img 14248
    with fade
    customer2 "Ну да, рассказывай. Если бы ты была не из деревни, тебя бы здесь не было!"
    customer2 "Свободна! И подходи ко мне время от времени, я быстро пью."
    customer2 "И, если будешь хорошо работать, может и заработаешь..."
    img 14239
    with diss
    mt "Да что ты знаешь про меня? Неудачник!"
    return

label gallery_14254:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14249
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 1:
        customer3 "А, это ты?"
        customer3 "Пойдем в приват?"
        m "Я не танцую. Тем более, приват!"
        customer3 "А если я тебе щедро заплачу?"
        mt "Таким неудачникам, как ты, можно только мечтать обо мне."
        mt "И не только неудачникам... Вообще всем!"
        m "Вы меня с кем-то путаете."
        customer3 "Я спрошу у Джо..."
        mt "!!!"

    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 0:
        customer3 "Твоя задница со сцены смотрится отлично."
        m "Вы меня с кем-то путаете."
        m "Я просто официантка..."
        customer3 "Я хорошо запоминаю задницы. И твою я отлично помню."
        m "Я не танцую здесь на сцене."
        customer3 "Можешь дальше врать, мне все равно."
        mt "!!!"
        mt "Он что о себе возомнил?!"

    #

    m "Вам что-нибудь принести?"
    img 14250
    with diss
    customer3 "Скучно мне..."
    img 14251
    with diss
    m "Может быть пиво?"
    img 14252
    with fade
    customer3 "Да ну его..."
    customer3 "Мне все надоело... Стриптизерши одни и те же изо дня в день, скучно..."
    customer3 "Но ты тут недавно... Как тебя зовут?"
    img 14253
    with diss
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14254
    with fade
    customer3 "Ага, ну и ладно, я все равно не запомню..."
    customer3 "Я вообще не запоминаю имена женщин, я запоминаю их жопы. И твою я запомнил!"
    customer3 "Как насчет танца?"
    img 14255
    with diss
    menu:
        "Не сегодня.":
            img 14256
            with fade
            m "Я официатка, стриптизом занимаются другие."
            img 14257
            with diss
            customer3 "Да знаю я, что другие. Но их я уже видел не один раз..."
            customer3 "Ладно, проваливай, никакого толку от тебя."
            img 14258
            with diss
            mt "Какого черта ты тут вообще сидишь, если ничего не заказываешь?"
            return
        "Я что, похожа на стриптизершу?":
            music Power_Bots_Loop
            img 14259
            with fade
            m "Я что, похожа на стриптизершу?"
            m "Даже не вздумай меня спрашивать о таком!"
            img 14260
            with diss
            customer4 "Мда, скучно... А ты еще и грубиянка... Думаю, стоит рассказать об этом Джо."
            customer4 "Или не стоит... Что-то совсем лениво."
            customer4 "Иди отсюда! Клиенты ждут!"
            img 14258
            with diss
            mt "Козел!"
    return

label gallery_14268:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14261
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    music Groove2_85
    img 14262
    with vpunch
    customer3 "Ого! Вот это дамочка!"
    # смотрит на монику
    img 14263
    with fade
    customer3 "У тебя должна быть прекрасная попка!"
    customer3 "Но ничего, сейчас ты пойдешь мне за заказом и я ее рассмотрю."
    customer3 "В общем мне пиво. Давай, поворачивайся уже!"
    img 14264
    mt "Вот извращенец."
    mt "Хотя откуда могут быть нормальные люди в этой дыре?"
    img 14265
    with diss
    m "Что к пиву?"
    img 14269
    with diss
    customer3 "Ничего, давай уже!"
    # поворачивается
    sound highheels_short_walk
    img 14266
    with diss
    w
    sound Jump1
    img 14267
    with diss
    w
    sound snd_whistle1
    img 14268
    with diss
    customer3 "Да! Я знал! Ай да жопа!"
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14270
    with fade
    w
    sound snd_plates1
    img 14271
    with diss
    w
    sound snd_beer_table
    img 14272
    with diss
    m "Вот, пожалуйста."
    music Groove2_85
    img 14273
    with fade
    customer3 "О да! Жду твою жопу на пилоне!"
    img 14264
    with diss
    mt "Не дождешься..."
    return

label gallery_14294:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14274
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 1:
        customer3 "Так что? Надумала насчет моего предложения?"
        m "Какого предложения? Вы что-то хотели заказать?"
        customer3 "Тебя хочу. Сколько будет стоит?"
        mt "Моника, спокойно. Просто очередной пьяница. Их тут целый паб."
        m "Я работаю официанткой и меня нельзя заказать."
        customer3 "А если я тебе щедро заплачу?"
        mt "Отдашь всю свою зарплату за год? Думаю, даже этого будет недостаточно."
        mt "Таким неудачникам, как ты, можно только мечтать обо мне."
        mt "И не только неудачникам... Вообще всем!"
        m "Вы меня с кем-то путаете."
        customer3 "Я спрошу у Джо..."
        mt "!!!"

    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 0:
        customer3 "Я думал, ты уже не официанткой здесь работаешь... "
        customer3 "Твоя задница со сцены смотрится отлично."
        m "Вы меня с кем-то путаете."
        m "Я просто официантка..."
        customer3 "Я хорошо запоминаю задницы. И твою я отлично помню."
        customer3 "Сколько стоит приват? Я заплачу."
        m "Я не танцую здесь на сцене. Тем более, не танцую при..."
        customer3 "Окей. Можешь дальше врать, мне все равно."
        customer3 "Как надумаешь насчет приват танца, знаешь, где меня найти."
        mt "!!!"
        mt "Он что о себе возомнил?!"
        mt "Всего лишь очередной неудачик, который спускает все свои деньги на шлюх и пиво!"

    #

    m "Что будете заказывать?"
    img 14275
    with diss
    customer3 "Возможно, что-то и буду..."
    customer3 "Для начала, давай поговорим, а то скучно."
    img 14276
    with diss
    menu:
        "Хорошо.":
            music Hidden_Agenda
            img 14277
            with fade
            m "Хорошо."
            img 14278
            with diss
            mt "Похоже лучше поговорить с этим придурком, иначе он разольет пиво или что-нибудь еще..."
#            mt "Нмчего же не произойдет, если я с ним немного поговорю."
            pass
        "Мне некогда.":
            music Groove2_85
            img 14279
            with fade
            m "Мне некогда."
            img 14280
            with diss
            customer3 "Я клиент. И я могу сказать Джо, что ты не выполняешь мои просьбы."
            img 14281
            m "Но разговоры не входят в обязанности официантки!"
            img 14282
            with diss
            customer3 "Верно. Но тебе же нужны чаевые?"
            img 14278
            with fade
            mt "Мне противно, но если он даст чаевые, может и стоит потерпеть его дурной язык. Но только совсем чуть-чуть..."
#            mt "Здесь он прав, перекинусь с ним парой фраз..."
            img 14277
            with diss
#            m "Хорошо, немного поговрим."
            m "Хорошо, говори..."
            pass

    img 14283
    with fade
    customer3 "Напомни, как тебя зовут?"
    img 14284
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14285
    with fade
    customer3 "Очень приятно. Хотя это не важно, я не запомню. И кем ты работаешь, [monica_pub_name]?"
    music Groove2_85
    img 14286
    mt "Он что, издевается?"
    img 14287
    with diss
    m "Вы не видите? Я официантка."
    img 14288
    with fade
    customer3 "Да, я это вижу! [monica_pub_name] - официантка и я Билли - директор фирмы."
    img 14278
    with diss
    mt "Да что ты знаешь обо мне?"
    img 14289
    with fade
    customer3 "Наверняка ты хотела стать актрисой.... Или нет, моделью! А возможно ты мечтала создать модный журнал?"
    img 14290
    mt "Я его уже создала!"
    img 14291
    with fade
    customer3 "Но нет, ты [monica_pub_name] - официантка. И знаешь, [monica_pub_name]... Принеси мне бургер."
    img 14292
    with diss
    m "Хорошо."
    # поворачивается
    sound highheels_short_walk
    img 14293
    with diss
    w
    sound Jump1
    img 14294
    with diss
    w
    sound snd_whistle1
    img 14295
    with diss
    customer3 "И жопа у тебя просто отпад!"
    img 14296
    with diss
    mt "Извращенец..."
    # приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14345
    with fade
    w
    sound snd_plates1
    img 14346
    with diss
    w
    sound snd_beer_table
    img 14347
    with diss
    w
    img 14348
    with diss
    customer3 "Молодец, красивая жопа! Вот тебе целый доллар! Купи себе помаду!"
    img 14258
    with diss
    mt "Какой же он мерзкий..."
    return

label gallery_14303:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14298
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    customer5 "Какая красота! И давно ли ты тут?"
    # смотрит на монику
    img 14299
    with fade
    m "Я? Всего пару дней..."
    music In_Your_Arms
    img 14300
    with diss
    customer5 "Ой как хорошо! Теперь я буду бывать здесь еще чаще!"
    customer5 "Скажи, у тебя есть парень?"
    customer5 "Или нет... Где же мои манеры? Как тебя зовут?"
    img 14301
    mt "Не хватало еще, чтобы ко мне подкатывал какой-то кретин..."
    img 14302
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14303
    with fade
    customer5 "Ох... [monica_pub_name] и Джери...Шикарно звучит..."
    customer5 "Мне надо все обдумать... Лучше всего это делается за пивом..."
    customer5 "Да, ты не ответила на мой вопрос: У тебя есть парень?"
    img 14304
    with diss
    m "Вообще-то я замужем."
    # смотрит на моникт руку
    img 14305
    with diss
    w
    img 14306
    with fade
    customer5 "Понятно, ты врешь, кольца нет, значит ты свободна!"
    customer5 "У меня все шансы!"
    customer5 "В общем, мне пива!"
    music Groove2_85
    img 14301
    mt "Еще чего... Размечтался... Ему никогда не светит такая леди, как Я!"
    img 14307
    with diss
    m "Хорошо."
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Groove2_85
    img 14308
    with fade
    w
    sound snd_plates1
    img 14309
    with diss
    w
    sound snd_beer_table
    img 14310
    with diss
    m "Пожалуйста."
    music In_Your_Arms
#    img 14311
#    with fade
    img 14312
    with diss
    customer5 "Да, спасибо. Можешь идти."
    customer5 "Хотя стоп...Где же мои манеры? Вот тебе доллар. Скоро заработаешь себе на платье."
    img 14313
    with diss
    mt "Изысканные манеры... Фи!"
    return

label gallery_14318:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14317
    with fade
    m "Вам что-нибудь принести?"
    music Groove2_85
    img 14318
    with diss
    customer6 "А?! Ты что, не видишь, я сижу у стойки! Ик!"
    customer6 "Эй, бармен! Виски с колой! Или водку с колой?"
    customer6 "Ну или нет! Виски с водкой! Ик!"
    img 14319
    with diss
    mt "Да он похоже пьян... Думаю, Джо о нем позаботится..."
    return

label gallery_14320:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14320
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14321
    with diss
    customer4 "Оу! Какая красивая мордашка! Новенькая?"
    # смотрит на монику
    music Groove2_85
    img 14322
    with diss
    m "Кто, Я?!"
    img 14323
    with fade
    customer4 "Нет, твоя мордашка! Ну конечно же ты!"
    customer4 "Мда... Понятно почему ты официантка."
    customer4 "Как зовут? Только не спрашивай кого..."
    img 14324
    mt "Он что, думает, что Я глупая?"
    mt "Я?!"
    img 14325
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14326
    with fade
    customer4 "Отлично, [monica_pub_name]! Я не буду говорить как меня зовут, и даже делать заказ."
    customer4 "Ты новенькая, не уверен, что эта информация уместится в твоей красивой головке."
    customer4 "Можешь идти, увидимся!"
    img 14327
    with diss
    mt "Почему он так со мной разговаривает? Я не глупая!"
    return

label gallery_14340:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14328
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer4_dance_comment_stage == 1:
        customer4 "А вот и официанточка, она же стриптизерша!"
        m "Я не стритизерша."
        customer4 "Ну, конечно! Еще скажи, что я снова перепутал."
        customer4 "Ты думала, в маске никто не узнает, кто ты на самом деле?"
        mt "???"
        mt "Он... узнал... м-меня?"
        mt "!!!"
        customer4 "Ты боишься, если узнают, что ты еще и официанткой тут работаешь, то приставать будут?"
        customer4 "Ладно. Я не скажу никому. Притворяйся дальше."
        mt "Как же этот придурок напугал меня!"
        mt "Фу-у-у... Что-то с нервами у меня совсем непорядок!"
        m "..."


    if monicaStartedStripDanceFlag == True and customer4_dance_comment_stage == 0:
        customer4 "Эй, отлично выступаешь на сцене!"
        m "Вы меня с кем-то путаете."
        m "Я здесь не танцую."
        customer4 "Я не могу тебя с кем-то путать. Я тебя видел на сцене!"
        m "Я не танцую на сцене."
        customer4 "Хммм... Странно..."
        mt "!!!"
        mt "Какое ему дело до этого?!"

    #

    m "Вам что-нибудь принести?"
    img 14329
    with diss
    customer4 "Да! Принеси мне пива и Ваш восхитительный Shiny бургер!"
    img 14330
    with diss
    m "Да, конечно."
    img 14331
    with fade
    customer4 "Запомнила? Одно пиво и Shiny бургер. Не харчо и не пасту!"
    music Groove2_85
    img 14332
    m "Я поняла!"
    img 14333
    customer4 "Я надеюсь..."
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14334
    with fade
    w
    sound snd_plates1
    img 14335
    with diss
    w
    sound snd_beer_table
    img 14336
    with diss
    m "Вот, пожалуйста!"
    img 14337
    with fade
    customer4 "Ой, какая молодец! Все как надо!"
    customer4 "Держи доллар за красивую мордашку! А если улыбнешься, дам два!"
    img 14338
    with diss
    menu:
        "Улыбнуться.":
            music Hidden_Agenda
            img 14339
            with diss
            mt "Доллар за одну улыбку... Чтож, пускай..."
            mt "Он не знает что я буду думать, пока улыбаюсь ему..."
            music Loved_Up
            img 14340
            with fadelong
            w
            mt "Придурок..."
            w
            img 14341
            with diss
            customer4 "Какая умничка, держи еще доллар!"
            return
        "Не улыбаться.":
            # стоит с каменным лицом
            music Groove2_85
            img 14342
            with fade
            mt "С чего бы мне улыбаться этой деревенщине?"
            img 14343
            with diss
            m "..."
            img 14344
            with diss
            customer4 "Не хочешь? Это все потому, что ты тут недавно..."
    return

label gallery_14358:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14314
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer5_dance_comment_stage == 1:
        customer5 "А я тебя ждал!"
        m "Да? Хотите сделать заказ?"
        customer5 "Конечно! Скажи, а сколько будет стоить приват с тобой?"
        m "!!!"
        m "Я не танцую!"
        mt "Как же они меня все достали со своими расспросами!!!"
        customer5 "Не, теперь ты меня не обманешь! Я видел тебя на сцене!"
        m "Вы меня с кем-то перепутали. Тут работает девушка, она немного похожа на меня..."
        customer5 "Да? Это она новенькая стриптизерша?"
        m "Да."
        customer5 "А как мне заказать у нее приват?"
        m "Не знаю. По-моему, она только на сцене танцует и в приват не ходит."
        customer5 "Жаль..."



    if monicaStartedStripDanceFlag == True and customer5_dance_comment_stage == 0:
        customer5 "Ого! Ты же на сцене танцуешь!"
        m "Вы меня с кем-то путаете."
        m "Я не танцую на сцене."
        customer5 "Серьезно? По-моему, это ты была!"
        m "Я работаю тут просто официанткой и не танцую стриптиз."
        customer5 "Вот черт. Видимо, я перебрал с пивом тогда..."
        mt "Неудивительно..."

    #


    m "Вам что-нибудь принести?"
    img 14315
    with diss
    customer5 "Да! Мне пожалуйста два бургера, и два Ваших самых лучших коктейля!"
    img 14316
    with diss
    m "Хорошо, один момент!"
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14349
    with fade
    w
    sound snd_plates1
    img 14350
    with diss
    w
    sound snd_beer_table
    img 14351
    with diss
    w
    img 14353
    with diss
    m "Вот, пожалуйста! Что-нибудь еще?"
    music In_Your_Arms
    img 14354
    with fade
    customer5 "Да, Вас! Не зря же я купил всего по два!"
    customer5 "Садитесь рядом и давайте пообщаемся!"
    customer5 "Я верю, что мы созданы друг для друга!"
    menu:
        "Сесть рядом с клиентом. (в будущих обновлениях) (disabled)":
            # в след обнове
            return
        "Не буду!":
            # клиент злой
            m "Не буду!"
            music Power_Bots_Loop
            img 14355
            with fade
            customer5 "Ах ты глупая официантка! Даже школьницы знают этот способ знакомства!"
            customer5 "Не могла сказать сразу?!"
            img 14357
            with diss
            m "Я подумала, что Вы очень голодный."
            m "Что-нибудь еще?"
            img 14358
            with diss
            customer5 "Да! Свали отсюда!"
    return

label gallery_14370:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14359
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    sound snd_whistle1
    img 14360
    with diss
    w
    music Groove2_85
    img 14361
    with fade
    customer10 "Да! Я желаю Вас. Сколько?"
    music Power_Bots_Loop
    img 14362
    with hpunch
    m "Что? Вы это о чем? Я не продаюсь!"
    img 14363
    with diss
    customer10 "Серьезно? У всего есть цена..."
    customer10 "Как тебя зовут?"
    music Groove2_85
    img 14364
    with fade
    m "Меня зовут [monica_pub_name]."
    img 14365
    with diss
    customer10 "Любопытно... [monica_pub_name] - это сценическое имя или настоящее?"
    img 14366
    mt "Почему он спрашивает?"
    img 14367
    with diss
    m "Конечно настоящее!"
    img 14368
    with fade
    customer10 "Правда? Я думаю, тебе бы больше пошло имя Анжелина! Или Виолетта!"
    customer10 "Что думаешь?"
    img 14369
    with diss
    m "Ничего... Мне мое имя нравится..."
    img 14370
    with diss
    customer10 "А мне вот что-то не очень... Надо бы тебе придумать другое имя...Подумай над этим!"
    customer10 "А пока принеси мне что-нибудь выпить!"
    img 14371
    with diss
    m "Да, хорошо."
    # уходит приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14372
    with fade
    w
    sound snd_plates1
    img 14373
    with diss
    w
    sound snd_beer_table
    img 14374
    with diss
    customer10 "А...Виолетта! Наконец то!"
    music Groove2_85
    img 14375
    m "Я не Виолетта..."
    img 14376
    with diss
    customer10 "Это не важно, но важно то, что я тут постоянный клиент и советую тебе это запомнить, Виолетта!"
    customer10 "Но я могу тебя звать и Новенькая... Что думаешь?"
    img 14377
    mt "Что ты урод!"
    img 14378
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14379
    with fade
    customer10 "Да, Виолетта, я помню!"
    customer10 "Кстати, спасибо за выпивку. Еще увидимся."
    img 14380
    with diss
    mt "Надеюсь, нескоро."
    return

label gallery_14383:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14381
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer11_dance_comment_stage == 1:
        customer11 "Не буду ничего говорить про то, как ты танцуешь у пилона."
        m "Я..."
        customer11 "А то снова будет много слов о том, что ты не такая."
        customer11 "Ты же официантка сейчас?"
        m "Да..."
        customer11 "Давай, ты просто выполнишь свою работу и все?"
        mt "?!"

    if monicaStartedStripDanceFlag == True and customer11_dance_comment_stage == 0:
        customer11 "Ты неплохо танцевала в прошлый раз на сцене."
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer11 "Расскажи это кому-нибудь другому."
        m "Я официантка, а не стрип..."
        customer11 "Мне это неинтересно совсем!"
        mt "!!!"
        mt "Очередной хам..."

    #


    m "Вы готовы сделать заказ?"
    # рассматривает
    sound snd_whistle1
    img 14382
    with diss
    w
    music Groove2_85
    img 14383
    with diss
    customer11 "А ты конфетка!"
    customer11 "В общем все просто: мне пиво и бургер и быстро!"
    img 14384
    m "Да, конечно!"
    img 14385
    customer11 "И можно это делать без слов. Быстро пошла и принесла мой заказ."
    img 14386
    with diss
    mt "Грубиян..."
    # уходит приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14387
    with fade
    w
    sound snd_plates1
    img 14388
    with diss
    w
    sound snd_beer_table
    img 14389
    with diss
    w
    img 14390
    with fade
    customer11 "Вот видишь, все очень просто. Молодец, держи." # дает чай
    img 14391
    with diss
    m "Спасибо."
    music Groove2_85
    img 14392
    with diss
    customer11 "Да, да... Иди уже..."
    img 14393
    with fade
    mt "Очередной придурок."
    return

label gallery_14395:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14394
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14395
    with diss
    customer9 "Оу! Новенькая? Скажи, ты любишь подарки?"
    img 14396
    mt "Подарки? Вероятно, он о чаевых..."
    img 14397
    with diss
    menu:
        "Ну да...":
            music Hidden_Agenda
            img 14398
            with fade
            m "Да."
            img 14399
            with diss
            customer9 "Я так и думал. Вот скажи, что тебе подарить?"
            img 14400
            with diss
            m "У меня все есть, но чаевые были бы кстати."
            img 14401
            with fade
            customer9 "Нет, я не о чаевых. Как насчет страстного поцелуя?"
            music Groove2_85
            img 14402
            with diss
            m "Нет, спасибо."
            img 14403
            with diss
            mt "Да как он может подобное спрашивать у такой как Я!?"
            if monicaBitch == True:
                mt "Придурок!"
            pass
        "Я не готова отвечать на этот вопрос.":
            music Groove2_85
            img 14404
            with fade
            m "Я не готова отвечать на этот вопрос."
            img 14405
            with diss
            customer9 "Я понял... Свидетели... Хорошо, не отвечай, потом расскажешь!"
            pass
    # смотрит на монику
    img 14406
    with fade
    customer9 "Ты любишь классический секс или в попу?"
    music Power_Bots_Loop
    img 14407
    with hpunch
    m "А?!"
    img 14408
    customer9 "Я понял! Это значит в попу... Иначе ты бы не работала в Shiny Hole."
    img 14403
    with diss
    mt "Он нормальный?"
    img 14409
    with fade
    customer9 "Мне пожалуй ничего, но я очень рад нашему знакомству!"
    img 14410
    with diss
    mt "Неадекватный урод..."
    return

label gallery_14413:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14412
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    img 14413
    with diss
    w
    sound Jump1
    img 14414
    with diss
    w
    img 14415
    with fade
    customer12 "А время зря не теряет..."
    customer12 "Как зовут?"
    img 14416
    with diss
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14417
    with fade
    customer12 "Сколько стоят твои сиськи, [monica_pub_name]?"
    customer12 "Думаю, сколько приготовить тебе на чай. Я плачу 1 процент от цены сисек."
    music Power_Bots_Loop
    img 14418
    with hpunch
    m "Вы о чем? Они не продаются!"
    img 14419
    with fade
    customer12 "Не обмынывай! Ну дак что, сколько ты заплатила за операцию?"
    img 14420
    m "Они настоящие!"
    music Groove2_85
    img 14421
    with fade
    customer12 "Ну да, значит твои чаевые составят ноль долларов. Хотя кто знает..."
    customer12 "Другая официантка получает по 3 доллара, имей ввиду..."
    img 14422
    with diss
    mt "О чем ты вообще? Лучше бы я к тебе не подходила!"
    img 14424
    with fade
    customer12 "И это только за сиськи. А ведь есть еще и зад..."
    customer12 "Какая-то ты не разговорчивая для первого раза... Тогда и я ничего не буду заказывать..."
    img 14423
    with diss
    mt "Похоже, половина посетителей этого бара ненормальные..."
    return

label gallery_14428:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music RocknRoll_loop

    img 14453
    with fadelong

    m "Здравствуйте! Что будете заказывать?"
    img 14426
    with diss
    customer7 "Заказ? Да, готовы, но мы скажем, что мы хотим официантке, а Ты поднимайся! Надоело уже смотреть на эту стриптизершу."
    # смотрит на монику
    img 14427
    with diss
    m "Я и есть официантка..."
    img 14428
    with fade
    customer7 "Да? Да быть не может! Ты гораздо эффектнее смотрелась бы на пилоне!"
    customer7 "Ты новенькая?"
    customer7 "Как тебя зовут?"
    img 14429
    with diss
    m "Да, я тут недавно. Меня зовут [monica_pub_name]"
    img 14430
    with fade
    customer7 "[monica_pub_name], ты хочешь заработать?"
    img 14431
    with diss
    mt "Да я зарабатываю побольше, чем вся твоя семья и твой товарищ, и все их родственники во всем мире!"
    img 14432
    with diss
    m "Да, именно за этим я здесь."

    img 14454
    with fadelong

    customer7 "Я так и думал... Просто для информации: гораздо больше можно заработать тут.." # показывает на шест
    img 14434
    with diss
    m "Мне это не интересно."
    img 14435
    with fade
    customer7 "Да, да, все так говорят, пока не узнают какие тут деньги..."
    img 14437
    mt "Неужели и правда большие?"
    img 14455
    with diss
    menu:
        "И какие же?":
            img 14456
            with fade
            m "И какие же?"
            img 14457
            with fade
            customer7 "Ну за представление можно заработать 100 долларов..."
            customer7 "Но все зависит от того, что ты покажешь..."
            img 14458
            m "Я поняла, мне это неинтересно."
            img 14459
            with diss
            mt "100 долларов за вечер? Немаленькие деньги для такой дыры..."
            mt "Но это не для меня! Я не собираюсь танцевать у всех на виду!"
            pass
        "Мне это не интересно.":
            img 14460
            with fade
            m "Говорю же, мне это не интересно."
            img 14461
            with diss
            customer7 "Конечно, конечно, это пока..."
            pass
    img 14462
    with fade
    customer7 "А пока, принеси нам два шота! На свой вкус."
    img 14463
    with diss
    m "Хорошо."
    # уходит принтсит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music RocknRoll_loop
    img 14464
    with fade
    w
    img 14465
    with diss
    w
    sound snd_plates1
    img 14466
    with diss
    w
    sound snd_beer_table
    img 14467
    with fade
    customer7 "То что надо! Похоже, ты умеешь читать мысли!"
    customer7 "Вот, держи!" # дает доллар
    customer7 "Приходи к нам чаще! Я вижу в тебе потенциал."
    img 14468
    mt "Какой еще потенциал?"
    img 14469
    with diss
    m "До свидания."
    return

label gallery_14452:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14438
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer12_dance_comment_stage == 1:
        customer12 "О, это ты! Слушай, а как насчет привата?"
        m "Я не танцую приват... И на сцене не танцую."
        customer12 "Я это уже слышал... Аха-ха!!!"
        customer12 "Хорош уже строить из себя невинную цыпочку!"
        customer12 "Сколько за приват?"
        mt "?!"
        m "Я не танцую приват!"
        customer12 "А зря! Могла бы хорошо заработать!"
        customer12 "Ладно, думаю, это временно. Скоро ты передумаешь."
        mt "!!!"
        mt "Ни за что не пойду в приват!"
        mt "За кого он меня принимает?!"


    if monicaStartedStripDanceFlag == True and customer12_dance_comment_stage == 0:
        customer12 "Эй, ты же у пилона теперь сиськами трясешь!"
        customer12 "Или ты здесь на двух работах?"
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer12 "Ну конечно! Я что, слепой что-ли?!"
        m "Я просто официантка..."
        customer12 "Ну ладно. Не хочешь - не говори."
        customer12 "Только на сцене в следующий раз танцуй без этих своих шмоток."
        m "!!!"
        customer12 "Тогда не придется подрабатывать официанткой."
        customer12 "За такие сиськи чаевых много будут платить."
        mt "Фу, как грубо!"
        mt "По-моему, здесь все такие грубияны!"
        mt "!!!"
        mt "Как мне надоела эта дыра!"

    #


    m "Здравствуйте, что будете заказывать?"
    img 14439
    with diss
    customer12 "Пиво, бургер и ваш изумительный харчо!"
    img 14440
    with diss
    m "Да, хорошо, сейчас сделаем."
    # разворачивается спиной , кастомер бьет ее по жопе + звук шлепка
    sound snd_slap1
    img 14441
    with hpunch
    sound_from_side "(шлепок)"
    img 14442
    customer12 "Вот именно поэтому ты получаешь чаевые!"
    img 14443
    with diss
    menu:
        "Какого?!":
            music Power_Bots_Loop
            img 14444
            with fade
            m "Еще раз так сделаешь, и тебе не сдобровать!"
            img 14445
            with diss
            customer12 "Оу, какая ты злая, оказывается..."
            customer12 "Давай, неси уже мой заказ!"
            customer12 "И кстати, ты только что обнулила свои чаевые."
            # уходит за заказом, приходит, ставит на стол
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Groove2_85
            sound snd_plates1
            img 14446
            with fade
            w
            sound snd_beer_table
            img 14447
            with diss
            w
            img 14448
            with fade
            customer12 "Можешь идти. Если в следующий раз не будешь грубить, получишь пару долларов."
            img 14449
            with diss
            mt "Идиот..."
            return
        "Проигнорировать.":
            music Hidden_Agenda
            img 14451
            with fade
            mt "И не только поэтому..."
            img 14452
            with diss
            customer12 "Постарайся сделать так, чтобы я получил свой заказ как можно скорее."
            # уходит за заказом, ставит на стол
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Hidden_Agenda
            sound snd_plates1
            img 14446
            with fade
            w
            sound snd_beer_table
            img 14447
            with diss
            w
            img 14450
            with diss
            customer12 "Как раз вовремя! Молодчина!"
            customer12 "Вот, держи! Доллар за скорость и доллар за твою попку!"
            customer12 "Что стоишь? Иди, не заставляй клиентов ждать!"
    return

label gallery_14474:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music RocknRoll_loop

    img 14470
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer78_dance_comment_stage == 1:
        customer7 "Эй, детка! Когда уже разденешься на сцене?!"
        m "Я... Я не танцую..."
        customer7 "Мы это уже слышали. Не танцует она! Аха-ха!!!"
        customer7 "Запомни: чем меньше одежды на сцене, тем больше чаевые!"
        m "!!!"
        mt "Похотливые животные! Ненавижу!"
        m "Я..."
        customer7 "А если пойдешь с нами в приват, то заработаешь раз в десять больше!"
        m "Я не танцую!"
        mt "!!!"
        customer7 "А если будешь работать официанткой с голыми сиськами..."
        customer7 "То чаевых будет еще больше! Аха-ха!!!"
        mt "!!!"



    if monicaStartedStripDanceFlag == True and customer78_dance_comment_stage == 0:
        customer7 "О, детка! Правильно сделала, что послушалась нашего совета!"
        m "Какого совета?"
        customer7 "Отпадные сиськи! На сцене выглядишь охренительно!"
        m "Я официантка, а не стриптизерша..."
        customer7 "Конечно, конечно... А то я тебя не разглядел на сцене отсюда!"
        m "Я..."
        customer7 "В следующий раз снимай с себя все эти тряпки на сцене."
        customer7 "Если хочешь заработать хорошие чаевые."
        mt "!!!"

    #


    m "Что будете..."
    img 14471
    with diss
    customer7 "Нам два шота! И быстро! Хотим их выпить перед очередным выступлением!"
    img 14472
    with diss
    m "Хорошо, один момент!"
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14464
    with fade
    w
    img 14465
    with diss
    w
    sound snd_plates1
    img 14466
    with diss
    w
    sound snd_beer_table
    img 14473
    with diss
    m "Вот, пожалуйста! Что-нибудь еще?"
    img 14474
    with fade
    customer7 "Да, вот еще что! Не могла бы ты в следующия раз быть побыстрее!"
    customer7 "Похоже тебя сюда взяли по двум причинам. Эти причины: сиськи и жопа! Но уж точно не скорость!"
    music RocknRoll_loop
    img 14467
    with diss
    w
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14454
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14433
        with fadelong
    customer7 "А теперь иди, шоу уже началось!"
    img 14475
    with diss
    mt "Козлы..."
    return

label gallery_14477:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14411
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer9_dance_comment_stage == 1:
        customer9 "Эй, не могу дождаться, когда ты покажешь свою голую попку со сцены!"
        m "Вы меня с кем-то..."
        customer9 "Я хочу, чтобы ты сняла с себя трусики на сцене и бросила их мне..."
        customer9 "Я хочу забрать их..."
        customer9 "Я готов заплатить за это. Сколько? Назови цену."
        mt "?!"
        m "Я не танцую на..."
        customer9 "Не хочешь говорить? Хорошо, я буду ждать этого момента."
        customer9 "А потом просто заберу их..."
        mt "..."
        mt "Человек, озабоченный чужими трусами!"
        mt "Кого только не встретишь в этой дыре!"
        mt "!!!"


    if monicaStartedStripDanceFlag == True and customer9_dance_comment_stage == 0:
        customer9 "У меня в штанах дымится, когда вижу тебя на сцене!"
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer9 "Расскажи это кому-нибудь другому."
        m "Я официантка, а не стрип..."
        customer9 "Охренительная задница!!!"
        customer9 "Не могу дождаться, когда ты ее оголишь на сцене перед всеми!"
        m "Я..."
        customer9 "А еще хочу увидеть, как ты танцуешь только для меня..."
        mt "Долбанный извращенец!"
        mt "По-моему, здесь все такие!"
        mt "!!!"
        mt "Как мне надоела эта дыра!"

    #


    m "Что будете заказывать?"
    # чел резко хватает монику и садит себе на колени
    music Groove2_85
    sound Jump1
    img 14476
    with vpunch
    m "Ай!"
    sound Jump2
    img 14477
    with hpunch
    customer9 "Скажи, ты была хорошей девочкой?"
    customer9 "Расскажи Санте!"
    customer9 "И возможно, Санта сделает тебе хороший подарок!"
#    mt "Меня посадил к себе на колени незнакомый мужик! Возможно, стоит ему подыграть..."
    img 14478
    with diss
    menu:
        "Быстро отпусти меня!":
            music Power_Bots_Loop
            sound snd_punch_face2
            img 14479
            with diss
            m "Быстро отпусти меня!"
            sound Jump1
            img 14480
            with diss
            m "Еще раз попробуй сделай так и я сломаю тебе нос, урод!"
            # моника вырывается
            img 14481
            with fade
            customer9 "Ах вот ты как! Ну и вали! Ваше пиво кстати отстой!"
            img 14482
            with diss
            mt "Что же ты его тогда пьешь?"
            return
        "Да, я была хорошей девочкой.":
            label gallery_14485:
            music Hidden_Agenda
            img 14483
            with fade
            m "Да, я была хорошей девочкой."
            img 14484
            with diss
            customer9 "Я так и думал! Уверен, ты обслужила очень много клиентов и они остались довольны."
            # кладет ей под чулок купюру
            sound snd_take_paper
            img 14485
            with diss
            w
            img 14486
            with fade
            customer9 "Ладно, беги, у меня еще есть пиво."
            img 14487
            with diss
            mt "Он дал мне 20 долларов! Ничего себе..."
    return

label gallery_21047:
# Если идет, вызывается меню со сценами с Джо (открываются последовательно)
# Сцена1:
# Трогает зад
# Джо
    music Loved_Up
    img 21027
    with fadelong
    joe "О, [monica_pub_name], ты пришла!"
    m "Да, Джо, я пришла."
    music Groove2_85
    img 21028
    with diss
    joe "Тебя точно не видела Эшли?"
    joe "Не видела как ты сюда заходила?"
    img 21029
    with diss
    m "Нет, Джо."
    m "Меня не видела Эшли."
    m "Но она может придти сюда в любой момент."
    img 21030
    with fade
    joe "Нет, [monica_pub_name], она не придет."
    joe "Пока меня нет, она не оставит бар без присмотра."
    joe "У нас здесь, знаешь-ли, такие клиенты... хе-хе."
    img 21031
    m "Я знаю какие здесь клиенты, Джо..."
    img 21032
    joe "..."
    music Hidden_Agenda
    img 21033
    with fade
    m "Джо, я готова еще раз извиниться за то что не отдала деньги."
    m "Я правда забыла и..."
    music Loved_Up
    sound Jump1
    img 21034
    with diss
    joe "[monica_pub_name], хватит про эти деньги."
    joe "Мне не нужны эти деньги, я хочу тебя, [monica_pub_name]!"
    joe "Я хочу твою попку, [monica_pub_name]!"
    music Power_Bots_Loop
    img 21035
    with hpunch
    m "Джо, это исключено!"
    m "У тебя есть жена, которая прямо за стенкой!"
    m "Да, я хочу работать здесь, но я не собираюсь за это спать с таким жирным толстяком, как ты, Джо!"
    music Loved_Up
    img 21036
    with fade
    joe "[monica_pub_name], очень жаль."
    img 21037
    with diss
    joe "Но повернись, хотя бы, своей попой."
    joe "Покажи ее мне!"
    img 21038
    with diss
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            m "Нет, Джо!"
            return
    music Groove2_85
    img 21039
    with fade
    m "И на этом все, ты сделаешь так, чтобы Эшли простила меня!"
    img 21040
    with diss
    joe "Хорошо, [monica_pub_name]."
    joe "Повернись своей попой, скорее!"
    music Hidden_Agenda
    img 21041
    with fade
    m "..."
    mt "Дьявол, мне не хочется делать этого!"
    mt "С другой стороны, в этом нет ничего страшного и это позволит мне снова работать здесь..."
    mt "Мне нужны деньги..."
    img 21042
    with diss
    m "..."
    joe "Я жду!"
    # Моника показывает зад
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 21043
    with fadelong
    w
    img 21044
    with diss
    w
    sound Jump1
    img 21045
    with diss
    w
    img 21046
    with diss
    joe "!!!"
    music Groove2_85
    img 21047
    with fade
    m "Все? Достаточно?"
    sound Jump1
    img 21048
    with diss
    joe "[monica_pub_name], я должен потрогать твою попу!"
    joe "Она такая сладкая! Я хочу этого, [monica_pub_name]!"
    music Power_Bots_Loop
    img 21049
    with hpunch
    m "Нет!"
    music Groove2_85
    img 21050
    with fade
    joe "Я потрогаю ее и обещаю что Эшли простит тебя!"
    music Hidden_Agenda
    img 21051
    with diss
    mt "Черт! Что же мне делать?"
    mt "Мне нужна эта работа. Я могу здесь заработать хотя бы на еду..."
    mt "Но неужели я соглашусь на то, чтобы какой-то толстяк в трущобах лапал меня?!"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21049
            m "Нет, Джо!"
            return
    music Groove2_85
    img 21052
    with fade
    m "Ладно, но только в одежде!"
    m "И я не буду отдавать те чаевые, которые взяла себе!"
    music Loved_Up
    img 21053
    with diss
    joe "Хорошо, [monica_pub_name]!"
    joe "Можешь оставить эти деньги себе!"
    label gallery_21061:
    music stop
    img black_screen
    with diss
    pause 1.5
    # трогает
    music Loved_Up
    img 21054
    with fadelong
    joe "Ахххх!"
    joe "Как я мечтал об этом!"
    sound Jump1
    img 21055
    with diss
    joe "Я стал мечтать об этом с первой минуты, когда увидел тебя здесь, [monica_pub_name]!"

    img 21056
    with diss
    w
    sound Jump2
    img 21057
    with diss
    w
    stop music
    play music "Sounds/audio_Monica_Joe_Ass_1.mp3"
    scene black
    image videov_Monica_Joe_Ass_1_1 = Movie(play="video/v_Monica_Joe_Ass_1_1.mkv", fps=30)
    show videov_Monica_Joe_Ass_1_1
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    music Groove2_85
    img 21058
    with fade
    mt "Очередной озабоченный мерзавец!"

    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Ass_1.mp3"
    scene black
    image videov_Monica_Joe_Ass_1_2 = Movie(play="video/v_Monica_Joe_Ass_1_2.mkv", fps=30)
    show videov_Monica_Joe_Ass_1_2
    with fadelong
    wclean
    stop music
    music stop

    music Loved_Up2
    img 21059
    with diss
    joe "Ах, твоя попка!"
    img 21060
    with diss
    joe "Она такая упругая!"
    img 21061
    with diss
    joe "Ах!"
    music Groove2_85
    img 21062
    with fade
    m "Ну все, хватит!"
    m "Идем к Эшли!"
    return

label gallery_21180:
# Эшли
# Просит поцеловаться (хватает Монику за зад, под джинсы)
    music Groove2_85
    img 21172
    with fadelong
    m "Я пришла, Эшли..."

    music Loved_Up
    img 21173
    with diss
    ashley "О, [monica_pub_name]!"
    sound Jump1
    img 21174 # jump
    with diss
    ashley "Иди ко мне!"
    ashley "Я ждала когда ты что-нибудь натворишь..."
    img 21175
    with diss
    ashley "Иди ко мне! Иди я поцелую тебя!"
    img 21176
    with diss
    menu:
        "Позволить Эшли поцеловать себя.": #corruption
            pass
        "Отказать.":
            music Power_Bots_Loop
            img 21177
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return
#    music Loved_Up
    # Эшли целует Монику
    sound snd_longkiss1
    img 21178
    with fade
    ashley "Ммммм..."
    sound snd_longkiss1
    img 21179
    with fade
    mt "!!!"


    music audio_longkiss1
    scene black
    image videov_Monica_Ashley_Kiss_1_1 = Movie(play="video/v_Monica_Ashley_Kiss_1_1.mkv", fps=30)
    show videov_Monica_Ashley_Kiss_1_1
    with fadelong
    wclean

    stop music
    music Loved_Up
    sound snd_longkiss1
    img 21180
    with diss
    ashley "Ммммм... Моя конфетка... Мммммм..."
    # Эшли пропускает руку Монике под джинсы сзади
    sound snd_longkiss1
    img 21181
    with fade
    w
    music Loved_Up2
    sound Jump2
    img 21182
    with diss
    #sound
    w
    sound snd_longkiss1
    img 21183
    with diss
    mt "!!!"

    music2 audio_longkiss1
    scene black
    image videov_Monica_Ashley_Kiss_1_1 = Movie(play="video/v_Monica_Ashley_Kiss_1_1.mkv", fps=30)
    show videov_Monica_Ashley_Kiss_1_1
    with fadelong
    wclean

    music2 stop
#    music Loved_Up2
    img 21184
    with diss
    ashley "Ах, эта сладкая попка... Мммммм..."
    img 21185
    with diss
    ashley "Какая она упругая... Мммммм...."
    # Моника отстраняется
    music Groove2_85
    img 21186
    with fadelong
    m "Эшли, пожалуйста, хватит!"
    img 21187
    with diss
    ashley "[monica_pub_name], ты получила прощение на этот раз..."
    ashley "Я подожду, пока ты снова что-нибудь не напроказничаешь..."
    img 21188
    mt "!!!"
    return
