
default tt = Tooltip("")
define maxBitchness = 560
define maxBitchness_EP1 = 560
default monicaBitch = False
define m = Character(t_("Моника Бакфетт"), who_color=c_orange, what_color=c_white, what_italic=False) #Monica
define mt = Character(kind=m, what_color=c_blue, what_italic=True) #Monica thinking
#define narrator = Character(kind=m)

define help = Character(t_("HELP"), who_color=c_blue) #helper in intro
define julia = Character(t_("Юлия"), who_color=c_pink) #Julia Governess
define fred = Character(t_("Водитель Фред"), who_color=c_blue) #Fred
define neighbor = Character(t_("Сосед"), who_color=c_green) #Neighbor
define gray_mouse = Character(t_("Серая мышь"), who_color=c_gray) #Gray Mouse
define secretary = Character(t_("Секретарша"), who_color=c_pink) #Monica Secretary
define secretary_t = Character(t_("Секретарша"), who_color=c_pink, what_color=c_blue, what_italic=True) #Monica Secretary thinking
define steve = Character(t_("Партнер Стив"), who_color=c_blue) #Parthner Steve
define model1 = Character(t_("Кастинг модель 1"), who_color=c_pink) #Casting Model 1
define model2 = Character(t_("Кастинг модель 2"), who_color=c_pink) #Casting Model 2
define alex_photograph = Character(t_("Фотограф Алекс"), who_color=c_green) #Alex Photograph
define melanie = Character(t_("Модель Мелани"), who_color=c_pink) #Melanie Model
define melanie_t = Character(t_("Модель Мелани"), who_color=c_pink, what_color=c_blue, what_italic=True) #Melanie Model thinking
define dick = Character(t_("Дик Адвокат"), who_color=c_green) #Dick The Lawyer
define dick2 = Character(t_("Дик Адвокат"), who_color=c_red) #Dick The Lawyer
define saleswoman = Character(t_("Кристина"), who_color=c_pink) #Saleswoman
define saleswoman_boss = Character(t_("Босс"), who_color=c_orange) #Saleswoman Boss
define cashier = Character(t_("Продавщица"), who_color=c_pink) #Clothing Shop Saler
define waitress = Character(t_("Официантка"), who_color=c_green) #Waitress
define bartender = Character(t_("Бармен"), who_color=c_blue) #Bartender
define fitness_instructor = Character(t_("Фитнесс-инструктор"), who_color=c_blue) #Fitness Instructor
define rebecca = Character(t_("Ребекка"), who_color=c_green) #Rebecca
define stephanie = Character(t_("Стефани"), who_color=c_pink) #Stephanie
define bank_clerk = Character(t_("Банковский Клерк"), who_color=c_pink) #Bank Clerk
define jane = Character(t_("Секретарша Джейн"), who_color=c_pink) #Jane Secretary
define tiffany = Character(t_("Тиффани"), who_color=c_pink) #Tiffany
define mommy = Character(t_("Мамочка"), who_color=c_red) #Mommy
define shawarma = Character(t_("Продавец шавермы"), who_color=c_green) #Kebab saler
define marcus = Character(t_("Маркус"), who_color=c_red) #Marcus
define husband = Character(t_("Супруг"), who_color=c_green) #Husband
define policewoman = Character(t_("Полицейская"), who_color=c_red) #Policewoman
define policeman = Character(t_("Полицейский"), who_color=c_red) #Policeman
define policeman1 = Character(t_("Полицейский 1"), who_color=c_red) #Policeman
define policeman2 = Character(t_("Полицейский 2"), who_color=c_red) #Policeman
define detective = Character(t_("Детектив"), who_color=c_red) #Detective
define overseer = Character(t_("Надзиратель"), who_color=c_red) #Overseer
define prisoner = Character(t_("Заключенный"), who_color=c_blue) #Prisoner
define prisoner1 = Character(t_("Заключенный 1"), who_color=c_red) #Prisoner
define prisoner2 = Character(t_("Заключенный 2"), who_color=c_red) #Prisoner
define prisoner3 = Character(t_("Заключенный 3"), who_color=c_red) #Prisoner
define prisoner4 = Character(t_("Заключенный 4"), who_color=c_red) #Prisoner
define prisoner5 = Character(t_("Заключенный 5"), who_color=c_red) #Prisoner
define prisoner6 = Character(t_("Заключенный 6"), who_color=c_red) #Prisoner
define prisoners = Character(t_("Заключенные"), who_color=c_red) #Prisoners
define judge = Character(t_("Судья"), who_color=c_blue) #Judge
define reception_secretary = Character(t_("Секретарь на рецепшине"), who_color=c_pink) #Reception Secretary
define reception_secretary_t = Character(t_("Секретарь на рецепшине"), who_color=c_pink, what_color=c_blue, what_italic=True) #Reception Secretary
define reception = Character(t_("Рецепшин Администратор"), who_color=c_pink) #Reception Administrator
define reception_t = Character(t_("Рецепшин Администратор"), who_color=c_pink) #Reception Administrator
define house_guard = Character(t_("Охранник"), who_color=c_red) #Guard
define dick_secretary = Character(t_("Секретарша Дика"), who_color=c_red) #Dick Secretary
define victoria = Character(t_("Секретарша Дика"), who_color=c_red) #Dick Secretary
define perry = Character(t_("Перри"), who_color=c_green) #Perry
define ralph = Character(t_("Ральф Робертс"), who_color=c_green) #Ralph Roberts
define biff = Character(t_("Биф"), who_color=c_blue) #biff
define betty = Character(t_("Бетти Робертс"), who_color=c_pink) #Betty Roberts
define betty_t = Character(t_("Бетти Робертс"), who_color=c_pink, what_color=c_blue, what_italic=True) #Betty Roberts
define bardie = Character(t_("Барди"), who_color=c_blue) #Bardie
define bardie_t = Character(t_("Барди"), who_color=c_blue, what_color=c_blue, what_italic=True) #Bardie
define eric = Character(t_("Эрик"), who_color=c_green) #Eric
define eric_t = Character(t_("Эрик"), who_color=c_green, what_color=c_blue, what_italic=True) #Eric

define gas_boyfriend = Character(t_("Бойфренд"), who_color=c_blue) #бойфренд девушки с заправки
define hotel_staff = Character(t_("Сотрудник Отеля"), who_color=c_blue) #сотрудник отеля
define philip = Character(t_("Филипп"), who_color=c_blue) #Philip
define empty_name = Character("", who_color=c_blue) #empty name

define teacher = Character(t_("Мистер Эдвардс"), who_color=c_blue) #Teacher Edwards
define mansfield = Character(t_("Мисс Менсфилд"), who_color=c_pink) #Mansfield
define clare = Character(t_("Клэр"), who_color=c_green) #Mansfield
define stripper = Character(t_("Стриптизерша"), who_color=c_red) #Molly unknown
define molly = Character(t_("Молли"), who_color=c_red) #Molly unknown

define reporter1 = Character(t_("Репортер 1"), who_color=c_blue) #Reporter1
define reporter2 = Character(t_("Репортер 2"), who_color=c_orange) #Reporter2
define reporter3 = Character(t_("Репортер 3"), who_color=c_pink) #Reporter3

define citizen = Character(t_("Незнакомец"), who_color=c_pink) #Stranger
define citizen1 = Character(t_("Том"), who_color=c_pink) #Stranger
define citizen2 = Character(t_("Тим"), who_color=c_pink) #Stranger
define citizen3 = Character(t_("Джек"), who_color=c_orange) #Stranger
define citizen4 = Character(t_("Незнакомец"), who_color=c_blue) #Stranger
define citizen5 = Character(t_("Акира Сан"), who_color=c_blue) #Stranger
define citizen6 = Character(t_("Фил"), who_color=c_blue) #Stranger
define citizen7 = Character(t_("Сальвадор"), who_color=c_pink) #Stranger
define citizen8 = Character(t_("Хитрый Джонни"), who_color=c_blue) #Stranger
define citizen9 = Character(t_("Найджел"), who_color=c_green) #Stranger
define citizen10 = Character(t_("Реджинальд"), who_color=c_blue) #Stranger
define citizen11 = Character(t_("Саймон"), who_color=c_blue) #Stranger
define citizen12 = Character(t_("Незнакомец"), who_color=c_green) #Stranger
define citizen13 = Character(t_("Анджело"), who_color=c_pink) #Stranger
define citizen14 = Character(t_("Василий"), who_color=c_orange) #Stranger
define citizen15 = Character(t_("Френк"), who_color=c_blue) #Stranger

define ashley = Character(t_("Эшли"), who_color=c_pink) # Барменша
define joe = Character(t_("Джо"), who_color=c_blue) # Бармен

define sound_from_side = Character(t_("Звук"), who_color=c_blue)

define cit1 = Character(t_("Покупатель"), who_color=c_blue)
define cit2 = Character(t_("Покупатель"), who_color=c_blue)
define cit3 = Character(t_("Покупатель"), who_color=c_blue)
define cit4 = Character(t_("Покупательница"), who_color=c_pink)
define cit5 = Character(t_("Покупательница"), who_color=c_pink)
define cit6 = Character(t_("Покупательница"), who_color=c_pink)
define cit7 = Character(t_("Покупательница"), who_color=c_pink)
define cit8 = Character(t_("Покупательница"), who_color=c_pink)
define cit9 = Character(t_("Покупательница"), who_color=c_pink)
define cit10 = Character(t_("Покупательница"), who_color=c_pink)


define w1 = Character(t_("Марта"), who_color=c_pink)
define w1t = Character(t_("Марта"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w2 = Character(t_("Системный Администратор"), who_color=c_blue)
define w2t = Character(t_("Системный Администратор"), who_color=c_blue, what_color=c_blue, what_italic=True)
define w3 = Character(t_("Эмма"), who_color=c_pink)
define w3t = Character(t_("Эмма"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w4 = Character(t_("Элла"), who_color=c_pink)
define w4t = Character(t_("Элла"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w5 = Character(t_("Джон"), who_color=c_blue)
define w5t = Character(t_("Джон"), who_color=c_blue, what_color=c_blue, what_italic=True)
define w6 = Character(t_("Грета"), who_color=c_pink)
define w6t = Character(t_("Грета"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w7 = Character(t_("Лин"), who_color=c_pink)
define w7t = Character(t_("Лин"), who_color=c_pink, what_color=c_blue, what_italic=True)

define customer1 = Character(t_("Посетитель"), who_color=c_blue)
define customer1t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer2 = Character(t_("Посетитель"), who_color=c_blue)
define customer2t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer3 = Character(t_("Посетитель"), who_color=c_blue)
define customer3t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer4 = Character(t_("Посетитель"), who_color=c_blue)
define customer4t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer5 = Character(t_("Посетитель"), who_color=c_blue)
define customer5t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer6 = Character(t_("Посетитель"), who_color=c_blue)
define customer6t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer7 = Character(t_("Посетитель"), who_color=c_blue)
define customer7t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer8 = Character(t_("Посетитель"), who_color=c_blue)
define customer8t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer9 = Character(t_("Посетитель"), who_color=c_blue)
define customer9t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer10 = Character(t_("Посетитель"), who_color=c_blue)
define customer10t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer11 = Character(t_("Посетитель"), who_color=c_blue)
define customer11t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer12 = Character(t_("Посетитель"), who_color=c_blue)
define customer12t = Character(t_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)

define customers1 = Character(t_("Зритель"), who_color=c_blue)
define customers2 = Character(t_("Зритель"), who_color=c_orange)
define customers3 = Character(t_("Зритель"), who_color=c_red)
define customers4 = Character(t_("Зритель"), who_color=c_green)
define customers5 = Character(t_("Зритель"), who_color=c_pink)

define investor1 = Character(t_("Инвестор"), who_color=c_blue)
define investor2 = Character(t_("Инвестор"), who_color=c_blue)
define investor3 = Character(t_("Инвестор"), who_color=c_blue)
define investor4 = Character(t_("Инвестор"), who_color=c_blue)

define whore_number_1 = Character(t_("Шлюха номер 1"), who_color=c_pink)

define girl_1 = Character(t_("Девочка по вызову"), who_color=c_red)
define girl_2 = Character(t_("Девочка по вызову"), who_color=c_orange)
define girl_3 = Character(t_("Девочка по вызову"), who_color=c_green)
define girl_4 = Character(t_("Девочка по вызову"), who_color=c_pink)

define linda = Character(t_("Линда"), who_color=c_pink)

define cafe_visitor1 = Character(t_("Посетитель кафе"), who_color=c_blue)
define cafe_visitor2 = Character(t_("Посетитель кафе"), who_color=c_red)
define cafe_barista = Character(t_("Бариста"), who_color=c_pink)
#

define client = Character(t_("Клиент"), who_color=c_green)
define ned = Character(t_("Нэд"), who_color=c_green)
define ned2 = Character(t_("Нэд"), who_color=c_red)
define daniel = Character(t_("Дэниел"), who_color=c_blue)
define marty = Character(t_("Марти"), who_color=c_green)
define emma = Character(t_("Эмма"), who_color=c_orange)
define natalie = Character(t_("Натали"), who_color=c_pink)

define banker = Character(t_("Банкир"), who_color=c_green)

define guest1 = Character(t_("Миссис Уайт"), who_color=c_red)
define guest2 = Character(t_("Грейс"), who_color=c_pink)
define guest3 = Character(t_("Исаак"), who_color=c_green)
define guest4 = Character(t_("Райен"), who_color=c_blue)
define guest5 = Character(t_("Шарлотт"), who_color=c_red)
define guest6 = Character(t_("Мия"), who_color=c_pink)
define guest7 = Character(t_("Адриано"), who_color=c_blue)
define guest8 = Character(t_("Тернер"), who_color=c_green)
define campbell = Character(t_("Мистер Кэмпбэлл"), who_color=c_green)

define wife = Character(t_("Жена"), who_color=c_red)
define husband = Character(t_("Муж"), who_color=c_blue)

define whore = Character(t_("Шлюха"), who_color=c_pink)

define liam = Character(t_("Лиам"), who_color=c_green) #Neighbor Лиам

define olaf = Character(t_("Олаф"), who_color=c_blue)
define charlotte = Character(t_("Шарлотт"), who_color=c_red)
define mia = Character(t_("Мия"), who_color=c_pink)

define stranger = Character(t_("Незнакомец"), who_color=c_green) #stranger с веб-кам
