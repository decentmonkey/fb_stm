# На следующий день днем Мелани идет к Дику
# играет музыка, Мелани заходит в entrance
# Там ее узнает рецепшин, восторгается и говорит
# Здравствуйте, Мисс Мелани !
# Это Вы? Я не верю своим глазам!
# Чем я могу быть полезна для Вас?
# Мелани говорит что пришла проведать одного сеньора, его зовут Дик.
# Та спрашивает Мистер Дик?
# Мелани говорит: Да, Дик. То-ли адвокат, то-ли как-то еще.
# Рецепшин отвечает: да, его так называют!
# Он как раз на месте, Вы можете пройти к нему!
# Мисс Мелани , разрешите взять Ваш автограф? Это для моей дочери, она большая ваша поклонница!
# Мелани отвечает что да, можно, тогда проводите меня к Мистеру Дику.
# Я боюсь заблудиться и поцарапать свою туфельку.
# Рецепшин отвечает с радостью что проводит Мисс Мелани к Мистеру Дику!
label ep23_dialogues6_1:
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    music m80s_Things
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_16
    scene black_screen
    with Dissolve(1)
    img 8881
    with fadelong
    w
    img 8883
    with fade
    w
    img 8884
    with fade
    w
    img 8882
    with fade
    w
    img 8885
    with fade
    w
    img 8887
    with Dissolve(0.5)
    w
    img 8888
    w
    img 8889
    w
    img 8886
    with fade
    w
    music ZigZag
    img 8890
    with fade
    reception_secretary "Здравствуйте, Мисс Мелани!"
    "Это Вы? Я не верю своим глазам!"
    "Чем я могу быть полезна для Вас?"
    img 8891
    melanie "Добрый день."
    "Я пришла проведать одного сеньора."
    "Его зовут Дик."
    img 8893
    reception_secretary "Мистер Дик?"
    img 8892
    melanie "Да, Дик. То-ли Адвокат, то-ли как-то еще..."
    img 8893
    reception_secretary "Да, его так называют!"
    "Он как раз на месте, Вы можете пройти к нему!"
    img 8894
    with fade
    melanie "..."
    img 8895
    reception_secretary "Мисс Мелани, разрешите взять Ваш автограф?"
    "Это для моей дочери, она большая Ваша поклонница!"
    img 8896
    melanie "Да, конечно можно."
    "Тогда проводите меня к Мистеру Дику."
    "Я боюсь заблудиться здесь и поцарапать свою туфельку."
    img 8897
    with fade
    reception_secretary "Я с радостью провожу Мисс Мелани к Мистеру Дику!"
    "Пожалуйста, следуйте за мной!"
    return

label ep23_dialogues6_2:
    # Идут к Виктории.
    # Виктория сидит работает, несколько кадров как Мелани крутая идет в ее сторону.
    # Виктория поднимает глаза, удивленно.
    # Они подходят к столу Виктории.

    # Виктория зло смотрит на Мелани.
    # В это время сбоку говорит рецепшин.
    # Здравствуйте, Мисс Виктория, мы пришли к Мистеру Дику и...
    # Виктория прерывает и привстает. Мистер Дик занятой человек, как Вас представить? Вы записаны к нему на встречу?

    img 8898
    with fadelong
    w
    img 8899
    with fade
    reception_secretary "Этот этаж занимает Мистер Дик."
    "Пожалуйста, пройдемте."
    img 8900
    with Dissolve(0.5)
    w
    img 8901
    w
    img 8902
    with Dissolve(0.5)
    w
    img 8903
    w
    img 8904
    with fade
    w
    music Villainous_Treachery
    img 8905
    with fade
    reception_secretary "Здравствуйте, Мисс Виктория!"
    reception_secretary "Мы пришли к Мистеру Дику и..."
    img 8906
    dick_secretary "Мистер Дик занятой человек!"
    "Как Вас представить?"
    "Вы записаны к нему на встречу?"

    # Рецепшин обескураженно отвечает: я... мы.. Миссис Виктория, я не знаю есть-ли запись у Мистера Дика, дело в том что это...
    # Мелани прерывает и выходит вперед. Меня зовут Мелани. Не беспокойся, куколка, я представлюсь сама.
    # Мелани пальчиком на плечо сажает Викторию назад в кресло. Виктория обескуражена.
    # Мелани проходит вперед. Рецепшин по инерции тоже движется вперед.
    # Виктория вскакивает, преграждает дорогу ей и говорит что посещение Мистера Дика только по записи!
    img 8907
    with fade
    reception_secretary "Я... Мы.. Мисс Виктория..."
    "Я не знаю, есть-ли запись у Мистера Дика, дело в том что это..."
    sound heel1
    music ZigZag
    img 8909
    with fadelong
    #звук каблуков
    w
    img 8908
    with fade
    melanie "Меня зовут Мелани..."
    img 8910
    dick_secretary "!!!"
    img 8911
    with fade
    "Не беспокойся, куколка..."
    sound Jump1
    img 8912
    with Dissolve(0.5)
    w
    img 8913
    "Я представлюсь сама..."
    sound heel1
    img 8914
    #звук каблуков
    with fade
    w
    sound snd_door_close1
    img black_screen
    with fade

    music Villainous_Treachery
    img 8915
    #звук каблуков
    with fade
    w
    img 8916
    w
    img 8917
    with fade
    dick_secretary "Посещение Мистера Дика только по записи!"

    # Мелани заходит к Дику.

    # Здравствуйте, Мистер Дик. Могу я зайти?
    # Дик обескуражен! Мелани???
    # Мелани улыбается
    # Дик вскакивает подает стул для Мелани.
    # Конечно, Мелани! Я очен рад Вас видеть!
    # Пожалуйста, присаживайтесь! Что привело Вас ко мне?
    music ZigZag
    img 8918
    with fadelong
    w
    img 8919
    w
    img 8920
    melanie "Здравствуйте, Мистер Дик."
    "Могу я зайти?"
    img 8921
    dick "???"
    "!!!"
    img 8922
    with fade
    "Мелани???"
    melanie "..."
    sound snd_bodyfall
    img 8923
    with Dissolve(0.5)
    #bodyfall
    dick "ОЙ!!!"
    img 8924
    with fade
    melanie "Осторожнее, Мистер Дик."
    melanie "Берегите себя!"
    img 8925
    melanie "Так я могу зайти?"

    img 8926
    with fade
    dick "Конечно, Мелани!"
    "Я очень рад Вас видеть!"
    img 8927
    "Пожалуйста, присаживайтесь!"
    img 8928
    with fade
    "Что привело Вас ко мне?"

    # Мелани отвечает что привело к нему важное дело, касающееся юридической практики.
    # Что она пришла к Дику, так как слышала что он лучший адвокат в городе.
    # Дик отвечает что это так и он готов сделать все, чтобы помочь Мелани.
    # Дик садится на стул рядом с Мелани.
    music Groove2_85
    img 8929
    melanie "Меня привело к Вам важное дело, касающееся юридической практики."
    melanie "Я пришла к Вам, Мистер Дик, так как слышала что Вы лучший адвокат в городе."
    img 8930
    dick "Да, Мелани! Это так!"
    "Я готов сделать ВСЕ, чтобы помочь ВАМ!!!"

    # В это время заглядывает Виктория из-за двери и говорит "Мистер Дик?"
    # Дик отвечает Виктории что у него важный клиент и чтобы она подождала пока Дик освободится.
    img 5732
    with fade
    dick_secretary "Мистер Дик?"
    music Power_Bots_Loop
    img 8931
    dick "Виктория, у меня очень важный клиент."
    "Подожди, пожалуйста, когда я освобожусь."
    img 8932
    w
    img 5734
    w

    # Мелани улыбается, глядя в сторону Виктории.
    # Мелани говорит Дику, что случилась трагедия и это касается кое-какой вещи, которая имеет к Мелани близкие чувства.
    # Дик интересуется про какую трагедию говорит Мелани и готов всецело помочь ей.
    music Hidden_Agenda
    img 8933
    with fade
    melanie "..."
    melanie "Мистер Дик, дело в том, что случилась трагедия..."
    img 8934
    dick "..."
    img 8935
    with fade
    melanie "И это касается кое-какой вещи, с которой у меня близкие чувства!"
    img 8936
    dick "Мелани! Пожалуйста, расскажите скорее про какую трагедию Вы говорите!"
    "Я всецело готов помочь ВАМ!"

    # Мелани отвечает что у нее есть маленькая собачка, которую она выгуливала этим утром рядом с парком.
    # Собачка убежала с поводка и написала на колесо, стоящей неподалеку машины, очень дорогой машины.
    # К сожалению, Мелани не успела вовремя догнать собачку. В это время вышел водитель машины (наемный) и
    # стал ругаться на собачку и сказал что пустит ее на шашлык!
    img 8937
    with fade
    melanie "Видите-ли, Мистер Дик, у меня есть маленькая собачка."
    "Я выгуливала ее этим утром рядом с парком."
    img 8938
    with Dissolve(0.5)
    "Я думала про деревья, про прекрасную погоду и не заметила как собачка убежала с поводка!"
    "Она убежала с поводка и написала на колесо стоящей неподалеку машины, очень дорогой машины..."
    "К сожалению, я не успела вовремя догнать собачку!"
    img 8939
    with fade
    "В это время вышел мужчина из машины."
    "Я так поняла что он работает водителем."
    img 8940
    "Он (хмык) стал ругаться на собачку и сказал что..."
    music Power_Bots_Loop
    img 8941
    with hpunch
    "Он сказал что пустит ее на шашлык... (хмык)"

    # Дик поинтересовался очень участливо что этот негодяй сказал и Мелани что-то?
    # О, нет. Увидев меня он сразу же сел за руль и уехал. Но вот собачка... она очень тяжело пережила подобное обращение
    # Ведь собачки чувствуют эмоции людей. И теперь ей пришлось увезти ее к ветеринарному психологу, где она теперь получает помощь.
    # Дик в бешенстве. Да как смеет какой-то халдей нарушать права животных в этом городе!
    # Я проучу этого негодяя! Он будет всю оставшуюся жизнь обеспечивать Вашу бедную собачку лучшими кормами и оплачивать полный уход за ней!
    music Groove2_85
    img 8942
    with fade
    dick "Мелани, могу я поинтересоваться, имел-ли смелость этот негодяй сказать что-либо и в Ваш адрес?"
    music Hidden_Agenda
    img 8943
    melanie "О, нет! Увидев меня он сразу же сел за руль и уехал."
    img 8944
    "Но вот собачка... она очень тяжело пережила подобное обращение."
    "Ведь животные чувствуют эмоции людей."
    img 8945
    "И теперь мне пришлось отвезти ее к ветеринарному психологу."
    "Где она в данный момент получает помощь."
    music Groove2_85
    img 8946
    with fade
    dick "Мелани, Вы уже отвезли собачку? Может быть Вам нужна помощь?"
    img 8947
    melanie "Я уже отвезла собачку, Мистер Дик. Она в безопасности..."
    music Power_Bots_Loop
    img 8948
    with fade
    dick "Мелани! Я не верю своим ушам!"
    "Да как смеет какой-то халдей нарушать права животных в этом городе!"
    img 8949
    "Я проучу этого негодяя!"
    img 8950
    "Он будет всю оставшуюся жизнь обеспечивать Вашу бедную собачку лучшими кормами!"
    "И оплачивать полный уход за ней!"

    # Мелани говорит: спасибо, Мистер Дик! Я знала что Вы настоящий джентельмен.
    # Дик спрашивает записала-ли Мелани номер машины. Дик выяснит кому она принадлежит и инициирует иск.
    # Мелани отвечает что да, я записала в блокнотик, но, к сожалению, забыла его дома.
    # Она понимает что Мистер Дик очень занятой человек, но, если вдруг у него будет время,
    # То он мог бы отвезти Мелани к ней домой, чтобы записать номер из ее блокнотика.
    # Дик восторженно отвечает что у него всегда найдется время для такого важного клиента как Мелани.
    # Предлагает поехать прямо сейчас же, потому что столь важное юридическое дело не может ждать.
    # А вдруг этот мерзавец попытается выехать из страны! Надо действовать быстрее!

    music Hidden_Agenda
    img 8951
    with fade
    melanie "Спасибо, Мистер Дик! Я знала что Вы настоящий джентельмен!"
    music Power_Bots_Loop
    img 8952
    dick "Мелани, Вы записали номер машины?"
    "Я выясню кому она принадлежит и инициирую иск!"
    music Hidden_Agenda
    img 8953
    with fade
    melanie "Да, Мистер Дик..."
    "Я записала номер в блокнотик."
    "Но, к сожалению..."
    "Я забыла его дома..."
    img 8954
    melanie "Я понимаю что Вы, Мистер Дик, очень занятой человек..."
    "Но, если вдруг у Вас будет время, то..."
    img 8955
    with fade
    dick "..."
    img 8956
    with Dissolve(0.5)
    melanie "То Вы бы могли отвезти меня ко мне домой, чтобы записать номер из блокнотика."
    "Который я оставила дома..."
    music Groove2_85
    img 8957
    with fade
    dick "Что вы! У меня всегда найдется время для такого важного клиента, как Вы, Мелани!"
    dick "Я предлагаю поехать незамедлительно!"
    "Столь важное юридическое дело не может ждать ни минуты!"
    img 8958
    "Вдруг этот мерзавец попытается выехать из страны?"
    "Надо действовать быстрее!"
    img 8959
    with fade
    melanie "..."

    # Дик с Мелани выходят и идут мимо Виктории. Виктория смотрит зло.
    # Дик говорит: Виктория, я вынужден уехать по срочному делу. Отвечай всем что меня нельзя беспокоить!
    # Да, Мистер Дик, я поняла (зло щурится)
    # Мелани идет улыбаясь.

    img black_screen
    with fadelong
    sound snd_door_close1
    pause 1.0
    music Groove2_85
    img 8960
    with fadelong
    dick "Виктория, я вынужден уехать по срочному делу."
    "Отвечай всем что меня нельзя беспокоить!"
    img 8961
    dick_secretary "Да, Мистер Дик, я поняла..."
    img 8962
    with fade
    melanie "..."
    music Villainous_Treachery
    img 8963
    dick_secretary "..."
    dick_secretary "!!!"
    dick_secretary "!!!!!!"

    return
