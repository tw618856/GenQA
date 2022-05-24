# This test will execute Model Statistics


def HEMMDisplayModelStatistics(em):

    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Model Statistics: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Model Statistics: Model Management not found"

    # Select 2 (Model Statistics)
    em.app.ispf_command("5")
    em.screen.log()
    assert em.screen.contains("TIESTC"), "Model Management Model Statistics: Model Statistics not found"
    model = 'AUT HE MM SAMPLE MODEL          '
    em.screen['Model name'] = model
    em.submit_screen()
    assert em.screen.contains("TIESTATM"), "Model Management Model Statistics: Model Statistics Report not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF12")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")