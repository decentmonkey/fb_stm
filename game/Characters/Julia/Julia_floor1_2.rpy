label julia_interact3(obj_name, obj_data):
    if juliaPunished == True or juliaPunishedLow == True or juliaPunishedVoluntarily == True or juliaPunishedNone == True or juliaMonicaForgivenessAfterPunishment == True:
        jump floor1_monica_julia_revenge_interact
    if obj_data["action"] == "l":
        img 1029
        mt "А вот и Юлия.
        Она работает у меня гувернанткой."

        img 1030
        mt "Она из бедной семьи.
        Старается работать, но немного туповата."

        img 1031
        "Постоянно что-то путает и не туда кладет.
        Ее можно научить делать все как надо, но мне лень этим заниматься"
        return
    if monicaEated == True:
        if juliaMonicaYell == False and juliaPunished == False:
#            imgr Dial_Governess1 #4254
            $ imageName = "4254" + day_suffix
            img imageName

        if juliaMonicaYell == True and juliaPunished == False:
#            imgr Dial_Governess1
            $ imageName = "4255" + day_suffix
            img imageName

        if juliaPunished == True:
#            imgr Dial_Governess2
            $ imageName = "4256" + day_suffix
            img imageName

        julia "Миссис Бакфетт.
        Вы уже кушали недавно."

        "Вам подать снова?"

        menu:
            "Не надо, продолжай работу.":
                julia "Конечно, Миссис Бакфетт."

            "Похвалить Юлию за вкусную еду." if juliaPraiseOnOccasion == True:
                m "Ты готовишь довольно вкусно, Юлия."
                julia "Спасибо, Миссис Бакфетт!"
                call bitch(-5, "juliaPraiseOnOccasion") from _call_bitch_22


    return


label floor1_no_julia:
    $ remove_objective("find_julia")
    if juliaMonicaYell == False:
        imgc Monica_HomeCloth1_Thinking1
        m "Юлии нигде нет."
        "Придется искать платье самой?"

    else:
        imgc Monica_HomeCloth1_Angry1
        m "Этой служанки нет ни наверху, ни внизу."

        m "Вопрос..."

        "ГДЕ ЭТА СУЧКА???"

        "ЮЛИЯ!!!!"

        "ТЫ ГДЕ, МЕЛКАЯ СУЧКА???"

        "ЮЛИЯ!!!!"

        "..."

        "Ее нет.
        Ааааргх!"

        "Надо поискать самой.
        Возможно она перепутала шкаф."

        "А может комнату."

        imgc Monica_HomeCloth1_Angry2
        "Или работу (злобно ухмыляется)."

    imgc Monica_HomeCloth1_Thinking1
    m "Что же мне делать?"

    "Может остаться дома полежать в постели?"

    "Но нет, мне надо в фитнес зал, да и в Офисе были дела.
    Еще я обещала Дику встретиться с ним в неформальной обстановке."

    "Дик - это мой персональный юрист-адвокат.
    Он уже давно упрашивает меня о встрече.
    Мне даже немного жаль беднягу."

    "Может стоит сходить в подвал?
    Там бассейн, а за ним прачечная.
    Возможно платье там."

    "Я там никогда не бываю."

    "Попробую заглянуть."

    call miniMapRemoveDisabled("Basement") from _call_miniMapRemoveDisabled

    $ add_objective("laundry_find_dress", t_("Отыскать в прачечной свое платье"), c_blue, 20)
    $ businessClothSearchDressInProgress = True
    $ notWantToBasement = False
    return
