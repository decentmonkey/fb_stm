label afterJailHouse_dialogue1a(o,d): #
    mt "Мне надо сначала переодеться, а то хозяева будут ругаться!"
    return
label afterJailHouse_dialogue1b: #
#    help "В доме стали доступны новые локации! Гостиная, спальня для гостей и комната Барди."
    help "В доме стали доступны новые локации! Гостиная и спальня для гостей."
    return


label afterJailHouse_dialogue2: #bedroomsecond
    mt "Я сюда очень давно не заходила."
    "Эта спальня, конечно, не сравнится с моей, но меня она сейчас вполне устроит..."
    return
label afterJailHouse_dialogue3: #bedroombardie
    mt "Раньше здесь была моя гардеробная."
    "Они переделали мою гардеробную под комнату этого оболтуса!!!"
    return
label afterJailHouse_dialogue4: #livingroom
    mt "Не помню когда я здесь была в последний раз."
    "Кажется когда запретила мужу приводить гостей."
    return
label afterJailHouse_dialogue5: #bedroom_betty
    return
label afterJailHouse_dialogue6: #kitchen
    return

label afterJailHouse_dialogue8: #bed
    if cloth != "Governess":
        mt "Мне надо переодеться сначала."
        return
    if monicaEated == False:
        mt "Перед сном надо что-то поесть."
        "Я уже нормально не ела целую вечность!!!"
        return
    if bathTaken == False:
        mt "Хоть меня дождь хорошенько помыл, я хотела бы освежиться перед сном!"
        return
#    call afterJailHouse_dialogue17() from _call_afterJailHouse_dialogue17
    return


label afterJailHouse_dialogue10: #бетти запретила
    if lastSceneName != "bathroom_shower":
        mt "Бетти запретила мне заходить сюда."
    return


label afterJailHouse_dialogue15:
    if lastSceneName != "kitchen2":
        mt "Бетти запретила мне появляться на кухне... Так что в этом доме я остаюсь без еды..."
    return
label afterJailHouse_dialogue15b:
    if lastSceneName != "kitchen":
        mt "Бетти запретила мне появляться на кухне... Так что в этом доме я остаюсь без еды..."
    return
label afterJailHouse_dialogue15a:
    mt "Бетти запретила мне притрагиваться к чему-либо..."
    "Мне лучше уйти отсюда скорее, пока она не заметила меня!"
    call change_scene("floor1") from _call_change_scene_127
    return

label afterJailHouse_dialogue16a:
    if lastSceneName != "bedroom1" and monicaCleaningInProgress != True:
        mt "Эту спальню заняли новые хозяева. Мне нежелательно сюда заходить..."
    return


label afterJailHouse_dialogue20:
    img black_screen
    with Dissolve(1.0)
    help "Вы можете безопасно сохраниться в этой локации для того, чтобы использовать сохранение в Эпизоде 2."
    img 3374
    with fadelong
    mt "Вот где жила Юлия..."
    img 3375
    with fade
    mt "Узкая темная каморка, без окон."
    mt "В то время пока я нежилась в постели из шелка..."
    img 3376
    with fade
    mt "..."
    "Там на столике что-то лежит..."

    $ miniMapEnabledOnly = ["none"]


    $ add_objective("take_journal", t_("Там на столике что-то лежит..."), c_white, 15)

#    call refresh_scene_fade()
    return

label afterJailHouse_dialogue21:
    $ basementBedroomJournal = False

#    sound snd_take_paper
    img 3378
    with fadelong
    mt "Это мой журнал."
    "Я на обложке."
    "Зачем он Юлии?"
    img 3377
    with fade
    mt "Наверное она смотрела на него и думала про меня."
    "Про ту кто живет наверху..."
    "..."
    img 3379
    with fade
    mt "Моника."
    "Что с тобой стало?"
    "..."
    "Не могу сейчас ни о чем думать."
    "Главное что я под крышей над головой, а не в ледяной камере или еще где похуже."
    "..."
    "Надо раздеться и ложиться спать..."

    $ remove_objective("take_journal")
    $ add_inventory("journal", 1, True)
    $ basementBedroomStage = 1
    $ autorun_to_object("basement_bedroom1", "afterJailHouse_dialogue22")

    call change_scene("basement_bedroom2", "Fade", False) from _call_change_scene_128
    return

label afterJailHouse_dialogue22:
    mt "В этот старый шкаф можно повесить одежду..."
    "Если это можно назвать одеждой..."
    return
