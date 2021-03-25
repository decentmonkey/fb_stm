label mollyProgressLevelUp:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["caption"] = t_("Молли ненавидит Монику и пакостит ей. Моника тоже...")
    return
