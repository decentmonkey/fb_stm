# при условии, что у Барди достигнут максимальный уровень (8-?) и были сцены с одноклассником и не запущен ревендж-квест
# после уборки Барди ловит Монику

#call ep212_dialogues1_bardie_ralph1() # разговор с Барди с подвале
#call ep212_dialogues1_bardie_ralph2() # Моника думает после разговора с Барди
#call ep212_dialogues1_bardie_ralph3() # Моника 1-й раз приходит убираться в гостиную, меню
#call ep212_dialogues1_bardie_ralph4() # Моника убирается в трусиках Юлии
#call ep212_dialogues1_bardie_ralph5() # разговор с Барди после 1-й уборки
#call ep212_dialogues1_bardie_ralph6() # мысли Моники после ухода Барди
#call ep212_dialogues1_bardie_ralph7() # Моника 2-й раз приходит убираться в гостиную, мысли
#call ep212_dialogues1_bardie_ralph8() # Моника убирается в трусиках Бетти
#call ep212_dialogues1_bardie_ralph9() # разговор с Барди после 2-й уборки
#call ep212_dialogues1_bardie_ralph10() # мысли Моники после ухода Барди
#call ep212_dialogues1_bardie_ralph11() # Моника 3-й раз приходит убираться в гостиную
#call ep212_dialogues1_bardie_ralph12() # Моника убирается без трусиков
#call ep212_dialogues1_bardie_ralph13() # разговор с Барди после 3-й уборки
#call ep212_dialogues1_bardie_ralph14() # мысли Моники после ухода Барди

label ep212_dialogues1_bardie_ralph1:

    return

label ep212_dialogues1_bardie_ralph2:

    return

label ep212_dialogues1_bardie_ralph3: # Моника приходит убираться в гостиную
    # не рендерить
    if monicaBardieRalphSeducingStage == 1:
        call ep00_dialogues_ralph1()
        $ menu_corruption = [ep212_seduce_ralph1]
    if monicaBardieRalphSeducingStage == 2:
        $ menu_corruption = [ep212_seduce_ralph2]
    if monicaBardieRalphSeducingStage == 3:
        $ menu_corruption = [ep212_seduce_ralph4]
    menu:
        "Соблазнять Ральфа.":
            return True
        "Убираться как обычно.":
            return False
#    menu:
#        "Убираться на виду Ральфа в трусиках Юлии.":
#            pass
#        "Убираться на виду Ральфа в трусиках Бетти.":
#            pass
#        "Убираться на виду Ральфа без трусиков":
#            pass

label ep212_dialogues1_bardie_ralph3a: # Моника приходит убираться в гостиную в первый раз
    mt "Вот и Ральф..."
    mt "Легкая жертва для такой красивой девушки как я..."
    mt "Уверена, что он никогда не сталкивался с красотой, подобной моей..."
    mt "И даже не подозревает, как он уязвим и жалок..."
    mt "Я специально скрывала свою женственность, чтобы он не вздумал ко мне приближаться!"
    mt "Но теперь он - моя жертва!"
    mt "И я верну назад этот дом!"

    # если нет трусиков или одеты трусики Бетти
    if monicaUnder == "Nude":
        mt "Однако, не думаю что стоит делать это без трусиков."
        return False
    if monicaBettyPanties == True:
        mt "Однако, не думаю что стоит делать это в трусиках Бетти."
        mt "Для такого как он будет достаточно надеть [трусики Юлии]..."
        mt "[Они в прачечной около бассейна.]"
        mt "Сделаю это в следующую уборку."
        return False
    #
    return True


label ep212_dialogues1_bardie_ralph4: # Моника убирается в трусиках Юлии
    # не рендерить
    music stop high
    scene black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda high
    img 23765
    with fadelong
    mt "Мистер Робертс, разрешите мне убрать в этой комнате?"
    ralph "Конечно, Моника. Можешь убираться."

label ep212_dialogues1_bardie_ralph4a: # Моника убирается в трусиках Юлии
    # Ральф уперся в книгу и не замечает Монику
    if obj_name == "Chair3":
        img 23766
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23767
        with diss
        mt "Он смотрит или нет?"

    if obj_name == "Chair4":
        img 23768
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23769
        with diss
        mt "Ну же!"

    if obj_name == "Sofa":
        img 23770
        with fade
        mt "Мистер Робертс, я протру и здесь тоже!"
        $ cleaning_sound()
        img 23771
        with diss
        ralph "Да, Моника. Протирай везде..."

    if obj_name == "TableLamp1":
        img 23772
        with fade
        $ cleaning_sound()
        mt "Он что, даже не смотрит?!"
    return

label ep212_dialogues1_bardie_ralph4b:
    img black_screen
    with diss
    pause 1.5
    $ cleaning_sound()
    img 23773
    with diss
    w
    $ cleaning_sound()
    img 23774
    with fade
    w
    $ cleaning_sound()
    img 23775
    with diss
    mt "Я не понимаю..."

    $ restore_music()
    # Конец
    music Groove2_85
    sound highheels_short_walk
    img 23776
    with fade
    mt "Мистер Робертс, я закончила уборку здесь..."
    ralph "Да, Моника, конечно. Можешь продолжать уборку в других комнатах."

    img 23777
    with diss
    sound highheels_short_walk
    mt "Как же так?"
    mt "Я вертелась перед ним все время, а он даже не оторвался от своей дурацкой книги!"
    mt "Что за жалкий представитель мужской фауны?"

    return

label ep212_dialogues1_bardie_ralph5: # После уборки

    return

label ep212_dialogues1_bardie_ralph6: # autorun

    return


label ep212_dialogues1_bardie_ralph7: # Моника приходит убираться в гостиную 2-ой раз
    # не рендерить
    mt "Вот и Ральф..."
    mt "Похоже он слепой, как крот, раз не обратил внимание на меня в прошлый раз..."
    mt "Но, в трусиках Бетти, он меня явно заметит."
    mt "У него нет никаких шансов устоять против меня..."

    if monicaBettyPanties != True:
        # если нет трусиков или одеты трусики Юлии
        mt "Мне надо будет [надеть трусики Бетти]."
        mt "Сделаю это в следующую уборку."
        return False
    #
    return True

label ep212_dialogues1_bardie_ralph8: # Моника убирается в трусиках Бетти
    # не рендерить
    music stop high
    scene black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda high
    img 23778
    with fadelong
    mt "Мистер Робертс, разрешите мне убрать в этой комнате?"
    ralph "Конечно, Моника. Можешь убираться."

label ep212_dialogues1_bardie_ralph8a:
    $ monicaBettyPantiesOverlayId = monicaBettyPantiesId - 1
    if obj_name == "Chair3":
        img 23779 #over1, over2, over3, over4
        overlay 23779 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        mt "Трусики Бетти должны сработать..."
        $ cleaning_sound()
        img 23780
        with diss
        w

    if obj_name == "Chair4":
        img 23781 #over1, over2, over3, over4
        overlay 23781 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23782
        with diss
        mt "Смотрит он или нет?"
        img 23783 #over1, over2, over3, over4
        overlay 23783 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        w

    if obj_name == "Sofa":
        $ cleaning_sound()
        img 23786 #over1, over2, over3, over4
        overlay 23786 monicaBettyPantiesOverlayId
        with fade
        m "Мистер Робертс, скажите, здесь тоже на протирать в этот раз?"
        $ cleaning_sound()
        img 23785
        with diss
        ralph "Да, Моника протирай везде и тщательно..."
        img 23784 #over1 over2 over3 over4
        overlay 23784 monicaBettyPantiesOverlayId
        with diss
        w

    if obj_name == "TableLamp1":
        img 23789 #over1, over2, over3, over4
        overlay 23789 monicaBettyPantiesOverlayId
        with fade
        $ cleaning_sound()
        w
        $ cleaning_sound()
        img 23787 # over1, over2, over3, over4
        overlay 23787 monicaBettyPantiesOverlayId
        with diss
        w
        $ cleaning_sound()
        img 23788
        with diss
        mt "Он что, не смотрит?!"
    return

label ep212_dialogues1_bardie_ralph8b:
    img black_screen
    with diss
    pause 1.5
    $ cleaning_sound()
    img 23790 # over1, over2, over3, over4
    overlay 23790 monicaBettyPantiesOverlayId
    with fade
    w
    $ cleaning_sound()
    img 23791
    with diss
    w
    $ cleaning_sound()
    img 23792 #over1, over2, over3, over4
    overlay 23792 monicaBettyPantiesOverlayId
    with diss
    mt "Да он совсем обнаглел?!"
    mt "Как можно не смотреть на то что перед ним?!"

    $ menu_corruption = [ep212_seduce_ralph3]
    menu:
        "Убираться перед Ральфом.":
            pass
        "Закончить уборку.":
            return False
    # подходит к Ральфу
    sound highheels_short_walk
    img 23793
    with fade
    m "Мистер Робертс, разрешите я здесь тоже протру, я вижу пыль..."
    ralph "Да, Моника, конечно, можешь протирать..."

    $ cleaning_sound()
    img 23794
    with diss
    w
    $ cleaning_sound()
    img 23795 #over1, over2, over3, over4
    overlay 23795 monicaBettyPantiesOverlayId
    with fade
    w
    $ cleaning_sound()
    img 23796 #iover1, over2, over3, over4
    overlay 23796 monicaBettyPantiesOverlayId
    with diss
    mt "Он что, снова пялится в свою книгу, а не на меня?!"
    $ restore_music()
    music Groove2_85
    img 23797
    with diss
    mt "Да как он смеет?!"
    mt "Как такое вообще возможно?!"
    mt "Перед ним самая красивая девушка этого города!"
    mt "Он что, импотент?!"

label ep212_dialogues1_bardie_ralph8c:
    sound highheels_short_walk
    music Groove2_85
    img 23776
    with fade
    mt "Мистер Робертс, я закончила уборку здесь..."
    ralph "Да, Моника, конечно. Можешь продолжать уборку в других комнатах."
    return True


label ep212_dialogues1_bardie_ralph9: # После второй уборки

    return

label ep212_dialogues1_bardie_ralph10: #autorun
    # не рендерить

    return


label ep212_dialogues1_bardie_ralph11: # Моника приходит убираться в гостиную 3-ий раз
    # не рендерить
    music Groove2_85
    sound highheels_short_walk
    img 23799
    with fadelong
    mt "Вот и Ральф..."
    mt "Этот гребаный импотент."
    img 23798
    with fade
    mt "Мне придется пойти на крайнюю меру, чтобы соблазнить его..."
    mt "Но это того стоит!"
#    mt "Вот-вот я верну себе этот дом и избавлюсь от надоедливой малявки!"
    img 23800
    with diss
    mt "Похоже он слепой, как крот, раз не обратил внимание на меня в прошлый раз..."
    mt "Но, без трусиков, он меня явно заметит."
    mt "У него нет никаких шансов устоять против моих женственных форм..."

    # если одеты любые трусики
    if monicaUnder != "Nude":
        mt "Мне надо будет [придти без трусиков]."
        mt "Сделаю это в следующую уборку."
        return False
    #
    return True

label ep212_dialogues1_bardie_ralph12: # Моника убирается без трусиков
    # не рендерить
    music stop
    scene black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Hidden_Agenda high
    img 23801
    with fadelong
    mt "Мистер Робертс, разрешите мне убрать в этой комнате?"
    ralph "Конечно, Моника. Можешь убираться."
    return

label ep212_dialogues1_bardie_ralph12a:
    music Loved_Up high
    if obj_name == "Chair3":
        $ imgArr = [23802, 23803, 23804]

    if obj_name == "Chair4":
        $ imgArr = [23805, 23806, 23807]

    if obj_name == "Sofa":
        $ imgArr = [23808, 23809, 23810]

    if obj_name == "TableLamp1":
        $ imgArr = [23811, 23812, 23813]

    if monicaBardieRalphSeducingCleaningItemsCount == 4:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        mt "Ну что, Моника..."
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Ты задействовала самое сильное оружие, которое у тебя есть..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        w

    if monicaBardieRalphSeducingCleaningItemsCount == 3:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        w
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Ни один мужчина в мире не устоит перед таким..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        w
    if monicaBardieRalphSeducingCleaningItemsCount == 2:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        mt "Черт! Не могу поверить что я делаю это..."
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Соблазняю свой голой попой какого-то старикашку..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        mt "В своем совственном доме!"
        mt "Ужас!"
    if monicaBardieRalphSeducingCleaningItemsCount == 1:
        img imgArr[0]
        with fade
        $ cleaning_sound()
        w
        img imgArr[1]
        with diss
        $ cleaning_sound()
        mt "Но мне надо сделать это!"
        mt "Я в шаге от того чтобы вернуть мой дом назад..."
        $ cleaning_sound()
        img imgArr[2]
        with diss
        w
    return

label ep212_dialogues1_bardie_ralph12b:
    # autorun
    mt "Мне надо привлечь его внимание..."
    return False

label ep212_dialogues1_bardie_ralph12c:
    music stop high
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda high
    img 23814
    with fade
    m "Мистер Робертс, скажите, здесь тоже протирать?"
    ralph "Да, Моника, протирай везде..."
    img 23815
    with diss
    w
    img 23816
    with fade
    w
    $ restore_music()
    music Groove2_85
    img 23817
    with diss
    mt "Дьявол! Он даже не смотрит!"
    mt "Не смотрит на то, что ему показывает самая чуть-ли ни самая красивая девушка в этом мире!"
    mt "Сама Моника Бакфетт соблазняет его!"
    mt "А он не смотрит! Урод!"
    $ menu_corruption = [ep212_seduce_ralph5]
    menu:
        "Убираться перед Ральфом.":
            pass
        "Закончить уборку.":
            return False
    # подходит к Ральфу
    music Hidden_Agenda
    sound highheels_short_walk
    img 23818
    with fade
    m "Мистер Робертс, разрешите я здесь тоже протру, я вижу пыль..."
    ralph "Да, Моника, конечно, можешь протирать..."
    mt "Мне надо во что бы то ни стало заставить его посмотреть на меня!"

    img 23819
    with diss
    m "Спасибо, Мистер Робертс!"

    music Loved_Up
    img 23820
    with fade
    m "Скажите, здесь тоже протирать?"
    ralph "Да, Моника, протирай..."

    img 23821
    with diss
    m "А здесь?"
    img 23822
    with diss
    ralph "Да..."

    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 23823
    with fade
    m "И здесь тоже протирать?"
    img 23824
    with diss
    ralph "Да, Моника, протирай везде..."

    img 23825
    with fade
    w

    # Задевает книгу, она падает
    sound Jump2
    img 23826
    with diss
    w
    sound Jump1
    img 23827 #diss
    with diss
    w
    sound down10
    img 23828
    with diss
    # звук падения
    w
    m "Ой, Мистер Робертс, простите! Я случайно..."
    # поднимает книгу, показывая попу

    sound swish
    img 23829
    with fade
    # звук кладущегося дустера (которым протирает)
    w
    img 23830
    with diss
    m "Позвольте, я подниму Вашу книгу!"
    img 23831
    with diss
    mt "Он у меня почти в руках!"

    img 23832
    with fade
    w
    music stop
    img 23833
    with diss
    sound snd_boot1
    # звук наступает на ногу
    w
    sound scream_steve
    img 23834
    with vpunch
    # звук ральф кричит ай!
    w

    # дает ее
    music Loved_Up
#    music Groove2_85
    img 23835
    with fade
    m "Вот, Мистер Робертс, Ваша книга..."

    # Ральф встает
    # рендерить
    img 23836
    with diss
    ralph "Моника, мне надо с тобой поговорить..."
    music Stealth_Groover
    img 23837
    with diss
    mt "Все! Я сделала это!"
    mt "Он, наконец-то, обратил внимание на меня!"
    mt "Теперь ему никуда не деться, он мой!"
    mt "У него нет никаких шансов соскочить с моего крючка!"

    music Groove2_85
    img 23838
    with fade
    ralph "Моника, ты меня слышишь?"
    # улыбается заискивающе
    m "А? Да, Мистер Робертс, я Вас слушаю..."

    # строго
    img 23839
    with diss
    ralph "Моника, я давно заметил, что ты пытаешься обратить мое внимание на себя."
    ralph "С самого начала, как только ты начала работу здесь, ты проявляла интерес ко мне."
    img 23840
    with fade
    mt "Что? С самого начала?"
    mt "Это неправда!"

    img 23841
    with diss
    ralph "Бетти предупреждала меня об этом."
    ralph "Да и это, в общем, неудивительно."
    ralph "Такая молодая девушка как ты, без хорошего дохода."
    ralph "Конечно такой роскошный дом произведет на тебя впечатление."
    ralph "И ты попытаешься воспользоваться своими внешними данными, чтобы остаться здесь в качестве хозяйки."

    img 23842
    with fade
    mt "Что он имеет ввиду?"
    mt "Это он так пытается сказать что от меня без ума?!"

    img 23843
    with diss
    ralph "Я заверил Бетти что ты хорошая девушка и не станешь вести себя как все..."
    ralph "Однако, я ошибся..."
    ralph "И из всех способов, соблазнить хозяина дома, ты выбрала самый вульгарный..."
    ralph "Сначала ты пыталась соблазнить меня видом моих трусиков."
    mt "!!!"
#    ralph "Затем решила использовать трусики Бетти..."
#    music stop
#    sound plastinka1b
#    img 23845
#    with hpunch
#    mt "ЧТО?! ОН УЗНАЛ ИХ?!"

#    music Groove2_85
#    img 23844
#    with fade
#    ralph "У тебя на лице удивление?"
#    ralph "Да, я узнал их."
#    ralph "Я очень люблю все то, что носит Бетти."
#    ralph "И для меня удивительно, как гувернантка позволила себе одеть белье супруги своего работодателя."
    img 23846
    with diss
    m "!!!"
    img 23847
    with fade
    ralph "Конечно ты сделала это без спроса, но сделала всего один раз."
    ralph "Посчитаем это досадным недоразумением..."
    ralph "Я могу понять то, что тобой двжут корыстные мотивы."
    ralph "И ради них ты готова пойти на то, чтобы демонстрировать себя без всякого стыда..."
    ralph "Я знаю что моральные устои современных девушек, твоего возраста, далеки от тех идеалов к которым я привык..."
    ralph "Однако, я бы не хотел терпеть это в своем доме..."
    img 23848
    with diss
    m "!!!"
    img 23849
    with fade
    ralph "Давай ты мне пообещаешь, что больше не будешь так делать."
    ralph "И мы вместе забудем о том что здесь только что было..."
    ralph "Ты согласна со мной?"
    mt "!!!"
    # стоит потупившись
    music Hidden_Agenda
    img 23850
    with diss
    m "Да, Мистер Робертс... Я согласна..."
    ralph "Я не скажу об этом Бетти..."
    ralph "Я боюсь ее реакции на подобные вещи..."
    # сжимается (есть поза в артах рука на голове)
    img 23851
    with fade
    ralph "Ты ведь знаешь, что Бетти такая строгая..."
    ralph "Скорее всего, учитывая какого она мнения о тебе, тебе придется быть уволеной отсюда..."
    music Pyro_Flow
    img 23852
    with diss
    mt "Я никогда не чувствовала себя так глупо!!!"
    mt "Моника, какой кошмар!"
    mt "Тебя отчитывают за аморальное поведение в своем же собственном доме!"
    mt "Как до такого могло дойти?!"
    mt "Я не могу поверить что нахожусь здесь!"
    mt "Мне хочется провалиться сквозь землю..."
    music Groove2_85
    img 23853
    with fade
    m "Да, Мистер Робертс... Я поняла..."
    m "Простите, Мистер Робертс... Такого больше не повториться..."
    img 23854
    with diss
    ralph "Хорошо, Моника. Можешь быть свободна."
    sound highheels_short_walk
    img 23855
    with fade
    m "Спасибо, Мистер Робертс..."
    return True



label ep212_dialogues1_bardie_ralph13: # После третьей уборки

    return

label ep212_dialogues1_bardie_ralph14: # autorun
    # не рендерить
    mt "Не могу поверить что у меня не сработало!"
    mt "Меня отчитали как какую-то шлюху!"
    mt "Я не шлюха, которая пыталась переспать с хозяином, чтобы занять место жены!"
    mt "Я... Я лишь хотела восстановить справедливость!"
    mt "Если бы этот никчемный старикашка только знал кого он отчитывает!"
    mt "Мерзавец!"
    mt "Бесполезный, никчемный неудачник!"
    return
