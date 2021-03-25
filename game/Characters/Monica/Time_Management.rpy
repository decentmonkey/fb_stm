label time_management_street_wait_until_evening:
    music stop
    music2 stop
    img black_screen
    with Dissolve(1.0)
    pause 0.5
    $ changeDayTime("evening")
    call refresh_scene("Fade_long") from _call_refresh_scene_11
    return
