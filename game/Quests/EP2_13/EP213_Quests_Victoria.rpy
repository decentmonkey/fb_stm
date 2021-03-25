default ep213_quests_victoria1_init_flag = False
default ep213_quests_victoria_completed_day = 0

label ep213_quests_victoria1_init:
    if ep213_quests_victoria1_init_flag == True:
        return
    $ add_hook("before_open", "ep213_quests_victoria2_check", scene="monica_office_entrance", label="victoria_office_scene")
    $ ep213_quests_victoria1_init_flag = True
    return

label ep213_quests_victoria2_check:
    if day - ep212_quests_melanie_completed_day > 1 and week_day != 7 and day_time != "evening": # Запускается через день после событий с Мелани, не в воскресенье и днем
        $ remove_hook()
        call ep213_quests_victoria3() from _rcall_ep213_quests_victoria3
    return False

label ep213_quests_victoria3:
    $ questHelp("victoria_4", True)
    $ questHelp("victoria_5")
    $ define_inventory_object("victoria_pomade", {"description" : t_("Помада Виктории"), "label_suffix" : "_use_victoria_pomade", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/victoria_pomade" + res.suffix + ".png"})
    call ep213_dialogues1_victoria_1() from _rcall_ep213_dialogues1_victoria_1
    call ep213_dialogues1_victoria_2() from _rcall_ep213_dialogues1_victoria_2
    call ep213_dialogues1_victoria_3() from _rcall_ep213_dialogues1_victoria_3
    $ questHelp("victoria_5", True)
    $ questHelp("victoria_6")
    $ visited_list = [2]
label ep213_quests_victoria3_loop1:
    if len(visited_list) >= 4:
        jump ep213_quests_victoria3_loop2
    call ep213_dialogues1_victoria_3a() from _rcall_ep213_dialogues1_victoria_3a
    if _return in visited_list:
        call ep213_dialogues1_victoria_4() from _rcall_ep213_dialogues1_victoria_4
        jump  ep213_quests_victoria3_loop1
    $ visited_list.append(_return)
    if _return == 1:
        call ep213_dialogues1_victoria_5() from _rcall_ep213_dialogues1_victoria_5
        jump ep213_quests_victoria3_loop1
    if _return == 3:
        call ep213_dialogues1_victoria_6() from _rcall_ep213_dialogues1_victoria_6
        jump ep213_quests_victoria3_loop1
    if _return == 4:
        call ep213_dialogues1_victoria_7() from _rcall_ep213_dialogues1_victoria_7
        jump ep213_quests_victoria3_loop1

label ep213_quests_victoria3_loop2:
    call ep213_dialogues1_victoria_8() from _rcall_ep213_dialogues1_victoria_8
    call ep213_dialogues1_victoria_9() from _rcall_ep213_dialogues1_victoria_9
    call ep213_dialogues1_victoria_10() from _rcall_ep213_dialogues1_victoria_10
    call ep213_dialogues1_victoria_11() from _rcall_ep213_dialogues1_victoria_11
    call ep213_dialogues1_victoria_12() from _rcall_ep213_dialogues1_victoria_12
    call ep213_dialogues1_victoria_13() from _rcall_ep213_dialogues1_victoria_13
    call ep213_dialogues1_victoria_14() from _rcall_ep213_dialogues1_victoria_14
    $ questHelp("victoria_6", True)
    $ questHelp("melanie_19")
    $ questHelp("victoria_9")
    call put_work_clothes() from _rcall_put_work_clothes
    call change_scene("working_office_cabinet2", "Fade_long") from _rcall_change_scene_121
    $ add_hook("change_time_day", "ep213_quests_victoria4_checknext", scene="global", label="ep213_quests_victoria4_checknext")
    $ ep213_quests_victoria_completed_day = day
    return

label ep213_quests_victoria4_checknext:
    if day - ep213_quests_victoria_completed_day >= 1 and ep214_quests_melanie_day == 0:
        # на следующий день сцена
        $ move_object("Melanie", "empty")
        $ add_hook("change_time_evening", "ep214_quests_melanie", scene="global", label="ep214_melanie")
        return
    if ep214_quests_melanie_day > 0 and ep215_quests_victoria_melanie_inited1 == False:
        call ep215_quests_victoria_melanie1() from _rcall_ep215_quests_victoria_melanie1 # Виктория приходит к Юлии
    if ep215_victoria_visit_day > 0 and ep215_quests_victoria_melanie_inited2 == False:
        call ep215_quests_victoria_melanie4() from _rcall_ep215_quests_victoria_melanie4 # Виктория приходит к Алексу (у лифта)
    if ep215_victoria_dick_visit_day > 0 and ep216_quests_victoria1_init_flag == False:
        call ep216_quests_victoria1_init() from _rcall_ep216_quests_victoria1_init # Юлия сообщает что надо ехать к Виктории на девичник

#    if ep215_victoria_visit_alex_day > 0 and ep215_quests_victoria_melanie_inited3 == False:
#        call ep215_quests_victoria_melanie6()


    return
