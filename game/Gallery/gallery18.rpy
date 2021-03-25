label gallery_19010:
    # Мелани все также задумчиво сидит на диване
    # стук в дверь
    # Мелани идет к двери
    # затемнение, дверь открывается
    # заходит Алекс
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Некоторое время спустя..."))
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
    call textonblack(t_("Тем временем в офисе Дика..."))
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

label gallery_23739: #Поставить на стол одну ногу.
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

label gallery_23759: #Сесть на стол лицом к Бифу, широко раздвинув ноги.
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

label gallery_24377: #Сесть на стол спиной к Бифу.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    imgfl 22908
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
    imgf 22909
    mt "Сволочь!"

    imgd 24354
    m "Биф, что ты хочешь чтобы я снова сделала?!"

    biff "Это не моя задача придумывать, чем развлекать папочку, цыпочка!"
    biff "Залезь на стол, сделай что-нибудь новое."
    biff "Цыпочка должна развлекать папочку! Папочке скучно!"

    menu:
        "Залезть на стол Моники.":
            pass

    sound snd_walk_barefoot
    imgf 24355
    mt "Ненавижу! Ненавижу!"
    fadeblack 1.5
    music Groove2_85
    imgf 24356
    w
    imgd 24357
    m "Так достаточно, Биф?"

    imgf 24358
    biff "Нет, цыпочка!"
    biff "Папочке ничего не видно!"
    biff "Покажи себя сзади!"
    biff "Папочка хочет видеть за что он платит такие большие деньги какой-то шлюхе!"

    img 24359
    m "Я не шлюха, Биф!"

    imgd 24360
    biff "Ты уличная двадцатидолларовая шлюха, которая пытается быть хорошей цыпочкой и вечелить папочку!"
    biff "Она знает, что плохая цыпочка здесь не задержится и не будет зарабатывать такие огромные деньги!"
    biff "Быстро развернись и покажи мне свою задницу!"
    biff "Читатели нашего журнала ждут, когда твоя голая задница будет на обложке журнала!"
    biff "И я должен проверить, что они не будут разочарованы!"

    menu:
        "Сесть спиной к Бифу.":
            pass
    music Pyro_Flow
    imgf 24361
    mt "БОЖЕ! На что мне приходится идти, чтобы у меня были деньги для этой сучки Виктории и Дик продолжал заниматься моим делом!"
    mt "Этот Биф издевается надо мной все больше и больше!"
    mt "Сейчас у меня нет выбора, но мне надо найти выход!"
    mt "Так не может больше продолжаться!"
    fadeblack 1.5
    music Hidden_Agenda
    imgf 24362
    m "Мне... Нужны эти деньги Биф..."
    m "Я хорошая цыпочка..."
    mt "!!!"
    music Groove2_85
    imgd 24363
    biff "Это ты называешь показать себя?"
    biff "За такое наши читатели не заплатят ни цена!"
    biff "Цыпочка сейчас ляжет на стол и вытянет свои ножки ко мне!"

    menu:
        "Лечь на стол перед Бифом.":
            pass
    fadeblack 1.5
    music Hidden_Agenda
    imgf 24364
    m "Так дебя устроит, Биф?"
    m "Я достаточно развлекла папочку?!"
    music Loved_Up
    imgd 24365
    biff "Нет, цыпочка! Еще далеко не достаточно!"
    biff "Цыпочка сейчас раздвинет свои ножки, очень широко!"

    menu:
        "Раздвинуть ноги.":
            pass
    mt "Дьявол!"

    imgd 24366
    sound Jump2
    m "Так, Биф?!"

    imgf 24367
    biff "Нет, цыпочка! Еще шире!"
    biff "Папочка сказал что цыпочка раздвинет ноги очень широко!"
    biff "Перед папочкой!"

    menu:
        "Раздвинуть ноги еще шире.":
            pass
    sound Jump2
    imgd 24368
    m "Так устроит?"
    mt "Дьявол! Чувствую себя отвратительно!"
    mt "Грязный извращенец!"

    imgf 24369
    biff "Давай, тянись ручками к своим ножкам!"
    biff "Покажи папочке свою гибкость!"
    biff "Папочка любит гибких цыпочек!"
    biff "Скажи, ты гибкая цыпочка?"
    sound Jump1
    imgd 24370
    mt "БОЖЕ! Как я ненавижу этого Бифа!"
    mt "Я убью его, клянусь!"


    imgf 24371
    m "Я... Я гибкая цыпочка, Биф..."

    imgd 24372
    biff "Отлично!"
    biff "А теперь цыпочка встанет на колени и хорошенько выгнется к папочке!"
    biff "Папочка хочет хорошенько рассмотреть то, за что скоро будут платить наши читатели!"
    music Pyro_Flow
    imgd 24373
    mt "Нет, я его не убью!"
    mt "Я буду его мучать! Я его буду долго мучать!!"
    mt "Я сделаю из него ничтожество! Он будет моим ковриком для обуви!"
    mt "Он... Он..."
    biff "Цыпочка, я жду!"

    menu:
        "Дать Бифу хорошенько рассмотреть себя.":
            pass

    mt "Дьявол!"
    fadeblack 1.5
    music Loved_Up
    imgfl 24374
    biff "Да, отлично! Вот так!"

    imgf 24375
    biff "Итак, что сейчас делает цыпочка?"

    imgd 24376
    m "Цыпочка... Показывает себя папочке..."

    imgf 24377
    biff "Правильно! Хорошая цыпочка!"

    imgd 24378
    biff "Надо же, какие у цыпочки мягкие бархатные ножки!"

    imgd 24379
    biff "И не скажешь что они принадлежат двадцатидолларовой шлюхе, которая приыкла работать на улице!"

    img 24380 vpunch
    m "Биф, я не шлюха!"

    imgd 24381
    biff "Да, ты теперь цыпочка!"
    biff "Которой папочка платит достаточно денег, чтобы ей не приходилось сосать на улице члены за $ 20!"

    mt "!!!"

    imgd 24382
    mt "Я ненавижу этого ублюдка!"
#    sound Jump1
    sound Jump1
    imgf 24383
    biff "Да, многие читатели ждут обложку с этой киской."
    biff "Думая что это и правда Моника Бакфетт."

    music Power_Bots_Loop
    img 24384 hpunch
    m "Биф, не смей меня лапать!!!"

    imgd 24385
    biff "Это обычный осмотр модели журнала!"
    biff "Если цыпочка будет пререкаться с папочкой, то вылетит на улицу прямо сейчас!"

    menu:
        "Терпеть прикосновения Бифа.":
            pass

    music Loved_Up
    imgf 24386
    mt "Дьявол, как мне выдержать это?!"

    imgd 24387
    biff "Итак, вот что вскоре ждет наших читателей..."

    imgf 24388
    biff "Читатели должны подумать, что это дейстительно киска Моники Бакфетт..."
    biff "Они платят за это свои деньги..."
    biff "В мой журнал..."

    imgd 24389
    biff "Жаль что она не настоящая..."
    biff "Мне рассказывали как выглядит настоящая киска Моники Бакфетт..."

    imgd 24390
    w
    imgd 24389
    w
    imgd 24390
    w
    imgf 24391
    biff "И, по описанию, она совсем не похожа..."

    imgd 24392
    mt "Что значит непохожа?!"
    mt "Никто не мог видеть меня обнаженной! Что за вздор!"

    imgf 24393
    w
    imgd 24394
    biff "Хотя эта киска тоже красивая..."
    biff "Хоть и обходится папочке слишком дорого..."
    sound chpok8
    imgd 24395 #чавк
    mt "!!!"
    music Pyro_Flow
    img 24396 hpunch
    m "НЕТ!!!"
    sound snd_bodyfall
    img 24397 vpunch
    m "ЧТО ЭТО ЗНАЧИТ, БИФ?!"
    music Groove2_85
    imgf 24398
    biff "Это значит что папочка проверяет свою цыпочку!"
    biff "Которой оказывает безмерное доверие, разрешая снимать свою задницу под видом Моники Бакфетт!"

    imgd 24399
    biff "Цыпочка расстроила папочку!"
    biff "Убирайся отсюда! Папочке не нужны плохие цыпочки!"
    sound Jump2
    imgf 24400
    m "Биф... Почему убираться отсюда?"
    m "Я... Я ведь сделала как ты просил..."

    imgd 24401
    biff "Ты убежала от папочки! А так хорошие цыпочки себя не ведут!"
    biff "Я поменяю тебя на другую цыпочку, которая дает себя трогать!"

    imgd 24402
    mt "Мерзавец! Он теперь что, собирается меня лапать?!"
    music Hidden_Agenda
    imgf 24403
    m "Биф... Я..."
    m "Я не убегала от тебя..."
    music Groove2_85
    imgd 24404
    biff "А что тогда это было?!"
    biff "Папочка хотел проверить киску своей цыпочки изнутри!"
    biff "А цыпочка убежала от папочки!"
    biff "Теперь эта цыпочка не получит ни цента за свою работу!"

    menu:
        "Сказать Бифу что Моника хорошая цыпочка.":
            pass

    imgd 24402
    mt "Дьявол! Мне надо что-то придумать, чтобы успокоить этого придурка!"
    music Hidden_Agenda
    imgf 24405
    m "Биф, я не убегала от тебя..."
    biff "А что тогда случилось у цыпочки?"

    imgd 24406
    m "Мне... Мне просто стало щекотно..."
    m "Я хорошая цыпочка, Биф..."
    music Groove2_85
    imgf 24407
    biff "Ахахахаха!!!"
    biff "Цекотно?! Ну да, точно!"
    biff "Ты же еще неопытная цыпочка!"
    biff "Хотя это и странно, учитывая откуда ты пришла сюда!"

    imgd 24408
    m "Биф, я могу одеться и идти?"

    imgd 24409
    biff "Цыпочка развеселила папочку и цыпочка может идти!"
    biff "Надеюсь, в следующий раз цыпочка придумает еще что-нибудь интересное..."
    music Power_Bots_Loop
    imgf 22920
    m "..."
    mt "Ненавижу этого придурка!"
    sound snd_fabric1
    fadeblack 1.5
    return


label gallery_24506: #Сесть на стол, достать член Бифа и взять его в рот.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    imgfl 22908
    m "Биф, мне обязательно это делать?"
    biff "Ага. Чем сегодня ты порадуешь папочку?"
    imgf 22909
    mt "Сволочь!"

    m "Я не знаю чем еще порадовать папочку..."
    m "!!!"
    mt "Мерзавец! Он и так уже заставлял меня делать вещи, что хуже некуда!"

    imgd 24410
    biff "У папочки сегодня хорошее настроение."
    biff "Папочка считает что цыпочка уже достаточно долго работает здесь и зарабатывает хорошие деньги."
    biff "И держится подальше от грязных улиц, с которых папочка ее подобрал..."
    music Power_Bots_Loop
    img 24411
    mt "!!!"
    mt "Мерзавец! Это мой офис! Это ты вылез сюда из какой-то грязной дыры!"
    music Groove2_85
    imgf 24412
    biff "Так что папочка решил позволить цыпочке и дальше развлекать его."
    biff "Папочка знает что цыпочка мечтает об этом!"

    imgd 24413
    m "Мечтает о чем???"
    mt "Я мечтаю только о том, чтобы вышвырнуть тебя из этого кресла!"

    imgd 24414
    biff "Цыпочка, залезай на стол. Ха-ха-ха!"
    sound snd_walk_barefoot
    imgf 24415
    m "!!!"
    # Моника ложится на стол
    fadeblack 1.5
    music Loved_Up
    imgfl 24416
    mt "Снова показывать этому мерзавцу свое восхитительное тело!"
    mt "Ненавижу!"

    imgf 24417
    biff "Нет, цыпочка!"
    biff "Садись наоборот! Ха-ха-ха!"

    imgd 24418
    m "В смысле наоборот?"
    m "Что это значит?"
    biff "Лицом к папочке!"

    # Моника садится лицом к Бифу
    # Биф откидывается в кресле
#    sound vjuh3
    fadeblack 1.5
    music Loved_Up
    imgf 24419
    w
    imgd 24420
    m "Биф, это все?"
    m "Я могу идти?"

    imgf 24421
    biff "Цыпочка, останься! Я знаю о чем ты сейчас думаешь!"
    biff "Папочка разрешает тебе!"

    imgd 24422
    m "Разрешает что?!"
    mt "О чем я думаю по его мнению?!"
    mt "Я хочу быстрее закончить это, вот и все о чем я думаю!"

    sound Jump1
    imgf 24423
    biff "Цыпочка, не стесняйся."
    biff "Я ведь знаю ты любишь папочку. За все что он сделал для тебя."

    imgd 24424
    m "В смысле не стесняться?!"
    m "Биф, что ты имеешь ввиду?!"
    m "Я и так перед тобой абсолютно голая!"

    imgf 24425
    biff "Протяни вперед свою ручку!"

    # Моника протягивает
    imgd 24426
    w
    biff "Ниже, цыпочка, ниже!"

    # Моника опускает еще ниже
    imgd 24427
    m "Я не понимаю..."

    biff "Еще ниже, цыпочка! Не стесняйся!"

    imgd 24428
    w
    imgf 24429
    biff "И протяни ее еще дальше!"

    img 24430
    m "Биф, но там..."

    imgf 24431
    biff "Да, цыпочка! Там моя ширинка!"
    biff "Я заметил, цыпочка все время на нее смотрит!"
    music Power_Bots_Loop
    img 24432 hpunch
    m "ЧТО?! НЕТ!"
    music Groove2_85
    imgd 24433
    biff "Да, хорошая цыпочка не будет стесняться и расстегнет папочке брюки!"

    img 24434
    m "Нет, БИФ! Зачем?!"

    imgf 24435
    biff "У папочки хорошее настроение! Скорее, сделай это пока оно не упало!"
    sound Jump1
    imgd 24436
    m "Но Биф! Я ведь работаю просто моделью!"

    imgf 24437
    biff "Ты работаешь куклой, которая похожа на Монику Бакфетт!"
    biff "И ты хорошая цыпочка, потому я тебе плачу такие деньги!"

    imgd 24438
    m "!!!"

    biff "Мое настроение начинает падать..."

    imgf 24439
    menu:
        "Расстегнуть ширинку Бифу.":
            pass
    music Power_Bots_Loop
    mt "Дьявол! Мне что, придется расстегивать ширинку у какого-то мерзавца, который сидит в моем кресле?!"
    mt "Ладно... Я сделаю это и сразу уйду..."
    fadeblack 1.5
    music Loved_Up
    # Моника расстегивает ширинку
    imgfl 24442
    biff "Да, цыпочка, вот так..."
    sound snd_zip
    imgf 24440
    biff "Осторожно... Медленно..."
    imgd 24441
    biff "Это член папочки. Это очень важная вещь в твоей жизни!"

    sound Jump1
    imgd 24443
    biff "Да, цыпочка! Видишь какое у папочки приподнятое настроение!"
    biff "Это потому, что папочка придумал чем цыпочка может его развеселить!"
    music Hidden_Agenda
    imgf 24444
    m "Биф, я сделала что ты просил. Я могу идти?!"
    music Groove2_85
    imgd 24445
    biff "Цыпочка, я хочу чтобы ты притворилась Моникой Бакфетт!"
    biff "Я плачу тебе за это и хочу увидеть как хорошо ты это делаешь!"
    biff "Я хочу чтобы ты сказала как тебя зовут и что ты хочешь попосать член у папочки!"
    biff "В ее бывшем кабинете!"

    img 24446 vpunch
    m "Моника Бакфетт такого никогда бы не сказала!!!"

    imgf 24447
    biff "Да, я слышал что она была еще той сучкой!"
    biff "Но очень хорошо что вместо нее у меня есть такая послушная кукла, похожая на нее!"
    music Power_Bots_Loop
    img 24448 hpunch
    m "Нет!"
    music Groove2_85
    imgd 24449
    biff "Давай цыпочка! Папочка ждет!"
    fadeblack 1.5
    music Power_Bots_Loop
    imgfl 24450
    m "Биф, я не хочу этого делать!"

    imgf 24451
    biff "Ты делала это сотни раз на улице, дешевая кукла!"
    biff "И теперь ты хочешь сказать папочке НЕТ???"

    imgd 24452
    m "Биф! Я..."
    music Pyro_Flow
    imgf 24453
    mt "Что мне сказать???"
    mt "Как я могу пойти на такую мерзость???"
    mt "Но я знаю что будет если я откажусь!"
    mt "Он выгонит меня из моего же офиса и перестанет платить деньги за эти ужасные фотосессии!"
    mt "И тогда мне конец!"
    music Groove2_85
    imgd 24454
    biff "Или ты уже сегодня сосала кому-то другому и не хочешь испачкать папочкин член чужой спермой?"
    music Power_Bots_Loop
    img 24455 hpunch
    m "Я..."
    mt "ЧТО?! КОМУ-ТО ДРУГОМУ???"
    mt "Он что, считает что я похожа на какую-то шлюху, которая делает это направо и налево?!"
    music Stealth_Groover
    imgd 24456
    mt "Я - Моника Бакфетт!"
    mt "Я глава этой компании!"
    mt "Да, я нахожусь в трудном положении из-за какого-то временного недоразумения!"
    mt "Но, клянусь, я верну все назад!"
    mt "Потому что Я - Леди!!!"
    mt "Я самая умная и богатая леди этого города!!!"
    music Groove2_85
    imgf 24457
    biff "Ну так что, цыпочка!"
    biff "Отвечай скорее!"
    biff "У хорошей цыпочке есть только два варианта!"
    imgd 24527
    w
    sound Jump2
    imgd 24458
    biff "Либо она уже сосала член кому-то еще, либо она Моника Бакфетт, которая хочет пососать член у папочки!"
    music Pyro_Flow
    img 24459 hpunch
    m "!!!"

    biff "Отвечай быстрее! Счтиаю до трех!"

    imgd 24460
    w
    with vpunch
    biff "Раз!"

    m "Биф, давай я не буду делать этого!"

    img 24461 vpunch
    biff "Два!"

    imgd 24462
    m "Давай я сделаю это в другой раз или... черт!"

    img 24463 vpunch
    biff "Три!"
#    $ menu_corruption = [0, biffCastingTableBlowjobOption1, biffCastingTableBlowjobOption2]
    menu:
        "Убежать...":
            imgd 24464
            m "Нет! Я не буду этого делать!"
            m "И я не буду ничего говорить!"
            biff "Ты плохая цыпочка!"
            biff "Я запрещаю тебе появляться в офисе две недели!"
            biff "Пошла вон!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_run2
            pause 2.0
            return

        "Я уже сегодня сосала член другому мужчине, поэтому не хочу пачкать член папочки...":
            imgd 24465
            mt "Дьявол! Я не хочу трогать его вонючий отросток!"
            mt "Я скажу что угодно, лишь бы не делать этого!"
            mt "В конце концов, это просто сотрясание воздуха, просто слова!"
            music Hidden_Agenda
            imgf 24466
            m "Я... Я уже сегодня... Я..."
            imgd 24467
            biff "Говори быстрее! Папочка ждет!"
            imgd 24468
            m "Я сегодня уже..."
            m "Я уже делала это... делала это другому мужчине..."
            imgf 24469
            biff "Что ты делала другому мужчине, цыпочка?!"
            imgd 24470
            m "Я... Я сосала его член..."
            mt "О БОЖЕ!"
            imgf 24471
            biff "И? Что дальше?"
            imgd 24472
            m "И я... Я не хочу пачкать папочку..."
            music Groove2_85
            imgf 24473
            biff "Аха-ха-ха!!!"
            biff "Папочка не удивлен!"
            biff "Папочка знает что цыпочка - двадцатидолларовая шлюха!"
            biff "Шлюха неплохо зарабатывает в последнее время, но не может изменить своих привычек! Ха-ха!"
            m "!!!"
            fadeblack 1.5
            music Groove2_85
            imgd 24474
            sound snd_zip
            w
            imgd 24475
            biff "Однако, папочка любит честность..."
            biff "Но цыпочка должна учесть, что если она хочет и дальше нравиться папочке, то трахаться она должна только с папочкой!"
            biff "Или с инвесторами! Или еще с кем-то, с кем папочка скажет!"
            biff "Может быть ты не заметила, но твой ротик и твоя задница теперь стоят несколько дороже двадцати долларов, ха-ха-ха!"
            biff "Можешь идти, на сегодня ты достаточно рассмешила папочку!"
            music Power_Bots_Loop
            imgf 24476
            m "Мерзавец! Ненавижу!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_short_walk
            pause 2.0
            return
        "Я - Моника Бакфетт...":
            pass

    imgd 24477
    mt "Этот жалкий Биф даже не представляет мою ситуацию!"
    music Groove2_85
    imgd 24478
    biff "Ну, что молчишь?!"
    biff "Папочка ждет!"
    fadeblack 1.5
    music Groove2_85
    imgf 24479
    mt "Не могу поверить что я делаю это прямо в своем же кабинете..."
#    sound vjuh3
    imgd 24481
    w
    imgf 24482
    mt "Делаю это какому-то мерзавцу, который сидит в моем кресле..."
    imgd 24483
    mt "Как до этого могло дойти?"
    imgd 24484
    mt "Моника, я не верю во все происходящее..."
    mt "Это какой-то сон!"

    img 24485 vpunch
    biff "НУ?!"

    fadeblack 1.5
    music Loved_Up
    imgd 24486
    m "Я..."
    m "Меня зовут..."
    m "Меня зовут Моника Бакфетт..."
    m "Это... мой бывший кабинет..."
    imgd 24487

    m "..."
    imgf 24488
    biff "И???"
    music Power_Bots_Loop
    imgd 24489
    m "!!!"
    imgd 24490
    biff "!!!"
    music Groove2_85
    imgf 24491
    m "И я хочу пососать член папочки..."

    imgd 24492
    biff "Да, цыпочка! Наконец-то!"
    biff "Папочка разрешает тебе!"
    biff "Можешь приступать!"
    fadeblack 1.5
    music Loved_Up
    imgf 24493
    w
    imgd 24494
    w
    imgf 24495
    w
    imgd 24496
    mt "Я не верю... Я не верю..."

    imgf 24497
    w

    # Моника начинет делать минет
    sound hlup21
    imgd 24498
    w

    imgf 24499
    biff "Давай цыпочка, не стесняйся!"
    biff "У тебя внутри еще много места!"
    sound lick3
    imgd 24500
    biff "О Да!"

    $ localSoundVolume = 1.0
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_1 = Movie(play="video/v_Monica_Biff_Blowjob1_1.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Моника делает минет
    imgf 24501
    biff "Я буду представлять что сама Моника Бакфетт сосет папочкин член! О Да!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_2 = Movie(play="video/v_Monica_Biff_Blowjob1_2.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    music Loved_Up2
    imgd 24502
    w
    imgf 24503
    biff "У цыпочки маловато опыта!"
    biff "Отсасывая члены на улице за двадцать долларов она почти ничему не научилась!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_3 = Movie(play="video/v_Monica_Biff_Blowjob1_3.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_3
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 24504
    biff "Но я сделаю из тебя хорошую цыпочку!"
    biff "Я расскажу тебе как правильно поднимать настроение папочке!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_4 = Movie(play="video/v_Monica_Biff_Blowjob1_4.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound lick3
    imgf 24505
    biff "О Да!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_5 = Movie(play="video/v_Monica_Biff_Blowjob1_5.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_5
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 24506
    biff "Да, еще! Папочке нравится так! Да!"
    biff "Еще! Еще!"

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_6 = Movie(play="video/v_Monica_Biff_Blowjob1_6.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_6
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.166666666666667) + " loop 0.0>Sounds/v_Monica_Biff_Blowjob1_1.ogg"
    scene black
    image videov_Monica_Biff_Blowjob1_7 = Movie(play="video/v_Monica_Biff_Blowjob1_7.mkv", fps=30)
    show videov_Monica_Biff_Blowjob1_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 24507
    menu:
        "Кончить на лицо Моники.":
            img 24508
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            biff "Ааааааааа!!!"
            img 24509
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            sound squelch9
            imgd 24510 #хлюп :)
            w
            fadeblack 1.5
            music Groove2_85
            imgfl 24511
            m "!!!"
            mt "Отвратительно!!!"
            sound snd_zip
            imgf 24512
            biff "Цыпочка хорошо постаралась..."
            biff "Цыпочка, скажи, тебе понравился член папочки?"
            imgd 24513
            mt "Мерзавец! Это отвратительно!"
            menu:
                "Сказать что член папочки понравился.":
                    fadeblack 1.5
                    music Hidden_Agenda
                    imgf 24514
                    m "Да... Папочка... Мне понравился твой член..."
                    music Groove2_85
                    imgd 24515
                    biff "Хорошо, цыпочка!"
                    biff "Ты можешь идти."
                    biff "Папочка скоро снова нагуляет аппетит."
                    biff "Цыпочка должна не забыть развлечь его!"
                "Уйти.":
                    pass

            music Power_Bots_Loop
            imgf 24516
            m "Мерзавец! Ненавижу!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_short_walk
            pause 2.0

        "Кончить в рот Моники.":
            sound Jump1
            img 24517 hpunch
            sound chavc6
            biff "Иди к папочке! Ближе!"
            imgd 24518
            biff "Да, вот так!"
            img 24519
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            biff "Ааааааааа!!!"
            img 24520 #хлюююююп :) bulk(?)
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan1
            w
            fadeblack 1.5
            music Groove2_85
            imgfl 24521
            m "!!!"

            mt "Отвратительно!!!"

            sound snd_zip
            imgf 24523
            biff "Цыпочка хорошо постаралась..."
            biff "Цыпочка, скажи, тебе понравился член папочки?"

            imgd 24522
            mt "Мерзавец! Это отвратительно!"
            menu:
                "Сказать что член папочки понравился.":
                    fadeblack 1.5
                    music Hidden_Agenda
                    imgf 24524
                    m "Да... Папочка... Мне понравился твой член..."
                    m "Мпффф, мпфффф..."
                    music Groove2_85
                    imgd 24525
                    biff "Хорошо, цыпочка!"
                    biff "Ты можешь идти."
                    biff "Папочка скоро снова нагуляет аппетит."
                    biff "Цыпочка должна не забыть развлечь его!"
                "Уйти.":
                    pass

            music Power_Bots_Loop
            imgf 24526
            m "Мерзавец! Ненавижу!"
            fadeblack
            sound snd_fabric1
            pause 2.0
            sound highheels_short_walk
            pause 2.0
    return

label gallery_30118:
    # Моника с Биффом заходят в ресторан, там много гостей и репортеров
    # Монику освещают вспышки камер, она позирует и чувствует себя как рыба в воде
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Backbay_Lounge
    img 30118
    with fadelong
    show screen Reporters_Shoots_Screen()
    w
    img 30119
    with fade
    mt "В этот вечер я буду наслаждаться своей настоящей жизнью."
    mt "Наконец-то вкусно поем приличной еды и выпью дорогого вина..."
    mt "А вокруг меня будут крутиться журналисты и мои поклонники..."
    mt "Черт! Я заслужила возможность побыть собой настоящей!"
    # Бифф наклоняется к ней
    hide screen Reporters_Shoots_Screen
    show screen Reporters_Shoots_Screen2()
    img 30120
    with diss
    sound man_steps
    w
    music Groove2_85
    img 30121
    with fade
    hide screen Reporters_Shoots_Screen2
    biff "Цыпочка, ты помнишь о том, что ты должна быть хорошей..."
    biff "И не расстраивать папочку?"
    img 30122
    with diss
    biff "Сейчас цыпочка пойдет и пообщается с гостями."
    biff "Тебе нужно открывать свой рот и говорить только правильные вещи."
    biff "Для этого цыпочке не обязательно уметь разговаривать."
    img 30123
    with diss
    m "???"
    img 30124
    with fade
    biff "Что ты на меня так смотришь?"
    biff "Я знаю, что у тебя нет мозгов."
    img 30125
    with diss
    biff "Поэтому когда не знаешь, что сказать - молчи."
    biff "Когда ты молчишь, ты больше похожа на Монику Бакфетт."
    img 30126
    with diss
    m "..."
#    biff "И не забудь: если поставишь пятно на платье - заставлю снять трусики."
    img 30127
    with fade
    w
    sound Jump2
    img 30128
    with hpunch
    biff "Все, иди. Папочка будет за тобой присматривать."
    img 30129
    with diss
    biff "Представь, что ты не двадцатидолларовая шлюха..."
    biff "Какой и являешься на самом деле. Ты - Моника Бакфетт."
    # Моника смотрит на него свысока
    music Backbay_Lounge
    img 30130
    with fade
    mt "Пусть этот болван говорит, что хочет."
    mt "Я буду наслаждаться и ничего не сможет испортить мне настроение."
    # Биф отходит от нее
#    $ log1 = t_("Пообщаться с гостями.")
    return

label gallery_18306:
    # перед столом Бифа семь стульев, на стене экран
    # Биф, как в прошлый раз, стоит возле экрана
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    imgfl 15909
    m "Я пришла..."
    imgf 15910
    biff "А, цыпочка!"
    biff "Ты где ходишь?!"
    biff "Инвесторы придут с минуты на минуты!"
    m "..."
    imgd 18253
    biff "Давай, быстрее!"
    biff "Я приготовил наряд для тебя..."
    # но тут Биф прерывается на полуслове, т.к. заходят инвесторы
    # Биф наклоняется к Монике и недовольно говорит
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 0.5
    sound man_steps
    pause 0.5
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 18254
    w
    imgf 18255
    biff "Черт! Ты теперь не успеешь переодеться!"
    biff "Где тебя носило все это время?! Не могла прийти пораньше?!"
    m "..."
    mt "Да пошел ты, сволочь!"
    mt "!!!"
    imgd 18256
    biff "Ладно, будешь выступать в этом."
    biff "Надеюсь, ты компенсируешь свой скучный вид тем, что будешь показывать и говорить..."
    biff "Ну или другими талантами, которых у тебя не так много..."
    biff "Кроме сосания членов за 20 баксов."
    music Power_Bots_Loop
    img 18257
    mt "Мерзавец!"
    mt "!!!"
    # Биф поворачивается к входящим инвесторам и улыбается
    music Groove2_85
    sound man_steps
    imgf 18258
    biff "Добрый вечер, господа!"
    biff "Рады вас видеть!"
    biff "Присаживайтесь, пожалуйста."
    # затемнение, звук мужских шагов
    # смена кадра
    # Моника в своем рабочем костюме стоит перед экраном
    # инвесторы сидят на стульях и смотрят на нее
    # Биф либо стоит сбоку от Моники, либо сидит в своем кресле
    # на экране кадр с фотосессии в костюме Черный лебедь
    # Моника про себя в панике
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    # экран investors_1_2
    imgfl 18259
    w
    sound camera_lens1
    imgf 18260
    mt "Неужели этот кретин Биф собирается показать все кадры оттуда?!"
    mt "В том числе и последние?!"
    music Villainous_Treachery
    imgd 18261
    mt "!!!"
    mt "И все эти неудачники будут смотреть на ЭТО?!"
    mt "?!?!?!"
    # инвестор, который был в номере отеля, когда Моника работала реквизитом, внимательно смотрит на нее
    music Groove2_85
    imgf 18262
    investor3 "..."
    imgd 18263
    mt "..."

    # если Моника работала реквизитом Линды в номере отеля
    if monicaEscortLindaTable1 == True:
        #
        $ notif(t_("Моника работала реквизитом Линды в номере отеля Ле Гранд."))
        #
        imgf 18264
        mt "Почему этот неудачник так смотрит на меня?!"
        mt "Вдруг он меня узнает?!"
        mt "А потом расскажет об этом всем!"
        mt "!!!"
    if monicaEscortLindaTable3 == True:
        # если Моника ударила инвестора в номере отеля
        #
        $ notif(t_("Моника ударила инвестора и убежала из номера."))
        #
        music Power_Bots_Loop
        imgd 18264
        mt "Надо было ударить его не только по яйцам, но и по голове!"
        mt "Чтобы у него отшибло память!"
        mt "!!!"

    # Моника переводит взгляд на Бифа, тот самодовольно улыбается
    music Groove2_85
    imgf 18265
    biff "Можете начинать, Миссис Бакфетт."
    imgd 18266
    mt "Ненавижу скотину Бифа!!!"
    mt "!!!"
    # Филипп смотрит на Монику с мерзкой ухмылочкой
    imgf 18267
    philip "Да, Миссис Бакфетт."
    philip "Мы с нетерпением ждем Вашей презентации."
    if monica_philip_visited_last_day > 0:
        # если Моника работает у него субботней шлюхой
        #
        $ notif(t_("Моника работает у Филиппа субботней шлюхой номер 2."))
        #
        music Power_Bots_Loop
        imgd 18268
        mt "Ненавижу мерзавца Филиппа!"
        mt "Отвратительный самодовольный жадный извращенец! Как и все они!"
        mt "!!!"
    else:
        # если не работает шлюхой, и не было сцены в туалете ресторана

        #
        $ notif(t_("Филипп предлагал Монике деньги за секс в ресторане Ле Гранд."))
        #
        imgd 18268
        mt "Это тот мерзкий тип, который постоянно пытается предложить мне какую-нибудь извращенскую гадость!"
        mt "Какой же он отвратительный!"
        #

    # Моника смотрит на экран
    # экран investors_1_2, меняется на
    # экран investors_1_1
    music Groove2_85
    sound camera_lens1
    imgf 18269
    mt "Черт!"
    mt "И как я должна комментировать эти кадры?!"
    music Loved_Up
    imgd 18270
    m "..."
    m "Господа, взгляните на экран..."
    # Моника говорит и кадры меняются
    imgd 18271
    m "Перед вами костюм, разработанный одним из известных дизайнеров нашего города."
    m "Черный лебедь." # кадр
    # меняется на investors_1_3
    sound camera_lens1
    imgd 18272
    m "Посмотрите на то, как прекрасно он смотрится. #он - it" # кадр
    # меняется на investors_1_4
    sound camera_lens1
    imgd 18273
    m "Какие плавные линии..." # кадр
    # меняется на investors_1_5
    sound camera_lens1
    imgd 18274
    m "Какое внимание к деталям..." # кадр
    # меняется на investors_1_6
    sound camera_lens1
    imgd 18275
    m "Этот костюм подчеркивает всю изящность и плавность линий моей... Кхм... Фигуры модели..." # кадр
    # откровенный кадр
    # меняется на investors_1_7
    music Groove2_85
    sound camera_lens1
    imgd 18276
    with hpunch
    investor2 "Ого!"
    investor4 "Ух ты!"
    music Power_Bots_Loop
    imgd 18277
    mt "!!!"
    mt "Биф мерзавец!" # гневно смотрит на Бифа
    music Hidden_Agenda
    imgd 18278
    biff "Продолжайте, Миссис Бакфетт..." # мерзко улыбается
    music Groove2_85
    imgf 18279
    m "На этом кадре..."
    m "..."
    m "Раскрывается вся... Вся красота и женственность модели..."
    m "А этот изысканный костюм ее выгодно подчеркивает... #ее - it" # кадр
    m "!!!"
    img 18280 hpunch
    mt "Я убью мерзавца Бифа!!!"

    # кадры фотосессии в костюме Черный лебедь меняются на кадры в платье Королева сердец
    # меняется на investors_1_8
    sound camera_lens1
    imgf 18300
    mt "Наконец-то, он сменил эти ужасные кадры!"
    mt "Я сейчас сгорю от стыда, О БОЖЕ!"
    mt "!!!"
    imgd 18301
    m "Эта серия фотографий была сделана благодаря Мистеру Кэмпбеллу."
    m "Который предоставил платье 'Королева сердец' из своей новой коллекции."
    m "Посмотрите на экран..."
    # меняется на investors_1_9
    sound camera_lens1
    imgd 18302
    m "Мы видим перед собой уверенную в себе, красивую, современную женщину без комплексов..."
    # меняется на investors_1_10
    sound camera_lens1
    imgd 18303
    m "Такой, как она, в глубине души мечтает стать любая женщина." # новый кадр
    # меняется на investors_1_11
    sound camera_lens1
    imgd 18304
    m "Такой женщиной, как она, мечтает обладать любой мужчина." # новый кадр
    m "Посмотрите на следующий кадр..."
    # меняется на investors_1_12
    sound camera_lens1
    imgd 18305
    m "На следующем кадре мы видим, что она постепенно раскрывается..." # новый кадр, откровеннее
    # меняется на investors_1_13
    sound camera_lens1
    imgd 18306
    m "Показывая нам свою уверенность, раскованность и сексуальность." # новый кадр
    music Loved_Up
    imgd 18307
    steve "Вау!"
    steve "Миссис Бакфетт, шикарные кадры!"
    imgf 18308
    investor4 "Поддерживаю..."
    investor3 "Это настоящее искусство, Миссис Бакфетт."
    imgd 18309
    investor2 "А меня больше восхищает Ваша смелость и раскованность, Мэм..."
    # Моника натягивая улыбку
    imgf 18310
    m "Благодарю вас, господа..."
    music Power_Bots_Loop
    img 18311 hpunch
    mt "О БОЖЕ!"
    mt "Они рассматривают эти ужасные кадры!"
    mt "!!!"
    fadeblack 2.0
    music Groove2_85
    imgfl 18312
    m "На этом кадре очень удачно выбран ракурс, раскрывающий всю красоту и оригинальность платья." # новый кадр
    imgd 18314
    mt "Моника, какой бред ты несешь!"
    mt "!!!"
    imgf 18313
    m "С этим номером журнала зафиксировано рекордное количество продаж."
    m "Тираж разошелся в кратчайшие сроки."
    m "И рост продаж продолжает увеличиваться с каждым новым номером."
    m "..."
    img 18315
    biff "???"
    m "!!!"
    # Шепчет
    img 18316 vpunch
    biff "Ну же, кукла! Ты помнишь сценарий!"
    imgd 18317
    m "В ближайшем будущем мы планируем провести фотосессию с привлечением модели мужчины."
    m "Что, несомненно, сделает кадры более... Более интересными для любой аудитории."
    # Биф вскакивает и перебивает Монику
    imgd 18318
    biff "Благодарю, Миссис Бакфетт."
    biff "А теперь я хочу дать слово нашему многоуважаемому мистеру Кэмпбеллу..."
    biff "Чье платье было представлено для проведения фотосессии."
    # Моника отходит немного в сторону, Кэмпбелл выходит к экрану
    sound man_steps
    imgf 18319
    w
    imgd 18320
    campbell "Эта фотосессия дала рост продаж моей дизайнерской одежды."
    campbell "Значительно увеличилась прибыль и возросла клиентская база."
    # кадр с фотосессии меняется на график
    # campbell_chart
    sound camera_lens1
    imgf 18321
    campbell "Вы можете посмотреть на график, представленный моими аналитиками."
    campbell "Это график продаж."
    campbell "На нем можно наблюдать резкий скачок в день выхода номера с Миссис Бакфетт в платье 'Королева сердец'. #нем - it"
    imgd 18322
    campbell "Господа, это действительно выгодная сделка."
    campbell "По расчетам моих аналитиков мои вложения полностью окупятся..."
    campbell "Причем за более краткие сроки, чем можно было предполагать."
    # инвесторы заинтересованы
    imgf 18323
    investor4 "Перспективы достаточно заманчивы..."
    investor2 "Да, рост продаж впечатляющий, Мистер Кэмпбелл."
    philip "Я, честно сказать, несколько удивлен..."
    investor3 "Мистер Кэмпбелл, действительно ли платье предоставлялось из Вашей последней коллекции?"
    imgd 18324
    campbell "Да. Это лимитированная коллекция для особых случаев."
    campbell "И я совсем не ожидал к ней такого интереса покупателей. #ней - it"
    campbell "Я вижу в этом заслугу Миссис Бакфетт..."
    campbell "Которая сделала такую великолепную фотосессию."
    # включается следующий слайд, где Моника сидит с широко раздвинутыми ногами
    # меняется на investors_1_13
    # Кэмпбелл заканчивает свою речь
    sound camera_lens1
    imgf 18326
    campbell "Я лично контролировал проведение фотосессии..."
    campbell "Хочу сказать, что остался очень доволен работой команды этого журнала."
    # Моника зло смотрит на Бифа, он довольно улыбается
    music Power_Bots_Loop
    img 18325
    mt "Биф! Ублюдок!"
    mt "!!!"
    # Биф подходит к Кэмпбеллу
    music Groove2_85
    imgf 18327
    biff "Спасибо, Мистер Кэмпбелл. Отличная речь!"
    biff "Господа! Добавлю, что Миссис Бакфет готова сотрудничать в любом формате."
    imgd 18328
    investor3 "Действительно ли это так, Миссис Бакфетт?"
    philip "Миссис Бакфетт, это Ваше следование новому курсу журнала не является притворством?"
    # Моника вынуждена сказать что нет и что
    music Pyro_Flow
    imgf 18329
    mt "Чертов Филипп!"
    mt "!!!"
    mt "Может, сказать им всю правду?"
    mt "Сказать, что Биф меня заставляет, угрожая увольнением?"
    mt "..."
    imgd 18330
    mt "Нет, мне лучше заручиться поддержкой одного из них."
    mt "Как я и планировала ранее."
    mt "Это будет лучший способ вышвырнуть Бифа из МОЕГО кресла!"
    mt "..."
    menu:
        "Это не притворство.":
            pass
    fadeblack 1.5
    music Groove2_85
    imgfl 18331
    m "..."
    m "Это не притворство, Мистер Филипп, я..."
    # Биф снова ее перебивает
    biff "Мы с Миссис Бакфетт хотим доказать вам серьезность наших намерений."
    biff "Господа, прошу вас пройти в фотостудию..."
    biff "Чтобы лично поприсутствовать на фотосессии Миссис Бакфетт в костюме..."
    biff "Который нам любезно предоставил Мистер Кэмпбелл."
    # Биф поворачивается к Монике
    imgd 18332
    biff "Миссис Бакфетт, благодарю вас за выступление перед нашими многоуважаемыми господами."
    biff "Вы можете идти переодеваться к фотосессии."
    # Моника зло на него смотрит
    music Power_Bots_Loop
    img 18333
    mt "Я заставлю тебя, сволочь, молить у меня прощения!"
    mt "За каждый откровенный кадр!"
    mt "И за эти унизительные презентации!"
    mt "Сволочь!"
    mt "!!!"
    # Моника выходит
    return

label gallery_17406:
    # офис полон сотрудников, несколько из них (серая мышка, близняшки и китаянки Лин) стоят в кучке возле стола
    # они что-то рассматривают на столе и обсуждают
    music Blue_Ska
    img 17404
    with fadelong
    w
    img 17425
    with fade
    w
    img 17405
    with diss
    w1 "Ой... Какой кошмар!!!" # серая мышка
    w3 "А я и не удивлена!" # одна из близняшек
    img 17406
    with diss
    w3 "Это еще только начало!"
    w4 "Да-да! Позже будут публиковать фотографии еще хуже! Вот увидите!" # вторая близняшка
    sound highheels_short_walk
    img 17407
    with fade
    w
    img 17408
    with diss
    w7 "Тихо!" # китаянка Лин
    music Groove2_85
    sound Jump1
    img 17409
    with diss
    w
    # они видят Монику и замолкают, все смотрят на нее
    img 17410
    with fade
    mt "Это еще что такое?!"
    mt "Почему эти никчемные сотрудники так на меня смотрят?!"
    # подбегает подхалим
    music Sneaky_Snitch
    sound man_steps
    img 17411
    with diss
    w5 "Миссис Бакфет! Вы сегодня прекрасно выглядите!" # подхалим Джон
    w5 "Хотите чашечку горячего кофе?"
    music Groove2_85
    img 17412
    with fade
    m "Нет."
    m "Что здесь происходит?!" # сердито
    m "Почему половина офиса не на рабочих местах?!" # включаем большого босса
    # подбегает Гретта
    sound highheels_short_walk
    img 17413
    with diss
    w6 "Миссис Бакфетт, а они сегодня целый день ничего не делают!" # Гретта
    w6 "Только сидят и сплетничают!"
    music Pyro_Flow
    img 17414
    with fade
    m "Так! Быстро все за работу!!!"
    m "Или я уволю вас всех сегодня же!!!"
    m "!!!"
    music Groove2_85
    img 17415
    with diss
    w5 "Не понятно, за что они деньги получают!"
    w5 "Ничего не делают!"
    w5 "Целый день сегодня сидят и какой-то неприличный журнал обсуждают!"
    # в разговор вмешивается айтишник
    w2 "Гретта, они читают наш журнал."
    w2 "В котором мы работаем."
    w5 "А? Наш?!"
    music Loved_Up
    img 17416
    with fade
    w2 "Кстати, Миссис Бакфетт..."
    w2 "Отличная фотосессия получилась!"
    img 17417
    with diss
    w5 "Согласен на все сто."
    w5 "Это лучшее, что я видел в своей жизни, Миссис Бакфетт!"
    img 17418
    with fade
    m "Ты о чем?"
    w5 "Вам очень идет то красное платье..."
    w2 "И корона. Вы как настоящая королева на снимках."
    # Моника сначала не понимает, о чем они, но постепенно до нее доходит
    music Groove2_85
    img 17419
    with diss
    mt "Красное платье и корона?"
    mt "???"
    mt "?!?!?!"
    music stop
    sound plastinka1b
    img 17420
    with hpunch
    mt "ЧТОООООО?!"
    # шок, злость
    # потом орет на всех
    music Power_Bots_Loop
    img 17421
    with fade
    m "Быстро все за работу!!!"
    m "!!!"
    m "Бездельники!!!"
    m "!!!!!"
    # идет в свой кабинет
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Pyro_Flow
    img 17422
    with fadelong
    mt "Боже!"
    mt "Какой кошмар!"
    mt "Теперь все эти никчемные сотрудники видели мои фото с той ужасной фотосессии!!!"
    mt "!!!"
    img 17423
    with fade
    mt "Это все Бифф!"
    mt "Если бы не его дурацкая смена курса журнала!"
    mt "Никто и никогда не увидел бы подобных фотографий Моники Бакфетт!"
    mt "Потому что их не было бы!!!"
    mt "!!!"
    img 17424
    with diss
    mt "Я ненавижу этого мерзавца Биффа!"
    mt "Ненавижу!"
    mt "Убью его!"
    mt "!!!"
    mt "!!!!!!"
    return

label gallery_31476:
    # Клэр и Моника заходят в рабочий кабинет Моники
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 31453
    w
    imgf 31454
    m "Проходи, Клэр."
    m "Это мой рабочий кабинет."
    # Клэр спокойно отвечает
    clare "Ого! Мне здесь нравится."
    clare "А это твое кресло?"
    m "Да. Временное."
    # Моника поворачивается и указывает на Юлию
    imgd 31455
    m "А это моя личная помощница Юлия."
    m "Юлия, это Мисс Клэр. Она моя коллега."
    julia "Добрый день, Миссис Бакфетт, Мисс Клэр."
    julia "Приятно с вами познакомиться."
    clare "Мне тоже очень приятно, Юлия."

    # заходит Джон, несет чашки с чаем (как в сцене с Викторией)
    fadeblack
    sound snd_door_open1
    pause 1.5
    sound snd_door_locked1
    sound2 man_steps
    pause 2.0
    music Sneaky_Snitch
    imgfl 31456
    w5 "Миссис Бакфетт, Мисс Клэр, ваш чай готов."
    m "Хорошо, Джон. Поставь его на столик и можешь идти."
    w5 "Да, Миссис Бакфетт, как скажете."
    w5 "Приятного чаепития."
    # Моника указывает рукой в сторону комнаты отдыха
    sound snd_plates
    imgf 31457
    m "Клэр, пойдем сюда."

    # смена кадра
    # Моника и Клэр сидят на диванчике и пьют чай, Юлия за своим столом, косится на них и подслушивает
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 31467
    w
    imgf 31474
    w
    imgd 31475
    m "Это и есть мой офис, Клэр."
    m "Конечно, я показала тебе лишь малую его часть..."
    clare "Это все - лишь малая часть?!"
    m "Да, всего один небольшой отдел."
    m "Возможно, как-нибудь я тебе покажу свой офис полностью."

    # смена кадра, айтишник
    # показываем айтишника за его рабочим столом
    fadeblack 2.0
    music Marty_Gots_a_Plan
    imgfl 31470
    w
    # следом показываем монитор айтишника
    # на его компе вид из-под стола Моники с комнаты отдыха
    sound keyboard_click
    imgf 31486
    w
    # он через камеру подсматривает за ними, вертя камеру из стороны в стороны
    sound keyboard_click
    imgd 31471
    w2t "Что моя бывшая училка здесь делает?"

    # звук бзззз - камера передвигается и показывает то Монику, то Клэр
    imgf 31478
    w
    imgd 31468
    w
    sound camera_zoom
    imgd 31469
    w
    imgf 31479
    w
    fadeblack 2.0
    music Stealth_Groover
    # смена кадра, комната отдыха
    # если Моника рассказала Клэр правду о себе (диалог в лейбле ep210_dialogues4_dance_strip_2)
    if monicaClareStoryAboutLife == True:
        #
        $ notif(t_("Моника рассказывала Клэр правду о себе"))
        #
        imgfl 31476
        clare "Теперь я понимаю, почему ты готова пойти на многое, чтобы вернуть все это."
        clare "Мне нравится твоя целеустремленность, Моника."
        #
    else:
        # если Моника солгала Клэр про спор с подругами
        #
        $ notif(t_("Моника говорила Клэр, что работает в баре из-за спора с подругами"))
        #
        imgfl 31476
        clare "Хммм..."
        clare "Теперь я понимаю, почему ты решила поспорить со своими подружками, Моника."
        #
    imgf 31477
    m "Я рада, что ты меня понимаешь."
    clare "Понимаю и поддерживаю, Миссис Бакфетт."

    # смена кадра, айтишник
    # звук бзззз - камера передвигается и показывает то Монику, то Клэр
    fadeblack 2.0
    music Marty_Gots_a_Plan
    imgfl 31490
    w
    imgf 31468
    w
    sound camera_zoom
    imgd 31469
    w
    imgd 31491
    w
    sound keyboard_click
    imgf 31488
    w
    imgd 31487
    w2t "А у нашего Босса аппетитная киска!"
    w2t "Жаль, что я не слышу, о чем они разговаривают."
    w2t "Надо будет установить звук."

    # смена кадра, комната отдыха
    # Клэр улыбается Монике, ставит чашечку на столик
    fadeblack 2.0
    music Stealth_Groover
    imgf 31480
    clare "Моника, спасибо за чай."
    clare "Я с удовольствием погостила бы еще немного, но..."
    clare "К сожалению, у меня мало времени и мне нужно идти."
    # обе встают, Клэр направляется к выходу
    sound highheels_short_walk
    imgd 31481
    m "Я тебя провожу, Клэр."
    # Моника поворачивается в сторону Юлии
    m "Юлия, убери со стола чашки."
    m "Пожалуйста."
    julia "Хорошо, Миссис Бакфетт."
    # Юлия вскакивает со своего рабочего места и подходит к столу
    fadeblack
    sound highheels_short_walk
    pause 1.5

    # если Моника состоит в отношениях с Юлией
    # то Юлия подходит к столику и быстро чмокает Монику в щечку
    if monicaJuliaLoveStory8 == True:
        music Loved_Up
        imgfl 16506
        w
        sound snd_kiss2
        imgf 16508
        #
        $ notif(t_("Моника состоит в отношениях с Юлией"))
        #
        imgd 31482
        m "Юлия, милая."
        m "Нас могут увидеть."
        julia "Просто я соскучилась, Миссис Бакфетт."
        julia "А почему Вы сказали, что Мисс Клэр Ваша коллега?"
        julia "Разве она работает в Вашем журнале?"
        music Hidden_Agenda
        mt "Черт!"
        m "Нет, она..."
        m "Она, как и мы, работает в сфере искусства."
        # Моника наклоняется и чмокает Юлию в щечку, Юлия довольно улыбается
        sound snd_kiss2
        imgd 31483
        w
    # Моника выходит вслед за Клэр

    # Юлия подходит к столику и наклоняется за чашками
    music Groove2_85
    imgf 31484
    sound snd_plates
    w
    # смена кадра, айтишник
    # звук бзззз - Юлия приседает забрать чашки и айишнику видно, что она без трусиков
    if ep212_monica_known_julia_panties_color == True:
        fadeblack
        sound camera_zoom
        pause 2.0
        music Marty_Gots_a_Plan
        imgfl 31485
        w
        imgf 31489
        w
        imgd 31472
        w2t "Хмм... Мне кажется или Юлия теперь ходит без трусиков?"
        w2t "Как и Миссис Бакфет..."
    # звук каблуков
    sound highheels_short_walk
    imgd 31473
    w2t "Черт!"
    # затемнение
    return

label gallery_19642:
    # Моника заходит в кабинет Бифа и видит обнаженную Кристину (кассир с заправки)
    # Сбоку стоит улыбающийся Фред.
    # Моника в шоке, возмущенно смотрит на Кристину
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 19638
    w
    img 19639 vpunch
    mt "Какого черта?!"
    music Pyro_Flow
    imgd 19640
    m "Это еще что такое?!"
    m "?!?!?!"
    # потом на Фреда
    imgd 19641
    m "Фред! Мерзавец! Что ты делаешь здесь?!"
    m "Снова плетешь интриги у меня за спиной?!"
    # тычет пальцем в сторону Кристины
    imgf 19642
    m "И почему эта голая кукла торчит посреди кабинета?!"
    m "!!!"
    # Кристина испуганнно прикрывается руками
    sound highheels_run2
    saleswoman "Ой! Это что?! Начальница?!"
    imgd 19648
    w
    fadeblack
    sound highheels_run2
    pause 1.5
    sound snd_door_locked1
    pause 1.5
    music Groove2_85
    # и выбегает из кабинета
    # Фред со своей улыбочкой обращается к Монике
    imgfl 19643
    fred "Миссис Бакфетт, я как профессионал, проявляю инициативу... Помогая расширять модельный пулл."
    fred "А также я помогаю молодым талантам раскрывать себя."
    # Моника зло говорит ему
    music Stealth_Groover
    imgf 19644
    m "Фред! Твое место за рулем автомобиля!"
    m "Границы твоего профессионализма в том, чтобы не путать педали!!"
    m "А инициативу тебе лучше проявлять в том, чтобы заранее заправлять автомобиль керосином!!!" #(в англ. парафин? в общем то же слово что и в первом эпизоде)
    m "Пошел вон отсюда!"
    m "!!!"
    music Groove2_85
    imgd 19649
    sound snd_door_knock
    w
    # Фред ехидно ей улыбается и отворачивается от нее к Бифу
    # звук стук в дверь
    # в кабинет к Бифу заходит Грейс (модель с ивента у Кэмпбелла)
    imgf 19645
    guest2 "Мистер Биф, можно войти? Теперь моя очередь?"
    music stop
    sound plastinka1b
    img 19650 hpunch
    m "?!?!?!"
    music Groove2_85
    imgd 19646
    biff "Подожди еще немного, детка. Я пока занят."
    imgd 19647
    guest2 "Да, конечно, Мистер Биф."
    # Грейс уходит, Моника в недоумении смотрит на Бифа
    fadeblack
    sound snd_door_locked1
    pause 1.5
    music Groove2_85
    imgf 19651
    fred "Я могу идти, Мистер Биф?"
    # Биф отвечает с важным видом, ведь он биг босс
    imgd 19652
    biff "Да, Фред. Можешь идти."
    fred "Спасибо, что уделили время моей инициативе, Мистер Биф."
    biff "Твоя кукла вполне послушная, Фред. Она понравилась папочке."
    biff "Приводи ко мне побольше разных кукол. Аха-ха!!!"
    imgf 19653
    sound man_steps
    w
    # Фред профессионально улыбается и уходит
    # Моника злая смотрит ему вслед
    music Power_Bots_Loop
    imgd 19654
    mt "Мерзавец!!!"
    # потом смотрит на Бифа
    fadeblack
    sound snd_door_locked1
    pause 1.5
    music Pyro_Flow
    img 19655 hpunch
    m "Побольше разных кукол?!"
    m "Что все это значит?!"
    # Биф самодовольно
    music Groove2_85
    imgf 19656
    biff "Это значит, что эта кукла не имеет твоих недостатков, цыпочка!"
    biff "И папочка думает над тем, чтобы теперь она представляла журнал!"
    music Pyro_Flow
    imgd 19657
    m "Что?!"
    m "С какой стати эта глупая кукла будет представлять журнал?!"
    m "Она не имеет ни опыта, ни шарма!"
    m "Ни мозгов!!"
    music Groove2_85
    imgf 12829
    biff "Она имеет главное - это желание работать!"
    biff "Но папочка предусмотрел все варианты..."
    biff "Потому что папочка тут самый умный и заботится о своем журнале."
    imgd 13889
    biff "И если эта глупая кукла не сможет стать его главой..."
    biff "То я назначу на эту должность другую куклу... Поумнее..."
    biff "Она как раз ждет сейчас в приемной своей очереди на собеседование."
    imgf 19658
    m "!!!"
    m "Я и так работаю и прохожу эти твои дурацкие фотосессии!"
    m "Чего тебе еще нужно?!"
    m "?!"
    imgd 12811
    biff "Ты не развлекаешь папочку как требуется, цыпочка..."
    biff "Но это не главное..."
    imgf 12818
    m "..."
    imgd 15902
    biff "Главное то, что до сих пор не решен вопрос с инвесторами!"
    biff "Этому замечательному журналу во главе со мной..."
    imgd 12796
    biff "Дааа... Во главе со мной..."
    biff "Я глава этого журнала... Я люблю себя... Вау..."
    music Power_Bots_Loop
    imgf 15889
    mt "!!!"
    mt "Безмозглый придурок!"
    music Groove2_85
    imgd 13906
    m "К делу, Биф!"
    biff "Так вот! Этому замечательному журналу нужны деньги!"
    imgf 12807
    m "Я провожу твои дурацкие презентации! Что тебе еще от меня надо?!"
    imgd 19659
    biff "Презентаций здесь явно недостаточно!"
    biff "И я ожидал от двадцатидолларовой шлюхи того..."
    biff "Что она проявит свои привычные ей навыки и договорится с инвесторами!"
    # Моника зло спрашивает
    music Pyro_Flow
    imgd 19660
    m "Ты что, хочешь чтобы Я, Моника Бакфетт, трахалась с инвесторами?!"
    m "Ради того, чтобы они согласились инвестировать в этот журнал?!"
    m "?!?!?!"
    music Groove2_85
    imgf 15897
    biff "Слышишь ты, кукла безмозглая!"
    biff "Я смотрю, ты забыла, кто ты такая на самом деле?!"
    biff "Да, это твоя основная работа!"
    biff "Потому я и нанял эту куклу." # тычет пальцем в сторону Моники
    imgd 13900
    m "!!!"
    imgf 19661
    biff "Весь талант этой куклы в том, что она похожа на сучку Бакфетт."
    biff "Папочке нравится, что она любит притворяться ею и вживается в ее образ."
    biff "Однако папочке очень жаль, что эту куклу он подобрал буквально с улицы..."
    imgd 19662
    biff "А это значит, что у нее нет опыта для того, чтобы договориться с инвесторами, как следует."
    biff "Видимо она никогда не общалась с такими богатыми мужчинами."
    biff "Возможно, папочке стоит пригласить кого-нибудь из ВИП-эскорта..."
    biff "Чтобы этой кукле объяснили, где у богача искать член!"
    # Если Моника работает в эскорте
    if monicaHotelAdminAgreement3 == True and ep212_escort_monica_fired == False:
        #
        $ notif(_("Моника работает в ВИП-эскорте."))
        #
        music Stealth_Groover
        imgf 19663
        m "Меня не интересуют падшие особы из каких-то эскортов!"
        m "Они ничего про это не знают!"
        music Groove2_85
        imgd 13910
        biff "Я уверен, что они смогут эту куклу научить чему-нибудь!"
        biff "Пожалуй, я распоряжусь, чтобы сюда пригласили одну из них."
        music Power_Bots_Loop
        imgd 12790
        mt "Сволочь!!!"
        mt "!!!"
        music Groove2_85
        imgf 12796
        biff "Кстати, один из инвесторов упоминал про перспективную кандидатку в наши модели..."
        imgd 12812
        m "Биф..."
        m "Не надо никого приглашать..."
        m "Это приличное место."
        m "И нахождение здесь подобных особ может скомпрометировать его..."
        imgd 13895
        mt "Дьявол! Не хватало еще чтобы сюда притащили одну из тех шлюх из эскорта!"
    music Groove2_85
    imgf 19664
    biff "В общем, кукла, слушай меня!"
    biff "Сегодня со мной говорил один из инвесторов."
    biff "Он проявил интерес к тому, чтобы провести свидание с Моникой Бакфетт..."
    imgd 19665
    biff "В обмен на инвестирование в мой журнал."
    biff "И ты, глупая кукла, притворишься ею и встретишься с ним!"
    music Power_Bots_Loop
    img 19666 vpunch
    m "Нет!!!"
    music Groove2_85
    imgd 15906
    biff "Да! Иначе я вышвырну тебя отсюда! А твое место займет другая кукла!"
    biff "Например, та, которая только что была до тебя здесь!"
    imgf 19667
    m "Она не справится!"
    biff "Она хотя бы попытается это сделать!"
    biff "К тому же, ее услуги стоят значительно дешевле, чем твои!"
    imgd 12785
    biff "Фотосессии с ней обойдутся в разы дешевле! Возможно ей не надо будет платить вовсе!"
    biff "А папочка умеет считать деньги!"
    imgf 15899
    m "Биф, как ты можешь сравнивать ее и меня?!"
    m "Ведь я Леди и глава журнала!"
    imgd 15901
    biff "Главой журнала может быть и она! И совершенно бесплатно!"
    biff "А если не справится та кукла, то есть другая, которая ждет своей очереди в кабинет!"
    imgf 15894
    biff "Я даже, возможно, устрою кастинг между ними двумя... За то кто будет главной этого журнала. Ха-ха!"
    imgd 19668
    mt "Мерзавец!"
    imgf 19669
    m "Но никто не поверит в это!"
    biff "Ты, кукла, передашь одной из них свои полномочия публично!"
    music Power_Bots_Loop
    img 15905 hpunch
    m "Что?!"
    m "НЕТ!!!"
    m "Я никогда не сделаю этого!!!"
    music Groove2_85
    imgf 15906
    biff "За пару тысяч баксов такая кукла, как ты, сделает все, что ей скажут!"
    biff "Говорить ртом для тебя сложнее, чем сосать им члены!"
    biff "Но пара тысяч баксов значительно больше, чем двадцать баксов!"
    imgd 19670
    m "Биф, ты мерзавец!"
    m "!!!"
    imgf 19671
    biff "Кукла, ты меня достала!"
    biff "Завтра же вечером объявишь о своей отставке!"
    biff "А сейчас пошла отсюда вон!"
    music Pyro_Flow
    imgd 12792
    mt "Черт!"
    mt "Мне нельзя терять этот источник дохода!"
    mt "Где я еще смогу доставать деньги для мелкой сикалявки, которая подмяла Дика под свой каблук?"
    mt "И я потеряю доступ к своему офису и шансы вернуть его назад!"
    mt "Что же делать, Моника?!"
    mt "?!?!?!"
    ### отсюда начинается диалог, если Моника отказалась идти на встречу с инвестором
    menu:
        "Попытаться отговорить Бифа.":
            pass
        "Я ни за что на это не соглашусь!":
            imgf 12797
            m "Биф, я не собираюсь участвовать в этом!!!"
            music Groove2_85
            imgd 12811
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не встретишься с этим денежным мешком!"
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя заявить публично о твоей отставке!"
            music Power_Bots_Loop
            imgd 12814
            mt "!!!"
            mt "Чертовы инвесторы! Чертов Биф! Ненавижу их всех!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не согласится на свидание
            return
    # Моника злится
    imgf 15892
    mt "Что мне теперь делать?!"
    mt "Моника, неужели ты способна согласиться на такое?!"
    music Groove2_85
    imgd 19672
    m "Как этот инвестор посмел изъявить желание встретиться с самой Моникой Бакфетт?!"
    imgf 19673
    biff "Инвестор побаивается сучку Бакфетт..."
    biff "Потому мне самому пришлось предложить это."
    # Моника в ярости
    music Power_Bots_Loop
    img 19674 hpunch
    m "Биф, да как ты смел?!"
    m "!!!"
    music Groove2_85
    imgd 19675
    biff "Так, кукла! Хватит! Мне это уже надоело!"
    biff "Если ты не трахнешь инвестора как полагается!"
    img 19676 vpunch
    m "ЧТО?!"
    imgf 19677
    biff "Что слышала!"
    biff "И если он не согласится на вложение денег в журнал!"
    biff "То ты завтра же объявишь об уходе из журнала!"
    # Монику бомбит
    music Power_Bots_Loop
    img 19678 hpunch
    m "Я не какая-то там проститутка, чтобы спать с этим инвестором!!"
    m "!!!"
    music Groove2_85
    imgf 19679
    biff "Ты не проститутка! Ты дешевая двадцатидолларовая шлюха!"
    biff "Быстро пошла переоделась для господина будущего инвестора!!"
    biff "И только попробуй сделать что-то не так!"
    imgd 19680
    biff "Я распоряжусь и ты больше не сможешь войти в этот офис, безмозглая кукла!"
    biff "На твое место уже есть замена! Она станет лицом журнала!"
    biff "А ты отправишься сосать члены у прохожих за несколько баксов!"
    # Моника в ярости
    music Power_Bots_Loop
    imgd 19681
    m "БИФ!"
    # Биф зло
    music Groove2_85
    imgd 19683
    biff "Я сказал хватит!"
    biff "Сейчас же иди переодевайся и спускайся к лифту!"
    biff "Господин инвестор тебя ждет!"
    music Pyro_Flow
    imgd 19684
    m "БИФ!!!"
    biff "БЫСТРО!!!"
#    $ menu_corruption = [monicaBiffInvestorDatingAgree1]
    menu:
        "Согласиться на свидание с инвестором.":
            pass
        "Нет! Ни за что!":
            imgf 12797
            m "Биф, я не собираюсь участвовать в этом!!!"
            music Groove2_85
            imgd 12811
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не встретишься с этим денежным мешком!"
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя заявить публично о твоей отставке!"
            music Power_Bots_Loop
            imgd 12814
            mt "!!!"
            mt "Чертовы инвесторы! Чертов Биф! Ненавижу их всех!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не согласится на свидание
            return
    imgf 12805
    mt "ААААА!!!"
    mt "Ненавижу сволочь Бифа!!!"
    mt "Он мне заплатит за все эти унижения!!!"
    mt "Иначе я не Моника Бакфетт!!!"
    mt "!!!"
    # Моника направляется к выходу из кабинета и в этот момент в кабинет заходит Грейс
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound snd_door_open1
    pause 1.5
    music Groove2_85
    imgfl 19506
    guest2 "Мистер Биф, я могу войти?"
    biff "Да, заходи..."
    imgf 19682
    guest2 "Ой, Миссис Бакфетт, здравствуйте..."
    guest2 "Я и не заметила, что Вы здесь..."
    # Моника злобно на нее смотрит и проходит мимо, ничего не отвечая
    music Power_Bots_Loop
    imgd 19685
    mt "Наивная дура!"
    mt "!!!"
    return

label gallery_19794:
    # Моника с Олафом сидят за столиком, стол сервирован блюдами, стоит вино
    # Моника сидит с высокомерным видом
    fadeblack 1.5
    music Poppers_and_Prosecco
    imgfl 19786
    w
    imgf 19792
    mt "Хм... Этим никчемным Олафом можно легко манипулировать..."
    mt "Он, как послушный медвежонок, будет на все согласен ради меня."
    # Олаф спрашивает Монику
    imgd 19793
    olaf "Миссис Бакфетт, как Вам ужин? Все ли Вам нравится?"
    music Stealth_Groover
    imgf 19794
    m "Я ужинала в местах и получше, Олаф."
    m "Но здесь вполне сносная еда..."
    m "Хоть и не такая изысканная, к которой я привыкла."
    music Poppers_and_Prosecco
    imgd 19795
    olaf "В следующий раз, если Вы позволите, Миссис Бакфетт, я организую все на высшем уровне."
    imgd 19796
    m "..." # кривится
    imgf 19797
    olaf "Могу я предложить Вам вина, Миссис Бакфетт?"
    m "Да, немного..."
    # не показываем, просто звук, как наливают вино в бокал
    # Моника подносит бокал к губам, а Олаф пристально смотрит на нее, сам не пьет
    fadeblack
    sound pour_wine
    pause 2.0
    music Poppers_and_Prosecco

    imgfl 19798
    w
    imgf 19787
    m "Олаф, а вы почему не пьете вина?"
    mt "Он что, хочет меня отравить? Или что-то подсыпать?.."
    # Олаф немного смущен
    imgd 19799
    olaf "Миссис Бакфетт, дело в том... Кхм..."
    olaf "Я не пью, поскольку у меня периодически возникают проблемы с алкоголем."
    music Stealth_Groover
    imgf 19800
    mt "Какой же он все-таки жалкий этот Олаф."
    mt "Зачем он мне это говорит?"
    mt "Он что, не понимает, что мне плевать на него и его слабости?"
    mt "..."
    imgd 19801
    mt "Черт! Но мне нужно сделать вид, что я заинтересована..."
    mt "Нельзя допустить того, чтобы он отказался от своей инвестиции и ушел..."
    mt "Возможно, мне сегодня удастся не выполнять низменные требования Бифа."
    mt "Этот Олаф и так даст согласие на инвестицию."
    mt "В противном случае, если Биф закроет для меня офис, то меня ждет кое-что похуже..."
    # Моника говорит Олафу, плохо изображая интерес
    music Poppers_and_Prosecco
    imgf 19802
    m "Совсем ничего не будете пить, Олаф?"
    olaf "Совсем ничего, Миссис Бакфетт."
    olaf "Я хочу смотреть на Вашу красоту незатуманенным взглядом..."
    imgd 19803
    olaf "И хочу запомнить каждый миг, проведенный с Вами. Это такая честь для меня!"
    olaf "Ваша смелость в ведении бизнеса меня восхищает!"
    imgd 19804
    olaf "Ваша уверенность в себе... Как Вы провели последнюю фотосессию..."
    olaf "Я до сих пор под впечатлением!!"
    olaf "Вы самая прекрасная женщина, которую я когда-либо встречал, Миссис Бакфетт!"
    # Моника со скучающим видом
    imgf 19805
    m "Спасибо, Олаф. Я знаю об этом..."
    m "Я привыкла, что все мужчины вокруг постоянно восхищаются моей красотой... И моим умом."
    imgd 19806
    olaf "И я их прекрасно понимаю, Миссис Бакфетт! Вы - мечта любого мужчины!"
    # Моника молчит и высокомерно улыбается
    imgf 19807
    m "..."
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Pyro_Flow
    # затемнение, несколько минут спустя, звук каблуков
    # к их столику подходят недовольные Мия и Шарлотт (две светские львицы с ивента у Кэмпбелла)
    # Моника удивленно смотрит на них
    img 19808 vpunch
    w
    imgf 19809
    mt "А эти две овцы что тут делают?!"
    mt "Не хватало мне здесь их мерзких физиономий!"
    # Шарлотт (брюнетка) зло шипит на Олафа
    imgd 19810
    guest5 "Мой муж сидит здесь с этой Бакфетт!"
    guest5 "У всех на виду клеется к ней! Кобель!"
    guest5 "Да как ты посмел!"
    # Олаф испуганно
    imgf 19811
    olaf "Шарлотт, дорогая..."
    olaf "Это совсем не то, о чем ты подумала!"
    # Шарлотт зло
    imgd 19812
    charlotte "По твоей морде видно, как ты пускаешь слюни на эту!.. Эту женщину!!"
    charlotte "На вас смотрит весь ресторан!"
    charlotte "Я даже не поверила, когда мне позвонили и сказали, что ты здесь с этой девкой!!!"
    # Моника спокойно и максимально надменно
    music Stealth_Groover
    imgf 19813
    m "Девкой?" # усмешка высокомерная
    m "Я бы на вашем месте не судила других женщин по себе."
    imgd 19814
    charlotte "Что это значит?!"
    imgf 19815
    m "Я с Олафом веду здесь деловые переговоры..."
    m "Так как заинтересована в расширении своего бизнеса..."
    m "Который Я создала САМА и которым руковожу Я."
    m "Я - владелица многомиллионного бизнеса, а не девка."
    m "А вы что из себя представляете?"
    imgd 19816
    m "Молчите?"
    m "Потому что вы - пустое место."
    m "Вы - лишь тень своего мужа."
    m "Ничего не значащая и никчемная девка."
    # подруга Шарлотт, Мия, пытается возмущаться на это
    music Groove2_85
    imgf 19817
    guest6 "Как вы можете так говорить про Шарлотт?!"
    guest6 "Между прочим, ее муж, как и мой, уважаемые и влиятельные люди в нашем городе!"
    charlotte "Да!" # смотрит на Монику свысока
    # переводит взгляд на Олафа
    imgd 19818
    charlotte "И, кстати, муж Мии не таскается по ресторанам с какими-то дев... женщинами! Пусть и очень богатыми!"
    charlotte "Под предлогом деловых переговоров!!!"
    # Моника со скучающим видом
    music Stealth_Groover
    imgf 19819
    m "Можешь засунуть своего мужа куда подальше."
    m "Он для меня - деловой партнер и не более того."
    if monicaBitch == True:
        $ notif_monica()
        # оценивающий взгляд на Олафа
        imgd 19820
        m "С такими уродливыми и толстыми мужчинами меня может объединять только бизнес."
    # Олаф в шоке, смотрит на Монику
    # потом говорит своей жене
    music stop
    sound plastinka1b
    img 19821 hpunch
    w
    music Poppers_and_Prosecco
    imgf 19822
    olaf "Да, дорогая. У нас деловые переговоры."
    olaf "Как ты могла подумать о чем-то другом?"
    # Миа говорит Шарлотт
    imgd 19823
    mia "Шарлотт, я же тебе говорила, что он даже не посмотрит на такую, как она."
    mia "Единственное, что у них может быть общего - это их скучная работа."
    mia "О чем еще может разговаривать Олаф с такой женщиной?"
    # Шарлотт все еще бесится
    imgf 19824
    charlotte "Да, Мия, возможно..."
    charlotte "Но... Думаю, что Олаф будет не против, если мы с тобой присоединимся к их деловой беседе."
    charlotte "Послушаем, что за важные переговоры тут ведутся. Давай?"
    imgd 19825
    mia "Да, давай, Шарлотт. Отличная идея."
    imgf 19826
    charlotte "Олаф, ты же не против?"
    charlotte "Ведь у тебя нет никаких секретов от меня?"
    # Олаф в шоке, мнется, что-то мямлит
    imgd 19827
    olaf "Да, но..."
    olaf "Кхм..."
    olaf "Конечно, не против... Дорогая..."
    # что-то говорит. да, я не против дорогая...
    # Моника возражает
    music Stealth_Groover
    imgf 19828
    m "Я против, Олаф..."
    m "Но если вам так будет проще принять решение относительного нашего вопроса..."
    m "То я, так уж и быть, потерплю присутствие этих особ."
    olaf "Да, Миссис Бакфетт. Спасибо."
    # грымзы садятся за столик, Шарлотт рядом с мужем, Мия рядом с Моникой
    # Шарлотт испепеляет Монику взглядом, Моника продолжает вести себя надменно
    # Мия наклоняется к Шарлотт через столик и хихикает
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Poppers_and_Prosecco
    imgfl 19829
    w
    imgf 19830
    mia "Послушаем, как ведет переговоры владелица сомнительного журнала. Хи-хи!"
    music Stealth_Groover
    imgd 19831
    m "Мой журнал приносит мне миллионы."
    m "И мне мало интересно мнение особ, которые из себя ничего не представляют."
    imgf 19832
    charlotte "На какую тему ваши переговоры?"
    charlotte "Что общего может быть между бизнесом моего мужа и вашим, так сказать, бизнесом?"
    # Моника надменностью ее передавливает
    imgd 19833
    m "Сразу видно, что вам чужд этикет проведения деловых встреч..."
    m "Но вам простительно - вы ведь привыкли пить шампанское и сплетничать..."
    m "Обсуждая, во что одет тот или иной гость на каком-нибудь фуршете..."
    m "До такого серьезного уровня, на котором мы общаемся с Олафом, вам далеко."
    # Олаф немного нервничает
    music Groove2_85
    imgf 19834
    olaf "Миссис Бакфетт, я прошу прощения за свою супругу."
    olaf "Она у меня немного ревнивая."
    music Stealth_Groover
    imgd 19835
    mt "Еще бы она не ревновала к такой шикарной женщине, как Я!"
    # Моника снисходительно
    imgf 19836
    m "Я вас извиняю, Олаф."
    m "Налейте мне еще вина и продолжим."
    imgd 19837
    olaf "Конечно, Миссис Бакфетт."
    # Олаф наливает ей вина, Шарлот в это время зло смотрит на него
    fadeblack
    sound pour_wine
    pause 2.0
    music Poppers_and_Prosecco
    imgfl 19838
    m "Спасибо, Олаф..."
    m "На чем нас прервали эти две особы?"
    olaf "Мы... Мы обсуждали инвестицию в ваш журнал, Миссис Бакфетт..."
    m "Да, верно..."
    menu:
        "Заставить Олафа при его жене инвестировать в журнал.":# может быть, в этом пункте не коррапшн задирать, а сделать его доступным только при минимальной бичности
            label gallery_19848:
            music Stealth_Groover
            imgf 19801
            mt "Хммм..."
            mt "Моника, тебе выдался отличный шанс закрыть вопрос с этим инвестором!"
            mt "Эта его грымза даже не представляет, как она помогла мне!"
            # Моника обращается к Шарлотт
            music Hidden_Agenda
            imgd 19839
            m "Ваше появление в этом заведении прервало наши переговоры на том моменте..."
            m "Когда Олаф любезно согласился инвестировать в мой журнал."
            # Олаф растерянно смотрит на Монику
            # Шарлотт вопросительно смотрит на мужа, а Мия спрашивает у Моники
            music stop
            sound plastinka1b
            img 19840 vpunch
            w
            music Groove2_85
            imgd 19841
            mia "А зачем?"
            m "Вы можете спросить у Олафа..."
            # все смотрят на Олафа
            # он мнется, боится, растерян, в итоге кое-как отвечает заикаясь
            imgf 19842
            olaf "Я... Я видел п-презентации..."
            olaf "Там были графики роста... Оч-чень... Очень убедительные графики..."
            # Моника надменно
            music Stealth_Groover
            imgd 19843
            m "Достаточно, Олаф. Этого хватит."
            m "Уши присутствующих дам привыкли носить модные шляпки, а не воспринимать цифры."
            # Шарлотт смотрит на Монику как змея
            imgf 19844
            charlotte "Я потом проверю, насколько эти цифры будут соответствовать реальному доходу!"
            imgd 19845
            m "Смотрите, не запутайтесь, миссис. Это вам не рассматривать чеки после шоппинга в немодных местах."
            m "Речь идет об очень серьезных суммах."
            m "И Олаф очень заинтересован в такой большой прибыли."
            imgf 19846
            m "Да, Олаф?"
            olaf "Д-да, Миссис Бакфетт..." # растерянно
            m "Потому Олаф умолял меня встретиться с ним и обсудить это инвестирование..."
            m "Более мне эта встреча неинтересна..."
            # Моника встает
            fadeblack 1.5
            music Stealth_Groover
            imgfl 19847
            m "Завтра я проверю у своего помощника Бифа, что вы решили, Олаф."
            m "И лучше бы вам, Олаф, не задавать лишних вопросов Бифу."
            m "Он недостаточно компетентен в таких серьезных делах."
            music Master_Disorder
            imgf 19848
            m "И я на вашем месте не стала бы рассматривать другие сомнительные финансовые предложения."
            m "Иначе вы рискует потерять все ваши деньги, Олаф..." # угрожающе, давит. проработать (сделать акцент)
            # Олаф испуганно
            imgd 19849
            olaf "С-спасибо, Миссис Бакфетт..."
            fadeblack
            sound highheels_short_walk
            # Моника уходит с видом победителя
            return
#        "Заставить Олафа при его жене инвестировать в журнал. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
#            pass
        "Не рисковать.":
            pass
    # Моника задумчиво
    music Groove2_85
    imgf 19850
    mt "Черт! Я могла бы воспользоваться ситуацией!"
    mt "И вынудить этого неудачника дать согласие на инвестирование!"
    mt "..."
    mt "Но это слишком рискованно."
    imgd 19851
    mt "Что, если он откажется?!"
    mt "Или его грымза начнет его отговаривать?"
    mt "По нему же сразу видно, что он жалкий подкаблучник!"
    mt "Нет, Моника, лучше не рисковать..."
    # Моника обращается к Олафу
    music Hidden_Agenda
    imgf 19839
    m "Да, Олаф. Мы говорили о том, что это будет весьма выгодная сделка для вас..."
    m "Слова Мистера Кэмпбелла этому подтверждение."
    m "А он очень опытный и грамотный бизнесмен."
    # Олаф мнется, поглядывает искоса на свою жену
    imgd 19852
    w
    imgf 19843
    m "С вашей стороны было бы верным решением последовать совету Мистера Кэмпбелла. И сделать эту инвестицию."
    imgd 19853
    olaf "Кхм... Миссис Бакфетт, да, я думаю, что..."
    olaf "Такой уважаемый бизнесмен как Мистер Кэмпбелл не может ошибаться..."
    # Миа перебивает его, говорит Шарлотт
    music Groove2_85
    imgf 19854
    mia "Шарлотт, давай вернемся в тот клуб, мне здесь скучно!"
    # Шарлотт сомневается, не хочет оставлять мужа с Моникой наедине
    imgd 19855
    charlotte "Согласна с тобой, дорогая."
    charlotte "Ты была права, эта Бакфетт - скучная. И разговоры у нее скучные."
    music Pyro_Flow
    imgd 19800
    mt "Это я скучная?!"
    mt "Посмотрела бы на себя, дура!"
    mt "Ни воспитания, ни чувства такта! Фи!"
    mt "!!!"
    # Шарлотт и Мия встают из-за стола
    fadeblack 1.5
    music Poppers_and_Prosecco
    imgfl 19856
    charlotte "Олаф, дорогой, поехали с нами?"
    # Олаф растерянно смотрит на Монику
    olaf "Дорогая, я пока не могу... К сожалению... Сама понимаешь, это работа."
    imgf 19857
    olaf "Я подъеду немного позже, когда закончу переговоры. Хорошо?"
    imgd 19858
    charlotte "Хорошо, дорогой. Смотри не усни здесь от скуки."
    imgd 19859
    mia "Хи-хи-хи!!"
    # Моника надменно смотрит на них, грымзы уходят
    music Pyro_Flow
    imgf 19860
    sound highheels_short_walk
    mt "Наконец-то, эти две овцы ушли."
    imgd 19861
    mt "Терпеть их не могу!"
    mt "Провинциальные дуры!"
    mt "!!!"
    # Олаф с виноватым видом смотрит на Монику
    music Poppers_and_Prosecco
    imgf 19862
    olaf "Миссис Бакфетт, я приношу Вам свои извинения..."
    olaf "Поведение моей супруги было неприемлемым."
    olaf "Я хотел бы сгладить данный инцидент..."
    music Stealth_Groover
    imgd 19863
    mt "Жалкий подкаблучник!"
    imgf 19794
    m "Олаф, я - сильная, независимая, красивая и умная женщина."
    m "Остальные женщины могут только мечтать, чтобы стать такой, как Я."
    m "Я уже привыкла к тому, что все они мне завидуют..."
    imgd 19864
    m "И как правило, их зависть выражается в подобном хамском поведении."
    m "Которое и продемонстрировала сегодня ваша супруга."
    m "У меня такое поведение вызывает только жалость."
    # Олаф смотрит на ее грудь
    imgf 19865
    olaf "Да, Миссис Бакфетт..."
    olaf "Вы очень проницательны."
    imgd 19792
    mt "Да, я очень умная и проницательная."
    mt "Поэтому сегодня ты дашь свое согласие инвестировать в мой журнал..."
    mt "И мне для этого не потребуются идти на всякие грязные мерзости, про которые говорил сволочь Биф!"
    music Hidden_Agenda
    imgf 19801
    mt "Хммм... А что, если он даст свое согласие и отдаст деньги мне?"
    mt "А я скажу ему, что сама их зачислю на счет..."
    mt "Надо попробовать..."
    mt "..."
    imgd 19786
    m "Кстати, Олаф..."
    olaf "Да, Миссис Бакфетт?"
    # Моника надменно (поза из 6815) вообще можно натырить поз из первой встречи с Филиппом
    m "Я хотела узнать ваше решение об инвестировании в мой журнал."
    m "И если вы все еще сомневаетесь, то я могла бы облегчить вам эту задачу."
    imgf 19796
    m "Достаточно вспомнить график, продемонстрированный Мистером Кэмпбеллом..."
    m "Чтобы отбросить все сомнения..."
    m "И сделать эту инвестицию."
    m "Кстати, я могла бы предоставить вам реквизиты для перевода этих денежных средств..."
    imgd 19866
    mt "Черт! Моника, у тебя же нет никаких реквизитов!"
    mt "С другой стороны, я могу использовать реквизиты Стива, а потом забрать деньги у него..."
    mt "Хотя, этот мешок с дерьмом наверняка постарается меня обмануть!"
    mt "!!!"
    # Олаф улыбается
    music Poppers_and_Prosecco
    imgf 19795
    olaf "Мистер Биф предупреждал меня, что Вы можете проверять меня на честность, Миссис Бакфетт."
    olaf "Потому я должен настаивать на том, чтобы перечислять денежные средства только через Вашу компанию."
    olaf "Если приму положительное решение..."
    imgd 19867
    mt "Твою мать!"
    mt "!!!"
    imgf 19868
    olaf "Я думаю, Миссис Бакфетт, мне потребуется еще немного времени, чтобы принять это решение."
    olaf "Я хотел бы поблагодарить Вас за столь приятный вечер."
    olaf "Надеюсь, это была не последняя наша встреча."
    # Олаф встает из-за столика
    # хочет уйти
    imgd 19869
    mt "Он что, собирается уходить?!"
    mt "?!?!?!"
    mt "Нет! Нет!"
    mt "Мне нельзя допускать этого!"
    imgd 19870
    mt "Он должен принять это чертово положительное решение именно сегодня!"
    mt "!!!"
    mt "Что же делать, Моника?!"
    mt "?!?!?!"
    menu:
        "Предложить ему продолжить вечер.":
            pass
    # Моника, пытаясь флиртовать
    fadeblack 1.5
    music Hidden_Agenda
    imgfl 19871
    m "Олаф..."
    m "Неужели вы хотите покинуть меня?"
    m "Я думала, мы с вами продолжим нашу встречу..."
#    music Poppers_and_Prosecco
    imgf 40195
    w
    imgd 19872
    w
    # Олаф мнется, потом снова садится за столик
    imgd 19873
    olaf "Миссис Бакфетт, я... Я просто подумал, что..."
    olaf "Что такая статусная женщина, как ВЫ, не захочет продолжения..."
    olaf "После сегодняшней неудобной ситуации..."
    music Stealth_Groover
    imgf 19874
    mt "Какой же он жалкий! Фи!"
    imgd 19875
    m "Олаф, так уж и быть..."
    m "Я не только самая красивая и умная, я еще и добрая леди."
    m "Поэтому я позволю вам исправить ошибки сегодняшнего вечера..."
    m "Такие как этот посредственный ресторан и появление вашей жены..."
    # Олаф радостно
    music Poppers_and_Prosecco
    imgf 19876
    olaf "Конечно, Миссис Бакфетт!"
    olaf "Спасибо Вам за Вашу доброту..."
    # Моника снисходительно улыбается
    imgd 19877
    w
    imgf 19878
    olaf "Смею признаться, Миссис Бакфетт..."
    # мнется
    olaf "Я заранее позаботился об этом и..."
    olaf "Я забронировал самый лучший номер в самом лучшем отеле города!"
    imgd 19879
    olaf "Там мы сможем с Вами пообщаться и нам никто не помешает, Миссис Бакфетт."
    olaf "Если Вы не против, конечно..."
    # Моника презрительно
    music Stealth_Groover
    imgf 19880
    mt "Конечно же, я против!"
    mt "Как он смеет приглашать такую леди, как Я, в отель на первой же встрече!"
    mt "Это отвратительно!!!"
    mt "!!!"
    imgd 19881
    mt "И вообще!"
    mt "Что еще за лучший отель?!"
    # Если Моника работает в эскорте
    if monicaHotelAdminAgreement3 == True:
        #
        $ notif(_("Моника работает в ВИП-эскорте отеля Ле Гранд."))
        #
        imgd 19881
        mt "Надеюсь, это не какой-нибудь второсортный Ле Гранд!"
        mt "И в этом отеле не будет никаких шлюх!"
        mt "!!!"
    imgf 19882
    mt "А еще более отвратительно то, что..."
    mt "Я вынуждена дать свое согласие из-за мерзкого кретина Бифа!!!"
    mt "Ненавижу его!"
    mt "Ненавижу всех этих неудачников!"
    mt "!!!"
    imgd 19883
    olaf "Что скажете, Миссис Бакфетт?"
    m "Я соглашусь поехать только в самый лучший отель, Олаф..."
    imgf 19884
    olaf "Да, конечно, Миссис Бакфетт!"
    olaf "Для Вас - только самое лучшее!"
    fadeblack
    sound highheels_short_walk
    pause 1.5
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
#    sound snd_car_turn_on
#    $ renpy.pause (1.0, hard=True)
#    img scene_Map_Evening
#    with fade
#    sound snd_car_engine
#    $ renpy.pause(6.0, hard=True)
#    img black_screen
#    with fade
#    sound snd_car_door
#    $ renpy.pause (2.0, hard=True)
#    $ monicaBiffInvestorDate3 = True # Моника поехала с инвестором в отель
    # Моника встает из-за столика
    # затемнение, звук мотора
    return

label gallery_32122:
    # Моника заходит в свой рабочий кабинет
    # смотрит на рабочий стол Юлии, а ее нет на месте
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32114
    w
    imgf 32115
    mt "Куда делась эта никчемная Юлия?"

    # если есть отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях и живет у нее."))
        #
        music Stealth_Groover
        imgd 32116
        mt "Впрочем, это хорошо, что ее нет."
        mt "Наконец-то, я смогу спокойно провести день без этой надоедливой дурочки..."

    # Моника идет к своему столу и тут поворачивает голову в сторону комнаты отдыха
    # в это время в комнате отдыха Виктория встает из-за стола и обращается к Юлии (на Монику они не смотрят)
    # Виктория разговаривает с Юлией очень мило
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 32118
    w
    music Power_Bots_Loop
    img 32117 hpunch
    mt "КАКОГО ЧЕРТА?!"
    mt "!!?!?!!!"
    music Groove2_85
    imgd 32119
    victoria "Юлия, дорогая, спасибо за кофе."
    victoria "Я с удовольствием поболтала бы с тобой еще, но..."
    victoria "К сожалению, мне пора идти по делам."
    # Юлия смотрит на нее с обожанием
    imgf 32120
    julia "Приходите почаще, Мисс Виктория!"
    julia "Мне так нравится проводить с вами время!"
    julia "В следующий раз угощу вас прекрасным зеленым чаем..."
    julia "И куплю что-нибудь вкусненькое."
    # Юлия встает, Виктория своим привычным жестом указывает на свою щеку, Юлия наклоняется к ней и чмокает в щечку
    imgd 32121
    victoria "Спасибо, Юлия! Ты такая милая!"
    victoria "Обязательно загляну к тебе скоро."
    sound kiss2
    imgf 32122
    w
    # камера на Монику, у нее шок и ужас на лице
    music Power_Bots_Loop
    img 32123 hpunch
    mt "ЧТО???"
    mt "ЭТА ДРЯНЬ!!!"
    mt "ТУТ ДЕЛАЕТ?!?!?!"
    # кадр на комнату отдыха
    # Виктория направляется к выходу
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 32124
    # кадр на кабинет Моники и на Монику
    # Виктория проходит мимо нее, Моника смотрит на нее со злым недоумением
    w
    music Power_Bots_Loop
    sound highheels_short_walk
    imgf 32125
    mt "!!!"
    mt "!!!!!!"
    # Виктория с ехидной улыбочкой
    music Groove2_85
    imgd 32126
    victoria "Привет, подружка Моника!"
    victoria "Я знаю, что ты хотела бы поболтать со мной, но у меня дела..."
    victoria "В следующий раз я обязательно уделю тебе свое внимание."
    victoria "И, кстати, моя ценная вещь все еще у тебя?"
    sound snd_woman_laugh3
    # Моника со злостью и раздражением
    # pause 1.5
    # music Power_Bots_Loop
    imgd 32127
    m "!!!"
    m "Да!"
    imgd 32128
    victoria "Хорошо. Скоро я ее заберу."
    victoria "Смотри, не потеряй."
    victoria "Ну все, подружка Моника, пока."
    victoria "Передавай привет нашей подружке Мелани. Хи-хи."
    sound snd_woman_laugh3
    # Виктория уходит
    # Моника в шоке смотрит на Юлию, та убирает чашки со стола
    label gallery_32130:
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    imgfl 32129
    mt "Что эта сучка Виктория пытается вынюхать здесь!?"
    mt "Зачем она общается с никчемной дурочкой Юлией?"

    # если отношений с Юлией нет, то Моника рявкает на нее
    imgf 32130
    m "Юлия, тебе платят за то, что бы ты занималась работой, а не всякой ерундой!!!"
    m "Или ты забыла свое место!? Хочешь вылететь с этой работы?"
    sound highheels_run1
    imgd 32131
    m "РАБОТАТЬ!!!"
    m "ЖИВО!!!"
    julia "Д-да, М-м-миссис Бакфетт..." # испуганно
    julia "Из-звините..."
    # Юлия испуганно бежит к своему столу

    # если отношения с Юлией есть
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях и живет у нее."))
        #
        music Hidden_Agenda
        imgf 17817
        mt "Нужно аккуратно спросить у этой дурочки Юлии, о чем они говорили с Викторией."
        # Моника подходит к Юлии, обнимает за талию
        fadeblack
        sound highheels_short_walk
        pause 1.5
        music Loved_up
        imgfl 32132
        m "Милая, смотрю, вы подружились с Мисс Викторией..."
        # Юлия начинает восторженно рассказывать
        imgf 32133
        julia "О, Миссис Бакфетт! Мисс Виктория такая чудесная. Она очень милая и добрая!"
        julia "Я так счастлива, что мы познакомились с ней."
        julia "Как жаль, что вы не смогли присоединиться к нашему чаепитию! Оно было волшебным!"
        # Моника притворно улыбается
        imgd 32134
        m "Да, Юлия... Мисс Виктория очень милая и добрая девушка..."
        # снова притворно улыбается и целует Юлию
        sound kiss2
        imgf 32135
        w
        imgd 32134
        m "Дорогая, я рада, что твой день начался так чудесно."
        m "А теперь нам пора поработать."
        imgf 32136
        julia "Миссис Бакфетт, я соскучилась..."
        mt "О БОЖЕ!"
        m "Юлия, прости, мне надо работать..."

    # возвращается на свое рабочее место, Юлия - на свое
    fadeblack
    sound highheels_short_walk
    pause 1.5
#    music Groove2_85
    music Pyro_Flow
    imgfl 20253
    w
    imgf 32137
    mt "Виктория! Белобрысая тварь!"
    mt "Притворяется перед Юлией белой овечкой! А сама разнюхивает тут что-то!!!"
    mt "Лицемерная сучка!!!"
    mt "Бесит!!!"
    mt "Ненавижу!!!"
    mt "!!!"

    # Виктория идет мимо админа, кладет ласково на него руку
    # подмигивает
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Marty_Gots_a_Plan
    imgfl 32138
    w
    imgf 32145
    w
    imgd 32144
    sound Jump2
    victoria "Пока, красавчик..."

    # админ в шоке смотрит ей вслед
    imgf 32146
    sound snd_woman_laugh3
    w2t "!!!"
    return

label gallery_32142:
    # при клике в меню на рабочий кабинет Моники, показываем, как Моника заходит в отдел отчетов
    # ей со всех сторон летит
    fadeblack
    sound snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 17772
    w
    imgf 32112
    w3 "Добрый день, Миссис Бакфетт!"
    w5 "Здравствуйте, Миссис Бакфетт!"
    w1 "Добрый день!"
    # она сделала лицо кирпичом и не глядя ни на кого идет в свой кабинет
    imgd 17767
    mt "Никчемные людишки. Сидят занимаются никому ненужной работой!"
    mt "И думают, что делают важное дело!"
    mt "Бесполезные!"
    mt "Никчемные!"
    mt "!!!"
    # проходит мимо айтишника, также не глядя на него
    imgf 32113
    sound highheels_short_walk
    w
    # смена кадра, айтишник
    # показываем айтишника за его рабочим столом
    fadeblack 2.0
    music Marty_Gots_a_Plan
    imgfl 31470
    w
    # показываем кадр со спины айтишника, виден его монитор
    # у него на мониторе трансляция видео со скрытой камеры с комнаты отдыха
    # вид из-под стола - две пары женских ног, сидят рядом друг с другом, обе без трусиков (Виктория и Юлия)
    sound keyboard_click
    imgf 32205
    w
    imgd 32139
    w
    sound camera_zoom
    imgf 32140
    w
    sound camera_zoom
    imgd 32141
    w
    # айтишник про себя думает
    imgf 31471
    w2t "Интересно, в этом офисе все ходят без трусиков?"
    w2t "Хммм..."
    imgd 31487
    w2t "Нужно расставить камеры и под другими столами в офисе."
    w2t "И почему я раньше до этого не додумался?"
    # вдруг Виктория раздвигает ноги в показывает в камеру знак V пальцами
    # админ испугался
    imgf 32142
    sound Jump2
    w
    music stop
    sound plastinka1b
    img 32143 hpunch
    w2t "О ЧЕРТ!"
    w2t "Она заметила камеру???"
    return

label gallery_32162:
    # близняшки и Лин, наклонившись друг к другу, шепчутся, сплетничают
    # сбоку от них стоит серая мышь и периодически пытается участвовать в разговоре
    fadeblack
    music Hidden_Agenda
    imgfl 32147
    w
    imgf 32148
    w
    imgd 32149
    w3 "Помните!?"  # одна близняшка
    w3 "Я говорила вам, что та обложка, где она в красном платье и с голой грудью - это только начало?"
    # Лин и вторая близняшка переглядываясь
    w4 "Да."  # вторая близняшка
    w7 "Помню." # Лин
    # Первая близняшка выпрямилась и огляделась по сторонам
    sound Jump2
    imgf 32150
    w
    imgd 32149
    w3 "Недавно была фотосессия, где она позировала перед толпой каких-то мужчин..."
    w3 "Почти голая!"
    w3 "Представляете?!"
    # Все наклоняются к первой близняшке, прикрыв рот от удивления
#    music Sneaky_Snitch
    imgf 32151
    w4 "Ого!"
    w4 "Серьезно?!"
    # Лин, сдерживая улыбку и радось от интересной сплетни
    sound oooh4
    w7 "Да ладно!?"
    sound oooh1
    sound2 snd_woman_laugh2
    w7 "Не может такого быть!"
    # Первая близняшка вполголоса
    w3 "Это информация из проверенного источника. 100 процентов!"
    # 2-я близняшка с удивлением
    imgd 32152
    w4 "Что, прямо перед толпой мужчин?!"
    w4 "А кто они такие?"
    # Первая близняшка пожимая плечами
    w3 "Не знаю... Говорят, что какие-то богачи!"
    # Серая мышь вклинивается в разговор и все раздражительно оборачиваются на неё
    imgf 32154
    w1 "Но зачем ей это делать? Ради денег?"  # серая мышка в очках
#    music Hidden_Agenda
    imgd 32155
    w7 "Да ну, какие-то глупые слухи..."
    w7 "Денег у нее побольше, чем у каких-то там богачей."
    w7 "И этот журнал..."
    w3 "Говорю же вам, это правда!"
    w7 "Но тогда зачем ей это?"
    w7 "Раз деньги ей не нужны..."
    w3 "Не знаю, но зачем-то она делает это!"
    # спрашивает серая мышка в очках, с негодованием и стеснением
#    music Sneaky_Snitch
    imgf 32153
    w1 "Может быть, ей это нравится?"
    sound snd_woman_laugh2
    # Вторая блезняшка хихикая
    w4 "Может, она извращенка!?"
    # Первая блезняшка хихикая
    w3 "Хорошо, что она тебя сейчас не слышит!"
    sound snd_woman_laugh1
    # если Моника работала манекеном в магазине одежды
    if monicaAgreedToSellDress == True:
        #
        $ notif(_("Моника работала манекеном в магазине одежды."))
        #
        # Лин говорит,оглядываясь по сторонам

        imgd 32156
        w7 "Вообще-то... Я ее уже где-то видела..."
        w7t "Только никак не могу вспомнить, где же?"
        w7t "Хммм..."
        # Все наклоняются к Лин с удивлением и интересом

        w3 "И где же?.."
        w4 "В смысле, где?!"
        w4 "На обложке журнала, где же еще?!"
        w4 "Ну или в интервью."
        w7 "Кстати!"
    #
    imgf 32155
    w7 "Я видела интервью с ней на приеме у Кэмпбелла!"
    w7 "Она говорила, что никогда не стала бы обнажаться перед камерой!"
    # все оборачиваются и с раздражением смотрят на нее
    imgd 32154
    w1 "Я не верю в эти слухи!"
    # Первая близняшка нагибается и говорит вполголоса
    imgf 32157
    w3 "Да я же вам говорю, что информация из достоверного источника."
    # Первая близняшка раздраженно
    w3 "Как вообще такое можно было придумать?!"
    # Вторая близняшка с сарказмом и смехом
    imgd 32158
    w1 "Тебе наврали!"
    w4 "Это что-ли твой любовничек достоверный источник?"
    w4 "Какой-нибудь младший помощник какого-нибудь начальника в каком-нибудь мелком отделе?"
    sound snd_woman_laugh2
    w4 "Хи-хи-хи..."
    w4 "Я даже знаю такого... Работает этажом ниже..."
    w4 "Я как-то видела тебя с ним..."

    # Первая близняшка с раздражением и надменным лицом
    imgf 32159
    w3 "Нет!"
    w3 "Что ты такое говоришь?!"
    w3 "Что бы Я с ним!?"
    w3 "Ни за что!"
    w3 "Ты так говоришь, потому что мне завидуешь и сама хотела бы с ним..."
    w3 "Общаться!"
    # Вторая близняшка с сарказмом и смехом
    w4 "С ним?!"
    w4 "Фуууу!"
    w4 "Конечно, нет!"

    # кадр на Гретту
    # она с грозным видом смотрит на сплетничающих сотрудниц
    music Groove2_85
    imgd 32160
    w6 "Эй, вы! Дуры надутые!"  # Грета
    w6 "Немедленно прекратите эти сплетни на рабочем месте!"
    # сотрудницы межу собой переглядываются
    imgf 32149
    w3 "Достала уже эта жирная корова!"
    w4 "Везде свой нос сует!"
    imgd 32161
    w6 "Так! Вы на работу пришли делом заниматься или сплетничать?!"
    # близняшки и Лин переглянулись
    # тут кто-то из них испуганно
    music stop
    sound plastinka1b
    img 32162 hpunch
    w3 "Бакфетт идет!!!"
    # все пугаются
    music Turbo_Tornado
    w3 "Твою мать!"
    w4 "Быстро все по местам!!!"
    w1 "АААА!!!"
    sound highheels_run2
    pause 2.0
    # затемнение, топот
    return
