label ep24_dialogues2_steve1:
# После старта фитнеса с Бетти и первого посещения его, в ближайшую субботу приходит Стив.
# Бетти сообщает об этом Монике при входе в любую локацию дома (если приход не с улицы).
    $ store_music()
    music Groove2_85 high
    if cloth == "Whore":
        img 9710
        with fade
        betty "Моника, гувернантка..."
        img 9717
        w
        img 9718
        w
        img 9719
        with fade
        m "Да, Миссис Робертс?"
        betty "В эту субботу к нам придет важный гость."
        "Так что прибирайся в доме как следует."
        img 9720
        "Если где-нибудь останется пылинка и мне придется краснеть перед гостем, то ты будешь наказана."
        "Гувернантка, тебе понятно?"
        img 9721
        music Power_Bots_Loop high
        mt "!!!"
        img 9722
        with fade
        music Groove2_85 high
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        img 9723
        betty "И купи себе нормальную одежду!"
        betty "Меня раздражает твой внешний вид!"
        betty "Ты достаточно зарабатываешь для этого!"
        img 9724
        m "Да, Миссис Робертс..."
        mt "Черт, мне лучше поменьше показываться перед Бетти в этой жуткой одежде!"
        $ restore_music()
        return

    if cloth == "Governess" or 1==1:
        img 9710
        with fade
        betty "Моника, гувернантка..."
        img 9711
        m "Да, Миссис Робертс?"
        img 9712
        betty "В эту субботу к нам придет важный гость."
        "Так что прибирайся в доме как следует."
        img 9713
        "Если где-нибудь останется пылинка и мне придется краснеть перед гостем, то ты будешь наказана."
        img 9714
        with fade
        "Гувернантка, тебе понятно?"

        music Power_Bots_Loop high
        img 9715
        mt "!!!"
        music Groove2_85 high
        img 9716
        with fade
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        $ restore_music()
        return

    img 9710
    betty "Моника, гувернантка..."
    m "Да, Миссис Робертс?"
    betty "В эту субботу к нам придет важный гость."
    "Так что прибирайся в доме как следует."
    "Если где-нибудь останется пылинка и мне придется краснеть перед гостем, то ты будешь наказана."
    "Гувернантка, тебе понятно?"
    mt "!!!"
    m "Да, Миссис Робертс."
    "Я поняла."
    "Я буду стараться изо всех сил."
    $ restore_music()

    return

label ep24_dialogues2_steve2:
# В пятницу, при попытке выхода из дома, Бетти также напоминает Монике об этом.
    $ store_music()
    music Groove2_85

    if cloth == "Whore":
        img 9710
        with fade
        betty "Моника, гувернантка..."
        img 9717
        w
        img 9718
        w
        img 9719
        with fade
        m "Да, Миссис Робертс?"
        betty "В эту субботу к нам придет важный гость."
        "Так что прибирайся в доме как следует."
        img 9720
        "Если где-нибудь останется пылинка и мне придется краснеть перед гостем, то ты будешь наказана."
        "Гувернантка, тебе понятно?"
        img 9721
        music Power_Bots_Loop
        mt "!!!"
        music Groove2_85
        img 9722
        with fade
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        img 9723
        with fade
        betty "И купи себе нормальную одежду!"
        betty "Меня раздражает твой внешний вид!"
        betty "Ты достаточно зарабатываешь для этого!"
        img 9724
        m "Да, Миссис Робертс..."
        mt "Черт, мне лучше поменьше показываться перед Бетти в этой жуткой одежде!"
        $ restore_music()
        return
    if cloth == "Governess" or 1==1:
        img 9710
        with fade
        betty "Моника, гувернантка..."
        img 9711
        m "Да, Миссис Робертс?"
        img 9712
        betty "В эту субботу к нам придет важный гость."
        "Так что прибирайся в доме как следует."
        img 9713
        "Если где-нибудь останется пылинка и мне придется краснеть перед гостем, то ты будешь наказана."
        img 9714
        "Гувернантка, тебе понятно?"
        img 9715
        music Power_Bots_Loop
        mt "!!!"
        img 9716
        music Groove2_85
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        $ restore_music()
        return
    img 9710
    betty "Моника, гувернантка..."
    m "Да, Миссис Робертс?"
    betty "В эту субботу к нам придет важный гость."
    "Так что прибирайся в доме как следует."
    "Если где-нибудь останется пылинка и мне придется краснеть перед гостем, то ты будешь наказана."
    "Гувернантка, тебе понятно?"
    mt "!!!"
    m "Да, Миссис Робертс."
    "Я поняла."
    "Я буду стараться изо всех сил."
    return

label ep24_dialogues2_steve3:
# В субботу Стив приходит и здоровается с Бетти и Ральфом (Ральф в костюме)
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_4
    img black_screen
    with Dissolve(2.0)

    music BossaBossa
    img 9725
    with fade
    steve "Здравствуй, Ральф!"
    img 9726
    "Здравствуй, дружище!"
    img 9727
    with fade
    "Как ты обжился?"
    "Нравится тебе твой новый дом?"
    img 9728
    "А где твоя очаровательная супруга?"
    music Power_Bots_Loop
    img 9729
    with Dissolve(0.5)
    mt "!!!"
    mt "О Боже! Это Стив!"
    music BossaBossa
    img 9730
    with fade
    ralph "Да, Стив!"
    "Спасибо что пришел!"
    img 9731
    with Dissolve(0.5)
    "Бетти... Она где-то здесь..."
    betty "Добрый день, Стив."
    img 9732
    with fade
    "Давно тебя не видела."
    "Ты изменился."
    img 9733
    "Возраст идет тебе на пользу."
    img 9734
    with fade
    steve "О! Бетти!"
    "Ты стала еще более неотразима!"
    img 9735
    "Твоя фигура налилась соком!"
    img 9736
    betty "Спасибо, Стив!"
    "Ты меня смущаешь..."
    img 9737
    with fade
    betty "Пожалуйста, проходи в гостиную."
    "У меня все готово!"

# Бетти говорит Монике чтобы не показывала нос, что Бетти сама справится с обслуживанием гостей.
    music Groove2_85
    img 9738
    with fadelong
    betty "Гувернантка, не вздумай показывать нос!"
    "Я сама справлюсь с обслуживанием гостей!"
    img 9739
    m "Да, Миссис Робертс."
    "Я уверена, что Вы справитесь лучше!"
    img 9740
    with Dissolve(0.5)
    betty "..." #Надменно смотрит
    img 9741
    with fadelong
    mt "Как хорошо, что Бетти сама будет обслуживать Стива!"
    mt "Я уверена, что он меня узнает!"
    mt "Еще этого мне не хватало дополнительно ко всем моим проблемам!"
    return


label ep24_dialogues2_steve4:
# После этого вход в гостиную заблокирован в этот день.
    mt "Бетти запретила мне заходить туда..."
    mt "К тому же там Стив!"
    mt "Я не хочу, чтобы он узнал меня!"
    return False

label ep24_dialogues2_steve5:
    # Показывается сцена того как компания сидит в гостиной и общается.
    $ store_music()
    stop music fadeout 1.0
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_5
    scene black_screen
    with Dissolve(1)
    music Backbay_Lounge high
    img 9742
    with fadelong
    steve "О, Ральф!"
    steve "Я не видел этой фотографии!"
    img 9743
    steve "Это Ваша свадьба?"
    img 9744
    with Dissolve(0.5)
    betty "Да, Стив."
    img 9745
    with fade
    steve "А это фото?"
    steve "Бетти! Тебе, судя по всему, очень понравился этот дом!"
    img 9746
    betty "Да, Стив. Мне нравится это место..."
    img 9747
    steve "А ты, Ральф? Редкое фото, где ты улыбаешься, дружище!"
    ralph "Кхм... Да, Стив. Меня немного смущает, что Бетти развесила эти фото повсюду и..."
    music Groove2_85
    img 9748
    with fade
    betty "Ральф! Помолчи!"
    betty "Мы семья, а это значит, что наши фото должны быть повсюду."
    betty "Тем более в нашем доме!"
    img 9749
    with fade
    betty "Ральф, ты слишком стеснительный! Ведь Стив твой старый друг!"
    img 9750
    steve "О! Бетти! Ты, как всегда, очень строгая!"
    img 9751
    betty "Мне приходится быть строгой, Стив!"
    betty "Иначе повсюду здесь будет беспорядок!"
    betty "Мне приходится следить за всем."
    img 9752
    with fade
    ralph "Пойдемте скорее выпьем! Мне уже не терпится начать!"
    $ restore_music()
    return

label ep24_dialogues2_steve5a:
    #fade
    stop music fadeout 1.0
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_6
    scene black_screen
    with Dissolve(1)
    sound pour_wine
#    music Lobby_Time
    music BossaBossa
    img 9753
    with fadelong
    w
    img 9754
    with fade
    steve "Бетти, малышка!"
    img 9755
    betty "Да, Стив?"
    img 9756
    with fade
    steve "Ты очень вкусно готовишь!"
    img 9757
    betty "Спасибо, Стив..."
    img 9758
    with fade
    steve "Скажи, тебе хорошо живется здесь?"
    steve "Старина Ральф не обижает тебя?"
    img 9759
    betty "Нет, Стив..."
    "Ральф меня очень любит."
    img 9760
    with Dissolve(0.5)
    "Правда, Ральф?"
    img 9761
    with fade
    ralph "Да, любимая!"
    ralph "Ты самое лучшее, что есть в моей жизни!"
    img 9762
    with fade
    sound kiss2
    betty "Чмок!"
    img 9763
    with fade
    w


    #fade
    img 9764
    with fadelong
    betty "Стив. Я хочу, чтобы ты повлиял на Ральфа."
    img 9765
    betty "Он кушает нерегулярно и совсем не следит за своим желудком."
    betty "Я распланировала прием пищи и составила диету."
    img 9766
    betty "А Ральф как ребенок. За ним все время приходится приглядывать!"

    img 9767
    with fade
    steve "Бетти, Ральфу просто нравится твое внимание! Хе-хе."
    img 9768
    steve "Мы, мужчины, любим притворяться детьми перед такими заботливыми женами. Хе-хе."
    music Groove2_85
    img 9769
    with fade
    betty "А я думаю это из-за того, что Ральф рассеянный и неорганизованный."
    betty "Я люблю во всем порядок! А от Ральфа один бардак!"
    img 9770
    with Dissolve(0.5)
    betty "Он раскидывает носки где попало и прячется от меня, когда я его ищу!"
    img 9771
    ralph "Бетти, но Я..."
    music Pyro_Flow
    img 9772
    betty "Молчи, Ральф!"
    img 9773
    betty "И следи за тем, сколько грамм алкоголя ты выпил!"
    betty "Я не хочу, чтобы ты снова уснул в гостиной, как обычно!"
    img 9774
    ralph "Бетти..."
    img 9775
    with fade
    betty "Что? Не думай что я не заметила, что ты присасываешься к бутылке вина, которая стояла здесь!"
    img 9776
    betty "Сначала я подумала, что его пьет гувернантка, но я слежу за ней и это не она."
    img 9777
    steve "Бетти, не будь такой строгой! Хе-хе."
    img 9778
    with fade
    betty "А какой мне быть, Стив? Мне приходится следить за всеми!"

    img 9779
    with fade
    betty "И почему ты защищаешь Ральфа, Стив?"
    img 9780
    betty "Ты что, хочешь со мной спорить?"
    img 9781
    with fade
    steve "Бетти, нет! Что ты?"
    music Groove2_85
    img 9782
    with fade
    betty "И вообще, сколько ты уже выпил?"
    img 9783
    with fade
    steve "Я выпил совсем чуть-чуть, Бетти!"
    steve "Клянусь тебе!"
    img 9784
    with fade
    betty "Не обманывай меня, Стив!"
    betty "Вы с Ральфом уже изрядно напились!"
    img 9785
    with fade
    steve "Бетти! Я обещаю, что буду вести себя хорошо и буду слушаться тебя! Хе-хе."
    img 9786
    with Dissolve(0.5)
    betty "Хорошо, Стив. Я запомню."
    music BossaBossa
    img 9787
    with diss
    betty "..."
    img 9788
    with fadelong
    betty "А как ты поживаешь в столице, Стив?"
    img 9789
    with Dissolve(0.5)
    betty "Расскажи, как ты так быстро сделал карьеру?"
    img 9790
    steve "О! Эта история очень быстрая и очень долгая!"
    "Я расскажу тебе с удовольствием, если ты нальешь мне еще немного виски!"
    img 9791
    with diss
    betty "Конечно, Стив!"
    betty "Но только чуть-чуть!"

    img black_screen
    with Dissolve(1.0)
    return

label ep24_dialogues2_steve6:
# После начала сна, показывается сцена того как Бетти говорит что Ральф уже пьян и Бетти пойдет уберет посуду.
    stop music fadeout 1.0
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("ПОЗДНИЙ ВЕЧЕР...")) from _call_textonblack_7
    scene black_screen
    with Dissolve(1)
    music BossaBossa
    img 9792
    with fadelong
    w
    img 9793
    with fade
    betty "Ральф!"
    betty "Ральф!!!"
    img 9794
    music Groove2_85
    betty "Как всегда, он напился и уснул!"
    img 9795
    with diss
    betty "..."
    img 9796
    with fade
    betty "Я пойду убирать посуду, Стив!"
    betty "Спасибо за вечер..."
    img 9797
    with fade
    steve "Бетти, спасибо за гостеприимство!"
    img 9798
    with fade
    betty "Можешь ехать домой, Стив."
    "Я сама присмотрю за Ральфом."
    img 9799
    with fade
    sound highheels_short_walk
    w
    img 9800
    w
    img 9801
    with diss
    w
    return

label ep24_dialogues2_steve7:
# Бетти уходит на кухню, там к ней приходит Стив и общается с Бетти.
# Стив спрашивает у Бетти как она устроилась, нравится-ли ей город.
# Бетти общается улыбаясь, говорит что завидует Стиву в том что он давно уехал из той провинции, где она жила.
# Стив говорит помнишь-ли старые времена. Говорит что скучал по тебе, малышка Бетти.
# И по твоей сладкой попке.
# Хорошо-ли Бетти ее сохранила. Бетти отвечает что следит за собой.
# Стив снимает штаны и говорит чтобы Бетти скорее показала ему как она следит за собой.
# Секс Стива и Бетти
# Конец сцены.
    img black_screen
    with Dissolve(1.0)
    music Lobby_Time
    sound snd_washing_dishes2
    img 9802
    with fadelong

    w
    img 9803
    with fade
    w
    img 9804
    with fade
    w
    img 9805
    w
    music Groove2_85
    img 9806
    with fade
    betty "Что ты здесь делаешь, Стив?"
    sound highheels_short_walk
    img 9807
    with fade
    betty "Не видишь? У меня много работы по дому."
    music BossaBossa
    img 9808
    with fade
    steve "О! Бетти!"
    "Малышка Бетти!"
    steve "Скажи, как ты устроилась здесь?"
    "Нравится-ли тебе столица?"
    img 9809
    betty "Да, Стив. Мне нравится."
    "Если честно, я завидую тому, что ты давно уехал из нашей провинции и все это время жил здесь, а не там."
    img 9810
    with fade
    steve "Бетти! Но ведь нам есть что вспомнить!"
    steve "Помнишь наши вечеринки у костра?"
    steve "Мы собирались всеми друзьями. Пили и танцевали до утра."
    img 9811
    betty "Помню, Стив. Я думала ты уже забыл."
    betty "Ты ведь теперь такой большой Босс..."
    img 9812
    with fade
    steve "Бетти! У меня есть кое-кто, кто постоянно напоминает о тебе!"
    img 9813
    betty "И кто же это?"
    # Стив достает член
    # Бетти смотрит все время на член

    sound snd_zip
    music Pyro_Flow
    img 9814
    with Dissolve(1.0)
    steve "Вот он, Бетти!"
    "Это мой член!"
    img 9815
    with fade
    "Он все время напоминает о тебе!"
    img 9816
    with diss
    "Он помнит, Бетти!"
    "Он помнит твою попку!"
    img 9817
    with diss
    "Ведь он провел столько времени в ней!"
    img 9818
    with fade
    betty "..."
    img 9819
    with fade
    steve "Скажи, Бетти!"
    "Твоя попка помнит его, так ведь?"
    menu:
        "Да, помнит...":
            pass
        "Я замужем, Стив!":
            img 9821
            betty "Я замужем, Стив!"
            "Пожалуйста, оденься и иди домой!"
            steve "Хорошо, Бетти!"
            "Но я еще вернусь к тебе."
            return False

    music Loved_up
    img 9820
    with fade
    betty "Да, помнит..."
    img 9822
    steve "Он скучает по твоей попке, Бетти!"
    "Мне даже пришлось повысить Ральфа, чтобы твоя попка была поближе к моему члену."
    $ bettySteveKitchenTouchedDick = True
    img 9823
    with fade
    betty "Стив, ты ведь знаешь, я теперь замужем за Ральфом."
    img 9824
    "Я люблю его и он мой муж."
    img 9825
    with fade
    steve "Бетти, малышка!"
    "Я не собираюсь жениться на тебе!"
    img 9826
    "Я потратил столько денег, чтобы доставить эту попку сюда!"
    "Скажи, она в такой же форме как и раньше?"
    "Ты хорошо сохранила ее?"
    "Я ведь не буду разочарован?"
    img 9827
    with fade
    betty "Я слежу за собой, Стив."
    "Я регулярно занимаюсь фитнесом и йогой."
    img 9828
    with fade
    steve "Значит Бетти хорошо сохранила свою попку для Стива?"
    "Скорее повернись ко мне задом, покажи ее!"
    "Мой член уже не может, он хочет поскорее попробовать твою попку, вспомнить ее вкус!"
    img 9829
    betty "Стив, я замужем..."
    img 9830
    with fade
    sound Jump2
    steve "Бетти, скажи."
    "Твоей попке не нравилось когда он был внутри нее?"
    menu:
        "Это неважно, Стив! Я замужем!":
            music Pyro_Flow
            img 9837
            with fade
            betty "Это неважно, Стив! Я замужем!"
            return False
        "Нравилось...":
            pass
    img 9831
    with fade
    betty "Нравилось..."
    img 9832
    sound Jump1
    steve "И что, твоя попка не хочет, чтобы мой член снова оказался в ней?"
    menu:
        "Хочет...":
            pass
        "Это неважно, Стив! Я замужем!":
            music Pyro_Flow
            img 9837
            with fade
            betty "Это неважно, Стив! Я замужем!"
            return False

    img 9833
    with fade
    betty "Хочет..."
    betty "..."
    music Groove2_85
    img 9834
    with diss
    betty "Ой!"
    betty "Стив! Что я сказала?!"
    betty "Я замужем, я не могу заниматься этим с тобой!"
    betty "Я не могу изменять Ральфу..."
    music Loved_up
    img 9835
    with fade
    sound Jump1
    steve "Бетти! Это не измена!"
    steve "Он просто хочет вспомнить твой вкус!"
    img 9836
    with diss
    steve "Это как поцелуй старых друзей!"
    steve "В этом нет ничего плохого!"
    menu:
        "Хорошо, Стив... Только быстро...":
            pass
        "Это неважно, Стив! Я замужем!":
            music Pyro_Flow
            img 9837
            with fade
            betty "Это неважно, Стив! Я замужем!"
            return False
    # Бетти снимает трусики
    sound snd_fabric1
    $ bettySteveKitchenSex = True
    music Loved_up2
    img 9838
    with fade
    betty "Хорошо, Стив... Только быстро..."
    img 9839
    with fade
    w
    img 9840
    with diss
    w
    img 9841
    with diss
    w
    img 9842
    with diss
    w
    img 9843
    with fade
    betty "Стив! Давай быстрее!"
    "Мало времени!"
    img 9842
    with diss
    w
    img 9844
    with Dissolve(0.5)
    betty "Стив! Давай быстрее!"
    music stop
    img black_screen
    with Dissolve(1.0)


    stop music
    play music "Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_1 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_1.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_1
    with fade
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_2 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_2.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_2
    with fade
    steve "О! Бетти! Твоя попка бесподобна!"
    steve "Я так рад, что она теперь поблизости!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_3 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_3.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_3
    with fade
    steve "Я теперь смогу навещать эту попку когда захочу..."
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_4 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_4.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_4
    with fade
    betty "Не получится, Стив!"
    betty "Я не собираюсь изменять Ральфу!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_5 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_5.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_5
    with fade
    steve "О! Бетти!"
    "Малышка Бетти!"
    steve "Тебе не нравится?"
    "Хочешь чтобы я остановился?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_6 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_6.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_6
    with fade
    betty "Нет, Стив. Не останавливайся..."
    betty "Ахххх..."
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_7 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_7.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_7
    with fade
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_House_Kitchen_Steve_Betty_Sex1.mp3"
    scene black
    image video_House_Kitchen_Steve_Betty_Sex_1_8 = Movie(play="video/House_Kitchen_Steve_Betty_Sex_1_8.mkv", fps=30)
    show video_House_Kitchen_Steve_Betty_Sex_1_8
    with fade
    wclean

    # Идет секс

    music Loved_up2
    img 9845
    with fade
    sound bulk1
    steve "АААААрггхххххх!!!!"
    music Pyro_Flow
    img 9846
    with fade
    betty "Черт, Стив!"
    betty "Ты что, кончил в меня?!"

    img 9847
    with fadelong
    steve "Бетти, малышка! Прости, я увлекся..."
    steve "Хе-хе."
    img 9848
    betty "Мне надо скорее помыться и принять таблетку."
    betty "А ты свободен, Стив!"
    music stop

    return
#    # Конец, Бетти выходит из кухни. Встречает Барди
#    img black_screen
#    with Dissolve(1.0)
#    pause 2.0
#    music Groove2_85
#    img 9849
#    with fadelong
#    betty "Что ты делаешь здесь? Тебе разве не пора спать?!"
#    img 9850
#    with fade
#    bardie "Я услышал какие-то звуки и пришел проверить все-ли в порядке."
#    img 9851
#    with diss
#    betty "Здесь все в порядке, Барди!"
#    "У нас очень важный гость и он уже уходит."
#    img 9852
#    with fade
#    "Это взрослые дела и тебе не стоит лезть в них!"
#    "Вон отсюда!"

    return


# В следующую субботу снова приходит Стив.
# Бетти сообщает об этом Монике после уборки.
# В пятницу, при попытке выхода из дома, Бетти также напоминает Монике об этом.
# Также Бетти говорит что ее дома не будет и чтобы Моника позаботилась о гостях.


label ep24_dialogues2_steve8:
    $ store_music()
    music Groove2_85 high
    if cloth == "Whore":
        img 9853
        with fadelong
        betty "Моника, гувернантка..."
        img 9859
        m "Да, Миссис Робертс?"
        betty "В эту субботу к нам придет важный гость."
        betty "Меня дома не будет, поэтому ты должна будешь позаботиться о гостях!"
        img 9860
        "Гувернантка, тебе понятно?"
        img 9861
        mt "!!!"
        mt "Дьявол! Надеюсь это не Стив!"
        img 9862
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        $ restore_music()
        return
    if cloth == "Governess" or 1==1:
        img 9853
        betty "Моника, гувернантка..."
        img 9854
        m "Да, Миссис Робертс?"
        img 9855
        with fade
        betty "В эту субботу к нам придет важный гость."
        betty "Меня дома не будет, поэтому ты должна будешь позаботиться о гостях!"
        music Power_Bots_Loop high
        img 9856
        with diss
        "Гувернантка, тебе понятно?"
        img 9857
        mt "!!!"
        mt "Дьявол! Надеюсь это не Стив!"
        music Groove2_85 high
        img 9858
        with fade
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        $ restore_music()
        return

    img 9853
    betty "Моника, гувернантка..."
    m "Да, Миссис Робертс?"
    betty "В эту субботу к нам придет важный гость."
    betty "Меня дома не будет, поэтому ты должна будешь позаботиться о гостях!"
    "Гувернантка, тебе понятно?"
    mt "!!!"
    mt "Дьявол! Надеюсь это не Стив!"
    m "Да, Миссис Робертс."
    "Я поняла."
    "Я буду стараться изо всех сил."
    $ restore_music()
    return

label ep24_dialogues2_steve9:
    music Groove2_85
    if cloth == "Governess":
        img 9853
        with fadelong
        betty "Моника, гувернантка..."
        img 9854
        m "Да, Миссис Робертс?"
        img 9855
        with fade
        betty "В эту субботу к нам придет важный гость."
        betty "Меня дома не будет, поэтому ты должна будешь позаботиться о гостях!"
        img 9856
        with diss
        "Гувернантка, тебе понятно?"
        img 9857
        mt "!!!"
        mt "Дьявол! Надеюсь это не Стив!"
        img 9858
        with fade
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        return
    if cloth == "Whore":
        img 9853
        with fadelong
        betty "Моника, гувернантка..."
        img 9859
        m "Да, Миссис Робертс?"
        betty "В эту субботу к нам придет важный гость."
        betty "Меня дома не будет, поэтому ты должна будешь позаботиться о гостях!"
        img 9860
        with diss
        "Гувернантка, тебе понятно?"
        img 9861
        mt "!!!"
        mt "Дьявол! Надеюсь это не Стив!"
        img 9862
        with fade
        m "Да, Миссис Робертс."
        "Я поняла."
        "Я буду стараться изо всех сил."
        return
    img 9853
    betty "Моника, гувернантка..."
    m "Да, Миссис Робертс?"
    betty "В эту субботу к нам придет важный гость."
    betty "Меня дома не будет, поэтому ты должна будешь позаботиться о гостях!"
    "Гувернантка, тебе понятно?"
    mt "!!!"
    mt "Дьявол! Надеюсь это не Стив!"
    m "Да, Миссис Робертс."
    "Я поняла."
    "Я буду стараться изо всех сил."
    return

label ep24_dialogues3_steve10_locked1:
    mt "В доме гости. Мне нельзя отлучаться."
    mt "Иначе мне влетит от Бетти."
    if monicaBitch == True:
        mt "От этой сучки!"
    return

label ep24_dialogues3_steve10_enter_room1:
    if cloth != "Governess":
        mt "Я не пойду туда в таком виде!"
        mt "Я еще не сошла с ума!"
        return False
    return True

label ep24_dialogues3_steve10_enter_room2:
    mt "Я пойду туда только если меня позовут."
    mt "Мне вообще не хочется идти туда!"
    return False

label ep24_dialogues3_steve10:
# Сцена. Приходит Стив, здоровается с Ральфом и они идут за стол.
# Стив спрашивает а где Бетти.
# Ральф говорит что ее сегодня не будет.
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_8
    img black_screen
    with Dissolve(2.0)
    img 9863
    with fadelong
    music BossaBossa
    steve "Ральф! Привет, дружище!"
    steve "Извини, что я снова зашел!"
    steve "Надеюсь что ты мне рад!"
    ralph "Стив, я всегда рад тебе!"
    ralph "Пожалуйста, проходи!"
    return


label ep24_dialogues3_steve10a:
    # Гостиная
    music BossaBossa
    img 9864
    with fade
    steve "Ральф, а где Бетти?"
    img 9865
    ralph "Бетти сегодня не будет."

# Стив расстроен, говорит что она так прекрасно обслуживала их (и виляла своей попой)
# Ральф отвечает что пусть Стив не беспокоится, сегодня их будет обслуживать гувернантка.
# Стив спрашивает и что, она также хороша как Бетти?
    img 9866
    with fade
    steve "Ральф, но как же нам быть?"
    steve "Бетти так прекрасно обслуживала нас!"
    img 9867
    ralph "Стив, можешь не беспокоиться, сегодня нас будет обслуживать гувернантка."
    img 9868
    with diss
    steve "И что, эта гувернантка также хороша как Бетти?"
# Ральф говорит что Бетти она не нравится, она считает ее нерадивой гувернанткой.
# Но Ральф считает что она хорошая девушка и старается угодить хозяевам.
# Потому он думает что она имеет шанс исправиться и стать лучше убираться, более профессионально.
    img 9869
    with fade
    ralph "Нет, Стив. Бетти она не нравится. Она считает ее нерадивой гувернанткой."
    ralph "Но я считаю что она хорошая девушка и старается угодить хозяевам."
    img 9870
    with diss
    ralph "Потому я думаю, что она исправится и станет лучше убираться."
    ralph "Более профессионально..."

# Стив говорит Ральфу хорошо и просит позвать ее, чтобы та принесла стаканы под виски и лед.
# Ральф зовет Монику.
# Моника приходит, вся напряжена.
    img 9871
    with fade
    steve "Хорошо, Ральф."
    steve "Зови свою гувернантку!"
    img 9872
    with diss
    steve "Нам как раз нужны стаканы под виски и лед!"
    img 9873
    with fadelong
    ralph "Моника, гувернантка!"
    img 9874
    ralph "Иди сюда!"
    return

label ep24_dialogues3_steve10a2:
    music Groove2_85
    ralph "Моника, гувернантка!"
    ralph "Иди сюда!"
    mt "..."
    mt "Дьявол! Меня зовут!"
    mt "Интересно, кто там пришел..."
    return

label ep24_dialogues3_steve10b:

# Стив видит ее и удивляется. Смотрит на нее с улыбкой.
# Моника смотрит на него презрительно.
# Спрашивает у Ральфа что им нужно.
    #звук двери
    music stop
    img black_screen
    with Dissolve(1.0)
    sound snd_door_open1
    pause 1.0
    sound snd_door_close1
    music Groove2_85
    img 9877
    with fadelong
    w
    img 9875
    with fade
    w
    img 9876
    w
    img 9878
    w
    music Villainous_Treachery
    img 9879
    with fade
    w
    img 9880
    with diss
    mt "!!!"
    img 9881
    with fade
    w
    img 9882
    with fade
    m "!!!"
    img 9883
    with diss
    steve "???"
    img 9884
    with fade
    m "..."
    img 9885
    with diss
    steve "..."
    img 9886
    with fade
    w
    img 9887
    with diss
    w
    img 9888
    with fade
    w
    img 9889
    with diss
    w
    img 9890
    with diss
    w
    img 9891
    with fade
    w
#    music Funk_Soul1
    music Pyro_Flow
    sound highheels_short_walk
    img 9892
    with Dissolve(1.0)
    w
    img 9893
    with fade
    m "Да, Мистер Робертс."
    m "Чем могу быть Вам полезна?"
# Ральф просит принести стаканы для виски
# Моника говорит хорошо и уходит.
# Стив говорит Ральфу что рад за него. Теперь тот достаточно богат, чтобы позволить себе
# такую горячую гувернантку.
    img 9894
    with diss
    ralph "Моника, принеси стаканы для виски!"
    img 9895
    with fade
    m "Да, хорошо Мистер Робертс. Одну минуту."
    sound highheels_short_walk
    img 9896
    with diss
    w
    img 9897
    with diss
    w
    img 9898
    with diss
    w
    img 9899
    with diss
    steve "..." # смотрит на попу
    music stop
    sound snd_door_open1
    img black_screen
    with Dissolve(0.5)
    sound highheels_short_walk
    pause 1.0
    music BossaBossa
    img 9900
    with fadelong
    steve "Ральф, дружище!"
    steve "Я очень рад за тебя!"
    img 9901
    with diss
    steve "Ты теперь достаточно богат, чтобы позволить себе такую горячую гувернантку!"
# Ралфь отвечает что не оценивает гувернантку с точки зрения привлекательности, потому что
# Стив же знает, какая Бетти строгая.
    img 9902
    with fade
    ralph "Стив, я не оцениваю эту гувернантку с точки зрения привлекательности."
    ralph "Ты ведь знаешь, какая Бетти строгая..."
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Groove2_85
    return

label ep24_dialogues3_steve10b2:
    mt "Гость оказался Стивом! Я так и знала!"
    mt "Что же мне теперь делать?"
    mt "..."
    mt "Подумаю позже. Сейчас мне надо принести этим ничтожествам стаканы для виски."
    mt "Я думаю что Бетти все приготовила на кухне."
    return

label ep24_dialogues3_steve10b4:
    mt "Я еще не сделала то что мне сказал Ральф."
    return


label ep24_dialogues3_steve10b3:
    menu:
        "Взять стаканы под виски.":
            return True
        "Уйти.":
            return False
    return False

label ep24_dialogues3_steve10c:
# Приходит Моника.
# И говорит: вот, прошу, Ваши стаканы.
# Стив смотрит в свой стакан и говорит. Гувернантка, можно Вас попросить подойти сюда?
# Моника подходит: Да, Сэр?
    music stop
    img black_screen
    with Dissolve(0.5)
    sound highheels_short_walk
    pause 1.0
    sound snd_door_open1
    music Groove2_85
    img 9903
    with fadelong
    w
    #звук стакана
    img 9904
    with fade
    sound bottle1
    w
    img 9905
    with diss
    w
    img 9906
    with fade
    sound bottle1
    w
    sound Jump1
    img 9907
    with fade
    w

    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #подглядывание с 9907
            #governess
            img 9971
        else:
            #nude
            img 9977
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 9972
        if monicaBettyPantiesId == 2:
            img 9973
        if monicaBettyPantiesId == 3:
            img 9974
        if monicaBettyPantiesId == 4:
            img 9975
        if monicaBettyPantiesId == 5:
            img 9976

    with diss
    sound Jump2
    w

    img 9908
    with fade
    m "Вот Ваши стаканы, Мистер Робертс..."
    sound highheels_short_walk
    img 9909
    with fade
    steve "..."
    music stop
    img 9910
    with fade
    steve "Гувернантка, можно Вас попросить подойти сюда?"

    music Pyro_Flow
    img 9911
    w
    sound highheels_short_walk
    img 9912
    with fade
    w
    img 9913
    with diss
    m "Да, Сэр?"
# Стив говорит: посмотрите, этот стакан недостаточно чист!
# Моника отвечает что за чистотой посуды следит Миссис Робертс.
# Стив удивляется: ах, если так, то прошу прощения. Похоже это я только что поставил след
# от своих пальцев на этом стакане.
    img 9914
    steve "Посмотрите, этот стакан недостаточно чист!"
    img 9915
    with diss
    w
    img 9916
    with fade
    m "Прошу прощения, но за чистотой посуды следит Миссис Робертс..."
    img 9917
    steve "Ах, если так, то прошу прощения!"
    img 9918
    with diss
    steve "Похоже, это я только что поставил след от своих пальцев на этом стакане."
# Моника презрительно смотрит.
# Уходит
# Стив смотрит на ее задницу.
# Проходит время.
    img 9919
    with fade
    m "..."
    img 9920
    with diss
    steve "..."
    img 9921
    with Dissolve(0.5)
    w
    img 9922
    m "..."
    img 9923
    with fade
    steve "..."

    #звук двери
    sound snd_door_open1
    sound highheels_short_walk
    img 9924
    with fadelong
    w
    sound snd_door_close1
    img black_screen
    with Dissolve(0.5)
    pause 1.5
    sound pour_wine
    music BossaBossa
    #звук наливания
    img 9925
    with fadelong
    w
    img 9926
    steve "Ральф! Давай скорее выпьем!"
    steve "У меня отличное настроение сегодня!"
    music Groove2_85
    return

label ep24_dialogues3_steve10c3:
    #Спустя время
    music BossaBossa
    img 9927
    with fadelong
    steve "Ральф! Может быть позовешь свою гувернантку снова?"
    steve "Мы скучаем без внимания!"

# Ральф кричит: Моника, принеси нам что-нибудь закусить!
# Моника приходит и говорит, да, Мистер Робертс. Миссис Робертс приготовила для Вас эти колбаски.
# Кладет их на стол. Стив смотрит на грудь.
# Моника отворачивается и Стив роняет прибор на пол.
    img 9928
    with fade
    ralph "Моника, гувернантка!"
    music Groove2_85
    return

label ep24_dialogues3_steve10c2:
    ralph "Моника, гувернантка!"
    mt "..."
    mt "Меня снова зовут... Что им еще от меня надо?!"
    return

label ep24_dialogues3_steve10d:
    music stop
    img black_screen
    with Dissolve(0.5)
    sound highheels_short_walk
    pause 1.0
    sound snd_door_open1
    music Groove2_85
    img 9929
    with fadelong
    w
    img 9930
    with fade
    ralph "Моника! Принеси нам что-нибудь закусить!"
    img 9931
    with fade
    m "Да, Мистер Робертс..."
    return

label ep24_dialogues3_steve10d2:
    mt "Принеси то! Принеси это!"
    mt "Я им спрашивается кто?! Служанка?!"
    mt "Хотя, вообще-то я притворяюсь ей..."
    mt "..."
    mt "Ладно, где там эта еда? Бетти должна была все приготовить..."
    return

label ep24_dialogues3_steve10d3:
    menu:
        "Взять еду и отнести гостям.":
            return True
        "Уйти.":
            return False
    return False

label ep24_dialogues3_steve10e:

    music stop
    img black_screen
    with Dissolve(0.5)
    sound highheels_short_walk
    pause 1.0
    sound snd_door_open1
    music Groove2_85

    img 9932
    with fadelong
#    sound bottle1
    w
    img 9933
    with fade
#    sound bottle1
    m "Вот, Мистер Робертс... Пожалуйста..."
    img 9934
    with fade
    w
    img 9935
    with diss
    sound Jump1
    w
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
    #подглядывание с 9935
    #governess
            img 9978
        else:
            #nude
            img 9984
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 9979
        if monicaBettyPantiesId == 2:
            img 9980
        if monicaBettyPantiesId == 3:
            img 9981
        if monicaBettyPantiesId == 4:
            img 9982
        if monicaBettyPantiesId == 5:
            img 9983
    with diss
    sound Jump2
    w
    m "Миссис Робертс приготовила для Вас эту закуску..."
    sound highheels_short_walk
    img 9936
    with fade
    w
    img 9937
    with diss
    steve "..."
    img 9938
    w
    sound Jump1
    img 9939
    with fade
    w
    #звук падающей вилки
    sound snd_forkfall
    img 9940
    with diss
    w

# Стив говорит: Ой, гувернантка, ты не могла бы поднять прибор, я нечаянно уронил его.
# Моника наклоняется, чтобы подобрать.
# Стив наклоняется и видит что у Моники нет трусиков.
# Стив удивляется и пытается схватить ее рукой. Моника отскакивает и ненавидяще смотрит на Стива.
    img 9942
    steve "Ой, гувернантка!"
    steve "Ты не могла бы поднять прибор? Я нечаянно уронил его..."
    music Pyro_Flow
    img 9941
    with diss
    w
    img 9943
    with fade
    w
    img 9944
    with diss
    m "!!!"
    steve "..."
    img 9945
    with fade
    w
    img 9946
    with fade
    w
    img 9947
    with fade
    w
    img 9948
    with Dissolve(0.5)
    w
    img 9949
    with Dissolve(0.5)
    sound Jump1
    w

    #подглядывание
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #governess
            img 9985
        else:
            #nude
            img 9992
            with diss
            w
            img 9991
            with diss
            w
            img 9993
            with diss
            w
            img 9994
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 9986
        if monicaBettyPantiesId == 2:
            img 9987
        if monicaBettyPantiesId == 3:
            img 9988
        if monicaBettyPantiesId == 4:
            img 9989
        if monicaBettyPantiesId == 5:
            img 9990

    with diss
    w
    sound Jump2
    img 9950
    with diss
    w
    music stop
    img 9951
    m "!!!"
    menu:
        "Отдать вилку Стиву...":
            music Pyro_Flow
            img 9964
            with fade
            m "Пожалуйста, Мистер Стив."
            img 9962
            with diss
            "Вот Ваша вилка..."
        "Взять вилку в руку! (Bitchiness!)" if monicaBitch == True:
            #звук Моника разворачивается с вилкой
            $ monicaSteveLivingRoomOffended = True
            music Villainous_Treachery
            img 9952
            with fadelong
            w
            img 9953
            with diss
            w
            img 9954
            with diss
            w
            img 9955
            ralph "А? Что за шум?"
            img 9956
            with diss
            w
            img 9957
            with diss
            w
            img 9958
            with fade
            w
            music Hidden_Agenda
            img 9959
            with fadelong
            call bitch(10, "livingroom_steve_offended1") from _call_bitch_184
            m "Мистер Робертс, все в порядке!"
            img 9960
            with diss
            m "Просто упал столовый прибор."
            img 9961
            with fade
            m "Пожалуйста, Мистер Стив."
            "Вот Ваша вилка..."
            img 9963
            with diss
            w
            img 9962
            with Dissolve(0.5)
            w
            music Pyro_Flow
            img 9964
            with fade
            w
        "Взять вилку в руку! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass
    sound highheels_short_walk
    img 9965
    with fade
    w

    music stop
    sound snd_door_open1
    img black_screen
    with Dissolve(0.5)
    pause 1.5
    sound snd_door_close1

    music BossaBossa
    img 9966
    with fadelong
    steve "Какая у тебя горячая гувернантка, Ральф!"
    steve "Давай скорее еще выпьем!"
    ralph "Давай, Стив!"
    return

label ep24_dialogues3_steve10e2:
    # Моника была без трусиков
    mt "Мне надо надеть трусики! Стив все время пялится мне под юбку!"
    mt "Мерзавец!"
    return

label ep24_dialogues3_steve10e3:
    mt "Я не собираюсь снимать трусики, пока в этом доме Стив!"
    return


label ep24_dialogues3_steve10f:
# Проходит время.
# Ральф спит пъяный.
# Стив говорит: поспи здесь пока, дружище Ральф! Я скоро вернусь к тебе!

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Вечер...")) from _call_textonblack_9
    img black_screen
    with Dissolve(2.0)
    # Спустя время
    #звук храпа
    sound snd_hrap
    img 9968
    with fadelong
    w
    music BossaBossa
    img 9969
    with fade
    steve "Ральф?!"
    steve "Ты меня слышишь, Ральф?! Или ты спишь?"
    sound snd_hrap
    img 9967
    w
    img 9970
    with fade
    steve "Хе-хе..."
    steve "Поспи здесь пока, дружище Ральф! Я скоро вернусь к тебе!"
    return



label ep24_dialogues3_steve10g:

# Затемнение
# Стив находит Монику у бассейна в подвале.
# Стив говорит Монике. Ах вот где ты, Моника!
# Я тебя повсюду ищу!
# Моника зло отвечает зачем он ее ищет?! Что ему от нее надо?!
    sound highheels_short_walk
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.5
    music Groove2_85
    img 9995
    with fadelong
    steve "Ах вот ты где, Моника!"
    steve "Я тебя повсюду ищу!"
    img 9996
    m "Зачем ты меня ищешь?! Что тебе от меня надо?!"
# Стив говорит что вообще ищет Монику. Что Моника куда-то пропала.
# И он никак не думал обнаружить ее здесь!
# Моника отвечает: обнаружил, и что дальше?! Всем расскажешь?!
# Стив говорит что нет, это не в его интересах.
    img 9997
    with fade
    steve "Вообще-то я тебя давно ищу!"
    steve "Ты куда-то пропала в последнее время..."
    steve "И я никак не думал обнаружить тебя здесь!"
    img 9998
    m "Вообще-то это мой дом! Почему бы мне здесь не быть?!"
    m "Хорошо, обнаружил, и что дальше?! Всем расскажешь?!"
    img 9999
    with fade
    steve "Нет, Моника! Это не в моих интересах."
# Моника спрашивает: а что тогда в твоих интересах, Стив?!
# Стив отвечает: правда-ли то что Моника в кого-то влюбилась.
# И ради этой любви отреклась от денег и от компании.
# А вместо этого впала в пучину разврата и теперь спит с мужчинами за деньги?!
# Моника отвечает что Стив что, сошел с ума?!
# Откуда он взял такую чушь?!
    img 10000
    with diss
    m "А что тогда в твоих интересах, Стив?!"
    img 10001
    steve "Моника, верны ли слухи о тебе?"
    m "Какие еще слухи?!"
    img 10002
    with fade
    steve "Говорят, что ты в кого-то влюбилась!"
    "И ради этой любви отреклась от денег и от компании."
    "И, вместо этого, впала в пучину разврата и теперь спишь с мужчинами за деньги!"
    music Power_Bots_Loop
    img 10003
    with diss
    m "Ты что, Стив?! Сошел с ума?!"
    m "Откуда ты взял такую чушь?!"
# Стив отвечает ну как же, ты начала сниматься в обновленном журнале.
# Сама задала ему новый курс. И, все мы делаем ставки о том когда же ты
# Покажешь всему миру свою киску или, что лучше, займешься с кем-нибудь сексом на камеру!
# Моника отвечает что и не думала услышать чего-то другого от такого мерзавца как Стив!
# Стив спрашивает, а в чем тогда причина?
    music Groove2_85
    img 10004
    with fade
    steve "Ну как же. Ты начала сниматься в обновленном журнале."
    steve "Сама задала ему новый курс."
    img 10005
    with diss
    steve "И, все мы делаем ставки на то, когда же ты покажешь всему миру свою киску!"
    steve "Или, что еще лучше, займешься с кем-нибудь сексом на камеру!"
    img 10006
    m "Я и не думала услышать что-нибудь другое от такого мерзавца как ты, Стив!"
    img 10007
    with fade
    steve "Но, если это не так, то в чем же тогда причина, Моника?"
# Моника мнется и отвечает что все это немного сложно.
# Есть некоторые проблемы, но Моника их вскоре решит.
# И, пока Ральфу необязательно знать о том кто она.
# И вообще, Монике нужна от Стива кое-какая помощь.
    music Hidden_Agenda
    img 10008
    with fade
    m "..."
    m "Это..."
    m "Это все немного сложно, Стив..."
    img 10009
    m "Есть некоторые проблемы, но я их скоро решу!"
    m "Но, пока что Ральфу необязательно знать о том, кто я такая на самом деле."
    img 10010
    with diss
    m "И, вообще, мне нужна от тебя кое-какая помощь..."
# Стив отвечает что с удовольствием поможет Монике и не будет рассказывать Ральфу кто она такая!
# Моника зло отвечает: О! Спасибо, Стив! Спасибо большое тебе!
# Спасибо за твою помощь, которая заключается в том что ты не просто не расскажешь Ральфу обо мне!
# На что я еще могла рассчитывать от такого мерзавца как ты!
# Стив спрашивает а какая еще другая помощь Монике необходима?
    music Groove2_85
    img 10011
    with fade
    steve "Моника, я с удовольствием помогу тебе!"
    steve "Я не буду рассказывать Ральфу кто ты такая!"
    img 10012
    with diss
    m "О! Спасибо, Стив! Спасибо большое тебе!"
    m "Спасибо за твою помощь, которая заключается в том что ты просто не расскажешь Ральфу обо мне!"
    img 10013
    m "На что я еще могла рассчитывать от такого мерзавца как ты!"
    img 10014
    with fade
    steve "Моника, а какая еще другая помощь тебе необходима?"
# Моника отвечает: Деньги... Мне нужны деньги, Стив...
# Ты бедняк по сравнению со мной, но сейчас мне нужны даже те деньги что у тебя есть...
# Стив отвечает что готов перечислить любую сумму по официальному запросу.
# Моника говорит что сейчас временно не может отправить официальный запрос.
# Стив отвечает, как же тогда он может помочь Монике?
    music Pyro_Flow
    img 10015
    with fade
    m "Деньги... Мне нужны деньги, Стив..."
    mt "Дьявол! Мне надо где-то достать деньги для этой сучки Виктории!"
    img 10016
    with diss
    m "Ты бедняк по сравнению со мной, но сейчас мне нужны даже те деньги что у тебя есть..."
    music Groove2_85
    img 10017
    with fade
    steve "Моника, я готов перечислить любую сумму по официальному запросу."
    music Hidden_Agenda
    img 10018
    with fade
    m "Я... Временно не могу отправить официальный запрос..."
    steve "А как же тогда я могу помочь тебе?"
# Моника говорит что просто дай мне эти деньги, просто так.
# Стив говорит что он бизнесмен и ничего не может сделать просто так.
# Моника говорит что это не совсем просто так. Стиву вернутся эти деньги. В 5 раз больше.
# Это выгодная сделка...
# Он бизнесмен и он должен это понимать.
    music Pyro_Flow
    img 10019
    with fade
    m "Дай мне деньги. Просто дай. Просто так!"
    music Groove2_85
    img 10020
    with fade
    steve "Моника, но я ведь бизнесмен!"
    "Я ничего не могу сделать просто так!"
    img 10021
    m "Это будет далеко не просто так! Тебе вернутся эти деньги!"
    img 10022
    with diss
    m "Я верну тебе в 5 раз больше!"
    m "Это выгодная сделка... Ты бизнесмен и должен это понимать..."
# Стив говорит что сделка выглядит выгодной, но очень рискованной.
# Моника спрашивает почему это?
# Стив отвечает потому что я не вижу обеспечительных мер.
# У него нет ни одной бумаги, в соответствии с которой у Моники есть хоть что-то, чем она может
# обеспечить залог суммы, указанной в сделке.
    img 10023
    with fade
    steve "Да, сделка выглядит выгодной, но очень рискованной!"
    m "Почему это?!"
    img 10024
    with diss
    steve "Потому что я не вижу обеспечительных мер."
    steve "Я не вижу ни одной бумаги, в соответствии с которой у тебя есть хоть что-то..."
    steve "Чем ты можешь обеспечить залог суммы, озвученной в сделке."
# Моника зло смотрит на Стива. И говорит что он пожалеет о своих словах.
# Стив говорит что он знает один взаимовыгодный вариант.
# Моника интересуется: какой же?
# Стив говорит что может взять что-нибудь в аренду.
# Моника отвечает что ты уже взял в аренду этиж в ее тауэре. Или нет?!
# Когда Моника вернется, она это проверит!
# Стив мнется... ну... вообще-то... я собирался взять... да...
    music Power_Bots_Loop
    img 10025
    m "!!!"
    img 10026
    with diss
    m "Ты пожалеешь о своих словах..."
    music Groove2_85
    img 10027
    steve "..."
    img 10028
    m "..."
    img 10029
    with fade
    steve "Моника, я знаю один взаимовыгодный вариант!"
    m "Какой же?"
    steve "Я могу взять что-нибудь в аренду!"
    img 10030
    with fade
    m "Вообще-то ты уже взял в аренду этаж в моем тауэре."
    m "Или нет?!?!"
    m "Я проверю это, когда вернусь!"
    img 10031
    steve "..."
    steve "Ну... Вообще-то..."
    steve "Вообще-то... Я собирался взять... Да..."
# Моника злится.
# Стив говорит: Моника, я хочу кое-что взять в аренду у тебя!
# Моника спрашивает и что же? Этот дом она пока не может ему дать. Но это временно.
# Стив говорит что у Моника есть кое-что получше. Кое-что что стоит целое состояние!
# Моника спрашивает: Что?
# Стив отвечает: твоя попа, Моника! Попа Миссис Бакфетт!
# Этот бесценный девственный бриллиант!
    img 10032
    m "!!!"
    music BossaBossa
    img 10033
    with fade
    steve "Моника, я хочу кое-что взять в аренду именно у тебя!"
    img 10034
    m "И что же? Этот дом я пока не могу дать..."
    m "Но это временно..."
    img 10035
    with fade
    steve "Моника! У тебя есть кое-что получше!"
    steve "Кое-что, что стоит целое состояние!"
    img 10036
    m "И что же?!"
    img 10037
    with diss
    steve "Твоя попа, Моника!"
    steve "Попа Миссис Бакфетт!"
    steve "Этот бесценный девственный бриллиант!"
# Ты сама не понимаешь какими богатствами ты обладаешь!
# Моника отвечает гневно: Что?!?!
# Да как ты смеешь, Стив!
# Ты не забыл кто Ты и кто Я?!?
    music Power_Bots_Loop
    img 10038
    with fade
    w
    img 10039
    steve "Ты сама не понимаешь какими богатствами ты обладаешь!"
    img 10040
    with fade
    m "ЧТО?!?!"
    img 10041
    m "Да как ты смеешь, Стив!"
    m "Ты не забыл кто Ты и кто Я?!?"
    if monicaSteveLivingRoomOffended == True:
        $ notif(t_("Моника угрожала Стиву вилкой"))
        music Villainous_Treachery
        img 10042
        with fade
        m "Тебе надоело жить, Стив?"
        img 10043
        with fade
        m "Может быть мне пойти сходить за вилкой?"
    # Стив отвечает: прости, Моника, я не хотел обидеть тебя!
    # Я лишь пытаюсь помочь, изо всех сил. Ты ведь знаешь, я бы помог тебе просто так.
    # Но я бизнесмен и ограничен в своих действиях.
    # И, в рамках того что возможно для меня, я стараюсь помочь тебе изо всех сил!
        music Groove2_85
        img 10044
        with fade
        steve "Прости, Моника! Я не хотел обидеть тебя!"
        steve "Я лишь пытаюсь помочь!"
        img 10045
        with fade
        steve "Ты ведь знаешь, я бы помог тебе и просто так."
        steve "Но я бизнесмен и ограничен в своих действиях."
    else:
        music Groove2_85
        img 10045
        with fade
        steve "Прости, Моника! Я не хотел обидеть тебя!"
        steve "Я лишь пытаюсь помочь!"
        steve "Ты ведь знаешь, я бы помог тебе и просто так."
        steve "Но я бизнесмен и ограничен в своих действиях."

    img 10046
    with diss
    steve "И, в рамках того, что возможно для меня, я стараюсь помочь тебе изо всех сил!"
# Моника отвечет:...
# Я не собираюсь продавать тебе свою попу...
# Стив отвечает: Я не покупаю ее, Моника! Я всего-лишь хочу взять в аренду!
# На полчаса, не более! Подумай! Я ведь собираюсь щедро заплатить за этот бесценный объект!
# Это очень выгодная сделка!
    img 10047
    with fade
    m "Я не собираюсь продавать тебе свою попу!"
    img 10048
    steve "Я не покупаю ее, Моника! Я всего-лишь хочу взять в аренду!"
    steve "На полчаса, не более!"
    steve "Подумай! Я ведь собираюсь щедро заплатить за этот бесценный объект!"
    steve "Это очень выгодная сделка!"
# Выбор:
# Продажа, сдача в аренду... Неважно... Это не для меня...
# А теперь разреши я пойду выполнять свои обязанности, Стив!
# И учти, я припомню тебе твое поведение!
# Хорошо, Моника. Подумай! Я наведаюсь как-нибудь еще!
# Конец сцены
# Либо:
# В этом мире все сдается в аренду, Стив...
# Вопрос только в сумме...
    img 10049
    with fade
    menu:
        "Продажа, сдача в аренду... Неважно... Это не для меня...":
            music Pyro_Flow
            img 10050
            with fade
            m "Продажа, сдача в аренду... Неважно... Это не для меня..."
            m "А теперь разреши я пойду выполнять свои обязанности, Стив!"
            m "И учти, я припомню тебе твое поведение!"
#            m "Хорошо, Моника. Подумай! Я наведаюсь как-нибудь еще!"
            steve "Хорошо, Моника!"
            steve "Но, если передумаешь, приходи ко мне в офис!"
            $ questHelp("steve_6", False)
            $ questHelp("steve_4", False)
            $ questHelp("steve_5", True)
            $ questHelp("steve_7")
            return False
        "В этом мире все сдается в аренду, Стив...":
            pass
    mt "Надеюсь я не пожалею об этом..."
    mt "С другой стороны, у меня нет выхода..."
    mt "Мне надо где-то достать деньги..."
    img 10051
    with fade
    m "В этом мире все сдается в аренду, Стив..."
    img 10052
    m "Вопрос только в сумме..."
# Стив говорит: Моника, покажи ее, покажи свою попу!
# Прежде чем озвучить сумму, я должен посмотреть на объект аренды!
    img 10053
    with fade
    steve "Моника, покажи ее, покажи свою попу!"
    # Если есть трусики
#    steve "Сними трусики и покажи ее!"
    img 10054
    with fade
    menu:
        "Повернуться и показать Стиву свою попу...":
            pass
        "Я не собираюсь показывать никому свою попу, Стив!":
            music Pyro_Flow
            img 10050
            with fade
            m "Я не собираюсь показывать никому свою попу, Стив!"
            m "А теперь разреши я пойду выполнять свои обязанности, Стив!"
            m "И учти, я припомню тебе твое поведение!"
            steve "Хорошо, Моника!"
            steve "Но, если передумаешь, приходи ко мне в офис!"
#            m "Хорошо, Моника. Подумай! Я наведаюсь как-нибудь еще!"
            $ questHelp("steve_6", False)
            $ questHelp("steve_4", False)
            $ questHelp("steve_5", True)
            $ questHelp("steve_7")
            return False

# Выбор повернуться и показать Стиву свою попу...
# Либо конец

# Моника поворачивается и показывает свой зад, задирая юбку.
# Стив обрадованно смотрит и снимает штаны. Виден член.
    music Loved_up
    img 10055
    with fadelong
    w
    img 10056
    with fade
    steve "Хороший вид, Моника!"
    steve "Но можно я посмотрю поближе?"
    music Power_Bots_Loop
    img 10057
    m "..."
    music Loved_up
    img 10056
    with diss
    steve "Посмотрим, что у нас там!"
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #governess
            img 10058
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10059
        if monicaBettyPantiesId == 2:
            img 10060
        if monicaBettyPantiesId == 3:
            img 10061
        if monicaBettyPantiesId == 4:
            img 10062
        if monicaBettyPantiesId == 5:
            img 10063
    with diss
    w
    steve "О! Значит вот какие трусики ты любишь носить!"
    steve "Когда я смотрел на тебя, то всегда думал о том что же на тебе надето внизу!"

    img 10064
    m "Я..."
    m "Я не очень люблю носить их, Стив..."
    m "И давай закроем эту тему!"

    music Loved_up
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #governess
            img 10058
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10059
        if monicaBettyPantiesId == 2:
            img 10060
        if monicaBettyPantiesId == 3:
            img 10061
        if monicaBettyPantiesId == 4:
            img 10062
        if monicaBettyPantiesId == 5:
            img 10063

    with diss

    steve "Моника, ты не против если я их сниму?"
    steve "Мне надо осмотреть объект, который я собираюсь взять в аренду!"
    music Power_Bots_Loop
    img 10065
    mt "!!!"

    music Loved_up
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #Governess
            img 10066
    else:
        if monicaBettyPantiesId == 1:
    #betty
            img 10067
        if monicaBettyPantiesId == 2:
            img 10068
        if monicaBettyPantiesId == 3:
            img 10069
        if monicaBettyPantiesId == 4:
            img 10070
        if monicaBettyPantiesId == 5:
            img 10071
    with diss
    w
    img 10064
    m "..."

    sound snd_fabric1
    img 10072
    with diss
    steve "(Я не верю своим глазам! Я собираюсь трахнуть саму Монику Бакфетт!)"
    img 10073
    steve "(Черт! Сколько лет я мечтал об этом!)"
    img 10074
    with diss
    w

    sound snd_zip
    music Turbo_Tornado
    img 10075
    with fadelong
    steve "Я БЕРУ ЭТОТ ОБЪЕКТ!"


#    steve "!!!"
# Он приближает к попе Моники.
# Моника говорит: Стой! Не вздумай этого делать! Мы еще не заключили сделку!
# Стив говорит: Моника, ты настоящая бизнес-леди! Даже в такой момент ты не забываешь о выгоде!
# Моника отвечает: здесь сплошная выгода для тебя, Стив!
    sound plastinka2
    music Power_Bots_Loop
    img 10076
    m "Стой! Не вздумай этого делать! Мы еще не заключили сделку!"
    img 10077
    with diss
    steve "Моника, ты настоящая бизнес-леди! Даже в такой момент ты не забываешь о своей выгоде!"
    img 10078
    m "Здесь сплошная выгода только для тебя, Стив!"
# Всего за миллион долларов ты получишь то, о чем не могли мечтать и миллиардеры!
# Стив отвечает: какой миллион, Моника?!
# У меня сейчас нет таких средств.
    img 10079
    with diss
    m "Всего за миллион долларов ты получишь то, о чем не могли мечтать и миллиардеры!"
    music Groove2_85
    img 10080
    with fade
    steve "Какой миллион, Моника?!"
    steve "У меня сейчас нет таких средств."

# Моника отвечает: я прекрасно знаю об оборотах твоей компании, Стив!
# Стив говорит: да, но с тех пор как твою компанию возглавили другие люди, у меня начались сплошные проверки!
# Я не могу потратить ни цента, если они пойдут не на благо компании!
# Ты ведь не предлагаешь мне официально провести нашу сделку, правда Моника?!
    m "Я прекрасно знаю об оборотах твоей компании, Стив!"
    img 10081
    steve "Да, но с тех пор как твою компанию возглавили другие люди, у меня начались сплошные проверки!"
    steve "Я не могу потратить ни цента, если они пойдут не на благо компании!"
    steve "Ты ведь не предлагаешь мне официально провести нашу сделку, правда Моника?!"
# Моника говорит: твоя цена?
# $ 1000, Моника!
# Моника отвечает: СКОЛЬКО?!?!?
# Ты за кого меня принимаешь, Стив?!
    img 10082
    m "Твоя цена?"
    steve "$ 1000, Моника!"
    music Power_Bots_Loop
    img 10083
    with diss
    m "СКОЛЬКО?!?!?"
    m "Ты за кого меня принимаешь, Стив?!"
# Стив говорит: Но Моника! Я могу тратить только деньги из моей официальной зарплаты!
# И я теперь помолвлен с Джейн. Она следит за тем куда я трачу свою зарплату!
# Моника, я собираюсь отдать тебе все свои деньги на ланч на месяц вперед!
# Я жертвую всем! Ради тебя! Ради выгодной сделки...
    music Groove2_85
    img 10084
    with fade
    steve "Но Моника! Я могу тратить только деньги из моей официальной зарплаты!"
    steve "И я теперь помолвлен с Джейн. Она следит за тем куда я трачу свою зарплату!"
    img 10085
    with diss
    steve "Моника, я собираюсь отдать тебе все свои деньги на ланч на месяц вперед!"
    steve "Я жертвую всем! Ради тебя! Ради выгодной сделки..."
# По аренде твоей...
# Моника прерывает: Хватит! Необязательно каждый раз произносить вслух название предмета нашей сделки...
    steve "По аренде твоей..."
    m "Хватит! Необязательно каждый раз произносить вслух название предмета нашей сделки..."
# Выбор:
# Это слишком маленькие деньги, Стив! Я даже не буду это обсуждать...
# Конец
# Мне нужно хотя бы $ 10.000, Стив!

    menu:
        "Это слишком маленькие деньги, Стив! Я даже не буду это обсуждать...":
            music Pyro_Flow
            img 10050
            with fade
            m "Это слишком маленькие деньги, Стив! Я даже не буду это обсуждать..."
            m "А теперь разреши я пойду выполнять свои обязанности, Стив!"
            m "И учти, я припомню тебе твое поведение!"
#            m "Хорошо, Моника. Подумай! Я наведаюсь как-нибудь еще!"
            steve "Хорошо, Моника!"
            steve "Но, если передумаешь, приходи ко мне в офис!"
            $ questHelp("steve_6", False)
            $ questHelp("steve_4", False)
            $ questHelp("steve_5", True)
            $ questHelp("steve_7")
            return False
        "Мне нужно хотя бы $ 10.000, Стив!":
            pass
    $ questHelp("steve_4", True)
    $ questHelp("steve_5", False)
    $ questHelp("steve_6")
    $ questHelpDesc("steve_desc1", "steve_desc2")
    img 10086
    with fade
    m "Мне нужно хотя бы $ 10.000, Стив!"

# Стив, если $ 1.000 - это все что у тебя есть, то, может быть, ты дашь их мне просто так?
# Прости, Моника! Но мне очень важно заключить эту сделку!
# Это очень важный объект аренды, он мне очень нужен! Это...
    img 10087
    with diss
    m "Стив, если $ 1.000 - это все что у тебя есть, то, может быть, ты дашь их мне просто так?"
    steve "Прости, Моника! Но мне очень важно заключить эту сделку!"
    steve "Это очень важный объект аренды, он мне очень нужен! Это..."
# Моника: Молчи! Я говорила тебе не произносить вслух!
# Стив: Моника, у меня есть предложение! Давай я возьму в аренду половину твоей попы за $ 1.500!
# Моника: Половину?! Это как?! Это же не гребаный этаж в тауэре, Стив!
# Стив: Я буду двигаться аккуратно! Только в одну сторону! И не буду трогать руками другую половину!
# Я буду соблюдать условия сделки! Я честный бизнесмен.
    img 10088
    m "Молчи! Я говорила тебе не произносить вслух!"
    img 10089
    with fade
    steve "Моника, у меня есть предложение! Давай я возьму в аренду половину твоей попы за $ 1.500!"
    music Power_Bots_Loop
    img 10090
    m "Половину?! Это как?! Это же не гребаный этаж в тауэре, Стив!"
    music BossaBossa
    img 10091
    with fade
    steve "Я буду двигаться аккуратно! Только в одну сторону! И не буду трогать руками другую половину!"
    steve "Я буду соблюдать условия сделки! Я честный бизнесмен."

# Если Моника ругалась на Стива, то говорит что он мешок с дерьмом, а не бизнесмен.
    if steveOffended1 == True:
        $ notif(t_("Моника сказала Стиву по телефону что он мешок с дерьмом.."))
        img 10090
        m "Ты мешок с дерьмом, а не бизнесмен!"

label ep24_dialogues3_steve10_loop1:
# Выбор: отказаться, либо череда выборов с торговлей
# В итоге сходятся на $ 5.000
    img 10092
    with diss
    menu:
        "$ 8.000 за весь объект аренды!":
            img 10093
            with diss
            m "$ 8.000 за весь объект аренды!"
            steve "$ 2.000 за половину!"
            img 10094
            with diss
            menu:
                "Тогда за целый объект $ 7.000!":
                    img 10093
                    with diss
                    m "Тогда за целый объект $ 7.000!"
                    steve "За целый объект $ 4.000"
                    jump ep24_dialogues3_steve10_loop1
                "$ 6.000 за половину! За целый $ 10.000!":
                    img 10093
                    with diss
                    m "$ 6.000 за половину! За целый $ 10.000!"
                    steve "$ 3.500 за целый! $ 1.500 за половину!"
                    jump ep24_dialogues3_steve10_loop1
        "$ 7.000 за половину, за целый $ 10.000!":
            img 10094
            with diss
            m "$ 7.000 за половину, за целый $ 10.000!"
            steve "$ 2.000 за половину!"
            menu:
                "За половину $ 4.000, за целый $ 7.000...":
                    img 10093
                    with diss
                    m "За половину $ 4.000, за целый $ 7.000..."
                    steve "$ 2.200 за половину!"
                    jump ep24_dialogues3_steve10_loop1
                "$ 3.000 за половину, за целый $ 6.000!":
                    img 10093
                    with diss
                    m "$ 3.000 за половину, за целый $ 6.000!"
                    steve "$ 5.000 за целый!"
                    img 10095
                    with diss
                    menu:
                        "Я согласна...":
                            pass
                        "$ 5.500 за целый!":
                            img 10093
                            with diss
                            m "$ 5.500 за целый!"
                            steve "За целый $4.000!"
                            jump ep24_dialogues3_steve10_loop1
# Черт с тобой, Стив!
# (по крайней мере у меня будут деньги для этой сучки Виктории!)
# (и мне не придется позориться перед камерой на весь мир!)
# Я согласна...
    music Groove2_85
    img 10096
    with fade
    m "Черт с тобой, Стив!"
    mt "По крайней мере у меня будут деньги для этой сучки Виктории!"
    mt "И мне не придется позориться перед камерой на весь мир!"
    mt "Обо мне уже начинают ходить слухи..."
    mt "Это нехорошо. Я скоро верну свое положение и мне не стоит терять репутацию..."
    img 10097
    with fade
    m "Я согласна..."
# Стив начинает движение
# Моника говорит: Стой!
# Стив, ты же понимаешь, что тебе это не сойдет с рук?!
# Стив: да, Моника, я понимаю, но я готов рискнуть!
# Стив, ты понимаешь что я убъю тебя за это?!
    music Turbo_Tornado
    img 10098
    with fade
    steve "..."
    sound plastinka2
    music Power_Bots_Loop
    img 10099
    m "СТОЙ!"
    m "Стив, ты же понимаешь, что тебе это не сойдет с рук?!"
    steve "Да, Моника, я понимаю, но я готов рискнуть!"
    m "И ты понимаешь, что за это я сотру тебя в порошок?!"
    m "Я закрою твою фирму и заставлю тебя жить на улице!"
# Моника, но у нас честная сделка!
# Стив, ты понимаешь что эта задница стоит миллиарды?!
# Стив отвечает: Да, Моника! Я знаю!
# Это очень редкая и выгодная сделка!
    steve "Моника, но у нас честная сделка!"
    img 10100
    with diss
    m "Стив, ты понимаешь что эта задница стоит миллиарды?!"
    music Turbo_Tornado
    img 10098
    steve "Стив отвечает: Да, Моника! Я знаю!"
    steve "Это очень редкая и выгодная сделка!"
#    music stop
    w

    #звук входа
    sound hlup10
    img 10101
    with diss
    w
    sound snd_monica_ahh
    img 10102
    m "Ааааххххххх!!!"

# И входит в Монику
# Идет секс
    music stop
    img black_screen
    with Dissolve(0.5)
#    pause 0.3
    #видео1 начало
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_1 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_1.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_1
    with fadelong
    wclean
    m "Я забыла спросить, Стив..."
    m "Деньги у тебя с собой?!"
    steve "Моника, конечно с собой!"
    steve "Они у меня на банковской карте! Я могу перевести их тебе прямо сейчас..."
    steve "Вернее, после окончания аренды твоей..."
    m "Заткнись! Я так и знала!"
    m "Купишь подарочный сертификат и отправишь его на адрес, который я скажу."
    steve "Нет проблем, Моника! Не отвлекайся!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_2 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_2.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_3 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_3.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_4 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_4.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_5 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_5.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_6 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_6.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_7 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_7.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_7
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_8 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_8.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_1.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_1_9 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_1_9.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_1_9
    wclean


# Во время секса Моника говорит: я забыла спросить, Стив...
# Деньги у тебя с собой?!
# Стив отвечает: Моника, конечно с собой!
# Они у меня на банковской карте! Я могу тебе перевести их тебе прямо сейчас...
# Вернее, после окончания аренды твоей ...
# Моника говорит: Заткнись! Я так и знала!
# Купишь подарочный сертификат и отправишь его на адрес, который я скажу.
# Стив: Нет проблем, Моника! Не отвлекайся!

# Моника: черт, Стив! Какой ты огромный!
# Стив: Моника, тебе нравится? Я так и знал!
# Моника: Нет, Стив!
# Мне... Ах...
# Мне не нравится, конечно же! Ах!!!
    m "Черт, Стив! Какой ты огромный!"
    steve "Моника, тебе нравится? Я так и знал!"
    m "Нет, Стив!"
    stop music
    sound snd_orgasm1
    m "Мне... Ах..."
    sound snd_orgasm2
    m "Мне не нравится, конечно же! Ах!!!"

    #видео1 конец

# Ах!! Ах!! Ааааааххх!!
# Моника падает... Она кончила
# (снова это ощущение...)
# (что это было снова?!?!)
    music Loved_up2
    img 10103
    sound snd_orgasm3
    m "Ах!! Ах!! Ааааааххх!!"
    sound snd_bodyfall
    img 10104
    with fade
    m "..."
    img 10105
    with diss
    mt "Снова это ощущение..."
    mt "Что это было снова?!?!"
# Стив: Моника, я понимаю что ты кончила, но срок аренды твоей попы действует до тех пор пока не кончу Я!
# Пожалуйста, встань как ты стояла до этого, задери юбку!
# И обеспечь мне доступ к объету аренды!
    music Groove2_85
    img 10106
    with fade
    steve "Моника, я понимаю что ты кончила, но срок аренды твоей попы действует до тех пор, пока не кончу Я!"
    steve "Пожалуйста, встань как ты стояла до этого, задери юбку!"
    img 10104
    with fade
    steve "И обеспечь мне доступ к объекту аренды!"
    steve "В соответствии с договором!"
# Моника: Мерзавец...
# Моника встает. Стив снова входит.
# Стив: аааах!!!
# Моника кричит: не вздумай кончить в меня!
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    img 10107
    with fade
    w
    img 10108
    with diss
    steve "Иначе сделка недействительна!"

    sound highheels_short_walk
    img 10109
    with fade
    w
    img 10110
    with Dissolve(0.5)
    w
    music Loved_up2
    img 10111
    with fade
    w
    img 10112
    with fade
    w
    img 10113
    with fade
    w
    img 10114
    with fade
    m "Мерзавец..."
    music stop
    w
    #звук входа
    sound hlup10
    img 10115
    with diss
    w
    sound snd_monica_ahh
    img 10118
    m "Ааааххххххх!!!"

    img black_screen
    with diss
    pause 1.0
    #видео2
    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_1 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_1.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_1
    with fadelong
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_2 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_2.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_3 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_3.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_4 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_4.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_5 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_5.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_6 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_6.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_8 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_8.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_9 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_9.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_10 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_10.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_10
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_11 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_11.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_11
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_12 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_12.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_12
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Pool_Basement_Steve_Monica_Sex_2.mp3"
    scene black
    image videov_Pool_Basement_Steve_Monica_Sex_2_13 = Movie(play="video/v_Pool_Basement_Steve_Monica_Sex_2_13.mkv", fps=30)
    show videov_Pool_Basement_Steve_Monica_Sex_2_13
    wclean

    stop music
    music Indo_Rock
    img 10117
    with diss
    w
    img 10116
    with diss
    w

    img 10119
    with fade
    steve "Аааах!!!"
    img 10120
    m "Не вздумай кончить в меня!"
# Стив вынимает и хочет кончить на юбку Моники.
# Не вздумай кончить на мою униформу! У меня нет другой!
# Стив хочет кончить на коврик.
# Не вздумай кончать на коврик! Я не собираюсь убирать за тобой!
    img 10121
    with fade
    steve "Аааах!!!"
    m "Не вздумай кончить на мою униформу! У меня нет другой!"

    img 10122
    with fade
    steve "Аааах!!!"
    m "Не вздумай кончать на коврик! Я не собираюсь убирать за тобой!"

# Стив: О боже! Моника! Куда же мне можно кончить?! Скорее!
# Кончай в бассейн!
    img 10123
    with diss
    steve "О Боже! Моника! Куда же мне можно кончить?! Скорее!"
    img 10124
    m "Кончай в бассейн!"
# Стив поворачивается к бассейну и кончает.
# Выбор: если Моника сучка, то она может толкнуть Стива в бассейн.
# Остынь, Стив! Ты слишком возбудился, малыш!
# После этого бросает визитку у бассейна и говорит.
# И только попробуй не прислать сертификат!
# Тогда я наведаюсь к тебе!
# Либо:
# Стив, вот визитка. Пришли сертификат по этому адресу.
# И, Стив...
# Давай забудем об этом... Об этой сделке...
# И, необязательно об этом кому-то говорить. Ты понимаешь меня?
# О, Моника! Конечно!
# Если захочешь вспомнить, приходи ко мне в офис!
    img 10125
    with diss
    steve "Аааах!!!"
    img 10126
    with diss
    $ monicaHasSexWithSteveBasement = True
    menu:
        "Толкнуть Стива в бассейн..." if monicaBitch == True:
            $ monicaSteveBasementOffended = True
            img 10127
            with fade
            #звук бульк
            w
            music stop
            img black_screen
            with diss
            sound snd_water_splash
            pause 1.5
            music Pyro_Flow
            img 10128
            with fadelong
            m "Остынь, Стив! Ты слишком возбудился, малыш!"

# После этого бросает визитку у бассейна и говорит.
            sound snd_take_paper
            img 10129
            with fade
            m "Вот адрес!"
            img 10130
            with diss
            m "И только попробуй не прислать сертификат!"
            m "Тогда я наведаюсь к тебе!"
        "Толкнуть Стива в бассейн... (Моника недостаточно стерва) (disabled)" if monicaBitch == False:
            pass

        "Дать визитку..." if monicaBitch == False:
            music Groove2_85
            img 10131
            with fade
            m "Стив, вот визитка. Пришли сертификат по этому адресу."
            music Hidden_Agenda
            img 10132
            with diss
            m "И, Стив..."
            m "Давай забудем об этом... Об этой сделке..."
            m "Необязательно об этом кому-то говорить. Ты понимаешь меня?"
            img 10133
            with fade
            m "О, Моника! Конечно!"
            m "Если захочешь вспомнить, приходи ко мне в офис!"

        "Дать визитку... (Моника слишком стерва) (disabled)" if monicaBitch == True:
            pass

    img black_screen
    with Dissolve(1.0)
    pause 2.0
    return

label ep24_dialogues3_steve10a1:
    sound snd_hrap
    mt "Я не собираюсь подходить к этой пьяной скотине!"
    return False

label ep24_dialogues3_steve10b1:
    if monicaHasSexWithSteveBasement == True:
        mt "БОЖЕ! Моника!"
        mt "Что ты наделала?"
        mt "Надеюсь ты не пожалеешь об этом!"
        mt "И это... Что это было за чувство?"
        mt "Я, как-будто, потеряла сознание..."
        mt "Странное ощущение..."
    else:
        mt "Мерзавец!!!"
    return


label ep24_dialogues3_steve11:
# На следующее утро Моника думает что надо бы проверить, переслал-ли Стив деньги.
# Моника может проверить у Виктории это.
# Стив деньги не переслал, поэтому Моника злится.
    mt "Мне стоит проверить, переслал-ли Стив деньги..."

    #Если ругалась на Стива
    if steveOffended1 == True:
        mt "От этого мешка с дерьмом можно ожидать чего угодно!"
    return


label ep24_dialogues3_steve12:
    music Hidden_Agenda
    img 10134
    with fadelong
    m "Мисс Виктория..."
    m "Скажите... Вам приходил на почту подарочный сертификат?"
    music Groove2_85
    img 10135
    dick_secretary "Нет, не приходил..."
    dick_secretary "Но я его жду, как обычно..."
    img 10136
    with fade
    m "Да, Мисс Виктория... Он будет, не волнуйтесь..."
    img 7965
    dick_secretary "Я не волнуюсь, подружка!"

    music Power_Bots_Loop
    img 10137
    with fadelong
    mt "ЭТОТ СТИВ МЕНЯ ОБМАНУЛ!!!"
    mt "ОН ЧТО, ДУМАЕТ ЧТО БЕСПЛАТНО ТРАХНУЛ МЕНЯ?!?!"
    mt "ОН ПОПЛАТИТСЯ ЗА ЭТО!!!"
    return

label ep24_dialogues3_steve13:
# При входе в офис Бифа пишется что будет доступно в следующей версии.
    help "Будет доступно в следующем обновлении игры. Следите за новостями!"
    return


label ep24_dialogues3_steve14:
    # Разговор с Ральфом по поводу Стива (активация второго прихода)
    if cloth != "Governess":
        return
    menu:
        "Мистер Робертс. Я хочу спросить по поводу гостя...":
            pass
        "Уйти.":
            return False
    $ store_music()
    music Groove2_85 high
    img 5810
    with fadelong
    m "Мистер Робертс. Я хочу спросить по поводу гостя..."
    ralph "Да, Моника?"
    img 5807
    m "Скажите, откуда Вы знаете Стива?"
    img 5811
    ralph "Мы со Стивом старые друзья. К тому же, он сейчас мой Босс."
    ralph "Ты его знаешь, Моника? Ты когда-то убиралась у него?"
    img 5822
    m "Нет, Мистер Робертс... Я... Никогда не убиралась у него."
    img 5817
    ralph "Кстати, он собирается снова придти на днях."
    img 5819
    with diss
    w
    return True







#
