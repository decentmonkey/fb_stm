default dialogue_5_dance_strip_20_flag1 = False
default monicaClaireOilingCount = 0
default monicaClaireOilingToplessCount = 0
# Паб. Разговор с Эшли (Моника украла чаевые).
label dialogue_5_dance_strip_1:
    # Эшли орет на Монику, что та украла чаевые (ep27_dialogues7_pub8)
    # после их диалога появляется меню выбора, где строка "отработать на сцене" кликабельна
    # выбор Моники: отработать на сцене
    # Моника шокирована, что ей нужно будет танцевать, как стриптизерше, да еще и на сцене
    music2 pub_noise1_low
    music Groove2_85
    img 22650
    with fadelong
    mt "На сцене?!" # растерянно
    mt "!!!"
    m "Я должна буду выйти на сцену?!"
    m "Но..."
    music Power_Bots_Loop
    img 22651
    with diss
    ashley "Никаких 'но'!" # раздраженно
    ashley "Или ты идешь на сцену или убираешься отсюда!"
    if day_time != "evening":
        ashley "Так что {c}приходи вечером!{/c}"
        ashley "Днем танцев нет! Я не хочу терпеть эту громкую музыку еще и днем!"
        ashley "Мне и так хватает постоянного нытья Джо у меня под ухом!"
        return False

    music Groove2_85
    img 22652
    with fade
    m "Как я буду танцевать? Я... Я не смогу..."
    img 22653
    with diss
    mt "Я, Моника Бакфетт! Буду танцевать стриптиз! На сцене в грязном пабе в трущобах!"
    mt "Это немыслимо!!!"
    python:
        flag1 = False
        for progress_name in corruption_places:
            if progress_name.find('monicaWhoringClothPylonDanceCorruption') != -1:
                flag1 = True
    if flag1 == True:
        mt "Одно дело танцевать у пилона для одного-двух неудачников в подворотне..."
        mt "Они все равно никогда не узнают, кто я такая..."
        mt "А сцена..."
        mt "Это все равно, что фотосессия для обложки журнала, который увидят миллионы!"

    music Power_Bots_Loop
    img 22654
    with diss
    mt "Боже! А вдруг меня кто-нибудь узнает!!!"
    mt "!!!"
    music Hidden_Agenda
    img 22655
    with fade
    m "Я ни разу не танцевала... Я не знаю, как... Я стесняюсь!" # неуверенно
    music Groove2_85
    img 22656
    with diss
    ashley "А чего здесь стесняться?"
    ashley "Вышла, задом покрутила у пилона и дело сделано!"
    img 22657
    with diss
    ashley "Тем более, с таким задом, как у тебя..." # многозначительно улыбается
    ashley "Ты быстро сможешь отработать долг и даже заработать неплохие деньги."
    ashley "Так что попробуй. Тут нет ничего страшного."
    music Loved_Up
    ashley "А я с удовольствием посмотрю на твою попку на сцене!"
    music Power_Bots_Loop
    img 22658
    with fade
    mt "Черт! Если я сейчас откажусь, она меня выгонит с работы..."
    mt "Как подумаю, что мне нужно выйти на сцену..."
    music Groove2_85
    img 22659
    with diss
    ashley "Ну? Чего ты ждешь? Иди в гримерку."
    ashley "Тебе сначала нужно подготовиться к выступлению, переодеться..."
    music Loved_Up
    ashley "Вернее, раздеться!" # улыбается
    music Groove2_85
    img 22660
    with fade
    mt "..."
    # Моника в растерянности. Выбор: идти в гримерку или уйти
    menu:
        "Идти в гримерку.":
            pass
        "Уйти.":
            mt "Нет! Я не смогу!!!"
            mt "Я не опущусь до уровня этих девушек у пилона!"
            img 22661
            with diss
            m "Я... Мне нужно время подумать..."
            m "Сегодня я точно не готова это сделать..."
            return False
    # Моника выбирает идти в гримерку
    mt "С другой стороны..."
    mt "Если и правда получится быстро отработать долг перед Эшли..."
    img 22662
    with diss
    mt "..."
    mt "Схожу сначала в гримерку. Возможно, там есть приличные сценические костюмы..."
    mt "Хотя сомневаюсь что в этой дыре есть что-то подходящее для такой леди как Я..."
#    $ log1 = t_("Идти в гримерку, чтобы подготовиться к выступлению на сцене.")
#    $ log1 = t_("Мне нужно отработать долг $500, выступая на сцене в пабе.")
    return True

# Паб. Гримерка танцовщиц. Разговор Моники с рыжей стриптизершой.
# После того, как Моника не отдала чаевые и была наказана. Появляется меню отработать чаевые на сцене.
# После этого, танцует каждый день только рыжая до этого диалога.
label dialogue_5_dance_strip_2:
    # Моника стоит в дверях гримерки, рыжая сидит возле зеркала боком к ней, полуголая
    # cмотрит с пренебрежением
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22663
    with fadelong
    mt "Фи, это же просто подсобка, а не гримерка!"
    mt "И все такое... старое!"
    mt "Как здесь можно готовиться к выступлениям?!"
    call refresh_scene_fade() from _call_refresh_scene_fade_234
    # переключение на движок
    return
label dialogue_5_dance_strip_2a:
    # нажатие на Молли
    # к Монике поворачивается рыжая, смотрит на нее неприветливо
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22664
    with fadelong
    stripper "Это ты новая танцовщица что-ли?.." #осматривает Монику с ног до головы
    img 22665
    with fade
    stripper "М, понятно..."
    img 22666
    with diss
    mt "???"
    img 22667
    with diss
    w
    # и отворачивается
    music Groove2_85
    img 22668
    with fade
    stripper "Увижу тебя рядом со своими вещами - скажу Джо, что ты у меня украла что-нибудь." # не глядя на Монику
    stripper "Советую держаться подальше."
    # Моника неприятно удивлена таким теплым приемом
    music Power_Bots_Loop
    img 22669
    with diss
    sound highheels_short_walk
    mt "..."
    mt "И я рада познакомиться..."
    mt "Как грубо!"
    mt "Всего лишь какая-то стриптизерша из трущоб!"
    mt "Ей, видимо, неизвестно, что такое воспитание и манеры..."
    # Моника зло смотрит на нее и проходит в гримерку
    music Groove2_85
    img 22670
    with fade
    mt "Мне надо надеть сценический костюм. Которого у меня нет..."
    mt "Что же делать?"
    music Hidden_Agenda
    img 22671
    with diss
    mt "Попросить у этой хамки что-нибудь из одежды?"
    # Моника смотрит на рыжую
    sound highheels_short_walk
    img 22672
    with fade
    mt "..."
    # рыжая поворачивается к Монике
    music Groove2_85
    img 22673
    with diss
    stripper "Чего уставилась?!" #разговаривает высокомерно
    stripper "Тебе на сцену через пять минут, чего ты ждешь?"
    stripper "Или ты пойдешь в этом наряде для бомжей?"
    # Моника смотрит на нее с неприязнью
    img 22674
    with fade
    m "Мне не выдали сценический костюм. Я не знаю, в чем выходить на сцену."
    sound snd_woman_laugh
    img 22675
    with diss
    stripper "Сценический костюм?!"
    stripper "Аха-ха!!!"
    img 22676
    with diss
    sound snd_woman_laugh3
    stripper "Может, тебе еще личного ассистента и гримера предоставить?!"
    stripper "Аха-ха-ха!"
    music Power_Bots_Loop
    img 22677
    with fade
    mt "..." #Моника убивает ее взглядом
    # рыжая снова отворачивается к зеркалу
    music Groove2_85
    img 22678
    with diss
    stripper "Ты же не думаешь, что я тебе дам свою одежду?!"
    stripper "Иди танцуй голая!"
    music Power_Bots_Loop
    img 22679
    with diss
    mt "Вот стерва!!!"
    mt "!!!" # отворачивается от рыжей
    music Groove2_85
    img 22680
    with fade
    mt "Что же мне теперь делать?" # растерянно
    mt "Выйти на сцену в этой одежде?"
    mt "Но я не могу идти на сцену в таком виде!"
    mt "Кто-нибудь из этих неудачников узнает меня!"
    # с негодованием
    img 22681
    with diss
    mt "И не хватало еще, чтобы мое лицо узнал кто-то за пределами этих трущоб..."
    mt "..."
    music Groove2_85
    img 22682
    with fade
    sound highheels_short_walk
    mt "Где эта Эшли?!"
    mt "В чем, по ее мнению, я должна танцевать?!"
#    $ log1 = t_("Спросить у Эшли костюм для выступления.")
#    $ log1 = t_("Эта рыжая стриптизерша слишком многое себе позволяет. Как она смеет так общаться со мной?!")
    return
label dialogue_5_dance_strip_2b:
    mt "Я не хочу разговаривать с этой хамкой. Она провоцирует меня."
    mt "Я... боюсь не сдержаться и ударить ее..."
    return
# гримерка - один выход. Перед танцами выход ведет ко сцене. После танцев выход ведет к диалогу с Эшли или Джо (если ловит ее)
# Далее Моника оказывается в локации паба (как обычно)
# Локация сцены (крупным планом сцена и Моника стоит перед ней). Для танцев надо нажать на цену (look или walk)
# walk - начало танца
# выйти назад в гримерку

# Мысли Моники, когда смотрит на сцену.
label dialogue_5_dance_strip_4n:
    # не рендерить!
    mt "Грязная заляпанная сцена! Фи!"
    mt "Я не верю, что мне приходится танцевать на ней!"
    mt "Мне! Монике Бакфетт!!!"
    return

label dialogue_5_dance_strip_4na:
    if act=="l":
        return
    mt "Мне нужно идти в гримерную комнату..."
    return False

label dialogue_5_dance_strip_4nb:
    mt "Сначала мне надо поговорить с Эшли..."
    return False

label dialogue_5_dance_strip_4nc:
    if act=="l":
        return
    mt "Мне надо придти завтра."
    return False

# Моника после первого посещения гримерки идет к барной стойке к Эшли. Ей нужен костюм для выступления.
# Паб. Возле барной стойки. Эшли там нет, только Джо. Разговор Моники с Джо.
label dialogue_5_dance_strip_3:
    # Моника с негодованием
    music2 pub_noise1_low
    music Groove2_85
    img 22683
    with fadelong
    m "Где Эшли?"
    music Hidden_Agenda
    img 22684
    with fade
    joe "[monica_pub_name], можешь спросить у меня. Что ты хотела?"
    joe "Я тебе помогу решить любой вопрос!"
    music Groove2_85
    img 22685
    with diss
    m "Мне не в чем выступать на сцене!"
    m "В этой одежде я выходить туда не собираюсь!"
    img 22686
    with fade
    m "..."
    # Джо улыбается
    music Hidden_Agenda
    joe "Не вижу здесь никакой проблемы."
    joe "Иди голая! У тебя тогда будет больше чаевых."
    # Моника зло
    music Power_Bots_Loop
    img 22687
    with diss
    m "Конечно, нет! Я ни за что не буду танцевать голая!"
    m "!!!"
    m "Мне нужна какая-нибудь одежда для сцены!"
    # Джо удивленно
    music Groove2_85
    img 22688
    with fade
    joe "Ну, а я чем могу помочь?"
    joe "Попроси одежду у другой стриптизерши."
    img 22689
    with diss
    m "Она сказала, что не даст мне ничего..."
    img 22690
    with diss
    m "..." # ждет от него ответа
    img 22691
    with fade
    joe "Ну хорошо. Сегодня на сцену можешь не выходить."
    joe "Эшли я скажу, что ты будешь отрабатывать долг, начиная с завтрашнего дня."
    joe "{c}Приходи завтра{/c}"
    joe "Будет работать Клэр. Она тебе даст что-нибудь из одежды."
    # Джо отворачивается, продолжает свою работу. Моника сердито
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 22692
    with fadelong
    mt "{c}Завтра{/c} мне предстоит снова вернуться в эту ужасную гримерку, фи!"
    mt "Да еще и придется знакомиться с еще одной хамкой!"
    mt "!!!"
#    $ log1 = t_("Поговорить в пабе с другой стриптизершей.")
    return

# Мысли Моники на сцене. В зависимости от уровня corruption.
label dialogue_5_dance_strip_4a:
    mt "Мне хочется спрятаться подальше от всех этих похотливых взглядов!"
    return
label dialogue_5_dance_strip_4b:
    mt "Я должна держаться! Я сильная!"
    return
label dialogue_5_dance_strip_4c:
    mt "Мне просто нужно сделать несколько движений у пилона."
    mt "Они же просто будут смотреть."
    return
label dialogue_5_dance_strip_4d:
    mt "Нужно относиться к этому как Клэр. Я просто позволяю этим мужчинам смотреть на свою красоту..."
    mt "...недоступную для них красоту!"
    return
label dialogue_5_dance_strip_4e:
    mt "Сегодня хочется сделать так, чтобы у этой рыжей не осталось поклонников в этой дыре!"
    mt "Звезда здесь может быть только одна - Я. А она даже не конкурентка мне... У меня вообще не может быть конкуренток!!!"
    return

label dialogue_5_dance_strip_4f:
    # После того как поругалась с Молли (после d, e)
    mt "И не забывать про Молли... Надо поставить ее на место... В подворотню со шлюхами!"
    return


label dialogue_5_dance_strip_4g:
    # Отказывается переходить на стадию 1
    img 22904
    with fadelong
    mt "Я не буду снимать с себя жилет!"
    mt "Не хватало еще, чтобы эта толпа неудачников пялилась на мою прекрасную грудь!!!"
    help "У Моники мало опыта работы танцовщицей."
    if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToTopless:
        help "Окрыты не все движения. Требуется [monicaPosesOpenedToTopless]."
    if pubDanceCount < monicaDanceAmountToTopless:
        help "Требуется выйти на сцену [monicaDanceAmountToTopless] раз."
    return

label dialogue_5_dance_strip_4h:
    # Переход на стадию 1 успешен

    mt "Если я сниму жилет, то заработаю больше денег..."
    mt "Они же просто будут смотреть... на голую грудь [monica_pub_name]."
    return

label dialogue_5_dance_strip_4i:
    # Отказывается вставать в позу
    mt "Я не буду так крутиться на пилоне! Это пошло!"
    return

label dialogue_5_dance_strip_4j:
    # Отказывается вставать в позу
    mt "Я не буду вставать в такую откровенную позу!"
    return
label dialogue_5_dance_strip_4k:
    # Отказывается вставать в позу
    mt "Я не готова так позировать! Это уже слишком!"
    help "У Моники мало опыта работы танцовщицей."
    if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
        help "Окрыты не все движения. Требуется [monicaPosesOpenedToStage2]."
    if pubDanceCount < monicaDanceAmountToTopless:
        help "Требуется выйти на сцену [monicaDanceAmountToTopless] раз."
    return

label dialogue_5_dance_strip_4l:
    # На будущее
    mt "Я ни за что не буду танцевать голой! Ни за какие деньги!"
    return

label dialogue_5_dance_strip_4m:
    # Заканчивается танец
    mt "Все! С меня хватит!!!"
    mt "Я на сегодня наработалась [monica_pub_name]!"
    mt "Не хочу больше видеть эту толпу пьяных неудачников!"
    return False

# Крики посетителей из зала во время выступления Моники.
# Моника в корсете
# реплики для верха (лицо)
label dialogue_5_dance_strip_5a:
    if len(pub_dance_dialogues_up_list) == 0:
        $ pub_dance_dialogues_up_list = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list.pop()

    # правильные стрелки
    if idx == 1:
        customers1 "Эй, смотри, какая телка!"
    if idx == 2:
        customers2 "Кто это такая? Я ее раньше не видел!"
    if idx == 3:
        customers3 "Это новая стриптизерша? Вау!"
    if idx == 4:
        customers4 "Эй, красотка, иди к нам!"
    if idx == 5:
        customers5 "Снимай маску! Покажи нам себя!"
    return
label dialogue_5_dance_strip_5a1:
    if len(pub_dance_dialogues_up_list2) == 0:
        $ pub_dance_dialogues_up_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_up_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Эй! Хорош уже! Давай, раздевайся!"
    if idx == 2:
        customers2 "Где стриптиз?!"
    if idx == 3:
        customers3 "Это что?! Где сиськи голые?!"
    return
# реплики для side (тело)
label dialogue_5_dance_strip_5b:
    if len(pub_dance_dialogues_side_list) == 0:
        $ pub_dance_dialogues_side_list = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_side_list.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Давай, покажи класс, детка!"
    if idx == 2:
        customers2 "О, да! Вот это сиськи!"
    if idx == 3:
        customers3 "Охренеть!"
    if idx == 4:
        customers4 "Давай, раздевайся!"
    if idx == 5:
        customers5 "Эй, покажи нам сиськи!"
    return
label dialogue_5_dance_strip_5b2:
    if len(pub_dance_dialogues_side_list2) == 0:
        $ pub_dance_dialogues_side_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_side_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Уууууу!!!"
    if idx == 2:
        customers2 "Я пришел на голые сиськи посмотреть, а не на это!"
    if idx == 3:
        customers3 "Где нормальный стриптиз?!"
    return
# реплики для down (ноги, попа)
label dialogue_5_dance_strip_5c:
    if len(pub_dance_dialogues_down_list) == 0:
        $ pub_dance_dialogues_down_list = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_down_list.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Снимай с себя эти тряпки!"
    if idx == 2:
        customers2 "Пошли в приват, детка!"
    if idx == 3:
        customers3 "Да! Давай еще!"
    if idx == 4:
        customers4 "Вау, детка! У меня уже в штанах дымится! Иди сюда!"
    if idx == 5:
        customers5 "Давай, покрути своей задницей!"
    return
label dialogue_5_dance_strip_5c2:
    if len(pub_dance_dialogues_down_list2) == 0:
        $ pub_dance_dialogues_down_list2 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_down_list2.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Твою мать, сними с себя хоть что-нибудь!"
    if idx == 2:
        customers2 "И это все?!"
    if idx == 3:
        customers3 "Уууууу!!!"
    return

label dialogue_5_dance_strip_5ca:
    customers2 "И это все?!"
    customers2 "Детка, иди танцуй еще!"
    return

# Моника топлесс
# реплики для верха (лицо)
label dialogue_5_dance_strip_5d:
    if len(pub_dance_dialogues_up_list3) == 0:
        $ pub_dance_dialogues_up_list3 = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list3.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "О да! Детка, ты супер!"
    if idx == 2:
        customers2 "Да! Мы тебя ждали, красотка!"
    if idx == 3:
        customers3 "Спускайся сюда!"
    if idx == 4:
        customers4 "Покажи свои сиськи!"
    if idx == 5:
        customers5 "Давай, покажи класс, детка!"
    return
label dialogue_5_dance_strip_5d2:
    if len(pub_dance_dialogues_side_list4) == 0:
        $ pub_dance_dialogues_side_list4 = random.sample(set([1,2,3,4]), 4)
    $ idx = pub_dance_dialogues_side_list4.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Сиськи показывай!"
    if idx == 2:
        customers2 "Уууууу!!!"
    if idx == 3:
        customers3 "Эй, научите ее, как надо это делать!!!"
    if idx == 4:
        customers4 "Эй, мы это уже видели в прошлый раз! Покажи что-нибудь еще!"
    return
# реплики для side (тело)
label dialogue_5_dance_strip_5e:
    if len(pub_dance_dialogues_up_list3) == 0:
        $ pub_dance_dialogues_up_list3 = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list3.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Вау! Какие сиськи!"
    if idx == 2:
        customers2 "Детка, спускайся сюда! У меня для тебя есть кое-что!"
    if idx == 3:
        customers3 "Давай в приват!"
    if idx == 4:
        customers4 "Потряси своими сиськами!"
    if idx == 5:
        customers5 "Да! Охренительно!"
    return
label dialogue_5_dance_strip_5e2:
    if len(pub_dance_dialogues_side_list4) == 0:
        $ pub_dance_dialogues_side_list4 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_side_list4.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "Да разденься ты уже!!!"
    if idx == 2:
        customers2 "Я за что деньги платить должен?!"
    if idx == 3:
        customers3 "Покрути своей задницей!"
    return
# реплики для down (ноги, попа)
label dialogue_5_dance_strip_5f:
    if len(pub_dance_dialogues_up_list3) == 0:
        $ pub_dance_dialogues_up_list3 = random.sample(set([1,2,3,4,5]), 5)
    $ idx = pub_dance_dialogues_up_list3.pop()
    # правильные стрелки
    if idx == 1:
        customers1 "Эй, хочешь этих хрустящих купюр? Снимай свои трусики!"
    if idx == 2:
        customers2 "Покажи нам свою киску!"
    if idx == 3:
        customers3 "Давай, снимай с себя все!"
    if idx == 4:
        customers4 "Иди сюда! Смотри, что у меня есть для тебя!"
    if idx == 5:
        customers5 "О, какая задница! Папочка любит такие! Пошли ко мне, детка!"
    return
label dialogue_5_dance_strip_5f2:
    if len(pub_dance_dialogues_side_list4) == 0:
        $ pub_dance_dialogues_side_list4 = random.sample(set([1,2,3]), 3)
    $ idx = pub_dance_dialogues_side_list4.pop()
    # неправильные стрелки
    if idx == 1:
        customers1 "И это все?!"
    if idx == 2:
        customers2 "Уууууу!!!"
    if idx == 3:
        customers3 "Где нормальный стриптиз?!"
    return

# Паб. Моника возвращается в паб на другой день, после знакомства с рыжей.
# Она еще не танцевала на сцене. Нужен костюм. При клике на Джо или Эшли начинается диалог с Эшли.
label dialogue_5_dance_strip_6:
    # Эшли вопросительно
    music2 pub_noise1_low
    music Groove2_85
    img 22693
    with fadelong
    ashley "А, ты пришла?"
    ashley "Я уже думала, ты не вернешься..."
    if day_time != "evening":
        ashley "{c}Приходи вечером!{/c}"
        ashley "Днем танцев нет! Я не хочу терпеть эту громкую музыку еще и днем!"
        ashley "Мне и так хватает постоянного нытья Джо у меня под ухом!"
        return -1


    ashley "В прошлый раз я так и не увидела эту попку на сцене голой..." # с улыбочкой
    music Power_Bots_Loop
    img 22694
    with fade
    mt "Ты ее и не увидишь голой!"
    mt "Тем более, на этой сцене!!!" # сердито
    music Groove2_85
    img 22695
    with diss
    m "Мне не в чем было выходить на сцену..."
    m "..."
    ashley "Так в чем проблема?" # удивленно
    ashley "У девочек в гримерке полно одежды для выступления."
    ashley "Иди в гримерку и попроси что-нибудь из их шмоток."
    music Loved_Up
    img 22696
    with fade
    ashley "А лучше выходи на сцену вообще без одежды... Будет больше чаевых!" # многозначительно улыбается
    music Power_Bots_Loop
    img 22697
    with diss
    mt "!!!"
    m "Я не буду танцевать без одежды!" # сердито
    music Groove2_85
    img 22698
    with fade
    ashley "Тогда иди в гримерку и договаривайся с Клэр."
    ashley "Или отдавай $ 500 и можешь не танцевать."
    img 22699
    with diss
    mt "..."
    # Моника в растерянности. Выбор: отдать деньги, идти в гримерку или уйти
    $ menu_price = [500]
    menu:
        "Отдать деньги":
            music Hidden_Agenda
            img 21009
            with fade
            m "Эшли..."
            $ add_money(-500)
            $ ep27_dialogues7ReturnedMoneyCount += 1
            m "Вот $ 500..."
            music Groove2_85
            img 21010
            with diss
            ashley "Я так и знала, ха-ха!"
            ashley "Ладно, так уж и быть. Теперь ты можешь снова работать здесь."
            ashley "Но не испытывай моего терпения!"
            return 1
        "Идти в гримерку.":
            pass
        "Уйти.":
            music Groove2_85
            mt "Нет! Я не смогу!!!"
            mt "Я не опущусь до уровня этих девушек у пилона!"
            img 22700
            with fade
            m "Я... Мне нужно время подумать..."
            m "Сегодня я точно не готова это сделать..."
            return 0
    # Моника выбирает пойти в гримерку
    img 22701
    with fade
    mt "Возможно, у этой Клэр найдется приличный костюм..."
#    $ log1 = t_("Идти в гримерку, чтобы подготовиться к выступлению на сцене.")
    return 2


# Паб. Моника возвращается в паб на другой день, после того, как отказалась выйти на сцену.
# Она еще не была в гримерке. При клике на Джо или Эшли начинается диалог с Эшли.
label dialogue_5_dance_strip_7:
    # Эшли вопросительно
    music2 pub_noise1_low
    music Groove2_85
    img 22702
    with fadelong
    ashley "А, ты пришла?"
    ashley "Ты, наконец-то, решила отработать деньги?"
    ashley "Или ты готова вернуть долг?"
    img 22703
    with fade
    m "Мне нужна работа..." # растерянно
    if day_time != "evening":
        img 20993
        with diss
        ashley "{c}Приходи вечером!{/c}"
        ashley "Днем танцев нет! Я не хочу терпеть эту громкую музыку еще и днем!"
        ashley "Мне и так хватает постоянного нытья Джо у меня под ухом!"
    else:
        img 22704
        with diss
        ashley "Тогда чего ты ждешь? Иди в гримерку!"
        ashley "Тебе сначала нужно подготовиться к выступлению, переодеться..."
        music Loved_Up
        img 22705
        with fade
        ashley "Вернее, раздеться!" # улыбается
        music Groove2_85
        img 22706
        with diss
        mt "!!!"
        # Моника в растерянности. Выбор: отдать деньги, идти в гримерку или уйти
    if ep29_quests_pub_block_money_return == False:
        $ menu_price = [500]
    menu:
        "Отдать деньги" if ep29_quests_pub_block_money_return == False:
            music Hidden_Agenda
            img 21009
            with fade
            m "Эшли..."
            $ add_money(-500)
            $ ep27_dialogues7ReturnedMoneyCount += 1
            m "Вот $ 500..."
            music Groove2_85
            img 21010
            with diss
            ashley "Я так и знала, ха-ха!"
            ashley "Ладно, так уж и быть. Теперь ты можешь снова работать здесь."
            ashley "Но не испытывай моего терпения!"
            return 1
        "Идти в гримерку." if day_time == "evening":
            pass
        "Уйти.":
            if day_time == "evening":
                music Groove2_85
                mt "Я, Моника Бакфетт, на этой грязной сцене?!"
                mt "Нет! Я не смогу!!!"
                mt "Я не опущусь до уровня этих шлюх у пилона!"
                img 22707
                with fade
                m "Я... Мне нужно время подумать..."
                m "Сегодня я точно не готова это сделать..."
            return 0
    # Моника выбирает идти в гримерку
    img 22708
    with fade
    mt "Если это единственный способ быстро отработать долг перед Эшли..."
    mt "..."
    mt "Схожу сначала в гримерку. Возможно, там есть приличные сценические костюмы..."
#    $ log1 = t_("Идти в гримерку, чтобы подготовиться к выступлению на сцене.")
#    $ log1 = t_("Мне нужно отработать долг $ 500, выступая на сцене в пабе.")
    return

label dialogue_5_dance_strip_8a:
    mt "Это и есть вторая стриптизерша?"
    return

# Паб. Гримерка. Разговор Моники со второй стриптизершей.
# Следующий приход после начала цепочки квестов
label dialogue_5_dance_strip_8:
    music stop
    img black_screen
    with diss
    pause 1.5
    # брюнетка стоит спиной к Монике, переодевается, Моника стоит в дверях
    music Groove2_85
    img 22709
    with fadelong
    mt "Это и есть вторая стриптизерша?"
    img 22710
    with fade
    mt "Надо приготовиться к знакомству со второй хамкой." # с воинственным настроем
    mt "Она, наверное, тоже возомнила себя звездой, как та рыжая стерва..."
    music Pyro_Flow
    img 22711
    with diss
    mt "Звездой в грязном пабе в трущобах!.." # высокомерно
    # Брюнетка поворачивается к Монике, она после выступления в черной маске
    music Groove2_85
    img 22712
    with fade
    stripper "Привет." # без улыбки, спокойно
    stripper "Молли мне говорила, что у нас новенькая. Это ты?"
    # Моника готовилась не к такому знакомству, растерянно
    img 22713
    with diss
    m "..."
    m "Д-да... Привет..."
    img 22714
    with fade
    stripper "Я Клэр. А ты?"
    img 22715
    with diss
    m "Я [monica_pub_name]. А Молли это та рыжая стриптизерша?"
    img 22716
    with fade
    clare "Да." # с ехидной улыбкой
    img 22717
    with diss
    clare "Она тут звезда и очень гордится этим."
    img 22718
    with fade
    clare "С ней лучше дружить и не вставать у нее на пути."
    img 22719
    with diss
    mt "Звезда! Ха-ха! Стриптизерша со звездной болезнью!"
    mt "Похоже, эта Клэр единственная в этой дыре, кто может нормально общаться."
    img 22720
    with fade
    clare "Ты давно в стриптизе, [monica_pub_name]?"
    music Hidden_Agenda
    img 22721
    with diss
    m "Нет. Сегодня будет мое первое выступление..."

    # если были сцены в трущобах с ситизенами
    python:
        flag1 = False
        for progress_name in corruption_places:
            if progress_name.find('monicaWhoringClothPylonDanceCorruption') != -1:
                flag1 = True
    if flag1 == True:
        img 22722
        with diss
        mt "Танцы у пилона на улицах трущоб - не в счет!" # если были сцены в трущобах с ситизенами
    #
    music Groove2_85
    img 22723
    with fade
    clare "Не волнуйся." # дружелюбно
    clare "Я выступаю уже несколько лет и мне очень нравится."
    img 22724
    with diss
    m "Нравится?!" # удивленно
    m "Я думала такое делают только из-за денег..."
    img 22725
    with fade
    clare "Для меня это искусство. Мне нравится делиться своей красотой и видеть восторженные взгляды мужчин."
    img 22726
    with diss
    clare "Это занятие не является источником денег для меня."
    img 22727
    with fade
    mt "Хм... Искусство?.."
    mt "Возможно, если так к этому относиться, то намного проще выходить на сцену."
    mt "Но я не представляю себе такого отношения к этому."
    music Groove2_85
    img 22728
    with diss
    mt "Сами по себе танцы полуголой на публике отвратительны."
    mt "И я не изменю своего отношения к этому никогда!"
    mt "!!!"
    music Groove2_85
    img 22729
    with fade
    clare "[monica_pub_name], почему ты не переодеваешься?"
    clare "В чем ты будешь выступать?"
    clare "Тебе уже пора выходить на сцену."
    # Моника проходит в гримерку и подходит к Клэр. Та стоит возле вешалки.
    img 22730
    with diss
    m "У меня нет одежды для сцены..."
    m "Эшли сказала, что я могу спросить одежду у тебя."
    img 22731
    with fade
    clare "Без проблем. Ты можешь взять вот это." # отворачивается к вешалке, потом кладет одежду для Моники на стул рядом
    # Моника в это время смотрит на ее фигуру
    music Hidden_Agenda
    img 22732
    with diss
    mt "А из этой Клэр получилась бы неплохая модель..."
    mt "Конечно, до Мелани, а тем более до меня, ей далеко, но все же."
    img 22733
    with diss
    mt "И что она забыла в этой дыре, тем более, что она тут не из-за денег..."
    # Клэр поворачивается к Монике
    music Groove2_85
    img 22734
    with fade
    clare "К вещам Молли лучше не приближайся."
    img 22735
    with diss
    clare "Наша звезда очень ревностно к этому относится." # с ехидной улыбкой
    sound snd_fabric1
    img 22736
    with fade
    clare "У меня полно подобных шмоток."
    img 22737
    with diss
    clare "Можешь этот костюм оставить себе."
    img 22738
    with fade
    m "Серьезно?!" # удивленно
    music Groove2_85
    img 22739
    with diss
    m "..." # смотрит на вещи на стуле
    mt "Мне придется надевать на себя ЭТО?"
    mt "Фи! Какой вульгарный костюм!"
    mt "Да еще и после стриптизерши!"
    img 22740
    with diss
    mt "Какой ужас!"
    mt "Я, Моника Бакфетт, буду танцевать полуголая! В дешевом пабе для толпы неудачников!!!"
    mt "Я не могу поверить в это!"
label dialogue_5_dance_strip_8_loop1:
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            m "Я не выйду на сцену с голой грудью!!!"
            jump dialogue_5_dance_strip_8_loop1
    # Клэр отвернулась к вешалке, Моника снимает с себя свою одежду
    music Groove2_85
    img 22741
    with fadelong
    mt "Одно дело трущобы..." # если были сцены в трущобах с ситизенами
    mt "Там, конечно, приходилось показывать себя всяким неудачникам."
    music Power_Bots_Loop
    img 22742
    with diss
    mt "Но тут сцена!"
    mt "И этих неудачников целая толпа!!!"
    mt "Для меня быть на сцене - это все-равно что позировать на фотосессии перед всем миром."
    mt "Это не идет ни в какое сравнение с тихой подворотней, где меня никто не знает."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Molten_Alloy
    img 22744
    with fadelong
    w
    img 22743
    with fade
    mt "!!!"
    # Моника надевает костюм
    img 22745
    with diss
    mt "..."
    mt "Я очень надеюсь, что в этой маске мое лицо никто не узнает..."
    mt "..."
    music Groove2_85
    img 22746
    with fade
    mt "Так, мне надо собраться и сделать это!"
    mt "Это не я, а [monica_pub_name]."
    mt "Для [monica_pub_name] в этом нет ничего страшного."
    # Клэр поворачивается и смотрит на переодетую Монику
    music Groove2_85
    img 22747
    with diss
    clare "Отлично. Только..."
    # внимательно смотрит на Монику
    clare "Кое-чего тебе не хватает."
    img 22748
    with diss
    clare "Сразу видно, что у тебя нет опыта выступления на сцене."
    mt "???"
    # Клэр берет со столика в руки флакон
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22749
    with fadelong
    clare "Тебе нужно намазать тело этим маслом."
    img 22750
    with diss
    sound Jump1
    w
    sound highheels_short_walk
    img 22751
    with fade
    clare "Тогда ты будешь выглядеть более эффектно на сцене."
    img 22752
    with diss
    clare "[monica_pub_name], давай я тебе помогу?"
    img 22753
    with diss
    w
    $ menu_corruption = [0, monicaClaireOilingVest]
    menu:
        "Взять у Клэр масло и намазаться самой.":
            pass
        "Позволить Клэр намазать меня маслом.":

            # Клэр намазывает ее маслом
            img 22754
            with fade
            sound hlup2
            w
            music stop
            music2 Loved_Up
            img 22755
            with diss
            sound skin_lotion11
            w
            img 22756
            with diss
            w
            img 22757
            with fade
            w
            img 22758
            with diss
            sound skin_lotion11
            clare "А у тебя отличная фигура, [monica_pub_name]."
            img 22759
            with fade
            sound skin_lotion11
            mt "Она что, ко мне пытается пристать, как Эшли?!"
            mt "Я не хочу связываться с еще одной лесбиянкой!"
            img 22760
            with diss
            sound skin_lotion11
            clare "Мужчины в зале с ума сойдут, когда тебя увидят."
            img 22761
            with diss
            mt "Я к этому привыкла."
            mt "Мужчины всегда сходили по мне с ума..."
            if monica_shiny_hole_queen_day > 0: # Если Моника королева
                img 24345
            else:
                img 22762
            with fade
            sound skin_lotion11
            w
            if monica_shiny_hole_queen_day > 0: # Если Моника королева
                img 24346
            else:
                img 22763
            with diss
            w
            img 22764
            with fade
            sound skin_lotion11
            clare "Ты сегодня будешь звездой, [monica_pub_name]."
            img 22765
            with diss
            sound skin_lotion11
            mt "Конечно, буду! Мне нет здесь равных!"
            mt "И не только здесь! Мне нет равных нигде!"
            img 22766
            with fade
            sound skin_lotion11
            w
            img 22767
            with diss
            sound skin_lotion11
            w
            img 22768
            with diss
            sound skin_lotion11
            clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."
            img 22769
            with fade
            sound skin_lotion11
            w
            img 22770
            with diss
            sound skin_lotion11
            clare "Ты просто создана для обложки какого-нибудь модного журнала."
            img 22771
            with fade
            mt "Хм... Хорошо, что она их не читает."
            mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
            ###################################
            if game.extra == True:
                img black_screen
                with diss
                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_1 = Movie(play="video/v_Monica_Claire_Oiling3_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_1
                with fadelong
                wclean

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_2 = Movie(play="video/v_Monica_Claire_Oiling3_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_2
                with fadelong
                wclean

            ###################################
            $ monicaClaireOilingCount += 1
            $ add_char_progress("Pub_StripteaseGirl2", 50, "oiling1")
            music2 stop
    # Клэр, осматривая Монику
    music stop
    img black_screen
    with diss
    pause 1.5
    music Molten_Alloy
    if monica_shiny_hole_queen_day > 0: # Если Моника королева
        img 24347
    else:
        img 22772
    with fadelong
    clare "Вот теперь ты выглядишь на миллион баксов!"
    img 22773
    with fade
    mt "Я всегда выгляжу на миллион баксов... И не только выгляжу... Я и стою..."
    img 22774
    with diss
    mt "Миллиарды..."
    mt "Но, думаю Клэр не умеет даже считать до стольки..."

    # выход на движок (персонажи в сцене)
    clare "Давай, тебя там уже ждут!"
    mt "Черт. Черт! Черт!!!"

    $ pubMakeupRoomSkipMusicOnce = True
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
#    $ log1 = t_("Похоже, Клэр единственная в этой дыре, с кем можно нормально общаться.") # квест лог
    return

# Паб. Перед сценой. Разговор Моники с Джо.
# Джо ловит Монику перед подъемом на сцену первый раз
label dialogue_5_dance_strip_9b:
    clare "Вот теперь ты выглядишь на миллион баксов!"
    clare "Давай, тебя там уже ждут!"
    return False

label dialogue_5_dance_strip_9a:
    # Моника смотри на Джо у сцены
    # не рендерить!
    mt "Что это Джо делает здесь?"
    mt "Зачем этот жирный слизняк вертится у сцены?"
    return

label dialogue_5_dance_strip_9:
    # Джо стоит перед выходом на сцену
    music2 pub_noise1_low
    music Hidden_Agenda
    img 22775
    with fadelong
    joe "[monica_pub_name], а ты горячая штучка!"  # смотрит похотливо
    music Power_Bots_Loop
    img 22776
    with fade
    m "..." # раздраженно
    music Hidden_Agenda
    img 22777
    with diss
    joe "Только, жилет этот тут лишний."
    joe "Если хочешь чаевых, то сними это с себя!"
    joe "Местные девочки танцуют без одежды."
    # если видел грудь Моники
    if pubMonicaWaitressTipsPunishmentJoeStage >= 2:
        $ notif(t_("Моника показывала Джо свою грудь."))
        img 22778
        with fade
        joe "А твоих малышек наши посетители очень оценят, я их уже оценил!"
    #
    # если видел попу Моники
    if pubMonicaWaitressTipsPunishmentJoeStage >= 3:
        $ notif(t_("Моника показывала Джо свою попу."))
        img 22779
        with diss
        joe "И твоя попа также бесподобна. Тебе не стоит прятать ее от наших ребят!"
    #
    music Groove2_85
    img 22780
    with fade
    m "???" # удивленно и зло
    # движок
    menu:
        "Выйти на сцену в жилете.":
            pass
        "Снять жилет.":
            m "Я не выйду на сцену с голой грудью!!!"
            return False
    return

# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_10:
    # не рендерить!
    # Моника возвращается в гримерку, там уже нет Клэр
    mt "Чувствую себя такой грязной после всех взглядов и криков этих пьяниц!"
    mt "Мне хочется поскорее отмыться!!!"
    mt "Надо немного потерпеть... Это когда-нибудь закончится."
    mt "И я смогу выбраться из этого кошмарного дна... Я все сделаю для этого!!!"
    $ questHelp("shinyhole_13", True)
    $ questHelp("shinyhole_14", skipIfExists=True)
    $ questHelp("shinyhole_15", skipIfExists=True)
    $ questHelp("shinyhole_16", skipIfExists=True)
    return


# Паб. Моника выходит из гримерки. Если пытается снова пойти на сцену, хотя уже танцевала
label dialogue_5_dance_strip_11:
    # не рендерить!
    mt "На сегодня уже достаточно танцев."
    mt "Вернусь сюда в другой день. Возможно, удастся заработать больше чаевых."
    return

# Паб. Моника выходит из гримерки. Если идет в сторону барной стойки, появляется Эшли.
# Разговор с Эшли после первого выступления Моники.
# На выходе из гримерки
label dialogue_5_dance_strip_12:
    # Эшли требовательно
    music2 stop
    music stop
    img black_screen
    with diss
    pause 1.5
    music2 pub_noise1_low
    music Groove2_85
    img 22781
    with fadelong
    ashley "Ну что, [monica_pub_name], сколько ты заработала сегодня?"
    img 22782
    with fade
    m "???"
    img 22783
    with diss
    m "Что значит 'заработала'?! Я танцевала здесь!!!"
    m "Разве этого не достаточно?!" # возмущенно
    img 22784
    with fade
    ashley "Здесь надо не просто танцевать, а зарабывать деньги!"
    ashley "Если бы ты показала публике свою грудь или голую попку..."
    ashley "То тебе определенно дали бы несколько долларов."
    music Power_Bots_Loop
    img 22785
    with hpunch
    m "Я не собираюсь этого делать!!!"
    img 22786
    with diss
    ashley "А придется! Как ты собираешься возвращать мне долг?"
    ashley "Ты думала, что будешь просто танцевать?"
    ashley "Ты мне будешь отдавать свои чаевые, а я буду постепенно списывать твой долг."
    img 22787
    with diss
    m "!!!" # Моника офигевает
    music Groove2_85
    img 22788
    with fade
    ashley "Надеюсь, в следующий раз ты заработаешь хоть что-то на чай..."
    ashley "Для этого достаточно будет снять жилетку на сцене."
    img 22789
    with diss
    m "..."
    return

# Паб. Моника выходит из гримерки. Если идет в сторону барной стойки, появляется Эшли.
# Регулярный разговор с Эшли после выступлений Моники.
# У сцены
label dialogue_5_dance_strip_13:
    # Эшли требовательно
    music stop
    img black_screen
    with diss
    pause 1.0
    music2 pub_noise1_low
    music Groove2_85
    img 22790
    with fadelong
    ashley "[monica_pub_name], сколько ты заработала сегодня?"
    if monica_strip_tips_today == 0:
        # ничего не заработала
        img 22791
        with fade
        # заработала
        m "Сегодня я ничего не заработала..."
    else:
        img 22792
        with fade
        $ add_money(-monica_strip_tips_today)
        $ monica_strip_forgiveness_money_left -= monica_strip_tips_today
        m "Сегодня я заработала [monica_strip_tips_today]."
    img 22793
    with diss
    ashley "Тебе осталось отдать мне еще [monica_strip_forgiveness_money_left]."
    ashley "Если бы ты повертела своей попкой без трусиков, то отработала бы деньги гораздо быстрее..."
    music Loved_Up
    img 22794
    with diss
    ashley "А я с удовольствием посмотрела бы на это." # с улыбочкой
    music Power_Bots_Loop
    img 22795
    with fade
    m "Я не собираюсь этого делать!!!" # возмущенно
    m "!!!"
    mt "Одни извращенцы вокруг!"
    music Groove2_85
    img 22796
    with diss
    ashley "На сегодня ты свободна, [monica_pub_name]."
    ashley "Приходи завтра."
    return


# Паб. Гримерка танцовщиц. Разговор Моники с рыжей Молли.
# Далее, после первого выступления, танцует только рыжая
label dialogue_5_dance_strip_14:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22813
    with fadelong
    mt "Черт, я совсем забыла, что сегодня здесь звезда трущоб!"
    return
label dialogue_5_dance_strip_14a:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22814
    with fadelong
    sound highheels_short_walk
    mt "Я не хочу разговаривать с этой хамкой!"
    # Моника проходит в гримерку и молча переодевается в одежду Клэр
    # рыжая смотрит на Монику высокомерно
    img 22815
    with diss
    molly "Тебя здороваться не учили?.."
    # рыжая отворачивается
    img 22816
    with diss
    molly "Понабирают на работу шлюх из подворотни..."
    # Моника поворачивается и зло смотрит на нее\
    music Power_Bots_Loop
    img 22817
    with diss
    mt "!!!"
    menu:
        "Клэр предупреждала, что лучше не конфликтовать с ней":
            # отворачивается от Молли, послав ей убийственный взгляд
            pass
        "Да, Клэр предупреждала, но я же не могу просто проигнорировать такую наглость":
            music Power_Bots_Loop
            img 22818
            with fade
            m "Ты это сейчас про себя, да?" # со злостью
            m "Я такого же мнения после нашего с тобой так сказать 'знакомства'!"
            img 22819
            with diss
            mt "Этой хамке самое место в подворотне со шлюхами! Как она здесь оказалась?"
            # рыжая поворачивается к Монике и смотрит вопросительно и высокомерно
            music Groove2_85
            img 22820
            with fade
            molly "Мне послышалось или ты что-то сейчас мне сказала?"
            # Моника ей также высокомерно в ответ
            music Groove2_85
            img 22821
            with diss
            menu:
                "Взять стул Клэр и ударить им рыжую сучку!":
                    music Groove2_85
                    img 22822
                    with fade
                    mt "Нет, я не могу пока этого позволить себе."
                    mt "Эта сучка Эшли выгонит меня отсюда и я не смогу зарабатывать деньги..."
                    mt "Которые мне так нужны..."
                    mt "..."
                    mt "Я сделаю это позже..."
                "Мне не о чем разговаривать с такой как ты!":
                    pass
            music Groove2_85
            img 22823
            with fade
            m "Мне не о чем разговаривать с такой как ты!"
            m "И, тем более, о чем-то спорить!"
            img 22824
            with diss
            sound highheels_short_walk
            m "Я не собираюсь опускаться до твоего уровня!!!"
            m "!!!"
            # рыжая офигевает от такого, ничего не отвечает и зло смотрит на Монику
            music Power_Bots_Loop
            img 22825
            with fade
            molly "!!!"
    # Моника отворачивается от нее
    music Groove2_85
    img 22825
    with diss
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
    $ add_char_progress("Pub_StripteaseGirl1", 25, "Pub_StripteaseGirl1_conflict1")
#    menu:
#        "Надеть костюм с жилетом.":
#            pass
#        "Надеть только трусики.":
#            mt "Я не выйду на сцену с голой грудью!!!"
#            return False
#    $ log1 = t_("Выйти на сцену паба и танцевать.")
    return

# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_15:
    if monicaDancedLastDay != day:
        return
    # не рендерить!
    # Моника возвращается в гримерку, там уже никого нет
    mt "В этот раз уже было попроще... Не хватало еще привыкнуть к этому!"
    mt "Надо немного потерпеть... Это когда-нибудь закончится."
    mt "И я смогу выбраться из этого кошмарного дна... Я все сделаю для этого!!!"
    return


# Паб. Гримерка танцовщиц. Разговор Моники с брюнеткой Клэр.
# Следующий приход после второго разговора с рыжей танцовщицей
label dialogue_5_dance_strip_16:
    # брюнетка стоит спиной к Монике, переодевается, Моника стоит в дверях
    # Моника задумчиво смотрит на Клэр
    music Groove2_85
    img 22826
    with fadelong
    mt "Эта Клэр могла бы являть свою красоту с обложки журнала..."
    mt "А не танцуя в пабе перед толпой пьяных неудачников!"
    # Клэр в маске поворачивается к Монике, с улыбкой
    img 22827
    with fade
    clare "Привет, [monica_pub_name]. Ну как ты?"
    clare "Эшли говорит, что у тебя уже лучше получается. Она тобой довольна."
    if ep210_picture_was_marked == True and ep210_picture_marked_claire_comment == False:
        $ ep210_picture_marked_claire_comment = True
        # если Моника разрисовала портрет Молли
        # Клэр улыбаясь говорит
        img 22723
        with fade
        #
        $ notif(t_("Моника разрисовала фотографию Молли"))
        #
        clare "Кстати, отличный портрет получился!"
        clare "Наша звезда прямо-таки засияла..."
        music Hidden_Agenda
        img 16151
        with diss
        m "Нет-нет... Я тут ни при чем... Я ничего не делала."
        # Клэр смотрит на нее и улыбается
        img 16154
        with diss
        clare "Все ок. Я никому не скажу."


    img 22828
    with diss
    m "Хм. Я не удивлена, что Эшли довольна мной."  # проходит в гримерку и начинает раздеваться
    music Power_Bots_Loop
    img 22829
    with diss
    mt "Еще бы она была недовольна! Она теперь может на меня пялиться." # сердито
    mt "Как и ее муж-неудачник!"
    if ep29_quests_monica_molly_was_fine == False and ep29_quests_monica_molly_fine == False:
        music Groove2_85
        img 22830
        with fade
        clare "Надеюсь, у тебя не было конфликтов с ней?"
        clare "Про Эшли ходят не очень хорошие слухи."
        clare "Так что, лучше не связывайся с ней..."
        img 22831
        with diss
        m "Да? Я не знала..." # удивленно
        m "Спасибо за предупреждение..."
    music Groove2_85
    img 22832
    with diss
    mt "Эта озабоченная Эшли со своим таким же озабоченным мужем уже достали меня!"
    mt "Кто бы предупредил меня заранее, что с ними не стоит связываться?!"
    # Моника переодевается
    call dialogue_5_dance_strip_29b() from _call_dialogue_5_dance_strip_29b
    $ topless = False
    if _return == 0:
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    if _return == 1:
        $ topless = True
        $ cloth = "StripOutfit2"
        $ cloth_type = "StripOutfit"
#    menu:
#        "Надеть костюм с жилетом.":
#            pass
#        "Надеть только трусики.":
#            m "Я не выйду на сцену с голой грудью!!!"
#            return False
    # Клэр берет со столика в руки флакон
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    # корсет
    if topless == False:
        img 22753
        with fade
    # без корсета
    else:
        img 22833
        with fade
    clare "Ты забыла намазаться маслом для тела..."
    clare "[monica_pub_name], давай я тебе помогу?"
    $ menu_corruption = [0, monicaClaireOilingVest]
    menu:
        "Взять у Клэр масло и намазаться самой.":
            pass
        "Позволить Клэр намазать меня маслом." if game.extra == True or cloth == "StripOutfit1":
            # Клэр намазывает ее маслом
            if topless == True:
                $ monicaClaireOilingToplessCount += 1
                img 22754
                with fade
                sound hlup2
                w
                music stop
                music2 Loved_Up
                if monica_shiny_hole_queen_day > 0: # Если Моника королева
                    img 24348
                else:
                    img 22834
                with diss
                sound skin_lotion11
                w
                img black_screen
                with diss
                music stop
                stop music
                play music "<from " + str(float(rand(1,5))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling1_1 = Movie(play="video/v_Monica_Claire_Oiling1_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling1_1
                with fadelong
                wclean

#                music Loved_Up
                img 22835
                with diss
                clare "Какая же у тебя отличная фигура, [monica_pub_name]."

                img 22836
                with fade
                sound skin_lotion11
                mt "Она что, снова ко мне пытается пристать, как Эшли?!"

                music stop
                stop music
                play music "<from " + str(float(rand(1,5))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling1_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling1_2 = Movie(play="video/v_Monica_Claire_Oiling1_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling1_2
                with fadelong
                wclean
#                music Loved_Up
                img 22837
                with diss
                sound skin_lotion11
                w
                img 22838
                with diss
                sound skin_lotion11
                clare "Мужчины в зале с ума сойдут, когда тебя увидят."
                if monica_shiny_hole_queen_day > 0: # Если Моника королева
                    img 24349
                else:
                    img 22839
                with fade
                mt "Я к этому привыкла."
                mt "Мужчины всегда по мне с ума сходили..."
                img 22840
                with diss
                w

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling2_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling2_1 = Movie(play="video/v_Monica_Claire_Oiling2_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling2_1
                with fadelong
                wclean

                img 22841
                with diss
                sound skin_lotion11
                w
                img 22842
                with diss
                sound skin_lotion11
                clare "Ты сегодня будешь звездой, [monica_pub_name]."

                img 22843
                with fade
                sound skin_lotion11
                mt "Конечно, буду! Мне нет здесь равных!"
                mt "И не только здесь! Мне нигде нет равных!"

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_1 = Movie(play="video/v_Monica_Claire_Oiling3_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_1
                with fadelong
                wclean
#                music Loved_Up
                img 22844
                with diss
                sound skin_lotion11
                clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."
                img 22845
                with diss
                sound skin_lotion11
                clare "Ты просто создана для обложки какого-нибудь модного журнала."
                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_2 = Movie(play="video/v_Monica_Claire_Oiling3_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_2
                with fadelong
                wclean
                music2 stop
                music Groove2_85
                img 22846
                with fade
                mt "Хм... Хорошо, что она их не читает."
                mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
                ###################################





                ###################################

            else:
                $ monicaClaireOilingCount += 1
                img 22754
                with fade
                sound hlup2
                w
                music Loved_Up
                img 22755
                with diss
                sound skin_lotion11
                w
                img 22756
                with diss
                w
                img 22757
                with fade
                w
                img 22758
                with diss
                sound skin_lotion11
                clare "Какая же у тебя отличная фигура, [monica_pub_name]."
                img 22759
                with fade
                sound skin_lotion11
                mt "Она что, снова ко мне пытается пристать, как Эшли?!"
                img 22760
                with diss
                sound skin_lotion11
                clare "Мужчины в зале с ума сойдут, когда тебя увидят."
                img 22761
                with diss
                mt "Я к этому привыкла."
                mt "Мужчины всегда сходили по мне с ума..."
                if monica_shiny_hole_queen_day > 0: # Если Моника королева
                    img 24345
                else:
                    img 22762
                with fade
                sound skin_lotion11
                w
                if monica_shiny_hole_queen_day > 0: # Если Моника королева
                    img 24346
                else:
                    img 22763
                with diss
                w
                img 22764
                with fade
                sound skin_lotion11
                clare "Ты сегодня будешь звездой, [monica_pub_name]."
                img 22765
                with diss
                sound skin_lotion11
                mt "Конечно, буду! Мне нет здесь равных!"
                mt "И не только здесь! Мне нет равных нигде!"
                img 22766
                with fade
                sound skin_lotion11
                w

                img black_screen
                with diss
                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_1 = Movie(play="video/v_Monica_Claire_Oiling3_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_1
                with fadelong
                wclean

                music Loved_Up
                img 22767
                with diss
                sound skin_lotion11
                w
                img 22768
                with diss
                sound skin_lotion11
                clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_2 = Movie(play="video/v_Monica_Claire_Oiling3_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_2
                with fadelong
                wclean
                music Loved_Up
                img 22769
                with fade
                sound skin_lotion11
                w
                img 22770
                with diss
                sound skin_lotion11
                clare "Ты просто создана для обложки какого-нибудь модного журнала."
                img 22771
                with fade
                mt "Хм... Хорошо, что она их не читает."
                mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
                ###################################



                ###################################

            $ add_char_progress("Pub_StripteaseGirl2", 50, "oiling1")
#            return 1

    # Клэр, осматривая Монику
    # Переход на движок
    return

label dialogue_5_dance_strip_16a:
    clare "Выглядишь сногсшибательно."
    clare "Иди и покажи им, кто здесь звезда."

    return
# Джо перехватывает Монику перед входом на сцену
# Паб. Перед сценой. Разговор Моники с Джо.
# У сцены
label dialogue_5_dance_strip_17:
    # Джо стоит перед выходом на сцену
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music2 pub_noise1_low
    music Groove2_85
    img 22797
    with fadelong
    joe "[monica_pub_name], это костюм Клэр?"  # смотрит похотливо
    img 22798
    with fade
    m "Да." # раздраженно
    music Hidden_Agenda
    img 22799
    with diss
    joe "Я смотрю, ты с ней подружилась..."  # подмигивает
    music Groove2_85
    img 22800
    with fade
    m "Тебе что с этого?" # раздраженно
    img 22801
    with diss
    joe "Выяснишь для меня, как к ней подкатить?"
    m "???" # смотрит на него как на идиота
    music Hidden_Agenda
    img 22802
    with fade
    joe "Она тут ни с кем не общается..."
    joe "И никого к себе не подпускает..."
    joe "На приваты не соглашается, хотя предложений много..."
    joe "А она тут работает уже не один год. И я все это время не знаю, как подойти к ней..."
    # выходит Клэр с нагайкой, включает строгую училку
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 22803
    with fadelong
    clare "Что здесь происходит?!" # смотрит на Джо строго
    sound Jump2
    img 22804
    with hpunch
    clare "Тебе чего надо от [monica_pub_name]?!" # ткнув его в грудь нагайкой
    joe "Я... Мне... Я просто..." # растерянно мямлит и смотрит на нагайку
    music Power_Bots_Loop
    sound Jump2
    img 22805
    with vpunch
    clare "Я просто пойду сейчас к твоей жене!" #с угрозой
    clare "И расскажу, чем ТЫ тут занимаешься!"
    music Groove2_85
    img 22806
    with fade
    joe "Ч-ч-чем???"
    music Power_Bots_Loop
    img 22807
    with diss
    clare "Пристаешь к [monica_pub_name]!!!"
    music Groove2_85
    img 22808
    with diss
    joe "Я... Я не пристаю!"
    joe "Не надо ничего говорить Эшли!"
    music Power_Bots_Loop
    img 22809
    with diss
    clare "Тогда пошел отсюда! Быстро!!!" # ткнув его снова нагайкой
    joe "!!!"
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.0
    music Groove2_85
    img 22810
    with fade
    # Джо растерян, уходит
    clare "Вот кобель!"
    clare "!!!"
    # смотрит на Монику, улыбается
    img 22811
    with diss
    clare "Если снова будет приставать, скажи мне. Он меня боится."
    img 22812
    with fade
    m "Спасибо, Клэр."
    # Клэр уходит
    mt "Когда я выберусь из этого дна, заведу себе такой же хлыст от извращенцев!"
    $ add_char_progress("Pub_StripteaseGirl2", 50, "Pub_StripteaseGirl2_defend_monica1")
    music stop
    img black_screen
    with diss
    pause 1.5
    return


# Паб. Гримерка танцовщиц. Моника, после выступления.
label dialogue_5_dance_strip_18:
    if monicaDancedLastDay != day:
        return
    # не рендерить!
    # Моника возвращается в гримерку, там уже никого нет
    mt "В этот раз уже было попроще... Не хватало еще привыкнуть к этому!"
    mt "Надо немного потерпеть... Это когда-нибудь закончится."
    mt "И я смогу выбраться из этого кошмарного дна... Я все сделаю для этого!!!"
    return


# Паб. Моника выходит из гримерки. Если идет в сторону барной стойки, появляется Эшли.
# Разговор с Эшли после третьего (?) выступления Моники. Эшли прощает Монику (только первый раз)
# У сцены
label dialogue_5_dance_strip_19:
    # Эшли требовательно
    music2 pub_noise1_low
    music Groove2_85
    img 22790
    with fadelong
    ashley "[monica_pub_name], сколько ты заработала сегодня?"

    if monica_strip_tips_today == 0:
        img 22791
        with fade
        m "Сегодня я ничего не заработала..."
    else:
        img 22792
        with fade
        m "Сегодня я заработала [monica_strip_tips_today]."
        $ add_money(-monica_strip_tips_today)
        $ monica_strip_forgiveness_money_left -= monica_strip_tips_today

    img 22793
    with diss
    ashley "Тебе осталось отдать мне еще [monica_strip_forgiveness_money_left]."
    music Hidden_Agenda
    img 22847
    with fade
    ashley "Но я решила, что прощу тебе остаток долга." # улыбается
    img 22848
    with diss
    m "Простишь?" # удивленно
    m "???"
    music Groove2_85
    img 22849
    with fade
    ashley "В дни твоих выступлений в пабе всегда полно посетителей."
    ashley "И это приносит моему пабу хорошую выручку."
    ashley "Поэтому, если ты продолжишь танцевать, то сможешь зарабатывать."
    img 22850
    with diss
    m "Я смогу забирать чаевые?"
    img 22851
    with fade
    ashley "Да. Так что не спеши отказываться от танцев."
    ashley "Официанткой ты столько не заработаешь..."
    music Loved_Up
    ashley "А на сцене... Да еще и с голой попкой..."
    ashley "Ты будешь настоящей звездой, [monica_pub_name]!"
    music Power_Bots_Loop
    img 22852
    with diss
    m "Я не собираюсь выступать голая!!!"
    m "!!!"
    music Groove2_85
    img 22853
    with fade
    mt "Эта извращенка так и ждет, когда я выйду голая на сцену!"
    mt "Я не буду танцевать голой!"
    mt "Если меня кто-нибудь узнает, несмотря на мою маску..."
    mt "Боюсь даже думать о последствиях!"
    mt "!!!"
#    $ log1 = t_("Эшли простила мне долг. Теперь я могу зарабатывать, выступая на сцене в пабе Shiny Hole. Неужели для меня это теперь нормально?")
    return

# После этого появляется пункт выбора: Танцевать на сцене
label dialogue_5_dance_strip_20:
#    menu:
#        "Танцевать на сцене в Shiny Hole.":
#            pass
    music2 pub_noise1_low
    music Groove2_85
    img 22855
    with fadelong
    m "Эшли..."
    ashley "А, это ты..."
    img 22854
    with fade
    m "Я пришла работать на сцене."
    if day_time != "evening":
        img 20993
        with diss
        ashley "{c}Приходи вечером!{/c}"
        ashley "Днем танцев нет! Я не хочу терпеть эту громкую музыку еще и днем!"
        ashley "Мне и так хватает постоянного нытья Джо у меня под ухом!"
        return False
    img 22856
    with diss
    ashley "Хорошо, [monica_pub_name]."
    ashley "Иди в гримерку. Готовься к выступлению."

    if monica_shiny_hole_queen_day == 0: # Если Моника НЕ королева
        if dialogue_5_dance_strip_20_flag1 == True:
            img 22857
            with fade
            ashley "Не забудь потом отдать мне часть чаевых."
            ashley "Ты тут вертишь голым задом у пилона не просто так, [monica_pub_name]!"
            mt "Я не хочу даже спорить с этой хамкой..."
    return True


# Паб. Моника выходит из гримерки после выступления на сцене по желанию. Если идет в сторону барной стойки, появляется Эшли.
# Разговор с Эшли после первого выступления по желанию. ОДИН РАЗ!
# У сцены
label dialogue_5_dance_strip_21:
    # Эшли требовательно
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music2 pub_noise1_low
    music Groove2_85
    img 22790
    with fadelong
    ashley "[monica_pub_name], сколько ты заработала сегодня чаевых?"
    img 22791
    with fade
    m "Зачем тебе это нужно знать?" # удивленно
    img 22793
    with diss
    ashley "Ты забыла, что ты здесь работаешь за 30 процентов от чаевых?."
    m "???"
    music Power_Bots_Loop
    img 22858
    with fade
    m "Но ты же говорила, что я смогу забирать чаевые!"
    m "МОИ чаевые! Которые я заработала, выступая на сцене!"
    music Groove2_85
    img 22859
    with diss
    ashley "Ага. Ты забираешь 30 процентов чаевых, остальное - мне."
    ashley "Тебя что-то не устраиваает?!"
    music Groove2_85
    img 22860
    with fade
    m "..." # сердито смотрит на Эшли
    mt "Если я сейчас ей откажу, она запретит мне работать здесь..."
    mt "А мне нужна эта работа..."
    mt "Как же меня достала эта Эшли!"
    mt "!!!"
    img 22861
    with diss
    ashley "Чего ты ждешь?!"
    ashley "Сейчас же давай сюда чаевые или можешь убираться отсюда навсегда!"

    # Моника отдает чаевые
    if monica_strip_tips_today == 0:
        music Groove2_85
        img 22862
        with fade
        m "Мне никто не дал чевых сегодня..."
        img 22863
        with diss
        ashley "Надеюсь, в следующий раз ты заработаешь чаевые..."
        ashley "Для этого достаточно будет получше покрутить задом у пилона."
        music Loved_Up
        img 22864
        with fade
        ashley "Голым задом..."
        music Power_Bots_Loop
        img 22865
        with diss
        m "Я не собираюсь ТАК зарабатывать чаевые!!!"
        music Groove2_85
        img 22866
        with fade
        ashley "Хм. Все девочки сначала так говорят..." # c улыбкой
        ashley "Завтра приходи работать еще."
    else:
        music Groove2_85
        img 22792
        with fade
        $ add_money(-monica_strip_tips_today)
        m "Вот чаевые, которые я смогла получить..."
        $ tipsBack = round_down(float(monica_strip_tips_today)*pubMonicaDanceTipsKoeff, 0.05)
        if tipsBack == 0.0:
            $ tipsBack = 0.05
        $ add_money(tipsBack)
        ashley "Хорошо. Вот твои [pubMonicaDanceTipsKoeffText] процентов."
        music Loved_Up
        img 22867
        with diss
        ashley "И не забывай, что для твоей попки у меня найдется еще работа..." # подмигивает
        music Power_Bots_Loop
        img 22868
        with fade
        m "Меня не интересуют другие способы подработки!"
        mt "Она опять намекает на какую-то грязную работу!"
        mt "Извращенка!"
        mt "!!!"
        music Groove2_85
        img 22869
        with diss
        ashley "Завтра приходи работать еще."
    $ dialogue_5_dance_strip_20_flag1 = True
    return

# Паб. Моника выходит из гримерки после выступления на сцене по желанию.
# Регулярный разговор с Эшли после выступления по желанию. При клике на Джо или Эшли
# У барной стойки
label dialogue_5_dance_strip_22:
    if ep215_quests_ashley_dialogue1_active == True:
        $ ep215_quests_ashley_dialogue1_active = False
        jump ep215_dialogues1_pub_8
    if ep215_quests_ashley_dialogue2_active == True:
        jump ep215_dialogues1_pub_14
    music2 pub_noise1_low
    music Groove2_85
    img 21025
    with fadelong
    m "Эшли, я закончила работу."
    ashley "Сколько ты заработала сегодня чаевых, [monica_pub_name]?"
    if monica_strip_tips_today == 0:
        img 21013
        with diss
        m "Мне никто не дал чевых сегодня..."
    else:
        img 22899
        with fade
        $ add_money(-monica_strip_tips_today)
        m "Вот чаевые, которые я смогла получить..."
        if ep29_quests_monica_molly_fine == True:
            img 22651
            with diss
            ashley "Ты помнишь что ты наказана!?"
            ashley "Сделай так чтобы Молли простила тебя, иначе не будешь зарабатывать здесь ничего!"
            img 22653
            with fade
            mt "Сучка!"
            mt "Какой мне смысл танцевать, если приходится отдавать ей все деньги?!"
            return

        $ tipsBack = round_down(float(monica_strip_tips_today)*pubMonicaDanceTipsKoeff, 0.05)
        if tipsBack == 0.0:
            $ tipsBack = 0.05
        $ add_money(tipsBack)
        ashley "Хорошо. Вот твои [pubMonicaDanceTipsKoeffText] процентов."
        img 22696
        with fade
        ashley "Завтра приходи работать еще."

    $ questHelp("shinyhole_19", True)
#    if ep211_quests_pub_dialogue1_planned == True:
#        call ep211_quests_pub5()
#        $ ep211_quests_pub_dialogue1_planned = False
    return



# Моника может уйти, не отдавая чаевые.
label dialogue_5_dance_strip_23:
    if ep211_quests_pub_started_stole_tips == True:
        $ menu_corruption = [monicaPubDanceStoleTipsBanker]
        menu:
            "Уйти и не отдавать чаевые хозяевам бара.":
                if monica_shiny_hole_queen_day > 0:
                    mt "Я теперь королева Shiny Hole и мне не надо отдавать чаевые."
                    mt "Но, все-же, лучше сказать Эшли что я ухожу"
                    return True

                if monicaPubDanceStoleTipsStage == 0:
                    mt "Я не собираюсь отдавать никому мои чаевые!"
                    $ questHelp("shinyhole_27", True)
                    $ questHelp("shinyhole_28", skipIfExists=True)
                    call ep211_quests_pub2_exit_with_tips() from _rcall_ep211_quests_pub2_exit_with_tips
                    return False
                if monicaPubDanceStoleTipsStage == 1:
                    mt "Я боюсь воровать чаевые за танцы..."
                    mt "Не представляю что меня еще заставить делать эта извращенка Эшли..."
                return True
            "Остаться.":
                return True
    else:
        menu:
            "Уйти и не отдавать чаевые хозяевам бара.":
                if monica_shiny_hole_queen_day > 0:
                    mt "Я теперь королева Shiny Hole и мне не надо отдавать чаевые."
                    mt "Но, все-же, лучше сказать Эшли что я ухожу"
                    return True
                mt "По-моему Эшли следит за тем, чтобы я не ушла просто так..."
                return True
            "Остаться.":
                return True
    return


# Паб. Моника находится в гримерке после выступления на сцене по желанию. Появляется Джо.
# Моника заработала на сцене хорошие чаевые.
label dialogue_5_dance_strip_24:
    # Джо смотрит на Монику похотливо
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    sound2 man_steps
    pause 1.5
    music2 pub_noise1_low
    music Groove2_85
    img 22870
    with fadelong
    w
    img 22871
    with fade
    joe "[monica_pub_name], ты сегодня заработала хорошие чаевые..."  # с улыбкой
    img 22872
    with diss
    m "Да. А тебе какое дело до этого, Джо?" # раздраженно
    music Hidden_Agenda
    img 22873
    with fade
    joe "[monica_pub_name], ты хочешь заработать настоящие деньги?"
    joe "А не эти жалкие несколько баксов?"
    img 22874
    with diss
    m "На что ты намекаешь, Джо?" # с подозрением
    img 22875
    with fade
    joe "Есть один клиент..."
    joe "Он хочет, чтобы ты станцевала для него..."
    joe "Только для него."  # подмигивает
    music Power_Bots_Loop
    img 22876
    with hpunch
    m "Приватный танец?!" # зло
    m "Ты за кого меня принимаешь?!"
    music Groove2_85
    img 22877
    with diss
    mt "Как он смеет предлагать мне подобное?!"
    mt "Чтобы Моника Бакфетт танцевала приват!!!"
    mt "И для кого?! Для какого-нибудь неудачника?!"
    mt "Для которого лучшее развлечение в жизни - придти в эту дыру и выпить пива?!"
    mt "!!!"
    mt "Ни за какие деньги Я не стану этого делать!!!"
    img 22878
    with fade
    m "Я не собираюсь зарабатывать ТАКИМ способом, Джо!" # сердится
    m "И не хочу слышать больше подобных предложений!!!"
    m "!!!"
    music2 stop
    music Hidden_Agenda
    img 22879
    with diss
    joe "[monica_pub_name], может ты все-таки подумаешь хорошо?"
    joe "Это и правда неплохие деньги..."
    music Groove2_85
    img 22880
    with fade
    m "???" # смотрит на него как на идиота
    m "Нет!!!"
    music Hidden_Agenda
    img 22881
    with diss
    joe "Хорошо, [monica_pub_name]."
    joe "Но если подобные предложения от клиентов еще будут, то я тебе скажу об этом."
    joe "Вдруг ты передумаешь..." # Джо подмигивает и уходит
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    return

# Моника смотрит на Молли (глазик)
label dialogue_5_dance_strip_25a:
    mt "Что это еще такое? Она сидит с таким видом, будто она тут самая главная..."
    return
label dialogue_5_dance_strip_25:
    if monica_shiny_hole_queen_day > 0:
        mt "Молли... Бывшая королева Shiny Hole..."
        mt "Я выигрываю всегда! Не важно где!"
        return
    mt "Молли. Считает себя королевой сцены Shiny Hole..."
    mt "Звезда трущоб. Фи!"
    return

# Моника смотрит на Клэр (глазик)
label dialogue_5_dance_strip_26:
    mt "Эта Клэр могла бы быть моделью журнала..."
    mt "А не танцевать в пабе перед толпой пьяных неудачников!"
    return

# Моника говорит с Молли (диалог)
label dialogue_5_dance_strip_27:
    music Groove2_85
    img 22882
    with fade
    molly "Чего тебе?"
    molly "Я отдыхаю после выступления. Не отвлекай меня." # отворачивается
    if rand(1,2) == 1:
        mt "Я не хочу разговаривать с этой хамкой. Она провоцирует меня."
        mt "Я... боюсь не сдержаться и ударить ее..."
    else:
        mt "Ответить ей в таком же тоне означает - опуститься до ее уровня."
        mt "Я, Моника Бакфетт, никогда не опущусь до уровня этой хамки."

    if ep210_picture_was_marked == True and cloth == "Whore":
        # если Моника разрисовала портрет Молли
        img 16251
        with fade
        #
        $ notif(t_("Моника разрисовала фотографию Молли"))
        #
        molly " И кстати!"
        molly "Еще раз увижу, что ты испортила мой портрет!"
        molly "Простым штрафом ты не отделаешься, сучка!!!"
        $ ep210_picture_marked_molly_comment = True

    return

# Моника говорит с Клэр (диалог)
label dialogue_5_dance_strip_28:
    # strip corset
    if cloth == "StripOutfit1":
        music Groove2_85
        if monica_shiny_hole_queen_day > 0: # Если Моника королева
            img 24350
        else:
            img 22883
        with fade
        clare "Привет, [monica_pub_name]. Отлично выглядишь."
        m "Привет, Клэр. Ты тоже. Как отработала сегодня?"
        img 22886
        with diss
        clare "Получила массу удовольствия, как всегда."
        clare "Надеюсь, ты тоже хорошо отработаешь сегодня." # приветливо
        mt "Неужели в моем окружении появился хоть один адекватный человек?"

    if cloth == "StripOutfit2":
        #strip topless
        music Groove2_85
        if monica_shiny_hole_queen_day > 0: # Если Моника королева
            img 24351
        else:
            img 22884
        with fade
        clare "Привет, [monica_pub_name]. Отлично выглядишь."
        m "Привет, Клэр. Ты тоже. Как отработала сегодня?"
        img 22886
        with diss
        clare "Получила массу удовольствия, как всегда."
        clare "Надеюсь, ты тоже хорошо отработаешь сегодня." # приветливо
        mt "Неужели в моем окружении появился хоть один адекватный человек?"

    if cloth == "Whore":
        #whore outfit
        music Groove2_85
        if monica_shiny_hole_queen_day > 0: # Если Моника королева
            img 24352
        else:
            img 22885
        with fade
        clare "Привет, [monica_pub_name]. Отлично выглядишь."
        m "Привет, Клэр. Ты тоже. Как отработала сегодня?"
        img 22886
        with diss
        clare "Получила массу удовольствия, как всегда."
        clare "Надеюсь, ты тоже хорошо отработаешь сегодня." # приветливо
        mt "Неужели в моем окружении появился хоть один адекватный человек?"
    return

# Моника переодевается, кликнув на вешалку рядом со столиком Клэр
label dialogue_5_dance_strip_29:
    mt "Мне нужно переодеться. Что мне надеть?"
    if stage_dance_nude_planned == True and ep215_quests_vest_only_active == False or (ep215_quests_vest_only_active == True and get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False):
        $ menu_corruption = [0, monicaPutStripClothTopless]
    menu:
        "Костюм для сцены (с жилетом)":
            return 0
        "Костюм для сцены (без жилета)" if stage_dance_nude_planned == True and ep215_quests_vest_only_active == False or (ep215_quests_vest_only_active == True and get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False):
            if pubDanceCount < monicaDanceAmountToTopless or len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
                m "Я не выйду на сцену с голой грудью!!!"
                help "У Моники мало опыта работы танцовщицей."
                if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
                    help "Окрыты не все движения. Требуется [monicaPosesOpenedToStage2]."
                if pubDanceCount < monicaDanceAmountToTopless:
                    help "Требуется выйти на сцену [monicaDanceAmountToTopless] раз."
                return 0
            return 1
        "Одежда шлюхи":
            return 2
    return

label dialogue_5_dance_strip_29b:
    if stage_dance_nude_planned == True and ep215_quests_vest_only_active == False or (ep215_quests_vest_only_active == True and get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False):
        $ menu_corruption = [0, monicaPutStripClothTopless]
    menu:
        "Костюм для сцены (с жилетом)":
            return 0
        "Костюм для сцены (без жилета)" if stage_dance_nude_planned == True and ep215_quests_vest_only_active == False or (ep215_quests_vest_only_active == True and get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False):
            if pubDanceCount < 4 or len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
                m "Я не выйду на сцену с голой грудью!!!"
                help "У Моники мало опыта работы танцовщицей."
                if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
                    help "Окрыты не все движения. Требуется [monicaPosesOpenedToStage2]."
                if pubDanceCount < monicaDanceAmountToTopless:
                    help "Требуется выйти на сцену [monicaDanceAmountToTopless] раз."
                return 0
            return 1
    return
label dialogue_5_dance_strip_29a:
    mt "Я не буду ходить по этому мерзкому заведению в таком виде!"
    mt "Мне надо переодеться!"
    return

# мысли Моники
# не рендерить!!!
# Моника осматривает гримерку в Шайни-хол
label dialogue_5_dance_strip_30a:
    # бетонные стены, пол
    mt "Это гримерка?! Фи!"
    mt "В моем доме подвал выглядит приличнее!"
    mt "В моем бывшем доме..."
    return
label dialogue_5_dance_strip_30b:
    # трубы под потолком
    mt "Вентиляционные трубы в гримерке?"
    mt "Не похоже, что это дизайнерское решение..."
    return
label dialogue_5_dance_strip_30c:
    # картина Молли на стене
    img 22896
    with fade
    mt "Это что? Фото стриптизерши во время работы?"
    mt "Фи, как пошло!"
    mt "А где фото второй стриптизерши?"
    return
label dialogue_5_dance_strip_30d:
    # вешалки с одеждой
    mt "Какие-то дешевые тряпки на вешалке..."
    mt "Зачем им столько одежды здесь?"
    mt "Они же выступают на сцене почти голые."
    return
label dialogue_5_dance_strip_30e:
    # журналы на полу
    mt "Надеюсь, что там нет моего журнала..."
    mt "С моим фото на обложке..."
    return
label dialogue_5_dance_strip_30f:
    # мусорка возле столика Молли и в углу возле выхода
    mt "Фу! Здесь вообще не принято поддерживать порядок?"
    mt "Я такой грязи еще нигде не видела... Ну, если только в хостеле..."
    mt "В этих трущобах, наверное, жить и работать в грязи - это норма."
    return
label dialogue_5_dance_strip_30g:
    # столик Молли
    img 22898
    with fade
    mt "Это столик для грима?"
    mt "Минимум косметики, деньги, коктейль, сигарета... Фу!"
    return
label dialogue_5_dance_strip_30h:
    # столик Клэр
    img 22897
    with fade
    mt "Я тоже люблю, когда у меня есть много косметики."
    mt "Хоть я ею и не пользуюсь..."
    return
label dialogue_5_dance_strip_30i:
    # зеркала
    mt "В этих зеркалах возможно хоть что-то рассмотреть под слоем пыли?"
    return
label dialogue_5_dance_strip_30j:
    # плакат с Мулен Руж
    mt "Обои с изображением Мулен Руж?"
    mt "Кто додумался их сюда приклеить?"
    return
label dialogue_5_dance_strip_30k:
    # ковер
    mt "Ковер. Больше похож на какую-то тряпку..."
    return
label dialogue_5_dance_strip_30l:
    # комнатные растения возле двери
    mt "Хм... Как эти цветы здесь выживают?"
    return
label dialogue_5_dance_strip_30m:
    # одежда на полу
    mt "Одежда на полу вперемешку с мусором. Фу!"
    mt "Это потом кто-то надевает?"
    return
label dialogue_5_dance_strip_30n:
    # тумбочка с флокончиками из-под косметики
    mt "Это что? Какая-то косметика для тела..."
    return
label dialogue_5_dance_strip_30o:
    # тумбочка с JOY, лампочки над ней
    mt "Неплохо смотрится. Но не в этой убогой кладовке..."
    return
label dialogue_5_dance_strip_30p:
    # зеркало с бельем возле столика Клэр
    mt "Сломанное, старое зеркало вместо сушилки для белья? Хм..."
    return
label dialogue_5_dance_strip_30r:
    # штора - выход из гримерки
    mt "Здесь даже двери нет! Какая-то грязная тряпка вместо нее!"
    mt "Как здесь можно переодеваться?"
    return


label dialogue_5_dance_strip_scene_menu:
    menu:
        "Идти на сцену.":
            return True
        "Музыка: Последовательно" if stageMusicControlEnabled == True and stageMusicMode == 0:
            $ stageMusicMode = 1
        "Музыка: Случайно" if stageMusicControlEnabled == True and stageMusicMode == 1:
            $ stageMusicMode = 2
            $ stageCustomMusic = 0
        "Музыка: Трек 1" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 0:
            $ stageMusicMode = 2
            $ stageCustomMusic = 1
        "Музыка: Трек 2" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 1:
            $ stageMusicMode = 2
            $ stageCustomMusic = 2
        "Музыка: Трек 3" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 2:
            $ stageMusicMode = 2
            $ stageCustomMusic = 3
        "Музыка: Трек 4" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 3:
            $ stageMusicMode = 2
            $ stageCustomMusic = 4
        "Музыка: Трек 5" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 4:
            $ stageMusicMode = 2
            $ stageCustomMusic = 5
        "Музыка: Трек 6" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 5:
            $ stageMusicMode = 2
            $ stageCustomMusic = 6
        "Музыка: Трек 7" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 6:
            $ stageMusicMode = 2
            $ stageCustomMusic = 7
        "Музыка: Трек 8" if stageMusicControlEnabled == True and stageMusicMode == 2 and stageCustomMusic == 7:
            $ stageMusicMode = 0
            $ stageCustomMusic = 0
    jump dialogue_5_dance_strip_scene_menu
#        "Реплики из зала: Вкл":
#            pass
#        "Реплики из зала: Выкл":
#            pass
