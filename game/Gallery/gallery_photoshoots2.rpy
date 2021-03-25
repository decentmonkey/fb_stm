label gallery_ep211_dialogues3_photoshoot_7:
    # во время фотосессии периодически показывается лицо инвестора, который пристально смотрит на Монику, рассматривает ее
    # каждый раз, когда Моника отказывается принимать какую-либо позу, она смотрит на инвестора
    $ shotsAmount = PS9_shots_amount
    $ shotsTotalAmount = 33

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 23205
    with fadelong
    alex_photograph "Миссис бакфетт. Пожалуйста, уберите руки от груди, мне надо сделать кадр."
    m "Алекс, сделай кадр как есть, затем я уберу руки..."
    mt "Дьявол!"
    mt "Это все слишком далеко зашло..."
label gallery_ep211_photoshoot_suit9_pose1:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose1"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose2"
    img 23205

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        alex_photograph "А теперь уберите руки, Миссис Бакфетт, пожалуйтса."
        alex_photograph "Иначе я не смогу сделать работу, которую мне поручил мой босс и мне будет выговор."
        menu:
            "Обнажить грудь.":
                pass
            "Уйти.":
                m "С меня хватит!"
                m "Я не собираюсь завершать эту пошлую фотосессию!"
                hide screen photoshoot_camera_icon
                hide screen photoshoot2
                return
        img 23209
        with fadelong
        mt "Боже мой! не могу поверить что я это делаю!"
        mt "Я, Моника Бакфетт..."
        mt "Обнажить грудь, перед камерой..."
        mt "В своем же собственном журнале..."
        mt "Как же до этого могло дойти?!"
        mt "Ведь это увидит весь мир! Абсолютно весь!"
        mt "О Боже!!!"
        img 23210
        with fade
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Я буду фотографировать так, чтобы ничего не было видно!"
        m "Точно?"
        alex_photograph "Конечно, Миссис Бакфетт!"

        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23206, 23207, 23208], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23206
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23207
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23208
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot1_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep211_photoshoot_suit9_pose2:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose2"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose3"
    img 23210

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 23214
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23211, 23212, 23213], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23211
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23212
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23213
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot2_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose3:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose3"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose4"
    #photo
    img 23214

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23218
        with fadelong
        alex_photograph "Миссис Бакфетт! Пожалуйста, сядьте пораскованнее."
        alex_photograph "Не зажимайтесь!"
        m "Но так будет все очень хорошо видно!"
        alex_photograph "Миссис Бакфетт, не волнуйтесь!"
        alex_photograph "Свет от софитов засвечивает снимок и видно только ваше лицо!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23215, 23216, 23217], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23215
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23216
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23217
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot3_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose4:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose4"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose5"

    #4
    #photo
    img 23218
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23222
        with fadelong
        alex_photograph "Миссис Бакфетт, встаньте, пожалуйста, на трон."
        alex_photograph "Так будет лучше видно вашу королевскую фигуру!"
        m "Алекс, только фотографируй так, чтобы ничего не было видно!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23219, 23220, 23221], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23219
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23220
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23221
        img photoImage
        with Dissolve(0.2)
        m "Алекс, не фотографируй так, чтобы были видны мои ноги или... что-нибудь выше..."
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Я ни в коем случае не возьму такой кадр!"
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot4_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep211_photoshoot_suit9_pose5:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose5"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose6"

    #5
    #photo
    img 23222
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23226
        with fadelong
        m "Алекс, ты помнишь, что ты мне обещал перед началом съемки?"
        alex_photograph "Да, конечно, Миссис Бакфетт."
        alex_photograph "Я все сделаю, как надо, не переживайте."
        m "Алекс, эта поза не будет хорошо смотреться в кадре..."
        alex_photograph "Что вы, Миссис Бакфетт, это будет просто великолепный кадр!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23223, 23224, 23225], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23223
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23224
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23225
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot5_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose6:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose6"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose7"
    #6
    #photo
    img 23226

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23230
        with fadelong
        m "Алекс, ты уверен, что в таком ракурсе не будет видно ничего лишнего?"
        alex_photograph "Конечно, Миссис Бакфетт! Вы можете мне довериться."
        m "Алекс, не снимай меня крупным планом! Ты забыл, что ты мне обещал?"
        alex_photograph "Я помню, Миссис Бакфетт. Кадры получаются отличные!"
        alex_photograph "Вам очень идет это платье! Настоящая королева!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23229, 23228, 23227], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23229
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23228
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23227
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot6_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose7:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose7"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose8"

    #7
    #photo
    img 23230

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23234
        with fadelong
        m "Алекс, не бери близко кадр!"
        m "Будет все видно!"
        alex_photograph "Не волнуйтесь, Миссис Бакфетт!"
        alex_photograph "Я снимаю под таким углом, что форму груди будет не видно!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23231, 23232, 23233], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23231
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23232
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23233
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot7_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep211_photoshoot_suit9_pose8:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose8"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose9"

    #8
    #photo
    img 23234

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23238
        with fadelong
        m "Алекс, я не буду вставать в такую позу!"
        # инвестор
    #    campbell "Кхм... Эта поза как нельзя лучше демонстрирует платье..."
    #    campbell "И характеризует новый курс вашего журнала, Миссис Бакфетт..."
    #    mt "!!!"
        alex_photograph "Миссис Бакфетт, это очень интересный ракурс."
        alex_photograph "Ничего лишнего в кадре не будет видно, не переживайте."
        m "Ты уверен в этом, Алекс?"
        alex_photograph "Конечно. Я Вам обещаю, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23235, 23236, 23237], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23235
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23236
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23237
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot8_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose9:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose9"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose10"

    #photo
    img 23238

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 23242
        with fadelong
        alex_photograph "Миссис Бакфетт!"
        alex_photograph "Пожалуйста, оставьте ножки раздвинутыми, а сами откиньтесь на спинку трона."
        alex_photograph "И примите расслабленное положение!"
        alex_photograph "Это будет великолепный кадр!"
        m "Алекс, ни за что!"
        m "Ты ведь знаешь что там у меня ничего нет!"
        m "Даже на рассчитывай на это!"
        alex_photograph "Но Миссис Бакфетт, Мистер Биф сказал, что..."
        m "Мне плевать что он сказал!"
        m "Я не собираюсь брать такие пошлые кадры!"
        m "Фотографируй как есть, иначе я вообще сейчас уйду!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23239, 23240, 23241], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23239
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23240
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23241
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot9_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose10:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose10"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_pose10a"

    #photo
    img 23242

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23243, 23244, 23245], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23243
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23244
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23245
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot10_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_pose10a:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 2.0
    music Groove2_85
    img 23246
    with fade
    sound man_steps
    biff "Как проходит фотосессия, Мистер Кэмпбелл?"
    biff "Довольны ли Вы всем?"
    biff "Вы уже приняли окончательное решение по поводу инвестирования в журнал?"
    img 23247
    with diss
    campbell "Вы знаете, у меня сомнения по этому поводу."
    campbell "Вы, как личный менеджер Миссис Бакфетт, дали мне гарантию по поводу курса журнала и его содержания."
    campbell "Однако, я вижу что Миссис Бакфетт вовсе не поддерживаю ею же задекларированный курс."
    img 23248
    with fade
    biff "???"
    campbell "Вместо этого, она стесняется и отказывается принимать некоторые позы, которые очень бы подошли моему наряду."
    img 23249
    with diss
    biff "О, Мистер Кэмпбелл, не волнуйтесь!"
    biff "Миссис Бакфетт, действительно, немного стесняется при посторонних."
    biff "Это эмоции, вы же знаете женщин, Мистер Кэмпбелл."
    biff "Но я сейчас ее успокою и сделаю убеждение расслабиться перед камерой."
    img 23250
    with fade
    biff "Ведь Миссис Бакфетт также как и я понимает всю важность вашего решения касаемо инвестиций в журнал..."
    m "!!!"
    img 23251
    with diss
    biff "Как Вы хотите продолжить фотосессию?"
    biff "Хотите, Миссис Бакфетт обнажится полностью и примет любую позу, которые Вы пожелаете..."
    biff "Или, если хотите, можно пригласить мужскую модель и сделать фотосессию совокупления."
    biff "Это может сразу повысить рейтинги нашего с Вами журнала!"
    music Power_Bots_Loop
    img 23252
    with hpunch
    m "ЧТО?!!!"
    music Groove2_85
    img 23253
    with fade
    campbell "Нет, Мистер Биф. Давайте не будем торопиться."
    campbell "Я бы не хотел портить впечатление зрителей от закрытой фотосессии, которую Вы вскоре собираетесь опубликовать."
    campbell "И я бы не хотел, чтобы Миссис Бакфетт снимала платье, я не хочу лишаться рекламы моего бренда."
    campbell "Будет достаточно лишь немного приоткрыть его."
    campbell "В другой раз, я предоставлю соответствующий наряд и мы значительно продвинемся в направлении нового курса журнала."
    biff "Да, Мистер Кэмпбелл, конечно!"
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 2.0
    music Groove2_85
    img 23254
    with fadelong
    biff "Кукла, у тебя что, совсем закончились твои куриные мозги?!"
    biff "Ты вообще понимаешь перед кем ты здесь ломаешься?!"
    biff "Это Мистер Кэмпбелл, один из самых богатых людей этого города!"
    biff "Будь рада что он вообще пока еще не раскусил то, что ты поддельная резиновая кукла!"
    biff "Потому, встань в ту позу, которую он пожелал."
    img 23255
    with fade
    biff "Отвлеки его взгляд от своей глупой кукольной модрашки, чтобы продолжить оставаться неузнанной."
    biff "Пока он думает, что ты Моника Бакфетт, он готов инвестировать в наш журнал!"
    music Pyro_Flow
    img 23256
    with diss
    m "Биф, но я..."
    m "Это ведь публичная фотосессия!"
    biff "Если ты сейчас же не сделаешь что я тебе говорю, ты вылетишь отсюда и никогда больше не попадешь в этот шикарный офис!"
    biff "Я считаю до трех!"
    biff "Раз..."
    img 23257
    with fade
    mt "О Боже! Что мне делать?!"
    biff "Два..."
    img 23258
    with diss
    mt "Кэмпбелл сказал, что надо лишь немного приоткрыть платье..."
    mt "Может быть не будет ничего видно?"
    img 23259
    with diss
    biff "Три!"
#    if ep211_quests_photoshoot_stage == 2:
    menu:
        "Сделать как требует Биф.":
            pass
        "Уйти (конец квестов, связанных с офисом).":
            hide screen photoshoot_camera_icon
            hide screen photoshoot2
            music Power_Bots_Loop
            img 23278
            with hpunch
            m "Я не собираюсь участвовать в этом фарсе!"
            m "Прощайте, мерзавцы!!!"
            return
#    else:
#        menu:
#            "Сделать как требует Биф.":
#                pass
#            "Уйти.":
#                hide screen photoshoot_camera_icon
#                hide screen photoshoot2
#                music Power_Bots_Loop
#                img 23278
#                with hpunch
#                m "Я не собираюсь участвовать в этом фарсе!"
#                return 0
    mt "У меня нет выбора!"
    mt "Если у меня не будет денег от этих фотосессий, то Виктория скажет Дику бросить мое дело!"
    mt "И я окажусь в руках Маркуса и тех, кто стоит за ним!"
    mt "А там меня ждет... О Ужас!!!"
    mt "У меня нет выбора!"

    music stop
    img black_screen
    pause 1.5
    music Groove2_85
    img 23260
    with fadelong
    biff "Мистер Кэмпбелл. я убедил Миссис Бакфетт."
    campbell "Вы отличный личный менеджер, Биф! вы знаете подход к своему Боссу!"
    biff "Спасибо, Мистер Кэмпбелл!"
    biff "Вас устраивает поза Миссис Бакфетт?"
    biff "Хотите мы снимем это платье и повесим рядом, чтобы был виден Ваш бренд?"
    campbell "Нет, Мистер Биф. Все в порядке."
    campbell "Так вполне достаточно. Для этого раза..."

label gallery_ep211_photoshoot_suit9_pose11:
    $ photoPoseLabel = "gallery_ep211_photoshoot_suit9_pose11"
    $ photoPoseNextLabel = "gallery_ep211_photoshoot_suit9_end"

    #photo
    img 23260

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS9_shoots_array)
    show screen photoshoot2([23262, 23265, 23275], PS9_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 23261
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        $ photoImage = 23262
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 23263
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        img 23264
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        $ photoImage = 23265
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 23266
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        img 23267
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        img 23268
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        img 23269
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        img 23270
        with Dissolve(0.2)
        w
        mt "Мне нужно, чтобы он согласился вложить деньги в журнал..."
        call photoshop_flash()
        w
        sound camera_lens1
        img 23271
        with Dissolve(0.2)
        w
        mt "Если я сорву эту фотосессию, то этот неудачник просто откажется."
        call photoshop_flash()
        w
        sound camera_lens1
        img 23272
        with Dissolve(0.2)
        w
        mt "Биф сказал, что выгонит меня с работы, если хоть одни из инвесторов откажется..."
        call photoshop_flash()
        w
        sound camera_lens1
        img 23273
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        img 23274
        with Dissolve(0.2)
        w
        call photoshop_flash()
        w
        sound camera_lens1
        $ photoImage = 23275
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ photoshoot9MonicaShowedAss = True
#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot11_progress")
#        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep211_photoshoot_suit9_end:
    # после фотосессии инвестор смортит на Монику, она прикрывает грудь руками
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 2.0
    music Groove2_85
    img 23276
    with fadelong
    campbell "Благодарю. Мне было любопытно поприсутствовать."
    # инвестор встает со стула и уходит
#    if ep211_quests_photoshoot_stage == 2:
    img 23277
    with fade
    mt "Куда этот неудачник пошел?"
#    mt "А если он пошел к Бифу и сейчас скажет ему, что отказывается?!"
#    mt "Тогда я не смогу больше здесь работать!!!"
    mt "Мне нужно переодеться и идти к Бифу."
    mt "Нужно узнать, что решил этот мерзкий Мистер Кэмпбелл..."
#    $ shotsAmountCompleted = len(list(set(PS9_shoots_array)))
    return

label gallery_ep213_photoshoot10:
    $ shotsAmount = PS10_shots_amount
    $ shotsTotalAmount = 42

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    # Моника стоит, прикрывая грудь
    imgfl 24230
    w
    imgd 24231
    mt "Биф выгонит меня с работы, если я сорву эту фотосессию..."
    mt "Нужно сказать Алексу, чтобы не брал откровенные ракурсы."
    mt "Если это вообще возможно в ЭТОМ!"
    mt "!!!"

    imgf 24232
    m "Алекс..."
    alex_photograph "Да, Миссис Бакфетт?"
    alex_photograph "Вы готовы? Отлично выглядите!"
    m "Алекс, никаких откровенных ракурсов!"
    m "Ты понял меня?"
    alex_photograph "Да, конечно, Миссис Бакфетт."
    m "И никаких крупных планов!"

    imgd 24233
    alex_photograph "Я все сделаю, как надо, Миссис Бакфетт."
    alex_photograph "Не переживайте..."
    m "..."
    alex_photograph "Начнем?"
    fadeblack 2.0
    imgfl 24234

label gallery_ep213_photoshoot_suit10_pose1:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose1"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose2"
    # фразы Моники во время позирования для Алекса:
    #кадр
    img 24234
    #up
#    img 24235
    #side
#    img 24236
    #down
#    img 24237

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgf 24238
        m "Алекс, не забудь, что ты мне обещал."
        alex_photograph "Конечно, Миссис Бакфетт."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24235, 24236, 24237], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24235
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24236
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24237
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

#        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot1_progress")


label gallery_ep213_photoshoot_suit10_pose2:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose2"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose3"
    #кадр
    img 24238
    #up
#    img 24239
    #side
#    img 24240
    #down
#    img 24241

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24242
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24239, 24240, 24241], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24239
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_318
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24240
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_319
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24241
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_320
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep213_photoshoot_suit10_pose3:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose3"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose4"
    #кадр
    img 24242
    #up
#    img 24243
    #side
#    img 24244
    #down
#    img 24245

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24246
        m "Может, мне стоит немного прикрыть здесь руками?"
        biff "Миссис Бакфетт, отличная поза. Ничего не надо прикрывать!"
        m "!!!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24243, 24244, 24245], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24243
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_321
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24244
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_322
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24245
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_323
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel



label gallery_ep213_photoshoot_suit10_pose4:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose4"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose5"
    #кадр
    img 24246
    #up
#    img 24247
    #side
#    img 24248
    #down
#    img 24249

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24250
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24247, 24248, 24249], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24247
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_324
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24248
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_325
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24249
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_326
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep213_photoshoot_suit10_pose5:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose5"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose6"
    #кадр
    img 24250
    #up
#    img 24251
    #side
#    img 24252
    #down
#    img 24253

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24254
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24251, 24252, 24253], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24251
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_327
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24252
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_328
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24253
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_329
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep213_photoshoot_suit10_pose6:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose6"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose7"

    #кадр
    img 24254
    #up
#    img 24255
    #side
#    img 24256
    #down
#    img 24257

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24258
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24255, 24256, 24257], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24255
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_330
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24256
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_331
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24257
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_332
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose7:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose7"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose8"

    #кадр
    img 24258
    #up
#    img 24259
    #side
#    img 24260
    #down
#    img 24261

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24262
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24259, 24260, 24261], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24259
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_333
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24260
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_334
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24261
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_335
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose8:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose8"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose9"
    #кадр
    img 24262
    #up
#    img 24263
    #side
#    img 24264
    #down
#    img 24265

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24266
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24263, 24264, 24265], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24263
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_336
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24264
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_337
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24265
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_338
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label gallery_ep213_photoshoot_suit10_pose9:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose9"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose10"

    #кадр
    img 24266
    #up
#    img 24267
    #side
#    img 24268
    #down
#    img 24269

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24270
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24267, 24268, 24269], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24267
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_339
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24268
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_340
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24269
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_341
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose10:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose10"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose11"
    #кадр
    img 24270
    #up
#    img 24271
    #side
#    img 24272
    #down
#    img 24273

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24274
        investor2 "На прошлых двух фотосессиях было мало кадров сзади."
        investor2 "Я предлагаю сделать кадры именно с такого ракурса..."
        biff "Отличная идея!"
        biff "Алекс, ты слышал? Возьми крупным планом."
        m "Алекс!"
        alex_photograph "Миссис Бакфетт, я просто делаю свою работу."
        mt "Биф мерзавец!!!"
        mt "!!!"

        # Моника ложится в нужную позу

        imgfl 24274
        #engine
        m "Алекс, старайся не брать крупные планы..."
        alex_photograph "Я не делаю снимки, Миссис Бакфетт..."
        alex_photograph "Я просто подбираю лучший ракурс."
        mt "Этот фотограф-извращенец просто пялится на меня!"
        mt "!!!"

        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24271, 24272, 24273], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24271
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_342
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24272
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_343
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24273
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_344
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose11:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose11"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose12"
    #кадр
    img 24274
    #up
#    img 24275
    #side
#    img 24276
    #down
#    img 24277

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24278
        m "Алекс, мне кажется эта поза слишком откровенная..."
        alex_photograph "Нет, Миссис Бакфетт. Это будет отличный кадр, вот увидите."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24275, 24276, 24277], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24275
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_345
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24276
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_346
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24277
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_347
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose12:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose12"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose13"

    #кадр
    img 24278
    #up
#    img 24279
    #side
#    img 24280
    #down
#    img 24281
#    img 24282

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        imgfl 24283
        philip "Хотел бы добавить свое пожелание, если позволите..."
        biff "Да, конечно!"
        philip "Мне кажется, будет очень сексуальный кадр, если Миссис Бакфетт ляжет..."
        philip "И развинет ноги..."

        mt "ЧТО?!"
        biff "Миссис Бакфетт, прошу вас. Вы слышали пожелание нашего многоуважаемого гостя."
        mt "Биф, это съемка для модного журнала, а не для..."

        # Биф подходит к Монике и зло ей шепчет
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        fadeblack 1.5
        music Groove2_85
        imgf 24294
        biff "Еще одно слово, кукла безмозглая, и ты вылетишь с работы!"
        biff "Только сначала, шлюха, я отдам тебя всем этим денежным мешкам!"
        biff "Пусть делают с тобой все, чего им захочется!"
        biff "Быстро сделала, как сказал инвестор!"
        mt "!!!"
        menu:
            "Принять позу, которую хочет увидеть инвестор.":
                pass
        imgd 24295
        mt "Если я сейчас откажусь принимать эту позу, то я сорву фотосессию..."
        mt "Знал бы этот мерзавец, как мне нужны эти деньги..."
        mt "Ненавижу их всех!"
        mt "!!!"

        # Биф отходит обратно к инвесторам
        fadeblack 1.5
        music Groove2_85
        imgf 24296
        investor3 "Какие-то проблемы, Мистер Биф?"
        investor3 "Миссис Бакфетт отказывается от продолжения?"
        biff "Нет, все в порядке..."
        biff "Ей просто нужен был небольшой перерыв."

        imgd 24297
        biff "Алекс, продолжай!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24279, 24280, 24282], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24279
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_348
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24280
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_349
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24281
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_201
        w

        sound camera_lens1
        $ photoImage = 24282
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_350
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose13:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose13"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose14"
    #кадр
    img 24283
    #up
#    img 24284
#    img 24285
    #side
#    img 24286
#    img 24287
#    img 24288
    #down
#    img 24289
#    img 24290
#    img 24291
#    img 24292
#    img 24293

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        jump gallery_ep213_photoshoot10b

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24285, 24288, 24293], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 24284
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_202
        w
        sound camera_lens1
        $ photoImage = 24285
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_351
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        sound camera_lens1
        img 24286
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_203
        w
        sound camera_lens1
        img 24287
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_204
        w
        #side
        sound camera_lens1
        $ photoImage = 24288
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_352
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24289
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_205
        w
        sound camera_lens1
        img 24290
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_206
        w
        sound camera_lens1
        img 24291
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_207
        w
        sound camera_lens1
        img 24292
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_208
        w

        sound camera_lens1
        $ photoImage = 24293
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_353
#        $ PS10_shoots_array.append(photoImage)
        w
        music Groove2_85
        imgd 24298
        steve "Вы были правы, Мистер Филипп."
        steve "Поза очень сексуальная."
        steve "Если взять еще несколько крупных планов, то получатся отличные кадры..."
        music Power_Bots_Loop
        img 24299
        mt "Этот никчемный неудачник Стив еще что-то советует?!"
        mt "И вообще! Какого черта он здесь делает?!"
        mt "!!!"
        jump expression photoPoseLabel

label gallery_ep213_photoshoot10b:



    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    imgfl 24300
    alex_photograph "Съемка окончена!"
    biff "Отлично! Спасибо, Алекс!"
    # Моника стоит, прикрывшись, Биф обращается к инвесторам
    imgd 24301
    biff "Господа, спасибо за ваше присутствие!"
    biff "Надеюсь, вы убедились в серьезности наших намерений."
    biff "Всегда будем рады видеть вас в нашем офисе!"
    # все инвесторы встают со стульев, кроме одного
    # затемнение, звук мужских шагов
    imgd 24302
    w
    # смена кадра
    # Моника стоит также прикрывшись, на стуле сидит один инвестор, Биф стоит рядом с ним
    fadeblack 2.0
    music Groove2_85
    imgfl 24303
    investor4 "Я специально задержался, Мистер Биф..."
    investor4 "Меня впечатлила презентация Миссис Бакфетт, а также ее умение держаться перед камерой..."
    investor4 "Я вижу, что у вас достаточно серьезные намерения относительно смены курса журнала."
    investor4 "И Миссис Бакфетт это сегодня подтвердила... Почти..."
    investor4 "В связи с этим я принял решение..."
    imgd 24304
    biff "..."
    m "..."

    imgf 24305
    investor4 "Я готов инвестировать в журнал Миссис Бакфетт, но у меня есть одно условие..."

    imgd 24306
    biff "Какое условие? Мы готовы его рассмотреть!"
    investor4 "Я инвестирую в журнал, если Миссис Бакфетт сделает еще один кадр..."

    img 24307 vpunch
    m "Какой кадр?!"

    imgf 24308
    investor4 "Широко раздвинет ноги и сдвинет свои трусики."
    investor4 "Таким образом, я буду уверен в том, что..."
    investor4 "Откровенные кадры, которыми вы аргументируете серъезность принятого вами курса..."
    investor4 "Они являются плодом регулярной работы, а не случайным явлением... #они - it"
    investor4 "Когда фотограф внезапно подловил модель."
    investor4 "Я хочу увидеть, что Миссис Бакфетт осознанно сделает это..."

    music Power_Bots_Loop
    img 24309 hpunch
    m "!!!"
    # Биф радостный, Моника в шоке
    m "Что?!"
    m "Я..."

    music Groove2_85
    imgf 24310
    biff "О, Господин Инвестор, с этим нет никаких проблем!"
    biff "Конечно же, Миссис Бакфетт сделает это!"

    # поворачивается к Монике
    imgd 24311
    biff "Сделает прямо сейчас!"
    music Power_Bots_Loop
    img 24312 hpunch
    m "Биф!"

    music Groove2_85
    imgd 24313
    biff "И не будет тратить время на бесполезные разговоры."
    biff "У нашего многоуважаемого Господина Инвестора каждая минута на счету!"
    biff "Время - деньги, Миссис Бакфетт!"

    img 24314
    mt "!!!"
#    $ menu_corruption = [monicaPresentation2Choice3]
    menu:
        "Согласна.": #corruption высокий!
            pass
        "НЕТ!!!":
            music Power_Bots_Loop
            m "Нет! Я не буду делать ЭТОГО!"
            # Биф начинает наезжать на Монику
            img 24313
            biff "Миссис Бакфетт!!!"
            biff "Вы сейчас же сделаете, как просит Господин Инвестор!"
            biff "Иначе!"
            biff "Вы, Миссис Бакфетт, помните, что будет!"
            fadeblack 1.5
            music Power_Bots_Loop
            imgfl 24315
            m "Я не собираюсь сдвигать трусики!!!"
            m "!!!"
            # Моника уходит с фотосессии
            hide screen photoshoot_camera_icon
            hide screen photoshoot2
            return
    # Моника в растерянности
    music Hidden_Agenda
    mt "У меня есть шанс сделать так, что еще один инвестор согласится на инвестицию в мой журнал!"
    mt "Но не таким же способом!"
    mt "А вдруг этот снимок станет общедоступным?!"
    mt "Что тогда, Моника?!"
    mt "?!"
    mt "Дьявол!"
    mt "Но если я сейчас откажусь..."
    mt "Где я потом смогу зарабатывать $ 5000 каждую неделю?!"
    imgd 24316
    m "..."
    m "Я..."
    m "Я сделаю это..."

    fadeblack 2.0
    music Loved_Up
    # Биф радостно
    imgfl 24317
    biff "Алекс, ты готов?"
    alex_photograph "Да, Мистер Биф. Конечно."
    # хитро улыбается

    imgd 24318
    mt "Боже! Моника, как могло дойти до того, что ты сдвигаешь трусики для какого-то жалкого инвестора?!"
    imgd 24319
    mt "Да какая разница, для кого?!"
    imgd 24320
    mt "Как ты вообще могла позволить дойти до ТАКОГО?!"
#    music Power_Bots_Loop
    img 24321 vpunch
    mt "?!?!?!"
    imgd 24322
    mt "Я отомщу кретину Бифу за это!"
    mt "И этому извращенцу инвестору тоже!"
    mt "Они еще пожалеют об этом!"
    mt "!!!"
    music stop

label gallery_ep213_photoshoot_suit10_pose14:
    $ photoPoseLabel = "gallery_ep213_photoshoot_suit10_pose14"
    $ photoPoseNextLabel = "gallery_ep213_photoshoot_suit10_pose15"

    # кадр
    img 24322
    #up
#    img 24323
    #side
#    img 24324
    #down
#    img 24325
#    img 24326
#    img 24327
#    img 24328
#    img 24329
#    img 24330
#    img 24331

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85

        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS10_shoots_array)
    show screen photoshoot2([24323, 24324, 24331], PS10_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 24323
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_354
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24324
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_355
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24325
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_209
        w
        sound camera_lens1
        img 24326
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_210
        w
        sound camera_lens1
        img 24327
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_211
        w
        sound camera_lens1
        img 24328
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_212
        w
        sound camera_lens1
        img 24329
        with Dissolve(0.2)
        w
        call photoshop_flash()
# from _rcall_photoshop_flash_213
        w
#        sound camera_lens1
        imgfl 24330
#        with Dissolve(0.2)
#        w
#        call photoshop_flash()
        w
        sound camera_lens1
        $ photoImage = 24331
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count()
# from _rcall_photoshoot_flash_count_356
#        $ PS10_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label gallery_ep213_photoshoot_suit10_pose15:
# Моника раздвигает ноги и сдвигает трусики
    # Алекс делает кадр
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
#    alex_photograph "!!!"
    fadeblack 1.5
    music Groove2_85
    imgfl 24332
    investor4 "..."
    investor4 "Спасибо, Миссис Бакфетт."
    investor4 "Можете вернуть Ваши трусики на место."
    # инвестор встает
    imgf 24333
    biff "Господин Инвестор, пройдемте в мой кабинет."
    biff "Обсудим с Вами подробности нашей сделки."
    # они уходят
    sound man_steps
    fadeblack 2.0
    music Power_Bots_Loop
    img 24334 hpunch
    mt "Сволочи!"
    mt "Никчемные жалкие неудачники!"
    mt "!!!"
    # Алекс смортит к Монике
    music Groove2_85
    imgf 24335
    alex_photograph "Миссис Бакфетт, это была Ваша лучшая фотосессия!"
    # Моника прикрывается
    img 24336
    m "Алекс, не смотри на меня!"
    m "Отвернись, быстро!"
    mt "Еще одни извращенец!"
    mt "!!!"
    hide screen photoshoot_camera_icon
    hide screen photoshoot2

    return
