from GEN_func.HE_func.HEVC_func.parmsHEVC import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *

# This tests the Migration to Existing Model


def HEVCMigratetoExistingModel(em, model):
    # Start at Main Menu
    HEDeleteModel(em, model)
    HECopyModel(em, HEVCModel, model)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Migration Existing Model: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Migration Existing Model: Version Control not found"

    # Select 3 (Migrate)
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIVMIGS"), "Version Control Migration Existing Model: Migrate Source Model Name not found"

    em.screen['Source model name'] = HEVCModel
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains("TIVMIGD"), "Version Control Migration Existing Model:  Migrate Destination not found"
    em.screen['Destination model name'] = model
    em.screen['Max num of protection errors'] = '10'
    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVSET20"), "Version Control Migration Existing Model: Aggr Set Retrieval not found"
    em.screen['Retrieve aggregate set'] = 'N'

    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVMIGT"), "Version Control Migration Existing Model: Select Agg Obj Types not found"
    em.screen[2] = '/'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('Input has been accepted'), "Version Control Migration Existing Model: Input not accepted not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVMIGT1"), "Version Control Migration Existing Model: Obj Occ not found"
    em.screen[2] = 'S'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVMIGT1"), "Version Control Migration Existing Model: Obj Occ2 not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVMIGRL"), "Version Control Migration Existing Model: Confirm Migr List not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('Input has been accepted'), "Version Control Migration Existing Model: Conf Migr List2 not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('TIVAGGCF'), "Version Control Migration Existing Model: Confirm Sel Agg Obj not found"
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains('IEFFBRO'), "Version Control Migration Existing Model: Browse Report File not found"
    em.screen.log()
    assert em.screen.contains('MIGRATE AGGREGATE OBJECT REPORT'), "Version Control Migration Existing Model: Migrate Report not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('IEFFPRT'), "Version Control Migration Existing Model: Print Report Options not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('All processing completed normally'), "Version Control Migration Existing Model: All processing not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")