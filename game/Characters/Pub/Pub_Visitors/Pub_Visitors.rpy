# z- index (первый-дальний)
# visitor3
# visitor8
# visitor7
# visitor1
# visitor6
# visitor11
# visitor2
# visitor10
# visitor9
# visitor12
# visitor5
# visitor4


label pub_visitors_default:
    if act=="l":
        mt "Очередной пьяница..."
        return
    mt "Не собираюсь к нему подходить!"
    "Мне противно это место!"
    return

label Pub_Visitors_RemoveAll: #Убрать всех посетителей
    python:
        set_active(False, group="visitors", scene="pub")
        pubVisitor1Suffix = ""
        pubVisitor2Suffix = ""
        pubVisitor3Suffix = ""
        pubVisitor4Suffix = ""
        pubVisitor5Suffix = ""
        pubVisitor6Suffix = ""
        pubVisitor7Suffix = ""
        pubVisitor8Suffix = ""
        pubVisitor9Suffix = ""
        pubVisitor10Suffix = ""
        pubVisitor11Suffix = ""
        pubVisitor12Suffix = ""
    return

label Pub_Visitors_Remove_Food: # Убрать еду у всех посетителей
    python:
        pubVisitor1Suffix = ""
        pubVisitor2Suffix = ""
        pubVisitor3Suffix = ""
        pubVisitor4Suffix = ""
        pubVisitor5Suffix = ""
        pubVisitor6Suffix = ""
        pubVisitor7Suffix = ""
        pubVisitor8Suffix = ""
        pubVisitor9Suffix = ""
        pubVisitor10Suffix = ""
        pubVisitor11Suffix = ""
        pubVisitor12Suffix = ""
    return
label Pub_Visitors_Full_Food: # Все посетители + у всех еда
#    $ set_active(True, group="visitors", scene="pub")
    python:
        pubVisitor1Suffix = "_Food"
        pubVisitor2Suffix = "_Food"
        pubVisitor3Suffix = "_Food"
        pubVisitor4Suffix = "_Food"
        pubVisitor5Suffix = "_Food"
        pubVisitor6Suffix = "_Food"
        pubVisitor7Suffix = "_Food"
        pubVisitor8Suffix = "_Food"
        pubVisitor9Suffix = "_Food"
        pubVisitor10Suffix = "_Food"
        pubVisitor11Suffix = "_Food"
        pubVisitor12Suffix = "_Food"

    return

label Pub_Visitors_CheckStripLooking:
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False or get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        $ set_active(True, group2="strip_lookers")
    else:
        $ set_active(False, group2="strip_lookers")
    return

label Pub_Visitors_Add_Random(from_amount, to_amount):
    $ visitorsAmount = rand(from_amount, to_amount)
    $ visitorsArr = get_objects(scene="pub", group2="visitors_tables")
    if visitorsArr == False:
        return
    $ activeVisitorsList = random.sample(visitorsArr, visitorsAmount)
    $ print "visitors"
    python:
        for visitorObj in activeVisitorsList:
            set_active(visitorObj[1], True, scene="pub")
            print visitorObj[1]
    return



















#
