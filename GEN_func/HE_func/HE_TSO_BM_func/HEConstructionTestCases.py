from HE_func.HE_TSO_BM_func.HEBlockMode import *

# This calls the test case based on the input


def HEConstructionTestCases(em, functioncode, HETestModel):
    """ This function evaluates the name of the test case and branches to the proper function. """
    print('Starting Construction')
    if functioncode == 'HE':
        print('Starting HE Block Mode')
        HEBlockMode(em, HETestModel)
#   if functioncode == 'IT':
#       print('Starting IT Construction')
#       ITConstruction(em, HETestModel)
#   if functioncode == 'Batch':
#       print('Starting Batch Construction')
#       HEBatch(em, HETestModel)
