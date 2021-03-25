init python:
    def check_saves_for_migration():
        global renpy
        saves_directory = os.path.join(renpy.config.savedir, "")
        old_saves_directory = saves_directory.replace("fashionbusiness1_renpy", "TestProj-1525113205")
        if os.path.exists(old_saves_directory):
            return True
        return False

    def migrate_saves():
        global renpy
        saves_directory = os.path.join(renpy.config.savedir, "")
        old_saves_directory = saves_directory.replace("fashionbusiness1_renpy", "TestProj-1525113205")
        for r, d, f in os.walk(old_saves_directory):
            for file in f:
                in_filename = os.path.join(r, file)
                out_filename = os.path.join(saves_directory, file)
                print in_filename
                print out_filename
                copyfile(in_filename, out_filename)
        return True


label migrate_saves:
    call screen confirm(message="Your current saves will be overwritten.\nAre you sure?", yes_action=Return(1), no_action=Return(0))
    $ print _return
    if _return == 1:
        $ migrate_saves()
    $ renpy.full_restart()
#    $ MainMenu(confirm=False)()
    return
