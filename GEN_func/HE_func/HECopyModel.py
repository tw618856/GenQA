# This can be used by any HE Test to Copy from one model to another model
# This assumes that the from model exists and the destination model does not exist
# Use HEDeleteModel to delete the destination model

def HECopyModel(em,fromModel,toModel):
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
     em.screen.log()

     assert em.screen.contains("TIEA12"),"Model Management not found"
     em.app.ispf_command("1")
     # Select 1 (Copy Model )
     em.screen.log()
     em.app.ispf_submit(expect_panelid="TIECPYM")
     assert em.screen.contains("TIECPYM"),"Copy Model not found"
     em.screen['From model name'] = fromModel
     em.screen['Copy to new name'] = toModel

     em.screen['Execution mode'] = '/'
     em.screen[4] = '.'
     em.screen['New model object history'] = '.'
     em.screen[6] = '/'
     em.screen['Lock encyclopedia tables'] = '.'
     em.screen[8] = '/'
     em.app.ispf_submit()
     em.screen.log()
     assert em.screen.contains("All processing completed normally"),"HEMM Model copy failed"
     # Return back to Main Menu
     em.submit_screen("PF3")
     em.submit_screen("PF3")
     em.submit_screen("PF3")