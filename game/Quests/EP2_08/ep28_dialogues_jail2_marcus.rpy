label ep28_dialogues_jail2_marcus1:
# Моника оказывается у Маркуса в комнате допросов
# Боб говорит что заключенная доставлена
# Маркус отвечает что Боб может быть свободен

# Моника комментирует что снова этот ужасный кабинет.
# Но, в этот раз, она знает что надо делать и выберется отсюда!
# Ведь я знаю что делать... Хотя... Я пришла сюда и я не знаю что мне делать.
# Я как-то не задумывалась что скажу этому человеку, О БОЖЕ!!!
    music stop
    music2 stop
    music3 stop
    img black_screen
    with diss
    pause 3.0
    music Master_Disorder
    img 21630
    with fadelong
    marcus "О, Миссис Бакфетт..."
    marcus "Вы очень богатая и влиятельная женщина."
    img 21631
    with diss
    marcus "Ваш визит для меня большая честь."
    marcus "Чему я обязан такой чести?"
    img 21632
    with fade
    mt "Снова этот ужасный кабинет..."
    mt "Но, в этот раз я знаю, что надо делать, чтобы выбраться отсюда!"
    mt "Ведь я знаю, что делать... Хотя..."
    mt "Я пришла сюда и я не знаю, что мне делать."
    mt "Я как-то не задумывалась, что скажу этому человеку... О БОЖЕ!"
    music Groove2_85
    img 21633
    with diss
    mt "!!!"
    mt "Так! Моника, соберись! Скажи ему уже хоть что-нибудь!"
    m "..."
    # встает и расправляет плечи
    m "Мистер Маркус, я пришла поговорить с Вами."
    img 21634
    with diss
    marcus "???"
    img 21635
    with fade
    m "Мистер Маркус, спасибо, что согласились принять меня."
    music Master_Disorder
    img 21636
    with diss
    marcus "О, для меня честь принимать такую важную леди как Вы, Миссис Бакфетт."
    img 21637
    with diss
    marcus "Простите за условия нашей встречи. У меня не было времени подготовиться к ней."
    music Groove2_85
    img 21638
    with fade
    mt "Начало хорошее. Но расслабляться мне не стоит..."
    m "Ничего страшного, Мистер Маркус, все в порядке."
    marcus "Это замечательно!"
    img 21639
    with diss
    marcus "Итак, Миссис Бакфетт, Вы можете снять верхнюю одежду и присаживаться."
    music Power_Bots_Loop
    img 21640
    with fade
    mt "В смысле? Какую верхнюю одежду?"
    m "!!!"
    m "Верхнюю одежду?"
    music Groove2_85
    img 21641
    with diss
    marcus "Да, Миссис Бакфетт, уверен Вам неудобно находиться в помещении в верхней одежде."
    marcus "Рядом с Вами вешалка. Вы можете повесить ее."
    music Master_Disorder
    img 21642
    with diss
    marcus "Или, хотите, Я Вам помогу?"
#    music Groove2_85
    img 21643
    with fade
    mt "Он хочет, чтобы я разделась?! И сидела перед ним совсем голая?! И беззащитная..."
    m "!!!"
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 21644
    with fadelong
    mt "Он пытается унизить меня. Поставить в неловкое положение..."
    mt "Что ж..."
    mt "Я пришла сюда с определенной целью и я добьюсь ее!"
    mt "Этот жуткий Маркус не сломит меня!"
    mt "Просто сейчас нужно сделать, как он говорит..."
    m "Мистер Маркус, спасибо... Я сама..."
    sound highheels_short_walk
    img 21645
    with fade
    m "Спасибо что... заботитесь обо мне..."
    # Моника раздевается и присаживается, закрывшись руками

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 21646 #садится
    with fadelong
    mt "От этого разговора зависит моя жизнь!"
    mt "Я должна собраться и не обращать внимания на свою наготу..."
    mt "И на этот холодный стул..."
    mt "Это мелочи по сравнению с тем, что меня ожидает на ферме!"
    w
    img 21647
    with diss
    marcus "Миссис Бакфетт, не стесняйтесь."
    marcus "Вы можете вести себя более раскованно."
    img 21648
    with fade
    mt "!!!"
    img 21649
    with diss
    marcus "..."

    img 21650 # садится прямо
    with fade
    mt "Он... Издевается надо мной?"
    w
    menu:
        "Убрать руки с груди...":
            pass
    img 21651
    with diss
    mt "!!!"

    img 21652
    with fade
    marcus "Вы можете раздвинуть ноги, Миссис Бакфетт."
    marcus "Это не будет смущать меня."
    img 21653
    with diss
    marcus "Ведь мы с Вами друзья, не правда-ли?"
    music Power_Bots_Loop
    img 21654
    with hpunch
    mt "ЧТО?!"
    mt "Зачем? Что он задумал?!"
    w
    music Master_Disorder
    img 21655
    with fade
    marcus "Или мы не друзья?"
    # Моника опускает руки и садится ровно
    music Malicious
    img 21656
    with diss
    mt "Боже, как страшно!"
    mt "Но... мне нельзя сейчас спорить с ним!"
    mt "Я должна помнить о цели своего визита сюда!"
    mt "!!!"
    img 21657
    with diss
    w
    menu:
        "Раздвинуть ноги...":
            pass
    img 21658
    with Dissolve(1.0)
    mt "!!!"
    with diss
    w
    img 21659
    with fade
    m "Да, Мистер Маркус..."
    m "Мы... Мы с Вами друзья."
    music Master_Disorder
    img 21660
    with diss
    marcus "Итак, Миссис Бакфетт. О чем Вы хотели со мной поговорить?"

    music Malicious
    img 21661
    with fade
    mt "Мне надо собраться!"
    mt "Мне надо убедить его!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 21662
    with fadelong
    m "Мистер Маркус, Я пришла выразить Вам мою благодарность за свою заботу обо мне..."
    img 21663
    with diss
    marcus "..."
    img 21662
    with diss
    m "Вы замечательный, добрый человек."
    m "Вы умный и проницательный. И я пришла сказать это Вам."
    music Groove2_85
    img 21665
    with fade
    marcus "О, Миссис Бакфетт. Мы с Вами похожи."
    img 21666
    with diss
    m "???"
    img 21667
    with fade
    marcus "Из всей лести, я также предпочитаю самую грубую..."
    marcus "Итак, опустим..."
    marcus "Что Вы хотели обсудить со мной?"
    music Hidden_Agenda
    img 21668
    with diss
    mt "Надо аккуратнее подбирать слова..."
    m "Я... Я хотела обсудить с Вами..."
    m "Видите-ли, я сейчас нахожусь в довольно щекотливом положении."
    m "Мне приходится строго следить за тем что происходит вокруг..."
    music Groove2_85
    img 21669
    with fade
    marcus "Что Вы имеете ввиду, Миссис Бакфетт?"
    music Hidden_Agenda
    img 21670
    with diss
    m "Я имею ввиду соблюдение закона и..."
    music Groove2_85
    img 21671
    with fade
    marcus "Все вокруг соблюдают законы, Миссис Бакфетт."
    marcus "Разве это стоит вообще обсуждать?"

    music Hidden_Agenda
    img 21672
    with diss
    m "Мистер Маркус, я имею ввиду последствия..."
    m "Вы знаете, мне довольно сложно вести честный образ жизни, не имея документов и..."
    music Groove2_85
    img 21673
    with fade
    marcus "О, Миссис Бакфетт, право. Вам не стоит переживать из-за этого."
    music Hidden_Agenda
    img 21674
    with diss
    m "Да, но в ином случае я рискую отправиться в одно, место, где..."
    m "В которое я не хотела бы попадать, Мистер Маркус."
    music Groove2_85
    img 21675
    with fade
    marcus "Значит, тот образ жизни, что Вы сейчас ведете, не устраивает Вас, Миссис Бакфетт?"
    music Hidden_Agenda
    img 21676
    with diss
    m "Честно говоря, мне очень сложно, Мистер Маркус."
    m "И я бы хотела попросить Вас помочь мне..."
    music Groove2_85
    img 21677
    with fade
    marcus "О, Миссис Бакфетт. Я Вас понимаю."
    marcus "Я действительно осознаю все те неудобства, с которыми Вам приходится сталкиваться."
    marcus "И я категорически против этого."
    img 21678
    with diss
    m "???"
    img 21679
    with fade
    marcus "Я ведь с самого начала предупреждал Вас об этом."
    marcus "И я очень рад что Вы сами пришли к этому же выводу."
    music Hidden_Agenda
    img 21680
    with diss
    m "Что Вы имеете ввиду, Мистер Маркус?"
    m "К какому выводу я пришла?"
    music Villainous_Treachery
    img 21681
    with fade
    marcus "К тому, чтобы отправиться на ферму прямо сейчас."
    marcus "Я считаю, что такой леди как Вы ни к чему испытывать неудобства."
#    music Power_Bots_Loop
    img 21682
    with hpunch
    mt "ЧТО?! Нет-Нет!"
    m "!!!"
    music Master_Disorder
    img 21683
    with fade
    marcus "Вас сейчас окружает злой мир, полный неопределенности."
    marcus "А на Объекте 218 все будет просто и понятно."
    img 21684
    with diss
    marcus "Вам больше не придется принимать решений и питать излишние иллюзии о завтрашнем дне."
    music Power_Bots_Loop
    img 21685
    with hpunch
    m "НЕЕЕТ!!!"
    m "Мистер Маркус..."
    m "Я... Я не имела ввиду что пришла к такому выводу... Я..."
    music Master_Disorder
    img 21686
    with fade
    marcus "Но как же, Миссис Бакфетт."
    marcus "Вы же сами сказали, что Вас не устраивает Ваш теперешний образ жизни."
    music Malicious
    img 21687
    with diss
    mt "У меня путаются мысли! Все, что угодно, только не ферма!"
    mt "Надо сказать ему! Все, что угодно!!!"
    m "Я... Я..."
    music Master_Disorder
    img 21688
    with fade
    marcus "И Вы пришли ко мне за помощью..."
    marcus "Я окажу Вам помощь, Миссис Бакфетт."
    music Malicious
    img 21689
    with diss
    menu:
        "Спасибо, Мистер Маркус (отправиться на Ранчо 218 добровольно) (в будущих обновлениях) (disabled)":
            pass
        "Вы меня не так поняли!":
            pass
    # Моника вскакивает
    img 21690
    with fade
    m "Мистер Маркус! Я не это имела ввиду..."
    music Villainous_Treachery
    img 21691
    with diss
    marcus "А что же еще, Миссис Бакфетт?"
    marcus "Неужели Вам нравится то, как Вы сейчас живете?"
    m "Мне... Мне нравится, как я сейчас живу..."
    marcus "Вы лукавите, Миссис Бакфетт..."
    music Hidden_Agenda
    img 21692
    with fade
    m "Нет, Мистер Маркус! Мне... Мне правда нравится..."
    m "Я... Раньше я была слишком высокомерной..."
    m "У меня было слишком много денег и я..."
    m "И я не замечала мира вокруг..."
    img 21693
    with diss
    m "Текущее положение дел помогает мне открыть глаза..."
    m "Я... Я пережила много интересных историй."
    m "Моя жизнь стала очень разнообразна..."
    img 21694
    with diss
    m "Мистер Маркус... Спасибо Вам за это..."
    m "Я... Я правда хочу остаться здесь..."
    m "И... И не ехать на ферму!"

    music Master_Disorder
    img 21695
    with fade
    marcus "Миссис Бакфетт, неужели Вы правда справляетесь?"
    music Hidden_Agenda
    img 21696
    with diss
    m "С чем я справляюсь, Мистер Маркус?"
    music Master_Disorder
    img 21697
    with fade
    marcus "С тем что ничего не нарушаете."
    m "Ддддда....."
    img 21698
    with diss
    marcus "Вы действительно ничего не пытались нарушить здесь, в камере, пока ожидали нашей встречи."
    marcus "Оба раза. Хотя мы проверяли это."
    marcus "Мы общались с надзирателем и даже с заключенными."
    music Malicious
    img 21699
    with fade
    mt "!!!"
    mt "О БОЖЕ!"
    mt "Что бы было, если бы они рассказала про то, что я пыталась сбежать отсюда!"

    music Master_Disorder
    img 21700
    with diss
    marcus "Миссис Бакфетт, пожалуйста, сядьте на место в ту же позу, которую я попросил Вас принять..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Master_Disorder
    img 21702
    with fadelong
#    mt "..."
    w
    marcus "В ту же позу, Миссис Бакфетт... В ту же позу..."
    img 21703
    with Dissolve(1.0)
    w
    mt "!!!"
    marcus "И не двигайтесь. Тем что Вы бегаете передо мной, Вы меня отвлекаете от нашей беседы."

    music Master_Disorder
    img 21700
    with fade
    marcus "Вернемся к Вашей жизни вне этих стен."
    img 21701
    with diss
    marcus "А как же еда?"
    marcus "Вы ведь не можете работать, Миссис Бакфетт."
    marcus "Без документов это будет незаконно."

    music Hidden_Agenda
    img 21704
    with fade
    m "Я... Мистер Маркус..."
    m "Я - девушка. Я, как и все, сижу на диете."
    m "Так что мне практически не нужна еда."
    m "Благодаря этому я улучшаю свою фигуру."
    m "Я очень довольна своим образом жизни..."
    music Master_Disorder
    img 21705
    with diss
    marcus "А дом? У Вас нет средств снимать жилье."
    marcus "Да и, если бы были, Вы должны делать это официально, а иначе будет нарушение закона."
    marcus "Но у Вас нет документов."
    img 21706
    with diss
    m "..."
    img 21707
    with fade
    marcus "Где Вы живете, Миссис Бакфетт?" #пронзительно
    music Malicious
    img 21708
    with diss
    mt "Черт! Мне нельзя говорить ему, что я живу в своем доме!"
    mt "Но что я ему скажу?!"
    m "!!!"
    music Villainous_Treachery
    img 21709
    with fade
    marcus "Вы живете на улице?"
    img 21710
    with diss
    m "Я... Я... Да..."
    m "На улице..."
    img 21711
    with fade
    marcus "И Вам нравится?"

    img 21712
    with diss
    m "Дддда... Мистер Маркус... Мне нравится..."
    img 21713
    with fade
    marcus "Миссис Бакфетт, Вы знаете, что жить на улице без регистрации незаконно..."
    music Malicious
    img 21714
    with hpunch
    mt "О нет! Это нарушение закона! Он сейчас снова отправит меня в эту жуткую камеру!"
    mt "А потом на ФЕРМУ!!!"
    m "Я... Я... Мистер Маркус..."
    music Master_Disorder
    img 21713
    with diss
    marcus "Что Вы ответите на это?"
    music Malicious
    img 21714
    with fade
    m "Я... Я не знаю..."
    m "Я ничего не соображаю от ужаса..."
    m "Мистер Маркус, скажите что мне ответить?"
    music Groove2_85
    img 21715
    with diss
    marcus "Миссис Бакфетт, ответьте мне, зачем Вы на самом деле сюда пришли."
    music Malicious
    img 21716
    with fade
    mt "Я должна помнить о своей цели!"
    mt "Я должна уговорить его!"
    m "..."
    img 21717
    with diss
    marcus "..."
    m "Я... Я пришла..."
    m "Я пришла... пришла, чтобы..."
    img 21718
    with fade
    marcus "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21719
    with fadelong
    m "Я пришла, чтобы понравиться Вам, Мистер Маркус..."
    music Groove2_85
    img 21720
    with diss
    marcus "О, это похвально."
    marcus "Вы действительно можете понравиться мне, если будете стараться..."
    music Villainous_Treachery
    img 21721
    with diss
    marcus "На Ранчо 218."
    music Power_Bots_Loop
    img 21722
    with hpunch
    m "!!!"
    m "Мистер Маркус... На Ранчо... Я..."
    music Hidden_Agenda
    img 21723
    with fade
    m "Вы знаете, со мной могут произойти некоторые..."
    m "Некоторые изменения..."
    m "И я не смогу... понравиться Вам..."
    m "Поэтому я боюсь, что..."

    music Master_Disorder
    img 21724
    with diss
    marcus "Миссис Бакфетт, Вы правы. Вы будете смотреть на мир по-другому."
    marcus "И уже не будет той Моники Бакфетт, в глазах которой всегда горит огонь."
    marcus "Мне будет не хватать Вас..."
    music Malicious
    sound snd_bodyfall
    img 21725
    with hpunch
    mt "БОЖЕ!"
    mt "НЕТ!!!"
    m "!!!"
    music Master_Disorder
    img 21726
    with diss
    marcus "Но, возможно, есть другой путь..."
    img 21727
    with fade
    mt "Он... Он говорит... Про другой путь?"
    mt "Значит... Значит, он не торопится отправить меня на ферму?"
    mt "Это мой шанс!"
    m "???"
    img 21728
    with diss
    marcus "Миссис Бакфетт, подойдите сюда."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Master_Disorder
    img 21729
    with fadelong
    m "Да... Мистер Маркус..."
    # Подходит ближе к Маркусу
    img 21730
    with diss
    marcus "Я бы хотел проверить Ваше анальное отверстие, Миссис Бакфетт."
    marcus "Я боюсь, что для леди такого уровня и социального положения, как Вы, это будет не совсем комфортно."
    img 21731
    with diss
    marcus "И, если Вы откажетесь, я пойму Вас..."
    menu:
        "Позволить Маркусу проверить себя.":
            pass

    music Malicious
    img 21732
    with fade
    mt "Если я откажусь, мне конец. Я понимаю это!"
    mt "Мне надо разрешить ему, но надо как-то подыграть, я не должна быть просто куклой."
    mt "Иначе этому психу я стану неинтересна и для меня все будет кончено!"

    music Hidden_Agenda
    img 21733
    with diss
    m "Мистер Маркус... Это... Это вполне терпимая процедура..."
    m "Я... Я действительно леди очень высокого уровня, но..."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Hidden_Agenda
    img 21734
    with fade
    m "Но, если об этом просит такой мужчина как Вы..."
    music Loved_Up
    img 21735
    with diss
    m "То никакая леди не сможет отказать в этом..."
    mt "О БОЖЕ!!!"

    # Моника поворачивает к Маркусу задом
    img 21736
    with diss
    marcus "..."
    img 21737
    with diss
    w
    img 21738
    with diss
    w
    img 21739
    with diss
    w
    #sound Маркус вводит палец в попу Моники
    sound chpok2
    img 21740 # вводит палец
    with diss
    w
    sound snd_woman_pain
    img 21741
    with vpunch
    m "Ой!"

    music stop
    img black_screen
    with diss
    pause 1.5
    music Master_Disorder
    # Маркус запускает Монике в попу палец.
    #sound Маркус елозит пальцем
    music2 drkanje5
    img 21742
    with fadelong
    marcus "Хм... Миссис Бакфетт... Как интересно..."
    marcus "Моника Бакфетт... Владелица Модного Журнала..."
    marcus "Железная Леди... Холодная как лед..."
    img 21743
    with diss
    marcus "Мало кто знает что ТАМ у Вас очень тепло..."
    img 21744
    with diss
    m "..."
    img 21745
    with fade
    marcus "Сожмите мой палец..."
    m "Как?! Как я могу сжать его?"
    marcus "Сожмите его своим анальным отверстием."
    m "!!!"
    # Моника пытается сжать
    #sound Моника пытается сжать палец ))))
    music2 stop
    sound chpok9
    img 21746
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    m "Ииииииии..."
    img 21747
    with fade
    marcus "Слабовато, Миссис Бакфетт."
    marcus "Вы практически девственница."
    m "!!!"
    img 21748
    with diss
    m "Я... Я сильнее не могу, Мистер Маркус..."

    music stop
    img black_screen
    with diss
    #sound Маркус вытаскивает палец
    sound chpok6
    pause 1.5
    music Master_Disorder
    img 21749
    with fade
    marcus "А теперь присядьте."
    # Моника садится на стул
    sound highheels_short_walk
    img 21750
    with fadelong
    w
    img 21751
    with diss
    marcus "Нет, Миссис Бакфетт, не туда."
    marcus "Присядьте, пожалуйста, сюда."
    marcus "И сделайте это, пожалуйста, своим анальным отверстием."

    # Моника смотрит и видит анальную пробку
    music Malicious
    img 21752
    with hpunch
    mt "Анальным отверстием?! Я должна сесть на это?!"
    m "!!!"
    m "Что это?!"

    music Master_Disorder
    img 21753
    with diss
    marcus "Это, всего-лишь, небольшая трудность, Миссис Бакфетт."
    marcus "Я люблю людей, которые умеют их преодолевать."
    marcus "Любая девушка на ферме сделает это даже не поморщившись."
    marcus "Для Вас это будет сложнее, но я хочу увидеть доказательство."
    marcus "Того, что Вы действительно имеете желание выйти отсюда."

    music Malicious
    img 21754
    with fade
    m "Я..."
    mt "Мне нужно это сделать!"
    mt "Просто необходимо, если я хочу скорее выбраться отсюда!"
    music Master_Disorder
    img 21755
    with diss
    marcus "Я жду, Миссис Бакфетт."
    # Моника пытается сесть на пробку
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 21756
    with fadelong
    menu:
        "Сесть на анальную пробку.":
            pass
    w
    sound highheels_short_walk
    img 21757
    with diss
    w
    img 21758
    with diss
    w
    img 21759
    with fade
    w
    img 21760
    with diss
    w
    img 21761 # садится
    with fade
    w
    #sound Моника надавливает на пробку, но у нее не получается
    sound chpok12
    img 21762
    with diss
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 21763
    with fade
    m "У меня... Не получается..."
    m "Это штука... Она слишком большая..."

    marcus "Продолжайте, Миссис Бакфетт. У Вас должно получиться."

    menu:
        "Попробовать еще.":
            pass
    # Моника пробует еще
    img 21764
    with fade
    w
    #sound Моника садится на пробку, смещая ее в сторону
    sound chpok12
    img 21765
    with diss
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    # Пробка падает
    #sound пробка падает на пол
    sound down10
    img 21766
    with diss
    w
    music Groove2_85
    img 21767
    with fade
    m "Ой, она упала..."
    marcus "Подымите, поставьте ее и продолжайте далее."

    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 21768
    with fade
    m "Но..."
    music Villainous_Treachery
    marcus "Это Ваш шанс понравиться мне, Миссис Бакфетт."
    img 21769
    with diss
    marcus "Единственный шанс..."
    img 21770
    with fade
    m "!!!"
    menu:
        "Поставить пробку на место и сесть снова.":
            pass

    # Моника снова пытается
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 21771
    with fadelong
    w
    #sound Моника берет пробку рукой
    sound swish
    img 21772
    with diss
    w
    #sound Моника ставит пробку на стол
    sound Knock
    img 21773
    with diss
    w
    img 21774
    with fade
    w
    img 21775
    with diss
    w
    #sound Моника садится на пробку глубже
    sound chpok12
    img 21776
    with diss
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    music Malicious
    img 21777
    with fade
    w
    img 21778
    with diss
    mt "У меня не получается!"
    mt "Но это мой единственный шанс спастись!"
    menu:
        "Попытаться изо всех сил! Это единственный шанс спастись!":
            pass
    # Моника тужится и садится на пробку
#    sound anger2
#    sound snd_woman_scream1a
    img 21779
    with hpunch
    m "ААааааааргхххх..."
    #sound Моника села на пробку, звук
    sound chpok10
    img 21780 # звук что села
    with diss
    w
    img 21781
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "Ааааа!!! Как больно!"
    m "Я... Я села..."
    marcus "Встаньте и покажите мне."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Master_Disorder
    img 21783 # показывает
    with fadelong
    w
    img 21782
    with diss
    marcus "Браво, Миссис Бакфетт."
    marcus "Вам нравится то, что находится в Вас?"
    sound highheels_short_walk
    img 21784
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "Мне больно! Эта штука разрывает меня изнутри!"
    mt "Но что мне ответить ему?!"
    img 21785
    with diss
    m "Ддда..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Master_Disorder
    img 21786
    with fade
    marcus "Меня радует это."
    marcus "Сейчас Вам принесут Вашу одежду."
    marcus "Я жду Вас в своем кабинете."
    img 21787
    with diss
    m "..."
    img 21788
    with fade
    marcus "Да, и, если Вам действительно нравится, Я разрешаю Вам пока не вынимать это."
    img 21789
    with hpunch
    m "!!!"
    return


label ep28_dialogues_jail2_marcus2:
    # Сцена меняется на кабинет
    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_jail_door
    pause 1.0
    sound snd_fabric1
    pause 2.0
    sound highheels_run2
    pause 2.0
    music Groove2_85
    img 21790
    with fadelong
    marcus "О, Миссис Бакфетт..."
    marcus "Рад снова видеть Вас!"
    img 21791
    with diss
    marcus "У Вас красивое платье."
    marcus "Жаль это подделка. Вы достойны лучшего..."
    sound highheels_short_walk
    img 21792
    with fade
    marcus "Пожалуйста, присаживайтесь..."
    marcus "Платье можете пока оставить на себе."
    # Моника садится
    m "Сссспасибо... Мистер Маркус..."
    sound highheels_short_walk
    img 21793
    with diss
    m "ССсскажите... Что со мной будет?..."
    mt "Все, что угодно... Только не ферма!"
    img 21794
    with fade
    marcus "Миссис Бакфетт, скажите, Вам удобно?"
    img 21795
    with diss
    m "Да, Мистер Маркус. Мне вполне удобно."
    img 21796
    with fade
    marcus "Вам ничего не мешает?"
    img 21797
    with diss
    m "Нет, Мистер Маркус..."
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "Мне ужасно больно! Я хочу вытащить это поскорее!!!"
    music Master_Disorder
    img 21798
    with fade
    marcus "Вы ведь ничего не вынимали из себя?"
    marcus "Я к тому... Вам ведь действительно нравится то, что находится в Вас?"
    marcus "Вы меня не обманывали?"

    img 21799
    with diss
    m "Нет, Мистер Маркус..."
    m "Во мне... Во мне до сих пор это..."

    img 21800
    with fade
    marcus "Миссис Бакфетт, Вы бы хотели, чтобы это оставалось в Вас все время?"
    img 21801
    with diss
    m "Мистер Маркус... Я бы... Я бы хотела немного отдохнуть... От этого..."

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 21802
    with fadelong
    marcus "Миссис Бакфетт..."
    marcus "Я вспоминаю нашу первую встречу..."
    marcus "Вы пришли сюда и начали кричать на меня."
    marcus "Вы действительно были девушкой высокого положения и остаетесь ей."
    marcus "Но Вы сами сказали о том, что благодарны мне."
    marcus "Скажите, разве я заслуживал такого отношения к себе?"

    music Malicious
    img 21803
    with diss
    mt "О Боже..."
    mt "Что я ему тогда наговорила?! Знала бы я, что это за человек..."
    mt "..."
    music Hidden_Agenda
    m "Мистер Маркус... Я..."
    m "Я приношу свои извинения Вам."
    m "Это было ошибкой с моей стороны."
    m "Я... Я недооценила Вас."
    img 21804
    with diss
    m "Просто это было все было так неожиданно..."
    m "Я прошу Вас простить меня..."
    music Groove2_85
    img 21805
    with fade
    marcus "Мне нравятся Ваши слова, Миссис Бакфетт."
    marcus "Скажите, ведь Вы все та же сильная леди, которая вошла сюда?"
    marcus "Ведь Вы ничуть не изменились, правда?"
    music Master_Disorder
    img 21806
    with diss
    marcus "Для меня важно, чтобы эти слова говорила именно она."
    img 21807
    with diss
    m "Да, Мистер Маркус..."
    img 21808
    with fade
    marcus "Это неубедительно. Скажите кто Вы."
    marcus "Сделайте это так, как Вы умеете говорить!"
    # Моника встает, расправляет плечи и говорит ледяным тоном
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    img 21809
    with fadelong
    w
    img 21810
    with diss
    m "Я - Моника Бакфетт."
    m "Я - владелица Модного Журнала."
    m "Все люди вокруг подчиняются мне."
    m "Моя красота и богатство не имеют равных далеко за пределами этого места."
    music Master_Disorder
    img 21811
    with fade
    marcus "Хорошо. Теперь покажите мне."
    music Pyro_Flow
    img 21812
    with diss
    m "Показать ЧТО?"
    music Master_Disorder
    img 21813
    with fade
    marcus "Ту вещь, которая в Вас. Я хочу Вам помочь..."
    img 21814
    with diss
    m "!!!"
    img 21815
    with fade
    marcus "Владелица Модного Журнала, поднимите юбку. Не стесняйтесь."
    marcus "Я хочу проверить Ваши слова."
    img 21816
    with diss
    mt "Он смеется надо мной!!! Да как он..."
    mt "Черт!"
    m "..."

    # Моника задирает платье и показывает пробку, которая в нее вставлена
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 21817
    with fadelong
    w
    img 21818
    with diss
    w
    sound snd_fabric1
    img 21819
    with diss
    w
    marcus "О, Миссис Бакфетт..."
    marcus "Вы подобрали правильный цвет платья..."
    marcus "Должен признать, что Вы действительно разбираетесь в моде."
    img 21820
    with diss
    marcus "Ваша интуиция позволяет Вам соблюсти правильное сочетание цветов в любой ситуации."
    marcus "Даже в той, которую Вы не можете предугадать заранее."
    img 21821
    with fade
    marcus "Вы можете подойти ко мне, я помогу Вам."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 21822
    with fadelong
    marcus "Повернитесь спиной."
    # Моника подходит
    # Маркус вытаскивает пробку (анимация)
    sound highheels_short_walk
    img 21823
    with diss
    w
    img 21824
    with diss
    w
    music stop
    img 21825
    with diss
    w
    scene black
    sound Monica_butt_plug_v
    image videov_Marcus_Monica_Dildo_1_1 = Movie(play="video/v_Marcus_Monica_Dildo_1_1.mkv", fps=30, loop=False, image="/images/Slides/v_Marcus_Monica_Dildo_1_1_stop.jpg")
    show videov_Marcus_Monica_Dildo_1_1
    pause 2.5
    music Master_Disorder
    wclean

#    img 21826
#    img 21827
    sound snd_woman_pain
    img 21828
    with hpunch
    m "ААААЙ!!"
    # Моника оборачивается
    sound highheels_short_walk
    img 21829
    with diss
    w
    music stop
    w
    # Маркус держит пробку.

    # Маркус нюхает пробку
    sound snd_sniff1
    img 21830
    with fade
    marcus "Ммммм... Превосходно!"
    music Master_Disorder
    img 21831
    with diss
    marcus "Не хотите попробовать?"
    m "Что?!"
    img 21832
    with fade
    marcus "Попробуйте это, Миссис Бакфетт."
    marcus "Мне это нравится, а Вам?"
    music stop
    m "???"
    sound snd_sniff1
    img 21833 # Моника нюхает
    with diss
    mt "Это... Это просто отвратительно!"

    music Groove2_85
    img 21834
    with fade
    marcus "Вы достаточно сказали сегодня."
    img 21835
    with diss
    marcus "Теперь Я хочу кое-что Вам рассказать."
    marcus "Вы женщина очень высокого положения. Вы привыкли говорить, а не слушать."
    marcus "И, для того, чтобы быть уверенным, что Вы не будете перебивать меня..."
    img 21836
    with diss
    marcus "Возьмите это в рот."

    music Power_Bots_Loop
    img 21837
    with hpunch
    mt "Что?! В рот?! Он достал это из моей попы только что!"
    m "!!!"
    m "Но..."
    marcus "Вы же не собираетесь перебивать меня, Миссис Бакфетт?"
    m "Нет..."
    img 21838
    with diss
    marcus "Тогда нет причин не взять в рот это..."
    marcus "Или есть какие-то причины?"

    m "Нннет..."

    # Маркус засовывает пробку Монике в рот
    music stop
    img black_screen
    with diss
    pause 1.5
    music Malicious
    img 21839
    with fadelong
    mt "Фуууу!!! Как это противно!"
    mt "Но если я откажусь..."
    w
    sound snd_gulp
    img 21840
    with diss
    w
    music Groove2_85
    img 21841
    with fade
    marcus "Вы можете присесть."
    # Моника садится
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 21842
    with fadelong
    w
    img 21843
    with diss
    marcus "Итак, Миссис Бакфетт..."
    marcus "Я удивлен и обрадован Вашему визиту."
    marcus "Пока Вы меня ожидали, я был в отъезде."
    music Villainous_Treachery
    img 21844
    with fade
    marcus "И как раз собирался, по возвращению, арестовать Вас."
    img 21845
    with diss
    m "!!!"
    music Groove2_85
    img 21846
    with fade
    marcus "Вы спросите насчет Мистера Дика?"
    marcus "Да, действительно, его действия являются определенным препятствием между нами."
    img 21847
    with diss
    marcus "Однако, я нашел способ обойти его."
    music Malicious
    img 21848
    with hpunch
    m "!!!"
    music Groove2_85
    img 21849
    with fade
    marcus "Видите-ли, за мной стоят еще люди, с которыми я вынужден считаться..."
    marcus "И эти люди также хотят заполучить Вас."
    m "..."
    img 21850
    with diss
    marcus "Они видят препятствие только в действиях Мистера Дика."
    marcus "Но не знают о том, что в действиях Мистера Дика есть слабая сторона."
    marcus "Дело в том, что я работаю здесь, на месте. И вижу больше них..."
    music Malicious
    img 21851
    with diss
    m "!!!"
    music Groove2_85
    img 21852
    with fade
    marcus "И Я, и Эти Люди - всецело доверяем друг другу."
    marcus "С моей стороны было бы крайне неудобно не сообщать им новую информацию..."
    music Villainous_Treachery
    marcus "Поэтому, я собирался сообщить им о ней и арестовать Вас немедленно..."
    music Malicious
    img 21853
    with diss
    m "!!!"
    music Groove2_85
    img 21854
    with fade
    marcus "Для меня было удивлением, что Вы сделали такой своевременный упреждающий шаг..."
    m "..."
    music Master_Disorder
    img 21855
    with diss
    marcus "Как-будто кто-то очень мудрый подсказал Вам его..."
    img 21856
    with diss
    m "!!!"
    music Groove2_85
    img 21857
    with fade
    marcus "Но, думаю, это Ваша женская интуиция, которая помогает Вам..."
    img 21858
    with diss
    m "..."
    img 21859
    with fade
    marcus "Вы пытаетесь заставить меня думать, что играть с Вами ЗДЕСЬ будет интереснее, чем играть на Ранчо 218."
    marcus "Заставить быть ребенком, который не хочет делиться своей игрушкой с остальными..."
    img 21860
    with diss
    m "..."
    img 21861
    with fade
    marcus "Интересная попытка..."
    marcus "И, Вы знаете... Я заинтересован..."
    img 21862
    with diss
    m "..."
    music Master_Disorder
    img 21863
    with fade
    marcus "Понимаете-ли... Имея неограниченную власть..."
    marcus "Становится все сложнее и сложнее развлекать себя..."
    img 21864
    with diss
    marcus "Вы ведь меня понимаете, Миссис Бакфетт, правда?"
    img 21865
    m "!!!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music Master_Disorder
    img 21866
    with fade
    marcus "Вы можете идти, на этот раз..."
    marcus "Я пока не буду сообщать никому о той информации, что у меня есть..."
    marcus "Пока..."
    img 21867
    with diss
    marcus "И, не забывайте, я не единственный, кто стоит за всем этим."
    marcus "Стоит Вам хоть немного оступиться, и об этом узнают ТАМ."
    marcus "Даже в этом кабинете. Сейчас очень редкое короткое окно, когда я уверен, что нас не слышат."

    # Моника встает, продолжая держать пробку во рту
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 21868
    with fadelong
    marcus "Да, и Вы можете снова придти ко мне, когда будете готовы..."
    marcus "Заинтересовать меня еще раз..."
    music Master_Disorder
    img 21869
    with diss
    marcus "Пока я не успел потерять тот интерес, что у меня есть сейчас..."
    img 21870
    with diss
    m "!!!"
    marcus "Можете идти."
    sound highheels_short_walk
    img 21871
    with fade
    marcus "И сохраните эту вещь. Она будет Вам напоминать о нашей дружбе..."
    # Моника уходит

    return

label ep28_dialogues_jail2_marcus3:
    # Моника говорит на улице
    # no render
    mt "О БОЖЕ!"
    mt "Я вырвалась!"
    mt "ВЫРВАЛАСЬ!!!"
    mt "Я думала, что мне конец..."
    mt "Какой это был кошмар..."
    # Если были заключенные
    if ep28_quests_monica_offended_prisoners == False:
        mt "И эти заключенные..."
        mt "Я не хочу об этом думать!"
        mt "Лучше постараться об этом забыть!"
    #
    mt "Этот Маркус..."
    mt "И тот страшный сон..."
    mt "Чего он хочет от меня?!"
    mt "Я не понимаю этого!"
    mt "Он сказал, чтобы я снова пришла к нему..."
    mt "Но у меня от ужаса дрожат коленки, когда я даже думаю об этом..."
    mt "..."
    mt "Эта штука у меня во рту..."
    mt "Мне надо вынуть ее..."
    mt "Надо убрать ее куда-то, в спальне. Маркус сказал сохранить ее."
    mt "Но зачем?!"
    mt "И у меня болит попа..."
    mt "Но я счастлива, что я снова на свободе!"

#    help "Продолжение истории с Маркусом в следующих обновлениях игры!"
#    $ log1 = t_("Анальная пробка")
    return

label ep28_dialogues_jail2_marcus4:
    # Моника приходит в спальню
    mt "Мне лучше убрать эту штуку."
    return


label ep28_dialogues_jail2_marcus5:
    # Моника пытается зайти в полицию
    if act=="l":
        return
    call ep213_quests_police1_check_init() from _rcall_ep213_quests_police1_check_init
    if _return == False:
        return False
    mt "Я не готова идти туда..."
    mt "Мне придется это сделать..."
    mt "Но... Не сейчас... Нет!"
    return False







#
