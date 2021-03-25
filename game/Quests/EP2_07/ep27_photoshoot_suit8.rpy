default photoshoot8_count = 0
default photoshoot8_melanie_forced = False # Мелани принуждает Монику делать фотосессию
default photoshoot8_nude_completed = False # Монику сфотографировали полностью

label ep27_photoshoot_suit8:
    music Groove2_85
    $ shotsAmount = PS8_shots_amount
    $ shotsTotalAmount = 24

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
#    m "Алекс, у этого наряда нет трусиков."
    img 20509
    with fadelong
    m "Алекс, у этого наряда неполная комплектация."
    m "Я не смогла найти трусиков!"
    m "Их забыли положить?"
    img 20510
    with diss
    alex_photograph "Нет, Миссис Бакфетт!"
    alex_photograph "У этого наряда абсолютно полная комплектация!"
    alex_photograph "И мне она очень нравится!"
    alex_photograph "Вы выглядите просто восхитительно!"

    music Power_Bots_Loop
    img 20511
    with hpunch
    m "ТЫ СОШЕЛ С УМА, АЛЕКС?!"
    m "Я НЕ СОБИРАЮСЬ СНИМАТЬСЯ БЕЗ ТРУСИКОВ!!!"

    music Groove2_85
    img 20512
    with fade
    alex_photograph "Миссис Бакфетт, но здесь есть трусики!"

    m "Их нет!"

    img 20513
    with diss
    alex_photograph "Они есть! Вот это украшение! Оно выполняет их роль!"

    img 20514
    m "Оно ничего не закрывает, Алекс!"

    img 20515
    with fade
    alex_photograph "Миссис Бакфетт, эти трусики соответстуют новому курсу журнала, который Вы сами одобрили!"
    alex_photograph "Мы задаем новый тренд, которому последуют многие девушки!"
    alex_photograph "Приступим к съемкам скорее! Мне уже нетерпится запечатлеть Вашу красоту на пленку!"

    music Power_Bots_Loop
    img 20516
    with vpunch
    m "Нет, Алекс!"
    m "Даже не мечтай! Я не буду сниматься голой!"

    music Groove2_85
    img 20517
    with fade
    alex_photograph "Но Миссис Бакфетт, это соответствует прогрессу серии фотосессий, о которой Вы договорились с Мистером Бифом!"

    music Hidden_Agenda
    img 20518
    with fadelong
    m "Еще... Еще рано для такого, Алекс!"

    img 20519
    with diss
    mt "Черт! Я знала что эти фотосессии доведут меня до такого!"
    mt "Но мне нужно еще время... Еще немного времени... Надо как-то оттянуть этот момент..."

    music Groove2_85
    img 20520
    with fade
    m "Нет, Алекс! Я не буду этого делать!"
    alex_photograph "Миссис Бакфетт, Вы отказываетесь от фотосессии?"
    alex_photograph "Мне сообщить Мистеру Бифу?"

    music Hidden_Agenda
    img 20521
    with diss
    m "Алекс... Я не отказываюсь..."
    m "Но мне надо немного времени... Подготовиться."
    m "Давай пока сделаем фотосессию в другом... костюме..."

    # выход, если Мелани не здесь
    if photoshoot8_melanie_forced == False:
        help "Ожидание прогресса истории с Мелани."
        return False

    # если Мелани здесь

    music Master_Disorder
    img 20522
    with fadelong
    melanie "Миссис Бакфетт..."

    img 20523
    with diss
    mt "!!!"


    img 20524
    with diss
    w

    img 20525
    with fade
    melanie "Миссис Бакфетт, Вам стоит согласиться..."

    img 20526
    with diss
    $ menu_corruption = [PS8_monica_photoshoot8_agree]
    menu:
        "Согласиться на фотосессию.": #corruption
            pass
        "Отказаться.":
            music Hidden_Agenda
            img 20527
            with fade
            m "Алекс... Мелани..."
            m "Я... Я сделаю эту фотосессию..."
            m "Но мне нужно еще немного времени."
            music Master_Disorder
            img 20528
            with diss
            melanie "Не затягивайте, Миссис Бакфетт."
            return False

    mt "О БОЖЕ!"
    mt "Я снимаюсь на камеру... БЕЗ ТРУСИКОВ!"
    mt "ГОЛОЙ!"
    mt "Я не представляю как мне впоследствии оправдываться перед обществом за такие кадры..."
    mt "Может быть этот журнал не успеет распространиться до того как я верну свою власть?"
    mt "Я сделаю изъятие всех копий этих кадров, клянусь!"

    music Groove2_85
    img 20529
    with fadelong
    m "Хорошо, Алекс..."
    m "Я... Я сделаю эту фотосессию..."

    img 20530
    with fade
    alex_photograph "Миссис Бакфетт, не переживайте."
    alex_photograph "Это будет ограниченный выпуск журнала."
    alex_photograph "Он только для премиум подписчиков."
    alex_photograph "Остальной мир увидит Вашу фотосессию далеко не сразу!"

    m "..."

    alex_photograph "И у Вас вполне приличные трусики, Миссис Бакфетт!"
    alex_photograph "Они все закрывают так, что ничего не будет видно!"

    m "Ладно, Алекс."
    m "Только не снимай меня сзади..."
    m "И спереди тоже..."
    m "В общем, снимай так, чтобы ничего не было видно."
    m "Тебе понятно, Алекс?!"

    music Molten_Alloy
    img 20531
    with fade
    alex_photograph "Да, Мэм. Конечно!"
    alex_photograph "Итак, Мотор!"

    music stop
    img 20532
    with fadelong

label ep27_photoshoot_suit8_pose1:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose1"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose2"
    #кадр
    img 20532

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20536
        with fadelong
        music Groove2_85
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
        if corruption < PS8_monica_pose2_corruption_required:
            m "Алекс, я не буду вставать в эту позу, даже не надейся!"
            call corruption_required(PS8_monica_pose2_corruption_required) from _call_corruption_required_56
            return
        m "Алекс, снимай издалека!"
        alex_photograph "Конечно, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20533, 20534, 20535], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20533
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_186
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20534
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_187
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20535
        img photoImage
        with Dissolve(0.2)
        m "Алекс, не вздумай брать такой кадр!"
        m "У меня же там ничего нет!"
        if corruption < PS8_monica_shot1_corruption_required:
            call corruption_required(PS8_monica_shot1_corruption_required) from _call_corruption_required_57
            jump expression photoPoseLabel
        # если можно
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_188
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot1_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep27_photoshoot_suit8_pose2:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose2"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose3"
    #кадр+
    img 20536
    #up
#    20537
    #side
#    20538
    #down+
#    20539

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Molten_Alloy
        img 20540
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20537, 20538, 20539], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20537
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_189
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20538
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_190
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20539
        img photoImage
        with Dissolve(0.2)
        m "Алекс, я просила не снимать близко!"
        if corruption < PS8_monica_shot2_corruption_required:
            call corruption_required(PS8_monica_shot2_corruption_required) from _call_corruption_required_58
            jump expression photoPoseLabel
        # если можно
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_191
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot2_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep27_photoshoot_suit8_pose3:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose3"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose4"
    #кадр
    img 20540


    #up
#    20541
    #side

#    20543
    #down
#    20542

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Molten_Alloy
        img 20544
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20541, 20543, 20542], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20541
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_192
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20543
        img photoImage
        with Dissolve(0.2)
        m "Алекс, не вздумай брать такой кадр!"
        m "Ты что, сошел с ума?!"
        if corruption < PS8_monica_shot3_corruption_required:
            call corruption_required(PS8_monica_shot3_corruption_required) from _call_corruption_required_59
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_193
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot3_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20542
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_194
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep27_photoshoot_suit8_pose4:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose4"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose5"
    #кадр
    img 20544

    #up
#    20545
    #side+
#    20546
    #down+
#    20547

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Molten_Alloy
        img 20548
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music Groove2_85
        m "Алекс, я не собираюсь раздвигать ноги!"
        if corruption < PS8_monica_pose4_corruption_required:
            call corruption_required(PS8_monica_pose4_corruption_required) from _call_corruption_required_60
            return
        alex_photograph "Миссис Бакфетт, это всего-лишь образ!"
        alex_photograph "Не волуйтесь, ничего не видно!"
        m "Точно!?"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20545, 20546, 20547], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20545
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_195
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20546
        img photoImage
        with Dissolve(0.2)
        m "Алекс, не фотографируй сзади!"
        m "У меня же голый зад!"
        if corruption < PS8_monica_shot4_corruption_required:
            call corruption_required(PS8_monica_shot4_corruption_required) from _call_corruption_required_61
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я не буду приближать камеру."
        alex_photograph "Я фотографирую издалека!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_196
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot4_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20547
        img photoImage
        with Dissolve(0.2)
        m "Алекс, ты в своем уме?!"
        m "Ты хочешь сфотографировать мою... мою..."
        if corruption < PS8_monica_shot5_corruption_required:
            call corruption_required(PS8_monica_shot5_corruption_required) from _call_corruption_required_62
            jump expression photoPoseLabel
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        m "Точно?"
        alex_photograph "Да, Миссис Бакфетт! Уверяю Вас!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_197
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot5_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel



label ep27_photoshoot_suit8_pose5:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose5"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose6"
    #кадр+
    img 20548

    #up
#    20549
    #side+
#    20550

    #down+
#    20551

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20552
        with fadelong
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music Groove2_85
        m "Алекс, я не буду вставать в такую позу!"
        m "У меня голый зад! Абсолютно голый!"
        m "Алекс, ТЫ ЧТО, НЕ ПОНИМАЕШЬ МЕНЯ?!"
        alex_photograph "Миссис Бакфетт, у Вас прекрасная попа!"
        alex_photograph "Вам нечего стесняться показывать ее!"
        m "Алекс, вообще-то я Леди!"
        m "А Леди не показывают на камеру свой голый зад!"
        m "И я твой Босс, ты не забыл это?!"
    #
        if corruption < PS8_monica_pose5_corruption_required:
            call corruption_required(PS8_monica_pose5_corruption_required) from _call_corruption_required_63
            return
        alex_photograph "Миссис Бакфетт, не переживайте!"
        alex_photograph "Все-равно ничего не видно! Украшение дает блеск и засвечивает кадр!"
        m "Алекс, это точно?!"
        alex_photograph "Миссис Бакфетт, это абсолютно точно!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20549, 20550, 20551], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20549
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_198
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20550
        img photoImage
        with Dissolve(0.2)
        m "Алекс, там точно ничего не видно?"
        if corruption < PS8_monica_shot6_corruption_required:
            call corruption_required(PS8_monica_shot6_corruption_required) from _call_corruption_required_64
            jump expression photoPoseLabel
        alex_photograph "Не волнуйтесь, Миссис Бакфетт!"
        alex_photograph "Украшение все скрывает!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_199
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot6_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20551
        img photoImage
        with Dissolve(0.2)
        m "Алекс, что ты делаешь?!"
        m "Зачем ты снимаешь вблизи?!"
        if corruption < PS8_monica_shot7_corruption_required:
            call corruption_required(PS8_monica_shot7_corruption_required) from _call_corruption_required_65
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я фотографирую украшение."
        alex_photograph "Больше ничего не попадает в кадр!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_200
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot7_progress")
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep27_photoshoot_suit8_pose6:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose6"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose7"
    #кадр+
    img 20552

    #up
#    20553
    #side
#    20554
#    20555
    #down
#    20556

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20557
        with fadelong
        music Groove2_85
        m "Наконец-то нормальная поза."
        m "Алекс, до тебя, наконец-то дошло, что красота кроется не в развратных позах?"
        alex_photograph "Да, Миссис Бакфетт, я согласен с Вами!"
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20553, 20555, 20556], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20553
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_201
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20554
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_152
        w
        sound camera_lens1
        $ photoImage = 20555
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_202
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20556
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_203
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep27_photoshoot_suit8_pose7:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose7"
    $ photoPoseNextLabel = "ep27_photoshoot_suit8_pose8"
    #кадр
    img 20557
    #up
#    20559
    #side
#    20558
    #down
#    20560

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20561
        with fadelong
        music Groove2_85
        m "Алекс, ты точно сошел с ума!"
        m "Ты думаешь что я буду сниматься голой, да еще и раздвигать ноги?!"
        m "Ты не перепутал съемку на модный журнал и какое-нибудь порно?!"
        if corruption < PS8_monica_pose8_corruption_required:
            call corruption_required(PS8_monica_pose8_corruption_required) from _call_corruption_required_66
            return
        alex_photograph "Миссис Бакфетт, я буду снимать Вас только спереди!"
        alex_photograph "Положение Ваших ног лишь передает в кадр непринужденность."
        m "Непринужденность?!"
        m "Я лежу здесь голой задницей, раздвинув ноги!"
        m "Хорошо что сзади никого нет! Я не переживу этого стыда!"
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20559, 20558, 20560], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20559
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_204
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20558
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_205
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20560
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_206
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep27_photoshoot_suit8_pose8:
    $ photoPoseLabel = "ep27_photoshoot_suit8_pose8"
    #$ photoPoseNextLabel = "ep27_photoshoot_suit8_pose8"
    #кадр++
    img 20561

    #up
#    20562

    #side
#    20563 #fade

#    20564
#    20565
#    20566
#    20567
#    20568
#    m "Алекс!"
#    20569


    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        return
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot2([20562, 20569, 20586], PS8_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20562
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_207
        $ PS8_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20563
        with Dissolve(0.2)
        m "Ты куда пристроился, Алекс?!"
        alex_photograph "Миссис Бакфетт, мне надо сфотографировать Вас сверху!"
        m "Алекс, НЕТ!"
        m "Я же голая там!"
        if corruption < PS8_monica_shot8_corruption_required:
            call corruption_required(PS8_monica_shot8_corruption_required) from _call_corruption_required_67
            jump expression photoPoseLabel
        #
        alex_photograph "Миссис Бакфетт, я буду фотографировать только верхнюю часть."
        m "Ну.. Ладно..."
        m "Только не смотри ниже!"
        alex_photograph "Да, Миссис Бакфетт, конечно!"
        w
        call photoshop_flash() from _call_photoshop_flash_153
        w
        sound camera_lens1
        img 20564
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_154
        w
        sound camera_lens1
        img 20565
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_155
        w
        sound camera_lens1
        img 20566
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_156
        w
        sound camera_lens1
        img 20567
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_157
        w
        sound camera_lens1
        img 20568
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_158
        w
        m "Алекс!"
        sound camera_lens1
        $ photoImage = 20569
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_208
        $ PS8_shoots_array.append(photoImage)
        w
        $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot8_progress")
        jump expression photoPoseLabel
    if result == "down":
        #down
        music Groove2_85
        sound camera_lens1
        img 20570
        with Dissolve(0.2)
        m "Алекс, ты куда встал?!"
        alex_photograph "Миссис Бакфетт, мне надо сделать пару кадров Вашей обнаженной попы."
        m "ЧТО?! АЛЕКС!!!"
        m "ТЫ СОШЕЛ С УМА?!"
        alex_photograph "Это распоряжение Мистера Бифа."
        m "ЧТО?! Мне без разницы какие там Биф давал распоряжения!"
        m "Я не буду этого терпеть!"
        $ shotsAmountCompleted = len(list(set(PS8_shoots_array)))

        if shotsAmountCompleted < shotsTotalAmount-1: # Завершены не все кадры
            help "Необходимо сделать все предыдущие кадры..."
            return

        music Master_Disorder
        img 20571
        with fadelong
        melanie "Вы БУДЕТЕ это терпеть, Миссис Бакфетт."
        img 20572
        with diss
        m "Мелани?"
        melanie "Фотосессия должна быть завершена."
        melanie "Алекс, фотографируй так как посчитаешь нужным."
        melanie "Миссис Бакфетт, раздвиньте ноги и предоставьте Алексу доступ."

        music Hidden_Agenda
        img 20573
        with fade
        m "Алекс... Только..."
        m "Только так, чтобы ничего не было видно!"

        music Master_Disorder
        img 20574
        with fade
        melanie "Алекс, фотографируй так, чтобы было видно ВСЕ!"
        img 20575
        with diss
        melanie "Мистер Биф должен быть доволен."

        img 20576
        with diss
        m "!!!"

        music Loved_Up
        sound camera_lens1
        img 20577
        with Dissolve(0.2)
        w
        alex_photograph "О, Миссис Бакфетт!"
        alex_photograph "Как я мечтал рассмотреть Вашу киску поближе!"
        call photoshop_flash() from _call_photoshop_flash_159
        w
        sound camera_lens1
        img 20578
        with Dissolve(0.2)
        w
        alex_photograph "И Вашу попку!"
        call photoshop_flash() from _call_photoshop_flash_160
        w
        sound camera_lens1
        img 20579
        with Dissolve(0.2)
        w
        alex_photograph "Моя мечта сбылась!"
        call photoshop_flash() from _call_photoshop_flash_161
        w

        music Groove2_85
        img 20580
        with fadelong
        secretary "Мисс Мелани."
        secretary "Мистер Биф просил Вас зайти к нему!"
        melanie "Хорошо, я зайду к нему."

        music RnB4_100
        img 20581
        with fadelong
        secretary_t "Это что, очередная модель?" #думает
        secretary_t "Как ни стыдно! Эти модели готовы на все!"
        img 20582
        with diss
        secretary_t "Миссис Бакфетт никогда бы не позволила так вести себя!"

        music Groove2_85
        img 20583
        with fade
        melanie "Ты можешь идти..."
        secretary "А? Да, конечно..."
        sound highheels_run1
        music stop
        img black_screen
        with diss
        pause 3.0
        music Loved_Up2
        sound camera_lens1
        img 20584
        with Dissolve(0.2)
        w
        alex_photograph "Как только я устроился в этот журнал, я стал мечтать сфотографировать это!"
        call photoshop_flash() from _call_photoshop_flash_162
        w
        alex_photograph "Новая модель трусиков от Модного Журнала! Она так идем Вам, Миссис Бакфетт!"
        sound camera_lens1
        img 20585
        with Dissolve(0.2)
        w
        alex_photograph "Миссис Бакфетт... Ахххх..."
        call photoshop_flash() from _call_photoshop_flash_163
        w
        sound camera_lens1
        $ photoImage = 20586
        img photoImage
        with Dissolve(0.2)
        w
        alex_photograph "О, Миссис Бакфетт!"
        alex_photograph "Ахххх..."
        call photoshoot_flash_count() from _call_photoshoot_flash_count_209
        $ PS8_shoots_array.append(photoImage)
        w
        music stop
        img 20587
        show screen photoshot_screen()
        sound bulk1
        with hpunch
        pause 0.7
        hide screen photoshot_screen
        alex_photograph "ААААААААХХХХХ!"
        show screen photoshot_screen()
        sound bulk1
        with hpunch
        pause 0.7
        hide screen photoshot_screen
        w
        show screen photoshot_screen()
        sound bulk1
        with hpunch
        pause 0.7
        hide screen photoshot_screen
        alex_photograph "ААААААААХХХХХ!"

        music Sneaky_Snitch
        img 20588
        with fadelong
        alex_photograph "Я кончил?"
        sound snd_runaway
        img 20589
        with diss
        alex_photograph "Ой!"

        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music stop
        img black_screen
        with diss
        pause 2.0
        music Groove2_85
        img 20590
        with fadelong
        m "Мелани, отдай камеру!"
        m "Я сотру эти непристойные кадры!"
        img 20591
        with diss
        melanie "Миссис Бакфетт, я не хочу делать эту фотосессию вместо Вас."
        melanie "Если я отдам Вам камеру и Вы сотрете сделанные кадры, то Вам придется все это повторить еще раз."
        img 20592
        m "!!!"
        img 20593
        with diss
        melanie "Не волнуйтесь, этот выпуск получит широкое распространение далеко не сразу."
        m "!!!"
        music stop
        img black_screen
        with diss
        pause 2.0
        $ photoshoot8_nude_completed = True
        return


label ep27_photoshoot_suit8_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    music Groove2_85

    if questHelpFlag24 == False:
        $ questHelpFlag24 = True
#        $ questHelpDesc("photoshoot_desc7", "photoshoot_desc8")

    $ questHelp("photoshoot_7", True)
    $ questHelp("photoshoot_8", skipIfExists=True)
    $ shotsAmountCompleted = len(list(set(PS8_shoots_array)))
    if shotsAmountCompleted >= shotsTotalAmount:
#        $ questHelpDesc("photoshoot_desc8", False)
        $ questHelp("photoshoot_8", True)

#    $ questHelp("office_35", skipIfExists=True)
    # думает
    img 20594
    with fadelong
    mt "Я закончила эту непристойную фотосессию."
    mt "Что дальше?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True): #если есть кастинги
            mt "Я не собираюсь идти по офису голой! Я еще не докатилась до такого!"
            mt "И этого не произойдет никогда!!!"
            return
    return
