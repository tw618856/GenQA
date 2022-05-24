from ptg2.context import get_userid
from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *


# This will test Model Override Checkout

def HEMMOverrideCheckout(em):

    model = "AUT HE MM OVERRIDE MODEL"
    HEMMCopyModel(em, model)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Override Checkout: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Override Checkout: Model Management not found"

    # Select 15
    em.app.ispf_command("15")
    em.screen.log()
    assert em.screen.contains("TIEDOWNM"), "Model Management Override Checkout: Download model not found"

    em.screen['Model name'] = model
    em.screen['Software version'] = '9.2.A6'
    em.screen['Transaction file name'] = 'IEF.TRAN'
    em.screen['Upload option'] = '/'
    em.screen[5] = '.'
    em.screen['Extract option'] = '/'
    em.screen[7] = '.'
    em.screen['Child ency id'] = ''
    em.screen['Child model name'] = ''
    em.screen['Codepage'] = '1252'
    em.screen['Readonly option'] = '/'
    em.screen['Upload option'] = '/'
    em.screen[12] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[14] = '.'
    em.submit_screen()
    assert em.screen.contains("IEF OK"), "Model Management Override Checkout: Download failed"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Download failed"
    em.submit_screen("PF3")

    # Select 9
    em.app.ispf_command("9")
    em.screen.log()
    assert em.screen.contains("TIECKSTM"), "Model Management Override Checkout: Override Checkout Status not found"
    overrideID = get_userid()
    em.screen['Model name'] = model
    em.screen['User ID'] = overrideID
    em.screen.log()
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.submit_screen()
    assert em.screen.contains("TIECKSTA"), "Model Management Override Checkout: Override Checkout Status failed"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Override Checkout: Override failed"
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")