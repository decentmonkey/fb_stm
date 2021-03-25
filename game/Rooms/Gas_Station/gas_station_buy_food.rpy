default gasStationFoodInited = False

label gas_station_buy_food:
    $ print "enter_gas_station_buy_food"
    call gas_station_buy_food_init() from _call_gas_station_buy_food_init
    $ miniMapData = []

    $ scene_image = "scene_Gas_Station_View3"
    return

label gas_station_buy_food_init:

    $ add_object_to_scene("donut", {"type":2, "base":"Gas_Station_View3_Cakes1", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Пончик") + " $ " + convertMoneyStr(gasStationGoodsPrices["donut"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("cookies cherry filled", {"type":2, "base":"Gas_Station_View3_Cakes2", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Печенье с вишневой начинкой") + " $ " + convertMoneyStr(gasStationGoodsPrices["cookies cherry filled"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("chocolate cake", {"type":2, "base":"Gas_Station_View3_Cakes3", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Шоколадный торт") + " $ " + convertMoneyStr(gasStationGoodsPrices["chocolate cake"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("cannoli", {"type":2, "base":"Gas_Station_View3_Cakes4", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Канноли") + " $ " + convertMoneyStr(gasStationGoodsPrices["cannoli"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("napoleon", {"type":2, "base":"Gas_Station_View3_Cakes5", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Наполеон") + " $ " + convertMoneyStr(gasStationGoodsPrices["napoleon"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("brownie", {"type":2, "base":"Gas_Station_View3_Cakes6", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Пирожное") + " $ " + convertMoneyStr(gasStationGoodsPrices["brownie"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("cupcake", {"type":2, "base":"Gas_Station_View3_Cakes7", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Кекс") + " $ " + convertMoneyStr(gasStationGoodsPrices["cupcake"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("cookie with nuts", {"type":2, "base":"Gas_Station_View3_Cakes8", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Печенье с орехами") + " $ " + convertMoneyStr(gasStationGoodsPrices["cookie with nuts"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("waffles", {"type":2, "base":"Gas_Station_View3_Cakes9", "click" : "gas_station_buy_food_environment", "actions" : "l", "zorder" : 1, "group":"environment", "hovered_caption": (t__("Вафли") + " $ " + convertMoneyStr(gasStationGoodsPrices["waffles"]))}, scene="gas_station_buy_food")
    $ add_object_to_scene("Teleport_Street_Gas_Station", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_buy_food_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="gas_station_buy_food")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label gas_station_buy_food_teleport:
    if obj_name == "Teleport_Street_Gas_Station":
        call change_scene("street_gas_station") from _call_change_scene_241
        return
    return
label gas_station_buy_food_environment:
    call ep22_quests_Gas_Station_Food1_buy_food() from _call_ep22_quests_Gas_Station_Food1_buy_food
    return
