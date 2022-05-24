from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *
from GEN_func.HE_func.HESUB_func.parmsHESUB import *


# This will test Rename Subset

def HESUBRenameSubset(em, subset):

    # Start at Main Menu

    HEDeleteSubset(em, HESubModel, subset)
    HEDeleteSubset(em, HESubModel, subset+"1")
    HESUBAddSubset(em, subset)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Subset Management Rename: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()

    assert em.screen.contains("TIEA13"), "Subset Management Rename: Subset Management not found"

    # Select 5 (Rename Subset )
    em.app.ispf_command("5")
    em.screen.log()
    assert em.screen.contains("TIEREN"), "Subset Management Rename: Rename Subset not found"

    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset

    em.screen['New subset'] = subset+"1"

    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Subset Management Rename: Subset rename failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")