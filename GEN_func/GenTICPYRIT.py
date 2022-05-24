# Execute Host Encyclopedia Environment

def GenTICPYRIT(em):

     # Invoke the HE
     em.ispf_app.ispf_command("TSO TICPYRIT", expect_panelid="TICPYRIT")
     assert em.screen.contains("TICPYRIT"),"HE Copyright not found"
     em.submit_screen()
     em.screen.log()



