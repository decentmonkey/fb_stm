define wardrobeBasementWhoreTakeFlag = False

label wardrobeBasement_EP1:
    img 3368
    with fadelong
    mt "Что мне одеть?"
    menu:
        "Одежда шлюхи.":
            $ cloth = "Whore"
            $ cloth_type = "Whore"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
            $ renpy.pause(0.5)

            $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue1_whore_EP1")

        "Униформа гувернантки.":
            $ cloth = "Governess"
            $ cloth_type = "Governess"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            img 3370
            with fadelong
            mt "Кошмарная униформа."
            "Я никогда себя не представляла в этом..."
        "Оставить трусики Юлии.":
            $ cloth = "GovernessPants"
            $ cloth_type = "Nude"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            $ autorun_to_object("basement_bedroom1", "wardrobeBasement_dialogue2_pants_EP1")

        "Снять все.":
            $ cloth = "Nude"
            $ cloth_type = "Nude"
            sound snd_fabric1
            img black_screen
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            img 3369
            with fadelong
            mt "Какой ужас..."

    call refresh_scene_fade() from _call_refresh_scene_fade_82
    return

label wardrobeBasement_dialogue1_whore_EP1:
    if wardrobeBasementWhoreTakeFlag == True:
        mt "Никогда не представляла себя в этом..."
        "Это просто ужас..."
    else:
        mt "Я не могла подумать, когда увидела эти тряпки в хостеле, что мне придется носить их."
        "Вместо моего красивого платья... (хмык)"
    $ wardrobeBasementWhoreTakeFlag = True
    return
label wardrobeBasement_dialogue2_pants_EP1:
    mt "Это не мои трусики..."
    "И мне не комфортно их носить..."
    "Но это лучше чем вообще без них..."
    "(хмык)"
    return
