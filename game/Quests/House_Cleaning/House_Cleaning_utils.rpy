init python:
    def add_cleaning(status): #True - уборка была сделана, #False - уборка была не сделана
        global cleaningLog
        cleaningLog.insert(0, status)
        return

    def get_cleaning_status(days): # Подсчитывает есть-ли пропуски уборки за последние 3 дня
        if len(cleaningLog) < days:
            return False
        need_amount = days
        for idx1 in range(0,days):
            if cleaningLog[idx1] == True:
                need_amount = need_amount -1
        if need_amount == 0:
            return True
        else:
            return False
