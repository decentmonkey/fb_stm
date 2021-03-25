default streetJuliaHomeMonicaSuffix = 1
default streetJuliaHomeJuliaSuffix = 1

label street_juliahome:
    $ print "enter_street_juliahome"
    $ miniMapData = []
    if ep216_juliahome_blocked_day < day:
        call miniMapJuliaHomeGenerate() from _rcall_miniMapJuliaHomeGenerate_4

    $ sceneIsStreet = True

    $ scene_image = "scene_Street_JuliaHome[day_suffix]"
    if day_time == "day":
        music street4
    else:
        if rand(1,4) > 1:
            music street_evening3
        else:
            music street13_ambulance

    if streetJuliaHomeMonicaSuffix == 1 and get_active_objects("Julia", scene="street_juliahome") != False:
        $ move_object("Julia", "empty")
    if cloth != "CasualDress1" and streetJuliaHomeMonicaSuffix == 2 and get_active_objects("Julia", scene="street_juliahome") != False:
        $ move_object("Julia", "empty")
        $ streetJuliaHomeMonicaSuffix = 1
    return


label street_juliahome_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_JuliaHome_Monica_[cloth]_[streetJuliaHomeMonicaSuffix][day_suffix]", "click" : "street_juliahome_environment", "actions" : "l", "zorder" : 10}, scene="street_juliahome")
    $ add_object_to_scene("Julia", {"type":2, "base":"Street_JuliaHome_Julia_[streetJuliaHomeJuliaSuffix][day_suffix]", "click" : "street_juliahome_environment", "actions" : "lt", "zorder" : 5, "active":False}, scene="street_juliahome")

    $ add_object_to_scene("JuliaHome", {"type":2, "base":"Street_JuliaHome_JuliaHome", "click" : "street_juliahome_teleport", "actions" : "lw", "zorder" : 0, "group":"environment", "teleport":True, "active":False, "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]}, scene="street_juliahome")
    $ add_object_to_scene("JuliaCafe", {"type":2, "base":"Street_JuliaHome_Cafe", "click" : "street_juliahome_teleport", "actions" : "lw", "zorder" : 0, "group":"environment", "teleport":True, "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]}, scene="street_juliahome")

    $ add_object_to_scene("Teleport_StreetCorner", {"type":3, "text" : t_("УГОЛ УЛИЦЫ"), "larrow" : "arrow_right_2", "base":"Street_JuliaHome_Teleport_StreetEdge", "click" : "street_juliahome_teleport", "xpos" : 1613, "ypos" : 1003, "zorder":15, "teleport":True}, scene="street_juliahome")
    return

label street_juliahome_teleport:
    if obj_name == "Teleport_StreetCorner":
        if cloth_type == "Nude":
            call change_scene("street_corner", "Fade", "snd_walk_barefoot") from _rcall_change_scene_69
            return
        call change_scene("street_corner", "Fade", "highheels_run2") from _rcall_change_scene_70
        return
    return

label street_juliahome_environment:
    if obj_name == "Monica":
        mt "Здесь живет Юлия..."
    return
