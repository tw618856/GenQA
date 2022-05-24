from ptg2.context import get_userid

# This is the Backup and Restore Utilities


def HEMMBackupRestoreUtilities(em):

    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Backup Restore: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()

    assert em.screen.contains("TIEA12"), "Model Management Backup Restore: Model Management not found"

    # Select 1 (Copy Model )
    em.app.ispf_command("10")
    em.screen.log()
    assert em.screen.contains("TIEBR"), "Model Management Backup Restore: Backup and Restore Utilities not found"
    em.app.ispf_command("1")
    assert em.screen.contains("TIEBKUP"), "Model Management Backup Restore: Create Sequential Backup not found"

    model = 'AUT HE MM SAMPLE MODEL          '
    qualifier = get_userid()
    em.screen['Model name'] = model
    em.screen['Backup dataset name'] = qualifier + '.hemm.sample'
    em.screen['Cleanup value'] = '1'
    em.screen.log()
    em.submit_screen()

    assert em.screen.contains("ISREDDE2"), "Model Management Backup Restore: JCL not found"
    em.screen.log()
    em.app.ispf_command("cancel")
    em.submit_screen("PF3")
    em.screen.log()

    em.app.ispf_command("2")
    assert em.screen.contains("TIEREST"), "Model Management Backup Restore: Restore Model not found"
    em.screen.log()

    em.screen['Model name'] = model
    em.screen['Restore users/groups'] = 'Y'
    em.screen['Image copy step '] = 'Y'
    em.screen[4] = '1024'
    em.screen['Include STEPLIB for DB2 utilities'] = 'Y'
    em.submit_screen('PF12')
    em.submit_screen('PF12')

    # Return to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
