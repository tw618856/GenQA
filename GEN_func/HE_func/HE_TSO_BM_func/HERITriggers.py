def HERITriggers(em, HETestModel):
    # On panel TICCD01 - "Referential Integrity Trigger Construction":
    em.screen["modelname"] = HETestModel + "          "
    em.ispf_app.ispf_submit(expect_panelid="TICCASC")
    em.screen.log()

    # On panel TICCASC - "Referential Integrity Trigger Construction Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Generate all referential integrity triggers")[0] = "3"
    em.ispf_app.ispf_submit(expect_panelid="TICCASCT")
    em.screen.log()

    # On panel TICCASCT - "Specify RI Trigger Target Environment and Construction Libraries":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Specify RI Trigger Target Environment")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICCASCE")
    em.screen.log()

    # On panel TICCASCE - "Specify RI Trigger Target Environment Parameters":
    em.screen["databasemanagementsystem"] = "db2"
    em.screen["db2subsystemforpackagebinds"] = "dtgp"
    em.screen["tpmonitor"] = "iefae"
    em.screen["dynamicallylinkritriggers"] = "no"
    em.screen["ritriggernamecascade"] = "cascade"
    em.screen["supportfordsnuli"] = "no"
    em.ispf_app.ispf_submit(expect_panelid="TICCASCE")
    em.screen.log()

    # em.control_manually()

    # On panel TICCASCE - "Specify RI Trigger Target Environment Parameters":
    em.ispf_app.ispf_submit(action="PF2", expect_panelid="TICCASCT")
    em.screen.log()

    # On panel TICCASCT - "Specify RI Trigger Target Environment and Construction Libraries":
    table = em.screen.table()
    em.screen.log()
    # table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Specify RI Trigger Target Environment")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICCASCE")
    em.screen.log()

    # On panel TICCASCE - "Specify RI Trigger Target Environment Parameters":
    em.screen["databasemanagementsystem"] = "db2"
    em.screen["db2subsystemforpackagebinds"] = "dtgp"
    em.screen["tpmonitor"] = "iefae"
    em.screen["dynamicallylinkritriggers"] = "no"
    em.screen["supportfordsnuli"] = "no"
    em.ispf_app.ispf_submit(expect_panelid="TICCASCE")
    em.screen.log()

    # On panel TICCASCE - "Specify RI Trigger Target Environment Parameters":
    em.ispf_app.ispf_submit(action="PF2", expect_panelid="TICCASCT",
                            expect_message="Referential integrity trigger target environment accepted.")
    em.screen.log()

    # On panel TICCASCT - "Specify RI Trigger Target Environment and Construction Libraries":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Specify RI Trigger Target Environment")[0] = "2"
    em.ispf_app.ispf_submit(expect_panelid="TICCASCL")
    em.screen.log()

    # On panel TICCASCL - "Specify RI Trigger Libraries":
    # Need to copy and paste the dataset names since it won't type a period.
    em.screen["generatedsourcecode"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.RI.COB'________"
    em.screen["compiledloadmodules"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.RI.LOAD'_______"
    em.screen["db2dbrmmodules"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.RI.DBRM'_______"
    em.screen["installationcontrol"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.RI.INST'_______"
    em.screen["compilelistings"] = "'AAAC.AG86.TJW.SAMP.TSO.LNG3.RI.LIST'_______"
    em.ispf_app.ispf_submit(action="PF6", expect_panelid="TICCASCT",
                            expect_message="Referential integrity trigger libraries saved on encyclopedia.")
    em.screen.log()
    # On panel TICCASCT - "Specify RI Trigger Target Environment and Construction Libraries":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICCASC")
    em.screen.log()

    # On panel TICCASC - "Referential Integrity Trigger Construction Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Generate all referential integrity triggers")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICBLDPO")
    em.screen.log()

    # On panel TICBLDPO - "Referential Integrity Processing Options":
    em.screen["generatetriggers"] = "/"
    em.screen["yes-1"] = "/"
    em.screen["installtriggers"] = "/"
    em.screen["processinforeground"] = "/"
    em.screen["yes-4"] = "/"
    em.screen["forcecompileofalltriggers"] = "/"
    em.ispf_app.ispf_submit(expect_panelid="TICCD02")
    em.screen.log()

    # On panel TICCD02 - "Confirm Referential Integrity Trigger Generation":
    em.ispf_app.ispf_submit(expect_panelid="TICSDIS")
    em.screen.log()

    # On panel TICSDIS - "Generation Status":
    em.ispf_app.ispf_submit(expect_panelid="TICCASC")
    em.screen.log()

    # Look for 'Generation is complete message' and then press enter key.

    # On panel TICCASC - "Referential Integrity Trigger Construction Menu":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICCD01")
    em.screen.log()

    # On panel TICCD01 - "Referential Integrity Trigger Construction":
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TISMENU1")
    em.screen.log()

    # RI trigger generation complete
    print("RI Trigger generation complete.")
    em.screen.log()
