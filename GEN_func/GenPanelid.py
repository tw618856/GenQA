# Display Panelid

def GenPanelid(em):

     # Turn on the Panel id
     em.ispf_app.ispf_command("panelid", expect_panelid="ISR@PRIM")
     em.screen.log()
     assert em.screen.contains("ISR@PRIM"),"Invalid Panelid"


