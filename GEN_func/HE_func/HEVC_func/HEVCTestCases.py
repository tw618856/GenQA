from GEN_func.HE_func.HEVC_func.HEVCRenameModelFamily import *
from GEN_func.HE_func.HEVC_func.HEVCMigratetoNewModel import *
from GEN_func.HE_func.HEVC_func.HEVCMigratetoExistingModel import *
from GEN_func.HE_func.HEVC_func.HEVCAdoptModel import *
from GEN_func.HE_func.HEVC_func.HEVCUnadoptModel import *
from GEN_func.HE_func.HEVC_func.HEVCCompareObjects import *
from GEN_func.HE_func.HEVC_func.HEVCTrialMigrateExistingModel import *
from GEN_func.HE_func.HEVC_func.HEVCTrialAdoptionModel import *
from GEN_func.HE_func.HEVC_func.HEVCAggregateObjectWhereExists import *

# This calls the Test Case based on the input


def HEVCTestCases(em,testCase):
     em.screen.log()
     if testCase == 'HEVCRenameModelFamily':
          HEVCRenameModelFamily(em,'AUT HE VC MODEL FAMILY')
     if testCase == 'HEVCMigratetoNewModel':
          HEVCMigratetoNewModel(em,'AUT HE VC NEW MODEL')
     if testCase == 'HEVCMigratetoExistingModel':
          HEVCMigratetoExistingModel(em, "AUT HE VC MIGRATE MODEL")
     if testCase == 'HEVCAdoptModel':
          HEVCAdoptModel(em, 'AUT HE VC ADOPT MODEL')
     if testCase == 'HEVCUnadoptModel':
          HEVCUnadoptModel(em, 'AUT HE VC UNADOPT MODEL')
     if testCase == 'HEVCCompareObjects':
          HEVCCompareObjects(em, 'AUT HE VC COMPARE MODEL')
     if testCase == 'HEVCTrialMigrateExistingModel':
          HEVCTrialMigrateExistingModel(em, 'AUT HE VC TRIAL MIGRATE OBJECTS')
     if testCase == 'HEVCTrialAdoptionModel':
          HEVCTrialAdoptionModel(em, 'AUT HE VC TRIAL ADOPT MODEL')
     if testCase == 'HEVCAggregateObjectWhereExists':
          HEVCAggregateObjectWhereExists(em)




