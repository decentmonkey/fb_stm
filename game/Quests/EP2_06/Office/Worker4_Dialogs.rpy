default worker4Option1Cnt = 0
default worker4Option2Cnt = 0

# близняшка 2
label worker4_look:
    img 20305
    with fade
    w
    img 20306
    with diss
    mt "Две близняшки."
    mt "Они думают что они красивые?"
    mt "Они ошибаются! Фи!"
    return

label worker4_dialogue_workplace:
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

label worker4_dialogue_office:
    music ZigZag
    img 20350
    with fadelong
    w4 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            $ worker4Option1Cnt += 1
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
            call bitch(-1, "worker4_dialogue_office") from _call_bitch_188
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
            $ worker4Option2Cnt += 1
            m "Я занята, приходи завтра."
            w4 "Ладно, но у меня проблема..."
            call bitch(1, "worker4_dialogue_office") from _call_bitch_189
            music Pyro_Flow
            img 20356
            with fade
            m "Ты что, не понимаешь? Я сейчас занята!"
            return

label takeReportsFlashCard_Worker4:
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
