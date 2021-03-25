
label cloth_shop_refuse1:
    $ store_music()
    hide screen Rain
    hide screen Rain_overlay
    music Power_Bots_Loop
    img 3042
    with fade
    mt "Здесь снова полно народа!"
    "Но ведь здесь никого не было, когда я приходила сюда с Диком!"
    "Почему так???"
    img 3043
    "Мне надо скорее убираться отсюда, пока меня не заметили!"
    "Они сразу позовут эту продавщицу."
    "Увидев меня в таком виде, она сразу вызовет полицию."
    $ restore_music()
    call refresh_scene_fade() from _call_refresh_scene_fade_26
    return
