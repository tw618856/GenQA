# from ptg2 import zos
# from ptg2.zos import DatasetType, DatasetFormat, DatasetStorage, Dsn
# from ptg2.context import use_system, set_system, get_system, get_userid, set_userid
# from ptg2.zos.eml import get_emulator
# from ptg2.zos.eml_apps import TPXApp, TSOApp, ISPFApp
# import GenLogin
# import GenPanelid
# import GenLogoff
# import GenTICPYRIT
# import GenLogin
from GenLogin import *
from GenPanelid import *
from GenLogoff import *
from GenTICPYRIT import *
# import HE_func.HEMM_func.HEMMSetupModel
# from HE_func.HEMM_func.HEMMSetupModel import *
from HEConstructionTestCases import HEConstructionTestCases
import csv
# import ptg2.zos.jes
# import time
from ptg2.zos.emul import get_emulator
import datetime
from HE_func.HECopyModel import *
from HE_func.HEDeleteModel import *

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

    # Open the output report as HEConstructionReportMMDDYYHHMMSS.csv

    rptDateTime = datetime.datetime.now()
    rptStrDateTime = rptDateTime.strftime('%m%d%Y%H%M%S')
    rptName = 'HEConstructionReport' + rptStrDateTime + '.csv'
    with open(rptName, 'w') as csvfile:
        fieldnames = ['Test', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    # Open the input file
        print('Open and read input file')
        # Previous input file name
        # with open('HETSOConstructionInput.csv', newline='') as csv_file:
        # Open the GEN_MVS_V86C_Models_Execution_Tests spreadsheet
        with open('GEN_MVS_V86C_Models_Execution_Tests.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print('Open write output file')

    # Loop through the input file until EOF
    # On the first record read, we need to start the emulator,
    # and login to the Release and Build provided on the input records
    # We will log in to the HE and set up the test model

            readCount = 0
            # skip first row which is the header row
            next(csv_reader)
            for row in csv_reader:
                if readCount == 0:
                    print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    print('Start emulator')
                    release = row[4]
                    build = row[3]
                    em = get_emulator()
                    print('Starting TSO logon')
                    GenLogin(em, release, build)
                    print('Gen logon complete')
                    GenPanelid(em)
                    print('Executing Copyright command')
                    GenTICPYRIT(em)
                    readCount += 1
                    em.screen.log()

                    # assert em.screen.contains("IEF@PRIM"), "Main Menu not found"
                    # em.screen.log()
                    # Select 1 (Host Encyclopedia functions )
                    # em.app.ispf_command("1")
                    # em.screen.log()

                    # assert em.screen.contains("TIEUTILS"), "Host Encyclopedia not found"
                    # Select 3 (Model Management )
                    # em.app.ispf_command("3")
                    # em.screen.log()

                    # assert em.screen.contains("TIEA12"), "Model Management not found"

                    # For each record read, we will check the RunFlag and if "Y", we will execute the Test Case
                    # The call to a module cannot be done with a string variable, so we will call the test case module
                    # and determine which test call to run with a series of IF statements
                    # Currently, if the logic returns to main, we assume a successful test case and
                    # write out to the output report

                selectFlag = row[2]
                testCase = row[1]
                functionCode = row[0]
                print('readCount', readCount)
                print('select flag', selectFlag)
                if selectFlag == 'YES':
                    writer.writerow({'Test': testCase, 'Status': 'Started'})
                    model = row[5]
                    print('Model Name', model)
                    if model == 'SAMPLE':
                        # Copy the Sample Model
                        GenSampleModel = 'GEN SAMPLE MODEL 8 6            '
                        # HETSOSampleTestModel = 'AUT HE TSO SAMPLE MODEL          '
                        HETestModel = 'AUT HE TSO SAMPLE MODEL          '
                        HEDeleteModel(em, HETestModel)
                        # Navigate to Model Management from Main Menu
                        em.screen.log()
                        HECopyModel(em, GenSampleModel, HETestModel)
                        em.screen.log()
                        assert em.screen.contains("IEF@PRIM"), "Main Menu not found"
                        em.screen.log()

                    # Assign long model name
                    if model == 'ABLK01':
                        HETestModel = 'AUT ABLK01 DB2'
                    if model == 'ABLK01MR':
                        HETestModel = 'AUT ABLK01MR DB2'
                    if model == 'ABLK03':
                        HETestModel = 'AUT ABLK03 DB2'
                    if model == 'ABLK04':
                        HETestModel = 'AUT ABLK04 DB2'
                    if model == 'ABLK06':
                        HETestModel = 'AUT ABLK06 DB2'
                    if model == 'ABLK06MR':
                        HETestModel = 'AUT ABLK06MR DB2'
                    if model == 'ABLK08':
                        HETestModel = 'AUT ABLK08 DB2'
                    if model == 'ABLK09':
                        HETestModel = 'AUT ABLK09 DB2'
                    if model == 'ABLK10':
                        HETestModel = 'AUT ABLK10 DB2'
                    if model == 'ABLK11':
                        HETestModel = 'AUT ABLK11 DB2'
                    if model == 'ABLK12':
                        HETestModel = 'AUT ABLK12 DB2'
                    if model == 'ABLK13':
                        HETestModel = 'AUT ABLK13 DB2'
                    if model == 'ABLK15':
                        HETestModel = 'AUT ABLK15 DB2'
                    if model == 'ABLK24':
                        HETestModel = 'AUT ABLK24 DB2'
                    if model == 'ABLK26':
                        HETestModel = 'AUT ABLK26 DB2'
                    if model == 'ABLK26MR':
                        HETestModel = 'AUT ABLK26MR DB2'
                    if model == 'ABLK27':
                        HETestModel = 'AUT ABLK27 DB2'
                    if model == 'ABLK27MR':
                        HETestModel = 'AUT ABLK27MR DB2'
                    if model == 'ABLK29':
                        HETestModel = 'AUT ABLK29 DB2'
                    if model == 'ABLK30':
                        HETestModel = 'AUT ABLK30 DB2'
                    if model == 'ABLK31':
                        HETestModel = 'AUT ABLK31 DB2'
                    if model == 'ABLK32':
                        HETestModel = 'AUT ABLK32 DB2'
                    if model == 'ABLK32MR':
                        HETestModel = 'AUT ABLK32MR DB2'
                    if model == 'ABLK36':
                        HETestModel = 'AUT ABLK36 DB2'
                    if model == 'ABLK37':
                        HETestModel = 'AUT ABLK37 DB2'
                    if model == 'ABLK38':
                        HETestModel = 'AUT ABLK38 DB2'
                    if model == 'ABLK38DE':
                        HETestModel = 'AUT ABLK38DE DB2'
                    if model == 'ABLK38ND':
                        HETestModel = 'AUT ABLK38ND DB2'
                    if model == 'ABLK42':
                        HETestModel = 'AUT ABLK42 DB2'
                    if model == 'ABLK43':
                        HETestModel = 'AUT ABLK43 DB2'
                    if model == 'ABLK48':
                        HETestModel = 'AUT ABLK48 DB2'
                    if model == 'ABLK49':
                        HETestModel = 'AUT ABLK49 DB2'
                    if model == 'ABLK51':
                        HETestModel = 'AUT ABLK51 DB2'
                    if model == 'ABLK53':
                        HETestModel = 'AUT ABLK53 DB2'
                    if model == 'ABLK57':
                        HETestModel = 'AUT ABLK57 DB2'
                    if model == 'DMGR22':
                        HETestModel = 'AUT DMGR22 DB2'
                    if model == 'IRUN01':
                        HETestModel = 'AUT IRUN01 DB2'
                    if model == 'MAPG01':
                        HETestModel = 'AUT MAPG01 DB2'
                    if model == 'MAPG02':
                        HETestModel = 'AUT MAPG02 DB2'
                    if model == 'TRCE01':
                        HETestModel = 'AUT TRCE01 DB2'

                    # Call the Host Encyclopedia Construction script.
                    HEConstructionTestCases(em, functionCode, HETestModel)

                    # em.submit_screen("PF3")
                    print('Block mode generation finished. About to logoff of TSO.')
                    # em.screen.log()

                    # testCase = 'HEBlockMode'
                    writer.writerow({'Test': testCase, 'Status': 'Complete'})

                else:
                    print(row)
                    readCount += 1

        # Exit from HE (Application System Menu)
        print('Exit from HE')
        em.screen.log()
        # Logoff TSO here
        print("Starting TSO logoff.")
        em = get_emulator()
        GenLogoff(em)
