label splashscreen:
    call init_launch() from _rcall_init_launch
    if debugMode == True:
        return

    scene black
#    image videoIntro_Video = Movie(play="video/Intro_Video.webm", fps=30)
#    show videoIntro_Video
#    $ renpy.pause(2.0, hard=True)
#    $ renpy.pause(68.0)
#    stop music fadeout 0.5
    img black_screen
    with Dissolve(0.5)
    img decentmonkey_logo
    with Dissolve(0.7)
    $ renpy.pause(1.0)
    pause 4.0
    img black_screen
    with Dissolve(0.7)
    img black_screen
    with Dissolve(0.5)
    img all_over_18
    with Dissolve(0.7)
    $ renpy.pause(2.0)

    img black_screen
    with Dissolve(0.5)
#    img Patreon_Game_Logo
#    with Dissolve(0.7)
#    $ renpy.pause(1.0, hard=True)
#    pause 4.0
#    img black_screen
    $ renpy.pause(2.0)


    return

    wclean
    img decentmonkey_logo
    with fade
    pause 3.0
    img all_over_18
    with fade
    pause 3.0
    scene black
    with dissolve
    return
