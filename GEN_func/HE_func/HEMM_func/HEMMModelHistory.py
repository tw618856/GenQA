from ptg2.context import get_userid

# This test will test Model History Reports


def HEMMModelHistory(em):

    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management History: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management History: Model Management not found"

    # Select 12 (Model History)
    em.app.ispf_command("12")
    em.screen.log()
    assert em.screen.contains("TIEMH2"), "Model Management History: Model History not found"
    model = 'AUT HE MM SAMPLE MODEL'

    # Select Model Activity History
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEMH"), "Model Management History: Model Activity History not found"
    em.screen['Model name'] = '***** NONE - SET MAX *****'
    em.screen['Type / by a sort option'] = '/'
    em.screen[3] = '.'
    em.screen[4] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIEMHACT"), "Model Management History: Model Activity Selection List not found"
    em.screen[2] = '/'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIEMHD5"), "Model Management History: Detailed Activity not found"
    em.submit_screen()
    em.submit_screen("PF3")

    # Select Maximum object ID update activity
    em.app.ispf_command("2")
    em.screen.log()
    assert em.screen.contains("TIEHACT"), "Model Management History: Maximum Object ID Update Activity not found"
    em.screen[2] = '/'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIEMHD5"), "Model Management History: Detailed Activity for Model History not found"
    em.submit_screen()
    em.submit_screen("PF3")

    # Select Archive history data
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEMHARC"), "Model Management History: Parameters for Archiving not found"
    qualifier = get_userid()
    em.screen['Number of days of history data to keep'] = '1'
    em.screen['Archive dataset'] =  qualifier + '.hemm.archist'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("ISREDDE2"),"Model Management History: JCL not found"
    em.submit_screen("PF3")
    em.submit_screen("PF3")

    # Select Enable/Disable
    em.app.ispf_command("4")
    em.screen.log()
    assert em.screen.contains("TIEHOFF"), "Model Management History: Enable or Disable not found"
    em.screen['Model name'] = model
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIEMHOFF"), "Model Management History: Object History Logging not found"
    em.screen['Object change history'] = '/'
    em.screen[2] = ''
    em.screen['Object migrate history'] = '/'
    em.screen[4] = ''
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("All processing completed normally"), "Model Management History: Object History Logging not complete"
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")