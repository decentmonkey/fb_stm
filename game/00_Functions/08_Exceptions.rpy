# Thanks to SadCrab for this code :)

screen IW_exception(can_return, traceback_fn):
    default reportSent = False
    layer "special"
    add "images/Help/error_screen.jpg"
    fixed:
        pos (getRes(170), getRes(50))
        fit_first True
        fixed:
            area (getRes(50), getRes(50), getRes(900), getRes(300))
            frame:
                background Solid("#18181a")
                padding (getRes(50),getRes(50))
                text _("Oops, something went wrong...\n\nPlease, email me {b}decentmonkeybox@gmail.com{/b} and send me the {b}traceback.txt{/b} file located in the game folder. \n\nIf you need more information, be sure to check out my {a=https://www.patreon.com/decentmonkey/overview}Patreon{/a} page, {a=http://decent-monkey.com/}Website{/a} or {a=http://wiki.decent-monkey.com/}Wiki{/a}. Thanks!") style "error_messsage_header_style"

    vbox:
        xanchor 0.5
        xpos getRes(700)
        if gui.flag720 == False:
            yalign 0.8
        else:
            yalign 0.9
        hbox:
            vbox:
                xalign 0.0
                if can_return:
                    button:
                        anchor (0.0,0.5)
                        frame:
                            background Solid("#18181a")
                            margin (0,0)
                            padding (getRes(30),getRes(30))
                            style "sprite_textbutton_frm"
                            text t__("Try to continue") style text_button_layouts["default"]["text_button.style"]
                        action Return("continue")

                button:
                    anchor (0.0,0.5)
                    frame:
                        background Solid("#18181a")
                        margin (0,0)
                        padding (getRes(30),getRes(30))
                        style "sprite_textbutton_frm"
                        text t__("Return to main menu") style text_button_layouts["default"]["text_button.style"]
                    action Return("menu")
                button:
                    anchor (0.0,0.5)
                    frame:
                        background Solid("#18181a")
                        margin (0,0)
                        padding (getRes(30),getRes(30))
                        style "sprite_textbutton_frm"
                        text t__("Exit the game") style text_button_layouts["default"]["text_button.style"]
                    action Return("exit")
            null:
                width getRes(100)

            vbox:
                xalign 0.0
                if not reportSent:
                    button:
                        anchor (0.0,0.5)
                        frame:
                            background Solid("#18181a")
                            margin (0,0)
                            padding (getRes(30),getRes(30))
                            style "sprite_textbutton_frm"
                            text t__("Send report") style text_button_layouts["default"]["text_button.style"]
                        action ToggleScreenVariable("reportSent", False, True), _sendPOST(traceback_fn)
                else:
                    button:
                        anchor (0.0,0.5)
                        frame:
                            background Solid("#18181a")
                            margin (0,0)
                            padding (getRes(30),getRes(30))
                            style "sprite_textbutton_frm"
                            text t__("Done") style text_button_layouts["default"]["text_button.style"]
                        action ToggleScreenVariable("reportSent", False, True)
                button:
                    anchor (0.0,0.5)
                    frame:
                        background Solid("#18181a")
                        margin (0,0)
                        padding (getRes(30),getRes(30))
                        style "sprite_textbutton_frm"
                        text t__("Copy error text") style text_button_layouts["default"]["text_button.style"]
                    action _CopyCollapsedMarkdown(traceback_fn)
                button:
                    anchor (0.0,0.5)
                    frame:
                        background Solid("#18181a")
                        margin (0,0)
                        padding (getRes(30),getRes(30))
                        style "sprite_textbutton_frm"
                        text t__("Open the folder with error file") style text_button_layouts["default"]["text_button.style"]
                    action _OpenFolder(traceback_fn)


define _last_exception_handled = False
init 1000 python:
    class _sendPOST(Action):
        def __init__(self, filename):
            self.filename = filename
        def __call__(self):
            try:
                import urllib
                import urllib2

                with open(self.filename, "rb") as f:
                    f.read(3) # skip the BOM.
                    s = f.read().decode("utf-8")

                s = s.replace("\n", "\r\n")
#                s = s.replace("\r\r", "\r")
#                s = s.replace(" ", "%20")
#                s = s.replace("\r\n", "%0A")

                url = "http://update2.decent-monkey.com/sendreport/send.php"
                values = {"game_version": config.version,"body": "game version: " + config.version + "\n" + s}
                data = urllib.urlencode(values)
                req = urllib2.Request(url, data)
                response = urllib2.urlopen(req)
                the_page = response.read()

            except:
                pass

    class _SendEMail(Action):
        def __init__(self, filename):
            self.filename = filename

        def __call__(self):
            try:
                import webbrowser

                with open(self.filename, "rb") as f:
                    f.read(3) # skip the BOM.
                    s = f.read().decode("utf-8")

                s = s.replace("\n", "\r\n")
                s = s.replace("\r\r", "\r")
                s = s.replace(" ", "%20")
                s = s.replace("\r\n", "%0A")
                url = "mailto:decentmonkeybox@gmail.com?subject=Game%20Traceback&body={}"
                url = url.format(s)
                webbrowser.open_new(url)
            except:
                pass

    class _CopyCollapsedMarkdown(Action):
        def __init__(self, filename):
            self.filename = filename

        def __call__(self):
            import pygame.scrap

            with open(self.filename, "rb") as f:
                f.read(3) # skip the BOM.
                s = f.read().decode("utf-8")

            s = s.replace("\n", "\r\n")
            s = s.replace("\r\r", "\r")
            s = s.encode("utf-8")
            s = "```\n{}```\n".format(s)

            while len(s) > 2000:
                lines = s.split("\r\n")
                third_lines = len(lines) / 3
                lines = lines[:third_lines] + ["One third removed."] + lines[-third_lines:]
                s = "\r\n".join(lines)

            pygame.scrap.put(pygame.SCRAP_TEXT, s)

    class _OpenFolder(Action):
        def __init__(self, filename):
            self.filename = filename

        def __call__(self):
            import os
            try:
                filename = renpy.exports.fsencode(self.filename)
                if os.path.isfile(filename):
                    filename = os.path.dirname(filename)
                os.startfile(filename)
            except:
                pass

    def handle_exception(short, full, filename):
        try:
            import sys
            is_unhandlable = sys.exc_info()[0] is renpy.script.ScriptError
            if _last_exception_handled:
                store._last_exception_handled = False
                is_unhandlable = True

            def IW_exception(can_return, traceback_fn):
                old_quit = renpy.config.quit_action
                try:
                    config.quit_action = None
#                    print "here!!!"
#                    renpy.pause()
                    renpy.show_screen("IW_exception", can_return, traceback_fn, _transient=True)
                    rv = renpy.ui.interact(mouse="screen", type="screen", suppress_overlay=True, suppress_underlay=True)
                    return rv
                finally:
                    config.quit_action = old_quit


            rv = renpy.invoke_in_new_context(IW_exception, not is_unhandlable, filename)
            if rv == "exit":
                raise renpy.game.QuitException(relaunch=False, status=1)
            elif rv == "menu":
                renpy.full_restart(config.game_main_transition)


            store._last_exception_handled = True
            return True
        except renpy.game.CONTROL_EXCEPTIONS:
            raise
        except:
            renpy.display.log.write("While handling exception:")
            renpy.display.log.exception()
            return False

    def check_exception(statement_name):
        if renpy.is_init_phase():
            return

        if statement_name not in ["python"]:
            store._last_exception_handled = False

    config.exception_handler = handle_exception
    config.statement_callbacks.append(check_exception)
