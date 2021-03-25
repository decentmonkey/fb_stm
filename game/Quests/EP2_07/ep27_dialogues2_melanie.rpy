# Мелани2, разговор с Викторией
label ep27_dialogues2_melanie1:
    # Гримерка
    # Секретарша стоит перед сидящей Мелани, закрывая зад руками
    # Секретарша говорит по деловому, Мелани отвечает надменно.
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Утро...")) from _call_textonblack_24
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 13926
    with fadelong
    secretary "Мисс Мелани, со мной связалась Мисс Виктория, секретарь Мистера Дика." #-
    secretary "Она просила передать Вам, чтобы Вы посетили его офис."
    img 13927
    with diss
    melanie "Она сообщила причину необходимости визита?" #+
    img 13928
    with fade
    secretary "Мисс Мелани, она сказала что это в Ваших интересах." #+
    img 13929
    with diss
    melanie "Эта девочка так и сказала, дословно?" #-
    img 13930
    with fade
    secretary "Да, Мисс Мелани, она так и сказала."
#    img 13931
    music Master_Disorder
    img 13936
    with diss
    menu:
        "Идти на встречу с Викторией.":
            pass
        "Отказаться от встречи (пропуск всех событий с Викторией).":
            music Groove2_85
            img 13932
            with fade
            melanie "Если эта девочка еще раз позвонит, то передайте ей, что мои интересы ее никак не касаются." #+
            img 13933
            with diss
            secretary "Хорошо, Мисс Мелани, я передам."
            return False
    music Groove2_85
    img 13934
    with fade
    melanie "..." #+
    melanie "Хорошо, спасибо. Я подумаю насчет этого."

    # Фотостудия, кадр Алекс улыбается (в своей дурацкой позе) и смотрит на уходящую секретаршу.
    # Та стыдливо прикрывается сзади и испуганно косится.
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    sound highheels_run2
    music Hidden_Agenda
    img 14040
    with fadelong
    w
    img 14041
    with diss
    w
    sound Jump2
    img 14042
    with diss
    w
    img 14043
    with diss
    w
    sound Jump1
    img 14044
    with diss
    w
    sound Jump2
    img 14045
    with Dissolve(0.2)
    w

    music stop
    img black_screen
    with diss
    pause 2.0
    # Снова гримерка
    music Master_Disorder
    img 13935
    with fadelong
    melanie "В моих интересах?" #-
    melanie "Очень странный подбор слов..."
    melanie "Возможно, это перефразировала его секретарь."
    melanie "Юная девочка, ревнующая своего Босса."
    img 13936
    with diss
    melanie "Странно что Дик не связался со мной напрямую..." #+
    melanie "Ладно, стоит навестить его."
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 2.0
    return True

label ep27_dialogues2_melanie2:
    # Мелани входит в здание Дика. Ее видит секретарь на рецепшене.
    # 2-3 кадра как подходит.
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    music m80s_Things
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_25
    scene black_screen
    with Dissolve(1)
#    music Groove2_85
    img 13937
    with fadelong
    w
    img 13938
    with diss
    w
    img 13939
    with diss
    w
    img 13942
    with diss
    w
    img 13940
    with fade
    reception_secretary "Здравствуйте, Мисс Мелани!" #+
    reception_secretary "Рада снова видеть Вас!"
    reception_secretary "Вы решили навестить Мистера Дика?"
    music ZigZag
    img 13941
    with diss
    melanie "Да, верно." #-
    melanie "Его офис все там-же?"
    img 13943
    with fade
    reception_secretary "Да, его офис там же." #-
    reception_secretary "Разрешите Вас проводить туда?"
    img 13944
    with diss
    melanie "Нет необходимости в этот раз." #+
    melanie "Я помню как туда подняться."
    img 13945
    with fade
    reception_secretary "Если что-то понадобится, дайте мне знать!" #-
    img 13946
    with diss
    melanie "Спасибо." #- #уходит

    music stop
    img black_screen
    with diss
    sound snd_lift
    pause 2.0
    # звук лифта, Мелани заходит в приемную к Дику
    # Там секретарши нет
    music ZigZag
    img 13947
    with fadelong
    melanie "Странно, а где эта маленькая девочка, которая думает что знает что и в чьих интересах..." #-
    melanie "Надо высказать Дику свое неудовольствие ей."
    img 13948
    with diss
    melanie "..." #- вид из-за стола (пустого) Мелани смотрит на стол
    img 13949
    with fade
    melanie "И где сам Дик?" #+ вид сзади Мелани, на дверь
    melanie "Наверное, в своем кабинете..."

    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound highheels_short_walk
    pause 1.5
    sound snd_door_close1
    music Groove2_85
    # Мелани заходит в кабинет Дика. Там на кресле надменно сидит Виктория
    img 13950
    with fadelong
    dick_secretary "О, Мисс Мелани..." #+
    dick_secretary "Проходите, я Вас как раз ждала..."
    music ZigZag
    # Мелани надменно отвечает
    img 13951
    with fade
    melanie "Девочка, я не ошиблась кабинетом?" #-
    melanie "Или, может быть, это ты ошиблась стулом?"
    img 13952
    with diss
    melanie "Я пришла к Мистеру Дику, твоему Боссу." #+
    melanie "Любишь посидеть на его месте, пока его нет?"
    music Groove2_85
    img 13953
    with fade
    dick_secretary "Вы не ошиблись кабинетом, Мисс Мелани." #-
    dick_secretary "И Вы пришли ко мне, а не к Мистеру Дику."
    dick_secretary "Это я пригласила Вас..."
    music ZigZag
    img 13954
    with fade
    melanie "Ты?!" #-
    melanie "Не слишком-ли смелая инициатива, юная девочка?"
    melanie "Это слишком много чести для маленькой секретарши, которая спит со своим Боссом."
    melanie "Ты ведь знаешь кто я такая."
    music Groove2_85
    img 13955
    with diss
    dick_secretary "Я знаю кто Вы такая, Мисс Мелани..." #+
    music ZigZag
    img 13956
    with fade
    melanie "Ты ревнуешь и делаешь глупости, но помни." #+
    melanie "Я могу щелчком пальцев лишить тебя милости твоего Босса и этой работы."
    melanie "Ты играешь с огнем, девочка."
    music Groove2_85
    img 13957
    with fade
    dick_secretary "Мисс Мелани." #-
    dick_secretary "Меня трогают Ваши слова, но я трачу сейчас свое время на разговор, который в Ваших же интересах."
    music ZigZag
    img 13958
    with fade
    melanie "У нас с тобой разные интересы, девочка." #-
    melanie "И они никак не могут пересекаться."
    melanie "Ты не можешь сказать ничего, что могло бы заинтересовать меня."
    melanie "Ты очень предсказуемая и примитивная."
    melanie "Я вижу тебя насквозь."
    music Groove2_85
    img 13959
    with fade
    dick_secretary "Мисс Мелани, Вы продолжаете делать все, чтобы более и более нравиться мне." #-

    # Серьезное лицо
    img 13960
    with diss
    dick_secretary "Но перейдем к делу."  #+ сбоку
    img 13961
    with fade
    dick_secretary "В круг моих знакомых входит фотограф, папарацци." #+ прямо, чуть снизу
    dick_secretary "Он следит за знаменитостями, вроде Вас."

    # Надменное, напряженное, сосредоточенное
    img 13962
    with diss
    melanie "..." #+

    # Сосредоточенное, злое
    img 13963
    with diss
    dick_secretary "..." #+

    # Надменное
    music ZigZag
    img 13964
    with fadelong
    melanie "Таких знаменитых моделей как Я окружает множество извращенцев." #-
    melanie "Я к этому привыкла."
    melanie "Чем ты хочешь меня удивить, девочка?"


    # деловое
    music stop
    img black_screen
    with diss
    pause 0.5
    music Groove2_85
    img 13965
    with fade
    dick_secretary "Дело в том, что Мистер Дик уже какое-то время занимается делом некой Моники Бакфетт." #-
    dick_secretary "Она чем-то неугодила некоему Мистеру Маркусу и теперь отчаянно нуждается в помощи."
    dick_secretary "Вы знаете что-нибудь про это, Мисс Мелани?"

    # Мелани напряжена, но старается держаться надменно
    music ZigZag
    img 13966
    with fade
    melanie "Я знаю Миссис Бакфетт. Это мой бывший Босс." #-
    melanie "Она покинула место работы и теперь я не знаю что с ней."
    img 13967
    with diss
    melanie "Меня это неинтересует." #+
    melanie "Это все?"
    music Groove2_85
    sound snd_paper1
    img 13968
    with fade
    dick_secretary "Мисс Мелани." #-
    dick_secretary "Пожалуйста, взгляните на эти снимки."

    # Мелани подходит
    img 13969
    with fade
    melanie "..."
    sound snd_paper1
    img 13970
    with diss
    dick_secretary "Вот на этот."
    # Кладет на стол снимок как Мелани показывает грудь Дику
    img 13971
    with diss
    w
    img 13972
    with diss
    w
    sound snd_paper2
    img 13973
    with fade
    dick_secretary "И вот на этот."
    # Кладет снимок как Мелани общается с Моникой у нее дома
    music Power_Bots_Loop
    img 13974
    with hpunch
    w
    img 13975
    with diss
    w
    music ZigZag
    img 13976
    with fade
    melanie "И что с того?" #-
    melanie "Эти снимки сделаны в разное время."
    melanie "На первом - моя личная жизнь."
    melanie "На втором - Миссис Бакфетт навестила меня для того, чтобы..."

    music Groove2_85
    # крупным, ехидно
    sound snd_woman_laugh3
    img 13977
    with diss
    dick_secretary "Для того, чтобы попросить Вас о помощи." #+

    # зло
    music ZigZag
    img 13978
    with fade
    melanie "Это не твое дело, девочка." #+
    melanie "Я понимаю твою ревность, но смирись с тем, что Я нравлюсь твоему Боссу больше чем ТЫ."

    # Виктория злится, крупный план
    music Groove2_85
    img 13979
    with diss
    dick_secretary "..." #+

    # Виктория снова надменно улыбается
    sound snd_paper2
    img 13980
    with fadelong
    dick_secretary "Если мы положим эти снимки в следующем порядке..." #- сбоку издалека
    # Кладет снимки, где сначала разговор с Моникой, затем с Диком
    img 13981
    with fade
    dick_secretary "То становится очевидно, что Миссис Бакфетт пришла к Вам за помощью." # сверху на снимки
    dick_secretary "Затем Вы помогли ей, соблазнив Мистера Дика, моего Босса."
    img 13983
    with diss
    melanie "..." #+
    img 13984
    with fade
    dick_secretary "Мистер Маркус связывался со мной какое-то время назад." #-
    dick_secretary "И просил сообщить ему, если кто-либо еще будет пытаться помочь Миссис Бакфетт."

    # Мелани переживает
    music Power_Bots_Loop
    img 13985
    with hpunch
    melanie "!!!" #+
    img 13986
    with fade
    dick_secretary "Я решила пойти Вам навстречу и сообщила Вам об этом до того, как эти кадры попадут на публику." #+
    dick_secretary "И до того, как эти кадры попадут к Мистеру Маркусу."
    dick_secretary "Я подумала что это может заинтересовать Вас, Мисс Мелани."
    music Power_Bots_Loop
    img 13987
    with diss
    melanie "..." #-
    music Groove2_85
    img 13988
    with fade
    dick_secretary "Вам это интересно или мы можем закончить разговор?" #-
    music Hidden_Agenda
    img 13989
    with fade
    melanie "Виктория, я бы..." #+
    img 13990
    with diss
    melanie "Я бы предпочла, чтобы эти фото не попадали на публику и к Мистеру Маркусу вовсе..." # сбоку издалека
    music Groove2_85
    img 13991
    with fade
    dick_secretary "Это весьма сложно, Мисс Мелани." #-
    dick_secretary "Мой знакомый хочет заработать на этих фото."
    img 13992
    with diss
    dick_secretary "К тому же, мне показалось что Мистер Маркус влиятельный человек." #+
    dick_secretary "И может достойно отблагодарить меня за помощь."
    dick_secretary "Вы знакомы с ним?"
    music Power_Bots_Loop
    img 13993
    with hpunch
    melanie "!!!" #+
    img 13994
    with diss
    melanie "Я..." #-
    melanie "Я немного знакома с ним..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 13995
    with fadelong
    melanie "Мисс Виктория." #+
    melanie "Мы с Вами умные люди."
    melanie "Я уверена, что мы можем найти компромисс."
    melanie "Назовите сумму."
    music Groove2_85
    img 13996
    with fade
    dick_secretary "Ах, деньги..." #-
    dick_secretary "Да, это разумное предложение."
    dick_secretary "И я готова принять их, но..."
    img 13997
    with diss
    melanie "Что Но?.." #+
    img 13998
    with fade
    dick_secretary "Я не принимаю подарков от незнакомых людей..." #+
    music Power_Bots_Loop
    img 13999
    with diss
    melanie "Что ты имеешь ввиду, девочка?" #+
    music Groove2_85
    img 14000
    with diss
    dick_secretary "Мисс Виктория." #+ зло

    # злится в сторону
    music Power_Bots_Loop
    img 14001
    with fade
    melanie "..." #+

    # смотрит язвительно, но напряженно
    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 14002
    with fadelong
    melanie "Что Вы имеете ввиду, Мисс Виктория?" #-
    music Groove2_85
    img 14003
    with fadelong
    dick_secretary "Видите-ли, Мисс Мелани." #-
    dick_secretary "У меня здесь ответственная работа."
    dick_secretary "У меня строгий Босс, который учит меня не доверять незнакомым людям."
    dick_secretary "Поэтому я не могу принять у Вас Ваши деньги."
    music Power_Bots_Loop
    img 14004
    with diss
    melanie "..." #+
    img 14005
    with diss
    dick_secretary "..." #+ прищурившись зло
    music ZigZag
    img 14006
    with fadelong
    melanie "Что мне сделать, чтобы Вы стали доверять мне, Мисс Виктория." #-
    music Groove2_85
    img 14007
    with fade
    dick_secretary "Вы должны сделать так, чтобы я могла доверять Вам, Мисс Мелани." #-

    # подозрительно
    music ZigZag
    img 14008
    with fade
    melanie "Что для этого надо сделать?" #+

    # ехидно
    music Loved_Up
    sound snd_woman_laugh2
    img 14009
    with diss
    dick_secretary "Стать моей подружкой." #+
    music ZigZag
    img 14010
    with fade
    melanie "Что мне надо сделать, чтобы стать Вашей подружкой, Мисс Виктория?" #-
    music Groove2_85
    img 14011
    with fade
    dick_secretary "Мисс Мелани, Вам надо попросить меня о том, чтобы стать ей." #-
    dick_secretary "Затем вести себя как хорошая подружка."
    dick_secretary "С плохими подружками я не дружу."
    dick_secretary "И для плохих подружек я не буду идти на жертвы, чтобы не распространять их неосторожные фото..."
    music Power_Bots_Loop
    img 14012
    with diss
    melanie "..." #+ напряжена
    img 14013
    with diss
    dick_secretary "..." #+ язвительная (вообще она все время язвительная, если не злится)
    img 14014
    with diss
    melanie "!!!" #+
    img 14015
    with diss
    dick_secretary "???" #+ язвительно, смотрит искоса вопрошающе
    img 14016
    with fade
    menu:
        "Попросить Викторию стать ее подружкой.":
            pass
        "Уйти.":
            music stop
            img black_screen
            with diss
            pause 1.5
            music Power_Bots_Loop
            img 14017
            with fadelong
            melanie "Мне надо подумать!" #- уходит
            img 14018
            with diss
            dick_secretary "Думайте быстрее, Мисс Мелани!"
            return 0

    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 14019
    with fadelong
    melanie "Мисс Виктория..." #-
    melanie "Я хочу стать Вашей подружкой."
    music Groove2_85
    img 14020
    with diss
    dick_secretary "Неубедительно." #-
    dick_secretary "Я не верю в искренность Ваших слов."
    dick_secretary "Попробуйте еще раз."

    # в сторону
    music Power_Bots_Loop
    img 14021
    with diss
    melanie "!!!" #+
    music ZigZag
    img 14022
    with fade
    melanie "Мисс Виктория..." #-
    melanie "Я - Мелани, самая популярная модель Модного Журнала."
    melanie "Я очень известна и знаменита."
    melanie "И Я бы очень хотела стать Вашей подружкой."
    melanie "И была бы счастлива, если бы Вы приняли мою дружбу с Вами..."
    music Groove2_85
    img 14023
    with fade
    dick_secretary "Хорошо, но ты обещаешь быть хорошей подружкой?" #-
    dick_secretary "Каждый четверг присылать мне сертификат на $ 10.000 и делать все что я скажу."
    music Power_Bots_Loop
    img 14024
    with hpunch
    melanie "!!!" #+
    img 14025
    with diss
    dick_secretary "..." #+ язвительно

    # Мелани смотрит близким планом на фото
    img 14026
    with diss
    melanie "!!!"

    # Зло щурится
    img 14027
    with diss
    dick_secretary "???" #+
    music stop
    img black_screen
    with diss
    pause 1.0
    music ZigZag
    img 14028
    with fadelong
    melanie "Да, я согласна..." #-
    music Groove2_85
    img 14029
    with fade
    dick_secretary "Повтори все что я сказала!" #-
    music Power_Bots_Loop
    img 14030
    with diss
    melanie "!!!" #+
    img 14031
    with diss
    dick_secretary "!!!" #+ зло

    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 14032
    with fadelong
    melanie "Я..." #-
    melanie "Я обещаю что буду хорошей подружкой."
    melanie "И буду каждый четверг присылать Вам сертификат на $ 10.000."
    img 14033
    with diss
    dick_secretary "И?" #-
    music Power_Bots_Loop
    img 14034
    with diss
    melanie "..." #+
    img 14035
    with diss
    dick_secretary "..." #+
    music Hidden_Agenda
    img 14036
    with fadelong
    melanie "И буду делать что Вы скажете, Мисс Виктория." #-
    music Groove2_85
    img 14037
    with fade
    dick_secretary "Хорошо, подружка." #-
    dick_secretary "Пока ты будешь хорошей подружкой, эти фото останутся только у меня."
    img 14038
    with diss
    melanie "..." #+

    if monicaShowedBoobsToVictoriaCamera == True:
        img 14039
        with fade
        dick_secretary "Да, кстати." #-
        dick_secretary "У меня есть еще одна подружка, которую ты хорошо знаешь."

        # Кладет фото Моники, где она показывает грудь на телефон
        sound snd_paper2
        img 14046
        with diss
        w
        # Мелани крупным планом, напряжена
        img 14047
        with diss
        melanie "..."
        img 14048
        with diss
        dick_secretary "Она навещает меня регулярно." #крупный план фотографии Моники
        dick_secretary "Однако, она не всегда себя хорошо ведет."
        dick_secretary "И, чтобы сновать стать хорошей подружкой, ей приходится просить прощения у меня."
        sound snd_woman_laugh
        img 14049
        with diss
        melanie "..." # вид из фотографии на Мелани
    else:
        img 14039
        with fade
        dick_secretary "Да, кстати." #-
        dick_secretary "У меня есть еще одна подружка, которую ты хорошо знаешь."
        dick_secretary "Она навещает меня регулярно." #крупный план фотографии Моники
        dick_secretary "Однако, она не всегда себя хорошо ведет."
        dick_secretary "И, чтобы сновать стать хорошей подружкой, ей приходится просить прощения у меня."
        sound snd_woman_laugh
        img 14049
        with diss
        melanie "..." # вид из фотографии на Мелани

    if monicaShowedBoobsToVictoriaCamera == True:

        # Достает телефон
        sound Jump1
        img 14050
        with fade
        dick_secretary "Это хорошо что ты одела ту же шубку, что и на фото."  #-
        dick_secretary "Можно сделать хороший кадр."
        sound snd_woman_laugh3
        img 14051
        with diss
        melanie "..." #-
        img 14052
        with fade
        dick_secretary "Могу поспорить, что под этой шубкой ничего нет." #+ держит телефон
        dick_secretary "Ты ведь пришла для того, чтобы трясти своими сиськами перед Диком, да?"
        music Power_Bots_Loop
        img 14053
        with diss
        melanie "!!!" #+

        # В одной руке телефон, держащий для фото, в другой - фото Моники с грудью
        # Поворачивает фото к Мелани. Видто спину Мелани, фото и ехидную Викторию
        music Groove2_85
        sound snd_paper1
        img 14054
        with fade
        dick_secretary "Давай, показывай их, как это сделала первая подружка." #

        # Поворачивает фото к себе, держа рядом с телефоном
        img 14055
        with diss
        dick_secretary "Я хочу сделать фото и сравнить Ваши сиськи."

        # возмущенно
        music Power_Bots_Loop
        img 14056
        with fade
        melanie "!!!" #+
        img 14057
        with diss
        melanie "Я не буду показывать свою грудь!" #-
        melanie "Я уважающая себя женщина и..."

        # пренебрежительно
        # убирает телефон и фото
        sound snd_paper2
        img 14058
        with fade
        dick_secretary "Ты плохая подружка! Можешь уходить!" #-
        dick_secretary "Хорошая подружка не пререкается со мной."
        img 14059
        with diss
        melanie "!!!" #+
        img 14060
        with fade
        dick_secretary "Можешь идти, я не задерживаю тебя!" #+
        img 14061
        with diss
        melanie "!!!" #+
        img 14062
        with diss
        dick_secretary "..." #+
    else:
        # Достает телефон
        sound Jump1
        img 14052
        with fade
        dick_secretary "Это хорошо что ты одела ту же шубку, что и на фото."  #-
        dick_secretary "Можно сделать хороший кадр."
        sound snd_woman_laugh3
        img 14051
        with diss
        melanie "..." #-
        img 14052
        with fade
        dick_secretary "Могу поспорить, что под этой шубкой ничего нет." #+ держит телефон
        dick_secretary "Ты ведь пришла для того, чтобы трясти своими сиськами перед Диком, да?"
        music Power_Bots_Loop
        img 14053
        with diss
        melanie "!!!" #+

        music Power_Bots_Loop
        img 14056
        with fade
        melanie "!!!" #+
        melanie "Я не буду показывать свою грудь!" #-
        melanie "Я уважающая себя женщина и..."

        # пренебрежительно
        # убирает телефон и фото
        sound snd_paper2
        img 14058
        with fade
        dick_secretary "Ты плохая подружка! Можешь уходить!" #-
        dick_secretary "Хорошая подружка не пререкается со мной."
        img 14059
        with diss
        melanie "!!!" #+
        img 14060
        with fade
        dick_secretary "Можешь идти, я не задерживаю тебя!" #+
        img 14061
        with diss
        melanie "!!!" #+
        img 14062
        with diss
        dick_secretary "..." #+

    music stop
    img black_screen
    with diss
    pause 1.5
    music ZigZag
    img 14063
    with fadelong
    melanie "..." #-
    melanie "Хорошо..."
    melanie "Я сделаю это, но на этом все, договорились?"
    music Groove2_85
    img 14064
    with fade
    dick_secretary "Это только начало, подружка!" #-
    dick_secretary "Да, и еще одно пререкание и я с тобой больше не дружу!"
    img 14065
    with diss
    melanie "!!!" #+

    # Снова достает телефон и фото
    sound Jump1
    img 14052
    with fade
    dick_secretary "Давай, показывай!" #+ держит телефон
    dick_secretary "Мне нужно фото, дискредитирующее тебя перед Мистером Диком!"
    melanie "..." #-

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    # Мелани показывает грудь
    img 14070
    with fadelong
    w
    # щелчок фото
    sound camera_lens1
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14069
    else:
        img 14068
    with Dissolve(0.2)
    w
    call photoshop_flash() from _call_photoshop_flash_164
    w
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14071
    else:
        img 14070
    with Dissolve(0.2)
    w
    call photoshop_flash() from _call_photoshop_flash_165
    w
    music Groove2_85
    img 14068
    with diss
    dick_secretary "Отлично!" #+ держит телефон
    dick_secretary "Теперь Мистер Дик поймет, что ты такая же шлюха, как и Бакфетт!"
    music Power_Bots_Loop
    img 14072
    with diss
    melanie "!!!" #+
    music Groove2_85
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14073
        with fade
        dick_secretary "У тебя красивая грудь, подружка!" #-
        img 14074
        with diss
        melanie "Я знаю..." #-
        melanie "Мисс Виктория..."
        melanie "Все мечтают о такой груди, как у меня..."

        # Удаление
        img 14075
        with fade
        dick_secretary "Но скажи, чья грудь лучше?" #-
    else:
        img 14068
        with fade
        dick_secretary "У тебя красивая грудь, подружка!" #-
        img 14072
        with diss
        melanie "Я знаю..." #-
        melanie "Мисс Виктория..."
        melanie "Все мечтают о такой груди, как у меня..."
        # Удаление
        img 14052
        with fade
        dick_secretary "Но скажи, чья грудь лучше?" #-


    # Крупным
    img 14076
    with diss
    dick_secretary "Твоя или моя?" #+
    img 14077
    with diss
    melanie "..." #+

    # прищуривается
    img 14078
    with fade
    dick_secretary "..." #+
    dick_secretary "Хорошенько подумай, прежде чем ответить, подружка..."
    img 14079
    with diss
    melanie "..." #+
    img 14080
    with diss
    melanie "Ваша грудь лучше, Мисс Виктория..." #-
    sound snd_woman_laugh

    if monicaShowedBoobsToVictoriaCamera == True:
        img 14081
    else:
        img 14076
    with fade
    dick_secretary "Правильный ответ." #-
    dick_secretary "Хорошая подружка!"

    if game.extra == True:
        dick_secretary "А теперь потряси своими сиськами. Я хочу снять видео!"
        music Power_Bots_Loop
        img 14072
        with diss
        melanie "!!!"
        music Groove2_85
        img 14068
        with fade
        dick_secretary "Мне надо повторить? Хочешь быть плохой подружкой?"
        img 14079
        with diss
        melanie "..."
        # video shaking boobs
        music stop
        img black_screen
        with diss
        pause 2.0
#        music Loved_Up2
        music audio_Melanie_Victoria_Boobs_1
        if monicaShowedBoobsToVictoriaCamera == True:
            scene black
            image videov_Melanie_Victoria_Boobs_1_1 = Movie(play="video/v_Melanie_Victoria_Boobs_1_1.mkv", fps=30)
            show videov_Melanie_Victoria_Boobs_1_1
            wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_2 = Movie(play="video/v_Melanie_Victoria_Boobs_1_2.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_2
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_3 = Movie(play="video/v_Melanie_Victoria_Boobs_1_3.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_3
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_4 = Movie(play="video/v_Melanie_Victoria_Boobs_1_4.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_4
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_5 = Movie(play="video/v_Melanie_Victoria_Boobs_1_5.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_5
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_6 = Movie(play="video/v_Melanie_Victoria_Boobs_1_6.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_6
        wclean
        scene black
        image videov_Melanie_Victoria_Boobs_1_7 = Movie(play="video/v_Melanie_Victoria_Boobs_1_7.mkv", fps=30)
        show videov_Melanie_Victoria_Boobs_1_7
        wclean
    music stop
    img black_screen
    with diss
    pause 1.5
    # Мелани закрывается
    music Groove2_85
    img 14082
    with fade
    melanie "Мисс Виктория, мы закончили?" #-
    melanie "Я могу идти?"
    img 14083
    with diss
    dick_secretary "Нет, подружка." #-
    dick_secretary "Я хочу чтобы ты мне помогла..."
    img 14084
    with diss
    melanie "..." #+
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14085
        with fade
    melanie "В чем Вы хотите чтобы я Вам помогла, Мисс Виктория?" #-
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14086
        with diss
    else:
        img 14083
        with diss
    dick_secretary "Подружка, я ждала тебя здесь целый день." #+
    # Кладет ногу в сапоге на стол
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Loved_Up
    img 14087
    with fadelong
    w
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14088
        with diss
        w
    sound desk_open
    img 14089
    with diss
    w
    sound Jump1
    img 14090
    with fade
    dick_secretary "Я всегда ношу сапожки, чтобы выглядеть красиво." #-
    dick_secretary "И, пока я тебя ждала, у меня затекла ножка."

    # смотрит на ногу
    img 14091
    with diss
    melanie "..."
    img 14092
    with fade
    dick_secretary "Пожалуйста, сними этот сапожок!" #+
    dick_secretary "Будь хорошей подружкой!"
    music Power_Bots_Loop
    img 14093
    with diss
    melanie "!!!" #+

    # смотрит вопросительно - язвительно
    img 14094
    with diss
    dick_secretary "..." #+

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    # мелани начинает снимать сапог
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14096
        with fadelong
        w
    sound snd_zip
    img 14095
    with diss
    w
    img 14097
    with diss
    w
    sound snd_zip
    img 14098
    with diss
    w
    # снимает сапог
    sound snd_boot1
    img 14099
    with fade
    dick_secretary "Хорошо, а теперь сделай моей ножке массаж своей грудью..." #-
    music Power_Bots_Loop
    img 14100
    with hpunch
    melanie "ЧТО?!" #+
    img 14101
    with diss
    melanie "Моей грудью?! Трогать моей грудью твои ноги?!!" #-
    img 14102
    with diss
    dick_secretary "Кажется я слышала пререкание?" #+
    dick_secretary "Или мне послышалось?"

    # Мелани отвернулась в бешенстве
    img 14103
    with diss
    melanie "!!!" #+
    img 14104
    with fade
    dick_secretary "Мне послышалось?" #-
    dick_secretary "Или передо мной плохая подружка?!"

    # Мелани смотрит на фото
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14105
        with diss
    melanie "!!!"

    # Зло смотрит
    img 14106
    with diss
    dick_secretary "..." #+
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 14107
    with fadelong
    melanie "Вам послышалось, Мисс Виктория..." #-
    img 14108
    with fade
    dick_secretary "Давай, подружка!" #-
    dick_secretary "Твои сиськи - это твой основной рабочий инструмент."
    dick_secretary "С помощью этого инструмента ты сделала карьеру."

    # Мелани садится и тянется грудью к ноге Виктории
    sound desk_open
    img 14109
    with diss
    dick_secretary "Почему бы не использовать его, чтобы снять усталось у лучшей подружки?"
    img 14110
    with diss
    melanie "..."
    sound snd_woman_laugh2
    img 14111
    with diss
    dick_secretary "Я ведь твоя лучшая подружка, Мелани? Правда?"
    img 14112
    with diss
    melanie "!!!"
    img 14113
    with fade
    melanie "Вы..."
    melanie "Вы моя лучшая подружка, Мисс Виктория..."
    music stop
    img black_screen
    with diss
    pause 2.0
    music2 audio_Melanie_Victoria_Titjob_1b
    stop music
    play music "Sounds/audio_Melanie_Titjob_1a.mp3"
    scene black
    image videov_Melanie_Victoria_Titjob_1_1 = Movie(play="video/v_Melanie_Victoria_Titjob_1_1.mkv", fps=30)
    show videov_Melanie_Victoria_Titjob_1_1
    with fadelong
    wclean
    stop music
    play music "Sounds/audio_Melanie_Titjob_1a.mp3"
    scene black
    image videov_Melanie_Victoria_Titjob_1_2 = Movie(play="video/v_Melanie_Victoria_Titjob_1_2.mkv", fps=30)
    show videov_Melanie_Victoria_Titjob_1_2
    dick_secretary "Да, Давай!"
    wclean
    if game.extra == True:
        stop music
        play music "Sounds/audio_Melanie_Titjob_1a.mp3"
        scene black
        image videov_Melanie_Victoria_Titjob_1_4 = Movie(play="video/v_Melanie_Victoria_Titjob_1_4.mkv", fps=30)
        show videov_Melanie_Victoria_Titjob_1_4
        dick_secretary "Хорошенько работай своими сиськами, Да!"
        wclean
        stop music
        play music "Sounds/audio_Melanie_Titjob_1a.mp3"
        scene black
        image videov_Melanie_Victoria_Titjob_1_5 = Movie(play="video/v_Melanie_Victoria_Titjob_1_5.mkv", fps=30)
        show videov_Melanie_Victoria_Titjob_1_5
        dick_secretary "Меня так возбуждает!"
        wclean
        stop music
        play music "Sounds/audio_Melanie_Titjob_1a.mp3"
        scene black
        image videov_Melanie_Victoria_Titjob_1_6 = Movie(play="video/v_Melanie_Victoria_Titjob_1_6.mkv", fps=30)
        show videov_Melanie_Victoria_Titjob_1_6
        wclean

    music2 stop
    music Loved_Up
    # video
    sound hlup25
    img 14114
    with diss
    w
    if monicaShowedBoobsToVictoriaCamera == True:
        sound hlup10
        img 14115
        with diss
    dick_secretary "Эти сиськи стоят миллоны долларов."
#    w
    sound hlup10
    img 14116
    with diss
    dick_secretary "Тебе пишут сотни тысяч поклонников, Да?"
#    w
    sound hlup25
    img 14117
    with diss
    melanie "Да, Мисс Виктория..."
#    w





    # end video
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 14118
    with fadelong
    dick_secretary "Но я думаю это лучшее применение твоим сиськам, нежели показ их Мистеру Дику!"
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14119
        with diss
    melanie "!!!"
    img 14120
    with fade
    dick_secretary "Скажи, ты рада сделать массаж своей лучшей подружке?"
    img 14121
    with diss
    melanie "!!!"
    img 14122
    with fade
    melanie "Да, я рада сделать Вам массаж, Мисс Виктория..."
    if monicaShowedBoobsToVictoriaCamera == True:
        img 14123
        with diss
    dick_secretary "Хорошо..."
    dick_secretary "Возьми мой большой пальчик себе в рот..."
    music Power_Bots_Loop
    img 14124
    with hpunch
    menu:
        "Сделать что приказала Виктория.":
            pass
        "Уйти.":
            music stop
            img black_screen
            with diss
            pause 1.5
            music Power_Bots_Loop
            if monicaShowedBoobsToVictoriaCamera == True:
                img 14127
            else:
                img 14128
            with fadelong
            melanie "Я не готова сделать это!"
            dick_secretary "Хорошая подружка должна быть готова всегда."
            return 1
    # Мелани в шоке, злится
    img 14125
    with fade
    melanie "!!!"

    # ехидно
    img 14126
    with diss
    dick_secretary "Мне надо повторить?"

    # Мелани берет ногу Виктории в рот
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    sound hlup19
    img 14129
    with fadelong
    w
    img 14130
    with diss
    w
    # Виктория рукой держит между ног (мастурбирует)
    img 14131
    with fade
    dick_secretary "Ах! Как чудесно!"
    sound hlup21
    img 14132
    with diss
    w
    img 14133
    with diss
    dick_secretary "Ах! Ах!"

    # Мелани продолжает держать ногу во рту
    if monicaShowedBoobsToVictoriaCamera == True:
        sound hlup19
        img 14134
        with fade
    melanie "!!!"
    img 14135
    with diss
    dick_secretary "А теперь... теперь..."
    # Виктория кончает
    img 14136
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    dick_secretary "Теперь... АААаааааааххххх!!!"
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14137
    with fadelong
    dick_secretary "Ладно, подружка..." #+
    dick_secretary "На сегодня хватит..."
    dick_secretary "Мы продолжим нашу дружбу позже..."

    # Мелани встает, Виктория убирает ногу
    sound snd_woman_laugh3
    img 14128
    with fade
    dick_secretary "Ты можешь идти, подружка, но помни про наш уговор..." #-

    # Мелани уходит, закрывая рукой рот в отвращении и злобе, другой рукой закрывает шубу.

    return




















#
