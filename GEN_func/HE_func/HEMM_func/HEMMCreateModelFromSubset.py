from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *
from GEN_func.HE_func.HEMM_func.HEMMAddSubset import *
from GEN_func.HE_func.HEDeleteModel import *

# This tests the Create Model from Subset


def HEMMCreateModelFromSubset(em):

    # Start at Main Menu

    model = 'AUT HE MM CREATE MODEL FROM SUB'
    subset = 'SUBSET'
    newModel = 'AUT HE MM NEW MODEL FROM SUB'
    HEMMCopyModel(em, model)
    HEMMAddSubset(em, model, subset)
    HEDeleteModel(em, newModel)
    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Model Management Create Mod from Sub: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Create Mod from Sub: Model Management not found"

    # Select 8
    em.app.ispf_command("8")
    em.screen.log()
    assert em.screen.contains("TIENMDL"), "Model Management Create Mod from Sub: Create model from subset not found"

    em.screen['Current model name'] = model
    em.screen['Current subset name'] = subset
    em.screen['New model name'] = newModel
    em.screen['Execution mode'] = '/'
    em.screen[5] = '.'
    em.submit_screen()
    assert em.screen.contains("All processing completed normally"), "Model Management Create Mod from Sub: Create model failed"
    em.screen.log()

    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")