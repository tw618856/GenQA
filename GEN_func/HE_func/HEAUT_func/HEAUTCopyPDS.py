from ptg2.context import get_userid
# This deletes the automation dataset for the current ID


def HEAUTCopyPDS(em):

    # Start at ISPF Menu
    em.app.ispf_command("=3.3")
    em.screen.log()
    assert em.screen.contains("ISRUMC1"), "Automation Load Copy PDS: Move/Copy Utility From not found"
    prefix = get_userid()
    em.screen['Option ===>'] = 'C'
    em.screen['Name'] = "'AAAC.AG86.QA.MODELS.AUT.S92A6'"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("ISRUMC2B"), "Automation Load Copy PDS: Move/Copy Utility To not found"
    em.screen['Name'] = 'AG86.QA.MODELS.AUT.S92A6'
    em.screen[9] = '2'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("Allocate Target Data Set"), "Automation Load Copy PDS: Allocate Target not found"
    em.screen[1] = '1'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("ISRUMCM1"), "Automation Load Copy PDS: Member List not found"
    em.screen['Command ==>'] = 's *'
    em.submit_screen(wait_for_text='COPIED')
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains("member(s) copied"), "Automation Load Copy PDS: Members not copied"
    em.screen.log()
    em.submit_screen("PF3")
