default ep28_quests_initialized = False

label ep28_quests:
    if ep28_quests_initialized == True:
        return

    if check_hook(label="ep26_bardie_dialogue5_betty_kitchen"):
        $ bettyMustFeedMonicaOnKitchenBoobs = True
        call ep28_monica_bardie_init() from _call_ep28_monica_bardie_init
    $ ep28_quests_initialized = True
    return
