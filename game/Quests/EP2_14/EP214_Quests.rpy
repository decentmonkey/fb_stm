default ep214_quests_load_init_flag = False
label ep214_quests_load_init:
    if ep214_quests_load_init_flag == False:
        $ ep214_quests_load_init_flag = True
        $ slumsApartmentsRentPrice = 100.0
        $ slumsApartmentsRentPriceDiscount1 = 90.0
        $ slumsApartmentsRentPriceDiscount2 = 80.0
        if char_info["Ralph"]["level"] == 1:
            $ char_info["Ralph"]["enabled"] = True
            $ char_info["Ralph"]["caption"] = t_("Ральф примерный семьянин.")
