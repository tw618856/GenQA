# This tests the Consistency Check


def HEMMConsistencyCheck(em):
    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Consistency Check: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Consistency Check: Model Management not found"

    # Select 2 (Model Statistics)
    em.app.ispf_command("6")
    em.screen.log()
    assert em.screen.contains("TIECCMOP"), "Model Management Consistency Check: Consistency Check not found"
    model = 'AUT HE MM SAMPLE MODEL          '
    em.screen['Model name'] = model
    em.screen['Range of objects'] = '/'
    em.screen[3] = '.'
    em.screen['Execution mode'] = '/'
    em.screen[5] = '.'
    em.submit_screen()
    assert em.screen.contains("TIECCROP"), "Model Management Consistency Check: Consistency Check Options not found"
    em.screen['Diagnostic report type'] = 'N'
    em.screen['Diagnostic severity'] = 'W'
    em.screen['Diagnostic threshold'] = '1000'
    em.screen['Diagnostic rule level'] = 'BAA'
    em.screen['DBMS specific rules'] = 'DB2ZOS'
    em.submit_screen(wait_for_text='Browse Report File')
    assert em.screen.contains("IEFFBRO"), "Model Management Consistency Check: Browse Report not found"
    assert em.screen.contains('Consistency Check Diagnostic Report'), "Model Management Consistency Check: Consistency Check Report not found"
    assert em.screen.contains('AUT HE MM SAMPLE MODEL'), "Model Management Consistency Check: Consistency Check Model not found"
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF12")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")