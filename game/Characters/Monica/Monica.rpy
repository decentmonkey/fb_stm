default monicaCumInside = 0 # Сколько раз кончили внутрь Моники
default monicaEatedLastDay = 0
default monicaEatedLastDayTime = "day"
default monicaFoodInventory = {} #какая еда есть у Моники с собой
default monicaFoodInventoryBasement = {} #какая еда лежит на столе в спальне в подвале

#define monicaCantSleepHungry = True
define monicaCantSleepHungry2 = True

default monicaWorkingAsDishwasher = False
default monica_pub_name = False

default monicaCleaningRoomsAmount = 2
default monicaCleaningInProgress = False
default monicaCleaningObject = ""

default monicaLastCleaningCompletedDay = 0 #Последний день, когда Моника убиралась в доме
default monicaLastCleaningOfferedDay = -1 #День, когда Монике предлагалась уборка в доме (предлагается один раз в день)

default monicaLastPissedDay = 0 # Последний день, когда Моника писала
default monicaLastPissedDayTime = "day"
default monicaLastShowerDay = 0 # Последний день, когда Моника принимала душ
default monicaLastShowerDayTime = ""

default monicaStoleFoodGasStationAmount = 0
default monicaStoleFoodTotal = 0
default monicaKebabWorkAmount = 0

default melanieOffended2 = False # Моника съязвила Мелани в фотостудии при встрече после Бифа
default monicaTalkedToMelanie1 = False
default monicaTryToDickBlowjob = False # Моника пыталась сделать Дику миньет

default hotelStaffOffended1 = False # Моника ругалась на hotelStaff за то что постер с ее изображением заслонен одеждой

default monicaOfferedBlowjobForBigMoney = False #Моника предложила сделать минет за $30 млн
default monicaOfferedBlowjobAgain = False #Моника предложила Филиппу сделать минет еще раз


default monicaMadeBlowjobToPhilip = False
default monicaMadeBlowjobToHotelStaff = False
default monicaSaidBiffSheIsWillBeAGoodChick = False

default monicaVictoriaKissHeels = False
default monicaVictoriaLickAssAtBegin = False

default monicaHasSexWithSteveBasement = False # У Моники был секс со Стивом в подвале
default monicaSteveLivingRoomOffended = False # Моника угрожала Стиву вилкой
default monicaSteveBasementOffended = False # Моника толкнула Стива в бассейн

default monicaUnder = "Governess"
default monicaPussyShaved = False
default monicaBettyPanties = False
default monicaBettyPantiesId = 1
default monicaMustWearBettyPanties = False
default monicaMustNotWearPanties = False

default monicaLaundryBettyPantiesSelectMode = 0
default monicaLaundryBettyPantiesSelectNudeDisabled = False

label monicaEat: #кормим Монику
    $ monicaEatedLastDay = day #кормим Монику
    $ monicaEatedLastDayTime = day_time
    return
