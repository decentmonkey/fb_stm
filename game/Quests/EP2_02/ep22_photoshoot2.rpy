default photoshoot2_count = 0

label ep22_photoshoot2:
    music Groove2_85
    img 8350
    with fade
    m "Алекс, это что?"
    "Наряд Леди Нуар?"
    img 8351
    alex_photograph "Видимо да, Миссис Бакфетт!"
    m "И ты считаешь мне это идет?"
    alex_photograph "О, Миссис Бакфетт!"
    "Вам идет все, если взять правильный ракурс съемки!"
    img 8352
    m "Знаю я твои правильные ракурсы..."

    $ shotsAmount = PS1_shots_amount
    $ shotsTotalAmount = 21
#    music Molten_Alloy_low
    music stop

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    img 8353
    with fadelong
    alex_photograph "Мотор!"

    label ep22_photoshoot2_pose1:
        #кадр
        img 8353
        #up
#        img 8354
        #side
#        img 8355
        #down
#        img 8356

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8357
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot2_pose2
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8354, 8355, 8356], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8354
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8355
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_1
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8356
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_2
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose1


    label ep22_photoshoot2_pose2:
        #кадр
        img 8357
        #up
#        img 8358
        #side +
#        m "Эй! Хватит брать свои правильные ракурсы!"
#        img 8359
        #down
#        img 8360

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8361
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot2_pose3
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8358, 8359, 8360], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8358
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_3
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose2
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8359
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot1_corruption_required:
                m "Эй! Хватит брать свои правильные ракурсы!"
                call corruption_required(PS2_monica_shot1_corruption_required) from _call_corruption_required
                jump ep22_photoshoot2_pose2
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot1_progress")
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_4
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose2
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8360
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_5
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose2


    label ep22_photoshoot2_pose3:
        #кадр
        img 8361
        #up
#        img 8362
        #side
#        img 8363
        #down +
#        img 8364

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8365
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot2_pose4
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8362, 8363, 8364], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8362
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_6
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8363
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_7
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose3
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8364
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot2_corruption_required:
                m "Эй! Хватит брать свои правильные ракурсы!"
                call corruption_required(PS2_monica_shot2_corruption_required) from _call_corruption_required_1
                jump ep22_photoshoot2_pose3
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot2_progress")
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_8
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose3


    label ep22_photoshoot2_pose4:
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
        #кадр
        img 8365
        #up
#        img 8366
        #side
#        img 8367
        #down+
#        m "Эй! Ты что делаешь?!"
#        "Ты что не видишь что у меня там ничего нет?!"
#        "Хотя только попробуй увидь!"
        #иначе
#        m "Алекс, не вздумай подвинуть камеру ни на градус!"
#        alex_photograph "Хорошо, Мэм!"
#        img 8368


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8369
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            if corruption < PS2_monica_pose5_corruption_required:
                call corruption_required(PS2_monica_pose5_corruption_required) from _call_corruption_required_2
                m "Эй! Алекс!"
                "Я не собираюсь делать снимки в такой позе!"
                return
            jump ep22_photoshoot2_pose5
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8366, 8367, 8368], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8366
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_9
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8367
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_10
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose4
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8368
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot3_corruption_required:
                m "Эй! Ты что делаешь?!"
                "Ты что не видишь что у меня там ничего нет?!"
                "Хотя только попробуй увидь!"
                call corruption_required(PS2_monica_shot3_corruption_required) from _call_corruption_required_3
                jump ep22_photoshoot2_pose4
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            alex_photograph "Хорошо, Мэм!"
            w
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot3_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_11
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose4



    label ep22_photoshoot2_pose5:
        #кадр
        img 8369
        #иначе
        #up
#        img 8371
        #side
#        img 8370
        #down+
#        m "Алекс! Даже не думай об этом!"
        #иначе
#        m "Алекс, не вздумай подвинуть камеру ни на градус!"
#        img 8372

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8373
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot2_pose6
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8371, 8370, 8372], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8371
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_12
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8370
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_13
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose5
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8372
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot4_corruption_required:
                m "Алекс! Даже не думай об этом!"
                call corruption_required(PS2_monica_shot4_corruption_required) from _call_corruption_required_4
                jump ep22_photoshoot2_pose5
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            w
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot4_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_14
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose5


    label ep22_photoshoot2_pose6:
        #кадр
        img 8373
        #up
#        img 8374
        #side
#        img 8375
        #down +
#        m "Алекс! Даже не думай об этом!"
        #иначе
#        m "Алекс, не вздумай подвинуть камеру ни на градус!"
#        img 8376

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8377
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            music Groove2_85
            m "Алекс! Ты сошел с ума?!"
            "У меня платье натянулось, оно сейчас поднимется!"
            alex_photograph "Миссис Бакфетт! Это необходимо!"
            "Вы - Леди Нуар!"
            "Это, как бы, послание. Раскрытие сущности добра, которое находится вглубине Вас!"
            m "Какое раскрытие сущности добра?!"
            "Показывая жопу?!"
            alex_photograph "Миссис Бакфетт!"
            "Всего несколько кадров!"

            if corruption < PS2_monica_pose7_corruption_required:
                m "Даже не думай!"
                call corruption_required(PS2_monica_pose7_corruption_required) from _call_corruption_required_5
                mt "О Боже! Зачем я связалась с этими фотосессиями!!!"
                "Если бы только у меня был выбор!"
                return
            m "Хорошо, только быстро!"
            "И не бери камеру слишком низко!"
            alex_photograph "Конечно, Мэм!"
            music stop
            jump ep22_photoshoot2_pose7
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8374, 8375, 8376], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose6
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8374
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_15
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8375
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_16
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose6
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8376
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot5_corruption_required:
                m "Алекс! Даже не думай об этом!"
                call corruption_required(PS2_monica_shot5_corruption_required) from _call_corruption_required_6
                jump ep22_photoshoot2_pose5
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            w
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot5_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_17
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose6


    label ep22_photoshoot2_pose7:
        #
        img 8377

        #up
#        img 8378
        #side+
#        m "Даже не думай брать этот ракурс!"
        #иначе
#        m "Алекс, не вздумай подвинуть камеру ни на градус!"
#        img 8379

        #down+
#        m "Алекс, даже не вздумай снимать с этой стороны!"
        #иначе
#        img 8380
#        alex_photograph "Мэм! Могли бы вы убрать руки?"
#        m "НЕТ!!!"
#        "Алекс! Платье сразу поднимется!!!"
#        "У меня под ним ничего нет!!!"
        #далее
#        img 8381
#        m "ТЫ ЧТО НЕ ПОНЯЛ МЕНЯ!!!"
#        "ХВАТИТ!!!"
        #иначе фото
#        m "Алекс! Зачем ты сделал фото?!"
#        "Удали его немедленно!"
#        alex_photograph "Мэм! Не переживайте!"
#        "Оно получилось в затемнении и там ничего не видно!"


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            return
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot2([8378, 8379, 8380], PS2_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot2_pose7
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8378
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_18
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose7
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8379
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot6_corruption_required:
                m "Даже не думай брать этот ракурс!"
                call corruption_required(PS2_monica_shot6_corruption_required) from _call_corruption_required_7
                jump ep22_photoshoot2_pose7
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            w
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot6_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_19
            $ PS2_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot2_pose7
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8380
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot7_corruption_required:
                m "Алекс, даже не вздумай снимать с этой стороны!"
                call corruption_required(PS2_monica_shot7_corruption_required) from _call_corruption_required_8
                jump ep22_photoshoot2_pose7
            alex_photograph "Мэм! Могли бы вы убрать руки?"
            m "НЕТ!!!"
            "Алекс! Платье сразу поднимется!!!"
            "У меня под ним ничего нет!!!"
            w
            call photoshop_flash() from _call_photoshop_flash_25
            w
            #далее
            img 8381
            with Dissolve(0.2)
            if corruption < PS2_monica_shot8_corruption_required:
                m "ТЫ ЧТО НЕ ПОНЯЛ МЕНЯ!!!"
                "ХВАТИТ!!!"
                call corruption_required(PS2_monica_shot8_corruption_required) from _call_corruption_required_9
                jump ep22_photoshoot2_pose7
            #иначе фото
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_20
            w
            m "Алекс! Зачем ты сделал фото?!"
            "Удали его немедленно!"
            alex_photograph "Мэм! Не переживайте!"
            "Оно получилось в затемнении и там ничего не видно!"
            $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot7_progress")
            $ PS2_shoots_array.append(photoImage)
            jump ep22_photoshoot2_pose7

    return


label ep22_photoshoot2_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2

    music Stealth_Groover
    $ monicaOutfitsEnabled[2] = True # Открываем следующий костюм

    $ questHelp("photoshoot_3", skipIfExists=True)
#    if questHelpFlag7Worker == False:
#        $ questHelpDesc("photoshoot_desc3")

    $ shotsAmountCompleted = len(list(set(PS2_shoots_array)))
    $ questHelp("photoshoot_2", True)
#    $ questHelp("office_14", skipIfExists=True)

    if questHelpFlag19 == False:
        $ questHelpFlag19 = True
#        $ questHelpDesc("photoshoot_desc2", "photoshoot_desc9")
        $ questHelpDesc("office_desc7", "office_desc8")
    $ questHelp("photoshoot_9", skipIfExists=True)
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_9", True)

#    $ shotsTotalAmount

    img 8382
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 8383
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot2_casting_corruption_required : #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep22_photoshoot2_casting() from _call_ep22_photoshoot2_casting
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot2_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot2_casting_corruption_required:
            pass

return

label ep22_photoshoot2_casting:
    music Groove2_85
    sound highheels_short_walk
    img 8447
    with fadelong
    w
    img 8448
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."
    img 8449
    $ add_char_progress("Biff", PS2_BiffProgressCasting, "PS2_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS2_shoots_array)))
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 8451
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 8452
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Леди Нуар..."
            $ add_char_progress("Biff", PS2_BiffProgressCastingChick, "PS2_BiffProgressCastingChick_day" + str(day))
            biff "Что Леди Нуар хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 2
            call ep22_casting() from _call_ep22_casting
            img 8462
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 8450
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 2
            $ chickMode = False
            call ep22_casting() from _call_ep22_casting_1
            img 8462
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
