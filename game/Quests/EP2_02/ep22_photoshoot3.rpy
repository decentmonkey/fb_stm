default photoshoot3_count = 0

label ep22_photoshoot3:
    music Groove2_85
    img 8384
    with fade
    m "Алекс, это что? Какая-то шутка?"
    "Кто-то перепутал коробку для нарядов с одеждой для рабочих???"
    img 8385
    alex_photograph "Нет, Мэм!"
    "Вы сегодня девушка-рабочий! Бригадир!"
    img 8386
    with fade
    m "Какого черта, Алекс?!?!"
    "Ты не забыл вообще-то кто я такая?!"
    alex_photograph "Мэм! Это распоряжение Мистера Бифа!"
    "У нас контракт с крупной строительной компанией!"
    "И, в конце концов, это всего-лишь образ, Миссис Бакфетт!"
    img 8387
    m "Эти штуки... Какие-то... Я не знаю как они называются..."
    "Можно я сниму их? Я могу пораниться!"
    alex_photograph "Нет, Мэм! Это часть образа!"
    img 8388
    with fade
    m "Ладно... Только давай без своих грязных ракурсов..."
    alex_photograph "Так точно, Мэм!"

    $ shotsAmount = PS1_shots_amount
    $ shotsTotalAmount = 21

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img 8389
    with fade
    alex_photograph "Мотор!"
    label ep22_photoshoot3_pose1:
        #кадр
        img 8389
        #up
#        img 8390
        #side
#        img 8391
        #down
#        img 8392

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            img 8393
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            m "Алекс! Ты снова начинаешь?!"
            "Мы не успели начать, а у тебя уже двусмысленные позы!"
            alex_photograph "Мэм! Эти фото на календарь строительной компании!"
            "Вы будете стимулировать рабочих трудиться лучше!"
            "Вы должны быть соблазнительны!"

            m "Не вижу в этом ничего соблазнительного, Алекс!"
            mt "О БОЖЕ! Я фотографируюсь на календарь для рабочих!"
            "Я - МОНИКА БАКФЕТТ!!"
            "О БОЖЕ!!!"
            music stop
            jump ep22_photoshoot3_pose2
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8390, 8391, 8392], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8390
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_75
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8391
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_76
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8392
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_77
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose1



    label ep22_photoshoot3_pose2:
        #кадр
        img 8393

        #up
#        img 8394
        #side+
#        m "Алекс! Не начинай!"
        #иначе
#        img 8395

        #down+
#        m "Алекс! Хватит!"
        #иначе
#        img 8396

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8397
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot3_pose3
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8394, 8395, 8396], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8394
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_78
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose2
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8395
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot1_corruption_required:
                m "Алекс! Не начинай!"
                call corruption_required(PS3_monica_shot1_corruption_required) from _call_corruption_required_21
                jump ep22_photoshoot3_pose2
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot1_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_79
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose2
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8396
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot2_corruption_required:
                m "Алекс! Хватит!"
                call corruption_required(PS3_monica_shot2_corruption_required) from _call_corruption_required_22
                jump ep22_photoshoot3_pose2
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot2_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_80
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose2




    label ep22_photoshoot3_pose3:
        #кадр
        img 8397

        #up
#        img 8398

        #side
#        img 8399

        #down
#        img 8400


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8401
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            if corruption < PS3_monica_pose3_corruption_required:
                call corruption_required(PS3_monica_pose3_corruption_required) from _call_corruption_required_23
                m "Алекс! Я не буду вставать в такую развратную позу!"
                "И это не обсуждается!"
                return
            jump ep22_photoshoot3_pose4
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8398, 8399, 8400], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8398
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_81
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8399
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_82
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8400
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_83
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose3



    label ep22_photoshoot3_pose4:
        #кадр
        img 8401
        #иначе
        #up
#        img 8402
        #side+
#        m "Алекс! Я не буду делать такой кадр!"
#        img 8403

        #down+
#        m "Алекс! Забудь про такие ракурсы!"
#        img 8404

        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8405
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot3_pose5
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8402, 8403, 8404], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8402
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_84
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose4
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8403
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot3_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS3_monica_shot3_corruption_required) from _call_corruption_required_24
                jump ep22_photoshoot3_pose4
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot3_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_85
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose4
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8404
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot4_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS3_monica_shot4_corruption_required) from _call_corruption_required_25
                jump ep22_photoshoot3_pose4
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot4_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_86
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose4


    label ep22_photoshoot3_pose5:
        #кадр
        img 8405

        #up
#        img 8406

        #side
#        img 8407
#        img 8408

        #down+
#        m "Алекс! Я не буду делать такой кадр!"
#        img 8409


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8410
            with fadelong
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            jump ep22_photoshoot3_pose6
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8406, 8407, 8409], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8406
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_87
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8407
            img photoImage
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_38
            w
            img 8408
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_88
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose5
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8409
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot5_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS3_monica_shot5_corruption_required) from _call_corruption_required_26
                jump ep22_photoshoot3_pose5
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot5_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_89
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose5



    label ep22_photoshoot3_pose6:
        #кадр
        img 8410

        #up+ (жесткий)
#        alex_photograph "Миссис Бакфетт!"
#        "Возьмите, пожалуйста, молоток и сделайте вид, как-будто вы его лижите."
#        "Сексуально."
#        "Это будет самый популярный кадр!"
#        #если не хватает
#        m "ЧТО??!"
#        "НИКОГДА!"
#        alex_photograph "Миссис Бакфетт! Но молоток чистый! Это реквизит!"
#        "Я специально подготовил его!"
#        "НИКОГДА!"
#        #иначе
#        m "Алекс!"
#        "Это последнее что я сделаю!"
#        "Ты меня достал своей назойливостью!"
#        img 8413
#        img 8414
#        img 8415
#        img 8416
#        img 8417
#
#        #side
#        img 8411
#
#        #down+
#        m "Алекс! Забудь про такие ракурсы!"
#        img 8412


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            alex_photograph "Следующая поза, Миссис Бакфетт!"
            "Пожалуйста, сядьте на колени и выдвиньте одну ногу вперед!"
            m "Хорошо, звучит не так уж страшно..."
            music Groove2_85
            img 8419
            with fadelong
            m "ЧТО?!?!"
            "ЧТО ТЫ СДЕЛАЛ, МЕРЗАВЕЦ???"
            "Куда ты поставил молоток!"
            "Ты хоть заметил куда в какое место он упирается мне?!?!"
            alex_photograph "Миссис Бакфетт!"
            "И сделайте, пожалуйста, такое лицо как когда Вы облизывали молоток..."
            if corruption < PS3_monica_pose6_corruption_required:
                call corruption_required(PS3_monica_pose6_corruption_required) from _call_corruption_required_27
                #если не хватает
                m "ЧТО?!?!"
                "Иди ты к черту!"
                "Это называется фотосессия для календаря?!?!"
                "Может быть мне еще снять шорты и дать ему свободу войти туда куда он упирается сейчас?!"
                alex_photograph "..."
                m "Ах! Что я спрашиваю!"
                "Для тебя это было бы прекрасной новостью!"
                "НО НЕ ДЛЯ МЕНЯ?!?!"
                "Фотосессия закончена!!!"
                #уходим на конец фотосессии
                return

            #если хватает
            alex_photograph "Мэм, я понимаю, может быть Вам неудобно как он упирается..."
            "Но если Вам чуточку приятно это, то, пожалуйста, высуньте язычок..."
            "Без него композиция будет неполной..."
            "А ведь Вы знаете, что от меня ждут лучших результатов."
            "Иначе Мистер Биф уволит меня..."
            "Поверьте, этот кадр выглядит прилично..."
            m "..."
            "Алекс, это точно выглядит прилично?"
            alex_photograph "Да, Мэм!"
            "Поверьте мне!"
            m "Мне это не нравится, Алекс..."
            alex_photograph "Миссис Бакфетт... Не переживайте, я сделаю кадры быстрее чем будет заметно что Вы стали влажной..."
            m "ЧТО?!?!..."
            alex_photograph "Я снимаю, Миссис Бакфетт!"
            "Пожалуйста, покажите эмоции!"
            m "Я...."
            "Ладно..."
            music stop
            img 8418
            with fadelong
            jump ep22_photoshoot3_pose7
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8413, 8411, 8412], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose6
        #up
        if result == "up":
            alex_photograph "Миссис Бакфетт!"
            "Возьмите, пожалуйста, молоток и сделайте вид, как-будто вы его лижите."
            "Сексуально."
            "Это будет самый популярный кадр!"
            if corruption < PS3_monica_shot6_corruption_required:
                m "ЧТО??!"
                "НИКОГДА!"
                alex_photograph "Миссис Бакфетт! Но молоток чистый! Это реквизит!"
                "Я специально подготовил его!"
                "НИКОГДА!"
                call corruption_required(PS3_monica_shot6_corruption_required) from _call_corruption_required_28
                jump ep22_photoshoot3_pose5
            m "Алекс!"
            "Это последнее что я сделаю!"
            "Ты меня достал своей назойливостью!"
            sound camera_lens1
            $ photoImage = 8413
            img photoImage
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_39
            w
            img 8414
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_40
            w
            img 8415
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_41
            w
            img 8416
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_42
            w
            img 8417
            w
            call photoshop_flash() from _call_photoshop_flash_43
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot6_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_90
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8411
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_91
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose6
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8412
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot7_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS3_monica_shot7_corruption_required) from _call_corruption_required_29
                jump ep22_photoshoot3_pose5
            w
            $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot7_progress")
            call photoshoot_flash_count() from _call_photoshoot_flash_count_92
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose6


    label ep22_photoshoot3_pose7:

        #кадр
        img 8418

#        #up
#        img 8420
#        w
#        img 8421
#        w
#        img 8422
#        w
#        img 8423
#        w
#        img 8424
#        w
#
#        #side
#        img 8425
#        w
#        img 8426
#        w
#        img 8427
#        w
#        img 8428
#        w
#
#        #down
#        img 8429
#        w
#        img 8430
#        w
#        img 8431
#        w
#        img 8432
#        w
#        img 8433
#        w


        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            return
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot2([8420, 8425, 8429], PS3_shoots_array)
        $ result = ui.interact()
        hide screen photoshoot2
        if result == "next":
            $ shots = 0
            jump ep22_photoshoot3_pose7
        #up
        if result == "up":
            sound camera_lens1
            img 8420
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_44
            w
            img 8421
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_45
            w
            img 8422
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_46
            w
            img 8423
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_47
            w
            img 8424
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_48
            w
            $ photoImage = 8420
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_93
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose7
        if result == "side":
            #side
            sound camera_lens1
            img 8425
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_49
            w
            img 8426
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_50
            w
            img 8427
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_51
            w
            img 8428
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_52
            w
            $ photoImage = 8425
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_94
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose7
        if result == "down":
            #down
            sound camera_lens1
            img 8429
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_53
            w
            img 8430
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_54
            w
            img 8431
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_55
            w
            img 8432
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_56
            w
            img 8433
            with Dissolve(0.2)
            w
            call photoshop_flash() from _call_photoshop_flash_57
            w
            $ photoImage = 8429
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _call_photoshoot_flash_count_95
            $ PS3_shoots_array.append(photoImage)
            w
            jump ep22_photoshoot3_pose7

    return

label ep22_photoshoot3_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2

    $ shotsAmountCompleted = len(list(set(PS3_shoots_array)))
#    $ shotsTotalAmount
    if questHelpFlag20 == False:
        $ questHelpFlag20 = True
#        $ questHelpDesc("photoshoot_desc3", "photoshoot_desc10")

#    $ questHelp("office_16", skipIfExists=True)
    $ questHelp("photoshoot_10", skipIfExists=True)
    $ questHelp("photoshoot_3", True)
    $ questHelp("photoshoot_3a", skipIfExists=True)
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_10", True)

    $ monicaOutfitsEnabled[3] = True # Открываем следующий костюм
    music Stealth_Groover
    img 8434
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 8435
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot3_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep22_photoshoot3_casting() from _call_ep22_photoshoot3_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot3_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot3_casting_corruption_required:
            pass

    return

label ep22_photoshoot3_casting:
    music Groove2_85
    sound highheels_short_walk
    img 8463
    with fadelong
    w
    img 8464
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."
    img 8465
    $ add_char_progress("Biff", PS3_BiffProgressCasting, "PS3_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS3_shoots_array)))
#    $ shotsTotalAmount
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 8467
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 8468
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это девушка-рабочий с календаря, который будет висеть у каждого менеджера строительной компании..."
            $ add_char_progress("Biff", PS3_BiffProgressCastingChick, "PS3_BiffProgressCastingChick_day" + str(day))
            biff "Что девушка с календаря хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 3
            call ep22_casting() from _call_ep22_casting_6
            img 8480
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 8466
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 3
            $ chickMode = False
            call ep22_casting() from _call_ep22_casting_7
            img 8480
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
