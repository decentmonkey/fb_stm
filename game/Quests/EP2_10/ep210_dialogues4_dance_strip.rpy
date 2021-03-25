default monicaClareStoryAboutLife = False   # Моника рассказывает Клэр правду о себе
default monicaMollyFoto = False   # Моника разрисовала портрет Молли

# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_1:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    # Моника недовольно
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16130
    with fadelong
    mt "Черт! Совсем забыла, что сегодня здесь звезда трущоб..."
    mt "Не хочу разговаривать с этой дрянью!"
    # Моника проходит в гримерку и подходит к вешалке рядом со столиком Клэр
    sound highheels_short_walk
    img 16132
    with fade
    m "..."
    img 22815
    with diss
    w
    # рыжая ей, не поворачиваясь,
    img 22667
    with diss
    w
    img 16131
    with diss
    molly "Эшли говорит, что твоими выступлениями довольны посетители..."
    molly "И хотят видеть тебя чаще на сцене..."
    # Моника поворачивается и зло смотрит на нее
    img 16133
    with fade
    m "И что?"
    img 16134
    with diss
    mt "На что эта дрянь намекает?"
    mt "Ее бесит, что она, может быть, уже и не звезда?"
    # рыжая смотрит на Монику зло
    music Pyro_Flow
    img 16135
    with fade
    molly "Я тебя предупреждаю, шлюха!"
    molly "Если из-за тебя я потеряю хотя бы один цент от своего заработка..."
    molly "Я сделаю все, что бы тебя выкинули отсюда..."
    img 16136
    with diss
    molly "Или отправлю тебя за решетку, мошенница..."
    molly "Там тебе и место!"
    molly "!!!"
    music Groove2_85
    img 16137
    with diss
    menu:
        "Клэр предупреждала, что лучше не конфликтовать с ней":
            # отворачивается от Молли, послав ей убийственный взгляд
            music Power_Bots_Loop
            img 22823
            with fade
            m "!!!"
        "Да, Клэр предупреждала. Но я не могу просто проигнорировать такую наглость!":
            # Моника ей высокомерно в ответ
            music Pyro_Flow
            img 16138
            with fade
            m "Что я слышу?.."
            m "Мне угрожает сама звезда паба Shiny Hole?!"
            img 16139
            with diss
            m "Ты серьезно?!"
            m "Думаешь, что ТЫ можешь испугать меня чем-то?!"
            m "!!!"
            img 16134
            with fade
            mt "Никчемная бесполезная дрянь!"
        "Взять стул и ударить эту сучку!":
            # Моника смотрит на стул, потом зло на Молли
            # арт стула крупным планом можно взять готовый
            music Power_Bots_Loop
            img 22822
            with fade
            mt "Черт!!!"
            mt "Не хватало еще мне проблем с полицией из-за этой сучки!"
            img 22823
            with diss
            m "..."
            mt "Но когда-нибудь я не сдержусь и сделаю это!"
            m "!!!"
    # рыжая зло смотрит на Монику
    music Groove2_85
    img 16140
    with fade
    sound highheels_short_walk
    molly "!!!"
    # Моника отворачивается от нее
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
    m "..."
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
    return

# далее в этот день все, как обычно. Моника выступает на сцене, потом переодевается, платит проценты Эшли и уходит

# на другой день
# Паб. Гримерка танцовщиц. На работе Клэр.
label ep210_dialogues4_dance_strip_2:
    # Клэр сидит за своим столиком, Моника стоит в дверях
    # Моника задумчиво смотрит на Клэр
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22709
    with fadelong
    w
    img 22711
    with fade
    mt "Надо будет узнать у нее, как она догадалась использовать хлыст..."
    mt "Хлыст от извращенцев."
    mt "Эффективная штука. Мне такая просто необходима."
    # Клэр в маске поворачивается к Монике, с улыбкой
    sound highheels_short_walk
    img 16141
    with diss
    clare "Привет, [monica_pub_name]!"
    clare "Джо больше не приставал?"
    img 16142
    with diss
    m "Нет,не приставал. Твой инструмент для отпугивания был..."
    m "Весомым арументом больше не лезть ко мне."
    # проходит в гримерку к вешалке
    sound highheels_short_walk
    img 22714
    with fade
    clare "Да, я никогда с ним не расстаюсь."
    clare "Клиенты не обижают?"
    img 22715
    with diss
    m "Пока все нормально. Сцена меня уже не так пугает как поначалу..."
    img 22716
    with diss
    clare "Ты скоро научишься получать от этого удовольствие."
    img 16143
    with fade
    mt "Хм, сомневаюсь в этом..."
    img 22723
    with diss
    clare "[monica_pub_name], ты чем-то еще занимаешься, помимо танцев на сцене?"
    # Моника смотрит на нее, в сомнениях
    img 16144
    with diss
    m "..."
    menu:
        "Рассказать ей правду.":
            img 22729
            with fade
            mt "Она была добра ко мне..."
            mt "И даже помогла мне..."
            img 16145
            with diss
            mt "Прогнав неудачника Джо, когда он прицепился ко мне у сцены..."
            mt "Думаю, я могу сказать ей правду..."
            mt "..."
            img 16146
            with fade
            m "Я... Для меня..."
            m "Для меня трущобы - это отдельный мир... Который существует где-то далеко..."
            m "И ни при каких обстоятельствах не может появиться в моей жизни."
            img 16147
            with diss
            clare "???" # смотрит на нее удивленно
            img 22724
            with fade
            m "В данный момент у меня денежные трудности..."
            m "Поэтому я нахожусь здесь."
            m "Но это временно!"
            music Mandeville
            img 16148
            with diss
            m "Я сильная и независимая женщина."
            m "У меня есть успешный бизнес и очень высокое положение в обществе."
            img 16149
            with fade
            m "Потратить несколько тысяч долларов на платье с последней коллекции..."
            m "Что бы надеть его всего один раз на какое-нибудь мероприятие..."
            m "Это для меня в порядке вещей."
            music Groove2_85
            img 16150
            with diss
            clare "А почему ты тогда здесь?" # смотрит на нее удивленно
            img 16151
            with fade
            m "..."
            m "Мне нужно еще немного времени и я решу свои... Небольшие проблемы..."
            music Mandeville
            img 16152
            with diss
            m "И снова буду управлять своим бизнесом и сотнями подчиненных."
            m "Сидя в своем кабинете на своем кресле босса."
            clare "!!!"
            img 16153
            with diss
            m "Просто мне сейчас нужно немного подзаработать денег..."
            m "Танцуя здесь..."
            m "..."
            music Groove2_85
            img 16154
            with fade
            clare "Ого! Ничего себе!"
            clare "Слушай, ну если вдруг тебе понадобится помощь..."
            clare "Ты всегда можешь обратиться ко мне."
            m "..."
            img 16155
            with diss
            clare "А [monica_pub_name]..."
            clare "Это твое настоящее имя?"
            music Mandeville
            img 16156
            with fade
            m "Нет. Это выдуманное имя. Специально для этой дыры."
            m "На самом деле я Миссис Бакфетт."
            m "Моника Бакфетт."
            img 16157
            with diss
            clare "Мне можно обращаться к тебе просто Моника?"
            img 16158
            with fade
            m "Да, но только когда мы вдвоем."
            m "Я не хочу, чтобы здесь узнали мое настоящее имя."
            music Groove2_85
            img 16159
            with diss
            clare "Моника, можешь рассказать мне, из-за чего у тебя эти..."
            clare "Временные денежные трудности."
            clare "Или из-за кого?"
            m "..."
            img 16160
            with fade
            mt "Я и так рассказала ей слишком многое о себе..."
            music Hidden_Agenda
            img 16161
            with diss
            m "Просто произошло небольшое недоразумение..."
            m "Которое я скоро устраню."
            music Groove2_85
            img 16162
            with fade
            clare "Небольшое недоразумение - это мужчина?"
            img 16163
            with diss
            mt "Точнее и не скажешь."
            mt "А она догадливая..."
            music Hidden_Agenda
            img 16164
            with fade
            m "Да. Мужчина."
            music Groove2_85
            img 16165
            with diss
            clare "Я так и подумала!"
            clare "Наверное, к другой ушел?!"
            img 16166
            with diss
            m "..."
            clare "Вот сволочь!"
            clare "!!!"
            img 16167
            with fade
            m "Только... Не рассказывай никому..."
            clare "Не переживай. Я на твоей стороне."
            img 16168
            with diss
            m "Спасибо..."
            m "А ты, Клэр?"
            img 16169
            with diss
            m "Какое у тебя настоящее имя?"
            m "Ты где-нибудь еще работаешь?"
            $ monicaClareStoryAboutLife = True # Моника рассказала Клэр правду о себе
            pass
        "Соврать ей.":
            img 16170
            with fade
            mt "Клэр, конечно, ничего плохого мне не сделала..."
            mt "И даже помогла мне..."
            mt "Прогнав неудачника Джо..."
            mt "Когда он прицепился ко мне у сцены, но..."
            img 16171
            with diss
            mt "Я не могу признаться, что работаю гувернанткой... Притом в своем бывшем доме..."
            mt "..."
            mt "Да и все остальное..."
            mt "Не хочу, чтобы здесь кто-то знал обо мне правду."
            music Mandeville
            img 16149
            with fade
            m "..."
            m "Я? Конечно!"
            m "Вообще, у меня есть успешный бизнес и очень высокое положение в обществе."
            m "И, в принципе, я ни в чем не знаю нужды..."
            img 16150
            with diss
            clare "А почему ты тогда здесь?" # смотрит на нее удивленно
            img 16172
            with fade
            m "Мои подруги соответствуют моему уровню."
            m "Такие люди как я, как правило, перепробовали все виды удовольствия в жизни..."
            m "Познали все виды роскоши и..."
            img 16148
            with diss
            m "Для того, чтобы получить немного адреналина, мы с подругами решили поспорить..."
            m "Что я смогу месяц прожить без всех тех удобств и комфорта..."
            m "К которому привыкла."
            m "Чтобы выиграть спор, я должна была устроиться на работу где-нибудь в трущобах..."
            img 16152
            with diss
            m "И жить только на заработанные деньги."
            m "Притворившись обычной девушкой, без денег."
            m "Естественно, это все временно."
            img 16173
            with diss
            m "Это такой своего рода эксперимент. И скоро он закончится."
            m "И я вернусь в свой роскошный дом с прислугой."
            m "И в свою комфортную беззаботную жизнь."
            music Groove2_85
            img 16157
            with fade
            clare "Ого!"
            clare "Ты меня удивила!"
            clare "Какой-то странный спор..."
            music Mandeville
            img 16153
            with diss
            m "Да. Но нам с подругами захотелось поэкспериментировать..."
            m "Посмотреть, так сказать, на другую жизнь."
            m "Только... Не рассказывай никому..."
            music Groove2_85
            img 16154
            with fade
            clare "Не переживай. Я на твоей стороне."
            clare "А [monica_pub_name]..."
            clare "Это твое настоящее имя?"
            music Mandeville
            img 16156
            with diss
            m "Нет. Это выдуманное имя. Специально для этой дыры."
            m "На самом деле я Миссис Бакфетт."
            m "Моника Бакфетт."
            music Groove2_85
            img 16162
            with fade
            clare "Мне можно обращаться к тебе просто Моника?"
            img 16144
            with diss
            m "Да, но только когда мы вдвоем."
            m "Я не хочу, чтобы здесь узнали мое настоящее имя."
            m "..."
            img 16169
            with fade
            m "А ты, Клэр?"
            m "Какое у тебя настоящее имя?"
            m "Ты где-нибудь еще работаешь?"
            pass
    # Клэр, загадочно улыбаясь
    music Groove2_85
    img 16174
    with diss
    clare "Я? Да так..."
    clare "Ничего серьезного. Так... Случайные подработки..."
    clare "Не сравнится с тем, что рассказала мне ты, Моника."
    img 16175
    with fade
    clare "И мое имя - не псевдоним. Меня и правда зовут Клэр."
    clare "..."
    clare "Мы с тобой заболтались. Тебе пора одеваться и идти на сцену."
    img 16176
    with diss
    mt "Черт! Снова эта сцена! И толпа пьяных неудачников!"
    m "..."
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
    return

# далее в этот день все, как обычно.

# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_3:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    # Моника недовольно
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22813
    with fadelong
    mt "Не хочу разговаривать с этой дрянью!"
    # Моника проходит в гримерку и подходит к вешалке рядом со столиком Клэр
    sound highheels_short_walk
    img 22814
    with fade
    m "..."
    # рыжая смотрит на нее зло, но ничего не говорит
    img 22815
    with diss
    molly "!!!"
    # потом отворачивается к зеркалу
    # Моника переодевается
    img 16131
    with fade
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
    m "..."
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
    return


# после выступления Моники на сцене, она заходит в гримерку
# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_4:
    # Моника заходит в гримерку
    # сразу после того, как Моника переоделась в свой наряд шлюхи, в гримерку забегает Молли
    # Молли начинает орать на Монику
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Pyro_Flow
    img 16177
    with fadelong
    molly "Воровка!"
    molly "Я знала, что ты не чиста на руку, сучка!"
    img 16178
    with hpunch
    molly "Решила прикарманить мои деньги!!!"
    molly "Дрянь! Мошенница!!!"
    # Моника в шоке
    music Power_Bots_Loop
    img 16179
    with fade
    m "Что происходит?!"
    m "!!!"
    m "Ты чего разоралась?! Какие деньги?!"
    music Pyro_Flow
    img 16180
    with diss
    molly "И не притворяйся, что ты тут ни при чем!!!"
    music Power_Bots_Loop
    img 16181
    with diss
    m "Ты что, дрянь, совсем головой поехала?!"
    m "Какого черта ты тут разоралась?!"
    m "!!!"
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    # на шум приходит Эшли
    img 16182
    with fadelong
    ashley "Что здесь происходит?!"
    ashley "Вас слышно даже у барной стойки!!!"
    img 16183
    with fade
    ashley "У меня клиенты просятся сюда и предлагают деньги..."
    ashley "Чтобы посмотреть на битву сучек!"
    # Молли орет, тыча пальцем в Монику
    music Pyro_Flow
    img 16184
    with diss
    molly "Эта дрянь украла у меня мои деньги!!!"
    molly "Они всегда были в этой банке на столике!"
    molly "Сейчас там пусто!!!" # банка крупным планом, пустая
    img 16185
    with diss
    molly "Кроме нее никого в гримерке сегодня не было!"
    molly "Это сделала она!"
    music Power_Bots_Loop
    img 16186
    with hpunch
    m "Что?!"
    m "!!!"
    music Pyro_Flow
    img 16187
    with fade
    molly "Я просто так этого не оставлю!"
    molly "Я требую вернуть мои деньги! А эту шлюху наказать!!!"
    # Эшли строго смотрит на Монику
    music Groove2_85
    img 16188
    with diss
    ashley "Это правда?!"
    # Моника возмущенно
    img 16189
    with fade
    m "Конечно, нет!"
    m "Это какой-то бред!!!"
    m "Эта стерва специально все подстроила!!!"
    music Power_Bots_Loop
    img 16190
    with diss
    mt "Вот сучка!!!"
    mt "Ненавижу!"
    mt "!!!"
    # Молли продолжает орать
    music Pyro_Flow
    img 16191
    with fade
    molly "Эшли, ты сама мне рассказывала..."
    molly "Что эта дрянь воровала твои чаевые!!!"
    molly "Значит это она украла мои деньги!!!"
    img 16192
    with diss
    molly "Я сейчас проверю ее карманы!"
    molly "Наверняка, она спрятала их там!"
    # подходит к Монике
    # Моника ее останавливает
    sound Jump1
    img 16193
    with diss
    w
    music Power_Bots_Loop
    img 16194
    with diss
    m "Какого черта ты тут устроила?!"
    m "Не прикасайся ко мне!!!"
    # Молли смотрит на нее насмешливо и говорит, обращаясь к Эшли
    music Groove2_85
    img 16195
    with fade
    molly "Вот видишь, Эшли?!"
    molly "Эта дрянь боится, что я найду там деньги!"
    molly "Которые она у меня украла!!!"
    music Power_Bots_Loop
    img 16196
    with diss
    m "!!!" # зло
    music Groove2_85
    img 16197
    with diss
    ashley "Сколько там было денег?"
    molly "1000 баксов!"
    # Эшли строго смотрит на Монику, подходит к ней
    sound highheels_short_walk
    img 16198
    with fade
    ashley "[monica_pub_name], показывай, что у тебя в карманах!"
    ashley "Иначе я сама проверю их!"
    img 16199
    with diss
    m "У меня нет ничего в карманах!"
    # Эшли засовывает руку во внутренний карман ее куртки, попутно лапая ее за грудь, Моника зло на нее смотрит
    music Loved_Up
    img 16200
    with fade
    w
    sound vjuh3
    img 16201
    with diss
    w
    sound vjuh3
    img 16202
    with diss
    w
    img 16203
    with diss
    mt "!!!"
    mt "Извращенка!"
    # Эшли вытаскивает из кармана купюры
    # Моника растерянно смотрит на них
    music Groove2_85
    img 16204
    with hpunch
    sound Jump2
    molly "Вот!!! Я же говорила!!! Она воровка!!!"
    img 16205
    with diss
    m "Но... Я... Я не брала этих денег!"
    music Power_Bots_Loop
    img 16207
    with fade
    mt "!!!"
    # смотрит зло на Молли
    mt "Вот сучка!!!"
    img 16206
    with diss
    m "Эшли! Она специально это подстроила!"
    m "Она хочет, чтобы ты выгнала меня отсюда!"
    m "Потому что я популярнее, чем она!!!"
    music Pyro_Flow
    img 16208
    with fade
    molly "Это не так!"
    molly "Она воровка!!!"
    molly "Эшли, вызывай полицию!"
    mt "!!!"
    img 16209
    with diss
    ashley "Молли заткнись! Я сама разберусь!" # обращаясь к Молли
    ashley "Никакой полиции!"
    ashley "Я сама накажу [monica_pub_name], чтобы думала в следующий раз!"
    # Моника рассержена
    img 16210
    with fade
    m "!!!"
    m "За что меня наказывать?!"
    m "Я ни в чем не виновата!!!"
    music Power_Bots_Loop
    img 16211
    with diss
    ashley "Так, [monica_pub_name], хватит!!!"
    m "!!!"
    ashley "Как мы будем решать эту проблему?"
    ashley "Это не первый раз, когда ты присваиваешь чужие деньги!"

    if pubMonicaWaitressTipsPunishmentAshleyStage >= 1:
        # если извинялась в подсобке перед Эшли
        music Hidden_Agenda
        img 16212
        with fade
        ashley "А потом просишь простить тебя, извиняешься..."
        ashley "Пользуешься моей добротой..." # хитро смотрит на Монику
        music Pyro_Flow
        img 16213
        with diss
        ashley "И после этого снова крадешь деньги!" # снова строго
        ashley "Я просто так тебе этого не могу простить..."
        m "..."
    img 16214
    with diss
    ashley "Я тебя оштрафую! Ты теперь должна отдавать мне все свои чаевые!"
    ashley "Пока Молли не простит тебя!"
    ashley "Она самая популярная девочка в этом пабе..."
    ashley "Ее слова для меня значат больше, чем твои, [monica_pub_name]..."
#    music Power_Bots_Loop
    img 16215
    with diss
    m "ЧТО?!" # возмущенно
    # Эшли уходит, Моника злобно смотрит на Молли
    sound highheels_short_walk
    img 16216
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    img 16217
    with fade
    m "Сучка!"
    molly "..." # насмешливый высокомерный взгляд
    img 16218
    with diss
    mt "Ненавижу!!!"
    mt "!!!"
    # та на нее смотрит свысока и уходит из гримерки
    music Pyro_Flow
    img 16219
    with fade
    sound highheels_short_walk
    molly "..."
#    $ log1 = t_("Из-за это рыжей сучки я теперь должна отдавать все свои чаевые Эшли! Ненавижу ее!!!") # квест лог
    return

# Паб. Гримерка танцовщиц.
label ep210_dialogues4_dance_strip_5_0:
    img 22718
    with fadelong
    mt "Никчемная!"
    mt "Бесполезная!"
    mt "Сучка!!!"
    mt "!!!"
    mt "..."
    mt "Может быть сделать какую-то пакость ей?"
    return

label ep210_dialogues4_dance_strip_5_1:
    mt "Лучше не делать этого при свидетелях..."
    return
label ep210_dialogues4_dance_strip_5_2:
    if ep210_picture_marked == True:
        img 16226
        with fade
        mt "Шедеврально!"
        mt "!!!"
    else:
        img 22718
        with fadelong
        mt "Никчемная!"
        mt "Бесполезная!"
        mt "Сучка!!!"
        mt "!!!"
    return False

label ep210_dialogues4_dance_strip_5:
    # Моника в ярости, смотрит на фото Молли на стене
    music Pyro_Flow
    img 22670
    with fadelong
    w
    img 22671
    with fade
    mt "Никчемная!"
    mt "Бесполезная!"
    mt "Сучка!!!"
    mt "!!!"
    # переводит взгляд на помаду на столике
    music Hidden_Agenda
    img 16220
    with diss
    mt "Хммм..." # задумывает мелкую пакость
    mt "..."
    img 16221
    with diss
    menu:
        "Взять помаду и испортить фото рыжей сучки.":
            $ monicaMollyFoto = True # Моника разрисовала портрет Молли
            pass
        "Не делать этого.":
            img 16222
            with fade
            mt "Идея хорошая, но..."
            music Groove2_85
            mt "Эта дрянь сразу поймет, что это сделала я..."
            mt "И снова мне подкинет деньги."
            img 16223
            with diss
            mt "Или сделает какую-нибудь другую гадость."
            mt "..."
            mt "У меня и без нее проблем хватает."
            return False
    # берет помаду, подходит к потрету и рисует на нем член? кровь? рога и хвост? просто замазывает помадой?
    # потом ухмыляется довольно
    sound highheels_short_walk
    img 16224
    with fade
    w
    img 16225
    with diss
    sound Jump1
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    sound vjuh4
    pause 1.0
    sound vjuh4
    pause 1.0
    music Hidden_Agenda
    img 16227
    with fadelong
    w
    img 16226
    with fade
    mt "Шедеврально!"
    mt "!!!"
    return True

# Паб. Гримерка танцовщиц. На работе Клэр.
label ep210_dialogues4_dance_strip_6:
    # Клэр сидит за своим столиком, Моника стоит в дверях
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16228
    with fadelong
    w
    img 16229
    with fade
    mt "Интересно, Клэр в курсе того, что произошло?"
    # Клэр поворачивается к ней
    img 16230
    with diss
    clare "Моника, привет! Как ты?"
    clare "Наша звезда все-таки разозлилась на тебя?"
    # Моника удивленно
    img 16231
    with fade
    mt "!!!"
    m "Ты в курсе?"
    img 16232
    with diss
    clare "Да. Не переживай."
    clare "Я уверена, что это она специально все подстроила..."
    img 16233
    with diss
    m "Я в этом не сомневаюсь!"

    if ep210_picture_was_marked == True and ep210_picture_marked_claire_comment == False:
        $ ep210_picture_marked_claire_comment = True
        # если Моника разрисовала портрет Молли
        # Клэр улыбаясь говорит
        img 22723
        with fade
        #
        $ notif(t_("Моника разрисовала фотографию Молли"))
        #
        clare "Кстати, отличный портрет получился!"
        clare "Наша звезда прямо-таки засияла..."
        music Hidden_Agenda
        img 16151
        with diss
        m "Нет-нет... Я тут ни при чем... Я ничего не делала."
        # Клэр смотрит на нее и улыбается
        img 16154
        with diss
        clare "Все ок. Я никому не скажу."
    music Groove2_85
    img 22720
    with fade
    clare "По поводу твоего наказания... Это несправедливо."
    clare "У меня есть план..."
    img 16234
    with diss
    clare "Жди здесь."
    clare "Мне надо поговорить с Эшли..."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    # Клэр выходит из гримерки
    # Моника в растерянности
    img 22722
    with fade
    mt "Клэр пошла заступаться за меня?!"
    mt "???"
    mt "..."
    img 22728
    with diss
    mt "Наверное, попросит что-то взамен за это..."
    mt "..."
    mt "Надеюсь, не какое-нибудь извращение..."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    # возвращается Клэр вместе с Эшли
    # Эшли стоит руки в боки и строго смотрит на Монику
    img 16235
    with fade
    ashley "Ладно, [monica_pub_name]."
    ashley "Мне тут Клэр предложила помочь тебе отработать штраф..."
    ashley "В общем, ты можешь выйти на сцену вместе с Клэр..."
    img 16236
    with diss
    mt "???" # удивленно на Клэр, потом снова на Эшли
    img 16188
    with fade
    ashley "Будете танцевать вдвоем."
    ashley "Все чаевые от выступления отдашь мне..."
    ashley "И я забуду про тот случай с Молли..."
    img 16237
    with diss
    mt "!!!" # удивленно
    img 16238
    with fade
    ashley "Или, если хочешь, разберись с Молли..."
    ashley "Советую тебе перед ней извиниться."
    ashley "Только не устраивать тут больше битву сучек!"
    music Power_Bots_Loop
    img 16190
    with diss
    mt "Извиняться перед этой никчемной сучкой?!"
    mt "!!!"
    music Groove2_85
    img 16239
    with fade
    ashley "И чтобы ничего, связанного с воровством, больше не было!!!" # грозно
    ashley "Еще раз сделаешь подобную хрень..."
    ashley "Ты просто так не отделаешься!!!"
    ashley "Ясно тебе, [monica_pub_name]?!"
    # Эшли уходит
    return

# переход на движок
# мысли Моники
# Паб. Гримерка танцовщиц, Клэр сидит у своего зеркала.
label ep210_dialogues4_dance_strip_7:
    # не рендерить!!!
    mt "..."
    mt "И что мне делать?!"
    mt "???"
    menu:
#        "Попросить прощения у рыжей сучки. (в следующем обновлении)":
#            mt "Возможно, мне стоит попытаться найти с этой дрянью общий язык?"
#            mt "Чтобы быть уверенной в том, что она мне больше не будет пакостить..."
#            mt "Ведь если Эшли меня простит после танца с Клэр..."
#            mt "Эта рыжая сучка взбесится еще больше."
#            mt "Мне нужно подумать об этом..."
#            mt "..."
#            help "В следующем обновлении!"
#            return False
        "Танцевать с Клэр. (доступно при открытии всех движений на сцене)":
            mt "Я ни за что не буду просить прощения у этой рыжей сучки!"
            mt "Ненавижу ее!!!"
            mt "Танец с Клэр - отличный способ разрешить сложившуюся ситуацию."
            mt "И позлить эту рыжую дрянь!"
            mt "Интересно, что она сделает, когда узнает об этом?"
            mt "..."
            return True
        "Уйти.":
            return False
    return

# Паб. Гримерка танцовщиц, Клэр сидит у своего зеркала.
# клик на Клэр
# выбран пункт меню "Танцевать с Клэр"
label ep210_dialogues4_dance_strip_8:
    if len(list(set(stage_Monica_shoots_array))) >= monicaPosesOpenedToDanceClaire:
        # если опция доступна, т.е. все движения на сцене открыты
        # Моника растерянно
        music Groove2_85
        img 16240
        with fade
        m "Я... Я не ожидала, что ты..."
        m "Поможешь мне..."
        img 16241
        with diss
        clare "Да ладно! Ничего сложного для меня в этом нет."
        img 16242
        with fade
        m "Я что-то должна тебе за это?"
        # Клэр удивленно
        img 16243
        with diss
        clare "Нет, конечно! О чем ты?!"
        clare "Просто старайся больше не конфликтовать с нашей звездой..."
        img 16176
        with fade
        mt "Я ей ничего не должна?"
        mt "Хммм..."
        img 16244
        with diss
        mt "Может, здесь какой-то подвох?"
        mt "..."
        img 16245
        with fade
        m "Клэр, а как мы будем танцевать вдвоем?"
        m "Я так ни разу не танцевала..."
        img 16246
        with diss
        clare "Моника, все получится отлично, вот увидишь!"
        clare "Мужчин в зале это крайне порадует."
        music Molten_Alloy
        img 16247
        with fade
        clare "Переодевайся и выходи на сцену. Я присоединюсь к тебе во время твоего танца."
        clare "Покажем им, кто здесь звезды!"
        return True
    else:
        # если опция недоступна, движения открыты не полностью
        img 16248
        with fade
        m "Клэр, а как мы будем танцевать вдвоем?"
        m "Я так ни разу не танцевала..."
        img 16249
        with diss
        clare "Моника, все получится отлично, вот увидишь!"
        clare "Только сначала тебе нужно набраться больше опыта..."
        clare "Ты еще слишком скованна на сцене."
        img 16250
        with diss
        m "..."
        help "Окрыты не все движения. Требуется [monicaPosesOpenedToDanceClaire]."
        return False
    return False

# во время танца Моники и Клэр из зала кричит Эшли
label ep210_dialogues4_dance_strip_9:
    # во время выступления из зала
#    music Hidden_Agenda
#    img 16255
#    with fade
    ashley "Давайте, девочки!!!"
    ashley "Покажите этим денежным мешкам, у кого самые аппетитные попки!"
    ashley "Пусть раскошеливаются!!!"
    return

# если был танец вдвоем с Клэр
# Паб. Гримерка после танца с Клэр.
label ep210_dialogues4_dance_strip_10:
    # использовать арты из идентичной сцены в версии 0.9
    # Моника отдает Эшли заработанные за двойной танец чаевые
    # Эшли требовательно
    music Groove2_85
    img 22790
    with fadelong
    ashley "[monica_pub_name], сколько вы заработали чаевых?"
    img 22792
    with fade
    $ add_money(-monica_strip_tips_today)
    m "Сегодня мы заработали [monica_strip_tips_today]."
    img 22793
    with diss
    ashley "Скажи спасибо Клэр."
    ashley "Я прощаю тебя... И чтобы больше никакой ругани с Молли!"
    music Hidden_Agenda
    img 22794
    with fade
    ashley "Кстати, было отличное выступление!"
    ashley "Клиентам понравилось!" # с улыбочкой
    ashley "Думаю, нам нужно ввести это в программу."
    music Groove2_85
    img 16252
    with diss
    mt "В принципе, идея неплохая..."
    mt "Чаевых намного больше..."
    img 16253
    with fade
    mt "Жаль их сейчас было отдавать Эшли..."
    mt "Из-за какой-то рыжеволосой сучки!"
    mt "!!!"
    img 22869
    with diss
    ashley "На сегодня ты свободна, [monica_pub_name]."
    return

# если был танец вдвоем с Клэр
# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_11:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    # рыжая сидит возле зеркала, Моника стоит в дверях
    img 22813
    with fadelong
    mt "Какая же она сучка!"
    mt "Решила подставить меня с деньгами перед Эшли!"
    music Power_Bots_Loop
    img 16130
    with fade
    mt "Меня, Монику Бакфетт!"
    mt "Дрянь!"
    mt "!!!"
    # Моника проходит в гримерку и подходит к вешалке
    # рыжая ей, не поворачиваясь
    music Groove2_85
    img 22816
    with diss
    molly "Слышала, Эшли тебя простила..."
    molly "Клэр тебе помогла..."
    # Моника поворачивается и зло смотрит на нее
    img 22817
    with fade
    m "И что?"
    m "Тебе какое дело?"
    # Молли, также не поворачиваясь к Монике
    img 22819
    with diss
    molly "Смотрю, ты тут хорошо устроилась..."
    molly "Ну что ж..."
    molly "Посмотрим, надолго ли..." # злобно
    music Power_Bots_Loop
    img 16140
    with fade
    mt "!!!"
    mt "Она специально меня провоцирует на..."
    mt "На битву сучек, как Эшли это назвала..."
    mt "Эшли меня предупредила, что больше такого не должно быть..."
    music Groove2_85
    img 16134
    with diss
    mt "Я просто не буду разговаривать с этой дрянью."
    mt "..."
    mt "Как было бы хорошо, если бы ее тут просто не стало."
    mt "Может, все-таки стоит двинуть ей стулом по голове?"
    mt "..."
    # рыжая поворачивается к Монике и смотрит на нее зло
    music Pyro_Flow
    img 22820
    with fade
    molly "Ты здесь долго не продержишься, поняла?"
    molly "Я сделаю все для того, чтобы тебя вышвырнули отсюда!!!"
    img 16135
    with diss
    molly "Советую тебе искать другое место для заработка."
    molly "Например, в подворотне."

    if ep210_picture_was_marked == True:
        # если Моника разрисовала портрет Молли
        img 16251
        with fade
        #
        $ notif(t_("Моника разрисовала фотографию Молли"))
        #
        molly " И кстати!"
        molly "Еще раз увижу, что ты испортила мой портрет!"
        molly "Простым штрафом ты не отделаешься, сучка!!!"
        $ ep210_picture_marked_molly_comment = True

    # отворачивается от Моники к зеркалу
    # Моника смотрит злобно
    music Power_Bots_Loop
    img 22679
    with diss
    mt "Дрянь!"
    mt "!!!"
    mt "Ненавижу!!!"
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
    return

# Паб. Моника на сцене.
label ep210_dialogues4_dance_strip_12:
    music stageCurrentMusicLoop
    img 23182
    with fade
    w
    img 23181
    with hpunch
    sound vjuh3
    w
    sound2 fx_coins_b1
    $ money += 20
    $ monica_strip_tips_today += 20
    $ notif ("+ $20")
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound applauseSound
    call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash
    customers1 "ДА! ДААААА!!!"
    w
    img 23191
    with diss
    sound2 fx_coins_b1
    $ money += 15
    $ monica_strip_tips_today += 15
    $ notif ("+ $15")
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound applauseSound
    call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_1
    customers2 "СНИМИ ИХ! СНИМИ!!!"
    w
    sound2 fx_coins_b1
    $ money += 30
    $ monica_strip_tips_today += 30
    $ notif ("+ $30")
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound applauseSound
    call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_2
    customers3 "ПОКАЖИ НАМ СВОЮ КИСКУ! ВАУ!!!"
    w
    img 23191
    with diss
    sound2 fx_coins_b1
    $ money += 50
    $ monica_strip_tips_today += 50
    $ notif ("+ $50")
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound applauseSound
    call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_3
    customers4 "Я ХОЧУ ТРАХНУТЬ ЭТУ СТРИПТИЗЕРШУ! Я ПЕРВЫЙ!!!"
    w
    sound2 fx_coins_b1
    $ money += 40
    $ monica_strip_tips_today += 40
    $ notif ("+ $40")
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound applauseSound
    call pub_dance_stage_flash() from _rcall_pub_dance_stage_flash_4
    customers4 "НУ ЖЕ! СНИМИ ТРУСИКИ! СНИМИ ИХ ПОЛНОСТЬЮ!!!"
    w
    img 23185
    with diss
    sound vjuh3
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound2 applauseSound
    customers4 "ОНА СПЕЦИАЛЬНО ТАК СДЕЛАЛА! Я ЗНАЮ!"
    w
    img 23184
    with hpunch
    $ idx = rand(1,3)
    $ applauseSound = "snd_applause" + str(idx)
    sound applauseSound
    w
    $ questHelp("shinyhole_31", True)
    $ questHelp("shinyhole_32", skipIfExists=True)
    # во время танца или сразу после него, когда Моника еще не ушла со сцены, с нее падают трусики
    # чаевые бешенно растут
    # Моника наклоняется, поднимает трусики
    # испуганно прикрывается и убегает со сцены, сверкая голой попой
    return

# Паб. Моника в гримерке после выступления, когда упали трусики.
label ep210_dialogues4_dance_strip_13:
    music stop
    music2 stop
    img black_screen
    with diss
    pause 3.0

    # не рендерить!!!
    # Моника переоделась в свою одежду и думает
    music Power_Bots_Loop
    img 23186
    with fadelong
    mt "Какой кошмар!"
    mt "Мои трусики чуть не упали перед толпой пьяных неудачников!!!"
    mt "!!!"
    music Groove2_85
    img 23187
    with diss
    mt "Как это могло произойти?!"
    mt "Что случилось?"
    mt "???"
    mt "Я столько раз танцевала в этих трусиках..."
    mt "Всегда все было хорошо, а тут..."
    img 23188
    with diss
    mt "..." # выражение лица меняется, Монику посетила догадка
    mt "Хмммм..."
    mt "А возможно?.."
    # смотрит на трусики, они лежат где-нибудь на стуле
    music Pyro_Flow
    with fade
    mt "Возможно, что они расстегнулись на мне во время выступления не просто так..."
    mt "А из-за того что кто-то подстроил это до того, как я их надела!!!"
    mt "!!!"
    mt "И этим 'кто-то' мог быть только один человек!"
    mt "Сучка Молли!!!"
    mt "!!!"
    return

# Паб. Моника, после того, как отдала процент от чаевых Эшли (сразу после dialogue_5_dance_strip_22).
label ep210_dialogues4_dance_strip_14:
    music Hidden_Agenda
    img 22849
    with fade
#    ashley "И кстати!"
    ashley "Тебе не кажется, что надо выступать вообще без трусиков, а?" # улыбочка
    music Power_Bots_Loop
    img 22852
    with diss
    m "Нет!"
    m "Мне так не кажется!"
    m "!!!"
    music Hidden_Agenda
    img 22867
    with fade
    ashley "А что тут такого?"
    ashley "Ты видела, как публике это понравилось?"
    ashley "В следующий раз выйдешь на сцену без одежды..."
    ashley "Это привлечет в мой паб больше клиентов..."
    img 22847
    with diss
    ashley "Значит, ты заработаешь больше чаевых."
    ashley "Тебе то какая разница, ты же в маске будешь."
    music Loved_Up
    ashley "Как представлю тебя на сцене... Да еще и с голой попкой..."
    ashley "Ты будешь настоящей звездой, [monica_pub_name]!"
    music Power_Bots_Loop
    img 22858
    with fade
    m "Я не собираюсь выступать голая!!!"
    m "!!!"
    music Groove2_85
    img 16253
    with diss
    mt "Эта извращенка так и ждет, когда я выйду голая на сцену!"
    mt "Я не буду танцевать голой!"
    mt "Если меня кто-нибудь узнает, несмотря на мою маску..."
    img 16254
    with diss
    mt "Боюсь даже думать о последствиях!"
    mt "!!!"
    return

# Паб. Гримерка танцовщиц. На работе Клэр.
label ep210_dialogues4_dance_strip_15:
    # Клэр сидит за своим столиком, Моника стоит в дверях
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22709
    with fadelong
    mt "Наверняка, Клэр уже знает о том, что..."
    mt "Что я стояла почти голой на сцене."
    # Клэр поворачивается к ней
    img 22712
    with fade
    clare "Моника, привет! Как ты?"
    img 16146
    with diss
    m "Привет, Клэр."
    m "Если не считать, что на прошлом выступлении с меня упали трусики..."
    img 16161
    with fade
    m "И я стояла на сцене, чуть-ли ни сверкая голой попой..."
    m "То у меня все просто отлично!"
    img 22716
    with diss
    clare "Да, я уже слышала об этом."
    clare "Трусики просто так не могли расстегнуться. Их специально кто-то надрезал."
    img 16144
    with fade
    m "И я догадываюсь, кто именно..."
    img 16159
    with diss
    clare "..."
    clare "Моника, будь поаккуратнее с Молли..."
    img 16155
    with fade
    clare "Ты же видишь, что она готова пойти на все..."
    clare "Ради того, чтобы сохранить свое положение звезды Shiny Hole."
    img 16156
    with diss
    m "Меня эта дрянь не напугает."
    m "Я и не с такими легко справлялась."
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
    return


# Моника переодевается, добавлен пункт в меню
label ep210_dialogues4_dance_strip_16:
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            pass
        "Выйти на сцену голой":
            mt "Я же буду не совсем голая. На мне будет маска..."
            mt "Зато я смогу заработать много чаевых."
            mt "Меня все равно никто здесь не знает..."
            mt "..."
            pass
    return

label ep210_dialogues4_dance_strip_17:
    menu:
        "Предложить Клэр танцевать с Моникой.":
            m "Клэр, не хочешь составить мне компанию на сцене?"
            if day - ep29_quests_dancing_with_claire_last_day >= monicaClaireDanceDaysInterval:
                clare "Хорошо, Моника. Выходи на сцену."
                clare "Я присоединюсь к тебе во время твоего танца."
                clare "Покажем им, кто здесь звезды!"
                return True
            else:
                clare "Я сегодня уже натанцевалась. Давай в другой раз?"
                return False

        "Уйти.":
            return False
    return


label ep210_dialogue_5_dance_clare:
    img 23179
    with fadelong
    w
    img 23180
    with diss
    clare "Заждалась меня, Моника?"
    clare "Покажем им, кто здесь звезды!"
    return

label ep210_dialogue_5_dance_strip_5a:
    if len(pub_dance_claire_dialogues_up_list) == 0:
        $ pub_dance_claire_dialogues_up_list = random.sample(set([1,2,3,4,5,6,7,8,9,10,11,12,13,14]), 14)
    $ idx = pub_dance_claire_dialogues_up_list.pop()

    # правильные стрелки
    if idx == 1:
        customers1 "Эй, смотри, какие телки!"
    if idx == 2:
        customers2 "Одна - это Клэр, а как зовут другую? Я ее раньше не видел!"
    if idx == 3:
        customers3 "Смотри что они вытворяют! Вау!"
    if idx == 4:
        customers4 "Красотки! Спускайтесь к нам!"
    if idx == 5:
        customers5 "Раздевайтесь! Покажите нам свои задницы! Да!"
    if idx == 6:
        customers1 "Вот это девочки, вау! Посмотрите!"
    if idx == 7:
        customers2 "Раздевайтесь! Покажите нам свои задницы! Да!"
    if idx == 8:
        customers3 "Покрутитесь на моем члене так же!"
    if idx == 9:
        customers4 "Давай! Поцелуй ее!"
    if idx == 10:
        customers5 "Полижи ей киску на сцене!"
    if idx == 11:
        customers1 "Я сейчас кончу! Вот это шоу!"
    if idx == 12:
        customers2 "Нереально красиво!"
    if idx == 13:
        customers3 "Раздвиньте ножки! Покажите что у вас там!"
    if idx == 14:
        customers4 "Задницы! Задницы!!!"
    return

label ep210_dialogue_5_dance_strip_5aa1:
    if len(pub_dance_claire_dialogues_up_list2) == 0:
        $ pub_dance_claire_dialogues_up_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_claire_dialogues_up_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Эй! Хорош уже! Давайте, раздевайтесь!"
    if idx == 2:
        customers2 "Где стриптиз?!"
    if idx == 3:
        customers3 "Это что?! Где сиськи голые?!"
    return

############################################ в след. апдейте
# Джо или Эшли будут заставлять танцевать приват для сотрудника банка (т.к. у них кредит)
# Моника танцует голая, клиент может ее потрогать
# один из клиентов ей говорит, да ладно Мэрилин, снимай маску. я знаю, что это ты
# Моника снимает маску, а клиент говорит, фигасе, а я сомневался, что это ты. даже у Джо спросил, тот говорит, что это не ты
