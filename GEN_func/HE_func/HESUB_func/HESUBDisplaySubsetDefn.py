from GEN_func.HE_func.HESUB_func.parmsHESUB import *
from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *
from GEN_func.HE_func.HEDeleteSubset import *
# This test will execute Subset Definition


def HESUBDisplaySubsetDefinition(em, subset):

    HEDeleteSubset(em, HESubModel, subset)
    HESUBAddSubset(em, subset)
    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Subset Management Subset Definition: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA13"), "Subset Management Subset Definition: Subset Management not found"

    # Select 3 (Subset Definition)
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIESMIS"), "Subset Management Subset Definition: Display Subset Definition not found"

    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset
    em.submit_screen()
    assert em.screen.contains("TIESUBRL"), "Subset Management Subset Definition: Subset Definition Summary not found"
    em.screen.log()

    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")