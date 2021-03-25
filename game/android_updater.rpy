label android_assets_updater(downloading_assets_list):
    python:
        baseURL = "http://update.decent-monkey.com/repo/online_DM/assets/"
    $ updateStatusLog = []
    $ updateTotalFiles = len(downloading_assets_list)
    $ updateFetchedFiles = 0
    $ updateGlobalStatusText = ""
    $ updateButtonEnabled = False
    $ updateQuitButtonEnabled = False
    python:
        for idx in range(0, len(downloading_assets_list)):
            fileName = downloading_assets_list[idx]
            updateStatusLog.append("Fetching: " + fileName)
            renpy.show_screen("game_updater")
            renpy.pause(0.05)
            fetchData = get_url_data(baseURL + urllib.quote(fileName))
            if fetchData != False:
                outputFilePath = os.path.join(assetsStorageDirectory, "images/" + fileName)
                if not os.path.exists(os.path.dirname(outputFilePath)):
                    os.makedirs(os.path.dirname(outputFilePath))
                open(outputFilePath, "wb").write(fetchData)
                updateFetchedFiles += 1
            else:
                updateStatusLog.append("Error during downloading assets!")
                renpy.pause(5.0, hard=True)
                renpy.pause()
                break
    hide screen game_updater
    $ list_files_dict_assets = False
    return

label android_assets_updater_check:
    return
    $ assetsStorageDirectory = renpy.config.savedir.replace("/saves", "/assets")
    # if android
    if renpy.android != True:
        return
    python:
        list_files = renpy.list_files()
        downloading_assets_list = []
        list_files_dict_assets = {}
        for filename in list_files:
#            baseName = os.path.basename(os.path.splitext(filename)[0]).lower()
            baseName = os.path.split(filename)[1]
            list_files_dict_assets[baseName] = filename

        assets_list = get_assets_list()

        for asset_name in assets_list["slides"]:
            if list_files_dict_assets.has_key(asset_name) == False:
                if os.path.exists(os.path.join(assetsStorageDirectory, "images/" + asset_name)) == False:
                    downloading_assets_list.append(asset_name)

    if len(downloading_assets_list) > 0:
        call android_assets_updater(downloading_assets_list) from _rcall_android_assets_updater
    return
