from GEN_func.HE_func.HEVC_func.parmsHEVC import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *

# This will test Rename Objects

def HEVCTrialMigrateExistingModel(em, model):

    # Start at Main Menu
    HEDeleteModel(em, model)
    HECopyModel(em, HEVCModel, model)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Trial Migration: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Trial Migration: Version Control not found"

    # Select 7 (Trial Migrate)
    em.app.ispf_command("7")
    em.screen.log()
    assert em.screen.contains("TIVTMGS"), "Version Control Trial Migration: Migrate Source Model Name not found"

    em.screen['Source model name'] = HEVCModel
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains("TIVTMGD"), "Version Control Trial Migration:  Migrate Destination not found"
    em.screen['Destination model name'] = model
    em.screen['Max num of protection errors'] = '10'
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVSET20"), "Version Control Trial Migration: Aggr Set Retrieval not found"
    em.screen['Retrieve aggregate set'] = 'N'

    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVTMGT"), "Version Control Trial Migration: Select Agg Obj Types not found"
    em.screen[2] = '/'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('Input has been accepted'), "Version Control Trial Migration: Input not accepted not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVTMGT1"), "Version Control Trial Migration: Obj Occ not found"
    em.screen[2] = '/'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVTMGT1"), "Version Control Trial Migration: Obj Occ2 not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVTMGRL"), "Version Control Trial Migration: Confirm Migr List not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('Input has been accepted'), "Version Control Trial Migration: Input not acc2 not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('TIVAGGCF'), "Version Control Trial Migration: Confirm Sel Agg Obj not found"
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains('IEFFBRO'), "Version Control Trial Migration: Browse Report File not found"
    em.screen.log()
    assert em.screen.contains('TRIAL MIGRATE AGGREGATE OBJECT REPORT'), "Version Control Trial Migration: Migrate Report not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('IEFFPRT'), "Version Control Migration Existing Model: Print Report Options not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('All processing completed normally'), "Version Control Trial Migration: All processing not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")