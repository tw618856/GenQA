# This will test Modify Subset
from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *
from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.parmsHESUB import *


def HESUBModifySubset(em, subset):

    HEDeleteSubset(em, HESubModel, subset)
    HESUBAddSubset(em, subset)

    # Start at Main Menu
    # Now navigate to Subset Management

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Subset Management Modify Subset: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()

    assert em.screen.contains("TIEA13"), "Subset Management Modify Subset: Subset Management not found"

    # Select 2 (Modify Subset)
    em.app.ispf_command("2")
    em.screen.log()
    assert em.screen.contains("TIESMIM"), "Subset Management Modify Subset: Modify Subset not found"

    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset

    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIESUBT"), "Subset Management Modify Subset: Select Scoping Object Type not found"
    # The Business System is already selected so press enter
    em.app.ispf_submit()
    assert em.screen.contains("Input has been accepted"), "Subset Management Modify Subset: Input Accepted failed"
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIESUBT1"), "Subset Management Modify Subset: Object Occurrences not found"
    em.app.ispf_submit()
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("TIESUBRL"), "Subset Management Modify Subset: Subset Definition Summary not found"
    em.screen.log()
    em.screen[6] = "A"
    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("Input has been accepted"), "Subset Management Modify Subset: Input Accepted2 failed"
    em.app.ispf_submit()
    assert em.screen.contains("TIESMIM"), "Subset Management Modify Subset: Modify Subset incomplete"
    assert em.screen.contains("All processing completed normally"), "Subset Management Modify Subset: Modify Subset failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")