from GEN_func.GenLogin import *
from GEN_func.GenPanelid import *
from GEN_func.GenLogoff import *
from GEN_func.GenTICPYRIT import *
from GEN_func.HE_func.HEAUT_func.HEAUTCopyPDS import *
from GEN_func.HE_func.HEAUT_func.HEAUTDeletePDS import *
from GEN_func.HE_func.HEAUT_func.HEAUTUploadModel import *
import csv
from ptg2.zos.emul import get_emulator
from datetime import *
import time

# Copyright (c) 2022 Broadcom. All rights reserved. The term 'Broadcom'
# refers to Broadcom Inc., and/or its subsidiaries.
#
# This software and all information contained therein is confidential and
# proprietary and shall not be duplicated, used, disclosed or disseminated
# in any way except as authorized by the applicable license agreement,
#  without the express written permission of Broadcom. All authorized reproductions
# must be marked with this language.
#
# EXCEPT AS SET FORTH IN THE APPLICABLE LICENSE AGREEMENT, TO THE EXTENT
# PERMITTED BY APPLICABLE LAW, BROADCOM PROVIDES THIS SOFTWARE WITHOUT
# WARRANTY OF ANY KIND, INCLUDING WITHOUT LIMITATION, ANY IMPLIED
# WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.  IN
# NO EVENT WILL BROADCOM BE LIABLE TO THE END USER OR ANY THIRD PARTY FOR ANY
# LOSS OR DAMAGE, DIRECT OR INDIRECT, FROM THE USE OF THIS SOFTWARE,
# INCLUDING WITHOUT LIMITATION, LOST PROFITS, BUSINESS INTERRUPTION,
# GOODWILL, OR LOST DATA, EVEN IF BROADCOM IS EXPRESSLY ADVISED OF SUCH LOSS OR
# DAMAGE.

# This script loads the automation models
# The production list of models are found on dataset AAAC.AG86.QA.MODELS.AUT.S92A6
# Models must be uploaded by the userid logged on
# The production list is copied to a new dataset prefixed by the logged on userid
# Each model is a member of the dataset and is uploaded one by one


if __name__ == '__main__':

    # Start timer to track total time for execution
    starttime = time.time()

    # Open the output report as HEAUTReportMMDDYYHHMMSS.csv

    rptDateTime = datetime.now()
    rptStrDateTime = rptDateTime.strftime('%m%d%Y%H%M%S')
    rptName = 'HEAUTReport' + rptStrDateTime + '.csv'
    with open(rptName, 'w') as csvfile:
        fieldnames = ['Test', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Open the input file

        with open('HEAUTInput.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Loop through the input file until EOF
            # On the first record read, we need to start the emulator,
            # and login to the Release and Build provided on the input records

            readCount = 0
            for row in csv_reader:
                if readCount == 0:
                    release = row[0]
                    build = row[1]
                    em = get_emulator()
                    GenLogin(em, release, build)
                    GenPanelid(em)

                    readCount += 1
                    HEAUTDeletePDS(em)
                    HEAUTCopyPDS(em)
                    # Navigate to Model Management from Main Menu
                    em.screen.log()
                    GenTICPYRIT(em)
                    assert em.screen.contains("IEF@PRIM"), "Model Management:  Main Menu not found"

                else:
                    readCount += 1

                # For each record read, we will check the RunFlag and if "Y", we will upload the model
                # Currently if the logic returns back to main, we assume a successful upload and write out to the output report

                runTest = row[3]
                model = row[2]
                if runTest == 'Y':
                    HEAUTUploadModel(em, model)
                    writer.writerow({'Test': model, 'Status': 'Uploaded'})

        # em.submit_screen("PF3")
        em.screen.log()

        test = 'HE Automation Upload'
        writer.writerow({'Test': test, 'Status': 'Complete'})
        totaltime = round((time.time() - starttime), 2)
        test = 'Total Time'
        writer.writerow({'Test': test, 'Status': str(totaltime)})

        # Exit from HE (Application System Menu)
        em.screen.log()
        GenLogoff(em)
