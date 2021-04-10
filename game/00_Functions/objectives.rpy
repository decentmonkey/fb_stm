default questLogJustUpdated = False
default questLogUpdatedDay = 0
default questHelpJustUpdated = False
default questHelpUpdatedDay = 0
default questHelpData = {}
default questHelpDataQuests = {}
default questHelpDataCategoriesDescriptions = {}
default questHelpDataCategoriesDescriptionsData = {}
default questHelpDataLastMemory = {}
default questHelpDataLastQuestsBold = {}
default questHelpDataCategoriesBold = {}
default questHelpCurrentCategory = False
default questHelpCurrentQuest = False
default questHelpCategoriesHistory = []
default questHelpCategoriesHistoryStatic = []

default questHelpFlag1 = False
default questHelpFlag2 = False
default questHelpFlag3 = False
default questHelpFlag4 = False
default questHelpFlag5 = False
default questHelpFlag6Noir = False
default questHelpFlag7Worker = False
default questHelpFlag8Melanie = False
default questHelpFlag9 = False
default questHelpFlag10 = False
default questHelpFlag11 = False
default questHelpFlag12 = False
default questHelpFlag13 = False
default questHelpFlag14 = False
default questHelpFlag15 = False
default questHelpFlag16 = False
default questHelpFlag17 = False
default questHelpFlag18 = False
default questHelpFlag19 = False
default questHelpFlag20 = False
default questHelpFlag21 = False
default questHelpFlag22 = False
default questHelpFlag23 = False
default questHelpFlag24 = False
default questHelpFlag25 = 0
default questHelpFlag26 = False

default questHelpActivated = False

init python:
    def add_objective(objective_id, objective_name, objective_color="#ffffff", objective_priority=0):
        global objectives_list
        for objective in objectives_list:
            if objective[0] == objective_id:
                return
        objective = [objective_id, objective_name, objective_color, objective_priority]
        if len(objectives_list) > 0:
            for idx in range(0, len(objectives_list)):
                if objectives_list[idx][3] >= objective_priority:
                    objectives_list.insert(idx, objective)
                    return;
        objectives_list.append(objective)


    def remove_objective(objective_id):
        global objectives_list
        for idx in range(len(objectives_list)-1, -1, -1):
            if objectives_list[idx][0] == objective_id:
                objectives_list.pop(idx)
#                renpy.pause()
#                idx = 0
#        print objectives_list

    def questLog(questLogIdx, status):
        global questLogDataEnabled, questLogLinesUpdated, questLogJustUpdated, questLogUpdatedDay, day
        if status == True and (questLogDataEnabled.has_key(str(questLogIdx)) == False or questLogDataEnabled[str(questLogIdx)] != True):
            if day > 0:
                notif(t__("Журнал обновлен"))
            questLogLinesUpdated.append(str(questLogIdx))
            questLogJustUpdated = True
            questLogUpdatedDay = day
        questLogDataEnabled[str(questLogIdx)] = status
#        for idx in range(0, len(questLogData)):
#            if questLogData[idx][0] == questLogIdx:
#                questLogData[idx][2] = status
#                break
        return

    def questHelp(*args, **kwargs): # questHelp(questHelpName, True/False) #True - пройден, False - провален, без второго аргумента - просто новый квест (желтенький)
        global questHelpDataQuests, questHelpData, questHelpJustUpdated, questHelpUpdatedDay, day, questHelpActivated
        questHelpName = args[0]
        if len(args) > 1:
            status = 1 if args[1] == True else -1
        else:
            status = 0

        if questHelpDataQuests.has_key(questHelpName) == False:
            return
        questCategory = questHelpDataQuests[questHelpName][0]
        if questHelpData.has_key(questCategory) == False:
            questHelpData[questCategory] = []

        if kwargs.has_key("skipIfExists"):
            if kwargs["skipIfExists"] == True:
                for idx in range(0, len(questHelpData[questCategory])):
                    if questHelpData[questCategory][idx][0] == questHelpName:
                        return

        if kwargs.has_key("skipIfTrue"):
            if kwargs["skipIfTrue"] == True:
                for idx in range(0, len(questHelpData[questCategory])):
                    if questHelpData[questCategory][idx][0] == questHelpName and questHelpData[questCategory][idx][0] == 1:
                        return

        if kwargs.has_key("skipIfFalse"):
            if kwargs["skipIfFalse"] == True:
                for idx in range(0, len(questHelpData[questCategory])):
                    if questHelpData[questCategory][idx][0] == questHelpName and questHelpData[questCategory][idx][0] == -1:
                        return

        for idx in range(0, len(questHelpData[questCategory])):
            if questHelpData[questCategory][idx][0] == questHelpName:
                if day > 0 and questHelpData[questCategory][idx][1] != status and questHelpActivated == True:
                    notif(t__("Список событий обновлен"))
                    questHelpJustUpdated = True
                    questHelpUpdatedDay = day
                questHelpData[questCategory][idx][1] = status
                if status == 1:
                    questHelp_achievement_check(questHelpName)
                del questHelpData[questCategory][idx]
                questHelpData[questCategory].append([questHelpName, status])

                if questCategory in questHelpCategoriesHistory: questHelpCategoriesHistory.remove(questCategory)
                questHelpCategoriesHistory.append(questCategory)
                if questCategory not in questHelpCategoriesHistoryStatic: questHelpCategoriesHistoryStatic.append(questCategory)
                return
        if questCategory in questHelpCategoriesHistory: questHelpCategoriesHistory.remove(questCategory)
        questHelpCategoriesHistory.append(questCategory)
        if questCategory not in questHelpCategoriesHistoryStatic: questHelpCategoriesHistoryStatic.append(questCategory)
        questHelpData[questCategory].append([questHelpName, status])
        if day > 0 and questHelpActivated == True:
            notif(t__("Список событий обновлен"))
            questHelpJustUpdated = True
            questHelpUpdatedDay = day
        return

    def questHelpRemove(questName):
        global questHelpDataQuests, questHelpData, questHelpJustUpdated, questHelpUpdatedDay, day
        for questCategory in questHelpData:
            for idx in range(len(questHelpData[questCategory])-1, -1, -1):
                if questHelpData[questCategory][idx][0] == questName:
                    del questHelpData[questCategory][idx]
        return

    def questHelpGetQuestsAmount():
        global questHelpDataQuests, questHelpData, questHelpJustUpdated, questHelpUpdatedDay, day
        questsAmount = 0
        for questCategory in questHelpData:
            for idx in range(len(questHelpData[questCategory])-1, -1, -1):
                if questHelpData[questCategory][idx][1] == 0:
                    questsAmount += 1
        return questsAmount

    def questsCompleteByCategory(questCategory):
        if questHelpData.has_key(questCategory) == True:
            for idx in range(len(questHelpData[questCategory])-1, -1, -1):
                if questHelpData[questCategory][idx][1] == 0:
                    questHelpData[questCategory][idx][1] = 1

    def questsFailByCategory(questCategory):
        if questHelpData.has_key(questCategory) == True:
            for idx in range(len(questHelpData[questCategory])-1, -1, -1):
                if questHelpData[questCategory][idx][1] == 0:
                    questHelpData[questCategory][idx][1] = -1


    def questHelpDesc(*args): #questHelpDescriptionName, True/False, либо нет аргумента, значит True
        global questHelpDataCategoriesDescriptions, questHelpDataCategoriesDescriptionsData
        questHelpDescriptionName = args[0]
        if len(args) > 1:
            if isinstance(args[1], (int, float)) == False:
#            if isinstance(args[1], str) == True:
                questHelpDesc(args[0], False)
                questHelpDesc(args[1], True)
                return
            status = args[1]
        else:
            status = True
        if status == True:
            questHelpDataCategoriesDescriptionsData[questHelpDescriptionName] = status
        else:
            if questHelpDataCategoriesDescriptionsData.has_key(questHelpDescriptionName) == True:
                del questHelpDataCategoriesDescriptionsData[questHelpDescriptionName]
        return
