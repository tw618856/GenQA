# This will test Model Rename
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *


def HEMMRenameModel(em):

    # Start at Main Menu
    sampleModel = 'AUT HE MM SAMPLE MODEL'
    renameModel = 'AUT HE MM RENAME MODEL'
    rename2Model = 'AUT HE MM RENAME 2 MODEL'
    HEDeleteModel(em, renameModel)
    HEDeleteModel(em, rename2Model)
    HECopyModel(em,sampleModel, renameModel)

    # Now navigate to Model Management

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Rename Model: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()

    assert em.screen.contains("TIEA12"), "Model Management Rename Model: Model Management not found"

    # Select 1 (Rename Model )
    em.app.ispf_command("7")
    em.screen.log()
    assert em.screen.contains("TIERENMM"), "Model Management Rename Model: Rename Model not found"
    model = 'AUT HE MM RENAME 2 MODEL          '

    em.screen[1] = renameModel
    em.screen[2] = rename2Model

    em.app.ispf_submit()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Rename Model: Model Rename failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")