# from ptg2 import zos
# from ptg2.zos import DatasetType, DatasetFormat, DatasetStorage, Dsn
# from ptg2.context import use_system, set_system, get_system, get_userid, set_userid
# from ptg2.zos.emul import get_emulator
# from ptg2.zos.emul import *
# import ptg2.zos.emul
# from ptg2.zos.emul_apps import TPXApp, TSOApp, ISPFApp
# from GenLogin import *
# from GenPanelid import *
# from GenLogoff import *
# from GenTICPYRIT import *
from HERITriggers import *
from HEBusSysGeneration import *
from datetime import *
from ptg2.zos.jes import *
import time
# import csv


def HEBlockMode(em, HETestModel):

    # System & Userid were set in the environment variables section
    # using the variables PTG_SYSTEM, PTG_USERID
    # Password it already set, as I have updated using the PTG_AUTH
    print(get_system())
    print(get_userid())

    # def set_target_parms(em):
    # em.screen["operatingsystem"] = "MVS"
    # em.screen["generatedsourcelanguage"] = "COBOL"
    # em.screen["databasemanagementsystem"] = "DB2"
    # em.screen["tpmonitor"] = "IEFAE"
    # em.screen["screenformattype"] = "BYPASS"
    # em.screen["profiletype"] = "SQL"
    # em.screen["extendedattributesupport"] = "YES"
    # em.screen["enforcedmconstraints"] = "NO"
    # em.screen["optimizeimportviewinitialization"] = "NO"
    # em.screen["restartableapplication"] = "YES"
    # em.screen["clearscreendefaultcommand"] = "RESET"
    # em.screen["db2subsystem"] = "DTGP"
    # em.screen["supportfordsnuli"] = "NO"
    # em.screen["dynamicallylinkproceduresteps"] = "NO"
    # em.screen["dynamicallylinkactionblocks"] = "NO"
    # em.screen["dynamicallylinkscreenmanagers"] = "NO"
    # em.screen["pseudoconversationalsupport"] = "NO"
    # em.screen["handlecicscommandabends"] = "YES"
    # em.screen["xctlforflowswhenpossible"] = "NO"
    # release = "GEN86"
    # build = "H1"

    # if __name__ == '__main__':
    # Start a 3270 emulator and do automatic login to TSO:
    # em = get_emulator()
    # em.screen.log()
    # GenLogin(em,release,build)
    # print('Login to TSO')
    # GenPanelid(em)
    # print('Copyright')
    # GenTICPYRIT(em)
    # Enter the QA logon CLIST command at the Ready prompt
    # em.app.tso_command("ex 'AAAC.DEV.QALOGON.R86.CLIST(QATEST00)'")
    # em.screen.log()
    # Waits until "-->" is on the screen and keyboard is unlocked, screen is submitted using Enter:
    # em.submit_screen(wait_for_text="-->")
    # Now enter the required option (For example : H8 )
    # em.app.tso_command("H8")
    # Waits until a field is on the screen and keyboard is unlocked, screen is submitted using Enter:
    # em.screen.log()
    # em.submit_screen()
    # After entering into HE Environment, convert the current app to ISPF from TSO
    # print("Current app: %s" % em.app.name)
    # em.add_app(ISPFApp(em))
    # print("Current app: %s" % em.app.name)
    # Turn on the Panel id
    # em.app.ispf_command("panelid on")
    # em.app.ispf_command("TSO GENHE")
    # Press enter on GEN HE screen (it appears for the first time on logon)
    # em.submit_screen()
    # em.screen.log()
    print("Current panel: Gen 8.6 HE Main Menu.")

    # We are at the HE Main Menu, so we need to call new script here

    # em.control_manually()

    table = em.screen.table()
    table.find_row(
            selectoneoftheoptionsbelowthen="_ 1. Host Encyclopedia functions")[0] = "4"
    em.ispf_app.ispf_submit(expect_panelid="TISMENU1")
    em.screen.log()

    # On panel TISMENU1 - "Application System Menu":
    table = em.screen.table()
    table.find_row(
            selectoneoftheoptionsbelowthenpressenter="_ 1. Application system construction")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICMSEL")
    em.screen.log()

    # On panel TICMSEL - "Application System Construction":
    em.screen["modelname"] = HETestModel
    em.screen["businesssystemname"] = "corporate_management"
    em.ispf_app.ispf_submit(expect_panelid="TICMENU@",
                            expect_message="Target environment and libraries retrieved.")
    em.screen.log()

    print("Current panel: Application System Construction Menu.")

    print("Current panel: Starting setup for Bus Sys target variables before DDL generation.")

    # Need to set the Business System target variables before starting DDL generation.

    # On panel TICMENU@ - "Application System Construction Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Generate business system")[0] = "5"
    em.ispf_app.ispf_submit(expect_panelid="TICBLB")
    em.screen.log()

    # On panel TICBLB - "Specify Target Environment and Construction Libraries":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Specify Target Environment")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICBLBP")
    em.screen.log()

    # On panel TICBLBP - "Specify Target Environment Parameters":
    em.screen["operatingsystem"] = "mvs"
    em.screen["generatedsourcelanguage"] = "cobol"
    em.screen["databasemanagementsystem"] = "db2"
    em.screen["tpmonitor"] = "iefae"
    em.screen["screenformattype"] = "bypass"
    em.screen["profiletype"] = "sql"
    em.screen["extendedattributesupport"] = "yes"
    em.screen["enforcedmconstraints"] = "no"
    em.screen["optimizeimportviewinitialization"] = "no"
    em.screen["restartableapplication"] = "yes"
    em.screen["clearscreendefaultcommand"] = "reset"
    em.screen["db2subsystem"] = "dtgp"
    em.screen["supportfordsnuli"] = "no"
    em.screen["dynamicallylinkproceduresteps"] = "no"
    em.screen["dynamicallylinkactionblocks"] = "no"
    em.screen["dynamicallylinkscreenmanagers"] = "no"
    em.screen["pseudoconversationalsupport"] = "no"
    em.screen["handlecicscommandabends"] = "no"
    em.screen["xctlforflowswhenpossible"] = "no"
    em.ispf_app.ispf_submit(expect_panelid="TICBLBP")
    em.screen.log()

    # On panel TICBLBP - "Specify Target Environment Parameters":
    em.ispf_app.ispf_submit(action="PF6", expect_panelid="TICBLB",
                            expect_message="Target environment saved on encyclopedia.")
    em.screen.log()

    # On panel TICBLB - "Specify Target Environment and Construction Libraries":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Specify Target Environment")[0] = "2"
    em.ispf_app.ispf_submit(expect_panelid="TICBLBM")
    em.screen.log()

    # On panel TICBLBM - "Specify Construction Libraries":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Specify internal libraries")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICBLB1")
    em.screen.log()

    # On panel TICBLB1 - "Specify Internal Libraries":
    em.screen["generatedsourcecode"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.COBOL'"
    em.screen["ncalloadmodules"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.NCAL'"
    em.screen["executableloadmodules"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.LOAD'"
    em.screen["execbatchdynamablibrary"] = "                                            "
    em.screen["dsnulidynamablibrary"] = "                                            "
    em.screen["db2dbrmmodules"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.DBRM'"
    em.screen["installationcontrol"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.INSTC'"
    em.screen["bindercontrolcards"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.BINDCTL'"
    em.screen["batchbindercontrolcards"] = "                                            "
    em.screen["dsnulibindercontrolcards"] = "                                            "
    em.screen["generatedmfs"] = "                                            "
    em.screen["generatedbatchjcl"] = "                                            "
    em.screen["compilelistings"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.LISTING'"
    em.ispf_app.ispf_submit(expect_panelid="TICBLB1")
    em.screen.log()

    # On panel TICBLB1 - "Specify Internal Libraries":
    em.ispf_app.ispf_submit(action="PF6", expect_panelid="TICBLBM",
                            expect_message="Internal libraries saved on encyclopedia.")
    em.screen.log()

    # On panel TICBLBM - "Specify Construction Libraries":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICBLB")
    em.screen.log()

    # On panel TICBLB - "Specify Target Environment and Construction Libraries":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICMENU@")
    em.screen.log()

    print("Select DDL generation panel.")

    # On panel TICMENU@ - "Application System Construction Menu":
    table = em.screen.table()
    table.find_row(
            selectoneoftheoptionsbelowthenpressenter="_ 1. Generate business system")[0] = "4"
    em.ispf_app.ispf_submit(expect_panelid="TIDDLDB")
    em.screen.log()

    print("Begin setup for DDL generation.")

    # On panel TIDDLDB - "Data Base List":
    em.screen["localorremoteinstall"] = "l"
    em.screen["gendb"] = "a"
    em.ispf_app.ispf_submit(expect_panelid="TIDDLOP1")
    em.screen.log()

    # On panel TIDDLOP1 - "DDL Options":
    em.screen["qualifynamewithownerid"] = "n"
    em.screen["issuedropbeforecreate"] = "y"
    em.screen["createstoragegroup"] = "n"
    em.ispf_app.ispf_submit(expect_panelid="TIDDLALL")
    em.screen.log()

    # On panel TIDDLALL - "Generated DDL text":
    em.ispf_app.ispf_submit(expect_panelid="TIDDLJCE")
    em.screen.log()

    # On panel TIDDLJCE - "JCL Job Statement Information Input":
    em.ispf_app.ispf_submit(expect_panelid="ISREDDE2")
    em.screen.log()

    # On panel ISREDDE2 - "QAGEN008.TICTEMP1.TIDDLJCL":
    em.ispf_app.ispf_command(
        "C GENDB QAGEN8DB ALL", expect_panelid="ISREDDE2", expect_message="CHARS 'GENDB' changed")
    em.screen.log()

    # On panel ISREDDE2 - "QAGEN008.TICTEMP1.TIDDLJCL":
    output = em.ispf_app.ispf_command("SUB")
    # assert output == [' IKJ56250I JOB QAGEN8DB(JOB65561) SUBMITTED']
    # assert output == ['IKJ56250I JOB QAGEN8DB']
    # assert output == ['SUBMITTED']
    em.screen.log()

    # On panel ISREDDE2 - "QAGEN008.TICTEMP1.TIDDLJCL":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TIDDLDB")
    em.screen.log()

    # On panel TIDDLDB - "Data Base List":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICMENU@",
                            expect_message="User exited from function in progress.")
    em.screen.log()

    print("DDL generation in progress.")

    # On panel TICMENU@ - "Application System Construction Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICMSEL")
    em.screen.log()

    # On panel TICMSEL - "Application System Construction":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TISMENU1")
    em.screen.log()

    # On panel TISMENU1 - "Application System Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="IEF@PRIM")
    em.screen.log()

    # On panel IEF@PRIM - "Main Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="ISR@PRIM")
    em.screen.log()

    # On panel ISR@PRIM - "CA CA31 ISPF Primary Option Menu":
    em.ispf_app.ispf_command("V", expect_panelid="GSVX000P",
                    expect_message="GSVX942I CA SYSVIEW 16.0 0990 GSVX Copyright (c) 2021 Broadcom. All rights res+")
    em.screen.log()

    # On panel GSVX000P - "MENU, Primary Option Menu":
    em.ispf_app.ispf_command("ST", expect_panelid="GSVX000P")
    em.screen.log()

    # On panel GSVX000P - "JOBSUM.DETAIL, Job Status":
    em.ispf_app.ispf_command("PREFIX QAGEN8*", expect_panelid="GSVX000P",
                             expect_message="PRFX002I Prefixes are QAGEN8*")
    em.screen.log()

    # On panel GSVX000P - "JOBSUM.DETAIL, Job Status":
    em.ispf_app.ispf_submit(expect_panelid="GSVX000P")
    em.screen.log()

    print("Wait 60 seconds for DDL install job to finish executing.")

    # Wait for 60 seconds
    time.sleep(60)

    # em.control_manually()

    # On panel GSVX000P - "JOBSUM.DETAIL, Job Status":
    # Look for status of job to change to HELDCLS
    # em.ispf_app.ispf_submit(expect_panelid="GSVX000P")
    # em.screen.log()

    print("DDL generation complete.")

    em.ispf_app.ispf_submit(expect_panelid="GSVX000P")
    em.screen.log()

    # On panel GSVX000P - "MENU, Primary Option Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="GSVX000P")

    # On panel GSVX000P - "MENU, Primary Option Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="GSVX000P",
                    expect_message="GSVX197A Enter RETURN command to terminate - Enter anything else to continue")

    # On panel GSVX000P - "MENU, Primary Option Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="ISR@PRIM")

    # em.control_manually()

    # On panel GSVX000P - "MENU, Primary Option Menu":
    # em.screen.fields["command"].focus()
    # em.ispf_app.ispf_submit(action="PF2", expect_panelid="TICCASCT")
    # em.screen.log()

    # On panel ISR@PRIM - "CA CA31 ISPF Primary Option Menu":
    em.ispf_app.ispf_command("tso ticpyrit", expect_panelid="IEF@PRIM")
    em.screen.log()

    # On panel IEF@PRIM - "Main Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthen="_ 1. Host Encyclopedia functions")[0] = "4"
    em.ispf_app.ispf_submit(expect_panelid="TISMENU1")
    em.screen.log()

    # On panel TISMENU1 - "Application System Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Application system construction")[0] = "3"
    em.ispf_app.ispf_submit(expect_panelid="TICCD01")
    em.screen.log()

    # Call the RI Trigger generation script here
    HERITriggers(em, HETestModel)

    # Call Business System Generation here
    HEBusSysGeneration(em, HETestModel)

    # On panel TICMENU@ select option 2 - "Application System Construction Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Generate business system")[0] = "2"
    em.ispf_app.ispf_submit(expect_panelid="TICAEFT")
    em.screen.log()

    print("Application runtime execution starting.")

    # em.control_manually()

    # On panel TICAEFT - "Application Test Facility":
    em.screen["endfunctionkey"] = "pf6"
    em.screen["db2subsystem"] = "dtgp"
    em.submit_screen()
    em.screen.log()

    # On panel ? - "Application Test Facility":
    em.screen["unnamed-1"] = "MENU"
    em.submit_screen(wait_for_text="MAIN MENU")
    em.screen.log()

    # On panel MENU - "CA Gen Sample Model - Online":
    em.screen["1"] = "1"
    em.submit_screen(wait_for_text="MDIV")
    # em.ispf_app.ispf_submit(expect_panelid="MDIV")
    em.screen.log()

    # On panel MDIV - "DIVISION MAINTENANCE":
    em.screen["unnamed-1"] = "a"
    em.screen["div"] = "001"
    em.screen["divisionname"] = "division 1"
    em.ispf_app.ispf_submit(expect_panelid="MDIV")
    em.screen.log()

    # On panel MDIV - "DIVISION MAINTENANCE":
    table = em.screen.table()
    table.row_above_header["divisionname"] = "01"
    table.find_row(act="")[0] = "l"
    em.ispf_app.ispf_submit(expect_panelid="MDEP")
    em.screen.log()

    # On panel MDEP - "DEPARTMENT MAINTENANCE":
    em.screen["ac"] = "a"
    em.screen["unnamed-1"] = "001"
    em.screen["unnamed-2"] = "0001"
    em.screen["departmentname"] = "department 1"
    em.ispf_app.ispf_submit(expect_panelid="MDEP")
    em.screen.log()

    # On panel MDEP - "DEPARTMENT MAINTENANCE":
    # Wait for 5 seconds
    time.sleep(5)
    em.screen["ac"] = "l"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE MAINTENANCE":
    em.screen["ac"] = "a"
    em.screen["div"] = "001"
    em.screen["dept-1"] = "0001"
    em.screen["emp-1"] = "111111"
    em.screen["employeename"] = "employee 111111"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE DETAIL MAINTENANCE":
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE DETAIL MAINTENANCE":
    em.screen["fulltime"] = "y"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    print("First record added.")

    # On panel MEMP - "EMPLOYEE DETAIL MAINTENANCE":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="MENU")
    em.screen.log()

    print("Back to Main Menu.")

    print("Start adding second record.")

    # Adding Division 2
    em.screen["1"] = "1"
    em.ispf_app.ispf_submit(expect_panelid="MDIV")
    em.screen.log()

    # On panel MDIV - "DIVISION MAINTENANCE":
    em.screen["unnamed-1"] = "a"
    em.screen["001-1"] = "002"
    em.screen["division1"] = "division 2"
    em.ispf_app.ispf_submit(expect_panelid="MDIV")
    em.screen.log()

    # On panel MDIV - "DIVISION MAINTENANCE":
    table = em.screen.table()
    table.find_row(act="")[0] = "l"
    em.ispf_app.ispf_submit(expect_panelid="MDEP")
    em.screen.log()

    # em.control_manually()

    # On panel MDEP - "DEPARTMENT MAINTENANCE":
    em.screen["unnamed-2"] = "a"
    em.screen["001"] = "002"
    em.screen["0001-1"] = "0002"
    em.screen["department1"] = "department 2"
    em.ispf_app.ispf_submit(expect_panelid="MDEP")

    # On panel MDEP - "DEPARTMENT MAINTENANCE":
    em.screen["ac"] = "l"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE MAINTENANCE":
    em.screen["ac"] = "a"
    em.screen["div"] = "002"
    em.screen["dept-1"] = "0002"
    em.screen["emp-1"] = "222222"
    em.screen["employeename"] = "employee 222222"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # em.control_manually()

    # On panel MEMP - "EMPLOYEE DETAIL MAINTENANCE":
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE DETAIL MAINTENANCE":
    em.screen["fulltime"] = "y"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE DETAIL MAINTENANCE":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="MENU")
    em.screen.log()

    print("Second record added.")

    print("Starting delete of second record.")

    # On panel MENU - "CA Gen Sample Model - Online":
    em.screen["1"] = "3"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    # On panel MEMP - "EMPLOYEE MAINTENANCE":
    em.screen["002"] = "d"
    em.ispf_app.ispf_submit(expect_panelid="MEMP")
    em.screen.log()

    print("Second employee deleted.")

    # On panel MEMP - "EMPLOYEE MAINTENANCE":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="MENU")
    em.screen.log()

    # On panel MENU - "CA Gen Sample Model - Online":
    em.screen["1"] = "2"
    em.ispf_app.ispf_submit(expect_panelid="MDEP")
    em.screen.log()

    # On panel MDEP - "DEPARTMENT MAINTENANCE":
    em.screen["002"] = "d"
    em.ispf_app.ispf_submit(expect_panelid="MDEP")
    em.screen.log()

    print("Second department deleted.")

    # On panel MDEP - "DEPARTMENT MAINTENANCE":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="MENU")
    em.screen.log()

    # On panel MENU - "CA Gen Sample Model - Online":
    em.screen["1"] = "1"
    em.ispf_app.ispf_submit(expect_panelid="MDIV")
    em.screen.log()

    # em.control_manually()

    # On panel MDIV - "DIVISION MAINTENANCE":
    table = em.screen.table()
    table.row_above_header["divisionname"] = "002"
    em.ispf_app.ispf_submit(expect_panelid="MDIV")

    table = em.screen.table()
    table.find_row(act="")[0] = "d"
    em.ispf_app.ispf_submit(expect_panelid="MDIV")
    em.screen.log()

    print("Second division deleted.")

    # On panel MDIV - "DIVISION MAINTENANCE":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="MENU")
    em.screen.log()

    # On panel MENU - "CA Gen Sample Model - Online":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="MENU")
    em.screen.log()

    print("Back to the main menu.")

    print("Second record deleted.")

    print("Application runtime execution complete.")

    # em.control_manually()

    # On panel MENU - "CA Gen Sample Model - Online":
    # PF15 to exit back to blank screen
    # em.screen["1"]="PF6"
    # On panel MENU - "CA Gen Sample Model - Online":
    em.ispf_app.ispf_submit(action="PF6")
    # em.ispf_app.ispf_submit(action="PF1", expect_panelid="MENU")

    print("Exit back to blank screen.")

    # On panel "Application Test Facility": - Blank screen
    # PF15 to exit back to "Application Test Facility"
    em.ispf_app.ispf_submit(action="PF6", expect_panelid="TICAEFT")
    # em.screen["1"]="PF15"
    em.screen.log()

    print("Exit back to Application Test Facility screen.")

    # On panel TICAEFT - "Application Test Facility":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICMENU@")
    em.screen.log()

    # On panel TICMENU@ - "Application System Construction Menu":
    # Need to go back to the TSO Main Menu
    # em.screen.fields["command"].focus()
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICMSEL")

    # On panel TICMSEL - "Application System Construction":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TISMENU1")

    # On panel TISMENU1 - "Application System Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="IEF@PRIM")

    # On panel IEF@PRIM - "Main Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="ISR@PRIM")

    # Should be at TSO Main Menu
    # CA CA31 ISPF Primary Option Menu
    print("Back to the TSO main menu.")

    # em.control_manually()
