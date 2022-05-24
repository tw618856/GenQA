def HEBusSysGeneration(em, HETestModel):
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

    # On panel TICMENU@ - "Application System Construction Menu":
    table = em.screen.table()
    table.find_row(
        selectoneoftheoptionsbelowthenpressenter="_ 1. Generate business system")[0] = "1"
    em.ispf_app.ispf_submit(expect_panelid="TICBLDLM")
    em.screen.log()

    # On panel TICBLDLM - "Generate Business System":
    table = em.screen.table()
    table.find_row(modulejob="MENU")[0] = "g"
    em.ispf_app.ispf_submit(expect_panelid="TICBLDGO")
    em.screen.log()

    # On panel TICBLDGO - "Generation Options for MENU":
    em.screen["generatedebugsupport"] = ""
    em.screen["yes"] = "/"
    em.screen["generatedialogmanager"] = "/"
    em.screen["yes-1"] = ""
    em.screen["processmodulesmarkedforcompatibility"] = ""
    em.screen["yes-2"] = "/"
    em.screen["automaticinstallation"] = "/"
    em.screen["yes-3"] = ""
    em.screen["processinforeground"] = "/"
    em.screen["yes-4"] = ""
    em.screen["targettsotestfacility"] = "/"
    em.screen["yes-5"] = ""
    em.screen["remoteinstallation"] = ""
    em.screen["yes-6"] = "/"
    em.screen["forcecompileofallcomponents"] = "/"
    em.screen["yes-7"] = ""
    em.screen["linkeditdynamicallylinkedmodules"] = "/"
    em.screen["yes-8"] = ""
    em.screen["linkeditloadmodule"] = "/"
    em.screen["yes-9"] = ""
    em.screen["binddb2applicationplan"] = "/"
    em.screen["yes-10"] = ""
    em.ispf_app.ispf_submit(expect_panelid="TICCNF2")
    em.screen.log()

    print("Business System generation starting.")

    # On panel TICCNF2 - "Confirm Generation and Installation of MENU":
    # em.ispf_app.ispf_submit(expect_panelid="TICCNF2")

    # On panel TICSDIS - "Menu Generation Status":
    em.ispf_app.ispf_submit(expect_panelid="TICSDIS")
    em.screen.log()

    # Look for Status msg 'INSTALLATION COMPLETE' message and then press enter key.

    # On panel TICSDIS - "MENU Generation Status", press enter:
    em.ispf_app.ispf_submit(expect_panelid="TICBLDLM")
    em.screen.log()

    print("Business System generation complete.")

    # On panel TICBLDLM - "Generate Business System":
    # Look for status msg - 'G-GENERATE OPERATION COMPLETE'

    # On panel TICBLDLM - "Generate Business System":
    # PF3 back to the main menu
    em.screen.fields["command"].focus()
    em.ispf_app.ispf_submit(action="PF3", expect_panelid="TICMENU@",
                            expect_message="User exited from function in progress.")
    em.screen.log()
