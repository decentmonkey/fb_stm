default visitorsVisits = {}

default pubQueenCustomer1Count = 0
default pubQueenCustomer2Count = 0
default pubQueenCustomer3Count = 0
default pubQueenCustomer4Count = 0
default pubQueenCustomer5Count = 0
default pubQueenCustomer78Count = 0
default pubQueenCustomer9Count = 0
default pubQueenCustomer10Count = 0
default pubQueenCustomer11Count = 0
default pubQueenCustomer12Count = 0

default pubCustomersQueenList = []
default pubAfterBattleVisitorsServedAmount = 0

label ep27_pub_visitors_init:
    if get_pub_visitor_visits("Pub_Visitor9") > 0:
        $ pubVisitor9Suffix = "_Food"
    if get_pub_visitor_visits("Pub_Visitor10") > 0:
        $ pubVisitor9Suffix = "_Food"
    return

label ep27_pub_visitors_click:
    if act=="l":
        return
    if pubMonicaWaitressServedCustomersToday >= pubMonicaWaitressVisitorsPerDay:
        call ep27_dialogues7_pub3() from _call_ep27_dialogues7_pub3_1
        call ep27_dialogues7_pub3a() from _call_ep27_dialogues7_pub3a
        return False
    if obj_name in pubMonicaWaitressVisitorsServed:
        call ep27_dialogues7_pub19() from _call_ep27_dialogues7_pub19
        return False
    music2 pub_noise1_low
    $ visitsCount = get_pub_visitor_visits(obj_name)
    if obj_name == "Pub_Visitor1":
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer1_1stmeeting() from _call_customer1_1stmeeting
            # nofood
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer1_afterbattle() from _rcall_customer1_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor1")
                if _return == True:
                    $ pubVisitor1Suffix = "_Food"
            else:
                call customer1_serve1() from _call_customer1_serve1
                if _return == True:
                    $ pubVisitor1Suffix = "_Food"
        $ autorun_to_object("customer1_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor2":
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer2_1stmeeting() from _call_customer2_1stmeeting
            $ pubVisitor2Suffix = "_Food"
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer2_afterbattle() from _rcall_customer2_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor2")
                $ pubVisitor2Suffix = "_Food"
            else:
                call customer2_serve1() from _call_customer2_serve1
                $ pubVisitor2Suffix = "_Food"
        $ autorun_to_object("customer2_after_serve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor3":
        if monica_shiny_hole_queen_day > 0:
            call customer3_afterbattle() from _rcall_customer3_afterbattle
            $ pubCustomersQueenList.append("Pub_Visitor3")
            $ pubVisitor3Suffix = "_Food"
        else:
            if customer3_after_private == True:
                call ep212_dialogues2_shiny_hole_3() from _rcall_ep212_dialogues2_shiny_hole_3
                $ pubVisitor3Suffix = "_Food"
                if _return != False:
                    $ customer3_after_private_agree_count += 1
            else:
                if visitsCount == 0:
                    call customer3_1stmeeting() from _call_customer3_1stmeeting
                    $ pubVisitor3Suffix = "_Food"
                if visitsCount > 0:
                    if visitsCount%2 == 1:
                        call customer3_serve1() from _call_customer3_serve1
                        $ pubVisitor3Suffix = "_Food"
                    else:
                        call customer3_serve2() from _call_customer3_serve2
                        # nofood
        $ autorun_to_object("customer3_after_serve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor4":
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer4_1stmeeting() from _call_customer4_1stmeeting
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer4_afterbattle() from _rcall_customer4_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor4")
                $ pubVisitor4Suffix = "_Food"
            else:
                call customer4_serve1() from _call_customer4_serve1
                $ pubVisitor4Suffix = "_Food"
        $ autorun_to_object("customer4_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor5":
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer5_1stmeeting() from _call_customer5_1stmeeting
            $ pubVisitor5Suffix = "_Food"
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer5_afterbattle() from _rcall_customer5_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor5")
                $ pubVisitor5Suffix = "_Food"
            else:
                call customer5_serve1() from _call_customer5_serve1
                $ pubVisitor5Suffix = "_Food"
        $ autorun_to_object("customer5_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor6":
        call customer6_serve1() from _call_customer6_serve1
        $ pubCustomersQueenList.append("Pub_Visitor6")
        $ autorun_to_object("customer6_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor7" or obj_name == "Pub_Visitor8":
        $ visitsCount = get_pub_visitor_visits("Pub_Visitor7") + get_pub_visitor_visits("Pub_Visitor8")
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer78_1stmeeting() from _call_customer78_1stmeeting
            $ pubVisitor7Suffix = "_Food"
            $ pubVisitor8Suffix = "_Food"
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer78_afterbattle() from _rcall_customer78_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor7_8")
                $ pubVisitor7Suffix = "_Food"
                $ pubVisitor8Suffix = "_Food"
            else:
                call customer78_serve1() from _call_customer78_serve1
                $ pubVisitor7Suffix = "_Food"
                $ pubVisitor8Suffix = "_Food"
            $ autorun_to_object("customer78_afterserve1", scene=scene_name)

    if obj_name == "Pub_Visitor9":
        if visitsCount == 0 and customer9_after_private == False and monica_shiny_hole_queen_day == 0:
            call customer9_1stmeeting() from _call_customer9_1stmeeting
            $ autorun_to_object("customer9_afterserve1", scene=scene_name)
        if visitsCount > 0 or customer9_after_private == True or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer9_afterbattle() from _rcall_customer9_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor9")
                $ autorun_to_object("customer9_afterserve2", scene=scene_name)
            else:
                call customer9_serve1() from _call_customer9_serve1
                if _return == False:
                    $ autorun_to_object("customer9_afterserve1", scene=scene_name)
                else:
                    $ autorun_to_object("customer9_afterserve2", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor10":
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer10_1stmeeting() from _call_customer10_1stmeeting
            $ pubVisitor10Suffix = "_Food"
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer10_afterbattle() from _rcall_customer10_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor10")
#                $ pubVisitor10Suffix = "_Food"
            else:
                call customer10_serve1() from _call_customer10_serve1
        $ autorun_to_object("customer10_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor11":
        if monica_shiny_hole_queen_day > 0:
            call customer11_afterbattle() from _rcall_customer11_afterbattle
            $ pubCustomersQueenList.append("Pub_Visitor11")
            if _return != False:
                $ pubVisitor11Suffix = "_Food"
        else:
            call customer11_1stmeeting() from _call_customer11_1stmeeting
            $ pubVisitor11Suffix = "_Food"
    if obj_name == "Pub_Visitor12":
        if visitsCount == 0 and monica_shiny_hole_queen_day == 0:
            call customer12_1stmeeting() from _call_customer12_1stmeeting
        if visitsCount > 0 or monica_shiny_hole_queen_day > 0:
            if monica_shiny_hole_queen_day > 0:
                call customer12_afterbattle() from _rcall_customer12_afterbattle
                $ pubCustomersQueenList.append("Pub_Visitor12")
            else:
                call customer12_serve1() from _call_customer12_serve1
            $ pubVisitor12Suffix = "_Food"
        $ autorun_to_object("customer12_afterserve1", scene=scene_name)
        pass

    if monica_shiny_hole_queen_day > 0:
        $ pubCustomersQueenListUniq = set(pubCustomersQueenList)
        $ pubAfterBattleVisitorsServedAmount = len(pubCustomersQueenListUniq)
        if pubAfterBattleVisitorsServedAmount >= 3:
            $ questHelp("shinyhole_58", True)
    $ pubMonicaWaitressVisitorsServed.append(obj_name)
    $ increment_pub_visitor_visits(obj_name)
    $ pubMonicaWaitressServedCustomersToday += 1
    $ pubMonicaWaitressServedCustomersTotal += 1
    if pubMonicaWaitressServedCustomersToday >= pubMonicaWaitressVisitorsPerDay:
        if day_time == "day":
            $ changeDayTime("evening") # Если закончили, упершись в лимит клиентов, то меняем время суток
#        $ autorun_to_object("ep27_pub_visitors_dummy_autorun", scene=scene_name)
        $ autorun_to_object("ep27_dialogues7_pub3b", scene=scene_name)
        $ questHelp("shinyhole_5", True)
        $ questHelp("shinyhole_6", skipIfExists=True)
#        call ep27_quests_pub_work5() # Заканчиваем работу
        return False
    $ scene_sound = "highheels_short_walk"
    call refresh_scene_fade() from _call_refresh_scene_fade_170
    return False

label ep27_pub_visitors_dummy_autorun:
    return

init python:
    def get_pub_visitor_visits(obj_name):
        global visitorsVisits
        if visitorsVisits.has_key(obj_name):
            return visitorsVisits[obj_name]
        return 0

    def increment_pub_visitor_visits(obj_name):
        global visitorsVisits
        if visitorsVisits.has_key(obj_name):
            visitorsVisits[obj_name] += 1
        else:
            visitorsVisits[obj_name] = 1
        return

    def add_tips(amount):
        global pubMonicaWaitressTips
        pubMonicaWaitressTips += amount
        add_money(amount)
        return
