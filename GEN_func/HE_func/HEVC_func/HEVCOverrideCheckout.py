from ptg2.context import get_userid

# This will test Model Override Checkout

def HEVCOverrideCheckout(em, model):

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Version Control Override Checkout: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Version Control Override Checkout: Model Management not found"


    # Select 9
    em.app.ispf_command("9")
    em.screen.log()
    assert em.screen.contains("TIECKSTM"), "Version Control Override Checkout: Override Checkout Status not found"
    overrideID = get_userid()
    em.screen['Model name'] = model
    em.screen['User ID'] = overrideID
    em.screen.log()
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.screen.log()
    em.submit_screen()
    if (em.screen.contains("This model is not checked out") | em.screen.contains("The model name is not found")):
        em.screen.log()
    else:
        assert em.screen.contains("TIECKSTA"), "Version Control Override Checkout: Override Checkout not found"
        em.app.ispf_submit()
        em.screen.log()
        assert em.screen.contains("All processing completed normally"), "Version Control Override Checkout: Override Checkout failed"


    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")