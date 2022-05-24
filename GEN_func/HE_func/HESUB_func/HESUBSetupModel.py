from GEN_func.HE_func.HESUB_func.HESUBDeleteAllSubsets import *
from GEN_func.HE_func.HECopyModel import *
from GEN_func.HE_func.HESUB_func.parmsHESUB import *


# This copies the Gen Sample Model to a Subset Maintenance Test Model


def HESUBSetupModel(em):
    em.screen.log()

    # Override and Delete all subsets

    HESUBDeleteAllSubsets(em)
    HEDeleteModel(em, HESubModel)
    em.screen.log()
    HECopyModel(em,GenSampleModel, HESubModel)








