# This deletes a model

def HEDeleteModel(em,model):
     # Start at Main Menu
     em.screen.log()

     assert em.screen.contains("IEF@PRIM"),"Main Menu not found"
     em.screen.log()
     # Select 1 (Host Encyclopedia functions )
     em.app.ispf_command("1")
     em.screen.log()

     assert em.screen.contains("TIEUTILS"),"Host Encyclopedia not found"
     # Select 3 (Model Management )
     em.app.ispf_command("3")
     assert em.screen.contains("TIEA12"),"Model Management not found"
     em.screen.log()
     em.app.ispf_command("4")
     # Select 4 (Delete Model )
     assert em.screen.contains("TIESTMDL"),"Delete Model not found"
     em.screen['Model name'] = model
     em.screen['Execution mode'] = '/'
     em.screen[3] = '.'
     em.screen['Lock encyclopedia tables'] = '.'
     em.screen[5] = '/'
     em.screen['Flag model for future delete'] = '/'
     em.screen[7] = '.'
     em.submit_screen()
     em.screen.log()

     if em.screen.contains("The model name is not found") == False:
          em.submit_screen(wait_for_text="All processing completed normally")

     # Return back to Main Menu
     em.submit_screen("PF3")
     em.submit_screen("PF3")
     em.submit_screen("PF3")





