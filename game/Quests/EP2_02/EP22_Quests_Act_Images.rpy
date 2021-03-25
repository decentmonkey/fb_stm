    # Общие 7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431

    # Если Governess Pants (Betty 7419), 7421, 7432, 7433, 7434, 7435
    # Если Governess Pants Betty_1 (Betty 7436) 7437, 7438, 7439
    # Если Governess Pants Betty_2 (Betty 7440) 7441, 7442, 7443
    # Если Governess Pants Betty_3 (Betty 7444) 7445, 7446, 7447
    # Если Governess Pants Betty_4 (Betty 7448) 7449, 7450, 7451
    # Если Governess Pants Betty_5 (Betty 7452) 7453, 7454, 7455

label ep22_Act_Images_monica_cleaning_spot:
    $ images = [7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431]
    $ imagesList = random.sample(set(images), 4)
    $ amount = 4
    $ bettyHere = False
    if get_active_objects("Betty", scene="floor2") != False:
        $ bettyHere = True
    if cloth == "Governess":
        if monicaBettyPanties == False:
            if monicaUnder == "Nude":
                if bettyHere == True:
                    img 10609
                    w
                img 10610
                call showRandomImages(images, 4, True) from _call_showRandomImages_22
                img 10611
                w

            else:
                if bettyHere == True:
                    img 7419
                    w
                img 7421
                call showRandomImages(images, 4, True) from _call_showRandomImages_23
                img 7432
                w
        else:
            if monicaBettyPantiesId == 1:
                if bettyHere == True:
                    img 7436
                    w
                img 7437
                call showRandomImages(images, 4) from _call_showRandomImages_24
                img 7437
                w
            if monicaBettyPantiesId == 2:
                if bettyHere == True:
                    img 7440
                    w
                img 7441
                call showRandomImages(images, 4) from _call_showRandomImages_25
                img 7441
                w
            if monicaBettyPantiesId == 3:
                if bettyHere == True:
                    img 7444
                    w
                img 7445
                w
                img 7446
                w
                call showRandomImages(images, 4) from _call_showRandomImages_26
                img 7447
                w
            if monicaBettyPantiesId == 4:
                if bettyHere == True:
                    img 7448
                    w
                img 7449
                call showRandomImages(images, 4) from _call_showRandomImages_27
                img 7449
                w
            if monicaBettyPantiesId == 5:
                if bettyHere == True:
                    img 7452
                    w
                img 7453
                w
                img 7454
                w
                call showRandomImages(images, 4) from _call_showRandomImages_28
                img 7455
                w
    call ep22_dialogue2_7() from _call_ep22_dialogue2_7
    return

label ep22_Act_Images_monica_put_up_panties:
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10612
            with fade
            $ images = [10613, 10614, 10615, 10616]
            mt "Я... Не привыкла..."
            call showRandomImages(images, 2) from _call_showRandomImages_29
            mt "Ходить без трусиков..."
        else:
            $ images = [7121, 7122]
            img 7120
            with fade
            mt "Это трусики Юлии..."
            "Я уже к ним привыкла..."
            w
            call showRandomImages(images, 2) from _call_showRandomImages_30
    else:
        if monicaBettyPantiesId == 1:
            $ images = [7124, 7125, 7126, 7127, 7128, 7129, 7130]
            img 7123
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4) from _call_showRandomImages_31
        if monicaBettyPantiesId == 2:
            $ images = [7132, 7133, 7134, 7135, 7136]
            img 7131
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 3) from _call_showRandomImages_32
        if monicaBettyPantiesId == 3:
            $ images = [7138, 7139, 7140, 7141, 7142, 7143, 7144]
            img 7137
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4) from _call_showRandomImages_33
        if monicaBettyPantiesId == 4:
            $ images = [7146, 7147, 7148, 7149, 7150, 7151, 7152]
            img 7145
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4) from _call_showRandomImages_34
        if monicaBettyPantiesId == 5:
            $ images = [7154, 7155, 7156, 7157, 7158, 7159, 7160, 7161, 7162]
            img 7153
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 5) from _call_showRandomImages_35
        $ add_corruption(monicaBettyPantiesCorruption, "monicaBettyPantiesCorruption_" + str(day))

    return
