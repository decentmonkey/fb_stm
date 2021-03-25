label Steve_init:
    call Steve_Life_init() from _call_Steve_Life_init
    return

label getSteveStatus:
    if get_active_objects("Steve", scene="steve_office_office_table") == False:
        if week_day == 7:
#            jane "Нет, Миссис Бакфетт, Мистер Стив будет только на следующей неделе."
            return 2
        else:
#            jane "Нет, Миссис Бакфетт, Мистер Стив будет только завтра."
            return 1
    return 0
