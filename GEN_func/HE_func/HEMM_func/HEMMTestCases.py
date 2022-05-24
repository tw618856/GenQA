from GEN_func.HE_func.HEMM_func.HEMMCopyModel import *
from GEN_func.HE_func.HEMM_func.HEMMCopyAcrossEncy import *
from GEN_func.HE_func.HEMM_func.HEMMDeleteObjects import *
from GEN_func.HE_func.HEMM_func.HEMMRenameObjects import *
from GEN_func.HE_func.HEMM_func.HEMMDeleteModel import *
from GEN_func.HE_func.HEMM_func.HEMMDisplayModelStatistics import *
from GEN_func.HE_func.HEMM_func.HEMMConsistencyCheck import *
from GEN_func.HE_func.HEMM_func.HEMMRenameModel import *
from GEN_func.HE_func.HEMM_func.HEMMCreateModelFromSubset import *
from GEN_func.HE_func.HEMM_func.HEMMOverrideCheckout import *
from GEN_func.HE_func.HEMM_func.HEMMBackupRestoreUtilities import *
from GEN_func.HE_func.HEMM_func.HEMMModelConversion import *
from GEN_func.HE_func.HEMM_func.HEMMModelHistory import *
from GEN_func.HE_func.HEMM_func.HEMMChangeModelUserID import *
from GEN_func.HE_func.HEMM_func.HEMMDownloadModel import *
from GEN_func.HE_func.HEMM_func.HEMMUploadModel import *
# This calls the Test Case based on the input


def HEMMTestCases(em,testCase):
     if testCase == 'HEMMCopyModel':
          HEMMCopyModel(em,'AUT HE MM COPY MODEL')
     if testCase == 'HEMMCopyAcrossEncy':
          HEMMCopyAcrossEncy(em)
     if testCase == 'HEMMDeleteObjects':
          HEMMDeleteObjects(em)
     if testCase == 'HEMMRenameObjects':
          HEMMRenameObjects(em)
     if testCase == 'HEMMDeleteModel':
          HEMMDeleteModel(em)
     if testCase == 'HEMMDisplayModelStatistics':
          HEMMDisplayModelStatistics(em)
     if testCase == 'HEMMConsistencyCheck':
          HEMMConsistencyCheck(em)
     if testCase == 'HEMMRenameModel':
          HEMMRenameModel(em)
     if testCase == 'HEMMCreateModelFromSubset':
          HEMMCreateModelFromSubset(em)
     if testCase == 'HEMMOverrideCheckout':
          HEMMOverrideCheckout(em)
     if testCase == 'HEMMBackupRestoreUtilities':
          HEMMBackupRestoreUtilities(em)
     if testCase == 'HEMMModelConversion':
          HEMMModelConversion(em)
     if testCase == 'HEMMModelHistory':
          HEMMModelHistory(em)
     if testCase == 'HEMMChangeModelUserID':
          HEMMChangeModelUserID(em)
     if testCase == 'HEMMDownloadModel':
          HEMMDownloadModel(em)
     if testCase == 'HEMMUploadModel':
          HEMMUploadModel(em)



