default photoshoot6_count = 0

label ep26_photoshoot_suit6:
    music Groove2_85
    $ shotsAmount = PS6_shots_amount
    $ shotsTotalAmount = 33

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20001
    with fadelong
    m "Что это, Алекс?"
    # Что это?
    img 20002
    with diss
    m "Это что, называется костюм для съемок?"
    # Это что, называется костюм для съемок?
    img 20003
    with diss
    # А это что такое?
    m "А это что такое?"
    img 20004
    with fade
    # Миссис Бакфетт, это реквизит и тд
    alex_photograph "Миссис Бакфетт, этот костюм называется Алая Жемчужина"
    alex_photograph "А этот реквизит олицетворяет раковину, в которой находится изысканная жемчужина!"
    alex_photograph "Это будет замечательная сцена, Миссис Бакфетт!"
    img 20005
    with diss
    # И что мне делать на этой кушетке?
    m "И что мне делать на этой... раковине?"
    img 20006
    with fade
    # Проходить фотосессию
    alex_photograph "Миссис Бакфетт, Вам надо принимать различные позы."
    alex_photograph "Читателям должно понравиться то, как Вы будете выглядеть!"

    img 20007
    with fade
    # Ладно, Алекс!
    # Только на этот раз без пошлых поз!
    m "Ладно, Алекс."
    m "Только на этот раз без пошлых поз!"

    music Molten_Alloy
    img 20008
    with diss
    alex_photograph "Конечно, Миссис Бакфетт! Все будет очень прилично, как обычно!"
    alex_photograph "Итак, мотор!"
    music stop
    img 20009
    with fadelong

$ photoPoseLabel = "ep26_photoshoot_suit6_pose1"
$ photoPoseNextLabel = "ep26_photoshoot_suit6_pose2"
label ep26_photoshoot_suit6_pose1:
    #кадр
    img 20009
    # up
#    img 20011
    # side
#    img 20010
    # down
#    img 20012
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20013
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20011, 20010, 20012], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20011
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_120
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20010
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_121
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20012
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_122
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit6_pose2:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose2"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose3"
    # кадр
    img 20013
    # up
#    img 20014
    # side
#    img 20015
    # down
#    img 20016
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        # кадр+
        img 20017
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        if corruption < PS6_monica_pose3_corruption_required:
            m "Алекс! Я не буду вставать в позу, будто показываю задницу!"
            "И это не обсуждается!"
            call corruption_required(PS6_monica_pose3_corruption_required) from _call_corruption_required_36
            return
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot1_progress")
        m "Алекс, мне не нравится это поза!"
        m "Постарайся поменьше фокусировать камеру на месте ниже спины!"
        alex_photograph "Конечно, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20014, 20015, 20016], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20014
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_123
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20015
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_124
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20016
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_125
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit6_pose3:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose3"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose4"
    # кадр +
    img 20017
    # up
#    img 20019
    # side
#    img 20018
    # down
#    img 20020
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20021
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20019, 20018, 20020], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20019
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_126
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20018
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_127
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20020
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_128
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit6_pose4:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose4"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose5"
    # кадр
    img 20021
    # up
#    img 20022
    # side +
#    img 20024
    # down
#    img 20023
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20025
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20022, 20024, 20023], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20022
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_129
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side+
        sound camera_lens1
        $ photoImage = 20024
        img photoImage
        with Dissolve(0.2)
        if corruption < PS6_monica_shot1_corruption_required:
            m "Алекс! Забудь про такие ракурсы!"
            call corruption_required(PS6_monica_shot1_corruption_required) from _call_corruption_required_37
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_130
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot3_progress")
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20023
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_131
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit6_pose5:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose5"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose6"
    # кадр
    img 20025
    # up
#    img 20026
    # side
#    img 20027
    # down
#    img 20028

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20029
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20026, 20027, 20028], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20026
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_132
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20027
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_133
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20028
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_134
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit6_pose6:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose6"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose7"
    # кадр
    img 20029
    # up
#    img 20030
    # side
#    img 20031
    # down
#    img 20032

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20033
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20030, 20031, 20032], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20030
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_135
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20031
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_136
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20032
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_137
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit6_pose7:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose7"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose8"

    # кадр
    img 20033
    # up
#    img 20034
    # side
#    img 20035
    # down +
#    img 20036
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20037
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20034, 20035, 20036], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20034
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_138
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20035
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_139
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20036
        img photoImage
        with Dissolve(0.2)
        m "Алекс! Зачем ты оттуда фотографируешь?"
        m "Что ты хочешь там увидеть?!"
        if corruption < PS6_monica_shot2_corruption_required:
            call corruption_required(PS6_monica_shot2_corruption_required) from _call_corruption_required_38
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я фотографирую Ваши ножки!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_140
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot4_progress")
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit6_pose8:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose8"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose9"
    # кадр
    img 20037
    # up
#    img 20038
    # side
#    img 20039
    # down +
#    img 20040
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20041
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20038, 20039, 20040], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20038
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_141
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20039
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_142
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20040
        img photoImage
        with Dissolve(0.2)
        if corruption < PS6_monica_shot3_corruption_required:
            m "Алекс! Я не буду делать такой кадр!"
            call corruption_required(PS6_monica_shot3_corruption_required) from _call_corruption_required_39
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_143
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot5_progress")
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit6_pose9:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose9"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose10"

    # кадр
    img 20041
    # up
#    img 20042
#    img 20043
    # side
#    img 20044
#    img 20045
    # down +
#    img 20046
#    img 20047
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20048
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20043, 20045, 20047], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20042
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_103
        w
        $ photoImage = 20043
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_144
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20044
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_104
        w
        $ photoImage = 20045
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_145
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20046
        with Dissolve(0.2)
        if corruption < PS6_monica_shot4_corruption_required:
            m "Алекс! Забудь про такие ракурсы!"
            call corruption_required(PS6_monica_shot4_corruption_required) from _call_corruption_required_40
            jump expression photoPoseLabel
        w
        call photoshop_flash() from _call_photoshop_flash_105
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot6_progress")
        w
        $ photoImage = 20047
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_146
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit6_pose10:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose10"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose11"
    # кадр
    img 20048
    # up
#    img 20049
#    img 20050
#    img 20051
    # side
#    img 20052
#    img 20053
#    img 20054
    # down+
#    img 20055
#    img 20056
    #+
#    img 20057
#    img 20058
#    img 20059
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
    # кадр +
        img 20060
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        m "Алекс! Я не буду вставать в такую развратную позу!"
        "И это не обсуждается!"
        if corruption < PS6_monica_pose10_corruption_required:
            call corruption_required(PS6_monica_pose10_corruption_required) from _call_corruption_required_41
            return
        alex_photograph "Миссис Бакфетт, это сюжетная поза."
        alex_photograph "Раковина, как-бы раскрывается, обнажая жемчужину!"
        m "Я не собираюсь обнажать никакую... жемчужину!"
        alex_photograph "Миссис Бакфетт, не волнутесь, я буду фотографировать только сбоку!"
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot7_progress")
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20051, 20054, 20059], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20049
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_106
        w
        img 20050
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_107
        w
        $ photoImage = 20051
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_147
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20052
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_108
        w
        img 20053
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_109
        w
        $ photoImage = 20054
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_148
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20055
        with Dissolve(0.2)
        m "Алекс! Я не буду делать такой кадр!"
        m "Что это за поза?"
        if corruption < PS6_monica_shot5_corruption_required:
            call corruption_required(PS6_monica_shot5_corruption_required) from _call_corruption_required_42
            jump expression photoPoseLabel
        alex_photograph "Это прекрасная поза, Миссис Бакфетт!"
        w
        call photoshop_flash() from _call_photoshop_flash_110
        w
        img 20056
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_111
        w
        img 20057
        with Dissolve(0.2)
        m "Алекс! Хватит!"
        m "Что ты там хочешь сфотографировать?!"
        if corruption < PS6_monica_shot6_corruption_required:
            call corruption_required(PS6_monica_shot6_corruption_required) from _call_corruption_required_43
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я хочу сфотографировать Ваш чудесный педикюр!"
        w
        call photoshop_flash() from _call_photoshop_flash_112
        w
        img 20058
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_113
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot8_progress")
        w
        $ photoImage = 20059
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_149
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit6_pose11:
    $ photoPoseLabel = "ep26_photoshoot_suit6_pose11"
    $ photoPoseNextLabel = "ep26_photoshoot_suit6_pose12"
    # кадр +
    img 20060
    # up
#    img 20061
#    img 20062
#    img 20063
    # side
#    img 20064
#    img 20065
#    img 20066
    # down +
#    img 20067
#    img 20068
#    img 20069
    #+
#    img 20070
#    img 20071
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        return
    show screen photoshoot_camera_icon(PS6_shoots_array)
    show screen photoshoot2([20063, 20066, 20071], PS6_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20061
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_114
        w
        img 20062
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_115
        w
        $ photoImage = 20063
        img photoImage
        with Dissolve(0.2)
        m "Я слежу за тобой, Алекс!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_150
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20064
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_116
        w
        img 20065
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_117
        w
        $ photoImage = 20066
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_151
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20067
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_118
        w
        img 20068
        with Dissolve(0.2)
        m "Алекс, твою мать! Это называется вид сбоку?"
        if corruption < PS6_monica_shot7_corruption_required:
            call corruption_required(PS6_monica_shot7_corruption_required) from _call_corruption_required_44
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, это вид снизу!"
        alex_photograph "На нем видны только Ваши пальчики на ногах и больше ничего!"
        w
        call photoshop_flash() from _call_photoshop_flash_119
        w
        img 20069
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_120
        w
        img 20070
        with Dissolve(0.2)
        m "Алекс! Это тоже вид снизу?!"
        if corruption < PS6_monica_shot8_corruption_required:
            call corruption_required(PS6_monica_shot8_corruption_required) from _call_corruption_required_45
            jump expression photoPoseLabel
        alex_photograph "Да, Миссис Бакфетт!"
        alex_photograph "Но не волнуйтесь, костюм плотно все закрывает!"
        m "Точно?!"
        alex_photograph "Да, Миссис Бакфетт! Всего один кадр!"
        m "Только один! И не ближе!"
        alex_photograph "Конечно!"
        w
        call photoshop_flash() from _call_photoshop_flash_121
        w
        $ photoImage = 20071
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_152
        $ add_char_progress("AlexPhotograph", PS6_AlexProgressEachCorruptionShot, "PS6_monica_shot9_progress")
        $ PS6_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    return

label ep26_photoshoot_suit6_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2

    if questHelpFlag22 == False:
        $ questHelpFlag22 = True
#        $ questHelpDesc("photoshoot_desc5", "photoshoot_desc11")


    $ shotsAmountCompleted = len(list(set(PS6_shoots_array)))
#    $ shotsTotalAmount
#    $ questHelp("office_20", skipIfExists=True)
    $ questHelp("photoshoot_5", True)
    $ questHelp("photoshoot_11", skipIfExists=True)
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_11", True)

    music Groove2_85
    img 20072
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 20073
    with fade
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot4_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep26_photoshoot6_casting() from _call_ep26_photoshoot6_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot6_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot6_casting_corruption_required:
            pass
    return

label ep26_photoshoot6_casting:
    music Groove2_85
    sound highheels_short_walk
    img 20176
    with fadelong
    w
    img 20177
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 20178
    $ add_char_progress("Biff", PS6_BiffProgressCasting, "PS6_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS6_shoots_array)))
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 20179
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 20180
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Алая Жемчужина..."
            $ add_char_progress("Biff", PS6_BiffProgressCastingChick, "PS6_BiffProgressCastingChick_day" + str(day))
            biff "Что Алая Жемчужина хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 6
            call ep22_casting() from _call_ep22_casting_10

            img 20183 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 20182 #9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 6
            $ chickMode = False
            call ep22_casting() from _call_ep22_casting_11
            img 20183 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
