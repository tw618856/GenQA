from ptg2.context import get_userid
from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *

# This is the Change Model User ID


def HEMMChangeModelUserID(em):

    model = "AUT HE MM CHANGE USER MODEL"
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Change Userid: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Change Userid: Model Management not found"

    # Override the checkout status
    em.app.ispf_command("9")
    em.screen.log()
    assert em.screen.contains("TIECKSTM"), "Model Management Change Userid: Override Checkout Status not found"
    overrideID = get_userid()
    em.screen['Model name'] = model
    em.screen['User ID'] = overrideID
    em.screen.log()
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.submit_screen()

    if em.screen.contains("This model is not checked out"):
        em.screen.log()
    elif em.screen.contains("This model/subset is not checked out to user"):
        em.screen.log()
        if overrideID == "QAGEN":
            em.screen['User ID'] = "QAGEN008"
            em.screen.log()
            em.submit_screen()
            assert em.screen.contains("All processing completed normally"), "Model Management Change Userid: Override Checkout failed"
        elif em.screen.contains('TIECKSTA'):
            em.screen.log()
            em.submit_screen()
            assert em.screen.contains("All processing completed normally"), "Model Management Change Userid: Override Checkout failed"
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    HEMMCopyModel(em, model)

    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Change Userid: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Change Userid: Model Management not found"

    # Select 15
    em.app.ispf_command("15")
    em.screen.log()
    assert em.screen.contains("TIEDOWNM"), "Model Management Change Userid: Download model not found"

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
    assert em.screen.contains("IEF OK"), "Download failed"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Change Userid: Download failed"
    em.submit_screen("PF3")

    # Select 14
    em.app.ispf_command("14")
    em.screen.log()
    assert em.screen.contains("TIEMODU"), "Model Management Change Userid: Change Model Checkout not found"
    loggedInID = get_userid()
    if loggedInID == 'QAGEN008':
        overrideID = 'QAGEN'
    else:
        overrideID = 'QAGEN008'
    em.screen['Model name'] = model
    em.screen['New checkout user ID'] = overrideID
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("All processing completed normally"), "Model Management Change Userid: Change Checked ID failed"
    em.screen['New checkout user ID'] = loggedInID
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("All processing completed normally"), "Model Management Change Userid: Change back ID failed"
    em.screen.log()
    em.submit_screen("PF3")

    # Select 9
    em.app.ispf_command("9")
    em.screen.log()
    assert em.screen.contains("TIECKSTM"), "Model Management Change Userid: Override Checkout Status not found"

    em.screen['Model name'] = model
    em.screen['User ID'] = loggedInID
    em.screen.log()
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.submit_screen()
    assert em.screen.contains("TIECKSTA"), "Model Management Change Userid: Override Checkout Status failed"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Change Userid: Override Checkout failed"

    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")