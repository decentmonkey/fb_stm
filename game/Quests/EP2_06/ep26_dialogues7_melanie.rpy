default ep26_dialogues7_melanie1_flag1 = False

label ep26_dialogues7_melanie1:

# Моника подходит к Мелани в гримерной (первый раз)
# Мелани сидит за гримерным столиком
    menu:
        "Мелани, ты вернулась?":
            $ ep26_dialogues7_melanie1_flag1 = True
            music Groove2_85
            img 20485
            with fadelong
            m "Мелани, ты вернулась?"
            img 20486
            with diss
            m "Где ты так долго была? Что с тобой случилось?"
            music Master_Disorder
            img 20487
            with fade
            melanie "Миссис Бакфетт, это Вы?"
            music Groove2_85
            img 20488
            with fade
            m "Да, Мелани, это Я!"
            m "И я ждала тебя все это время!"
            img 20489
            with diss
            m "Почему тебя так долго не было?!"
            m "Я уже думала что Маркус забрал тебя!"
            music Master_Disorder
            img 20490
            with fade
            melanie "Миссис Бакфетт, я не понимаю о чем Вы говорите..."
            music Groove2_85
            img 20491
            with fade
            m "Что значит ты не понимаешь, Мелани?"
            m "Я говорю про твой визит к Маркусу!"
            img 20492
            with diss
            m "Ты должна была решить с ним вопрос по поводу меня!"
            m "Но, вместо этого, ты куда-то пропала!"
            music Master_Disorder
            img 20493
            with fade
            melanie "Мэм, Я не знаю о чем и о ком Вы говорите..."
            music Pyro_Flow
            img 20494
            with fade
            m "Ты что, играешь со мной, Мелани?!"
            m "Ты прекрасно знаешь что я говорю о Маркусе!"
            # Мелани отворачивается
            music stop
            img black_screen
            with diss
            pause 2.0
            music Master_Disorder
            img 20495
            with fadelong
            melanie "Мэм, я не знаю кто это..."
            img 20496
            with diss
            melanie "Миссис Бакфетт, я очень занята. Пожалуйста, не отвлекайте меня..."

            img black_screen
            with diss
            pause 2.0
            music Groove2_85
            img 20497
            with fade
            mt "Она не хочет говорить про Маркуса..."
            mt "Она что, обманула меня и не ходила к нему?!"

            $ monicaOfficeMakeupRoomSkipMusicOneTime = True
            $ questHelp("melanie_7", True)
            $ questHelp("melanie_7a", skipIfExists=True)

        "Посмотреть на Мелани." if ep26_dialogues7_melanie1_flag1 == True:
            music stop
            img black_screen
            with fadelong
            music Malicious
            pause 1.0
            img 20498
            show screen vignette_screen
            with fadelong
            m "У меня странное чувство..."
            img 20499
            with Dissolve(1.0)
            m "Мелани?"
            img 20500
            with Dissolve(1.0)
            m "Мелани!"
            # убирает волосы
            img 20501
            with Dissolve(1.0)
            m "Что там? Что там такое?"
            img 20502
            with Dissolve(1.0)
            w
            music Villainous_Treachery
            img 20503
            with Dissolve(1.0)
            with hpunch
            w
            img 20504
            with hpunch
            m "О БОЖЕ!"
            sound snd_woman_scream1a
            img 20505
            with diss
            m "НЕТ!"
            hide screen vignette_screen
            img 20506
            with fade
            melanie "Миссис Бакфетт, я просила Вас не беспокоить меня."
            img 20507
            with diss
            m "!!!"
#            music stop
            img black_screen
            with diss
            pause 2.0
            $ melanieMonicaSawFarmTattoo = True
            $ monicaOfficeMakeupRoomSkipMusicOneTime = True
            return True

            img black_screen
            with Dissolve(2.0)
            call textonblack_long(t_("Узнайте что случилось с Мелани в продолжении игры...")) from _call_textonblack_long_2
            img black_screen
            with Dissolve(2.0)
    #    "Мелани, сучка, ты что, никуда не ходила?! (next update) (disabled)":
    #        pass
#        "Мелани, пожалуйста, для меня это очень важно! (next update) (disabled)":
#            pass
        "Уйти.":
            img black_screen
            with diss
            return

    return






























#
