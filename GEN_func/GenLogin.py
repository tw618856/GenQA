from ptg2.zos.emul_apps import ISPFApp

# starting the emulator and logging in


def GenLogin(em, release, build):

    em.screen.log()

    em.app.tso_command("ex 'aaac.dev.qalogon.clist(qatest00)'")
    em.screen.log()

    # Waits until "-->" is on the screen and keyboard is unlocked, screen is submitted using Enter:
    em.submit_screen(wait_for_text="-->")

    # Now enter the required option (For example : GEN86 )
    print("                ")
    print("Current release: " + release)
    print("                ")
    em.app.tso_command(release)
    em.screen.log()
    assert em.screen.contains("BUILD MENU"),"Invalid Panelid"

    # Waits until "-->" is on the screen and keyboard is unlocked, screen is submitted using Enter:
    em.submit_screen(wait_for_text="-->")

    # Now enter the required option (For example : H1 )
    print("                ")
    print("Current build: " + build)
    print("                ")
    em.app.tso_command(build)

    # Waits until a field is on the screen and keyboard is unlocked, screen is submitted using Enter:
    em.screen.log()
    em.submit_screen()

    # After entering into Hx Environment, convert the current app to ISPF from TSO
    print("Current app: %s" % em.app.name)
    em.add_app(ISPFApp(em))
    print("Current app: %s" % em.app.name)
    em.screen.log()
    assert em.screen.contains("ISPF Primary Option Menu"),"Invalid Panelid"
