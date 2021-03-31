#default bettyLocation = "none"

default bettyPantiesLog = []
default bettyPantiesCurrent = 3
default bettyPantiesCurrentList = []
define bettyPantiesList = [1, 2, 3, 4, 5]

default bettyTouchedFredDick = False
default bettyFredLandrySexPlanned = False
default bettyTouchedFredDickByTongue = False
default bettyFredLaundryHasSex = False
default bettyFredBedroomHasBlowjob = False # Бетти делала минет Фреду в спальне
default bettyFredBedroomHasSex = False # Бетти имела секс со Фредом в спальне
default bettyKissedRalphSpermCheek = False # Бетти поцеловала Ральфа в щеку после секса со Фредом в спальне
default bettyKissedRalphSpermLips = False # Бетти поцеловала Ральфа в губы после секса со Фредом в спальне
default bettyNotKissedRalphSperm = False # Бетти не стала целовать Ральфа после секса со Фредом в спальне

default bettySteveKitchenTouchedDick = False # Бетти потрогала член Стива на кухне
default bettySteveKitchenSex = False # Бетти имела секс со Стивом на кухне

default bettyInstructorSex1 = False # Бетти имела секс с инструктором на виду у Барди

default bettyFitnessToday = False

default bettyMustNotWearPanties = False

label bettyInteract1:
    if act == "l":
        mt "Это Бетти..."
        "Редкая сучка!"
        "Она следит за мной, за каждым моим шагом."
        "Мне надо быть осторожнее с ней, пока..."
        if monicaBettyPanties == True:
            mt "К тому же на мне одеты ее трусики... Ужас!!!"
        "Она еще поплатится за свое ко мне отношение!"

    if act == "t":
        if bettyLocation == "Bedroom1":
            if day_time == "day":
                call bettyDialogue1() from _call_bettyDialogue1
                return
    return

label bettyGetTodayPanties:
    if len(bettyPantiesCurrentList) > 0:
        $ bettyPantiesCurrent = bettyPantiesCurrentList.pop(0)
        $ bettyPantiesLog.insert(0, bettyPantiesCurrent)
        if bettyMustNotWearPanties == True:
            $ bettyPantiesCurrent = 0
            return
        return
    python:
        bettyPantiesCurrentList = copy.deepcopy(bettyPantiesList)
#        print bettyPantiesCurrentList
        if bettyPantiesCurrent != 0:
            idx = bettyPantiesCurrentList.index(bettyPantiesCurrent)
            bettyPantiesCurrentList.pop(idx)
#        print bettyPantiesCurrentList
        shuffle(bettyPantiesCurrentList)
#        print bettyPantiesCurrentList

        if bettyPantiesCurrent != 0:
            bettyPantiesCurrentList.append(bettyPantiesCurrent)
#        print bettyPantiesCurrentList

    call bettyGetTodayPanties() from _call_bettyGetTodayPanties
    return

label bettyProgressLevelUp1:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ questHelp("house_10", skipIfExists=True)
        if ep22_started == False:
            $ char_data["enabled"] = False
            $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
            $ char_data["show_caption_diabled"] = True
        $ move_object("Betty", "floor2")
        $ add_hook("Betty_Life_day", "Betty_Life_day1_lower", scene="global", priority=50, label="betty_level2_onetime")
    if char_data["level"] == 3:
        $ char_data["enabled"] = True
        $ char_data["caption"] = t_("Бетти хочет чтобы я носила ее сумку с вещами на фитнесс...")
        $ char_data["show_caption_diabled"] = False
        call EP22_Quests_Betty1() from _call_EP22_Quests_Betty1
#    if char_data["level"] == 4:
#        $ char_data["enabled"] = False
#        $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
#        $ char_data["show_caption_diabled"] = True
#        $ questHelp("fitness_1a", True)
#        $ char_data["caption_diabled"] = t_("Work in progress...")
#        call ep24_quests_bardie1b() from _call_ep24_quests_bardie1b


    if char_data["level"] == 5:
        if char_info["Bardie"]["level"] < 5:
            $ char_data["enabled"] = False
            $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
            $ char_data["show_caption_diabled"] = True
            return
        $ questHelp("house_15", True)
        call ep24_quests_betty5() from _call_ep24_quests_betty5
    if char_data["level"] == 6:
        $ questHelpDesc("house_desc12", False)
        $ char_data["enabled"] = False
        $ char_data["show_caption_diabled"] = False
        $ char_data["caption_diabled"] = t_("Work in progress...")
        help "Уровень Бетти максимален для этой версии игры. Ожидайте обновлений!"

        if char_info["Bardie"]["level"] >= 6:
            $ questHelp("house_16", True)

    return
