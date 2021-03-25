default melanie_photoshoot1_count = 0

label ep29_photoshoot_melanie1:
    $ shotsAmount = PS_Melanie_1_shots_amount
    $ shotsTotalAmount = 36

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    music ZigZag
    img 22593
    with fadelong
    melanie "Алекс, я буду следить за тем, какие ты берешь ракурсы."
    alex_photograph "Да, Мелани. Конечно."

label ep29_photoshoot_melanie_suit1_pose1:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose1"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose2"
    #кадр
    img 22593

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22597
        with fadelong
        alex_photograph "Отлично! Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22594, 22595, 22596], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22594
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_210
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22595
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_211
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22596
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_212
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep29_photoshoot_melanie_suit1_pose2:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose2"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose3"
    #кадр
    img 22597

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22601
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
        melanie "Алекс, что ты делаешь?"
        alex_photograph "Мелани, я нашел интересный ракурс."
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22598, 22599, 22600], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22598
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_213
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22599
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, ты помнишь, о чем мы с тобой договаривались?"
        alex_photograph "Конечно, Мелани. Никаких откровенных ракурсов!"
        alex_photograph "Я делаю все, как ты сказала!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_214
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22600
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_215
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose3:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose3"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose4"
    #кадр
    img 22601

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22605
        with fadelong
#        w
#        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22602, 22603, 22604], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22602
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Ты просто божественно прекрасно получишься на снимке."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_216
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22603
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Ничего лишнего не будет видно, Мелани."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_217
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22604
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_218
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep29_photoshoot_melanie_suit1_pose4:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose4"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose5"
    #кадр
    img 22605

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22609
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22606, 22607, 22608], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22606
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_219
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22607
        img photoImage
        with Dissolve(0.2)
        alex_photograph "Ничего лишнего не будет видно, Мелани."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_220
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22608
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, меня, как Миссис Бакфетт, не проведешь..."
        melanie "Не смей снимать меня с такого ракурса."
        alex_photograph "Мелани, не переживай. На снимке ничего не видно."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_221
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose5:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose5"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose6"
    #кадр
    img 22609

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22613
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22610, 22611, 22612], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22610
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_222
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22611
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс. Не смей делать такие кадры!"
        alex_photograph "Я не фотографирую, Мелани."
        alex_photograph "Я просто пытаюсь подобрать интересный ракурс."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_223
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22612
        img photoImage
        with Dissolve(0.2)
        melanie "Ты меня за кого принимаешь, Алекс?"
        melanie "Я не первый раз участвую в фотосессии."
        melanie "Думаешь, я не понимаю, что ты сейчас сделал?"
        alex_photograph "Мелани, я потом покажу тебе снимки."
        alex_photograph "Ты увидишь, что я делаю вполне приличные кадры."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_224
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose6:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose6"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose7"
    #кадр
    img 22613

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22617
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22614, 22615, 22616], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22614
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_225
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22615
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_226
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22616
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, если ты и дальше будешь продолжать делать такие кадры..."
        melanie "То я откажусь от этой фотоссесии."
        alex_photograph "Мелани, снимки получаются очень приличные."
        alex_photograph "Ты зря так переживаешь. На них совсем ничего не видно."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_227
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose7:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose7"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose8"
    #кадр
    img 22617

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22621
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
#        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22618, 22619, 22620], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22618
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_228
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22619
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_229
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22620
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, тебе сколько раз нужно повторить, чтобы ты не брал такие ракурсы?"
        melanie "Ты хочешь, чтобы эта фотосессия стала последней нашей совместной работой?"
        alex_photograph "Мелани, нет конечно! Кадры получаются очень красивые и приличные!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_230
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose8:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose8"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose9"
    #кадр
    img 22621

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22625
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22622, 22623, 22624], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22622
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_231
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22623
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_232
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22624
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс. Не смей делать такие кадры!"
        alex_photograph "Мелани, с этого ракурса ничего не видно. Не переживай."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_233
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep29_photoshoot_melanie_suit1_pose9:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose9"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose10"
    #кадр
    img 22625

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22629
        with fadelong
        alex_photograph "Следующая поза, Мелани!"
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22626, 22627, 22628], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22626
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_234
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22627
        img photoImage
        with Dissolve(0.2)
        melanie "А сейчас что ты делашь?"
        alex_photograph "Это будет великолепный кадр, Мелани!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_235
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22628
        img photoImage
        with Dissolve(0.2)
        melanie "Если ты меня обманешь, Алекс, то я не буду больше с тобой работать."
        alex_photograph "Мелани, ты можешь не беспокоиться."
        alex_photograph "Я помню, о чем мы договаривались."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_236
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose10:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose10"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose11"
    #кадр
    img 22629

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22633
        with fadelong
        melanie "Алекс, не вздумай в этой позе делать кадры сзади или крупным планом."
        alex_photograph "Конечно, Мелани. Никаких откровенных ракурсов! Я помню."
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22630, 22631, 22632], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 22630
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_237
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22631
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, что ты делаешь?"
        alex_photograph "Мелани, я нашел интересный ракурс."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_238
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22632
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс, ты помнишь, о чем мы с тобой договаривались?"
        alex_photograph "Конечно, Мелани. Никаких откровенных ракурсов!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_239
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose11:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose11"
    $ photoPoseNextLabel = "ep29_photoshoot_melanie_suit1_pose12"
    #кадр
    img 22633

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        img 22638
        with fadelong
        melanie "Алекс, я не буду принимать такую позу."
        melanie "Это пошло. Я тебе не порномодель."
        alex_photograph "Мелани, я обещаю, что эти снимки будут настоящим произведением искусства!"
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22635, 22636, 22637], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 22634
        with Dissolve(0.2)
        w
        call photoshop_flash() from _call_photoshop_flash_175
        w
        sound camera_lens1
        $ photoImage = 22635
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс?"
        alex_photograph "Я фотографирую не сзади, а сверху. Потрясающий кадр, Мелани!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_240
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22636
        img photoImage
        with Dissolve(0.2)
        melanie "А сейчас что ты делашь?"
        alex_photograph "Фотографирую сверху. Просто немного сменил ракурс."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_241
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 22637
        img photoImage
        with Dissolve(0.2)
        melanie "Алекс! Никаких крупных планов. Ты помнишь об этом?"
        alex_photograph "Конечно, Мелани!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_242
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep29_photoshoot_melanie_suit1_pose12:
    $ photoPoseLabel = "ep29_photoshoot_melanie_suit1_pose12"
    $ photoPoseNextLabel = "ep29_photoshoot_suit1_end"
    #кадр
    img 22638

    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        #music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS_Melanie_1_shoots_array)
    show screen photoshoot2([22640, 22641, 22644], PS_Melanie_1_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 22639
        with Dissolve(0.2)
        alex_photograph "Когда ты их увидишь, то захочешь разместить их, как свои портреты, в гримерке!"
        w
        call photoshop_flash() from _call_photoshop_flash_176
        w
        sound camera_lens1
        $ photoImage = 22640
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_243
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 22641
        img photoImage
        with Dissolve(0.2)
        melanie "Чтобы я никаких своих интимных мест крупным планом на них не видела, Алекс."
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_244
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 22642
        with Dissolve(0.2)
        alex_photograph "Конечно, Мелани!"
        w
        call photoshop_flash() from _call_photoshop_flash_177
        w
        sound camera_lens1
        img 22643
        with Dissolve(0.2)
        alex_photograph "Никаких откровенных ракурсов, я помню!"
        w
        call photoshop_flash() from _call_photoshop_flash_178
        w
        sound camera_lens1
        $ photoImage = 22644
        img photoImage
        with Dissolve(0.2)
        alex_photograph "И никаких крупных планов!"
        w
        call photoshoot_flash_count() from _call_photoshoot_flash_count_245
        $ PS_Melanie_1_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel


label ep29_photoshoot_suit1_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    music stop
    img black_screen
    with diss
    pause 0.2
    $ melanie_photoshoot1_count += 1
    $ questHelp("melanie_13", True)
    return
