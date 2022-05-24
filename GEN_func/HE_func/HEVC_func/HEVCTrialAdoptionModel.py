from GEN_func.HE_func.HEVC_func.HEVCDownloadUploadModel import *


# This will test Rename Objects

def HEVCTrialAdoptionModel(em, model):
    # Start at Main Menu
    HEDeleteModel(em, model)
    HECopyModel(em, HEVCModel, model)
    HEVCDownloadUploadModel(em, model)

    # Now navigate to Model Management

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Trial Adoption: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Trial Adoption: Version Control not found"

    # Select 8 (Trial Adoption)
    em.app.ispf_command("8")
    em.screen.log()
    assert em.screen.contains("TIVTADS"), "Version Control Trial Adoption: Trial Adoption Adoptee not found"

    em.screen['Adoptee model name'] = HEVCModel
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVTADD"), "Version Control Trial Adoption: Trial Adoption Related Model not found"
    em.screen['Related model name'] = model
    em.screen['Range of objects'] = '/'
    em.screen[3] = '.'
    em.screen[4] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[6] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVTADAL"), "Version Control Trial Adoption: Confirm Parameters not found"
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains('IEFFBRO'), "Version Control Trial Adoption: Browse Report File not found"
    em.screen.log()
    assert em.screen.contains('TRIAL ADOPT MODEL/OBJECTS REPORT'), "Version Control Trial Adoption: Adoption Report not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('IEFFPRT'), "Version Control Trial Adoption: Print Report Options not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('All processing completed normally'), "Version Control Trial Adoption: All processing not found"
    em.screen.log()
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")