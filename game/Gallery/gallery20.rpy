label gallery_32236:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14202
    w
    imgf 14203
    m "Что будете заказывать?"
    imgd 14204
    customer1 "В твоем вопросе кое-чего не хватает..."
    customer1 "Разве обслуживающий персонал так должен обращаться с клиентами?"
    music Stealth_Groover
    imgf 14209
    mt "Какого черта этот неудачник постоянно ко мне придирается?"
    mt "И вообще! Я не обслуживающий персонал!"
    mt "Я здесь Королева!"
    mt "!!!"
    menu:
        "Быть вежливой.":
            music Groove2_85
            imgd 14205
            mt "Если я спрошу его вежливо, он быстрее сделает заказ."
            mt "И отстанет от меня со своими дурацкими замечаниями!"
            imgf 14216
            m "Добрый вечер, вы готовы сделать заказ?"
            customer1 "Так значит ты умеешь быть вежливой?"
            customer1 "Умница, детка!"
            customer1 "Принеси мне чего-нибудь на свой выбор."
            #music Pyro_Flow
            imgd 14211
            mt "Никчемный неудачник!"
            mt "Хочет, что бы перед ним выслуживались..."
            m "Одну минуту."
            # уходит, приносит пиво
            fadeblack
            sound highheels_run2
            pause 1.5
            music Groove2_85
            music2 pub_noise1_low
            pause 1.5
            sound snd_plates1
            imgfl 14219
            w
            sound snd_beer_table
            imgf 14220
            m "Пожалуйста, ваш заказ."
            mt "Специально для вас наши лучшие 'помои'..."
            imgd 14221
            customer1 "Стоп!"
            customer1 "Это еще не все..."
            mt "Чего еще ему нужно?!"
            customer1 "Я видел твои выступления на сцене..."
            m "И?"
            customer1 "И готов заплатить тебе $ 5..."
            customer1 "Если дашь мне потрогать твою ножку."
            imgf 14215
            m "..."
#            $ menu_corruption = [0, pubQueenCustomer1CorruptionRequired]
            menu:
                "Нет!":
                    music Stealth_Groover
                    imgd 32232
                    m "Я Королева Shiny Hole!"
                    m "И никому не позволено прикасаться ко мне!"
                    m "Ни за 5 долларов, ни за 1 000 долларов!"
                    imgf 14222
                    mt "Хотя..."
                    mt "За тысячу долларов я подумала бы об этом..."
                    imgd 14223
                    customer1 "Ясно."
                    customer1 "Придется поговорить с Джо о привате с тобой..."
                    customer1 "Все, свободна!"
                    stop music2
                    return
                "Согласиться.":
                    music Hidden_Agenda
                    imgd 14222
                    mt "Всего $ 5?!"
                    mt "Чтобы прикоснуться к моим шикарным ножкам?!"
                    mt "Жмот!"
                    mt "С другой стороны..."
                    mt "Эти деньги для меня не будут лишними..."
                    # оборачивается
                    imgf 32233
                    mt "Надо только проследить, чтобы этого никто не заметил..."
                    m "Только потрогать и быстро!"
                    # клиент кладет руку ей на колено, сбоку
                    # и быстро проводит ею вверх, под юбку, и хватает за попу
#                    $ add_corruption(pubQueenCustomer1Corruption, "customer1_afterbattle")
                    music Loved_Up
                    imgd 32234
                    w
                    sound Jump1
                    imgf 32235
                    w
                    imgd 32236
                    w
                    music stop
                    sound plastinka1b
                    img 32237 hpunch
                    pause 1.5
                    music Pyro_Flow
                    music2 pub_noise1_low
                    m "Что ты делаешь?!"
                    # Моника резко от него отстраняется
                    m "!!!"
                    mt "Мерзавец!!!"
                    music Groove2_85
                    customer1 "Отличная упругая задница! Аха-ха!"
                    customer1 "Я ее себе именно такой и представлял!"
                    mt "Сволочь!"
                    # Моника злобно на него смотрит
#                    $ add_tips(5.0)
                    imgf 32238
                    customer1 "Вот, держи свои 5 баксов."
                    customer1 "Заслужила."
                    customer1 "Все, свободна!"
#                    $ pubQueenCustomer1Day = day
                    stop music2
                    return
        "Ответить грубо":
            # Моника возмущенно
            music Stealth_Groover
            imgd 14215
            mt "Этот пьяница опять решил учить меня манерам?"
            imgf 14216
            m "Полагаю, чего-то вежливого?"
            customer1 "Ага..."
            m "Нет в меню!"
            imgf 14217
            customer1 "Тогда я передумал делать заказ! Можешь идти!"
            mt "Жалкий неудачник!"
            # развернуться и уйти
            fadeblack
            sound highheels_short_walk
            stop music2
            return
    return

label gallery_32251:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14225
    w
    imgf 14229
    customer2 "Ну что, дорогуша!"
    customer2 "Я могу тебя поздравить! Ты стала королевой Shiny Hole!"
    customer2 "Видел твое выступление - папочке понравилось!"
    customer2 "Теперь, наверное, будешь перед всеми хвастаться в своей провинции?"
    customer2 "Жопой трясти - это тебе не картошку сажать... Или что там у вас?!"
    music Stealth_Groover
    imgd 14228
    mt "Я же говорила, что я не из провинции! Болван!"
    mt "Что он вообще несет? Какая к черту картошка?"
    m "Я из этого города, а не из провинции..."
    music Groove2_85
    imgf 14226
    customer2 "Всего пару недель и уже городская? Ик!"
    customer2 "Это так не работает..."
    customer2 "Эх... Вот все вы такие, глупые... Из этих своих провинций."
    customer2 "Ладно, неси пива."
    music Stealth_Groover
    imgd 14227
    mt "Он вообще слышит, что я ему говорю?!"
    mt "Я - Моника Бакфетт, а не какая-то провинциалка!"
    mt "А ты - жалкий неудачник!"
    mt "И это отвратительное пиво - лучшее, на что ты можешь расчитывать!"
    # уходит, приносит пиво
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 14236
    m "Ваше пиво."
    sound snd_beer_table
    imgf 14238
    customer2 "Спасибо, дорогуша."
#    $ add_tips(1.0)
    customer2 "Вот тебе немного чаевых... Съездишь к себе домой, в провинцию..."
    mt "Пьяный болван!"
    customer2 "Не убегай так быстро, дорогуша!"
    customer2 "У меня есть к тебе еще небольшое дельце..."
#    music Pyro_Flow
    imgd 14230
    mt "Что еще?!"
    mt "!!!"
#    music Groove2_85
    imgf 32239
    customer2 "Меня заворожили твои королевские сиськи..."
    customer2 "Порадуй меня ими, дорогуша. Дай потрогать!"
    customer2 "Получишь за это парочку мистеров франклинов!" # подмигивает Монике
    # клиент тянет руку к Монике
    music Stealth_Groover
    imgd 14239
    mt "Конечно, нет!"
    mt "Я - Королева Shiny Hole! А ты - никто!"
    mt "Да что ты позволяешь себе, животное!"
    sound Jump2
    imgf 32240
    m "Не смей прикасаться ко мне!"
    customer2 "Чего ты так взбесилась, дорогуша?"
    customer2 "Тебе не нужен мистер Франклин?"
    m "Я тебе не какая-то дешевка!"
    m "Чтобы позволять прикасаться ко мне за пару долларов!"
    music Groove2_85
    imgd 32241
    customer2 "А... Ну так сразу бы и сказала...."
#    customer2 "А что насчет Гамильтона?! Ик!"
    customer2 "А если просто посмотреть на них?"
#    $ menu_corruption = [0, pubQueenCustomer2CorruptionRequired]
    menu:
        "Мое решение неизменно!":
            imgf 32242
            m "Мое решение неизменно!"
            m "Если это все, я ухожу!"
            customer2 "Ну и проваливай, Королева Hole!"
            imgd 14227
            mt "Грязное животное!!!"
            mt "!!!"
            sound highheels_short_walk
            stop music2
            return
        "Мне нужны деньги!":
            imgf 32243
            mt "Черт!"
            mt "Мне нужны эти деньги!"
            mt "Моя жизнь стала похожа на ужасный сон!"
            mt "Сон, в котором мне приходится считать каждый доллар!"
            mt "Когда этот кошмар закончится?!"
            imgd 32244
            m "!!!"
            m "Деньги вперед! И держи свои руки при себе!"
            # Моника забирает деньги
            imgf 32245
            w
            sound vjuh3
            imgd 32246
            w
            # Моника оглядывается по сторонам что бы убедиться что никто не смотрит
            # показывает грудь
#            $ add_corruption(pubQueenCustomer2Corruption, "customer2_afterbattle")
            sound Jump1
            imgf 32247
            w
            sound Jump1
            imgd 32248
            w
            sound Jump2
            imgf 32249 vpunch
            w
            sound wow
            imgd 32250
            customer2 "Оооо! У вас, провинциалок, сиськи что надо!"
            customer2 "Действительно королевские сиськи!!!"
            # клиент хватает ее за грудь
            # Моника отпрыгивает от него
            music stop
            sound plastinka1b
            img 32251 vpunch
            w
            music Stealth_Groover
            imgf 32252
            m "С тебя достаточно!!!"
            m "!!!"
#            $ add_tips(10.0)
            fadeblack 1.0
            # Мон уходит
            sound highheels_short_walk
            stop music2
            # доход 10 $
#            $ pubQueenCustomer2Day = day
            return
    return

label gallery_32256:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14249
    w
    imgf 14250
    customer3 "О, сама королева Shiny Hole будет меня обслуживать!"
    customer3 "Решила предложить мне приват?"
    m "Нет, я готова принять ваш заказ."
    customer3 "Тогда записывай. Я делаю заказ на приватный танец в твоем исполнении!"
    customer3 "Или снова будешь врать, что не танцуешь?"
    imgd 14251
    m "Я не танцую приватные танцы."
    m "Мои выступления проходят только на сцене."
    imgf 14252
    customer3 "Обманывать нехорошо, милочка!"
    if customer3_after_private == True:
        customer3 "Ты уже была в привате со мной. Ха-ха-ха!"
    customer3 "Давай так!"
    customer3 "Если я куплю приват с тобой..."
    customer3 "То ты сделаешь мне бесплатный минет за то, что обманываешь."
    music Pyro_Flow
    img 14256 hpunch
    m "ЧТООО?!?!!"
    m "НЕТ!"
    mt "Он совсем охренел?!"
    mt "?!?!?!"
    mt "А вдруг этот неудачник договорится с Джо?!"
    mt "Что же тогда делать!?"
    music Groove2_85
    imgf 14257
    customer3 "АГА!!!"
    customer3 "ЗАНЕРВНИЧАЛА!?"
    customer3 "Но зато, если ты не обманщица, я заплачу тебе $ 10 моральной компенсации!"
    customer3 "Что скажешь?"
    music Hidden_Agenda
    imgd 14258
    mt "Думай, Моника! Думай!"
    mt "Возможно, стоит сказать, что я временно не танцую приваты?"
    mt "Или соврать, что приватный танец стоит $ 2000? Я же королева Shiny Hole..."
    if customer3_after_private != True:
        mt "Вряд ли у кого-то в этой дыре найдутся такие деньги!"
        mt "А вдруг у него найдутся?!"
    music Groove2_85
    imgd 14254
    customer3 "Хотя нет, у меня сейчас нет денег на приват с тобой..."
    customer3 "Неси заказ!"
    sound Jump2
    imgf 14266
    w
    sound highheels_short_walk
    imgd 14267
    w
    imgd 14268
    w
    # уходит - приносит
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 14270
    w
    imgf 14271
    w
    sound snd_beer_table
    imgd 14272
    m "Ваш заказ."
    imgf 14273
    customer3 "Ага..."
    customer3 "На чаевые ты не заработала!"
    customer3 "Хотя..."
    customer3 "Если ты приспустишь трусики и покажешь мне свою попку..."
    customer3 "Я готов заплатить тебе $ 10!"
    imgd 14281
    m "..."
#    $ menu_corruption = [0, pubQueenCustomer3CorruptionRequired]
    menu:
        "Нет!":
            music Stealth_Groover
            imgf 14286
            mt "Для тебя - ни за какие деньги на свете!"
            imgd 14279
            m "Я обнажаюсь только на сцене..."
            m "И только для танца!"
            customer3 "Ну тогда проваливай!"

            # Моника злится
            pass
        "Мне нужны деньги...":
            imgf 14278
            mt "Эти $ 10 для меня не будут лишними..."
            imgd 14274
            m "Только быстро..."
            customer3 "Ага... Давай!"
            customer3 "Хоть посмотрю вблизи на королевску попку! Аха-ха!!"
            # Моника оглядывается что никто не смотрит
            # Задирает юбку сзади
            # потом быстро натягивает трусики обратно и опускает юбку
            fadeblack 1.5
#            $ add_corruption(pubQueenCustomer3Corruption, "customer3_afterbattle")
            music Loved_Up
            imgf 32253
            w
            sound Jump2
            imgd 32254
            w
            sound Jump1
            imgd 32255
            w
            imgf 32256
            w
            imgd 32257
            w
            imgf 32255
            w
            sound Jump1
            imgd 32254
            w
            sound Jump2
            imgd 32253
            w
            music Groove2_85
            imgf 14280
            m "Достаточно! Давай мои деньги!"
            customer3 "Отличная задница! У меня даже привстал! Аха-ха!"
            customer3 "Держи свои десять баксов!"
            # дает ей деньги
            imgd 32258
#            $ add_tips(10.0)
            customer3 "И жди меня на привате в скором времени!" # подмигивает
            customer3 "Там ты не отделаешься так легко, королева! Аха-ха!!!"
            customer3 "Я вгоню свой член в твою упругую попку!"
            imgd 14286
            mt "Мерзавец!"
            mt "!!!"
#            $ pubQueenCustomer3Day = day
            pass
    imgf 14296
    sound highheels_short_walk
    customer3 "Свободна!"
    mt "Жалкий неудачник!"
    mt "!!!"
    stop music2
    return

label gallery_32262:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14320
    m "Здравствуйте! Что будете заказывать?"
    customer4 "Привет, симпатичная мордашка!"
    customer4 "Принеси мне Ваш восхитительный Shiny бургер. Очень уж он мне нравится."
    imgf 14339
    mt "Восхитительный бургер?!" # Моника надменно улыбается
    # Моника поглощена воспоминаниями о изысканной жизни
    music Stealth_Groover
    mt "Это фуа-гра с трюфелем восхитительны, болван! Но откуда тебе знать?"
    mt "Ты, наверное, и слов таких никогда не слышал..."
    mt "О, Моника! Ты достойна своей прежней роскошной жизни!"
    mt "Среди лоска и изыска..."
    mt "С шампанским и восхитительной изысканной высокой кухней!"
    music Groove2_85
    # кадр на клиента
    imgd 14323
    customer4 "Эй, мордашка! Ты чего там зависла? Неси заказ!"
    imgf 14324
    mt "Вот черт..."
    mt "Я замечталась..."
    mt "..."
    mt "Грубиян!"
    imgd 14321
    customer4 "Знаешь, мордашка! Ты так сильно похожа на одну девицу из телика."
    mt "!!!"
    customer4 "Не будь ты официанткой..."
    customer4 "Как же ее звали? Погоди, сейчас вспомню..."
    customer4 "Ми... Ма..."
    customer4 "А, точно! МОНИКА!"
    # Мон в ужасе!!!!!
    music Power_Bots_Loop
    img 32259 hpunch
    mt "ОН УЗНАЛ МЕНЯ!!!"
    mt "УЗНАЛ!!!"
    mt "!!!"
    mt "МОНИКА, ЧТО ТЕПЕРЬ ДЕЛАТЬ!?"
    mt "АААААААА!!!"
    music Groove2_85
    imgd 32260
    customer4 "Да, Моника... Как я мог забыть?"
    customer4 "В сериале каком-то снимается..."
    customer4 "Хотя... Вот сейчас смотрю на тебя - совсем не похожа..."
    customer4 "Та, в телике, посимпатичнее была."
    music Stealth_Groover
    imgf 14342
    mt "Сериале?"
    mt "Посимпатичнее?!"
    mt "Я! Я самая красивая женщина этого города!"
    mt "И я не какая-то официантка, Я БИЗНЕС-ЛЕДИ! Я Моника Бакфетт!"
    mt "!!!"
    mt "С другой стороны, хорошо, что этот пьяный кретин меня не узнал..."
    music Groove2_85
    imgd 14326
    customer4 "Не растраивайся, мордашка. Хочешь 5 баксов?"
    m "..."
    customer4 "Молчание - знак согласия."
    customer4 "Тогда дай потрогать твои сиськи."
    m "..."
#    $ menu_corruption = [0, pubQueenCustomer4CorruptionRequired]
    menu:
        "Нет!":
            music Stealth_Groover
            imgf 14327
            mt "Он решил, что может облапать МЕНЯ, Королеву Shiny Hole?!"
            mt "За какие-то жалкие 5 долларов?!"
            mt "!!!"
            imgd 14328
            m "Нет!"
            m "Я не оказываю подобные услуги!"
            m "Я здесь Королева, а не какая-нибудь дешевая проститутка!"
            m "Хочешь протрогать грудь - иди к этой рыжей Молли!"
            m "Она тебе за 5 долларов сделает все, что захочешь!"
            customer4 "Она мне уже надоела!"
            m "Ничем не могу помочь!"
            customer4 "Это мы еще посмотрим..."
            pass
        "Согласиться.":
            imgf 14342
            mt "Всего $ 5?!"
            mt "С другой стороны..."
            mt "Он ведь только прикоснется..."
            mt "Черт!"
            # Моника оглядывается что никто не смотрит
            # наклоняется к клиенту
            # клиент обеими руками обхватывает грудь Моники и тискает
            # Моника отпрыгивает
            fadeblack
            sound snd_fabric1
            pause 1.5
#            $ add_corruption(pubQueenCustomer4Corruption, "customer4_afterbattle")
            music Loved_Up
            imgfl 32261
            w
            imgf 32262
            w
            imgd 32263
            w
            sound Jump2
            imgf 32264
            m "Все! Этого достаточно!"
            music Groove2_85
            customer4 "Отличные сиськи!"
            customer4 "Трахнуть бы тебя между ними!"
            mt "Фу! Извращенец!"
            mt "!!!"
            customer4 "Вот. Держи свои пять баксов..."
#            $ add_tips(5.0)
            fadeblack 1.5
            # дает ей деньги
#            $ pubQueenCustomer4Day = day
            pass
    music Groove2_85
    imgd 32265
    customer4 "Теперь неси скорее Ваш Shiny бургер и пиво!"
    # уходит - приносит
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 14336
    w
    imgf 14334
    w
    sound snd_beer_table
    imgd 14337
    customer4 "Держи доллар за красивую мордашку!"
#    $ add_tips(1.0)
    imgf 14338
    customer4 "А где спасибо?"
    m "Спасибо..."
    mt "Придурок!"
    stop music2
    return

label gallery_32271:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14298
    w
    imgf 14302
    m "Здравствуйте. Желаете сделать заказ?"
    customer5 "Оооо!"
    customer5 "Самая лучшая задница Shiny Hole ко мне пришла!"
    customer5 "Повернись ко мне своей сладкой попкой! Хочу с ней поздороваться!"
    imgd 14299
    mt "!!!"
    m "Что будете заказывать?"
    imgd 14300
    customer5 "Неси бургер! А когда будешь идти, повиляй своей раскошной задницей... И подмигни мне."
    customer5 "Я хорошо приплачу тебе за это! $ 10!"
    m "..."
    menu:
        "Принести заказ как обычно.":
            # на лице Моники отвращение и раздраженность, она оскорблена
            music Stealth_Groover
            imgf 14307
            m "Я принесу ваш заказ, но без виляний и подмигиваний."
            mt "Мерзкий извращенец!"
            mt "!!!"
            pass
        "$ 10? Хммм...":
            imgf 14301
            mt "$ 10 за то, чтобы пройтись и подмигнуть? Не самая плохая сделка..."
            mt "Боже, Моника! Не могу поверить!"
            mt "Ты готова выслуживаться за $ 10 перед каким-то грязным пьяньчугой?!"
            mt "Да что с тобой такое?!"
            music Hidden_Agenda
            mt "С другой стороны..."
            mt "А если на это согласится не Моника, а Королева Shiny Hole?"
            mt "..."
#            music Groove2_85
            imgd 14304
            m "Только деньги вперед!"
#            $ add_tips(10.0)
            # он дает ей деньги, Моника удаляется за заказом виляя попой,
            # поворачивается и подмигивает
            fadeblack 1.5
#            $ add_corruption(pubQueenCustomer5aCorruption, "customer5_afterbattle1")
            music Loved_Up
            imgf 32270
            sound highheels_short_walk
            w
            sound Jump2
            imgd 32271
            w
            pass
    # уходит-приходи с заказом
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 32266
    m "Ваш заказ."
    imgf 32267
    customer5 "О, детка, смотри! Мой дружок оценил твою попку!"
    customer5 "Может потрешься об него? За $ 50. Что скажешь?"
#    $ menu_corruption = [0, pubQueenCustomer5CorruptionRequired]
    menu:
        "Отшить мерзавца!":
            music Pyro_Flow
            imgd 32268
            mt "Грязный свин!"
            mt "Перевернуть бы этот бургер на его тупую голову!"
            mt "Но тогда Эшли меня сразу уволит..."
            mt "А мне пока нужны работа в этой грязной дыре!"
            music Stealth_Groover
            imgd 32269
            m "Нет!" # высокомерно
            m "Внимание Королевы Shiny Hole стоит в десятки раз дороже!"
            customer5 "Даже так?!"
            customer5 "Хм... Я поговорю с Джо..."
            customer5 "Узнаю, сколько стоит твой приват..."
            mt "Тебе не по карману, неудачник!"
            mt "!!!"
            pass
        "Мне нужны деньги":
            imgd 32272
            mt "$ 50 звучит неплохо..."
            mt "Черт! Мне нужны эти деньги!"
            mt "!!!"
            m "..."
            imgd 32273
            #customer5 "Сойдет для первого раза."
            customer5 "Давай уже, не томи! Мой дружок тебя заждался!"
            # Моника садится к нему на колени,
            label gallery_32276:
            fadeblack 1.5
#            $ add_corruption(pubQueenCustomer5bCorruption, "customer5_afterbattle2")
            music Loved_Up
            imgfl 32274
            customer5 "Оооооо! Королевская жопа!!!"
            imgf 32275
            w
            sound Jump2
            imgd 32276
            w
            # хватает Мон за попу и та отпрыгивает
            music stop
            sound plastinka1b
            img 32277 hpunch
            m "Достаточно! А теперь плати!"
            music Groove2_85
            customer5 "Ух, какая ты горячая штучка!"
            customer5 "Что насчет привата, а?"
            # Мон раздражительно
            m "Я не танцую приваты!"
            m "Ты и так уже получил достаточно внимания от королевы Shiny Hole!!!"
            customer5 "Раньше ты говорила, что на сцене не танцуешь..."
            customer5 "А теперь ты - Королева Shiny Hole... Хе-хе..."
            customer5 "Ладно, Королева, позови Джо!"
            customer5 "Хочу оставить отзыв о твоей работе..."
            imgf 32278
            m "Зачем вам Джо?"
            mt "О боже, он хочет рассказать о том, что я только что сделала!"
            mt "Или этот мерзавец хочет заказать приват через Джо!?"
            customer5 "А знаешь что, я сам к нему подойду! Так что топай..."
            m "А деньги?!"
            imgd 32280
            customer5 "О, точно! Нууу, ты слегка коснулась своей попкой меня..."
            customer5 "А теперь деньги слегка коснутся твоей ручки..."
            # проводит деньгами по руке Мон и подмигивает ей, деньги не дает
            imgf 32279
            w
            sound vjuh3
            img 32281 vpunch
            w
            imgd 32280
            customer5 "А это, за сервис."
#            $ add_tips(2.0)
            fadeblack 1.5
#            $ pubQueenCustomer5Day = day
            # Дает ей пару баксов
            pass
    # Моника злится и уходит
    # он шлепает по попе уходящую Мон, она отпрыгивает, куксит злую моську и уходит
    sound highheels_short_walk
    imgf 32282
    mt "Грязный извращенец!"
    mt "И ты, и все остальные мерзавцы!"
    mt "Вы все поплатитесь!!!"
    mt "Вы еще узнаете, кто такая Моника Бакффет!!!"
    mt "!!!"
    stop music2
    return

label gallery_32287:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14425
    w
    imgf 14427
    m "Здравствуйте. Что будете заказывать?"
    customer7 "Эй, детка! Это твой костюмчик для сцены?"
    sound Jump2
    img 32283 hpunch
    # пытается облапать Монику за грудь
    music Pyro_Flow
    m "Эй! Что ты делаешь?!"
    m "Убери руки!"
    m "Я работаю здесь официанткой!!"
    m "Не смей ко мне прикасаться!"
    music Groove2_85
    imgf 14433
    customer7 "Ладно, ладно... Остынь."
    customer7 "Официантка - это скучно."
    customer7 "Лучше полезай на сцену и сними с себя этот костюмчик!"
    customer7 "Как ты это умеешь делать. Аха-ха!"
    m "Я же уже сказала, что сегодня работаю здесь официанткой!"
    imgd 14431
    mt "Здесь одни извращенцы и пьяницы!"
    mt "Похоже я здесь единственный нормальный человек!"
    mt "Ну и Клэр еще..."
    imgd 14430
    customer7 "Ладно... Раз не хочешь танцевать, тогда хоть выпить нам принеси..."
    customer7 "Неси пару лонг-дринков! И покрепче!!"
    mt "Нахал! Может плюнуть ему в коктейль?"
    # уходит - приносит
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 14464
    w
    imgf 14465
    w
    imgd 14466
    m "Пожалуйста, ваши коктейли!"
    imgf 14467
    customer7 "Умница, детка!"
    customer7 "Хочешь чаевых?"
    m "..."
    customer7 "Ну-ка, наклонись вперед!"
    customer7 "Я положу пару баксов тебе и твоим малышкам!"
    # Моника злобно смотрит
    m "..."
#    $ menu_corruption = [0, pubQueenCustomer78CorruptionRequired]
    menu:
        "Нет!":
            music Stealth_Groover
            imgd 14469
            m "Оставь свои пару баксов себе!"
            m "Похоже, тебе они нужнее."
            customer7 "Эй, полегче!"
            customer7 "За такой сервис и цента не оставлю!"
            imgd 14475
            sound highheels_short_walk
            mt "Да пошли вы, два придурка!"
            mt "Уроды!"
            mt "!!!"
            # уйходит без чаевых
            pass
        "Сделать, как просят клиенты!":
            imgd 14468
            mt "Черт!"
            mt "Лишние деньги мне не помешают..."
            # Моника боязливо оглядывается, чтобы никто этого не увидел
            # наклоняется вперед, выставляя грудь на показ
            fadeblack 1.5
#            $ add_corruption(pubQueenCustomer78Corruption, "customer78_afterbattle")
            music Loved_Up
            imgfl 32284
            m "Быстрее!"
            imgf 32285
            w
            imgd 32286
            customer7 "Отличные сиськи!"
            # засовывает деньги Монике между грудями
            customer7 "Держи, детка!"
            customer7 "Вот твои $ 5!"
            sound vjuh3
            imgd 32287
#            $ add_tips(5.0)
            customer7 "За шикарные королевские сиськи!"
            customer7 "Аха-ха!!!"
            mt "!!!"
            fadeblack 2.0
            music Stealth_Groover
#            $ pubQueenCustomer78Day = day
            pass
    imgf 14459
    mt "Все так и норовят облапать меня!"
    mt "Почему меня, такую красивую и хорошую женщину..."
    mt "Окружают одни извращенцы!"
    mt "!!!"
    stop music2
    return

label gallery_32289:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14359
    m "Здравствуйте. Что будете заказывать?"
    customer10 "Моя Виолетта пришла поздоровоться?"
    customer10 "Или ты хочешь узнать, как мне твое выступление на сцене?"
    imgf 14366
    mt "Мне все равно, что думает об этом такой извращенец, как ты!"
    mt "!!!"
    imgd 14361
    customer10 "Не переживай, мне понравилось..."
    customer10 "А знаешь, что мне понравится еще больше?"
    customer10 "Если ты сейчас же запрыгнешь на этот пилон... Или на меня."
    imgd 14364
    m "!!!"
    m "Я не собираюсь танцевать!"
    customer10 "А я слышал, что танцуешь..."
    customer10 "И не только..."
    m "!!!"
    imgf 14370
    customer10 "Можем пойти в гримерку..."
    customer10 "Я намажу тебя маслом для выступления на сцене..."
    customer10 "Я хорошо промажу все твои формы."
    mt "Мерзавец! Как он смеет так со мной говорить!?"
    m "Если вы хотите сделать заказ на еду или выпивку, то я вас слушаю."
    m "В противном случае - я ухожу!"
    imgd 14368
    customer10 "Ты не в настроении что-ли?"
    customer10 "Так бы и сказала, что в следующий раз..."
    mt "Никакого следующего раза не будет!"
    customer10 "Сейчас принеси мне пива, а я посмотрю на твою задницу..."
    customer10 "А вечером буду представлять, как ты трешься ею об меня..."
    customer10 "И дрочить. Аха-ха!"
    music Pyro_Flow
    imgd 14377
    mt "Он думает мне должно это нравится?!"
    mt "Это звучит омерзительно!"
    # уходит приходит
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 14372
    w
    imgf 14373
    w
    imgd 14374
    sound snd_beer_table
    m "Ваш заказ..."
    customer10 "Ага... Молодец..."
    customer10 "Дай я отблагодарю тебя своим горячим поцелуем, Виолетта!"
    imgf 14375
    mt "Фу! Нет!"
    mt "!!!"
    # Моника корчит моську отвращения
    customer10 "Или ты можешь подарить мне свой королевский поцелуй сама!"
    customer10 "$ 20 - достаточная цена королевы Shiny Hole?!"
#    $ menu_corruption = [0, pubQueenCustomer10CorruptionRequired]
    menu:
        "Нет!":
            music Stealth_Groover
            imgd 14379
            m "Королевский поцелуй может подарить лишь [monica_pub_name]!"
            m "Она новая королева Shiny Hole!"
            m "А Виолетта не дарит королевские поцелуи!"
            m "Даже за $ 1 000!"
            customer10 "Овца!"
            imgd 14377
            mt "УРОД!"
            pass
        "Эти $ 20 не будут лишними...":
            music Stealth_Groover
            imgd 14380
            mt "Целовать это мерзкое существо..."
            mt "Фу! Он омерзителен мне!"
            mt "Но эти $ 20 не будут лишними..."
            # клиент тянеся губами к Монике
            music Groove2_85
            imgf 32288
            w
            imgd 32289
#            $ add_corruption(pubQueenCustomer10Corruption, "customer10_afterbattle")
            m "Но только королевский поцелуй в щеку..."
            imgf 32290
            customer10 "На пилоне с голой жопой значит..."
            customer10 "А поцелуй, как от монашки?"
            customer10 "Такое кидалово и $ 5 не стоит, Виолетта!"
            customer10 "Давай королевский засос прямо в губы..."
            imgd 32291
            m "Фу!"
            m "НЕТ!"
            customer10 "Тогда свободна!"
#            $ pubQueenCustomer10Day = day
            pass
    sound highheels_short_walk
    imgf 32292
    mt "Этот район кишит извращенцами и отбросами..."
    mt "Ненавижу их всех!"
    mt "!!!"
    stop music2
    return

label gallery_32293:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 14394
    m "Здравствуйте."
    m "Что будете заказывать?"
    imgf 14395
    customer9 "Ну здравствуй, горячая королевская киска!"
    customer9 "Я рад, что ты ко мне подошла."
    customer9 "Сегодня я принес тебе подарочек! Хочешь его получить?"
    customer9 "Присаживайся к Санте на колени."
    imgd 14396
    mt "К черту такого Санту!"
    imgd 14397
    m "Мне не нужен ваш подарок!"
    customer9 "Ладно, сегодня Санта добрый..."
    customer9 "Поэтому эта проказница все равно получит то, что принес ей Санта."
    # клиент показывает у себя в руках кружевные трусики
    sound vjuh3
    imgf 32293
    w
    imgd 32294
    m "Трусы?!"
    customer9 "Я хотел забрать твои трусики, когда ты выступала..."
    customer9 "Надеялся, ты кинешь их мне..."
    customer9 "Мммм... Трусики с твоей горячей киски..."
    imgd 32295
    mt "Фу! Грязный извращенец!!!"
    imgf 32296
    customer9 "Но не вышло..."
    customer9 "Поэтому я решил, что ты можешь поносить эти трусики для меня."
    customer9 "А я буду их нюхать и облизывать вечерами. И дрочить на них. Хе-хе!"
    customer9 "Ну как? Тебе нравится моя идея?"
    music Stealth_Groover
    imgd 14402
    mt "!!!"
    mt "КАК ТАКОЕ ВООБЩЕ МОЖЕТ НРАВИТСЯ!?!?!"
    m "Я не буду этого делать!"
    m "Сам носи эти трусики и дро... И делай с ними, что хочешь!"
    music Groove2_85
    customer9 "А если я заплачу тебе $ 50 за это?"
    customer9 "Ты их поносишь немного, а потом отдашь мне."
    customer9 "Что скажешь?"
    m "..."
#    $ menu_corruption = [0, pubQueenCustomer9CorruptionRequired]
    menu:
        "Отказаться!":
            imgf 14407
            m "Я уже сказала нет! Но могу повторить еще раз. НЕТ!"
            mt "Грязное животное!"
            imgd 14401
            customer9 "Горячая киска растроила Санту..."
            customer9 "Проваливай!"
            customer9 "Плохая киска!"
            sound highheels_short_walk
            imgf 14410
            mt "Придурок!"
            mt "!!!"
            # Моника уходит
            music2 stop
            return
        "$ 50?":
            imgf 14403
            mt "У меня сейчас такое тяжелое положение... Каждый доллар на счету."
            mt "О, Боже!"
            mt "На какие ужасные вещи мне приходится идти, чтобы заработать!"
            mt "!!!"
            music Hidden_Agenda
            mt "Хм... А что, если..."
            mt "..."
#            $ add_corruption(pubQueenCustomer9Corruption, "customer9_afterbattle")
            imgd 14404
            m "Я надену их только за $ 5 000!"
            customer9 "Эй! Эти трусы стоят 6 баксов! Откуда такие цены?!"
            m "А как ты хотел? Вообще-то, Я - Королева Shiny Hole!"
            m "!!!"
            customer9 "$ 200!"
            m "$ 4 000 и ни центом меньше!"
            music Groove2_85
            imgd 14405
            customer9 "Я подумаю над этим предложением, детка..."
            # Моника уходит
            sound highheels_short_walk
            imgf 14410
            mt "Такая шикарная женщина, как Я, тебе не по карману!"
            mt "Неудачник!"
            music2 stop
#            $ pubQueenCustomer9Day = day
            return
    return

label gallery_32301:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 pub_noise1_low
    imgfl 32297
    m "Здравствуйте. Готовы сделать заказ?"
    imgf 32298
    customer11 "Неужели! Наконец-то!"
    customer11 "Изволила подойти!"
    customer11 "Ты королева или официантка?!"
    customer11 "Видишь, что гость сидит?!"
    customer11 "Это значит, что нужно тащить свою задницу и принимать заказ!"
    # Мон злится
    imgd 32299
    mt "Похоже, в этом пабе собрались все хамы города..."
    imgf 32300
    customer11 "Неси мне... Знаешь что... Хммм..."
    # рука клиента заныривает под юбку Моники сзади
    sound Jump2
    imgd 32301
    w
    music Pyro_Flow
    img 32302 hpunch
    mt "ОН ЧТО!!"
    mt "ЛАПАЕТ МЕНЯ!?!?!"
#    $ menu_corruption = [pubQueenCustomer11aCorruptionRequired]
    menu:
        "Промолчать.":
            imgf 32303
            mt "Врезать бы ему!!!"
            mt "Как он посмел лапать МЕНЯ?!"
            mt "?!?!?!"
            mt "Так, Моника, спокойно!"
            mt "Теперь, когда я зарабатываю больше, я не могу потерять этот источник дохода!"
            music Groove2_85
            mt "Просто сделай вид, что ничего не происходит..."
            imgd 32304
            m "Вы готовы сделать заказ?"
            customer11 "Так ты королева или официантка?"
            m "Теперь я Королева Shiny Hole!"
            customer11 "А киска у тебя тоже королевская?"
            customer11 "Хочу поверить..."
            customer11 "Сколько стоит свидание с твоей киской?"
            m "..."
#            $ menu_corruption = [pubQueenCustomer11bCorruptionRequired]
            menu:
                "$ 100!":
                    imgf 32299
                    mt "Он уже видел меня полностью голой со сцены..."
                    mt "И извращенка Эшли следит, чтобы я выслуживалась перед клиентами!"
                    imgd 32298
                    m "$ 100 чтобы посмотреть!"
                    customer11 "Даааа... Цены у тебя королевские!"
                    customer11 "Я дам $ 20!"
#                    $ menu_corruption = [pubQueenCustomer11cCorruptionRequired]
                    menu:
                        "Да.":
                            pass
                        "Нет!":
                            music Pyro_Flow
                            imgf 32305
                            sound highheels_short_walk
                            mt "Иди в жопу, придурок!"
                            mt "!!!"
                            music2 stop
                            # уходит
                            return
                    imgf 32306
                    m "$ 20 и ни центом меньше!"
                    customer11 "Договорились!"
                    customer11 "Показывай свою подружку..."
                    # Моника оглядывается, поверяет что никто не смотрит
                    # покзывает киску, приспуская трусики (быстро) спереди
                    label gallery_32309:
                    fadeblack 1.5
#                    $ add_corruption(pubQueenCustomer11Corruption, "customer11_afterbattle")
                    music Loved_Up
                    imgf 32307
                    w
                    sound Jump2
                    imgd 32308
                    w
                    sound Jump1
                    imgd 32309
                    w
                    imgd 32310
                    w
                    fadeblack
                    sound snd_fabric1
                    pause 1.5
                    music Groove2_85
                    imgfl 32311
                    customer11 "А сколько стоит лизнуть ее?"
                    m "Нисколько!!!"
                    m "Можно только смотреть!!!"
                    m "!!!"
                    customer11 "Тогда неси мне бургер и пива..."
                    customer11 "От ее вида у меня все пересохло во рту..."
                    customer11 "Горячая королевская киска!"
                    mt "Извращенец!"
                    # уходит приходит
                    fadeblack
                    sound highheels_run2
                    pause 1.5
                    music Groove2_85
                    music2 pub_noise1_low
                    pause 1.5
                    sound snd_plates1
                    imgfl 14387
                    w
                    imgf 14389
                    m "Ваш заказ..."
                    sound snd_beer_table
                    imgd 14390
                    customer11 "Как захочешь еще что-то показать, тащи сюда свой зад..."
                    customer11 "А сейчас брысь!"
#                    $ add_tips(20.0)
                    # оплата
                    music Pyro_Flow
                    imgf 14386
                    mt "Фу! Мерзость! И эти ужасы я должна терпеть!"
                    mt "!!!"
                    music2 stop
#                    $ pubQueenCustomer11Day = day
                    return
                "Нисколько!":
                    music Power_Bots_Loop
                    img 32312 vpunch
                    mt "Я больше не могу это терпеть!"
                    music Stealth_Groover
                    imgf 32313
                    m "Свидание с моей к... Кхм..."
                    # клиент лезет к ней рукой, Моника отстраняется
                    m "Уберите свои руки!"
                    m "И делайте уже заказ, если вообще собирались его делать!"
                    imgd 32314
                    customer11 "Проваливай! Грубиянка!"
                    customer11 "Не порть мне вечер!"
                    customer11 "Пошла вон!"
                    music2 stop
                    return
        "Уберите свои руки!":
            pass
    sound highheels_short_walk
    imgd 32305
    mt "Грубиян!"
    mt "Мерзкое инстинктивное животное!"
    mt "!!!"
    music2 stop
    return

label gallery_32319:
    fadeblack 2.0
    music Groove2_85
    music2 pub_noise1_low
    # кадр на клиента. Он свистит и подзывает рукой
    imgfl 32315
    customer12 "Эй ты! Тащи свои королевские сиськи сюда!"
    sound highheels_short_walk
    imgf 14412
    m "Меня зовут [monica_pub_name]."
    m "А не сис... Кхм..."
    m "Вы хотели сделать заказ?"
    imgd 14414
    customer12 "Нет. Хотел посмотреть на твои сиськи... Аха-ха!"
    m "Или делайте заказ или я ухожу!"
    imgf 14413
    customer12 "Ха! Я и жопу твою заценю, когда уходить будешь!"
    m "Я ухожу!"
    mt "Грубиян!"
    imgd 14417
    customer12 "Подожди! Я сделаю заказ!"
    customer12 "Хочу еще раз посмотреть на твои сиськи, когда ты принесешь мой заказ..."
    customer12 "Ну-ка! Давай быстро, как козочка, спрыгай мне за пивом!"
    music Pyro_Flow
    imgf 14422
    mt "Грязное отродье!"
    mt "Обращается со мной, как с дешевкой какой-то!"
    mt "!!!"
    # уходит-приходит с пивом
    fadeblack
    sound highheels_run2
    pause 1.5
    music Groove2_85
    music2 pub_noise1_low
    pause 1.5
    sound snd_plates1
    imgfl 14446
    m "Ваш заказ."
    mt "Идиот!"
    imgf 14447
    customer12 "Спасибо! Отличные королевские сиськи! Аха-ха!"
    sound snd_beer_table
    imgd 14448
    m "До свидания!"
    customer12 "Подожди!"
    customer12 "А жопа такая же королевская?"
    customer12 "А знаю... Ты же тут ничего бесплатно не делаешь..."
    customer12 "$ 20 устроит?"
    m "..."
#    $ menu_corruption = [0, pubQueenCustomer12CorruptionRequired]
    menu:
        "Нет!":
            music Stealth_Groover
            imgf 14449
            mt "Для тебя ни за какие деньги на свете!"
            imgd 14450
            m "Я обнажаюсь только на сцене..."
            m "И только для танца!"
            music Groove2_85
            customer12 "Цену набиваешь?"
            customer12 "Ну тогда я отсюда посмотрю на твой зад!"
            customer12 "Свободна!"
            # Моника злится
            #music Pyro_Flow
            imgf 14423
            sound highheels_short_walk
            mt "Сволочь!"
            mt "!!!"
            pass
        "Мне нужны деньги...":
            imgf 14449
            mt "Теперь для меня даже $ 20 - большие деньги..."
            imgd 32316
            m "Я не стану ее оголять..."
            customer12 "А я и не просил..."
            customer12 "Но теперь подумаю об этом! Аха-ха!"
            # Моника оглядывается что никто не смотрит
            # Задирает юбку сзади
            # Клиент оттягивает трусы Моники  и они отстреливают ей по попе
            # Моника отпрыгивает
            fadeblack 1.5
#            $ add_corruption(pubQueenCustomer12Corruption, "customer12_afterbattle")
            music Loved_Up
            imgf 32317
            w
            sound Jump2
            imgd 32318
            w
            imgf 32320
            w
            sound vjuh3
            imgd 32319
            w
            sound Jump1
            img 32320 vpunch
            w
            music stop
            sound plastinka1b
            img 32321 hpunch
            music Power_Bots_Loop
            m "Мерзавец!"
            mt "!!!"
            music Groove2_85
            imgd 32322
#            customer12 "Грубиянка!"
            customer12 "Грубиянки не получают чаевые! Аха-ха!"
            music Pyro_Flow
            imgf 14423
            sound highheels_short_walk
            mt "Сволочь! Он обманул меня!"
            mt "Он оставил меня без чаевых!"
            mt "Пусть в следующий раз сам себя обслуживает!"
            mt "Когда этот кошмар уже закончится?!"
            mt "?!?!?!"
#            $ pubQueenCustomer12Day = day
            pass
    stop music2
    return

label gallery_16964:
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
#    $ menu_price = [50]
    menu:
        "Согласиться.":
#            $ monicaShawarmaApartment3 = True # Моника посмотрела квартиру и согласилась ее арендовать (50 баксов)
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
            return
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
#    $ menu_price = [slumsApartmentsRentPrice]
    menu:
        "Согласиться.":
#            $ monicaShawarmaApartment4 = True # Моника согласилась арендовать квартиру за 300 баксов
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
            return
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
#    $ menu_price = [slumsApartmentsRentPrice]
    menu:
        "Заплатить $ 300 за апартаменты.":
#            $ monicaShawarmaApartment5 = True # Моника внесла первую оплату Джеку за квартиру
            pass
#    $ add_money(-slumsApartmentsRentPrice)
    # у Моники списываются с баланса деньги
    img 16983
    with fade
    shawarma "Джек счастлив помочь прекрасной Мадаме!"
    shawarma "Джек придти за деньгами в следующий суббота."
    img 16987
    with diss
    shawarma "Вот ключи от Ваш шикарный апартамент!"
    # ключи кладет куда-нибудь на стол и уходит
#    $ add_inventory("keys_apartments", 1, True)
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
    call textonblack(t_("Несколько минут спустя..."))
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
    return

label gallery_17028:
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
#    $ add_money(-slumsApartmentsRentPriceDiscount1)
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

label gallery_23627:
#    if act=="l":
#        return
#    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
#        mt "Я уже принимала душ недавно..."
#        return
    $ store_music()
    music stop
    img black_screen
    with diss
    pause 1.5
    music snd_shower2

    $ shower_images = ["23623", "23624", "23625", "23626", "23627", "23628", "23629", "23631", "23632", "23633"]
    $ images = random.sample(set(shower_images), 5)

    img images[0]
    with fade
    w
    img images[1]
    with diss
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Я вынуждена мыть свое прекрасное тело в этом жалком подобии душа!"
    if rnd == 2:
        mt "Какой идиот придумал сделать душ из куска ржавой трубы?!"
    if rnd == 3:
        mt "По крайней мере, здесь есть горячая вода..."
    img images[2]
    with diss
    w
    img images[3]
    with diss
    w
    img images[4]
    with diss
    w
#    $ cloth = "BathCloth1"
#    $ cloth_type = "HomeCloth"
#    $ monicaHomeBathroomMonicaSuffix = 2
#    $ autorun_to_object("ep211_dialogues6_slum_apartment_34_after_shower", scene="monicahome_bathroom")
#    $ monicaLastShowerDay = day
#    $ monicaLastShowerDayTime = day_time
    $ restore_music()
#    call refresh_scene_fade() from _rcall_refresh_scene_fade_25
    return

label gallery_19056:
    # Моника стоит у пилона, ситизен напротив нее
    fadeblack 2.0
    music Groove2_85
    imgfl 19038
    w
    imgf 13400
    citizen4 "Ну что, давай начнем."
    if citizen4BoobsShowedFirstTime == True:
        citizen4 "Я бы посмотрел на твои сиськи еще разок."
        #
        $ notif(_("Моника показывала обнаженную грудь за деньги."))
        #
        citizen4 "Но это будет скучно."

    # Моника зло на него смотрит
    imgd 13377
    m "Скучно?!"
    music Stealth_Groover
    imgd 13312
    mt "Вот мерзавец!"
    mt "Как он смеет говорить подобное обо МНЕ?!"
    mt "О такой шикарной женщине, как Я, мечтает любой мужчина!"
    music Groove2_85
    imgf 13373
    citizen4 "Ага. Скучно."
    citizen4 "Я тут подумал..."
    citizen4 "Я провернул небольшое дельце и у меня есть лишние 100 баксов."
    citizen4 "Я мог бы потратить их на тебя."
    citizen4 "Но тебе для этого придется постараться, детка."
    # Моника смотрит на него с подозрением
    imgd 13316
    mt "100 долларов?"
    mt "Хмм.. Было бы неплохо."
    mt "И что хочет этот мерзавец?"
    mt "Мне нужны деньги."
    imgd 13398
    m "И что ты предлагаешь?"
    imgf 13378
    citizen4 "Ты покажешь мне свои голые сиськи."
    citizen4 "И отсосешь у меня."
    music Pyro_Flow
    img 19039 hpunch
    m "Что?!"
    m "За кого ты меня принимаешь?!"
    m "?!?!?!"
    imgd 19040
    mt "Сволочь!"
    mt "Жалкий неудачник!"
    mt "Никчемный!!"
    music Groove2_85
    imgf 13401
    citizen4 "Девочка, ты забыла где ты? В этом районе каждая вторая готова таким образом заработать пару лишних долларов."
    citizen4 "Решайся быстрее, у меня нет времени. Ну дак что?"
    imgd 19041
    mt "Черт!"
    mt "..."
    menu:
        "Ты точно мне заплатишь $ 100?":
            pass
        "Хватит с тебя того, что ты уже видел! (прерывание квеста)":
            music Stealth_Groover
            imgf 13376
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            imgd 13424
            m "Хватит с тебя того, что ты уже видел!"
            return
    # Моника в замешательстве
    music Groove2_85
    imgf 13399
    m "Ты точно мне заплатишь $ 100?"
    imgd 19042
    citizen4 "Ага. Вот они." # показывает купюры
    citizen4 "Снимай свою майку и приступай."
    citizen4 "У меня яйца уже дымятся."
#    $ menu_corruption = [monicaSlumsFirstBlowjobCorruptionRequired, 0]
    menu:  # коррапшн! 600-?
        "Оголить грудь и сделать минет клиенту.":
#            $ monicaPerryMommyDebt1 = True # Моника дала согласие сделать минет ситизену в подворотне у пилона
            pass
        "Хватит с тебя того, что ты уже видел! (прерывание квеста)":
            music Stealth_Groover
            imgf 13376
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            imgd 13424
            m "Хватит с тебя того, что ты уже видел!"
            return
    music Groove2_85
    imgf 19043
    mt "Это звучит дико, но мне нужны деньги..."
    mt "Похоже, в этом районе все относятся совершенно нормально к таким вещам..."
    mt "А я нахожусь здесь анонимно..."
    mt "То что здесь происходит никак не связано с жизнью Моники Бакфетт."
    mt "Так что мне нечего стесняться."
    music Stealth_Groover
    imgd 19044
    mt "Мне это глубоко противно, но я отношусь к этому с хладнокровием."
    mt "В конце концов, это ненадолго."
    mt "Моя цель - это вернуть назад мою роскошную жизнь."
    mt "И я не остановлюсь ни перед чем!"
    # клиент расстегивает штаны и достает свой стояк
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 19045
    citizen4 "Ну? Чего стоишь?"
    citizen4 "Или тебе не нужны лишние 100 баксов?"
    citizen4 "Я не люблю долго ждать."
    imgf 19046
    mt "Черт! Черт! Черт!"
    mt "!!!"
    # Моника снимает майку
    sound snd_fabric1
    imgd 19047
    w
    imgf 19048
    w
    imgd 19049
    citizen4 "У тебя неплохие сиськи, детка."
    citizen4 "Осталось проверить, как хорошо ты работаешь ртом."
    citizen4 "Начинай уже!"
    # Моника опускается перед ним на колени, смотрит на член перед своим лицом
    fadeblack 2.0
    music Loved_Up
    imgfl 19050
    w
    imgf 19051
    mt "Моника, я не могу поверить, что ты будешь делать ЭТО!"
    mt "!!!"
    imgd 19052
    citizen4 "Ты собираешься отрабатывать свои 100 баксов?!"
    citizen4 "Мне уже надоело ждать!"
    citizen4 "Открывай свой рот!"
    # Моника зло смотрит на него исподлобья
    menu:
        "Открыть рот.":
            pass
    # открывает рот
    # ситизен хватает ее за голову и входит в ее рот
    imgf 19053
    citizen4 "Давай, соси!"
    imgd 19066
    w
    sound chpok6
    img 19054 vpunch
    citizen4 "Тебе, шлюха, не привыкать делать это за деньги!"
    menu:
        "Укусить его!!! (прерывание квеста)":
            music Pyro_Flow
            imgf 19056
            mt "Это я шлюха?!"
            mt "Мерзкий грязный слизняк!!!"
            # Моника зло смотрит на ситизена и сжимает челюсти на его члене
            sound hlup25
            imgd 19055
            m "!!!"
            # он загибается
            sound Jump1
            imgd 19057
            w
            sound vjuh2
            img 19058
            w
            sound scream_steve3
            img 19059 hpunch
            citizen4 "АААААА!!!"
            citizen4 "ААААААААААААА!!!"
            sound scream_steve3
            imgf 19060
            m "Я не шлюха!"
            m "Ублюдок!!!"
            m "!!!"
            sound scream_steve3
            imgd 19061
            citizen4 "СУКАААААА!!!"
            citizen4 "ААААААААААААА!!!"
            # Моника убегает
#            $ monicaPerryMommyDebt2 = True # Моника укусила ситизена и убежала
            return
        "Продолжить минет.":
            pass
    # Моника делает минет ситизену
    fadeblack 1.5
    music2 Loved_Up

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Prisoner1_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob1_1 = Movie(play="video/v_Monica_Citizen4_Blowjob1_1.mkv", fps=30)
    show videov_Monica_Citizen4_Blowjob1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19062
    citizen4 "Ааа..."
    imgd 19063
    citizen4 "Глубже давай!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Prisoner1_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob1_2 = Movie(play="video/v_Monica_Citizen4_Blowjob1_2.mkv", fps=30)
    show videov_Monica_Citizen4_Blowjob1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19065
    citizen4 "Вот тааак..."
    imgd 19064
    citizen4 "Ааааа..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Prisoner1_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Citizen4_Blowjob1_3 = Movie(play="video/v_Monica_Citizen4_Blowjob1_3.mkv", fps=30)
    show videov_Monica_Citizen4_Blowjob1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Над Моникой нависает Перри (внезапно)
    music2 stop
    music stop
    sound plastinka2
    img 19070 vpunch
    perry "Ах ты сучка!!!"
    # Моника отстраняется от клиента
    sound snd_bodyfall
    music Villainous_Treachery
    img 19071 hpunch
    w
    imgd 19072
    mt "Мое... Мое платье..."
    mt "Это Перри!!!"
    mt "О Боже!!! Нет!!!"
    mt "!!!"
    mt "!!!!!!"
    # Моника потрясенно смотрит на нее, клиент тем временем возмущается
    music Groove2_85
    imgf 19073
    citizen4 "Эй, детка!"
    citizen4 "Ты что, не видишь, чем эта шлюха занимается?"
    citizen4 "Или ты хочешь присоединиться к ней?"
    # Перри орет на него
    music Power_Bots_Loop
    img 19074 vpunch
    perry "Заткнись!"
    perry "Я эту сучку везде ищу!"
    perry "А она тут развлекается с мужиками!"
    music Groove2_85
    imgd 19075
    citizen4 "Эй, полегче!"
    citizen4 "Сейчас она закончит начатое дело и разбирайся с ней."
    citizen4 "Кстати, эта шлюха тут уже давно работает."
    imgd 19076
    perry "Ах ты, дрянь!"
    perry "Я так и думала, что ты проститутка!!!"
    # Перри достает телефон и делает фото
    imgf 19077
#    sound snd_photo_capture
    call photoshop_flash()
    w
    music Power_Bots_Loop
    imgd 19078
    mt "Она меня сфотографировала!!!"
    mt "!!!"
    mt "!!!!!!"
    music Groove2_85
    imgf 19079
    perry "Теперь ты от меня никуда не денешься!"
    perry "По этому фото мои ребята тебя быстро найдут!"
    perry "Когда ты мне отдашь МОИ деньги?!"
    # у Моники шок
    music Power_Bots_Loop
    imgd 19080
    mt "Что мне делать?!"
    mt "?!?!!?!?!!"
    mt "Я ей должна $ 10 000!!!"
    mt "И еще она угрожала мне бандитами!!!"
    mt "ЧТО ДЕЛАТЬ?!?!?!!?"
#    $ monicaPerryMommyDebt3 = True # у Перри есть фото, где Моника стоит на коленях перед ситизеном
    menu:
        "МОНИКА, БЕГИ!!! (прерывание квеста)":
            # Моника толкает ситизена, тот падает
            # возможно, задевает Перри и та тоже падает
            music Turbo_Tornado
            imgf 19081
            sound anger2
            w
            sound snd_bodyfall
            img 19082 vpunch
            w
            sound highheels_run2
            imgd 19083
            citizen4 "Твою мать!!!"
            citizen4 "Да ты охренела?!"
            imgd 19084
            perry "Держи ее! Держи!"
            perry "Она воровка!!!"
            # Моника убегает
#            $ monicaPerryMommyDebt4 = True # Моника сбежала от Перри
#            $ questHelp("work_slums_46", False)
            return
        "Попробовать договориться с Перри.":
            pass
    music Pyro_Flow
    imgf 19085
    mt "Дьявол!"
    mt "Не могу же я постоянно скрываться от этой извращенки!"
    mt "И вообще!"
    mt "С чего я должна отдавать ей $ 10 000?!"
    mt "За одну ночь!"
    imgd 19086
    mt "В какой-то занюханной грязной дыре!"
    mt "!!!"
    mt "Эта дрянь напялила МОЕ платье!"
    mt "Весь ее гребаный хостел не стоит той цены, за которую я покупала это платье!"
    # Моника встает и отходит от ситизена, смотрит на Перри
    music Groove2_85
    imgf 19087
    citizen4 "Эй!" # возмущенно
    citizen4 "Ты куда?!"
    citizen4 "Я тебе не заплачу ни цента, пока ты не закончишь!"
    citizen4 "Тебе что, 100 баксов не нужны?"
    music Power_Bots_Loop
    imgd 19088
    m "Хватит с тебя того, что я уже сделала!"
    # Перри орет возмущенно
    imgd 19089
    perry "100 баксов?!"
    perry "Эта проститутка сосет за 100 баксов?!"
    perry "И не отдает мне МОИ деньги!!!"
    # ситизен застегивает штаны
    music Groove2_85
    imgf 19090
    citizen4 "Да пошла ты, шлюха!"
    citizen4 "Даже отсосать нормально не можешь!"
    citizen4 "Пойду найду себе детку, которая за 100 баксов сделает все, что я захочу."
    sound man_steps
    imgd 19091
    w
    return

label gallery_19155:
#    if ep214_slums_monica_perry_talk_count == 0:
    # Моника заходит в хостел, Перри у столика, который служит ресепшном
    fadeblack 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19133
    mt "Не могу поверить, что я снова оказалась здесь!"
    mt "Какой кошмар!"
    # подходит к Перри
    sound highheels_short_walk
    imgf 19134
    perry "А, воровка пришла!"
    m "Я не воровка!"
    m "Не называй меня так!"
    imgd 19135
    perry "Я называю вещи своими именами!"
    perry "Ты должна мне 50 00 баксов и не отдаешь их!"
    perry "Значит, ты воровка!"
    music Power_Bots_Loop
    img 19136
    mt "Тварь!"
    mt "!!!"
    music Groove2_85
    imgf 19137
    m "Откуда такая сумма?!"
    m "Я переночевала в этой дыре всего один раз!"
    m "И договаривались мы с тобой всего на $ 10 000!"
    imgd 19138
    perry "Будешь спорить со мной, воровка, твой долг станет 100 000 баксов!"
    perry "Я тебя искала, потратила на это немало времени, а ты скрывалась от меня!"
    #
    $ notif(_("Моника согласилась сделать минет незнакомцу возле пилона."))
    #
    imgd 19138
    perry "При этом работала, отсасывая у прохожих!"
    perry "Короче, я поставила тебя на счетчик. Поэтому теперь ты мне должна 50 000 баксов."
    music Power_Bots_Loop
    imgf 19139
    mt "Мерзкая тупая стерва!"
    mt "Ненавижу ее!"
    mt "!!!"
    music Groove2_85
    imgd 19140
    perry "Ну так что?"
    perry "Ты принесла мне мои 50 000 баксов?"
#    else:
    #### отсюда можно сделать регулярный разговор, когда Моника приходит к Перри
    #### + возможность скипнуть это
#        fadeblack 1.5
#        sound highheels_short_walk
#        pause 2.0
#        music Groove2_85
#        imgfl 19140
#        perry "Ты принесла мне остаток долга?"
#        perry "$ [ep214_perry_debt]"
        #

#    $ ep214_slums_monica_perry_talk_count += 1
#    if money < ep214_perry_debt:
    # если денег недостаточно
    imgf 19141
    m "Я сейчас не располагаю такой суммой!"
    imgd 19142
    perry "Либо ты отдаешь мне деньги. Столько, сколько можешь сейчас отдать."
    sound highheels_short_walk
    imgf 19176
    w
    imgd 19177
    perry "Либо отрабатывай!" # раздвигает ноги и задирает юбку
    #
    sound Jump1
    imgd 19143
    mt "!!!"
    imgf 19144
    w
#    $ menu_price = [20,0]
#    $ menu_corruption = [0, 0, monicaPerryLickingCorruption]
    menu:
        "Отдать Перри часть долга.":
            # Моника смотрит на раздвинувшую ноги Перри с отвращением
            music Pyro_Flow
            imgd 19145
            mt "Отрабатывать?!"
            mt "?!?!?!"
            mt "Нет! Ни за что!"
            mt "Лучше я отдам ей часть моих денег!"
            music Groove2_85
            imgf 19146
            m "Перри, я могу тебе отдать сейчас $ 20."
            perry "Всего 20 баксов?"
            m "Да."
            perry "Ладно, давай."
            fadeblack 1.5
#            sound fx_coins_b3
#            $ add_money(-20.0)
#            $ ep214_perry_debt -= 20.0
#            $ notif(t__("Моника должна Перри" + " $" + str(ep214_perry_debt)))
#            $ ep214_slums_monica_paid_money_this_week = True
            pause 2.0
            music Groove2_85
            # Моника отдает ей деньги
#            $ monicaPerryMommyDebt6 = True # Моника заплатила Перри часть долга
            imgfl 19147
            perry "Жду тебя {c}через неделю!{/c}"
            perry "Если не придешь, то твой долг увеличится на 1 000 баксов!"
            perry "Поняла меня, воровка?"
            imgf 19148
            mt "Черт!"
            m "Да!"
            # Перри садится на стол, обнажая киску
            imgd 19149
            perry "Может, ты все-таки хочешь полизать мою волосатую киску"
            perry "Я засчитаю за это еще $ 10..."
            perry "И разрешу остаться на одну ночь в моем хостеле. Бесплатно."
            # Моника смотрит с ужасом на киску
            imgf 19150
            m "..."
#            $ menu_corruption = [monicaPerryLickingCorruption]
            menu:
                "Отработать.":
                    # Моника в сомнениях
                    music Pyro_Flow
                    imgd 19145
                    mt "Фууу!!!"
                    mt "Как она может предлагать мне подобную гадость?!"
                    mt "?!"
                    music Groove2_85
                    mt "С другой стороны..."
                    imgf 19151
                    mt "Одна ночь в хостеле бесплатно..."
                    mt "И плюс $ 10 к оплате долга..."
                    mt "Моника, неужели ты способна согласиться на такое?!"
                    mt "Но ведь об этом никто не узнает."
                    mt "Зато сумма долга станет меньше и я смогу провести ночь здесь."
                    mt "Черт!"
                    # Перри снова показывает свою киску
                    imgd 19152
                    perry "Ну? Ты надумала?"
                    perry "Давай!"
                    perry "Моя киска уже вся влажная."
                    perry "Иди сюда."
                    m "..."
                    # Моника нерешительно подходит к ней
                    music Stealth_Groover
                    imgf 19153
                    mt "Я это делаю для того, чтобы быстрее расплатиться с этой сучкой."
                    mt "Я хочу поскорее решить этот вопрос и забыть об этом."
                    mt "Когда я верну себе свою власть и деньги, я накажу эту стерву!"
                    imgd 19154
                    mt "Она не только вернет мне все деньги!"
                    mt "Она заплатит значительно более высокую сумму!"
                    mt "За все мои моральные страдания!"
                    # Моника опускается перед Перри на колени и смотирт на ее волосатую киску
                    fadeblack 1.5
                    music Groove2_85
                    imgfl 19157
                    w
                    imgf 19155
                    mt "Как я буду делать ЭТО?"
                    mt "Фу!!!"
                    mt "Меня сейчас стошнит!"
                    imgd 19156
                    perry "Тебе стоило с самого начала согласиться полизать мне киску!"
                    perry "Тогда бы у тебя не было таких долгов! Ха-ха!"
                    perry "Давай скорее!"
                    perry "Мне не терпится почувствовать твой язычок!"
                    mt "!!!"
                    fadeblack 1.0
                    # ликинг
                    music2 Loved_Up
                    imgf 19158
                    w

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_1 = Movie(play="video/v_Monica_Perry_Licking1_1.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_1
                    with fade
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgd 19159
                    perry "ООООО!"
                    perry "Это чертовски охренительно, детка!"

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_2 = Movie(play="video/v_Monica_Perry_Licking1_2.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_2
                    with fade
                    perry "Но я даже рада что ты такая воровка!"
                    perry "Теперь моя киска будет вылизана на годы вперед! Ха-ха!"
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    imgf 19160
                    perry "О даааа!!!"
                    perry "Давай быстрее работай язычком!"
                    imgd 19161
                    w
                    sound lick3
                    imgd 19162
                    mt "Я не могу поверить..."
                    mt "Я - Моника Бакфетт, самая богатая и влиятельная Леди этого города..."

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_3 = Movie(play="video/v_Monica_Perry_Licking1_3.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_3
                    with fade
                    mt "Лижу жуткую волосатую промежность хозяйке какого-то занюханного хостела в трущобах..."
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    sound lick3
                    imgd 19161
                    w
                    sound lick3
                    imgd 19162
                    w
                    sound lick3
                    imgd 19161
                    w
                    sound lick3

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_4 = Movie(play="video/v_Monica_Perry_Licking1_4.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_4
                    with fade
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    music2 stop
                    fadeblack 1.0
                    music2 Loved_Up2
                    imgd 19162
                    perry "Еще быстрее!!"
                    sound lick3
                    imgd 19161
                    w
                    sound lick3
                    imgd 19162
                    w
                    imgf 19163
                    perry "Я скоро кончу!!"

                    img black_screen
                    with diss
                    stop music
                    $ renpy.music.set_volume(0.5, 0.5, channel="music")
                    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
                    play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
                    scene black
                    image videov_Monica_Perry_Licking1_5 = Movie(play="video/v_Monica_Perry_Licking1_5.mkv", fps=30)
                    show videov_Monica_Perry_Licking1_5
                    with fade
                    wclean
                    stop music
                    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
                    $ renpy.music.set_volume(1.0, 0.5, channel="music")

                    # кончает
                    img 19164
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    perry "ТВОЮ МААААТЬ! ДАААА!"
                    img 19165
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound snd_melanie_cum2
                    perry "ООООО!!!"
                    perry "АААААААААА!!!"
                    # затемнение
                    # Моника с отвращением вытирает рот, Перри сидит довольная
#                    $ monicaPerryMommyDebt8 = True # Моника сделала ликинг Перри
                    music2 stop
                    fadeblack 1.5
                    music Power_Bots_Loop
                    imgfl 19166
# Monica_Citizen1,2 - 1
                    mt "Это было отвратительно!!!"
                    mt "!!!"
                    mt "Меня тошнит от нее!!!"
                    music Groove2_85
                    imgf 19167
                    perry "Мне кажется, тебе понравилось, детка."
                    m "Нет!"
                    imgd 19168
                    perry "Ха! Зато мне понравилось!"
#            $ add_money(-20.0)
#                    $ ep214_perry_debt -= 10.0
#                    $ notif(t__("Моника должна Перри" + " $" + str(ep214_perry_debt)))
                    perry "Я засчитываю 10 баксов в счет оплаты долга."
                    perry "И можешь остаться сегодня на ночь в номере."
                    perry "Можешь лизать мою киску хоть каждый день и ночевать здесь, я не против."
                    imgd 19148
                    m "Иди ты в жопу, Перри!!!"
                    m "!!!"
#                    if ep214_slums_monnica_licked_perry_first_day == 0:
#                        $ ep214_slums_monnica_licked_perry_first_day = day
#                    $ ep214_slums_monnica_licked_perry_last_day = day
#                    $ ep214_slums_monica_rent_hostel_last_day = day
#                    $ ep214_slums_monica_paid_money_this_week = True
                    menu:
                        "Идти в номер хостела.":
                            music Groove2_85
                            imgf 19169
                            m "Куда тут идти, чтобы поспать?!"
                            perry "Иди по коридору, детка!"
                            perry "А я посмотрю, как ты виляешь своей аппетитной попкой!"
                            perry "Аха-ха!"
                            music Power_Bots_Loop
                            imgd 19170
                            mt "!!!!!!!"
                            m "!!!"
                            # Моника уходит в номер
                            return
                        "Уйти отсюда!":
                            music Power_Bots_Loop
                            imgf 19136
                            mt "Я не хочу оставаться в этой вонючей дыре!"
                            mt "!!!"
                            #
                            return
                    return
                "Нет! Ни за что!":
                    music Pyro_Flow
                    imgd 19154
                    m "Нет! Я не буду делать этого!"
                    m "Достаточно того, что я отдала тебе часть долга!"
                    music Groove2_85
                    imgf 19149
                    perry "Если захочешь остаться в номере хостела на ночь..."
                    perry "Ты знаешь, что нужно сделать."
                    m "Да пошла ты!"
                    # уходит
                    return
        "Отдать Перри остаток долга (в будущем обновлении) (disabled)":
            pass
        "Отработать.":
            # отработка
            # Моника в сомнениях
            music Pyro_Flow
            imgd 19145
            mt "Фууу!!!"
            mt "Как она может предлагать мне подобную гадость?!"
            mt "?!"
            music Groove2_85
            mt "С другой стороны..."
            imgf 19151
            mt "Одна ночь в хостеле бесплатно..."
            mt "И плюс $ 10 к оплате долга..."
            mt "Моника, неужели ты способна согласиться на такое?!"
            mt "Но ведь об этом никто не узнает."
            mt "Зато сумма долга станет меньше и я смогу провести ночь здесь."
            mt "Черт!"
            # Перри снова показывает свою киску
            imgd 19152
            perry "Ну? Ты надумала?"
            perry "Давай!"
            perry "Моя киска уже вся влажная."
            perry "Иди сюда."
            m "..."
            # Моника нерешительно подходит к ней
            music Stealth_Groover
            imgf 19153
            mt "Я это делаю для того, чтобы быстрее расплатиться с этой сучкой."
            mt "Я хочу поскорее решить этот вопрос и забыть об этом."
            mt "Когда я верну себе свою власть и деньги, я накажу эту стерву!"
            imgd 19154
            mt "Она не только вернет мне все деньги!"
            mt "Она заплатит значительно более высокую сумму!"
            mt "За все мои моральные страдания!"
            # Моника опускается перед Перри на колени и смотирт на ее волосатую киску
            fadeblack 1.5
            music Groove2_85
            imgfl 19157
            mt "Мое платье... Как я скучаю по нему..."
            perry "Тебе стоило с самого начала согласиться полизать мне киску!"
            perry "Тогда бы у тебя не было таких долгов! Ха-ха!"
            imgf 19155
            mt "Как я буду делать ЭТО?"
            mt "Фу!!!"
            mt "Меня сейчас стошнит!"
            imgd 19156
            perry "Но я даже рада что ты такая воровка!"
            perry "Теперь моя киска будет вылизана на годы вперед! Ха-ха!"
            perry "Давай скорее!"
            perry "Мне не терпится почувствовать твой язычок!"
            mt "!!!"
            # ликинг
            fadeblack 1.0
            music2 Loved_Up
            imgf 19158
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_1 = Movie(play="video/v_Monica_Perry_Licking1_1.mkv", fps=30)
            show videov_Monica_Perry_Licking1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 19159
            perry "ООООО!"
            perry "Это чертовски охренительно, детка!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_2 = Movie(play="video/v_Monica_Perry_Licking1_2.mkv", fps=30)
            show videov_Monica_Perry_Licking1_2
            with fade
            perry "Но я даже рада что ты такая воровка!"
            perry "Теперь моя киска будет вылизана на годы вперед! Ха-ха!"
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 19160
            perry "О даааа!!!"
            perry "Давай быстрее работай язычком!"
            imgd 19161
            w
            sound lick3
            imgd 19162
            mt "Я не могу поверить..."
            mt "Я - Моника Бакфетт, самая богатая и влиятельная Леди этого города..."

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_3 = Movie(play="video/v_Monica_Perry_Licking1_3.mkv", fps=30)
            show videov_Monica_Perry_Licking1_3
            with fade
            mt "Лижу жуткую волосатую промежность хозяйке какого-то занюханного хостела в трущобах..."
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            sound lick3
            imgd 19161
            w
            sound lick3
            imgd 19162
            w
            sound lick3
            imgd 19161
            w
            sound lick3

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_4 = Movie(play="video/v_Monica_Perry_Licking1_4.mkv", fps=30)
            show videov_Monica_Perry_Licking1_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.0
            music2 Loved_Up2
            imgd 19162
            perry "Еще быстрее!!"
            sound lick3
            imgd 19161
            w
            sound lick3
            imgd 19162
            w
            imgf 19163
            perry "Я скоро кончу!!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.333333333) + " loop 0.0>Sounds/v_Monica_Perry_Licking1.ogg"
            scene black
            image videov_Monica_Perry_Licking1_5 = Movie(play="video/v_Monica_Perry_Licking1_5.mkv", fps=30)
            show videov_Monica_Perry_Licking1_5
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # кончает
            img 19164
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            perry "ТВОЮ МААААТЬ! ДАААА!"
            img 19165
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound snd_melanie_cum2
            perry "ООООО!!!"
            perry "АААААААААА!!!"
            # затемнение
            # Моника с отвращением вытирает рот, Перри сидит довольная
#            $ monicaPerryMommyDebt8 = True # Моника сделала ликинг Перри
            music2 stop
            fadeblack 1.5
            music Power_Bots_Loop
            imgfl 19166
            mt "Это было отвратительно!!!"
            mt "!!!"
            mt "Меня тошнит от нее!!!"
            music Groove2_85
            imgf 19167
            perry "Мне кажется, тебе понравилось, детка."
            m "Нет!"
            imgd 19168
            perry "Ха! Зато мне понравилось!"
#            $ notif(t__("Моника должна Перри" + " $" + str(ep214_perry_debt)))
#            $ ep214_perry_debt -= 10.0
            perry "Я засчитываю 10 баксов в счет оплаты долга."
            perry "И можешь остаться сегодня на ночь в номере."
            perry "Можешь лизать мою киску хоть каждый день и ночевать здесь, я не против."
            imgd 19148
            m "Иди ты в жопу, Перри!!!"
            m "!!!"
#            if ep214_slums_monnica_licked_perry_first_day == 0:
#                $ ep214_slums_monnica_licked_perry_first_day = day
#            $ ep214_slums_monnica_licked_perry_last_day = day
#            $ ep214_slums_monica_rent_hostel_last_day = day
#            $ ep214_slums_monica_paid_money_this_week = True
            return
            pass
        "Уйти!":
            # Моника зло
            music Pyro_Flow
            imgd 19154
            mt "Я не собираюсь отдавать ей деньги, которые я заработала с таким трудом!"
            music Groove2_85
            imgf 19137
            m "У меня нет денег!"
            imgd 19142
            perry "Тогда отрабатывай!" # показывает на свою киску
            fadeblack
            sound highheels_short_walk
            pause 2.0
            music Groove2_85
            imgfl 19143
            w
            imgf 19144
            w
            imgd 19145
            w
            music Power_Bots_Loop
            imgd 19171
            m "Нет!"
            m "Я ни за что не буду делать этого!"
            imgf 19172
            perry "Тогда твой долг вырастет на 1 000 баксов!"
            imgd 19173
            m "Пошла ты в жопу, Перри!"
            imgd 19136
            mt "Гребаная извращенка!"
#            $ monicaPerryMommyDebt5 = True # Моника отказалась давать деньги или отрабатывать у Перри
            # Моника уходит
            return
    return

label gallery_24340:
    # Моника заходит в душевую
#    mt "А вот и душ."
    music snd_shower2
    if day_time == "day":
        imgf 24339
    else:
        imgf 24341
    mt "Душ...."
    mt "Как же хорошо..."
    mt "Мммм..."
    if day_time == "day":
        imgd 24340
    else:
        imgd 24342
    mt "Боже, я сейчас вспомнила, как я тогда напугалась в душе!"
    mt "Эти голые мужчины! Сколько их было? Целая толпа!"
    mt "Страшно представить, что бы они со мной сделали!"
    mt "!!!"
    mt "Моника, тебе нужно быть осторожной, когда ты остаешься здесь!"
    return

label gallery_31730:
    # Моника стоит посреди своей комнаты, панки оглядываются
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 31692
    w
    imgf 31693
    citizen1 "Эй, теть!"
    citizen1 "Ты эту хату снимаешь, чтоб работать тут?"
    m "Нет!!"
    m "!!!"
    imgd 31694
    citizen2 "Не, Том. Ты дебил?"
    citizen2 "Она работает, показывая сиськи у пилона за 2 бакса."
    citizen2 "А эту хату ей дал ее сутенер, чтоб она сюда водила важных клиентов, таких как мы."
    citizen2 "Так что это не ее хата. Здесь раньше работала какая-то другая шлюха."
    citizen1 "Ты откуда знаешь?"
    citizen2 "Мне братан рассказывал про хату, где он трахал ту шлюху."
    citizen2 "Сказал, что прям на обоях написано 'Fuck', а на стене рыба висит."
    citizen1 "Рыба?!"
    citizen2 "Ага, смотри, Том!"
    # Том оглядывается и смотрит на рыбу
    imgf 31695
    citizen1 "Аха-ха-ха!!!"
    sound male_laugh4
    citizen1 "Что это за хрень?!"
    citizen2 "Ха-ха-ха!"
    imgd 31696
    m "Ничего смешного!"
    citizen1 "Аха-ха-ха!!!"
    sound male_laugh2a
    citizen1 "Тим, дай свою бутылку из-под пива!"
    citizen1 "Спорим, попаду в эту рыбу отсюда?"
    music Power_Bots_Loop
    m "Не смей делать этого!"
    m "Я откажусь с вами работать!"
    m "!!!"
    music Groove2_85
    citizen2 "Тихо, чувак. Слышишь, что она говорит?"
    citizen2 "Не переживай, теть. Я бутылку еще по дороге выкинул."
    citizen2 "В следующий раз покидаем, Том."
    music Turbo_Tornado
    imgf 31697
    citizen2 "Лучше смотри, какая тут кровать! Ха-ха!"
    citizen2 "Сколько тут мужиков у тебя было, теть?"
    citizen2 "50 было? Или больше?"
    citizen2 "Сейчас 51 будет!"
    # запрыгивает на кровать в обуви, начинает прыгать на ней
    sound Jump1
    img 31698 vpunch
    w
    sound Jump1
    img 31699 vpunch
    citizen2 "Дааа!"
    citizen2 "Аха-ха-ха!!!"
#    music Power_Bots_Loop
    imgd 31700
    m "ТЫ ЧТО ДЕЛАЕШЬ?!"
    m "КРЕТИН!!!"
    m "!!!"
    m "Быстро слезь с моей кровати!!!"
    m "!!!"
    # с кровати прыгает в сторону кресла, через столик
    # опрокидывает кресло и сам падает
    sound Jump1
    img 31701
    w
    sound snd_bodyfall
    sound2 snd_heavy_papers_drop
    img 31702 vpunch
    citizen2 "Ха-ха-ха!!!"
    citizen1 "Аха-ха-ха!!!"
    sound male_laugh2a
    citizen1 "Вот ты дебил, Тим!!! Ха-ха-ха!!!"
#    sound male_laugh4
    citizen1 "Теть, а прикольно тут у тебя! Ха-ха!"
    # Тим поугарал и встает с пола
    imgf 31703
    citizen1 "Да! Мы теперь твои постоянные клиенты и будем почаще приходить к тебе!"
    music Power_Bots_Loop
    m "Вы мне тут сейчас все сломаете, идиоты!"
    m "Мне не нужны такие постоянные клиенты!"
    m "!!!"
    m "!!!!!!"
    music Groove2_85
    imgd 31704
    sound snd_cardboard2
    citizen2 "Слышь, Том, если мы что-то сломаем, сутенер накажет нашу тетю."
    citizen2 "Давай, не будем ее подставлять?"
    imgf 31703
    citizen1 "А я бы сломал, Тим. А потом посмотрел, как он ее наказывает."
    citizen2 "Аха-ха-ха!!!"
#    sound male_laugh2a
    citizen1 "Как он это делает, теть, а?"
    citizen1 "Раскладывает тебя прямо на этой кровати, да? Ха-ха!"
    music Power_Bots_Loop
    m "У меня нет никакого сутенера!"
    imgd 31705
    mt "Боже!"
    mt "Зачем я только связалась с этими тупыми придурками?!"
    mt "!!!"
    music Groove2_85
    imgf 31706
    citizen1 "Ладно, ладно."
    citizen1 "Все. Я себя буду вести хорошо."
    citizen1 "Мы же сюда пришли не за этим."
    citizen1 "Давай начнем, теть?"
    music Turbo_Tornado
    imgd 31707
    citizen2 "Подожди! Я сначала отлить хочу."
    citizen1 "Эй! Я тоже!"
    imgd 31708
    citizen1 "Давай, ты пойдешь отольешь в туалете, а я - на кухню в раковину."
    citizen2 "Не, давай я тогда здесь в окно!"
    citizen2 "Давай бросим жребий, кто куда!"
    # бросают жребий камень-ножницы-бумага
    imgf 31709
    citizen1 "Камень, ножницы, бумага..."
    # Моника прерывает их, ее бомбит
    music Power_Bots_Loop
    img 31710 hpunch
    m "ВЫ ОХРЕНЕЛИ?!"
    m "Только попробуй пойти на кухню или к окну!"
    m "По очереди сходите в туалет, недоумки!!!"
    m "!!!"
    music Groove2_85
    imgd 31711
    citizen2 "Да ладно тебе, теть!"
    citizen2 "Не твоя же хата!"
    # Моника орет
    music Power_Bots_Loop
    imgf 31712
    m "Кретины!!!"
    mt "ААААА!!!"
    mt "Бесят!!!"
    imgd 31713
    mt "!!!"
    # citizen2 бежит к окну, citizen1 выбегает из комнаты
    music Turbo_Tornado
    imgd 31714
    sound gretta_jone_run
    citizen2 "Аха-ха-ха!!!"
    sound male_laugh2a
    citizen1 "Аха-ха!!!"
    mt "ТВОЮ МААААТЬ!"
    img 31715
    m "Эй, ты куда?!"
#    fadeblack 1.5
    imgf black_screen
    sound highheels_run2
    pause 2.0
    music Turbo_Tornado
#    music Pyro_Flow
    # Моника бежит за тем, кто пошел отливать в раковину на кухне
    # кухня
    # забегает на кухню, тот стоит и расстегивает ширинку
    imgf 31717
    w
    sound anger2
    imgd 31718
    m "!!!"
    m "Пошел отсюда на хрен!!!"
    # толкает его от раковины
    citizen1 "Ай!"
    citizen1 "Больно же!"
    # Моника размахивается и лупит еще раз
    sound snd_punch_face1
    img 31719 hpunch
    citizen1 "АЙ!!!"
    citizen2 "Все-все!"
    citizen2 "Теть! Ай!"
    citizen1 "Я же пошутил! Ты чего сразу дерешься?!"
    # убегает от нее в комнату
    imgf 31716
    sound run2
    w
    music Pyro_Flow
    imgd 31720
    mt "Бесполезные!"
    mt "Никчемные!"
    mt "Отбросы общества!"
    mt "Ненавижу!!!"
    mt "!!!"
    # Моника выходит из кухни
    # комната
    # в комнате стоят оба панка
    fadeblack
    sound highheels_run2
    pause 2.0
    music Power_Bots_Loop
    imgfl 31722
    w
    imgf 31721
    m "Да, это не моя квартира! Это квартира сутенера!!!"
    m "Еще что-нибудь сделате и я позвоню ему, чтоб он вас отсюда вышвырнул!!!"
    m "И учтите, он заберет все ваши деньги за мое время, потраченное на вас!"
    music Groove2_85
    # панки слушаются
    citizen2 "Все-все-все!"
    citizen2 "Не надо никому звонить, теть."
    citizen1 "Мы так больше не будем!"
    citizen1 "Мы просто пошутили!"
    # Моника возвращается в комнату и про себя злится
    music Power_Bots_Loop
    imgd 31723
    mt "Чертовы идиоты!"
    mt "Гребаные кретины!"
    mt "ААААА!!!"
    mt "!!!"
    mt "Так, Моника!"
    mt "Успокойся!"
    music Stealth_Groover
    imgd 31724
    mt "Этой грязной дыре хуже уже не будет."
    mt "А тебе нужно возвращать назад свою прошлую жизнь!"
    mt "А для этого нужны деньги!"
    mt "Поэтому твоя цель - заработать их!"
    mt "!!!"
    # Тим и Том смотрят на нее
    music Groove2_85
    imgf 31725
    citizen2 "Теть?"
    citizen1 "Мы готовы."
    citizen1 "Начнем?"
    music Power_Bots_Loop
    imgd 31726
    m "Нет!" # зло
    m "За то, что вы здесь устроили, я не буду работать с вами за 15 баксов!"
    m "!!!"
    music Groove2_85
    citizen1 "Мы заплатим тебе больше, теть."
    citizen2 "Да, я купил пива, но у меня еще остались деньги."
    imgd 31727
    citizen1 "Сколько там у тебя осталось?"
    citizen2 "Я могу еще 5 баксов добавить."
    citizen2 "Что насчет 20 баксов, теть?"
    menu:
        "Деньги вперед!":
            pass
        "Прогнать придурков!!!":
            music Pyro_Flow
            imgf 31723
            mt "Нет!"
            mt "Я не собираюсь терпеть этих кретинов ни за какие деньги!"
            imgd 31805
            m "Пошли вон отсюда, придурки!!!"
            citizen1 "Да ладно тебе, теть!"
            citizen2 "Что мы такого сделали?!"
            music Power_Bots_Loop
            m "ВОН ОТСЮДА!" # орет на них
            m "БЫСТРО!!!"
            m "!!!"
#            $ monicaCitizensPunksBlowjob4 = True # Моника прогнала Тома и Тима из своей квартиры
            return
    music Stealth_Groover
    imgf 31723
    mt "Я не верю этим придуркам!"
    mt "Что, если они меня обманут?"
    imgd 31725
    m "Я сделаю, что вы хотите, но при условии, что сначала вы отдадите мне деньги!"
    music Groove2_85
    citizen1 "Нее, теть!"
    citizen2 "За дураков нас принимаешь?"
    citizen1 "Давай, половину сейчас, а половину после работы!"
    citizen2 "Да! По-другому никак, теть!"
    m "10 долларов сейчас, 10 долларов после работы."
    sound vjuh3
    imgf 31728
    citizen1 "Ага!"
#    $ add_money(10.0)
    citizen2 "Держи 10 баксов."
    citizen2 "Том, я первый!"
    # расстегивает штаны и достает член
    fadeblack
    sound snd_zip
    pause 1.5
    music Groove2_85
    imgfl 31729
    citizen2 "Только теть, раз 20 баксов, то ты работаешь не рукой, а ртом!"
    m "Еще чего!"
    m "Я не собираюсь делать минет и тебе, и ему за $ 20!"
    citizen1 "Тогда Тиму минет, а для меня поработаешь рукой, теть."
    citizen2 "Давай уже начнем, а?"
    sound snd_zip
    imgf 31730
    citizen2 "Смотри, как он хочет к тебе в рот!"
    # указывает на свой стояк
    # второй панк тоже достает свой член
#    citizen1 "А мой стояк хочет, чтобы ты его потрогала рукой!"
    # Моника зло смотрит на них
    music Stealth_Groover
    imgd 31723
    mt "Черт!"
#    mt "Из этих 20 долларов мне половину придется отдать старой карге!"
#    mt "Мне останется всего 10!"
    mt "Терпеть такое из-за $ 20?!"
    mt "!!!"
    imgd 31724
    mt "Но это лучше, чем вообще ничего..."
    mt "На эти деньги можно купить целых 10 кебабов..."
    mt "..."
    music Turbo_Tornado
    imgf 31731
    citizen1 "Эй! Я тоже хочу, чтобы она отсосала мне!"
    citizen2 "Нет мне!"
    citizen1 "Это в прошлый раз покупал пиво!"
    citizen2 "А я покупал вкусную рыбу! Ха-ха!"
    citizen1 "Ладно, пусть тетя сама решает кому из нас сосать, а кому дрочить!"
    citizen1 "Все-равно она выберет меня!"
    citizen2 "Ха-ха! Вот увидишь, она выберет сосать у меня!"
    label gallery_31794:
    music Groove2_85
    imgd 31732
    mt "Какие же эти кретины мерзкие! Фу!"
    mt "Скорее бы уже их отсюда прогнать!"
#    $ monicaCitizensPunksBlowjob2 = False
#    $ monicaCitizensPunksBlowjob3 = False
    menu:
        "Встать на колени и взять в рот член Тима.":
            # Моника встает на колени перед Тимом
            label gallery_31739:
            fadeblack
            sound snd_fabric1
            pause 1.5
            sound highheels_short_walk
            pause 2.0
            music Loved_Up
            imgfl 31733
            w
            imgf 31734
            citizen2 "О, даа!"
            citizen2 "Теперь возьми его в рот."
            ## тут Моника может и посопротивляться!!
            imgd 31735
            mt "Гребаные придурки!"
            mt "!!!"
            mt "Черт! Моника!"
            mt "Никогда бы не подумала, что ты окажешься в такой ситуации!"
            mt "!!!"
            # Моника выполняет
            # Моника делает минет Тиму
            # Том стоит сбоку от них и дрочит
            fadeblack 1.5
            music2 Loved_Up
            sound chpok6
            img 31736 vpunch
            w
            imgd 31737
            citizen1 "Эй, теть!"
            citizen1 "А я?!"
            citizen1 "Давай дрочи мне!"
            menu:
                "Взять член Тома в руку.":
                    pass
            # Моника берет его в руку и начинает водить туда-сюда

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob1_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob1_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob1_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31738
            citizen1 "Тееееть, круто!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob1_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob1_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob1_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31739
            citizen2 "Дааа!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob1_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob1_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob1_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.0
            music Groove2_85
            imgf 31740
            citizen2 "Покажи свои сиськи!"
            citizen2 "Снимай майку!"
            citizen2 "Я доплачу еще 1 бакс!"
            citizen1 "Давай, снимай!"
            citizen1 "Заработаешь 21 бакс!"
            imgd 31741
            mt "Черт!"
            mt "!!!"
            menu:
                "Снять одежду.":
                    pass
            # Моника снимает майку
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Loved_Up
            imgfl 31742
            w
            imgf 31743
            citizen2 "Да!!!"
            citizen2 "Прикольные сиськи!!!"
            imgd 31744
            citizen1 "Давай работай дальше!"
            # Моника берет член в рот, а второго держит за член рукой
            # минет и хэнджоб двоим одновременно
            fadeblack 1.5
            music2 Loved_Up
            sound chpok6
            img 31745 vpunch
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob2_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob2_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob2_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31746
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob2_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob2_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob2_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob1.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob2_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob2_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob2_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31747
            citizen2 "А теперь выпусти мой ствол изо рта."
            citizen2 "Оближи мои яйца."
            # Моника выпускает член, возмущенно
            music2 stop
            fadeblack 1.5
            music Groove2_85
            imgd 31748
            m "Я не буду этого делать!"
            citizen2 "Я доплачу еще 2 бакса. Заработаешь 23 бакса."
            citizen2 "Ну же. Давай."
            mt "Черт!"
            menu:
                "Лизать яйца Тима.":
                    label gallery_31750:
                    music Groove2_85
                    imgf 31743
                    mt "Фу! Я никогда такого не делала!"
                    mt "!!!"
                    mt "С другой стороны, он готов доплатить за это..."
                    mt "А мне нужны деньги..."
                    # Моника облизывает его мошонку
                    fadeblack 1.5
                    music Loved_Up
                    imgfl 31749
                    citizen2 "Оооо!!!"
                    sound lick3
                    imgf 31750
                    w
                    sound lick3
                    imgd 31751
                    w
                    sound lick3
                    imgd 31750
                    w
                    sound lick3
                    imgd 31751
                    w
                    sound lick3
                    imgd 31750
                    w
                    sound lick3
                    imgd 31751
                    w
                    sound lick3
                    imgd 31750
                    w
                    sound lick3
                    imgd 31751
                    citizen2 "Прикольноооо!!!"
                    imgf 31752
                    citizen2 "Дааа!!!"
                    citizen2 "А теперь соси дальше!"
                    # Моника берет член в рот
#                    $ monicaCitizensPunksBlowjob2 = True # Моника облизала мошонку панку за 2 бакса, когда делала минет
                    pass
                "Нет!":
                    music Power_Bots_Loop
                    imgf 31743
                    mt "Я не собираюсь ему все облизывать!"
                    mt "Фу!"
                    mt "Тем более, за 2 доллара!"
                    music Groove2_85
                    imgd 31753
                    m "Нет!"
                    m "Только минет!"
                    citizen2 "Тогда давай, продолжай!"
                    citizen2 "И бери его поглубже!"
                    # Моника снова берет у него в рот
                    pass
            label gallery_31759:
            fadeblack 1.5
            music Loved_Up2
            imgfl 31754
            citizen2 "Оооо, охренительно!!!"
            imgf 31756
            w
            sound drkanje5
            imgd 31755
            w
            imgd 31756
            w
            sound drkanje5
            imgd 31755
            w
            imgd 31756
            w
            sound drkanje5
            imgd 31755
            w
            imgd 31756
            w
            sound drkanje5
            imgd 31755
            citizen1 "Оооох, твою мать! Кончу сейчас!"
            img 31757
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan5
            citizen2 "ОООО!!!"
            citizen1 "ОООО, кончаю!!!"
            menu:
                "Кончить в рот Моники.":
                    # один кончает Монике в рот, второй на руку
                    img 31758
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen2 "ДАААА..."
                    citizen2 "АААА КААААЙФ!!!"
                    citizen1 "АААААААА!!!"
                    # Моника зло смотрит то на одного, то на второго
                    imgd 31759
                    w
                    imgf 31760
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
#                    $ ep214_citizens1_2_cumzone1 = 1
                    pass
                "Кончить на лицо Моники.":
                    # один кончает Монике на лицо, второй на руку
                    img 31761
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen2 "ДАААА..."
                    citizen2 "АААА КААААЙФ!!!"
                    citizen1 "АААААААА!!!"
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31762
                    w
                    imgf 31760
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
#                    $ ep214_citizens1_2_cumzone1 = 2
                    pass
                "Кончить на грудь Моники.":
                    # один кончает Монике на грудь, второй на руку
                    img 31763
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan8
                    citizen2 "ДАААА..."
                    citizen2 "АААА КААААЙФ!!!"
                    citizen1 "АААААААА!!!"
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31764
                    w
                    imgf 31760
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
#                    $ ep214_citizens1_2_cumzone1 = 3
                    pass
            music Groove2_85
            imgd 31765
            sound snd_punch_face2
            citizen2 "Это так крутоооо, тееееть!"
            citizen1 "Дааа!!!"
            citizen1 "Надо было не покупать пиво."
            citizen1 "Сейчас она и мне отсосала бы."
            citizen1 "В следующий раз она сосать будет у меня!"
            citizen2 "Договорились, чувак."
            pass

        "Встать на колени и взять в рот член Тома. (in Extra version) (disabled)" if game.extra != True:
            pass
        "Встать на колени и взять в рот член Тома." if game.extra == True:
            # Моника встает на колени перед Томом

            fadeblack
            sound snd_fabric1
            pause 1.5
            sound highheels_short_walk
            pause 2.0
            music Loved_Up
            imgfl 31766
            w
            imgf 31767
            citizen1 "Давай, тетя, начинай!"
            citizen1 "Этот член не будет сосаться сам!"
            # Моника выполняет
            # Моника делает минет Тому
            # Тим стоит сбоку от них и дрочит
            fadeblack 1.5
            music Loved_Up
            imgf 31770
            w
            sound chpok6
            imgf 31768
            w
            imgd 31769
            w
            imgf 31771
            citizen2 "Вот черт! А мой член?"
            citizen1 "Твой член в пролете, Тим! Ха-ха!"
            citizen2 "Тогда дрочи мне!"
            citizen2 "Так не честно! Я тоже заплатил деньги!"

            menu:
                "Взять член Тима в руку.":
                    pass
            # Моника берет его в руку и начинает водить туда-сюда
            # дописать сцену
            fadeblack 1.5
            music2 Loved_Up
            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31772
            citizen1 "Аааа! Это чертовски охренительно, чувак!"
            citizen2 "Дааа, чувак!"

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob3_4 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob3_4.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob3_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music2 stop
            fadeblack 1.0
            music Groove2_85
            imgf 31774
            citizen2 "Эй, теть, а сиськи?!"
            citizen2 "Снимай майку!"
            citizen2 "Я доплачу еще 1 бакс!"
            citizen1 "Давай, снимай!"
            imgd 31773
            mt "Черт!"
            mt "!!!"
            menu:
                "Снять одежду.":
                    pass
            # Моника снимает майку
            fadeblack
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            imgfl 31777
            w
            imgf 31775
            w
            imgd 31776
            citizen1 "Сиськи что надо!"
            citizen2 "Да!!!"
            citizen2 "В следующий раз будешь работать не рукой, а сиськами!"
            citizen2 "После того, как отсосешь у меня! Ха-ха!"
            mt "!!!"
            # Моника берет член в рот, а второго держит за член рукой
            # минет и хэнджоб двоим одновременно
            fadeblack 1.0
            music2 Loved_Up

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_1 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_1.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_1
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgfl 31778
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_2 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_2.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_2
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31779
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_3 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_3.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_3
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 31780
            w

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_4= Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_4.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_4
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img black_screen
            with diss
            stop music
            $ renpy.music.set_volume(0.5, 0.5, channel="music")
            $ renpy.music.set_volume(0.2, 0.5, channel="music2")
            play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Citizen1_Citizen2_Blowjob3.ogg"
            scene black
            image videov_Monica_Citizen1_Citizen2_Blowjob4_5 = Movie(play="video/v_Monica_Citizen1_Citizen2_Blowjob4_5.mkv", fps=30)
            show videov_Monica_Citizen1_Citizen2_Blowjob4_5
            with fade
            wclean
            stop music
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgd 31781
            citizen1 "Эй, теть!"
            citizen1 "Давай я засуну свой член между твоими сиськами."
            citizen2 "Это я придумал!"
            citizen1 "Тим, заткнись!"
            citizen1 "В следующий раз рот и сиськи тети будут работать для тебя!"
            # Моника выпускает член, возмущенно
            music2 stop
            fadeblack 1.5
            music Groove2_85
            imgf 31782
            m "Я не буду этого делать!"
            citizen1 "Да ладно тебе!"
            citizen1 "Я же только потрогаю их немного."
            citizen1 "Зато доплачу еще 2 бакса. Заработаешь 23 бакса."
            citizen1 "Ну же. Давай."
            mt "Черт!"
            menu:
                "Согласиться.":
                    music Groove2_85
                    imgd 31776
                    mt "Фу! Я не хочу, чтоб он прикасался к моей груди!"
                    mt "!!!"
                    mt "С другой стороны, он готов доплатить за это..."
                    mt "А мне нужны деньги..."
                    # Моника злобно на него смотрит
                    imgd 31783
                    m "Только быстро!"
                    # Том немного приседает, обхватывает груди Моникик руками и засовывает между ними член
                    music Loved_Up
                    imgf 31784
                    w
                    imgd 31785
                    w
                    # она в это время продолжает дрочить Тиму
                    imgf 31786
                    w
                    # Том делает несколько движение членом между грудями Моники
                    imgd 31787
                    w
                    imgd 31788
                    w
                    sound drkanje5
                    imgd 31787
                    w
                    imgd 31788
                    w
                    sound drkanje5
                    imgd 31787
                    w
                    imgd 31788
                    w
                    sound drkanje5
                    imgd 31787
                    w
                    imgd 31788
                    citizen2 "Оооо!!!"
                    citizen1 "Какие сиськииии!!!"
                    citizen1 "Охренеееть!!!"
                    imgf 31789
                    mt "Гребаные придурки!"
                    mt "!!!"
                    mt "Черт! Моника!"
                    mt "Никогда бы не подумала, что ты окажешься в такой ситуации!"
                    mt "!!!"
                    ## можно и эмоцию Моники какую-нибудь про этих панков
                    # потом отпускает грудь и направляет член ей в рот
                    imgd 31790
                    citizen1 "А теперь соси дальше!"
                    # Моника берет член в рот
#                    $ monicaCitizensPunksBlowjob3 = True # Моника позволила Тому засунуть член между своими грудями за 2 бакса, когда делала минет
                    pass
                "Нет!":
                    music Power_Bots_Loop
                    imgd 31776
                    mt "Я не хочу, чтоб он прикасался к моей груди!"
                    mt "Своим грязным вонючим отростком!"
                    mt "Фу!"
                    mt "Тем более, за 2 доллара!"
                    music Groove2_85
                    imgf 31783
                    m "Нет!"
                    m "Только минет!"
                    citizen1 "Тогда давай, продолжай!"
                    citizen1 "И бери его поглубже!"
                    # Моника снова берет у него в рот
                    pass
            fadeblack 1.5
            music Loved_Up2
            img 31791 vpunch
            w
            sound drkanje5
            imgd 31792
            w
            imgd 31791
            w
            sound drkanje5
            imgd 31792
            w
            imgd 31791
            w
            sound drkanje5
            imgd 31792
            w
            imgd 31791
            w
            sound drkanje5
            imgd 31792
            citizen1 "Оооо, охренительно!!!"
            citizen1 "Оооох, твою мать! Кончу сейчас!"
            imgf 31793
            mt "Не могу поверить что я делаю это..."
            mt "Двум грязным панкам в какой-то дыре в трущобах..."
            img 31794
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan8
            citizen2 "Я тоже!"
            citizen2 "ОООО!!!"
            citizen1 "Аааа, кончаю!!!"
            menu:
                "Кончить в рот Моники.":
                    # один кончает Монике в рот, второй на руку
                    img 31795
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan5
                    citizen1 "АААААААА!!!"
                    citizen1 "КААААЙФ!!!"
                    citizen2 "ДАААА..."
                    # Моника зло смотрит то на одного, то на второго
                    imgd 31796
                    w
                    imgf 31797
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
#                    $ ep214_citizens1_2_cumzone2 = 1
                    pass
                "Кончить на лицо Моники.":
                    # один кончает Монике на лицо, второй на руку
                    img 31798
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan5
                    citizen1 "АААААААА!!!"
                    citizen1 "КААААЙФ!!!"
                    citizen2 "ДАААА..."
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31799
                    w
                    imgf 31797
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
#                    $ ep214_citizens1_2_cumzone2 = 2
                    pass
                "Кончить на грудь Моники.":
                    # один кончает Монике на грудь, второй на руку
                    img 31800
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man_moan5
                    citizen1 "АААААААА!!!"
                    citizen1 "КААААЙФ!!!"
                    citizen2 "ДАААА..."
                    # Моника зло смотрит то на одного, то на второго
                    sound hlup2
                    imgd 31801
                    w
                    imgf 31797
                    mt "ФУУУ!!!"
                    mt "Придурки!!!"
                    mt "!!!"
#                    $ ep214_citizens1_2_cumzone2 = 3
                    pass
            music Groove2_85
            imgd 31802
            citizen1 "Это было крутоооо, тееееть!"
            citizen2 "Дааа!!!"
            citizen2 "В следующий раз она сосать будет у меня!"
            citizen1 "Или у нас двоих!"
            citizen1 "!!!"
            pass
    # Моника зло на них смотрит, вытираясь рукой
    music Pyro_Flow
    imgf 31803
    mt "Никакого следующего раза не будет!"
    mt "Два никчемных идиота!"
    mt "Что бы я еще раз пустила в свою квартиру кого-то!!!"
    mt "Ни за что!!!"
    # затемнение
    # комната Моники
    # все стоят одетые, панки довольные, Моника злая
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85

    if monicaCitizensPunksBlowjob2 == True or monicaCitizensPunksBlowjob3 == True:
        imgfl 31804
        citizen1 "Это было круто, теть!"
        ## они же отдали ей уже 10 баксов
#        $ add_money(13.0)
        citizen2 "Вот твои 13 баксов."
        citizen2 "Итого ты заработала 23 бакса, теть!"
    else:
        imgfl 31804
        citizen1 "Это было круто, теть!"
#        $ add_money(11.0)
        citizen2 "Вот твои 11 баксов."
        citizen2 "Итого ты заработала 21 бакс, теть!"

    # дают ей деньги
    imgf 31725
    citizen2 "Как насчет того, чтобы отсосать у двоих сразу! Аха-ха!"
    sound male_laugh2a
    citizen1 "Надо будет братану нашему рассказать."
    citizen1 "Он уже был на этой хате с другой шлюхой."
    citizen1 "По-любому захочет тоже прийти с нами!"
    music Pyro_Flow
    imgd 31726
    m "Что?!"
    m "?!?!?!"
    m "Я больше никого сюда не пущу!"
    m "После того, что вы здесь устроили!"
    music Groove2_85
    imgf 31805
    sound man_steps
    citizen2 "Да ладно тебе, теть!"
    citizen2 "Давай, до следующей нашей встречи!"
    # уходят
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.5
    music Power_Bots_Loop
    imgfl 31806
    mt "Мерзкие тупые придурки!!!"
    mt "Безмозглые никчемные кретины!!!"
    mt "Свиньи!!!"
    mt "Не хочу их больше видеть у себя в квартире!!!"
    mt "Ненавижу их!!!"
    mt "!!!"
    return
