from GEN_func.HE_func.HEVC_func.parmsHEVC import *
from GEN_func.HE_func.HECopyModel import *
from GEN_func.HE_func.HEDeleteModel import *

# This will test Compare Objects

def HEVCCompareObjects(em, model):

    # Start at Main Menu
    HEDeleteModel(em, model)
    HECopyModel(em, HEVCModel, model)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control Compare Report: Host Encyclopedia not found"
    # Select 2 (Version Control)
    em.app.ispf_command("2")
    em.screen.log()

    assert em.screen.contains("TIV001"), "Version Control Compare Report: Version Control not found"

    # Select 6 (Compare Report)
    em.app.ispf_command("6")
    em.screen.log()
    assert em.screen.contains("TIVCMPS"), "Version Control Compare Report: Compare Source Model not found"

    em.screen['Source model name'] = HEVCModel
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains("TIVCMPD"), "Version Control Compare Report: Compare Destination Model failed"
    em.screen['Destination model name'] = model
    em.screen['Range of Objects'] = '/'
    em.screen[3] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[5] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVSET22"), "Version Control Compare Report: Compare Rpt Aggr Set failed"
    em.screen['Save in aggregate set'] = 'N'
    em.screen['Aggregate set name'] = ''
    em.screen[3] = '/'
    em.screen[4] = '.'
    em.screen[5] = '.'
    em.screen[6] = '/'
    em.screen[7] = '.'
    em.screen[8] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIVCMPAL"), "Version Control Compare Report: Confirm Model Names not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains('IEFFBRO'), "Version Control Compare Report: Browse Report File not found"
    em.screen.log()
    assert em.screen.contains('COMPARE AGGREGATE OBJECTS'), "Version Control Compare Report: Compare Report not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('IEFFPRT'), "Version Control Compare Report: Print Report Options not found"
    em.screen.log()
    em.submit_screen("PF3")
    assert em.screen.contains('All processing completed normally'), "Version Control Compare Report: All processing not found"
    em.screen.log()
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")