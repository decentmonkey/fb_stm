# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       softkeyboard.rpy [ソフトキーボード関数]
#                                                                                                       作成者:  Andrea Rubenstein
#                                                                                                       作成日 : 2011/10/15
#                                                                                                       更新日: 2011/10/16
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

init python:

##############################################################################
#       関数
##############################################################################

    # Alphabets for soft keyboard
    softkey = {}

##################################################
#　クラス名：SetAlphabet
#　説　明　：入力するアルファベットを設定する処理
##################################################
    def SetAlphabet(type,lang="en"):
        alphabet = []
        for column in softkey[lang][type]:
            alphabet.append(column)

        return alphabet

##################################################
#　クラス名：SwithCapsSingle
#　説　明　：アルファベットの大文字と小文字の変換処理
##################################################
    def SwitchCapsSingle(base,upper):
        switched = []
        for letter in base:
            if letter is not None:
                if upper:
                    switched.append(letter.upper())
                else:
                    switched.append(letter.lower())

        return switched

##################################################
#　クラス名：SwitchCaps
#　説　明　：アルファベットの大文字と小文字の変換処理
##################################################
    def SwitchCaps(base,upper):
        switched = []
        for array in base:
            switched.append(SwitchCapsSingle(array,upper))

        return switched

##################################################
#　クラス名：AddLetter
#　説　明　：文字を文字配列に入れる処理
##################################################
    def AddLetter(base,letter):
        base = base + letter
        if len(base) > INPUT_MAX:
            base = base[:-1]

        return base


##################################################
#　クラス名：ShiftDown
#　説　明　：小文字にする処理
##################################################
    def ShiftDown(base):
        if input_shift:
            return SwitchCaps(base,False)
        else:
            return base

#EOF


﻿# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       common.rpy [共有部分]
#                                                                                                       Author   :  Andrea Rubenstein
#                                                                                                       Created : 2011/10/15
#                                                                                                       Updated: 2011/10/16
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

##############################################################################
#       DEFAULTS
##############################################################################
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       english.rpy [English Soft Keyboard]
#                                                                                                       Author   :  Andrea Rubenstein
#                                                                                                       Created : 2011/10/14
#                                                                                                       Updated: 2011/10/16
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

init python:
    INPUT_MAX = 15
    INPUT_MARGIN = 15

    key_row = 5
    key_col = 8

    input_caps = False
    input_shift = False

    main_buttons = {}
    input_nav_buttons = {}

init python:

##############################################################################
#       KEYS
##############################################################################
    INPUT_VALUE_DEFAULT = "Marylin"
    INPUT_LABEL_DEFAULT = "Monica's name:"

    softkey_type = [{"alphabet" : "en"}, {"symbols" : "en"}]

    main_buttons["default"] = "Default"
    main_buttons["clear"] = "Clear"
    main_buttons["confirm"] = "OK"

    input_nav_buttons["alphabet"] = "ABC"
    input_nav_buttons["symbols"] = "123"

    softkey["en"] = {}
    softkey["en"]["alphabet"] = []
    softkey["en"]["alphabet"].append(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"])
    softkey["en"]["alphabet"].append(["à","á","â","ã","ä","å","æ","ç","è","é","ê","ë","ì","í","î","ï","ð","ñ","ò","ó","ô","õ","ö","ø","ù","ú","û","ü","ý","þ","ÿ"])

    softkey["en"]["symbols"] = []
    softkey["en"]["symbols"].append(["1","2","3","4","5","6","7","8","9","0","#","$","%","&","(",")",":",";",".",",","?","!","•",">","<","|","=","…","¡","¿","„","§","†","‡","±"])
    softkey["en"]["symbols"].append(["\'","\"","-","_","~","^","\\","/","★","☆","♀","♂","♥","♠","♣","♦","♪","♫","♭","♯","∞","™","©","®"])


##############################################################################
#       VARIABLES
##############################################################################
init python:
    input_value = "Marylin"
    input_label = "Monica's name:"
    input_keyboard = softkey_type[0].keys()[0]

    input_alphabet = SetAlphabet(input_keyboard)

    input_special = {}
    input_special["backspace"] = "←"
    input_special["space"] = "SPACE"
    input_special["caps"] = "CAPS"
    input_special["shift"] = "SHIFT"
    input_special["handakuten"] = "゜"
    input_special["dakuten"] = "゛"
    input_special["komoji"] = "小文字"


##############################################################################
#       SCREENS
##############################################################################
screen input_special_type:
    $col = key_col-2
    grid 1 col:
        if input_keyboard == "alphabet":
            textbutton input_special["caps"] action [ToggleVariable("input_caps"),SetVariable("input_alphabet", SwitchCaps(input_alphabet,not input_caps))] style "keyboard_button_special"
            textbutton input_special["shift"] action [ToggleVariable("input_shift"),SetVariable("input_alphabet", SwitchCaps(input_alphabet,not input_shift))] style "keyboard_button_special"
            for i in range(2,col):
                null
        else:
            for i in range(0,col):
                null

#EOF


##############################################################################
#       SCREENS
##############################################################################
screen input_softkeyboard:
    frame:
        xfill True
        yfill True
        style "input_softkeyboard"
        vbox:
            #area(xpos, ypos, width, height)
            area (INPUT_MARGIN, INPUT_MARGIN, config.screen_width-(INPUT_MARGIN*3), config.screen_height-(INPUT_MARGIN*3))

            use input_line
            null height 5
            use input_keyboard

        use input_main_buttons

init -2 python:
    style.input_softkeyboard = Style("frame")
    style.input_softkeyboard.background = "#dcebff"

screen input_line:
    frame:
        xfill True
        vbox:
            label input_label
            xpos 10
            null height 4
            text input_value style "input_line"
            null height 7

init -2 python:
    style.create("input_line", "text")
    style.input_line.size= 35
    style.input_line.xanchor= -10

screen input_main_buttons:
    vbox:
        xpos (config.screen_width-(INPUT_MARGIN*2)-300)
        ypos INPUT_MARGIN

        textbutton main_buttons["confirm"] action Return(input_value) style "input_main_buttons_confirm"
        hbox:
            textbutton main_buttons["default"] action SetVariable("input_value",INPUT_LABEL_DEFAULT)  style "input_main_buttons"
            textbutton main_buttons["clear"] action SetVariable("input_value","")  style "input_main_buttons"

init -2 python:
    style.input_main_buttons = Style("button")
    style.input_main_buttons.xminimum = 150
    style.input_main_buttons.yminimum = 40
    style.input_main_buttons.xmaximum = 150
    style.input_main_buttons.ymaximum = 40

    style.input_main_buttons_confirm = Style("button")
    style.input_main_buttons_confirm.xminimum = 300
    style.input_main_buttons_confirm.yminimum = 55

screen input_nav:
    hbox:
        xfill True

        null width 5
        for dict in softkey_type:
            for k, v in dict.iteritems():
                textbutton input_nav_buttons[k] action [SetVariable("input_alphabet",SetAlphabet(k,v)),SetVariable("input_keyboard",k)]  style "input_nav"

init -2 python:
    style.input_nav = Style("button")
    style.input_nav.size= 40
    style.input_nav.xminimum = 180
    style.input_nav.yminimum = 50

screen input_keyboard:
    frame:
        xfill True
        yfill True

        vbox:
            use input_nav
            null height 10
            hbox:
                null width 15

                use input_keys

screen input_keys:
    hbox:
        xfill True
        for column in input_alphabet:
            grid key_row key_col:
                spacing 7
                for letter in column:
                    if letter is not None:
                        textbutton letter action [SetVariable("input_value", AddLetter(input_value,letter)),SetVariable("input_alphabet",ShiftDown(input_alphabet))] style "keyboard_button"
                    else:
                        null
                for i in range(len(column),key_row*key_col):
                    null

        use input_special

init -2 python:
    style.create("keyboard_button", "button")
    style.keyboard_button.xminimum = 48
    style.keyboard_button.yminimum = 48
    style.keyboard_button_text.size= 22

screen input_special:
    vbox:
        grid 1 2:
            textbutton input_special["backspace"] action SetVariable("input_value",input_value[:-1]) style "keyboard_button_special"
            textbutton input_special["space"] action SetVariable("input_value",input_value+" ") style "keyboard_button_special"
        use input_special_type

init -2 python:
    style.keyboard_button_special = Style("keyboard_button")
    style.keyboard_button_special.xminimum = 125

#EOF
