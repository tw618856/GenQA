from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *


# This will test Rename Objects

def HEMMRenameObjects(em):

    # Start at Main Menu

    model = 'AUT HE MM RENAME OBJECTS MODEL'
    HEMMCopyModel(em, model)
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Rename Objects: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Rename Objects: Model Management not found"

    # Select 3 (Delete Objects)
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEDELS"), "Model Management Rename Objects: Rename Objects not found"

    em.screen['Model name'] = model
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIEDELT"), "Model Management Rename Objects: Aggregate Objects not found"

    # Select Attributes
    em.screen[3] = '/'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("Input has been accepted"), "Model Management Rename Objects: Rename Objects selection failed"
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIEDELT1"), "Model Management Rename Objects: Object Occurrences not found"
    em.screen[2] = 'R'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIERNM3"), "Model Management Rename Objects: Rename Aggregate Objects not found"
    em.screen['New Name'] = 'RENAME'
    em.screen['New DSDname'] = 'RENAME'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("ATTRIBUTE DEPARTMENT RENAME"), "Model Management Rename Objects: Rename not found"
    em.screen.log()
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")