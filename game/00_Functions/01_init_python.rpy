python early:
    def overlay_parse(lex):
        img = lex.simple_expression()
        overlay = lex.simple_expression()
        return (img, overlay)
    def overlay_exec(o):
        imgName, overlayName = o
        try:
            imagePathExt = img_find_path_ext(str(renpy.eval(imgName)) + "_oversprite")
        except:
            imagePathExt = img_find_path_ext(str(imgName) + "_oversprite")
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imagePath = imagePathExt[0]
            imgName = imagePathExt[1]
        try:
            overlayName = renpy.eval(overlayName)
        except:
            overlayName = overlayName
        canvas_offsets = get_overlay_canvas_offset(imgName)
        renpy.show_screen("show_image_screen_image_overlay", imagePath, canvas_offsets, overlayName)
        return

    def overlay_pred(o):
        imgName, overlayName = o
        try:
            imagePathExt = img_find_path_ext(str(renpy.eval(imgName)) + "_oversprite")
        except:
            imagePathExt = img_find_path_ext(str(imgName) + "_oversprite")
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imgName = imagePathExt[1]
            imagePath = imagePathExt[0]
        return [Image(imagePath)]
    renpy.register_statement("overlay", parse=overlay_parse, execute=overlay_exec, predict=overlay_pred) #кастомный overlay

    def img_disp(l):
        return (l.simple_expression(), l.rest())
#        return l.string()

    def imgd_disp(l):
        return (l.simple_expression(), "d")
    def imgf_disp(l):
        return (l.simple_expression(), "f")
    def imgfl_disp(l):
        return (l.simple_expression(), "fl")

    def img_exec(s_in):
        global dialogue_active_flag, screenActionHappened, config
#        config.has_autosave = False
#        config.autosave_on_choice = False
        s = s_in[0]
        transition = s_in[1]
        try:
            imagePathExt = img_find_path_ext(renpy.eval(s))
        except:
            imagePathExt = img_find_path_ext(s)
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imagePath = imagePathExt[0]
        if renpy.exists(imagePath) == False and not renpy.android:
            imagePath = "images/Overlays/black_screen.jpg"

        check_achievement(imagePathExt[1])
        if (renpy.get_screen("say") != None or renpy.get_screen("choice") != None or renpy.get_screen("window") != None or dialogue_active_flag == True) and persistent.pause_before_change_slide == True and renpy.get_screen("show_image_screen_image") != None:
            renpy.hide_screen("say")
            renpy.hide_screen("choice")
            renpy.hide("window")
            renpy.show_screen("dialogue_down_arrow")
            renpy.pause()
            renpy.hide_screen("dialogue_down_arrow")
            dialogue_active_flag = False
        renpy.scene()
        renpy.show_screen("show_image_screen_image", imagePath)
        image_screen_scene_flag = False
        screenActionHappened = True
        if transition and transition != "":
            transitions_dict = {
                "f": fade,
                "d": diss,
                "fl": fadelong
            }
            if transitions_dict.has_key(transition):
                transition = transitions_dict[transition]
            else:
                try:
                    transition = renpy.eval(transition)
                except:
                    transition = transition
            renpy.with_statement(transition)
        return

    def img_pred(s_in):
        s, transition = s_in
        try:
            imagePathExt = img_find_path_ext(renpy.eval(s))
        except:
            imagePathExt = img_find_path_ext(s)
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imagePath = imagePathExt[0]
        return [Image(imagePath)]
    renpy.register_statement("img", parse=img_disp, execute=img_exec, predict=img_pred) #кастомный scene
    renpy.register_statement("imgd", parse=imgd_disp, execute=img_exec, predict=img_pred)
    renpy.register_statement("imgf", parse=imgf_disp, execute=img_exec, predict=img_pred)
    renpy.register_statement("imgfl", parse=imgfl_disp, execute=img_exec, predict=img_pred)

    def imgl_exec(s_in):
        s, transition = s_in
        global dialogue_active_flag, screenActionHappened
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_left", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgl", parse=img_disp, execute=imgl_exec, predict=img_pred)

    def imgr_exec(s_in):
        s, transition = s_in
        global dialogue_active_flag, screenActionHappened
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_right", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgr", parse=img_disp, execute=imgr_exec, predict=img_pred)

    def imgcenter_exec(s_in):
        s, transition = s_in
        global dialogue_active_flag, screenActionHappened
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_center", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgc", parse=img_disp, execute=imgcenter_exec, predict=img_pred)

    def saywrapper_parse(lex):
        who = lex.simple_expression()
        what = lex.simple_expression()
#        what = lex.string()
        if what == None:
            what = who
            who = "Noone"
        return (who,what)

    def saywrapper_lint(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)


    def saywrapper_execute(o):
        global last_dialogue_character
        global dialogue_active_flag, screenActionHappened, config

        who, what = o
        if who == "Noone":
            who = last_dialogue_character
        else:
            last_dialogue_character = who
#        who = t__(eval(who).name)
        what = what[1:-1]
#        what = re.sub(r'\n' , '\s', what)
        dialogue_active_flag = True
        screenActionHappened = True

        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_SLASH]:
            return

        what = t___(what)
#        what = re.sub(r'(\n\s*)', " ", what)
#        what = t__(what)
#        what = what.replace(" ", " ")
#        what = re.sub("\!\s{1,}", "!\n", what)
#        what = re.sub("\?\s{1,}", "?\n", what)
#        what = re.sub("\.\s{1,}", ".\n", what)
#        what = re.sub("Mr\.\\n", "Mr. ", what)
#        what = re.sub("Mrs\.\\n", "Mrs. ", what)
#        what = re.sub("Ms\.\\n", "Ms. ", what)

        if persistent.auto_clipboard == True:
            copy_what = re.sub("\!\s{1,}", "!\n", what)
            copy_what = re.sub("\?\s{1,}", "?\n", copy_what)
            copy_what = re.sub("\.\s{1,}", ".\n", copy_what)
            mycopytext(copy_what) #put into clipboard

        renpy.say(who, what)

    renpy.register_statement("", parse=saywrapper_parse, execute=saywrapper_execute, lint = saywrapper_lint, translatable=True) #враппер для say, чтобы подымать флаг активного диалога


    def w_parse(l):
        return None

    def w_exec(o):
        global dialogue_active_flag, screenActionHappened
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        renpy.show_screen("dialogue_down_arrow")
        dialogue_active_flag = True
        keyPressed = pygame.key.get_pressed()
        if not keyPressed[pygame.K_SLASH]:
            renpy.pause()
        dialogue_active_flag = False
        renpy.hide_screen("dialogue_down_arrow")
        dialogue_active_flag = False
        screenActionHappened = True

    def wclean_exec(o):
        global dialogue_active_flag, screenActionHappened
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = True
        renpy.pause()
        dialogue_active_flag = False
        screenActionHappened = True

    renpy.register_statement("w", parse=w_parse, execute=w_exec) #w - оператор ожидания с мигающей стрелкой
    renpy.register_statement("wclean", parse=w_parse, execute=wclean_exec) #w - оператор ожидания с мигающей стрелкой

    def wc_exec(o):
        global dialogue_active_flag
        dialogue_active_flag = False

    renpy.register_statement("wc", parse=w_parse, execute=wc_exec) #wait dialogue clear, удаляет флаг того что висит открытый диалог (для пикч)


    def sound_parse(l):
        return l.simple_expression()

    def sound_exec(o):
        try:
            soundName = renpy.eval(o)
        except:
            soundName = o
        checkPath = "Sounds/" + str(soundName) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Sounds/" + str(soundName) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Sounds/" + str(soundName) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Music/" + str(soundName) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Music/" + str(soundName) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Music/" + str(soundName) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return

    renpy.register_statement("sound", parse=sound_parse, execute=sound_exec) #sound - оператор воспроизведения звука

    def sound2_parse(l):
        return l.simple_expression()

    def sound2_exec(o):
        try:
            sound2Name = renpy.eval(o)
        except:
            sound2Name = o
        checkPath = "Sounds/" + str(sound2Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Sounds/" + str(sound2Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Sounds/" + str(sound2Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Music/" + str(sound2Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Music/" + str(sound2Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Music/" + str(sound2Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return

    renpy.music.register_channel("sound2", "sfx", False)
    renpy.register_statement("sound2", parse=sound2_parse, execute=sound2_exec) #sound2 - оператор воспроизведения звука

    def sound3_parse(l):
        return l.simple_expression()

    def sound3_exec(o):
        try:
            sound3Name = renpy.eval(o)
        except:
            sound3Name = o
        checkPath = "Sounds/" + str(sound3Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Sounds/" + str(sound3Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Sounds/" + str(sound3Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Music/" + str(sound3Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Music/" + str(sound3Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Music/" + str(sound3Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return

    renpy.music.register_channel("sound3", "sfx", False)
    renpy.register_statement("sound3", parse=sound3_parse, execute=sound3_exec) #sound3 - оператор воспроизведения звука

    def music_parse(l):
        return (l.simple_expression(), l.rest())

    def music_exec(ob1):
        global currentMusic, currentMusicPriority
        o, priority = ob1

        if o == "stop":
            currentMusic = False
            currentMusicPriority = 0
            renpy.music.stop(channel='music', fadeout=1.0)
            return
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        if musicName == currentMusic:
            return

        try:
            priority1 = int(priority)
        except ValueError:
            priority1 = 0
        if str(priority) == "low":
            priority1 = 0
        if str(priority) == "high":
            priority1 = 10
        if priority1 < currentMusicPriority:
            return
        currentMusic = musicName
        currentMusicPriority = priority1
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
            print "play!" + str(checkPath)
            renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)
        else:
            checkPath = "Sounds/" + str(musicName) + ".ogg"
            if renpy.loadable(checkPath):
                renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)
        return

    renpy.register_statement("music", parse=music_parse, execute=music_exec) #music - оператор воспроизведения музыки

    def fadeblack_parse(l):
        return (l.rest())
    def fadeblack_exec(ob1):
        music_exec(("stop", ""))
        img_exec(("black_screen", "d"))
        try:
            if float(ob1) > 0:
                renpy.pause(float(ob1))
        except:
            return
        return

    renpy.register_statement("fadeblack", parse=fadeblack_parse, execute=fadeblack_exec) #fadeblack - оператор затухания экрана

    def store_music():
        global storedMusic, currentMusic, currentMusicPriority
        storedMusic.insert(0, currentMusic)
        storedMusicPriority.insert(0, currentMusicPriority)
        return

    def restore_music():
        global storedMusic, currentMusic, currentMusicPriority
        currentMusic1 = False
        if len(storedMusic) > 0:
            currentMusic1 = storedMusic.pop(0)
            currentMusicPriority1 = storedMusicPriority.pop(0)
        if currentMusic1 == False:
#            renpy.music.stop(channel='music', fadeout=1.0)
            return
        if currentMusic1 == currentMusic:
            return
        currentMusic = currentMusic1
        currentMusicPriority = currentMusicPriority1
        checkPath = "Music/" + str(currentMusic) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)
        return

    def clear_music_stack():
        storedMusic = []
        currentMusicPriority = 0
        return

    def music2_exec(ob1):
        global currentMusic2
        o, priority = ob1
        if o == "stop":
            currentMusic2 = False
            renpy.music.stop(channel='music2', fadeout=1.0)
            return
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        if musicName == currentMusic2:
            return

        currentMusic2 = musicName
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
#            print "play music: " + checkPath
            renpy.music.play(checkPath, channel="music2", loop=True, fadeout=1.0, fadein=1.0)
        else:
            checkPath = "Sounds/" + str(musicName) + ".ogg"
            if renpy.loadable(checkPath):
                renpy.music.play(checkPath, channel="music2", loop=True, fadeout=1.0, fadein=1.0)
        return

    renpy.music.register_channel("music2", "music", True)
    renpy.register_statement("music2", parse=music_parse, execute=music2_exec) #music - оператор воспроизведения музыки

    def music3_exec(ob1):
        global currentMusic3
        o, priority = ob1
        if o == "stop":
            currentMusic3 = False
            renpy.music.stop(channel='music3', fadeout=1.0)
            return
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        if musicName == currentMusic3:
            return

        currentMusic3 = musicName
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
#            print "play music: " + checkPath
            renpy.music.play(checkPath, channel="music3", loop=True, fadeout=1.0, fadein=1.0)
        else:
            checkPath = "Sounds/" + str(musicName) + ".ogg"
            if renpy.loadable(checkPath):
                renpy.music.play(checkPath, channel="music3", loop=True, fadeout=1.0, fadein=1.0)
        return

    renpy.music.register_channel("music3", "music", True)
    renpy.register_statement("music3", parse=music_parse, execute=music3_exec) #music - оператор воспроизведения музыки

    def video_parse(l):
        return l.simple_expression()
    def video_exec(o):
        try:
            videoName = get_filename(renpy.eval(o))
        except:
            videoName = get_filename(o)
        print(videoName)
        playing_video = Movie(play=videoName, channel="movie") #?????


    renpy.register_statement("video", parse=video_parse, execute=video_exec) #video - оператор воспроизведения видео


    def custom_tag1(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color=#e8b131"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
