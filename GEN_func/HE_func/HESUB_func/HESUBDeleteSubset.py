from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *
from GEN_func.HE_func.HEDeleteSubset import *
from GEN_func.HE_func.HESUB_func.parmsHESUB import *

# This tests the Subset Delete


def HESUBDeleteSubset(em, subset):

    # Start at Main Menu
    # Delete the subset, add the subset, and then delete again

    HEDeleteSubset(em, HESubModel, subset)
    HESUBAddSubset(em, subset)
    HEDeleteSubset(em, HESubModel,subset)
