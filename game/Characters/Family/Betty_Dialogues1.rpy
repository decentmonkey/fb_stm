label bettyDialogue1:
    #render+
    #Моника говорит с Бетти в спальне днем (у зеркала)
    $ store_music()
    music Groove2_85
    img 5801
#    imgr Dial_Betty_1
    with fadelong
    betty "Я буду следить за тем как ты работаешь."
    $ restore_music()
#    music casualMusic
    call refresh_scene_fade() from _call_refresh_scene_fade_40
    return

label bettyDialogue2:
    # Спальня вечер
    mt "Бетти отдыхает..."
    "Мне лучше уйти отсюда пока она на меня не наорала."
    if monicaBitch == True:
        "Сучка..."
    return

label bettyDialogue3:
    mt "Мне лучше не подходить к Бетти в таком виде..."
    "Она и так все время называет меня шлюхой..."
    if monicaBitch == True:
        "Сучка..."
    return
