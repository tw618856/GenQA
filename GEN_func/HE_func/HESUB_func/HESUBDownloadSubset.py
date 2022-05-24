from GEN_func.HE_func.HESUB_func.parmsHESUB import *
from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *

# This test will test Subset Download


def HESUBDownloadSubset(em, subset):

    HEDeleteSubset(em, HESubModel, subset)
    HESUBAddSubset(em, subset)

    # Start at Main Menu
    # Now navigate to Subset Management
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Subset Management Download: Host Encyclopedia not found"

    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()
    assert em.screen.contains("TIEA13"), "Subset Management Download: Subset Management not found"

    # Select 12
    em.app.ispf_command("12")
    em.screen.log()
    assert em.screen.contains("TIEDOWNS"), "Subset Management Download: Download subset not found"

    em.screen['Model name'] = HESubModel
    em.screen['Subset name'] = subset
    em.screen['Software version'] = '9.2.A6'
    em.screen['Transaction file name'] = 'IEF.TRAN'

    em.screen[5] = '/'
    em.screen[6] = '.'
    em.screen['Child ency id'] = ''
    em.screen['Child model name'] = ''
    em.screen['Codepage'] = '1252'
    em.screen['Readonly option'] = '/'
    em.screen[11] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[13] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("IEF OK"), "Subset Management Download: Download failed"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Subset Management Download: Download failed"

    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")