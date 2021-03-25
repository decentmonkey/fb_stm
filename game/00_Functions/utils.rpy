
init python:
    def getRes(pixels):
        return int(pixels * gui.resolution.koeff)

    def getMousePosition():
        import pygame
        x, y = pygame.mouse.get_pos()
        store.mousex = x
        store.mousey = y

    def checkDialogueExists():
        if renpy.get_screen("choice") != None or renpy.get_screen("window") != None:
            return True
        return False

    def mycopytext(t):
        try:
            pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))
        except:
            print "error copy to clipboard!"

        return

    def makeDump():
        global scenes_data, debugMode
        if debugMode != True:
            return
        print "Debug!"
        dir1 = "/tmp"
        if os.path.isdir(dir1) == True:
            str1 = json.dumps(scenes_data)
            f = open(dir1 + "/renpy_debug.json","w")
            f.write(str1)
            f.close()
            import operator
            x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
            sorted_x = sorted(hooks_log.items(), key=operator.itemgetter(1))
            str1 = json.dumps(sorted_x)
            f = open(dir1 + "/renpy_debug_hooks.json","w")
            f.write(str1)
            f.close()
        if os.path.isdir("c:/debug") == True:
            str1 = json.dumps(scenes_data)
            f = open("c:/debug/renpy_debug.json","w")
            f.write(str1)
            f.close()
            return

    profileTime = time.time()
    def profile(log_message=False):
        global profileTime
        timeDiff = time.time()-profileTime
        if log_message != False:
            print log_message
        print timeDiff
        profileTime = time.time()

    def notif(str1):
        global notifList, lastNotifTime
        if renpy.get_screen("notify") == None:
            notifList = []

        notifList.append(str1)
#        renpy.notify(str1)
        lastNotifTime = time.time()
        renpy.hide_screen("notify")
        renpy.show_screen("notify", "notifList")
        return

    def notif_clean():
        renpy.hide_screen("notify")
        notifList = []
        return

    def notifCheckTimeout(): #костыль на исчезание нотификаций при скиппинге текста
        global lastNotifTime
        if time.time() - lastNotifTime > 20.0:
#            print "force remove notifications"
            notifList = []
            renpy.hide_screen("notify")
        return

    def notif_monica():
        global monicaBitch
        if monicaBitch:
            notif(t_("Моника стерва"))
        else:
            notif(t_("Моника приличная"))

        return

    def rand(from_int, to_int):
        return renpy.random.randint(from_int,to_int)

    def convertMoneyStr(in_money):
        return '{:3,.2f}'.format(in_money)

    def round_down(x, a):
        return math.floor(x / a) * a

    def check_hide_text():
        if not renpy.get_screen("screen_sprites"):
            renpy.hide_screen("say")
            return
        return True

    def cleaning_sound():
        cleanSound = "cleaning" + str(renpy.random.randint(1, 3))
        sound_exec(cleanSound)
        return

    def check_julia_progress(progress_amount):
        if char_info.has_key("Julia") and char_info["Julia"]["level"] == 7 and char_info["Julia"]["current_progress"] >= progress_amount:
            return True
        return False

    def set_rest_place(str):
        global monicaRestHostel, monicaRestApartments, monicaRestJuliaHome, monicaRestHouse, monicaRestHouseDay, monicaRestJuliaHomeDay, monicaRestApartmentsDay, monicaRestHostelDay
        if str == "basement_bed":
            monicaRestHostel = False
            monicaRestApartments = False
            monicaRestJuliaHome = False
            monicaRestHouse = True
            monicaRestHouseDay = day
        if str == "juliahome":
            monicaRestJuliaHome = True
            monicaRestJuliaHomeDay = day
            monicaRestHouse = False
            monicaRestApartments = False
        if str == "slums_apartments":
            monicaRestHostel = False
            monicaRestApartments = True
            monicaRestApartmentsDay = day
            monicaRestHouse = False
            monicaRestJuliaHome = False
        if str == "hostel":
            monicaRestHostel = True
            monicaRestApartments = False
            monicaRestHostelDay = day
            monicaRestHouse = False
            monicaRestJuliaHome = False
        if str == "none":
            monicaRestHostel = False
            monicaRestApartments = False
            monicaRestHouse = False
            monicaRestJuliaHome = False
        return

    def pub_dance_dialogues_set_excitement_monica(excitement):
        global stage_Monica_Excitement_Current, stage_Monica_Excitement_Last
        stage_Monica_Excitement_Last = stage_Monica_Excitement_Current
        stage_Monica_Excitement_Current = stage_Monica_Excitement_Current + excitement
        if stage_Monica_Excitement_Current > 100:
            stage_Monica_Excitement_Current = 100
        return

    def pub_dance_dialogues_set_excitement_molly(excitement):
        global stage_Molly_Excitement_Current, stage_Molly_Excitement_Last
        stage_Molly_Excitement_Last = stage_Molly_Excitement_Current
        stage_Molly_Excitement_Current = stage_Molly_Excitement_Current + excitement
        if stage_Molly_Excitement_Current > 100:
            stage_Molly_Excitement_Current = 100
        return

    def pub_dance_dialogues_fix_excitement():
        global stage_Monica_Excitement_Current, stage_Monica_Excitement_Last, stage_Molly_Excitement_Current, stage_Molly_Excitement_Last
        stage_Monica_Excitement_Last = stage_Monica_Excitement_Current
        stage_Molly_Excitement_Last = stage_Molly_Excitement_Current
        return

    def gallery_stor(*args):
        global gallery_store_vars
        gallery_store_vars = {}
        for storeVar in args:
            if globals().has_key(storeVar):
                gallery_store_vars[storeVar] = globals()[storeVar]

    def gallery_rest():
        global gallery_store_vars
        for storeVar in gallery_store_vars:
            globals()[storeVar] = gallery_store_vars[storeVar]
        gallery_store_vars = False

label mycopytext_label(txt):
    $ mycopytext(txt)
    return

label photoshop_flash():
    sound snd_photo_capture
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return

label textonblack(in_text):
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    $ renpy.pause(1.0, hard=True)
    pause 0.5
    scene black_screen
    with Dissolve(1)
    return


label textonblack_long(in_text):
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    $ renpy.pause(5.0, hard=True)
    scene black_screen
    with Dissolve(1)
    return

label textonblack_pause(in_text):
#    $ _dismiss_pause = False
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
#    $ _dismiss_pause = True
    pause
    scene black_screen
    with Dissolve(1)
    return

label cleanNotifList():
    $ notifList = []
    return

label showRandomImages(imagesList, imagesAmount, makeRandom=False):
    $ imagesList = random.sample(set(imagesList), imagesAmount)
    if makeRandom == False:
        $ imagesList.sort()
    $ imagesListIdx = 0
    label showRandomImages_loop:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            w
            $ imagesListIdx += 1
            jump showRandomImages_loop
    return

label showRandomImagesDiss(imagesList, imagesAmount, makeRandom=False):
    $ imagesList = random.sample(set(imagesList), imagesAmount)
    if makeRandom == False:
        $ imagesList.sort()
    $ imagesListIdx = 0
    label showRandomImages_loop_diss:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            with diss
            w
            $ imagesListIdx += 1
            jump showRandomImages_loop_diss
    return


label showRandomImagesFirstFade(imagesList, imagesAmount, makeRandom=False):
    $ firstFlag = True
    $ imagesList = random.sample(set(imagesList), imagesAmount)
    if makeRandom == False:
        $ imagesList.sort()
    $ imagesListIdx = 0
    label showRandomImages_loop2:
        if imagesListIdx < imagesAmount:
            $ imageName = str(imagesList[imagesListIdx])
            img imageName
            if firstFlag == True:
                with fade
                $ firstFlag = False
            w
            $ imagesListIdx += 1
            jump showRandomImages_loop2
    return








#
