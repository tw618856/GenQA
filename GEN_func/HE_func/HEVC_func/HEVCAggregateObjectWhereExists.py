from GEN_func.HE_func.HEVC_func.parmsHEVC import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *


# This will test Aggregate Object Where Exists Report

def HEVCAggregateObjectWhereExists(em):

    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Where Exists: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Where Exists: Version Control not found"

    # Select 9 (Agg Obj Report)
    em.app.ispf_command("9")
    em.screen.log()
    assert em.screen.contains("TIVEXSS"), "Version Control Where Exists: Specify Model not found"

    em.screen['Model name'] = HEVCModel
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.screen.log()
    em.submit_screen()


    assert em.screen.contains("TIVSET20"), "Version Control Where Exists: Aggr Set Retrieval failed"
    em.screen['Retrieve aggregate set'] = 'N'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVEXST"), "Version Control Where Exists: Select Agg Obj not found"
    em.screen[2] = '/'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('Input has been accepted'), "Version Control Where Exists: Input accepted not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVEXST1"), "Version Control Where Exists: Obj Occ not found"
    em.screen[2] = 'S'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('TIVEXST1'), "Version Control Where Exists: Obj Occ2 not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('TIVEXSRL'), "Version Control Where Exists: Confirm Report not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('Input has been accepted'), "Version Control Where Exists: Input accepted not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('TIVAGGCF'), "Version Control Where Exists: Confirm Sel Agg Obj not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('IEFFBRO'), "Version Control Where Exists: Browse Report File not found"
    em.screen.log()
    assert em.screen.contains('AGGREGATE OBJECT WHERE EXISTS REPORT'), "Version Control Where Exists: Where Exists Report not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('IEFFPRT'), "Version Control Where Exists: Print Report Options not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('All processing completed normally'), "Version Control Where Exists: All processing not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")