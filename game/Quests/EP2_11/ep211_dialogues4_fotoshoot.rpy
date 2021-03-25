default photoshoot9_count = 0

default monicaBiffPhotoshootInvestor1 = False  # Моника с 1-го раза согласилась фотографироваться в платье Королева сердец
default monicaBiffPhotoshootInvestor2 = False  # Моника со 2-го раза согласилась фотографироваться в платье Королева сердец

default photoshoot9MonicaShowedAss = False

#call ep211_dialogues3_photoshoot_1() # мысли, пришла в офис в день фотосесии
#call ep211_dialogues3_photoshoot_2() # встреча с инвестором в кабинете Бифа, разговор с Бифом
#call ep211_dialogues3_photoshoot_3() # фотостудия, разговор с Алексом, переодевается
#call ep211_dialogues3_photoshoot_4() # переоделась, разговор с Бифом в его кабинете
#call ep211_dialogues3_photoshoot_5() # Моника отказалась от фотосессии, оказалась на улице, но потом передумала и пришла к Бифу
#call ep211_dialogues3_photoshoot_6() # фотостудия, разговор с Алексом, приходит инвестор
#call ep211_dialogues3_photoshoot_7() # фотосессия
#call ep211_dialogues3_photoshoot_8() # кабинет Бифа, после фотосессии

# другой день после паблик ивента, Моника приходит на работу в офис
label ep211_dialogues3_photoshoot_1:
    # не рендерить!
    mt "Сегодня у меня фотосессия в каком-то наряде от инвестора."
    mt "Надеюсь, это будет приличный наряд..."
    return

# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_2:
    # Моника заходит в кабинет, там сидит инвестор на стуле перед проектором
    # Биф показывает ему фотки с ее фотосессии в костюме черного лебедя
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    img 16867
    with fadelong
    w
    img 16868
    with fade
    sound camera_lens1
    w
    img 16869
    with diss
    sound camera_lens1
    w
    sound camera_lens1
    music stop
    img 16870
    with hpunch
    sound plastinka1b
    w
    music Power_Bots_Loop
    img 16871
    with fade
    mt "!!!"
    music Groove2_85
    img 16872
    with diss
    biff "В скором времени, Я планирую опубликовать эти кадры в широкий доступ."
    music Power_Bots_Loop
    img 16873
    with diss
    mt "ЧТО-О-О?!"
    mt "!!!!!"
    # инвестор говорит, внимательно рассматривая кадры
    music Groove2_85
    img 16874
    with fade
    campbell "Опубликуйте их после фотосессии в моем платье 'Королева сердец'."
    campbell "Если вы их опубликуете до этой фотосессии..."
    campbell "То снимки в моем платье будут публике неинтересны."
    img 16875
    with diss
    biff "Конечно, Мистер Кэмпбелл!"
    biff "Кстати, Миссис Бакфетт уже пришла на фотосессию."
    img 16876
    with diss
    biff "Можете проходить в фотостудию, Мистер Кэмпбелл."
    campbell "Да, спасибо."
    img 16877
    with fade
    sound man_steps
    w
    img 16878
    with diss
    w
    # инвестор уходит в фотостудию
    # Моника орет на Бифа
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Power_Bots_Loop
    img 16879
    with hpunch
    m "Биф!"
    m "Зачем ты показал эти фотографии инвестору?!"
    m "!!!"
    music Groove2_85
    img 16880
    with fade
    biff "Я тебя забыл спросить, кукла безмозглая, что мне делать!"
    biff "Ты не задаешь вопросы, когда сосешь на улице члены за $ 20!.."
    biff "Но пытаешься спорить, когда я показываю твою задницу, даже без члена в ней, состоятельному инвестору!"
    biff "Не забывай, какае деньги я плачу тебе, кукла!"
    m "!!!"
    img 16881
    with diss
    biff "Хватит орать тут и быстро иди переодевайся!"
    biff "Тебя ждет Мистер Кэмпбелл. И только попробуй сорвать эту фотосессию!!!"
    biff "Я тебя в один миг вышвырну отсюда на улицу!!!"
    music Power_Bots_Loop
    img 16882
    with fade
    mt "ААААААА!"
    mt "НЕНАВИЖУ!!!"
    mt "УБЬЮ!!!"
    #$ log1 = t_("Идти в фотостудию и переодеться.")
    return


# фотостудия
label ep211_dialogues3_photoshoot_3:
    # Моника заходит в фотостудию, разговор с Алексом, как обычно
    # в меню выбора новый костюм. Моника переодевается и выходит к Алексу, прикрывшись руками
    # начинает возмущаться
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    img 23193
    with fadelong
    m "Алекс!!!"
    m "Это разве платье?!?!?!"
    m "Эта тряпка на мне совсем не закрывает мою грудь!!!"
    m "Алекс, как я буду сниматься в этом?! Да еще и при этом инвесторе?!"
    # Алекс пускает слюни и пялится на Монику
    music Groove2_85
    img 23194
    with fade
    alex_photograph "Миссис Бакфетт, не переживайте."
    alex_photograph "Это платье очень Вам идет! Вы в нем настоящая королева!"
    alex_photograph "Я буду делать кадры, на которых ничего не будет видно."
    # Моника смотрит на него недоверчиво
    music Pyro_Flow
    img 23195
    with diss
    mt "Этот фотограф-извращенец всегда так говорит, а в итоге..."
    mt "Нужно сходить к Бифу и послать его к черту!"
    mt "Или пусть предоставит другое платье!"
    mt "Или фотосессия отменяется!"
#    $ log1 = t_("Пойти к Бифу.")
    return

# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_4:
    # Моника, прикрывшись руками, заходит в кабинет Бифа и орет
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    img 16856
    with fadelong
    w
    sound highheels_short_walk
    img 16857
    with fade
    m "Биф, я не буду фотографироваться в ЭТОМ!!!"
    m "Это не платье!"
    m "У меня вся грудь открыта в нем!!!"
    m "!!!"
    music Groove2_85
    img 16858
    with diss
    biff "У тебя, кукла, никто не спрашивал!"
    music Pyro_Flow
    img 16859
    with fade
    m "Биф, я предупреждаю, что я не буду делать никаких откровенных кадров!"
    m "Я соглашусь на кадры только с прикрытой грудью!"
    music Groove2_85
    img 15902
    with diss
    biff "А я тебя предупреждаю, что если Кэмпбелл откажется инвестировать..."
    biff "То виновата в этом будешь ты, кукла безмозглая!"
    biff "У тебя не хватает мозгов понять, что от этой фотосессии многое зависит?"
    img 16860
    with fade
    biff "Проведи ее и чтобы никаких глупостей!"
    biff "Это твоя работа! Ты получаешь за это немаленькие деньги!"
    biff "Иди в фотостудию!"
    # Моника зло
    music Power_Bots_Loop
    img 16861
    with diss
    mt "Мерзавец!"
    mt "!!!"
    $ menu_corruption = [monicaPhotoshoot9CorruptionRequired]
    menu:
        "Идти в фотостудию и провести фотосессию в платье 'Королева сердец'.": #corruption
            $ monicaBiffPhotoshootInvestor1 = True # Моника с 1-го раза согласилась фотографироваться в платье Королева сердец
            pass
        "Я не буду участвовать в этом!!!":
            music Pyro_Flow
            img 16863
            with fade
            m "Биф, я не буду фотографироваться в этом платье!"
            m "Да еще в присутствии этого инвестора!"
            img 16864
            with diss
            m "Я не хочу, чтобы он на меня пялился!"
            m "Почему я?! Почему не Мелани?"
            music Groove2_85
            img 15870
            with fade
            biff "Потому что Мистер Кэмпбелл так хочет!"
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            img 16865
            with diss
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            music Power_Bots_Loop
            img 16862
            with fade
            mt "!!!"
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    music Pyro_Flow
    img 16862
    with fade
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги."
    mt "Где я смогу заработать 5 тысяч в месяц для сучки Виктории?"
    music Groove2_85
    img 16866
    with diss
    m "Я проведу эту фотосессию..."
    img 16865
    with fade
    biff "Иди в фотостудию."
    music Power_Bots_Loop
    img 16861
    with diss
    mt "Чертов Биф!"
    mt "На публичном вечере я всем сказала, что публика никогда не увидит мою грудь!"
    mt "Что я всем им скажу теперь?! О ужас!!!"
    mt "!!!"
    $ log1 = t_("Идти в фотостудию и провести фотосессию.")
    return True

label ep211_dialogues3_photoshoot_4b:
    "Я не буду участвовать в этом!!!":
    return

# если Моника отказалась фотографироваться в этом платье и оказалась на улице, но потом передумала и пришла к Бифу
# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_5:
    music Groove2_85
    img 13891
    with fade
    m "Биф..."
    m "Мне нужна работа."
    img 13892
    with diss
    biff "Если цыпочка хочет работать, она сделает фотосессию."
    biff "В платье от инвестора и в его присутствии."
    img 13900
    with fade
    m "..."
    img 13906
    with diss
    biff "Ты согласна?"
    mt "!!!"
    $ menu_corruption = [monicaPhotoshoot9CorruptionRequired]
    menu:
        "Идти в фотостудию и провести фотосессию в платье 'Королева сердец'.": #corruption
            $ monicaBiffPhotoshootInvestor2 = True # Моника со 2-го раза согласилась фотографироваться в платье Королева сердец
            pass
        "Я не буду участвовать в этом!!!":
            music Pyro_Flow
            img 15896
            with fade
            m "Нет! Я не буду фотографироваться в этом платье!"
            m "Да еще в присутствии этого инвестора!"
            m "Я не хочу, чтобы он на меня пялился!"
            music Groove2_85
            img 15906
            with diss
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            img 15902
            with fade
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            music Power_Bots_Loop
            img 12792
            with diss
            mt "!!!"
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    music Pyro_Flow
    img 12810
    with fade
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги."
    mt "Где я смогу заработать 5 тысяч в месяц для сучки Виктории?"
    img 12792
    with diss
    mt "..."
    mt "На публичном вечере я всем сказала, что публика никогда не увидит мою грудь!"
    mt "Что я всем им скажу теперь?! О ужас!!!"
    mt "..."
    music Groove2_85
    img 12799
    with fade
    m "Я проведу эту фотосессию..."
    img 12815
    with diss
    biff "Иди переодевайся."
    biff "Я пока позвоню Мистеру Кэмпбеллу, чтобы приехал на съемку."
    img 12809
    with fade
    mt "..."
#    $ log1 = t_("Идти в фотостудию и провести фотосессию.")
    return True


# фотостудия, Моника в платье Кролева сердец
label ep211_dialogues3_photoshoot_6:
    # Моника с угрозой обращается к Алексу
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    img 23196
    with fadelong
    m "Алекс!"
    m "Только попробуй взять ракурс, где будет видна моя... моя..."
    # Моника замолкает, так как в фотостудию заходит инвестор
    music Groove2_85
    img 23197
    with fade
    sound man_steps
    campbell "Миссис Бакфетт, Вам нравится платье, которое я Вам подбрал?"
    # Моника сердито смотрит на него, продолжая прикрывать грудь руками
    music Pyro_Flow
    img 23198
    with diss
    mt "Биф сказал, что от этой фотосессии зависит решение этого неудачника..."
    mt "Если я сделаю что-то не так, он откажется от инвестирования в журнал..."
    mt "Тогда Биф выгонит меня с этой работы..."
    mt "А мне нужны деньги для этой сучки Виктории."
    mt "Черт!!!"
    # Моника сквозь зубы
    menu:
        "Платье мне нравится, Мистер Кэмпбелл...":
            pass
    music Groove2_85
    img 23199
    with fade
    m "Платье мне нравится, Мистер Кэмпбелл..."
    m "Только мне кажется, что оно несколько откровенное..."
    img 23200
    with diss
    campbell "Вы сами мне сказали, что поддерживаете новый курс журнала."
    campbell "Я подобрал платье в соответствии с курсом Вашего журнала."
    img 23201
    with fade
    campbell "И нахожу его весьма подходящим для Вас, Миссис Бакфетт."
    # инвестор садится на стул напротив съемочной площадки и с надменным видом смотрит на Монику
    img 23202
    with diss
    campbell "Приступайте!"
    # Моника
    music Power_Bots_Loop
    img 23203
    with fade
    mt "Мерзкий тип!"
    mt "Скорее надо провести эту долбанную фотосессию..."
    mt "И пусть он убирается отсюда!"
    music Groove2_85
    img 23204
    with diss
    alex_photograph "Приступим, Миссис Бакфетт."
    return

# фотосессия
label ep211_dialogues3_photoshoot_7:
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
label ep211_photoshoot_suit9_pose1:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose1"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose2"
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
                return 0
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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23207
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_1
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23208
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_2
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot1_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep211_photoshoot_suit9_pose2:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose2"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose3"
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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_3
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23212
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_4
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23213
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_5
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot2_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose3:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose3"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose4"
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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_6
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23216
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_7
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23217
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_8
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot3_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose4:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose4"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose5"

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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_9
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23220
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_10
        $ PS9_shoots_array.append(photoImage)
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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_11
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot4_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep211_photoshoot_suit9_pose5:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose5"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose6"

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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_12
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23224
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_13
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23225
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_14
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot5_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose6:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose6"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose7"
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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_15
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23228
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_16
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23227
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_17
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot6_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose7:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose7"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose8"

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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_18
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23232
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_19
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23233
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_20
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot7_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep211_photoshoot_suit9_pose8:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose8"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose9"

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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_21
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23236
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_22
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23237
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_23
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot8_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose9:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose9"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose10"

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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_24
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23240
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_25
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23241
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_26
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot9_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose10:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose10"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_pose10a"

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
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_27
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23244
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_28
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23245
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_29
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot10_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_pose10a:
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
    if ep211_quests_photoshoot_stage == 2:
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
                return -1
    else:
        menu:
            "Сделать как требует Биф.":
                pass
            "Уйти.":
                hide screen photoshoot_camera_icon
                hide screen photoshoot2
                music Power_Bots_Loop
                img 23278
                with hpunch
                m "Я не собираюсь участвовать в этом фарсе!"
                return 0
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

label ep211_photoshoot_suit9_pose11:
    $ photoPoseLabel = "ep211_photoshoot_suit9_pose11"
    $ photoPoseNextLabel = "ep211_photoshoot_suit9_end"

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
        call photoshop_flash() from _rcall_photoshop_flash
        w
        sound camera_lens1
        $ photoImage = 23262
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_30
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 23263
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_1
        w
        sound camera_lens1
        img 23264
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_2
        w
        sound camera_lens1
        $ photoImage = 23265
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_31
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 23266
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_3
        w
        sound camera_lens1
        img 23267
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_4
        w
        sound camera_lens1
        img 23268
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_5
        w
        sound camera_lens1
        img 23269
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_6
        w
        sound camera_lens1
        img 23270
        with Dissolve(0.2)
        w
        mt "Мне нужно, чтобы он согласился вложить деньги в журнал..."
        call photoshop_flash() from _rcall_photoshop_flash_7
        w
        sound camera_lens1
        img 23271
        with Dissolve(0.2)
        w
        mt "Если я сорву эту фотосессию, то этот неудачник просто откажется."
        call photoshop_flash() from _rcall_photoshop_flash_8
        w
        sound camera_lens1
        img 23272
        with Dissolve(0.2)
        w
        mt "Биф сказал, что выгонит меня с работы, если хоть одни из инвесторов откажется..."
        call photoshop_flash() from _rcall_photoshop_flash_9
        w
        sound camera_lens1
        img 23273
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_10
        w
        sound camera_lens1
        img 23274
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_11
        w
        sound camera_lens1
        $ photoImage = 23275
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_32
        $ photoshoot9MonicaShowedAss = True
        $ add_char_progress("AlexPhotograph", PS9_AlexProgressEachCorruptionShot, "PS9_monica_shot11_progress")
        $ PS9_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep211_photoshoot_suit9_end:
    # фразы Моники во время позирования для Алекса:

#    m "Алекс! Снимай меня с другого ракурса!!"
#    alex_photograph "Да, конечно. Сейчас еще один снимок и я возьму другой ракурс."



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
    if ep211_quests_photoshoot_stage == 2:
        img 23277
        with fade
        mt "Куда этот неудачник пошел?"
    #    mt "А если он пошел к Бифу и сейчас скажет ему, что отказывается?!"
    #    mt "Тогда я не смогу больше здесь работать!!!"
        mt "Мне нужно переодеться и идти к Бифу."
        mt "Нужно узнать, что решил этот мерзкий Мистер Кэмпбелл..."
        $ questHelp("photoshoot_13", True)
        $ questHelp("photoshoot_13a", skipIfExists=True)
        $ questHelp("office_45a")

        $ questHelp("office_43", skipIfExists=True)
    $ shotsAmountCompleted = len(list(set(PS9_shoots_array)))
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_13a", True)
#    $ log1 = t_("Пойти в кабиент к Бифу и узнать, что решил инвестор.")
    return 1

# кабинет Бифа
label ep211_dialogues3_photoshoot_8:
    # заходит к Бифу, тот стоит вместе с инвестором
    # жмут друг другу руки
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 16883
    with fadelong
    w
    img 16884
    with fade
    biff "Мистер Кэмпбелл, я уверен, что вы сделали правильный выбор!"
    img 16885
    with diss
    campbell "Посмотрим."
    campbell "Будем надеяться, что это будет выгодная сделка для нас обоих..."
    img 16886
    with diss
    biff "Конечно, Мистер Кэмпбелл!"
    biff "С Вами приятно сотрудничать."
    # инвестор смотрит на часы
    campbell "Я уже опаздываю на важную встречу."
    biff "Как я Вам уже говорил, мы будем рады видеть Вас снова в нашем офисе!"
    # инвестор проходит мимо Моники
    img 16887
    with fade
    sound man_steps
    campbell "Миссис Бакфетт, надеюсь, это была не последняя фотосессия..."
    campbell "На которую я был приглашен..."
    mt "???"
    # Моника грозно смотрит на Бифа, тот стоит довольный
    music Pyro_Flow
    img 16888
    with diss
    m "До свидания, Мистер Кэмпбелл."
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Groove2_85
    # инвестор уходит
    # Биф довольный, садится на свой стул
    img 12785
    with fade
    biff "Папочка доволен, что цыпочка смогла убедить первого инвестора."
    biff "Но папочка недоволен тем, что осталось еще пять колеблющихся инвесторов..."
    biff "Цыпочка должна проявить свои таланты убеждения..."
    img 12865
    with diss
    biff "Полученные ею в прошлой жизни на грязной улице."
    biff "Иначе цыпочка рискует вернуться к ней!"
    # Моника
    music Power_Bots_Loop
    img 12792
    with fade
    mt "!!!"
    mt "Вот сволочь!!!"
    return


label ep211_dialogues3_photoshoot_8b:
    mt "НОГИ МОЕЙ ЗДЕСЬ БОЛЬШЕ НЕ БУДЕТ, ПОКА МОЕ МЕСТО ЗАНИМАЕТ ЭТОТ МЕРЗАВЕЦ!!!"
    mt "Я ДОСТАТОЧНО УМНА, ЧТОБЫ НАЙТИ ДРУГОЙ ПУТЬ РЕШИТЬ СВОИ ПРОБЛЕМЫ!!!"
    return False
