#default ralphLocation = "none"
#default ralphStage = 0
#default ralphAskedAboutPayment = False

label ralphInteract1:
    if act == "l":
        mt "Это Ральф."
        "Подкаблучник."
        "Бетти неплохо выдрессировала его, надо отдать должное ей."
        "Но мужчины такими и должны быть."
        "Мы, женщины, выше мужчин и они должны это понимать!"
        return
    if act == "t":
        if cloth_type != "Governess":
            mt "Мне надо переодеться сначала."
            "Не стоит портить впечатление у Ральфа."
            if monicaBitch == True:
                "Я не хочу оставаться один на один с этой сучкой Бетти."
            else:
                "Я не хочу оставаться один на один с Бетти."
            return
        call ralphDialogue1() from _call_ralphDialogue1
        call refresh_scene_fade() from _call_refresh_scene_fade_11
        return
    return
