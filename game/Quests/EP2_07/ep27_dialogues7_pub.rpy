# Появляется диалог поговорить о повышении
# Только если Эшли или Джо уровень 2
default ep27_dialogues7ReturnedMoneyCount = 0
label ep27_dialogues7_pub1:
#    menu:
#        "Спросить о повышении.":
#            pass
# Моника спрашивает, можно-ли ее повысить, чтобы она зарабатывала какие-то деньги?
    music2 pub_noise1_low
    music Groove2_85
    img 20953
    with fadelong
    m "Эшли..."
    m "Можно-ли попросить дать мне еще другую работу, чтобы я..."
    m "Чтобы я зарабатывала какие-то деньги здесь?"
# Далее:
# Если ур у Эшли и Джо < 1
    if char_info["Bartender_Waitress"]["level"] < 2 and char_info["Bartender"]["level"] < 2:
        img 20954
        with fade
        ashley "Хммм..."
        ashley "Если честно, я не уверена в тебе [monica_pub_name]."
        ashley "Поработай пока посудомойкой!"
        img 20955
        with diss
        m "!!!"
        help "Требуется отношение с Джо, либо Эшли выше 1."
        return False

# Если у Эшли ур.1, то она говорит что не уверена в ней, но Джо отзывается о ней хорошо (показан хитрый Джо)
    if char_info["Bartender_Waitress"]["level"] < 2:
        img 20956
        with fade
        ashley "Хммм..."
        ashley "Если честно, я не уверена в тебе [monica_pub_name]."
        ashley "Но Джо отзывается хорошо о тебе."
        joe "..." # хитрый
    else:
    # Если у Эшли ур.2, то она говорит что уже успела разглядеть ее попку
        img 20957
        with fade
        ashley "Хммм..."
        ashley "Если честно, то я уже успела разглядеть твою попку, [monica_pub_name]."

# И, пока она работает, никто не пришел проверять ее из миграционной полиции или санитарного контроля.
# Также после ее мытья посуды не отравился ни один клиент.
# И Эшли было бы интересно посмотреть на ее голую попку, которая будет крутиться на пилоне.
# Поэтому она разрешает ей танцевать здесь, но трахаться с клиентами пока нельзя, хотя я знаю что ты за этим пришла сюда.
    img 20958
    with diss
    ashley "И, пока ты работаешь, никто не пришел проверять тебя из миграционной полиции или санитарного контроля."
    img 20959
    with diss
    m "..."
    img 20960
    with fade
    ashley "Также, после твоего мытья посуды не отравился ни один клиент."
    music Loved_Up
    img 20961
    with diss
    ashley "Так что мне было бы интересно посмотреть на твою голую попку, которая будет крутиться на пилоне."
    ashley "Поэтому, так уж и быть."
    ashley "Я разрешаю тебе танцевать здесь..."

    music Groove2_85
    img 20962
    with fade
    ashley "Но трахаться с клиентами пока нельзя!"
    ashley "Хотя я знаю что ты за этим пришла сюда."
# Моника в шоке. Отвечает что не собирается танцевать здесь в голом виде!
# Эшли удивленно спрашивает а что же она тогда хочет? О каком повышении говорит?
# Джо говорит что видишь Эшли, она приличная девушка, пусть она работает у нас официанткой!
# Эшли спрашивает у Джо что ты решил отдать мою работу Мэрилин?
    music Power_Bots_Loop
    img 20963
    with vpunch
    m "!!!"
    m "Я не собираюсь танцевать здесь в голом виде!"
    music Groove2_85
    img 20964
    with fade
    ashley "А что же ты тогда хочешь?"
    ashley "О каком повышении ты говоришь?"
    joe "Видишь, Эшли? [monica_pub_name] приличная девушка."
    joe "Пусть она работает у нас официанткой!"
    music Power_Bots_Loop
    img 20965
    with diss
    ashley "Джо, ты что, решил отдать мою работу [monica_pub_name]?!"
# Может быть ты на ней женишься вместо меня, Джо?!
# И будешь сам платить кредиты за это заведение?!
# Джо улыбается. Нет, Эшли, я не это имел ввиду.
# У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов, правда, Мерилин?
    img 20966
    with diss
    ashley "Может быть ты на ней женишься вместо меня, Джо?!"
    ashley "И будешь сам платить кредиты за это заведение?!"
    img 20967
    with fade
    joe "Нет, Эшли! Я не это имел ввиду!"
    joe "У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов."
    music Hidden_Agenda
    img 20968
    with diss
    joe "Правда, [monica_pub_name]?"

# Моника кривится
# Уверен, что обладательнице такой попки будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!
# Она ведь работает у нас неофициально! Скажем, отдавать ей 10 процентов от того что ей дадут клиенты.
# И ей необязательно платить основную зарплату, ей вполне хватит остатка от чаевых.
# Ведь так, Мэрилин?
    img 20969
    with diss
    mt "!!!" # Моника кривится
    img 20970
    with fade
    joe "Уверен, что обладательнице такой фигуры будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!"
    img 20971
    with hpunch
    mt "ЧТО?!"
    img 20972
    with fade
    joe "Она ведь работает у нас неофициально!"
    joe "Можно, скажем, отдавать ей 30 процентов от того, что ей дадут клиенты."
    joe "И нам необязательно платить ей основную зарплату."
    joe "Ей вполне хватит остатка от чаевых."
    img 20973
    with diss
    joe "Ведь так, [monica_pub_name]?"
# Моника кривится
# А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару.
# Эшли задумалась. Т.е., Джо, ты предлагаешь отправить Мэрилин к этим пьяницам и не платить ей деньги?
# Платить, но только 10 процентов от чаевых. Мы ничем не рискуем, Эшли! Нет зарплаты - не нужны документы!
# Эшли спрашивает: а если она нагрубит клиенту? Или заберет чаевые себе?
# Джо говорит что Мэрилин выглядит как порядочная девушка и не будет брать себе лишнего!
# Эшли спрашивает у Моники: Мэрилин, и ты согласна на такую работу?
    img 20974
    m "!!!" # Моника кривится
    img 20975
    with fade
    joe "А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару."
    music Groove2_85
    img 20976
    with fade
    ashley "..."
    ashley "То есть, Джо, ты предлагаешь отправить [monica_pub_name] к этим пьяницам и не платить ей деньги?"
    img 20977
    joe "Платить, но только 30 процентов от чаевых. Мы ничем не рискуем, Эшли!"
    joe "Нет зарплаты - не нужны документы! Не страшны никакие проверки!"
    img 20978
    with diss
    ashley "А если [monica_pub_name] нагрубит клиенту?"
    ashley "Или заберет чаевые себе?"
    img 20979
    m "!!!"
    img 20980
    with fade
    joe "[monica_pub_name] выглядит как порядочная девушка и не будет брать себе лишнего."
    img 20981
    with diss
    ashley "..."
    ashley "Ну, не знаю..."
    img 20982
    with diss
    ashley "[monica_pub_name], и ты согласна на такую работу?"

# Выбор:
# Я не согласна работать за такие копейки!
# Моника говорит что не согласна работать за такие копейки. (уходя)
# Джо говорит что если надумает, то пусть приходит
    menu:
        "Я не согласна работать за такие копейки!":
            music Power_Bots_Loop
            img 20983
            with fade
            m "Я не согласна работать за такие копейки!"
            img 20984
            with diss
            joe "[monica_pub_name], если надумаешь, то приходи." # подмигивает
            return -1
        "Согласиться.":
            pass
# Согласиться.
# Моника говорит что согласна работать, ей нужна хоть какая-то работа.
# Что не будет грубить клиентам, будет общаться с ними вежливо.
# И что будет отдавать чаевые им.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 20985
    with fadelong
    m "Я..."
    m "Я согласна работать. Мне нужна хоть какая-то работа."
    m "Я обещаю что не буду грубить клиентам, а буду обращаться с ними вежливо."
    img 20986
    with diss
    ashley "..."
    img 20987
    with diss
    m "И буду отдавать чаевые Вам..."
# Эшли говорит что хорошо, ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!
# Здесь не бордель! И она не потерпит официантку, которая будет вести себя как шлюха!
# Моника отвечает что Эшли может не беспокоиться, она не будет выходить за рамки рабочих обязанностей.
    music Groove2_85
    img 20988
    with fade
    ashley "Ну хорошо. Ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!"
    ashley "Здесь не бордель!"
    ashley "И я не потерплю официантку, которая будет вести себя как шлюха!"
    img 20989
    with diss
    m "Эшли, Вы можете не беспокоиться."
    m "Я не буду выходить за рамки рабочих обязанностей."
# Моника думает что ей с трудом вериться что она вообще ведет такой диалог!
# Она, Моника Бакфетт! И говорит такие слова!
# Утешает только то, что ее считают здесь Мерилин, а это значит она в этом месте не имеет ничего общего с Моникой Бакфетт.
# Иначе, она не смогла бы согласиться на такое.
    music RnB3_65
    img 20990
    with fade
    mt "О БОЖЕ!"
    mt "Мне с трудом вериться в то что я вообще такое говорю!"
    mt "Я! Моника Бакфетт!"
    mt "И говорю такие слова!"
    img 20991
    with diss
    mt "..."
    mt "Утешает только то, что меня здесь считают [monica_pub_name]."
    mt "А это значит, что в этом месте я не имею ничего общего с Моникой Бакфетт."
    mt "Но мне не стоит забывать кто Я!"
    mt "В конце концов, мне еще предстоит долгая жизнь, когда я верну свое положение назад..."
#
# Эшли говорит Мэрилин, чтобы та одевала рабочую униформу и шла работать.
#
    music Groove2_85
    with vpunch
    ashley "[monica_pub_name], ты меня слышишь?!"
    img 20992
    with fade
    m "А?" # оборачивается
    img 20993
    with diss
    ashley "[monica_pub_name], ты можешь одевать рабочую униформу и идти работать."
    return

#label ep27_dialogues7_pub2:
# Появляется опция меню Работать официанткой.
#    menu:
#        "Работать официанткой в Shiny Hole.":
#            pass

label ep27_dialogues7_pub3:
# Если уже работала
# Моника говорит что уже работала сегодня и больше не может терпеть эти пьяные лица.
    mt "Я уже работала сегодня и больше не могу смотреть на эти пьяные лица!"
    return

label ep27_dialogues7_pub3a:
    mt "Моя смена закончена. Пусть дальше с ними общается Эшли. Это ее уровень!"
    return

label ep27_dialogues7_pub3b:
    mt "Все, хватит!"
    if monica_shiny_hole_queen_day > 0:
        mt "Моя смена закончена. Надо сказать об этом Эшли!"
        return
    if pubMonicaWaitressTips > 0:
        mt "Моя смена закончена. Теперь мне надо отдать чаевые Эшли."
        mt "С другой стороны, мне бы эти чаевые тоже бы не помешали..."
        mt "Мне не очень хочется {c}отдавать их Эшли{/c}..."
    else:
        mt "Моя смена закончена. Мне надо сказать Эшли что у меня нет чаевых за сегодня."
    return

label ep27_dialogues7_pub4:
#
# Если не работала сегодня, то подходит и говорит что пришла работать официанткой.
# Эшли говорит чтобы Моника шла и переодевалась в униформу и шла работать.
# Эшли уже надоело работать самой. Для этого есть Мерилин.
# Моника злится
    music2 pub_noise1_low
    music Groove2_85
    img 20994
    with fadelong
    m "Эшли..."
    ashley "..."
    m "Я пришла работать официанткой."
    ashley "Хорошо, [monica_pub_name]."
    ashley "Иди переодевайся в униформу и иди работать."
    ashley "Мне уже надоело работать самой."
    ashley "Для этого есть ты, [monica_pub_name]!"
    mt "Меня бесит эта женщина..."
    return

label ep27_dialogues7_pub5:
# Моника закончила работать
# Моника говорит что хватит с нее. Она больше не может терпеть эти пьяные лица.
    mt "Все, с меня хватит!"
    mt "Я больше не могу терпеть эти пьяные лица!"
    return

label ep27_dialogues7_pub6:
# Моника может уйти. Тогда идет выбор уйти без того что отдала чаевые. Если да, то уходит.
# Если нет, то остается.
    menu:
        "Уйти и не отдавать чаевые хозяевам бара.":
            if monica_shiny_hole_queen_day > 0:
                mt "Я теперь королева Shiny Hole и мне не надо отдавать чаевые."
                mt "Но, все-же, лучше сказать Эшли что я ухожу"
                return True
            return False
        "Остаться.":
            return True
    return

label ep27_dialogues7_pub6a:
    mt "Я не собираюсь отдавать никому мои чаевые!"
    return False


label ep27_dialogues7_pub7:
# При клике на барменов, Моника говорит что закончила работу и вот чаевые.
# Эшли дает ей 10 процентов и говорит приходить работать еще.
    music2 pub_noise1_low
    music Groove2_85
    img 20995
    with fadelong
    m "Эшли, я закончила работу."
    if monica_shiny_hole_queen_day > 0: # Если Моника королева
        if pubMonicaWaitressTips == 0:
            m "Мне никто не дал чевых сегодня..."
        else:
            $ add_money(-pubMonicaWaitressTips)
            m "Я заработала $ [pubMonicaWaitressTips]"
        img 20996
        with diss
        ashley "[monica_pub_name], ты теперь королева Shiny Hole..."
        $ add_money(pubMonicaWaitressTips)

        ashley "И тебе полагается не отдавать мне процент от заработка."
        imgd 20995
        ashley "Но не забывай про свои королевские обязанности..."
        ashley "Завтра приходи работать еще."
        return


    if pubMonicaWaitressTips == 0:
        m "Мне никто не дал чевых сегодня..."
    else:
        $ add_money(-pubMonicaWaitressTips)
        m "Вот чаевые, которые я смогла получить..."

    # если есть чаевые
        img 20996
        with diss
        $ tipsBack = round_down(float(pubMonicaWaitressTips)*pubMonicaWaitressTipsKoeff, 0.05)
        if tipsBack == 0.0:
            $ tipsBack = 0.05
        $ add_money(tipsBack)
        ashley "Хорошо. Вот твои тридцать процентов."
        ashley "Завтра приходи работать еще."
        $ questHelp("shinyhole_19", True)

    # если нет чаевых
#    img 20995
#    m "Мне никто не дал чевых сегодня..."
    return

label ep27_dialogues7_pub7a:
    menu:
        "Закончить работу.":
            return True
        "Продолжить.":
            return False
    return

label ep27_dialogues7_pub8:
    if pubMonicaWaitressTipsPunishmentTalkStage == 0:
        music2 stop
        music Power_Bots_Loop
    # Если Моника не отдала чаевые, то при клике на барменов, идет диалог:
    # Эшли ругается на Монику за то что та не отдала чаевые.
    # Эшли говорит Джо что она так и знала. Она с самого начала говорила что Мэрилин шлюха, которая ворует деньги.
    # Эшли говорит Монике чтобы та убиралась и что у нее больше нет работы для нее.
        img 20997
        with fadelong
        ashley "[monica_pub_name], я так и знала что ты воровка и шлюха!"
        img 20998
        with hpunch
        m "!!!"
        img 20999
        with fade
        ashley "Джо! Я тебе говорила!"
        ashley "Я тебя предупреждала!"
        ashley "Она украла наши деньги, Джо!"
        img 21000
        with diss
        m "!!!"
        mt "Черт! Мне нужно убедить ее, что я не забирала деньги."
        mt "Только, как это сделать?"
        mt "Эта Эшли все равно мне не поверит."
        mt "..."
        ashley "Что смотришь? Убирайся отсюда!"
        ashley "Здесь больше нет для тебя работы!"
        ashley "И я не буду тебя обслуживать даже за деньги!"

    # Выбор
    # Уйти
    # Попросить снова взять работать
        menu:
            "Попросить снова взять работать в Shiny Hole.":
                mt "Мне нужна эта работа..."
                mt "Может, если я извинюсь, у меня получится с ней договориться?"
                pass
            "Уйти.":
                mt "Я не собираюсь терпеть такое хамское отношение ко мне!"
                mt "С меня хватит!"
                return 0
    # Моника говорит что извиняется, что просто забыла в конце смены отдать деньги.
    # Она готова это сделать и продолжить работать.
    # Эшли спрашивает, сколько чаевых было в тот день.
    # Моника отвечает сколько
    # Эшли говорит что не верит ей. Чаевых было как минимум $ 500, раз она решила не отдавать эти деньги.
    # Моника оправдывается что нет.
    # Эшли говорит что ничего не знает. Либо Моника отдает $ 500, либо пусть идет отрабатывать деньги виляя задницей.
    # А до этого пусть убирается отсюда!
        music Hidden_Agenda
        img 21001
        with fade
        m "Эшли, Джо, я прошу извинить меня."
        m "Я просто очень устала за рабочий день и забыла в конце отдать деньги."
        m "Я готова сделать это сейчас и продолжить работать здесь."
        music Groove2_85
        img 21002
        with diss
        ashley "Сколько чаевых было в тот день?"
        music Hidden_Agenda
        img 21003
        with fade
        if pubMonicaWaitressTips > 0:
            m "В тот день было $ [pubMonicaWaitressTips]."
        else:
        # либо
            m "В тот день не было чаевых."
        music Power_Bots_Loop
        img 21004
        ashley "Я не верю тебе, [monica_pub_name]!"
        ashley "Чаевых было как минимум $ 500, раз ты решила не отдавать их."
        img 21005
        with diss
        m "Нет, столько не было!"
        m "Клянусь!"
        m "Такой суммы просто не могло быть..."
        mt "В этой дыре!!!"
        img 21006
        with fade
        ashley "Меня не волнуют твои оправдания, [monica_pub_name]."
        if ep29_quests_pub_forgiveness_dancing_enabled == True:
            ashley "Либо ты отдаешь эти $ 500 наличными, либо иди отрабатывать эти деньги, виляя своей задницей на сцене."
            img 21007
            m "!!!"
            img 21008
            with diss
            w
            img 21000
            with fade
            ashley "А иначе убирайся отсюда!"
        else:
            img 21000
            ashley "Ты отдашь эти $ 500 наличными."
            ashley "А иначе убирайся отсюда!"

# После этого появляется выбор при клике на барменов
# -Отдать $ 500
# Моника отдает деньги Эшли
# Эшли говорит что так уж и быть, теперь ты можешь снова работать, но не испытывай моего терпения!
# -Идти танцевать на сцену (в следующей версии игры)
# -Попросить прощения по другому...
    $ menu_price = [500]
    if pubMonicaWaitressTipsPunishmentTalkStage == 0 and pubMonicaWaitressTipsPunishmentTalkStage == 0 and ep29_quests_pub_forgiveness_dancing_enabled == True:
        $ menu_corruption = [0, monicaForgivenessDancingAgreeCorruption]
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
        "Идти танцевать на сцену" if ep29_quests_pub_forgiveness_dancing_enabled == True and pubMonicaWaitressTipsPunishmentTalkStage == 0:
            return 5
        "Попросить прощения у Джо." if obj_name == "Bartender" and pubMonicaWaitressTipsPunishmentTalkStage == 1:
            return 3
        "Попросить прощения у Эшли." if obj_name == "Bartender_Waitress" and pubMonicaWaitressTipsPunishmentTalkStage == 1:
            return 4
        "Попросить прощения по другому..." if pubMonicaWaitressTipsPunishmentTalkStage == 0:
            return 2
        "Уйти.":
            return 0
    return


label ep27_dialogues7_pub9:
# Если подходит к Джо:
# Моника говорит что у нее нет таких денег и она бы не хотела танцевать голой у всех на виду.
# Может быть есть еще какие-то варианты.
# Джо отвечает, что есть один вариант попросить прощения. Джо подмигивает
# Моника напряженно смотрит
# Джо говорит Мэрилин, чтобы она дождалась пока Эшли отвернется и шла в подсобку за Джо
    music Hidden_Agenda
    img 21011
    with fadelong
    m "Джо... У меня нет таких денег."
    m "И я бы..."
    m "Я бы не хотела танцевать голой у всех на виду..."
    m "Может быть есть еще какие-то варианты?"
    music Loved_Up
    img 21012
    with diss
    joe "Вообще-то, [monica_pub_name], есть один вариант попросить прощения."  # Джо подмигивает
    img 21013
    with diss
    m "..." # Моника напряженно смотрит
    img 21014
    with fade
    joe "[monica_pub_name], если хочешь, чтобы тебя простили, дождись пока Эшли отвернется"
    joe "И иди в служебную комнату за мной."

# Выбор:
# Подождать пока Эшли отвернется и идти в подсобку за Джо
# Уйти
    menu:
        "Подождать пока Эшли отвернется и идти в подсобку за Джо.": #corruption
            pass
#        "Подождать пока Эшли отвернется и идти в подсобку за Джо. (в следующем обновлении) (diabled)":
#            pass
        "Уйти.":
            return False

    return True

label ep27_dialogues7_pub9a:
    menu:
        "Прощение у Джо 1" if pubMonicaWaitressTipsPunishmentJoeStage >= 0:
            return 1
        "Прощение у Джо 2" if pubMonicaWaitressTipsPunishmentJoeStage >= 1:
            return 2
        "Прощение у Джо 3" if pubMonicaWaitressTipsPunishmentJoeStage >= 2:
            return 3
        "Прощение у Джо 4" if pubMonicaWaitressTipsPunishmentJoeStage >= 3:
            return 4
#        "Прощение у Джо 5" if pubMonicaWaitressTipsPunishmentJoeStage >= 4:
#            return 5
    return

label ep27_dialogues7_pub10:
# Если идет, вызывается меню со сценами с Джо (открываются последовательно)
# Сцена1:
# Трогает зад
# Джо
    music Loved_Up
    img 21027
    with fadelong
    joe "О, [monica_pub_name], ты пришла!"
    m "Да, Джо, я пришла."
    music Groove2_85
    img 21028
    with diss
    joe "Тебя точно не видела Эшли?"
    joe "Не видела как ты сюда заходила?"
    img 21029
    with diss
    m "Нет, Джо."
    m "Меня не видела Эшли."
    m "Но она может придти сюда в любой момент."
    img 21030
    with fade
    joe "Нет, [monica_pub_name], она не придет."
    joe "Пока меня нет, она не оставит бар без присмотра."
    joe "У нас здесь, знаешь-ли, такие клиенты... хе-хе."
    img 21031
    m "Я знаю какие здесь клиенты, Джо..."
    img 21032
    joe "..."
    music Hidden_Agenda
    img 21033
    with fade
    m "Джо, я готова еще раз извиниться за то что не отдала деньги."
    m "Я правда забыла и..."
    music Loved_Up
    sound Jump1
    img 21034
    with diss
    joe "[monica_pub_name], хватит про эти деньги."
    joe "Мне не нужны эти деньги, я хочу тебя, [monica_pub_name]!"
    joe "Я хочу твою попку, [monica_pub_name]!"
    music Power_Bots_Loop
    img 21035
    with hpunch
    m "Джо, это исключено!"
    m "У тебя есть жена, которая прямо за стенкой!"
    m "Да, я хочу работать здесь, но я не собираюсь за это спать с таким жирным толстяком, как ты, Джо!"
    music Loved_Up
    img 21036
    with fade
    joe "[monica_pub_name], очень жаль."
    img 21037
    with diss
    joe "Но повернись, хотя бы, своей попой."
    joe "Покажи ее мне!"
    img 21038
    with diss
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            m "Нет, Джо!"
            return False
    music Groove2_85
    img 21039
    with fade
    m "И на этом все, ты сделаешь так, чтобы Эшли простила меня!"
    img 21040
    with diss
    joe "Хорошо, [monica_pub_name]."
    joe "Повернись своей попой, скорее!"
    music Hidden_Agenda
    img 21041
    with fade
    m "..."
    mt "Дьявол, мне не хочется делать этого!"
    mt "С другой стороны, в этом нет ничего страшного и это позволит мне снова работать здесь..."
    mt "Мне нужны деньги..."
    img 21042
    with diss
    m "..."
    joe "Я жду!"
    # Моника показывает зад
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 21043
    with fadelong
    w
    img 21044
    with diss
    w
    sound Jump1
    img 21045
    with diss
    w
    img 21046
    with diss
    joe "!!!"
    music Groove2_85
    img 21047
    with fade
    m "Все? Достаточно?"
    sound Jump1
    img 21048
    with diss
    joe "[monica_pub_name], я должен потрогать твою попу!"
    joe "Она такая сладкая! Я хочу этого, [monica_pub_name]!"
    music Power_Bots_Loop
    img 21049
    with hpunch
    m "Нет!"
    music Groove2_85
    img 21050
    with fade
    joe "Я потрогаю ее и обещаю что Эшли простит тебя!"
    music Hidden_Agenda
    img 21051
    with diss
    mt "Черт! Что же мне делать?"
    mt "Мне нужна эта работа. Я могу здесь заработать хотя бы на еду..."
    mt "Но неужели я соглашусь на то, чтобы какой-то толстяк в трущобах лапал меня?!"
    $ menu_corruption = [monicaTipsPunishmentScene1AssCorruption]
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21049
            m "Нет, Джо!"
            return False
    music Groove2_85
    img 21052
    with fade
    m "Ладно, но только в одежде!"
    m "И я не буду отдавать те чаевые, которые взяла себе!"
    music Loved_Up
    img 21053
    with diss
    joe "Хорошо, [monica_pub_name]!"
    joe "Можешь оставить эти деньги себе!"
    music stop
    img black_screen
    with diss
    pause 1.5
    # трогает
    music Loved_Up
    img 21054
    with fadelong
    joe "Ахххх!"
    joe "Как я мечтал об этом!"
    sound Jump1
    img 21055
    with diss
    joe "Я стал мечтать об этом с первой минуты, когда увидел тебя здесь, [monica_pub_name]!"

    img 21056
    with diss
    w
    sound Jump2
    img 21057
    with diss
    w
    stop music
    play music "Sounds/audio_Monica_Joe_Ass_1.mp3"
    scene black
    image videov_Monica_Joe_Ass_1_1 = Movie(play="video/v_Monica_Joe_Ass_1_1.mkv", fps=30)
    show videov_Monica_Joe_Ass_1_1
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    music Groove2_85
    img 21058
    with fade
    mt "Очередной озабоченный мерзавец!"

    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Ass_1.mp3"
    scene black
    image videov_Monica_Joe_Ass_1_2 = Movie(play="video/v_Monica_Joe_Ass_1_2.mkv", fps=30)
    show videov_Monica_Joe_Ass_1_2
    with fadelong
    wclean
    stop music
    music stop

    music Loved_Up2
    img 21059
    with diss
    joe "Ах, твоя попка!"
    img 21060
    with diss
    joe "Она такая упругая!"
    img 21061
    with diss
    joe "Ах!"
    music Groove2_85
    img 21062
    with fade
    m "Ну все, хватит!"
    m "Идем к Эшли!"
    return

label ep27_dialogues7_pub11:
# Трогает голую грудь
    music Loved_Up
    img 21063
    with fadelong
    joe "[monica_pub_name], ты пришла!"
    joe "Я хочу посмотреть твою грудь!"
    joe "Я хочу увидеть ее!"
    music Groove2_85
    img 21064
    with hpunch
    m "Нет!"
    img 21065
    with fade
    joe "Мне жаль, [monica_pub_name], но Эшли начнет что-то подозревать."
    joe "Это большой риск для меня."
    img 21066
    with diss
    mt "Дьявол! Снова я в такой глупой ситуации!"
    mt "Настолько-ли мне нужна эта дурацкая работа?!"
    $ menu_corruption = [monicaTipsPunishmentScene2ShowBoobsCorruption]
    menu:
        "Согласиться показать грудь.": #corruption
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21064
            with fade
            m "Нет, Джо!"
            return False

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21067 # звук одежды
    with fadelong
    m "Ладно..."
    m "Только быстро..."
    # Моника снимает верх
    sound Jump1
    img 21068
    with fadelong
    joe "Ах! Какие сиськи!"
    img 21069
    with diss
    joe "Тебе определенно надо танцевать на сцене, [monica_pub_name]!"
    mt "!!!"
    img 21070
    with diss
    joe "Можно я потрогаю их?"
    m "Нет, Джо! Мы договорились!"
    music Groove2_85
    img 21071
    with fade
    joe "Я не могу так, не могу, [monica_pub_name]!"
    joe "Дай я только прикоснусь к ним и Эшли простит тебя, я обещаю!"
    music Hidden_Agenda
    img 21072
    with diss
    mt "Я не могу пойти на это!"
    mt "..."
    mt "Хотя... Он не знает кто я на самом деле..."
    $ menu_corruption = [monicaTipsPunishmentScene2TouchBoobsCorruption]
    menu:
        "Согласиться.": #corruption
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21071
            with fade
            m "Нет, Джо!"
            return False
    music Groove2_85
    img 21073
    with fade
    m "Ты прикоснешься к моей груди буквально на секунду."
    joe "Да, [monica_pub_name], я обещаю!"
    img 21074
    with diss
    m "И больше никаких условий после этого."
    m "Обещаешь?!"
    joe "Да, [monica_pub_name], я обещаю!"
    music Hidden_Agenda
    img 21075
    with fadelong
    mt "Дьявол!"
    mt "Мое изысканное тело создано для того, чтобы быть на обложке модного журнала..."
    mt "До чего я докатилась, О БОЖЕ!"
    img 21076
    with diss
    mt "Хотя... Это не Я... Это [monica_pub_name]..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 21077
    with fadelong
    w
    # джо трогает грудь
    sound Jump2
    img 21078
    with diss
    joe "Ах, какие сиськи!"
    img 21079
    with diss
    joe "Вот это да!"
    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Boobs_1.mp3"
    scene black
    image videov_Monica_Joe_Boobs_1_1 = Movie(play="video/v_Monica_Joe_Boobs_1_1.mkv", fps=30)
    show videov_Monica_Joe_Boobs_1_1
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up2

    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21082
    with diss
    w

    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Boobs_1.mp3"
    scene black
    image videov_Monica_Joe_Boobs_1_2 = Movie(play="video/v_Monica_Joe_Boobs_1_2.mkv", fps=30)
    show videov_Monica_Joe_Boobs_1_2
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up2

    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21085
    with diss
    joe "Лучшие сиськи в shiny hole!"

    music Power_Bots_Loop
    img 21086
    with fade
    m "Все, Джо!"
    m "Хватит!"
    m "Идем к Эшли!"
    return

label ep27_dialogues7_pub12:
# Просит посмотреть на ее обалденную попку
    music Loved_Up
    img 21087
    with fadelong
    joe "[monica_pub_name], я хочу увидеть твою попку!"
    m "!!!"
    img 21088
    with diss
    m "Ладно..."
    # Моника поворачивается задом
    img 21089
    with diss
    w
    img 21090
    with diss
    w
    img 21091
    with diss
    w
    music Groove2_85
    img 21092
    with hpunch
    joe "Нет, [monica_pub_name], я хочу увидеть твою попку голой!"
    joe "Покажи ее мне и я сделаю так, чтобы Эшли снова простила тебя!"
    music Hidden_Agenda
    img 21093
    with diss
    m "Джо, может быть, можно как-то без этого?"
    music Groove2_85
    img 21094
    with fade
    joe "Нет, [monica_pub_name], я действительно хочу увидеть твою попку."
    joe "Это мое самое большое желание сейчас!"
    joe "И, пока оно не исполнится, я не смогу ничего сделать с Эшли."
    music Hidden_Agenda
    img 21095
    with diss
    mt "Что же мне делать?"
    mt "Может быть лучше достать $ 500? Но как?!"
    $ menu_corruption = [monicaTipsPunishmentScene3ShowNakedAssCorruption]
    menu:
        "Показать Джо свою голую попу.": #corruption
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21094
            with fade
            m "Нет, Джо!"
            return False
    music Groove2_85
    img 21096
    with fade
    m "Джо, но только никаких прикосновений, тебе ясно?!"
    joe "Конечно, [monica_pub_name], я только посмотрю!"
    img 21097
    with diss
    m "И никаких дополнительных условий, ясно?!"
    joe "Да, [monica_pub_name], я обещаю!"
    music Hidden_Agenda
    img 21098
    with fade
    mt "Дьявол!"
    mt "Мне так стыдно делать это..."
    mt "Показывать свой голый зад в какой-то shiny hole посреди трущоб..."
    mt "Это какой-то сон..."
    music Groove2_85
    img 21099
    with diss
    joe "[monica_pub_name], я жду!"
    img 21100
    with diss
    joe "Скорее, показывай свою попку!"
    img 21101
    with diss
    m "!!!"
    # Моника показывает голую попу
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21102
    with fadelong
    w
    img 21103
    with diss
    w
    img 21104
    with diss
    joe "Ах, какая попка!"
    img 21105
    with diss
    joe "Давно я не видел такой идеальной формы!"
    music Groove2_85
    img 21106
    with fade
    mt "Ты этого недостоин, толстяк! Смотреть на мое восхитительное тело!"

    music Loved_Up2
    sound Jump1
    img 21107 #jump
    with diss
    w
    img 21108
    with diss
    joe "[monica_pub_name], почему ты не показала мне ее сразу, как только пришла?"

    img 21109
    with diss
    joe "Я бы сразу взял тебя официанткой. Без необходимости мыть посуду!"
    img 21110
    with fade
    mt "Это он думает что оказал бы мне честь?! Сразу бы дал работать официанткой в этой дыре?!"
    mt "Мне?! Монике Бакфетт?!"
    sound Jump2
    img 21111
    with vpunch
    joe "[monica_pub_name], можно потрогать?!"
    # Моника одевается
    music Power_Bots_Loop
    img 21112
    with diss
    m "Только попробуй, Джо!"
    m "И я сломаю тебе пальцы!"
    music Groove2_85
    img 21113
    with fade
    joe "Но [monica_pub_name]! Мы ведь только начали!"
    joe "Признайся, ты ведь для этого и пришла сюда, в Shiny Hole."
    joe "Чтобы показывать свое тело за деньги!"
    joe "Просто ты не хочешь торопиться с этим."
    joe "Хочешь сначала освоиться здесь."
    joe "Я тебя понимаю, [monica_pub_name]."
    joe "Все девочки, которые танцуют на сцене, сначала стеснялись."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 21114
    with fadelong
    m "Все, Джо!"
    m "Хватит!"
    img 21115
    with diss
    m "Идем к Эшли!"
    return

label ep27_dialogues7_pub13:
# Просит раздеться и забраться на стол
    music Groove2_85
    img 21116
    with fadelong
    joe "[monica_pub_name], ты уже украла столько денег..."
    joe "И Эшли уже начинает что-то подозревать."
    img 21117
    with diss
    joe "Обычно... Знаешь..."
    joe "Больше денег я люблю только шлюх..."
    joe "И Эшли знает об этом и очень ревнует."
    music Power_Bots_Loop
    img 21118
    with vpunch
    mt "Я не шлюха!!!"
    music Groove2_85
    img 21119
    with fade
    joe "Если честно, она так следит за мной, что уже очень давно я не видел другой голой женщины."
    m "И что же ты хочешь на этот раз, Джо?"
    joe "Я хочу чтобы ты разделась, [monica_pub_name]."
    joe "Полностью."
    img 21120
    with diss
    m "Это исключено, Джо!"
    img 21121
    with diss
    joe "Тогда извини, для меня это слишком большой риск."
    joe "Ты можешь идти. Если Эшли догадается, она прибьет меня."
    menu:
        "Уйти.":
            music Power_Bots_Loop
            img 21122
            with fade
            m "Твоя жена тоже может быть голой женщиной, Джо!"
            m "Смотри лучше на нее!"
            return False
        "Предложить компромисс.":
            pass

    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 21123
    with fadelong
    m "Джо..."
    m "Мне действительно надо снова работать здесь."
    m "Может быть мне не надо раздеваться полностью?"
    music Groove2_85
    img 21124
    with fadelong
    joe "Хорошо, [monica_pub_name]."
    joe "Ты можешь раздеться наполовину и встать на этот стол."
    joe "И принять пару сексуальных поз."
    mt "!!!"
    img 21125
    with diss
    joe "Это будет как приватный танец."
    music Hidden_Agenda
    img 21126
    with fadelong
    m "Ладно, Джо..."
    m "Сейчас я сниму верх..."
    music Groove2_85
    img 21127
    with diss
    joe "Нет, [monica_pub_name]!"
    joe "Я хочу чтобы ты сняла низ!"
    music Power_Bots_Loop
    img 21128
    with hpunch
    m "ЧТОООО?!"
    music Groove2_85
    img 21129
    with fade
    joe "[monica_pub_name], твоя грудь прекрасна!"
    joe "Но от твоей попки я просто без ума!"
    joe "Это мое условие!"
    joe "Если ты не согласна, то можешь идти и искать $ 500!"
    img 21130
    with diss
    m "!!!"
    $ menu_corruption = [monicaTipsPunishmentScene4DanceNakedCorruption]
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21128
            with fade
            m "Нет, Джо!"
            return False
    music Hidden_Agenda
    img 21131
    with fade
    mt "Дьявол!"
    mt "До чего ты докатилась, Моника!"
    mt "..."
    mt "Мне не стоит даже в мыслях называть себя Моникой..."
    mt "Вдруг я проговорюсь..."
    mt "Ведь меня здесь знают под именем [monica_pub_name]..."
    img 21132
    with diss
    mt "Черт! Мо... [monica_pub_name]!"
    mt "Закрой глаза и сделай это..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    # Моника снимает низ и залезает на стол
    music Groove2_85
    img 21133
    with fadelong
    mt "Ненавижу этого Джо!"
    mt "На что мне приходится идти ради этой дурацкой работы!"
    img 21134
    with diss
    mt "Как могло дойти до такого?"
    mt "Не могу поверить..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Molten_Alloy
#    music RocknRoll_loop
    img 21135
    with fadelong
    sound heel1
    $ add_corruption(10, "joe_punishment_scene4a")
    # звук каблука
    w
    img 21136
    with diss
    w
    img 21137
    with fade
    sound heel1
    joe "О да, [monica_pub_name]!"
    img 21138
    with diss
    joe "Покажи мне свою попу, Да!"
    img 21139
    with fade
    joe "Давай, меняй позы! Развлеки малыша Джо!"
    img 21140
    with fade
    joe "Вот так! Активнее виляй своей задницей, [monica_pub_name]!"
    img 21141
    with diss
    joe "Вот так! Теперь повернись, ДА!"
    img 21142
    with fade
    joe "Да! Запомни! Клиент должен хорошо рассмотреть твою задницу, [monica_pub_name]!"
    joe "Тогда ты получишь больше чаевых!"
#    music stop
    img 21143
    with diss
    $ add_corruption(10, "joe_punishment_scene4b")
    joe "Стоп! Вот так, замри!"
    # достает член
    img 21144
#    with fade
    sound jump1
    # jump
    w
#    music Molten_Alloy
    img 21145
    with diss
    joe "Можешь продолжать!"
    joe "Положи руки на задницу."
    img 21146
    with diss
    $ add_corruption(10, "joe_punishment_scene4c")
    joe "Вот так!"
    img 21147
    with fade
    joe "Давай, [monica_pub_name], двигайся поактивнее!"
    joe "Зарабатывай на чай!"
    m "Джо, хватит грязных комментариев!"
    m "Я и так не знаю как согласилась на это!"
    img 21148
    with diss
    joe "Да, [monica_pub_name]! У тебя лучшая задница, которую я видел в Shiny Hole!"
    img 21149
    with diss
    joe "Да, выгнись посильнее, да!"
    joe "Твоя задница ослепительная!"
    img 21150
    with diss
    joe "Ни у одной из наших девочек нет таких идеальных форм!"
    img 21151
    with diss
    joe "Эта задница должна сиять в Shiny Hole!"
    joe "[monica_pub_name], ты станешь звездой!"
    m "Нет, Джо!"
    m "Я никогда не буду танцевать голой на публике!"
    sound snd_masturbation1
    img 21152
    with diss
    joe "Продолжай! Поближе! Я... Я почти все..."
    img 21153
    with fade
    joe "Но как же! Ты должна танцевать!"
    joe "За такую задницу дадут... дадут..."
    joe "Аххх!"
    $ add_corruption(10, "joe_punishment_scene4d")
    img 21154
    with diss
    joe "Дадут 20... 50..."
    img 21155
    with diss
    joe "Нет, даже 100 долларов! Сто!"
    img 21156
    with diss
    m "Сколько?! 100 долларов?!"
    m "Ты шутишь, Джо?!"
    img 21157
    with diss
    joe "Может... Ах.... Может не столько..."
    joe "Но 20 долларов за такую задницу дадут точно, [monica_pub_name]!"
    joe "Это хорошие деньги... Аххххх!"

    music Groove2_85
    img 21158
    with fadelong
    m "Все, мне надоело кривляться!"
    joe "Аааааххх!"

    music Power_Bots_Loop
    img 21159
    with hpunch
    m "ЧТО?!"
    m "Ты там что, дрочишь на меня, Джо?!"
    sound snd_masturbation1
    img 21160
    with diss
    joe "Ааааххх! Ааааааааххх!"
    joe "Еще чуть-чуть!"
    music Groove2_85
    img 21161
    with fade
    m "Дьявол!!!"
    m "Все, шоу закончено!"
    m "Иди к Эшли, немедленно!"
    m "Мне нужна эта работа!"
    mt "Извращенец!!!"

    music Power_Bots_Loop
    img 21162
    with fade
    joe "Что?! Кто-то идет?"
    img 21163
    with diss
    joe "Это Эшли! Прячься!"
    mt "О БОЖЕ!"
    music stop
    img black_screen
    with diss
    sound snd_bodyfall
    pause 1.5
    music Groove2_85
    img 21164 #Моника прячется
    with fadelong
    w
    img 21165
    with fade
    ashley "Джо! Вот ты где!"
    ashley "Что ты здесь делаешь, дармоед?!"
    music Power_Bots_Loop
    img 21166
    with diss
    mt "Как я вляпалась!"
    mt "Я здесь, без трусов, прячусь за диваном!"
    mt "От жены хозяина какой-то дыры в трущобах!"
    mt "Моника! Как до такого могло дойти?!"
    mt "Что ты сделала не так, чтобы такое произошло?! ЧТО?!"
    music Groove2_85
    img 21167
    with fade
    ashley "Я что, должна одна целый день обслуживать пьяниц?!"
    ashley "Эта шлюха, [monica_pub_name], больше не работает здесь! Ты забыл?!"

    img 21168
    with diss
    joe "Эшли! Я просто устал, решил отдохнуть..."
    sound snd_kick_fred1
    img 21169
    with fade
    ashley "Никакого отдыха! Быстро работать!"
    img 21170
    with fadelong
    ashley "Зачем я только вышла замуж за такого растяпу!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21171
    with fadelong
    m "!!!"
    mt "Хорошо что Эшли не заметила мою одежду. Мне надо незаметно выбраться отсюда..."
    return


label ep27_dialogues7_pub14:
# Затем Джо говорит Эшли что та самая красивая и любимая и что он поговорил с Мэрилин и ей кажется надо дать ей еще шанс.
# Что он ручается за нее. Эшли тает и говорит что так уж и быть.
# Говорит Монике что та снова может работать, но чтобы не испытывала ее терпения.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 21018
    with fadelong
    joe "Эшли, ты моя самая красивая и любимая жена!"
    img 21019
    with diss
    ashley "И, Джо? Что тебе снова понадобилось от меня?"
    img 21018
    with fade
    joe "Я поговорил с [monica_pub_name] и, мне кажется, надо дать ей еще шанс."
    joe "Я ручаюсь за нее, Эшли."
    joe "И..."
    sound Jump1
    img 21020
    with vpunch
    joe "И я тебя очень сильно люблю..."
    # обнимает
    sound kiss2
    img 21021
    with diss
    ashley "Ох, Джо..."
    img 21022
    with diss
    ashley "Ну ладно... Хорошо..."
    # поворачивается к Монике
    music Groove2_85
    img 21023
    with fade
    ashley "[monica_pub_name], ты можешь снова работать."
    ashley "Но не испытывай моего терпения!"
    img 21026
    with diss
    mt "!!!"
    return

label ep27_dialogues7_pub14a:
# Если подходит к Эшли:
# Моника говорит что у нее нет таких денег и она бы не хотела танцевать голой у всех на виду.
# Может быть есть еще какие-то варианты.
# Эшли отвечает, что для такой аппетитной попки у нее есть один вариант.
# Моника напряженно смотрит
# Эшли говорит Мэрилин, чтобы она дождалась пока Джо отвернется и шла в подсобку за Эшли
    music Hidden_Agenda
    img 21015
    with fadelong
    m "Эшли... У меня нет таких денег."
    m "И я бы..."
    m "Я бы не хотела танцевать голой у всех на виду..."
    m "Может быть есть еще какие-то варианты?"
    img 21016
    with diss
    ashley "Вообще-то, [monica_pub_name], у обладательницы такой раскошной попки есть один вариант попросить прощения у меня."  # подмигивает
    img 21013
    with diss
    m "..." # Моника напряженно смотрит
    img 21017
    with fade
    ashley "[monica_pub_name], если хочешь, чтобы тебя простили, дождись пока Джо будет занят"
    ashley "И иди в служебную комнату за мной."

# Выбор:
# Подождать пока Джо отвернется и идти в подсобку за Эшли
# Уйти
# Если идет, вызывается меню со сценами с Эшли (открываются последовательно)
    menu:
        "Подождать пока Джо будет занят и идти в подсобку за Эшли.":
            pass
#        "Подождать пока Джо будет занят и идти в подсобку за Эшли. (в следующем обновлении) (diabled)":
#            pass
        "Уйти.":
            return False
    return True

label ep27_dialogues7_pub14b:
    menu:
        "Прощение у Эшли 1" if pubMonicaWaitressTipsPunishmentAshleyStage >= 0:
            return 1
        "Прощение у Эшли 2" if pubMonicaWaitressTipsPunishmentAshleyStage >= 1:
            return 2
        "Прощение у Эшли 3" if pubMonicaWaitressTipsPunishmentAshleyStage >= 2:
            return 3
#        "Прощение у Эшли 4" if pubMonicaWaitressTipsPunishmentAshleyStage >= 3:
#            return 4
#        "Прощение у Эшли 5" if pubMonicaWaitressTipsPunishmentAshleyStage >= 4:
#            return 5
    return


label ep27_dialogues7_pub15:
# Эшли
# Просит поцеловаться (хватает Монику за зад, под джинсы)
    music Groove2_85
    img 21172
    with fadelong
    m "Я пришла, Эшли..."

    music Loved_Up
    img 21173
    with diss
    ashley "О, [monica_pub_name]!"
    sound Jump1
    img 21174 # jump
    with diss
    ashley "Иди ко мне!"
    ashley "Я ждала когда ты что-нибудь натворишь..."
    img 21175
    with diss
    ashley "Иди ко мне! Иди я поцелую тебя!"
    img 21176
    with diss
    $ menu_corruption = [monicaTipsPunishmentAshleyScene1KissingCorruption]
    menu:
        "Позволить Эшли поцеловать себя.": #corruption
            pass
        "Отказать.":
            music Power_Bots_Loop
            img 21177
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return False
#    music Loved_Up
    # Эшли целует Монику
    sound snd_longkiss1
    img 21178
    with fade
    ashley "Ммммм..."
    sound snd_longkiss1
    img 21179
    with fade
    mt "!!!"


    music audio_longkiss1
    scene black
    image videov_Monica_Ashley_Kiss_1_1 = Movie(play="video/v_Monica_Ashley_Kiss_1_1.mkv", fps=30)
    show videov_Monica_Ashley_Kiss_1_1
    with fadelong
    wclean

    stop music
    music Loved_Up
    sound snd_longkiss1
    img 21180
    with diss
    ashley "Ммммм... Моя конфетка... Мммммм..."
    # Эшли пропускает руку Монике под джинсы сзади
    sound snd_longkiss1
    img 21181
    with fade
    w
    music Loved_Up2
    sound Jump2
    img 21182
    with diss
    #sound
    w
    sound snd_longkiss1
    img 21183
    with diss
    mt "!!!"

    music2 audio_longkiss1
    scene black
    image videov_Monica_Ashley_Kiss_1_1 = Movie(play="video/v_Monica_Ashley_Kiss_1_1.mkv", fps=30)
    show videov_Monica_Ashley_Kiss_1_1
    with fadelong
    wclean

    music2 stop
#    music Loved_Up2
    img 21184
    with diss
    ashley "Ах, эта сладкая попка... Мммммм..."
    img 21185
    with diss
    ashley "Какая она упругая... Мммммм...."
    # Моника отстраняется
    music Groove2_85
    img 21186
    with fadelong
    m "Эшли, пожалуйста, хватит!"
    img 21187
    with diss
    ashley "[monica_pub_name], ты получила прощение на этот раз..."
    ashley "Я подожду, пока ты снова что-нибудь не напроказничаешь..."
    img 21188
    mt "!!!"
    return

label ep27_dialogues7_pub16:
    music Groove2_85
    img 21189
    with fadelong
    m "Я пришла, Эшли..."
    music Loved_Up
    img 21190
    with diss
    ashley "О, [monica_pub_name]!"
    ashley "Иди ко мне!"
    ashley "Дай я потрогаю твою киску!"
    $ menu_corruption = [monicaTipsPunishmentAshleyScene2PussyTouchigCorruption]
    menu:
        "Позволить Эшли потрогать свою киску.": #corruption
            pass
        "Отказать.":
            music Power_Bots_Loop
            img 21189
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return False
    music Groove2_85
    img 21191
    with fade
    mt "О Боже!"
    mt "Что эта Эшли собралась делать?!"
    # Эшли запускает руку Монике в джинсы и трогает киску
    music Loved_Up
    sound Jump1
    img 21192
    with fade
    ashley "Да, [monica_pub_name]!"
    ashley "Чувствуешь меня?"
    sound audio_Monica_Cabinet_FaceSitting_3
    img 21193
    with diss
    m "Ахххх!"
    img 21194
    with diss
    w
    ashley "Наслаждаешься этим?"
    img 21195
    with diss
    m "Ахххх!"
    music Loved_Up2
    sound audio_Monica_Cabinet_Dildo_3
    img 21196
    with diss
    w
    img 21197
    with diss
    w
    ashley "Почуствуй меня, [monica_pub_name]!"
    img 21198
    with diss
    ashley "Если захочешь, это можно сделать по другому."
    img 21199
    with diss
    m "ААА! Ааааахх!"
    img 21200
    with diss
    ashley "Ах, какая ты вкусная, [monica_pub_name]!"

    music2 stop
    # Моника отстраняется
    music Groove2_85
    img 21201
    with vpunch
    m "Погоди, Эшли!"
    m "Я..."
    m "На меня что-то начинает накатывать..."
    m "Погоди, я боюсь этого..."
    music Loved_Up
    img 21202
    with fade
    ashley "Это оргазм, моя [monica_pub_name]."
    ashley "Ты разве не любишь это?"
    img 21203
    with diss
    m "Я... Я не совсем знаю что это такое и..."
    img 21204
    with fade
    ashley "Ах, иди ко мне, [monica_pub_name], я тебе покажу!"
    music Groove2_85
    img 21205
    with diss
    m "Нет, Эшли! Мне..."
    m "Мне надо идти!"
    return

# Засовывает руку Монике спереди в джинсы, и трогает там, что-то говоря, какая Мерилин вкусная. Моника ахает и еле сдерживается.
# Просит Мэрилин спустить ее джинсы, чтобы посмотреть на ее попку, затем задирает юбку и просит потереться своей попой о Мэрилин

label ep27_dialogues7_pub17:
    music Groove2_85
    img 21206
    with fadelong
    m "Эшли, я пришла."
    m "Только пожалуйста, давай ты не будешь трогать мою киску..."
    m "По крайней мере не в этот раз..."
    music Loved_Up
    img 21207
    with diss
    ashley "Хорошо, [monica_pub_name]."
    ashley "Снимай свой низ, я хочу потереться о твою сладкую попку!"
    menu:
        "Сделать то о чем просит Эшли.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21206
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return False
    sound snd_fabric1
    img 21208
    with fadelong
    m "Эшли, и что будет дальше?"
    img 21209
    with diss
    ashley "Не бойся, [monica_pub_name], снимай!"
    sound snd_fabric1
    img 21210
    with fadelong
    m "Ладно..."
    m "А ты мне точно разрешишь снова работать здесь?"
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    # Моника снимает низ
    img 21211
    with fadelong
    # Эшли поднимает юбку
    ashley "Потрись о мою попку своей и я прощу тебя!"
    music Power_Bots_Loop
    img 21212
    with hpunch
    m "ЧТО??!"
    music Loved_Up
    img 21213
    with fadelong
    ashley "Давай, [monica_pub_name]!"
    ashley "Я хочу почувствовать твою сладкую попку!"
    img 21214
    with diss
    ashley "Иначе я тебя не прощу!"
    $ menu_corruption = [monicaTipsPunishmentAshleyScene3AssToAssCorruption]
    menu:
        "Сделать то о чем просит Эшли.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21213
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return False

    # Моника трется своей попой о попу Эшли.

    img 21215
    with fade
    ashley "Ну же, [monica_pub_name]!"
    img 21216
    with diss
    ashley "Я не чувствую твою попку! Где она?"
    img 21217
    with diss
    ashley "Не будет твоей попки - не будет прощения!"
    music Groove2_85
    img 21218
    with fadelong
    w
    img 21219
    with fade
    mt "О БОЖЕ! Что я делаю?!"
    music Loved_Up2
    sound hlup10
    img 21220
    with diss
    ashley "Да, [monica_pub_name]!"
    sound hlup25
    img 21221
    with diss
    ashley "Какая у тебя упругая и приятная попка!"
    ashley "Это просто персик!"
    img 21222
    with diss
    mt "!!!"
    sound hlup25
    img 21223
    with diss
    ashley "Ах! Как здорово!"
    sound hlup10
    img 21224
    with diss
    ashley "Ах! Ах! Да!"
    sound hlup10
    img 21225
    with diss
    w
    sound hlup19
    img 21226
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    ashley "Дааааааа!!!" # Эшли кончает
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 21227
    with fadelong
    ashley "Ты отлично справилась, [monica_pub_name]."
    ashley "Но, если при клиентах ты будешь такой же шлюхой, какой была сейчас, я тебя уволю."
    img 21228
    mt "Я не шлюха!!!"
    return

label ep27_dialogues7_pub18:
# Эшли говорит Джо что подумала и решила дать Мэрилин еще один шанс
# Говорит Монике что та может снова работать, но чтобы не испытывала ее терпения.
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 21024
    with fadelong
    ashley "Джо, я подумала и решила дать [monica_pub_name] еще один шанс."
    joe "Правда, Эшли? Рад это слышать!"
    img 21025
    with diss
    ashley "[monica_pub_name], ты можешь снова работать."
    ashley "Но не испытывай моего терпения, иначе ты снова будешь наказана." # Подмигивает
    img 21026
    with diss
    mt "!!!"
    return



label ep27_dialogues7_pub19:
    mt "Я уже обслуживала этого посетителя..."
    return
























#
