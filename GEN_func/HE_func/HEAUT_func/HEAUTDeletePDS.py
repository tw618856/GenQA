from ptg2.context import get_userid
# This deletes the automation dataset for the current ID


def HEAUTDeletePDS(em):

    # Start at ISPF Menu
    em.app.ispf_command("=3.4")
    em.screen.log()
    prefix = get_userid()
    assert em.screen.contains("ISRUDLP"), "Automation Load Delete PDS: Dataset List Utility not found"
    em.screen['Dsname Level'] = prefix + '.AG86.QA.MODELS.AUT.S92A6'
    em.screen.log()
    em.submit_screen()
    if em.screen.contains("No data set names found"):
        em.screen.log()
    elif em.screen.contains("ISRUDSL0"):
        em.screen.log()
        em.screen[2] = 'd'
        em.screen.log()
        em.submit_screen()
        assert em.screen.contains("Confirm Delete"), "Automation Load Delete PDS: Confirm Delete not found"
        em.screen[1] = '/'
        em.screen.log()
        em.submit_screen()
        assert em.screen.contains("Data set deleted"), "Automation Load Delete PDS: Delete failed"
        em.screen.log()
        em.submit_screen("PF3")
    else:
        assert em.screen.contains("ISRUDSL0"), "Automation Load Delete PDS: DSLIST not found"
    em.submit_screen("PF3")
    em.screen.log()

