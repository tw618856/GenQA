from GEN_func.HE_func.HESUB_func.parmsHESUB import *
from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *

# This test will execute Subset Statistics


def HESUBDisplaySubsetStatistics(em, subset):

    HEDeleteSubset(em, HESubModel, subset)
    HESUBAddSubset(em, subset)
    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Subset Management Subset Statistics: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA13"), "Subset Management Subset Statistics: Subset Management not found"

    # Select 10 (Subset Statistics)
    em.app.ispf_command("10")
    em.screen.log()
    assert em.screen.contains("TIESMI"), "Subset Management Subset Statistics: Subset Statistics not found"
    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset
    em.submit_screen()
    assert em.screen.contains("TIESTAT"), "Subset Management Subset Statistics: Subset Statistics Report not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF12")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")