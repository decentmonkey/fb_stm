label bartenderWaitressProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ questHelp("shinyhole_2", True)
        $ questHelp("shinyhole_4", skipIfExists=True)
        $ questHelpDesc("shinyhole_desc1", False)
        $ questHelpDesc("shinyhole_desc2")
        $ char_data["caption"] = t_("Жена бармена. Лапает меня, пока Джо не видит.")
        pass
    if char_data["level"] == 3:
        $ progress_character_name = t_("Эшли")
        help "Прогресс [progress_character_name] максимален, ждите следующих обновлений игры!"
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = t_("Work in progress...")
    return
