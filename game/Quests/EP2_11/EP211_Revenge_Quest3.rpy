label ep211_revenge_quest1:
    call e211_dialogues_revenge_quest1() from _rcall_e211_dialogues_revenge_quest1
    $ questHelp("revenge_5", True)
    $ questHelp("revenge_6")
    $ questHelpDesc("revenge_desc1", "revenge_desc2")

    $ remove_objective("find_fred")
    $ add_objective("go_to_steve", t_("Идти к Стиву"), c_red, 125)
    $ day_time = "day"
    $ day_time_suffix = ""
#    if week_day == 7:
#        $ day += 1
    $ remove_hook(label="steve_office_check_evening")
    $ move_object("Steve", "steve_office_office_table")
    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    $ map_enabled = False
    $ add_hook("Teleport_Building", "ep211_revenge_quest2", scene="street_steve_office", quest="revenge_quest", label="revenge_quest_steve")
    $ autorun_to_object("e211_dialogues_revenge_quest1a", scene="street_steve_office")
    call change_scene("street_steve_office", "Fade_long", "highheels_run2") from _rcall_change_scene_8
    return False


label ep211_revenge_quest2:
    call e211_dialogues_revenge_quest2() from _rcall_e211_dialogues_revenge_quest2
    call e211_dialogues_revenge_quest3() from _rcall_e211_dialogues_revenge_quest3
    $ questHelp("revenge_6", True)
    $ questHelp("revenge_7")

    stop music
    sound snd_cinematic_impact

    img black_screen
#    pause 2.0
    $ renpy.pause(2.0, hard=True)
    img black_screen
    with Dissolve(2.0)
    call textonblack("FASHION BUSINESS") from _rcall_textonblack_34
    img black_screen
    with Dissolve(2.0)
    $ renpy.pause(2.0, hard=True)

    call ep212_dialogues_revenge_quest1() from _rcall_ep212_dialogues_revenge_quest1

    $ questHelp("revenge_7", True)

    stop music
    sound snd_cinematic_impact
    img black_screen
    $ renpy.pause(4.0, hard=True)
    music Continue_Life
    img black_screen
    with Dissolve(2.0)
    call textonblack("TO BE CONTINUED IN THE NEXT UPDATE") from _rcall_textonblack
    img black_screen
    with Dissolve(2.0)
    $ renpy.pause(2.0, hard=True)
    img black_screen
    with Dissolve(0.5)
    img Patreon_Game_Logo
    with Dissolve(0.7)
    $ renpy.pause(1.0, hard=True)
##    pause 4.0
    $ renpy.pause(4.0, hard=True)
    img black_screen
    with Dissolve(0.7)
    $ renpy.pause(3.0, hard=True)
##    pause 30.0
##    music stop
##    pause 1.0
    call credits() from _rcall_credits
    $ MainMenu(confirm=False)()
    return False
