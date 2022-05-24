from GEN_func.HE_func.HEVC_func.HEVCAdoptModel import *

# This tests the Copy Model option

def HEVCUnadoptModel(em, model):
    # Start at Main Menu
    HEVCAdoptModel(em,model)

    # Now navigate to Model Management

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Unadoption: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Unadoption: Version Control not found"

    # Select 5 (Unadoption)
    em.app.ispf_command("5")
    em.screen.log()
    assert em.screen.contains("TIVUADP"), "Version Control Unadoption: Unadopt not found"

    em.screen['Model name'] = model
    em.screen['New model family name'] = model+'2'
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("All processing completed"), "Version Control Unadoption: Unadoption not successful"
    em.screen.log()
    assert em.screen.contains("TIV001"), "Version Control Unadoption: Version Control Management"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")