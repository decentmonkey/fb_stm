default pubBar1MonicaSuffix = 1
default pubBar1BartenderSuffix = 1
default pubBar1BartenderWaitressSuffix = 1

label pub_bar1:
    $ print "enter_pub_bar"
    $ miniMapData = []

    $ scene_image = "scene_pub_bar1"

    return
label pub_bar1_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"pub_bar1_Monica_Washing[pubBar1MonicaSuffix]_[cloth]", "click" : "pub_environment", "actions" : "l", "zorder" : 10}, scene="pub_bar1")
#    $ add_object_to_scene("Teleport_pub_Door", {"type":2, "base":"pub_Teleport_pub2", "click" : "pub_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True})

    $ add_object_to_scene("Bartender", {"type" : 2, "base" : "Pub_Bar1_Bartender[pubBartenderSuffix]", "click" : "pub_environment", "actions" : "l", "zorder":30, "icon_t":"/Icons/talk" + res.suffix +".png"}, scene="pub_bar1")
    $ add_object_to_scene("Bartender_Waitress", {"type" : 2, "base" : "Pub_Bar1_Bartender_Waitress[pubBartenderSuffix]", "click" : "pub_environment", "actions" : "l", "zorder":30}, scene="pub_bar1")
    $ add_object_to_scene("Pub_Bar1_Washbasin", {"type" : 2, "base" : "Pub_Bar1_Washbasin", "click" : "pub_environment", "actions" : "l", "zorder":0, "group":"environment"}, scene="pub_bar1")

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label pub_bar1_teleport:
    return
label pub_bar1_environment:
    if obj_name == "Bartender":
        if act=="l":
            mt "Это Джо. Он дал мне работу посудомойщицей."
            mt "Это ужас, конечно, но, по крайней мере, у меня есть еда..."
    if obj_name == "Bartender_Waitress":
        if act=="l":
            mt "Это Эшли. Жена Джо."
            mt "Мне кажется что она немного странная."
            mt "Хотя что может быть не странного в этой дыре?!"

    if obj_name == "Monica":
        mt "Какое жуткое место!"
        "Я даже представить себе не могла что могу оказаться в подобном заведении!"


    return
