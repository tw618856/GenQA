from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *
from GEN_func.HE_func.HEDeleteModel import *
from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.parmsHESUB import *

# This tests deletes all subsets for the subset test model


def HESUBDeleteAllSubsets(em):

    # Start at Main Menu
    # navigate to subset maintenance
    # override and delete all subsets

    em.screen.log()
    assert em.screen.contains("IEF@PRIM"), "Subset Delete All: Main Menu not found"
    em.screen.log()

    for row in subsetList:
        HEDeleteSubset(em, HESubModel, row)
        print('Row',row)
        em.screen.log()

