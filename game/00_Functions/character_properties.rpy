init python:
    def get_bitchmeter_description():
        global bitchmeterValue, maxBitchness, monicaBitch
        bitchmeter_captions = ["Shy Girl", "Decent Girl", "Casual Girl", "Hot-Tempered", "Bitch", "Complete Bitch", "Bitch from the Hell"]

        if bitchmeterValue <= maxBitchness / 2:
            monicaBitch = False
        else:
            monicaBitch = True

#        if bitchmeterValue < float(maxBitchness) / 100 * 20:
        if bitchmeterValue <= 153:
            return bitchmeter_captions[0]
        if bitchmeterValue <= float(maxBitchness) / 100 * 49:
            return bitchmeter_captions[1]
        if bitchmeterValue <= float(maxBitchness) / 100 * 51:
            return bitchmeter_captions[2]
        if bitchmeterValue < float(maxBitchness) / 100 * 60:
            return bitchmeter_captions[3]
        if bitchmeterValue < float(maxBitchness) / 100 * 80:
            return bitchmeter_captions[4]
        if bitchmeterValue < float(maxBitchness) / 100 * 100:
            return bitchmeter_captions[5]
        if bitchmeterValue >= maxBitchness:
            return bitchmeter_captions[6]

    def check_object_has_character(obj_name):
        global char_info
        if char_info.has_key(obj_name) == True:
            return True
        return False

    def process_character_info_buttons(scene_data): #добавляем кнопки info для персонажей со свойствами
        if scene_data is None:
            return scene_data
        for obj_name in scene_data:
            if check_object_has_character(obj_name) == True:
                if scene_data[obj_name].has_key("actions"):
                    scene_data[obj_name]["actions"] = scene_data[obj_name]["actions"] + "i"
        return scene_data

    def add_char_progress(char_name, progress_value, progress_name, **kwargs):
        global char_data, char_info, gallery_mode
        duplicate = False
        if char_info.has_key(char_name) == False or gallery_mode == True:
            return
        if kwargs.has_key("duplicate") == True and kwargs["duplicate"] == True:
            duplicate = True
        else:
            if char_progress_stored.has_key(char_name) == True and char_progress_stored[char_name].has_key(progress_name) == True:
                return
        if char_progress_stored.has_key(char_name) == False:
            char_progress_stored[char_name] = {}
        if char_progress_stored[char_name].has_key(progress_name) == False:
            char_progress_stored[char_name][progress_name] = 0
        if char_info[char_name]["enabled"] == False:
            if char_info[char_name].has_key("show_caption_diabled") and char_info[char_name]["show_caption_diabled"] == True:
                notif(t__(char_info[char_name]["name_orig"]) + ". " + t__(char_info[char_name]["caption_diabled"]))
                return
#            notif(t__(char_info[char_name]["name_orig"]) + " " + t__("прогресс максимален, ждите следующих обновлений игры!"))
            return
        char_progress_stored[char_name][progress_name] = char_progress_stored[char_name][progress_name] + 1
        char_info[char_name]["current_progress"] = char_info[char_name]["current_progress"] + progress_value
        if char_info[char_name]["current_progress"] < 0:
            char_info[char_name]["current_progress"] = 0
        char_data = char_info[char_name]
        if char_info[char_name]["current_progress"] >= char_info[char_name]["max_progress"]:
#            char_info[char_name]["current_progress"] = char_info[char_name]["max_progress"]
            notif(t__(char_info[char_name]["name_orig"]) + " " + t__("прогресс перешел на следующий уровень!"))
            char_info[char_name]["current_progress"] = 0
            renpy.play("Sounds/level_up.ogg", channel="sound")
            if char_info[char_name]["uplevel_label"] != False and renpy.has_label(char_info[char_name]["uplevel_label"]) == True:
                progressFuncName = char_info[char_name]["uplevel_label"]
                renpy.call(progressFuncName)
        else:
            if progress_value > 0:
                notif(t__(char_info[char_name]["name_orig"]) + " " + t__("прогресс увеличен!"))
            else:
                if char_info[char_name]["current_progress"] > 0:
                    notif(t__(char_info[char_name]["name_orig"]) + " " + t__("прогресс понижен!"))
            if char_info[char_name]["progress_label"] != False and renpy.has_label(char_info[char_name]["progress_label"]) == True:
                progressFuncName = char_info[char_name]["progress_label"]
                renpy.call(progressFuncName)
        return


    def add_corruption(amount, progress_name):
        global char_data, corruption, corruption_places, gallery_mode
        if amount == 0 or gallery_mode == True:
            return
        duplicate = False
        if corruption_places.has_key(progress_name) == False:
            corruption_places[progress_name] = 0
        if corruption_places[progress_name] > 0:
            return
        corruption_places[progress_name] = corruption_places[progress_name] + 1
        corruption = corruption + amount
        if corruption < 0:
            corruption = 0
        if corruption > corruptionMax:
            corruption = corruptionMax

        if amount > 0:
            notif(t_("Corruption +") + str(amount))
        else:
            notif(t_("Corruption -") + str(amount))

        renpy.call("process_hooks", "corruption", "global") #процессим хуки
        return

    def monica_eated(): # Вызывается когда Моника поела
        global day, day_time, monicaEatedLastDay, monicaEatedLastDayTime
        monicaEatedLastDay = day
        monicaEatedLastDayTime = day_time
        return

    def add_money(amount):
        global money
        money = money + float(amount)
        if amount >= 0:
            notif ("+ $" + str(abs(amount)))
            renpy.play("Sounds/fx_coins.ogg", channel="sound")
        else:
            notif ("- $" + str(abs(amount)))
            renpy.play("Sounds/fx_coins.ogg", channel="sound")
        renpy.call("process_hooks", "money_change", "global") #процессим хуки
        return

#    if check_object_has_character(i) == True:
#        $ data["actions"] = data["actions"] + "i"

label bitch(amount, place=False):
    $ global bitchmeter_places
    if gallery_mode == True:
        return
    if place != False:
        if bitchmeter_places.has_key(place):
            return
        $ bitchmeter_places[place] = amount


    if bitchmeterValue > maxBitchness / 2 and amount < 0:
        $ amount *= 3
    if bitchmeterValue <= maxBitchness / 2 and amount > 0:
        $ amount *= 3

    $ bitchmeterValue += amount
    if bitchmeterValue < 0:
        $ bitchmeterValue = 0
    if bitchmeterValue > maxBitchness:
        $ bitchmeterValue = maxBitchness
    if amount > 0:
        show screen notify ("Bitchness increased!")
    else:
        show screen notify ("Bitchness decreased!")
    return

label low_corruption(req):
    $ requiredCorruption = req
    help "Not enough corruption! Required [requiredCorruption]."
    return
