# This creates a subset


def HEMMAddSubset(em, model, subset):
    # Start at Main Menu

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Add Subset: Host Encyclopedia not found"
    # Select 4 (Subset Management )
    em.app.ispf_command("4")
    em.screen.log()

    assert em.screen.contains("TIEA13"), "Model Management Add Subset: Subset Management not found"

    # Select 1 (Add Subset )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIESMIA"), "Model Management Add Subset: Subset not found"

    em.screen['Model name'] = model
    em.screen['Subset name'] = subset
    em.submit_screen()
    assert em.screen.contains("TIESUBT"), "Model Management Add Subset: Select Scoping Object Types not found"
    em.screen[6] = '/'
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("Input has been accepted"), "Model Management Add Subset: Select Scoping Object Types not found"
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("TIESUBT1"), "Model Management Add Subset: Object Occurrences not found"
    em.screen[2] = 'S'
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("TIESUBT1"), "Model Management Add Subset: Object Occurrences2 not found"
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("TIESUBRL"), "Model Management Add Subset: Subset Definition not found"
    em.submit_screen()
    em.screen.log()
    assert em.screen.contains("All processing completed normally"), "Model Management Add Subset: Subset failed"
    # Return back to Main Menu
    em.submit_screen("PF3")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
