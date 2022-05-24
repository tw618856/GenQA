from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *
from GEN_func.HE_func.HEDeleteModel import *

# This tests the Model Delete


def HEMMDeleteModel(em):

    # Start at Main Menu

    model = 'AUT HE MM DELETE MODEL'
    HEMMCopyModel(em, model)
    HEDeleteModel(em, model)

