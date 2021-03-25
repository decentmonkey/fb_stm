# Моника приходит на работу и работает до вечера.Днем к ней приходит Мелани и происходит диалог.
# Вечером Моника идет к Мелани в гости и думает, что там будет Маркус.
# Стук в дверь, заходит Виктория. И появляется затемнение экрана "Ранее в этот день..."
# И начинается сцена с Мелани в гримерке и игра за Мелани

# кабинет Моники, сцена начинается автоматически, когда Моника заходит к себе в кабинет
# в кабинет к Монике приходит Мелани
label ep29_dialogues3_melanie_monica_victoria_3b:
    # Моника смотрит на Мелани удивленно
    music ZigZag
    sound snd_door_open1
    img 15409
    with fadelong
    w
    sound highheels_short_walk
    img 15410
    with fade
    m "Мелани? Ты ко мне?"
    music Master_Disorder
    img 15411
    with diss
    mt "Мелани не просто так зашла ко мне в гости. Что-то случилось."
    mt "Надеюсь, это не касается Маркуса!"
    mt "!!!"
    # Мелани равнодушно
    music ZigZag
    img 15412
    with fade
    melanie "Миссис Бакфетт. Я сейчас была на встрече с нашим общим хорошим другом..."
    # Моника явно напугана
    music Master_Disorder
    img 15413
    with diss
    mt "!!!"
    sound Jump1
    img 15414
    with diss
    m "Нашим общим д-другом?"
    music ZigZag
    img 15415
    with fade
    melanie "Да, Миссис Бакфетт. Этот человек хочет сегодня встретиться с нами."
    img 15416
    with diss
    mt "!!!"
    img 15417
    with fade
    w
    img 15418
    with diss
    melanie "Встреча состоится вечером у меня."
    melanie "В Ваших же интересах, Миссис Бакфетт, присутствовать на встрече..."
    # Моника смотрит на Мелани ошарашенно
    img 15419
    with fade
    julia "???"
    img 15420
    with diss
    melanie "..."
    music Master_Disorder
    img 15421
    with fade
    mt "Встреча с Маркусом?!"
    mt "У Мелани дома?!"
    img 15422
    with diss
    mt "Сегодня?!"
    mt "!!!"
    # Юлия заинтересованно наблюдает за их диалогом
    # Моника смотрит на Юлию, потом снова на Мелани, берет себя в руки
    img 15423
    with fade
    w
    music ZigZag
    img 15424
    with diss
    m "Я поняла, Мисс Мелани. Я приду вечером."
    img 15425
    with fade
    melanie "Договорились, Миссис Бакфетт."
    # Мелани уходит
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    sound2 snd_door_close1
    pause 2.0
    # у Моники в заданиях появляется "Пойти вечером к Мелани домой на встречу с 'другом'"
    #$ log1 = t_("Пойти вечером к Мелани домой на встречу с 'другом'")
    return

# кабинет Моники, когда поработала до вечера и пора идти к Мелани
label ep29_dialogues3_melanie_monica_victoria_7:
    # Моника сидит в своем кабинете за столом, она одна, уже вечер
    # Моника взволнованна
    mt "Почему-то, мне совсем не хочется ехать к Мелани..."
    mt "Ничего хорошего меня там не ждет."
    mt "..."
    mt "Она сказала 'наш общий друг'..."
    mt "Это может быть только один человек. Маркус."
    mt "Я уверена в этом!"
    mt "Хм... А почему тогда у Мелани дома? Почему не в полиции?"
    mt "???"
    mt "Я могу не ехать к Мелани, но..."
    mt "Тогда меня могут ждать большие неприятности с Маркусом!"
    mt "Даже не хочу думать о том, что тогда меня может ожидать!"
    mt "!!!"
    mt "Лучше мне пойти сейчас к Мелани и самой все узнать."
    mt "Да, так будет лучше всего."
    # в заданиях появляется "Нужно переодеться и ехать к Мелани"
    #$ log1 = t_("Нужно переодеться и ехать к Мелани")
    return

# мысли Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_7a:
# Моника пытается пойти к Мелани в красивом платье
    mt "Думаю, мне стоит надеть что-то более простое..."
    mt "В прошлый раз я была у Мелани в одежде шлюхи. Сегодня тоже нужно надеть его."
    return

# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_7b:
# Моника пытается пойти к Мелани в любой другой одежде, кроме одежды шлюхи
    mt "В прошлый раз я была у Мелани в одежде шлюхи. Сегодня тоже нужно надеть его."
    return

# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_7c:
# Моника пытается лечь спать
    img scene_Basement_Bedroom1
    with fadelong
    mt "Я, конечно, могу не ехать к Мелани, но..."
    mt "Тогда меня могут ждать большие неприятности с Маркусом!"
    mt "Даже не хочу думать о том, что тогда меня может ожидать!"
    mt "!!!"
    mt "Лучше мне пойти сейчас к Мелани и самой все узнать."
    menu:
        "Лечь спать (пропуск событий с Мелани).":
            return True
        "Не ложиться.":
            return False
    return False

label ep29_dialogues3_melanie_monica_victoria_7d:
    mt "Ой, я заснула? Мне приснился странный сон."
    mt "Впрочем, уже вечер. Мне нечего делать здесь."
    return

# при клике на Дом Мелани на карте включается сцена у Мелани дома
# вызов "ep29_dialogues4_lesbian_threesome_victoria_1"
# сцена у Мелани дома обрывается на моменте, когда заходит в дверь Виктория
# появляется затемнение экрана "Ранее в этот день..."


# Автоматически включается сцена в гримерке у Мелани, после нее управление переходит на Мелани
label ep29_dialogues3_melanie_monica_victoria_1:
    # Мелани сидит перед зеркалом в гримерке, поправляет макияж кистью для мейкапа
    music ZigZag
    img 15392
    with fadelong
    w
    img 15393
    with fade
    melanie_t "Я выгляжу какой-то уставшей..."
    melanie_t "Мне нужно взять несколько выходных и отдохнуть."
    img 15394
    with diss
    melanie_t "Возможно, стоит полететь на острова... Океан, пальмы, никаких папарацци..."
    melanie_t "Нужно будет подойти к Бифу, попросить у него небольшой отпуск."
    img 15395
    with diss
    melanie_t "Он не сможет мне отказать."
    melanie_t "Еще ни один мужчина не отказывал мне. И Биф не станет первым..."
    # в гримерку заходит серкретарша Бифа
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 15386
    with fadelong
    secretary "Мисс Мелани..."
    # Мелани поворачивается к ней
    img 15387
    with diss
    melanie "Да?"
    img 15388
    with fade
    secretary "Сейчас звонила Мисс Виктория."
    # Мелани вопросительно смотрит на нее
    img 13932
    with diss
    melanie "И что Мисс Виктория сказала?"
    img 13930
    with fade
    secretary "Она просила передать Вам, что она сегодня ждет Вас у себя."
    secretary "Она сказала, что это очень срочно."
    # Мелани смотрит на секретаря вопросительно
    img 15389
    with diss
    melanie "Говорила ли Мисс Виктория еще что-нибудь?"
    img 15390
    with fade
    secretary "Нет, Мисс Мелани. Она только сказала, что это очень срочно."
    img 15391
    music Master_Disorder
    with diss
    melanie "..."

### меню выбора взято из другого диалога

    menu:
        "Идти на встречу с Викторией":
            pass
        "Отказаться от встречи (пропуск всех событий с Викторией)":
            music Groove2_85
            img 13932
            with fade
            melanie "Если эта девочка еще раз позвонит, то передайте ей, что у меня нет времени на это." #+
            img 13933
            with diss
            secretary "Хорошо, Мисс Мелани, я передам."
            return False
###
    music ZigZag
    img 13929
    with fade
    melanie "Спасибо. Я проведаю Мисс Викторию сегодня."
    melanie "Вы можете идти."
    # секретарша уходит, Мелани поворачивается снова к зеркалу и задумчиво смотрит на свое отражение
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Master_Disorder
    img 13935
    with fade
    melanie_t "Что этой мерзкой Мисс Виктории снова нужно от меня?"
    melanie_t "Почему Я должна ехать к ней по первому же ее звонку?"
    melanie_t "..."
    # Мелани снова берет в руки кисть для мейка и проводит ею по скуле
    img 15396
    with diss
    melanie_t "Эта мелкая стерва возомнила себя самой умной и хитрой..."
    melanie_t "Нужно будет придумать, как поставить ее на место."
    img 15397
    with fade
    melanie_t "Кто она вообще такая, чтобы вести себя со МНОЙ подобным образом?"
    melanie_t "Нужно во что бы то ни стало лишить эту сучку возможности шантажировать меня."
    img 15398
    with diss
    melanie_t "Если я узнаю, кто снабжает ее моими фотографиями, шпионя за мной..."
    melanie_t "То у меня будет хоть какая-то зацепка. Я смогу договориться с этим папарацци."
    img 13936
    with diss
    melanie_t "Уверена, что все дело в деньгах."
    melanie_t "..."
    # положила кисть на столик, поправляет прическу
    music ZigZag
    img 15399
    with fade
    melanie_t "Конечно, проще всего было бы соблазнить Дика."
    melanie_t "В моих силах сделать так, чтобы он вышвырнул эту сучку на улицу..."
    img 15400
    with diss
    melanie_t "Где он ее и подобрал, я так полагаю."
    melanie_t "Но ведь она сидит и охраняет Дика, как цепной пес."
    img 13935
    with diss
    melanie_t "Хм... Интересно, Дик вообще ходит куда-нибудь без нее?"
    melanie_t "Нужно будет узнать об этом."
    # Мелани смотрит на себя в зеркало
    music Power_Bots_Loop
    img 15401
    with fade
    melanie_t "А пока мне придется поехать к этой мелкой сучке..."
    melanie_t "И узнать, что взбрело ей в голову на этот раз."
    music ZigZag
    img 15402
    with diss
    melanie_t "Сейчас мне нужно ехать в офис Дика."
    # встает со стула
#    $ log1 = t_("Пойти в офис Дика и узнать, что нужно Виктории")
    return

# управление перешло на Мелани
# появляется иконка Мелани справа
# в заданиях появляется "Пойти в офис Дика и узнать, что нужно Виктории"
# денег у Мелани 500 000 баксов

# мысли Мелани в гримерке
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1a:
    # смотрит на свой портрет
    melanie_t "Это одна из моих любимых работ."
    return
label ep29_dialogues3_melanie_monica_victoria_1b:
    # смотрит на другие свои фотографии
    melanie_t "Любая моя фотография - произведение искусства."
    return
label ep29_dialogues3_melanie_monica_victoria_1c:
    # смотрит на зеркала
    melanie_t "Люблю, когда меня окружает много зеркал. Мне нравится смотреть на себя."
    return
label ep29_dialogues3_melanie_monica_victoria_1d:
    # смотрит на косметику на столе
    melanie_t "Косметики много не бывает. Я готова покупать ее каждый день."
    return
label ep29_dialogues3_melanie_monica_victoria_1e:
    # смотрит на чемоданы
    melanie_t "Здесь можно найти красивый наряд для любого события. Дорогие наряды отлично подчеркивают мою красоту."
    return
label ep29_dialogues3_melanie_monica_victoria_1f:
    # клик на Мелани
    melanie_t "Я не могу позволить, чтобы мною командовала какая-то девочка. И где только Дик ее нашел?"
    return

# мысли Мелани в фотостудии
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1g:
    # смотрит на съемочную площадку
    melanie_t "Перед объективом камеры я чувствую себя превосходно. Люблю быть в центре внимания."
    return
label ep29_dialogues3_melanie_monica_victoria_1h:
    # смотрит на оборудование для фотосессии
    melanie_t "В этой студии самое лучшее оборудование. Мне нравится работать здесь."
    return
label ep29_dialogues3_melanie_monica_victoria_1i:
    # смотрит на Алекса (глазик)
    melanie_t "Алекс. Неплохой фотограф. А я его любимая модель."
    return
label ep29_dialogues3_melanie_monica_victoria_1j:
    # смотрит на Алекса (разговор)
    melanie_t "Он снова начнет уговаривать меня сняться для его личной коллекции... Мне пока не до этого."
    return

# мысли Мелани на ресепшене перед кабинетом Бифа
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1k:
    # смотрит на любой предмет в приемной Бифа
    melanie_t "Всегда не любила это место. Никогда не знаешь, что ожидать, когда входишь в дверь босса. Будь то Миссис Бакфетт или Биф..."
    return
label ep29_dialogues3_melanie_monica_victoria_1l:
    # смотрит на секретаря Бифа (глазик)
    melanie_t "Секретарю Бифа не помешало бы сходить к косметологу. Нельзя же себя так запускать..."
    return


label ep29_dialogues3_melanie_monica_victoria_1m:
    # смотрит на секретаря Бифа (разговор, когда Бифа нет на месте)
    #img
    music Groove2_85
    img 15801
    with fade
    melanie "Биф у себя?"
    img 15802
    with diss
    secretary "К сожалению, Мисс Мелани, он будет только вечером. Что-нибудь ему передать?"
    img 15803
    with fade
    melanie "Нет, спасибо. Я позже сама с ним поговорю."
    img 15804
    with diss
    melanie_t "Бифа сложно застать на рабочем месте. Такое ощущение, что он сюда приходит только выпить виски по вечерам..."
    return


label ep29_dialogues3_melanie_monica_victoria_1n:
    # смотрит на секретаря Бифа (разговор, когда Биф на работе, вечером после посещения офиса Дика)
    #img
    music Groove2_85
    img 15805
    with fade
    melanie "Биф у себя?"
    img 15802
    with diss
    secretary "Да, Мисс Мелани. Проходите."
    img 15803
    with fade
    melanie "Спасибо."
    return

label ep29_dialogues3_melanie_monica_victoria_1n2:
    # Мелани заходит в кабинет Бифа, когда его нет
    melanie_t "Бифа сейчас нет."
    melanie_t "И мне нечего делать здесь. Я не найду здесь ничего, кроме пустых бутылок из-под виски."
    return

# мысли Мелани в кабинете Бифа
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1o:
    # смотрит на Бифа (глазик)
    melanie_t "Если Биф выпивает полбутылки виски, то становится намного сговорчивее."
    return
label ep29_dialogues3_melanie_monica_victoria_1p:
    # смотрит на любой предмет в кабинете Бифа
    melanie_t "Миссис Бакфетт, должно быть, очень хочет вернуться в свой кабинет."
    melanie_t "Хотя, я тоже была бы не прочь оказаться в этом кресле..."
    return

# мысли Мелани в холле у лифта
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1q:
    # если не была еще в офисе Дика, при любом клике, кроме выхода
    melanie_t "Сейчас мне нужно ехать в офис Дика. Что этой ненормальной Виктории снова от меня нужно?"
    return

# мысли Мелани в отделе отчетов
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1r:
    # смотрит на сотрудников отдела отчетов
    melanie_t "Никогда не понимала, как люди целыми днями могут работать с документами? Это так скучно."
    melanie_t "И зачем здесь так много сотрудников? Неужели этот отдел настолько важен для журнала?"
    return
label ep29_dialogues3_melanie_monica_victoria_1s:
    # смотрит на подхалима (глазик)
    melanie_t "У него такой важный вид, как-будто он здесь всеми руководит."
    return
label ep29_dialogues3_melanie_monica_victoria_1t:
    # смотрит на айтишника (глазик)
    melanie_t "Очередной мой поклонник, который ни слова при мне не может сказать..."
    melanie_t "Мужчины часто в моем присутствии теряют дар речи..."
    return

# мысли Мелани в кабинете Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1u:
    # смотрит на Юлию (глазик)
    if act=="l":
        melanie_t "Это кто? Наверное, помощница Миссис Бакфетт. Я не хотела бы оказаться на ее месте."
        return
    melanie_t "Мне с ней не о чем разговаривать."
    return

label ep29_dialogues3_melanie_monica_victoria_1w:
    # смотрит на Монику (глазик)
    melanie_t "Миссис Бакфетт. Она неплохо тут устроилась."
    melanie_t "У нее есть много подчиненных и помощница. Можно целыми днями командовать людьми, как она любит."
    return
label ep29_dialogues3_melanie_monica_victoria_1x:
    # смотрит на предмет в кабинете Моники
    melanie_t "Вполне приличный рабочий кабинет. Конечно, не сравнить с бывшим кабинетом Миссис Бакфетт."
    melanie_t "Она, наверное, скучает по кастингам..."
    return

# мысли Мелани на ресепшене в офисе Дика на первом этаже
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1y:
    # смотрит на секретаря на ресепшене (глазик)
    melanie_t "Она неплохо выглядит... В отличие от секретарши Бифа."
    return


label ep29_dialogues3_melanie_monica_victoria_1z:
    # смотрит на секретаря на ресепшене (разговор)
    img black_screen
    with diss
    sound highheels_short_walk
    music m80s_Things
    pause 2.0
    img 15454    # секретарь ресепшн на первом этаже у Дика
    with fadelong
    w
    sound highheels_short_walk
    img 15455   # секретарь ресепшн на первом этаже у Дика
    with fade
    w
    img 15713
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 1.0
    music ZigZag
    img 15714
    with fadelong
    reception_secretary "Здравствуйте, Мисс Мелани!"
    reception_secretary "Я так рада Вас видеть!"
    reception_secretary "Вы, как всегда, великолепно выглядите!"
    img 15715
    with diss
    melanie "Спасибо."
    img 13940
    with fade
    reception_secretary "Вы пришли к Мистеру Дику? Он как раз у себя."
    reception_secretary "Уверена, что Мистер Дик будет рад Вашему визиту! Я могу проводить Вас, Мисс Мелани."
    img 15716
    with diss
    w
    img 15717
    with diss
    melanie "Это совсем необязательно. Я помню, где находится кабинет Мистера Дика."
    img 15718
    with fade
    melanie_t "Не хватало еще, чтобы мелкая сучка сказала что-нибудь унизительное мне при этой женщине."
    return

# мысли Мелани в приемной перед офисом Дика, второй этаж
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1aa:
    # смотрит на Викторию (глазик)
    melanie_t "Эта мелкая стервозная сучка начинает раздражать меня..."
    melanie_t "Нужно найти способ поставить ее на место."
    return
label ep29_dialogues3_melanie_monica_victoria_1bb:
    # смотрит на дверь в кабинет Дика
    melanie_t "Может проигнорировать Викторию и пойти напрямую к Дику?"
    melanie_t "Дик быстро разберется с ней. Мне стоит только попросить его об этом."
    melanie_t "С другой стороны... Неужели Я не смогу справиться с ней?"
    return

# мысли Мелани в ее квартире
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1cc:
    # смотрит на сумочку Виктории
    melanie_t "Эта мелкая сучка снова раздобыла какую-то компрометирующую информацию."
    return
label ep29_dialogues3_melanie_monica_victoria_1dd:
    # смотрит на свои портреты
    melanie_t "Все мои портреты - произведения искусства."
    melanie_t "Мне нравится окружать себя прекрасным."
    return
label ep29_dialogues3_melanie_monica_victoria_1ee:
    # смотрит на столик с бокалами
    melanie_t "Это вино многолетней выдержки - подарок одного коллекционера."
    melanie_t "Вряд ли Виктория сможет понять разницу между ним и дешевкой из магазина."
    return
label ep29_dialogues3_melanie_monica_victoria_1ff:
    # смотрит на мебель
    melanie_t "Интерьер моей квартиры разрабатывал один из лучших дизайнеров города."
    melanie_t "В целом, мне нравится. Просто и со вкусом."
    return

# мысли Мелани, когда вышла из здания, где расположен офис Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1gg:
    # перед посещением офиса Дика
    melanie_t "Мне нужно ехать в офис Дика. Виктория передала, что это срочно."
    melanie_t "Эта девочка Дика начинает мне надоедать..."
    return
label ep29_dialogues3_melanie_monica_victoria_1hh:
    # перед тем, как поехать к себе домой
    melanie_t "Скоро ко мне придет Миссис Бакфетт и эта мелкая дрянь."
    melanie_t "Надеюсь, мне не придется долго терпеть ее присутствие в моей квартире."
    return

# мысли Мелани перед зданием, где расположен офис Моники
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1ii:
    # после посещения офиса Дика
    melanie_t "Необходимо убедить Миссис Бакфетт в необходимости ее присутствия на встрече с Викторией."
    melanie_t "Виктория ясно дала понять, что она обязательно должна быть сегодня вечером у меня."
    return

# мысли Мелани перед зданием, где расположен офис Дика
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_1jj:
    # перед посещением офиса Дика
    melanie_t "В прошлый раз Мистер Дик был крайне рад меня видеть."
    melanie_t "И достаточно пренебрежительно обошелся с Викторией в моем присутствии."
    melanie_t "После такого Виктория и близко меня к нему не подпустит."
    return

# мысли Мелани, когда вышла из здания, где расположен офис Дика
label ep29_dialogues3_melanie_monica_victoria_1kk:
    # после посещения офиса Дика
    melanie_t "Мелкая дрянь... Кем она себя возомнила?"
    melanie_t "Мне нужно вернуться на работу и поговорить с Миссис Бакфетт."
    return

# мысли Мелани перед домом, где расположена ее квартира
label ep29_dialogues3_melanie_monica_victoria_1ll:
    melanie_t "Виктория сегодня обещала устроить девичник."
    melanie_t "Что ж... Посмотрим, чем это закончится..."
    return

# клик на Мелани возле здания, где офис Моники (глазик)
label ep29_dialogues3_melanie_monica_victoria_1mm:
    melanie_t "Любая девушка в мире может только мечтать о такой работе, как у меня."
    melanie_t "Но они - не я. Недостаточно быть просто красивой."
    return

# клик на Мелани возле здания, где офис Дика (глазик)
label ep29_dialogues3_melanie_monica_victoria_1nn:
    melanie_t "Я сегодня выгляжу сногсшибательно. Впрочем, как всегда..."
    melanie_t "Виктория ненавидит меня за это."
    return

# клик на Мелани возле ее дома (глазик)
label ep29_dialogues3_melanie_monica_victoria_1oo:
    melanie_t "Люблю свою квартиру. Там я могу скрыться от посторонних глаз и объективов камер."
    return

# если Мелани хочет зайти снова к Виктории после разговора с ней
label ep29_dialogues3_melanie_monica_victoria_1pp:
    melanie_t "Виктория ясно дала понять, что продолжит разговор вечером."
    melanie_t "Сейчас нет смысла возвращаться в офис Дика."
    return False

# если Мелани хочет зайти снова к Монике после разговора с ней
label ep29_dialogues3_melanie_monica_victoria_1rr:
    melanie_t "Думаю, Миссис Бакфетт поняла, что должна прийти ко мне вечером."
    melanie_t "Уверена, что она не проигнорирует эту встречу."
    return False

# если Мелани хочет зайти снова к Бифу после разговора с ним
label ep29_dialogues3_melanie_monica_victoria_1ss:
    if act=="l":
        return
    melanie_t "Я больше не хочу с ним разговаривать."
    return False

label ep29_dialogues3_melanie_monica_victoria_2:
    # Виктория сидит за своим рабочим столом с самодовольным видом

#    sound snd_lift
#    pause 2.0
    music ZigZag
    img 15456
    with fadelong
    w
    img 15457
    with diss
    melanie "Мисс Виктория, мне передали, что вы просили меня приехать к вам..."
    # Виктория смотрит на нее с недоброй ухмылкой
    music Groove2_85
    img 15458
    with fade
    victoria "Подружка, мне кажется, что ты не рада меня видеть..."
    victoria "Хорошие подружки так себя не ведут."
    victoria "Давай сделаем вид, что ты ничего мне сейчас не говорила. И ты подойдешь снова."
    # Мелани смотрит на нее непроницаемым взглядом
    music ZigZag
    img 15459
    with diss
    melanie "..."
    menu:
        "Сделать, как требует Виктория":
            pass
    img 15460
    with diss
    melanie_t "Мне было бы приятно видеть ее лицо не здесь..."
    melanie_t "Например, на обложке журнала Фермы 218 она смотрелась бы неплохо."
    # разворачивается, отходит от стола, потом подходит снова
    # Виктория внимательно наблюдает за ней
    # Мелани с каменным лицом
#    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    music ZigZag
    img 15461
    with fadelong
    w
    return

label ep29_dialogues3_melanie_monica_victoria_2a0:
    music ZigZag
    sound highheels_short_walk
    img 15462
    with fadelong
    w
    img 15463
    with diss
    melanie "Виктория, здравствуй. Я рада нашей встрече."
    music Groove2_85
    img 15464
    with diss
    victoria "Уже лучше."
    victoria "Хорошие подружки целуются при встрече. Потому что действительно рады встрече."
    img 15465
    with fade
    victoria "..."
    victoria "Ты же хорошая подружка?"
    # Мелани молча смотрит на нее
    music ZigZag
    img 15466
    with diss
    melanie "..."
    img 15467
    with fade
    melanie_t "Эта сучка откровенно издевается надо мнойю."
    melanie_t "Сейчас я поиграю по ее правилам..."
    img 15468
    with diss
    melanie_t "Она ведь не просто так позвала меня."
    melanie_t "Нужно узнать, что она хочет."
    melanie_t "Но я не оставлю подобное поведение безнаказанным..."
    img 15469
    with diss
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани подходит и целует Виктория в щеку, та самодовольно улыбается
    sound highheels_short_walk
    img 15470
    with fade
    w
    img 15471
    with diss
    w
    music Loved_Up
    img 15472
    with fade
    sound snd_kiss2
    w
    img 15473
    with diss
    victoria "Подружка соскучилась по мне?"
    # Мелани отходит от Викториии снова встает перед ее столом, сверлит ее взглядом
    music Groove2_85
    img 15474
    with fade
    melanie "..."
    img 15475
    with diss
    victoria "Я не слышу ответа..."
    victoria "Возможно, я ошибаюсь и ты не моя подружка?"
    victoria "Ты не соскучилась по мне?"
    music ZigZag
    img 15476
    with fade
    melanie "Конечно, соскучилась... Подружка."
    # Виктория довольно хихикает
    music Loved_Up
    img 15477
    with diss
    sound snd_woman_laugh3
    victoria "Раз ты так скучаешь по мне, подружка..."
    victoria "То, так уж и быть, я найду время, чтобы навестить тебя сегодня."
    victoria "Я приду к тебе вечером в гости."
    img 15478
    with fade
    victoria "И еще я хочу, чтобы вторая наша подружка тоже пришла."
    victoria "Уверена, она тоже соскучилась по мне. Как ты думаешь?"
    # Мелани удивленно приподнимает бровь
    music Power_Bots_Loop
    img 15479
#    with diss
    melanie "Ко мне в гости?"
    melanie "..."
    music Hidden_Agenda
    img 15480
    with fade
    victoria "Да. Я тут подумала, что ни разу не была у тебя в гостях."
    victoria "А подружки ходят друг другу в гости и устраивают девичники."
    img 15481
    with diss
    victoria "Сегодня вечером я хочу устроить девичник с моими хорошими подружками."
    victoria "Ты ведь рада, что я приду к тебе в гости?"
    victoria "Ты же хорошая подружка?"
    # Мелани молчит
    music Master_Disorder
    img 15482
    with fade
    melanie "..."
    img 15483
    with diss
    menu:
        "Согласиться на предложение Виктории":
            music Master_Disorder
            img 15484
            with fade
            melanie_t "Она явно что-то задумала..."
            melanie_t "Узнать это можно только одним способом - согласиться, чтобы она пришла ко мне."
            img 15485
            with diss
            melanie_t "Эта мелкая сучка не напугает меня, как бы она не старалась."
            melanie_t "Она ничего мне не сделает. Она и может только, что угрожать и все. На большее она не способна."
            pass
        "Отказаться":
            music ZigZag
            img 15486
            with fade
            melanie "Cегодня вечером я буду занята."
            melanie "Меня не будет дома."
            # Виктория хмурится и пристально смотрит на Мелани
            music Hidden_Agenda
            img 15487
            with diss
            victoria "Подружка хочет сказать, что у нее нет времени на меня?"
            img 15466
            with fade
            melanie "..."
            img 15487
            with diss
            victoria "Хорошая подружка отменила бы все свои планы."
            victoria "Иначе она может поссориться со мной."
            music Master_Disorder
            victoria "И тогда о ее маленькой тайне узнает один наш общий друг..."
            img 15489
            with fade
            melanie "..."
            img 15490
            with diss
            victoria "Подружка же не хочет со мной ссориться?"
            melanie_t "Чертова интриганка."
            pass
    # Мелани равнодушно
    music ZigZag
    img 15491
    with fade
    melanie "Я хорошая подружка и буду ждать тебя сегодня в гости."
    # Виктория довольно улыбается
    music Groove2_85
    img 15492
    with diss
    victoria "Я очень расстроюсь, если вторая наша подружка не придет сегодня."
    victoria "Я тогда подумаю, что она не соскучилась по мне."
    victoria "Как ты думаешь, ведь вторая подружка не захочет меня расстраивать?"
    # Мелани с покерфейсом
    music ZigZag
    img 15493
    with fade
    melanie "..."
    melanie "Я уверена, что она с радостью с тобой встретится."
    # Виктория хихикает
    sound snd_woman_laugh3
    img 15494
    with diss
    victoria "Не могу дождаться нашей встречи!"
    # Мелани бросает взгляд на дверь Дика, Виктория это видит и хмурит брови
    img 15495
    with fade
    w
    music Groove2_85
    img 15496
    with diss
    victoria "Ты можешь идти, подружка."
    victoria "Я понимаю, что ты с радостью повторила бы нашу встречу в этом кабинете..."
    victoria "Поэтому ты туда так смотришь. Но не расстраивайся. Мы увидимся сегодня вечером."
    # молча смотрят друг на друга
    music Master_Disorder
    img 15497
    with fade
    w
    img 15464
    with diss
    victoria "До встречи, подружка."
    victoria "Я принесу тебе подарок сегодня."
    victoria "И не только тебе..."
    img 15466
    with fade
    melanie "..."
    # Мелани бросает на нее непроницаемый взгляд, разворачивается и уходит
    # в заданиях появляется "Вернуться в студию и поговорить с Миссис Бакфетт"
#    $ log1 = t_("Вернуться в студию и поговорить с Миссис Бакфетт")
    return

# мысли Мелани в холле у лифта
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_2a:
    # после разговора с Викторией в офисе Дика
    melanie_t "Будет не так просто заставить Миссис Бакфетт придти на встречу с Викторией..."
    melanie_t "Нужно сказать это так, чтобы она не смогла отказаться."
    return

# Мелани заходит в отдел отчетов
label ep29_dialogues3_melanie_monica_victoria_3:
    # подхалим подрывается с места, системный администратор подскакивает, все остальные смотрят на Мелани с изумлением
    # подхалим подбегает к Мелани
    music stop
    img black_screen
    with diss
    sound highheels_run1  #изменить звук - бег нескольких человек
    pause 2.0
    music m80s_Things
    img 15403
    with fadelong
    w
    music Sneaky_Snitch
    img 15404
    with fade
    w5 "Мисс Мелани! Вы великолепно выглядите!"
    w5 "Я так рад Вас видеть в моем... нашем отделе!"
    img 15405
    with diss
    w5 "Желаете, я проведу Вам небольшую экскурсию?"
    w5 "Расскажу немного о нашей работе..."
    w5 "И угощу Вас чашечкой великолепного кофе!"
    # системный администратор смотрит на нее, открыв рот взглядом, как у Эрика
    music ZigZag
    img 15406
    with fade
    w2 "!!!"
    # Мелани смотрит на него, потом на подхалима и, игнорируя его предложения, спрашивает
    img 15407
    with diss
    melanie "Миссис Бакфетт у себя?"
    music Sneaky_Snitch
    img 15408
    with fade
    w5 "Да, Мисс Мелани. Она у себя в кабинете. Я провожу Вас!"
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    call refresh_scene_fade() from _call_refresh_scene_fade_233
    # подхалим ведет ее через офис и открывает ей дверь в кабинет Моники, та заходит
    # Моника сидит за своим столом со скучающим видом и "работает", Юлия как всегда вся в работе
    return

# кабинет Моники, Мелани зашла в кабинет
label ep29_dialogues3_melanie_monica_victoria_3a:
    # Мелани появляется в кабинете Моники
    music ZigZag
    img 15409
    with fadelong
    melanie_t "Миссис Бакфетт не так уж и плохо тут устроилась."
    melanie_t "По ней не скажешь, что она особо здесь перерабатывает."
    melanie_t "Хотя... Заметно, что ей здесь откровенно скучно..."
    w
    sound highheels_short_walk
    img 15410
    with fade
    m "Мелани? Ты ко мне?"
    music stop
    img black_screen
    with Dissolve(2.0)
    # затемнение экрана, надпись "Несколько минут спустя..."
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("5 минут спустя...")) from _call_textonblack_49
    img black_screen
    with Dissolve(2.0)
    return

# кабинет Моники, Мелани выходит из кабинета
label ep29_dialogues3_melanie_monica_victoria_3c:
    # Мелани выходит из кабинета Моники
    img black_screen
    with Dissolve(2.0)
    music Master_Disorder
    img 15426
    with fadelong
    melanie_t "Миссис Бакфетт явно напугана..."
    melanie_t "Теперь она точно придет ко мне."
    melanie_t "..."
    music ZigZag
    img 15427
    with fade
    melanie_t "Сейчас мне нужно поговорить с Бифом."
    melanie_t "Мне понравилась моя идея насчет небольшого отпуска."
    melanie_t "Думаю, он мне не откажет..."
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Спустя некоторое время...")) from _call_textonblack_50
    img black_screen
    with Dissolve(2.0)
    # в заданиях появляется "Пойти в кабинет Бифа и поговорить с ним"
#    $ log1 = t_("Пойти в кабинет Бифа и поговорить с ним")
    return

label ep29_dialogues3_melanie_monica_victoria_3c0:
    melanie_t "Сейчас мне нужно поговорить с Бифом."
    melanie_t "Мне понравилась моя идея насчет небольшого отпуска."
    melanie_t "Думаю, он мне не откажет..."
    return

label ep29_dialogues3_melanie_monica_victoria_3d:
    melanie_t "У меня нет желания общаться с этим... Боссом..."
    return False

# Мелани заходит в кабинет Бифа
label ep29_dialogues3_melanie_monica_victoria_4:
    # Биф, как обычно, сидит за столом с бутылкой алкоголя
    music Groove2_85
    img 15428
    with fadelong
    w
    img 15429
    with fade
    biff "А! Моя лучшая цыпочка пришла!"
    biff "Чем порадуешь папочку сегодня?"
    music ZigZag
    img 15430
    with diss
    melanie_t "У него вокруг одни цыпочки... Как это пошло..."
    sound highheels_short_walk
    img 15431
    with fade
    melanie "Биф, я хотела поговорить с тобой."
    melanie "Надеюсь, ты мне не откажешь..."
    # смотрит на него заигрывающе, Биф сидит расплывается в улыбке
    music Groove2_85
    img 15432
    with diss
    biff "Цыпочка что-то хотела попросить у меня?"
    biff "Говори. Папочка сегодня добрый."
    music Hidden_Agenda
    img 15433
    with fade
    melanie "..."
    sound Jump1
    img 15434
    with diss
    melanie "Возможно, ты позволишь мне..."
    melanie "Взять несколько выходных дней и немного отдохнуть?"
    music Groove2_85
    img 15435
    with fade
    biff "Цыпочка устала? Конечно, папочка позволит ей отдохнуть!"
    biff "..."
    biff "Только цыпочка сначала сделает фотосессию!"
    img 15436
    with diss
    melanie "Какую фотосессию?"
    img 15437
    with fade
    biff "Мне нужны фотографии для следующего номера журнала."
    biff "И я хочу видеть на этих фотографиях твое лицо, цыпочка..."
    img 15438
    with diss
    biff "И не только лицо..."
    biff "У цыпочки есть, что показать в объектив камеры."
    # Мелани приподнимает бровь удивленно
    music ZigZag
    img 15439
    with fade
    melanie "..."
    music Groove2_85
    img 15440
    with diss
    biff "В прошлый раз я просил тебя сделать фотосессию."
    biff "А ты сама не стала в ней сниматься."
    img 15441
    with fade
    biff "Поэтому мне сейчас нужны именно твои фотографии."
    biff "А не той цыпочки, которая притворяется Моникой Бакфетт."
    music ZigZag
    img 15442
    with diss
    melanie_t "Хм... Я надеялась, что его устроят фотографии Миссис Бакфетт..."
    img 15443
    with fade
    melanie "В каком костюме нужно провести съемку?"
    music Groove2_85
    img 15444
    with diss
    biff "Мне нравится твой костюм с красными трусиками..."
    img 15445
    with diss
    biff "Хочу увидеть тебя в нем на фотографиях!"
    melanie "..."
    img 15446
    with fade
    biff "Сделай эту фотосессию и можешь взять несколько выходных."
    biff "Папочка добрый, папочка разрешает."
    # сидит с видом "хозяин мира", улыбается
    music ZigZag
    img 15447
    with diss
    menu:
        "Согласиться на фотосессию":
            pass
        "Отказаться (пропуск фотосессии)":
            music ZigZag
            img 15448
            with fade
            melanie_t "Он намекнул, что ему нужны откровенные фотографии..."
            melanie_t "В этом костюме с трусиками другие фотографии и не получатся..."
            melanie_t "..."
            melanie_t "Думаю, Биф обойдется без этих фотографий."
            img 15449
            with diss
            melanie "Биф, я пока не совсем готова к фотосессии..."
            melanie "Я ее сделаю, но позже..."
            img 15450
            with diss
            melanie_t "... возможно."
            img 12847
            with fade
            biff "Папочка добрый, поэтому разрешает тебе подумать."
            return False # пропуск фотосессии, сразу в гримерку, оттуда домой на девичник
    img 15448
    with fade
    melanie_t "Что ж... У меня как раз есть время до встречи с мелкой дрянью Викторией."
    img 15451
    with diss
    melanie "Хорошо, Биф. Я сделаю, как ты хочешь." # без эмоций
    music Groove2_85
    img 15452
    with fade
    biff "Хорошая цыпочка. Папочка цыпочкой очень доволен."
    img 15453
    with diss
    melanie_t "Нужно пойти в фотостудию. Надеюсь, Алекс на месте."
    # в заданиях появляется "Провести фотосессию"
#    $ log1 = t_("Провести фотосессию")
    return

# Мелани заходит в фотостудию
label ep29_dialogues3_melanie_monica_victoria_5:
    # Алекс на своем рабочем месте
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 22583
    with fadelong
    alex_photograph "Мелани! Надеюсь, ты пришла поработать со мной?"
    img 22584
    with fade
    melanie "Да, Алекс. Сегодня у нас фотосессия."
    return
#    menu:
#        "Переодеться":
#            pass

label ep29_dialogues3_melanie_monica_victoria_5a1:
    img 22585
    with fadelong
    music ZigZag
    sound highheels_short_walk
    # появляется окно выбора костюма, там только один (с красными трусиками)
    melanie "Я сейчас переоденусь и вернусь."
    # через несколько минут
    # в студии появляется Мелани в костюме, Алекс смотрит на нее как на богиню
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music ZigZag
    img 22586
    with fade
    sound highheels_short_walk
    alex_photograph "Мелани! Ты великолепна!!!"
    img 22587
    with diss
    melanie_t "Мне не нравится идея фотосессии в этом костюме."
    melanie_t "Он практически ничего не прикрывает."
    melanie_t "Надо сказать Алексу, чтобы не брал откровенных ракурсов."
    # Мелани бросает на него взгляд и идет на съемочную площадку
    music Hidden_Agenda
    img 22588
    with fade
    melanie "Алекс?"
    alex_photograph "Да, Мелани?"
    melanie "Ты все еще хочешь, чтобы мои фотографии появились в твоей личной коллекции?"
    # Алекс воодушевленно
    img 22589
    with diss
    alex_photograph "Конечно, Мелани! Я давно мечтаю об этом! Так ты согласна?"
    melanie "Алекс, я обещаю подумать об этом. При одном условии."
    alex_photograph "???"
    img 22590
    with fade
    melanie "Мое условие простое, Алекс."
    melanie "Никаких откровенных ракурсов на этой фотосессии."
    melanie "Тогда я обдумаю возможность согласиться на твое предложение..."
    music Groove2_85
    img 22591
    with diss
    alex_photograph "Мелани! Ты можешь не переживать! Я сделаю все, как ты скажешь!"
    melanie "Отлично, Алекс. У меня мало времени. Приступим?"
    # Мелани принимает первую позу
    img 22592
    with fade
    alex_photograph "Итак, мотор!"
    return

label ep29_dialogues3_melanie_monica_victoria_5a0:
    # после окончания фотосессии
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 22645
    with fadelong
    alex_photograph "Мы закончили, Мелани! Ты была просто великолепна!!!"
    melanie "..."
    alex_photograph "Мелани, ты подумаешь над моим предложением?"
    # Мелани смотрит на него пристально
    music ZigZag
    img 22646
    with fade
    melanie "Я уже подумала, Алекс."
    melanie "Я не могу себе позволить сотрудничать с фотографом..."
    melanie "Который так пренебрежительно относится к моим просьбам."
    img 22647
    with diss
    alex_photograph "Мелани... Но ведь я..."
    img 22648
    with diss
    melanie "Алекс, ответ 'нет'."
    melanie "Я не хочу больше ничего слышать о твоей личной коллекции."
    img 22649
    with fade
    alex_photograph "Но..."
    melanie "Надеюсь, ты доволен сегодняшней фотосессией..."
    melanie "..."
    # Алекс смотрит расстроенно

    melanie_t "Нужно переодеться и ехать домой. Скоро придут Миссис Бакфетт и Виктория."
    # в заданиях появляется "Идти в гримерку, переодеться"
#    $ log1 = t_("Идти в гримерку, переодеться")
    return

# Гримерка
label ep29_dialogues3_melanie_monica_victoria_6:
    # Мелани переоделась, сидит возле зеркала
    melanie_t "Ну что ж... Посмотрим, что мелкая сучка Дика приготовила нам."
    melanie_t "Что бы это ни было, меня это вряд ли порадует. Как и Миссис Бакфетт."
    melanie_t "Должен существовать способ поставить Викторию на место..."
    melanie_t "Возможно, стоит поговорить об этом с Миссис Бакфетт..."
    # в заданиях появляется "Нужно ехать домой. Скоро придет Виктория"
#    $ log1 = t_("Нужно ехать домой. Скоро придет Виктория")
    return

# вызов "ep29_dialogues4_lesbian_threesome_victoria_1a"

# мысли Мелани в холле у лифта
# не рендерить!!!
label ep29_dialogues3_melanie_monica_victoria_6a:
    # едет к себе домой, при любом клике, кроме выхода
    melanie_t "Сейчас мне нужно ехать к себе домой."
    melanie_t "Скоро придут Миссис Бакфетт и Виктория."
    return

# мысли Моники после сцены с Викторией, когда вышла от Мелани
label ep29_dialogues3_melanie_monica_victoria_6b:
    mt "ЧТО... ЭТО... БЫЛО?!"
    mt "!!!"
    mt "Когда я верну себе все, что у меня отняли..."
    mt "Эта сучка будет первой, кому я буду мстить!!!"
    return
