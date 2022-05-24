from GEN_func.HE_func.HEVC_func.parmsHEVC import *
from GEN_func.HE_func.HEVC_func.HEVCOverrideCheckout import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *

# This will Download a model with upload to create an update.trn


def HEVCDownloadUploadModel(em, model):
    HEVCOverrideCheckout(em, model)
    # copy model, download model w upl, delete model, upload
    HEDeleteModel(em, model)
    HECopyModel(em, HEVCModel, model)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Version Control New Model: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Version Control New Model: Model Management not found"

    # Select 8
    em.app.ispf_command("15")
    em.screen.log()
    assert em.screen.contains("TIEDOWNM"), "Version Control New Model: Download model not found"

    em.screen['Model name'] = model
    em.screen['Software version'] = '9.2.A6'
    em.screen['Transaction file name'] = 'IEF.TRAN'
    em.screen['Upload option'] = '.'
    em.screen[5] = '/'
    em.screen['Extract option'] = '/'
    em.screen[7] = '.'
    em.screen['Child ency id'] = ''
    em.screen['Child model name'] = ''
    em.screen['Codepage'] = '1252'
    em.screen['Readonly option'] = '/'

    em.screen[12] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[14] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("IEF OK"), "Version Control New Model: IEF OK not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("All processing completed normally"), "Version Control New Model: Download failed"
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")

    HEDeleteModel(em,model)

    em.screen.log()
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Version Control New Model: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    assert em.screen.contains("TIEA12"), "Version Control New Model: Model Management not found"
    em.screen.log()
    em.app.ispf_command("16")
    # Select 4 (Upload Model )
    assert em.screen.contains("TIEUP"), "Version Control New Model: Upload Model not found"
    em.screen.log()
    em.screen['Transaction file name'] = 'IEF.TRAN'
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.screen.log()
    em.submit_screen()
    em.submit_screen(wait_for_text="IEF OK")
    assert em.screen.contains("All processing completed normally"), "Version Control New Model: Upload model failed"
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()