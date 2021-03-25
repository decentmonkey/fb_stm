default monica_cheats_inited = False
default monica_cheats_iteration_count = 0
default monica_cheats_hungry_enabled = True
label monica_cheats_init:
#    if game.extra == True and monica_cheats_inited == False:
    if monica_cheats_inited == False:
        $ set_var("Picture", actions="lh", scene="bedroom2")
        $ add_hook("Picture", "monica_cheats", scene="bedroom2", label="cheats")
    return

label monica_cheats:
    $ questHelp("other1", True)
    if act=="l":
        return
    menu:
        "Добавить $ 100.":
            $ add_money(100)
        "Увеличить Bitchiness.":
            call bitch(20, "cheat_bitchiness_" + str(monica_cheats_iteration_count)) from _rcall_bitch_2
            $ monica_cheats_iteration_count += 1
        "Уменьшить Bitchiness.":
            call bitch(-20, "cheat_bitchiness_" + str(monica_cheats_iteration_count)) from _rcall_bitch_3
            $ monica_cheats_iteration_count += 1
        "Увеличить Corruption.":
            $ add_corruption(30, "cheat_corruption_" + str(monica_cheats_iteration_count))
            $ monica_cheats_iteration_count +=1
        "Голод: Вкл." if monica_cheats_hungry_enabled == True:
            $ monica_cheats_hungry_enabled = False
            $ monica_eated()
            jump monica_cheats
        "Голод: Выкл." if monica_cheats_hungry_enabled == False:
            $ monica_cheats_hungry_enabled = True
            jump monica_cheats
        "Уйти.":
            pass
    return False
