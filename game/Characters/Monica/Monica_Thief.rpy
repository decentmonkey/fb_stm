label monica_gas_station_thief:
    call monica_gas_station_thief_dialogue2() from _call_monica_gas_station_thief_dialogue2
    return

label monica_gas_station_thief_dialogue1:
    if monicaEatedLastDay < day:
        #Моника заходит на заправку (голодная)
        mt "На этой заправке продается еда."
        "Если я буду осторожна, то могу украсть какое-нибудь пирожное..."
        "Но стоит-ли мне рисковать?"
        return
    else:
        #Моника заходит на заправку (сытая)
        mt "Что я здесь делаю?"
        mt "Есть я пока не хочу, а говорить с этой кассиршей мне не о чем..."
    return
label monica_gas_station_thief_dialogue2a:
    menu:
        "Купить продукты.":
            if money <= 0:
                mt "У меня нет денег на это..."
                return
            call ep23_dialogues4_1() from _call_ep23_dialogues4_1
            return
        "Уйти.":
            return
    return

label monica_gas_station_thief_dialogue2:
    menu:
        "Купить продукты.":
            if money <= 0:
                mt "У меня нет денег на это..."
                return
            call ep23_dialogues4_1() from _call_ep23_dialogues4_1_1
            return
        "Украсть еду.":
            pass
        "Не делать этого.":
            mt "Я не стану рисковать..."
            return

    #Моника ворует еду
    if monicaEatedLastDay == day:
        mt "Я не так уж голодна."
        "Не стоит лишний раз рисковать..."
        return
    $ store_music()
    music Hidden_Agenda
    #render
    img 7072
    with fade
    w
    img 7073
    w
    img 7074
    mt "Думаю не будет ничего страшного если я украду одно пирожное..."
    img 7075
    w

    #вариации (случайно)
    $ gasStationThiefImages = ["7076", "7077", "7078"]
    $ images = random.sample(set(gasStationThiefImages), 1)
    img images[0]
    $ add_corruption(monicaThiefCorruptionAmount, "stole_food_gas_station_day" + str(day))
    "Я заслужила его за все то что пережила..."

    $ monicaStoleFoodGasStationAmount +=1
    $ monicaStoleFoodTotal +=1
    call monicaEat() from _call_monicaEat_2
    $ restore_music()
    call change_scene("street_gas_station", "Fade_long", "snd_gulp") from _call_change_scene_60
    return
