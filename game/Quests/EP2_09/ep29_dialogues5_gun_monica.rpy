# квест с колледжем у Моники должен быть завершен
# сцена включается автоматически, когда Моника после уборки в доме заходит в свою спальню в подвале
label ep29_dialogues5_gun_monica_1:
    # Моника заходит в свою комнату в подвале, у нее на кровати валяется Барди
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 15806
    with fadelong
    w
    img 15807
    with diss
    mt "Снова этой малявке что-то нужно от меня!"
    mt "Боже! Как же он меня достал!"
    mt "!!!"
    mt "Хорошо, хоть своего друга сюда не притащил..."
    # Моника подходит к кровати, смотрит на него недовольно
    sound highheels_short_walk
    img 15808
    with fade
    m "Что тебе нужно?"
    # Барди со своей улыбочкой
    music Sneaky_Snitch
    img 15809
    with diss
    bardie "Ничего, гувернантка."
    bardie "Давно у тебя не был... Решил вот зайти..."
    img 15810
    with diss
    bardie "Заодно проверю, насколько гувернантка хорошая."
    bardie "Соблюдает ли гувернантка правила этого дома?"
    # Барди садится на кровати, спустив ноги на пол
    # рядом с его ногой под кроватью виднеется пробка, ни Барди, ни Моника ее не видят
    music Groove2_85
    img 15811
    with fade
    mt "Ненавижу эту малявку!"
    mt "Как бы сделать так, чтобы он поскорее убрался отсюда?!"
    mt "!!!"
    # Моника сквозь зубы
    img 15812
    with diss
    m "Я хорошая гувернантка и соблюдаю правила дома..."
    music Sneaky_Snitch
    img 15813
    with fade
    bardie "Покажи мне, как ты соблюдаешь правила."
    bardie "Поднимай юбку, гувернантка!"
    music Groove2_85
    img 15814
    with diss
    m "..."
    if monicaUnder != "Nude":
        img 15815
        with diss
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        img 15816
        with fade
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        music stop
        img black_screen
        with diss
        sound highheels_run2
        pause 2.0
        return 0
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать. (Пропуск квеста мести)":
            img 15816
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            img 15817
            with diss
            w
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 2.0
            return 1
    # Моника поднимает юбку, она без трусиков
    # Барди доволен
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15818
    with fadelong
    w
    img 15819
    with diss
    bardie "Гувернантка хорошая. Гувернантка слушается приказов хозяина."
    img 15820
    with fade
    m "..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Sneaky_Snitch
    img 15821
    with fadelong
    bardie "Хозяин будет доволен своей гувернанткой еще больше, если она..."
    bardie "Кое-что сделает для него..." # с мерзкой улыбочкой
    # Моника смотрит на него ненавидящим взглядом
    music Groove2_85
    img 15822
    with fade
    m "!!!"
    m "В колледж я больше не пойду ни за что!"
    # Барди смеется
    music Sneaky_Snitch
    img 15823
    with diss
    bardie "Гувернантке не понравилось договариваться с мистером Эдвардсом?"
    bardie "Странно. А Бетти была вполне довольна 'переговорами' с ним."
    img 15824
    with diss
    m "!!!"
    img 15825
    with fade
    bardie "Гувернантка хорошо уладила вопрос с учителем."
    bardie "У Эрика пока что никаких проблем в колледже нет."
    music Groove2_85
    img 15826
    with diss
    mt "Это ненадолго..."
    mt "В следующий раз сами будут 'договариваться' с учителем..."
    img 15827
    with fade
    m "Тогда что ты хотел?"
    music Sneaky_Snitch
    img 15828
    with diss
    bardie "Гувернантка, мне надоел тот журнал с твоей фотографией на обложке."
    bardie "Он стал весь испачканный и мою гувернантку Монику Бакфетт на фото теперь плохо видно."
    # Моника удивленно смотрит на него
    music Groove2_85
    img 15830
    with fade
    mt "Фу!"
    mt "Не хочу даже думать о том, в чем он испачкал мой журнал!"
    img 15829
    with diss
    m "..."
    m "А я здесь причем?"
    music Sneaky_Snitch
    img 15831
    with fade
    bardie "Если гувернантка хочет, чтобы хозяин был ею доволен..."
    bardie "То она должна принести ему журнал с другой ее фотографией!"
    music Groove2_85
    img 15832
    with diss
    m "У меня нет других журналов с моими фотографиями!"
    m "!!!"
    # Барди ехидно
    img 15833
    with fade
    bardie "Ты уверена, гувернантка?"
    bardie "Интересно, а куда ты бегаешь в красном платье почти каждый день?"
    img 15834
    with diss
    m "Не твое дело!"
    img 15835
    with diss
    bardie "..."
    bardie "Может, мне стоит спросить об этом отца или Бетти?"
    # тут Барди задеват ногой пробку под кроватью, удивляется и наклоняется (немного)
    img 15836
    with fade
    w
    sound Jump2
    img  15837
    w
    music Marty_Gots_a_Plan
    img 15838
    with diss
    sound vjuh2
    bardie "Гувернантка, что ты там прячешь под кроватью?"
    # Моника замечает пробку, пугается
    music Pyro_Flow
    img 15839
    with fade
    mt "Анальная пробка!"
    mt "!!!"
    mt "Сейчас малявка увидит ее!"
    img 15840
    with diss
    mt "И придумает какое-нибудь извращение с ней!"
    mt "Или, что еще хуже, заберет ее у меня!"
    music Master_Disorder
    mt "Если Маркус узнает, что я не послушалась его приказа и не хранила пробку..."
    mt "!!!"
    # Моника поспешно говорит Барди, пока тот не рассмотрел, что он там задел под кроватью
    music Groove2_85
    img 15841
    with fade
    m "Ничего я не прячу!"
    m "Там мои туфли стоят!"
    m "Я... Я их надеваю к красному платью!"
    m "!!!"
    # Барди продолжает попытки посмотреть под кровать
    sound Jump1
    img 15842
    with diss
    m "Не говори никому, что ты видел меня в красном платье..."
    m "..."
    m "Я хорошая гувернантка..."
    m "Я тебе принесу другой номер журнала с моей фотографией."
    # Барди перестает рассматривать, что там под кроватью, смотрит довольный на Монику
    music stop
    img black_screen
    with diss
    pause 1.0
    music Sneaky_Snitch
    img 15843
    with fadelong
    bardie "Хорошая гувернантка! Хозяин ею доволен!"
    bardie "Хозяин будет ждать новый журнал..."
    bardie "С нетерпением!"
    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.5
    # Барди самодовольно улыбается и уходит
    return 2

# после ухода Барди Моника стоит возле своей кровати
label ep29_dialogues5_gun_monica_2:
    # Моника переживает
    music Groove2_85
    img 15844
    with fadelong
    mt "Боюсь себе представить что было бы, если бы эта малявка нашел пробку!"
    mt "Или забрал бы ее, или заставил бы меня ходить с этой пробкой!"
    mt "И еще проверял бы, слушается ли гувернантка его приказа..."
    mt "Фу, какой кошмар!"
    mt "Хорошо, что он ее не увидел."
    # недовольно
    img 15845
    with fade
    mt "..."
    mt "Теперь придется принести ему другой журнал..."
    mt "Но лучше уж так, чем уборка с пробкой в моей попе."
    mt "..."
    # задумчиво
    img 15846
    with diss
    mt "Пробку надо куда-нибудь спрятать, чтобы Барди не смог ее случайно увидеть."
    mt "Только куда? Комната у меня не закрывается на ключ."
    mt "Малявка в любой момент, когда меня нет, может зайти и обыскать мою комнату."
    # смотрит на шкаф
    img 15847
    with fade
    mt "И в шкафу ее тоже нет смысла прятать... Он не закрыается на замок."
    # Моника задумчиво оглядывается
    img 15848
    with diss
    mt "..."
    # тут ее взгляд падает на шкафчик возле кровати
    img 15849
    with fade
    mt "Хм..."
    # Моника подходит, дергает этот шкафчик, он закрыт
    img 15850
    with diss
    sound snd_door_locked1
    w
    img 15851
    with fade
    mt "Это было бы идеальное место..."
    mt "Где может быть ключ от этого шкафчика?"
    mt "???"
    # оглядывается
    img 15852
    with diss
    mt "Уверена, что где-то недалеко отсюда..."
    mt "..."
    # у Моники в заданиях появляется "Найти ключ от прикроватной тумбочки"
#    $ log1 = t_("Найти ключ от прикроватной тумбочки")
    return

label ep29_dialogues5_gun_monica_a:
    mt "Где может быть ключ от этого шкафчика?"
    return

# мысли Моники
# не рендерить!!!

label ep29_dialogues5_gun_monica_3:
    # если хочет переместиться в любую локацию дома, кроме прачечной, подвала и бассейна
    mt "Мне нужно срочно найти ключ от шкафчика."
    mt "Барди в любой момент может вернуться и обнаружить анальную пробку!"
    mt "Ключ должен быть где-то недалеко..."
    return

label ep29_dialogues5_gun_monica_4:
    # ищет ключ у себя в комнате под кроватью
    mt "Под кроватью его точно нет. Я бы заметила его, когда прятала пробку."
    return

label ep29_dialogues5_gun_monica_4a:
    img scene_Basement_Bedroom1
    with fadelong
    menu:
        "К черту этот дурацкий запертый ящик. Просто запихаю пробку подальше под кровать. (пропуск квеста мести)":
            return False
        "Надо поискать ключ еще раз...":
            return True
    return


label ep29_dialogues5_gun_monica_5:
    # ищет ключ у себя в комнате в шкафу
    if act=="l":
        return
    mt "В шкафу ключа нет. Там только мои вещи и больше ничего."
    return False

label ep29_dialogues5_gun_monica_6:
    # ищет ключ у бассейна
    mt "Здесь я бы заметила ключ уже давно."
    mt "Нужно поискать еще где-нибудь..."
    return

label ep29_dialogues5_gun_monica_7:
    # выходит в темный коридор подвала
    mt "Думаю, нужно вернуться и поискать ключ в своей комнате или в прачечной."
    $ remove_hook(label="ep29_revenge_quest1_comment2")
    return


label ep29_dialogues5_gun_monica_8:
    # заходит в прачечную
    mt "Вполне возможно, что ключ где-то здесь..."
    return

label ep29_dialogues5_gun_monica_9:
    # ищет по шкафчикам
    mt "В этом шкафчике только трусики Бетти."
    return
label ep29_dialogues5_gun_monica_9b:
    mt "В этом нет ключа."
    return
label ep29_dialogues5_gun_monica_9b2:
    mt "Здесь тоже пусто."
    return
label ep29_dialogues5_gun_monica_9b3:
    # поворачивается, смотрит в сторону гладильной доски
    mt "Где же этот чертов ключ?! Может, там?"
    # ищет у гладильной доски
    img 22895
    with fade
    mt "Черт! В этой прачечной можно найти все что угодно, кроме ключа!"
    return
    # смотрит на стиральную машинку
label ep29_dialogues5_gun_monica_9b4:
    mt "Может, он внутри стиральной машинки?"
    # подходит, приседает, чтобы открыть ее и замечает ключ под шкафчиками на полу
    return
label ep29_dialogues5_gun_monica_9b5:
    mt "Что там?"
    mt "Что-то блестит..."
    return
label ep29_dialogues5_gun_monica_9b6:
    mt "Неужели ключ?! Ну наконец-то!"
    mt "!!!"
    mt "Надеюсь, что это тот ключ, который мне нужен."
    mt "Нужно скорее проверить!"
    return

# комната Моники в подвале, после того, как нашла ключ
label ep29_dialogues5_gun_monica_10:
    # Моника заходит в комнату, достает пробку из-под кровати
    # подходит к шкафчику возле кровати, вставляет ключ в замок
#    music stop
#    img black_screen
#    with diss
#    sound metal_slide
#    pause 2.0
#    sound2 snd_door_open1
#    pause 1.0
#    music Groove2_85
    music Marty_Gots_a_Plan
    img 22887
    with fadelong
    mt "Отлично! Ключ подошел!"
#    mt "!!!"
    # с улыбочкой
    mt "Интересно, что же там хранила Юлия?"
    mt "???"
    # делает один оборот ключа с скрипучим звуком, дергает шкафчик, он не открывается
    # делает еще один оборот ключа, дергает шкафчик
    # шкафчик приоткрывается чуть-чуть
    # Моника с заинтересованным видом тянет шкафчик на себя, открывая его
    music Gearhead
    img 22888
    with fade
    mt "!!!"
    img 22889
    with hpunch
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    # переход на сцену
    return

label ep29_dialogues5_gun_monica_10b:
    help "Внимание! Все прочие события станут неактивными!"
    help "Вы действительно хотите продолжить?"
    menu:
        "Взять пистолет.":
            pass
        "Продолжить игру.":
            return False
    music vendetta
    img black_screen
    with diss
    $ renpy.pause (2.0, hard=True)
    img 22890
    with fadelong
    $ renpy.pause (4.0, hard=True)
    img 22891
    with fadelong
    $ renpy.pause (5.0, hard=True)
    img 22892
    with fadelong
    $ renpy.pause (6.0, hard=True)
    img 22893
    with fadelong
    $ renpy.pause (5.0, hard=True)
    img 22894
    with fadelong
    $ renpy.pause (3.0, hard=True)
    img 22905
    with diss
    pause 0.5
#    scene black
#    image videov_Monica_TakeGun1 = Movie(play="video/v_Monica_TakeGun1.mkv", fps=25, loop=False, image="/Overlays/black_screen.jpg")
#    show videov_Monica_TakeGun1
#    pause 1.8
    stop music
    sound snd_cinematic_impact

    img black_screen
#    pause 2.0
    $ renpy.pause(1.5, hard=True)
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack("FASHION BUSINESS") from _rcall_textonblack_13
    img black_screen
    with Dissolve(2.0)
    return


    img black_screen
#    pause 2.0
    $ renpy.pause(4.0, hard=True)
    music Continue_Life
    img black_screen
    with Dissolve(2.0)
    call textonblack("TO BE CONTINUED IN THE NEXT UPDATE") from _call_textonblack_46
    img black_screen
    with Dissolve(2.0)
    $ renpy.pause(2.0, hard=True)
    img black_screen
    with Dissolve(0.5)
    img Patreon_Game_Logo
    with Dissolve(0.7)
    $ renpy.pause(1.0, hard=True)
##    pause 4.0
    $ renpy.pause(4.0, hard=True)
    img black_screen
    with Dissolve(0.7)
    $ renpy.pause(3.0, hard=True)
##    pause 30.0
##    music stop
##    pause 1.0
    call credits() from _call_credits_2
    $ MainMenu(confirm=False)()
    # заглядывает и видит там пистолет
    # тревожная музыка
    # занавес
    return True

# + отрывок музыки из "Убить Билла"
