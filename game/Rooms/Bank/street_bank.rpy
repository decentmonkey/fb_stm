label street_bank:

    $ print "enter_street_bank"
    $ miniMapData = []

    $ sceneIsStreet = True
    $ scene_image = "scene_Bank_Street[day_suffix]"
    $ scene_sound = "streets_sound"
    return

label street_bank_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"Bank_Street_Monica_[cloth][day_suffix]", "click" : "street_bank_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Traffic_Light", {"type":2, "base":"Bank_Street_Traffic_Light", "click" : "street_bank_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Bank_Green", {"type":2, "base":"Bank_Street_Bank_Green", "click" : "street_bank_environment", "actions" : "l", "zorder" : 0, "b":0.2})
    $ add_object_to_scene("Building", {"type":2, "base":"Bank_Street_Building", "click" : "street_bank_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Bank_Street_Teleport_Inside", "click" : "street_bank_teleport", "actions" : "lw", "zorder" : 1, "b":0.12, "teleport":True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_bank_teleport:
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Это мой банк!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Сейчас вечер. Банк уже закрыт."
                return
            if cloth == "CasualDress1":
                call ep25_dialogues1_shop17() from _call_ep25_dialogues1_shop17
                return
            mt "Что мне там делать?"
            "У меня нет никаких документов!"
            "(хмык)"
#            call change_scene("bank_office", "Fade_long")
            return
    return
label street_bank_environment:
    if obj_name == "Traffic_Light":
        m "Светофор?"
    if obj_name == "Bank_Green":
        m "Bank Green..."
    if obj_name == "Building":
        m "Это зеленое здание.
        В нем должен быть мой банк."
    if obj_name == "Monica":
        mt "На этой оживленной улице находится мой банк..."
        "Но мне он сейчас ни к чему..."
        "У меня нет никаких документов!"
        "(хмык)"
        return

    return
