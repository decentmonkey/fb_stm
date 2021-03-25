#0 01 - Ползет (перемещается)
#1 02 - Еда
#2 03 - Потягушки от удовольствия (доработать руки как лапки). Когда хвалят или говорят что-то хорошее про тебя (чешут за ухом), то кошка должна показывать как она рада и предлагать себя.
#3 04 - Кошка спит (когда кошка спит, она должна лежать на спине в позе, удобной для того, если кто-то захочет воспользоваться ей во сне)
#4 06 - Кошка провинилась, просит прощения. Ласкает ботинки.
#5 07 - Покажи себя. Должна сразу вставать в эту позу.
#6 08 - Команда кошка просыпается. Тянется.
#7 09 - Играет с игрушкой
#8 10 - Ждет команду. Либо ждет после команды брысь.
#9 11 - Просит разрешения покушать. (без разрешения кушать нельзя)

default marcusCatTrainingButtons = ["Marcus_Cat_Command_01", "Marcus_Cat_Command_02", "Marcus_Cat_Command_03", "Marcus_Cat_Command_04", "Marcus_Cat_Command_06", "Marcus_Cat_Command_07", "Marcus_Cat_Command_08", "Marcus_Cat_Command_09", "Marcus_Cat_Command_10", "Marcus_Cat_Command_11"]

label ep213_police_marcus_day2:
    # Маркус день 1
    call ep213_dialogues_marcus1() from _rcall_ep213_dialogues_marcus1
    if _return == False:
        call ep213_dialogues_marcus5() from _rcall_ep213_dialogues_marcus5

    return
label ep213_police_marcus_day3:
    # Маркус день 2
    call ep213_dialogues_marcus2() from _rcall_ep213_dialogues_marcus2
    return

label ep213_police_marcus_day4:
    call ep213_dialogues_marcus3() from _rcall_ep213_dialogues_marcus3
    return

label ep213_police_marcus_day5:
    call ep213_dialogues_marcus4() from _rcall_ep213_dialogues_marcus4
    return
