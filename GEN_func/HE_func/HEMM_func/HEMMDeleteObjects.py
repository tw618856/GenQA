from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *

# This test will delete model objects


def HEMMDeleteObjects(em):
    # Start at Main Menu

    model = 'AUT HE MM DELETE OBJECTS MODEL'
    HEMMCopyModel(em, model)
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Delete Objects: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Delete Objects: Model Management not found"

    # Select 3 (Delete Objects)
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEDELS"), "Model Management Delete Objects: Delete Objects not found"

    em.screen['Model name'] = model
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIEDELT"), "Model Management Delete Objects: Aggregate Objects not found"
    em.submit_screen("PF8")
    em.screen.log()

    # Select Server Manager
    em.screen[26] = '/'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("Input has been accepted"), "Model Management Delete Objects: Delete Objects selection failed"
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIEDELT1"), "Model Management Delete Objects: Object Occurrences not found"
    em.screen[2] = 'D'
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIEDELDC"), "Model Management Delete Objects: Confirm Deletion not found"
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("IEFFBRO"), "Model Management Delete Objects: Browse Report not found"
    assert em.screen.contains('DELETE AGGREGATE OBJECTS REPORT'), "Model Management Delete Objects: Delete Objects Report Title not found"
    assert em.screen.contains('AUT HE MM DELETE OBJECTS MODEL'), "Model Management Delete Objects: Delete Objects Report Model not found"

    em.submit_screen("PF3")
    # Delete the report
    em.app.ispf_command("D")
    em.app.ispf_submit()
    em.screen.log()
    em.submit_screen("PF3")
    em.submit_screen("PF3")