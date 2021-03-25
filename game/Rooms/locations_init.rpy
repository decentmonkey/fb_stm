label locations_init:
    #MAP
    $ add_location("map", caption="", label="map", parent="World")
    $ add_location("Monica_Office", caption="", label="empty_label", parent="World")
    $ add_location("Street_Corner", caption="", label="empty_label", parent="World")
    $ add_location("Dick_Office", caption="", label="empty_label", parent="World")
    $ add_location("Gas_Station", caption="", label="empty_label", parent="World")
    $ add_location("Police", caption="", label="empty_label", parent="World")
    $ add_location("Rich_Hotel", caption="", label="empty_label", parent="World")
    $ add_location("Fitness", caption="", label="empty_label", parent="World")
    $ add_location("Steve_Office", caption="", label="empty_label", parent="World")
    $ add_location("Bank", caption="", label="empty_label", parent="World")
    $ add_location("Cloth_Shop", caption="", label="empty_label", parent="World")
    $ add_location("Street_Corner", caption="", label="empty_label", parent="World")
    $ add_location("Hostel2", caption="", label="empty_label", parent="World")
    $ add_location("House", caption="", label="empty_label", parent="World")

    #BANK
    $ add_location("bank_office", caption=t_("BANK"), label="bank_office", init_label="bank_office_init", parent="bank_office")
    $ add_location("street_bank", caption=t_("BANK"), label="street_bank", init_label="street_bank_init", parent="Bank")

    #CLOTHING SHOP
    $ add_location("street_cloth_shop", caption=t_("Clothing Shop"), label="street_cloth_shop", init_label="street_cloth_shop_init", parent="Cloth_Shop")

    #DICK OFFICE
    $ add_location("street_dick_office", caption=t_("Dick's Office"), label="street_dick_office", init_label="street_dick_office_init", parent="Dick_Office")
    $ add_location("dick_office_cabinet", caption=t_("Dick's Cabinet"), label="dick_office_cabinet", init_label="dick_office_cabinet_init", parent="dick_office_entrance")
    $ add_location("dick_office_entrance", caption=t_("Dick's Office Reception"), label="dick_office_entrance", init_label="dick_office_entrance_init", parent="street_dick_office")
    $ add_location("dick_office_hall1", caption=t_("Dick's Office Hall"), label="dick_office_hall1", init_label="dick_office_hall1_init", parent="dick_office_entrance")
    $ add_location("dick_office_secretary", caption=t_("Dick's Secretary"), label="dick_office_secretary", init_label="dick_office_secretary_init", parent="dick_office_entrance")

    #FITNESS
    $ add_location("street_fitness", caption=t_("Fitness"), label="street_fitness", init_label="street_fitness_init", parent="Fitness")

    #GAS STATION
    $ add_location("street_gas_station", caption=t_("Gas Station"), label="street_gas_station", init_label="street_gas_station_init", parent="Gas_Station")
    $ add_location("gas_station_view1", caption=t_("Gas Station"), label="gas_station_view1", init_label="gas_station_view1_init", parent="street_gas_station")
    $ add_location("gas_station_view2", caption=t_("Gas Station"), label="gas_station_view2", init_label="gas_station_view2_init", parent="street_gas_station")
    $ add_location("gas_station_view3", caption=t_("Gas Station"), label="gas_station_view3", init_label="gas_station_view3_init", parent="street_gas_station")
    $ add_location("gas_station_view4", caption=t_("Gas Station"), label="gas_station_view4", init_label="gas_station_view4_init", parent="street_gas_station")
    $ add_location("gas_station_view5", caption=t_("Gas Station"), label="gas_station_view5", init_label="gas_station_view5_init", parent="street_gas_station")
    $ add_location("gas_station_view6", caption=t_("Gas Station"), label="gas_station_view6", init_label="gas_station_view6_init", parent="street_gas_station")
    $ add_location("gas_station_view_cashier", caption=t_("Gas Station"), label="gas_station_view_cashier", init_label="gas_station_view_cashier_init", parent="street_gas_station")
    $ add_location("gas_station_view_door", caption=t_("Gas Station"), label="gas_station_view_door", init_label="gas_station_view_door_init", parent="street_gas_station")

    #HOSTEL
    $ add_location("hostel_edge_1_a", caption=t_("BLIND ALLEY"), label="hostel_edge_1_a", init_label="hostel_edge_1_a_init", parent="Street_Corner")
    $ add_location("hostel_edge_1_b", caption=t_("BLIND ALLEY"), label="hostel_edge_1_b", init_label="hostel_edge_1_b_init", parent="Street_Corner")
    $ add_location("hostel_edge_1_c", caption=t_("BLIND ALLEY"), label="hostel_edge_1_c", init_label="hostel_edge_1_c_init", parent="Street_Corner")
    $ add_location("hostel_street", caption=t_("HOSTEL STREET"), label="hostel_street", init_label="hostel_street_init", parent="Street_Corner")
    $ add_location("hostel_street_door", caption=t_("HOSTEL ENTRANCE"), label="hostel_street_door", init_label="hostel_street_door_init", parent="Street_Corner")
    $ add_location("hostel_street2", caption=t_("DIRTY STREET"), label="hostel_street2", init_label="hostel_street2_init", parent="Street_Corner")
    $ add_location("hostel_street3", caption=t_("POOR STREET"), label="hostel_street3", init_label="hostel_street3_init", parent="Street_Corner")

    #HOUSE
    $ add_location("basement_bedroom2_cupboard", caption=t_("BASEMENT"), label="basement_bedroom2_cupboard", init_label="basement_bedroom2_cupboard_init", parent="basement_hole")
    $ add_location("basement_bedroom_table", caption=t_("BASEMENT"), label="basement_bedroom_table", init_label="basement_bedroom_table_init", parent="basement_hole")
    $ add_location("basement_bedroom1", caption=t_("BASEMENT"), label="basement_bedroom1", init_label="basement_bedroom1_init", parent="basement_hole")
    $ add_location("basement_bedroom2", caption=t_("BASEMENT"), label="basement_bedroom2", init_label="basement_bedroom2_init", parent="basement_hole")
    $ add_location("basement_hole", caption=t_("BASEMENT"), label="basement_hole", init_label="basement_hole_init", parent="basement_laundry")
    $ add_location("basement_laundry", caption=t_("Laundry"), label="basement_laundry", init_label="basement_laundry_init", parent="basement_pool")
    $ add_location("basement_pool", caption=t_("Basement Pool"), label="basement_pool", init_label="basement_pool_init", parent="floor1")
    $ add_location("bathroom_bath", caption=t_("Bathroom Bath"), label="bathroom_bath", init_label="bathroom_bath_init", parent="floor1")
    $ add_location("bathroom_shower", caption=t_("Bathroom Bath"), label="bathroom_shower", init_label="bathroom_shower_init", parent="floor1")

    $ add_location("bedroom1", caption=t_("Bedroom"), label="bedroom1", init_label="bedroom1_init", parent="floor1")
    $ add_location("bedroom2", caption=t_("Bedroom"), label="bedroom2", init_label="bedroom2_init", parent="floor1")

    $ add_location("kitchen", caption=t_("Kitchen"), label="kitchen", init_label="kitchen_init", parent="floor1")
    $ add_location("kitchen2", caption=t_("Kitchen"), label="kitchen2", init_label="kitchen2_init", parent="floor1")

    $ add_location("bedroom_bardie", caption=t_("BARDIE'S ROOM"), label="bedroom_bardie", init_label="bedroom_bardie_init", parent="floor1")
    $ add_location("bedroom_second", caption=t_("GUEST'S BEDROOM"), label="bedroom_second", init_label="bedroom_second_init", parent="floor1")

    $ add_location("living_room", caption=t_("LIVING ROOM"), label="living_room", init_label="living_room_init", parent="floor1")

    $ add_location("floor1_fountain", caption=t_("Fountain"), label="floor1_fountain", init_label="floor1_fountain_init", parent="floor1")
    $ add_location("floor1_stairs", caption=t_("Stairs Ground Floor"), label="floor1_stairs", init_label="floor1_stairs_init", parent="floor1")
    $ add_location("floor1", caption=t_("Hall Ground Floor"), label="floor1", init_label="floor1_init", parent="street_house_main_yard")
    $ add_location("floor2_mirrors", caption=t_("Mirrors"), label="floor2_mirrors", init_label="floor2_mirrors_init", parent="floor1")
    $ add_location("floor2_stairs", caption=t_("Stairs Top Floor"), label="floor2_stairs", init_label="floor2_stairs_init", parent="floor1")
    $ add_location("floor2", caption=t_("Hall Top Floor"), label="floor2", init_label="floor2_init", parent="floor1")

    $ add_location("street_house_fence", caption=t_("House Fence"), label="street_house_fence", init_label="street_house_fence_init", parent="street_house_main_yard")
    $ add_location("street_house_gate", caption=t_("House Gates"), label="street_house_gate", init_label="street_house_gate_init", parent="street_house_main_yard")
    $ add_location("street_house_main_yard", caption=t_("House Yard"), label="street_house_main_yard", init_label="street_house_main_yard_init", parent="House")
    $ add_location("street_house_outside", caption=t_("House Outside"), label="street_house_outside", init_label="street_house_outside_init", parent="street_house_main_yard")

    # Monica's Office
    $ add_location("street_monica_office", caption=t_("Monica's Office Outside"), label="street_monica_office", init_label="street_monica_office_init", parent="Monica_Office")
    $ add_location("monica_office_cabinet_table", caption=t_("Monica's Office"), label="monica_office_cabinet_table", init_label="monica_office_cabinet_table_init", parent="monica_office_entrance")
    $ add_location("monica_office_cabinet", caption=t_("Monica's Office"), label="monica_office_cabinet", init_label="monica_office_cabinet_init", parent="monica_office_entrance")
    $ add_location("monica_office_entrance", caption=t_("Monica's Office Entrance"), label="monica_office_entrance", init_label="monica_office_entrance_init", parent="street_monica_office")
    $ add_location("monica_office_photostudio", caption=t_("Photostudio"), label="monica_office_photostudio", init_label="monica_office_photostudio_init", parent="monica_office_entrance")
    $ add_location("monica_office_secretary_teatable", caption=t_("Monica's Secretary"), label="monica_office_secretary_teatable", init_label="monica_office_secretary_teatable_init", parent="monica_office_entrance")
    $ add_location("monica_office_secretary", caption=t_("Monica's Secretary"), label="monica_office_secretary", init_label="monica_office_secretary_init", parent="monica_office_entrance")

    # Police
    $ add_location("street_police", caption=t_("Police Station"), label="street_police", init_label="street_police_init", parent="Police")
    $ add_location("police_entrance", caption=t_("Police Station"), label="police_entrance", init_label="police_entrance_init", parent="street_police")

    # Rich Hotel
    $ add_location("street_rich_hotel", caption=t_("Hotel Le Grand"), label="street_rich_hotel", init_label="street_rich_hotel_init", parent="Rich_Hotel")
    $ add_location("rich_hotel_event_hall", caption=t_("Hotel Le Grand"), label="rich_hotel_event_hall", init_label="rich_hotel_event_hall_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_scene", caption=t_("Hotel Le Grand"), label="rich_hotel_event_scene", init_label="rich_hotel_event_scene_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_sittable", caption=t_("Hotel Le Grand"), label="rich_hotel_event_sittable", init_label="rich_hotel_event_sittable_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_sofa", caption=t_("Hotel Le Grand"), label="rich_hotel_event_sofa", init_label="rich_hotel_event_sofa_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_tables", caption=t_("Hotel Le Grand"), label="rich_hotel_event_tables", init_label="rich_hotel_event_tables_init", parent="rich_hotel_reception")

    # Steve's Office
    $ add_location("street_steve_office", caption=t_("STEVE'S OFFICE"), label="street_steve_office", init_label="street_steve_office_init", parent="Steve_Office")

    # Whores place
    $ add_location("street_corner", caption=t_("Street Edge"), label="street_corner", init_label="street_corner_init", parent="Street_Corner")
    $ add_location("whores_place", caption=t_("Whores place"), label="whores_place", init_label="whores_place_init", parent="Street_Corner")
    $ add_location("whores_place_shawarma", caption=t_("Shawarma"), label="whores_place_shawarma", init_label="whores_place_shawarma_init", parent="Street_Corner")
    $ add_location("whores_place_street1", caption=t_("Dirty street"), label="whores_place_street1", init_label="whores_place_street1_init", parent="Street_Corner")

    # Dummy location
    $ add_location("empty", caption="", label="", parent="none")




    return

label locations_init_clothing_shop:
    $ add_location("cloth_shop_view1", caption=t_("Clothing Shop"), label="cloth_shop_view1", init_label="cloth_shop_view1_init", parent="Cloth_Shop")
    $ add_location("cloth_shop_view2", caption=t_("Clothing Shop"), label="cloth_shop_view2", init_label="cloth_shop_view2_init", parent="Cloth_Shop")
    $ add_location("cloth_shop_cashier", caption=t_("Clothing Shop"), label="cloth_shop_cashier", init_label="cloth_shop_cashier_init", parent="Cloth_Shop")
    $ add_location("cloth_shop_dressing_room", caption=t_("Clothing Shop"), label="cloth_shop_dressing_room", init_label="cloth_shop_dressing_room_init", parent="Cloth_Shop")
    $ add_location("cloth_shop_dressing_room2", caption=t_("Clothing Shop"), label="cloth_shop_dressing_room2", init_label="cloth_shop_dressing_room2_init", parent="Cloth_Shop")


    return

label locations_init_steve_office:
    $ add_location("steve_office_secretary", caption=t_("Офис Стива"), label="steve_office_secretary", init_label="steve_office_secretary_init", parent="Steve_Office")
    $ add_location("steve_office_office", caption=t_("Офис Стива"), label="steve_office_office", init_label="steve_office_office_init", parent="Steve_Office")
    $ add_location("steve_office_office_table", caption=t_("Офис Стива"), label="steve_office_office_table", init_label="steve_office_office_table_init", parent="Steve_Office")
    return

label locations_init_working_office:
    # Офис Моники (работа)
    $ add_location("working_office", caption=t_("ОФИС"), label="working_office", init_label="working_office_init", parent="monica_office_entrance")
    $ add_location("working_office2", caption=t_("ОФИС"), label="working_office2", init_label="working_office2_init", parent="monica_office_entrance")
    $ add_location("working_office_cabinet", caption=t_("КАБИНЕТ МОНИКИ"), label="working_office_cabinet", init_label="working_office_cabinet_init", parent="monica_office_entrance")
    $ add_location("working_office_cabinet2", caption=t_("КАБИНЕТ МОНИКИ"), label="working_office_cabinet2", init_label="working_office_cabinet2_init", parent="monica_office_entrance")

    return

label locations_init_rich_hotel_restaurant:
    # Рецепшин и вход в ресторан Le Grand
    $ add_location("rich_hotel_reception", caption=t_("Hotel Reception"), label="rich_hotel_reception", init_label="rich_hotel_reception_init", parent="street_rich_hotel")
    $ add_location("rich_hotel_restaurant_entrance", caption=t_("Restaurant"), label="rich_hotel_restaurant_entrance", init_label="rich_hotel_restaurant_entrance_init", parent="rich_hotel_reception")

    return

label locations_init_melanie_home:
    # Дом Мелани (пока пустой)
    $ add_location("melanie_home", caption=t_("АПАРТАМЕНТЫ МЕЛАНИ"), label="melanie_home", init_label="melanie_home_init", parent="World")
    return


label locations_init_police_jail_cage:
    # Камера в полиции
    $ add_location("police_cell1", caption=t_("КАМЕРА"), label="police_cell1", init_label="police_cell1_init", parent="police_entrance")
    $ add_location("police_cell2", caption=t_("КАМЕРА"), label="police_cell2", init_label="police_cell2_init", parent="police_entrance")
    $ add_location("police_cell3", caption=t_("РЕШЕТКА"), label="police_cell3", init_label="police_cell3_init", parent="police_entrance")
    return

label locations_init_college:
    # Колледж
    $ add_location("street_college", caption=t_("КОЛЛЕДЖ"), label="street_college", init_label="street_college_init", parent="World")
    $ add_location("college_class", caption=t_("КЛАСС БАРДИ"), label="college_class", init_label="college_class_init", parent="street_college")
    return

label locations_init_pub_stage:
    $ add_location("pub_makeuproom", caption=t_("ГРИМЕРНАЯ КОМНАТА"), label="pub_makeuproom", init_label="pub_makeuproom_init", parent="pub")
    $ add_location("pub_stage1", caption=t_("SHINY HOLE"), label="pub_stage1", init_label="pub_stage1_init", parent="pub")
    return

label locations_init_pub_makeuptoom_mollytable:
    $ add_location("pub_makeuproom_mollytable", caption=t_("СТОЛИК МОЛЛИ"), label="pub_makeuproom_mollytable", init_label="pub_makeuproom_mollytable_init", parent="pub_makeuproom")
    return

label locations_init_laundry_wash_machine:
    $ add_location("basement_laundry_washmachine", caption=t_("Laundry"), label="basement_laundry_washmachine", init_label="basement_laundry_washmachine_init", parent="basement_laundry")
    return

label locations_init_basement_bedroom_table_opened:
    $ add_location("basement_bedroom_table_opened", caption=t_("BASEMENT"), label="basement_bedroom_table_opened", init_label="basement_bedroom_table_opened_init", parent="basement_laundry")
    return


label locations_init_julia_street:
    $ add_location("street_juliahome", caption=t_("ДОМ ЮЛИИ"), label="street_juliahome", init_label="street_juliahome_init", parent="Street_Corner")
    return

label locations_init_philip_home:
    $ add_location("street_philiphome", caption=t_("ДОМ ФИЛИППА"), label="street_philiphome", init_label="street_philiphome_init", parent="World")
    return


label locations_init_monicahome:
    $ add_location("street_monicahome", caption=t_("Дом в трущобах"), label="street_monicahome", init_label="street_monicahome_init", parent="Street_Corner")
    $ add_location("monicahome_livingroom", caption=t_("СПАЛЬНЯ"), label="monicahome_livingroom", init_label="monicahome_livingroom_init", parent="street_monicahome")
    $ add_location("monicahome_livingroomwardrobe", caption=t_("ГАРДЕРОБ"), label="monicahome_livingroomwardrobe", init_label="monicahome_livingroomwardrobe_init", parent="monicahome_livingroom")
    $ add_location("monicahome_kitchen", caption=t_("КУХНЯ"), label="monicahome_kitchen", init_label="monicahome_kitchen_init", parent="monicahome_livingroom")
    $ add_location("monicahome_bathroom", caption=t_("ВАННАЯ КОМНАТА"), label="monicahome_bathroom", init_label="monicahome_bathroom_init", parent="monicahome_livingroom")
    return

label locations_init_juliahome:
    $ add_location("juliahome_livingroom", caption=t_("АПАРТАМЕНТЫ ЮЛИИ"), label="juliahome_livingroom", init_label="juliahome_livingroom_init", parent="street_juliahome")
    $ add_location("juliahome_kitchen", caption=t_("АПАРТАМЕНТЫ ЮЛИИ"), label="juliahome_kitchen", init_label="juliahome_kitchen_init", parent="juliahome_livingroom")
    $ add_location("juliahome_bathroom", caption=t_("АПАРТАМЕНТЫ ЮЛИИ"), label="juliahome_bathroom", init_label="juliahome_bathroom_init", parent="juliahome_livingroom")
    $ add_location("juliahome_bathroomshower", caption=t_("АПАРТАМЕНТЫ ЮЛИИ"), label="juliahome_bathroomshower", init_label="juliahome_bathroomshower_init", parent="juliahome_bathroom")

    return

label locations_init_public_event2:
    $ add_location("public_event2", caption=t_("КЛУБ КЭМПБЕЛЛА"), label="public_event2", init_label="public_event2_init", parent="World")
    return

label locations_init_rich_hotel_restaurant2:
    $ add_location("rich_hotel_restaurant", caption=t_("Restaurant"), label="rich_hotel_restaurant", init_label="rich_hotel_restaurant_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_lift", caption=t_("Lift"), label="rich_hotel_lift", init_label="rich_hotel_lift_init", parent="rich_hotel_reception")

    return

label locations_init_hostel_inside:
    $ add_location("hostel_bathroom_toilet", caption=t_("ДУШЕВАЯ"), label="hostel_bathroom_toilet", init_label="hostel_bathroom_toilet_init", parent="hostel_reception")
    $ add_location("hostel_bathroom", caption=t_("ДУШЕВАЯ"), label="hostel_bathroom", init_label="hostel_bathroom_init", parent="hostel_reception")
    $ add_location("hostel_bedroom", caption=t_("ХОСТЕЛ"), label="hostel_bedroom", init_label="hostel_bedroom_init", parent="hostel_reception")
    $ add_location("hostel_reception", caption=t_("ХОСТЕЛ"), label="hostel_reception", init_label="hostel_reception_init", parent="hostel_street")
    return

label locations_init_house_neighbour:
    $ add_location("street_house_neighbour", caption=t_("ДОМ СОСЕДА"), label="street_house_neighbour", init_label="street_house_neighbour_init", parent="House")
    return

label locations_init_victoriahome1:
    $ add_location("street_victoriahome", caption=t_("АПАРТАМЕНТЫ ВИКТОРИИ"), label="street_victoriahome", init_label="street_victoriahome_init", parent="World")
    return


label world:
    return
label world_init:
    return


#
