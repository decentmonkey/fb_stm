label ep212_melanie_home_photoshoot1a:
    $ shotsAmount = 36
    $ shotsTotalAmount = 36
    $ MelanieHome_Photoshoot1_shoots_array = []

    $ shots = 3
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    #кадр
#    img 23856
    #up
#    img 23857
    #side
#    img 23858
    #down
#    img 23859

    # поза 1
    img 23856
    with fadelong
    alex_photograph "Отличная поза, Мелани."
    melanie "Алекс, старайся не брать крупным планом..."
    music stop
label ep212_melanie_home_photoshoot1a_pose1:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose1"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose2"
    img 23856

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        $ renpy.music.set_volume(1.0, 0.5, channel="music")
        music Groove2_85
#        img 23860
#        with fadelong
        # поза 2
        victoria "Нет-нет. Так не пойдет."
        victoria "Нужно что-то более раскрепощенное, подружка Мелани."
        music Molten_Alloy
        img 23860
        with fadelong
        melanie_t "!!!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23857, 23858, 23859], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23857
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_279
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23858
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_280
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23859
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_281
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose2:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose2"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose3"
    #кадр
    img 23860
    #up
#    img 23861
    #side
#    img 23862
    #down
#    img 23863

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        victoria "Подружка Мелани сейчас перестанет прикрываться."
        victoria "Не забывай, что у нас откровенная фотосессия."
        music Molten_Alloy
        img 23864
        with fadelong
        alex_photograph "О, отличный ракурс! Это будут шедевральные кадры!"
        melanie_t "Алекс так радуется..."
        melanie_t "Как-будто я позволю ему оставить эти кадры себе..."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23861, 23862, 23863], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23861
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_282
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23862
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_283
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23863
        img photoImage
        with Dissolve(0.2)
        w
        victoria "Алекс, возьми еще с этого ракурса."
        melanie "Алекс, думаю, что это перебор."
        alex_photograph "Что ты, Мелани! В кадре все смотрится прекрасно!"
        melanie_t "!!!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_284
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose3:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose3"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose4"


    #кадр
    img 23864
    #up
#    img 23865
    #side
#    img 23866
    #down
#    img 23867


    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Molten_Alloy
        # поза 4
        img 23868
        with fadelong
        victoria "Думаю, если подружка Мелани снимет свои трусики..."
        victoria "Кадры станут намного интереснее."
        victoria "Что скажешь, Алекс?"
        alex_photograph "О, да! Это отличная идея, Мисс Виктория!"
        melanie "Алекс, недостаточно того, что у меня грудь практически не прикрыта?"
        alex_photograph "Мелани,  не переживай."
        alex_photograph "Я буду брать такие ракурсы, что ничего лишнего не будет видно."
        melanie_t "Он думает, что меня также легко обмануть, как Миссис Бакфетт..."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23865, 23866, 23867], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23865
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_285
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23866
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_286
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23867
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_287
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose4:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose4"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose5"



    #кадр
    img 23868
    #up
#    img 23869
    #side
#    img 23870
    #down
#    img 23871

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music Groove2_85
        img 17429
        with fadelong
        victoria "Ну? Мы ждем, подружка..."
        melanie_t "!!!"
        # Мелани снимает трусики и остается в одном прозрачном пеньюаре
        music stop
        img black_screen
        with diss
        sound snd_fabric1
        pause 1.5
        music ZigZag
        img 17430
        with fadelong
        # поза 6
        victoria "По-моему, отличная поза."
        victoria "Не останавливайся, Алекс. Продолжай работать."
#        img 23876
#        with fadelong
#        w
        img 23872
        with fadelong
#        w
        # поза 5
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23869, 23870, 23871], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23869
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_288
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23870
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_289
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23871
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_290
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose5:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose5"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose6"


    #кадр
    img 23872
    #up
#    img 23873
    #side
#    img 23874
    #down
#    img 23875

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        img 23876
        with fadelong
        # Виктория пристально смотрит на нее
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23873, 23874, 23875], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23873
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_291
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23874
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_292
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23875
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, мы делаем кадры для порножурнала?"
        alex_photograph "Нет, конечно, Мелани!"
        melanie "Тогда не нужно делать кадры в такой позе."
        melanie_t "!!!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_293
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose6:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose6"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose7"

    #кадр
    img 23876
    #up
#    img 23877
    #side
#    img 23878
    #down
#    img 23879

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        # Виктория пристально смотрит на нее
        img 23880
        with fadelong
        w
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23877, 23878, 23879], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23877
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_294
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23878
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_295
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23879
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_296
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose7:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose7"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose8"






    #кадр
    img 23880
    #up
#    img 23881
    #side
#    img 23882
    #down
#    img 23883

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        # Виктория пристально смотрит на нее
        img 23884
        with fadelong
        victoria "Нужно сделать снимки еще в этой позе."
        victoria "И с этого ракурса."
        melanie_t "!!!"
        alex_photograph "Отличная идея, Мисс Виктория!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23881, 23882, 23883], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23881
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_297
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23882
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_298
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23883
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_299
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose8:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose8"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose9"

    #кадр
    img 23884
    #up
#    img 23885
    #side
#    img 23886
    #down
#    img 23887

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        # Виктория пристально смотрит на нее
        img 23888
        with fadelong
        victoria "Подружка Мелани, расставь ноги пошире."
        victoria "Это будет смотреться более изысканно."
        melanie "Алекс, ты помнишь, что я тебе говорила про кадры крупным планом?"
        alex_photograph "Да, Мелани, конечно."
        alex_photograph "Не беспокойся."
        melanie_t "Дрянь!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23885, 23886, 23887], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23885
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_300
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23886
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_301
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23887
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_302
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose9:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose9"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose10"

    #кадр
    img 23888
    #up
#    img 23889
    #side
#    img 23890
#    img 23891
    #down
#    img 23892

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        # Виктория пристально смотрит на нее
        img 23893
        with fadelong
        # поза 8
        melanie "Алекс, думаю, что пора заканчивать."
        alex_photograph "Еще несколько кадров, Мелани!"
        alex_photograph "Ты не представляешь, какие шикарные кадры получаются!"
        melanie_t "Тебе осталось недолго радоваться этим кадрам..."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23889, 23890, 23892], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23889
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_303
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 23890
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_192
        w
        sound camera_lens1
        $ photoImage = 23891
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_304
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 23892
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_305
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose10:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose10"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose11"




    #кадр
    img 23893
    #up
#    img 23894
    #side
#    img 23895
    #down
#    img 23896
#    img 23897

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        # Виктория пристально смотрит на нее
        img 23898
        with fadelong
        w
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23894, 23895, 23897], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23894
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_306
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 23895
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_307
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 23896
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_193
        w
        sound camera_lens1
        $ photoImage = 23897
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_308
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose11:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose11"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose12"



    #кадр
    img 23898
    #up
#    img 23900
#    img 23899
    #side
#    img 23902
#    img 23901
    #down
#    img 23903
#    img 23904
#    img 23905

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        music ZigZag
        # Виктория пристально смотрит на нее
        img 23906
        with fadelong
        victoria "Нужно сделать снимки еще в этой позе."
        victoria "И с этого ракурса."
        melanie_t "!!!"
        alex_photograph "Отличная идея, Мисс Виктория!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23899, 23901, 23905], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        img 23900
        sound camera_lens1
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_194
        w
        sound camera_lens1
        $ photoImage = 23899
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_309
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        img 23902
        sound camera_lens1
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_195
        w
        sound camera_lens1
        $ photoImage = 23901
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_310
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        img 23903
        sound camera_lens1
        with Dissolve(0.2)
        # поза 7
        victoria "Алекс, возьми еще с этого ракурса крупным планом."
        victoria "Получится отличный кадр."
        melanie_t "Сучка!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_196
        w
        sound camera_lens1
        img 23904
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_197
        w
        sound camera_lens1
        $ photoImage = 23905
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_311
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose12:
    $ photoPoseLabel = "ep212_melanie_home_photoshoot1a_pose12"
    $ photoPoseNextLabel = "ep212_melanie_home_photoshoot1a_pose_end"

    #кадр
    img 23906
    #up
#    img 23907
    #side
#    img 23909
#    img 23908
    #down
#    img 23910
#    img 23911
#    img 23912

    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(MelanieHome_Photoshoot1_shoots_array)
    show screen photoshoot2([23907, 23908, 23912], MelanieHome_Photoshoot1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 23907
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_312
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        img 23909
        sound camera_lens1
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_198
        w
        sound camera_lens1
        $ photoImage = 23908
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_313
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        img 23910
        sound camera_lens1
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_199
        w
        sound camera_lens1
        img 23911
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_200
        w
        sound camera_lens1
        $ photoImage = 23912
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_314
        $ MelanieHome_Photoshoot1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep212_melanie_home_photoshoot1a_pose_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    music stop
    img black_screen
    with diss
    pause 2.0
    return
