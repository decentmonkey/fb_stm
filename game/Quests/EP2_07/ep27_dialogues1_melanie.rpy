# Моника говорит с Мелани в гримерке
default ep27_dialogues_melanie_stage = 0

default monicaAskMoneyFromMelanie = False

label ep27_dialogues1_melanie1:
    if ep27_dialogues_melanie_stage == 0:
        music Groove2_85
        img 20601
        with fadelong
        m "Мелани, скажи!"
        m "Что случилось с тобой?!"
        m "Это важно для меня! Ты же знаешь!"
        music Master_Disorder
        melanie "Я Вам сказала, Миссис Бакфетт. Я занята..."
    else:
        music Master_Disorder
    menu:
        "Мелани, ты решила мой вопрос?" if ep27_dialogues_melanie_stage >= 0:
            img 20602
            with fade
            m "Мелани, ты решила мой вопрос?"
            # если была фотосессия
            if monicaMelanieCastingLickedDildo == True:
                music Power_Bots_Loop
                img 20604
                with diss
                m "Ты что думаешь, что я забуду про то что ты заставила меня делать, там в офисе?!"
                m "Что ты сможешь сделать вид будто ничего не было?"
                m "У тебя не выйдет, Мелани!"
            music Master_Disorder
            img 20603
            with diss
            melanie "..."
            melanie "Я не знаю про что Вы говорите, Миссис Бакфетт."
            melanie "Я работаю здесь моделью, а Вы отвлекаете меня."
            if ep27_dialogues_melanie_stage < 1:
                $ ep27_dialogues_melanie_stage = 1
            $ monicaOfficeMakeupRoomSkipMusicOneTime = True
            return False

        "Мелани, ты была у Маркуса?" if ep27_dialogues_melanie_stage >= 1:
            music Groove2_85
            img 20605
            with fade
            m "Мелани, скажи, ты вообще была у Маркуса?!"
            m "Я понимаю, у тебя не получилось ничего решить."
            m "Но что Маркус сказал тебе?"
            music Master_Disorder
            img 20606
            with diss
            melanie "Я не знаю про кого Вы говорите, Миссис Бакфетт."
            if ep27_dialogues_melanie_stage < 2:
                $ ep27_dialogues_melanie_stage = 2
            $ monicaOfficeMakeupRoomSkipMusicOneTime = True
            return False
#        "Мелани, мне важно что случилось с тобой! (disabled)":
#            pass
        "Мелани, мне важно что случилось с тобой!" if ep27_dialogues_melanie_stage >= 2: # открывается позднее
            music Groove2_85
            img 20607
            with fade
            m "Мелани. Я понимаю что тебе не удалось решить вопрос с Маркусом."
            m "Я с самого начала понимала что это невозможно."
            m "Но скажи, что случилось с тобой?"
            m "Для меня важно это знать!"
            music Master_Disorder
            img 20608
            with diss
            melanie "Вам важно знать что случилось со мной? Вы задумались про меня?"
            m "Да, Мелани!"
            m "Если не хочешь, можешь больше ничего не говорить."
            m "Расскажи про себя, хотя бы про себя!"
            img 20609
            with fade
            melanie "Почему Вам это интересно, Миссис Бакфетт?"
            img 20610
            with diss
            m "..."
            melanie "..."
            img 20611
            with diss
            m "Потому что..."
            melanie "..."
#            music stop
#            img black_screen
#            with diss
#            pause 1.5
#            music Master_Disorder
            img 20612
            with fade
            m "Потому что меня, возможно, ждет то же самое..."
            music stop
            img black_screen
            with diss
            pause 1.5
            music Master_Disorder
            # Мелани встает
            img 20613
            with fadelong
            melanie "Нет, Миссис Бакфетт."
            melanie "Вас ждет другая судьба..."
            img 20614
            with diss
            m "!!!"
            melanie "Я не буду говорить об этом здесь..."
            img 20615
            with fade
            melanie "Приходите завтра ко мне домой..."
            melanie "Я живу рядом с отелем Le Grand."
            img 20616
            with diss
            melanie "Сделайте это так, чтобы никто не видел и не знал..."
            melanie "Можете одеть эту Вашу одежду, в которой Вы первый раз пришли к Бифу."
            img 20617
            with diss
            melanie "Никто не подумает что такая девушка идет ко мне."
            img 20618
            mt "!!!"
            img 20619
            with diss
            m "Хорошо, Мелани."
            m "Я приду к тебе..."

            return True
        "Уйти.":
            return False
    return
    # Мелани исчезает и ждет дома

label ep27_dialogues1_melanie1a:
    # говорит в фотостудии
    mt "Итак, мне, наконец-то, удалось заставить Мелани пойти на контакт..."
    mt "Завтра я узнаю что случилось с ней."
    mt "Мне нужна информация, любая..."
    mt "Это поможет мне выбраться из тех неприятностей, которые слишком затянулись..."
    return False


label ep27_dialogues1_melanie1b:
    mt "Мне надо {c}идти к Мелани{/c}..."
    mt "Мне нужна информация, любая..."
    mt "Это поможет мне выбраться из тех неприятностей, которые слишком затянулись..."
    return


label ep27_dialogues1_melanie2:
    # Моника приходит к Мелани
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("АПАРТАМЕНТЫ МЕЛАНИ")) from _call_textonblack_30
    img black_screen
    with Dissolve(2.0)
#    music Groove2_85
    music Villainous_Treachery
    img 20620
    with fadelong
    w
    img 20621
    with diss
    m "Мелани, я пришла..."
    img 20622
    with diss
    melanie "..."
    img 20623
    with fade
    m "И я жду ответы..."
    img 20624
    with fade
    melanie "Миссис Бакфетт."
    melanie "Я не уверена в правильности решения пригласить Вас..."
    melanie "Вы точно вошли незаметно? Вас никто не видел?"
    music Groove2_85
    img 20625
    with fadelong
    m "Мелани, меня никто не видел. Я уверена в этом."
    m "И, раз уж я пришла, позволь мне войти."
    img 20626
    with diss
    melanie "..."
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music In_Your_Arms
    img 20627
    with fadelong
    melanie "Хорошо, Миссис Бакфетт..."
    melanie "Проходите."
    #
    sound highheels_short_walk
    img 20628
    with fadelong
    melanie "Присаживайтесь."
    img 20629
    with diss
    melanie "Давайте выпьем вина..."
    img 20630
    with fade
    m "..."
    music Groove2_85
    img 20631
    with fade
    m "Мелани, давай перейдем сразу к делу."
    m "Ты видела Маркуса?"
    img 20632
    with diss
    m "Что он сказал тебе?"
    m "Как мне избавиться от него?!"
    music Villainous_Treachery
    img 20633
    with fade
    melanie "Миссис Бакфетт..."
    melanie "Вы задаете слишком прямые вопросы."
    melanie "Для меня большой риск общаться с Вами..."
    img 20634
    with diss
    m "Мелани, я задаю те вопросы, которые меня больше всего волнуют!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music In_Your_Arms
    sound pour_wine
    img 20635 #наливает
    with fadelong
    melanie "Выпейте вина, Миссис Бакфетт."
    img 20630
    with diss
    m "..."
#    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
#    music In_Your_Arms
    img 20636
    with fadelong
    m "Хорошо, Мелани."
    img 20637
    with diss
    mt "Вкусное вино..."
    mt "Как вкусно..."
    mt "Я уже отвыкла..."
    melanie "Зря Вы не согласились, Миссис Бакфетт..."
    sound plastinka2
    music Groove2_85
    img 20638
    with diss
    w
    img 20639
    with diss
    m "На что я зря не согласилась, Мелани?"
    img 20640
    with fade
    melanie "На то, чтобы поехать на ферму, когда Мистер Маркус предложил Вам..."
    music Power_Bots_Loop
    img 20641
    with hpunch
    m "ЧТО?!"
    img 20642
    with fade
    m "Мелани, ты представляешь о чем идет речь?!"
    m "Ты, вообще, знаешь что это за место?!"
    img 20643
    with diss
    m "Как ты можешь говорить мне такое?!"
    music Villainous_Treachery
    img 20644
    with fadelong
    melanie "Я знаю что это за место, Миссис Бакфетт..."
    melanie "Я видела его..."
    img 20645
    with vpunch
    m "Ты была там?!"
    m "Ты видела это... это место...?"
    m "Оно действительно такое, как говорит Маркус?!"
    sound highheels_short_walk
    img 20646
    with fade
    melanie "Да, Миссис Бакфетт..."
    melanie "Оно... Даже хуже..."
    melanie "И вскоре Вы отправитесь туда..."
    music Power_Bots_Loop
    img 20647
    with hpunch
    m "Нет! Я не отправлюсь туда, никогда!"
    music Villainous_Treachery
    img 20648
    with fade
    melanie "Вы отправитесь... И будете делать что Вам скажут..."
    melanie "Вы будете умолять о том, чтобы оказаться на обложке их журнала..."
    music Power_Bots_Loop
    img 20649
    with diss
    m "Я знаю что там за журнал!"
    m "Я не буду умолять об этом!"
    music Villainous_Treachery
    img 20650
    with fade
    melanie "Будете, как и остальные девушки, которые находятся там."
    melanie "Вы будете удивлены, когда увидите КОГО там можно встретить среди них..."
    melanie "У наших хозяев действительно хороший вкус..."
    img 20651
    with diss
    m "Наших хозяев?!"
    img 20652
    with fade
    melanie "Но Вам не удастся добиться ничего..."
    melanie "Вы упустили свой шанс."
    img 20653
    with diss
    melanie "Теперь Вы попадете туда в качестве..."
    img 20654
    with diss
    melanie "Я не буду об этом..." # Отворачивается
    img 20655
    with fade
    m "Нет, Мелани! Я лучше умру!"
    img 20656
    with diss
    melanie "Миссис Бакфетт..."
    melanie "Я видела там вещи..."
    img 20657
    with diss
    melanie "Вещи... которые похуже смерти..."
    img 20658
    with vpunch
    m "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music In_Your_Arms
    img 20659
    with fadelong
    melanie "Выпейте вина, Миссис Бакфетт..."
#    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.5
    show screen camera_viewfinder_screen()
    sound camera_lens1
    img 20660 # photo
    with Dissolve(0.2)
    w
    sound camera_lens1
    img 20661
    with Dissolve(0.2)
    w
    sound camera_lens1
    img 20662 #photo
    with Dissolve(0.2)
    w
    call photoshop_flash() from _call_photoshop_flash_150
    w

    #
    music stop
    img black_screen
    hide screen camera_viewfinder_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20663
    with fadelong
    m "Итак, Мелани."
    m "Почему ты утверждаешь что я обязательно попаду туда?"
    music Power_Bots_Loop
    img 20664
    with vpunch
    m "Ты что, заодно с этими людьми?"
    music Groove2_85
    img 20665
    with fade
    melanie "Нет, Миссис Бакфетт."
    melanie "Я на Вашей стороне..."
    img 20666
    with diss
    m "Но как? Как ты выбралась оттуда?!"
    music Master_Disorder
    img 20667
    with fade
    melanie "Я... не выбралась оттуда, Миссис Бакфетт..."
    img 20668
    with diss
    melanie "Оттуда невозможно выбраться..."
    music Power_Bots_Loop
    img 20669
    with fade
    m "Но ты сидишь здесь, передо мной!"
    music Master_Disorder
    img 20670
    with diss
    melanie "Миссис Бакфетт..."
    melanie "Я была глупа и думала что весь мир принадлежит мне."
    melanie "Что я могу добиться любой цели и поставить на колени любого мужчину..."
    m "..."
    img 20672
    with diss
    melanie "Я ошибалась..."
    melanie "Есть мужчины, которые гораздо сильнее меня..."
    img 20671
    with diss
    melanie "И, все на что хватило моих сил - это убедить их в том, что пока я полезнее здесь."
    img 20673
    with diss
    melanie "Нежели там..."
    melanie "Потому я не проходила тех тренировок, которые проходят все, кто попадает туда."
    img 20674
    with diss
    m "..."
    img 20675
    with fade
    melanie "Это бы..."
    melanie "Это бы изменило меня..."
    melanie "И я бы не смогла быть в той форме, чтобы сохранять эффективность здесь..."
    melanie "По эту сторону Фермы 218..."
    img 20676
    with hpunch
    m "!!!"
    music Villainous_Treachery
    img 20677
    with fade
    melanie "Но меня могут вернуть туда в любой момент..."
    melanie "Например, если я вдруг стану помогать Вам..."
    melanie "Для меня большой риск даже просто говорить с Вами, Миссис Бакфетт..."
    music Groove2_85
    img 20678
    with fadelong
    m "Мелани! Все что ты говоришь..."
    m "Этот Маркус..."
    m "Ведь он всего-лишь полицейский!"
    img 20679
    with diss
    m "Ведь есть законы, есть пресса."
    m "Есть здравый смысл, в конце концов!"
    img 20680
    with fade
    m "Я была шокирована после того что случилось и действительно испугалась этих людей."
    m "Но сейчас понимаю, что это все выглядит настолько нереально, что просто не может быть правдой!"
    img 20681
    with diss
    m "Может быть обратиться в другой полицейский участок или в организацию, которая выше?"
    m "Пойти к другому адвокату, обратиться за получением новых документов..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Master_Disorder
    img 20682
    with fadelong
    melanie "Миссис Бакфетт..."
    melanie "Вы имели деньги и власть."
    img 20683
    with diss
    melanie "Неужели Вы не поняли как устроен этот мир?"
    melanie "Вы говорите про законы?"
    music Power_Bots_Loop
    img 20684
    with fade
    m "Да, Мелани! Я говорю про законы!"
    sound snd_bodyfall
    img 20685
    with diss
    m "Эта ферма! Это какое-то безумие! Произвол!"
    m "Это нарушение всех мыслимых норм!"
    music Master_Disorder
    img 20686
    with fadelong
    melanie "Миссис Бакфетт."
    melanie "Закон - это лишь инструмент для управления теми, у кого нет власти."
    melanie "Для тех, у кого есть деньги и власть, закон не существует..."
    music Groove2_85
    img 20687
    with diss
    m "Это неправда, Мелани!"
    m "Даже богача можно засадить за решетку!"
    melanie "Да, Миссис Бакфетт, можно..."
    melanie "Но..."
    #
    music stop
    img black_screen
    with diss
    pause 1.5
#    music Groove2_85
    music Loved_Up
    img 20688
    with fadelong
    melanie "Представьте, что Ваш водитель задавил собачку."
    melanie "Хозяин собачки оказался обычным человеком."
    melanie "Закон бы действовал на Вас?"
    img 20689
    with diss
    melanie "Нет. Вы бы позвонили Дику и во всем виноват оказался бы обычный человек."
    melanie "А если бы это оказалась собачка Виктории, его секретаря?"
    sound highheels_short_walk
    img 20690
    with fade
    m "!!!"
    img 20691
    with diss
    melanie "Тогда бы закон работал как обычно."
    melanie "Вы бы заплатили компенсацию..."

#    m "!!!"
    sound Jump1
    img 20692
    with diss
    melanie "Все потому, что появился бы другой человек, также имеющий власть."
    melanie "И закон в его руках был бы просто интрументом."

    img 20693
    with diss
    melanie "Миссис Бакфетт, закон работает только для равных..."
    melanie "Вы сейчас можете забыть про это..."
    m "И ты хочешь сказать что Маркус..."

    sound Jump1
    img 20694 # Мелани нагибается
    with diss
    w
    sound Jump2
    img 20695
    with diss
    melanie "Да, Миссис Бакфетт."
    melanie "Мистер Маркус - это очень... очень большой человек..."
#    sound snd_back1
    sound Jump1
    img 20696
    with diss
    m "Большой человек, который работает простым полицейским?"

    music Groove2_85
    sound highheels_short_walk
    img 20697
    with fadelong
    melanie "Мистер Маркус не является частью системы, Миссис Бакфетт..."
    melanie "Он использует ее, потому что этого хочет."
    melanie "Так ему удобнее... Быть полицейским..."

    music Power_Bots_Loop
    img 20698
    with vpunch
    m "Он просто мерзавец! И все!"
    music Master_Disorder
    img 20699
    with fadelong
    melanie "Нет, Миссис Бакфетт."
    melanie "Я не считаю его мерзавцем."
    m "Почему, Мелани?!"
    m "Как ты можешь оправдывать его?!"

    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    img 20700
    with fadelong
    melanie "Миссис Бакфетт."
    melanie "Мистер Маркус - это мужчина."
    melanie "Мужчина, который имеет силу и власть поступать так как он хочет."
    melanie "Вы не встречали таких сильных мужчин ранее..."
    melanie "И вот... встретили..."
    melanie "Впрочем и я тоже..."

    music Power_Bots_Loop
    img 20701
    with fade
    m "Силу? Власть?!"
    m "Он просто работает на каких-то безумных хозяев, которые делают немыслимые вещи!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Master_Disorder
    img 20702
    with fadelong
    melanie "Нет, Миссис Бакфетт."
    melanie "Мистер Маркус имеет свое мнение на все вопросы."
    melanie "Например, он помогает Вам вместо того, чтобы делать так, как его просят люди, стоящие за ним..."

    music Power_Bots_Loop
    img 20703
    with fade
    m "МАРКУС?! ПОМОГАЕТ?! МНЕ???"
    m "Маркус только и ждет, чтобы забрать меня!"

    music Master_Disorder
    img 20704
    with fadelong
    melanie "Все несколько иначе, Миссис Бакфетт..."
    melanie "Есть люди, которые стоят за Мистером Маркусом."
    melanie "Они тоже обладают огромном властью и влиянием."
    melanie "И они ждут Вас."
    img 20705
    with diss
    melanie "Дик нарушил их планы."
    melanie "Он хороший адвокат. Он имеет влияние и опыт, но..."
    m "Что НО...?"
    melanie "Проблемы, которые создают действия Дика, они..."
    img 20706
    with diss
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Villainous_Treachery
    img 20707
    with fadelong
    melanie "Они несколько преувеличены Мистером Маркусом в глазах людей, которые ждут Вас..."
    melanie "Мистер Маркус может забрать Вас в любой момент, Миссис Бакфетт..."
    img 20708
    with hpunch
    m "!!!"
    music Master_Disorder
    img 20709
    with diss
    melanie "Но, почему-то, он этого не делает..."
    music Power_Bots_Loop
    img 20710
    with diss
    m "Почему?!"
    m "Если он может забрать меня в любой момент, то почему он ждет от меня каких-то нарушений закона?!"
    music Master_Disorder
    img 20711
    with fade
    melanie "Вы нравитесь ему, Миссис Бакфетт."
    melanie "Он играет с Вами."
    melanie "Однако, если Вы действительно нарушите хоть что-то, ему придется забрать Вас."
    melanie "На него давят люди, которые стоят за ним."
    img 20712
    with diss
    melanie "Они очень ждут, чтобы попробовать Вас... в деле..."
    m "!!!"
    img 20713
    with fadelong
    melanie "Это как кот, который играет с пойманной мышкой."
    melanie "Мышка пытается убежать, но у нее нет шансов, она уже поймана..."
    melanie "Радуйтесь тому, что у Вас есть какое-то время до того, пока с Вами наиграются..."
    melanie "Итог один. В конце концов, Вы окажетесь в том месте..."
    music Power_Bots_Loop
    img 20714
    with hpunch
    m "!!!"

    img 20715
    with fade
    m "Я не верю..."
    m "Этого не может быть..."
    m "Должен быть какой-то выход..."

    img 20716
    with diss
    m "..."
    music stop
    img black_screen
    with diss
    pause 2.0
    music Hidden_Agenda
    img 20717
    with fadelong
    m "Мелани, я признаю что ты в чем-то разбираешься больше меня..."
    m "Подскажи, что мне делать. Как выбраться из всего этого?"

    sound snd_bodyfall
    music Loved_Up
    img 20718 # толкает
    with diss
    w
    sound Jump1
    img 20719
    with fade
    melanie "Вам не выбраться из этого, Миссис Бакфетт."
    melanie "Я советую Вам затянуть эту игру."
    img 20720
    with diss
    melanie "Создайте для Мистера Маркуса дополнительный интерес к Вам."
    melanie "Проявите инициативу."
    img 20721
    with fade
    m "Что ты имеешь ввиду, Мелани?"
    m "Какую инициативу я должна проявить?"

    img 20722
    with diss
    melanie "Придите к нему, придите к Мистеру Маркусу."
    img 20723
    with diss
    melanie "Постарайтесь понравиться ему."
    img 20724
    with fade
    melanie "Не бегайте от него, ведь он помогает Вам."
    music Power_Bots_Loop
    img 20725
    with fade
    m "Придти к человеку, который лишил меня всего?!"
    m "И, при этом, пытаться понравиться ему?!"
    music Master_Disorder
    img 20726
    with fade
    melanie "Да, это не поможет Вам избежать участи."
    melanie "Но может помочь попасть на ферму в качестве той, кто согласилась на это добровольно."
    melanie "Вы, возможно, сможете исправить совершенную ошибку..."
    sound Jump1
    music Loved_Up2
    img 20727 #Мелани залезает
    with diss
    w
    music Power_Bots_Loop
    sound plastinka2
    img 20728
    with vpunch
    m "Мелани, за кого ты принимаешь меня?!"
    m "Я что, по твоему, сошла с ума?!"

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20729
    with fadelong
    melanie "Миссис Бакфетт."
    melanie "Я могу сказать Вам честно."
    melanie "Я считала Вас надменной дурой, которой богатство и власть достались благодаря случайности."

    img 20730
    with diss
    m "..."

    img 20731
    with fade
    melanie "Когда с Вами произошли изменения, Я даже не представляла с чем Вы столкнулись."
    melanie "Сейчас, зная про Вас все, я могу сказать что восхищаюсь Вами."
    melanie "В борьбе за свою свободу Вы проявляете такую волю и характер, что..."
    img 20732
    with diss
    melanie "Что я начинаю считать Вы заслуживали то положение, которое имели..."

    img 20733
    with diss
    m "..."

    img 20734
    with fade
    melanie "Потому я искренне желаю удачи Вам."
    img 20735
    with diss
    m "И ты не винишь меня в том что случилось с тобой?"
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Power_Bots_Loop
    img 20736
    with fadelong
    melanie "..."
    img 20737
    with hpunch
    melanie "Я ненавижу Вас за это, Миссис Бакфетт."


    img 20738
    with diss
    m "Ты ненавидишь меня, но помогаешь мне?"

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20739
    with fadelong
    melanie "Я пытаюсь извлечь выгоду даже из этой безнадежной ситуации."
    melanie "Я умею справляться со своими эмоциями..."
    img 20740
    with diss
    m "Спасибо, Мелани."

    music Master_Disorder
    img 20741
    with fade
    melanie "Вы сниметесь в костюме черного лебедя..."

    music Groove2_85
    img 20742
    with diss
    m "Что? Мелани, про что ты говоришь?"

    img 20743
    with fade
    melanie "Биф. Он заставляет меня сниматься в костюме черного лебедя."
    melanie "Мне не уйти из этой компании сейчас, Миссис Бакфетт."
    melanie "Но я не хочу проходить эту фотосессию."

    music Hidden_Agenda
    img 20744
    with diss
    m "У этого костюма нет трусиков..."
    music Groove2_85
    img 20745
    with fade
    melanie "Да, именно."
    melanie "И Вы пройдете эту фотосессию вместо меня, Миссис Бакфетт."

    music Power_Bots_Loop
    img 20746
    with diss
    m "Мелани, ты сошла с ума?!"
    m "Я не буду сниматься в таком виде!"

    music Villainous_Treachery
    img 20747
    with fade
    melanie "Вы будете, Миссис Бакфетт."
    melanie "Иначе, клянусь, Вы отправитесь к Маркусу очень скоро!"
    melanie "Помочь Вам очень сложно, а сделать наоборот очень легко..."

    img 20748
    with diss
    m "!!!"

#    melanie "Но я умею справляться со своими эмоциями..."
#    m "Мелани, спасибо. Я подумаю над твоими словами."

    img 20749
    with fade
    melanie "А сейчас Вы можете идти, Миссис Бакфетт."
    melanie "Я не хочу рисковать и далее, общаясь с Вами..."


    menu:
        "Попросить деньги у Мелани.":
            music Hidden_Agenda
            m "Мелани."
            m "Раз уж ты желаешь мне удачи..."
            m "Скажи, у тебя ведь есть деньги?"
            melanie "У меня достаточно денег, Миссис Бакфетт."
            img 20750
            with fade
            m "Могла бы ты мне немного одолжить..."
            melanie "Нет, Миссис Бакфетт. Я не собираюсь рисковать, помогая Вам..."
            m "Я поняла, Мелани. Всего хорошего."
            melanie "Всего хорошего, Миссис Бакфетт..."
            $ monicaAskMoneyFromMelanie = True
        "Уйти.":
            pass


    return


label ep27_dialogues1_melanie3:
    mt "У меня очень смешанные чувства после разговора с Мелани."
    mt "Она убеждена, что мне не уйти от Маркуса."
    mt "..."
    mt "И этот ее совет, придти к нему."
    mt "Меня охватывает ужас от одной мысли снова увидеть этого человека..."
    return


label ep27_dialogues1_melanie4:
    mt "Мелани говорила что ей опасно общаться со мной."
    mt "Думаю, пока лучше не рисковать приближаться к ней..."
    return False





















#
