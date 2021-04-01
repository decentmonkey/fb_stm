default neighborCalled = False
default neighborOffended1 = False #не здороваться
default neighborOffended2 = False #без разницы что он чуть не погиб
default neighborOffended3 = False #решил потоптать во дворе?
default neighborOffended4 = False #это не просто царапина, наехать
default neighborOffended5 = False #прогнать идиота, грубо
default neighborOffendedSue = False #закатить иск
default neighborOffendedSueBig = False #иск огромный
default neighborOffendedFarm = False #наехать на ферму

label EP1_neighbor_quest1:

    music Funk_Soul1
    img 1095
    w
    img 1096
    fred "Добрый день, Мэм!"

    menu:
        "Спросить что случилось на улице.
        Откуда был шум?":
            jump EP1_neighbor_quest1_1
        "Не спрашивать. Поздороваться грубо":
            call EP1_bitch(2, "fred_hello1")
            img 1100
            m "Мне не нужны пожелания доброго дня от своих слуг."
            "У меня и без тебя день хороший и всегда будет таким!"
            call EP1_get_to_drive_dialogue()
            return

        "Не спрашивать. Просто поздороваться":
            call EP1_bitch(-2, "fred_hello2")
            m "Добрый день, Фред."
            call EP1_get_to_drive_dialogue()
            return

label EP1_neighbor_quest1_1:
    m "К делу, Фред."

    m "Что случилось на улице?"

    "Я проснулась от какого-то шума."

    fred "Ваш сосед, Мэм."

    "Он зацепил газонокосилкой забор."

    m "Свой забор?"

    fred "И свой и Ваш, Мэм!"

    img 1097
    mt "Значит это какой-то криволапый сосед разбудил меня.
    Мне все-равно надо было вставать, но все-же!"

    img 1098
    m "Фред!"

    fred "Да, Мэм?"

    m "Где сейчас этот сосед?"

    fred "Он, как обычно, гуляет у своего дома, Мэм."

    menu:
        "Позови его сюда.":
            jump EP1_neighbor_quest1_2
        "Пусть гуляет, забор - это проблемы мужа. Мне все-равно.":
            m "Пусть гуляет.
            Сообщи моему мужу об этом инциденте, когда он вернется."
            fred "Да, Мэм!
            Конечно!"
            return

label EP1_neighbor_quest1_2:
    $ houseStreetFenceLocationOpened = True
    m "Позови его сюда.
    Быстро."

    fred "Одну минуту, Мэм!"

    #neighbor
    img 4260
    with fadehold
    w
    img 4261
    w
    img 4262
    w
    img 4263
    w
    img 4264
    neighbor "Вау...!"

    img 1099
    with fade
    neighbor "Здравствуйте, Мэм!"

    "Я Ваш сосед."
    "Я..."

    menu:
        "Мне без разницы кто он. Очередной тупица.":
            $ neighborOffended1 = True
            call EP1_bitch(2, "neighbor_dial1")
            m "Я вижу что сосед."

            "Как вы объясните то что произошло?"

        "Поздороваться вежливо, все-таки он мой сосед.":
            call EP1_bitch(-2, "neighbor_dial1")
            $ neighborOffended1 = False
            m "Добрый день.
            Будем знакомы, я Моника."
            "Так что же случилось с утра?"

    neighbor "Видите-ли, дело в том что я с утра решил покосить траву в своем дворе."

    "Все было хорошо, но между домом и забором с Вашей стороны очень тесно."

    "Я пробовал аккуратно стричь газон, но газонокосилка зацепила за забор и взлетела."

    "Она чуть не убила меня!"

    "Я чуть не погиб!"

    menu:
        "Мне нет дела до того погиб-бы ты или нет, придурок!":
            $ neighborOffended2 = True
            call EP1_bitch(2, "neighbor_dial2")
            img 1100
            m "Меня не волнует состояние вашей жизни."

            "Покажите где это случилось."

        "Он был в опасности, это стоит сострадания.":
            $ neighborOffended2 = False
            call EP1_bitch(-2, "neighbor_dial2")
            m "Ничего себе, вам повезло что Вы остались живы!"
            "Я рада что Вы целы!"
            img 1101
            neighbor "Эммм...
            Спасибо, Мэм."
            m "Покажите, пожалуйста, где это случилось?"

    img 1101
    neighbor "Сейчас я Вам покажу."

    "Удобнее будет с Вашей стороны двора."

    menu:
        "Решили потоптать в моем дворе?":
            $ neighborOffended3 = True
            call EP1_bitch(2, "neighbor_dial3")
            img 1102
            m "Решили потоптать в моем дворе?"

            "Или заляпать мне все своими грязными ботинками?"

            img 1103
            w
            img 4265
            neighbor "Вау...!"

            img 1103
            neighbor "Но мэм! У меня чистные ботинки."

            img 1104
            m "У вас грязные ботинки."

            "Да вы и сами грязный. Фу."

            "Показывайте мне быстрее где это случилось."

            img 1105
            neighbor "Пойдемте, мэм, я покажу."


        "Раз удобнее с моей стороны двора, то пойдемте посмотрим с ней.":
            $ neighborOffended3 = False
            call EP1_bitch(-2, "neighbor_dial3")
            img 1097
            m "Хорошо, если так удобнее, то пойдемте."



#

    img 1106
    with fade
    neighbor "Смотрите, Мэм."

    "Тут всего-лишь маленькая царапинка."
    img 1107
    w

    menu:
        "Ох ничего себе! Он сломал мне забор!":
            $ neighborOffended4 = True
            call EP1_bitch(5, "neighbor_dial4")
            jump EP1_neighbor_quest1_3
        "Эту царапину еле видно! Из-за чего весь шум?":
            $ neighborOffended4 = False
            call EP1_bitch(-5, "neighbor_dial4")
            img 1113
            m "И это все?"
            "Из-за этого был весь шум?"
            neighbor "Да, Мэм!"
            "Это всего-лишь царапина, как я и говорил!"
            "Можно я пойду?"
            img 1113
            "Хорошо, идите.
            У меня и так много дел."
            img 1119
            neighbor "До свидания, Мэм.
            Простите что так вышло..."
            return


label EP1_neighbor_quest1_3:
    img 1108
    m "Ох ничего себе!"

    "Маленькая царапинка!"

    "Вы хоть знаете сколько стоит этот забор?"

    img 1109
    neighbor "Да, мэм, но его можно починить."

    "Это совсем не сложно."

    img 1110
    m "У меня был забор."

    "Мне он очень нравился."

    "Мне не так-то много вещей вообще может понравиться."

    "Но этот забор был той вещью, которая мне пришлась по душе."

    img 1111
    "И вы лишили меня этой вещи."

    img 1112
    neighbor "Но мэм!"
    "Его же можно починить."
    "Тут дел на 5 минут!"

    img 1113
    m "Если его починить, то это все-равно уже будет не тот забор, который мне нравился."

    menu:
        "Закатить соседу иск.":
            $ neighborOffended5 = False
            $ neighborOffendedSue = True
            jump EP1_neighbor_quest1_4
        "Прогнать этого идиота":
            $ neighborOffended5 = True
            img 1124
            m "Так что проваливайте отсюда, пока я не разозлилась по настоящему!"
            m "Грязный бомж."
            return

label EP1_neighbor_quest1_4:

    m "Вы отобрали у меня мою вещь."

    "Я считаю что пострадала."

    "Меня устроит комненсация в размере ..."
    menu:
        "$50.000":
            $ neighborOffendedSueBig = True
            call EP1_bitch(10, "neighbor_suebig")
            m "Меня устроит комненсация в размере $50.000."

            "Сюда я включаю ремонт забора и моральный ущерб."

            "Если моральный ущерб вообще можно оценить."

            img 1114
            neighbor "Сколько???"

            "Мэм!"

            "Вы в своем уме?"

            "За какую-то царапину такие деньги!"

            img 1115
            m "Что?"

            "Вы еще и употребили некорректное выражение в мой адрес?"

            "Теперь ущерб составляет $100.000."

            "Я сегодня же свяжусь со своим адвокатом."

            "Его зовут Дик.
            Думаю вы слышали про него."

            "Он закатит вам иск, гораздо превышающий мое условие."

            "И победит."

            img 1116
            neighbor "Дик Адвокат?"

            "О нет!"

            "Я знаю этого человека, Он акула-людоед."

            "Он вытряхивает из людей все до последнего цента."



        "$500":
            $ neighborOffendedSueBig = False
            m "$500.
            Буду честна, эта царапина больше не стоит."
            img 1116
            neighbor "Хмммм...
            Мэм, спасибо!"
            "Это достаточно небольшая сумма, но...."


    m "..."

    img 1117
    neighbor "Мэм!"

    "Я прошу Вас!"

    "У меня и так много долгов."

    if neighborOffendedSueBig == False:
        "Может быть вы просто простите мне эту оплошность?"

    "Банк уже собирается описывать часть моего имущества, включая мою ферму через дорогу."

    menu:
        "Так эта вонючая ферма через дорогу принадлежит вам?":
            call EP1_bitch(3, "neighbor_offendfarm")
            $ neighborOffendedFarm = True

        "Какая еще ферма? Что с деньгами?":
            $ neighborOffendedFarm = False

    if neighborOffendedFarm == True:
        img 1118
        m "Так эта вонючая ферма через дорогу принадлежит вам?"

        "Мне все не доходили руки заняться ей."

        "Она портит мне вид из окна."

        "И я уверена, что если подойти к ней, то она будет вонять."

        "А меня это не устраивает."

        img 1119
        neighbor "Мэм."

        "Это мое хобби."

        "Там нет ничего такого что бы могло портить окружающую среду."

        img 1120
        m "Она выглядит некрасиво, этого достаточно."

    if neighborOffendedFarm == False:
        img 1108
        m "Какая еще ферма?"
        "Что по поводу компенсации ущерба??"
    if neighborOffendedSueBig == True:
        img 1121
        neighbor "Но Мэм!"

        "Прошу Вас!"

        "У меня и так много долгов."

        "Ваш иск просто сломает мне жизнь!!"
        "Прошу Вас."

        "Умоляю!"

        "Не делайте этого!"

        img 1122
        m "После того как Дик оставит вас без штанов, я надеюсь вы уберетесь отсюда со своей фермой."

        m "И я больше никогда не увижу ваше лицо."

    if neighborOffendedSueBig == False:
        img 1121
        neighbor "Мэм.
        Я постараюсь компенсировать эту сумму как можно скорее."
        "Я отдам ее в течении недели!"

        img 1122
        m "Если в течении недели денег не будет, то вы заплатите сумму большую в 10 раз."
        "Мой адвокат позаботится об этом."

    m "И это считайте что я очень добрая."

    img 1123
    m "Люди часто не ценят мою доброту и потом об этом жалеют."

    img 1122
    m "А сейчас покиньте мою собственность, иначе я вызову полицию."

    img 1124
    m "Грязный бомж."
    w



    return
