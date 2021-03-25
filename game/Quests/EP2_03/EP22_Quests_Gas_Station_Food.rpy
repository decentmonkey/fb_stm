define gasStationGoodsPrices = {
    "donut": 2,
    "cookies cherry filled": 2,
    "chocolate cake": 2,
    "cannoli": 3,
    "napoleon": 2,
    "brownie": 2,
    "cupcake": 4,
    "cookie with nuts": 1,
    "waffles": 1,
}

define gasStationGoodsNames = {
    "donut": t_("Пончик"),
    "cookies cherry filled": t_("Печенье с вишневой начинкой"),
    "chocolate cake": t_("Шоколадный торт"),
    "cannoli": t_("Канноли"),
    "napoleon": t_("Наполеон"),
    "brownie": t_("Пирожное"),
    "cupcake": t_("Кекс"),
    "cookie with nuts": t_("Печенье с орехами"),
    "waffles": t_("Вафли"),
}

label ep22_quests_Gas_Station_Food1_buy_food:

    if gasStationGoodsPrices[obj_name] > money:
        mt "У меня нет денег на это..."
        return
    $ add_money(-gasStationGoodsPrices[obj_name])
    $ notif(gasStationGoodsNames[obj_name])
    $ add_inventory("food_package", 1, True)
    if monicaFoodInventory.has_key(obj_name) == False:
        $ monicaFoodInventory[obj_name] = 0
    $ monicaFoodInventory[obj_name] += 1
    return
