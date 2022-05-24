from GEN_func.HE_func.HEDeleteModel import HEDeleteModel

# This tests the Copy Model option


def HEMMCopyModel(em, toModel):
    # Start at Main Menu

    HEDeleteModel(em, toModel)

    # Now navigate to Model Management

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Copy: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()

    assert em.screen.contains("TIEA12"), "Model Management Copy: Model Management not found"

    # Select 1 (Copy Model )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIECPYM"), "Model Management Copy: Copy Model not found"
    fromModel = 'AUT HE MM SAMPLE MODEL          '

    em.screen['From model name'] = fromModel
    em.screen['Copy to new name'] = toModel

    em.screen['Execution mode'] = '/'
    em.screen[4] = '.'
    em.screen['New model object history'] = '.'
    em.screen[6] = '/'
    em.screen['Lock encyclopedia tables'] = '.'
    em.screen[8] = '/'
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Copy: Model copy failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
