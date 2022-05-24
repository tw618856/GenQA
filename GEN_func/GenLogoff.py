from ptg2.zos.emul_apps import TSOApp


# Logging off

def GenLogoff(em):

     # On panel ISR@PRIM - "CA CA31 ISPF Primary Option Menu":
     em.screen.log()
     em.ispf_app.ispf_command("=x")

     em.screen.log()
     # Waits until "-->" is on the screen and keyboard is unlocked, screen is submitted using Enter:
     em.submit_screen(wait_for_text="-->")
     em.add_app(TSOApp(em))
     print("Current app: %s" % em.app.name)
     em.app.tso_command("x")
     em.submit_screen()
     em.screen.log()
     # Waits until "-->" is on the screen and keyboard is unlocked, screen is submitted using Enter:
     em.submit_screen(wait_for_text="-->")
     em.app.tso_command("x")
     em.submit_screen()
     em.screen.log()
     em.app.tso_command("logoff")
     em.terminate()