init python:
    import urllib
    import urllib2
    import json
    import ssl
    print config.basedir
    import os

    def get_url_data(url):
        retry = 5
#        renpy.pause()
        while retry > 0:
            try:
                response = urllib2.urlopen(url)
                response_data = response.read()
                response.close()
                return response_data
            except:
                retry -=1
#                return response.getcode()
        return False

    def updating_game(URL, updateData, localUpdateData, updateFiles, deleteFiles):
        global updateStatusLog, updateGlobalStatusText, updateButtonEnabled, updateTotalFiles, updateFetchedFiles, updateQuitButtonEnabled
        updateGlobalStatusText = False
        updateButtonEnabled = False
        updateTotalFiles = len(updateFiles)
#        updateFiles = []
#        deleteFiles = []

        for idx in range(0, len(updateFiles)):
            fileName = updateFiles[idx]
            updateStatusLog.append("Fetching: " + fileName)
            renpy.show_screen("game_updater")
            renpy.pause(0.05)
            fetchData = get_url_data(URL + urllib.quote(fileName))
            if fetchData != False:
                outputFilePath = config.basedir + "/game/" + fileName
                if not os.path.exists(os.path.dirname(outputFilePath)):
                    os.makedirs(os.path.dirname(outputFilePath))
                open(outputFilePath, "wb").write(fetchData)
                localUpdateData["files"][fileName] = updateData["files"][fileName]
                update_update_data(localUpdateData)
                updateFetchedFiles += 1
            else:
                updateStatusLog.append("Error during downloading update!")
                renpy.pause(5.0, hard=True)
                renpy.pause()
                return

        for fileName in deleteFiles:
            updateStatusLog.append("Deleting: " + fileName)
            renpy.show_screen("game_updater")
            renpy.pause(0.1)
            outputFilePath = config.basedir + "/game/" + fileName
            try:
                os.remove(outputFilePath)
            except:
                updateStatusLog.append("Can't delete: " + fileName)
            if localUpdateData["files"].has_key(fileName):
                localUpdateData["files"].pop(fileName, None)
                update_update_data(localUpdateData)

        updateStatusLog = []
        localUpdateData["version"] = updateData["version"]
        update_update_data(localUpdateData)
        updateGlobalStatusText = "Updating completed!"
        updateTotalFiles = 0
        updateQuitButtonEnabled = True

        renpy.pause()
        renpy.quit()
        return

    def update_update_data(localUpdateData):
        str = json.dumps(localUpdateData)
        open(config.basedir + "/game/update_data.json", "wb").write(str)
        return

label show_game_updater:
#    if persistent.download_code
    show screen game_updater_background()
    with diss
    $ updateDownloadCode = renpy.input("Download code: (enter to confirm)", "")
    hide screen game_updater_background

    $ URL = "http://update.decent-monkey.com/repo2/" + updateDownloadCode + "/game/"
    $ updateDataURL = URL + "update_data.json"

    $ updaterProgressBarValue = 50
    $ updateGlobalStatusText = "Checking for Updates..."
    $ updateButtonEnabled = False
    $ updateQuitButtonEnabled = False
    $ updateTotalFiles = 0
    $ updateFetchedFiles = 0
    $ updateStatusLog = []
    show screen game_updater()
    with diss
    pause 0.1
    $ updateError = False
    $ print updateDataURL
    $ updateDataRaw = get_url_data(updateDataURL)
    if updateDataRaw == False:
        $ updateError = True
        $ updateGlobalStatusText = "Error in connection! (wrong code?)"
        show screen game_updater()
        pause
        return

    python:
        try:
            updateData = json.loads(updateDataRaw)
        except:
            updateError = True
            updateGlobalStatusText = "Error in connection! (wrong code?)"
            renpy.show_screen("game_updater")
            renpy.pause()
    if updateError == True:
        return

    python:
        localUpdateDataRaw = open(config.basedir + "/game/update_data.json", "r").read()
        localUpdateData = json.loads(localUpdateDataRaw)
        updateFiles = []
        for fileName, hash in updateData["files"].iteritems():
            if fileName.find(".rpy") == -1:
                if localUpdateData["files"].has_key(fileName) == False or hash != localUpdateData["files"][fileName]:
                    updateFiles.append(fileName)
        for fileName, hash in updateData["files"].iteritems():
            if fileName.find(".rpy") != -1:
#            if fileName.find(".mkv") != -1:
                if localUpdateData["files"].has_key(fileName) == False or hash != localUpdateData["files"][fileName]:
                    updateFiles.append(fileName)
        listFiles = renpy.list_files()
        deleteFiles = []
        for fileName in listFiles:
            fileName = str(fileName)
            if updateData["files"].has_key(fileName) == False and fileName != "update_data.json" and fileName != "script_version.txt":
                deleteFiles.append(fileName)


        updaterProgressBarValue = 100

        if len(updateFiles)>0 or len(deleteFiles)>0:
            updateGlobalStatusText = updateData["version"]
            updateButtonEnabled = True
        else:
            updateGlobalStatusText = "Up to date!"
            updateButtonEnabled = False
    show screen game_updater()
    $ result = ui.interact()
    if result == 1 and updateButtonEnabled == True:
        $ _game_menu_screen = None
        if updateData.has_key("assets_url"):
            URL = updateData["assets_url"]
        $ updating_game(URL, updateData, localUpdateData, updateFiles, deleteFiles)
        $ _game_menu_screen = 'save'
    return

screen game_updater_background():
    add "gui/main_menu.png"

screen game_updater():
    layer "master"
    zorder 20
#    modal True
    button:
        background "gui/main_menu.png"
        xfill True
        yfill True
        action [
            Return()
        ]

    frame:
        background Frame("gui/updater/frame_updater.png", left=2, top=2, right=2, bottom=2)
        pos (0.5,0.5)
        anchor (0.5,0.5)
        xysize (900,480)


        if updateTotalFiles > 0:
            text str(updateFetchedFiles) + " / " + str(updateTotalFiles):
                pos (0.5, 280)
                anchor (0.5,0)
                font "fonts/BebasNeue Regular.ttf"
                size 40
                color "#ffffff"
            $ updaterProgressBarValue = float(updateFetchedFiles) / float(updateTotalFiles) * 100.0
            $ print updaterProgressBarValue

        bar:
            value int(updaterProgressBarValue)
            range 100
            xysize (800, 40)
            xalign 0.5
            ypos 220

        if updateGlobalStatusText != False:
            text updateGlobalStatusText:
                pos (0.5, 170)
                font "fonts/BebasNeue Regular.ttf"
                color "#ffffff"
                size 40
                anchor(0.5, 0)

        if updateButtonEnabled == True:
            imagebutton:
                xpos 350
                ypos 280
                idle "gui/updater/update_button.png"
                hover "gui/updater/update_button_hover.png"
                action [
                    Return(1)
                ]
        if updateQuitButtonEnabled == True:
            imagebutton:
                xpos 350
                ypos 280
                idle "gui/updater/update_button_restart.png"
                hover "gui/updater/update_button_restart_hover.png"
                action [
                    Return(1)
                ]

        if len(updateStatusLog) > 0:
            python:
                startIdx = 0
                if len(updateStatusLog)>5:
                    startIdx = len(updateStatusLog)-5
                logText = ""
                for idx in range(startIdx, len(updateStatusLog)):
                    logText += updateStatusLog[idx] + "\n"
            text logText:
                pos (80, 220)
                anchor(0.0, 1.0)
                size 20
                font "fonts/arial.ttf"
                color "#ffffff"
                xsize 640
