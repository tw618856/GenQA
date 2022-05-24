from GEN_func.HE_func.HESUB_func.parmsHESUB import *
from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *

# This tests the Consistency Check


def HESUBConsistencyCheck(em, subset):
    # Start at Main Menu
    HEDeleteSubset(em, HESubModel, subset)
    HESUBAddSubset(em, subset)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Subset Management Consistency Check: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA13"), "Subset Management Consistency Check: Model Management not found"

    # Select 7 (Subset Consistency Check)
    em.app.ispf_command("7")
    em.screen.log()
    assert em.screen.contains("TIECCSOP"), "Subset Management Consistency Check: Consistency Check not found"
    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset
    em.screen['Report scope'] = '/'
    em.screen[4] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[6] = '.'
    em.submit_screen()
    assert em.screen.contains("TIECCROP"), "Subset Management Consistency Check: Consistency Check Options not found"
    em.screen['Diagnostic report type'] = 'N'
    em.screen['Diagnostic severity'] = 'W'
    em.screen['Diagnostic threshold'] = '1000'
    em.screen['Diagnostic rule level'] = 'BAA'
    em.screen['DBMS specific rules'] = 'DB2ZOS'
    em.submit_screen(wait_for_text='Browse Report File')
    assert em.screen.contains("IEFFBRO"), "Subset Management Consistency Check: Browse Report not found"
    assert em.screen.contains('Consistency Check Diagnostic Report'), "Subset Management Consistency Check: Consistency Check Report not found"
    assert em.screen.contains('AUT HE SUB SAMPLE MODEL'), "Subset Management Consistency Check: Consistency Check Model not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF12")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")