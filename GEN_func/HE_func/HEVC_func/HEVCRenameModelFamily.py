from GEN_func.HE_func.HEVC_func.HEVCDownloadUploadModel import *

# This Renames a Model Family

def HEVCRenameModelFamily(em, model):

    #Start at Main Menu
    HEVCDownloadUploadModel(em, model)
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Rename Family: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Rename Family: Version Control not found"

    # Select 1 (Rename Model Family )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIVRENS"), "Version Control Rename Family: Rename Model Family not found"

    em.screen[1] = model
    em.screen[2] = model + "2"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Version Control Rename Family: Rename Model Family failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
