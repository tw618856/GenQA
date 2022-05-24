from GEN_func.HE_func.HEVC_func.HEVCDownloadUploadModel import *


# This tests the Adopt Model option

def HEVCAdoptModel(em, model):
    # Start at Main Menu
    HEVCDownloadUploadModel(em, model)

    # Now navigate to Model Management

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Adoption: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Adoption: Version Control not found"

    # Select 4 (Adoption)
    em.app.ispf_command("4")
    em.screen.log()
    assert em.screen.contains("TIVADPS"), "Version Control Adoption: Adoption Adoptee not found"

    em.screen['Adoptee model name'] = HEVCModel
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVADPD"), "Version Control Adoption: Adoption Related Model not found"
    em.screen['Related model name'] = model
    em.screen['Range of objects'] = '/'
    em.screen[3] = '.'
    em.screen[4] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[6] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVADPAL"), "Version Control Adoption: Confirm Parameters not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('IEFFBRO'), "Version Control Adoption: Browse Report File not found"
    em.screen.log()
    assert em.screen.contains('ADOPT MODEL/OBJECTS REPORT'), "Version Control Adoption: Adoption Report not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('IEFFPRT'), "Version Control Adoption: Print Report Options not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('All processing completed normally'), "Version Control Adoption: All processing not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")