default photoshoot7_count = 0

label ep26_photoshoot_suit7:
    music Groove2_85
    $ shotsAmount = PS7_shots_amount
    $ shotsTotalAmount = 33
#    $ shotsAmount = 33 #debug

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20074
    with fadelong
    m "Алекс! Ты что, сошел с ума?!"
    m "У этого костюма прозрачная грудь!"
    m "Я уже не говорю про трусики, которых почти нет!"
    alex_photograph "Но Мэм..."

    img 20075
    m "Никаких Мэм!"
    m "Я не собираюсь обнажаться на эту чертову камеру!"
    img 20076
    with fade
    alex_photograph "Мэм, этот наряд называется Запретное Желание."
    alex_photograph "И, если Вы хотите, Вы можете закрывать грудь руками..."
    img 20077
    with diss
    m "Да, я буду закрывать грудь руками!"
    m "И только на этом условии я соглашаюсь на съемку!"
    mt "Черт! Куда эти фотосессии меня доведут..."

    music Molten_Alloy
    img 20078
    with fade
    alex_photograph "Мэм, отлично, мы договорились!"
    alex_photograph "Итак, мотор!"

    music stop
    img 20079
    with fadelong


$ photoPoseLabel = "ep26_photoshoot_suit7_pose1"
$ photoPoseNextLabel = "ep26_photoshoot_suit7_pose2"
label ep26_photoshoot_suit7_pose1:
    # кадр
    img 20079
    # up
#    img 20080
    # side
#    img 20081
    # down +
#    img 20082

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20083
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20080, 20081, 20082], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20080
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_153
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20081
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_154
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20082
        img photoImage
        with Dissolve(0.2)
        m "Алекс, эти стринги совсем тонкие."
        m "Постарайся не брать ракурсы сзади."
        alex_photograph "Мэм, но Вы и так закрываете грудь."
        alex_photograph "Я ведь должен что-то снимать..."
        m "Снимай мое лицо, болван!"
        if corruption < PS7_monica_shot1_corruption_required:
            call corruption_required(PS7_monica_shot1_corruption_required) from _call_corruption_required_46
            jump expression photoPoseLabel
        # если можно
        alex_photograph "Миссис Бакфетт?"
        m "Ладно, только так чтобы было ничего не видно!"
        alex_photograph "Конечно, Миссис Бакфетт! Как скажете!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_155
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot1_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel



label ep26_photoshoot_suit7_pose2:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose2"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose3"
    # кадр
    img 20083
    # up
#    img 20084
    # side
#    img 20085
    # down
#    m "Алекс, ты снова за свое?!"
#    img 20086

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20087
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        music Groove2_85
        m "Алекс, я не хочу вставать в эту позу!"
        m "Трусики слишком тонкие!"
        alex_photograph "Миссис Бакфетт, я буду брать ракурсы так, чтобы ничего не было видно, обещаю!"
        m "Ну, ладно... Но смотри у меня!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20084, 20085, 20086], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20084
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_156
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20085
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_157
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20086
        img photoImage
        with Dissolve(0.2)
        m "Алекс, ты снова за свое?!"
        if corruption < PS7_monica_shot2_corruption_required:
            call corruption_required(PS7_monica_shot2_corruption_required) from _call_corruption_required_47
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_158
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot2_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit7_pose3:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose3"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose4"

    # кадр
    img 20087
    # up
#    img 20088
    # side
#    img 20089
#    img 20090
    # down +
#    img 20091
#    img 20092
#    m "Алекс! Я же попросила!"
#    alex_photograph "Миссис Бакфетт, я только замеряю фокус!"
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20093
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20088, 20090, 20092], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20088
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_159
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20089
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_122
        w
        $ photoImage = 20090
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_160
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20091
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_123
        w
        $ photoImage = 20092
        img photoImage
        with Dissolve(0.2)
        m "Алекс! Я же попросила!"
        if corruption < PS7_monica_shot3_corruption_required:
            call corruption_required(PS7_monica_shot3_corruption_required) from _call_corruption_required_48
            jump expression photoPoseLabel
        w
        alex_photograph "Миссис Бакфетт, я только замеряю фокус!"
        call photoshoot_flash_count() from _call_photoshoot_flash_count_161
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot3_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit7_pose4:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose4"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose5"

    # кадр
    img 20093
    # up
#    img 20094
    # side
#    img 20095
    # down
#    img 20096
#    m "Алекс, что за дурацкие ракурсы ты берешь?!"
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20097
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20094, 20095, 20096], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20094
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_162
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20095
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_163
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20096
        img photoImage
        with Dissolve(0.2)
        m "Алекс, что за дурацкие ракурсы ты берешь?!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_164
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit7_pose5:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose5"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose6"

    # кадр
    img 20097
    # up +
#    img 20098
#    m "Алекс, убери камеру!"
#    m "У меня видно грудь!"
#    alex_photograph "Миссис Бакфетт, ее не видно, клянусь!"
    # side
#    img 20099
    # down+
#    img 20100
#    m "Алекс, я устала тебя предупреждать!"
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20101
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20098, 20099, 20100], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20098
        img photoImage
        with Dissolve(0.2)
        m "Алекс, убери камеру!"
        m "У меня видно грудь!"
        if corruption < PS7_monica_shot4_corruption_required:
            call corruption_required(PS7_monica_shot4_corruption_required) from _call_corruption_required_49
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, ее не видно, клянусь!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_165
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot4_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20099
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_166
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20100
        img photoImage
        with Dissolve(0.2)
        m "Алекс, я устала тебя предупреждать!"
        if corruption < PS7_monica_shot5_corruption_required:
            call corruption_required(PS7_monica_shot5_corruption_required) from _call_corruption_required_50
            jump expression photoPoseLabel
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_167
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot5_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit7_pose6:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose6"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose7"

    # кадр
    img 20101
    # up
#    img 20102
    # side
#    img 20103
    # down+
#    img 20104
#    m "Алекс, ты глухой?!"
#    m "Не бери такие ракурсы!"
#    alex_photograph "Миссис Бакфетт, я просто обхожу Вас, чтобы зайти с другой стороны..."

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20105
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        m "Алекс, я не буду вставать в эту позу, даже не надейся!"
        m "У меня грудь почти открыта, прикрыты только соски!"
        if corruption < PS7_monica_pose6_corruption_required:
            call corruption_required(PS7_monica_pose6_corruption_required) from _call_corruption_required_51
            return
        # если да
        alex_photograph "Миссис Бакфетт, Ваша грудь обнажена не более, чем в приличном нижнем белье."
        alex_photograph "Не переживайте, ничего не видно."
        m "Точно?"
        alex_photograph "Да, Миссис Бакфетт!"
        m "Ладно, только без дурацких ракурсов!"
        m "Снимай меня прямо и... красиво..."
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20102, 20103, 20104], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20102
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_168
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20103
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_169
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20104
        img photoImage
        with Dissolve(0.2)
        m "Алекс, ты глухой?!"
        m "Не бери такие ракурсы!"
        if corruption < PS7_monica_shot6_corruption_required:
            call corruption_required(PS7_monica_shot6_corruption_required) from _call_corruption_required_52
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я просто обхожу Вас, чтобы зайти с другой стороны..."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_170
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot6_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep26_photoshoot_suit7_pose7:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose7"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose8"
    # кадр +
    img 20105
    # up
#    img 20106
    # side
#    img 20107
#    img 20108
#    img 20109
    # down
#    img 20110

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20111
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20106, 20109, 20110], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20106
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_171
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20107
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_124
        w
        img 20108
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_125
        w
        $ photoImage = 20109
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_172
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20110
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_173
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit7_pose8:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose8"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose9"
    # кадр
    img 20111
    # up
#    img 20112
#    m "Алекс!"
#    img 20113
    # side
#    img 20114
    # down +
#    img 20115
#    m "Алекс, перестань фотографировать меня сзади!"
#    # да
#    alex_photograph "Миссис Бакфетт, последний кадр..."
#    img 20116
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20117
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20113, 20114, 20116], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20112
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_126
        w
        $ photoImage = 20113
        img photoImage
        with Dissolve(0.2)
        m "Алекс!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_174
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20114
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_175
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20115
        with Dissolve(0.2)
        m "Алекс, перестань фотографировать меня сзади!"
        if corruption < PS7_monica_shot7_corruption_required:
            call corruption_required(PS7_monica_shot7_corruption_required) from _call_corruption_required_53
            jump expression photoPoseLabel
        w
        call photoshop_flash() from _call_photoshop_flash_127
        w
        $ photoImage = 20116
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Миссис Бакфетт, последний кадр..."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_176
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot7_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep26_photoshoot_suit7_pose9:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose9"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose10"


    # кадр
    img 20117
    # up
#    img 20118
    # side
#    img 20119
    # down +
#    img 20120
#    img 20121

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 20123
        with fadelong
        alex_photograph "Следующая поза, Миссис Бакфетт!"
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20118, 20119, 20122], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20118
        img photoImage
        with Dissolve(0.2)
        m "Алекс!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_177
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20119
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_178
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20120
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_128
        w
        img 20121
        with Dissolve(0.2)
        m "Все, Алекс!"
        m "Хватит с меня твоих грязных кадров!"
        m "Мы закончили!"
        if corruption < PS7_monica_shot8_corruption_required:
            call corruption_required(PS7_monica_shot8_corruption_required) from _call_corruption_required_54
            jump expression photoPoseLabel
        # да
        alex_photograph "Миссис Бакфетт, это последний такой кадр, я обещаю!"
        alex_photograph "Осталась еще пара приличных кадров и мы успешно закончим!"
        m "Точно?!"
        alex_photograph "Клянусь!"
        w
        call photoshop_flash() from _call_photoshop_flash_129
        w
        $ photoImage = 20122
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_179
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot8_progress")
        $ PS7_shoots_array.append(photoImage)
        w
        m "А это что был за кадр?!"
        m "Ты сказал что тот был последним!"
        alex_photograph "Миссис Бакфетт, это чистка затвора."
        alex_photograph "Я не делал съемку!"
        jump expression photoPoseLabel


label ep26_photoshoot_suit7_pose10:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose10"
    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose11"

    # кадр
    img 20123
    # up
#    img 20124
#    img 20125
    # side
#    img 20126
#    img 20127
    # down +
#    img 20128
#    alex_photograph "Миссис Бакфетт, я не снимаю."
#    alex_photograph "Я просто настраиваю фокус."
    # если нет
#    m "Я прекрасно знаю что ты меня обманываешь, Алекс!"
#    m "Достаточно с меня всего этого!"
    # если да
#    m "Алекс, ты не врешь?"
#    alex_photograph "Миссис Бакфетт, я клянусь!"
#    m "Ладно..."
#    img 20129
#    img 20130
#    img 20131


    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        if shotsAmount == 0:
            return
        jump ep26_photoshoot_suit7_pose11_pre
#        img 20123
#        with fadelong
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
#        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20125, 20127, 20131], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20124
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_130
        w
        $ photoImage = 20125
        img photoImage
        with Dissolve(0.2)
        m "Алекс!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_180
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20126
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_131
        w
        $ photoImage = 20127
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_181
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20128
        with Dissolve(0.2)
        alex_photograph "Миссис Бакфетт, я не снимаю."
        alex_photograph "Я просто настраиваю фокус."
        if corruption < PS7_monica_shot9_corruption_required:
            m "Я прекрасно знаю что ты меня обманываешь, Алекс!"
            m "Достаточно с меня всего этого!"
            call corruption_required(PS7_monica_shot9_corruption_required) from _call_corruption_required_55
            jump expression photoPoseLabel
        m "Алекс, ты не врешь?"
        alex_photograph "Миссис Бакфетт, я клянусь!"
        m "Ладно..."
        w
        call photoshop_flash() from _call_photoshop_flash_132
        w
        img 20129
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_133
        w
        img 20130
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_134
        w
        $ photoImage = 20131
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_182
        $ add_char_progress("AlexPhotograph", PS7_AlexProgressEachCorruptionShot, "PS7_monica_shot9_progress")
        $ PS7_shoots_array.append(photoImage)
        jump expression photoPoseLabel


label ep26_photoshoot_suit7_pose11_pre:

    # поза
    music Groove2_85
    img 20132
    with fadelong
    w
    m "Алекс, что ты так на меня смотришь?"
    m "Зачем ты попросил меня встать в эту позу?"
    img 20133
    alex_photograph "Миссис Бакфетт, я хочу попросить Вас убрать руки..."
    music Power_Bots_Loop
    img 20134
    with diss
    m "ЧТО?!"
    m "НЕТ!!!"
    m "Даже не надейся!"
    img 20135
    alex_photograph "Миссис Бакфетт, но это не моя прихоть, а распоряжение Мистера Бифа!"
    img 20136
    with diss
    m "Мне плевать!"
    music Groove2_85
    img 20137
    with fade
    alex_photograph "Но Миссис Бакфетт, Ваша грудь закрыта."
    alex_photograph "При таком свете, материал белья не такой уж прозрачный."
    alex_photograph "Он сильно бликует на камере и ничего не видно!"
    img 20138
    m "..."
    img 20139
    alex_photograph "К тому же, будет видно не больше чем на предыдущих кадрах."
    alex_photograph "Все что можно было увидеть, уже есть на пленке."
    alex_photograph "Зато подумайте, фотосессия будет завершена и Мистер Биф будет доволен."
    img 20140
    with diss
    alex_photograph "Я не думаю что он потребует еще больше от Вас, Миссис Бакфетт."
    img 20141
    with fade
    m "Ты так думаешь, Алекс?"
    img 20142
    alex_photograph "Миссис Бакфетт, я в этом уверен!"
    music Hidden_Agenda
    img 20143
    with fade
    mt "Черт возьми!"
    mt "Мне не хочется показывать свою грудь на весь мир, хоть и прикрытую какой-то тряпочкой..."
    img 20144
    mt "С другой стороны, Алекс говорит что материал сильно бликует и ничего не будет видно..."
    mt "И Биф, наконец-то, отстанет от меня."
    mt "Вряд-ли он сможет потребовать больше..."
    mt "Иначе он может перестать давать мне мне деньги..."
    mt "И я даже боюсь представить что тогда будет..."
    img 20145
    with diss
    mt "К тому же, мне нечего стыдиться. У меня самая красивая грудь в этой стране..."
    mt "А может и во всем мире!"
    img 20146
    with fade
    mt "..."
    mt "Итак, что же мне делать?"

    if char_info["AlexPhotograph"]["level"] < 2:
        menu:
            "Опустить руки. (недостаточные отношения с Алексом, required lvl. 2) (disabled)": #corruption
                pass
            "Прекратить фотосессию":
                music Groove2_85
                img 20147
                with fadelong
                m "Нет, Алекс!"
                m "Я не поддамся на твои уловки!"
                m "С меня хватит!"
                return False
    else:
        $ menu_corruption = [PS7_monica_shot10_corruption_required_high]
        menu:
            "Опустить руки.": #corruption
                pass
            "Прекратить фотосессию":
                music Groove2_85
                img 20147
                with fadelong
                m "Нет, Алекс!"
                m "Я не поддамся на твои уловки!"
                m "С меня хватит!"
                return False

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20148
    with fadelong
    m "..."
    img 20149
    alex_photograph "..."

    music stop
    img black_screen
    with diss
    pause 1.0
    music Molten_Alloy
    img 20150
    with fadelong
    w
    alex_photograph "Мотор!"

    music stop
    img 20151
    with fadelong

label ep26_photoshoot_suit7_pose11:
    $ photoPoseLabel = "ep26_photoshoot_suit7_pose11"
#    $ photoPoseNextLabel = "ep26_photoshoot_suit7_pose11"

    # кадр
    img 20151
    # up
#    img 20152
#    img 20153
#    img 20154
#    img 20155
#    img 20156
#    img 20157
    # side
#    img 20158
#    img 20159
#    img 20160
    # down
#    img 20161
#    img 20162
#    img 20163
#    img 20164
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        return
#        img 20123
#        with fadelong
#        alex_photograph "Следующая поза, Миссис Бакфетт!"
#        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS7_shoots_array)
    show screen photoshoot2([20157, 20160, 20164], PS7_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 20152
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_135
        w
        img 20153
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_136
        w
        img 20154
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_137
        w
        img 20155
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_138
        w
        img 20156
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_139
        w
        $ photoImage = 20157
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_183
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20158
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_140
        w
        img 20159
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_141
        w
        $ photoImage = 20160
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_184
        $ PS7_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 20161
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_142
        w
        img 20162
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_143
        w
        img 20163
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_144
        w
        $ photoImage = 20164
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_185
        $ PS7_shoots_array.append(photoImage)

        w
        music Groove2_85
        alex_photograph "Миссис Бакфетт."
        alex_photograph "Могли бы Вы убрать руки?"
        alex_photograph "Они мешают мне фотографировать нижнюю часть Вашего тела..."
        $ menu_corruption = [PS7_monica_shot11_corruption_required_high]
        menu:
            "Делать что просит Алекс. (опционально)": #corruption (very high)
                pass
            "Завершить фотосессию.":
                m "Нет, Алекс."
                m "Я думаю фотосессия завершена и так."
                return
        music I_Feel_You
        $ add_corruption(30, "ep26_photoshoot_suit7_optional")
        m "Да, Алекс..."
        m "Я понимаю..."
        img 20165
        with diss
        w
        m "Надо раздвинуть ноги?"
        alex_photograph "Да, Миссис Бакфетт."
        alex_photograph "Если Вам не трудно."
        m "Я понимаю, Алекс..."
        img 20166
        with diss
        m "Так тебя устроит?"
        img 20167
        with fade
        w
        alex_photograph "Да, Миссис Бакфетт. Вполне."
        call photoshop_flash() from _call_photoshop_flash_145
        w
        img 20168
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_146
        w
        img 20169
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_147
        w
        sound Jump1
        img 20170
        with fade
        alex_photograph "Миссис Бакфетт."
        alex_photograph "Можно, пожалуйста, я сниму эти трусики и сделаю пару кадров?"
        alex_photograph "Мистер Биф даст мне солидную премию за это."
        music stop
        img black_screen
        with diss
        pause 1.0
        music Master_Disorder
        img 20171
        with fadelong
        m "Нет, Алекс."
        m "Я закончу с проблемами до того как дойдет до этого..."
        img 20172
        with diss
        m "А сейчас..."
        m "Если ты не уберешь руку, то умрешь..."
        img 20173
        w
        jump expression photoPoseLabel




label ep26_photoshoot_suit7_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2

    if questHelpFlag23 == False:
        $ questHelpFlag23 = True
#        $ questHelpDesc("photoshoot_desc6", "photoshoot_desc12")

#    $ questHelp("office_22", skipIfExists=True)
    $ questHelp("photoshoot_6", True)
    $ questHelp("photoshoot_12", skipIfExists=True)
    $ shotsAmountCompleted = len(list(set(PS7_shoots_array)))
    if shotsAmountCompleted >= shotsTotalAmount:
        $ questHelp("photoshoot_12", True)
#        $ questHelpDesc("photoshoot_desc12", False)
#    $ shotsTotalAmount

    music Groove2_85
    img 20174
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 20175
    with fade
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            $ biffMonicaLastCastingSkipped = True
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot7_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call ep26_photoshoot7_casting() from _call_ep26_photoshoot7_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot7_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot7_casting_corruption_required:
            pass

    return


label ep26_photoshoot7_casting:
    music Groove2_85
    sound highheels_short_walk
    img 20195 #9470
    with fadelong
    w
    img 20196 #9471
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 20197 #9472
    $ add_char_progress("Biff", PS7_BiffProgressCasting, "PS7_BiffProgressCasting_day" + str(day))
    $ shotsAmountCompleted = len(list(set(PS7_shoots_array)))
#    $ shotsTotalAmount

    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 20198 #9473
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 20199 #9474
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Запретное Желание..."
            $ add_char_progress("Biff", PS7_BiffProgressCastingChick, "PS7_BiffProgressCastingChick_day" + str(day))
            biff "Что Запретное Желание хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 7
            call ep22_casting() from _call_ep22_casting_12
            img 20201 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 20200 #9475
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 7
            $ chickMode = False
            call ep22_casting() from _call_ep22_casting_13
            img 20201 #9476
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
