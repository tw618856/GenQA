from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *
from GEN_func.HE_func.HEDeleteModel import *
# This will test the Model Upload


def HEMMUploadModel(em):

    model = "AUT HE MM UPLOAD MODEL"
    HEMMCopyModel(em, model)

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Upload: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Upload: Model Management not found"

    # Select 8
    em.app.ispf_command("15")
    em.screen.log()
    assert em.screen.contains("TIEDOWNM"), "Model Management Upload: Download model not found"

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
    em.screen.log()
    assert em.screen.contains("IEF OK"), "Model Management Upload: IEF OK not found"
    em.screen.log()
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Upload: Download failed"
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")

    HEDeleteModel(em,model)

    em.screen.log()
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Upload: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    assert em.screen.contains("TIEA12"), "Model Management Upload: Model Management not found"
    em.screen.log()
    em.app.ispf_command("16")
    # Select 4 (Upload Model )
    assert em.screen.contains("TIEUP"), "Model Management Upload: Upload Model/Subset not found"
    em.screen.log()
    em.screen['Transaction file name'] = 'IEF.TRAN'
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.screen.log()
    em.submit_screen()
    em.submit_screen(wait_for_text="IEF OK")
    assert em.screen.contains("All processing completed normally"), "Model Management Upload: Upload failed"
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()