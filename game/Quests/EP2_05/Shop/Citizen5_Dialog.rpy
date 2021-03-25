# Girl2
label cit5_dialog_1:
    $ store_music()
    music Hidden_Agenda
    img 10868
    with fade
    w
    sound highheels_short_walk
    img 10869
    with fade
    m "Добрый день, Девушка."
    m "Можно к Тебе обратиться?"
    img 10870
    with diss
    cit5 "Что?"
    # Убегает
    music Groove2_85
    sound Jump1
    img 10871
    "Ой! Хи-хи"
    sound highheels_run1
    img black_screen
    with diss
    pause 2.0
    $ restore_music()
    return True

label cit5_dialog_2:
    $ store_music()
    music Hidden_Agenda
    sound highheels_short_walk
    img 10872
    with fadelong
    m "Добрый день, Девушка."
    m "Можно к Тебе обратиться?"
    cit5 "Ой!"
    music Groove2_85
    sound Jump1
    img 10873
    with diss
    m "Стой!"
    img 10874
    with diss
    cit5 "Да? Что? Хи-хи"
    img 10875
    m "У тебя есть деньги?"
    cit5 "У меня много денег, но родители не разрешают мне ходить по магазинам. Хи-хи"
    music Hidden_Agenda
    img 10876
    with fade
    m "Я никому не скажу. Купи это платье..."
    img 10877
    cit5 "Хорошо, завтра я возьму деньги и куплю его."
    img 10878
    with fade
    m "Может быть сегодня?"
    sound Jump1
    img 10879
    with diss
    w
    sound highheels_run1
    img black_screen
    with diss
    pause 2.0
    # Убегает
    $ restore_music()
    return True
label cit5_dialog_3:
    music Hidden_Agenda
    sound highheels_short_walk
    img 10880
    with fadelong
    m "Добрый день, Девушка."
    m "Можно к Тебе обратиться?"
    img 10881
    with fade
    cit5 "Да..."
    img 10882
    with fade
    m "Ну что, ты взяла с собой деньги сегодня?"
    img 10883
    with fade
    cit5 "Да..."
    img 10884
    with fade
    m "Покажи их..."
    img 10885
    with diss
    w
    img 10886
    with fade
    w
    sound Jump1
    img 10887
    with diss
    # Девушка задирает юбку и показывает киску
    w
    music Groove2_85
    img 10888
    m "ЭТО ЧТО ЕЩЕ?!"
    img 10889
    with fade
    w
    img 10890
    with diss
    cit5 "Покажи свою киску и я куплю это платье..."

    music Power_Bots_Loop
    img 10891
    with fade
    m "ЧТООООО?!!!"
    cit5 "Твою киску!"
    cit5 "Покажи ее и я куплю это платье..."
    music Groove2_85
    img 10892
    with fade
    mt "Эта девочка что, ненормальная?!"
    mt "Она думает что Моника Бакфетт будет показывать ей свои интимные места в какой-то примерочной?!"
    mt "Да, у меня временные проблемы, но я не настолько опустилась, чтобы делать это!"
    music Hidden_Agenda
    img 10893
    with fade
    mt "..."
    mt "С другой стороны, никто здесь не знает кто я такая."
    mt "И, если эта девочка купит платье, то этот кошмар с ненормальными клиентами закончится."
    mt "Я получу другое платье, как договорилась с продавщицей и смогу пойти к Стиву."
    mt "Я буду выглядеть красиво!"
    # corruption +5 req 120
    $ menu_corruption = [120]
    menu:
        "Показать девочке что она просит.":
            pass
        "Уйти.":
            $ monicaSellingDressRefuseLastDay = day
            return False

    music Groove2_85
    img 10894
    with fade
    mt "Никого рядом нет..."
    img 10895
    with diss
    m "Хорошо, я сделаю это. Пока никто не видит."
    $ add_corruption(5, "cit5_dialog_3")
    # Моника показывает
    sound snd_fabric1
    img 10896
    with fadelong
    w
    img 10897
    with diss
    w
    img 10898
    with diss
    w
    img 10899
    with diss
    w
    img 10900
    with diss
    w
    img 10901
    with diss
    w
    img 10902
    with diss
    w
    sound Jump1
    music stop
    img 10903
    with fade
    cit5 "Я пошутила! Хи-хи!"
    sound highheels_run1
    img black_screen
    with diss
    pause 2.0
    music Power_Bots_Loop
    img 10904
    mt "Вот дьявол!"
    mt "О чем я только думала?! Откуда у этой дуры деньги на платье?!"
    mt "Моника, ты уже совсем сходишь с ума."
    mt "Как ты могла показать что-то без гарантий?!"
    mt "Хотя какие к черту гарантии?! С какой стати я вообще что-то кому-то показала?!"
    mt "Я - Моника Бакфетт!"
    return True
