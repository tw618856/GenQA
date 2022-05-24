from GEN_func.HE_func.HECopyModel import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HEVC_func.parmsHEVC import *

# This copies the Gen Sample Model to a Subset Maintenance Test Model

def HEVCSetupModel(em):
    em.screen.log()
    HEDeleteModel(em, HEVCModel)
    em.screen.log()
    HECopyModel(em,GenSampleModel, HEVCModel)








