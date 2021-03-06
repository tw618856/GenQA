from ptg2.common import set_debug
from ptg2.context import set_system, set_userid
from ptg2.auth import set_password
import sys
from GEN_func.GenLogin import *
from GEN_func.GenPanelid import *
from GEN_func.GenLogoff import *
from GEN_func.GenTICPYRIT import *
from GEN_func.HE_func.HEMM_func.HEMMSetupModel import *
from GEN_func.HE_func.HEMM_func.HEMMTestCases import *
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

# This script reads in a file with test cases
# The test cases have a Run flag of Y or N values - N is default
# The scripts executes the test cases marked with a Run flag of Y
# As the script executes the test, there are error checks and messages will be flagged in the log
# If the script runs successfully, an entry will be written to the output file
# Still need to add logic to determine how to continue after an error

if __name__ == '__main__':
    set_debug(debug)

    # Start timer to track total time for execution
    starttime = time.time()

    # Open the output report as HEMMReportMMDDYYHHMMSS.csv

    rptDateTime = datetime.now()
    rptStrDateTime = rptDateTime.strftime('%m%d%Y%H%M%S')
    rptName = 'HEMMReport' + rptStrDateTime + '.csv'
    with open(rptName, 'w') as csvfile:
        fieldnames = ['Test', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Open the input file

        with open('HEMMInput.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Loop through the input file until EOF
            # On the first record read, we need to start the emulator,
            # and login to the Release and Build provided on the input records
            # We will also login to the HE and setup the main HE Model Management test model

            readCount = 0
            for row in csv_reader:
                if readCount == 0:
                    release = row[0]
                    build = row[1]
                    em = get_emulator()
                    GenLogin(em, release, build)
                    GenPanelid(em)
                    GenTICPYRIT(em)
                    readCount += 1
                    HEMMSetupModel(em)
                    # Navigate to Model Management from Main Menu
                    em.screen.log()

                    assert em.screen.contains("IEF@PRIM"), "Model Management:  Main Menu not found"

                else:
                    readCount += 1

                # For each record read, we will check the RunFlag and if "Y", we will execute the Test Case
                # The call to a module cannot be done with a string variable, so we will call the test case module
                # and determine which test call to run with a series of IF statements
                # Currently if the logic returns back to main, we assume a successful test case and write out to the output report

                runTest = row[3]
                testCase = row[2]
                if runTest == 'Y':
                    HEMMTestCases(em, testCase)
                    writer.writerow({'Test': testCase, 'Status': 'Passed'})

        # em.submit_screen("PF3")
        em.screen.log()

        testCase = 'HE Model Management Test'
        writer.writerow({'Test': testCase, 'Status': 'Complete'})
        totaltime = round((time.time() - starttime), 2)
        testCase = 'Total Time'
        writer.writerow({'Test': testCase, 'Status': str(totaltime)})

        # Exit from HE (Application System Menu)
        em.screen.log()
        GenLogoff(em)
