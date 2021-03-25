default monicaOfficeWorkOffendedCount1 = 0 # Кол-во раз Моника заставляла Юлию работать допоздна
default monicaOfficeWorkKindCount1 = 0 # Кол-во раз Моника жалела Юлию и не заставляла много работать
default juliaOfficeOffended1 = False # Моника заставляла Юлию работать допоздна
default juliaOfficeOffended2 = False # Моника заставляла Юлию собирать отчеты вместо себя и ругалась при этом

default juliaOfficeOffendedDay = 0

label juliaProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = t_("Юлия стесняется комплиментов Моники и боится ее.")
    if char_data["level"] == 3:
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
    if char_data["level"] == 4:
        $ questHelp("julia_24", True)
        $ questHelp("julia_25", skipIfExists=True)
        $ questHelp("julia_26", skipIfExists=True)
        $ char_data["enabled"] = True
        $ char_data["caption"] = t_("Юлия приняла ухаживания Моники, но еще побаивается ее.")
    if char_data["level"] == 5:
        $ char_data["enabled"] = True
        $ char_data["caption"] = t_("Юлия влюбляется в Монику, но еще не доверяет ей.")
    if char_data["level"] == 6:
        $ questHelp("julia_30", True)
        $ questHelp("julia_31", skipIfExists=True)
        $ char_data["enabled"] = True
#        $ char_data["caption"] = t_("Юлия влюбляется в Монику, но еще не доверяет ей.")
    if char_data["level"] == 7:
        $ char_data["enabled"] = True
        $ char_data["caption"] = t_("Юлия влюбилась в Монику, но боится обжечься в отношениях.")

    if char_data["level"] == 8:
        $ char_data["enabled"] = True

    if char_data["level"] == 9:
        $ char_data["enabled"] = True
        $ char_data["caption"] = t_("Юлия любит Монику и хочет с ней пробовать все виды развлечений.")
#        $ char_data["caption"] = t_("Юлия любит Монику и хочет быть с ней.")


#        $ char_data["enabled"] = False
#        $ char_data["caption_diabled"] = t_("Work in progress...")
#    $ char_data["caption_diabled"] = t_("Ожидание дальнейшего прогресса сюжета игры...")
#    $ char_data["show_caption_diabled"] = True
#    if char_data["level"] == 4:
    return
