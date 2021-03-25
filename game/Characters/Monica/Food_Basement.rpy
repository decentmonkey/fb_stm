#define monicaFoodInventory = {} #какая еда есть у Моники с собой
#define monicaFoodInventoryBasement = {} #какая еда лежит на столе в спальне в подвале


#cake2
#cake3
#cake9
#cake8
#cake4
#cake6
#cake1
#cake5
#cake7
default sleepAfterEat = False

label food_basement_room_init:
label food_basement_room_init2:
    $ print "food init!"
    $ flag1 = False
    python:
        for food_name in monicaFoodInventory:
            if monicaFoodInventory[food_name] > 0:
                if monicaFoodInventoryBasement.has_key(food_name) == False:
                    monicaFoodInventoryBasement[food_name] = 0
                monicaFoodInventoryBasement[food_name] += monicaFoodInventory[food_name]
                remove_inventory("food_package", monicaFoodInventory[food_name], True)
                monicaFoodInventory[food_name] = 0
                flag1 = True
    if flag1 == True:
        sound snd_take_paper

    python:
        set_active(False, label="food", scene="basement_bedroom2")
        set_active(False, label="food", scene="basement_bedroom_table")
        flag1 = False
        for food_name in monicaFoodInventoryBasement:
            if monicaFoodInventoryBasement[food_name] > 0:
                set_active(food_name, True, scene="basement_bedroom2")
                set_active(food_name, True, scene="basement_bedroom_table")
                flag1 = True

        set_active("Book", True, scene="basement_bedroom2")
        set_active("Book", True, scene="basement_bedroom_table")
        if flag1 == True:
            set_active("FoodPaper", True, scene="basement_bedroom2")
            set_active("FoodPaper", True, scene="basement_bedroom_table")
            set_active("Book", False, scene="basement_bedroom2")
            set_active("Book", False, scene="basement_bedroom_table")


    return


label food_basement_eat_food:
    if act == "l":
        if obj_name == "donut":
            mt "Пончик..."
            sound snd_eat1
        if obj_name == "cookies cherry filled":
            mt "Печенье с вишневой начинкой."
            sound snd_eat1
        if obj_name == "chocolate cake":
            mt "Шоколадный торт."
            "От такой еды полнеешь, я такое не люблю!"
            sound snd_gulp
        if obj_name == "cannoli":
            mt "Канноли."
            sound snd_eat1
        if obj_name == "napoleon":
            mt "Наполеон."
            "От такой еды полнеешь, я такое не люблю!"
            sound snd_gulp
        if obj_name == "brownie":
            mt "Пирожное."
            "От такой еды полнеешь, я такое не люблю!"
            sound snd_gulp
        if obj_name == "cupcake":
            mt "Кекс!"
            mt "Мое любимое кондитерское изделие! Ням-ням!"
            sound snd_eat1
        if obj_name == "cookie with nuts":
            mt "Печенье с орехами."
            mt "Жуткое печенье, очень жирное."
            sound snd_gulp
        if obj_name == "waffles":
            mt "Вафли."
            mt "Я не люблю вафли!!!"
            sound snd_gulp
        return
#    if rand(0,1) == 0:
#        sound snd_eat1
#    else:
#        sound hlup21
#        sound snd_gulp
    $ monicaFoodInventoryBasement[obj_name] -= 1
    $ eatFoodName = obj_name
    call monicaEat() from _call_monicaEat_11
    call food_basement_room_init() from _call_food_basement_room_init
    call refresh_scene_fade() from _call_refresh_scene_fade_94
    $ autorun_to_object("food_basement_eat_food_comment", scene="basement_bedroom_table")
    return

label food_basement_eat_food_comment:
    if eatFoodName == "chocolate cake" or eatFoodName == "cannoli" or eatFoodName == "napoleon" or eatFoodName == "brownie":
        mt "От такой еды полнеешь, я такое не люблю!"
    if eatFoodName == "cupcake":
        mt "Мое любимое кондитерское изделие! Ням-ням!"
    if eatFoodName == "cookie with nuts":
        mt "Жуткое печенье, очень жирное."
    if eatFoodName == "waffles":
        mt "Я не люблю вафли!!!"

    if sleepAfterEat == True:
        $ sleepAfterEat = False
        call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_240
        call monica_process_sleep() from _call_monica_process_sleep_2
        return False
    return

label food_basement_check_food:
    $ flag1 = food_basement_check_food_func()
    return flag1

init python:
    def food_basement_check_food_func():
        flag1 = False
        for food_name in monicaFoodInventoryBasement:
            if monicaFoodInventoryBasement[food_name] > 0:
                flag1 = True
        return flag1
