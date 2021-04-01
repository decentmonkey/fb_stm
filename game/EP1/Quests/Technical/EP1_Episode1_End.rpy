label EP1_episode1End:
#    $ _dismiss_pause = False
    img black_screen
    with Dissolve(2.0)
    img 3371
    with fadelong
    mt "Я так устала."
    img 3372
    with fadelong
    "Я хочу спать..."
    img 3373
    with Dissolve(8.0)
#    show black at credits_black_overlay
#    call EP1_credits
    $ renpy.pause(3.0, hard = True)
    pause
#    hide screen show_image_screen
    $ EP1_skipintro = True
#    hide screen credits_screen
    fadeblack 2.0


#    $ cloth_type = "Nude"
#    $ cloth = "GovernessPants"

    jump startfromep1
    $ renpy.pause(gui.credits.timeout, hard=True)
#    $ renpy.pause()
#    $ _dismiss_pause = True
    stop music fadeout 1.0
    $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
#    help "the end"
    return

label EP1_episode1End_Dick:
#    music beautiful_messenger_piano
#    $ _dismiss_pause = False
    img 5765
    with Dissolve(5.0)
#    $ renpy.pause(3.0)
    with Dissolve(8.0)
    show black at credits_black_overlay
    call EP1_credits
    $ renpy.pause(5.0, hard = True)
#    hide screen show_image_screen
    $ renpy.pause(gui.credits.timeout, hard=True)
#    $ renpy.pause()
#    $ _dismiss_pause = True
    stop music fadeout 1.0
    $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
    return

init python:

    credits = [(2, "IDEA"),
    (3, "DecentMonkey"),
    (0, ""),
    (0, ""),
    (2, "SCREENPLAY"),
    (3, "DecentMonkey"),
    (0, ""),
    (0, ""),
    (2, "TEXT AND DIALOGUES"),
    (3, "DecentMonkey"),
    (0, ""),
    (0, ""),
    (2, "PROGRAMMING"),
    (3, "DecentMonkey"),
    (0, ""),
    (0, ""),
    (2, "GERMAN TRANSLATION AND GLOBAL SUPPORT"),
    (3, "Ragnaroekr"),
    (0, ""),
    (0, ""),
    (2, "TEXT CORRECTION"),
    (3, "Aesthetic Dialectic"),
    (3, "ColdBlade"),
    (3, "Meli_x3"),
    (0, ""),
    (0, ""),
    (2, "SPANISH TRANSLATION"),
    (3, "Lupita"),
    (0, ""),
    (0, ""),
    (2, "CHINESE TRANSLATION"),
    (3, "coolyama_ru"),
    (0, ""),
    (0, ""),

    (2, "ITALIAN TRANSLATION"),
    (3, "snake"),
    (0, ""),
    (0, ""),

    (2, "TURKISH TRANSLATION"),
    (3, "Yossarian"),
    (0, ""),
    (0, ""),

    (2, "FRENCH TRANSLATION"),
    (3, "YoyoRTx"),
    (0, ""),
    (0, ""),

    (2, "GAME ENGINE"),
    (3, "Ren'Py"),
    (0, ""),
    (0, ""),
    (2, "RENDER CHARACTERS"),
    (3, "DAZ3D"),
    (0, ""),
    (0, ""),
    (2, "RENDER ENVIRONMENT"),
    (3, "3DS MAX"),
    (0, ""),
    (0, ""),
    (2, "RENDER ENGINE"),
    (3, "Corona Renderer"),
    (0, ""),
    (0, ""),
    (0, ""),
    (0, ""),
    (3, "CAST"),
    (0, ""),
    (4, "MONICA", "AS SHESELF"),
    (4, "BETTY ROBERTS", "Maryann BY Addy"),
    (4, "JULIA", "Amina BY Anagord"),
    (4, "SECRETARY", "Greer BY AliveSheCried"),
    (4, "CLOTHING STORE SALESWOMAN", "Kelly BY Raiya"),
    (4, "BANK CLERK 1", "Jenna BY Aquarius"),
    (4, "BANK CLERK 2", "Maggy BY OziChick"),
    (4, "LA GRAND RECEPTION", "Chen Ting BY Dyys3d"),
    (4, "PERRY", "Ej Etta BY EmmaAndJordi"),
    (4, "DICK SECRETARY", "Lilah BY P3Design"),
    (4, "CASTING MODEL 1", "Hope BY Most Digital Creations"),
    (4, "CASTING MODEL 2", "Heather BY Most Digital Creations"),
    (4, "MELANIE SUPERMODEL", "Pepper BY Addy"),
    (4, "OIL SALESWOMAN", "Pink BY Spows"),
    (4, "JANE SECRETARY", "Rowan BY Rhiannon"),
    (4, "TIFFANY", "Arianna BY Exnem"),
    (4, "RESTAURANT WAITRESS", "Dara BY Gypsyangel"),
    (4, "GIRLFRIEND REBECCA", "Jolina BY Raiya"),
    (4, "GIRLFRIEND STEPHANIE", "Josina BY P3Design"),
    (4, "MOMMY", "Mother BY Anain & AkashaBloodRiver"),
    (4, "FANCY LADY", "Rhona BY Brahann"),
    (4, "RALPH ROBERTS", "Dale BY Saiyaness"),
    (4, "BARDIE ROBERTS", "Curro BY Anain & AkashaBloodRiver"),
    (4, "STEVE", "Old Chap BY Kayleyss"),
    (4, "POLICEMAN 1", "Brett BY Daz Originals & Fred Winkler Art"),
    (4, "POLICEMAN 2", "Felipe BY Daz Originals & Fred Winkler Art"),
    (4, "FITNESS INSTRUCTOR", "Malachai BY Darwins Mishap(s)"),
    (4, "GROCERY STORE SALESMAN", "Roman BY Toyen"),
    (4, "ALEX PHOTOGRAPHER", "Diesel BY Darwins Mishap(s)"),
    (4, "POLICE DETECTIVE", "Dante BY Daz Originals"),
    (4, "OVERSEER", "AS HIMSELF"),
    (4, "DICK THE LAWYER", "George BY Deepsea"),
    (4, "NEIGHBOR", "Adama BY Samsil"),
    (4, "DRIVER FRED", "Ahmad BY Darwins Mishap(s)"),
    (4, "MARCUS", "Leo BY Daz Originals"),
    (4, "BARTENDER", "Jaque BY JavierMicheal"),
    (4, "SHAWARMA MAN", "Samanyo BY JavierMicheal"),
    (4, "OFFENDERS", "Xavier BY Daz Originals & Fred Winkler Art & Sabby"),
    (0, ""),
    (0, ""),
    (3, "MUSIC"),
    (2, " "),
    (2, "Dan O'Connor"),
    (1, " "),
    (1, "Jazz Remember The Stars"),
    (1, "Living The Daydream"),
    (1, "Beautiful Messenger - Piano"),
    (2, " "),
    (2, " "),
    (2, "Kevin MacLeod"),
    (1, " "),
    (1, "Stealth Groover"),
    (1, "Gagool"),
    (1, "Bossa Bossa"),
    (1, "Mandeville"),
    (1, "Pyro Flow"),
    (1, "DarxieLand"),
    (1, "Master Disorder"),
    (1, "Cheery Monday"),
    (1, "Villainous Treachery"),
    (1, "Gearhead"),
    (1, "ZigZag"),
    (1, "Molten Alloy"),
    (1, "Hidden Agenda"),
    (1, "Poppers and Prosecco"),
    (1, "In Your Arms"),
    (1, "Marty Gots A Plan"),
    (2, " "),
    (2, " "),
    (2, "Pascal Tatipata"),
    (1, " "),
    (1, "Walking Sax2"),
    (1, "All Stars"),
    (1, "RnB4_100"),
    (2, " "),
    (2, " "),
    (2, "DL Sounds"),
    (1, " "),
    (1, "Indo Rock"),
    (1, "Indo_Rock2"),
    (1, "Groove2_85"),
    (1, "Funk7_110"),
    (1, "Road Trip"),
    (1, "Funk Soul1"),
    (1, "Jazz Club1_130"),
    (1, "Power Bots"),
    (2, " "),
    (2, " "),
    (2, "Longzijun"),
    (1, " "),
    (1, "As Long As A Word Remains Unspoken"),
    (2, " "),
    (2, " "),
    (2, "Backgroundloop"),
    (1, " "),
    (1, "Rock'n'Roll"),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, "GREETINGS TO GREAT AUTHORS"),
    (2, " "),
    (2, "Terebonkoff Studios"),
    (1, " "),
    (2, "DarkSilver"),
    (1, " "),
    (2, "OldHunter"),
    (1, " "),
    (2, "ICSTOR"),
    (1, " "),
    (2, "Malleck"),
    (1, " "),
    (2, "DeepSleep"),
    (1, " "),
    (2, "3Diddly Games'n Comics"),
    (1, " "),
    (2, "Tremmi Games"),
    (1, " "),
    (2, "xRed"),
    (1, " "),
    (2, "AdultJunkie"),
    (1, " "),
    (2, "CaizerGames"),
    (1, " "),
    (2, "Zuleyka"),
    (1, " "),
    (2, "KosmosGames"),
    (3, " "),
    (3, " "),
    (3, " "),
    (2, "Greatest thanks to my best friend"),
    (3, "Dmitry"),
    (2, "for help and support during creation of this game."),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, "TO BE CONTINUED..."),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " "),
    (3, " ")
    ]

label EP1_credits:
    show screen credits_screen(credits)
#    $ renpy.pause()
    return