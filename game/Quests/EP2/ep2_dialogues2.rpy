label monica_shawarma_dialogue0:
    #Моника пришла к кебабу вечером до того как узнала про разноску кебабов (нет рендеров вечера)
    #вечер
    $ store_music()
    music DarxieLand
    img 6159
    shawarma "Я уже закрываюсь!"
    "Приходите завтра!!!"
    #
    $ restore_music()
    $ autorun_to_object("monica_shawarma_dialogue0a")
    return
label monica_shawarma_dialogue0a:
    if shawarmaTraderOffended1 == True:
        mt "Животное!"
    else:
        mt "Вот мерзавец!"
    return
label monica_shawarma_dialogue1:
    #render
    #Моника пришла к кебабу говорить о еде
    #первый раз
    $ store_music()
    music DarxieLand
    img 6084
    shawarma "Мадаме! Снова ВЫ!"
    "Осмелюсь высказать сожаление, Мадаме!"
    img 6085
    m "О чем?!" #раздраженно
    shawarma "О Вашем платье, Мадаме!"
    "Вам оно шло гораздо больше, Мадаме!"
    "Все женщины, в погоне за красотой, в конце концов теряют её!"
    music Hidden_Agenda
    img 6086
    with fade
    m "Ты считаешь что я некрасивая?"
    img 6087
    music DarxieLand
    shawarma "О нет, Мадаме! Вы прекрасны как утренний цветок!"
    img 6088
    m "Какой еще утренний цветок?"
    m "Слушай... У меня к тебе вопрос..."
    img 6089
    shawarma "Да, Мадаме! Я слушаю Вас!"
    music Hidden_Agenda
    img 6090
    with fade
    m "Так я тебе нравлюсь или нет..." #ехидно смотрит
    img 6091
    w
    img 6092
    music DarxieLand
    shawarma "Да, Мадаме! Как утренний цветок!"
    img 6093
    mt "Что за утренний цветок!? Этот идиот несет какую-то чушь..."
    music Hidden_Agenda
    img 6094
    with fade
    m "Ты говорил что у тебя вкусный кебаб?"
    img 6095
    mt "Как же я хочу есть!"
    img 6096
    with fade
    shawarma "Да, Мадаме! Самый вкусный кебаб в округе, Мадаме!"
    img 6097
    m "И ты дашь его попробовать такой красивой девушке как Я?"
    img 6098
    shawarma "Мадаме, я не могу дать Вам мой самый вкусный кебаб, Мадаме!"
    img 6099
    m "Почему это?"
    img 6100
    shawarma "Ваша красота слишком велика, чтобы покупать её, Мадаме!"
    music Stealth_Groover
    img 6101
    m "Причем здесь покупать? Я ничего не собираюсь продавать тебе!"
    #до этого добавить kebab advertising!
    img 6102
    shawarma "Но как же, Мадаме! Вы предложили французский поцелуй за мой вкусный кебаб, Мадаме!"
    music Pyro_Flow
    img 6103
    m "ЧТО Я ПРЕДЛОЖИЛА?!"
    img 6104
    "ЕЩЕ ЧЕГО!!!"
    "Я говорю тебе дай свой кебаб сюда, быстро!"
    img 6105
    shawarma "Хорошо, Мадаме! Только для Вас самый вкусный кебаб за $ 1! Мадаме!"
    img 6118
    w
    img 6119
    with fade
    w
    music DarxieLand
#    if money > 0:
#        call monica_shawarma_dialogue2a() from _call_monica_shawarma_dialogue2a_1
#        return
    #если есть доллар, то уходим на покупку
#    music Stealth_Groover
    img 6106
    mt "Черт! У меня нет этого гребаного доллара!!!"
    img 6107
    m "Можешь дать мне его просто так?"
    img 6108
    shawarma "Нет, Мадаме! Только за $ 1, Мадаме!"
#    music Pyro_Flow
    img 6109
    m "У меня нет этого гребаного доллара! Есть еще какие-то варианты?"
    img 6110
    music DarxieLand
    shawarma "Конечно есть, Мадаме!"
    "Если такой красивый женщин, как Вы, {c}расскажет всем вокруг про мой самый вкусный кебаб{/c}, то кебаб сам будет Вас искать!"
    img 6111
    "Он уже ждет, он хочет чтобы Вы всем рассказали про него!"
    img 6112
    m "Итак, ты хочешь чтобы я кому-то рассказала про тебя?"
    img 6113
    shawarma "Да, Мадаме! Вы разносить всем красивый флаер с рекламой самого вкусного кебаба!"
    "Если Вы разнести все флаер, то вкусный кебаб ждать Вас!"
    music Stealth_Groover
    img 6114
    m "Хорошо, если ты дашь мне сейчас свой кебаб, то {c}я разнесу твои флаеры{/c}..."
    img 6115
    with fade
    w
    music DarxieLand
    img 6116
    shawarma "Нет, Мадаме! Сначала флаер, потом вкусный кебаб!"
    img 6117
    mt "Вот урод!"
    "Неужели мне правда стоит разносить эти флаеры за какой-то кебаб?"
    menu:
        "Согласиться разносить флаеры.":
            music Hidden_Agenda
            img 6120
            mt "О БОЖЕ! Что мне только ни приходится делать чтобы хоть что-то поесть!"
            img 6121
            "Надеюсь я скоро решу это небольшое недоразумение и забуду это как кошмарный сон!"
            img 6122
            with fade
            m "Давай сюда свои флаеры!"
            img 6123
            music DarxieLand
            shawarma "Да, Мадаме! Вам надо надеть это!"
            music stop
            img 6124
            w
            #звук одежды
            sound snd_cardboard1
            img 6125
            with fade
            w
            img 6126
            w
            music Power_Bots_Loop
            img 6127
            m "ЧТО..."
            "ЧТО ЭТО ЗА ХРЕНЬ!?!?!?"
            img 6128
            "ЧТО ТЫ НАЦЕПИЛ НА МЕНЯ?!"
            img 6129
            w
            img 6130
            w
            shawarma "Это условие работа!"
            "Нет реклама, нет вкусный кебаб!"
            img 6131
            w
            img 6132
            w
            music Hidden_Agenda
            img 6133
            m "О БОЖЕ!"
            "Мне придется в этом ходить?!?!"
            img 6134
            mt "Он заплатит за это!"
            "..."
            "Но по крайней мере меня точно никто не узнает в этом!"
            "Я быстро раздам эти долбаные флаеры и забуду этот кошмар!"

            $ monicaKnowAboutKebabWork = True
        "Отказаться.":
            music Power_Bots_Loop
            img 6135
            m "Я не собираюсь ничего разносить! Давай кебаб сюда!"
            img 6136
            shawarma "Нет, Мадаме! Нет флаер, нет кебаб!"
            w
            img 6138
            with fade
            w
            $ autorun_to_object("monica_shawarma_dialogue0a")

    $ restore_music()
    call refresh_scene_fade() from _call_refresh_scene_fade_35
    return

label monica_shawarma_dialogue2:
    #Моника пришла разносить флаеры
    #render
    $ store_music()
    music DarxieLand
    img 6139
    shawarma "Мадаме! Я знаю! Вы пришли за вкусный кебаб!"
    menu:
        "Купить кебаб за $ 1":
            if money < 1:
                mt "У меня нет этого гребаного доллара!"
                return
            img 6140
            m "Давай сюда свой жуткий кебаб..."
            $ add_money(-1)
            img 6141
            shawarma "Пожалуйста, Мадаме!"
            music stop
            "Самый вкусный кебаб в округе!"
            img 6142
            w
            sound snd_gulp
            call monicaEat() from _call_monicaEat_3
            img 6143
            with fade
            w
            #звук еды
            img 6144
            mt "Отвратительная еда... Но, по крайней мере, я больше не хочу есть... Пока..."
            pass
        "Разносить флаеры.":
            img 6145
            m "Угостишь меня свои кебабом?"
            img 6146
            shawarma "Конечно, Мадаме!"
            "Я бесплатно угощу Вас кебаб, когда Вы разнести все флаер!"
            img 6147
            m "Еще бы! Я и не надеялась на твою порядочность и щедрость..."
            music stop
            "Давай сюда свои флаеры!"
            #звук одежды
            sound snd_cardboard1
            img 6148
            with fade
            mt "Черт! Сколько же мне еще придется позориться?"
            call kebab_work_start() from _call_kebab_work_start_1
            call refresh_scene_fade() from _call_refresh_scene_fade_36
            $ restore_music()
            return
        "Я не собираюсь ничего разносить! Давай кебаб сюда!":
            music Power_Bots_Loop
            img 6135
            m "Я не собираюсь ничего разносить! Давай кебаб сюда!"
            img 6136
            shawarma "Нет, Мадаме! Нет флаер, нет кебаб!"
            w
            img 6138
            with fade
            w
            $ autorun_to_object("monica_shawarma_dialogue0a")

        "Уйти.":
            pass

    $ restore_music()
    return

label monica_shawarma_dialogue2a:
    #Моника пришла покупать кебаб
    #render

    $ store_music()
    music DarxieLand
    #день
    if day_time == "day":
        menu:
            "Купить кебаб за $ 1":
                if money < 1:
                    mt "У меня нет этого гребаного доллара!"
                    return
                img 6140
                m "Давай сюда свой жуткий кебаб..."
                $ add_money(-1)
                img 6141
                shawarma "Пожалуйста, Мадаме!"
                music stop
                "Самый вкусный кебаб в округе!"
                img 6142
                w
                sound snd_gulp
                call monicaEat() from _call_monicaEat_4
                img 6143
                with fade
                w
                #звук еды
                img 6144
                mt "Отвратительная еда... Но, по крайней мере, я больше не хочу есть... Пока..."
            "Уйти.":
                pass

    else:
        #вечер
        img 6149
        shawarma "Мадаме! Я знаю! Вы пришли за вкусный кебаб!"
        if money < 1:
            mt "Черт! У меня нет денег!"
            "И я не собираюсь разносить флаеры по ночным улицам!"
            return
        menu:
            "Купить кебаб за $ 1":
                img 6150
                m "Давай сюда свой жуткий кебаб..."
                $ add_money(-1)
                img 6151
                shawarma "Пожалуйста, Мадаме!"
                music stop
                "Самый вкусный кебаб в округе!"
                sound snd_gulp
                call monicaEat() from _call_monicaEat_5
                img 6152
                with fade
                w
                #звук еды
                img 6153
                mt "Отвратительная еда... Но, по крайней мере, я больше не хочу есть... Пока..."
            "Уйти.":
                pass
    $ restore_music()
    return


label monica_shawarma_dialogue3a:
    #Моника раздала все флаеры
    # комментарий на улице
    mt "Я раздала все флаеры, где мой кебаб?"
    return

label monica_shawarma_dialogue3_food:
    #Моника раздала все флаеры
    #render
    $ store_music()
    music DarxieLand
    img 6154
    m "Я раздала все флаеры, где мой кебаб?"
    img 6155
    w
    img 6141
    music stop
    shawarma "Пожалуйста, Мадаме! Приятного аппетита!"
    #звук бросаемого полотна
    sound snd_cardboard2
    img 6156
    w
    img 6142
    w
    sound snd_gulp
    img 6143
    with fade
    w
    #звук еды
    img 6144
    mt "Отвратительная еда... Но, по крайней мере, я больше не хочу есть... Пока..."
    $ restore_music()
    return

label monica_shawarma_dialogue3_end_half_food:
    #Моника раздала не все флаеры
    $ store_music()
    music DarxieLand
    img 6157
    with fade
    m "У меня не получилось раздать все флаеры..."
    img 6158
    w
    img 6159
    shawarma "Ничего страшного, Мадаме!"
    img 6160
    "У меня есть половина кебаб! Не вся работа, не весь кебаб!"
    m "Его что, кто-то ел?!?!"
    shawarma "Нет, мадаме! Это половина кебаб. Он такой родился на свет!"
    music stop
    mt "Что-то я сомневаюсь... Но у меня нет выбора..."
    #звук бросаемого полотна
    sound snd_cardboard2
    img 6156
    m "Давай сюда свой кебаб..."
    img 6142
    w
    sound snd_gulp
    img 6143
    w
    #звук еды
    img 6144
    mt "Отвратительная еда... Но, по крайней мере, я больше не хочу есть... Пока..."
    $ restore_music()
    return

label monica_shawarma_dialogue3_end_no_food:
    #Моника не раздала флаеры
    $ store_music()
    music DarxieLand
    img 6161
    with fade
    m "Я раздала все флаеры, где мой кебаб?"
    shawarma "Мадаме! Вы не раздали флаер!"
    "Кебаб ждать Вас когда флаер будет роздан!"
    music stop
    img 6162
    mt "Сволочь!!!"
    #звук бросаемого полотна
    sound snd_cardboard2
    img 6156
    w
    $ restore_music()
    return

label monica_shawarma_dialogue4:
    #Моника уже кушала сегодня
    mt "Спасибо, я на сегодня сыта!"
    "У меня нет желания подходить к этому негодяю!"
    return

label monica_shawarma_dialogue5:
    #Моника хочет уйти в сторону магазина во время раздачи кебабов
    mt "Я не собираюсь ходить по приличным улицам в таком виде!"
    "Мне лучше ходить по этому району, где я в таком виде не слишком выделяюсь на фоне окружающих."
    return False

label monica_shawarma_dialogue6:
    #Моника заходит первый раз в hostel_street с полотном
    mt "Возможно здесь я найду кого-то кому можно раздать эти дурацкие флаеры..."
    "Главное не подходить к тому хостелу..."
    $ remove_hook()
    return
label monica_shawarma_dialogue7:
    #Моника заходит первый раз в hostel_street2 с полотном
    mt "Какой грязный вонючий район..."
    "Такие же и обитатели здесь..."
    "Но мне главное раздать эти флаеры и убраться отсюда!"
    "Такая девушка как Я не подходит подобному месту!"
    $ remove_hook()
    return

label monica_shawarma_dialogue8:
    #Моника заходит первый раз в hostel_edge_1c с полотном
    mt "Грязная подворотня."
    "Там дальше есть улица, может быть попробовать поискать там кого-то, чтобы раздать эти дурацки флаеры?"
    $ remove_hook()
    return
label monica_shawarma_dialogue9:
    #Моника заходит первый раз в hostel_street3 с полотном
    mt "Этот место не совсем уж грязное, но жители здесь не лучше..."
    $ remove_hook()
    return

label monica_shawarma_dialogue10:
    #Моника высказывается по поводу ситизенов
    mt "В этом районе одни наркоманы и извращенцы!"
    "Здесь нет ни одного нормального человека, которому можно просто так дать этот чертов флаер!!!"
    return

label monica_shawarma_dialogue11:
    #Клик на Монику во время разноски флаеров
    mt "О БОЖЕ!"
    mt "Какой ужас"
    "Моника! Как ты докатилась до того, чтобы ходить В ЭТОМ!!!"
    "И разносить флаеры за еду!!!"
    mt "О БОЖЕ!"
    return False
