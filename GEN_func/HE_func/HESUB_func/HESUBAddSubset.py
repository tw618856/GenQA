from GEN_func.HE_func.HESUB_func.parmsHESUB import *
# This creates a subset


def HESUBAddSubset(em, subset):
    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Subset Management Add Subset: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()

    assert em.screen.contains("TIEA13"), "Subset Management Add Subset: Subset Management not found"

    # Select 1 (Add Subset )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIESMIA"), "Subset Management Add Subset: Subset not found"

    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset
    em.submit_screen()
    assert em.screen.contains("TIESUBT"), "Subset Management Add Subset: Select Scoping Object Types not found"
    em.screen[6] = '/'
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("Input has been accepted"), "Subset Management Add Subset: Select Scoping Object Types not found"
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("TIESUBT1"), "Subset Management Add Subset: Object Occurrences not found"
    em.screen[2] = 'S'
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("TIESUBT1"), "Subset Management Add Subset: Object Occurrences2 not found"
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("TIESUBRL"), "Subset Management Add Subset: Subset Definition not found"
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Subset Management Add Subset: Subset failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
