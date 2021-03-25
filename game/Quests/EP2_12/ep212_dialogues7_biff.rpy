#call ep212_dialogues7_biff1() # нога на столе
#call ep212_dialogues7_biff2() # сидит на столе


label ep212_dialogues7_biff1: #Поставить на стол одну ногу.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 22908
    with fade
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
    img 22909
    with diss
    mt "Сволочь!"
    music Loved_Up
    img 23738
    with fade
    w
    sound grabbing7
    img 23739 # звук ноги на стол (без каблуков)
    with diss
    w
    img 23740
    with fade
    m "Так тебя устроит, Биф?"
    img 23741
    with diss
    biff "Да, цыпочка! Это хоть что-то новенькое..."
    img 23742
    with fade
    biff "Надеюсь, в следующий раз цыпочка придумает еще что-нибудь интересное..."
    music Power_Bots_Loop
    img 22920
    with fade
    m "..."
    mt "Ненавижу этого придурка!"
    return

label ep212_dialogues7_biff2: #Сесть на стол лицом к Бифу, широко раздвинув ноги.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 22908
    with fade
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
    img 22909
    with diss
    mt "Сволочь!"
    music Loved_Up
    img 23743
    with fade
    w
    img 23744
    with diss
    w
    sound Jump1
    img 23745 # запрыгивает резко
    with diss
    w
    img 23746
    with fade
    biff "О! Цыпочка!"
    biff "Какая ты горячая! Ты даже напугала папочку!"
    biff "Что дальше?"
    img 23747
    with diss
    m "Ничего, Биф! Этого достаточно!"
    img 23748
    with fade
    biff "Нет, цыпочка!"
    biff "Хорошая цыпочка должна дать папочке хорошенько рассмотреть себя!"
    img 23749
    with diss
    m "Нет!!!"
    img 23750
    with fade
    biff "Плохая цыпочка снимется завтра с членом во рту и закончит контракт на серию фотосессий!"
    img 23751
    with diss
    biff "И отправится назад сосать члены за $ 20!"
    biff "А ее место займет другая цыпочка!"
    img 23752
    with fade
    m "!!!"
    biff "Так какая ты цыпочка?"
    img 23753
    with diss
    menu:
        "Я хорошая цыпочка...":
            pass
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 23754
    with fade
    m "Я хорошая цыпочка..."
    img 23755
    with diss
    biff "Давай, цыпочка, раздвинь широко свои ножки!"
    biff "Покажи как ты любишь папочку!"
    img 23756
    with fade
    m "Биф, тебе и так прекрасно видно все!"
    img 23757
    with diss
    biff "Если цыпочка не любит папочку, то она вылетит с этой работы прямо сейчас!!!"
    img 23758
    with diss
    m "!!!"
    menu:
        "Я хорошая цыпочка...":
            pass
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 23759
    with fade
    m "Я хорошая цыпочка..."
    img 23760
    with diss
    m "Я люблю папочку..."
    img 23761
    with fade
    biff "Ха-ха!!!"
    img 23762
    with diss
    biff "Вот так-то лучше!"
    img 23763
    with fade
    biff "Надеюсь, в следующий раз цыпочка придумает еще что-нибудь интересное..."
    img 23764
    with diss
    m "!!!"
    music Power_Bots_Loop
    img 22920
    with fade
    m "..."
    mt "Ненавижу этого придурка!"

    return
















#
