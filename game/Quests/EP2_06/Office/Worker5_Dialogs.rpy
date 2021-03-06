default worker5Option1Cnt = 0
default worker5Option2Cnt = 0

# мужик
label worker5_look:
    img 20312
    with fade
    mt "Этот карьерист метит на место Босса в этом отделе?"
    mt "Наивный дурачок!"
    return

label worker5_dialogue_workplace:
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

label worker5_dialogue_office:
    music Sneaky_Snitch
    img 20358
    with fadelong
    w5 "Миссис Бакфетт, я бы хотел поговорить о моем повышении!"
    menu:
        "Давай поговорим.":
            $ worker5Option1Cnt += 1
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
            $ worker5Option2Cnt +=1
            music Pyro_Flow
            img 20361
            m "Повышении?!"
            m "Не сегодня. Выйди и закрой за собой дверь."
            call bitch(1, "worker5_dialogue_office") from _call_bitch_190
            music Sneaky_Snitch
            img 20363
            with fade
            w5 "Хорошо. Понимаю, Вы очень заняты. Ну ничего, в другой раз."
            return


label takeReportsFlashCard_Worker5:
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
