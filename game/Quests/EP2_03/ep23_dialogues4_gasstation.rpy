# На заправке можно покупать еду.
# Периодически не работает касса.
# Кристина не узнает Монику, на что Моника делает комментарий, что ее никто не узнает в этих лохмотьях.
# По крайней мере хоть что-то хорошее есть в этой одежде.
# Если не работает касса, то Моника думает какую бы трепку сейчас устроила продавщице.
# Если разбивала бутылку, то думает что стоит разбить что-нибудь еще, но сейчас это слишком опасно.

# Еда выбирается из прилавков. Пирожные и гамбургеры.
# Дают разное кол-во еды. (как инвентарь)
# Каждый день еда убавляется (с утра) и обновляется флаг monicaEat()

default gasStationFoodBought = False
default gasStationBuyFoodFirstTime = True
default gasStationComputerNotWorkingDay = 0
default gasStationComputerNotWorkingDayTime = ""

label ep23_dialogues4_1:
    if gasStationFoodInited == False:
        $ add_location("gas_station_buy_food", caption=t_("Gas Station"), label="gas_station_buy_food", init_label="gas_station_buy_food_init", parent="street_gas_station")
        $ gasStationFoodInited = True
    # Моника заходит
    $ gasStationFoodBought = False
    if cloth == "CasualDress1":
        music Groove2_85
        img 11743
        with fade
        m "Я хочу купить продукты!"
        m "И только попробуй сказать мне что у тебя не работает касса, детка!"
        img 11744
        saleswoman "Мэм, касса работает."
        saleswoman "Пожалуйста, скажите, если я смогу чем-то помочь Вам!"

        music Hidden_Agenda
        call change_scene("gas_station_buy_food") from _call_change_scene_247

        return



    if gasStationBuyFoodFirstTime == True and cloth == "Whore":
        # первый раз
        $ gasStationBuyFoodFirstTime = False
        img 9515
        with fade
        saleswoman "Эй! Здесь приличная заправка!"
        "Зачем Вы пришли?"
        if cloth == "Whore":
            img 9516
        mt "Хорошо что она не узнает меня... Единственный плюс этой одежды..."
        #

    if cloth == "Whore":
        img 9517
        with fade
    m "Я хочу купить продукты!"



    #Если касса не работает
    if gasStationBuyFoodFirstTime == True or (gasStationComputerNotWorkingDay == day and gasStationComputerNotWorkingDayTime == day_time) or day%4 == 0:
        $ gasStationComputerNotWorkingDay = day
        $ gasStationComputerNotWorkingDayTime = day_time
#        $ gasStationBuyFoodFirstTime = False



        if cloth == "Whore":
            img 9518
        else:
            img 9519
        saleswoman "У нас не работает касса! Так что попрошу выйти отсюда!"
        if monicaBitch == True:
            if cloth == "Whore":
                img 9520
                with fade
            mt "Сучка!"
            "Эх! Какую-бы я сейчас устроила ей трепку, с огромным удовольствием!"
            mt "Я еще вернусь сюда, когда закончится этот кошмар!"
            #Если разбивала бутылку
            if gasStationSaleswomanMischiefed == True:
                if cloth == "Whore":
                    img 9521
                    with fade
                music Hidden_Agenda
                mt "Может разбить здесь что-нибудь еще?"
                "Проучить эту сучку!"
                "Но нет... Сейчас это слишком опасно!"
        call change_scene("street_gas_station") from _call_change_scene_217
        return
    #


#    $ gasStationBuyFoodFirstTime = False
    if cloth == "Whore":
        img 9522
    else:
        img 9523
    saleswoman "Выбирайте, но учтите, что я слежу, чтобы Вы ни украли ничего!"
    if monicaBitch == True:
        mt "Сучка!"

    music Hidden_Agenda
    call change_scene("gas_station_buy_food") from _call_change_scene_218

    #

    # Если касса работает:


    return
