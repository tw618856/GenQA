from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HECopyModel import *

# This copies the Gen Sample Model to a Model Maintenance Test Model


def HEMMSetupModel(em):
    em.screen.log()
    GenSampleModel = 'GEN SAMPLE MODEL 8 6            '
    HEMMSampleTestModel = 'AUT HE MM SAMPLE MODEL          '
    HEDeleteModel(em, HEMMSampleTestModel)
    #Navigate to Model Management from Main Menu
    em.screen.log()
    HECopyModel(em, GenSampleModel, HEMMSampleTestModel)



