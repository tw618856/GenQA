
# This test will test Model Conversion


def HEMMModelConversion(em):

    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Conversion: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()

    assert em.screen.contains("TIEA12"), "Model Management Conversion: Model Management not found"

    # Select 1 (Copy Model )
    em.app.ispf_command("11")
    em.screen.log()
    assert em.screen.contains("TIUCVTS"), "Model Management Conversion: Model Conversion Utilities not found"
    model = 'AUT HE MM SAMPLE MODEL          '
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIUCVTS0"), "Model Management Conversion: Model Conversion not found"
    em.screen['Model name'] = model
    em.screen.log()
    em.submit_screen("PF12")

    em.app.ispf_command("2")
    em.screen.log()
    assert em.screen.contains("TIUCVTS1"), "Model Management Conversion: Model Conversion not found"
    em.screen['Model name'] = model
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIUCVTS3"), "Model Management Conversion: Model Conversion not found"
    assert em.screen.contains("MODEL CONVERSION PROCESS BEGINS"), "Model Management Conversion: Conversion message not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("TIUCVTS4"), "Confirm Conversion not found"
    assert em.screen.contains("The model selected for conversion to  9.2.A6    already exists"), "Model Management Conversion: Already converted not found"
    em.screen.log()
    em.submit_screen()
    assert em.screen.contains("IEFFBRO"), "Model Management Conversion: Browse Report not found"
    assert em.screen.contains("MODEL CONVERSION REPORT FOR MODEL"), "Model Management Conversion: Report not found"
    assert em.screen.contains("AUT HE MM SAMPLE MODEL"), "Model Management Conversion: Model not found in report"
    assert em.screen.contains("CONVERSION COMPLETED SUCCESSFULLY"), "Model Management Conversion: Successful message not found in report"
    em.submit_screen("PF3")
    assert em.screen.contains("IEFFPRT"), "Model Management Conversion: Report Print Options not found"
    em.app.ispf_command("D")
    assert em.screen.contains("TIUCVTS1"), "Model Management Conversion: Model Conversion not found"
    assert em.screen.contains("All processing completed normally"), "Model Management Conversion: Success message not found"
    assert em.screen.contains("RETURN CODE = 0, 9.2.A6 MODEL CONVERSION COMPLETED"), "Model Management Conversion: Conversion message not found"
    em.submit_screen("PF12")

    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIUCVTS6"), "Model Management Conversion: Confirm Conversion of ALL not found"
    # PF3 to go back without converting
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")


