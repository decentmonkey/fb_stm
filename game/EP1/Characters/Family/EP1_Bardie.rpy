default bardieLocation = "none"
default monicaBardieOffended1 = False

label EP1_bardieInteract1(obj_name, obj_data):
    if act == "l":
        mt "Этот маленький оболтус меня бесит!"
        return
    if act == "t":
        if bardieLocation == "BedroomBardie":
            call EP1_bardieDialogue1()
            return

    if bardieLocation == "Floor1" and act == "w":
        call EP1_change_scene("floor1_fountain", "Fade", "snd_fountain")


    return
