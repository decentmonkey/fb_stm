label gallery_ep22_photoshoot1:
    img 8317
    with fade
    m "Алекс, я уже снималась в этом платье..."
    img 8318
    alex_photograph "Мистер Биф сказал одеть его!"
    "Вы всем очень понравились на благотворительном вечере!"
    "Публика хочет еще Ваших фотографий в этом платье!"

    $ shotsAmount = PS1_shots_amount
    $ shotsTotalAmount = 24
#    music Molten_Alloy_low
    music stop

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    img 8319
    with fadelong
    label gallery_ep22_photoshoot1_pose1:
        # кадр
        img 8319
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8323
            with fadelong
            jump gallery_ep22_photoshoot1_pose2
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8320
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_162
####            $ PS1_shoots_array.append(photoImage) - убрать
            w
            jump gallery_ep22_photoshoot1_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8321
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_163
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8322
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_164
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose1

    label gallery_ep22_photoshoot1_pose2:
        # кадр
        img 8323
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8327
            with fadelong
            jump gallery_ep22_photoshoot1_pose3
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8324
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_165
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose2
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8325
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_166
            w
            jump gallery_ep22_photoshoot1_pose2
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8326
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_167
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose2

    label gallery_ep22_photoshoot1_pose3:
        # кадр
        img 8327
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8330
            with fadelong
            jump gallery_ep22_photoshoot1_pose4
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8535
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_168
###            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose3
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8328
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot1_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS1_monica_shot1_corruption_required) from _rcall_corruption_required_28
                jump gallery_ep22_photoshoot1_pose3
            w
            # $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot1_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_169
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8329
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_170
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose3


    label gallery_ep22_photoshoot1_pose4:
        # кадр
        img 8330
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8334
            with fadelong
            jump gallery_ep22_photoshoot1_pose5
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8331
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_171
####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8332
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_172
#####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose4
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8333
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot2_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS1_monica_shot2_corruption_required) from _rcall_corruption_required_29
                jump gallery_ep22_photoshoot1_pose4
            w
            # $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot2_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_173
#####            $ PS1_shoots_array.append(photoImage)
            w
            jump gallery_ep22_photoshoot1_pose4


    label gallery_ep22_photoshoot1_pose5:
        #кадр
        img 8334
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8338
            with fadelong
            jump gallery_ep22_photoshoot1_pose6
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8335
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_174
            w
            jump gallery_ep22_photoshoot1_pose5
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8336
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot3_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS1_monica_shot3_corruption_required) from _rcall_corruption_required_30
                jump gallery_ep22_photoshoot1_pose5
            w
            # $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot3_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_175
            w
            jump gallery_ep22_photoshoot1_pose5
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8337
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_176
            w
            jump gallery_ep22_photoshoot1_pose5


    label gallery_ep22_photoshoot1_pose6:
        #кадр
        img 8338
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8342
            with fadelong
            jump gallery_ep22_photoshoot1_pose7
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose6
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8339
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_177
            w
            jump gallery_ep22_photoshoot1_pose6
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8340
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot4_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS1_monica_shot4_corruption_required) from _rcall_corruption_required_31
                jump gallery_ep22_photoshoot1_pose6
            w
            # $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot4_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_178
            w
            jump gallery_ep22_photoshoot1_pose6
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8341
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_179
            w
            jump gallery_ep22_photoshoot1_pose6


    label gallery_ep22_photoshoot1_pose7:
        #кадр
        img 8342
        if shots == 0 or shotsAmount == 0:
            $ shots = 2
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            img 8346
            with fadelong
            jump gallery_ep22_photoshoot1_pose8
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose7
        #up+
        if result == "up":
            sound camera_lens1
            $ photoImage = 8343
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot5_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS1_monica_shot5_corruption_required) from _rcall_corruption_required_32
                jump gallery_ep22_photoshoot1_pose7
            w
            # $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot5_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_180
            w
            jump gallery_ep22_photoshoot1_pose7
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8344
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_181

            w
            jump gallery_ep22_photoshoot1_pose7
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8345
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_182

            w
            jump gallery_ep22_photoshoot1_pose7


    label gallery_ep22_photoshoot1_pose8:
        #кадр
        img 8346
        if shots == 0 or shotsAmount == 0:
            return
        show screen photoshoot_camera_icon(PS1_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot1_pose8
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8347
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_183
            w
            jump gallery_ep22_photoshoot1_pose8
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8348
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_184
            w
            jump gallery_ep22_photoshoot1_pose8
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8349
            img photoImage
            with Dissolve(0.2)
            if corruption < PS1_monica_shot6_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS1_monica_shot6_corruption_required) from _rcall_corruption_required_33
                jump gallery_ep22_photoshoot1_pose8
            w
            # $ add_char_progress("AlexPhotograph", PS1_AlexProgressEachCorruptionShot, "PS1_monica_shot6_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_185
            w
            jump gallery_ep22_photoshoot1_pose8

    return

label gallery_ep22_photoshoot1_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot

    music Stealth_Groover
    img 6632
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 6631
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
####            $ biffMonicaLastCastingSkipped = True

            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot1_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                "..."
                "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call gallery_ep22_photoshoot1_casting() from _rcall_gallery_ep22_photoshoot1_casting
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot1_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot1_casting_corruption_required:
            pass

return

label gallery_ep22_photoshoot1_casting:
    music Groove2_85
    sound highheels_short_walk
    img 8436
    with fadelong
    w
    img 8437
    with Dissolve(0.5)

#    $ shotsTotalAmount


    m "Привет, Биф. Я пришла..."
#######    # $ add_char_progress("Biff", PS1_BiffProgressCasting, "PS1_BiffProgressCasting_day" + str(day))
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 8439
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 8440
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Моника Бакфетт с благотворительного вечера..."
######            # $ add_char_progress("Biff", PS1_BiffProgressCastingChick, "PS1_BiffProgressCastingChick_day" + str(day))
            biff "Что Моника Бакфетт хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 1
            call gallery_8442() from _rcall_gallery_8442_6
            img 8446
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                img 8439
                with fade
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 8438
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
                #
            biff "И что цыпочка будет делать?"
            call gallery_8442() from _rcall_gallery_8442_7
            img 8446
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return

##########################################################
##########################################################

label gallery_ep22_photoshoot5:
    $ melanieWaitingOpenedOutfits = False
    $ shotsAmount = PS5_shots_amount
    $ shotsTotalAmount = 27

    $ shots = 3
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

#    m "Алекс, я не буду сниматься в таком ракурсе!"

#    m "Алекс, даже не думай делать такой кадр!"


#    m "Алекс, я не собираюсь вставать в эту позу!!!"
#    "Даже не мечтай!"

    music Molten_Alloy
    img 8748
    with fade
    alex_photograph "Итак, пассажиру авиакомпании нужна помощь с багажом..."

        #кадр
#        img 8748
        #up
#        img 8749
        #side
#        img 8750
        #down
#        img 8751

    label gallery_ep22_photoshoot5_pose1:
        img 8748

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8752
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Пассажир авиакомпании замечает стюардессу..."
            jump gallery_ep22_photoshoot5_pose2
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose1
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8749
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_186

            w
            jump gallery_ep22_photoshoot5_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8750
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_187
            w
            jump gallery_ep22_photoshoot5_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8751
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_188
            w
            jump gallery_ep22_photoshoot5_pose1


        #кадр
#        img 8752
        #up
#        img 8753
        #side
#        img 8754
        #down
#        img 8755
    label gallery_ep22_photoshoot5_pose2:
        img 8752

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8756
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Представитель авиакомпании спешит помочь..."
            jump gallery_ep22_photoshoot5_pose3
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose2
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8753
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_189
            w
            jump gallery_ep22_photoshoot5_pose2
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8754
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_190
            w
            jump gallery_ep22_photoshoot5_pose2
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8755
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_191
            w
            jump gallery_ep22_photoshoot5_pose2


        #кадр
#        img 8756
        #up
#        img 8757
        #side
#        img 8758
        #down
#        img 8759

    label gallery_ep22_photoshoot5_pose3:
        img 8756

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8760
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            img 8761
            with fade
            mt "Какая у Мелани бархатная кожа на ощупь..."
            music Molten_Alloy
            img 8760
            with fade
            jump gallery_ep22_photoshoot5_pose4
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose3
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8757
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_192
            w
            jump gallery_ep22_photoshoot5_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8758
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_193
            w
            jump gallery_ep22_photoshoot5_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8759
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_194
            w
            jump gallery_ep22_photoshoot5_pose3

        #кадр
#        img 8760
        #вид кадра с комментарием о попе Мелани
#        img 8761

        #up
#        img 8762
        #side
#        img 8764
        #down
#        img 8763

    label gallery_ep22_photoshoot5_pose4:
        img 8760

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8765
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Пассажир не удовлетворен качеством услуг..."
            if corruption < PS5_monica_pose4_corruption_required:
                music Groove2_85
                m "Алекс! Я не собираюсь сидеть на коленях перед Мелани!"
                "И это не обсуждается!"
                call corruption_required(PS5_monica_pose4_corruption_required) from _rcall_corruption_required_34
                return False
            m "Алекс! Я не собираюсь сидеть на коленях перед Мелани!"
            m "..."
            m "Ну, ладно..."
            mt "Черт, мне надо узнать правду про Дика!"
            # $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot1_progress")

            jump gallery_ep22_photoshoot5_pose5
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose4
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8762
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_195
            w
            jump gallery_ep22_photoshoot5_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8764
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_196
            w
            jump gallery_ep22_photoshoot5_pose4
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8763
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_197
            w
            jump gallery_ep22_photoshoot5_pose4


        #кадр
#        img 8765
        #up
#        img 8766
        #side
#        img 8767
        #down
#        img 8768

    label gallery_ep22_photoshoot5_pose5:
        img 8765

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8769
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            alex_photograph "Стюардесса просит прощения у пассажира..."
            if corruption < PS5_monica_pose5_corruption_required:
                music Groove2_85
                m "Алекс! Я не собираюсь ползать в ногах у Мелани!"
                "И это не обсуждается!"
                call corruption_required(PS5_monica_pose5_corruption_required) from _rcall_corruption_required_35
                return False
            # $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot2_progress")
            jump gallery_ep22_photoshoot5_pose6
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose5
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8766
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_198
            w
            jump gallery_ep22_photoshoot5_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8767
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_199
            w
            jump gallery_ep22_photoshoot5_pose5
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8768
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_200
            w
            jump gallery_ep22_photoshoot5_pose5

        #кадр
#        img 8769
        #up
#        img 8770
        #side
#        img 8771
        #down
#        img 8772

    label gallery_ep22_photoshoot5_pose6:
        img 8769

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Molten_Alloy
            img 8773
            with fadelong
            alex_photograph "Следующая поза, девочки!"
            jump gallery_ep22_photoshoot5_pose7
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose6
        music stop
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8770
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_201
            w
            jump gallery_ep22_photoshoot5_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8771
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_202
            w
            jump gallery_ep22_photoshoot5_pose6
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8772
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_203
            w
            jump gallery_ep22_photoshoot5_pose6


        #кадр
#        img 8773
        #up
#        img 8774
        #side
#        img 8775
#        img 8776
#        img 8778
        #down
#        img 8777

    label gallery_ep22_photoshoot5_pose7:
        img 8773

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            img 8779
            with fadelong
            alex_photograph "Миссис Бакфетт, пожалуйста, поместите голову Мелани между ног!"
            m "Какого черта, Алекс?!"
            "Может мне еще что-нибудь сделать?!"
            alex_photograph "Авиакомпания показывает насколько важен каждый пассажир!"

            if corruption < PS5_monica_pose7_corruption_required:
                call corruption_required(PS5_monica_pose7_corruption_required) from _rcall_corruption_required_36
                m "Алекс! Я не собираюсь ползать в ногах у Мелани!"
                "И это не обсуждается!"
                return False
            music Loved_Up
            # $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot2_progress")
            jump gallery_ep22_photoshoot5_pose8
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose7
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8774
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_204
            w
            jump gallery_ep22_photoshoot5_pose7
        if result == "side":
            #side
            sound camera_lens1
            img 8775
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_85
            w
            img 8776
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_86
            w
            $ photoImage = 8778
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_205
            w
            jump gallery_ep22_photoshoot5_pose7
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8777
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_206
            w
            jump gallery_ep22_photoshoot5_pose7

        #кадр
#        img 8779
        #up
#        img 8780
        #side
#        img 8781
        #down
#        img 8782
#        w

    label gallery_ep22_photoshoot5_pose8:
        img 8779

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            music Groove2_85
            jump gallery_ep22_photoshoot5_pose9_pre
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose8
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8780
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_207
            w
            jump gallery_ep22_photoshoot5_pose8
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8781
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_208
            w
            jump gallery_ep22_photoshoot5_pose8
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8782
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_209
            w
            jump gallery_ep22_photoshoot5_pose8

    label gallery_ep22_photoshoot5_pose9_pre:
        #вступление
        music Groove2_85
        hide screen photoshoot_no_next
        img 8783
        with fade
        w
        img 8784
        with Dissolve(0.5)
        music Power_Bots_Loop
        alex_photograph "Теперь сделайте вид что Вы касаетесь язычком ее киски!"
        m "ЧТО?!?! АЛЕКС, ТЫ В СВОЕМ УМЕ?!?!"
        m "Я НЕ СОБИРАЮСЬ ЛИЗАТЬ У МЕЛАНИ МЕЖДУ НОГ!!!"
        "ДА ЕЩЕ И НА КАМЕРУ!!!"
        music Groove2_85
        img 8785
        with fade
        alex_photograph "Миссис Бакфетт! Это ведь просто симуляция!"
        "Вам надо просто коснуться язычком и все!"
        img 8786
        with Dissolve(0.5)
        "Тем более это всего-лишь трусики!"
        "Вы не сделаете ничего неприличного, если дотронетесь до белья другой модели!"
        img 8787
        with Dissolve(0.5)
        m "АЛЕКС, НО!!!..."
        alex_photograph "Миссис Бакфетт, это эротическая фотосессия."
        "В ней авиакомпания хочет показать что готова на все, лишь бы ее клиенты остались довольны!"


        img 8788
        with fade
        melanie "Миссис Бакфетт?"

        mt "Похоже у меня нет выхода..."
        "Мне надо любой ценой узнать замешан-ли во всем этом Дик!"
        "И Мелани единственная надежда на это!"
        music Loved_Up2
        img 8791
        with fade



    label gallery_ep22_photoshoot5_pose9:
        img 8791

        if shots == 0 or shotsAmount == 0:
            $ shots = 3
            $ arrowUp = True
            $ arrowSide = True
            $ arrowDown = True
            hide screen photoshoot_no_next
            # $ add_char_progress("AlexPhotograph", PS5_AlexProgressEachCorruptionShot, "PS5_monica_shot3_progress")
            return True
        show screen photoshoot_camera_icon(PS5_shoots_array)
        show screen photoshoot_no_next()
        $ result = ui.interact()
        hide screen photoshoot_no_next
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot5_pose9
        #up
        if result == "up":
            sound camera_lens1
            img 8800
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_87
            w
            img 8792
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_88
            w
            $ photoImage = 8793
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_210
            w
            jump gallery_ep22_photoshoot5_pose9
        if result == "side":
            #side
            sound camera_lens1
            img 8801
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_89
            w
            img 8790
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_90
            w
            img 8794
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_91
            w
            $ photoImage = 8795
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_211
            w
            jump gallery_ep22_photoshoot5_pose9
        if result == "down":
            #down
            sound camera_lens1
            img 8799
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_92
            w
            img 8796
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_93
            w
            img 8797
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_94
            w
            $ photoImage = 8798
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_212
            w
            jump gallery_ep22_photoshoot5_pose9

    return

label gallery_ep22_photoshoot5_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot_no_next
    hide screen photoshoot

    music Stealth_Groover
    img 8745
    with fadelong
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption >= photoshoot5_casting_corruption_required: #если есть кастинги
            mt "Биф ждет меня на свой дурацкий кастинг..."
            "Он говорил даст мне работу если я буду хорошей цыпочкой..."
            "Это позволит мне приблизиться к цели, возвратить мою компанию назад!"
            "Так может быть притвориться?"
            "Ведь у меня нет к нему чувств, я хладнокровная женщина, идущая к своей мести..."
            #если обещала
            "..."
            "Черт... Тем более я ему обещала быть хорошей цыпочкой и, в противном случае, он может перестать давать работу мне..."
            call gallery_ep23_photoshoot5_casting() from _rcall_gallery_ep23_photoshoot5_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot5_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot5_casting_corruption_required:
            pass

    return

label gallery_ep23_photoshoot5_casting:
    music Groove2_85
    sound highheels_short_walk
    img 9493
    with fadelong
    w
    img 9494
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."

    img 9495

#    $ shotsTotalAmount
    biff "О! Цыпочка пришла к папочке!"
    menu:
        "Притвориться цыпочкой...":
            mt "Мне надо притвориться и завоевать его расположение..."
            img 9496
            with fade
            m "Да, цыпочка пришла к папочке..."
            "Цыпочка хорошая..."
            img 9497
            biff "Кто сегодня цыпочка?"
            m "Сегодня цыпочка - это Стюардесса из Fashion Airlines..."
            biff "Что Стюардесса хочет показать папочке?"
            call gallery_8442() from _rcall_gallery_8442_8
            img 9499
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа

        "Я не собираюсь никем притворяться!":
            #если обещала хорошо себя вести
            if monicaSaidBiffSheIsWillBeAGoodChick == True:
                m "Я пришла, потому что обещала хорошо вести себя..."
            else:
                #иначе
                img 9498
                with fade
                m "Ты заставил меня придти..."
            mt "Ненавижу!!!"
            biff "И что цыпочка будет делать?"
            $ castingCloth = 5
            $ chickMode = False
            call gallery_8442() from _rcall_gallery_8442_9
            img 9499
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return

##########################################################
##########################################################

label gallery_ep27_photoshoot_suit8:
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
            return

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

label gallery_ep27_photoshoot_suit8_pose1:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose1"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose2"
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
            call corruption_required(PS8_monica_pose2_corruption_required) from _rcall_corruption_required_37
            return
        m "Алекс, снимай издалека!"
        alex_photograph "Конечно, Миссис Бакфетт!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20533
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_213
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20534
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_214
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
            call corruption_required(PS8_monica_shot1_corruption_required) from _rcall_corruption_required_38
            jump expression photoPoseLabel
        # если можно
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_215
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot1_progress")
        w
        jump expression photoPoseLabel


label gallery_ep27_photoshoot_suit8_pose2:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose2"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose3"
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
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20537
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_216
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20538
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_217
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
            call corruption_required(PS8_monica_shot2_corruption_required) from _rcall_corruption_required_39
            jump expression photoPoseLabel
        # если можно
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_218
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot2_progress")
        w
        jump expression photoPoseLabel


label gallery_ep27_photoshoot_suit8_pose3:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose3"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose4"
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
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20541
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_219
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
            call corruption_required(PS8_monica_shot3_corruption_required) from _rcall_corruption_required_40
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_220
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot3_progress")
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20542
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_221
        w
        jump expression photoPoseLabel


label gallery_ep27_photoshoot_suit8_pose4:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose4"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose5"
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
            call corruption_required(PS8_monica_pose4_corruption_required) from _rcall_corruption_required_41
            return
        alex_photograph "Миссис Бакфетт, это всего-лишь образ!"
        alex_photograph "Не волуйтесь, ничего не видно!"
        m "Точно!?"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20545
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_222
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
            call corruption_required(PS8_monica_shot4_corruption_required) from _rcall_corruption_required_42
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я не буду приближать камеру."
        alex_photograph "Я фотографирую издалека!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_223
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot4_progress")
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
            call corruption_required(PS8_monica_shot5_corruption_required) from _rcall_corruption_required_43
            jump expression photoPoseLabel
        alex_photograph "Не переживайте, Миссис Бакфетт!"
        alex_photograph "Из этого ракурса ничего не видно."
        m "Точно?"
        alex_photograph "Да, Миссис Бакфетт! Уверяю Вас!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_224
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot5_progress")
        w
        jump expression photoPoseLabel



label gallery_ep27_photoshoot_suit8_pose5:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose5"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose6"
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
            call corruption_required(PS8_monica_pose5_corruption_required) from _rcall_corruption_required_44
            return
        alex_photograph "Миссис Бакфетт, не переживайте!"
        alex_photograph "Все-равно ничего не видно! Украшение дает блеск и засвечивает кадр!"
        m "Алекс, это точно?!"
        alex_photograph "Миссис Бакфетт, это абсолютно точно!"
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS8_shoots_array)
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20549
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_225
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
            call corruption_required(PS8_monica_shot6_corruption_required) from _rcall_corruption_required_45
            jump expression photoPoseLabel
        alex_photograph "Не волнуйтесь, Миссис Бакфетт!"
        alex_photograph "Украшение все скрывает!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_226
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot6_progress")
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
            call corruption_required(PS8_monica_shot7_corruption_required) from _rcall_corruption_required_46
            jump expression photoPoseLabel
        alex_photograph "Миссис Бакфетт, я фотографирую украшение."
        alex_photograph "Больше ничего не попадает в кадр!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_227
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot7_progress")
        w
        jump expression photoPoseLabel


label gallery_ep27_photoshoot_suit8_pose6:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose6"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose7"
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
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20553
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_228
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 20554
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_95
        w
        sound camera_lens1
        $ photoImage = 20555
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_229
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20556
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_230
        w
        jump expression photoPoseLabel


label gallery_ep27_photoshoot_suit8_pose7:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose7"
    $ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose8"
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
            call corruption_required(PS8_monica_pose8_corruption_required) from _rcall_corruption_required_47
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
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20559
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_231
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 20558
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_232
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 20560
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_233
        w
        jump expression photoPoseLabel


label gallery_ep27_photoshoot_suit8_pose8:
    $ photoPoseLabel = "gallery_ep27_photoshoot_suit8_pose8"
    #$ photoPoseNextLabel = "gallery_ep27_photoshoot_suit8_pose8"
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
    show screen photoshoot()
    $ result = ui.interact()
    hide screen photoshoot
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 20562
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_234
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
            call corruption_required(PS8_monica_shot8_corruption_required) from _rcall_corruption_required_48
            jump expression photoPoseLabel
        #
        alex_photograph "Миссис Бакфетт, я буду фотографировать только верхнюю часть."
        m "Ну.. Ладно..."
        m "Только не смотри ниже!"
        alex_photograph "Да, Миссис Бакфетт, конечно!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_96
        w
        sound camera_lens1
        img 20564
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_97
        w
        sound camera_lens1
        img 20565
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_98
        w
        sound camera_lens1
        img 20566
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_99
        w
        sound camera_lens1
        img 20567
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_100
        w
        sound camera_lens1
        img 20568
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_101
        w
        m "Алекс!"
        sound camera_lens1
        $ photoImage = 20569
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_235
        w
        # $ add_char_progress("AlexPhotograph", PS8_AlexProgressEachCorruptionShot, "PS8_monica_shot8_progress")
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
        call photoshop_flash() from _rcall_photoshop_flash_102
        w
        sound camera_lens1
        img 20578
        with Dissolve(0.2)
        w
        alex_photograph "И Вашу попку!"
        call photoshop_flash() from _rcall_photoshop_flash_103
        w
        sound camera_lens1
        img 20579
        with Dissolve(0.2)
        w
        alex_photograph "Моя мечта сбылась!"
        call photoshop_flash() from _rcall_photoshop_flash_104
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
        call photoshop_flash() from _rcall_photoshop_flash_105
        w
        alex_photograph "Новая модель трусиков от Модного Журнала! Она так идем Вам, Миссис Бакфетт!"
        sound camera_lens1
        img 20585
        with Dissolve(0.2)
        w
        alex_photograph "Миссис Бакфетт... Ахххх..."
        call photoshop_flash() from _rcall_photoshop_flash_106
        w
        sound camera_lens1
        $ photoImage = 20586
        img photoImage
        with Dissolve(0.2)
        w
        alex_photograph "О, Миссис Бакфетт!"
        alex_photograph "Ахххх..."
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_236
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
        hide screen photoshoot
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
        return


label gallery_ep27_photoshoot_suit8_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot
    music Groove2_85

    # думает
    img 20594
    with fadelong
    mt "Я закончила эту непристойную фотосессию."
    mt "Что дальше?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (corruption)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True): #если есть кастинги
            mt "Я не собираюсь идти по офису голой! Я еще не докатилась до такого!"
            mt "И этого не произойдет никогда!!!"
            return
    return

##########################################################
##########################################################

label gallery_monica_office_photostudio_alex_dialogue2:
    if act == "l":
        return
    #render
    #Моника разговаривает с Алексом в фотостудии (фотосессия)
    $ store_music()
    music Stealth_Groover
    img 6516
    with fade
    alex_photograph "Миссис Бакфетт!"
    "Мистер Биф сказал что мне надо провести фотосессию с Вами!"
    "Вы будете участвовать?"
    menu:
        "Да, буду...":
            pass
        "Пока нет...":
            m "Пока нет..."
            $ restore_music()
            return

    img 6517
    with fade
    m "Да, буду..."
    "Что мне одеть?"
    "Я ведь не буду сниматься в этом?!"

    img 6518
    alex_photograph "Это была бы замечательная идея!"
    "К сожалению, Мистер Биф сказал одеть то платье, в котором Вы снимались в прошлый раз!"
    "Но я бы попросил Вас сначала сделать несколько кадров в этом наряде!"
    "Он Вам очень идет, у Вас потрясающий вкус!"

    img 6519
    m "Ты издеваешься?!"

    img 6520
    alex_photograph "Но Вы бы иначе не надели его, так ведь?"

    music Hidden_Agenda
    img 6521
    m "Ну... Вообще-то да..."
    "Это мой маленький эксперимент."
    "Но я бы пока не хотела широко освещать его."
    music Stealth_Groover
    img 6522
    "Поэтому Алекс... Не надо делать никаких лишних кадров, хорошо?"

    img 6523
    alex_photograph "Как скажете, Миссис Бакфетт!"

    img 6524
    "Вы можете переодеться, все готово!"

    img 6525
    m "Где то платье, которое мне надо надеть?"
    img 6526
    alex_photograph "Оно здесь! Вы можете переодеться в него!"
    img 6525
    m "Я переоденусь в гримерной комнате..."

    img 6526
    alex_photograph "Миссис Бакфетт! Мелани ушла и закрыла ее!"
    alex_photograph "Переодевайтесь здесь! Я не буду смотреть, обещаю!"

    img 6527
    mt "!!!"

    menu:
        "Переодеться.":
            pass
        "Уйти.":
            $ restore_music()
            return

    #переодевание
    img 6528
    with fade
    m "Алекс, отвернись!"
    "Если попробуешь подсмотреть, я прибью тебя!!!"
    img 6529
    alex_photograph "Обещаю, Мэм!"
    #музыка переодевания
    music Loved_up
    img 6530
    with fadelong
    w
    sound snd_fabric1
    img 6531
    with fadelong
    w
    img 6532
    w
    img 6533
    w
    img 6534
    with fade
    w
    img 6535
    w
    img 6536
    w
    img 6537
    with fade
    w
    img 6538
    w
    img 6539
    w
    img 6540
    w
    img 6541
    w
    img 6542
    w
    img 6543
    w
    img 6544
    w
    img 6545
    w
    img 6546
    w
    img 6547
    w
    img 6548
    w
    img 6549
    with fade
    w
    img 6551
    w
    sound wow
    img 6550
    w
    img 6552
    w
    img 6553
    w
    img 6554
    w
    img 6555
    w
    img 6556
    w
    img 6557
    w
    img 6558
    w
    sound Jump2
    img 6559
    w
    img 6560
    w
    img 6558
    w
    sound wow
    img 6561
    w
    music Loved_up2
    sound Jump1
    img 6562
    with fade
    w
    img 6563
    with fade
    mt "Черт!"
    "Гребаные колготки!"
    img 6564
    w
    img 6565
    with fade
    w
    sound Jump2
    img 6566
    w
    img 6567
    w
    img 6568
    alex_photograph "Ну же, фокусируйся, скорее!"
    w
    img 6569
    w
    music Stealth_Groover
    sound Jump1
    img 6570
    with fade
    m "Алекс!"
    img 6571
    alex_photograph "Да, Мэм?"
    "Вы все? Я могу поворачиваться?"
    m "Нет!"
    "Я еще переодеваюсь!"
    "И не вздумай даже пошевелиться, если тебе дорога жизнь!"
    alex_photograph "Конечно, Мэм!"

    "Я все время стою неподвижно!"
    "И жду Вашего разрешения, Мэм!"

    music Loved_up2
    sound snd_fabric1
    img 6572
    with fadelong
    w
    img 6573
    w
    img 6574
    with Dissolve(0.8)
    w
    img 6575
    w
    img 6576
    with fade
    mt "Черт! У меня нет трусиков под это платье!"
    "Надо было взять хоты бы трусики Юлии!"
    "Но под те жуткие джинсовые шорты, что я ношу, их все-равно не оденешь..."
    sound Jump2

    img 6577
    w
    img 6578
    with Dissolve(0.5)
    w
    #звук затвора
    sound snd_photo_capture
    img 6580
    w
    #звук затвора
    sound snd_photo_capture
    img 6579
    with Dissolve(0.5)
    w
    img 6581
    with Dissolve(0.5)
    w
    img 6582
    alex_photograph "..."
    w
    img 6583
    with fade
    mt "Ладно... Этого все-равно никто не заметит..."

    music Stealth_Groover
    img 6584
    with fadelong
    alex_photograph "Вы выглядите потрясающе, Миссис Бакфетт!"
    m "Спасибо, Алекс..."

    img 6585
    m "Но я уже снималась в этом платье..."
    "Думаешь будет уместно делать две одинаковые фотосессии в одном и том же?"

    img 6586
    with fade
    alex_photograph "Это РАЗНЫЕ фотосессии, Миссис Бакфетт!"

    music Molten_Alloy
    img 6587
    with fade
    alex_photograph "Начинайте, позировать!"
    "Мотор!"
    img black_screen
    with Dissolve(1.0)
    #фотосессия Моники обычная
    # $ add_char_progress("AlexPhotograph", photoshot1AlexProgressAmount, "photoshot1")

    img 6588
    call photoshop_flash() from _rcall_photoshop_flash_107
    w
    img 6589
    call photoshop_flash() from _rcall_photoshop_flash_108
    w
    img 6590
    call photoshop_flash() from _rcall_photoshop_flash_109
    w
    img 6591
    call photoshop_flash() from _rcall_photoshop_flash_110
    w
    img 6592
    call photoshop_flash() from _rcall_photoshop_flash_111
    w
    img 6593
    call photoshop_flash() from _rcall_photoshop_flash_112
    w
    img 6594
    call photoshop_flash() from _rcall_photoshop_flash_113
    w
    img 6596
    call photoshop_flash() from _rcall_photoshop_flash_114
    w
    img 6595
    call photoshop_flash() from _rcall_photoshop_flash_115
    w
    img 6597
    call photoshop_flash() from _rcall_photoshop_flash_116
    w

    music Groove2_85
    img 6598
    with fade
    alex_photograph "Миссис Бакфетт! Сядьте, пожалуйста, на этот стул!"
    img 6599
    m "Зачем?"
    alex_photograph "Я фотограф! Я вижу композицию со стороны!"
    m "Ладно..."

    music Molten_Alloy
    img black_screen
    with Dissolve(1.0)
    #фотосессия Моники со стулом
    img 6600
    with fade
    call photoshop_flash() from _rcall_photoshop_flash_117
    w
    img 6601
    call photoshop_flash() from _rcall_photoshop_flash_118
    w
    img 6602
    call photoshop_flash() from _rcall_photoshop_flash_119
    w

    music Groove2_85
    img 6603
    with fade
    alex_photograph "Миссис Бакфетт! Сядьте, пожалуйста, вот так..."
    #сажает Монику в развратную позу
    m "Алекс! Я не собираюсь сниматься в такой позе!"
    "Ты сошел с ума?!?"

    alex_photograph "Миссис Бакфетт! Это необходимо!"

    img 6604
    m "Алекс! Ты, кажется, давал слово что больше не будешь брать подобные ракурсы!"
    img 6605
    alex_photograph "Да, Миссис Бакфетт! Я давал слово что буду делать как скажет Босс!"

    img 6606
    m "А кто твой Босс?!"

    img 6605
    alex_photograph "Мистер Биф! И он сказал мне брать все возможные ракурсы!"

    img 6607
    mt "Вот сволочь!"
    img 6608
    with fade
    m "Я не буду так сниматься!"
    m "Мы закончили фотосессию! Хватит и того что снято!"

    img 6609
    alex_photograph "Миссис Бакфетт!"
    "Тогда я вынужден сообщить Мистеру Бифу о срыве фотосессии..."

    m "Мы сделали достаточно кадров!"

    if alexPhotographOffended1 == True:
        #если Моника зла к Алексу
        img 6610
        alex_photograph "Мы не сделали самого главного, Миссис Бакфетт."
        "Но я имею права настаивать..."
        "Я сообщу Мистеру Бифу..."
        img 6611
        mt "ЧЕРТ! НЕ ХВАТАЛО ЕЩЕ СРЫВА ФОТОСЕССИИ!!!"
        "Это значит что Биф не даст мне деньги..."
        "И я не поеду на благотворительный вечер..."
        "А я так хочу туда!"

    else:
        #если Моника добра к Алексу
        img 6612
        alex_photograph "Миссис Бакфетт!"
        "Я знаю что Вы цените меня как профессионала."
        "И я понимаю что Вы не хотите делать эти кадры..."
        "Но это приказ Мистера Бифа."
        "Если я ослушаюсь, то меня уволят!..."

    img 6613
    with fade
    m "Хорошо, Алекс."
    "Давай сделаем пару кадров, но постарайся брать ракурсы поприличнее, хорошо?"
    mt "По крайней мере мне надо потерпеть это всего один раз!"
    "Давай, Моника! Ты справишься! Ты выдержишь!"

    img 6614
    with fade
    "Хорошо, Мэм!"
    "Как скажете!"

    label gallery_monica_office_photostudio_alex_dialogue2aa:
    music Molten_Alloy
    img black_screen
    with Dissolve(1.0)
    img 6615
    with fade
    w

    #Идет фотосессия с пошлыми ракурсами
    img 6616
    call photoshop_flash() from _rcall_photoshop_flash_120
    w
    img 6617
    call photoshop_flash() from _rcall_photoshop_flash_121
    w
    img 6618
    call photoshop_flash() from _rcall_photoshop_flash_122
    w
    img 6619
    call photoshop_flash() from _rcall_photoshop_flash_123
    w
    img 6620
    call photoshop_flash() from _rcall_photoshop_flash_124
    w
    label gallery_local1:
        menu:
            "Продолжить делать кадры. (corruption)" if corruption >= monicaBiffWorkPhotoShot1PervertCorruptionRequired:
                # $ add_char_progress("AlexPhotograph", photoshot1AlexProgressPervertAmount, "photoshot1_corruption")
                img 6621
                with fade
                call photoshop_flash() from _rcall_photoshop_flash_125
                w
                img 6622
                call photoshop_flash() from _rcall_photoshop_flash_126
                w
                img 6623
                call photoshop_flash() from _rcall_photoshop_flash_127
                w
                img 6624
                call photoshop_flash() from _rcall_photoshop_flash_128
                w
                img 6625
                call photoshop_flash() from _rcall_photoshop_flash_129
                w
                img 6626
                call photoshop_flash() from _rcall_photoshop_flash_130
                w
                img 6627
                call photoshop_flash() from _rcall_photoshop_flash_131
                w
                img 6628
                with Dissolve(0.5)
                w
                img 6629
                with Dissolve(0.5)
                m "Эй! Не вздумай заглядывать туда!!!"
                mt "Черт!!!"
                #конец фотосессии
                music Stealth_Groover
                img 6630
                with fade
                alex_photograph "Мы закончили, Мэм!"
                "Хотите переодеться назад?"

            "Продолжить делать кадры. (low corruption, required [monicaBiffWorkPhotoShot1PervertCorruptionRequired]) (disabled)" if corruption < monicaBiffWorkPhotoShot1PervertCorruptionRequired:
                jump gallery_local1
            "Прекратить это.":
                music Stealth_Groover
                img 6630
                with fade
                m "Я не буду так сниматься!"
                m "Мы сделали достаточно кадров!"
                alex_photograph "Хотите переодеться назад?"


    img 6631
    with fade
    mt "Вот еще! Теперь это мое платье!!!"
    "Я не собираюсь переодеваться в те тряпки!"
    "Ни за что!"

    img 6632
    m "Нет, Алекс."
    "Мне понравилось это платье, я оставлю его."

    alex_photograph "Но Мэм..."
    "Платье, украшения..."
    "Это реквизит фотостудии и..."

    img 6633
    m "Алекс, достаточно."

    alex_photograph "Мэм..."

    img 6634
    mt "Итак, {c}надо вернуться к Бифу{/c}..."
    $ store_music()

    return True

label gallery_monica_office_secretary_dialogue7:
    if act == "l":
        return
    #Моника обращается к секретарше одетая в платье
    $ store_music()
    music RnB4_100
    img 6345
    with fade
    secretary "МИССИС БАКФЕТТ!!!"
    "Вы бесподобны в этом платье!"
    img 6346
    "Вы займете свой кабинет с завтрашнего дня?"
    img 6347
    m "Хм... Дорогая..."
    "Может быть не с завтрашнего, но скоро..."
    "Обещаю тебе!"
    img 6348
    secretary "Спасибо, Миссис Бакфетт!"
    "Я жду! Эти люди... они..."
    "Они угрожают мне и..."
    img 6349
    m "Я знаю, дорогая, подожди немного..."
    img 6348
    secretary "Да, Миссис Бакфетт!"
    "Я жду ВАС!"
    $ restore_music()
    return

label gallery_monica_office_cabinet_biff_dialogue5:
    #render
    #Моника разговаривает с Бифом после фотосессии.
    music Stealth_Groover
    img 6635
    with fade
    m "Биф!"
    "Я закончила фотосессию!"
    "И я жду свои деньги..."
    img 6636
    biff "О! Цыпочка!"
    "Сообщи моей секретарше свои реквизиты и деньги будут переведены в течении..."
    "Ну... Может быть месяца..."

    music Power_Bots_Loop
    img 6637
    m "ЧТО???"
    "МНЕ НУЖНЫ ДЕНЬГИ СЕЙЧАС, ПРЯМО СЕЙЧАС!"

    img 6638
    biff "Банки уже не работают, детка!"

    img 6639
    m "Биф!"
    "Мне нужны деньги! Сейчас же!"
    "Иначе можешь забыть про речь, которую я должна сказать на благотворительном вечере!"
    "Я просто уйду!"

    img 6641
    biff "Детка, я сказал, что банки уже не работают!"

    img 6640
    m "Мне нужны наличные, Биф!"
    "И прямо сейчас!"

    music Groove2_85
    img 6642
    biff "Ха-ха-ха!"
    "Какой темперамент!"

    img 6643
    biff "Хорошо!"
    "Если ты уйдешь сейчас, то я не успею посмотреть на твою голую попку!"
    "Я заплачу тебе наличными, но только после речи на благотворительном вечере!"

    img 6644
    m "Я не верю тебе! Какие гарантии, Биф?!"

    img 6645
    biff "Гарантии???"
    "Ты знаешь, что расчет наличными сам по себе является незаконным!"
    "Ты хочешь чтобы я заплатил тебе деньги без оформления бумаг и еще хочешь каких-то гарантий?!"

    img 6646
    "Мои гарантии - это твой ротик!"
    "Он должен говорить то что скажу Я и только тогда ты получишь свои деньги!"

    img 6647
    with fade
    m "Биф, если я скажу речь, я получу деньги?"
    img 6648
    biff "Конечно, цыпочка!"
    "Я понимаю, ты стесняешься."
    "Но не переживай, это небольшой вип зал, там будет мало людей."
    "В основном пресса."

    img 6649
    "Я же не рассчитывал что найду такую цыпочку!"
    "В следующий раз я позабочусь чтобы мою новую куклу увидели все!"

    music Power_Bots_Loop
    img 6650
    mt "!!!"

    music Groove2_85
    img 6651
    with fade
    biff "Поехали, детка!"
    "Уже пора!"
    "И не забудь вернуть платье назад после вечера!"
    "А также украшения!"
    img 6652
    "Без них ты не похожа на Монику Бакфетт и только поэтому я разрешил тебе одеть их!"

    music Power_Bots_Loop
    img 6653
    with fade
    m "Я оставлю это платье себе! Оно мое!"

    biff "Нет! Даже не обсуждается!"
    "Я не позволю чтобы шлюха за $ 10 ходила сниматься в платье от Модного Журнала!"
    "А вдруг кто-нибудь узнает это платье?!"
    "Что тогда?!"

    img 6654
    with fade
    m "Я поставлю пятно на него!"

    img 6655
    biff "Только попробуй!"
    "И тогда твой гонорар пойдет на погашение стоимости платья!"

#    music Power_Bots_Loop
    img 6656
    mt "!!!"

    music Groove2_85
    img 6657
    biff "Закрой свой ротик, пока я не заткнул его своим членом!"
    "Ты будешь открывать его когда скажу Я!"
    img 6658
    with fade
    "А сейчас поехали!"
    "Нам еще надо подобрать {c}Мелани{/c} по пути!"
    mt "!!!"
    return
    #

##########################################
##########################################

label gallery_ep22_photoshoot2:
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

    label gallery_ep22_photoshoot2_pose1:
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
            jump gallery_ep22_photoshoot2_pose2
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8354
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_237
            w
            jump gallery_ep22_photoshoot2_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8355
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_238
            w
            jump gallery_ep22_photoshoot2_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8356
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_239
            w
            jump gallery_ep22_photoshoot2_pose1


    label gallery_ep22_photoshoot2_pose2:
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
            jump gallery_ep22_photoshoot2_pose3
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8358
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_240
            w
            jump gallery_ep22_photoshoot2_pose2
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8359
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot1_corruption_required:
                m "Эй! Хватит брать свои правильные ракурсы!"
                call corruption_required(PS2_monica_shot1_corruption_required) from _rcall_corruption_required_49
                jump gallery_ep22_photoshoot2_pose2
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot1_progress")
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_241
            w
            jump gallery_ep22_photoshoot2_pose2
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8360
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_242
            w
            jump gallery_ep22_photoshoot2_pose2


    label gallery_ep22_photoshoot2_pose3:
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
            jump gallery_ep22_photoshoot2_pose4
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8362
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_243
            w
            jump gallery_ep22_photoshoot2_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8363
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_244
            w
            jump gallery_ep22_photoshoot2_pose3
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8364
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot2_corruption_required:
                m "Эй! Хватит брать свои правильные ракурсы!"
                call corruption_required(PS2_monica_shot2_corruption_required) from _rcall_corruption_required_50
                jump gallery_ep22_photoshoot2_pose3
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot2_progress")
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_245
            w
            jump gallery_ep22_photoshoot2_pose3


    label gallery_ep22_photoshoot2_pose4:
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
                call corruption_required(PS2_monica_pose5_corruption_required) from _rcall_corruption_required_51
                m "Эй! Алекс!"
                "Я не собираюсь делать снимки в такой позе!"
                return
            jump gallery_ep22_photoshoot2_pose5
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8366
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_246
            w
            jump gallery_ep22_photoshoot2_pose4
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8367
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_247
            w
            jump gallery_ep22_photoshoot2_pose4
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
                call corruption_required(PS2_monica_shot3_corruption_required) from _rcall_corruption_required_52
                jump gallery_ep22_photoshoot2_pose4
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            alex_photograph "Хорошо, Мэм!"
            w
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot3_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_248
            w
            jump gallery_ep22_photoshoot2_pose4



    label gallery_ep22_photoshoot2_pose5:
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
            jump gallery_ep22_photoshoot2_pose6
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8371
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_249
            w
            jump gallery_ep22_photoshoot2_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8370
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_250
            w
            jump gallery_ep22_photoshoot2_pose5
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8372
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot4_corruption_required:
                m "Алекс! Даже не думай об этом!"
                call corruption_required(PS2_monica_shot4_corruption_required) from _rcall_corruption_required_53
                jump gallery_ep22_photoshoot2_pose5
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            w
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot4_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_251
            w
            jump gallery_ep22_photoshoot2_pose5


    label gallery_ep22_photoshoot2_pose6:
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
                call corruption_required(PS2_monica_pose7_corruption_required) from _rcall_corruption_required_54
                mt "О Боже! Зачем я связалась с этими фотосессиями!!!"
                "Если бы только у меня был выбор!"
                return
            m "Хорошо, только быстро!"
            "И не бери камеру слишком низко!"
            alex_photograph "Конечно, Мэм!"
            music stop
            jump gallery_ep22_photoshoot2_pose7
        show screen photoshoot_camera_icon(PS2_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose6
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8374
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_252
            w
            jump gallery_ep22_photoshoot2_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8375
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_253
            w
            jump gallery_ep22_photoshoot2_pose6
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8376
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot5_corruption_required:
                m "Алекс! Даже не думай об этом!"
                call corruption_required(PS2_monica_shot5_corruption_required) from _rcall_corruption_required_55
                jump gallery_ep22_photoshoot2_pose5
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            w
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot5_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_254
            w
            jump gallery_ep22_photoshoot2_pose6


    label gallery_ep22_photoshoot2_pose7:
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
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot2_pose7
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8378
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_255
            w
            jump gallery_ep22_photoshoot2_pose7
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8379
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot6_corruption_required:
                m "Даже не думай брать этот ракурс!"
                call corruption_required(PS2_monica_shot6_corruption_required) from _rcall_corruption_required_56
                jump gallery_ep22_photoshoot2_pose7
            m "Алекс, не вздумай подвинуть камеру ни на градус!"
            w
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot6_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_256
            w
            jump gallery_ep22_photoshoot2_pose7
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8380
            img photoImage
            with Dissolve(0.2)
            if corruption < PS2_monica_shot7_corruption_required:
                m "Алекс, даже не вздумай снимать с этой стороны!"
                call corruption_required(PS2_monica_shot7_corruption_required) from _rcall_corruption_required_57
                jump gallery_ep22_photoshoot2_pose7
            alex_photograph "Мэм! Могли бы вы убрать руки?"
            m "НЕТ!!!"
            "Алекс! Платье сразу поднимется!!!"
            "У меня под ним ничего нет!!!"
            w
            call photoshop_flash() from _rcall_photoshop_flash_132
            w
            #далее
            img 8381
            with Dissolve(0.2)
            if corruption < PS2_monica_shot8_corruption_required:
                m "ТЫ ЧТО НЕ ПОНЯЛ МЕНЯ!!!"
                "ХВАТИТ!!!"
                call corruption_required(PS2_monica_shot8_corruption_required) from _rcall_corruption_required_58
                jump gallery_ep22_photoshoot2_pose7
            #иначе фото
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_257
            w
            m "Алекс! Зачем ты сделал фото?!"
            "Удали его немедленно!"
            alex_photograph "Мэм! Не переживайте!"
            "Оно получилось в затемнении и там ничего не видно!"
            # $ add_char_progress("AlexPhotograph", PS2_AlexProgressEachCorruptionShot, "PS2_monica_shot7_progress")
            jump gallery_ep22_photoshoot2_pose7

    return


label gallery_ep22_photoshoot2_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot

    music Stealth_Groover
    $ monicaOutfitsEnabled[2] = True # Открываем следующий костюм

    img 8382
    with fadelong
    alex_photograph "Мэм! Мы закончили фотосессию!"
    m "Наконец-то!!!"
    img 8383
    mt "Что теперь?"
    #Если кастинг у Бифа
    menu:
        "Переодеться назад...":
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
            call gallery_ep22_photoshoot2_casting() from _rcall_gallery_ep22_photoshoot2_casting
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot2_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot2_casting_corruption_required:
            pass

return

label gallery_ep22_photoshoot2_casting:
    music Groove2_85
    sound highheels_short_walk
    img 8447
    with fadelong
    w
    img 8448
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."
    img 8449
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
            biff "Что Леди Нуар хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 2
            call gallery_8442() from _rcall_gallery_8442_10
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
            call gallery_8442() from _rcall_gallery_8442_11
            img 8462
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return

##########################################
##########################################

label gallery_ep22_photoshoot3:
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
    label gallery_ep22_photoshoot3_pose1:
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
            jump gallery_ep22_photoshoot3_pose2
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose1
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8390
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_258
            w
            jump gallery_ep22_photoshoot3_pose1
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8391
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_259
            w
            jump gallery_ep22_photoshoot3_pose1
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8392
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_260
            w
            jump gallery_ep22_photoshoot3_pose1



    label gallery_ep22_photoshoot3_pose2:
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
            jump gallery_ep22_photoshoot3_pose3
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose2
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8394
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_261
            w
            jump gallery_ep22_photoshoot3_pose2
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8395
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot1_corruption_required:
                m "Алекс! Не начинай!"
                call corruption_required(PS3_monica_shot1_corruption_required) from _rcall_corruption_required_59
                jump gallery_ep22_photoshoot3_pose2
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot1_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_262
            w
            jump gallery_ep22_photoshoot3_pose2
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8396
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot2_corruption_required:
                m "Алекс! Хватит!"
                call corruption_required(PS3_monica_shot2_corruption_required) from _rcall_corruption_required_60
                jump gallery_ep22_photoshoot3_pose2
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot2_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_263
            w
            jump gallery_ep22_photoshoot3_pose2




    label gallery_ep22_photoshoot3_pose3:
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
                call corruption_required(PS3_monica_pose3_corruption_required) from _rcall_corruption_required_61
                m "Алекс! Я не буду вставать в такую развратную позу!"
                "И это не обсуждается!"
                return
            jump gallery_ep22_photoshoot3_pose4
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose3
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8398
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_264
            w
            jump gallery_ep22_photoshoot3_pose3
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8399
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_265
            w
            jump gallery_ep22_photoshoot3_pose3
        if result == "down":
            #down
            sound camera_lens1
            $ photoImage = 8400
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_266
            w
            jump gallery_ep22_photoshoot3_pose3



    label gallery_ep22_photoshoot3_pose4:
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
            jump gallery_ep22_photoshoot3_pose5
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose4
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8402
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_267
            w
            jump gallery_ep22_photoshoot3_pose4
        if result == "side":
            #side+
            sound camera_lens1
            $ photoImage = 8403
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot3_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS3_monica_shot3_corruption_required) from _rcall_corruption_required_62
                jump gallery_ep22_photoshoot3_pose4
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot3_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_268
            w
            jump gallery_ep22_photoshoot3_pose4
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8404
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot4_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS3_monica_shot4_corruption_required) from _rcall_corruption_required_63
                jump gallery_ep22_photoshoot3_pose4
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot4_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_269
            w
            jump gallery_ep22_photoshoot3_pose4


    label gallery_ep22_photoshoot3_pose5:
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
            jump gallery_ep22_photoshoot3_pose6
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose5
        #up
        if result == "up":
            sound camera_lens1
            $ photoImage = 8406
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_270
            w
            jump gallery_ep22_photoshoot3_pose5
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8407
            img photoImage
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_133
            w
            img 8408
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_271
            w
            jump gallery_ep22_photoshoot3_pose5
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8409
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot5_corruption_required:
                m "Алекс! Я не буду делать такой кадр!"
                call corruption_required(PS3_monica_shot5_corruption_required) from _rcall_corruption_required_64
                jump gallery_ep22_photoshoot3_pose5
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot5_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_272
            w
            jump gallery_ep22_photoshoot3_pose5



    label gallery_ep22_photoshoot3_pose6:
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
                call corruption_required(PS3_monica_pose6_corruption_required) from _rcall_corruption_required_65
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
            jump gallery_ep22_photoshoot3_pose7
        show screen photoshoot_camera_icon(PS3_shoots_array)
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose6
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
                call corruption_required(PS3_monica_shot6_corruption_required) from _rcall_corruption_required_66
                jump gallery_ep22_photoshoot3_pose5
            m "Алекс!"
            "Это последнее что я сделаю!"
            "Ты меня достал своей назойливостью!"
            sound camera_lens1
            $ photoImage = 8413
            img photoImage
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_134
            w
            img 8414
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_135
            w
            img 8415
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_136
            w
            img 8416
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_137
            w
            img 8417
            w
            call photoshop_flash() from _rcall_photoshop_flash_138
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot6_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_273
            w
            jump gallery_ep22_photoshoot3_pose6
        if result == "side":
            #side
            sound camera_lens1
            $ photoImage = 8411
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_274
            w
            jump gallery_ep22_photoshoot3_pose6
        if result == "down":
            #down+
            sound camera_lens1
            $ photoImage = 8412
            img photoImage
            with Dissolve(0.2)
            if corruption < PS3_monica_shot7_corruption_required:
                m "Алекс! Забудь про такие ракурсы!"
                call corruption_required(PS3_monica_shot7_corruption_required) from _rcall_corruption_required_67
                jump gallery_ep22_photoshoot3_pose5
            w
            # $ add_char_progress("AlexPhotograph", PS3_AlexProgressEachCorruptionShot, "PS3_monica_shot7_progress")
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_275
            w
            jump gallery_ep22_photoshoot3_pose6


    label gallery_ep22_photoshoot3_pose7:

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
        show screen photoshoot()
        $ result = ui.interact()
        hide screen photoshoot
        if result == "next":
            $ shots = 0
            jump gallery_ep22_photoshoot3_pose7
        #up
        if result == "up":
            sound camera_lens1
            img 8420
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_139
            w
            img 8421
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_140
            w
            img 8422
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_141
            w
            img 8423
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_142
            w
            img 8424
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_143
            w
            $ photoImage = 8420
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_276
            w
            jump gallery_ep22_photoshoot3_pose7
        if result == "side":
            #side
            sound camera_lens1
            img 8425
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_144
            w
            img 8426
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_145
            w
            img 8427
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_146
            w
            img 8428
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_147
            w
            $ photoImage = 8425
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_277
            w
            jump gallery_ep22_photoshoot3_pose7
        if result == "down":
            #down
            sound camera_lens1
            img 8429
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_148
            w
            img 8430
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_149
            w
            img 8431
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_150
            w
            img 8432
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_151
            w
            img 8433
            with Dissolve(0.2)
            w
            call photoshop_flash() from _rcall_photoshop_flash_152
            w
            $ photoImage = 8429
            img photoImage
            with Dissolve(0.2)
            w
            call photoshoot_flash_count() from _rcall_photoshoot_flash_count_278
            w
            jump gallery_ep22_photoshoot3_pose7

    return

label gallery_ep22_photoshoot3_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot

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
            return
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
            call gallery_ep22_photoshoot3_casting() from _rcall_gallery_ep22_photoshoot3_casting
            return
        "Идти на кастинг к Бифу и притвориться цыпочкой... (low corruption, required [photoshoot3_casting_corruption_required]) (disabled)" if (biffMonicaCastingsEnabled == True or monicaWorkingAtBiffOffice == True) and corruption < photoshoot3_casting_corruption_required:
            pass

    return

label gallery_ep22_photoshoot3_casting:
    music Groove2_85
    sound highheels_short_walk
    img 8463
    with fadelong
    w
    img 8464
    with Dissolve(0.5)
    m "Привет, Биф. Я пришла..."
    img 8465
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
            biff "Что девушка с календаря хочет показать папочке?"
            $ chickMode = True
            $ castingCloth = 3
            call gallery_8442() from _rcall_gallery_8442_12
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
            call gallery_8442() from _rcall_gallery_8442_13
            img 8480
            with fade
            mt "Мерзавец!"
            #рост прогресса у Бифа


    return
