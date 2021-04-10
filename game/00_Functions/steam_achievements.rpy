init:

#    $ achievement.register("")
#    $ achievement.sync()
init python:
    def steam_achievement(achName):
        achievement.grant(achName)
        achievement.sync()
        return


    def questHelp_achievement_check(questName):
        questHelp_achievements_list = {
            "house_10" : "ach18",
            "house_36" : "ach19",
            "shop_6" : "ach20",
            "shop_2" : "ach21",
            "shop_3" : "ach21",
            "shop_6" : "ach21",
            "steve_16" : "ach22",
            "photoshoot_1" : "ach23",
            "office_11" : "ach24",
            "philip_2" : "ach24",
            "melanie_5" : "ach25",
            "office_25" : "ach26",
            "office_34" : "ach27",
            "office_41" : "ach28",
            "office_44" : "ach29",
            "office_50" : "ach30",
            "escort_12" : "ach31",
            "photoshoot_14a": "ach32",
            "office_28" : "ach33",
            "julia_35" : "ach35",
            "julia_55" : "ach36",
            "victoria_1a" : "ach37",
            "victoria_3" : "ach38",
            "victoria_13" : "ach39",
            "victoria_14" : "ach40",
            "marcus_2" : "ach41",
            "marcus_11" : "ach42",
            "marcus_19" : "ach44",
            "work_slums_1" : "ach46",
            "work_slums_4" : "ach47",
            "shinyhole_1" : "ach48",
            "shinyhole_4" : "ach49",
            "shinyhole_9" : "ach50",
            "shinyhole_29" : "ach51",
            "shinyhole_49" : "ach52",
            "work_slums_46" : "ach53",
            "hostel_2" : "ach54",
            "flat_slums_2" : "ach56",
            "escort_2" : "ach57",
            "philip_4" : "ach58",
            "escort_8" : "ach59",
            "escort_10" : "ach60",
            "philip_7" : "ach61",
            "revenge_3" : "ach63"
        }
        if questHelp_achievements_list.has_key(questName):
            achievement.grant(questHelp_achievements_list[questName])
            achievement.sync()
        return
















#
