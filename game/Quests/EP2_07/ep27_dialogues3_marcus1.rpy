
# Моника приходит в полицейский участок и остается там до утра в тюрьме
label ep27_dialogues_marcus1_1:
    # Моника заходит в локацию полиции
    mt "Мне страшно..."
    mt "У меня ноги подкашываются от ужаса... Мне страшно... Что делать?"
    mt "Стоит-ли мне идти туда..."
    return


label ep27_dialogues_marcus1_1a:
    # При нажатии на вход
    help "Вы уверены в том чтобы Моника вошла туда?"
    help "Этот набор событий необязателен для прохождения игры."
    menu:
        "Не рисковать.":
            return False
        "Все равно войти.":
            pass

    help "Пожалуйста, сохранитесь. Часть событий внутри полиции все еще в разработке."
    return True

label ep27_dialogues_marcus1_1b:
    # Если пытается зайти в участок вечером
    mt "Сейчас темно..."
    mt "Поздно вечером я точно не найду в себе смелость зайти туда."
    mt "{c}Лучше придти туда днем{/c}."
    return

label ep27_dialogues_marcus1_1c:
    mt "В таком виде я точно туда не пойду. {c}Мне надо переодеться{/c}."
    return

label ep27_dialogues_marcus1_1d:
    mt "Мне страшно..."
    mt "У меня ноги подкашываются от ужаса..."
    return

label ep27_dialogues_marcus1_2:
    # Диалог с полицейской на входе
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 14138
    with fadelong
    policewoman "Да, гражданка?"
    policewoman "Что вам надо?"
    img 14139
    with diss
    m "Я... Я..."
    img 14140
    with fade
    policewoman "Ну же? Что молчишь?!"
    policewoman "Говори! Или выметайся!"
    policewoman "Здесь полицейский участок!"
    img 14141
    with diss
    m "Я... Пришла..."
    m "Я пришла, чтобы... чтобы увидеть Мистера Маркуса..."
    img 14142
    with fade
    policewoman "Мистер Маркус занятой человек."
    policewoman "У Вас к нему какое-то дело?"
    img 14143
    with diss
    m "У меня... Я..."
    m "Да... У меня важное дело к нему..."
    img 14144
    with fade
    policewoman "Я позову детектива и он решит что с Вами делать!"
    img 14145
    with diss
    m "Да, Мэм... Конечно..."
    img 14146
    with fadelong
    mt "О БОЖЕ!"
    mt "Может быть мне убежать, пока не поздно?!"
    img 14147
    with diss
    menu:
        "Убежать!":
            return False
        "Остаться и дождаться детектива.":
            pass

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("5 минут спустя...")) from _call_textonblack_31
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    sound man_steps
    img 14148
    with fadelong
    detective "Добрый день, Мэм."
    detective "Вы хотели увидеть Мистера Маркуса?"
    img 14149
    with diss
    m "Да, Сэр..."
    m "Я бы... Я бы хотела увидеть его..."
    img 14150
    with fade
    detective "Пожалуйста, скажите, как Вас зовут?"
    img 14151
    with diss
    m "Меня зовут... Моника Бакфетт..."
    img 14152
    with fade
    detective "Хорошо, Мэм."
    detective "Подождите минуту."
    img 14153
    with diss
    m "Да, Сэр, конечно..."
    music stop
    sound man_steps
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_32
    img black_screen
    with Dissolve(1)
    ## Проходит время
    music Groove2_85
    img 14154
    with fadelong
    detective "Мэм, Мистер Маркус сейчас занят и он попросил Вас подождать, пока он освободится."
    img 14155
    with diss
    m "..."
    img 14156
    with fade
    detective "Вы ведь не против подождать, пока Мистер Маркус освободится?"
    img 14157
    with diss
    menu:
        "Согласиться подождать.":
            music Hidden_Agenda
            img 14158
            with fade
            m "Да, Сэр..."
            m "Я подожду его."
            img 14159
            with diss
            detective "Хорошо, Мэм."

        "Попытаться уйти.":
            music Hidden_Agenda
            img 14160
            with fade
            m "Я зайду попозже, когда Мистер Маркус будет свободен."
            img 14159
            with diss
            detective "Мэм, я попрошу Вас обождать."
            detective "Мистер Маркус настаивает, чтобы Вы подождали его."

    # Появляются полицейские
    music stop
    img black_screen
    with diss
    pause 1.5
    sound man_steps
    music Groove2_85
    img 14161
    with fadelong
    w
    img 14162
    with diss
    detective "Миссис Бакфетт."
    detective "Вас сейчас проводят в место, где Вам будет комфортно ожидать Мистера Маркуса."
    music Power_Bots_Loop
    img 14163
    with hpunch
    mt "О Боже!"
    mt "ЭТО ОНИ!"
    img 14164
    with diss
    policeman1 "Пройдемте с нами, Мэм..."
    img 14165
    with diss
    policeman2 "Рад тебя снова видеть, сучка..."
    img 14166
    with hpunch
    mt "!!!"

    return

label ep27_dialogues_marcus1_3:
    # Монику приводят в тюрьму
    music stop
    sound man_steps
    img black_screen
    with diss
    pause 1.0
    sound snd_jail_door
    pause 2.0
    music Gearhead
    img 14167
    with fadelong
    m "Это... Это место!"
    m "Но!"
    m "Мистер Маркус согласился встретиться со мной!"
    m "Зачем Вы привели меня сюда?!"
    img 14168
    with diss
    policeman1 "Мистер Маркус освободится только завтра с утра."
    policeman1 "До этого времени ты подождешь его здесь."
    img 14169
    with fade
    m "Зачем Я здесь?"
    img 14170
    with diss
    policeman1 "Боб!"
    policeman1 "Эта сучка вернулась!"
    img 14171
    with diss
    policeman1 "Представляешь? Сама!"
    img 14172
    with Dissolve(0.2)
    policeman2 "Ха-ха-ха!"
    img 14173
    with fade
    m "Нет! Я пришла к Мистеру Маркусу!"
    img 14174
    with diss
    overseer "О! Это она?"
    overseer "У меня от нее все время болела голова!"
    overseer "И вот вы снова привели ее!"
    img 14175
    with fade
    policeman1 "Не беспокойся, Боб!"
    policeman1 "Она у тебя ненадолго."
    policeman1 "После встречи с Мистером Маркусом она отправится на объект."
    sound snd_woman_scream1a
    img 14176
    with hpunch
    m "НЕЕЕЕТ!"
    return

label ep27_dialogues_marcus1_4:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Gearhead
    sound snd_woman_pain1
    img 14177
    with fadelong
    w
    img 14178
    with diss
    w
    # Заходят в камеру
#    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.0
    sound snd_jail_door
    pause 2.0
#    music Gearhead
    img 14179
    with fadelong
    policeman2 "Соскучилась по своей клетке, сучка?"
    policeman2 "Раздевайся, иначе порвем твое платье!"
    img 14180
    with hpunch
    m "!!!"
    img 14181
    with fade
    policeman1 "Снимай одежду, мы дадим тебе другую."
    img 14182
    with diss
    m "Хорошо..."

    music stop
    sound snd_fabric1
    img black_screen
    with diss
    pause 1.5
    # Моника снимает одежду
    music Gearhead
    img 14183
    with fadelong
    with hpunch
    m "Что?"
    m "А где низ?"
    m "Дайте мне что-нибудь прикрыть низ?"
    img 14184
    with diss
    policeman2 "Скажи спасибо за то что есть."
    img 14185
    with diss
    policeman1 "Оставайся и веди себя хорошо."
    music stop
    img black_screen
    with diss
    sound snd_jail_door
    pause 1.5
    music Gearhead
    # уходят
    img 14186
    with fadelong
    policeman2 "Одно нарушение порядка и мы сообщим об этом Мистеру Маркусу."
    sound man_steps
    music stop
    img black_screen
    with diss
    pause 1.5

    return

label ep27_dialogues_marcus1_5:
    # Моника оказывается в клетке
    music stop
    img black_screen
    with diss
    pause 1.5
    music I_Feel_You
    img 14187
    with fadelong
    with hpunch
    mt "О БОЖЕ!"
    with hpunch
    mt "О БОЖЕ!!!"
    mt "Я снова здесь!"
    img 14188
    with diss
    mt "..."
    mt "И я пришла сюда сама!"
    img 14189
    with diss
    mt "Что же мне делать?!"
    img 14190
    with fade
    mt "ОНИ СКАЗАЛИ ЧТО ОТСЮДА Я НАПРАВЛЮСЬ НА ОБЪЕКТ!!!"
    mt "Я УВЕРЕНА ЧТО ОНИ ГОВОРИЛИ ПРО ЭТУ ФЕРМУ!!!"
    mt "О БОЖЕ!!!"
    mt "Как мне спастись?!"
    img 14191
    with hpunch
    mt "Зачем я пришла сюда?!"
    img 14192
    with diss
    mt "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Master_Disorder
    img 14193
    with fadelong
    mt "Так, Моника, стоп!"
    mt "Не паникуй!"
    mt "Мне посоветовала это сделать Мелани."
    img 14194
    with diss
    mt "А Мелани, как мне кажется, знает что делает."
    mt "В конце концов, ей удалось выбраться оттуда."
    img 14195
    with fade
    mt "С другой стороны, она могла сделать это специально, чтобы я попала в руки к Маркусу..."
    mt "Или она хотела наоборот помочь мне..."
    mt "На чьей же стороне Мелани?"
    img 14196
    with diss
    mt "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Euro_Loop1
    img 14197
    with fadelong
    mt "Но, к черту!"
    mt "Эти мерзавцы специально пытаются вывести меня из равновесия."
    mt "Они пугают меня, думая что я сдамся!"
    mt "Но я не сдамся!"
    img 14198
    with diss
    mt "Я - Моника Бакфетт!"
    mt "И я пройду через все! Я одержу победу!"
    mt "Завтра я встречусь с Маркусом."
    mt "Я ничего не нарушала, ни одного закона или правила!"
    img 14199
    with diss
    mt "..."
    mt "По крайней мере, Маркус не знает про некоторые исключения..."
    img 14200
    with fade
    mt "Я поговорю с ним и выйду отсюда!"
    mt "Я пришла сюда сама! И я смогу отсюда выйти!"
    music stop
    img black_screen
    with diss
    pause 2.0
    return

label ep27_dialogues_marcus1_6:
    # Моника смотрит на унитаз
#    img 14201
    mt "Эта жуткая штука!"
    mt "Не могу поверить что я снова здесь!"
    return

label ep27_dialogues_marcus1_7:

    mt "Кошмарная кровать..."
    mt "Хоть я и првыкла спать в подвале дома, но эта кровать очень жесткая и она плохо пахнет..."
    return

label ep27_dialogues_marcus1_8:
    mt "Решетка..."
    mt "Ее можно подергать, чтобы позвать этого кошмарного Боба..."
    return

label ep27_dialogues_marcus1_9:
    # Моника дергает за решетку
    # Подходит Боб
    music2 stop
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Groove2_85
    img 21235
    with fadelong
    overseer "Ну, что тебе?!"
    overseer "Теперь ты снова будешь целыми днями стучать?"
    overseer "А у меня болит голова!"
    overseer "Еще больше чем ранее!"
    img 21236
    with fade
    mt "Дьявол! Я ненавижу этого урода!"
    mt "Но, по моему опыту, с ним лучше быть повежливее."
    mt "Хоть мне здесь и придется быть лишь до завтрашнего утра, но я уже проголодалась."
    mt "Здесь подают помои, но я немного отвыкла от вкусной еды."
    mt "Для девушки такого уровня как Я будет сложно есть такую пищу, но я научилась справляться с этим."

    music Hidden_Agenda
    img 21237
    with fade
    m "Мистер Боб."
    m "Могли бы Вы принести мне немного Вашей вкусной еды?"
    music Groove2_85
    overseer "Не положено! Сегодня заключенных уже кормили!"
    overseer "Жрать завтра!"
    mt "БОЖЕ! Ну и урод!"
    img 21238
    with diss
    m "Спасибо, Мистер Боб... Я подожду до завтра..."
    img 21239
    with fade
    mt "Не больно-то и хотелось есть его помои!"
    mt "И я рада, что он их не принес!"
    mt "Уж лучше немного подождать до завтра и поесть нормальную еду в городе!"
    return

label ep27_dialogues_marcus1_10:
    # Моника ложится спать
    mt "Я устала. Может быть лечь поспать?"
    menu:
        "Лечь спать.":
            return True
        "Не ложиться.":
            return False
    return

label ep27_dialogues_marcus1_11:
    # Моника легла спать
    music2 stop
    music stop
    img black_screen
    with diss
    pause 2.0
    music Euro_Loop1
    img 21232
    with fadelong
    mt "Завтра новый день."
    img 21233
    with diss
    mt "С утра я встречусь с Маркусом лицом к лицу и решу все мои проблемы."
    mt "Я сильная и я знаю что справлюсь..."
    img 21234
    with diss
    mt "Все будет хорошо!"
    mt "А сейчас пора спать..."

#    img black_screen
#    with Dissolve(2.0)
#    call textonblack(ts__("Узнайте что ждет Монику\nв грядущем обновлении игры!")) from _call_textonblack_33
#    pause 2.0
    img black_screen
    with Dissolve(1.0)
    stop music fadeout 4.0
    $ renpy.pause(4.0, hard=True)
#    pause 4.0
    music Malicious
#    pause 2.0
    $ renpy.pause(2.0, hard=True)
    sound man_steps
#    pause 2.0
    $ renpy.pause(2.0, hard=True)
    sound snd_jail_door
#    pause 2.0
    $ renpy.pause(2.0, hard=True)
    img 21240
    with fadelong
#    pause 2.0
    $ renpy.pause(2.0, hard=True)
    stop music
    sound snd_cinematic_impact
    img black_screen
#    pause 2.0
    $ renpy.pause(2.0, hard=True)
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Fashion Business")) from _call_textonblack_34
    img black_screen
    with Dissolve(2.0)
    $ renpy.pause(2.0, hard=True)
    return


#    img black_screen
#    with Dissolve(0.5)
#    img Patreon_Game_Logo
#    with Dissolve(0.7)
#    $ renpy.pause(1.0, hard=True)
##    pause 4.0
#    $ renpy.pause(4.0, hard=True)
#    img black_screen
#    with Dissolve(0.7)
#    pause 3.0
##    pause 30.0
##    music stop
##    pause 1.0
#    $ MainMenu(confirm=False)()
#    return

#audio_woman_breathing_painfully



#$ jailCageBlackmailBoobsShowed
#$ jailCageBlackmailAssShowed
#$ jailCageBlackmailMonicaSaidSheIsAWhore










#
