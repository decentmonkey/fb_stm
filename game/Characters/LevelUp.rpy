label biffProgressLevelUp:
    call biffProgressLevelUp1() from _call_biffProgressLevelUp1
    return
label bettyProgressLevelUp:
    call bettyProgressLevelUp1() from _call_bettyProgressLevelUp1
    return

label bettyProgressForward:
    return

label bardieProgressLevelUp:
    call bardieProgressLevelUp1() from _call_bardieProgressLevelUp1
    return

label alexPhotographProgressLevelUp:
    call alexPhotographProgressLevelUp1() from _call_alexPhotographProgressLevelUp1
    return

label cashierProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1

    return

label driverProgressLevelUp:
    return

label gasSalesWomanProgressLevelUp:
    return

label janeProgressLevelUp:
    return

label marcusProgressLevelUp:
    return

label melanieProgressLevelUp:
    return

label mommyProgressLevelUp:
    return

label neighborProgressLevelUp:
    return

label perryProgressLevelUp:
    return

label ralphProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = t_("Ральф привык к регулярному сексу с гувернанткой...")
    return

label rebeccaProgressLevelUp:
    return

label receptionGirlProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1

    return

label shawarma_TraderProgressLevelUp:
    return

label stephanieProgressLevelUp:
    return

label steveProgressLevelUp:
    return

label tiffanyProgressLevelUp:
    return
