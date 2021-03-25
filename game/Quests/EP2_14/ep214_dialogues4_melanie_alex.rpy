default melanieAlexFirstDate1 = False  # Мелани предложила Алексу жить вместе
default melanieAlexFirstDate2 = False  # Мелани переоделась для Алекса в наряд, который выбрала Виктория
default melanieAlexFirstDate3 = False  # Мелани и Алекс занимались сексом перед камерой

#call ep214_dialogues4_melanie_alex_1() # разговор с Викторией у Мелани дома
#call ep214_dialogues4_melanie_alex_2() # свидание с Алексом

default melanieAlexFirstDate_cumzone = 0

# апартаменты Мелани
label ep214_dialogues4_melanie_alex_1:
    # Виктория с Мелани вдвоем, Мелани в своем домашнем пеньюаре
    # Виктория стоит, собираясь уходить
    # Мелани сидит на диване
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_57
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 18840
    victoria "Подружка Мелани, ты же помнишь что нужно делать?"
    melanie "Помню..."
    victoria "Позвони Алексу. Спроси, он скоро придет?"
    imgf 18841
    melanie "Я ему уже звонила."
    melanie "Он сказал, что скоро будет."
    # Виктория насмешливо
    imgd 18842
    victoria "Подружка, ты же хочешь, чтобы я осталась и посмотрела?"
    # Мелани зло на нее смотрит
    music Master_Disorder
    imgd 18843
    melanie "..."
    music Groove2_85
    imgf 18844
    victoria "Я не слышу ответа, подружка Мелани..."
    imgd 18845
    melanie "Да!"
    sound highheels_short_walk
    imgf 18846
    victoria "Что 'да'? Скажи, я хочу это слышать."
    music Master_Disorder
    imgd 18847
    melanie "Я хочу, чтобы ты осталась... Подружка..."
    imgf 18848
    w
    music Groove2_85
    imgd 18849
    sound snd_woman_laugh3
    victoria "Я бы с удовольствием осталась и помогла тебе, подружка..."
    victoria "Но я не хочу смущать Алекса."
    # Виктория хихикает
    imgf 18850
    victoria "Ладно, мне нужно идти."
    victoria "Не нужно, чтобы Алекс знал, что я тебе помогаю, подружка."
    victoria "Ты помнишь, что ты должна будешь надеть и что должна будешь сказать при этом Алексу?"
    melanie "Помню..."
    victoria "Кстати, я чуть не забыла."
    # лезет в сумочку, достает оттуда камеру
    imgd 18851
    victoria "Если я не хочу смущать Алекса, не значит, что я не хочу посмотреть..."
    # Виктория оставляет камеру на столе
    # Мелани в недоумении смотрит на нее
    melanie "Может, лучше спрятать ее?"
    victoria "Нет, подружка. Камера будет стоять здесь."
    imgf 18852
    melanie "А что мне сказать Алексу, когда он спросит про эту камеру?"
    imgd 18853
    victoria "Подружка, ты же умная."
    victoria "Ты не можешь сама придумать, что сказать Алексу?"
    music Master_Disorder
    imgd 18854
    melanie "..."
    music Groove2_85
    imgf 18855
    victoria "Хорошо... Я тебе помогу."
    victoria "Скажи Алексу, что ты любишь записывать все на камеру..."
    victoria "А потом выкладывать это в интернет."
    # Мелани в шоке
    music stop
    sound plastinka1b
    img 18856 hpunch
    melanie "?!"
    melanie "?!?!!"
    melanie "?!?!!??!?"
    music Groove2_85
    imgf 18857
    sound snd_woman_laugh3
    victoria "Я пошутила."
    # Виктория хихикает
    imgd 18858
    victoria "Ты доверяешь своей подружке смотреть это и решать, выкладывать это в интернет или нет."
    victoria "Ведь это так?"
    # Мелани все еще шоке
    melanie "Да, я доверяю тебе..."
    # Виктория пристально смотрит на Мелани
    imgf 18859
    victoria "Кстати, подружка..."
    victoria "Ко мне недавно заходили полицейские от мистера Маркуса."
    # Мелани испуганно смотрит на нее
    music Master_Disorder
    img 18860 vpunch
    melanie "!!!"
    melanie "!!!!!!"
    melanie "!!!!!!!!!"
    imgd 18861
    victoria "Они спрашивали про Миссис Бакфетт и ее ближайшее окружение."
    victoria "Я собралась им рассказать про тебя..."
    melanie "!!!"
    music Groove2_85
    imgd 18862
    victoria "Но потом вспомнила, что вы мои подружки и сказала, что ничего не знаю."
    victoria "Они меня попросили сообщить им, если вдруг мне что-то станет известно..."
    # Виктория подходит к двери
    sound highheels_short_walk
    imgf 18863
    victoria "Помни, подружка."
    victoria "Ты не должна прятаться от камеры."
    imgd 18864
    victoria "Я должна постоянно видеть подружку в кадре."
    victoria "Алекс останется жить у подружки сегодня и у вас обязательно сегодня должен быть секс."
    # Виктория уходит, Мелани задумчиво смотрит на камеру
    fadeblack
    sound highheels_short_walk
    sound2 snd_door_close1
    pause 1.5
    music Master_Disorder
    imgfl 18865
    w
    imgf 18866
    melanie "..."
    return


# апартаменты Мелани
label ep214_dialogues4_melanie_alex_2:
    # Мелани все также задумчиво сидит на диване
    # стук в дверь
    # Мелани идет к двери
    # затемнение, дверь открывается
    # заходит Алекс
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Некоторое время спустя...")) from _rcall_textonblack_58
    scene black_screen
    with Dissolve(1)
    music Master_Disorder
    imgfl 18867
    sound snd_door_knock
    w
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    pause 1.0
    music ZigZag
    imgf 18868
    alex_photograph "Мелани, привет."
    # Алекс напряжен, Мелани не глядя на него говорит
    imgd 18869
    melanie "Привет, Алекс."
    melanie "Проходи."
    # Мелани идет к дивану, садится
    # Алекс садится в кресло напротив
    sound highheels_short_walk
    imgf 18870
    w
    fadeblack
    sound man_steps
    pause 1.5
    music Groove2_85
    imgfl 18871
    w
    imgf 18872
    melanie "..."
    imgd 18873
    alex_photograph "Кхм..."
    alex_photograph "Честно сказать, для меня было большой неожиданностью твое приглашение."
    # если Мелани делала Алексу минет на камеру
    if monicaMelanieVictoriaPunishment3 == True:
        alex_photograph "Я подумал, что в тот раз... В общем, это все было постановкой."
        #
        $ notif(_("Мелани делала Алексу минет на камеру"))
        #
        imgf 18874
        melanie "Почему ты так подумал, Алекс?" # у Мелани покер-фейс
        imgd 18875
        alex_photograph "Ну..."
        alex_photograph "Я же попытался с тобой поговорить после этого, Мелани..."
        alex_photograph "Ты мне ясно дала понять, что не хочешь иметь со мной ничего общего."
        imgd 18876
        melanie "Я просто немного перенервничала, Алекс..."
        alex_photograph "Да?"
        # Алекс заметно нервничает
        alex_photograph "Кхм... Я не знаю, что это значит, Мелани."
        alex_photograph "Но вообще..."
    imgf 18877
    alex_photograph "Ты всегда так холодно ко мне относилась..."
    alex_photograph "Совсем не обращала на меня внимания..."
    alex_photograph "Я даже надеяться не мог на интерес с твоей стороны."
    imgd 18878
    melanie "Тем не менее, это так, Алекс."
    melanie "Я... Просто хорошо умею скрывать свои чувства."
    imgf 18879
    alex_photograph "То есть все, что тогда говорила Виктория про тебя..."
    alex_photograph "Это правда?"
    # Мелани бросает взгляд на камеру
    music Master_Disorder
    imgd 18880
    melanie "..."
    imgd 18881
    melanie "Да, правда."
    melanie "Виктория моя подружка и знает о моих чувствах к тебе."
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса
    # У Виктории ехидная улыбка
    # затемнение, смена кадра
    # апартаменты Мелани
    imgf 18924
    w
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Тем временем в офисе Дика...")) from _rcall_textonblack_59
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 19023
    w
    imgf 19022
    w
    fadeblack 2.0
    music Groove2_85
    imgf 18882
    alex_photograph "Я не ожидал услышать подобного признания от тебя, Мелани..."
    alex_photograph "Я... Я немного растерян..."
    alex_photograph "Ты - самая знаменитая топ-модель..."
    alex_photograph "У тебя миллионы поклонников..."
    alex_photograph "И я..."
    imgd 18883
    melanie "Все хорошо, Алекс."
    melanie "Выпей немного вина, расслабься."
    melanie "И мне налей."
    melanie "А я пока включу нам что-нибудь романтическое..."
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound metal_slide
    imgfl 18932
    w
    sound gramophone
    imgf 18884
    w
    # Мелани протягивает руку к патефону
    # затемнение, звук льющегося в бокал вина
    # звук патефона, музыка (какой-нибудь романтик)
    # смена кадра
    # играет патефон, перед Мелани на столе стоит полный бокал вина, она без эмоций сидит и смотрит в одну точку
    music In_Your_Arms
    imgd 18885
    melanie "..."
    # Алекс в этой время делает глоток вина и немного расслабляется, но все еще на нервах
    imgf 18886
    w
    imgd 18887
    alex_photograph "Приятная музыка, Мелани. Твоя любимая?"
    # Мелани выходит из состояния задумчивости
    imgf 18888
    melanie "Что?"
    melanie "Музыка?"
    melanie "Ах, да. Мне тоже нравится..."
    # Алекс смотрит на патефон и только сейчас замечает, что за ним стоит камера
    imgd 18889
    alex_photograph "Мелани, это что, камера?"
    melanie "Да."
    imgf 18890
    alex_photograph "Зачем тебе камера?"
    alex_photograph "Ты хочешь все записать?"
    melanie "Да, хочу..."
    imgd 18891
    alex_photograph "Хм, это странно..."
    alex_photograph "Я не замечал раньше за тобой такого."
    alex_photograph "Ты всегда избегала моей камеры, Мелани."
    # она ему холодно отвечает
    imgf 18892
    melanie "Потому что тогда тебя не было со мной в кадре, Алекс."
    melanie "Я хочу запечатлеть наше с тобой свидание."
    melanie "На память..."
    imgd 18893
    melanie "Ты же не будешь против, Алекс?"
    imgd 18894
    alex_photograph "Все равно мне кажется это странным..."
    alex_photograph "Но я не против, Мелани. Ты знаешь, я люблю камеры!"
    # Алекс откидывается на спинку кресла и осматривается, смотрит на портреты на стене
    # замечает, что один из портретов разрисован
    # Алекс удивленно смотрит на портрет
    imgf 18895
    w
    imgd 18896
    alex_photograph "Мелани, это одна из моих любимых работ."
    alex_photograph "Почему она разрисована?"
    alex_photograph "Она тебе не нравится?"
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса, с улыбочкой
    # затемнение, смена кадра
    # апартаменты Мелани
    # Мелани, глядя в камеру, говорит
    imgf 18872
    melanie "Алекс, я..."
    imgd 18924
    w
    imgf 18872
    melanie "Я мечтала о твоем члене, рисовала его и думала в тот момент о тебе."
    melanie "Это твоя работа и я хочу, чтобы это тут осталось."
    melanie "Как символ наших с тобой чувств."
    melanie "Поэтому, давай не будем это стирать?"
    imgd 18924
    w
    fadeblack 2.0
    music Groove2_85
    imgfl 19024
    sound snd_woman_laugh3
    w
    # Алекс удивленно смотрит на Мелани
    fadeblack 2.0
    music In_Your_Arms
    imgf 18897
    alex_photograph "Ну хорошо..."
    alex_photograph "Ты правда думала о моем... Обо мне, когда рисовала это?"
    melanie "Да."
    imgd 18882
    alex_photograph "И много у тебя разрисованных портретов?"
    imgd 18883
    melanie "..."
    melanie "Только этот."
    melanie "И я..."
    # снова взгляд на камеру
    menu:
        "Предложить Алексу жить вместе.":
            $ melanieAlexFirstDate1 = True # Мелани предложила Алексу жить вместе
            pass
    imgf 18898
    melanie "Я надеюсь, что мне не придется больше мечтать о тебе, Алекс..."
    melanie "Рисуя на твоих работах."
    melanie "Потому что ты согласишься на мое предложение."
    imgd 18899
    alex_photograph "Какое предложение, Мелани?"
    melanie "..."
    melanie "Жить вместе со мной."
    # Алекс шокирован
    music stop
    sound plastinka1b
    img 18900 hpunch
    alex_photograph "Ты хочешь, чтобя я и ты?"
    alex_photograph "Чтобы мы жили вместе?!"
    img 18901
    alex_photograph "?!!!!?!?!"
    music Master_Disorder
    imgf 18902
    melanie "Да..." # без особого энтузиазма
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса
    # затемнение, смена кадра
    # апартаменты Мелани
    # Алекс не верит
    imgd 18851
    w
    fadeblack 2.0
    music Groove2_85
    imgf 19025
    w
    imgd 19026
    w
    fadeblack 2.0
    music In_Your_Arms
    imgfl 18903
    alex_photograph "Это очень странно, Мелани..."
    alex_photograph "Почему ты предлагаешь мне сразу жить вместе?"
    melanie "Потому что я хочу этого, Алекс..."
    imgf 18904
    alex_photograph "Мы с тобой даже не встречались."
    alex_photograph "Ты всегда была так холодна со мной и вдруг сразу предлагаешь жить вместе."
    imgd 18905
    melanie "..."
    melanie "Просто я долго сомневалась."
    melanie "Но теперь я точно знаю, что хочу этого."
    imgd 18906
    alex_photograph "Мелани, но как ты можешь это утверждать?"
    alex_photograph "У нас с тобой не было даже интима!"
    # Мелани снова смотрит на камеру
    menu:
        "Переодеться в одежду, которую выбрала Виктория.":
            $ melanieAlexFirstDate2 = True # Мелани переоделась для Алекса в наряд, который выбрала Виктория
            pass
    imgf 18907
    melanie "Алекс, подожи минуту. Я сейчас вернусь."
    # затемнение
    # спустя несколько минут
    # Мелани возвращается в гостиную, переодевшись в откровенный наряд
    # Алекс смотрит на нее обалдевшим взглядом
    # она садится напротив него, смотрит в камеру
    fadeblack
    sound2 snd_fabric1
    sound highheels_short_walk
    pause 2.5
    music ZigZag
    imgfl 18908
    w
    img 18909 vpunch
    w
    imgd 18910
    w
    imgd 18911
    melanie "Алекс, ты меня очень огорчишь, если откажешься жить со мной."
    # он пускает на нее слюни и ничего уже не соображает
    music In_Your_Arms
    imgf 18912
    alex_photograph "Мелани!"
    alex_photograph "О Боже! Мелани, что ты со мной делаешь?!"
    # Алекс соскакивает с кресла и припадает к ногам Мелани (она на диване, он на коленях на полу перед ней)
    sound Jump1
    imgd 18913
    alex_photograph "Я согласен! Я все готов сделать для тебя, Мелани!"
    alex_photograph "Дай мне! Дай рассмотреть твою киску вблизи!"
    # Мелани недовольно смотрит на камеру, потом на Алекса
    menu:
        "Раздвинуть ноги.":
            pass
    imgd 18914
    melanie "..."
    # раздвигает ноги
    music stop
    music2 Loved_Up
    imgf 18915
    alex_photograph "Оооо!!!"
    imgfl 19013
    alex_photograph "Оооо, Меланиии..."
    # Алекс взглядом маньяка рассматривает ее, потом припадает губами к ее киске, ликинг
    imgf 18916
    w

    sound vjuh3
    img 18917 vpunch
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking1_1 = Movie(play="video/v_Melanie_Alex_Licking1_1.mkv", fps=30)
    show videov_Melanie_Alex_Licking1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18918
    alex_photograph "Ммммм!!!"
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking1_2 = Movie(play="video/v_Melanie_Alex_Licking1_2.mkv", fps=30)
    show videov_Melanie_Alex_Licking1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 18919
    w
    imgf 18920
    alex_photograph "МММММ!!!"
    w
#    sound lick3
    imgd 18921
    w
    sound lick3
    imgd 18922
    w
    sound lick3
    imgd 18921
    w
    sound lick3
    imgd 18922
    w
    sound lick3
    imgd 18921
    w
    sound lick3
    imgd 18922
    w
    sound lick3
    imgd 18921
    w
    sound lick3
    imgd 18922
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking1_3 = Movie(play="video/v_Melanie_Alex_Licking1_3.mkv", fps=30)
    show videov_Melanie_Alex_Licking1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgf 18924
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking1_4 = Movie(play="video/v_Melanie_Alex_Licking1_4.mkv", fps=30)
    show videov_Melanie_Alex_Licking1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Мелани сидит, прикрыв глаза, особо не эмоционирует
    # потом снова смотрит на камеру
    # офис Дика, Виктория сидит у компа
    # Виктория зло смотрит на монитор
    music2 stop
    fadeblack 2.0
    music Groove2_85
    imgfl 19027
    victoria "И что, подружка? Ты решила отделаться лишь этим?"
    imgf 19028
    victoria "Просто дать полизать ему свою киску?"
    victoria "Ты решила подвести меня?"
    # смена кадра на апартаменты Мелани
    fadeblack 2.0
    music In_Your_Arms
    imgf 18925
    melanie "Алекс, стоп!"
    imgd 18926
    alex_photograph "Да? Что-то не так?"
    alex_photograph "Тебе что-то не нравится?"
    imgf 18927
    melanie "Все хорошо, Алекс."
    melanie "Может, пойдем в спальню?"
    melanie "Нам там будет намного удобнее..."
    imgd 18928
    alex_photograph "Да-да, пойдем."
    alex_photograph "Конечно."
    # Мелани берет камеру с собой
    imgf 18929
    alex_photograph "Мелани, давай мы оставим камеру здесь?"
    melanie "..."
    melanie "Я хотела бы записать не только наше с тобой первое свидание, Алекс."
    melanie "Но и наш первый интим."
    melanie "Ты ведь не откажешь мне в этом?"
    imgd 18930
    alex_photograph "Я не в силах отказать тебе, Мелани."
    alex_photograph "Мне до сих пор кажется, что я попал в один из своих снов..."
    alex_photograph "Что все это сюр и..."
    alex_photograph "Скоро я открою глаза и ты растворишься в утреннем тумане."
    alex_photograph "Мелани... У меня просто нет слов, насколько ты прекрасна!"
    imgd 18931
    melanie "Спасибо, Алекс..."
    # берет камеру
    # смена кадра, спальня
    # Мелани заходит в спальню
    # Алекс идет за ней, плотоядно на нее смотрит
    # Показываем камеру на тумбочке со звуком того что ее ставят, Мелани стоит рядом
    # Алекс подходит к ней и присев или наклонившись (как делал Эдвардс) целует ее ягодицы
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music In_Your_Arms
    imgfl 18933
    w
    imgf 18934
    w
    sound snd_cardboard1
    imgd 18935
    w
    imgf 18936
    alex_photograph "Меланиии..."
    alex_photograph "Ты - богиня."
    sound kiss1
    imgd 18937
    alex_photograph "Мммм..."
    w
    sound kiss1
    imgd 18940
    w
    sound kiss1
    imgd 18941
    w
    # Мелани остается равнодушной
    imgf 18938
    melanie "Алекс, подожди."
    melanie "Пойдем на кровать?"
    # Алекс отстраняется, Мелани ложится на кровать в соблазнительную позу
    # Алекс смотрит на нее и пускает слюни
    # она смотрит на камеру
    fadeblack 1.5
    music ZigZag
    imgfl 18939
    w
    imgf 18942
    w
    imgd 18943
    melanie "Алекс..."
    melanie "Чего ты ждешь?"
    melanie "Иди сюда."
    imgd 18944
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    # Алекс снимает с себя свой свитер и лезет к Мелани на кровать
    # она выжидательно смотрит на него, эмоций никаких не показывает
    # Алекс осторожно прикасается ладонями к ее ногам
    # ведет ладонями от коленей вверх по бедрам
    # Мелани во время ласк лежит на кровати, прикрыв глаза
    # иногда приоткрывает глаза и бросает взгляд на камеру или на Алекса
    imgfl 18945
    alex_photograph "Я никода не видел столь совершенной красоты..."
    alex_photograph "Мелани..."
    alex_photograph "Твоя кожа как бархат..."
    # ладонями по попе и к талии
    imgf 18946
    alex_photograph "Твои формы... Такие женственные... Идеальные..."
    # Алекс опускает ладнони на грудь Мелани
    alex_photograph "Моя богиня..."
    # смена кадра, офис Дика
    # Виктория сидит у компа, отодвинувшись от стола
    # ноги широко раздвинуты, одна на столе
    # Виктория неотрывно смотрит в монитор и ласкает себя
    # смена кадра на апартаменты Мелани
    # Алекс гладит Мелани по скуле, прикасается пальцем к губам
    sound kiss1
    imgd 18947
    w
    imgd 18948
    w
    imgd 18949
    w
    sound kiss2
    imgd 18950
    w
    imgd 18949
    w
    imgd 18948
    w
    sound kiss1
    imgd 18947
    w
    imgd 18948
    w
    imgd 18949
    w
    sound kiss2
    imgd 18950
    w
    imgd 18949
    w
    imgd 18948
    w
    sound kiss1
    imgd 18947
    w
    imgf 18951
    alex_photograph "Смотрю на тебя и у меня просто сносит крышу."
    alex_photograph "Мне никто в этом мире больше не нужен."
    alex_photograph "Только ты, моя богиня."
    # наклоняется к ее губам
    # поцелуй
    imgd 18952
    alex_photograph "Мммм..."
    alex_photograph "Мелани..."
    # целует ее лицо, шею
    sound snd_fabric1
    imgd 18953
    alex_photograph "Ты само совершенство, Мелани..."
    # спускается на плечи, потом ниже
    # целует грудь через бра
    imgf 18954
    alex_photograph "Твоя грудь..."
    imgd 18955
    alex_photograph "Я мечтал прикоснуться к ней... Целовать ее, ласкать..."
    imgd 18954
    w
    imgd 18955
    w
    imgd 18954
    w
    imgd 18955
    w
    imgd 18954
    w
    imgd 18955
    w
    # приспускает или снимает бра
    # гладит груди ладонями, сжимает их
    # наклоняется к соскам и целует их (или посасывает, немного оттягивая грудь вверх)
    imgf 18956
    alex_photograph "Мммм..."
    imgd 18957
    w
    sound kiss1
    imgd 18958
    w
    imgd 18956
    w
    imgd 18957
    w
    sound kiss1
    imgd 18958
    w
    imgd 18956
    w
    imgd 18957
    w
    sound kiss1
    imgd 18958
    w
    imgd 18956
    w
    imgd 18957
    w
    sound kiss1
    imgd 18958
    w
    # спускается поцелуями по животу
    sound kiss2
    imgf 18959
    alex_photograph "Какой божественный аромат..."
    alex_photograph "Обожаю тебя..."
    alex_photograph "Мммм..."
    # спускается к ее киске, начинает лизать
    sound kiss2
    imgd 18960
    alex_photograph "Ммммм!!!"
    w
    imgf 18970
    w
    fadeblack 2.0
    music Groove2_85
    imgf 19029
    w
    imgd 19030
    w
    sound ahhh1
    imgf 19031
    w
    # Мелани прикрывает глаза, ей приятно, но не более того, никаких бурных эмоций
    # Алекс лижет киску и одной рукой надрачивает свой стояк
    # после буквально пары движений рукой вверх-вниз Алекс кончает
    fadeblack 2.0
    music stop
    music2 Loved_Up
    imgfl 18961
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking2_1 = Movie(play="video/v_Melanie_Alex_Licking2_1.mkv", fps=30)
    show videov_Melanie_Alex_Licking2_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18962
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking2_2 = Movie(play="video/v_Melanie_Alex_Licking2_2.mkv", fps=30)
    show videov_Melanie_Alex_Licking2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18963
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Licking1.ogg"
    scene black
    image videov_Melanie_Alex_Licking2_3 = Movie(play="video/v_Melanie_Alex_Licking2_3.mkv", fps=30)
    show videov_Melanie_Alex_Licking2_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18967
    w
    imgd 18964
    w
    sound lick3
    imgd 18966
    w
    sound lick3
    imgd 18965
    w
    sound lick3
    imgd 18966
    w
    sound lick3
    imgd 18965
    alex_photograph "ААА!"

    sound lick3
    imgd 18966
    alex_photograph "АААААА!!"
    img 18968
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan1
    alex_photograph "ААААААААА!!!"
    # Алекс растерянно смотрит на свой член
    # Мелани приподнимается и удивленно и слегка насмешливо смотрит на него
    music2 stop
    fadeblack 1.5
    music In_Your_Arms
    imgfl 18969
    melanie "И это все?"
    melanie "???"
    # Мелани смотрит на камеру, она обеспокоенна
    imgf 18970
    melanie "..."
    menu:
        "Черт! Виктория сказала, что обязательно должен быть секс...":
            $ melanieAlexFirstDate3 = True # Мелани и Алекс занимались сексом перед камерой
            pass
    imgd 18971
    melanie "А я?"
    melanie "???"
    melanie "А интим?"
    imgf 18972
    melanie "Если ты хочешь жить со мной..."
    melanie "То ты..."
    melanie "Ты должен сделать это..." # Смущенно отворачивается
    # Алекс вовсе не возражает
    imgd 18973
    alex_photograph "Я сейчас..."
    alex_photograph "Дай мне пару минут."
    alex_photograph "Я сейчас все сделаю, Мелани."
    # он снова гладит ее бедра, она переворачивается на живот
    # он начинает мять попу
    fadeblack 1.5
    music In_Your_Arms
    imgf 18974
    w
    imgd 18975
    alex_photograph "Ммммм... Какие формы..."
    # потом приближает свой полувялый член к ее попе и начинает им водить туда-сюда по ягодицам, трется
    # у него начинает вставать
    # Мелани снова бросает обеспокоенный взгляд в камеру
    imgf 18976
    w
    imgd 18977
    w
    sound kiss2
    imgd 18978
    alex_photograph "Мммм..."
    imgd 18979
    melanie "Алекс?"
    alex_photograph "Да, Мелани?"
    melanie "Ты точно не против жить со мной?"
    melanie "Ты точно этого хочешь?"
    music stop
    music2 Loved_Up
    # раздвигает ноги
    imgf 19067
    alex_photograph "Мелани, раздвинь скорее свои ножки!"
    alex_photograph "Я хочу к тебе!"
    imgd 19068
    w
    imgd 19069
    w
    imgf 18980
    alex_photograph "Да!"
    alex_photograph "Я о таком даже мечтать не мог!"
    # Алекс начинает вводить член в ее киску, вводит наполовину
    imgd 18981
    melanie "Точно? Ты в этом уверен?"
    alex_photograph "Конечно, Мелани!"
    # он вводит в нее головку и спрашивает
    alex_photograph "Мелани, ты не передумала?"
    alex_photograph "Я могу войти в тебя глубже?"
    melanie "Я не передумала, Алекс..."
    # он вводит головку полностью
    imgf 18982
    alex_photograph "Точно?"
    alex_photograph "Я могу полность войти в твою киску, Мелани?"
    melanie "Алекс, сделай уже это!"
    melanie "Я не передумала!"
    # Алекс входит в нее, начинает двигаться
    sound chpok6
    img 18983 vpunch
    w
    alex_photograph "Ооооо!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Sex1.ogg"
    scene black
    image videov_Melanie_Alex_Sex1_1 = Movie(play="video/v_Melanie_Alex_Sex1_1.mkv", fps=30)
    show videov_Melanie_Alex_Sex1_1
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18984
    alex_photograph "Как же хорошо!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Sex1.ogg"
    scene black
    image videov_Melanie_Alex_Sex1_2 = Movie(play="video/v_Melanie_Alex_Sex1_2.mkv", fps=30)
    show videov_Melanie_Alex_Sex1_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18985
    alex_photograph "Не могу поверить, что мой член внутри такой топ-модели!!"
    alex_photograph "Оооох..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Sex1.ogg"
    scene black
    image videov_Melanie_Alex_Sex1_3 = Movie(play="video/v_Melanie_Alex_Sex1_3.mkv", fps=30)
    show videov_Melanie_Alex_Sex1_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Sex1.ogg"
    scene black
    image videov_Melanie_Alex_Sex1_4 = Movie(play="video/v_Melanie_Alex_Sex1_4.mkv", fps=30)
    show videov_Melanie_Alex_Sex1_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 18986
    alex_photograph "У тебя миллионы поклонников!"
    imgd 18987
    alex_photograph "Но именно мне выдался шанс трахать тебя!"
    alex_photograph "Даааа!!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Melanie_Alex_Sex1.ogg"
    scene black
    image videov_Melanie_Alex_Sex1_5 = Movie(play="video/v_Melanie_Alex_Sex1_5.mkv", fps=30)
    show videov_Melanie_Alex_Sex1_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # смена кадра, офис Дика
    # Виктория продолжает смотреть в монитор и ласкать себя
    # смена кадра на апартаменты Мелани
    # потом Алекс останавливается
    imgf 18970
    w
    music2 stop
    fadeblack 2.0
    music Groove2_85
    imgfl 19032
    w
    sound ahhh1
    imgd 19033
    w
    sound ahhh11
    imgd 19034
    w
    fadeblack 2.0
    music In_Your_Arms
    imgfl 18988
    alex_photograph "Мелани, я хочу видеть твое лицо!"
    alex_photograph "Давай, поменяем позу?"
    # Мелани говорит ему равнодушно
    imgf 18989
    melanie "На сегодня достаточно, Алекс..."
    melanie "Секс уже был."
    imgd 18990
    alex_photograph "Но Мелани!"
    alex_photograph "Раз ты не кончила, значит секса не было!"
    # Мелани смотрит на камеру, злится
    img 18991
    melanie "!!!"
    imgd 18992
    melanie "Какую позу ты хочешь, Алекс?"
    alex_photograph "Я хочу, чтобы ты смотрела мне в глаза."
    alex_photograph "Хочу увидеть, как ты кончаешь!"
    melanie "Мне перевернуться?"
    alex_photograph "Нет, давай по-другому..."
    alex_photograph "Садись на меня..."
    # Мелани медлит
    imgf 18993
    melanie "..."
    melanie "Я не очень люблю эту позу..."
    alex_photograph "Ну, Мелани!"
    alex_photograph "Давай!"
    alex_photograph "Хотя бы чуть-чуть!"
    # Мелани смотрит на камеру, потом нехотя соглашается
    imgd 18994
    melanie "Хорошо..."
    melanie "Ложись на кровать."
    # Алекс довольный ложится на спину
    # Мелани свысока смотрит на него, на его член
    # потом нехотя садится на него, смотрит на камеру, потом в его глаза
    # секс, Мелани сверху, она начала получать удовольствие от процесса, стонет
    # Алекс периодически мнет ее груди, гладит ее бедра
    fadeblack 1.5
    music Loved_Up
    imgf 18995
    w
    imgd 18996
    w
    fadeblack 1.5
    music stop
    music2 Loved_Up2
    sound chpok6
    img 18997 vpunch
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Melanie_Alex_Sex2.ogg"
    scene black
    image videov_Melanie_Alex_Sex2_1 = Movie(play="video/v_Melanie_Alex_Sex2_1.mkv", fps=30)
    show videov_Melanie_Alex_Sex2_1
    with fade
    alex_photograph "Ооооо!!!"
    alex_photograph "Как же хорошо!"
    alex_photograph "Ты само совершенство, Мелани..."
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # смена кадра, офис Дика
    # Виктория продолжает смотреть в монитор и ласкать себя
    # смена кадра на апартаменты Мелани
    imgd 18970
    w

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Melanie_Alex_Sex2.ogg"
    scene black
    image videov_Melanie_Alex_Sex2_2 = Movie(play="video/v_Melanie_Alex_Sex2_2.mkv", fps=30)
    show videov_Melanie_Alex_Sex2_2
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 18998
    alex_photograph "Звезда мира моды! Знаменитость!"
    alex_photograph "Сколько журналистов гадали, какая твоя киска на вкус!"
    sound kiss1
    imgd 18999
    alex_photograph "Оооо..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Melanie_Alex_Sex2.ogg"
    scene black
    image videov_Melanie_Alex_Sex2_3 = Movie(play="video/v_Melanie_Alex_Sex2_3.mkv", fps=30)
    show videov_Melanie_Alex_Sex2_3
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19000
    alex_photograph "Тебя желает пол мира!!!"
    imgd 19001
    alex_photograph "А трахаю тебя Я!!!"
    alex_photograph "Ааааа!!"

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Melanie_Alex_Sex2.ogg"
    scene black
    image videov_Melanie_Alex_Sex2_4 = Movie(play="video/v_Melanie_Alex_Sex2_4.mkv", fps=30)
    show videov_Melanie_Alex_Sex2_4
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 19002
    alex_photograph "Оооох..."
    melanie "Мммм..."

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Melanie_Alex_Sex2.ogg"
    scene black
    image videov_Melanie_Alex_Sex2_5 = Movie(play="video/v_Melanie_Alex_Sex2_5.mkv", fps=30)
    show videov_Melanie_Alex_Sex2_5
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19003
    alex_photograph "Ааааа!!"
    imgf 19004
    alex_photograph "Мммм..."
#    music Loved_up2

    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.0) + " loop 0.0>Sounds/v_Melanie_Alex_Sex2.ogg"
    scene black
    image videov_Melanie_Alex_Sex2_6 = Movie(play="video/v_Melanie_Alex_Sex2_6.mkv", fps=30)
    show videov_Melanie_Alex_Sex2_6
    with fade
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 19005
    alex_photograph "Даааа... Продолжай таааак..."
    melanie "Мммм..."
    imgf 19006
    alex_photograph "Быстрее..."
    # Мелани кончает первой, Алекс следом за ней
# snd_melanie_cum
# snd_melanie_cum2
    img 19007
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound snd_melanie_cum
    melanie "Ооооо!!"
    melanie "ОООООО!!!"
    menu:
        "Кончить внутрь Мелани.":
            imgd 19008
            alex_photograph "Я сейчас кончуууу!!!"
            melanie "Не вздумай кончать в меня!"
            # она хочет встать, но Алекс хватает ее за бедра и удерживает, кончает внутрь
            img 19009
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            img 19010
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            melanie "Черт!"
            melanie "Алекс!"
            melanie "!!!"
            # испуганный взгляд на камеру
            $ melanieAlexFirstDate_cumzone = 1
            pass
        "Кончить на киску Мелани.":
            imgd 19008
            alex_photograph "Я сейчас кончуууу!!!"
            alex_photograph "ААА!"
            melanie "Не вздумай кончать в меня!"
            # Мелани приподнимается и он кончает на нее
            img 19009
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            img 19011
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            imgd 19012
            w
            # Мелани смотрит недовольно на камеру
            $ melanieAlexFirstDate_cumzone = 2
            pass
    # смена кадра, офис Дика
    # Виктория кончает
    imgf 18970
    w
    music2 stop
    fadeblack 2.0
    music Loved_Up
    imgfl 19035
    victoria "Мммм..."
    sound ahhh1
    imgf 19036
    victoria "Ааааа!"
    img 19037
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan11
    victoria "АААААААА!!!"
    # смена кадра на апартаменты Мелани
    # Мелани ложится спать
    # довольный Алекс лезет обниматься к ней
    fadeblack 2.0
    music In_Your_Arms
    imgfl 19014
    w
    imgf 19015
    alex_photograph "Мелани, это был самый лучший вечер в моей жизни!"
    alex_photograph "Ты прекрасна!"
    alex_photograph "Я тебя обожаю, Мелани!"
    # Мелани раздражена
    imgd 19016
    melanie "Алекс..."
    melanie "Ты будешь спать на диване в гостиной."
    # Алекс расстроенно
    music stop
    sound plastinka1b
    img 19017 hpunch
    alex_photograph "Но, Мелани..."
    alex_photograph "Почему?"
    alex_photograph "Если мы теперь живем вместе, то и спать должны вместе!"
    music ZigZag
    imgf 19018
    melanie "Я привыкла спать одна в своей постели..."
    melanie "Мне нужно время."
    melanie "Поэтому сегодня ты спишь в гостиной."
    melanie "И это не обсуждается, Алекс."
    music Groove2_85
    imgd 19019
    alex_photograph "..." # расстроен
    # Алекс уходит, говорит оборачиваясь
    imgf 19020
    alex_photograph "Тогда я с утра приду к тебе."
    alex_photograph "И разбужу тебя своими ласками!"
    alex_photograph "Люблю начинать день с хорошего секса!"
    imgd 19021
    melanie "!!!"
    # Мелани зло на него смотрит
    # занавес
    fadeblack 3.0
    return
