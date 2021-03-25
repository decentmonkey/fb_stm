default monicaEscortClientHotel1 = False  # Моника согласилась пойти с клиентом в номер
default monicaEscortClientHotel2 = False  # Моника согласилась пососать палец клиента
default monicaEscortClientHotel3 = False  # Моника согласилась дрочить перед клиентом
default monicaEscortClientHotel4 = False  # выбор сцены 1 с клиентом в отеле
default monicaEscortClientHotel5 = False  # выбор сцены 2 с клиентом на выезде
default monicaEscortClientHotel6 = False  # выбор пункта "Ждать клиента."
default monicaEscortClientHotel7 = False # выбор сцены3
default monicaEscortClientHotel8 = False # выбор сцены4
default monicaEscortClientHotel9 = False # выбор сцены5
default monicaEscortClientHotel10 = False # месть (смена ролей)

#call ep211_escort_scene1_1a() # меню выбора, когда приходит на работу в эскорт (сцена, ждать клиента или уйти)
#call ep211_escort_scene1_1() # ресторан, Моника сидит за столиком, приходит клиент
#call ep211_escort_scene1_2() # ресепшн, разговор с администратором
#call ep211_escort_scene1_2_1() # служебный коридор, Моника переодевается в нижнее белье
#call ep211_escort_scene1_3() # возле лифта, Моника с клиентом
#call ep211_escort_scene1_4() # номер в отеле, секс с клиентом
#call ep211_escort_scene1_5() # ресепшн, разговор с администраторшей после обслуживания клиента
#call ep211_escort_scene1_6() # ресепшн, мысли Моники, если хочет уйти, не отдав денег администраторше
#call ep211_escort_scene1_7() # мысли Моники возле отеля после того, как обслужила клиента
#call ep211_escort_scene1_8() # мысли Моники возле отеля, если отказалась обслуживать клиента


# Моника приходит в эскорт на работу, выбор ивент (доступен раз в неделю) или ждать клиента
# если ивент, то одна из двух сцен работают (доступен повтор этих сцен)
label ep211_escort_scene1_1a:
    # после регулярного диалога с администраторшей (лейбл ep210_dialogues7_escort_hotel_8a) возникает меню
    mt "Что мне делать дальше?"
    mt "..."
label ep211_escort_scene1_1a_loop1:
    menu:
        "Встреча с клиентом (сцена)." if math.floor(monicaEscortSceneDay/7)<math.floor(day/7):
            menu:
                "Клиент в номере отеля.":
                    # запускается сцена 1 с клиентом в отеле, начиная с лейбла ep211_escort_scene1_1 (если в первый раз)
                    # при повторном выборе начинается с лейбла ep211_escort_scene1_3 (перед лифтом + сцена)
                    $ monicaEscortClientHotel4 = True # выбор сцены 1 с клиентом в отеле
                    return 1
                "Выезд к клиенту." if monicaEscortScenesCount > 0:
                    # запускается сцена 2 - выезд к клиенту, начиная с лейбла ep211_escort_scene2_1 (если в первый раз)
                    # при повторном выборе начинается с лейбла ep211_escort_scene2_3 (служ. коридор + выезд)
                    $ monicaEscortClientHotel5 = True # выбор сцены 2 с клиентом на выезде
                    return 2
                "Провинившийся завсегдатай." if monicaEscortClientHotel5 == True:
                    $ monicaEscortClientHotel7 = True
                    return 3
                "Реквизит отеля." if monicaEscortClientHotel7 == True:
                    $ monicaEscortClientHotel9 = True
                    return 5
                "Обслуживание персонала." if monicaEscortClientHotel9 == True and monicaHotelStaffEscort2 == True:
                    $ monicaEscortClientHotel8 = True
                    return 4
                "Смена ролей." if monicaEscortClientHotel8 == True and monicaEscortClientHotel9 == True:
                    $ monicaEscortClientHotel10 = True
                    return 6
#                "Отношения в коллективе (Начало)." if ep215_quests_escort_completed_day > 0 and monicaEscortRevengeGirl2 == True:
                "Отношения в коллективе (Начало)." if monicaEscortRevengeGirl2 == True and monicaEscortClientHotel10 == True:
                    return 7
                "Назад.":
                    jump ep211_escort_scene1_1a_loop1
            return
        "Встреча с клиентом (на следующей неделе) (disabled)" if math.floor(monicaEscortSceneDay/7)==math.floor(day/7):
            pass
        "Ждать клиента за столиком.":
            # Моника нерешительно
            mt "Что ж... Надеюсь, [monica_hotel_name] повезет сегодня с клиентом..."
            $ monicaEscortClientHotel6 = True # выбор пункта "Ждать клиента."
            menu:
                "Просто ждать.":
                    return -1
                "Пытаться привлечь внимание. (в следующих обновлениях) (disabled)":
                    pass
                "Кастинг в номерах. (в следующих обновлениях) (disabled)":
                    pass
                "Назад.":
                    jump ep211_escort_scene1_1a_loop1
            return
        "Уйти отсюда!":
            mt "Нет! Я не буду заниматься этим!!!"
            mt "Я Моника Бакфетт! Я никогда не опущусь до подобной грязи!"
            mt "!!!"
            # Моника уходит
            return False
    return


# сцена 1
# Моника сидит за столиком в ожидании клиента
label ep211_escort_scene1_1:
    music Poppers_and_Prosecco
    img 30076
    with fadelong
    w
    img 30077
    with fade
    mt "Так, Моника. Соберись!"
    mt "Не надо так нервничать."
    mt "Ты в любой момент можешь послать всех к черту и уйти."
    # к столику подходит полный мужчина, очкарик. в приличном костюме. с виду интеллигентный интеллигент
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    img 30078
    with fade
    client "Добрый вечер, Мисс."
    client "Я Вас раньше здесь не видел. Как вас зовут?"
    img 30079
    with diss
    m "Добрый вечер, Мистер."
    m "Меня зовут [monica_hotel_name]."
    img 30080
    with fade
    client "[monica_hotel_name]. Какое прекрасное имя. Как и его обладательница."
    client "Я очень рад, что сегодня проведу вечер с Вами, [monica_hotel_name]."
    # Моника смотрит на него, размышляя
    music Groove2_85
    img 30081
    with diss
    mt "Хмм... Разговаривает вежливо, выглядит вполне прилично."
    mt "Думаю, от него не стоит ожидать никаких извращений..."
    music Poppers_and_Prosecco
    img 30082
    with fade
    client "Позволите мне сразу пригласить Вас в номер, [monica_hotel_name]?"
    img 30083
    with diss
    mt "..."
    menu:
        "Уйти отсюда!":
            # Моника нерешительно
            music Groove2_85
            img 30084
            with fade
            mt "Нет! Я не могу это сделать!"
            img 30086
            with diss
            m "Я..."
            m "Я не смогу с Вами пойти..."
            img 30087
            with fade
            m "Я... Я не работаю здесь!"
            m "Я просто зашла поесть в ресторан..."
            img 30088
            with diss
            client "О, извините, Мисс."
            client "Наверное, я перепутал столик."
            # Моника встает и уходит
            return False
        "Пойти в номер с клиентом.":
            $ monicaEscortClientHotel1 = True # Моника согласилась пойти с клиентом в номер
            pass
    music Groove2_85
    img 30084
    with fade
    mt "Это же совсем нестрашно."
    mt "Это просто обычный неудачник."
    mt "Наверное, приходит сюда раз в месяц в день зарплаты. Фи!"
    mt "Что-то пойдет не так - я просто уйду отсюда."
    mt "Хммм..."
    img 30085
    with diss
    mt "Они мне тогда сказали, что будут давать мне заказы..."
    mt "Только с проблемными клиентами."
    mt "..."
    mt "Мне нужно сказать этой никчемной администраторше, что у меня клиент."
    mt "Может, она скажет, что с ним не так."
    # Моника смотрит на клиента
    img 30086
    with fade
    m "Да, мы можем пойти в номер."
    m "Только мне нужно отойти на пару минут."
    img 30078
    with diss
    client "Конечно, [monica_hotel_name]."
    client "Я буду ждать тебя {c}у лифта{/c}."
#    $ log1 = t_("Пойти на ресепшн к администратору.")
    return True

# Моника приходит на ресепшн
label ep211_escort_scene1_2:
    music Groove2_85
    img 30089
    with fadelong
    sound highheels_short_walk
    m "У меня клиент. Он зовет пойти с ним в номер..."
    img 30090
    with fade
    reception "Я уже в курсе..."
    reception "Это один из наших постоянных клиентов."
    reception "Девочки не любят работать с ним."
    img 30091
    with diss
    m "Почему?"
    img 30092
    with diss
    mt "Вроде он не похож на извращенца."
    img 30093
    with diss
    reception "У него не встает, но он никак не хочет смириться с этим..."
    reception "Он всегда заказывает девочек и мурыжит их до утра."
    img 30094
    with diss
    reception "Очень хочет кончить..."
    reception "Но, как правило, безрезультатно."
    reception "Потом скандалит и обвиняет девочек в том, что они плохо работают."
    img 30095
    with diss
    mt "!!!"
    img 30096
    with fade
    m "То есть... Если он скажет, что я плохо работаю, то..."
    img 30097
    with diss
    reception "Штраф."
    music Power_Bots_Loop
    img 30098
    with fade
    mt "Вот сучка!"
    music Groove2_85
    img 30099
    with diss
    m "Ты же сама говоришь, что дело в клиенте, а не в девочках!"
    m "Какой еще штраф?!"
    img 30100
    with diss
    reception "Это правило нашего ВИП Эскорта."
    img 30098
    with diss
    mt "Что за бред!!!"
    img 30101
    with diss
    reception "И я переоделась бы на твоем месте..."
    reception "У девочек есть много разной одежды, подходящей для таких случаев."
    reception "Иди в служебный коридор. Поищи там что-нибудь по-сексуальнее."
    m "!!!"
    img 30102
    with diss
    m "Я не собираюсь надевать чье-то чужое белье!"
    m "Как ты себе это представляешь?!"
    music Power_Bots_Loop
    img 30095
    with diss
    mt "Я не буду надевать на свое прекрасное тело белье, которое..."
    mt "Которое носили эти сучки!"
    mt "!!!"
    mt "Они же в этом белье обслуживали клиентов! Фи!"
    music Groove2_85
    img 30103
    with fade
    reception "Ты сейчас же пойдешь и наденешь на себя белье для клиента!"
    reception "Это твоя работа! Я не потерплю подобного отношения к клиентам!"
    reception "У нас ВИП Эскорт с отличной репутацией."
    reception "И все должно быть на высшем уровне."
    img 30105
    with diss
    reception "Если я тебе сказала, что нужно переодеться, значит нужно!"
    reception "Если что-то тебя не устраивает, тогда иди работать в подворотне!"
    reception "Все! Иди переодевайся! Не заставляй клиента ждать тебя!"
    music Power_Bots_Loop
    img 30104
    with diss
    mt "Сучка!"
    mt "!!!"
#    img 30105
    reception "Быстро!"
#    $ log1 = t_("Пойти в служебный коридор и переодеться.")
    return

##############################################
# служебный коридор отеля
label ep211_escort_scene1_2_1:
    # затемнение экрана, прошло 5 мин
    # Моника стоит в служебном коридоре в нижнем черном белье
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Несколько минут спустя...")) from _rcall_textonblack_3
    pause 1.5
    music Power_Bots_Loop
    img 17092
    with fadelong
    mt "Это просто отвратительно!"
    mt "Почему я должна надевать ЭТО?!"
    img 17093
    with fade
    mt "Еще и после того, как эти сучки работали в этой одежде!!!"
    mt "!!!"
    # заходит администраторша
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 17094
    with fadelong
    reception "Что ты здесь делаешь так долго?!"
    reception "Переоделась?"
    reception "Хорошо, клиенту должно понравится."
    img 17095
    with fade
    m "!!!" # Моника зло смотрит на нее
    m "Почему я должна надевать нижнее белье после других девочек?"
    img 17096
    with diss
    reception "А у тебя есть какие-то другие варианты?"
    reception "Может, у тебя есть что-то подобное?"
    m "..."
    img 17097
    with diss
    reception "Нет?"
    reception "Вот и не спорь со мной!"
    reception "Не нравится носить белье девочек, приноси свое белье!"
    music Power_Bots_Loop
    img 17098
    with diss
    mt "!!!"
    music Groove2_85
    img 17099
    with fade
    reception "И вообще... Не понимаю, что тебя не устраивает..."
    reception "Вчера клиенту так понравилось это белье на одной из девочек..."
    reception "Что он оставил ей неплохие чаевые."
    img 17100
    with diss
    mt "Надеюсь, это белье хоть постирали после вчерашнего клиента?! Фу!"
    img 17101
    with diss
    reception "Все. Хватит тут возиться. Иди к клиенту!"
    m "Мне..."
    m "Мне идти в номер прямо в таком виде?"
#    reception "Конечно, ты можешь пойти и в таком виде..."
    img 17102
    with diss
    reception "Возможно ты привыкла ходить в таком виде, работая на улице..."
    m "?!?!?!"
    reception "Но у нас тут приличное заведение!"
#    reception "Но, боюсь, что тебя увидит кто-то из гостей нашего отеля..."
    img 17103
    with diss
    reception "Надевай сверху свое рабочее платье!"
    img 17104
    with diss
    m "И как я буду выглядеть?! Через это платье все видно!"
    img 17105
    with diss
    reception "[monica_hotel_name]!!! Ты испытываешь мое терпение!"
    reception "Сейчас же прекрати со мной спорить!"
    reception "И делай, что Я тебе говорю!"
    music Power_Bots_Loop
    img 17106
    with hpunch
    reception "Быстро оделась и пошла к клиенту!!!"
    reception "Если он уйдет, не дождавшись тебя, ты будешь оштрафована!"
    # админ уходит
    img 17093
    with fade
    mt "Никчемная!"
    mt "Бесполезная!"
    mt "Ненавижу ее!!!"
    mt "!!!"
    # затемнение экрана, прошло 5 мин
    # Моника идет мимо ресепшена в сторону лифта, под платьем видно черное белье с поясом и чулками
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 17107
    with fadelong
    w
    img 17108
    with fade
    reception "Не вздумай в таком виде попасться на глаза другим гостям отеля!"
    reception "Здесь останавливаются приличные люди и нам незачем портить свою репутацию!"
    img 17109
    with diss
    mt "Она еще и комментирует мой внешний вид!"
    mt "Мерзкая сучка!"
    mt "!!!"
#    $ log1 = t_("Пойти к клиенту. Он ждет у лифта.")
    return
##############################################


# Моника с клиентом возле лифтов в отеле
label ep211_escort_scene1_3:
    client "Я Вас уже заждался..."
    client "Мммм, [monica_hotel_name] приготовила для меня что-то интересное?"
    client "Пошлите скорее в номер!"
    client "Мне не терпится посмотреть, что у Вас под платьем..."
    mt "..."
    mt "Так, Моника, соберись!"
    mt "Тебе надо представить, что ты [monica_hotel_name]."
    mt "А не Моника Бакфетт."
    mt "А это просто обычный неудачник."
    mt "Наверное, приходит сюда раз в месяц в день зарплаты. Фи!"
    mt "Что-то пойдет не так - я просто уйду отсюда."
    return False

# Моника с клиентом в номере отеля
label ep211_escort_scene1_4:
    # клиент сидит на кровати, Моника растерянно стоит перед ним
    music stop
    img black_screen
    with diss
    sound snd_lift
    pause 2.0
    music Groove2_85
    img 16765
    with fadelong
    w
    img 16782
    with fade
    sound highheels_short_walk
    w
    img 16766
    with diss
    m "Что мне нужно сделать?"
    img 16767
    with fade
    mt "Дал бы денег просто так и отпустил бы..."
    mt "У меня нет никакого желания делать для него что-то."
    mt "..."
    img 16768
    with diss
    client "Для начала [monica_hotel_name] должна снять платье..."
    img 16769
    with fade
    mt "Моника, не переживай."
    mt "Тебе нечего стесняться. У тебя великолепное тело."
    img 16770
    with diss
    mt "..."
    mt "Он, наверняка, никогда не видел такой красивой женщины, как я."
    # она снимает платье и стоит перед клиентом голая
    # тот ее рассматривает внимательно
    img 16771
    with fade
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 16772
    with fadelong
    w
    img 16773
    with fade
    w
    img 16774
    with diss
    mt "Сейчас он разденется и начнет лапать мое прекрасное тело. Фу!"
    # клиент не раздевается
    img 16775
    with diss
    client "[monica_hotel_name], присаживайтесь рядом со мной."
    # Моника садится на кровать, клиент опускается на колени на пол перед ней
    img 16776
    with fade
    w
    img 16777
    with diss
    client "Если [monica_hotel_name] позволит мне целовать ее ножку..."
    client "Я буду щедр с Мисс."
    # Моника смотрит на него удивленно
    music stop
    img 16778
    with hpunch
    sound plastinka1b
    mt "Он хочет целовать мне ноги?"
    mt "Да еще и платить за это?!"
    mt "?!?!?!"
    music Loved_Up
    img 16779
    with diss
    mt "Он это серьезно?!"
    mt "???"
    mt "Может, я ослышалась?"
    img 16780
    with fade
    m "Мистер, Вы хотите целовать мою ногу?"
    img 16781
    with diss
    client "Да, Мисс. Позвольте Вашу ножку."
    m "..."
    # Моника протягивает ему ногу и он начинает целовать ее, берет пальчики в рот, облизывает
    # Монике приятно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 16783
    with fadelong
    w
    img 16784
    with fade
    sound lick13
    mt "О, как же это..."
    m "Ммммм..."
    img 16785
    with diss
    mt "Это приятно..."
    mt "Черт!"
    img 16786
    with fade
    mt "Он за это еще и денег заплатит?"
    mt "Я готова работать так каждый вечер."
    img 16787
    sound lick10
    with diss
    mt "О, как же приятно..."
    img 16788
    with diss
    w
    # клиент отстраняется от ее ноги
    music stop
    img black_screen
    with diss
    music Loved_Up
    img 16789
    with fadelong
    w
    img 16790
    with fade
    client "А теперь [monica_hotel_name] возьмет мой палец в свой ротик..."
    client "И пососет его..."
    # Моника смотрит удивленно на его руку, он улыбается
    music Groove2_85
    img 16791
    with diss
    mt "???"
    menu:
        "Нет, я не смогу!":
            # Моника нерешительно
            music Groove2_85
            img 16818
            with fade
            mt "Фу! Нет! Я не могу это сделать!"
            mt "Я не хочу облизывать грязные руки этого неудачника!"
            img 16819
            with diss
            m "Я..."
            m "Я не смогу..."
            m "Я... Я не предоставляю такую услугу!"
            img 16820
            with fade
            client "Но, Мисс... Мне сказали, что..."
            img 16821
            with diss
            m "Нет. Я не буду этого делать!"
            # Моника встает и уходит
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            img 16825
            with fade
            sound highheels_short_walk
            return False
        "Сделать, как требует клиент.":
            $ monicaEscortClientHotel2 = True # Моника согласилась пососать палец клиента
            pass
    # Моника с отвращением смотрит на его руку
    music Groove2_85
    img 16792
    with fade
    mt "Это унизительно и..."
    mt "Противно!"
    mt "Но брать в рот его грязный палец!!!"
    mt "!!!"
    mt "Но он сказал, что будет щедр..."
    img 16793
    with diss
    mt "Все же это не какое-то там гадкое извращенство..."
    mt "..."
    mt "Это просто работа, Моника."
    mt "..."
    # Моника с отвращением, но все приближает губы к его руке
    img 16794
    with fade
    mt "Главное, чтобы меня не стошнило прямо на него."
    # она прикасается к его руке губами и берет в рот его палец
    img 16796
    with diss
    w
    img 16795
    with fade
    client "Соси его!"
    img 16797
    with diss
    sound hlup21
    client "Оооооо!!!"
    img 16798
    with diss
    sound drkanje5
    client "Как же приятно! Ещееее!!!"
    # в процессе он другой рукой расстегивает ширинку, достает член и дрочит, пока Моника сосет его палец
    img 16799
    with fade
    client "А теперь, [monica_hotel_name], раздвинь ноги!"
    client "Я хочу посмотреть на твою киску!"
    client "!!!"
    img 16800
    with diss
    mt "Черт!"
    mt "Какой-то мерзкий неудачник сейчас будет пялиться на мою..."
    mt "..."
    mt "Но если я откажу ему, он не заплатит денег."
    img 16801
    with fade
    mt "И будут проблемы с этой никчемной администраторшей..."
    mt "Она говорила, что будет штраф."
    mt "А мне нужны деньги."
    mt "..."
    img 16802
    with diss
    menu:
        "Сделать, как требует клиент.":
            pass
    # клиент продолжает дрочить себе и рассматривает киску Моники
    music Loved_Up
    img 16803
    with fade
    client "О, дааааа!"
    img 16804
    with diss
    w
    img 16805
    with fade
    client "Дрочи!"
    img 16806
    with diss
    sound drkanje5
    m "???"
    client "Я хочу смотреть, как ты ласкаешь себя!"
    client "Ну! Давай же! Ласкай!"
    img 16807
    with diss
    menu:
        "Нет, я не хочу этого делать!":
            # Моника нерешительно
            music Groove2_85
            img 16818
            with fade
            mt "Фу! Нет! Я не хочу!"
            mt "Мне надоело возиться с этим неудачником!"
            mt "!!!"
            img 16819
            with diss
            m "Нет. Я не буду этого делать!"
            # Моника встает и уходит
            music stop
            img black_screen
            with diss
            sound snd_fabric1
            pause 2.0
            music Groove2_85
            img 16825
            with fade
            sound highheels_short_walk
            return False
        "Сделать, как требует клиент.":
            $ monicaEscortClientHotel3 = True # Моника согласилась дрочить перед клиентом
            pass
    music Loved_Up
    img 16808
    with diss
    mt "Надеюсь, ему достаточно будет того, что он посмотрит как я себя трогаю..."
    mt "Лучше так, чем он будет лезть к моей..."
    mt "Ко мне своими грязными пальцами!"
    # Моника прикасается к себе, клиент смотрит
    # клиент дрочит, пока его палец во рту у Моники, и кончает на постель
    music Loved_Up2
    img 16809
    with fade
    w
    img 16810
    with diss
    client "Оооо!!! Я сейчас!!!"
    client "Еще чуть-чуть!!!"
    img 16811
    with fade
    sound drkanje5
    client "Ааааа!!!"
    client "Засунь свой палец себе в дырочку!!!"
    # Моника выполняет требование
    img 16812
    with diss
    sound hlup10
    w
    img 16813
    with diss
    w
    img 16814
    with fade
    sound drkanje5
    client "Давай же!!!"
    img 16815
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    client "ААААААА!!!"
    img 16816
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan9
    # клиент кончает на постель
    img 16817
    with diss
    mt "?!"
    mt "Кончил?"
    # клиент доволен, застегивает штаны
    # Моника молча смотрит на него, вытирается
    music Groove2_85
    img 16822
    with fade
    mt "Этот никчемный неудачник в жизни не видел такой красивой женщины как Я."
    mt "Неудивительно, что с теми сучками из эскорта у него не получалось!"
    mt "!!!"
    music Pyro_Flow
    img 16778
    with diss
    mt "Боже. Моника, ты серьезно сейчас?!"
    mt "Ты гордишься тем, что какой-то мерзкий тип обкончался, глядя на тебя?!"
    img 16823
    with diss
    mt "Ты что, совсем с ума сошла?!"
    mt "Фу!"
    mt "..."
    music Groove2_85
    img 16824
    with fade
    client "Ты самая лучшая девочка здесь, [monica_hotel_name]."
    client "Мне очень понравилось."
    m "..."
    # он встает и оставляет на кровати купюры
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    sound snd_zip
    pause 1.0
    music Groove2_85
    img 16826
    with fadelong
    client "Здесь 700 долларов. Я обязательно приду к тебе еще раз, [monica_hotel_name]." # уходит
    img 16827
    with fade
    sound man_steps
    w
    # Моника смотрит на деньги
    img 16828
    with diss
    mt "700 долларов?!"
    mt "Я заработала 700 долларов, облизывая палец незнакомому мужчине!"
    mt "..."
    $ add_money(700.0)
    img 16767
    with fade
    mt "Меньше всего хочется отдавать половину этой сучке на ресепшене..."
    mt "Может, уйти и больше просто не приходить сюда?"
    mt "Что она мне сделает?"
    img 16770
    with diss
    mt "С другой стороны, здесь я за вечер могу заработать такие большие деньги."
    mt "Вернее, это сущие копейки для меня, но... в моем положении сейчас..."
    mt "Эта сучка больше не пустит меня в ресторан..."
    mt "Нет, мне не стоит пока терять эту возможность заработка."

    $ log1 = t_("Пойти на ресепшн и отдать 50 процентов от заработка администратору.")
    return

# Моника после клиента идет на ресепшен
label ep211_escort_scene1_5:
    # китаянка стоит за стойкой ресепшена
    music Groove2_85
    img 30106
    with fadelong
    sound highheels_short_walk
    w
    $ add_money(-700.0)
    img 30107
    with fade
    m "Клиент заплатил 700 долларов."
    img 30108
    with diss
    reception "И остался доволен."
    reception "Ты хорошо поработала ротиком."
    music stop
    img 30109
    with hpunch
    sound plastinka1b
    mt "!!!"
    music Groove2_85
    img 30110
    with diss
    m "Откуда ты?.."
    img 30111
    with fade
    reception "Я все знаю..."
    reception "Это моя работа!"
    sound vjuh3
    $ add_money(350.0)
    img 30112
    with diss
    reception "Вот твои деньги."
    # отдает ей 350 долларов
    img 30113
    with fade
    reception "Завтра можешь приходить снова."
    reception "На сегодня все."
    reception "Клиенты не любят использованный товар."
    if char_info["ReceptionGirl"]["level"] == 1:
        $ add_char_progress("ReceptionGirl", 25, "ReceptionGirl_escort_scene1")
    img 30114
    with diss
    mt "Вот сучка!"
    mt "Откуда она знает, что я... Работала ртом?!"
    mt "Она подглядывала?!"
    mt "!!!"
    # Моника уходит
    return

# если Моника хочет уйти, не отдавая денег
label ep211_escort_scene1_6:
    music Groove2_85
    img 30115
    with fadelong
    mt "Я пока не могу так рисковать!"
    mt "Эта сучка меня не пустит больше в ресторан, если я не отдам ей 50 процентов."
    mt "А мне не выгодно терять такой заработок."
    mt "Но я обязательно потом что-нибудь придумаю: чтобы не делиться с ней!"
    mt "..."
    return

# в неделю максимальный заработок 5500 баксов
# если заработала 5500 в отеле, то фотосессии и контракт со Стивом недоступны

# Моника, выйдя из отеля после того, как обслужила клиента
label ep211_escort_scene1_7:
    # не рендерить!
    mt "Я сегодня за вечер заработала 350 долларов."
    mt "Неплохой заработок, учитывая мою временную ситуацию."
    mt "Возможно, мне стоит пересилить себя и поработать здесь еще какое-то время."
    mt "Быть может, у меня получится зарабатывать еще больше."
    mt "Мне нужно будет прийти сюда завтра."
    mt "..."
    mt "Я ведь в любой момент смогу отказаться и уйти."
    return

# Моника, выйдя из отеля после того, как отказалась обслуживать клиента
label ep211_escort_scene1_8:
    # не рендерить!
    mt "Я никогда не смогу решиться на такое!"
    mt "Я - Моника Бакфетт, а не какая-то проститутка!"
    return


# если в меню ep211_escort_scene1_1a выбран пункт "Ждать клиента"
# то Монику в процессе ожидания могут вызвать вместе с остальными девочка на кастинг в клиенту
# перед кастингом будет выбор одежды: платье или нижнее белье
# где они стоят в ряд и клиент не знает, кого выбрать.
# клиент просит их показать грудь или попу, например или спрашивает, что вы умеете
# девочки что-нибудь показывают
# при клике на Монику будет выбор стоять прямо или что-нибудь продемонстрировать (демонстрация будет пока недоступна)
# при клике на любую из девочек, та что-нибудь показывает и клиент ее выбирает
# а потом выберет
# не Монику
# чтобы Монику начали выбирать нужно повышать коррапшн

label ep211_escort_scene1_9:
    mt "Не могу поверить что я сижу здесь, за этим-же столом, где ужинала с Диком..."
    mt "Сижу для того, чтобы найти клиента..."
    mt "Какой ужас, Моника!"
    mt "Даже не хочу об этом думать!"
    return

label ep211_escort_scene1_10:
    mt "Я не собираюсь разговаривать ни с кем из них!"
    return

label ep211_escort_scene1_11:
    mt "Эта дура Администратор говорила что мне не стоит афишировать себя вне ресторана."
    mt "Видите-ли здесь живут приличные люди..."
    if monicaBitch == True:
        mt "Ничтожества! Ненавижу!"
    return

label ep211_escort_scene1_12:
    mt "Этот лифт ведет на этажи с номерами отеля..."
    return

label ep211_escort_scene1_13:
    mt "Мне нечего там делать сейчас!"
    mt "Ненавижу это место!"
    return

label ep211_escort_scene1_13a:
    mt "Эта дверь ведет в служебный коридор, где решаются вопросы, связанные с эскортом."
    mt "И проводятся... кастинги..."
    return


label ep211_escort_scene1_14:
    menu:
        "Уйти.":
            return 1
        "Остаться.":
            return 2
        "Меня зовут не [monica_hotel_name]!":
            return 3
    return

# Моника уходит, не работая
label ep211_escort_scene1_15:
    # китаянка стоит за стойкой ресепшена
    music Groove2_85
    img 30106
    with fadelong
    sound highheels_short_walk
    w
    img 30107
    with fade
    m "Я на сегодня закончила работу."
    m "Мне не удалось найти клиента."
    m "Мне нужно идти."
    img 30113
    with diss
    reception "И куда ты собралась в этом платье?"
    reception "Оно для работы в ВИП-эскорте."
    reception "В нем нельзя работать на улице!"
    music Pyro_Flow
    img 30114
    with diss
    mt "!!!"
    mt "Сучка!"
    music Groove2_85
    img 30107
    with fade
    m "Я не собираюсь работать на улице!"
    img 30108
    with diss
    reception "Тогда переодевайся и приходи потом..."
    reception "Нечего занимать просто так место в ресторане!"
    music Pyro_Flow
    img 30115
    with fade
    sound highheels_short_walk
    mt "Никчемная администраторша!"
    mt "!!!"
    return

label ep211_escort_scene1_16:
    mt "Никто ко мне не подошел, дьявол!"
    mt "К черту всех этих неудачников!"
    call change_scene("rich_hotel_reception") from _rcall_change_scene_17
    return

label ep211_escort_scene1_17:
    mt "Мне надо подойти к чертовой администраторше..."
    return False

label ep211_escort_scene1_18:
    mt "Мне надо переодеться..."
    return False
