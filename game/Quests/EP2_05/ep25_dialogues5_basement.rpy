label ep25_dialgues5_basement1:
    # Моника пробует одеть платье с трусиками
    $ store_music()
    music Groove2_85
    sound snd_fabric1
    img 11731
    with fade
    w
    img 11732
    with diss
    w
    img 11733
    with diss
    w
    img 11734
    with diss
    mt "Дьявол!"
    img 11735
    mt "Под это платье мои трусики не одеть!"

    img 11736
    with fade
    mt "Что же делать?"
    mt "Не буду же я ходить по улице в трусиках Бетти!"
    img 11737
    mt "..."
    sound snd_fabric1
    img 11738
    with fadelong
    mt "Буду ходить пока без трусиков!"
    img 11739
    with diss
    mt "Ничего страшного!"
    img 11740
    with fade
    mt "Я ведь не собираюсь задирать платье нигде!"
    mt "Никто никогда не увидит что под ним!"
    $ restore_music()
    return

label ep25_dialgues5_basement2:
    # Моника раздевает платье перед тем как прилечь отдохнуть
    mt "Мне стоит снять это платье. Я не хочу его мять. Другого у меня нет!"
    return
