default monicaShawarmaApartment1 = False  # Моника спросила у продавца шавермы про квартиру
default monicaShawarmaApartment2 = False  # Моника сразу согласилась посмотреть квартиру продавца шавермы
default monicaShawarmaApartment3 = False  # Моника посмотрела квартиру и согласилась ее арендовать (50 баксов)
default monicaShawarmaApartment4 = False  # Моника согласилась арендовать квартиру за 300 баксов
default monicaShawarmaApartment5 = False # Моника внесла первую оплату Джеку за квартиру
default monicaShawarmaApartment6 = False  # Моника согласилась сделать минет за скидку в 10 процентов
default monicaShawarmaApartment7 = False  # Моника согласилась заняться сексом за скидку в 20 процентов
default monicaShawarmaApartment8 = False  # Моника заплатила $ 300 за квартиру (без скидки)
default monicaShawarmaApartment9 = False  # Джек выселил Монику за неуплату
default monicaShawarmaApartment10 = False  # Моника заплатила денег после ее выселения и снова может жить в квартире
default monicaShawarmaApartment11 = False  # Моника отказалась оплачивать ремонт и мебель

default ep211_dialogues6_slum_apartment_3_flag1 = False

default skip_scenes_list = []

label check_skip_scene(skip_scene_check_name):
    if skip_scene_check_name in skip_scenes_list:
        menu:
            "Продолжить.":
                return False
            "Пропустить.":
                return True
    $ skip_scenes_list.append(skip_scene_check_name)
    return False

#call ep211_dialogues6_slum_apartment_1() # мысли Моники об аренде квартиры, она стоит возле хостела
#call ep211_dialogues6_slum_apartment_2() # мысли перед разговором с Джеком о съеме квартиры
#call ep211_dialogues6_slum_apartment_3() # разговор с Джеком об аренде
#call ep211_dialogues6_slum_apartment_4() # мысли Моники (глазик) возле дома, где квартира
#call ep211_dialogues6_slum_apartment_5() # Моника с Джеком возле дома, где квартира
#call ep211_dialogues6_slum_apartment_6() # квартира, разговор с Джеком, оплата, осмотр своих владений
#call ep211_dialogues6_slum_apartment_7() # квартира, мысли Моники после ухода Джека
#call ep211_dialogues6_slum_apartment_8a() # мысли, осматривает квартиру - стены, пол
#call ep211_dialogues6_slum_apartment_8b() # мысли, осматривает квартиру - мусор, грязь в квартире
#call ep211_dialogues6_slum_apartment_8c() # мысли, осматривает квартиру - раскладушка
#call ep211_dialogues6_slum_apartment_8d() # мысли, осматривает квартиру - деревянная мебель, стул, рыбка
#call ep211_dialogues6_slum_apartment_8m() # мысли, осматривает квартиру - окно
#call ep211_dialogues6_slum_apartment_8f() # мысли, осматривает кухню - стены, пол
#call ep211_dialogues6_slum_apartment_8g() # мысли, осматривает кухню - кухонная утварь
#call ep211_dialogues6_slum_apartment_8h() # мысли, осматривает ванную - стены, пол
#call ep211_dialogues6_slum_apartment_8i() # мысли, осматривает ванную - унитаз
#call ep211_dialogues6_slum_apartment_8j() # мысли, осматривает ванную - раковина
#call ep211_dialogues6_slum_apartment_8k() # мысли, осматривает ванную - душ
#call ep211_dialogues6_slum_apartment_8l() # мысли, осматривает квартиру - мохито на столике (глазик)
#call ep211_dialogues6_slum_apartment_8n() # мысли, мохито на столике в комнате (hand)
#call ep211_dialogues6_slum_apartment_9() # Моника в квартире в домашней одежде (глазик)
#call ep211_dialogues6_slum_apartment_10() # суббота, приходит Джек за деньгами
#call ep211_dialogues6_slum_apartment_11() # сцена минета, когда выбран пункт меню 'Скидка 10 процентов' и 'Согласиться'
#call ep211_dialogues6_slum_apartment_12() # сцена секса, когда выбран пункт меню 'Скидка 20 процентов' и 'Согласиться'
#call ep211_dialogues6_slum_apartment_13() # мысли Моники перед домом, выбран пункт меню 'У меня нет денег' и Джек ее выселил
#call ep211_dialogues6_slum_apartment_14() # мысли, Моника пытается зайти в квартиру сразу же после того, как Джек ее выставил
#call ep211_dialogues6_slum_apartment_15() # мысли, Моника перед домом спустя какое-то время после выселения, Джек поменял замки
#call ep211_dialogues6_slum_apartment_16() # мысли, у Моники достаточно денег, чтобы заселиться в квартиру снова, пришла к дому
#call ep211_dialogues6_slum_apartment_17() # у Моники достаточно денег, чтобы заселиться в квартиру снова, пришла к шаверме, разговор с Джеком
#call ep211_dialogues6_slum_apartment_18() # мысли, Моника вернулась в квартиру после ее выселения
#call ep211_dialogues6_slum_apartment_19() # после оплаты аренды в субботу, перед уходом Джек предлагает ремонт и мебель в квартире


# улица Хостела, рядом с пабом, после работы
label ep211_dialogues6_slum_apartment_1:
    # Моника стоит на улице
    $ questHelp("flat_slums_1", skipIfExists=True)
    mt "Каждый раз, когда прихожу сюда..."
    mt "Боюсь, что встречу ту кошмарную лесбиянку."
    mt "Как вспомню этот ужас в хостеле..."
    mt "Нет! Даже думать об этом не хочу!"
    mt "Тоже мне, дешевый ночлег!"
    mt "!!!"
    mt "Хммм..."
    mt "Кстати, о дешевом ночлеге..."

    if ep211_julia_second_date_completed == False:
        # если нет отношений с Юлией и Моника не задумывалась ранее об аренде квартиры
        mt "И почему я раньше об этом не задумывалась?!"
        mt "У меня сейчас есть работа. Заработок у меня стабильный."
        mt "Возможно, мне удастся арендовать какую-нибудь небольшую квартиру?"
        mt "По-моему, это хорошая идея!"
        mt "Я, наконец-то, перестану работать на эту семейку идиотов!"
        mt "И жить независимо ни от кого!!!"
        mt "Только как мне подобрать подходящую по цене квартиру?"
        mt "..."
        #
    else:
        # если Моника была в гостях у Юлии и задумывалась об аренде квартиры
        mt "Юлия снимает квартиру в ужасном доме!"
        mt "Но стоит признать, что квартира у нее довольно уютная."
        mt "Конечно, там все старое и убогое..."
        mt "Но все же я была бы не против жить в подобной квартире."
        mt "Представь только, Моника!"
        mt "Никто не будет тебе указывать, что делать и какую одежду носить..."
        mt "Никто не будет ограничивать тебя в еде или в походах в душ..."
        mt "..."
        #

    mt "Кто может знать, где найти дешевое жилье?"
    mt "???"
    mt "В прошлый раз продавец шавермы посоветовал мне хостел..."
    mt "Возможно, стоит спросить у него?"
    return

# трущобы, рядом с шавермой
label ep211_dialogues6_slum_apartment_2:
    # не рендерить!
    mt "Уверена, он знает какое-нибудь дешевое жилье."
    mt "Мне эта идея настолько понравилась..."
    mt "И почему я раньше об этом не подумала?"
    return

# разговор с продавцом шавермы, при клике на него
label ep211_dialogues6_slum_apartment_3:
    menu:
        "Разговор...":
            return 0
        "Спросить про апартаменты...":
            if day_time == "evening":
                mt "Не хочу вести такие разговоры посреди ночи..."
                mt "Лучше приду {c}завтра днем{/c}"
                return -1
            music DarxieLand
            img 16940
            with fadelong
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            m "Нет. Мне не нужен твой кебаб!"
            m "..."
            $ monicaShawarmaApartment1 = True # Моника спросила у продавца шавермы про квартиру
            pass
        "Уйти отсюда.":
            if day_time == "evening":
                return -1
            music DarxieLand
            img 16940
            with fadelong
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            img 16941
            with fade
            mt "Нет, я пока не готова тратить деньги на апартаменты."
            mt "Мне это сейчас не по карману."
            music Pyro_Flow
            img 16942
            with diss
            m "Сам ешь свой отвратительный кебаб!"
            # если называла его животным
            if shawarmaTraderOffended1 == True:
                #
                $ notif(t_("Моника называла продавца шавермы животным"))
                #
                img 16943
                with diss
                mt "Животное!"
            #
            m "!!!"
            return -1

    if ep211_dialogues6_slum_apartment_3_flag1 == False:
        # ехидно смотрит на него
        img 16942
        with fade
        m "Я хотела кое-что у тебя спросить..."
        img 16944
        with diss
        shawarma "Все, что Мадаме захотеть, Джек все сделать!"
        shawarma "Для прекрасной Мадаме Джеку ничего не жалко!"
        music Hidden_Agenda
        img 16945
        with fade
        m "Мне..."
        m "..."
        m "Одной моей знакомой нужны апартаменты."
        img 16946
        with diss
        m "Она хочет их арендовать..."
        m "За небольшую плату."
        m "Ты знаешь, где можно найти что-то подходящее?"
        music DarxieLand
        img 16947
        with fade
        shawarma "О, Мадаме!"
        shawarma "Вы правильно сделали, что пришли ко мне!"
        shawarma "Джек все здесь знать!"
        shawarma "Для восхитительной Мадаме у Джека есть апрартаменты!"
        img 16948
        with diss
        m "Это... Это не для меня квартира..."
        shawarma "Мадаме может не волноваться."
        shawarma "Джек никому не рассказывать!" # подмигивает ей
        img 16949
        with fade
        m "!!!"
        m "Так у тебя есть апартаменты под аренду?" # воодушевленно
        img 16944
        with diss
        shawarma "Конечно, Мадаме!!!"
        shawarma "И как раз сейчас они свободны!"
        shawarma "Это шикарный апрартамент! Мадаме будет очень доволен!"
        shawarma "И всего за 50 долларов за один неделя!"
        shawarma "Прекрасный Мадаме не найдет ничего дешевле!"
        music RnB3_65
        img 16950
        with fade
        mt "Всего 50 долларов в неделю?!"
        mt "Боже! Я не верю в эту удачу!"
        mt "Наконец-то!"
        img 16951
        with diss
        mt "..."
        mt "Хотя... Это не такие уж маленькие деньги для меня сейчас..."
        mt "!!!"
        mt "Интересно, что это за апартаменты?"
        music DarxieLand
        img 16945
        with fade
        m "А где эти апартаменты находятся?"
        shawarma "Недалеко отсюда, Мадаме!"
        $ ep211_dialogues6_slum_apartment_3_flag1 = True

# если отказалась идти смотреть квартиру, диалог начнется с этого момента
    img 16940
    with diss
    shawarma "Мадаме хочет посмотреть свой будущий шикарный апрартамент?"
    m "..."
    $ menu_price = [50]
    menu:
        "Согласиться.": #corruption
            $ monicaShawarmaApartment2 = True # Моника сразу согласилась посмотреть квартиру продавца шавермы
            pass
        "Нет. $ 50 в неделю - это слишком дорого.":
            music Groove2_85
            img 16941
            with fade
            mt "Я пока не готова тратить деньги на жилье."
            mt "Мне это сейчас не по карману."
            img 16942
            with diss
            m "Нет."
            m "Мне нужно еще подумать."
            music DarxieLand
            img 16944
            with fade
            shawarma "Если Мадаме надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадаме!"
            return -1
    # подозрительно
    music Hidden_Agenda
    img 16945
    with fade
    m "А там никто больше не будет жить, кроме меня?"
    music DarxieLand
    img 16947
    with diss
    shawarma "Конечно, нет!"
    shawarma "Мадаме будет хозяйкой в этот шикарный апрартамент!"
    img 16946
    with fade
    m "Отлично!"
    m "Я хочу их посмотреть!"
    $ questHelp("flat_slums_1", True)
    $ questHelp("flat_slums_2", skipIfExists=True)
    # Некоторое время спустя Моника и животное оказываются в новой локации перед страшным домом в трущобах
    return 1

# Моника возле дома, где будет снимать квартиру (глазик)
label ep211_dialogues6_slum_apartment_4:
    # не рендерить!
    mt "Этот дом просто кошмарный!!!"
    return False

# Моника с животным возле дома, где будет снимать квартиру
label ep211_dialogues6_slum_apartment_5:
    # стоит возле дома, Джек стоит рядом
    mt "Жуть!!!"
    mt "Он что-то говорил про шикарные апартаменты?"
    mt "Шикарные апартаменты в ТАКОМ доме?!"
    mt "???"
    m "Ты уверен, что апартаменты хорошие?"
    shawarma "Конечно, Мадаме!"
    shawarma "Там есть очень большой комнат!"
    shawarma "Отдельный кухня!"
    shawarma "И даже отдельный душ!"
    shawarma "Мадаме идти за мной и сам все посмотреть!"
    m "..."
    return

# квартира Моники
label ep211_dialogues6_slum_apartment_6:
    # Моника стоит посередине квартиры
    music Groove2_85
    img 16968
    with fadelong
    w
    img 16953
    with vpunch
    w
    img 16954
    with diss
    m "Куда ты меня привел?!"
    m "Это что?! Квартира?!"
    m "?!?!?!"
    music DarxieLand
    img 16955
    with fade
    shawarma "Да, Мадаме!"
    shawarma "Теперь это Ваш шикарный апрартамент!"
    music Power_Bots_Loop
    img 16956
    with hpunch
    m "Шикарный?!"
    m "Да ты охренел?!"
    music DarxieLand
    img 16957
    with fade
    shawarma "В этот прекрасный апрартамент раньше жить рабочие."
    m "Рабочие?!"
    img 16958
    with diss
    shawarma "Да! Они делать ремонт в очень богатых местах!"
    shawarma "Может быть, Мадаме слышать про отель Ле Фгранд или офис Модный Журнал?"
    music Power_Bots_Loop
    img 16959
    with fade
    m "!!!"
    music DarxieLand
    img 16960
    with diss
    shawarma "Рабочий, который делать такую хорошую работу, всегда любить комфорт и чистота."
    shawarma "Они бы не жить здесь, если бы это место не быть таким хорошим!"
    img 16961
    with fade
    m "..."
    m "А что это за убогая картина?! Это тоже от рабочих?"
    img 16962
    with diss
    shawarma "Нет, Мадаме."
    shawarma "Еще раньше здесь жить прекрасный женщин, чистый ангел!"
    shawarma "Он оказывать здесь небольшие услуги уважаемым жителям нашей улица!"
    music Power_Bots_Loop
    img 16963
    with fade
    mt "Боже! Какой кошмар!"
    music DarxieLand
    img 16964
    with diss
    shawarma "Ну что? Мадаме будет жить в этот шикарный квартир?"
########
    img 17053
    with fade
    shawarma "Джек специально для Мадаме приготовить самый восхитительный напиток!"
    shawarma "Напиток богов!"
    # указывает на столик с мохито
    shawarma "Вот он, Мадаме!"
    shawarma "Великолепный махит для прекрасный леди!"
    music Groove2_85
    img 17054
    with diss
    m "..."
    m "Я не пью!"
    music DarxieLand
    img 16985
    with fade
    shawarma "А здесь и нет алкоголь, Мадаме!"
    shawarma "Я просто налить воды из крана!"
    shawarma "Джек стараться специально для Вас!"
    img 17055
    with diss
    shawarma "В этот апартмент есть шикарный кухня, где можно делать махит каждый день!"
    shawarma "А потом садиться на этот прекрасный стул для пляж!"
    shawarma "И наслаждаться этот изумительный вид из окна!" # указывает на окно
    music Groove2_85
    img 16978
    with fade
    m "Ты что, издеваешься?!"
    m "Где здесь окно с изумительным видом?!"
    m "!!!"
    music DarxieLand
    img 17056
    with diss
    shawarma "А Мадаме пить напиток богов и представлять, что за теми домами океан!"
    shawarma "Чистейший песок, прозрачный волны и крики чаек..."
    img 17057
    with fade
    shawarma "Тут даже есть рыбка на стене! Смотрите, Мадаме!" # на рыбку
    m "О Божееее!!!"
    m "..."
    img 17058
    with diss
    shawarma "Я же Вам говорить, что Джек стараться для прекрасной Мадаме!"
    shawarma "Мадаме сейчас платить Джек деньги за шикарный апартамент..."
    shawarma "И сразу может оставаться здесь жить! И пить махит каждый день!"
    music Groove2_85
##########
    m "..."
    $ menu_price = [50]
    menu:
        "Согласиться.":
            $ monicaShawarmaApartment3 = True # Моника посмотрела квартиру и согласилась ее арендовать (50 баксов)
            pass
        "Уйти отсюда!":
            music Power_Bots_Loop
            img 16965
            with hpunch
            m "Я не буду жить в этой!"
            m "В этой!"
            m "В этом пристанище для бомжей!!!"
            m "!!!"
            music DarxieLand
            img 16966
            with fade
            shawarma "Если Мадаме надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадаме!"
            if shawarmaTraderOffended1 == True:
                # если называла его животным
                #
                $ notif(t_("Моника называла продавца шавермы животным"))
                #
                music Power_Bots_Loop
                img 16967
                with diss
                mt "Животное!"
                #
            m "!!!"
            # Моника уходит
            return 0
    music Groove2_85
    img 16967
    with fade
    mt "Может быть, стоит арендовать эту грязную дыру?"
    mt "Всего 50 долларов в неделю..."
    mt "..."
    img 16969
    with diss
    mt "Это ведь на какое-то время."
    mt "Потом я подберу себе жилье получше."
    img 16970
    with fade
    m "Я... Я согласна арендовать эти ужасные апра... апартаменты ненадолго."
    music DarxieLand
    shawarma "Отлично! Мадаме сделать правильный решение!"
    shawarma "Джек очень счастлив, что такой восхитительный женщин будет жить в его апрартамент!"
    img 16971
    with diss
    m "Когда требуется оплата, прямо сейчас? Я сразу смогу здесь жить?"
    img 16972
    with diss
    shawarma "Конечно, Мадаме сразу может тут остаться и жить!"
    shawarma "Только Джеку сначала нужен документ Мадаме..."
    music Power_Bots_Loop
    img 16973
    with diss
    mt "Документы?!"
    mt "Дъявол!!!"
    mt "!!!"
    mt "Что же делать?!"
    music Hidden_Agenda
    img 16974
    with fade
    m "Я... Я не хотела бы показывать свои документы..."
    m "Тем более, у меня их нет с собой..."
    img 16975
    with diss
    m "Я их забыла дома..."
    m "..."
    m "Без документов никак нельзя?"
    music DarxieLand
    img 16976
    with fade
    shawarma "Если Мадаме хочет снять этот квартир без документ..."
    shawarma "То Джек легко помочь Мадаме с этим!"
    shawarma "Этот прекрасный апартамент не входит в жилой фонд..."
    img 16966
    with diss
    shawarma "Поэтому здесь нет злой проверяющий миграционных бумаг!"
    shawarma "И такой прекрасный леди мочь жить здесь без документ!"
    music Groove2_85
    img 16977
    with fade
    m "В таком случае, мы договорились."
    m "Я арендую эту ужасную квартиру!"
    music DarxieLand
    img 16962
    with diss
    shawarma "Прекрасно! Джек счастлив помочь такой восхитительный женщин!"
    shawarma "Этот шикарный квартир будет стоить всего 300 долларов в неделю для Мадаме!"
    music Power_Bots_Loop
    img 16956
    with hpunch
    m "!!!"
    m "ЧТО?!"
    m "Ты же говорил, что она стоит $ 50 в неделю!"
    m "Почему сейчас стало $ 300?!"
    m "?!?!?!"
    music DarxieLand
    img 16957
    with fade
    shawarma "Специально для Мадаме!"
    shawarma "Документ есть - апартамент стоит $ 50 в неделю!"
    shawarma "Документ нет - апартамент стоит $ 300 в неделю!"
    img 16964
    with diss
    shawarma "Джек все для Вас готов сделать, Мадаме!"
    shawarma "Мадаме никакой квартир больше не найдет, если у нее нет документ!"
    shawarma "Да еще и по специальный цена!"
    music Groove2_85
    img 16978
    with fade
    m "Апартаменты в трущобах за 300 долларов в неделю?!"
    m "?!?!?!"
    img 16959
    with diss
    mt "Вот сволочь!"
    mt "!!!"
    mt "300 долларов в неделю..."
    mt "..."
    $ menu_price = [slumsApartmentsRentPrice]
    menu:
        "Согласиться.":
            $ monicaShawarmaApartment4 = True # Моника согласилась арендовать квартиру за 300 баксов
            pass
        "Уйти отсюда!":
            music Power_Bots_Loop
            img 16965
            with hpunch
            m "Я не буду жить в этом!"
            m "В этом пристанище для бомжей!!!"
            m "Да еще и за такие деньги!"
            m "!!!"
            music DarxieLand
            img 16966
            with fade
            shawarma "Если Мадаме надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадаме!"
            if shawarmaTraderOffended1 == True:
                # если называла его животным
                #
                $ notif(t_("Моника называла продавца шавермы животным"))
                #
                music Power_Bots_Loop
                img 16967
                with diss
                mt "Животное!"
                #
            m "!!!"
            # Моника уходит
            return -1
    music Groove2_85
    img 16979
    with fade
    mt "Вот дъявол!"
    mt "Мне не удастся снять жилье без документов..."
    mt "Получается, что это единственный вариант, который я могу найти..."
    mt "..."
    music DarxieLand
    img 16980
    with diss
    shawarma "Мадаме жить один и Джек ее не беспокоить совсем."
    shawarma "Только один раз в неделю Джек приходить за деньгами."
    music Groove2_85
    img 16981
    with fade
    mt "И что мне делать?"
    mt "???"
    mt "С другой стороны... Это будет МОЕ жилье... МОЕ!!!"
    music RnB3_65
    img 16982
    with diss
    mt "О том, где я живу, никто не будет знать..."
    mt "Я буду сама себе хозяйка..."
    mt "И больше никакие никчемные деревенщины мною не будут командовать!"
    # поворачивается к Джеку
    music Groove2_85
    img 16955
    with fade
    shawarma "Мадаме согласен?"
    m "Деньги платить сейчас?"
    shawarma "Да. Сейчас."
    shawarma "И Мадаме может сразу оставаться жить здесь."
    img 16970
    with diss
    m "Следующая оплата ровно через неделю?"
    music DarxieLand
    shawarma "Джек будет приходить {c}каждая суббота утро{/c} за деньгами."
    shawarma "Мадаме платить и оставаться здесь жить!"
    m "..."
    $ menu_price = [slumsApartmentsRentPrice]
    menu:
        "Заплатить $ 300 за апартаменты.":
            $ monicaShawarmaApartment5 = True # Моника внесла первую оплату Джеку за квартиру
            pass
    $ add_money(-slumsApartmentsRentPrice)
    # у Моники списываются с баланса деньги
    img 16983
    with fade
    shawarma "Джек счастлив помочь прекрасной Мадаме!"
    shawarma "Джек придти за деньгами в следующий суббота."
    img 16987
    with diss
    shawarma "Вот ключи от Ваш шикарный апартамент!"
    # ключи кладет куда-нибудь на стол и уходит
    $ add_inventory("keys_apartments", 1, True)
    img 16984
    with fade
    sound man_steps
    shawarma "До суббота, прекрасный леди!"
    img 16986
    with diss
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    m "..." # смотрит на него недовольно
    # Джек уходит
    # затемнение экрана, несколько минут спустя
    # Моника стоит возле гардероба
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_2
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16988
    with fadelong
    mt "Это еще что?!"
    mt "?!?!?!"
    mt "Это одежда тех рабочих, про которых говорил этот идиот?"
    img 16990
    with fade
    mt "Фууу! Она же грязная! От нее воняет!!!"
    mt "Какого дъявола он ее здесь оставил?!"
    mt "!!!"
    img 16989
    with diss
    mt "Нужно будет принести сюда свои наряды..."
    mt "А это все - вышвырнуть в мусорку!!!"
    mt "Я наведу здесь порядок!"
    # затемнение экрана, несколько минут спустя
    # Моника подходит к деревянной тумбочке и, открыв ее, находит там домашнюю одежду
    scene black_screen
    with Dissolve(1)
    sound highheels_short_walk
    pause 1.5
    img 16991
    with fadelong
    mt "А это еще что за ящик?!"
    mt "Может, там что-то есть?"
    img 16992
    with fade
    mt "Хммм... Это даже не одежда... Просто какие-то дешевые тряпки..."
    mt "Фи!"
    mt "..."
    mt "Хотя..."
    mt "Эта одежда выглядит относительно новой... И чистой..."
    mt "А у меня нет домашней одежды..."
    mt "..."
    img 17051
    with diss
    mt "Не буду же я ходить здесь в своем платье или в этом ужасном костюме!"
    mt "От этого отвратительного костюма меня уже тошнит!"
    mt "А платье я могу здесь испачкать!"
    img 17052
    with fade
    mt "Почему бы мне не носить это дома?"
    mt "Меня все равно никто в этом не увидит."
    mt "..."
    mt "Мне нужно примерить эту одежду."
    # переодевается и смотрит на себя в зеркало. если нет зеркала, то просто смотрит на себя
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 16993
    with fadelong
    mt "..."
    mt "Выглядит, конечно, ужасно..."
    mt "Дешевые, ношенные кем-то тряпки! Фи!"
    w
    img 16994
    with fade
    mt "И я догадываюсь, кто носил это раньше..."
    mt "..."
    mt "Но это неважно..."
    mt "Теперь эта домашняя одежда МОЯ!"
    img 16995
    with diss
    w
#    $ log1 = t_("Заработать $ 300 за аренду апартаментов до субботы.")
#    $ log1 = t_("У меня теперь есть место, где я могу жить. Апартаменты в трущобах... Но это лучше, чем подвал в доме, где живет семейка идиотов.") # квест-лог
    return

# квартира Моники, сразу после ухода Джека
label ep211_dialogues6_slum_apartment_7:
    # Моника стоит посередине квартиры оглядывается
    # не рендерить!
    mt "Это самое жуткое место, которое я видела в своей жизни!"
    mt "Ни в коем случае нельзя, чтобы кто-нибудь узнал, что Моника Бакфетт живет здесь!"
    mt "!!!"
    mt "С другой стороны..."
    mt "Теперь у меня есть МОЕ жилье!"
    mt "Я могу послать к черту эту дуру Бетти и ее мужа-подкаблучника!"
    mt "Хотя... Наверное пока не стоит этого делать..."
    mt "Вдруг у меня не окажется денег на продление аренды..."
    mt "Но, все равно, Я теперь независима от них!"
    mt "Это маленький шаг навстречу к моей цели."
    mt "Тот день, когда Моника Бакфетт вернет себе все, что у нее отняли, становится все ближе!"
    return


# квартира Моники, мысли Моники, когда осматривает квартиру
# лейблы с 8а по 8к не рендерить!
# комната
label ep211_dialogues6_slum_apartment_8a:
    # комната (стены, пол)
    mt "Какое же кошмарное это место!"
    mt "Может, стоит сделать тут небольшой ремонт?"
    return
label ep211_dialogues6_slum_apartment_8b:
    # мусор на полу, бочки и т.п.
    mt "Фи! Какая грязь!"
    mt "Кто сюда притащил весь этот хлам?"
    return
label ep211_dialogues6_slum_apartment_8c:
    # раскладушка
    mt "Это, конечно, не сравнится с моей шикарной кроватью..."
    mt "На которой спит теперь эта сучка Бетти."
    mt "Но все же, на этом можно спать..."
    return
label ep211_dialogues6_slum_apartment_8db:
    mt "Что за кошмарная мебель здесь?!"
    return
label ep211_dialogues6_slum_apartment_8d:
    # деревянные стулья, столик, деревянная рыбка, тумбочка
    mt "Что за кошмарная мебель здесь?!"
    mt "Как на этом можно сидеть, да еще и пить 'махит'?! Фи!"
    return
# кухня
label ep211_dialogues6_slum_apartment_8f:
    # кухня (стены, пол)
    mt "Ужасная кухня!"
#    mt "Я не смогу готовить здесь еду!"
    mt "..."
    mt "Хммм... Здесь есть что-то съедобное..."
    mt "Выглядит неплохо..."
    mt "Если проголодаюсь, возьму немного."
    return
label ep211_dialogues6_slum_apartment_8g:
    # кухонная утварь, посуда
    mt "Эта посуда осталась от прежних жильцов?"
    mt "Фи!"
#    mt "Фи! Я не буду ее трогать!"
    return
# ванная комната
label ep211_dialogues6_slum_apartment_8h:
    # комната (стены, пол)
    mt "Эта ванная комната отвратительна!"
    mt "Я не хочу сюда даже заходить!"
    return
label ep211_dialogues6_slum_apartment_8i:
    # унитаз
    mt "Фууу!"
    mt "Как мне на этом писать?!"
    return
label ep211_dialogues6_slum_apartment_8j:
    # раковина
    mt "Это что за непонятная куча старого хлама?"
    mt "В этом можно как-то умываться и мыть руки?"
    return
label ep211_dialogues6_slum_apartment_8k:
    # душ
    mt "Мне придется мыть свое великолепное тело водой из куска ржавой трубы..."
    mt "..."
    return
label ep211_dialogues6_slum_apartment_8l:
    # мохито на столике в комнате (глазик)
    mt "Мохито из воды... из ржавого крана..."
    mt "Отвратительно!"
    mt "..."
    mt "Хотя..."
    mt "Если мне очень захочется пить, то можно сделать пару маленьких глотков..."
    return
label ep211_dialogues6_slum_apartment_8m:
    # комната (окно)
    mt "Какой отвратительный вид!"
    mt "!!!"
    mt "Мне нужно быть аккуратнее."
    mt "Из окон напротив за мной может подглядывать какой-нибудь извращенец!"
    return


label ep211_dialogues6_slum_apartment_8n:
    # мохито на столике в комнате (hand)
    # если в домашней одежде
    if cloth == "HomeCloth4":
        music Groove2_85
        img 17062
        with fadelong
        w
    # если голая
    if cloth == "Nude":
        music Groove2_85
        img 17063
        with fadelong
        w
    # если в полотенце
    if cloth == "BathCloth1":
        music Groove2_85
        img 17076
        with fadelong
    mt "Мне очень хочется пить..."
    mt "Пожалуй, можно сделать пару маленьких глотков..."
    return

# Моника в квартире в домашней одежде (глазик)
label ep211_dialogues6_slum_apartment_9:
    # не рендерить!
    mt "Хорошо, что никто не увидит меня в этой дешевой одежде..."
    mt "О том, что ее до меня носил кто-то, я предпочитаю не думать."
    mt "Джек говорил, что раньше здесь жила какая-то проститутка..."
    mt "..."
    mt "Мне не важно! Эта одежда теперь моя!"
    return

# квартира Моники, вечером в субботу приходит Джек за деньгами
label ep211_dialogues6_slum_apartment_10:
    # стук в дверь, затемнение экрана - шаги, звук открывающейся двери
    music stop
    img black_screen
    with diss
    sound snd_door_knock
    pause 2.0
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music DarxieLand
    img 16996
    with fadelong
    shawarma "Прекрасный Мадаме!"
    shawarma "Джек пришел взять с нее деньги за шикарный апартамент!"
    music Groove2_85
    img 16997
    with fade
    mt "За эту квартиру и $ 50 жалко платить..."
    m "..."
    music DarxieLand
    img 16998
    with diss
    shawarma "Мадаме стал еще прекрасней в этот домашней костюм!"
    shawarma "Джек не может отвести глаз от прелестной Мадаме!"
    img 16999
    with fade
    shawarma "Вы такой яркий сияющий женщин!"
    shawarma "Я подходить к дом и видеть, как он светится, благодаря Ваша красота!"
    music Groove2_85
    img 17000
    with diss
    mt "Когда он уже заткнется и уйдет отсюда?!"
    m "..."
    music DarxieLand
    img 17001
    with fade
    shawarma "Я подумал, что Мадаме слишком прекрасен, чтобы давать Джеку целых $ 300!"
    shawarma "Джек сделать благородный поступок и предложить скидку для Мадаме!"
    img 17002
    with diss
    m "Скидку?"
    img 17003
    with fade
    shawarma "Да!"
    shawarma "Джек сделать скидка в 10 процент, если..."
    shawarma "Мадаме позволит прикоснуться ему к ее красота и целовать Джека!"
    mt "!!!"
    img 17004
    with diss
    shawarma "Но это еще не все!"
    shawarma "Джек сделать очень-очень щедрый скидка для Мадаме. 20 процент!"
    shawarma "Если нефритовый стержень Джека проникать внутрь прекрасный Мадаме!!!"
    music Power_Bots_Loop
    img 17005
    with fade
    m "Что ты несешь?!"
    m "Что это все значит?!"
    music DarxieLand
    img 17006
    with diss
    shawarma "Это значит, Джек предлагать Вам выгодный сделка."
    shawarma "Скидка в 10 или 20 процент."
    music Groove2_85
    img 17007
    with diss
    m "..."
label ep211_dialogues6_slum_apartment_10_loop1:
    $ menu_corruption = [slumsApartmentsRentPriceDiscountCorruption1]
    $ menu_price = [0, slumsApartmentsRentPrice]
    menu:
        "Заплатить со скидкой.": #corruption
            $ menu_price = [slumsApartmentsRentPriceDiscount1]
            menu:
#                "Скидка 10 процентов. (in Extra version) (disabled)" if game.extra != True:
#                    pass
#                "Скидка 10 процентов." if game.extra == True:
                "Скидка 10 процентов.":
                    # Моника с подозрением
                    music Groove2_85
                    img 17008
                    with fade
                    mt "Почему бы мне не воспользоваться его предложением?"
                    mt "Скидка мне не помешает."
                    img 17009
                    with diss
                    m "И что мне сделать, чтобы получить эту скидку?"
                    music DarxieLand
                    img 17010
                    with fade
                    shawarma "У прекрасной Мадаме рот как лепесток роз!"
                    shawarma "Такой же восхитительный и нежный!"
                    shawarma "Джек будет счастлив дать в этот рот свой нефритовый стержень!"
                    music Power_Bots_Loop
                    img 17011
                    with hpunch
                    m "ЧТО?!"
                    m "Да как ты смеешь мне подобное предлагать?!"
                    m "!!!"
                    music DarxieLand
                    img 17012
                    with fade
                    shawarma "Джек делать очень щедрый и благородный предложение Мадаме..."
                    shawarma "Но если Мадаме откажется, Джек на нее не обижаться."
                    shawarma "Тогда она может просто заплатить Джеку $ 300 за шикарный квартир."
                    music Groove2_85
                    img 17013
                    with diss
                    mt "Черт!"
                    mt "И что же мне делать?"
                    mt "10 процентов от $ 300 - это немало."
                    mt "А у меня сейчас каждый цент на счету."
                    m "..."
                    $ menu_corruption = [slumsApartmentsRentPriceDiscount10Corruption]
                    menu:
                        "Согласиться.": #corruption
                            $ monicaShawarmaApartment6 = True # Моника согласилась сделать минет за скидку в 10 процентов
                            # переход к лейблу ep211_dialogues6_slum_apartment_11
                            $ questHelp("flat_slums_3", True)
                            return 2
                        "Ни за что!!!":
                            music Power_Bots_Loop
                            img 17014
                            with hpunch
                            if questHelpFlag18 == False:
                                $ questHelp("flat_slums_3", False)
                            m "Ты что, ненормальный?!"
                            m "Конечно, я не буду этого делать!"
                            m "Как ты мог вообще до такого додуматься!!!"
                            if shawarmaTraderOffended1 == True:
                                # если называла его животным
                                #
                                $ notif(t_("Моника называла продавца шавермы животным"))
                                #
                                img 17015
                                with diss
                                mt "Животное!"
                                #
                            m "!!!"
                            music DarxieLand
                            img 16962
                            with fade
                            shawarma "Тогда Мадаме платить Джеку $ 300."
                            # jump на первоначальное меню
                            $ questHelp("flat_slums_3", False, skipIfTrue=True)
                            jump ep211_dialogues6_slum_apartment_10_loop1
                    return
                "Скидка 20 процентов." if 1==2: #corruption
                    # Моника с подозрением
                    music Groove2_85
                    img 17008
                    with fade
                    mt "Почему бы мне не воспользоваться его предложением?"
                    mt "Скидка мне не помешает."
                    img 17009
                    with diss
                    m "И что мне сделать, чтобы получить эту скидку?"
                    music DarxieLand
                    img 17010
                    with fade
                    shawarma "Красота Мадаме ослеплять Джека!"
                    shawarma "Мадаме прекрасна как древнегреческий богинь!"
                    shawarma "Джек будет счастлив, если она позволит..."
                    shawarma "Проникнуть нефритовый стержень Джека в ее сладкий дырочка!"
                    music Power_Bots_Loop
                    img 17011
                    with hpunch
                    m "ЧТО-О-О-О?!"
                    m "?!?!?!"
                    m "Да как ты смеешь мне подобное предлагать?!"
                    m "!!!"
                    music DarxieLand
                    img 17012
                    with fade
                    shawarma "Джек делать очень щедрый и благородный предложение Мадаме..."
                    shawarma "Но если Мадаме откажется, Джек на нее не обижаться."
                    shawarma "Тогда она может просто заплатить Джеку $ 300 за шикарный квартир."
                    music Groove2_85
                    img 17013
                    with diss
                    mt "Черт!"
                    mt "И что же мне делать?"
                    mt "20 процентов от $ 300 - это немало."
                    mt "А у меня сейчас каждый цент на счету."
                    m "..."
                    menu:
                        "Согласиться.": #corruption
                            $ monicaShawarmaApartment7 = True # Моника согласилась заняться сексом за скидку в 20 процентов
                            # переход к лейблу ep211_dialogues6_slum_apartment_12
                            return
                        "Ни за что!!!":
                            music Power_Bots_Loop
                            img 17014
                            with hpunch
                            m "Ты что, ненормальный?!"
                            m "Конечно, я не буду этого делать!"
                            m "Как ты мог вообще до такого додуматься!!!"
                            # если называла его животным
                            #
                            $ notif(t_("Моника называла продавца шавермы животным"))
                            #
                            img 17015
                            with diss
                            mt "Животное!"
                            #
                            m "!!!"
                            music DarxieLand
                            img 16962
                            with fade
                            shawarma "Тогда Мадаме платить Джеку $ 300."
                            # jump на первоначальное меню
                            return
                    return
                "Назад.":
                    jump ep211_dialogues6_slum_apartment_10_loop1
            return
        "Заплатить $ 300":
            # Моника с деловым видом
            music Groove2_85
            img 17016
            with fade
            m "Мне не нужны никакие скидки!"
            m "Я готова заплатить сумму полностью."
            m "Забирай деньги и иди!"
            $ add_money(-slumsApartmentsRentPrice)
            music DarxieLand
            img 17017
            with diss
            shawarma "Отлично, Мадаме! Джек очень рад!"
            shawarma "Джек придет в {c}следующий суббота утро{/c}!"
            shawarma "И Мадаме может не сомневаться!"
            img 17018
            with fade
            shawarma "Джек очень благородный и щедрый!"
            shawarma "Он снова предлагать Мадаме скидку в следующий суббота!"
            music Groove2_85
            img 17019
            with diss
            m "Все! Иди! Мне некогда!"
            # $ 300 списываются с баланса Моники, Джек уходит
            # лейбл ep211_dialogues6_slum_apartment_19 (про квартиру и ремонт)
            music Groove2_85
            img 17015
            with diss
            mt "Животное!"
            mt "Как хорошо, что я его целую неделю теперь не увижу!"
            $ monicaShawarmaApartment8 = True # Моника заплатила $ 300 за квартиру (без скидки)
            $ questHelp("flat_slums_3", False, skipIfTrue=True)
            return 1
        "У меня нет денег.":
            # Моника нерешительно
            music Groove2_85
            img 17013
            with fade
            mt "Что же мне делать?"
            mt "У меня не хватает денег на оплату..."
            mt "Может, он согласится подождать несколько дней?"
            m "..."
            music Hidden_Agenda
            img 17016
            with diss
            m "Я тебе смогу заплатить за апартаменты через несколько дней."
            m "Ты же не выселишь такую прекрасную леди, как я, на улицу?"
            m "Всего лишь несколько дней и я все оплачу."
            music DarxieLand
            img 17017
            with fade
            shawarma "Нет-нет, Мадаме!"
            shawarma "Джек восхищается Вашей красотой."
            shawarma "Но Джек с Мадаме договорился, что деньги будут каждый суббота."
            img 17018
            with diss
            shawarma "Нет денег в суббота - нет шикарный апрартамент у Мадаме!"
            shawarma "Джеку, конечно, очень жаль..."
            shawarma "Но он вынужден выселять прекрасный леди прямо сейчас!"
            # затемнение экрана. Моника оказывается на улице (переход к лейблу ep211_dialogues6_slum_apartment_13)
            $ monicaShawarmaApartment9 = True # Джек выселил Монику за неуплату
            $ questHelp("flat_slums_3", False, skipIfTrue=True)
            return -1
    return

# если выбран пункт меню 'Скидка 10 процентов' и 'Согласиться'
label ep211_dialogues6_slum_apartment_11:
    call check_skip_scene("ep211_dialogues6_slum_apartment_11") from _rcall_check_skip_scene_1
    if _return == True:
        return True


    # Моника смотрит на Джека зло
    music Groove2_85
    img 17020
    with fade
    m "10 процентов - это сколько?"
    music DarxieLand
    img 17021
    with diss
    shawarma "Целых $ 30, Мадаме!"
    shawarma "Джек делать очень щедрый предложение для Вас!"
    music Groove2_85
    img 17000
    with fade
    mt "Черт!"
    mt "Если я соглашусь, я сэкономлю целых $ 30!"
    mt "..."
    music Power_Bots_Loop
    img 17015
    with diss
    m "Если об этом узнает хоть одна живая душа!!!"
    m "!!!"
    music DarxieLand
    img 16980
    with fade
    shawarma "Что Вы, Мадаме?!"
    shawarma "Джек честный и благородный!"
    shawarma "Джек никому не рассказать о Мадаме!"
    music Power_Bots_Loop
    img 17014
    with diss
    m "Если кто-то узнает, я тебя убью!"
    music DarxieLand
    img 16996
    with fade
    shawarma "Прекрасный Мадаме может не переживать!"
    shawarma "Джек дает слово мужчины!"
    # Джек расстегивает штаны и достает свой причиндал
    music Groove2_85
    img 17022
    with diss
    mt "Моника, до чего ты докатилась?"
    mt "Ты собралась делать минет какому-то неудачнику за скидку..."
    mt "..."
    img 17023
    with diss
    mt "Но об этом ведь никто не узнает..."
    mt "Тем более он даже не догадывается кто я такая..."
    mt "..."
    mt "А я сэкономлю деньги."
    # Моника опускается на колени перед ним
    img 17024
    with fade
    mt "Фу! Не могу поверить, что я делаю это..."
    mt "И, главное, кому?!"
    mt "Фу!!!"
    mt "!!!"
    # минет
    music stop
    img black_screen
    with diss
    pause 1.0
    music2 Loved_Up
    img 17025
    with fadelong
    shawarma "О, прекрасный Мадаме!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_MonicaHome_Jack_Blowjob1_1.ogg"
    scene black
    image videov_MonicaHome_Jack_Blowjob1_1 = Movie(play="video/v_MonicaHome_Jack_Blowjob1_1.mkv", fps=30)
    show videov_MonicaHome_Jack_Blowjob1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

#    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 17026
    with fade
    shawarma "Словно лепестки роз ласкают мой нефритовый стержень!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_MonicaHome_Jack_Blowjob1_1.ogg"
    scene black
    image videov_MonicaHome_Jack_Blowjob1_2 = Movie(play="video/v_MonicaHome_Jack_Blowjob1_2.mkv", fps=30)
    show videov_MonicaHome_Jack_Blowjob1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17027
    with diss
    shawarma "Такие нежный и сладкий губы и ротик у Мадаме."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_MonicaHome_Jack_Blowjob1_1.ogg"
    scene black
    image videov_MonicaHome_Jack_Blowjob1_3 = Movie(play="video/v_MonicaHome_Jack_Blowjob1_3.mkv", fps=30)
    show videov_MonicaHome_Jack_Blowjob1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17028
    with fade
    shawarma "Джек готов наслаждаться этим вечно!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_MonicaHome_Jack_Blowjob1_1.ogg"
    scene black
    image videov_MonicaHome_Jack_Blowjob1_4 = Movie(play="video/v_MonicaHome_Jack_Blowjob1_4.mkv", fps=30)
    show videov_MonicaHome_Jack_Blowjob1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17029
    with diss
    shawarma "О, Мадаме! Поласкайте мой стержень своим нежным языком!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_MonicaHome_Jack_Blowjob1_1.ogg"
    scene black
    image videov_MonicaHome_Jack_Blowjob1_5 = Movie(play="video/v_MonicaHome_Jack_Blowjob1_5.mkv", fps=30)
    show videov_MonicaHome_Jack_Blowjob1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")

    img 17030
    with fade
    shawarma "Да, восхитительно!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.5) + " loop 0.0>Sounds/v_MonicaHome_Jack_Blowjob1_1.ogg"
    scene black
    image videov_MonicaHome_Jack_Blowjob1_6 = Movie(play="video/v_MonicaHome_Jack_Blowjob1_6.mkv", fps=30)
    show videov_MonicaHome_Jack_Blowjob1_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    music stop
    music2 stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 17031
    with fade
    shawarma "Мммммм!!!"
    img 17032
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    shawarma "Ещееее!"
    img 17033
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    shawarma "ОООООООО!!!" # кончает
    img 17034
    with fade
    w
    # Моника недовольно вытирает рот
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music DarxieLand
    img 16999
    with fadelong
    shawarma "Мадаме, мне никто не доставлял большего наслаждения, чем Вы!!!"
    shawarma "Джек сдержать свое слово и сделать для Мадаме скидку в 10 процент!"
    $ add_money(-slumsApartmentsRentPriceDiscount1)
    m "..."
    img 17001
    with fade
    shawarma "Джек снова предлагать Мадаме скидку в следующий суббота!"
    music Groove2_85
    img 17007
    with diss
    m "Все! Иди! Мне некогда!"
    # $ 270 списываются с баланса Моники, Джек уходит
    # лейбл ep211_dialogues6_slum_apartment_19 (про квартиру и ремонт)
    music Power_Bots_Loop
    img 16997
    with fade
    mt "Животное!"
    mt "Как хорошо, что я его целую неделю теперь не увижу!"
    mt "Не могу поверить, что я сделала это!!!"
    img 17035
    with diss
    mt "Какая мерзость!!!"
    music Groove2_85
    mt "В следующий раз никаких скидок, Моника!"
    mt "Такой леди, как ты, не пристало заниматься подобными непотребствами!"
    mt "!!!"
    return


# если выбран пункт меню 'Скидка 20 процентов' и 'Согласиться'
label ep211_dialogues6_slum_apartment_12:
    call check_skip_scene("ep211_dialogues6_slum_apartment_12") from _rcall_check_skip_scene_2
    if _return == True:
        return True

    # Моника смотрит на Джека зло
    music Groove2_85
    img 17009
    with fade
    m "20 процентов - это сколько?"
    music DarxieLand
    img 17003
    with diss
    shawarma "Целых $ 60, Мадаме!"
    shawarma "Джек делать очень щедрый предложение для прекрасный леди!!!"
    music Groove2_85
    img 16997
    with fade
    mt "Черт!"
    mt "Если я соглашусь, я сэкономлю целых $ 60!"
    mt "..."
    music Pyro_Flow
    mt "Моника, ты сейчас серьезно?!"
    img 17035
    with diss
    mt "Как ты можешь даже предполагать подобное?!"
    mt "Ты действительно займешься с этим животным сексом за скидку в $ 60?!"
    mt "?!?!?!"
    mt "..."
    music Groove2_85
    img 17008
    with diss
    mt "Но об этом ведь никто не узнает..."
    mt "..."
    mt "А я сэкономлю деньги."
    # с угрозой
    music Power_Bots_Loop
    img 17005
    with hpunch
    m "Я тебя сразу предупрежаю!!!"
    m "Если об этом узнает хоть одна живая душа!!!"
    m "Если ты хотя бы намекнешь кому-то о том, что здесь сейчас будет!!!"
    img 17007
    with diss
    m "Я тебя убью!!!"
    m "!!!"
    m "Ты меня понял?!"
    music DarxieLand
    img 17004
    with fade
    shawarma "Что Вы, Мадаме?!"
    shawarma "Джек честный и благородный!"
    shawarma "Джек никому не рассказать о Мадаме!"
    img 16996
    with diss
    shawarma "Прекрасный Мадаме может не переживать!"
    shawarma "Джек дает слово мужичины!"
    # Джек расстегивает штаны и достает свой причиндал
    img 17036
    with fade
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music DarxieLand
    img 17037
    with fadelong
    shawarma "У Мадаме великолепный попочка!!!"
    shawarma "Сладкий и прекрасный попочка!!!"
    shawarma "Джек очень любить такие!"
    music Power_Bots_Loop
    img 17038
    with fade
    m "Не смей делать какие-нибудь извращенства!"
    music DarxieLand
    img 17001
    with diss
    shawarma "Нет-нет, что Вы, Мадаме."
    shawarma "Джек просто трогать сладкий попочка."
    shawarma "Ммммм, гладкий и упругий... как персик!"
    music Groove2_85
    img 17008
    with fade
    mt "Боже... Когда же он заткнется?!"
    # Моника опирается на стол или кушетку, встает задом к Джеку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 17041
    with fadelong
    w
    img 17042
    with fade
    mt "Фу! Не могу поверить, что я делаю это..."
    mt "!!!"
    # секс
    img 17039
    with diss
    shawarma "О, какой сладкий дырочка у Мадаме!!!"
    img 17040
    with fade
    shawarma "Как тепло и хорошо мой нефритовый стержень!!!"
    img 17043
    with diss
    shawarma "Ооооо, как сладко!!!"
    shawarma "Джек готов наслаждаться этим вечно!"
    img 17044
    with diss
    shawarma "Мммммм!!!"
    img 17045
    with fade
    shawarma "Джек делать прекрасный Мадаме скидка каждый суббот!!!"
    img 17046
    with diss
    shawarma "Оооо, Джек просто на седьмом небе!!!"
    music Loved_Up2
    img 17047
    with diss
    shawarma "Ааааа!!!"
    img 17048
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    shawarma "Мммммм!!!"
    img 17049
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    shawarma "ОООООООО!!!" # кончает
    img 17050
    with fade
    w
    # Моника недовольно вытирает рот
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music DarxieLand
    img 16999
    with fadelong
    shawarma "Мадаме, мне никто не доставлял больший наслаждений, чем Вы!!!"
    shawarma "Джек сдержать свое слово и сделать для Мадаме скидку в 20 процент!"
    m "..."
    img 17001
    with fade
    shawarma "Джек снова предлагать Мадаме скидку в следующий суббота!"
    music Groove2_85
    img 17000
    with diss
    m "Все! Иди! Мне некогда!"
    # лейбл ep211_dialogues6_slum_apartment_19 (про квартиру и ремонт)
    # $ 240 списываются с баланса Моники, Джек уходит
    music Power_Bots_Loop
    img 16997
    with fade
    mt "Животное!"
    mt "Как хорошо, что я его целую неделю теперь не увижу!"
    mt "Не могу поверить, что я сделала это!!!"
    img 17035
    with diss
    mt "Какая мерзость!!!"
    music Groove2_85
    mt "В следующий раз никаких скидок, Моника!"
    mt "Такой леди, как ты, не пристало заниматься подобными непотребствами!"
    mt "!!!"
    return True

# если выбран пункт меню 'У меня нет денег' и Джек выселил Монику
label ep211_dialogues6_slum_apartment_13:
    # Моника стоит на улице перед домом
    # не рендерить!
    mt "Вот скотина!"
    mt "Грязное инстинктивное животное!!!"
    mt "Как он посмел меня выставить на улицу?!"
    mt "?!?!?!"
    mt "Я все равно зайду обратно в квартиру!"
    mt "Ключи же остались у меня!"
    mt "!!!"
    mt "Только нужно дождаться, когда он уйдет из квартиры."
#    $ log1 = t_("Вернуться в квартиру позже.")
    return

# если Моника пытается зайти в квартиру сразу же после того, как Джек ее выставил
label ep211_dialogues6_slum_apartment_14:
    # не рендерить!
    mt "Мне нужно немного позже прийти сюда."
    mt "Это животное еще в квартире..."
    return False

# Моника приходит в квартиру спустя какое-то время
label ep211_dialogues6_slum_apartment_15:
    # Моника стоит на улице перед домом
    # не рендерить!
    sound snd_door_locked1
    pause 1.0
    sound snd_door_locked1
    pause 0.5
    mt "Вот скотина!!!"
    mt "Он поменял замки в моей квартире!!!"
    mt "Сволочь!!!"
    mt "!!!"
    mt "И что мне теперь делать?!"
    mt "Неужели мне придется идти к нему и уговаривать впустить меня обратно?!"
    mt "?!?!?!"
    if money < 300:
        mt "Он все равно меня не впустит. У меня нет денег заплатить за неделю..."
        mt "Мне нужно заработать $ 300."
        mt "Потом я пойду и поговорю с ним."
        mt "Он не сможет отказать мне."
#        $ log1 = t_("Заработать $ 300.")
    if check_inventory("keys_apartments",1) == True:
        $ remove_inventory("keys_apartments", 1, True)
    return

# у Моники на балансе достаточно денег, чтобы заселиться в квартиру снова
# если Моника пришла к дому, где квартира
label ep211_dialogues6_slum_apartment_16:
    sound snd_door_locked1
    pause 1.0
    sound snd_door_locked1
    pause 0.5
    # не рендерить!
    mt "Я не могу зайти в свою квартиру..."
    mt "Эта сволочь поменяла замки!"
    mt "Мне нужно пойти к нему."
    if check_inventory("keys_apartments",1) == True:
        $ remove_inventory("keys_apartments", 1, True)
#    $ log1 = t_("Поговорить с Джеком и снова заселиться в квартиру.")
    return

# у Моники на балансе достаточно денег, чтобы заселиться в квартиру снова
# если Моника пришла к шаверме
label ep211_dialogues6_slum_apartment_17:
    menu:
        "Разговор...":
            return 0
        "Спросить про квартиру...":
            if day_time == "evening":
                mt "Не хочу вести такие разговоры посреди ночи..."
                mt "Лучше приду {c}завтра днем{/c}"
                return -1
            music DarxieLand
            img 16940
            with fadelong
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            shawarma "Или Мадаме хочет снова жить в шикарный апрартамент?"
            img 16942
            with fade
            m "Я хочу вернуться в свою квартиру!"
            img 16944
            with diss
            shawarma "Джек не может отказать такой прекрасный леди!"
            shawarma "А у Мадаме есть деньги?"
            img 16945
            with diss
            m "Да!"
            shawarma "Мадаме может заплатить деньги Джеку прямо сейчас."
            shawarma "Джек даст Мадаме новый ключ."
            shawarma "И она может снова жить в шикарный апрартамент Джека!"
            $ menu_price = [slumsApartmentsRentPrice]
            menu:
                "Заплатить $ 300.":
                    $ add_money(-slumsApartmentsRentPrice)
                    music DarxieLand
                    img 16947
                    with fade
                    shawarma "Отлично, Мадаме!"
                    shawarma "Джек счастлив, что прекрасный Мадаме снова будет жить в его апрартамент!"
                    shawarma "Вот Ваш ключ. С возвращенем, прекрасный леди!"
                    if check_inventory("keys_apartments",1) == True:
                        $ remove_inventory("keys_apartments", 1, True)
                    $ add_inventory("keys_apartments", 1, True)
                    music Groove2_85
                    img 16950
                    with diss
                    mt "Наконец-то я могу вернуться в свою квартиру!"
                    mt "!!!"
                    $ monicaShawarmaApartment10 = True # Моника заплатила денег после ее выселения и снова может жить в квартире
                    return 1
                "Нет! Я не готова платить такую сумму!":
                    music Groove2_85
                    img 16943
                    with fade
                    mt "Нет, я пока не готова тратить деньги на жилье."
                    mt "Мне это сейчас не по карману."
                    img 16948
                    with diss
                    m "Я пока не готова заплатить деньги..."
                    shawarma "Если Мадаме передумает, она знать, где найти Джека!"
                    m "..."
                    return -1
            return -1
        "Уйти отсюда.":
            music DarxieLand
            img 16940
            with fadelong
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            shawarma "Или Мадаме хочет снова жить в шикарный апрартамент?"
            music Groove2_85
            img 16943
            with fade
            mt "Нет, я пока не готова тратить деньги на жилье."
            mt "Мне это сейчас не по карману."
            img 16946
            with diss
            m "Я пока не готова заплатить деньги..."
            shawarma "Если Мадаме передумает, она знать, где найти Джека!"
            m "..."
            return -1
    return

# Моника вернулась в квартиру после ее выселения
label ep211_dialogues6_slum_apartment_18:
    # не рендерить!
    mt "Наконец-то я дома!"
    mt "Никогда бы не подумала, что буду рада вернуться сюда!"
    mt "!!!"
    return

    # Если суббота, но Моника ночевала не дома
    $ log1 = t_("Оплата за апартаменты в трущобах.")
    return

# после оплаты аренды в субботу, перед уходом Джек предлагает ей ремонт и мебель в квартире
label ep211_dialogues6_slum_apartment_19:
    music DarxieLand
    img 17021
    with fade
    shawarma "О, Мадаме! Я чуть не забыть!"
    shawarma "Джек мочь сделать полезный дело для прекрасный Мадаме!"
    music Groove2_85
    img 17020
    with diss
    mt "???"
    m "Какое еще полезное дело?" # подозрительно
    music DarxieLand
    img 17012
    with fade
    shawarma "Джек привозить для Мадаме новый мебель и делать ремонт!"
    img 17059
    with diss
    m "Серьезно?!"
    m "?!?!?!"
    img 17003
    with fade
    shawarma "Все ради Вас, прекрасный леди!"
    shawarma "Джек очень благородный и хорошо относиться к Мадаме!"
    # если был секс
    shawarma "Ведь Мадаме пускать нефритовый стержень Джека в свой чудесный дырочка!!!"
    #
    $ notif(t_("У Моники был секс с Джеком."))
    #
    # если секса не было
    shawarma "Ведь Мадаме когда-нибудь пускать нефритовый стержень Джека в свой чудесный дырочка!!!"
    music Groove2_85
    img 17000
    with diss
    mt "О, Боже!!!"
    mt "Он опять несет эту чушь! Это отвратительно!!!"
    mt "!!!"
    img 17009
    with fade
    m "Ты правда сделаешь тут ремонт?" # с подозрением
    m "И привезешь новую мебель?"
    music DarxieLand
    img 17010
    with diss
    shawarma "Конечно, Мадаме!"
    shawarma "Джек сделать это специально для Вас!"
    m "Когда ты это сделаешь?"
    shawarma "Как только Мадаме платить - Джек мебель привозить!"
    img 17019
    with fade
    m "То есть я заплачу за ремонт и мебель и ты эту сумму вычтешь из арендной платы?"
    img 17018
    with diss
    shawarma "Нет, Мадаме."
    shawarma "Вы платить - Джек привозить."
    shawarma "Но аренда шикарный апартамент оставаться $ 300."
    shawarma "Мебель и ремонт оставаться потом у Джека в апартамент."
    music Groove2_85
    img 17023
    with fade
    mt "Сволочь, мог бы и снизить аренду!"
    mt "!!!"
    music DarxieLand
    img 17017
    with diss
    shawarma "Ну что? Мадаме хочет новый мебель и ремонт?"
    m "..."
    menu:
        "Согласиться (в следующих обновлениях).":

            return
        "У меня нет на это денег.":
            music Groove2_85
            img 17060
            with fade
            m "Я..."
            m "Я пока не буду этого делать..."
            m "Если я передумаю, я скажу тебе об этом."
            m "..."
            music DarxieLand
            img 17061
            with diss
            shawarma "Хорошо, Мадаме."
            shawarma "Джеку будет приятно помочь такой прекрасный леди!"
            # Джек уходит
            $ monicaShawarmaApartment11 = True # Моника отказалась оплачивать ремонт и мебель
            return
    return


label ep211_dialogues6_slum_apartment_20:
    mt "Какой жуткий мусор!"
    mt "И прямо под моим окном!"
    mt "Какой мерзавец посмел оставить это здесь?!"
    mt "В месте, где живет... Стоп... Моника, лучше не называй себя по имени в этом месте."
    mt "Никто не должен узнать кто я на самом деле. Это ведь все временно..."
    return

label ep211_dialogues6_slum_apartment_21:
    mt "Заколоченные окна..."
    mt "Похоже, у меня нет соседей, и это хорошо."
    mt "Меньше никчемных бездельников извращенцев!"
    return

label ep211_dialogues6_slum_apartment_22:
    mt "Одинокое окно..."
    mt "Не могу поверить что это мой новый дом..."
    mt "Но, по крайней мере, у меня есть крыша над головой..."
    return

label ep211_dialogues6_slum_apartment_23:
    mt "Это что, рыба?!"
    return

label ep211_dialogues6_slum_apartment_24:
    mt "Этот маленький светильник светит ночью для меня."
    mt "Он как маленький лучик солнца в моей кошмарной жизни..."
    return

label ep211_dialogues6_slum_apartment_25:
    mt "Какие жуткие лампы..."
    mt "Они напоминают мне освещение в камере у Маркуса..."
    return

label ep211_dialogues6_slum_apartment_26:
    mt "Какая безвкусица!"
    mt "Но я не буду трогать эту картину, боюсь что эта стена держится на ней..."
    mt "Или за картиной окажется огромная дыра или что-нибудь еще..."
    return

label ep211_dialogues6_slum_apartment_27:
    mt "В этом столе больше ничего нет..."
    return

label ep211_dialogues6_slum_apartment_28:
    mt "Жираф..."
    mt "Это портрет хозяина апартаментов?"
    mt "Поражает натуральность визуального сходства!"
    return

label ep211_dialogues6_slum_apartment_29:
    mt "Выход на улицу... На кошмарную улицу..."
    return

label ep211_dialogues6_slum_apartment_30:
    mt "Здесь осталась какая-то еда..."
    mt "Возможно я смогу что-то приготовить себе..."
    return

label ep211_dialogues6_slum_apartment_31:
    mt "Какое-то грязное полотенце..."
    mt "Я не буду его трогать, у меня есть хорошее чистое."
    return
label ep211_dialogues6_slum_apartment_32:
    mt "В это мутное зеркало ничего не видно..."
    return
label ep211_dialogues6_slum_apartment_33:
    mt "Не удивлюсь если в этих ящиках живут тараканы..."
    return

# комментарии Моники
label ep211_dialogues6_slum_apartment_34:
    # Моника встает после дневного отдыха (3 варианта комментария)
#    mt "Как же хорошо, что я теперь сама себе хозяйка. Никакая провинциальная дура теперь не командует мною."
#    mt "Здесь так шумно. Не могу привыкнуть к этому."
#    mt "Я немного задремала, а на улице уже вечер. Что мне сегодня еще нужно сделать?"
    # Моника просыпается (3 варианта комментария)
#    mt "Еще один день в этой ужасной дыре... С другой стороны, здесь все МОЕ. И это не может не радовать."
#    mt "Ужасно неудобное спальное место! У меня такое чувство, что я спала на полу."
#    mt "Если бы у меня получилось сделать здесь ремонт и обновить мебель, здесь стало бы довольно уютно."
    # Моника писает (3 варианта комментария)
#    mt "Фи! Никогда бы не подумала, что моя попа будет прикасаться к такому ужасному унитазу!"
#    mt "Такая красивая женщина, как я, не заслуживает всего, что со мной произошло."
#    mt "Я не собираюсь оставаться в этой ужасной дыре надолго! Скоро я верну себе все!"
    # Моника принимает душ (3 варианта комментария)
#    mt "Я вынуждена мыть свое прекрасное тело в этом жалком подобии душа!"
#    mt "Какой идиот придумал сделать душ из куска ржавой трубы?!"
#    mt "По крайней мере, здесь есть горячая вода..."
    # Моника выходит из душа (3 варианта комментария)
#    mt "Как же хорошо после душа! Я чувствую прилив сил."
#    mt "Моя кожа такая нежная и такая красивая. Она нуждается в королевском уходе, а не в мытье под этим ужасным душем!"
#    mt "И почему в этой ужасной дыре нет ни одного нормального зеркала? Я даже не могу посмотреть на свое прекрасное тело."
    return

label ep211_dialogues6_slum_apartment_34_after_shower:
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Как же хорошо после душа! Я чувствую прилив сил."
    if rnd == 2:
        mt "Моя кожа такая нежная и такая красивая. Она нуждается в королевском уходе, а не в мытье под этим ужасным душем!"
    if rnd == 3:
        mt "И почему в этой ужасной дыре нет ни одного нормального зеркала? Я даже не могу посмотреть на свое прекрасное тело."
    return

label ep211_dialogues6_slum_apartment_35:
    $ rand1 = rand(1,5)
    if rand1 == 1:
        mt "Как же хорошо, что я теперь сама себе хозяйка. Никакая провинциальная дура теперь не командует мною."
    if rand1 == 2:
        mt "Здесь так шумно. Не могу привыкнуть к этому."
    if rand1 == 3:
        mt "Еще один день в этой ужасной дыре... С другой стороны, здесь все МОЕ. И это не может не радовать."
    if rand1 == 4:
        mt "Такая красивая женщина, как я, не заслуживает всего, что со мной произошло."
    if rand1 == 5:
        mt "Я не собираюсь оставаться в этой ужасной дыре надолго! Скоро я верну себе все!"
    return

label ep211_dialogues6_slum_apartment_36:
    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_plates2
    if cloth == "HomeCloth4":
        img 23611
    if cloth == "BathCloth1":
        img 23609
    with fade
    mt "Невкусные продукты..."
    mt "Но, по крайней мере, мне не надо платить за них..."
    return

label ep211_dialogues6_slum_apartment_37:
    if cloth == "HomeCloth4":
        img 23610
    if cloth == "BathCloth1":
        img 23608
    with fade
    mt "Я сегодня уже ела..."
    return
