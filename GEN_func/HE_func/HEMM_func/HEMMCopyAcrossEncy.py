
# This tests the Copy Across Encyclopedias


def HEMMCopyAcrossEncy(em):

    # Start at Main Menu
    # We will not be executing the functionality as we don't configure this capability
    # We will just test that we can fill in the values and then Cancel

    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()

    assert em.screen.contains("TIEUTILS"), "Model Management Copy Across Ency: Host Encyclopedia not found"
    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Model Management Copy Across Ency: Model Management not found"

    # Select 2 (Copy Model across Encyclopedias )
    em.app.ispf_command("2")
    em.screen.log()
    assert em.screen.contains("TIEXCPY"), "Model Management Copy Across Ency: Copy Model Across Encyclopedias not found"
    model = 'AUT HE MM SAMPLE MODEL          '
    em.screen['Model name'] = model
    em.screen['Schema level'] = '9.2.A3'

    em.screen['From ency plan prefix '] = 'PRF1'
    em.screen['From ency load library'] = 'AAAC.TEST.LOAD1'
    em.screen['To ency plan prefix'] = 'PRF2'
    em.screen['To ency load library'] = 'AAAC.TEST.LOAD2'
    em.screen.log()
    # Return back to Main Menu
    em.submit_screen("PF12")
    em.submit_screen("PF3")
    em.submit_screen("PF3")
