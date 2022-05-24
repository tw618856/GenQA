from GEN_func.HE_func.HEVC_func.parmsHEVC import *
from GEN_func.HE_func.HEDeleteModel import *

# This is the Migration to a New Model

def HEVCMigratetoNewModel(em, model):

    HEDeleteModel(em, model)

    # Start at Main Menu
    # Now navigate to Version Control
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Version Control Migrate New Model: Host Encyclopedia not found"

    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()
    assert em.screen.contains("TIV001"), "Version Control Migrate New Model: Version Control not found"

    # Select 2
    em.app.ispf_command("2")
    em.screen.log()
    assert em.screen.contains("TIVMIGS"), "Version Control Migrate New Model: Migrate Source not found"

    em.screen['Source model name'] = HEVCModel
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains("TIVCRTD"), "Version Control Migrate New Model: Migrate to New Model not found"
    em.screen["Destination model name"] = model
    em.screen['Range of objects'] = '/'
    em.screen[3] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[5] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("All processing completed normally"), "Version Control Migrate New Model: Migration failed"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")