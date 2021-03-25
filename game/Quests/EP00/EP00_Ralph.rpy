label ep00_ralph1:
#    $ questHelp("house_30", True)
    $ questHelp("house_31")
#    $ questHelpDesc("house_desc14", "house_desc15")
#    $ questLog(72, True)
    $ add_objective("seduce_ralph", t_("Соблазнить Ральфа."), c_blue, 105)
    $ add_hook("monica_cleaning_start", "ep212_quests_bardie_ralph3_init_cleaning", scene="global", label="ep212_quests_bardie_ralph3_init_cleaning")
    $ add_hook("monica_cleaning_end", "ep212_quests_bardie_ralph6_cleaning_end", scene="global", label="ep212_quests_bardie_ralph3_init_cleaning")
    $ monicaBardieRalphSeducingStage = 1
    return
