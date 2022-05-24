from GEN_func.HE_func.HESUB_func.HESUBAddSubset import *
from GEN_func.HE_func.HESUB_func.HESUBModifySubset import *
from GEN_func.HE_func.HESUB_func.HESUBDisplaySubsetDefn import *
from GEN_func.HE_func.HESUB_func.HESUBCopySubset import *
from GEN_func.HE_func.HESUB_func.HESUBRenameSubset import *
from GEN_func.HE_func.HESUB_func.HESUBDeleteSubset import *
from GEN_func.HE_func.HESUB_func.HESUBConsistencyCheck import *
from GEN_func.HE_func.HESUB_func.HESUBDownloadSubset import *
from GEN_func.HE_func.HESUB_func.HESUBChangeSubsetUserID import *
from GEN_func.HE_func.HESUB_func.HESUBOverrideCheckout import *
from GEN_func.HE_func.HESUB_func.HESUBDisplaySubsetStatistics import *

# This calls the Test Case based on the input


def HESUBTestCases(em,testCase):
     em.screen.log()
     if testCase == 'HESUBAddSubset':
          HESUBAddSubset(em,'AUT HE SUB ADD SUBSET')
     if testCase == 'HESUBModifySubset':
          HESUBModifySubset(em,'AUT HE SUB MODIFY SUBSET')
     if testCase == 'HESUBDisplaySubsetDefinition':
          HESUBDisplaySubsetDefinition(em, "AUT HE SUB DEFINITION")
     if testCase == 'HESUBCopySubset':
          HESUBCopySubset(em, 'AUT HE SUB COPY SUBSET')
     if testCase == 'HESUBRenameSubset':
          HESUBRenameSubset(em, 'AUT HE SUB RENAME SUBSET')
     if testCase == 'HESUBDeleteSubset':
          HESUBDeleteSubset(em, 'AUT HE SUB DELETE SUBSET')
     if testCase == 'HESUBConsistencyCheck':
          HESUBConsistencyCheck(em, 'AUT HE SUB CONSISTENCY CHECK')
     if testCase == 'HESUBDownloadSubset':
          HESUBDownloadSubset(em, 'AUT HE SUB DOWNLOAD SUBSET')
     if testCase == 'HESUBChangeSubsetUserID':
          HESUBChangeSubsetUserID(em, 'AUT HE SUB CHG USERID SUBSET')
     if testCase == 'HESUBOverrideCheckout':
          HESUBOverrideCheckout(em, 'AUT HE SUB OVERRIDE SUBSET')
     if testCase == 'HESUBDisplaySubsetStatistics':
          HESUBDisplaySubsetStatistics(em, 'AUT HE SUB STATISTICS')




